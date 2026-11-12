No outcome changed. The second verifier disagreed with one outcome, fig7g: it is still partially reproduced, and reproduced is written under `proposed` for a third round. I re-ran the entry once with `python tools/entry.py all entries/plitt-2021` and it passed (part 1 took 53 min, part 2 20 min). `entry.py check` passes with 0 errors.

**Outcomes**
- **fig7g:** The verifier pointed out that this claim's criterion names no partial outcome, and its test passes as written. Both signs are as expected, and the magnitudes (0.098 and 0.626 bits) are below the neural means (0.223 and 1.125). The attempt applies the same rule to four other claims. So the proposal is reproduced. The caveat stays in the notes: the rare neural mean it is compared with has the wrong sign. The fig7/fig7g conclusion, the summary table and the README row now say this.
- **The other 28:** The verifier agreed, and they are unchanged.

**Corrected or added**
- **edf5:** The conclusion and the record notes now use this run's numbers. That is 16 of 20 clusters significant against 100 shuffles and 13 of 20 against 1,000, with 292 cells between the manifolds. The leave-one-mouse-out results are 0.372 to 0.688 (median 0.546), above the mouse relabelings in 5 of 20 clusters.
- **Why edf5 keeps going stale:** The UMAP layout changes from run to run even though every seed is fixed. The kept cells (18,742) stay the same, but the cluster counts move. The conclusion now says this and lists the counts from each run seen; both readings of the claim held every time.
- **edf6:** F5 is now given as 3.4 from a session at about 12.26. That session's value changes in the third decimal between runs (12.262, 12.266, 12.264).
- **Clock check (nb1 cell 9):** It now says 44 of 47 sessions peak within 0.5 s and three at about 1 s, so the clocks agree to within about a second, not half a second.
- **Unmatched deposit files:** The record's finding now says R6's 12 unmatched files fall on seven dates, five before its session 8 and two after it.
- **Small fixes:** The 3.5% figure now points to its section in part 2, not part 1. The notebooks now give the questions file as `questions/plitt-2021.yaml` everywhere. The README timings now give the ranges seen (34 to 53 min and 16 to 20 min).
- **Verification record:** Round 2 is under `verifications`, with all 29 claims, the verifier's reasons in its own words, and my responses.

**Not done, and why**
- **No new reader question for fig6d.** The verifier said the claims file wrongly credits the criterion's formula to the paper's code. The existing fig6d question, asked 2026-11-10, already quotes that attribution and the code line that differs. I said so in the response instead of adding a duplicate.
- **Place-cell excess:** It is still unexplained, about 60% above the paper. The verifier agreed the outcomes are stated correctly, and nothing new was tried.
- **R5 session 8 (edf7):** This failing session is one of the R5 files replaced in this version, without release notes. The materials cannot show whether the replacement changed it; the existing finding records that.
- **No second run.** All edits after the run were to markdown only. I copied the edited text into the executed notebooks and checked that every code cell matches the run; outputs are untouched. A second run would change the edf5 numbers again.
- **Untracked files:** `git status` shows dotfiles (`.bashrc`, `.gitconfig` and others) and a `scripts` directory at the repository root that I did not create. I left them alone.

Nothing is committed.
