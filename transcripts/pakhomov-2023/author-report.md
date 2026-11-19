I finished steps 1 to 6. The entry is at `entries/pakhomov-2023`, the record is `attempts/pakhomov-2023-05.yaml`, and the handover package is in `executed/pakhomov-2023/handover/`. `entry.py all` passes: the notebook runs in 11.5 min with a 7.0 GB memory peak. Nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig3-field-simulation | blocked, data_missing |
| fig4-sham-no-uptake, fig4-unipolar-strongest, fig4-bipolar-weaker, fig4-twenty-fold-cancellation | blocked, data_missing |
| fig8-cancellation-predicts-targeting | blocked, data_missing (needs the Fig. 4 data) |
| fig5a-trains-stronger | partially reproduced (trains are not stronger at the e3 end) |
| fig5a-packet-center-enhanced | partially reproduced (the e1 end is not significantly above the centre) |
| fig5b-rotation-center-peak | reproduced, assumed (unpaired test) |
| fig5c-normalized-contrast | reproduced |
| fig6a-more-packets-more-uptake | partially reproduced |
| fig6b-peak-relative-to-periphery | partially reproduced |
| fig6-trough-half-of-center | partially reproduced |
| fig6-peak-narrower | reproduced, assumed |
| fig7a-amplitude-scales-uptake | partially reproduced (ratios about 6 to 7 in the main reading; the paper gives about 16) |
| fig7b-targeting-independent-of-amplitude | reproduced, assumed (fragile: no pair differs in only 26% of readings) |
| fig7cd-holds-for-large-array | reproduced, assumed |
| discussion-independent-of-array-size | reproduced, assumed |
| fig8a-equal-center-uptake | not reproduced |
| fig8a-more-uptake-near-electrodes | not reproduced |
| fig8b-packet2-best-targeting | not reproduced |
| fig9a-gap-reduces-periphery-more | partially reproduced |
| fig9b-gap-boosts-targeting | reproduced (541% at 2 mm) |
| fig9c-restricted-to-center | not reproduced |

## 2. The datasets, assumptions and questions

**What the data hold.**
- There are 70 files, each one stitched image of one dish. None holds the Fig. 4 single-cell time lapse or the Fig. 3 field maps.
- No file gives a pixel size, ROIs, electrode positions, array size or which needle is e1.
- 000686 and 000875 give the species as Bos taurus for CHO cells.
- Six dishes appear twice with identical pixels, each in two dandisets (000875 and 001025; 001025 and 001028). That fits their use in two figures; I used each in each figure.
- 001025 has 4 dishes at 2.4 kV (small array) and 2 at 4.8 kV (large array); the paper gives n = 3.
- 17 files hold an unexplained second channel.
- In 001027, the dishes labelled Packet 3 show the targeting the paper reports for Packet 2. With the Packet 2 and 3 labels swapped, the paper's 183/83/74% match within 10% under 15 readings. The labels may be swapped; I recorded this as a possible metadata error, not a proof.

**Assumptions.**
- Pixel size of 0.65 µm, from the paper's 10x objective and ORCA-Flash4 camera. It gives an 8.25 mm large-array diagonal against the paper's 8.4 mm.
- Electrode positions found from the dark needle footprints in each image. For electrodes lifted 2 and 3 mm, which leave no footprint, they come from needle marks in the second channel. Where both methods apply, the centres agree within 0.23 mm.
- e1 is the needle that is brightest in all the train dishes.
- Where the claims file's readings disagree, I adopted the first reading of each as the main one. For comparisons within the same dishes I used the unpaired test, because Methods 2.4 judges significance by the gap between error bars.

**Questions for the paper's authors** are in one `methods_unavailable` finding: ROI layout and width, how the centre was located, background subtraction and the a.u. scale, paired or unpaired tests, which needle is e1, and the LOESS span.

**Questions to a reader:** none.

I came across no earlier attempt. I saw that `claims/pakhomov-2023/` holds older per-dataset claims files and did not open them.

## 3. Where the protocol was unclear

1. Expected values may match "under one combination of readings", and the readings here give up to 576 combinations. Partial matches were then found in about 8 combinations. I followed the rule and reported the main reading and the share of readings that match.
2. The rule for tests says to adopt "the reading the paper best supports", but there are eight independent reading dimensions. I took the first reading of each together as the main reading, and the unpaired test, citing Methods 2.4.
3. fig6a's partial outcome only covers "rise at one or two places". Here the rise holds at all three places but the peak test fails for two treatments; I read that as partial.
4. "Stream, do not download": reading through remfile was too slow for 0.4 to 1 GB images, so each file is read into memory with HTTP range requests, never to disk. This is stated in the helper.
5. "Count each recording once" does not fit a dish legitimately reused across figures. I reported the pairs and used each in its own figure.
6. A blocked claim's `output` must be a cell tag; the protocol does not say so. I tagged the inventory cell `blocked`.
7. The clock check does not apply to single still images; the notebook says so.
8. Some expected values cover several groups ("Packets 1 and 3"); `measured` gives one value per group, with the order stated in the notes.

## 4. Runtime and failures

The work ran from 14:14 to 15:25 UTC, about 1 h 11 min. The full notebook took about 11.5 min and was run twice; the outputs are identical. Nothing failed in the entry.

One read-only `sed` command was denied by the permission system; I read the same file with the Read tool instead. The first check failed only because the blocked-claim output was not a cell tag; that is fixed.
