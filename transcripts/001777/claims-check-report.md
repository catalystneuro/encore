I checked nothing, because there is still no claims file for DANDI:001777. `claims/001777/` is missing from this checkout and from the git history.

**Checker result:** not run, since there was no file to give it.

**Why there is no file:** the latest claims run (commit 5c16efc2) is labelled "success" but never wrote the file. Its report says a safety classifier stopped the response that would have created `claims/001777/10.1126-sciadv.adq8840.yaml`, so nothing was saved. The transcript shows the draft broke off inside its opening comment, before any claim. The earlier claims run (b723ef24) failed the same way, and the check run after it (694d3392) found no file either.

**Changes:** none. Writing the claims file is the reader's step 3, not this step 5 check, so I didn't write one. I also didn't add a `checks` entry, because there is no file to add it to.

**Still open:** the claims run's report lists details a later check will need to settle:
- **Text and legends disagree:** Fig. 3B gives n = 10 in the text and n = 45 in the legend. Fig. 3D gives P = 0.13 against P = 0.06. Figs. 4A and 4B give P = 0.02 and P = 0.19 in the text, against P < 0.01 and P = 0.16 in the legends.
- **Tests not named:** Figs. 6C, 7D, 7E, 7H, S3 and S4D. No test is reported for Fig. S6.
- **Methods left open:**
  - The stable window is chosen by eye in the code.
  - Percent changes could be computed more than one way.
  - The Fig. 2C windows are not defined.
  - The IPSC amplitude and paired-pulse ratio measures are not described.
  - The sidedness of the tests is not stated.
  - The Fig. S6 deletion groups are not described.

**Ready:** no. The Paper run workflow needs to run the `claims` role for 001777 again, and then `claims-check`. Since it has been stopped twice while writing the file, it may need to write the file in smaller pieces to get past the classifier.
