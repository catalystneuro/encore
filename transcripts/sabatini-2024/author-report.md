I finished steps 1 to 5 and the handover (step 6). The entry is at `entries/sabatini-2024` and the record at `attempts/sabatini-2024-02.yaml`. Both notebooks ran clean through `entry.py all`, and `check` reports 0 errors. One thing is left undone: the notebook 1 header puts the version number in bold, which your rules don't allow. I saw it at 02:11, too late for another 46-minute run, so the next revision needs to remove it.

**(1) Outcomes** (34 claims: 13 reproduced, 10 partially reproduced, 10 not reproduced, 1 blocked)

| Outcome | Claims |
|---|---|
| reproduced | tbf-variance-explained, tbf-shuffle-control, fig3h-recoverability, jpca-variance-explained, fig2c-condition-lds-variance, suppfig6c-location-distinct-from-rotations, fig5c-rotations-predict-rotations, fig6b-location-predicts-rotations, fig6c-location-tracks-direction, fig7c-ldr-encoding, suppfig7a-not-memorization, fig7c-standard-encoding-worse, fig7f-ldr-decoding |
| partially reproduced | data-composition, fig3g-basis-frequencies, jpca-fit-r2, fig4b-plane-alignment, suppfig6a-location-alignment, fig5a-frequencies-segregated, fig4c-subspace-excursion-angles, fig4f-plane-alignment-explains-jpca, fig6e-kinematics-predict-location, trial-curvature-decoding |
| not reproduced | fig3i-duration-warping, single-lds-variance, fig3a-eigenvalue-clusters, fig3c-eigenvalue-distance-auc, suppfig2-eigenvalues-from-kinematics, suppfig3-model-comparison, fig4d-jpca-variance-correlation, rotation-orientation-dimensionality, suppfig6b-location-dimensionality, suppfig8-no-output-potent-dependence |
| blocked (too_large) | fig7f-decoder-beats-standard: single-trial kernel decoders need about 10^10 kernel entries (80 GB), and the paper gives no GPFA settings |

**(2) The dataset, assumptions and questions**
- **Version:** I pinned 0.261122.2046. The paper cites no version, and the two sessions it names are in that version.
- **Matches the paper:** 72 conditions (36 straight, 36 curved). Trial counts are within 10%: monkey J has 1595 successful trials (paper 1469), monkey N has 2121 (paper 2014).
- **Units (major finding):** the units are unsorted threshold crossings, 96 per array. The paper used sorted single and multi-units (79 to 118 per array), and that sorting is not in the dandiset.
- **Missing column (minor):** two Nitschke sessions not used by the paper (2010-09-20 and 2010-09-22) have no `maze_condition` column.
- **Checks that passed:** trials, spikes and hand share one clock, and no session is deposited twice.
- **Paper findings:** the published code's dimensionality cross-validation can't choose k, because `idDynamics.m` returns the training data as its approximation. Several code pieces are also missing from the repository (the kinematic basis, the Figure 6e regression, GPFA, the 250 ms warp).
- **Assumptions:**
  - Trials are aligned on `move_begins_time`.
  - Hand positions are taken relative to the start of the reach (marked `assumed` on the kinematic claims).
  - jPCA is written from the codepack's published description, because the codepack is not in the paper's repository.
- **Questions for the paper's authors:** which movement onset they used, whether positions were start-relative, and which jPCA version and parameters.
- **Questions to a reader:** none.

**(3) Protocol points**
1. The rule that every random result runs under five seeds conflicts with the 60-minute notebook limit for heavy resampling. I used fewer folds or repeats for the extra seeds, and skipped the extra seeds on 7 claims; each case is recorded as a deviation.
2. Three steps ran with fewer repeats than the Methods or the code for time, each recorded as a deviation: the eigenvalue nulls (150 and 30 repeats instead of 500), the noise for the excursion angles (36 half-splits instead of 200), and the code's 3/4 split (20 folds).
3. When the Methods and the code describe different procedures and the code is broken (the dimensionality cross-validation), the protocol says nothing about what to do. I ran both the Methods' score and a working LDS score; they agree.
4. Any edit to the entry, even to markdown, forces a full re-run. With conclusions written after the run, that cost two extra 46-minute runs.
5. It is unclear whether a finding's `output` can point at a tag that several cells share. My "checks passed" finding points at `sanity`.

**(4) Runtime and failures**
- Notebook 1 takes 37 minutes and notebook 2 takes 8.4, with peak memory 3.4 GB.
- An early development run that used a fork-based multiprocessing pool hung, and its 50-minute timeout killed it. I removed the pool and ran everything serially.
- The first full run failed on the two sessions without `maze_condition`; I fixed that and the re-run passed.

**Accidental exposure:** the version's DANDI release notes, which I read as dataset metadata, list conversion fixes linked to shenoy-lab-to-nwb issues #9 to #13. These may come from earlier attempts. I did not open the issues, and I saw no earlier results.
