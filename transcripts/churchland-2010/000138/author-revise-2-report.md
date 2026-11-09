All 15 outcomes are unchanged and nothing is proposed for a third round. I fixed every point in the round-2 report and re-ran the entry: `python tools/entry.py all` passes with 0 errors, and the last run took 7.6 minutes. Every number in the text now matches the printed outputs. Nothing is committed.

**Outcomes:** The verifier agreed with all 15, and none needed to change. Round 2 is recorded under `verifications` in the attempt record, with the verifier's reasons in its own words and my reply under `response` for each claim.

**fig7c, the upper-limit space (the one assumption I revised):** The verifier said that keeping the unit being fit in its upper-limit space is at least as well supported as leaving it out. I checked the supplement: it builds that space "from the preparatory activity of all neurons" and calls it "a rough upper limit on performance". It states no exclusion for this space, while the Methods do state one for the peri-movement space. With the unit left out, 11 of 40 random halves score above that limit.
- The main reading now keeps the unit in, and every row counts.
- Under the new main reading the anterior array scores 0.963 of the random halves and the posterior array 0.615. Posterior is below the random halves' 5th percentile.
- Anterior now comes out better than posterior, as the paper reports.
- 2 of 16 rows meet the criterion, both with the space recomputed for each left-out condition. The outcome stays not reproduced.
- I updated the notebook's conclusion, the summary, the record's notes and deviation, and the question for the paper's authors.

**Outputs added:**
- **fig7a:** The notebook now prints the peri-movement curve under the per-axis trial selection. It peaks at 0.150 and falls to −3.102 at 14 dimensions, with the shuffled space above it from 9 dimensions up. This replaces the unsupported word "collapses".
- **fig7a, recomputed space:** It also prints the standard error of the shuffled space's best score (0.009). The text now says the 0.001 margin in that variant is within the noise of the draws.
- **Test-file check:** It now covers all 122 units: 0 of 8734 runs of five intervals match the training data. The summary sentence now says exactly that.
- **fig7a and fig7c tables:** fig7c now prints the share of random halves above 1; fig7a prints the standard error above.

**Text corrected:**
- **fig4d:** The Spearman range now reads 0.146, as the output prints.
- **Run time:** The README said about ten minutes; three runs here took 7.3 to 8.7, so it now says about eight minutes, and `entry.yaml` says 8.
- **fig7d:** The notebook and the record no longer claim that overlapping draws raise consistency. They give the overlap and say its effect was not measured.
- **Round-1 record:** The "reviewed" text now says the first cell's outcome table was left in the handover.

**Not done:**
- **Claims file:** The verifier found no misreading of the paper, so I added nothing to `questions/000138.yaml`.
- **Open points:** Two points stay as they were, because the files cannot settle them: which session this is and which id prefix is which array, and how the space is computed for each left-out condition. Both are already in the record and put to the authors.
- **Deleted file:** I deleted a stray `uv.lock` that this session created at the repository root.
