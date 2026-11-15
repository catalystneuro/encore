I've done steps 1 to 6: the entry is at `entries/martinez-conde-2019/`, the record at `attempts/martinez-conde-2019-02.yaml`, and `tools/entry.py check` and `all` report 0 errors. The handover is in `executed/martinez-conde-2019/handover/`. Nothing is committed. I did not see any earlier attempt, by accident or otherwise.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| neuron-counts | not reproduced (53 cells; 22/29/26 maps per stimulus against the paper's 25/30/28; 7 cells in all three stimuli matches) |
| spikes-per-condition | blocked, data_missing |
| s4-baseline-no-difference | not reproduced, rests on an assumption |
| fig4a-above-baseline | reproduced |
| fig4b-spike-rate-difference | partially reproduced, rests on an assumption (order holds; S90 is 8.21, just below its tolerance) |
| fig4b-pairwise-significance | reproduced |
| fig5-average-maps | reproduced, rests on an assumption |
| table1-edge | not reproduced |
| table1-p180 | partially reproduced |
| table1-s90 | not reproduced |
| table1-s52 | partially reproduced, rests on an assumption |
| table1-s40 | reproduced |
| fig6-midpoint-representative | reproduced |
| fig7a-rms-contrast-fit | not reproduced |
| fig7c-fold-edge-equivalence | not reproduced |
| fig7c-fold-edge-significance | reproduced |
| fig7d-nonlinear | reproduced, rests on an assumption |
| fig7d-dog-similar | blocked, data_missing |
| s3-latency-peak | blocked, data_missing |

## 2. Dataset, assumptions, questions

What the dataset holds:
- **Counts.** One zip holding 77 rate maps for 53 cells. The spreadsheet lists 58 cells, but 5 of them have no files.
- **Registration.** Only 60 maps carry `Standard`, the authors' map registered to the stimulus, which the data descriptor does not mention. Placing a map on the stimulus needs the receptive-field position, which no file stores, and it differs between experiments of the same cell by 11 to 58 DU.
- **Star neurons left out.** Because of that, the 17 Star maps without `Standard` cannot be registered, and the Star results rest on 12 of the paper's 30 neurons.
- **Units.** The descriptor calls `image` raw spike counts; it is actually a rate (spikes per 1 ms sample of eye time).
- **Smoothing.** The stored smoothing is close to a Gaussian with SD 5 DU, not the 7 DU in the Fig 3B legend.
- **Undocumented baseline.** The files' `BaseActivity` is not documented, does not match the paper's baseline squares, and is exactly 0 in two files.
- **Missing data.** The files have no spike counts, eye times (except in one file), spike times or eye positions, which is what blocks the spike-count and latency claims.

Assumptions:
- **Baseline square positions.** For Square and Edge and for Star, I put the squares inside the corners of the circumscribing square, because centred on the corners they fall outside the region analysed. The paper gives no positions for the two Corners squares; I used the two bottom corners of that region, the only 0% luminance band in it. The files' `BaseActivity` is run as a variant.
- **Which S40 fold is bright.** I picked it from the stimulus image as the fold where luminance peaks; it is the same fold in all 26 Corners files.

There are three `methods_unavailable` questions for the authors: where the baseline squares are, how RMS contrast is defined (their reference [21]), and which test and order of summary lie behind S4 Fig and Table 1. I asked no reader questions.

## 3. Protocol gaps

1. The protocol has no spatial version of the "same clock" check for map-only data. I compared each neuron's response along the Edge with the same band shifted sideways (16 of 22 neurons peak on the Edge) and reported it as consistent with registration, not proof.
2. It is unclear whether the data set's own undocumented baseline counts as the paper's method. I kept the paper's squares as the main reading and showed `BaseActivity` as a variant; the outcomes are marked as resting on the assumption wherever the two disagree.
3. The `assumed` flag does not say whether an assumption the claims file itself names (for example the non-linearity rule in fig7d-nonlinear) counts. I set `assumed: true` in those cases.
4. For "record the first reading" when no reading matches, the protocol gives no rule. I recorded reading (a), halves (i) for S90.

## 4. Runtime and failures

The notebook runs in about 73 s with 0.51 GB peak memory, and the whole session took about 35 minutes. Nothing failed.
