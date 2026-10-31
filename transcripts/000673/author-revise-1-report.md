I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all`. The check passes with 0 errors. Three notebooks pass, but `reproduce_daume_2024_lfp.ipynb` fails the 30-minute limit: it took 42 minutes, both times I ran it. Its channel processing took 38 minutes here, against 18 minutes in the author run. The per-channel work is unchanged (about 3.5 s per channel), so this looks like a slower runner, but CI will mark it as failed on a runner like this one.

**Outcome changes**
- **`edf3-hippocampus-pac-controls`**: blocked → `not_reproduced`, resting on artefact reading (a). The missing parts now run in a new notebook, `reproduce_daume_2024_lfp_controls.ipynb`. Two load tests give p < 0.05:
  - high-gamma power (p = 0.035 and 0.006);
  - gamma peak frequency (p = 0.003; reading it as the single largest bin instead gives p = 0.34).
  Waveform asymmetry, phase-phase coupling (both ratios), theta peak frequency and the preferred-phase t-test show no difference. Under reading (b) no load test is significant.
- **`fig3h-pac-category-firing`**: blocked → `not_reproduced`. On 166 hippocampal and 450 amygdala pairs (paper 151 and 423), no reading gives a positive hippocampal spike-count term. One reading gives a negative one (p = 0.015), and the amygdala term is null.
- **`fig2a-theta-gamma-pac`**: still reproduced, no longer marked as resting on an assumption. Reading (b) now also meets the criterion (peak at 4 Hz and 80 Hz, local maxima at 45 and 80 Hz).

**Added or corrected**
- **Tie-break for the artefact rejection reading (problem 6).** The paper's code ships `artif_trials.mat`, the 17 trials the paper rejected on its example channel (sub-26 session 1, channel 33). Reading (a) removes 4 trials there, all among the paper's; reading (b) removes 9, five of which the paper kept. This comparison and the spread of removed trials per channel are in the data check, and the record cites it wherever reading (a) is assumed.
- **PAC neurons (problem 1).** The paper's `plot_PAC_neuron.m` fits fixed-effects GLMs to 20 pooled bin counts, as `sbcat.py` does. So a per-trial layout or a random effect is not the difference the verifier suspected. Even uncorrected, only 41 hippocampal and 66 amygdala neurons qualify, fewer than the paper's 79 and 163 after correction.
- **Firing rate units (problem 3).** The evidence that rates are compared as % of baseline (the paper's frontal n match exactly) is now in `fig3c`'s deviation and `edf8fgh`'s notes.
- **Other outputs the verifier asked for:**
  - the 17 pre-SMA channels one by one: six patients, and the effect survives dropping the three largest (p = 0.0045);
  - `fig2f` with RT below 10 s and with log RT. With log RT the hippocampal term turns negative and significant under one single-trial PAC reading (p = 0.0066), but the claim's test is on RT itself, so the outcome stands;
  - the nesting count under windows of 25 to 85 ms: it depends on the alignment, not the window;
  - the units-table columns: waveforms are in all 44 files.
- **Questions file.** I added `questions/000673.yaml` with the V-test misreading (problem 5). The claim is unchanged.
- **Record.** The round-1 `verifications` block covers all 57 claims: the verifier disagreed with 16.

**Disagreements kept**
- `fig3c-category-load` stays `not_reproduced`, assumed. The verifier would give partially reproduced, but its own problem 3 supports the % of baseline reading, under which the claim fails.
- The five PAC-neuron firing claims stay blocked (other). The verifier gave outcomes for them, but its own problem 1 says tests on 8 and 5 neurons cannot test the paper's populations.
- `fig3b` and `edf4b` stay partially reproduced, as their criterion requires both firing-rate readings. The notes say they hold in full under % of baseline alone.

**Not done**
- **Spike-field coherence** (`fig3f`, `fig3g`, `edf5c`, `edf5d`, `edf5fg`, panels f and g of `edf8fgh`): still blocked as `too_large`, now with a measured estimate. I timed it on one session while preparing, outside any notebook. With each surrogate averaged over 500 spike subsamples like the observed value, it needs about 18 CPU hours. With one subsample per surrogate it would fit, but there was no time to write it.
- **`edf7a`, `fig5cd` and `fig6g`** stay blocked: they need SFC, the decoding analysis, or the PAC-neuron selection, none of which was run.

**Time**
To keep the LFP notebook from growing further, the Extended Data Fig. 3 controls run in the new controls notebook (21 min). After the final run I corrected one number in markdown only (an interaction p bound, from 0.002 to 0.0025), which changes no outputs. I did not commit.
