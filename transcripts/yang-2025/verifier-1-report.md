**A. Outcomes** (19 claims in the claims file: 14 tested, 5 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| tables1-network-stable-short-term | reproduced | With self-pairs included (reading d), 7/7 rats are significant and 13/14 means are within tolerance (cell 18, 1 kHz). With self-pairs excluded (reading c), only 4/7 rats are significant at the main detector, which is not even partial; 6/7 at the other onset thresholds. The outcome rests entirely on reading (d) (problem 6). |
| fig2-r1-target-shifts | reproduced | Under out−in at 1 kHz the top nodes are ANT, ANT, CA3, DG: 4 of 4 match (cell 19). Within-group agreement of the top node is 9/9, 8/10, 4/5 and 6/11. |
| figs2-target-assignment | partially_reproduced | At best 18/28 baseline groups match Figure S2 (reading a, 1 kHz or 250 Hz), and at best 24/28 stimulation labels agree, never 28 (cell 20). |
| fig3a-target-reduces-each-rat | not_reproduced | Only 3/8 target groups are below zero at the main settings, and at most 4/8 under any variant. Partial needs 6 (cell 23). |
| fig3a-nontarget-can-lengthen | reproduced | 13/20 non-target groups have a positive mean (main), and 10–14 under the variants; the criterion needs 5 or more (cell 24). |
| fig3a-per-rat-site-differences | partially_reproduced | 5 of the 11 listed pairs are significant at the main settings (Bonferroni Dunn), which meets the threshold of 5 exactly. R6 has significant pairs (DG–ANT, Bonferroni p = 0.021), and R5 and R7 have none (KW p = 0.66 and 0.33) (cell 25). The partial outcome is fragile (problem 2). |
| fig3a-target-vs-nontarget-total | not_reproduced | Target −0.020±0.028 against non-target 0.087±0.034, Mann-Whitney p = 0.085. No variant has p < 0.05, and no target mean is near −0.26 (cell 26). |
| fig3a-some-nontarget-shorten | not_reproduced | At most 3 of the 5 named groups are significant (reading c), and only 2 of 5 are less effective than the rat's target. Partial needs 3 of each (cell 27). |
| fig3b-same-site-target-vs-nontarget | not_reproduced | Each reading has at most one of DG, CA3 and ANT significant with target lower (ANT for main rel; CA3 for stimulated-only). Partial needs two. CA1 is not significant (cell 28). |
| seizure-duration-proportion | blocked (data_missing) | I confirmed this on the archive (section C). |
| fig3c-frequency-no-difference | blocked (data_missing) | Same as above. |
| fig4b-psd-target-bands | not_reproduced | 0 of 36 method×post-hoc readings hold, and alpha with gamma holds in none (cell 32). |
| fig4b-psd-other-bands-unchanged | not_reproduced | Delta KW p ranges from 4.8e-21 to 2.5e-3 across all readings, and high gamma has p < 0.05 in several (cell 33). |
| fig5b-iis-post-seizure | reproduced | Under reading (b) (paired t over 30 bins of 1 s): p = 2.1e-9, target 0.142 against non-target 0.210 /s (cell 34). Under reading (a) p = 0.0032, which is partial, and per seizure p = 0.033. The result rests on the pseudo-replicated reading (problem 7). |
| fig5c-interictal-iis-no-difference | blocked (data_missing) | I confirmed this on the archive. |
| fig5d-iis-seizure-correlation | blocked (data_missing) | I confirmed this on the archive. |
| fig6cd-interictal-hfo-no-difference | blocked (data_missing) | I confirmed this on the archive. |
| fig6e-ictal-ripples-no-difference | reproduced | Paired t-test by rat gives p = 0.26 (cell 37). This is a weak absence: the measure's magnitudes (+229% and +348%, against the paper's about −0.16 and −0.04) do not resemble the paper's (problem 9). |
| fig6f-ictal-fast-ripples-reduced | not_reproduced | Target (+4.16) is not below baseline (+2.31) under the main reading, and is below both others in none of the 8 readings; all paired p > 0.19 (cell 38). |

The paper states no chance level for any selection.

**B. Problems**

1. **[affects a conclusion] Group order against the dates (`norm_table`, cells 7, 9 and 21).**
   - R3-07 (CA1 stimulation) predates R3-06 (baseline). Archive session start dates are 2023-10-18 for R3-07 and 2023-10-22 for R3-06, and the epoch dates (10-18 to 10-20 against 10-22 to 10-23) agree.
   - R3-07 also starts the same day as R3-05 (DG stimulation).
   - `bi = index − 1` therefore normalizes R3 CA1 to a later baseline. R3-06 also contains detected trains in 3 epochs.
   - The R3 DG–CA1 pair is one of the 5 that give fig3a-per-rat-site-differences its partial outcome, which sits exactly at the threshold.
   - R3 CA1 also enters fig3a-some-nontarget-shorten and fig3b (CA1).
   - The notebook prints the overlap but neither discusses it nor tests the date-based order.
2. **[affects a conclusion] Stimulation groups with few or no detected trains (cell 11).**
   - R3-07: 0/8 epochs; R7-05: 0/7; R7-07: 0/4; R7-01: 1/12; R7-03: 1/13.
   - It is never checked whether the train detector misses these trains or whether the seizures were not stimulated.
   - The main analysis counts all of them as stimulation. R7 ANT, one of the few target groups below zero, becomes −0.07 with n = 1 when only stimulated seizures are kept.
   - Separately, 11 baseline epochs have "trains", mostly at about 125 Hz rather than the rat's usual rate. This points to false positives or mislabeled files.
