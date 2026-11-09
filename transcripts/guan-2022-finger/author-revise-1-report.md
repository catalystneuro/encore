The round-1 revision is finished, and no outcome changed. The verifier agreed with all 19 outcomes, and every one is the same after the re-run. The final `python tools/entry.py all entries/000252-guan-2022` passed with 0 check errors and took 806 s. The new numbers match the notebook text and the attempt record.

**What I added for each point in the report**
- **fig8b scaling (problem 1):** I added a cell with a synthetic check: the O4 (a) scaling returns 5.17 times the true distance, against 1.03 for O4 (a1) and (b). The cell also prints the N-PPC distance-matrix range for each, mean and per session: 0.57–3.90 for O4 (a), 0.11–0.78 for O4 (a1), 0.12–0.79 for O4 (b). The paper's text gives no colour-bar range for Figure 8a, so the comparison the verifier suggested can't be made. The outcome stays reproduced and marked as resting on the assumption. The report calls this a gap in the claims file, not a misreading, so I added no question for a reader.
- **Per-session standard accuracy (problem 2):** it now runs under every O1×O7 combination and is printed next to every O1×O6×O7 row of the CCGP table, with a verdict for each population. J-PPC within-hand accuracy per session is 0.680–0.690 in all readings. With it, the O1b/O6a/SVM reading would be fully reproduced, as the verifier expected; on the pseudo-population it is partially reproduced. I kept the pseudo-population as the assumption, so jppc-finger-ccgp-low stays partially_reproduced and marked as resting on it. Reasons:
  - the Methods call standard accuracy an upper bound on CCGP, which only holds for the same neurons;
  - the CCGP paper the Methods cite (ref 60) uses one pseudo-population;
  - N-PPC finger CCGP exceeds the per-session accuracy (ratio up to 1.31), which an upper bound would not allow.
- **Exact p values (problem 3):** the notebook now prints how many of the 1001 null values reach each observed CCGP. Hand CCGP, and finger CCGP for N-PPC and J-MC, have 0 everywhere. For J-PPC finger CCGP the count runs from 0 to 37, so p < 0.001 holds only in one reading, at the floor of the test. This fragility is now in the notes.
- **Discriminative-fraction window:** I swept the 500 ms window start from 0.5 s before to 0.5 s after the Go cue. The best values are 47.8%, 43.5% and 72.2%, still short of the paper for N-PPC and J-PPC. A 1 s window from the Go cue gives 60.8%, 56.8% and 82.9%, all within tolerance. The claims file fixes the 200–700 ms window, so the outcome stays not_reproduced. The 1 s result is in the notes and in the question for the paper's authors.
- **figs11 (problem 5):** it now also runs under O1 (b). J-PPC is lowest at every size in all 8 readings.
- **Unused shuffled-label time course (problem 6):** removed from the clock check.
- **Unit counts (problem 7):** the notebook now says that the paper's counts match the units before the 0.5 Hz exclusion, while every analysis uses the units kept after it.
- **DANDI:000147:** I checked it in the archive. It holds 10 BMI finger-press files of participant N from 2018, from the paper's ref 46, and not the alternating-cues task. The blocked outcomes stand.

The attempt record now has updated notes, deviations and findings, plus a `verifications` entry for round 1 covering all 19 claims, each with the verifier's reason and my response. The notebook's runtime went from about 7 to about 13 minutes, so `entry.yaml` and the README now say 14.

**Not done**
- **Conservative null for O6 (b) (problem 4):** I didn't change it. Averaging each of the 1001 null draws over 100 matchings would take about 100 times as long, and the outcome rests on an O6 (a) reading. It is stated as a deviation.
- **Nothing committed or pushed**, as instructed.
