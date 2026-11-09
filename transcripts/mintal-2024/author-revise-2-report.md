No outcome changed. All 18 stay as round 2 verified them: 12 reproduced, 4 partially reproduced and 2 blocked. The verifier agreed with all 18, so nothing goes under `proposed`. The entry re-ran cleanly twice with `python tools/entry.py all` (0 check errors, notebook passes in about 9.5 minutes), and the conclusions match the final run.

**Outputs added**
- **collection-window (cell 14):** prints the first three rows. The file is sorted newest first, so its first row (the Table 1 sample) is the latest timestamp. It also prints the 26-day count under both readings (26 each) and the R filter's count on `data_cleaned_corrected`, the rows the code actually filters: 451 (461 on the raw rows).
- **uni-and-landscape-placements (cell 29):** prints the economic scores with statement 10 or statement 21 left out. PS then scores 52.5 or 47.5, still below DEMOKRATI (55.0), so neither variant explains Fig. 3. The conclusion and notes now cite this output instead of work done only while preparing.

**Text corrected**
- **collection-window (cell 15, notes, finding):** now give 451. They say the R code parses both the timestamps and the cut-off as UTC, so it compares the values as given. Its comment suggests local time but does not settle it.
- **efa-eleven-factors:** I withdrew the unshown "looser optimiser tolerance" sentence. The 12th polychoric value now reads 0.0106, the value cells 51 and 53 print in both runs. The run the verifier reviewed printed 0.0103, so this value varies slightly between runs; the count stays 11 either way.
- **age-education-inconsistencies:** fixed the misquotation of "upon initial review" in the notes, and in the reader question in `questions/figshare-24949470.yaml`, which had the same error.
- **README:** the kappa line now gives both parts of the assumption (quadratic weights, "No opinion" left out).
- **Record:** round 2 is added under `verifications`, with the verifier's reasons in its own words and my response for each claim.

**Not done**
- **Figure overlay:** the placements and the clustering still rest on figure readings that the verifier cannot check against the images. The registry's check refuses code that reads an image file, so I could not draw the readings onto the figures in the notebook.
- **Open questions:** the kappa reading and the age–education counts stay with the paper's authors and a reader, as before.

Nothing is committed; the workflow commits the changes.
