# Malfatti, Velica et al. (2026) from dandiset 002056

Tests the findings of [Malfatti, Velica et al. (2026)](https://doi.org/10.7554/eLife.109286) that
can be tested on [DANDI:002056](https://dandiarchive.org/dandiset/002056/0.261113.1541). The
dandiset holds DeepLabCut tracking of the single pellet prehension task for three groups of mice
(behaviour-only learning, miniscope, LFP), the raw miniscope videos, and one LFP channel per mouse
of the LFP group.

| Claim | Outcome |
|---|---|
| No genotype effect on learning (Figure 1F-H) | Reproduced |
| Effect of session on learning (Figure 1F-H) | Reproduced |
| Failed prehensions overlap more often than successful ones | Partially reproduced |
| CLZ raises the success ratio of trained Cre+ mice (Figure 4B) | Reproduced |
| Higher theta and low theta power in Cre+ mice (Figure 4D) | Not reproduced |
| Higher high theta power on successful prehensions (Figure 4E) | Not reproduced |
| Gamma effects in session 13 (Figure 4F-H) | Not reproduced |
| Genotype by session interaction outside prehensions (Supplemental Figure 7) | Not reproduced |
| Calcium imaging findings (Figures 1J, 2, 3, Supplemental Figures 2 to 6; 21 claims) | Blocked: data missing |
| Histology and caspase ablation (Supplemental Figure 1, Figure 5; 5 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The miniscope data are raw video only, with no extracted cells or traces, and the paper does not
give the CNMF-E parameters to extract them again. In the behaviour-only group the files of session 6 are
copies of session 5. The LFP of four control mice shows no prehension-locked potential at the deposited alignment and
one about 8 s earlier, which the files cannot confirm as a clock offset. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/malfatti-2026-01.yaml`](../../attempts/malfatti-2026-01.yaml).

- `reproduce_malfatti_2026.ipynb`: the analysis. It takes about 10 to 20 minutes, most of it streaming
  the files.
- `m1mc.py`: loading the files, the prehension detection and classification of the paper's code,
  LFP band power, and the mixed ANOVA and ANOVA-type statistics. Other notebooks on this dandiset
  can import it.
