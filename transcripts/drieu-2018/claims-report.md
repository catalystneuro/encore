I wrote `claims/drieu-2018.yaml`, and the quote checker passes it with 0 problems (all 86 recorded statistical values found in the text). Nothing is committed.

**Text read**
- The version of record, for the main text and the Fig. 1–3 legends.
- The author manuscript (HAL hal-02330673v1), for the Methods, the Fig. 4 legend and figs. S1–S13 with their legends.
- Page 5 of the version of record (Fig. 4 and the closing paragraphs) is missing from the extracted text, so the Fig. 4 legend is quoted from the manuscript. I could not render PDF pages because poppler is not installed, so some figure values could not be read.
- Code: FMAToolbox at commit 6bbb366. It has general functions (decoding, remapping test, ripple detection, field statistics) but not the paper's scripts for trajectory scores, quadrant scores, z-proportions or bias correlations. Where its defaults differ from the Methods, the claims follow the Methods.
- The dataset's description says the authors' own scripts are in the archive. I did not read them, since they are part of the dataset's files.

**Counts**
- 35 claims: 34 have quotes, and 1 (fig. S5B per-rat ANOVAs) is marked inferred.
- 30 have statistics, 7 have expected values, and all 35 have criteria.

**Discrepancies noted in the opening comment**
- The two versions print different P bounds for Fig. 1C (10⁻³ against 10⁻⁴) and Fig. 1E (10⁻¹⁰ against 10⁻¹¹); the version of record is used.
- The Methods describe "three rats" with tetrodes and "three rats" with octrodes, though the paper has five rats.
- The main text compares sleep measures "across animals", while the fig. S11 legend compares them between sleep conditions; the legend's comparison is tested.

**Details the paper leaves open, with the readings named**
- **Place fields:** minimum field size (none, or the toolbox default of 10 bins); whether a cell's second field counts.
- **Theta LFP:** which channel (the one with the most theta power, or the mean of the pyramidal-layer channels); spike phase (interpolated between peaks and troughs, or the phase of the theta-filtered signal).
- **Slopes:** conversion to m/s (each cycle's duration, or the mean theta period).
- **Joint score-slope plots:** matrix bin sizes (a standard grid, plus half and double); what counts as "high-value" (score above the shuffled 95th percentile and slope above 3 m/s).
- **Sleep events:** whether the candidate-event mean and s.d. come from SWS only or the whole sleep session; whether "restricted to ripples" means any overlap or the event's peak inside a ripple.
- **Remapping:** which cells enter (field in both conditions, or in either); circular or linear cross-correlogram.
- **Unassigned P values:** which pairs the P values belong to in Figs. 2D, 2F, 3C and 4E.
- **Fig. 2B power:** the unit of the ANOVA (per rat, or per spectrogram window), since P < 10⁻⁶ is hard to reach with 5 rats.
- **Replay proportion (Fig. 4E):** whether a positive slope is also required.
- **Forward replay (Fig. 4F):** compared with reverse within the session, or with baseline sleep.
- **Bias correlations:** which theta cycles count as sequences (all analysed cycles, or only significant ones).
- **Smaller choices made outright:** fig. S8 matches mean rate or peak in-field rate; fig. S9 drops bins highest-error first; fig. S10 decodes each lap from its own laps or the others.
- **Fixed choices that cannot change the outcome:** chronux defaults for spectra, 1000 surrogates for bias correlations.
- **Choices made here:** 95% as the threshold for "covered the entire track", because fig. S2C's values are not legible in the text; and the assignment of the Fig. 3B and fig. S5B values to conditions, read from panel order.

**Missing from the paper:** the paper's own scripts are not linked (only the general toolbox).

The repository also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone; only the claims file is mine.
