**Verifier report, round 2: 000691-scherrer-2023-02**

The claims file has 23 claims, and the attempt record gives an outcome for all 23. I found no new place where the claims file misreads the paper.

## 1. The stated outcomes

I agree with all 23 outcomes in the attempt record. That includes the two I disputed in round 1.

- **fig2-quadrant-direction-decoding and ed9b-octant-decoding, blocked (not_runnable):** I now agree and withdraw my round-1 "reproduced". Both criteria judge p under (n1) and (n2). The (n2) null takes 24.6 h (quadrant nb cell 9) and 25.0 h (octant nb cell 8) against a 30-minute limit. Nine (n2) null decoders cannot show p < 0.001. The evidence still points strongly to (n2) agreeing with (n1): 0.089–0.145 against 0.437, and 0.109–0.149 against 0.326.
- **fig2k, fig2l, ed9c, blocked (not_runnable):** I agree. The measured costs (3.0 h, 2.7–2.9 h and 6.9–7.4 h on four cores) are all far over the limit.
- **ed7-motion-small, not_reproduced:** I agree, and it is no longer tentative (see section 3).
- **fig1f-kiloscope-psf, partially_reproduced:** I agree with the outcome. The printed outputs give no reading with both values within tolerance under any of the three sets of fits (cells 29–31), and the edge is wider than the centre. The record's reasons for it are wrong, though (section 2).
- **All the others:** I agree, for the reasons I gave in round 1.

## 2. Sentences the printed numbers do not support

Every number below is quoted from the conclusion or record and compared with the notebook's own printed output. These numbers appear only in the prose, never in an output. They look like they were carried over from a different run.

**fig1f-kiloscope-psf** (main nb cell 33; attempt record notes, and the response to round 1)

| Prose says | Notebook prints |
|---|---|
| Centre under (a) is "4.467 um, 0.067 um above the bound" | 4.422, 0.022 above (cell 29) |
| "4.422 um in the run reviewed in round 1 and is 4.467 um in this run" | 4.422 in this run as well |
| Mean major axis (c) centre "4.537 um" | 4.416 |
| Jacobian scaling: "15 of 118 beads' major FWHM move" | 14 of 118 (cell 30) |
| Jacobian (a) centre "3.639 um (within)" | 3.578, which is outside |
| Lower-cost fits: "4.467 and 5.892 um under (a), both outside" | 4.084 (within) and 5.892 (cell 31) |
| Lower-cost fits under (c): "4.685 and 7.944" | 4.222 (within) and 7.952 |
| The 27.77 µm bead's costs: "60.1 against 79.9" | 60.092 and 60.092 |
| "the centre lies within 0.07 um of its tolerance" | 0.022 |

The outcome survives, but the reason given for "partial" is false. With the lower-cost fits, it is the centre that is within tolerance and the edge that is not.

**fig1e-featherscope-psf** (cell 32 and record), trivial: "(c) … 6.883" is 6.884 in the output, and the minor-axis edge "5.203" is 5.202.

**Run times** (quadrant nb cells 10, 13, 16; octant nb cells 9, 12; record notes for the five decoding claims)

| Prose says | Notebook prints |
|---|---|
| "about 33.6 hours" | 24.6 h (quadrant nb cell 9) |
| "33.9 hours" | 25.0 h (octant nb cell 8) |
| "about 5.0 hours on four cores" | 3.0 h (cell 12) |
| "4.5 to 4.8 hours" | 2.7–2.9 h (cell 15) |
| "11.9 to 12.8 hours" | 6.9–7.4 h (octant nb cell 11) |

The same stale figures recur elsewhere:
- the "about 34 hours" in cell 0 of both null-(n2) notebooks;
- the "4 to 11 hours" in cell 0 of the reduced notebook;
- the README's notebook run times (7, 20, 25, 22 and 21 min), where the notebooks print 4.6, 12.3/12.4, 15.4, 15.2 and 12.4 min.

