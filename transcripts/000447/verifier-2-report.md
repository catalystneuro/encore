**Verifier report, round 2: 000447-tang-2023-01**

The notebook was re-executed, but the conclusions for the UMAP-based claims were not updated to match it. Every number based on UMAP (Figures 3H, 3I, 3J, the CCGP of 4D, S7B and S7D) differs from the printed outputs. Results that do not use UMAP (Figure S6, every claim on the linearized maps) match. Two statements that decide outcomes no longer hold: the seed robustness of fig3h, and the reliance of fig3j on gap filling.

## 1. Outcomes and assumptions

There are 32 claims in the claims file and 32 outcomes in the record:
- 9 reproduced
- 7 partially reproduced
- 2 not reproduced
- 14 blocked: 4 data_missing, 1 other, 9 methods_underspecified

**I agree with these outcomes:**
- All four data_missing blocks.
- fig1c-familiar-above-novel, cells-per-session, both figs3a claims, fig2d, both fig2e claims, figs3c, figs3d, both figs4 ramping claims.
- figs4d, figs5d, figs5e, figs5f, fig3d, fig3e, manifold-cell-counts, fig3i, figs6.
- fig4d-pfc-ccgp (blocked, methods_underspecified). This still holds on the current outputs: 8 of 16 decoders pass at 8 cm, and all 16 pass at 2 cm (cell 79).

**Agreed with reservations:**
- **fig2f (partial).** At 2 cm, CA1 does not rise under either reading. Only the PFC claim of absence holds there, so "the other widths give no more" hides a qualitative difference. Calling it partial at every width is a judgement call, not a reading of the criterion.
- **fig3h (reproduced) and fig3fg, which follows it.** These hold at seed 0. At seed 1, the CA1 main alignment gives p = 0.096 (cell 81), so the outcome depends on the seed.
- **fig4d-ca1-ccgp-chance, figs7b, figs7d (blocked because they depend on fig4d-pfc-ccgp).** The rule "a claim that depends on a blocked claim is blocked" is not in the claims file, and I cannot check it against the protocol.
  - fig4d-ca1's own result does not change with width (4 to 7 significant decoders in every variant), so on its own it would be not_reproduced.
  - The figs7b null and the figs7d dichotomies were not run at the other widths.

**`assumed: true` flags:**
- **fig3h:** stated and reasonable. The flag is supported: without gap filling at 2 cm, PFC gives p = 0.105.
- **fig3fg:** follows fig3h, so the flag is fine.
- **fig3j:** stated, but the current outputs do not support it. Without gap filling at 2 cm, PFC is 4.86% closer than the shuffle, p = 6.2e-12 (cell 79). Every variant now agrees, so the outcome does not rest on the gap filling.

## 2. Sentences the outputs do not support

**Cell 82 (fig3h):**
- "13.81 against 16.05, rank-sum p = 0.0098 … 14.24 against 17.17, p = 0.0012". The output (cell 81) is CA1 13.83 vs 17.08, p = 0.00067, and PFC 14.72 vs 16.83, p = 0.015.
- "Both regions keep the direction at p < 0.01 under every alignment and seed". The output has PFC by location p = 0.081 (seed 0) and 0.15 (seed 1), and CA1 by location p = 0.096 (seed 1).
- "without gap filling at 8 cm (… PFC p = 0.00044)". The output is 0.0067.
- "(13.8 and 13.9, p = 0.28)". The output is 8.55 and 8.65, p = 0.105.
- The attempt record's notes repeat all of these, and its response says the numbers were "corrected".

**Cell 85 (fig3i):**
- "14.41 against 17.02 … 14.20 against phase 16.81 (p = 7.1e-259)". The output (cell 84) is 14.52 vs 16.91 (p = 4.7e-181), and CA1 13.84 vs 17.98 (p = 0).
- "The code's variant … fails under seed 0 (CA1 reversed, p = 0.008; PFC p = 0.19) and for CA1 under seed 1 (p = 0.44), and holds under seed 2". The output shows the opposite pattern:
  - Seed 0: CA1 holds; PFC is reversed (p = 0.0058).
  - Seed 1: both hold.
  - Seed 2: CA1 is reversed (p = 0.35).
- The same text is in the attempt record.

**Cell 88 (fig3j):**
- "11.99 against 13.86, 13.5% closer, p = 1.4e-127". The output (cell 87) is 11.70 vs 14.56, 19.6%, p = 8.6e-241.
- "12.60 against 13.38, 5.9% closer, p = 2.0e-47". The output is 13.65 vs 13.97, 2.3%, p = 1.5e-25.
- Seeds: the text gives "CA1 6.8% and 7.4%, PFC 26.0% and 14.1%". The output gives 6.0% and 3.3%, and 24.8% and 16.2%.
- Variants: the text gives "CA1 3.9% to 5.9%, PFC 5.9% to 59.6%". The output (cell 79) gives 2.1% to 5.5%, and 8.5% to 60.3%.
- "Without gap filling at 2 cm PFC … +1.8%, p = 0.41". The output is −4.86%, p = 6.2e-12.
- The same text is in the attempt record, along with the Summary bullet "at 2 cm the PFC parts of 3H and 3J fail" (the 3J part is wrong), the methods_unavailable finding ("PFC parts of Figure 3H and 3J fail at 2 cm"), and the README line "Partially reproduced, on an assumption".

