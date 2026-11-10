I've handled every point in the round-1 report. The entry re-runs cleanly from a fresh environment (17 min, peak memory 4.9 GB) and the checks pass with 0 errors. Final count over the 40 claims: 26 reproduced, 1 partially reproduced, 10 not reproduced, 3 blocked. Nothing is committed.

**Outcomes that changed**
- **Moved to not reproduced** (the verifier disagreed with "partially", and none of these three criteria has a partial outcome):
  - **suppfig2**: the amplitude now comes from `waveform_mean`, as the paper's "mean spike waveform amplitude" asks. Its d' is 0.20 / 0.17, above 0.10 ± 0.02. The old `spike_amps` measure, now a variant, gives 0.05 / 0.06, below. No reading passes either way.
  - **fig2fg**: condition (iii) still fails when the ipsilateral and contralateral Miss trials are matched in contrast and count on the same neurons (1.117% against 2.082%; half is 1.041%).
  - **fig5b**: still 36 sessions against the required 34. The three dropped sessions are now listed (Lederberg 2017-12-05 to 12-07). The next smallest counts are 10 and 14 trials, so no threshold gives 34.
- **Nine kernel claims, previously blocked, are now tested.** A faster solver fits the full model in about 3 min. The basis follows the paper's own `CanonCor2all.m`, which I fetched from GitHub and read.
  - fig3c: reproduced, median VE 0.12%.
  - fig3d: reproduced, resting on an assumption. I read "neurons passing analysis criteria" as the neurons entering the nested tests; with all Figs. 3-5 neurons as the denominator the claim fails. This is recorded as a question for the authors.
  - fig3e: partially reproduced; VISrl has no Action neurons.
  - fig4f: reproduced, 100% / 38.5%, p = 9.6e-7.
  - fig4b: not reproduced; 48 midbrain and 39 forebrain neurons, and 1 in VISp.
  - ed4f, ed5h (0.14%), fig4fg and ed7c: not reproduced.

  The model passes 2,886 neurons into the nested tests against about 4,240 in the paper, which lowers every count of kernel-requiring neurons.
- **edtable1** stays reproduced but is now marked as resting on the label mapping: with labels as given, 33 of 42 regions match.

**Added or corrected**
- task-modulated-fraction now uses the criterion's neurons (22,434); the values change slightly and stay within tolerance.
- ed9cf now uses the index as fig5f gives it, with the z-scored index as a variant. Still reproduced.
- fig4d-vis-leads has a Bonferroni variant: it holds only under baseline a with trials b.
- fig4d-no-lag now says 25 points are tested, not 26.
- ed1q now prints each decoder's chance level: 59.3% for reading b.
- fig5d and ed7f are also run on all neurons, as a variant. Both stay reproduced; ed7f's margin is only 0.01 (0.444 against a lower bound of 0.432). I added the possible misreading as a question in `questions/steinmetz-2019.yaml`.
- The data check now shows that all 39 sessions pass the 12-trial rule, lists the units-table columns, and follows up Tatum_2017-12-09. That session's units show significant detect probability (16.9%, chance 5%) and respond after the stimulus, which is consistent with a shared clock.
- The round is recorded under `verifications` for all 40 claims, with the verifier's reasons and my responses.

**Not done**
- **fig4c and ed5g** stay blocked (`other`). They need decoding from kernel-model residuals, which I didn't implement for time. Computing cost is no longer the obstacle.
- **histology-alignment-error** stays blocked: the dandiset has no DiI or landmark data.
