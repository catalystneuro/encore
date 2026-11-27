**Verifier report, round 2: Mills et al. 2026 on DANDI:001203 (attempt mills-2026-01)**

Counts are taken from the files. The claims file has 48 claims and the attempt record has 48 outcomes: 2 reproduced, 5 partially reproduced, 6 not reproduced and 35 blocked (29 data_missing, 3 metadata_insufficient, 3 not_runnable). The notebook now has 54 cells, so cell numbers differ from round 1. I found no new place where the claims file misreads the paper.

**1. Outcomes and assumptions**

I agree with all 13 tested outcomes and all 35 blocked ones. Caveats:

- **figs10-no-reward-relationship** (partially reproduced, `assumed: true`): I agree. Using the tone duration as the latency follows the Methods and is stated. But with that latency, the 10 ms bin gives p = 0.047 (cell 19), and the claims file names 10 ms as the bin Figure S6 shows. So the across-trials half of this claim of absence holds under 3 of 4 readings, not cleanly. The notes say this.
- **figs13-imaging-mice-discriminate** (reproduced, `assumed: true`): I agree. The assumptions (pixel scale, haunch as the rear body centre) are stated and reasonable. The whole difference comes from darting (cell 34), so the result rests on the darting threshold, which depends on the assumed scale. Drd2 p = 0.046 is near the threshold.
- **figs15-no-context-encoding** (not reproduced, `assumed: true`): I agree. Drd2 peak rate gives p = 0.042, and Drd2 freezing is not higher in Context A whatever the scale (cell 48). The assumption is stated and does not decide the outcome.
- **fig5h and fig5k** (not reproduced): I agree under the criterion. Both still rest on uncurated ROIs, 2.6 and 3.3 times the paper's n, with mouse-level and deconvolved tests not significant. This is stated as a deviation.
- **fig5m** (not reproduced): see section 3. One reading that is not shown in the notebook may decide this outcome.

**2. Sentences the printed outputs do not support**

- **fig5m note:** "While preparing, a version of the window reading that dropped the 233 ROIs whose clips start late gave rho 0.76, p = 0.017; it was not run here". No cell prints this.
- **figs14 note:** "plus one 'undefined' trial in some". No cell prints this either.
- **Cell 26 and the fig2q note:** cell 26 says the 3 mice are "the mice with the most responsive units", and the note says "the mice with the most units responding to CS-shock". One of the 3 is 7008, which has 0.00 CS-shock-responsive units in cell 5 and a sustained CS-shock z of −0.04 in cell 16.
- **Cell 0:** "31 calcium imaging discrimination sessions (30 mice, one deposited twice)". Cells 9 and 10 show 34 files and 33 mice.
- **Cell 11, finding 1 and the figs5, figs10lm and fig3fg notes:**
  - "changes by up to 200 s between quarters": cell 8 shows 7001 going from +288.0 to −241.2 s and 7049 from +242.2 to −228.0 s.
  - "constant (within 0.6 s)" includes 3024, whose quarter lags run from −10.0 to −9.2 s (0.8 s).
  - Cell 11 says the lags are "different in each" session, and the Summary (cell 52) says "by a different amount in each session". In cell 7, 3016 and 3024 both have −9.8 s.
  - "clusters … in five of the six 2018 sessions": 3014's best spread is 60.4 px and its quarter lags drift (cells 7 and 8), so four sessions is supported.
- **fig2p note:** "reading (b) and 10 ms bins give p 0.15 to 1". Cell 51 shows p = 0.0986 (10 ms, reading (a), CS-reward phasic).
- **Finding 9:** "each discrimination session has 15 imaged CS-reward trials". Seven sessions have 17 to 19 (cell 10).
- **Note and cell 32 on fig3h:** "two mice (3026, 6197) are at chance". 6197 scores 0.53 to 0.60 against chance near 0.49 (cell 31), and no per-mouse test was run.
- **README:** "about 20 minutes". Cell 53 prints 25.1 minutes.

Every other number in the "**Result:" cells, the Summary, the README and the outcome notes matches the outputs.

The record states my round-1 reasons faithfully and mostly in my wording. Recording "agrees: false" for fig2o-ast-greater and fig2p is a fair reading of my problem 2.

**3. Round-1 points**

All ten points are resolved:

- 1 (figs10 run)
- 2 (one-sample test run; ASt against CeA printed)
- 3 (mouse-level tests, decay table, detrended variant)
- 4 (displacement distribution; freezing and darting shown separately)
- 5 (tone-duration latency)
- 6 (attainable Wilcoxon p stated)
- 7 (probe_depth, label and histology listed)
- 8 (complete-space distance is the Methods' reading)
- 9 (per-quarter lag fit)
- 10 (variant without the thin sessions)

Of my section C items, clip coverage and the mouse-level tests are answered. The GEO data remain outside access.

What remains that bears on a conclusion:

- **fig5m:** the criterion says reproduced "under one reading". The record says the full-window reading, with late-starting ROIs dropped instead of early bins, gave rho 0.76, p = 0.017. If so, the outcome would change. That reading should be run and printed in the notebook, or the reason for excluding it argued there.
- **fig5h and fig5k:** the significant results come from the uncurated ROI count. This is inherent in the data and stated.
- **figs13 and figs15:** the paper's freezing rule, applied to these poses, counts only frames that nearly repeat the previous pose (finding 12). figs13 therefore passes on darting alone, under the haunch and pixel-scale assumptions.

**4. Critical findings**

- **Finding 1** (Open Ephys poses not on the clock of the spikes and trial table): shown.
  - Cell 5 shows spikes and trial events share a clock.
  - Cell 7 shows the nose clustering at port entries at nonzero lags, with the shock-speed check agreeing within 0.6 s in 3012, 3016 and 3024, and no clustering in the 2019 sessions.
  - Cell 8 shows the drift; cell 9 is the imaging control.
  - **Critical is right:** these are signals on different clocks, and the files don't say so. The "up to 200 s" and "five of six" wording should be corrected (section 2).
- **Finding 6** (duplicate deposits): shown.
  - Cell 4: the two 6197 files have identical spike trains and CS onsets.
  - Cell 9: the two J933 files have identical traces. The `_ses-` copy has 55 port entries against 193, with best lag −236.4 s and spread 27.0 px, against 1.6 s and 2.8 px for the other copy.
  - **Critical is right:** one recording deposited as two, plus port entries that are silently wrong. The finding's last sentence, "The duplication shows in the shared subject names", should be dropped. It is inaccurate, since many subjects legitimately have several files (J895, K008 and others, cell 3), and it contradicts the critical rating.
