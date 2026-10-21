# Mantas, Contestabile, Skara et al. (2024) from dandiset 001828

Tests the findings of [Mantas et al. (2024)](https://doi.org/10.1101/2024.12.22.629963), a bioRxiv
preprint, on [DANDI:001828](https://dandiarchive.org/dandiset/001828/0.261020.1002). The dandiset
holds the paper's behaviour and fiber photometry: open field pose, kinematics and VAME motif labels
(some sessions with photometry), optogenetically evoked dLight release, water drop and forelimb
reaching sessions with annotated events, and arrow maze pose. The histology, RNA-seq, qPCR and
nosepoke data of Figures 1 to 3 are not in it. The MitoPark RNA-seq counts are read from GEO
GSE282753, which lacks the cMfn2KO counts the same claim needs.

| Claim | Outcome |
|---|---|
| Evoked dLight release is larger in dCP than in cCP (Figure S2) | Reproduced |
| Anxa1 and DAT axons in dCP ramp to the water drop and drop after it (Figure 3D) | Not reproduced |
| dLight in dCP follows them, cCP has a reward profile (Figure 3E) | Not reproduced (cCP holds, dCP does not) |
| AUC changes from baseline (Figure 3F-G) | Partially reproduced (holds with one of two z-scorings) |
| Anxa1 and dLight-dCP signals correlate with speed (Figure 4B) | Partially reproduced (Anxa1 misses p < 0.05; not reproduced is proposed for a third round) |
| dLight-cCP correlates negatively with speed (Figure 4B) | Reproduced |
| Anxa1-TeTx mice are slower in the open field (Figure 5C-E) | Reproduced |
| Their phenotype resembles the early PD models (Figure 5C-F) | Reproduced |
| Arrow maze speed lower on day 4 (Figure 6C) | Not reproduced |
| Reaching accuracy (Figure 6J) | Partially reproduced (controls and TeTx hold, Arch lower but not significantly) |
| VAME motifs, motif-onset signals, motif PCA and per-motif changes (Figure 4C-H, 5G-J, 5M; ten claims) | Blocked: data missing (the paper's motif labelling is not in the dandiset) |
| Arrow maze preference and efficiency (Figure 6D; two claims) | Blocked: data missing |
| RNA-seq (Figure 1B) | Blocked: GSE282753 lacks the cMfn2KO data (Anxa1 is down in MitoPark) |
| Histology, qPCR, self-stimulation and ratio tasks (15 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

Groups, cohorts and days are given only in the free text of each file's `session_description`, 86
open field sessions are labelled as `tmaze` sessions, subject genotypes conflict across files, and
the VAME labels are not the paper's motifs and are stored about 18 frames early. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/001828-mantas-2024-01.yaml`](../../attempts/001828-mantas-2024-01.yaml); the questions for
a reader, and their answers, are in [`questions/001828.yaml`](../../questions/001828.yaml).

- `reproduce_mantas_2024.ipynb`: the analysis. It takes about 2.5 minutes (printed at its end), most of it streaming the
  516 NWB files and the two DESeq2 fits.
- `anxa1.py`: listing and loading the four kinds of file, parsing the groups from the descriptions,
  the peri-event, AUC and ANOVA measures, and reading the GEO counts with the DESeq2 and edgeR
  readings. Other notebooks on this dandiset can import it.
