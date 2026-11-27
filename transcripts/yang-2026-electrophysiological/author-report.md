I've done steps 1 to 6 for yang-2026-electrophysiological: the entry is written, locked and run clean with `entry.py all` (it passes, about 23 min), the record `attempts/yang-2026-electrophysiological-01.yaml` is written, the checks report 0 errors, and the handover is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome | Rests on an assumption |
|---|---|---|
| fig1c-cells-per-protocol | partially_reproduced (ramp 3275 and brief pulse 2166 match; no long-pulse reading is within 2270 ± 227: 3276, 1957 or 1881) | yes |
| fig1d-driver-line-coverage | reproduced (named lines are the 9 and 11 largest; 8 shared) | yes |
| fig2a-longpulse-low-dimensional | not_reproduced (0 of 24 readings; PC2 is 18.7 to 25.3% against 15 ± 1.5) | no |
| fig2b-longpulse-continuous-biased | reproduced | yes |
| fig2d-longpulse-loadings | reproduced | yes |
| fig2c-longpulse-centroid-distances | reproduced | yes |
| fig2e-longpulse-pc2-pvalb-high-vip-low | reproduced | yes |
| fig3a-ramp-variance | reproduced (reading b, dV/dt spikes) | yes |
| fig3b-ramp-continuous-biased | reproduced | yes |
| fig3d-ramp-loadings | reproduced | yes |
| fig3e-ramp-recruitment-current-order | reproduced | no |
| fig4a-brief-response-variance | reproduced (only with the 50 ms window) | yes |
| fig4b-brief-continuous-biased | reproduced | yes |
| fig4c-brief-response-pc1-loadings | reproduced | yes |
| fig4e-brief-response-base-alignment | reproduced (0.886 and 0.876, n 2166) | yes |
| fig4f-brief-gain-vip-cck-high | reproduced | no |
| disc-brief-gain-sncg-cck-non-pvalb | reproduced | no |
| fig5a-longpc2-ramppc1-centroids | reproduced (r 0.900, p 0.0009; Sncg, not Vip, is lowest on ramp PC1) | yes |
| fig5b-long-ramp-distance-alignment | partially_reproduced (r 0.881, above 0.707 ± 0.071) | yes |
| fig5c-balanced-correlations-positive | partially_reproduced (all positive, 2 of 6 within tolerance) | yes |
| fig5d-f-true-above-shuffle-null | reproduced (labels shuffled in both geometries; one-geometry shuffle gives p 0.051 for long pulse against gain) | yes |

No outcome changes across the five seeds.

## 2. Dataset, assumptions, questions

**Dataset.** The pinned version is 0.210913.1639: the paper cites it and it is the only published version. It holds 4435 files, one cell each, from 1040 mice. Units, the 50 kHz sampling rate, the 25 pA/s ramp slope and the clock shared by command and voltage all check out.
- **Critical finding:** one recording is deposited twice. Sessions 680563483 (Vip-Cre) and 680897463 (Ndnf-Cre with Slc32a1-FlpO) hold identical sweeps under two subjects. I left both out of the line analyses.
- The driver line exists only inside the genotype string. Sncg cells carry a Flp allele and no Cre.
- Truncated sweeps are padded with zeros, not NaN.
- X5SP_Search_DA_0 exists only in the newer stimulus set (2597 cells).

**Assumptions** (all stated in the record and in `geometry.py`):
- My own QC thresholds and per-sweep feature definitions.
- The driver line is the gene of the first driver allele.
- Long pulse uses every long square step and leaves out the command-binned features.
- Ramp uses the 8 features of Figure 3D.
- Brief response uses the 10 features of Figure 4C plus the two gains, with a 50 ms window.
- Spikes are detected at dV/dt of 20 V/s, the Allen pipeline's criterion.
- Mean imputation.
- Lines are included if they are the largest groups.
- Balanced resampling draws the smallest retained count per line, and the null shuffles labels in both geometries.

**Questions for the paper's authors** (four `methods_unavailable` findings):
- What defines the 2270 long-pulse cells?
- Which spike criterion, response windows and feature lists were used?
- What are the resampling and null settings, and what do the stars in Figure 5C mean?
- What is the rule for including a driver line?

**Questions to a reader:** none.

## 3. Where the protocol was unclear
1. Criteria say "reproduced under a reading", while step 1.6 says to adopt the best-supported reading for open details. It does not say how the two combine when details multiply across dependent claims (up to 384 combinations for fig5b). I fixed one main reading per geometry from the paper and applied the criterion's readings on top of it.
2. `depends_on` does not say which upstream reading a downstream claim should inherit. I used the main reading.
3. A value that misses tolerance because the effect is stronger than the paper's (fig5b, r 0.88) fits no outcome definition, since "partially" is defined as "weaker or in part". I used partially_reproduced.
4. The suggested clock check (decoding a task variable) does not fit icephys data. I used the sign of the command against the voltage change before and after onset.
5. The protocol gives no cheap way to check for duplicate recordings across 4435 files. I compared per-sweep summaries.
6. The protocol has no guidance on caching derived data during development. I cached per-sweep features in TMPDIR for development only; the notebook streams everything itself.

## 4. Runtime and failures
- The run took about 2 h 15 min (00:34 to 02:49 UTC).
- The notebook takes about 23 min: 15 min streaming in 40 processes, peak memory 0.7 GB. That is over the 10-minute aim and under the 60-minute limit.
- Nothing failed and no file errored. I ran it in full three times after changes that touched only text and the data-check printout; every analysis result was identical.
