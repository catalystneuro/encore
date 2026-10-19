No outcome changed. The verifier agreed with all 22. The entry re-ran cleanly with `python tools/entry.py all` (the notebook took 247 s), and `entry.py check` reports 0 errors. The text in the notebook and the attempt record now matches the new numbers, and round 1 is recorded under `verifications` with the verifier's reasons in its own words and my response to each.

**Changes in reply to the report**
- **Problem 1 (are the "pose error" flags real postures?):** I added a check of the flags against the MARS confidence scores. In close frames, flagged frames have lower confidence than unflagged ones (median 0.574 against 0.657, difference −0.082, interval −0.107 to −0.050). I also added a figure of eight randomly drawn flagged close frames with the keypoints drawn on the video. In each one, at least one segment visibly crosses the other mouse or the background, so these look like tracking errors. That last point is my judgement by eye on eight frames, and the notes say so. `pose-errors-close-fast` stays partially reproduced.
- **Problem 2 (bootstrap on non-contiguous frames):** the bootstrap helper now draws contiguous blocks of session time and keeps only the frames being compared. I tested it on synthetic data. The new contact intervals are −408.9 to −295.2 and −413.6 to −303.8 px, so the outcome is the same.
- **Problem 3 (order of the speed measure):** I added the other order as a variant. In fast frames, the error fraction is −0.020 at 10% and −0.011 at 20%, where the interval now includes 0. The confidence difference is +0.018. Neither outcome changes.
- **Problem 4 (patch labelled 6 px):** patches are now centred, and the smallest is a true 8 px patch (resident darker in 0.997 of frames).
- **Problem 5 (fig4b boundary case):** the verifier's figure was wrong. Annotator 1 attack is 4,517 frames, not 4,521, so it is 3.2468%, 0.047 from 3.2. It would stay within tolerance with up to 4 more attack frames, not one. The notebook now prints all the label fractions with their integer counts, and the fig4b values in the record are now given to three decimals.
- **Things it could not check:**
  - I added a per-sequence table for annotator 1's training set. The paper gives no per-sequence counts, so the table cannot show where the 10-frame gap comes from.
  - Frames are now also counted from the keypoints. The two counts agree in all 574 sequences, including the unlabelled ones.
- **Problem 8 (train/test overlap):** the duplicate-recordings finding now cites the CaltechDATA readme's statement that train and test are "split by animal identity". I checked that wording against the readme.

**Where I kept my outcome over the verifier's**
- **fig7 and fig11:** the verifier agrees both are blocked but would give `data_missing` as the reason. I kept `methods_underspecified` and recorded the disagreement:
  - fig7 depends on the blocked baseline claim (`table1-architectures`), and the protocol says such a claim is blocked for the same reason.
  - fig11's matrix is a model output that could not be produced even with the data.

  For both, the missing deposit is now listed in the notes as a second reason.

**Not done**
- Problems 6, 7 and 9 needed no change. Problem 6 was judged adequate by the verifier, and problems 7 and 9 were already findings.
- I downloaded no paper text, so nothing new went into `paper/`.
- Nothing is committed, as instructed.
