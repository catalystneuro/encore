# Prakash et al. (2022) from dandiset 000935 and the article's source data

Tests the findings of [Prakash et al. (2022)](https://doi.org/10.1038/s42003-021-02981-7) on
[DANDI:000935](https://dandiarchive.org/dandiset/000935/0.240319.2026), which holds the in vivo
experiment of Figure 7: laminar recordings and bioluminescence imaging in six PV-Cre mice given CTZ
over barrel cortex, three with a postsynaptic opsin and three without. The in vitro findings of
Figures 2 to 6 are tested on the per-electrode spike counts that the article publishes as
Supplementary Data 1 to 6.

| Claim | Outcome |
|---|---|
| In vitro ladder plots, Figs. 2d, 3c, 4c, 4e, 5c, 6c and Supplementary Fig. 4c (11 claims) | Reproduced |
| Fig. 6f, no response with a non-functional opsin | Blocked: the published comparison column is a copy of another panel's |
| Supplementary Figs. 2, 3, 5 and 6, recordings and images not deposited (4 claims) | Blocked: data missing |
| Fig. 7b, CTZ raises bioluminescence in both groups | Reproduced |
| Fig. 7c, gamma emerges in Opsin (+) mice | Reproduced |
| Fig. 7d, contacts exceeding baseline | Not reproduced |
| Fig. 7d, gamma increase in superficial layers | Blocked: metadata insufficient |
| Fig. 7e, gamma power and events across electrodes, gamma power across mice | Partially reproduced |
| Fig. 7e, gamma events across mice | Blocked: methods underspecified |
| Fig. 7f, MUA across electrodes | Not reproduced |
| Fig. 7f, MUA across mice | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/prakash-2022-01.yaml`](../../attempts/prakash-2022-01.yaml).

- `reproduce_prakash_2022.ipynb`: the analysis. It streams the 40 GB of recordings from the archive three times,
  and takes about 40 minutes.
- `interlum.py`: streaming the files by byte range, the bioluminescence onset, the errant-contact
  rule, the multitaper gamma power, gamma events and MUA of the paper's Methods, and reading the
  article's Supplementary Data. Other notebooks on this dandiset can import it.
