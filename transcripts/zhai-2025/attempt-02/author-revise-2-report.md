I've worked through all of the round-2 points. No outcome changed and nothing is under `proposed`. The verifier agreed with all 45 outcomes and found nothing that should change one. The last run of `python tools/entry.py all entries/zhai-2025` passed with 0 errors in 6.8 min, and the numbers are the same as before.

**What I corrected or added:**
- **fig1i-dspn-dendritic-sch-lower:** "The other eight SCH cells are within 10%" now reads "seven of the other eight", naming 2019-05-03 cell 3. I fixed it in cell 65, in the record's notes and in my round-1 response. Cell 64 now prints each cell's difference from the paper's value and the count (7 of 8). The printed difference for that cell is 10.9%, so the text says 10.9%. The verifier's 10.7% came from the rounded values, and its round-2 reason keeps its own figure.
- **README run time:** "about eight minutes" now says 7 to 13 minutes, most of it streaming the files. My runs took 6.8 to 6.9 min, and the run the verifier saw took 13.1. I set `runtime_minutes` in `entry.yaml` to 13.
- **fig2h headline:** the notes and cell 82 now lead with the per-cell median (P = 0.0044), which is the reading the record says it adopts, and give the mean second (P = 0.0031). fig4g had the same problem without being flagged, so I made it consistent: median first (P = 0.014), mean second (P = 0.0093), plus the same deviation stating the adopted reading.
- **Cell 27 (link-grab-rois):** the sentence contradicted itself. It now lists as possible causes of the gaps the missing region identifiers, the 50 um circle used here in place of the region Prairie View saved, and the one region that takes its Fmax from another region in its slice. It also says a constant background cancels in the normalised area, so the missing background images cannot explain the gaps. I checked the cancellation against the area calculation in `lid.grab_auc`.
- **Round 2 in the attempt record:** recorded under `verifications` with all 45 claims, each with `agrees: true`, the verifier's outcome, its reasons paraphrased closely from its report, and my response.

**What I left alone, and why:**
- The round-1 fig4k reason still says "17 files", because it is the verifier's own text. Its correction (16 Z-stacks plus 1 overview) is recorded in the round-2 reason.
- The README fix is not tied to any one claim, so nothing in the record's per-claim results mentions it. It appears only in this report.
- No new questions for a reader: this round reported no new place where the claims file misreads the paper.
- Nothing is committed or pushed, as instructed.
