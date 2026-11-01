# Kalugin et al. (2026) from dandiset 001074

Tests the findings of [Kalugin et al. (2026)](https://doi.org/10.1016/j.neuron.2026.07.008) that can
be tested on [DANDI:001074](https://dandiarchive.org/dandiset/001074/0.260928.0807). The dandiset
holds the CaImAn traces and 3D masks of the paper's MORSE recordings (dipping, slice and in vivo),
with no sensor labels and no well, wash-on, injection or stimulation times.

| Claim | Outcome |
|---|---|
| The code's well order fits the revision probes' recordings (link) | Reproduced |
| 100 to 200 cells per gel, through its thickness | Reproduced |
| Sensor yield of the ten ten-sensor probes | Partially reproduced |
| All ten sensors respond in their own wells | Not reproduced as the criterion is written (responses carry over between wells; asked of a reader) |
| Only DA/NE, and less so AVP/OXT, show crosstalk | Not reproduced |
| On-target and off-target EC50s of Table 1 | Not reproduced |
| Peak dF/F0 of Table 1 | Not reproduced |
| EC50s consistent across probes | Not reproduced |
| tau-on under 1 minute for almost all sensors | Reproduced |
| tau-on rises with depth for all sensors but ATP | Not reproduced |
| 70 to 130 cells tracked per probe across recordings | Reproduced |
| Hydrogel deformation and stability, photometry, ELISA, choroid plexus, histology (13 claims) | Blocked: data missing |
| Slice and in vivo CSF claims (22 claims) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files carry no sensor labels and no well timing. The well order and mixture concentrations of
the ten revision probes come from the paper's code (github.com/pkalugin/kalugin-et-al-morse at
commit fa4526a), and the labels are made from the traces by the Methods' clustering, without the
code's hand corrections. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001074-kalugin-2026-01.yaml`](../../attempts/001074-kalugin-2026-01.yaml).

- `reproduce_kalugin_2026.ipynb`: the analysis. It takes about eighteen minutes, most of it the
  survey of the 713 files.
- `morse.py`: loading (traces, and masks reordered from their scrambled storage), the well timing
  and order, dF/F0, the dipping artefact and background corrections, the sensor clustering, and
  the dose-response and tau-on fits. Other notebooks on this dandiset can import it.
