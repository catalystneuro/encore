# Hristova, Fasol et al. (2025) from dandiset 001888

Tests the findings of [Hristova, Fasol et al. (2025)](https://doi.org/10.1111/epi.18606) that can
be tested on [DANDI:001888](https://dandiarchive.org/dandiset/001888/draft) (draft as modified on
2026-07-31; there is no published version). The dandiset holds 73 to 99 h wireless EEG and EMG
recordings, each with two 24-h baseline windows, and the automated sleep scores and SWD events of
those windows, for 14 Grin2b+/- rats, 2 wild type rats and one rat without genotype. The paper analysed 15 Grin2b+/- and 9 wild type rats, so every genotype
comparison here rests on two wild type rats; each is also shown without the Grin2b+/- rat with
almost no SWDs (GRIN2B-228) and without the wild type rat with none (GRIN2B-238).

| Claim | Outcome |
|---|---|
| More SWDs per hour, number and total time in Grin2b+/- (Fig. 2B, 2C) | Reproduced |
| Longer SWDs in Grin2b+/- (Fig. 2C) | Partially reproduced |
| Grin2b+/- spend 59.97 min a day in SWDs, WT under 1 min | Partially reproduced |
| No light-dark or sex effect on SWDs (Fig. S5A, S8) | Reproduced |
| SWD spectrum peaks in theta with a harmonic (Fig. 2D) | Reproduced |
| Less REM per hour, less REM, fewer REM bouts (Fig. 3D, 3G) | Reproduced |
| Longer REM bouts; fewer, longer NREM bouts; less wake; more, shorter wake bouts (Fig. 3G-I) | Partially reproduced |
| No NREM time difference; no REM spectral difference (Fig. 3H, 4A) | Reproduced |
| Higher NREM beta and lower wake power in Grin2b+/- (Fig. 4B, 4C) | Not reproduced |
| SWDs mostly in wake (94.8%, 4.4%, 0.5%); all Grin2b+/- have transitional SWDs (Fig. 5A, 5C) | Partially reproduced |
| 24.2% of SWDs at wake-NREM transitions (Fig. S5B) | Reproduced |
| SWD time correlates with wake time only (Fig. 5D-F) | Reproduced (wake), partially (others) |
| SWD delta power and state share by genotype (Fig. 2E, 5A) | Blocked: data missing (one WT rat with SWDs) |
| Western blots, development, scorer validation, pharmacology (Figs. 1, 6, 7, S1, S4) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001888-hristova-2025-01.yaml`](../../attempts/001888-hristova-2025-01.yaml).

- `reproduce_hristova_2025.ipynb`: the analysis. It takes about four minutes, most of it streaming
  the processed tables of the 17 files and about 4.8 h of raw EEG per rat.
- `grin2b.py`: loading the files, the per-day sleep and SWD measures (with SWD epochs or only SWD
  time removed, and bouts split or not by SWD epochs), raw-EEG spectra following the Methods on
  either S1 channel, and the split-plot ANOVA used for the paper's mixed models. Other notebooks on this
  dandiset can import it.
