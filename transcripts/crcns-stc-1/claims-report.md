I wrote no claims, because the paper's supplement is missing.

**What was read:** the version of record of Gu et al. 2011, *Neuron* 71:750–761 (`paper/10.1016-j.neuron.2011.06.015.txt`, 12 pages, matching the 12-page PDF). It has the main text, the main Experimental Procedures and the figure legends for Figures 1–8. I also read the CRCNS stc-1 data descriptor, only to see what the dataset holds: MSTd and VIP; its experiment 3 has 127 MSTd pairs with signal and noise correlations.

**What is missing:** the Supplemental Information. The paper says it "includes Experimental Procedures and eight figures". The protocol's Reader step 1 says to stop when a supplement the results rest on is absent, and several results here rest on it:
- **Pair selection:** the 127 pairs analysed are chosen by distance under 1 mm, which is justified by Figure S1.
- **Findings shown only in supplementary figures:**
  - the trained-versus-naive difference shrinking over time (R = −0.9), Figure S2A, and that it held in each animal, Figure S2B
  - congruency, Figure S5
  - fixation against discrimination task (p = 0.3), Figure S6
  - renormalization (p > 0.3, ANCOVA p = 0.7 / 0.9), Figure S8
  - fixation accuracy and microsaccades, Figures S8A and S8B
- **Methods that are probably in the Supplemental Experimental Procedures**, since the main Methods do not describe them:
  - the per-neuron Fisher-information thresholds (Figures 4C, 4D, 4G, 4H and S4)
  - choice probability (Figure 8)
  - the pair thresholds of Figure 7B
  - microsaccade detection
  - which monkeys were naive and which trained. Criteria for the trained-versus-naive claims need this to split the dataset's pairs, and the main text gives only the counts: 3 naive and 5 trained, 38 and 89 pairs.

**Code:** the paper links none, so there was nothing to read.

**Counts:** 0 claims, 0 quotes, 0 statistics, 0 criteria. Nothing was written under `claims/crcns-stc-1/`, so no quote check was run.

**To go ahead:** add the Supplemental Information (Supplemental Experimental Procedures and Figures S1–S8, from doi:10.1016/j.neuron.2011.06.015) under `paper/` and run the reader again.
