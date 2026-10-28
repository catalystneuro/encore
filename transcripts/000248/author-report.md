Every claim is recorded as blocked. Two commands I ran without a time limit hung for about two hours in total. The notebook was not executed until after the 04:49 cutoff, so no outcome comes from a notebook run.

## 1. Outcomes

| Claims | Outcome |
|---|---|
| 18 Neuropixels claims: unit counts, IC-encoder and segment responder counts, exclusive-center RF (fig1e/f/g), fixed gaze (ed2b, ed2f), pupil and gaze (ed2g, ed2a), cross-correlograms (fig2d), decoding (fig3a, 3c, 3d, ed7a, ed7b, ed6ef), ed6cd | blocked, `too_large` (ran out of time) |
| supp3-decoder-types | blocked, `too_large` (the 50,000-epoch network is estimated at hours) |
| 21 claims on 2p imaging, mesoscope and holography | blocked, `data_missing` |

The entry is in `entries/000248-shin-2025/`: notebook, `illusion.py`, README, lock file. `tools/entry.py all` passes; the notebook ran in 1,202 s, after the cutoff, and I did not review its outputs. `handover` is built and the record is `attempts/000248-shin-2025-01.yaml`. I pinned 0.240502.2344 because it is the only published version and the paper cites none.

## 2. The dataset

The record has seven findings:
- **2p data missing:** the dandiset holds only the 12 Neuropixels sessions. The paper names no public archive for the 2p data, and its Code Ocean capsule returned 403 from here.
- **Noise units included:** the files contain units labelled `noise`, although the Methods say none were packaged.
- **Mouse count:** the Methods list 14 mice (10 Sst, 4 PV); the files hold 12 (9 Sst, 3 Pvalb).
- **Pupil units:** pupil position is labelled meters but the values are camera pixels, with no conversion to degrees. The 8-degree criterion therefore cannot be applied; only the code's 20-pixel reading can.
- **Eye frame rate:** the eye video is 60 Hz; the Methods say 30 Hz.
- **No image names:** the IC block tables give each image only as a frame index. The image templates stored in the files match the code's names.
- **NaN timestamp:** the last eye timestamp in each session is NaN.

Development runs on cached data were done outside the notebook, so under the protocol they supply no numbers to the record.

- **Assumptions:** reading (b) of fig1e's ed6b criterion was run two ways, citing the Methods' "All units not classified as noise were packaged". The decoder's reading (b) was limited to C from 10^-3 to 1, and to V1 only, for time. Both are recorded in the notebook.
- **Questions for the paper's authors:** none filed.
- **Questions to a reader:** none.

## 3. Protocol issues
1. **Check can hang.** The long-literal regex in `tools/entry.py` backtracks without end on a two-line integer list (the 22 trial codes in the helper), so `check` hung with no message. I split the list. The checker should guard against this.
2. **No time limits on commands.** The protocol says to time subsets but not to wrap commands in timeouts. A development run whose SVM step was very slow (large C), and the hanging check, cost about two hours. I recorded the claims as `too_large` with the reason given.
3. **Tight time budget.** Many SVM fits (63 session-area pairs, two readings, TRE and XRE decoders) do not fit in a 30-minute notebook. I limited the inner C search to V1 and said so in the notebook.
4. **No category for "not reviewed in time".** Neither `too_large` nor any other reason fits well, so I used `too_large` and explained in the notes.

## 4. Runtime and failures
Run from 00:36 to about 05:12 UTC. Loading all 12 sessions takes about 2.5 minutes; the whole notebook took 20 minutes. Failures were the two hung commands (one hour each), the 403 from Code Ocean, and the network decoder being too slow to run.
