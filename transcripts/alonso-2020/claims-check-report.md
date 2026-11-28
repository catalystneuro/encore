The claims file is fixed and ready for an attempt. I found and corrected several real errors; nothing is committed or pushed.

**Checker:** the first run gave `claims/alonso-2020.yaml: 22 claims, 22 quotes, 0 statistical values, 0 problems`. After my edits it gives `23 claims, 23 quotes, 0 statistical values, 0 problems`. The paper reports no statistical tests, so having no statistics entries is correct.

**Changes, by claim:**
- **deposit-models:** the source paragraph for the Q10 ranges was wrong (it is paragraph 5). The 30 and 18 model counts were not marked as invented; they are now labelled a standard choice.
- **fig1c-frequency-q10-phase-constant:** the 20% constancy bound was credited to the Methods. The Methods' 0.2 bound is a burst-to-burst stability check at one temperature, not a limit on change across temperatures, so the 20% bound is now a standard choice.
- **all-models-compensated:**
  - The statement now says "multiple sets of" Q10 values, as the quote does.
  - Source corrected to paragraph 6.
  - The 34 model bound had been justified by the "2 in 40" failures, but those were screened out before the 36 models were kept. It is now a standard choice.
- **intermediate-temperature-failures:** source corrected to paragraph 6.
- **figs3-duty-cycle-variable-across-models:** the source cited Discussion paragraph 9, which is about hysteresis. It now names the paragraph that holds the quote.
- **fig3, fig4, currentscapes-dominant, fig5, fig6, fig7:** the Results paragraph numbers were off or inconsistent. Sources now name each paragraph by its opening words; fig7's text is one paragraph.
- **fig3 and fig8a/b:** the Methods list two models per figure without saying which panel is which. The listed order is now stated as an assumption, with the swapped order as a variant.
- **currentscapes-dominant-currents:**
  - 10 °C was called a control temperature, but it is the reference temperature. The control temperatures are 15, 20, 25 and 35 °C.
  - The paper does not say whether IH and the synaptic current dominate the inward or the outward current. The split used is now marked as a reading, with a variant.
- **fig5-a-to-kca-tradeoff:** the statement overstated the paper. It said IA "dominates" at 10 °C; the paper says IA makes a "large contribution" there and IKCa becomes dominant at 25 °C.
- **fig6-crash-different-mechanisms:** quiescence was defined as "no spikes". The Methods define it as no more than one interval between spikes.
- **fig7:** the legends of Figures 5 and 9B point Figure 7A at model FGFKQS, so that model is added as a variant for panel A.
- **fig8-up-down-ramps:** the reason given for the tolerance gave 4, not 3. The 3 is 10% of the reported 34, rounded down, and the reason now says so.
- **fig10a-graded-removal:** the paper says removing KCa at 10 °C leaves the rhythm triphasic, which includes complete removal. The criterion only tested 25 to 100% and now includes 0%.
- **fig10b:** the 33 model bound for the H current is now labelled a standard choice.
- **Added fig6s1-crash-mechanisms:** the Results state a finding on Figure 6, figure supplement 1 that had no claim (eight more models crash by different mechanisms). Its temperatures and measure are named as open.

**Still open:**
- The second character of model "4?6W66" is garbled in the extracted text. No PDF reader was available here to check it, so the author will have to match it in the deposit.
- The figure supplement legends are not in `paper/`. Several criteria therefore rely on the main text, and the Figure 10B pie-chart counts are not recorded.
- The target duty cycle for LP and PY is 20% in the Results and 25% in the Methods. The file keeps 25% as the main value and 20% as a variant, since the protocol puts the Methods first.

**Ready:** yes. The `checks` entry records `ready: true`.
