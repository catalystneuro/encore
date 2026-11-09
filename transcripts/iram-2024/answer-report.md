There was one question. The claims file was wrong, and I changed it.

**figs4ef-assembly-not-disassembly-genes: claim changed.** I rendered the supplement's Fig. S4. Panel F shows Cfl1 lower in SRF-KO oligodendrocytes (p 0.007, DESeq2) and unchanged in OPCs, so the claim was wrong to name Cfl1 as a disassembly gene SRF does not regulate.
- **Statement:** it now says the main actin disassembly genes are largely unchanged in SRF-KO cells. Cfl1 is named as the exception: lower in SRF-KO oligodendrocytes and unchanged in OPCs.
- **Statistics:** I recorded the Cfl1 oligodendrocyte p of 0.007, with 4 samples per group.
- **Criterion:** I removed the line saying no value is printed. The claim is still marked not testable here, because the RNA-seq data are in GEO.

The answer and `answered: 2026-11-02` are in `questions/001350.yaml`.

`python tools/claims_check.py` passes the schema and every quote. It exits non-zero with 14 VALUE NOT FOUND lines, all on p-values printed only in figure panels and none from this edit. The text the checker reads has no figure panels, so I confirmed 0.007 on the rendered panel. Only `claims/001350/` and `questions/001350.yaml` are changed, and nothing is committed.
