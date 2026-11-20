The claims file is ready for an attempt (`ready: true`). I corrected 14 things across 13 claims, all from the paper, and recorded four open points. Only `claims/xia-2021.yaml` was changed, and nothing was committed.

**Checker result** (the same before and after my edits): `claims/xia-2021.yaml: 29 claims, 29 quotes, 1 statistical values, 0 problems`

**Changes, by claim**
- **Opening comment:** it said Table S1 was missing from the extracted text. It is there, on supplement page 18.
- **fig2d-hplc-yield:** the second-peak window, widened by 10% of each bound, starts at 8.19 mL, not 8.28. The source now names its paragraph by its opening words.
- **fig2g-conjugation-ratios:** the paper never says how the pHAb concentration was measured. That is now named as open, with the 532 nm absorbance peak (Fig. 2F) as the reading. Source pointer fixed.
- **fig2e-page-bands:**
  - The source pointed at the wrong paragraph; the PAGE sentences sit in the HPLC paragraph.
  - "At least two bands" is now marked as this file's reading of "several".
  - Noted that Fig. S2C labels lane 1 differently from Fig. 2E.
- **figs3-size:** how size is measured on the AFM images, and how particles are segmented, were the file's own choices presented as standard. Both are now open, with two readings. Source pointer fixed.
- **figs4-stability:**
  - The rule "two of three ROIs" was looser than the paper; it now requires all three, as the paper reports all three rising 20 to 45%.
  - Whether the ACh test was done at 0 h or 5 h is now open.
  - The ROIs are picked before the response is looked at.
- **figs6a-response-time:** if the time of ACh addition is unknown, the file took the onset from the steepest rise in the response itself, which makes the test circular. The claim is now untestable in that case. The 3 SD threshold is marked as the file's choice.
- **fig4b-lod:** the statement now says the 0.72% response at the lower limit of detection is theoretical, from the Michaelis-Menten equation, as the paper says. Background noise gets a second reading: frame-to-frame change.
- **fig4c-control-ph:**
  - Which value of each trace counts as the "fluorescence change" is now open.
  - The free-pHAb pKa had an expected value but no test; one is added, from Fig. S7A.
- **fig5b-in-vivo-response:** the 2 SD return-to-baseline threshold was called "standard". It is now marked as the file's own choice.
- **fig5c-ach-concentration:**
  - Noted that the printed rates imply different sensor concentrations in the same ROI: 8.8, 45.6 and 46.4 nM.
  - Noted that the claim cannot be tested without the AF647 calibration data.
- **fig5e-reversibility:** the 10% in the partial-reproduction rule is marked as a choice made here.
- **figs7b-in-vitro-reversibility:** the garbled return-to-baseline rule is rewritten, citing the Methods.
- **fig7-peak-timing:** "most events" weakened the paper's "all evoked responses"; it now requires all four events. It counts as partially reproduced if only the most caudal one falls outside. The paper contradicts itself there: Fig. 7B puts that event's peak at 44.55 s.

**Still open**
- I couldn't check the paragraph numbers in the Fabrication section, because no PDF renderer was available. Those sources now point by opening words and by the equations instead.
- Equation 3 applied to the printed rates gives ACh concentrations 4.2% above the printed ones, and the paper doesn't explain why.
- Two legends cite the wrong figure (S6B and S11). I read these as typos and changed no claim.
- Two minor observations have no claim: BTX doesn't change HPLC retention (Fig. S2), and fewer nanosensors than free BTX bind (Discussion). I judged neither a main finding.
