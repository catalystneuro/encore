I've finished steps 1 to 6 of the Author section for CRCNS alm-3 against Li et al. (2016). The entry passes `tools/entry.py all` (0 check errors; the notebook runs in about 4 minutes) and the handover package is built. Nothing is committed.

## 1. Outcomes (29 claims)

| Claim | Outcome |
|---|---|
| units-and-sessions | not reproduced: 1012 units, 20 + 38 sessions, 12 mice and 890 pyramidal all match exactly, but 89 FS against the paper's 72 |
| ed1-selective-fraction | reproduced (633 / 176 / 336 / 493 against 634 / 176 / 337 / 493, correct trials only) |
| fig1d-late-delay-ipsilateral-bias | blocked: data_missing |
| fig1d-earlier-photoinhibition-minimal | reproduced (p = 0.23 and 0.22; only 4 mice, recording sessions) |
| ed3-recovery-interval | blocked: data_missing |
| ed2b-silencing | reproduced |
| ed2d-spatial-extent | blocked: data_missing |
| ed2e-no-rebound | partially reproduced: no rebound on average, but more neurons excited (24) than suppressed (9) |
| fig1f-rate-recovery | partially reproduced (exactly 168 / 168 / 175 neurons; fractions 9 to 20%) |
| fig1g-selectivity-recovery | reproduced (347, 420, 236 ms) |
| ed4-return-to-trajectory | not reproduced |
| ed5-photoactivation | blocked: data_missing |
| fig2b-bilateral-behaviour | partially reproduced |
| ed6-bilateral-bias-inconsistent | reproduced (under the criterion's second reading only) |
| fig2-bilateral-recovery | partially reproduced: ipsilateral selectivity reaches 80% before the cue in only 25% of bootstrap resamples |
| ed7-unilateral-4-spots-bilateral-1-spot | partially reproduced: bilateral 1-spot selectivity recovers in 80% of resamples, where the paper says it does not |
| ed7e-size-and-roc | partially reproduced |
| fig3-cd-roc | reproduced (exactly 16 sessions; only under the leave-one-out reading) |
| ed8-roc-during-photoinhibition | reproduced (3 of 24 readings match) |
| ed9b-cd-stability | reproduced |
| ed8a-mode-variance | partially reproduced |
| fig3-cd-predicts-movement | reproduced |
| fig3-other-modes | not reproduced |
| ed9f-reaction-time | blocked: data_missing (no licks in the Experiment 2 lick traces) |
| fig5b-callosotomy-behaviour | partially reproduced (only after-cut sessions exist) |
| fig5-callosotomy-recovery | reproduced |
| ed10e-callosotomy-preparatory-activity | partially reproduced |
| models-monolithic-fail | partially reproduced (3 of 5 models simulated; marked assumed) |
| fig6-modular-models-robust | partially reproduced (attractor works; the printed integrator matrix recovers lick-right trials only; marked assumed) |

Totals: 10 reproduced, 11 partially reproduced, 3 not reproduced, 5 blocked.

## 2. Dataset, assumptions and questions

**What the dataset holds.** 91 sessions from 19 mice, and the trial tables and laser timing match the description. The authors' MATLAB scripts in the dataset reproduce several of the paper's counts exactly.

**Findings recorded:**
- **FS labels:** 89 units are labelled FS against the paper's 72, and the labels don't follow the waveform widths.
- **Missing `depth` field:** the description lists one; the files have none.
- **Type 9 mislabelled:** still described as "ipsilateral"; the FAQ says contralateral.
- **Lick trace:** shows no licks in 48 of 90 sessions, including all 26 Experiment 2 sessions.
- **No silencing in four sessions:** photoinhibition doesn't reduce activity there, so the spike/laser/trial clock can't be confirmed for them.
- **Session with no performing trials:** ANM270340_20150618.
- **Experiment not labelled:** nothing says which experiment a session belongs to, and six sessions hold a condition mix the Methods don't describe.
- **Not deposited:** the behaviour-only sessions, photoactivation data, untrained-mouse recordings, pre-callosotomy sessions and the simulations named in the title.
- **Scripts against Methods:** the deposited scripts disagree with the Methods. cd is a Fisher discriminant there, not the mean difference. The selectivity test uses correct plus error trials, yet the paper's counts match correct trials only.

**Version.** CRCNS has no versions, so I pinned the `live/` copy as `unversioned`. The notebook header says why and prints the MD5 sums of the files read.

**Assumptions** (outcomes marked `assumed: true`):
- fig6: noise variance taken per integration step, and the inter-module partner taken to share its neuron's preference.
- models-monolithic-fail: the simple integrator is a random rank-one matrix, and the FORCE network uses standard choices for target, feedback and update rate.

**Questions for the paper's authors** (one `methods_unavailable` finding):
1. Is the Fig. 6b noise variance per step?
2. Is the Fig. 6c matrix complete? As printed, lick-left trials don't recover.
3. ED Fig. 4 has 6 mice, but Experiment 1 has 4. Which sessions were used?
4. How were bootstrap resamples that never recover counted in Fig. 2e?

**Questions to a reader:** none.

## 3. Protocol gaps

1. **Code in the dataset, not linked by the paper.** The protocol only covers "code it links". I treated the deposited scripts as the paper's code, Methods first, and recorded each use.
2. **Readers can't see dataset files,** so the claims file was written without those scripts. Reader and author then work from different method sources (cd definition, trial sets).
3. **Every reading must be run, and any match counts.** Readings multiply into large grids, and one reading moved fig3-cd-roc from partial to reproduced. I ran the grids and reported how many readings match. The leave-one-out split for fig3-other-modes was not run because of its cost; I said so.
4. **Criteria without a partial rule** (ed2e, ed7, ed7e, ed10e, models). I used the protocol's general definition of partially reproduced.
5. **Claims that use no recorded data** (the simulations). It is unclear whether they should be tested. I tested them.
6. **`measured` when no reading matches** is not specified. I recorded the main reading (the script's, or the first listed).
7. **Peak memory:** `ru_maxrss` doesn't count worker processes. I printed the main process and stated the per-worker bound.
8. **"Use a pinned published version"** doesn't apply to CRCNS. I followed docs/archives.md.

## 4. Runtime and failures

- Work ran from about 19:24 to 20:35 UTC (about 1 h 10 min). The final notebook run took 226 s, with peak memory 0.59 GB in the main process.
- Two early notebook runs failed on cell ordering and were fixed; nothing is outstanding.
- Untracked dotfiles (`.bashrc`, `.gitconfig`, `.idea` and others) are at the repository root. I did not create them and left them alone; the workflow may pick them up when it commits.

Files are in `entries/crcns-alm-3-li-2016` and `attempts`:
- `reproduce_li_2016.ipynb`
- `alm3.py`
- `models.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`
- `crcns-alm-3-li-2016-01.yaml`
