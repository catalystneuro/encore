No outcome changed. The verifier agreed with all 20 in round 2, and I found nothing that called for a `proposed` change. The record still has 6 reproduced, 5 partially reproduced and 9 blocked (methods underspecified).

**Corrected, following the report:**
- **Main notebook, cell 21:** it named a notebook that doesn't exist and said "11 labels". It now names `responsive_zeta_cuts.ipynb` and `responsive_zeta_labels.ipynb`, says they cover 9 labels, and says Tom Faces and Summer Faces are not run because no responsive-unit claim uses them.
- **Main notebook, cell 65:** "no larger for camera cuts than for Summer" is now "about the same" (drops of 0.062 and 0.060).
- **"Calibrated" for the ZETA test:** this appeared in main notebook cells 22, 31 and the summary, in both ZETA notebooks' conclusions, and in the record's notes for fig2b-phc-camera-cuts and tables1-few-semantic-responses. It now reads "not anticonservative" (camera and scene cuts) or "conservative" (the other labels), and the ZETA counts are described as lower bounds.
- **README:**
  - The "about 70% at random times" line now gives 68.4% with as many events as camera cuts and 9.5 to 55.5% with as many as each other label's onsets.
  - "Far fewer units than the paper" now holds only for camera cuts, scene cuts, Summer and Tom. For Outdoor, Indoor and McKenzie, ZETA counts a few more units than the paper.
- **Run times:** updated in the README and notebook headers from this run: main 22 min, top-ranked 8 min, ZETA 15 and 10 min.

**Re-run:** `python tools/entry.py all entries/001616-gerken-2025` passed all four notebooks with 0 check errors. I checked every number cited in the conclusions against the new outputs and none moved, so no conclusion needed new numbers. `tools/entry.py check` also passes after the record update.

**Recorded:** round 2 is now under `verifications`, with the verifier's reasons for each claim and my response.

**Not done:**
- I did not run ZETA with 1000 resamplings for every unit and label (still 100 apart from PHC scene cuts). The verifier listed this as partly resolved, but it changes no outcome, and it was too slow for all units in round 1.
- The mapping from subject ids to the paper's patient numbers is still unconfirmed, because the Figure 4 image could not be retrieved. fig4-named-patients keeps resting on that assumption, as its notes say.

Separately, untracked files that I did not create have appeared at the repo root (`.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.mcp.json`, `scripts`, and others). I left them alone; you may want to keep them out of the workflow's commit.
