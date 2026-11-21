I've addressed every point in the round-2 report and recorded the round. No outcome changed, and no `proposed` changes were needed. The final run of `python tools/entry.py all entries/huszar-2022` passed: the check found 0 errors, the notebook took 47.6 min and peaked at 1.4 GB, and I confirmed the conclusions match its numbers. Nothing is committed.

**Outcomes:** all 44 are unchanged (17 reproduced, 10 partially reproduced, 7 not reproduced, 10 blocked). The round-2 entry records the verifier agreeing with 38 and disagreeing with 6: sessions-durations, ed10, fig3c, fig3e, ed6 and fig4d. fig6c-novel is recorded as accepted only on condition of the open-field scale.

**Fixes and new outputs:**
- **Theta channel:** a channel now has to show a positive sharp wave *and* sit above the layer centre. 72 of 104 sessions follow that rule, and the notebook prints that every one of their channels is above the centre and positive. Six sessions with 20 or fewer non-REM ripples (including the two with no non-REM) fall back to all ripples; this is now stated and printed. Added variants on the rule-following sessions only:
  - fig6c-theta: rho = 0.734.
  - fig6d-rate: rank-sum p = 0.051 on that subset (paired p = 0.0047), stated in the notes.
  - fig7fg: theta slope 0.0026.
- **fig2c:** the SBD median is 0.0170, still just below tolerance by the notebook's check, so it stays partially reproduced.
- **Open-field scale (fig6c-novel and the other novel-environment claims):** a new data-check cell prints the evidence. Lab-unit tracks recorded alongside centimetre positions work out at 0.85 to 0.93 cm per unit. A 0.85 variant gives p = 0.57 for fig6c-novel, the same outcome. The open fields themselves carry no scale, so that outcome stays marked as resting on an assumption and conditional on it.
- **fig6f:** ran the scale variants (the main effect holds under each) and compared against the Supplementary Table 5 means.
- **fig7d:** added a bootstrap over connections. The 29–42 ms peak wins in 999 of 1,000 resamplings, and the difference from the next bin has a 95% interval of 0.00017 to 0.00050.
- **Wrong numbers and sentences:** corrected every one the report quoted (ed5, ed10, fig5b, fig7b, fig7fg, the "60% more" sentence, the README row count and "without sleep states"), and removed the uncited "earlier run" sentence.
- **ed5 and ed10 fractions:** these move between runs because each claim shares one random generator across its comparisons. ed5's novel fraction is now 0.498 (0.604 before); ed10's ratemap fraction is 0.132 (0.106 before). The notes and notebook say so.
- **ed3:** its numbers moved slightly with the new theta channel; the notes are updated and the outcome is unchanged.
- **Round 1 record:** ed3, ed5, ed7 and ed10 now read `agrees: false`, as the verifier said those were disagreements.
- **ed10:** added a question to `questions/huszar-2022.yaml` asking whether its dependency on ed2 should be dropped. With it dropped, its own parts would give not reproduced (p = 0.078).

**Not done, and why:**
- **ed10** stays blocked with no proposed change, because the claims file's `depends_on` still blocks it.
- **fig3c, fig3e, ed6, ed7 and fig4d** stay blocked as `too_large`; the first run's time limit is what stopped them. Their notes now say plainly that they were not attempted and that the 9 to 12 GB figure only applies to holding the whole matrix in memory. A chunked version would be a new analysis, which the protocol leaves to a new attempt. fig4d's notes give its size from the Methods, with no timing.
- **sessions-durations** stays not reproduced, with the disagreement recorded and the existing reader question still open.
- **The paper's pair set of 315,722** (fig7fg) is still unexplained.

I also set `runtime_minutes` to 47 in `entry.yaml`.
