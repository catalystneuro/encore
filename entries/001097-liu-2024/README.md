# Liu, Nair et al. (2024) from dandiset 001097

Tests the findings of [Liu, Nair et al. (2024)](https://doi.org/10.1038/s41586-024-07916-w) that
can be tested on [DANDI:001097](https://dandiarchive.org/dandiset/001097/0.260624.0330), which holds
miniscope imaging of VMHvl alpha-cells and annotations of male and female behaviour during mating.

| Claim | Outcome |
|---|---|
| Accepting behaviour escalates over mating; resistance rises then falls (Figure 1b) | Reproduced |
| 83.9% of female mating time is male-responsive (Figure 1c) | Reproduced |
| Males spend 11.3 times more time in self-initiated mating behaviour (Figure 1d) | Reproduced |
| Mean interbout interval 13.7 s (Figure 1e) | Reproduced |
| Social behaviour for 62% of bouts and 23% of intervals (Figure 1g) | Reproduced |
| About 2 to 13% of cells tuned to a behaviour (Figure 2c) | Not reproduced |
| Behaviour GLMs explain 8 to 15% of variance (Figure 2e) | Not reproduced |
| Adding the other cells raises it to 46% (Figure 2f) | Reproduced |
| 30% of cells have ACHW above 25 s (Figure 2i) | Not reproduced |
| The receptive-day dimension stays low on unreceptive days (Extended Data Figure 6e) | Partially reproduced |
| Its cells are less persistent on unreceptive days (Extended Data Figure 7) | Partially reproduced |
| The population mean does not track receptivity (Extended Data Figure 10c) | Reproduced |
| Pencil-cup persistence (Extended Data Figure 3b) | Blocked: metadata insufficient |
| Optogenetic perturbation of the attractor (Figure 3h-k) | Blocked: data missing |
| Ten claims that need new rSLDS fits (Figures 3 to 5) | Blocked: other |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The paper's line-attractor claims rest on rSLDS models, which cannot be built or fit within the
registry's environment and time limit; two of them are tested with the authors' deposited weights
for two mice. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001097-liu-2024-01.yaml`](../../attempts/001097-liu-2024-01.yaml).

- `reproduce_liu_2024.ipynb`: the analysis. It takes about five minutes.
- `vmhvl.py`: listing and streaming the files, preprocessing as in the authors' code, behaviour
  rasters and bouts, the autocorrelation half-width, choice probability, the ridge GLM and the
  clock check. Other notebooks on this dandiset can import it.
