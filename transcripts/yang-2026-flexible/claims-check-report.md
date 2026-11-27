The claims file is ready for an attempt. I made six corrections to criteria. Every quote, p-value, n and expected value was already right.

**Checker result:** `claims/yang-2026-flexible.yaml: 29 claims, 29 quotes, 26 statistical values, 0 problems`. I ran it before and after my edits, with the same result.

I also cloned the paper's code at the commit the file cites (61a5a41) into a temporary folder and checked each criterion against it. Nearly everything the file attributes to the code is there.

**Changes, by claim**
- **pc1-long-pulse-loadings:** I added `hero_sweep.stim_amp` to the current features. Its amplitude is set at a fixed offset above rheobase, so the paper's "rheobase/threshold current" covers it; leaving it out could have made reading (a) fail on a technicality.
- **ttype-beyond-cre:** The test for "residual t-type structure remained detectable" (residual η² above a shuffle null) was presented as the paper's own. The paper prints no residual η² value and no test for it. It is now marked open, with two readings: residual A_t above its null (Table 2 rows g–i), or residual η² above a label-shuffle null.
- **type-level-exceeds-cell-level:** I removed a made-up bound (15-NN Jaccard below 0.05). The claim is now judged on type-map concordance against cell–cell distance correlation; the Jaccard values are reported but not judged.
- **pair-tag-threshold-sensitivity:** I removed two made-up bounds (20%, and 10 percentage points). The claim is now judged on the ordering the Results describe: at every cutoff in the code's grids, the selective fraction is below both the stable and the intermediate fractions.
- **fig4-alternative-panels:** I replaced an invented margin ("more than 0.3") with the code's own asymmetry rule from `q3bc_explain.py`: ρ with mean S of at least 0.25, and |ρ| with rank range below 0.15.
- **fig4c-no-module-tracks-rank-range:** The 0.10 bound used for a partial result had no source. It now says the bound is borrowed, as an assumption, from the paper's WGCNA threshold (Table 2 row y).

Every change, with its reason, is in the new `checks` entry at the end of the file. No claim ids were changed.

**Still open**
- The Extended Data figures and the DOCX tables are not in the text, and no PDF was supplied, so only their legends were read. No expected value depends on them.
- The code lacks the script that ran IPFX on all cells and the one that produced the 1,000-shuffle null for Table 2 rows m and n. The claims already name readings for both.
- The hierarchical-subtype and Cre alignments in Extended Data Figure 2-1A have no numbers in the text, so they have no claim.

The only tracked change is to `claims/yang-2026-flexible.yaml`; nothing is committed or pushed. Git also shows some untracked files at the repository root (dotfiles, `.idea`, `.vscode`, `scripts`). I left them alone; the `scripts` folder was already there before I made any changes.
