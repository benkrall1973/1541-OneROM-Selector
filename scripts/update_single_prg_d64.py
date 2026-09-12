#!/usr/bin/env python3
"""Replace the only PRG in a D64 while reusing its sector chain."""

from pathlib import Path
import argparse


SECTORS_PER_TRACK = [0, *([21] * 17), *([19] * 7), *([18] * 6), *([17] * 5)]


def offset(track: int, sector: int) -> int:
    if not (1 <= track <= 35 and 0 <= sector < SECTORS_PER_TRACK[track]):
        raise ValueError(f"invalid D64 track/sector {track}/{sector}")
    return (sum(SECTORS_PER_TRACK[1:track]) + sector) * 256


def petscii_name(text: str, width: int) -> bytes:
    raw = text.upper().encode("ascii")[:width]
    return raw + bytes([0xA0]) * (width - len(raw))


def set_free(image: bytearray, track: int, sector: int, free: bool) -> None:
    bam = offset(18, 0) + 4 + (track - 1) * 4
    mask = 1 << (sector & 7)
    index = bam + 1 + sector // 8
    was_free = bool(image[index] & mask)
    if was_free == free:
        return
    if free:
        image[index] |= mask
        image[bam] += 1
    else:
        image[index] &= 0xFF ^ mask
        image[bam] -= 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_d64", type=Path)
    parser.add_argument("prg", type=Path)
    parser.add_argument("output_d64", type=Path)
    parser.add_argument("--file-name", default="ONEROMV110")
    parser.add_argument("--disk-name", default="ONEROM V1.1.0")
    args = parser.parse_args()

    image = bytearray(args.source_d64.read_bytes())
    if len(image) != 174848:
        raise ValueError("expected a standard 35-track D64")
    payload = args.prg.read_bytes()

    entries = []
    track, sector = image[offset(18, 0)], image[offset(18, 0) + 1]
    while track:
        base = offset(track, sector)
        for slot in range(8):
            entry = base + 2 + slot * 32
            if image[entry] & 0x07:
                entries.append(entry)
        track, sector = image[base], image[base + 1]
    if len(entries) != 1 or (image[entries[0]] & 0x07) != 2:
        raise ValueError("expected exactly one PRG directory entry")

    entry = entries[0]
    chain = []
    track, sector = image[entry + 1], image[entry + 2]
    seen = set()
    while track:
        if (track, sector) in seen:
            raise ValueError("loop in PRG sector chain")
        seen.add((track, sector))
        chain.append((track, sector))
        base = offset(track, sector)
        track, sector = image[base], image[base + 1]

    needed = (len(payload) + 253) // 254
    if needed > len(chain):
        for candidate_track in range(1, 36):
            if candidate_track == 18:
                continue
            for candidate_sector in range(SECTORS_PER_TRACK[candidate_track]):
                if len(chain) >= needed:
                    break
                bam_entry = offset(18, 0) + 4 + (candidate_track - 1) * 4
                bitmap_index = bam_entry + 1 + candidate_sector // 8
                bitmap_mask = 1 << (candidate_sector & 7)
                if image[bitmap_index] & bitmap_mask:
                    set_free(image, candidate_track, candidate_sector, False)
                    chain.append((candidate_track, candidate_sector))
            if len(chain) >= needed:
                break
        if len(chain) < needed:
            raise ValueError("replacement PRG does not fit available D64 sectors")

    for index, (track, sector) in enumerate(chain[:needed]):
        base = offset(track, sector)
        chunk = payload[index * 254:(index + 1) * 254]
        image[base + 2:base + 256] = bytes(254)
        image[base + 2:base + 2 + len(chunk)] = chunk
        if index + 1 < needed:
            next_track, next_sector = chain[index + 1]
            image[base] = next_track
            image[base + 1] = next_sector
        else:
            image[base] = 0
            image[base + 1] = len(chunk) + 1

    for track, sector in chain[needed:]:
        image[offset(track, sector):offset(track, sector) + 256] = bytes(256)
        set_free(image, track, sector, True)

    image[entry + 3:entry + 19] = petscii_name(args.file_name, 16)
    image[entry + 30] = needed & 0xFF
    image[entry + 31] = needed >> 8
    bam = offset(18, 0)
    image[bam + 0x90:bam + 0xA0] = petscii_name(args.disk_name, 16)
    args.output_d64.parent.mkdir(parents=True, exist_ok=True)
    args.output_d64.write_bytes(image)


if __name__ == "__main__":
    main()
