I've finished the repeat attempt as `attempts/000005-yu-2016-02.yaml` and built the handover; nothing is committed. The notebook ran from a clean environment in 281 s, and its outputs match the conclusions. One thing is not clean: `python tools/entry.py check` still reports 25 errors, all on the earlier record `000005-yu-2016-01.yaml` (see section 4). The new record passes. I pinned the same version, 0.220126.1853: it is the only published version, and the draft has the same 148 assets.

### 1. Outcome per claim (earlier outcome in brackets)
| Claim | Outcome |
|---|---|
| behavior-touches | partially reproduced |
| vpm-touch | not reproduced [reproduced] |
| vpm-whisking | partially reproduced [reproduced] |
| vpm-whisking-phase | reproduced |
| exc-vm-touch-whisking | partially reproduced |
| exc-threshold-touch-vs-whisking | partially reproduced |
| exc-effective-reversal | reproduced |
| exc-inhibition-timing, exc-inhibition-whisking | blocked, data missing |
| fs-touch-response | partially reproduced |
| fs-vm-touch-whisking | not reproduced |
| fs-whisking-rate | partially reproduced |
| fs-whisking-phase | reproduced |
| fs-touch-and-whisking | reproduced [reproduced] |
| exc-mainly-touch | not reproduced [not reproduced] |
| vpm-photoinhibition | blocked, data missing |
| exc-thalamus-photoinhibition | partially reproduced |
| thalamus-drives-fs | blocked, other: only 5 FS cells qualify [reproduced] |
| rabies-vpm-input | blocked, data missing |
| six ION-cut claims plus sensory-input-drives-fs | blocked, metadata insufficient [sensory-input-drives-fs was also blocked, metadata insufficient] |
| pv-enphr-suppression | partially reproduced |
| fs-suppress-movement-spiking | partially reproduced [reproduced] |
| fs-enhance-touch-selectivity | partially reproduced [not reproduced] |
| exc-touch-spikes-enphr | not reproduced |
| auc-weak-strong | reproduced |
| auc-groups | blocked, methods underspecified (its two named readings disagree) |
| behavior-false-alarms | blocked, methods underspecified (with or without the continuity correction) |

Where a kept id changed outcome, the record says why. In short, the new criteria test the paper's own numbers and the claims file's cell rules. Two examples: the file names one principal whisker per VPM session, which lowers VPM spikes per touch, and the waveform boundary leaves only 5 FS cells for the thalamic test. A two-sided test cannot reach p < 0.05 with 5 cells.

I added 7 questions to `questions/000005.yaml`. They cover:
- the time resolution of dVm/dt;
- the latency bin position;
- the light-driven test and the waveform measures;
- the chi-squared correction;
- one- or two-sided tests;
- whether light trials count in the behaviour numbers;
- the whisking-onset and touch-exclusion windows.

### 2. Earlier findings
All 11 are still present, which follows from the dandiset being unchanged: same version and same assets.
- Cell type: not named in any file.
- ION-cut mice: not marked.
- Genotypes: missing or given as Ai32.
- Layer: every file says layer 4.
- Light: conditions undescribed, power NaN in all 130 files.
- Recording mode: wrong in 24 session descriptions.
- `first_touch_time`: still divided by 1000 in the L4 files.
- Sampling rate: given only by the timestamps.
- Principal whisker: missing in 8 files, one per VPM file. Now shown per unit: 11 of 20 units respond most to another whisker.
- Wavelengths: still look wrong.
- Analysis code: none linked.

### 3. New findings
- The injected current is stored in nA, but its conversion factor assumes µA, so it is off by 1,000. The stored test pulse reads −0.1, which matches the Methods' −0.1 nA.
- Data the paper reports are absent: the depolarized excitatory recordings of Fig. 3, the 17 thalamic multiunits of Fig. 6b,c, and the rabies histology.
- The VPM-site light trains run at 50 Hz in 12 of 33 files; the Methods say 100 Hz.
- The no-lick trial type is spelled both `Nogo` and `NoGo`, and its column has no description.

### 4. Where the protocol does not fit a repeat attempt
- **Check fails on the earlier record.** `entry.py check` requires every attempt of the entry to have an outcome for every claim. That includes the deprecated `-01` record, which predates the rewritten claims file and must stay as it is. So `entry.py all` cannot pass; I ran `check` and `run` separately.
- **No status field for earlier findings.** The findings schema has nowhere to say whether an earlier finding is fixed, so I put "Still present from 000005-yu-2016-01" or "New" in each statement. The `-01` record also cannot get a `superseded_by` without being edited.
- **Repeat-attempt section assumes a changed dandiset.** It describes a new version and a kept claims file. Here neither holds: the version is the same and the claims file was rewritten. Comparing outcomes for kept ids therefore compares different tests, and "is each finding fixed" can only come out as still present.
