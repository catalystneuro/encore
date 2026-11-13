I answered both questions. Both claims misread the paper, so the claims file changed for each. `python tools/claims_check.py` reports 0 problems, and both files still parse as YAML. Nothing is committed or pushed.

1. **edtable1-region-counts: changed.** The table counts every neuron in the 42 regions, meaning every curated single unit with a trial firing rate of at least 0.1 Hz. Its neuron column sums to the Results' 22,458 "localizable to one of 42 brain regions". Its responsive column gives the 60.0% (13,466) that `task-modulated-fraction` already uses. The rule of 13 per session applies only to "further analysis".
   - The criterion now counts those neurons, with definition N as a variant.
   - The recordings count has two readings: (a) sessions with any neuron of the region, or (b) sessions with at least 13.
   - `supptable2-sessions` now takes its area lists from the same neurons and readings.

2. **fig4d-jpecc-vis-leads, and with it fig4d-jpecc-no-lag-frontal-midbrain: changed.** The Methods do one PCA per region group "across time points and trials", while jPECC.m fits a new PCA for each time bin. Where they disagree, protocol Reader step 2 puts the Methods first. The criterion now uses the Methods' PCA, with the code's per-bin PCA as a variant. The no-lag claim takes its method from `vis-leads`, so its own text needed no edit.

I did not add a `checks` entry to the claims file. The changes and their reasons are recorded in each question's `answer`.
