No outcome changed and none is proposed. The verifier agreed with all 30 outcomes (reproduced: link-authors-deposit and data-scale; partially reproduced: fig6e-marker-clustering; blocked as data_missing: the other 27), so a third round is not needed. I re-ran the entry with `python tools/entry.py all entries/wang-2025`. It passed, and the entry's check reports 0 errors. Every printed number is the same as in the run the verifier reviewed, except the timed video read rate. Nothing is committed.

**Text the verifier said the numbers did not support, now corrected:**
- **Read times in the 27 blocked notes:** they now give this run's figures, 1.4 h a session and 47 h for the 34 sessions with video. They also say the timed rate varies from run to run (1.3 h and 44 h in the run the verifier saw).
- **fig6e variant:** the summary and the notes now say 166 of the 167 sessions that pass the clock check are decoded.
- **Finding 7:** it now says the Methods give 28 mice and the Results give 105 sessions (Fig. 2c–e) and 106 (Fig. 6). Before, it put the 105 in the Methods.

**Remaining points the verifier raised:**
- **fig6e:** the result cell and the notes now say the effect is weaker *under this decoder*. The decoder is itself weaker than the paper's: its response-epoch AUC is 0.754 against the paper's 0.88, and its delay-epoch AUCs are 0.61 for the jaw and 0.59 for the nose. So the Calinski-Harabasz score of about half the paper's may come from the decoder and not the data.
- **data-scale:** the notes and the notebook now say that "ALM" means isocortex units on probes aimed at ALM, so it may include neighbouring motor cortex, and that the margin over the threshold is narrow (13 structures against more than 12).

**What I added:**
- **A new notebook cell 11, checking finding 1's doubled frame interval without using the licks.** The verifier agreed the finding is critical but noted the 6.8 ms frame spacing was inferred, not measured.
  - In mice SC011 and SC022, the five flagged sessions have trials as long as the other eight sessions (median 4.83 to 4.90 s in all 13).
  - But they hold 934 to 946 frames per trial video, against 1864 to 1886 in the other eight. That works out to 6.76 to 6.81 ms a frame.
  - The video in the later dataset version can't settle it directly: it has the same frame counts and no real timing (a placeholder rate of 1.0, no timestamps).
  - The finding keeps its critical rating, and its statement now says the spacing is inferred from frame counts and licks.
- **Round 2 under `verifications`:** all 30 claims, with the verifier's reasons and my responses. Under the round's `findings` I recorded finding 1, which it agreed with.
- **No question for a reader:** the verifier found no place where the claims file misreads the paper.

**What I did not do:**
- **Finding 2 (SC026_080719) stays major.** The verifier said it would make it critical only if videos filed under the wrong trials were confirmed, and called major defensible. Confirming it is a new analysis, and the run already sits at the 60-minute limit.
- **Runtime is the main risk.** The first re-run finished every cell but failed for going 7 s over the limit; the slow part, reading and decoding the sessions, took 51 min against about 32 min before. I raised the worker pool from 4 to 6, which does not affect the results. The second run passed in 3589 s, only 11 s under the limit, so a later run on a slow network could fail on time.
- **One small inaccuracy left in the notebook.** Cell 12 gives the trial durations as "median 4.85 to 4.90 s", which covers the five flagged sessions only; across all 13 it is 4.83 to 4.90 s. The record has the right range. Fixing the notebook would have meant another hour-long run at that limit.
