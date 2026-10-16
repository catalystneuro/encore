# Senzai and Buzsaki (2017) from dandiset 000003

Tests the findings of [Senzai and Buzsaki (2017)](https://doi.org/10.1016/j.neuron.2016.12.011) on
[DANDI:000003](https://dandiarchive.org/dandiset/000003/0.260218.2052), which holds silicon probe
recordings of the dentate gyrus and CA3 in 16 mice over 101 recording days, with each unit labelled
as a granule cell, mossy cell, CA3 pyramidal cell or interneuron.

| Claim | Outcome |
|---|---|
| Unit counts (586 GC, 500 MC) | Partially reproduced |
| First-stage labels follow latency and burst criteria | Partially reproduced |
| Narrow interneurons faster than wide ones (7.97 and 2.11 Hz) | Partially reproduced |
| GC waveforms narrower than MC | Reproduced |
| Light suppresses 29 of 107 MC and no GC in DRD2 mice | Partially reproduced |
| MC more active than GC in wake and NREM | Reproduced |
| GC fire most in NREM, similarly in wake and REM | Partially reproduced |
| CA3 most active in wake, least in REM | Not reproduced |
| GC raise their rate in NREM, MC do not | Reproduced |
| GC more theta-modulated, at later phases | Reproduced |
| GC more gamma-modulated, at earlier phases | Reproduced |
| Slow cells more gamma-coupled (r = -0.176, -0.184) | Partially reproduced |
| GC recruited more and earlier by DS2 | Reproduced |
| 5.5% of GC excite MC, no MC excites GC | Partially reproduced |
| Transmission rises from first to second burst spike | Reproduced |
| GC to MC transmission lower in NREM | Not reproduced |
| Synchrony in 23% of MC, 9% of CA3, under 0.2% of GC pairs | Partially reproduced |
| More active cells in the central arm | Partially reproduced |
| Two or more T-maze fields: 6.6% GC, 57.8% MC, 36.1% CA3 | Partially reproduced |
| GC lowest peak rate and spatial information | Reproduced |
| Splitter fractions comparable | Reproduced |
| Remapping index above zero in each type | Reproduced |
| GC remap less than MC | Not reproduced |
| Remapping fractions 36.7%, 61.3%, 55.6% | Partially reproduced |
| GC smallest population-vector remapping | Reproduced |
| Few GC fields overlap partner MC fields (T-maze) | Reproduced |
| GC and MC maps uncorrelated within GC fields (open field) | Reproduced |
| MC deeper than GC (17 files) | Reproduced |
| K-means on the paper's features separates GC and MC (17 files) | Reproduced |
| GC 59 um above their MC partners; GC backpropagation | Blocked: no site coordinates |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000003-senzai-2017-01.yaml`](../../attempts/000003-senzai-2017-01.yaml).

- `reproduce_senzai_2017.ipynb`: the analysis. It takes about 8 minutes, most of it streaming the
  spike times, waveforms and LFP from the 101 files.
- `dg.py`: loading the files (with the repair of the unit boundaries cut at multiples of 65,536
  spikes), and the measures: rates by state, burst index, waveform latency, phase locking, DS2 and
  light responses, cross-correlograms, and T-maze and open-field rate maps. Other notebooks on this
  dandiset can import it.
