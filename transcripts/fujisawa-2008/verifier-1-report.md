**Verification report: Fujisawa et al. 2008, round 1**

Claim and outcome counts come from the claims file (33 claims) and from my own judgement of the notebook outputs. My outcomes: 5 reproduced, 11 partially reproduced, 16 not reproduced, 1 blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| channel-region-link | not_reproduced | Check (i) holds in the 12 sessions with raw signal; EE088 has none. Check (ii) fails in GG069, GG097 and GG149 (0.30, 0.42, 0.42), and even the best channels found by search reach only 0.68–0.78, below 90% (cell 6). |
| rats-and-units | partially_reproduced | The total is 627, within 633 ± 63.3. No rat has 222 ± 22.2 units (FF 146, EE 446, GG 35; cell 8). This rests on an unverified unit list (B1). |
| task-performance | blocked (data_missing) | SessionNP is documented as "Only correct trials are listed", and the NWB trials tables are identical (cells 3, 10). The criterion says to block in this case. |
| fig2-population-uniform | not_reproduced | In EE188, peaks per tenth are [24,0,1,2,14,5,3,8,1,59] against 11.7 expected. The population rate test passes (cell 39). Peaks were computed with the P-b rate only (B2). |
| fig2c-active-fraction | not_reproduced | No reading has both values in tolerance. Reading (a): EE188 11.8% (needs 10 ± 1). Reading (b), R-a: layer 2/3 12.6%, layer 5 20.3% (cell 41). |
| fig2-field-size | reproduced | 5 of 24 combinations have both mean and s.d. in tolerance, e.g. P-a (b)(i)(x) 0.241 ± 0.169 and P-b (a)(ii)(y) 0.286 ± 0.185 (cell 43). |
| population-vector-width | partially_reproduced | The claim's own method (raw PSTHs) gives about 1.0. Values fall in tolerance only after the author's z-scoring, which neither the paper nor the claims specify: EE188 0.19–0.22. With peak normalisation (as Figure 2a displays rates), layer 2/3 just misses: 0.268 against a limit of 0.267. The layer 5 value comes only from a stand-in session or the rat readings (cell 45). |
| fig2d-layer-rates | partially_reproduced | Under R-a, trial periods: pyramidal cells L5 > L2/3 at p = 0.0028. All neurons only reach p = 0.026 (Welch). No combination gets both below 0.01 (cell 47). |
| fig2e-layer-discrimination | not_reproduced | At most one group (pyramidal, R-a, p = 0.023) is higher at p < 0.05. The partial criterion needs two (cell 49). |
| traj-diverge | partially_reproduced | EE188 path diverges at 0.30 (in tolerance). Head direction diverges at 0.02 against 0.24 (cell 51); see B8. |
| side-arm-selectivity-by-layer | partially_reproduced | Values are far from tolerance (about 50–60% against 40% and 22%). Under R-a, L5 > L2/3 by one-sided Fisher test, p = 0.046 (reading a) and p = 0.017 (reading b) (cell 14). |
| central-arm-selectivity | partially_reproduced | Values are 23–31% against 16% and 18%. The pooled 30.1% is far above one random relabelling (1.4%, p = 6e-52) (cell 16). |
| odor-nosepoke | not_reproduced | 39–45% in EE188 and 31–33% over all neurons, against 26 ± 2.6 (cell 53). |
| odor-unrelated-to-stem | not_reproduced | Fisher tests are not significant, but the correlation with the stem is r = −0.38 (p = 2e-5) and with the side arms p = 0.03 in EE188 (cell 55). |
| retrospective-coding-rare | reproduced | Previous-trial labels give 4–13% of neurons against 51–80% for current labels, in every reading (cell 57). |
| speed-not-correlated | reproduced | Median r = −0.022, so not above 0 (cell 59). |
| fig3-connection-rates | not_reproduced | None of the three directed percentages is in tolerance in any of the 4 combinations (e.g. 1.45 / 1.17 / 0.28%) (cell 21). |
| fig3-cell-classes | not_reproduced | Interneurons are 2.6–4.4% against 12.5%, and the pyramidal-to-interneuron ratio is 9.9–14.8 against 2.82 (cell 23). |
| pyr-pyr-connections | partially_reproduced | No value is in tolerance. L5 > L2/3 under R-a, reading (a): 0.355% against 0.261% (cell 25). |
| nearby-pyr-int-probability | not_reproduced | 45–59% against 0.9–2.2% (cell 27). |
| fig3b-session-connections | not_reproduced | EE188 gives 119/22 directed connections and 67/16 distinct reference cells, against 48/30. The layer 5 session was not identified, which rests on B1 (cell 29). |
| fig3d-hub | not_reproduced | EE188's largest component is 65–86 cells, against 39. The lab's own `pairs_all` list gives exactly 39 (cell 31), so detection here is much more liberal than the lab's. |
| fig3f-distance | partially_reproduced | Same shank 384 against 200 on other shanks, and the confidence intervals separate. But the largest separation with a connection is 1400 µm, not 1200 µm (cell 33). |
| fig3-trajectory-by-class | partially_reproduced | Under R-a, reading (b), 2 of 4 values are in tolerance: layer 2/3 pyramidal 66.8% and layer 2/3 interneurons 52.6% (cell 35). |
| no-spatial-clustering | reproduced (layer 2/3 session only) | EE188: shank × class p = 0.27, shank × peak tenth p = 0.23. The layer 5 session was not tested (cell 37). |
| fig4-position-dependence | partially_reproduced | 6.4–7.2% against 19.5%, but well above the 1–2% null rate (binomial p ≤ 5e-8) (cell 63). |
| fig5a-session-selective-connections | not_reproduced | 8–9 of 119 connections found here, and 6–7 of the lab's 43 (cell 65). |
| fig4-pair-156-136 | not_reproduced | The region starts at 0.34 (needs 0.4 ± 0.04), and cell 136 varies by 61% between 0.2 and 0.5, so it is not steady (cell 67). |
| fig5b-example-pairs | not_reproduced | Only 197-201 holds. 49-52 has no region on left trials, and 186-201's region starts at 0.73, not beyond 0.75 (cell 69). |
| thinning-preserves-dependence | reproduced | Under region reading (a), 7 of 34 pairs keep their dependence in most repetitions (cell 71). |
| fig6-facilitation-depression | not_reproduced | No combination has both fractions above 5% at p < 0.05 (cell 73). The depression/facilitation split is flawed (B3). |
| fig6b-convergent-examples | partially_reproduced | By the literal criterion: 197 has first > later, but p ≥ 0.26. 186 has later > first with p = 0.064 or 0.034 (cell 75). The sign for 197 carries no information (B3). |
| fig7-supralinear | not_reproduced | S-b gives 14 satellites, but the excess over linear at 5 ms is negative in every reading (cell 77). |

