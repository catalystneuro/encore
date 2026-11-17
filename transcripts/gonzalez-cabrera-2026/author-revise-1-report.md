I finished the round-1 revision. No outcome changed: both photometry claims are still reproduced, resting on an assumption, and the 39 other claims are still blocked. The basis for Figure 3b did change, and 15 blocked claims now carry a different reason. The final `python tools/entry.py all entries/gonzalez-cabrera-2026` run passed in 13.0 min and `check` reports 0 errors. The conclusions, record and README match the new numbers. Nothing is committed.

**The main change: how the post hoc tests are computed (problems 2 and 4).** I checked GraphPad's own description of how Prism computes post hoc tests after an ANOVA ([PDF](https://cdn.graphpad.com/faq/1688/file/MulitpleComparisonAlgorithmsPrism8.pdf)). Prism's choice of error depends on the design:
- **Fig. 3b, repeated measures on both factors:** Prism's error is the epoch × frequency × subject mean square with df 12. My round-1 "pooled" form was not this. With Prism's form, continuous light gives p 2.0e-4 to 5.3e-4. That is significant but misses the criterion's p < 0.0001, which the criterion counts as only partially reproduced.
- **Fig. 3b, ordinary two-way ANOVA (no repeated measures):** continuous light gives p 3.8e-6 to 3.8e-5 in all 32 readings, and no train frequency is significant. The outcome now rests on this reading, for two reasons:
  - The Fig. 3b legend says only "two-way ANOVA", while the Fig. 2f and 2i legends say "with repeated measures".
  - It is the only one of Prism's forms that gives the paper's p < 0.0001.
- **The catch:** the comparison in this reading is not paired, while the claims file asks for a "post hoc paired" test. I added this as a question for a reader in `questions/gonzalez-cabrera-2026.yaml` and did not change the claim.
- **Fig. 3c:** for both the ordinary and the mixed design, Prism uses the same error I already used, with df 24. So the verifier's suggested Satterthwaite df does not apply, and the result is p 0.00074 to 0.0028 (the paper reports 0.002).
- **Separate t-tests:** with a separate t-test per frequency (what Prism does when sphericity is not assumed), neither claim holds. Fig. 3b gives p 0.072 to 0.11 and Fig. 3c gives p 0.13 to 0.19.
- **Added output:** the notebook now prints the raw p, SE and df per frequency for every form, as the verifier asked.

**Other fixes and added outputs**
- **The trial-selection bug (problem 1):** `regular_onsets` now compares interval lengths to the median without rounding. It drops only the two stray intervals of photometry-exp-5 at 5 Hz, and trial counts per file are printed. With the fix, no train frequency reaches p < 0.05 in any reading.
- **Zero-variance Pre (problem 3):** the ordinary reading also holds with the paper code's −3.0 s baseline, where Pre is not zero by construction (p 9.9e-6 to 3.8e-5).
- **Isosbestic dependence (problem 6):** a variant on the 470-nm signal without the 405-nm correction gives the same outcomes.
- **Clock check (problem 7):** the notebook now says the shared clock is shown only for the opsin continuous files and assumed for the train and control files. Per-file counts are printed.
- **Block reason for the 15 silicon-probe claims (problem 5):** changed from `data_missing` to `methods_underspecified`, since the paper's Kilosort sort and manual curation cannot be repeated. The missing labels are recorded in the notes as metadata gaps.
- **ADC scan:** I scanned every ADC channel of all 255 recordings in the 34 ecephys files.
  - There are 133 tagging trains, on ADC1, ADC2 or ADC3, and nothing says which laser colour each one is.
  - The 2-s rotarod bouts are on ADC1 in 16 chronic recordings, so rotation onsets are recoverable, but nothing marks a block as reverse or forward.
- **Record:** I added round 1 under `verifications`. The 15 silicon-probe claims are marked as disagreed because of the reason change. I also added two `methods_unavailable` findings for the paper's authors: which ANOVA design and post hoc error they used, and their sorting and curation details.

**Not done**
- I did not change any claim's statement, expected values or criterion; the "paired" point is with a reader.
- I did not re-sort any silicon-probe data.
- The uncommitted changes to `tools/build_site.py` and `tools/site_assets/app.css` were there before this run; I left them alone.

Sources:
- [How Prism 8.0 computes multiple comparisons tests following ANOVA](https://cdn.graphpad.com/faq/1688/file/MulitpleComparisonAlgorithmsPrism8.pdf)
- [GraphPad FAQ 2172](https://www.graphpad.com/support/faq/multiple-comparisons-2-way-RM-ANOVA-no-sphericity/)
- [Prism guide, two-way ANOVA model tab](https://www.graphpad.com/guides/prism/latest/statistics/stat_experimental_design_tab_2way.htm)
