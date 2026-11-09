**A. Outcomes** (23 claims in the claims file; the notebook treats all 23, testing 10 and blocking 13)

| Claim | My outcome | Reason |
|---|---|---|
| recordings-two-cells-runs | reproduced | There are 2 NWB files with 5 and 4 runs; the median run lasts 195.8 s, within 200 ± 20 (cell 18). Cell 2's runs are the original runs 3 to 6, as in the code. |
| ecode-protocol-structure | reproduced | Under IV reading (a), every run of both cells has the stated sweep counts, durations and amplitudes. The largest amplitude error is 1.2 percentage points (cells 20–21). Reading (b) fails, which the criterion allows. |
| holding-potential | reproduced | The median pre-onset potential is −69.54 mV for cell 1 and −69.12 mV for cell 2, within −70 ± 7 under reading (a) (cell 23). |
| extracellular-spikes-above-50uv | reproduced | The chosen-run templates give a negative peak of 217.0 / 159.2 µV and a peak-to-peak of 274.0 / 192.2 µV; every run is at least 159 µV (cell 25). |
| mea-electrodes-and-rates | partially_reproduced | 678 and 675 electrodes are recorded, and the MEA runs at 20 kHz. The patch rate is 20.41 kHz (49 µs) for six protocols, 20 kHz only for IDthres, and 125 kHz for APWaveform (cell 28); with tolerance 0 the patch-rate part fails. The criterion has no partial clause; read strictly, this is not_reproduced. |
| culture-age | blocked (metadata_insufficient) | I confirmed this in the archive: neither the dandiset nor the asset metadata (`wasAttributedTo` has species and id only) gives an age, DIV or plating date. |
| fig6-ais-from-dendrite | reproduced | In both cells the AIS root's parent has type 3 (cell 31). |
| gt-rheobase | reproduced | The notebook's step series gives 150 pA, but it starts at 150 pA, so it cannot give anything lower. The series from 0.10 nA gives 140 pA. Both are within 150 ± 15 (cell 33). |
| fig3b-ap-initiates-distal-ais | reproduced | The order is distal, then middle AIS, then soma under both readings (cell 35). The margin is fragile: see problem 1. |
| fig3a-largest-channel-at-ais | reproduced | Channel 43 has both the largest peak-to-peak and the largest negative peak, and it is nearest the AIS midpoint (cell 37). The result hinges on a placement that was never checked: see problem 2. |
| table1-feature-counts | reproduced | 76 / 87 / 109 / 153 match exactly, and the 79 variant is also found (cell 39). |
| fig4a-strategy-balance, gt-intracellular-scores, fig4c-hyperdepol-only-single, fig4b-intra-no-difference, fig4b-extra-better-than-soma, fig4d-templates-better-than-soma, fig5-ap-distribution | blocked (too_large) | These need 4 strategies × 10 seeds × 600 generations × 20 offspring. The lower bound is 1466 CPU-hours (cell 41), and the repository holds no optimization results. |
| fig78a-soma-intra-all-extra, experimental-intracellular-scores | blocked (too_large) | They need the same kind of fits on the two cells; again at least 1466 CPU-hours. |
| fig78b-validation-spiking, fig78c-cell2-worse-extracellular, fig10-cell2-soma-underestimated | blocked (too_large) | Each needs the fitted models. Some sub-parts could be computed (see problem 9), but none decides the claim. |

No claim states a chance level.

**B. Problems**

1. [does not affect a conclusion] **fig3b, cell 35 / `gtmodel.averaged_cutouts`.** Under reading (a) the distal AIS leads the middle AIS by only 0.005 ms.
   - That is below the 0.01 ms grid of the averaged cut-out; the 0.5 µs grid is a linear interpolation of it.
   - It is ten times below the code's own `get_peak_cutout`, which interpolates at 20 kHz (0.05 ms). At the code's resolution the two would probably tie, and reading (a) would then fail.
   - Reading (b) has a 0.02 ms lead.
   - I keep "reproduced" because the simulation (cvode, as in the code) does produce this ordering, but it should be confirmed at the code's resolution.
