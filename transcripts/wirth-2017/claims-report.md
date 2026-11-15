I stopped before writing any claims, so `claims/wirth-2017.yaml` is unchanged. The protocol (Reader, step 1) and your instructions both say to stop when a supplement the results rest on is missing, and one is.

**Text read.** `paper/10.1371-journal.pbio.2001045.txt` is the version of record (PMC5328243, Europe PMC JATS XML). It has the Results, Discussion, Materials and Methods, the legends of Figs 1 to 7 and S1 to S7 Figs, and the movie legends. No PDF was provided, and the paper links no code repository.

**What is missing:**
- **S1 Appendix** (DOCX, sections A1 to A5). It is not under `paper/` (the manifest lists 0 supplements for this paper). The Results rest on it:
  - **A2** holds the method of the two gaze findings, with their Wilcoxon p < 0.001: gaze anticipates the next joystick action, and gaze anticipates where landmarks will appear. The Results (500 ms) and the S2 Fig legend (300 ms) disagree on the window, and only A2 can settle it.
  - **A3** holds the recording methods and the cell selection behind the 189 cells. Every neural claim uses those cells.
  - **A5** is itself a result: the control showing that space dimensionality does not explain the higher information content in the state space (S7 Fig).
  - **A1** (the gaze density maps) and **A4** (population averages) hold the methods behind the gaze density result and the population-average maps (S5B and S6 Figs).
- **S2 Appendix** describes the CRCNS files and Matlab scripts. It is not needed for any finding.
- **The reference list** is cut off in the stored text, so reference 60, the learning-curve method behind the learning and probe-session claims, cannot be identified.

The last check of the existing file already flagged this: "Supplying S1 Appendix would settle them."

**How the existing file falls short of the current protocol** (to fix once S1 Appendix is supplied):
- It names a single dataset (`dataset: crcns hc-21`) and its claims have no `datasets:` field. The paper is tested on both `crcns-hc-21` and `crcns-hc-12`, and each claim needs to name the ones it rests on.
- The hc-12 descriptor says that dataset holds the paper's 189 cells, the full set analysed. hc-21 has 101 cells, with a familiar-maze condition the paper does not describe. The opening comment should say this.
- The four claims that depend on S1 Appendix (the two gaze claims, `dimensionality-control` and `fields-per-cell`) still have methods the paper's text does not fix.
- The provenance date needs updating.

**Counts:** no claims written. The existing file holds 37 claims (id lines counted); I did not count its quotes, statistics or criteria in this run.

**To unblock:** add S1 Appendix (and ideally the PDF, for reference 60) to the paper store and re-run the reader.
