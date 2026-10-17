**Round 2 verifier report: Xu et al. 2022 on DANDI 000239 (version 0.230607.1752)**

The paper text is from PMC9109820, saved as `paper/pmc9109820.xml` and `paper/pmc9109820.txt`. Cell indices below are the code-cell positions in the re-executed notebook. They differ from round 1 because cells were added.

## 1. Outcomes

The claims file has 39 claims. The attempt record has 39 outcomes: 20 reproduced, 5 partially reproduced, 3 not reproduced and 11 blocked (9 metadata_insufficient, 1 data_missing, 1 methods_underspecified).

I agree with all 39 outcomes under the criteria in the claims file.

- **fig3-units-per-session (reproduced):** this rests on reading (b), the 57 sessions. Reading (a), the 35 sessions the record itself says the claim refers to, has an SD of 14.4 against a limit of 14.3 (cell 31). That result does not depend on the seed. The criterion allows either reading.
- **ed2-backtracking-counts (not reproduced):** this would still hold under the 47-session variant (cells 104–105). That variant has 8 mice, and 8891 standard and 3207 backtracking trials before the extra filters.

## 2. Statements the printed numbers do not support

**Conclusions and summary in the notebook**

- **Cell 26** (repeated in the record's ephys-unit-counts notes): "only a 20% contamination threshold gives a count inside the tolerance (295)". Cell 23 prints two other variants inside 272.7–333.3:
  - "contamination <= 15% only": 331 multi-units
  - "RPV <= 0.5% only": 309 multi-units
- **Cell 106:** "it shows that the paper's numbers can be reached with its own exclusions".
  - The last step, initiation under 1 s, is the Figure 3 trial selection, as cell 105 says. It is not an exclusion the Methods give for Extended Data Fig. 2.
  - The variant has 8 mice, against the paper's 9.
  - Before that step the counts are 8627 and 3104, both above tolerance.
- **Cell 102** (also in the record): "every mouse's first file already holds only standard sequences". Cell 101 shows "other" trials in the first files of MX170903 (2), MX180803 (1) and MX181002 (1). This is minor.
- **Cell 121:** it treats the Methods' remark that mice "did not have experience with earplugs prior to the earplug session" as support for the earplug session being the earlier one. The remark says nothing about session order. The claim stays blocked either way.
- **Cell 14:** "stimulus and acquisition are empty". Cell 13 prints `stimulus` as holding `presentation` and `templates`. Their contents are not shown.

**Attempt record notes and responses**

- **ed7f notes:** "With trial folds 0.159 against 0.028 to 0.034". Cell 76 gives 0.022 for S1BF, so the range is 0.022 to 0.034.
- **ed2e notes:** "The touch tolerance (0 to 25 ms) changes the mean to 1.846".
  - Cell 108 gives 1.846 at both 0 and 25 ms, so the tolerance has no effect.
  - The variant loop also skips the video-end check and the filter on sessions with backtracking. That different trial set is what moves the mean from 1.854.
- **ephys-unit-counts response:** "The criterion's 15% gives 339 under the first two". The 0.5 ms censored-period estimate gives 341 (cell 23).

**Entry README**

- "It takes about 20 to 25 minutes on four cores". The execution timestamps run from 12:31:15 to 12:37:53, about 7 minutes. No core count is printed. The verification response says "about 21 minutes".
- "93 recording sessions in S1TJ, M1TJ, ALM, S1BF and other areas". The 93 files with units include the 14 opto efficiency recordings (cell 3). They are not recording sessions in the sense of the 57.
- "Optogenetic inhibition and control experiments (nine claims)". The nine include ed1f-lick-force, which is a calibration claim.

Everything else in the conclusions, the summary, the README and the record's notes matches the printed outputs. I checked each number against its cell. The two paper facts the record relies on match the paper text:
- Air flow on first in two mice and off first in four.
- Extended Data Fig. 7b shows 8 mice.

**My round-1 reasons as stated in the record**

They are faithful paraphrases. Two omissions:
- None of the fig3c reasons includes my point that I could not verify the Figure 3b targets, which were read from the figure image. All five fig3c outcomes depend on those values.
- My point that the effect of the missing inter-lick-interval standardisation on ed4m and ed4o was not quantified appears in no reason. I had marked it as not affecting a conclusion.

## 3. Round-1 points

**Resolved**
- Seed sensitivity for ed5e, ed5f and the units SD (cell 64). ed5e stays inside its range under all four seeds, and ed5f stays partial.
- Greedy trial selection (cell 35).
- Single/multi split per session and the alternative contamination estimates (cells 23–25).
- ed2 trial-level filters (cell 105).
- ed6b distribution and the video-based bout threshold (cell 111).
- First learning file contents and early speeds for ed1l-proficiency (cell 101).
- MX181003 handled by a variant (cell 97).
- fig3f: behaviour difference and PCA fitted before cross-validation, now in the conclusion and deviations.
- ed4l: S1BF and the per-second fractions (cell 85).
- ed7f: one value per mouse (cell 76).
- Opto and control metadata, the `opto` column values and the force `conversion` attribute (cell 13).
- Label-free checks for ed1i, ed1j and ed1k (cells 118–120).
- Random folds documented as a deviation.

**Remaining that bears on a conclusion**
1. **fig3c (all five claims):** the expected means and SDs come from the Figure 3b image, and I still cannot verify them.
2. **ephys-unit-counts:** the partial outcome depends on details of the contamination estimate. Dropping either criterion puts the multi-units inside tolerance. Cell 26 and the record need correcting on this point, though the outcome under the fixed criterion stands.
3. **ed1l-proficiency-1500:** it is still unsettled whether the learning files start at the start of training. The paper says training began with the complete task, which fits standard-only first files. But 3 of 15 mice are already fast in their first 100 trials. Reading (a) also saturates within about 200 trials, so the not-reproduced outcome partly reflects how proficiency was defined.
4. **fig3-units-per-session:** the reading the record says the claim refers to fails the SD limit by 0.1. The outcome is reproduced only under the wider reading.
