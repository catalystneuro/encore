No outcome changed in this round. I answered each point in the round-1 report, re-ran the entry (`tools/entry.py all` passes, 2.0 min), and recorded the round under `verifications`. The outputs match between the last two runs apart from timings, and the conclusions were checked against them.

**Outcomes.** The verifier agreed with 18 of 19 claims. The one disagreement is figs7e-ibi-chance, which the verifier would call not reproduced. I kept it as blocked (methods underspecified) and recorded the disagreement. My reason is the protocol's chance-level rule: the procedure the Methods describe has a chance level of 10.8% under its own null, against the paper's 25%. The above-chance rates the verifier cites come from settings the paper does not use, and, as the verifier says, they may reflect slow drift. Each odor has only one inter-block interval per session, so a test that holds out a whole block cannot be run.

**Fixed in the helper:** analysis windows that ran past the first or last imaging frame were filled by linear extrapolation. They are now left empty, and a new data-check cell shows no window falls outside the imaging span.

**Added outputs the verifier asked for:**
- **ON-OFF angles (mouse fig2h, locust fig1g).** The centring in the paper's code pushes angles above 90° on its own. The two halves of a single ON window come out at about 101° (mouse) and 96° (locust), and a synthetic check shows the same. The conclusions now say the angles above 90° do not show that ON and OFF responses are inverted.
- **Normalisation (fig2f, fig6e, fig7d).**
  - With z-scores based only on the 2 s before odor onset, ON and OFF stay positively correlated (median r 0.53) and there is no contrast enhancement (p = 0.58).
  - On synthetic data, z-scoring each trial over its whole window turns pure excitation into negative correlations (r about −0.9).
  - Counting windows in frames, as the paper's code does, gives the same conclusions.
- **Classifiers in the block sessions.**
  - With fewer neighbours than trials per odor (k = 5 or 9 for fig7h, k = 5 or 10 for figs7e), accuracy is 69% to 100%.
  - For fig7j, the only shuffle that keeps blocks together (relabelling the four blocks) gives about the same accuracy as the real labels. So these classifiers cannot tell the odor apart from slow differences between blocks.
- **Variants:**
  - fig6e on the three sessions the published version's Table 1 names: p = 0.082.
  - figs8e on the two dandiset sessions whose ROI counts appear in that table.
  - figs4a without the reference odor's angle to itself: the count is still 4.

**Checked against the source:** I downloaded the published iScience version from PMC into `paper/`. Its Table 1 and the 44.7° median ON-ON angle confirm what the verifier reported. That led to a new finding: the dandiset and Table 1 disagree on which mouse the 318-ROI session belongs to. Two existing findings now also cover the acetophenone panel's session assignment and the random-order sessions that do not match. The README, the notebook summary and the attempt notes are updated to match.

**Not done:**
- No block-structure control for the locust classifiers (fig7f, fig7i). The Figshare files hold only the 40 s around each trial, so nothing between blocks is available; the notes say so.
- The preprint's Table S1 is still unread (it is an image), so the session assignments come from the published version, not the preprint.

Untracked shell config files and a `scripts` folder in the repo root were created by the sandbox; I left them alone and they should not be committed.
