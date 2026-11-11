I've built and run the entry, written the attempt record, and produced the handover package. Of the 37 claims, 22 reproduced, 12 partially reproduced, 2 did not reproduce and 1 is blocked. Nothing was committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| fig2ab-fms-smf-not-discriminated | partial (only 5 of 8 rats in the data; 62SC is missing) |
| training-days | partial (fewest days is 11, not 8) |
| fig2c-choice-follows-mean-speed | reproduced |
| fig2d-fixed-panel-impairs | blocked, data_missing |
| dprime-fff-sss-range | partial (highest is 1.09, not 1.5) |
| fig3-fsfs-sffs-intensity-only | reproduced (from the paper's S1 Data) |
| units-recorded | reproduced (but 506 units, not 473) |
| baseline-rates | partial (highest RS layer mean is 11.4 Hz, limit 11) |
| temporal-modulation-count | reproduced (310 units) |
| modulated-higher-baseline | reproduced |
| fig4d-evoked-modulation-by-layer | partial (best reading gets 4 of 5 layers) |
| latency-by-layer | partial (layer order holds, values are 14 to 20 ms) |
| fig4d-gradual-decrease | not reproduced (L5a also decreases) |
| fig6-regression-significant | reproduced (194) |
| fig6e-unit-classes | partial (51 Slow Negative units, limit 48.4) |
| fig6fg-laminar-classes | partial (4 of 6 values) |
| fig7c-fast-impulse-velocity, fig7c-fast-sequence-rate | reproduced |
| fig7-fff-adaptation | partial (test selects 34 units, not 61; only pulse 2/1 significant) |
| fig7-sss-no-adaptation, s4-fms-middle-pulse | reproduced |
| fig7de-medium-suppressed | partial (no suppression), rests on an assumption |
| fig8a-slow-positive-no-sequence-difference | partial (S impulses also evoke a response) |
| fig8b-slow-negative-no-impulse-response | reproduced |
| fig8d-slow-positive-right-choice-l5 | partial (L5b only), rests on an assumption |
| fig8d-fast-medium-no-choice-bias | reproduced |
| fig8e-choice-divergence-125ms | reproduced (122 ms), rests on an assumption |
| s5-slow-positive-no-integration | reproduced, rests on an assumption |
| s6-head-position-choice | reproduced (from S2 Data) |
| s7-no-fs-l5-slow-positive | reproduced |
| fig9b fast/medium, fig9c, fig9b slow-chance, fig9d, fig9e, fig9g | reproduced |
| fig9f-choice-decoder | not reproduced (Slow units 80 to 92%, not 65%; Fast/Medium 67 to 79%, not near chance) |

## 2. What was found about the dataset

- **Version:** the data set is one file, `AllRats.mat`, under `ssc-4/live/`. It is pinned as `unversioned` with the MD5 sum from the data set's `checksums.md5`; it is the only copy in the bucket.
- **Column map missing:** the descriptor says to drop units in columns A1 and B2 using a `MapPosition` field, but the file has no such field. So 33 units beyond the paper's 473 cannot be removed, and every unit analysis uses all 506.
- **Stored p-values:** the deposited temporal-modulation p-values were computed over -50 to 300 ms, not the Methods' 0 to 180 ms after nose-poke entry. My recomputation gives the same count (310) but agrees unit by unit for only 73%.
- **Trials used by the authors:** the deposited regression inputs equal spike counts summed over completed trials, and the deposited R² and p reproduce exactly. That settles which trials the paper analysed.
- **Not deposited:** the fixed-panel sessions and three behaviour-only rats (62SC, 107Si, 62SS). Rat 18FB's per-rat values differ from S1 Data by up to 0.026; the other four rats match exactly.
- **Checks passed:** no recording is deposited twice, and spikes and trials share one clock (impulse-2 timing contrast, 61 of 80 sessions; weak in rat 18Ro).

**Assumptions:**
- Downstream claims use my own recomputed unit classes. They agree 99.6% with the deposited labels where both mark a unit as modulated. The deposited labels are shown as a variant. Four claims are marked `assumed` because that variant would change their outcome or the reading matters (fig7de, fig8d-L5, s5, and fig8e, where the third impulse is taken to end at 150 ms).
- The choice decoder weights right and left equally in training, since the paper gives chance as 50%. The unweighted fit is shown; it does not give the claim either.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which window and statistic the temporal-modulation test used.
- Which test selected the 61 F-responsive Fast RS units. A paired t test gives 34; all Fast RS units number 63, and with those the FMS/SMF test gives p = 0.087 against the paper's 0.08.
- How the 65% choice-decoder accuracy was obtained.
- How peak latency and evoked modulation were computed.

**Question for a reader** (`questions/mcguire-2016.yaml`): should fig2d be marked `data: elsewhere`? The paper's S2 Data holds the per-rat values; tested as a variant there, they give p = 0.012, matching the paper.

## 3. Where the protocol was unclear

1. `archives.md` describes CRCNS data sets as zip files; this one is a single MATLAB file. I streamed it with fsspec into `scipy.io.loadmat` in memory.
2. The protocol does not say whether the author may treat a claim's `data` field as part of the claim. Here fig2d's data are public in S2 Data. I left the field as written, blocked the claim, showed the S2 Data test as a variant and asked a reader.
3. It is silent on whether the data set's own stored analysis results (labels, p-values) or a recomputation should select units for dependent claims. I recomputed, showed the stored labels as a variant, and marked `assumed` where the outcome depends on it.
4. It does not say which reading of an upstream claim feeds the claims that depend on it. I adopted one, recorded it as a deviation, and flagged the outcomes it changes.
5. `measured` is defined for when a reading matches, not for when none does. I recorded the closest reading and said so in the notes.
6. It does not say whether an expensive reading may run with fewer repeats. The cross-validated decoder reading ran with 5 to 10 repeats instead of 300 to stay within the runtime limits; I recorded this in the notebook and the deviations.
7. The suggested clock check (decoding a task variable around trial start) did not fit well. I used a contrast of impulse-2 onset times between sequences, plus a pre-onset control window.

## 4. Runtime and failures

The run took about 1 h 10 min (16:54 to about 18:03 UTC). In the clean run the main notebook took 106 s and the decoder notebook 925 s, both passing; `entry.py check` reports 0 errors and the handover is in `executed/mcguire-2016/handover/`. During development there were only small script errors, all fixed before the final run; nothing failed in it.
