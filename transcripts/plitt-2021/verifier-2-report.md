**Verifier report, round 2: Plitt & Giocomo 2021 on DANDI:000054 (0.260415.1712)**

The claims file holds 29 claims. The attempt record gives 29 outcomes: 13 reproduced, 4 partially reproduced, 10 not reproduced and 2 blocked. These are the same as my round-1 outcomes, one for one. Neither file sets `assumed: true` anywhere.

### 1. Outcomes

I agree with 28 of the 29 outcomes. The exception is fig7g.

- **fig7g-model-prior-reconstruction: I disagree with `partially_reproduced`, and I am withdrawing my own round-1 judgement.**
  - The criterion names no partial outcome. It says "Reproduced when [signs] … and its magnitude is below the neural across-mouse mean magnitude … in both conditions."
  - As written it passes. The model values are −0.098 and 0.626 bits, both of the expected sign. Their magnitudes are below the neural 0.223 and 1.125 (nb2 cell 51).
  - For four other claims (session counts, fig2eh, edf7, edf9l) the attempt applies the rule that a criterion naming no partial outcome cannot give one. Applied consistently, fig7g is **reproduced**.
  - The caveat belongs in the notes: the rare neural yardstick (+0.223) has the wrong sign, so "less closely matched than neural" means little for the rare condition.
- **fig6d (not reproduced) and edf10 (reproduced)** follow the criterion. The ideal-observer check (nb2 cell 35) shows the criterion's formula cannot give the rare sign on this design: an ideal rare observer gets +0.547. So fig6d's failure says nothing either way about the paper.
  - The claims file follows the Methods text (I checked the Methods passage), so it does not misread the paper.
  - It does say this R is computed "as the code computes it (SFReg, prior_post_reconstruction)". The attempt's code_mismatch finding says the code takes Z at f instead. I cannot check the code, but if the attempt is right, that attribution is wrong.
  - edf10's reading (b) also holds under the code's computation (0.433 to 0.627 against the ideal observers' 0.047 rare and 0.502 frequent), so its outcome is safe.
- **No outcome is flagged `assumed: true`.** The main assumption left unflagged is that file day equals the paper's session number (edf7, edf9). It is now argued from the deposit (nb2 cell 6). Under the date-ordinal numbering, R1 to R4's and R6's named sessions would fall on dates that have no imaging file, so the file-day reading is reasonable.

### 2. Text against the printed outputs

These statements are not supported by the outputs:

- **nb1 cell 38 (edf5 conclusion).** It says classification "beats every shuffle in 17 of the 20 clusters against 100 shuffles". Cell 36 prints "significant clusters: 16 of 20 against 100 shuffles". The `sig 100` column has four False values.
  - "Accuracies are 0.519 to 0.708" does not match the printed 0.524 to 0.701.
  - "balanced accuracy 0.380 to 0.711 (median 0.560), above 0.5 in 15 of 20" does not match the printed "0.381 to 0.714, median 0.557; above 0.5 in 14 of 20".
  - The attempt-record notes for edf5 repeat the same stale numbers. The outcome is unaffected, since 16 of 20 is still "most", but the text was written against an earlier run.
- **nb1 cell 34 and the edf6 record notes.** They say "F5 (3.399, from a session at 12.262 …)"; cell 33 prints F5 3.4 and 12.266.
- **The record's findings, kind other.** It says the 26 unmatched imaging-flag files include "12 of them R6's, on dates before its session 8". nb2 cell 5 lists R6 dates 10_02_2020 and 11_02_2020, which come after its session 8 (09_02_2020).
- **nb1 cell 9.** It says the clocks are consistent "in every session, to within about half a second". Cell 6 prints three sessions whose maximum lies at ±15 frames, about 1 s.
- **nb2 cell 13.** It cites 3.5% intermediate "(part 1)"; the figure is computed in part 2, cell 9.
- **Questions to a reader.** The record and notebooks cite them as `questions/plitt-2021.yaml` (nb1 cell 15, nb2 cell 36) and `questions/000054.yaml` (nb2 cell 0). The two names disagree, the file is not among my materials, and the record has no questions field, so I could not check them.

Everything else checks out against the printed numbers: every other "**Result:" paragraph, the Summary (nb2 cell 56), the README table and the README text, and the other record notes. README timings are approximate: about 30 min against a printed 33.7, and about 18 min against a printed 15.6.

The record's round-1 reasons state my reasons accurately and in my words. The fig6d and edf7 reasons fold in the substance of my problems B1 and B3.

### 3. Round-1 points

**Resolved:**
- **B1 (prior reconstruction).** The ideal-observer check was run, the code's computation was shown as a variant, and a finding was raised.
- **B2 (place cells).** The 95th-percentile signal leaves 99.91% of decisions unchanged, and the numba shuffle matches a plain numpy version in 500 of 500 entries. The M2 misreading is raised as a question and makes no difference here.
- **B3 (session mapping).** R5's day-8 file is its 8th date under either numbering.
- **B4 to B10**:
  - B4: clipped and median step shares added.
  - B5: the 2020 code's session selection was rebuilt; it does not identify the two extra rare sessions.
  - B6: edf9k/l were run under all three likelihoods.
  - B7: the unsmoothed fig2eh variant was run.
  - B8: the fig7 stimulus-range statement is raised as a question.
  - B9: the session listing is fixed and dropped asset paths are now counted (0).
  - B10: the edf4bc notes now say reference (b) includes the overlap cells.
- **C items**: the decision-mouse table and leave-one-mouse-out classification are in.

**Remaining, where it bears on a conclusion:**
1. **fig7g's outcome label.** It is inconsistent with the "no partial outcome named" rule (section 1); I recommend reproduced, with the caveat in the notes.
2. **edf5's conclusion and record notes** quote a different run's numbers and need refreshing.
   - Leave-one-mouse-out beats the mouse relabelings in only 5 of 20 clusters. So the separation may partly reflect which mouse a cell came from. That should stay in the notes, although the criterion does not judge it.
3. **fig6d, edf10 (b) and fig7g** rest on a criterion formula that cannot give the rare sign on this design. Whether the claim should follow the code is still an open question to a reader.
4. **The place-cell excess (about 60% above the paper) is still unexplained.** It sets the magnitudes in place-cell-fractions, edf4a-overlap and the edf4bc counts. The outcomes are stated correctly.
5. **edf7's single failing session (R5 session 8) is one of the R5 files replaced in this version**, with no release notes (record finding). Whether the replacement changed its content cannot be settled from these materials.
