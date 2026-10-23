I checked `claims/000015/10.1016-j.neuron.2017.05.005.yaml` against the paper, made 10 changes and added one claim, and marked it ready. Nothing is committed.

**Checker result** (run again after my edits): `32 claims, 32 quotes, 1 statistical values, 0 problems`. Before the edits it was 31 claims with 0 problems.

**Changes, by claim** (each is also logged under `checks`):
- **fig6-object-location-mm**: the second window was said to end at "1.5 s, the time of Figure 6D". The figure labels put 6C at 1.5 s and 6D at 2.7 s, so that window now ends at 2.7 s.
- **fig6-lick-direction-deep-alm-first**: the criterion did not test "early in the delay epoch". Onset must now be no later than 2.7 s, the time of Figure 6D, the first panel the sentence cites.
- **fig8d-mm-object-location**: part (a) compared every MM group with ALM deep IT only, which is the earlier writer's choice, not the paper's. Each MM group is now compared with the ALM group of the same depth and type. I also added the Discussion paragraph saying MM PT cells had the strongest object location selectivity to the source.
- **fig8d-mm-posterior-preferring, fig1c-whisking-similar, fig8d-error-outnumber-correct, ephys-pt-it-onset-not-detected**: the Discussion paragraph numbers were wrong. These sources now name each paragraph by its first words. **fig8d-alm-deep-lick-direction** now cites its sentence, because the paragraph break isn't certain.
- **fig8d-error-outnumber-correct**: the paper cites Figure 8D, which shows mean signed γ, but the criterion only counted neurons. Mean signed γ is added as a second reading, and both readings must find more error-preferring neurons.
- **fig8ef-area-explains-variance**: the criterion required depth alone to beat projection type, which the paper doesn't say. It now requires area to be the largest of the three (as the Summary says) and area plus depth together to exceed projection type.
- **ephys-selective-counts**: the Methods exclude the 9 units of intermediate spike width, so a 558-unit reading is added.
- **widefield-mm-to-alm**: the statement includes the rise in activity after the response, which the criterion doesn't test. The criterion now says that rise is reported, not judged.
- **figs9-photoinhibition-alm-mm**: added a note that the Discussion attributes the inactivation experiments to Guo et al. (2014b).
- **New claim, alm-pt-it-lick-fraction-below-20**: the Discussion says fewer than 20% of ALM PT or IT cells were lick-direction selective at any time, and no claim covered that number.

**Still open:**
- I couldn't render the PDF here because pdftoppm isn't installed. Paragraph breaks and the Figure 6 panel times are therefore read from the extracted text only.
- The two silicon-probe claims are marked as data held at CRCNS (10.6080/K0S180F9), based on the earlier writer's reading of the dandiset metadata. The paper lists imaging and probe data as one deposit, so the author should check whether the dandiset holds the probe units.
- Many criteria for qualitative claims use thresholds or tests chosen by the earlier writer, because the paper gives none. Each says so.
- Supplementary Figures S1 to S10 aren't in the text. The claims on S1, S4, S5, S7 and S9 rest on the main text alone.

**Ready:** yes; the new check entry is marked `ready: true`.
