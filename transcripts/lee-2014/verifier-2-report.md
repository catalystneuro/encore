**Round 2 verification: Lee et al. (2014), CRCNS hc-10, attempt `crcns-hc-10-lee-2014-01`**

**1. Outcomes**

The claims file has 34 claims, and the attempt record gives an outcome for each: 4 reproduced, 1 partially reproduced, 27 blocked as data_missing and 2 blocked as too_large. I agree with all 34.

- **figs1e-if-curves, reproduced:** agree. Two-way ANOVA group p = 0.411 under reading (a) and 0.866 under (b); the mixed ANOVA gives 0.759 and 0.951. At +550 pA the rates are 31.62 / 30.56 Hz (a) and 33.63 / 31.24 Hz (b), all within tolerance (cell 12).
- **figs1f-input-resistance, reproduced:** agree. 118.7 / 124.9 MΩ, Mann-Whitney p = 1.000 (cell 16).
- **figs1g-resting-potential, blocked (data_missing):** agree. No PC file has a current channel, and every baseline is within 2.6 mV of the −70 mV holding level (cell 19).
- **figs1h-sag, reproduced:** agree. 8.71 / 5.69 mV, p = 0.0020 (cell 22).
- **tables1-rheobase, partially reproduced:** agree. Reading (a), the median, gives 200 / 150 pA; reading (b), the rounded mean, gives 200 pA for both. No cell's rheobase changes under any threshold or under the CellData definition (cell 25).
- **figs3f-pvbc-firing, reproduced:** agree. PV34 gives 2.0, 17.0, 36.0 and 52.0 Hz and is silent up to +300 pA (cell 28).
- **The 26 claims on paired recordings, anatomy, imaging and optogenetics, blocked (data_missing):** agree.
- **fig4d-model-feedforward and fig4ef-model-pvbc-rates, blocked (too_large):** agree. The printed timing (cell 31) supports the block. The record's numbers for it do not match that output (see 2).

No outcome in the record carries `assumed: true`. The claims file's one assumption is in figs3f-pvbc-firing: 1 s steps in 50 pA increments for the PVBCs. The record states it as a deviation, and it is reasonable: cell 6 shows 1.000 s steps, and the data descriptor gives 50 pA increments. I found no new misreading of the paper in the claims file.

**2. Text against the printed outputs**

Not supported:

- **Cell 32 (Result, model claims):** "each simulated millisecond about 12 s on one core, so one 5,000 ms run would take about 17 hours and the 39 runs ... about 670 core-hours". Cell 31 prints 11.43 s per simulated ms, "about 16.0 h on one core" and "about 625 core-hours". Its "about 9 minutes" to build the network is fine (499.8 s).
- **Cell 34 (Summary):** "about 670 core-hours, from a 20 ms run timed here". The run printed 625.
- **Attempt record, fig4d-model-feedforward notes:** "a 20 ms run of one network on one core took 808 s, 537 s to build the cells and then 12.39 s per simulated millisecond; a 5 s run is so about 17.4 hours, and the 39 runs about 677 core-hours". Cell 31 prints a wall time of 749 s, 499.847 s to create the cells, 11.43 s/ms, 16.0 h and 625 core-hours. The same numbers appear in the fig4ef notes ("about 677 core-hours") and in both round-2 responses for the model claims. They come from a different run. "Compiles with NEURON 9.0.2" and "the model's own job scripts ran each simulation on 64 cores" are not printed anywhere in the notebook.
- **README:** the notebook "takes about 15 minutes". Cell 33 prints 12.8 min. This is a loose approximation and does not affect a conclusion.
- **Cell 9, and the record's PV37 finding:** "−13.1 against −8.7 and −9.1 mV". These deflections are never printed; cell 8 shows only `monotonic_up_to_0pA False` and Spearman 0.964. Taken at face value, the numbers put the break between −250 and −200 pA (−8.7 then −9.1). Cell 9 places it "between its −300 and −250 pA sweeps".
- **Record, fig5-cckbc-nonselective notes:** "sh108_BC ... from Lee et al. (2010)". This is not shown in the notebook; cell 30 says only "from other papers".

Every other sentence of the Result cells (14, 17, 20, 23, 26, 29), the Summary, the README and the record notes matches the printed numbers. I checked the following specifically:

- The spike counts differ by under 1% across thresholds (3121, 3144, 3143).
- 2 PC sweeps have one spike and none has two.
- Smoothing changes the sag means by at most 0.05 mV.
- The peaks at rheobase are 46.1 and 42.0 mV.
- The rheobase t test gives p = 0.732.
- The PVBC mean at +300 pA is 16.17 Hz.
- 26 + 2 = 28 untested claims.

**Round-1 reasons in the record:** they state my reasons faithfully, in my own words, with one exception. My problem 2, rate reading (b) being unreliable near rheobase, used PV34 at +350 pA (14.9 against 2.0 Hz), a figs3f claim. The record files it under figs1e without that example, and the figs3f reason leaves it out.

**3. Round-1 points**

Resolved:
- **B1 (input resistance window):** it was a disclosure and is stated.
- **B2 (rate reading b):** PC one- and two-spike sweeps are counted (cell 11), and the figs3f result states PV34's reading (b) value.
- **B3 (ANOVA independence):** the mixed ANOVA is shown.
- **B4 (rheobase thresholds):** each cell's rheobase is shown under −20, 0 and +10 mV and under CellData, with no changes.
- **B5 (PV34 as the figure's cell):** taking the best of six cells is now stated as permissive. The figure's cell is still unidentified, which is inherent to the data.
- **B6 (header table):** figs1g now has its reason code.
- **C, CellData's rheobase definition:** read and run.
- **C, ATF header:** printed. It holds only sweep start times, so the onset has to come from the voltage.
- **C, per-cell rheobase:** resolved (same as B4).
- **C, model timing:** a run is now logged in the notebook.

Remaining items that bear on a conclusion:
- The too_large reason for fig4d-model-feedforward and fig4ef-model-pvbc-rates quotes timing numbers (808 s, 537 s, 12.39 s/ms, 17.4 h, 677 core-hours) that the re-executed notebook does not print. Cell 32, cell 34 and the record should use the cell 31 values: 499.8 s, 11.43 s/ms, 16.0 h and 625 core-hours. The outcome does not change.
- The NEURON version and the 64-core job scripts cited for the model claims are not shown in the notebook.

The PV37 numbers in cell 9 and the record's finding should be printed or removed, but they bear on no conclusion.
