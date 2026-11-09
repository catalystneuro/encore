**Verifier report, round 2: Semenov et al. 2025 (attempt 001048-semenov-2025-01)**

This round I had the right claims file (dandiset 001048). It has 20 claims, all `data: elsewhere`, with readings O1–O6, and the notebook and attempt record follow it. The record lists 20 outcomes: 3 reproduced, 7 partially reproduced, 1 not reproduced and 9 blocked.

### 1. Outcomes

| Claim | Recorded | Agree? | Assumption (`assumed: true`) stated and reasonable? |
|---|---|---|---|
| ap-selection | partially | Yes | Stated. The crop ROI is reasonable: the Otsu masks have a median of 35 or 10 pixels, some only 1–3 (cell 8). The peak also holds under ROI a in 16/16 readings. |
| fig1-pure-sine-excites-all | partially | Yes | Stated. The partial outcome rests mainly on the falling latency (34/37). Excitation at 20 kHz reaches ≥90% only with crop ROI + O3 b; with O3 a it is 88.2% (cell 18). Latency and ceiling fail under every reading. |
| fig1-excitation-block | not reproduced | Yes | – |
| fig1-20khz-needs-twice-the-field | blocked, metadata insufficient | Yes | – |
| fig2d-5ap-above-1ap | reproduced | Yes, conditional on the crop-ROI rule (§3) | Stated. The Otsu readings fail (cell 33). |
| fig2d-modulated-thresholds-higher | partially | Yes | **Should be marked assumed.** The one significant test needs crop ROI + O3 a (p = 0.034). It is 0.10 with O3 b, so with O3 b none of the three tests reaches p < 0.05 even under the crop ROI. Under ROI b the 20-kHz 1-AP direction reverses (12.00 vs 12.33; cell 36). |
| fig2-modulated-locks-to-beats | reproduced | Yes, marginally | Stated. Envelope reading a is reasonable: under reading b the APs would sit at the field minima. The O4 b choice is made after the fact. It removes the one O4 a session (001032/2_1, 5.96%; cell 41), and its stated reason ("tied to the neuron's own APs") would apply to every claim that uses O4. |
| fig2c-pure-more-aps | reproduced | Yes | Stated. Holds in 11 of 12 readings (cell 44). |
| fig3b-low-conductivity-halves-threshold | blocked, other | Yes | – |
| fig3-extrapolated-threshold | blocked, other | Yes | – |
| fig3-not-heating | blocked, methods underspecified | Yes; follows the criterion (cell 59) | – |
| fig3c-sustained-firing-2s | partially | Yes | Not marked assumed. That is acceptable: c7 meets parts (i) and (ii) under every reading and correction, and the block fails everywhere (cell 47). |
| figs1-di8-same-as-fluovolt | partially | Yes | Stated. One of the two neurons counted as "latency falls" has ρ = −0.03 (cell 51). |
| figs2-ttx-blocks-depolarization | partially | Yes | Stated (vehicle split, crop ROI). The depolarization half rests on one neuron. |
| fig4-pooled-time-constants | blocked, metadata insufficient | Yes | – |
| fig4-orientation-and-poles | blocked, metadata insufficient | Yes | – |
| fig5-sine-asymmetry | blocked, metadata insufficient | Yes | – |
| fig5-whole-cell-depolarization | blocked, metadata insufficient | Yes | – |
| fig6-sine-less-than-pulse | partially | **No** | Stated, but inconsistent. fig4-pooled was blocked because its values "depend on ROIs and a selection the dandiset does not give". The same is true here: the deviations say "the sensitivities depend on it", and the nine cells are inferred. The 12×12 boxes would dilute the peak polarization, which fits 17.4 against 28. The sizes should be recorded as not judgeable, not as "fail under every reading", or the claim blocked. The direction (18/18 under the signed reading, 15/18 per cycle) is the only part that holds. |
| threshold-depolarization-estimate | blocked, metadata insufficient | Yes | – |

### 2. Sentences the printed outputs do not support

