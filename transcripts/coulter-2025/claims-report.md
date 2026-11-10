I wrote `claims/coulter-2025.yaml` with 35 claims. Every quote passes the checker. Three p-values are flagged because the text prints them with a garbled minus sign (3.9e-11, 3.6e-11 and 1.3e-11, lines 302 and 526); I read them there and they are recorded correctly.

**Text read:** the version of record (Neuron 113:949–961, CC BY), with the STAR Methods and the full supplement (Figures S1 to S7 legends and Table S1). Nothing the claims need is missing from the text.

**Code read:** LorenFrankLab/hippocampus_content_neurofeedback, tag v0.0.4, commit b27655c (Zenodo 10.5281/zenodo.14522610). It contains the scripts that compute the per-session numbers, and one notebook that runs the tests from summary files on Dryad. The code fixes these details:
- the position bins of the arm ends, arm bases and box;
- the 17 cm limit to the center port and the 0.4 posterior threshold;
- how the tone-triggering bins are removed;
- the way the "2-fold" figure is normalized;
- the mixed-model formula, the two-sided Mann-Whitney test, and the regression on per-rat z-scored values;
- the speed smoothing, how bins are assigned to SWRs, and the 5–11 Hz theta band;
- the rat names and the target arm on each day.

**Where the data are:** the decoded positions are the real-time decoder's output, which the paper put on Dryad (doi:10.5061/dryad.dz08kps72), not on DANDI.
- **On the dataset (2 claims):** the reward counts (Figure 2, Figure S2D).
- **Elsewhere, on Dryad (19 claims):** Figures 1, 3, 4 and 5, Figures S1 to S5, and the reward-to-representation correlation.
- **With inputs (14 claims):** Figures 6 and 7, S6 and S7. These combine the decoder output with spikes, LFP and position from the raw recordings.

**Counts:** 35 claims; all 35 have quotes, 23 have statistics (47 values), 35 have criteria, and 17 have expected values.

**Details the paper and code leave open, with the readings named:**
- **Session quality rule:** what "running outward" means (speed above 4 cm/s, or any outward bin) and which arm is meant (the target arm, or each arm in turn).
- **Figure 3 event classes** (their code isn't in the repository):
  - whether arm-base mass is counted per bin or summed over the 90 ms window;
  - which three bins make up the 15 cm arm base;
  - whether the 1–4% counts long trajectories only, or medium and long together;
  - how the trajectory regression is done (posterior-maximum position, or posterior-weighted).
- **Figure 3C/D:** the threshold for "representing" a 5 cm bin (posterior above 0.2, above 0.4, or that bin being the maximum).
- **Figure S4A:** what counts as a "high-confidence representation" (summed over the arm end, or a single bin).
- **Reward-representation correlation:** Pearson or Spearman, and over neurofeedback sessions only or all sessions.
- **Figure 5:** the session index (the position in the full series, or among included sessions only).
- **Figure 6:**
  - assembly bins: 30 ms in the Methods, while the code's binning is labelled 10 ms (kept as a variant);
  - how an assembly is classed as target (three readings);
  - how the fold changes are taken (ratio of means, ratio of medians, or mean of per-rat ratios);
  - what "outside detection" excludes (the 30 ms window only, or also the 10 s after each reward);
  - how the mean and SD behind the high-weight cutoff are computed (Figure S6B);
  - the exploration-visit window and the 50 ms placement (Figure S6E/F).
- **Figure S6D:** the remapping measure.
- **Figure 7:**
  - which sessions count (neurofeedback only, or pooled with head direction);
  - "primarily" (more than 50%, or the largest state);
  - whether the chi-squared tests count bins or events;
  - the denominator for the SWR and non-SWR measures (all center-port bins, or only the SWR or non-SWR bins).
- **Figure S7:**
  - the "late" theta phase reference;
  - for S7B, S7C and S7D the paper gives no test, so I set thresholds myself and say so in each criterion.

**Missing from the paper and its code:**
- The SWR detection parameters: the Methods only cite ref. 25, and the code's stored parameters aren't in the repository. The author has to take them from ref. 25.
- The code for the Figure 3 event classification, the Figure 6 per-assembly summaries and the chi-squared tests.
- The notebook's reward-count lists for rats 3 and 4 are identical, which looks like a copying error, so rat 3's list is not used for comparison.
