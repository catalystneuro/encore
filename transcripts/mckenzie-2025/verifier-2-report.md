**Verifier report, round 2: McKenzie et al. (2025) on DANDI:000552, attempt mckenzie-2025-01**

## 1. Outcomes

The claims file has 28 claims, and the attempt record has an outcome for each.

| Claim | Agree? | Assumption (`assumed: true`) stated and reasonable? |
|---|---|---|
| 13 photometry claims, ne-and-settling-time-course: blocked (data_missing) | Yes | n/a |
| ephys-ensemble-size: reproduced | Yes. Reading (b) gives 259.38, 191 to 363 (settling cell 16). | n/a |
| figs6b-decorrelation-novel: not_reproduced | Yes under E2. With time 0 at the first tracked frame, reading (a) gives p = 0.053 (cell 21). | n/a |
| figs6d-decorrelation-familiar: reproduced | Yes (cell 19) | n/a |
| fig7ab-umap-embedding: partially_reproduced | Yes (cell 24) | Yes. The measures come from the claims file, and the position is linearized because x, y is not in cm. |
| fig7e, fig7f, fig7g: reproduced | Yes (cells 28 to 31). fig7g is weaker than the paper: under E1 (b) with all bins p = 0.126, and on 7 sessions p = 0.089. It passes because the criterion asks for one combination. | Yes. 1 cm linearized bins, stated, and the (x, y) variant agrees where it can be run. |
| figs7ab-in-field-out-field: partially_reproduced | Yes (cell 35) | Yes |
| figs7cd-movement-not-time-locked: partially_reproduced | Yes. This now matches my round-1 rating. | Stated. The novel run fails in 14 of 16 readings, so the choice of reading does not decide the outcome. |
| figs7ef-time-explains-similarity: not_reproduced | Yes (cell 41, all 28 combinations) | n/a |
| figs7gh-unconditioned-similarity: reproduced | Yes (cell 44) | Yes. Reading (b) is degenerate. |
| fig8b-late-moments-reactivated: not_reproduced | Yes under E2 (reactivation cells 6 and 7). It would be reproduced under the first-tracked-frame variant (p = 0.0229). | The E2 dependence is stated. |
| fig8d-familiar-no-difference: not_reproduced | Yes as judged (familiar cell 5, p = 0.0134). The result is fragile: it is not significant with pooled shuffles (p = 0.56) or from the first tracked frame (p = 0.286). | Pool (a) is stated as the assumption. Reasonable. |
| fig8-no-pre-reactivation: not_reproduced | Provisionally. See remaining point (b) in section 3. | n/a |

## 2. Sentences the outputs do not support

- settling cell 26, and the attempt record's fig7ab notes: "R^2 0.185 to 0.717 against -0.194 to -0.108". Cell 24 prints 0.166 to 0.720 for the mapped sessions and −0.166 to −0.114 for the shuffled position (−0.081 for 211211b).
- Same places: from the first tracked frame, "0 or 1 of 8 over the seeds". Cell 24 shows 0/8 under every seed.
- Attempt record deviations (figs6b, fig7ab, figs7ab, figs7cd, figs7ef, figs7gh, fig8b) and settling cell 12: in e15-13f1-220118, e15-13f1-220119 and e16-3m2-211212 "only one reading can be run there". That is true only for the analyses that use position. Decorrelation, UMAP periphery and reactivation need no tracking, and the attempt itself runs them on the untracked open-field epoch of e16-3m2-211211.
- reactivation cell 12: "The rates found are low (0.1 to 0.3% of ripples per moment)". Session values in cell 6 run from 0.078 to 0.622.
- README: "ripples detected on the LFP of the raw files". For e13-26m1-211119 the LFP comes from the later version's behavior+ecephys file (reactivation cell 2).
- README: run times "About 25 minutes" for settling, and "About 40 and 25 minutes" for the reactivation notebooks. The notebooks print 21.5 (settling cell 47), 31.6 (reactivation cell 13) and 20.2 min (familiar cell 12). This is minor.
- Every other sentence I checked in the Result cells, the Summaries, the README and the record's notes matches the printed outputs.
- My round-1 reasons are restated faithfully in the record's verifications, mostly verbatim. The references to my problems are fair paraphrases.

## 3. Round-1 points

Resolved:
- 2 (E1 (b) for e16-3m2-211211). It is now run throughout, and cell 12 is corrected.
- 3 (reactivation readings not crossed). All six post and eight pre readings now run.
- 4 (sign-constrained model). Betas are now bounded at ±10, and the old form is kept as a variant.
- 5 (reading (b) degenerate). This is now stated, and the outcome rests on reading (a).
- 6 (ripples from the LFP). Detected ripples are now the main reading; 79 to 97% fall inside a deposited ripple.
- 7 (spike times compared). cell_types now compares them (cell 3).
- 8 (ensemble count conflict). Now recorded as the paper_inconsistency finding.
- Section C: epochs are printed for all sessions (cell 3), and streaming the LFP one channel at a time works.

Partly resolved:
- 1 (time 0). The first-tracked-frame variant is now run for every analysis except fig8-no-pre. E2 is kept as binding and put to a reader as a question. This is correct under the protocol, but fig8b and fig8d would flip, and figs6b reaches p = 0.053.

Remaining points that bear on a conclusion:
- (a) E2 decides fig8b and fig8d, as above. The claims file's reading of "transfer" as the start of the epoch still does not fit the data: tracking begins 14.6 to 63.3 s later.
- (b) fig8-no-pre-reactivation. The above-chance rate comes from minute 1.
  - In pre ripples, `late_pct` is at the false positive rate: novel mean about 0.096% (reactivation cell 10), familiar about 0.113% (familiar cell 9).
  - `early_pct` is about 0.10 to 0.28%.
  - The test averages only the 1200 moments of minute 1 and minutes 10 to 11. That is a stated deviation, but it gives minute 1 half the weight, and under E2 minute 1 includes the seconds before tracking starts.
  - The first-tracked-frame variant and the whole-run mean were not run for this claim. Either could change the outcome, at least in the novel run.
- (c) E1 reading (a) or (b) for e15-13f1-220118, e15-13f1-220119 and e16-3m2-211212 was not run for the analyses that need no position (figs6b, fig8b, fig8d, fig8-no-pre). I do not expect it to change an outcome.

## 4. Critical findings

Only finding 2 is rated critical: metadata_error, tracking of e16-3m2-211211 misfiled.

- **Notebook support:** `settling.ipynb` cell 10 (`finding-tracking-misfiled`) shows what it states:
  - tracking at 9575.3 to 11203.0 s, with 45 trials, inside the openField_thomas epoch (9559 to 12002 s);
  - spatial information as filed of 0.245 to 0.256 bits per spike at every shift, with no peak at zero;
  - after moving the tracking by 5564.5 s onto the linear_manu epoch, 0.656 at zero shift against 0.252 and 0.271 at ±30 s;
  - in the later version, the linear_manu tracking at the same times.

  Cell 9 supports "every other run peaks at zero shift".
- **Versions:** the finding lists 0.230630.2304 and 0.261113.1035, with no `fixed_in`.
  - In the pinned version, the spatial-information test shows the problem directly.
  - In the later version, the outputs show identical timestamps (cell 10) and identical spike times (cell 3), so the problem carries over. The spatial-information test itself was not re-run on the later version's file.
- **Rating:** `critical` is right. Position and trials are filed at the wrong time relative to the spikes, and nothing in the pinned files reveals it. An analysis that takes them as given pairs open-field spikes with linear-track positions.
