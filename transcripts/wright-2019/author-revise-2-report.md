Round 2 is answered. All 39 outcomes are unchanged (32 reproduced, 7 partially reproduced), and nothing is proposed for a third round. The verifier agreed with every outcome. All its points were wording errors or a missing printed output, and none of them moves an outcome.

**Corrections made:**
- **fig2e-departure-times:** the conclusion cell, the record note and the finding now give the times measured by window end: 3.7, 5.5, 6.1 and 7.4 s (measure a) and 3.7, 5.7, 6.2 and 7.4 s (measure b). By window end, the danger time at p < 0.00025 is within tolerance. The danger time at p < 0.05 (3.7 against 2.8 ± 0.28) and the uncertainty time at p < 0.00025 (7.4 against 6.5 ± 0.65) are not. No reading puts all four times within tolerance, so it stays partial. I left the verifier's round-1 reason as it was recorded, even though it has the same error.
- **Summary, match to the paper:** I replaced "most reported statistics to their printed precision". It now says only a few values match exactly (F = 7.16, F = 3.14, the fig5i means). Many are close but not exact, and some miss widely (fig6ef: 3 of 20 against the paper's 13 of 20, and the fig2e times).
- **The data set's script (`cubeScript.m`):** the data-check cell now also prints the script lines showing that the 20 s nose-poke baseline is used for both the total ratio and the 1 s interval ratios. This is the output the verifier asked for. The text under that cell, the Summary and the finding about the script now say this.
- **fig6ef note:** it said one reading had a different outcome before and two do now. In fact two readings differed before as well. The note now says so and names them.
- **fig5s1-ramping-regressor-combinations:** the conclusion now says the claim held in all six old readings that used 2 s for both ratios, and in none of the six that used 10 s.

**Recorded:** round 2 is added under `verifications` in `attempts/wright-2019-01.yaml`. Each of the 39 claims has the verifier's agreement, its outcome, its reason in close paraphrase and my response. The verifier's general points (the Summary's precision claim, the script lines, the fig4 correlations being no stronger than Z-scoring alone produces) are filed under the claims they concern, because the record has no field for round-level notes.

**Checks:** `python tools/entry.py all entries/wright-2019` passed, the notebook ran in 122 s with 0 errors, and the numbers my text cites match the new output.

**Not done:**
- The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/wright-2019.yaml`.
- One item is still open: no second value in the paper tests the main reading's nose-poke windows. I found none, and it does not change a conclusion.
- Nothing is committed. Some dotfiles I did not create (`.bashrc`, `.idea`, `scripts`, and others) are untracked in the checkout; I left them alone.
