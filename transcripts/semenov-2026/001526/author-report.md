I did steps 1 to 6 of the Author section. The entry, the attempt record and the handover are written, and `tools/entry.py all` passes (0 errors, notebook ran in 747 s). Of the 30 claims, 5 could be tested and 25 are blocked because their data are not in the dataset.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig2cd-nonelectroporating-stable | not reproduced, rests on the background assumption |
| fig2c-1000-within-set | reproduced, rests on the background assumption |
| fig2d-lasting-reduction | partially reproduced |
| fig4d-short-pulses-same-limit | not reproduced |
| fig5b-eq2-sensitivity | partially reproduced |
| the other 25 claims | blocked, data missing |

- **fig2cd:** one of 12 comparisons is significant (p = 0.047) with a cell-free background subtracted. Without subtraction none is (smallest p 0.057), which would reproduce the claim.
- **fig2c-1000:** the start and end values are 31.9% and 21.0%, against 40% and 26.6%. The p-value is 0.051, just on the right side of the paper's p > 0.05.
- **fig2d:** the drop after 1000 V/cm is significant but larger than the paper's: 22 to 33% per set, 27.5% on average, against about 20%.
- **fig4d:** the maximum dF is 34.9% and 34.0% at the two poles, against 53 ± 4%. The pattern of decline at stronger fields does match the paper.
- **fig5b:** Eq. (2) gives 11.9% for a 100-fold increase, which matches the paper's 12%, but 1.3% for a 10-fold increase, where the paper says about 2%.

**2. Dataset, assumptions, questions**
- **Version:** I pinned 0.261006.1851. It is the only published version, and the paper cites none.
- **What it holds:** Di-8-ANEPPS images only. There are 11 cells for the Fig. 2C/D protocol (the paper reports 8) and 8 cells for the 0.3 µs escalation of Fig. 4D (the paper reports 10).
- **What it lacks:** the FluoVolt, the 1 µs escalation (Fig. 1, 2B, 4B, 4C, 7B top), Gd3+, Ca2+ and two-pulse experiments.
- **Findings recorded:**
  - The files give pulse amplitudes in volts, not field strengths. I matched them to the paper's V/cm labels by order.
  - The electrode distance is 1.00 mm in the files and 1.6 mm in the paper.
  - Every file carries the same description, which describes only the 2025-05-01 protocol.
  - `starting_time` holds Unix times, not seconds from session start.
  - There is no pixel size.
  - Nothing says which of the several cells in each field of view was analysed.
  - In 174 of 232 cell recordings the first image is about 22% darker than the rest.
- **Assumptions:**
  - A cell-free background is subtracted before computing dF. The paper's values at 1000 V/cm are on the scale of the subtracted readings, and all readings are shown.
  - The analysed cell is the one nearest the image centre.
  - The membrane trace is found automatically instead of drawn by hand.
  - The pole angle is the session's median cosine phase.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): was background subtracted, and which cells form n = 8 and n = 10? The Eq. (2) 10-fold mismatch is recorded as a `paper_inconsistency`.
- **Questions to a reader:** none.

**3. Protocol gaps**
1. Neither the protocol nor the claims file says what to do when a method reading named in the claims header (background subtraction) applies to every claim at once. I treated it as a step 1.6 assumption shared by all tested claims and ran every reading.
2. fig5b's criterion defines no partial case. I recorded one of two values matching as `partially_reproduced`.
3. The protocol has no rule for one expected value that covers "each pole" (fig4d). I gave the larger pole's maximum as `measured`, with both in the notes.
4. fig2d's criterion leaves unclear whether "within tolerance" and "p < 0.05" must hold for the same set. I report both ways; with the paper's F0 neither way is met.

**4. Runtime and failures**
- The notebook takes about 12.5 minutes, most of it streaming the 243 files (8.3 GB), with no failures.
- One permission-gated shell command (a grep over saved output) was denied automatically. I read the same output with the Read tool instead.
- The untracked dotfiles in the checkout (`.bashrc`, `.idea` and so on) are not mine, and I left them alone.
- I did not commit, as instructed.
