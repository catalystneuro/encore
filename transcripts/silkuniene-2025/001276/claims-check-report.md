The claims file for DANDI:001276 is ready for an attempt. I made four fixes and added one claim, and four questions are still open.

**Checker result** after my changes: `claims/001276/10.1016-j.bioelechem.2025.109016.yaml: 23 claims, 23 quotes, 15 statistical values, 0 problems`. Before my changes it was 22 claims, 22 quotes, 0 problems.

**Changes, by claim**
- **fig7-cho-replicates-ct26:** the quote gave the reason for running the CHO series ("to make sure that our findings are not restricted..."), not the finding. I replaced it with the Results 3.4 sentence saying the central peak grew with burst number in both cell lines. The criterion only counts from 2 bursts (x4) up; I added the Fig. 7 legend as the reason.
- **fig7-offtarget-40-50-fold:** the criterion read the 40 to 50 range as being about 1 burst (x4) only. The sentence ends a paragraph covering all CT26 burst numbers, so I added a second reading: the range is the span over 1, 2 and 4 bursts (x4).
- **fig3bc-lorentzian-profile:** the paper reports R > 0.9 with p < 0.001, but the criterion only required R > 0.9. It now requires both.
- **fig7b-ct26-saturation:** for CHO, the criterion fits only 1, 2 and 4 bursts, while the paper's CHO fit uses all four burst numbers. I marked this as the file's own reading.
- **New claim, fig3bc-offtarget-deviation-falls-with-rate** (Results 3.1, Fig. 3B and 3C): no claim covered this main finding, including the suppression at the perimeter shown in Fig. 3C. The paper gives no measure or test for it, so I chose the measure and the criterion says it is the file's reading.

**Still open** (recorded under `checks`)
- **fig5c-irreversible-center:** the criterion needs Hoechst "above background", but the paper defines a background for YP only. The author will need to ask.
- **Tests the paper doesn't report:** four criteria judge findings with tests taken from the general list in Methods 2.5, not from results the paper gives. These are fig4b-near-electrode-rate-decline, fig5-raised-electrodes-weaker-center, the 10 kHz against 0.2 MHz part of fig4c-log-dependence, and fig6c-normalized-decline-similar.
- **fig4b-center-no-rate-effect:** the file records p > 0.05 because the paper says "no significant effect", but the paper prints no p-value and doesn't say which rates were compared.
- **Figures:** there was no PDF, so the figures were never seen. The ROI spacing, the panel layout of Fig. 5B and the Fig. 5C zones are still as the file describes them.

Nothing is committed or pushed, as instructed.
