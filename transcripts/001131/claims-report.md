I wrote the claims file at `claims/001131/10.1016-j.cell.2024.08.015.yaml`. The quote checker passes it with 0 problems.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC11490375), not the version of record. It has the Results, Discussion, STAR Methods, and the legends for both the main and supplementary figures. The supplement PDF holds only the images of Figures S1 to S7, so I could read the star levels for the supplementary panels. The main figures are not in the files I was given.

**Code read.**
- DJALab/VMHvl_MPOA_dynamics at commit ed83c41 holds one notebook that draws flow fields for synthetic linear systems. It has no code for this paper's data.
- Its README points to the rSLDS notebook in lindermanlab/ssm (commit eb6c8aa). I took the rSLDS fitting settings from that notebook.

**Claims.** There are 34, all with quotes. 24 have statistics (29 p-values) and all 34 have criteria. One claim, the RNA-seq co-expression figures, uses outside data, from the Kim et al. 2019 atlas. The claims cover the RNA-seq atlas, slice imaging, behaviour, fiber photometry, the miniscope single-unit analyses, the rSLDS time constants and line attractor score, the activity on the first rSLDS dimension, autocorrelation half-width (ACHW), and the rSLDS fit to slice data.

**Details the paper leaves open, and the readings named for each:**
- **"Nested" Mann-Whitney and KS tests:** (a) on all units pooled; (b) on per-mouse means or medians.
- **Sigma baseline:** (a) the whole pre-intruder period; (b) the 7 s before the first intruder.
- **Analysis window:** the Results say the first 2 minutes and the Figure 4 legend says 1 minute; both are named. The same 1 or 2 minutes apply to the "first 1–2 minutes" ACHW windows.
- **Number of control mice:** the Results say 4, while the legends and Methods say 5. Both are named.
- **Fractions:** pooled over units, or the mean over mice. "Increase" or "reduction" as a relative change, or as percentage points.
- **rSLDS fit:** which frames are fit (the male-intruder part, or the whole session); z-scored or sigma-normalised traces; seeds 0 to 3, with the outcome the one all seeds give.
- **Which dynamics matrix gives the time constant:** (a) that of the state in which attack occurs; (b) the mean over the three states.
- **"Attack in a single state":** a majority of attack frames, or at least 90%.
- **Fit-quality horizon:** forward-simulation score at 1 s or 5 s.
- **Choice probability:** how the direction is computed, how bouts are shuffled, and which trace is used. Every combination is run.
- **ACHW:** which units count as weighted on a dimension (by largest weight, or the top 25%); one autocorrelation, or the mean over trials.
- **Other details:**
  - SVM regularisation: C = 0.1, 1 and 10.
  - "Clear separation" in the PLS plot: two measures named.
  - Post-intruder window: until the next intruder, or the first 60 s.
  - Pre-bout baseline for the bout-triggered averages: 2 s or 3 s.
  - Rate of the behaviour decoder: the Methods say 15 Hz against 10 Hz traces; the data's own rate is used.
  - Slice rSLDS: 2 or 5 dimensions, 1 or 3 states.

**Missing from the paper that some claims needed:**
- Which significance stars go with each main-figure panel. Where those were unreadable I recorded p < 0.05, the paper's lowest level.
- The rule for a responsive cell in the slice data.
- The expression threshold for the atlas.
- How ACHW is computed, which the paper cites to Remedios et al. 2017.
- How the rSLDS was fit, which it cites to Nair et al. 2023 and which the code fixes only in part.
- The test for Figure S4A. I used Mann-Whitney, the paper's test for the same measures elsewhere.
- Any measure of the flow-field shape. That claim is judged on the line attractor score instead.

Nothing is committed.
