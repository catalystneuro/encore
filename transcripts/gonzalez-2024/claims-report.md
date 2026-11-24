I wrote `claims/gonzalez-2024.yaml` with 28 claims. The quote checker reports one problem, which I left as is: the Figure 3g p-value. The text prints it as "p = 3.61 − 10", with the "e" lost in extraction, so the checker can't find "3.61e-10". I read the passage and kept the value, with a comment beside it.

**Text read.** The Europe PMC full text (PMC10942598) of the eLife reviewed preprint, as revised and published 16 Feb 2024. It has the main text, Methods, every figure and figure-supplement legend, the assessment and the public reviews. The only supplement file is the MDAR checklist, which has no results. Nothing the results rest on is missing, and I did not open the PDF.

**Code read.** github.com/alexgonzl/TMA at commit 6f93593, the version the paper archives. The current head differs only in the README. Its `paper_stats.py` holds the exact mixed-model and likelihood-ratio specifications; the `metadata/` tables hold per-session performance and the paper's unit matches with their open-field clusters.

**Claims.**
- **Quotes:** all 28 have one, and all are found word for word.
- **Statistics:** 18 claims carry them, 42 values in all.
- **Expected values:** 13 claims.
- **Criteria:** all 28 have one.
- **Data:** two claims (Figure 7g and 7h) use the repo's cluster labels (`with_labels`). The rest use the dataset.
- **Coverage:**
  - behaviour (performance, switch trials, training);
  - cue and reward error coding and remapping;
  - remapping against behaviour, at unit, session, population and subject level, plus the control analyses;
  - the rate- against global-remapping encoders;
  - the position and decision decoders;
  - the supplement analyses of overlap and persistence;
  - open-field models, unit matching, clusters, and the head-direction cluster remapping more.

**Details the paper leaves open, with the readings named:**
- **Unit set:** isolated units only (Figure 2—figure supplement 6 says that is what Figure 2 used), or isolated units plus MUA (the code's default).
- **"Across subject median" accuracy:** pooled over sessions, or the median of the subjects' medians.
- **Reward null balancing:** the Methods and the code balance the null by cue; the Results text says it was balanced by reward. Cue balancing is the main reading and reward is the variant.
- **Encoder folds:** 5 in the Methods, 10 in the code. The Methods are followed and 10 is the variant.
- **Encoder model comparison:** the LMEM on per-unit Mann-Whitney z of test R², or the LMEM on R² itself.
- **Performance scale:** the code logit-transforms it in the LMEM and the Methods don't say. The slope is judged on the logit scale, with the raw fraction as a variant.
- **Decoder unit groupings:** read as at most 8, 9 to 19, and at least 20 units, from the text and the 2 degrees of freedom.
- **"Above chance" decoding:** balanced accuracy above 0.5, or above a shuffle null. The zone it is counted in is also open: the stem or the last zone.
- **Training criterion:** 70% in the Results, 75% in the Methods.
- **Correct/incorrect coding threshold (Figure 4—figure supplement 6):** sign only, or |U_Z| > 1.96.
- **Open-field cross-validation blocks:** 20 s in the Methods, 30 s in the code's call. The Methods are followed.
- **Unit matching:** UMAP parameters are not given, so the paper's own matches in `unit_table.csv` are shown alongside.

Where the paper reports no test, I fixed one and said so in the criterion: switch-trial "similar" is judged as within 10 percentage points, and the cue-to-reward remapping correlation uses Kendall.

**Missing from the paper.** No claim lacked a needed passage. Three claims rest on data the dandiset may not hold:
- the pre-surgery training sessions (training-to-criterion claim);
- spike waveforms, needed to redo the unit matching;
- the paper's cluster labels, which come from the GitHub metadata, not the paper itself.
