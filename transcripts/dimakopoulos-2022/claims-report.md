I wrote `claims/openneuro-ds004752/10.7554-elife.78677.yaml`. The quote checker reports 21 claims, 20 quotes, 18 statistical values and 0 problems.

**Text read:** the version of record from Europe PMC (PMC9374435): main text, figure legends, Table 1 and Methods. Of the supplement, the text gives only descriptions: Supplementary file 1 (electrode coordinates) and the legends of the two figure supplements are absent. No claim rests on them.

**Code read:** `vdimakopoulos/verbal_working_memory` at commit 395ae13. It settles the 40 Hz downsampling, the trial selection (correct trials, set sizes 6 and 8, artifact-free), the time windows, the Granger settings, the min/max reduction for each participant, the group statistic, and how Cowan's K and the response-time slope are computed. The calls for the paired permutation test and for the Kruskal-Wallis and Dunn's tests are not in the repository.

**Claims:**
- 21 in all: 20 with quotes, and one, `table1-heschl-dgranger-correct`, marked `inferred` because its per-participant values appear only in Table 1.
- 17 carry statistics and all 21 have criteria.
- They cover behaviour (cohort, accuracy, Cowan's K, response time), ECoG in Participants 1 to 4 (power, phase locking, Granger reversal, spatial spread, no effect in Participant 4), and the EEG-source results across all 15 participants (left-hemisphere sources, group Granger, the left temporal scalp electrodes with and without a Laplacian, auditory cortex strongest, reversal in every participant, Table 1 values, no reversal in prefrontal cortex or on incorrect trials, the balanced 10% subset).

**Details the paper leaves open, with the readings named:**
- **Hippocampal channel:** the most distal contact, a bipolar pair as in the code, or the mean over contacts.
- **Auditory cortex source:** the dataset's AC sensor, Heschl gyrus, or superior temporal gyrus.
- **Theta ΔGranger per participant:** the mean over 4 to 8 Hz (Results) or the extreme value (legend "maximal", and the code).
- **Trials for each participant's value:** all correct trials, or 10% of them redrawn 200 times, taking the mean (Methods) or the median (Results).
- **Taper:** Hann (Methods). The code's dpss is run as a variant.
- **Group value:** mean or median, and whether the three ECoG values are pooled in, as the figure code does.
- **Behaviour:** whether averages are over trials, sessions or participants; mean or median response time; which trials make up the 3045.
- **Power analysis:** how the window "toward the end" of maintenance is read, and whether ">100%" is the band average or its peak.
- **Phase locking:** the comparison period, fixation (legend) or encoding (Results).
- **Spatial test:** how "exceeds the 95th percentile" is judged.
- **Scalp result:** which left temporal electrodes, and which Laplacian.
- **Areas in Figure 4b and 4c:** which areas enter the Kruskal-Wallis test.
- **Group test variant:** dependent against independent samples t.

**Missing or inconsistent in the paper:**
- **Participant numbers:** the paper never maps them to subjects; only Table 1's pathology and the ECoG participants can match them to the dataset.
- **p-values below what the test resolves:** p = 4.1e-10 and p < 0.0005 are below what 200 permutations, or exact sign flips over 15 pairs, can give. These claims are judged at 0.05 and the smallest attainable p is reported.
- **Head model:** it is not named, so the left-hemisphere source claim needs outside data (`with_inputs`).
- **ECoG:** the dataset description mentions only depth iEEG, so the ECoG claims may not be testable on this dataset.
