I've finished steps 1 to 6 for `entries/johnson-2017` on CRCNS pfc-5. All 22 claims were tested and none is blocked: 10 reproduced, 4 partially reproduced, 8 not reproduced. `entry.py all` passes (0 errors, notebook ran in 27 min) and the handover is built in `executed/johnson-2017/handover/`. Nothing is committed.

**1. Outcomes** ("assumed" means the outcome rests on a choice the paper leaves open)

| claim | outcome | assumed |
|---|---|---|
| cohort-and-trials | reproduced: 187.3 trials; lesioned hemifield 94.4 ± 21.1 [55–119]; intact 93.0 ± 22.1 [51–120] | |
| demographics-matched | reproduced | |
| patient-factors-no-effect | reproduced (smallest p = 0.106) | |
| table-s1-patient-accuracy | partially reproduced: 20 of 28 values within 0.02 | |
| accuracy-patients-impaired | partially reproduced: linear model p = 7.6e-4; F not 16.77 under any reading | yes |
| patients-above-chance | reproduced: t = 14.13 | |
| accuracy-no-hemifield-condition-effect | reproduced (linear model) | yes |
| erp-lesioned-maintenance | reproduced: p = 0.006 anterior, p = 0.014 over P6/P8/P10/PO8 | yes |
| erp-processing-interaction | not reproduced (p = 0.294) | |
| erp-intact-none | reproduced | |
| baseline-spectral-interaction | reproduced: p = 0.004 over AF3/F3/F5 | |
| baseline-no-group-effect | partially reproduced: no cluster, but 476 points with uncorrected p < 0.05 | |
| power-anterior-theta-controls | reproduced: maximum Z 3.74 in processing | yes |
| power-posterior-alphabeta | not reproduced | |
| power-lowtheta-interaction | partially reproduced: lesioned hemifield p = 0.040; intact p = 0.134 | yes |
| power-no-group-main-effect | reproduced | |
| psi-deltatheta-bottomup-encoding | not reproduced | |
| psi-deltatheta-pfc-lead-controls | not reproduced | |
| psi-deltatheta-group-clusters | not reproduced | |
| psi-network-degree | not reproduced | |
| psi-alphabeta-bottomup | not reproduced (the paper's code as written does reproduce it) | yes |
| psi-alphabeta-no-group-effect | not reproduced | yes |

**2. Dataset**

Version: CRCNS data sets are not versioned, so the files under `pfc-5/live/` are pinned by the MD5 sums the notebook prints.

What I found (recorded as findings):
- **Processing segment out of order:** in all 34 subjects it is stored in a different trial order from the other segments. `erp_compute.m` and `tfr_compute.m` select its trials with the encoding segment's indices, so they average the wrong trials.
- **Hemifield code:** the derived column the descriptor calls "1 intact / 2 lesioned" equals the trial table's left/right column in every trial of every subject. The docs summary, which equals Table S1, contradicts the paper's own note on which hemifield is lesioned. Which 10 controls were swapped across the midline is not recorded.
- **No buffers on the segments:** they are 500, 1500 and 900 ms long. FieldTrip's 3/f windows therefore leave no baseline power below 7 Hz and no delta-theta PSI at all.
- **PSI code:** `psianalysis.m` leaves out the complex conjugate. The result depends only on channel B's phase (up to sign), so it is not Nolte's PSI.
- **Other file problems:**
  - Channel order differs in 13 subjects.
  - Six two-block subjects have trial tables whose trial numbers overlap; I linked trials by trial number plus response time.
  - The pretrial `fsample` field reads 255.64 Hz.
  - The descriptor says 6 male patients; the summary file has 5.
- **Clock check:** I could not establish that the segments share the trial table's clock from the ERP.

Assumptions:
- Hemifield coding: the descriptor's.
- Window edges: windows may run into the zero padding (the only reading under which the 3–4 Hz results exist).
- Low-theta test: run on the 3–4 Hz mean.
- Accuracy model: linear, as the Methods say.
- PSI: the code's structure with the conjugate restored.
- Clustering: the code's per-seed PSI test.

I replaced the bootstrap Z with its exact expectation. Every alternative reading is run and shown in the notebook.

Questions for the paper's authors (in the record's findings):
- Were the analyses run on segments with buffers? This is the only one filed as a `methods_unavailable` question.
- Which hemifield code is right?
- Was the missing conjugate in `psianalysis.m` intended?
- Which controls were swapped?

The last three are written as statements in the findings, not as explicit questions. I asked a reader nothing.

**3. Where the protocol was unclear or wrong**
1. `entry.py lock` writes `python: "3.13"` into `entry.yaml`, and the entry schema then rejects it. I deleted the line; the tool falls back to the lock file's version.
2. `archives.md` covers zips only. pfc-5 is tar.gz, which has to be read in order, and fsspec range reads were 4× slower. I streamed each file with urllib, keeping nothing on disk.
3. The protocol has no rule for code that is wrong, as opposed to code that disagrees with the Methods. I applied "Methods first" and ran the literal code as a variant.
4. Absence claims are to be judged "on the paper's test", but that test's clustering was itself open. I followed the deposited code, which the claims file allows.
5. When an expected value fails (F = 16.77) but the criterion's condition passes, the protocol doesn't say which wins. I chose partially reproduced.
6. The suggested clock check assumes trial-level decoding is available. Here it gave nothing conclusive, and I recorded it as not established.
7. "Trust the data" can't settle a conflict between two of the data set's own documents. I adopted the descriptor's coding as an assumption.
8. The "under 10 minutes" target can't be met: each run has to stream about 20 GB (19 min), and caching between runs isn't allowed.

**4. Runtime and failures**

The clean run took 27.3 min end to end (notebook 27.0 min, peak memory 3.4 GB). The first full development pass failed after 18 min on two-block subjects; fixed. The full binomial accuracy model did not converge; the record says so. The untracked `scripts` entry at the repo root is a device file that predates this run and isn't mine.
