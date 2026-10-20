# Economo et al. (2018) from dandiset 000006

Tests the findings of [Economo et al. (2018)](https://doi.org/10.1038/s41586-018-0642-9) on
[DANDI:000006](https://dandiarchive.org/dandiset/000006/0.220126.1855), version 0.220126.1855, the only
published version. The claims file (`claims/000006/10.1038-s41586-018-0642-9.yaml`) was written by a
reader from the full text and checked by a second reader. This is the second attempt
(`attempts/000006-economo-2018-02.yaml`); it replaces `000006-economo-2018-01`, whose claims were
written from the abstract only. The dandiset holds silicon probe recordings from the anterior lateral
motor cortex of 12 mice in a delayed response task, with tagged PTupper (thalamus-projecting) and
PTlower (medulla-projecting) units. The claims on sequencing and axon reconstructions are tested on the
paper's Figshare record (doi:10.25378/janelia.7007846), which the claims file names as their home.

| Claims | Outcome |
|---|---|
| Data elsewhere: transcriptomic clusters, thalamus and medulla projections of the reconstructions, cluster mapping of projection types, bulk against single-cell fold changes | Reproduced |
| Data elsewhere: all PT neurons in the two types | Partially reproduced |
| Data elsewhere: shared targets (the bulk labelling part has no method of analysis), retrograde co-labelling | Blocked: methods underspecified |
| smFISH markers | Blocked: data not public |
| Unit counts (61 and 69), selective units in any epoch (122 of 130), spike rates similar | Not reproduced |
| Depth, rate heterogeneity, variance explained, PTlower early selectivity decay, coding direction stability, single-neuron early selectivity, PTlower late activity and CDgo motor command | Reproduced |
| Late delay selective counts, bursting, single-unit decoding (two claims), CDgo onsets | Partially reproduced |
| PTupper early and persistent activity, coding direction change at the go cue, movement termination, cohort control, the summary of the two types' timing | Blocked: methods underspecified |
| Reaction time | Blocked: no video |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The unit selection, epochs, smoothing, coding directions and hierarchical bootstrap follow the claims
file, which cites the Methods and the analysis code on the Figshare record. A reader answered this
attempt's questions (`questions/000006.yaml`), and the claims file now settles the unit selection
(the code's per-unit rule) and the trial range (each unit's range in the code); the outcomes are
decided under those, with the Methods' session rule and all trials shown as variants. On the
dandiset the code's rule keeps 44 PTupper and 56 PTlower units, not the paper's 61 and 69, because
11 sessions are missing from it. Where the remaining open readings give different outcomes, the
claim is blocked. The same code run on the paper's units from its processed data gives most of the
paper's numbers; those runs are variants, and no outcome rests on them. Run on the processed data for
only the 100 units the dandiset holds, the code gives the dandiset's counts and test results, so most
failures here come from the missing units; the files' clock raises every unit's baseline rate by about
1 Hz. The spike and lick times in
the files are not sorted, and consecutive trials overlap on the files' clock; the notebook shows
this and rebuilds the trials from the stored order.

- `reproduce_economo_2018.ipynb`: the analysis. It takes about twelve minutes, most of it streaming
  the files and the processed data and running the bootstraps.
- `alm.py`: loading the files, the paper's processed data and the Seq and Axons files of the Figshare
  record; the two unit selections; smoothed rates; the single-unit measures; the hierarchical
  bootstrap of the coding directions; the coding direction correlations; variance explained. Other
  notebooks on this dandiset can import it.
