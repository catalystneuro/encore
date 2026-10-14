# Economo et al. (2018) from dandiset 000006

Tests the findings in the abstract of [Economo et al. (2018)](https://doi.org/10.1038/s41586-018-0642-9)
that [DANDI:000006](https://dandiarchive.org/dandiset/000006/0.220126.1855) can test. The paper is not
open access, so only its abstract was used. The dandiset holds silicon probe recordings from the
anterior lateral motor cortex of 12 mice in a delayed response task, with tagged PTupper (thalamus-projecting)
and PTlower (medulla-projecting) units.

| Claim | Outcome |
|---|---|
| PT neurons carry preparatory activity | Reproduced |
| Thalamus-projecting PT neurons carry early preparatory activity | Reproduced |
| Their preparatory activity persists until the movement | Reproduced |
| Medulla-projecting PT neurons mainly carry late preparatory activity and motor commands | Partially reproduced |
| The two types differ in timing (early against late and motor) | Not reproduced |
| Transcriptomic types, projection targets (four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The epochs, trial and unit selection and the selectivity test follow the analysis code on the
paper's Figshare record (doi:10.25378/janelia.7007846). The spike times in the files are not sorted,
and consecutive trials overlap on the files' clock; the notebook shows this and checks that it does
not change the outcomes. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000006-economo-2018-01.yaml`](../../attempts/000006-economo-2018-01.yaml).

- `reproduce_economo_2018.ipynb`: the analysis. It takes about a minute, half of it streaming the files.
- `alm.py`: loading the files, the code's unit inclusion rule, epoch rates, the selectivity test and
  its label-shuffle null. Other notebooks on this dandiset can import it.
