**Verifier report, round 2: Yang (2026) on DANDI:000363**

The claims file has 25 claims. The attempt record has 25 outcomes: 16 reproduced and 9 partially reproduced, with none not reproduced or blocked. My round-1 opening sentence said "15 reproduced and 10 partially reproduced". That was my own miscount: my round-1 table gives 16 and 9, and the record's `verifications` copy that table correctly. Cell numbers below are those of the re-executed notebook. They differ from round 1; for example, the session counts are now in cell 13 and the decoding in cell 70.

### 1. Outcomes and assumptions

I agree with all 25 outcomes. The new runs change none of them:
- **Laser trials kept (M1 reading a):** cell 18 gives 5/5 joint fractions under the licks reading, 4/5 under the outcome reading, 10/10 axis fractions and both cosines within tolerance.
- **Decoding laser trials alone (M8 reading a):** cells 70 and 73 give 0–4 of 10 values within tolerance, and the Go-aligned criterion fails in every part.
- **Seed 17:** cells 27, 30, 41, 47, 50, 56, 59, 62, 65, 70 and 73 give the same outcome as the claim's seed everywhere except fig3c-late-residuals.
- **The fig1b rule under all eight readings:** cell 88 never selects the paper's session.

Two outcomes are marked `assumed: true`. Both assumptions are stated, as a deviation, in the notes and in the Result cell, and both are reasonable:
- **fig2d-choice-share-flat:** the partial clause is read with the criterion's own SEM rule. That rule is the only definition of "rise" the criterion gives. Cell 76 prints both counts: 4 regions not rising under the SEM rule, 3 counting any increase.
- **fig3-1c-alm-early-residual:** the early window is scored in two 50 ms bins. This rests on the Methods passages quoted in cell 58 and matches the paper's 12.6 ± 2.0 almost exactly. Cell 59 prints both readings (12.59 binned, 18.36 as one window).

fig3c-late-residuals is correctly kept at the claim's seed and flagged `seed_sensitive: true`.

### 2. Sentences the printed numbers do not support

1. **fig1b, wrong session named.** Cell 89 says: "the readings that drop trials without keypoints select ses-20210129T132207 and rank it 38th". The same claim appears in the attempt record's fig1b notes and in the `response` to my round-1 reason. Cell 88 shows the drop readings select ses-20201230T112558 under three readings and ses-20200925T153348 under one. ses-20210129T132207 appears in no output. The rank of 38 and the joint fraction of 0.0008–0.0009 belong to the paper's session, so "rank it" has the wrong referent. The outcome is not affected.
2. **fig1e, highest other region.** Cell 28 says "so is the highest of the other regions (midbrain, 7.6 to 8.8)", meaning within tolerance under every reading. Cell 27 prints "ratio a, independent: … highest within False" (7.56, against a lower bound of 7.83). The seed-17 run's a/disjoint value, 7.69, is also outside. The attempt record's "under three of four" is correct. The outcome is not affected.
3. **fig1-1c, pooled ρ range.** The attempt record says "pooled rho −0.366 to −0.423 over the eight readings". Cell 33 prints −0.366 to −0.428.
4. **Run time.** The README and cell 0 say "It takes about 40 minutes". Cell 94 prints "total run time 62.1 min".
5. **Two incomplete parentheticals, minor:**
   - fig2a: the attempt record's "(thalamus below 0.657)" and cell 74's "the thalamus 250 ms bin 0.63" omit that ALM, at 0.635 (cell 73), is also below 0.657.
   - fig2b: cell 83 and the attempt record list medulla and thalamus as outside 0.036–0.088 in the delay bins. Cell 82 also lists ALM at 0.035 in the overlapping bins.

Everything else checks against the printed outputs: all other Result cells, the Summary (cell 93), the rest of the README, and every other note and finding statement in the record.

**My round-1 reasons.** The `verifications` block states them faithfully and in my own words. Where problems 1–5 bear on a claim, they are folded into that claim's reason accurately. The record notes that cell numbers in the reasons are those of the round-1 copy.

### 3. Round-1 points

**Resolved:**
- Point 1: laser-only decoding is now run on the 26 entries, and the false markdown sentence is corrected (cell 67).
- Point 2: seed 17 is run as a variant and stated as a deviation. Cell 65 names the failing region: thalamus in the bin centred 375 ms.
- Point 4: the fig1b rule is now run under all eight readings, apart from the wrong session name above.
- Point 6: the M1 reading a results are added.
- Points 7, 8 and 10: each is now stated in the notebook (cells 67, 26 and 10).
- Point 9: the per-session trial counts are printed (cell 68).

**Remaining, bearing on a conclusion:**
- **fig3-1c-alm-early-residual (point 3):** reproduced only under the two-bin reading. The single 100 ms window the claims file's criterion implies gives 18.36 and would be partial. The claims file does not name this binning as open; this is a gap in the claims file, now asked of a reader.
- **fig2d-choice-share-flat (point 5):** partial only under the SEM-rule reading of the partial clause. Counting any increase as a rise gives not reproduced. This ambiguity is in the claims file, and it has been asked of a reader.
- **fig3c-late-residuals:** reproduced at the claim's seed and at +2000. It is partial at +1000, +3000, +4000 and at the paper's seed 17, where thalamus is 0.76–0.81 against a bound of 0.81. The outcome is protocol-correct and flagged, but it is fragile.
- **fig1b-example-session notes:** the wrong session name (section 2, item 1) should be corrected. The outcome stands.

### 4. Critical findings

No finding in the attempt record's `findings` is rated `critical`, and none should be. Finding 1, the data check (`severity: none`), is supported by cells 3, 5 and 8:
- no recording is duplicated;
- every photostimulation trial has one onset event;
- the ALM laser effect is present in 99 of 99 sessions, which ties spikes and trials to one clock;
- the tongue is detected in 97% of frames after a lick against 40% at shifted times, in 112 of 112 sessions, which ties licks and video to one clock.

The `minor` ratings of findings 2–5 are right: the unsorted spike times, the two region fields, the keypoints without a detection flag, and the video gaps in two sessions are each evident from the values or easy to work around.
