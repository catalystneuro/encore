**Verifier report, round 2: Vijayan et al. 2022 (doi:10.1126/sciadv.abn3852), DANDI:000212 draft**

The claims file has 45 claims and the attempt record has 45 outcomes, one per claim. Those outcomes are 22 reproduced, 7 partially reproduced, 4 not reproduced and 12 blocked (all data_missing). Four outcomes are marked `assumed: true`: fig3e, fig5ab, fig7cf and figs4.

### 1. Outcomes

I agree with all 45 stated outcomes. The changes since round 1:

- **fig6cd and fig6g, now reproduced, and fig6b, now blocked as data_missing.** I agree. My round-1 agreement with blocking these for metadata_insufficient was wrong. Cell 14 shows the Agarose_Percentage series, which changes only with the island, and that the chambers were loaded both ways round (18/6 and 12/12 flies).
  - fig6cd (cell 84): merges at 20 and 20/25 s.
  - fig6g (cell 90): median time on 0.8% is 0.609 over all frames and 0.672 over search frames.
  - fig6b: bars 2, 3 and 6 are missing, and the criterion needs them.
  - The criterion's "chambers with equal sucrose" is tested on the one such chamber the dandiset holds, and the record says so.
- **fig3e, now partially reproduced (assumed).** I agree, and this replaces my round-1 "reproduced". Cell 48 shows the 150–240 s bin already high: 0.922 against 0.316 eggs/min, p = 0.0014. That is a rise below 240 s, the edge the claims file fixed.
  - The assumption is stated and reasonable, but the step test carries it. Starting the Spearman test at 5 s, on the grounds that the merge point counts from there, does not carry over: this x-axis is dwell time, not time since a transition.
  - The case is borderline, because the paper says "~4 min".
- **figs4, kept as reproduced (assumed).** I now agree, and drop my round-1 "partially reproduced".
  - The criterion tests model 1 only. The log-link fit (cell 117) also overestimates the 0/500 rate in 7 of 7 bins, so the result does not depend on the negative rates.
  - The fit still matches its training curve only loosely: 3 or 4 of 7 bins fall inside the CI, and the 0–5 s bin predicts 0.54 eggs/min against 0 observed. The 8.08 eggs/min log-link overshoot is largely built in by linearity in concentration.
  - Claims-file point (report, not correct): the statement names two models, but the criterion tests only model 1. "Reproduced" therefore covers half the statement, and the notes say so.

Assumptions:

- **fig5ab** (visit trials): stated and reasonable.
- **fig7cf** (5–10 s as the first bin past 5 s): stated and defensible. The other reading is about as plausible and flips the outcome. Both are printed, and the question is put to the authors.
- **figs2 is not marked assumed, but its outcome rests on an assumption.** The response to round 1 says "marked assumed", and the Summary (cell 121) says "(rests on an assumption)", but the outcome has no `assumed: true`. Under search trials the criterion holds (cell 111), so the outcome depends on the visit reading. It should be marked.
- **fig6ef is not marked assumed, but its outcome rests on a tie-break.** The 0–5 s bin is 0/973 against 0/1478, a tie, and it is set aside by analogy with the merge-point rule. The deviation itself says "read literally, with that bin, the criterion fails". The outcome rests on this reading, so it should be `assumed: true`.

### 2. Sentences the printed numbers do not support

- **Cell 37 and the fig2-earlier-merge notes overstate the later bins.** They say "the bins after them differ (p = 0.011 or less from 15 s on in the first, p < 0.001 from 10 s on in the second)". That holds only up to 60 s:
  - Cell 36, 0/500/500/500/200: the 60–90 s bin is p = 0.013 and 90–150 s is p = 0.051, then 0.781.
  - Cell 36, 0/500/200/500/200: the 300–600 s bin is p = 0.002 and 600–1200 s is p = 0.006.
- **Cell 115 and the figs3 notes are wrong about one bin.** They say the fraction is "above 0.89 in every bin", but in cell 114 the 0-transition bin is 0.888.
- **Cell 46 overstates the flicker conclusion.** It says "Flicker at the boundary does not explain the short medians". For the 4-mm chamber the merged median, 48.5 s, is 0.1 s below the tolerance of 48.6 s (cell 45). The sentence holds for the 2-mm and bounce chambers, but not for the 4-mm one.
- **Cell 121 and the data finding: "egg counts per group are within a few eggs of the legends".** Dop1R2-mutant-1 holds 596 eggs against 586, and D. suzukii 220 against 214 (cell 6). Only the egg-aligned counts match. This is a minor point.

All other "**Result:**" sentences, the Summary, the README (its claim counts per row add to 6+5+4+7+7+4+12 = 45 and match the record) and the record's notes agree with the printed outputs.

The verification block gives my round-1 reasons in my own words, taken from my table and the problems I linked to each claim; the cell numbers there are those of the handover notebook, as the record states. One of my own figures was wrong: in round 1 I wrote "1000 of 1031 eggs at 18 C" for fig7df, which the record carries forward as my words. 1000 is the number counted; 31 are left out, as the record's notes and cell 96 correctly say.

### 3. Round-1 points

**Resolved:**

- 1, boundary flicker: the visit-length distribution and the merged reruns are now printed. This changed fig3e.
- 2, pause and transit quantisation: now flagged in cells 51, 54 and 102.
- 3, merges on near-empty bins: now printed and discussed.
- 6, overlapping search windows: printed, 1.6% of frame counts.
- 7, short inter-egg intervals: listed, including 10 implausible end-of-recording eggs; no outcome changes.
- 8, frames before the first crossing (fig7df): the variant gives the same pattern.
- 9, the figs4 fit: the log-link fit was added.
- 12, agarose labels: resolved, and it changed three outcomes.
- 13, criteria not applied in cells: now applied.
- 4 and 5, the first-bin and trial readings: now explicit assumptions.

**Still bearing on a conclusion:**

- Point 4: fig7cf turns on which bin is first past 5 s.
- Point 5: fig5ab and figs2 turn on the trial reading; figs2 is not marked assumed (section 1).
- Point 10, claims-file reading of fig7ik "unrelated to egg number": the egg part would hold under the correlation reading (rho −0.07, p = 0.72). It is put to a reader.
- Point 11, claims-file reading of fig5c with no multiple-testing correction: with Holm, the smallest adjusted p is 0.38. It is put to a reader.
- The fig3d medians remain unexplained for the 2-mm and bounce chambers, and the question is put to the authors.
- New: fig6ef rests on an unmarked tie-break (section 1).
- New: the fig3e outcome is borderline against the paper's "~4 min".

### 4. Critical findings

No finding in the attempt record's `findings` is rated `critical`. Nothing in the printed outputs points to one. Cell 8 finds no recording deposited twice, cell 12 puts the eggs on the position clock, cells 4 and 14 show the island, sucrose and agarose labels change together, and cells 6 and 7 support the subject and group labels.
