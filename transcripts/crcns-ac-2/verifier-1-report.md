**Verifier report, round 1: DeWeese & Zador 2004 on CRCNS ac-2**

The claims file has 23 claims. The notebook tests all 23, and I judged each one from the notebook's printed outputs. No attempt record was among my materials, so the count comes from the claims file alone. The archive listing matches the notebook's MD5 sums (S3 ETags `af006ca3…`, `6ffd4657…`). The helper functions behaved correctly on synthetic inputs:
- `heights` finds the right peak.
- `cull` removes a trial with a negative scale factor and a time-shifted trial.
- `estimate_q` gives about the residual variance divided by the mean.
- The shuffle reduction is about q/(N−1).

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig2-stereotyped-shape | partially_reproduced | Latency 26.5–41.5 ms and height 1.19–18.12 mV are inside the widened ranges, and the median aligned correlation is 0.991 (cell 16). Only 19 of 33 neurons peak within 50 ms for their largest tone, so the "all neurons" part fails. |
| fig3a-reliable-neuron | reproduced | 022801md01b: <q> 0.876 mV over 26 tones, 20 repetitions, q at 31,118 Hz 0.229 (cell 14). |
| fig3b-total-variability-distribution | reproduced | Range 0.88 to 11.21 mV. 7 neurons have q < 2 (the second reading) and 18 have 4 < q < 12 (cell 18). The strict 1–2 mV bin gives 6. Under the −20 mV spike rule it fails (16 high, max 9.13). |
| total-variability-population | reproduced | 4.58 ± 0.47 against 4.6 ± 0.5 (cell 20). The −20 mV spike rule gives 4.05, outside. |
| lfp-culling-reduction | reproduced | 29 flagged neurons. 4.80 before and 3.19 after, the latter at the edge of 3.0–3.2 (cell 22). |
| fig5b-residual-lfp-psp-correlation | reproduced | 396 tones: 81% positive, 32% with p < 0.05, against 5% expected by chance (cell 24). |
| fig7a-lfp-culling-estimation | partially_reproduced | 2.68 mV and 26/29 neurons reduced both hold, and the mean of per-neuron reductions is 40.2%. The largest reduction is 80.1% against a limit of 78.1%. No single reading meets every part (cell 26). |
| psp-culling-reduction | partially_reproduced | Mean 2.19 holds, but only 30 of 33 neurons are at or below 3.3 mV, where 31–33 are needed (cell 28). Reading 1b (31, 2.09) and reading 3 (32, 2.02) would pass. |
| fig4c-psp-culling-can-increase | partially_reproduced | 32/33 neurons fall (holds). 16 neurons have a tone whose q rises, where at least 16.2 are needed (cell 30). The −20 mV spike rule gives 17, which passes. The 9.2-kHz example (0.47 to 0.57) is not found in any neuron. |
| fig7b-private-best-estimate | reproduced | 1.51 ± 0.21 mV with n = 28, largest reduction 87.8% (cell 32). |
| culling-controls | not_reproduced | The LFP-matched random control gives 3.82 (29 neurons) or 3.80 (33) against 4.5 ± 0.1. PSP-matched gives 3.737 against 3.67, just outside 3 SE. PSP culling removes 24.1% of trials against 29 ± 2.9%. The "both" control (2.988), the second control (2.95) and LFP culling's 37.8% hold (cell 34). |
| fig7d-large-responses | reproduced | 2.92 mV with exactly 19 neurons, LFP bound 1.62, best estimate 1.38 (cell 36). Only 14 neurons have an estimate, against the paper's 16. |
| large-responses-controls | not_reproduced | Random control 2.43 and second control 2.40 ± 0.39, against 3.2 (cell 38). |
| cv-large-responses | partially_reproduced | Total CVs hold (0.371, 0.734). Private CVs miss narrowly: 0.259 against at least 0.26, and 0.385 against at least 0.39. Both t-tests are significant (p = 0.0085, p < 1e-4; cell 40). The criterion's partial rule needs all four values to hold, so its letter leaves this case unclassed. |
| lfp-cv-not-different | reproduced | No difference: p = 0.674 for LFP height, 0.350 for the scale factor (cell 42). The less-variable group's CV (0.57) is outside 0.74 ± 0.09, which the criterion does not score. |
| anesthesia-comparison | partially_reproduced | Totals 3.69 / 6.15 / 4.99 hold, ANOVA p = 0.25 and Kruskal–Wallis p = 0.35. The private difference is significant (t p = 0.014, Mann–Whitney p = 0.004). Pentobarbital-alone private is 0.98, against at least 1.0 (cell 44). |
| fig8-spontaneous-veto | reproduced | Readings (a,b): LFP −0.155, whole cell −0.193, 29/33 negative. Readings (b,b): −0.149, −0.210, 28/33 (cell 46). |
| overfitting-correction-example | reproduced | 0.759 / 0.746 / 0.525 / 0.538 against 0.76 / 0.74 / 0.55 / 0.57, all within 10% (cell 48). |
| private-shared-ranges | partially_reproduced | Only 64% of private values are in 0.9–3.3 mV, where 80% is needed. Shared spans −0.84 to 9.25 mV and its SD (2.71) exceeds the private SD (1.09) (cell 50). |
| quantal-comparison | reproduced | 14 of 33 under both "factor of 2" readings with 0.38 mV (cell 52). |
| mepsp-size | partially_reproduced (notebook says blocked) | The archive holds all six TTX recordings and the documented gain of 4, and the claims file's detector readings were run, so it is testable. The derivative detector at k = 3–4 gives 0.34–0.41 mV, within 0.39 ± 0.08. The CV is out under all six readings (0.43–0.75 against 0.36 ± 0.03), and the template detector gives 0.17 mV (cell 54). |
| recording-properties | reproduced | Repetitions 18.1 ± 1.9 (10–63). Resting potential median −70.0, range −58.4 to −92.0. Input resistance minus access is 19.1–140.6 MΩ, median 65.1 (cell 56). The claims file's plain step reading gives 58–438 MΩ and fails. |
| access-resistance-depth-no-effect | reproduced | Median 60 MΩ. Groups 4.88 (17 above) and 4.27 (16 below) are within tolerance, and all four correlations have p > 0.05 (cell 58). |

