# Russo, Claar, Furregoni et al. (2025) from dandiset 000458

Tests the findings of [Russo et al. (2025)](https://doi.org/10.1038/s41467-025-58717-2) on
[DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), the version the paper
cites. The dandiset holds EEG, Neuropixels LFP and units, wheel speed and trial tables from 24
sessions of cortical electrical stimulation in mice (Claar et al. 2023). Ten sessions from ten mice
have the deep MOs stimulation the paper analyses, about a third of the paper's mouse data.

| Claim | Outcome |
|---|---|
| The dandiset holds the sessions behind Figures 1C and 2B | Partially reproduced |
| Human TMS-EEG and iEEG claims, on the paper's Source Data file (5 claims) | Reproduced |
| Human and mouse responses are similar (Figure 5A) | Blocked: data missing |
| The late EEG, LFP and CSD responses are larger at rest (Figure 1C to 1E, S1B) | Reproduced |
| The modulation depends on intensity (Figure S4) | Reproduced |
| The modulation holds for speed thresholds up to 5 cm/s | Not reproduced |
| The early component is not modulated in the EEG (Figure S5) | Reproduced |
| No modulation for posterior stimulation (Figure S6) | Blocked: data missing |
| Triphasic spiking pattern with a 127.8 ms silence | Partially reproduced |
| SM-TH rebound precedes cortical measures (Figure 2B) | Not reproduced |
| Latencies are shorter during running, and correlate on single trials (Figure S7) | Reproduced |
| SM-TH late rate is higher during running (Figure 3A) | Reproduced |
| MOs late rate is not modulated (Figure S9A) | Not reproduced |
| FS and TRN late rates are not modulated (Figure S10A) | Reproduced (fragile: FS rates are lower during running within sessions) |
| Relay unit ISIs are bimodal (HF and LF, Figure 3B) | Not reproduced |
| HF units respond earlier (Figure S11D) | Not reproduced |
| Higher intensity recruits more HF units (Figure S12) | Reproduced |
| Baseline thalamic rate doubles during running (Figure 3E) | Reproduced |
| LF onset variability rises during running (Figure 3E) | Not reproduced |
| HF response frequency falls during running (Figure 3E) | Reproduced |
| Thalamic features predict the EEG amplitude (Figure S13) | Not reproduced |
| LF cross-correlation differs by state (Figure S13D) | Not reproduced |
| Initial latency is more variable in SM-TH than MOs | Reproduced |
| Thalamic light delays the rebound (Figure 2F, 2G) | Not reproduced |
| Cortical light barely shifts the rebound (Figure S8B) | Reproduced |
| Thalamic or cortical light suppresses firing (Figure 2H) | Reproduced |
| Model claims (Figure 4, S14; 5 claims) | Blocked: not runnable (built and timed; too slow for the time limit) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/russo-2025-01.yaml`](../../attempts/russo-2025-01.yaml).

- `reproduce_russo_2025.ipynb`: the EEG, LFP, CSD and unit claims on the dandiset, the link claim,
  and the human claims on the Source Data file. It takes about 15 minutes, most of it streaming
  the EEG and the MOs LFP. Its model section builds the paper's network model and needs `make`
  and `g++`.
- `opto_russo_2025.ipynb`: the optogenetic claims on the paper's figshare deposit
  (doi:10.6084/m9.figshare.28440311.v1). About 3 minutes.
- `russo.py`: streaming of the dandiset's chunked arrays, the paper's EEG, LFP and CSD
  preprocessing, and the unit measures. Other notebooks on this dandiset can import it.
- `opto.py`: reading the figshare zip in place.
