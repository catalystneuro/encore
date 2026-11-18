## Verifier report: Okuno et al. 2025 on DANDI:000727, round 2

Counts are taken from the files. The claims file has 30 claims. The attempt record has 30 outcomes: 14 blocked, 10 reproduced, 3 partially reproduced and 3 not reproduced. Eight outcomes carry `assumed: true`: fig3d-flyem-vs-flywire, fig3e, fig3g, fig4e, fig4f, fig4i, fig5b-walking-activation and fig5b-walking-suppression.

The main finding of this round is that the notebook was re-executed but its text was not updated. Almost every FC and GLM number in the "Result:" cells, the Summary and the record's notes and `measured` fields comes from an earlier run. The numbers in this run's printed output are different. Every outcome still holds on this run's output, but the stated values do not match it.

### 1. Outcomes

I agree with all 30 outcomes as stated, with these remarks:

- **fig3d (partially reproduced), agree.** Cell 19 prints FlyEM 0.5925 and FlyWire 0.5557: FlyEM is higher, and both values are below tolerance. The record's `measured` values (0.6161, 0.5808) are not this run's.
- **fig3e (reproduced), agree, but it is fragile.** Cell 23 prints 55. Across runs the count has been 54 (round 1), 53 (record) and 55 (now), against a lower bound of 52.2. It falls out of tolerance with left and right swapped (44) and with no nuisance removal (48). The record's `measured: 53` is not this run's value.
- **fig3g (not reproduced), agree.** Cell 26 prints ACh r = −0.072 (p = 0.573) and GABA r = −0.067 (p = 0.601). The record's `measured` values (0.033, −0.17) are not this run's.
- **fig4e, fig4f (reading a) and fig4i (reproduced), agree.** In cells 30, 32 and 34 the MAIN line is True/True for all three. For fig4i, the synapse p = 1.4e‑4 is below 8.3e‑3.
- **fig5b-walking-activation (reproduced), agree under reading (a).** Cell 38 prints True for all four neuropils, both atlases and both regressors.
- **fig5b-walking-suppression (not reproduced), agree.** Cell 41: no voxel is below −3.24 (minimum −1.45).
- **fig3a (partially reproduced), fig3c, figs3-1a and fig3f (reproduced), agree.** Cells 46–53 print values consistent with the notes.
- **fig4b (partially reproduced), agree with reservations.** The criterion defines no partial outcome for this claim, and the claims-file misreading I raised in round 1 is still open.
- **fig4h (reproduced), agree.** The mode is the 1–2 µm bin, and ACh plus GABA make up 0.756. The criterion says "pairs", but each reciprocal synapse is counted from both of its neurons. The presynaptic-only split (0.761) gives the same outcome.
- **fig4a and fig4c (blocked), agree.** The FlyWire halves hold (connectome notebook cells 10 and 13). `blocked_by: other` is honest: the FlyEM synapses are public but the DBSCAN was not run.
- **figs4-1ij (not reproduced), agree.** The FlyWire mean is 0.363, which is closer to 0.5 than to 0. The claim fails whatever the 0.25 bound and whatever the untested FlyEM half gives.
- **fig5-wagn (reproduced under reading b), agree.** The values are PPSSI 0.1332 and 22 ascending neurons at sc50 with at least 5 synapses each. At sc140 they are 212 synapses from the ANs, 65 to WPNb and a closest distance of 852.3 nm.
- **The 14 blocked outcomes, agree.** figs3-2cd is now `not_runnable` with a stated reason.

**The assumptions are stated.** Each of the eight outcomes lists them as deviations: the registration with no M1 motion or slice-timing correction, tCompCor taken from native voxels, the subject order, the left-right orientation, no Tukey taper, smoothing applied to the betas, and the README's cluster extent. Two of them are weaker than the record says:

