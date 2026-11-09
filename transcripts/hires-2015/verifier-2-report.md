# Round 2 verification report: Hires et al. (2015), eLife 4:e06619, on DANDI:000013 (0.220126.2143)

## 1. Stated outcomes

The claims file has 45 claims and the attempt record has 45 outcomes, one per claim, with no claim missing or extra. They are 22 reproduced, 1 partially reproduced, 8 not reproduced and 14 blocked (all methods_underspecified). The Summary in cell 151 gives the same counts.

**I agree with all 45 outcomes.** Six of them differ from what I said in round 1, and I now accept them:

- **example-cell-ff-around-touch, blocked.** I said reproduced in round 1. Cell 127 now shows that pooled touches give no matching cell in 62 units, and grouped touches give a match only for cell 11, in 2 of 394 units. The two readings of the touches therefore give different outcomes. Two matches out of about 400 tries could also be chance.
- **table1-l4-outside, blocked.** I said not reproduced. Under the criterion's readings, 52 combinations give not reproduced and 12 give partially reproduced (cell 60).
- **fig5-modulation-correlations, blocked.** I said partially reproduced. The claim holds in 16 of the 64 inherited fig5c readings and fails in 48 (cell 120), and the criterion has no rule for a partial result.
- **fig3c-touch-spikes-outside, fig3d-touch-phase-outside and fig4a-touch-detection-outside, blocked.** These are blocked because they depend on a blocked claim. The record states this as a protocol rule; I could not check it, because docs/protocol.md is not among my materials. On their own criteria:
  - The fig3c and fig3d outside claims fail under every reading: 0 of 32 (cell 87) and 0 of 64 (cell 95).
  - fig4a-touch-detection-outside holds under every reading (cell 105).
  - fig3d-phase-only, also blocked by dependency, holds in 32 of 32 (cell 99).
- **fig4c-phase-decoding, not reproduced.** In round 1 I said blocked. Every reading now fails, with C2 never better than outside C2 (cell 113). One point about the claims file, to report rather than correct: its criterion literally says "else methods_underspecified", which would block any result that is not reproduced. The record reads that phrase as the rule for readings that disagree. That is a reasonable reading, but it is not the literal text.

## 2. Sentences the printed numbers do not support

**These affect a conclusion's text, but not its outcome:**

- **Cell 72 (l5-higher-rates).** The sentence "L5 medians are 12.90 spikes/s outside whisking and 10.96 (11.33 with touch epochs) during it, against 0.32 and 0.86 (2.28) for L4 C2 and 1.09 and 1.75 (1.78) for L4 outside C2" quotes the earlier mask, which is now only a variant. Cell 71 prints the criterion's values: 12.82 (11.52), 0.38 (2.27) and 1.46 (1.54). The attempt record has the right numbers.
- **Cell 75, and the attempt record's notes for phase-mod-l4-inside-outside.** Both say "with the cycles counted only in exploration time p = 0.971". Cell 74 prints p = 0.798.
- **Cell 114 (fig4c-phase-decoding).** "C2 reaches it at 102.8 deg (random shifts) or 98.2 deg (even shifts)" overstates the result. Only 42 and 38 of the 100 runs reach 76% correct (cell 113, `runs_reaching`), and the median is taken over those runs alone. In most runs, C2 never reaches 76%. The outcome does not change.

**Minor:**