- **Cell 63:** "no cell in 001274 has more than 4 sessions at 100 Hz". Also cell 76 ("four at most") and the record's fig5-sine-asymmetry notes ("four at most at 100 Hz"). Cells 62 and 70 show that 2_20240522 has 5. The conclusion is unchanged, since 5 is still less than 12.
- **Record, fig5-whole-cell-depolarization notes:** "the fitted carrier phases of the two ROIs lie near antiphase". The fig6 notes say the same with "near antiphase with each other", and the round-1 response adds "so the positive correlations come from what the LOESS leaves". Cell 71 shows antiphase in 7 of 9 cells only. 4_20240523 is nearly in phase (−2.70 / −2.13), and 2_20240523 is in quadrature (−3.14 / 1.56). Cells with near-antiphase carriers still have r = 0.66 (cell 77), so this explanation is plausible but not shown.
- **Record, fig1 round-1 response:** "the excitation and falling latency hold under the crop ROI". At 20 kHz excitation holds only with O3 b; it is 88.2% with O3 a (cell 18). The record's own deviation states this correctly.
- **Cell 16 and record, ap-selection:** "The peak holds under the crop ROI". This is true in only 12 of 16 crop readings; it fails in the four every-AP readings with O3 b (cell 14). "Lengthened by the noise around F0" has no output behind it.
- **Summary (cell 81) and record findings:** "sine waves of 20 Hz to 10 kHz in 001032, 001033 and 001035". Cell 6 also shows 40 kHz in 001033 and 100 kHz in 001035.
- **Summary table:** figs2 is listed as "(assumed: vehicle split)", while the record also rests it on the crop ROI.
- **Findings with no printed output:** the TTX description saying TTX "caused sustained depolarization", and the 001272 "vehicle control" text. I could not check either from the notebook.
- **README:** every claim is said to be "tested on the ten dandisets". 001031 is not used, and 001034 serves only as the duplicate check.

Everything else in the conclusion cells, the Summary, the README table and the record notes matches the outputs. That includes the latency range 59.8–88.4 ms, the rate range 22.6–42.3 Hz, the block counts, the ratios 2.33–2.80, the p values, 76.0/90.1 V/cm, the fig3c APs and prominences, the TTX tables, the time-constant medians, the fig6 values and the threshold-depolarization range.

**My round-1 reasons in the record.** They are stated faithfully, mostly close to my own wording, each mapped to this file's claim. One simplification: for fig1-pure-sine-excites-all the record gives my outcome as "blocked". I actually judged its latency and ceiling parts (fig1-onset-delay, fig1-max-rate-ceiling) as not reproduced. The reason text includes them.

### 3. Round-1 points

**Resolved:**
- Wrong claims file and dataset mismatch. This was a handover error; the notebook matches this file.
- Problems 1, 2, 5, 8, 12, 13 and 14. The criteria and readings are this file's.
- Problem 3, the plateau oscillations. The new detector leaves c7 at 2.3 V with 1 AP instead of 11 (cell 48), and the variants show the outcomes are stable (cell 80).
- Problem 7, the early latencies. TTX control in cell 20; the median moves from 60.8 to 63.9 ms.
- Problem 9. fig1-20khz-needs-twice-the-field is now blocked.
- Problem 11. Measured amplitudes are printed; fig4 is blocked.
- Problem 10: the LOESS is now R-style degree 2, the carrier phase is fitted and the pulse onset is at frame 20.
- All section C outputs were added.

**Remaining, bearing on conclusions:**
1. **Crop-ROI rule (round-1 problem 4).** The crop is not an ROI the claims file names, and the header says to block when ROI readings disagree. The override cites protocol step 1.6, which I could not check. If the header applies:
   - fig2d-5ap-above-1ap and fig2c-pure-more-aps become methods_underspecified;
   - so does figs1-di8-same-as-fluovolt;
   - ap-selection, fig1-pure-sine-excites-all and figs2-ttx-blocks-depolarization also rest on the crop ROI.
2. **fig6-sine-less-than-pulse.** It is treated differently from fig4-pooled-time-constants, as described in §1.
3. **fig2d-modulated-thresholds-higher.** It should be marked assumed.
4. **fig2-modulated-locks-to-beats.** The O4 b choice is made after the fact; one session decides between reproduced and partially reproduced.
5. **Bleaching (problem 6).** It is still not corrected, which the claims file's F2 supports, and the bias is stated. It does not change fig1-excitation-block, since most neurons still have APs in the last 100 ms (cell 24).
