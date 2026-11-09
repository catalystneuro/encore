**Verifier report, round 2: Johnson et al. 2019 on CRCNS fcx-3**

Cell numbers are 0-based positions in the executed `.ipynb`; the layout has changed since round 1. The claims file has 17 claims and the attempt record has 17 outcomes. Outside the notebook I ran one check of my own: a synthetic test of the PSI null in `$TMPDIR`, using no dataset files. It is described under fig4c.

### 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| table1-electrodes | partial | Yes. 187 channels and 1135 pairs (cell 17). |
| trial-counts | reproduced | Yes. Cell 20. |
| fig1b-accuracy | reproduced | Yes. Range 0.625–0.975; p = 0.283 (cell 23). |
| fig1b-rt-identity-slower | reproduced | Yes. p = 0.024, 0.005, 0.010 and 0.254 (cell 26). |
| erp-no-condition-difference (assumed) | not reproduced | Yes. The assumption is stated and reasonable. The outcome hardly depends on it: in the main configuration, 5 of the 6 neighbour × alpha-per-tail combinations give a cluster with p < 0.05 (or < 0.025 where that is the threshold). Only adjacent neighbours at 0.025 per tail give none (cell 29). |
| fig2-spatial-power | partial | Yes. 5 and 1 subjects, within one of the paper's counts. The percentages are off: 37.7 and 11.8 (cell 32). |
| fig3-temporal-power | partial | Yes. 5 and 2 subjects (4 and 2 with assignment b); no reading gets the percentages within tolerance (cell 32). |
| power-difficulty-subjects | reproduced | Yes. Holds under reading (b)(i) in every configuration. S3 breaks the converse (cell 37). |
| power-low-frequencies (assumed) | reproduced | Yes, by the letter. The assumption is stated and defensible, but weak: a "maximum" at the 2-Hz end of the range only means the density keeps rising below 2 Hz. Without counting that edge, the identity > other effect fails in every combination (cell 40). |
| fig4-maintenance-parietal-led | not reproduced | Yes. No subject is below −1.96 under either reading (cell 45). |
| fig4a-delta-theta-shift | not reproduced | Yes. 0 of 7 subjects above zero under both readings (cell 48). |
| fig4c-alpha-beta-shift (assumed) | partial | **No, the evidence does not support it.** See below. |
| directional-pairs | not reproduced | Yes. 1 or 78 delta-theta pairs and 74 or 104 alpha-beta pairs, all near the trial-shuffled surrogate (cell 51). |
| fig5a-delta-theta-epochs | not reproduced | Yes. No FDR-significant points (cells 54 and 56). |
| fig5a-identity-direction | not reproduced | Yes (cell 58). |
| fig5a-spatiotemporal-bidirectional (assumed) | not reproduced | Yes, by the letter, but the evidence is one pair in S1 (cell 60). The assumption is stated, but its reasoning does not address calibration (below). |
| fig5b-alpha-beta-no-sustained (assumed) | reproduced | Yes, by the letter. The significant points come only from reading (b)'s pair-level test (30 and 35 points, smallest p 2e-18). The 74 pairs it selects are about the number the trial-shuffled data select (71), and S3 supplies 44 of them, all treated as independent. No subject-level test is shown. Under reading (a) the outcome is partial. |

**Why fig4c is not supported, and why the PSI reading (b) assumption is weak.**
- The partial match rests on the sign of subject means that are all close to zero: −1.35 to 0.46 (cell 48).
- Under reading (b) with the Methods' null, z is not centred on zero for independent signals. I simulated 33 trials of independent 1/f and brown noise, 900-ms Hanning segments padded to 7.5 s, with one permutation of the parietal bins per shuffle, as `psi_z` does:
  - Reading (b): mean z −0.32 to −0.34, in both bands (SE about 0.04).
  - Reading (b), delta-theta: SD 0.75–0.82.
  - Reading (a): mean z about 0 in delta-theta and −0.13 to −0.17 in alpha-beta, with SD about 1.
