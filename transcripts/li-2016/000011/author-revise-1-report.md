I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all`: the check finds 0 errors and the notebook runs in 791 s. The new outputs that overlap the verifier's numbers match them, and every conclusion now matches the new numbers. The round is recorded under `verifications` in `attempts/000011-li-2016-01.yaml`, all 38 claims, with the verifier's reasons in its own words. Nothing is committed.

**Outcomes that changed**
- **selective-fraction**: partially_reproduced → not_reproduced, as the verifier said. With lick-early trials dropped (K1), only 1 of the 4 counts is within tolerance (the response epoch). My earlier conclusion had wrongly suggested three counts reached tolerance under K1; that was only true with them kept (K2). I still leave out the 44 units of the three unlabelled sessions, because the criterion asks for control trials and those sessions have none that can be identified. So I did not move it to methods_underspecified as the verifier suggested; this is recorded.
- **ed2b-silencing-strength**: partially_reproduced → not_reproduced, as the verifier said. Under K2 only the contralateral part of four holds.
- **cd-stable-over-epochs**: reproduced → blocked (methods_underspecified). The verifier showed that taking w from all correct control trials was my own choice. That reading gives 0.563 and 0.588 (inside 0.56–0.66); taking w from the training subset gives 0.534–0.554 (outside). The claims file fixes neither, so both are now run.
- **Kept with the disagreement recorded:** ed7e and ed8 stay partially_reproduced; the verifier would give not_reproduced. Three of four values hold with lick-early trials dropped and two of four with them kept.
- **Rule for partial outcomes:** the protocol doesn't say what to do when a criterion has no partial clause. I wrote a rule, stated in the summary and applied to all seven such claims: partial when at least half the criterion's parts hold under every reading that must agree. It is my own judgement, and round 2 should look at it.

**Outputs I added**
- **Spike widths from upsampled waveforms:** this gives 11 intermediate units, so the 19.5 kHz sampling does not explain the shortfall against the paper's 50.
- **Size of the lick-early problem under K2:** 339 of 931 lick-early light trials have the logged event more than 0.1 s after the light. That is 3–16% of each condition's trials in experiment 1 and 6.5–7.5% in experiment 2.
- **Included neurons:** per-neuron trial counts and which epochs each neuron is selective in, for the populations the recovery-time claims use. No simple extra selection brings them to the paper's 55, 143 or 40.
- **Modes 2 and 4:** per-session ROC values and the mean of |ROC − 0.5|.
- **ed9f (lick trace):**
  - Per-session summaries of the raw trace and example traces show the experiment-2 traces are flat.
  - Three raw thresholds above the experiment-2 baseline (0.16, 0.20, 0.25), since the old ones sat below it.
  - The same test on the 6 experiment-3 sessions, whose trace does carry licks, as a reference variant. It holds under 18 of 26 combinations; ed9f stays blocked because those are not the claim's sessions.
- **Reference numbers for blocked claims:** experiment-3 behaviour per mouse and a one-spot test with both hemispheres pooled (fig2b); selectivity counts on all trials of the unlabelled sessions (ed10).
- **Notes:**
  - fig1f's only passing reading tests 248 neurons per condition, against the paper's 168–175.
  - cd-captures values are measured on the trials that built the modes, so they are in-sample.
  - Under the search that stops at the go cue, fig1g's late-delay time is never found in any of 96 readings. That is what the data give, not something forced by the design: that search can return up to 300 ms, inside the tolerance.
- The data-check finding on lick-early trials and the summary now use the full counts.

**Questions added for a reader** (`questions/000011.yaml`)
- Which trials give the w in cd-stable-over-epochs.
- Whether K2 should align the shifted lick-early trials to the light in the laser trace.
- Whether the go-cue search end is meant for fig1g's late-delay condition.

**What I did not do**
- I changed no claim and ran no held-out reading for cd-captures, since the claims file names none.
- I left `provenance.runner.url` as it was, because I don't know this run's URL.
- `runtime_minutes` in `entry.yaml` is now 14, to match the shorter run.
