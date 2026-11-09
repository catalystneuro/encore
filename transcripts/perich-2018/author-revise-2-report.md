I made the round-2 revision and re-ran the entry twice. Both runs passed the checks with 0 errors, and every printed number came out the same as before. Nothing is committed.

**Outcomes.** No verified outcome changed. I propose one change, written under `proposed` on fig3b-pmd-higher-dimensional for round 3: reproduced to partially_reproduced.
- The verifier found that the record used the 100 ms full-width kernel reading for fig3b and the 100 ms standard-deviation reading for fig6c. No single reading gives both verified outcomes.
- I adopted the standard deviation for every claim. It is the usual way a Gaussian kernel's width is stated, and the same group's 2020 paper on Monkey C recordings (in `paper/`) gives its kernel as "s.d.: 50 ms".
- Under that reading the fig3b medians are 7 (M1) and 10 (PMd), outside tolerance over 21 sessions and in all 2002 sets of 16 sessions. PMd is still above M1 in every session, which the criterion counts as partial.
- Under the same reading, fig6c stays partially reproduced, all four figs4c readings meet the criterion, and figs4d still holds.

**Added or corrected**
- **New notebook section, "One kernel reading for every claim".** It prints the numbers each criterion is judged on under each kernel reading, and says why the standard deviation was adopted.
- **Which rule governs the kernel reading.** The claims file's header says a claim whose readings disagree is blocked. I followed the protocol's later rule instead (author step 1.6: adopt the best-supported reading as an assumption), and recorded the conflict in the fig3b and fig6c deviations.
- **fig3b record.** It now says the outcome rests on all 21 sessions (910 of 2002 sixteen-session sets fit). It also says the synthetic check does not choose between noise scales.
- **figs4c record.** It now says its one failing reading uses the full-width kernel.
- **Text the outputs did not support, now corrected:**
  - Cell 0: one Monkey C session has too few PMd units.
  - Cell 4: there are 13 later Monkey M sessions, not four, and why they are left out.
  - Cell 8: the error comparison now names M 2014-03-03, 2014-02-03, 2014-02-18 and C 2016-09-19, and the decreasing trend in C 2016-10-11.
  - figs4d: only PMd shows a fall at small sizes; M1 does not fall consistently.
  - The cursor-in-target finding: M 2014-02-03 and 2014-02-18 are 1%, not never.
  - The misquoted round-1 figs4d reason.
- The summary, README, the kernel question to the authors, and the helper docstring now match.
- Round 2 is recorded under `verifications`, 28 claims, all agreeing, with the verifier's reasons and my responses.

**Not done**
- I added nothing to `questions/000688.yaml`. The verifier called the kernel issue an inconsistency inside the claims file, not a misreading of the paper.
- Whether the deposited units are the paper's spike sort is still open. The files cannot show it, so it stays under the existing finding.
- I kept the session-selection rule as it was and only described it accurately: the February to March Monkey M block is taken as a whole, and two Monkey C sessions outside the reward range are kept, as the second session set shows.