- An offset of that size alone would put most subjects below zero. The data show the same pattern under (b): every maintenance subject mean in alpha-beta is negative, and 6 of 7 in delta-theta (cell 43).
- Cell 44 prints the surrogate's |z| > 1.96 rate and SD but not its mean.
- The record justifies reading (b) by its structure (psianalysis.m and the Figure 4A legend), not by calibration. The surrogate (cell 44) shows (b) is too conservative in delta-theta: SD 0.60 and a 0.1% pass rate. In alpha-beta its per-subject rates run from 0% (S7) to 24% (S1), where (a) is about 5–7%.
- If reading (a) were adopted, fig4c would be not reproduced, fig5b partial, and fig5a-spatiotemporal reproduced by the letter but uninformative.

### 2. Sentences the outputs do not support

- **Cell 30 and the record's erp notes:** "The deciding p values lie between 0.02 and 0.05, so the outcome is close to the threshold under every reading." The distance reading gives p = 0.014 (cell 29), about 6 Monte Carlo SE below 0.05. Only the adopted adjacent reading (0.041) is close to the threshold.
- **README** ("about 35 minutes, about 20 of them streaming") **and cell 0** ("about 20 of the run's 35 minutes"): cell 2 prints 46.7 min for the loading cell alone.
- **README:** "The deposited code omits the conjugate … and z-scores against a null that is not the statistic it tests, which marks about 90% of pairs as directional even when the trials … are shuffled." The 90% and 92% (cell 44) come from psianalysis.m's null with the conjugate added. The code as deposited was never run on the surrogate; on the real data it marks 99.5–100% of pairs (cell 51). The record's code_mismatch finding states this correctly.
- **Cell 5:** "the docs' channel list names 192 analysed channels in all (Table 1)". Cell 17 counts 187.
- **Record, fig2 notes** (minor): "Five subjects show spatial > identity effects under every reading" and "S4 alone identity > spatial under every reading but …". This holds for the main spectra only. The 900-ms variant gives 2 or 3 subjects, and the whole-epoch windows add S7 (cell 32). The note itself reports both of these later on.
- **Record, fig4c notes and cell 50:** the numbers are right. The reading that "6 of 7 below 0" is the criterion's partial match conflicts with the offset described in section 1.

All other Result, Summary, README and notes sentences agree with the printed outputs.

**Verification block.** The 17 reasons are my round-1 reasons, nearly verbatim. Three of them (erp, fig2-spatial-power, power-low-frequencies) add which of my problems bear on the claim (problems 4 and 5, 6, and 9). Those additions describe my report accurately. The counts are also right: 10 problems, 5 marked as affecting a conclusion.

### 3. Round-1 points

**Resolved:**
- 2: the deposited code's variants are labelled as not a reading and decide no outcome.
- 3: one null per pair.
- 4: the scripts are printed, and they contain no cluster test.
- 5: per-trial baseline and band-pass variants are run, and the segments are padded before filtering.
- 6: the zero-padded segment is the main reading.
- 8: the question goes to a reader.
- 9: recorded as an assumption, with the result without the edge printed.

**Partly resolved, and bearing on a conclusion:**
- **1, PSI null.**
  - Reading (a) is now calibrated: 6.0% and 6.9% on the surrogate.
  - Reading (b) now computes the same statistic for the null as for the observed value. It is still miscalibrated: too conservative in delta-theta and offset toward negative z in both bands (synthetic test above).
  - This bears on fig4c, and on fig5a-spatiotemporal and fig5b through the choice of reading.
  - Needed: the surrogate's mean z per subject under (a) and (b), and possibly (b) with one permutation per trial (P1 null reading (b)), which was not run.
- **10, pairs treated as independent.** Subject-level tests are now printed for the task-induced PSI, but not for the time-resolved PSI. This bears on whether fig5b's "significant at some time points" holds.
- **7, timing of the 1150-ms trials.**
  - The 900-ms-only variant removes most power effects: spatial 2–3 and 0 subjects, temporal 1–3 and 0–1 (cell 32).
  - That loss cannot yet be separated from the halving of trials. A control on a random half of all trials would separate the two.
  - The cue-locked traces were not added, and PSI was not run on the 900-ms trials.
  - This bears on how far fig2, fig3 and power-difficulty-subjects can be read, not on their outcomes by the letter.
