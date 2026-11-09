**Verification report, round 2: Duszkiewicz et al. 2024 on DANDI:000939 (0.261016.2310)**

The claims file has 34 claims, and the attempt record has 34 outcomes: 24 reproduced, 6 partially reproduced, 1 not reproduced and 3 blocked. One outcome rests on an assumption (`assumed: true`): fig6c.

### 1. Outcomes

I agree with 33 of the 34 outcomes. Notes on the ones that changed or were in question:

- **cell-classes-counts, now reproduced: agree.** The code's session list shows that the one missing session is the Neuropixel recording, with 239 units, and 1,760 + 239 = 1,999 (cell 6). My round-1 argument assumed the missing session was one of the H5 recordings (185 units at most), so it does not apply. The criterion foresees exactly this case.
- **fig3e, partially reproduced: agree.** The main reading (numeric covariate, squared modulus) gives p = 0.365. The rms and categorical readings are significant, and the direction holds under every reading (cell 53).
- **fig3g, partially reproduced: agree.** The criterion defines no partial outcome. Under squared modulus only components 1 and 2 are above control (component 3, p_bonf = 0.064); under rms, components 1 to 4 are (cell 34). Each reading gets part of the claim, so partial is a fair call. The set the claim names, 1 to 3, holds under neither. In round 1 I labelled problem 6 (the reversal order) "does not affect a conclusion". Its fix did move component 3 under squared modulus from significant to not, but the outcome is unchanged.
- **fig3h, not reproduced: agree.**
- **ed8cd, partially reproduced: I now disagree, and would give reproduced.** The criterion itself says the noise is titrated, so the code's fixed 1.8 × 1.8 noise is not a reading the criterion asks for. I used that noise in round 1, and that part of my reasoning was wrong. With titrated noise, the outcome depends only on which control is used. The recorded-control reading fails its own check: the titrated *no-gain* simulation already differs from the recorded controls (multiplicative p = 0.0026, additive p = 0.039; cell 82). So that comparison cannot tell gain types apart. Against the simulated control, which is how Figure_GainSimulation.m builds it, the criterion holds: p = 0.022, 7.5e-5 and 0.127. That leaves reproduced, with the caveat that it holds in 80% of 50 seeds.
- **fig5e, partially reproduced: agree, as tested on the claims file.** It fails only under exclusion reading (b), which the Methods' "no cells from other populations" rules out (see section 3).
- **fig6c, reproduced and assumed: agree.** The assumption is stated in the record, the notebook and the Summary, and it is reasonable. The flagged pairs are clearly divergent fits (|coupling| up to 3e73), while the kept pairs' |coupling| is at most 4.2 in WAKE and 10.7 in REM. The Spearman ordering holds even with nothing removed: HD-HD 0.759 against FS-FS 0.417 (cell 96). The mirror follows glmfit's IRLS start, the sqrt(mu) weights, the eps^(2/3) bad-scaling test and the convergence rule. It may not reproduce glmfit's clamping of the linear predictor (my recollection, not checked), but that should only change coefficients of pairs that are flagged and removed anyway. One difference is not covered: the code also removes pairs with warnings at any of 201 lags, and only lag 0 is fitted here. The pair counts (34,611 against the paper's 34,270) suggest this effect is small.
- **ed6, blocked: agree.** The record uses `other` rather than `data_missing`, citing the protocol, which I cannot see. This is a labelling question only, not the outcome.
- **fig1ac, reproduced (qualitative): agree.** The commented-out line of GetCellTypes_PoSub.m identifies the PoSub side independently of the depth sign. The crossing is at cellDep = −35 µm, and the two sides have mean HD information 0.905 and 0.145 bits per spike (cell 111).

### 2. Text against the printed outputs

Nearly every number in the "Result" cells, the Summary, the README and the record notes matches the outputs. The exceptions:

- **Cell 7:** "The dandiset's own labels agree with the code's classes for 99.9% of units." This holds for excitatory and FS only. HD agreement is 0.9967 (cell 6), which the record states correctly as 99.7%.
- **Cell 54:** "its cumulative signature is above both at every component." Only components 1 to 9 are tested; at component 10 all three cumulative signatures equal 1. The record says "components 1 to 9".
- **Cell 112 and the fig1ac record note:** "stays near 0.01 to 0.24 … over the top 1.4 mm", "between 0.78 and 1.19 from 1.8 mm down" and "a smaller bump near −0.6 mm (0.19)". These rest on a print of every fourth 50 µm bin (cell 111). Only the overall extremes (0.008 and 1.192) are printed in full, so the bins in between are unverified.
- **Record findings, format_error:** "933,367,680 samples for an 11,667 s session" and "In A1808 it holds one channel of 0 and 1". No cell prints the series shape; cell 71 prints only the decoded pulses.
- **Record findings, metadata_error:** "A1821 (57 s, during the optogenetic exploration) and A3712 (12 s, during the square exploration)". Cell 2 prints the seconds, but not which exploration epoch each falls in.
- **ed8cd (cell 83, record notes, Summary row):** "The criterion holds under one of the four combinations" counts the fixed code-noise readings, which the criterion does not call for (see section 1).
- **README:** the GLM row says "Reproduced" without the assumption that the Summary and the record state.

The record's statements of my round-1 reasons are accurate and close to my wording. My separate problems 4, 5, 7, 8 and 9 are folded into the matching claims correctly, and the `agrees` flags match my round-1 outcomes.

### 3. Round-1 points

**Resolved:**
- Problem 1 (ArchT mice): the choice is stated, and a five-mouse variant was run. HD against control is still z = 7.09, so the missing mice do not explain the HD z.
- Problem 3 (fig3e had no conclusion text).
- Problem 4 (parallel-unit shortfall).
- Problem 5 (decoder chance level scored against the reversed HD).
- Problem 6: the HD series is now reversed before the speed mask, and viable units are cut at ≥ 0.5 Hz. The split into halves remains a stated assumption.
- Problem 9 (identical CCG spans).
- Problem 11 (titrated noise is now the main reading).
- From section C: the depth sign, the REM epochs (restricted to the home-cage epochs, identical in both dandiset versions), the light pulses (matched to figshare within 0.1 ms) and the figshare loading (CellTypes agreement 1.0 for ADN-HD and 0.985 for the ADN opto cells).

**Partly resolved:**
- Problem 2 (GLM filter): there is now an explicit glmfit mirror, and the flagged pairs are described. The outcome still rests on the stated assumption; only a MATLAB run would settle it.

**Remaining and bearing on a conclusion:**
1. **fig5e:** the claims file's exclusion reading (b) contradicts the Methods (it excludes 31 of 62 HD cells; the Methods report 1 FS cell and no others). This misreading is reported, not corrected; it has been passed to a reader. Without reading (b), fig5e is reproduced.
2. **ed8cd:** the outcome should be reproduced, not partial, for the reasons in section 1.
3. **Power reading (problem 8):** the criteria's requirement of the rms reading decides fig3-ten-components-power (partial) and contributes to fig3e and fig3g. It is recorded as a question for the authors.
4. **fig6c:** the outcome rests on the glmfit-mirror assumption, plus the lag-0-only removal.
