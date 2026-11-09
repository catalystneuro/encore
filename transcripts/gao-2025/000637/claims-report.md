I wrote `claims/000637/10.1523-jneurosci.2218-24.2025.yaml`. The quote checker passes: 31 claims, 31 quotes, 84 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record from PubMed Central (PMC12139594), with Methods, Results, figure legends and Discussion. The paper has no supplement and no PDF was supplied. It links no code, so no code was read.

**Counts:**
- **Quotes:** all 31 claims have one, so none needed an `inferred` note.
- **Statistics:** 28 claims carry them.
- **Criteria:** all 31 have one.
- **Expected values:** 9 claims have them. These are unit counts with a 10% tolerance, and mean normalized rates with the paper's stated SEM as the tolerance.
- **Scope:** the claims cover Figures 4 to 11: spiking responses in S1, POm and auditory cortex across PRF and duty-cycle series, sham and CG1 control (absence claims judged on the paper's test), and the correlation analyses (dSTTC and STTC).

**Shared methods:** the opening comment defines three shared methods, which the criteria refer to by name. Method S covers spiking, Method D directional correlation (dSTTC) and Method T plain correlation (STTC). Each part is cited to the Methods, Results or legends.

**Details the paper leaves open, and the readings named:**
- **Cell-type clustering:** k-means over the units of one area pooled across sessions (K1), or over all areas pooled (K2).
- **Normalized rate:** the ratio of summed counts in the window to summed counts before stimulation (N1), or the mean of per-trial ratios (N2).
- **The "two-sample Wilcoxon" test against baseline:** rank-sum (W1) or paired signed-rank (W2).
- **Bonferroni count:** comparisons with baseline only (M1), or all pairs (M2). I took the reported p-values as already corrected, since several are printed as 1.0.
- **Windows:**
  - Fig. 4 post-sonication from 134 ms: 134–201 ms or 201–268 ms.
  - POm at 30 Hz: 134–201, 201–268, or the whole of 134–268 ms.
  - Fig. 10A post-sonication: each 67 ms window from 67 to 268 ms.
- **dSTTC formula:** the equation is lost from the text. I wrote it in the Cutts & Eglen STTC form, built from the terms the text defines.
- **Normalized dSTTC:** the difference from pre-stimulus (D1) or that difference divided by the pre-stimulus value (D2). The 67 ms windows, with time fractions taken inside the window, are also my reading.
- **Inconsistencies in the paper:**
  - "Higher than 1,500 Hz" for S1 FSUs: read as 3000 and 4500 Hz, or as 1500 Hz and above.
  - For POm RSUs the same phrase sits beside "highest at 1500 Hz": I took 1500 Hz and above, with 3000 and 4500 Hz as a variant.
  - Fig. 7C lists 6% under "higher than 6%", and one entry (n = 7) has no duty cycle; by its position I read it as 30%.
  - The Fig. 11C AC-to-S1 correlation is said to last about 150 ms (legend) and about 200 ms (Results).
  - AC-to-S1 FSU is said to decrease (legend) and to show the same synchronization (Results). This part is reported and does not decide the claim.
  - The duty cycle used with each PRF in the Fig. 11 auditory series is not given: the 200 µs pulse-duration series or the 60% duty-cycle series.
- **Fig. 9A:** the direction of the 30 Hz difference is not stated, so both tails are reported.

**Missing from the paper:**
- **dSTTC equation:** absent from the text, and there was no PDF to read it from. Supplying the PDF would settle the formula used by claims fig10a, fig10b, fig11c and fig11d.
- **Analysis code:** none is linked, so nothing in the Methods could be settled from code.
- **Data location:** the paper says all its data are in DANDI:000946, not 000637. The 000637 description lists S1 recordings only, with pulse durations of 100, 200 and 400 µs. The POm, auditory cortex, sham, CG1 and duty-cycle claims may therefore not be testable on this dandiset; finding out is the author's job, and the opening comment says so.
