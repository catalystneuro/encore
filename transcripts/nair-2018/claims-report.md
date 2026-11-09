I wrote `claims/crcns-bf-1/10.1073-pnas.1712431115.yaml`. The quote checker reports 28 claims, 28 quotes, 37 statistical values and 0 problems. Nothing was committed.

**Text read.** I read the version of record (PNAS 115:1352–1357) from `paper/`, including the supplement (pnas.201712431si.pdf). The SI Materials and Methods are where the analysis methods are fixed. The paper links no analysis code; it only names the toolboxes it used (Wave_clus, CircStat, Chronux, BSMART, MVGC, SPSS). I couldn't render the PDF here because no renderer is installed, so I read the figures from their legends and the Results text.

**Claims.** All 28 claims have a quote and a criterion, 10 have expected values, and 24 carry statistics. They cover:
- behavior (time spent per behavior, speed);
- the main result, a 35 ± 3% drop in BF gamma in the arena, and that the drop is significant in each hemisphere;
- the bipolar recordings;
- the movement quartiles (Fig. 3B), the days and sessions (Fig. 3C), and the correlation with time in the arena plus the fast switch back to the home cage (Fig. 3D);
- gamma by behavior (Fig. 3F) and object exploration (Fig. 4);
- phase locking, PLI and spike width (Fig. 5);
- ACC and VC gamma, coherence and Granger causality (Fig. 6);
- the supplement: band powers (Fig. S2), unimodality (Fig. S3), excursions during arena exploration (Fig. S5) and locomotion (Fig. S6).

From its description, the CRCNS dataset holds BF LFP and the movement sensor only, for six rats with two home-cage and two arena sessions each. The claims that need ACC or VC recordings, spikes, object sessions, video scoring or day labels are kept, and their criteria say so.

**Details the paper leaves open, with the readings named:**
- **Epoch length:** 2 s, or 10 s as a variant.
- **Artifact rejection:** use the segments as delivered, or apply the paper's median + 1 SD rule again.
- **Unit of pairing:** the paper pairs hemispheres; the dataset allows rats, with the two sessions averaged or paired session by session.
- **FFT details:** a plain periodogram is used as a standard choice.
- **How the 35% (and the 5.62%) is formed:** the mean of per-recording ratios, or the ratio of group means.
- **Movement quartiles:** formed per recording or per rat with sessions pooled. The matched comparison uses either the paper's quartile 4 versus quartile 3, or the closest-movement pair. A repeated-measures ANOVA is shown as a variant.
- **Post hoc tests, which the paper doesn't name:** Tukey's HSD, with Bonferroni-corrected tests as a variant.
- **Correlation r = 0.72:** binned group time course, mean of per-recording r, or all epochs pooled.
- **"Rapid" switch to the home cage:** two one-minute readings.
- **Spike-width test, not named:** unpaired t test, or Mann-Whitney.
- **Burst "amplitude":** the absolute band-passed signal, or the Hilbert envelope.
- **Excursions:** the histogram bins that set the threshold, the power scale (raw, log10 or normalized), and which arena session is used.
- **Unimodality:** which session per rat.

**Missing from the paper:**
- **Unreadable p-value:** the extracted text prints the ACC gamma p-value as "P < 0.0", so that claim has no p-value recorded.
- **No power units:** the paper never states the power units, so the excursion threshold (2.6) and the 0.56 gamma increase can't be placed on a scale. The 0.56 value is judged only under a reading whose scale puts the threshold near 2.6.
- **Unlabelled n's:** the n labels in Fig. 3 can't be tied to their panels from the text alone.

The SEM-based tolerances (for example ±3 on the 35% drop) will be strict, because the dataset has 6 rats where the paper had 22 hemispheres.
