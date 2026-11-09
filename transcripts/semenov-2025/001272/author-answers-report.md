The reader's answer changed one detail, and after re-running every claim it affects, no outcome changed. The entry check reports 0 errors, all three notebooks ran from a clean environment (4, 5 and 2 minutes), and the verifier's package is built in `executed/001272-semenov-2025/handover/`. Nothing is committed or pushed.

## The question and its answer

There was one question, on the claims file's header item O3, which sets the width an AP must have at half its height. O3 asked for 2 to 20 ms. I asked whether the 2-ms lower bound was right, since FluoVolt APs are about 2 ms wide at half height and the paper's "about 10 ms" is the AP's whole duration.

The reader agreed and amended O3 to 1 to 20 ms. The 1-ms floor only excludes single-frame noise.

## What I changed

- **Helper:** `sinewave.py` now detects APs with the 1-ms lower bound by default.
- **Both notebooks:** every claim is tested with the 1-ms bound, and the 2-ms result is printed beside it to show what the answer changed.
- **New outputs:** the 2-kHz 5-AP p-value in fig2d now prints to four decimals, because it sits at the 0.05 bound. fig2 lists the modulated sessions with more than 10 APs. The near-threshold claim gets a per-neuron table for one more reading.
- **Text:** the conclusions, the summaries, the README, and each affected claim's notes in the attempt record are rewritten. Each claim's notes now open by saying what the answer changed.
- **Unchanged:** figs1-eight-neurons and the blocked claims do not use O3.

## Outcome per affected claim (now, with the earlier outcome)

| Claim | Now | Earlier | What the 1-ms bound changed |
|---|---|---|---|
| figs1-aps-as-emission-decrease | reproduced | reproduced | Still met under 12 of 12 readings. The trace as recorded now yields 2 APs under 4 readings (it yielded none). |
| figs1-near-threshold-delayed-aps | partially reproduced, assumed | partially reproduced, assumed | Met in 19 of 48 reading combinations (was 12). Under the adopted O5 (a), a first AP at least 100 ms after onset, it is now met in 6 of 24 (was 0): 2 of 3 neurons under whole/a/b, 1 of 3 under whole/b/b. |
| figs1-stronger-field-shorter-delay-sustained-firing | reproduced, assumed | reproduced, assumed | Same: 10 of 12 readings, 6 of 6 under height (b). |
| figs1-culminates-in-sustained-depolarization | not reproduced | not reproduced | Still at most 1 of 3 neurons. Subject 3 no longer meets it with the Otsu ROI. |
| figs1-noisier-than-fluovolt | partially reproduced | partially reproduced | Same: lower signal to noise in 10 of 12 readings, higher SD in 0 of 12. |
| figs1-effects-same-as-fluovolt | partially reproduced, assumed | partially reproduced, assumed | Reading (i): still no difference in 12 of 12. Reading (ii), FluoVolt volts halved: Di-8-ANEPPS thresholds higher in 9 of 12 (was 12 of 12). |
| fig1-pure-sine-excites-all | not reproduced | not reproduced | Still 0 of 12 readings. Measured values change from 96.4 / 41.15 / 78.63 to 96.4 / 62.99 / 32.46. Under two readings the firing-rate ceiling now falls in range, but the latency does not. |
| fig1-20khz-needs-twice-the-field | not reproduced | not reproduced | Still 0 of 12. Ratios now range from 1.71 to 2.98; the measured value goes from 2.16 to 2.0. |
| fig2d-modulated-thresholds-higher | not reproduced | not reproduced | Still 0 of 12, but close: under 2 whole-frame readings the only failing part is the 2-kHz 5-AP test, p = 0.0500, at the bound and not below it. The notes say so. |
| fig2-modulated-locks-to-beats | partially reproduced, assumed | partially reproduced, assumed | Met under 4 of 12 readings (was 8 of 12). Under the adopted whole frame it now fails because one session (001032 neuron 10_1) has 13 APs; earlier it failed on one session with sustained depolarization. The locking itself still holds. |
| fig2c-pure-more-aps | reproduced | reproduced | Same: 12 of 12. |
| fig3c-sustained-firing-2s | partially reproduced, assumed | partially reproduced, assumed | Still only neuron c7 shows the pattern (whole frame, height as prominence). No reading now has more than 1 of 4 neurons meeting it (was at most 2). |
| figs2-ttx-blocks-depolarization | reproduced, assumed | reproduced, assumed | Same: 8 of 12 readings. |
| threshold-depolarization-estimate | blocked | blocked | Only the reported range of the FluoVolt thresholds changes, now 140 to 178 V/cm. |

One more effect of the 1-ms bound: the Otsu ROI with the 5% height now detects 20 APs in the 5 sham sessions (no stimulus), against 5 with the 2-ms bound. The whole-frame ROI detects none. This adds to the reasons the record adopts the whole frame.
