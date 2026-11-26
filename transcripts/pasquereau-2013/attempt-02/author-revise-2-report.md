The round 2 verifier agreed with all 28 outcomes, so no outcome changed and I proposed no changes. It also now accepts `false-positive-rate` as blocked (methods underspecified), which settles its round-1 disagreement. I re-ran the entry twice with `python tools/entry.py all`; both runs passed with every number the same as before. `entry.py check` reports 0 errors.

**What I corrected (text only, no analysis changed):**
- **README run time:** it now gives the latest run's 4.1 min (1.7 to 5.2 min in earlier runs).
- **The m2 claim (Summary and README):** "the m2 response is smaller after MPTP, not larger" now says the comparison is possible at one command step only, with 66 against 11 channel-sessions. There the combined median is smaller after MPTP, but on triceps longus 2 it is larger (52.2 against 113.0, 4 post-MPTP channel-sessions, p = 0.36). The cell 95 conclusion and the record's notes now give that triceps longus 2 result too.
- **m2 and command size (cell 95 and the record's notes):** they now say m2 does not rise with command size before MPTP but does after (1.81 to 194.4).
- **Header count in the Summary:** it now reads "`false-positive-rate` and the 15 claims blocked by it" where it said "16 claims blocked by the false-positive rate".
- **Cell 43:**
  - The rates are now "about 23 and 46 times the paper's", where it said "more than 3 times".
  - The two clashing sentences are merged: either the procedure here differs from the paper's, or the paper's stated rate does not hold, and the analysis cannot tell which.
- **Cell-directions that "can never respond" (cell 43 and the record's notes):** this now applies only to the 14 with a baseline SD of exactly 0. Nearly silent cell-directions with a threshold of about 0 can still respond, and add to the false positives; v5801.1 is given as the example.
- **Changes paragraph:** the Summary now has one for the second verification round.

**Recorded:** I added round 2 under `verifications` in `attempts/001636-pasquereau-2013-02.yaml`. For each of the 28 claims it gives agrees: true, the outcome, the verifier's reason in its own words, and my response.

**Not done:**
- The verifier could not check the claims file's expected values against the supplementary table, because it had no PDF reader. I did not check them either; the record notes this as unchecked.
- I left the round-1 cell numbers in the record as the round-1 report gave them, though the cells have since been renumbered.
- Changes are not committed, as instructed.
