I've written `claims/000336/10.1038-s41597-023-02214-y.yaml`: 18 claims, all 18 with quotes. The quote checker found 0 problems. Nothing is committed.

**The dataset doesn't hold this paper's data.** The paper describes DANDI:000037, the OpenScope "Credit Assignment" project. By its title and description on the archive, DANDI:000336 is a different OpenScope project, "Dendritic Coupling": L2/3 and L5 somata and dendrites imaged in V1, LM, PM and AM, which the paper never describes. So:
- One link claim asks whether 000336 holds any of the sessions in the paper's Table 2. It is matched by subject and session ID.
- The other 17 claims are marked `data: elsewhere`, on DANDI:000037 version 0.230426.0054.

**Text read:** the version of record from Europe PMC (PMC10192216), with the full Methods, Technical Validation, Tables 1 and 2 and the figure legends. There was no PDF, so I saw no figures, only their legends. Supplementary Table 1 is not under `paper/`, but it repeats Tables 1 and 2 plus some notes, and no claim needs it. The other file in `paper/` (Keller and Mrsic-Flogel 2018) is a different paper the dataset also cites; I didn't use it.

**Code read:** the paper's analysis code (`OpenScope_CA_Analysis` at 046e7fe), its `util` dependency (2b05f95) and the stimulus code (`cred_assign_stimuli` at d056e0b). The code settles:
- which sessions are used: sessions 1 to 3 that passed QC, so 11 mice and 33 sessions;
- how SNR and signal are computed;
- the correlation smoothing (4-sample rolling mean);
- the onset and offset windows (±2 s);
- how ROIs are pooled across mice;
- the windows for Fig. 5.

**Statistics:** none. The paper says it runs no statistical analyses, so there are 0 statistics entries.

**Criteria:** all 18 claims have one, and 11 also have expected values. Counts of deposited records get a tolerance of 0, with the reason given.

**Details the paper leaves open, and the readings named:**

| Claim | Open detail | Readings |
|---|---|---|
| Table 2 sessions | The text says two mice failed QC; Table 2 shows three | Mice with a failed session among sessions 1 to 3, or any failed session |
| Session schedule | Which three sessions; how "three to six days" is counted | Sessions 1 to 3, or the three tracked sessions; days from first to last, or calendar days inclusive |
| ROI counts per session | Which sessions | The 33 analysed, all that passed QC, or all 50 |
| Tracked ROIs | The "theoretical maximum" behind 32 to 75% | Per plane, the sum of each mouse's smallest session count; per plane, the sum of mean counts; per mouse |
| Fig. 8 ordering variation | Overlap threshold; measure of variation | 10% or 20%; range over mean, or SD over mean |
| Stimulus fractions and blocks | How 7% and 5% are averaged; what "30 blocks" counts | Mean per session, or pooled; per stimulus, or per session |
| Fig. 5 | Which ROIs; which test (the paper names none) | All ROIs, or the legend's selection; Wilcoxon p < 0.05, or mean difference above 2 SEM |
| Fig. 7a, 7b | What "above 1" and "stable" mean | Median, or 25th percentile above 1; session medians inside the other sessions' interquartile ranges, or within 10% of the mean of the three |
| Fig. 7c | What "very similar" means | Dendritic median inside the somatic interquartile range; dendritic 99th percentile within 10% of the somatic one |
| 0.01% of pairs above r = 0.8 | The denominator | Pooled, mean per session, or session 1 only. Tolerance 0.005%, from rounding (reason in the file) |
| Fig. 9 | The test; the sign of offset transients | Above 2 SEM, or Wilcoxon, either sign. Gabor-only onsets are a variant, because the legend names only Gabor while the text and code use both stimuli |

**Missing:**
- The custom-modified ROI matching code is not public; the repository holds only its outputs. So the conflict counts in Fig. 8 (4 and 2) and the ordering-variation claim can only be tested by approximately rerunning the public matching package.
- Session QC status may not be in the files; Table 2 and the code's session table give it.
