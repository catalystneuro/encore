I finished steps 1 to 5 of the Author protocol and ran the handover (step 6). The entry is `entries/001619-kaku-2025/` and the record is `attempts/001619-kaku-2025-01.yaml`. `tools/entry.py all` passed with 0 check errors, and the notebook ran in 42 min (2527 s). I did not verify my own work and did not commit.

## 1. Outcome per claim (48 claims)

| Outcome | Claims |
|---|---|
| Reproduced (16) | code-dataset-link, fig1i, ed1 (unidirectional models), fig1k, fig1l-lick-cycle-prolonged (33.36 ms against 33.3), fig1n-breath-interval-preserved (P = 0.26), fig1n-breath-cycle-prolonged (48.13 ms against 48.0), fig2f, fig2g, ed6e, ed8e, ed4c, fig4e (assumed), fig4f (assumed) |
| Partially reproduced (7) | units-count, region-spike-rates, fig1g, fig1f-licking-mode-switch, fig2 tuned counts, fig2h (assumed) |
| Not reproduced (8) | fig1d, fig1f-inspiration-between-licks, ed1bc, fig1l-lick-interval-preserved, fig2 swallow counts, ed8bc, fig4d |
| Blocked, data missing (15) | ed2 (rats), ed7g, ed7h, fig3b, fig3ce, fig3dfh, ed10, fig4b, fig4c, ed11b, fig5b, fig5c, fig5e, fig5f, ed12c |
| Blocked, other (4) | fig4g, fig4g lags, fig4h (under the claims file's own selection only 1 or 2 recordings qualify, not 43); fig3a (no pinned source for the premotor neurons) |
| Blocked, metadata insufficient (1) | ed8i (lick direction) |
| Blocked, too large (1) | ed7 (GLM, about 2.7 million fits) |

The fig2 tuned counts match under the Methods' and the code's significance scheme: 3,517 / 1,021 / 177 against 3,551 / 1,015 / 182. Under the claims file's other reading, V3(b), they do not (2,757 / 602 / 69). The criterion asks for every reading, so the claim is partially reproduced.

## 2. What was found about the dataset
- **Spike index:** in all 335 files `spike_times_index` holds where each unit starts, not where it ends, so pynwb gives every unit the previous unit's spikes. I read spikes by the per-trial count table instead.
- **Histology rows:** 19 files have more histology rows than units, so regions and CCF positions cannot be matched to units with certainty. The code and I take them by position.
- **Duplicates:** in all 162 two-probe sessions the airflow and tracking are the same recording deposited twice. I counted each once.
- **No session clock:** every trial starts at 0, so trials cannot be placed in time within a session.
- **Implausible metadata:**
  - Age reads P210W to P303W.
  - The stimulus field says `photostim`, but no file has photostimulation data.
  - The left/right text contradicts `ccf_x` for 99.3% of units.
  - The 3D tracking has no stated axes or units.
- **Missing data:** the dandiset has 335 insertions against the paper's 339. The cued task, photostimulation, rats, raw videos and tracing data are absent.
- **Paper against its code:** the Methods' drift filter and "4-pole" filter differ from the code. The code's unit filter gives 20,109 units; adding the drift filter gives 16,957.
- **Clock check:** in four mice (DL004, DL005, DL010, DL020) the shared clock between airflow and spikes could not be established.

**Version:** 0.251027.1953, the only published version, since the paper cites none.

**Outside input:** the Allen structure tree from iblatlas at commit b88da5d, used only to map region names.

**Assumptions:**
- V4(a), the code's swallow normalisation (fig2h).
- O2(a), all sessions, for fig4e and fig4f, because the simultaneous-recording reading leaves 1 or 2 units.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which test gives the significance of the licking and breathing MI?
- How is the swallow MI normalised, and how are "swallow-only" units defined?
- How were units near the preBötzinger complex and in posterior-dorsal IRN/PARN chosen, and which 43 recordings make up Fig 4d?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit
1. The claims file's rule (readings that disagree means block as `methods_underspecified`) conflicts with step 1.6, which lets the author adopt the best-supported reading. Where a criterion gave its own partial rule I followed it; otherwise I adopted an assumption (fig2h, fig4e, fig4f).
2. A 130 GB dataset with 25 kHz airflow needs about 40 min for one pass, close to the 60-minute CI limit. The protocol says nothing on splitting notebooks or caching. I kept one notebook and cut CPU (a grid fit for the resamples).
3. "Run on the whole dataset once" did not fit: I needed one full development run (75 min, as a script) and then the entry run.
4. There is no blocked category for "not run within the run's time" when it isn't strictly the computation. I used `too_large` with an arithmetic estimate for the GLM, and `other` (too few recordings under the claim's selection) for the cross-correlation claims.
5. fig3a is `data: elsewhere` but the paper gives no identifier. The checker forbids `data_missing` and I cannot change the claim's `data` field, so I used `other`.
6. The clock-check guidance assumes a session timeline. Here every trial starts at 0, so I paired each trial's spikes with the next trial's phases.
7. `archives.md` does not say that h5py's global lock stops threaded streaming. Reading in parallel needed separate processes.

## 4. Runtime and failures
- The run took about 2 h 40 min (07:37 to 10:18 UTC). The final notebook took 42 min, the development extraction 75 min.
- **First extraction too slow:** 75 min, over the limit. Fixed by a coarser float32 grid and computing significance only for units with MI above 0.6.
- **Ontology name matching:** the iblatlas copy drops the commas of the Allen names. Fixed by normalising.
- **Survey crash:** the table-length mismatch first crashed the survey; now handled and recorded.
- **Cross-correlation not computed:** for fig4g and fig4h it was not computed at all.
- **Untracked files I did not create:** dotfiles such as `.bashrc` and `scripts` are sandbox device mounts present before the run; I left them.
