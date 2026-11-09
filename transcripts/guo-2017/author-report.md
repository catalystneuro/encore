I did steps 1 to 5 of the Author section and ran the handover (step 6). `tools/entry.py check` reports 0 errors, and the notebook runs from a clean environment in 330 s. Executed outputs match my development run line for line, and every conclusion sentence was checked against them. I pinned version 0.220126.1903: the paper cites no DANDI version, and this is the only published one (the draft has the same 173 assets).

## 1. Outcomes (39 claims: 4 reproduced, 11 partially reproduced, 3 not reproduced, 21 blocked)

| Claim | Outcome |
|---|---|
| fig1c-alm-photoinhibition-bias, fig2e-alm-contra-ipsi-balance, vgat-thalamus-reduction, fig3-onset-latencies | reproduced |
| task-performance, alm-unit-classes, fig2e-alm-selectivity, thalamus-unit-classes, fig2f-vmval-selectivity, fig3-alm-collapse, fig3f-thalamus-silenced, fig6c-unmodulated-less-selective, fig6d-localized, snr-photoinhibition, selectivity-time-course | partially reproduced |
| wc-near-threshold, fig6c-vmval-reduced, fig6e-onset-latencies | not reproduced |
| wc-thalamus-hyperpolarization, wc-m1-small-effect, wc-contra-alm-small-effect, thalamus-stronger-than-cortex, vm1-photoinhibition-no-effect, gad2-thalamus-reduction | blocked: metadata insufficient |
| fig3d-all-layers, fig3b-…, fig6b-… (the criteria's own rule when readings disagree), latency-model-t3, network-models | blocked: methods underspecified |
| fig1d, muscimol, wc-loss-of-excitation, indirect-pathway, conduction-delay, fig5 (both), snr-unit-properties, anatomy, alm-gabaergic | blocked: data missing |

## 2. What was found about the dataset
- **Partial deposit.** It holds 966 of 1214 ALM units and 789 of 790 thalamic units. In SNr it holds 181 of 227 units, apparently only the putative GABAergic ones. Fig. 5, behaviour-only, muscimol, non-behaving and M1 whole-cell recordings, and the anatomy are absent.
- **Mean waveforms are cut short.** Widths above about 0.5 ms cannot be measured, so the Methods' width classes cannot be recovered. The `cell_type` labels have no stated rule but match the paper's class sizes.
- **Spikes are stored only to about 5 s after pole onset**, though trials last about 9 s.
- **Most units span only part of their session** (median 70% of trials), and there are no per-unit observation intervals. Once each unit was restricted to its span, ALM selectivity came out at 70.5% against the paper's 70%.
- **Whole-cell files record no photostimulus time.** The effect starts about 0.19 s after the onset the claims' convention implies; this is what blocks the four whole-cell Vm claims.
- **Metadata errors:**
  - one whole-cell trial table (cell_21_1) has start and stop times shifted by one row;
  - the Vm `conversion` (0.001, unit mV) contradicts values already in mV;
  - every electrode group carries the ALM coordinates;
  - the SNr units of one mouse sit at AP −1.56 mm, outside SNr;
  - the Gad2 sessions have genotype `Ai35D x GAD2_Cre` and no photostimulus trials;
  - the VGAT thalamic sessions give 2.23 mW where the paper gives 10 mW;
  - the galvo site at (0.5, 0.5) mm is unnamed;
  - PV-Cre x Ai32 sessions with thalamic photostimulation are not described in the paper.

**Questions asked** (6, in `questions/000009.yaml`):
1. Unit classes: computed width or the files' label.
2. Whether the PV-Cre x Ai32 sessions with thalamic photostimulation belong in Fig. 3.
3. Whether the 0.75/0.79 mW ALM trials count as photoinhibition.
4. Where the photostimulus starts in the whole-cell files.
5. Whether the (0.5, 0.5) site is vM1, and which ALM power to compare it with.
6. Control-only or all correct trials for the selectivity time course.

## 3. Where the protocol was unclear, wrong or missing something
1. **A claims-file convention the data contradict** (the whole-cell photostimulus onset). The protocol says "trust the data" but gives no outcome rule. I ran both onsets the text supports and blocked the four claims as metadata insufficient.
2. **Readings multiply.** My question-driven unit readings (P1/P2) multiply with each criterion's readings, and the protocol does not say how they combine. I applied "under one reading" across all combinations.
3. **Counts short only because the dataset holds fewer units.** Criteria without a partial clause do not say what this is. I chose partially reproduced when the fractions or effects matched.
4. **No rule for missing per-unit observation intervals.** I used each unit's first-to-last-spike trials as a standard choice and recorded it as a deviation.
5. **`measured` when no reading matches.** The protocol only covers the case where several match. I recorded the first reading.
6. **Criteria that block on trivial disagreement.** For fig3d the failing bins are 0-against-0 ties of 1 to 4 neurons; I followed the criterion and blocked.
7. **Data-interpretation questions.** Which site is vM1 and where the laser starts can't be answered from the paper. I asked them anyway, as step 1.6 says.
8. **A claim testable only in part** (snr-unit-properties: the selectivity count is testable, the rates are not). I blocked it as data missing and put the selectivity count in the notes.

## 4. Runtime and failures
- The notebook takes 330 s (about 5.8 min for the full `all` run). Most of it is streaming 12.7 GB of whole-cell data.
- Development errors (read-only arrays, empty unit sets) were fixed; the final runs had no failures.
- Untracked dotfiles in the repository root (.bashrc, .idea and others) and an empty `.claude/.cc-writes` folder inside the entry came from the environment, not from me; I left them alone. Nothing was committed.
