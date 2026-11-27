I've revised the attempt for every point in the round-1 report and re-run the entry with `python tools/entry.py all entries/wei-2023`. It passed in 2571 s, about 43 minutes, so I raised `runtime_minutes` to 50. The checks give 0 errors, and every conclusion matches the executed notebook. Nothing is committed.

The main change is the unit set. For problem 1 I found why the paper's units differ: every unit in the code's own unit tables has at least 100 spikes in the first 5-min gray screen, while 270 of the 297 reading (a) units outside those tables have fewer. So the claims after fig1d now use a third reading, (c): reading (a) plus that 100-spike condition. It comes from the paper's "well-isolated … during spontaneous activity" and the Methods' 100-spike rule, and I record it as an assumption. It keeps all 603 reading (a) units of the code's tables and adds 27, where reading (a) added 297. Readings (a) and (b) and the Source Data labels are still printed beside it. About half the paper's units remain, so several weaker effects lose significance.

I also changed how depth is set. The code's depth turns out to be the probe position minus one layer-4 centre per probe, so I now take depth from the paper's own centres. My CSD centre is kept as a variant; it differs from them by −420 to +340 µm per probe, and the CSD plots are added.

**Outcome changes:**

| Claim | Was | Now | Why |
|---|---|---|---|
| fig2-fs-rs-counts | not reproduced | reproduced | FS fraction 25.4% under (c), within 23.3 ± 2.33 |
| fig3a-isi-fs-rs | not reproduced | partially reproduced | both medians within 10%; matches the verifier |
| fig7g-pvalb-more-symmetric | not reproduced | reproduced | tagged units now pass the code's exclusions; t-test p = 0.0034 |
| fig7h-pvalb-higher-cv | not reproduced | reproduced | Pvalb CV higher within presentations, p = 0.0013 |
| fig6cf-kv31 | reproduced | partially reproduced | only 5 conductances are public; matches the verifier |
| figs5-depth-distribution | reproduced | not reproduced | p = 0.25 with the paper's layer-4 centres |
| fig3a-rs1-excitability | reproduced | partially reproduced | one of three measures holds under each period |
| fig3a-rs23-visual-responses | partially reproduced | not reproduced | no metric holds in full under (c) |
| fig3c-fs-more-phase-locked | partially reproduced | not reproduced | only 2 bands significant |
| figs6c-fs-stronger-across-depth | partially reproduced | not reproduced | FS higher in 13 or 12 of 15 cells, not all 15 |
| fig7e-pvalb-sst-one-channel | partially reproduced | not reproduced | TPW p = 0.013, above 0.01 |

All outcomes resting on reading (c), the depth source, the forced K = 3 or the opto exclusions are marked as assumed. fig5c is now marked seed-sensitive: one of the five seeds goes above 94%.

**Where I kept my outcome and recorded the disagreement:**
- **figs3b-fs-faster:** the verifier says not reproduced; I kept partially reproduced, because FS is faster under every reading and only the medians miss.
- **figs5-depth-distribution:** the verifier says partially reproduced; I give not reproduced, because neither the clusters found here nor the paper's labels differ in depth on the paper's own placement.
- **figs8-rotation-symmetry:** I kept the block as `not_runnable`. The claims file marks it `data: elsewhere`, and the check rejects `data_missing` for such claims. The notes now say the models and simulations are not public.

**Fixes and added output:**
- `name_by_overlap` now returns only names it was given.
- Reading (b) now includes the units of quality noise, as the criterion words it.
- LV no longer pairs ISIs across trial boundaries.
- Spikes now map to the nearest LFP sample.
- Per-session, per-feature table of mismatches with the Source Data features.
- The paper's own Fig2d features, clustered: K = 3 for FS and RS, with the paper's labels for all 1204 units. So the clustering method reproduces, and the fig2d failure comes from the features recomputed here.
- An LFP channel at least 100 µm from the peak. Spontaneous theta locking stays at about 93% (FS) and 81% (RS), so the unit's own spike does not explain it.
- Classifiers:
  - Every classifier now runs on readings (b) and (c).
  - I added label-permutation baselines and versions that split the data before upsampling.
  - The code's order (upsample, then split) inflates the random-forest scores: 61.7% on shuffled labels against about 33% chance.
- Opto table now shows direction and both periods for every tagged set.
- Counts of in vitro cells missing a value.
- A t-test for fig6g.

**Record and questions:**
- **Round 1 under `verifications`:** each claim has the verifier's reason in close paraphrase and my response.
- **Two new findings:**
  - The electrodes tables' CCF coordinates are NaN in 6 of 24 sessions, and in the other 18 y equals z on every channel, so the CCF-layer reading cannot be run. Rated major.
  - The classifier inflation, filed as a finding about the paper.
- **`questions/wei-2023.yaml`:** asks a reader about the claims-file gap that the isolation readings carry no spontaneous-activity condition.

**Not done:**
- The 3 SD outlier step is not applied to the opto-tagged units, because it depends on the pooled wild-type units.
- I did not search further for the model parameters beyond the two repositories and the Source Data.
- The 12 missing sessions are still not available, so every dataset claim is judged on 13 of 25.
