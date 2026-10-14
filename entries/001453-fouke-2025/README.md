# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
| Figures 2 to 4: imaging and head-fixed tail tracking (nine claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files carry no names for their stimulus codes. The names come from the paper's analysis
notebook and the protocol file of its stimulus software, so most claims use these outside inputs.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001453-fouke-2025-01.yaml`](../../attempts/001453-fouke-2025-01.yaml).

- `reproduce_fouke_2025.ipynb`: the analysis. It takes about five minutes, most of it streaming the
  files.
- `omr.py`: loading the files, the stimulus names, and the trial measures of the paper's code, with
  the angular acceleration of the Methods. Other notebooks on this dandiset can import it.
