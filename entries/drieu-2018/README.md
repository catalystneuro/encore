# Drieu, Todorova & Zugaro (2018) from CRCNS hc-18

Tests the findings of [Drieu et al. (2018)](https://doi.org/10.1126/science.aat2952) on
[CRCNS hc-18](https://doi.org/10.6080/K0Z899MM), which holds the CA1 spikes, LFP and head positions
of the paper's five rats, each recorded on one day of passive, active and passive travel on a model
train, with sleep before and after each travel. The five archives (47 GB) are streamed from the
CRCNS bucket and reduced in memory by `drieu2018.py`.

| Claims | Outcome |
|---|---|
| Peak rates lower in Passive 1; fields cover the track; field size alike (assumed field-size rule); theta frequency unchanged; theta asymmetry reduced in passive travel | Reproduced |
| Theta scores above chance; quadrant scores highest in Active; joint score-slope excess in Active, for theta sequences and for replay | Reproduced |
| No remapping between conditions (three claims); theta power lower in passive travel; precession slopes degraded | Partially reproduced |
| Average and per-rat theta reconstructions; steeper Active theta slopes; decoding-quality control; steeper replay slopes after Active; forward replay after Active | Partially reproduced |
| Travel alike across conditions; place-cell counts; burst frequency and proportions; precession range alike; sleep sessions alike | Not reproduced |
| Proportion of significant theta sequences; replay scores and proportions relative to baseline; ripple-restricted replay | Not reproduced |
| Bias correlations (fig. 3G, 4G); cell-count, firing-rate and lap-by-lap controls (figs. S7, S8, S10) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set includes the paper's MATLAB scripts (`code.zip`), but not the channel lists, theta-cycle
files and place-cell lists they load, so these were rebuilt from the data. The place cells found
here outnumber the paper's. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/drieu-2018-01.yaml`](../../attempts/drieu-2018-01.yaml).
