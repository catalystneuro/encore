The reconciliation block is written in `attempts/choi-2025-02.yaml`. I added `entries/choi-2025/earlier_findings.ipynb` and listed it in `entry.yaml`. The lock file didn't change, both notebooks ran clean (90 s and 18 s), and `python tools/entry.py check entries/choi-2025` reports 0 errors. Nothing is committed.

**1. Blind: no (`blind: false`).** The author saw no record, entry, questions, transcript or note of choi-2025-01. The audit lines are only links to the pilot notes and the README. But two inputs the protocol hands the author summarised the earlier attempt's results:
- the dandiset's release notes, which list the conversion fixes made after "a reproduction attempt";
- the claims file's opening comment, which gives the earlier 11812.1 s clock offset.

The author disclosed both in its report and tested the offset, which does not hold on this version. If the registry counts dataset metadata as allowed exposure, this could be flipped to `true`.

**2. Earlier findings**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Raw ephys and spikes on a different clock (11812.11 s) | fixed | |
| 2 | Absolute times disagree with the Neuralynx header | fixed | |
| 3 | Spike times 7.1 ms after the raw trough | fixed | |
| 4 | LFP called beta-band, wrong conversion factor | fixed | |
| 5 | Waveforms and FSCV current in the wrong units | fixed | |
| 6 | FSCV table columns have no units; `good` is true everywhere | still_present | 3 |
| 7 | Subject and session descriptions from another study | fixed | |
| 8 | Events stored about five times each, unsorted; Plexon times unsorted | fixed | |
| 9 | Trial tags carry no trial type; trial 1411 differs from the paper's lists | still_present | 6 |
| 10 | Target top/bottom position not in the data (only left/right) | still_present | 10, added with `found: on_prompt`, severity minor |
| 11 | Raw FSCV clock not established; `iox` not found in raw scans | partly_fixed | 9 |
| 12 | Only one session of monkey T deposited | still_present | 1 |

For finding 10, the reward condition codes 41 and 40 are now described as the big and small reward. Only the target position is still missing.

**3. New findings in choi-2025-02:** 2, 4, 5, 7 and 8.

**4. Outcomes that changed:** none. All 13 claims have the same outcome in both attempts: four reproduced, one partially reproduced (fig9d), eight blocked as data_missing. So the block has no `outcomes` list.

**5. Protocol issues**
- `docs/pilot-notes.md` has no sections for pilot-15 to pilot-18. I took the pilot-18 severity rule from `docs/protocol.md` and said so under `protocol`.
- The blind rule doesn't cover release notes that summarise an earlier attempt's findings. Step 1.1 requires reading them, so here the exposure couldn't be avoided. The claims file's opening comment had the same effect.
- The claims file was never rewritten after pilot-9 and pilot-10. Both attempts applied criteria whose method choices the earlier author made after seeing the data. So the two attempts agreeing is weaker evidence than two independent readings of the paper would be.
- Earlier finding 11 is now resolved as a problem with the earlier attempt's method, but it has been replaced by a new one: `iox` is a smoothed copy of the raw current, lagging it by about 1.5 s, and the file doesn't say so. I marked it `partly_fixed`, pointing at finding 9.
- The working tree shows untracked entries such as `.bashrc`, `.idea` and `scripts`. They are sandbox device placeholders, not files I made; I left them alone.
