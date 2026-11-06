# Rodgers & DeWeese (2014) from CRCNS pfc-1

Tests the findings of [Rodgers and DeWeese (2014)](https://doi.org/10.1016/j.neuron.2014.04.031) on
CRCNS data set [pfc-1](https://doi.org/10.6080/K0W66HPJ), which holds the spike times and trial
tables of 55 sessions of six rats performing an auditory stimulus selection task, with units in
medial prefrontal cortex and primary auditory cortex, and the data of the paper's mPFC disruption,
catch-trial, video-tracking and network-model analyses.

| Claim | Outcome |
|---|---|
| The code's unit and session tables match the data set (link) | Reproduced |
| Behaviour: above chance, go better than nogo, block switching, intertrial interval | Reproduced (4) |
| Hold-period rule encoding in mPFC and A1, its size, independence of auditory responsiveness | Reproduced (4) |
| Example mPFC units (Figure 3A, 3B) | Reproduced |
| Example A1 units (Figure 4A, 4B) | Reproduced, with the units identified by preference as the legends describe them (the code's figure index swaps them) |
| Error trials, trial types, spontaneous rate, reaction and movement time | Reproduced (5) |
| Time course of rule encoding (Figure 5) | Reproduced (3) |
| Evoked responses, baseline and evoked change, decoding, tuning, stimulus pairs | Reproduced (8) |
| Head angle and posture equalization | Reproduced (4) |
| mPFC disruption and catch trials | Reproduced (3) |
| Network model (Figure 8) | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The units the paper analysed, their region and their auditory response windows are not in the data
set; they come from `metadata/unit_db.csv` of the paper's code
([cxrodgers/Rodgers2014](https://github.com/cxrodgers/Rodgers2014) at commit 390b608). The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-pfc-1-rodgers-2014-01.yaml`](../../attempts/crcns-pfc-1-rodgers-2014-01.yaml).

- `reproduce_rodgers_2014.ipynb`: the analysis. It takes about two to three minutes, streaming the
  zip from the CRCNS bucket.
- `pfc1.py`: streaming the zip, reading its Python 2 pandas pickles, the code's tables, and the
  measures of the paper's code (hold counts, R-equivalent tests, the code's Gaussian smoother, the
  stimulus-equalized bootstrap, the onset-window recomputation). Other notebooks on this data set
  can import it.
