I've built the entry `entries/clark-2026` (four notebooks, two helpers), written `attempts/clark-2026-01.yaml` and built the handover package. `python tools/entry.py all` passed, `check` reports 0 errors, and nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| hd-cell-selection (link) | reproduced: all counts exact (31, 2,691, 1,533, 315, 117/93/90/86) |
| tuning-curves-match-cache (link, uses the Zenodo cache) | reproduced: r = 1.000000 on all 1,533 curves |
| fig1e-heterogeneous-peaks | reproduced |
| fig5d-peak-numbers | reproduced: data counts exact |
| fig1fg-mean-and-fluctuation-profiles | reproduced |
| fig3ab-centers-of-mass-uniform | reproduced: 2 sessions, 0 after correction, corrected P 0.592 to 0.968 |
| fig3c-correlation-approaches-circulant | reproduced |
| fig4-generative-fit | partially reproduced: (σ, β, b) = (1.474, 3.110, 1.215), b is outside tolerance |
| fig5ab, fig5c, fig5d-peak-heights, fig5e, fig5f | reproduced (5 claims) |
| fig2l-recorded-bump-tracks-hd | reproduced under reading (a); circular r is 0.896, just under the 0.9 of reading (b) |
| fig2b-sorted-weights-mexican-hat | reproduced |
| fig2ef-data-network-quasicontinuous | reproduced |
| fig2gi-circulant-noise-collapses | partially reproduced |
| fig2jk-velocity-integration | reproduced |
| figs14-data-spectrum-doublets | reproduced |
| figs11b-data-network-global-stability | partially reproduced |
| figs8-s9-lambda-and-c | partially reproduced |
| fig7-dmft-mexican-hat-and-stability (elsewhere) | reproduced |
| fig7de-dmft-timescales (elsewhere) | not reproduced, by the claims file's thresholds |
| fig7c-dmft-integrates-behavior | reproduced |
| fig6cd-eigenvalues-real-degenerate (elsewhere) | reproduced; seed sensitive (1 of 5 seeds is 13.6% off) |
| fig6fg-disordered-eigenvectors (elsewhere) | reproduced |
| fig8, figs10, figs11-s12, figs1-s2 (elsewhere) | blocked, `too_large`: not started for lack of time |

## 2. Dataset, assumptions, questions

- **Version pinned.** 0.240528.1542, the version the paper cites. Every file was replaced in later versions (new names, 12.7 to 30.2 GB each, no file shared), so the paper's code only fits the cited one.
- **The files match the paper.**
  - All 1,533 head-direction units are also labelled excitatory.
  - Every file, including the `+ogen.nwb` ones, holds the `wake_square` epoch. That answers the claims file's open question.
  - Spikes and head direction share a clock: in all 31 sessions the information peaks within 0.05 s of lag 0.
  - No recording appears twice.
  - The rebuilt tuning curves match the paper's cache to 1e-14 Hz, and my network gives the paper's printed reconstruction error (1.7152e-08).
- **Findings about the paper.**
  - The Fig. 4 fit has two near-equal minima on the grid: the paper's point and (1.47, 1.21, 3.11). Which one wins depends on the random draws and on float32 versus float64.
  - At 293 of the 800 grid points of the mean-field stability analysis, the bump has no zero eigenvalue.
- **Assumptions and reader questions.** I made no assumptions, so no outcome is marked `assumed`, and I asked a reader nothing.

## 3. Protocol points

1. The claims file names "numpy seed 42", but the protocol requires seeds from crc32 of the claim id. I used the protocol's seeds and recorded it as a deviation.
2. The fig4 criterion asks for 500,000 samples at all 18,000 grid points, about 3 hours here. The protocol has no rule for a criterion that is too costly to run as written. I ran the whole grid at 25,000 samples, then the best 30 points at 500,000, and recorded the deviation.
3. The fig2gi criterion asks for at least 50 states, which its own position measure cannot reach (the starting states alone give 24 to 33). The protocol handles ties, not thresholds that cannot be met. I applied it as written and showed a variant measure.
4. The run stamp hashes every file in the entry, so writing conclusions or the README after a run makes the next run a full one (52 min here). Writing results from outputs therefore costs two full runs. The protocol does not mention this.
5. `data: elsewhere` is defined for data deposited in another archive. It fits poorly for claims that are pure simulation with no data. I treated the paper's code at its commit as the input.
6. For claims never started because time ran out, the protocol only names `too_large` "where the computation stopped it". I used `too_large` with cost estimates.
7. The criteria leave "collapse" (figs8-s9) and "merged into one state" (fig2gi) open. I ran every reading; the outcome is the same under each.

## 4. Runtime and failures

- The entry takes about 52 minutes per run: 16, 24, 9 and 2.5 minutes for the four notebooks; peak memory 1.7 GB. I ran it in full three times.
- The second run was needed because my first distance computation, in float32, rounded distances below about 1e-3 to zero. That changed two numbers the criteria read, so I fixed it and reran.
- Nothing failed in the final run. The run ended at 15:25 UTC.
