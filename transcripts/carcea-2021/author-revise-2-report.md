No outcome changed and I made no proposed changes. All 19 outcomes stay as the verifier agreed in round 2. I re-ran `python tools/entry.py all entries/000114-carcea-2021`: 0 errors, and the notebook passes in about 3 minutes. Every number from the earlier run came out the same.

**New outputs the verifier asked for**
- **Dam retrieval in V111 03032018 (point 3a):** I added each unit's spike counts in the baseline and in the episode, and the population's spike count around the episode.
  - The baseline is not a gap in the recording. The population fires 537 spikes in it, which is more than in 43% of the session's 10 s windows, and no silent stretch near the episode lasts over 0.22 s.
  - The 9 activated units are nearly silent in the baseline (0 to 2.1 Hz).
  - During the 5.2 s episode about 16 units fire together at 144 to 221 Hz. That is 14,346 population spikes in the first 5 s, against 1,838 per 5 s over the session; only 12 of the session's 3,325 five-second windows reach that size.
  - So the retrieval falls on one of the session's largest synchronous bursts. These outputs cannot tell a real response from a burst that happens to coincide with the episode. The criterion counts the units as given, so I kept partially reproduced and did not propose a change. The conclusion, notes and summary now say this, and I added it to the unit-quality finding.
- **Annotation coverage for the rate claims (point 3c):** I added the first and last times and the longest gap per session for the virgin labels, "Mom agressing" and "Mom retrieval".
  - The virgin labels run from within 0.61 h of each session's start to within 0.15 h of its end, with gaps of up to 1.93 h.
  - Shepherding and retrieval are too rare for their spacing to reveal stretches that were not scored.
  - The fig1j conclusion no longer says the low rate cannot come from partial scoring. It now says the coverage is consistent with sessions scored in full.

**Corrections**
- **Singly housed dams:** the hard-coded 0.17 per hour is replaced by 0.2 ± 0.1 per hour (N = 5), from the Extended Data Fig. 8a legend. This is in the printed reference, the conclusion and the notes. I saved the paper text to `paper/PMC8387235.txt`, but `paper/` is in `.gitignore`, so it will not be committed.
- **Nest entry:**
  - The 24.1% variant (leaving out the 20 units above 1,048,500 spikes) is now stated as inside both tolerances.
  - The baseline-overlap sentence now gives the largest count (V110, 20 of 72) and the largest share (V116 03092018, 16 of 29).
- **Draft comparison:** the summary and introduction now say the voltage values were not compared, only the series' shape and rate.
- **Smaller text fixes:**
  - The introduction now says 8 of 14 ecephys files.
  - The label-link notes give the V118 median as 64.1 s.
  - The coverage text gives V118 03192018 as 0.61 h short and names the three V116 files that end early. I also corrected that sentence in the round-1 response.
  - The README now says about three minutes.
  - The round-1 nest-entry reason now reads "17 of its 26 units", as the verifier asked.
- Round 2 is recorded under `verifications` with a result and response for each of the 19 claims.

**Not done**
- **Shared clock (point 3b):** I ran no new test. No test so far establishes a shared clock in any session. The fig2j and nest-entry results without V116 03102018 are already shown, and both outcomes are kept because the criterion fixes the set of units.
- **fig2j variant:** without V116 03102018 it would pass (p = 0.0237). I recorded this as a variant and did not change the outcome, since nothing shows that session is on a different clock from the others.
