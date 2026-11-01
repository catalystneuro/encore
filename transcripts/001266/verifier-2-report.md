**Verifier report, round 2: Park, Wong-Campos et al. 2025 on DANDI:001266 (0.250710.0758)**

The claims file has 55 claims. The attempt record has 55 outcomes: 8 reproduced, 14 not_reproduced, 33 blocked (29 data_missing, 4 methods_underspecified). One outcome is `assumed: true` (fig3d). Cells are cited as [n] for `reproduce_park_2025.ipynb` and [S n] for `simulations_park_2025.ipynb`.

### 1. Outcomes

I agree with 54 of the 55 outcomes. I disagree with one: **fig3d-distal-first-bap**.

**fig3d-distal-first-bap (reproduced, `assumed: true`): disagree.**
- The assumption (a 4 s.d. somatic threshold) is stated.
- It is not reasonable for this file. The criterion asks for the count "under the reading whose total counts match the legend". File D4 has exactly the legend's 84 bAPs at 5 s.d., and 85 to 88 at 4 s.d. [13]. So the criterion points to 5 s.d.
- At 5 s.d. the median filter gives 32 (inside 31.5–38.5) and the Butterworth filter gives 31 (outside) [41]. The readings disagree, so the claim should be blocked (methods_underspecified).
- The 4 s.d. justification comes from the two burst files, and even there 4 s.d. does not reach the legend's totals (161–165 against 167, and 167 against 170).
- The response says "The verifier itself finds the 4 s.d. variant right (B2)". My B2 said running k=4 *as a variant* was right, not adopting it.

**Agreements that carry a caveat:**
- **fig2e-f, fig3f:** not_reproduced holds under the claims file's region (beyond 300 µm). fig3f passes when the region is cut at 400 µm (51 and 49), and [19] shows the traced line leaves the trunk beyond about 400 µm.
- **fig3-subthreshold:** the outcome holds at both 4 and 5 s.d., because the D4+soma events remain. Whether those events are noise is unresolved, as the record says.
- **fig4d:** not_reproduced, but it rests on a dSpike rule and a somatic detection that are not validated (see section 3).
- **figs15-stochastic:**
  - The claims file may misread the paper. Its criterion requires somatic spike times "within 2 ms of each other across trials". The Fig. S15 legend (supp1) says only "The spike train in the soma was regular, but the pattern of bAP propagation showed trial-to-trial variability". That more naturally means regular within a train, which was not tested.
  - The 14–85 ms spreads also coincide with unstable somatic counts (71 to 132 bAPs across readings [52]), so misaligned spike positions may produce them.
- **figs17e (blocked, methods_underspecified):** reasonable. Two omissions:
  - Under the median filter the count is undefined, not opposite. "Disagree" overstates it.
  - Under its own threshold, the 100 nM file has 4 dSpikes in the Butterworth k=4 >300 µm reading [63]. The result leaves this out.
- **fig1 (blocked, methods_underspecified):** acceptable under the claims header's rule. The only reading that passes is raw counts, which [50] itself says measures resting brightness.
- **figs18g, fig5d-single, figs23, figs2:** agree. figs2's noise-equivalent voltage was still computed without the maximum-likelihood pixel weighting, which the Methods describe and which would lower the noise.
- **figs21:** agree. The criterion itself names the Methods' parameters, and the Methods give u_D = −13.

### 2. Sentences the outputs do not support

**[15]**
- "161 to 167 and 165 to 170 bAPs with the 4 s.d. variant": at 4 s.d. the D4+soma file has 167 in both readings [13].
- "the totals of the legend (167, 170) are met only at 4": they are not met at 4 (soma 161–165, D4+soma 167).

**[44]**
- "the 4 s.d. threshold (which gives the legend's bAP total, 161 to 165 against 167)": the sentence contradicts itself.

**[47]**
- "The early dSpikes are mostly … second-bAP dSpikes in the D4+soma file": the D4+soma dSpikes are mostly on the third bAP. At 4 s.d. the counts are 2 on the second bAP against 46–51 on the third; at 5 s.d. they are 14 against 30–35 [41].
- "only 45 to 48%": the output shows 44% (Butterworth, k=4, 300–400 µm) [46]. Minor.

**[58]**
- "the best epoch matches the target sequence at 8 of 12 positions": the Butterworth k=5 readings give 7/12 [57]. Minor.

**[67], repeated in the record's figs18g notes**
- "the Ni2+ file has no trough in 6 of 8 readings": [52] shows no trough in 7 of 8; only Butterworth k=5 >300 µm has one.
- "defined only in 2 Butterworth readings (… 4 s.d. between 300 and 400 µm), where it holds (0, 2.0 to 3.75, 0)": in [66] the Ni²⁺ file is NaN at Butterworth k=4 300–400 µm. The comparison is defined in one reading only, with Ba²⁺ means of 2.0 and 2.5, not up to 3.75.

