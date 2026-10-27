# Ocagli et al. (2024) from Figshare item 26877211

Tests the findings of [Ocagli et al. (2024)](https://doi.org/10.1038/s41597-024-04294-w), a Data
Descriptor of an index scraped from the JECFA portal, on
[Figshare 26877211](https://doi.org/10.6084/m9.figshare.26877211.v1), version 1, which holds the
scraped table as `jecfa.rds` and `JECFA.csv`.

| Claim | Outcome |
|---|---|
| The deposit has 6552 rows and the 17 fields of Table 1 (link) | Reproduced |
| 6549 unique pages after removing a duplicate and a test page | Reproduced (6550) |
| Availability of each Table 1 field | Reproduced |
| Evaluations by year (Table 2) | Reproduced |
| Substances by functional class (Table 2) | Reproduced |
| The unknowns have only a JECFA name | Partially reproduced |
| FAS 40 to 52 (even codes) account for 50% of the records | Partially reproduced |
| Discrepancies found by the manual check of 700 pages | Blocked: data missing |
| The portal count of 6547 is in line with the pages with a JECFA name | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/figshare-26877211-ocagli-2024-01.yaml`](../../attempts/figshare-26877211-ocagli-2024-01.yaml).

- `reproduce_ocagli_2024.ipynb`: the analysis. It takes under a minute, most of it streaming the
  two files.
- `jecfa.py`: loading both files into memory, the measures of the criteria, and the FAS derivations
  of the paper's code (`R/process_df.R`, `R/add_metadata.R`). Other notebooks on this item can
  import it.
