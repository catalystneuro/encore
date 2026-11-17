I made nine corrections to `claims/mohebi-2019.yaml` and marked it ready, with three problems left open. Nothing is committed or pushed.

**Checker:** `claims/mohebi-2019.yaml: 37 claims, 36 quotes, 7 statistical values, 0 problems`. The result was the same before and after my edits.

**Changes, by claim**
- **fig1cd-nac-core-dopamine-reward-rate:** the criterion was worded backwards. As written, it required dopamine in NAc shell and dorsomedial striatum to have a significant coefficient. It now requires that neither has one.
- **ed1-behavior-similar-across-subregions:** the paper gives latency without a unit, so seconds is now marked as a reading.
- **fig2-tagged-dopamine-cells:** the criterion asked for per-rat counts "within tolerance", but no tolerance is set for them. It is now judged on the two totals (27 and 2), and the per-rat counts are only shown.
- **ed5a-pavlovian-behavior:** the per-trial head-entry measure is now named as open, with two readings. The legend defines head entry % for each moment in time, not for each trial.
- **fig2efgh-tonic-firing-indifferent-to-reward-rate:** I removed a leniency the paper doesn't support, which allowed as many significant cells as chance would give. The paper says no individual cell changed. Both test readings are now run, and the binomial count is reported but doesn't decide the claim.
- **fig3cd-dlight-reward-rate-minutes:** the Methods drop the 1 min sample that contains the block transition, not the whole 3 min epoch. Corrected.
- **fig4ef-dlight-ramps-before-approach:** Center-In is now limited to long-latency trials (> 2 s), as in the Results, and the criterion says how sessions are counted.
- **ed8-other-reward-expectation-estimates:** the paper doesn't give the range of alpha searched. It is now named as open, with a reading.
- **fig5cd-dlight-positive-not-negative-rpe:** the statement's timing part ("slightly delayed and prolonged, but subsecond") had no criterion. I added one, marked as a reading.

**Still open**
- **Missing figure legends:** the text has no legends for main Figs. 1 to 5. So the paper's own tests for six claims of absence are unknown, and so are the windows used in Figs. 4 and 5. The six are fig2efgh, fig2fh, fig2i-burst, fig2i-inactive, fig4a and fig5a-early. Their criteria run several plausible tests, but the protocol says a claim of absence should be judged on the paper's own test. Someone with the article PDF should replace those readings with the tests the legends give.
- **fig2i-no-inactive-states:** the paper doesn't give the inter-spike interval that counts as "long", or a bound for "very low". The criterion's 5% bound is not from the paper.
- **No claim for one minor finding:** the Extended Data Fig. 7 legend notes that spiking, dLight and voltammetry respond to cue onsets with different timing. It has no claim. It is minor and rests on voltammetry data reused from an earlier paper.

Every main finding has a claim, and every claim comes from this paper.

**Ready:** yes. The `checks` entry is added with `ready: true`, and it lists the open items above.
