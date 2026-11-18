I've written the `reconciliation` block into `attempts/fujisawa-2008-03.yaml` and added `entries/fujisawa-2008/earlier_findings.ipynb`. The block lists it in `entry.yaml` and the README. After locking, `python tools/entry.py all entries/fujisawa-2008` reports 0 errors and both notebooks pass: the main one in 2117 s (it re-ran because the entry changed), the new one in 108 s. Every number I cite appears in the executed copies. I committed nothing.

**1. Blind.** Yes, `blind: true`. The audit points at two places, and neither shows an earlier attempt's results:
- `author-answers.md` lines 106 to 107 are the file names `summaries/fujisawa-2008-01.md` and `-02.md`, printed by a `find`. Their contents were never read.
- `author.md` line 4237 is the record this attempt wrote.

The author-answers run also relayed a note from the answer run: an older questions file holds two unanswered questions, on `odor-unrelated-to-stem` and `speed-not-correlated`. It saw only the claim ids, after the outcomes were recorded, and changed nothing.

**2. Earlier findings (fujisawa-2008-02)**

| Earlier | Status | Now | How it was decided |
|---|---|---|---|
| 1 three rats, correct trials only, no layer 5 session | still_present | 10 | same problem (correct trials only is finding 9) |
| 2 EE188_example.mat only inside EE.188.tar.gz | still_present | 18 (on_prompt) | checked: member 62 of 75, 1.99 GB into 2.41 GB |
| 3 two cell-type classifications | still_present | 7 | same values (87/18 against 33/15/69) |
| 4 CellsInfo selection undocumented | still_present | 13 | same problem |
| 5 probe layer not given | still_present | 10 | same problem |
| 6 spike labels start at first nose-poke | still_present | 19 (on_prompt) | checked: 269071 of 676892 labelled spikes in the poke, all 13 sessions |
| 7 pairs_all, 43 connections, selection unstated | still_present | 20 (on_prompt) | checked: 43 pairs, largest component 39 |
| 8 second LED untracked in 10 of 13 sessions | still_present | 11 | same problem |
| 9 jitter band, bin width, pairs_all choice (question to the authors) | still_present | 21 (on_prompt) | the paper is unchanged and no answer is recorded |
| 10 Supp. Fig. 2A normalisation | still_present | 14 | same question |
| 11 EE188 table leaves out 3 correct trials and 1 error trial | still_present | 22 (on_prompt) | checked: the same four trials are missing |
| 12 no Cells variable in the files | still_present | 13 | same problem |

None is fixed. The CRCNS files and their description (version 0.7) look unchanged.

**3. New findings in fujisawa-2008-03:** 1, 2, 3, 4, 5, 6, 8, 15, 16 and 17.

**4. Outcomes that changed** (7 of the 19 claim ids both attempts tested)
- **`task-performance`** (partially reproduced, now blocked): a difference in method. The earlier attempt read EE188's error trials from the nose-poke sensor channels; this one kept to the trial tables.
- **`side-arm-selectivity-by-layer`, `central-arm-selectivity`** (both not reproduced, now partial): a change in the claims file. The merged file adds a partial outcome; the numbers barely moved.
- **`pyr-pyr-connections`** (not reproduced, now partial): mainly the claims file's new partial outcome. The two attempts also used different global bands for the jitter test.
- **`fig4-pair-156-136`** (partial, now not reproduced): the numbers are nearly the same. The two authors graded the same result differently.
- **`thinning-preserves-dependence`** (not reproduced, now reproduced): a difference in method. The earlier attempt counted a thinning only when it reached the flatness target.
- **`population-vector-width`** (reproduced, now partial): a difference in how the firing-rate curves were built. EE188 gives 0.239 there and 0.268 to 0.314 here, against a limit of 0.267.

**5. What did not fit the protocol**
- `docs/pilot-notes.md` has no section for pilot-15. I described pilot-14, where records are filed by paper and use both datasets with a merged claims file. For pilot-15 I used the one rule `tools/entry.py` names as pilot-15's: findings must say what they are about and which datasets.
- Earlier finding 9 is a question about the paper, so no dataset version can settle it. I marked it still present because the paper is unchanged and the new attempt took one answer to the question without raising it.
- Earlier finding 1 covers two problems that the new attempt reports separately (findings 9 and 10), but `now` takes a single number. I pointed it at 10 and named 9 in the note.
- Earlier finding 6 overlaps new finding 12: same problem, but 12 is about the position file, not the spikes' own labels. Since the rule asks for the same fields, I added it as finding 19 and explained the link in the note.
- For finding 18 I used `metadata_insufficient`, not the earlier `metadata_error`. The description also says each session's tar holds all of that session's files, so the problem is a missing location more than a wrong one.
- The `fig4-pair-156-136` change fits none of the four reasons the task lists (dataset, protocol, claims file, method). I described it as a difference in grading.
