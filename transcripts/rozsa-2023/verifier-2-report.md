**Verifier report, round 2: Rozsa et al. 2023 on DANDI:000341 0.241220.1312**

The claims file has 31 claims and the attempt record gives 31 outcomes: 15 blocked, 9 not_reproduced, 4 partially_reproduced and 3 reproduced. Five outcomes are marked `assumed: true`. Cell references are `ind[n]` (induction notebook), `sl[n]` (slices notebook) and `iv[n]` (in vivo notebook).

### 1. Outcomes

I agree with 30 of the 31 outcomes. I do not agree with fig2e-sag-raf-smaller as it stands.

- **fig2e-sag-raf-smaller** (partially_reproduced, assumed): **I do not agree yet.**
  - In ind[29], the comparison does not filter on `tested`. Cells that have no induction sweeps are therefore counted as "without RAF".
  - Rat has 132 files, 118 tested and 129 with sag. Under the assumed reading, 34 rat cells are "without RAF", but only 118 − 97 = 21 of them are tested cells. That leaves about 13 untested cells in the group.
  - Under the interstimulus reading the human "without RAF" group is 12 cells, but only 6 tested cells lack RAF.
  - The criterion takes RAF status "as in fig1d", where the denominator is tested cells.
  - The partial outcome rests on the rat result alone (P = 2.8e-05). That result is already fragile: P = 0.0020 on the drug-free files and P = 0.0021 at the step nearest −90 mV. It needs to be rerun on tested cells only.
  - The assumption itself (RAF status from the continuous recording) is stated and reasonable. Part of its rationale does not hold, though; see section 2.
- **fig3l, fig3k, fig3m-rat-ais-phase-coupling, fig3m-rat-ra-no-phase** (all assumed, resting on reading (b)): I agree under the stated assumption, which is an allowed reading and is stated. The rat mixture passes the slope check, but it labels 14161 of 18779 APs as RA, while the paper counts 76 RA-APs against 534 AIS-APs (sl[31]). The human and in vivo claims were blocked because the mixture's classes "are not the paper's". The rat classes are not the paper's either, by proportion, so the two decisions use different standards. The fig3m population assumption (no drugs beyond carbachol and SCH23390) is stated and reasonable.
- **fig3-human-ap-states, fig3f, and the 8 in vivo claims** (blocked, methods_underspecified): I agree. This is a judgement, and it is the check I asked for in round 1 (problem 4). The record should say that the claims file's reading (b) does not include this check. Applied mechanically, reading (b) would give mixed outcomes: fig4-invivo-up-down-balance would be reproduced (iv[29]), and fig4i and figs4i partially reproduced. This is a gap in the claims file. It does not misread the paper.
- **fig2h** (partially_reproduced): I agree under the criterion's mechanical rule. As the notes say, the result rests on sweeps whose sag peak lies below −150 mV.
- **fig1d and figs1b** (not_reproduced): I agree. The folders are an undocumented selection, which the record reports as a finding.
- **The rest**: I agree with fig1ab, fig1c, fig1f, fig1g, figs1d, fig1hk, fig2c, figs2, fig2e-sag-species, fig2il, fig3i, figs3 and figs5.

### 2. Sentences the printed outputs do not support

- **ind[30], and the record's fig2e-sag-raf-smaller deviation:** "induction stops once APs appear between the pulses, so the interstimulus APs mark nearly every induced cell (0.980 …)". Stopping induction when interstimulus APs appear does not imply that nearly every cell has them; the paper has 87 of 385 cells with RAF. The 0.980 comes from this dataset (ind[20]). The record's findings and the ind[31] summary use the same 0.980 as evidence of an undocumented selection, so the two uses contradict each other.
- **sl[19], the sl[51] summary, the fig1hk notes and the finding:** "Somatic thresholds lie at -30 to -11 mV in every file". These are per-file medians, from −30.4 to −11.2 mV (sl[17]). The RA-class APs have median thresholds of −60.6 mV (220504) and −69.6 mV (220616) (sl[18]).
- **sl[51]:** "In the rat active slices and the bleb recordings its RA component has the lower threshold and slope". In the rat bleb recordings the RA class has the steeper slope (2.78 to 4.68 against 1.14 to 1.32 mV/ms, sl[18]). Only the human bleb mixture passes the check.
- **sl[51], the fig3m notes and the iv[37] summary:** "The Vm and LFP series share their starting times". This is printed for 3 of 39 rat files (sl[7]) and 3 of 245 in vivo files (iv[7]) only. In the rat files, the 1 s correlation at lag 0 is still no better than at shifted lags (mean −0.046, sl[7]), and the 9 of 16 recordings with |z| > 2 have mixed signs. The in vivo check is strong (143 of 167, median z −10.4).
- **Record, fig3m-rat-ais-phase-coupling:** "256 and 251 degrees". Order 4 gives 255° (sl[44]).
- **Record, fig1c:** "Rat gives the same direction". This holds pooled, but at 100 kHz the rat RA-AP threshold is higher (−41.69 against −42.48 mV, ind[17]).
- **README and the in vivo notes:** "about 41 minutes" against 28.9 min to read and 30.4 min in total (iv[1], iv[35]). The induction notebook is "about 27 minutes" against 19.1 printed (ind[29]); the slices notebook is "about 8 minutes" against 5.4 (sl[49]).
- **Record response to fig1f:** "The data check now also prints the general and subject fields". ind[5] prints only the session and subject description counts; it is not a dump of the fields.

Every other number in the Result cells, the summaries and the record notes matches the printed outputs.

The verifications block states my round-1 reasons faithfully, in my words, with a few items from my problem list added (for example the problem 9 note under fig2c and the problem 10 note under fig3i). It records `agrees: false` correctly for figs3 and the 8 in vivo claims.

### 3. Round-1 points

**Resolved:**
- 1: absolute-current rule, plus pre-induction firing and holding current printed.
- 2: drug-free subsets.
- 3: artefacts removed, robust scaling; the mixture still fails its check, and that consequence is accepted.
- 5: smoothed threshold, synthetic test across rates, within-rate comparison.
- 6: pairing checked, thresholds examined and recorded as doubtful.
- 7: variants run.
- 8: the further RAF readings were run.
- 9, 11, 12, 13, 14 and 15.

**Partly resolved:**
- 10: start times are identical where shown; the rat evidence is weak, the in vivo evidence strong.
- 4: resolved for human and in vivo by blocking. For rat, the inverted RA/AIS proportion is not addressed.

**Remaining issues that bear on a conclusion:**
1. **fig2e-sag-raf-smaller:** untested cells are counted as without RAF (ind[29]). Rerun on tested cells only and check whether the rat P < 0.001 survives.
2. **fig3l, fig3k, fig3m-ais and fig3m-ra:** the rat mixture labels about 75% of APs as RA against the paper's roughly 12%. Either apply the same validity standard used to block the human and in vivo claims, or say in each note why the slope check alone is enough.
3. **fig2e-sag-raf-smaller assumption:** remove the non sequitur from its rationale.
4. **Wording:** fix the sentences quoted in section 2.
