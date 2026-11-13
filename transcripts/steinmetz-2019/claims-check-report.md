**Checker result:** `claims/000017/10.1038-s41586-019-1787-x.yaml: 40 claims, 38 quotes, 11 statistical values, 0 problems`. I ran it before and after my edits and got the same result both times.

I checked the file against the paper text, the supplement 2 Word file (the subject table is only there) and the paper's code at commit 9a0bea8.

**Changes, by claim**
- **Opening comment:** it said supplement 1 holds Supplementary Tables 1 and 2 and the legends. It holds only the guide; the tables and legends are in supplement 2.
- **fig1d-reaction-time-difficulty:** added a third reading of the ANOVA factors: contrast and presence of a competing stimulus, the variables the Fig. 1d legend names.
- **early-response-fraction:** the paper does not say what counts as "turning the wheel within 400 ms". Named it open, with two readings: a 90 d.v.a. turn, or any detected movement onset.
- **task-modulated-fraction:** the rule for a test's direction was wrong for the ranksum test 6; it now follows the code. Reading (b) said "test 6 as a rank-sum, as the code does", but the Methods already make it a ranksum, so it was the same as (a). Replaced it with a reading at p < 0.05.
- **suppfig2-rate-amplitude:** said the d' formula is a standard choice; the paper does not define it.
- **fig2de-activity-order:** added the Methods' own rule for selecting responsive neurons for display as reading (a); the criterion had missed it. Said the quarter and third thresholds are the file's own reading.
- **fig2fg-miss-restricted:** removed `depends_on` fig5b-miss-more-than-passive; the criterion does not use that claim's result.
- **fig3d-vision-localized, fig4b-choice-regions:** said which thresholds and definitions (the half of neurons, the five top regions, "higher-order thalamus", the 5% bound for "rare") are the file's readings and not the paper's.
- **ed4f-focality:** said the index is taken over the 42 regions; the legend's floor of 0.0238 is 1/42.
- **fig4d-jpecc-vis-leads:** the number of principal components is the same for both groups (jPECC.m), not set per group.
- **fig5c-prestimulus-task-vs-passive:** the criterion required VISp and CP to pass the nested ANOVA. The paper only states their difference for Miss against passive trials (Fig. 5a), with no test. The statement and criterion now compare those means.
- **fig5f-engagement-index:** contrast reading (b) did not differ from (a); it now includes all four contralateral contrast levels, zero included.

**Still open** (recorded under `checks`)
- fig4d-jpecc-vis-leads does not test the ~40 ms lag, and does not say how many time points must be significant.
- fig4d-jpecc-no-lag-frontal-midbrain uses a time window the file chose, with uncorrected t-tests at each time point, so a false positive is likely.
- fig5d-go-miss-matches-task-passive uses a Pearson correlation as its test; the paper gives no test for Fig. 5d.
- No claim covers Extended Data Fig. 4c-e (activity before movement onset in most regions, activity after reward), a secondary finding.

**Ready:** yes (`ready: true`). Every main finding has a claim and every claim comes from this paper. Nothing was committed.
