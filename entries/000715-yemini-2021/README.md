# Yemini, Lin, Nejatbakhsh et al. (2021), NeuroPAL, from dandiset 000715

Tests the findings of [Yemini et al. (2021)](https://doi.org/10.1016/j.cell.2020.12.012) that can
be tested on [DANDI:000715](https://dandiarchive.org/dandiset/000715/0.241009.1514), which holds the
head volumes and hand-annotated neurons of the paper's ten NeuroPAL atlas worms (otIs669). The tails
of the same worms, and the whole-brain activity recordings, are on the paper's Zenodo record
(doi:10.5281/zenodo.3906530), not in the dandiset.

| Claim | Outcome |
|---|---|
| Positional variability differs across neurons (head) | Reproduced |
| OLLR is over twice as variable as OLLL along the anterior-posterior axis | Reproduced |
| Automatic detection, 80% accuracy and 90% precision and recall (head) | Partially reproduced |
| Identification accuracy 86% in the head | Not reproduced |
| Accuracy without color 50% in the head | Not reproduced |
| Eight guided annotations bring head accuracy above 90% | Not reproduced |
| Guided annotation beats random annotation (head) | Reproduced |
| Confidence is calibrated | Blocked: the criterion's two readings disagree |
| NeuroPAL leaves 3.5% color violations (with the paper's NeuroPAL colors) | Reproduced |
| Optimal coloring finds 1.7% with 39 reporters and 10.5% with 3 (with the paper's reporter table) | Partially reproduced |
| Ventral ganglion least accurate | Blocked |
| Whole-brain activity, five claims on the Zenodo record (counted apart) | 2 reproduced, 1 partially, 2 not reproduced |
| Reporter expression, mutants, phenotypes and other activity claims | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files' metadata describe another strain (OH16230), microscope and preparation, and dates in
2021; two of the volumes are identical to the Zenodo volumes of the otIs669 atlas worms. With the
held-out worm aligned by its true correspondences the atlas and colors from the dandiset give 78 to
80% head accuracy, so the shortfall in identification comes from the alignment step as the paper
and its code describe it, run here on worms imaged in two orientations.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000715-yemini-2021-01.yaml`](../../attempts/000715-yemini-2021-01.yaml).

- `reproduce_yemini_2021.ipynb`: the dandiset's claims. It takes about 17 minutes, six of them
  for the neuron detection.
- `wholebrain_zenodo.ipynb`: five whole-brain activity claims on the Zenodo record, about 4
  minutes, most of it reading the record.
- `optimal_coloring.ipynb`: the optimal-coloring claim, a Python port of the paper's solver run
  on the dandiset's head atlas, about 20 minutes.
- `neuropal.py`: loading, color readout, the statistical atlas, identification, guided
  annotation, detection, color violations and the optimal-coloring solver, with the source of
  each parameter.
- `wholebrain.py`: reading the Zenodo activity files and the response tests of the STAR Methods.
