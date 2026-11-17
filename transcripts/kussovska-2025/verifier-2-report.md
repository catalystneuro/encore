**Verifier report, round 2: Kussovska et al. 2025 on DANDI:000469 (0.231213.2047)**

The claims file has 45 claims and the attempt record has 45 outcomes: 31 reproduced, 7 partially reproduced, 7 not reproduced. Seventeen outcomes are marked `assumed: true`. I checked the re-executed main notebook (149 cells), the new dPCA notebook (`dpca_kussovska_2025.ipynb`, 18 cells), `wm.py`, the README and the record.

### 1. Outcomes and assumptions

**The 39 outcomes left as they were after round 1: I agree with all of them.** That includes fig6cd, now not reproduced as I said in round 1. The printed values in the re-run support each one; caveats on fig4c and fig6e are in section 3.

**The three dPCA claims, now tested: I agree with all three.**
- **fig3abc, reproduced.** Maintenance medians are higher than encoding under both measures and both trial readings (dpca cell 12). Most of the gap comes from the longer maintenance window: over the first 499 bins it is tortuosity 2.46–2.57 against 2.16, and 9 reversals against 8. The record says so. The rank-sum p values treat the 500 values as independent, which they are not, but the criterion uses only medians.
- **fig3d, reproduced, but only under reading (b).** That reading is the code's own trial-selection bug, which the record reports as a finding (dpca cell 9):
  - Reading (b): H = 457.62; maintenance in its own space against maintenance projected onto encoding, p = 0.077.
  - Reading (a), the same trials in both epochs: those two maintenance conditions differ (p = 0.019).
  - The criterion names (b) as a reading, so the outcome stands. It is the code's result, not one independent of it.
- **fig3h, reproduced** with `protect=[]` for the early half (H = 410 and 413; dpca cell 15). Under the code's own setting the early half separates less than the late half in all 100 splits. That setting gives H = 394 and 380, also inside the tolerance, but in the wrong direction. The record states this.

**fig4c, reproduced: I agree only by the letter of the criterion.** It now passes only under `methods/height/d1/real` (cells 90–91). The criterion calls the 1-bin spacing a variant and the 2-bin spacing the main reading.
- With 2 bins, low ACG has BH p = 0.0601, so it fails.
- In round 1 the same reading passed with 2 bins (BH p 0.038 / 0.048). One run-to-run change in the ACG fit moved it across 0.05.
- Under the main spacing the best result meets the criterion's partial condition: `code/prominence/d2` gives all neurons and low ACG, plus concept cells (BH p 0.045).
- I would record this as weak. The record's own wording ("rests on one named reading") understates that it is the 1-bin variant.

**fig4d, reproduced: I agree.** It now uses the criterion's own-maintenance reading, and the control in cell 95 justifies that choice. Under that reading, `methods/prominence` gives the pattern with all three threshold settings, and concept cells have BH p 0.09–0.35.

**fig6e, reproduced: I agree by the letter of the criterion, but the result is fragile.** IN concept cells are 3 of 15 = 20.00% with p = 0.038 (cell 124). This rests on:
- the reading (a) cell types, whose PY count (102) is outside the fig5c tolerance;
- a fit that kept one more neuron in round 1, giving 16 IN concept cells and 18.75%.

With the reading (b) types, which have the paper's 14 IN concept cells, the matched-trial result is 14.29% with p = 0.15. Partially reproduced would describe the evidence better. The notes do disclose all of this.

**The assumptions are both stated and reasonable.**
- *Reading (a) cell types (all spikes).* This is justified by the shipped table, which matches on firing rate, ISI CV, mean ACG and burst index. Every cell-type claim is also run with the (b) types.
- *Own-maintenance window for fig4d and fig6ab.* This is justified by the burst-free Poisson control.
- *One gap:* the τdecay groups come from a scipy fit that agrees with the shipped MATLAB τdecay for only 11% of neurons (cell 75). The record states this as a limitation but never compares its groups with groups built from the shipped `Decay` column (see section 3).

**The claims file misses one paper statement.** The Fig. 6c legend defines M1–M3 as "the first, second, and final thirds of the maintenance epoch". The fig4f and fig6cd criteria cite only the Methods' 1 s windows and the code's thirds of the whole train. Per-trial thirds of maintenance are a third reading that was not run.

### 2. Text against printed outputs

