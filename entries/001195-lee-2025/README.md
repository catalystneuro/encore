# Lee, Matthews, Lemieux et al. (2025) from dandiset 001195

Tests the findings of [Lee, Matthews, Lemieux et al. (2025)](https://doi.org/10.7554/eLife.105955) that can be
tested on [DANDI:001195](https://dandiarchive.org/dandiset/001195/0.250408.1733). The dandiset holds the ex vivo
patch-clamp recordings of Figure 6 and Figure 7 supplement 1, tested here, and the in vivo CeA calcium imaging of
Figure 7, without the pose or cup-interaction data its analysis needs. The tracing, behavioural and RNAscope data of
Figures 1 to 5 and 8 are not in it.

| Claim | Outcome |
|---|---|
| EPSPs and IPSPs at rest in the BNST, CeA and BLP (Figure 6D-F) | Reproduced |
| Firing responses: BNST excited, CeA and BLP mixed (Figure 6G-I) | Partially reproduced |
| EPSP amplitude differs by region, CeA above BLP (Figure 6J) | Reproduced, on an assumption |
| IPSP trough differs by region (Figure 6K) | Not reproduced |
| Responses survive TTX/4AP (Figure 6 supplement 1D-E) | Blocked: metadata insufficient |
| CeA clusters: late-firing excited, regular-firing inhibited (Figure 6N-O) | Partially reproduced |
| CeA clusters differ in their four properties | Reproduced |
| BLP clusters: 93% of pyramidal inhibited, 62% of interneurons excited (Figure 6P-Q) | Partially reproduced |
| BLP clusters differ in their four properties | Reproduced |
| Voltage area differs between clusters (Figure 6 supplement 1J-K) | Reproduced |
| Combined CeA and BLP clustering (Figure 6 supplement 1L-N) | Not reproduced |
| Red light evokes larger ChrimsonR potentials than blue (Figure 7 supplement 1E-F) | Reproduced |
| Red-evoked potentials smaller during blue light (Figure 7 supplement 1H-I) | Partially reproduced |
| In vivo imaging (eight claims, Figure 7 and its supplements) | Blocked: data missing |
| Figures 1 to 5 and 8 (17 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not record when the light was on, so the notebook takes the time from the responses. The imaging
files are stated at 25 Hz but match the behaviour videos only at the Methods' 20 Hz, hold about twice as many ROIs
as the paper's cell counts, and describe another experiment in their virus and stimulus fields. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001195-lee-2025-01.yaml`](../../attempts/001195-lee-2025-01.yaml).

- `reproduce_lee_2025.ipynb`: the analysis. It takes about 15 minutes, most of it streaming the patch-clamp sweeps.
- `drn_ephys.py`: loading the patch-clamp files, the evoked potential, firing and baseline measures, and the
  Prism-style post hoc tests. Other notebooks on this dandiset can import it.
