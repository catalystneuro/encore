I've revised the attempt for every point in the round-1 report and re-run it. `python tools/entry.py all entries/000213-tingley-2018` passes in 690 s, and every conclusion matches the executed numbers. Round 1 is recorded under `verifications`, and nothing is committed.

**Outcome changes**
- **fig1i-hpc-rate-phase-equivalent:** reproduced → not reproduced. With the corrected place fields, the KS test over 531 fields gives p = 0.044, so the "no difference" claim fails. Over 42 sessions p = 0.61. It sits near the threshold: the old field set gives p = 0.097.
- **ls-few-place-fields:** not reproduced → partially reproduced. LS is 5.4% and hippocampus 10.5% (paper 31.7%); LS is lower at p = 9e-18.
- **ls-place-fields-unstable:** partially reproduced → not reproduced. Under neither reading of the paper's undefined variability measure are LS fields more variable.
- **fig6d-cfc-stronger-ca3:** reproduced → not reproduced. With the grouping the criterion actually states, CA3 > CA1 coupling gives p = 0.089, where the old p = 0.041 came from 19 sessions with no hippocampal units counted as CA1. Coupling still rises along the run in both groups.
- **fig5-assemblies:** blocked → not reproduced. On a random 1% of pairs (670), 5.2% form assemblies (95% interval 3.7% to 7.2%) against 18.5%, and the median window is 20 ms against 25.
- **ls-information-lower:** blocked → partially reproduced. LS is lower (0.63 against 1.49 bits/cm, p = 6e-287), but neither value is within tolerance.

The other 19 outcomes are unchanged.

**What I corrected or added**
- **Place fields (verifier's main problem):** the paper's code builds its place-field files from the Gaussian-smoothed rate maps (`scratch_07_25_17_calc_firingMaps.m`), so I switched from the box filter to a Gaussian with SD 4 bins. A Gaussian with SD 5, the old box map and the code's 1% threshold are shown as variants. That script names its file for a 20% threshold but passes none, so its 1% default applies; this is now a `code_mismatch` finding.
- **Theta reference:** no session has both `hpc` and `ca3` channels, so in the 11 `ca3` sessions the reference is necessarily a CA3 channel, which is what the paper's code does when a session has no CA1 channel. I added the spectral peak and theta contrast per session. Theta is weak in DT5, but repeating the phase claims on the 37 sessions with clear theta gives the same results (52.9% against 51.1%).
- **Decoder split:** I confirmed in the paper's per-cell decoder that it splits samples at random (`randperm` over all samples), which the main analysis follows.
- **Ensemble claim (figs7):** tests are now one-sided in each direction, with the mean differences printed.
- **Figure 6:** added per-animal tests within DT5 and DT9.
- **Depth claims:** added a pooled test using the second depth in the session name.
- **Data check:** it now prints what `allocentric_frame_tracking` holds. It is only a head-orientation quaternion, with its unit stated as metres (a new finding), and nothing marks a maze rotation.
- **Smaller fixes:**
  - Text now acknowledges that the LFP clock check is weak.
  - The RMS-smoothed peak rate is kept, because that is what the paper's function reports; its RMS smoothing is now zero-padded as in buzcode.
  - The summary miscounted the DT8 and DT2 files (it said ten and nine; both are eight).
- **Claims file:** I added criteria for fig5-assemblies and ls-information-lower before running them. The opening comment says they were written after all other results had been seen.

**What I did not do**
- **fig5g and fig6e stay blocked as `not_runnable`.** The verifier called that reason invalid and preferred `too_large`, but `not_runnable` is in the protocol's list. They need every pair, and the notebook now shows that takes about 23 process-hours at about 1.2 s per pair.
- **Which depth is the LS probe** remains an assumption, since no metadata settles it.
- **Choices with no source:** the peer-prediction bin size, kernel and window grid are my own, because the paper's assembly code is not public. They are recorded as deviations.

The paper text is saved under `paper/`. The runtime is now about 12 minutes, up from 8, and `entry.yaml` lists it as 15.
