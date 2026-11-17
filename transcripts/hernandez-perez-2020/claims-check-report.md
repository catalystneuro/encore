I checked `claims/hernandez-perez-2020.yaml` against the paper, made five corrections, and the file is ready for an attempt.

**Checker result:** before my changes it reported `24 claims, 24 quotes, 53 statistical values, 0 problems`. After them it reports `24 claims, 24 quotes, 55 statistical values, 0 problems`.

**Changes, by claim**
- **fig5c-peak-trough-gradient:** the ventral tolerance was 0.09, and the file said this covered both ways of reading the printed interval "[–0.16 – 0.01]". It did not cover an upper bound of +0.01. The paper prints intervals that span zero with a dash before both bounds (Figure 2G, "[–0.08 – 0.93]"), so I read this one as -0.16 to 0.01, added it under statistics, and set the tolerance to 0.11.
- **fig5c-rise-decay-gradient:** the file read both intervals as all negative "since the median must lie inside". That reason fails: -0.43 and -0.11 also lie inside the other readings. I replaced it with the paper's own typography: an interval starting with a minus sign drops the sign of its upper bound, as in Figure 8D's "[−3.52–2.71]", where all six slopes are negative. Values and tolerances are unchanged.
- **fig8d-absolute-delay-slope:** it had the same faulty reason for its interval. The reason is now the paper's test result: signed rank 0 of 21, so all six slopes are negative.
- **fig2c-coherence:** reading (b) said MATLAB `cohere` defaults to 50% window overlap. Its default is no overlap, so I corrected it. This rests on my knowledge of the old MATLAB function, not on the paper.
- **fig6c-delay-phase-slope:** the slope was fixed as one line fitted to all rats' points pooled. The paper prints it with a bootstrap interval, and its Methods report summaries as medians with bootstrap intervals. I added the median of the six per-rat slopes as a second reading.

**Checked and unchanged:**
- The one equation lost from the text (the delay due to waveform asymmetry) matches the paper's Europe PMC XML, which I fetched.
- The file reads the paper's "rank sum [max]" test as an exact signed-rank test on six values. Its p-values (0.03, 0.06, 0.09, 0.16, 0.84; 0.25 for n = 3) are correct for that test.
- Every tolerance taken from an interval uses the farther bound.
- Every main finding has a claim, and every claim comes from this paper.

**Still open (recorded under `checks`)**
- **fig4d-mua-phase-shift:** the paper prints a test on 3 rats whose maximum is 21, which no signed-rank test of three per-rat values can give. The two readings in the criterion are the file's own, not the paper's.
- **fig5c-rise-decay-gradient:** the ventral interval is settled by typography only. The text does not rule out -0.13 to 0.09, which would widen the tolerance to 0.20.
- **Multi-unit claims (fig4d):** they need broadband layer II recordings. The dataset description lists only LFP at 500 Hz, too slow for the 600 to 3000 Hz spiking band, so whether the dataset holds them is for the author to find.
- **No PDF:** none was supplied, so no figure could be read. Per-rat values, the electrode reconstruction in Figure 3B and the sites compared in Figure 5C rest on the text and legends.

**Ready:** yes (`ready: true`). Nothing is committed.
