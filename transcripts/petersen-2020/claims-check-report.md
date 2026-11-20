I've checked the claims file against the full paper and corrected it in 11 places; it is ready for an attempt. Nothing was committed or pushed, and only `claims/petersen-2020.yaml` was changed.

**Checker result:** `46 claims, 46 quotes, 31 statistical values, 1 problems`. The one problem is that the checker could not find `8e-05` for fig5h-time-lags-increase. The Figure 5H legend prints "P = 8.0 −5", and reading it as 8.0e-5 is correct, so I left the value as it was.

**Changes, by claim**
- **Opening comment:** it said buzcode and FMA Toolbox are spike-sorting and classification tools. The Key Resources Table lists them as general MATLAB analysis tools, and the paper never says which of their functions it used. Corrected.
- **cooling-time-course:** it used only the Methods' figures (10 to 12 min, about 50 trials). I added the Results' figures (about 15 min, 20 to 60 cooling trials) as a second accepted reading.
- **fig6c-worst-trials-4-to-8:** the temperature and theta minima were allowed anywhere in trials 2 to 10, a window not in the paper. Narrowed to the paper's trials 4 to 8.
- **suppl5j-errors-best-theta-frequency:** the pass rule now checks both the correlations and the partial correlations, as the statement and the legend do.
- **fig4e-speed-decreases-within-session:** dropped "independent of cooling", which the paper does not say, and added Figure 4E to the source.
- **fig4c-fp-flfp-correlation:** the spread of fp against fLFP was compared by interquartile range. It now uses standard deviation, which is the spread the Results report (0.95 against 0.38 Hz).
- **fig4ac-fp-flfp-difference-preserved:** added the fp minus fLFP differences from the paper's own means (2.2, 1.8 and 1.9 Hz), to be reported alongside the attempt's.
- **fig4a-frequency-temperature-slopes:** marked two details as the file's own choices, since the paper gives neither: measuring temperature at the field's spikes, and the Hz per °C unit of the slopes.
- **fig4f-speed-theta-power:** removed the required positive sign and the "4 of 5 rats" rule, neither of which is in the paper. It now needs P < 0.05 under one reading (in every rat under the per-rat reading), and the sign is reported.
- **fig5cg-compression:** noted that Figure 5C puts distance on the y axis. The file reads the fit equation's x as distance anyway, because only that reading makes b a period in ms, as the Methods define it.
- **fig5h-time-lags-increase:** comparing lags as absolute values is now marked as a choice the paper does not make.

**Still open** (recorded under `checks`)
- buzcode and FMA Toolbox were not read. The paper does not say any analysis used them.
- fig4ac-fp-flfp-difference-preserved claims no change, but the paper ran no test. Its own means show a 0.4 Hz drop, so the default signed-rank test over 365 fields may well find a difference. The outcome rests on that default test.
- Several pass rules are the file's own thresholds, not the paper's:
  - P < 1e-6 in suppl2-place-cell-rates-decrease;
  - 90% of position bins in suppl3-theta-cycle-duration;
  - two of three states in suppl2e-trial-speed-theta-frequency;
  - at least 10 fields per speed bin and a bootstrap interval in fig4gh-fp-speed;
  - a rank-sum test per rat as a fallback in fig6d-errors-increase.

  They turn words like "consistently" into a test without changing what is measured, so I left them.
- The paper does not fix when the cooling state ends or how the place fields of Figures 3 and 4 were bounded (they were "manually defined"). The alternative readings in the opening comment stand.

Every main finding has a claim, and every claim comes from this paper.
