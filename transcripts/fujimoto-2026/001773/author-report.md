I've finished steps 1 to 6 for DANDI:001773: the entry `entries/001773-fujimoto-2026/`, the record `attempts/001773-fujimoto-2026-01.yaml`, one reader question in `questions/001773.yaml`, and the handover package. Lock, check and run all pass, and the notebook runs in 32 s from a clean environment. Nothing is committed.

**(1) Outcome per claim** (32 claims)

| Outcome | Claims |
|---|---|
| reproduced (27) | ed1-behavior-increase, fig2a-cb-fa-increase, fig2a-no-change-other-tracts, ed2-cb-both-monkeys, fig2b-mcc-cb-fa-increase, fig3c-cc1-dapi-ratio, ed5-cc1-count-dapi-unchanged, ed6-dacc-ufm-no-oligodendrocyte-change, fig3f-g-ratio-decrease, fig4a-cortical-down-subcortical-up, fig4b-roi-changes-counts (rests on an assumption), fig4-nonsurgical-no-pattern, fig5a-pre-scc-connectivity, fig5b-scc-decreases, fig5b-scc-increases, ed9-control-hemisphere-changes, ed9-no-change-motor-mcc, ed7-decreases-both-monkeys, fig5c-dmn-lim-cen-decrease, fig5c-smn-increase, fig5c-vis-no-change, fig5c-san-rebalanced, fig6a-monkey-d-cb-fa-decrease, fig6b-monkey-d-dacc-cb-decrease, fig6c-monkey-d-cc1-no-change, ed10c-monkey-d-subcortical-decrease, ed10d-monkey-d-roi-changes |
| not reproduced (1) | ed1-monkey-d-no-change: monkey D's foraging falls from 0.183 to 0.050, P = 0.023 |
| blocked (4) | fig4c-network-sorted-reduction (methods_underspecified: the connectome ROIs have no names or network assignment); fig5a-nonsurgical-no-reduction and fig6d-monkey-d-scc-local-increase (data_missing); fig6e-monkey-d-no-network-reduction (methods_underspecified: it was run, its readings disagree, and the criterion says to block in that case) |

**(2) The dataset**
- **Contents:** no NWB. It holds 34 Excel sheets of derived values and 18 MATLAB scripts. I pinned 0.260416.1939, the version the paper cites; the latest version, 0.260615.1838, has identical asset ids.
- **Match to the paper:** with the scripts' models, almost every F value, partial eta squared and voxel or field count matches the paper to the printed digits.
- **Missing:** fMRI and DWI images, whole-brain seed maps, the nonsurgical controls' seed data, per-monkey connectomes, ROI names for the 123 x 123 connectomes, and the lead location.
- **Errors:**
  - The behavior legend codes foraging as yes 2 / no 1, but the values are 0/1. Monkey D's group code (2) is not in the legend.
  - Two MCC-CB fields have ratios that don't match their counts, and two have more CC1 than DAPI cells.
  - The EM "diameter" column holds a radius.
  - Two scripts are deposited twice under different names.
  - The dandiset metadata does not link the paper.
  - The Fig. 6a legend's interaction df is printed as 1; the data give 2.
- **Assumption (fig4b):** I took the per-ROI test and threshold from the paper's Fig. 4 script: a rank-sum of each ROI's changes against zeros at P < 0.05/123. That gives exactly 69 and 44 ROIs, and the largest P counted (3.88e-4) matches the Supplementary Tables. The Methods say P < 0.01 with Bonferroni correction, and none of the criterion's readings gets both counts within tolerance. I recorded this as a `code_mismatch` finding.
- **Question for the paper's authors (fig6e):** does "not observed" cover the control hemisphere, and which LIM membership is meant?
- **Question to a reader (fig4b):** should the criterion include the script's test and threshold? I also asked whether "122 ROIs" is right, since the matrices have 123 and 122 is the number of values per ROI.

**(3) Where the protocol was unclear or did not fit**
1. The DANDI reading rules assume NWB read with remfile and h5py. I fetched each xlsx asset into memory through the API's download endpoint.
2. The step 2 clock and stream-alignment check has nothing to act on in derived tables. I checked that the side labels match the hemispheres (coordinates, voxel counts, EM image labels) and recorded pre/post as consistent with the data but not shown.
3. The paper's code sits inside the dataset, so the readers, who may not open dataset files, never saw it. Code-settled details fell to me, and for fig4b the code's procedure is not among the criterion's readings. The rule "Methods first, code as variant" conflicts with the fact that the paper's own tables follow the code. I adopted the code's procedure as an assumption and asked a reader.
4. A criterion reading the data cannot support: only concatenated-run seed maps are deposited, so the per-run reading could not be run. I recorded it as a deviation.
5. For absence claims, the protocol says the several-readings rule does not apply, but the fig6e criterion says to block when its readings disagree. I followed the criterion.
6. SciPy's studentized-range tail stops at about 1e-11, where MATLAB prints 0. I stated this; it cannot change an outcome at P < 0.05.

**(4) Runtime and failures**
The run took about 25 minutes (16:09 to 16:33 UTC), and the notebook itself takes 32 s. The only failure was one notebook run that broke on a string escape in my generator; I fixed it and the rerun passed. The working tree also shows untracked dotfiles and a `scripts` entry; these are sandbox device placeholders created before the run, and I left them alone.
