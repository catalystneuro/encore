I rewrote `claims/000006/10.1038-s41586-018-0642-9.yaml` from the full text, and the quote checker passes with no problems.

**Text read:** the version of record (Nature 563, 79–84, 2018), from the PDF someone supplied and its `.txt` extraction. That covers the main text, Methods, the Extended Data Fig. 1–10 legends and the Reporting Summary. The supplement (Supplementary Tables 1–4) is not in the text.

**Code read:** the paper only links a GitHub organisation (`github.com/SvobodaJanelia`), not a repository. I read the MATLAB `.m` files in `Code/` of `Ephys.zip` from Figshare doi:10.25378/janelia.7007846, version 1 (file 13292708). I did not open the data files in that zip.

**Claims:** 31 claims, all with quotes; none needed an `inferred` note.
- 8 claims carry statistics (10 values), 17 have expected values with tolerances, and 23 have criteria.
- 9 claims rest on anatomy and sequencing data held elsewhere (Figshare, GEO GSE119182, Tasic et al. 2018). The dandiset cannot test them.
- Kept ids: the 9 from the old file. All their criteria are new; the old label-shuffle null, McNemar and Fisher tests are gone.
  - `pt-lower-late-and-motor` now tests selectivity along the late-delay and go-cue coding directions (CDlate, CDgo) with the paper's hierarchical bootstrap.
  - `pt-types-differ-in-timing` is now a summary that depends on six claims.
- New claims: 22, among them unit counts, depth, spike rates and their spread, bursting, selectivity in any epoch, variance explained, CDearly decay in PTlower, coding-direction stability, single-neuron early selectivity, decoding (plain and rectified), CDgo onset, reaction time, the change in coding direction at the go cue, movement termination, and the cohort control.

**Details the paper leaves open, and the readings named for each:**
- **Trial range per unit, go-cue-aligned rates:** (a) the code's ±10-trial range, which it applies only to last-lick-aligned rates; (b) all trials.
- **Unit inclusion:** (a) the code's per-unit rule (>50 trials, >3.2 spikes per trial, >65% correct, unit quality); (b) the Methods' per-session rule (≥50 trials). The code and Methods differ here.
- **Bootstrap:**
  - what a "mouse" is: 4 mice, or the code's 6 animal ids (two right-hemisphere recording sets are numbered as separate animals);
  - whether resampled trials enter the projected rates: no, as in the code, or yes.
  - The code's 100 iterations with a ±1.545 s.d. band is kept only as a variant.
- **Early selectivity 0.41 vs 0.25:** the measure is either the coding-direction-style d′ or the code's ROC d′; the test is not named, so both Student's t and Mann–Whitney are run.
- **Rate heterogeneity "χ2 test":** Bartlett's test is the main reading; the code's two-sample F test is a variant.
- **"Task epoch" in the 122/130 count:** the code's 400 ms sample window, or the full 1 s sample epoch.
- **"Larger" along CDearly:** averaged over the CDearly window or the whole sample epoch. "More consistent across trials" is read as bootstrap s.d. over median.
- **"Remained constant":** significant at every bin, or a significant mean over the last 400 ms of the delay.
- **The CDearly decay p-value (P = 0.34):** computed as the bootstrap fraction at or below zero.
- **CD stability:** Pearson r of the coding-direction weights (from the Extended Data 7d legend) and the code's inner product.
- **CDgo onset:** bin time stamp (start, centre or end), and whether one bin or three consecutive bins count.
- **"Larger / persisted longer" along CDgo:** the window mean or the peak, and the end of the first significant run.
- **Rapid vs slow change at the go cue:**
  - the time at which normalised similarity falls to 0.5 or 0.75;
  - the code normalises to the whole delay epoch, against the legend's last 400 ms; the code's version is a variant.
- **Movement-termination windows:** 200 ms or 400 ms either side of the last lick.
- **"Nearly as diverse" (variance explained):** a ratio of at most 1.3, taken from the code's plot axis. Separately, the code smooths with 100 ms and normalises differently from the Methods.
- **Cohort control:** what counts as "similar", and whether the 495/511/276 unit counts are before or after exclusion.

**Missing from the paper:**
- The reaction-time onset rule is not given, and its confidence level is stated as 95% in the Methods but 99% in the Results.
- Supplementary Table 1 is not in the text; `pt-types-account-for-all-pt` cites it, but its numbers are quoted from the main text.
- No method detail a claim on this dandiset needed is missing beyond the open details listed above.
