I wrote the reconciliation block in `attempts/watson-2016-03.yaml`, along with eight new findings marked `found: on_prompt` (12 to 19) and the new notebook `entries/watson-2016/earlier_findings.ipynb`, which is listed in `entry.yaml`. Lock and check give 0 errors, and a clean run passes both notebooks (`reproduce_watson_2016.ipynb` 1285 s, `earlier_findings.ipynb` 491 s). The blind attempt's existing findings, outcomes, notes, notebooks and claims file are untouched. Nothing is committed.

**1. Blind: `false`.** The author run and both revise runs saw nothing of `watson-2016-02`. The author-answers run came after the outcomes were recorded. It printed `answer-report.md`, which quotes one line of the earlier record: the `post-sleep-wake-lower` question had been left "with a reader (questions file)". A file search in that run also listed the earlier entry's `entry.yaml` path without opening it. It saw no earlier outcome, value or finding, and changed nothing. I set `false` because gao-2018-02 did the same for a similar case; `blind_note` says all of this.

**2. Earlier findings.** None of them is fixed. CRCNS:fcx-1 is unversioned, and every value checked is unchanged.

| Earlier | Problem | Status | Now |
|---|---|---|---|
| 1 | 51 cycles in the files, the paper says 54 | still_present (checked) | 12 |
| 2 | 434 MAs against the paper's 790; short WakeInterruptions; a 14 s packet | still_present | 7 (the unreported parts were checked and added as 13) |
| 3 | Overlapping cycles in Rizzo_022715 and Splinter_020515 | still_present (checked) | 14 |
| 4 | Dino days deposited as two sessions | still_present | 6 (the two Dino_062014 scorings still differ, said in the note) |
| 5 | Motion said to be z-scored but is not; NaN values | still_present (checked) | 15 |
| 6 | RecordingFileIntervals ends at inf; UP/DOWN file name | still_present (checked) | 16 |
| 7 | Spindle incidence, Results against Table S1 | still_present | 8 |
| 8 | No scored WAKE after most SLEEPs (23 of 51 cycles) | still_present (checked) | 17 |
| 9 | Tar member order; full streaming needed | still_present (checked) | 18 |
| 10 | Questions for the paper's authors | still_present | 11 (questions 2 to 6 added as 19) |

**3. New findings in `watson-2016-03`:** 1, 2, 3, 4, 5, 9 and 10.

**4. Outcomes that changed.** 13 of the 37 shared claims differ. Most of the changes come from the rewritten claims file: `claims/watson-2016.yaml` with 53 claims replaced the per-dataset file with 41.
- **Claims file:**
  - `table1-dataset-counts` (partial to reproduced): the 54 cycles moved to another claim.
  - `ma-statistics` (partial to not): the trends were split off and a new partial rule needs three of the four values.
  - `fig1e-up-state-dynamics` (not to partial): the last bin is now compared with the first bin, not the first two.
  - `post-sleep-wake-lower`, `figs3a-first-last-rem-ma-slopes` and `fig3e-wake-before-after-sextiles` (partial to reproduced): a new reading takes the WAKE after SLEEP as the arousal that ends SLEEP.
  - `cv-decreases-over-sleep` (not to reproduced): one point per packet is now a reading.
  - `fig4-spindles-within-nrem` (reproduced to partial): the two absences are now required.
  - `sleep-homogenizes-rates` (partial to reproduced): it follows the claims it depends on.
- **Method:**
  - `fig4cd-packet-rate-lfp-correlations` (partial to not): band-power windows of 10 s against 2 s, so gamma misses its bound.
  - `figs5d-rem-nrem-rem` (partial to not): a different rule for forming triplets.
- **Both:**
  - `fig3c-spindles-over-sleep` (partial to not): the 10 s-bin trend differs between the notebooks, and the new partial rule needs the decrease.
  - `fig5b-wake-between-packets` (partial to reproduced): the movement part was dropped, and pairing packets across cycles gives 24 triplets.

**5. Protocol, what did not fit:**
- `docs/pilot-notes.md` has a section for pilot-14 but none for pilot-15. Under `protocol` I described pilot-14 (records filed by paper), which is why the blind attempt used both datasets and the new claims file. For pilot-15 I used the one rule `tools/entry.py` names: findings must say whether they are about the data or the paper, and name their datasets.
- The steps assume an earlier finding is either reported again or checked in the notebook. Findings 2, 4 and 10 were only partly reported again. I pointed `now` at the matching blind finding and added the unreported parts as separate on-prompt findings (13 and 19), except the Dino_062014 scoring detail, which stays in the note.
- The questions in finding 10 are about the paper, not the data, and the paper text is not committed, so the CI notebook cannot check them. My evidence for them is the claims file, which still lists each as open.
- Untracked files at the repository root (`.bashrc`, `.gitconfig`, `scripts` and others) are sandbox device placeholders dated 11:14, before this run. They are not mine and I left them alone; whoever commits should leave them out.
