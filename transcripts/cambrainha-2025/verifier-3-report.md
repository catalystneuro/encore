**Verification report, round 3: Cambrainha et al. 2025 on DANDI:000713 (0.240702.1725)**

The attempt record proposes a change of outcome for one claim, and this round covers only that claim. All other outcomes are as verified in round 2.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| figs3-exponents-stable-with-threshold | partially_reproduced | Yes, provided it stays marked as assumed | — | See below (cells 81, 82, 83) |

**1. The numbers come from the data (cell 81, grid from 7 to 12 under CV (a), 101 points).**
- The code applies the criterion as written:
  - The SD is the across-session SD at the start of the grid (`per[0][e].std()`).
  - A grid point counts only if at least 10 sessions contribute (`notna().sum() >= 10`).
  - An exponent holds only if it holds in every phase.
- The printed table gives these results:
  - **α and β:** within one SD in all three phases. The largest departure is 0.036, against an SD of 0.048 or more.
  - **Active μ:** within (0.122 against 0.197, at 64 points from up to 32 sessions).
  - **Active and passive z:** within (0.028 against 0.045; 0.023 against 0.047).
  - **NNI z:** fails (0.083 against 0.058).
  - **Passive and NNI μ:** no point has 10 sessions (at most 7 and 6, cell 82).

**2. The criterion is applied as written (cell 82).**
- The claims file asks for stability "at every grid point with at least 10 sessions contributing". With no such point, the condition holds vacuously. Under that reading, passive and NNI μ do not fail, so μ holds overall.
- The only failure is NNI z. Three of the four exponents hold, which is the claims file's definition of "partially reproduced".
- Counting an exponent with no evaluable point as a failure is a convention the claims file does not state. I objected to it in round 2.

**3. The choice was not made to reach the result.**
- The literal reading came from my round-2 report, not from the author.
- Under that reading, no start gives not reproduced (cell 82):
  - Partially reproduced from 7 and from the 99th percentile, under both CV (a) and CV (c), and on the variant grid from 4 to 12.
  - Reproduced from the 99.9th percentile and under CV (b).
- The outcome therefore still depends on the start of the grid (7) and on CV (a), and `assumed: true` must be kept. The `proposed` block gives only the outcome. Its reason does say the outcome rests on CV (a) and the start of 7.

**Caveats to keep in the notes.**
- Passive and NNI μ are not actually tested. Only 1.7% of windows pass the r² ≥ 0.85 rule, so the partial outcome rests partly on a vacuous condition. Cell 83 and the notes already say this.
- The NNI z failure is narrow. Its departure of 0.083 is the same at every start; whether it counts as a failure depends only on the SD at the start of the grid.

**Claims file.** I found no misreading of the paper. The paper says the exponents "remain within their respective error bars" (Supplemental Material III, Fig. S3). Using one SD across sessions as that error bar, and the 10-session floor, are the claims file's own choices; it labels the floor as such.
