**Verification report, round 2: Watters et al. 2026 on DANDI:000620 (version 0.261019.2000)**

Counts come from the files. The claims file has 26 claims, and the attempt record has 26 outcomes, one per claim:
- 7 reproduced;
- 5 partially_reproduced;
- 1 blocked as methods_underspecified;
- 13 blocked as too_large.

Only ext1-misbinding-errors carries `assumed: true`. The record's round-1 verification lists 26 results, and only ext3c is marked `agrees: false`.

### 1. Outcomes

I agree with all 26 stated outcomes.

| claim | agree | comment |
|---|---|---|
| fig1b, fig1c, triangle-unit-counts, ring-unit-counts, ext2, fig5ab | yes | Each holds under every reading and radius the criterion asks for (reproduce cells 8, 11, 17, 22, 26). |
| ext1-misbinding-errors (assumed) | yes | The assumption is stated in the deviations and is reasonable: every trial with an error under 0.2 arena widths was rewarded and none above (cell 4). Under the Methods' radius, Monkey P with 2 objects fails (0.449, cell 14). |
| fig2b, fig5cd | yes | Identity's top decile is ≤0.700 in Monkey E and in P under the Methods p-value (cell 31). In the Ring, identity fails for both monkeys and position fails for E (cell 34). |
| fig2d (methods_underspecified) | yes | Under the code variant, E's lowest bin is 0.0245 (−0.0327 to 0.0818) even with intervals clustered by pair (cell 38). |
| fig5e | yes | E's bins overlap under both readings, with and without clustering (cell 41). |
| ext3ab | yes | Position passes in 3 of 3 sessions and identity in 0 of 3, under both readings (decoding cell 8). |
| ext3c | yes, with a caveat | The Triangle neural medians are 106.7 / 106.6 (decoding cell 11). In the delay phase all three sessions are above 105 (105.3–110.7), so the 20-unit session does not cause the failure. **The Ring pass, though, depends on the code's sigmoid output.** With the linear output the Methods describe, the Ring neural medians are 140.2 / 142.1 (variants cell 11). Neural data would then fail in both datasets, which by the criterion is not_reproduced. The outcome rests on choosing the code over the Methods, so it should carry `assumed: true`, as ext1 does. |
| 13 too_large | yes | The data are complete and there is no GPU. Even at 100× speed the printed estimates are 3.0–54.0 h, all over the 60-minute notebook limit (cell 44). |

**Unflagged label choice.** For fig2b, fig5cd, fig5e and ext3ab the criterion defines only a "reproduced" case, so "partially" is the author's label (and mine in round 1). Only ext3c's notes say so; the other four should state it too.

**Claims-file reading (reported, not corrected).** Two points:
- The ext3c statement is about synthetic data ("orthogonality resulted even on synthetic data"), and that part holds in both datasets. The requirement that the neural data also be near 90° is the claims-writer's reading. It is defensible because of the word "even", but it is what makes the outcome partial.
- The Methods call this panel "Extended Data Figure 3b", while the legend calls it (c). The claims file follows the legend.

### 2. Sentences the printed outputs do not support

The decoding prose looks as if it came from a different execution than the outputs saved in the notebooks.

**Decoding notebook**

Cell 9 (ext3ab):
- It says identity is "46.7% (2022-05-31), 50.0% … against 30.5%, 34.2% and 30.8% shuffled, above control in all ten splits only in 2022-05-31 and by two standard deviations only in 2022-06-01". Cell 8 prints 46.2 against 32.4 and 50.0 against 37.5, and "identity: reading (a) in 0 of 3 sessions, reading (b) in 0 of 3". Both rows are False/False.
- It gives shuffled position as "32.1% to 33.3%"; cell 8 prints up to 33.8.
- It gives training accuracy as "92.6% against 86.1%, 84.9% against 82.3%"; cell 8 prints 92.5 against 89.5 and 82.7 against 84.1.

Cell 12 (ext3c):
- "medians 91.8 to 96.5": cell 11 prints up to 96.7.
- "Orthogonal data's 90.7 to 95.1": cell 11 prints 90.8 to 95.0.
- "106.6 degrees in both phases": cell 11 prints 106.7 (delay) and 106.6.
- "15.6 and 15.9 degrees": the printed values give 15.7 and 15.8.
- "stimulus phase passes (99.2)": cell 11 prints 99.3.

**Variants notebook**

Cell 9:
- "absent identity … 32.6% to 43.8%": cell 8 prints a maximum of 43.5.
- "as with rates in Hz": this contradicts the 0 of 3 in decoding cell 8. The same applies to the Summary row "as with the code's inputs".

