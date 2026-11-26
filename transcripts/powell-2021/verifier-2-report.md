**Verifier report, round 2: Powell et al. 2021 (doi:10.7554/elife.60454), attempt powell-2021-01**

**1. Outcomes**

The claims file has 22 claims. The attempt record gives 22 outcomes: 10 reproduced, 4 partially reproduced, 4 not reproduced and 4 blocked (data_missing). I agree with all 22.

- **fig3-evoked-7-to-21-in-9-of-10, reproduced (assumed: true).** I agree. Cell 16 gives 9 of 10 under reading (a), counting the held bins as the criterion words it; only 901_086 fails. Requiring 21 C gives 8 of 10. Cell 17 shows that 901_062's last stimulation was at 19.0 C and its maximum temperature was 19.30 C, so 21 C was never tried. The assumptions are stated in the deviations and in a methods_unavailable finding:
  - a bin counts as held at 120 s or more;
  - a preparation whose warmest step was 19 C still passes.

  Both are reasonable. The 2-minute step comes from the Methods and from BurstPeriodsVsTime.m. The pass-through bins hold 0 to 14 LG periods in 20 to 105 s, so they cannot show a rhythm.
- **fig3s1-spontaneous-and-evoked-similar, now not reproduced (it was blocked).** I agree. Under the Methods burst rule only 901_080 is similar, under both readings (cell 20). So at most 2 of 4 can be similar whatever 941_006 shows. The result holds when all pre-stimulation periods at 11 C are used instead.
- **The other 20.** These are as in round 1, or as I recommended there. For fig6b-lg-start-counts, partially reproduced matches my round-1 rating.
- **Other assumptions.** No other outcome is marked `assumed`. None needs to be, because the open choices are shown under both options and do not change the outcome:
  - for fig6b-lg-start-counts, the denominator of the fraction;
  - for fig4c-q10-about-2, which bins enter the Q10;
  - for fig5e-lg-area-exceeds-dg, the SEM of bins with a single preparation.

**2. Text checked against the printed outputs**

Almost every number in the Result conclusions, the Summary, the README and the record's notes matches the printed outputs. These sentences do not:

- **Cell 21 (fig3s1), wrong logic.** The text says "…which would leave three of four possible if 941_006 were not similar". With 901_080 and 901_062 similar and 901_086 not, three of four needs 941_006 to be similar. The record's note does not repeat the error.
- **Cell 59, wrong number.** The text says "(0.37 for both together)". Cell 58 prints 0.361 for LG and DG together under the Methods rule; 0.387 is the code rule. The record's `measured` value of 0.36 is correct. The words "near the reported ~35%" are also loose for DG: 0.386 is just outside 0.35 ± 0.035, though the outcome uses the LG value of 0.339.
- **Cell 28, and the record's fig4c-q10-about-2 notes.** The sentence reads: "the per-bin LG Q10s from the pass-through bins grow larger … (up to 705 in 901_052), because those bins were crossed near 10 C". Two parts are not supported:
  - 705.065 is the per-preparation mean (`LG_all_bins_mT`), not a per-bin value. Per-bin Q10s with measured temperatures are not printed.
  - The measured temperatures at which the pass-through bins were crossed are not printed either, so "near 10 C" has no output behind it.

  This does not change the outcome.
- **README.** It says "about four minutes, most of it reading `evoked_data.mat`". Cell 1 prints 28 s for fetching and loading that file, and no total run time is printed.
- **Data-check text, minor and outside the conclusions.**
  - Cell 8 says "every raw file of each preparation is in the stacked data". The same sentence notes that 901_062's zip holds 101 files against 58 stacked.
  - Cell 7 prints "Spike times sorted in the file: True" from `all(True for _ in preps)`, which is always true and checks nothing.

The record states my round-1 reasons in my own words, accurately. One of those reasons was wrong: I wrote that p < 1e-5 is missed at "17, 19 and 21 C". Cell 39 shows a median p of 1.69e-6 at 19 C, so the author's correction to 17 and 21 C is right.

**3. Round-1 points**

All but problem 3 are fully resolved:

- **Problem 1 (fig3, counting rule):** resolved. Both counts are reported, the outcome is marked assumed, the 901_062 printout is added, and a methods_unavailable finding asks the authors which bins they counted.
- **Problem 2 (fig3s1):** resolved. Three preparations are tested and the pre-stimulation table covers all ten.
- **Problems 3 and 4 (claims-file issues):** handled correctly for the attempt. Variants are reported and the questions are put to a reader without changing the criteria.
- **Problem 5 (Q10 temperature):** resolved with the measured-temperature variant; the counts are unchanged.
- **Problem 6 (odd-temperature filter):** resolved. The dropped counts are printed: 0 of 64 stretches, 220 of 4128 LG starts, 3.6% of LG spikes and 9.2% of DG spikes.
- **Problem 7 (fraction denominator):** resolved; the reason is stated and the outcome does not depend on it.
- **Problem 8 (single-preparation SEM):** resolved with the count over the six bins with more than one preparation (1 of 6).
- **"Not checked" items:** the independent-draw run for fig5e is done (2 or 3 of 8 overlap).

What remains and bears on a conclusion:

- **The claims-file question from problem 3 is still open.** The paper's numbers come from the code's burst rule and sampling. Under those variants, three outcomes would change:
  - fig4c-q10-about-2 would become reproduced (8 of 10);
  - fig6b-lg-start-counts would become reproduced;
  - fig6b-lg-phase-locked would become reproduced, or nearly so, since its largest p is 4.5e-4 against a 4.4e-4 cutoff.

  That is for the reader to decide (questions/powell-2021.yaml).
- **fig3s1, first quantity (3 of 10 against 4).** This rests on the 10 to 12 C bin. 932_151 has 16 pre-stimulation LG periods at 9.83 to 9.93 C, so 4 of 10 have pre-stimulation bursting. The paper_inconsistency finding names only 941_006 as the fourth preparation. 932_151 is an alternative it should mention.
- **fig3s1, temperatures of the one similar preparation.** 901_080's evoked file 0012 is at 7.25 C, against 10.86 C for its spontaneous file. The script selects it, so the comparison is faithful to the paper, but the text should say so. It does not change the outcome.
- **Cell 21's logic error** (section 2) should be fixed.

**4. Critical findings**

No finding in the attempt record is rated `critical`. Findings 1 to 6 are major, major, minor, minor, minor, minor. Findings 7 and 8 have severity none, and findings 9 to 13 (code_mismatch, paper_inconsistency, methods_unavailable) have no severity.

Nothing in the printed outputs points to a critical data problem:

- cell 13 shows no recording deposited twice;
- cell 11 shows the stimulation mask and LG spikes, and the temperature and PD spikes, share their clocks;
- cell 7 shows the preparation identities match getEvokedData.m.

The date discrepancy for 932_151 (2019 in its header, 2017 in the Methods) is rightly minor.
