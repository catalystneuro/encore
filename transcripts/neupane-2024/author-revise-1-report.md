I finished the round-1 revision. The entry passes its checks, and the full notebook re-ran cleanly in 1,483 s. Nothing is committed.

**Outcomes that changed**
- **ed2c-pi-error-below-correct**: partially reproduced → not reproduced (rests on an assumption). After the null fix, only 1 of 4 groups reaches p < 0.0001 under either neuron selection, and none does once correct trials are cut to the error-trial count.
- **fig2f-earlier-peaks-multiples**: partially reproduced → not reproduced, which is the verifier's outcome. No reading puts the third peak near -1.95 s.
- **fig3d-offset-coding-stronger**: partially reproduced → reproduced (rests on an assumption). The verifier was right that the regression has an artefact, but the Methods do centre across both windows. I adopted per-bin centring from the method the paper cites (Mante 2013). Under it, offset R² is higher than onset R² in both monkeys. Under the Methods' own centring, monkey M still reverses, and that question is now a finding for the paper's authors.
- **ed5-xcorr-conserved-other-epochs**: blocked → reproduced (r 0.78 to 0.95), as the verifier said it could be tested.
- **fig4g-reset-model-fits-better**: blocked → partially reproduced. The reset model is better in all 15 sessions, but with only 6 and 9 sessions the paired test reaches p 2.5e-4 and 1.1e-3, not the p < 0.0001 bound.
- **fig4d-model-subscalar-variability**: blocked → not reproduced. I ported the paper's model from its MATLAB code. Under the paper's fit, the model without landmarks also has an exponent significantly below 1; under the code's fit the criterion would be met.
- **ed3-no-eye-hand-periodicity**: kept as reproduced, with the verifier's disagreement recorded. Its first reason no longer applies, because monkey M is now included and the test is met in both monkeys under every reading. The mean PIs are still outside tolerance; the criterion only asks for them to be reported.

The other outcomes are unchanged. The counts are now 6 reproduced, 7 partially reproduced, 4 not reproduced and 7 blocked.

**What I added or corrected**
- **Surrogate null:** draws now come at random from a wide pool, and each unit's null uses as many trials as the unit keeps. The code's GP null without the Poisson step runs as a variant. The notebook prints thresholds per group and compares the null with one generated afresh (0.150 to 0.154 against 0.141).
- **fig2 under the fixed null:** the main reading now gives A 15.7% and M 7.8%, so fig2 stays not reproduced.
- **Every claim that uses periodic units** now runs under four periodic sets: the main reading, rule a1, rule b and the GP null.
- **Clock offset:** the eye and joystick clock offset is estimated from the joystick trace for the 10 sessions on another clock, after checking the estimate on the 5 sessions that are on the trial clock.
- **Extra outputs the verifier asked for:**
  - the trial table's columns, and the evidence that `attempt` 2 rows hold the first attempt;
  - a matched-trial control for ed2c;
  - the false-positive rate of the Fano selection for ed8;
  - a trial-level t-test for ed10, which finds only about 6% of units motor-related against 68 to 76% with the bootstrap test;
  - intervals between peaks for fig2f;
  - results without the three sessions whose clock could not be checked;
  - fig3d without distance 1.
- **Records:** `questions/000897.yaml` is new and asks whether fig4d's Weber fraction should be 0.08 where the claims file says 0.8. The code's file naming implies 0.08, and 0.8 cannot be run. The attempt record now has the round-1 `verifications` block, updated findings, the README and `entry.yaml`.

**Not done**
- fig4b-learned-landmark-input and ed6d-model-fano-periodic are still blocked. Each needs a long simulation that would push the notebook past the 30-minute limit; it now runs in about 25 minutes.
- ed5efg-tighter-phase-clustering stays blocked because the model's side was not simulated.
- I kept one shared surrogate firing rate per monkey, since the verifier found the threshold barely depends on rate.
- To port the models I cloned the paper's code repository at the commit the claims file cites. I used it only as a reference for the port; the notebook does not read it.
