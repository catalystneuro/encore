# Kaku, Liu et al. (2025) from dandiset 001619

Tests the findings of [Kaku, Liu et al. (2025)](https://doi.org/10.1101/2025.01.27.635041), "A
brainstem map of orofacial rhythms", that can be tested on
[DANDI:001619](https://dandiarchive.org/dandiset/001619/0.251027.1953). The dandiset holds the brainstem
Neuropixels recordings of 31 mice in the multi-directional licking task (335 probe insertions in 173
sessions), with DeepLabCut tracking of jaw and tongue, the 25 kHz airflow trace and CCF positions of the
units. The cued licking task with photostimulation, the rat recordings, the raw videos and the premotor
tracing data are not in it.

| Claim | Outcome |
|---|---|
| The dandiset holds the inputs of the paper's code (20,109 units pass its filter) | Reproduced |
| 20,300 units, 5,700 cerebellum, 3,700 pons, 10,900 medulla, 339 insertions | Partially reproduced (change to not reproduced proposed) |
| Spike rates of cerebellum, vestibular nuclei and medulla | Not reproduced |
| Lick and breath frequencies (Fig 1d) | Partially reproduced |
| Inspiration never coincides with licking (Fig 1f) | Not reproduced |
| Second lick delayed before a slow breath (Fig 1g) | Partially reproduced |
| Licks added as breathing slows, fixed latency (Fig 1f) | Not reproduced |
| Inspiration delayed before a slow lick (Fig 1i) | Reproduced |
| Unidirectional oscillator models fail (Extended Data Fig 1d-i) | Reproduced |
| Licking paused at swallows (Extended Data Fig 1b-c) | Not reproduced |
| Rhythms follow swallows at fixed latencies (Fig 1k, m) | Reproduced |
| Inter-lick interval preserved across a swallow (Fig 1l) | Not reproduced |
| Lick cycle with a swallow prolonged by 33.3 ms (Fig 1l) | Reproduced |
| Inter-breath interval preserved; breath cycle prolonged by 48.0 ms (Fig 1n) | Reproduced (both) |
| 3,551 licking, 1,015 breathing and 182 both-tuned units | Partially reproduced |
| Swallow-modulated unit counts | Not reproduced |
| Breathing units near preBotzinger and posterior ventral IRN (Fig 2f) | Reproduced, on an assumption (change to blocked proposed) |
| Licking units in XII, V, IRN and pons (Fig 2g) | Reproduced |
| Swallow units in V, IC, NLL, beside NTS and above AMB (Fig 2h) | Blocked: methods underspecified |
| Swallow activity leads in V and IRN, follows in IC and NLL (Extended Data Fig 6e) | Reproduced |
| preBotzinger units fire at inspiration (Extended Data Fig 8b-c) | Reproduced, on an assumption (change to blocked proposed) |
| Licking units active at full protrusion (Extended Data Fig 8e) | Reproduced |
| Licking map robust to a 500 uV amplitude filter (Extended Data Fig 4c) | Reproduced |
| Licking units anticipate the next breath (Fig 4e) | Reproduced |
| Breathing units anticipate the next lick (Fig 4f) | Reproduced, on an assumption |
| 43 simultaneous licking and breathing oscillator recordings (Fig 4d) | Blocked: data missing |
| Lick direction tuning (Extended Data Fig 8i) | Blocked: metadata insufficient |
| GLM (Extended Data Fig 7) | Blocked: too large |
| Cross-correlation of oscillator pairs (Fig 4g, h; three claims) | Blocked: data missing |
| Premotor regions and licking units inside them (Fig 3a, b) | Blocked: other (public source found, not analysed) |
| Autoencoder, rats, photostimulation, cued task (14 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's analysis code (github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe) is ported to the
streamed NWB files. The files store the offset where each unit's spikes start, not where they end, so a
standard NWB reader misassigns spikes; the helper reads them by the per-trial spike counts. Regions
the CCF does not label are built from the Allen CCFv3 annotation volume. The peak-difference measures
of Figs 1g and 4e give a positive difference under a random split of the cycles, so their positive
results carry little weight (see the notebook). The attempt
record, with the reasons, the verifier's two reports and the replies to them, the changes proposed for a third round, and the differences from the paper's method, is
[`attempts/kaku-2025-01.yaml`](../../attempts/kaku-2025-01.yaml).

- `reproduce_kaku_2025.ipynb`: the analysis. It took 50 to 71 minutes in the runs made so far, most of it
  streaming the airflow of 173 sessions and fitting tuning curves.
- `kaku.py`: loading, and the paper's code steps (movement timing, swallow detection, phase tuning,
  peak differences, swallow modulation). Other notebooks on this dandiset can import it.
