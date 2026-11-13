I've finished the author steps for niknam-2019 (steps 1 to 6). `python tools/entry.py all entries/niknam-2019` reports 0 errors, the notebook runs in 49 s, and the handover package is in `executed/niknam-2019/handover/`. Nothing is committed. Of the 34 claims, 8 were tested and 26 are blocked; most of the blocked ones need the paper's models, which can't be fitted within the run's limits.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| probe-locations-link | reproduced |
| methods-neuron-counts | reproduced |
| fig1b-saccadic-suppression | reproduced (8 neurons; 2.24 → 1.24 against the paper's 2.53 → 1.51) |
| fig1c-ff-remapping | not reproduced (8 neurons against 23) |
| fig1d-st-remapping | not reproduced (11 against 37) |
| fig1e-ff-and-st-remapping | not reproduced (6 against 22) |
| fig1-remapping-longer-latency | reproduced (RF peak 62 ms; FF 108 ms, ST 99 ms) |
| fig1-example-neurons | partially reproduced (3 of 4 examples matched) |
| fig5a-n-model-no-perisaccadic-gain | blocked: methods_underspecified (the N-model) |
| 24 claims on the S-, F- and A-models (Figures 3, 5 to 8, S4, S5) | blocked: too_large |
| figs1-rf-centres | blocked: metadata_insufficient |

**2. Dataset, assumptions, questions**
- **Pinned version:** CRCNS mt-3 is unversioned and the bucket holds one copy (`live/`), so it is recorded as `unversioned` with the MD5 of `data.zip`, which the notebook checks against `checksums.md5`. All 41 neurons are there, from 11 sessions, matching the descriptor's per-session counts. Each recording appears once, and the files are identical to the copies in the paper's code repository.
- **Clocks:** the RF response peaks 58 ms after probe onset and disappears when the stimulus codes are shifted by 300 ms. Aligning on the true saccade times gives a larger rate modulation than shuffled times.
- **Missing from the data:** the saccade direction, the RF, FF and ST probes, the grid's position and spacing, and which monkey each session comes from. The probes exist only in `main_lists.mat` in the code repository.
- **Probe timing differs from the paper:** 91.5% of probe runs last 7 ms; the rest are mostly 6, 14 or 21 ms, and there are 10 to 21 ms gaps with no probe on screen. The arrays are 3000 ms long, while the paper gives trials of 2100 to 2300 ms.
- **Undocumented tables:** `main_lists.mat` holds five more 41 × 6 tables that look like the paper's own per-neuron classifications. `nuron_list` counts 8, 23 and 37 neurons, matching the paper. They are shown for reference only and decide no outcome.
- **The main open method question:** the Methods name a one-sided signed-rank test without saying what is paired. Pairing by trial gives no pairs at all, because no trial shows the same probe in both windows. Pairing by condition reproduces the suppression count but finds far fewer remapping neurons.
- **Example neurons:** three examples match neurons with perisaccadic rates equal to the paper's to two decimals. Their fixation rates are slightly lower, which suggests the paper used a slightly different fixation set.
- **Assumptions:** none decide an outcome; every outcome follows the readings the claims file names.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): what produced the Figure 1 classification (presentations, pairs and test), and which publication and code define the N-model.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. The claims file's reading O1(a) cannot be run on these data (no pairs). I showed that it gives zero pairs and let reading (b) decide.
2. `too_large` and `not_runnable` overlap for a computation that exceeds the time limit. I used `too_large` with an estimate measured in the notebook, as "Develop on a subset" says.
3. An estimate measured on a straightforward port depends on how efficient the port is. Mine gives about 1,000 h on 4 CPUs, so I also measured a lower bound for a fully batched port: about 7 h, still over the 60-minute notebook limit and the time left.
4. The N-model is defined only by a cited reference that the text read doesn't identify. It could be `methods_underspecified` or `not_runnable`; I followed the claims file's O8 and used `methods_underspecified`.
5. The protocol has no category for the paper's own per-neuron results found in its code repository. I listed them under `inputs` and showed them for reference only.
6. Results are to be broken down by animal, but no animal identifier exists. I broke them down by session and by saccade direction, and recorded the missing identity as a finding.
7. Blocked model claims have no cell of their own, so their `output` points to the shared benchmark cell.

**4. Runtime and failures**
The run took about 25 minutes (05:16 to about 05:40 UTC); the notebook takes 49 s with 1.35 GB peak memory. Nothing failed. The benchmark timing varies a little between runs, so those figures are rounded in the text. The checkout has untracked dotfiles at the top level (`.bashrc`, `.idea`, `scripts`, and others) that I didn't create; I left them alone.
