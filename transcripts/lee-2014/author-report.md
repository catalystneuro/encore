I've written the entry and the attempt record, run them, and built the hand-over. `entry.py all` reports 0 errors and the notebook runs in about 15 s. The verifier's package is in `executed/crcns-hc-10-lee-2014/handover/`. Nothing is committed. Of the 34 claims, 4 are reproduced, 1 is partially reproduced and 29 are blocked.

## 1. Outcomes

| Claim | Outcome | Key numbers |
|---|---|---|
| figs1e-if-curves | reproduced | two-way ANOVA group p = 0.411 (reading a), 0.866 (b); at +550 pA sPC 31.62, dPC 30.56 Hz |
| figs1f-input-resistance | reproduced | sPC 118.7, dPC 124.9 MOhm; Mann-Whitney p = 1.0 |
| figs1g-resting-potential | blocked, data_missing | every PC sits within 2.6 mV of the -70 mV holding level and no file records a current, so the criterion says it cannot be tested |
| figs1h-sag | reproduced | at -400 pA, sPC 8.71, dPC 5.69 mV; p = 0.0020 |
| tables1-rheobase | partially reproduced | median gives sPC 200, dPC 150 pA; rounded mean gives 200 pA for both, not 150 |
| figs3f-pvbc-firing | reproduced | cell PV34 is silent up to +300 pA, then fires 2, 17, 36 and 52 Hz, exactly the expected values |
| 26 claims (paired recordings, anatomy, imaging, optogenetics, labelling) | blocked, data_missing | |
| fig4d, fig4ef (network model) | blocked, too_large | about 670 core-hours estimated |

## 2. Dataset, assumptions and questions

**Version:** CRCNS does not version data sets, so I pinned `crcns:hc-10/unversioned`. There is only one published copy, under `live/`. The notebook checks the zip's MD5 (99bc6c87…) against the data set's `checksums.md5` while streaming it.

**What the data set holds:** the current-step sweeps of 8 superficial and 9 deep pyramidal cells and 6 PV basket cells, voltage only.

**What I found:**
- PV34 is deposited twice under two names with identical bytes, so it is counted once.
- No file records the injected or holding current, so the step levels come from the descriptor's table alone. The voltage responses are consistent with that order in every PC.
- No file gives the animal, slice, region or soma position of a cell.
- In PV37 the first three sweeps are out of order.
- The data set holds only the material for Figures S1E–H, S3F and Table S1.

**Assumptions:** none that an outcome rests on (`assumed` is false everywhere). Each reading the claims file lists was run. I made three standard choices and recorded each as a deviation:
- the two-way ANOVA is run with the interaction term, and also without it and as a mixed ANOVA; all agree;
- a sweep with fewer than two spikes gets 0 Hz under the second firing-rate reading;
- the baseline is the 0.2 s before the step.

**Questions for the paper's authors:** none. **Questions to a reader:** none.

## 3. Protocol points

1. **Checking the clock with a trial table** (step 2) does not fit single-cell sweeps that have no trial table and no current channel. I checked instead that the voltage deflection rises with sweep order and is near 0 on the 0 pA sweep, and reported the step labels as consistent with the data, not shown.
2. **Where a too_large estimate may come from:** the protocol says numbers from analyses run outside the notebook must not supply a number in the record. It does not say whether a timing estimate behind a `too_large` block counts. I timed a 20 ms model run while preparing the entry: 808 s on one core. I put the estimate in the notes, labelled as not run in the notebook.
3. **Outside code used only for timing:** it is unclear whether code used only to estimate cost belongs under `inputs`. I listed the model repository at its commit and said it decides no outcome.
4. **Fetching the model:** the claims file cites the ModelDB download, which now returns 404/504. I used the GitHub mirror, ModelDBRepository/153280 at commit 5314d07.

## 4. Runtime and failures

- The run took about 40 minutes, from 03:35 to 04:16 UTC. The notebook itself takes about 15 s.
- The first model timing run failed with a hoc error: setting `PrintVoltage=0` leaves `objref f` undeclared. The rerun with the default setting worked.
- A few notebook bugs (header parsing, a pingouin column name) were fixed during development.
- Untracked files such as `.bashrc` and `scripts` at the repository root are sandbox device mounts, not created by me.
