A. Outcomes for the 16 claims in `doi-10.1038-nn.2134.yaml`. The paper's full text could not be fetched: PMC returned a reCAPTCHA page, the publisher does not allow PMC XML download, and the BioC API answered "Too Many Requests". I read only the abstract (`paper/abstract.txt`) plus the Methods as the claims file quotes them. No attempt record was among my materials, so the counts come from the claims file alone.

| Claim | Outcome | Reason |
|---|---|---|
| channel-region-link | partially_reproduced | Cell 16: with the CRCNS channel numbers the sensor check fails in GG (agreement 0.35–0.42). With the per-rat correction found in the data (GG sensors on 65/66, CA1 on 70–101), the theta and sensor checks hold in every session (theta 0.37–0.54 vs 0.16–0.27; agreement 0.97–1.00). |
| rats-and-units | not_reproduced | Cell 18: the dandiset has 3 rats, not 4. The readings 417, 346 and 491 units are all outside 570–696. EE.152/165/188 are not in the archive (I confirmed this from the asset list) and EE.088's 350 units are not placed on a probe. |
| task-performance | blocked (data_missing) | The trial tables hold correct trials only (cell 6), so the exact percentage cannot be computed. A partial test was possible and was not tried (see B9). |
| fig2c-active-fraction | not_reproduced | Cell 21: per-rat medians are EE 10.2%, FF 19.7% and GG 6.2%, so GG matches neither layer. GG.149's max/min over position bins is 2.57, above the threshold of 2. Neither part of the criterion holds. |
| fig2-field-size | partially_reproduced | Cell 23, reading a: mean 0.270 is within tolerance, s.d. 0.196 is outside 0.153–0.187. Readings b and c also fail on the s.d. The mean's tolerance (±0.17) is so wide that passing it says little. |
| fig2b-trajectory-selective | partially_reproduced | Cell 25: no rat is in the central range of 14.4–19.8% (EE 22.9, FF 24.5, GG 26.2). Side-arm values (52–60%) match neither layer. Pooled central 24.0% vs chance 0.9%, Fisher p = 7e-24. The paper states no chance level; 0.9% is plausible for a global band at 0.05 tested over 30% of the track. |
| traj-diverge | blocked (data_missing) | There is no y coordinate. However, the notebook never shows that the x coordinate (x1) cannot separate the two sides (B8), so the block is unverified. |
| odor-nosepoke | partially_reproduced | Cell 28: the Mann-Whitney test gives 37.8%, outside 20–30%. Chance is 4.0%, which matches the 5% implied by the paper's per-cell P < 0.05; Fisher p = 6e-35. The t-test variant (28.5%) would fall within tolerance, but the criterion fixes Mann-Whitney. |
| fig3-connection-rates | partially_reproduced (fragile) | Cell 30: total 1.131% and excitatory 0.898% are outside tolerance; inhibitory 0.233% is within. The inhibitory match is unreliable because the classifier creates spurious inhibitory links in the reverse direction of excitatory ones (B1). |
| fig3-cell-classes | not_reproduced | Cell 32: pyramidal 37.9%, interneurons 3.1%, ratios 11.9 / 12.2 / 13.0, targets 7.3% (20.2% with any inhibitory output). All four values are outside tolerance under every reading. |
| fig3f-distance | not_reproduced | Cell 34: the Fisher test holds (4.60% vs 0.52%, p = 1e-89) and connections reach 1400 µm. The Spearman test fails (rho −0.62, p = 0.10). This hinges on one bin: 1400 µm, 2 connections in 310 pairs. Over 0–1200 µm rho is −0.96, p = 0.0005. |
| fig4-position-dependence | not_reproduced | Cell 36: 3.5% (reading a) and 2.1% (reading b) against 19.5 ± 1.95%. The rank-band variants give 1.4–1.8%. The median is only 7 coincidences per pair during runs, so the test has little power. |
| fig6-facilitation-depression | not_reproduced | Cell 38: depressing 4.9%, facilitating 15.5%; both are outside tolerance. Depressing is not above the 5% null (binomial p = 0.56). |
| fig7-supralinear | not_reproduced (uninformative) | Cell 40: 15 of 40 satellites (38%) are supralinear, Wilcoxon p = 0.993. The measure itself is biased toward sublinear (B2), so this result is not evidence against the claim. |
| fig3-trajectory-by-class | not_reproduced | Cell 42: only FF matches a layer (66.7/62.5 → layer 2/3). EE (58.5/60.0) matches neither. GG has 0 putative interneurons and 14.3% of its 7 pyramidal cells are specific, so the partial condition "every rat both fractions above chance" cannot hold. |
| ee188-example-session | blocked (data_missing) | The asset list for 0.250624.0419 (28 assets) has no EE.188, EE.152 or EE.165 file. No part can be tested. |

B. Problems

