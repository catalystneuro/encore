I revised the attempt after round 1. One outcome changed: stimuli-word-frequency went from blocked (other) to **reproduced**, resting on an assumption about which corpus counts the paper used. I re-ran `python tools/entry.py all entries/001193-zhu-2022`: the check gives 0 errors and the notebook passes in 67 s. The conclusions match the new numbers. Nothing is committed.

**The outcome that changed: stimuli-word-frequency.** The verifier was right that "unpinned" is not a reason to block, so I tested the claim. The new helper `keyword_frequency.py` does three things:
- It fetches the supplement from the publisher and checks it by SHA-256 against the copy in `paper/`, then takes word 4 of the CORR and SYN-C sentence lists.
- It reads each keyword's raw count from the bigram search of the site the paper names (lingua.mtsu.edu/chinese-computing).
- It turns counts into frequencies per million using the sub-corpus sizes in Table 6 of the site's 2004 technical report.

The site has no word frequency list as such. It only has two-character (bigram) counts for two sub-corpora, news and fiction, and the paper does not say which one it used or what it divided by. I ran all six combinations:

| Reading | CORR mean (31.88 ± 3.19) | SYN-C mean (30.25 ± 3.03) | t(62), p |
|---|---|---|---|
| News + fiction pooled, per million bigrams | 31.57 | 29.95 | 0.11, 0.910 |
| The other five combinations | at least one mean outside its band | | p > 0.05 in all |

- Only the pooled reading meets the criterion, so I adopted it as the assumption (`assumed: true`). The paper's figures are t(62) = 0.11, P = 0.91.
- The paper's means and standard deviations are each 1.010 times the pooled values, as if the paper divided the same counts by about 28.0 million where the corpus holds 28.3 million bigrams.
- Variants are printed: each keyword counted once, the one keyword with no news count dropped, and Welch's t-test. All stay within tolerance on the pooled reading.
- The site has no version, DOI or commit. That is recorded as a deviation and under `inputs`, and the notebook prints every count it read.

**Other additions and corrections:**
- **New paper finding (`paper_inconsistency`):** the Methods say SYN-P and SEM use the same keywords as CORR, but in sentences 3 and 11 they differ (孩子/衣服 against 小孩/上衣). With the SYN-P keywords the pooled CORR mean becomes 47.35, so the paper's values come from the CORR list.
- **File contents (problem 2, and the first point it could not check):** the data check now lists every object at the top level and under `acquisition` and `general`. All 40 files share one listing: the ECoG series, devices, electrode groups, electrode table, and subject and session text. There are no event or annotation objects.
- **File sizes (the second point it could not check):** a table of path, sample count and file size for all 40 files shows each holds exactly 242,424 bytes beyond its uncompressed ECoG data.
- **Sex counts (problem 3):** male and female counts are now reported as "not determinable (sex U for 10 of 10)" instead of "found 0".
- **Recording dates:** the participants conclusion now says the 5/5 split by recording period is not evidence of which participants did COM and which did NL.
- **Sampling rate (problem 5):** the notebook now says an analysis would take the files at 100 Hz, and that no claim here uses time.
- `pypdf` is added to the requirements and the lock is updated. The header, summary, README and `entry.yaml` are updated.
- Round 1 is recorded under `verifications`. All 24 dataset outcomes are marked agreed. Stimuli-word-frequency is marked `agrees: false`, since the verifier rejected the reason for blocking it.

**Not done:**
- I added no question to `questions/001193.yaml`, because the verifier reported no place where the claims file misreads the paper. The claim's mention of a "Modern Chinese word frequency list" that the site does not have is explained in the notebook and the record, without changing the claim.
- I left alone the existing uncommitted changes in `tools/build_site.py` and `tools/site_assets/progress.js`; they are not part of this attempt.
