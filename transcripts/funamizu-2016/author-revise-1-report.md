I've worked through the round-1 report. Ten outcomes changed, and every outcome now matches the one the verifier gave. The only remaining disagreement is the blocking reason for two claims. The entry re-ran cleanly in 24 minutes and `tools/entry.py check` passes. The handover is rebuilt and nothing is committed.

**Outcome changes (all to the verifier's outcome)**
- **Blocked because the readings disagree (`methods_underspecified`), 10 claims:** supp1-licking-speed, fig2d-after-vs-before, fig2d-layer-distance-preference, supp8a, supp8b, supp8c, fig4-above-chance, fig4c, fig4d. Before, I had settled each by adopting one reading as an assumption. The claims file's header says to block in that case, so all those assumptions are withdrawn.
- **Now not reproduced, because their criteria have no partial outcome:** lick-goal-correlation, supp9-preserved-representation, fig5a-map-decreases-without-sound.
- **Now partially reproduced:** fig4e. Two configurations reach 99.8% of bins, not 100%.

**Questions added to `questions/001605.yaml`**
- **supp1:** I rendered the supplement page. The panel titles read "Intermittent 1: 8.4 cm to 0 cm from goal" and "Intermittent 2: 25 cm to 8.4 cm from goal", which is zone reading (b). The question asks a reader whether that zone should be the only one tested.
- **fig4-above-chance:** chance reading (b) permutes distances across trials. Every trial still falls from 67 cm to the goal, so that decoder still decodes distance and does not measure chance.

**Fixes and outputs the verifier asked for**
- **Speaker table:** every row in all 94 files starts at a trial start and lasts one frame. There are 6 to 26 rows per trial start, one per speaker listed, which explains the 1,085 to 1,240 rows.
- **Clock:** trial frames sum to the series length in all files, and every series stores a 30.9 Hz rate. The reward-time distribution is printed: median 8.83 s, with 22.1% of trials under 7.4 s.
- **Lick frequency:** the notebook now shows its form. It is held between licks and is non-zero at 33 cm in a median 22% of trials. That explains why the "first non-zero frame" onset fails, and supports detecting onsets where the value changes. A third onset variant, the first rise from 0 Hz, does worse.
- **MAP in intermittent 1, 8.4 to 0 cm:** the zero slopes are not caused by the 0.84 cm grid. The MAP sits at 0 cm in 51.6% of frames, and is constant through the zone in 18 to 29% of trials, nearly all of them at 0 cm.
- **K-means run per session:** shown for the class counts and the supp8 claims. It reproduces 5 of 12 counts under one baseline and 3 under the other, which changes no outcome.
- **Width fits:** they are no longer limited to the grid; a bounded optimizer refines each one. tuning-similar-ppc-pm stays blocked, because the one reading that passed still passes.
- **Smaller fixes:** fig4c no longer counts trials from sessions without goal-distance neurons, which removes the NaN medians. supp11 zone reading (a) now leaves out the first 33 cm, which always have sound. Neither changes an outcome.
- **Running time:** worker processes are now limited to one linear-algebra thread each. My first full run timed out at 60 minutes because the threads competed for the four cores.

**What I did not do**
- **fig3b and svm-correlations:** these stay blocked as `too_large`, where the verifier would give "other". The protocol prescribes `too_large` when a computation's estimate exceeds the 60-minute notebook limit, and I recorded the disagreement. Both estimates now come from timings in the notebook on real data: about 37 h per reading for fig3b, and about 1.2 h for one reading of the SVM claim.
- **Point B12** (decoder neurons are selected using all trials, as the paper does) needed no change.
