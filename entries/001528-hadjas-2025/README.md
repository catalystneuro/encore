# Hadjas et al. (2025) from dandiset 001528

Tests the mouse findings of [Hadjas et al. (2025)](https://doi.org/10.1101/2025.06.03.657460) on
[DANDI:001528](https://dandiarchive.org/dandiset/001528/draft), which holds fiber photometry from
120 mice during optogenetic stimulation of STN or PPN inputs to the substantia nigra (Figures 2
to 5, S3 and S4). The dandiset has no published version; the draft as modified on 2026-09-01 was
used. The human tissue counts of Figure 1 are not in it.

| Claim | Outcome |
|---|---|
| Mice per group as in the figure legends | Not reproduced |
| SNr GABA neurons are excited by STN and PPN input | Reproduced |
| The SNr GABA response scales with frequency | Reproduced |
| Pan-DA response to a 250 ms STN train peaks 0.50 s after onset | Partially reproduced |
| Pan-DA response to STN input varies with train duration | Reproduced |
| Pan-DA response to STN input does not scale with frequency | Reproduced |
| Pan-DA response to PPN input varies with train duration | Not reproduced |
| Pan-DA response to PPN input does not vary with frequency | Reproduced |
| Opposite DA release in TS and DLS | Reproduced |
| TS DA release scales with frequency | Reproduced |
| DLS DA inhibition scales with frequency | Reproduced |
| 5 Hz stimulation increases DLS DA | Not reproduced |
| DLS DA rebounds after the train | Partially reproduced |
| DA terminals in TS and DLS respond oppositely | Reproduced |
| Vglut2+ DA neurons are excited | Reproduced |
| The Vglut2+ response scales with frequency | Reproduced |
| Anxa1+ DLS terminals are inhibited | Blocked: data missing |
| The Anxa1+ terminal inhibition scales with frequency | Partially reproduced |
| Anxa1+ terminals rebound after the train | Partially reproduced |
| Anxa1+ cell bodies are inhibited | Partially reproduced |
| Vglut2+ excited and Anxa1+ inhibited | Reproduced |
| Human tissue counts (Figure 1, S1; four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The analysis uses the lab's dF/F stored in the files. Many of the paper's statistics come out to
the first decimal. The dandiset holds Anxa1 DLS recordings for 9 of the 18 mice the paper
analyses; for the other nine mice it holds SNc recordings only. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/001528-hadjas-2025-01.yaml`](../../attempts/001528-hadjas-2025-01.yaml).

- `reproduce_hadjas_2025.ipynb`: the analysis. It takes about seven minutes, most of it streaming
  the files and recomputing the dF/F for the data check.
- `photometry.py`: loading the files, trial alignment, response measures, a recomputation of the
  dF/F, and the statistical tests. Other notebooks on this dandiset can import it.
