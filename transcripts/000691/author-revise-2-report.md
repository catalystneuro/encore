I made no outcome changes and proposed none, so the verifier agrees with all 23 outcomes and no third round is needed. Every correction in this round is to text.

**Re-run.** `python tools/entry.py all` stops at its check step because of 11 errors in the earlier record `attempts/000691-scherrer-2023-01.yaml`. That record was written against an older claims file, and the protocol says earlier records stay as they are, so I didn't touch it. The new record has no errors. As in the round-1 revision, I ran `entry.py run` on its own. It hit the 2-hour tool limit after six notebooks. I ran the seventh, `decoding_reduced.ipynb`, by itself in the same environment (20.3 min). All seven finished, the slowest in 22.4 minutes, under the 30-minute limit.

**What the re-run showed.** The verifier thought the mismatched numbers were left over from another run, which was right. The cause is that some results change between runs on different machines, even with every seed fixed:
- **fig1f fits:** my run prints exactly the numbers the prose already had (4.467 µm at the centre, 15 of 118 beads moving, lower-cost costs 60.092 against 79.942). The run the verifier reviewed printed 4.422 µm, 14 of 118, and a lower-cost centre of 4.084 µm, which is within tolerance.
- **Reduced runs:** they differ too. For ed9c, 7 of 56 map points are significant in my run and 0 in the verifier's, so test (i) holds in one run and fails in the other. These runs decide no outcome.
- **Cost estimates:** about 33 h in my run against 24.6 h in the verifier's for the full (n2) null. Both are far over the limit.

I couldn't find the cause. Running the small-subset fits in parallel threads gave identical results on test data, so the notes report the variability without naming a cause.

**Corrections:**
- **fig1f:** the conclusion and notes now use this run's numbers. They say the fits differ between runs and give the verifier's run's values in the record. The verifier was right that the old reason for "partial" (centre 0.067 µm off, edge within) didn't hold in its run. The new reason holds in both runs: under reading (a), one position is within tolerance for each set of fits. The deviation no longer says the fits differ only "in the last digits".
- **fig1e:** I added 6.884 for reading (c) under Jacobian scaling. The minor-axis edge stays 5.203, as my run prints it; the verifier's run printed 5.202.
- **Timings and reduced runs:** the fig2, fig2k, fig2l, ed9b and ed9c conclusions and notes now use this run's figures, with the verifier's run's figures in the record.
- **Notebook headers:** the two null-(n2) notebooks now say "more than a day on four cores", and that 8 decoders is a number chosen to keep the notebook well within the limit, not "as many as fit". The reduced notebook no longer quotes "4 to 11 hours".
- **README:** run times are now the ranges seen in both runs.
- **Main notebook cell 23:** fig2d is now described as methods_underspecified, matching the record.
- **Movie wording:** the README, main notebook cell 0 and `entry.yaml` now say "the imaging video", consistent with the raw video, instead of stating it is the raw video. Cell 17, the motion summary and the finding now say "rigid shifts against a template", not "frame-to-frame".
- **Round-1 record:** the ed8 reason again says the split is at the midlines "of the footprints' extent", as the verifier wrote it.
- **Round 2:** recorded under `verifications` for all 23 claims, with the verifier's reasons in its own words and my responses.

**Not done:**
- The executed notebooks show this run's numbers. Any later run on another machine may print slightly different PSF fits, reduced-run counts and timings; the notes say so.
- I left the `runtime_minutes` values in `entry.yaml` as they were, since they are within a minute or two of this run's times.

Nothing is committed, as you asked.