2. [affects a conclusion] **fig3a, cell 37.** The AIS midpoint sits at x = +1.7 µm. The two flanking electrodes are 23.3 µm away (channel 43, x = +25) and 26.8 µm away (channel 23, x = −25), and their peak-to-peak ratio is 0.939.
   - Which electrode is "nearest" therefore turns on the assumption that the template was simulated with the soma's 3D-point mean at the origin, with no rotation.
   - That placement in BluePyOpt's `LFPyCellModel` was never verified. An offset of about 2 µm in x would make channel 23 the nearest, and the criterion would fail.
   - The y position (largest channel at y = −25; the AIS spans −8.6 to −39.7) supports the assumption but does not prove it.
3. [does not affect a conclusion] **mea-electrodes-and-rates, cell 28.** The 49 µs interval is real data, not an export artefact. `0-export-to-nwb.ipynb` writes `p["time"]` from neo/WinWCP (`sync_patch_mea`), and the measured step durations match the nominal ones.
   - The claims file allows only "20 or 200 kHz" for APWaveform. The paper says "typically 200 kHz", so 125 kHz arguably fits; the claims file reads the paper narrowly here.
   - This does not change the outcome, because the other six protocols at 20.41 kHz already fail the 20 kHz requirement.
4. [does not affect a conclusion] **extracellular-spikes, cell 25.** The run is chosen by the count of non-blank channels.
   - Choosing by the count of channels with peak-to-peak ≥ 5 µV would pick cell 1 run1 and cell 2 run4 instead.
   - Every run is at least 159 µV, so the choice is immaterial.
5. [does not affect a conclusion] **`template_from_waveforms`.** The 2 SD cleaning uses the max channel of the *uncentred* median. The code's `clean_sta` recomputes it from the centred median.
   - I tested the helper on synthetic waveforms (jittered spikes, outliers, a masked channel). It recovered the right channel, the trough at sample 40, and amplitude ≈ 200 µV, and it rejected the outliers.
   - `segments` and `ramps` also behaved correctly on synthetic steps and ramps. Ramp phases come out about 1.4% short because of the 5 pA threshold, which explains the measured 3924–3975 ms against 4000 ms.
6. [does not affect a conclusion] **ecode-protocol-structure, cell 20.** The 100% scale is fitted from IDthres itself, so the IDthres amplitude check only tests linearity. The claims file prescribes this.
   - For the 0% IV step the notebook uses a 2-point tolerance; this is stated as a deviation and is reasonable.
7. [does not affect a conclusion] **holding-potential, cell 23.** The claims file treats the code's `ton` (400 ms) as the pre-stimulus point. In the files the onset is at 350 ms, so `ton` falls 50 ms into the step.
   - The notebook rightly uses the measured onset and shows the `ton` window as a variant; both give −69 mV.
8. [does not affect a conclusion] **gt-rheobase / fig3b.** The simulations use BluePyOpt's NEURON simulator, not the LFPy simulator the paper's notebooks use. The deviation is stated, and the intracellular dynamics are the same model.
   - table1 counts features from the feature files rather than from the evaluator's objectives; this is stated and reasonable.
9. [does not affect a conclusion] **Blocked claims, cells 0 and 40.** Some sub-parts could have been computed without any fits, but were not:
   - the ground-truth spike counts at HyperDepol −160% and −40% (fig4c), using gtmodel;
   - the counts of 86 validation intracellular features and about 796 extracellular features (fig4b), from the repository's feature files and template;
   - the recorded spike-count ranges per validation sweep (fig78b), from the dataset.

   None of these decides a claim.
10. [does not affect a conclusion] **Archive metadata (cells 4–5).** The dandiset's `relatedResource` links the paper to the wrong DOI (`neco_a_01676`). The notebook reports this correctly.

**C. What I could not check**

- **fig3b at the code's resolution.** I need the −20 mV crossing and peak times computed with the code's `get_peak_cutout` (20 kHz interpolation), or with a fixed `dt`.
- **fig3a placement.** I need the AIS midpoint in the coordinates of the instantiated `LFPyCellModel` (`lfpy_cell` x/y), or the template recomputed on the 20 × 4 probe from the released model.
- **Patch–MEA alignment within long sweeps.** I need a plot or table of each spike's centring shift against its time within the sweep (for example, late firepattern spikes) for every run. That would confirm that the 49 µs patch clock stays aligned with the 20 kHz MEA across 3.6 s sweeps. The clock check (cell 15) covers only first-run averages, not per-spike shifts.
- **Junction-potential correction.** No metadata says whether the stored voltages are LJP-corrected. Reading (a) passes, so this does not matter.
- **The figures (cells 21, 26, 35).** These were image outputs I did not view; I relied on their printed ranges.
