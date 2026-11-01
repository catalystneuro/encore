## Verifier report, round 2: DANDI:001272 (Semenov et al. 2025)

The claims file is now the right one (`dataset.id: "001272"`). It has 19 claims, and the attempt record has 19 outcomes, one for each claim.

### 1. Outcomes and assumptions

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| figs1-eight-neurons | not_reproduced | Yes | 3 subjects (di8 cell 14). |
| figs1-aps-as-emission-decrease | reproduced | Yes | 12 of 12 readings (cell 17). |
| figs1-near-threshold-delayed-aps | partially_reproduced, assumed | **No** | The two assumptions are stated. Prominence is well founded (null test 0.02 against 1.43 per 100 ms, cell 11). O5 (a) has a source in the paper. But under those assumptions the criterion is met in 0 of 24 combinations under O5 (a) (cell 20): only 1 of 3 neurons qualifies, and more than half are needed. The criterion is one per-neuron test that needs "1–3 APs" and "delayed" together. It does not split into parts. So the outcome under the assumptions is not_reproduced. "Partially" only describes the halves of that test. |
| figs1-stronger-field-shorter-delay-sustained-firing | reproduced, assumed | Yes | The assumptions (prominence, height (b)) are stated and reasonable, and the outcome is the same with the value reading. One caveat: subject 3's rho is −0.03 (p 0.88). It counts as negative only because the criterion looks at the sign alone. |
| figs1-culminates-in-sustained-depolarization | not_reproduced | Yes | Subjects 2 and 4 were never stimulated above 234 V/cm, so in effect only subject 3 tests this claim. |
| figs1-noisier-than-fluovolt | not_reproduced | Yes | The SD is higher for Di-8-ANEPPS in 0 of 12 readings. |
| figs1-effects-same-as-fluovolt | partially_reproduced, assumed | Yes, with a caveat | The criterion does not cover the case "pattern fails, no threshold difference", so partial is a fair call. Unit reading (i) is stated, but its only basis is the 001271 check (p = 0.29), and reading (ii) flips the result (difference in 9 of 12 readings). With n = 2–3 and 95% intervals as wide as −156 to 124 V/cm, "no difference" carries almost no information. |
| fig1-pure-sine-excites-all | not_reproduced | Yes | 0 of 12 readings, also in all three variants (cell 11). |
| fig1-20khz-needs-twice-the-field | not_reproduced | Yes | 0 of 12 (cell 14). The nominal-volts caveat is stated. |
| fig2d-modulated-thresholds-higher | not_reproduced | Yes | 0 of 12. Under whole/a/a and whole/b/a it fails only at p = 0.0500. |
| fig2-modulated-locks-to-beats | partially_reproduced, assumed | Yes | The whole-frame assumption is stated and backed by the sham and null tests. |
| fig2c-pure-more-aps | reproduced | Yes | 12 of 12 readings, under all three variants. |
| fig3b-low-conductivity-halves-threshold | blocked (other) | Yes | In substance this is data_missing; the notes explain why it is recorded as other. |
| fig3c-sustained-firing-2s | partially_reproduced, assumed | Yes | The cell 27 figure supports the prominence assumption. At 2.3 V, c7 fires about 6 APs, then sits on a flat plateau with no visible APs, so the 9 late detections under the value reading are noise. c8 at 2.0 V also looks like a block in the figure, so partial may be conservative. Two weaknesses: no null test was run on 001030, and the two bleaching corrections subtract the same trace from c7's sessions (c7 at 1.0 V is the only AP-free session), so "either correction" is one check, not two. |
| figs2-ttx-blocks-depolarization | reproduced, assumed | Yes, by the criterion | The second part passes on 1 neuron (14_20240731). No TTX neuron has a late mean above 5% before TTX (cell 30). The record states this. |
| fig4-pooled-time-constants | not_reproduced | Yes | 0 of 8 readings, also with whole-frame scaling (cell 9). The unscaled fits follow 001273-F2. 22 experiments against 19 is recorded as a deviation. |
| fig4-orientation-and-poles | blocked (metadata_insufficient) | Yes | The files have no cell-shape groups. |
| fig6-sine-less-than-pulse | blocked (other: not attempted) | Yes | The record is accurate, but the data are in 001274. |
| threshold-depolarization-estimate | blocked | Yes | One note: its first expected value, 57.7 ± 3.6 V/cm, already fails on either stated scale (140–178, or 70–89 V/cm if halved). |

