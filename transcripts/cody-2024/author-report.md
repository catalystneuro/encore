I've finished steps 1 to 6 for DANDI:001256: the entry, the record and the handover are written. The notebook ran clean in 2 minutes (`tools/entry.py all` passes with 0 errors), and the verifier's handover is in `executed/001256-cody-2024/handover/`. Nothing is committed. The entry is `entries/001256-cody-2024/` and the record is `attempts/001256-cody-2024-01.yaml`. I pinned version 0.241120.2150, the only published version; the paper cites none, and the draft has the same 30 assets.

**1. Outcomes (24 claims)**

| Claim | Outcome |
|---|---|
| fig1f-tone-response-inverse-u | reproduced (318 cells, expected 295 ± 29.5) |
| fig1g-reliability-intermediate | reproduced |
| fig1h-cgc-largest-intermediate | reproduced |
| fig1h-cgc-evident-all-bins | not reproduced (the 32-43% bin is never above 1) |
| fig1i-baseline-contrast-interaction | reproduced (1830 values) |
| fig1i-contrast-effect-intermediate-only | not reproduced |
| fig2b-evoked-pd-whole-drc | not reproduced |
| fig2c-evoked-pd-1-2s | blocked, methods_underspecified (the readings disagree) |
| fig2e-drc-responses-no-difference | not reproduced (contrasts differ, p < 1e-8) |
| fig3b-lme-coefficients | reproduced |
| fig3c-lme-likelihood-ratio | not reproduced (p 0.001 to 0.048, paper 0.330) |
| fig4c-wt-contrast-zx1-effects | not reproduced (contrast x ZX1 p = 0.25) |
| fig4-wt-posthoc | not reproduced |
| fig4f-ko-no-contrast-effect | blocked, methods_underspecified (model readings disagree) |
| fig4f-ko-zx1-slope | blocked (depends on the claim above); its KO slope term is not significant |
| fig5 (three claims) | blocked, data_missing (no widefield imaging in the dandiset) |
| fig6a-baseline-pd-drift | not reproduced (both slopes positive, but the 95% CIs do not overlap) |
| fig6b-acsf-contrast-effect | partially reproduced (intercept effect yes, slope no) |
| fig6c-no-baseline-evoked-correlation | reproduced |
| methods-baseline-evoked-correlation | partially reproduced, assumed (r = -0.218 against -0.35) |
| fig6d-ko-reduced-high-contrast | reproduced |
| discussion-zx1-wt-like-ko | reproduced |

**2. Dataset, assumptions and questions**

What the dataset holds:
- Each of the 30 files is one mouse. It has a per-trial stimulus table (sound, contrast, treatment, delay to sound onset), ROI fluorescence at 5 Hz and pupil radius at 10 Hz.
- The files carry labels naming the paper's analyses, and these identify most groups. Group sizes still differ from the paper:
  - Figs 1-3: 10 mice in the files, 8 in the paper.
  - ZnT3-WT: 5 F and 5 M in the files, 6 F and 4 M in the paper.
  - Fig 2d-e: 12 mice in the files (two of them ZnT3-KO), 14 in the paper. No label names this group.
- No file holds widefield imaging, so Figure 5 cannot be tested.

Problems in the files, each recorded as a finding:
- The pupil traces contain tracking failures up to 1.5e6 pixels, and the DeepLabCut points the paper's cleaning needs are not deposited.
- 25 pupil series have the wrong length for their trial.
- Every pupil series's description names the wrong TwoPhotonSeries.
- For 84 trials in seven files, the stimulus table's starting time is off by exactly 24 h.
- The tone-free DRC stimuli switch contrast after 10 s, which the paper does not describe.
- Neuropil correction of the fluorescence is not stated.

Assumptions:
- **Pupil cleaning.** I added a spike filter to the paper's single derivative pass, repeated the pass, and dropped trials with more than half their frames missing. The single pass is shown as a variant. It leaves every outcome the same except fig4f-ko-no-contrast-effect, which would become not reproduced.
- **Contrast of a tone-free DRC trial** is the contrast of its first 10 s. The analysed 0 to 2 s fall inside that block.
- **Methods correlation.** I used the mice the files label `pupilBaseline_vs_evoked`, the only set whose counts match both reported counts. None of the claims file's readings matches.

Questions for the paper's authors, recorded as `methods_unavailable` findings:
- Which mice and which unit the Fig 2c test used.
- The exact GCA formula and factor coding.
- How the time polynomials are scaled (my WT ZX1 slope weight is -3.8 to -7.7 against the reported -1.41).
- How pupil tracking failures were handled.
- Which trials the Methods correlation uses.

I asked a reader nothing.

**3. Where the protocol was unclear, wrong or missing something**

1. For methods-baseline-evoked-correlation, the criterion's rule would block the claim, but the dataset's own label gives a well-supported reading. The protocol does not say which wins when the data, not the paper, settles a choice. I adopted the label reading as an assumption and noted that the criterion alone would block it.
2. Some blocked claims were fully analysed (blocked because readings disagree, or through a blocked dependency). The schema forbids `assumed` on blocked outcomes, but the protocol does not say how to report the analysis that ran. I put the results in the notes.
3. Whether to block a claim that depends on a blocked claim when its own analysis ran (fig4f-ko-zx1-slope). I followed the rule and blocked it, with the result in the notes.
4. When the data contain artifacts the paper's stated method cannot handle, it is unclear whether a fix counts as a deviation or an assumption. I recorded it as both a deviation and an assumption, and showed the paper's method as a variant.
5. Readings the author finds in the data (dataset labels) are not in the claims file. I ran them in addition to the claims file's readings and marked them as such.

**4. Runtime and failures**

The run took about 40 minutes (12:23 to 13:02 UTC); the notebook itself takes about 2 minutes. Statsmodels has no Satterthwaite F tests, so the mixed models use Wald z tests; this is stated as a deviation. Nothing failed.