Cell 12:
- "Triangle neural data move to 95.2 (delay) and 97.6": cell 11 prints 96.1 and 98.5.
- "Ring neural data (98.8, 102.0)": cell 11 prints 99.1 and 101.6.
- "Receptive Field data (102.0, 102.3)": cell 11 prints 102.0 and 102.2.

**Main notebook**

Cell 45:
- "0.983 s, printed above", "about 2.7 h", "about 262 days", "240", "87", "246", "15 days" and "3.5 h … to 62.9 h" are all unsupported.
- Cell 44 prints 0.843 s, 2.3 h, 225 / 206 / 75 / 211 / 12 days, and 3.0–54.0 h at 100×.

Summary: "one fit is 2.4 h here" is unsupported; cell 44 prints 2.3 h.

**Attempt record**

- ext3ab notes: the shuffled values "32.9%, 33.3%" should be 33.8 and 33.3. The identity values "50.0%, 46.7%, 30.0% against 34.2%, 30.5%, 30.8%", "above control in all ten splits only in 2022-05-31 and by two standard deviations only in 2022-06-01", the training "84.9% against 82.3%, 92.6% against 86.1%", and "identity is again above control in one session" all fail against cell 8.
- ext3ab response: "In the re-run identity is above control in all ten splits in 2022-05-31 … 2022-05-31 shuffled identity 30.5% in place of 32.4%". The saved output still shows 32.4 and 0 of 3.
- ext3c notes and response:
  - The Receptive Field values "92.0 … 96.5 and 96.0" should be 91.9, 91.8, 96.4 and 96.7.
  - The Orthogonal values "91.0, 90.7, 92.4, 95.1" should be 91.0, 90.8, 92.5 and 95.0.
  - "93.3" should be 93.2, "106.6 in both phases" should be 106.7 / 106.6, and "99.2" should be 99.3.
  - For the z-scored variant, "95.2 and 97.6" should be 96.1 and 98.5. "102.0 to 102.3" should be 101.6 to 102.2. "98.8" should be 99.1.
- The 13 too_large notes and responses: "0.98 s", "2.7 h", the day counts and "3.5 to 62.9 h" do not match cell 44. Their "far over … the run's 5 hours" is true only at 1× speed: at 100×, nslots is 3.0 h.

None of these changes an outcome.

Everything else checks against the outputs:
- the other "**Result:**" cells, the two Summaries and the README;
- the notes for fig1b, fig1c, ext1, the unit counts, ext2, fig2b, fig5ab, fig5cd, fig2d and fig5e;
- the findings.

**Round-1 reasons.** The record states them faithfully and in my own words, spread across the claims. One correction to my own round 1: I wrote that at 100× speed the claims "would still take days", but nslots comes to 3.0 h. The verdict is unchanged, because 3.0 h is still over the 60-minute limit.

### 3. Round-1 points

**Resolved**
1. **Input normalisation.** With z-scored inputs, identity still fails 2 of 3 sessions under each reading (variants cell 8). I cannot check the author's statement that `dataset.py` comments out the normalisation, but the variant settles the question either way.
2. **Simultaneity filter.** The filter counts and per-session medians are now printed. The Triangle delay-phase failure holds without 2022-06-04. The stimulus-phase failure does depend on that session (99.3 without it), and the notes say so.
3. **Ordered pairs (fig5e)** and the clustered fig2d intervals: clustered intervals are now shown, and no outcome changes.
4. **Cost cell.** The config is now cited, the GPU check is printed, and the 100× case is shown. The prose numbers are wrong, as listed in part 2.
5. Points 5, 7 and 8 are recorded; the ext3ab identity question has gone to the questions file.

**Remaining, bearing on a conclusion**
- **Decoding prose against outputs.** The ext3ab and ext3c conclusions, the variants conclusions and the record's notes and responses quote numbers, and for ext3ab a qualitative result (identity passing in 1 of 3 sessions), that the saved outputs contradict. Either re-run the notebooks so the saved outputs carry the quoted numbers, or rewrite the prose from the outputs.
- **ext3c's dependence on the sigmoid.** The Ring half passes only with the code's sigmoid, whose outputs cannot reach the negative Ring targets. With the Methods' linear decoder, neural data fail in both datasets. This should be marked `assumed: true`, with the reason stated.
- **Not checkable by me.** Whether `wm.py` matches the paper's code still rests only on the author's word: the greedy filter, the sigmoid on the Ring decoders, the commented-out normalisation and the ordered pairs.
