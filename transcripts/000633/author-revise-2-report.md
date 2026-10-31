No outcomes changed, and I proposed none. `python tools/entry.py all entries/000633-kim-2023` passes (0 errors; the notebook ran in 154 s), and every number the corrected text cites matches the new run. Nothing is committed.

**What I corrected, by verifier point**
- **fig4bc:** now flagged `assumed: true`. The assumption that the single-pulse file is the image of Figure 4A is stated in a deviation, the result cell and the summary.
- **fig4-comet-shape, "extents agree":** that statement in deviation 3 was wrong and is corrected. At half maximum, without the bright objects, the extent along the line is smaller than across it (2446 vs 2592 µm at 10× and 20×, 2446 vs 2473 µm at 5×). The notes, result cell and summary now say the half-maximum pass depends on the reach measure.
- **"One object left out":** now says the pixels on objects bright in MemBrite are left out (0.54% of the region, several objects). Fixed in the README, summary, result heading, deviation and the question to the authors.
- **Cell 15, "taken from the figure, no longer circular":** withdrawn. The text now says:
  - where Figure 4A places E1 is not shown in the notebook;
  - the deposited images do not keep one orientation;
  - the choice E1 = `base_a` therefore rests on the uptake, so the order reading does not check it independently.
- **"Co-directional pairs from one electrode":** now quotes the session description and marks the one-electrode field as an inference.
- **Round 2 is recorded** under `verifications`, with the verifier's reasons and my responses.

**What I did not do, and why**
- **Figure 4 comparison left out of the entry:** to check E1's position, I mapped each deposited image onto the published Figure 4 image from PubMed Central, matching the three electrode centres.
  - The paired-pulse file matched Figure 4B, rotated 180° and not mirrored (fine-detail correlation 0.18, 0.34 after a one-pixel shift).
  - The single-pulse file did not match Figure 4A in either orientation. Its best was 0.03, the same level as pairs that don't belong together.
  - I put this in the notebook, but the entry check refuses any code that reads an image file ("figures must be computed from the data"). I removed it and did not route around the check.
- **No outcome change proposed:** a proposed change needs its analysis in the notebook, which isn't possible here. The comparison is disclosed in the fig4a and fig4bc notes as done outside the entry and not verified, and it is in the question to the paper's authors. If it holds, Figure 4A's image is not deposited, and both claims would become blocked (data missing) in a later attempt.
- **No reader question added:** the verifier found no misreading of the paper in the claims file.
