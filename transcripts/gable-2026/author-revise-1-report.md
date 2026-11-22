I've revised the attempt for every point in the round-1 report and re-run the entry. The notebook passes in 270 s, `tools/entry.py check` reports 0 errors, and the conclusions match the new outputs. Nothing is committed.

**Outcome changes**
- **figs4-high-couplers-correlated:** changed from not reproduced to **partially reproduced**, resting on an assumption. Following the verifier's Problem 2, I now run all four claims both with duplicated units counted once and with every stored row kept, which gives 16 readings. I adopted every stored row because only then is the paper's third Tlx mouse selected, and the sessions and neurons come closer to the code's 20 and 411. Under `baa-r` all three bins are significant (0.026, 0.035, 0.130), and seven of the eight readings that keep every row agree. Most of the gain comes from the duplicates themselves: 12 of the 14 duplicated units fall in the top bin, each paired with its own copy at r = 1.
- **figs4-middle-couplers-not-correlated:** changed from reproduced to **blocked (`methods_underspecified`)**, as the verifier proposed. Once every row is kept, the outcome no longer depends on which trials enter (O3) but on which firing rate the 0.5 Hz filter uses (O2): `baa-r` and `bab-r` give reproduced, `bba-r` and `bbb-r` give not reproduced. The Methods paragraph calls a window-based estimate "session-wide", so neither rate reading has a defensible basis. Across all 16 readings, eight give reproduced and eight do not.
- **figs4-session-selection** stays not reproduced and **figs4-lowest-couplers-correlated** stays partially reproduced. Their measured values are now under `baa-r` (selection: 10 mice, 17 sessions, 575 and 5,686 pairs; lowest bin: 0.041). The verifier agreed with both, and with the 30 imaging claims blocked as `data_missing`.

**Added or corrected**
- **Paper's code output:** the notebook now reads the printed outputs of the paper's FigureS4.ipynb at the pinned commit (neurons per session, pair counts and mean differences per bin) and compares each reading with them.
- **Outputs the verifier asked for:** a table of where the duplicated units fall (bins, couplings, twin correlations), sessions per mouse passing each filter, and trial-type counts per session.
- **Photostimulation check:** it now covers every selected session. The four sessions from the Ai32 mice have no laser trace, no photostimulation onsets and no optogenetics metadata, recorded as a new minor finding (`metadata_insufficient`) at the end of the findings list.
- **Updated findings:** the duplicate-units finding (still `critical`) now says the copies end up in the top coupling bin. The selection finding has the per-mouse detail. The `methods_unavailable` question to the authors now asks about the duplicates and the rate measure.
- **Record and docs:** the README, the helper docstring, the inputs entry and a round-1 `verifications` block (results for all 34 claims, with the verifier's reasons and my responses) are updated.

**Not done**
- No question was added to `questions/gable-2026.yaml`, because the verifier found no misreading of the paper in the claims file.
- I left the bootstrap's false-positive rate (Problem 5) and the zeroed single-trial types under O3 (b) (Problem 6) unchanged. The first is a property of the paper's method and is noted on the middle claim; the second is allowed by the claims file.
- Whether the Ai32 sessions had light during trials cannot be settled from the files.
- No reading reproduces the paper's exact 20 sessions.
