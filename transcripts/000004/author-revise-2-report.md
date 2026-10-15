No outcome changed and I proposed no change, so all 25 outcomes stay as verified: 10 reproduced, 10 partially reproduced, 4 not reproduced, 1 blocked. `python tools/entry.py all` passes on the final run (0 errors). The round is recorded under `verifications`; the verifier agreed with all 25 outcomes. Nothing is committed.

**What I fixed or added, by report point:**
- **2a / 3a, z-ROC slopes (fig5b):** the helper now flags sessions whose five middle z(FA) or z(H) points are all equal, so the fitted slope is not a real estimate. A synthetic check gives the verifier's −0.2074 and is flagged. Six sessions are flagged (59, 60, 93, 99, 119, 2008); the verifier named five, and session 93 also has an undetermined fit (0.415). Without them: 81 sessions, mean 0.792, 64 below 1, t-test p = 6.6e-09, Wilcoxon p = 3.3e-08. The 87-session numbers are kept as a variant, and I added a deviation for this. The outcome stays reproduced.
- **2b, diagnoses:** the text now says 19 of 59 differ: 8 broader, 6 "Lateral Frontal", and 5 that differ in substance (C34 is now among these).
- **2c, statements the verifier could not check:** the notebook now fetches the session list (`defineNOsessions_release.ini`) and `export.py` from the pinned commit and prints the lines used. All 87 files match their session-list entry on age and sex. It also shows that session 98's entry is commented out in that list, which I added to the notes and findings.
- **2d:** the README and summary now say 147 against the paper's 146.
- **2e:** cell 0 now lists fig3 as metadata insufficient.
- **2f:** cell 28 now says that 6 of the 7 files without a start code 55 meet every condition.
- **3b, fig3 cell number:** the printed value goes against the verifier's hypothesis. The Figure 4 unit is at 0-based index 4 (1-based 5) on electrode row 4, so "cell number" is the 0-based index or the row. On that reading the phone-selective unit in session 2009 is cell 2 (or 1), not 3. fig3 stays blocked, and I added a conclusion cell for it.
- **3c, null for the paper's code settings:** the count from the code's settings (147: 1.5 s window, correct trials only) now has its own shuffled null: 5.58%, against which 147 gives p = 2.5e-05. This null uses a separate random generator, so the existing nulls (5.39%, p = 0.18) did not move. My first run showed that sharing the generator would have changed them.

**Not done:** the verifier's round-1 problem 4 (the shared spike/trial clock is shown for only 38 of 87 sessions) is still assumed for the other 49. It is tied to no claim, so I noted it in the round's `reviewed` text. I downloaded no paper text, so nothing new is in `paper/`.

The working tree also has untracked files I did not create (`.bashrc`, `.gitconfig`, `.idea`, `.vscode`, `scripts`, and similar). They should be left out of the commit.
