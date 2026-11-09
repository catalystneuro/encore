I've finished steps 1 to 5 and run the handover (step 6) for DANDI:001273 at version 0.250805.1356. Of the 17 claims, 2 were reproduced, 1 partially reproduced, 2 not reproduced and 12 blocked. `tools/entry.py check` reports 0 errors and all three notebooks pass from a clean environment. Nothing is committed and no reader was asked a question.

**Version.** The paper cites no version. The two published versions have identical files (same 181 blobs) and differ only in an added grant, so I pinned the most recent and said why in the notebook header.

## 1. Outcomes

| Claim | Outcome | Notes |
|---|---|---|
| fig4-polarized-poles-face-electrodes | reproduced (assumed) | 13 of the 14 experiments that state an electrode axis pass; 1 of 14 passes with the axes swapped |
| fig4-no-pole-difference | reproduced | none of the 16 readings is significant at p < 0.05; wide intervals, so little power |
| fig4-pooled-time-constants | not reproduced | no reading puts all four within the paper's SEMs; cathodic discharging is 1.37 to 4.20 us against 0.91 |
| fig4-orientation-time-constants | blocked: metadata_insufficient | no shape or orientation labels in the dataset |
| fig4-discharging-slower | blocked: metadata_insufficient | the same labels are missing; the pooled test is shown |
| fig4-full-charge-within-3us | blocked: metadata_insufficient | its reading (b) fails, so it cannot stand in for (a) |
| fig3c-sustained-firing-2s (DANDI:001030) | partially reproduced | firing rises with field in all 4 cells; no cell meets the block test (c7 is closest, with 1 AP) |
| figs1-di8-anepps-control (DANDI:001272) | not reproduced | no session reaches the 5% depolarization (largest 3.2%); 3 neurons where the paper has 8 |
| fig1, fig2, fig2c, fig2d, fig3b, figs2 | blocked: other | not tested for lack of time; fig3b's sodium gluconate sessions do not appear to be deposited |
| fig5, fig6, threshold-depolarization-estimate | blocked: too_large | DANDI:001274 is 25 GB, about 45 minutes of streaming at the rate measured here |

## 2. The dataset

**What it holds.** 181 files, each one replicate of 160 frames of 512 × 512 at 50-ns steps. They form 22 runs of 7 or 8 replicates (the experiments) plus 6 single files; the paper reports 19 experiments.

**What is missing:**
- No polarized ROIs, no debris ROI and no shape or orientation groups.
- The January 17 runs have no electrode axis, and no file gives the electrode polarity.

**Metadata problems:**
- Files recorded "backward" are stored in reverse time order. The data show this, but the files say nothing beyond the word "backward".
- The time base is only in prose: the rate is the camera's 6 Hz, and `starting_time` holds a Unix time.
- Subjects are cells, labelled age P18D.
- Most files have a dim first frame (a failed flash).
- There are no duplicate files.

**Findings in other dandisets.** These come from a metadata survey done outside the notebooks:
- DANDI:001034 duplicates DANDI:001032 byte for byte, under other subject ids.
- No 250-ms sodium gluconate sessions exist anywhere, which is why fig3b is blocked.
- DANDI:001030 lists the species as mouse, where the paper used rat.

**Assumptions:**
- "Up and Bottom" in the session text is taken to be the image's vertical axis.
- For figs1, "latency falls" is judged by a negative Spearman correlation, and depolarization over the last 100 ms of the stimulus.
- For fig3c, each cell's field series is judged on its own, as the figure shows one cell.

**Question for the paper's authors**, recorded as a `methods_unavailable` finding: the ROI size and placement, how the fits were weighted, whether the discharge amplitude was free, and which 19 experiments were used and in which groups.

## 3. Where the protocol was unclear

1. **Claims elsewhere whose data are not there (fig3b).** The protocol forbids `data_missing` for elsewhere claims but has no reason for this case. I used `other` and explained it.
2. **Claims never started for lack of time.** `too_large` covers only a computation that stopped. I used `other` for six claims, and `too_large` where the streaming estimate was the reason.
3. **The paper's experiments cannot be identified (22 runs against 19).** No rule covers this. I ran two sets, all 22 and the 15 at 40 V, and recorded a `selection_undocumented` finding.
4. **Criteria that point to another dataset's claims file (fig5, fig6).** The protocol does not say whether the author may read it. I did not; those claims are blocked anyway.
5. **Surveys run outside the notebooks.** The protocol does not say whether findings may rest on them. I put them only in notes and findings, labelled "not in the notebook", and none decides an outcome.
6. **Runtime.** The main notebook takes 22.5 minutes, nearly all of it streaming 10 GB. That is over the 10-minute aim and under the 60-minute limit. I could not reduce it, because every frame is needed at full resolution.
7. **Missing debris ROI.** Without it, the paper's correction for laser-flash fluctuations cannot be repeated. As the claims file says, I used unscaled traces and showed whole-frame scaling as a variant only.

## 4. Runtime and failures

The run went from 15:04 to about 18:16 UTC. Running the entry from a clean environment takes about 24.5 minutes (1349 s, 40 s and 81 s for the three notebooks). The first full run exposed a wrong check of `starting_time` and a wrong count of single files; I fixed both and re-ran. In development, some fits degenerated to the amplitude bound; they are now dropped and counted, which changed fig4-no-pole-difference. Nothing failed in the final run.

Files are in `entries/001273-semenov-2025/`:
- reproduce_semenov_2025.ipynb
- elsewhere_001030.ipynb
- elsewhere_001272.ipynb
- strobe.py
- fastimg.py

The attempt record is `attempts/001273-semenov-2025-01.yaml`, and the verifier's package is in `executed/001273-semenov-2025/handover/`.
