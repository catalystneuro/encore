I wrote the claims file `claims/crcns-alm-3/10.1038-nature17643.yaml`. The quote checker passes: 29 claims, 29 quotes, 0 problems.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC5081260), as supplied in `paper/`. It has the main text, the Methods, and the legends of Figures 1–6 and Extended Data Figures 1–10. The paper has no separate supplement. No PDF of the paper was supplied, so numbers that appear only inside figures were not read: the per-condition performance in Fig. 1d and 5b, and the bar values in ED Fig. 8a and 8b. I did not read the version of record or the listed corrigendum (doi:10.1038/nature18623), because neither was supplied. The paper links no code. The data set's description says it includes MATLAB scripts that reproduce the figures; those are data set files, so I did not open them.

**Counts.**
- **Claims:** 29, and all 29 have quotes. None needed an `inferred` note.
- **Criteria:** all 29 have one.
- **Expected values:** 18 claims have them.
- **Statistics:** 5 claims carry 11 test entries. These are Fig. 1d, the early-delay absence claim, Fig. 2b (5 tests), ED Fig. 4c (paired t-test), and the callosotomy behaviour (t-tests and the repeated-measures ANOVA). I left out the p < 0.05 and p < 0.01 thresholds the paper uses to count selective neurons or neurons with a changed rate.

**Details the paper leaves open, with the readings named:**
- **Lick-early trials in the electrophysiology analyses:** excluded, or included.
- **Response epoch length:** the first 400 ms after the go cue, or the 1.5 s answer window.
- **Trials for the selectivity test:** correct trials only, or all trials grouped by instructed movement.
- **Excluding neurons under 1 spike/s in Fig. 1f, 2d and 5d:** with, or without.
- **Preferred trial type:**
  - 10 trials of each type, or 10 trials in total.
  - The window that sets the preference: the whole trial, or the most selective epoch.
- **Selectivity time bins:** 200 ms or 400 ms windows. The 50 ms step is a standard choice.
- **Time stamp of a window:** its centre, or its end.
- **Window meant by "within 400 ms after" offset (Fig. 1f):** the window starting at offset, or the one centred 400 ms after it.
- **"Spike rate (> 90 %)" in Fig. 2:** more than 90% of neurons unchanged, or the mean rate within 10% of control.
- **Population analyses:**
  - Units: pyramidal only, or all units.
  - Which windows build cd: centre inside the sample and delay epochs, or wholly inside them.
  - How control trials are split: random halves, or leave-one-out.
  - Scaling of cd: raw, or unit length.
- **Mode decomposition:** the baseline (pre-sample, or whole trial) and how a mode's share is computed (RMS ratio, or squared-norm ratio).
- **The "during photoinhibition" ROC window:** the 400 ms before the ramp, or the whole 0.8 s.
- **Behavioural t-tests:** paired or unpaired. A mouse's performance as pooled trials, or the mean over sessions.
- **ED Fig. 4c:** which photoinhibition conditions are pooled.
- **Reaction time:** not defined; I read it as go cue to first lick.
- **Model simulations:** integration step, noise scaling and random seeds.

Where the paper gives no test at all (ED Fig. 6, ED Fig. 9f, the claims that the persistent and ramping modes do not predict, prediction along cd), I named a standard test as a choice and said so.

**Inconsistencies noted:**
- The paper uses two names for the third Experiment 1 window: "late delay" in the Methods and Fig. 1g, "middle delay" in the Results. The file identifies that window by its end time instead.
- The ED Fig. 7e bilateral ROC is printed as 0.54 ± 0.8. I took 0.08 as its tolerance and marked that as a reading.

**Data the claims need that the data set may not hold:** the data set's documentation says it does not contain the behaviour-only sessions or the photoactivation data. That affects:
- Fig. 1d at the go cue.
- ED Fig. 3.
- Most of the 13 mice behind Fig. 2b.
- ED Fig. 5.
- The untrained-mouse mapping in ED Fig. 2d.
- Possibly the pre-callosotomy sessions needed for the Fig. 5b interaction.

The two model claims are simulations built from the parameters in the Methods. The FORCE training is not fully specified, so those networks are to be reported but are not part of the pass/fail test.
