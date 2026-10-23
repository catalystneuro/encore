The paper answers none of the five questions. For each one I've said so in `answer`, written the readings the paper allows into the criteria, and set `answered: 2026-10-21`. No statement or expected value changed. `python tools/claims_check.py` reports 33 quotes and 0 problems. The paper links no code, so these answers come from the text alone.

1. **ephys-pt-it-onset-not-detected:** The paper gives no method for the Li et al. (2015) units, only their counts (45/27) and, for its own probe units, "the same analyses as imaging data" with 400 ms windows in 100 ms steps. The criterion now names these readings:
   - 400 ms windows in 100 ms steps.
   - The four trial types without photostimulation trials, early-lick trials excluded by the early-lick record.
   - Time measured from pole movement onset, which this paper calls trial start.
   - Baselines O1 and O2, with onset rules S1 and S2.
   - Units of all sessions pooled, with the bootstrap both over units and hierarchical.

   The outcome rule is now: reproduced when no combination of readings finds PT earlier at p < 0.01, partially reproduced when only some do.
2. **fraction-selective-alm-mm:** The Methods give (F-F0)/F0 with no exception for F0 ≤ 0. Convention T now uses dF/F as computed (V1), which decides; leaving out the ROIs with F0 ≤ 0 (V2) is reported as a check. The five dF/F claims named in the question now cite it.
3. **fig8d-pt-earlier-than-it:** The paper gives only ">6 SD above baseline". "Above baseline" is read as above the baseline mean. Convention O now names two onset rules: the first bin over the threshold (S1), or the first bin from which it stays over the threshold up to the go cue (S2).
4. **figs4-peak-shift:** Figure S4 is not in the text, so neither term is defined. The criterion now reads the sample-epoch level as its mean or its maximum, and the end of the delay as the last bin or the last 0.5 s. One combination is enough; all are reported.
5. **fig6-lick-direction-spread:** Figure S7 is not in the text. Part (c) now reads both the mean over the delay bins and the maximum there, and holds under either.

Only `claims/000015/` and `questions/000015.yaml` were changed, and nothing is committed. `git status` also lists some untracked files (dotfiles, `.idea`, `scripts`, and others) that I did not create.
