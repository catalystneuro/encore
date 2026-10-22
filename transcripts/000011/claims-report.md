I wrote `claims/000011/10.1038-nature17643.yaml`, with 38 claims. The quote checker reports 38 claims, 38 quotes, 11 statistical values and 0 problems. Nothing is committed.

**Text read:** the HHMI author manuscript (PMC5081260, served by Europe PMC), not the version of record. It has the main text, Methods, and the legends of Figures 1 to 6 and Extended Data Figures 1 to 10. The paper has no supplement beyond the Extended Data, so nothing the results rest on is missing. Two gaps:
- **No PDF:** no figure could be read, so values shown only in figures are not claimed.
- **Corrigendum not read:** the record lists one (doi:10.1038/nature18623) but its text was not supplied, so I don't know whether it changes any value.

**Code:** the paper links no code. It names its data deposit as CRCNS doi:10.6080/K0RB72JW.

**Counts:**
- **Quotes:** 38 of 38 claims; none needed an `inferred` note.
- **Statistics:** 7 claims carry 11 entries, all t-tests (two-tailed or paired) plus one repeated-measures two-way ANOVA.
- **Criteria:** every claim has one.
- **Expected values:** 19 claims. Tolerances are the paper's s.e.m. where it gives one, otherwise 10%.
- **Absence claims:** three, each judged on the paper's own test (p > 0.1, the t-test of Extended Data Fig. 3, and p > 0.05).
- **Simulations:** the two model claims are simulations, not tests on recorded data.

**Details the paper leaves open, with the readings named** (shared ones are set once in the opening comment):
- **Condition names:** the Results and Methods name the unilateral conditions differently. The Results call the 0 s condition "late delay" and the 0.3 s one "middle delay"; the Methods call the 0.3 s one "late delay".
- **Callosotomy timing:** either as in the bilateral experiment, or as recorded in the dataset's trial metadata.
- **Response epoch length:** 1.3 s or 1.5 s.
- **Selectivity t-test:** correct trials only, or all trials; Student's or Welch's.
- **Selectivity time-course bin:** 200 ms or 400 ms.
- **Rate-test windows:** labelled by their end or their centre; with the 1 spike/s and 3-trial exclusion or without it.
- **Performance t-test:** paired or unpaired over mice.
- **Trials held out to compute the coding direction:** half or a third of control trials.
- **Variance captured:** ratio of RMS or of squared RMS; baseline taken before the sample epoch or over the whole trial.
- **ROC window during photoinhibition:** three readings.
- **Fig. 1f:** whether the 10% describes each condition or the three pooled.
- **Fig. 2 recovery:** "spike rate (> 90%)" as a fraction of neurons not changed, or as the population mean rate.
- **Fig. 2b durations:** 0.8 s only, or 0.8 s and 1.3 s pooled.
- **Ipsilateral bias measure:** performance on contralateral trials, or overall performance.
- **Extended Data Fig. 4:** how photoinhibition conditions and trial types are pooled.
- **Half-max radius:** linear interpolation or a Gaussian fit.

Where the paper gives no test (above chance, "similar", "little affected", "resistant"), the criterion names the reading it uses and says it is one.

**Paper inconsistencies and gaps a claim needed:**
- **514 vs 510 ms:** the Results give 514 ms for selectivity recovery; the Fig. 1g legend gives 510 ms. The legend's values are used.
- **Misprinted s.e.m.:** Extended Data Fig. 7e prints the bilateral ROC as 0.54 ± 0.8; 0.08 is used.
- **Mislabelled figure:** the Methods cite "Extended Data Fig. 2h, i" for the trained recurrent networks, which are in Extended Data Fig. 1h, i.
- **Photoactivation timing:** not given in the text; the criterion reads it from the dataset's trial metadata.
- **Models:** the integration step and noise scaling are not given. The corrective-feedback, tamed-chaos and modular FORCE models lack parameters, so those parts are reported only.
- **Modular integrator:** its 8×8 weight matrix was read from flattened text, row by row, with no PDF to confirm it.

Whether the dataset holds the behaviour-only sessions, the untrained-mouse recordings (Extended Data Fig. 2d) and the sessions before callosotomy is for the author to find.
