**Verifier report: Grosmark & Buzsáki 2016 (doi:10.1126/science.aad1935), round 2**

The claims file has 36 claims and the attempt record has 36 outcomes. All 36 are tested this round, including figs11, which was blocked in round 1. Cell numbers below are those of the re-executed notebook.

### 1. Outcomes and assumptions

I agree with 33 of the 36 outcomes. I disagree with two (fig4e, figs16de) and agree with one (fig2d) only if reading Y-a is accepted. Every outcome except sessions-and-tracks has `assumed: true`, and each one states the assumption it rests on. The assumptions are reasonable, with these qualifications:

- **fig4e-gain-sequences (partially_reproduced): I disagree.** Its criterion has no partial outcome. It is reproduced only when the low-gain group does not rise, and in cell 106 the low-gain group rises under 5 of 6 readings (main reading p 0.0163, interval 0.0061 to 0.0568). Round 2 changed place-cell-count, rigid-plastic-counts, figs16ab and fig4c-slow-replay to not_reproduced for the same reason ("the criterion has no partial outcome"). By that rule this one is not_reproduced, unless "As fig4d-slow-sequences" is read as carrying over fig4d's partial clause. I agreed with partially_reproduced in round 1, and that was my mistake.
- **figs16de-more-ripples-post (partially_reproduced): I disagree, for the same reason.** The criterion has no partial outcome, and the ripple-event medians (2.424 and 1.944 s against 3 and 2.47 s, cell 91) are outside tolerance. So the outcome is not_reproduced. I also agreed with this one in round 1.
- **fig2d-shuffle-high-dpcc (reproduced): I agree only if Y-a is accepted.** The criterion asks for the result under all readings of Y and D with one reading of "eliminated" (cell 55):
  - Under reading (a), Y-c with D-b eliminates replay at 5%.
  - Under reading (b), replay is eliminated at 5% under all six readings.
  - The pass therefore rests on adopting Y-a, which is stated. Y-a has no more support from the text than Y-b. Choosing it also decides figs5e: under Y-b with L-a and S-a the test gives p 0.455 with medians within tolerance.
- **D-a against D-b.** This is a stated assumption, and the Methods' quote supports it. It cuts both ways, and the record says so: D-b would make rigid-plastic-counts reproduced, fig2b partially reproduced, fig2-pre-post-overlap not reproduced and figs16ab reproduced.
- **place-cell-count.** Not_reproduced is correct under the claims file's reading of the kernel as its SD. Something to report about the claims file: it says the SD-or-width choice "should not change outcomes", and cell 17 shows that it does (573 against 507, the latter within tolerance).
- **figs11-cluster-quality-similar (reproduced).** I accept the outcome, with a caveat about the measure's power. Centre and covariance come from the unit's own spikes, so the median Mahalanobis distance is close to √(feature dimension) by construction: medians are 5.4–5.7 with 24–30 PCA columns (cell 110). This is a claim of absence tested on a measure with little room to differ. The record names the covariance as an assumption but does not mention this. The claim's waveform part is not tested, which the record states and the criterion does not require.

### 2. Sentences the outputs do not support

- **Record, fig4a-rigid-faster notes:** "By session the rigid median exceeds the plastic one in 6 of 8 sessions (reading b, D-a)." Cell 64 shows rigid above plastic in 5 of 8; Buddy, Cicero_09012014 and Gatsby_08282013 go the other way.
- **Record, figs5e notes:** "the other readings give p 0.0419 or less". Cell 33 shows Y-b, L-b, S-b at p 0.116. Four readings are not significant, not three. For the same reason, "The yoking reading decides the test" overstates it.
- **Record and cell 107, fig4d:** "main reading 0.0458, bootstrap interval 0.0156 to 0.0766, rank-sum … p 0.00682; 0.0508 to 0.0764 under the others". Cell 106 prints 0.046, 0.0158 to 0.0768, p 0.00658, and 0.0511 to 0.0767. Cell 107's "up to 0.0764 under Y-c with D-b" should be 0.0767.
- **Record and cell 60, fig2e:** "interval -0.0538 to -0.00969" and "D-b groups -0.0572". Cell 59 prints -0.00964 and -0.0568.
- **Record, figs11 notes and response:** "streamed … (196 s, four at a time)". Cell 110 prints "8 tarballs streamed in 142 s".
- **fig1c-post-gt-pre (record and cell 26):** gives the interval as 0.0078 to 0.0127, while figs5b (cell 30) gives 0.0078 to 0.0125 for the same quantity. Both values are printed, from different draws, so this is a minor inconsistency.

All other sentences I checked match the outputs. That covers the remaining "**Result:" cells, the Summary (cell 112), the README and the rest of the record's notes. The README's 18 rows cover all 36 claims.

**My round-1 reasons in the record.** They are given in my words, close to verbatim, with my B-points paraphrased fairly in parentheses. Two remarks:
- figs11 is recorded as `agrees: true, outcome: blocked`. In round 1 I said the claim was testable, so `agrees: false` is closer to what I meant.
- The cell numbers in my reasons are those of the round-1 notebook, and the record does not say so.

### 3. Round-1 points

**Resolved:**
- **B1:** D-b groups are shown for every split claim.
- **B2:** the reruns use all six Y and D readings.
- **B3:** fig2d now averages 100 shuffled templates, and the question is put to the authors.
- **B4:** Buddy_06272013 was rescored with 1,000 of each: rZ r 0.996, PCC r 0.995, 40 of 41 strongly contributing labels kept (cell 41).
- **B5:** the kernel and 1 Hz variants were run (cell 17).
- **B6:** figs11 was tested (cell 110).
- **B7:** all three session-rate readings were run (cell 98).
- **B8, B9, B11, B12:** resolved; the dead loop is gone.
- **B10:** left unchanged, which is acceptable.
- **Section C:** everything is covered except the comparison with MATLAB's `multcompare`, and that is acknowledged.

**Remaining points that bear on a conclusion:**
1. **The kernel reading is not carried downstream.** Every later claim uses the 573-unit set of the SD reading. Under the width reading (507 units), the D-a counts for fig2b (246) and rigid-plastic (120/120) would likely move toward tolerance: scaled by 507/573 they are about 218 and 106. So the D-a against D-b conclusion is confounded with the kernel reading, and that was not run.
2. **fig4e and figs16de** should be not_reproduced by the record's own rule (section 1).
3. **fig2d** passes only under Y-a and eliminated-reading (a) (section 1).
4. **figs11's quality measure** is close to fixed by the feature dimension (section 1).
5. **Five claims rest on a single assumption, and the outcome flips under the alternative:**
   - figs5e on Y-a;
   - fig4c-pre-fast and fig4c-slow-replay on sess_c;
   - fig2b and figs16ab on D-a.

   All five are stated as assumptions, but readers should know the outcomes hinge on them.

### 4. Critical findings

No finding is rated `critical`.

- **Finding 1** (`none`): cell 6 shows the identical units, spikes and states it describes.
- **Finding 2** (Gatsby_08022013 continues after the stated POST end, `minor`): cell 11 shows it, and minor is the right rating because the overrun is evident from the spike times.
- **Finding 3** (39.06 Hz position sampling, `minor`): cell 12 shows it.
- **Finding 4** (`minor`): it names cell 12, which shows the 1D range of 0 to 2.84–2.90 m. The absence of directions in the circular-track trials appears in cell 78, not cell 12.
- **Finding 5** (`minor`): it names no notebook cell.
- **Finding 13** (`none`): cell 110 shows it.

I would not raise any of them to critical.
