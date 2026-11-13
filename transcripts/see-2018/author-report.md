I ran steps 1 to 6 of the Author protocol on CRCNS ac-3. `entry.py all` passes with 0 errors, and the notebook runs in 34 min (peak memory 1.9 GB). It ran three times on the full data. The last two runs gave identical outputs. The handover is built in `executed/see-2018/handover/`. Nothing is committed.

**1. Outcomes (31 claims)**

| Claim | Outcome | Key numbers (paper) |
|---|---|---|
| fig7-totals | reproduced | 16 recordings, 655 units, 104 cNEs, 6.50 ± 1.97 per recording (identical) |
| fig4-example-nine-cnes | reproduced | site 10: 9 cNEs of 2 to 6 members |
| fig7a-number-vs-neurons | reproduced | R² 0.745, p = 1.7e-5 (0.74, 1.68e-5); 16.1% of units |
| fig7d-pairs-within-200um | reproduced | 88.5% (82%) |
| fig7e-no-depth-bias | reproduced, assumed | KS p = 0.999, MWU p = 0.47; the tests are the claims file's, the paper names none |
| fig4s2-interleaved-halves-stable | reproduced | 93.7% (96%) |
| fig5b-number-decreases-with-bin, fig5c-size-increases-with-bin | reproduced | monotonic trends |
| fig6c-spike-pwc-narrower-than-strf-pwc | reproduced, assumed | 63% of cNE pairs; reverses under the other reading |
| fig10b-ptd-higher | reproduced | p from 8e-12 to 6e-4 under all four readings; 476 pairs (703) |
| fig10s1-random-group-strfs | reproduced | 103 cNEs (103); PTD p = 7.0e-4, MI p = 3.1e-6 |
| fig11c-models-number | reproduced | shuffled 0.23, PR 1.4, DG 8.0 cNEs, against real 6.5 |
| fig11s3b-pr-strf-similarity | reproduced, assumed | PR 0.737 on 5-ms bins (0.645 on 10-ms bins) |
| fig6j-sharpness-cne-pairs | partially reproduced | p < 0.001 in 14 of 16 recordings |
| fig11ef-coincidence-ratios | partially reproduced | all three models below 1; the 'repeat' data are missing |
| fig2bd-pwc-measures-covary | not reproduced | R² 0.09 to 0.23 (0.5) |
| fig2eg-distance-weak | not reproduced | R² 0.006 to 0.06 (0.10 to 0.30) |
| fig4s3-train-test-83pct | not reproduced | 102 training cNEs (102), but 98% matched (83%) |
| fig5a-mi-peaks-10-15ms | not reproduced | MI peaks at 35 ms or 2 ms, depending on the event reading |
| fig6-member-pwc-sharpness-delay | not reproduced | median sharpness 12 ms (2 ms) |
| fig7b, fig7c, fig7f, fig7-negative-weights | not reproduced | mean cNE size 4.6 (7.4); 34% of units in no cNE (9%); 24 cNEs with a negative member (9); 80.8% of cNEs span 200 µm or less (70%) |
| fig10c-strf-mi-higher | not reproduced | best p = 0.0015 |
| fig11d-models-size | not reproduced | model cNEs are not consistently smaller |
| fig8, fig9c, fig9s1, fig9s2, fig11ab | blocked: data_missing | |

**2. Dataset, assumptions and questions**
- **What the data set holds:** 16 files (8 with the DMR stimulus `rn1`, 8 with the RN stimulus `rn16`), 655 units, and the stimuli. The triggers, the stimulus columns and the spike clock all agree, checked by STRF strength and latency against spikes shifted by 30 s.
- **What it lacks:** the 5-s repeats, the 15 repeats of the 10-min RN, and the 64-channel recordings, although the paper points to this data set for its data.
- **Other data findings:**
  - Two units have spike times slightly out of order.
  - The descriptor does not name rn1 and rn16 as DMR and RN, and does not say that `position` is a pair (lateral offset, depth).
  - Paired files share a tip depth and may be one penetration recorded twice. No unit matches across them, so each file counts once.
- **Assumptions:**
  - STRFs use 5-ms bins and 20 lags, from the data set's sample code by the first author.
  - The STRF cross-correlation is made non-negative by subtracting its minimum (fig6c).
  - The PR model uses 5-ms bins (fig11s3b).
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How IC weights were scaled and membership thresholds set; the number of cNEs matches but they are smaller.
  - The lag range, bin and any baseline correction of the pairwise correlation functions.
  - The STRF parameters, MI bins and how cNE events are timed.
  - How the STRF cross-correlation was computed, and the PR model's time bin.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or missing something**
1. CRCNS has no versions, so step 1.3's pinning does not fit. I recorded `unversioned` with the MD5 sums from `checksums.md5`, as archives.md says.
2. Any edit to the entry, including the README, forces a full re-run, and conclusions can only be written after a run. With a 34-min notebook that meant at least two full runs, and I made three. I wrote all text before the last run.
3. The protocol does not say whether the readings in the claims file's opening comment (IC sign, activity projection, event definition) should be crossed with every claim's own readings. I ran the ones that matter for each claim.
4. The protocol has no rule for cutting iterations to fit the time limit, short of blocking as `too_large`. I recorded these cuts as deviations: 100 random groups (paper 500), 200 CR runs (paper 1000), and the real data's membership thresholds reused for model runs, justified by the thresholds following ±1.5/√n.
5. The source order (Methods, paper's code, other software) does not mention a data set's own code. I used it only as the basis for a stated assumption.
6. Gaps in the criteria:
   - fig4s3's criterion does not cover a correct count with an out-of-range percentage; I judged it not reproduced.
   - fig2eg expects a range but `measured` takes one number; I gave the largest R² under the first reading.
   - When no reading matches, the protocol does not say which reading goes under `measured`; I gave the first one listed.

**4. Runtime and failures**
- The session took about 2 h 50 min (03:43 to 06:32 UTC).
- Each full notebook run took 34 min on 4 processes.
- Bugs I found and fixed before the final runs:
  - 2-member cNEs got no random groups, which made the fig10s1 test give p = nan.
  - A stale copy of the helper in the temp directory shadowed the real one in a dev script.
- An empty `entries/see-2018/.claude/.cc-writes` directory left by the harness is in the entry. I can't remove it, and git does not track empty directories.
- Nothing else failed.
