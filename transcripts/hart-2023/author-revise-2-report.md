I've finished the round-2 revision. No outcome changed, and I proposed one change of outcome for the third round to settle. I re-ran the entry twice with `python tools/entry.py all`: all three notebooks pass, every number is the same as in the round-2 notebooks, and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes**
- **figs5c-mho-rarely-overlaps:** it stays "reproduced (assumed)", with a `proposed` change to not_reproduced. The verifier is right: the criterion requires the result "under each M2 reading". It holds under only 4 of the 8 readings at both concentration settings, because all four readings that use the ROI's maximum value fail. The notebook now prints this test as the criterion words it. The conclusion, the summary and the README state the proposed change.
- **figs4a-bilateral-symmetry:** I kept "partially reproduced" and recorded the disagreement again, in the notes and under `verifications`. The correlation part holds in every ant and the count part fails, which matches the protocol's "holds only in part".
- **The other 30 outcomes** are unchanged, and the verifier agreed with all of them.

**Corrected text and added outputs**
- **Summary of the alarm notebook:** fixed the sentence on which readings fail figs5a-sparse (aiy, aiix and aiiy fail; biix and biiy pass). It now also covers figs5a-concentration.
- **fig5d:** removed "hold by construction" from the notebook and the deviation. The notebook now prints the readings where the direction conditions fail, and the notes list them.
- **figs7a:** under the disc one trial returns after more than 100 s, and under the region ROI with return reading b two trials do. The notebook now prints this count for each reading.
- **figs7c:** the notebook now prints convergence for every fit. 23 of 24 sets converged; the ones that did not are the onset fits of reading a, with the region ROI and plane a. "All fits converged" is gone from the notes.
- **fig3fg:** dropped the explanation that leaned on round-1 numbers.
- **README:** the runtimes now match the printed values (4.1, 17.3 and 11.9 minutes), and it notes the earlier slower run.
- **Single-glomerulus claims (fig5c-s6, fig5c-6g-slow, figs7a, figs7c):** the deviations and conclusions now name the inconsistency the verifier raised. The aiiy identification uses the ROI maximum and drawing a, which the attempt sets aside elsewhere, and most of drawing a's regions are under 10 µm across. For the region ROI, 618 of 1,684 traces fell back to the disc, and the conclusions now say so. fig5c-6g-slow also notes that its PGa part passes trivially.
- **fig6:** the notes now mention the proposed change to figs5c. It is already not reproduced, so its outcome does not move.
- **Attempt record:** round 2 is recorded under `verifications` for all 32 claims, with the verifier's reasons quoted and my responses.

**Not done**
- **Drawing a:** I did not change it, and I added no new reader question. The verifier's remaining concern is that drawing a has no size floor, which is a claims-file question already in `questions/000467.yaml`. The claims are tested as the claims file states them.