### B. Problems

1. **[affects a conclusion]** `Session` and cells 2, 8, 29: the unit list is `CellsInfo` from the `Behavior_PFC` files, which the CRCNS description does not document.
   - For EE188 this list has 105 cells, while the paper's session has 117, so these lists are subsets. They may be the 1 Hz "Cells" list, which the claims file treats only as a variant.
   - The notebook never compares the list with `spikeph` or the NWB units tables.
   - The NWB variant promised in cell 7 was never computed: `nwb_by_rat` is defined and never used.
   - Affected claims: rats-and-units (FF could hold about 222 units); "no session of 142 cells", and with it fig3b, fig3d-hub and every layer 5 stand-in; fig2c (leaving out low-rate units inflates the active fraction); every fraction by layer.
2. **[affects a conclusion]** `peak_tenth` (cells 37, 39): peak positions use only the P-b PSTH. The claims header asks for both P-a and P-b wherever peaks matter. P-b peaks pile up at 0 and 1, where the rat lingers. This decides fig2-population-uniform and test (ii) of no-spatial-clustering.
3. **[affects a conclusion]** `standardized_height_test` and cell 73 label a pair depressing or facilitating by the sign of z_first − z_later.
   - Standardized height grows with √n, and first spikes far outnumber later ones (e.g. 2311 against 252).
   - On synthetic data with no true effect, the difference was positive in 40 of 40 pairs, so every significant pair would be called "depressing".
   - The Figure 6c legend assigns the label by which tail of the permutation distribution the result falls in.
   - Reassigning the 69 significant pairs of the (a,y) reading could put both fractions above 5% and turn fig6 into partially reproduced.
   - The claims file's literal "first-spike height above later" for fig6 and fig6b repeats this reading of the paper (reported, not corrected).
