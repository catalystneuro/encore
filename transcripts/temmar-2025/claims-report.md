I stopped without writing any claims, because the supplement is missing. `claims/temmar-2025.yaml` has not been created and nothing was changed.

**Text read:** the version of record, the NeurIPS 2025 Datasets and Benchmarks proceedings PDF from Curran Associates (`paper/10.52202-085713-4642.txt`). It has 23 pages: main text pp. 1–10, references pp. 11–16, NeurIPS checklist pp. 17–23. That covers the abstract, Introduction, Related Work, Section 3 (the dataset), Section 4 (Analyses), Section 5 (Limitations and Discussion) and the figure legends for Figs 1–5. Each figure has a legend, but nothing beyond it.

**Missing:** the supplement (the paper calls it "Supplemental materials" or "Supplementary Materials"), with Appendices A, B and C and Figures S1 to S5. The text is all 23 pages and ends with the checklist, so the supplement is not in it. Every analysis result depends on it:
- **Appendix C.1, decoder training.** It fixes how the ridge penalty is chosen, the LSTM architecture and training, how the 300/75 trial split is formed, and how R² is computed and averaged across DOFs. Figs 4 and 5 rest on this: same-day R², decay across days, multi-session training with its double-exponential fit, and fine-tuning.
- **Appendix C.2, preferred tuning.** It sets the regression form, the angle and strength decomposition, and the circular median and circular IQR (Fig 3).
- **Appendix C.3, neural activity over time.** It covers the SBP trend model, the active-channel rule, participation ratio, the PCA centroids and the max-jerk alignment (Fig 2).
- **Appendices A and B.** These give task and implant details and the curation stages.
- **Figures S1 and S3 to S5.** Section 4.1 bases the per-bank and active/inactive SBP findings on Figs S4 and S5. Fig S3 shows low-strength channels having low TCR.

The main text gives only sketches of these methods. The protocol requires every part of a criterion's method to come from the Methods, the supplement or the code, so the claims can't be written faithfully from the main text alone. I didn't read the linked code (github.com/chesteklab/LINK_dataset), because the missing supplement already blocks the claims and the code doesn't replace it.

**To supply:** the NeurIPS 2025 supplementary PDF for this paper (Appendices A to C and Figs S1 to S5), put under `paper/`. The OpenReview or NeurIPS proceedings supplement, or an arXiv version that includes the appendices, would do.

**Counts:** 0 claims, 0 quotes, 0 statistics, 0 criteria. No open details were recorded, since no criteria were written.
