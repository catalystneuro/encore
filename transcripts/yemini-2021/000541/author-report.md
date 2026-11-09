Steps 1 to 6 of the Author section are done. The entry passes `check`, runs from a clean environment in 3 to 6 minutes with no errors, and the handover package is in `executed/000541-yemini-2021/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| link-zenodo-traces (link I added) | partially reproduced: files and stimulus orders match in 21 of 21; median r 0.972; 81.7% of traces reach r ≥ 0.9, below the 90% I set |
| link-connectome-names (link I added) | reproduced: 190 of 193 names match; the 3 that don't are not neurons |
| fig6-sample-sizes | partially reproduced: head counts match, no tails in the dandiset |
| fig6-all-heads-responsive | not reproduced: 19 of 21 heads pass under the most lenient rule |
| fig6d-ase-nacl | reproduced |
| fig6-nacl-unknown-interneurons | partially reproduced: 4 of 6 (AVF and AVJ fail) |
| fig6c-odors-more-inhibitory | reproduced |
| fig6d-awc-asymmetric | blocked, metadata_insufficient (variant with the Zenodo ON/OFF labels: p = 0.56 and 0.087) |
| fig6-asj-ric | partially reproduced, rests on an assumption |
| fig6-interneurons-downstream | reproduced |
| fig6-tail-responses | blocked, data_missing |
| fig6f-pharyngeal | reproduced |
| fig6-stimulus-sets-distinct | reproduced |
| figs1h-avf-cyclic | not reproduced: median 0.12 to 0.19 Hz against 0.3 Hz |
| fig6gi-stimulus-specific-correlations | reproduced, rests on an assumption; a window with no stimulus passes the same test |
| figs2a-pca-trajectories | not reproduced: at most 1 of 3 pairs separated |
| fig6jk-connectome-correlation | partially reproduced: heads only; all R² below 5%, none within tolerance |
| fig6-connectome-variations | reproduced: largest R² 1.66% |
| 11 claims on Figures 1, 2, 4, 5, 7 and S1A to S1G | blocked, data_missing |

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.241009.1457, the most recent published version. The paper cites no dandiset version, and all three published versions hold the same 21 assets.

**What the dataset holds.**
- Only the 21 OH16230 head recordings. The 21 tails, the 7 OH15500 heads and the 10 atlas worms are in the paper's Zenodo deposit (doi:10.5281/zenodo.3906530), not in the dandiset.
- AWC ON and OFF are not labelled. The Zenodo deposit has this (`is_AWCL_OFF`).
- The "raw" and "dNMF" trace series are identical in all 21 files.
- The neuron labels include two glia (AMSOL, AMSOR), the head mesodermal cell (HMC), and DD6, a posterior motor neuron, in one head file.
- 101 named traces have no counterpart in the paper's deposit, and 13 traces are all NaN.
- The stimulus table gives 2-butanone as "10^-4mM" and calls the order random. The files show three orders, seven heads each, which fits the paper's "rotated periodically".

**Assumption.** The STAR Methods say neurons within 5 µm whose traces correlate at 0.95 or more "were deemed too similar and removed", without saying whether one or both of a pair go. I removed both, the plainest reading of that sentence, and ran "one" and "none" as variants. Two outcomes depend on this choice:
- fig6-asj-ric would be not reproduced under the other readings.
- fig6gi-stimulus-specific-correlations would be partially reproduced under the other readings.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which member of a near-duplicate pair was removed?
- Were the t-tests run on ΔF/F0 or on the dNMF histogram-normalised traces?
- How was a head judged to show the published ASE and AWC responses?

**Questions to a reader:** none.

## 3. Protocol gaps

1. Tail claims are marked `data: dataset`, but the tails are public on Zenodo. The protocol says data in another archive should be `elsewhere` and never blocked as `data_missing`, but the author may not edit the claims file. I blocked them as `data_missing`, with the Zenodo location in the notes. fig2-positional-variability and fig7bc-id-accuracy have the same problem: the 10 atlas worms are on Zenodo.
2. The author cannot add a link claim to a reader's `depends_on`. fig6jk and fig6-connectome-variations need link-connectome-names, so I said so in their notes instead.
3. The protocol has no form for a link claim's criterion written after the outside data were seen. I wrote the Zenodo link's thresholds after reading the deposit's layout and said so in a deviation.
4. When an expected value cannot be measured at all (tail R²), `measured` must still give one value per expected value. For fig6jk I left `measured` out; for fig6-sample-sizes I recorded the dataset's tail count of 0.
5. Nothing says how to judge a criterion whose test also passes a null control. In fig6gi, a window with no stimulus gives 100 of 100 splits too. I kept the criterion's outcome and stated the null result in the notes.

## 4. Runtime and failures

The run took about 50 minutes (16:01 to 16:51 UTC). The final notebook run took 332 s, most of it streaming 21 files of about 1.45 GB each plus the 1.1 GB Zenodo zip read in place. Nothing failed. The untracked dotfiles in the repository root (`.bashrc`, `scripts` and so on) are sandbox device nodes, not files I created.

Files are in the repository:
- `entries/000541-yemini-2021/`
- `attempts/000541-yemini-2021-01.yaml`
- `claims/000541/10.1016-j.cell.2020.12.012.yaml` (two link claims appended; nothing else changed)
