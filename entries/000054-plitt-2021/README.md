# Plitt & Giocomo (2021) from dandiset 000054

Tests the findings of [Plitt & Giocomo (2021)](https://doi.org/10.1038/s41593-021-00816-6) on
[DANDI:000054](https://dandiarchive.org/dandiset/000054/0.260415.1712), which holds two-photon
imaging of CA1 with the aligned virtual reality behaviour of 16 mice (six rare morph, six frequent
morph and four decision mice) running morphed linear tracks.

| Claim | Outcome |
|---|---|
| Cells per session (161 to 3,657) | Reproduced |
| Session and trial counts | Partially reproduced |
| Link of the authors' VR deposit to the dandiset (link claim) | Reproduced |
| Intermediate trials before session 8 (deposit data) | Reproduced |
| Place-cell counts and fractions | Not reproduced |
| Fewer place cells in frequent morph mice | Reproduced |
| Overlap of S-tilde 0 and 1 place cells above chance | Partially reproduced |
| Overlap cells at the track ends and reward zone | Not reproduced |
| Place-cell similarity matrices differ between groups | Partially reproduced |
| NMF confirms discrete against gradual remapping | Not reproduced |
| UMAP separates rare and frequent morph cells | Reproduced |
| Licking rises before the reward | Reproduced |
| Block against gradual population similarity | Not reproduced |
| Checkerboard bands in six named sessions | Partially reproduced |
| Z-scored similarity differs at S-tilde 0.25 | Reproduced |
| Position-wise SF stable along the track | Reproduced |
| Delta D_KL sign and group means | Partially reproduced |
| Pooled Delta D_KL | Partially reproduced |
| Reconstructed priors | Not reproduced |
| MAP estimates | Reproduced |
| Patterns from session 3 on | Reproduced |
| Null models, rare morph sessions | Reproduced |
| Null models, frequent morph sessions | Partially reproduced |
| Decision mice like frequent morph mice | Reproduced |
| Hebbian model and its prior reconstruction (two claims) | Reproduced |
| Simulated posterior population | Not reproduced |
| Image statistics of the VR scenes | Blocked: data missing |
| Earlier morph studies (simulation only) | Blocked: other |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold only the imaged trials. Following a reader's answer, the priors behind every
posterior, and the training statistics, come from the authors' later deposit of all VR sessions on
figshare ([doi:10.6084/m9.figshare.31974756.v1](https://doi.org/10.6084/m9.figshare.31974756.v1)),
read file by file into memory; a link claim shows that its sessions match the dandiset's files.
The claims that use it are counted apart from those on the dandiset alone. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000054-plitt-2021-01.yaml`](../../attempts/000054-plitt-2021-01.yaml).

- `01_sessions_place_cells.ipynb`: the data check of every file, sessions, licking, place cells,
  their similarity matrices, NMF and UMAP. About 28 minutes, most of it streaming the files and the
  place-cell shuffles.
- `02_population_inference.ipynb`: the link to the figshare VR deposit and the training trials,
  population similarity, SF, Q estimates, prior reconstruction, the decision mice, the Hebbian
  model and the simulated posterior population, and the summary. About 24 minutes.
- `morph.py`: streaming and reducing the files, place cells, the stimulus axis, priors, posteriors,
  Q estimates, Delta D_KL, the mouse permutation test, and reading and linking the figshare VR deposit. Other notebooks on this dandiset can
  import it.
