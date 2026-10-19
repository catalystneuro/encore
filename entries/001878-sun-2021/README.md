# CalMS21 (Sun et al. 2021) from dandiset 001878

Tests the claims of [Sun et al. (2021)](https://arxiv.org/abs/2104.02710), the paper describing the
CalMS21 dataset ([doi:10.22002/D1.1991](https://doi.org/10.22002/D1.1991)), on
[DANDI:001878](https://dandiarchive.org/dandiset/001878/draft) and on the full dataset on CaltechDATA.
The dandiset has no published version; the entry reads the draft and stops if an asset it uses has
changed. For CalMS21 it holds one sequence, the Task 1 test sequence mouse071, with its video.

| Claim | Data | Outcome |
|---|---|---|
| Keypoint format, 30 Hz, 1024 x 570, with confidence scores | dandiset | Partially reproduced (no confidence values) |
| The resident is the black mouse | dandiset | Reproduced |
| Task 1 vocabulary, one annotator, one label per frame | dandiset | Reproduced |
| Task 1 video at 30 Hz and 1024 x 570 | dandiset | Reproduced |
| Investigation and mount happen in close contact | dandiset | Reproduced |
| Pose errors are most common in close contact or fast movement (body-length proxy) | dandiset | Partially reproduced |
| The dandiset's sequence is CalMS21 mouse071 | with inputs | Reproduced |
| Pose errors in close contact or fast movement (MARS confidence) | with inputs | Partially reproduced |
| Table 5, Task 1 counts | elsewhere | Reproduced |
| Table 5, Task 2 counts | elsewhere | Partially reproduced |
| Table 5, Task 3 counts | elsewhere | Reproduced |
| Table 6, Task 1 label fractions | elsewhere | Partially reproduced |
| Figure 4B, Task 2 label fractions | elsewhere | Reproduced |
| Table 7, Task 3 label fractions | elsewhere | Reproduced |
| Size of the unlabeled set and of the dataset | elsewhere | Reproduced |
| Task 3 performance depends on frequency and bout length | elsewhere | Partially reproduced |
| Model benchmarks (Tables 1 to 4, Figures 7 and 11; six claims) | elsewhere | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001878-sun-2021-01.yaml`](../../attempts/001878-sun-2021-01.yaml).

- `reproduce_sun_2021.ipynb`: the analysis. It takes about four and a half minutes, most of it streaming the
  video and the CaltechDATA zips.
- `calms21.py`: loading the dandiset's CalMS21 file and video, and streaming sequences from the
  CaltechDATA zips with range requests. Other notebooks on this dandiset can import it.
