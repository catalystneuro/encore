I've revised the attempt for every point in the round-1 report and re-run the entry. `tools/entry.py all` reports 0 errors and the notebook passes (70 s). Nothing is committed.

**Outcomes changed (all three now match what the verifier gave):**
- **fig2g-attack-willingness: not_reproduced → reproduced.** The main test now uses the group counts from the workspace's Figure 2G table, which match the paper (29 of 46, 8 of 36, 8 of 22). The model depends only on these counts, so refitting on them is exact. It gives the paper's model: pH 2.734 (p = 0.042), time p = 0.246, residual deviance 127.58, ROC area 0.699. The per-squid file, which is missing 11 chronic-OA squid, is now the variant and stays a data finding.
- **sfig3-prey-velocity-unchanged: reproduced → partially_reproduced.** The CO2 10–20 min column is a copy of the control column, so only part of the claim can be tested. That part holds: pH at 0–10 min p = 0.64, and control shrimp across the two times p = 0.36. The CO2 group's time effect and the interaction cannot be tested. The two-way ANOVA on the deposited table is now printed for reference only.
- **rnaseq-assembly: reproduced → partially_reproduced.** The mapping rate is not deposited, so not every value can be checked. The notes now also say the 475.5 bp N50 covers only the 610,324 transcripts with any expression, not all 902,413.

**Bug fixed (verifier's point 11):** in reading (b) of fig4a-pca, the batch factor is stored as text but was compared with a number, so no batch was removed. Corrected, reading (b) gives PC1 31.7% and PC2 16.6%, just outside the PC2 tolerance, and chronic-OA is not separated on PC2. fig4a-pca stays partially reproduced. The notebook and record now say plainly that this outcome depends on reading "spread" as the range of the control samples, and that it would be reproduced if spread meant their SD. Distances for sfig5b under reading (b) are now 477.1 against 532.8, the same order as before.

**Outputs and corrections added:**
- **Workspace contents:** every object in `Squid.RData` and the README inside the zip are now printed. None holds body mass, mantle length, seawater chemistry, tracks or ERG traces, which confirms the four blocked claims.
- **Left-out acute-OA squid:** the workspace's figure tables line up per squid. They show that the squid left out to match the paper is the one missing from the distance and velocity files, which backs up the sums-of-squares match.
- **Transcriptomic claims:** the notebook, summary, README and record now say these outcomes show agreement with the authors' saved results, not an independent recomputation. A new cell confirms the saved DESeq2 fits use the deposited counts, with size factors recomputed here matching the stored ones (difference about 1e-15).
- **fig3c-ratio-declines:** the SDs and the implied peak frequencies in FFT bins are now printed. The notebook explains why control and acute-OA are identical up to 45 Hz (every squid's peak fell in the same bin). The deposit gives no n per mean.
- **PCO2:** the finding now says the formula's tenfold PCO2 is the one consistent with the measured TCO2 and pH. Bicarbonate means recomputed with it stay within tolerance.
- **New finding 13 (paper_inconsistency):** the paper's own Welch line for blood pH (W = 5.983 on 2 and 9.196 df) gives p = 0.022, not the printed 0.00965.
- **Outside data:** the introduction no longer says none is used; it names the NCBI TSA record.

The round is recorded under `verifications` with all 31 claims. Three new questions for a reader are in `questions/allen-2026.yaml`: the FFT rounding in fig3c, the undefined "spread" in fig4a, and the "anion"/"transition metal ion" keyword matches in optic-lobe-no-ion-regulation. No claim was changed.

**Not done:** DESeq2 and GSEA were not re-run, because R, clusterProfiler and the authors' GO annotation database are not in this environment. The mapping rate and the N50 of the whole assembly still can't be checked, since there is no alignment log or assembly FASTA in the deposit. `tools/build_site.py` and `tools/site_assets/list.js` were already modified before this run, and I left them alone.
