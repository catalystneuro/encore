**Round 2 verification: Claar et al. 2023 (eLife 84630) on DANDI:000458 v0.230317.0039**

The claims file has 37 claims and the attempt record has 37 outcomes: 12 reproduced, 12 partially reproduced, 7 not reproduced and 6 blocked. Cell numbers below are 0-based indices into `claar_eeg.ipynb` ("EEG") and `claar_spikes.ipynb` ("spikes").

## 1. Outcomes

**Agreed: 35 of 37.** On these, the outcome follows from the printed outputs and the claims-file criterion. Four of the passes are fragile:
- **fig1-supp1, fig1f, fig8b:** they pass only at the medium current. That is a reading the claims file allows, and the near-exact example match (1.011 s and 11.133 SD·s against 1.01 and 11.13, EEG cell 19) supports it.
- **fig2c-superficial-quiescence:** it rests on 2 sites. Under reading (b) the per-site values are 0 and 64 ms (spikes cell 34), so the in-tolerance mean averages a site with no zero-rate period and one with 64 ms.
- **fig8e:** 1 of 8 combinations passes (medium current, first trials, the 8 sites with all four stages). See the open points in section 3.
- **fig4-unit-counts and fig5c:** both outcomes are correct on the claims file as written. The disputed parts are the claims file's (unit × current counting; a tolerance of exactly 0) and are correctly referred to a reader.

**Disagreed: fig3abc-decay-with-distance and fig3d-magnitudes (blocked, metadata_insufficient).**
- The record itself says the single-session LFP/CSD pipeline "was not built within this run's time", and that fig3d exceeds a runtime limit.
- Those are effort limits, not missing metadata. The layer-1 exclusion could be a stated deviation, and `probe_vertical_position` is in the electrode table (EEG cell 3). fig3abc covers one session.
- The 80-minute estimate behind fig3d (1.7 s per 50,000 samples) is not in any notebook output.

**Assumptions (`assumed: true`).** Only fig7f and fig7g carry the flag, for responsive units taken from all awake trials. It is stated in the deviations and notes, and it is reasonable, since per-state selection leaves 3 animals. The fig7f pass is still weak:
- It rests on 6 to 8 animals against the paper's 13.
- The state effect has p = 0.08 to 0.20 at the high current.
- The SM-TH confidence interval of the paired state differences spans −7.5 to +2.4 ms, against latencies of about 9 ms (spikes cell 63).

## 2. Statements the outputs do not support

**EEG notebook**
- **EEG cell 0:** "Neuropixels LFP and sorted units in 19 sessions." EEG cell 3 shows 18 sessions with probes and units, and spikes cell 1 prints "18 sessions with units".
- **EEG cell 13, three sentences:**
  - "after the masked samples (for example 586466 SSp-deep, 326 uV at k + 1 …)". Sample k+1 is inside the mask, which covers k−1 to k+4 (`claar.py` lines 241–243). The k+5 value of 129 µV would support the sentence; 326 µV does not.
  - "The paper's 2 ms mask does not remove this either." This is not shown. The pre-onset spread comes from the zero-phase filter, which is the attempt's own choice.
  - "the early peaks (at 6 to 31 ms) lie after it." This is not shown. The raw EEG is still raised at k+10 (4 ms) at several sites (for example 551397 at 187 against 50 µV, 569064 at 151 against 60 µV), and the post-onset residue is not separated from the signal.

**Spikes notebook**
- **Spikes cell 4:** "Unit z coordinates (… midline about 228 …) are all on one side." The printed z ranges reach 251 to 253 (586468, 590479, 590480; spikes cell 3).
- **Spikes cell 4:** "median about 0.55". The printed median is 0.577.
- **Spikes cell 12:** "two superficial non-stimulated groups … with medians of 0.10 and 0.20". Spikes cell 11 prints 0.10 and 0.29.
- **Spikes cell 37 and the record (fig2c-deep):** "Quiescence below baseline lasts 108.7 to 135 ms". The largest value printed for quiescence (a) is 131.9 (spikes cell 36).

