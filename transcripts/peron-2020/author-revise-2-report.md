I've answered every point in the round-2 report and re-run the entry (`python tools/entry.py all entries/peron-2020`: 0 errors, notebook passes in 2,233 s). `entry.py check` passes after the record was updated. Nothing is committed.

**Outcomes.** All 31 verified outcomes stand as they were. I put two changes under `proposed` for a third verification round:
- **model-equal-connectivity-ablation-increases:** not reproduced → partially reproduced proposed. Counting excitatory neurons only, scores rise in 30 of 30 networks (0.546 to 0.562, p = 1.9e-09), the direction the claim states. Both values are outside tolerance.
- **model-more-ablation-larger-decline:** partially reproduced → reproduced proposed. Under calibration (a) with excitatory neurons, R = -0.590 (p = 1.3e-12), and the decline grows at each larger ablation size. That is inside -0.65 ± 0.065, but only just: the bound is -0.585.

**Assumptions revised in reply to the report:**
- **Which neurons are counted.** The main reading is now excitatory neurons, and all neurons are a variant. The verifier pointed to the neuron counts. The Methods also calibrate the input on excitatory scores and ablate excitatory neurons, and the in vivo data the model stands for are excitatory neurons (Methods, Mice). That is why both changes above are proposed.
- **Calibration (b).** The verifier noted that its minimum was never bracketed, so every sweep now starts at no input. At Pconn 0.4 the smallest KS distance is at no input (0.514 for touch input, 0.510 for slow input), so (b) sets no strength there and its runs are gone. The cause is that 66 to 75% of the model's excitatory neurons score exactly 0 at every strength, while almost no in vivo neuron does. That leaves (a) as the only reading that sets both matched strengths. Amplification stays reproduced under (a), and the record says that (a) is only weakly set at Pconn 0.2.

**Sentences corrected (notebook, README, record):**
- The archives are 120.9 GB compressed, not 128 GB. The streaming time is now given as 11 to 18 minutes: this run took 949 s, an earlier one 1,052 s.
- The ablation-log finding now says 77.1 GB of the 166.7 GB uncompressed.
- The percentile description in cell 18 now gives both rules.
- The unsupported "other data" sentence about the silent ablations is gone.
- The MAD comparison now says about half for touch ablations and about a tenth for whisking ablations.
- The summary now names per-mouse-table as the one claim where the two cylinders differ, and says the table's score changes match within 0.005 in 23 of 24 rows.
- The response-similarity note now says the paper's values come from the bin-mean fit only. The point fit gives 4 of 9 whisking slopes negative (p = 1.000) and 2,824 neurons.
- The proximity finding now says the Methods cylinder is the main reading.
- The "about twice the paper's" sentence now says the grand median of 0.546 is 2.3 times the paper's 0.237.
- For model-all-or-none-robust, the record now says the negative extrapolated strength comes from this attempt's calibration.
- The model question for the authors now also asks which neurons are counted.

**Round 2 is recorded under `verifications`**, all 31 claims with the verifier's reasons in its words:
- It agreed with 29 outcomes.
- It disagreed with model-equal-connectivity, giving partially reproduced.
- It left model-more-ablation unsettled and gave no outcome.

**Not done:**
- **No new reader questions.** The report found no new place where the claims file misreads the paper, so `questions/peron-2020.yaml` is unchanged.
- **Round-1 entries left as they are.** The verifier said `agrees: true` understates its round-1 reason for the seven model claims. Its own round-1 outcome there was blocked, the same as the record, so I didn't edit those entries. The round-2 `reviewed` text records its note.
- **Two open points, still stated as before.** The 50 ms burst rule and the check of the Extended Data Table 1 transcription remain open.