### B. Problems

1. **[affects a conclusion] Spike rule (cells 11–12, `ac2.spikes`).**
   - The main reading uses each neuron's `spikethresh`, an assumption the author states, in place of the claims file's detail 6.
   - The "claims file" variant is not that rule. It drops the "fast rise" condition and applies −20 mV to the uncorrected trace, which is about −32 mV after correction, so it removes large subthreshold PSPs (up to 73 trials in a neuron).
   - The notebook says these crossings happen "without a spike" but shows no output for it.
   - Outcomes change with the rule for total-variability, fig3b, lfp-culling (4.25), fig4c (17 passes), fig7a, and the depth correlation (Spearman p = 0.028).
2. **[affects a conclusion] Combining the two cullings (`ac2.analyse_neuron`).** Both cullings are decided on the full ensemble and the surviving trials intersected. The Figure 6/7B legend says "PSP-based culling followed by LFP-based culling", and that sequential reading (LFP mean recomputed over the PSP-culled trials) was not run. It bears on fig7b, fig7d, both control claims, cv, anesthesia, private-shared and the overfitting example.
3. **[affects a conclusion] mepsp-size (cell 54, `minis_*`).**
   - It is labelled blocked although the claims file's readings were run.
   - For 050801md01c the derivative detector barely responds to its threshold (3052 to 2909 events for k = 3 to 5, about 0.1-mV events at 17 Hz). This suggests the robust noise SD has collapsed and the detector is picking up noise.
   - The template detector finds 15–28 Hz of 0.1–0.2-mV events.
   - Amplitude is taken as the peak minus the local baseline on the smoothed trace, which inflates noise events.
   - The mapping of sweep files (`ep_<trial−1>`) is not checked, and 050401md02 uses a single 7.7-s sweep.
4. **[does not affect a conclusion] Overfitting correction (`neuron_summary`).** Per-neuron and per-tone corrections give the same number by algebra (confirmed on synthetic rows: 2.85 and 2.85), so the "correction per tone (7)" variant tests nothing.
5. **[does not affect a conclusion] Mixing readings across claims.** Several outcomes pass only under a reading that other claims reject: psp-culling under 1b or 3, fig4c under −20 mV, fig8 under (a,b). No single reading reproduces everything.
6. **[affects a conclusion; possible claims-file misreading] Random control (`random_control`, culling-controls).** The paper has random culling of 38% of trials leaving q unchanged, while culling 29% lowers it. That pattern suggests the paper's LFP-matched control did not drop tones below 10 trials the way the claims file's "tone criteria are then applied" reads it. The mismatch at 3.82 against 4.5 may come from that reading.
7. **[does not affect a conclusion] fig2 "all neurons" (cell 16).** It takes the argmax over 135 ms, so late components count, and it was not run under reading 1b. Response onsets in cell 7 are 14–38 ms in every neuron. The 50-ms bound is the claims file's own choice.
8. **[does not affect a conclusion] Access resistance (cell 58).** The group ordering is the reverse of the paper's (above-median 4.88 > below 4.27, where the paper has 4.2 < 4.9). Each value is still within its SE.
9. **[does not affect a conclusion] fig8 (cell 46).** The 15-ms PSP baseline lies inside the 100-ms spontaneous window, and spikes in that window are not excluded. Part of the negative correlation is therefore mechanical, and there is no control for it.

### C. What I could not check

Each item names the output that would have let me check it.

- Whether trials crossing −20 mV contain spikes. Needed: for each neuron, the count of such trials with their maximum dV/dt, plus example traces.
- The sequential-culling reading. Needed: fig7b, fig7d and the overfitting values recomputed with LFP culling on the PSP-culled ensemble.
- Why the LFP-matched random control is low. Needed: the number of tones dropped per neuron, and the control run without re-applying the 10-trial criterion.
- mEPSP detection. Needed: the sampling rate of each TTX file, its noise SD and the fraction of zero differences, event-triggered averages and amplitude histograms for each recording, and a check of stimulus-locked events.
- fig7a's 80.1% outlier (030301md03b). Needed: its per-tone q before and after.
- Figure panels. The PDF was not rendered, so I could not compare fig2/fig3a/fig4 shapes and the 9.2-kHz example by eye.
