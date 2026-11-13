**Verifier report, round 2: Zandvakili & Kohn (2015) on CRCNS v1v2-1**

The claims file has 26 claims, and the attempt record gives an outcome for each: 5 reproduced, 6 not_reproduced, 2 partially_reproduced and 13 blocked. The notebook tests 13 claims and blocks 13. My round-1 count of "14 tested, 12 blocked" was wrong. I found no new place where the claims file misreads the paper. Its statement that some penetrations targeted middle-layer sites matches Experimental Procedures, Physiology.

**1. Outcomes**

| claim | record | agree? | note |
|---|---|---|---|
| fig4c-broad-ccg-peaks | reproduced | yes | 31 of 31 under both readings (cell 11). |
| fig4c-narrow-peak-sites | not_reproduced | yes | 0.516 against 0.206 ± 0.021 (cell 8). |
| fig4-narrow-peak-depth | blocked, data_missing | yes | The only fields are spikeRasters, stim, trialId, unitCodes and rfInfo (cell 5). |
| fig5a-rf-alignment | blocked, metadata_insufficient | yes | |
| fig5-narrow-pairs-rare | not_reproduced | yes | 0.0105 (cell 15). |
| fig5b-v1v2-latency | not_reproduced | yes | Median 2.0 ms (cell 18). |
| fig5b-intra-areal-zero-lag | partially_reproduced (`assumed: true`) | the label yes, the basis no | See below. |
| figs3-efficacy | not_reproduced | yes | 0.324% and 0.496% (cell 24). |
| fig6a-coordination-before-v2 | reproduced | yes | 6 of 6 windows under every reading and both p readings (cell 30). |
| fig7a-threefold | not_reproduced | yes | Only e-b3 with the median summary (2.011) reaches the range, and e-b3 is a stand-in. |
| fig7a-above-shuffle | reproduced | yes, but fragile | Rests on realization 0. Realization 3 of (a,c) and realization 2 of (a,d) give 4 of 5 windows, which the criterion would call partial (cell 40). The record says this. |
| fig6b-not-after-v2 | not_reproduced | yes | p-b < 0.05 at 80 ms in every reading (cell 43). |
| fig6-slow-both-sides | reproduced | yes | |
| fig7d-time-course | partially_reproduced | yes | The peak is 2.5 to 3.5 ms before the spike in all 10 cells of every method. Under p-b there are significant after-spike epochs at 80 ms, and also at 40 ms in d-b (cell 49). |
| figs4-partner-not-needed | reproduced | yes, with a caveat | Under e-b2 with p-b, the subset without a partner is above control at 2 of 5 windows. That is not a majority, so this one combination fails the criterion (cell 52). The record gives "2 in e-b2" but does not name it as a combination that fails. It is a stand-in reading, so the outcome holds, consistent with how fig7a treats e-b3. |
| fig7b, fig7e, fig7c, figs2a, figs2b, figs5 | blocked, data_missing | yes | |
| rf-sizes | blocked, metadata_insufficient | yes | |
| fig1, fig3, figs1, fig8 | blocked, other (not attempted) | yes | |

**The one assumption (fig5b-intra-areal-zero-lag)** is stated: the paper's test is taken to be the Wilcoxon signed-rank test. It is plausible but cannot be checked, since the paper's p = 0.45 and 0.42 cannot tell the two tests apart.

The outcome does not follow from the assumption. The criterion has only "reproduced when no difference in both areas" and defines no partial outcome. Under the assumed Wilcoxon test, V1-V1 differs (p = 0.016), so the outcome would be not_reproduced. That is the same rule the record now applies to fig5b-v1v2-latency and fig7a-threefold.

My round-1 basis for partially_reproduced was different: the two readings disagree, with the sign test matching in both areas and Wilcoxon failing for V1-V1. The record says "as the verifier gave it" but gives "one of two areas holds" as the reason. I recommend one of two fixes:
- Drop the assumption and justify the label by the readings disagreeing.
- Keep the assumption and record not_reproduced.

**2. Sentences the numbers do not support**

