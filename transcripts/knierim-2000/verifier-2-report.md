## Verifier report, round 2: Knierim, McNaughton & Poe (2000), dandiset 001754 @ 0.260728.1352

The claims file has 10 claims, and the attempt record gives an outcome for each of them. All cell indices below refer to the re-executed notebook.

### 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| flight-spatial-code | blocked (methods_underspecified) | Yes. Cell 39: the dependencies are partial, blocked and reproduced, so the rule could give not_reproduced or partially_reproduced. |
| si-comparable-to-preflight | partially_reproduced | Yes. Cell 29: p is 0.88 and 0.66, and no reading puts both means within tolerance. |
| si-rat1-fd9-vs-preflight | blocked (methods_underspecified) | Yes. Cell 32: p is 0.50 against preflight ES and 0.0055 against preflight MC. |
| si-rat3-fd4-vs-preflight | reproduced | Yes. Cell 35: p is 0.28 and 0.77, and both means are within tolerance under the ES reading. The counts are off (11 against 7, 38 against 24), but the rule does not use counts. |
| fd4-abnormal-selectivity | partially_reproduced | Yes, by the criterion. Cell 42: the drop holds for rat 2 under both readings (p 0.0006 and 0.0015) and for rat 1 under neither. The rat 2 caveat remains (see 3). |
| fig3-stability-across-sessions | not_reproduced | Yes. Cell 46: tying each map to the unit it best matches leaves four units tied to two session 3 maps, and three of them belong to active session 2 maps. The criterion's condition fails, so M-a is not run. Cell 45: under M-b, (a) 6 of 16 and (b) 1 of 16 cells keep their field, neither more than 8. |
| direction-selectivity | blocked (methods_underspecified) | Yes. Cell 49: position exists only at spike times, there is no occupancy by direction and no track layout. The criterion fixes the label. |
| theta-normal | blocked (data_missing) | Yes. There is no ElectricalSeries or LFP (cell 3). |
| ripples-normal | blocked (data_missing) | Yes, as for theta-normal. |
| three-orthogonal-surfaces | not_reproduced | Yes. Cell 54: fig3 is not reproduced, and the criterion then gives not_reproduced whatever part (ii) gives. |

**Claims file:** I found no misreading of the paper. The Fig. 3 legend ("same seven cells", "the fourth cell lost its field", "a few other cells (not shown) gained a field") is rendered faithfully.

### 2. Sentences the printed numbers do not support

- **Cell 30, and the record's notes for si-comparable-to-preflight:** "p < 1e-6" and "(p below 1e-6)". Cell 29 prints p only to four decimals, as 0.0000, which supports p < 5e-5 and nothing smaller. This is a variant and decides nothing.
- **Cell 48:** "the NASA record (below) lists no continuous position". The same claim is in the record's notes for direction-selectivity: "the names of the files in the NASA record (OSD-968) show no continuous position". Cell 51 prints only the file names and, for each zip, how many entries have an EEG-like name. It prints no entry names and does not search for position, so nothing printed supports the statement. No outcome depends on it, because the claims file names no outside data.
- **Record notes for fig3-stability-across-sessions:** "Each distinct deposited map of session 2 (19) … was tied to the unit of its tetrode". Cell 44 says the same ("ties every distinct map of session 2 and of session 3"). Cell 46 prints "ES1: 19 distinct maps, 17 with a unit of their tetrode", so two session 2 maps are tied to no unit. All 11 active maps are tied, so the outcome is unaffected.
- **Cell 23:** the trace behaves as Rat2's position in Rat2's FD9 window, "and not in Rat2's FD4 ES window". This is stronger than the outputs support. Cells 19 and 21 show only that no attribution could be made (0 of 17, 1 of 16), and cells 20 and 22 themselves say it "could not be established" and "remains unknown".

Everything else checks against the outputs: the other Result paragraphs (cells 33, 37, 40, 43, 47, 55), the Summary (cell 58), the README, and the record's notes, findings and header.

My round-1 reasons are stated faithfully in my own terms for all 10 claims. The fd4 reason correctly folds in B2, and the fig3 reason folds in B1 and my "if the condition fails … not_reproduced". The "reviewed" text is also accurate: all 10 outcomes agreed with the record as it then stood, and I flagged a possible not_reproduced for fig3.

### 3. Round-1 points

**Resolved**
- **B1 (fig3 pairing):** The check now ties every map in both sessions to the unit it best matches, which is the direction the criterion states. It flags conflicts both ways and fails in session 3 (cell 46). The outcome moved to not_reproduced, as I predicted, and three-orthogonal-surfaces followed.
- **B3 (maps with `cell_number` −1):** Cell 26 now lists every active map. In flight, the active −1 maps outside Rat3 FD4 match a single unit (median r 0.555, against 0.595 for numbered maps). They also match one unit better than the tetrode's summed spikes in 94% of cases. Leaving them out changes no test. Two parts cannot be checked: the preflight −1 maps (there is no preflight position), and the variant for rat 3's flight side, where every map is −1.
- **C (requested outputs):** All are supplied. The contrast I asked for, at timestamps where the Rat1 and Rat2 traces differ, turns out to be moot: the two files hold the same trace in Rat 2's FD4 window (4 of 707 positions more than 2 px apart).

**Remaining, bearing on a conclusion**
- **B2 (fd4-abnormal-selectivity):** The outcome rests entirely on Rat 2's low FD4 information. Whether the position trace in that window is Rat 2's is still unknown: 0 of 17 units are selective on the Rat2 file's copy, against 12 of 28 on FD9. The criterion sets no condition on tracking, so the outcome stands by its rule, but its only support may come from tracking rather than firing.
- **fig3, and through it three-orthogonal-surfaces:** Both outcomes now rest on M-b alone, which uses unsmoothed 4-px maps with few spikes per bin. My B5 now bears on these outcomes: reading (b) almost never passes on such maps (cell 45: 2, 1, 0 and 0 cells at thresholds 0.1 to 0.5). The counts are also off: "more than half" is taken of 16 units against the paper's 7, and nothing identifies the paper's 7. This follows the criterion and is not an error, but these not_reproduced outcomes come from a reading that is weak by construction.
- **Cell selection:** Counts differ from the paper's in most comparisons, for example 11 maps or 16 units against 7, and 38 against 24. Rat3's reproduced outcome and Rat2's partial outcome come from cell sets that are not the paper's. The criterion's rules do not use counts.
- **Unchanged and not deciding anything:** B4 (M-b spikes in unvisited bins are dropped), B6 (Rat 2's preflight and flight units share no tetrode), and the unknown smoothing kernel.
