The round-2 revision is done. The final re-run (`python tools/entry.py all entries/000773-hart-2024`) passed, took 36.2 minutes, and `check` reports 0 errors. Nothing is committed.

**Outcomes:** none changed and none are proposed. The verifier agreed with all 22, so there is no `proposed` entry and no third round is needed for outcomes. Every number quoted in the text was the same after the re-run.

**Outputs added (notebook):**
- **fig2b:** cell 10 now reads the Brain Image Library landing page and prints it: 15 brains (7 young, 8 old) and its two notices (the repository is under review, and data were unavailable October 5 to 16). The download server again timed out on all three tries.
- **fig3d-pg-60-vs-90-days-same, reading (a):** the verifier asked for the held-out 60-day values against the 000467 90-day values; these are now compared. There is no difference (p = 0.60, 0.53, 0.18; reading b 0.33 to 0.74). At the placement from the general odorants alone, only reading (b) of PGb with 4-methyl-3-heptanone differs (p = 0.041). The claim stays blocked.

**Text corrected (notebook, README, attempt record):**
- **fig3b:** "4 old ants" is now 5, in the notebook, the notes and the round-1 response.
- **fig2b:** the timeouts are now given as printed. The earlier shell attempts are described as appearing in no output.
- **Data S2 sentences:** the README and summary now say every focal glomerulus claim holds on Data S2's own values *except* pg-opposite-modulation.
- **Whole-AL outline:** "need no hand-drawn ROI" now says the outline is a threshold stand-in for the paper's hand-drawn one.
- **Run time:** about 40 minutes, not 30.
- **Hand-drawn ROI finding:** twelve claims depend on the hand-drawn ROIs, not ten.
- **figs2a:** the smallest p is now given as 0.0799, not 0.080.

**Caveats added:**
- **fig4 notes, conclusion, summary and README:** they now say which way the placement problem pushes the results. Where an old-ant ROI misses the glomerulus, old values come out too low. That favours fig4, which needs old responses to be lower, and works against fig3d and figs4d, which need them higher. The spurious PGb decline with 3-hexanone (old 12.8 here against Data S2's 25.1) is the visible case, and G2 gives p = 0.059 with all trials.
- **figs2a:** the notes now say this null result is weak evidence for the same reason figs3c was blocked. They also say why it stays reproduced: the glomeruli are placed from Data S2 for each ant, not by figs3c's automated rule, and no variant reaches p < 0.05.

**Recorded:**
- The round-2 verification is under `verifications` in the attempt record, with all 22 claims marked as agreed, the verifier's reasons in its own words, and my responses.
- `questions/000773.yaml` has a new question for a reader: fig3d-pg-60-vs-90-days-same's criterion gives no rule for when its two readings disagree. The other two claims-file problems the verifier listed were already there from round 1.

**Not done:** the claims file is unchanged, as the protocol requires. The confocal data are still unreachable because the download server never answered, and no other network was available to this run.
