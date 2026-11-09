I went through every point in the round-2 report. No outcome changed, and I proposed none, so this round doesn't need a third verification. I re-ran the entry with `python tools/entry.py all entries/001791-wong-campos-2023`: 0 errors, and the notebook ran through in 59 s. All the conclusions match the new outputs. Nothing is committed.

**Outcomes:** they stay as the verifier agreed: 3 reproduced, 6 partially reproduced, 3 not reproduced, 7 blocked.

**What I corrected or added**
- **figs12 (mislabelled):** the outcome stays partially reproduced, but it is no longer marked as assumed. The verifier was right that it doesn't rest on taking column 1 as the soma. The deviation now says column 1 is *not* taken as the soma in the anesthetized recordings, and the failures under that reading are shown only as a comparison. The conclusion cell, the Summary row, the README and the notes now say the anesthetized half isn't tested, and that it would pass if column 1 were accepted as the soma.
- **fig2f-delay-range (zero delays):** the old check only looked for delays exactly equal to 0. It now counts delays that round to 0.00 at the data's 0.01 ms precision and prints the smallest values.
  - One LR delay is 3.6e-15 ms (at 181 μm), so it is effectively 0. One ST delay is exactly 0, and one is -0.20 ms.
  - The sentence saying the small delays are real values, not placeholders, is gone. It now says the file can't tell us which they are.
  - Leaving out the LR zero, 22 of 31 LR delays are still below 1.35 ms, so the outcome doesn't change.
- **fig2f-conduction-speed (point b):** I added a check and a discussion of why the speed reproduces on the same delays whose range doesn't.
  - The speed depends only on the slope. Shifting the LR delays up by 1.9 ms gives the same 0.088 m/s and R² of 0.462, with the fit running from 1.47 to 4.08 ms.
  - The paper's range implies 0.092 m/s, and the LR fit rises 2.62 ms between 50 and 280 μm.
  - So the deposited delays are offset by about 1.9 ms but agree with the paper in slope. That is why the range fails and the speed does not.
- **fig4d:** reading (c) now gives medians and p-values for each window separately: 0–5 ms, p = 6e-14 and 1.2e-05; 0–8 ms, p = 1.1e-12 and 5.9e-05.
- **fig4bc notes:** these now say that, measured from its own baseline, the second bAP is still larger than the first, just by less (median ratios 1.07 to 1.15).
- **fig4ijk:** I removed the claim that the orphan dendritic spikes have a somatic event below threshold. The text now says the soma comes close to its threshold around most of them, but the data don't show whether a somatic event is there.
- **Round 2 recorded:** it is under `verifications` in the attempt record, with an agreement flag, outcome, reason and response for each of the 19 claims.

**Not done, and why**
- The verifier found no place where the claims file misreads the paper, so I added nothing to `questions/001791.yaml`.
- The two items still open (point d) are the Fig. 2 site set and the Fig. 1 pulse times. They stay as stated assumptions, because the dandiset can't settle either.