1. [affects a conclusion] `pfc.directed` / `_direction_result`: a strong excitatory peak at +1 to +4 ms gets spread into negative lags by the ±5 ms jitter of both trains. The reverse direction then shows an observed "trough" below the lower global band. `directed` only excludes inhibition when there is a peak in the same direction. On synthetic pairs (5–20 Hz, transmission 0.05), 26–30 of 30 detected excitatory connections also got a spurious inhibitory connection in the reverse direction.
   - This contaminates the inhibitory rate (fig3-connection-rates), the interneuron, "both" and target classes (fig3-cell-classes: 54 of 74 inhibitory links come from "both" units), fig3-trajectory-by-class, and the reciprocal count (40).
   - The criterion's wording permits it, but the classes are not interpretable.

2. [affects a conclusion] `pfc.coincidence_gain`: the response is counted 1–4 ms after the event's last spike, so the effect of the first partner is missed when the two spikes are more than about 3 ms apart. Under exact linear summation in a synthetic test, excess₂ − 2·excess₁ = −0.034 (excess₂/excess₁ = 1.29). The observed ratio (0.0197/0.0145 = 1.36) is therefore close to what linear summation gives under this measure. The fig7 test cannot detect supralinearity as built.

3. [affects a conclusion] `pfc.coincidence_test` (cell 36): the null jitters both trains and keeps the events' positions. It is a one-sided test for excess coincidences somewhere on the track, so a pair with constant efficacy is also flagged. It tests for any excess, not for position dependence beyond rates. The low rate here comes mainly from power: median 7 coincidences, and 21.4% of the pairs with at least 50 coincidences are significant. Neither problem rescues the claim, but a valid test is missing.

4. [affects a conclusion] Cell 34 (fig3f): the outcome depends on a Spearman test over 8 distance bins, with the 1400 µm bin holding 2 connections in 310 pairs. In addition, the distance is 200 µm × |channel//8 difference|, which assumes channel order equals spatial shank order. That is consistent with the file's 8-channel groups but never checked against the data.

5. [does not affect a conclusion] Cell 35's markdown says the rank band "is empty and nothing can be significant", but the rank variants in cell 36 find 4 and 5 pairs.

6. [does not affect a conclusion] `pfc.field_size` returns 1.0 for an all-zero map. Reading b includes a silent side for units whose peak of at least 1 Hz is on the other side, which inflates b. The s.d. fails under every reading anyway.

7. [does not affect a conclusion] `pfc.positions_at` maps spike time to frame as round(t·rate), assuming the linearized series starts at t = 0; `starting_time` is never read. Cell 5 supports the alignment indirectly (first d ≈ 1.02 after run start, d > 0 in at most 0.5% of frames outside trials).

8. [affects a conclusion: traj-diverge] Cells 6 and 26 assert that the side arms differ only along y. The x1 range is about 600 px and is never compared between Left and Right trials, so the block is an unchecked assumption.

9. [affects a conclusion: task-performance] Cell 19 says error trials cannot be recovered. The nose-poke sensors are recorded continuously and match the trial side in 97–100% of trials (cell 9). Counting poke bouts with no table entry would bound the error rate, but this was not tried.

10. [does not affect a conclusion] Cells 25 and 28: the Fisher tests of real against chance treat paired measurements on the same units as independent samples; McNemar is the right test. With p ≤ 1e-23 the outcome does not change.

11. [does not affect a conclusion] `pfc.decode_side`: the z-scoring uses the held-out trial. The leakage is negligible and this is a data check, not a claim.

12. [does not affect a conclusion] The multi-unit split uses only the 2% ISI rule. 35 first-of-block units are kept as single units and there is no isolation-distance criterion, so the unit counts are slightly inflated. They are still below the paper's 633.

Synthetic checks that passed: `jitter_expectation` matches Monte Carlo; `connections` gave 0 false positives in 120 null ordered pairs and detects a +2 ms drive with width 2; `transmission` is unbiased under the null (−0.0003 ± 0.0014).

C. What I could not check, and the output that would have settled it

- The paper's Methods and supplement themselves: whether the published jitter test excludes reverse-direction troughs, the position-dependence null, and the definitions behind Fig. 6 and Fig. 7. This needs the full text, which was blocked.
- How many of the 74 inhibitory connections are the reverse of an excitatory one. Output needed: that count, plus the inhibitory rate and cell classes recomputed with those excluded.
- Whether x1 separates the sides. Output needed: mean x1 for Left and Right trials against normalized position, per session.
- Task performance. Output needed: per session, the number of nose-poke bouts in the sensor channels and how many of them have a trial-table entry.
- Calibration of the fig4 test. Output needed: the fraction flagged for synthetic pairs with constant efficacy, and the same fraction restricted to pairs with at least 50 coincidences.
- A fair fig7 test. Output needed: the two-partner excess compared with a linear prediction built from one-partner events at the same separation, with the response window set from the first spike.
- Linearized-position alignment. Output needed: the `starting_time` of the LinearizedTimeSeries.
- EE.088's PFC units for rats-and-units. Output needed: a shank assignment of its units from the conversion's block order, and the total count with it included.
