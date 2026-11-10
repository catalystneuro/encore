# Gonzalez-Cabrera et al. (2026) from dandiset 001955

Tests the findings of [Gonzalez-Cabrera et al. (2026)](https://doi.org/10.64898/2026.02.17.706301)
that can be tested on [DANDI:001955](https://dandiarchive.org/dandiset/001955/0.261103.0758). The
dandiset holds fiber photometry of VTA dopamine neurons during optogenetic stimulation of VTA-PnO
neurons (5 opsin and 3 control mice, 5, 10 and 20 Hz and continuous light) and raw acute and
chronic silicon-probe recordings without sorted units.

| Claim | Outcome |
|---|---|
| Continuous light, but not 5 to 20 Hz trains, raises the dopamine photometry signal in opsin mice (Figure 3b) | Reproduced, resting on an assumption |
| The evoked change is larger in opsin than control mice for continuous light only (Figure 3c) | Reproduced, resting on an assumption |
| Acute and chronic silicon-probe findings (15 claims) | Blocked: data missing (no sorted units) |
| Juxtacellular, tracing, slice and open-field findings (24 claims) | Blocked: data missing |

Both photometry outcomes rest on reading the paper's "post hoc comparisons" after its two-way ANOVA
as contrasts on the ANOVA's pooled error, GraphPad Prism's default. With a separate t-test per
frequency neither claim holds; the notebook shows both.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/gonzalez-cabrera-2026-01.yaml`](../../attempts/gonzalez-cabrera-2026-01.yaml).

- `reproduce_gonzalez_cabrera_2026.ipynb`: the data check of every file group and the two
  photometry claims. It takes about eight minutes, most of it streaming the files.
- `vtapno.py`: listing and surveying the files, the paper's photometry preprocessing, peri-stimulus
  z-scores and the Figure 3b,c tests. Other notebooks on this dandiset can import it.
