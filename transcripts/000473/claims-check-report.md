I made the corrections and added the `checks` entry. I think the file is ready for an attempt and set `ready: true`. Nothing was committed.

**Checker result:** `claims/000473/10.1038-s41593-023-01367-8.yaml: 33 claims, 31 quotes, 37 statistical values, 2 problems`. Neither problem is a real error. Both values are in the paper, but the checker cannot match them: 6.20 × 10⁻⁹ is in the Fig. 3f legend, and 0.045 is in Supplementary Table 6, which is an image.

**Changes, by claim**
- **ed1j-optotagged-tonic:** The criterion said the paper never defines how a unit counts as optotagged. The Methods do define it: responses in more than 10% of trials in the 10 ms bin after the pulse, the spike latency test at α 0.01, and a waveform correlation of r > 0.9. The criterion now uses that rule. How "tonic" was judged is not stated, so the rule used here is marked as a choice.
- **ed7g-eye-closing-airpuff:** The per-trial reading was made up. The paper's code (`Extended_Data_Fig7g_boxplots.jl`) and the figure both use one event count per mouse, so I removed that reading. The event thresholds are now marked as choices. The 10-mouse Esr1 group is judged by the paper's test. The three 5-mouse groups are judged by whether every mouse moves the same way (a choice), with the code's own calculation shown as a variant.
- **fig4f-pupil-persistent, fig4g-opto-tuning-score:** Tolerances were 10% with no reason given. They are now the s.d. that Supplementary Tables 5 and 6 print next to each mean, as the protocol requires.
- **ed9bg-state-clusters:** The rule could never find a state cluster, because every cluster has a most common tuning and so always got a tuning name. The Methods call the cluster names subjective. Supplementary Table 9 shows significant baseline changes in 8 of the 15 clusters, not just the 5 the paper names. The criterion now asks for at least five clusters that show the baseline change the sentence describes, and I removed the expected exact count of 5.
- **fig4jl-pl-esr1, ed8o-conditioned-units:** Thresholds and comparisons with controls that the paper does not use are now marked as choices. For ed8o, using the first 50 trials of block 2 is added as a variant.
- **fig3mn-persistent-cpa, ed10-female-mild-aversive:** Added the number of mice for each test, taken from the figure legends.

Everything else checked out against the paper, the supplementary tables and the analysis code: the other statements, quotes, p-values, unit counts, and tuned-unit counts. Every main finding has a claim.

**Still open**
- **ed1j:** The legend gives 5 mice for the 165 units but 9 mice for the 9 optotagged units. The paper does not say which is right.
- **ed7g:** An exact signed-rank test on 5 mice cannot give p-values as low as the printed 0.002 and 0.0078. They match a 10-pair test in which the code's blank padding rows were counted as data.
- **ed9bg:** No rule in the paper or the code reproduces which clusters the authors chose to call "state" clusters.
- **Choices with no basis in the paper:** Several criteria (latency, PCA distance, decoding margins, comodulation test) are judged by choices of ours. Each is named as a choice in its criterion.
