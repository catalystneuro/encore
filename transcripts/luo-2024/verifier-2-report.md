**Verifier report, round 2: Luo et al. 2024 (doi:10.1002/cne.70001) on DANDI:001261 v0.250917.2023**

The claims file has 29 claims, and the attempt record has 29 outcomes with the same IDs: 7 reproduced, 6 partially reproduced, 4 not reproduced and 12 blocked (11 data_missing, 1 methods_underspecified). The notebook was re-run with the step onset fixed, and many numbers have changed since round 1.

### 1. Outcomes

I agree with all 29 stated outcomes as judged against the claims file's criteria.

| Claim | Outcome | My check (cell) |
|---|---|---|
| sample-sizes | partially reproduced | 4 of 5 counts match; mouse NC is 45 distinct recordings against 46 (21). The 46 macaque C neurons come from only 6 of the 9 macaques. Read strictly against "46 cholinergic neurons from nine macaques", the macaque count also fails. The outcome stays partial either way. |
| fig2-mouse-c-nc-15-of-18 | reproduced | 13 of 17 under F17/F18 reading b, inside 13 to 15. Width, upstroke and downstroke do not differ (24). This meets the criterion as written, but only just: it sits on the lower edge, and one of the 13 is AHP width in the reversed direction. Counting only differences in the paper's direction gives 12. The record says this. |
| fig2d-mouse-max-firing-rate | partially reproduced | p = 1.9e-12. NC mean 34.8 is outside 35.1 to 42.9 (27). |
| fig2d-mouse-threshold-rheobase | partially reproduced | Rheobase p = 1.13e-3, not below 0.001 (30). |
| fig2d-mouse-ahp | not reproduced | Width is reversed: p = 4.1e-5 in the window, p = 0.017 to the end of the step (33). |
| fig2d-mouse-adaptation | reproduced | Reading b: p = 0.011, both means within tolerance (36). |
| fig2d-mouse-passive | not reproduced | Tau p = 3.2e-3, and both means are outside tolerance (39). |
| figs2-2-mouse-amplitude-cv-sag | reproduced | p = 5.4e-5, 1.3e-3 and 1.8e-3 (42). The outcome depends on the saturation rule; see the assumptions below. |
| fig2c-mouse-umap-separation | not reproduced | Medians 4 and 8.5 against at most 2 (45). |
| fig5a-mouse-lda-electrophysiology, fig5b-mouse-lda-ahp-amplitude-top | reproduced | Cells 48 and 51. |
| fig7d-macaque-more-excitable | partially reproduced | Macaque maximum rate 21.47 is outside 23.67 to 28.93 (54). |
| fig7d-macaque-threshold-ahp | partially reproduced | Two of three tests hold; width p = 0.17 (57). |
| fig7-macaque-spike-width | not reproduced | p = 0.013, not below 0.01 (60). |
| figs7-1-macaque-amplitude-cv-sag-upstroke | partially reproduced | Sag p = 0.090; downstroke differs, p = 7.6e-3 (63). |
| fig7-macaque-mouse-feature-count | reproduced | 14 of 17 under reading b, the lower edge of 14 to 16 (66). |
| fig7d-macaque-input-resistance | reproduced | p = 2.9e-5 and 6.1e-11 (69). |
| fig7c-macaque-mouse-umap-separation | blocked, methods_underspecified | Reading b holds and reading a fails (72), the case the criterion assigns. |
| The 11 morphology claims | blocked, data_missing | Unchanged from round 1. |

**Assumptions.** No outcome carries `assumed: true`. Two outcomes rest on choices the attempt made that the record should flag:
- **figs2-2-mouse-amplitude-cv-sag.** "Saturated" is read as 1000 or more consecutive identical samples, because the code's own test cannot fire. Without the rule, sag gives p = 0.011, which misses the figure's 0.01, so this reading decides the outcome. The reading is reasonable: the 7 mouse responses it catches are clipped at -100 or -105.5 mV for 1144 to 4793 samples (16). It should still be marked `assumed: true`.
- **sample-sizes.** The duplicated CG608 file is counted as C because its name says G+. That is reasonable and it does not change the outcome.

The new onset rule (the longest non-zero run in each sweep) is shown by the data, not assumed. Cell 8 shows it and plots one sweep, and cell 7 finds no step whose onset differs from its file's onset (0 of 2309).

