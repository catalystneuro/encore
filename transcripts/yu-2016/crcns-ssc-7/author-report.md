I finished steps 1 to 6 of the Author section. The entry `entries/crcns-ssc-7-yu-2016/` passes `tools/entry.py all`: the check reports 0 errors and the notebook runs in 583 s. The record is `attempts/crcns-ssc-7-yu-2016-01.yaml`, and the handover is built in `executed/crcns-ssc-7-yu-2016/handover/`. Nothing is committed.

**1. Outcomes (48 claims: 24 reproduced, 14 partially reproduced, 5 not reproduced, 5 blocked)**

| Outcome | Claims |
|---|---|
| Reproduced | vpm-whisking-count, vpm-whisking-rate, vpm-phase-modulation, vpm-rate-amplitude-trials, l4e-example-e1, l4e-resting-vm, l4e-whisking-vm, l4e-hf-fluctuations, fs-baseline-rate, fs-touch-vm, fs-whisking-count, fs-whisking-rate, fs-hf-fluctuations, thalamus-inhibition-dose, ion-cut-behavior, ion-cut-l4e-whisking, ion-cut-l4e-phase, ion-cut-l4e-spectra, ion-cut-fs-touch, ion-cut-fs-whisking, ion-cut-fs-phase, enphr-kruskal-wallis, enphr-whisking-driven, enphr-auc |
| Partially reproduced | behavior-performance*, vpm-baseline-rate, vpm-touch-response, l4e-example-e24-e32, l4e-touch-psp, l4e-distance-threshold, l4e-reversal-potential, fs-touch-spikes*, fs-whisking-vm, fs-phase-coupling, thalamus-inhibition-l4e-vm*, thalamus-inhibition-fs, enphr-l4e-rates, enphr-pv-latency |
| Not reproduced | l4e-spikes-touch-selective, ion-cut-l4e-touch, enphr-spikes-per-touch, enphr-auc-groups, enphr-behavior |
| Blocked (`data_missing`) | l4e-inhibition-window, l4e-whisking-inhibition, thalamus-inhibition-vpm, rabies-vpm-input, ion-cut-l5-fs |

\* marked `assumed: true`

**2. The dataset, assumptions and questions**
- **Pinned version:** `unversioned`, since CRCNS has no versions. The notebook header gives the MD5 of `data.tar.gz` and why `live/` was used.
- **Layout:** one 6.2 GB `data.tar.gz` holding 148 NWB 1.0 files in 7 folders. The counts match Supplementary Table 2, and no recording is deposited twice.
- **Findings recorded:**
  - The cortical whisker timestamps mix units: the trial start is in ms, the time within a trial in seconds.
  - Nothing says which of the two tracked whisker series is the principal whisker. Taking them in `whisker_configuration` order leaves FS neurons almost without touch responses (0.45 against 1.78 spikes per touch).
  - JY1139, in the whole-cell FS folder, is described in its file as "Excitatory".
  - 155 flagged stimulus trials have no light in any photostimulus series.
  - Neuron counts differ from the paper's (43 eNpHR neurons against 40, 13 against 12, 9 mice against 8).
  - Missing data: the thalamic multiunit recordings, the rabies tracing, the L5 FS neurons and the depolarized Fig. 3 recordings.
- **Assumptions:**
  - The principal whisker is series 1, as the dataset's example code takes it (`mainwid = 0`).
  - For the light-onset Vm latency I used 1 ms smoothing and a 1 ms hold. The rule as written crosses at the onset sample, where the light makes a step in Vm.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): how the light-onset latency was measured; which tracked series is the principal whisker; and whether the example code's touch-speed cutoff was applied.
- **Questions to a reader:** none.

**3. Where the protocol was unclear, wrong or missing something**
1. The CRCNS section of archives.md assumes zips that can be opened in place. This dataset is a single gzip tar, which can only be read in order. I streamed it once per run (about 8 minutes) and reduced each file in memory.
2. Developing on a subset is costly when every read means streaming from the start. While developing I kept a reduced cache of the arrays in `$TMPDIR`, never in the repo. The entry itself only streams. That cache had a placement bug that, for a while, made the light traces look stored for one trial per file. The first full streamed run exposed it, and I redid those claims; no finding rests on it.
3. Many criteria say "reproduced when…" with no rule for a partial result. I used `partially_reproduced` when some parts held and the effect was present.
4. For ion-cut-l4e-touch, the absence rule forces `not_reproduced`. The criterion's test against zero uses a peak-minus-baseline measure, which is positive even with no response. I showed a comparison with random times as a variant (p = 0.148).
5. Where a fixed latency rule fails on the data (a light artifact, or a sparse PSTH), the protocol gives no guidance. I adopted a stated variant for the Vm latency and reported the PSTH latencies as not found.
6. The protocol asks for runs under ten minutes. Here the streaming alone takes about 8 minutes.

**4. Runtime and failures**
The final notebook run took 583 s with peak memory about 5.3 GB. Three full runs passed. Early on, one development load failed on an `h5py` dataset I had mistaken for a group, and a few fixes followed (scalar spike times, YAML quoting). None is left over.

Untracked dotfiles (`.bashrc`, `.idea` and others) and a `scripts/` directory sit at the repo root. I did not create or touch them.
