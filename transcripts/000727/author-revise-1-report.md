No outcome changed. The 14 tested outcomes stay at 7 reproduced, 5 partially reproduced, 1 not reproduced and 1 reproduced but disputed (fig5c), with 6 blocked. The entry was re-run twice from a clean environment, passes `check`, and both runs give identical numbers in about 12.5 minutes. The round is recorded under `verifications` in `attempts/000727-brezovec-2022-01.yaml`, and nothing is committed.

**Outcome disagreements**
- **fig5c-global-below-threshold:** I kept "reproduced" and recorded the disagreement; the verifier would give "partially reproduced". Its objection was that the p = 0.031 behind the pass ignores autocorrelation. I added the null it asked for: 200 circular shifts of each fly's behaviour, which keep the autocorrelation. Under reading (b) all nine below-threshold correlations still beat it. The weakest, r = 0.013, has p = 0.025 against a null 95th percentile of 0.010. Reading (a) still fails.
- **The four region-level claims (fig2e, fig3, fig6eg, fig7):** the verifier agrees they are blocked but would give `data_missing`. I kept `metadata_insufficient`, because the voxel data are in the dandiset and only the labels are missing. The disagreement is recorded.

**Added or corrected, by verifier point**
- **fig2c, reading (b):** fixed the denominator, so 54.9% becomes 53.5%. A null with shifted behaviour gives 0.0% under both readings. The fig2c-venn reading (b) value moved with it (VF and turning 40.4% to 39.4%).
- **Clock check:** the null is now the largest |r| over the same 101 lags, so it is comparable with the observed peak. Its 99th percentile is at most 0.103, against observed peaks of 0.412 or more.
- **fig2-symmetry:**
  - Both turn directions are on the expected side in 6 of 9 flies, not 5 as the verifier counted (fly_097's left-turn difference is small but positive).
  - No fly appears flipped: every fly's maps correlate more with the pooled maps than with their mirror images (fly_105: 0.418 against 0.240).
  - I recorded that the 0.7 threshold was chosen after seeing r = 0.82, and the plot's colour range now spans the data.
- **fig4i:** added a shifted-behaviour null. The median pair correlation of weights is at most 0.151 under it, against 0.65 to 0.76 observed. The conclusion now says part (iv) follows partly from how PC1 is signed.
- **fig5a:** the text now says the forward-velocity advantage depends on the 0.01 threshold and on how walking state is defined.
- **fig5f:** added the contrast from the demixing model, as the paper uses. The mirror blocks still rise (6.5% and 18.8% fall), so "not reproduced" holds. The difference in method is recorded as a deviation.
- **fig6-peak-time-range:** added leads per imaging plane. With each plane's median removed, the 99th percentile becomes 0.50 s. The notes now say the 0.32 s match is not robust to the unknown plane times, while the lag of more than 1 s holds in every plane from 38 on.
- **fig6h-peak-vs-width:** with plane means removed the lag-width correlation is r = 0.623. Within single planes it is positive in all 10, and p < 0.05 in 8.
- **figs2-tdtomato-control:** added a check on two raw, uncorrected planes per fly. Across flies and planes, the median share of voxels correlated with behaviour is 0.23% for tdTomato and 0.60% for GCaMP6f, but fly_089 reaches 3.53% in tdTomato. The claim stays blocked.
- **Data check:** it now lists the nine AVI behaviour videos and every array in each file with its shape and chunks.
- **Housekeeping:** the README and `entry.yaml` now give the new runtime of about 13 minutes.

**Not done**
- **Partial supervoxel-number sweep (figs4a):** not attempted. It would need each plane's voxel time series in memory (about 3 GB per plane) for Ward clustering at seven sizes. The notes now say this.
- **Plane-axis orientation:** the verifier asked how the atlas's plane axis relates to the acquisition order. The dandiset does not hold the acquisition order, so this cannot be answered.
- **Paper text:** bioRxiv rate-limited every download (error 1015 and HTTP 429), so nothing is saved under `paper/`. No change depended on new reading of the paper; the method used for Figure 5F comes from the verifier's quote.
