I worked through all seven of the verifier's round-1 points, re-ran the entry with `python tools/entry.py all entries/saez-2016` (passes, 172 s), and updated every conclusion to the new numbers. The round is recorded under `verifications`. Nothing is committed.

**Outcome changes**
- **dataset-size**: partially reproduced → reproduced, measured 14/14/26. I took the verifier's view: the sheets list and give data for all 28 control cells, and the 8 missing recordings remain a data finding that limits the control claims.
- **fig1-vc-ic-same**: still reproduced, but now marked as resting on an assumption. After the fixes below, the all-post-sweeps reading (P)(a) gives Shapiro-Wilk p = 0.0497 for the current-clamp cells, so the readings disagree. I adopted (P)(c), the last 120 post-pairing sweeps, because all 40 voltage-clamp sheets record "Traces compared 120" and their changes are closest to (c). Under (c) no test is below 0.05.
- Every other outcome is unchanged. The verifier agreed with all of them except dataset-size.

**Fixes and additions**
- **Stimulus alignment (point 4)** was a real problem. The artifact has two phases, and in 41 of 115 files the largest step landed on different phases in different sweeps. Sweeps are now aligned on the artifact's start: 16,351 sweeps sit at their file's usual time, 342 are one sample (0.05 ms) off and 5 are further. Stimulus times are printed at 0.05 ms resolution. The old alignment is kept as a variant; it changes one cell's class (VCB33).
- **IC13 (point 6)**: its last four post-pairing sweeps had no stimulus or a spike, and were being measured as 43 to 51 mV responses. Sweeps without a stimulus artifact are now dropped (5 of 17,319). IC13 goes from +20.6% to −10.9%, against −12.8% in its sheet, and the sheet's per-sweep values match the recording (r = 0.995).
- **VCB17 (point 1)**: I kept the cell and recorded the disagreement. The data check now shows a real stimulus-locked current: 93 pA before pairing and 473 pA after. The change is +390% to +408% by every estimate. The sheet's amplitudes minus the holding current also give +390%, so the sheet's +62.9% includes the holding current. That is a new data finding, and it feeds into the bicuculline mean and SD that the sheets share with the paper.
- **Filling in the 8 missing control cells (point 2)**: there is now a table of all 28 control cells. The sheets store no p values (the voltage-clamp sheets' p cells are empty). Five measured cells whose sheet change is under 15% are plastic in some reading, so the fill-in is loose, and the notes say fig1c's partial outcome depends on it.
- **Inclusion marking (point 5)**: a fill-colour table is added. Every excluded row is red; included rows are unfilled (current clamp, bicuculline) or green (voltage clamp).
- **Baseline choice (point 3)**: no change; the notes and README now say the control outcomes depend on using the last 120 baseline sweeps.
- **Clamp labels (point 7)**: I added `questions/saez-2016.yaml`, asking a reader whether the paper swapped its V-clamp and I-clamp labels. The notebook shows the swapped reading: the current-clamp mean then falls outside tolerance in every reading, which would change fig1-control-mean-change.

**Not done**
- I did not exclude VCB17 by a rule, as the verifier suggested, because the evidence shows its response can be measured. The analysis without VCB17 is still shown.
- I did not recover per-cell p values from the sheets' green-marked sweeps. The column layouts differ between sheets, so any matching rule would be guesswork.
