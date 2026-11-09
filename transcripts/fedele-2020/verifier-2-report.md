# Round 2 verifier report: Fedele, Tzovara et al. 2020 on DANDI:000576 (0.231010.1811)

The claims file has 25 claims. The attempt record gives:
- 0 reproduced
- 4 partially reproduced: table2-delta-reduced-12-of-14, neuron-count, fig3b-firing-hgp-no-condition-difference, fig3d-firing-correlations-modalities
- 12 not reproduced
- 2 blocked because the methods are underspecified: fig1b-delta-decrease, fig1f-hgp-more-specific-than-delta
- 7 blocked because data are missing

The README and the Summary in cell 86 show the same outcomes.

## 1. Outcomes and assumptions

**Agree, no further comment:** fig1b-delta-decrease (blocked; the criterion says to block when readings disagree, and they hold in 6 of 12), fig1c-hgp-increase-first-2s, table2-mi-values, neuron-count, fig3a-firing-increase-aversive, fig3a-firing-gradual-sustained, fig3d-firing-correlations-modalities, and all 7 data_missing blocks.

**Agree, with notes:**

- **other-bands-no-effect** (not reproduced, `assumed: true`). The assumption is stated and reasonable: the paper's pipeline is one that also produces its delta result. The outcome hardly depends on it, because the criterion says "not reproduced when any [band] does". There are other-band clusters under `baseline` (both amygdala sets) and under `amygdala` (all 14) (cell 32).

- **fig3c-ssi-frv-correlation and fig4b-regression-firing-hgp** (not reproduced, `assumed: true`). The assumption is that SSI uses every other unit in the same amygdala, and it is stated and reasonable. Cell 77 shows that the units table records no microwire, and dropping the 4 pairs likely recorded on one wire changes nothing:
  - fig3c: r 0.24 and 0.35.
  - fig4b: the FRV coefficient has p ≥ 0.07 in every reading (cell 83).

- **The five other claims that rest on the MI values: fig1d-delta-hgp-mi-correlation, nsoz-delta-hgp-mi-inverse, table2-hgp-mi-positive-nsoz, fig1e-hgp-not-delta-distinguishes-soz, hgp-soz-sensitivity-specificity** (not reproduced), **and fig1f-hgp-more-specific-than-delta** (blocked).
  - I agree with the outcomes, but each one rests entirely on window (c). That window is the author's reading (0–2 s for HGP, 0–24 s for delta), not one from the claims file.
  - Windows (a) and (b) never define the HGP MIs these claims need (cells 43, 46, 52, 55, 58, 61).
  - Window (c) has support in Results 2.1 and Methods 4.11 ("HGP enhancement in the first 2 s"). But the paper defines the MI over "the interval where the two curves are significantly separated" (Table 2 legend).
  - This is stated in the deviations, but none of these six outcomes carries `assumed: true`. They should.

- **table2-delta-reduced-12-of-14** (partially reproduced).
  - I agree with the outcome. The criterion defines no partial outcome, so this is a judgement call.
  - The claim holds in every claims-file window reading that defines all 14 MIs: baseline a_nSOZ, baseline a_all14 and amygdala a_all14 (11, 11 and 12).
  - Its only failure is `trial` z-scoring with window (c), which gives 10 (cell 49). So this outcome also rests on window (c).

- **fig3b-firing-hgp-no-condition-difference** (partially reproduced).
  - The criterion offers only "reproduced" or "not reproduced". With 2 of 6 readings finding NEUTRAL > AVERSIVE (p 0.012 and 0.023, cell 74), "blocked (methods_underspecified)" would match how fig1b and fig1f are handled. It would also match the record's own methods_unavailable question about the time base.
  - Either outcome is defensible, but the record should say why partial was chosen over blocked.

## 2. Statements the numbers do not support

- **Cell 30:** "the previous epoch gives … an HGP cluster in the nSOZ amygdalae from 0.6 to 5.5 s (p = 0.002), the only reading here with an HGP cluster that begins in the first 2 s".
  - Cell 29 also shows `hgp allepochs trialsd nSOZ A>N 0.6 to 1.9 s p=0.028` and `hgp prevepoch trialsd nSOZ A>N 0.5 to 8.4 s p=0.002`.
  - The first of these is a cluster entirely inside the paper's 0–2 s window.
  - The fig1c notes in the record mention only the prevepoch/amygdala case. They are variants, so the outcome stands, but the sentence is wrong and the record leaves the cluster out.

- **Cell 6 ("The `location` of four channels does not name the amygdala") and Cell 86 ("four channel locations name the hippocampus or are unknown").** Cell 5 lists five channels: 1 AR, 5 AR, 9 AR, 6 AL and 6 AR.

- **Cell 65:** "as only units above 1 Hz were deposited". Cell 64 shows 2 units at 0.88 Hz over the 442 s. The record's wording, "above about 1 Hz", is correct.

- **Cell 86:** the within-patient model "equals" the paper's mixed model. Cell 16 shows the β values identical but t differing slightly (−2.594 against −2.611). The record's phrase "same condition estimate" is accurate.

- **Record, table2-mi-values notes:** "Re-mapping … does not bring the values closer (0 to 4 within tolerance)". This holds for the claims-file z-scorings. The trialsd variant goes from 6 to 7 under the subject 7 → 8 L/5 R mapping (cell 38). This is minor.

- **README:** "It takes about six minutes". Cell 87 prints 4.1 min. This is minor.

Every other sentence of the **Result:** cells (22, 27, 33, 36, 44, 47, 50, 53, 56, 59, 62, 65, 69, 72, 75, 78, 81, 84), the Summary, the README and the record's notes matches the printed outputs.

**My round-1 reasons in the record:** they are stated in my own words, condensed. The six BOLD-claim entries share one reason, which drops my fig4d remark that only the firing-HGP axis exists. "20 agree" is correct: 5 entries have `agrees: false`.

## 3. Round-1 points

**Resolved:**
- 1 (outcomes judged on an adopted reading): none are now.
- 2 (unstable `baseline` SD): the `baselinepool` variant and the autocorrelation check are added.
- 4 (SSI microwire): checked; no microwire is recorded, and a variant drops the 4 likely same-wire pairs.
- 5 (smoothing mixed blocks): smoothing is now per block, and the difference persists.
- 6 (`trialsd`): it no longer enters any count.
- 7 (patient mapping): re-mappings are tested.
- 8 (CIs): other interval methods are printed, and the question goes into the questions file.
- 12 (Table 2's own DELTA p): recorded as a paper_inconsistency.

Every item from my "Not checked" list is now addressed: per-amygdala 2 s tables, per-block concatenation for fig3b, the other Methods 4.8 baselines, per-unit rates and PSTH, and the patient mapping. Points 9 and 10 did not bear on a conclusion and still stand as they were.

**Remaining, bearing on conclusions:**
1. **Window (c).** MIs are now left undefined rather than set to 0, but window (c), the author's reading, is the only basis for 6 MI-claim outcomes and the only failing reading for table2-delta-reduced-12-of-14. They should be marked `assumed: true`, or else blocked on the MI-window question the record already asks.
2. **fig3b outcome category.** Partial versus blocked when the readings disagree, as set out in section 1.
3. **Cell 30 misstatement.** It understates the variant results: two variants (allepochs/trialsd 0.6–1.9 s and prevepoch/trialsd 0.5–8.4 s, both nSOZ) give an HGP cluster in the first 2 s. This does not change fig1c, but it bears on the record's z-scoring/baseline question to the authors.

The claims file: I found no new misreading of the paper beyond round-1 points 8 and 12, which are now recorded.
