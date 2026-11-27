I've revised the attempt in reply to the round-1 report. The entry passes its checks and the clean re-run passes (about 2 minutes). Nothing is committed.

**Outcomes that changed** (round 1, so changes were allowed):
- **fig6cd-hardness-fast-merge: blocked → reproduced.** The verifier asked for every attribute of a 0.8/1.4% file to be printed, and that showed an `Agarose_Percentage` series in all four agarose groups, which the first version never read. With it, the 0.8% and 1.4% curves merge at 20 s, and at 20 or 25 s with 200 mM on both sides. That is within 25 s under every reading.
- **fig6g-more-time-softer: blocked → reproduced.** Flies spend a median 0.609 of all time on 0.8%, and 0.672 of search time.
- **fig6b-softer-preferred: still blocked, but now for `data_missing`.** Four of the six Fig. 6B conditions are not in the dandiset, including bar 6, which the criterion needs. (An earlier progress note of mine said three; it is four.) The first bar is shown for information: 0.800 of eggs on 0.8%.
- **fig3e-rate-after-long-absence: reproduced → partially reproduced, marked as resting on an assumption.** The rate after long absences is clearly higher, but the "no rising trend below 240 s" part holds on only one reading:
  - the 150 to 240 s bin is already high (p = 0.0014);
  - the trend over the bins from 5 s is significant (p = 0.029);
  - with sub-second visits merged, the trend over all bins is significant (p = 0.009).
- **fig5ab-strains-release-faster and figs2-search-definition-robust: outcomes unchanged, now marked as resting on an assumption.** I adopted one trial per visit for the bin test, citing the Methods' "each substrate transition within a search are independent". With one trial per search, figs2 would be reproduced, and the notebook shows that.
- **figs4-models-fail: kept as reproduced; the verifier said partially reproduced.** I added the non-negative (log-link) fit it asked for. It follows the 0/200 curves inside the 90% CI in 4 of 7 bins and still overestimates the 500 to 0 mM rate in 7 of 7. Model 2 cannot be fit because the paper gives neither its equations nor its constants. The disagreement is recorded under `verifications`.

**What I added or corrected:**
- **Boundary flicker (fig3d):** the visit-length distribution is printed, and the claim is rerun with short visits merged. The medians stay outside tolerance (48.5, 57.0 and 441.5 s), so fig3d stays partially reproduced. The cell also shows why the claim's two readings of "within 10 s" give the same frame.
- **Short egg intervals:** the 48 pairs under 10 s are listed. Ten eggs fall in the last 19 s of two Dop1R2-mutant-1 recordings while the flies are walking, and are probably not real eggs. That is a new minor finding at the end of the list; it changes no outcome.
- **Finding 1** wrongly said the agarose files hold no hardness label. It is rewritten in place, as `other` with severity `none`, so the finding numbers still point at the same findings.
- **Other output the verifier asked for:**
  - a note that pause times come in 0.5-s steps, so the claims file's 10% and 20% bounds are one frame;
  - the merges in fig2-earlier that rest on bins with almost no eggs;
  - the size of the search-window overlap (1.6%);
  - fig7df counted over all search frames;
  - Holm and Benjamini-Hochberg corrections for fig5c;
  - an explicit verdict for fig7cf;
  - fig8fg with 30-, 60- and 120-s windows, plus per-mutant speed traces;
  - the criteria applied in the fig4e, fig4f, fig6ef and fig8fg cells.
- **Reader questions:** a new `questions/vijayan-2022.yaml` puts the two places the verifier said the claims file may misread the paper (fig7ik's "unrelated to the number of eggs", and fig5c's test of every bin without a multiple-testing correction) to a reader. Neither claim was changed.
- **The record:** round 1 is recorded under `verifications` for all 45 claims. The notebook text, README and entry.yaml are updated to match the new numbers.

**Not done, and why:**
- Model 2 of fig. S4 is not fit, because the paper gives neither its equations nor its constants.
- No critical findings exist, so there were no finding reviews to record.
- The runner URL in `provenance` still points at the first run, because I don't know this run's address.
