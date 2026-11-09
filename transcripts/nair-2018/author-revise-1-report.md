I've worked through all nine points in the round-1 report. One outcome changed: fig3c-home-cage-above-both-sessions. The entry re-runs cleanly: `python tools/entry.py all` gives 0 errors and the notebook runs in 19 s. Nothing is committed.

**Outcome changes**
- **fig3c-home-cage-above-both-sessions**: changed from not_reproduced to partially_reproduced, as the verifier proposed. I withdrew my assumption that the dataset's sessions 1 and 2 are the first and second arena trials of a day. The data descriptor calls them "two separate examples", so the 15.9% drop from session 1 to 2 is now reported but not judged, and its measured value is removed.
  - The part that can be tested: the home cage is above both arena sessions by Bonferroni-corrected paired t tests (p = 0.038 and 0.035), but not by Tukey's test (p = 0.30 and 0.19).
  - The finding about session order is now addressed to the data owners as missing metadata (`metadata_insufficient`), no longer a question for the paper's authors.
- **fig3d-gamma-rises-with-time-in-arena**: still partially_reproduced, but now marked `assumed: true` because the result depends on bin width. With the claims file's 1-min bins, r = 0.859, outside 0.72 ± 0.072. With 30-s bins, r = 0.744 and 0.747, which would be inside tolerance and give reproduced. The question to the paper's authors now also asks about bin width and where the time axis starts.
- Every other outcome is unchanged and agrees with the verifier.

**Outputs added or corrected**
- **Fig. 3D**:
  - The 10-min window is now also anchored at the file end, where Fig. 3D puts the transfer. This gives r = 0.885.
  - Reading (b) does not depend on where a file's clock starts. Over whole files it gives r = 0.165, p = 0.011.
  - r is now shown for bins of 20 s to 2 min.
  - Movement in each arena file's first minute, middle and last minute is now printed. The first minute is higher than the middle in 9 of 12 files. That fits arena entry being near t = 0 but does not prove it.
- **Fig. 3B**: added a one-way ANOVA on values divided by each rat's mean, as a variant that is shown but does not decide the outcome. The home-cage rise gives p = 1.6e-9 and the movement-matched comparison p = 7.5e-8. The arena result still shows no effect (p = 0.12 and 0.33).
- **Smoothing fix**: the 3-point smoothing in `bflfp.py` used to pull values at the ends of each file down to two thirds. It now averages only the values that exist; I checked this on synthetic input. Excursion counts are now 10.7 to 14.5 per 20 min, durations 5.1 to 5.6 s, and the excursions outcome is unchanged.
- **Excursion size**: added the scale-free comparison the verifier asked for. The gamma rise over the threshold is 0.39 to 0.44 here, against 0.215 in the paper.
- **Dip tests on log10 power**: with sessions pooled, every test gives p > 0.1. Taking each session alone, one test falls below 0.05: rat 5, home cage, session 1, gamma, p = 0.035. The claims file tests power, not log power, so figs3-unimodal-states stays reproduced. This test is reported in the notes.
- Added `questions/crcns-bf-1.yaml`. It asks a reader whether the claims file's test for Fig. 3B (a one-way ANOVA on per-rat means, with no normalization) is the right one. Under that test the two Fig. 3B claims are not reproduced at p = 0.82 and 0.070; under the variants that account for differences between rats, both would be reproduced.
- Updated the notebook conclusions, summary and header table, the README table, and the record's notes, deviations and findings. Added the round-1 `verifications` block covering all 28 claims.

**Not done**
- The two Fig. 3B claims stay not_reproduced. The claims file fixes their test, and the verifier agreed with both outcomes; the question to a reader covers it.
- I left the threshold-finding function in `bflfp.py` unchanged; the verifier marked this as not affecting a conclusion. The other threshold method runs alongside it and gives nearly the same counts. I documented the case where it crosses early in its docstring.
- The verifier's remaining points (Tukey ignoring the pairing within rats, and the cell 4 text) also don't affect a conclusion. Only the Tukey point needed text, which is now in the fig3c notes.

There are also some untracked files in the working tree that I did not create (`.bashrc`, `.idea`, `scripts` and others); I left them alone.
