I wrote `claims/johnson-2017.yaml` with 22 claims. The quote checker found every quote in the text; its one flag is a value I checked by hand (below).

**Text read.** The version of record with its supplemental information: main text, figure legends 1 to 4, STAR Methods, Figures S1 to S4 legends and Tables S1 to S3. Nothing the claims need was missing. The PDF could not be rendered here (no pdftoppm or PyMuPDF), so I read no figure images. The data descriptor was read only to learn what the dataset holds.

**Code.** The paper says its MATLAB code is deposited with the data at CRCNS. According to the descriptor it sits in pfc-5's own `analysis_scripts` directory. Because it is one of the dataset's files I did not read it, and no commit is recorded. Every method in the file comes from the paper's text. The opening comment tells the author they may settle open details from those scripts.

**Counts.**
- **Quotes:** 21 of the 22 claims have one. `table-s1-patient-accuracy` is marked `inferred`, because its numbers appear only in Table S1.
- **Statistics:** 21 claims carry 33 statistical values.
- **Expected values:** 7 claims have them.
- **Criteria:** all 22 claims have one, and 8 of them are claims of absence judged on the paper's own test.
- **Coverage:** accuracy, ERP, baseline power, task-induced power, delta-theta and alpha-beta PSI, and network degree.

**Checker flag.** The checker could not find p = 5e-10 (`patients-above-chance`). Line 190 of the text prints it as "one-tailed p < 5 3 10�10", which is the extraction's garbling of 5 × 10⁻¹⁰, so the value is correct.

**Open details shared across claims (O1 to O7), with the readings named:**
- **O1, spatial neighbours for clustering:** FieldTrip's biosemi64 template, or triangulation.
- **O2, clustered dimensions:** channels by time by frequency, or channels by time on the band average.
- **O3, hemisphere index:** 27 lesioned-side indices, or 54 values (each channel minus its homolog).
- **O4, which 10 controls were swapped:** the deposited swap if there is one, or several random draws.
- **O5, surface Laplacian parameters:** FieldTrip spline defaults as the standard choice.
- **O6, the PFC region of interest for PSI:** the text gives no channel list. The readings are the anterior channels of the reproduced Figure 2 cluster, or AF7-F5-F7-FC5-FT7 from Figure S4. The parieto-occipital partners are read as P1-P3-P5-P7-P9-PO3-PO7-O1.
- **O7, how a thresholded Z is summarised:** the group mean crosses the threshold, or most subjects cross it.

**Open details in single claims:**
- **Mixed model:** a linear (Gaussian) model on the 204 cell accuracies or a binomial logit model; the paper calls it "logit" in the Results and "linear" in the Methods. Also condition coded as one number or as a three-level factor. The degrees of freedom in Table S3 fit 204 subject-by-hemifield-by-condition cells with a one-number condition term.
- **Accuracy means:** over all of a subject's trials, or the mean of its six cells.
- **Accuracy denominator:** trials after the eye-gaze exclusion, or trials kept after EEG cleaning.
- **Above-chance tests:** one test, one per hemifield, or one per hemifield and condition (suggested by "t1,13 > 15.43").
- **Variance F test:** on age, on education, or both.
- **Trial counts:** all trials kept, or correct trials only.
- **ERP zero-padding:** "7,500" has no unit (ms or samples), unlikely to matter.
- **Figure S4 hemifields:** pooled, or each separately.
- **Pair clustering for PSI:** over time per pair, or also over neighbouring pairs.
- **Network degree:** signed sum of Z over true connections, or a count.
- **Delta-theta PSI windows:** the lesioned/intact pairing of the stated time windows is my reading of the sentence.

**Missing from the paper.** No data a claim needed was absent. Two gaps come only from the figures I could not view: the channel list of the Figure 2 cluster, which is open detail O6, and the time courses of Figures 2 to 4, which the claims take from the text and legends instead.

**Tolerances.** Where the paper states a spread I used it, as the protocol says, so the means of accuracy, age and trial counts use the subjects' SDs. That makes some of these checks loose. For the per-patient values of Table S1 I set 0.02 instead of 10%, and the file gives the reason.
