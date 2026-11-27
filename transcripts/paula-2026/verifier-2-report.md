**Verifier report, round 2: de Paula et al. 2026 (doi:10.1103/wndc-k654) on DANDI:000713 0.240702.1725**

The claims file has 38 claims, and the attempt record has 38 outcomes: 12 reproduced, 6 partially reproduced and 20 not reproduced. They match the notebook's Summary (cell 137) and its verdict table (cell 136).

### 1. Outcomes and assumptions

I agree with all 38 stated outcomes. Each one follows from the claims-file criterion applied to the printed outputs.

- **Changed since round 1.** The record agrees with my round-1 outcome on 31 claims and moves seven. Six move because of the new unit filter, 'vbn' (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s):
  - fig1c-cv-region-medians: not reproduced → partially reproduced
  - fig1e-positive-cv-modules: not reproduced → reproduced
  - fig1e-dg-ca3-anticorrelation-hubs: not reproduced → reproduced
  - fig2a-hippocampus-cv-stable: not reproduced → reproduced
  - fig3c-vis-ch-plane: stays not reproduced
  - fig4b-thalamus-lgd-lp-modulated: reproduced → not reproduced

  The seventh, fig4b-other-thalamus-not-modulated, moves from my partially reproduced to not reproduced because of the stricter pairwise test (cell 93). I accept that: Kruskal-Wallis finds MGd, SGN, MGm and MGv, the any-pair Mann-Whitney test finds MGd, SGN and MGv, and the criterion says "not reproduced when the test finds modulation in any".
- **Assumptions.** All 36 claims on the recordings other than table1-sample carry `assumed: true`, and fig3a-reference-systems does too. Each states the 'vbn' unit filter in its deviations, with the evidence for it. That evidence holds:
  - Neurons per population are within 5% of Table I in every area (VIS 92.7 against 92.1, TH 64.7 against 65.6, HP 112.0 against 116.8, MB 98.0 against 98.1; cell 8).
  - It is the closest of the six filters by largest |log ratio| (0.073).
  - The choice uses counts only, not outcomes.

  Adding a third reading to the claims file's two is reasonable, and it is disclosed. The claim-specific readings are also stated: session combination (b) for fig1e, effect form (i), the any-pair test, and the fig3a readings. The claims file allows judging "under one reading", so fig4c (legend values) and complexity-separates (JS reading) are within the rules.
- **Knife-edge outcomes.** Several outcomes fall within about 0.004 of their bounds, and five of them flip under the other unit readings:
  - fig4b-thalamus-lgd-lp-modulated: LP spontaneous median 0.098 against a lower bound of 0.099 (cell 90). Reproduced under 'all' and 'qc'.
  - fig1e-dg-ca3-anticorrelation-hubs: most negative r −0.247 against −0.243, under 'vbn' with reading (b) only (cell 25). Also, the 32 "most negative" pairs reach +0.026, while the paper gives a range up to −0.002. The criterion does not test that upper end.
  - fig1e-positive-cv-modules: passes in 1 of the 6 unit and session combinations (cell 22).
  - fig3c-vis-ch-plane: C 2.5th percentile 0.0887 against 0.090. Reproduced under 'qc' (cell 70).
  - fig4b-thalamus-lgd-lp-modulated and fig2a-hippocampus-cv-stable both change with the unit reading.

### 2. Text against outputs

Nearly every sentence checks out. These do not:

