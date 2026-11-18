I've finished steps 1 to 5 of the Author section and run the handover (step 6). Of the 33 claims, 13 were tested: 7 reproduced, 3 partially reproduced and 3 not reproduced. The other 20 are blocked. `tools/entry.py check` passes with 0 errors. The main notebook ran cleanly from a clean environment in 1053 s.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| fig1-poltcomp-optimal, fig2b, figs2-1b, fig2c, figs2-1d, fig2d-log-decline, fig2d-fly-values, fig2d-ten-thousand-rois, discussion-twenty-rois | with_inputs | blocked, `data_missing` (the SCKm and DistKm atlases are not published) |
| fig3d-confidence-threshold | with_inputs | blocked, `data_missing` (FlyEM SC at confidence 0.5, 0.6, 0.7 and 0.9 is not published) |
| fig3d-flyem-vs-flywire | with_inputs | partially reproduced: FlyEM 0.616 against FlyWire 0.575, so FlyEM is higher, but both are below tolerance |
| fig3e-flyem-higher-most-regions | with_inputs | reproduced: 55 of 63 regions (`assumed`, depends on left-right orientation) |
| fig3g-transmitter-correlation | with_inputs | not reproduced: ACh r = 0.013, GABA r = -0.157 |
| fig4e-unsegregated-higher | with_inputs | reproduced; selected total 2,373,104, null-totals p = 0.832 |
| fig4f-segregated-lower | with_inputs | reproduced under reading (a); reading (b) not run |
| fig4i-reciprocal-higher | with_inputs | reproduced |
| figs4-1-flyem-permutation | with_inputs | blocked, `data_missing` |
| fig5b-walking-activation | with_inputs | reproduced under reading (a) |
| fig5b-walking-suppression | with_inputs | not reproduced: no negative cluster (lowest t is -0.82) |
| fig3a-postsynapse-counts | elsewhere | partially reproduced: FlyEM at confidence 0 is not in the deposited table |
| fig3c, figs3-1a, fig3f | elsewhere | reproduced, from the paper's own per-ROI tables |
| fig4b-ppssi-distribution | elsewhere | partially reproduced: mean 0.471 fits, but 138,144 neurons have a PPSSI, not 139,255 |
| figs3-2cd-apl-similarity | elsewhere | blocked, `not_runnable` |
| fig4a, fig4c, figs4-1ij, fig4h, fig5-wagn | elsewhere | blocked, `other` (not attempted; I gave the time to the dataset claims) |

All tested with_inputs outcomes are marked `assumed`, because they rest on registration and tCompCor choices the paper does not fix. The FC computed here gives FlyWire r = 0.575 where the paper's own Zenodo output gives 0.684. The paper's per-region values give its transmitter numbers exactly, so the fig3g failure comes from this attempt's FC, not from the SC.

## 2. Dataset, assumptions, questions

**Version.** 0.240106.0043, the version the paper cites and the only published one.

**What checked out.**
- The files match their description: 9 flies, 3384 volumes at 1.8797 Hz, 50 Hz FicTrac speed.
- In name order, the files reproduce the walking regressor stored in the paper's code (`data/behavior.mat`) to 1e-5. That confirms the subject order and that behaviour is aligned to the imaging.
- fly-100, the seventh fly, which the code leaves out, has the worst field-of-view coverage. That fits the paper's reason for dropping one fly.
- No duplicate recordings.

**Problems recorded as findings.**
- The SCKm and DistKm atlases are not published anywhere; Zenodo holds their SC matrices but not which voxels belong to which ROI.
- The files do not say which side of the volume is left or right.
- The `dimension` attribute is [128, 256, 49] while the data are stored as (time, 256, 128, 49).
- The processed series has no voxel size.

**Inputs.** The paper's code at commit 4b92add and Zenodo 10.5281/zenodo.15532272 (the version cited by the code's README, which predates the preprint).

**Assumptions.**
- No left-right flip. Swapping left and right lowers the FC-SC correlation, which supports this.
- No SPM12 motion or slice-timing correction; ANTs SyN registration in Python.
- tCompCor voxels chosen in native space, before warping.
- GLM fitted by OLS without the Tukey-taper pre-whitening, smoothed on the beta maps.
- Cluster extent taken from the code's README.

**Question for the authors** (recorded as a `methods_unavailable` finding): which SPM12 and ANTs settings, and which NIfTI voxel size, were used?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. "Fix every random seed": ANTs registration is not repeatable even with a seed and one thread. I said so in the notebook and record; numbers can shift slightly when CI re-runs the notebook.
2. I edited conclusion markdown after execution and copied the same edits into the executed copy. No code changed.
3. I ran the companion notebook (`connectome_okuno_2025.ipynb`) with nbconvert in the entry's environment, not with `entry.py run`, to avoid re-running the main notebook and shifting its numbers. `result.json` therefore lists only the main notebook.
4. For the elsewhere claims, the protocol does not say whether the paper's own derived tables count as the data. I used them and recorded it as a deviation.
5. The Time rule only covers claims cut off at the deadline. For claims I chose not to attempt earlier, I used `other` and said so.
6. There was no clear place for a link claim, since the SC is matched to the data through template space. I added none and checked subject identity through the behaviour regressor instead.
7. The claims file's M3 says tCompCor voxels are ranked by SD after detrending, but the code it cites ranks them before. I followed the code and recorded a deviation. I didn't ask a reader, because it cannot change an outcome.

## 4. Runtime and failures

The run took about 3 h (05:09 to 08:04 UTC). The main notebook takes about 18 min and 4.6 GB peak memory; the companion takes under 1 min.

Fixed during development:
- Streaming through remfile ran at about 10 MB/s; switching to parallel direct chunk reads gave about 165 MB/s.
- Antspy's default affine registration stalled for three flies; I now start from the better of two affine registrations.
- A slow column gather made each fly take 400 s; fixed to about 65 s.

Nothing is committed.
