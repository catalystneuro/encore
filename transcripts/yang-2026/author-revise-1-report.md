No outcome changed in this round. The verifier agreed with all 25 outcomes (15 reproduced, 10 partially reproduced), and the new analyses it asked for confirm them. The final run passed (`python tools/entry.py all entries/yang-2026`: 0 errors, 41 minutes), and every conclusion matches its numbers. Nothing is committed.

**What changed in the outcomes**
- **fig2d-choice-share-flat** stays partially reproduced, but is now marked as resting on an assumption. I read the criterion's partial clause with the same SEM rule as its reproduced clause, and recorded that as a deviation. Counting any rise of the mean, only three regions don't rise and the outcome would be not reproduced. I added this as a question for a reader in `questions/yang-2026.yaml`.
- **fig3-1c-alm-early-residual** stays reproduced, resting on the two-50 ms-bin reading. The claims file reads the window as one 20 to 120 ms window and doesn't list the binning as open. I asked a reader about this in the same questions file and left the claim unchanged.

**What I added or corrected, by report point**
1. **Laser-only decoding (M8 reading a):** now run on the 26 entries that qualify, under all six seeds.
   - table1-decoding-early-vs-prelick: 0 of 10 values within tolerance under the claim's seed (1 to 4 under the others), so it stays partial.
   - fig2a fails every part on this reading and stays reproduced on reading (b), which the criterion allows.
   - The fig2d and fig2e session sets match less well with laser trials alone.
   - I corrected the false markdown sentence ("no entry passes the rule").
2. **Seed 17:** the paper's seed now runs as a variant for every random step.
   - It gives the same outcome as the claim's seed everywhere except fig3c-late-residuals (4 of 5 regions).
   - The failing region there is thalamus, in the bin centred 375 ms after Go: 0.76 to 0.81 against a lower bound of 0.81, at seeds +1000, +3000, +4000 and 17. That claim stays reproduced and marked seed-sensitive.
   - The seed deviation now says that NumPy's generator and draw order can't be the paper's, so seed 17 doesn't recreate its draws.
3. **fig3-1c window:** handled by the reader question above.
4. **fig1b example session:** the selection rule now runs under all eight readings. None selects ses-20200922T135318: it ranks 2nd or 3rd on the "fill" readings and 38th on the "drop" readings.
5. **fig2d rule:** the cell now prints both counts (with and without the SEM rule).
6. **Early-lick laser trials kept (M1 reading a):** the early joint, axis-fraction and cosine claims give the same outcomes under it.
7. **Z-scoring before cross-validation:** the notebook now says it uses control trials and no labels.
8. **fig1e columns:** the notebook now says the disjoint and independent columns are the same method on different draws, since no side is small.
9. **"67 / 36" statement:** bilateral and laser trials per session are now printed (median 36 bilateral, range 4 to 67).
10. **"Drop" reading:** the notebook now says it removes about 82% of control trials from the choice-axis fit itself.

I also added a fourth point (laser-only decoding) to the existing question-for-the-authors finding, updated the runtime in entry.yaml, the README and the header, and recorded round 1 under `verifications`. Each claim has the verifier's reason in its own words, its outcome and my response. Findings keep their order, and none was added.

**Not done**
- I didn't carry the early-lick-kept reading of M1 into the decoding and matching claims. It would roughly double those computations, and the verifier rated the point as not affecting a conclusion.
- There is no critical finding, so there was no critical-finding review to record for this round.
