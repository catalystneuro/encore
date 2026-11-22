All four claims that can be tested on DANDI:000010 have been tested. The entry passed `tools/entry.py check` and a clean `run` (220 s, peak memory 1.24 GB), and the handover package is built. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| figs4-session-selection | not reproduced: 9 or 10 mice and 15 to 18 sessions under every reading, against the paper's 11 mice and 20 sessions |
| figs4-lowest-couplers-correlated | partially reproduced, rests on an assumption: 0.048 against 0.06 ± 0.006, Holm p = 0.0007 |
| figs4-high-couplers-correlated | not reproduced, rests on an assumption: the 57–71% bin is 0.008 (p = 0.074); the 71–86% bin is 0.021 and the top bin 0.067 (both p = 0.0007) |
| figs4-middle-couplers-not-correlated | reproduced, rests on an assumption: Holm p 1.0, 1.0 and 0.54 |
| 30 imaging claims | blocked (`other`): the paper's imaging data are not public |

No outcome changes across the five seeds.

**2. Dataset, assumptions and questions**

- **Version:** only one published version exists (0.220126.1905). The draft holds the same 158 assets, so I pinned the published one.
- **Duplicated units (rated critical):** 50 of 99 files list some unit ids twice, 72 extra rows in all, and each repeated id holds an identical spike train. I count them once. This changes which sessions pass the paper's 18-unit filter.
- **Selection gap (rated major):** the dataset holds 10 KJ18 (Sim1) and 6 PL56 (Tlx) mice. Under every reading only 7 Sim1 and 2 or 3 Tlx mice have a session that passes, against the paper's 8 and 3.
- **Minor findings:**
  - All 1,441 units are labelled "good", so the paper's quality filter keeps every unit.
  - Every trial is labelled "audio delay", but the files' own description and the paper describe a tactile task.
  - 558 event timestamps are NaN.
  - 574 trials have a sample time but no observation interval, so no spikes are stored for them.
  - 10 units store spike times out of order.
  - Two files hold spikes outside the observation intervals.
- **Checks that passed:** decoding the instructed side gives about 0.52 before the sample cue and 0.88 after GO, and about 0.5 with labels shifted by one trial, so spikes and trial events share a clock. Photostimulation onsets agree with the stored laser trace.
- **Assumption:** I adopted reading `baa` of the claims file's open details (the three letters are O1, O2, O3 in order):
  - O1 (b): only units above 0.5 Hz enter a session. The paper's FigureS4.ipynb prints 20 sessions of 18 to 25 neurons, and only the O1 (b) readings give that range.
  - O2 (a): the "session-wide" rate is taken over the whole recording.
  - O3 (a): only the four trial types CL, CR, IL and IR are used.
  
  All eight readings are shown in the notebook.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): their code does not include the step that builds the per-session arrays from DANDI. It asks them to confirm the unit filter, the rate measure, the trial set, the common window length, and whether duplicated units were counted once.
- **Question for a reader** (`questions/gable-2026.yaml`): the 30 imaging claims are marked `data: elsewhere` although the data are in no public archive. The protocol calls for `data: dataset` with `data_missing` here.

**3. Protocol gaps**

1. For claims marked `elsewhere` whose data are not public, the checker refuses `data_missing`. I blocked them as `other` and asked the reader the question above.
2. The protocol does not say which value to record as `measured` when no reading matches. I recorded the values under the adopted reading.
3. The claims file's standard choice for O5, the shortest common window, would collapse to 2 s if every trial were kept, because a few odd trials have GO at the sample time. I used a fixed 4.6 s window (1.3 s sample + 1.3 s delay + 2 s after GO), dropped trials that are shorter, and recorded this as a deviation.
4. The protocol does not say whether an analysis should follow the paper in counting units stored twice. I counted them once and showed the counts with every stored row as a variant.

**4. Runtime and failures**

The run took about 45 minutes and nothing failed. While developing, I found that spike times were unsorted in some units and that observation intervals end at 5.5 s, not at the trial's stop time. Both are fixed and covered by the data check before the final run. Untracked dotfiles, `.idea`, `.vscode` and `scripts` appeared in the repository root during the run; I did not create them and left them alone.

Files are in `entries/gable-2026/`:
- `reproduce_gable_2026.ipynb`
- `alm_coupling.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is at `attempts/gable-2026-01.yaml`.
