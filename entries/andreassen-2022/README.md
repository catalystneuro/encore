# Andreassen, Hall, Khatibzadeh, Jutfelt & Kermen (2022) from FIGSHARE:19640805

Tests the findings of [Andreassen et al. (2022)](https://doi.org/10.1073/pnas.2207052119) that can
be tested on [Figshare item 19640805, version 4](https://doi.org/10.6084/m9.figshare.19640805.v4),
which holds the paper's derived per-fish tables and its R script. The imaging, the experiment-2
temperatures and onsets, the experiment-4 medulla counts, the behavioural scores of Figure S1B, C
and E and the light-response amplitudes are not in it.

| Claim | Outcome |
|---|---|
| CTmax of 5 dpf larvae, 41.4 °C | Reproduced |
| CTmax similar in 5 dpf, 9 dpf and adult fish | Reproduced |
| Swim speed falls during the assay, no treatment difference | Reproduced |
| Heat-ramp larvae spend more time in loss of equilibrium | Reproduced |
| Medulla activity stable in controls, 1.6 peaks/min | Reproduced |
| Medulla activity rises to 3.6 peaks/min, then falls before the depolarization | Reproduced |
| CTmax precedes the depolarization by 0.5 °C | Reproduced |
| Heart rate rises from 28 to 34 °C, falls to 37 °C, then stays stable | Reproduced (two claims) |
| Oxygen level sets CTmax and the depolarization onset | Reproduced (two claims) |
| Oxygen does not change depolarization amplitude; hypoxia prolongs recovery | Reproduced (two claims) |
| Medulla activity drops before the depolarization in all oxygen treatments | Reproduced, on an assumption |
| Medulla activity with warming in normoxia and hyperoxia | Reproduced (two claims) |
| Medulla activity falls with warming in hypoxia (Q10 0.8 and 0.02) | Partially reproduced |
| Light responsiveness by oxygen level (Figure 6C) | Partially reproduced |
| Binomial model of light responses (Table S10) | Reproduced |
| Spiral swimming, loss of response, experiment-2 temperatures and onsets, depolarization spread and recovery, experiment-4 medulla, light-response amplitudes, depolarization magnitude (nine claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The models, outlier rule and variables follow the paper's R script, deposited in the same item;
mixed-model p-values use Satterthwaite degrees of freedom where the script's tables use
Kenward-Roger. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/andreassen-2022-01.yaml`](../../attempts/andreassen-2022-01.yaml).

- `reproduce_andreassen_2022.ipynb`: the analysis. It takes under a minute, most of it streaming
  the files.
- `thermal.py`: streaming the files with an MD5 check, the outlier rule, Q10, and REML and
  binomial mixed models with a random intercept per fish. Other notebooks on this item can import
  it.
