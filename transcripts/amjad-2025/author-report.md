I tested all 14 claims on DANDI:002013 version 0.261120.1306: 8 reproduced, 1 partially reproduced, 1 not reproduced and 4 blocked. The entry is at `entries/amjad-2025/` and the record at `attempts/amjad-2025-02.yaml`. `python tools/entry.py all` passed with 0 errors, and the handover package is in `executed/amjad-2025/handover/`. I did not verify my own work, and nothing is committed.

**1. Outcomes**

| claim | outcome | key numbers |
|---|---|---|
| insertion-yield | blocked, data_missing | the list of implanted sensors is not in the dataset |
| chronic-duration | blocked, data_missing | no implantation dates anywhere in the files or metadata |
| fscv-waveform | partially reproduced | lowest potential -0.347 V (paper says -0.4 ± 0.04); 1.34 V, 400.5 V/s and 10 Hz are within tolerance |
| ephys-acquisition | reproduced | 30000 Hz and 31999.96 Hz; stored filter 0.1 to 8000 Hz (paper says 7500, still within tolerance) |
| shape-task-structure | reproduced | forced trials 24.39%; 8 complete blocks of 71 to 273 trials |
| zenodo-link (uses Zenodo data) | reproduced | trial lists agree 99.82 to 100%; example beta trace r = 0.94 at a 6 ms lag |
| fig3a-dual-channel | blocked, data_missing | the second channel (c8ds) is not in the dataset or on Zenodo |
| fig3a-redox-peaks | not reproduced | in the raw current, the most negative value on the falling sweep is at 0.897 V, not near -0.2 V; changes are under 0.08 nA |
| fig3b-beta-bursts | reproduced | burst rate 1.51 → 1.21 per s, p = 9.5e-10 (the direction flips with the threshold) |
| fig4a-dopamine-reward | reproduced | large-reward median 1.37 vs small 0.19, p = 0.023 |
| fig4b-beta-reward | reproduced | p = 1e-8 over 0 to 0.5 s; not significant over wider windows |
| fig4c-beta-side | reproduced | left vs right p = 1.6e-6 |
| fig5a-spike-reward | blocked, metadata_insufficient | Monkey P's event codes have no names and there is no trials table |
| fig5bc-unit-isolation | reproduced | 0.0032% of spike intervals under 1 ms; waveform trough 4.58 times the noise |

**2. The dataset**
- **Clocks:** the events, trials tables, bipolar LFP, raw EPhys and raw FSCV share one clock. Raw EPhys and the LFP line up within 0 to 1 ms. The raw FSCV current lines up with the trial-aligned table within 0.1 s, but only when compared across the whole session; single trials are too noisy to show it. Monkey P's spikes sit on its raw signal within 0.1 ms.
- **Missing:** the second dopamine channel (c8ds), the implantation dates, the list of implanted sensors, and a code map and trials table for Monkey P.
- **Mismatches with the paper:** the stored filter high cut is 8000 Hz where the paper and the description say 7500 Hz. The stored FSCV waveform starts at -0.347 V where the paper says -0.4 V; the dataset description agrees with the files.
- **Smaller problems:** Monkey P's site is named cl3 in the electrodes table, ch33 in the unit names and c33 in the paper. The trial-aligned FSCV series have no units and cover only trials 0 to 733 of 1468, without saying so. Monkey P's raw signal sits at the ±1 mV input limit in 2.9 to 10.7% of samples.
- **Raw FSCV:** the raw current, and the stored oxidation current at 0.6 V, show no dopamine signal after large-reward cues, while the stored PCA dopamine of the same trials does. I rated this minor because the data do not show whether it is an error or a small signal.
- **Zenodo deposit:** the example-trial file stores its time axis in the field meant for the LFP trace, so the Figure 3B example trace is not deposited. I recorded this as a finding about the paper.
- **Assumptions:** no outcome rests on one. The details I chose (the 600 s noise segment, the edges of the dopamine window, and reading "all trial windows" as the union of the 60 s windows, which turns out to cover every sample) are standard choices that do not change any outcome.
- **Questions:** none for the paper's authors, and none for a reader.
- **Earlier results:** I did not seek out earlier attempts. However, the claims file's opening comment describes an earlier look at the data: it says the raw 09/26 EPhys and Monkey P's spikes were offset from the trial clock, that events repeated about five times, and that the raw FSCV could not be matched to the trial-aligned traces. I read this before my own analysis. In this version the events are stored once each and the offsets are not present. The finding that the raw FSCV current shows no dopamine contrast at the value cue is the same as that comment reports.

**3. Where the protocol was unclear**
1. Step 1.3 asks to show how versions differ, but this is a blind repeat. I only listed the file sizes of both published versions and did not compare their contents.
2. Link claims are meant to be written by the author, but `zenodo-link` was already in the claims file. I tested it as written.
3. The protocol does not say whether a blocked claim may have a tagged output cell. I added one to fig3a-dual-channel showing the c8dg half, marked as not deciding.
4. The severity scale gives only a ceiling ("at most major") for problems the data cannot settle. I rated the raw-FSCV finding minor and said why.
5. Findings about the paper's own Zenodo deposit fit neither the "data" nor the "paper" category cleanly. I filed it under the paper, since the deposit is not the dataset.
6. `measured` is described as being for claims with expected values, so I left it out of claims that have none.
7. The Zenodo events file for Monkey P was inspected while preparing but is not read in the notebook. Its finding (no code map) is only cited in the notes and decides no number.

**4. Runtime and failures**
The notebook runs in 73 s with a peak of 3.35 GB of memory; my work took about 32 minutes (22:48 to 23:21 UTC). Nothing failed in the final run. During development there were a few script bugs (an array reshape, string quoting, a cast from a missing value), all fixed before the final run.
