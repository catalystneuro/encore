# Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019) from dandiset 000574

Tests the findings of [Boran et al. (2019)](https://doi.org/10.1126/sciadv.aav3687) on
[DANDI:000574](https://dandiarchive.org/dandiset/000574/0.250815.1108), which holds the trials,
sorted units, scalp EEG, macroelectrode iEEG and microwire LFP of nine epilepsy patients doing a
modified Sternberg task (37 sessions, 8 s stored per trial).

| Claim | Outcome |
|---|---|
| Behavior: accuracy by set size, capacity, RT and workload, RT of errors (4 claims) | Reproduced |
| Electrode labels match the G-Node deposit (link) | Reproduced |
| 1526 neurons, 676 / 449 / 401 by region | Not reproduced |
| Spike sorting quality | Partially reproduced |
| Hippocampal maintenance neurons (Fig. 2B) and their load dependence (Fig. 2C) | Reproduced |
| Entorhinal probe neurons (Fig. 3E); probe-aligned peaks above button-aligned | Reproduced |
| Few probe neurons task specific | Partially reproduced |
| dPCA variance and set-size angles (Fig. 4A) | Not reproduced |
| Speed lowest in maintenance (Fig. 4B) | Partially reproduced |
| Distance largest in maintenance (Fig. 4C); hippocampal loadings (fig. S3d) | Reproduced |
| Encoding decodes later correctness (Fig. 4D) | Not reproduced |
| Maintenance decodes workload, leave-one-subject-out, maintenance neurons, no 6 against 8 (Fig. 4E, 4 claims) | Reproduced |
| Retrieval decodes IN/OUT (Fig. 4F) | Not reproduced |
| Subject 1 scalp EEG power | Partially reproduced |
| Subject 1 hippocampal power | Reproduced |
| Subject 1 maintenance neurons; subject 1 PLV with Pz | Partially reproduced |
| PLV peak in all subjects; workload PLV in eight of nine | Partially reproduced |
| Table S1 per subject; maintenance PLV above encoding; power unchanged; posterior gradient | Not reproduced |
| No left-right difference; no SOZ difference | Reproduced |
| Spike-field coherence (second notebook) | Partially reproduced |
| HFO rates | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dataset holds 1487 units where the paper has 1526, and gives no region for the microwires.
As the amended claims file says, a unit's region is that of the tip contact of its electrode
(contact 1): (a) its label as updated after visual inspection of MRI, which is the dandiset's
`location`, or (b) its Brainnetome label, which is not deposited for the four tip contacts
labelled by hand (25 units). The G-Node deposit of the data descriptor, read for the link
claim, flags those contacts. The electrode names give very different counts. The attempt record, with the reasons, the assumptions and the findings about
the dataset, is [`attempts/000574-boran-2019-01.yaml`](../../attempts/000574-boran-2019-01.yaml).

- `reproduce_boran_2019.ipynb`: all claims but spike-field coherence, and reading (b) of the regions
  for the selection claims. About 20 minutes, most of it decoding and dPCA resampling.
- `reproduce_boran_2019_sfc.ipynb`: spike-field coherence; streams the LFP of 47 microwires. About
  13 minutes.
- `reproduce_boran_2019_regions_b.ipynb`: the decoding and dPCA claims under reading (b) of the
  regions. About 14 minutes.
- `sternberg.py`: loading (tables, spikes, EEG, hippocampal iEEG, LFP, G-Node electrode labels), the permutation and
  cluster tests, multitaper spectra and PLV, pseudopopulation decoding, dPCA and PPC. Other
  notebooks on this dandiset can import it.
