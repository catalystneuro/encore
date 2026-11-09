Steps 1 to 6 are done and the handover is built. All 55 claims are in the record; the entry check passes with 0 errors, and both notebooks run clean from a fresh environment. Nothing is committed.

**1. Outcomes**

| Outcome | Claims |
|---|---|
| Reproduced (7) | source-data-index, fig2a-dspike-dichotomy, fig3d-distal-first-bap (rests on an assumption), fig4a-step-example, figs18g-ba-increases-calcium-spikes, figs2d-frame-rate-same-sensitivity, figs20ab-model-patch-vs-opto |
| Partially reproduced (5) | fig2e-f-dspike-maps, fig3-subthreshold-no-dendritic-initiation, fig3f-soma-plus-distal (rests on an assumption), fig5a-plateau-collision (146 ms against 120 ± 12), figs23-dendrite-drives-soma (206 ms against about 300) |
| Not reproduced (10) | fig2h-length-constant, fig3-two-motifs-location-independent, fig3e-soma-third-bap, fig3-predepolarization-rule, fig1-denoising-variance, fig4d-example-alternation, figs15-stochastic, figs17e-ttx-high-dose, figs2-imaging-fidelity, fig4f-g-model-accelerometer |
| Blocked, methods underspecified (2) | fig2b-bimodal-distal-amplitudes (dip test and Gaussian mixture disagree), fig5d-single-bap-no-plateau (the two AUC windows disagree) |
| Blocked, data missing (29) | every claim resting on pooled samples |
| Blocked, too large (1) | figs20-model-robustness: one Fig. S20c sweep is about 57 minutes, and there are three |
| Blocked, not runnable (1) | figs21-izhikevich: MATLAB script, and neither MATLAB nor Octave is available |

**2. What was found**

- **Dataset:**
  - The dandiset holds only the example recordings (raw movies plus DAQ channels), not the pooled samples behind the statistics.
  - There is no pixel size, no regions of interest, no structural or eYFP images and no stimulus masks.
  - Every file is its own subject, with date of birth 1900-01-01 and sex unknown.
  - Three recordings are deposited twice, with identical files.
  - Frames are 971 Hz and 1923 Hz where the paper says 1 and 2 kHz.
  - Channel names vary between files and the camera series has no description.
  - The legends' site labels don't match the file names: Fig. 2 "D1" is file D3, Fig. 3 "D2" is file D4.
  - In the Fig. 2 recording, 7 to 10 of the 54 trials have three somatic spikes, where the paper says two, and the dSpikes ride on the third.
  - The paper's published model code doesn't run as shipped: a missing argument, and non-ASCII characters in a mod file.
  - Version 0.250710.0758 is pinned: the paper cites no version, and the two published versions have identical assets.
- **Assumptions:**
  - Somatic spike threshold of 4 robust s.d., where the claims file's standard choice was 5. At 5 it misses spikes in bursts; 4 matches the legend's bAP totals (167, 170). Both are shown.
  - Distal region of 300 to 400 µm shown beside the claims file's ">300 µm", because my traced line leaves the trunk beyond about 400 µm.
  - Raw -dF/F shown beside dF/F_ref.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): the spike and dSpike thresholds and the distal region; dF_ref for bursts and the length-constant fit; the AUC window; the noise-equivalent voltage definition; the pixels used for the PCA.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**

1. The claims file said its somatic threshold "cannot change the outcome", but it does. I treated the threshold as an open detail, ran both values, and adopted the one the paper's own counts support.
2. The claims file says readings that disagree make a claim methods_underspecified, while protocol step 1.6 lets the author adopt one. I followed the claims file for the readings it names and step 1.6 for readings I added.
3. I found no rule for which blocked reason applies when a run is short of time but not computation-bound. I ran the simulations late instead, and used `too_large` with a timed estimate for the sweeps.
4. `archives.md` says to read files with pynwb; I read them with h5py over remfile only. This is recorded nowhere else.
5. The protocol is silent on non-ASCII characters in published code. I stripped them from mod-file comments and recorded it as a deviation.

**4. Runtime and failures**

- The run took about 2 h 55 min, finishing at 16:32 UTC.
- The main notebook takes 26 minutes (it streams 41 GB) and the simulation notebook 2 minutes.
- One full run had a bug in electrical spike counting; I fixed it and re-ran.
- After the last execution I edited only markdown text in both copies of the main notebook.
- Dotfiles, `.idea`, `.vscode` and `scripts/` are untracked at the repository root. I didn't create them on purpose and left them alone.
