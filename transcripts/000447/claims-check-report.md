The claims file for DANDI:000447 is ready for an attempt. I made 8 corrections and left 2 problems open. Only `claims/000447/10.1016-j.celrep.2023.112246.yaml` changed, and nothing was committed.

**Checker result:** `32 claims, 32 quotes, 49 statistical values, 1 problems`. The one problem is p = 1.39e-11 in fig3d-selectivity-index. The text prints it as "1.39e11" with the minus sign lost, as it does "1.35e16". The claim already reads them as 1.39e-11 and 1.35e-16, which is correct.

**Changes, by claim**
- **fig1c-session-performance, fig2d-pv-similarity, figs5d-path-equivalence:** I removed the overall ANOVA entries recorded as "p < 0.05". The legends give only F (40.48, 83.24, 25.37) and no p for the ANOVA, so that bound was not the paper's. The F values are kept in the criteria.
- **fig1-denovo-final-performance and fig1c-session-performance:** which session counts as "final de novo" is open. Three of the five rats trained 2 more days before the N-F-N' day. The criteria now allow two readings: (a) the last session before the N-F-N' day, as the Figure 1C legend says; (b) the eighth session of the de novo day.
- **fig1c-familiar-above-novel:** the p = 0.0053 Tukey pair is now marked as not named, since the legend does not say which pair it is.
- **fig2d-pv-similarity, fig3d-selectivity-index:** the main rule for a spatially tuned cell is now the Methods' "peak rate at least 3 Hz". The code's "above 3 Hz" is a variant.
- **fig2e-ca1-error-familiar, fig2e-pfc-error-stable:** the legend does not say which groups go into one Kruskal-Wallis test. The criteria now allow all four groups together, or N and F per region. They also say the 100 shuffles in one reading are a standard number, not the paper's.
- **figs4d-reward-location-similarity:** the criterion judged only the reward-well bins. The legend says Grubbs' test found no outlier at any location, so the criterion now requires that. It also names the open choices of what one test covers and which novel session is meant.
- **fig3e-selectivity-stable:** full reproduction now needs the CA1 r within its tolerance too. The expected values and the partial-reproduction clause already used it.
- **fig4d-pfc-ccgp:** I rewrote the task-sequence decoders from CCGP_taskSeq.m. Each decoder is tested on the two outbound or the two inbound clusters at one phase and trained on the other direction's four clusters. Training on all six remaining clusters is a variant.

I also cloned the paper's code at the cited commit and checked the main code details the criteria cite. They match the file.

**Still open**
- The width of the 1D smoothing of the rate maps is garbled in the text and the code is not in the repository. It stays open, with readings, as the file already had it.
- The main-text PDF is not in `paper/`. So I could not read Figure 2F (the trial range -10 to 10) or Figure 4D (whether the permutation test is per decoder or per variable). The criteria follow the code for both.
