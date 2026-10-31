# Gao, Ramachandran, Yu & He (2025) on dandiset 000637

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) on
[DANDI:000637](https://dandiarchive.org/dandiset/000637/0.250829.1249), which holds spike times of
sorted units from one 32-channel probe in S1 of 25 rats, under tFUS at PRFs of 30 to 4500 Hz and pulse
durations of 100 to 600 us, with trial start and stop times.

| Claims | Outcome |
|---|---|
| All 30 claims (unit counts, Figures 4 to 11) | Blocked: data missing |

Every claim is about units classified as RSUs or FSUs from their waveforms, and the dandiset has spike
times only. Most claims also need POm or auditory cortex units, sham or CG1-targeted recordings, or duty
cycles that are not in it. The paper's data statement names another dandiset, 000946, whose rats are not
those of 000637, and 000637 has about 3.6 times as many S1 units over the paper's 2,000 spike threshold
as the paper reports for S1, so its recordings could not be linked to those the paper analysed.

The notebook checks the description against the data (trial counts, the condition codes in the file
identifiers, the trial clock, units deposited twice), counts units under the paper's spike threshold,
and shows the responses of all S1 units pooled across cell types, as a description of the data that
decides no claim. The attempt record is
[`attempts/000637-gao-2025-01.yaml`](../../attempts/000637-gao-2025-01.yaml).

- `reproduce_gao_2025.ipynb`: the analysis, about six minutes, most of it streaming the 292 files.
- `tfus.py`: loading, the condition codes in the identifiers, and the window counts and normalized
  rates of the claims file's Method S. Other notebooks on this dandiset can import it.
