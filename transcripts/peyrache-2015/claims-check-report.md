The claims file is ready for an attempt: the new `checks` entry says `ready: true`. Only `claims/peyrache-2015.yaml` changed, and nothing is committed or pushed.

**Checker result:** before my edits, `34 claims, 33 quotes, 31 statistical values, 0 problems`. After them, `claims/peyrache-2015.yaml: 35 claims, 34 quotes, 32 statistical values, 0 problems`.

**Changes, by claim**
- **fig6a-fast-oscillation:** the statement was wrong. It said "periods of about 1 to 5 ms (130 to 160 Hz)", but the Results speak of *windows* of 1 to 5 ms, and 130 to 160 Hz is a period of about 6 to 8 ms. It now states the windows and the frequency band separately.
- **fig2e-decoded-speed:** added an open reading. The Fig. 2e legend says "actual or Bayesian estimates of HD angular speed", so waking speed can come from the decoded HD or from the actual head direction. Both are now named.
- **fig3b-packet-coherence:** added open readings. The Methods say the 5000 reference vectors are "randomly chosen from the wake recordings", which also allows random waking bins. The criterion had also picked the median over time bins without saying so; mean or median are now both named.
- **fig5b-sleep-tuning-similar:** the statement and quote cover decoding in both directions, but the criterion tested only PoS cells decoded from ADn. It now tests both directions.
- **fig6b-adn-synchrony:** neither the text nor the legend says which state Fig. 6b and its p < 1e-10 refer to. The criterion had assumed waking; it now names waking or the three states pooled as readings.
- **fig7-adn-pos-connections:** the Fig. 7a legend uses a baseline from spikes jittered by ±10 ms. This is now a variant beside the Methods' smoothed baseline.
- **fig2b-pair-correlations-preserved:** the criterion now says its bins come from the Fig. 3a legend, because Fig. 2b gives none.
- **hd-cell-fraction:** added a note. Averaging the per-animal fractions in Supplementary Table 1 gives 49%, not the paper's 41%, so only the mean-over-sessions reading fits the paper's numbers.
- **fig3a-packet-60-degrees:** added the checklist's p < 1e-10 (Pearson) for ADn-ADn and ADn-PoS pairs in all states and PoS-PoS pairs in waking. Only the REM PoS-PoS value had been recorded.
- **sleep-duration (new claim):** the Results report 5 h ± 1 s.d. of sleep per session, a number that had no claim. Its criterion offers two readings of what counts as sleep, because the Methods describe two sessions of about 2 h each.

All other claims checked out against the text, the legends, Supplementary Table 1 and the reporting checklist: statements, sources, statistics, expected values, and the open details already named.

**Still open**
- The Results sentence "HD cell ensembles covered the full span of head-directions" has no claim. The paper gives no measure for it, so I added none.
- No PDF of the article is under `paper/`, so values printed only inside the figures (Fig. 2a,b r values, Fig. 4d errors) could not be read. The thresholds the criteria set in their place remain assumptions.
- Some criteria use made-up thresholds or estimators that are labelled as such: the 30° error in decoding-tracks-hd, 0.5 in fig5b, and the OLE estimator, which the Methods never define.
