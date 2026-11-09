I answered the one question and amended the claims file.

**neurons-recorded** (claims file changed): The criterion was wrong to assign units to regions by electrode name.
- **What the paper does:** its Methods say contacts "were normalized to the MNI space and assigned to a brain region using the Brainnetome Atlas" and were verified by the neurosurgeon. Fig. 1D colours regions by "the positions of all electrode tips, i.e., the positions of the microelectrodes". The data descriptor adds that labels outside an MTL structure were entered by hand, and it lists an "Anatomical label updated after visual inspection of MRI" among the deposited data.
- **New criterion:** a unit's region now comes from the tip contact of its electrode, read two ways: (a) the hand-updated anatomical label, (b) the Brainnetome label. The electrode name (AH/PH, EC, A) is kept only as a variant.
- **Also in the answer:** the author must work out from the data which deposited contact is the tip. The counts stay exact, and this region assignment applies to every claim that groups neurons by region.
- **Marked** `answered: 2026-10-30`.

The quote check passes for all 34 quotes, but `tools/claims_check.py` reports one problem: the p-value 5e-05 in `behavior-rt-correct-incorrect` is not found in the text and needs confirming by reading. That claim is one I didn't edit. Nothing is committed.
