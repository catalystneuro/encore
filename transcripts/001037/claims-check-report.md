The claims file is ready for an attempt, with five problems left open. It's in `claims/001037/10.1038-s41586-024-07915-x.yaml`; nothing is committed.

**Checker result:** `54 claims, 53 quotes, 81 statistical values, 0 problems`. It read 75 statistical values before my edits; I added six.

**Changes, by claim:**
- **Header, on which test was used.** The file said every Mann-Whitney test in the paper was unpaired. That's wrong for some panels: the printed p-values 0.125 and 0.1875 at n = 5, and 0.8125 at n = 7, can only come from a paired signed-rank test, not an unpaired Mann-Whitney. The header now says so.
- **ed3e, ed3f, ed4hi, ed5e, fig1m:** for the reason above, each now runs a paired signed-rank test as well as the unpaired Mann-Whitney.
- **ed3e:** the paper doesn't define "full interaction". Two readings are now named: the whole session, and first intruder entry to last removal.
- **ed1n (and ed1p, which follows it):** the criterion dropped mice whose model explained under 70% of variance. The paper's own mean for observation is 67.2%, yet it reports all 5 mice, so this would have excluded fits the paper used. All mice are now kept and the value is reported.
- **ed3g:** added the Methods' 1,000 shuffles per mouse for the significance test. Also added a third train/test reading from the Methods' wording: train on one trial, test on all the others.
- **ed5e:** the Methods call the ten model inputs "binary" without saying how. This is now named as open, with two readings.
- **x1-time-constant-range:** removed "at most one mouse outside", which has no source in the paper. Which fits the 50 to 200 s range comes from is now named as open.
- **Missing p-values added:** fig2no (P = 0.029, P > 0.05, P = 0.0508), ed8jl (the second P = 0.276), ed9i (P > 0.05), ed10g (P > 0.05).
- **ed10hi:** removed "in at least 5 of 8 mice", which has no source in the paper.
- **ed10lm:** the 1.5 SD rule was cited to the wrong place; it comes from the Extended Data Fig. 10h legend. The Methods define follower cells as lying beyond 50 µm, which can't give the legend's "11% within 50 µm". The criterion now says this and counts responding neurons at any distance.
- **fig4ce:** the density range over which fast networks must fail is now stated (0 to 20%, from the Fig. 4c legend).
- **fig4hj:** the Methods give an inhibition gain of 1 and the Fig. 4h legend gives 1.25. Both are now run.

**Still open (recorded under `checks`):**
- **methods-cvr2:** the spreads printed as "0.03%" and "0.02%" are read as 3 and 2 percentage points. The paper doesn't settle this.
- **ed4g, ed4hi:** the printed p-values 0.012 and 0.34 at n = 5 aren't exact values of either test, so the test behind them is unknown.
- **ed1m:** the legend is garbled, so the direction of the difference and the reason for n = 4 aren't given.
- **ed5e, ed6g:** "small fraction" and "close to zero" have no number in the paper. The 10% thresholds are the earlier agent's choice, not the paper's.
- **ed10lm, ed12eh:** the paper gives no test for these "no correlation" findings. A Pearson test is used, by analogy with Fig. 5g.

Every main finding has a claim, and every claim comes from this paper.
