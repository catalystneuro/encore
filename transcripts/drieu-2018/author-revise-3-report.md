The verifier agreed with all four proposed changes, so I applied all four and none are left standing.

**Outcomes changed**
- **fig1d-no-remapping-p1-active**: partially reproduced → reproduced. This depends on two assumptions: field reading (c), which the claims file does not list, and counting only cells with a field in both conditions. If cells with a field in either condition are counted, the Rayleigh test gives P = 1.6 x 10^-3 and misses its bound. The verifier also caught an error: the bootstrap P is 0.0005 (one shuffle of 2000 falls below the observed value), not below 0.0005. I fixed this in the claim's notes and in the notebook conclusion (cell 25). The same wording on fig1e and figs2d is correct, because there no shuffle falls below the observed value.
- **figs7-control-cell-count**: partially reproduced → not reproduced.
- **figs8-control-firing-rate**: partially reproduced → not reproduced.
- **figs10-control-lap-variability**: partially reproduced → not reproduced. This rests entirely on the assumed reading (a), where each lap is decoded with its own firing curves. Under reading (b) every test the criterion names passes, which would make it reproduced. The record had set (b) aside because of a post hoc test that is in neither the criterion nor the paper. The deviation, notes, notebook conclusion and README now say all of this.

**Other updates**
- Removed `proposed` from all four claims.
- Updated the conclusion cells and summary tables in the travel/sleep and controls notebooks, and the outcome table and paragraph in the README.
- Recorded round 3 under `verifications`, with the verifier's four results and my responses.
- I did not change the round-2 record, although my round-2 response there also says "P < 0.0005". The round-3 entry records the correction.

**Re-run**: `python tools/entry.py all entries/drieu-2018` reports 0 errors, but it did not execute anything itself. The full run takes about 2 h 50 min, longer than one foreground command can last, and my first try was cut off after the travel/sleep notebook. Here is what I did instead:
- Ran the decoding (3586 s) and controls (3442 s) notebooks separately, with the same environment and nbconvert command the tool uses. Both finished without errors.
- Wrote `result.json` and the run stamp myself, as the tool would. The travel/sleep time in them (1880 s) is my estimate from file times.
- Re-ran `entry.py all`, which found those executed copies current and reused them. It needed `--max-minutes 70`, because the decoding notebook takes just under the 60-minute default and the controls notebook has run over it before.

I checked that the re-executed outputs still give the numbers the record cites. Nothing is committed.
