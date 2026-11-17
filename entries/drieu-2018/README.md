# Drieu, Todorova & Zugaro (2018) from CRCNS hc-18

Tests the findings of [Drieu et al. (2018)](https://doi.org/10.1126/science.aat2952) on
[CRCNS hc-18](https://doi.org/10.6080/K0Z899MM), which holds the CA1 spikes, LFP and head positions
of the paper's five rats, each recorded on one day of passive, active and passive travel on a model
train, with sleep before and after each travel. The five archives are streamed from the
CRCNS bucket and reduced in memory by `drieu2018.py`.

| Claims | Outcome |
|---|---|
| Peak rates lower in Passive 1; fields cover the track; theta frequency unchanged; theta power (per-window reading) and asymmetry reduced in passive travel; precession range alike | Reproduced |
| Theta scores above chance; per-rat reconstructions; steeper Active theta slopes; quadrant scores highest in Active; joint score-slope excess in Active, for theta sequences and for replay; forward replay after Active | Reproduced |
| Place-cell counts (assumed field limits); no remapping between conditions (three claims); burst and precession proportions; precession slopes degraded | Partially reproduced |
| Average theta reconstruction; proportion of significant theta sequences; decoding-quality, cell-count, firing-rate and lap-by-lap controls; replay scores relative to baseline | Partially reproduced |
| Travel alike across conditions; field size alike; burst frequency; sleep sessions alike; steeper replay slopes after Active; replay proportions relative to baseline; ripple-restricted replay; bias correlations (fig. 3G, 4G) | Not reproduced |

After the second round of verification, changes of outcome are proposed for a third round: the cell-count,
firing-rate and lap-by-lap controls to not reproduced, and no remapping between Passive 1 and Active to
reproduced under the adopted field limits. The table gives the verified outcomes.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set includes the paper's MATLAB scripts (`code.zip`), but not the channel lists, theta-cycle
files and place-cell lists they load, so these were rebuilt from the data. The place cells found
here outnumber the paper's. A third notebook, added after the first round of verification, runs the
decoding controls, the pairwise bias correlations on samples of pairs, and the decoding under other readings. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/drieu-2018-01.yaml`](../../attempts/drieu-2018-01.yaml).
