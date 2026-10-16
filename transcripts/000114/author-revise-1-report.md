No outcome changed. The round-1 verifier agreed with all 19 outcomes, so each one stays as it was. The entry check passes and the notebook re-ran cleanly in 113 s, giving the same numbers on each run. Nothing is committed.

**Added to the notebook, in reply to the report:**
- **Unit names:** the data check now prints them. In every session they are just the indices 0 to n-1.
- **Annotation coverage:** a new data check shows annotations start at the start of every file and no gap is longer than 0.81 h. That fits each session being scored over its whole length, which the two rate claims assume.
- **Draft against pinned version:** all 30 files are now compared, not one. Spike times, events and series are identical in all 30.
- **New variants for the three "fraction of units activated" claims:**
  - counting episodes with no spikes as 0, the same way the shuffles do (helper option in `pvn.py`);
  - the test's false-positive level, measured on Poisson units that have no response: 1.0 to 2.3% activated;
  - counting V111's three days as one set of units, trying each of its sessions;
  - leaving out V116 03102018, the session whose clock is unknown.
- **Nest entry:** I also counted how often the baseline window overlaps an earlier nest dwell or a shepherding episode: 3 to 20 entries per session.
- **Dam retrieval:** the 9 activated units in V111 03032018 share a median 71% of their spikes pairwise within 0.1 ms, against 1.7% among that session's other units. They are probably far fewer than 9 neurons.
- **Blocked claims:** two outputs the verifier asked for. For fig2f, "Virgin Agressing" never overlaps "Mom agressing", and only 2 of the 3 shepherding-activated units have such episodes. For fig4i, the response after the dam's retrievals is positive in all six animals on Day 1. Both stay blocked.

**Variants you should know about.** Under the criteria these don't change outcomes, but the notes and conclusions now state them:
- **fig2j:** leaving out V116 03102018 gives p = 0.0237. The test passes in that variant; the main result is p = 0.182.
- **Nest entry:** counting V111 once using its 03032018 session gives 28.8%, which is inside the tolerance of the pooled reading (23.9 to 29.2%).
- **Dam retrieval:** counting V111 once using its 03062018 session gives p = 0.061, which would fail the test. The suppressed count (20) is close to what the Poisson null produces (12).

**Corrected:**
- The notebook said about 5% of units would pass by chance; it now gives the measured false-positive level.
- The conclusions, the summary, the outcome notes and the findings now match the new numbers.
- The attempt record has a deviation about the empty-episode handling and a `verifications` round 1 entry for all 19 claims. Each one has the verifier's reason and my response.

**Not done:**
- I made no code change for problem 1 (empty episodes) or problem 3 (V111's days counted separately). The main analysis keeps following the paper's code and counting units per day, as the paper does; both are now shown as variants.
- I left the shared-clock problem (problem 4) unresolved because the data can't settle it. The record still says so, and every unit claim now also has a result without V116 03102018.
