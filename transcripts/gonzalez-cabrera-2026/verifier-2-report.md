**Verifier report, round 2: Gonzalez-Cabrera et al. (2026), attempt gonzalez-cabrera-2026-01**

Counts come from the claims file and the attempt record: 41 claims, of which 2 are reproduced (both `assumed: true`) and 39 are blocked (15 `methods_underspecified`, 24 `data_missing`).

**1. Outcomes**

| Claim | Stated outcome | Do I agree? |
|---|---|---|
| fig3b-photometry-continuous-only | reproduced, assumed | Yes, but the assumption is weaker than the record makes it look (below). |
| fig3c-photometry-opsin-vs-control | reproduced, assumed | Yes. The assumption is stated and reasonable. |
| 9 acute and 6 chronic silicon-probe claims | blocked, methods_underspecified | Yes. Cells 4 and 8 show no units, unlabelled tagging channels (ADC1 69, ADC2 45, ADC3 19) and rotarod bouts with no direction. |
| 11 juxtacellular/tracing, 5 slice, 8 open-field claims | blocked, data_missing | Yes. |

**fig3b assumption.** The outcome now rests on the ordinary two-way ANOVA (no repeated measures) with post hoc tests on its residual mean square.
- The assumption is stated in cell 24, the deviations, the README and the summary.
- The GraphPad document it cites supports the description of Prism. I fetched and decoded it: simple effects use MS(Residual) after an ordinary ANOVA; with both factors repeated they use the epoch × frequency × subject mean square; without sphericity each comparison uses only its own two groups.
- Two problems with how well it is supported:
  - One of the two arguments is circular: "the only one of Prism's forms that gives the legend's p < 0.0001" picks the method by its result. The other argument is real but weak: the Figure 3b legend omits "repeated measures" while the Figure 2f,i legends include it.
  - The ordinary form's comparison is unpaired, and the criterion asks for "post hoc paired".
- How each paired form comes out (cells 20–21):
  - Prism's repeated-measures error: continuous BH p 2.0e-4 to 5.3e-4, which is partially reproduced.
  - Separate paired t-tests: p 0.072 to 0.11, not reproduced.
  - The paired pooled-difference form: holds in 20 of 32 readings, including the main reading (9.4e-5). This keeps "reproduced" defensible under the criterion's own wording. The record sets this form aside as "not Prism's" and does not use it as support.
- Under the Methods baseline, the ordinary form's SE equals the pooled-difference SE (both 1.209 in cell 21; I recomputed it from the per-mouse values). The only difference is df 32 against 16, and the extra 16 df come from Pre cells that are fixed at 0 (cell 21, SD 0.0).
  - So "which lowers this residual mean square" (cell 24) is true as written but does not show the effect; the gain comes from the df.
  - The code-baseline readings (p 9.9e-6 to 3.8e-5) carry the result without this artefact.

**fig3c assumption.** The outcome rests on Prism's within-cell error with df 24, which is the same under the ordinary and the mixed design. This matches the GraphPad formula (SS(Subjects) + SS(Residuals)) / (DF(Subjects) + DF(Residuals)). It holds in 64 of 64 rows of that form. With separate unpaired tests it fails (p 0.13 to 0.19).

**A claims-file point (reported, not corrected).** The fig3b criterion says "post hoc paired", but the paper says only "FDR-corrected post hoc comparisons". The same criterion also allows an ANOVA "without repeated measures", whose standard post hoc test is not paired. In round 1 I said I found no misreading; this one matters now that the outcome rests on the unpaired form.

**2. Text against the printed outputs**

Every number in the two "**Result:**" cells (24 and 29), the summary (cell 31) and the record's outcome notes matches cells 13, 15–16, 19–23 and 26–28. Those include 3.8e-06 to 3.8e-05, 9.9e-06 to 3.8e-05, 2.0e-04 to 5.3e-04, 0.072 to 0.11, 20 of 32, 7.5e-06 to 4.1e-05, 0.00074 to 0.0028, 0.13 to 0.19, the interaction ranges, 133 trains, and 16 recordings in 7 files. These do not match:

- **Record, fig3-optotag-counts and fig3i-recruitment-beyond-tagged notes:** "about 1.5 h at the measured rate of about 35 MB/s". Cell 10 prints 41 MB/s and 1.3 h.
- **Record, first methods_unavailable finding:** "the pooled form gives continuous p 3.8e-06 to 2.9e-04 (Figure 3b) … separate t-tests give BH p 0.048 to 0.11". This is stale.
  - The range mixes the ordinary form (min) with the pooled-difference form (max).
  - The separate-test range is now 0.072 to 0.11 (cell 20).
  - The second methods_unavailable finding asks the same question with the correct numbers, so the first should be removed.
- **Record, fig3b notes:** "23 trials per file (13 for photometry-exp-5)". The main reading uses all intervals, and photometry-exp-5 at 5 Hz has 15 (cell 13).
- **README:** "Both photometry outcomes rest on an assumption about … an ordinary two-way ANOVA"; cell 31 says the same ("The outcomes rest on the ordinary two-way ANOVA"). Figure 3c holds equally under the mixed design (cells 26–27), so only fig3b rests on the ordinary ANOVA.
- **README:**
  - The table says fig3b is "resting on an assumption"; cell 24 and the summary say two.
  - "about thirteen minutes": cell 32 prints 10.5 min.
- **Record notes and cell 30, the Zenodo contents** (doi 10.5281/zenodo.21390830 and 10.5281/zenodo.18661700): no notebook output shows them, so I could not check them. No outcome depends on them.

The record's statements of my round-1 reasons are accurate to what I wrote. Listing the silicon-probe claims as `agrees: false` is fair: I agreed they are blocked and disagreed only with the reason.

**3. Round-1 points**

Resolved:
- 1: `regular_onsets` now drops only the two stray intervals (cell 13), and no train frequency reaches p < 0.05 anywhere.
- 4: df 24 is shown to be Prism's.
- 5: the blocked reason is now methods_underspecified.
- 6: the 470-nm-only variant gives the same outcomes.
- 7: the shared clock is now stated as shown only for the opsin continuous files and assumed for the others (cell 17).
- All of section C: post hoc forms with SE and df are printed, trial counts are printed, and the ADC and rotarod scan is done.

Superseded:
- 2: the "pooled" form I accepted is not Prism's. The record now explicitly rests on another form.

What still bears on a conclusion:
- (a) fig3b now rests on the unpaired ordinary-ANOVA comparison that I flagged in round-1 problem 3. That conflicts with the criterion's "paired". Under the paired forms the result is partially reproduced (Prism's error), reproduced in 20 of 32 readings (pooled differences), or not reproduced (separate tests). The record should say that a paired reading also gives "reproduced". The choice between reproduced and partially reproduced is open until the reader or the authors answer.
- (b) fig3c depends on the pooled error. With separate tests it is not reproduced. The record states this.
