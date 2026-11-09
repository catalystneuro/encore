I re-ran nothing and changed no claim, notebook or record, because there were no questions to answer.

**The questions.** `questions/000129.yaml` does not exist, and git history shows it was never created. My first author run (commit 9a22704cb) asked no reader anything. It found no place where the claims file misreads the paper. The open questions it did raise are for the paper's authors, not a reader, and are recorded as `methods_unavailable` findings in `attempts/000129-makin-2018-01.yaml`:
- which kinematics were decoded;
- which input went into the figure 8 Gaussian-versus-UKF comparison;
- whether the UKF2 code and its ridge setting can be shared.

The answer run (commit ebd0b57ec) came to the same conclusion and made no changes. `claims/000129/` was last changed by the claims-check run, before my author run.

**Effect per claim.** Every outcome stays as the first author run recorded it, and no claim's notes needed an update.

**Entry checks.**
- `python tools/entry.py lock` rewrote `requirements.lock.txt` with no change to its contents.
- `python tools/entry.py all` found 0 errors, and both notebooks passed on a clean run: `reproduce_makin_2018.ipynb` in 586 s and `binwidth_training_neurons.ipynb` in 1255 s. Both times are close to the first run's (604 s and 1301 s).
- `python tools/entry.py handover` wrote `executed/000129-makin-2018/handover`.

I did not verify the work, and nothing was committed or pushed. Some untracked files appeared at the repository root during the run (`.bashrc`, `.profile`, `.gitconfig`, `.vscode`, `.idea`, `.mcp.json`, `scripts`, and others). They look like leftovers from the sandbox environment, not anything this run wrote. I left them alone; they should not be committed.
