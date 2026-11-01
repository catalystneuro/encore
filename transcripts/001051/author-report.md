I've finished steps 1 to 5 of the Author protocol and ran `handover` (step 6). `entry.py check` reports 0 errors, and `entry.py all` ran the notebook from a clean environment in 24.4 min (it passed). Nothing is committed or pushed.

**Version pinned:** DANDI:001051 0.260922.1827. The paper cites no version. The two published versions hold the same 666 assets with the same blobs; the later one only updated metadata. The notebook header says so.

### 1. Outcomes (46 claims: 16 reproduced, 5 partially reproduced, 5 not reproduced, 20 blocked)

| Claim | Outcome |
|---|---|
| link-code-tables (a link claim I added) | partially reproduced |
| fig4b-units-areas, scale, penetration, fig4d-unit-drift, qc-pass-fraction, fig4e-unit-yield, fig4e-vbn-yield, firing-rate, rf-fraction, fig4g | reproduced |
| fig7a, fig7b-visp-offset, fig7cd-mop, fig8d-cp-rf-larger-response, fig8e | reproduced |
| fig8d-response-latencies | reproduced, resting on an assumption (half-peak latency) |
| figs4ab (implant holes not testable), behavior (stable, but only 2 of 4 medians match), fig7b-low-arousal (right direction, wrong size), fig8bc (CP-RF units are more dorsal but more lateral, not medial) | partially reproduced |
| fig4d-qc-metrics, figs4i (time constant 36 min, not 25 to 30), figs6-replay (r ≤ 0.63), fig7e (lags differ from zero), fig7-hippocampus (DG coherent) | not reproduced |
| fig7cd-visp, fig7f-visp, fig7f-mop, fig8f | blocked: methods underspecified (the open readings disagree) |
| fig4c | blocked: methods underspecified |
| fig4b-trajectory, figs4de, figs4f, figs4gh | blocked: metadata insufficient |
| fig3b, fig3c, fig3d, tracks-bleeding, fig3fh, fig3i, fig4f, figs3d, fig5, fig6bc, fig6ef | blocked: data missing |

### 2. Dataset findings, assumptions, questions
- **Different units in 6 sessions.** In 6 of the 87 QC-passing sessions, the unit ids name different units from the paper's unit table. Metrics differ for 55 to 99.8% of units, and receptive-field p values are uncorrelated (r = −0.02, against 0.999 in the other 81 sessions). In 5 of those sessions, 328 of the paper's units sit on probes the files lack.
- **Extra probes.** The files hold 40 probe recordings the paper's tables leave out, almost all on unannotated channels, and nothing marks them. Leaving them out reproduces the Figure 4E insertion counts exactly (129, 126, 121, 91).
- **Undocumented selection.** The 87-session list exists only in the paper's code.
- **Missing labels.** Nothing records which probes were retracted or sharpened, the implant hole of each insertion, Dura-Gel use, or failed insertions.
- **Missing material.** None of the Figure 3 material, the Figure 5 bilateral sessions, or the VGAT-ChR2 and Vglut2-Cre mice of Figure 6 is in the dataset.
- **Smaller gaps.** Two sessions have no eye tracking, and each session has 4 image stimuli where the Methods say 8.
- **Assumption:** latency in Figure 8D taken as the half-peak time of the population mean.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - how the random-time coherence was formed;
  - how units were assigned to areas;
  - the alpha-event rule;
  - the Figure 8D latency measure;
  - the Figure S4I fit;
  - the Figure S6 windows and normalisation.

  The code's choices give the paper's 439 events for Figure 8F.
- **Questions to a reader:** none.

### 3. Where the protocol was unclear
1. **Conflicting rules for disagreeing readings.** The claims file's header says the claim is methods_underspecified; protocol step 1.6 allows adopting an assumption. I followed the claims file, which blocked 4 alpha claims.
2. **"Any reading" against "all readings".** Matching under any reading (for ambiguous reported numbers) and requiring all readings to agree (for open method details) mix within one criterion. Where the criterion said "under a reading" (fig7a) I accepted any; otherwise all had to agree, or I made an assumption (fig8d latencies).
3. **Link claims need claims-file edits.** Adding one means editing other claims' `depends_on`, though only reader runs write the claims file. I added `link-code-tables` and its dependencies to 28 claims.
4. **No outcome for a partly testable claim.** figs4ab could only be tested in part; I recorded it as partially reproduced and said why.
5. **No clock check fits eye tracking and running.** The suggested contrasts don't apply to these streams; I named them as not established.
6. **Editing conclusions after the run.** Not addressed by the protocol. I changed only markdown after the run and copied it into the executed copy (code cells checked identical).
7. **Expected counts that match only under a variant** (fig8d, the code's 0.9 presence filter). I recorded the variant's counts as measured, with a deviation.
8. **Full run outside the notebook.** I ran the full spike pass once outside the notebook, keeping derived results in `$TMPDIR` to develop the analyses, so the whole dataset was streamed twice.

### 4. Runtime and failures
About 1.5 h in all (03:50 to 05:20 UTC). The full development pass took 29 min and the notebook 24.4 min. Two sessions without eye tracking crashed the first pass; I fixed and re-ran them. Nothing failed after that.
