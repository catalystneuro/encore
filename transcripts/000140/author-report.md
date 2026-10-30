I finished steps 1 to 5 and ran the handover (step 6). The entry passes `lock` and `all` with 0 errors, and the notebook runs in 110 s. I did not verify my own work, asked no reader any question, and committed nothing.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig4d-mean-correlation-j-array | not reproduced (mean r −0.079, Spearman −0.020; no reading within tolerance or positive at p < 0.05) |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing |
| fig4-broad-near-zero | partially reproduced (assumed): the interquartile range is 0.17–0.29, below the required 0.3; the other four conditions hold |
| fig4e-correlation-time-course | reproduced (assumed): 0.295 at −200 ms falls to −0.078 at onset |
| suppfig1-population-averages-lose-tuning | reproduced |
| fig6d-perimovement-best-j-array | reproduced (assumed); every space scores below zero under the main reading |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing |
| fig6-perimovement-best-each-dimensionality | not reproduced |
| fig6-maze-endpoint-speed-space-poor | not reproduced (assumed) |
| fig6-dimensionality-trend | not reproduced (assumed) |
| fig6e-summary-rank | blocked: data_missing (a J-array version without EMG is shown) |
| prep-dimensionality-7-to-10 | not reproduced (16 components; shuffled labels also give 16–17) |
| fig7a-shuffled-space-poor | reproduced |
| fig7b-window-start-slide | not reproduced |
| ap-location-no-effect-j-array | reproduced (assumed; r = 0.105, p = 0.668) |
| ap-location-no-effect-other-datasets | blocked: data_missing |
| fig7c-anterior-posterior-performance | not reproduced (assumed) |
| prep-activity-more-anterior | not reproduced (assumed) |
| fig7d-pd-consistency | not reproduced (segment directions beat the peri-movement space) |
| fig8-linear-dynamics-simulation | reproduced |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.220113.0408, the only published version. The paper cites none. The draft holds the same two assets.

**What the dandiset holds.** One J-array session (Jenkins, 2009-09-28): 100 trials over 27 maze conditions. After the paper's delay > 400 ms rule, 78 trials remain, 1 to 4 per condition. It has 142 units. The paper's J-array data had 108 conditions and about 2166 trials per neuron. The condition means here are therefore noisy: the median split-half reliability of preparatory tuning is 0.20. The 100 test segments have no conditions or behaviour, and none duplicates a train trial. The single-electrode data of monkeys A, B and J and all EMG are absent.

**Metadata problems.**
- Every unit's `electrodes` entry points to the PMd group, although the unit ids carry two array prefixes (72 units with 1, 70 with 2).
- All electrode x, y, z and impedance values are NaN, so no unit has an anterior-posterior position.
- 22 of the 100 trials have delays of 400 ms or less, which the paper excludes.
- How the 27 conditions and 100 trials were chosen is not documented.

**Assumptions** (each run under every reading, all shown in the notebook):
- **O1, the measure of "spikes/s of tuning":** the range across conditions. Under the SD reading, which keeps 7 or 8 units, four outcomes change (fig4-broad, fig4e, the endpoint-speed claim and the dimensionality trend).
- **O3, movement onset:** the dataset's `move_onset_time`.
- **O4, the trial filter:** the proto-trial is the trial best correlated with its condition mean. Under the other filter or onset readings, fig6d drops to partially reproduced.
- **Array mapping:** id prefix 1 is PMd and prefix 2 is M1, with array identity standing in for anterior-posterior location.

**Questions for the paper's authors** (recorded as three `methods_unavailable` findings):
- How was preparatory tuning measured for the inclusion rule?
- How was the proto-trial chosen, and how was movement onset detected?
- For the task spaces: where does the reach end, are segments equal in length or duration, is peak velocity signed, how were axes scaled for Figure 7D, and does the upper-limit space include the fitted neuron?

## 3. Where the protocol was unclear or missing something

1. **A criterion can stop making sense.** In fig7c the upper limit is ≤ 0, so normalised performance is undefined. In fig7b both performances are negative, so their ratio means nothing. The protocol has no rule for this. I recorded `not_reproduced` and explained why in the notes.
2. **No partial rule in a criterion.** fig4-broad's criterion only defines "reproduced", but four of its five conditions held. I used `partially_reproduced`.
3. **Many interacting open details.** O1, O2, O3, O4 and the task-space details give up to 96 readings per claim. The protocol does not say whether an adopted assumption must be the same across claims. I kept it the same for all claims.
4. **A dataset too small to resolve the effect.** The protocol has no notion of statistical power, so a claim can be "not reproduced" only because the subset is tiny. I said so in the notes and recorded a `data_missing` finding.
5. **`measured` when one expected value cannot be computed.** For fig7b the monkeys A and B value is not in the dandiset. I gave the single J value.
6. **Metadata assumptions versus method assumptions.** Step 1.6 covers method details. The array-to-region mapping is a metadata question; I treated it the same way, as an assumption with both readings shown.

## 4. Runtime and failures

The work took about 30 minutes (00:05 to 00:32 UTC). The notebook runs in 110 s in the clean environment, and two executed runs gave identical numbers. Nothing failed.

The repository root has untracked dotfiles (`.bashrc`, `.idea`, `scripts`, and similar) that I did not create and left untouched.

Files are in `entries/000140-churchland-2010/`:
- `reproduce_churchland_2010.ipynb`
- `maze_prep.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/000140-churchland-2010-01.yaml`, and the verifier's package is in `executed/000140-churchland-2010/handover/`.
