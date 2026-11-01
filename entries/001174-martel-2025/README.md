# Martel et al. (2025) from dandiset 001174

Tests the findings of [Martel et al. (2025)](https://doi.org/10.1016/j.isci.2025.112767),
microendoscopic calcium imaging in SMA and M1 of four macaques at rest and during reaching, on
[DANDI:001174](https://dandiarchive.org/dandiset/001174/0.250331.2218) (version 0.250331.2218, the one
the paper cites). The dandiset holds, per session and condition, the miniscope movie, the accepted
cells' footprints, their denoised traces and their deconvolved events. It holds no TTL or trial data
and no raw traces, so the task-aligned analyses of Figure 2 and Figure S1 cannot be tested.

| Claim | Outcome |
|---|---|
| The dandiset's cells and descriptors match the paper's Zenodo per-cell table | Not reproduced (cells match, rates and amplitudes differ) |
| Cell counts per site (129, 61, 63, 37, 23) | Reproduced, through the Zenodo table's first occurrences |
| 18% of cells tracked across sessions | Blocked: metadata insufficient |
| No change of event rate or IEI CV from rest to task | Reproduced (two claims) |
| U SMA amplitude higher at rest than in the task | Reproduced |
| U event rate higher in M1 than in SMA | Reproduced |
| U task amplitude higher in M1 than in SMA | Not reproduced |
| Task-aligned responses (Figure 2, Figure S1; six claims) | Blocked: data missing |
| Synchronized pairs in SMA and M1, unrelated to distance, not changed by the task | Reproduced (three claims) |
| Example sequence counts (Figure 4A, 4B) | Blocked: methods underspecified (no setting of the detection gives the paper's own counts; two claims) |
| Sequence measures vary across conditions and sites | Reproduced |
| Cells in sequences not clustered | Blocked: methods underspecified |
| Histology (two claims) | Blocked: other (needs an anatomist's reading) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The cells' first occurrences come from the paper's per-cell table on Zenodo
(doi:10.5281/zenodo.14727695), as the dandiset does not identify cells across sessions. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/001174-martel-2025-01.yaml`](../../attempts/001174-martel-2025-01.yaml).

- `reproduce_martel_2025.ipynb`: data check, the link to the Zenodo table, Figures 1 and 3. About one and a
  half minutes on the last run (82 s), most of it streaming.
- `sequences_martel_2025.ipynb`: the sequence detection of Figure 4 on every 10-min slice, under each
  reading of the paper's open parameters, and a sweep of the detection's parameters against the paper's
  own counts. About fifteen minutes on the last run (915 s); an earlier run on another machine took about
  twenty-six.
- `sma_m1.py`: loading the files, the per-cell descriptors, the Z-Jaccard and the Zenodo tables.
- `sequences.py`: a Python (numba) port of the paper's `identify_sequences.m`.
