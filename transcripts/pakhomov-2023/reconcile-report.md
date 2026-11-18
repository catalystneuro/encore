I've added the `reconciliation` block to `attempts/pakhomov-2023-05.yaml`. `python tools/entry.py check entries/pakhomov-2023` reports 0 errors, and a clean run passed both notebooks: `reproduce_pakhomov_2023.ipynb` (1004 s) and the new `earlier_findings.ipynb` (92 s). Nothing is committed.

**1. Blind: yes.** The audit printed three lines. Two are the repository README naming the registry website, which the author read when it read the README; the author never fetched the site. The third is the author writing its own record. No transcript mentions attempts `-01` to `-04` or the entry `pakhomov-2023-001027`.

**2. Earlier findings**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Fig. 4 time lapse, and the Fig. 5–7 and 9 monolayers, not in 001027 | still_present | 1 |
| 2 | Protocol 2 and Protocol 3 labels look exchanged | still_present | 8 |
| 3 | No pixel size, electrode positions or e1; exposure and gain not recorded; Packet 1 dishes have twice the background | still_present | 2 |
| 4 | Species summary "Cricetulus griseus - Cricetulus aureus", age P1D, dish 10 names no device | still_present | 9 (added, `found: on_prompt`) |

- **Finding 1:** the Fig. 5–7 and 9 data were in the other four dandisets all along, at versions published in 2024, before attempt 04. Attempt 04 only looked at 001027, so nothing about that part changed. The note says so.
- **Finding 3:** 05's finding 2 covers the pixel size and the electrodes but not exposure, gain or background. The notebook checked that part: no field names exposure or gain, and the background is 308.9 a.u. on 24 March against 161.1 and 150.0 a.u. on 17 and 18 March, 1.94 times the other days. I put this into finding 9, because `now` can point at only one finding.
- **Finding 4:** unchanged; dish 10's description gives an unknown microscope, detector and objective, and its session starts 18 March 2021 at 18:50.

**3. New findings:** 3, 4, 5, 6 and 7 (the second frame in 17 files, the Bos taurus species in 000686 and 000875, the six dishes deposited twice, the dish counts in 001025, and the questions for the paper's authors).

**4. Outcomes that changed**
- `fig6a-more-packets-more-uptake`: blocked → partially_reproduced.
- `fig9b-gap-boosts-targeting`: blocked → reproduced.

The reason for both is the protocol and claims-file change, not the data. Attempt 04 tested only 001027, which holds neither experiment. Attempt 05 used the Fig. 6 and Fig. 9 dandisets (000875 and 001028).

`fig6-peak-narrower` is blocked in both, but for different reasons (data_missing earlier, methods_underspecified now). Since the outcome is the same, I added no item for it. The three Fig. 8 claims are not_reproduced in both.

**5. Protocol fit**
- The `protocol` field says pilot-14 files records by paper. The earlier attempt tested one dandiset with its own 18-claim file; this one used all five with a new 24-claim file, so several claim ids no longer match and only shared ids could be compared.
- Earlier finding 3 is only partly covered by 05's finding 2, and the schema allows one `now` per finding, so I put its uncovered part into finding 9, as described above.
- Finding 2 in 05's record reports "1 or 96" for the resolution of 001025, 001027 and 001028; that is consistent with dish 10's 1.0.

Other untracked files are in the working tree that I did not create: dotfiles (`.bashrc`, `.profile`, `.gitconfig`, `.zshrc` and others), `.idea`, `.vscode`, `.mcp.json` and `scripts/`. I left them alone, so you may want to check that the workflow's commit doesn't pick them up.
