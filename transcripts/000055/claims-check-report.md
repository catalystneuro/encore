I made eight corrections and added one claim. The file is ready for an attempt (`ready: true`).

**Checker result:** before my edits it read `23 claims, 21 quotes, 14 statistical values, 0 problems`; after them it reads `24 claims, 22 quotes, 14 statistical values, 0 problems`.

I checked every claim against the paper's full text and against the code the paper links (BruntonUWBio/naturalistic_arm_movements_ecog, at the commit the file names, 04c6faf). The quotes, sources, p-values, Table 1 intervals, the Table 2 days per subject (55 subject-days) and nearly every method detail credited to the code are correct.

**Changes, by claim**
- **Header:** the code fits models at bad electrodes too and keeps them in the Fig. 6c-d box plots. The Methods and the Fig. 1 legend drop bad electrodes, so good electrodes stay the main result and the code's choice is recorded as a variant.
- **fig2-reach-shape:** the statement left out "minimal intersubject variability" for reach duration and magnitude. I added it and tied it to the criterion's existing 10-of-12-subjects rule.
- **fig2-bimanual-skew:** the paper's "less skew for subjects 02, 04 and 05" covers both bimanual ratio and overlap, but the criterion judged the ratio only. It now uses both.
- **fig4-precentral-subject-variability:** added the code's second subtraction of the -1.5 to -1 s baseline from each subject's median. I also said where the 0 to 0.5 s window comes from: the Methods' banded analyses, since Fig. 4 fixes no window.
- **extfig5-1-baseline-reduces-day-variability:** the test for "clear variability remains" (median SD above 0) could never fail. It is now judged through the day effects of fig5-recording-day-effects, which the Results give as the variability that remains; I added that dependency.
- **fig6c and fig6d-upward-reaches:** added the code's inclusion of bad electrodes as a variant.
- **fig6d-angle-and-day-largest-coefficients:** the paper does not say how coefficient magnitude is summarised, and its box plots show signed values. The criterion now names two readings: the median of absolute values, and the absolute value of the median. I also noted that the Results cite Fig. 6c for coefficients that are actually in Fig. 6d.
- **extfig6-2-angle-most-retained:** the statement includes the order of the next four features, but the criterion only reported it. The order is now judged under two readings of which regions it covers; failing it gives a partial outcome.
- **Added extfig2-1c-contralateral-larger:** contralateral wrist displacement is larger than ipsilateral (Extended Data Fig. 2-1c, cited in the Results). No claim covered it. The rest position is left open with two readings, and the threshold for "substantially" is the file's own.

**What remains open**
- Many criteria turn words the paper never measures into thresholds of the file's own, for example "most" as more than half, peaks within 15 degrees of ±90, and waking hours as 08:00 to 24:00. They are readings, not the paper's methods.
- **discussion-day-changes-small:** "day-to-day changes" of ±1-2 dB are undefined. The file reads them as the largest deviation of a day mean from the subject's mean; the range of day means is another reading and would be about twice as large. The voltage unit behind the 10-50 dB level is also not stated.
- **cohort:** the stated SDs are used as tolerances on the means. The protocol allows this, but they are wide (29.4 ± 7.9 years, for example).
- The Extended Data figures are EPS files that are not in the text, and no PDF was supplied, so only their legends could be checked.

Nothing was committed or pushed.
