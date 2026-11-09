The claims file for 000774 is ready for an attempt. I corrected eight claims; three questions stay open because the paper doesn't settle them.

**Checker:** `42 claims, 42 quotes, 66 statistical values, 0 problems`. It said the same before my edits (62 values then; I added four).

I checked the claims against the paper's text, the supplement legends, and the paper's code at the cited commit (`denmanlab/estim_populations` c4aaa608). The code outputs the file cites matched in every cell I opened. One statistic I suspected was wrong is right: polarity p = 0.086 in `figs1b-saturation-polarity` comes from the Figure S1B legend, so I left it.

**Changes, by claim**
- **fig2g-extent-increases:** added the Figure 2G legend's amplitude result (p < 0.001) next to the Results value (p = 0.002).
- **fig2g-extent-sublinear:** the criterion now says the distances are CCF distances. It gives the code's printed R² values (deep 0.16 linear, 0.17 quadratic). It also runs the Figure S2F legend's peak-aligned fits (0.02 and 0.20) as a second reading.
- **fig3fg-anisotropy-strength:** "the code appears to group monopolar against bipolar" now says what code cell 35 does. It groups them that way, and that grouping gives the printed F values.
- **figs3cd-gmm-window:** the baseline window length had been chosen by the writer. The paper leaves it open, so the criterion now names two readings.
- **fig4h-ks-distinct:** the statement said all other amplitude pairs did not differ, but the paper prints no value for 5 against 50 µA. The statement and criterion now name the four pairs it does report. I added the three missing adjusted p-values, and 5 against 50 µA is reported but not judged.
- **fig5ef-polarity-clusters:** the criterion now says its half-maximum rule for labelling clusters is not from the paper. The outcome rests on the cluster fractions matching.
- **figs6b-fsrs-early-firing:** the criterion called the KS test's inputs open and offered a first-spike-latency reading the paper doesn't support. The code (cells 62 to 67) settles it, and I rewrote the criterion from the code. The legend says 2 ms bins and the code uses 1 ms, so both are run.
- **fig6g-dimensionality-collapse:** I removed the requirement "below 1 in at least 7 of 9 recordings", which no source gives. The criterion now names the legend's 5 ms bins next to the 2 ms used by the Methods and the code. "Transient increase within 20 ms" is now open between the mean over that window and its largest bin.

**Still open**
- Table S1 (the statistics table) is not in the text read. So `figs10e-reaction-times` has no test from the paper: its two readings and its 2 to 8% "low contrast" range are the writer's.
- `fig5bc-amplitude-clusters` labels clusters with a rule that isn't in the paper. The outcome rests on the fractions matching, so the rule doesn't decide it.
- `fig4i-proportion-within-ep` treats the printed spreads as coming from a 0/1 responder flag over units pooled across recordings. The legend says n = 9 recordings. The arithmetic supports the claim's reading, but the paper never states it.

Every main finding has a claim, and none comes from outside this paper. The only file changed is `claims/000774/10.1016-j.celrep.2026.117420.yaml`; nothing is committed or pushed.
