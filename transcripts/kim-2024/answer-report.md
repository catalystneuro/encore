There was one question. I changed the claims file to answer it.

**figs12-other-features-shared** (changed): The question was right. The Figure S12 legend in the supplement names ten features as similar (panels F to O) and five as different (A to E). The old fourteen-feature criterion included four features the paper reports as different.
- **Amended claim:** the statement, source and quote now name the legend's ten similar features. The criterion is a claim of absence over those ten: a one-way ANOVA per feature at alpha 0.05, reproduced when more than half show no difference, with every feature listed. It also notes that panel O (adaptation index) has an asterisk in the figure even though the legend calls it similar; it is counted with the ten, as the legend says.
- **New claim, `figs12-app-differs-from-all`:** the four APP-against-ALL differences (input resistance, AP width, downstroke, f-I slope) are now their own claim. I did not fold them into the absence claim as the question suggested, because they are a separate finding. They use the same two test readings as `fig6f-max-firing-rate`. Sag stays with `figs12a-sag-higher`.
- **Opening comment:** a short note now says the supplement was read for this amendment.

`tools/claims_check.py` reports 0 problems. The question is marked `answered: 2026-11-03`, and its answer gives the changes and quotes the legend. Only `claims/001544/` and `questions/001544.yaml` were changed, and nothing was committed.
