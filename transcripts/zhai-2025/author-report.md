I've written the entry at `entries/zhai-2025/`, the record at `attempts/zhai-2025-02.yaml`, and one question to a reader in `questions/zhai-2025.yaml`. `entry.py all` passes with 0 errors; the notebook ran clean in 6.1 min with peak memory 0.7 GB. The verifier's package is built in `executed/zhai-2025/handover/`. I worked blind: I did not look for the earlier attempts and did not come across any of their results.

## 1. Outcomes (45 claims)

| Claim | Outcome |
|---|---|
| link-somatic-cells | partially reproduced (73% of cells match a paper row exactly, 85% within 3 spikes; every group has the paper's n) |
| link-dendritic-cells | reproduced (8 of 10 groups have the paper's n; median difference from the paper's values 2.8%) |
| link-sr-cells | partially reproduced (all 33 cells match by identifier; event counts do not) |
| link-grab-rois | not reproduced (16 of 34 regions within 0.05 of a paper region) |
| link-aim-mice | not reproduced (Figure 8 mice differ from the paper; Figure 10 mice match in 98% of sessions) |
| fig1f, fig1e, fig1f-sch (dSPN somatic) | reproduced |
| fig1i-dspn-dendritic-on-higher | reproduced (P = 0.0091) |
| fig1i-dspn-dendritic-sch-lower | not reproduced (lower with SCH, but P = 0.066; paper 0.0133) |
| fig2h, fig2i, fig4g, fig4h (Sr2+-oEPSC) | reproduced, resting on an assumption (my event detector) |
| fig3d, fig3c, fig3d-sul, fig3f ×2 (iSPN) | reproduced |
| fig5f ×5 (GRAB-ACh) | reproduced |
| fig6c, fig6d, fig7c, fig7f, fig9d | reproduced |
| fig10b-m1r-aims | reproduced (axial, limb and orolingual F values equal the paper's) |
| 8 claims tested on the paper's Zenodo tables (`data: elsewhere`) | reproduced |
| 5 two-photon spine claims, fig4k (confocal) | blocked: not_runnable (the counts need NeuronStudio, AutoQuant and Imaris, with manual steps) |
| fig8bc-cdgi-aims | blocked: other (link-aim-mice fails for the Figure 8 mice) |

## 2. The dataset, assumptions and questions

**What the draft holds (modified 2026-11-09T19:30Z; the draft was asked for):**
- Cell counts match the paper's legends for every on-state, off-state, drug and genotype group, for somatic, dendritic, Sr2+ and GRAB recordings.
- Every timing check passes: all 11,886 spikes fall inside the current step, the Ca2+ signal rises after the injection at every site, and the Sr2+ and GRAB responses follow the stimulus.

**Problems found:**
- The confocal images for Figure 4I–K are missing, and the dandiset description does not list them as missing.
- Two cells were imaged at one dendritic site only, so they have no dendritic index. The paper counts them.
- 33 of 123 somatic cells do not exactly match any row of the paper's table.
- The Figure 8 AIM sheets differ from the paper's table, as the dandiset description itself says. Mouse 7830 has identical sheets for sessions 4 and 5, in both the dandiset and the paper's table.
- Mouse counts differ from the legends in 4 groups. The files have one subject per recording day, so mice recorded on the same day would be merged.
- GRAB regions carry no identifier linking them to the paper's ROIs.
- About the paper: its per-cell Sr2+ "average" amplitudes are the medians of its own event lists, not the means.

**Assumptions:**
- Sr2+ events: the paper used TaroTools with visual checking and gives no settings. I wrote a stand-in detector at the paper's 5 SD threshold and also ran 3 and 4 SD, with per-cell mean and median. The outcomes hold under nearly all readings. This is recorded as a `methods_unavailable` question for the paper's authors.
- GRAB: one region has no acetylcholine trial, so it takes its Fmax from the other region of its slice.

**Question to a reader:** the criterion for fig5f-ach-off-elevated says "one region per mouse", but the paper's n is regions (ROIs). I tested one value per mouse as written (P = 0.036) and per region as a variant (P = 5e-05).

## 3. Where the protocol or claims file did not fit

1. The claims file groups cells by a `condition_subfolder` column that the draft no longer has. I used the `condition` column instead and recorded it as a deviation.
2. The claims file names `lid.detect_events`, a function from an earlier helper that is not in this checkout. I wrote a new detector under that name and documented every assumption in it.
3. The GRAB link and fig5f criteria were written for one region per mouse; the draft now holds several regions per mouse. I matched per region and tested per mouse, which led to the question above.
4. The AIM link fails overall but holds for every Figure 10 mouse. The protocol has no rule for a link that holds for one dependent claim and fails for another. I tested fig10b and blocked fig8bc, and recorded the reasoning.
5. The dendritic link's "first, second, third cell of the day" is ambiguous. I read the letter as the cell number, which is how the Figure 6D identifiers line up with the files.
6. The protocol has no blocked_by code for a claim that fails because its link failed. I used `other`.

## 4. Runtime and failures

The analysis finished at about 02:09 UTC, well inside the time limit. The full notebook run takes 6.1 min, most of it streaming the files. Nothing failed; the only fix along the way was resolving the S3 URL without a HEAD request, which S3 rejected with a 403.
