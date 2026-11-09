I wrote `claims/000939/10.1038-s41593-024-01588-5.yaml`. The quote checker passes it with no problems: 34 claims, 34 quotes, 9 statistical values found in the text. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC11001581): main text, figure legends, Methods and Extended Data legends. Both supplements were there: the Supplementary Methods on model fitting and theory, and the Reporting Summary. The main article's PDF was not supplied, so I never saw the figures. Values printed only on figure panels are not recorded, for example the r values of Fig. 6c, the CV of Fig. 4f and most p-values.

**Code read.** figshare doi:10.6084/m9.figshare.24921252, version 3: `MatlabCode_Duszkiewicz2024.zip` (md5 8f391dec…) and `SessionLists_ForAnalysis.zip`. It has the MATLAB code for every analysis except the simulations. The Python code for the simulations and the model fit (Fig. 4, Extended Data Fig. 5) is not deposited.

**Claims.**
- **Counts:** all 34 have quotes, none is `inferred`, and all 34 have criteria.
- **Statistics:** only 6 claims have a statistics entry. Most legends print a z value and no p-value, and the schema needs a p or an interval, so those z values are written into the criteria.
- **Data:** 22 claims use the dataset. 12 use data held elsewhere: ADN, cue rotation, Neuropixel and ADN opto data on figshare, plus the simulations, the model fit and the anatomy, which are not deposited anywhere.

**Where the Methods and code disagree.** The Methods are followed and the code's choice is named as a variant:
- **Cell classes:** the trough-to-peak cut is 0.4 ms in the Methods and 0.35 ms in the code.
- **KL divergence direction:** the Methods give D_KL(σ_i‖S); the code computes D_KL(S‖σ_i).
- **Smoothing in the stability analyses:** 3° in the Methods, 2° in the code.
- **Width tests (ED Fig. 7d,i):** the legends say Wilcoxon signed-rank; the code uses a rank-sum test.
- **Cross-correlogram window:** ±50 ms in the Methods, ±25 ms in the code.
- **Multipeak filter:** the code as shipped drops multipeaked HD cells from every Fourier analysis. The legends' n = 1,602 shows Fig. 3 used all HD cells, so the filter is treated as the ED Fig. 3k control only.

**Details left open, with the readings named for each:**
- **Fourier power:** the squared modulus (what the code computes, and what the Parseval check needs) or the root mean square (the Methods' wording).
- **HD threshold:** a fixed 0.2 bits per spike, or the 99th percentile computed from the time-reversed controls. The HD fraction is 87% in the Results and 85% in the Methods.
- **Opto exclusion:** the Methods' sentence allows excluding cells that fail both tests or either test; the code uses the correlation test alone.
- **Cue rotation exclusion:** an epoch is dropped if it fails either condition, or both.
- **ED Fig. 3g distance:** the KL divergence the legend names, or the Euclidean distance the code uses.
- **"Similar" proportions (Fig. 3h):** the same rank order, or each within 10%.
- **"The cell population" for the 98% power figure:** FS and HD cells pooled, or each separately.
- **REM comparison (Fig. 7d):** the WAKE Isomap curve (legend) or the real-HD WAKE curve (code).
- **HD-FS pair count:** 8,992 in Fig. 6c against 18,992 in ED Fig. 9d.
- **Legend n values that look like slips:** n = 52 in ED Fig. 7i and n = (83, 52) in Fig. 5e, read as 83 and 46.
- **Decoding:** the Methods give no decoder; the code settles it.

**Missing from the paper.**
- **Simulation and model-fit code:** not deposited. The two claims built on them (Fig. 4a–d,g and Fig. 4h) can't be tested from the recordings.
- **Anatomy images (ED Fig. 6):** not deposited.
- **Session coverage:** the dandiset holds 31 of the paper's 32 PoSub sessions. Whether it has the control-virus opto sessions is for the author to find.