**Wrong against the printed numbers:**
- **Cell 35 (fig1e):** "preSMA (20.40%, p = 0.000), vmPFC (18.75%, p = 0.009) and dACC (10.53%, p = 0.025) … the within-participant permutation gives 19.20%, 18.75% and 9.94%". Cell 34 prints preSMA 20.000% (50 of 250), vmPFC p 0.007, dACC p 0.026, and within-participant preSMA 18.800%.
  - The record's fig1e notes repeat the same stale values, and `measured` lists 20.4.
  - These are the round-1 run's numbers. The outcome is unchanged, since 20.0 and 18.8 are both inside 17.64–21.56.
- **Cell 41:** "seed 0 gives the paper's regional shares exactly". The notebook prints HPC 18.97% and vmPFC 5.17%; the paper gives 18.96% and 5.15%. "Exactly" is too strong.
- **Cell 53:** "The shuffled maps had no supra-threshold cluster" sits next to "Only 3 of the 1,000 shuffled maps have a significant pair". Those three pairs are clusters of extent 1. It is the 95th percentile of extents that is 0.
- **Record finding (peak-rule question):** "Fig. 4c is reproduced under the Methods' height rule with the Methods' groups". It holds only with the 1-bin spacing, not the Methods' 140 ms (cell 90).
- **Record `acg-fit-yield` notes and finding:** "317 in an earlier run of the same code, so one unit lies at the threshold". The fig1e GLM also changed between runs (51 → 50 significant preSMA neurons), and it does not use the ACG fit. So the change is not explained by one neuron at the R2 threshold (see section 3).

**Everything else checks out.** Every other "**Result:" sentence in both notebooks, both Summary sections, the README table and the record's notes matches the printed outputs. The README's category counts add up to 45, and its run times (about 45 and 22 min) match the printed 45.9 and 21.6 min.

**Round-1 reasons.** The record states them faithfully, largely in my words, including problems 1, 3–9, 11 and 12, each attached to the claims they bear on. Two are missing from every `reason`:
- **Problem 2** (types (a) used downstream; claims never run with the (b) types). It appears only in the author's responses.
- **Problem 10** (the 0 s subject-9 trial).

### 3. Round-1 points

**Resolved:**
- **1** (dPCA): computed in the new notebook.
- **2** (types (b) downstream): run for every cell-type claim, plus PY_b and IN_b burst groups.
- **3** (2.8 s window): confirmed by the burst-free control. The own-maintenance reading is now run under every reading and recorded as a finding.
- **4** (M3 rates per second): now given for every group.
- **5** (ACG fit): stated as a limitation.
- **6** (cluster rule): extents and shuffled-map counts are printed.
- **7** (chance level): binomial tests against 20% added.
- **9** (trial-draw spread): stated.
- **10** (subject-9 trial): checked and recorded as a finding.
- **11** (no single burst reading): stated.
- **12** (cross-trial intervals): within-trial CV2 variant added; spike counts stated for ext5gh.

**Accepted with no change:** 8 (the downstream concept set is a single seed). It does not affect a conclusion.

**What remains that bears on a conclusion:**
1. **Results change between runs and this is not explained.** Seeds are fixed, yet:
   - ACG yield went 317 → 316;
   - fig1e preSMA went 51 → 50 significant neurons (a GLM result independent of the ACG fit);
   - fig4c low ACG at 2-bin spacing went 0.048 → 0.060;
   - fig6e IN concept went 18.75% → 20.00%.

   Both the fig4c and the fig6e outcomes sit on this instability. A likely cause is the GLM's `|b1| ≥` 95th-percentile-of-null rule, which can flip on floating-point ties. Two repeat runs and a stability check would settle it.
2. **fig4c rests on the 1-bin spacing variant.** Under the main 2-bin spacing the best result is partial.
3. **fig6e rests on the reading (a) types and fails with the paper-matching (b) types.** Partially reproduced would describe it better.
4. **The τdecay groups were never checked against groups built from the shipped `Decay` column** (11% agreement within 1%). This bears on short vs long τdecay in fig4-acg-group-differences, on fig4hj, and on the decay groups in fig4c, fig4d and ext2.
5. **Fig. 4 still has no single peak rule supporting it as a whole.** fig4c needs the height rule (and 1-bin spacing), while fig4d, fig4-acg, fig4hj, ext2 and ext5bd need prominence. This is disclosed, not resolved.
6. **fig3d passes only with the code's mis-selected maintenance trials, and fig3h only with a protect setting the code does not use.** Both are disclosed; the outcomes are the code's result under one reading.
