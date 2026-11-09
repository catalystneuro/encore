I answered all 7 questions in `questions/000010.yaml`, each marked `answered: 2026-10-21`. The paper settles none of them, and it links no code. For each one I wrote the readings the paper allows into the claim's criterion, citing the passage. No claim's statement or expected values changed. `python tools/claims_check.py` reports 0 problems, and every quote in the answers and the new criterion text matches the paper. Nothing is committed.

- **reaction-time:** The paper gives no rule for reading a reaction time from the photodiode signal. The only passage is the one in the question. The readings are a fixed threshold on the raw signal, or the baseline mean plus some number of s.d. before the go cue; the threshold, the number and the baseline window are left open.
- **behaviour-performance:** The paper does not say. The Methods exclude only lick early trials, so the literal reading counts no-lick ("ignore") trials as not correct. The other reading leaves them out. Both are run.
- **fig2c-population-dynamics:** None of the three details is given.
  1. The text says "normalized to the variance"; dividing by the s.d. is still a reading the paper allows.
  2. "10 trials" is not said to be per trial type.
  3. The 200 ms bin at t = 0 may start at, be centred on, or end at the go cue.

  All combinations are run.
- **imaging-selectivity-counts** (and the claims listed with it): The paper never gives the length of the response epoch, for imaging or electrophysiology. The 1.5 s figure is only the window for a lick. Both 1.3 s and 1.5 s are readings.
- **fig4h-pt-contra-imaging:** Nothing besides the 450 to 700 um imaging depth marks the layer 5 planes. The paper also says IT neurons "were also found in superficial layers". So testing all labelled cells is a substitute, to be recorded as a deviation, not a reading of the paper. The IT counts are not expected to match on it; the PT side is less affected.
- **fig2-selective-fraction** (tagging light trials): The paper does not say. Its only trial filter is correct trials, so using all correct trials is the literal reading. Using only trials without the tagging light is the second reading. This applies to every electrophysiology claim of Figs 2 and 3.
- **antidromic-latencies:** The paper gives no rule for telling antidromic from spontaneous spikes. The readings are:
  - the first spike in a window after the first pulse of each pair, with the window open (about 10 ms);
  - the same, leaving out collision trials;
  - the same, keeping only spikes in the evoked latency peak.

  Jitter is the s.d. over the pulses kept, per neuron, then averaged over neurons.
