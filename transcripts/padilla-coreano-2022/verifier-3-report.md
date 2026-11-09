**Verifier report, round 3: Padilla-Coreano et al. 2022 on DANDI:001749 (0.260311.1727)**

The attempt record proposes a change of outcome for one claim only. Counted from the record, there is one `proposed:` block, on `ed5k-hmmglm-generalizes-across-rank`. No other claim has one.

| Claim | Outcome now | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|---|
| ed5k-hmmglm-generalizes-across-rank | not_reproduced (assumed) | reproduced | **Yes**, provided `assumed: true` is kept | — | See below. |

**Reason (cells 49, 50, 51, 53, 57, 60, 61)**

1. **The numbers come from the data.**
   - **Rates per channel (cell 49):** median 16.41 Hz for negative crossings and 23.05 Hz for crossings in either direction, computed from the raw `ElectricalSeries` of the 17 files used (512 trials).
   - **The paper's input (cell 50):** its median rate per channel is 28.15 Hz. Over the trials matched at label agreement of 0.9 or more (346 of 512), the paper's counts are 1.47 times the negative crossings (median over the 17 files, range 1.21 to 2.11) and 1.06 times the crossings in either direction (range 0.63 to 1.41). The proposal's reason and the cell 51 text quote these figures correctly.
   - **Cross-rank runs (cell 60):** with crossings in either direction, dom to sub, sub to dom, dom 10-fold and sub 10-fold each give 9 of 9 AUCs above 0.5 (sign p = 0.0039), both with and without the shift. The lowest AUC is 0.580 or more in every case (0.5816 for sub to dom with the shift). The medians are 0.821 and 0.788 for the two cross-group directions.
   - **Main reading, for contrast (cell 60):** sub to dom gives 7 of 9 (p = 0.18).

2. **The criterion is applied as written.** It asks for every train and test combination to give a sign test of the 9 AUCs at p < 0.05: both cross-group directions plus the within-group 10-fold runs. Cell 60 runs all four under reading (b) with the rest of the fig1i model unchanged (counts, contiguous folds, the shift), and all four pass.

3. **The choice was not made to reach the result.** It is post hoc, because reading (b) was argued for after it had been seen to pass. But the evidence for it comes from outside the decoding: the count level of the paper's own processed input. The two levels point the same way. Under negative crossings, the paper's counts are higher in every file (range 1.21 to 2.11, never below 1). Under crossings in either direction, the per-file ratio straddles 1. The paper names no direction (Methods 17, paper text line 476: "determining spikes using 4 standard deviations from the mean"), and the claims file lists both readings as open. Picking a reading because the paper's processed input supports it is the same rule the record already applies to fig1i, where counts and contiguous folds rest on the same input.

4. **Why the assumption must stay.** The count level does not settle the direction. Cell 50 shows that the counts computed here barely follow the paper's in time: channel by channel the median correlation is about 0, and summed over channels it is -0.09 to 0.73 per file. Both readings correlate equally poorly (`r_paper_neg` and `r_paper_both` are nearly identical in every file). So the paper's thresholding or channel order differs in ways Methods 17 does not fix. A 1.47-fold gap could also come from those differences. Examples are a noise estimate other than the SD of the 14 s trial window (for instance a median-based one) or another filter band. The proposal itself says the outcome "would still rest on that assumption", and the `methods_unavailable` finding asking the authors is the right follow-up.

5. **The dependent claims stay consistent.**
   - **fig1i:** passes under reading (b) (cell 53: median 0.910, every test True), so its outcome is the same under both readings.
   - **ed5j:** not reproduced under both readings (cell 57, and the record notes). Reading (b) selects 3 or 4 states, against 2 under reading (a).
   - **The main readings will differ.** If the proposal is accepted, ed5k would rest on reading (b) while fig1i and ed5j keep reading (a). No outcome changes, but the record should say so in ed5k's deviations.

6. **A minor point, not bearing on the outcome:** the subordinate group still holds only 4 mice (213 trials), as the deviations already state.

**Places where the claims file may misread the paper:** none found for this claim. ED Fig. 5k's legend gives 482 dom and 478 sub trials, and the claims file quotes them as the paper prints them. The paper's input holds 487 dom trials (cell 51). That difference is in the paper and its deposited input, not a misreading by the claims file.
