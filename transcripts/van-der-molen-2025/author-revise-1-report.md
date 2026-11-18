I've addressed the round-1 report and re-run the entry with `tools/entry.py all`. Both notebooks pass (29 and 18 minutes), the two clean runs printed the same numbers, the entry check shows 0 errors, and the record matches the attempt schema. The round is recorded under `verifications` with each claim's agreement, the verifier's outcome and reason, and my response. Nothing is committed.

**Outcome changes** (now 31 reproduced, 11 partially reproduced, 7 not reproduced, 1 blocked; before, 29, 11, 5 and 5):
- **ed4d** (blocked → reproduced, resting on an assumption): the (A−B)/(A+B) normalisation can't be used on signed shuffle correlations centred on 0. The sum A+B changes sign for 8.8% of burst pairs and the ratio runs from −86,000 to 3,200. I adopted the legend's z-score.
- **supp10b** (blocked → reproduced, assumed): with the z-score and Satterthwaite t, the main effect is p 0.032 and human organoids against primary cultures p 0.031. Under the second reading of the recording length both are no longer significant (p 0.064 and 0.099), so it also rests on the code's recording lengths.
- **supp8** (blocked → reproduced, assumed): units are linked by their identical positions taken in order. Every 0 h unit links (HO3's extra 4 h unit is left out), and the criterion holds in both organoids.
- **supp27** (blocked → partially reproduced, assumed): I ported the d2 code from the figshare article the paper uses. Shuffling raises d2, Welch p 5e-38, and every intact d2 is at most 0.1. How many recordings pass the AR fit check depends on how "one order of magnitude" is read: 0/5/0/1 or 7/9/3/8, against the paper's 3/7/4/7.
- **fig5f** (partially → not reproduced): the criterion defines no partial outcome, and the comparison of state features with firing rate fails.
- **fig7b-normalized-b2b** (partially → not reproduced): the murine within-type contrast is now p 0.11, so the criterion's partial outcome no longer holds.
- **supp26** (reproduced → partially reproduced): with Satterthwaite t, primary cultures against slices is p 0.056.

**Fixes and added outputs:**
- **Duplicate bursts:** overlapping bursts are merged, keeping the higher peak. This dropped 35 bursts in 13 recordings, none in HO1 to HO4. Burst counts at 2000 ms are shown as a variant.
- **Mixed models:** they now use Satterthwaite t, as lmerTest does. I checked this against an exact balanced case (df 8, same p as a t-test).
- **Recording length:** the second reading (the shortest segment holding about 40 bursts) is now run for Figs. 6 and 7 and Supplementary Figs. 10B and 24C.
- **HMM scoring:** the surrogate is scored the same way as the real data. Real still beats surrogate in all 120 and all 40 combinations, smallest margin 0.015, with every fold printed.
- **Other outputs the verifier asked for:**
  - Burst thresholds for the murine organoids without bursts: their highest peaks reach only 3.0 to 3.7 times the RMS.
  - Okun swaps done against requested: all complete.
  - PCA on the code's own burst-only rates: HO1 non-rigid is 15.3%, still outside the expected range.
  - The majority-class chance level for fig5f.
  - Why MO13 is left out of the ed4c variant.
  - Corrected helper docstrings.
- **Record:** findings revised and one new methods question for the authors on the d2 fit check; the figshare d2 code is listed under `inputs`.

**Disagreements kept, with reasons in the record:**
- **fig1e and fig3f** stay partially reproduced, not blocked: the criterion requires every reading, so a failure under one is a partial result.
- **fig7d-murine-organoids-slices-same-lag** stays not reproduced (now assumed): the code's lag table has no zero lags, so dropping them is the best-supported reading, and the slices-against-primary-cultures contrast fails under every reading.
- **supp5** stays blocked as `methods_underspecified`, not `data_missing`: the data are public in GEO, and the protocol does not allow `data_missing` for such claims.

**Not done:**
- I added no reader questions to `questions/`, because the report names no place where the claims file misreads the paper. Its note that the paper's n counts all units is recorded in the notes; a test over all units can't be run because burst-to-burst correlations exist only for units active in bursts.
- These stay as recorded deviations: SSM (replaced by the entry's own EM), 100 shuffles (10 used), every K from 10 to 30 (11 values used), and K as a random intercept in fig5d.
