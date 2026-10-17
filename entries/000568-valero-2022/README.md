# Valero, Zutshi, Yoon & Buzsaki (2022) from dandiset 000568

Tests the findings of [Valero et al. (2022)](https://doi.org/10.1126/science.abm1891) that can be
tested on [DANDI:000568](https://dandiarchive.org/dandiset/000568/0.230705.1633). The dandiset holds
28 sessions of CA1 units recorded with uLED probes in four mice. Light pulse times and laps are in
two of these sessions only, so most claims rest on those two sessions of one mouse. Even there the
files hold only about a third of the pulses, so control time is limited to the windows the stated
protocol keeps dark.

| Claim | Outcome |
|---|---|
| Four mice, 822 pyramidal neurons, 43.3 per session | Partially reproduced |
| 20 ms pulses, 20 to 40 ms offsets, each site every 0.3 to 0.6 s | Partially reproduced |
| 611 of 822 pyramidal neurons respond to light | Reproduced |
| Light responses decrease during sharp-wave ripples | Reproduced |
| Ripple rate change correlates negatively with baseline rate (rho -0.19) | Partially reproduced |
| Light gain is largest at the theta trough | Not reproduced |
| Place cells are as common among responsive as non-responsive cells | Partially reproduced |
| Light gain is higher inside than outside the place field | Reproduced |
| In-field gain correlates with out-of-field and home-cage rates | Not reproduced |
| Place cells respond more to light in the home cage | Not reproduced |
| Light unmasks place fields in 69% of non-place cells | Not reproduced |
| Light-induced fields sit where the control spikes are | Partially reproduced |
| Light fields are more stable than control fields | Not reproduced |
| Spatial information, control against light | Partially reproduced |
| Ripple cofiring tracks spatial overlap for place cell pairs | Reproduced |
| With light, the relation appears for pairs with non-place cells | Not reproduced |
| Light intensity effects (Figures 1J, 2F, 3D) | Blocked: data missing |
| Intracellular recordings (Figure 1K to M) | Blocked: data missing |
| Excitatory against inhibitory cells during ripples | Blocked: metadata insufficient |
| Position decoding, assemblies, replay | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's Materials and Methods are in its supplement, which this attempt could not obtain. The
light-response test comes from the first author's later code, the place fields from a port of
buzcode's bz_findPlaceFields1D, and other measures are common choices. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000568-valero-2022-01.yaml`](../../attempts/000568-valero-2022-01.yaml).

- `reproduce_valero_2022.ipynb`: the analysis. It takes about seven minutes, most of it streaming
  the files.
- `valero.py`: loading the files, pulse and control windows, the light-response test, rate maps,
  place fields and theta phase. Other notebooks on this dandiset can import it.
