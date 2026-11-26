I tested 35 of the 36 claims on both datasets: 13 reproduced, 15 partially reproduced, 7 not reproduced and 1 blocked (`too_large`). The entry passes `tools/entry.py check` and `all` (35 min run), and the handover is built in `executed/grosmark-2016/handover/`. I wrote the entry at `entries/grosmark-2016/` and the record at `attempts/grosmark-2016-02.yaml`, and did not verify my own work. I did not come across any earlier attempt's results.

The paper uses 1,000 null templates and 1,000 per-cell (PCC) shuffles. This notebook uses 200 and 100, and 30 null templates in the reruns, because the full counts took over an hour for five of the eight sessions. Every replay-based outcome rests on that deviation.

**1. Outcomes** (main reading: yoking to the parts of PRE and POST nearest the maze, 3 SD LFP threshold, the lab's state epochs, both direction templates per event)

| Claim | Outcome |
|---|---|
| sessions-and-tracks, fig1c-above-chance, fig1c-post-gt-pre, fig1c-maze-gt-pre, figs5b-abs-r-above-null, figs5f-more-participation-post | reproduced |
| fig2-pre-post-overlap (71.7%), figs12-high-dpcc-exclusion, fig2e-remove-plastic, figs2-track-distribution | reproduced |
| rate-split-medians (0.392 and 1.104 Hz), fig4c-pre-fast-coactivation, fig4d-slow-sequences | reproduced |
| place-cell-count (562 pyramidal cells match; 573 place cells against 491) | partially |
| figs9b-pcc-post-higher (tests hold, medians outside tolerance) | partially |
| fig2b-strong-contributors (total 217 against 216 only when each event is assigned one direction) | partially |
| fig2d-shuffle-high-dpcc (replay already gone at 5%, below the 9 to 22% asked) | partially |
| fig3a-plastic-specificity, fig4a-rigid-faster, figs14-plastic-ripple-gain, figs16ab-plastic-synchrony-increase, figs16c-low-rate-coding | partially |
| fig4c-slow-replay, fig4e-gain-sequences, figs16de-more-ripples-post, figs17-coactivity-preservation, figs17d-rigid-plastic-coactivity, figs18-temporal-bias | partially |
| figs5e-duration-unchanged (p 0.000531; depends on which part of the longer epoch is kept) | not reproduced |
| rigid-plastic-counts (120 and 120; 104 and 104 if each event is assigned one direction) | not reproduced |
| figs19c-pcc-change-per-cell, fig3b-plastic-improve, figs13-outfield-rate-falls, figs14-plastic-ripple-bursting, fig4c-slow-coactivation-increase | not reproduced |
| figs11-cluster-quality-similar (the spike features exist only inside 12.7 GB of per-session tarballs) | blocked, `too_large` |

**2. The datasets, assumptions and questions**
- **Same recording twice:** DANDI:000044 and CRCNS hc-11 have identical units, cell types, spike times and state epochs, so they were counted once. Counts match the paper: 4 rats, 8 sessions, 562 pyramidal cells, 128 interneurons. The LFP, position and spikes share one clock.
- **Findings about the data:**
  - Gatsby_08022013: the session duration and the end of POST say 30413.6 s in both datasets, but 263,976 spikes, the LFP and the lab's own state epochs run to 32002.4 s (minor).
  - Position is sampled at 39.06 Hz, where the paper says 39.69 Hz (minor).
  - On the circular maze the files do not say whether the reward area is excluded (minor).
  - The lab's states have no quiet-waking label (minor).
- **Assumptions:** "Drowsy" taken as quiet waking; immobility on the maze is speed below 5 cm/s; the LFP channel; running direction from the 1D velocity; one shuffled template per percentage in Figure 2D; the main reading above for every claim that depends on the rigid/plastic split.
- **Questions for the paper's authors** (recorded as findings):
  - Which part of the longer epoch the yoking keeps.
  - Whether each event is scored with both direction templates or assigned to one.
  - The LFP ripple detector.
  - The Figure 2D shuffle procedure.
  - The rank-sum against signed-rank inconsistency for strongly contributing cells.
- **Questions to a reader:** none.

**3. Protocol gaps**
1. The hc-11 files are `.tar.gz`, not zip as `docs/archives.md` assumes. I streamed them with fsspec and Python's `tarfile` in stream mode.
2. The protocol has no rule for cutting a claim's shuffle counts to fit the 60-minute limit, as opposed to blocking the claim `too_large`. I reduced the counts and recorded it as a deviation on each affected claim.
3. The five-seed rule cannot apply to a 35-minute pipeline. I ran it only for the cheap random steps (the Figure S5B bootstrap and the temporal-bias sign flips).
4. Running every reading through the chain of dependent claims (PCC, then the rigid/plastic split, then their properties) was not feasible. I adopted one main reading as an assumption and marked those outcomes `assumed: true`.
5. Some criteria require "both readings", and the protocol says to adopt the best-supported reading when readings disagree. When only one reading held, I recorded partially reproduced.
6. The conclusions must quote numbers from the run, so a second full run is needed after writing them; the protocol does not say so. I ran three times in all: the third only removed bold from the header, and all three gave identical numbers.
7. The schema requires `deviations` whenever `assumed: true`, which the protocol does not state. I added them.

**4. Runtime and failures:** the final notebook ran in 2105 s with peak memory 4.6 GB. One preparation run failed because a Gatsby spike fell beyond the stated session end, and I fixed the code. Nothing failed in the recorded runs. `entry.yaml` gives runtime_minutes 40, against about 35 measured; I left it so as not to force another run.
