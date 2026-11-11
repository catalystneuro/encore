I've done steps 1 to 6 of the Author section and built the handover. The entry ran from a clean environment with 0 check errors: the Neuropixels notebook in 123 s and the model notebook in 1903 s. Nothing was committed.

The main result is that the dandiset gives the paper's Figure 4 numbers exactly, but only under the firing rate the paper's own code computes, not the one its Methods describe. The claims file judges each claim under the Methods' rate, so three claims that would otherwise reproduce are partial.

## 1. Outcomes (35 claims)

| Claim | Outcome |
|---|---|
| dataset-sessions-link | reproduced |
| fig4c-sample | partially reproduced: 721 kept and 144 excluded against 662 and 203; exact under the code's rate |
| fig4d-synchrony-lower-awake | partially reproduced: 0.3188 awake (just outside 0.325 ± 0.005) and 0.3862 isoflurane, p = 1.45e-32; exact under the code's rate |
| fig4d-entropy-higher-awake | partially reproduced: 1.389 and 1.150 nats, both outside tolerance, p = 3.3e-30; exact under the code's rate |
| fig4-rate-higher-awake | reproduced (14.0 against 7.6 Hz) |
| figs6-rate-regressed | reproduced: all three regression readings agree, every p below 1e-10 |
| fig4f-model-hyperpolarizing-less-activity | reproduced |
| fig4h-model-synchrony | partially reproduced: 0.7833 and 0.8789; the hyperpolarizing mean is 0.0011 outside tolerance |
| fig4h-model-entropy | partially reproduced: 0.4516 and 0.2014; the hyperpolarizing mean is 0.0024 outside tolerance |
| figs7-model-decoding | reproduced: 0.985 against 0.932, shunting higher in 20 of 20 runs |
| figs4-intrinsic-properties | blocked, `other` |
| 24 patch-clamp claims | blocked, `data_missing` |

## 2. Dataset, assumptions and questions

**What the dataset holds.**
- **Version pinned.** 0.230317.0039 is the only published version and the one the paper's code names. The draft has the same assets.
- **The paper's recordings are all there.** All 17 recordings (16 mice) are present with every field the analysis needs.
  - Unit ids equal row numbers, so the code's keying of units by row selects the right units.
  - Labels and clocks are consistent with the data: evoked spiking is 3 to 18 times the spiking in time-shifted windows, and the isoflurane trials fall inside the isoflurane epoch.
  - There are no duplicate files.
- **Code mismatch on the firing rate.** The paper's code sums spike latencies where the Methods describe an average firing rate. That rate gives exactly 662 kept, 203 excluded, a median of 34 per recording (1 to 93), and the Figure 4D means. Its 200 Hz exclusion bound therefore acts on spike-count rates near 45 Hz.
- **Undocumented selection.** One file with units and stimulation, sub-599017, is in the version but not used by the paper, and the paper does not say why. Six other files hold EEG only.
- **Missing data.** The patch-clamp recordings (Figures 1 to 3, S1 to S5) are not deposited anywhere. A DANDI search for gramicidin, Akerman, Burman and EGABA found nothing.
- **Minor code mismatch.** The waveform cut (≥ against > 0.4 ms) and the area rule differ between the Methods and the code, but select the same 865 units here.

**Assumptions:** none (no outcome is marked `assumed`). The Figure S6 regression method is open, but all three readings in the criterion agree.

**Questions for the paper's authors:** none filed. **Questions to a reader:** none. The claims file follows the Methods, as the protocol requires; it does not misread the paper.

## 3. Protocol gaps

1. There is no block reason for a claim whose method lives only in a supplement that was not supplied (Figure S4, which also needs Matlab). I used `other` and explained it in the notes.
2. The protocol makes the Methods reading decide the outcome even when the code's reading reproduces the paper exactly. I followed it, recorded the code mismatch as a finding, and showed the code's reading as a variant.
3. "Fix every random seed" conflicts with the model criterion's "seeds as given by the gist (none set)". I fixed seeds 1 to 20 and recorded it as a deviation.
4. The paper's simulation builds a 4 GB stimulus array that does not fit in memory, and the protocol says nothing about changing an outside input's code. I held one periodic stimulus set instead, showed it gives identical spikes on a small run, and recorded the change.
5. For stochastic simulations, the paper's SEM over pooled neurons is narrower than the spread between seeds, and the protocol has no rule for this. I applied the criterion as written, so the two model claims are partial, and noted the spread.
6. The clock-check guidance (decoding a task variable around trial starts) is heavier than needed here. I used a shifted-window contrast on two files at full length.
7. `entry.py check` requires every notebook to name the dataset, including the simulation-only one, so that notebook imports the version constant from the helper.

## 4. Runtime and failures

- **Runtime.** The agent run took about 2 h 10 min (05:13 to 07:21 UTC). The entry was run in full twice, about 35 min each; the second run came after correcting the Figure S4 block reason in the notebook text.
- **Failures.**
  - A first parallel test with 2 repeats failed because 5-fold cross-validation needs at least 5 repeats; I re-ran with 5.
  - The loader first crashed on the six files with no units table; it now handles them.
  - Nothing failed in the final run.
- **Files I did not create.** `git status` shows untracked dotfiles at the repo root (.bashrc, .gitconfig, .vscode and others), a `scripts/` folder, and an `entries/burman-2023/.claude/` folder. I left them alone; `.claude/` looks like a harness file, so you may want to exclude it from the commit.

Files are in `entries/burman-2023/`:
- `reproduce_burman_2023.ipynb`
- `network_model.ipynb`
- `npx.py`
- `network.py`
- `README.md`

The attempt record is `attempts/burman-2023-01.yaml`.
