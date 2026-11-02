# Kauvar, Richman, Liu et al. (2025) from dandisets 001326 and 001347

Tests the findings of [Kauvar, Richman, Liu et al. (2025)](https://doi.org/10.1126/science.adt3971) on
[DANDI:001326](https://dandiarchive.org/dandiset/001326/0.250528.1957), the brain-wide mouse Neuropixels
recordings (13 sessions, 10 mice), and on the behavior in
[DANDI:001347](https://dandiarchive.org/dandiset/001347/0.250528.0702).

The claims file has 52 findings of the paper and two link claims added by this attempt. 42 are tested: 31 reproduced, 8 partially reproduced and 3 not reproduced; 12 are blocked (8 human iEEG findings for lack of time, 4 whose data are not in DANDI:001347).

| Claim | Outcome |
|---|---|
| `fig4-recordings-scale` | Reproduced |
| `fig4de-response-clusters` | Partially reproduced |
| `figs31b-cluster-overrepresentation` | Reproduced |
| `fig4g-ketamine-alters-slow-clusters` | Not reproduced |
| `fig4i-rise-times-unchanged` | Reproduced |
| `fig4h-decay-shortened` | Reproduced |
| `fig4h-decay-anatomical-progression` | Reproduced |
| `fig5d-emotion-dimension-accumulates` | Partially reproduced |
| `fig5e-late-reduced` | Not reproduced |
| `fig5e-rapid-unchanged` | Reproduced |
| `figs32c-regional-emotion-dimension` | Reproduced |
| `fig5g-tau-persist-model` | Reproduced |
| `figs33-alternative-models` | Reproduced |
| `fig6d-mouse-persistent` | Reproduced (rests on an assumption) |
| `fig6f-mouse-fast-unchanged` | Reproduced |
| `fig6b-persistent-dimension-distributed` | Reproduced |
| `fig6h-mouse-timescale` | Reproduced (rests on an assumption) |
| `fig6j-mouse-coupling` | Partially reproduced (rests on an assumption) |
| `figs34d-tone-fast-unchanged` | Reproduced (rests on an assumption) |
| `figs34e-tone-persistent` | Reproduced |
| `figs34f-tone-shorter-than-puff` | Reproduced |
| `figs34g-tone-timescale` | Partially reproduced (rests on an assumption) |
| `figs34h-tone-coupling` | Not reproduced |
| `figs30-correlation-structure` | Partially reproduced |
| `figs29-rsp-oscillations` | Partially reproduced |
| `link-001347-condition-labels` | Reproduced |
| `link-001347-recorded-sessions` | Partially reproduced |
| `fig4b-recorded-eye-closure-ketamine` | Reproduced (rests on an assumption) |
| `fig5b-recorded-accumulation` | Reproduced (rests on an assumption) |
| `figs34c-tone-no-eye-closure` | Reproduced |
| `fig1k-mouse-ketamine-late-closure` | Reproduced |
| `fig1l-dissociatives-preinfusion` | Reproduced |
| `figs2bc-mouse-early-late` | Reproduced |
| `fig1m-accumulation-persistence` | Partially reproduced |
| `figs2g-scaling-puff-number` | Reproduced |
| `figs2h-dose-response` | Reproduced |
| `fig1p-anesthesia-abolishes-both` | Reproduced |
| `figs5-other-drugs` | Reproduced |
| `figs6-vpm-muscimol` | Reproduced |
| `fig5hi-behavior-model-doses` | Reproduced |
| `fig1e-human-ketamine-late-closure` | Reproduced |
| `figs1b-human-early-closure-unchanged` | Reproduced |
| `figs4-reward-licking` | Blocked: other |
| `fig1f-human-reports` | Blocked: other |
| `fig2d-cadss-ketamine` | Blocked: other |
| `figs14g-cadss-correlation` | Blocked: other |
| `fig2g-six-factors` | Blocked: too large |
| `fig2i-factors-1-2-ketamine` | Blocked: too large |
| `fig3b-cluster-test-networks` | Blocked: too large |
| `figs12-erp-not-blink` | Blocked: too large |
| `fig6c-human-persistent` | Blocked: too large |
| `fig6e-human-fast-unchanged` | Blocked: too large |
| `fig6g-human-timescale` | Blocked: too large |
| `fig6i-human-phase-locking` | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001326-kauvar-2025-01.yaml`](../../attempts/001326-kauvar-2025-01.yaml).

- `reproduce_kauvar_2025.ipynb`: the electrophysiology of DANDI:001326. It takes about seven minutes, most of it streaming and reducing the files.
- `reproduce_kauvar_2025_behavior.ipynb`: the eye closure of the recorded mice, the behavior-only mouse experiments and the non-implanted participants, from DANDI:001347. It takes about three minutes.
- `kauvar.py`: loading and the measures of the paper's code (unit selection, coding and emotion-like dimensions, timescales, coupling, the first-order model) for DANDI:001326.
- `behavior.py`: loading, the session lists of the paper's code and the eye-closure measures for DANDI:001347.
