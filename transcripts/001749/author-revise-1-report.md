I've revised the attempt for every point in the round-1 report, and the entry re-runs cleanly: `tools/entry.py all` passed in 26 min and `check` reports 0 errors. Every conclusion in the notebook and record matches the new numbers. Nothing is committed.

**Outcome changes**
- **ed5c (rewards):** reproduced → partially_reproduced, as the verifier gave it. The rewards part holds (p = 0.498 over 20 sessions). The body-weight part can't be tested: a new cell prints every subject field of all 53 files, and none holds a weight.
- **ed5d (latency):** reproduced → not_reproduced, marked as resting on an assumption. I ran the robustness checks the verifier asked for:
  - Using the hand-scored labels on the same trials: p = 0.16.
  - Leaving out the files whose labels and port entries agree at r below 0.3: p = 0.158.
  - Matching each file's labels to the tones they actually belong to, then leaving out the poorly matched files: p = 0.375.
  - Subordinates are slower in every version. The difference is significant only when trials whose labels can't be placed on the port entries are kept.
- **fig1i, ed5j, ed5k (HMM-GLM):** these were blocked and are now tested. I ported the paper's MATLAB HMM-GLM (Tyelab/HMMGLM at the pinned commit) line by line to `hmmglm.py`. On the paper's own processed input it reproduces Fig. 1i and ED Fig. 5k. The main input is multi-unit counts I computed from the raw recordings of the 17 labelled files whose offset can be placed (512 of 965 trials, 10 of 14 mice).
  - **fig1i:** reproduced, marked as resting on an assumption. HMM-GLM AUCs are 0.60 to 0.83 against GLM medians near 0.54, and the tests give sign p = 0.0039 and rank-sum p = 0.0003. Two other ways of preparing the input or forming the folds fail: rates z-scored per channel, and random folds without the one-bin shift. The outcome rests on counts and contiguous folds, which the paper's own input and code use.
  - **ed5j:** not_reproduced. Held-out likelihood peaks at 2 states, not 6.
  - **ed5k:** not_reproduced. Trained on subordinates (only 4 mice) and tested on dominants, 7 of 9 labels are above chance (p = 0.18). On the paper's input both directions pass.

The README and summary now carry the required "failure to reproduce" sentence.

**Added or corrected**
- A file-contents cell: the full group tree of one file per cohort, the units table columns, and the 52 mp4 assets. It shows there is no `video_gap`, stimulus, optogenetic series or weight.
- A cell checking which tones the label trials belong to. In 18 files the labels hold fewer trials than tones, and in several the labelled trials start at a later tone.
- Alignment checks for the HMM-GLM input:
  - The computed counts follow the spikes in the same windows (median r 0.40 to 0.96 per file).
  - The paper's processed input confirms the estimated offset in 16 of the 17 files used. The exception, 20191029-chrimson2-2-2v3, is noted as most likely misaligned.
- Sessions are now the main reading for ed5c and ed5e, and files a variant, since files double-count sessions.
- I removed the ed5f "competitor's view" variant (it gave identical numbers) and noted that the two switch rules can't differ.
- The header table now counts 22 single-unit claims, 46 in all.
- Three new findings, the two code-repository inputs, and the round-1 `verifications` entry for all 46 claims.

**Not done, and why**
- **Behaviour videos:** not read. The LED places the tone in the video, and the labels are already on the tone clock; it doesn't give the offset between video and logger, which is what's missing.
- **ed7b partial route:** not tried, block kept. Identifying the subject by dye pattern would mean scoring the videos by hand, and a port location estimated from poses isn't the paper's hand-marked one.
- **The SVM model and the five-model Kruskal-Wallis test:** not run, because the fig1i criterion doesn't use them.
- **ed5j on the paper's input:** run for 1, 6 and 10 states only.
- **Questions for a reader:** none added, since the verifier found no misreading of the paper in the claims file.
