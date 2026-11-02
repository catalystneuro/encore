**Round 2 verification: Zhu et al. (2022) on DANDI:001193 0.240921.1006**

**1. Outcomes**

The claims file has 25 claims and the attempt record has 25 outcomes: 1 partially_reproduced, 23 blocked (data_missing) and 1 reproduced (`assumed: true`).

- **participants: partially_reproduced. I agree.**
  - Cell 16 shows 10 subjects, each with 256 electrodes in two groups of 128.
  - Sex is `U` for 10 of 10 subjects, so the male and female counts cannot be determined. No file has task labels, so the COM and NL counts cannot be determined either.
  - One point the record does not state: the criterion defines a partial outcome as "a subset of the participants with matching metadata". Here all participants are present but most of the metadata is missing, so the criterion does not literally describe this case. Partially_reproduced is still the natural reading. It does not change the outcome.
- **The 23 data_missing claims: blocked. I agree with all of them.**
  - Cell 6 prints one listing shared by all 40 files. It has the ECoG ElectricalSeries, devices, electrode groups, electrode table and subject/session text, and nothing else in `acquisition` or `general`.
  - `stimulus`, `analysis` and `processing` are empty, there is no trials table, and every `location` is `unknown`.
  - Cell 7 shows exactly 242,424 bytes beyond the data in all 40 files.
  - For task-structure: cell 19 now reads 32 sentences per list and 6/7/6/6 words (CORR/SYN-P/SYN-C/SEM) from the supplement, which matches three expected values. The criterion's partial outcome still needs trial counts and timings per participant, so blocked stands. The record's notes could mention this.
- **stimuli-word-frequency: reproduced, assumed. I agree, and the assumption is stated (deviations 1–2) and reasonable.**
  - I re-read four of the keywords' counts from the site (电脑 857/361, 甘香 0/1, 重要 9778/1910, 意见 2801/1386); all match cell 19.
  - From the counts printed in cell 19, I recomputed the pooled result: 31.568 (s.d. 34.80) against 29.955 (s.d. 72.86), t = 0.113.
  - The site's home page does list only character and bigram frequency lists, as the notebook says.
  - The stated basis leans on "only this one meets the criterion", which picks the reading by its outcome. It leaves out the strongest independent evidence. The t statistic does not depend on the divisor, so it identifies the sub-corpus: pooled gives t = 0.113 against the paper's 0.11, news alone gives −0.356 and fiction alone 1.126. In addition, all four statistics share one ratio (1.0099), as the same counts over a slightly different divisor would. The record should state this; it would not change the outcome.
- **A claims-file misreading (reported, not corrected).** The criterion of stimuli-word-frequency names "the Modern Chinese word frequency list". The paper (txt, lines 753–756) gives only the URL, and the site has no word list. The notebook handles this correctly by using bigram counts.

**2. Sentences against the printed outputs**

- **Cell 10:** "standard deviation 1 to within 3e-5". This is not supported. Cell 9 prints a minimum channel s.d. of 0.9999 in several files ("0.9999 to 0.99999"), which is about 1e-4 from 1. The record's metadata_error finding ("within 1e-4") is correct.
- **Cell 10:** "Some files (counted above; all those of TC5, TC6, TC7 and TC9)". Cell 9 counts 17 files, and its subject list includes TC17 (TC17_block4, first-sample median 3.14). The four subjects named account for only 16 of the 17.
- **README:** "It takes about a minute". Cell 1 prints 76 s just to read the 40 files, before any of the web fetches. This is minor.
- Every other sentence I checked is supported by the printed numbers: cells 17, 22 and 23, the README, the record's notes, deviations and findings. That includes the p ranges 0.264–0.910 and 0.139–0.964, the ratio 1.010 and about 28.0 M bigrams, 47.35 with the SYN-P keywords, 282–381 s, 34/40 against 19/40, and 40 of 40 blocks too short at 400 Hz.
- **My round-1 reasons are stated faithfully in my own words.** The participants and stimuli-word-frequency reasons are close to verbatim. Each blocked reason carries my archive-check summary. The one thing dropped is my caveat on the byte balance, that I had assumed the smallest and largest files were the ones with the fewest and most samples. Cell 7 now makes that caveat moot.

**3. Round-1 points**

All are resolved:
- **Problem 1:** resolved. The claim is now tested, and I verified the result.
- **Problem 2 and the first "could not check":** resolved by the full listing in cell 6.
- **The second "could not check":** resolved by the size table in cell 7, which covers all 40 files.
- **Problem 3:** resolved. Cell 16 now reports the male and female counts as "not determinable".
- **Problem 4:** needed no change.
- **Problem 5:** resolved. Cell 12 now says an analysis would take the files at 100 Hz.
- **Problem 6:** needed no action.
- **The third "could not check":** resolved. The word-frequency output is now printed, and I checked it.
- **The fourth "could not check":** resolved. Cell 17 and the record now say the 5/5 split by recording period is not evidence of the task groups.

Nothing that remains changes an outcome. Still open:
- (a) The stimuli-word-frequency assumption should cite the t match and the common ratio, not only that it is the one reading that passes.
- (b) The claims file's "word frequency list" misreading, reported above.
- (c) Cell 10's "3e-5", which should be about 1e-4.
