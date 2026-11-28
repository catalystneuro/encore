I wrote `claims/malfatti-2026.yaml` with 32 claims; nothing is committed. All 32 quotes pass the checker. It still exits non-zero, reporting 37 p-values as not found. All 37 are printed in the supplement with two-digit exponents ("5.5e-03"), a form the checker does not try. I matched every value against the text in that form and all of them are there. I did not change the checker.

**Text read.** The eLife reviewed preprint v3 (2026-11-02), from a PDF supplied by a person. That covers the main text, Methods, legends and author responses, plus the supplement (Supplemental Figures 1 to 7 and Tables 1 to 6). I could not open the PDF pages because the page renderer is not installed.

**Code read.** gitlab.com/malfatti/M1MartinottiOnMovement, commit 86efdf1 (2024-04-26), the only branch. It is older than all the reviewed preprint versions. It has no spectrogram or band-power code for the LFP bands, and no code for the trial-adjacency, baseline-epoch or during/before ratio analyses. Those methods rest on the Methods text alone.

**Claims.** All 32 have a quote and none needs an `inferred` note. 26 carry statistics, 66 values in all, and 10 have expected values. 31 have a criterion; only the ablation-efficiency claim is settled by its expected value alone. Several claims cannot be tested on this dataset: the c-Fos histology, the ablation efficiency, pasta handling and hanging wire.

**Details the paper leaves open, and the readings named:**
- **Prehension detection:** the Methods say the left paw and its three fingers; the code uses the paw and one finger. The code's version is kept as a variant. Accuracy is scored by the code's automatic classifier, since the Methods don't say how it was scored.
- **Task-modulated neurons:** selected per session (Methods) or per animal across sessions (code, run as a variant).
- **Learning-group behaviour:** all 11 sessions or only sessions 1, 2 and 6 (as the code tests); raw counts or counts per 10 minutes.
- **Baseline PC activity:** all frames outside the prehension windows, or the −5 to −1 s windows.
- **Prehension overlap:** within 2 s after onset, before onset, or either.
- **Trial adjacency:** observations are neurons or time samples.
- **Paired or unpaired** comparison of accuracies within session 2.
- **Which phase or accuracy** carries the genotype latency differences: before-peaking neurons, during-peaking neurons, or any.
- **Resilience:** equation 1 is lost in the extracted text, so the code's formula is used, with the code's loop over every reference session as a variant.
- **LFP:**
  - sessions 11 to 13, or 8 to 13 with treatment as a factor;
  - mean over channels, or one channel per mouse (the code's channel list is not in the repository);
  - two readings of "divided by the cumulative mean";
  - spectrogram window not given (1 s and 0.5 s);
  - the beta band is never defined (13 to 30 Hz is named as a standard choice).
- **Ratio:** how to handle a near-zero "before" amplitude is a standard choice (those neurons are left out).

**Missing from the paper:**
- Supplemental Table 1M to 1P (pasta handling, prehension after ablation) is cited but not in the supplement, so those two claims have no statistics.
- Equation 1 does not survive in the text, and equation 2 survives only as its terms.
- No test is named for the lower baseline in Cre+ mice (Supplemental Figure 2I).
- The paper's own counts disagree in places:
  - Cre+ per-animal cell averages give 459 cells, not the reported 403;
  - the LFP group is 11 or 13 mice;
  - the ablation group is 9 mice in the Methods but 14 in the Figure 5I legend.
