# Amjad et al. (2025) from dandiset 002013

Tests the findings of [Amjad et al. (2025)](https://doi.org/10.1021/acschemneuro.5c00071) that can be
tested on [DANDI:002013](https://dandiarchive.org/dandiset/002013/0.261012.0921), which holds the three
example sessions of the paper: FSCV from site c8dg and LFP from c3bs-c3a in monkey T, and spikes in
monkey P.

| Claim | Outcome |
|---|---|
| Insertion yields of 21.4% and 33% | Blocked: data missing |
| Recordings 483, 496 and 390 days after implantation | Blocked: metadata insufficient |
| FSCV waveform from -0.4 to 1.3 V at 400 V/s and 10 Hz | Partially reproduced |
| EPhys at 30 and 32 kHz, filtered 0.1 to 7500 Hz | Reproduced |
| Shape task: 25% forced trials, blocks of 50 to 300 trials | Reproduced |
| The dandiset agrees with the paper's Zenodo files (outside data) | Reproduced |
| Dopamine from two channels, c8dg and c8ds (Figure 3A) | Blocked: data missing |
| Dopamine redox current after the value cue (Figure 3A) | Blocked: metadata insufficient |
| Beta bursts change around the cue (Figure 3B) | Reproduced |
| More dopamine after large-reward cues (Figure 4A) | Reproduced |
| More beta suppression after large-reward cues (Figure 4B) | Reproduced |
| More beta suppression for contralateral cues (Figure 4C) | Reproduced |
| Firing differs with reward size (Figure 5A) | Blocked: data missing |
| A well-isolated sorted unit (Figure 5B, C) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The trials tables carry no conditions; they are decoded from the event codes. The raw FSCV could not be
linked to the trials, the raw ephys of 09/26/2024 is 9831 s off the trial clock, and monkey P's spike times
are 6800.666 s off its raw signal; the attempt record lists these and the other findings. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/002013-amjad-2025-01.yaml`](../../attempts/002013-amjad-2025-01.yaml).

- `reproduce_amjad_2025.ipynb`: the analysis. It takes a few minutes, most of it streaming the raw ephys.
- `microprobes.py`: loading the files, decoding the trial conditions, and the dopamine, beta-power and spike
  measures. Other notebooks on this dandiset can import it.
