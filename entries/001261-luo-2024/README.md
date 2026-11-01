# Luo, Jiang, Desai et al. (2024) from dandiset 001261

Tests the findings of [Luo et al. (2024)](https://doi.org/10.1002/cne.70001) that can be tested on
[DANDI:001261](https://dandiarchive.org/dandiset/001261/0.250917.2023), which holds whole-cell
current-clamp recordings of BLA-projecting NBM/SI neurons: 48 cholinergic and 46 noncholinergic
files from 27 mice, and 46 cholinergic and 12 noncholinergic files from 9 macaques. The morphology
of the paper is not in it.

| Claim | Outcome |
|---|---|
| Sample sizes | Partially reproduced |
| Mouse cholinergic and noncholinergic neurons differ in 15 of 18 features | Not reproduced |
| Noncholinergic neurons fire about six times faster | Partially reproduced |
| Cholinergic neurons have a higher threshold and rheobase | Partially reproduced |
| Cholinergic neurons have a larger and wider AHP | Partially reproduced |
| Cholinergic neurons adapt more | Reproduced |
| Cholinergic neurons have a higher resting potential and a longer tau | Partially reproduced |
| Spike amplitude, CV of intervals and sag differ (Fig. S2-2) | Partially reproduced |
| UMAP separates the mouse groups with two errors | Not reproduced |
| LDA separates the mouse groups | Reproduced |
| AHP amplitude has the largest LDA weight | Reproduced |
| Macaque cholinergic neurons are more excitable than mouse ones | Partially reproduced |
| Macaque neurons have a lower threshold and a smaller, narrower AHP | Partially reproduced |
| Macaque neurons have wider spikes | Partially reproduced |
| Spike amplitude, CV, sag and upstroke differ between species (Fig. S7-1) | Partially reproduced |
| Most features differ between species | Not reproduced |
| Macaque neurons have a larger input resistance and a smaller rheobase | Reproduced |
| UMAP separates macaque from mouse strongly | Blocked: methods underspecified |
| Morphology, Sholl analysis and combined features (eleven claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The features are re-implemented in Python from the paper's Methods and its MATLAB code. The
resting potential is not recorded, so the feature counts are out of 17. Where the Methods and the
code differ, the claims file makes the Methods decide; for the AHP the paper's values match the
code's window, not the Methods'. The dandiset repeats two recordings (one of them under both
mouse groups), holds one macaque file scaled 20 times too large, and has eight neurons that do not
depolarise with positive steps. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/001261-luo-2024-01.yaml`](../../attempts/001261-luo-2024-01.yaml).

- `reproduce_luo_2024.ipynb`: the analysis. It takes about two minutes, a quarter of it reading the
  files.
- `nbmsi.py`: loading the files, the 18 features of the paper with their variants, the rank-sum
  tables, the UMAP and the LDA. Other notebooks on this dandiset can import it.
