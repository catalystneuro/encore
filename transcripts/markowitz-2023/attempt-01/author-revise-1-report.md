I've revised the attempt for round 1. The entry re-runs cleanly in about 16 minutes (`entry.py all` and `check` both pass), and the last run printed the same numbers as the run before it. Nothing is committed.

**Outcome changes**
- **fig3e-learner-count:** changed from partially reproduced to not reproduced, as the verifier said. The criterion only defines the reproduced case (9 learners), and 7 is outside the tolerance. The notes still say the "only a fraction learn" part of the statement holds (7 of 20).
- **All other outcomes are unchanged.** The verifier thought fig2e might become reproduced once its shuffle was fixed. It did not: it is now significant at 6 of the 10 values of n up to 190. It is not significant at n = 110 to 170, with P from 0.05 to 0.18.

**Fixes for the verifier's problems**
1. **fig2e and the DMS test:** the shuffle now moves only instances that have a dLight peak. The output now shows that the observed value and every shuffle use the same number of groups (15,480 at n = 10). DMS is significant at 9 of 10 values, so ed7-dms-no-usage-prediction stays not reproduced.
2. **fig3l and fig3m:** the notebook now says the blocking rests on evidence, not on a decision made once the analysis had run:
   - Under the substitute catch set, stimulation covers a median 0.593 of detections per mouse in the 250-ms sessions. The Methods give 0.75.
   - With catch trials at least 2 s from any pulse, the no-opsin controls stay significant (9 of 12 at 250 ms, 2 of 2 at 3 s).
   - Taken literally, the criteria would give fig3l not reproduced and fig3m partially reproduced. Both remain blocked because the controls fail.
3. **fig3h:** the test is now one-sided as labelled, with the two-sided P printed beside it. Learners give r = 0.891, P = 0.017.
4. **fig1e:** bins are now dropped only when they have fewer frames than the mode, as the criterion says. The transient rate is significantly positive at 47 of 100 timescales of 10 s or more; the binned amplitude at none.
5. **Habituation sessions:** these are now left out of all photometry analyses (17 DLS files, 1 DMS file). This moved most of the DLS numbers, and the notes and conclusions now match the new numbers. The habituation files of dms-dlight-1 and -4 have no dLight series, so the analysis never loaded them.
6. **Shuffle P values:** fig2b and fig2i now print "P < 0.005" when no shuffle reaches the observed value. The forest settings and single label shuffle in fig1l are now listed as deviations.

**Outputs the verifier asked for, now added**
- Files left after each filter, per mouse. 177 DLS sessions are usable, against 379 in the Methods.
- Kruskal-Wallis H with the sessions that fail quality added, and for each session set. The quality filter does not explain the difference: H is 265.6 with the failing sessions against 266.4 without.
- The stimulation-pulse clock check split by rotated and unrotated clocks. The two give the same result (0.936 against 0.938).
- Per-target counts and baseline days for 3442, dls-ai32jr-1 and vta-nacc-ctrl-6. These show no single reason for the two missing learners.

The attempt record now has the round-1 `verifications` entry for all 24 claims, with updated outcome notes and findings. The README and `entry.yaml` have the new outcome and runtime.

**Not done, and why**
- I did not attempt the blocked claims the verifier called testable: fig1f, fig2k, ed10d, fig4b, fig4c, fig4h and fig5. That was out of scope for this revision; each response in the record says so.
- I did not add the spontaneous half of fig2a, because the claim is a comparison with reward transients and those are not in the dandiset.
- I did not add a comparison with the pre-stimulation baseline for fig3i, because the claim compares stimulation with catch trials and that would be a different test.
- The fig1l forest was not changed to the paper's 1,000 trees and 100 shuffles; this is recorded as a deviation.
- I did not paste the paper text into `paper/`; the notebook already cites the open-access full text.

Some untracked dotfiles and folders (`.bashrc`, `.idea`, `scripts` and others) are in the repository root. I did not create them and left them alone; the workflow's commit should leave them out.
