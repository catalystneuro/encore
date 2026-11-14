The file is ready for an attempt (`ready: true`). I changed only `claims/gao-2018.yaml` and did not commit.

**Checker result:** `claims/gao-2018.yaml: 45 claims, 45 quotes, 21 statistical values, 0 problems`. The first run gave 44 claims and 0 problems; the count is now 45 because I added one claim.

**Changes, by claim**
- **fig1d-fastigial-lesion-contra-choice:** Fig. 1d plots each mouse separately, so the criterion now says it is open whether the p < 0.001 marks are per mouse or pooled over the 4 mice, and runs both.
- **fig1e-fastigial-lesion-slow-initiation:** the statement now includes bout duration (Extended Data Fig. 1c). For "not affected by lesion", it is now open whether the comparison is before against after the lesion, or contralesional against ipsilesional bouts.
- **fig1d-dentate-lesion-no-effect:** the file called p < 0.05 the legend's lowest mark, but Fig. 1d defines only p < 0.001. The threshold is now justified by the paper's other "no effect" statements (p > 0.05). The criterion had not tested the "movement execution" half of the statement, and the paper shows no dentate data for it; it is now tested, with the test named as a choice.
- **fig1h-fastigial-activation-delay-bias:** the supplement's mouse table puts Fig. 1h under both the 0.455 s and the 1.255 s stimulus, so both are now readings. The per-mouse bootstrap is named as a choice, since the paper gives no per-mouse test.
- **fig1g-dentate-activation-little-effect:** I removed the expected value on the p-value; the file itself said it would not be judged. The stimulus length is now open: the Methods put Fig. 1g under the 0.455 s experiments, but the table lists the 8 dentate mice only under 1.3 s.
- **fig1j-photoinhibition-silences-fastigial:** "most" and "few or none" are replaced by stated thresholds, with the test named as a choice.
- **fig1k-inhibition-delay-bias:** the file said 7 mice, but whole-delay inhibition was done in only 3. Both readings (0.5 s in 7 mice, 1.3 s in 3) are now given.
- **E5 (shared latency method):** the paper describes this method only for CN photo-activation, so using it for the Fig. 3 latencies is now marked as an assumption.
- **fig3b-cn-net-disinhibition:** the paper does not say whether the binomial test is one- or two-sided; this is now stated.
- **fig2cd-selectivity-emerges-gradually:** noted that the CN count of 197 equals 35% of 564 and equals 87 + 50 + 60 from Extended Data Fig. 4f. This supports the reading "neurons with sample or delay selectivity".
- **fig4e-fastigial-activation-abolishes-alm-selectivity:** the per-neuron "abolished/new" test is now named as a choice; the paper gives none.
- **ed10c-alm-inhibition-endpoints-predict:** the supplement presents this as an earlier finding and cites Li et al. 2016 and Inagaki et al. 2017, so its trials may come from those studies.
- **Opening comment:** added the unilateral ALM photo-inhibition stimulus from the Methods.
- **New claim, ed4f-preparatory-all-nuclei:** the Results sentence "Preparatory activity was present in all three cerebellar nuclei" (Extended Data Fig. 4f, n = 87, 50, 60) had no claim.

**Open**
- The paper does not say whether the ALM photo-inhibition trials in Extended Data Fig. 10c are its own recordings or reused from those earlier studies. The claim's `data` field is left at its default.
- The paragraph numbers in the sources could not be checked, because the stored text has no paragraph breaks.
- The 64.1 ± 3.4% and 27.0 ± 4.2% tolerances use the stated spread, which the paper does not say is an s.e.m. or a standard deviation.
