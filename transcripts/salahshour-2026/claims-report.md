I stopped without writing any claims, as protocol step 1 requires. `claims/salahshour-2026.yaml` was not created, and the working tree is unchanged.

**Text read:** the arXiv preprint v1 (arXiv:2610.00990v1, 1 Oct 2026) in `paper/10.48550-arxiv.2610.00990.txt`. I read the main text, the Methods (Sec. 4) and the legends of Figures 1 to 8. There is no PDF.

**What is missing:**
- **The supplement.** The paper relies on Supplementary Notes S1 to S9 and Table S2, which "lists every claim, the test applied to it and the outcome". The note at the end of the text file says arXiv has no supplement for this preprint: the source has only the manuscript and its eight figures, with no ancillary files.
- **The parts that DANDI:000289 would test.** The paper uses that dandiset (Basnak and Wilson, version 0.240801.1040) for Secs. 2.7.2 and 2.7.3. The Methods hand every method detail for those sections to Note S7: "ring reconstruction, session inclusion, the cue-shift null and the placement-error deconvolution are specified in S7". The cue-free bump-frame estimator, the ring embedding from the correlation matrix, the Gaussian, exponential and square fits, and the gain-ladder and synthetic controls are also described only as "(S7)". Without S7 no criterion can be written from the paper.
- **The code.** "The analysis code will be deposited in a DOI-bearing repository before publication." No repository is linked, so none could be read.
- **Numbers dropped from the extracted text.** Several key values for the 000289 claims are blank, for example "below 0.05 in of 101 sessions", "a median of . across flies", "Mn/M1 = , .152", "Deconvolving the median .9◦ split-half placement scale" and "a placement error of about ◦". Others outside 000289 are blank too: "κ2 = ." in Sec. 2.5.2 and "in of 30 flies" in Sec. 2.7.1. Without the PDF these values can't be recovered.

**Claims:** none, so there are no quotes, statistics or criteria, and I did not run `tools/claims_check.py`. No open details are named, because the method for each claim cannot be fixed without S7.

To unblock this paper, supply the Supplementary Information (Notes S1 to S9, Table S2), or at least Note S7 and S9 for the 000289 claims, and preferably the PDF and the analysis code once deposited. Then re-run the reader. Earlier reader runs for richardson-2018 and fujimoto-2026 also stopped on a missing supplement and succeeded once it was added.
