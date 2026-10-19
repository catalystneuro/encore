# Moore et al. (2025) from dandiset 001699

Tests the findings of [Moore et al. (2025)](https://doi.org/10.1101/2025.01.09.632139), a bioRxiv
preprint on head-direction coding in the postsubiculum of juvenile and adult Fmr1-/y rats, on
[DANDI:001699](https://dandiarchive.org/dandiset/001699/0.260917.2322). The dandiset holds the
silicon-probe recordings of 24 rats during open-field exploration and sleep, with spike times, mean
waveforms, head direction, position and sleep stages.

| Claim | Outcome |
|---|---|
| Unit and rat counts per group | Partially reproduced |
| Units per recording (8 to 83, 30 to 114) | Partially reproduced |
| No behavioural differences (juvenile, adult) | Reproduced (2 claims) |
| No differences in contamination, rates, vector length (juvenile, adult) | Reproduced (2 claims) |
| Juvenile Fmr1-/y cells more sharply tuned | Partially reproduced (HD information yes, width no) |
| Juvenile Fmr1-/y tuning curves drift less within a session | Reproduced |
| Juvenile Fmr1-/y decoder drift lower | Not reproduced (p = 0.085, same direction) |
| Juvenile Fmr1-/y better tuned to the waking Isomap angle | Not reproduced (p = 0.056, same direction) |
| Juvenile Fmr1-/y better tuned to the REM Isomap angle | Reproduced (p = 0.045) |
| Adult tuning, Isomap tuning (waking and REM) unchanged | Reproduced (3 claims) |
| Adult Fmr1-/y drift more, within and between sessions, and by decoding | Reproduced (3 claims) |
| Correlations of HD information (halves, sessions, Isomap) | 1 reproduced, 5 partially reproduced, 2 not reproduced |
| Juvenile drift between sessions unchanged | Reproduced |
| Probe tracts in PoSub (histology) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The archive labels H3026 as wild type and gives H3029 an adult's birth date; the paper's unit counts
match only if H3026 is a juvenile Fmr1-/y rat and H3029 a juvenile wild-type rat, and the analysis uses
that grouping, with the archive's labels and the juvenile results without H3026 as variants. Several juvenile effects
are near p = 0.05 and lose significance under these variants. H4825's file is a re-timed copy of H4824's
recording, so one adult Fmr1-/y rat is missing. The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/001699-moore-2025-01.yaml`](../../attempts/001699-moore-2025-01.yaml).

- `reproduce_moore_2025.ipynb`: the analysis. It takes about five minutes, most of it streaming the
  units and tracking of the 36 files and fitting Isomap, in parallel.
- `hdfx.py`: loading, cell selection, tuning curves, HD information, offsets, the decoder, Isomap and
  the mixed-model test. Other notebooks on this dandiset can import it.
