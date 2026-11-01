# Verifier report, round 2: Fan et al. 2024 (DANDI:000959, version 0.261020.0242)

The claims file holds 36 claims, and the attempt record gives 36 outcomes: 23 reproduced, 5 partially reproduced, 2 not reproduced and 6 blocked. **Correction to my round-1 report:** its headline counts were wrong. My own table there gives 22 reproduced, 4 partially reproduced, 2 not reproduced and 8 blocked, not 23 and 7.

## 1. Outcomes and assumptions

**Outcomes I agree with.** I agree with 34 of the 36 outcomes as recorded:
- **Unchanged since round 1 (33):** these keep the outcome and the reasons I gave then.
- **fig5a-trigger-duration-unchanged:** now partially reproduced, the outcome I gave in round 1. Cell 95 holds it up: OFC p = 0.61 and 0.36; dmPFC p = 0.019 and 0.028, and 0.020 in the variant.

**The six causal-decomposition claims (blocked, too_large): I agree.** Cell 92 now times the decomposition directly. At the claims file's reading (a), 1,000 ensembles:
- One EEMD takes 13.1 s on one core, which is 209 CPU s per trial.
- The smallest subset any of the six claims needs, the 2,250 OFC epoch trials, costs 130.7 CPU hours, or 55 hours of wall time on four processes.
- The spline floor for any implementation is 12 CPU hours for that subset.

Reading (a) alone is enough to block the claims, so how reading (b)'s settings are chosen does not matter here.

**The two saccade claims: I agree with them as computed, but they rest on an assumption that is not stated.** fig5cd-saccade-counts-unchanged is partially reproduced: cell 101 gives 1 of 4 tests failing under reading (a), OFC macrosaccades p = 0.044. fig5e-h-saccade-kinematics-unchanged is reproduced: cell 105 gives 0 of 14 failing under (a). The problem is the detector:
- **Its output is not physiological.** Cell 101: median saccade duration 147 ms, 95th percentile 1,062 ms, median amplitude 13.7°, 386 saccades per run. Cell 102: gaze velocity inside fixations has a median of 19.7 deg/s and is under the 5 deg/s limit for only 5.4% of samples.
- **The micro/macro labels may not mean much.** The record says itself that many detected "saccades" span several fixations.
- **The outcome depends on the labelling.** Reading (b) gives 0 of 4 and 3 of 14 failing tests, against 1 of 4 and 0 of 14 under (a).
- **The port was never checked against the MATLAB code** on any sample (`microstim.py` has no such check).

Both outcomes depend on this detection standing in fairly for the paper's, including that the paper did not filter the gaze first. No outcome is marked `assumed: true`. These two should be, with the assumption stated. It is not clearly reasonable given the notebook's own diagnostics.

**Other unstated choices.** No other outcome carries `assumed: true`. The remaining choices are recorded as deviations, and I find them reasonable:
- fig5a: the offline Eyes event in progress stands in for the trigger.
- Causal-decomposition reading (b): the example's settings, 0.35 noise and 1,000 ensembles.

## 2. Statements the printed numbers do not support

**Cells 92 and 93 against the attempt record (affects the blocked notes).** The causal-decomposition figures in the record were not updated after the re-run:

| Quantity | Record (figs4a notes and response) | Cell 92 |
|---|---|---|
| One EEMD, one core | 18.3 s | 13.1 s |
| One EEMD, four processes | 9.2 s | 5.5 s |
| CPU time per trial | 293 s | 209 s |
| Every social trial | about 1,590 CPU hours (about 790 hours of wall time) | 1,131.6 CPU hours (475.8 hours of wall time) |

The same holds for the epoch subsets:
- **The record** (ofc-slope, fig4c, fig4d and dmpfc-slope-positive, and the responses) says "2,250 trials ... about 183 CPU hours (92 hours of wall time) ... ACCg about 191".
- **Cell 92** prints 130.7 CPU hours (55.0 hours of wall time) for OFC and dmPFC, and 136.0 for ACCg.

The outcome stands, but every one of these figures is wrong.

**Cell 27 against the record (fig2a notes).** The record has "dmPFC (whole Face -2.46 and -0.0026)". Cell 27 prints −2.5599 and −0.0027, and cell 28's text agrees with cell 27.

**Cells 86 and 87, and the record (partner-monkey-unchanged).** The text says "1 of the 21 tests does". Cell 86 prints 18 tests: 6 distance tests, then 3 each for interval (a), interval (b), latency (a) and latency (b).

**Cell 90.** It says the five excluded days are "the days the paper names". The paper gives only their composition. The dates come from the code, as cell 89 and the record say.

**Cell 107, the Summary.** "6% of the M1 Eyes events have a mean position outside the Eyes rectangle" is true only of social runs. Cell 3 gives 6.3% for social runs and 10.7% for Dot runs, about 8% over both. The record's finding states both figures correctly.

**Cell 93.** "would still exceed it for every subset" compares CPU hours with a wall-time limit. 12 CPU hours spread over enough cores would fit in an hour. At four processes it does not, so the conclusion holds, but the sentence should say so.

**Minor.** In the figs1d notes, monkey T's control trials per day are 71 to 77 (cell 16), not 71 to 76.

**Everything else matches.** Every other "**Result:**" sentence, the rest of the Summary, the entry README and the other notes and findings agree with the printed outputs.

**My round-1 reasons in the record.** The record states them faithfully and in substance in my own words. Some entries fold my B points into the reason, which is acceptable. For both saccade claims my blocked reason was "other". The record keeps the outcome, blocked, and quotes my objection to not_runnable, which the author disputes. I cannot check that against the protocol here.

## 3. Round-1 points

**Resolved:**
- **B2:** both saccade claims are now tested with the outside detector.
- **B3:** the cost is now timed directly and per subset; too_large is shown. Only the stale figures in the record remain (section 2).
- **B4:** the bootstrap is run under the code's reading too; still not reproduced.
- **B6:** the trials with no Eyes event are broken down and spread evenly; the dmPFC result holds in the variant.
- **B7:** the axis label is corrected.
- **B8:** the ROI squares are the intersection over each day's runs; the recalibrated days are dmPFC and ACCg days.
- **B12:** times run up to 9,955 s, below the 10⁶ s offset.
- **B13:** the tie rule is recorded as a standard choice.

**Resolved as far as my round-1 questions go:**
- The mutual tables are shown (cell 3).
- The control-run listing is added (cell 10).
- The groups of one file are printed (cell 3). That file is a Dot run, so the absence of saccade tables is shown only for one control file, not for a social one.

**Acknowledged, nothing more needed:** B9, B10 and B11.

**Still open, bearing on a conclusion:**
1. **figs1e-eyes-vs-rdm-comparable (B1).** It is not reproduced only because of the claims file's deciding reading (a), which I still take to misread the paper. That is referred to a reader and is pending.
2. **fig3b-ofc-inter-looking-interval (B5).** p = 0.044 becomes 0.058 when the 91 events that start on the trial sample are counted. The question is put to the paper's authors; the outcome stays fragile.
3. **Saccade claims (new).** Both outcomes rest on a detector whose output, by the notebook's own diagnostics, is not physiological. The port is unvalidated, and the outcome changes with the micro/macro labelling. This assumption should be marked and stated (section 1).
4. **Causal-decomposition figures in the record (new).** They do not match cell 92. The outcome is not affected, but the notes and responses need correcting.
5. **partner-monkey-unchanged test count (new).** "1 of 21 tests" should read "1 of 18" in cell 87 and in the record. The outcome is not affected.