**[81]**
- "The 20 ms smoothing removes most of the noise-driven early returns": beyond 200 µm it creates new 0 ms returns (215424 goes from 2.1 to 0.0 ms, 204403 from 3.1 to 0.0 ms) [80]. Minor.

**[52], printed note**
- "Where trough_found is False the distal amplitudes have one density mode": the `kde_modes` column in the same table shows 2 modes with no trough (152954 median k=4 300–400 µm; 154649 median k=4 >300 µm, Butterworth k=4 both regions). It shows 1 mode with a trough found (174900 rows 9 and 12; 152954 row 58). See section 3, B1.

**[S15] and the record's figs20 notes and response**
- "about 34 min on 4 processes": [S13] prints 22 s plus 22.3 min, and the whole notebook ran in 23.9 min [S20].

**README**
- "in about 37 minutes" (simulations notebook): [S20] prints 23.9 min.
- "Spike and dSpike thresholds follow the claims file's rules": the 4 s.d. somatic threshold departs from the claims file's 5 s.d.

**Summary [92]**
- "4 s.d. gives the legend's totals": it does not (see [15]).
- "All results except the Fig. S2 ones rest on one neuron or one example recording per claim": fig5b uses 10 cells and figs23 uses 9.

**Attempt record notes**
- **fig2e-f:** "Neither of the criterion's thresholds is met under any reading". The +dSpike threshold is met beyond 300 µm (1.01–1.06 ≥ 1) [28]. Only both together are never met, which is what [29] says.
- **fig2h:** "109 to 110 -dSpike bAPs in the Fig. 2 file" should be 106 to 110 [31]. `measured: 1488.2` is the median k=4 variant; the claims-setting value is 1457.0. Minor.
- **fig3-predepolarization:** "45 to 48%" should be 44 to 48% (as in [47]).

**Round-1 reasons:** the attempt record restates all 55 of my round-1 reasons faithfully, close to my own wording. The one misstatement is in the fig3d *response*, about B2 (see section 1).

### 3. Round-1 points

**Resolved:**
- **B5:** figs20 was run (429 runs); figs21 was ported to Python.
- **B7:** traces and a table for the orphan distal events were added [35].
- **B9:** a shared threshold for the three Fig. S18g files was added, but [67] misreports the per-file case (section 2).
- **B11:** the uncentred PCA readings were added [49].
- **B13:** the 488 nm drive is 0.200 V in all 20 stimuli [60].
- **B15:** runs with Table 1's NaV 47 and 300 ms steps were added [S7].
- The fig5b part of B4: ratios computed [77].
- fig3i: I accept the author's reasoning for data_missing.

**Remaining points that bear on a conclusion:**
- **B1 (partly resolved), dSpike threshold rule.** A NaN threshold is now reported as undefined, and the "more dSpikes than failures" case is fixed by taking the lowest mode. However, the stated rule that "density peaks under a quarter of the highest are not modes" only picks the lowest mode. It does not stop a trough in front of a small tail bump.
  - On synthetic data (100 failures around 0.4, plus 2 outliers near 0.95–1.0), `first_min_threshold` returns 0.78 rather than undefined.
  - So "defined" and "undefined" calls do not follow the rule as stated. This bears on fig4d (174900: 0–3 dSpikes), figs17e (whether the Butterworth baseline has a trough), figs18g (152954 row 58) and figs15.
- **B2, the 4 s.d. threshold:** fig3d rests on it (section 1).
- **B3 (partly resolved), the distal region:** the region overlay [19] confirms the line is off the trunk beyond about 400 µm. Yet the claims-setting region still averages in background. fig3f passes and fig2a changes (6 rather than 8, Butterworth) under the region cut at 400 µm.
- **B12, unstable somatic detection:** still unvalidated. 174900 gives 58–160 bAPs, 001459 gives 71–132, 181900 gives 18–62. This bears on fig4d, figs15 and figs17e.
- **B14 (partly resolved), figs2:** electrical spikes are now counted after repolarization. The noise-equivalent voltage with maximum-likelihood weighting, and away from the first second, was not run, and the NEV failure may hinge on it.
- **B8 (partly resolved), figs23:** cell 160204 still gets 0–6 ms. The measure counts deviations of either sign: 002658, with a negative mean difference, gets 134 ms. The outcome holds in every reading.
- **B10, fig5d window (b):** the ratios at +30 and −100 ms are undefined, not lower. The "disagreement" is between a fail under (a) and undefined under (b).
- **B4, single-cell tests:** the single-cell parts of 27 blocked claims were not run "for lack of time". This does not change any blocked outcome.

**Remaining, no effect on a conclusion:** B6 (third spikes in Fig. 2; stated, not investigated), B16–B19. The B19 clock check still fails for 184232 [8].
