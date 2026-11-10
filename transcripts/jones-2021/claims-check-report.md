The checker passes and the file is ready for an attempt.

**Checker:** `claims/jones-2021.yaml: 42 claims, 42 quotes, 173 statistical values, 0 problems` (the first run gave 41 claims, 0 problems).

I read the paper's main text, Methods, legends and Tables S1 to S6. I also cloned the paper's code at the cited commit (63b1acb, tag v1.0.0) and checked the code details the criteria rely on.

**Changes, by claim**
- **Method M (header):**
  - The genotype test now uses the Methods' model, `feature ~ treatment:genotype + (treatment:genotype|animal)`. The code's `Genotype*Treatment` model is named as a variant.
  - The code's 5 SD threshold covered more than the file said. It also applies to SWR size, SWR frequency, SW amplitude, CSD and SWR-coincident SG power, and the code uses 3 SD for coherence.
- **swr-longer-100ms:** the criterion now counts SWRs longer than 100 ms, as the text says; the code's ">=" is a variant.
- **fig3f-swr-frequency-pv:** the model data are one mean per SWR. Table S3's degrees of freedom match the other per-SWR features, so the second reading (every interpeak value) is only a variant now.
- **tables2-detection-unchanged:** added the CA3 and DG rest MUA tests from Table S2, which the criterion already required.
- **tables2-rest-sg-pv:** added the SST-Cre CA3 and DG baseline tests. The text names no region, so the criterion now requires no SST-Cre change in any region.
- **figs2cd-sg-predicts-sw-frequency, figs4e-sg-fg-inverse:** added the R² values printed in the panels as expected values (0.55 and 0.44; 0.81 and 0.84). Each matches F/(F + df) from the legends.
- **figs3-ca3-swr-pv, figs3c-ca3-swr-rate-sst:** the code keeps only CA3 SWRs that overlap a CA1 SWR; the Methods don't say this. Both readings are now named. I also fixed a miscount: the claim has four effects, not "five".
- **figs3-dentate-spikes:** "ten parts" changed to the eight the statement has.
- **fig5f-sg-frequency-pv:** added the SST-Cre CA3 and DG tests that the "not SST+" part rests on.
- **fig5g-sg-theta-modulation:** the statement now includes the genotype difference the text claims. The criterion requires it in CA3 and DG only, since the CA1 legend p is 0.95.
- **figs5-theta-coherence-frequency:** "other ten tests" changed to nine.
- **figs6-double-unlike-sst:** the "at least half" rule was not from the paper. It is replaced by the eight SST vs P/S tests that the Figure S6 and S7 legends show as significant under Holm. Added the CA3 and DG FG-frequency tests for the double-suppression group.
- **tables6-sex-swr-size:** applying Holm to Table S6 would fail the paper's own p = 0.0046. The correction is now marked as open, with two readings.
- **New claim, figs4h-fg-theta-modulation-pv:** PV+ suppression dampens how strongly theta modulates fast gamma. The Results summary and the Discussion state it, and no claim covered it.

**Still open**
- **Table S6 correction:** with Holm, the paper's own SWR-size result fails. With no correction, five other features become sex differences the text denies.
- **Run coherence:** the code computes coherence both over all run periods and per time bin, so it doesn't settle which reading the paper used. Both readings stay.
- **Code's Holm step:** `HBcorrect.m` doesn't stop at the first failing test, so it can mark more tests significant than proper Holm. Method M's simpler threshold holds under both.
- **Histology and slice claims (fig1-tables1-expression, figs1ef-exvivo-cno):** these data are deposited nowhere. The schema's `data: elsewhere` means another public archive, so I tried it and reverted it.
- **sex-stratified-effects:** Table S7 is not under `paper/`, so its features and p-values are not recorded.

All of this is recorded under `checks` with `ready: true`. Nothing is committed.
