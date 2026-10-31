# Chartrand et al. (2023) from dandiset 000630

Tests the findings of [Chartrand et al. (2023)](https://doi.org/10.1126/science.adf0805) that can be
tested on [DANDI:000630](https://dandiarchive.org/dandiset/000630/0.230915.2257), which holds the
recordings of the paper's 210 Seattle human L1 patch-seq cells. Features are computed
with IPFX from the long square sweeps and compared with the paper's own per-cell values; cell types
come from the paper's cell table, which links to the files through the LIMS number in `session_id`.

| Claim | Outcome |
|---|---|
| The files match the paper's cell table one to one (link) | Partially reproduced |
| Cell counts by subclass (Table S2) | Reproduced |
| Subclasses differ in sag and initial firing rate (FDR p < 1e-7) | Partially reproduced |
| Subclass profiles (PAX6 low sag and high initial firing rate) | Reproduced |
| Upstroke adaptation against sag, R2 = 0.74 | Not reproduced |
| Sag and firing rate gradient within LAMP5 t-types | Partially reproduced |
| No effect of donor condition, sex or age | Reproduced |
| Input resistance varies with region | Reproduced |
| MC4R cells: strong sag and irregular firing | Reproduced |
| ADARB2 MC4R against SST CHRNA4 | Not reproduced |
| PAX6 TNFAIP8L3: initial firing rate and ADP | Reproduced |
| Electrophysiological d' is smaller within subclasses | Partially reproduced |
| Gaussian mixture F1 per subclass | Reproduced |
| Subclass classifier, 82% accuracy | Reproduced |
| Held-out classifier on Amsterdam and Szeged cells | Blocked: data missing |
| Mouse comparison (DANDI 000020): link | Partially reproduced |
| Human and mouse vary along different features | Reproduced |
| Mouse MC4R and PAX6 cells (irregular firing, doublets) | Not reproduced |
| Human against mouse sag, AP height and rheobase | Partially reproduced |
| Mouse TEa recordings (Fig. 3E) | Blocked: data missing |
| A-type potassium conductance densities (Fig. 3F) | Blocked: patch surface areas not public |
| Subclass proportions by species (Fig. 1E) | Blocked: metadata insufficient |
| L1 cytoarchitecture (Fig. 3B) | Blocked: metadata insufficient |
| Four morphology claims on the paper's deposited features | Three partially reproduced, one blocked |
| Ephys d' against transcriptomic d' (Fig. 6B) | Blocked: not attempted |
| Twelve claims on transcriptomic references, mouse morphology and morphology models | Blocked: not attempted |

After the second round of verification, three changes of outcome are proposed for a third round:
the subclass differences in sag and initial firing rate to reproduced (they hold when the features
are extracted without the Methods' 500 ms noise criterion, which the paper's own per-cell values
show its pipeline did not apply as measured here), and the LAMP5 gradient and the d' structure to
not reproduced (their criteria name no partial level).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/000630-chartrand-2023-01.yaml`](../../attempts/000630-chartrand-2023-01.yaml).

- `reproduce_chartrand_2023.ipynb`: the claims on the dandiset. It takes about 20 minutes, of
  which about 6 are streaming the files and extracting the features twice (with and without the
  500 ms noise criterion) and 10 the Gaussian mixture search.
- `mouse_comparison.ipynb`: the claims that compare the human cells with the paper's mouse cells
  from DANDI:000020 (about 10 minutes).
- `morphology_tables.ipynb`: four morphology claims on the paper's deposited morphology features
  (under a minute).
- `l1ephys.py`: loading the files, the IPFX feature extraction with the Methods' sweep QC, the
  paper's tables, and the statistics of the paper's code. Other notebooks on this dandiset can
  import it.
