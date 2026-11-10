I tested 1 of the 39 claims and blocked the other 38. The entry passes `tools/entry.py all` (0 errors; the notebook runs in about 21 s), and the handover is built in `executed/kennedy-2020/handover/`. The main reason so much is blocked: the dataset holds no stimulus times or names, so no stimulus response can be located.

**1. Outcomes**

| Claims | Outcome |
|---|---|
| `imaging-cell-counts` | not_reproduced as the claims file states it (see below); a reader is asked |
| 20 photometry, behaviour, optogenetics, tetanus toxin, slice and silicon probe claims (`fig1*`, `ed1` to `ed4`, `ed6`) | blocked, data_missing |
| 15 imaging claims (`fig2*`, `fig3*`, `ed7*`, `ed9`, `fig4cd`, `fig4g`) | blocked, metadata_insufficient |
| 3 model claims (`fig4e`, `fig4h`, `fig4ijk`) | blocked, metadata_insufficient, because they depend on blocked imaging claims |

**2. The dataset (DANDI:001182, version 0.240827.1656)**

- **Version:** this is the only published version and the paper cites none. The draft holds the same files with the same blobs and sizes.
- **What it holds:** 15 files, one per mouse (M1 to M5) and day (1 to 3). Each has a frames-by-cells trace matrix and one annotation, "Ch1: baseline", which is empty for M3, M4 and M5.
- **What it lacks:**
  - stimulus onset times and stimulus names;
  - cell identifiers, cell footprints and the registration of cells across days;
  - the photometry, behaviour, slice and silicon probe data, which are not anywhere else on DANDI either.
- **Cell counts match the paper exactly:** summed over the five mice, the days hold 203, 183 and 176 cells, a mean of 187.33 with an SEM of 8.09. That is the paper's 187.3 ± 8.1, which supports that these are the paper's cells.
- **Metadata errors:**
  - the files say "VMHvl" and "GCaMP6m"; the paper imaged VMHdm/c with GCaMP6s;
  - every file has the same session start time;
  - the subject id changes per file, so the archive counts 15 subjects for 5 mice;
  - every file states 11 Hz, while the Methods have one mouse at 20 Hz;
  - the units are given as both "DF/F" and "a.u.", and the values are not in the Methods' baseline-SD units.
- **Possible joins:** steps shared by many cells recur about every 100 s, and the baseline intervals start and end on them. This fits the Methods' joining of a day's recordings into one stack, but any joins are unmarked.
- **Checked and fine:** no recording is deposited twice. Columns are sorted by amplitude within each file; they give no sign of being the same cell across days.
- **Assumptions and questions for the paper's authors:** none, since no outcome rests on a method choice.
- **Question to a reader** (`questions/kennedy-2020.yaml`): the claims file gives 187.3 the unit "cells per mouse per day". Per mouse and day the data hold 37.47 cells, so the claim fails as written. The paper's number is the total over the five mice per day. On the same reading, "78 tracked cells" is also the total over the mice: no mouse has 78 cells on every day.

**3. Where the protocol was unclear**

1. **A claim with one part untestable and the other failing on the file's unit.** I recorded not_reproduced: the criterion needs both parts, and the file's reading fails either way. The protocol says nothing about mixed cases like this.
2. **`measured` with two expected values when one cannot be measured.** The schema allows no null, so I gave the single number and explained it in the notes.
3. **The shared-clock check (step 2) with no trial table at all.** I named every session as not established and showed only that the baseline intervals line up with the steps in the traces.
4. **Inferring stimulus onsets from the responses.** The protocol does not say this is forbidden. I judged it circular, since identity cannot be recovered that way, and blocked the claims as metadata_insufficient.
5. **The model claims.** Their simulations need no data, but their scores are measured against blocked data curves. I applied "a claim that depends on a blocked claim is blocked for the same reason" and did not run the MATLAB code, which also calls functions missing from its repository.
6. **The questions file.** `questions/README.md` names files `<dandiset>.yaml`, while the protocol and the existing files use the paper key. I used `questions/kennedy-2020.yaml`.

**4. Runtime and failures**

The run took about 16 minutes, from 03:12 to 03:28 UTC, and nothing failed. For exploration only, I cached the extracted trace arrays in `$TMPDIR`; the notebook itself streams every file. Nothing is committed.
