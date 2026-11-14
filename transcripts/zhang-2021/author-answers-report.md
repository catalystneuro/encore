No reader question was answered, so nothing changed and no claim was re-run.

- **No questions to answer.** `questions/zhang-2021.yaml` does not exist, either in the working tree or in git history. The reader's answer run found the same thing and said so in `transcripts/zhang-2021/answer-report.md`. It left `claims/zhang-2021.yaml` unchanged. My first run asked the reader nothing. Its three open questions are for the paper's authors and are already recorded as `methods_unavailable` findings in `attempts/zhang-2021-01.yaml`:
  - how the attention axis is defined when its regression weight is zero;
  - in what order the nine game variables enter the QR;
  - what exactly the passive-against-attentive test compared.
- **Notebook, conclusions and record.** I didn't edit any of them, so no claim's notes have anything new to report.

| claim | outcome now | earlier outcome |
|---|---|---|
| fig1-csi-s2 | reproduced, assumed | same |
| att-csi-group | reproduced, assumed | same |
| supp-csi-per-subject | reproduced, assumed | same |
| att-passive-lower | not reproduced | same |
| att-classification | reproduced | same |
| att-weights-cortex | blocked, data_missing | same |
| game-csi | reproduced | same |
| game-mutual-negative-projection | reproduced, assumed | same |
| fig3b-state-relations | reproduced | same |
| game-classification | partially reproduced | same |
| game-weights-two-groups | blocked, data_missing | same |

**Entry steps:**
- `lock` rewrote the lock file with identical content, so the file is unchanged.
- `all` reported 0 errors. It reused the executed notebook from 11:27 UTC today and executed nothing, because nothing the run reads has changed. The notebook passed, with a runtime of 1195 s from that run.
- `handover` rebuilt `executed/zhang-2021/handover`.

No tracked file changed. I didn't verify my own work, and I didn't commit or push.
