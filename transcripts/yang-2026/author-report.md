## Report: yang-2026, attempt 01 (author run)

All 25 claims were tested and none is blocked. 15 are reproduced (one of them rests on an assumption, one is seed-sensitive) and 10 are partially reproduced. The notebook passes `tools/entry.py all` in a clean environment, taking about 29 minutes with a peak memory of 9 GB. The handover is built in `executed/yang-2026/handover/`. Nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| session-counts | reproduced (all eleven counts equal the paper's) |
| table1-early-joint-fraction | reproduced |
| table1-early-axis-fractions | reproduced (10/10 within tolerance) |
| axes-cosine | reproduced |
| fig1e-laser-vs-control-split | partial: the lowest other-region ratio is 2.7, against 3.3 ± 0.33 |
| fig1-1b-corrected-joint-fraction | partial: no correction gives both the medulla and thalamus values |
| fig1-1c-fraction-vs-neurons | reproduced (rho −0.37, p = 3e-10) |
| fig1-1d-without-video-regression | reproduced (thalamus 0.116) |
| fig1b-example-session | partial: the paper's session ranks second, 0.0001 behind another |
| table1-decoding-early-vs-prelick | partial: 7 of 10 values within, 8 needed; the early accuracies are low |
| fig2a-decoding-rises-after-go | reproduced |
| matched-reaction-time | reproduced |
| fig2d-choice-share-flat | partial |
| fig2e-action-share-rises | partial |
| fig2b-go-aligned-joint-fraction | partial: the 250 ms bin matches, the delay range does not |
| fig2-1-energy-outside-subspace | partial: ALM at onset 25.8 matches; before onset 0.053 against 0.09 |
| fig3a-matched-pairs | reproduced (2,667 pairs, median 1.3 ms, largest 99 ms) |
| table1-prelick-residual | reproduced |
| fig3e-residual-ratio | reproduced |
| fig3-1ab-distances-scale | reproduced |
| fig3-1d-matching-keeps-distance | reproduced |
| fig3-1c-alm-early-residual | reproduced, resting on an assumption (12.59 binned; 18.4 unbinned) |
| fig3c-residual-time-course | reproduced (7/7 values within tolerance) |
| fig3c-late-residuals | reproduced, seed-sensitive (4 of 5 regions under 3 of the other 4 seeds) |
| fig3b-example-plane | partial: the plane holds 70–97% of the difference, against 25% |

### 2. Dataset, assumptions and questions

**Dataset.** I pinned version 0.231012.2129: the paper cites it and it is also the latest published version. Earlier versions hold the same 174 assets without the raw ephys; none of the raw series is read here.
- 168 sessions have photoinhibition, and 112 late-delay bilateral sessions come from 19 mice.
- No session was deposited twice.
- Spikes, trials, licks and video share one clock. This rests on two contrasts: the ALM effect is larger after laser onset than before it in 99 of 99 sessions, and the tongue is detected more often just after a lick than at shifted times in 112 of 112.

Findings recorded about the data:
- 4 units have spike times out of order (format_error, minor).
- A unit's region exists only as the probe target and a CCF annotation; neither is documented as the analysis label (minor).
- The video keypoints have a likelihood per frame but no detection flag. The tongue is undetected in the choice window on 82% of trials (minor).
- In 2 sessions the video does not cover the trials to within 5 s (minor).

**Readings the data settled.** Each of these is a reading the claims file lists, and in each case the data matched only one:
- Laser trials with an early lick are dropped. Only this reading gives the Table 1 counts exactly.
- Matching takes the closest control trial. A random match within the caliper gives a median difference of 43 ms, not 1.3 ms.
- Missing keypoints take the control mean. Dropping trials without them gives the wrong fractions.

**Assumptions.**
- One outcome rests on an assumption: the early-window residual is scored in two 50 ms bins, as all of the paper's other distances are (Methods, Matched distance; Time courses).
- Standard choices that do not change any result: a keypoint counts as detected at likelihood ≥ 0.9 (cuts of 0.5 and 0.99 change no fraction by more than 0.002), and the penalty is chosen by an inner 5-fold search.

**Questions for the paper's author** (recorded as two `methods_unavailable` findings):
- Was the early residual computed in 50 ms bins?
- Please confirm the early-lick, matching and keypoint choices above.
- How were the Fig 1-1B correction, the 25% plane fraction (Fig 3B) and the 0.09 pre-onset energy (Fig 2-1A) computed?

**Questions to a reader:** none.

### 3. Protocol issues

1. **Seeds.** The paper states one seed, 17; the protocol requires the claim seeds. I used the claim seeds and recorded this as a deviation.
2. **Re-runs after text edits.** Any edit to the entry forces a full re-run, so the "Result" text had to be written before the last run. With a 30-minute notebook this cost three extra full runs: one to fix conclusions, one to add the likelihood-cut variant, one to remove bold. A rule allowing markdown-only edits without re-execution would help.
3. **Author readings versus criterion readings.** Several criteria say "reproduced under any reading", while step 1.6 says to adopt one reading when they disagree. It is unclear how the two interact when the author adds a reading the criterion does not list (the early-residual binning). I applied step 1.6 and set `assumed`.
4. **`measured` when no reading matches.** The protocol says what to record when several readings match, but not when none does. I recorded the reading the outcome rests on (energy, reading b), or otherwise the first one listed.
5. **Clock check.** The suggested decoding check does not fit this dataset. I used the photoinhibition contrast and the lick/tongue contrast instead.
6. **Region reading (b).** This reading needs the Allen ontology, an outside input the claims file does not name, so it was not run. Reading (a) matched the counts exactly.

### 4. Runtime and failures

- Notebook: about 29 minutes per run (5 min survey, 13–14 min streaming, 9 min decoding), peak memory 9 GB.
- Session: about 3 h 45 min in total, including four full runs.
- Nothing failed.
