I've written the new entry at `entries/gao-2018`, the record at `attempts/gao-2018-02.yaml`, and built the handover in `executed/gao-2018/handover/`. The entry check gives 0 errors and the notebook runs from a clean environment in about 20 minutes. I did not verify my own work, commit or push. I did not come across any earlier attempt's results.

**1. Outcomes (46 claims: 14 reproduced, 7 partially reproduced, 1 not reproduced, 24 blocked)**

| Claim | Outcome |
|---|---|
| fig1g early-sample no effect; fig1g delay errors; ed10b; fig1h delay bias; fig1g dentate little effect; fig1k delay bias | reproduced (all from the behavior in the recording sessions) |
| fig2-alm-selective-fraction (856/1084 = 0.79) | reproduced |
| fig2-preparatory-more-in-alm (ALM only, 0.563) | reproduced (the CN comparison is untested) |
| fig2-peri-movement-equal; fig2cd-selectivity-emerges-gradually | partially reproduced (ALM half holds; CN not deposited) |
| fig3d ALM altered by CN inhibition (fraction 0.469 matches; latency 15 to 32 ms, not 7.1) | partially reproduced, assumed |
| fig3e mean rate unchanged (4.03 vs 4.21 spikes/s, p = 0.51) | reproduced |
| fig3e increase/decrease (fraction 0.535) | reproduced, assumed |
| fig3f selectivity abolished by CN inhibition (falls 73%, but its interval stays above zero) | partially reproduced |
| fig4 fastigial latency (3.6 ms matches; 177 modulated neurons against 227) | partially reproduced, assumed |
| fig4e (n = 328 exactly, as the paper); fig4f persistence | reproduced |
| fig4g dentate recovers (late fraction still above baseline) | partially reproduced, assumed |
| fig4i control separation | reproduced |
| fig4i fastigial collapse (dentate also drops 14%, interval excludes zero) | partially reproduced |
| cd-captures-selectivity (66.3% and 28.4%) | reproduced, assumed |
| ed10d: projection no longer predicts licking (slope still significant, p = 0.003) | not reproduced |
| 24 claims on lesions, CN recordings, licks, behavior-only sessions, VGAT mice, anatomy | blocked, data_missing |

**2. What I found about the datasets**
- **Same recordings in both:** the two datasets hold the same 54 sessions of 13 mice, and every unit's spike times are identical. I analysed the CRCNS copy and checked DANDI against it.
- **DANDI gaps:** DANDI lacks 26 trials in one session and 268 of 302 in another. Its trial start times are rounded, and its event times are described as relative to the trial start when they are in session time.
- **Laterality:** for mice CD12, CD13 and CD14, both datasets put the fastigial fiber on the same side as the recorded ALM. This contradicts the paper's contralateral design. Both side assignments were run; fig1k reproduces either way.
- **Laser traces:**
  - Several 2015 sessions disagree with their trial codes: one has 1.3 s of light instead of 500 ms, one has varying durations, one has almost no light.
  - In one 2017 session, many delay-coded trials are lit at sample onset.
  - The photo-inhibition power values match neither of the 1.5 and 4.5 mW the Methods state.
- **More units than the paper reports:** 1084 pyramidal neurons in the photo-activation mice against the paper's 912, and 682 in the photo-inhibition mice against 454.
- **Analysis code:** CRCNS:alm-4 holds the lab's analysis scripts, which the paper's reporting summary says would be deposited there. The claims file says the paper links no code. I took the method details the Methods leave open from these scripts and cited each one.
- **Assumptions:** latency bins labelled by start (fastigial) or centre (dentate); counts compared by fraction where the files hold more neurons; for the cd fractions, squared ratios on held-out trials with single-trial variance.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): how latency bins are placed in time; how the cd fractions are computed; the neuron and session selection.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. When a claim compares ALM with CN and only ALM can be tested, it is unclear whether the outcome is partial or blocked. I followed the criterion where it allows ALM alone, and used partially reproduced elsewhere, explaining why in the notes.
2. Several count criteria fall back to a fraction "where the dataset holds fewer neurons", but here the files hold more. I used the fraction as an assumption.
3. `measured` has no slot for an expected value that cannot be computed (the CN fractions). I recorded the ALM value alone.
4. The CRCNS data are gzip tar archives, which cannot be opened in place as `archives.md` assumes for zips. I read each archive once as a stream and reduced it in memory (12.8 GB, about 12 minutes).
5. Any edit to the entry, even the README, forces a full re-run. I re-ran (20 minutes) after fixing the claim count in the README from 45 to 46.

**4. Runtime and failures**
- The notebook takes 17 to 20 minutes with a peak of 3.2 GB; the whole session ran from 10:40 to 12:32 UTC.
- I could not remove two stray directories from `entries/gao-2018`. The cleanup command needed approval, which this session cannot give, so it was denied and nothing was removed. They are `__pycache__` (compiled helper files) and an empty `.claude` directory the harness created. The entry check passes with them present; they should be deleted before the workflow commits.
