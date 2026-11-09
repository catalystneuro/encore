**Round 2 verifier report: attempt 001751-liu-2026-01**

**1. Outcomes**

The claims file has 35 claims and the attempt record has 35 outcomes, one per claim. They are: reproduced 9, partially_reproduced 7, not_reproduced 2, and blocked 17 (other 12, methods_underspecified 2, metadata_insufficient 2, data_missing 1).

I agree with 34 of the 35 outcomes. Compared with round 1:
- **fig4d-sodium-current, now reproduced:** I agree. In round 1 I gave partially_reproduced because the peak measure was not checked against the code's values. It now is (cell 52). With a 1 kHz low-pass and the code's 2 ms baseline, r = 0.99 and the median difference is 1.28 pA, and p = 0.0010 in every window. Any low-pass from 500 Hz to 2 kHz gives p = 0.0006 to 0.0040. Only the unfiltered readings depend on the window, and their peaks fall as late as 9.99 ms. The paper's Methods give no filter; I checked the paper text.
- **fig8a-metabolite-gradient, partially_reproduced:** I agree. My round-1 objection was that the input was incomplete. The test now runs on the MetaboLights deposit itself, which holds the same 558 metabolites (cell 58). So the 581 the paper states is a difference in the data, not an input gap. The gradient holds (175–195 against 84–98, with similar ratios), AIC-V1 fails its tolerance under every reading, and AIC-PrC passes under one.
- **fig5-ven-outputs-absent, changed to partially_reproduced:** I agree, as I gave this in round 1.
- **patchseq-mapping, blocked (metadata_insufficient):** I still lean to partially_reproduced. Three of the four values are within tolerance and the fourth cannot be tested (cell 62). The claims file gives no criterion for this claim, the record states the disagreement, and no number depends on it.
- **fig4j-eepsp-latency, blocked (other) rather than data_missing:** I accept the change, for the protocol reason the record gives.

Both assumptions an outcome rests on are stated and reasonable:
- **fig4d (`assumed: true`):** the 1 kHz low-pass, 2 ms baseline, 0.2–3 ms window and steps up to 0 mV are chosen because they reproduce the code's per-patch `max_Na_current`. The record and cell 53 say so, and the question is put to the authors.
- **fig4j-eepsp-amplitude (`assumed: true`):** the values in `sumData_StimWM.xlsx` are taken to be the selected monosynaptic eEPSPs. This is stated as a deviation, along with 23 pairs against the paper's 26.

**2. Sentences the printed outputs do not support**

- **Cell 13, and the code-table-link notes:** "Every file the table names is in the dandiset (296 of 296)." The table names 288 files. The other 8 were assigned by `link_blank_blocks`, which picks them by the firing channel (cell 7).
  - For the same reason, the "294 of 296 (99.3%)" presynaptic match includes 8 files that match by construction. The independent figure is 286 of 288.
  - The outcome does not change.
- **Finding (metadata_error, stimulated electrode):** "in 281 of 288 files the firing channel is the presynaptic channel of the code's table." This is my round-1 number under the old rule and was not updated. Cell 11 now prints 294 of 296, or 289 with the −30 mV rule.
- **Cell 53:** "r = 0.99, median difference 1.28 pA, every window." This holds only for steps up to 0 mV. With steps up to +85 mV, r is 0.77 to 0.94 (cell 52, rows 25–31).
- **Cell 0:** "its content is the same as the draft (301 files, 6,964,257,080 bytes, both modified 2026-08-25)." No output compares against the draft. The same applies to "the only published version" (cells 0 and 51) and "the only revision" (cell 57).
- **fig4d deviation:** "whose filter_1000Lowpass the paper's code uses in extFig9ad_plotVENsubtypeAP_Cmp.m." No output shows this.
- **README:** "about five minutes." Cell 1 prints only the 106 s spent streaming.

Every other sentence of the "**Result:**" cells, the Summary, the README and the record's notes and findings matches the printed numbers. That includes the per-class pair and connection counts, the subject breakdowns, the Fisher p range, the at_edge counts, and the PSC, ANOVA, peak-index, metabolite and mapping values.

The record states my round-1 reasons accurately and in my own words, including the problem numbers attached to each claim. Its "31 of 35 agree" matches the four claims I disagreed on in round 1.

On the claims file: as in round 1, it says the Supplementary Information was not read, but `paper/` holds supp1–9. The PDFs still have no extractable text, and I could not render them.

**3. Round-1 points**

Resolved:
- Problem 1: the table is now filled within each presynaptic block, and the blank blocks are linked or left out.
- Problem 2: the peak measure is validated against the code's values; reading (b) is now treated as a rescaling of (a).
- Problem 3: the full group tree of the files and the electrode values are printed, and the search for a position is run, not asserted.
- Problem 4: the test uses the MetaboLights deposit.
- Problem 5: the presynaptic rule now follows the criterion, with the −30 mV rule as a variant.
- Problem 6: response peaks on the first sample of the window are flagged (`at_edge`) and counted.
- Problem 7: the annotation oddities are reported.
- Problem 8: the counts are compared with their tolerances.
- Problem 11: the 9-sweep file is recorded.
- Problem 12: the notebook says the two neuron counts disagree.
- Problems 9 and 10 remain as stated deviations, which is acceptable.
- The cluster names, sheet layouts, Na+ scatter plot and holding potentials I could not check in round 1 are now printed.

What remains that bears on a conclusion:
- **Supplementary Table 5** is still unread, by me and by the author. Its per-class pair and neuron counts bear on every Fig. 5 pair count that fails: fig5d, fig5-pc-to-pc, fig5-ven-outputs-absent, fig5-pc-to-ven and fig5-pc-in. A question on it has been put to a reader.
- **patchseq-mapping:** whether it should be blocked or partially_reproduced (see 1).
- **fig4d** rests on its stated filter assumption.
- **Descriptive only:** 3 of the 26 annotated connections (rows 362, 742 and 784) peak on the first sample of the window, as an artefact would. The criteria rest on the annotations, so no outcome changes.
