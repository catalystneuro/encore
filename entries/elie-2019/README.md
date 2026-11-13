# Elie & Theunissen (2019) from CRCNS aa-4

Tests the findings of [Elie and Theunissen (2019)](https://doi.org/10.1371/journal.pcbi.1006698) on
[CRCNS aa-4](https://doi.org/10.6080/K00C4T06), the spike times of auditory units of six zebra finches
to the calls of their vocal repertoire.

| Claim | Outcome |
|---|---|
| 404 of 914 single units selected by the 2015 decoding | Blocked: methods underspecified |
| Claims on the 404 and 337 units (Poisson checks, information, time constants, CII; 19 claims) | Blocked: methods underspecified |
| Three example neurons (Figures 3 to 5) | Blocked: methods underspecified |
| Anatomy (Table 1, Figure 10; 5 claims) | Blocked: data missing |
| Model neurons of Figure 1 | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold 1281 units labelled single units, of which 1246 pass the 2015 auditory threshold, and
mark neither the 914 single auditory units nor the 404 the paper analyses. The anatomical locations
of the recording sites are not in the data set. The attempt record, with the reasons and the
differences from the paper's method, is [`attempts/elie-2019-01.yaml`](../../attempts/elie-2019-01.yaml).
