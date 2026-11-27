**Verifier report, round 2: Haley, Hampton & Marder 2018 (haley-2018-01)**

Counts come from the claims file and the attempt record. The claims file has 30 claims. The record gives 11 reproduced, 2 partially_reproduced, 11 not_reproduced and 6 blocked. Every outcome that is not blocked is marked `assumed: true`. Cell indices below refer to the re-executed notebook (103 cells), so they differ from my round-1 numbering.

**1. Outcomes and their assumptions**

The assumptions are all stated in each outcome's deviations: automatic spike thresholds, states read from the spikes, the LC burst rule (1.0 s, 1 spike), the code's starting waveform parameters, PTX pH taken from the bath signal, and missing steps counted as 0. Each is reasonable given that the annotations and Spike2 output are not deposited.

| Claim | Agree? | Comment |
|---|---|---|
| fig2a | yes | The lvn condition barely discriminates. 1, 2 and 4 lvn spikes and PD bursting alone give nearly identical fractions (cell 21). They differ only at 5.5, in 877_121 and 887_049. So "triphasic" still rests mainly on PD bursting. |
| fig2bcd, fig3e, fig3f, fig4de, fig4fg, fig6a, fig7d, fig7e, fig8b, fig8b-cross, baseline, intact | yes | |
| fig3a, stg-state-transitions, cg-state-transitions | yes (blocked) | States 1 and 2 cannot be separated without telling LP from PY. |
| fig3c | yes | 10.4 has p_corr 0.31; the criterion has no partial condition. |
| fig3d | yes, as the criterion is written | The criterion probably misreads "relatively invariant" (round-1 point 4, now sent to a reader). |
| fig3s2, fig7s2 | yes, under reading (b) | Reading (b) passes almost any data (round-1 point 11). |
| fig4a | yes | Rests on one preparation (903_052). |
| fig4bc | yes | Fragile: LP 8.8 depends on 903_056 (p_corr 0.056 without it, cell 52). |
| gastric ×3 | accept, arguable | The claims file gives a fallback ("rhythmic LG bursting (lgn or lvn) with alternating DG bursting (dgn) where recorded"). Blocking it for lack of thresholds is the attempt's choice. Nothing in the data or methods forces it. |
| fig6 | yes as computed | Weak evidence. The notebook's own isolation check (cell 23) shows 877_149 CG2L counting events 3.1 times the control height, already at ctl_base, with 15 to 25 spikes per burst. |
| fig7b | yes on the main reading | Fragile. With factor 2 it would be partial (stated). Without the four doubtful units it would also be partial: both ANOVAs pass (0.045 and 1.3e-11) and 9.8 and 10.4 pass (cell 23). The record does not say this. |
| fig7c | yes as computed | Depends on the four doubtful units (stated). Without them both ANOVAs and 10.4 pass. |
| fig8a | yes | The partial condition needs all three t-tests. |
| robust | yes | Still favoured by a proxy that hardly separates out state 3. |

**2. Sentences the printed outputs do not support**

- **Record, fig8b-cross notes:** "877_121 keeps a fraction of 0.59 at 5.5". In the main reading it is 0.398 (cells 19 and 87). 0.59 is the PD-alone value (`frac_pd_alone`, cell 87).
- **Record, finding 6 (903_046_0002 swap):** "0.62 of them within 5 ms". No output prints this. Cell 15 shows a match of 1.00 at the 38 ms lag. The record itself says elsewhere that the 5 ms window missed the conduction delay.
- **Cell 32 and the record's fig3a notes:** "at 10.4, 887_005 has fraction 0". 887_005 has no 10.4 file (cell 12), so this 0 is the zero-fill. The text does not say so.
- **README:** "It took 56 minutes in the revision's run" and "about 64 GB". Cell 101 prints 39.6 min, and no output gives a data volume.
- **Cell 6:** "about 10 min and 3.3 GB". Cell 7 prints 24.1 + 7.7 min and a peak of 8.23 GB.
- **Cell 88 and the record:** "877_141, 887_141 and 897_037 burst throughout 5.5". 877_141 has fraction 0.954 there. This is minor.

Every other "**Result:**" sentence, the Summary, the README outcome table and the remaining notes match the outputs.

The record's verification block gives my round-1 reasons faithfully, essentially in my own words. The agrees flags and the outcomes match my round-1 table.

**3. Round-1 points**

Resolved:
- **3:** The zero-fill now cites the code, and the variant is run for fig8a/b.
- **5:** The 903_052 PD label is supported by a 34–38 ms lag, 0.61–1.0 matched against chance of at most 0.037 (cells 10 and 49).
- **6:** 903_056 is now shown and disclosed.
- **8:** 877_101 is explained.
- **10:** The [RM] rule is now stated.
- **C:** The electrode lists are now printed.

Partly resolved or open, bearing on conclusions:
- **1, state proxy:** The lvn requirement changes almost nothing (cell 21), so state 3 is still effectively counted as rhythmic. The gap factor still flips outcomes:
  - fig7b becomes partial at factor 2.
  - The fig8a acid ganglion effect has p 0.143 at factor 2, and the base effect has p 0.061 at factor 5 (cell 84). Cell 85 does not mention these.
- **2, LC isolation:** The histograms (cell 23) confirm the four named units. They also show doubtful isolation in units the variant keeps:
  - 887_127 CG1L at 10.4: 1300 events, ratio 0.67.
  - 897_041 CG1L at ctl_base: ratio 0.52, 21 spikes per burst.
  - 887_005 CG2L at 5.5: ratio 0.62.

  Affects fig6, fig7b–d and fig8.
- **4, 11:** Claims-file issues, sent to a reader. They are still open.
- **7:** The gastric fallback was not attempted (see the gastric row above).
- **903_052 pH compression:** The "10.4" file estimates pH 9.75 and the "5.5" file 5.87 (cell 10). This is still unaddressed. The 6.7 file used for the fig4a slow-wave part has a PD–pdn match of 0.02, near its chance of 0.011, so PD identity in that file is unconfirmed.
- **Not provided:** No comparison of the proxy against Figure 8B, and no trace overlays.

**4. Critical findings**

No finding in the record is rated `critical`.

I would rate finding 6 (903_046_0002, PD and LP channel names swapped) critical, not major. It is data filed under the wrong label, and nothing in the file's metadata shows it. An analysis by channel name silently swaps PD and LP in that experiment's acid control. Cell 15 shows it: the file's channels are ['PY1', 'LP3', 'stn', 'PD4'] where the other files have ['PY1', 'PD3', 'stn', 'LP4']. The "LP3" channel matches the pdn at 1.00 (38 ms lag), and the "PD4" channel matches at 0.13 against chance of 0.154. The finding gives no `versions` or `fixed_in`.

The other ratings are reasonable:
- Finding 5 (903_058 and 903_060 steps out of order) is minor. The recorded bath pH shows it (cell 14).
- Finding 3 (README mismatches) is minor. It is evident from the folders (cell 13).
