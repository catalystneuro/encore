I finished the attempt and ran the handover. The notebook executes cleanly through `tools/entry.py all` in about 13 minutes (peak memory 3.7 GB), and `check` reports no errors. The handover package is in `executed/laboy-juarez-2019/handover/`. Nothing is committed.

## 1. Outcomes (50 claims)

| Claim | Outcome |
|---|---|
| exp1-units, exp1-cw-tuned-fraction | reproduced (assumed) |
| fig1b, supp1d, fig1d, fig1f, fig1g, supp2 | reproduced |
| exp1-cw-sw-comparable-firing | partially: spontaneous rates match; maximal evoked firing is 0.6–0.9 spikes per stimulus against the paper's 4.8 |
| fig1e-best-combination-includes-cw | partially (assumed): SW-tuned fraction 0.421 against a lower bound of 0.423 |
| exp2-units, fig2f-shuffle, fig2f-most-selective, fig2g, fig3a, fig3b both, fig4a, fig5a, fig5c-pseudo, fig5c-all-dt, supralinear, fig6b-best/worst, fig6b-suppression | reproduced |
| fig7a-dt-half-width | reproduced (assumed): 11.5 ms |
| supp4, supp6, fig4c, fig5bc, fig6c, fig7b, fig7c, fig7e, fig7f | partially |
| methods-dt-modulation, exp2-combination-selective-prevalence, fig3e, fig3g, fig6b-enhancement-not-different, fig7g, supp8 | not reproduced |
| exp3-units, fig8d, exp3-combination-selective, fig8i, fig8j, fig8k | reproduced |
| fig8c, fig8h | partially |
| fig8b-awake-behavior | blocked: data_missing |

The total is 29 reproduced, 13 partially, 7 not reproduced and 1 blocked. The main divergence is the shuffle test: it finds 318 of 463 response sets combination-selective, against the paper's 187 of 451. Every later claim about selective units uses this larger set.

## 2. Dataset, assumptions and questions

**What the dataset holds.** Unit counts match the paper: 160, 247 and 81 units, in 8, 16 and 6 recordings. Problems found:
- **Experiment 1:** the files hold rostral as well as caudal single-whisker deflections (18 stimuli, not 9). In both 20170510 recordings, whiskers 3 and 8 are deflected rostrally in their pairs.
- **Undocumented three-whisker trials** in 9 of the 16 experiment 2 recordings, 16,000 to 24,000 each.
- **Duplicated unit:** two units in 20160909 have identical spike trains. In 20160803 and 20160909, some units carry the recName of a different recording than the one whose trials they hold.
- **Missing sham trials** in two experiment 2 recordings (20160225, 20160316).
- **Experiment 2 dt values:** 101 of them (−50 to +50 ms), where the paper says 100.
- **Experiment 3 gaps:** no deflection times, lick times, trial types or per-unit depth. The sign convention of DeltaT is undocumented; I worked it out from CW response latencies.
- **Experiment 3 late spikes:** about a third of spike times fall after the ~300 ms epoch, up to 425 s.

**Assumptions.** These are recorded as deviations, with `assumed: true` on exp1-units, exp1-cw-tuned-fraction, fig1e, fig7a and fig8c.
- Experiment 1 single-whisker stimuli are the caudal deflections. Experiment 3, which the Methods call identical to experiment 1, used only caudal ones, and this reading gives the paper's counts.
- Response sets whose best-combination curve was set constant across dt have no best dt, so they are left out of the Fig. 7a alignment.

**Questions for the paper's authors** (`methods_unavailable` findings):
- How the dt smoothing handled edges, zero rates and held-out dt values with no training trials. The "unsmoothed" category never wins here.
- Which best dt was used for units whose curves were set constant.
- Which deflection direction experiment 1 used.
- How the selectivity shuffle handled constant curves and inverted the Mahalanobis covariance.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Every reading versus combinations of readings.** The claims file has several open details that multiply (O1 to O4). I ran the main combination for every claim, the variants on each claim's own readings, and did not carry alternative selections (for example the other FDR family) into the downstream claims.
2. **Expected values the criterion leaves out.** For supp6 and fig7f, the layer and group counts are in `expected` but not in the criterion's "reproduced when" clause. I treated a missed count as partially reproduced.
3. **Partial rules that miss the case.** For fig8c and fig1e the result fits neither the criterion's full rule nor its partial rule. I used the protocol's definition of partially reproduced and explained this in the notes.
4. **Testing on a parent claim's different selection.** Dependent claims are blocked only when their parent is blocked. Here the parent ran but selected a different set of units. I tested the dependent claims anyway and noted the different set in each.
5. **Which outcomes to mark `assumed`.** A single assumption (the experiment 1 direction) touches every experiment 1 claim. I marked only the claims whose outcome changed under the alternative reading, and showed all readings in one variant table.
6. **The clock check does not fit experiment 3.** Its epochs start at the stimulus, so decoding before onset is trivially at chance. I added the CW latency shift (30 ms against 70 ms) as the check instead.

## 4. Runtime and failures

The final notebook takes 13 minutes. The session took about 1 h 50 min from the start of work.

Two problems during development were fixed before the final run:
- Peak memory reached 9.8 GB. pandas copies `DataFrame.attrs` into every derived object, and a wide concatenation of tables made it worse; the final peak is 3.7 GB.
- Python's randomized `hash()` gave recording IDs that changed between runs; I replaced it with MD5.

Nothing failed in the final run. The untracked `.bashrc`, `scripts` and similar entries in the repository root are sandbox device files that existed before this session.
