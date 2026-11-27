**Verifier report, round 2: hiraoka-2025-01 (doi:10.1063/5.0296506, DANDI:000044 0.210812.1516)**

**1. Outcomes**

The claims file has 14 claims and the attempt record has 14 outcomes: 12 tested, 2 blocked. Cell indices below are main = `reproduce_hiraoka_2025.ipynb`, on = `other_neurons.ipynb`, cap3 = `other_neurons_cap3.ipynb`, model = `model.ipynb`.

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| fig2-neuron-representative-sequence | reproduced | yes | main 9 |
| fig2-iet-broad | reproduced | yes | main 12 |
| fig2-neuron-burst-size-heavy-tail | reproduced | yes | 8/8 and 40/40 under both KS fits, capped or not (main 18) |
| fig2-neuron-beta-stable | not_reproduced | yes | Range 1.079; capped KS ranges 0.552–0.705 (main 21) |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | yes | Part (2) rests on 6 points at p = 0.0416 (main 33), and the record says so |
| fig2-neuron-merging-heavy-tail | reproduced | yes, now | My round-1 objection is answered. Without the cap, ks_discrete IQR is 0.378 and 0.415, with 13/15 and 70/76 supported (main 24). |
| fig2-neuron-merging-collapse | not_reproduced, `assumed: true` | yes, with a caveat | The assumption (unbounded exponent) is stated and is methodologically reasonable. The result is knife-edge: 0.538 unbounded against 0.490 capped, band 0.5 (main 27). O3(a) says "the powerlaw package's default", and the locked 2.0.0 default is the capped fit, so a literal O3 reading would give reproduced. The outcome is best read as undetermined between the two. |
| fig2-exponents-above-two | reproduced | yes | main 30 |
| fig2-other-neurons-similar | reproduced | yes, under the one-reading rule; fragile | Passes only under x1_continuous (0.883–0.906, on 5). That reading also passes for inhibitory (0.781–0.836) and all units (0.872–0.893), so the pass does not depend on the pyramidal restriction or on the cap (cap3 5). |
| fig2-wikipedia-beta | blocked (too_large) | blocked, yes | The record answers my data_missing objection with a protocol rule I cannot see, and the disagreement is recorded. |
| fig2-earthquake-beta | blocked (other) | yes | The pinning rationale is stated and the disagreement is recorded. |
| fig4-model-heavy-tails | partially_reproduced, `assumed: true` | yes | The assumption (one fit reading applied to all three series) is stated and reasonable (model 4). The criterion defines no partial outcome, while the author's response on beta-stable changed that outcome for exactly that reason. By that logic this claim would be not_reproduced under the adopted reading. The record should say why "partially" is used here. |
| fig4-model-iet-shapes | partially_reproduced | yes | 1 of 3 values within tolerance (model 8). The same caveat about an undefined partial outcome applies. |
| model-decremental-equivalent | not_reproduced | yes | Under L every test rejects, and the calibrated variant also rejects in 3/3 series at p = 0.0079 (model 11, 14). |

**2. Sentences the printed numbers do not support**

- **Attempt record, finding 6 (about: paper):** "0.68 to 0.74 of 128 against 0.08 to 0.45 of 562". Over the 562 pyramidal units the KS fits give 0.233–0.454 (on 5, set (b)). The 0.083 is set (a), Achilles-10252013 alone, which has 120 units.
- **Attempt record, second methods_unavailable finding:** "The Figure 2 labels fit 41 log-spaced points over the relevant range, which this attempt used". Grid (b) as run has 40 points, 55.2 to 5581.5 ms (main 15).
- **main 38 (Summary):** "Figure 2 shows 6300 ms, which has 99 bursts by this count". No output prints the burst count at 6300 ms. main 15 only implies at most 99 bursts above 6282.75 ms.
- **main 38 (Summary table):** "KS fits 0.083 to 0.454". This mixes set (a) and set (b) without saying so. It is not wrong, but it is the source of the error in finding 6.
- **README:** "about 45 minutes on 4 processes" for `other_neurons.ipynb`. It printed 49.8 min of fitting and 50.1 min in total (on 5, 8). This is minor.

Every other "**Result:**" sentence (main 10, 13, 19, 22, 25, 28, 31, 34, 37; on 6, 9; cap3 6; model 5, 9, 12, 15) and every other note in the record matches the printed values.

The record's round-1 reasons are my own, faithfully condensed, and the `agrees` flags are correct.

**3. Round-1 points**

Resolved:
- **1 (cap):** the version is printed (powerlaw 2.0.0, main 1), and unbounded fits are run with capped fits beside them.
- **2 (interneurons):** all 690 units are fitted, and the inhibitory units and all units are run as variants (on 5).
- **3 (one-reading rule):** resolved for fig4, which now uses one reading for all series. For other-neurons the pass is now openly called fragile.
- **4 (KS calibration):** a calibrated permutation variant was added (model 14).
- **5 (Eq. 16 inconsistency):** recorded as a paper inconsistency.
- **6 (590/6490 ms pair):** now noted.
- **7–10:** recorded.

What remains and bears on a conclusion:
- **(a) fig2-neuron-merging-collapse:** the outcome turns on whether the paper's fits were capped at 3, which is unknowable from the paper. This is correctly marked assumed, and the question is put to the authors.
- **(b) fig2-other-neurons-similar:** this rests solely on x1_continuous, a poor fit for integer data whose median β is about 1.75 against the paper's 2.35.
- **(c) Claims-file misreadings, reported not corrected:**
  - The claims file restricts fig2-other-neurons-similar to pyramidal units, but the paper's own representative unit is labelled inhibitory.
  - The model-decremental-equivalent KS criterion rejects two runs of the same algorithm (N: 4 and 11 rejections, model 11), so it cannot test equivalence. That outcome stands only because L also fails the calibrated test.
- **(d) Not resolved:** which circles are filled in Figures 2 and 4 (no PDF), and the earthquake n (the author declined, citing the pinning rule).

**4. Critical findings**

No finding in the attempt record is rated `critical`.

On finding 1 (format_error, rated `major`): main 3 and on 3 show it as stated. Three unit-id-2 trains are two sorted runs, broken after index 65 535 (131 071 in Gatsby-08022013). Rating it `critical` would be wrong, because the fault shows in the values: negative IETs, min_iet −2×10⁷ ms in main 3. For the same reason I would rate it `minor`. Excluding the units changes no fraction by more than 0.003 (on 5). `major` is defensible only on the grounds that whether each train holds one unit's spikes cannot be checked.
