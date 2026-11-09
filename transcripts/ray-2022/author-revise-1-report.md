I went through every point in the round-1 report, re-ran the entry with `python tools/entry.py all entries/crcns-nac-1-ray-2022` (0 errors, the notebook now takes about 5 minutes), and recorded the round under `verifications` with all 34 claims.

**Outcomes that changed**
- **units-recorded**: partially reproduced → not reproduced, as the verifier said. The data set has 90 sessions where the paper says 95, the tolerance is zero, and the criterion has no partial outcome.
- **fig9bcd-reward-pre-post**: partially reproduced → not reproduced, as the verifier said. With the baseline fixed and events kept inside the recording, the claims-file reading fails: Bidirectional Valence firing before reward is above zero (0.18 [0.02, 0.34]) and the post-reward means (1.43 and 0.78) are outside 0.47 ± 0.15. The old partial result came from the script's own procedure, which the Methods don't describe; it is now shown only as a variant.
- **fig10bcd-poke-cessation-pre-post**: reproduced → not reproduced. Once the pokes just before a recording pause are dropped, the Bidirectional Valence pre-cessation CI contains zero (0.085 [-0.009, 0.207]). The verifier had marked it reproduced, but only on the uncorrected events.
- **fig10a-poke-cessation-anova** stays reproduced, against the verifier's not reproduced, and the disagreement is recorded. It no longer rests on the script's windows: with the events corrected, the claims-file reading shows no interval effect (p = 0.26 and 0.12) and a significant interaction (p < 1e-4).

**Fixes and added outputs**
- **Problem 1, event baseline.** The baseline is now the 1 s before the event, as the Methods say. I printed the script's own lines (it uses 2 to 1 s before) and added this to the code-mismatch finding.
- **Problem 2, recording pauses.** Events must now lie inside a recorded segment, and a cessation only counts if its 2 s without a poke are recorded. The notebook prints how many were dropped: 301 of 2159 rewards and 2737 of 15363 cessations under reading (b). This leaves reading (a) with no events at all, so it is reported as untestable.
- **Problem 3, CI form.** A new section re-judges every CI-based claim under both interval forms, with the analytic and the `bootci`-style inner-bootstrap standard error, over five seeds. Only fig1g changes with the form: without reflection it is reproduced under all six readings. fig8ab and fig8cd shift for some readings but their outcomes hold. I removed the untested claim in `nac.py` that the standard-error choice can't move a bound.
- **Problem 4, which clustering.** I kept the "best match to the five patterns" rule as a stated assumption. A new section sets every population claim's outcome on the primary clustering beside the near-tied alternative. They differ for fig5ab (reproduced on the alternative) and for the fig7 Threat Inhibited peak (0.50 on the alternative).
- **Problems 5 to 8.**
  - The 193-unit screen is now stated as an assumption.
  - Outcome counts only include clusterings whose clusters match their names.
  - The two fig6 readings, and the two fig7 per-trial readings, are shown to give identical results; they are one reading each.
  - The chance check now places fake cue onsets inside recorded time. About 26% of units pass, against 59.5% at the true onsets.
  - A mislabelled "N1" in the reward section is corrected.
- **Section C requests.** The notebook now prints:
  - the script lines for the 0/0 = 1 setting, the event windows and baselines, and the `bootci` call;
  - sessions per rat;
  - the seed-1001 CI flags for fig1g.
- **Item 9.** I created `questions/crcns-nac-1.yaml` with three questions for a reader: whether to add 0/0 = 1 as a reading, whether to add the script's normalization, and which interval form the paper used. No claim was changed.

**Not done, and why**
- The 90 versus 95 sessions can't be checked against the paper's per-rat counts, because Extended Data Figure 1-1 isn't available.
- I did not switch the judging to the paper's interval form. The claims file says studentized `bootci`, so the standard interval stays primary; the paper's form is shown alongside and asked as a question.

Nothing has been committed or pushed.
