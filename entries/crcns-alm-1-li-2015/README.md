# Li, Chen, Guo, Gerfen & Svoboda (2015) from CRCNS alm-1

Tests the findings of [Li et al. (2015)](https://doi.org/10.1038/nature14178) that can be tested
on CRCNS data set [alm-1](https://doi.org/10.6080/K0RF5RZT), which holds the extracellular
recordings of Figures 2 and 3: 1,408 units from left ALM of 19 mice over 99 sessions, with
pyramidal, FS, PT and IT labels, trial types, epoch times, and the lick and photostimulation
traces. The photoinhibition and photoactivation behaviour, the calcium imaging and the anatomy
are not in it.

| Claim | Outcome |
|---|---|
| Mean performance 78.4% correct, fewer than 13% early responses | Reproduced (19 of 42 mice) |
| 1,408 units; 1,245 pyramidal, 124 FS, 39 intermediate by spike width | Partially reproduced |
| 73% (912/1,245) of pyramidal neurons are selective | Reproduced |
| 219 preparatory, 389 and 304 peri-movement categories | Reproduced (figure's reading) |
| Selectivity emerges in the sample epoch, grows, peaks after the cue | Reproduced |
| Dynamic single neurons, stable population selectivity | Reproduced |
| Activity on error trials follows the lick | Reproduced |
| Equal numbers of contra- and ipsi-preferring neurons | Reproduced |
| No contralateral bias in the population spike count | Reproduced |
| FS neurons fire more at baseline and are less selective | Partially reproduced |
| 45 PT and 27 IT neurons passed the collision test | Reproduced |
| Antidromic latency and jitter of PT and IT neurons | Partially reproduced (assumed window) |
| IT neurons have less jitter on the second pulse | Reproduced |
| PT and IT neurons both preparatory and movement-related | Reproduced |
| Contra-preferring neurons outnumber ipsi among PT, not IT | Reproduced (selective neurons) |
| Late contralateral selectivity in PT neurons, from 570 ms before the cue | Not reproduced |
| Reaction time 61.1 ± 10.5 ms | Blocked: methods underspecified |
| Large differences in contra-preferring neurons, contra-suppression in ipsi-preferring | Partially reproduced |
| Photoinhibition, photoactivation, imaging and anatomy (eleven claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set's own labels and trial tables reproduce the paper's counts of selective neurons,
response categories and contra and ipsi preference exactly. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/crcns-alm-1-li-2015-01.yaml`](../../attempts/crcns-alm-1-li-2015-01.yaml).

- `reproduce_li_2015.ipynb`: the analysis. It takes about six minutes, most of it streaming
  about 14 GB of session files from the CRCNS bucket.
- `alm.py`: streaming and reducing the session files, the unit table of epoch rates and
  selectivity tests, and the antidromic latency measures. Other notebooks on this data set can
  import it.
