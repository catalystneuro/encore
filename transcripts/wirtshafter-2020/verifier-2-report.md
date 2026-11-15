**Verifier report, round 2: Wirtshafter & Wilson 2020 on CRCNS hc-29**

The claims file lists 31 claims and the attempt record gives 31 outcomes: `units-recorded` is partially_reproduced and the other 30 are blocked (data_missing).

### 1. Outcomes

- **`units-recorded`, partially_reproduced: I agree.** Cell 24 prints 452 LS and 178 HPC clusters from 6 rats, against the paper's 452 and 178, so both are within tolerance. 410 LS trains are distinct, also within ±45. The counts of 165 CA1 and 378 LS cells meeting the criteria need speed and coverage, so they are blocked correctly. This is the label I asked for in round 1.
- **The 30 blocked claims, blocked (data_missing): I agree with all 30.** Nothing in the new outputs changes this. Cells 15–16 find no position or behaviour variable in the three files. Cell 17 lists the code repository: its own non-code files are all ≤8.5 kB.
- **Assumptions.** No outcome has `assumed: true`, so there are no assumptions to judge. The two deviations for `units-recorded` (counting deposited clusters, and leaving the two criteria counts uncomputed) are stated and reasonable.
- **Claims file.** I found nowhere that it misreads the paper. Paper line 77 gives "165 CA1 … 378 LS cells meeting spike rate and track coverage criteria", which matches the claim.

### 2. Sentences the outputs do not support

1. **"No minute without a spike" (README; finding 4; cells 13–14).** The README says "no recording has a minute without a spike". Finding 4 says "no recording has a stretch of 60 s without a spike from any of its clusters, so neither the time bases nor the spikes mark the session". Cell 14 says "the spikes do not mark a 30 min maze session either".
   - `spike_gaps` only measures gaps between a recording's first and last pooled spike. It never counts the silence before the first spike or after the last.
   - Cell 11 shows that this silence is large. Rat 9's spikes cover 0.76 h of a 4.77 h recording (fraction 0.16), rat 8's cover 0.54 of 1.87 h, and rat 6's median fraction is 0.34. So several recordings have hours with no spike.
   - Cell 12 itself says the rat 7, 8 and 9 spike spans (0.5–0.9 h) are "in line with a 30 min session". In those rats the spike span may well mark the session. The fair claim is narrower: no silent stretch *within* the spike span.
   - The check also leaves out one recording. Cell 13 drops the 43 copies, which leaves 18 of rat 7's 19 recordings, so 45 of the 46 recordings with clusters are covered, not "every recording".
2. **Cell 28, Summary, first bullet:** "so none of the paper's 31 findings can be tested". This contradicts the partially_reproduced outcome given in the same sentence and in the table. It should say 30 findings, or "none beyond the counts of units recorded".
3. **Rat 6 tetrode 26.** Three places describe this:
   - Cell 28 says "one cluster per recording holds all the spikes of the others".
   - The README says "holds the spikes of the others on its tetrode".
   - Finding 3 says "holds at least 99% of the spikes of the tetrode's other clusters".

   Cell 19 prints only that each of the 14 recordings has a cluster holding ≥99% of *another* cluster's spikes. It never prints the number of tetrode-26 clusters per recording, so "the others" (all of them) is not shown. "All" also overstates a 99% threshold.
4. **Finding 3:** "against a median of 0.8% (at most 12%) for the same pairs with one train shifted by 1 s". Cell 19 computes the shifted control over all 117 same-recording pairs, not the 24 cross-tetrode pairs. The maximum still bounds those 24, but the median is not theirs.
5. **The 8.7 ms lower bound (cell 10 and finding 4):** "25 brief gaps of 8.7 to 93 ms". Cell 9 prints the count (3+5+5+8+2+2 = 25) and each recording's *longest* interval. 8.70 ms is the smallest of those maxima. The shortest of the 25 gaps could be anywhere above 1.5 × 3.2 = 4.8 ms, so the lower bound is not shown.
6. **Finding 2:** "27 of them hold spikes *after the end* of their recording's timestamps". Cell 11 counts spikes *outside* the recording (before the first or after the last timestamp), so "after the end" is not shown.
7. **Cell 14:** "the longest silence anywhere is 38 s (rat 6, 2017-05-01)". Cell 13 prints 38.15 s for rat 6 but does not name the recording.
8. **Cell 18:** "so no session's tracking is in the repository". This is inferred from file sizes, but the largest files are 640–860 kB `.mat` files. One session's x and y in single precision is about 430 kB, so size alone does not rule tracking out. Of the 177 files that could hold data, only the 12 outside the libraries are listed, and that includes the 51 `.mat` and 2 `.nex` files. Excluding `hc-29/include/` as third-party is not shown to be right. This is still very likely true, but not demonstrated.

Everything else checks against the outputs:
- the cell 25 Result (452/178, 410, 423/166);
- the remaining Summary bullets;
- the README counts (57 recordings, 43 names, about 5 min against 251 s);
- the record notes for `units-recorded` (42 = 41 + 1 copies, all 178 CA1 trains distinct);
- the notes of the 30 blocked claims;
- finding 4's sampling and repeat figures;
- finding 5.

**Round-1 reasons in the record.** The record gives my reasons faithfully. For the 30 blocked claims they are verbatim, and for `units-recorded` they are combined with problems 1–3, still in my wording.

### 3. Round-1 points

**Resolved:**
- **Problem 1:** the outcome is now partially_reproduced.
- **Problem 4:** cell 27 has no default need, and it prints the claims without an entry and the entries without a claim; both lists are empty.
- **Problem 5:** cells 5–6 now say that rats 10 and 12 give 184 of 452 LS clusters.
- **Problem 6 and the numerical helpers:** cell 21's synthetic test gives the expected answers.
- **Times.mat middle:** cell 9 reads every interval and finds no change of rate and no gap of 0.1 s or more.
- **The code repository:** it is listed in cell 17, but see item 2.8 above.
- **Problems 2 and 3:** these needed no change, and none was made.

**Remaining.** None of these changes an outcome, since every blocked claim fails for lack of position whatever the epoch evidence shows:
- **The maze-session window (item 2.1).** The new spike-gap output does not support "nothing marks the session" for rats 6, 7, 8 and 9. In those rats the spike span itself may bound the session. Finding 4, cell 14, the Summary and the README should be narrowed to "no silent stretch within the spike span", and the excluded rat 7 recording should be noted.
- **The "31 findings" wording in cell 28 (item 2.2)** contradicts the outcome for `units-recorded`.
- **The 410 distinct trains.** This bears on the remark that the count is "still within tolerance" (cell 25; record notes), not on the outcome. 410 discounts only byte-identical copies. If the rat 6 tetrode-26 clusters that hold the others' spikes are, as finding 3 suggests, not single units (at least 14 of them), and MUA9 is also dropped, the LS count would fall to about 395 or below. That is outside 452 ± 45. The outcome stands because the paper's 452 evidently counts these same entries, but the robustness remark is stronger than the outputs support.
