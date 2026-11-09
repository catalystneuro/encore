I checked the claims file against the paper and made eight corrections, including one new claim. The file is ready for an attempt.

**Checker result:** `43 claims, 43 quotes, 125 statistical values, 2 problems`. Both problems are values the checker could not match because of how they are printed: p 9.0e-4 (`figs2de-behaviour-increase-comparison`) and p 2.0e-4 (`fig4ij-pyramidal-modulation-increase`). I found both in the text ("p = 9.0e-4" in the fig. S2E legend and "P = 2.0 × 10 −4" in the Results), and both are right. The file passes schema validation.

I cloned the paper's code at the commit the file cites (d1922d1) and spot-checked the code details the criteria rely on. Most matched; the figs4b one did not.

**Changes, by claim:**
- **figs4b-pl-latency-distance:**
  - The criterion said the code does not define PL latency, jitter or the fitted segment, but it does. Latency is the mean over bootstrap draws of the peak-bin time; jitter is its variance in ms². Bins are 120 µm wide starting at 60 µm. The code fits latency on binned medians over 120 to 840 µm and jitter on the unbinned responses. These now come from the code, with the legend's "binned means" kept as the other reading.
  - The expected range was wrong: 0.235 ± 0.062 gives 0.173 to 0.297, not the 0.18 to 0.297 the criterion states. I set it to 0.2385 ± 0.0585.
- **fig3lm-deconvolved-spikes-subgroup:**
  - Added three effect sizes the text gives but the file left out (spike count week 0 r < 0.01, week 1 r = 0.08; onset week 0 r < 0.01).
  - Added to the statement the finding its own quote states: the subgroup's spike counts rise and onset falls from early to late, while the remaining neurons change little. The criterion now says how this is tested.
- **fig3n-newly-recruited-weaker:**
  - Two statistics were labelled "across groups", but the text attaches them to the newly recruited versus weeks 2 to 4 subgroup comparison. I relabelled them.
  - The expected "subgroup neurons at week 0" is now "week-0 group neurons", because the text and legend describe that group as all tracked neurons at week 0.
  - The criterion now says the paper does not state whether each printed P is the omnibus Kruskal-Wallis P or the post hoc pairwise P.
- **figs2de-behaviour-increase-comparison:**
  - Removed "over the same weeks as the controls" from the statement; it comes from the code, not the paper.
  - Late weeks 2 and 3 (the code) and late weeks 2 to 4 (Figs. 2C and 2E, which the legend says the data are reproduced from) are now both readings.
- **figs9a-coupling-700ms (new claim):** Fig. S9A reports its own tests and the Results cite it, but no claim covered it. The Results say it shows coupling among PL cells; the legend and code describe the Fig. 6F computation without Mouse 6. Both are readings.

**What remains open:**
- The fig. S2D and S2E sample sizes do not match Figs. 2C and 2E, although the legend says the data are reproduced from them.
- Several imaging claims rest on definitions the paper does not give, which the file takes from the code and lists as readings: dF/F, onset, and how the high-intensity subgroup is chosen.
- The paper does not give the control-animal currents for fig. S7.
- I did not re-read every code citation, only a sample.

**Ready:** yes. The `checks` entry at the end of the file records each change and these open problems, with `ready: true`. Nothing was committed.
