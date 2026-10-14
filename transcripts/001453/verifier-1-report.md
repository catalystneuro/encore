**Verifier report, round 1: Fouke et al. 2025 (doi:10.1016/j.cub.2025.04.027), dandiset 001453 v0.250518.1950**

The claims file lists 20 claims. The notebook tests 10 and marks 10 as blocked. There is no separate attempt record among my materials, so these counts come from the claims file and the notebook's own claim table. Paper text was read from PMC12218792 (accepted manuscript), saved under `paper/`.

### A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| stimulus-code-link | reproduced | All 13 codes the analysis uses are present. 17 of 18 species×stimulus speed medians are within 10% of the paper code's printed values; the one miss is DC static, 10.52 against 11.9 (cell 18). Angular velocities match to a median of 0.02 deg/s. ZF turning to code 9 is +0.02 deg/s and to code 11 is +1.59 deg/s (cell 19), so the sign cannot settle which of them is lateral right. |
| fig1d-dc-faster-all-codes | reproduced | Species effect F=78.4, p=6e-18. DC median 94.0 px/s against ZF 55.2 px/s (cell 21). The ANOVA treats each fish×code value as independent. A Mann-Whitney test I ran on the per-fish medians printed in cell 21 gives p=0.02, which still passes. |
| fig1d-median-velocity | reproduced | Under all four readings both values are within tolerance: reading (b) gives DC 9.87 and ZF 6.41 mm/s. Species effect p=7.5e-6 with 305 residual df, the same df as the paper's code (cell 24). The 30 Hz variant also passes (9.79 and 6.08, p=0.0011). |
| fig1d-zf-forward-faster-than-static | reproduced | ZF static 4.84 mm/s (18 fish) and forward 8.78 mm/s (25 fish); both within tolerance (cell 28). |
| fig1d-dc-no-modulation | not_reproduced | The pre-specified Tukey test finds 3 significant DC pairs, all against DC static (adjusted p 0.030 to 0.049, cell 30). These come from one fish×stimulus value, DC-sub-2 static at 106.5 mm/s. Without static, or without values above 100 mm/s, no DC pair is significant (cell 31). The main test also finds no significant ZF pair. |
| fig1d-dc-faster-oblique | reproduced (marginal) | Reading (b), which matches the Results' wording "oblique motion (>90°)": right p=0.0002 and backward_right p=0.0047, both below 0.0056, so 2 of 4. backward_left misses at p=0.0071. Reading (a), the intercardinal directions, gives 1 of 4 (cell 33). |
| fig1g-follow-direction | partially_reproduced | ZF right-minus-left is 29.5 deg/s, 23 of 25 fish positive, p=1e-6. DC is 0.88 deg/s, 7 of 12 positive, p=0.15 (cell 35). DC's left median is +0.25 deg/s, and the paper code's printed value is also +0.3 deg/s. |
| fig1h-zf-higher-angular-acceleration | not_reproduced | Under the Methods definition, DC is higher on all 9 stimuli: about 143 to 191 against 55 to 66 deg/s² (cell 38), so 0 of 9 meet the criterion. The code's own quantity gives 7 of 9 (cell 39), but it divides by a mean frame interval that is 8.7 times the true one for DC and 1.4 times for ZF. That biases it against DC. |
| figs1e-dc-respond-less-monocular | reproduced (fragile) | Species effect p=2.5e-6. Medial: DC 3.26 against ZF 13.48 deg/s, p=0.0003. Lateral: DC -1.07 against ZF -0.13, p=0.96 (cell 41). The lateral condition is met only by noise around zero. Under the protocol file's 9/11 assignment DC is higher on lateral (1.07 against 0.13, cell 42), which would make the outcome partial. |
| fig1c-continuous-vs-bouts | reproduced | Steadiness ZF 0.306 against DC 0.908, p=5e-5. It holds in the 128 to 171 Hz files only (p=0.003) and in forward trials only (cell 44). |
| fig1cef-representative-values | blocked (methods_underspecified) | Neither the paper nor the archive identifies the representative fish or trials. I agree nothing can be tested. Population values exist, for example DC forward median 9.69 mm/s against the representative 13.7, but they test a different quantity. |
| fig2d-shared-architecture | blocked (data_missing) | Confirmed from the API: 37 assets, all `*_behavior.nwb`, with only BehavioralTimeSeries. No other DANDI dandiset matches "Danionella". |
| fig2g-dsi-similar | blocked (data_missing) | Same as fig2d. |
| fig2h-fewer-motion-responsive | blocked (data_missing) | Same as fig2d. |
| fig2k-more-monocular | blocked (data_missing) | Same as fig2d. |
| fig2l-bi-ratio | blocked (data_missing) | Same as fig2d. |
| fig3e-longer-swims | blocked (data_missing) | No head-fixed tail tracking in the archive. |
| fig3cd-zf-turn-more | blocked (data_missing) | Same as fig3e. |
| fig4f-longer-on-duration | blocked (data_missing) | No imaging or tail data in the archive. |
| fig4hi-vspn-lateralized | blocked (data_missing) | Same as fig4f. |

