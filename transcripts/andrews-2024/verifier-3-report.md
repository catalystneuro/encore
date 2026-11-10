**Verifier report, round 3: Andrews et al. 2024 on DANDI:001132 version 0.241130.1903**

The claims file has 29 claims and the attempt record has 29 outcomes. Only one outcome carries a `proposed` change: simulation-dampening, from blocked (not_runnable) to reproduced.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| simulation-dampening | reproduced | Yes | — | See below. |

**How the result was produced (cells 28 and 29).**
- Cell 28 builds a throwaway micromamba environment from conda-forge with NEST 3.4, as the published `environment.yml` (printed in cell 27) asks, plus NESTML 5.3.0. Every build step is printed with its exit code and error:
  - With odetoolbox at today's release, the build fails (`simplify_expression`).
  - With odetoolbox 2.5, it fails at cmake. `nest-config --compiler` printed `echo ""`.
  - After `nest-config` is patched to name the environment's compiler, the build succeeds. The printed versions are NEST 3.4, nestml 5.3.0, odetoolbox 2.5.
- Both changes are to the environment, not the model or the script, and both are listed as deviations. odetoolbox is unpinned in the published file and its newest release cannot be called by NESTML 5.3.0, so pinning it is forced, not a choice made to reach the result.
- Cell 29 runs `simulation.py` unchanged. I read the script at commit 6865bf6 myself. It uses 1000 granule and 12 basket cells, `N_perforant=0`, seed 20 and `T=1e3` after a 1 s warmup, which is discarded. It sweeps fractions 0, 0.10, 0.25 and 0.50. The script's own printed lines (80.65, 60.06, 52.49 and 49.65 Hz; opto fired 0, 16, 11 and 9 times) appear in cell 29's output.

**The event measure (cell 30).**
- An event is a run of 1 ms bins of `sd.binned(1)` over all 1012 cells with a count `> threshold`. Cell 30 reads `threshold` from the run's metadata, `opto_threshold`, which is 100.
- This matches the script's closed-loop test (`rec.n_events - last_n_events > opto_threshold` on both populations) and the Methods ("if the total spike count in a single step exceeded a threshold x_opto"). The claims file's "above the closed-loop threshold x_opto the code sets" is therefore applied as written.

**The numbers (cell 30).** All values below derive from the saved runs.

| Seed 20 reading | Fraction 0 | 0.10 | 0.25 | 0.50 | Criterion met |
|---|---|---|---|---|---|
| (a) total event duration, ms | 278 | 124 | 37 | 4 | yes |
| (b) number of events | 10 | 10 | 10 | 4 | no |
| (c) spikes in events | 52,366 | 17,594 | 4,086 | 441 | yes |

The criterion asks for one reading to be lower at 0.25 or less than at 0, and lower at 0.50 than at 0. Readings (a) and (c) both meet it. The verdict uses the script's own seed, which was fixed before any analysis.

**The seed check.**
- For seeds 21, 23 and 24, readings (a) and (c) are at most 0.698 of their value at fraction 0, as the record says.

**Points that do not change the outcome.**
1. Reading (b) fails at seed 20. With seeds 21, 23 and 24 the number of events often rises under light, up to 4.5 times the value at 0 (seed 24 at fraction 0.10). The criterion's "under one reading" allows the verdict to rest on (a) and (c). I report this as a weak point of the claims file's criterion, not a misreading of the paper. The paper's own wording, "length and intensity of seizure-like events", corresponds to (a) and (c).
2. For seed 22, the record says there is "nothing to dampen". That is true at fraction 0 (1 ms above threshold), but at fraction 0.50 the seed does not meet the criterion under any reading: duration ratio 1.0, 103 against 101 spikes. The record should say this plainly. It does not affect the verdict, which uses seed 20.
3. The README gives about 35 minutes for the notebook and 4.4 minutes for the network model. Cell 33 prints 46.5 minutes for the notebook and cell 29 prints 5.6 minutes for the model runs, seed check included.
4. The protocol now lists `not_runnable` (author, step 1.5). That settles my round-1 objection to the reason code.
