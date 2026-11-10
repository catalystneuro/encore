I've written `claims/burman-2023.yaml`. The quote checker reports 35 claims, 34 quotes, 27 statistical values and 0 problems. Nothing was committed.

**Text read.** The version of record (open access, Europe PMC PMC11913778): main text, the legends of Figures 1 to 4, and the STAR Methods with Tables 1 and 2. **The supplement (Figures S1 to S7 and their legends) is not in the text, and there is no PDF.** I went ahead because the main results, including every number for Figure 4A to 4D, are in the main text. Only `figs6-rate-regressed` needs a method found only in the supplement. Claims on S2 to S5 and S7 rest on the main-text sentences that cite those figures, and their tests are unknown.

**Code read:**
- Neuropixels analysis gist `a77bcf5e`, revision 43a13d89. It names DANDI:000458 version 0.230317.0039 and the 17 sessions.
- Network simulation gist `2ce61e4e`, revision f6a05661.
- The `richardjburman/burman-et-al-2022---Awake-EGABAAR` repository at a404c3e: the NEURON model for Figure S4.

**Claims:**
- **Counts:** 35 claims. 34 have quotes; the one without is the link claim (`dataset-sessions-link`), which checks that the 17 sessions are in the dataset with the fields the code uses. 24 claims carry statistics (27 entries), 25 have expected values, and all 35 have criteria.
- **Testable on DANDI:000458:** 6 claims (the session link, the sample counts, synchrony, entropy, firing rate, and Figure S6).
- **Not testable:** 24 patch-clamp claims (Figures 1 to 3, S2, S3, S5). DANDI:000458 is only the Claar et al. Neuropixels data, and the paper deposits its own recordings nowhere ("available on request").
- **Model claims:** 5, marked `data: elsewhere` and pointing at the simulation code (Figure 4F/H, S4, S7).

**Details left open, and the readings named:**
- **Area selection:** (A1) the Methods' annotations SSp-ll, SSp-tr or MOs; (A2) the code's first three characters of `location` matched against `estim_target_region`.
- **Evoked firing rate, used for the 0.1 to 200 Hz exclusion:** (F1) the Methods' spike count over trials × 10 ms; (F2) what the code actually computes. The code's `get_firing_rate` sums spike *times* where a count is expected, and divides by the highest trial index with a spike plus one. Every dataset claim runs under all four combinations of A and F.
- **Waveform cut:** ≥0.4 ms in the Methods, >0.4 ms in the code. The code's cut is a variant.
- **Alignment and pooling:** the code aligns to the trial's `stop_time` and pools all intensities and stimulation sites. The Methods say neither, so I followed the code.
- **Figure S6 regression (supplement missing):** (R1) a pooled regression on rate, then a paired t test of the residuals; (R2) an OLS model with condition and rate; (R3) the per-neuron awake-minus-anesthetized difference regressed on the rate difference, with the intercept tested.
- **Firing-rate claim:** the paper gives no value or test in the text I read. I used the paired t test the paper applies to the other per-neuron comparisons, a standard choice.
- **Figure S7 decoding test (unknown):** (D1) a paired t test over the 20 runs; (D2) shunting more accurate in every run.
- **Model activity claim:** the paper gives no test, so I set "lower in at least 18 of the 20 runs" as a standard choice. Random seeds are left unset, as in the code.
- **Neurons with an undefined value:** left out of the paired test, a standard choice.

**Missing from the paper.** The supplement. It holds the methods and numbers for Figures S2 to S7, which the S6 regression and the S7 decoding test need, and the tests for the S2, S3 and S5 claims.