3. **[affects a conclusion] The post window can include the next train (`psd_windows`, `epoch_features`).**
   - The post window is the 5 s after the first train. The 25th percentile of the detected pause is 4.75 s, so in roughly a quarter of seizures the next train starts inside the window.
   - Aliases of the about 130 Hz pulses fall in gamma (8 × 131.75 → 54 Hz), high gamma, ripple and fast-ripple bands.
   - The notebook neither excludes nor counts these cases, which bear on fig4b, fig6e and fig6f.
4. **[does not affect a conclusion] The clock check is circular (cell 11).** `detect_seizure` counts train windows as ictal, so trains overlap the detected seizure by construction. The 0.983 overlap therefore does not validate the onset and end times.
5. **[does not affect a conclusion] Pre-window length (`psd_windows`).**
   - The latency from onset to the first train has a median of 12.8 s and reaches 40.5 s, although the paper says the stimulator fires immediately on detection. The LFP onset is therefore earlier than the device's.
   - Pre windows of 0.5 to 1 s use Welch with nperseg equal to the window length, a coarser resolution than the post window's.
   - The effect is unquantified; fig4b fails under all 36 readings.
6. **[affects a conclusion] Table S1 (`pair_sets`, cell 18).** Reading (d) adds n values of r = 1 to the intra-group set. This makes intra > inter nearly automatic: R4 goes from p = 0.878 to p < 0.001. The criterion allows the reading, but the reproduced outcome rests entirely on it.
7. **[affects a conclusion] fig5b statistics (cell 34).**
   - p < 0.001 comes only from the paired t-test across 30 autocorrelated 1 s bins of grand-mean curves. Those bins are not independent samples.
   - With seizure-channels as the unit, p = 0.0032; with seizures, p = 0.033. Either would make the claim partial.
   - Per rat, target is lower than non-target in only 5 of 7 rats (not R3 or R4).
8. **[does not affect a conclusion] Figure S2 against the dandiset order (cells 9 and 20).**
   - For R5 and R6 the dandiset order differs from Figure S2, and the epoch and session dates support the dandiset order.
   - Applying Figure S2's own targets to the dandiset order gives 9 target groups (R6 ANT becomes a target). So "all 28 labels agree" cannot be reached even with perfect targets. The notebook printed the 9 but did not flag it.
   - The "baseline in Figure S2 order" variant contradicts the dates.
   - This is a data-versus-paper conflict, not a misreading in the claims file.
9. **[affects a conclusion] HFO detector parameters (`hfo_rate`).**
   - The parameters are presented as HFO App defaults without that being checked: a 5 ms line-length window, a mean + 3 or 5 SD threshold, a 6 ms minimum duration.
   - Group changes are a ratio of means, and the means run to hundreds or thousands of percent, so the measure is not the paper's. fig6e's "no difference" result therefore says little.
10. **[does not affect a conclusion] Other notes.**
    - The notebook adds variants the claims file does not name (onset thresholds 1.5 and 3, 250 Hz, end before final train, Figure S2 order). No positive outcome above depends on them alone.
    - Dunn tests are run even where KW is not significant (R5, R7); none of those reach significance anyway.
11. **[does not affect a conclusion] Synthetic tests of the helpers all passed.**
    - `cond_gc` and `cfw_onset` recover ANT→CA1 and ANT→CA3 and give ANT the highest out−in cf_w.
    - `detect_iis` keeps the larger of two peaks within 200 ms.
    - `detect_seizure` recovers a 200–250 s seizure as 199.5–250.5 s.
    - `find_trains` finds 130 Hz trains, padding each by 0.25 s on both sides. This explains the 5.5 s median train length and means real pauses are about 0.5 s longer than detected.

**C. Blocked claims on the archive, and what I could not check**

- **Blocked claims.** The archive has 56 assets. The API metadata gives only a session start date per asset, with no duration or recording-time fields. The notebook shows each asset holds only 600 s seizure-centred epochs (519 × 600000 × 4 samples).
  - There is therefore no recording time for seizure-duration-proportion and fig3c, and no interictal segments at least 1 h from a seizure for fig5c, fig5d and fig6cd.
  - The dandiset also appears to hold a selection of seizures, not all of them. For example, R2-05 has 9 seizures dated on a single day, and R4-01 has 10, whereas the paper says each group was recorded for 5 to 10 days. So per-group seizure counts cannot stand in for frequency either.
  - No part of these five claims can be tested; data_missing is right for all of them.
- **Not checkable, and the output that would allow it:**
  - Whether R3-07 and the R7 stimulation seizures were stimulated: per-group example spectrograms or comb-score traces.
  - Whether the onset and end times are plausible: example traces per rat with the detected onset, end and trains marked.
  - The share of PSD and HFO post windows that overlap a later train, and the results with those windows excluded.
  - fig3a and fig3a-per-rat with R3-07 normalized to R3-04 (the date-based order).
  - The HFO App's actual default parameters; the paper links no code.
  - VAR model checks (stability and residual whiteness) for the order of about 11 at 1 kHz.
  - The distribution of pre-window lengths for the PSD.
