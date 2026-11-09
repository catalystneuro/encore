I've finished steps 1 to 6. `python tools/entry.py all` passed (0 errors, notebook ran in 437 s) and the handover package is in `executed/001535-natraj-2025/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| rnn-training-data-amount | Reproduced, resting on an assumption: 837.4 min against 888 ± 88.8 |
| 49 claims (Figures 1 to 3, 5 to 7, S2 to S8, and fig4cd, fig4fg, figs8ab) | Blocked, `data_missing` |
| fig4b-day-differences, fig4i-boundary-convergence | Blocked, `metadata_insufficient` |

## 2. The dataset, assumptions and questions

- **Version.** I pinned 0.260608.0617, the latest published version, because the paper cites none. It has the same single asset and blob as 0.250714.1218; only the metadata differs.
- **Contents.** There is one NWB file, for participant B1 only. It holds 9737 trials of 256 features at 100 Hz: high gamma in columns 0 to 127, then low frequency, each block L2-normalized to 1 per trial. That is the biLSTM input the Methods describe. Each trial also has `target_id`, `is_virtual` and `is_robot`.
- **What is missing.** There is no participant B3, no Figure 1 task, no MLP band-power features, no online decoder outputs, no kinematics and no task outcomes. No trial has a day, session or OL/CL label; trial start and stop times are placeholders.
- **Metadata problems.**
  - The 9 target ids have no names, while the description says 7 targets.
  - There is no electrodes table, so channels can't be placed on the grid.
  - The age is P38Y where the paper says 41, possibly measured at different dates.
- **Checks.** No trial is deposited twice. The trial labels line up with their own series: target decoding is 0.72 with the true labels, 0.17 to 0.18 with labels shifted by one trial, and 0.13 shuffled.
- **Assumption.** The 9737 trials are the paper's RNN training data, with the 1886 robot trials counted as the "practice with the Kinova Jaco" the Methods include. Without the robot trials the total is 540.0 min, outside the tolerance.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): are these trials the 14 h 48 min training set, are the robot trials that practice or the later RNN fine-tuning data, and is each stored trial whole or only its active portion?
- **Questions to a reader:** none.

## 3. Where the protocol was unclear

1. `archives.md` says to read files with pynwb. With 9737 TimeSeries, reading the metadata over the network is slow: listing the group alone took 164 s. I read the file with h5py and remfile by the same paths, and say why in the helper's docstring.
2. The clock check in step 2 assumes event times or continuous sessions; this file has neither. I decoded the target from trial-mean features with true, shifted and shuffled labels, and stated that this cannot check timing within a trial.
3. Many claims fail for two reasons at once: B3 or the features are absent, and B1's trials have no labels. The protocol asks for one main reason. I gave `data_missing` where the data can't be supplied by better metadata, and named the other reason in the notes.
4. `assumed` is defined for method choices. Here the open point is what the dataset's trials are, not a method, and the criterion shows the robot split without making it a reading. I still marked the outcome `assumed: true`, with a deviation and a finding.
5. Reading (b) of the claim (active portion only) can't be run because there are no task states. I noted it can only be shorter than reading (a) and left the outcome to reading (a), as the criterion's "under one reading" rule allows.

## 4. Runtime and failures

- **Runtime.** About 1 h 55 min, from 23:46 to 01:42 UTC. The notebook takes about 7 min, mostly streaming the file.
- **Lost hour.** A `grep` with a long backtracking pattern on the paper's text hung for the full 1 h tool timeout. After that I searched the text with Python instead.
- **Untracked files.** `git status` shows files I didn't create in the repository root (`.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.vscode`, `.mcp.json`, `scripts` and other dotfiles). I left them alone. Check them before the workflow commits, since it may otherwise commit them.
- Nothing else failed.
