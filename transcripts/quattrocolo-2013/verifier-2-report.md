**Verifier report, round 2: Quattrocolo & Maccaferri 2013, CRCNS hc-9**

The claims file has 26 claims, and the attempt record has 26 outcomes: 1 reproduced and 25 blocked for missing data.

**1. Outcomes**

- **fig7a-olm-sag: reproduced (`assumed: true`). I agree.**
  - The criterion's two readings both give 3 of 3 cells (cell 14). Reading (a) gives sags of 17.5, 7.9 and 8.7 mV, which is 21.8 to 46.6 times its threshold. Reading (b) gives sag ratios of 0.448, 0.224 and 0.208, all above 0.1.
  - Every variant in cell 16 also gives 3 of 3.
  - The assumption is stated in three places: the outcome's first deviation, the conclusion and the Summary. It is reasonable. The paper defines no sag measure, and the claims file sets this one.
  - The new 0 pA check (cell 20) shows that reading (a)'s 2 SD threshold is passed by noise alone. The author says so openly. The outcome still holds for two reasons:
    - The -100 pA sags are 4.5 to 7.3 times the 0 pA value, and 4.2 to 10.8 times twice the SD of the 0 pA step window.
    - Reading (b) gives 3 of 3, with the smallest ratio 0.200 (cell 16).
- **The 25 blocked claims (data_missing): I agree with all of them.** The zip holds only the three O-LM current-step ATF files (cell 3), and the signals are "2CC mV" and "AO #1" (cell 4). None of these claims can be tested, even in part.

**2. Text checked against the outputs**

Cells 5, 7, 9, 11, 13 and 24 match the printed numbers, as do the README and the outcome notes, deviations and findings. Cell 5's "3 to 5 s" also matches the data description. Three statements are not fully supported:

- **Attempt record, fig7a notes:** "With raw V_min and end windows of 50 to 200 ms the smallest sag is 42.4 baseline SDs and the smallest ratio 0.200."
  - In cell 16 both minima come from the 1 ms running-mean variant with a 200 ms end window (42.392 and 0.200).
  - The raw-V_min minima are 42.697 and 0.201.
  - Cell 24 phrases this correctly ("every variant shown (raw V_min, end windows…)"). The record's notes do not.
- **Cell 25 (Summary):** "reading (b) and the comparison with the 0 pA sweep do [separate a sag from noise in these recordings]."
  - Reading (b)'s false-positive rate is tested only on synthetic white noise (cell 20). Its ratio is not computed on the recordings' own 0 pA sweeps.
  - The synthetic noise (0.2 mV, white) also lacks the slow fluctuations that make reading (a) fail on the real recordings.
  - From the printed numbers I estimate a noise ratio of about 0.03 to 0.06 (a 1.3 to 2.4 mV 0 pA "sag" over a 35 to 42 mV hyperpolarization). That supports the claim, but the notebook does not show it. "In these recordings" holds only for the 0 pA comparison.
- **README:** "It takes under a minute." No output shows total runtime; cell 1 prints only the 3.0 s load time.

**My round-1 reasons in the attempt record:** the `verifications` entries state my reasons in my own words, condensed and accurately. That includes the 4.0 SD versus 0.7 SD synthetic result and both "could not check" items. Leaving out my point B5 (units and timing check) loses nothing. Its references to cells 14 and 16 still point to the main measures and the variants in the current notebook.

**Claims file:** I found no new place where it misreads the paper.

**3. Round-1 points**

Resolved:
- **B1 (raw minimum biases reading (a)):** the main measure now takes V_min from a 1 ms running mean (`hc9.sag_measures`). Cell 20 repeats my synthetic test and gets the same result: the raw minimum passes in 100 of 100 draws, the running mean in none.
- **C2 (noise floor on the 0 pA sweep):** done in cell 20. It shows a weakness of reading (a) larger than I found, and the author reports it.
- **B2, B3, B4:** kept as they were, with disclosures. B4 is filed as two metadata_error findings. Not raising the "30 pA" in the claims-file header is acceptable, since no claim or criterion depends on it.

Partly resolved:
- **C1 (traces against Figure 7):** a zoomed plot of the first 300 ms is added (cell 23). It is not set against the printed figure, and the record says so. This affects only which file shows which panel, not the outcome.

Remaining items that bear on a conclusion: none change an outcome. Two fixes to the wording are needed:
- The attempt record's "with raw V_min" sentence on the variant minima.
- The Summary's claim that reading (b) separates sag from noise "in these recordings". It should either be limited to the synthetic test, or backed by computing the sag ratio on the 0 pA sweeps.
