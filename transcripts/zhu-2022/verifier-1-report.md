**A. Outcomes** (25 claims in the claims file; the notebook tests one)

| Claim | My outcome | Reason |
|---|---|---|
| participants | partially_reproduced | Cell 15 finds 10 distinct subjects, and every file has 256 electrodes in two groups of 128. Both match the expected values exactly. Sex is `U` and age is the group range `P19Y/P50Y` in every file, and no task labels exist. So the 4/6 sex split and the 5 COM / 5 NL split cannot be counted per subject. The free-text "4 males and 6 females" is the depositor's statement, not a count. |
| task-structure | blocked: data_missing | No trials table and empty `stimulus`/`intervals` (cell 6). The archive agrees (see below). |
| behaviour-response-time | blocked: data_missing | No responses or question onsets (cell 6). |
| fig1b-high-gamma-best-band | blocked: data_missing | Only one HGA series and no broadband signal (cells 3 and 6, dandiset description). |
| fig1c-responsive-in-ifg | blocked: data_missing | No events. `location` is `unknown` for every electrode, and there are no coordinates (cell 6). |
| fig1d-only-after-keyword | blocked: data_missing | No events or condition labels. |
| fig2b-violation-electrodes | blocked: data_missing | No events, labels or IFG labels. |
| fig2b-single-type | blocked: data_missing | Depends on fig2b-violation-electrodes. |
| suppfig6a-half-split | blocked: data_missing | No events or sentence identities. |
| suppfig6b-duration-metric | blocked: data_missing | No events or labels. |
| fig2c-euclidean-similarity | blocked: data_missing | Depends on fig2b-violation-electrodes. |
| suppfig7a-com-overlap | blocked: data_missing | No COM labels. |
| suppfig7b-not-nonlinguistic | blocked: data_missing | No NL labels. |
| fig2de-no-spatial-separation | blocked: data_missing | No MNI coordinates. |
| suppfig8b-individual-no-separation | blocked: data_missing | No coordinates. |
| fig2f-circuit-diameter | blocked: data_missing | Depends on fig2b-single-type. |
| suppfig9-predict-from-corr | blocked: data_missing | No CORR labels or events. Never run, so the chance level could not be compared (the paper gives 25%). |
| fig3-latency-values | blocked: data_missing | No keyword onsets. |
| fig3d-latency-differences | blocked: data_missing | Depends on fig3-latency-values. |
| fig3-sync-latency-variability | blocked: data_missing | Depends on fig3-latency-values. |
| fig3e-latency-not-location | blocked: data_missing | No coordinates, no onsets. |
| suppfig10a-separable-400-700 | blocked: data_missing | No labels or onsets. |
| suppfig10b-duration-differs | blocked: data_missing | Depends on fig2b-violation-electrodes. |
| nl-low-frequency | blocked: data_missing | No 4–10 Hz signal and no NL labels. |
| stimuli-word-frequency | blocked: other (not attempted) | The claim is `data: with_inputs` and does not use the dataset. The notebook skips it as needing "an unpinned web corpus", which is not a reason the criterion allows. Its inputs are available, so it should have been tested (problem 1). |

**Archive check of the blocked claims.** I queried the DANDI API at 0.240921.1006:
- **Contents:** 40 assets. Asset metadata gives sex "Unknown", age P19Y/P50Y, `variableMeasured` ElectrodeGroup and ElectricalSeries only, and no `relatedResource`.
- **Byte balance:** I compared file sizes against 256 × n_samples × 4 bytes. The largest TC5 file (39,255,800 B, 38,099 samples) and the smallest TC12 file (29,627,128 B, 28,696 samples) each carry exactly 242,424 B beyond the data. This assumes the smallest and largest files are the ones with the min/max sample counts. A fixed overhead like this argues against per-block event tables, which would vary in size.
- **Conclusion:** no part of any `data_missing` claim can be tested. The only extra fact available is the four blocks per subject, which is not an expected quantity in any claim.

**B. Problems**

1. **[affects a conclusion]** stimuli-word-frequency (cell 0 table) was not attempted.
   - The keyword lists are in `paper/…txt` (supplement stimulus lists, around line 1510).
   - The corpus the paper names, lingua.mtsu.edu/chinese-computing, answers HTTP 200.
   - "Unpinned" could be recorded as a caveat, but it is not a reason to block. This claim's outcome is undecided only because of that.
2. **[does not affect a conclusion]** `ifg_hga.summarize` never lists what is inside `acquisition/`, or inside `general/` beyond subject and electrodes. It only lists `stimulus`, `intervals`, `analysis`, `processing` and `units`. So an event TimeSeries or annotation stored in `acquisition` would go unseen, and the "no events" basis for 23 blocks is incompletely checked. The byte balance above makes such tables unlikely.
3. **[does not affect a conclusion]** Cell 15 prints "male participants: found 0" and "female: found 0". The field is `U` (unknown), not a count of zero. These should be reported as "not determinable", not as a mismatch.
4. **[does not affect a conclusion]** Cell 15 checks the ages only against the group range. That is correct given the data: cell 5 rightly notes that nothing maps TC5–TC20 to participants 1–10 of Supplementary Table 1. This supports partially_reproduced, not reproduced.
5. **[does not affect a conclusion]** Cells 9 and 11 argue that the data are z-scored per block (correct: mean of about 0 and SD of about 1 on every channel) and that the true rate is 100 Hz, not the stated 400 Hz.
   - Both arguments are reasonable. With 160 linguistic+COM/NL trials over 4 blocks (about 40 per block) at about 8 s per trial, 100 Hz fits the block lengths.
   - However, the notebook never says which rate any analysis would use. That would matter if events were ever added.
6. **[does not affect a conclusion]** The helpers work on synthetic inputs:
   - `best_match` gives 1.0 for an exact or affine copy, and returns the Pearson r (0.703) for a noisy copy.
   - `_peak_excess` detects an injected 1/50-cycle peak (2.24, against 0.05 off-peak).
   - The duplicate-block check in cell 12 is sound.

**C. What I could not check**

- I could not confirm that `acquisition/` holds only `ECoG`, or that no file contains event or annotation objects elsewhere. A printed full HDF5 path listing of `acquisition` and `general` for one file per subject would settle this.
- I could not see the per-file `n_samples` next to the asset sizes, which would tighten the byte-balance argument. A table of path, n_samples and asset size would let me check it directly.
- stimuli-word-frequency cannot be judged without its output: the 32 CORR and 32 SYN-C keywords, their corpus frequencies, both means, and the t-test.
- Whether the 5/5 split by recording date (TC5–TC12 against TC16–TC20, which also differ in block length and the start transient) corresponds to the COM/NL groups is unverifiable from the dataset. It should not be used to count the participants with COM and with NL.