**Reduced runs** (decoding_reduced.ipynb; record notes)

- **fig2k, cell 6:** the prose says the median rises "from 0.099"; the output gives 0.101. It says p is "1.5e-6 to 6.7e-6 from 32 on"; the output gives 1.54e-6 to 7.96e-6. It says "2 to 8 (p 0.53 to 0.87)"; the output gives 0.356, 0.749 and 0.0935. It says "16 (p 0.017)"; the output gives 0.00213.
- **fig2l, cell 9:** the prose says "0.094 to 0.281 (0.187)" and "31 with (k + 1)/(n + 1)"; the output gives 0.097 to 0.282 (span 0.184), and 32 under both definitions of p.
- **ed9c, cell 12:** the prose says "0.078 to 0.203 (0.125), and 5 of 56 points are significant … so (i) holds". The output gives 0.090 to 0.197 (span 0.107) and **0 of 56 significant under both definitions, so (i) is False** (cell 11). The record's ed9c note repeats "5 of 56". The run decides no outcome, but the prose states the opposite of the result.

**Other sentences**

- **Main nb cell 23:** "ed6a … metadata_insufficient …; the others as data_missing". "The others" includes fig2d, which the record blocks as methods_underspecified.
- **Both null-(n2) notebooks, cell 0:** they run 8 decoders, "as many as fit within the time limit". Eight took 706 s and each notebook ran 15.2 min, so about twice as many would have fitted.
- **README, and main nb cells 0 and 17:**
  - They call the movie "the raw imaging video" as a fact, where the record says only that it is "consistent with" the raw video.
  - Cell 17 and the motion summary call the shifts "frame-to-frame". They are shifts against a template.

**My round-1 reasons in the record:** they are stated faithfully in my own words. The one exception is ed8, where "the midline split leaves 85 footprints" drops "of the footprints' extent". That distinction matters now that the image-midline split is added. The count of 22 of 23 claims, with none given for ed3-adc, is correct.

## 3. My round-1 points

**Resolved**

1. **Raw movie (point 1):** there are no comments and no motion-correction module. The histogram roughness is 0.740–0.745 in every block. A sub-pixel shift of 0.13 px lowers it to 0.052. The zeros are scattered single pixels. A known jitter is recovered (r = 0.996, RMS 0.033 → 0.136). The re-implementation remains a stated deviation.
2. **Null decoders (point 2):** the real single fits are now compared with the (n1) null on equal terms, and nine (n2) decoders are shown. The full (n2) null is correctly not_runnable.
3. **Analyses not run (point 3):** reduced runs are now given. I accept not_runnable as the reason.
4. **PSF fits (point 4):** the lower-cost fits are shown, with the per-bead table.
5. **ed8 (point 5):** the image-midline split is shown (86 footprints in the lower left; 8 of 8 and 7 of 8). The five off-event times are stated.
6. **Kiloscope image order (point 10):** this matters less than I said. The Featherscope stack, whose order is confirmed, also has only 71% of beads within 5 slices (cell 28), so the 72% figure says nothing about order.
7. **Fig2d, notebook header table (point 11):** fixed in the header, the summary and the README.
8. **Old verdicts in cells 28 and 34 (point 12):** no longer applicable.

Points 6–9 needed no change; point 9 is now in the notes.

**Remaining, bearing on a conclusion**

- **fig1f:** the conclusion and record must be rewritten from cells 29–31. The outcome holds, but the stated margins and the lower-cost result are wrong, and the lower-cost fits actually split the other way (centre within, edge outside).
- **ed9c:** the reduced-run statement must be corrected to 0 of 56 significant, with (i) failing. fig2k and fig2l need their reduced-run figures corrected too.
- **Costs:** every cost and run-time figure in the conclusions, the record, the README and the added notebooks' headers should be taken from the printed outputs. None of these changes an outcome.
- **Main nb cell 23:** fig2d is still described as data_missing, which contradicts the record.
