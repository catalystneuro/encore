I wrote no claims. The paper text we have is incomplete, and it is an older version than the paper named, so I stopped as step 1 of the Reader section requires. Nothing under `claims/000986/` was created.

**What I read:** `paper/10.1101-2024.04.04.588209.txt`, which is bioRxiv preprint version 1 (JATS XML, title "…explains optimal coding at moderate arousal in auditory cortex"). It has the main text, figure legends and Methods. There is no supplement and no PDF, and `papers/manifest.yaml` agrees (`supplements: 0`, `pdf: false`).

**What is missing:**
1. **The supplement.** Figures S1 to S17 and Tables S1 and S2 are cited but not in the text, and several findings rest on them:
   - Fig. S5A/B: in every session, decoding accuracy and single-cell discriminability (d′) peak at moderate pupil size.
   - Fig. S6: the inverted-U still holds with locomotion trials left out.
   - Fig. S10: the stimulus-induced drop in Fano factor. The Results state it, but the test and n are only in the S10 legend.
   - Fig. S8: the sign of firing-rate modulation in each session.
   - Figs. S2 and S4: pupil sampling and decoding for each session.
   - Tables S1 and S2: every model parameter, which all the model claims need.
2. **The right version.** The bioRxiv API lists three versions. Versions 1 (2024-04-05) and 2 (2024-04-08) have the old title. Version 3 (2025-11-01) has the title given for this task ("…explains the inverted-U relationship between tone discriminability and arousal in auditory cortex"). The preprint has since been published as **doi:10.1016/j.neuron.2025.11.011** in Neuron. Under `docs/pipeline.md`, a published paper replaces its preprint, so the claims should be read from the Neuron version of record.

**What needs supplying:** the full text and supplement of doi:10.1016/j.neuron.2025.11.011. Version 3 of the preprint, with its supplement, would do if the Neuron text cannot be had. The triage should also list the preprint under `not_papers` and the Neuron paper under `papers`.

Because nothing was written, there are no claims, quotes, statistics, criteria or open details to report. I also did not read the paper's code, since no claims were going to be written from it.
