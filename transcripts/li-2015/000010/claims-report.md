I wrote the claims file for DANDI:000010 at `claims/000010/10.1038-nature14178.yaml`. The checker passes: 27 claims, 27 quotes, 13 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record, from a PDF supplied by a person. The extracted text has the main text, the legends of Figs 1 to 5, the Methods, and the legends of Extended Data Figs 1 to 7. The paper has no supplement beyond Extended Data, so nothing the results rest on is missing. The extraction prints "=" as "5", "<" as ",", ">" as "." and "±" as "6". The quotes keep these characters so they match the text word for word.

**Code:** the paper links no analysis code, so no repository or commit was read. It names one deposit, the data at CRCNS (doi:10.6080/K0RF5RZT). Every method in the criteria comes from the Methods and the figure legends.

**Claims:**
- **Quotes:** all 27 claims have one; none needed an `inferred` note.
- **Statistics:** 11 claims carry them. They are the bootstrap tests (Figs 1d, 3f, 5b), the t-tests against 0 (P = 0.13; Fig. 3f P < 0.05 and P = 0.40), the spatial shuffles (P = 0.34 and 0.61), and the binomial and chi-squared tests of Fig. 4h.
- **Expected values:** 12 claims. They are counts and numbers with a 10% tolerance; the reaction time uses the paper's s.d. of 10.5 ms.
- **Criteria:** 26 claims. The absence claims are judged on the paper's own test: the spike-count bias, the IT neurons in Fig. 3f, and spatial intermingling.
- **Scope:** the claims cover behaviour, photoinhibition, unit counts and selectivity, the tagged PT and IT neurons, imaging, photoactivation and its dose response, the persistence data of Extended Data Fig. 7, and anatomy.

**Details the paper leaves open, and the readings named for each:**
- **Mean performance (78.4%):** all control trials pooled, the mean over sessions, or the mean over mice.
- **Trials for selectivity:** correct trials only, or all non-early trials by instructed trial type.
- **Response epoch length:** no passage gives it. Readings are 1.3 s, like the other epochs, or the 1.5 s lick window.
- **Peak of selectivity "at the beginning of the response epoch":** the first 200 ms window after the go cue, or any window starting within 0.5 s of it. The 200 ms window step is a standard choice, with 50 ms as a variant.
- **Population correlation (Fig. 2c):** the vector concatenates both trial types, or uses their difference.
- **Error trials:** at least 1, or at least 5, error trials of each type per neuron.
- **Population for P = 0.13:** all 1,245 putative pyramidal neurons, or the 912 selective ones.
- **Fast-spiking baseline:** the 0.5 s before the pole moves, or all recorded time before it. Selectivity is the fraction significant, or the mean absolute rate difference.
- **PT and IT neurons counted (Fig. 3f):** all tagged neurons of the type, or only the selective ones.
- **PT contra-selectivity (Fig. 3f):**
  - Test window: from 570 ms before the cue to the cue, or the whole delay epoch.
  - Modulation %: divided by the mean rate over both trial types, or by the lick-left rate.
  - Onset: the earliest window from which selectivity stays significant until the cue, with windows stepped by 10 ms.
- **Imaging selectivity:** how far the Kruskal-Wallis bins extend, mean ΔF/F over the whole trial or each epoch separately, and correct or all trials.
- **Spatial shuffles:** labels shuffled within each field of view, or across all.
- **Reaction time:** which mice, per-mouse mean or median, and which trials.
- **Powers pooled for Fig. 5:** 0.12 to 0.8 mW as the legend says, or below 0.25 mW as the text says. The paper disagrees with itself here.
- **Dose-response effect size:** the change on ipsilateral trials, or the ipsilateral minus the contralateral change.
- **No measure or test given:** the smaller bias with sample-epoch inhibition, the inconsistent effect of IT stimulation, and the activity change in Extended Data Fig. 7. Each criterion says this and names the readings.

**What the claims lacked:** the PDF pages could not be rendered here (no pymupdf or poppler), so values shown only in figures were not read. These are which panels carry which stars in Figs 1d and 5b, the inset fractions of Fig. 3f, and the curves of Extended Data Figs 3, 6 and 7. The claims record the lowest significance level the legend states and say the figures were not read. The paper also gives no number for the "short latency" of contralateral licking.
