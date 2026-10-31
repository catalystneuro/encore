No questions were asked or answered for this attempt, so no claim changed and no outcome changed. I re-ran the entry as you asked and built the handover. Nothing is committed or pushed.

**Questions.** `questions/000467.yaml` does not exist, and no other question file for 000467 exists on any branch. The author run filed no questions to a reader; its open method questions went to the paper's authors as `methods_unavailable` findings. The answer run (`transcripts/000467/answer-report.md`) says: "There was nothing to answer, and I changed nothing." The claims file `claims/000467/` was last changed in d4bbaa251, before the attempt.

**What the answers changed:** nothing. So I did not touch the notebooks, the conclusions, the record `attempts/000467-hart-2023-01.yaml` or any claim's notes.

**Outcomes:** all 32 claims keep the outcomes they had:

| Claim | Earlier outcome | Now |
|---|---|---|
| fig3f-general-odorants-unique | not reproduced | same |
| fig3fg-hexanone-broad | partially reproduced | same |
| figs4a-bilateral-symmetry | partially reproduced | same |
| fig4b-vehicle-no-response | not reproduced | same |
| fig4-no-decreases | not reproduced | same |
| fig4-large-lasting-responses | partially reproduced (assumed) | same |
| figs5a-sparse-median-6 | reproduced (assumed) | same |
| figs5a-concentration-more-glomeruli | reproduced (assumed) | same |
| figs5b-shared-glomerulus | partially reproduced (assumed) | same |
| figs5c-mho-rarely-overlaps | reproduced (assumed) | same |
| fig6-shared-panic-pathway (imaging half) | partially reproduced (assumed) | same |
| fig5ab-focal-glomeruli | not reproduced | same |
| fig5d-stereotyped-positions | not reproduced | same |
| fig5c-s6-tuning | partially reproduced (assumed) | same |
| fig5c-6g-slow | partially reproduced (assumed) | same |
| figs7a-6g-extended | not reproduced (assumed) | same |
| figs7c-temporal-lme | blocked (other) | same |
| 8 behaviour, transgenesis and pupae-image claims | blocked (data_missing) | same |
| 4 Brain Image Library claims | blocked (other) | same |
| figs2ab, figs3 | blocked (not_runnable) | same |

**Entry run:**
- **Lock:** the lock file came out unchanged.
- **Check and run:** `entry.py all` found 0 errors, and all three notebooks passed in 47.9 min in total (general_odorants 438 s, alarm_pheromones 1149 s, concentration 1278 s).
- **Numbers:** the three claims with a recorded measured value show the same values in this run (3; 7, 4, 0; 4.8, 70.5), so the conclusions still hold.
- **Handover:** `entry.py handover` wrote `executed/000467-hart-2023/handover/` with the three notebooks, `al_imaging.py` and the claims file.

I did not verify my own work.
