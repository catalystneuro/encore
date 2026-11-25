I've checked and corrected `claims/powell-2021.yaml`, and I think it is ready for an attempt. Nothing was committed or pushed.

**Checker result** (after my edits): `claims/powell-2021.yaml: 22 claims, 22 quotes, 7 statistical values, 0 problems`

I also compared the file's code citations with https://github.com/marderlab/gastric at commits fa07d36 and 7a82b1f. They match: burst thresholds, the per-burst Q10, the significance test's shuffle (100 draws of each period), the area measure, the pooled phase test, the 7 to 21 C Spearman test, and the `PD_hyp.m` and slowdown script settings.

**Changes, by claim**
- **Wrong paragraph in `source`**, corrected against the paper text:
  - `fig4b-periods-decrease-all-preps`, `fig4c-q10-about-2`, `fig4c-q10-pd-lg-not-different` and `fig4s1-slowdown-after-stimulation`: that section has only two paragraphs.
  - `fig5d-lg-pd-integer-coupled`, `fig5d-dg-pd-not-coupled`, `fig5e-lg-area-exceeds-dg` and both `fig5f` claims: the quoted sentences are all in paragraph 4.
- **`fig3-evoked-7-to-21-in-9-of-10`**: removed "the evoked rhythms remained regular at high temperature" from the statement. The paper says it only of the example preparation at 23 C, and the criterion never tested it.
- **`fig2a-less-regular-at-high-temperature`**: the minimum of three periods per step is now marked as a choice made here.
- **`fig3s1-spontaneous-and-evoked-similar`**:
  - The paper gives no measure for similar spike and burst timing, so that part is now shown but not judged.
  - Added a note that `941_006`, one of the script's four spontaneous files, is not among the ten evoked preparations.
- **`fig5a-example-ratios`**:
  - "Within 0.2 of an integer" is now marked as a choice made here.
  - "PD bursts end shortly before LG bursts start" has no measure in the paper, so it is now shown but not judged.
- **`fig6b-lg-phase-locked`**: the protocol says to follow the Methods and treat the code's choices as variants, but the file treated three samples as equal readings.
  - The main result now uses the Methods sample: the first 40 burst starts per preparation and temperature.
  - The two code samples are variants: the first 50 per preparation (later code) and all starts pooled across preparations with at least 100 (archived code).
  - The p bound is now judged with its 10% tolerance.
- **`fig6e-dg-not-phase-locked`**: the criterion required every DG z to be below every LG z. The paper's own ranges would fail that (DG z goes up to 13, LG z starts at 7.5). I replaced it with a comparison of median z, marked as a choice made here, using the same samples as the LG claim.

**Still open** (recorded under `checks`)
- **LG upper z**: the reported LG z of 45 cannot occur with the Methods sample, because z is at most n = 40. The paper's number probably comes from the pooled sample in the archived code.
- **DG ranges**: the reported DG numbers contradict each other. A z of 13 gives p near 1e-6, below the reported smallest p of 0.001.
- **`fig5a` expected values**: 10.06 and 10.98 are the labels drawn in Figure 5a (from `fig_integer_coupling.m`). The text says only "~10" and "~11".

**Ready**: yes. The last `checks` entry has `ready: true`.
