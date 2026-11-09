I checked the claims file against the full paper and made 16 corrections. I think it is ready for an attempt.

**Checker result** (same before and after my edits): `claims/crcns-alm-3/10.1038-nature17643.yaml: 29 claims, 29 quotes, 11 statistical values, 0 problems`

**Changes, by claim** (each is recorded with its reason under `checks`):
- **Header:** the reason given for which Experiment 1 window was recorded did not hold up. It now cites the Methods' list of recorded conditions and the Extended Data (ED) Fig. 5f naming.
- **fig1d-late-delay-ipsilateral-bias:** the paper does not say Fig. 1d is tested on contralateral-lick trials. That is now open, with two readings: contralateral-lick trials or all trials.
- **fig1d-earlier-photoinhibition-minimal:** a p-value between 0.05 and 0.1 was left undecided. Absence is now judged at the paper's p < 0.05 level, and the paired test is marked as a choice.
- **ed3-recovery-interval:** the "similar" part (ED Fig. 3e) had no criterion. I added one and stated it as a choice.
- **ed2b-silencing:** the criterion contradicted its own expected value and the paper's ">90%" per mouse line. It now requires a reduction of at least 0.81 for ipsilateral and bilateral photoinhibition and for each mouse line.
- **ed2e-no-rebound:** the population test now applies in each of the two windows after offset.
- **fig1f-rate-recovery:** one expected entry gave 168 neurons with tolerance 0 for all three conditions. Fig. 1f gives 168, 168 and 175, and the inclusion rule is open. It is now three entries with the default 10% tolerance.
- **fig2b-bilateral-behaviour:** the bilateral 1-spot against unilateral 4-spot comparison now uses the paper's test and level (two-tailed t-test, p < 0.05).
- **ed6-bilateral-bias-inconsistent:** "closer to" a control trajectory is now open, with two readings: the side of the decision boundary, or the nearer control mean.
- **fig2-bilateral-recovery, ed7-unilateral-4-spots-bilateral-1-spot, fig3-cd-roc:** margins and windows the paper does not give are now marked as choices.
- **ed7e-size-and-roc:** the bilateral tolerance of 0.08 assumed the printed "0.8" is a misprint. It is now the protocol default of 0.054, with 0.08 as a variant.
- **fig3-cd-predicts-movement:** the statement covers unilateral perturbation but the criterion did not test it. Full reproduction now needs all four conditions; control and bilateral alone count as partial.
- **fig5b-callosotomy-behaviour:** the comparison with 58.0% had no rule. It now requires the after-cut value to be within 10% of 58.0%.
- **fig5-callosotomy-recovery:** the number of laser spots in the callosotomy conditions is not in the paper and now comes from the data set's labels. What the cd selectivity is "reduced" against is now open, with two readings.
- **models-monolithic-fail:** the corrective-feedback integrator is silenced by current injection (ED Fig. 1g), not by clamping half the neurons. Using a module of the Fig. 6b model as the monolithic fixed-point attractor is now marked as a reading.

**What remains open:**
- The corrigendum (doi:10.1038/nature18623) was not supplied or read. It may correct a number used here, such as the ED Fig. 7e s.e.m.
- No PDF was supplied, so values printed only inside figures (Fig. 1d, 5b, ED Fig. 8a and 8b) were not read.
- Every quote, statistic and expected value I checked matches the paper, and every claim comes from this paper. The paper's main findings (Figs 1 to 6) each have a claim.

**Ready:** yes (`ready: true`).
