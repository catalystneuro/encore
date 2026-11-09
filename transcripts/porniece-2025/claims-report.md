I wrote `claims/001474/10.1038-s41598-025-19800-2.yaml`. The quote checker passes on it with 0 problems. Nothing is committed.

**Text read:** the version of record (open access, Europe PMC PMC12521569): main text, figure legends and Methods. It came with Supplementary Material 1, the legends of Supplementary Figs. 1 to 3. I couldn't open the supplementary PDF as images (no renderer installed), and the main figures weren't available. So significance marks that appear only inside figures were not read. Supplementary Materials 2 to 8, likely the source data, were not supplied.

**Code read:** github.com/xzhang03/Photometry_analysis at commit b88d3943. It is the lab's general MATLAB preprocessing toolbox and contains none of this paper's Python statistics. The one detail it settles is the per-mouse Z-score: `tcpZ.m` computes one SD per mouse over all that mouse's recordings, joined end to end.

**Claims:** 37 findings, all with quotes. 14 claims carry statistics: 14 p-values, with tests in the paper's own words. 37 claims carry criteria, and 16 have expected values with tolerances. Where the paper gives mean ± s.e.m., the s.e.m. is the tolerance; otherwise it is 10%.

**Details the paper leaves open, and the readings named for each:**
- **Response window:** 1–10 s (Methods), 1–9 s (Fig. 2–3 legends), or 0–10 s (Results, Fig. 1).
- **How the Z-score is applied to each trial:** (F − F0) divided by the code's per-mouse SD, or dF/F0 divided by the SD of the mouse's dF/F0 over all its trials.
- **ΔZ-score:** last 5 minus first 5 triggered trials (Methods), or last 15 minus first 15 (legends and the early/late definition used elsewhere).
- **Which sessions count:** at least 15, at least 30, or all triggered-trial sessions (Fig. 2b, Fig. 3k and the correlations).
- **Ensure volume:** the recorded total, or triggered trials × ~50 µL.
- **Supp. Fig. 1d licking measure:** baseline subtracted or divided out; AUC over 1–10 s or the whole post-cue trace; paired or unpaired t-test (the legend and Methods disagree).
- **Fig. 2e lick vigour:** two readings of "throughout", and two of where the decline starts.
- **Fig. 2f–j "initial" lick rate:** the first triggered trial, or the mean of the first 15.
- **Rolling-SD window (Supp. Fig. 2j):** 1, 10 or 60 s.
- **Fasting comparison (Supp. Fig. 2l–p):** no test named; readings are a t-test or a mixed-effects model.
- **Within-group test for Fig. 3i:** the mixed-effects model or the paired t-test of Supp. Fig. 3i.
- **Weight change (Supp. Fig. 3m, q):** as a difference or a ratio, measured from the maximum ad libitum weight, the weight before HFD, or the start of ad libitum feeding.
- **Fig. 1c, ~30% heavier:** which body weights are averaged, and how.
- **Recording-day choice:** where meal-size groups or sessions are ambiguous, both sets are run.

**Where the paper contradicts itself (recorded in the file):**
- **Supp. Fig. 2h:** the sentence calls the NCD correlation positive and the HFD one negative, but the printed values are r = −0.34 and r = 0.26.
- **Fig. 3 counts:** the Results and the legends give different numbers of recordings.
- **Fig. 2f–s:** the meal-size groups add up to 57 NCD and 53 HFD recordings, not 59 and 54.
- **Mixed-effects model:** the Methods place it on "Fig. 1 i", while the legend places it on Fig. 1k.
- **Panel letters:** the text cites Supp. Fig. 3m and 3q for analyses the legends assign to other panels.

**What claims needed and the paper lacks:**
- p-values for Fig. 1l, Fig. 2c–d, 3h and the Supp. Fig. 1–3 tests appear only as figure asterisks, which I couldn't read. Where the text says "significant", the paper's alpha of 0.05 is recorded instead.
- The paper names no test for several claims of "no effect" or "comparable": fasting, locomotion against meal size, and absolute weight against meal length (Supp. Fig. 3l). The readings named for each are recorded as deviations.
- The paper's own analysis code isn't public.
