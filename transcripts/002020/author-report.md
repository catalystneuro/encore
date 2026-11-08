I've done steps 1 to 6 of the Author section. The entry passes `python tools/entry.py check` with 0 errors, the notebook ran cleanly from a clean environment in 6.6 minutes, and the handover is built in `executed/002020-nakamuta-2025/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| dishes-analysed | reproduced (assumed), 7 dishes |
| activity-onset | blocked, metadata_insufficient |
| fig1b-async-to-bursts | reproduced (assumed) |
| fig1d-power-law-emerges | blocked, methods_underspecified |
| fig1e-example-dish | blocked, metadata_insufficient |
| fig1f-transition-15div | blocked, metadata_insufficient |
| fig1f-exponent-1p2 | blocked, metadata_insufficient (depends on the claim above) |
| fig1d-shuffle | blocked, methods_underspecified |
| fig2b-spatial-structure | not_reproduced (assumed) |
| fig2c-locality-spectrum | reproduced (assumed) |
| fig2d-locality-slope | partially_reproduced (assumed) |
| fig2d-shuffle-locality | partially_reproduced (assumed) |
| fig3c-avalanches-emerge | blocked, metadata_insufficient |
| fig3d-decay-rates-correlated | not_reproduced |
| fig3ef-groups-cooccur | blocked, methods_underspecified |
| figs1-classified-by-avalanches | blocked, methods_underspecified |
| figs2-shuffle-breaks-cooccurrence | blocked, methods_underspecified (its readings disagree) |
| no-temporal-structure | not_reproduced (assumed) |
| fig4d-cauchy-model-power-law, fig4d-gaussian-model-no-power-law | blocked, methods_underspecified |

## 2. Dataset, assumptions, questions

**Version.** I pinned `0.261004.1410`. It is the only published version and the draft is identical to it.

**What the dataset holds.** Seven dishes and 129 recordings of unsorted spike detections, with electrode positions. The positions match the MaxOne grid. Frame numbers match the spike times. Since the files hold only spike times and no trial or annotation table, the clock check had nothing to compare against. No recording is deposited twice: dishes recorded at the same moments have population counts that correlate at most 0.225.

**Findings about the dataset.**
- **No days in vitro.** The files have no DIV and no plating date; they say so themselves. This is the main reason claims are blocked.
- **Time origin.** Spike times run from the first detected spike, not from the start of the recording.
- **Unmarked inactive recordings.** 17 recordings are at or below the paper's 0.03 Hz rate. Some fall in the middle of a dish's series, and nothing marks which recordings the paper analysed.
- **Short electrode counts.** Seven recordings have 338 to 702 electrodes, where the rest have about 1,000.

**The fitted decay rate b does not match the paper's scale.** On the claims file's reading of the fit (rank as x), b is 0.001 to 0.03 in every active recording. The paper's 0.1 group threshold therefore puts almost every recording in the Power-law group. Fitting only the top 30 or 100 ranks, or dividing rank by the number of PCs, does not separate early from late recordings either. I blocked the claims that need the 0.1 threshold on this b. This follows the protocol's chance-level rule by analogy: when your procedure is far from the paper's, block it as underspecified.

**Assumptions.**
- **DIV.** DIV = days since the dish's first recording + 2. The notebook also shows offsets of 1 and 3. fig1b's outcome changes if the offset is 1.
- **Local Moran's I.** The unnormalized form (M2) with slope against log PC index (L1). The Methods' surviving words define no variance term, and the 0.0001 threshold only selects anything under M2. Every reading is shown.
- **Continuity.** A day with no recording does not break a dish's run of activity.

**Questions for the authors** (recorded as `methods_unavailable` findings):
- How is b computed: the formula, the x variable, which ranks are fitted, and whether the error is on log or raw values?
- Is local Moran's I normalized by the variance, and which axis of the slope is logarithmic?
- How are cascades defined (pooled train? spikes or electrodes?), and what are the Figure S1 threshold and the Figure S2 method?
- What are the model's parameters (network size, weight scaling with g, run length, binning)?

**Questions to a reader:** none.

## 3. Protocol points

1. The claims file says to block a claim where readings disagree, but protocol step 1.6 allows adopting the best-supported reading as an assumption. I followed step 1.6 for M2 with L1 and recorded the conflict in the deviations.
2. Nothing in the protocol covers a fitted quantity whose scale cannot match a threshold the paper states. I used the chance-level rule by analogy: claims that need the threshold are blocked, and the threshold-free ones (correlations, trends) are tested.
3. Nothing covers a time axis with an unknown offset. I assumed an offset for claims that compare early and late windows, and blocked claims whose result is a DIV.
4. The step-2 clock check (decoding a contrast) does not apply to a single spike stream with no annotations. I recorded it as not applicable.
5. The rule that a claim depending on a blocked claim is blocked for the same reason applied to fig1f-exponent-1p2, even though the transition it needs is the same set of recordings whatever the DIV offset. I followed the rule.
6. Two rules about multiple readings pull against each other: "reproduced under any reading" (reader, step 3) and "the outcome is the one they all give" (step 1.6). I followed each criterion's own wording; for example, fig2d-shuffle-locality says "under each of" its readings.
7. Building the analyses meant extracting from all files once outside the notebook (6 minutes). Every recorded number comes from the notebook run.

## 4. Runtime and failures

The run went from 23:37 to about 00:18 UTC. The notebook took 396 s, with a peak of 2.8 GB per worker across 3 processes. Nothing failed.

The only untracked items besides my entry and attempt record are dotfiles and a `scripts` device node that were already in the checkout before the run; I left them alone.
