# Yemini, Lin, Nejatbakhsh et al. (2021) from dandiset 000541

Tests the whole-brain imaging findings of [Yemini et al. (2021)](https://doi.org/10.1016/j.cell.2020.12.012), "NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identification in C. elegans", on [DANDI:000541](https://dandiarchive.org/dandiset/000541/0.241009.1457). The dandiset holds the 21 OH16230 head recordings of Figure 6, each with NeuroPAL neuron identities, dNMF traces and the times of the three stimuli. The tail recordings and the imaging behind Figures 1 to 5 and 7 are not in it.

| Claim | Outcome |
|---|---|
| The traces match the paper's Zenodo deposit (link) | Partially reproduced |
| Neuron names match the Cook et al. connectome (link) | Reproduced |
| 21 heads, 189 neurons, 21 tails, median 18 animals per neuron | Partially reproduced (no tails) |
| All 21 heads show the published ASE and AWC responses | Not reproduced (19 of 21) |
| ASER excited by NaCl, ASE asymmetric | Reproduced |
| NaCl responses in AIN, AVF, AVH, AVJ, I2 and MI | Partially reproduced (4 of 6) |
| Odors more inhibitory than NaCl | Reproduced |
| AWC ON/OFF asymmetric | Blocked: metadata insufficient |
| ASJ and RIC responses | Partially reproduced (assumed) |
| Downstream interneurons AIN, AVH, RIF, RIG, RIR respond | Reproduced |
| Tail responses | Blocked: data missing |
| Pharyngeal responses | Reproduced |
| Stimulus sets overlap but differ | Reproduced |
| AVF cycles at about 0.3 Hz | Not reproduced |
| Stimulus-specific correlations | Reproduced (assumed; a null window passes too) |
| PCA trajectories distinguishable | Not reproduced |
| Low R2 with the connectome | Partially reproduced (heads only) |
| Variations do not improve it | Reproduced |
| Figures 1, 2, 4, 5, 7 and S1A-G (11 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is [`attempts/000541-yemini-2021-01.yaml`](../../attempts/000541-yemini-2021-01.yaml).

- `reproduce_yemini_2021.ipynb`: the analysis. It takes about five minutes, most of it streaming the files and reading the Zenodo deposit.
- `neuropal.py`: loading the files, the dF/F0 of the STAR Methods, near-duplicate removal, the response tests with Storey q values, and readers for the Zenodo deposit and the Cook et al. synapse counts. Other notebooks on this dandiset can import it.
