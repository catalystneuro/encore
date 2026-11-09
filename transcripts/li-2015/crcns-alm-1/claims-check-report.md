The claims file was mostly sound. I made ten corrections, three problems are still open, and the file is ready for an attempt.

**Checker result:** `29 claims, 29 quotes, 18 statistical values, 0 problems`. I ran it before and after my edits and got the same line both times.

I checked the values read from figures against PDF pages 2, 3, 5 and 15. To see the pages I installed PyMuPDF into `$TMPDIR`, outside the repo. The stars in Fig. 1d and Fig. 5b, the bars in Fig. 2d and 2e, the 427/485 axis counts and the Fig. 3e fractions all match the file.

**Changes, by claim:**
- **task-performance:** The file used control trials only, but the paper doesn't say which trials the 78.4% comes from. I listed both readings: control trials only, or all trials.
- **ed2-error-trials-predict-choice:** The criterion required P < 0.05 for r, which the paper doesn't report; it is now labelled a standard choice. The statement's "majority" is now part of the test: more than half of neurons must switch the sign of their selectivity, as the ED Fig. 2c legend says.
- **fig2e-equal-contra-ipsi:** The counts 427 and 485 come from the Fig. 2c sort, which may use the preferred trial type taken from 10 trials. Fig. 2e uses total spike counts. Both are now listed as readings.
- **ed1-no-population-contra-bias:** I added a third reading, all 1,408 units, since ED Fig. 1 shows both cell classes. The criterion now says the result must hold under every reading.
- **antidromic-latency-jitter:** The PT and IT jitter tolerances (0.01 and 0.02 ms) contradicted the criterion's own rounding rule. Both are now 0.05 ms.
- **fig3ei:** The IT fractions in Fig. 3i were misread as 0.2, 0.65 and 0.15. The figure shows about 0.22, 0.56 and 0.22.
- **fig3fj:** The inset fractions are about 0.65 (Fig. 3f) and 0.45 (Fig. 3j), not 0.7 and 0.5. The `n` fields now say it is open which neurons enter the bootstrap.
- **fig4h:** I added how the paper sets preference in the imaging data (average calcium signal during the trial epochs). How the epochs are combined is named as open.
- **ed6b-pt-dose-response:** The criterion listed 0.06 mW, which ED Fig. 6b does not plot for PT neurons. The powers are 0.12, 0.24 and 0.8 mW, and not every mouse was tested at each.
- **ed3-high-power-contralateral-licking:** The criterion left out two parts of the statement: licking in untrained mice and premature licks in trained mice. I added both and noted that the paper gives no test for them.

**Still open (recorded in `checks`):**
- **fig2d:** The text says 389 neurons are peri-movement only and 304 have both; Fig. 2d shows the reverse. The PDF confirms the disagreement, and the criterion keeps both readings.
- **fig5:** The Results define subthreshold power as below 0.25 mW, but the Fig. 5 legend pools 0.12 to 0.8 mW, and ED Fig. 3 calls 0.8 mW high power. The criterion follows the legend.
- **fig2c-dynamic-single-neurons:** The 0.5 bound on the population response correlation is read off the figure and remains an assumption.

**Coverage:** Every main finding has a claim, and none comes from outside the paper. The data descriptor is used only to describe the dataset.

**Ready:** yes. The `checks` entry is appended with `ready: true`. Only `claims/crcns-alm-1/10.1038-nature14178.yaml` changed, and nothing is committed.
