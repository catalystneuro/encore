I've answered every point in the round-2 report, re-run the entry (`python tools/entry.py all`: 0 errors, notebook passes in about 3.5 min), and recorded round 2 under `verifications`. Nothing is committed.

**Outcomes.** None changed, as round 2 requires. The verifier disagreed with two, and I agree with both, so each carries a `proposed` change for round 3:
- **fig4c-wt-contrast-zx1-effects:** stays blocked; proposed partially_reproduced. All four model readings meet the partial condition, and they differ only on the full one. The partial condition holds under all four readings with the main cleaning, the narrower jump rule (below) and the round-1 cleaning without AA0319 and AA0334. It holds under none with the round-1 cleaning or the single pass.
- **fig4-wt-posthoc:** stays partially_reproduced; proposed not_reproduced. The criterion has no partial level, and the "ZX1 does not change LOW" part fails (p = 0.0496). The proposal states one complication: with the narrower jump rule all four parts are met. So this outcome rests on the cleaning.

**What I added or corrected:**
- **Jump rule's reach:** it runs on the raw trace, so it drops 118 trials in 15 mice. I added a variant that counts the jumps after the spike filter. It drops 39 trials in 6 mice and gives the same animal maxima. This is now stated in the data check, the summary, every cleaning deviation, and the notes of the outcomes it moves.
- **Group A keeps AA0335:** this is now stated as an assumption that fig2b and fig3b rest on. Without AA0335, fig2b's readings would disagree (p = 0.028) and fig3b would be partially reproduced (p = 0.087).
- **Fig. 6a check:** the variants cell now checks all four ZX1 readings against ACSF under every cleaning, not just reading (a). The sentence "no cleaning variant gives an overlap" was wrong. With the round-1 cleaning without AA0319 and AA0334, the added reading (d) overlaps ACSF. The three readings the criterion lists never do, so the outcome stands.
- **Text corrections:**
  - The Fig. 2c finding now gives 0.011, 0.099 and 0.16.
  - The GCA weight finding now gives -4.12 to -8.24.
  - "13 of 16" is replaced by a printed count: 5 of 8 readings with SD over time and 8 of 8 with SD across trials.
  - The per-bin table in the fig1i post hoc cell is no longer called the "main reading".
  - The README now says Figure 1 outcomes also change with the cleaning.
- **Notes:** fig1i, fig2c and fig6c now say their outcome rests on the cleaning, giving the single-pass and narrow-rule results.

**What I did not do:**
- **`assumed: true` on blocked outcomes:** the record's schema rejects this flag on a blocked outcome, so the five blocked outcomes the verifier named (fig2c, fig4c, fig4f-ko-no-contrast-effect, fig6c, methods-corr) cannot carry it. Their notes say instead that the outcome rests on the cleaning, and fig4c's proposal says the new outcome would carry the flag.
- **fig2e:** left without the flag, since its test uses no pupil data, as the verifier suggested.
- **Main cleaning:** kept as it was. The narrower jump rule is only a variant, because adopting it in round 2 would change numbers across the whole record.
- **Questions:** none added to `questions/001256.yaml`, since the report found no place where the claims file misreads the paper.
