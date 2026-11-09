# Round 3 verifier report: 000939-duszkiewicz-2024-01

I agree with the one proposed change: ed8cd-multiplicative-detectable should move from partially reproduced to reproduced.

The claims file has 34 claims and the attempt record has 34 outcomes. Only one outcome carries a `proposed` entry, so that is the only claim reviewed here.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| ed8cd-multiplicative-detectable | reproduced (from partially_reproduced) | Yes | — | See below (cells 81–83). |

## ed8cd-multiplicative-detectable

**The numbers come from the data (cell 82).**
- The simulation starts from the ArchT FS cells' own unsmoothed OFF curves (6° bins). It uses reading (c), which keeps cells with a significant tuning correlation.
- Factors are computed as for the data: the slope and intercept of a polyfit of noisy ON on noisy OFF, both divided by the noisy OFF maximum.
- The noise is titrated on a grid of 1–12 Hz in 0.25 Hz steps. It lands at 4.25 Hz, where the no-gain median r is 0.731 against the observed ArchT FS median of 0.730. That median is the data's `r_tc`, not a fixed constant.
- The printed outputs match every number in the `proposed` reason and the notes:
  - With titrated noise against the simulated control, the multiplicative simulation's multiplicative factors give p = 0.0222.
  - The additive simulation gives additive p = 7.55e-5 and multiplicative p = 0.127.
  - The titrated no-gain simulation against the recorded control gives p = 0.00257 and 0.0392.
  - Over 50 seeds all three conditions hold in 80% of runs. The multiplicative simulation is detected in 98%, the additive in 100%, and the additive simulation leaves the multiplicative factor unchanged in 82%.
  - In the data, FS multiplicative against control gives p = 0.272 and additive p = 3.3e-4.

**The criterion is applied as written.** The criterion says the Gaussian noise is "titrated to the observed distribution of baseline-high-gain correlations". The code's fixed noise of 1.8 × 1.8 Hz is not titrated: it gives a simulated r of about 0.82 against the observed 0.73. So it is a variant, not a reading the criterion asks for. Counting it in round 1 was my mistake, as I said in round 2.

With titrated noise, only the choice of control group is left open. The criterion says only "the control group's", with n = 38, and both the simulated and the recorded control come from the same 38 control FS cells.

**The choice was not made to reach the result.**
- Both control readings were already in the round-1 notebook, so the simulated control was not added afterwards.
- The reason for preferring it is a check that does not depend on the outcome. With no gain added, a simulation should not differ from its control.
  - Against the simulated control it does not (p = 0.114 and 0.094).
  - Against the recorded control it does (p = 0.0026 and 0.039). The recorded comparison therefore picks up a mismatch between the noise model and the recordings, not gain.
- The seeds (8, 80, 81 and 1000–1049) follow a plain pattern and do not look picked. The criterion calls the seed "a standard choice", and the result holds in 80% of seeds.

**Caveats, none of which changes the outcome:**
- **The control built "as Figure_GainSimulation.m builds it" is unchecked.** That control is ON = OFF plus noise. The MATLAB code is not among my materials, so this rests on the notebook's description (cell 81).
- **The titration does not quite hold in the main run.** It was done with seed 80. In the seed-81 run that decides the outcome, the simulated median r values are 0.69–0.71, slightly below the observed 0.73. The match is "similar" but not exact; the 50-seed rate covers this spread.
- **The result is not robust to every seed.** It holds in 80% of seeds, and in most of the other 20% the additive simulation also moves the multiplicative factor. The record and cell 83 both state this.

I found no place where the claims file misreads the paper for this claim.
