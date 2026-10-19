Steps 1 to 6 are done: the entry passes `check` and `all`, and the handover package is built in `executed/001692-bouabid-2026/handover/`. I did not verify my own work and committed nothing.

Paper: the full bioRxiv preprint (CC-BY). Dandiset: version 0.260303.1724, the version the paper's Zenodo Key Resources Table cites and the only published one.

## 1. Outcome per claim (33 claims)

| Claim | Outcome |
|---|---|
| fig1e-dominant-polarity (133/128, 41/32 against 132/127, 42/31) | reproduced |
| fig1f-adls-hotspot | partially reproduced: the hotspot is negative, anterior and dorsal, but its centroid is 0.02 mm medial of the median site |
| fig1h-in-vs-out, fig1f-positive-posterior, ed2-hotspot-per-mouse | reproduced |
| ed1-controls-no-organization | not reproduced: control correlations are as strong as the sensor mice's (median abs r 0.238 against 0.240), and a hotspot is found |
| fig2a-directionality, fig2b-pairing-overlaps-hotspot, ed3e-transient-rates-in-hotspot | reproduced |
| fig2-magnitude-correlations (115/70/90/76 against 121/81/97/78), fig2d-magnitude-in-out | partially reproduced |
| fig3b-reward-correlation | partially reproduced (52 positive sites against 58) |
| fig3d-reward-in-out, fig3e-reward-hotspot-overlap | reproduced |
| fig4-cue-sequence | not reproduced (58 of 75 sites against 49; the majority statement holds) |
| fig4c-cue-correlation | partially reproduced |
| fig4h-extinction-correlation, fig4d-cue-in-out, fig4j-extinction-in-out | reproduced |
| fig5d-initiation-responses | partially reproduced |
| fig5-latency-order | reproduced (two medians at the edge of the tolerance) |
| fig5e-initiation-topography | not reproduced |
| fig6a-initiation-correlation, fig6c-initiation-in-out, fig6g-invigoration-in-out | reproduced |
| fig7-da-release (179/180), fig7f-ach-dip-in-out | reproduced |
| fig7e-ach-suppression (147 against 116), ed9-cohort-hotspot (overlap p = 0.085) | partially reproduced |
| fig8b, fig8fg (Zenodo source data) | reproduced |
| fig8e (Zenodo source data) | partially reproduced (stimulus F 47.7 against 36.4) |
| fig8c (Zenodo source data) | blocked, methods_underspecified |

## 2. The dandiset
- The site counts match the paper exactly: 174, 75 and 180.
- Every photometry series states 9 Hz. The timestamps, the Methods and the code all give 18 Hz.
- No field says which experiment, cohort or Pavlovian phase a session belongs to. I inferred these from subject names, indicators and how many light cues were rewarded.
- The Pavlovian files have no tone cue events.
- One session, UG27 240313r, lacks the artifact-removed green series.
- Some device and session descriptions are wrong or inconsistent:
  - The excitation-source descriptions describe 405 nm light at 100 Hz.
  - The mutant sensor is named ACh4.3mut, where the paper says ACh3.0-mut.
  - The reward volume and intervals differ from the Methods.
  - The micro sign is stored mis-encoded.
- Figure 8's slice data are only on Zenodo, and their source data disagree with the legend on slice and mouse counts and on two stimulus F values.
- The analysis code (HoweLab/BouabidVu2026 at 833fa3d) has two errors in `fig4_pav.m`: it loads the wrong session directories, and it uses the DA peak where the legend says trough. Its parameters also differ from the Methods in several places.

## 3. Where the protocol was unclear, wrong or missing something
1. **A count above the reported value.** "Partially reproduced" covers a weaker effect only. My criterion for fig4-cue-sequence gave partial credit only for a shortfall, so 58 against 49 counts as not reproduced. I followed the wording and explained this in the notes.
2. **Tolerance for means reported as mean ± SD across sites.** "The stated spread" would give an almost unfalsifiable tolerance. I used the implied standard error and recorded the reason.
3. **A method too heavy for the time limit.** The protocol does not say whether to simplify or to block as not_runnable. The MATLAB hotspot procedure uses 10,000 shuffles and an Allen atlas mask; I simplified it and listed every simplification as a deviation.
4. **Code with evident bugs.** The protocol only says to follow the code where the Methods are silent. Where the code is clearly wrong (the session loop in `fig4_pav.m`), I followed its evident intent and recorded the bug as a finding.
5. **Whether code read for parameters is an "input".** I listed the code repository as one, while stating that no data came from it.
6. **Inferring labels from the data versus taking them from outside.** The Zenodo table maps sessions to experiments, but I inferred phases from events so every claim stays `data: dandiset`. The protocol does not say which to prefer.
7. **Summary data as `data: elsewhere`.** The Figure 8 Zenodo source data are per-slice values, not raw recordings. I classified those claims as `elsewhere`.
8. **Clock check for continuous sessions.** In place of decoding with shifted labels, I compared responses at true and shifted event times. For spontaneous sessions I used locomotion initiations; the contrast there is weak (ratio 1.28 for UG28).
9. **Fitting the time limit.** For the control mice I used 15 of their 114 sessions and recorded this as a deviation.
10. **Getting the paper.** bioRxiv blocked curl (Cloudflare) and Europe PMC's full-text endpoint returned an error. I got the PDF through the web-fetch tool and saved it under `paper/`.

## 4. Runtime and failures
- The notebook runs in 9.7 min; `entry.py all` takes 10 min and passes.
- My first metadata scan of all 339 files took 29 min because h5py serialises threads. The helper now uses processes.
- Failures I hit and fixed:
  - One load failed on the missing series; those sessions are now skipped and reported.
  - Constant red traces at some control sites gave undefined correlations; those are now averaged over the defined sessions, and the one site with none is dropped.

Untracked dotfiles (`.bashrc` and others) and a `scripts/` folder appear in `git status`; I did not create them and left them alone.
