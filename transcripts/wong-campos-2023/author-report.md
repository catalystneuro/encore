Those are character devices (`/dev/null` bind mounts the sandbox put there at 12:33, before the run started), not my files, so I left them alone. The work is done: the entry passes its checks, runs in 47 s, and the verifier's handover is built in `executed/001791-wong-campos-2023/handover/`. Nothing is committed.

## Report: DANDI:001791 against doi:10.1101/2023.05.25.542363 (author run)

### 1. Outcomes

| Claim | Outcome | Rests on an assumption |
|---|---|---|
| fig1d-light-intensity-spike-rate | partially reproduced | yes (pulse times inferred) |
| fig1fg-dendrite-peaks-after-soma | partially reproduced | yes (peak timed between frames) |
| fig2c-no-trial-variation | blocked, data_missing | |
| fig2e-half-amplitude-distance | reproduced (238.9 μm, R² 0.491) | yes (LR site set) |
| fig2f-delay-range | not reproduced (delays 0.00 to 3.92 ms) | |
| fig2f-conduction-speed | reproduced (0.088 m/s, R² 0.462) | yes (LR site set) |
| fig3d-dendrite-cross-correlation | partially reproduced | yes (which branch pairs) |
| figs9-shot-noise-bound | blocked, data_missing | |
| fig3i-coupling-vs-distance | blocked, data_missing | |
| figs11-dendritic-spikes-rare | blocked, data_missing | |
| fig4a-doublet-isi | not reproduced | |
| fig4bc-doublet-first-fails | reproduced | yes (spike threshold) |
| fig4d-accelerating-amplifies | reproduced | yes (spike threshold) |
| fig4fg-opto-first-bap-attenuated | blocked, other (at most 2 distal dendrites, all in one recording) | |
| fig4h-biphasic-bap-amplitude | blocked, other (depends on fig4fg) | |
| figs13-distal-more-modulated | blocked, other (depends on fig4h) | |
| fig4ijk-sensory-first-fails | partially reproduced | |
| fig4l-sensory-plateau | not reproduced (264 ms against 400) | |
| figs12-spontaneous-failures-both-states | reproduced | |

### 2. The dataset, assumptions and questions

**Version.** I pinned 0.260424.0313, the only published version; the paper cites none. The draft has the same paths and sizes.

**What the dataset holds.**
- Per-branch traces and summary tables from the authors' pipeline, grouped by figure, plus nine HiLo z-stacks.
- The 44 assets are 22 pairs of byte-identical files. One recording also appears a third time.
- The files follow a later version of the paper than the preprint the claims were read from: 12 neurons for Fig. 2 (preprint 5), 7 for Fig. 3d (preprint 3), and 238 triplets in 5 neurons for Fig. 4d (preprint 186 in 3).

**What is missing.** Imaging movies, recordings of dendrite-targeted stimulation, the Fig. 2 traces, the record of the Fig. 1 light pulses, and morphology reconstructions.

**Errors in the files.**
- The "delay" file labels its delays as amplitudes in −dF/F, and repeats 17 rows three times in one series.
- The deposited Fig. 3d table has 30 correlations above 1.
- The anesthetized file of the Fig. 3 neuron is described as awake.
- The Fig. 4a-d spike times are stated as frame indices but are seconds, one frame after the soma's peak.
- Two optogenetic recordings list stimulus onsets closer together than the stated stimulus length.
- Spike times are unsorted in two sensory recordings.
- No deposited delay exceeds 3 ms, the Methods' cut-off for distal dendrites.

**Assumptions.**
- **Fig. 2 sites:** the preprint's 30 sites are the 30 sites of the Lucy-Rho (LR) construct, the only construct the preprint describes; its n = 30 equals that count.
- **Fig. 3d pairs:** the result rests on the pair set. Only the Fig. 3 neuron gives the paper's values (0.903 and 0.732). The three neurons recorded in both states give 0.863 and 0.803.
- **Spike threshold:** where 5 and 4 robust s.d. disagree, I adopted 4, because it recovers more of the deposited spike times (recall 0.72 against 0.41).
- **Peak timing:** a parabola fit between frames, since the dataset's own delays are given to 0.01 ms at 2 ms frames.
- **Fig. 1 pulses:** pulse times inferred from the traces, with the 1 s period read from them.

**Questions for the paper's authors.** These are recorded as two `methods_unavailable` findings and in the claim notes. They cover the spike detection method, the doublet definition, which sites and fit give the 50% distance, peak timing below one frame, the 23 pairs of Fig. 3d, how the plateau duration was measured, and when the Fig. 1 pulses were given.

**Questions to a reader:** none.

### 3. Where the protocol was unclear

1. **Paper version.** The dataset matches a later version of the paper than the claims file. The protocol says nothing about this; I tested the claims as written and recorded it as a `paper_inconsistency` finding, which is not a clean fit for the kind.
2. **Inherited readings.** Spike detection and doublet readings are taken from other claims ("as in fig1d"). Combined with "under every reading" in one claim and "under one reading" in another, the logic is undefined. I ran every combination and applied step 1.6, adopting K = 4 on evidence.
3. **Authors' derived values in the dataset.** Deposited spike times, delays and amplitudes are not covered by the protocol. I used them as variants, or as the only data where nothing else exists (Fig. 2).
4. **A reading with no units.** When one reading of a criterion selects nothing (distal dendrites in Fig. 4i-k), the protocol gives no rule. I tested on the remaining reading and said so.
5. **Dependent blocks.** For claims blocked because few units pass the claim's own rule, I gave dependent claims `other` as the "same reason".
6. **No finding kind for duplicates.** Duplicate deposits went under `other`.
7. **`measured` when nothing matches.** The protocol only says what to record when several readings match. I recorded the first reading the criterion lists.
8. **`assumed` and data labels.** It is defined for method choices only. I did not set it for a data-label assumption (column 1 as soma in figs12) and stated that assumption in the deviations.
9. **Clock check without a stimulus table.** The check could not be done for Fig. 1; I said so.
10. **Which cells to tag.** "The cells that show the result" is vague. I tagged every code cell in each claim section.
11. **Harness name.** The prompt says "Claude Code" and the example record says "Claude Code (GitHub Actions)"; I used the prompt's.

### 4. Runtime and failures

- The run took about 32 minutes (12:34 to 13:06 UTC); the notebook runs in 47 s in the clean environment.
- One shell `cd` mistake briefly produced stale output; I re-ran the notebook and confirmed the executed copy matches the conclusions number for number.
- Nothing failed in the final runs.

Files are in `entries/001791-wong-campos-2023/` (the notebook and `dendvolt.py` helper), with the record at `attempts/001791-wong-campos-2023-01.yaml`.
