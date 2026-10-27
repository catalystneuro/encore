# Wang, Wang, Yang, Lu, Fields, Xu, Shen, Wei & Friman (2024) from Dryad dataset tdz08kq5d

Tests the findings of [Wang et al. (2024)](https://doi.org/10.1093/evlett/qrad056) on
[doi:10.5061/dryad.tdz08kq5d](https://doi.org/10.5061/dryad.tdz08kq5d), version 263142, one workbook with
the data behind each figure: the selection experiment of Figure 1, the per-clone traits of Figure 2, the
variant calls of Table 1, the adsorption assay of Figure S3 and the transcriptome tables of Figure 4.

| Claim | Outcome |
|---|---|
| Higher bacterial densities at 35 than at 25 degrees C (Figure 1B) | Reproduced |
| Phage reduced bacterial densities at both temperatures | Reproduced |
| The phage effect diminished over time | Reproduced |
| Area under the curve reduced by 66.8% at 25 and 37.18% at 35 degrees C | Reproduced |
| Phage densities higher at 25 degrees C, rising then falling (Figure 1C) | Reproduced |
| Mucoid colonies lost with phage except in one replicate (Figure 1D) | Reproduced |
| About 20% and 55% mucoid without phage; phage raised SCV frequency | Partially reproduced |
| Phage-exposed clones more resistant (Figure 2A) | Reproduced |
| Clones from 35 degrees C more resistant | Reproduced |
| No temperature by phage interaction for resistance | Reproduced |
| SCVs more resistant than mucoid clones | Reproduced |
| Mucoid clones of one 25 degrees C phage replicate resistant | Reproduced |
| SCVs grow faster (Figure 2B) | Reproduced |
| SCVs have lower carrying capacity (Figure 2C) | Reproduced |
| No exposure effect on SCV twitching (Figure 2D) | Reproduced |
| 25 degrees C phage mucoid clones twitch less | Reproduced |
| Mucoid clones form more biofilm than the ancestor, SCVs as much (Figure 2E) | Not reproduced |
| No exposure effect on biofilm | Reproduced |
| Phage exposure reduced virulence (Figure 2F) | Reproduced |
| All SCVs avirulent | Reproduced |
| 25 degrees C phage mucoid clones avirulent | Reproduced |
| 8.5 nonsynonymous mutations per clone | Not reproduced |
| phcS mutations in 13 of 16 SCVs (Table 1) | Reproduced |
| pilD mutations in two 25 degrees C phage mucoid clones | Reproduced |
| gspE or gspF mutations in three of four 35 degrees C phage SCVs | Blocked: metadata insufficient |
| pilB and pilM mutants resistant (Table S6) | Blocked: data missing |
| pilD mutants adsorb less phage, phcS and T2SS mutants do not (Figure S3) | Reproduced |
| 1477 genes differentially expressed, 707 up and 770 down (Figure 4A) | Reproduced |
| Five KEGG pathways enriched (Figure S5) | Blocked: methods underspecified |
| phcR and phcS up, pilD down, 7 of 13 mutated genes differentially expressed | Not reproduced |
| Defense system genes up, JetC down (Figure 4C) | Reproduced |
| Type II and III secretion genes down | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The deposited data reproduce nearly every statistical table of the paper exactly, under the OD time points
and the ANOVA unit that the claims file names after a reader answered this attempt's questions (days 2 to 12
for Table S1a, replicate means by colony type for Tables S3a to S3c). The
exceptions are the twitching sheet, whose strain names do not identify the clones and whose values do not
reproduce Table S3d, and several statements of the text that the deposited tables contradict (SCV biofilm
above the ancestor, gspG up, phcS below the fold-change threshold). The growth curves, per-clone variant
calls, genome reads and the Table S6 data are not deposited. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/dryad-tdz08kq5d-wang-2024-01.yaml`](../../attempts/dryad-tdz08kq5d-wang-2024-01.yaml).

- `reproduce_wang_2024.ipynb`: the analysis. It runs in under a minute.
- `phage_temp.py`: loading the workbook with its checksum, tidy tables for each sheet, and the
  repeated-measures and clone ANOVAs. Other notebooks on this dataset can import it.
