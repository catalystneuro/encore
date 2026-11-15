I've addressed every point in the round-1 report. The entry re-ran cleanly with `python tools/entry.py all entries/asari-2009` (both notebooks pass, about 5 and 24 minutes), and every conclusion, the README and the record match the new numbers. Round 1 is recorded under `verifications`. Nothing is committed.

One thing to flag first: this attempt may not have been fully blind. `transcripts/asari-2009/verifier-2-report.md` belongs to the earlier attempt (asari-2009-01) and was in the checkout. I read its first part before I saw which attempt it was about. That part mentions running an MGB detector at half the automatic threshold, and I later used that same check as a second reading (after first trying a 5-SD detector). Whoever runs `reconcile` should know this.

**Outcomes that changed**
- **fig3b-fractional-power-decay and fig4-predictability-upper-bound:** partially reproduced → not reproduced, as the verifier gave. I ran the missing reading (all probes, with ended probes counted as zero). It moves the time constant by at most 0.04 s, so it stays at 1.27 to 1.78 s (fig3b) and 1.45 to 2.81 s (fig4) against 1.04 s in every listed reading. The criteria have no rule for partial.
- **The five Figure 8 claims:** blocked → tested. The files name the property sets for only six recordings, so I rebuilt the sets from the stimulus descriptions and parameters; every outcome is marked as resting on that assumption. Where the data hold the cells, the main reading gives several Table 1 rows exactly or closely (DMR 8 and 20 probes, natural AM and FM 25).
  - fig8a-proportion-by-property: partially reproduced. The order of the proportions holds, but every count is low.
  - fig8a-significance-fits: not reproduced. Four of five time constants match, but the sizes are out of the paper's order.
  - fig8b-decay-by-property: not reproduced. The amplitude constant is 0.35 s against 0.66 s.
  - fig8c-relative-effects: not reproduced.
  - fig8-natural-synthetic-probes-alike: reproduced.
  - fig8b and fig8c would become partial if the naturalistic probes were counted. I kept the main reading because Table 1 lists no naturalistic probes. I also added a question for the paper's authors to the findings, and a data-missing finding: almost none of Table 1's MHT probes are in the data set.

**Added or corrected, outcomes unchanged**
- **fig7:** the search now covers all 105 synthetic recordings and reads band edges from the TORC parameters too. No recording has the Figure 7 bands. As the nearest design, I ran the significance measure on the five natural probes after DMR frequency variants; it does not decide the claim. The claim stays blocked (data missing), with the verifier's disagreement recorded.
- **MGB spike threshold:** the authors' code applies one threshold per file, which I confirmed and cite in the helper. The notebook now prints each file's threshold (76 to 235 noise SDs) and its spike counts. At half the threshold the MGB evoked rate is 7.15 Hz, still outside tolerance, so a1-mgb-firing-rates stays partially reproduced.
- **fig4-strf:** I widened the ridge grid; 1 of 208 fits now sits at an edge, against 37 before. The Wilcoxon test still finds an improvement (p = 0.0031 and 0.025). The stimulus sampling rate is now read from the files (97656 Hz in all 51).
- **Smaller points:** the notebook now lists the 14 cells that explain 132 against 123 (without them, 118 remain). fig4 has a 1 − Q(t) comparison. fig9 compares the late plateau with the paper's κ (0.39 to 0.60 of it).

**Not done**
- The trial-resampling reading for fig8c was not run; the record says so.
- The 10-kHz response-sampling reading for the STRF claim was not run.
- No questions were added to `questions/asari-2009.yaml`. The report names no place where the claims file misreads the paper; the 1 − Q point is about the paper's figure, and the verifier said it does not change the outcome.
