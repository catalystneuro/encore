I wrote no claims. The paper's text is here, but the supplement that its statistical results rest on is missing, so under the Reader section, step 1, I stopped.

**Text read:** `paper/10.1101-2023.04.19.537568.txt`, the bioRxiv preprint (version 1, from the JATS XML). It has the main text, the Methods, the figure legends and the figure supplement legends. There is no PDF and no supplement file (`papers/manifest.yaml` lists `supplements: 0`).

**What is missing:**
1. **Supplementary Tables S1 to S18.** The paper puts the statistical results of almost every finding in these tables. The text and legends only point to them ("Table S3 for statistical details", and so on). Examples:
   - Fig. 2b stride-velocity t-tests (S2).
   - Slomo, shuffle and fast signature F-tests (S3, S8, S12).
   - EMG tests (S4, S10, S13) and the Z-score correlations (S5).
   - Laterality tests (S7, S11) and motor tests (S6, S9, S14).
   - Bouton counts and sensory tests (S15 to S17) and optogenetics (S18).
   - Dose and time titration (S1).

   Without them, no claim could have the paper's statistics or reported values, beyond a few numbers in the text (such as p 0.016 for lamina III boutons).
2. **The Z-score equation in the Methods** (section "a) Group definition"). The text breaks off at "Z-scores of the change in gait metrics were then calculated as follows:" and the equation is gone, probably an image that the XML extraction dropped. Every subgroup in the paper (slomo, shuffle, fast, and their opposites) is defined by Z_SwT or Z_StrV thresholds, so no criterion could fix how mice are grouped.
3. **Figure 7-Figure supplement 3:** the legend is cut off after its title.

**To proceed:** someone needs to add the bioRxiv supplementary file with Tables S1 to S18, and the preprint PDF so the Z-score equation can be read. A reader run can then write the claims. Because I stopped, I did not read the linked code (the two SourceForge projects, gait-analysis-gui and gait-emg-step-trigger).

**Counts:** 0 claims, so 0 with quotes, statistics or criteria. No open details or readings were recorded. Nothing was written under `claims/002010/`.
