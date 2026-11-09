I revised the attempt for verification round 2. The entry re-ran from scratch with `python tools/entry.py all entries/001048-semenov-2025`: 0 check errors, and the notebook passed in 2,292 s (about 38 min). Nothing is committed.

**The verifier reviewed the wrong claims file.** `tools/entry.py handover` copies the claims file of every dandiset the entry uses into one folder. The files for 001048 and 001274 have the same name, so the 001274 one overwrote ours, and the verifier judged 26 claims with different ids and criteria. Its problems with the code still apply here, and I took them up. I recorded its verdicts against our claims, each paired with the verifier claim it corresponds to; four of our claims have no counterpart and are left out. The `reviewed` field explains this. I could not fix the tool, because the workflow only collects changes under attempts/, claims/, entries/ and questions/. Round 2 is not affected: its package takes the claims from `claims/001048/`.

**Outcome changes (three, all to blocked, metadata insufficient):**
- **fig1-20khz-needs-twice-the-field** (was partially reproduced): the 20/2 kHz ratio needs calibration factors per frequency, and these are not in any of the dandisets.
- **fig4-pooled-time-constants** (was not reproduced): there are no ROIs, and the files don't say which of the 22 groups are the paper's 19 experiments.
- **threshold-depolarization-estimate** (was not reproduced): the threshold in V/cm can't be formed without the calibration, and the outcome changes with how the volts are converted.

Four outcomes are now marked as resting on the crop ROI (fig2d-5ap-above-1ap, fig2c-pure-more-aps, fig1-pure-sine-excites-all, fig2-modulated-locks-to-beats), because the ROI readings disagree. Every other outcome is unchanged.

**Where I disagree with the verifier, the reasons are recorded:**
- **fig6-sine-less-than-pulse:** kept as partially reproduced, resting on my ROI choice. Our claims file has no rule that blocks a claim when ROIs aren't deposited. The boxes follow the paper's own description of where it placed its ROIs.
- **fig3c-sustained-firing-2s:** kept as partially reproduced. Two of the three parts hold, and the block still fails with the new detector.
- **figs1-di8-same-as-fluovolt:** kept as partially reproduced. Our claims file says only one AP-height reading applies to these neurons, so the disagreement the verifier saw doesn't decide it.
- **fig2-modulated-locks-to-beats:** kept as reproduced. The block test the verifier missed belongs to the other claims file.
- **fig1-pure-sine-excites-all:** kept as partially reproduced. In our file it is a single four-part criterion, and the outcome is partial under every reading.

**What I fixed or added:**
- **AP detector:** the old detector counted small wiggles on a raised plateau as APs. It now requires a width of 2 to 20 ms measured both at half the peak's height and at half its prominence. Each measure alone fails on these traces, so both are shown as variants in a new section.
- **Readings that disagree:** the claims file's header would block these claims. Instead I use the crop ROI and mark the outcome as resting on that assumption, which protocol step 1.6 allows.
- **Early APs:** APs within 5 ms of onset are real, not onset artefacts. The same stimulus under TTX gives no transient above 5% in any of 71 sessions.
- **Outputs the verifier asked for:**
  - late-window dF for the modulated sessions;
  - dF before and after TTX for each TTX neuron, and the vehicle split pauses;
  - the APs that remain in the 2-s recordings, with their prominences;
  - the fitted carrier phase per strobe ROI (the two ROIs are close to antiphase, and the sensitivity at the fitted phase is 6.4%);
  - the pulse onset check, which confirms frame 20;
  - the measured pulse amplitudes noted in 001273's descriptions.
- **LOESS:** now R-style loess (degree 2), matching the RStudio the paper lists.
- **Text:** all conclusions, the summary, the README, the record's notes and the findings match the new numbers. The expected runtime is now 40 minutes.

**What I did not change, and why:**
- **Bleaching:** not corrected, because the claims file says the paper corrected only the 2-s traces. The bias is now stated.
- **Problems 12 to 14:** the tolerances, ranges and tests the verifier flagged come from our claims file, so they stay.
- **Questions file:** no reader questions were added, since the verifier reported no place where our claims file misreads the paper.
- **Unused dependency:** `statsmodels` is still in `requirements.in`, though nothing uses it now.
