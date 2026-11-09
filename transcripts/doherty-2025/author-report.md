I did steps 1 to 6 of the Author section. The entry runs from a clean environment in 320 s, `entry.py check` reports 0 errors, and the handover is in `executed/001444-doherty-2025/handover/`. Nothing is committed. I pinned version 0.250805.2002: the paper cites no version, it is the only published one, and the draft has the same 17 assets and blobs. Run time was about 40 minutes (16:58 to 17:37 UTC).

## 1. Outcomes (40 claims)

| Outcome | Claims |
|---|---|
| Reproduced (10) | fig2-control-rest-beta (19 Hz), fig2-control-activated-gamma (44 Hz), fig5-pd-rest-beta (15 Hz), fig2c-control-pt5b-rate-activated, fig5c-pd-pt5b-rate-activated, rest-pt5b-rate-pd-vs-control, control-cv-isi, pd-cv-isi, pd-activated-vm-more-negative, activated-20-35hz-power-pd-vs-control |
| Partially reproduced (2) | activated-pt5b-rate-pd-vs-control (Mann-Whitney p = 0.0052, the criterion needs < 0.001); rest-beta-power-order-of-magnitude (ratio 65 to 129, above the criterion's 3.16 to 31.6) |
| Not reproduced (23) | the IT rate claims (fig2c-control-it23, fig2c-control-it6, control-it5-silenced, control-it4, fig5c-pd-it23, pd-it5-silenced, pd-it6-unchanged, rest-it4, rest-it5a, activated-it6); fig1-network-size; fig5-pd-activated-gamma (27 Hz); control-duty-cycle and pd-duty-cycle; fig3a, fig3b, fig6a, fig6b; control-coincident-spikes and pd-coincident-spikes; fig4 and fig7 unitary events; rest-synchrony-increase |
| Blocked (5) | model-pt5b-excitability-decrease (data_missing); robustness-four-sets, pt5b-highest-rate, control-subthreshold-oscillations, pd-no-subthreshold-oscillations (methods_underspecified) |

## 2. Dataset, assumptions and questions

**Findings about the dataset:**
- **Only cells that fired are stored.** The units tables hold 2,917 to 4,480 of the 10,073 M1 cells per file, not all of them as the description says. I took population sizes from the gid blocks in the unit names.
- **Fewer potentials in the paper's set.** Its files hold 20 PT5B membrane potentials each, not 400.
- **Those potentials don't match the stored spikes.** They agree with the same cells' spikes for the first 0.5 s, but only 1.5 to 5.6% from 2 s on. In set 04-22-2024 they match throughout, so the paper's-set traces seem to come from a run that diverged from the stored one.
- **Duplicate file.** `sub-001.nwb` is the same blob as `sub-001_ses-sM1-04-22-2024-01.nwb`.
- **One LFP trace, position unknown.** Each file has a single LFP trace with no electrode position, where the model records 11.
- **Metadata.** The files link the preprint, not the paper; the dandiset lists no related resource; the archive summary gives "spike sorting" as the technique.
- **Other numbers in the paper's set.** PT5B rates and CVs match the paper to the printed decimal. Coincidence and unitary-event measures over all PT5B cells saturate: 17 to 42 spikes per ms give about 100% coincident spikes and no significant window.

**Assumptions:** no outcome is marked `assumed`. Choices recorded as deviations:
- "LFP 0" is taken as electrode 0 (reading E1). E2, the mean over 11 electrodes, cannot be computed.
- The short-time Fourier reading (S2) uses a 250 ms window, because NetPyNE's default FFT has a 156 Hz frequency step.
- I classed rest-beta-power-order-of-magnitude as partially reproduced, because its criterion gives no outcome for a ratio above 31.6.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which cells enter a population's mean rate, and which test gave the rate p-values?
- Which cells and definition gave the coincidence and unitary-event numbers?
- How were LFP bursts defined, and was the spike count histogram smoothed for the duty cycle?
- Does "any neuron population" include interneurons? PV5A fires faster than PT5B.
- How were subthreshold oscillations detected?

**Question to a reader** (`questions/001444.yaml`): every IT value matches the paper to the printed decimal under a third reading, R3. R3 averages over the cells the file holds (those that fired at any time in the run) with rates over the last 2.3 s. For example, IT2 at control rest gives 1.203 ± 1.649 against the paper's 1.2 ± 1.6. The claims file lists only R1 (all cells) and R2 (cells active in the last 2.3 s). I tested on R1 and R2 as written and showed R3 as a variant. Ten not-reproduced claims and pt5b-highest-rate would be decided again under R3; rest-it4 would still fail its tests.

## 3. Protocol gaps

1. **Readings found after the analysis.** The protocol does not say what to do when the data show a reading the claims file missed that matches the paper exactly. I asked a reader, kept the outcomes on the file's readings, and showed R3 as a variant.
2. **Gaps in a criterion.** rest-beta-power gives outcomes only for ratios in 3.16 to 31.6 or below 3.16, and nothing above. I chose partially reproduced and recorded the reason.
3. **Readings that can't be computed.** Readings the dataset cannot support (E2 needs 11 electrodes) have no rule. I ran the readings that could be run and recorded a deviation.
4. **Results that show the method differs.** When a result shows the paper's procedure must differ (100% coincident against 1%), the protocol only says `methods_underspecified` for chance levels. I recorded not reproduced, with the reason and a question for the authors.
5. **Format files.** To learn the questions-file format I opened `questions/000005.yaml`, from another dataset. It is not an attempt record, but it falls outside the files the prompt pointed me to.

## 4. Runtime and failures

The notebook takes about 5.5 minutes, nearly all of it streaming the files. Nothing failed. Untracked dotfiles (`.bashrc`, `.idea`, `scripts`, and others) appeared at the repository root during the run. They are not mine and I left them alone.
