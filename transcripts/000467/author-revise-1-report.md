I've worked through the round-1 report, re-run the entry with `python tools/entry.py all entries/000467-hart-2023`, and rewritten every conclusion to match the new numbers. All three notebooks passed (general 6 min, alarm 21 min, concentration 17 min) and `entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **fig3fg-hexanone-broad:** partially reproduced → **reproduced**. With ImageJ's 21-pixel radius-2 Minimum filter (fixing verifier point 7), 3-hexanone's median area is 2.57 times ethylpyrazine's (was 1.91), and it is still the largest in all 6 ants.
- **fig4-large-lasting-responses:** partially → **not reproduced**, as the verifier gave it. No value reading meets both parts (b/i median 0.453; b/ii median 1.016 but only 41% still elevated after the pulse).
- **figs5b-shared-glomerulus:** partially → **not reproduced**. Only biy at 48% meets it; under bix the median is 0 at each ant's higher concentration.
- **fig6-shared-panic-pathway (imaging half):** partially → **not reproduced**, because it depends on figs5b.
- **figs7c-temporal-lme:** blocked → **not reproduced (assumed)**. bix finds no PGa, so the models can't be fitted there. aiiy is the identification that finds PGa in the most ants (4 of 13, 3 at 48%), and under it 1 to 4 of the 5 effects reach p < 0.05. The time-to-maximum interaction is significant in 9 of 12 readings, where the paper reports p = 0.88. With PGa in only 3 ants against the paper's 8, this is weak evidence.
- **figs7a-6g-extended:** stays not reproduced but no longer rests on an assumption. 6G is now found in all 5 ants with 144 s recordings.

**Outcomes kept, with the verifier's disagreement recorded**
- **figs4a-bilateral-symmetry** stays partially reproduced: the correlation part holds in all three ants and the count part fails.
- **figs5a-sparse-median-6, figs5a-concentration-more-glomeruli and figs5c-mho-rarely-overlaps** stay reproduced (assumed). The readings still disagree, but after the rebuild of drawing a, every reading that uses the ROI's mean with the Methods' trial-mean rule meets these criteria, under both ROI drawings.
- **The seven Brain Image Library and NCBI claims** stay blocked as `other` or `not_runnable`, not `data_missing`. The protocol never blocks a `data: elsewhere` claim as `data_missing`.

**Fixes and added outputs**
- **ROI drawing a:** rebuilt as the claims file states it. A thresholded region in one trial counts when it overlaps a region in another trial of the same odour by at least half the smaller one; this replaces counting single pixels above 0.2 in two trials. Reading a now gives 8 to 40 ROIs per ant, down from up to 469.
- **Single-glomerulus traces:**
  - Each plane's row band is now motion-corrected, and the uncorrected trace is kept for comparison. PGb peaks differ by a median of 0.035, and 3 of 129 trials change side of 0.2.
  - The traces are computed under bix and under aiiy, the reading that finds PGa in the most ants, so PGa is now tested.
  - Both of the claims file's ROIs are run: the 15 µm disc and the region of at least 0.2.
  - Times now include each plane's offset within the volume scan.
- **figs7c model fits:** the notebook now states which fits cannot be run and why, instead of hiding the failure.
- **Outputs the verifier asked for:**
  - per-ant ROI images for both drawings
  - the fraction of the AL at 0.2 or more for each vehicle trial, and fig4b re-run without the flagged trial
  - where the negative regions of fig4-no-decreases lie: 487 of 594 touch the AL border and 384 overlap another odour's negative region, which points to motion
  - shift against volume for a few trials, and a corrected against uncorrected PGb trace
  - a baseline image of one ant with PGb, 6G and PGa marked, which matches the orientation of Figure 5B
- **Smaller fixes:** the header now counts 15 blocked claims, and the record notes that the directions in fig5d hold by construction of the identification.
- **Question for a reader:** added `questions/000467.yaml`, asking whether drawing (a) should have a minimum size.
- **Records:** updated the attempt record (outcomes, notes, deviations, and the round-1 `verifications` entry for all 32 claims), the README and `entry.yaml` runtimes.

**Not done**
- The verifier asked for traces under aiix. I used aiiy instead, because after the rebuild aiix finds PGa in only 3 ants against aiiy's 4.
- After the run I changed only markdown text, so I copied the new conclusions into the executed notebooks rather than running everything again.
- The attempt record was rewritten by a YAML dump, so its whole-file diff looks larger than the actual changes.
- In the ROI figure, the per-ant titles of the bottom row (drawing b) appear to be hidden by the images above them. The data in the panels is correct.
- Untracked files such as `.bashrc`, `.vscode` and `scripts/` appeared in the working tree. I didn't create them and left them alone.
