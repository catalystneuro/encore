# Mills, Lee, Howe, Li et al. (2026) from dandiset 001203

Tests the findings of [Mills et al. (2026)](https://doi.org/10.1016/j.neuron.2026.08.012) that can be
tested on [DANDI:001203](https://dandiarchive.org/dandiset/001203/0.261103.1719), which holds Open
Ephys and Neuropixels recordings of the amygdalostriatal transition zone (ASt) and calcium imaging of
its Drd1a+ and Drd2+ neurons during a two-tone discrimination task and contextual fear.

| Claim | Outcome |
|---|---|
| The dandiset holds the paper's ephys units, with its counts per region and group | Not reproduced |
| Sustained ASt responses to CS-shock, not CS-reward (Figure S9) | Partially reproduced |
| ASt trajectories for the two cues diverge from onset (Figure 2Q) | Reproduced |
| Single-trial shock-reward trajectories less similar than same-cue pairs (Figure S8) | Partially reproduced |
| CS identity decoded from ASt activity in paired mice (Figure 3H) | Not reproduced |
| Imaging mice discriminate the cues (Figure S13) | Reproduced |
| Drd2+ CS-shock responses greater in paired mice (Figure 5J) | Partially reproduced |
| Drd1a+ responses do not differ between groups (Figure 5H-I) | Not reproduced |
| Drd2+ CS-reward responses do not differ between groups (Figure 5K) | Not reproduced |
| Drd2-rich clusters respond to CS-shock (Figure 5M) | Not reproduced |
| No change in activity between contexts (Figure S15) | Not reproduced |
| Ephys behavior claims (three) | Blocked: metadata insufficient |
| Region comparisons, unpaired controls, GLM, unpredicted US (eighteen) | Blocked: data missing |
| RNAscope and optogenetics (thirteen) | Blocked: data missing |
| snRNA-seq (three) | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The Neuropixels files have no trial events, no behavior and no region per unit, so the ephys claims
are tested on the 10 paired ASt mice recorded with Open Ephys, and claims on TS, CeA or unpaired
neurons are blocked. The poses of the Open Ephys sessions are on a different clock from their spikes
and trial events. The imaging files hold every CNMF-E ROI, not the paper's curated neurons, and the
three imaging claims of no difference fail on them. The attempt record, with the reasons and the
differences from the paper's method, is [`attempts/mills-2026-01.yaml`](../../attempts/mills-2026-01.yaml).

- `reproduce_mills_2026.ipynb`: the analysis. It takes about 20 minutes, most of it streaming the files.
- `mills.py`: loading the files, cue responses for spikes and calcium, and freezing and darting from
  the poses. Other notebooks on this dandiset can import it.
