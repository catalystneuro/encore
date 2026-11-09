The claims file for DANDI:001518 is ready for an attempt. I made six changes, and the checker passes before and after them.

**Checker result:** `claims/001518/10.1016-j.bioelechem.2026.109283.yaml: 30 claims, 30 quotes, 9 statistical values, 0 problems`

The quotes match the text and the sources point at the right paragraphs. All 30 claims come from this paper, and its main findings each have a claim.

**Changes, by claim**
- **fig2d-lasting-reduction:**
  - The criterion also accepted a reduction of 10 to 22%. The 10% bound is not in the paper, so I removed that clause. The expected 20 ± 2 already fits the legend's "≤20%".
  - The criterion fixed the reference as the first set. The paper allows two readings: the first set (the legend's dashed lines) or the mean of all sets before the 1000 V/cm exposure. Both are now listed.
- **fig3-fluovolt-nonlinear:** FluoVolt had to depart from the line at 250 mV or more, a bound the paper never gives. I set it to 220 mV, which is the paper's ±200 mV plus 10%.
- **fig4a-fluovolt-limits and fig4b-di8-limits:** these used a paired t-test, which was the previous agent's choice. Methods 2.5 names only "Student's t-test", so paired and unpaired are now both readings. The criteria also now say the paper reports no test for these comparisons.
- **fig4a-fluovolt-cathodic-decline:**
  - The 71% at 360 V/cm had a tolerance of 7.1. The paper gives an s.e. of ±10 for the same 71% one sentence earlier, so the tolerance is now 10.
  - The 45 to 50% range was stored as 47.5 ± 7.5, which gives 40 to 55 and not the stated 40.5 to 55. It is now 47.75 ± 7.25.
- **fig7c-fast-conductivity-drop:**
  - The cathodic and anodic poles were compared against an invented factor-of-3 bound. I replaced it with the paper's own test from the Fig. 7 legend (a two-sided t-test), applied between the poles as a claim of absence.
  - The criterion said a 100% test-pulse value gives no finite ratio. That is wrong: it maps to the intact conductivity. The paper's "most datapoints" leaves open whether those points count, so both readings are now listed.

**What remains open** (all recorded in the check entry)
- **fig5b-conductivity-calibration:** I worked out Eq. (2) with the Methods constants. A 10-fold rise gives about a 1.2 to 1.3% reduction, against the paper's "~2%". I left the claim as written for the attempt to report.
- **fig4c-equator-follows-cosine and fig5a-gd-linear:** these claims of absence are judged with a paired t-test, but the paper names no test for them. I kept paired because the comparison is within cells.
- **Other gaps:** the paper gives no rule for several criteria. These are fig1 (the pole conditions), fig5a-gd-cathodic (the "prevented the decline" rule), fig6b (what counts as a "strong response", and 90% for "nearly all") and fig4c (how wide the arcs around the equator are). The criteria use readings named in the file, and those are not the paper's method.
- **Calculated IMP** (the theoretical membrane potential used in many claims) needs a fit of charging time against cell radius from the earlier paper (reference [20]). That fit is not in this paper.

**Ready:** yes (`ready: true`).
