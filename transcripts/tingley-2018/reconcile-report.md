I've reconciled `tingley-2018-02` with `tingley-2018-01` and written the `reconciliation` block. The new notebook `entries/tingley-2018/earlier_findings.ipynb` is in `entry.yaml`. The lock came out unchanged, both notebooks pass `run` (the main one in 3048 s, the new one in 111 s), and the executed copy prints the same numbers as my trial run. `python tools/entry.py check entries/tingley-2018` still reports one error, which predates my changes and is described in section 5. Nothing is committed.

**1. Blind: yes.** The audit printed three lines, and none of them is an earlier result. Two are the README's dashboard URL, which the author read while reading the repository README. The third is the author's own run URL. The author's listing of `entries/tingley-2018` failed with "No such file or directory", and no transcript reads an earlier record, transcript or the website.

**2. Earlier findings**

| # | Earlier finding | Status | `now` |
|---|---|---|---|
| 1 | Processed behaviour missing | partly_fixed | 3 |
| 2 | Units have no site or largest-waveform channel | partly_fixed | 6 |
| 3 | Session-name depths undescribed; `hpc` not defined | partly_fixed | 14 |
| 4 | Eight DT8 files in metres labelled mm | partly_fixed | 1 |
| 5 | z is a copy of y | fixed | |
| 6 | DT2 position timestamps repeat | fixed | |
| 7 | Spike times out of order | fixed | |
| 8 | DT2 labels and scale; DT7 units | partly_fixed | 2 |
| 9 | Trials without type or direction | partly_fixed | 6 |
| 10 | Trials do not match positions (DT9 20170501, DT2 20160221) | still_present | 15 (on_prompt) |
| 11 | Unit counts against the paper | still_present | 5 |
| 12 | Paper's code not public | still_present | 16 (on_prompt) |
| 13 | Quaternion stated in meters | fixed | |
| 14 | One hippocampal label per session | partly_fixed | 5 |
| 15 | Place-field threshold 1% in the code, 20% in the Methods | still_present | 17 (on_prompt) |
| 16 | LFP chunked across all channels | fixed | |

Three statuses need explaining:
- **4:** The eight files are now right, but 31 files that hold millimetres are now labelled meters. That is the same field as the new finding 1, so I marked it partly fixed and explained this in the note.
- **10:** In DT2 20160221 the speed check no longer shows the offset. A new check against the dataset's own linearization still finds the best match 0.75 s after the trial times.
- **12:** Only `bz_phaseMap2Bins` is still missing from the public repositories. buzcode at e615663 does hold `bz_olypherInfo.m` and `bz_peerPrediction.m`, so that part of the earlier statement was not right.

**3. New findings:** 4, 7, 8, 9, 10, 11, 12 and 13. Findings 15, 16 and 17 are the ones I added, marked `found: on_prompt`.

**4. Outcomes that changed** (11 claims, each with a note in the record):
- **hpc-unit-count** (partially reproduced → not reproduced): the claims file dropped the partial rule based on the sum of the two counts.
- **fig2e-ls-phase-lower-mse** and **fig2fg-mse-difference** (reproduced and partially reproduced → not reproduced): a difference in method. The new notebook sets the phase of bins with no spike to 0; under its leave-out variant the LS results look like the earlier ones.
- **ls-place-fields-unstable** (not reproduced → partially reproduced): the new notebook builds rate maps on the lab's linearization, which this version adds. The hippocampal median falls from 83.6% to 71.7%.
- **fig1g-phase-more-info-fine-scale** (partially reproduced → reproduced): the claims file added a KS-test reading, and the phase-0 fill drives the match.
- **fig4d-depth-gradient** (partially reproduced → reproduced): a looser criterion, plus unit sites that are new in this version. It holds under one decoder reading only.
- **fig6c-ca3-coherence-increases** and **fig6d-cfc-stronger-ca3** (not reproduced → reproduced): this version now flags each session's CA1 and CA3 channels, and the claims file now follows the paper's figure script (`makeFig6.m`).
- **fig5g-assembly-neurons-stronger-phase** and **fig6e-assembly-position** (blocked → tested): the earlier attempt blocked them for time; the new one tested them on a sample of pairs.
- **speed-independent** (blocked → partially reproduced): a reader-written claims file now names readings, and the protocol requires running them before blocking.

**5. What did not fit the protocol**
- **The earlier entry could not be found the way the prompt says.** The clone is shallow, so `git log -1 -- attempts/tingley-2018-01.yaml` returns the current commit, which holds the new entry. I read the earlier entry from `main` instead (`lshpc.py`, version 0.250624.0438), where `attempts/tingley-2018-01.yaml` is identical.
- **The check error.** It comes from `tingley-2018-01.yaml` naming the cell tag `claim:ls-information-lower`, which the new notebook does not have because the claim was renamed `ls-lower-peak-info`. I must not change that record. The uncommitted edit to `tools/entry.py` that was already in the checkout covers renamed claims but not this cell-tag case, so the workflow or that tool will need a fix.
- **No notes for pilot-11 or pilot-15.** `docs/pilot-notes.md` has no section for either, so the `protocol` text covers pilot-8, 9, 10, 12, 13 and 14 and says that the two are missing.
- **"Tested by both".** I read this as any claim with the same id in both records, so the three that were blocked earlier are listed under `outcomes`. The schema allows `earlier: blocked`.
- **Finding 15 (place-field threshold) is about code at fixed commits.** Nothing about the dataset version could change it.
