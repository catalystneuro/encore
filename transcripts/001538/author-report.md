Done. I followed steps 1 to 5 of the protocol and ran `python tools/entry.py handover entries/001538-zhai-2025`. `check` reports 0 errors and the notebook runs from a clean environment in 248 s. Nothing is committed. I used the full text of the paper, which is open access (PMC12674127, CC BY). I pinned dandiset version 0.260527.1302: the paper cites no version, this is the only published one, and the draft holds the same 468 files.

**1. Outcomes (44 claims)**

| Claim | Data | Outcome |
|---|---|---|
| link-somatic-cells | with_inputs | partially reproduced (73% of cells match exactly, the criterion asked for 80%) |
| link-dendritic-cells | with_inputs | reproduced |
| link-sr-cells | with_inputs | partially reproduced |
| link-grab-rois | with_inputs | not reproduced |
| link-aim-mice | with_labels | not reproduced |
| fig1f rheobase on < off; fig1e F-I; fig1f SCH no change; fig1i dendritic on > off | dandiset | reproduced (4) |
| fig1i SCH lowers the dendritic index | dandiset | partially reproduced (P = 0.066) |
| fig3d, fig3c, fig3d sulpiride no change, fig3f | dandiset | reproduced (4) |
| fig3f sulpiride does not change the dendritic index | dandiset | not reproduced (P = 0.0164; the paper reports 0.0545) |
| fig5f off-state > unlesioned; off-state similar to 6-OHDA | dandiset | reproduced (2) |
| fig6c, fig6d, fig7c, fig7f, fig9d | dandiset | reproduced (5) |
| Sr2+-oEPSC claims (4), GRAB-ACh claims (3), AIM claims (2) | dandiset / with_labels | blocked, other (too few units for the paper's test) |
| Spine density claims (6) | dandiset | blocked, not_runnable |
| 8 claims on the paper's Zenodo tables (lesion groups, oxo-M, rotations, open field) | elsewhere | reproduced (8) |

**2. What was found about the dandiset**
- **What is there:** the somatic and dendritic patch-clamp data are present for every group except the unlesioned control and 6-OHDA groups, and every cell count matches the paper's.
- **What is missing:** the unlesioned control and 6-OHDA patch-clamp groups, the oxo-M data and the open-field data. All are in the paper's raw-data zip on Zenodo.
- **Groups need `condition_subfolder`:** files named for SCH 23390 or sulpiride also hold baseline cells, and 11 cells in them are baseline only.
- **Subsets too small for the paper's tests:**
  - Sr2+-oEPSC: one cell per mouse, 14 of the paper's 33.
  - GRAB-ACh: one region per mouse, 11 of 34.
  - AIM: 7 of the paper's 44 mice, plus 2 mice that are not in the paper. The totals of the Figure 8 mice differ from the paper's in 20 of 25 sessions.
- **Contradictory AIM genotypes:** the subject metadata, session names, the table's genotype column and the video files disagree with each other.
- **Raw data without measurements:** there are spine image stacks and rotation videos, but no spine or rotation counts.
- **Stimulus and background records:**
  - Every dendritic stimulus series is all zero.
  - The light-pulse trace is all zero in 69 of 140 Sr2+-oEPSC sweeps.
  - The GRAB-ACh "zero-laser" background images are brighter than the signal.
- **Identifiers and labels:** files cite the preprint and use its figure numbers, and patch-clamp subjects have no animal identifiers.
- **Paper against its own tables:** the CDGI KO oxo-M test gives P = 0.47 on the paper's own table, where the paper reports 0.910.

**3. Where the protocol was unclear, wrong or missing something**
1. It does not say what to do when the dandiset has so few units that the paper's test cannot reach P < 0.05 whatever the data. I blocked those claims with `other` using a smallest-attainable-P rule, including the claims of absence, and showed their numbers under the link claims.
2. It does not say how to grade a criterion that defines only "reproduced". For fig1i SCH I used partially_reproduced, because the effect has the stated direction but is not significant, and recorded this as a deviation.
3. It does not cover a dandiset that holds the raw data but not the derived measurement. I kept the spine claims as `dandiset`, blocked as not_runnable, and tested the rotation claims as `elsewhere` on the paper's tables. These two choices are not fully consistent.
4. For `elsewhere` claims it says to test on "those data". I used the paper's per-cell tables, not its 13 GB raw zip, and recorded that.
5. Link claims are described as gates for claims that need outside data. Here most links gate nothing and serve only to check whether the dandiset holds the paper's cells. I counted them as with_inputs.
6. The protocol allows the data check before the criteria, but my data check already showed group medians. I said so in the claims file header.
7. Its clock-check recipes assume trial tables or continuous sessions. For sweeps I used within-sweep contrasts: spikes inside the step, Ca after the spikes, events after the light pulse and before/after the stimulus for GRAB-ACh.
8. It does not say whether a conclusion may cite the paper's reported values, which are not printed numbers. I cited them as "the paper reports".
9. No finding kind fits "the paper's reported P disagrees with its own deposited table". I used paper_inconsistency.

**4. Runtime and failures**
- The notebook takes about 4 minutes, mostly streaming files. The whole session took about 3 hours.
- My first check for line-scan kymograph slices missed references of −1; after the fix it finds 53 of 997 sweeps without a slice. The data check also caught three wrong sentences in my prose, and I corrected them before the final run.
- No run failed.
- The repo root has untracked dotfiles (`.bashrc`, `.vscode`, `scripts/` and others) that I did not create or touch.
