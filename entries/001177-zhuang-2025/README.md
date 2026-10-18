# Zhuang, Lemak, Sridhar & Nelson (2025) from dandiset 001177

Tests the findings of [Zhuang et al. (2025)](https://doi.org/10.1093/brain/awaf312) that can be tested
on [DANDI:001177](https://dandiarchive.org/dandiset/001177/0.250902.2127), which holds open-field
recordings from the dorsomedial striatum of 18 mice given pramipexole (PPX) or saline, and on the
behavioural, rotarod and histology data the paper deposited on
[Zenodo](https://doi.org/10.5281/zenodo.15258978).

The dandiset holds raw voltage and unsorted threshold crossings, but no sorted units with cell types,
no optogenetic labels and no injection times, so the paper's unit-level claims are blocked. Three
claims test the same effects on the multi-unit activity of each channel.

| Claim | Data | Outcome |
|---|---|---|
| Unit-level claims of Figures 4, 6F-I and S5 (seven claims) | dandiset | Blocked: data missing |
| Multi-unit response types, parkinsonian against control | dandiset | Partially reproduced |
| Multi-unit response to saline | dandiset | Blocked: other |
| Multi-unit response types, first against fourth session | dandiset | Partially reproduced |
| TH depletion in DLS and DMS, less in VS (Fig. 1B) | Zenodo | Reproduced |
| Rotarod deficit improved by PPX (Fig. 1C) | Zenodo | Reproduced |
| Similar baseline discounting (Fig. 1F, G) | Zenodo | Reproduced |
| PPX does not change discounting in controls (Fig. 1F) | Zenodo | Reproduced |
| PPX makes parkinsonian mice impulsive (Fig. 1G) | Zenodo | Reproduced |
| PPX lowers A and AUC, raises K (Fig. 1I-K) | Zenodo | Partially reproduced |
| Washout (Fig. S2I-K) | Zenodo | Partially reproduced |
| A77636 in controls and parkinsonian mice (Fig. 2D, E) | Zenodo | Reproduced (two claims) |
| A77636 raises K, lowers AUC, not A (Fig. 2F-H) | Zenodo | Reproduced |
| A77636 locomotion (Fig. 2B, C) | Zenodo | Blocked: metadata insufficient |
| A correlates with DMS TH (Fig. 3A) | Zenodo | Not reproduced |
| K does not correlate with TH (Fig. 3B) | Zenodo | Reproduced |
| CNO in mCherry mice (Fig. 5G) | Zenodo | Reproduced |
| hM4Di and hM3Dq make mice impulsive (Fig. 5H, I) | Zenodo | Partially reproduced |
| DREADD effects on A, K and AUC (Fig. 5J-L) | Zenodo | Partially reproduced |
| DREADD locomotion (Fig. 5C-F) | Zenodo | Blocked: metadata insufficient |
| PPX effect grows from first to fourth session (Fig. 6B, C) | Zenodo | Not reproduced |
| A77636 effect does not grow (Fig. 6D, E) | Zenodo | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001177-zhuang-2025-01.yaml`](../../attempts/001177-zhuang-2025-01.yaml).

- `reproduce_zhuang_2025.ipynb`: the analysis. It takes about five minutes, most of it streaming
  the threshold crossings (6.5 GB of timestamps, read as byte ranges).
- `icd.py`: loading the NWB files and the Zenodo deposit, the paper's response-type rule, the
  inferred injection time, and the delay-discounting measures and tests. Other notebooks on this
  dandiset can import it.
