I wrote the claims file at `claims/001347/10.1126-science.adt3971.yaml`. The quote checker passes every quote. It still exits non-zero on one item: it cannot find p = 1.8e-09 (fig2i). Table S3 prints that value as "1.80e-09", and I confirmed it by reading the table. Nothing is committed.

**Text read.** The version of record (Science, 29 May 2025): main text, Methods and figure legends. Both supplements: the MDAR checklist, and the Supplementary Materials with Supplemental Note 1, the legends of figs. S1 to S38 and Tables S1 to S3. Neither PDF tool (pdftoppm, PyMuPDF) was installed, so I could not look at any figure. The body of Table S1 is garbled in the extraction and I did not use it.

**Code read.**
- Zenodo 14920570, the human analysis code and mouse behaviour code: one git commit, b873ca5. It loads its data from dandiset 001347.
- Zenodo 14876694, the mouse electrophysiology analysis.py: no commit and no driver script.

**Dataset.** The archive description lists iEEG participants ("SD"), non-iEEG participants ("h"), mice ("m") and aggregated folders. The mouse Neuropixels data are in DANDI 001326, so the eight claims that need them are marked as data elsewhere.

**Counts.**
- 54 claims, all with a criterion; 53 have a quote.
- The one without a quote (fig5g) is marked `inferred`: its variance-explained values (0.954, 0.870, 0.927) exist only as figure labels.
- 36 claims carry statistics (188 statistical values in all); 29 carry expected values.

**Details the paper leaves open, and the readings named:**
- **Trials dropped at the start of a human session:** first two (fig. S1 legend and code) or first one only (Methods).
- **Late/early normalisation, non-iEEG cohort:** ratio of trial means (code) or mean of per-trial ratios.
- **Human coding-dimension z-scoring:** the Methods use a window from −0.5 to 1.5 s with baseline −0.5 to 0 s. The code uses −1.0 to 1.5 s with baseline −1.0 to 0 s, and reads the summary window on a time axis shifted by 0.05 s.
- **White matter in the coding dimension:** excluded (code) or kept.
- **Baseline for the human timescale:** 8 min (Methods) or 10 min (Table S3 and code). The fit starts at lag 0 or at lag one sample (code).
- **Human phase-locking windows and normalisation:** the 25-min windows and z-scoring of the Methods, or the 10-min windows and ratio to preinfusion of Table S3. The code for this figure is not released.
- **NMF factor identity:** the code's fixed order after its fit, or factors 1 and 2 matched to the paper's descriptions of them.
- **fig. S14G change score:** the code's (mean of pre and post) minus ketamine, or ketamine minus preinfusion as Table S3 has it.
- **Slow-oscillation claim (fig. S27):** CADSS threshold >10 or ≥10, and the cohort (the 7 included participants or every infused participant).
- **Mouse infusion trials:** the code's trials 23 to 37, or every trial starting 3 min or more after injection.
- **Mouse persistence start (fig. S2E):** the code starts 3.3 s after the last puff, or 0.3 s after it.
- **Fig. 5H/5I:** which of 0.870 and 0.927 belongs to ketamine and which to PCP.
- **Fixed here because the paper gives no measure:** "similar" eyelid closure (fig. S12D), the reward-licking claim (fig. S4), the skipped-puff claim (fig. S2O), and the spectral-change magnitude by region (fig. S15).

**Missing from the paper or its code:**
- The code for Fig. 6I (human phase locking) and fig. S27 is not in the release.
- The mouse electrophysiology record has no session lists or driver script.
- The CADSS scores sit in the code record (`data/cadss_across_pts.csv`, plus constants in one script); the dataset may not hold them.
- The verbal reports, the spontaneous-blink onsets and the lick data may not be in the dataset; the criteria say those claims are blocked if absent.
