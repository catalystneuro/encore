I stopped without writing `claims/brudner-2026.yaml`, because the supplement the results rest on is missing.

**Text read:** `paper/10.1073-pnas.2608896123.txt`. This is the version of record (PNAS 123(29) e2608896123, published July 14, 2026), taken from a PDF a person supplied. It holds pages 1 to 11 of 11: the main text, figure legends 1 to 5, a short Methods summary and the references. The PDF under `paper/` is the same article.

**What is missing:** the SI Appendix (https://www.pnas.org/lookup/suppl/doi:10.1073/pnas.2608896123/-/DCSupplemental).
- The Methods section is only a summary paragraph. It says that "Detailed descriptions of plume construction, feature calculations, regression analyses, neural network training, simulation parameters, fly selection criteria, turn detection, and statistics are provided in SI Appendix."
- The Results cite "SI Appendix, Supplementary Methods" 19 times, and Figs. S1 to S5 are part of the findings.
- Without the supplement, the main behavioural claims on the fly data (Fig. 5E and F) cannot have their criteria taken from the paper. That covers:
  - the turn detection rule;
  - the "upwind tracking in the bulk of the plume" fly selection;
  - how the gradient and motion cues are computed at the antennae;
  - the logistic regression and its cluster-robust standard errors;
  - the cue dominance score.
- The same applies to the plume features (Fig. 1), the logistic regression AUCs (Fig. 2), the network training (Fig. 3) and the agent simulations (Fig. 4).

Writing claims now would mean leaving nearly every part of every method open. The protocol says to stop in that case.

**Claims written:** none, so there are no quotes, statistics or criteria, and I named no open details or readings. I did not read the linked code (github.com/emonetlab/GradientMotionMultiplePlumes) or the Yale Dataverse deposit (doi:10.60600/YU/590UBV). The code can settle details but cannot stand in for the missing Methods. I did not look at the dataset.

**To proceed:** add the SI Appendix text (the Supplementary Methods and the legends for Figs. S1 to S5) under `paper/`, then rerun the reader.
