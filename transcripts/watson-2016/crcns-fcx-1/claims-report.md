I wrote the claims file at `claims/crcns-fcx-1/10.1016-j.neuron.2016.03.036.yaml`. It has 41 claims, all with quotes, and the quote checker passes with 0 problems.

**Text read:** the accepted author manuscript from PubMed Central (PMC4873379), not the version of record. That covers the Introduction, Results, Discussion, Experimental Procedures and the legends of Figures 1 to 6. I also read supplement 1 (Table S1, the S1 to S5 legends, the Supplemental Experimental Procedures and the figure pages as extracted text) and supplement 2 (only the Figure 1 artwork). The paper links no analysis code. It names only third-party tools (MATLAB, KlustaKwik, Klusters, and FMAToolbox's FindRipples for spindles), so every method in the file comes from the text.

**Counts:** 41 claims, 41 with quotes. 29 claims carry statistics (63 values in all), 40 have a criterion and 17 have expected values. All test data are `dataset`.

**Details the paper leaves open, with the readings named:**
- **Firing-rate groups (sextiles):** "WAKE rate" can mean all WAKE in the session or the WAKE of each cycle. Figure 2F's groups ("mean rate") are read as the same WAKE sextiles, or as sextiles of the nonREM rate.
- **Cells recorded in two WAKE-SLEEP cycles:** they can count once per cycle or once with the cycles averaged.
- **Correlations against normalized time:** the unit is one point per nonREM packet or one per 10 s bin, with rates normalized by the recording mean.
- **Rate-against-rate slopes:** a fit on log rates (from the log axes and the S2D legend) or on linear rates. Cells with zero rate are left out as a standard choice.
- **Burst index:** the Results say ISIs below 15 ms over all spikes; the supplement says 15 ms or less in 10 s bins.
- **Autocorrelogram decay fit:** not described. The readings are a power-law fit to 100 ms or to 500 ms.
- **Synchrony per cell:** firing together with another cell, or firing at all, in a window.
- **UP/DOWN states and spindles:** the deposited detections, or a new detection by the stated rules.
- **Within-UP comparison:** the Results say first against second third of packets; the Figure 4E legend says first against last third.
- **Triplet tests:** the per-sextile test isn't named. The readings are Wilcoxon signed-rank or a t-test against zero.
- **WAKE between packets:** a scored WAKE of 7+ min, or any arousal over 40 s.
- **"Slow-firing" for MAs:** the lowest sextile or the lowest two.
- **Spindle-duration "from … to":** the first and last tenth of normalized time, or the first and last third.

**Inconsistencies in the paper, recorded in the file:**
- Spindle incidence is 1.94 per minute in the Results but 0.049 Hz (2.94 per minute) in Table S1. Both are compared.
- WAKE and REM both have 19.2% of cells above 2 Hz, yet the paper says "all comparisons p < 1e-10". I read the comparisons as nonREM against each of the other two.
- Spindle incidence within packets is printed as R = 0.7, likely a misprint for 0.07.
- The time "neither UP nor DOWN" is said to increase with R = -0.04. This is reported but not judged.
- The WAKE before/after slope interval reads "0.801 – 0.0856" in the Results. The S3A legend's 0.80 to 0.86 is used.

**Missing or unreadable:**
- No main-paper PDF was supplied, and no PDF renderer is installed, so I couldn't read values printed only inside figures. These are the per-sextile R and p of Figures 3B and 4A–B iv, and the triplet counts and asterisks of Figure 5B. Those claims are judged on direction and significance only.
- I couldn't confirm which of the two extracted S5A/S5B value lists belongs to WAKE and which to REM. So the within-WAKE claim is judged on the Results sentence.

Nothing has been committed.
