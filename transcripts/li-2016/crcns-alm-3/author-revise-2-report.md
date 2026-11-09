I've answered every point in the round-2 report. `python tools/entry.py all entries/crcns-alm-3-li-2016` gives 0 check errors and the notebook passes (358 s). The conclusions match the new numbers, and the spot-checked key values are the same as before. Nothing is committed.

**Outcomes**
- None changed, as round 2 requires.
- **fig6-modular-models-robust:** I agree with the verifier. The criterion has no partial rule, and the integrator recovers on lick-right trials only (-7.2 against -14.4 on lick-left). So I kept partially_reproduced and proposed not_reproduced under `proposed`, with the reason. The notebook result, the summary and the README say so. Round 3 reviews it. I also added the 4 s bilateral run as a deviation, which the verifier noted was missing.
- **fig2-bilateral-recovery:** kept as partially reproduced. A new printed line shows that in the six passing readings, ipsilateral selectivity just before the cue is still 28% to 43% below control. The verifier wrote 28% to 54%; I recorded its words and the printed range. The notes now say the criterion's partial rule (a time outside tolerance) does not fit this case, so the outcome uses the protocol's general meaning of partial.
- **ed6-bilateral-bias-inconsistent:** the claim is unchanged. I added a question to `questions/crcns-alm-3.yaml` asking whether the criterion's last sentence means reading (a) only. The deviation, summary and README say the pass holds under reading (b) only.
- **models-monolithic-fail:** the notes now say "partial" means two of five models could not be tested. They also say the borderline 0.212 deviation depends on the assumed rank-one matrix.

**Added outputs**
- The MD5 sum of each session file is now computed from the bytes read and compared with `checksums.md5`. All 91 match. The notebook header and README wording are updated to match.
- The notebook now prints its total run time (353 s). The README says about six minutes.
- New printed lines:
  - fig1g: resample fractions to three decimals (0.997 to 1.000 under the code's reading, at least 0.962 over all readings).
  - fig2: the deficit range in the six passing readings.
  - fig5: the largest bilateral fraction (0.002) and the seven readings where any resample recovers.

**Text corrections**
- ed8: 3 of 32 readings (it said 24), and the window (a) ranges now match the printout.
- ed2b: 56 is below the legend's 102. Mouse lines come from the meta data files.
- fig1g: "every resample" became "at least 99%".
- fig5: bilateral recovery is at most 0.2%, not none.
- ed7e: the deviation now says four of six sessions pass, each with trials in every group.
- ed4: the notes say the window and the end point changed together, so the effect of the window alone was not isolated.

I recorded round 2 under `verifications`: all 29 claims, the verifier's agreement and outcome, its reasons from the report, and my response.

Not done, and why:
- The fig1g neuron count (72 against 55) is still unexplained.
- The ed2e reading stays with a reader, as before.
