I wrote `claims/peron-2020.yaml`. All 30 quotes pass `tools/claims_check.py`. The checker still reports 7 problems, all "value not found": these are P values printed only inside figure images that the text extraction drops, P = 0.098 in Extended Data Fig. 5 and the six behaviour P values in Extended Data Fig. 6 (0.863, 0.666, 0.065, 0.721, 0.710, 0.620). I confirmed each one on the rendered PDF pages.

**Text read.** The version of record: main text, figure legends, Methods, Extended Data Figs. 1–8 legends, Extended Data Table 1 and the reporting summary. The only supplementary information named online is the reporting summary, so no supplement is missing. I opened the PDF pages for the P values inside Figs. 2j–k, 3b, 3f–g and Extended Data Figs. 5–6, and for the rows of Extended Data Table 1. To render them I installed PyMuPDF into the temp directory.

**Code read.**
- **Analysis code** (github.com/peronlab/ablation, commit 74b7321, MATLAB). It supplied the mouse lists for each ablation type, the folder pairing for mice with two ablations in sequence, the session-file feature names, the shuffle rule, the bins and fits, and the example mouse 272761.
- **Simulation code** (github.com/jwittenbach/ablation-sim, commit a8b5583, from 2016). Its parameters (5,000 neurons, ablating 30) are not the published model's, so the model claims follow the Methods.

**Counts.** 31 claims: 30 with quotes, and 1 marked `inferred` (the per-mouse rows of Extended Data Table 1). 19 claims carry statistics, 33 test entries in all. All 31 have criteria. 7 claims are simulation findings, marked `data: elsewhere` because the model outputs were not deposited and must be regenerated. 9 are claims of absence, each judged at the 0.05 level the paper uses. Tolerances are 10% throughout: the paper's ± values are spread across mice, not uncertainty of the statistic. The file states this reason, plus two exceptions (a value of 0.000, and table changes near zero).

**Details the paper leaves open, and the readings named for each:**
- **Neuron counts in the Results (901 touch, 865 whisking, 932→716, etc.):**
  - (a) the code's rule: score above 0.1 only, keeping ablated neurons and neurons in both representations;
  - (b) the full membership rule in the Methods.
  - Extended Data Table 1 gives means of about 780 and 624, so the table and the text appear to follow different rules.
- **Exclusion cylinder around ablated neurons:** the Methods say 10 µm radius and 60 µm height; the code uses a signed depth difference under 30 µm, which also drops every shallower neuron within 10 µm laterally. The Methods version is the main reading; the code's is a variant.
- **Fig. 2m and Extended Data Fig. 5:** the code uses per-mouse means and pools neurons for the reported values; the legend says medians across mice. Both readings are named.
- **Fig. 3:**
  - Slopes could be fitted to the 0.1-wide bin means (code) or to the individual neurons.
  - The code's trial-average loader overwrites the left-trial average with the right-trial one, so only right trials enter; this is a variant against the Methods' concatenation of both.
- **Whisking-ablation percentile:** the Methods reading ranks ablated neurons among whisking neurons; the code ranks them among touch neurons' touch scores.
- **Extended Data Fig. 6:** the legend's signed-rank test against the code's rank-sum test, and KS tests on the raw samples against the code's tests on histograms.
- **Model:**
  - The input strength is fixed only by "most closely matching" the in vivo data. Readings: (a) match the 0.108 touch fraction, (b) minimise the KS distance to the in vivo Rtouch distribution.
  - The reset pulse strength (Extended Data Fig. 1).
  - The input strength for the slow, whisking-like input.
  - Whether the networks with 0 ablations enter the Extended Data Fig. 4 correlation.
- **Extended Data Fig. 2:** 7 ablations excluded for incomplete logs are not named.

**Missing from the paper.** Nothing a claim needed is missing. Two findings rest on data the paper describes but the dataset may not hold: the histology (glial reaction radii) and the simulation outputs.

I committed nothing. Other untracked files in the working tree (such as `.bashrc`, `.idea`, `scripts`) were not created by me and I left them alone.
