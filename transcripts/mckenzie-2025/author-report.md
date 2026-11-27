The attempt is recorded and handed over. `entry.py lock`, `check` and `all` all pass, and the verifier's package is in `executed/mckenzie-2025/handover/`. I did not verify my own work and committed nothing.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| 13 photometry claims (Figs 1–6, S1–S5) and ne-and-settling-time-course | blocked, `data_missing` |
| ephys-ensemble-size | reproduced: all units give a mean of 259.4 (range 191–363); pyramidal cells only give 215.8, outside tolerance |
| figs6b-decorrelation-novel | not reproduced (no reading has p < 0.05) |
| figs6d-decorrelation-familiar | reproduced (p = 0.459) |
| fig7ab-umap-embedding | partially reproduced, assumed: position maps in 7 of 8 sessions, early moments are peripheral in 1 of 8 |
| fig7e-novel-settling | reproduced, assumed (p = 0.0066) |
| fig7f-familiar-settling | reproduced, assumed (p = 0.0007) |
| fig7g-familiar-more-similar-early | reproduced, assumed (p = 0.042) |
| figs7ab-in-field-out-field | partially reproduced, assumed: out-of-field firing does not fall in novel runs |
| figs7cd-movement-not-time-locked | not reproduced, assumed: in novel runs the movement differences fall with time (p ≈ 0.001) |
| figs7ef-time-explains-similarity | not reproduced: dropping \|Δvel\|NN also worsens the fit, in both environments |
| figs7gh-unconditioned-similarity | reproduced under reading (a) |
| fig8b-late-moments-reactivated | not reproduced (late minus early is −0.024 percentage points, p = 0.20) |
| fig8d-familiar-no-difference | not reproduced, assumed: early > late, p = 0.0074 under all five seeds |
| fig8-no-pre-reactivation | not reproduced: pre ripples run 0.13–0.15%, above the 0.1% false positive rate |

**2. What was found about the dataset (pinned 0.230630.2304, the version the paper cites)**
- **Critical:** in session e16-3m2-211211, the linear-track tracking and its 45 trials are filed inside the open-field epoch. Spikes show no spatial tuning to them at any time shift. Moved 5564.5 s later, onto the linear-track epoch, the tuning appears. The newest version, 0.261113.1035, has the same error.
- **Major, fixed in 0.261113.1035:**
  - There are no cell-type labels and no epoch names, and session e13-26m1-211116 has no epochs at all.
  - There is no open-field tracking.
- **Minor:**
  - In five novel runs the x, y position runs 0 to 1 but is labelled cm.
  - Tracking starts 15 to 63 s after each maze epoch begins, so the transfer time is uncertain by that much.
  - In three files the behavior module's description spells "alternation" as separate letters.
- Pyramidal cells come from the 0.261113.1035 labels. I checked that its spike times are identical, and listed it under `inputs`.
- Sessions: 9 have a familiar run and a tracked novel run, and 8 of those are long enough to test. All units of the 9 give exactly the paper's 253.8 (range 191–363). I recorded this as a `paper_inconsistency`, since the Methods say only pyramidal cells were analysed.
- **Assumptions:**
  - Location is binned on the linearized position in cm, because the 2D position is not in cm in five novel runs. The Methods' 1 × 1 cm (x, y) bins could be run on all familiar runs and agree there, but on only 4 novel runs.
  - For fig8d, the shuffle pool is the ripple's own set (pre or post).
  - For figs7cd, absence is judged under the first reading of each open detail.
- Seven questions for the paper's authors are in a `methods_unavailable` finding.
- I asked a reader no questions.

**3. Where the protocol was unclear or missing something**
1. It does not say what to do when the cited version lacks labels that a later version adds. I pinned the cited version and took only the labels from the later one, listed under `inputs`. `entry.yaml` can name only one version per dataset.
2. It does not say how to handle a recording known to be misfiled. I kept it as filed in the main reading (matching the paper's 8 sessions) and showed the 7 clean sessions as a variant.
3. The reactivation claims list 2 × 2 × 2 readings, and crossing them all would push that notebook past the time limit. I varied one reading at a time around a main reading and recorded this as a deviation.
4. "Absence is judged on the paper's test alone" does not fit when the criterion leaves a reading open (the pool for fig8d, several readings for figs7cd). I used the first-listed reading and marked the outcome assumed.

**4. Runtime and failures**
- `settling.ipynb` takes 11 minutes and `reactivation.ipynb` 35 minutes; peak memory is 4.1 GB.
- `reactivation.ipynb` is over the protocol's 10-minute aim but under the 60-minute limit.
- Ripples are the ones deposited in the files, not re-detected: the broadband LFP is only in the 120–180 GB raw files.
- Nothing failed, and the full run's numbers match the development run.
