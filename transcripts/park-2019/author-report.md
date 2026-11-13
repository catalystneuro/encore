I've finished the author steps (1 to 5) and built the handover package. The entry passes `python tools/entry.py all entries/park-2019` (0 errors), and the notebook runs from a clean environment in 103 to 125 s with a peak of 1.0 GB. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cell-counts | partially reproduced (115 head-direction cells, 13 rats; the 353 MEC cells and 556 pairs aren't in the dataset) |
| hd-cell-rate | reproduced (1.392 AP/s) |
| fig1a-avoidance-learning | blocked: data_missing (no training sessions) |
| fig1c-speed | reproduced, assumed |
| fig1c-lfp-power | blocked: data_missing (no LFP) |
| fig1c-firing-rate | reproduced (p = 0.184) |
| fig1c-directionality | reproduced, assumed (repeated-measures Tukey) |
| fig1d-preference-change | partially reproduced (order of trial pairs reversed for the arena frame) |
| fig1d-instability | partially reproduced (2 of 3 Dunnett tests significant) |
| fig2-decoding-stable-vs-rotating | reproduced, assumed (7 ensembles; 4 of 7 and 5 of 7) |
| figs2-frame-preference | reproduced, assumed (4 and 2 under only 1 of the 16 readings) |
| fig2c-proximity-anticorrelation | partially reproduced (mean r between -0.05 and -0.09) |
| figs3-no-head-direction-bias | reproduced, assumed (r = 0.166) |
| fig3-hd-pair-correlations-preserved | reproduced |
| figs4, figs5, figs6 | blocked: data_missing (non-head-direction cells aren't deposited) |
| no-angular-velocity-tuning | not reproduced, assumed (10.4% of cells significant, binomial p = 0.013) |
| fig4-internal-tuning-preserved | not reproduced (instability differs, p = 8e-5; the clean variant passes all four tests) |
| fig4c-arena-registration-short-lived | partially reproduced (both rotating frames fall after 10 s, not the arena frame alone) |
| fig5-error-inhomogeneous | partially reproduced (tests hold; resultant lengths far from the paper's) |
| fig5c-error-minima-at-cues | reproduced (105 and 345 degrees, shallow, one reading only) |

## 2. Dataset, assumptions and questions

**Dataset.** CRCNS hc-20 is not versioned, so I pinned `unversioned`. `data.zip` has MD5 b82c7b97…, and the notebook checks the bucket's ETag against it. It is the only published version and the one the paper cites by DOI.

It holds only the 115 head-direction cells (13 rats, 44 sessions) and the tracker files. Problems in the files:
- **File list:** FileNameList.xlsx puts the stable2 files of five units in session 1121R157 one row off.
- **Copied spikes:** the rotating-trial spike file of unit 1024R157 P9C1 holds exactly its stable1 spike times.
- **Copied track:** the rotating room-frame track of 1211R039 is the track of 1212R039.
- **Misaligned frames:** in four R029 sessions (1009, 1015, 1023, 1025) the room and arena tracks of the rotating trial drift apart through the trial and don't match the tracker files.
- **Bad header:** one stable2 file states 2000 samples/s.
- **Short file:** one stable2 file holds half a trial.
- **Clock drift:** spike timestamps run about 0.05% fast against the header's sampling rate.
- **Counts:** per-rat counts differ from Table S1 for R029 (40 against 41) and R523 (2 against 1). There are 146 simultaneously recorded pairs against the paper's 142.

**How I handled the bad files.** The main analyses use the files as deposited, because the paper's n of 115 implies every unit was used. A "clean" variant leaves the bad files out. This choice changes fig4 (it passes when they're excluded) and weakens the room-frame result in fig1c-directionality.

**Assumptions:**
- The Tukey test after a repeated-measures ANOVA uses that ANOVA's error term.
- Speed drops steps faster than 100 cm/s.
- Distance to a shock zone is measured to the centre point of its sector.
- The Rayleigh test in figs3 uses n = sum of the weights.
- The Idir readings are the ones the claims file names.

**Questions for the paper's authors** are recorded as two `methods_unavailable` findings:
- How Idir is defined: bins, which trial's probabilities, which SD the 2 SD rule uses, the no-preference margin, how proximity is computed, and the n of the Figure S3 test.
- The post hoc Tukey test, how speed is computed, how pairs are ordered and dropped for internal tuning, and what "divided by the sum of the time offsets" means.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. It doesn't say whether the main analysis should use files the data check shows to be wrong. I used the files as deposited and showed a clean variant.
2. For claims of absence it says multiple readings don't apply, but the figs3 criterion lists readings for n. I ran both and adopted one as an assumption.
3. "Reproduced under any reading" lets figs2 pass on 1 of 16 readings. I marked it assumed and gave the count of readings in the notes.
4. `entry.py check` requires the version string ("unversioned") to appear in code, which archives.md doesn't mention. I added a `VERSION` constant to the helper.
5. The `measured` field can't hold values for counts the dataset lacks, so I left it out for cell-counts.
6. The clock check is described for trial tables. I used directionality against directions shifted by 60 s (109 of 115 units higher with the true alignment) plus a spike-in-sample timestamp check.

## 4. Runtime and failures

The whole run took about 40 minutes (16:25 to about 17:05 UTC). My first check failed on the missing version string; after the fix, every check and run passed. Nothing else failed.
