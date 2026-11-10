**Verifier report: daste-2025 on DANDI:000785 @ 0.260520.1603, round 1**

The claims file has 36 claims. My outcomes: 19 reproduced, 1 partially reproduced, 11 not reproduced, 5 blocked. Passive notebook = `P`, Go/NoGo notebook = `G`; numbers after them are cell indices.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| dataset-neuron-counts | partially_reproduced | Identity counts are 81/84/1937 and concentration counts 87/102/2132, all within tolerance (P5). Go/NoGo OB-p averages 103.3 or 107.5 per session against 95 ± 2, which fails under every reading and mouse set. |
| fast-dataset-counts | reproduced | 24/27/424 from 5 mice, an exact match (P7). |
| figs2b-labeling-similar | reproduced | No p < 0.05 under any of the 6 combinations (lowest p = 0.187) (P9). The groups are 10 OB-p and 8 mPFC-p mice, not the paper's 9 and 10. |
| mlp-projection-f1 | blocked (methods_underspecified) | Table 8 is missing from the text. The archive holds only 61 NWB files and no model files or hyperparameters (checked through the API). The traces it needs are present. |
| transformer-projection-f1 | blocked (methods_underspecified) | Tables 5 and 6 are missing; nothing in the archive supplies them. |
| fig1g-attention-timing | blocked (methods_underspecified) | Depends on the transformer. |
| fig1f-latent-separation | blocked (methods_underspecified) | Depends on the transformer. |
| fig2b-lifetime-sparseness-similar | not_reproduced | mPFC-p vs untagged has corrected p = 0.0067 (start reading) and 0.0147 (centre reading) (P14). |
| fig2c-mutual-information | not_reproduced | OB-p is lower than untagged, but corrected p = 0.19 and 0.17 (P16). |
| fig2d-population-sparseness | not_reproduced | All 3 pairs are significant, including OB-p vs mPFC-p (corrected p = 8.7e-6) (P20). |
| fig2-proportion-responding | reproduced | Reading (a): OB-p 9.5% vs mPFC-p 6.9%, corrected p = 9e-6. Reading (b) fails (p = 1) (P22). |
| fig2e-reliability | not_reproduced | No combination has both tests holding at Bonferroni ×3, and at most 1 of the 4 percentages is within tolerance (P24). |
| fig2f-latency | reproduced | Per-trial reading: OB-p median 3.58 s vs mPFC-p 4.65 s, corrected p = 3e-16. OB-p vs untagged corrected p = 1. The per-neuron reading also holds (P38). |
| fig2g-early-peaks | reproduced | OB-p > mPFC-p in both windows: 0.198 vs 0.138 (0–2 s) and 0.349 vs 0.203 (0–3 s) (P40). |
| fig2h-identity-decoding-5s | blocked (methods_underspecified) | The windows disagree: 0–5 s gives p = 0.675, 1–5 s gives p = 9.7e-9. The criterion assigns methods_underspecified in that case (P28). |
| fig2i-identity-decoding-early | reproduced | 17.8% vs 16.3%, p = 5e-5 (P30). |
| fig2j-identity-decoding-peaks-earlier | reproduced | OB-p peaks at 5.75 s and 5.50 s, mPFC-p at 9.25 s and 9.00 s, under both widths. The per-repeat 95% intervals overlap widely (P32). |
| fig2k-mpfc-late-identity | reproduced | mPFC-p is above 12.5% and above OB-p in all 4 combinations (largest MWU p = 3.8e-5) (P34). |
| fig3bc-concentration-tuning | reproduced | Concentration 10.3% vs 6.9%, interaction 9.2% vs 6.9%, identity difference 1.56 < 3.48 (P44). These are about 9 vs 7 neurons and no test was run. |
| fig3de-concentration-decoding | not_reproduced | mPFC-p peaks at 53.6% and 52.4%, above the midpoints of 47.6% and 47.7% (P47). |
| figs5g-pairwise-concentration | not_reproduced | The order OB-p > untagged > mPFC-p holds for only 1 of the 3 pairs, under both widths (P49). |
| figs5-sparseness-concentration | reproduced | No monotonic change of more than half the 0.1% value; the largest is untagged % active at +48% (P51). |
| fig4c-behavior-learning | not_reproduced | F is between 1.57 and 3.74 against 4.375 ± 0.44. The day effect is not significant in the 7-mouse readings (p 0.12–0.25). The day-3 mean of 76–79% is within tolerance (G7). |
| fig4c-anticipatory-licking | reproduced | Day-3 CS+ lick rate is higher than day 1 in both windows and for both mouse sets (G9). |
| fig4def-identity-decoding-gng | reproduced | 7 mice, mean aggregate: OB-p above chance in all 4 phases, peak in delay, act-late below delay. mPFC-p lowest in odor and delay, peak in act-early (G16). mPFC-p odor accuracy (36%) is far from "near chance". |
| fig4g-valence-any | reproduced | Any-p is above 50% in all phases under both aggregates (largest corrected p = 9e-7) (G18). |
| fig4h-valence-timing | not_reproduced | OB-p act-late is above 50% under every reading (56–57%, p ≤ 5e-25). Under the mean aggregate, mPFC-p odor is also above 50% (G20). |
| fig4ij-valence-correct-trials | not_reproduced | mPFC-p odor is far above 50% (70–73%), and only 2 or 3 phases differ between groups (G22). |
| figs8-generalized-valence-correct | not_reproduced | Delay differs strongly in every reading (corrected p ≤ 2e-28), and act-late differs in most (G24). |
| tracked-neuron-counts | reproduced | 46 OB-p / 41 mPFC-p, exact under min_3_sessions (G28). The OB-p cells come from 3 mice; sub-664 contributes 0. |
| figs10d-slope-no-difference | reproduced | Projection p = 0.35; interaction p = 0.0035 against the paper's 0.0031 (G32). |
| figs10e-sparseness-slope-no-difference | reproduced (weak) | Projection p = 0.29 and 0.48, but only 16 and 8 of 87 neurons are kept. One variant (centre reading, undefined values set to 0) gives p = 0.048 (G34). |
| fig5c-cv-higher-obp | reproduced | Projection p = 0.0115; OB-p median CV 0.230 vs 0.193; the two CV readings give identical results because all means are positive (G36). |
| fig5e-transferability | reproduced | Only under reading (a), every entry as a sample: identity proximal and distal p = 1, generalized distal mPFC-p higher with p ≈ 0. Per-mouse means (reading b) give p = 0.6 (G39). |
| fig5f-stability | not_reproduced | No combination of readings meets the criterion. Unconstrained valence is never significant (G41). |
| discussion-differences-grow | reproduced | Identity, mean and max aggregates: OB-p slopes positive in odor and delay, mPFC-p positive in the action phases (G26). |

