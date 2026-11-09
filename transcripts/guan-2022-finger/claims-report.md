I wrote `claims/000252/10.1101-2022.12.07.22283227.yaml`. The quote checker reports 19 claims, 19 quotes and 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, from the JATS XML. It includes the main text, Methods, figure legends and the legends of Supplementary Figures 1 to 11. There is no PDF. The paper links no analysis code. It names two Python libraries, rsatoolbox (for the neural distances) and DABEST (for effect sizes and bootstrap intervals).

**Dataset:** its archive title is "Finger_RL", attempted finger movements of the right and left hands, so it should hold the ten-finger task. The claims about the right-hand-only task and the online BMI sessions may have no data in it. The author has to find out.

**Claims:** 19, all with quotes and all with criteria; 15 have expected values.
- **Statistics:** 9 entries in 4 claims.
  - Three 95% confidence intervals: matching right/left finger pairs are closer than non-matching ones.
  - Six permutation tests at p < 0.001: decoders generalize across hand and across finger type.
- **Ten-finger task (8 claims):**
  - neuron and session counts, and the 1111 pooled N-PPC neurons
  - share of neurons that tell fingers apart (66%, 57%, 78%)
  - ten-finger decoding accuracy (70%, 66%, 75%) and the kinds of errors made
  - matching against non-matching distances, and the index finger standing apart in N-PPC
  - generalization of hand and finger-type decoders, with J-PPC's finger-type result low (36% against 65%), even at matched neuron counts
- **Right-hand task, offline (5 claims):** single-neuron tuning, planning against execution, decoding with its error structure, how much data N-PPC needs, and planning-period decoding.
- **BMI (3 claims):** online accuracy (86% and 92%), single-array decoding after the fact (83% and 87%), and left-hand control (94%).

**Details the paper leaves open, with the readings named:**
- **O1, the 0.5 Hz neuron exclusion:** the average rate over the whole session, or over the analysis windows.
- **O2, how trials go into the 8 folds:** in trial order, or shuffled over 10 seeds.
- **O3, the noise covariance for the distances:** rsatoolbox's `shrinkage_diag`, `shrinkage_eye` or `diag`.
- **O4, how trials are split for the distances:** odd and even halves, or leave one repetition out.
- **O5, the confidence interval method:** DABEST's bias-corrected bootstrap, or a percentile bootstrap.
- **O6, how trials from different sessions are combined into one population:** matched by repetition index, or matched at random and resampled.
- **O7, the decoder for the generalization test:** the Methods' diagonal LDA, or a linear SVM.
- **O8, the accuracy that generalization is compared with:** decoding within each hand, or decoding finger type over both hands.
- **O9, what "close to" that accuracy means:** the paper gives no margin. I named two readings: at least 0.9 of it, or a ratio above J-PPC's 0.55, which the paper calls "much lower". The 0.9 is my own figure, so a checker may want to look at it.
- **O10, the inputs to the single-array BMI decoder:** threshold crossings, or sorted neurons.
- **Inside single claims:**
  - whether "mean number of significant fingers" and the share with large effect sizes are taken over selective neurons or over all neurons
  - whether the false discovery rate correction is applied per window or over both windows

**Missing from the text:**
- The contents of Supplementary Tables 1 (phase durations) and 2 (session dates); only their captions are there. No claim rests on them, because every analysis window is timed from a phase onset.
- The equation for the cross-validated distance; it is lost in the text, so I used its description in words.
- **Minor count mismatch:** the pooled right-hand-task neuron count in the Figure 4c legend (466) does not match 118 neurons per session over 4 sessions (472). The count claims accept counts taken before or after the 0.5 Hz exclusion.
