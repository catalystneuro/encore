# Round 3 verifier report: danish-2017-01

According to the attempt record (`danish-2017-01.yaml`), only one claim has a proposed change of outcome after round 2: `spectral-features-weak`, under `proposed` at line 318. No other outcome in the record has a `proposed` entry.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| spectral-features-weak | not_reproduced (rests on the approximate SAP features, assumed) | Yes | — | See below. |

## spectral-features-weak

**The numbers come from the data (cell 42).** `uva.load_ephys` computes the six features with `uva.sap_features` from each file's raw sound channel, at 1 kHz on the same time grid as that file's MUA, and cuts both to the same length (`uva.py`, `finish`).

- Windows run from 10 ms after each selected song syllable's onset to 10 ms before its offset. Introductory notes, calls and untitled segments are left out (`syl_mask`).
- The MUA is taken from the same window shifted 42 ms earlier (`m[a - 42:z - 42]`), as the criterion says.
- Pearson r is tested at 0.05/6 for each bird and pooled, under:
  - reading (a): per rendition
  - reading (b): per 1 ms bin
  - the z-scored variant: within syllable type, applied to (a) and pooled
- Every number in the record's notes and in the `proposed` reason matches the printed output of cell 42:
  - 9 of 18 bird-feature pairs significant under (a), 15 of 18 under (b)
  - pooled amplitude r = 0.156 (a) and 0.183 (b)
  - pooled gravity center r = 0.291 (a) and 0.082 (b)
  - Wiener entropy p = 0.06 under the z-scored variant
- Cell 43 now matches cell 42, including the Wiener entropy exception that I raised in round 2.

**The criterion is applied as written.** The claim counts as reproduced only if, under one reading, no feature passes in any single bird. It fails under both readings.

**The outcome does not depend on a choice made to reach it.**
- Both readings that the claims file allows were run, and both fail.
- The outcome does not even depend on the approximate SAP features. Amplitude is the feature that depends least on the approximations (10 log10 of the summed band power), and it alone breaks the single-bird condition:
  - reading (a): b871 p = 0.0074 and Uva4 p = 0.0012
  - reading (b): all three birds p ≈ 0
- The other approximations would only add failures to that. The Hann taper is used where SAP uses Slepian tapers, and pitch goodness and FM follow the helper's own forms.
- The pooled condition also fails under every reading. Under (a) and (b), pitch goodness, FM and Wiener entropy all pass, and under (b) AM passes too. Under the z-scored variant, gravity center does not pass (p = 0.013) and pitch goodness and FM do.
- `assumed` is justified because the claims file adopts the SAP definitions as an assumption, and the deviation states how the helper departs from them.

**Caveats (no effect on the outcome):**
- The single-bird tests use 317 to 2138 renditions and 31k to 257k bins per bird. At that size, correlations as small as r = 0.058 come out significant. The paper does not report its own n, so a difference in statistical power may explain part of the disagreement. The criterion has no effect-size floor, so that does not change the outcome.
- The z-scored variant is run only on pooled data, not per bird. That matches the claims file, which defines it as a variant applied before pooling.

**Claims file:** I found no place where it misreads the paper for this claim. Its criterion matches Results, paragraph 5: six features, windows 10 ms inside syllable edges, 42 ms latency, and Bonferroni over 6 comparisons.
