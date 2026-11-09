No reader answered any question on this attempt, so I changed no claim, notebook, conclusion or attempt record.

**Questions:** there are none. `questions/crcns-ac-2.yaml` doesn't exist, and no branch's git history has ever had it. In the first run I asked a reader nothing; my open points were for the paper's authors and are recorded as `methods_unavailable` findings. The answer run (`transcripts/crcns-ac-2/answer-report.md`) says the same: it had nothing to answer and left the claims file alone. `claims/crcns-ac-2/10.1152-jn.00197.2004.yaml` hasn't changed since the claims-check commit.

**Outcomes:** all 23 outcomes are the same as before.

| Claim | Before | Now |
|---|---|---|
| fig2-stereotyped-shape | partially reproduced | unchanged |
| fig3a-reliable-neuron | reproduced | unchanged |
| fig3b-total-variability-distribution | reproduced (assumed) | unchanged |
| total-variability-population | reproduced (assumed) | unchanged |
| lfp-culling-reduction | reproduced (assumed) | unchanged |
| fig5b-residual-lfp-psp-correlation | reproduced | unchanged |
| fig7a-lfp-culling-estimation | partially reproduced (assumed) | unchanged |
| psp-culling-reduction | partially reproduced | unchanged |
| fig4c-psp-culling-can-increase | partially reproduced (assumed) | unchanged |
| fig7b-private-best-estimate | reproduced | unchanged |
| culling-controls | not reproduced | unchanged |
| fig7d-large-responses | reproduced | unchanged |
| large-responses-controls | not reproduced | unchanged |
| cv-large-responses | partially reproduced | unchanged |
| lfp-cv-not-different | reproduced | unchanged |
| anesthesia-comparison | partially reproduced | unchanged |
| fig8-spontaneous-veto | reproduced | unchanged |
| overfitting-correction-example | reproduced | unchanged |
| private-shared-ranges | partially reproduced | unchanged |
| quantal-comparison | reproduced | unchanged |
| mepsp-size | blocked (`methods_underspecified`) | unchanged |
| recording-properties | reproduced (assumed) | unchanged |
| access-resistance-depth-no-effect | reproduced (assumed) | unchanged |

**Entry checks:**
- `python tools/entry.py lock` rewrote `requirements.lock.txt` with the same content as before.
- `python tools/entry.py all` reported 0 errors, and the notebook passed in 120 s.
- `python tools/entry.py handover` wrote `executed/crcns-ac-2-deweese-2004/handover`.

Nothing is committed or pushed. Git now shows some untracked files in the repo root (`.bashrc`, `.gitconfig`, `.idea`, `.vscode`, `scripts` and similar) that I didn't create and left alone. The tracked files are unchanged.

If a verifier round later sends a question to a reader and it gets answered, this run will need to be done again.
