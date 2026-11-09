**Round 2 verification: Yu et al. 2016 (doi:10.1038/nn.4412) on CRCNS ssc-7**

**1. Outcomes**

The claims file has 48 claims. The attempt record has 48 outcomes: 24 reproduced, 13 partially reproduced, 6 not reproduced and 5 blocked (data_missing). Four outcomes are marked `assumed: true`: behavior-performance, fs-touch-spikes, thalamus-inhibition-l4e-vm and enphr-auc.

My round-1 count line ("17 / 15 / 11 / 5") was wrong. My own round-1 table gives 25 / 13 / 5 / 5.

I agree with all 48 outcomes, with one caveat on enphr-behavior. Three outcomes changed since round 1, and I agree with each:
- **l4e-reversal-potential → reproduced.** With Vm after a later touch set to NaN, as M-EPOCH asks, the median whisking reversal is 4.9 mV above rest, inside the 5 mV margin. Cell 78 also gives p = 2.6e-5 and 34 of 35. The margin is very narrow, and the record says so.
- **ion-cut-l4e-whisking → partially reproduced.** The control mean is 1.337 against a bound of 1.34 (cell 96). No reading has both means within tolerance.
- **enphr-auc → not reproduced.** Cell 129 gives p = 0.16 (reading a) and 0.09 (reading b).

l4e-example-e24-e32 is now reproduced, as I gave it in round 1.

The four assumptions:
- **behavior-performance:** stated and reasonable. The outcome does not depend on it: under the "config" variant Go touches are 5.93 (within) but Nogo is 0.63 and reaction time 334 ms (both outside).
- **fs-touch-spikes:** stated and reasonable. The FS touch responses support taking series 1 as the principal whisker.
- **thalamus-inhibition-l4e-vm:** stated and reasonable. The rule as written gives 0 ms at the light step. The smoothing grid in cell 114 shows the thalamic latency is always longer, and both latencies are never within tolerance together.
- **enphr-auc:** stated, and reasonable because it matches `touch_table`. But the outcome depends on it entirely: keeping the passive first touches gives ρ = −0.34, p = 0.038 under reading (b), which would be reproduced. The claims file's M-ROC says only "the first touch", so both choices are defensible.

Two assumptions are not marked:
- **enphr-behavior** rests on the recording sessions being the paper's Supplementary Fig. 14 behaviour sessions. The record raises this only as a deviation. The evidence that they are not the same sessions is real:
  - 9 mice against the paper's 8.
  - Light falls in 23–48% of Nogo trials, against the legend's "small subset of trials".
  - No session matches the example.

  This should be `assumed: true` at least, and arguably blocked (data_missing or metadata_insufficient).
- **fs-touch-vm**, and the other cortical touch measures, rest on the same series-1 choice as fs-touch-spikes but carry no flag. It was not run under "config". The risk to the outcome is low: only one FS whole-cell neuron (JY1171) changes series.

**2. Sentences the printed outputs do not support**

- **Cell 34, and the fs-touch-spikes notes:** "Three of the five values hold under either edge." At the bin centre four of five hold (cell 33: spikes per touch mean and median, latency median 4.5, n = 25). The outcome is unchanged.
- **Cell 4:** "Seven VPM sessions come from one mouse (ANM199552)." Cell 27 shows 7 units in 6 sessions (two units share 20130608). The record's "Seven units" is correct.
- **Cell 0:** the stream takes "about twelve to fourteen minutes", but cell 1 prints 510 s. The README's "about twenty minutes" is not shown anywhere.
- **Cell 46:** "both medians (0.09 and 0.21) are within tolerance." This holds only under rate reading (a). Under (b) the nonwhisking median is 0.116 to 0.121, which is outside.
- **Cell 70:** the long latencies come from "neurons with small PSPs". No per-neuron amplitudes are printed. Four latencies of 0.0 to 1.4 ms, faster than VPM, are not flagged.
- **Summary (cell 142):** "The order of `whisker_configuration` does not give it." This is true for FS (cell 5). For several L4 E neurons the "config" series gives the larger touch response (JY1345 0.857 vs 0.235; Exp_2015-09-04_001 0.42 vs 0.058; Exp_2015-08-28_003 0.372 vs −0.248).
- **Summary:** "enphr-auc reproduces only with those touches kept." This is shown for reading (b) only; reading (a) with those touches kept is not printed.
- **Record finding paper_inconsistency:** "direct cortical activation 8 or 9". The notebook prints only 8 (cells 105 and 114).

Everything else in the Result cells, the summary, the README and the record notes matches the outputs, including the outcome counts and the README table.

The verification entries give my round-1 reasons verbatim for all 48 claims. `agrees: false` appears only for l4e-example-e24-e32, which is correct.

**3. Round-1 points**

Resolved:
- **1 (distance to threshold):** variants and per-neuron slopes are printed. The outcome stays partial under every reading of the paper's method.
- **2 (principal whisker):** the L4 E rows are printed and the L4 E claims were rerun; no outcome changes.
- **3 (blocked Fig. 3 evidence):** ephys trial counts match the whisker trials, JY0978 tops out at −66 mV, JY1139 is shown to be a drift, and the 2 nA current belongs to JY1171.
- **4 (M-LIGHT reading d):** run.
- **5 (latency windows):** the grid is shown.
- **6 (cell 45 tolerance):** applied.
- **9b (enphr-auc bias):** the split-half check gives ρ = 0.02.
- **11 (the 43 eNpHR neurons):** listed against the cell list.
- **12 (passive touches, NaN after a later touch):** both fixed.
- **14 (fs-hf chance level):** about 1.0 of 7 neurons by chance.
- **C items:** trial-type columns, pole times and the depolarized-trial check are all printed.

I was wrong in round 1 to say point 12 did not affect a conclusion: its two fixes changed three outcomes (enphr-auc, l4e-reversal-potential, ion-cut-l4e-whisking).

Partly resolved: 7 (the VPM median latency of 1 ms against 2.5 ms is still unexplained, and stated as such) and 13 (the forward-difference check is quoted but not run in the notebook). Neither changes a conclusion.

What still bears on a conclusion:
- **enphr-behavior (point 10):** the outcome rests on an unflagged assumption about which sessions these are. It should be `assumed: true`, or blocked.
- **enphr-auc:** the outcome flips with the passive-touch choice. It is stated and flagged, but it is knife-edge.
- **Narrow margins:** l4e-reversal-potential (4.9 against 5 mV) and ion-cut-l4e-whisking (0.003 mV outside) sit on their margins. Both are stated.
- **Claims-file issues, which I report and do not correct:**
  - **ion-cut-l4e-touch (point 8):** the peak-minus-baseline amplitude is tested against zero. Random times give 0.208 mV, and touch does not differ from them (p = 0.148).
  - **thalamus-inhibition-dose (point 9a):** the test mostly compares light with no light. Among light trials only, a dose effect appears in 1 of 3 epochs.

  Both are now asked of a reader.
- **fs-touch-vm:** it rests on the series-1 choice without a flag. The risk is low.
