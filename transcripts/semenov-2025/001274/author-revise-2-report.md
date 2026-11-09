I've finished the round-2 revision of 001274-semenov-2025-01. No outcome changed, and I've proposed one change, for fig3c-sustained-firing-2s, for a third round. The entry ran twice with `python tools/entry.py all` (21.5 min each) and passed both times with 0 check errors. The second run was on the final notebook, and every number matched the first.

**Outcomes**
- **fig3c-sustained-firing-2s:** the verifier now disagrees with not_reproduced. The record keeps it, as round 2 requires, and proposes `reproduced` under `proposed`. A new notebook cell measures how many false APs noise alone produces on c7's own bleaching-corrected trace over 0.25 to 2 s:

  | Estimate | Reading (a) | Reading (b) |
  |---|---|---|
  | Found in the data | 5 | 1 |
  | Same trace mirrored about its running median | 6 | 7 |
  | Running median plus Gaussian noise (mean of 300 draws) | 7.8 | 5.1 |
  | Running median plus the residual shuffled in time | 8.4 | 4.6 |

  So the peaks that fail part (iii) are no more than noise produces. The 8 to 10 APs of part (i) are well above the noise rate of about 1.1 and 0.7 per 250 ms, so part (i) still holds. The proposed outcome rests on reading "no APs" as "no more detections than noise gives". The proposal's reason says it should be marked assumed. The notebook result cell, the summary and the README now say a change is proposed.
- The other 25 outcomes are unchanged; the verifier agreed with all of them.

**Corrections and added output**
- **fig2d calibration:** the old statement that a 20-kHz factor of 0.64 to 0.97 would bring the ratios into tolerance was wrong. The notebook now works out the bounds from the ratios themselves. A single factor would need to be at least 0.794 and at most 0.779, which is impossible. So no calibration can bring all four ratios into 1.8 to 2.2. The notebook, the notes and the round-2 response now say so.
- **Short-latency APs (fig1-onset-delay):** of the five sessions at 10 to 16 ms, three are the first of 4 regular APs and two are single APs. The earlier text called all five isolated APs.
- **Pooling:** the notes and result cells now say that the outcomes of fig1-onset-delay and threshold-2khz-unmodulated depend on pooling 001032, 001033 and 001035. 001035 alone gives a latency of 101 ms and a threshold of 58.3 V/cm, both inside the paper's ranges.
- **Brightness (fig1-pure-sine-excites-all):** I added the actual brightness of the two neurons never excited at 20 kHz (78th and 74th percentile of all recordings). The ratio the text had called brightness is now called contrast.
- **Smaller fixes:**
  - The shifted-beat 0.04 is now described as pooled over all modulated sessions.
  - The round-1 count of 12 APs is removed.
  - The README says the variant's ROIs come from a RATIO image computed by the Methods' recipe, not from the paper's own image.
  - The frame-count finding now reads "one has 1,400 and one 1,800".
  - `runtime_minutes` in `entry.yaml` is now 22 (it said 12).
- Round 2 is recorded under `verifications`, with the verifier's reasons and my responses for all 26 claims.

**Not done**
- No question was added to `questions/001274.yaml`, because the verifier found no place where the claims file misreads the paper.
- Problem 9 from round 1 (other neurons corrected with c7's AP-free trace) is unchanged. The verifier said it does not affect a conclusion.
- `tools/build_site.py` was already modified before I started. I didn't touch it, so the workflow's commit may include it unless it's excluded.
- Nothing is committed or pushed.
