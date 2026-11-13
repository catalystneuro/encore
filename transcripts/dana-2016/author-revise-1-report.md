I've revised the attempt for every point in the round-1 report. The entry re-ran cleanly with `python tools/entry.py all entries/dana-2016` (pass, about 3 minutes, 0 check errors), and every conclusion matches the new outputs. Nothing is committed.

**Outcome changes**
- **`fig4d-event-counts`: partially_reproduced → not_reproduced.** This is problem 1. The Methods say events are isolated by more than 1 s, and the claims-file header says the Methods win when they and the script disagree. The script uses 0.8 s after the event, even though its own comment says 1000 ms. So isolation (a) is now the main reading, and under it 6 of 18 counts are within tolerance, the best of the claim's readings. The script's isolation is still shown as a variant: it gives 11 of 18, with all nine jRGECO1a counts exact. The `code_mismatch` finding now says the published jRGECO1a counts look like they came from the script's 0.8 s.
- **`fig4g-kinetics-like-gcamp6`: blocked → not_reproduced.** The notebook now reads Chen et al. (2013b) Supplementary Tables 3 and 1 from the PMC open-access copy, added under `inputs`. Under the main reading none of the four times is within 25% of the matching GCaMP6 value. Across all 24 combinations of readings and variants, at most 2 of the 4 pass.
- **Everything else is unchanged, re-measured under isolation (a):**
  - jRGECO1a 1 AP detection: 84.3%.
  - jRGECO1a 2 AP detection: 100%.
  - jRCaMP1a detection: 63.3% and 80.7%, still reproduced and marked assumed.
  - jRGECO1a above jRCaMP1a in amplitude and d′: 8 of 8 values of n.
  - jRGECO1a faster: half rise 15 against 47 ms, fitted decay 225 against 2300 ms.

**Added or corrected**
- A cell that prints the three .m scripts, so the "script" rules can be checked line by line (problem 8).
- A table of jRCaMP1a counts and rates under each isolation reading, with all recordings, without `data_20150707_cell1_001`, and without both recordings that failed the clock check (problem 3). Without it the 1 AP rate is 71.7 to 75.4%, outside tolerance under every reading. I kept it, because it is the only recording of its cell and dropping it leaves 9 cells where the paper reports 10. The notes now say the outcome depends on it, and the question to the paper's authors asks whether it was included.
- Robustness tallies now also count only the claim's own isolation readings, and separately only the combinations whose noise traces cannot contain a spike's transient (problem 4).
- The kinetics conclusion now covers the short fit window, the jRCaMP1a traces dropped from the trace measure, and the ranking by RMS relative to the peak (problems 5 and 6).
- `questions/dana-2016.yaml` is new, with three questions for a reader:
  - whether `culture-jrcamp1-dynamic-range` should be `data: elsewhere`, since Figure 2, source data 1 is public on eLife;
  - the same for the five fly claims, since Figure 7, source data 1 to 3 are public;
  - which measure the GCaMP6 comparison means, because Chen et al. report 1 AP time to peak, not a 2 AP half rise.
- The attempt record has round 1 under `verifications` for all 35 claims, with the verifier's reasons and my responses. Notes, deviations, findings, README, `entry.yaml` (runtime), `requirements` (adds pypdf, re-locked) and the notebook summary are updated to match.

**Not done**
- I kept the script's segment as the main reading for problem 2 and did not switch to the claim's named segments. The Methods don't give the segment, and the claims-file header makes the script the main reading where it settles an open detail. For jRGECO1a 1 AP, one of the claim's own combinations is within tolerance anyway (76.3%). For jRCaMP1a the result still rests on the stated assumption.
- I didn't test the claims behind the eLife source-data tables, because the claims file marks them `data: dataset`. That is now a question for a reader.

`git status` also shows untracked files I didn't create (`.bashrc`, `.bash_profile`, `.gitconfig`, `.profile`, `.zprofile`, `.zshrc`, `.ripgreprc`, `.mcp.json`, `.idea`, `.vscode`, `scripts/`). I left them alone.
