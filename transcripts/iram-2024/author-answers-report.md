One question was answered, and it changed the outcome of one claim, `figs4ef-assembly-not-disassembly-genes`, from partially reproduced to reproduced, resting on an assumption. The data and numbers are the same as before; the claim's wording changed. Both notebooks pass `python tools/entry.py all entries/001350-iram-2024` (110 s and 820 s), and the handover is built in `executed/001350-iram-2024/handover/`. I committed and pushed nothing, and did not verify my own work.

## The question and what the answer changed

- **The question:** the claim said SRF does not regulate the main actin disassembly genes "such as Cfl1". But the paper's own Fig. S4F shows Cfl1 lower in SRF-KO oligodendrocytes (p 0.007), and the GEO counts agree.
- **The answer:** the reader agreed the claims file had misread the panels and amended the claim. It now says the disassembly genes are largely unchanged in SRF-KO cells, with Cfl1 the exception: lower in KO oligodendrocytes and unchanged in OPCs. Under statistics it records Cfl1's p of 0.007 (4 and 4 samples).

## Outcome

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| figs4ef-assembly-not-disassembly-genes | partially reproduced (Cfl1 lower in KO oligodendrocytes went against "not ... such as Cfl1") | reproduced, resting on an assumption |

The result is the same under all three DESeq2 readings:
- **Other disassembly genes:** none of the 12 genes of Fig. S4E other than Cfl1 reaches padj < 0.05 in oligodendrocytes. In OPCs, none of the 12 or 13 genes tested does.
- **Cfl1:** it is lower in KO oligodendrocytes (log2FC -0.78, p 0.0003, padj 0.024 in reading a; padj 0.029 in b and 0.0016 in c), where Fig. S4F prints p 0.007. It is unchanged in OPCs (log2FC -0.05, padj 0.91).
- **Actin:** Actb is lower in KO in both stages under readings a and b.

The outcome rests on an assumption because one part depends on the model. If all 15 samples go into one joint model (reading c), Actb is no longer significantly lower in OPCs (padj 0.51). So the "actin itself included" part holds in OPCs only under the per-stage model, the one already adopted for `fig4ab-rnaseq-degs`. That is now a deviation, and the outcome carries `assumed: true`.

## What I updated

- **Notebook (`geo_sequencing_claims.ipynb`):**
  - The section quotes the amended claim and says what the answer changed.
  - It now tests each part separately: the other disassembly genes, Cfl1 in each stage against the paper's p of 0.007, and the actin genes.
  - The paper's padj < 0.05 threshold is cited from the Results and the Figure 4A legend.
  - The conclusion and the summary row are rewritten.
- **Attempt record (`attempts/001350-iram-2024-01.yaml`):**
  - The claim's outcome, notes (including the earlier outcome and why it changed) and deviations are updated.
  - The `paper_inconsistency` finding is reworded: the Results name no exception, while Fig. S4F shows Cfl1 lower.
  - The runner URL now points to this run.
- **Entry files:** the README table row is updated. The notebook's runtime in `entry.yaml` (and the README's description of it) goes from 12 to 17 minutes, because the first run here took 1018 s while waiting on GEO.

The README still carries the "failure to reproduce" sentence, because `fig3d-shared-carg-targets` is still partially reproduced. No other claim was affected by the answer.
