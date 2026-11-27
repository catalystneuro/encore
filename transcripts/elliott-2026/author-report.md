I finished steps 1 to 5 and ran the handover (step 6). Both notebooks pass `tools/entry.py all` (10.4 and 21.4 min), and `check` reports 0 errors. Dandiset 001132 is pinned at version 0.241130.1903: the paper cites no version, and the two published versions list the same 69 assets.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| sorting-dandiset-link (link claim I added) | partially reproduced: 6 of 8 recordings found |
| table1-unit-counts | not reproduced: unit counts 8 of 8 equal; durations of the dandiset files 5 of 8 |
| fig1g-ka-synchronized-bursting | not reproduced |
| methods-burst-counts | not reproduced |
| methods-rate-increase-after-ka | not reproduced: the rate per unit falls by 0.10 to 0.12 spikes/s |
| methods-onset-latency | blocked (metadata_insufficient) |
| s4-ka-no-epileptiform | not reproduced |
| ext3-onset-spectral-signature | reproduced, resting on an assumption (`assumed: true`) |
| fig1j-theta-propagation-stages | not reproduced |
| ext4b-theta-delay | not reproduced |
| ext4-electrode-lag-clusters | partially reproduced |
| methods-rolling-wave-counts | blocked (methods_underspecified) |
| fig2a-subbursts-track-theta | not reproduced |
| table2-phase-locking-counts | not reproduced with the Methods' spike selection; the code's selection matches S1 and S2 |
| table2-phase-locking-seizure-vs-not | partially reproduced |
| fig2b-phase-cluster-kuiper | reproduced, but only on the Methods' split, which is significant by construction |
| fig2c-sttc-two-clusters | partially reproduced: holds for S2, not S1 |
| ext9-sttc-eigenvector-gradient | partially reproduced: holds for S2, not S1 |
| ext9-sttc-beats-correlation | reproduced |
| fig3a-significant-pairs | reproduced: all 8 counts equal the paper's, and the pairs are identical to the code's saved lists |
| fig3a-bipolar-angle-histograms | partially reproduced |
| ext10-baseline-same-circuit | reproduced |
| table3-geometry-test | reproduced: 8 of 8 within tolerance |
| ext12-simulation-recurrence | blocked (not_runnable) |

## 2. Dataset, assumptions and questions

**What the dataset holds:**
- Raw voltage only: no units, no epochs, no conditions, and no record of when kainic acid was applied. All session start times are the conversion date.
- The curated sortings come from the paper's GitHub repository at commit 0f83f70 (listed under `inputs`). I matched them to dandiset files by electrode layout and by aligning spike times with the raw voltage.
- Recordings 1 to 6 are in the dandiset. The S1 baseline starts 20 s into sub-10F-0 and the S4 recording starts 30 s into sub-9E-2.
- The raw recordings of S5 and S6 are not in any file with their electrode layout (finding rated major).
- Subjects are named by slice, and the patient letters differ from the paper's.
- sub-3C-1 to sub-3C-4 share 78 to 82% identical samples. Other same-length pairs share 4 to 8%. I could not tell whether they are duplicates or share a large artifact, so I rated it major. No analysis uses these files.
- The S1 STTC matrix is not positive semidefinite, which contradicts the Methods (recorded as a paper inconsistency).

**Assumptions:**
- ext3: onset set at the paper's initiation burst (14.4 s, from the code and Extended Data Fig. 4). The criterion's onset falls at 0.9 s, which leaves no 5 s baseline.
- Burst reading (a): the pre-KA reference is the separate baseline recording, because no KA time is recorded.
- Stage windows are taken from the times in the paper's figures and code.
- The hilus is assumed to lie on the concave side of the fitted cell layer.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How were bursts and superbursts detected?
- Which spike selection produced Extended Data Table 2, the Methods' or the code's?
- Which split gave the Kuiper p = 0.01?
- How were onset, the stage windows, propagation direction and rolling waves defined?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. Adding a link claim requires dependent claims to list it in `depends_on`, which edits existing claims. I added `depends_on` to four claims and changed no statement, expected value or criterion.
2. There is no rule for choosing between published versions with identical contents. I pinned the latest.
3. A criterion reading can need metadata the dataset lacks (the pre-KA part). I substituted the nearest available data and recorded it as a deviation.
4. For claims of absence, the protocol says the readings rule does not apply, but the criterion names readings. I ran them all; they agree, so the outcome does not depend on the choice.
5. There is no rule for a criterion reading that passes by construction (Kuiper reading b). I applied the criterion and flagged it.
6. When the criterion's partial clause holds only under the code variant (table2), I decided on the main reading, which is the Methods'.
7. Step 1.6 assumptions sit uneasily with "do not change the criterion" when the criterion itself fixes a choice that cannot work (ext3's onset). I adopted an assumption and showed both results.
8. When the dataset lacks recordings, criteria fail through no fault of the paper's numbers (table1), and there is no partial-blocked route. I applied the criterion and explained in the notes.
9. `measured` must be all numbers, so I omitted it where some recordings are missing.
10. The "same clock as the trial tables" check does not apply: there are no trial tables. I used spike-to-raw alignment instead.
11. I could not render the supplement PDF with `pdftoppm`. I used PyMuPDF in a scratch environment, not in the entry.

## 4. Runtime and failures

About 3 h (01:55 to 04:52 UTC). Peak memory was 3.6 GB.
- The first pair-selection code reversed pairs in a different order from the paper's code. I fixed it, and the counts then matched exactly.
- The simulation could not be built. The code pins conda NEST 3.4 with NESTML 5. With NEST 3.10 from PyPI, NESTML 9 cannot parse the model and NESTML 5 calls an API that NEST 3.10 removed. The sweep was not timed.
- ext4b's second reading (the figure's three electrodes) was not run, because the figure gives no electrode coordinates.

Nothing was committed or pushed.
