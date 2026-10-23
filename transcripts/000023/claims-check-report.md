The claims file is ready for an attempt. I changed 11 claims; nothing is committed.

**Checker result:** `33 claims, 32 quotes, 12 statistical values, 2 problems`. Both problems are in fig6e-deep-de-genes (p = 3.5e-06 and 5.3e-05). The values are correct; the text extraction prints them as "3.5 10 −6" and "5.3 10 −5", so the checker can't match them. Every quote matches word for word.

**The paper's code.** I read it at commit 3daf9f0 (AllenInstitute/patchseq_human_L23). It confirms what the criteria cite: the statistical tests and corrections, the deep FREM3 cut at depth above 0.575, the pathology test and its grouping, the classifier settings, and dropping cells with missing features. One difference: the code runs 10 classifier splits where the Methods say 1000. The criterion follows the Methods.

**Changes, by claim:**
- **Thresholds removed from `statistics`** (in each case "FDR below 0.05" only decides which features or genes are counted, so it is a method, not a result):
  - edtable1-species-ephys
  - fig5c-frem3-ephys-depth (first entry only; the FDR below 1e-7 for the three regressions in Figure 5c stays)
  - fig5b-frem3-morph-depth
  - fig5d-frem3-gene-depth
  - fig6-deep-ephys-anova (its cell counts and the counting rule moved into the criterion)
- **Method readings must now agree.** These criteria passed if any one reading matched; now the outcome must be the same under every reading, and the claim is blocked as `methods_underspecified` when they differ:
  - edtable1-species-ephys: Student's or Welch's t-test.
  - fig6c-carm1p1-upstroke-rin: upstroke rate or upstroke/downstroke ratio.
  - fig3d-depth-by-type: 90% or 80% for "almost entirely".
  - fig2ef-pathology-ephys: difference of medians or of means for the 5 mV.
- **Statements that left out part of the quoted finding:**
  - fig4-glp2r-sag: added "higher input resistance". It is not judged, because the paper doesn't say what it is higher than.
  - fig1g-deep-types-de-genes: added that the homologous types are similarly distinct from one another in both species.
- **fig6c-col22a1-rin-fi-sag:** the criterion now says that the f-I gain, like sag, is shown only in Figure 6b with no test, and that the Methods' pairwise test is used for both.
- **edfig6-classifier-human-ephys:** noted the 10 against 1000 splits.

**Still open:**
- **Pathology test:** the paper names no test for the pathology comparison (fig2ef), so that criterion relies on the code. The code's cell table for it (`human_distillery_selection_new.csv`) is not in the repository.
- **Findings without a claim:** a few smaller, figure-only findings have none:
  - Fig. 1d-e UMAP compactness
  - the mouse depth order in Fig. 3d
  - Extended Data Fig. 2 and Extended Data Fig. 5

  The main findings are all covered, and every claim comes from this paper.
