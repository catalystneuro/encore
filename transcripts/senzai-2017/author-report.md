I finished steps 1 to 6 for `senzai-2017` on DANDI:000003 version 0.261122.2143. The entry is at `entries/senzai-2017`, the record is `attempts/senzai-2017-02.yaml`, and `lock`, `check`, `all` and `handover` all passed with 0 errors.

I did not see any earlier attempt's entry, record or transcript. However, the claims file's own opening comments describe an earlier author's analysis and print a few of its numbers: DS2 amplitudes of -83 and +150 uV in one file, mc-deeper P = 5.7e-09, and a classification agreement of 0.944 with a log ratio. I read these before my analysis, so the reconcile step should know this attempt saw them.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| unit-counts | reproduced (583 GC, 503 MC) |
| first-stage-labels | partially reproduced (89.9% of narrow interneurons below 0.425 ms, just under 90%) |
| interneuron-rates | reproduced (7.65 and 2.05 Hz, P = 1e-13) |
| gc-narrower-waveform | reproduced (0.710 vs 0.740 ms) |
| optotag-drd2 | partially reproduced (68 of 106 MC suppressed, against the paper's 29) |
| mc-more-active | reproduced |
| gc-nrem-highest | partially reproduced (wake and REM differ) |
| ca3-wake-highest | not reproduced (NREM 0.473 Hz is above wake 0.450 Hz) |
| nrem-wake-ratio | reproduced |
| theta-modulation, gamma-modulation | reproduced |
| gamma-rate-correlation | not reproduced (MC r = -0.119, P = 0.008) |
| ds2-recruitment | reproduced |
| monosyn-gc-to-mc | partially reproduced (63 GC→MC and 8 MC→GC pairs) |
| burst-facilitation | reproduced (P = 3e-9) |
| state-transmission | not reproduced (P = 0.52; P = 0.018 on the authors' 32 pairs) |
| zero-lag-synchrony | partially reproduced |
| tmaze-central-active | partially reproduced (holds for MC only) |
| tmaze-multiple-fields | partially reproduced (rests on an assumption) |
| tmaze-peak-info, tmaze-splitters | reproduced |
| remap-positive | reproduced |
| remap-gc-lt-mc | not reproduced (KW P = 0.69) |
| remap-fractions | partially reproduced |
| pv-remap | reproduced, seed sensitive (at 20 cells the GC and MC medians are 0.003 apart) |
| inheritance-tmaze | reproduced (rests on an assumption) |
| inheritance-openfield | reproduced |
| mc-deeper | reproduced |
| gc-mc-classification | reproduced (94.9% agreement under all five seeds) |
| gc-mc-distance, gc-backpropagation | blocked: metadata insufficient |

### 2. Dataset, assumptions, questions
- **Agrees with the paper:**
  - The labels match the paper's counts closely, including 248 dentate narrow-waveform interneurons and 106 MC, 198 GC in the DRD2 mice.
  - The authors' monosynaptic table holds exactly the paper's 32 GC→MC pairs, 18 of them in T-maze files as in Figure 7A.
  - The zero-lag table gives 22.1% of MC with a partner (paper 23%).
  - The open-field files hold 246, 182 and 317 units (paper 247, 181, 317).
- **Checks that passed:**
  - The seven same-day "b" files are separate recordings, not duplicates.
  - The stored-waveform site and the wide-band site agree for 89% of GC and MC.
  - Spikes share the clock of the DS2 events (80 of 81 files), of the positions, and of the light pulses. The DS2 clock could not be shown for YutaMouse44-151130, which has few GC and MC.
- **Problems found:**
  - **No site coordinates (major):** the electrodes table gives no recording-site positions, which blocks the two depth claims.
  - **`arm_start` (minor):** it is described as entry into the central arm, but it falls 27.3 cm into the 65 cm arm.
  - **Truncated waveforms (minor):** the stored 1.6 ms waveforms end before the peak for 44% of GC and 69% of MC. With wide-band waveforms the GC/MC latency difference is not significant (P = 0.43).
  - **Missing tables (minor):** 13 files have no monosynaptic table, and they don't say whether that means no pairs.
- **Assumptions:**
  - T-maze fields are found from the highest local maximum down.
  - Each run starts at the mouse's last entry into the central arm before `arm_start`.
- **Questions for the paper's authors**, recorded as `methods_unavailable` findings:
  - How local maxima were found for the T-maze fields.
  - Which significance test was used for optogenetic suppression.
  - What the manual inspection of the cross-correlogram pairs excluded.
  - Where the gate opening falls relative to the files' trial times.
- **Questions to a reader:** none.

### 3. Protocol points
1. The claims file's opening comments describe an earlier author's runs and numbers, so a blind repeat attempt still sees them. I read them and report it here.
2. Two claims (gc-mc-distance, gc-backpropagation) have no criterion. I blocked both for missing metadata, and they would not be testable anyway.
3. The step 3 rule that "every sentence must be backed by a printed number" applies to the notebook; the protocol does not say whether it also covers the record's notes. I held the notes to it and removed two sentences that were not backed.
4. Changing any wording in the notebook forces a full 20-minute re-run. I ran the whole entry three times for text-only fixes.
5. The harness left a protected empty `.claude/.cc-writes` folder inside `entries/senzai-2017` that I could not delete. The workflow should not commit it.

### 4. Runtime and failures
The notebook runs in about 21 minutes (1239 s) and the three runs gave identical outputs. The first full pass over the files failed on about 40 of them, because some tables are optional and some T-maze series use timestamps; I fixed the helper and the pass then completed. Nothing failed after that, and no claim was blocked for time. I finished at about 01:07 UTC.
