I checked the claims file and made seven corrections. It is ready for an attempt, with five problems left open.

**Checker result** (after my edits): `claims/001517/10.1016-j.bioelechem.2026.109283.yaml: 31 claims, 31 quotes, 9 statistical values, 0 problems`

**Changes, by claim**
- **File-level:** `dataset.id` was "001518", carried over from the sibling 001518 file. I set it to "001517", which is what the folder and the header name.
- **fig2a-fluovolt-saturation:** the criterion required the cathodic value at 360 V/cm to be the largest of the series. The paper only says "apparent saturation" there. Now 570 and 780 V/cm must not exceed it by more than the tolerance, which is how the anodic pole was already handled.
- **fig2a-fluovolt-stable:** the criterion now says what happens under its two start/end readings. Both must agree, or the claim is blocked as `methods_underspecified`.
- **fig2b-di8-bleaching:** reading (b) subtracted baseline images from pulse images, so it measured the pulse response plus the drift, not the bleaching. I replaced it with the offset common to both poles, taken from the text's "reduced it by the same ~5%".
- **fig2b-di8-decline-within-set:** the pole is now the cathodic one. Discussion point (a) cites Fig. 2B for a decrease at that pole; the anodic pole is shown as a variant. I also stated what happens under the start/end readings.
- **fig3-fluovolt-nonlinear:** the Di-8-ANEPPS check now covers |IMPC| from 150 to 500 mV. Near zero, a 10% band around the line is smaller than the noise, so the old check would have failed on noise alone.
- **fig7c-full-reseal-mild:** I added a condition for 1000 V/cm: the mean test-pulse dF must be below 100%. The paper's "more intense PEFs" include 1000 V/cm, and Fig. 7C is computed from the means.

**Open**
- **fig6b-ca-train-responders:** the paper never defines a "strong response". The thresholds in the criterion (3 s.d., 50%, 100%) and the 90% for "nearly all" were made up by the claims writer. Fig. 6B prints cell counts and percentages per group, but this environment has no tool to render PDF pages, so I could not read them.
- **fig3-fluovolt-nonlinear:** the 10% departure band and the LOESS spans are not from the paper, which judges linearity by eye.
- **fig2d-lasting-reduction:** the text says "about 20%" and the legend says "≤20%". The tolerance of 18 to 22% follows the text.
- **fig5b-conductivity-calibration:** working Eq. (2) with the Methods constants, a 10-fold rise gives about 1.2 to 1.3%, not the paper's ~2%. The 100-fold figure (about 12%) matches. I kept the claim as the paper states it, so it may fail on the paper's own equation.
- **fig1-pole-dimming:** the test uses the Fig. 4B cells, and the paper does not say the Fig. 1 cell is one of them.

Every finding in the Results has a claim, and every claim comes from this paper. The only thing without a claim is the abstract's 1000 V/cm onset for 0.3-µs pulses. It has no Results sentence, so it can't be a claim under the protocol, which forbids claims from the abstract; the Fig. 4D legend reflects it.

**Ready:** yes, recorded as `ready: true` in a new `checks` entry. Nothing was committed or pushed.
