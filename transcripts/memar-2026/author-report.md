The iEEG part of the attempt is done: 11 claims tested, 7 reproduced, 1 partially reproduced and 3 not reproduced. The 9 EEG claims are blocked. The record is `attempts/memar-2026-01.yaml`, the handover is built, and `entry.py check` reports 0 errors. The entry was not run end to end by `entry.py all`: the tool cut that run at 60 minutes, and I ran the last two notebooks myself (point 1 below).

**1. Outcomes**

| Claim | Outcome | Measured |
|---|---|---|
| intra-ieeg-mean | reproduced (assumed) | 0.602 ± 0.058 for preprocessing before cutting trials, 0.570 for preprocessing each trial; 0.598 to 0.602 over five seeds |
| table2-ieeg-intra-subjects | partially reproduced (assumed) | 8 of 12 subjects within tolerance with per-trial preprocessing, 4 of 12 with preprocessing first |
| cross-ieeg-mean | reproduced | 0.351 (0.339 to 0.351 across the four readings) |
| table2-ieeg-cross-subjects | not reproduced | 0 of 12 within tolerance; rank correlation with the table 0.16 to 0.28 |
| cross-below-intra-ieeg | reproduced | 0.351 against 0.602; 11 or 12 of 12 subjects |
| fig4a-mask-sweep-ieeg | reproduced | 0.712 → 0.674 → 0.650 → 0.628 → 0.602, falling in all 12 subjects |
| full-mask-above-zero-ieeg | reproduced (assumed) | 0.602 against 0.201 for the phase-shuffled surrogate |
| fig5a-coverage-ieeg | not reproduced | All 0.712, Local 0.567, Non-local 0.602 (Local is lower) |
| surrogate-ieeg | reproduced | 0.201 phase, 0.184 IAAFT, 0.229 block |
| surrogate-order-ieeg | not reproduced | IAAFT is lowest in all 12 subjects, not phase |
| lagged-ieeg-no-gain | reproduced | 0.603 against 0.602 |
| 9 EEG claims | blocked (`not_runnable`) | the EEG data are not in DANDI:000055; the iEEG work used the whole run |

**2. The dataset, assumptions and questions**
- **Version:** I pinned 0.220127.0436, the only published version. The paper cites no version.
- **Event times (major):** in four files the `reaches` table and the ReachEvents timestamps disagree by 29,240 to 86,400 s. In three of them, the recordings shorter than 24 h, the table puts 22 to 132 events after the end of the recording. I did not establish which table is right.
- **Electrode metadata:** no electrode has an anatomical label (every `location` is "unknown"), so the code's atlas neighbourhood could not be built. Eight sub-12 electrodes have no coordinates. sub-09 has 16 electrodes on the other hemisphere's side, although the paper says one hemisphere per subject.
- **Event alignment:** sub-02 and sub-09 show no high-gamma change locked to the movement events, so alignment is not established for them. No session was deposited twice.
- **Data dropped:** 7,718 of 8,088 events were kept. 238 were past the recording's edges and 132 had missing samples nearby.
- **Assumptions:**
  - Trials are the `reaches` events with all sessions pooled.
  - Whole-recording preprocessing is approximated by filtering each event with 5 s of padding. The real version would mean reading 845 GB.
  - The mask covers the whole neighbourhood (m = 1.0).
  - Row n of Table II is sub-n.
- **Questions for the paper's authors:** recorded as a `methods_unavailable` finding. They ask which events and days form the trials, where preprocessing is applied, how the table rows map to subjects, and which mask intensity the tables use.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or did not fit**
1. The protocol asks for one `entry.py all` run, but my tool stops a command at 60 minutes by default. The first `all` was cut after notebook 1 finished, so there is no run stamp. I ran notebooks 2 and 3 in the entry's locked environment with the same nbconvert command. There was no time left for a full re-run.
2. The protocol does not say how to write the conclusion cells when the notebooks take most of the run to execute. I added the conclusion and summary markdown after execution, identically to the notebooks and the executed copies, leaving code and outputs untouched. A fresh `run` will re-execute everything.
3. The five-seed rule could not fit the time on this many model fits. I ran it for intra-ieeg-mean only and said so in the other claims' deviations.
4. Speed deviations: training used every 10th sample and stopped at 200 epochs. On sub-07 this changes the score by at most 0.0003.
5. For `data: elsewhere` claims stopped by the time limit, the protocol names no block reason. I used `not_runnable`.
6. The surrogate claim's end-matched reading is not well defined, because trimming gives series of different lengths. I recorded it as not run.
7. The criterion's second event reading, movement plus rest trials, has no definition of rest trials in the paper or its code. It was not run.

**4. Runtime and failures**
- The notebooks took 45.7, 41.8 and 41.7 minutes, with peak memory up to 8.6 GB. Most of each is loading about 7,700 events over the network, about 14 to 22 minutes per notebook.
- The first `all` run was lost to the 60-minute tool limit.
- Untracked dotfiles and folders I did not create (`.bashrc`, `.idea`, `scripts` and others) appeared at the repository root. I left them alone; they should not be committed.
