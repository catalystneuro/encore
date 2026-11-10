I've written `claims/kennedy-2020.yaml`: 39 claims, nothing committed. All 38 quotes pass the checker word for word. It reports two problems, both p-values the table prints as "1.80E‐05" and "5.20E‐05" (`fig1km-thigmotaxis`, `fig1lmn-silencing-before`). The checker doesn't know that number format, and I confirmed both by reading Supplementary Table 1. Because of these two, the checker still exits non-zero.

**Text read.** The accepted author manuscript in Europe PMC (PMC7606611), not the version of record. It has the main text, Methods, figure legends and Extended Data legends 1 to 10, plus Supplementary Table 1 (the statistics table). No main-text PDF was supplied, so I read no figures; the text and legends were enough.

**Code read.** github.com/DJALab/VMHdm_persistence at commit 7e5911b. It has the photometry scripts, the Fig 3m decoder, the Fig 2d/3b decay fits, the ED 7c cross-day correlation and the six network models. It has no code for picking responsive cells, peak times, the preference index, the PCA, the time-resolved decoders, the autocorrelation of the imaging data, or the similarity scores. Two helper functions the model scripts call are also missing.

**Claims.**
- 38 have quotes; one (`ed3de-openfield-vs-headfixed`) is `inferred`, read from legends and the supplement table.
- 16 have statistics, all from Supplementary Table 1 plus the r values in the ED 3h legend.
- 10 have expected values; 29 have criteria.
- 3 model claims are `with_inputs`, with the model code pinned as the outside input.
- 19 claims are on data the dataset doesn't hold: photometry, behaviour, slice and silicon-probe recordings. I kept them as `data: dataset`; the paper says these data are available on request.

**Details the paper leaves open, with the readings named:**
- **Responsive cells:** whether the 1 s windows slide or are fixed bins; whether the baseline SD is over frames or over 1 s means.
- **Cell counts:** cell-days pooled versus distinct tracked cells. The "78 tracked" can be a mean per mouse or a total.
- **The one mouse imaged at 20 Hz:** resampled to 11 Hz by averaging, as a standard choice.
- **Peak-time search window:** 0 to 30 s or 0 to 45 s.
- **Inhibited cells:** the Methods define only excitation, so I named a mirror of the 4-SD rule or a mean below the threshold.
- **Fig 3k:** excited only versus excited or inhibited; denominator of responsive cells or all cells; pooled versus mean over mice.
- **Preference histogram:** the Methods' formula runs 0 to 1 but the histogram runs −1 to +1, so I used the signed form.
- **Fig 2d fit:** which trials are used (the code uses the first trial; the Methods fit each trial), and the fit window (Methods 30 s; code −18 to 50 s, kept as a variant).
- **Decoder response window:** the code's baseline-subtracted mean after onset versus the Methods' −30 to +60 s.
- **Time-resolved decoder:** with or without baseline subtraction.
- **PCA:** the legend plots 5 trials per stimulus out of 6 presented.
- **Autocorrelation:** all cells versus tracked cells; the code's 1 Hz smoothing kept as a variant.
- **Specificity score frames:** 0 to 45 s as the score defines it, or 0 to 30 s where the correlation is defined.
- **"Matching" or "satisfying" the model scores:** no cut-off given; I named the mice's leave-one-out score range, or a ranking.
- **Model parameters:** the code's scripts differ from the Methods (for example, the low-gain script has g 2 and g_inh 2.4 against the Methods' 1 and 8.8). The Methods are followed and the code is a variant.

Many imaging claims say only "many", "most" or "above chance", with no number. For those I set thresholds or tests myself (for example at least 10% of cells, or AUC ≥ 0.9), and each criterion says the threshold is set there, not taken from the paper.

**Missing.** Nothing a claim needed is missing from the paper. The Methods and the legends cite different panel numbers in several places (decoder, confusion matrix, preference histograms); I followed the legends and recorded this in the opening comment. Supplementary Table 1 gives n = 8 mice for Fig 1g/h where the legends say 6; both are recorded.
