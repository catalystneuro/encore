**Verifier report: jones-2021 on DANDI:000165 (0.211118.1526), round 2**

The claims file has 42 claims. The attempt record has 42 outcomes: 5 reproduced, 3 partially reproduced, 31 not reproduced and 3 blocked (data_missing). Eight outcomes are marked `assumed: true`. I found no new misreading of the paper in the claims file.

**1. Outcomes**

I agree with all 42 stated outcomes, with these qualifications:

- **fig6g-fg-frequency-sst (partially_reproduced).** I agree only under the pooled-frequency reading, and the outcome is not marked `assumed: true`. With one site per region, none of the three regions is significant (run cell 39: CA1 p=0.807, CA3 0.239, DG 0.327). Under that reading the outcome would be not_reproduced. The assumption is the same one that figs5-theta-coherence-frequency and tables4 rest on, and those two carry the flag.
- **tables2-rest-sg-pv (partially_reproduced).** As in round 1, the criterion defines no partial outcome. Read strictly, the SST CA3 and DG failures make it not_reproduced.
- **fig2ef-csd-sr (not_reproduced).** I agree under the 3 SD main reading. Under the code's 5 SD SWRs with reading (b), three of four effects hold, which meets the partial rule (csd cell 5). The notes say this.
- **figs5-theta-coherence-frequency and tables4-genotype-baseline (now reproduced).** Both rest on pooling peaks over a region's sites. The assumption is stated and reasonable: the pooled PV CA1 SG count is 980,169 (run cell 21), against 1,038,019 in Table S3. However, the README itself says p-values of these per-peak features are "less stable than their coefficients". The one-site p-values are 0.31 and 0.44, against 0.00056 and 0.00034 pooled, for similar mean differences.

The assumptions behind the eight flagged outcomes:

- **Reasonable:** fig3b and figs3-ca3-swr-pv (spike-clock shift, with a deposited-time variant), fig4d, fig4e and figs2cd (tapers and z-scoring; fig4d is not reproduced under both z-scorings).
- **figs3-dentate-spikes:** the assumption is stated, but its justification is wrong (see 2h). Table S4 gives a DS rate of 9.18 and 8.45 Hz. The 8.6/s found here supports the reading as implemented.

**2. Statements the printed outputs do not support**

a. **fig6g, one-site variant.** Run cell 40 and the record say "With one site per region it rises in DG only (p = 2.2e-08…)" and "Both readings give one or two regions of three". The printed DG p is 0.327, and no region is significant (run cell 39). The verification response repeats "one site per region gives DG only".

b. **P/S FG frequency.** Run cell 64 and the record (figs6-double-unlike-sst) say "FG frequency in CA3 (p = 8.5e-07) and DG (p = 1.8e-08)". The printed values are 1.35e-06 and 1.44e-08 (run cells 7 and 63).

c. **fig3f.** Rest cell 29 and the record say "p = 4.5e-05". The printed value is 4.82e-05 (rest cell 28). The verification response says "the numbers are the same in the new run".

d. **fig3g.** Rest cell 32 and the record say "p = 0.00207, just below … 0.00208". The printed value is 0.00202 (rest cell 31); the decision is unchanged. The record's "SST-Cre p 0.00016 to 0.0021" should end at 0.0020.

e. **fig2ef.** csd cell 6 and the record say "p = 4.4e-11". The printed value is 4.51e-11 (csd cell 5).

f. **fig5f genotype tests.** Run cell 22 says "No genotype test is significant (p from 0.11 to 0.998)". The printed values are 0.0496 to 0.998, and 0.0046 to 0.93 with 5 df (run cell 21).

g. **Sex interactions.** Run cell 58 and the record (sex-stratified-effects) say "p from 0.021 to 0.85". The printed maximum is 1.0 (SST fg_pow_dg, run cell 57).

h. **Dentate spikes.** Rest cell 62 says "far more than dentate spikes usually occur, so the detection likely differs from the paper's". The record's notes and its methods_unavailable finding say the rate "suggests a step is missing". Table S4 reports a DS rate of 9.18 Hz (PV) and 8.45 Hz (SST), so the paper's own rate matches the 8.58/s found here (rest cell 61).

