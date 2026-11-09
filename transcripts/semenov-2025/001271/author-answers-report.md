I re-ran the one claim the reader amended. Its outcome moves from partially reproduced to reproduced, and it still rests on an assumption. The entry was locked, checked and run: 0 errors, and all three notebooks pass (Figure S2 notebook 391 s, Figure 3C notebook 44 s, Figures 1 and 2 notebook 1115 s). The handover is built in `executed/001271-semenov-2025/handover`. I did not verify my own work, and nothing is committed or pushed.

## Question: fig2-modulated-locks-to-beats

**What I asked.** The header's standard definition of "sustained firing" (header item O4) is at least three APs with one in the last 50 ms of the stimulus. The fifth beat peaks 225 ms into the 250-ms wave, so a neuron firing one AP per beat meets that definition. Did the paper mean firing that is not tied to the beats?

**What the answer changed.** The reader agreed and amended the criterion. A modulated session now counts as sustained firing when either:
- one beat holds more than two APs, or
- the session has 5 APs or more and at least as many of them fall outside 12.5 to 37.5 ms of a beat as inside.

Sustained depolarization is still tested as in O4. The statement and the other tests are unchanged.

**What I re-ran.** I rewrote the test in `reproduce_fig1_fig2_001032.ipynb` (claim cell, conclusion and summary). The notebook still prints the old O4 count for comparison, and a printout of the one session that fails.

**Outcome.**

| | Earlier | Now |
|---|---|---|
| fig2-modulated-locks-to-beats | partially reproduced (assumed) | reproduced (assumed) |

- 12 of the 16 combinations of AP-detection settings pass: all four with the main soma outline (O1(a)) and the 5-SD height, and all eight with the eroded outline (O1(b)).
- With the main outline and the 5% height:
  - 92% of 212 APs fall within 12.5 to 37.5 ms of a beat, against 49% for unmodulated waves.
  - No session has more than 8 APs.
  - All 14 sessions with 5 APs or more have most of their APs near the beat peaks.
  - No session shows sustained depolarization.
- The four main-outline settings with the 5% height fail because of a single session: subject 9_2 at 2 kHz and 3.4 V, with three APs in the fifth beat. Its baseline noise (SD 9.8% dF) is about twice the 5% level. Its peaks are 11 to 22% dF, and none of them passes the 49% dF that the 5-SD height sets for that session.
- **The new assumption:** the 5-SD height decides for this claim, because the 5% level sits inside that session's noise.
  - It is recorded as a deviation.
  - I added a note on it to the existing question to the paper's authors about how APs were counted.
- The earlier assumption that the main outline decides is no longer needed, since the eroded outline passes too.
- Under the old definition, 15 to 32 modulated sessions would still count as sustained firing. The amended rule flags 88 of the 197 unmodulated sessions with 3 APs or more, so it does tell the two kinds of wave apart.

## Other changes

- **A corrected number.** This run gives a slightly different p-value for fig2c-pure-more-aps: 2.3e-10 to 7.8e-07, where the text said 4.7e-10. I corrected it in the notebook conclusion and the attempt record. Its outcome stays reproduced (assumed).
- **The same small drift in fig2-modulated-locks-to-beats.** The first run recorded 213 APs and 91%; this run gives 212 APs and 92%. The code changes alone don't explain this, and I did not track down why. All other conclusions match the executed numbers.
- **Run times.** I updated the timings in `README.md`. The Figures 1 and 2 notebook now takes about 19 minutes, most of it streaming, where it took about 6 before.

Files changed: `attempts/001271-semenov-2025-01.yaml`, `entries/001271-semenov-2025/README.md`, `reproduce_fig1_fig2_001032.ipynb`, and the summary row in `reproduce_semenov_2025.ipynb`.
