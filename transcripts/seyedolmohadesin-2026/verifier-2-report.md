**Round-2 verification: Seyedolmohadesin et al. 2026 (attempt seyedolmohadesin-2026-01)**

The claims file has 34 claims and the attempt record has 34 outcomes: 25 reproduced, 4 not reproduced, 5 blocked.

**1. Outcomes and assumptions**

I agree with all 34 stated outcomes.

- **fig5b-layer-counts (now reproduced, was partially reproduced).** I agree.
  - The change rests on a new layer assignment taken from the column headings of Figure 3A. The paper's text file does not contain those headings, so I rendered the PDF page (cell 13 lists the assignment). The headings are Sensory (ADE to URYV, IL1 included), Interneuron (ADA to URB), Motor (RMD to VB2, RMG and URA included) and Pharyngeal (I1 to NSM). This matches `chemo.LAYER_CLASSES` class for class.
  - With it, reading (a) puts all eight counts within tolerance under both exclusions (cell 28), which meets the criterion.
  - Two counts sit at the edge of tolerance: sensory dimorphic 24 against 22 ± 2.2, and pharyngeal dimorphic 11 against 12 ± 1.2.
- **fig2-awa-awb-nociceptive (now not reproduced).** This now matches my round-1 outcome.
- **fig4g (blocked).** I agree with the outcome, though one supporting sentence is wrong (section 2).
- **Assumptions.** No outcome now has `assumed: true`. That is reasonable:
  - The layer assignment is now taken from the paper and recorded as a deviation, as the claims file's CLASSES section asks.
  - The remaining author choices are each stated as deviations, and none decides an outcome: the 95% quantile over nonzero weights, the baseline fit (10th percentile of each 100-frame bin), the 13-frame window, and the h3/m3 split.
  - I showed in round 1 that taking the quantile over all values including zeros also misses the tolerance.

**2. Text against printed outputs**

These sentences are not supported by the numbers:

- **Cell 43, and the record's notes for fig3a-osmotic-onset-examples:** "both respond to sorbitol in each sex (RESPONSIVE p 9.2e-09 or below)". ASER's hermaphrodite p is 3.7e-06, and 4.5e-06 under exclusion (b) (cell 42). The bound should be about 5e-06. The conclusion is unaffected.
- **Cell 110, and the record's fig4g notes and response:** "the claim stays blocked whichever form is taken". With Cook's counts, both orders meet the criterion (cell 109: order (i) under both "not connected" readings, order (ii) under reading (b)). So with counts alone the outcome would be reproduced. The claim is blocked because the two forms disagree, and because sections fail order (ii).
- **Cell 68, the Summary's last-but-one bullet, and the record's tail-unresponsive notes:** "the tracked positions in the files are all zero". Cell 15 sampled every 997th ROI of one file (20220327-h2), from the `processing/NeuroPAL` copy only. The findings entry states this scope correctly; the other three places generalise it to all files.
- **README:** "nearly two of them streaming the trace tables". Cell 1 prints 55 s for loading all 47 trace tables.
- **Record, connectome-link notes:** "185 in the male matrix". That figure is for the sections sheet; the counts sheet matches 165 (cell 96).

Every other "**Result:**" sentence, the Summary, the README table and the record's notes agree with the printed outputs. I checked every number in cells 20 to 125 against its output, including all counts in the 48-combination table for figs3fg.

The record states my round-1 reasons faithfully for all 34 claims. They are condensed but in my wording, and the problem numbers are carried over correctly (1, 2, 3, 4, 7, 8, 9, 10).

**3. Round-1 points**

Resolved:
- **1. Layer assignment.** The assignment is now Figure 3A's, which I confirmed against the figure. The earlier assignment is run as a variant for every layer-dependent claim. sensory-dimorphic-and-monomorphic stays at 21 and 20 of 24 under both assignments.
- **2. Baseline fit.** The baseline-only fit is now run (48 combinations), with per-layer cell counts and three example AVA traces with both fits. figs3fg stays blocked: 36 of 48 combinations at q < 0.05, with at most 13 interneuron cells in any combination.
- **3. Sections as the paper's form.** The record and notebook now draw this out.
- **6. Tail traces.** An h5 listing of two files shows no trace table other than ActivityTraces.
- **7. Chance level.** Now stated in the notes.
- **8. Band-pass filter.** The code's functions were copied in and compared with the helper on a toy trace with a gap: largest difference 0.0 (cell 69).
- **10. Connectome forms.** connectome-link is now run with both Cook forms.
- **Section C, Cook counts parse.** Known connections are now printed from every sheet (cell 94).
- **Points 4, 5, 9, 11 and 12** needed no change. I still find no misreading of the paper in the claims file. One omission: the claims file says the layers are given only in Figure 5A and Data S4, but Figure 3A labels them.

Remaining:
- **Bears on a conclusion (fig4g):** the "whichever form" sentence above. The outcome stays blocked, but the stated reason should be that counts and sections give different outcomes.
- **Does not bear on a conclusion:**
  - In cell 94, AVAL→VA08 is 0 in both Cook counts sheets and 7 in both sections sheets. This is unexplained. It does not touch the 83 subclasses compared.
  - The per-stimulus counts of Figure 5B remain unchecked, because Data S4 is unavailable. The red, black and gray name colours of Figure 3A now offer a partial check that was not run.
  - The zero-ROI finding rests on one file, sampled.
