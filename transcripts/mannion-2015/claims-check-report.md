The claims file for CRCNS:vim-3 is ready for an attempt. I made four corrections, and two minor points stay open.

**Checker result:** `16 claims, 16 quotes, 10 statistical values, 0 problems` (before and after my edits).

Every quote, source paragraph, statistic and expected value matches the paper. I cloned the analysis code (mannion-lab/ul_sens_fmri_analysis at 571e9312) and checked the code details the criteria rely on. All of them match the code as described. The paper's main findings each have a claim, and every claim comes from this paper.

**Changes**
- **Opening comment, localiser threshold:** it said a one-sided t above 2.58 is p < 0.01. In fact 2.58 is the two-sided p < 0.01 value, and the code keeps only positive t. Reworded.
- **localiser-masks-ventral-dorsal:** the rule for "largely confined" (most nodes in the expected half, in most participants) is not from the paper, which shows only one example participant. The criterion now says so, marks the outcome as resting on that assumption, and asks for the fraction of nodes in the expected half per participant.
- **fig5-no-other-pixel-relations:** "mean of the two chromatic channels" could be read as one averaged measure. The paper and the code test the mean of each chromatic channel separately, so I reworded the statement and criterion.
- **fig5bc-spatial-frequency:** the filter scale (pixels per degree) comes from a local display calibration file that is not in the code. I named it as open, with the two values the paper's own display and stimulus numbers give: about 78.7 and 78.2.

**Open**
- The "partially reproduced" levels in several criteria are judgement scales not taken from the paper. The "reproduced" rules rest on the paper's numbers.
- The Figure 4 differences and Figure 5 data points are printed only inside the figures, which I did not have as images, so they are not expected values.

Each change and open point is recorded under `checks` at the end of `claims/crcns-vim-3/10.7717-peerj.1038.yaml`, with `ready: true`. Nothing is committed or pushed.
