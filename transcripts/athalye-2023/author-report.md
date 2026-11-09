I did steps 1 to 5 and the handover. Of the 29 claims, 17 are reproduced, 9 partially reproduced, 2 not reproduced and 1 blocked. Both notebooks pass `python tools/entry.py all` (14 min and 7 min) and `check` reports 0 errors. The handover is in `executed/000404-athalye-2023/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| conditions-per-session | reproduced (17.46) |
| figs1b-conditions-per-command | reproduced (7.06) |
| figs1d-command-subtrajectories-differ | reproduced |
| figs1e-next-commands-differ | partially (Monkey G 1.873, above 1.844) |
| fig3d-population-distance | reproduced |
| fig3b-single-neuron-distance | reproduced (shuffle means also match the code's printout) |
| fig3e-fractions-significant | partially (4 of 6 within tolerance) |
| fig4c-dynamics-predict-activity-given-command | reproduced, rests on an assumption |
| fig4de-condition-specific-activity-predicted | reproduced |
| fig4f-condition-specific-component | partially (session values fall outside 0.18 to 0.44) |
| fig4g-majority-predicted | reproduced |
| figs3-low-dimensional-decaying-dynamics | not reproduced |
| fig5c-next-activity | partially, rests on an assumption |
| fig5d-four-dimensions | reproduced |
| fig5e-next-command | partially, rests on an assumption |
| fig5f-condition-specific-next-command | partially (errors are 1/10 of expected; question asked) |
| fig5h-turn-predicted | partially (sign test p < 0.001 in 7 of 9 G sessions; 8 needed) |
| figs5b-dynamics-beyond-behavior | reproduced |
| figs5f-nonlinear-no-better | blocked, `too_large` |
| figs3f-residual-early-late | reproduced |
| figs4b-generalize-command-sets | reproduced, rests on an assumption |
| figs4g-generalize-condition-classes | partially, rests on an assumption |
| figs6cd, figs6g, figs6k | reproduced |
| fig6c-dynamics-reduce-input, fig6d-decoder-null-dynamics-no-saving | reproduced, rest on an assumption for Monkey J |
| fig6g-ofc-uses-distinct-patterns | partially (Monkey J decoder-null LME p = 0.02), rests on an assumption for Monkey J |
| monkey-j-linear-command | not reproduced (98.9 to 99.6%), rests on an assumption |

## 2. What was found about the dataset

I pinned version 0.230605.2024: the paper cites it, it is the only published version, and the draft holds the same files.

**Findings:**
- **Decoder matrices are missing**, although the paper's Data availability lists decoder parameters; the code that wrote the files has those lines commented out. I recovered Monkey G's Kalman gain exactly from the decoder state and spike counts (variance accounted for ≥ 0.99999 on 99% of updates). For Monkey J I refitted the linear approximation the paper itself uses.
- **Monkey J's target and obstacle series are wrong**: one value for every trial of a session, because the writer indexes frames with event-list positions. Monkey G's target series does not hold the trial's target either. I read targets from the cursor position at reward.
- **The trials table has only start and stop times.** Monkey J's obstacle trial types can only be recovered with a target-list file from the paper's code, which I recorded as an outside input.
- **Monkey J's units are mixed**: cursor in m, target series in cm with m values mixed in.

**Assumptions:**
- The R2 of the dynamics models and of the shuffle models is scored only on bins whose command is below the 95th percentile of magnitude. The Methods say those commands are "not analyzed", and this is the only reading under which the shuffle 95th percentiles match Table S1 (0.132 and 0.203 against 0.130 and 0.196). Both readings are shown.
- Monkey J's 100 ms decoder for the simulations is fitted to the decoder state, since the PPF parameters are not in the files.
- Monkey J's PPF update is taken as the velocity minus the fitted cursor dynamics.

**Questions for the paper's authors** (`methods_unavailable` findings in the record): which bins enter the R2 values; how Monkey J's simulation decoder was built; the units of the Table S1 next-command errors.

**Question for a reader** (`questions/000404.yaml`): for fig5f, the expected errors look like they are in units 10× the command's. Multiplied by 10, mine are 3.973 and 7.052, within tolerance.

## 3. Where the protocol was unclear

1. The protocol says to block `too_large` from a timed subset, but also says analyses run outside the notebook may never supply a number in the record. For figs5f, one Laplace-EM iteration did not finish in 10 minutes on the smallest session. I timed this outside the notebook and stated so in the notes.
2. Several criteria define "partially reproduced" only as "tests hold, values outside tolerance". They do not cover values within tolerance with one session test failing (fig5h, figs4g, fig5c) or per-session ranges failing (fig4f). I used `partially_reproduced`, as an effect that holds only in part.
3. When no reading matches, `measured` has no rule. I recorded the first reading the criterion lists.
4. A detail no criterion named (which bins are scored) changed outcomes. I handled it under step 1.6 as an assumption with both readings shown, which the protocol supports but does not anticipate for a detail spanning many claims.
5. The prompt forbids bold apart from the Result openers, while the example entry uses bold labels. I followed the prompt.

## 4. Runtime and failures

- **Runtime:** about 2 h 25 min (01:59 to 04:25 UTC). The two notebooks take about 14 and 7 minutes on 4 cores.
- **Failures:** none in the final runs. The rsLDS timing test was killed at its 10-minute timeout.
- **Untracked files not mine:** `git status` shows dotfiles (`.bashrc`, `.mcp.json`, and others) and a `scripts/` directory at the repo root. I left them untouched.
