There was one open question, and the claims file changed.

**fig5f-condition-specific-next-command** (are the Table S1 row 5E errors in the command's own units, or ten times larger?): **Changed.** The values are ten times the command's own units.
- **Paper:** it gives no unit. The Methods say only "The L2-norm of the difference was computed", so the paper's code decides it.
- **Code:** the function that prints the 5E error and its shuffle 5th percentile is `pred_fwd.frac_next_com_mov_sig` (`pred_fwd.py` lines 326-330 and 606, at the commit the claims file records). It applies the decoder gain K to activity loaded by `DataExtract.load`. That loader multiplies spike counts and the predictions by 10 (`mult = 10.`, `generalization_plots.py` lines 204-206 and 256).
- **Edit:** the criterion now says the error is computed this way, ten times the error in the command's own units. I also added a line to the file's `checks` log saying what this answer changed.
- **Unchanged:** the expected values (3.956 for Monkey G, 7.324 for Monkey J), their tolerances, and the shuffle values (5.38, 9.240).

`python tools/claims_check.py` reports 0 problems. The question has its `answer` and `answered: 2026-10-30`. Nothing is committed or pushed.
