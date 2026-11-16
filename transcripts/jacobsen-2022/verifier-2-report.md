**Verifier report, round 2: jacobsen-2022-01**

The claims file has 28 claims. The attempt record has 28 outcomes: 7 tested, 19 histology claims blocked (data_missing) and 2 imaging claims blocked (data_missing). Cell numbers below refer to the re-executed notebook, which has 39 cells.

**1. Outcomes and assumptions**

| Claim | Outcome | Agree | Assumption (`assumed: true`) |
|---|---|---|---|
| fig5c-functional-cell-types | reproduced | Yes | The standard shuffle (shifts of at least 20 s). It is stated and reasonable. Cell 14 shows that the literal shuffle's 95th percentile for T4 C16 is 0.762, against an observed 0.912. The outcome rests on this choice: under the literal shuffle T4 C50 scores 0.656 against a threshold of 0.663 (cell 13). |
| fig5c-responsive-grid-cell | reproduced | Yes | None needed. T1 C89 is a grid cell under both shuffles and is responsive under reading (a) (cell 18). |
| fig5c-example-cells | reproduced | Yes, with the caveat already given | Choosing a laser epoch per cell on day 17. It is stated, and the record says plainly that this goes beyond the criterion. With the epochs pooled, T1 C52's latency is 2.358 ms against a floor of 2.385, which would make the outcome partial. I accept it because of the four-digit matches. |
| figs3-stable-input-cell | partially_reproduced | Yes | Two assumptions: the six units are the same cell, and the open field is the whole position series. Both are stated and reasonable. Under the first-1800 s reading all 18 values match (cell 26). Not adopting that reading is defensible, since it was found from the expected values. |
| figs4-nonresponsive-cells | partially_reproduced | Yes | The head direction score is taken as the tuning-map mean vector length (MVL) with the archdata parameters. It is stated and reasonable. Cell 29 shows the result does not depend on that choice: no tuning setting puts both the peak rate and the MVL within tolerance of 9.02 Hz and 0.81. |
| responsive-cells-at-19-days | reproduced | Yes | None needed. |
| mec-inputs-from-two-weeks | reproduced | Yes | None needed. The record states that the test cannot fail on the early side. |
| 19 histology claims and 2 imaging claims | blocked (data_missing) | Yes | None. |

I found no place where the claims file misreads the paper. I checked the STAR Methods text for the latency and fidelity definitions, "approximately 30 min" and "10 Hz continuously".

**2. Sentences the printed outputs do not support**

- The first TTL event lasting "0.6 to 1.9 s" (cell 4, Summary in cell 37, the record's `format_error` finding, helper docstring). No output prints this range. Cell 22 prints only the two day-17 events (809.6 and 1523.6 ms). Cell 3 prints only how many events per file are longer than 5 ms.
- Cell 6: "The LFP timestamps run backwards 3 or 4 times within each file". Cell 5 prints 2 for both day-15 files. The record's finding ("2 to 4") is correct.
- Summary (cell 37): "`waveform_mean` ... holds values with peak-to-trough 31 to 41". This is printed only for the six 70375 units (cell 25: 30.63 to 41.04). The record limits it to 70375 correctly; the Summary reads as if it covers all units.
- Cell 27, the record's figs3 notes and the record's response to round 1 all present the "first 275 pulses of each session" variant as matching. Cell 26 shows that for day 15 session 1 (278 pulses) the variant moves the fidelity off the exact printed value (68.71% with all pulses, 69.09% with the first 275). So the paper did not apply a uniform first-275 rule. The day 14 session 2 selection remains a one-off; the outcome is unchanged.
- README: "It takes about four minutes". Cell 38 prints 106 s, of which the shuffles take 42 s twice (cells 12 and 14).
- README table: figs3 and figs4 lack "(resting on an assumption)", although the record sets `assumed: true` for both and cells 27 and 30 say so.
- The record's verification reasons still cite the round-1 cell numbers (11, 14, 16, 19, 21, 23, 25). In this notebook the corresponding cells are 13, 18, 21, 26, 29, 32 and 35, so a reader following those references lands on the wrong cells.

All other sentences check out. That covers the Result conclusions (cells 16, 19, 23, 27, 30, 33, 36), the rest of the Summary (including "8 of the 9 printed latencies within 0.01 ms" and "no rate moved by more than 0.001 Hz except day 14 session 2"), the README outcome rows, and the record notes and measured values.

The record's reasons state my round-1 points accurately and in substance. They are a light third-person paraphrase that keeps my numbers and reasoning. Nothing is misattributed.

**3. Round-1 points**

Resolved:
- B1: corrected in cell 0, and cells 9 and 10 list the assets of every version.
- B4: the open-field assumption is now stated, and the first-1800 s reading is run for all 12 units with no change of class.
- B5: as far as the data allow. The 48-setting tuning sweep is in cell 29, the MVL definition is fixed, and a question goes to the paper's authors.
- B6 and B7: stated in the conclusions.
- B8: stated in the helper docstring.
- B9: no change needed.
- From section C: the shuffle sentence of Rowland et al. (2018) is now quoted, the shuffled MVL distribution is shown, and the per-epoch spike counts for day 17 are printed.

Documented but still open; each bears on a conclusion:
- B2, fig5c-functional-cell-types: the border class still depends on the shuffle reading. The question goes to the paper's authors.
- B3, fig5c-example-cells: the per-epoch choice still decides reproduced against partial. Nothing in the file distinguishes the epochs except the firing rates per epoch (cell 22: T1 C57 12.72 against 9.93 Hz, T4 C16 2.32 against 0.37 Hz). The conclusion does not mention these rates, and they do not establish laser power.
- figs3: the outcome depends on how much of the open field is used, and the day 14 session 2 selection is undocumented (see section 2).
- figs4: what quantity the paper's "head direction score" of 0.81 is, and what gives the 9.02 Hz peak rate.

Not resolved and not affecting a conclusion: I still cannot view the rendered rate maps. Cell 15 now prints their ranges, and the grid and border calls rest on the printed scores.