- **Registration repeatability.** Cell 2 says repeated registrations "differed slightly" and that results "can move in the second or third decimal". Cell 9 contradicts this: a second seed moves native voxels by a median of 0.88–25.4 µm per fly, and the ROI series of the two registrations correlate at a median of 0.41–0.98. The changes between runs (fig3d r by about 0.024, fig3e by 2 regions, per-region r by about 0.07) confirm it.
- **Orientation.** The per-region check supports no flip: r = 0.637 as registered against 0.404 swapped (cell 23). The voxel-wise GLM comparison in cell 43 points the other way, at 0.373 as registered against 0.40 flipped. Neither the notebook nor the record mentions this.

A smaller point: the deviation "Native voxel size from the NWB grid_spacing (2.55 to 2.61 by 2.61 to 2.68 by 5 um)" implies a per-fly spacing. `NATIVE_SPACING_MM` (flyfc.py:87) is fly-087's spacing, used for every fly.

### 2. Statements the printed numbers do not support

**reproduce_okuno_2025.ipynb**

- **Cell 21:**
  - "r is 0.616 for FlyEM and 0.581 for FlyWire": printed 0.5925 and 0.5557.
  - "no nuisance removal 0.630 against 0.592": printed 0.6310 and 0.5987.
  - "nine flies 0.608 against 0.573": printed 0.5973 and 0.5604.
  - "synapse SC 0.562 against 0.535": printed 0.5405 and 0.5162.
  - "second registration (0.611 against 0.570)": printed 0.5991 and 0.559.
- **Cell 24:**
  - "53 of 63 … 53 with nine flies and 55 with the second registration": printed 55, 54 and 56.
  - "swapped … 43": printed 44.
  - "without nuisance removal it is 50": printed 48.
  - "r = 0.704 as registered and 0.414": printed 0.637 and 0.404.
- **Cell 27:** "r = 0.033, p = 0.80" and "r = −0.170, p = 0.18": printed −0.072 (p = 0.573) and −0.067 (p = 0.601).
- **Cell 31:**
  - "0.636 against 0.598, z = +23.9, p = 3e-126": printed 0.6147 against 0.5777, z = +22.6, p = 1.4e‑113.
  - "0.586 against 0.570, z = +6.6, p = 3e-11": printed 0.5660 against 0.5513, z = +6.4, p = 1.3e‑10.
  - "z = −9.0 and −10.6": printed −6.0 and −8.4.
  - "p = 5e-45" and "p = 0.88": printed 1.95e‑44 and 0.935.
- **Cell 33:**
  - "0.579 against 0.584, z = −5.6, p = 2e-8": printed 0.5553 against 0.5592, z = −5.3, p = 1e‑7.
  - "0.529 against 0.545, z = −11.7": printed 0.5118 against 0.5256, z = −10.0.
  - "(p = 0.93)": printed 0.827.
- **Cell 35:**
  - "0.640 against 0.601, z = +23.9": printed 0.6198 against 0.5808, z = +24.2.
  - "0.582 against 0.574 … p = 0.00016": printed 0.5633 against 0.5552, p = 1.4e‑4.
  - "Without nuisance removal the synapse SC is below the null (p = 0.0002)": printed p = 0.0232, which is not significant at 0.05/6.
  - "(p = 0.00025)": printed 2.9e‑4.
- **Cell 40:**
  - "396,982 voxels": printed 389,784.
  - "maximum t = 20.9": printed 18.18.
  - "the paper's deposited map 416,801": no cell prints the deposited positive cluster.
  - "Reading (b) fails for LAL (rank 23 of 63 at best)": cell 38 prints reading (b) True for LAL with the graded regressor (ranks 19 and 17). It fails only with the binary regressor, and for GNG with the graded regressor under JFRC2010.
  - "r = 0.447": printed 0.565.
- **Cell 44:**
  - "the lowest t is −1.74": printed −1.45.
  - "87 to 100%": printed 88–100 %.
  - "t = 3.32 and 4.62": printed 3.67 and 4.04.
  - "r = 0.363 (0.390 …)": printed 0.373 (0.40).
