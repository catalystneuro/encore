All four answers are applied. Both notebooks ran clean from a fresh environment (01 in 23 min, 02 in 20 min) and `check` shows 0 errors. The handover is built in `executed/plitt-2021/handover/` with the conclusions and summary removed. Nothing is committed or pushed.

The earlier author-answers run (22 Oct, recorded as a failure) had already re-run the affected claims and written the notebooks, helper, record and notes. It was cut off during its last full run, so those edits had never run clean together. This run did that full run and checked every printed number behind the conclusions and the record against the output; they all match. Two things changed this time:
- **Runtimes:** I updated them in `entry.yaml` and the README.
- **Lock:** I re-locked the requirements. The uncommitted `tools/entry.py` in your working tree makes `lock` add hashes and a `python: "3.13"` field to entry.yaml, but the committed schema rejects that field, so `check` failed. I removed the field; the runner reads 3.13 from the lock header, the same as before, and the package versions are unchanged. That tool and its schema need to be brought into line.

## Q1. training-intermediate-fraction: use the figshare VR deposit for the priors (M7)?
**Answer:** yes. This claim and fig7 became `data: elsewhere`, using only the deposit. The claims that build posteriors from it became `data: with_inputs`. A link claim, vr-deposit-link, was added. The rare prior's intermediate mass fell from 0.256 to 0.183.

| Claim | Before | Now |
|---|---|---|
| vr-deposit-link (new) | none | reproduced: all 89 files match exactly one deposit file of their own mouse |
| training-intermediate-fraction | blocked (data_missing) | reproduced: pooled, rare 3.49%, frequent 59.83%; per mouse it fails (R4 4.1%, R6 5.7%) |
| fig6a-dkl-sign | partially reproduced | partially reproduced: 43 of 47 sessions, rare −0.660, frequent 0.158, 8 mice |
| fig6bc-pooled-dkl | not reproduced | partially reproduced: rare −0.464 within tolerance, frequent 0.125 outside it |
| fig6d-prior-reconstruction | partially reproduced | not reproduced: the rare mean is now positive, 0.223 |
| map-estimate-values | reproduced | reproduced |
| edf9-early-sessions | reproduced | reproduced: 8 of 11 under both readings |
| edf9k-null-models-rare | reproduced | reproduced |
| edf9l-null-models-frequent | partially reproduced | partially reproduced: 4 of 5 nulls now hold, the uniform prior fails |
| edf10-decision-mice-like-frequent | partially reproduced | reproduced: pooled Delta D_KL 0.042 and 0.125 |

## Q2. fig7-model-reproduces-remapping: which scale, input range, Gaussian form and noise?
**Answer:** the code's scale. The width sigma is 0.15 units (4.11 f_h), centres run from −0.1 to 1.1 units, and stimulus, output and weight noise are used in both training and testing. Test stimuli are S from −0.3 to 1.3. The network now learns: mean weight 2.25 (rare-trained) and 2.77 (frequent-trained), where the weights used to decay to about 0.

| Claim | Before | Now |
|---|---|---|
| fig7-model-reproduces-remapping | not reproduced | reproduced: median Delta D_KL rare −0.564, frequent 0.093 |
| fig7g-model-prior-reconstruction | not reproduced | reproduced: −0.098 and 0.626 bits |

The notes record one oddity: the criterion says the test stimuli lie within 5.5 to 38.5 f_h, but computed as it prescribes they span 0.04 to 38.45.

## Q3. edf4bc-overlap-cells-at-ends-and-reward: how are a cell's two peaks counted?
**Answer:** the paper does not say. The criterion now names two readings: (i) each environment's peaks separately, and (ii) cells with both peaks in the regions, against the product of the references. Reference (b) is now taken per environment, and every combination must hold.

| Claim | Before | Now |
|---|---|---|
| edf4bc-overlap-cells-at-ends-and-reward | not reproduced | not reproduced |

44 of the 48 combinations hold. All four failures are reading (i) against reference (b), with the end points as the first and last bin. The counts (5,997 and 2,552) are outside tolerance.

## Q4. edf3-simulated-posterior-population: what range do the centres tile, and is the result the mean over simulations?
**Answer:** the centres tile the M6 grid, as the earlier run already had them. The result is the mean over 1,000 simulations, with each simulation's matrix z-scored before averaging.

| Claim | Before | Now |
|---|---|---|
| edf3-simulated-posterior-population | not reproduced | not reproduced |

At S-tilde 1.0 the sign matches under reading (a), −0.036, but not under reading (b), +0.030, and the criterion requires both.

All other claims keep their earlier outcomes, and their numbers in this run match the record.
