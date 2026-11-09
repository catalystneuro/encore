I've finished the author run (protocol steps 1 to 6) for CRCNS hc-8 and Timme et al. 2016. The entry is `entries/crcns-hc-8-timme-2016/` (three notebooks, helpers `hc8.py` and `models.py`) and the record is `attempts/crcns-hc-8-timme-2016-01.yaml`. `entry.py check` reports 0 errors and the handover is built. Nothing is committed.

The analyses use a Python port of the paper's NCC MATLAB toolbox. I downloaded it from the author's website; its sha256 matches the one in the claims file, and it is listed under `inputs`. The data set is pinned as `unversioned`, with the MD5 of `Data.zip` from `checksums.md5`. CRCNS data sets have no versions and the bucket holds only this one copy.

**1. Outcomes** (29 claims: 12 reproduced, 4 partially reproduced, 8 not reproduced, 5 blocked)

| claim | outcome |
|---|---|
| culture-counts | reproduced: 435 recordings, 39,529 neurons, median 91 neurons |
| fig2d-network-isi | reproduced: median 6.67 ms |
| fig2e-avalanche-count | not reproduced: median 83,289 avalanches, not about 10,000 |
| fig8-subsampling-exponents | reproduced |
| fig8-exponents-match-literature | blocked (`other`): reference values from the three cited papers not retrieved |
| fig8-sigmanuz-methods-agree | reproduced |
| eq4-exponent-relation | reproduced (weak test: the propagated SDs are large) |
| eq4-relation-randomized | reproduced |
| fig9-branching-ratio | reproduced |
| fig10b-susceptibility-randomization | reproduced (under N·var(A/N) with Benjamini-Hochberg) |
| fig10c-curvature-randomization | partially reproduced: 4 of 5 randomizations |
| fig11ac-fit-range-randomization | reproduced |
| fig11bd-exponents-randomization | partially reproduced: tau 4 of 5, alpha 3 of 5 |
| fig10a-complexity-randomization | partially reproduced: shuffling raises complexity |
| figs8-complexity-susceptibility-correlation | not reproduced: r 0.542 vs 0.23 |
| figs9-complexity-fit-range-correlation | not reproduced: r 0.143 and -0.049 |
| fig12a-swap-preserves-complexity | not reproduced: swapping lowers complexity by 65% |
| fig12b-shuffle-lowers-complexity | not reproduced: real exceeds shuffled in only 10% of recordings |
| fig3-chain-model-complexity | reproduced |
| fig5d-bethe-small-avalanches | reproduced |
| fig5e-shuffle-removes-complexity | reproduced |
| fig5f-network-state-poisson-keeps-complexity | not reproduced |
| fig6-cb-distribution-curvature | partially reproduced: durations match, sizes at p_trans 0.2 do not |
| fig7c-cb-curvature-no-peak | not reproduced: curvature peaks at 0.25 |
| fig7ab, fig7a-complexity-boundary-rise, figs2, fig7d | blocked (`too_large`): complexity of sub-sampled cortical branching models, about 14 to 26 h of CPU |

Most of the complexity failures come from one step: the toolbox cuts the integration curve at its first peak. In the real data that cut keeps a median of 8 of 94 subset sizes, against 75 in shuffled data. Without the cut, fig10a, fig12a, fig12b and fig5f agree with the paper. No outcome is marked as resting on an assumption.

**2. Dataset**
- The counts match the paper exactly, and no recording is deposited twice.
- Findings recorded:
  - 47 files have 64 spike times beyond `data.nbins`.
  - 6 files repeat a spike time within a neuron, 21 times in all.
  - `wave_ClusParams.ref` is 30 samples (1.5 ms) in every file, although Methods 2.2 say the dead time was removed; intervals as short as 0.05 ms occur.
- Four questions for the paper's authors are recorded as `methods_unavailable` findings:
  - how avalanches were counted for Figure 2E;
  - which recordings were excluded for too few avalanches, and by what threshold (none are excluded under the reading used here);
  - how often the complexity cut applied with 100 subsets, and whether randomized data were cut the same way;
  - the p_trans grid of Figure 7.
- No questions to a reader.

**3. Where the protocol was unclear or missing something**
1. It doesn't say how to classify claims that are pure simulations and use no recorded data. I tested them with the default `data: dataset` and said in the notebook and summary that they say nothing about the dataset.
2. Under "Time" it allows `too_large` only "where the computation stopped it". For claims that only depend on a claim blocked for cost (fig7d, fig7a-boundary), I used `too_large` and named the dependency in the notes.
3. It doesn't say how to block an outside input that is public but wasn't retrieved in time (fig8-literature). I used `other`.
4. It doesn't say how to add the "**Result:**" cells, which can only be written after the full run, without re-executing. I inserted the same markdown cells into the source and the executed notebooks, leaving code and outputs untouched.
5. "Run every command in the foreground" plus the 60-minute notebook limit forced splitting the work into three notebooks; the protocol could suggest this for heavy entries.
6. The data-check step's clock check doesn't fit a dataset with a single spike-time stream. I said in the notebook that there is no second clock to check.

**4. Runtime and what failed**
- Full runs: 46 min (criticality, all 435 recordings), 32 min (complexity, 180 recordings), 12 min (models). The criticality notebook was re-run once (47 min) to print the firing-rate percentile at higher precision and read the wave_Clus parameters from the files.
- About 47 minutes were lost early to a development cell whose run time I underestimated: a sub-sampling layout that ran 44.9 min on 4 recordings. That layout ended up being run on one recording only.
- To fit the limits, complexity uses 10 subsets per size instead of 100 and 180 of the 435 recordings, and the p_trans grid is 0.01 only. Each is recorded as a deviation.
- Untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others) are at the repository root; I didn't create them. `tools/build_site.py` was already modified when the run started.
