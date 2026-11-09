**Verifier report, round 2: Welch et al. 2025 on DANDI:001863 (0.260806.2109)**

The claims file has 36 claims. The attempt record has 36 outcomes, one for each claim: 23 reproduced, 2 partially_reproduced, 2 not_reproduced and 9 blocked (data_missing). My round-1 tally ("24 reproduced… ") added up to 37 and was wrong; the outcomes in my round-1 table do add up to 23.

### 1. Outcomes and assumptions

- **I agree with all 36 outcomes.**
  - **fig3c and fig3d:** both are now not_reproduced. Cells 53 and 56 give signed-rank p = 0.063 and 0.079, and the criterion has no partial outcome.
  - **fig4supp:** now partially_reproduced, on reading (a). Cell 79: 11 of 13 mice have p < 0.001, which is at least the criterion's two thirds.
  - **Every other outcome** follows its criterion from the printed numbers. The numbers are unchanged from round 1.
- **The record marks two outcomes `assumed: true`. Both assumptions are stated, and both are reasonable.**
  - **fig4supp-ks-every-mouse, percentile exclusion applied per session.** The Methods quote the record gives does put the exclusion in the per-recording MATLAB step. The outcome would be the same under the code's computation, which applies no further exclusion (11 of 13). Only reading (b) gives 13 of 13. The question is also put to the authors.
  - **fig5ab-occupancy-similar, arena box from the pooled 0.5–99.5 percentile nose positions.** This is reasonable given that entropy p = 0.063 and the corner measures have p = 0.25 and 0.70. The record says plainly that other boxes were not run.
- **One place where the claims file misreads the paper** (reported, not corrected): fig1c. The paper's "higher… after the first 10 min, except for the 30–35 min bin" implies the 25–30 min bin is higher too. The criterion leaves that bin out of its requirements. It makes no difference to the outcome, since cell 24 gives p = 0.018 for that bin.

### 2. Sentences the printed outputs do not support

- **Attempt record, fig3supp-doi-iti-slower-than-odor, "Fitted clock -3.54 cm/s":** cell 62 prints −3.5697. Cell 63's "-3.5 cm/s" should round to −3.6.
- **Cell 13, "the code, which reads the field as thousandths, by up to 0.7 s":** this contradicts the record's finding ("shifting the HTR times by up to 0.9 s").
  - `htr_times` reads the field as FF/1000 where the true value is FF/80. With FF at most 79, the error is up to 0.91 s.
  - 0.7 s is only the code's error relative to the stored times, not to the true times.
- **Record finding, the stored times "are late or early by up to 0.2 s":** FF/100 is always below FF/80, so the stored times are always early.
- **Cell 101 and the fig5e note, the rate rises "to about 6.5 at the odor end":** cell 100 shows the rate peaks at 6.76 (x bin 800) and falls to 5.65 in the last bin (1100).
- **README, "a clock fitted to each session does" line the frames up:** cell 8 gives a good fit in only 30 of 44 sessions. The Summary states this caveat, but the README leaves it out.
- **Minor, attempt record:** only fig2a of the nine blocked Figure 2 outcomes has `notebook` and `output` fields.

All other "**Result:**" sentences, the Summary, the README table and the record's notes match the printed outputs. That includes the counts 16/22, 15/22, 19/22, 18/22, 21/22, 8 of 13 and 11/22, the fitted-clock p-values, 151 of 3057 HTRs within trials, 30 of 44 good fits, 10 mice with both fits good, 17 good DOI fits, the 311 s and 165 s video overruns, and the 21 or 22 of 22 HTR-peak sessions.

**My round-1 reasons in the record:** they are stated faithfully. Most are taken almost word for word from my round-1 table. Problems 3, 4 and 5 are folded correctly into the fig4supp, fig2a and fig5ab reasons, and problems 1, 2, 6 and 7 are in `reviewed`.

### 3. Round-1 points

**Resolved:**
- **2:** `r_signrank` now uses the normal approximation when a zero difference is present, as R does.
- **3:** fig4supp is now partially reproduced on a stated assumption, and the notes now say the medians are lower on DOI in 5 of the 13 mice.
- **4:** cell 39 lists the groups of all 44 files. No path names a port, poke, reward, lick, beam or drink, apart from the trial table's repoke column.
- **5:** acknowledged in the notes and kept as the claims file's reading.
- **6:** under the fitted clock, speed is now scaled by the fitted rate (cell 51).
- **7:** printed in cell 8 (11 of 22 mice, median difference −0.003).
- **From my "could not check" list:**
  - The sniff descriptions are now printed (cell 10).
  - Each fit's implied video span is printed, and the quality flag now uses it.
  - The HTR series is shown to be on the video clock at 80 frames/s (cell 14).

**Remaining, bearing on conclusions:**
- **Problem 1, which clock the trial table is on, is still open.** The new HTR check sharpens it.
  - HTR time t sits at frame t × 80 (cell 14), and the code compares t directly with trial times. So the code's split is right only if the trial table is on the frame/80 clock, which cell 8 contradicts.
  - This means the reproduced outcomes of fig5f and fig5supp-htr-within-trial-x-not-y probably come from the misaligned clock. Under the fitted clock fig5f reverses (p < 1e-4), and the within-trial x effect goes to p = 0.96.
  - The speed outcomes that split frames by period depend on the same unresolved clock.
  - The outcomes correctly follow the claims file's clock, and the record states this. Settling it needs the authors' answer, which is already asked in the record.
- **R parity is still unchecked**, both for the tests and for `clean_nose` against the authors' `CleanTracking`. This matters most for the two not_reproduced outcomes, whose p-values (0.063 and 0.079) are near the cut. A small difference in tracking cleaning could move them.
