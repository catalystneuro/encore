I wrote `claims/garud-2026.yaml`. The quote checker passes with 0 problems: every quote is word for word and every p-value was found in the text.

**What I read:** the bioRxiv preprint posted April 8, 2026, from the extracted text in `paper/`: main text, figure legends, the Table 1 legend and Methods. There was no PDF, so I didn't look at any figures.

**What was missing:**
- **The supplement.** The paper relies on it for the derivation (S1), the phasic walkthrough (Fig S1), the Brown et al. analysis (Fig S2) and "further detailed methods". I went ahead because the main Methods describe the Figure 4 analysis on DANDI:001552 in enough detail to test. Other claims files in the repo did the same when a supplement was missing. The Fig S2 claim can't be judged without the supplement, so its criterion marks it blocked.
- **The code.** It is on OSF at https://osf.io/g3e2d/, but that project is private: the OSF API answered 401 (authentication required). No method detail is settled by code.

**Counts:** 18 claims, all with quotes. 4 have statistics, 10 have expected values and all 18 have criteria.
- 5 claims are on DANDI:001552 (Figure 4): mice and session counts, lick rate short vs long ITI, the long-ITI dip below baseline, the dip deepening with training (r = -0.29), and lick rate rising with training (r = 0.65).
- 12 are on the Krausz rat data (Figures 2, 3 and 5), held on Mendeley at doi:10.17632/m59zdjpm9h.1, so they are marked as data held elsewhere.
- 1 is on the Brown et al. data (Fig S2). The text read doesn't say where those data are held.

**Details the paper leaves open, with the readings I named:**
- **ΔF/F correction:** a fit of the 405 nm signal to the 470 nm signal, with ΔF/F = (470 − fit)/fit; or ΔF/F of each channel, then the fitted control subtracted. No filtering is named.
- **ITI duration and midpoint:** measured from reward to the next cue, or from cue to cue.
- **"Observation" in the rule that drops 1-s bins with fewer than 20:** a trial or a sample.
- **Baseline:** read as ΔF/F of zero. No test is named for Fig 4B, so I used the paper's one-sample, one-tailed t-test from its rat analysis.
- **Session number:** among all of a mouse's sessions, or among its long-ITI sessions only.
- **The r values printed beside the mixed-effects models:** Pearson r over pooled values, or after removing each subject's mean.
- **Sessions in the Fig 4C lick trend:** long-ITI only, or all sessions.
- **Lick comparison (Fig 4A):** each mouse's rate per condition as a mean of session means or over pooled trials. The test is taken as two-tailed.
- **Krausz claims:**
  - Fig 2A–E name no tests, so I built criteria from the tests the paper does name.
  - Fig 2F has df = 18 (20 points), which matches neither the 49 positions nor the 10 rats. I named three readings.
  - Fig 2G–H: approach observations only (per the Methods) or approach and non-approach (per the legend).
  - Fig 3: the forms of the four profiles aren't given, nor is the axis the gradient is integrated along.
  - BIC is read as n ln(SSE/n) + k ln n.
  - Fig 5D: three readings of how each factor's ΔBIC is formed.

**Inconsistencies in the paper, noted in the file:**
- The ITIs are given as about 8 and 55 s in the Results but about 15 and 45 s in the Methods.
- The Fig 4C p-value is printed garbled as "p=so this 1e-4". I read it as 1e-4.
- The reward cutoffs are "> 80" and "< 20" µL in the legend but inclusive in the Methods. I followed the Methods.
- The Fig 2C legend says ramps show a "modest reduction" from early to late sessions, while the Results say they "look similar".
