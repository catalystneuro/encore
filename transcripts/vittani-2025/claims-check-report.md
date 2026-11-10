I've checked `claims/vittani-2025.yaml` against the paper and supplement and marked it ready for an attempt. Nothing is committed or pushed.

**Checker result:** before my edits it reported `40 claims, 40 quotes, 43 statistical values, 0 problems`. After them it reports `40 claims, 40 quotes, 46 statistical values, 0 problems`; the three added values are paper tests that were missing.

**Changes, by claim**
- **Header:** removed the statement that Prism applies the Geisser-Greenhouse correction by default. The paper doesn't say it; the header now says only that the fractional degrees of freedom imply it.
- **figs1n-startle-camp-awake-higher:** the paper says the awake startle response was "higher and longer". I added "longer" to the statement. The criterion reports duration but doesn't judge on it, because the paper gives no measure or test for it.
- **figs1p-whisker-camp-length:** the statement says the response lasts through the stimulation, but nothing checked that. I added a check, with its threshold named as a standard choice.
- **fig2j-timing-anesthetized:** the file said the paper pairs the second arteriole cohort with the Figure 1 cAMP mice. No passage says so. It is now called an inference, and which 1 s cAMP trace to use is listed as open, with three readings.
- **fig3b-camp-awake:** "and not in control mice" went beyond the paper, which only says bPAC mice rose significantly more than controls. Restated.
- **awake-vs-anesthetized-camp-kinetics:** the 10% bound for "similar peaks" isn't from the paper. It is now named as a standard choice.
- **fig3k-timing-awake:** added a reported check that dilation starts as the cAMP rise slows, as the statement says.
- **fig5h-j-ca-ip3r2-reduced:** added two findings the statement left out: the Ca2+ rise is "slightly delayed" in IP3R2-/- mice, and peaks fall over successive recordings. I added that recording test (P = 0.0012) to the statistics and to the criterion.
- **figs5a-d-ca-transient-camp-sustained:** the criterion now tests what the paper says: Ca2+ falls before dilation starts and keeps falling during it. It now requires all four groups, as the paper claims, instead of an invented 3 of 4.
- **figs5i-twophoton-ca-camp-correlation:** the half-peak level used for "transient" and "sustained" is now named as a standard choice.
- **fig6c-e-camp-mild:** added the two missing paired t tests for rise and decay time (Figure S6A and B). The statement now says what the criterion already judged, that the recordings don't differ. The similarity to sensory-evoked cAMP is now reported.
- **mild-dilation-size:** the comparison with whisker stimulation in the statement is now reported.

**What remains open** (recorded in `checks`)
- **fig3cd-camp-awake-stable:** two tests print numerator degrees of freedom below 1 (0.6271 and 0.8315). That is impossible for the correction with four recordings, so an attempt can't be expected to match them.
- **fig4g-i-arteriole-ip3r2-no-difference:** the printed df of 34 doesn't fit 75 arterioles, and the paper gives no threshold for excluding vasomotion.
- **Table S1:** the 25 ms cAMP values are said to average recordings "#1 and 6", but only four recordings were made.
- **Minor findings without a claim:** a few small results have no claim. None is a main finding.
- **Discussion paragraph numbers** in the sources couldn't be checked: the text has no paragraph breaks and the main-text PDF isn't under `paper/`.

Every main finding has a claim, and every claim comes from this paper.
