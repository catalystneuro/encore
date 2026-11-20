I've finished the round-2 revision of `markowitz-2023-02`. Both notebooks ran clean with `tools/entry.py all` (photometry 2,410 s, optoda 473 s), and `check` reports 0 errors. Nothing is committed.

**Outcomes**

No outcome changed, as round 2 requires. Two changes are written under `proposed` for a third round:
- **fig1f-syllable-vs-movement-onset: reproduced → partially reproduced.** I added the count-matched comparison the verifier asked for, drawing syllable onsets down to each mouse's initiation count under five seeds.
  - Against initiations from stillness, reading (a) no longer favours syllables. Under the claim's seed syllables are higher in 5 of 14 mice (P = 0.068); under the other four seeds 2 to 4 of 14 (P 0.0023 to 0.013, favouring movement).
  - Against all detections, the criterion's own definition, reading (b) favours syllables in 14 of 14 mice and reading (a) favours movement in 14 of 14 (P = 0.00012).
  - So the verifier was right: the reproduced outcome came from the difference in event counts.
- **ed10d-optoda-vigour: blocked → not reproduced.** Trying the verifier's suggestion showed that in the velocity-modulation files the detection and light-onset times are 2,700.03 s off the syllable clock. Once shifted, the velocity of the stimulated instances gives the direction of stimulation, and it agrees with the stated direction in 16 of 17 files. The criterion's test then runs on 11 up and 6 down experiments from 5 mice: up is higher but not significantly (U = 47, P = 0.180). This result rests on the clock shift, the directions read from the data, and my choice of baseline for the inclusion rule.

**Added or corrected**
- **The 2 extra experiments:** confirmed. Two 2-s excitation sessions with baseline and post-day session numbers had entered the code-reading set. I removed them and re-ran; every affected number is updated, and no outcome moves.
- **fig2k:** I ran the Methods' null (shuffling dLight values) as a variant. Reading (a) stays significantly positive (P = 0.025 and 0.005); reading (b) turns significantly negative.
- **fig3i:** I added the comparison between the two arms of stimulation minus catch. No bin differs (Holm P 0.16 to 1.0 with all trials, 1.0 with matched trial counts).
- **Within-DLS group split:** the dLight+ChrimsonR mice's syllable-onset averages peak lower (U = 48 of 48, P = 0.001) and later (0.97 to 1.0 s in 5 of 8 mice, against 0.30 to 0.33 s in every dLight-only mouse). The cause is not found; it is recorded as a finding.
  - For ed7d with the dLight-only mice alone, the syllable half holds, but the movement half goes the opposite way, so it is still not reproduced.
- **ed3c and fig2e-not-autocorrelation:** now marked `assumed: true`, with deviations explaining why.
- **Questions for a reader:** three added to `questions/markowitz-2023.yaml`, on the fig2k null, the ed3c inconsistency in the claims file, and the gap in the fig2e-not-autocorrelation criterion. The ed10i question from round 1 still stands.
- **Statements the verifier flagged:** the experiment count (now 164), the fig4i row of cell 0, the DLS files without photometry (32), and the floor of the fig2h check are fixed. The README now gives about 45 minutes and lists ed10d among the blocked claims.
- **Findings:** new ones on the clock offset in the velocity-modulation files, the DLS group difference, and a question for the authors on ed10d; existing findings updated.
- **Record:** the round-2 verification is recorded for all 44 claims.

**Not done**
- The cause of the DLS group difference was not found.
- fig1f-dip-then-peak is not re-tested with a wider window; the notes say the maximum sits at the window's edge.
- Five-seed ranges are still missing for several claims, as before.
