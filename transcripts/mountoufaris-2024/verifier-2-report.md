# Round-2 verifier report: 001131-mountoufaris-2024-01 (doi:10.1016/j.cell.2024.08.015)

The claims file has 36 claims and the attempt record has 36 outcomes. They split as: 3 reproduced (all assumed), 1 partially reproduced (assumed), 10 not reproduced, 20 blocked as data_missing, 1 blocked as metadata_insufficient and 1 blocked as other.

## 1. Outcomes

**I agree with all 36 outcomes.** That includes the two I disputed in round 1; the reasons are below.

- **figs4a-unilateral-no-behavior-deficit, reproduced (assumed).** I now agree. Attack probability is now run under four declared readings. The adopted reading (a) is an attack-triggered probability over 0–10 s, which fits how panel S4A(vii) is plotted against t (s) and the S2C/S3C "τ attack probability". The record states this reading and it is reasonable. The bout-rate reading (p = 0.036, experimental mice attack more) is reported. Two caveats:
  - The absence rests on 3 vs 5 mice.
  - Possible claims-file misreading (reported, not corrected). The extracted text of the Figure S4A image has two "*" marks among the "ns" labels ("% Time attacking … * … Interval (s) between attacks … *"). The claims file says every S4A measure is at p > 0.05, and its comment says S4 stars begin at "**". If two S4A panels are significant, most likely towards more aggression, then the paper's "no deficits" means no reduction, not no difference. The criterion "none differs at p < 0.05" would then be stricter than the paper. No PDF renderer was available here, so I could not tell which panels carry the marks.
- **figs4e-active-units-unchanged, reproduced (assumed).** I now agree. The baseline of all frames before the first behaviour is the claims file's reading (a). It is justified as the nearest stand-in for the 5-min home-cage baseline. It is now the same baseline that fig4ef and fig5bd use, so the two activity claims no longer rest on opposite readings. Under it, neither reading of "nested" finds a difference. The 7-s pooled difference is disclosed.
- **fig4ef-male-activity-slightly-lower, reproduced (assumed).** The pooled reading of "nested" and the assumed baseline are both stated. The new sensitivity check is honest: without mice 497, 510 and 500, the 7-s baseline fails (Mann-Whitney p = 0.051 and 0.060).
- **fig5bd-behavior-selective-units-reduced, partially reproduced (assumed).** Agree: the baseline assumption is stated, the directions hold and 3 of 7 values are inside tolerance.
- **figs5c-peth-activity, not reproduced.** Agree; this is now fixed as I asked.
- **Other not-reproduced outcomes: methods-unit-counts, figs5e, fig7c and the six rSLDS claims.** Agree.
  - **fig7b:** its criterion says "blocked as methods_underspecified if combinations disagree on … significance". Pooled and per-mouse tests disagree on significance, but that is a split between nested readings, not between the criterion's combinations. No combination reaches the expected values anyway, so not reproduced stands.
- **fig6e, blocked (metadata_insufficient)** and the 20 data_missing blocks: agree.
- **fig1e, blocked (other).** Agree. The claims file marks the atlas `with_inputs` but gives no accession, and the record says plainly that the analysis was not attempted.

## 2. Sentences not supported by the printed outputs

- **Attempt record, `findings`, 9th entry:** "their |Spearman r| with the weights of any fitted dimension is at most 0.47 over four seeds". This is wrong. Any dimension reaches 0.701 (rslds_seeds_0_1 cell 6: mouse 500, seed 1, dimension 4) and 0.547 (rslds_seeds_2_3 cell 6). The 0.47 is the maximum for dimension 1 only. The fig6-rslds-fit-quality notes have it right ("0.47 for dimension 1, 0.70 for any dimension").
- **Main notebook, cell 49 (Summary):** "tests across mice use 3 to 5 mice per group". fig7c (cell 36) and the figs5c sniffing test (cell 39) use 4 control and 6 experimental mice.
- **Cell 45 and the record's fig4g-male notes:** "the experimental fraction is inside 34.6 +/- 3.46% only with the `7s` baseline". This is too broad: at 1 min the pooled 7-s value is 40.1% (cell 44), which is outside tolerance. It is inside only for the 1-min mean over mice and both 2-min values. This does not affect the outcome, which is blocked.
- **Cell 28:** "more than nearly twice as many control units … pass 2 sigma" is self-contradictory. Cell 27 gives 157 → 279 units (×1.78) at 1 min. The record's wording, "nearly twice", is correct.
- **README:** "Blocked: not attempted for time". The record also gives the missing accession as a reason.

Everything else in the "**Result:**" conclusions, the four notebook summaries, the README and the record's notes matches the printed outputs. I checked every number in them.

**Round-1 reasons in the record.** They are in my words. Two small attributions don't match my report:
- The fig7b reason carries problem 7 (identical W columns, NaN dimension 2). In round 1 I marked that "does not affect a conclusion" and tied it to cell 13, not to the fig7b outcome.
- The fig6g reason appends problem 9. That one is fair.

## 3. Round-1 points

**Resolved:**
- 1 (figs5c outcome).
- 2 (ACHW estimator): three estimators plus a synthetic check.
- 3 (decoder): 31-unit subsampling and shuffles at each C.
- 4 (figs4a readings).
- 5 for fig4g and fig5e: the male parts were added.
- 6 (`alpha = 0`).
- 7 (complex pairs now use the imaginary part).
- 9 (flow fields of all ten mice).
- The parts of 10 about which mice/data the files hold: "male part only" is now stated as consistent with the files, not shown. Mice 510/500 now have evidence that their traces are z-scores. The sniffing-state reading for 510/500 is stated.
- All the outputs I asked for in round-1 section C.

**Remaining issues that bear on a conclusion:**
- **fig6-rslds-fit-quality (11):** the 85% may not be the emissions R². This is now put to a reader. Under the majority reading, seed 0 has attack mostly in one state in 7 of 8 mice. So if the 85% were read differently, this claim's outcome would still differ across seeds rather than become reproduced.
- **fig6-rslds-fit-quality (8):** a held-out score exists only for seed 0, one fold. It shows the groups differ at the 5-s horizon (p = 0.010). The sigma-normalized fits differ at both horizons (p = 0.016). So the "similar performance" part of the claim also fails under those readings. That does not change the outcome, but it is not in the outcome's notes as a criterion failure.
- **fig7c:** the least biased estimator (no mean removed) leaves 46–81 units undefined, dropping more control than experimental units. These are the slowest units, so the 25–31% reduction may understate the true one. The whole-file variant gives 43–47%. Not reproduced still stands on the stated window, but it is not robust to this choice.
- **figs5e:** the subsampled shuffled decoders also separate the groups (p = 0.036 at every C, cell 33). The group difference therefore exists without behaviour labels. Not reproduced follows the criterion, but it does not show that behaviour decoding is impaired. The conclusion does not say this.
- **figs4a:** the possible S4A star misreading described in section 1.
- **10:** the clock-alignment sensitivity check was run only for fig4ef. Mice 497 and 500 also enter figs4e, fig5bd, figs5e and fig7c. The pre-intruder baseline remains an assumption throughout.
- **fig1e:** still not attempted.
