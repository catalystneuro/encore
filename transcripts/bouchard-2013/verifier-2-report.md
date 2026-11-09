## 1. Outcomes

The claims file has 22 claims, and the attempt record gives an outcome for each of them. I agree with all 22: data-composition is partially reproduced; active-electrodes is blocked (methods_underspecified); fig1c-e and the seven spatial claims are blocked (metadata_insufficient); fig1f-h is not reproduced; suppfig6 is reproduced; fig3d is not reproduced; pca, fig4a, suppfig11, fig4c-d, fig4ef, fig5d and suppfig13 are blocked (methods_underspecified); fig5c and suppfig9 are not reproduced. Every count, range and measured value in the record matches the printed outputs (cells 20, 23, 26, 29, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64).

Three places where the claims file may misread the paper. I report these and have not corrected them:
- **suppfig13:** a reading reproduces only if the pair count is 4623. That count is fixed by which syllables the dataset holds, not by the effect the paper reports. Read strictly, every reading is not reproduced.
- **suppfig6:** grouping electrodes by their largest weight almost guarantees the result. The test also holds on permuted weights in 94 of 96 readings (cell 34).
- **suppfig9:** jaw against larynx is judged at p > 0.05, but the paper says P > 0.2. This does not change the outcome, since the measured p is 5e-11.

## 2. Sentences the outputs do not support

- **Attempt record, fig2a-lips-dorsal notes:** "the median z coordinate of the top 10% of lips weights is above that of the tongue weights in EC2 (36.6 against 15.6) and GP31." Cell 32 prints `GP31: ... Tongue no window`, so there is no GP31 comparison. This is for information only and affects no outcome.
- **README:** "The claims blocked as methods underspecified depend on details the paper does not fix: [CV set, baseline, z-scoring, projection]". **Summary (cell 66):** "The blocked outcomes of the state-space claims and of active-electrodes come from these readings giving different results." Neither holds for fig5d. Cell 58 shows its split comes from the reading of R (all 120 "mean of three" readings fail) and from the cluster reading (all 48 k-means readings fail). The four listed factors show similar mixes at every level.
- **Cell 59 and the fig5d notes:** "the reading of R decides the split". This is incomplete. With the matching feature set, k-means clusters still fail all 24 readings (cell 58 table), so the cluster reading also splits the outcome.
- **README:** "It takes about 20 minutes, 14 of them streaming about 42 GB". Cell 3 prints 1002 s cumulative, about 16 minutes of processing after the 52 s metadata pass. The total of 21.6 minutes (cell 67) fits "about 20". The 42 GB figure is printed nowhere.
- **Cell 10** (a note, not a conclusion): "EC9 has 24 consonant labels". Cell 8 gives 19 plus /ch/, /dh/, /j/ and /sk/, which is 23.

Every other "Result:" sentence, the Summary and the remaining record notes match the outputs.

**My round-1 reasons in the verification record.** They are faithful condensations of my rows plus the related B points. Three gaps:
- The cell numbers are from round 1 and are now stale. For example, "cells 8, 18" and "cell 22 prints `[]`" now refer to cells 8/20 and 26.
- Under active-electrodes, the record drops part of B3: that the /thi/ split also flips GP31's silhouettes and the fig4ef late-window tests.
- "The verifier asked for …" restates my section C in the third person, not in my words. That is acceptable, but it is a paraphrase.

## 3. Round-1 points

**Resolved:**
- **B1:** cell 5 now reads each file's objects. EC2-B1 holds a power spectrum, and no file has audio.
- **B4, B5, B6, B8:** fixed or documented as I asked.
- **B7:** I read the `separability` code in `bouchard.py`, and it now leaves out a token's pairs with its own copies, correctly.
- **B9:** recorded as a deviation.
- **B10:** confirmed by the permutation null.
- **B11:** the artifact-trial variant is run for active-electrodes and fig3d.
- **B12:** recorded as a finding.
- **Section C:**
  - the processing module is listed;
  - the all-vSMC count for fig1f-h is printed;
  - outcome counts per reading factor are printed;
  - the artifact variants are run;
  - I checked the Supplementary Figure 12 transcription myself this round. I extracted the image from the supplement PDF, and all 15 consonant rows and the 4 vowel rows match cell 16.

**Still open, and bearing on a conclusion:**
- **B2:** that GP31 is EC31 and GP33 is EC33 remains an assumption, and GP33's hemisphere cannot be checked. This affects data-composition and is recorded as a deviation; no field in the files can settle it.
- **B3:** GP31's /thi/, with 2 renditions, alone creates the CV-set split for active-electrodes. The one reading within tolerance (rest, 15+ CVs: 27.0) relies on trials the files mark as ECoG artifacts. Without them, GP31's count falls from 31 to 2 and the mean to 15.0. The blocked outcome stands, but under every variant tried no reading supports about 30 electrodes.
- **suppfig13:** its outcome stays blocked only because the attempt treats the pair-count failure as partial. That rests on the claims-file issue above.
- **suppfig6:** it is reproduced under a criterion that barely discriminates. The outcome is correct under that criterion, but it shows little.
