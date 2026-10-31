I've written and run the entry for DANDI:000576 (Fedele, Tzovara et al. 2020) and built the handover package. All 25 claims have an outcome: 4 reproduced, 3 partially reproduced, 10 not reproduced and 8 blocked. The notebook runs in about 2.7 min from a clean environment; `check` and `all` pass and `handover` built the package. I did not verify my own work, and nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1b-delta-decrease | blocked, methods_underspecified (holds in 10 of 16 readings; the criterion blocks when they disagree) |
| fig1c-hgp-increase-first-2s | not reproduced (no high gamma cluster under any of the 32 readings) |
| other-bands-no-effect | not reproduced (assumed) |
| table2-mi-values | not reproduced |
| fig1d-delta-hgp-mi-correlation | not reproduced |
| nsoz-delta-hgp-mi-inverse | reproduced (assumed), weakly: r = -0.14 |
| table2-delta-reduced-12-of-14 | reproduced (assumed): 11 of 14 |
| table2-hgp-mi-positive-nsoz | not reproduced |
| fig1e-hgp-not-delta-distinguishes-soz | not reproduced |
| hgp-soz-sensitivity-specificity | not reproduced |
| fig1f-hgp-more-specific-than-delta | reproduced (assumed) |
| neuron-count | partially reproduced (42 or 40 units, but 8 amygdalae, not 9) |
| fig3a-firing-increase-aversive | not reproduced (27 of 42 units have positive FRV, mean 0.03 Hz) |
| fig3a-firing-gradual-sustained | not reproduced |
| fig3b-firing-hgp-no-condition-difference | reproduced (assumed) |
| fig3c-ssi-frv-correlation | not reproduced (assumed) |
| fig3d-firing-correlations-modalities | partially reproduced (only the high gamma part can be tested) |
| fig4b-regression-firing-hgp | partially reproduced (assumed): SSI describes it, FRV does not |
| fig3b-firing-muhgp-higher-aversive | blocked, data_missing |
| The six BOLD claims (fig2-participant4, table2-bold-correlations-group, table2-bold-correlation-values, bold-hgp-uncorrelated-low-mi, fig4c, fig4d) | blocked, data_missing |

### 2. Dataset, assumptions and questions

**Version.** I pinned 0.231010.1811, the only published version; the paper predates the dandiset and cites no version.

**What the dataset holds:**
- The 14 bipolar amygdala channels match Table 2, and their SOZ flags agree with it.
- Each session is deposited twice, as `_ecephys` and `_ecephys+image`, with identical data, so I counted each recording once.
- The iEEG is labelled volts but holds microvolts.
- The 26 s epochs are laid end to end with jumps at their boundaries, although the timestamps run without a gap.
- In the trial table, trial 1 includes its 2 s baseline and the other trials do not.
- Unit observation intervals claim all 17 epochs, but subject 7's 16 units have no spikes after 286 s, and 4 units of subject 2 have none in the first epoch.
- The ages of subjects 2 and 8 differ from the paper.
- Four channels are labelled hippocampus or "unknown" though the paper places them in the amygdala.
- No unit is assigned to a microwire.
- The 42 units come from 8 amygdalae of 5 patients. That does not match Table 1, which lists units for patients 5 and 8 and none for 7. Three of the 8 are SOZ amygdalae, against Discussion 3.4.
- The BOLD time courses are not public anywhere I looked: the dandiset, the OpenNeuro copy ds003374 and the data descriptor. The continuous microwire signals are not deposited either.

**Paper inconsistency.** Run on the paper's own printed Table 2 values, the Fig. 1E tests also find the DELTA modulation index differing between SOZ and non-SOZ amygdalae (p = 0.035 and 0.013). The Fig. 1F chi-square on the printed counts gives p = 0.0098, not about 0.2.

**Assumptions:**
- **z-scoring.** Power is z-scored against each trial's 2 s baseline (FieldTrip's baseline z-score). A z-score over the whole trial would void the paper's baseline correction and erase the sustained delta decrease.
- **Modulation index window.** Fixed windows from the Results' text: 0 to 2 s for high gamma, the whole block for delta. The paper's group-cluster window does not exist for high gamma in these data.
- **Firing-HGP correlations (Fig. 3B).** The 1 s time base of Fig. 3A, over each condition's blocks laid end to end.
- **SSI.** Uses every other unit in the same amygdala, because microwire identity is missing.
- **Silent epochs.** Epochs in which a unit has no spike at all are treated as not recorded.

**Questions for the authors** (recorded as three `methods_unavailable` findings):
- How were the power envelopes z-scored?
- Over which window was each modulation index computed?
- What time base and span were used for the Fig. 3B firing-HGP correlations?

**Questions to a reader:** none.

### 3. Where the protocol was unclear
1. Several criteria require a result "under every reading" while one listed reading (per-amygdala clusters) leaves most values at 0 in these data. I showed that reading but judged on the readings the data can carry, and said so in the deviations.
2. For a claim of absence with several open details, the protocol says to judge on "the paper's test alone", which still leaves the open details unresolved. I adopted one reading as an assumption and showed all of them.
3. `measured` has no way to mark an expected value that cannot be tested. I gave the first expected value only and explained the rest in the notes.
4. Neighbouring claims settle the same open detail differently: fig1b's criterion forces a block when readings disagree, while the others allow an assumption. I followed each claim's own criterion, so fig1b is blocked while other claims rest on the baseline-z reading.
5. The prose rule against bold conflicts with the bold headers in the example notebook. I removed all bold except the "**Result:**" openers.

### 4. Runtime and failures
The run took about 37 minutes, from 21:07 to 21:44 UTC. Only two small coding errors occurred, both fixed during development. Device-node files appeared at the repository root (`.bashrc`, `scripts` and others); they come from the sandbox, not from me, and I left them alone.

Files are in `entries/000576-fedele-2020/`:
- `reproduce_fedele_2020.ipynb`
- `amygdala.py`
- `README.md`
- `entry.yaml`

The attempt record is `attempts/000576-fedele-2020-01.yaml`.
