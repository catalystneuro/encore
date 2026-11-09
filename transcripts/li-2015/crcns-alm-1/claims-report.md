I wrote the claims file for CRCNS alm-1 at `claims/crcns-alm-1/10.1038-nature14178.yaml`. The quote checker reports 29 claims, 29 quotes, 18 statistical values and 0 problems. Nothing is committed.

**Text read**
- **Version:** the version of record, as text extracted from the PDF: main text, Methods, and the legends of Figs 1–5 and Extended Data Figs 1–7.
- **Supplement:** the paper has no separate Supplementary Information.
- **Figures:** I opened PDF pages 2, 3 and 5 to read Figs 1d, 2c, 2d, 3e, 3f, 3i and 5b.
- **Code:** the paper links none. The dataset's own MATLAB scripts are dataset files, so I did not read them.

**Claims**
- **Quotes:** all 29 have a quote; none is inferred.
- **Statistics:** 12 claims carry statistics. The stars in Figs 1d and 5b were assigned to their comparisons by reading the figure.
- **Expected values:** 13 claims have them.
- **Criteria:** 27 claims have a criterion.
- **Coverage:** the claims cover photoinhibition, task performance, unit counts, selectivity and its time course, error trials, contra/ipsi balance, the fast-spiking neurons, tagging counts and latencies, PT/IT selectivity, reaction time, imaging, photoactivation and dose response, high-power licking, anatomy, and Extended Data Fig. 7.
- **Not in the dataset, going by its description:** the imaging, photoactivation behaviour, photoinhibition and anatomy claims have no data in the dataset. They are included so the main findings are covered.

**Details the paper leaves open, and the readings named**
- **Response epoch length:** 1.3 s or 1.5 s.
- **Lick-early trials in the neural analyses:** dropped or kept.
- **Tagging-stimulation trials:** left out of the task analyses. The paper is silent on this; the file says so.
- **t-test variance:** Student (main) or Welch (variant).
- **Fig. 2d labels:** the text and the figure swap which of 389 and 304 is "peri-movement only" and which is "both". Both readings are named.
- **Fig. 2e:** the paper names no test, so I used the Fig. 3f/j bootstrap. The counts 427 and 485 are read from the Fig. 2c axes.
- **Population contralateral bias (P = 0.13):** all 912 selective neurons or all 1,245 putative pyramidal neurons.
- **Fig. 3f, onset 570 ms, 34% and −19%:** all tagged neurons (legend) or only selective ones (Methods). Onset found by a sustained or a first-crossing significance rule. Window either 570 ms before the cue to the cue, or extended through the response epoch. Percentage relative to the window's mean rate or the pre-sample rate. Onset tolerance is ±100 ms, half the 200 ms averaging window.
- **Antidromic jitter:** first pulse only or both pulses. Values printed to one decimal count as matching when they round to the printed value.
- **Selectivity time course and population correlation:** two readings of "emerged" and "beginning". The 0.5 correlation bound is read from the figure and marked as an assumption.
- **Error trials:** minimum of 1 or 5 error trials of each type.
- **FS neurons:** baseline is the whole pre-sample period or the last 0.5 s before it. Selectivity is the fraction of significant neurons or the size of the rate difference. The paper reports no test.
- **Performance (78.4%) and reaction time (61.1 ± 10.5 ms):** averaged over sessions, over mice, or over pooled trials, and over which trials and mice. The paper's numbers cover 42 mice.
- **"Large" differences and contra-suppression:** top quarter or top tenth. The paper does not define contra-suppression, so the file gives a definition and marks it as an assumption.
- **Extended Data Fig. 7 "changes in activity":** a selectivity difference, or the fraction of neurons with changed spike counts.
- **No tests given:** the paper reports no test for the sample-versus-delay comparison, the second-pulse jitter, or dose monotonicity. The criteria judge these by direction and say so.

**Missing from the paper:** nothing a claim needed. The full text, Methods and legends are all present.
