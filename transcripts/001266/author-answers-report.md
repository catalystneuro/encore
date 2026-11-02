No reader questions were asked or answered for DANDI:001266, so nothing in the entry or the record changed.

- **Questions:** `questions/001266.yaml` does not exist and never has. My first author run asked readers no questions. The answer run (`transcripts/001266/answer-report.md`) found nothing to answer and left `claims/001266/` unchanged. The five open method details I raised earlier went to the paper's authors as `methods_unavailable` findings, not to a reader:
  - the spike and dSpike thresholds and the distal region
  - dF_ref for bursts
  - the AUC window
  - the noise-equivalent voltage
  - the PCA pixels
- **Changes:** with no amended claims, I re-ran no analyses. The notebooks, conclusions, claim notes and attempt record (`attempts/001266-park-2025-01.yaml`) are as the author run left them.
- **Outcomes:** all 55 are the same as before:

| Outcome | Claims |
|---|---|
| Reproduced | 7 |
| Partially reproduced | 5 |
| Not reproduced | 10 |
| Blocked, methods underspecified | 2 |
| Blocked, data missing | 29 |
| Blocked, too large | 1 |
| Blocked, not runnable | 1 |

- **Entry commands:**
  - `lock` rewrote `requirements.lock.txt`, and its content is the same as before.
  - `all` found 0 errors. `reproduce_park_2025.ipynb` passed in 1459 s and `simulations_park_2025.ipynb` in 99 s, both run from a fresh environment.
  - `handover` wrote `executed/001266-park-2025/handover`.

Nothing is committed or pushed. `git status` shows no tracked changes. The untracked dotfiles, `.idea`, `.vscode` and `scripts/` at the repository root were there before this run, and I left them alone.
