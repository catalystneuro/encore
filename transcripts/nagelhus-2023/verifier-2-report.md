**Round 2 verification: Nagelhus et al. 2023 (Neuron) on EBRAINS Q0FG-1X8 v1**

The attempt record has 57 outcomes, matching the 57 claims in the claims file: 30 reproduced, 5 partially reproduced, 9 not reproduced and 13 blocked (8 `methods_underspecified`, 5 `data_missing`). I did not download the data or re-run anything. I checked the record and notebooks against the printed outputs, the claims file, the paper text and the code of `objcode.py`/nb06 c4.

### 1. Stated outcomes

**I agree with 56 of the 57 outcomes. The one I disagree with is figs4-object-traces.**

- **figs4-object-traces (partially_reproduced): I disagree and would record not_reproduced.**
  - The claim's main quantity is the trace fraction. It is 0.061–0.098 against 0.183 ± 0.018 under every field, ROI and rate-overlap reading, less than half the paper's value (nb02 c12).
  - Being above the 1% chance level, and the NO–NO′ count falling within tolerance, do not make up for that.
  - This is not like fig1c, where the miss is within sampling error.
- **Where I now agree after disagreeing in round 1:**
  - **fig1c (partially_reproduced):** the CA1 fraction is within tolerance and significant. The control count of 9/219 cannot be told apart from the paper's 11/219 (binomial p = 0.64, nb01 c24); a ±10% tolerance on 11 cells is tighter than sampling noise.
  - **fig1d (partially_reproduced):** the mean (8 of 12 readings) and the coverage of all sectors hold. The range fails, but only on 2–19 cells (nb01 c29).
  - **fig7-single-cell-properties (partially_reproduced):** three of the four correlations are within tolerance over the 1,189 cells. Only spatial information misses (nb04 c17).
  - **fig1e and fig7-slope-variant (now not_reproduced):** the author changed these to my round-1 outcome.
  - **figs7e (reproduced):** the corrected selection in nb06 c4 picks the top c words once, over both trials, in each session and distance bin. That removes the label leak. All 80 of 80 pairs have words higher, W = 0 (c24).
  - **figs5d:** now `data_missing`, as I gave.
- **The 8 `methods_underspecified` blocks** are fig2d-rate-overlap, figs3f, figs2d, ovs-method-extra-cells, fig4e, figs5e, fig6c and fig6d. I accept them under the rule the record cites: a claim is blocked when readings the claims file leaves open give different outcomes.
  - Each criterion's "under one reading" clause covers only that criterion's own readings, never the shared speed or rate-overlap readings. So the record is consistent with fig1c/1d/1e being judged "under one reading".
  - For ovs, blocking is better than my round-1 "reproduced (fragile)": the pass rests on an exclusion rule that the claims file does not give.
- **figs6hij (blocked, `data_missing`):** I accept this. The third test cannot be run, so whether the whole criterion holds cannot be decided.
- **All other outcomes:** I agree, as in round 1.

### 2. Sentences against the printed numbers

Every number I checked in the "**Result:**" cells, the six Summary sections, the README and the record's notes matches the printed outputs. That includes the tallies, ranges, p bounds, per-rat figures and variant results. The README counts (30/5/9/13, 8 of them reading splits) agree with the record.

Three sentences are loose rather than wrong:
- **nb01 c59, and the figs3f note:** "All four spatial-correlation tests … p ≤ 1.6e-6". This is true, but the largest printed p is 1.37e-6 (NO–NO′). 1.6e-8 is the NO–O value, so the bound looks miscopied.
- **nb05 c13:** "The mean difference rises and the mean slope falls with size". The trends are not monotone. In the tetrode sessions the difference is 0.200 at 30 cells against 0.176 at the full count, which the cell does acknowledge. In the 135-cell session with speed filter (a), the slope is −0.0508 at 30 cells against −0.0495 at 50 (c12).
- **figs7e note, "c … 5 to 16":** that range is printed only for subset reading (a) (nb06 c24).

**My round-1 reasons in the record:** the `verifications` block states my reasons faithfully, including the B and C points. My "B"/"C" findings (B = problems, C = checks I could not make) are folded into the matching claims. Nothing is misattributed.

### 3. Round-1 points

**Resolved:**
- **B1 (figs7e leak):** fixed and re-run; the old selection is shown as a variant.
- **B2 (figs2c):** the analysis is shown as a variant and a question is filed.
- **B4 (ovs):** now blocked.
- **B5 (shuffled accuracy):** the caveat is now noted in nb03 c37.
- **B6 (outcomes depending on readings, few subsets):** handled by blocking, plus a variant with 100 subsets per size.
- **B12 (CA3 session 3):** results without that session are now given.
- **B13:** confirmed.
- **All of section C:**
  - the occupancy decoder's per-session accuracies and a NO-half against NO-half control;
  - per-session CA3 counts;
  - the distance tail for fig1d;
  - 100 subsets per size for fig6c;
  - the struct field listing, which now confirms there is no head direction.

**Remaining issues that bear on a conclusion:**
1. **figs4-object-traces outcome:** see section 1. I would record not_reproduced.
2. **Field detection (B7) is still not the Methods' contour-from-peak method.** The edge-connectivity variant does not test that. The failures of fig1d (the range tail of 1–7% of cells), fig1e and figs4 (the trace fraction) may depend on it.
3. **figs6-behaviour-decoders-flat:** the control shows the occupancy decoder's dependence on distance appears without any object (H = 25.6, p = 3.8e-5, nb03 c46). The not_reproduced outcome therefore may reflect this implementation, as the record says, rather than the paper's result.
4. **CA3 has 341 cells against the paper's 313 (B3).** The paper's 313 cannot be identified. figs3a's not_reproduced rests on all 341 cells. For figs3f, two of the four spatial tests are not significant with tetrode cells only.
5. **figs2d rests on about half the paper's trace cells (B9).** It is blocked now, but this matters if the width question is settled.
6. **Claims-file misreadings, reported and not corrected:**
   - **figs7e:** the criterion says "per session and distance bin", but the Methods say "In a given trial, … kept the c words with the largest frequencies" (paper txt l.2065). The literal reading leaks the label, so the claims file's reading is the workable one, but it departs from the paper.
   - **figs2c:** the claims file says the claim needs the implant sites. It does not note that the Supplementary Figure 2C legend gives the order of the cell counts, so the test is partly possible without them.
