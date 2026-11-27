I checked the claims file against the paper, its two supplements and the paper's code (github.com/rhuszar/optotagCA1_final, commit 51320d4), made 9 corrections, and judge the file ready for an attempt.

**Checker:** `claims/huszar-2022.yaml: 44 claims, 43 quotes, 54 statistical values, 1 problems`. The one problem is the p-value I added for the new claim. The legend prints it as "P=1.4e-04", a form the checker can't read; I confirmed it by reading Extended Data Fig. 10b. Before my changes the file passed with 0 problems.

I read the supplementary tables from the images in the PDF. The per-mouse counts in Supplementary Table 1 add up to the n values the file uses (96 and 104 sessions, 664 light-responsive cells, 57 maze sessions), and the Table 4 and 5 means match. The statements, quotes and statistics of the other claims hold.

**Changes, by claim**
- **spwr-duration:** The code computes the 36.4 ms as the mean of each session's median ripple duration, over all detected ripples (`ccg_sessionVisualize.m`). I added that as reading (c). The file also said the code uses homecage ripples here; it uses all of them.
- **ed3-depth-control:**
  - The depth resampling is in the code (`hpc/resample_depth.m`), which the file said it wasn't. The code keeps a resampling only when the depth test gives 0.4 < p < 0.6. Only the binning inside the `subsample1D` helper is still open, because that file isn't in the repository.
  - I added the reported fractions the statement rests on: participation 93.8%, theta depth modulation all, spatial information 72.6%, coverage 73.8%.
- **ed5-matched-controls:**
  - The file's "20 equal-count bins" was invented. The code (`subsample2D_local.m`) uses a 2D log10 histogram of 100 × 100 bins, and the criterion now says so.
  - I added the novel-environment panels k to p (P = 3.3e-6, 95.8% and 97.4% of resamplings).
- **fig3c-assembly-cofiring:** I set the expected means to Supplementary Table 4's values (0.0191, 0.0328, 0.0267, 0.0165). The legend's rounded 0.027 and 0.016 fall outside their own s.e.m. tolerance.
- **fig6f-remap-together-novel:** The tercile edges were wrong. The code takes them from SBD and DBD correlations across the familiar and both novel environments, not the familiar ones only. The legend's version and the code's are now two readings.
- **fig7fg-convergence-cofiring:** The code's p-value comes from resampling the pairs' values with replacement into groups of the quintile sizes. The file had called it label shuffling.
- **ed10-waveform-matched-controls (new):** Extended Data Fig. 10, which the Results cite, had no claim. It covers waveform-matched controls for SPW-R, theta-cycle and ratemap cofiring.

**Still open**
- In the new ed10 claim, Extended Data Fig. 10c and f describe their resampling only in the legend. I assumed it bins the way the ed5 code does.
- For fig2b-synchrony-per-animal, the paper doesn't state the per-animal significance threshold behind "11 of 13 animals". The readings already in the criterion stand.

**Ready:** yes. The last `checks` entry says `ready: true`. Nothing is committed.