**Cell 98 (fig4d-pfc):**
- "12 of the 16 … two of them … predict one class … 10 of 16 have p < 0.001". The output (cell 97) shows 9 by the strict count, 1 constant-prediction decoder, and 8 counting ties.
- The failing decoders are not the ones named. They are:
  - phase IN_R (0.583, p = 0.004)
  - phase OUT_L (0.230)
  - sequence IN_R/IN_L b (constant)
  - three environment phase decoders (0.385, 0.512, 0.486)
  - two environment sequence decoders (p = 0.001)
- "4 cm give 15 of 16 … without gap filling at 8 cm 4 of 16". Above all 200 shuffles, the output (cell 79) gives 14 and 1.
- The attempt record's notes, its round-1 response ("at 8 cm 10 of 16 pass") and the methods_unavailable finding ("(10 of 16)") repeat these numbers.

**Cell 100 (fig4d-ca1):**
- "8 of the 16 … predict one class (all four phase and all four sequence decoders) … 6 … all environment decoders (CCGP 0.578 to 0.680 …)". The output (cell 99) shows:
  - 4 constant-prediction decoders.
  - 5 significant counting ties. One is a sequence decoder (0.596); the CCGPs run from 0.562 to 0.642.
- "variants give 5 to 7". The output gives 4 to 7.
- The attempt record repeats this.

**Cell 103 (figs7b):**
- "PFC p 0.58 to 0.85 (a), 0.05 to 0.42 (b); CA1 0.17 to 0.77". The output (cell 102) gives PFC (a) 0.29 to 0.86 and (b) 0.23 to 0.65; CA1 (a) 0.72 to 0.94 and (b) 0.57 to 1.00.
- The attempt record's means "0.582, 0.637, 0.631" are 0.534, 0.713, 0.618 in the output.

**Cell 106 (figs7d):**
- "PFC 32 of 35 … median 0.830 against 0.635, p = 1.2e-09". The output (cell 105) is 33 of 35, 0.831 vs 0.660, p = 5.7e-08.
- The attempt record repeats this.

The direction of every one of these results is unchanged, except the two named above (the fig3h seed robustness and the fig3j gap-filling claim).

**Minor issues:**
- Cell 23 says the shuffle result is shown "over 200 draws"; cell 25 runs 100.
- Cell 71 / figs5f reports only 8 cm. At 2 cm the signed SI also gives a correlation (PFC SI(OUT) p = 0.047, cell 70). The outcome does not change.

All other "**Result:**" sentences, the rest of the Summary, the README's other rows, and the attempt record's other notes match the outputs.

The attempt record states my round-1 reasons in my own words, verbatim.

## 3. Round-1 points

**Resolved:**
1. **fig2f labelling (B1):** fixed. Reading (b) now has n = 114 at trial −1, against 258 under (a).
2. **Constant-prediction ties (B2):** fixed. `p_ge` is used and `frac_pred_1` is printed.
3. **figs3d K (B3):** fixed. Each animal's own last pass is used and the source epochs are shown.
4. **Width rule (B4):** applied.
5. **Ramping cell floor (B6):** justified.
6. **Decoder check (B7):** cross-validated N' error added.
7. **ZT2 transits (B8):** added. However, every session's trials tile its epoch, so "tile" is no evidence of completeness; the transit counts are.
8. **Native-map peak (B10):** added.

**Partly resolved:**
- **Gap filling (B5):** the variants were run, but the text describing them does not match their outputs (section 2).

**Remaining issues that bear on a conclusion:**
1. **The UMAP conclusions are stale.** The UMAP-based conclusions and record notes for fig3h, fig3i, fig3j, fig4d-pfc, fig4d-ca1, figs7b and figs7d do not match the re-executed outputs. The embedding with seed 0 also gave different results from one run to the next. This run-to-run variation is not stated and should be.
2. **fig3h and fig3fg depend on the seed.** At seed 1 the CA1 main alignment gives p = 0.096. The record says the opposite.
3. **fig3j's `assumed: true` is not supported** by the current outputs, and nor are the statements built on it: the Summary, the finding and the README.
4. **The dependency-blocking of fig4d-ca1, figs7b and figs7d** rests on a rule that is not in the claims file. fig4d-ca1's own result is not_reproduced at every width.
5. **fig2f at 2 cm** has no CA1 rise under either reading. Whether that is still "partial" should be stated as a judgement call.
