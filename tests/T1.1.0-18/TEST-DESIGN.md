# T1.1.0-18 Test Design

The selector's visible ROM array is one-based (`1..U`), while RBCP host-visible
flash slots are zero-based (`0..U-1`). Therefore the flash slot associated
with current menu item `G` is `G-1`.

T18 obtains the current active RAM slot from `GET_RAM_SLOT_INFO_ALL`, obtains
the boot metadata through `GET_BOOT_SLOT_INFO`, and calculates `CF=G-1`. It
requires the calculated menu flash to equal the returned boot flash for this
unchanged-menu test.

The diagnostic displays the candidate pair `current RAM, menu flash`. It never
reaches or sends the resident `LOAD_AND_EXIT` helper. Closing DOS channel 15
does not repair the displaced response area, so power cycle remains required.
