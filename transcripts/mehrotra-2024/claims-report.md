I wrote the claims file for DANDI:000987 at `claims/000987/10.1016-j.cub.2024.05.048.yaml` and did not commit it. The quote checker passes on all 19 quotes; its one flag is p = 6.1e-5 in `fig1g-dv-sequence-du`, which the extracted text prints garbled as "6.1 3 10�5" and which I confirmed by reading. Other untracked files in the working tree (`.bashrc`, `.idea`, `scripts` and so on) were not created by me.

**Text read:** the version of record, from a PDF supplied by a person, with its STAR Methods (pages e1 to e8) and the supplement (legends of Figures S1 to S5). I did not view the figures, because the PDF could not be rendered here, and no claim needed one. Nothing the claims depend on is missing from the text.

**Code read:** github.com/PeyracheLab/MehrotraLevenstein_2023 at commit 4ee34f3. It has Python scripts for each figure panel, the DOWN-state detectors (including `detectDOWNs_RSC.py` and `Figure5F.py`), and the MATLAB model. It has no code for Figures 1I to 1K, 2, 4 or S4, and it does not pin its pynapple version.

**Counts:** 19 claims, all with quotes. 15 carry statistics (28 values) and 18 have criteria; `fig1e-delay-range` is judged by its expected values alone.
- **This dandiset:** only 2 claims use it. `rsc-dataset` checks the counts of 570 units, 14 sessions and 3 mice. `fig5f-rsc-pmr-onset` tests the correlation between UP onset delay and peak-to-mean ratio (PMR; Kendall τ = -0.28, p = 6.76e-21, n = 570).
- **Other data:** the remaining 17 cover the paper's other findings:
  - 12 use the postsubiculum recordings at DANDI:000939.
  - 1 uses the frontal-cortex recordings at CRCNS fcx-1.
  - 2 are model claims run from the repository's simulation code.
  - 2 use the slice-recording data, which were not deposited, so those claims will be blocked.

**Details the paper leaves open, and the readings named:**
- **Which units enter Figure 5F:** (a) all sorted units, as the RSC script does and as the legend's "570 units" implies; (b) excitatory units only, per the Methods' general rule. Both are run, and the claim is blocked if they disagree on sign or significance.
- **UP/DOWN states for Figure 5F:** the dandiset's own detected states if it holds them (its archive description says it does), with a re-detection by the code's procedure shown as a check.
- **Panel 5F's form:** the legend says it is "Same as (D)", an Isomap plot, but the code draws a histogram of onset delay against PMR. Only the correlation is tested.
- **Fig 1E "99th percentile range":** 0.5th to 99.5th percentiles, or 1st to 99th.
- **Fig 1H units:** all good units, as the code does, or excitatory units only.
- **Fig 1J:** which bin gives the angle at the UP-to-DOWN transition (the last bin above threshold, or the mean of the last 150 ms), and the histogram bin width (10, 20 or 36 bins).
- **Fig S1J:** how dorsal and ventral halves are split (equal-width depth bins or a median split).
- **Fig 2F:** the window searched for the maximal gamma slope (0 to 150 ms, or ±250 ms).
- **Fig S2E:** the direction of the speed regression (delay on depth or depth on delay). The extracted text prints the speed unit as "mm/s", and the same extraction turns µ into "m" elsewhere.
- **Fig 3F:** "near zero" UD slope is not quantified, so the slopes will be reported.
- **Pynapple version:** a standard choice, which cannot change the outcome.

**Missing or inconsistent in the paper:**
- **ADN data:** the paper names no archive for the thalamic (ADN) dataset it reuses (ref. 14).
- **ADN statistics:** the ADN test is printed differently in the Results (U = 29, p = 0.016) and the Figure S2G legend (U = 30, p = 0.019); either is accepted.
- **Slice recordings:** the data are not deposited.