**Possible gaps in the claims file (reported, not corrected):**
- **fig2-modulated-locks-to-beats:** the statement includes "triggered no sustained firing", but the criterion tests only sustained depolarization. The O6 rule for sustained firing (3 APs with one in the last 50 ms) is met by firing locked to the beats (45–46 of 84 modulated sessions, cell 20), so it does not fit this claim.
- **figs2-ttx-blocks-depolarization:** the criterion is conditional, so the depolarization part passes trivially when no neuron is depolarized before TTX. The paper describes a depolarization that the intense sine waves caused, which means it was present before TTX.
- **figs1-effects-same-as-fluovolt:** the criterion has no outcome for "pattern fails, no threshold difference".

### 2. Sentences the printed outputs do not support

**Attempt record:**
- figs1-stronger…, deviation: "the Di-8-ANEPPS APs measured here have a median height of 4.1 to 6.6%". The printed values are 3.73–6.67% (di8 cell 31).
- figs1-near…, deviation: "Under O5 (b) … (12 of 24)". With the 1-ms bound the outputs give 13 of 24 (value) and 20 of 24 (prominence). 12 of 24 is the old 2-ms result (cell 20).
- figs1-culminates…: "(with 2 ms also with the Otsu ROI and level (b))". No per-neuron table is printed for 2 ms. Cell 27 and its output give this result for prominence, not for 2 ms.
- fig1-pure-sine…: "these readings detect peaks before the onset and after the stimulus at nearly the rate during it". For a/a/a and a/b/a the rates are 1.10 and 1.06 per 100 ms against 2.47, a little under half (fluovolt cell 7). The response under fig2-modulated-locks-to-beats repeats the phrase.
- fig2-modulated-locks…: "001032 neuron 2_1, 11 V" is not printed anywhere.
- fig3b notes: "0 of 1,090 mention gluconate" is not printed. The notebook shows 0 of 454 (fluovolt cell 4).
- Findings: "All 178 files" of 001034 are identical to 001032. Only 80 of 80 2-kHz files are shown (di8 cell 29).
- Findings: 001272 files say "without tetrodotoxin (vehicle control)", and 001271 files say TTX "caused sustained depolarization". Neither description text is printed in any output.
- The other numbers in the record notes match the outputs.

**Notebooks:**
- fluovolt cell 21: "detect peaks … at nearly the rate during it". The same objection as above applies to ROI (a).
- fluovolt cell 8: "so most of its detections are noise". This holds for ROI (b) (2.1–2.4 against 3.33–3.37 per 100 ms) but not for ROI (a) (about 43%). The same cell says "2.44 to 3.38"; the printed maximum is 3.37.
- strobe cell 14: "the first acquired frame of every file is dark". This appears only in `strobe.py`, with no printed output behind it.
- All other "**Result:**" conclusions, the three Summary sections and the README match the outputs.

**My round-1 reasons in the record:** they are stated in my own words, mostly verbatim, and each sits under the right claim. Two small points:
- For threshold-depolarization-estimate, my outcome was "not_reproduced (threshold part); rest untested". The record shortens this to not_reproduced.
- fig4-orientation-and-poles combines my three separate fig4 rows. The combination is fair.

### 3. Round-1 points

**Resolved:**
- 1, the claims-file mismatch. With this file, my round-1 objections on fig3c (the window and the 5% level) and on figs2 (the 5% level) no longer apply.
- 2, the TTX pass on sustained depolarization: the record now says it rests on 1 of 6 neurons.
- 3, noise counted as APs on a raised baseline, for Di-8-ANEPPS.
- 4, the detector null test.
- 5, the degenerate eroded ROI.
- 6, the hard-coded text.
- 7, the wording on the amplitude scale.
- 8, the strobe fits: all 22 experiments are now fitted, fits stuck at a bound are flagged and left out, and the bleach-corrected variant has been added.
- 10, the fig3c window.
- 11, the truncated files and pooled latencies.

**Remaining, and bearing on a conclusion:**
- figs1-near-threshold-delayed-aps: under its stated assumptions the outcome should be not_reproduced (section 1).
- fig3c-sustained-firing-2s: the prominence reading decides the outcome (0 of 4 neurons with the value, 1 of 4 with prominence) and has no null test on 001030. For FluoVolt the record uses prominence only for fig3c and the value reading elsewhere. That includes figs2, where prominence would fail (3–4 TTX neurons keep detections). Each choice has a stated reason, but each is the reading that favours the claim.
- figs2-ttx-blocks-depolarization: the depolarization half rests on one neuron.
- figs1-effects-same-as-fluovolt: the outcome depends on the undeposited amplitude scale and an underpowered test.
- Point 9: fig6-sine-less-than-pulse and threshold-depolarization-estimate are still not attempted, though the data are in 001274.
- fig4-pooled-time-constants: 58 of 352 charging fits are left out at a bound, and the signal is a median 1.97 times the pre-pulse SD. The failure may come from the missing debris scaling, as the record says.
