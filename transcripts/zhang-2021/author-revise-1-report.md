I've worked through all of the verifier's round-1 report. The final run of `python tools/entry.py all entries/zhang-2021` passed in 51 minutes, under the 60-minute limit, and the entry and record checks report 0 errors. Nothing is committed.

**Outcome changes (both were blocked as `data_missing`)**
- **att-weights-cortex: now reproduced, resting on assumptions.** This follows the verifier's point 3. I used two public fsaverage atlases through the data set's own mappers: visfAtlas (Rosenke et al. 2021) for FFA, OFA, EBA, PPA, OPA and MT+, and HCP-MMP1.0 for RSC, LO, FO, IFS, IPS, FEF and SEF.
  - With the claims file's threshold (ii), the WordNet encoding model I added to the helper, the pattern holds in 4 of 5 subjects under all three weight readings. Without a threshold it holds in 3 of 5.
  - FFA, OFA, RSC, PPA and OPA hold in all five subjects. The outcome rests on EBA, which fails in S2 under every reading.
- **game-weights-two-groups: now not reproduced, resting on assumptions.** Only S7 can be placed on the cortex. In S7, 3 to 5 of the 8 dimensions fail the grouping under every reading, where the criterion allows one. S1 and the consistency between the two subjects stay untested.
  - In a variant that doesn't decide the outcome, S1's denoised weight maps cluster into exactly the paper's two groups.

The other nine outcomes are unchanged.

**Other fixes and added outputs**
- **Code's third axis:** the code's own coefficient for the attention variable is about 1e-13, against about 1e2 for human and vehicle, so its third axis is rounding noise too. As a result, the values from the code's own axis move slightly between runs: S2's are now 0.743, 0.721 and 0.675, against 0.740, 0.718 and 0.676 before. Classification on contiguous folds moved from 44.4% to 43.7% with the same seeds; I did not trace the cause. All numbers in the notebook and record match this run.
- **att-passive-lower:** the full null quantiles are printed. S2's difference (0.057) is above the 99th percentile but not above every null value. I stated that the refitted null is not computed the way the observed value is.
- **S1 game data:** they are six whole runs of 325 TRs, so the 65 minutes are not a subset of a longer session. They match no mapper, including the superseded ones in `Mappers/old`. The record finding is revised, and game-classification now notes that this could explain why S1 comes out above the paper's value.
- **Game labels one TR later:** the game CSI and classification are now also run this way. S7's CSI under reading (a) is then within tolerance, and no classification reading puts both subjects within tolerance.
- **Classification scoring:** a class dropped from a training fold is no longer scored with a recall of 0. The first reading is now 46.5% (S1) and 33.8% (S7).
- **fig3b:** added a test centred on the null's mean. The counts change by at most one pair.
- **Record:** added the round-1 `verifications` block, the two atlases under `inputs` (pinned by DOI and checksum), and two new questions for the paper's authors: how the game labels were aligned in time, and which encoding models set the map thresholds.

**Not done**
- Folds with a gap at their edges (point 6) were not run. The outcomes already hold under contiguous folds, and S1 is above tolerance under both fold schemes.
- No question was added to `questions/zhang-2021.yaml`, because the verifier reported no misreading of the claims file.
- The full run now takes 51 minutes, up from 28, mostly because of the WordNet model.
