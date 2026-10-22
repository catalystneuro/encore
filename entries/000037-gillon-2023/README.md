# Gillon, Lecoq et al. (2023) from dandiset 000037

Tests the data descriptor of [Gillon, Lecoq et al. (2023)](https://doi.org/10.1038/s41597-023-02214-y)
on [DANDI:000037](https://dandiarchive.org/dandiset/000037/0.230426.0054), the version the paper
cites. The dandiset holds two-photon imaging of L2/3 and L5 pyramidal cell somata and distal
apical dendrites in 13 mice over 50 sessions, with running, pupil and stimulus tables, each
session in three files.

| Claim | Outcome |
|---|---|
| Subjects, cohorts, sex split and session count (four claims) | Reproduced |
| Session attributes of Table 2 | Not reproduced |
| Two animals had sessions that failed QC | Blocked: metadata insufficient |
| Session schedule, imaging depths, acquisition rates | Reproduced |
| ROI noise rejection, ROI count ranges | Reproduced |
| Tracked ROI totals and tracking across sessions | Reproduced |
| Fig. 8 example matches and conflicts (four claims) | Reproduced |
| Somata less order dependent than dendrites in matching | Blocked: data missing |
| Gabor sequence structure | Partially reproduced |
| Visual flow structure, stimulus durations, inconsistent fractions and blocks | Reproduced |
| Fig. 5 example responses, consistent against inconsistent | Blocked: methods underspecified |
| Running and pupil in all 11 mice (Fig. 6) | Reproduced |
| SNR above 1 (Fig. 7a), and its link to the paper's source data | Reproduced |
| SNR and signal stable over days (Fig. 7a, b) | Blocked: methods underspecified |
| Correlations similar, high-correlation fraction (Fig. 7c) | Blocked: methods underspecified |
| Onset and offset transients (Fig. 9) | Reproduced |
| File sizes, 33-file download | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The claim not reproduced rests on differences between the files and the paper's tables. The
session start times carry a Pacific offset on what the authors' own table gives as UTC clock
values, which moves four session dates by a day. Mouse 433414 is recorded at 60 um where Table 2
says 75; that depth is within the 50 to 75 um range the Methods give, so the imaging-depths claim
is reproduced. The files hold no QC result, so the paper's 33 analysed sessions are selected with its
Supplementary Table 1. Several Fig. 5 and Fig. 7 claims ran, but their criteria give different
outcomes under different readings, and are blocked. For Fig. 5 a reader answered that the paper
does not say which Gabor panel the rule uses, and the three readings still disagree. Two claims
are blocked only because they depend on a blocked claim: their own tests give partially
reproduced (Fig. 5, consistent against inconsistent) and not reproduced (the Fig. 7c fraction of
highly correlated pairs), and the verifier would give those outcomes. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/000037-gillon-2023-01.yaml`](../../attempts/000037-gillon-2023-01.yaml).

- `reproduce_gillon_2023.ipynb`: the analysis. It streams the 50 basic files (25 GB) once each
  and takes about seven minutes.
- `openscope_ca.py`: streaming the files, the trial tables, and the measures of the paper's code
  (SNR, smoothing, robust scaling, the Fig. 5 selection). Other notebooks on this dandiset can
  import it.
