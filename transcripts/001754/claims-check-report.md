I checked the claims file for 001754 against the paper. It is ready for an attempt, with the open points listed below.

**Checker result:** `claims/001754/10.1038-72910.yaml: 10 claims, 10 quotes, 0 statistical values, 0 problems`, both before and after my edits. There are no statistics entries because the paper reports means ± s.e. and "not significant by Mann-Whitney" but no p-values.

**Changes, by claim**
- **Opening comment:** the paper names the rectangular preflight track only for rat 2 (Fig. 2b). The comment had said all rats ran it; it no longer does, and reading S-b no longer requires a rectangular-track session.
- **si-rat3-fd4-vs-preflight, fig3-stability-across-sessions:** the sources now point at the paragraph beginning "The mean spatial-information content for all 7", sentences 1 and 2. They had cited sentences of the paragraph before. I based this on a line break in the extracted text after a sentence end; I could not render the PDF to confirm it.
- **flight-spatial-code:** the source and criterion now cite both paragraphs. The outcome rule did not say what happens when a claim it depends on is only partially reproduced; it now does.
- **si-rat1-fd9-vs-preflight, si-rat3-fd4-vs-preflight:** the criteria now say that the paper does not call these rats' preflight cells "active", nor say which track they were recorded on, and how each point is read.
- **theta-normal:** the speed split and the 6 to 10 Hz band are now marked as standard choices, not the paper's.
- **ripples-normal:** I removed the unsupported statement that 100 to 250 Hz was "the band of ref. 15's era". The band, the detection threshold and the sharp-wave filter are now marked as standard choices.
- **three-orthogonal-surfaces:** the outcome rule left some cases undecided, such as part (ii) failing for both rats. It now decides every case.

The statements, quotes, expected values and tolerances (the paper's standard errors, and 10% for cell counts) match the paper. Every main finding has a claim, and none comes from outside this paper. A `checks` entry is added with `ready: true`.

**Open**
- **Measures the paper does not give:** direction-selectivity, fig3-stability-across-sessions, fd4-abnormal-selectivity, theta-normal, ripples-normal and three-orthogonal-surfaces are each judged by one or two standard readings. A different reasonable choice could change their outcome.
- **fd4-abnormal-selectivity:** the paper gives this only as unpublished observations. Reading "abnormal" as lower spatial information than preflight is only one reading; unstable or misplaced fields are others.
- **Mann-Whitney test:** the paper prints neither its significance level nor whether it is two-sided. The file keeps the two-sided p < 0.05 reading.

**Ready:** yes. Nothing is committed or pushed.
