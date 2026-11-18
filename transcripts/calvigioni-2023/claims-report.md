I wrote `claims/000473/10.1038-s41593-023-01367-8.yaml`. The quote checker matches all 31 quotes word for word. It still exits non-zero because it cannot find two p-values in the text, and I checked both by reading: P = 6.20 × 10⁻⁹ is printed in the Fig. 3f legend, and p = 0.045 is in Supplementary Table 6, which exists only as an image.

**Text read:** the version of record (open access), with Methods, figure legends and Extended Data legends. I also read the Supplementary Information PDF: the Supplementary Methods and Supplementary Tables 1 to 10. Tables 4 to 10 are images, so I rendered and read those pages. I read the paper's code, `PierreLeMerre/Esr1_NPX_code` at commit 85187f3. The dandiset's archive description matches the Neuropixels experiment in Fig. 4 and Extended Data Figs. 7 to 9.

**Claims:** 33 in total: 1 link claim and 32 findings.
- 31 have quotes; 2 are marked `inferred` (the control pupil result and the tuned-unit counts, both read from the supplementary tables).
- 21 claims record 37 statistical values.
- 22 claims have expected values, and 25 have criteria.
- 21 are about the Neuropixels data. The other 12 cover findings this dataset cannot test: patch-clamp, Patch-seq, anatomy, behavior and stress. The Patch-seq marker claim is marked as held in BioStudies S-BSST1069.

**What the code shows:** its saved model outputs list 1,937 fitted units. Three groups match the paper exactly (Ctl 482, Vglut2 738, Npy 406), but Esr1 has 311 where the paper says 319, and four sessions have no fitted units. The link claim checks the dataset's sessions and units against these outputs.

**Details the paper leaves open, and the readings named:**
- **Which units the model was fitted on:** the code keeps units with mean count per 100 ms bin above 0.2 (about 2 Hz), but its comment says 0.2 Hz; both are named. The Methods do not mention this rule.
- **Pupil value per trial:** the whole trial, or the interval in the NWB trials table. The z-scoring uses either all block-1 frames or the block-1 trial values.
- **Eye-closing events:** the paper never defines an event; thresholds of 50% and 75% of the eye area are named. The unit of observation is also unclear, since an exact signed-rank test on 5 mice cannot give p below 0.0625; per mouse and per trial are both named.
- **Mean tuning score (Supplementary Table 6):** averaged over all fitted units or only the significantly tuned ones.
- **Conditioned units:** how the change over trials is tested; two readings are named.
- **"Task-modulated" units for the activity modes:** tuned units, all fitted units, or all units.
- **Unit count after cluster quality control:** 1,770 in the Results, 1,788 in the Methods; either is accepted.
- **Decoding comparison:** at the largest common unit count, or averaged over unit counts.
- **Latency detection:** thresholds of 3 or 2 baseline standard deviations.

**Choices I made because the paper gives no measure or test:** I flagged these in the criteria as my choices, not the paper's. They cover:
- the tests for the genotype differences in opto-modulation and for the comodulated units against chance;
- the 20 ms bound for "similar" latency;
- a distance measure for the PCA trajectories, which the paper judged by eye;
- the decision rules for decoding, and for decoding showing no difference in the other subregions.

Where the Methods and the code disagree, I followed the Methods and named the code as a variant: primary tuning (absolute versus signed maximum), the baseline test (signed-rank versus rank-sum), the activity-mode windows, and the smoothing kernel.

**Missing from the paper:** nothing a claim depends on. The source data files and the intermediate pupil and eye CSVs that the code reads are not available, so those values must be recomputed from the dataset. The paper does not define an eye-closing event, which may leave that claim to be blocked as underspecified.