- **Cell 91 and the record's fig4b-thalamus-lgd-lp-modulated notes:** "every visually driven condition against spontaneous p at most 3.2e-21 and 2.9e-19". LGd's largest such p is 4.5e-21, under reading b/b (cell 90).
- **Cell 17:** "'all' and 'qc' give the same outcome. The outcome rests on the adopted unit reading ('vbn')". The two sentences contradict each other; cell 136 gives partially reproduced under all three unit readings.
- **Cell 100:** the sentence "The outcome rests on…" appears twice. This is cosmetic.
- **Cell 60:** "Most midbrain values are below 0.165 under most readings (13 to 26 of 30)". 13 of 30 is not most.
- **Cell 137 (Summary):** "The visual cortex responds to every session's flash onsets and not … to omitted flashes". Cell 6 shows omitted-flash contrasts up to 92.6, above the smallest true-onset contrast (69.2). What is shown is that the true-onset response is larger than the omitted-flash one in 153 of 153 sessions, not that there is no response.
- **Findings 4, 5 and 11** in the attempt record's `findings` list are wrong or out of date:
  - **Finding 4:** "active against blanks 0.3% to 9.5% in visual cortex". That is the 'all' range. Under 'vbn' it is 3.12% to 11.24% (cell 47).
  - **Finding 5:** "Kruskal-Wallis gives p < 0.001 and pairwise Mann-Whitney tests do not, so the outcome of the claim depends on the test". This is out of date. Under the adopted any-pair reading the pairwise tests find MGd, SGN and MGv (cell 93), and the outcome is not reproduced under both test readings (cell 94).
  - **Finding 11:** concatenating gives "NB as the leading anticorrelation hub". Under 'vbn' reading (a), CA3 and NB tie at 8 pairs each (cell 25). NB leads alone only under 'all'.
- **README:** "about 47 minutes, most of it reading the spike times" cannot be checked. Only the extraction time is printed, 32.9 min (cell 3), and cell 2 says "about 46 minutes" for that same step.

The README's claim counts and its "ten outcomes would differ" match cell 136. The attempt record's `verifications` section gives my round-1 reasons faithfully, in my words.

### 3. Round-1 points

**Resolved:**
- **B1 (unit reading):** 'qc' is now run for every claim, and the other filters are counted ('good', and presence ratio > 0.95).
- **B3 (fig3a):** the Ikeda map is judged at 6.683 and 12.966, and the sine is judged against its floor reading.
- **B4 (fig4b-other):** all six pairwise p-values are printed, and the any-pair reading is used.
- **B6:** natural-log JS divergences are added.
- **B10, partly:** per-population Wilcoxon tests are added for Fig. 1c and Figs. 3c to 3f.
- **B11:** spans are compared unrounded.
- **B8:** it is now the stated reason for adopting reading (b) in fig1e, and reading (b) is one of the claims file's two readings.

**Unchanged, no effect on a conclusion:** B5 (effect form; the value part fails anyway) and B7 (fig2b legend reading b).

**Remaining, bearing on conclusions:**
1. **Sessions (B2).** The 102 sessions remain unidentified, and every pooled result uses 153 sessions (about 1.5× the paper's populations and windows). This cannot be settled from the files.
2. **Pseudo-replication in the condition tests (B10).** The Kruskal-Wallis and Mann-Whitney tests in fig4a and fig4b are still run on windows. For fig4b-other-thalamus-not-modulated, a claim of absence, the "modulation" comes from median differences of at most 0.0055 over thousands of non-independent windows. A per-population test might not reach p < 0.001. The paper appears to do the same, so the outcome stands under the claims file, but it is fragile.
3. **Blank series length (B9).** The blank series is 286 s against the paper's ~240 s, and this is unexplained. It is now recorded as a finding.
4. **Unit and session readings.** Ten outcomes depend on the 'vbn' reading, and fig1e also depends on session reading (b). These are reasonable and stated, but they decide several near-threshold outcomes (section 1).
5. **Claims-file issue, reported not corrected.** The 'qc' presence-ratio cutoff of 0.9 is unverified against the AllenSDK default of 0.95. The 'qc95' counts (0.31 to 0.51× Table I) show it makes no difference.
6. **Figures.** The PDF figures were never compared, including the Fig. 3a parameters.

### 4. Critical findings

No finding is rated `critical`. Only two findings carry a severity, both "none": the checks that passed (finding 8) and the generic location labels (finding 9). The record's clock, duplicate and fingerprint checks (cells 4 and 6) show none of the problems that would make a finding critical, and I would not rate any finding critical.
