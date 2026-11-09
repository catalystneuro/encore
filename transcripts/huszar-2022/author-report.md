Everything for steps 1 to 6 is in place: the claims file, the entry, the attempt record, a clean locked run, and the verifier's handover package. The paper's full text was open access (the author manuscript, PMC10807234), but the Supplementary Tables could not be read. I pinned version 0.230630.2304, the only published version. The draft adds only three BIDS files.

### 1. Outcome per claim

| Claim | Outcome |
|---|---|
| cohort-birthdates (17 mice by birthdate, 12 M / 5 F) | not reproduced: the files give 13 M / 4 F because e13_1f1 is stored as male |
| sessions-durations (92 sessions, 113.7 to 475.6 min, median 309.1) | partially reproduced: 104 files, median 319.6; two files have no scored sleep |
| spwr-duration (median 36.4 ms) | reproduced: 36.0 ms |
| unit-count (9,471 units) | not reproduced: 8,201 |
| maze-cohort (9 maze mice by birthdate, 3 novel-environment mice) | reproduced, under the paper code's reading |
| maze-task (205 cm trials, 30 Hz, at least 10 trials per arm) | not reproduced: only 38 of 65 sessions have 10 or more trials per arm |
| novel-explorations (16) | partially reproduced: 9 have position |
| fig5e population-vector decorrelation | partially reproduced: stem 0.937 matches; the other three segments come out more correlated than reported (0.547, 0.492, 0.465) |
| fig6c firing rates preserved familiar vs novel | reproduced: rho 0.734 |
| fig6c ratemap correlations higher in novel mazes | not reproduced: p = 0.67, though the novel median is higher in all 9 sessions |
| fig6d spatial information lower in novel mazes | partially reproduced: direction holds, both medians lower than the paper's |
| fig6d firing rates lower in novel mazes | partially reproduced: direction holds, both medians higher than the paper's |
| 22 claims comparing same- and different-birthdate neurons, birthdate profiles, the model, histology | blocked: data missing |
| fig7fg convergence onto interneurons | blocked: metadata insufficient |

### 2. What was found about the dandiset
- **Light-responsive labels are missing.** No unit is marked light-responsive, and no cell type, waveform or optogenetic pulse time is stored, in the processed or the raw files. This blocks the paper's central findings. The labels exist in the lab's CellExplorer files, which are only reachable through the lab databank via Globus, with no DOI or commit.
- **Units are missing for 6 of the 17 mice** (39 files hold only sleep states and ripples).
- **7 of the 16 novel explorations have no position**, likely the three open fields. Five novel recordings give x and y between 0 and 1 even though the unit is stated as cm.
- **Metadata errors:**
  - `is_familiar_maze` is wrong in sessions with only the familiar maze.
  - e13_1f1's sex field says male.
  - 12 of the 13 raw files give a session start of 2011-08-18.
  - One processed file holds a copy of the LFP labelled 30 kHz with a wrong conversion factor.
  - Unit `group_id` values don't match the electrode group names in 64 of 65 files, and units have no link to electrodes.
  - The electroporation day is stored only in the subject id.
- **The paper contradicts itself on session count.** The Methods say 92 sessions; Figure 1e says 96. The files of the 15 homecage mice are exactly 96, and they match Figure 1e by birthdate and the Methods' duration bounds.
- **No duplicate recordings were found.**

### 3. Where the protocol was unclear, wrong or missing something
1. Outside data must be "public and pinned", but the paper's own data link reaches only an unpinned lab server behind Globus. I treated this as not usable and blocked those claims as data missing.
2. For a label that exists in the lab's derived files but not in the dandiset, it is unclear whether the block reason is data missing or metadata insufficient. I used data missing, because the pulse times needed to derive the label are also absent.
3. There is no guidance on when to stop trying to recover missing data from raw files (pulse artefacts in 54 to 184 GB files). I made one quick look at the LFP while preparing, mentioned it as not run here, and blocked.
4. Using the paper's code to choose subsets (which mice to exclude, which sessions to include) is somewhere between "following the code" and an outside input. I listed the code under `inputs` as parameters only and kept those claims as using the dandiset alone.
5. My sessions criterion named a condition (each session holds sleep) without saying which outcome its failure gives. I chose partially reproduced and recorded it as a deviation. The protocol could require every condition to map to an outcome.
6. The default 10% tolerance doesn't work for values near zero (median correlations around ±0.05). I used ±0.03 and gave the reason.
7. The protocol doesn't say what to do when a criterion's literal reading gives a result that is probably a metadata typo (the sex field). I followed the criterion and recorded a finding.
8. Data-description claims (counts, durations) aren't addressed by the protocol. I included them because they speak directly to whether the dandiset is complete.

### 4. Runtime and failures
- The notebook takes 356 s in the clean environment (about 2.5 min of that is streaming). `entry.py check`, `all` and `handover` all passed.
- The Europe PMC full-text API returned a server error, so I got the text through PMC's OAI service instead.
- **Left behind, needs your attention:** an empty `.claude/` directory inside `entries/000552-huszar-2022/`. I couldn't delete it because the removal needed a permission approval this session can't give. It holds no files, so git won't commit it.
- **Untracked files I didn't create:** dotfiles (`.bashrc` and others) and `scripts` appear untracked at the repo root. I left them alone.
- Nothing was committed.
