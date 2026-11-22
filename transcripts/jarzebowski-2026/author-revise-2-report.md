No outcome changed. The round-2 verifier agreed with all 31 (22 reproduced, 4 partially reproduced, 5 not reproduced), and nothing needed a `proposed` change. I re-ran the entry twice with `python tools/entry.py all`; both runs passed with 0 errors, about 16 minutes each, and every number the conclusions cite came out the same.

**Text corrected to match the printed numbers**
- **figs1-post-omission-bursting:** the L2/3 p range under O9 (a) is now 0.0026 to 0.032 (it said 0.006), in the notebook and the record.
- **figs1-novel-firing-rate-unchanged:** the lowest p is now 0.00027 (it said 0.00025), in the notebook and the record.
- **fig5c-fsb-highest-on-first-repetition:**
  - `measured` is now the O9 (b) values, −0.0524 and −0.0548. O9 (b) is the only session reading under which cell-counts matches the paper.
  - The notes, the claim's conclusion and the Summary now give the margins under both O9 readings: 0.0002 to 0.0003 under O9 (b), up to 0.0012 under O9 (a).
  - They also state that the one passing O9 (b) reading codes repetition as k. Switching between k and k − 2 moves the L5 intercept by about 0.0018, six times that margin.
- **fig6b and fig6c (shared deviation and notebook text):**
  - I removed the argument that "the paper's n is every cell". It applies only to O5 (b); under O5 (a), block 1 leaves out only 4 and 15 cells (O9 a), or 1 and 9 (O9 b).
  - The text now says that "both blocks" is in effect block 3 (a median of 1155 block-3 windows per cell against 40 from block 1).
  - It also says the assumption is no better supported than block 1 alone, and that block 1 would reproduce neither claim. I kept the assumption because the verifier found it defensible.
- **Cell 0:** I removed the statement that the draft has the same asset count and size, because no output shows it.
- **README:** the run times now read four minutes (it said six) to run the claims on all 16 selections, and 15 to 25 minutes in total.

**Added**
- **New reader question** in `questions/jarzebowski-2026.yaml`: whether coding repetition as k fits fig5c-fsb-highest. Under that coding the intercept is extrapolated to repetition 0, not the drop from Repetition 1 to 2 that the claim states. The claim itself is unchanged.
- **Round 2 in the record:** the verifier's reasons in its own words and my responses, recorded under `verifications` for all 31 claims (agrees true). No finding is rated `critical`, so the round has no `findings` list. The verifier agreed with all four ratings, which I note under `reviewed`.

**Not done**
- The open questions on the spontaneous period (O5), the running definition for Figure 7, and the fig2a reading of "weaker" were already in the questions file, so I added nothing for them.
- The paper's model code and the legends of Figures S1 and S2 are still not available.

Nothing is committed, as instructed.
