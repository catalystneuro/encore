I've worked through every point of the round-2 report and re-run all three notebooks; `entry.py check` reports 0 errors. Nothing is committed. One thing is not as asked: `python tools/entry.py all` got cut off at the tool's 2-hour limit. The classifier (47 min) and neural (54 min) notebooks finished, but the model notebook had not started, so I ran it on its own with the same environment and nbconvert command (37 min). As a result `entry.py` wrote no run stamp and `result.json` is stale, so the next `run` will execute everything again.

**Outcomes.** None changed; round 2 doesn't allow it. I proposed two changes for round 3:
- **fig9a** (optimal resolution): stays `reproduced`, proposed `partially_reproduced`. The final run is on a different machine from round 2, and at a few resolutions one sound's decision flipped. Under the (6b)(7b) readings the spectro-temporal maximum (81.5%) is now tied at 141 and 283 ms, with 81.0% at 100 ms. So no reading puts both optima on the reported points. 141 ms is one grid step from 100 ms, which meets the partial rule.
- **fig10** (vocalization against background): stays `reproduced`, proposed `partially_reproduced`. With the curves matched by duration instead of by window index, the temporal deficit is 23.2 or 24.3 points, outside 20 ± 2 under every reading. The trends with duration and the spectral advantage still hold.
- **fig9-spectrum**: still `not_reproduced`, now marked `assumed: true`.

**Added to the notebooks:**
- **Ties (fig9a):** every resolution tied at the optimum is listed, with two tie-breaks and a bootstrap over sounds. At each tied resolution I recomputed fig9a, fig9b, the rise times, fig9c and fig10. Two of them depend on the tie: at 283 ms the fig9c reduction is 25.6 points, inside its tolerance, and the fig9b order fails. The record says so.
- **Spectrum classifier:** the full-duration margins are printed; it exactly ties the temporal classifier (+0.0). The verifier also asked about its unstated component count. With 13 components, the count the Methods' cross-validation picks, the result is the same. With 5 it would meet the partial rule.
- **fig7i bandwidth variant** (the verifier's open point 8): this is now run. With the code's bandwidth formula the SI values barely move (0.717 and 0.358), so fig7i stays not reproduced.

**Corrected text:** I fixed every sentence the verifier quoted, in the notebooks, the record, the README and the findings:
- fig1k: "7 to 8 of 11" match, not "6 to 8".
- figs9: 3 of 32 reading combinations pass, and one of them also meets the per-paradigm rule.
- CDI: the squared-norm values are 2.4 to 7.7 times smaller, not "ten times".
- Run times now match the printed ones, in the README, `entry.yaml` and the record. The round-1 "38 min" is now "22 min in that run".

The round-2 verification is recorded for all 28 claims, with the verifier's reasons and my responses. I added no reader questions, because the verifier found no misreading of the paper.