**README**
- "which blocks five claims". The record blocks six: stim-depths, fig1-supp2, fig3abc, fig3d, fig6a and fig6-supp1.
- "counting each unit once per current gives the legend's counts". This is exact for three counts; the fourth is 9486 against 9363 (spikes cell 14).
- "sorted units of 23 mice". Units exist for 17 mice (18 sessions).

**Attempt record**
- **fig6-supp2 notes:** "The electrode reading of the late ERP gives the same pattern." None of the 4 electrode rows meets the criterion: 12/13 sites with r = 0.424 at the high current, and 11/13 at the medium current (spikes cell 58).
- **fig8b deviation:** "checked on four sites in the notebook". EEG cell 10 checks all 30 sites, on ERPs decimated by 10.
- **fig4cf notes:** "the high current gives 15 of 16". Two rows give 16/16 (spikes cell 24).
- **fig6c measured:** 0.217, where spikes cell 56 prints 0.218.
- **fig3abc and fig3d notes:** the LFP timing figures do not appear in any output.

**My round-1 reasons in the record.** They are stated faithfully and in my own words. The fig1f entry cites "(problems 4 and 5)"; problem 5 is my own mis-reference from round 1 and belongs to fig7f.

## 3. Round-1 points

**Resolved**
- **Problem 4:** reading (b) of magnitude is dropped as a basis. fig1f now passes on reading (a): 3.03 and 5.86, p = 0.035.
- **Problem 5:** confidence intervals of the paired state differences and the low power are now stated for fig7f.
- **Problems 6 and 2 (procedurally):** both were referred to a reader. For problem 2, the pooled-current fractions are also shown, and they still fail.
- **Problem 7:** "first" trials now take the earliest awake trials in time; the code sorts the awake trials by onset.
- **Problem 9:** quiescence that ignores gaps under 5 ms, and a triphasic flag needing 10 ms below baseline, were added.
- **Problem 10:** non-stimulated fractions pooled per session are now printed.
- **Problem 11:** fig8d now runs per animal.
- **Problem 12:** the artifact profile now prints for all 30 sites.
- **Section C items:** PCIst is checked against the original code on 30 sites with zero difference; the fig5f line (3 of 128) and the per-area table print in full; EEG coordinates and table columns print; fig8d matched trials (41 and 45 per state, against 51) print.

**Partly resolved, still bearing on conclusions**
1. **Artifact (problem 1).** The k−1 sample is now masked, and all metrics were re-run. A residue remains:
   - The GFP reaches |z| = 2 to 21.8 between −20 and −2 ms, and is above 10 at 11 sites (EEG cell 12).
   - That window lies inside the GFP z-score baseline (−2 to 0 s) and the PCIst baseline (−0.8 to −0.002 s). It inflates the baseline SD at those sites, which lowers durations and magnitudes.
   - The effect is not measured. Values that sit at tolerance edges could move: fig1e (superficial 0.02 s below), fig7d (isoflurane 0.07 below), and fig8b, fig8d and fig8e.
2. **fig8e (problem 8).** The outlier is explained: 546655 MOs-deep is matched on 1 trial at the high current. But:
   - There is no minimum trial count.
   - That site is in the 8-site, four-stage sample of the one passing reading.
   - The medium-current per-site PCIst and matched counts, which decide the outcome, are not printed.
3. **fig3abc and fig3d (problem 3).** The LFP and CSD parts are still not run (section 1). The spiking magnitude integrates the signed z-scored rate (`spiking_magnitude`), so the 100+ ms suppression cancels the excitation. That likely explains the AUC below 0.4 SD·s against the paper's 30.9. The record's notes present these numbers ("no stimulated group is significantly above zero") as a result on the paper's claim, though they more likely reflect a different method.
4. **fig4-unit-counts (problem 2).** The outcome depends on the reader's answer. Counting each unit once per current (unit × current) reproduces 870, 4110 and 2559 exactly and 9486 against 9363.
