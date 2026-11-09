The round-2 revision is finished. No outcome changed, and nothing is under `proposed`. The entry re-ran with `python tools/entry.py all entries/001193-zhu-2022`: the checks report 0 errors and the notebook passes in 84 s. The new numbers are the same as before: pooled means 31.568 and 29.955, t(62) = 0.113, p = 0.910, and the keyword counts on the site have not changed.

**Outcomes (unchanged, all agreed by the verifier):** participants is partially reproduced, 23 claims are blocked (data missing), and stimuli-word-frequency is reproduced on an assumption.

**What I added or corrected, point by point:**
- **(a) Basis of the word-frequency assumption.**
  - Cell 20 now prints the t statistic for each sub-corpus: news −0.356, fiction 1.126, pooled 0.113, against the paper's 0.11. It also prints how far apart the four paper/attempt ratios are (1.0001, all near 1.0099).
  - The deviation, the claim's notes and cell 22 now give these two facts as the main reason for the choice; that only this reading meets the tolerances comes after them.
  - The protocol requires a `methods_unavailable` finding for an assumed outcome, and the record had none. I added one asking the paper's authors which sub-corpus and which total they divided by.
- **(b) The claims file's "word frequency list".** I created `questions/001193.yaml` with a question for a reader: the site has no word frequency list, so the claim's criterion names something that does not exist. I did not change the claim, and the notes say the question is open.
- **(c) Cell 10's standard deviation:** it now says within 1e-4 (0.9999 to 0.99999), where it said 3e-5.
- **Cell 10's list of files with a start transient:** it now names all 17 files, the 16 of TC5, TC6, TC7 and TC9 plus TC17_block4.
- **README run time:** it now says about two minutes, where it said about a minute.
- **participants notes:** they now say the criterion's wording for a partial outcome does not literally fit this case, and that partially reproduced is taken as the closest reading.
- **task-structure notes:** they now say the supplement gives 32 sentences per list and 6, 7, 6 and 6 words per sentence, which matches three expected values. The claim stays blocked because the criterion needs trial counts and timings for each participant.
- **Round 2 under `verifications`:** recorded for all 25 claims, with the verifier's reasons taken from the report and my reply under `response`.
- **Fetch date:** the record now gives 2026-11-02 as the date the site's counts were read, since this run fetched them again.

**Not done:**
- I left the unrelated changes to `tools/build_site.py` and `tools/site_assets/progress.js`, which were already in the working tree, untouched.
- Nothing is committed, as instructed.