i. **Record finding (metadata_error, cohort 3).** It says the empty vector mice "change with CNO in 3 rest and 7 run features". This is stale: the current outputs give 4 rest and 9 run features (rest cell 70, run cell 63).

j. **Stale text.** Rest cell 69 says "Rest features computed here (17 of the 24)". Cell 70 computes 22.

k. **fig4d inference.** Rest cell 44 says "so part of the rise comes from z-scoring a CNO session by another session's statistics". The empty vector rise in CA1 (p=1.6e-05) is equally consistent with session order. No output separates the two causes.

l. **Speed by session.** The record (running-speed-unchanged) says "Speed rises over the three vehicle sessions in every group". SST runs 4.43, 4.38, 4.55 and P/S runs 5.14, 4.72, 5.75 (run cell 60). Cell 61's "from the first to the third" is accurate.

m. **fig5b group count.** Run cell 13 says "no group has such sessions under both treatments from two or more mice". No output prints this count; only `holds None` is shown.

The README counts (5, 3, 31, 3) match the record. The README and the run Summary should say that fig6g also rests on pooled frequency.

The verification block states my round-1 reasons faithfully in my own words for every claim. One inaccuracy: "reviewed" says the conclusion cells were removed, but my round-1 report noted remaining author result cells (rest cells 41, 44 and 47; run cells 42 and 45), which I did not use.

**3. Round-1 points**

Resolved:

- **1 (blocked for lack of time):** CSD, fig4d, fig4e and figs2cd are now computed. 22 of 24 rest features enter the figs6 comparisons.
- **3 (freq_sites bug):** fixed. All 8 PV, 7 SST, 7 P/S and 8 EV mice have frequency values (run cells 21 and 39).
- **7 (0.195 scale text):** resolved.
- **9 (5-df genotype tests):** now printed with Holm decisions. None changes a decision.
- **10 (P/S skipped in the track sex interaction):** explained by the 6 female and 1 male track mice.

Partly resolved:

- **2 (track alignment):** `starting_time` is 0 in every file, and theta/delta against speed peaks near zero lag (mean r 0.134 at 0 and 0.161 at +2 s, against 0.009 beyond 30 s). 48 of 170 sessions still have their peak more than 2 s from zero. The position end minus LFP end still ranges from −92 to +1229 s and is not discussed (run cell 3).
- **4 (one site per region):** the pooled main reading plus a one-site variant addresses this. The outcomes of figs5-theta-coherence-frequency, tables4 and fig6g now depend on the reading; only the first two are flagged, and fig6g's variant is misreported (2a).
- **5 (SW amplitude):** the offset is ruled out (median raw LFP 39 against a median amplitude of 3274). The factor of about 8 against Table S4 remains unexplained and is recorded.
- **6 (spike clock):** the track check finds a clear peak in only 24 of 170 sessions. The fig5b run MUA therefore stays on deposited times. The "only at the edges" argument is weak for laps of about 7 s (36 cm at about 5 cm/s) if lags reach 1 to 2 s, although the median track lag is −0.245 s.

Not resolved:

- **11 (dentate spikes):** the amplitude is still in z units against Table S4's µV. The rate point I raised was answered "No change", but the conclusion and a finding now contradict it (2h).

Remaining issues that bear on a conclusion:

- fig6g: mark the outcome `assumed: true`, and correct the one-site result (2a).
- tables4, figs5-theta-coherence-frequency and fig6g rest on per-peak p-values the README calls unstable. Refits from several starting values, or the fitted random-slope variances, would show whether the pooled significance holds.
- figs3-dentate-spikes: correct the stated rationale for the assumption, and the question for the authors, in light of Table S4's 9.18 and 8.45 Hz.
- figs6-empty-vector-control and the cohort 3 finding: update to 4 rest and 9 run features. Note that fig4d's empty vector rise may come from session order and not only from z-scoring.
- Items 2b to 2g and 2i to 2m are text corrections. None changes an outcome.
