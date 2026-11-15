I finished the blind repeat attempt and wrote it to `entries/martinez-conde-2019/` and `attempts/martinez-conde-2019-02.yaml`. `tools/entry.py check` gives 0 errors, the clean run passes in 32 s, and the handover is built in `executed/martinez-conde-2019/handover/`. I did not verify my own work, and nothing is committed. I never saw an earlier attempt's results, not even by accident.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| neuron-counts | not reproduced (53 neurons, paper 58) |
| spikes-per-condition | blocked, data_missing |
| s4-baseline-no-difference | not reproduced (rests on an assumption) |
| fig4a-above-baseline | reproduced (assumption) |
| fig4b-spike-rate-difference | partially reproduced: S40 26.5, S52 19.0, S90 8.2, P180 3.9 spikes/s; order holds, S90 just outside tolerance (assumption) |
| fig4b-pairwise-significance | reproduced (assumption) |
| fig5-average-maps | reproduced (assumption) |
| table1-edge | not reproduced (assumption) |
| table1-p180 | partially reproduced (assumption) |
| table1-s90 | not reproduced (assumption) |
| table1-s52 | reproduced (assumption; 12 of the paper's 30 Star neurons) |
| table1-s40 | reproduced (assumption) |
| fig6-midpoint-representative | reproduced (assumption) |
| fig7a-rms-contrast-fit | not reproduced |
| fig7c-fold-edge-equivalence | not reproduced (assumption) |
| fig7c-fold-edge-significance | reproduced (assumption) |
| fig7d-nonlinear | reproduced (assumption) |
| fig7d-dog-similar | blocked, data_missing |
| s3-latency-peak | blocked, data_missing |

**(2) What I found about the dataset, assumptions and questions**
- **Neuron count:** the files hold 53 neurons. Their spreadsheet lists 58 cells, but 5 of those have no condition marked and no files.
- **`image` field:** the description calls it raw spike counts. It is actually spikes per 1 ms eye sample, so I multiply by 1000 to get spikes/s. The one file that also stores eye time confirms this.
- **Missing raw data:** there are no spike times, no eye positions, and eye time in only 1 of 75 files. That is why three claims are blocked.
- **Misfiled Star files:** 2 files in the Star folder (`ABS042700J2`, `ABS051000J3`) hold a Corners-type stimulus, not the Star.
- **Star neurons I could not use:** 15 of the 27 Star files have no aligned frame. Their maps are in gaze coordinates, and neither the receptive-field offset nor the aligned diagonal is stored. So the Star claims rest on 12 neurons.
- **Undocumented fields:** `Standard`, `BaseActivity` (present in 38 of 60 files), `smoothed_image_norm` and `eyetime` are not described anywhere. The Corners aligned frames come in two sizes.
- **Main assumption: where the baseline squares sit.** The Corners squares appear only in Fig 2C, which is not in the text; I placed them at the bottom corners of the frame. For Square and Edge and for Star, I placed them inside the corners of the circumscribing square and showed corner-centred squares as a variant. The stored `BaseActivity` matches neither placement, and the S4 baseline outcome changes with it: my placement finds a difference (p = 0.004), the stored values do not (p = 0.11). Every outcome that uses a baseline is marked `assumed`.
- **Two questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which RMS contrast definition gives 0.61 to 0.943? Neither reading in the claims file does.
  - Where exactly are the baseline squares and the Edge blocks?
- I asked a reader no questions.

**(3) Where the protocol was unclear or did not fit**
1. The "clock" check assumes time streams, but the data are spatial maps only. I used a spatial version instead: the response on the fold against 32 DU off the fold.
2. For fig7a, both readings in the claims file fail, which may reflect a missing definition more than the data. I recorded `not_reproduced` as the criterion says, and added a question for the authors.
3. The neuron-counts claim tests counts the dataset cannot fully hold. I recorded `not_reproduced` with a `data_missing` finding.
4. Nearly every claim rests on the same baseline-placement assumption. I marked each one `assumed` instead of blocking them.
5. CRCNS is unversioned. I recorded `unversioned` and checked that `checksums.md5` still lists the zip's MD5; verifying the sum itself would mean downloading the whole 175 MB file.

**(4) Runtime and failures**
The notebook runs in about 30 s with a peak of about 460 MB. Development took roughly 04:25 to 04:47 UTC. Nothing failed in the final run.
