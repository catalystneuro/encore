I wrote `claims/gable-2026.yaml`. It has 34 claims, and the quote checker passes with 0 problems (33 quotes, 52 statistical values found). Only 4 of the claims can be tested on DANDI:000010.

**Text read.** The version of record (PMC13612898, J Neurosci 46(38) e0974262026): Methods, Results, legends for Figures 1–5, Tables 1–8 and the Discussion. The same text file holds the supplement (legends and panel text of Figures S1–S5). Nothing the claims need is missing.

**Code read.** github.com/kerlin-lab/Gable_2026 at commit 688e662. It has one notebook per figure and a function library, but no data. For Fig. S4 it holds the coupling, pairwise-correlation and bootstrap code. It does not hold the step that builds the notebook's input from the DANDI files: unit, session and trial selection, binning, smoothing, and the trial-specific activity (each trial's activity minus the mean for its trial type).

**What the dataset can test.** DANDI:000010 (Li et al. 2015, ALM silicon probes) is only reanalysed for Fig. S4 and Table 5. These are the 4 dataset claims:
- **Session selection:** 11 mice, 20 sessions, 753 same-bin and 6,586 different-bin neuron pairs.
- **Lowest coupling bin:** neurons are more correlated within the bin than with other bins (mean difference 0.06, p = 7e-4).
- **Top three bins:** same result (0.02, 0.06, 0.1).
- **Middle three bins:** no significant difference (a claim of absence).

The other 30 claims rest on the paper's own two-photon imaging. That is not in a public archive, so they are marked `data: elsewhere` (not public). They still carry criteria taken from the Methods.

**Counts.** All 34 claims have criteria, 33 have quotes (one uses `inferred`), 22 have statistics and 21 have expected values.

**Details left open for the Fig. S4 claims, with the readings named:**
- **O1, which units count in a selected session:** (a) all high-quality units of a session that has at least 18 units above 0.5 Hz; (b) only the units above 0.5 Hz.
- **O2, "session-wide firing rate":** (a) over the whole recording; (b) within the analysis windows of the included trials.
- **O3, trials outside the four correct/incorrect × left/right types (e.g. early-lick or no-response):** (a) excluded; (b) kept, each with its own trial-type mean subtracted.
- **O4 and O5, standard choices:** smoothing within each trial, and a common window length if trial lengths differ. The bootstrap seed is not given either.
- **Tolerances:** Table 5 prints one significant figure, so for 0.02 and 0.1 I used the rounding interval of that digit instead of 10%, and say why in the criterion.

**Missing from the paper:**
- The paper's imaging data are not public. Code and data availability names the GitHub repository, which holds code only.
- The step that prepares the DANDI data for Fig. S4 is not in the code, so O1 to O3 rest on the text alone.
- The code's printed output gives 771 same-bin pairs where Table 5 prints 753. I noted it in the file and did not use it for any expected value.
- A few imaging criteria use measures I chose where the paper gives no number or test. They are marked "chosen here": the coupling median near zero, the dF/F0 group contrast, and the peak-time ordering.

I did not commit anything. The untracked dotfiles and `scripts` in the working tree were there before this run.
