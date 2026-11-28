The attempt is recorded and handed over: 33 of 34 claims tested, one (the decoder comparison) tested without its GPFA part. `python tools/entry.py all` passes (check clean, notebook runs in 29.5 min), and the handover package is in `executed/sabatini-2024/handover/`. Nothing is committed.

**(1) Outcomes** (`attempts/sabatini-2024-01.yaml`)

| Outcome | Claims |
|---|---|
| Reproduced (9) | fig2c-condition-lds-variance, tbf-variance-explained, fig4b-plane-alignment, suppfig6c-location-distinct-from-rotations, fig5c-rotations-predict-rotations, fig6b-location-predicts-rotations, fig6e-kinematics-predict-location, fig7c-ldr-encoding, fig7c-standard-encoding-worse |
| Partially reproduced (16) | data-composition, jpca-fit-r2, jpca-variance-explained, fig3a-eigenvalue-clusters, fig3g-basis-frequencies, tbf-shuffle-control, fig3h-recoverability, fig4c-subspace-excursion-angles, fig4f-plane-alignment-explains-jpca, fig5a-frequencies-segregated, suppfig6a-location-alignment, fig6c-location-tracks-direction, suppfig7a-not-memorization, fig7f-ldr-decoding, trial-curvature-decoding, fig7f-decoder-beats-standard (GPFA decoders not run) |
| Not reproduced (9) | single-lds-variance, fig3c-eigenvalue-distance-auc, suppfig2-eigenvalues-from-kinematics, fig3i-duration-warping, suppfig3-model-comparison, rotation-orientation-dimensionality, fig4d-jpca-variance-correlation, suppfig6b-location-dimensionality, suppfig8-no-output-potent-dependence |
| Blocked | none |

The most notable differences from the paper:
- The rotations sit near 0.7, 1.6 to 1.8 and 2.7 to 3.2 Hz, not 0.5, 1.5, 2.5 and 4 Hz.
- Eigenvalues differ between conditions more than the paper reports: AUC 0.63 to 0.81, against 0.51 to 0.58.
- Rotation orientations and the state space location are much lower-dimensional than in the paper.
- One linear dynamical system across all conditions fits better here (77 to 82%, against 46 to 66%).

**(2) Dataset, assumptions, questions**

Version 0.260528.0919 is pinned: the paper cites none, and the two published versions list the same assets.

Findings about the data:
- **Units (major):** each array holds 96 units, one per electrode, with no single-unit, multi-unit or quality label. The paper used 79 to 118 sorted units per array.
- **Nitschke file clocks (major):** the file joins five recording segments whose clocks overlap. Trial times, hand timestamps and every unit's spike times jump backwards four times, so a trial's spikes cannot be found by time alone. Splitting by segment gives above-chance condition decoding in each segment. Segment 3 carries less condition information within itself (0.16 against 0.41 to 0.46), which looks like drift over the session.
- **Jenkins unit (minor):** one unit's spike train holds two runs, the second restarting at the start of the session. I merged and sorted them.
- **Hand units (minor):** hand position is labelled "meters" with a NaN conversion factor, but the values are millimetres.
- **No EMG (minor):** so suppfig8 removes the kinematic dimensions only.

Assumptions:
- Every analysis uses the successful trials with a delay above 400 ms, because those counts are nearest the paper's. This is marked `assumed: true` on every analysis outcome.
- The penalty of 0.1 on the standard kernel encoders. With it, those encoders predict only the mean, so fig7c-standard-encoding-worse rests on the linear comparisons.
- The SEA noise level, the span of the time shuffle, and the subset size for the kernel decoders.

Questions for the paper's authors are in a `methods_unavailable` finding:
- the trial selection;
- which units were used;
- the kernel penalty;
- how the SEA noise angles were computed;
- whether the Supplementary Figure 3 comparison is cross-validated.

No questions were put to a reader.

**(3) Protocol gaps**
1. Running every reading of a choice that applies to every claim (the trial selection) would double a 30-minute notebook. I ran both readings only for data-composition and marked the rest as assumed.
2. Requiring five seeds on every random null multiplies run time. For the eigenvalue nulls I used 100 repeats instead of the Methods' 500, and 20 repeats for the four extra seeds; these are recorded as deviations.
3. The clock check does not cover a file made of segments with overlapping clocks. I checked per segment, and also with a decoder trained on the other segments; segment 4 (22 trials) is too small to check on its own.
4. Conclusions must be written after the outputs, and any edit forces a full re-run, so each change cost about 30 minutes. The protocol's time guidance does not mention this.
5. Some criteria have no "partially" clause (fig3a, fig3g, fig3h, fig6c). I used the protocol's general definition.
6. The direction of a signed-rank result is undefined when median and mean disagree (fig5a, M1-N 3.23 Hz). I counted it as not shown and gave both numbers.
7. archives.md says to read files with pynwb; I read them with h5py directly.

**(4) Runtime and failures**
- About 3 h 15 min of the 5 h (10:35 to 13:50 UTC).
- Three clean runs of the notebook, about 29 minutes each, all passing.
- Early development runs were too slow (about 25 minutes per part). I fixed this by running independent fits in parallel processes and replacing one loop with a closed form.
- Nothing failed in the final runs.
