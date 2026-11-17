Round 3 is recorded. One outcome changed and no proposals stand.

**Outcome changed**
- `supp12-no-false-eye-detection` goes from blocked (`too_large`) to **reproduced**. The verifier agreed with the proposal, so I set the outcome, removed `blocked_by` and `proposed`, and left every other outcome as it was.

**Record and text**
- In `attempts/mallory-2021-01.yaml`, round 3 is under `verifications` with one result: the verifier agrees, gives reproduced, its reason is in its own words, and my response is there.
- The verifier noticed the notebook time didn't match: the notes said 41.3 min but the notebook printed 40.4. The notes now give 40.4 min, and also the time of this round's re-run.
- The summary tables in both notebooks, the main notebook's status table, the simulated notebook's result line and the README now all say reproduced.
- `python tools/entry.py check entries/mallory-2021` passes with 0 errors.

**The re-run was incomplete**
- `entry.py all` could not run as one command. Running all four notebooks takes about 3 hours, and a single shell command here is cut off at 2 hours. Starting it in the background didn't work either, because the sandbox stops background processes when the command that started them ends.
- Instead I ran `check`, then executed each notebook separately with the same environment and nbconvert call that `run` uses. This means no clean-run stamp was written.
- The machine was under load from outside this session (load average about 5 on 4 cores), so the notebooks ran slower than before:

| Notebook | Time | Over the 60-minute limit? | Results |
|---|---|---|---|
| `simulated_eye_mallory_2021.ipynb` | 72.1 min | Yes | Same as before: 718 eye units; 0, 2, 2 and 0 detections; mutual information above every shuffle in 11 of 11 sessions |
| `reproduce_mallory_2021.ipynb` | 78.9 min | Yes | Same counts as before (718; 341, 243, 238, 137) |
| `readings_folds_mallory_2021.ipynb` | 70.7 min | Yes | No errors |
| `freely_moving_mallory_2021.ipynb` | Not run | — | Not re-run before the 22:09 cutoff; its text has not changed since round 2 |

Because three notebooks went over 60 minutes, `entry.py run` would mark them as failed on this machine. The workflow's own run should confirm the times.

Nothing is committed. The sandbox shows placeholder files in the repo root (`.bashrc`, `.idea`, `scripts` and others, dated 17:53, before this work started). I left them alone, but they shouldn't be committed.
