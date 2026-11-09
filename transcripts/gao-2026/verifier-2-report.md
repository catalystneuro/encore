**Verifier report, round 2: 001683-gao-2026-01**

**1. Outcomes**

The claims file has 22 claims and the attempt record gives 22 outcomes. I agree with all 22.

- **Agree, no assumption needed:** fig2c, fig2d, fig2e, fig3a-count-reduction, fig3a-count-sham-vs-tfus (partial), fig3b-percent-time-reduction, fig3b-percent-time-sham-vs-tfus, fig3c-interval-sham-vs-tfus (partial), fig3d, fig4c (partial), fig6 (not reproduced), fig5b (blocked), fig5cdj (blocked). Where an outcome needs a particular reading, the claims file allows it ("under one reading"), and the printed p values support each one.
- **Agree, and the `assumed: true` assumptions are stated and reasonable:**
  - **fig2f.** Three assumptions: BH635 taken in time order, the repeated-measures reading, and family (i). It is fragile: p_family is 0.040, p_all is 0.051, and with BH635 by its labels p is 0.13 or 0.94.
  - **fig3b-sham-percent-time-no-change.** Two assumptions: repeated measures and family (i), with contralateral post 2 at p_family 0.034 and p_all 0.057. The record lists two assumptions, but cell 37 and the README say "on an assumption".
  - **fig3c-interval-increase.** The gap reading, which matches the paper's six percentages to within 0.4 point.
  - **fig4 and figs4.** Both rest on the repeated-measures reading. figs4 would be blocked under the ordinary reading, and the record says so.
  - **figs5.** Two assumptions: the pre-4-AP state from the gaps between pulses, and AI computed on band power. The second decides the outcome; on band ratios the claim fails in every combination. The paper's text is ambiguous here: "absolute power … by dividing … Furthermore, the asymmetry index … using Eq. 1 for each of the aforementioned".
  - **figs7.** The pre-4-AP state from the gaps between pulses.
- **Agree, but an `assumed` flag is missing:**
  - **fig4ef (partially reproduced)** rests on the same band-power AI choice that is flagged as an assumption for figs5. On band ratios neither part of the claim holds, so the outcome would be not reproduced (cell 21).
  - **fig5ghi (not reproduced)** rests on replacing the target-confirmation EEG, which the claims-file criterion specifies, with the PLV recordings. Under the claims file's own data definition this would be blocked (data_missing), like fig5cdj. The record discloses it only as a deviation.
- **Claims file:** I found no place where it misreads the paper.

**2. Sentences the numbers do not support**

- **seizure_metrics cell 51 (Summary), repeated in the fig3b-sham deviation:** "Its significant within-group changes of Fig. 3 (count and percent time against baseline …) appear only under the repeated-measures reading."
  - Cell 33 shows ordinary-ANOVA percent time at post 1 and post 2 significant (p_family 0.0077 to 0.0122). Only percent time at the stimulation block, the count changes and the interval need the repeated reading.
  - The argument for adopting the repeated reading still stands, but the sentence overstates it.
- **seizure_metrics cell 51:** "counting the six that end 1 to 1.4 s before a block end as cut off". The record notes for fig2c and fig3d say the same.
  - The variant counts seizures within 2 s of either end of the block as cut off. It leaves out 14 seizures, against 6 by default (cell 9), so 8 more, not 6.
  - The results do not change.
- **Attempt record, last finding:** "The PLV EEG recordings of the 16 epileptic rats are the last recordings…". Only 13 of the 16 rats have one (eeg_blocks cell 24).
- **README:** "about 25 minutes" for eeg_blocks and "about 12 minutes" for wild_type. The notebooks report 17.9 and 8.5 min.
- **Minor:**
  - eeg_blocks cell 5 (not a conclusion cell) says "tens to hundreds of microvolts", but cell 4 prints −16 to 14 µV with per-channel SD 1 to 5 µV.
  - seizure_metrics cell 44 says "the others … 0.70 or more", but one value is 0.6976.
- **Everything else checks out.** Every other sentence of the Result cells, the three Summary cells, the README and the record notes matches the printed outputs.
- **My round-1 reasons:** the record states them in my own words, verbatim from my round-1 table. The "19 of 22 agree" count is correct: three are `agrees: false`.

**3. Round-1 points**

All nine are resolved. Point 3 is resolved mostly rather than fully.

1. **z reference.** Replaced with t and F tests on Satterthwaite degrees of freedom. Repeated p is now at least the ordinary p for the between-group contrasts (for example 0.0400 against 0.0348). fig3a-count-sham-vs-tfus and fig3c-interval-sham-vs-tfus are now partial. I could not run the module (no numpy in my environment), so I checked the code and the outputs only.
2. **PLI window-length bias.** Fixed with nine 20 ms sub-windows and trial-shuffled noise floors.
3. **EP alignment.** Mostly resolved. A burst marker is found 10 to 60 ms after onset in 13 of 23 CENTER recordings and in none of the resting ones. In the other 10 rats no marker appears at any lag, so alignment there is unverified, though nothing suggests misalignment. fig5b stays blocked either way.
4. **Pre-4-AP EEG.** Used. figs5 and figs7 are now tested, on a stated assumption.
5. **`ai_ratio`.** Now tested.
6. **Sign of an increase under division.** Fixed.
7. **Time-point test.** Replaced with the two-way ANOVA, and a split-half position reading was added.
8. **Block-end variant.** Added. The results do not change.
9. **BH635 under the ordinary ANOVA.** Now shown (p = 0.94).

**What remains that bears on a conclusion**

- **The protocol's absence rule.** I still cannot check it. fig3b-sham-percent-time-no-change, fig4 and figs4 are "not reproduced" only because the repeated-measures reading is adopted where the two ANOVA readings disagree on a claim of absence.
- **Missing `assumed` flags.** fig4ef rests on band-power AI and fig5ghi on the PLV substitution; neither is flagged.
- **Family (i).** fig2f and fig3b-sham-percent-time-no-change both turn on it (p_family against p_all: 0.040 against 0.051, and 0.034 against 0.057). This is stated, but both outcomes would flip under family (ii).
