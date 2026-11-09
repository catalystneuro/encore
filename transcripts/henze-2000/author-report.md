I finished steps 1 to 5 and ran the handover (step 6). The entry is `entries/henze-2000/` (helper `hc1.py`, notebook `reproduce_henze_2000.ipynb`) and the record is `attempts/henze-2000-01.yaml`. `tools/entry.py all` gave 0 errors and the notebook ran from a clean environment in 532 s. I did not change the claims file, did not add any reader questions, and did not commit.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| sample-cells | not reproduced: 21 tetrode cells, not 33; all 21 have a resting potential below -55 mV; none has a cell-type label |
| fig1c-start-end-timing | not reproduced: the start lead is outside 0.01 ± 0.02 ms under all 16 readings |
| ap-duration-match | reproduced under 6 of 16 readings (1.38 and 1.28 ms) |
| duration-correlation | partially reproduced: R 0.76 to 0.94 with P < 0.03; no reading gives R near 0.66 with P < 0.03 |
| neg-peak-precedes-intra-peak | reproduced: 0.207 ± 0.094 ms over 8 cells |
| fig1c-derivative-mismatch | reproduced: holds in 7 of 8 cells |
| notch-and-ahp-landmarks | not reproduced |
| fig2-interneuron-narrow | blocked, metadata_insufficient |
| fig3b-latency-vs-amplitude | reproduced: r -0.70, P 0.0006; dendritic median latency above somatic |
| fig3a-example-pair | blocked, metadata_insufficient: two candidate pairs, neither matches |
| fig3c-backprop-velocity | not reproduced: 0.23 to 0.49 m/s with all spikes |
| fig4bc-burst-attenuation | reproduced, `assumed: true`: 9 of 17 cells, which depends on how cells are selected |
| fig4d-amplitude-correlation | reproduced: two cells give R 0.367 and 0.431 |
| fig5, theta-higher-rates, fig6, tetrode-cell-count-estimate, silent-cells-inference, fig8 | blocked, data_missing |
| fig7-vertical-spread | not reproduced: the spike reaches 100 µm from the soma site in 3 of 10 cells |
| propagation-velocity-range | blocked, data_missing; the anesthetized silicon-probe recordings are shown as a variant |

**2. The dataset**
- **What it holds:** 39 cell folders, 169 binary files, about 23 GB. There are 21 tetrode cells and 18 silicon-probe cells, and only the anesthetized recordings. CRCNS does not version datasets, so I pinned the `live/` files by their MD5 sums; there is no other copy, and the notebook header says so.
- **Channels:** only 5 folders have a README naming the channels. The intracellular channel moves between files of one cell, and two binary formats (12-bit and 16-bit) are mixed with no note. The notebook picks the intracellular channel from the data in each file.
- **Scaling:** every xml file says gain 1000. The intracellular channel matches the spreadsheet's resting potentials only at the README's "typical" gain of 50 (within 5 mV for 11 of 17 cells). At that gain, D128's 16-bit files give an implausible -108 mV.
- **Spreadsheet:** it covers 18 of 39 cells and only 2 of the 21 tetrode cells. There are no cell types, impalement sites or tetrode-to-soma distances for the other 19.
- **Duplicates:** two D81 files repeat parts of a third file.
- **Missing xml:** two files have none, and one of them has no intracellular action potentials.
- **Site order:** the spreadsheet lists channel numbers up to 10 for files that have only six extracellular channels.
- **Assumptions:** for Fig. 4 a cell enters with at least 10 current steps reaching a 5th spike (the only outcome resting on an assumption). For the six-channel probe files the site order is the listed channel divided by two; fig7 fails with or without these cells.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): which cells and trains form the Fig. 4B and C analysis?

**3. Where the protocol was unclear or did not fit**
1. The prompt asks for a pinned published version, but CRCNS has no versions. I recorded `unversioned` with the MD5 sums, as docs/archives.md says.
2. Nothing covers a dataset whose channel roles have to be inferred from the data. I chose them by a stated rule and printed the choice per file in the data check.
3. For the clock check, the protocol suggests decoding against shifted labels. Here the channels share one sampled matrix, so I compared the extracellular average at the spike times with the same average 25 ms later: 35 of 38 cells show a spike at the true times, 2 do at the shifted times.
4. Step 1.5 says to decide blocks before analysis, but for propagation-velocity-range the dataset only allows the criterion's first reading, while the paper's counts imply the second. I ran the first reading and then blocked the claim as data_missing, showing the results.
5. It is unclear whether "identified" in the fig3a criterion covers a pair guessed from folder names. I blocked it and reported both candidates.
6. Nothing says how to treat a criterion's majority that depends on a selection threshold the paper never states. I marked fig4bc `assumed` and showed the result at 10, 20 and 50 trains.

**4. Runtime and failures**
The work took about 1 h 35 min of the 5 h. Building the cache of all files takes about 5 minutes with three workers, and the full notebook run took 622 s, then 532 s on the rerun. Nothing failed. Executed outputs were identical to the development run, and all claims were tested or blocked well before the time limit.
