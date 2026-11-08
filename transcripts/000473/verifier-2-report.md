**Verifier report, round 2: Calvigioni et al. 2023 on DANDI:000473 (0.230417.1502)**

Counts are taken from the claims file and the attempt record. The claims file has 33 claims, and the record has one outcome for each. The record gives 11 reproduced, 4 partially reproduced, 2 not reproduced and 16 blocked (15 data_missing, 1 metadata_insufficient), so 17 claims are tested. Nine outcomes are marked `assumed: true`. My round-1 header said 18 tested and 15 blocked; that was my miscount, and my own round-1 table lists 17 tested.

**1. Outcomes**

I agree with all 33 outcomes. Comments where they are needed:

- **code-outputs-link** (partially reproduced, assumed): Agree. The assumption is the blocks 1 to 4 GLM period. It is stated, and it is reasonable because the code's tmu units match it (no tmu unit missing; 18 of 25 sessions identical against 4) (cell 9). Four of those 18 are sessions with no units on either side, so 14 of 21 sessions with units match. The criterion's "reproduced" branch also requires the session table's genotypes to be present, but the files label 216300 and 216301 Vglut2-cre. That would block "reproduced" even if 22 sessions matched.
- **fig4g-glm-units** (reproduced, assumed): Agree. The assumption (GLM period) is stated and reasonable.
- **fig4e-opto-modulation-genotypes** (partially reproduced, assumed): Agree. The criterion defines only "reproduced", so "partially" is a judgment, and the record explains it. The Npy failure depends on the seed: p < 0.05 in 5 of 10 seeds, Bonferroni p = 0.132, mouse-level p = 0.905 (cell 22). The record says this.
- **fig4g-opto-tuning-score** (not reproduced, assumed): Agree. The Esr1 corrected p is 0.072 to 0.11 over all seeds, with the LFP series, and 0.159 on the code's own scores (cell 31). This fails even the "partial" branch.
- **fig4g-tuned-unit-counts** (partially reproduced, assumed): Agree for seed 0. 4 of 10 seeds would give "reproduced" (cell 29). The record says so, so the outcome sits on a boundary that the seed decides.
- **ed7bd-latency-similar** (reproduced, assumed): Agree under the pre-event baseline. The baseline-window assumption is stated and is a literal reading of "pre-event baseline".
- **ed8r-comodulated-units** (reproduced, assumed): Agree. The assumption (GLM period) is stated only as a deviation, but the margins are large (cell 37).
- **fig4h-opto-clusters** (partially reproduced, assumed): Agree, as a conservative judgment. Taken literally, the criterion's rule (two opto clusters, each at least 90% Vglut2 and Esr1) gives "reproduced". The claims file does not say how the failed expected count of 1,770 enters the outcome. Its "partial" branch ("one cluster meets this") does not describe this case.
- **fig4jl-pl-esr1** (reproduced, assumed): Agree under the rule, as weak evidence. With measure 1 a tie, the outcome needs measures 2 and 3. Measure 2 holds only because the ranking is by magnitude (that choice is stated). Measure 3's PL lead (0.104 against 0.099) is smaller than the s.d. of about 0.02.
- **ed7a, ed8h, ed8o, ed9a, ed9bg, fig4i, fig4k** (reproduced) and **ed9no** (not reproduced): Agree.
- **The 16 blocked claims**: Agree. Cells 71 to 74 now support ed1j (0 of 5,046 non-PFC units have an LH label), fig2d (Ephys_Category codes 1 to 6 with no names) and the eye/pupil claims (one Npy mouse).
- **`assumed` flags**: ed8h, ed9bg and fig4i readings (a) and (b) also use the GLM-fitted units or tuned flags, but they are not flagged. Their margins make this immaterial.

**2. Sentences the numbers do not support**

