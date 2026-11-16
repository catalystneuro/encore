I finished author steps 1 to 6 for `entries/jacobsen-2022/` and the record `attempts/jacobsen-2022-01.yaml`. The entry passes `tools/entry.py all` with 0 errors, the notebook runs in 81 s in a clean environment, and the handover is in `executed/jacobsen-2022/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig5c-functional-cell-types | reproduced, resting on an assumption (which shuffle reading) |
| fig5c-responsive-grid-cell | reproduced |
| fig5c-example-cells | reproduced, resting on an assumption (which laser epoch for each day-17 cell) |
| figs3-stable-input-cell | partially reproduced, resting on an assumption (same cell matched by waveform); 17 of 18 values match |
| figs4-nonresponsive-cells | partially reproduced, resting on an assumption (definition of the head direction score); the head direction score and the peak rate miss |
| responsive-cells-at-19-days | reproduced |
| mec-inputs-from-two-weeks | reproduced |
| 19 histology claims and 2 imaging claims | blocked, `data_missing` |

With the pulse time taken as the laser onset, the latencies and fidelities in the paper come out exactly, to two decimals (for example T1 C89 at 2.75 ms and 40.73%).

## 2. The dataset, assumptions and questions

**Version.** 0.220506.1516 is the version the paper cites and also the latest published one.

**What it holds.** Nine optrode sessions from mice 58313 and 70375, with only the 12 curated units shown in the figures. Unit ids are tetrode × 1000 + cluster, so the figure labels can be found directly. The histology and imaging are not in it, and the paper names no other deposit for them.

**Findings recorded:**
- The open field part of each session is not an epoch in the files.
- The two laser epochs of the day-17 session carry no power label; the other files say 20 mW.
- The first laser event of every epoch is spurious: it starts at the epoch start and lasts 0.6 to 1.9 s.
- The pulses come in trains of 6 every 2.6 s, where the Methods say "10 Hz continuously".
- The LFP timestamps run backwards within each file.
- `waveform_mean` is labelled volts but its values cannot be volts.
- In day 14 session 2 of 70375, the paper's values match the first 1800 s and the first 275 pulses of a longer file; over the whole file the rate misses.
- The day-17 open field covers only 76 × 75 cm.

**Assumptions:**
- The shuffle is a shift of at least 20 s. Read literally (within ±20 s), the border cell misses its threshold, 0.656 against 0.663.
- Each day-17 example cell is matched to its own laser epoch: T1 C57 matches the second, T1 C52 the first.
- The six 70375 units are one cell: their waveforms correlate 0.92 to 1.00.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How is the head direction score defined? Rowland et al. (2018) name only the mean vector length. How is the 9.02 Hz peak of the tuning curve computed?
- Which day-17 laser epoch does Figure 5C use?
- What does "random interval between ± 20 s" mean in the shuffle?

**Questions to a reader:** none.

## 3. Problems with the protocol and tools

1. `tools/entry.py lock` wrote `python: "3.13"` into `entry.yaml`, and the entry schema then rejected that field. I removed the line; the Python version falls back to the lock file.
2. The protocol does not say how to treat readings listed in the claims file's shared opening comment (here, laser onset against offset). I applied the rule for criteria, that a claim holds under any listed reading, and reported both readings for every claim.
3. The protocol has no rule for an epoch choice made per unit, where the files leave two laser epochs unlabelled. I ran every option and marked the outcome as resting on an assumption.
4. The cited paper's linked code (Rowland's archdata repository) gives parameters its Methods text leaves out, and in one case disagrees with the text (2 cm against 2.5 cm bins). The protocol's order of sources covers this paper's own code, not code of a paper it cites. I put the text first, used the code for the gaps, and listed the code under `inputs`.
5. The claims file adds a fidelity floor to the responsiveness rule but gives no chance level, so the protocol's rule on chance levels could not be applied. I showed the fidelity in the 10 ms before each pulse and with the pulse times shifted by 50 ms.

## 4. Runtime and failures

The work took about 21 minutes (03:04 to 03:25 UTC). The only failure was the `python` field in item 1. Untracked files such as `.bashrc` and `.idea` in the repository root are sandbox device files created at 03:03, before this run; I left them alone.
