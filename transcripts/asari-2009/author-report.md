The entry is written at `entries/asari-2009`, the record at `attempts/asari-2009-03.yaml`, and the handover is built. `tools/entry.py check` reports 0 errors, and `all` ran the notebook from a clean environment and it passed. I did not see any earlier attempt's results during this run. The protocol text itself says that "on three claims of asari-2009 one attempt of four was the one that was right"; I read that sentence, but it gives no outcomes.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-recording-counts | partially reproduced |
| a1-mgb-firing-rates | partially reproduced (assumed) |
| fig2-example-reliability | reproduced |
| fig2-example-long-context | reproduced |
| fig3a-proportion-significant | reproduced |
| fig3a-significance-decay | partially reproduced |
| fig3b-fractional-power-decay | partially reproduced |
| timescale-longer-than-membrane | reproduced |
| fig4-predictability-upper-bound | partially reproduced |
| fig4-strf-performance-low | blocked (other: not run in the time available) |
| fig5-example-conductances | blocked (data_missing) |
| fig6-conductance-decay | blocked (data_missing) |
| fig8a-proportion-by-property | partially reproduced (assumed) |
| fig8b-decay-by-property | partially reproduced (assumed) |
| fig8a-significance-fits | not reproduced (assumed) |
| fig8c-relative-effects | partially reproduced (assumed) |
| fig8-natural-synthetic-probes-alike | reproduced (assumed test) |
| fig9-mgb-fast-decay | partially reproduced |
| fig9-example-first-bin | reproduced |
| fig7-example-frequency-context | blocked (other: no recording matches) |
| figs1-silence-probe | reproduced |

### 2. Dataset, assumptions and questions

**What the dataset holds.**
- **Pinned version:** CRCNS ac-1, `unversioned`, pinned by the MD5 sums of the three zips. It is the only published version.
- **Counts that match:** the natural-sound and thalamic samples match the paper exactly: 305 probes in 39 cells, and 93 probes in 14 cells.
- **Missing voltage clamp:** there are no voltage-clamp recordings, so Figures 5 and 6 cannot be tested.
- **Fewer cells:** there are 145 current-clamp A1 cells (the paper recorded 194) and 14 MGB cells (the paper recorded 16).
- **Metadata error:** in two files, `20051107-ha1-001-003` and `-004`, the triggers number the sequences 2, 4, 6, 8 while the notes number them 1 to 4. I matched sequences by their content.
- **Clock:** the trial tables share the traces' clock, shown by a test that jitters each trial's onset.
- **Authors' code:** the dataset includes the authors' analysis code (`asari/Tools/CxtDep.m` and helpers). I used it, with citations, for details the Methods leave open: silence counts as a context, how many trials each context keeps, the run rule for significance, how traces are centred, and the MGB spike detector.

**Assumptions** (each marked `assumed: true` in the record):
- **A1 spike detector:** the authors extracted whole-cell spikes by hand. I used peaks more than 15 mV above the trace's 10-ms median, and also ran 10 and 20 mV.
- **Figure 8 stimulus sets:** I formed the groups of conditioning stimuli that differ in one property from the stimulus parameters. This reproduces the paper's AM (96) and FM (82) totals exactly. It gives 104, 120 and 354 tests for amplitude, frequency and higher-order, against the paper's 95, 110 and 137.
- **Fisher test:** fig8-natural-synthetic uses the Fisher test that the claims file fixes.

**Questions for the paper's authors** (filed as `methods_unavailable` findings):
- At time t, is the proportion of significant probes taken over all probes or only those still running? The late fraction matches (0.255) only under "all probes".
- How were the probe sets behind Table 1 and Figure 8 formed?
- How were A1 spikes detected, and which windows define spontaneous and evoked rates?
- What fit ranges and size bounds were used for the exponential fits?

**Questions to a reader:** none.

### 3. Protocol points

1. **Repeat-attempt section names this paper.** It says "on three claims of asari-2009 one attempt of four was the one that was right", which hints at earlier outcomes in a blind run. I ignored it and did not look further.
2. **No outcome rule for some misses.** Several criteria say only when a claim is reproduced, with no partial rule (fig3b, fig4, fig9-mgb). Where the effect was present but a value fell outside tolerance, I used the protocol's general meaning of "partially reproduced" and gave the reason in the notes.
3. **Blocking for lack of time.** "Blocked for time" only names `too_large` when the computation is what stopped it. I blocked the STRF claim as `other`: it was never started for lack of time, and its data are in the dataset.
4. **Analysis code inside the dataset.** The protocol does not say how to rank code that ships with the data but that the paper does not link. I treated it after the Methods, like the paper's own code, and cited it.
5. **Recordings deposited twice.** The protocol asks for a check but this dataset has no identifiers for it. I compared each file's first-probe power trace and found no duplicates.

### 4. Runtime and failures

- **Runtime:** the notebook takes about 33 minutes (1988 s in the clean run) with peak memory about 1.2 GB. I ran it in full twice; the second run was after a text-only fix, and the numbers were identical.
- **Lost time:** about 30 minutes, when my first pass using forked worker processes hung, because the HTTP reader used to stream from the bucket does not survive a fork. I switched to spawned processes.
- **Not run:** the trial-resampling reading of the Figure 8C intervals; only probe resampling was run.
- **Leftover folder:** the harness left a `.claude/` folder inside `entries/asari-2009`. Deleting it needed approval that this session cannot give, so it is still there and should be removed before commit.
