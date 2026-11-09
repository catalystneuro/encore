I made five corrections to `claims/johnson-2017.yaml`, added the checks entry, and marked the file ready for an attempt. Nothing is committed.

**Checker result:** `claims/johnson-2017.yaml: 22 claims, 21 quotes, 33 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND patients-above-chance 5e-10`. The value is correct; the text extraction garbled the exponent in "one-tailed p < 5 3 10�10" (Results, Behavior, paragraph 2), so the checker can't match it.

**Changes, by claim:**
- **patients-above-chance:** the criterion asked for t above 13.89 (the paper's 15.43 less 10%) and also p < 5 x 10^-10. But t = 13.89 with 13 df gives p = 1.8 x 10^-9, so the p requirement cancelled the tolerance. The p is now reported, not required. The paper's bound is simply the p of t = 15.43, which is 4.9 x 10^-10.
- **accuracy-patients-impaired:** the criterion now explains why p < 7 x 10^-5 belongs to the group-only model, though the Results sentence places it after the full model. Table S3 gives the full model's group effect p = 0.03, its legend ties the bound to the re-run models, and F(1,202) = 16.77 gives p = 6.1 x 10^-5.
- **erp-lesioned-maintenance:** "reversed polarity" now has a clear test: a cluster in which the patients' mean ERP has the opposite sign to the controls'.
- **psi-deltatheta-group-clusters:** the sign of each cluster is now reported. The next sentence of the paper says controls showed greater PFC leads than patients, and the claim had given no direction.
- **psi-network-degree:** added a third reading of network degree: the sum of |Z| over true connections in either direction. The Methods say "between each channel and all other channels", not outgoing only. The paper prints the cluster p as at most 0.01; the schema has no "<=", so it stays "<" with a note.

Everything else matches the paper, including the cohort figures, Tables S1 to S3, the channel lists, the time windows, the Z bounds and every p-value. Every main finding has a claim, and no claim comes from outside the paper.

**Still open:**
- **PFC channels for the PSI analysis (O6):** they are only shown in Figure 2, and I couldn't render the PDF here (neither poppler nor PyMuPDF is installed). The claims file's two readings stand.
- **accuracy-no-hemifield-condition-effect:** it is judged on the third model in Table S3. The Results sentence could also mean the full model, where the hemifield by condition interaction has p = 0.03. That model is shown as a variant.
- **Analysis code:** the paper's analysis scripts are deposited with the dataset, so they weren't read here. They may settle the open details O1 to O5 and how network degree is defined; the author should record what they find.
