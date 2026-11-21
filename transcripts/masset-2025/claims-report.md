I wrote `claims/masset-2025.yaml` with 23 claims. The quote checker found no problems (23 claims, 23 quotes, 26 statistical values). Nothing was committed.

**Text read.** `paper/10.1038-s41586-025-08929-9.txt`. Its header says "version of record", but the body is the PMC author manuscript (PMC13254605). It has the main text, figure legends, Methods, the legends of Extended Data Figs 1 to 10, and the data and code statements. The paper has no supplement beyond the Extended Data. The extraction drops inline equations and symbols, and the code supplied the values that mattered. No PDF was available.

**Code read.**
- **Analysis code:** the MATLAB scripts in the Mendeley deposit (doi:10.17632/tc43t3s7c5.1, version 1). I did not open its data files.
- **Simulation code:** github.com/pablotano8/multi_timescale_RL at commit 37f11c6.

**Claims.**
- All 23 have quotes; none needed an `inferred` note.
- 15 record statistics.
- 21 have criteria; the other two (mixing model and branching task) are judged on their expected values alone.
- 18 rest on the dataset. Four are simulations (`data: elsewhere`) and one is the mixing-model claim, whose code is in neither deposit.

**Details the paper leaves open, with the readings named:**
- **Neuron selection, cued delay task:** the exclusion counts disagree (17 + 11 + 4 = 32 removed from 78, yet 50 kept; Extended Data Fig. 3b shows 23 non-selected and Fig. 3c 13 excluded). The criterion is applied as written and the counts at each step are reported. The SALT threshold for identifying dopamine neurons is not given here, so the dandiset's own labels are used, with the Mendeley selection flags as a variant.
- **Decoder:** the function is missing from the deposit. Readings: all singular components (Eq. 21-22), or the first 12 as elsewhere in the code.
- **Lick onset (Fig. 2b):** no definition. Readings: half-rise threshold, or pre-cue mean plus 2 s.d.
- **Lick window (Extended Data Fig. 5):** 0.6 s after the cue in the Methods decides; the code's 0.2 to 0.8 s is a variant.
- **Split-half reliability (Extended Data Fig. 3f):** which neurons are correlated. Readings: the 50 selected, or all fitted.
- **Bootstrap correlation (Fig. 4b):**
  - Which estimates are paired: the code draws from the first half-fits only; the other reading draws from all 200.
  - Number of pairs: 10,000 in the Methods, 100,000 in the code (variant).
  - The t-test's null is taken as zero.
- **Trials per session:** readings for which trials count (open-loop only or all trials for VR; four-odor trials or all trials for the cued delay task).
- **Cue response:** taken as the raw rate, since the fit has its own baseline term.
- **VR value-function fit:** random initial values, so a standard seed is recorded.

**Missing from the paper or its deposits:**
- The helper functions `DecodeTime`, `rsquare`, `hist2samples`, `ExpResponse`, `HypResponse` and `compute_psth`.
- The code for the mixing model, and its sharing parameter, which the extraction dropped.
- The definition of the selection flags (`Valid.OdorNew`, `Valid.VR`) used to pick the analysed neurons.
- Whether the dandiset holds the cued delay task's units is for the author to find.
