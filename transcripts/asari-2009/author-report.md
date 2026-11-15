I've written the entry at `entries/asari-2009/` and the record at `attempts/asari-2009-02.yaml`. `entry.py all` passes with 0 check errors, and the handover is in `executed/asari-2009/handover/`. I did not come across any earlier attempt, and nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-recording-counts | partially reproduced: 305 probes / 39 cells and 93 MGB probes / 14 cells match exactly; 132 A1 cells meet the criterion against the paper's 123; voltage-clamp counts untestable |
| a1-mgb-firing-rates | partially reproduced (rests on an assumption): A1 rates below 1 Hz and MGB evoked above 5 Hz, but no reading puts all four means within 10% |
| fig2-example-reliability | reproduced: 0.310 ± 0.092 over cells; cell 20051222-ha1-001 gives exactly 0.61 and 0.74 |
| fig2-example-long-context | partially reproduced: nothing significant from 1.60 to 3.97 s; the criterion asks for nothing from 2 to 4 s |
| fig3a-proportion-significant | reproduced: 186 of 305 probes, late fraction 0.252, cumulative peak at 4.78 s (paper 4.72 s) |
| fig3a-significance-decay | partially reproduced (rests on an assumption) |
| fig3b-fractional-power-decay | not reproduced: time constant 1.29 to 1.78 s against 1.04 s |
| timescale-longer-than-membrane | reproduced |
| fig4-predictability-upper-bound | not reproduced: time constant 1.46 s or longer against 1.04 s |
| fig9-mgb-fast-decay, fig9-example-first-bin, figs1-silence-probe | reproduced |
| fig5, fig6 (conductances) | blocked, `data_missing` |
| fig4-strf, fig7, fig8 ×5 | blocked, `other` (not tested for lack of time) |

### 2. Dataset, assumptions, questions
- **Version:** CRCNS is unversioned. I pinned what the bucket serves and recorded the MD5 sums of the three zips in the notebook header.
- **Voltage clamp:** there are no voltage-clamp recordings. All 346 files are current-clamp or cell-attached traces in mV.
- **Partial deposit:** only the analysed cells are there (39 natural-sound A1, 96 synthetic, 12 unpublished, 14 MGB), not the 194 current-clamp and 16 MGB cells behind the paper's firing rates.
- **Authors' code:** the dataset ships the authors' MATLAB analysis code (`CxtDep.m` and others). The paper doesn't mention it; I followed it where the Methods leave a detail open.
- **Code problems:**
  - `CxtDep.m` ranks tied values by trial order instead of averaging them, so I used average ranks.
  - `GetSpikes.m` uses a high-pass filter designed for 4 kHz on 10 kHz traces, and its automatic threshold gives the lowest MGB rates of the three thresholds tried.
- **Labelling problems:**
  - In one recording (20051107-ha1-001-003) the trigger labels are numbered 2, 4, 6, 8 while the stimulus table numbers the same sequences 1 to 4. I matched triggers to the table by their fragment lists.
  - In 28 synthetic files nothing says which sound property varies, which is what the fig8 claims need.
- **MGB clock check:** spikes rise after stimulus onsets in 18 of 21 MGB files. In the other three (cells 20071012-ha1-002 and -003, 15 of the 93 probes) this check doesn't establish the alignment; I kept them.
- **Assumptions:**
  - Spike detectors: A1 spikes as excursions above the median-clipped trace, and MGB spikes at three thresholds.
  - The sizes in the Fig 3A two-exponential fit are bounded at zero. With free signs, the fit uses one term for the rise after onset.
- **Questions for the authors:** both assumptions are recorded as `methods_unavailable` findings.
- **Questions to a reader:** none.

### 3. Protocol gaps
1. The Time rule covers only claims still open at the stop time. I dropped the STRF and synthetic-sound claims early to finish the rest and recorded them as `other`, not `too_large`, since computation didn't stop them.
2. The protocol's order of sources doesn't cover analysis code shipped in the dataset but not linked from the paper. I ranked it as the paper's analysis code.
3. `measured` can't carry a gap for an expected value that can't be tested (the voltage-clamp counts), so I left it out for methods-recording-counts.
4. For the firing rates, the "one reading" rule doesn't say how readings combine when A1 and MGB use different detectors. `measured` mixes the 10 mV A1 reading with the 40 SD MGB reading, and the notes say so.

### 4. Runtime and failures
- The notebook runs in 9.5 minutes from a clean environment, with a peak of 1.2 GB.
- One exploration run hung on forked worker processes, most likely because they shared the parent's open HTTP connections. The tool reported a 1-hour timeout, but the clock showed far less time lost. Workers now start fresh with "spawn".
- Nothing else failed.
