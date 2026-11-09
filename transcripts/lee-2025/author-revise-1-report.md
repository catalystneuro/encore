I've revised the attempt and re-run the entry with `python tools/entry.py all entries/001195-lee-2025`. It passes in 22 minutes, and `check` reports 0 errors. The round-1 verification is recorded under `verifications` for all 38 claims. Nothing is committed.

**Outcome changes** (now 5 reproduced, 6 partially reproduced, 1 not reproduced, 26 blocked):
- **fig6j** (EPSP amplitude by region): reproduced → partially reproduced, as the verifier gave, and the assumption is dropped. With the new sweep selection, only one of the criterion's four readings is significant, and narrowly (3 SD, mix cells included, p = 0.049). Both readings pass at 5 SD.
- **fig6k** (IPSP trough by region): not reproduced → partially reproduced, resting on an assumption. The verifier had agreed with "not reproduced", so round 2 should look at this one. At 3 SD the ANOVA now gives p = 0.0021 and CeA against BLP p = 0.0031. I adopted 3 SD because 2 SD finds an IPSP in 67% of windows with no light. The test has 58 cells against the paper's 34.
- **fig6no** (CeA clusters): kept as partially reproduced; the verifier says not reproduced, and I recorded the disagreement. 11 to 13 of the 17 or 18 late-firing cells are excited and 2 or 3 are inhibited (now named per cell). The other half of the criterion holds.
- **fig7-s1ef** (red against blue light): still reproduced, but now marked as resting on the assumption that the "+0.3mW blue" and "+0.2mW blue" sweeps had no red pulses.

**What I added or corrected:**
- **Threshold check:** the EPSP/IPSP detection now also runs in a window with no light, 12 s after the pulses. At 2, 3 and 5 SD it finds an EPSP in 94, 80 and 40% of cells and an IPSP in 67, 30 and 5%. fig6df rests on the difference between these and the light window. 5 SD labels are shown as a variant for all the clustering claims.
- **Rest sweeps:**
  - 148 rest sweeps (in 28 cells) fire before the light; they are now left out, since the Methods say cells at rest were held below threshold.
  - P10's 51 broken sweeps (0 mV, impossible injected current) are left out per sweep. Its other sweeps are normal, so the cell stays in.
  - A table now compares the holding current each description names with the one measured.
- **Sex of the mice:** the verifier suggested dropping the 17 cells from mice labelled female. Without them only 25 BLP cells have current steps, fewer than the 27 the paper clusters, so I kept them and reran every claim on male mice only as a variant. Under that variant, fig6-s1jk no longer holds and fig6j passes at 2 and 3 SD.
- **Fragile BLP clustering:** while preparing, a version that dropped P10 entirely split the BLP cells 12/15 and fig6-s1i failed. The notes say so; that version is not in the notebook.
- **Other data checks:**
  - The ChrimsonR red, blue and red-during-blue sweeps all start at the assumed light time.
  - None of the files' text fields mentions TTX or 4-AP; I also corrected the markdown that claimed more fields had been searched.
  - One frame from each of the 41 behaviour videos is shown: the mouse and both cups are visible, but the cups are covered.
- **Combined clustering:** the notebook now draws the combined dendrogram with region and response under each leaf.
- **New findings in the record:**
  - the female labels;
  - descriptions that disagree with the measured holding current;
  - the ambiguous blue-light sweep descriptions;
  - duplicate-looking subject ids (17 mice rather than 20 if they are the same).
- **Capacitance:** I noted in the helper's docstring that the capacitance estimate reads low.

**Question for a reader:** I rendered Figure 6 supplement 1N from the PDF. It appears to show the excited combined cluster differing between CeA and BLP, which is what this attempt finds. I added this to `questions/001195.yaml` for fig6-s1ln and left that claim as not reproduced under the criterion as written. The figure's pattern, run as a variant, holds at 2 and 3 SD.

**Not done:**
- I did not track side times from the behaviour videos for fig7e. The paper's pose model isn't published and nothing records which cup held the juvenile.
- I did not run the CellReg co-registration for fig7i, since without the response classes it does not test the overlap the claim is about.

Both reasons are in the notes.
