**Verifier report, round 2: Elie & Theunissen 2019 on CRCNS aa-4**

The claims file has 26 claims and the attempt record has 26 outcomes. 20 are blocked as methods_underspecified, 5 are blocked as data_missing, and 1 is partially_reproduced. No outcome carries `assumed: true`. I found no place where the claims file misreads the paper. The Fig 1 "approaches the maximum possible value (2 bits)" is in the Results text, and "min = 9, max = 11" trials and "114 (sd = 22, min = 34, max = 123)" stimuli are in the Methods.

### 1. Outcomes

| claims | record | agree? |
|---|---|---|
| units-404 | blocked, methods_underspecified | Yes. Cell 12 finds 1281 files labelled single, 1246 of them auditory, and confirms the description's 1401. Cell 14 shows that an SNR above 5 leaves 461 (reading A) or 274 (reading B) units, not 914. No list of the 404 exists anywhere in the materials. Both SNR readings follow the description's wording. The record says the main cause is the missing labels, which is fair. |
| units-337, s1, fig2a, fig2cd, fig2b, s2, and the 12 claims that depend on units-337 | blocked, methods_underspecified (too_large also named for the units-337 group and fig2a) | Yes. |
| fig3-5-example-neurons | blocked, methods_underspecified | Yes. Cell 30 states that the S4 to S6 images were not available. |
| table1-anatomy-counts and the four fig10 claims | blocked, data_missing (changed from my methods_underspecified) | Yes, the change is reasonable. Cell 12 lists every root attribute of the files and cell 16 lists every dataset in `class_info` and `extra_info`; none holds an area or a coordinate. Two small gaps remain: the attributes of groups under `class_info` and `extra_info` are not listed, and only selected attributes of the stimulus groups are read. The dependence on units-337 is stated. |
| fig1-model-neurons | partially_reproduced | Yes. Cell 28 runs the paper's procedure and gives a mean \|KDE − model\| of 0.009 spikes/ms. The cumulative information reaches 1.982 bits (last bin 1.884). The peak instantaneous information is 0.520 bits. The MATLAB tutorial's saved results agree (1.981 and 1.894). Only one of the three model neurons is available. |

### 2. Text against the printed outputs

The "**Result:" cells (17, 29) and the Summary (31) are supported by the outputs, with one imprecision. Cell 29 and the fig1 notes say the model rate gives "cumulative 1.956". In cell 27 that is the last bin; the largest value is 1.990, at 340 ms. The conclusion does not change.

These statements are not supported:
- **Entry README:** "Claims on the 404 and 337 units (…; 19 claims)". The record has 18 such claims. With them, the README's rows add up to 27, not 26.
- **Attempt record, notes on units-337 and the 12 claims that depend on it:** "(118 to 120 h in three runs)". The re-executed cell 19 prints "117 h on one core". The "more than 100 hours" holds.
- **Attempt record, fig1 deviations:** "its rows sum to the observed spikes per trial (11.8 against 12.1 for stimulus 1)". 12.1 follows from cell 27 (121 spikes over 10 trials), but no output prints 11.8.
- **Cell 10:** this text is not a conclusion, but it does not match the cell 9 output above it, which suggests it is left over from an earlier run.
  - "0.9% to 1.9%": the printed values before onset are 0.5% to 1.3%.
  - "about 6.1 spikes/s": printed 6.33 to 6.41.
  - "44% to 66%": printed 42.2% to 65.3%.
  - "rises to 22 spikes/s": printed peak 23.30.

  The conclusion that the clock is aligned still holds.

**Round-1 reasons in the record:** they are in my words, condensed, and my problems B1 to B8 are attached to the relevant claims. One omission: the fig1 reason leaves out my statement that the conclusion stood anyway because the MATLAB results agreed. That does not misrepresent me.

### 3. Status of round-1 points

All are resolved:
- **B1 (snippet files):** the files are read and the SNR is computed (cell 14). All 42 snippet files are listed, and every site has one for its call protocol.
- **B2:** the count of 1401 is confirmed (cell 12).
- **B3 (anatomy):** `class_info` and `extra_info` are now listed (cell 16), with the small gap noted in section 1.
- **B4:** call stimuli now come from the call protocol only, and no stimulus appears in two groups of a unit (cell 4).
- **B5:** `cum_info_mc` now matches exact enumeration to 0.0034 bits for stimuli and 0.0019 for categories (cell 25).
- **B6 (fig1 procedure):** fixed by cell 28; see the note below.
- **B7:** the coherence variant is now stated to say nothing about the paper (cell 23).
- **B8:** too_large is now named as a blocking reason (cell 20).

From my round-1 section C, the fig3-5 statement has been added.

On B6: cell 28 uses an adaptive sample size, 20 bootstraps of the jackknife and the 0.6-bit stop. The record cites the code for the shared random numbers. I could not see the code, but the per-bin agreement with the MATLAB saved results supports it. The Fig 1 legend's "the Monte Carlo simulations were repeated for each jackknife estimate" could be read as independent draws. The record's "other" finding notes that the text is silent on this.

Nothing left bears on a conclusion. What remains is the text fixes listed in section 2.
