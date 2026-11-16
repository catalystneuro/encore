I've revised the attempt and re-run the entry with `python tools/entry.py all entries/scholl-2015`. It passes in 540 s with 0 check errors. The record and every conclusion match the new outputs.

**What changed in the outcomes.** The verifier's main point held up: the bucket folder `original/to_remove/` holds per-cell structs I had set aside. I now use them to test 18 of the 25 claims, on mice 8, 9 and 10, plus the PV+ cells of mouse 7 for Figure 3. The paper had 6 mice.
- **Reproduced (6):** fig3abc, fig3c, mi-per-animal, fig4ag, figs6ab, figs6cd.
- **Partially reproduced (4):** fig3-pv-lower-monocularity, fig3def, fig4d, fig4ef.
- **Not reproduced (8):** mi-dsi-relation, pv-larger-dff-low-dsi, fig4f-pv-od-spatial-decay, fig4f-od-length-constant, figs4, fig4i, fig4k, fig4jk.
- **Still blocked, `data_missing` (7):** the histology, the three CaMKIIa claims, the two neuropil-patch claims, and cell-counts-responsive. The structs hold only cells already selected (every PV+ cell in them passes the binocular index), so the counts of all identified cells can't be made.

**The assumption most outcomes rest on.** I took the undocumented `binocmonocinds` lists as the paper's visually responsive cells. Their name reads as cells responsive to binocular and monocular stimuli, nearly all their cells pass the paper's response criterion, and their totals (109 PV+, 769 PV-) are near the paper's 115 and 944. Outcomes that change under another cell set are marked `assumed: true`, and the notebook shows the paper's criterion with and without a neuropil test for every claim.

Three results lean on things worth knowing:
- **fig3-pv-lower-monocularity:** the PV+ mean is 0.452 against a limit of 0.451, which is what makes it partial.
- **Significance in two claims comes from mouse 7:** in fig3-pv-lower-monocularity and pv-larger-dff-low-dsi it depends on mouse 7's PV+ cells. That mouse has no PV- data; within mice 8 to 10 alone neither difference is significant.
- **Cell counts in the local analyses are about half the paper's or less** (for example 18 PV+ cells at 50 µm against 86), which weakens every significance test there.

**What I added or corrected.**
- **Basis for using the folder:** the header and data check now say why: the files are public, sit under the data set's own identifier, and each is identified by its S3 ETag. The stored `Ftrace` exactly equals the mask means of the published movie for the 9 cells checked (mouse 8, 205 µm). The decision no longer rests on pinning.
- **Outputs the verifier asked for:** one struct entry printed in full (each entry is one cell), the date per struct, per-mouse counts, mask sizes and centroids, and trial counts against the stim files. Also the `binocmonocinds` contents against the entries and criteria, and a check of how the stored indices are computed. The stored DSI matches the paper's formula for all 578 cells; the stored responsiveness index matches for only 279.
- **Smaller points:**
  - The clock check now also shows a 13-frame window and a per-mask window, and says the window placement is circular.
  - There is now a note on mouse 10's 4 to 5 repeats and its 125 µm plane.
  - The redundant conditional in cell 3 is removed.
- **Findings, rewritten and new:**
  - **About the data:** the per-cell data are missing from the published folder and present, unpublished and partial, in `original/to_remove/`. The structs and lists are undocumented, and the structs hold an unstated selection of cells.
  - **For the paper's authors:** a question asking how the neuropil test, the baseline and the response window were computed, and which cells the `binocmonocinds` lists hold.
- **Round 1 in the record:** recorded under `verifications`. The verifier agreed with all 25 blocked outcomes, so each entry quotes its reason and gives my reply under `response`.

**Not done.**
- No questions file: the verifier found no place where the claims file misreads the paper, and I found none either.
- I couldn't rebuild the stored per-trial responses from the traces using the paper's description; they correlate with mine at r = 0.39. This is recorded in the question to the authors.
- Untracked dotfiles (`.bashrc`, `.profile`, `.idea`, `scripts` and others) are in the repo root. I didn't create or touch them; check they aren't swept into the workflow's commit.
- Nothing is committed.
