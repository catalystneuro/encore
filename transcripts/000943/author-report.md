I've finished steps 1 to 6 for DANDI:000943. All 31 claims are blocked, because the dataset holds no sorted spikes and every claim needs them. `python tools/entry.py check` and `all` pass (0 errors; the notebook ran clean in 203 s, 456 s on the first run). The handover is in `executed/000943-clark-2024/handover/`. Nothing is committed.

## 1. Outcome per claim

| Claim | Outcome |
|---|---|
| All 31 claims (grid-cell-count, supp1-recording-summary, grid-field-size-spacing, the 6 fig2, 8 fig3, 3 fig4 and 11 fig6 claims) | blocked, `too_large` |

- **Why:** every claim rests on single units. No file in the dataset has spike-sorted units, a units table, a trials table or any processed data. The paper sorted its units from the raw signal with MountainSort.
- **Size:** I measured streaming at 71 MB/s (16 processes). At that rate, just reading the 638 GB of raw signal for the paper's recording days takes about 2.5 h, and all 976 GB takes 3.8 h. The notebook limit is 1 h, and sorting time would come on top, so I did not start the sort.
- **Behaviour without units:** for supp1-recording-summary I compared the counts that need no units in the data check, not as a test of the claim. The dataset has 242 usable 200 cm sessions for the nine mice against the paper's 215, which is outside the tolerance. Five of the nine mice are within 10% of the paper's table. The mean trials per session is 183.9 against 179.1.

## 2. The dataset, assumptions and questions

- **Version:** 0.240614.0754, the only published version. The paper cites none, and the draft has the same 734 files and 976 GB.
- **What it holds:** 12 mice, 379 open arena and 355 virtual track files. Each file has the raw 16-channel signal at 30 kHz and a position series, nothing else.
- **Findings recorded in the attempt:**
  - No units or processed data in any file (`data_missing`). The paper's sorted units are at Edinburgh DataShare (doi:10.7488/ds/7684), but in one 26.5 GB pickle that can't be read in part, so I did not use it.
  - The position description is the same in every file and fits neither the 3 virtual track columns nor the 9 open arena columns.
  - The 9 open arena columns are not named.
  - The files describe a 100 x 100 cm arena, but 38 open arena sessions of mice M1 and M2 span only 68 to 90 cm.
  - Two virtual track files have position for only part of the recording.
  - Open arena position runs past the end of the raw signal by a median 2.9 s, and by more than 10 s in 20 files.
  - Nothing marks which sessions the paper used; four mice have more sessions than the paper's table.
- **Duplicates:** no recording is deposited twice.
- **Shared clock:** I checked it by comparing multi-unit activity with running speed in 9 sessions. Seven are consistent with one clock to within about 0.5 s. In two (M3 and M12, virtual track) the check could not tell.
- **Assumptions and questions:** none for the paper's authors, since no claim's method was run. I asked no reader questions.

## 3. Where the protocol was unclear or missing something

1. **Raw data present but derived data missing.** The protocol has no blocking reason for "the raw data are here, but the derived data every claim needs are only elsewhere and not readable." `data_missing` doesn't fit (the units are public) and neither does `elsewhere` (the dataset does hold the raw data). I used `too_large` with the measured estimate, and recorded the missing units as a `data_missing` finding.
2. **The rule for blocked dependent claims hides partial results.** supp1-recording-summary depends on grid-cell-count, so it is blocked, although its session and trial counts can be checked. I kept it blocked and put those numbers in its notes.
3. **No step for when the paper's processed data are outside the archive.** The protocol says outside data may supply "only what the dataset lacks, such as a label". It does not say what to do when what is lacking is the units themselves, deposited as derived tables in another archive. I did not use the DataShare files and explained why in the notebook summary.
4. **The clock check assumes spikes or a trials table.** This dataset has neither, so I compared multi-unit activity from the raw signal with running speed, and shifted the running and stopped labels in time. I named the two sessions where this could not settle the clock.
5. **Blocked claims have no output to point to.** I tagged the size-estimate cell `size-estimate` and pointed every outcome there.
6. **Supplementary file naming.** The claims file calls the per-mouse summary table supp1.docx, but under `paper/` it is supp2.docx (supp1.docx is the MDAR checklist). I read the table from supp2.docx; it changes nothing.

## 4. Runtime and failures

- **Runtime:** the run took about 55 minutes (19:10 to 20:05 UTC). The notebook runs in 3.5 to 7.5 minutes.
- **Slow first pass:** my first survey of the files used threads and took 17 minutes, because h5py only lets one thread read at a time. I switched to processes, and the survey now takes about 2 minutes.
- **Blocked cleanup:** the harness left an empty `.claude/.cc-writes` folder in `entries/000943-clark-2024/`. My attempt to delete it was refused, because it needed an approval this session can't give. It should not be committed.
- **Untracked files:** the checkout also has untracked files that are not mine (`.bashrc`, `.idea`, `scripts` and others). I left them alone.
