I've revised the attempt after round 1. All four notebooks pass a clean run (`python tools/entry.py all entries/vinograd-2024`), and the record check reports 0 errors. Nothing is committed.

**Outcome changes**

The record now has 8 reproduced, 10 partially reproduced, 10 not reproduced and 26 blocked, the same totals as the verifier's.

| Claim | Was | Now | Why |
|---|---|---|---|
| ed7f | reproduced | not reproduced | Shifting M70's target indices by −2 to +2 does not fix them. The cells that respond rank 1, 2, 4, 8 and 64 by stored x1 weight, so M70's target list is wrong, not its weights. With M70 left out, activation is higher in 6 of 6 mice (p = 0.0043). |
| ed8c | reproduced | partially reproduced | I added the simulation without kicks. It also rises in 7 of 7 mice. The part due to the kicks also grows in 7 of 7. |
| methods-cvr2 | blocked | not reproduced | The random-frame folds still can't be fit with the rSLDS library (ssm), so I added an upper bound instead: even in sample, the models explain only 51.0% and 54.2% of the variance, against 84.7% and 67.2%. |
| ed3h | reproduced | partially reproduced | I ran it with each of the four seeds the sample code tries. One reading holds with 3 of 4 seeds, the other with only seed 0. |
| fig2gh, fig2no | not reproduced | partially reproduced | Accepted the verifier's reading. |
| ed8b | reproduced | partially reproduced | Accepted the verifier's reading. |

**What I added or corrected**
- **Data checks:**
  - The projection metadata printed row by row. The frames 300 to 400 baseline belongs only to M79RL's observation session, and the smoothing only to M179's, so no stimulation claim uses either.
  - The sign of each target's stored weight. All x2 targets are positive.
  - A check that the two miniscope sessions of a mouse hold the same cells. Each cell's 5 s autocorrelation agrees across sessions in every mouse (r 0.35 to 0.61), which is consistent with matched cells but not proof.
- **Seeds:** the decoding claims now run with all four seeds. ed3g holds with 3 of 4 and stays reproduced, still resting on seed 0. The helper no longer calls the seed a choice that can't change a result.
- **Assumptions now marked:** ed4c and ed4d rest on the cells being matched. ed4g and ed4hi rest on the time before the first annotation being the end of the 5-minute baseline the files don't hold.
- **ed8gi:** added the result without M70, where nothing is significant. The notes now say the outcome rests on that one mouse.
- **ed9d:** the notes now say that "lower in 7 of 7" holds by construction.
- **Small fixes:**
  - fig2gh/fig2no now take the last pulse's frame at onset + 210, as the criterion says.
  - The autocorrelation is now scaled so its value at lag 0 is 1. This moved ed3f from 12.7 to 12.8 s.
  - Result headings in `rslds_fits.ipynb` are renamed so the handover tool strips them.
- **Record:** findings updated (the M70 target list, the cvR2 question, cell matching, questions for the authors). Round 1 is recorded under `verifications`: 45 of 54 claims agree, with the verifier's reasons and my responses. The protocol version is now pilot-14.

**Not done**
- **fig4hj and ed10g** stay blocked as data missing, with the disagreement recorded. The claims file lists dependencies on blocked claims, and the protocol blocks such claims. For ed10g, the Methods define "follower" cells by the 50 µm exclusion, which needs cell positions the files don't have.
- **ed10c** partial test without the exclusion was not run, because the exclusion is part of its criterion.
- **The random-frame cross-validation** was not run; the in-sample bound covers it.
- **No questions** were added to `questions/vinograd-2024.yaml`, because the verifier found no place where the claims file misreads the paper.
- **The cross-validation notebook** takes 44 minutes, which leaves little room under the 60-minute limit.
