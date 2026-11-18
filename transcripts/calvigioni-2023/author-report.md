I've finished steps 1 to 5 of the Author protocol and built the handover (step 6). The entry is in `entries/000473-calvigioni-2023/` and the record in `attempts/000473-calvigioni-2023-01.yaml`. `entry.py lock`, `check` and `all` all pass, and `handover` built `executed/000473-calvigioni-2023/handover/`. I pinned version 0.230417.1502 because the paper cites it; the later 0.261102.1657 has the same 25 files and only adds metadata.

**1. Outcomes (33 claims)**

| Claim | Outcome |
|---|---|
| code-outputs-link | partially reproduced (assumed: GLM period) |
| ed7a-unit-counts | reproduced (4,159 units, all four genotype counts within tolerance) |
| fig4g-glm-units | reproduced (assumed: GLM period) |
| fig4e-opto-modulation-genotypes | not reproduced (assumed): Npy also has more light-tuned units than controls (14.4% vs 10.0%, p = 0.044) |
| fig4g-opto-tuning-score | not reproduced (assumed): the four means are within tolerance, but Esr1 vs control gives corrected p = 0.11 with only 7 Esr1 mice |
| fig4g-tuned-unit-counts | partially reproduced (assumed): 5 of 8 counts match |
| ed8h-waveform-classes, ed8r-comodulated-units, ed8o-conditioned-units | reproduced |
| ed7bd-latency-similar | reproduced (assumed: baseline window) |
| ed9a-pca-divergent-block2, ed9bg-state-clusters, fig4i-activity-modes, fig4k-decoding-pl, fig4jl-pl-esr1 | reproduced |
| fig4h-opto-clusters | partially reproduced: 2 opto clusters, 100% Vglut2/Esr1 units, but 1,995 units kept against 1,770 |
| ed9no-decoding-other-regions | not reproduced: 49 genotype differences, mostly Esr1 decoding better |
| 3 pupil/eye claims, ed1j optotagging, 11 ex vivo/anatomy/behavior claims | blocked, data missing |
| fig2d-markers (Patch-seq on BioStudies) | blocked, metadata insufficient: cell-type codes 1 to 6 have no names |

**2. What the dataset holds, assumptions, questions**
- The dataset holds only the Neuropixels recordings of Fig. 4 and Extended Data 7 to 9. One file has an eye-area trace; there is no pupil data.
- **Genotype labels:** two sessions the code lists as controls (216300, 216301) are labelled Vglut2-cre in the files.
- **Sex:** 10 of 25 mice are female in the files; the paper says all male.
- **Missing units:** four sessions have no unit in the four subregions, so only 21 mice contribute (7 of 10 Esr1-cre).
- **Stimulus metadata:** the light-power column is 0 and the light trace peaks at 0.9 to 3.3 "mW" against 6 mW in the paper. Blocks 9 to 12 are undocumented. `opto_pulse_ts` has no unit. Three sessions have tone events outside the trial table. The air-puff duration says 20 ms against 50 ms. The stimulation site is LHA in every file.
- **Saturation:** one session's "LFP saturation" period covers all of block 3.
- **Code mismatches:** the code says it fits the GLM over the whole session, but its outputs match a fit over blocks 1 to 4. Its outputs also leave out 61 units that pass its own selection.
- **Assumptions:**
  - GLM period: blocks 1 to 4, because that is what the code's outputs match.
  - Saturation: spikes are removed using the files' "spike saturation" series, as the code does, rather than the "LFP saturation" series the Methods' wording points to.
  - Latency baseline: the window just before each event.
- **Questions for the paper's authors** (recorded as findings): the GLM period and saturation series, and how latency was detected.
- No questions to a reader.

**3. Where the protocol was unclear**
1. The claims file tells me to take genotypes from the code's session table, an outside source. The protocol doesn't say whether that makes those claims `with_inputs`. I kept `data: dataset`, as the claims file has it.
2. The code carries out the Methods' saturation step but on a differently named series. It is unclear whether that is a Methods-vs-code disagreement (Methods first) or an open detail. I treated it as an open detail with two readings, used the code's series and showed the other in the data check.
3. A claim's expected value can fail while its criterion's rule passes (fig4h). The protocol doesn't say how to combine them. I recorded partially reproduced.
4. Two criteria have no "partially reproduced" clause, yet most of the effect holds (fig4e, the tuning score). I followed "the criterion decides" and recorded not reproduced, saying so in the notes.
5. For data held elsewhere, the protocol lists block reasons but not the case where labels are missing there. I used `metadata_insufficient` for fig2d.
6. The protocol forbids writing data to disk in the entry but says nothing about development. While developing I cached streamed data in `$TMPDIR`; the notebook itself streams.

**4. Runtime and failures**
The run took about 1 h 45 min (02:49 to 04:34 UTC); the notebook takes about 12 min. Nothing failed in the final run. The untracked `.bashrc`, `.idea`, `scripts` and similar entries at the repository root are sandbox device files that were there before my run; I left them alone. Nothing is committed.
