**Round 2 verification: steinmetz-2019-01**

**1. Outcomes**

The claims file has 40 claims. The attempt record gives 40 outcomes: 26 reproduced, 1 partially reproduced, 10 not reproduced and 3 blocked. In round 2 the kernel model was run, so nine of the eleven kernel claims are now tested.

I agree with every outcome as the claims file's criteria decide it. Some come with conditions:

- **Agree, with no further comment:** the 6 behaviour claims, passive-no-movement, recording-counts, task-modulated-fraction, fig2de, the fig5c–ed7f group (4 claims), the 6 engagement claims, ed7b, fig4d-no-lag, fig3c, fig3e (partially reproduced) and fig4f.
- **suppfig2, fig2fg, fig5b (not reproduced):** agree. The criteria give no partial outcome. fig2fg's condition (iii) fails by more once the two Miss sets are matched (cell 49). fig5b fails only because 36 sessions are kept, not the required 34 (cell 52).
- **fig4d-jpecc-vis-leads (reproduced):** agree, but weakly. The VIS–Midbrain lead rests on a single point at 0.08 s, under trials reading b only. With Bonferroni correction it survives only with baseline a and trials b (cell 95).
- **fig4b, ed4f, ed5h, fig4fg, ed7c (not reproduced):** agree under the criteria, with two cautions.
  - The model lets only 2,886 neurons into the nested tests, against about 4,240 in the claims file. Every count of kernel-requiring neurons is therefore lower, so these failures may come from this attempt rather than the paper. The record says so.
  - ed5h turns on one neuron in one shuffle with one seed. 4 of 2,871 passed; the lower bound of 0.16% needs 5 (cell 118).
- **fig4c, ed5g (blocked_by: other):** agree they are untested. But the obstacle is neither the data nor the size: the whole notebook ran in 1,234 s (cell 127), well under the 60-minute limit. The decoding was simply not written. The record says this honestly.
- **histology (blocked):** agree.

**Assumptions (`assumed: true`)**

- **edtable1 and supptable2:** stated and reasonable. Finer labels are mapped to their parent region in the Allen hierarchy. Labels as given are run as a variant: edtable1 drops to 33 of 42 regions (partial) and supptable2 to 25 of 39 sessions.
- **fig3d:** stated and plausible. Under the Figs. 3 to 5 set, the legend's rule of "fewer than 5" would exclude no region, which argues for the nested-test neurons as the denominator. But the outcome flips with this choice. VISrl gets into the top five on 3 of 5 neurons. And the method text still names the other reading as the main one: cells 105, 108 and 114 call the Figs. 3 to 5 set the denominator, while the code and cells 107, 110 and 116 use the nested-test neurons. The analysis should state one reading and keep to it.

**Where the claims file may misread the paper (reported, not corrected)**

- **fig5b:** the criterion makes a claim about activation fail on a session count (34) taken from the Methods.
- **fig5d and ed7f:** the neuron set is still with a reader. It no longer changes either outcome.

**Where the analysis departs from the claims file**

- **fig5b, neuron reading b:** the claims file asks for all neurons of the 42 regions at ≥ 0.1 Hz; the notebook uses neurons N (cell 52). This does not change the outcome.

**2. Sentences the printed outputs do not support**

- **README:** "It takes about 17 minutes". Cell 127 prints 1,234 s, about 21 minutes. "about 15 GB read" is not printed anywhere.
- **Attempt record, fig3c notes and the fig3c response:** "fitted … in under 3 minutes". Cell 101 prints 213 s.
- **Attempt record, kernel deviations:** "checked against scikit-learn's ElasticNet while preparing". No such check appears in the notebook.
- **Cell 96, and the fig4d-vis-leads notes:** "that point stays significant" in 5 of 5 and 3 of 5 seeds. The seed table in cell 95 counts any significant point from 0.08 to 0.12 s, not the 0.08 s point.
- **Attempt record, ed4f notes:** "Vision is more focal than Action under every reading but … B2 over the Figs. 3 to 5 set". In cell 115 the point estimate is higher under every reading; only the significance fails under B2. Cell 116 words this correctly.
- **Cells 105, 108 and 114:** the denominator stated in the method text contradicts the code (see fig3d above).

All other "**Result:" sentences, the Summary and the record's notes match the printed numbers.

**My round-1 reasons in the record:** they are stated in my own words. Two problems:

- For the nine kernel claims the record has `agrees: true`. My round-1 reasons questioned the block (problem 2), so that overstates my agreement.
- The response to problem 14 sits in the `reviewed` field, which describes what I reviewed. It belongs in the responses.

**3. Round-1 points**

**Resolved:**

- **1 (fig2fg):** the matched comparison is run; (iii) fails by more.
- **2 (kernel block):** the model runs and ed7c's ccCP part is tested. Two claims are still untested.
- **3 (fig5b sessions):** the dropped sessions are listed, and no threshold gives 34.
- **4 (suppfig2 amplitude):** the amplitude is now taken from `waveform_mean`.
- **5 (fig5d, ed7f):** both run on all neurons N as a variant and reproduce under either set.
- **6 (fig4d Bonferroni):** a corrected variant is printed.
- **7 (25 points):** the count, the correction and the text are fixed.
- **8 (12-trial rule):** 39 of 39 sessions pass.
- **10 (task-modulated neurons):** the test now uses the criterion's neurons.
- **11 (label mapping):** labels as given are run, and the outcome is marked as an assumption.
- **12 (ed9cf):** the fig5f index is used as it is.
- **13 (infinite-z readings):** the conclusions now say they carry no information.
- **14 (Tatum clock):** followed up in the data check.
- **9 and 15:** needed no change.

**What remains that bears on a conclusion:**

1. **fig3d:** the outcome rests on the denominator, and the method text in cells 105, 108 and 114 contradicts the code.
2. **The kernel model:** only 2,886 neurons pass the 2% VE threshold, against about 4,240 in the paper. That is unexplained, and the solver's check against scikit-learn or glmnet is not shown. It bears on fig4b, ed4f, ed5h, fig4fg, ed7c (the MOs share) and fig3d. ed5h turns on one neuron.
3. **fig4c and ed5g:** not tested, by choice rather than for lack of data or time.
4. **fig5b:** the paper's 34 sessions cannot be identified. The question is with the authors; the outcome turns on the claims file's session-count condition.
5. **fig4d-vis-leads:** rests on a single time point, and the wording about the seed test needs correcting.