None of the claims involves a selection with a chance level, so there was nothing to compare.

### B. Problems

1. [affects a conclusion] `angular_acceleration`, cells 38–39: no check of the tracking-noise floor.
   - DC acceleration on static trials (179 deg/s²) is the same as on every motion stimulus, which is what a noise floor would look like.
   - In my synthetic test, heading noise of 1 to 2 degrees with no turning gives kept medians of 75 to 145 deg/s². That is close to the DC values.
   - DC `f0_vtheta` does not sum to the change in `f0_theta` (ratio 0.09 to 0.89, cell 5), so the DC heading is suspect.
   - The not_reproduced outcome stands, but the reversal (DC higher) may be an artefact and should not be read as evidence against the paper.
2. [affects a conclusion] `trial_measures`, cells 16 and 30: the speed rejection for DC uses the stored `dist` series over 0 to 35 s. It lets through 11 DC trials whose measured speed is above 100 mm/s, up to 1057 mm/s. One of them is DC-sub-2 static at 106.5 mm/s, which alone produces the 3 significant DC pairs in fig1d-dc-no-modulation.
3. [affects a conclusion] `load_session`, code 20: "static" is taken as the first 60 s of a 4 h blank block, which is an assumption. DC static misses the paper code's value (10.52 against 11.9), and two DC fish have a static speed of 0.0. The code-20 window drives both the no-modulation outcome and, through medians, the ZF static value.
4. [affects a conclusion] cell 41, `monocular_table`: the lateral comparison sits on a 0.9 deg/s difference (p=0.96) whose sign depends on the unresolved 9/11 assignment.
5. [does not affect a conclusion] `trial_measures`, speed: path length from Savitzky-Golay-smoothed positions grows with frame rate. In my test a still fish with 1 px noise reads 2.18 mm/s at 150 Hz and 0.48 mm/s at 33 Hz. DC files are mostly fast (11 of 12) and ZF files mostly slow (18 of 25). The 30 Hz variant (cells 22, 25) and the per-rate splits show the species difference survives.
6. [does not affect a conclusion] cells 21, 24, 41: the two-way ANOVAs treat each fish×stimulus value, and in figs1e each side of a category, as independent, which inflates significance. This follows the paper's code, and the per-fish test (p=0.02) still passes for speed.
7. [does not affect a conclusion] Data issues that the notebook reports correctly:
   - 18 of 25 ZF files are at 32 to 35 Hz, against the Methods' ">150 Hz".
   - `f0_vtheta`, `f0_vx` and `f0_vy` have wrong units (per frame, not per second).
   - 25 ZF fish against the 26 in the paper.
   - The archive summary says 25 subjects of one species.
8. [does not affect a conclusion] cell 13: the stimulus-label timing check works for ZF but is inconclusive for DC (4.6 against 0.1 deg/s, with noisy pre-motion bins). Under that limit the DC labels are taken on trust.
9. Helper checks on synthetic inputs all passed:
   - `angular_acceleration` recovers a known sinusoid's peak (289 against 296 deg/s²) at both 33 and 150 Hz.
   - `trial_measures` returns 5.0 mm/s and 20.0 deg/s for constant swimming and turning.
   - Steadiness is 1.0 for steady swimming and 0 for bursts.

### C. What I could not check, and the output that would settle it

- Whether DC angular acceleration is noise. Needed: DC and ZF acceleration in the 0 to 3 s stationary phase, or for stationary fish, plus the same measure computed from unwrapped `f0_theta` in place of the cumulative sum of `f0_vtheta`.
- Why the DC rejection passes trials above 100 mm/s. Needed: a per-trial table of the `dist`-based check speed next to the position-based speed for the 11 DC trials, and the effect on the Tukey test of computing the check from positions.
- The definition of static (code 20) in the paper's code. Needed: the code's static window, and the DC static per-fish values it gives, to explain 11.9 against 10.52.
- Whether the 9/11 assignment can be settled. Needed: per-fish turning time courses for codes 9 and 11 against medial codes 10 and 13, by species.
- Whether the frame-rate differences reflect real acquisition rates or a timestamp conversion error. Needed: the raw timestamp intervals per file (median and spread), compared with the Methods' >150 Hz.
