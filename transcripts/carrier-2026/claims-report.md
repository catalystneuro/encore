I wrote `claims/carrier-2026.yaml`. The quote checker reports 29 claims, 29 quotes, 70 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the version of record (J Neurophysiol 135: 797–814, 2026): main text, Methods, all nine figure legends, Table 1 and Data availability. The paper has no supplement and cites none. It links no code repository. It says its scripts are in the two Zenodo records, but the archive file lists show no separate script files, so any scripts are inside the data zips, which I did not open. So no code was read.

**Claims.**
- **Totals:** 29 claims, all with quotes. 23 report statistics and 29 have criteria.
- **Crab, isolated nervous system (both datasets):** salinity at 10 °C (Fig. 1B, 1D, 1E); crash temperature in 0.75x and 1.25x saline (Fig. 2B, 2E); temperature sensitivity (Q10) in 0.75x and 1.25x (Fig. 2G, 2H); the frequency rise in 1.25x (Fig. 2F); the mixed-effects model; neuron crash counts and crash temperatures (Fig. 2I–K).
- **Lobster, isolated nervous system (`zenodo-17624449`):** Q10 (Fig. 3B); phase relationships (Table 1); salinity at 10 °C (Fig. 4B, 4D, 4E); LP crashing before PY (Fig. 5B); the mixed-effects model (Fig. 5C); Q10 across salinities (Fig. 5D); PY and LP crash temperatures across salinities (Fig. 6A, 6B).
- **Comparing the species (both datasets):** frequency at 10 °C; Q10 in each saline (Fig. 7A–C); crash temperatures (Fig. 7D–F).
- **Live animals (`zenodo-17794764`):** the rhythm holding during 1-hour salinity exposures (Fig. 8) and deaths after 15-hour exposures (Fig. 9).
- **Tolerances:** for means I used the standard error worked out from the stated SD and n, because the SD is the spread across preparations. This departs from the protocol's "stated spread" default, and the file gives the reason. For Q10 values I used half the width of the paper's 95% CI.

**Details the paper leaves open, with the readings named:**
- **Q10 fit:** a least-squares fit of the exponential model on raw frequency, or a linear fit of log frequency on temperature.
- **Fig. 3B points:** the fit uses either the step means (its F(1,8) implies about 10 points) or every preparation's values (the same Q10 appears again with a different CI and n = 19).
- **Crab mixed model:**
  - Which salinities are in it: 1x with 1.25x, 1x with 0.75x, or all three. The legend sits under the 1.25x figure, but n = 11 is the 0.75x set.
  - Whether salinity is a number or a factor, and whether the response is frequency or log frequency.
  - The random-slope candidates.
- **Lobster mixed model:** salinity as a number or a factor, and frequency or log frequency.
- **Fig. 7C temperature range:** 10–22, 10–24 or 10–28 °C.
- **Preparations with two 1x ramps (Fig. 7B, 7E):** use every ramp or only the first.
- **Frequency at 10 °C, n = 19 and 15:** taken from the first ramp step or from the baseline of the salinity series.
- **1x baseline segment for the salinity tests:** the end of the 30-minute baseline, or the 1x period just before the series.
- **Levene's test:** centred on the mean or the median.
- **Table 1 "95% CI" column:** I read it as the half-width; it could be a standard error.
- **Live-animal spectrograms:** the window settings are a standard choice that cannot change the outcome. Whether a frequency band counts as present has two readings: a peak-power rule over the full hour, or over the first 30 minutes.
- **Throughout:**
  - Burst detection criteria are not given.
  - Whether frequency is the mean of 1/period or a burst count is not given.

**Inconsistencies in the paper, recorded in the file:**
- The Fig. 4B legend gives n = 8 and the text n = 9.
- The Fig. 4D legend labels the 1.25x comparison as "0.75x" and gives P = 0.8 against 0.9 in the text.
- The Fig. 3C legend says PY-off changed with temperature; the text and Table 1 say PY-on. I followed Table 1.
- The Fig. 9 legend puts crabs in panel A; the text puts lobsters there.
- The Fig. 2 summary says 1.25x saline lowered frequency; the paragraph presenting Fig. 2F says it rose similarly.
- Crab 1x crash temperatures appear as three different means for different sets of preparations.
- The lobster 0.75x n is 10 in Fig. 5C and 14 in Fig. 7.

**Missing:**
- **Bar-graph percentages:** the PDF could not be rendered in this run, so I did not read the percentages in Figs. 1E, 4E and 9. Those claims use only the counts the text states, and the 15-hour mortality claim has no expected values.
- **Survival records:** the archive description does not say whether the 15-hour survival records are in the deposit.
