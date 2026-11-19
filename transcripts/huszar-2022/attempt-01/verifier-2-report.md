# Verifier report, round 2: Huszar et al. 2022 (doi:10.1038/s41593-022-01138-x), DANDI 000552 v0.230630.2304

The claims file has 35 claims and the attempt record has 35 outcomes, with the same ids. The record gives 5 reproduced, 4 partially reproduced, 3 not reproduced, 22 blocked as data_missing and 1 blocked as methods_underspecified. The notebook cell numbers below are 0-based indices in the re-executed notebook. They differ from the numbers in my round-1 report. I saved the paper text (the PMC10807234 author manuscript, BioC JSON and plain text) under `paper/`.

## 1. Outcomes

I agree with 34 of the 35 outcomes as stated. For fig7fg-convergence-cofiring I agree it is blocked, but its notes rest on a wrong session count; see below.

- **cohort-birthdates, reproduced:** I agree. This is the change I asked for in round 1.
- **sessions-durations, partially_reproduced:** I agree.
- **spwr-duration, reproduced:** I agree.
- **unit-count, not_reproduced:** I agree.
- **maze-cohort, reproduced:** I agree.
- **maze-task, not_reproduced:** I agree.
- **novel-explorations, partially_reproduced:** I agree.
- **fig5e-pv-decorrelation, partially_reproduced:** I agree under the fixed 5 Hz rule. The 2.59 Hz variant was chosen after the results were seen, and its turn-2 median of 0.357 sits just inside the lower bound of 0.355. The record correctly does not let the variant change the outcome.
- **fig6c-theta-rate-preserved, reproduced:** I agree. rho is 0.726.
- **fig6c-novel-ratemap-corr-higher, not_reproduced:** I agree.
- **fig6d-info-lower-novel, partially_reproduced:** I agree.
- **fig6d-rate-lower-novel, reproduced:** I agree, because the criterion is met (0.794 and 0.714 Hz, both within tolerance; rank-sum p = 0.041). The outcome is fragile: the paired test gives p = 0.19, every variant gives p ≥ 0.075, and one of the three mice goes the other way. The record says so.
- **The 22 data_missing blocks:** I agree.
- **fig7fg-convergence-cofiring, blocked (methods_underspecified):** I accept the block. The detector here gives 0.448 connections per possible pair against the paper's 0.173, so this is not the paper's procedure. Two parts of the reasoning are weak:
  - The Methods do name a test. It uses "3× bins surrounding that of peak", while `is_monosynaptic` uses fixed lags of 0.8 to 3.2 ms. So the gap is at least partly in this implementation, not only in what the paper leaves out.
  - The one test session, e15_13f1_220117, belongs to a mouse that by the attempt's own matching is not among the 15 mice of Fig. 7f.

## 2. Sentences the printed outputs do not support

I checked every Result conclusion and the Summary sentence by sentence. All their numbers match the outputs except the following.

- **"The units of 31 of the paper's 96 sessions are also not in the dandiset."** This is in cell 62. Cell 63 also prints "Files with units: 65 of the paper's 96 sessions". The record's fig7fg notes repeat it as "include 31 whose units are not in the dandiset".
  - The attempt itself identifies the paper's 96 sessions as the files without e15_13f1 and e16_3m2 (cell 26, and the paper_inconsistency finding).
  - Those two mice account for 8 of the 65 files with units. That leaves 57 of the 96 sessions with units, so 39 lack them, not 31.
  - My round-1 phrase "65 of 96 sessions" made the same error.
- **"neither the processed nor the raw files have a stimulation channel".** This is in cell 62. The same generalisation appears in the record's ed2 notes ("the raw files hold only the ElectricalSeries and LFP"), the first Summary bullet ("in the processed or the raw files") and the README ("no optogenetic pulse times … are stored"). Only one of the 13 raw files was listed in full (cell 15). The other 12 were probed for two fixed keys only (cell 14). Cell 16 itself states this limit correctly.
- **"where clipping around pulses given every 200 ms would leave several in each window"** (cell 16). The paper (Methods, Stimulation protocol) gives blocks of five pulses at 200 ms intervals, with no interval stated between blocks. It also says data were "clipped out", which does not say the samples were zeroed or held flat. "Several in each window" is therefore an assumption, though the sentence that follows is suitably hedged.
- **"Pairs per session (familiar, novel)"** (cell 54). The columns are actually (novel, familiar): the novel column sums to 242,655, and the sessions with no novel maze show 0 in the first column. This does not change any conclusion.
- **"match the paper's figure-eight and two linear tracks"** (cell 42). Reading the 164 cm T-maze as the paper's novel figure-eight is an interpretation and should be stated as one. This is minor.

Everything else checks against the outputs. That includes the README table, the 22-claim count, the run time of about 7 minutes, and the record's notes on cohort, sessions, ripples, units, maze, novel explorations, fig5e, fig6c, fig6d and the LFP being in 8 of the 9 novel sessions.

The record's verification entries state my round-1 reasons faithfully and in substance in my words. The "34 of 35" agreement count is correct for round 1. The one outcome that changed since then is fig6d-rate, which moved from partial to reproduced after the `running_rate` fix.

## 3. Status of round-1 points

**Resolved:**
- **B1:** `running_rate` now cuts stretches at trial changes and gaps; I read the code at `huszar.py:373`. There is a synthetic test with an assert (cell 49) and the requested output on gaps and running across trial edges.
- **B2:** sex is now tabulated per file and taken by majority, with both readings printed.
- **B3:** the count is 9, and the 7 epochs without position are excluded and described as picked after seeing the data.
- **B5:** a sign test across sessions and per-session rank-sum tests were added (cell 54).
- **Unit names and fig7fg feasibility:** the questions about `unit_name`/`clu_id` and the per-session interneuron and connection counts were answered with outputs.
- **B6, B8, B9:** these do not affect any conclusion and the responses are acceptable.

**Remaining points that bear on a conclusion:**
1. **fig5e still depends on the cell-rate rule (B4).** The difference is now disclosed: at 2.59 Hz all four medians fall within tolerance, at 2 Hz the arm median falls below. The outcome rests on an unvalidated 5 Hz choice that the criterion fixed in advance.
2. **fig6d-rate is reproduced only by the pooled test the criterion names (p = 0.041).** Every robustness check gives p > 0.05.
3. **fig7fg rests on one session from a mouse outside Fig. 7f's cohort.** The session count in its notes should read 39, not 31. The block reason relies on a detector that departs from the Methods' peak-centred bins.
4. **The "no stimulation channel in raw files" statement covers 1 of 13 files (B7, partly resolved).** It is stated generally in cell 62, the record, the Summary and the README. It bears on ed2 and the other label-dependent blocks only through whether pulse times could be recovered. The scan of that one file also suggests the stimulation period is not in the deposited recording.
