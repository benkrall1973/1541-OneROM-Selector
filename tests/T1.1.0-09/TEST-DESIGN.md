# T1.1.0-09 Test Design

The only functional change from T08 is removal of the mandatory device-9 file operations at lines 3564–3569. The verified on-screen query remains, followed by a safe checkpoint and the original Save finalization pathway.

This isolates the next question: whether Q can reliably reuse the proven Save pathway when `C` is reset to the original active entry `G` and all name-edit flags are cleared.
