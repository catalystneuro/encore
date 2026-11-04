# Kim, Lycke, Zolotavin, Montes, Xie & Luan (2026) from dandiset 001868

Tests the findings of [Kim et al. (2026)](https://doi.org/10.1126/sciadv.aef0343) that can be
tested on [DANDI:001868](https://dandiarchive.org/dandiset/001868/0.260715.2016), which holds
chronic electrophysiology, wheel behaviour and two-photon imaging of mouse S1 during an
intracortical microstimulation (ICMS) detection task, from six trained and six control mice.

| Claim | Outcome |
|---|---|
| Detection thresholds fall from early to late training (Fig. 2A) | Reproduced |
| The steepest fall is between weeks 0 and 1 | Reproduced |
| Response times follow the thresholds (fig. S1E) | Reproduced |
| Wheel-movement onset falls; medians 122, 135 and 129 ms (fig. S5C) | Reproduced |
| Unit counts, 973 recorded and 484 modulated (Fig. 4H) | Not reproduced |
| Modulation of all units rises at 4, 5 and 6 uA (fig. S3B) | Reproduced |
| Time to maximum falls at 5 uA only (fig. S3C) | Partially reproduced |
| Modulation at threshold is stable (fig. S3D) | Reproduced |
| More modulated units in Mouse 1 at 4 uA (Fig. 4G) | Reproduced |
| Pyramidal cells carry the increase; interneurons change little (Fig. 4, I and J) | Reproduced (both claims) |
| Over 80% of units keep PL or NPL identity across currents (Fig. 5D) | Not reproduced |
| More pyramidal cells among PL units (Fig. 5E) | Partially reproduced |
| PL latency rises with distance, 0.2 to 0.27 m/s (fig. S4B) | Partially reproduced |
| PL modulation rises; PL time to maximum falls (Fig. 5, F and G) | Reproduced |
| NPL responses do not change (fig. S4, D and E) | Reproduced |
| PL peak spike probability rises at 5 and 6 uA (Fig. 5H) | Partially reproduced |
| Results hold in a 120 ms premotion window (fig. S5) | Reproduced |
| Hit-miss KL divergence rises for PL and NPL (Fig. 6C) | Not reproduced |
| NPL hit-miss divergence from 65 and 35 ms, none for PL (Fig. 6D) | Not reproduced |
| Population coupling, PL rising, NPL above PL (Fig. 6F, fig. S9A) | Reproduced (both claims) |
| Coupling difference in the 120 ms window and absent in controls (fig. S9, B and C) | Reproduced, resting on an assumption about the control code |
| Volumetric imaging, Fig. 2B to 2G and fig. S2 (eight claims; the control counts are reported) | Blocked: metadata insufficient |
| Planar tracking, Fig. 3 and fig. S6 (nine claims) | Blocked: metadata insufficient |
| Waveform separation (Fig. 4D) and UnitMatch tracking (fig. S8) | Blocked: data missing |
| Control electrophysiology (fig. S7) | Reproduced, resting on assumptions about the control code |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The behavioural files hold no position of the stimulation site in the imaging volume and no
activation calls, and their planar ROIs carry no identity across sessions, so none of the imaging
findings can be tested. The control files use a stimulation protocol (3 bursts of 10 pulses at
50 Hz) other than the 700 ms, 100 Hz trains the paper's methods are defined on; the control claims
follow the paper's own control code. Where the paper is silent, method details come from the code
the paper links, cited in the notebook. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001868-kim-2026-01.yaml`](../../attempts/001868-kim-2026-01.yaml).
