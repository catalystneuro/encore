The round-2 revision is done and no outcome changed. The verifier agreed with all 29 outcomes and with both critical findings, so nothing is proposed for round 3. The final run of `python tools/entry.py all entries/carrier-2026` passed in 524 s, and `check` reports 0 errors. The executed copy shows the conclusions match the new numbers. The outcomes stay at 17 reproduced, 1 partially reproduced, 2 not reproduced and 9 blocked.

**Corrected**
- **Summary cell:** it no longer says the deposit reproduces the paper's Q10 statistics "exactly" across the board. It now names Figs. 2G, 2H, 3B and 7A to 7C as exact, and Fig. 5D and the PY-on phase as different. The scripts sentence now says no analysis script was found in the files read, since the 21 inner crab zips were only read at their start.
- **LP and PY burst files:** cell 86 now counts them in every folder, not just the "For Analysis" ones, and lists them per preparation. The count is 8 of 19, up from 6; the two added preparations are 021423 and 061223. It is corrected in cell 6, the Blocked claims cell, the fig5b notes and finding 5. The wrong phrase "the phase subset" is removed. 8 is still below the paper's n of 12 to 18, so fig5b stays blocked.
- **Smaller wording fixes:**
  - Cell 55 now says the interval is close to the paper's [1.30, 1.59], not the same.
  - Cell 71 no longer cites a Prism fit range that no cell prints.
  - Cell 76 no longer states a section runtime.
  - The README runtime now reads "seven to nine minutes".
  - The fig5b notes no longer give a reading time that no cell supports.

**Added outputs the verifier asked for**
- **Cell 15:** prints the first header line of both burst tables. Both name `0.75x_ramp.smr` from START= 329.541, which backs that detail in finding 1.
- **Cell 5:** times the reads of the 21 inner zips. The final run measured 1.6 MB/s in all, 0.4 MB/s per zip, and the fig1e notes now give that rate and its estimate of about 6 h for 37 GB. The rate varies between runs (2.0 MB/s in an earlier one).
- **Cell 86:** prints the 33.1 GB of Spike2 recordings.
- **Cell 84:** prints the power at twice crab 18's peak frequency. At 0.75x, 2.6 Hz is 47 times the window median, so the harmonic is now in the output and not only in the figure.
- **Cell 74 (fig7df):** the crab 1.25x test is re-run with the unit table's 26.0 °C for 963_106. The crab mean becomes 26.17 °C, the difference 1.91 °C and Welch P = 0.262, so "similar" holds under either value.

**Recorded**
- Round 2 is under `verifications`: all 29 claims with the verifier's reasons and my responses, plus findings 1 and 2 (both agreed, critical, severity kept).
- On fig2i, the verifier wondered whether the round-1 `agrees: false` was right. I kept it and said why: the round-1 notebook gave not reproduced, which differs from the verifier's reproduced.

**Not done**
- No questions were added to `questions/carrier-2026.yaml`, because the report names no place where the claims file misreads the paper.
- `tools/presentation_site.py` was already modified before this session. I left it as it was.

Nothing is committed.
