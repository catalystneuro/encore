## Report on DANDI:001750 (Liu et al. 2026), author run

I tested 8 of the 34 claims; the other 26 are blocked. `entry.py check` and `all` pass with 0 errors, the notebook runs in 164 s in a clean environment, and the handover package is built. Verification is still to come, and nothing is committed.

### 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| na-cell-table-link | with_labels | partially reproduced |
| fig4d-sodium-current-lower | dataset | blocked: methods_underspecified |
| model-na-ratio | dataset | blocked: methods_underspecified (depends on fig4d) |
| na-patch-capacitance | dataset | blocked: data_missing |
| fig8a-metabolite-gradient | elsewhere (MetaboLights) | not reproduced (175 and 84, against 228 and 108) |
| fig8de-glycolytic-bias | elsewhere (MetaboLights) | partially reproduced |
| fig4j-eepsp-amplitude | elsewhere (repository table) | reproduced |
| fig3c-ais-distance-length | elsewhere (repository table) | blocked: metadata_insufficient |
| Model claims (5) | elsewhere | blocked: not_runnable |
| scRNA-seq and Patch-seq mapping claims (7) | elsewhere | blocked: too_large |
| DANDI:001746 claims (5) | elsewhere | blocked: too_large |
| DANDI:001751/001752, NeuroMorpho, eEPSP latency (9) | elsewhere | blocked: other |

- **Fig. 4d:** VENs have the lower median under all 8 readings in the claims file. The difference is significant under only two of them, the ones that subtract no baseline (p = 0.045 and 0.025); the other six give p = 0.077 to 0.29. The criterion says to block when readings disagree, so I blocked it.
- **Link claim:** at most 2 of 35 computed maxima are within 10% of the paper's code table, where 28 are needed. A variant I added after looking at the data, a 0.75 ms moving average before taking the peak, gets 26 of 35 within 10% (Spearman 0.98) and gives VEN lower at p = 0.0008. It decides nothing.

### 2. Dataset, assumptions and questions

**Version:** 0.260825.0222, the only published version. The paper cites none.

**What the dataset holds:**
- 35 files from one macaque, two sessions, 100 kHz, 25 ms steps.
- No cell type: VENs and PCs can only be told apart through the code table. File names and cell IDs match that table for all 35 patches.
- No capacitance or compensation values.
- Holding currents of -131 to +92 pA remain in the traces, although the Methods say leak was subtracted online. One file (cell HS018) is very noisy.
- Steps go to +55 or +85 mV, where the Methods describe -80 to 0 mV.
- Every file gives the placeholder start time 2018-01-01, while the session IDs date the recordings to 6 December 2022.
- No duplicate recordings.

**Outside data:**
- The MetaboLights table has 558 metabolites, where the paper reports 581.
- The repository's AIS table has 500 PC and 120 VEN values, where the legend gives 430 and 108, and it has no slice or animal column for the two-way ANOVA.
- The eEPSP table labels its stimulation values 0.5, 1 and 2 mA, where the Methods give 0.05 to 0.2 mA, and gives no unit for the amplitudes.

**Assumptions:** none marked `assumed`. Method details I took myself are recorded as deviations: in the metabolomics, raw values with log2 as a variant, and "followed by" read as gated by Welch's ANOVA with the ungated test shown; in the eEPSP table, stimulation levels taken by their order within each pair.

**Question for the paper's authors** (recorded as a `methods_unavailable` finding): how was the maximal Na⁺ current measured, meaning which baseline, filter or fit, steps and window?

**Questions to a reader:** none.

### 3. Protocol points

1. **Claims whose criterion hands the test to another dandiset's claims file** (001751, 001752). The protocol has no block reason for this. I used `other` and said so in the notes.
2. **Claims not attempted for lack of time, where the time limit and not the computation stopped them.** The protocol gives no reason category. I used `too_large` only where I could estimate from my own streaming rate (DANDI:001746, about 14.7 GB, over an hour just to stream). Elsewhere I used `other`, stating that the claim was not attempted.
3. **A criterion that blocks when readings disagree**, against step 1.6, which allows adopting the best-supported reading as an assumption. I followed the criterion, as it decides.
4. **A dependent claim (model-na-ratio) is blocked automatically**, but I still showed its numbers in the notebook. The protocol doesn't say whether to.
5. **Variants found after looking at the data** (the smoothing). The protocol doesn't say how to label them. I said in the notebook, the helper and the record that the variant was found post hoc and decides nothing.

### 4. Runtime and failures

- About 2 h 25 min, from 13:18 to about 15:43 UTC.
- One `grep -o` with long context patterns on the paper's text hung for the full 60-minute tool timeout. That cost about an hour, during which some of the 26 blocked claims could have been tested.
- One YAML quoting error in the record, fixed.
- Untracked dotfiles (`.bashrc`, `.mcp.json`, `scripts/` and others) are in the repository root; I did not create them and left them alone.

Files are in `entries/001750-liu-2026/`:
- `reproduce_liu_2026.ipynb`
- `nacurrent.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/001750-liu-2026-01.yaml`.
