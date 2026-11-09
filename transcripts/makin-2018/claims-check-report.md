I checked the claims file for 000129 and made the corrections below. The file is ready for an attempt. Nothing is committed.

**Checker result:**
- Before my changes: `29 claims, 29 quotes, 12 statistical values, 0 problems`
- After: `31 claims, 31 quotes, 12 statistical values, 0 problems`

The earlier reader said the PDF could not be rendered. I rendered figures 2, 5, 7, 8 and 9 with PyMuPDF installed to a temp folder. Several criteria failed on the paper's own figures, and those are most of the changes.

**Changes, by claim:**
- **intro-gain-over-nearest:** reading (a) now leaves out the static rEFH as well. Figure 2 puts it only about 0.2 dB below the rEFH (+KF) for acceleration, so that reading could never give 1.2 dB. Figure 8's bars (about 0.14, 1.6 and 1.2 dB over the UKF) support reading (b), the UKF.
- **fig2-position-dynamic-gain:** tolerance raised from 0.3 to 0.5 dB, with the reason given. "Some 3 dB" is a round number, and figure 2 shows about 2.5 dB. The `expected` entry is now a list like the others.
- **fig2-linear-worst:** removed the exception that let static KFlatent and static rEFH fall below linear regression for position. Every bar in figure 2 is above zero. The comparison is now per axis, as the figure plots it.
- **fig2-velocity-boost, fig2-sagittal-better:** the bounds and gradings the earlier reader invented are now marked as fixed here, not taken from the paper.
- **fig5-derivative-order:** "overall reconstruction quality" is now the mean over the six decoders other than the two rEFH ones. Figure 5 shows linear regression and the WF decoding velocity better than position. The advantage is now measured as a percent. Measured in dB it falls from velocity to acceleration (1.60 and 1.2 dB in the Introduction), which contradicts the paper's own statement.
- **fig5-advantage-with-binwidth:** names both readings of "relative advantage" (dB difference and percent) and marks its bounds as fixed here.
- **fig7-vel-acc-neurons:** now uses the paper's levels: p < 0.01, or p < 0.05 for the WF in acceleration at f = 1/4. It limits the trend to f = 1/4, 1/2 and 1, and names what the percent gain may be taken over.
- **fig7-kinematic-model-saturates:** now compares slopes per unit f, with two readings of the initial interval. Comparing absolute rises over intervals of 1/8 and 1/2 fails for the UKF in figure 7.
- **fig8-position-variants:** the invented spread bounds failed on figure 8 (static spread is about 0.18 dB). Now the canonical static mean must beat both variants, and no dynamic variant may be below the canonical at bootstrap p < 0.01.
- **fig9-taps:** part (i) now asks for gains from taps at 16 and 32 ms only. Figure 9 shows the tapped and untapped rEFH about equal at 64 ms, and the rEFH has no taps at 128 ms.
- **kflatent-modest:** names three readings of which variables are compared. Averaged over all three, figure 2 puts KFlatent below KFobs.
- **Added two claims:**
  - **advantage-grows-with-derivative:** the relative advantage rises from position to velocity to acceleration, at 64 ms and at each amount of training data.
  - **static-refh-position-worse:** under the static mapping the rEFH decodes position significantly worse than the UKF (Discussion).

**What remains open:**
- **fig8-velocity-variants:** the text says 0.7 and 0.4 dB are lost, but figure 8 shows losses of about 0.3 and 0.4 dB, with the standard-normal variant losing more. The expected values stay the text's, and the criterion asks the author to report both.
- **Code details:** the details the claims cite from the code repository (one-sided bootstrap, pooling of x and y, the unit filter, the transforms) were not checked against it in this run.
- **fig4-advantage-grows:** the paper prints p ≪ 0.01. It is recorded as p < 0.01, unchanged.
