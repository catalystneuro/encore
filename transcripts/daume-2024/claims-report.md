I've written `claims/001187/10.1016-j.neuron.2024.09.013.yaml`. The quote checker passes with 0 problems (29 claims, 28 quotes, 43 statistical values checked), and the file has no em dashes, no "rather" and no colon-space in plain scalars. Nothing is committed.

**Text read**
- **Paper:** the accepted author manuscript from PubMed Central (PMC11624075). It has the full Results, figure legends and STAR Methods.
- **Supplement:** NIHMS2025394-supplement-1, with Figures S1 to S4 and Table S1.
- **Preprint:** I searched the bioRxiv preprint (v1) for method details only; it adds none.
- **Figures:** I could not view the main-text figures, because only the supplement PDF was supplied.
- **Code:** github.com/rutishauserlab/SBCAT-NO-release-NWB at commit 6d07204. It covers the behaviour plots, the 0.1 Hz rate filter, how category and memory-selective neurons are chosen, and the Fig. 3a GLM. There is no code for Fig. 2b–f, 3b–h or 4b–g.

**Counts**
- 29 claims: 28 quoted, 1 inferred (the per-session unit counts in Table S1).
- 25 claims record statistics, all 29 have criteria, and 14 have expected values.
- 10 are claims of absence, judged on the paper's own test.

**Method choices (code over Methods)**
- **How outlier neurons are removed:** the Methods say ±3 SD from the mean. The Fig. 3a code removes neurons above 3 SD of the neuron means, upper side only and not centred on the mean. The Methods rule is the main reading and the code's is a variant.
- **Confidence coding (1–6) and the baseline:** both are taken from the code, and the author must check the coding in the dataset.
- **Behaviour tolerances:** I used the standard error of the mean (the stated SD divided by √n) instead of the stated SD or the 10% default, since these are means of the same sessions. The reason is given in the file.

**Details the paper leaves open, with the readings named**
- **Fig. 2 baseline:** the mean over all WM trials, or over the rows of the code's table.
- **Fig. 2b, e rows:** one row per trial, or one row per picture as the code does.
- **Fig. 2c, f model:** main effects only, or with the accuracy × load interaction.
- **Fig. 1e and the LTM response times:** low confidence as unsure and guessing pooled (the code), or as the mean of the two. Response times above 5 s excluded or kept.
- **Fig. 3b outlier step:** applied over both areas together, or within each area.
- **Fig. 3c, 3e units:** baseline-normalised rates or spikes per second.
- **Fig. 3e binning:** 200 ms windows in 25 ms steps (Fig. 2a legend), or 50 ms bins (the code). The cluster-forming threshold is not given; I took FieldTrip's default of 0.05 and noted that it could change the cluster's extent.
- **Fig. 3g rows:** all non-preferred pictures, or only trials holding no preferred picture.
- **Fig. 3h rows:** trials whose first picture is preferred, or trials with a preferred picture in any slot.
- **Fig. 4b which neurons:** at least 10 correct trials per class, or at least 10 in each group compared. The AUC is oriented to each neuron's preferred direction.
- **Fig. 4d:** two confidence codings, and spikes per second or rates normalised to the WM baseline.
- **Fig. 4e, f:** the random intercept is the MS neuron or the pair; all old-picture LTM trials or hits only; whether a neuron that is both types is paired with itself; and the rate units. The Methods sentence on this GLM lost its variable names.
- **Standard choices that cannot change an outcome:** the d′ correction, which side of the median ties go to, ≥ for the Fig. 4c p-value, and permutation seeds.

**Missing from the paper**
- **Neuron totals don't agree:** Table S1's recorded units sum to 973, against 950 isolated and 883 analysed in the Methods. The session-count claims allow for this.
- **Healthy controls:** the data of the 100 healthy participants (Fig. S1) are neither deposited nor located, so I made no claim for them.
- **Missing units:** no text gives the axis units of Fig. 3c–f and 4d–g, so they are named as open readings.
- **Whole analyses without code:** nothing a claim needed is entirely absent, but every analysis except Fig. 3a, the neuron selection and the behaviour plots rests on the Methods and legends alone.
