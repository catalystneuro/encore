I've finished attempt `000006-economo-2018-02`: the conclusions are written from the executed numbers, the record and questions file are written, and the handover is built. I have not verified, committed or pushed anything.

**Version.** 0.220126.1855 is still the only published version, so it stays pinned (the notebook header says why). The helper constant and `entry.yaml`'s `dandi:` relation are unchanged. The run passes in about 11 minutes; two clean runs gave identical outputs.

**Why so many claims are blocked.** Neither of the claims file's unit selections gives the paper's 61 and 69 units on the dandiset: the code's rule keeps 44 and 56, the session rule 42 and 63. The file says to use the selection that matches, so I ran every claim under both, plus the other readings it names. Where readings disagree, the claim is blocked and asked about in `questions/000006.yaml` (15 questions). Run on the paper's own 130 units from the Figshare processed data, the same code gives the paper's numbers for unit counts, bursting, late-delay counts, decoding, early selectivity and spike rates. So the shortfall comes from the dandiset's missing sessions, not from the code. The exception is the CDgo onsets, which come out later than the paper's even on its own data.

### 1. Outcomes (earlier outcome in brackets; "new" means the claim did not exist before)

**Data elsewhere (tested on the paper's Figshare record):**

| Claim | Outcome | Earlier |
|---|---|---|
| pt-types-transcriptomic | reproduced (27 clusters under one counting reading) | blocked, data missing |
| pt-types-shared-targets | reproduced | blocked, data missing |
| pt-projection-cluster-mapping | reproduced (62 of 62; 91 of 94) | new |
| pt-bulk-sc-fold-change-correlation | reproduced (r = 0.867 / 0.874) | new |
| pt-types-account-for-all-pt | partially reproduced (17 of 18 reach the superior colliculus) | new |
| pt-upper-thalamus-projection | blocked, methods underspecified | blocked, data missing |
| pt-lower-medulla-projection | blocked, methods underspecified | blocked, data missing |
| pt-retrograde-sublaminae | blocked, methods underspecified | new |
| pt-marker-genes | blocked, other (smFISH data not public) | new |

**Data in the dandiset:**

| Claim | Outcome | Earlier |
|---|---|---|
| pt-tagged-units | not reproduced | new |
| pt-selective-any-epoch | not reproduced | new |
| pt-depth | reproduced | new |
| pt-lower-cdearly-decay | reproduced (p = 0.30 to 0.40; paper 0.34) | new |
| pt-cd-stability | reproduced | new |
| pt-lower-late-and-motor | reproduced | partially reproduced |
| pt-preparatory-activity | partially reproduced | reproduced |
| pt-lower-bursting | partially reproduced | new |
| pt-upper-decoding | partially reproduced | new |
| pt-upper-decoding-rectified | partially reproduced | new |
| pt-cdgo-onset | partially reproduced (37.5 and 77.5 ms against 24 and 48) | new |
| pt-upper-early-preparatory | blocked, methods underspecified | reproduced |
| pt-upper-persistent | blocked through its dependency; its own test fails under every reading | reproduced |
| pt-types-differ-in-timing | blocked through its dependencies | not reproduced |
| pt-spike-rates-similar | blocked, methods underspecified | new |
| pt-lower-heterogeneous-rates | blocked through its dependency (its own test holds under every reading) | new |
| pt-variance-explained | blocked, methods underspecified | new |
| pt-single-neuron-early-selectivity | blocked, methods underspecified | new |
| pt-cd-change-at-go-cue | blocked, methods underspecified | new |
| pt-lower-movement-termination | blocked, methods underspecified | new |
| pt-cohort-control | blocked, methods underspecified | new |
| reaction-time | blocked, data missing (no video) | new |

Every changed outcome comes from the rewritten criteria, not from the data; each is explained in the record's notes.

### 2. Earlier findings
All seven are still present, since the version has not changed; the notebook prints the evidence for each:
- 11 sessions are missing (17 PTupper and 13 PTlower units).
- No sequencing or anatomy is in the dandiset.
- Spike times are unsorted and trials overlap on the file's clock.
- `stop_time` is NaN and the trial times are relative to the trial start without saying so.
- The PT labels are not described.
- The quality, sex, genotype, electrode position and layer metadata are uninformative.
- The first ten trials are shifted in the processed data.

### 3. New findings
- The missing sessions also hold 285 PTupper-cohort and 117 PTlower-cohort unidentified units.
- Lick times are stored trial by trial and out of order in 105 of 106 series. Rebuilt from the stored order, each trial's last lick matches the processed data in 98.1% of correct trials.
- The files hold no session manipulator depth and no video.

### 4. What did not fit a repeat attempt
- **`entry.py check` fails on the earlier record.** It checks the deprecated `-01` record against the rewritten claims file and reports 22 claims with no outcome. I can't fix this without editing `-01`, so `entry.py all` stops at the check. I ran `entry.py run` instead; the new `-02` record passes.
- **The dependency rule over-blocks.** `pt-lower-heterogeneous-rates` uses only the rates from `pt-spike-rates-similar`, yet it is blocked because that claim is blocked.
- **The "elsewhere" rule forbids `data_missing`.** For `pt-marker-genes`, whose data are public nowhere, I used `other` and asked whether the claim's data field is wrong.
- **The repeat-attempt section assumes the dandiset changed.** Here the claims file changed and the data did not, so "fixed or still present" is trivially "still present" for every earlier finding.
- **No selection is designated when neither reading matches.** The claims file names no reading for that case, and that gap causes most of the blocks.

Files are in `entries/000006-economo-2018/`:
- reproduce_economo_2018.ipynb
- alm.py
- README.md
- entry.yaml

Also new:
- attempts/000006-economo-2018-02.yaml
- questions/000006.yaml
