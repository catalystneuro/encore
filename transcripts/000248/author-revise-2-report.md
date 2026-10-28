I've worked through all the round-2 points. In line with the round-2 rule, every recorded outcome stays as it was, and two changes are proposed under `proposed` for a third round to decide.

**Proposed outcome changes**
- **fig2d:** I'm proposing a change from reproduced to blocked (methods_underspecified). A new cell applies the criterion exactly as written: 7 of 8 combinations meet it. The one that fails has medians of 1 and 1, and equal medians are not a higher median, so there is no tie to break. I now agree with the verifier on this. The recorded outcome is now marked `assumed: true`, and the deviation quotes the protocol passage that the tie-break relied on.
- **fig3d:** I'm proposing a change from partially reproduced to reproduced. I re-ran decoder reading (b) on every area with the two extra seeds:
  - With seed +100000, five areas are significant (V1, LM, RL, AL, PM; AM p = 0.083).
  - With seed +200000, five areas are significant (V1, LM, RL, AL, AM; PM p = 0.052).
  - In both, LM, V1 and AL have the three largest scores.
  - The criterion is met in five of six runs (two readings, three seeds). The partial outcome comes only from the first seed under reading (b). Whether PM or AM is the significant one changes with the seed, and the finding that asks the authors now says so.

**Outputs added**
- The two seed runs are in two new notebooks, `decoding_seed1_shin_2025.ipynb` and `decoding_seed2_shin_2025.ipynb`, one seed each so each stays under the 30-minute limit.
- The check of the C range and the one-vs-all coding now covers V1, PM and AM. C above 1 does better in only 1 of 35 sessions (PM, by 0.001), and most of those fits did not converge. One-vs-all changes the best inner accuracy by -0.026 to 0.027. Cell 12 is rewritten to say this, with the caveats.
- A new check in reproduce cell 13 shows that XRE1's real bar has IC1's orientation (0.924 of central pixels agree with IRE1, against 0.656 with IRE2).
- The new seeds also confirm fig3c: under reading (b), both values stay within tolerance.

**Text corrections**
- fig1e (cell 30 labels, cell 31, record): the counts now read 383 units, then 68 with exactly one passing position, then 44 where that position is the center.
- supp3: the network timing now uses this run's figures (4.38 ms per epoch, 18.3 h on one core) and says timing varies between runs.
- ed7a: the notes now name RL and LM alongside PM and AM.
- Checks cell 9 now covers reading (a) only, and checks cell 12 is rewritten as above.
- Smaller fixes: the README load time (now 4 to 5 minutes, with the notebook list and outcome table updated), the waveform minimum (0.014 ms), and the ed2b reservation added to the notes and cell 40.

Round 2 is recorded under `verifications` with all 40 claims. `entry.py check` passes with 0 errors.

**Not done, and why**
- I ran `tools/entry.py all` once, and all five notebooks passed. Then I fixed two printed labels in the reproduce notebook, so I re-ran only that notebook in the same environment. After that I changed only markdown in the other four and copied it into their executed copies; their code is unchanged, which I checked. I did not run `all` a second time because it would change the network timing that the text now quotes.
- The checks notebook takes 26.6 minutes, close to the 30-minute limit.
- I did not change ed2b. The verifier agreed with it and only recorded a reservation.
- I added no questions to `questions/000248.yaml`. The verifier found no place where the claims file misreads the paper, only criterion problems.
- I did not compute how the one-vs-all coding would change the inference scores.
- There are untracked dotfiles and a `scripts` directory in the repository root. I didn't create them and left them alone.
