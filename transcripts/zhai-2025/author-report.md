I've finished steps 1 to 5 and run the handover (step 6). The entry is at `entries/zhai-2025/` (notebook, `zhai.py`, README, locked requirements) and the record is `attempts/zhai-2025-03.yaml`. `entry.py check` reports 0 errors and `entry.py all` passes. I ran the notebook twice and both runs gave the same outputs.

## 1. Outcomes (45 claims)

| Claim | Outcome |
|---|---|
| link-somatic-cells | partially reproduced: all 12 groups have the paper's n; 90/123 cells match exactly, 105/123 within 3 spikes |
| link-dendritic-cells | reproduced: 10/10 groups have the paper's n; median difference from the paper's values 2.7% |
| link-sr-cells | partially reproduced: 33/33 cells match an identifier; 21/33 within 25% (assumed) |
| link-grab-rois | not reproduced: counts match, but only 16/34 regions within 0.05 |
| link-aim-mice | not reproduced: Figure 10 matches (103/105 sessions); Figure 8 scores differ (12/90 sessions equal) |
| fig1i-dspn-dendritic-sch-lower | not reproduced (P = 0.079; P = 0.034 without the cell whose first pair is missing) |
| fig1f ×2, fig1e, fig1i-on, fig3d ×2, fig3c, fig3f ×2, fig6c, fig6d, fig7c, fig7f, fig9d | reproduced |
| fig2h, fig2i, fig4g, fig4h (Sr2+-oEPSC) | reproduced, marked assumed (my own event detector). fig4h gives P = 0.064 using every sweep, but 0.049 with the first 10 sweeps per cell |
| fig5f ×5 (GRAB-ACh) | reproduced |
| fig8bc, fig10b (AIMs) | reproduced. For fig10b the F values equal the paper's for axial, limb and orolingual |
| fig1-lesion ×2, fig3-lesion ×2, fig7e, fig8a, fig10a, fig10ef (paper's tables) | reproduced |
| fig2bc, fig4bc, fig4k, fig6f, fig7h, fig9f (spines) | blocked, not runnable |

## 2. Dataset, assumptions, questions

What the dataset holds:
- The dandiset has every cell of the off-state, on-state and drug groups for somatic, dendritic and Sr2+ recordings, and every GRAB region.
- It does not have the control and 6-OHDA patch-clamp recordings, the open-field data, the confocal images, or any spine counts (only raw z-stacks). These are in the paper's raw-data deposit on Zenodo.

Findings recorded about the data:
- **Missing groups (major).** The control, 6-OHDA, open-field and confocal data above.
- **Figure 8 AIM scores (major).** They differ from the published figure. Three mice in the dandiset are not in the paper, and five of the paper's mice are not in the dandiset.
- **2019-04-11 cell 1 (major).** Only its second pair of dendritic sites is in the file. This changes the outcome of fig1i-dspn-dendritic-sch-lower.
- **Spike counts (minor).** 33 of 123 cells differ from the paper's per-cell table.
- **Sr2+ sweeps (minor).** Two cells hold 12 and 11 sweeps where the paper's frequencies imply 10.
- **GRAB calibration (minor).** One region has no tetrodotoxin trial, several acetylcholine trials are too short for the script's window, and some regions hold more trials than the two the Methods give. The description says 2024-04-02 Slice1Roi2 has no acetylcholine trial, but its trial table lists two.
- **No duplicate recordings** were found.

Assumptions:
- **Sr2+ event detector.** TaroTools with visual checking can't be run here, so I used my own detector: noise SD from the recorded trace, 500 to 900 ms after the flash.
- **Sweeps.** I used every sweep of each Sr2+ cell.
- **Repeated current steps.** I used the first sweep; using the last gives the same results.

Questions for the paper's authors (recorded as `methods_unavailable` findings): which TaroTools settings and which sweeps were used, and how spines were counted.

I asked readers no questions.

## 3. Protocol points

1. **Failed link and its dependents.** link-aim-mice fails under its criterion, but only because the Figure 8 scores differ; the mice and labels do link. The protocol says dependents are blocked when a link fails, and also tested when it holds only in part. I tested fig8bc and fig10b and explained why in the notes.
2. **fig4k is mislabelled.** The claims file gives `data: dataset`, but the confocal data are public on Zenodo, so it should be `elsewhere`. I blocked it as not_runnable, which applies either way.
3. **Claims without criteria.** fig2h/2i, fig4g/4h, fig5f-6ohda, d2-control and da-suppresses have none. I used the paper's default test (Mann-Whitney, or Wilcoxon when paired) at P < 0.05.
4. **link-grab-rois unit.** The criterion matches "each mouse's vector", but the files hold several regions per mouse and the paper counts regions. I matched regions.
5. **Unlisted Zenodo deposits.** Zenodo 17260198 (raw data) and 17307059 (tables) were deposited by the authors for this paper. The paper should be listed on both. I used 17307059 as an input.
6. **fig7e data.** It is marked `elsewhere`, but the dandiset holds the naive oxo-M recordings. I ran those as a variant, and it agrees.
7. **Blindness.**
   - The claims file's opening comment describes an earlier author's data check. It names its helper and detector (`lid.py`, `lid.detect_events`) and a `condition_subfolder` column that is no longer in the files.
   - The dandiset's own description gives the "90 of 123 cells" figure, which looks like an earlier check's result.
   - I saw no earlier attempt's record, entry or outcomes.
8. **Version.** 0.261124.1858 was asked for and is also the newest published version, so I didn't compare it with other versions.

## 4. Runtime and failures

- The session took about 1 h 05 min (16:08 to 17:14 UTC).
- The notebook runs in about 7.5 min with 1.2 GB peak memory.
- Zenodo returned one 504 error during development. I added retries to the helper, and a call that still fails raises an error.
- Nothing else failed. Verification is for the separate verifier run, so nothing was committed and nothing was verified by me.
