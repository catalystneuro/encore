No outcome changed. The verifier agreed with all 20, and round 1 is recorded under `verifications` in `attempts/000147-guan-2022-01.yaml`. I re-ran the entry with `python tools/entry.py all entries/000147-guan-2022`: it passes with 0 errors in 102 s, and every conclusion matches the new outputs.

**Outputs the verifier asked for**
- **Cue location (fig1s6b), possible trial-order artefact:** all 340 screens cue each of the 12 locations once and each condition twice. With folds that never split a screen, accuracy is 11.1%, above all 200 shuffles of location within screens (highest 9.8%). With folds that never split a run it is 11.3%. One new fact: location and position within the screen are weakly linked (chi-square p = 0.037). The outcome stays not reproduced.
- **Gaze regression (fig1s6a), run under both assumed grid layouts:** ordinary least squares gives r² below 0 in all ten sessions. Ridge regression gives r² up to 0.10, and only 5 or 6 of the ten sessions pass the criterion. The claim stays blocked, because the layout is unknown and the result depends on the type of regression.
- **Is the trial start the cue?** The column descriptions are now printed. The start time has only the generic NWB description, so the decoding-curve check is still the evidence that it marks the cue.
- **Units table columns:** printed. They are spike times, observation intervals, electrodes and electrode groups only, which confirms the fig4s4 block.
- **Model files:** the condition-order check only ever ran on one of the two kinds of descriptor. The unstructured model stores its order under "finger", not "condition", so it was never checked. The helper now reads either, fails if neither is there, and the order is printed: T, I, M, R, P in all three files.

**Other problems from the report**
- **fig3a trend:** I added two other model specifications and the main statistic read with the paper's 6 degrees of freedom. The one-tailed p is 0.096, 0.116 and 0.84, none below 0.05, so "reproduced" stands.
- **fig3s1 per-run distances:** the conclusion now says the per-run noise estimate inflates the distances, and that the variant using the session's noise estimate is the better estimate of the session trend. I added that variant's effect sizes (0.017 and 0.013, still under 0.02).
- **0.1 Hz cutoff:** measured over the whole recording, the lowest rate is 0.147 Hz, so no unit is excluded under either definition.

**Correction:** the attempt said the cue location had no description. It is described as "screen location (index) where text cue was displayed". I fixed the notebook and the finding.

**Not done, and why**
- The authors' exact regression for fig3a can't be checked, because their code for it is not in the repository.
- No change to the fig1b error denominator, the 83 against 82 degrees of freedom, or the bootstrap test. These were already recorded as deviations, and the verifier said they do not change an outcome.
- The verifier said it saved the paper under `paper/`, but nothing was there. I downloaded the full text into `paper/guan-2022-elife-74478.xml`. The repo's `.gitignore` excludes that folder, so the file will not be committed.
- `README.md` is unchanged, since no outcome changed.

Nothing was committed or pushed.
