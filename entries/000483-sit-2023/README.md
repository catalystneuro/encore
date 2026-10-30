# Sit & Goard (2023) from dandiset 000483

Tests the findings of [Sit and Goard (2023)](https://doi.org/10.1038/s41467-023-37704-5),
"Coregistration of heading to visual cues in retrosplenial cortex", on
[DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321). The dandiset holds two-photon
recordings of retrosplenial somata and of ADN and visual cortical axons in RSC, made in a floating
chamber rotated by a motor, by the mouse or with the head rotated. The files hold raw ROI
fluorescence and chamber heading, with no neuropil trace, dF/F or inferred spikes; the notebooks
compute them.

| Claim | Outcome |
|---|---|
| 14.0% heading cells in the free chamber (Fig. 1D, E) | Blocked: data missing |
| 14.2% heading cells with motor rotation (Fig. 1G) | Reproduced (rests on an assumption) |
| No cell passes the test on pre-shuffled data | Not reproduced (rests on an assumption) |
| Preferred headings tile the chamber (Fig. 1H) | Partially reproduced (rests on an assumption) |
| Same preference under head and chamber rotation (Fig. 2F) | Partially reproduced (rests on assumptions) |
| Coherent remapping (Fig. 3C) | Partially reproduced (rests on an assumption) |
| ADN axons unimodal, visual axons bimodal in light (Fig. 4) | Reproduced |
| ADN axons keep tuning in the dark, visual axons lose it (Fig. 4) | Partially reproduced |
| Three classes by clustering (Fig. 5B) | Not reproduced |
| Class proportions (Fig. 5C to E) | Not reproduced |
| Alignment cells' dark peak at a light peak (Fig. 5E) | Partially reproduced |
| Heading cells' flip score unchanged in the dark (Fig. 5F) | Partially reproduced |
| Landmark and alignment flip scores drop in the dark (Fig. 5G, H) | Partially reproduced |
| Axons within the soma clusters (Fig. 5I) | Partially reproduced |
| Visual-cue-only rotation (Fig. 5K) | Blocked: metadata insufficient |
| Diversity persists across rotation direction (Fig. S5) | Reproduced |
| Diversity persists with animal or motor control (Fig. S6) | Not reproduced (rests on an assumption) |
| Decoding from all tuned cells, light-on (Fig. 6A) | Not reproduced |
| Decoding from all tuned cells, light-off (Fig. 6A) | Partially reproduced (rests on an assumption) |
| Decoding from heading cells (Fig. 6B) | Partially reproduced (rests on an assumption) |
| Decoding from landmark cells (Fig. 6B) | Partially reproduced (rests on an assumption) |
| Decoding from alignment cells (Fig. 6B) | Not reproduced |
| 180 degree errors of landmark, not heading, cells (Fig. 6B) | Reproduced (rests on an assumption) |
| Heading cells decode worse than all tuned cells (Fig. 6B) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000483-sit-2023-01.yaml`](../../attempts/000483-sit-2023-01.yaml).

- `single_cue.ipynb`: the data check of all 128 files, and Figure 1 (about 9 minutes).
- `rotation_remapping.ipynb`: Figures 2 and 3 (about 11 minutes).
- `axons.ipynb`: Figure 4 (about 6 minutes).
- `somata.ipynb`: Figure 5 (about 17 minutes).
- `directions.ipynb`: Figures S5 and S6, and the visual-cue-only files of Figure 5K (about 10 minutes).
- `decoding.ipynb`: Figure 6; it rebuilds the classes of `somata.ipynb` (about 16 minutes).
- `rsc.py`: loading, dF/F and spikes, trials, the heading-selection test of the paper's code,
  alignment, flip score and V-test. Other notebooks on this dandiset can import it.