### B. Problems

1. **[affects a conclusion] G13, clock check.** The per-session check fails for the two 2023b mPFC mice. Using all ~280–300 of each mouse's cells, odor-phase identity decoding is no better than baseline:
   - sub-2456: 33.4% in the odor phase vs 29.0% at baseline.
   - sub-2457: 29.2% vs 33.2%.
   - The other five mice reach 48–73% in the odor phase.

   These two mice supply about two-thirds of the day-3 mPFC-p cells (59 of 93). A wrong onset alignment, or a genuine absence of odor responses in these sessions, would produce exactly the "mPFC-p near chance early, better late" pattern. The notebook never follows this up. It bears on fig4def, fig4h, fig4ij, figs8 and discussion-differences-grow.
2. **[does not affect a conclusion] G13–G24, chance level.** The paper states chance as 25% and 50%. The notebook's day-3 pseudo-population trials are unbalanced: 70 trials with the smallest CS at 9, because sub-644 has only 9 trials of one CS; correct trials are 30 with a minimum of 3 per CS. The tests still use 25% and 50%. The empirical identity baseline of 29.4% (G13) suggests an effective chance near 30%. Unconstrained-valence chance is the majority fraction, which is unknown. The claims that depend on this fail for other reasons.
3. **[affects a conclusion] G34, figs10e.** The absence of a projection effect is judged on 16 (start) or 8 (centre) of 87 neurons. 71 and 79 neurons are dropped because their sparseness is undefined. One fill variant gives p = 0.048. The test has almost no power, so a non-significant p says little.
4. **[affects a conclusion] P12 and P14, fig2b.** Never-active cells are dropped: 21 of 81 OB-p, 11 of 84 mPFC-p, 230 of 1937 untagged. The paper reports n = 81 and leaves the handling open, but the notebook runs only this one treatment. The significant mPFC-p vs untagged result could change if the cells were filled, as G34 does for figs10e.
5. **[affects a conclusion] G39, fig5e.** "Reproduced" rests only on reading (a), which pools correlated matrix entries from 3 mice per group (60 entries each). The per-mouse reading gives p = 0.6. The distal effect is carried by sub-2456 and sub-644.
6. **[does not affect a conclusion] P24, fig2e.** The "Bonferroni over 2 tests" variant is the author's own addition. The Figure 2E legend shows three groups, which supports ×3. Under ×2, reading bceh would make the claim partially reproduced.
7. **[does not affect a conclusion] P47, fig3de.** mPFC-p concentration decoding before odor onset is 37.2–37.6% against a 33.3% chance, with near-balanced classes. This is unexplained. In addition, the peak of the mean curve across about 68 windows is biased upward by taking a maximum. mPFC-p fails the midpoint by about 6 points either way.
8. **[does not affect a conclusion] G26, discussion-differences-grow.** Mann-Whitney U on 1000 resampled slopes against 1000 null slopes makes p arbitrarily small. Nearly every cell is "significant", including mPFC-p odor and delay. The criterion never tests whether the OB-p/mPFC-p difference grows, which is a weak reading of "differences increased".
9. **[does not affect a conclusion] G28, tracked-neuron-counts.** Red-cell counts include the day-4 sessions of GNG_2023b. That follows the code, but the claims file says "red in at least 3 of [the four sessions]". The counts still match exactly.
10. **[does not affect a conclusion] `pcx.load_session`.** `np.clip` on the frame indices silently repeats edge frames for any trial window that runs past the end of the recording. The number of clipped trials is never printed.
11. **[does not affect a conclusion] Helper tests on synthetic inputs** all pass:
    - `mwu_greater_p` matches scipy's exact p for n1 = 3, 4, 7 and its asymptotic p for n1 = 9.
    - `vinje_gallant` and `mutual_info_bits` match hand values and sklearn.
    - The notebook's `anova2` matches statsmodels' type II ANOVA on an unbalanced design.
    - `pseudo_population` matching by (label, order) and `hit_relabel` behave correctly.
    - `binarize` detects a synthetic response, gives no false positives, and can fire in the 2 s odor phase.

### C. What I could not check, and the output that would settle it

- **Onset alignment for sub-2456 and sub-2457 Go/NoGo sessions.** Needed: onset-aligned mean traces (all cells) per session, and per-session decoding in 1 s windows across the trial.
- **Effective chance in Go/NoGo decoding.** Needed: per-CS and per-valence trial counts of every Go/NoGo pseudo-population table, plus shuffled-label null accuracies per scheme and phase.
- **Sniff alignment in the 30 Hz data.** I could not confirm that `stim_onset_timestamp` in the 30 Hz files is the first-sniff time; the file names (`fast_hz_sniff_trig`) suggest sniff-triggered delivery. Needed: the trials-table column names and one row from a fast-dataset file.
- **Lick time reference.** Needed: one Go/NoGo trial's `start_time`, `stim_onset`, `stim_onset_timestamp`, `reward_onset` and `lick_onset`, to confirm the licks are in the same reference frame as `stim_onset`.
- **Clipped trials.** Needed: the count of trials whose analysis window was clipped in `load_session`.
- **fig2b robustness.** Needed: the lifetime-sparseness tests with never-active cells filled (as G34 does).
- **Plots.** I saw only the printed value ranges, not the images.