- **Cell 41, the ed7bd notes, and the methods_unavailable finding on latency.** The text says: "With the pre-trial baseline (variant), the air-puff latencies agree in only 2 (3 s.d.) or 1 (2 s.d.) of 4 subregions." The finding says "only in 1 or 2". Cell 40 prints "reading 2 s.d.: regions with spread <= 20 ms, tone 4 of 4, air puff 2 of 4". It is 2 of 4 under both thresholds. This does not change the outcome.
- **Cell 19 and the fig4g-glm-units notes.** "Over the whole session, reading (a) gives 2,195, with Ctl, Npy and Esr1 outside 10%." The total is also outside: 2,195 against a limit of 2,139.5 (cell 18).
- **Cell 24 and the fig4e notes.** "These parts hold under every seed, period and saturation series shown." For Vglut2 and Esr1 this holds over seeds (cell 22). For sound 1 and air puff, tuned fractions and binomial tests are printed only for seed 0, the whole session and the LFP variant (fractions only). The claim is plausible at fractions of 37 to 64%, but no output shows it over seeds.
- **Cell 7, and the code-outputs-link notes ("With the Methods' saturation removal, 16 sessions match").** Cell 7 says "with and without the Methods' removal of spikes near LFP saturation". The removal in cell 9 is `s["clean"]`, which uses the code's 'spike saturation' series (helper `clean_spikes` default), not the Methods' LFP series. Cell 2 and the helper docstring describe this correctly.
- **README table and Summary (cell 75) against the record's flags.** The record marks ed8r-comodulated-units, fig4h-opto-clusters and fig4jl-pl-esr1 `assumed: true`. The README and the Summary list them without "(assumption)".

All other "**Result:" sentences (cells 11, 14, 19, 24, 27, 32, 35, 38, 41, 44, 49, 53, 56, 59, 63, 66, 69, 74), the Summary and README text, and the record's notes match the printed outputs. I checked every number they quote.

**My round-1 reasons in the record.** The `verifications` reasons state my round-1 points in my words, with my problems 1 to 4 and 6 to 12 merged into the per-claim reasons. There are two minor omissions:
- fig4e leaves out that the whole-session variant reverses Npy (p = 8e-12, lower) and that the code's own flags give p = 0.128.
- fig4g-opto-tuning-score leaves out that the criterion needs the tests to hold even for a partial outcome.

My problem 5 (the saturation series) is attached to no claim, and that is acceptable since it affected no conclusion.

**3. Round-1 points**

Resolved:
- 1: the GLM period is now stated in the helper and the GLM section. Only the cell 7 wording above remains.
- 2: Bonferroni, mouse-level and per-seed views have been added.
- 3: ten seeds are shown.
- 6: the block-4 contradiction is stated, and a question goes to a reader.
- 8: the false-positive rate is measured on null copies (0.23%).
- 9: recorded as a paper_inconsistency finding.
- 10: stated in the decoding section and the deviations.
- 11: described as the same kernel.
- 12: there is no curation column, recorded as a finding.
- Section C requests answered: the ed1j locations, the BioStudies listing, the 128514 description, and Supplementary Table 6 re-read.

Partly resolved:
- 5: the rationale is now given and the LFP variant runs through the four GLM claims with the same outcomes. It is not run for the other claims, and cells 7 and 9 and the record mislabel the series.
- 4: the count is now marked out of tolerance, the active-bin distribution is shown, and a question goes to the authors. The cause of the paper's 1,770 is still unknown.
- 7: the bootstrap, seeds and Ctl-referenced measure have been added, and the weakness is stated.

What remains that bears on a conclusion:
- **fig4h-opto-clusters:** the 1,995 against 1,770 gap is unexplained, so the clusters come from about 225 more units than the paper's. The claims file does not say how the count enters the outcome. Its criterion also puts z-scoring before the quality-control step, which differs from the code; the z-scored variant keeps 1,974, which does not change the outcome.
- **fig4e and fig4g-tuned-unit-counts:** both outcomes are set by seed 0. In 5 of 10 seeds Npy is not above Ctl, and 4 of 10 seeds reach 6 of 8 counts. Either outcome could flip with another seed.
- **fig4jl-pl-esr1:** "reproduced" rests on two leads that are within the noise, and ed9no contradicts PL specificity.
- **ed7bd-latency-similar:** the outcome rests on the baseline window, and the variant count is misreported (see section 2).
- **Claims file:** the ed9a statement's "similar ... in block 4" is contradicted by the data and not tested. This is pending the reader question; I report it and do not correct it.