- **Cell 40.** "The next nearest cell is four times farther in the scaled distance (5.38 against 1.10)": the ratio is 4.9.
- **Cell 151 (Summary).** "The Figure 6E Fano factors come out as the paper's to two or three digits": this holds for three of the five conditions. The 10 ms touch FF is 0.70 to 0.86 against 0.73, and the similar-touch FF is 0.50 to 0.69 against 0.54 (cells 144 and 146).
- **README.** "It takes about twelve minutes, two of them streaming the files": the notebook ran in 8.8 min (cell 152), with 43 s of loading (cell 2).
- **README.** "the Figure 3 claims stay blocked on the range of the cutoff curve (100 or 200 ms)" is true only of fig3c-touch-spikes-l4c2. For fig3c-touch-spikes-l5 the readings also disagree within each range, 2 of 4 passing at 100 ms and 2 of 4 at 200 ms (cell 89). For fig3d-touch-phase-l4c2, 1 of 8 readings passes at 100 ms (cell 93).
- **README.** "the spike train's timestamps run 10 ms ahead of the voltage" is ambiguous. Cell 7 and the findings say the SpikeTrain timestamps are 10 ms *before* the voltage timestamps.
- **Attempt record, fig4a-touch-detection-c2 response.** "the same synthetic test now gives 0.15": no printed output shows this test.

**Checked and supported.** Every other "**Result:**" sentence and the rest of the Summary, README and attempt-record notes match the printed outputs. These include the Table 1 counts (cells 58 to 62), the fig3, fig4a, fig4b, fig6d and fig6e figures, the per-cell windows, and the findings on clocks, voltage, theta_filt and pole_position.

**My round-1 reasons in the record.** The verifications block states my round-1 reasons faithfully and in my own words. My round-1 problems (whisking mask, threshold rule, sample-epoch cycles, `n_ok`, clock, repetitions, negative reaction times, five groups, and the claims-file points) are attached to the claims they concern. Problems referenced by number (for example in table1-l4-c2) are defined in other entries of the block.

## 3. Status of my round-1 points

- **1. Whisking mask: resolved.** Whisking now leaves out licking cycles and the 70 ms after each touch (cells 13, 51 and 79). As a result, whisking-rate-l4-no-change is now correctly blocked.
- **2. Touch-detector threshold rule: resolved.** The fraction detected is now taken at the time point of best percent correct, ties are broken at the middle threshold, there are 50 repetitions, and the N = 1 performance is printed (cells 102 to 105).
- **3. Phase cycles restricted to the sample epoch: resolved.** Phase tuning now uses every phase-analysis cycle of the trial. One effect remains: the cosine fit with a non-negative baseline is biased upward on sparse counts.
  - 12 of the 27 L4 C2 cells with a fit sit at depth 1, and the median is 14 spikes per cell.
  - The depth median is 0.859 over all cells but 0.444 over the cells with at least 20 spikes.
  - No outcome changes. The Table 1 depth median fails either way. The phase-modulation tests hold under every variant: p = 0.584, 0.934 and 0.798 for inside against outside C2; 8e-5 and 0.0043 for L4 C2 against L5.
- **4. `n_ok` in the Table 1 cell: resolved.** The two zero-median checks are now counted, and the count is out of 17 (cell 57).
- **5. Clock offset: partly resolved.** Per-file touch-peak latencies are now printed (cell 9). The residual 4 ms is stated as unexplained. It bears on no conclusion.
- **6. Repetitions: resolved.** Raised to 50.
- **7. Negative reaction times: resolved.** A variant without them is shown (cell 36).
- **8. Five touch groups: resolved.** Stated in the fig6s1b-clusters-less-variable notes.
- **9. Claims-file points: recorded, not changed,** as the protocol requires.

**What remains that bears on a conclusion:**

- **latency-determinable** (not reproduced). The claims file's rule of mean plus two s.d. over sparse 1 ms bins gives noise latencies, and these count as "determined": cells 36 to 38 get 0 ms from all touches and cell 40 gets 1 ms from first touches (cell 65). The 7 and 10 cells with a latency, against the paper's 4, may reflect the rule rather than the data.
- **table1-l4-c2** (reproduced) sits exactly at its threshold, 15 of 18. One value moving would change the outcome.
- **fig4c-phase-decoding** (not reproduced). The reported C2 resolutions are medians over the minority of runs that reach 76% correct. This does not change the outcome, but the conclusion text should say so.
- **The cell 72 and cell 75 / attempt-record number errors** above need correcting. They are wrong text, not wrong outcomes.
