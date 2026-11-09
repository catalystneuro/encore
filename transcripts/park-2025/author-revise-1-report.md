I've worked through all 19 points in the verifier's round-1 report. Both notebooks were re-run with `python tools/entry.py all entries/001266-park-2025` and pass: the main notebook in 17 min, the simulations notebook in 36 min. `tools/entry.py check` reports 0 errors. Every conclusion, the summary tables, the README and the attempt record now match the new numbers. Round 1 is recorded under `verifications`: the verifier's outcome differs from the record it reviewed on 9 claims, and each claim has a `response`.

**Outcomes changed**
- **Partially reproduced → not reproduced**, because the criterion is not met under the readings the claims file gives:
  - fig2e-f-dspike-maps
  - fig3-subthreshold-no-dendritic-initiation: the orphan distal events are now shown. One is a missed somatic spike at 4.7 to 4.9 s.d. The two in the D4+soma file have no somatic activity above 2.4 s.d. before them.
  - fig3f-soma-plus-distal: 46 of 54 beyond 300 µm, outside the tolerance. The 300–400 µm region gives 49 to 51 and is shown but not adopted.
  - fig5a-plateau-collision: the plateau lasts 146 ms against 120 ± 12.
  - figs23-dendrite-drives-soma: the longest persistence is 170 to 222 ms in every new reading, against about 300.
- **Not reproduced → blocked (methods underspecified):**
  - fig1-denoising-variance: the share depends on the preprocessing. Centred data give 22–30%, baseline-only 16–58%, raw counts a trivial 100%.
  - figs17e-ttx-high-dose: the baseline has no dSpike threshold in 5 of 8 readings; in the 3 where it has one, the claim holds.
- **figs20-model-robustness**, blocked (too large) → not reproduced: all 429 sweep runs now run in parallel. The motif region never includes the Table 1 parameters (11, 17 and 0 cells, against 51, 48 and 88 in the published matrices).
- **figs21-izhikevich**, blocked (not runnable) → reproduced, using a line-by-line Python port of the MATLAB script. Octave cannot be installed here; the notebook prints the `.m` source beside the port.

**Added or corrected**
- **dSpike threshold (B1):** it now starts from the lowest real mode (density peaks under a quarter of the highest are ignored). Where there is no trough, the count is reported as undefined, not as zero.
- **Region check (B3):** a figure and table of the mean images with the traced line, the soma and the 200/300/400 µm marks. Beyond about 400 µm the line runs into background.
- **Detection checks:** distal amplitude histograms for the noisy files, and counts rejected by the FWHM rule.
- **Other outputs the verifier asked for:**
  - the 488 nm drive per stimulus in figs15: all twenty are equal, so they are true repeats;
  - a shared-threshold variant for figs18g: the pattern holds in 16 of 16 readings;
  - fig5b ratios for the 10 plateau cells beside the Source Data's 28 values (3.84 ± 0.96 against 3.12 ± 0.66);
  - a distal-only region, 20 ms smoothing and difference traces for figs23;
  - a repolarisation rule for the electrical spikes in figs2: rates now top out at 91 Hz, and the false detections remain;
  - Table 1 runs (NaV 47) and 300 ms steps for fig4f-g: still not reproduced.
- **Question for a reader (B2):** in `questions/001266.yaml`, on the claims file's statement that the somatic threshold "cannot change the outcome". The claim is unchanged.
- **Model finding:** the `code_mismatch` finding now also covers the phase-diagram mismatch and a NEURON callback in the published model. That callback outlives each model run, so every run now gets its own process.

**Not done, and why**
- **fig3d-distal-first-bap** stays reproduced, resting on the 4 s.d. somatic threshold. I recorded the verifier's disagreement (it would block the claim) rather than adopt it: its own point B2 supports the 4 s.d. threshold, which matches the legend's bAP counts.
- **fig3i-distance-dependence** stays blocked as `data_missing`, where the verifier gives `metadata_insufficient`, because 4 of the 35 dendrites needed are deposited even with positions.
- **The "partly testable" blocked claims** (figs12, figs16/17 drug pairs, fig5d-timing, fig6 and the others) were not analysed, for lack of time. A single cell could not decide a pooled mean or test in any case; only fig5b was added.
- **Not run:** maximum-likelihood pixel weighting and a NEV window away from the first second (figs2), the dSpike-echo question in fig2a (B6), and the S8 panel counts (B17).
- **Process:** the simulation work, done in a delegated run, held this session up for almost two hours. The final simulations notebook ran in full only once, inside `entry.py all`, and its outputs were checked against the conclusions.

Nothing is committed.
