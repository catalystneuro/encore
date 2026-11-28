**Checker result:** `claims/carrier-2026.yaml: 29 claims, 29 quotes, 70 statistical values, 0 problems`. I got the same result before and after my edits.

**Changes, by claim**
- **fig2h-cb-q10-125-unchanged:** the printed F(1,148) needs 152 points. Nine preparations in two salinities over the eight steps from 10 to 24 C give at most 144, so the stated set cannot be the one that was fitted. I added two readings: W-a uses every crab 1.25x ramp (n = 10, as in Fig. 7C) with their 1x ramps over 10 to 24 C; W-b uses the 9 paired preparations over 10 to 26 C. The point count is to be reported.
- **fig7c-species-q10-125:** I removed reading T-a (10 to 22 C). F(1,175) needs 179 points, and 24 preparations over seven steps give at most 168. T-b and T-c stay.
- **fig5d-ha-q10-salinity-unchanged:** I added a note that the printed degrees of freedom confirm the 10 to 24 C and 10 to 22 C ranges and rule out ranges one step shorter.
- **fig2i-cb-neuron-crash-counts:** the statement gives LP crashing in every preparation at every salinity, and PY in every preparation at 0.75x, but these counts were missing from `expected`. I added all four.
- **fig6b-ha-lp-crash-temp-salinity:** the criterion said n = 18 for 1x, but the 1x tolerance (0.97) was computed with n = 19. I corrected the text to n = 19.
- **fig2i-cb-neuron-crash-temps-similar and fig6a-ha-py-crash-temp-salinity:** the criteria presented the Geisser-Greenhouse correction as the paper's method. The Methods never name it; it is only inferred from the fractional degrees of freedom. It is now marked as an assumption.
- **fig8-invivo-rhythm-maintained:** the 0.3 to 3 Hz band and the "three times the median power" rule are not from the paper, which judges the bands by eye. The criterion now says they are standard choices and that the outcome rests on them.

All other values check out against the paper: quotes, p-values, F statistics, confidence intervals, means and n, the Q10 tolerances (half the CI width), and the tolerances on means (SEM from the printed SD and n). Every main finding has a claim, and all claims come from this paper.

**Still open**
- I could not render the PDF either, so the bar heights in Figs. 1E, 4E and 9 are still unread. That covers the lobster crash fractions at 1.25x and 1.75x and the mortality percentages.
- Tolerances on means use the SEM, which is narrower than the "stated spread" the protocol names. The file's opening comment gives the reason, so I kept them.
- The paper contradicts itself in a few places, and the paper alone cannot settle them. These are the inconsistencies the file's opening comment lists:
  - the n in Fig. 4B
  - the P value and label in Fig. 4D
  - whether PY on or PY off is the exception in Fig. 3C
  - which panel of Fig. 9 is which species
  - the Fig. 2F summary sentence
  - three different crab 1x crash temperatures
  - the lobster 0.75x n

**Ready:** yes. The `checks` entry records `ready: true`. Only `claims/carrier-2026.yaml` was modified, and nothing is committed or pushed.
