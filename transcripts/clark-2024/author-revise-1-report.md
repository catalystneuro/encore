No outcome changed. The verifier gave blocked, `too_large` for all 31 claims, the same as the record. It found no place where the claims file misreads the paper, so I added nothing to `questions/000943.yaml`. I re-ran the entry; it passes in 189 s with 0 check errors.

**What I fixed, point by point:**
- **Where the limit comes from (B1, C):** the size-estimate cell now cites the protocol's limit ("CI fails a notebook over sixty" minutes, `docs/protocol.md`, Author, step 3). It also says the read time is only a lower bound, since sorting would come on top. The re-run measured 72.7 MB/s, so reading the paper's 638 GB takes 2.4 h and all 976 GB takes 3.7 h. The notes for all 31 claims and the README now use these numbers.
- **Session counts (B2):** the notebook and the notes for `supp1-recording-summary` now say the dandiset's 242 sessions are 27 more than the paper's 215, which is outside the 21.5 tolerance. They also say M3, M7, M10 and M12 have 15%, 22%, 56% and 33% more sessions than the paper's table.
- **Open-arena position columns (B3):** the notebook and the `grid-cell-count` notes now say that even with sorted units, grid cells would rest on column meanings guessed from their ranges. M1 and M2 also span about 70 cm in an arena the files call 100 × 100 cm. So a re-sort could still be blocked as `metadata_insufficient`.
- **Helper docstring (B4):** it now says 100 ms bins.
- **Clock check (B5):** `shifted_contrast` no longer wraps labels around the ends of the window, and its sign now matches `lagged_corr`. On synthetic data both give +5. In the real data, the M3 and M12 VR sessions now show their best shift at +2.0 s, next to their correlation peaks of +1.8 s and +1.7 s. The other counts are unchanged and the text still matches them.
- **File notes (C):** a new data-check cell prints the free-text notes and experiment description of one VR file and one open-arena file. They show the "only 200cm track" statement, the 4.7 cm/s stop speed measured over 100 ms, and the "100 x 100 cm open field". Both files are from M1, whose arena spans only about 70 cm.

Round 1 is now recorded under `verifications` in `attempts/000943-clark-2024-01.yaml`. For each claim it gives the verifier's reason and my response.

**Not done:**
- I did not run a timed MountainSort sort on one recording day. Reading the data alone already takes longer than the limit, so the sort could only add time and would not change any outcome.
- I kept `too_large` rather than switching to `data_missing`. The verifier itself called `too_large` defensible because the raw data are in the dandiset.

I did not commit anything, as instructed.
