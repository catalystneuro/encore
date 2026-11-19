I've worked through every point in the round-2 report and re-run the entry with `python tools/entry.py all entries/martinez-conde-2019`. It passes with 0 errors and runs in about 30 s.

**Outcomes:** none changed and nothing is proposed. The verifier agreed with all 19, and every variant added below gives the same outcome as the main analysis. The main numbers did not move.

**Added or corrected:**
- **The two "changes no outcome" sentences in the Summary.** One is about keeping the pixels that fall off the display, the other about the single 16 DU square that best matches the stored Square and Edge baselines. Each variant had only been run for some claims. Both are now run in all 14 claims that use the rate maps: fig4a, fig4b-pairwise, fig5, fig6, both fig7c claims and fig7d were added, and fig7c's Edge responses are recomputed under each variant. No outcome changes. The Summary now names the claims covered.
- **What `smoothed_image_norm` holds.** I added the missing check, and the old statement turned out to be only partly true. It holds in 21 of the 38 recordings that store the map. 5 store the same thing without the scaling, 11 match neither formula, and 1 is partly NaN. I corrected the data-check text, the Summary and the `metadata_error` finding. The analysis never used this map, so no number depends on it.
- **Cell 48 (fig7c significance).** It now says "BH over 40". It also notes that BH per fold makes S40 significant at 0.906 as well (p = 0.040).
- **fig6 notes and conclusion.** They now give each run's smallest p: 0.174 unsmoothed, 0.481 unmasked, 0.415 with the single square. None of the ten tests is significant in any run.
- **Round-1 reasons.** The fig7c reason now carries the verifier's "borderline" label, and the s4 reason its caveat that the main analysis follows the paper's text.
- **Round 2 recorded** under `verifications`. For each claim it gives agreement, the verifier's outcome, its reason in its own words and my response.

**Not done:**
- The Star finding's check that was "made while preparing, not run in the notebook" stays as it is. The verifier said it is labelled as such, so it is disclosed, not wrong.
- I added nothing to `questions/martinez-conde-2019.yaml`. The verifier reported no new misreading of the paper. The question on the fig7c margin was already filed; the verifier just didn't have that file.
- I didn't commit, as instructed.
