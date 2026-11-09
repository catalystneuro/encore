The reader's answer changed no outcome. I re-ran every affected claim under both region readings the amended criterion names, and each claim comes out the same under both readings as it did before.

`entry.py lock` and `all` passed with 0 errors; the notebook takes about 14.5 minutes. The numbers came out the same in two clean runs, and the conclusions match the executed copy. The handover is built in `executed/000575-boran-2022/handover/`. Nothing is committed or pushed, and I did not verify my own work.

## The question: how units are assigned to regions (neurons-recorded)

**What the answer changed.** The reader found that the claims file had fixed the electrode-name rule without a source. The criterion now names two readings: (a) by the anatomical location of the microwire tips, as Figure 1d shows them, and (b) by electrode name. The per-region claims use the reading under which neurons-recorded is judged.

**What I did.**
- **Reading (a).** The files hold no location for the wires themselves. I used the atlas label of each bundle's tip contact, citing Methods 2.3 (the wires protrude 4 mm from the tip) and the Figure 1d legend. This was a variant in the first run and is now reading (a) everywhere.
- **133 units without a usable tip label.** Their tip contact is labelled "unspecific" or "FuG". They keep their electrode-name region, because Figure 1d colours every site as one of the three regions. The notebook also prints the count without them, and this choice is recorded as a deviation.
- **Two analyses added under reading (a).** The cluster-based test of fig2d and the unpaired test of the correct-vs-incorrect claim had only run by electrode name.
- **Measured values.** No reading meets the criterion for any per-region claim, so I record the first reading the criterion lists, (a). This is why the measured values change while the outcomes do not.

Each claim's notes say what the answer changed. The notebook conclusions, the summary, the README, the helper docstring and one finding (the dataset holds no tip locations) are updated to match.

## Outcomes, now against before

| Claim | Before | Now | (a) tip location | (b) electrode name |
|---|---|---|---|---|
| neurons-recorded | partially reproduced | partially reproduced | Hipp 495, Ent 168, Amg 146: Hipp and Amg in tolerance, Ent not (paper 454, 209, 146) | 361, 217, 226: only Ent in tolerance |
| fig2c-maintenance-neurons | partially reproduced | partially reproduced | paired 62, 20, 16; unpaired 55, 19, 13: two of three in tolerance each, all p = .002 | 48, 28, 22 and 42, 26, 18: none in tolerance |
| fig2d-workload-modulated-maintenance-neurons | not reproduced | not reproduced | 2, 0, 2 (named counts), none significant | 2, 1, 2, none significant |
| maintenance-neurons-correct-vs-incorrect | not reproduced | not reproduced | 57 vs 19, difference p = .71 | 47 vs 13, p = .33 |
| fig3b-test-neurons | partially reproduced | partially reproduced | no reading puts all four counts in tolerance | same |
| fig4d-decode-workload-regions | not reproduced | not reproduced | Hipp 48–49%, Ent 47%, not significant | Hipp 49–53%, Ent 45–46%, not significant |
| decode-performance-not-significant | reproduced | reproduced | no group reaches p < .0125 | same |

`git status` shows untracked files at the repository root that I did not create: `.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.vscode`, `.mcp.json`, `scripts` and a few others. They are probably left over from the runner, and I did not touch them.
