# Mantas, Contestabile, Skara et al. (2024) from dandiset 001828

Tests the findings of [Mantas et al. (2024)](https://doi.org/10.1101/2024.12.22.629963), a bioRxiv
preprint, on [DANDI:001828](https://dandiarchive.org/dandiset/001828/0.261020.1002). The dandiset
holds the paper's behaviour and fiber photometry: open field pose, kinematics and VAME motif labels
(some sessions with photometry), optogenetically evoked dLight release, water drop and forelimb
reaching sessions with annotated events, and arrow maze pose. The histology, RNA-seq, qPCR and
nosepoke data of Figures 1 to 3 are not in it.

| Claim | Outcome |
|---|---|
| Evoked dLight release is larger in dCP than in cCP (Figure S2) | Reproduced |
| Anxa1 and DAT axons in dCP ramp to the water drop and drop after it (Figure 3D) | Not reproduced |
| dLight in dCP follows them, cCP has a reward profile (Figure 3E) | Partially reproduced |
| AUC changes from baseline (Figure 3F-G) | Blocked: methods underspecified |
| Anxa1 and dLight-dCP signals correlate with speed (Figure 4B) | Partially reproduced |
| dLight-cCP correlates negatively with speed (Figure 4B) | Reproduced |
| VAME finds 37 motifs (Figure 4C) | Not reproduced (the dandiset's labelling has 42) |
| Anxa1 activity at onsets of high-speed motifs (Figure 4E) | Partially reproduced |
| Motif onset AUC of Anxa1 against dLight-dCP and dLight-cCP (Figure 4F-G) | Reproduced |
| Motif onset AUC against motif speed, R = 0.83 (Figure 4H) | Partially reproduced |
| Anxa1-TeTx mice are slower in the open field (Figure 5C-E) | Reproduced |
| Their phenotype resembles the early PD models (Figure 5C-F) | Reproduced |
| Motif usage PC1 orders the groups by PD stage (Figure 5G) | Reproduced |
| PC1 loadings correlate with motif speed (Figure 5I) | Partially reproduced |
| Arrow maze speed lower on day 4 (Figure 6C) | Not reproduced |
| Reaching accuracy (Figure 6J) | Blocked: methods underspecified |
| Motif loadings and per-motif changes by the paper's motif numbers (Figure 5H, 5J, 5M; four claims) | Blocked: metadata insufficient |
| Arrow maze preference and efficiency (Figure 6D; two claims) | Blocked: data missing |
| RNA-seq (Figure 1B) | Blocked: GSE282753 lacks the cMfn2KO data |
| Histology, qPCR, self-stimulation and ratio tasks (16 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

Groups, cohorts and days are given only in the free text of each file's `session_description`, 86
open field sessions are labelled as `tmaze` sessions, subject genotypes conflict across files, and
the VAME labels cannot be mapped to the paper's motif numbers. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/001828-mantas-2024-01.yaml`](../../attempts/001828-mantas-2024-01.yaml); the questions for
a reader are in [`questions/001828.yaml`](../../questions/001828.yaml).

- `reproduce_mantas_2024.ipynb`: the analysis. It takes about two minutes, most of it streaming the
  516 NWB files.
- `anxa1.py`: listing and loading the four kinds of file, parsing the groups from the descriptions,
  and the peri-event, AUC and ANOVA measures. Other notebooks on this dandiset can import it.
