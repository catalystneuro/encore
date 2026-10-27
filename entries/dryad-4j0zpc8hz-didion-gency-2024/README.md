# Didion-Gency et al. (2024) from Dryad dataset 4j0zpc8hz

Tests the findings of [Didion-Gency et al. (2024)](https://doi.org/10.1093/plphys/kiad565), Plant
Physiology 194, on [DRYAD:4j0zpc8hz](https://doi.org/10.5061/dryad.4j0zpc8hz) (version id 260590),
which holds one table of 96 beech and oak trees grown in open-top chambers under warming and soil
moisture reduction, in monocultures and mixtures, measured from 2019 to 2021.

| Claims | Outcome |
|---|---|
| Phenology against air temperature (Figure 1, six claims), GDD against chilling days, maximum chilling days | Reproduced |
| Leaf water potential under the treatments (Figure 3, four claims) | 1 reproduced, 1 partially, 2 not reproduced |
| Carbon relations and growth under the treatments (Figure 4, ten claims) | 3 reproduced, 2 partially, 5 blocked (methods underspecified) |
| No seasonal variation of the leaf-level traits (Table S6) | Blocked (methods underspecified) |
| Species mixture and biodiversity effects (Tables S2 and S3, Figure 5, eleven claims) | 3 reproduced, 5 not reproduced, 3 blocked (methods underspecified) |
| Soil moisture, chamber climate and initial sizes (five claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dataset's treatment codes differ from its metadata, it has duplicated rows and negative
concentrations, its growing season length does not follow the Methods' definition, and it lacks the
soil moisture and chamber climate records. Refitting the paper's treatment model on it reproduces
Supplemental Table S1 for some traits exactly. Where the claims file leaves a method detail open,
every reading is run, and claims whose readings disagree are blocked. The
analysis follows the answers to the three questions the first run asked
([`questions/dryad-4j0zpc8hz.yaml`](../../questions/dryad-4j0zpc8hz.yaml)). The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/dryad-4j0zpc8hz-didion-gency-2024-01.yaml`](../../attempts/dryad-4j0zpc8hz-didion-gency-2024-01.yaml).

- `reproduce_didion_gency_2024.ipynb`: the analysis. It takes about two minutes.
- `oaktrees.py`: loading the workbook, the tree-year and campaign tables, the mixed model with nlme's
  F tests and multcomp-style contrasts, the biodiversity effects and the negative exponential fits.
  Other notebooks on this dataset can import it.

Dryad needs a token to download a file, so the files of the pinned version are staged in
`/tmp/dryad/4j0zpc8hz/260590/` before the notebook runs (`tools/stage_files.py`).
