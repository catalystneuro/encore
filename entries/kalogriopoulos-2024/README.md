# Kalogriopoulos, Tei et al. (2024) from dandiset 001354

Tests the findings of [Kalogriopoulos, Tei et al. (2024)](https://doi.org/10.1038/s41586-024-08282-3)
that rest on [DANDI:001354](https://dandiarchive.org/dandiset/001354/0.250312.0036), which holds
whole-cell current clamp recordings of 50 CA1 neurons from 8 mice expressing anti-mCherry
PAGER-Gi, the acute slice experiment of Fig. 4e-j and Extended Data Fig. 12a-h.

| Claim | Outcome |
|---|---|
| 15 cells from 7 mice with DCZ, 26 cells from 6 mice with DCZ plus mCherry | Blocked: metadata insufficient |
| Every DCZ plus mCherry cell preincubated 30 to 150 min (mean 73.4) | Blocked: data missing |
| Greater RMP hyperpolarization with DCZ plus mCherry (Fig. 4i) | Blocked: metadata insufficient |
| Greater rheobase increase with DCZ plus mCherry (Fig. 4j) | Blocked: metadata insufficient |
| Input resistance trend (Extended Data Fig. 12b) | Blocked: metadata insufficient |
| mEGFP expression and baseline, shifts and RMP (Extended Data Fig. 12c-h, three claims) | Blocked: data missing |
| Cell culture, imaging and biochemistry (24 claims) | Blocked: data missing |

The files do not record which cells received DCZ alone and which DCZ plus mCherry, when DCZ was
applied, the mEGFP intensity of each cell, or the mCherry preincubation time, so no claim can be
tested. The notebook checks the files against the paper and computes the paper's per-sweep
measures (RMP, input resistance, rheobase) and exclusions for all cells. It finds that the
second channel of every sweep holds the injected current under a membrane potential type, that
the stored stimulus gives the ramp as a step, and that 10 of the 50 cells received a steeper ramp
than the Methods describe. The attempt record, with the reasons, is
[`attempts/kalogriopoulos-2024-01.yaml`](../../attempts/kalogriopoulos-2024-01.yaml).

- `reproduce_kalogriopoulos_2024.ipynb`: the data check and the measures. It takes about 16
  minutes, nearly all of it streaming the 12,858 sweeps.
- `pager_slice.py`: loading the files and the per-sweep measures and exclusions of the Methods.
  Other notebooks on this dandiset can import it.
