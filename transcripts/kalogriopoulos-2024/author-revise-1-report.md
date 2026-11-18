I've revised round 1 and re-run the entry. It passed in 784 s, the attempt record matches the schema, and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes:** none changed. The verifier agreed with all 32 (every claim blocked), and the new outputs give no reason to change one. The new `verifications` entry records the verifier's reasons in its own words and my response for each claim.

**Fixes, by point in the report:**
1. **Text scan (the one that affected conclusions).** `pager_slice.file_text` now reads every object in every file: the attributes of every sweep's series, every string dataset of any length (including the icephys table columns), and `/intervals`, `/analysis` and `/processing` where they exist. The notebook now lists every path in one file; all 50 files have the same paths. It also prints the distinct description, stimulus description and comment values over all sweeps. No file has an `/intervals` group, and nothing names a drug, condition, onset or expression level, so the blocks for the slice claims stand. I corrected the notebook text and the record notes that had wrongly said the intervals were "empty".
2. **Totals.** The `methods-slice-sample` result now prints the totals (49 and 50) against the paper's 41. It says these rule out "reproduced" under both readings, and that no stated exclusion explains the 8 or 9 extra cells. The notes say the same.
3. **A2 against A1 detection.** A new data-check cell prints what the verifier asked for, plus the peak voltage after each first event:
   - Among sweeps with resting potential at or below -50 mV, the two rules give rheobase within 1 pA in 10,335 of 10,675 sweeps.
   - A2 fires more than 10 pA earlier in 335 sweeps, 325 of them in two cells. There it catches fast spikes that peak near -15 mV and never reach 0 mV, which A1 misses. So the difference is mostly small spikes, not noise.
   - In the first 100 ms of the ramp, A2 takes two deflections peaking at -49.3 and -55.8 mV for action potentials. That part of the verifier's concern holds.
4. **Ages.** The verifier is right that the 49–98 day range was too strict. The notebook now also shows the 49–110 day reading, and I withdrew the finding that PK-109 and PK-110 (101 and 107 days old) contradict the Methods.
5. **20 kHz sampling.** I added an interpolation test: each half of the samples is fitted on the other half. Every file leaves residuals of 0.87 to 1.58 ADC counts both ways, against about 0.3 expected if the data were interpolated from 10 kHz. The finding now says the samples are neither repeated nor interpolated 10 kHz samples.
6. **Holding current.** The notebook prints the per-cell baseline of the current channel, which varies by at most 0.037 pA within a cell. The `fig4j-rheobase-increase` notes now say the criterion's holding-current item is not met. I also added to an existing finding that the holding current is not recorded.

**Also updated:** the README runtime (13 min), `runtime_minutes` in `entry.yaml` (14), and the notebook summary.

**Not done:** I added no question to `questions/kalogriopoulos-2024.yaml`, because the verifier found no misreading of the paper in the claims file.
