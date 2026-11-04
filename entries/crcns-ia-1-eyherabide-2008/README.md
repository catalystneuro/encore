# Eyherabide, Rokem, Herz & Samengo (2008) from CRCNS ia-1

Tests the findings of [Eyherabide et al. (2008)](https://doi.org/10.3389/neuro.10.003.2008) that can
be tested on [CRCNS ia-1](https://doi.org/10.6080/K0BG2KWB), which holds the spike times of locust
auditory receptor cells driven by amplitude-modulated noise (Data1, the paper's data) and the
stimulus files. The cells' thresholds, which the paper's model needs, are not in the data set.

| Claim | Outcome |
|---|---|
| Cells, sessions and trials of the recordings | Partially reproduced |
| Kept sessions per stimulus protocol (Table 1) | Not reproduced |
| Firing rate 113 Hz, not different across protocols | Reproduced |
| Mean threshold 58 dB | Blocked: data missing |
| Bursting sessions per protocol (Table 1) | Partially reproduced |
| Percentage of isolated spikes per protocol (Table 1) | Not reproduced |
| Highest and average n per protocol (Table 1) | Not reproduced |
| Isolated spikes least likely at 12 dB and 100 Hz (Figure 5) | Reproduced |
| Shape of the correlation function across stimuli (Figure 3) | Reproduced |
| Error of the correlation function, 3.4% of its span | Reproduced |
| The model classifies sessions as the data do | Blocked: data missing |
| Bursts are less correlated than spikes (Figure 6) | Reproduced |
| Information per burst rises with n (Figure 7A, B) | Partially reproduced |
| Occurrence falls with n (Figure 7C, D) | Partially reproduced |
| Jitter does not depend on n (Figure 7E, F) | Reproduced |
| Information rate falls with n; n > 1 carry 47% (Figure 7G, H) | Not reproduced |
| Burst code against the direct method | Partially reproduced |
| Burst-triggered averages differ with n (Figure 8D) | Partially reproduced |
| Latency falls with n (Figure 8D) | Reproduced |
| Minimum of sigma_n at the same place for all n (Figure 8E) | Not reproduced |
| sigma_n below the SD of the stimuli before all spikes | Reproduced |
| nBTA differs from summed 1BTAs (Figure 9A, B) | Reproduced |
| Population nBTAs at 100 Hz (Figure 9C) | Reproduced |
| Burst size depends on the height of the stimulus maximum (Figure 10) | Not reproduced |
| Firing rate barely changes the limiting ISI | Reproduced |
| The model reproduces the coding trends | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's stated selection rule keeps 115 sessions in the data set where the paper kept 86.
Leaving out also the sessions with fewer than 98 trials and those sorted off-line keeps 89, close
to the paper's counts per protocol; the notebook uses that population and shows the 115 beside
it. The Methods leave open details of burst identification, for which the notebook shows every
reading. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-ia-1-eyherabide-2008-01.yaml`](../../attempts/crcns-ia-1-eyherabide-2008-01.yaml).

- `reproduce_eyherabide_2008.ipynb`: the analysis. It takes about nine minutes.
- `ia1.py`: streaming the zip from the CRCNS bucket, parsing spike and stimulus files, burst
  identification, information measures, the direct method with NSB entropies, and
  burst-triggered averages. Other notebooks on this data set can import it.
