I've revised the attempt for round 1. Two outcomes changed, one disagreement is recorded, and the entry re-ran clean: `python tools/entry.py all entries/kim-2022` gave 0 errors and the notebook passed in 798 s. I checked the executed copy against the conclusions, and round 1 is recorded under `verifications` with all 25 claims.

**Outcomes that changed**
- **fig2c-weaker-at-6-7: reproduced → partially reproduced.** The verifier was right that 50% only passed through pooling every dish×ROI value. The pooled test now takes one value per dish (its mean over the higher-field ROI). On that test 50% gives p = 0.049, short of the p < 0.01 it needs. 100% still passes (p ≤ 0.022). The verdict now uses only the unpaired test; it no longer ORs in the paired one.
- **fig2c-max-inhibition-50-75: partially reproduced → not reproduced.** The criterion runs the test at each field, and I now require it to hold at every field, like the ordering. My round-1 rule ("at most fields") had no basis. No comparison or variant reaches every field; the best is 7 of 10.

**Disagreement recorded:** fig2b-exponential-same-slope stays partially reproduced; the verifier would give not reproduced. I adopted the criterion's main reading (8 kV/cm cutoff, nonlinear fits). Under it the slopes don't differ but the exponential beats a line for only 3 of 5 amplitudes. The criterion names no outcome for that mixed case, and partially reproduced covers a claim that holds only in part.

**Added or corrected**
- **Assumptions now stated and marked:** units for vertical-scales; ROI on both sides of the centre for flat-above-8-7 and weaker-at-6-7. The notebook shows that one-sided ROI would change both of those outcomes.
- **Output the verifier asked for:**
  - per-dish background and ROI values by imaging day;
  - the 0.1 and 0.3 mm footprint variants for all three Fig. 2C claims;
  - a semi-log plot of the Fig. 2B fits;
  - Fig. 7 fit overlays with residuals.
- **Imaging-day confound, now in the notes:** the 0% and 25% dishes were imaged on 07-29 and the 75% and 100% dishes on 08-24, with different backgrounds. The conclusions also say:
  - the low-field percents (198% and 283% of unipolar) come from a unipolar mean near background;
  - 100% pulses don't inhibit in these dishes;
  - several "no difference" results rest on 3 to 5 dishes or cells.
- **Fig. 7:**
  - The charging window is now the criterion's full 0 to 600 ns; the fitted values didn't change.
  - A fit with t = 0 half a frame earlier gives 216 ns. Together with the one-frame shifts, this shows the charging τ is not robust.
  - The criterion's charging form is now the main one, and the free-start form is a labelled variant.
  - The time of the bipolar minimum now has a check at a time fixed in advance, 1175 ns, which gives the same result.
- **Record and files:** I rewrote notes, deviations and the pairing finding in `attempts/kim-2022-02.yaml`, updated the README and the notebook summary, and set `runtime_minutes` to 14.

**Not done**
- **No reader question:** the verifier called both claims-file points a statistical flaw and a scoping issue, not misreadings of the paper. So `questions/kim-2022.yaml` doesn't exist.
- **Blocked claims unchanged:** the verifier's table says "data_missing" while the record says `dataset_missing`. I kept `dataset_missing`, because 000548, 000549 and 000550 are listed under `missing_datasets`.
- **No handover rebuilt:** round 2 gets the full executed notebook.
- Nothing committed.
