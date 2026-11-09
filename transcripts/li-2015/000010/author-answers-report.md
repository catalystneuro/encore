I took up all seven answers and re-ran every affected claim. Four outcomes changed. `entry.py check` reports 0 errors, the clean run passed in 665 s, and the handover is built in `executed/000010-li-2015/handover/`. I did not verify my own work, and nothing is committed or pushed.

## Questions, what each answer changed, and the outcomes

**1. Reaction-time rule.** The answer named two readings: (k) a fixed threshold on the raw signal, and (z) the baseline mean plus some number of s.d. Both are now run on the lick trace of all 99 sessions.
- **reaction-time:** blocked (methods underspecified). Earlier: blocked (methods underspecified), because no rule was given.
  - The number of s.d., which the paper leaves open, sets the value. Under (z) the mean across mice runs from 40 to 129 ms; it is within 61.1 +/- 10.5 ms only at about 2 to 3 s.d.
  - Under (k) no single raw threshold suits every session, since baselines run from 0.07 to 4.8 a.u. Between 36% and 90% of trials never cross it, and the mean is never within tolerance.
  - Where the mean does match, the s.d. across mice is 31 to 38 ms, against the paper's 10.5.

**2. Trials without a lick.** The answer gave two readings: such trials count as not correct (x, the literal reading), or are left out (y). Both had already been run.
- **behaviour-performance:** reproduced. Earlier: reproduced. The recorded value is now that of (x), 75.8%; earlier it was 76.5% under (y).

**3. Three details of the population dynamics.** All open readings are now run in every combination. The new one is the go-cue bin centred on the cue.
- **fig2c-population-dynamics:** reproduced. Earlier: blocked (methods underspecified).
  - With the light trials kept (t1), all 24 correlation readings and all 4 selectivity readings hold.
  - With them left out (t2), 2 of 24 fail. Under question 6's answer either light reading may decide, so t1 decides.

**4. Length of the imaging response epoch.** The answer made 1.3 s and 1.5 s both readings. Both had already been run.
- **imaging-selectivity-counts:** partially reproduced. Earlier: partially reproduced.
- **fig4f-spatially-intermingled:** not reproduced. Earlier: not reproduced.

**5. Layer 5 without a plane depth.** The answer says testing all labelled cells is a substitute population, not a reading of the paper.
- **fig4h-pt-contra-imaging:** blocked (metadata insufficient). Earlier: not reproduced. The all-labelled-cells results are still shown as a variant; there the chi-squared test of PT against IT never reaches P < 0.001.

**6. Trials with tagging light.** The answer made (t1) all trials and (t2) trials without the light readings for every electrophysiology claim of Figs 2 and 3, and either may decide.
- **fig3f-pt-contra-preferring:** reproduced. Earlier: blocked (methods underspecified).
  - With the light trials, 30 of 45 PT neurons are contra-preferring (P = 0.010) and IT gives P = 0.58.
  - Without them the claim holds under no reading. So the result depends on keeping the trials in which the light drove the PT neurons.
- Unchanged, because t1 and t2 agree:
  - fig2-selective-fraction: reproduced
  - fig2d-preparatory-perimovement: not reproduced
  - fig2c-selectivity-time-course: reproduced
  - ed2c-error-trials-predict-choice: reproduced
  - fig2e-no-contra-bias-spikes: reproduced
  - ed1-fast-spiking-properties: partially reproduced
  - fig3e-pt-it-both-activity-types: reproduced
  - fig3f-pt-contra-selectivity: not reproduced

**7. Which spike is antidromic.** The answer named three readings: (w) the first spike in a window after the first pulse of each pair; (c) the same without collision trials; (r) only spikes in the evoked peak. Their parameters are run at several values.
- **antidromic-latencies:** partially reproduced. Earlier: blocked (methods underspecified).
  - PT latency is below IT latency in all 18 combinations. PT latency is within tolerance in all 18 and IT latency in 10.
  - Jitter matches the paper only under (r), and keeping spikes near the peak partly sets that agreement.
  - All four measurable values are within tolerance in one combination. The four values for neurons that failed the collision test cannot be measured, because those neurons have no label.

## Other changes
- **Helper module (`alm.py`):** it now reads the lick trace with parallel HTTP range requests (about 95 s for all sessions, against 400 s or more before), and has functions for reaction time and antidromic latency.
- **Records and text:** the notebook header, conclusions and summary, the README, `entry.yaml`, and the attempt record (provenance now points to this run, and the lick-trace finding notes the signal's level and direction vary by session) are updated.
- **Notebook cells:** some cells were missing ids, so I added them; the executed copy got the same ids.
