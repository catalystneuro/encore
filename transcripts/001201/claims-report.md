I stopped without writing any claims. The paper's supplement is missing, and the main text sends its analysis methods there. `claims/001201/` has not been created.

**What was read:** `paper/10.52202-085713-4642.txt`, the version of record from the NeurIPS 2025 proceedings PDF (Curran Associates). It has 23 pages: the main text (sections 1 to 5 with Figures 1 to 5), the references and the NeurIPS checklist. No supplement file is under `paper/`, and the text was extracted from that same PDF, so the PDF ends at the same place.

**What is missing:** the paper's Supplemental Materials, meaning Appendices A, B and C and Figures S1 to S5. The main text points to them for every analysis:
- **Section 4:** "Please refer to Appendix C for detailed descriptions of the methods used in these analyses."
- **Appendix C.1, decoders (Figures 4 and 5):** how the ridge regression and LSTM decoders were trained, including the regularisation, the architecture and the hyperparameters, and the setup for the cross-day, multi-session and fine-tuning runs, including the double-exponential fit.
- **Appendix C.2, tuning (Figure 3):** how the per-channel tuning regressions, tuning angle and strength, and circular median and IQR were computed.
- **Appendix C.3, neural activity over time (Figure 2):** the linear models for the SBP and PR trends, how participation ratio was computed, the PCA and per-quarter centroids, and the trial alignment by maximum jerk.
- **Appendices A and B:** task and implant details and the data selection steps. The NeurIPS checklist itself says training and test details are "mostly specified in the Supplemental materials."
- **Figures S1 to S5:** cited for the channel maps, the per-day TCR (S3), and the SBP split by bank and by active/inactive channels (S4 and S5).

Without these, most criteria would rest on choices the paper makes only in the appendices. The protocol says to stop in that case.

**To continue:** someone needs to add the NeurIPS 2025 supplemental PDF for doi:10.52202/085713-4642, holding Appendices A to C and Figures S1 to S5, to `paper/`, then rerun the reader. I did not read the linked code (github.com/chesteklab/LINK_dataset) or open the dataset, since no claims were being written.

**Counts:** 0 claims, 0 quotes, 0 statistics, 0 criteria. No method details were named as open, because no criteria were written.
