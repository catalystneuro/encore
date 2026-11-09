I wrote `claims/001193/10.1038-s41562-022-01334-6.yaml`. The quote checker passes with 0 problems (24 claims, 24 quotes, 9 statistical values). Nothing is committed.

**Text read.** The version of record (Nature Human Behaviour 6, 1104–1111): main text, figure legends, Methods, reporting summary, and the Supplementary Information PDF (Table 1, Figs. 1–10, the stimulus sentence lists). The paper links no code; it is "available from the authors upon reasonable request", so no repository was read. The PDF could not be rendered here because poppler is not installed. So numbers printed only inside figure panels, such as the region counts of the Fig. 2b Venn diagram, are not used.

**Claims.** There are 24, all with quotes and all with a criterion. The task-structure count of 32 sentences per condition comes from the supplement's lists; no sentence of the text gives it, and the criterion says so.
- **Statistics:** 9 entries on 4 claims: the six pairwise latency p-values of Fig. 3d, the t-test against 25% chance in Suppl. Fig. 9, the ANOVA in Suppl. Fig. 10b, and the word-frequency t-test.
- **Coverage:** participants and task structure, behaviour, frequency band, IFG localisation, effects only after the keyword, the 58 violation electrodes, 49 single-type and 9 co-activated electrodes, the half-split and duration robustness checks, Euclidean similarity, the COM overlap, the non-linguistic control, absence of spatial separation (pooled and per participant), the 3.25 mm circuit diameter, prediction from correct sentences, latency values and their tests, latency not depending on location, the 400–700 ms classification peak, the duration differences, the low-frequency effect in the non-linguistic task, and keyword frequency matching.
- **Data:** one claim (word frequency) is `with_inputs`, using the corpus the paper names. The rest are `dataset`. The dandiset's description says it holds high-gamma activity only, so the band-comparison and low-frequency claims (Fig. 1b, Suppl. Figs. 3, 4, 7c) are likely untestable.

**Details the paper leaves open, and the readings named:**
- **Resting state (E1):** the 800 ms fixation, or fixation plus the 500 ms blank (1,300 ms).
- **"More than 50 ms" (V1):** consecutive samples, or total samples.
- **"> 0.55 z" (V2):** the violation's own amplitude, or its difference from correct sentences.
- **The F value (F1–F3):** maximum over samples, mean over significant samples, or the F of the time-averaged amplitude.
- **Fractional-area latency (L1–L3):** the violation response or its difference from correct sentences; area over 0–1,000 ms or over the discriminating period; negative values set to zero or kept.
- **Latency electrode set:** per-condition violation electrodes, or responsive electrodes in pars opercularis, pars triangularis and precentral gyrus. The paper's n = 106 cannot be derived from anything stated.
- **Euclidean distance:** what the condition vectors are, and which pair "syntactic to semantic" means.
- **Half-split:** which half of the sentences is "first".
- **Duration-metric electrode selection (79 electrodes):** with or without the amplitude rule.
- **COM "responded":** passing the violation test, or F > 4.
- **Non-linguistic threshold:** 0.01/256, with 0.05/256 as a variant.
- **Permutation test for spatial separation:** centroid distance or KDE-peak distance.
- **kNN prediction:** which electrodes count as non-responding, the cross-validation scheme, and feature scaling.
- **Time-resolved classifier:** the paper does not name it; each of the three Methods classifiers is a reading.
- **IFG labels:** with or without pars orbitalis.
- **Fig. 3e axes:** the legend says "x or y"; both MNI axes are used.

**Missing from the paper:**
- the analysis code;
- the equation of the circuit-size estimate is garbled in the text; it was read as p = 1 − (r − 0.5)/r, which matches the figure's 15.6% and 3.25 mm;
- the non-linguistic correction factor;
- how the 106 electrodes of Fig. 3d were selected;
- the Supplementary Excel file and Source Data were not supplied, but no claim needs them.

The p-value printed for SEM against SYN-P onset (1.83 × 10⁻⁵, for means only 9 ms apart) looks surprising. It is matched as printed.
