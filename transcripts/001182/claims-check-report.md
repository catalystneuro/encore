I couldn't check anything: there is no claims file for this dataset. `claims/001182/` does not exist, so I didn't run the checker and have no checker result line to give.

**Why it is missing:** the previous reader run (`transcripts/001182/claims-report.md`) stopped on purpose and wrote no claims. The paper text under `paper/` is the NIH author manuscript (PMC7606611). It does not include Supplementary Table 1, and the Figure 1 legend says all exact p-values and tests are reported there. I confirmed the table is absent from the text. It is only named, at line 829 ("Supplementary Material 1 1606924_Supp_Tab1") and in the legend at line 930. There is also no PDF under `paper/`. Protocol step 1 says to stop when a supplement the results rest on is missing, so that run's decision was right.

**Changes, by claim:** none, because there are no claims. I did not create the file or add a `checks` entry, since a checks entry needs a file to go into. Writing claims myself would be the job of a `claims` run, not a check.

**Still open:**
- Supplementary Table 1 (`1606924_Supp_Tab1`, from the Nature supplementary information or PMC7606611) needs to be added under `paper/`. The published PDF would also help for reading values off the figures.
- After that, the reader (`claims` role) has to run again, including reading the linked code (github.com/DJALab/VMHdm_persistence). Then a new check can follow.

**Ready:** no. There is no claims file to run an attempt from.