4. **[affects a conclusion]** `standardized_height_test`: for fig6 it jitters only the presynaptic spikes, with 200 jitters (the Supplementary Figure 9A variant). The claims file says to use the shared method: both cells, 1,000 jitters. Several binomial p-values sit near 0.05 (e.g. 0.044, 0.054), so this could matter.
5. **[affects a conclusion]** Cell 45: the outcome of population-vector-width depends on the author's normalisation (z-score or peak), which neither the paper nor the claims specify. The assumption is stated, but it decides the outcome.
6. **[affects a conclusion]** `head_curves` (cell 51): head direction is the angle from LED 1 to LED 2, averaged linearly after wrapping. LED order and orientation are never checked, and the 0.02 onset is never inspected. A wrap artefact or an LED axis perpendicular to the heading would change the head-direction result. Only 3 sessions have two LEDs.
7. **[does not affect a conclusion]** `classify_ccg`: with a strong excitatory peak, the jittered surrogates inflate the baseline, so the real baseline breaks the global minimum band. In my synthetic test with 5% transmission, spurious troughs appeared in 33% of cases in the same direction and 62% in the reverse direction. The notebook never inspects its 39 units classed as both, its 80 reciprocal pairs, or the inhibitory counts. Those claims fail by wide margins anyway.
8. **[does not affect a conclusion]** Cell 18: the one-cell jitter variant (Supplementary Figure 9A) named in the claims header was not run. It is the obvious candidate for why 141 EE188 connections are found here against the lab's 43.
9. **[does not affect a conclusion]** Cell 27: `dirs = {…: k}` overwrites an E connection with an I one in the same direction, so E connections are undercounted. The values (45%) are far from 2% anyway.
10. **[does not affect a conclusion]** Cell 6: the NWB files for FF label 8 channels from 97 on, while CRCNS gives FF 101 channels; GG's are labelled "neural". Neither is remarked on.
11. **[does not affect a conclusion]** Cell 4: the clock check is weak for EE049 (0.58 against 0.53 chance) and GG097 (0.55 true against 0.61 shifted).

Checks that passed:
- `bands_from_curves` / `perm_bands`: on synthetic null curves the familywise error was at or below α. This matches the notebook's 4.8% null rate and the paper's α = 0.05. Very conservative with M = 1,000 at α = 0.01, as the notebook notes.
- `jitter_pair`: detects injected 2 ms connections and gives no false positives on independent Poisson trains.

### C. Not checked, and what output would have allowed it

- **Unit lists:** per-session counts of NWB units and `spikeph` entries, their overlap with `CellsInfo`, and the `Behavior_PFC` variable names (is there a `Cells` list?). This would also show whether any session has 142 units.
- **task-performance (blocked):**
  - The DANDI asset list (31 NWB files) has no other behavioural files.
  - Archive contents can't be inspected through metadata alone.
  - The notebook printed only the number of unique whl trial numbers, not their range or gaps; gaps would reveal error trials.
  - Poke bouts on sensor channels 97/98 plus the LED path could count error trials in the EE and FF sessions (not GG, not EE088). The criterion as written still blocks the claim.
- **Positions:** d at each trial's start and stop, to confirm that positions run from 0 to 1 within each trial window.
- **Trial tables:** what the 18–67% of whl frames with d > 0 outside trials are.
- **P-a peaks:** peak-tenth counts under P-a.
- **Head direction:** mean head angle against position for left and right trials.
- **fig6 tails:** the null mean of the first-minus-later difference for each pair, so tails can be reassigned.
- **CCGs:** the CCGs of units classed as both and of the reciprocal pairs.
- **Global bands:** the distribution of `kstar` (pointwise-equivalent level) for the left-right tests, to compare with the paper's example of global 5% ≈ pointwise 0.6%.
