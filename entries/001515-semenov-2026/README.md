# Semenov et al. (2026) from dandiset 001515

Tests the findings of [Semenov et al. (2026)](https://doi.org/10.1016/j.bioelechem.2026.109283) on
[DANDI:001515](https://dandiarchive.org/dandiset/001515/0.261006.1841). The dandiset names the paper,
but it holds FluoVolt strobe-imaging time courses of CHO cells charged by single 1-us pulses at one
amplitude per cell, the protocol the paper attributes to its reference [20]. None of the paper's own
recordings is in it.

| Claim | Outcome |
|---|---|
| Eq. (2): a 10-fold rise of membrane conductivity reduces IMP by ~2%, a 100-fold rise by 12% | Partially reproduced |
| The other 33 claims (Figures 1 to 7) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record is [`attempts/001515-semenov-2026-01.yaml`](../../attempts/001515-semenov-2026-01.yaml).

- `reproduce_semenov_2026.ipynb`: the data check and the one tested claim. It takes about four
  minutes (231 s in the last run), most of it streaming the files.
- `strobe.py`: listing and reading the files, a membrane mask and polarization index per frame, and Eq. (2)
  of the paper. Other notebooks on this dandiset can import it.