- Cell 55, Summary: "Narrow V1-V2 peaks are found at about half of the sites, against a fifth in the paper, so the deposited sessions are a selection the documentation does not describe." The record's selection_undocumented finding says the same: "They differ from the paper's sample in a measure the paper reports."
  - The numbers show that this attempt's measure differs. They do not show that the cause is the sample and not the method (1 ms bins, no SNR filter, the jitter implementation).
  - An excess in every session (cell 8) fits either cause.
  - Cell 16's "consistent with" is acceptable. The causal "so" and "differ from the paper's sample" go further than the data.
- Cells 35 and 44, the attempt record's notes for fig6b-not-after-v2 and fig7d-time-course, and the bootstrap finding all say p-a is "near its nominal level."
  - Cell 34 shows 13 of 150 epochs below 0.05 against 7.5 expected. The binomial tail is P ≈ 0.04, ignoring the dependence between epochs. At the 5 ms window it is 5 of 30.
  - So p-a runs somewhat above its nominal rate at 0.05. At the Bonferroni threshold it gives 0 of 150.
  - Cell 44 supports calibration with four null p-values (0.98, 0.29, 0.65, 0.10), and four values cannot show it.
  - A better support is already printed: the largest null |difference| (4.5e-5 at 40 ms, 5.2e-5 at 80 ms) is well below the observed after-spike differences (1.2e-4 and 2.7e-4). No outcome changes, because p-b alone decides fig6b and fig7d.
- Attempt record, fig6b-not-after-v2 notes: "At 5 to 20 ms the ratios are 1.03 to 1.08 (p-a 0.10 to 0.48)." This holds for the main reading only. In other readings s-b has 0.959 at 10 ms, and d-b has p-a = 0.024 at 20 ms (cell 43). Cell 44 does say "main".
- README: "Non-middle-layer, offset-RF, single-unit and V2 relay analyses (seven claims)." That row covers 6 claims. fig4-narrow-peak-depth has its own row, so the table adds up to 27 claims.
- README: "about 27 minutes". Cell 56 prints 1530 s, about 25.5 minutes.

I checked every other "**Result:**" sentence, the rest of the Summary, and the notes in the record against the printed outputs, and they match. That includes:
- the per-session and per-animal counts;
- the shuffle-realization values 2.073e-4 and 2.038e-4 and the SD of about 1e-5;
- the fig7d epoch lists and the 2.7e-4 against 8.3e-4 comparison;
- the figs4 ratios;
- the rf-sizes values;
- the permutation check (0.0121 against a largest permuted value of 0.0119).

**Round-1 reasons in the record:** all 11 points and section C are carried in my wording and attached to the right claims. The one misstatement is the basis for fig5b-intra described above.

**3. Status of round-1 points**

Resolved:
- 1: the simulation claims are now blocked as other (not attempted).
- 2: the null check was run. The wording caveat above remains.
- 3: the ordering and same-tetrode sensitivity are reported.
- 4: the 1 ms smear is stated.
- 5: the 3.54 ms smoothing floor and "2 ms or more" are stated.
- 6: the other readings are run for fig7d and figs4, and the 2000 draws are justified.
- 7: epochs are now counted as after only when wholly after the spike.
- 8: shuffle spread is shown.
- 9: stated, and I accept it.
- 10: partly. A permutation check was added, with a thin margin (0.0121 against 0.0119). It is for information only.
- Section C: the fields, calibration, shuffle spread and other-reading requests are met.

Open, and bearing on a conclusion:
- fig5b-intra-areal-zero-lag: the outcome is inconsistent with its stated assumption and with the criterion. Choose one of the two fixes in section 1.
- Point 11 and the selection finding: an excess in every session does not separate sampling from method. The Summary and the finding should say the difference may come from either.
- figs4-partner-not-needed: name e-b2 with p-b as a combination that does not meet the criterion.

Open, not bearing on a conclusion:
- The "near nominal" wording for p-a.
- The README claim count and run time.
- The "main" qualifier in the fig6b notes.
- I still have not reviewed the rendered figures.
