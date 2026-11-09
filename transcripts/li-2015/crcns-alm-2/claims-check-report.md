The claims file for CRCNS:alm-2 is now fit for an attempt, and its last `checks` entry says `ready: true`. Nothing was committed or pushed.

**Checker result:** `claims/crcns-alm-2/10.1038-nature14178.yaml: 25 claims, 25 quotes, 11 statistical values, 0 problems`. The first run, before my changes, gave 23 claims and 0 problems.

**Changes, by claim** (no claim id was changed):
- **fig4f-both-types-every-fov:** removed the rule that "all but one or two fields of view" counts as partially reproduced. The paper gives no such rule. The criterion now reports how many fields of view miss a type.
- **fig2e-equal-contra-ipsi:** the criterion had fixed which neurons and which time window the t-test (P = 0.13) uses, but the paper says neither. It now names three readings. The third is the late-delay test of all task-selective neurons, which also reports P = 0.13 and may be the same test.
- **ed2c-error-trials-predict-lick:** the statement added "and not the pole position", which the paper does not say, so I reworded it to the paper's words. The criterion now says error trials are grouped by the instructed trial type, which the negative correlations in the legend require.
- **fig3f-pt-contra-preferring:** the sample size assumed all 45 PT neurons, but the Methods sort only selective neurons by preference. Both populations are now readings.
- **fig3f-pt-late-contra-selectivity:** this claim had no criterion. The paper does not define the test window, the "spike rate modulation (%)" or how the 570 ms onset is found. I added a criterion built on the Methods' contra-selectivity, with those three details named as readings.
- **fig5-pt-stimulation-contra-bias and fig1d-photoinhibition-ipsi-bias:** the criteria required significance in every condition. The text of Fig. 5b holds only three significance stars and Fig. 1d five, which cannot be matched to conditions without the image. Both now name readings for which conditions must be significant. Fig. 5's dose response uses delay-epoch data only, per mouse or as the mean across mice. For Fig. 1d, I noted that the paper gives no test for the smaller bias in the sample epoch.
- **ed6d-it-stimulation-inconsistent:** the criterion joined its two parts with "or". The paper states both (effects varied across mice, and depended non-monotonically on power), so they are now joined with "and".
- **behaviour-performance:** added a criterion. The paper does not say which trials or averaging give 78.4% correct and under 13% early responses, so the criterion names readings.
- **Added two claims** for findings that had none: **fig2c-selectivity-time-course** (Fig. 2c) and **ed7-pt-stimulation-persistent-change** (Extended Data Fig. 7).

**Still open:**
- **fig4g-quarter-selective:** the paper says "approximately a quarter", but 182 of 534 and 174 of 542 are about a third. The claim keeps the paper's words and is judged on the counts.
- **Unread stars in Fig. 1d and 5b:** no PDF renderer was available, so the readings stand in for them. Someone with the image could replace the readings with the conditions the paper actually marks.

The rest of the file checked out against the paper. Every claim comes from this paper, and the main findings are now all covered.
