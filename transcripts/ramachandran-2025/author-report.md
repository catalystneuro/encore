I've finished steps 1 to 6 for DANDI:000945. Of the 22 claims, 2 were reproduced, 2 partially reproduced, 15 not reproduced and 3 blocked. The entry passes `check` and its notebook runs clean in 60 s; the handover package is built. Nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig3-cell-type-sorting | partially reproduced: two recordings match 28 FSU / 32 RSU / 60 units using the dataset's own labels; the k-means sorting can't be checked (no waveforms) |
| fig4-rsu-time-locked-both-states | blocked, data_missing (no sham) |
| fig4hi-fsu-delayed-latency | not reproduced (p = 0.018 to 0.85; anesthetized mean 0.38 to 0.52 s against 0.24 ± 0.08) |
| fig4h-awake-latency-wider | not reproduced (awake spread is wider in only 10 of 16 readings, by at most 0.02 s) |
| fig5a-rsu-time-locked-prf-awake | not reproduced (peak at 3000 Hz, not 1500 Hz) |
| fig5c-rsu-time-locked-prf-anesth | not reproduced |
| rsu-time-locked-anesthesia-factor | not reproduced (p ≈ 0.011 to 0.018, and anesthesia raises the response) |
| fig5bd-fsu-time-locked-no-prf | not reproduced (FSU do differ across PRF) |
| fig5e, fig5f, fig5gh | not reproduced |
| delayed-anesthesia-factor | reproduced, resting on assumption Rep2 |
| fig6ad-time-adjacent-batch | blocked, data_missing (second batch of rats absent) |
| fig6ef-rsu-ispta-rise-then-fall | partially reproduced, resting on assumption W2 |
| fig6fh, fig5a-1500-highest | not reproduced |
| fig7a, fig7a-60-highest, fig7b | not reproduced (6% and 60% duty cycle give strong time-locked responses, ~150 to 200%, in FSU too) |
| fig7c-rsu-delayed-dc | not reproduced, resting on assumption C1 |
| fig7d-fsu-delayed-dc | reproduced |
| sham-no-auditory-response | blocked, methods_underspecified (as the claims file says), and there is no sham data |

### 2. The dataset, assumptions and questions

**Version.** I pinned 0.250213.2212, the version the paper cites. All five published versions hold the same 75 files.

**What it holds.**
- **Contents.** Spike times, plus a cell-type label in 60 of 75 files. No waveforms or voltage traces, no sham, and none of the second batch of 5 rats.
- **Coverage.** Awake PRF series for 7 rats. Labelled anesthetized recordings for only 2 rats (BH512 has no 30 Hz). Duty-cycle recordings at 6% and 60% for 3 rats, with no 30% recording of their own.
- **Clock.** Trial `start_time` is the ultrasound trigger. Ten recordings show a stimulus-locked response and none does at shifted times; the other 54 can't tell.

**Problems found.**
- **Duplicates.** 12 files are second copies of other recordings:
  - the BH497 and BH514 folders are copies of the BH498 and BH512 anesthetized recordings, the only copies with labels;
  - `BH512_1500_200_anes2` is a third, re-sorted copy;
  - one 30 Hz recording is filed under both BH498 and BH508.
- **Undocumented metadata.** The condition is coded only in the file identifier. The `_2` suffix on 10 repeat recordings and the 2.2 s `stop_time` are not explained.
- **Missing labels.** 15 anesthetized files have no cell-type labels.
- **Metadata errors.** Every file says age P24W (the paper gives 7 to 10 months), the labelled anesthetized copies are described as awake, and electrode fields hold placeholders.
- **Short recordings.** Five recordings hold 203 to 339 trials instead of 500.

**Assumptions (each also recorded as a question for the paper's authors):**
- **Rep2:** the `_2` repeat recordings were left out, since Methods 2.3 describes one recording per condition per rat. This decides the FSU part of delayed-anesthesia-factor (p = 0.0013 without the repeats, 0.038 with them).
- **C1:** the 30% duty-cycle group is the 1500 Hz, 200 µs recordings of the same rats as the 6% and 60% recordings. This decides fig7c (not reproduced under C1, partially under all rats).
- **W2:** a window that doesn't fall on bin edges is measured from the overlapping PSTH bins, since Methods 2.4 builds responses from the binned PSTH. This decides fig6ef.

**Questions to a reader:** none.

### 3. Where the protocol was unclear
1. **A criterion part that can't be tested.** fig3's criterion has no branch for "counts match but the feature part can't be tested". Blocking it would, by the dependency rule, block every claim that uses cell types, although they only need the labels. I recorded it as partially reproduced and explained why.
2. **The sham rule only covers half the case.** The claims file's header says what to do when an anesthetized sham is missing, but not the awake sham. I applied the same rule (judge on the remaining parts) and recorded it as a deviation.
3. **Readings that come from the dataset, not the claims file.** The `_2` repeats and the missing 30% recordings forced choices (Rep1/Rep2, C1/C2) that step 1.6 covers only for gaps in the paper. I ran every reading and adopted one as an assumption.
4. **"Every reading" against "adopt the best reading".** fig4h's criterion requires the result under every reading, while step 1.6 says to adopt the best-supported reading when readings disagree. I followed the criterion.
5. **The "fewer than 500 trials" rule.** The protocol says nothing about recordings that hold fewer trials than the paper describes. I used them as they are and recorded a finding.

### 4. Runtime and failures
The run took about 23 minutes (21:25 to 21:48 UTC), and the notebook runs in 60 s. Nothing failed.

Files are in `entries/000945-ramachandran-2025/`:
- `reproduce_ramachandran_2025.ipynb`
- `tfus.py`
- `README.md`

The attempt record is `attempts/000945-ramachandran-2025-01.yaml`.
