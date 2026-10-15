I've finished steps 1 to 5 and run the handover (step 6). The entry is `entries/001616-gerken-2025/`, with `claims/001616/10.7554-elife.106758.1.yaml` and `attempts/001616-gerken-2025-01.yaml`. It is locked, `check` reports 0 errors, and two clean runs gave identical numbers. I used the full text of the eLife reviewed preprint v1, which is open access, plus its supplement. The pinned version is 0.260702.0824: the paper cites no DANDI version, this is the newest published one, and it holds each recording once.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| dataset-composition | partially reproduced (totals match; EC, PHC and PIC unit counts differ) |
| fig2b-phc-camera-cuts | blocked: methods_underspecified |
| tables1-camera-cuts-regions | blocked: methods_underspecified |
| fig2b-phc-scene-cuts | blocked: methods_underspecified |
| tables1-few-semantic-responses | blocked: methods_underspecified |
| tables1-no-indoor-response | blocked: methods_underspecified |
| results-cluster-regions | blocked: methods_underspecified |
| fig3b-single-neuron-threshold | reproduced |
| fig3c-logreg-characters-location | reproduced (Summer 0.302, Indoor/Outdoor 0.360) |
| fig3c-logreg-cuts-lower | reproduced (scene cuts 0.0745, camera cuts 0.0967) |
| fig3e-temporal-gap | reproduced (logistic regression in place of the LSTM; random split 0.947) |
| fig4-patients-below-pooled | reproduced |
| fig4-named-patients | reproduced (7 of 8 named patients above 0.2) |
| fig5-region-decoding | partially reproduced (3 of 4 orderings hold) |
| fig6-responsive-subsets | blocked: methods_underspecified (all 4 conditions hold, but it depends on the responsive test) |
| fig7b-top500-overlap | partially reproduced (97 shared units against the paper's 78; chance is 1.14) |
| fig3c-lstm-decoding, fig3d-temporal-shuffle, fig5-faces-presence, fig7a-500-neurons | blocked: methods_underspecified (the LSTM is not published) |

The six responsive-unit claims are blocked because the Methods' test, as written, is badly miscalibrated here. It flags 68% of units as responsive at random event times, and 100% of synthetic Poisson units when there are 883 events.

## 2. What was found about the dandiset

- **Totals match:** 29 patients, 17 female, 2286 units, 30 to 137 per patient.
- **Region counts differ from the paper**, and there is no mapping between them:

  | Region | Dandiset | Paper |
  |---|---|---|
  | A | 559 | 580 |
  | H | 846 | 794 |
  | EC | 493 | 440 |
  | PHC | 293 | 373 |
  | PIC | 68 | 99 |
  | Other (FF, LG, PRC) | 27 | not named |

- **Units:** spike times are stored in milliseconds, not the seconds NWB requires. The patient-aligned annotation columns say seconds but hold milliseconds.
- **Labels:**
  - The face labels lack the "excluded" state the Methods use.
  - There are 958 camera cuts (one every 5.25 s); the supplement says one every 3 s.
- **Versions:** the earlier version 0.260519.1133 holds 28 recordings twice, as older copies with identical spike times.
- **Dataset code (GitHub mormannlab/SUMMER @59fc242):**
  - It selects responsive units with the ZETA test, not the Methods' test. ZETA is calibrated here and gives 12.6% of PHC units responsive to camera cuts, against the paper's 51.7%.
  - Its training loader selects no hippocampal units, because no unit is labelled `H`.
- **Paper inconsistencies:** the responsive threshold is alpha 0.01 in the Methods and 0.001 in the Results. The patients' ages are 22–63 in the Results; the files have 19–62.
- **Clock check:** spikes and annotations look aligned. PHC firing rises 200–300 ms after cuts, and decoding with labels shifted by 300 s falls to kappa 0.016. Per patient, the alignment is shown for 12 of 29.

## 3. Points where the protocol was unclear or did not fit

1. **Chance-level rule.** It covers "a chance level or false-positive rate the paper states". The paper gives only the alpha, and I treated that as the stated false-positive rate. The responsive claims ran but are blocked. This includes an absence claim, which the protocol otherwise says to judge on the paper's test as written.
2. **Blocked claims that depend on blocked claims.** The rule blocks fig6 and the cluster claim even though their analyses ran. I blocked them and kept the numbers in the notes.
3. **Several readings vs one main choice.** The paper gives two alphas. I treated both as readings, and used 0.001 alone for the absence claim, since it is the threshold in the same Results paragraph.
4. **Data check vs claim analyses.** I saw one fold's Summer kappa while timing the model, before writing the criteria. I disclosed it in the claims file's opening comment.
5. **Reference values from code.** The protocol has no slot for these. The code's printed LSTM values per gap and region are listed under `inputs` and used only for comparison; all claims are `data: dandiset`.
6. **Tolerances.** For small proportions I used the 95% binomial interval instead of 10%. For the logistic regression I used the paper's LSTM SEM, since none is given for the regression. Both are stated in the claims file.
7. **Substitute model.** For claims stated about the LSTM, the protocol does not say whether a substitute counts as tested. I tested three with the paper's own logistic regression and recorded it as a deviation.
8. **Region claim (fig5).** The regions themselves differ from the paper's. I judged on the dandiset's regions and recorded it as a deviation.
9. **Data-check claim tag.** The protocol gives no claim tag for a data-check claim, so I pointed dataset-composition's `output` at the `sanity` cells.

## 4. Runtime and failures

- The notebook takes 22 minutes on 4 cores, over the 10-minute aim but under the 30-minute CI limit. Most of the time is about 285 logistic-regression fits and the ZETA variant.
- The ZETA variant uses 100 resamplings instead of the code's 1000, for time, and covers PHC units only.
- During development, an off-by-one in the bin labels and an impossible size-matched draw broke the run; both are fixed. A first version of the per-patient clock check cancelled out across regions and was replaced.
- `git status` shows dotfile names (`.bashrc`, `scripts`, and others) at the repo root. They are sandbox device mounts, not files I created.

Nothing was committed or pushed.
