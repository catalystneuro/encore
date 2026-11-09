I've finished steps 1 to 5 and built the verifier's package with `python tools/entry.py handover` (step 6). The final notebook run passed `tools/entry.py all` in 22.4 minutes (limit 30), and `check` reports 0 errors.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1c-old-faster-alarm (Data S1) | reproduced (F(3,314) = 8.006; all six parameters within tolerance) |
| fig1c-vehicle-single-curve | reproduced (p = 0.056) |
| fig1b-alarm-stimuli-similar | reproduced (p = 0.052) |
| figs1-heptanone-separate-curves | reproduced (p = 0.00057) |
| figs1-heptanol-blend-single-curve | reproduced (p = 0.12 and 0.061) |
| fig2b-gcamp-baseline-unchanged | blocked, data_unreadable: the Brain Image Library download server timed out three times |
| fig2d-whole-al-alarm-no-age-effect | reproduced |
| figs3b-whole-al-general-decline | partially reproduced: 3-hexanone ratio 41; the isopropanol old mean is negative, so its ratio is -5.7 |
| figs3b-whole-al-other-no-age-effect | reproduced |
| fig2e-heptanone-breadth-falls | blocked, methods_underspecified: the counts depend on glomerulus size; medians 4/2, 1/0, 0/0; no size gives p < 0.05 |
| fig2-alarm-sparse | blocked, because it depends on fig2e |
| figs3c-general-breadth-no-age-effect | reproduced, resting on an assumption |
| data-s2-glomerulus-link (link claim I added) | partially reproduced: 71 of 108 matches agree (66%) |
| figs2a-mean-six-glomeruli-no-age-effect | reproduced, resting on assumptions |
| fig3b-g2-heptanone-weaker-old | not reproduced (G2 p = 0.24) |
| fig3d-pg-stronger-old | not reproduced (PGb p = 0.87 and 0.16; PGa p = 0.044) |
| fig3d-pg-60-vs-90-days-same | reproduced under reading (a), using DANDI 000467, adopted as an assumption; not reproduced under reading (b), using Data S2's 90-day values |
| figs4a-general-odorants-in-focal-glomeruli | not reproduced: 57 of 60 cells match, but old G4 with 3-hexanone misses (p = 0.063) |
| fig4-general-odorants-decline | not reproduced: 7 of 10 declines significant |
| fig4-propionic-acid-g2-g3 | not reproduced |
| figs4d-pgb-hexanone-dynamics | partially reproduced |
| pg-opposite-modulation | partially reproduced |

## 2. What was found about the dataset

- **Version pinned:** 0.261004.1511, the only published version; the paper cites none.
- **Contents:** all 21 ants (7/7 at 48%, 3/4 at 3%), 22 trials each, 33 planes each. The ages and the ants match Data S2.
- **What is missing:** the dataset has no ROI positions, glomerulus identities, responding-ROI counts or stimulus times. The behaviour data are only in Data S1, which is public from the PubMed Central open-access copy and pinned by MD5.
- **Metadata errors:**
  - The timing fields disagree: the description gives 1.2 s per volume, the series rate is 1.21 Hz, and `imaging_rate` holds 0.83, a period stored as a rate.
  - One trial misspells ethylpyrazine as "ethylyprazine" in its file names.
- **Motion exclusions:** the Methods say some trials were excluded for motion artifacts, but Data S2 keeps all 21 trials of every ant, so the excluded ones can't be identified.
- **Key finding:** at positions matched to Data S2, the PGb alarm responses measured from the imaging are well below the paper's Figure 3C/3D values. This holds both for the 60-day ants here and for the 90-day ants of DANDI 000467. Run on Data S2's own values, every focal-glomerulus claim holds, so the failures above most likely come from how those ROIs were drawn or processed, not from the data.
- **Assumptions:**
  - Focal glomeruli are placed where the dataset's per-trial responses best follow Data S2's, and those claims are marked `with_inputs` and depend on the link claim.
  - The ROI is a disk of 8-pixel radius.
  - Fold change is the ROI mean first, then fold change (reading a).
  - Reading (a) is adopted for the 60- vs 90-day comparison.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How were the responding ROIs drawn (size and positions per ant), and what are the per-ant counts?
  - Where are the focal-glomerulus ROIs, what size are they, and was fold change computed per pixel or on the ROI mean?
  - Were the Figure 3C/3D PGb and PGa traces quantified the same way as the Figure 4 traces?
- **Questions to a reader:** none.

## 3. Where the protocol was unclear

1. The fig2e criterion blocks the claim when its result differs from "the paper's counts in Data S2", but Data S2 contains no counts. I ran three glomerulus sizes; their outcomes differed, so I blocked the claim as methods_underspecified.
2. The protocol has no rule for when an author may change a claim's `data` field or `depends_on`. I set `with_inputs` and added the link claim to `depends_on` on the focal claims, and left statements, expected values and criteria unchanged.
3. The protocol doesn't say how to choose between readings that differ only in where an outside comparison value comes from (fig3d 60 vs 90 days). I adopted the reading that measures both groups the same way, as an assumption.
4. It doesn't say which `blocked_by` reason to use when an outside archive is unreachable. I used data_unreadable.
5. The pg-opposite-modulation criterion states only when the claim is reproduced, with no partial or failing level. I gave partially_reproduced and explained why in the notes.
6. For the final text-only fixes I edited the Markdown of the executed copy directly instead of re-running for 23 minutes. Its code cells are identical to the committed notebook's.

## 4. Runtime and failures

- **Runtime:** about 2 h 35 min of the 5 h. Four full notebook runs, 19 to 23 minutes each.
- **Failed:** only the Brain Image Library download, which timed out three times.
- **Working files left:** the executed notebook and verifier package are in `executed/000773-hart-2024/`. Nothing was committed.