- **Cell 54 (Summary):**
  - "53 of 63": printed 55.
  - "0.581 against 0.684": printed 0.5557.
  - "r = 0.36 voxel by voxel": printed 0.373.
  - "median of 3 to 35 um": printed 0.88–25.4.
  - "median of 0.30 to 0.98": printed 0.41–0.98.
  - "8 ROIs partly outside … AL(L) 59% inside": cells 7–8 print 30 ROIs, AL(L) 0.05 and ROB(R) 0.00.
- **Cell 2:** "differed slightly … second or third decimal" is contradicted by cell 9.

**Attempt record notes.** The same stale values appear in:

- the notes and `measured` fields of fig3d, fig3e, fig3g, fig4e, fig4f, fig4i, fig5b-walking-activation and fig5b-walking-suppression;
- the orientation deviation, "(FlyEM 0.514 against 0.603)": printed 0.5103 and 0.5925;
- the registration deviation, "3 to 35 um";
- findings `methods_unavailable` ("0.581") and the fly-100 `other` finding ("8 hemibrain ROIs partly outside … AL(L) 59%"), and the deposited-GLM finding ("one positive cluster of 416,801 voxels", which is not printed).

The fig3d response's "tested on one fly (sub-voxel in-plane motion)" has no output in either notebook.

**Supported by the printed output:** connectome_okuno_2025.ipynb cells 4, 8, 11, 14, 17 and 20, and reproduce_okuno_2025.ipynb cells 47, 49, 51 and 53.

**README.** The outcome table agrees with the record, and its rows account for all 30 claims. It quotes no numbers that could be stale.

**Round-1 reasons.** The `verifications` block states my round-1 reasons for all 30 claims, condensed and faithful to my wording.

### 3. Round-1 points

**Resolved:**

- 5: the unjustified blocks are now tested (fig4h, fig5-wagn, figs4-1ij, and the FlyWire halves of fig4a and fig4c).
- 7: the FlyEM confidence-0 gap in fig3a is now stated.
- The cell 6 wording of point 2.
- The C items on the suppression map and the permutation tests: the paper's deposited t map and R values are now loaded and compared.

**Partly resolved:**

- 1 (motion and slice-timing correction): now stated everywhere, but not applied.
- 2 (orientation): the per-region check supports it, but the voxel-wise GLM comparison points the other way and is not mentioned.
- 3 (fragile permutation outcomes): the fragility is stated, and the deposited z values are shown.
- 4 (GLM differences): compared with the deposited map, but the Tukey taper and motion correction are still missing.
- C (registration repeatability): tested, and the variation is large.

**Open:** point 6 (fig4b count) is referred to a question for a reader, as is appropriate.

**What remains that bears on a conclusion:**

1. **The text describes another run.** The conclusions, Summary and record must be regenerated from this execution, or the notebook must be made deterministic. The outcomes do not change, but the fig4i no-nuisance statement and the fig5b-activation reading (b) statement reverse.
2. **The registration is unstable.** The second seed moves voxels by up to about 25 µm (median), and fig3e sits 1–3 regions above its bound across runs. fig3e's "reproduced" is therefore not robust. Its note should say so in terms of this instability, not "second or third decimal".
3. **Motion and slice-timing correction (M1) are still missing.** fig3d, fig3g, fig4e/f/i and fig5b-suppression all rest on uncorrected data. Whether the raw series needs the correction is still not shown in any output.
4. **The orientation evidence conflicts.** As registered: per-region r 0.637 against 0.404 swapped. Voxel-wise GLM: 0.373 against 0.40 flipped. fig3e and fig4e's synapse result depend on this choice.
5. **fig4b:** the claims file's quantity, neurons with a PPSSI = 139,255 with tolerance 0, may misread the paper's count of neurons the index was applied to.
