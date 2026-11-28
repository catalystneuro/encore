# Chan et al. (2024) from Dryad vt4b8gtzk

Tests the findings of [Chan et al. (2024)](https://doi.org/10.1126/science.adi0858) on
[Dryad doi:10.5061/dryad.vt4b8gtzk](https://doi.org/10.5061/dryad.vt4b8gtzk), version 289757,
which holds the field atmospheric logs, the flowtube CIMS and Vocus traces, the EAG and
dose-response data, the oxidation products of Fig. S6 and the field visitation table (Table S10).
The fruit-set counts, the Fig. 3B wind tunnel counts, the raw Vocus traces and the GEOS-Chem output
are not in it; they are read from the paper's code release on Zenodo,
[doi:10.5281/zenodo.8411927](https://doi.org/10.5281/zenodo.8411927). The bottom-level wind the
recognition distances need is read from GEOS-Chem's processed MERRA-2 files for July and January
2013, and the city coordinates from the UN World Urbanization Prospects 2018.

| Claim | Outcome |
|---|---|
| Fruit set under pollinator exclusion (Fig. 1E, three claims) | Reproduced |
| Night pollinators account for about 40% of fruit set | Reproduced |
| NO3 degrades b-pinene and ocimene by 84% and 67%, O3 by about 30% | Reproduced |
| Other compounds are unchanged by either oxidant | Reproduced |
| In the whole blend, monoterpenes drop and aldoxime and eucalyptol do not change | Partially reproduced |
| NO3 yields organic nitrates, O3 only C10H16O4 and C10H18O4 | Partially reproduced (assumed) |
| NO3 eliminates Hyles feeding in the wind tunnel | Partially reproduced |
| NO3 halves Manduca feeding; the NO3-proxy mixture lowers feeding as NO3 does | Reproduced (assumed) |
| O3 and NO2 do not change Manduca feeding | Reproduced |
| Manduca is more sensitive than Hyles; 1/100 floral equivalent dose | Reproduced |
| Field visits: NO3 odor fewer visits, real and synthetic odor alike, visits per night | Reproduced |
| Typical NO3 and O3 levels and floral reactivity (Fig. S8) | Partially reproduced |
| Field conditions of Table S1 | Partially reproduced |
| Pollinator assemblage, GC-EAD, emission rates, dose dependence | Blocked: data missing |
| NO3 shortens recognition distances, below 400 m in many populated areas (Fig. 4A, B) | Partially reproduced (assumed) |
| Recognition distances around cities (Table S13) | Not reproduced (assumed) |
| 75% or more decrease since preindustrial times, small change in Greenland (Fig. 4C) | Not reproduced (assumed) |
| Urban regressions (Fig. S9), on the rows Table S13 prints | Reproduced |
| Interannual similarity of the model runs | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The Dryad files are staged before the run in `/tmp/dryad/vt4b8gtzk/289757/`, as Dryad needs a
token to download them, and their SHA-256 digests are checked against Dryad's public file list. The
Zenodo zip is streamed. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/chan-2024-01.yaml`](../../attempts/chan-2024-01.yaml).

- `reproduce_chan_2024.ipynb`: the analysis. It runs in about five minutes, most of it reading the
  MERRA-2 wind.
- `chan.py`: loading the Dryad and Zenodo files, R's pairwise proportion test, the paper's Table S9
  test and trace processing, the GEOS-Chem land mask, the MERRA-2 bottom-level wind and the Table S13
  city coordinates.
