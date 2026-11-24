# Senzai and Buzsaki (2017) from dandiset 000003

Tests the findings of [Senzai and Buzsaki (2017)](https://doi.org/10.1016/j.neuron.2016.12.011) that can be
tested on [DANDI:000003](https://dandiarchive.org/dandiset/000003/0.261122.2143), version 0.261122.2143:
silicon probe recordings from the dentate gyrus and CA3 of 15 of the paper's mice (a sixteenth mouse in
the dandiset, YutaMouse57, is not in the paper and is left out).

| Claim | Outcome |
|---|---|
| 586 GC and 500 MC | Reproduced |
| First-stage thresholds separate the labelled groups | Partially reproduced |
| Narrow-waveform interneurons fire faster than wide-waveform ones (7.97 and 2.11 Hz) | Reproduced |
| GC waveforms are narrower than MC waveforms | Reproduced |
| Green light suppresses 29 of 107 MC and no GC in DRD2-Cre::Ai35 mice | Partially reproduced |
| MC are more active than GC in wake and NREM | Reproduced |
| GC fire most in NREM, equally in wake and REM | Partially reproduced |
| CA3 pyramidal cells fire most in wake, least in REM | Not reproduced |
| GC raise their rate in NREM, MC do not | Reproduced |
| GC are more theta-modulated than MC and fire later | Reproduced |
| GC are more gamma-modulated than MC and fire earlier | Reproduced |
| Slow-firing cells couple more to gamma (r = -0.176 and -0.184) | Not reproduced |
| GC are more recruited by DS2 than MC and fire earlier | Reproduced |
| 5.5% of GC drive MC; no MC drives a GC | Partially reproduced |
| GC to MC transmission rises from the first to the second burst spike | Reproduced |
| GC to MC transmission is lower in NREM than in wake | Not reproduced |
| Zero-lag synchrony in 23% of MC, 9% of CA3, under 0.2% of GC pairs | Partially reproduced |
| More units active in the T-maze central arm, for each type | Partially reproduced (rests on an assumption) |
| Two or more T-maze fields in 6.6% of GC, 57.8% of MC, 36.1% of CA3 | Partially reproduced (rests on an assumption) |
| GC have the lowest field peak rate and spatial information | Reproduced (rests on an assumption) |
| Splitter fractions are comparable across types | Reproduced (rests on an assumption) |
| Remapping index above zero in each type | Reproduced |
| GC remap less than MC | Not reproduced |
| 36.7% of GC, 61.3% of MC and 55.6% of CA3 place cells remap | Partially reproduced |
| Population-vector remapping is smallest for GC | Reproduced (seed sensitive) |
| MC rarely inherit T-maze fields from single GC | Reproduced (rests on an assumption) |
| GC and MC maps are not correlated within the GC field | Reproduced |
| MC lie deeper than GC relative to the DS2 reversal | Reproduced |
| K-means on the four features separates GC and MC | Reproduced |
| GC sit 59 um above their MC partners; GC spikes back-propagate | Blocked: methods underspecified, as the claims file gives no criterion (two claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/senzai-2017-02.yaml`](../../attempts/senzai-2017-02.yaml).

- `reproduce_senzai_2017.ipynb`: the analysis. It streams all 101 files, four at a time, and takes
  about half an hour, most of it reading the files.
- `senzai.py`: loading, and the per-unit and per-pair measures (rates by state, burst index,
  waveforms, DS2 amplitude and histograms, theta and gamma phase, optogenetic suppression,
  cross-correlogram tests, T-maze and open-field maps, with variants on the T-maze run). Other notebooks on this dandiset can import it.
