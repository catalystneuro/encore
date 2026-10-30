I've revised the attempt for every point in the round-1 report. One outcome changed, a second one I kept against the verifier's view, and the record now has the round under `verifications`. The final `python tools/entry.py all` run passed with 0 check errors (the notebook takes 712 s), and the handover was rebuilt. Nothing is committed.

**Outcome changes**
- **spontaneous-periods: changed from reproduced to partially_reproduced**, as the verifier gave. The notebook now compares the four range bounds with the expected values. Every scan still falls inside the widened ranges. But over the 14 scans the longest wait before the stimulus is 4.841 min, outside 5.5 ± 0.55 min. Over all 19 files the four bounds match the paper's.
- **monet2-directions: kept as reproduced, with the verifier's disagreement recorded.** I replaced the direction measure, so round 2 should look at this one.
  - The old phase-correlation measure snaps small frame shifts to whole pixels, which bends directions towards the axes and diagonals. The new measure is global optical flow (the Lucas–Kanade gradient method).
  - With it, all 560 trials have 16 distinct directions, both by the 10° rule and on the 22.5° grid. All directions lie within 7.9° of the grid, 99% within 5.0°.
  - The notebook prints both measures for seed 7637 (scan 5-6) and seed 6154 (scan 9-6). Under optical flow both hit all 16 grid directions. The period that phase correlation read as 124.9° measures 111.3°, next to the grid direction 112.5° that was missing.
  - The old results stay alongside for comparison: 556 and 554 of 560 trials with 16 directions.

All other outcomes are unchanged.

**Added or corrected**
- **fig3f-oracle-reliability:** I added the scores of the artifact masks alone, of each field's mean trace, and of each mask with its fit on that mean trace removed. The verifier's concern holds: artifact masks score as high as somata (0.235/0.402/0.650 against 0.208/0.396/0.702). The field mean scores 0.499, and removing it barely changes either group. The notes now say the score on fluorescence does not separate neural reliability from this shared signal.
- **fig3g-direction-tuning:** I added a reference from the data with no tuning in it (the difference between the two halves of the trials). It puts 6,153 to 8,217 units on each direction, so the "at least 5 per direction" count tests little. The conclusion now rests on the split-half check. Counts with the new directions are 5,205 (reading a) and 5,084 (reading b).
- **ed4-matched-higher-signal-correlation:** the partial test the verifier asked for now runs as a variant on the dataset's own EM matches, under the same-field reading of "nearest". The claim stays blocked with manual-coreg-19181.
  - In 538 pairs, the matched signal correlation exceeds both controls in 71.9%, and in 77.7% when both oracle scores are above 0.2.
  - Wilcoxon p is below 1e-43 throughout.
- **New finding (format error):** `pt_root_id` is stored as a 64-bit float, which cannot hold every 18-digit root id exactly. In 50 of the 538 pairs, the two masks' EM cell body points are more than 10 µm apart. Root id 0, which means no segment, is now excluded, which gives 395 shared root ids where the record had 396.
- **Other outputs the verifier asked for:**
  - every group in the files;
  - all eye and pupil series of scan 4-7 (three, all ending at 5,392.9 s);
  - a table of fields by depth (exactly two fields at every depth in all 19 files);
  - a count of stimulus trials starting inside an oracle repeat (0), in place of the check that was true by construction.
- **Removed:** the unsourced statement that the paper's matches span the whole field of view.
- **Blocked claim notes:** they now name what BossDB serves without a token: the synapse exports for versions 1078, 1181 and 1300, and a connection table with nucleus ids for 1300. They also say why that is not enough. The claims need tables that pick their neurons or matches, which are only in CAVE. BossDB's proofreading table is a 600-row release from 2021. cell-classification notes that 82,247 = 69,957 + 12,290.
- **Question for a reader:** the verifier reported no misreading of the paper. While checking the BossDB bucket I found a structural stack of this mouse, and the paper lists 2P structural images among its public data. So I added `questions/000402.yaml`, asking whether structural-stack, z-drift-under-10um and unique-neurons-75909 should be marked as data held elsewhere. Those claims stay blocked as `data_missing` until a reader answers.

**Not done**
- I did not test any claim on the BossDB stack or synapse exports. The claims file limits the stack claims to the dandiset. The EM claims need selection or match tables that only CAVE serves with a token, and counting the 20 GB synapse export already stalled in the first run.
- I can't print Extended Data Table 1's cells from the data; they stay cited from the table's image in the published paper.
- area-split-half-visp stays blocked as `metadata_insufficient`, where the verifier said `data_missing`. The outcome (blocked) is the same; the difference is recorded.
