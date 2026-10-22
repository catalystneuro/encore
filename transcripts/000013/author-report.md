I've done steps 1 to 6 for DANDI:000013 (Hires et al. 2015). The entry passes `check` and runs from a clean environment in 8.7 minutes, and the verifier's package is in `executed/000013-hires-2015/handover/`. Of 45 claims, 20 are reproduced, 5 partially, 5 not reproduced and 15 blocked as `methods_underspecified`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| recordings-counts, behavior-performance, behavior-sample-epoch | reproduced |
| example-cell-rates (cell 23 is the Figure 1 cell; p = 1.36e-7, paper 3.38e-7), example-cell-sample-ff (7.51, exact), text-spikes-per-touch, example-cell-phase-modulation | reproduced |
| l4-outside-weaker-touch, l5-higher-rates, phase-mod-l4-inside-outside, phase-mod-l4-vs-l5 | reproduced |
| fig5c-modulation-index, fig6s1b-clusters-less-variable, fig6cd-ff-near-binomial | reproduced |
| the five fig6e claims (e.g. 6.58 ± 5.40 against 6.57 ± 5.41), whisk-cycle-spikes | reproduced |
| behavior-whisking-bouts, behavior-touches-reaction, example-cell-touch-window, whisking-rate-l4-no-change, whisking-rate-l5-increase | partially reproduced |
| recordings-mice, text-whisking-rates, latency-determinable, fig4b-touch-time-precision (1.1 to 1.4 ms against 0.55), fig4c-phase-decoding | not reproduced |
| the three table1 claims, the three fig3c, the four fig3d, the two fig4a, fig5-modulation-correlations, fig6d-not-refractory, example-cell-ff-around-touch | blocked: methods underspecified |

## 2. The dataset and the questions

**What I found:**
- **Pinned version:** 0.220126.2143, the only published version. The paper predates the dandiset, and the draft holds the same 52 blobs.
- **Recordings:** all 52 recordings, groups and trials are present. No recording is deposited twice.
- **Spike clock:** in 36 files the spike-train timestamps run 10 ms before the voltage timestamps of the same samples. The touch response puts the spike timestamps on the behaviour's clock in both kinds of file. That is consistent with the data but not proven.
- **Voltage and `theta_filt`:** in 38 files the voltage's unit conversion is off by 1000, and `theta_filt` is not the band-passed angle that the stored amplitude and phase come from.
- **Other metadata:**
  - `set_point` is mislabelled as an amplitude.
  - `pole_position` is described in mm but spans several scales across files (up to 1e12).
  - The 23 subjects and their genotypes don't match the paper's 21 mice (three subjects have no genotype).
  - Files are named "ogen" but hold no optogenetic data.
  - `first_lick_time` disagrees with the lick series in about 180 trials.

**Questions asked** (in `questions/000013.yaml`):
1. Where the search for the touch-window cutoff starts. Read literally, it stops at 1 ms, before the response has risen. This one question decides most of the blocked claims.
2. The longest window over which the cutoff curve is fitted.
3. Which pre-touch window the touch detector uses.
4. The time classes of the naive Bayes time decoder.
5. The phase decoder's cycles, response and handling of zero rates.
6. Whether the refractory model's rate was raised to make up for refractoriness.
7. What "median whisking rate higher" means in the L5 criterion.

## 3. Where the protocol was unclear, wrong or missing something

1. **One literal reading can block many claims.** Ten claims hinge on two readings of the cutoff rule, one of which is degenerate. The protocol's "the outcome is the one all readings give" then blocks them. I ran both readings and asked.
2. **A blocked dependency hides a clear failure.** fig3c-touch-spikes-outside fails under all 32 readings but is blocked through its dependency on the L4 C2 claim. The failure is recorded only in its notes.
3. **A criterion's fallback can conflict with the protocol.** fig4c's criterion says "else methods_underspecified", but all its readings agree it fails. I followed the protocol and marked it not reproduced, saying so in the notes.
4. **Too many reading combinations to agree.** Table 1 has 256 combinations of readings, so an agreed outcome is nearly impossible. I recorded the full range of results.
5. **"Any cell" criteria let chance decide.** In example-cell-ff-around-touch, cell 11 matches in 2 of 394 tries. The two readings of the touches then give different outcomes, so I blocked it.
6. **`measured` has no slot for "never reached".** For fig4c the outside-C2 decoder never reaches 76%, so I left `measured` out.
7. **The suggested clock check doesn't fit continuous trial data.** I used the touch response compared across the two batches of files, plus a control with shifted touch onsets.
8. **No published version is cited.** I pinned the only published version and said why in the header.
9. **The no-download rule:** the entry streams everything. While developing I cached the reduced arrays (not the NWB files) in `$TMPDIR`.
10. **Streaming advice belongs in `docs/archives.md`.** h5py with remfile serialises reads across threads, and single-element reads cost about 80 ms each. Loading needs separate processes: 80 s instead of 13 minutes.

## 4. Runtime and failures

The notebook takes 8.7 minutes (530 s), of which about 80 s is streaming. It was run three times through `tools/entry.py all`, all passing. During development the first loader took 13 minutes until I switched to processes, and a few code errors were fixed before the final runs. Nothing failed at the end. The untracked dotfiles at the repository root (`.bashrc`, `scripts`, and others) are character-device mounts from the sandbox, not files I created; I left them alone.
