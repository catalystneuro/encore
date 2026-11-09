I've worked through all nine points of the round-1 report, re-run the entry twice (it passes both times, about 17.5 minutes) and recorded the round under `verifications`. Nothing is committed.

**Outcome changes** (all three now match the verifier's outcome):
- **collection-window**: not_reproduced → partially_reproduced. The start date and the 26 days hold, and 99.7% of rows fall inside the window. But 432 rows are dated after election day, so "every timestamp inside" fails.
- **age-education-inconsistencies**: not_reproduced → partially_reproduced. The 18–20 count (378) is within tolerance; the under-18 count (27) is not.
- **efa-loadings-consistent**: reproduced → partially_reproduced, still marked as resting on the claims file's thresholds. The two solutions agree on the Pearson matrix (35 of 39 statements) but not on the polychoric one (32 of 39).

All other outcomes are unchanged.

**What I added or corrected:**
- **Figure readings (problem 1):** a separate agent re-read Figs. 2, 3 and 7 from the publisher's images. It saw only the images, not the computed scores, and measured each logo's position in pixels against the axes. Its values and the axis positions now replace the earlier readings. It found that Fig. 2 places parties at whole percentages, which explains the tight matches. It read PS at 54.5 on Fig. 3's economic axis, so the PS mismatch (computed 47.7) stands. Fig. 7's tree and heights also stand (within 1).
- **R code (problem 2):** a new data-check section prints the R code lines the analysis relies on. The age and education validation rules only check that each value is a valid category; no rule relates the two.
- **Polychoric parallel analysis (problem 3):** I added psych's resampled-data reference for polychoric correlations. It still gives 11 factors for both row readings (12th value 0.0103 against 0.0143, s.d. 0.0009). The conclusion now says that with psych's defaults the claim holds under reading (a) only.
- **Non-converged fits (problem 4):** all 18 are on simulated reference matrices. Every fit on an observed or resampled matrix converged.
- **Problems 5, 7 and 9:**
  - The order comparison now counts a pair only when the figure and the scores order it opposite ways by more than 1 point (problem 5).
  - The MD5 of every streamed file is checked against the archive's list, and all 8 match (problem 7).
  - The collection-window notes now say the R code treats the timestamps as local time, which makes the UTC reading unlikely (problem 9).
- **Claims file (problem 8):** I added a question for a reader in `questions/figshare-24949470.yaml`: do the 40 and 400 describe the deposited data or an earlier state of it? The claim itself is unchanged.
- I updated the README, the notebook summary, the PS finding and `runtime_minutes` (now 20).

**What I did not do:**
- **Overlays on the published figures:** the verifier asked for the figures with the values drawn on them. `tools/entry.py check` rejects any code that reads an image file, so the notebook gives the blind readings with their pixel positions instead.
- **Blocked reasons:** I kept selected-parties-top-vote and website-views blocked as `other`, not the verifier's `data_missing`. The check does not allow `data_missing` on claims whose data is held elsewhere.
- **Election results:** the verifier said selected-parties-top-vote could be tested against the official results. Outside data must have a DOI or be in a repository at a commit, and the Statistical Office's site has neither. A new search found no such copy on Harvard Dataverse (ParlGov 2024 is the latest release and stops at 2020) or Zenodo. This search is not in the notebook.
