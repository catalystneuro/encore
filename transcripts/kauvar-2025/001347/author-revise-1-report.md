I've answered every point in the round-1 report. Five outcomes changed, and the entry re-ran cleanly with `python tools/entry.py all`: the check reports 0 errors, and all five notebooks passed in about 45 minutes. The longest are 04 at 21 min and 05 at 11 min. Nothing is committed or pushed.

**Outcome changes**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig4b | reproduced (assumed) | not_reproduced | Under the criterion's method (baseline subtracted, no normalisation) late eye closure is 0.174 ± 0.061 against 0.147 ± 0.034, and the intervals overlap. The script the criterion names, `fig1_npx_behavior.py`, does not normalise; only `analysis.py` does. That max-normalised reading separates the conditions and is now shown as a variant. |
| fig1no | partially_reproduced | reproduced (assumed) | "Not above" is read as a test. The rise from first to eighth puff is +0.017 (95% CI −0.012 to +0.046) under ketamine and +0.010 under PCP, against +0.350 under saline. |
| fig6j | not_reproduced | partially_reproduced | The claim holds under the code reading the criterion names (0.559, p = 8.7e-05) but not under the Methods rule. That rule divides near-zero correlations, so its ratio ranges from 0.576 to 1.450 across readings. |
| figs15 | blocked | not_reproduced (assumed) | Tested on approximate windows: the Methods put the infusion puff session about 30 min after infusion start. MCC has the largest change (2.644); ORB is third (2.141). The three frontal regions rank above the median region in 24 of 24 variants. |
| figs27 | blocked | reproduced (assumed) | Every high-CADSS participant has a ketamine-only oscillation below 10 Hz (4 of 4 under > 10, 5 of 5 under ≥ 10), in 50 of 54 variants. The detection also finds such channels in low-CADSS participants and in a reference run without ketamine; the notes say so. |

For figs27 I set `data: with_inputs` and `depends_on: cadss-scores-link` in the claims file, because the test uses CADSS scores from the code record. The statement, expected values and criterion are unchanged.

**Added or corrected**
- **figs38a/b:** I ran the fig. S38 code's band edges, and printed site and edge counts per participant along with the code that reads the precomputed edge file (64 readings). No selection gives the paper's 716 edges; they range from 339 to 1020.
  - figs38a stays not_reproduced. Ranking sites by each band's weights, as the criterion and legend say, the absence holds in only 4 of 44 readings.
  - Ranking by beta weights, as a code comment says, it holds in 20 of 20. I recorded this as a new code_mismatch finding.
  - figs38b stays partial.
- **fig6i:** sliding-window variants (2.5-s and 1-s steps) give the same result: the test holds and the ratio is never within tolerance.
- **fig6e and figs37b:** the conclusions now say the absence holds only under the code's z-scoring.
- **figs34:** the code's coupling rule over the windows before tone series (the Methods' window) gives ratios of 0.66 to 1.02, all outside tolerance. The coupling part fails there.
- **fig4hi:** no reading of the interval satisfies both parts (0 of 8). fig5e, fig5g and fig1m now print the code lines the verifier asked for.
- **figs13 and fig2i:** I added the all-preinfusion-trials variant (figs13) and the participant counts per factor (fig2i). The mouse 5 exclusion is stated as an assumption, and fig6h's 13-session result is recorded.
- **Handover:** every conclusion cell now starts with "**Result:", so the figs38a/b conclusions will be removed in future handovers.
- **Records:**
  - `questions/001347.yaml` is new, with reader questions on figs2bc (the expected 0.34 against about 0.20 implied by the paper's own numbers), fig1m (20 against 40 trials) and fig5e (the Methods' window against the code's).
  - I fixed a garbled sentence in the figs2bc notes, recorded round 1 under `verifications` (61 results, 5 disagreements), and updated the README, the notebook summaries, the runtimes and the lock file (adds `fooof`).

**Not done**
- No reading reproduces the paper's 716 edges.
- fig6i's reading (a) and figs15/figs27 cohort (b) cannot be run on this dataset.
- I filed no reader question for figs38a: the claims file follows the legend correctly, and the disagreement is between the paper and its code.
- I changed three conclusion headings and summary rows (fig1no, fig6j, figs38a) after the run. The changes are text only, in both the source and executed copies; I did not re-run for them.
