I've added the `reconciliation` block to `attempts/tingley-2019-02.yaml`. The new notebook `entries/tingley-2019/earlier_findings.ipynb` is listed in `entry.yaml` and the README. Locking changed nothing in the lock file. `entry.py check` reports 0 errors, and `entry.py run` passed all five notebooks (the new one took 298 s). I edited the README after that run, so the run's stamp may be out of date. Nothing is committed.

**1. Blind: yes.** The audit lines are the repository README and the run's own provenance URL. The author did read the dandiset's release notes to choose a version. They say the files were re-converted to fix "problems found by a reproduction attempt (issue #82)" and list the fixes. The author did not open the issue and saw none of tingley-2019-01's outcomes or findings. I left out `blind_note`, since the schema only asks for it when `blind` is false.

**2. Earlier findings**

| # | Problem | Status | Now |
|---|---|---|---|
| 1 | No detected events | partly_fixed (LSRipples in 77 files, CA1Ripples in 47; 8 files have no event table) | 8 |
| 2 | Units without a region | partly_fixed (only DT7 20170407 remains, 36 units) | 6 |
| 3 | `hpc` labels; four DT7 files all `unknown` | still_present (the `unknown` part was not reported, so I added it as finding 17) | 5 |
| 4 | CA3 files with no CA1 channel | partly_fixed (fixed in the 6 DT5 files, not in the 4 DT9 files) | 8 |
| 5 | No electrode positions or depth | still_present | 2 |
| 6 | No waveforms or quality metrics | partly_fixed (5968 of 6236 units have a waveform, 4519 an isolation distance) | 16 |
| 7 | Optogenetic rats missing | still_present | 1 |
| 8 | Spike times out of order | fixed (0 of 6236 units) | none |
| 9 | Paper's code repository lacks the analyses | still_present (repository still at commit 9f4cd48) | 18 (on_prompt) |
| 10 | Paper's band and figure references disagree | still_present (paper unchanged) | 19 (on_prompt) |
| 11 | A signal shared by the LS and CA1 channels | still_present (details below) | 20 (on_prompt) |

On finding 11, the same-sample pairs are gone: only 0.026 of coupled pairs fall within 0.5 ms for the lab's detections, against 35% in the earlier attempt's own detection. The shared signal is still in the LFP: at random times the phase-locking value has a median of 0.177, against 0.024 with a 1 s offset.

**3. New findings of tingley-2019-02:** 3, 4, 7, 9, 10, 11, 12, 13, 14, 15. Finding 3, the missing depth in LS, is also part of earlier finding 5, which can only point at finding 2.

**4. Outcomes that changed**
- **Version change.** Version 0.250624.0439 held no events, so tingley-2019-01 detected its own. This attempt used the lab's deposited detections.
  - fig1c-hfo-each-animal: not reproduced before, partially reproduced now.
  - fig1g-slower-than-ripples: not reproduced before, reproduced now. Part of the shift comes from the lab's own filter bands: 120-180 Hz for LS, 130-200 Hz for CA1.
  - fig5b-nrem-and-rates: partially reproduced before, reproduced now.
  - fig5d-lag: not reproduced before, reproduced now. The earlier lag of 0.00 ms came from its same-sample events; the lab's events give 6.20 ms.
- **Rewritten claims file.** A reader wrote the claims file again between the two attempts.
  - fig4b-pre-post-unchanged: reproduced before, partially reproduced now. The new file adds the paper's 7172 pairs as an expected value, which 462 pairs miss.
  - fig4-sessions-few-change: blocked before, not reproduced now. The new file drops the minimum of 5 pairs per recording.
  - fig4c-temporal-bias: blocked before, reproduced now. The new file drops the minimum of 10 pairs per recording.
  - fig4d-compression: not reproduced before, partially reproduced now. The new file's bound for a partial outcome is lower.
  - fig5e-state-coupling: not reproduced before, partially reproduced now. The new file allows pooling over all events; over recordings both attempts fail.
- **Method choice.** fig1h-no-amplitude-frequency-correlation went from not reproduced to reproduced. It turns on whether the amplitude is the stored peak normalized power or one recomputed from the LFP. This attempt's own recomputation gives r = 0.081, p = 1.3e-38, which would not reproduce.

**5. What did not fit**
- `docs/pilot-notes.md` has no sections for pilot-11, pilot-15 or pilot-16, so the `protocol` note covers pilot-8 to pilot-14.
- The history is a shallow clone, so the `git log` command in the prompt finds the current commit. I got the claims file tingley-2019-01 used from GitHub at commit 8b3aeba6f7.
- Finding 16 of tingley-2019-02 says the DT5, DT7 and DT9 files have no waveforms. The new notebook finds them in 19 DT5, 7 DT7 and 14 DT9 files. I said so in the note and left the statement unchanged.
- Earlier finding 3 was only partly reported by tingley-2019-02, so it got a `now` pointer to finding 5 plus a new finding 17 (`found: on_prompt`) for the `unknown` labels.
- I checked finding 10 against the paper's text, which is not part of the entry; its section in the notebook is prose only.
- Untracked dotfiles (`.bashrc`, `.gitconfig`, `.idea` and others) and a `scripts` folder are in the repository root. I did not make them and left them alone.
