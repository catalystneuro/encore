I didn't write a claims file. The response that was writing `claims/002010/10.1101-2023.04.19.537568.yaml` was stopped by a safety classifier before the file was saved. I was told not to produce that content again, so nothing is under `claims/002010/` and the quote checker was never run.

**What I read before it stopped:**
- **Text:** `paper/10.1101-2023.04.19.537568.txt`, the bioRxiv preprint, version 1, from the JATS XML. It has the main text, Methods, figure legends and figure supplement legends. It now also includes both supplement PDFs: the supplementary figures (media-1) and Supplementary Tables S1 to S18 (media-2). Those tables were missing in the earlier run, and they hold the statistics for nearly every finding. There is still no PDF of the main text.
- **Code:** the two SourceForge projects the paper links, with files dated 2023-04-14. SourceForge shows no commit for them, so I recorded checksums instead.
  - `gait-analysis-gui` is MATLAB. It scores footfalls on the video and turns them into stride metrics, using 119.88 fps and skipping trials with fewer than 3 strides in any limb. It exports these for GraphPad. Two functions it calls, `calcSpeed` and `calcTimeCoupling`, are not in the archive.
  - `gait-emg-step-trigger` is a Spike2 script that fires optogenetic pulses when it detects a TA EMG burst.
  - Neither project contains the statistics, the Z-scores or the curve fits.

**Still missing from the paper:**
- **The Z-score equation.** In the Methods, section (a), the sentence ends "calculated as follows:" and no formula follows. Every subgroup in the paper is defined by Z SwT or Z StrV. I had planned to name two readings: Z = (the mouse's change − the WT mean change) / the WT SD, with the change taken either as CNO minus saline or as a relative change. Whether to pool strides across sessions or average session means is also open.
- **The regression models behind the walking-signature F-tests.** The paper only cites its reference 36. The degrees of freedom in Tables S3, S8 and S12 imply a 2-parameter model for most metrics and a 4-parameter model for stance time. I had planned to name linear, power and semilog readings for the first, and polynomial or logistic readings for the second.

**Counts:** 0 claims, so none with quotes, statistics or criteria.

To get the file written, someone needs to start a new claims run, which could reuse the reading above. Alternatively, a person can write the file.
