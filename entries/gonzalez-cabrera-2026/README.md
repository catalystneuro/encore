# Gonzalez-Cabrera et al. (2026) from dandiset 001955

Tests the findings of [Gonzalez-Cabrera et al. (2026)](https://doi.org/10.64898/2026.02.17.706301)
that can be tested on [DANDI:001955](https://dandiarchive.org/dandiset/001955/0.261103.0758). The
dandiset holds fiber photometry of VTA dopamine neurons during optogenetic stimulation of VTA-PnO
neurons (5 opsin and 3 control mice, 5, 10 and 20 Hz and continuous light) and raw acute and
chronic silicon-probe recordings without sorted units.

| Claim | Outcome |
|---|---|
| Continuous light, but not 5 to 20 Hz trains, raises the dopamine photometry signal in opsin mice (Figure 3b) | Reproduced, resting on two assumptions |
| The evoked change is larger in opsin than control mice for continuous light only (Figure 3c) | Reproduced, resting on an assumption |
| Acute and chronic silicon-probe findings (15 claims) | Blocked: methods underspecified (no sorted units; the paper's sort and manual curation cannot be repeated, and the light colour and rotarod direction are not labelled) |
| Juxtacellular, tracing, slice and open-field findings (24 claims) | Blocked: data missing |

The Figure 3b outcome rests on two assumptions about the paper's "two-way ANOVA with FDR-corrected
post hoc comparisons": that the ANOVA is the ordinary two-way ANOVA, and that its comparisons use
the model's residual error, as GraphPad Prism computes them. That comparison is not paired, as the
claims file's criterion asks. Of the paired forms, a pooled-difference form also gives the claimed
result in 20 of 32 readings, Prism's repeated-measures error gives continuous p 2.0e-04 to 5.3e-04,
short of the paper's p < 0.0001, and separate paired t-tests give p 0.072 to 0.11. The Figure 3c
outcome rests on Prism's within-cell error, which is the same under the ordinary and the mixed
design; with separate unpaired t-tests it does not hold. The notebook shows every form.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/gonzalez-cabrera-2026-01.yaml`](../../attempts/gonzalez-cabrera-2026-01.yaml).

- `reproduce_gonzalez_cabrera_2026.ipynb`: the data check of every file group and the two
  photometry claims. It takes about ten minutes, most of it streaming the files.
- `vtapno.py`: listing and surveying the files and their ADC channels, the paper's photometry preprocessing, peri-stimulus
  z-scores and the Figure 3b,c tests. Other notebooks on this dandiset can import it.
