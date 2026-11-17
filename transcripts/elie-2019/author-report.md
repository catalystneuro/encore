The entry is written, locked and checked (0 errors), and the notebook ran from a clean environment in 13.3 minutes. `tools/entry.py handover` built the verifier's package in `executed/elie-2019/handover/`. Only one of the 25 claims could be tested: almost all the others rest on the paper's 404 units, which the files do not identify.

**1. Outcomes**

| claim | outcome |
|---|---|
| fig1-model-neurons (data: elsewhere) | partially reproduced |
| units-404 | blocked, methods_underspecified (the reason the criterion names) |
| units-337, s1, fig2a, fig2cd, fig2b, s2, fig6a, fig6c, fig6b, fig7a, fig7b, k300-rate-regression, fig9a-mean-cii, fig9a-top-quartile, s7, fig9b, fig9c, cii-unimodal | blocked, methods_underspecified (they rest on units-404); also too large to run, see section 4 |
| fig3-5-example-neurons | blocked, methods_underspecified (the paper does not name the three units) |
| table1-anatomy-counts and the four fig10 claims | blocked, data_missing |

- **Why fig1 is only partial:** the code repository holds one of the three model neurons in Fig 1, the temporal one. On that neuron all three conditions pass:
  - KDE error 0.009 spikes/ms, against a limit of 0.02.
  - Cumulative information reaches 1.928 bits, against a threshold of 1.8.
  - Peak instantaneous information 0.519 bits, within 0.5 ± 0.05.
- **KDE port:** the Python port matches the KDE saved by the paper's MATLAB tutorial to 0.0004 spikes/ms on average.

**2. Dataset, assumptions, questions**
- **Unit labels missing:** there are 1281 files labelled single units, and 1246 pass the 2.3 bits/s auditory threshold. The files do not mark the 914 single units or the 404 the paper analyses. The spike-shape quality score (SNR) that defines a single unit is not stored.
- **File counts:** the description says 688 multi-units and 914 single units. The files are 845 unsorted multi-unit files and 1453 spike-sorted files.
- **No anatomy:** there are no brain areas or coordinates for the recording sites, only electrode depths.
- **Stimulus and trial counts:**
  - Call stimuli per unit average 95.4, against the paper's 114.
  - Stimuli of any kind average 121.9, against the description's 144.
  - Some stimuli have 12 trials, against a stated maximum of 11.
- **Labelling errors:**
  - Three files store `sortType` as "singl".
  - The description spells one bird's name two ways (WhiBlu5896M and WhiBlu5396M).
  - The `.f32` spike-waveform files are undocumented.
- **Data checks that passed:** no recording is deposited twice, and spike times share the stimulus-onset clock. Before onset, about 1% of units respond differently by call type; after onset, 44% to 66% do.
- **Assumption (fig1):** the jackknife replicates of the Monte Carlo estimate share their random draws. With independent draws the result still passes, so the outcome does not rest on this.
- **Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
  - Can the lists of the 914, 404 and 337 units be published?
  - Do the jackknife replicates share Monte Carlo samples?
- **Questions to a reader:** none.
- **Variants that decide nothing:** I ran the cheap measures on all 1246 auditory single units instead of the 404, so they describe the units the files hold. Fano factor 1.027 (paper 1.04); stimulus correlation 0.29 (paper about 0.4). Coherence below 50 Hz is 65.8% against the paper's 96.7%. The coherence curve stored in the files may not be the one S1 Fig used.

**3. Protocol points**
1. **Missing base set:** the units-404 criterion assumes the 914 units can be found; it does not say what to do when the starting set itself cannot be identified. I blocked the claim with the reason it names (methods_underspecified) and said in the notes that the main cause is missing labels.
2. **Two block reasons:** "A claim that depends on a blocked claim is blocked for the same reason" conflicts with a claim that has its own, stronger reason. For the anatomy claims I used data_missing as the main reason and noted the inherited one.
3. **Variants:** the protocol does not say whether analyses on a stand-in population may appear when the dependency is blocked. I showed them, marked as deciding nothing.
4. **CRCNS layout:** `archives.md` describes zip files, but aa-4 is tar.gz archives. Those can only be read front to back, so the notebook reads all 7 GB on every run.
5. **One file instead of three:** the claim names three model neurons and the code repository holds one. I recorded partially reproduced.

**4. Runtime and failures**
- The session used about 1 h 26 min (20:25 to 21:51 UTC). The notebook runs in about 13 minutes, 7.5 of them reading the data from S3.
- The first loader took 18 minutes on one core; switching to separate processes fixed that.
- Nothing failed. Independent random draws in the jackknife made the cumulative information unstable, which led to the shared-draws assumption above.
- The paper's KDE pipeline was estimated at 146 hours on one core, or 37 hours on 4, for the rates alone.
- Untracked files I did not create are in the checkout: dotfiles at the repo root and `entries/elie-2019/.claude/`. I left them in place.

Nothing was committed.
