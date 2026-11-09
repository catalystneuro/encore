The answered questions are taken up, and the entry ran cleanly. `python tools/entry.py all` passed with 0 errors and the notebook ran in 17.2 minutes, 14 of them streaming the raw data. I ran `handover`, and the package is in `executed/000019-bouchard-2013/handover/`. I read through the executed copy, and its numbers back every conclusion. I did not verify the work and nothing is committed.

Over the 22 claims there is now 1 reproduced, 1 partially reproduced, 5 not reproduced and 15 blocked. Before, it was 1, 1, 7 and 13. Two claims changed outcome.

## Questions and what each answer changed

1. **Z-scoring before the PCA, and which input is projected.** The paper settles neither. The claims file now names both z-scorings (`row`: each electrode over its whole series; `time`: across syllables at each time) and two inputs to project: (i) the matrix given to the PCA, and (ii) the baseline z-scored high gamma, as Eq. 5 writes it. I added (ii) to the notebook, so each state-space claim now runs 24 readings, up from 8.
2. **Syllables with fewer than 15 renditions.** The paper does not say. Both sets, every syllable and only those with 15 or more renditions, are now readings in the claims file. They were already run, but the first run had added them itself as a question.
3. **Acoustic onset with no audio.** The criterion now allows the hand-marked syllable start, recorded as a deviation, with the result against t = 0 shown beside it. I added that comparison.
4. **The rest period as a baseline.** Yes. It is now baseline reading (c). The first run had shown it only as a variant; now it counts in every claim that uses the z-scored high gamma.
5. **Electrode positions from the grid geometry.** No. The spatial claims stay blocked, and their notes now cite the answer.

## Outcome per affected claim (earlier outcome in brackets)

| Claim | Now | Before |
|---|---|---|
| active-electrodes | blocked: methods_underspecified | not reproduced |
| fig4a-consonant-clusters | blocked: methods_underspecified | not reproduced |
| data-composition | partially reproduced | partially reproduced |
| fig1f-h-phonetic-contrasts | not reproduced | not reproduced |
| suppfig6-mixed-tuning | reproduced | reproduced |
| fig3d-timing-sequence | not reproduced | not reproduced |
| pca-nine-components | blocked: methods_underspecified | same |
| suppfig11-co-clustering | blocked: methods_underspecified | same |
| fig4c-d-hierarchy | blocked: methods_underspecified | same |
| fig4ef-feature-correlations | blocked: methods_underspecified | same |
| fig5c-separability-timing | not reproduced | not reproduced |
| fig5d-separability-coupling | blocked: methods_underspecified | same |
| suppfig13-consonant-vowel-distance | blocked: methods_underspecified | same |
| suppfig9-pc-articulator-weights | not reproduced | not reproduced |
| fig1c-e and the seven spatial claims | blocked: metadata_insufficient | same |

Why the two changed, and the details worth knowing for the others:
- **active-electrodes:** with every syllable, no baseline falls within 27 to 33 (rest gives 34.0). With only the 15+ syllables, the rest baseline gives exactly 27.0, at the lower edge of the tolerance. So the two syllable-set readings give different outcomes.
- **fig4a:** one of the 24 readings has three clusters as the best choice, by a very small margin (silhouette 0.333 against 0.329 for two clusters). It is enough to make the readings disagree.
- **fig1f-h:** with the rest baseline, some lips electrodes exceed z = 2 for /ju/ (largest 3.54), but at each one /ja/ or /ji/ is also above 2.
- **fig3d:** lips and tongue begin before the substitute onset in none of the 96 readings, and before t = 0 in 2. The other two order conditions fail everywhere, so the outcome is the same against either reference.
- **The blocked state-space claims:** the new readings still disagree. For example, the `time` z-scoring readings reach about 60% of variance only with the rest baseline, and the consonant-vowel distance ordering holds under (ii) but not under `time` with (i).

## Other changes

- **Speed:** the separability calculation now does its bootstrap as one matrix product. It gives the same numbers (differences below 1e-13) and is about 20 times faster. Without it the notebook would have taken over 30 minutes.
- **Text and record:** I updated the notebook header, conclusions and summary, the README, `entry.yaml` (runtime 20 minutes) and every affected outcome in `attempts/000019-bouchard-2013-01.yaml`. Each claim's notes now end with what the answers changed. Two deviations no longer apply, because their readings are now in the claims file, so I removed them.
