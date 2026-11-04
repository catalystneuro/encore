# Yuan, Chatterjee, Leys, Odom & Salido (2025) from dandiset 001882

Tests the findings of [Yuan et al. (2025)](https://doi.org/10.3390/genes16010043) on
[DANDI:001882](https://dandiarchive.org/dandiset/001882/0.260701.1757). The dandiset holds no
recording: a spreadsheet of the seven patients with IMPG1 or IMPG2 variants (the paper's Table 1), a
Word document of in silico tool outputs, and the paper's Figures 1 to 4 as image files. The clinical
images exist only as the annotated panels of Figures 2 and 3.

| Claim | Outcome |
|---|---|
| Cohort counts: 7 carriers, 2 RP, 5 VMD (denominator 480 from the paper) | Reproduced |
| Genotypes, diagnoses, sexes, ages, inheritance and acuities of Table 1 | Reproduced (four claims) |
| Only M73 has reduced acuity among the VMD patients | Reproduced |
| F32 sector RP phenotype; superior field loss and no cystoid maculopathy in the RP patients | Reproduced (visual reading of Figure 2) |
| M83 and the five VMD phenotypes; M73 against F57 | Partially reproduced (seven claims) |
| Variant positions in the protein domains | Partially reproduced |
| ProtParam values of IMPG1 (Table 4) | Partially reproduced |
| gnomAD frequencies | Reproduced |
| Pathogenicity scores (Table 2) | Not reproduced |
| p.Asp423Glu is novel (no ClinVar entry) | Not reproduced |
| All Caucasian; normal EOG of M73; other gene variants | Blocked: data missing |
| Stability (Table 3) and residue contacts (Figure 4) | Blocked: not runnable (three claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The phenotype claims were read by the author on the deposited figure panels, which are the paper's
own figures, so they test the text against the published images, not against independent data. The
in silico claims use pinned or versioned outside services (Ensembl VEP, dbNSFP, CADD, gnomAD, ClinVar,
UniProt, InterPro). The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/001882-yuan-2025-01.yaml`](../../attempts/001882-yuan-2025-01.yaml).

- `reproduce_yuan_2025.ipynb`: the analysis. It takes about 15 minutes, most of it waiting for the
  Ensembl VEP service.
- `impg.py`: loading the spreadsheet, the Word document and the figure files, the panel boxes of
  Figures 2 and 3, the FAF lesion measures, the outside services and the ProtParam measures. Other
  notebooks on this dandiset can import it.
