I took up all five answers. All of them were "the paper does not say", and each added readings to the claims file. Two outcomes changed: ephys-pt-it-onset-not-detected went from blocked to reproduced, and fig8d-pt-earlier-than-it went from not reproduced to reproduced, though only under some readings. The other affected claims kept their outcomes. The entry passes check and the clean run (0 errors, about 18 min, numbers the same on two runs), and the handover is in `executed/000015-chen-2017/handover/`. Nothing is committed, and I did not verify my own work.

| Question (claim asked on) | What the answer changed | Claim | Before | Now |
|---|---|---|---|---|
| 1. How to apply the onset test to the Li et al. (2015) units (ephys-pt-it-onset-not-detected) | Named the method: 400 ms windows in 100 ms steps; the four trial types without photostimulation or early licks; time from pole movement onset; baselines O1 and O2; rules S1 and S2; both bootstraps (H1, H2) | ephys-pt-it-onset-not-detected | blocked (methods_underspecified) | reproduced |
| 2. dF/F when the baseline F0 is zero or negative (fraction-selective-alm-mm) | V1 (dF/F as computed) decides; V2 (those ROIs left out) is only a check | fraction-selective-alm-mm | not reproduced | not reproduced |
| | | figs4-peak-shift | not reproduced | not reproduced |
| | | fig8d-pt-contra-bias | not reproduced | not reproduced |
| | | fig8d-mm-posterior-preferring | not reproduced | not reproduced |
| | | fig8d-error-outnumber-correct | partially reproduced | partially reproduced |
| 3. Onset rule (fig8d-pt-earlier-than-it) | Added rule S2 (first bin from which the curve stays above threshold up to the go cue) beside S1 (first single bin) | fig8d-pt-earlier-than-it | not reproduced (0.215 s) | reproduced (1.801 s) |
| 4. Sample-epoch level and end of delay (figs4-peak-shift) | Readings L1/L2 and E1/E2; E2 (mean over the last 0.5 s before the go cue) is new | figs4-peak-shift | not reproduced | not reproduced |
| 5. MM value in the delay (fig6-lick-direction-spread) | Mean or maximum over the delay, either one enough | fig6-lick-direction-spread | partially reproduced | partially reproduced |

- **ephys-pt-it-onset-not-detected (was blocked):** I analysed 45 PT and 26 IT units from 50 sessions of dandiset 000010. No combination finds PT earlier at p < 0.01. The IT minus PT onset is 0.7 s under rule S1 (p 0.30 to 0.34) and 0.2 s under S2 (p 0.15 to 0.20).
  - One IT unit has no error-right trial once photostimulated trials are removed, so it cannot be fitted and is left out.
  - Spikes are stored only from 0.52 s before trial start, so baselines O1 and O2 are the same two windows. The 8 combinations therefore give only 4 distinct results.
  - Trials were flagged as photostimulated from the laser pulses or the `photostim_start_time` events (4,152 of 16,571 trials).
- **fig8d-pt-earlier-than-it (now reproduced, but fragile):** the criterion asks for a match under any one combination of readings. Two combinations meet it, both with rule S2, 66.7 ms bins (T2) and the bootstrap over cells (H2): 1.80 s with p = 0.003, and 1.40 s with p = 0.006.
  - With frame bins (T1) the p-value is 0.021 or 0.170.
  - With the hierarchical bootstrap it is 0.065 to 0.319.
  - Rule S1 still gives about 0.2 s, as before.
- **dF/F with zero or negative F0:** V1 was already what decided these claims, so nothing changed in how they are tested. V2 is now reported in full. It does not change any outcome. The one place it reaches a bound is fig8d-error-outnumber-correct: under V2 its part (b) reaches 2.20 SD with frame bins, but only V1 decides.
- **figs4-peak-shift:** the new E2 reading is 0.205, above both sample-epoch levels, so that part holds as before. The claim still fails because the MM mean peaks after the ALM mean under every combination.
- **fig6-lick-direction-spread:** both readings were already run and both hold, so nothing changed.

Each affected claim's notes in `attempts/000015-chen-2017-01.yaml` say what the answer changed. I also updated the notebook, its conclusions and summary, the helper, the README and `entry.yaml`, where the runtime is now 18 minutes. Separately, I removed the bold labels such as "Paper." that were already in the notebook, so that only the "Result:" openers are bold.
