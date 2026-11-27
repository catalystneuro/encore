I re-read the notebooks, the attempt record, the claims file and my round-1 report, and checked them against each other.

## 1. Outcomes

The claims file and the attempt record each list 29 claims, with one outcome per claim.

**I agree with 28 of the 29 outcomes. One needs a caveat.**

- **Blocked (4):** fig1f, mixing-model-accuracy, ed2e and ed2-maze-lunar. I agree.
- **Reproduced:** link, fig2b, fig2c, fig2f, fig2g, fig2k-decoded, ed6e, ed5, fig3-common-value-fit, ed7c, ed7de, ed8cd, fig4a and fig4b. I agree. ed6e rests on the Methods baseline, which the claims file names as the main reading.
- **Partially reproduced:** fig2k-better, ed5g, fig3b and ed8ej. I agree.
- **ed3f and ed8b (partially reproduced):** I now agree. Neither criterion has a partial clause. The effects are strongly positive and significant but below tolerance. That is how fig2k-better was treated, and I accepted that one in round 1.
- **ed10 (partially reproduced):** I agree. With shared permutations, 9.375 s fails at the claim's seed: p = 0.098 under the Methods baseline (6 of 20 draws pass) and 0.83 under the code's baseline (cued notebook cell 57).
- **ed9g (partially reproduced):** I agree. rho = 0.743 is far below 0.837. In addition, 17 of 91 neurons sit at the γ lower bound, and the mean γ is 0.218 against 0.446 for the common value model (reward expectation notebook cell 5). The gap may come partly from the substitute fit and not the data. The record states the optimiser deviation.
- **ed6g (not reproduced):** I agree. The test agrees with the paper at only 2 delays. Over 10 simulated data sets, none agrees at all four delays (cell 45).
- **session-trial-counts (partially reproduced):** I agree, given the 78-neuron reading. The cued delay session count is 44 under reading (a) and 32 under reading (b), both outside 36 ± 3.6 (cell 48). On the deposited files alone, reading (a) passes (39 sessions).
- **cued-delay-neurons (reproduced, assumed):** I agree only with a caveat. The assumption is stated and checked: table rates against spike counts give a median correlation of 0.987 (cell 13). But the claims file allows the Mendeley flags only as labels, "where they can be matched" to deposited units. The 11 added neurons match no deposited unit, and 5 of the 48 selected neurons are table-only. On the deposited data the result would be partially reproduced (43 selected).

**Assumptions (`assumed: true`):** each one states its assumption.
- The iteration cap is reasonable, and the record shows its effect. It moves the results for ed8b and ed9g. For the claims of absence (ed7c, ed7de, ed8cd) the cap does not matter.
- The table-unit assumption is the scope stretch described under cued-delay-neurons.

## 2. Sentences the printed outputs do not support

- **Attempt record, notes of fig1f** (also cited by ed2e and ed2-maze-lunar): "The run's five hours went to the 23 claims on recorded data, which needed about 70 minutes of computing in their final run alone."
  - 25 outcomes are now on recorded data (24 paper claims plus the link).
  - The printed timings add up to well over 70 minutes. For example, vr_single_mouse alone is about 1950 s (cell 3 at 227 s plus cell 5 at 1610 s, plus loading). The README gives about 105 minutes.
  - This sentence dates from round 1.
- **Cued notebook cell 37:** "better than the hyperbolic one at 1.5, 3.75 and 9.375 s under every reading (p at most 0.0095)". This holds at the claim's seed only. Under seed +2000 the code baseline gives p = 0.982 at 9.375 s (cell 36). The sentence should say "under the claim's seed". The record states this correctly.
- **Attempt record, finding 1:** "nothing in the files or the dandiset's description says so". No printed output checks this. Neither session IDs, start times nor descriptions of the duplicate pairs are compared (see section 4).

Everything else matches the printed outputs: every "**Result:**" conclusion, the three Summary sections, the README table and data note, and the other outcome notes in the attempt record.

**My round-1 reasons in the record:** they are transcribed faithfully, with my numbered problems folded into the matching claims. One gap: problem 5 (the code's half splits share a trial, while this attempt's are disjoint) does not appear in any of my restated reasons. It does appear as a deviation and as a code_mismatch finding.

## 3. Round-1 points

**Resolved:**
- **Point 1 (ed8ej gains):** the like-for-like comparison was run and the m3044 gain is still below (0.698 and 0.674). The code citation is the author's; I cannot see the MATLAB code.
- **Point 2 (decoding readings):** the readings now share permutations and 20 draws are made, for ed10, ed5g and fig2k.
- **Point 3 (missing cued delay units):** addressed with the table units. The scope caveat from section 1 remains.
- **Point 4 (ed6g):** 10 simulated data sets were drawn.
- **Points 5 to 12:** addressed:
  - 5: stated as a deviation and finding.
  - 6: now an assumption, with its effect shown.
  - 7: a z-score variant was added.
  - 8: ed9g was fitted.
  - 9 and 10: code fixed.
  - 11 and 12: noted.
- **Opto-tag question:** now finding 4.

**Remaining, bearing on a conclusion:**
- **cued-delay-neurons, session-trial-counts:** both outcomes depend on using unmatched table rows as data, which goes beyond the claims file's labels-only allowance.
- **ed8b:** r depends on how far the fits converge. On the 20-fit subset, 30,000 iterations give 0.732, inside the 0.729 bound, against 0.718 at 10,000. The full 200-fit run was not done at 30,000.
- **ed9g:** the 17 neurons at the lower bound and the halved mean γ suggest a fitting difference. Partially and not reproduced cannot be told apart without the paper's fmincon fits.
- **Seed-sensitive outcomes:** ed5g, ed10, ed8ej, fig4b and session-trial-counts would change under other seeds. They are flagged correctly.

## 4. Critical findings

Only finding 1 is rated `critical`: "78 open-loop units are deposited twice…"

- **Do the outputs show it?** Yes, in vr_population cell 4: "257 distinct spike trains in 336 files; 78 deposited more than once". All 78 SU-VR-ALL-OL files share a spike train with an SU-VR-OL file under another session number: 77 pairs, plus one group that also includes SU-VR-ALL-TP-3. The example pair sub-3014 ALL-OL-1 / OL-2 is printed. The match is on an exact hash of the spike times (`multiscale.py:104`).
- **Not shown:** that nothing in the files says so. Session IDs, start times and descriptions of the pairs are not compared.
- **Rating:** `critical` is right. A unit deposited as two with nothing linking the copies is the defining case, and counting all single-unit files double-counts 78 units.

The other data findings are rated major or minor. I would lower finding 2 (the teleport session filed as open loop) from major to minor: the trial table shows it (cell 4), and it is easy to drop.
