No outcome changed. The verifier agreed with all 53 outcomes (27 reproduced, 10 partially reproduced, 16 not reproduced, 0 blocked), so nothing went under `proposed`. The entry passes its checks and its full run: `python tools/entry.py all entries/watson-2016` gives 0 errors and the notebook passes in 1513 s. In that run the numbers my corrected sentences rest on are unchanged.

**Corrected**, in both the notebook's conclusion cells and the attempt record's notes:
- **`fig2a-median-rates`:** the best DANDI reading is c, with five of six within tolerance (only pI REM, 6.00 Hz, misses), not reading a with four. The per-rat spread is about threefold, not twofold.
- **`post-sleep-wake-lower`:** I removed "Rank-sum tests are not significant." On CRCNS, reading ii with M1 a, the one-sided rank-sum p is 0.027; under the other readings it is 0.055 to 0.51.
- **`fig4e-within-up-sextiles`:** "DANDI: the same directions" was wrong. Under DANDI reading a(i) the top sextile rises, from 2.789 to 2.808 Hz (p = 0.64); under the other readings it falls.
- **Summary:** the WAKE-SLEEP duration (4214 s against 5918 s in Table S1) is now named as an exception, beside the microarousals.
- **Header cell:** it now says `fig5c-wake-movement` is tested on CRCNS only.
- **`fig3e-wake-before-after-sextiles`:** the notes now give p = 0.055 for the held-out ranking under M1 b, and say the claim would be partial under that reading. I kept the outcome because the criterion allows reading a and the verifier agrees with it.
- **`fig2de-fast-before-slow`:** I removed the `assumed` mark. The outcome rests on the deposited CRCNS UP states and the criterion's own 200 ms window; the DANDI detection only affects the DANDI result.
- **Round-1 reasons:** "B3" and "(B4)" now point to problem 5. Problem 4 is now cited for the four MA claims, and problem 2 for `fig4i-band-power-within-nrem` and `ma-fraction-over-nrem-episodes`.

**Added:**
- **Run-cost cell:** a new cell before the summary prints the CRCNS bytes streamed (88.9 GB), the run time (25.1 min), and the peak memory of the notebook process (2.62 GB) and of the largest loading worker (5.13 GB).
- **README:** the old "near 10 GB, about 20 minutes" is replaced by these printed figures. The worker's peak was different in each of my runs (4.88 to 5.28 GB), so the README gives "about 5 GB (4.9 to 5.3 GB)". `runtime_minutes` is now 25.
- **Round 2 in the attempt record:** recorded under `verifications`, one entry per claim, with the verifier's reasons in its words and my responses. The README and memory points, and the note that problem 6 is unchanged, are under `reviewed`.

**Not done:**
- **Problem 4, the microarousal set:** this is still open. The deposited MAs do not match the paper's 790, and the question is already filed for the paper's authors. The six outcomes that use MAs are tested on the MAs as deposited.
- **No new reader questions:** the claims-file readings the verifier refers to a reader (problem 8) are all already in `questions/watson-2016.yaml`, so I added nothing there and changed no claim.

Nothing is committed.
