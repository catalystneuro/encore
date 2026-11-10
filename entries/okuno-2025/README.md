# Okuno, Woodward, Okano & Hata (2025) from dandiset 000727

Tests the findings of [Okuno et al. (2025)](https://doi.org/10.7554/elife.107990.1) on
[DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), the whole-brain two-photon
imaging of nine walking flies (Brezovec et al.) that the paper reuses. The FC computed here from the
raw imaging is compared with the paper's published FlyEM and FlyWire SC matrices (its code at
commit 4b92add and Zenodo record 15532272).

| Claim | Outcome |
|---|---|
| FlyEM gives a higher FC-SC correlation than FlyWire (0.73 against 0.68) | Partially reproduced |
| FlyEM is higher in 58 of 63 regions | Reproduced |
| Regional FC-SC correlation rises with cholinergic and falls with GABAergic output share | Not reproduced |
| Unsegregated synapses give a higher FC-SC correlation than random samples | Reproduced |
| Segregated synapses give a lower FC-SC correlation than random samples | Reproduced |
| Reciprocal synapses give a higher FC-SC correlation than random samples | Reproduced |
| LAL, FB, IPS and GNG are active during walking | Reproduced |
| WED and AVLP are inactive or suppressed during walking | Not reproduced |
| Connectome counts per region and transmitter shares (four claims, data elsewhere) | Three reproduced, one partially |
| Smoothing, nuisance removal and ROI-count analyses on SCKm and DistKm ROIs (nine claims) | Blocked: atlases not published |
| FlyEM confidence thresholds, FlyEM permutation tests | Blocked: SC not published |
| PPSSI distribution over FlyWire neurons | Partially reproduced |
| Other connectome-only claims (six) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/okuno-2025-01.yaml`](../../attempts/okuno-2025-01.yaml).
