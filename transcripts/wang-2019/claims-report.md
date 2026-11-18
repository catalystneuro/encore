I wrote `claims/wang-2019.yaml` with 25 claims. The quote checker passes with no problems. Nothing is committed.

**Text read:** the accepted author manuscript from PubMed Central (PMC6675632). It has the full Methods, Results, Discussion and figure legends. There was no PDF, so I could not see the figures, and the paper cites no supplement.

**Code:** the paper links only to its two published heart-cell models, on the Bers lab and Grandi lab pages. Both pages load, but the MATLAB downloads need a registration form (name, affiliation, email), so I did not fetch them. The optical maps were analysed in Optiq, a closed program, so no criterion takes a detail from code.

**Counts:**
- **Quotes:** all 25 claims have one, and all match the text word for word.
- **Statistics:** 10 claims carry 12 statistical values. Most are "p<0.05 vs. time 0" or "vs. baseline"; the mouse base against apex comparison is p<0.01.
- **Expected values:** 3 claims have them:
  - mouse APD80 of 50.9, 60.6 and 46.5 ms at 0, 15 and 60 s of stimulation, with the stated SDs as tolerances;
  - rabbit repolarization reversal in 8 of 9 hearts;
  - mouse repolarization unchanged in 7 of 8 hearts.
- **Criteria:** 23 claims have one.
- **Model claims:** 4 rest on the simulations (Fig. 8 and 9) and are marked `data: elsewhere`, pointing to the two models.

**Details the paper leaves open, with the readings named:**
- **Which test:** the Methods allow repeated-measures ANOVA or paired t-tests. Readings are paired t-tests against time 0, or a one-way repeated-measures ANOVA with comparisons against time 0. The post hoc test is never named.
- **"During SNS" in the 20 s experiments:** the value at 20 s, the mean over the 20 s, or the peak.
- **Time points in the 60 s time courses:** the text names only 0, 15 and 60 s, so the data's own time points are used.
- **"Monotonic":** the mean over hearts moves the same way at every step, or no step differs significantly in the opposite direction.
- **"Similar" CaT amplitude between species:** each species' mean lies within the other's SD, or an unpaired t-test gives p ≥ 0.05 at each time point.
- **"Exaggerated" (Fig. 3E):** a larger peak rise in APD, or APD with stimulation significantly above APD without it at the peak.
- **"Prolonged compared to baseline" (Fig. 3F):** above the no-stimulation run, or above its own time 0.
- **Direction and reversal of repolarization:** the sign of the base-to-apex gradient of repolarization time flips, or the site of earliest repolarization moves to the opposite end of the map.
- **Base and apex regions:** the basal and apical thirds of the map, or quarters. The regions are drawn in Fig. 5E, which I could not see.
- **Activation "changed little" and the mouse AP and CaT maps being "spatially distinct":** the paper gives no measure. I named readings and these claims are reported descriptively.

**Missing from the paper:**
- The figure images, needed for the sampled time points and the regions.
- Any numbers beyond the three abstract APD values and the heart counts. Most results exist only as figure points.
- The model code itself, because of the registration form.
- The paper never says which of its two tests produced each p-value.

**One weak spot for the checker:** the 50.9, 60.6 and 46.5 ms values appear only in the Abstract. The claim's quote comes from the Results, which states the biphasic pattern without those numbers.
