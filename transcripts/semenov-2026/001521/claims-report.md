I wrote `claims/001521/10.1016-j.bioelechem.2026.109283.yaml`, and the quote checker passes it with 0 problems. Nothing is committed.

**Text read:** the version of record (a PDF supplied by a person, plus its extracted text): main text, Materials and methods, figure legends and Data availability.
- The paper has no supplement.
- It links no code, so there was none to read.
- Data are "available on request".
- I couldn't render PDF pages here (no PyMuPDF or poppler installed), so I read the figures only from their legends and the Results.

**What the dataset holds:** by its archive title and description, only the Fluo-4 calcium imaging of CHO cells after a single 1-µs pulse (Fig. 6A). The other claims (potentiometric dye imaging, Gd3+, 60-pulse trains, two-pulse recovery) are there to cover the paper's main findings, and the dataset likely cannot test them.

**Counts:**
- 27 claims, all with quotes, none inferred.
- 6 claims carry statistics, 8 tests in all: paired t-test, one-sample t-test, single-tailed t-test, 2-tailed t-test, two-sided t-test.
- 16 claims have criteria.
- 3 claims are on Fig. 6A itself:
  - Ca2+ entry at 1000 and 1200 V/cm.
  - The signal stays raised through the 5 minutes.
  - The 780 V/cm rise is not significant (a claim of absence).

**Details the paper leaves open, with the readings named:**
- **Fig. 6A field strengths:** given only as "0 to 1200 V/cm", with 780, 1000 and 1200 named. The author takes the set from the dataset.
- **"averaged across 14 cells":** this can mean 14 cells per field strength, or 14 in all.
- **Test for the Fig. 6A significance claims:** not named. Readings:
  - (a) a one-sample t-test of each cell's end-of-recording ΔF against zero, the test Section 3.6 uses for the trains. This is the primary reading for the absence claim.
  - (b) a two-tailed Student's t-test against the 0 V/cm group.
- **Which post-pulse value is tested:** not fixed. Readings: (a) the end of the recording, averaged over the last 10 frames (a standard choice), or (b) each cell's peak ΔF.
- **Region and background placement:** the size and position of the circular region and the cell-free background region are not given. I treated them as a standard choice that should not change the outcome.
- **"Strong" Ca2+ response (Fig. 6B):** not defined. Readings: above the largest response among the 0 V/cm (or lowest-field) cells, or above 3 standard deviations of that group.
- **Bounds the paper judges by eye:** linearity, the cosine fit near the equator, and the drop in response within a set. I fixed those bounds myself and said so in each criterion.

**Missing:** nothing the claims needed from the text is missing. The one gap is the Fig. 6A figure itself, which I couldn't open, so its exact field-strength steps and group sizes are unread.
