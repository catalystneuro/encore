# Yemini, Lin, Nejatbakhsh et al. (2021) from dandiset 000541

Tests the whole-brain imaging findings of [Yemini et al. (2021)](https://doi.org/10.1016/j.cell.2020.12.012), "NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identification in C. elegans", on [DANDI:000541](https://dandiarchive.org/dandiset/000541/0.241009.1457). The dandiset holds the 21 OH16230 head recordings of Figure 6, each with NeuroPAL neuron identities, dNMF traces and the times of the three stimuli. The tail recordings and the imaging behind Figures 1 to 5 and 7 are not in it.

| Claim | Outcome |
|---|---|
| The traces match the paper's Zenodo deposit (link) | Partially reproduced |
| Neuron names match the Cook et al. connectome (link) | Reproduced |
| 21 heads, 189 neurons, 21 tails, median 18 animals per neuron | Partially reproduced (assumed; no tails) |
| All 21 heads show the published ASE and AWC responses | Not reproduced (19 of 21) |
| ASER excited by NaCl, ASE asymmetric | Reproduced |
| NaCl responses in AIN, AVF, AVH, AVJ, I2 and MI | Reproduced (assumed: per-trace normalisation; 4 of 6 on dF/F0) |
| Odors more inhibitory than NaCl | Reproduced |
| AWC ON/OFF asymmetric | Blocked: metadata insufficient |
| ASJ and RIC responses | Partially reproduced (assumed) |
| Downstream interneurons AIN, AVH, RIF, RIG, RIR respond | Reproduced |
| Tail responses | Blocked: data missing |
| Pharyngeal responses | Reproduced |
| Stimulus sets overlap but differ | Reproduced |
| AVF cycles at about 0.3 Hz | Not reproduced |
| Stimulus-specific correlations | Partially reproduced (assumed; a null window passes in part) |
| PCA trajectories distinguishable | Not reproduced |
| Low R2 with the connectome | Partially reproduced (heads only) |
| Variations do not improve it | Reproduced |
| Figures 1, 2, 4C, 5, 7B-C and S1A-G (8 claims) | Blocked: data missing |
| GABA network and extrasynaptic signaling (Figure 4B-F) | Blocked: the paper does not name its transmitter map or connectome (methods underspecified proposed) |
| Optimal coloring (Figure 7D-E) | Blocked: not runnable (MATLAB) |

Two methods the paper leaves open are taken as assumptions and shown under every reading: one member of each near-duplicate pair is removed, and traces are z-scored before the response tests. Tests on z-scored traces match the p values of the paper's Table S6 far better than tests on dF/F0. Removing one member comes closest to Table S6's per-class trace counts; agreement with its p values is about the same under all four selection readings (257 to 261 class agreements at 0.05).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is [`attempts/000541-yemini-2021-01.yaml`](../../attempts/000541-yemini-2021-01.yaml).

- `reproduce_yemini_2021.ipynb`: the analysis. It takes about five minutes, most of it streaming the files and reading the Zenodo deposit.
- `neuropal.py`: loading the files, the dF/F0 of the STAR Methods, near-duplicate removal, the response tests with Storey q values, and readers for the Zenodo deposit and the Cook et al. synapse counts. Other notebooks on this dandiset can import it.
