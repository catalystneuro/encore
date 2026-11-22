I wrote no claims file. The only claim DANDI:001075 could test rests on methods that are in neither the paper nor any code, so under the protocol's Reader step 1 I stopped. `claims/seneque-2026.yaml` does not exist and nothing in the working tree changed.

**Text read:** I read the whole of `paper/10.48550-arxiv.2606.12923.txt`: arXiv preprint v2 (12 June 2026), the main text plus Appendices A to D. There is no PDF in `paper/`. The arXiv page shows v1 and v2, no ancillary files and no code repository, and the paper links no code.

**What the dataset can test:** DANDI:001075 is the Randi et al. C. elegans signal propagation atlas (reference [64]). The paper reuses it for one result, the worm "neural perturbation-propagation" operator:
- 315 event-receiver rows and 67 NeuroPAL labels.
- Held-out weighted sign accuracy of 0.596825 over 68 receiver/operator groups.
- Wilson 95% CI 0.541803 to 0.649515, and p = 6.988 x 10^-4 against a 50% sign null (Appendix B.1, Table 1).

The body text (Section 3) conflicts with this. It calls the result "68 held-out receiver/operator rows", where Appendix B.1 has 315 eval rows in 68 groups.

**What is missing for that claim:** Nothing in the paper defines the method. Appendix A.6 only lists generic denominator parts (perturbation family, receiver variables, event window, held-out split, validation test). It does not say:
- what an "event-receiver row" is (which stimulation events, which receiving neurons, which response window);
- what sign is predicted, and from what predictor or model;
- how the 68 held-out groups are formed;
- how the accuracy is weighted.

Appendix D.1 says the implementation details, analysis labels and figure source data "remain in supplementary materials". Those are not under `paper/` and not on arXiv. The predecessor ATLAS paper (arXiv 2604.17663, ref [3]), which supplies the "intervention and geometry pipeline", may describe the method, but it is a different paper and I did not use it.

If I wrote a criterion now, I would be making up every part of the method, which the protocol forbids. Since the method is missing entirely, not left partly open, I have no "open details with named readings" to report.

**Rest of the paper:** The other findings (mouse ALM, zebrafish, and all the LLM and adapter panels) use data outside this dataset. They report tables of numbers with no recoverable methods, and their source artifacts are internal (T-numbered rows) and unpublished.

**Needed before claims can be written:** the authors' supplementary materials or analysis code for the C. elegans panel (the T2541 to T2600 biological rows), or the methods document for it.
