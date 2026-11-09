The attempt is recorded and handed over. Both notebooks pass `entry.py all` (11.5 and 18.9 min) and `check` reports 0 errors. Run time was 00:34 to 02:47 UTC, about 2 h 13 min, and nothing failed.

Dandiset 000253 holds none of the paper's recordings, so every claim marked `elsewhere` was tested on the paper's own deposits. Those are DANDI 000021 (0.251116.2246) and 000022 (0.251116.2247), the only published versions of each. 000253 is pinned at 0.240923.1441, its latest published version, because the paper cites no version.

**(1) Outcomes (36 claims, including one link claim I added)**

| Claim | Outcome |
|---|---|
| methods-sessions-passing-qc, methods-probes-ccf (284 of 332), ed1jk-units-per-experiment | reproduced |
| fig1g-receptive-fields (60.8%; hippocampus 1.61%, outside 1.4 ± 0.14) | partially reproduced |
| link-unit-tables (ids and timescales match; latencies do not) | partially reproduced |
| fig3c (r 0.959), fig3f (0.958), fig3i (−0.954, assumed), fig3l (0.804) | reproduced |
| ed9a (27 of 28 pairs), ed9d (26 of 28) | partially reproduced |
| ed9e, ed9h (4 of 28 pairs disagree) | not reproduced (ed9e assumed) |
| fig3-unit-counts (17,167 and 8,381 with the code's windows) | reproduced, assumed |
| ed9fg, ed9bc, ed9ij | reproduced |
| ed10b-layers (3 of 4 parts; MI difference 0.127 against 0.09) | partially reproduced, assumed |
| anatomical-hierarchy-order (order only; bootstrap test not run) | reproduced |
| fig4e, fig4f, ed9k, ed9lmn, fig4h, ed9p (from the paper's metric tables) | reproduced |
| methods-gaze-stability (6.59 ± 2.18°, max 14.29°) | reproduced |
| fig4b-behaviour-performance | blocked: data_missing |
| fig2-sharp-peak-pairs (17,592 of 2,116,259 pairs; 0.94% per mouse), fig2d | reproduced |
| fig2f (r 0.809), ed8 (THS 0.904) | reproduced, assumed |
| ed10ce | reproduced |
| fig2-neighbour (AL-PM also differs), ed7c (9 of 10) | partially reproduced, assumed |
| ed7fg (spontaneous DS still correlates, r 0.54, p 0.012) | not reproduced |
| ed7e | blocked: metadata_insufficient |

**(2) What was found about the dataset**
- **000253 is a different experiment.** It is the OpenScope Global/Local Oddball project, yet its metadata names this paper as `IsSupplementTo`.
- **000021/000022 match the paper's counts** of sessions, genotypes and probes.
- **The left-right CCF coordinate is missing.** In all 58 sessions the electrode `y` and `z` columns are identical, which is why ed7e is blocked.
- **The paper's stimulus metrics are not in the files.** `p_value_rf`, `area_rf` and `mod_idx_dg` are absent, so I recomputed them from the spike times.
- **The behaviour sessions of Figure 4 were never deposited.** Only the paper's metric tables are public.
- **The paper's code and Methods use different windows.** The paper's timescale table matches the code's windows (99%+ of units); its latency table matches neither.
- **Smaller gaps.** The layer codes in `layer_info.csv` are undocumented and are reused for CA1, CA2 and CA3. 000022 has 26 connectivity mice where the paper uses 25, and the one left out is not identified.

**Assumptions:**
- **Figure 3 counts and ed10b** use the code's windows (200 ms latency, 40–290 ms decay), because Figure3.py and ExtDataFigure10.py read tables made with them. With the Methods' windows these fail.
- **CCG claims** use all non-noise units and 2 s windows, the only reading that reproduces the paper's pair count.
- **Modulation index:** the preferred condition is the one with the highest mean spike count.

**Questions for the paper's authors** are recorded as three `methods_unavailable` findings:
- Which latency and decay windows produced Figure 3 and Extended Data Figures 9 and 10?
- Which units and which window went into the CCGs, and how was the spontaneous block cut into trials?
- How is the preferred condition for the modulation index defined?

No questions were put to a reader.

**(3) Where the protocol was unclear, wrong or missing something**
1. **No way to record that the target has none of the data.** I kept `dataset` as 000253, listed 000021/000022 under `inputs`, and put the mismatch in the findings.
2. **Readings for dependent claims.** The protocol does not say whether the reading that reproduces a parent claim also fixes it for the claims that depend on it. For the CCG claims I adopted the parent's reading as a stated assumption and showed every reading.
3. **The claims file sets different main methods for related claims.** It makes the Methods' windows main for fig3c and fig3l, but says "as the code computes" for the counts and ed10b. I ran both and adopted the code for the latter two as assumptions.
4. **Link claims fit loosely here.** I matched the paper's tables to the 000021/000022 units, not the target's, and added `link-unit-tables` to `depends_on` of ed10b and ed10ce. I did not change any claim's statement, expected values or criterion.
5. **Some criteria have no partial rule.** fig1g holds only in part, so I recorded it as partially reproduced.
6. **Conclusions require a second full run.** They must be in the notebook before the final run, which here meant a second 30-minute run. The two notebooks run one after the other (about 30 min in total); each is under the 30-minute limit, but both exceed the 10-minute aim.
7. **The claims file says the code leaves the flashes open, but `get_flash_PSTH.py` uses all flashes.** I recorded this as a deviation citing the script and did not ask a reader.
8. **The repo root has untracked device-node dotfiles.** `.bashrc`, `scripts`, `.idea` and others are sandbox device nodes created before this run; I left them alone.

**(4) Nothing failed.** I did not commit; the new files are `entries/000253-siegle-2021/`, `attempts/000253-siegle-2021-01.yaml` and the edited claims file, and the verifier package is in `executed/000253-siegle-2021/handover/`.
