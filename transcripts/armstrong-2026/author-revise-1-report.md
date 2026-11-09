I've revised the attempt for every point in the round-1 report. One outcome changed, the rest are kept, and the entry re-runs cleanly with `entry.py all` (356 s, 0 check errors).

**Outcome changes**
- **fig1n-epoch-rates: blocked → not_reproduced.** The verifier suggested checking the epoch 1 rate without the spike clock. I computed it with the spikes shifted by every lag from -20 to 60 s, in 0.1 s steps (801 lags). The rate is 6.65 to 7.80 Hz under both window readings and both turn types, and never within 2.0 ± 0.1 Hz. The three timed values (peak, suppression, ramp) stay untested. Round 2 will review this change.
- **fig4-ddm-fit stays partially_reproduced**, now marked as resting on an assumption (`assumed`). I followed problem 1 and fitted every reading three ways: all reaction times kept, with a uniform-mixture overlay (PyDDM's robustness option), and with reaction times under 0.1 s dropped.
  - Non-decision time is 0.000–0.005, 0.000–0.039 and 0.080–0.094 s, never within 0.108–0.132 s.
  - The GDDM fits better in 4/4, 0/4 and 4/4 of the fitted readings.
  - A further cell shows that a hard cutoff sets the non-decision time: it lands 0.011–0.030 s under the shortest reaction time kept.
  - In the likelihood profile, fixing it at 0.12 s costs 4.4 BIC, so 0.12 s is less likely but not ruled out.

**Corrections and added outputs**
- **Bug fix, fig2b:** with the per-time counts added, only 212 of 513 trials (503) and 91 of 249 (489) had a value at t = 2 s. A grid time at the end of the turn fell between two trials' samples. After the fix every trial has a value, the 2 s SDs rise (503 7.02, 489 4.06 cm), and the outcome is unchanged.
- **Decoder:** the z-scoring now uses training-fold statistics only. Decoding at the stored onsets is still at chance.
- **Spike clock:**
  - A full listing of both files confirms there is no sync signal.
  - I added a random-onset null for the lag-search z-scores: 489 exceeds its 95th percentile in 2 of 12 windows, 503 in 10 of 12.
  - A straight-line clock fitted from running speed in 503 (11.86 s plus 1.37 ms per s) shows turn-specific responses and decodes trial type at 0.87–0.91. Its residual SD is 0.56 s, and it also decodes before the turn starts (0.655). That is far coarser than the 5–180 ms windows the claims test, and 489 has no usable clock, so those 15 claims stay blocked.
  - This is new: the earlier record said none of the neural findings could be tested, and the finding, notebook and README now describe the 503 offset and drift.
- **figs1:** I added running fractions by row type (503: CL 37.0%, OL_L 1.7%, OL_R 31.8%). The notebook now says the deposited 503 session or curation may differ from the one the paper analysed.
- **table-s1:** the notebook now states that taking the first 1000 rows of 489 as Table S1's trials is an assumption. It also counts all 1611 rows, which fall outside 10% of 1000.
- **Other text:**
  - The header notes that the SI says TTL signals were used to synchronise the recordings.
  - The blocked-claims section notes the counts that can be checked without the clock.
  - I updated the README, the summary and the runtime (6 min). I recorded round 1 under `verifications` for all 33 claims; the verifier agreed with every outcome as it then stood.

**Not done**
- **No reader question:** the verifier found no misreading of the paper, so nothing went into `questions/001341.yaml`.
- **GDDM coverage:** I fitted the GDDM only for sigma 0.25 and the 0–1 s window. The non-decision-time condition fails in every reading, so more fits could not change the outcome.
- **Leak range:** I did not widen it. The leak still sits at a range edge in some fits, and the notes report this.
- **Not committed:** nothing is committed, as instructed. `tools/build_site.py` was already modified when I started and I left it alone.
