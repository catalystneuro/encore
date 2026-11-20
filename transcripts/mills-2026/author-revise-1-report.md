I've worked through all ten points in the round-1 report. Two claims moved from blocked to partially reproduced and no other outcome changed. The entry was re-run with `python tools/entry.py all entries/mills-2026`: checks gave 0 errors and the notebook passed in 19 minutes, with the same numbers as the run before it. Nothing is committed.

**Outcome changes**
- **figs10-no-reward-relationship:** now partially reproduced, marked as resting on an assumption. The across-trials test across latency quartiles was run and finds no relationship in three of four readings (p = 0.14, 0.185, 0.18). The fourth (latency taken as tone duration, 10 ms bins) gives p = 0.047. The across-mice test needs unpaired mice, none of which have trial events, so it cannot be run.
- **fig2o-region-differs-cs-reward:** now partially reproduced. The ASt phasic CS-reward response is above zero (t(111) = 7.79, p = 3.9e-12). The comparison between regions cannot be run because no unit is labeled TS.
- **fig2o-ast-greater and fig2p:** still blocked. I ran ASt against the 22 CeA units from 2 mice and printed it for the record (no CS-shock difference). With 2 of the paper's 8 CeA mice and no TS units, it does not decide these claims.
- **figs10lm and fig3fg:** still blocked. A new check that fits the pose lag separately in each quarter of every session confirms a fixed offset in only 2 ASt mice, and only to within about 0.6 s. fig3fg judges a 0 to 1 s window after bout onsets, so an error that size would push the test toward the claim's own answer.

**Added or corrected**
- **Port latency (figs9):** now the tone duration, since the Methods say collecting the reward ends the tone. The first port entry is shown as the other reading; both give the same outcome.
- **Freezing (figs13, figs15):** in the imaging poses, about 20% of frames repeat the previous pose almost exactly (under 0.5 px) and every other frame moves more than 1.6 px. The paper's freezing rule therefore counts only those repeated frames, whatever the pixel scale.
  - In figs13, freezing alone does not differ between cues; the difference comes from darting. figs13 stays reproduced.
  - figs15 still fails on its activity part, so its outcome does not depend on freezing.
  - This is recorded as new finding 12 (minor).
- **Imaging checks:**
  - Fluorescence decays within each clip by the same amount in every group, so it does not explain the group differences.
  - A version with the baseline trend removed keeps them.
  - Mouse-level tests are added for fig5h CS-reward and fig5k.
  - fig5h is also shown without the two thin unpaired sessions.
  - Each session holds 15 imaged reward trials, not the roughly 22 the Methods imply. The 10 s requirement drops only one event.
- **Neuropixels units:** they do have a probe depth, a good/mua label and histology images. I corrected finding 3, and the fig2 cell now counts the units labeled good (still above the paper's counts).
- **Wording fixes:**
  - fig2q: the full-PCA distance is the Methods' reading, not only the code's.
  - figs8: five animals cannot reach p < 0.01, and the pooled reading overstates the evidence.
  - snRNA-seq claims: the reason now says the data are at GEO and the paper's R pipeline can't be installed in the entry's Python environment.
  - README, header and summary updated to 13 tested and 35 blocked.
- **Verification record:** round 1 is recorded for all 48 claims. The verifier disagreed with the block on 4 claims, and each response says what changed.

**Not done**
- No reader question was added, because the verifier reported no place where the claims file misreads the paper.
- The GEO snRNA-seq data was not fetched or analysed. Those three claims stay blocked because the paper's R pipeline can't run in the entry's environment.
