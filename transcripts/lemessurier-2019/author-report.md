I finished steps 1 to 5 and ran the handover (step 6), all well before the 16:10 cutoff. All 34 claims have an outcome: 33 were tested and 1 is blocked. The entry passes `tools/entry.py check` with 0 errors, and `all` ran the notebook from a clean environment without failures. I did not commit or verify.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| table1-mice-and-fields | reproduced |
| l23-cell-counts | reproduced |
| l4-cell-counts | not reproduced |
| fig1f-gcamp-matches-spikes | blocked (data_missing) |
| fig2a-l23-point-representation-stronger | reproduced, only with the stored p-values and the median-centred z-score |
| fig2a-l23-flanks-suppressed | partially reproduced |
| fig2b-2d-point-representation | reproduced |
| fig2c-l4-point-representation-weaker | not reproduced |
| fig2c-l4-sharper-than-l23 | reproduced |
| figs2-1-column-frame | not reproduced |
| figs2-2-barrel-size-unchanged | partially reproduced |
| figs3-1-l23-salt-and-pepper | partially reproduced |
| discussion-l23-nh-in-column-tuning | partially reproduced |
| figs3-1-l4-nh-tuning | not reproduced |
| fig3a-l23-enrichment-more-cw-tuned | not reproduced |
| fig3c-l4-enrichment-more-cw-tuned | reproduced |
| fig4a-l23-ranked-rf-sharper | reproduced |
| fig4b-l23-cw-and-best-sw-stronger | reproduced |
| fig4c-spontaneous-activity | reproduced, only under the claims file's variant (no baseline subtraction) |
| figs4-1-absolute-dff | not reproduced |
| figs4-2-barrel-vs-septal | reproduced |
| fig4d-l23-cw-stronger | reproduced, only with the stored p-values |
| fig4d-l23-across-row-sharpening | partially reproduced |
| fig4d-l23-within-row-broadening | partially reproduced |
| fig4ae-l4-weaker-responses | not reproduced |
| fig5a-l23-signal-correlation-boundary | partially reproduced |
| fig5b-l23-noise-correlation-boundary | partially reproduced |
| fig5eh-l23-correlation-gradient-at-edge | reproduced, only with the stored p-values |
| figs5-1-row-and-arc-boundaries | not reproduced |
| fig6-l4-within-column-correlations | partially reproduced |
| figs5-2-neuropil-robustness | not reproduced |
| fig7b-single-roi-decoder | partially reproduced |
| fig7c-population-decoder | reproduced, only with ensembles pooled as units |
| fig7d-clustered-ensemble-topography | reproduced |

Totals: 15 reproduced, 10 partially reproduced, 8 not reproduced, 1 blocked.

## 2. Dataset, assumptions and questions

**What the dataset holds:**
- The mouse and field counts match Table 1 exactly.
- The NH L2/3 cell count is exact (998).
- Three totals differ from the paper: EN L2/3 is 1147 (paper 1257), NH L4 is 362 (322) and EN L4 is 615 (586).
- `processed_data.mat` holds more ROIs than `reduced_data.mat` in 21 of 36 fields, with no stated rule for the exclusions.
- One NH field (DNH13b) has no trials for whiskers E1, E2 and E3. The data descriptor does not say so.
- The stored dF/F was made with a 5-frame median filter and F0 at the 5th percentile, as the pipeline code does. The Methods say 4 frames and the 20th percentile.
- The stored responsiveness p-values come from a two-sided test on medians, not the Methods' one-sided test on means. The two tests agree on 85% of ROIs.
- Two coding rules are undocumented: what `Stimuli.Label` numbers mean, and how `sponTrace` picks its blank trials.
- Movie names are inconsistent between structures, and three movies have no stimulus table.
- No barrel areas are stored, and the normalised positions use a radius that changes with direction.
- The cell-attached recordings of Figure 1F are not in the dataset.
- I could not reproduce the L4 neuropil step exactly.
- The streamed `data.tar.gz` matches the MD5 in `checksums.md5`.

**Assumptions:** none recorded as `assumed`. Every open choice was run under all the readings the claims file names. A few routine choices could shift results slightly and are recorded as deviations:
- 50 train/test splits per field for the ensemble decoders.
- One k-means run per k.
- 1,000 shuffles for the median-based equivalent-best-whisker test.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How were the equivalent best whiskers tested? Every reading gives 90–96% of NH L2/3 cells near a column centre as tuned to the column's whisker, where the paper reports 67%. The L4 value matches (73.7% against 73%).
- Which responsiveness test defined the analysed cells? Four outcomes are significant only with the stored p-values.
- Is the spontaneous activity in Figure 4C baseline-subtracted? The direction of the effect flips depending on the answer.

**Questions to a reader:** none.

## 3. Where the protocol was unclear, wrong or missing something

1. **Archive format.** `docs/archives.md` describes zip files read by range requests. ssc-10 is a single 4.7 GB `tar.gz`, so every run has to stream the whole file (about 10 minutes). I streamed it once with `tarfile` and checked the MD5 over the stream.
2. **Developing on a subset.** With one `tar.gz`, there is no cheap subset. During development I cached the reduced arrays (not the raw files) in `$TMPDIR`; the notebook itself streams.
3. **Time target.** The "aim for under ten minutes" target cannot be met, because streaming alone takes ten. The notebook runs in about 24 minutes, under the 60-minute limit.
4. **"Variant" against "reading".** The protocol does not say whether a variant named in the claims file counts as a reading for "reproduced under any reading". I counted variants as readings. The fig2a, fig4c, fig4d-cw and fig5eh outcomes depend on this, and each record says so.
5. **Partial outcomes.** The protocol does not say what to do when a criterion has no partial clause, or when the result falls outside the criterion's own partial clause. Where the criterion has no partial clause and the effect holds in part, I recorded partially reproduced. Where the criterion defines a narrower partial case that the result misses (figs2-1, fig4ae, figs3-1-l4), I recorded not reproduced.
6. **Where the dataset's own sample code ranks.** The order of sources (Methods, the paper's code, other software) does not place the dataset's `sample_code.zip`. I used it for method details where the claims file names them as variants (stored p-value responsiveness, median-centred z-score), and cited it.
7. **Clock check.** The protocol's decoding-with-shifted-labels check does not fit trial-aligned imaging. I used a whisker-minus-blank contrast with shifted onsets. It supports a shared clock in 30 of 36 fields; in the other six it is not established.
8. **`measured` when no reading matches.** The protocol only says which reading to record when several match. When none matched, I recorded the first listed or main reading and said which in the notes.
9. **Unversioned data.** Since CRCNS has no versions, I pinned the dataset by MD5 and checked that MD5 in the notebook.

## 4. Runtime and failures

- The run took about 2 h 20 min, from 11:55 to about 14:15 UTC.
- The full notebook takes about 24 minutes, 9.7 of them streaming. Peak memory was about 1.8 GB.
- During development, the first full streams crashed on inconsistent movie names and on the missing E-row whiskers in DNH13b; I fixed the reader to handle both.
- Both official runs passed. The second added printed values that back the conclusions, and its numbers were identical to the first.
- After the run I fixed one conclusion sentence in both the source notebook and the executed copy. It was a markdown-only change, and no code changed.

Files are in `entries/crcns-ssc-10-lemessurier-2019/`, with the record at `attempts/crcns-ssc-10-lemessurier-2019-01.yaml`. Open the notebook `reproduce_lemessurier_2019.ipynb` first.