### 2. Sentences the printed outputs do not support

- **Cell 67 and the record notes for fig7-macaque-mouse-feature-count:**
  - "Sag, AHP latency and AHP width do not differ under any set of readings". Under the code's AHP window, AHP latency (p = 0.011) and width (p = 3.5e-4) do differ (66). The sentence holds only for the F11/F17/F18 sets.
  - "counting F1 would not raise the count". This rests on names giving F1 for only 22 macaque and 8 mouse neurons, so it is not shown for the analysed neurons.
- **Cell 10:** "The steps run from -60 (or -100) to 200 pA, in some files to 300 pA". Cell 7 prints steps up to 1200 pA, and the finding itself says "one to 1200 pA".
- **Cell 4 and the amplifier finding:** both say the bridge balance (2e7 Ohm), capacitance compensation (1e-12 F) and gain (1) are the same in every file. Cell 3 prints only `bias_current`, so the other values are not in any output.
- **Cell 9, the record's deviations and finding, README line 39, Summary (cell 76):** "in every sweep" of the 8 files. Cell 8 counts the affected sweeps (170) but never prints how many sweeps those files hold. Cell 9's "two macaque neurons of M#11" is also never printed for those two files.
- **Cell 31:** "5 to 50 pA apart". Cell 7 also shows one file with 100 pA steps.
- **README line 42:** "about two minutes". Cell 77 prints 2.6 min.

Every other sentence in the Results, the Summary, the README and the record notes matches the printed numbers.

The record's round-1 reasons are my round-1 reasons, close to verbatim, with my numbered problems added to the relevant claims. Two small omissions:
- My round-1 problem 4 (files dropped where they could have been rescaled) is in no reason.
- The fig7-macaque-mouse-feature-count reason leaves out my note that the onset error likely changed that count.

### 3. Round-1 points

**Resolved:**
1. Step onset: fixed and shown (cells 7 to 12). The 8 "non-responsive" neurons and the tau outliers (CG250 401 ms) are gone.
3. F14 window: crossings are now searched within the window, as the claims file says.
4. Dropped macaque file: shown rescaled as a variant, which changes no outcome.
5. F16 cap at 200 pA: the code's maximum over every step is shown as a variant.
6. Tie correction: the rank-sum is now computed with the tie and continuity corrections.
7. Cross-validation leak: imputation and scaling are now fitted on the training folds only.
8. Sag saturation rule: implemented.
9. count() direction: now reported.
10. ChAT-unknown neurons: addressed in cell 21.

From "What I could not check":
- The tau fits now have R² values and a plot.
- `general/notes` is shown; it holds only a bregma position.
- UMAP parameter sensitivity is shown, and changes no outcome.

**What remains that bears on a conclusion:**
- **Problem 2, the claims file's AHP window.** This is still open and has gone to a reader. The code's window matches the paper's mouse AHP values. The Methods window reverses the width, and that reversal decides fig2d-mouse-ahp, fig7d-macaque-threshold-ahp and the "13" of fig2-mouse-c-nc-15-of-18.
- **A likely cause of the reversed AHP width (unverified).** Under F14's rule ("to the end of the step if it does not recross"), most widths reach the end of the step. NC widths average 298.9 ms against the 100 ms window, and the maximum is 449 ms. The width then mostly measures the time left after the first spike. NC neurons spike earlier (latency 142 ms against 283 ms for C, cell 18), so they get longer widths whatever the AHP's shape. A per-neuron table of AHP width against latency, with a flag for neurons that do not recross, would settle it. This adds to the case that the claims file's reading of F14 is not what the paper computed.
- **Tau fit quality.** The -20 pA fits are poor in many neurons: 33 of 47 mouse C fits have R² below 0.9, and the minimum is 0.094 (39). This decides fig2d-mouse-passive under the claims file's step, and the code's larger step reproduces the paper's values. The outcome follows the criterion, but it may reflect noisy fits on a small step more than the neurons.
- **The saturation reading for figs2-2-mouse-amplitude-cv-sag** should be flagged `assumed: true`, as above.
- **Both feature-count outcomes sit on the lower edge of their range:** 13 for mouse and 14 for species. The 200 pA reading drops each by one, to 12 and 13, which is out of range.
