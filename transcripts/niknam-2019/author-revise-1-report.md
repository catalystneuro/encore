No outcome changed. The verifier agreed with all 34 outcomes, and nothing in the new outputs moves any of them. I re-ran the entry with `python tools/entry.py all entries/niknam-2019`: the check reports 0 errors and the notebook ran in 71 s.

The outcomes stay as before:
- **Reproduced (4):** probe-locations-link, methods-neuron-counts, fig1b, fig1-remapping-longer-latency.
- **Partially reproduced (1):** fig1-example-neurons.
- **Not reproduced (3):** fig1c, fig1d, fig1e.
- **Blocked (26):** 24 model claims as too large, the N-model claim as methods underspecified, and figs1 as metadata insufficient.

**What I added or corrected, by point in the report:**
- **Pairing by trial (problem 1):** this reading is now shown as "not testable" instead of counts of 0. A new data check explains why. In no session does a trial show a probe in both the fixation and the perisaccadic window, because a probe comes back only after the whole probe order has played, a median 562 to 604 ms later.
- **Pairing (problem 2, and C2):** I added two variant pairings over the 1 ms bins of the response window, one on mean counts and one on smoothed curves. They appear in every Figure 1 table.
  - On mean counts, fig1c, fig1d and fig1e still fail.
  - On smoothed curves, fig1d would be reproduced (34 neurons, 0.815 to 1.365), and fig1c and fig1e would be partially reproduced. This variant agrees with the code's `nuron_list` on ST for 36 of 41 neurons. The Methods exclude it, though ("not estimates of firing rate").
  - Because the claims file lets only pairing by trial or by condition decide, I asked a reader in the new `questions/niknam-2019.yaml` whether that list should include a pairing over time bins. The claim notes say this.
- **Fixation values of the example neurons (problem 3, and C3):** I added a scan of the fixation-window boundaries and a ±1 ms shift of the saccade index. Our standard errors match the paper's to within 0.01. Even so, no single window matches the means of all three matched examples; the closest, -495 to -100 ms, is off by up to 0.054 spk/s. The RF example's candidate neuron reaches 53.87 to 59.68 spk/s, never 60.89. Shifting the saccade index moves the perisaccadic values away from the paper's, so I kept it. The paper's fixation set is still not identified, and this is now part of the methods finding.
- **Overlap with the authors' list (problem 4, and C1):** I added a per-neuron table, by name, of `nuron_list` against the p-value under each pairing. The fig1b notes now say that 5 of the 8 suppressed neurons are the authors'.
- **Latency claim (problem 5):** the conclusion now says the remapped peaks partly follow from how neurons are selected, and that the RF peak at 62 ms is the independent part.
- **Compute limits (problem 6):** the notes now name the limits: the 60-minute notebook limit and the 5 hours of an author run. This run's lower bound for the parameter-selection step alone is about 28 CPU hours, 7 hours on 4 CPUs. The four too-large claims that also need the N-model now say they would stay blocked as methods underspecified with any compute budget.
- **Probe order (problem 7, and C4):** the data check now prints, per session, onsets per trial, probe codes per trial, presentations of each probe per trial, and where the order restarts.
  - Three sessions use 75 or 80 codes instead of 81.
  - In most trials of every session except 20150717, the order restarts from its first probe 35 to 296 ms after the saccade. This is why only 7.6% of trials passed the check for blocks of 81.
  - A 14 or 21 ms run takes one place in the order, so it is one probe held longer.
  - I added these facts to the metadata finding.
- **Dead code (problem 8):** removed.
- **Record:** the round is recorded under `verifications`, quoting the report's reasons, with a response for each claim. The README now points to the reader question.

**Not done:** I did not compare the docx version of the data descriptor with the pdf. I did not commit or push.
