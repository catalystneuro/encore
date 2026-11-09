I checked all 37 claims in the claims file. The notebook tests 11 of them on CA1 alone. It treats `tables1-cell-counts` and the other 25 claims as blocked. The archive's own file list (`checksums.md5`, `filelist.txt`, shank maps) confirms that hc-2 holds only 21 open-field sessions with CA1 probes, from rats ec13, ec14 and ec16.

My outcomes: 5 reproduced, 2 partially reproduced, 4 not reproduced and 26 blocked. One of the blocked claims, `figs6-identified-cells`, could be partly tested on CA1 but was not attempted.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| tables1-cell-counts | blocked (metadata_insufficient) | The per-rat counts cover all tasks, and hc-2 holds only the open field. For the open-field totals (paper 1083 principal cells / 188 interneurons; hc-2 739 / 181 counted session by session, cell 14), the notebook asserts the paper's figure "includes i01" but shows nothing to support it. Whether hc-2 holds all of the paper's open-field sessions is also unknown. |
| fig3d-hippocampal-modulation | partially_reproduced | Mean R 0.193 is inside 0.19±0.019. Percent modulated is 93.0% against 84±8.4 (limit 92.4), so just outside (cell 16). Two of the four theta-epoch variants fall inside (91.1%, 92.0%; cell 17). The CA1-vs-CA3/DG comparisons cannot be tested. |
| fig3-interneurons-min-ascending | reproduced (CA1 only) | Minimum bin is 335° for principal cells and 315° for interneurons. Both stay inside reading (a), 180–360°, after converting to EC3 phase with the 0–80° shift (255–335° and 235–315°). The result is stable across rats, cell-type rules and epoch variants (cell 19). |
| figs9-phase-method | reproduced | Maxima, minima and Hilbert methods differ by at most 0.7° (cell 21). |
| fig5-rate-phase-shift | not_reproduced | CA1 principal cells advance by 130.2° from 4 Hz to ≥40 Hz; the criterion needs more than 135° (cell 23). Every variant gives 129–131°. Only the single-cell variant (−137°, which the criterion reports but does not judge on) and rat ec14 (−147°) exceed 135°. The EC2 part cannot be tested. |
| fig5b-burst-double-peak | not_reproduced | Burst spikes and ≥40 Hz spikes differ by 154°; the criterion requires under 90° (cell 25). The two-peak part does hold under both readings (peaks at 235° and 25°; the two-component BIC is lower). |
| figs13-interneuron-rate | not_reproduced | The largest pairwise difference is 59.6°, above the 33° limit (cell 27). It stays above 33° under every cell-type and epoch variant (minimum 43.2°). |
| figs12b-burst-single-phase | reproduced (CA1) | 64 of 226 cells (28%) under reading (a) and 177 of 226 (78%) under reading (b), each against 5% chance, binomial p ≤ 3e-30 (cell 29). |
| figs19-fast-firing-minority | reproduced (CA1) | Low against high rates: 0.546 vs 0.049 under reading (a), 0.662 vs 0.338 under (b); this holds in every rat (cell 31). The EC part cannot be tested. |
| figs7-individual-rats | reproduced (CA1) | Largest difference between rats is 8.5° for principal cells and 31.9° for interneurons, inside both 45° and 90° (cell 33). |
| figs11-phase-time-agreement | partially_reproduced | After wrapping the lag to one cycle, principal–interneuron pairs give r = 0.614 (circular 0.659), which passes. Principal–principal pairs give r = 0.146 (circular 0.205), which fails. All pairs pooled give r = 0.361, which also fails (cell 35). |
| figs2-ripple-sequence | not_reproduced | Firing increase during ripples, principal cells: 10.05× under baseline (a), 7.41× under (b), against 6±0.6. Interneurons: 4.41× and 2.12× against 3±0.3. No baseline reading puts either group inside tolerance (cell 37). The onset/peak delays need EC data and cannot be tested. |
| figs6-identified-cells | blocked (other: not attempted) | Figure S6 includes hippocampal neurons. The jitter test for monosynaptic pairs can be run on hc-2's CA1 spike times (20 kHz), so the CA1 part could be tested. "data_missing" is wrong for that part. |
| figs16-open-field-smallest-shift | blocked (data_missing) | Open field is the only task, so the comparison between tasks cannot be tested. The criterion still asks for the open-field median shift to be reported, and the notebook does not report it. |
| fig2c-ec-cell-classes, figs4-ec2-bursting, fig1-ec3-ca1-theta-coherence, fig1-layer-reversals, fig3-dg-ca3-precede-ca1, fig3-ec-opposite-to-targets, fig3c-ec3-subset-locked, fig3-ec5-weakest, fig3d-ec2-strongest-modulation, figs10-ca1-reference, fig4a-ec-hippocampus-offsets, fig4a-pair-offset-ranges, fig4a-ec5-ca1-flat, fig4-ec2-ec3-opposite-lags, discussion-ec-interneurons-with-ec2 | blocked (data_missing) | Each needs EC units or EC LFP, or CA3/DG units. The archive has none: no EC probe, and only CA1 shanks in the shank maps. Every bursting ordering in `figs4-ec2-bursting` involves EC, CA3 or DG. |
| figs8-task-invariance, fig6-hippocampal-precession, fig7a-precession-strength, figs15-ec3-no-precession, fig7b-frequency-shift, figs18-spike-phase-spectrum, fig7-ca1-highest-precession | blocked (data_missing) | Each needs several tasks, linear-track sessions, EC groups, or results that depend on those. The archive holds only open-field sessions. |
| fig8-ec-population-predicts-sinks | blocked (data_missing) | Needs the CSD data of Montgomery et al. and EC populations; neither is in hc-2. |

## B. Problems

1. **[affects a conclusion]** `hc2.classify` (cells 12 and 14). The main rule (trough-to-peak below 0.4 ms or rate above 10 Hz) labels 104 units firing at or below 1 Hz as interneurons. The "int" group's median rate is 0.24 Hz, which is implausible for CA1 interneurons under the methods the paper cites. The stricter variant `type_v3` (77 interneurons) was run for cells 19, 27 and 33 but not for `figs2-ripple-sequence` (interneuron fold, cell 37) or `figs11-phase-time-agreement` (principal–interneuron pairs, cell 35). It also decides whether hc-2's interneuron count matches Table S1's 188 (181 vs 77).
2. **[affects a conclusion]** `figs6-identified-cells` is blocked as data_missing, but its CA1 part is testable on hc-2 (Figure S6 covers hippocampal cells; the jitter test needs only spike times).
3. **[affects a conclusion]** `figs2-ripple-sequence`, cell 37. Firing increase is computed only as peak over baseline of the cell-averaged rate, which high-rate cells dominate. A per-cell fold (median of each cell's ratio) is another reading of the paper's open "fold increase" and was not run. Ripples also come only from pauses in the open field; the paper's Figure S2 ripple set is not stated. Either could move the result into or out of tolerance.
4. **[affects a conclusion]** `tables1-cell-counts`, cells 13 and 14. The claim that the open-field 1083/188 includes rat i01 is unsupported. If i01 had no open-field sessions, the open-field totals are testable (739 principal cells, outside 1083±108; 181 interneurons, inside 188±19), unless hc-2 holds only some of those sessions.
5. **[does not affect a conclusion]** Cell 35, `figs11-phase-time-agreement`. The pooled "all" correlation includes interneuron–interneuron pairs, which Figure S11 does not show (it has only principal–principal and principal–interneuron pairs). The per-category results are what decide the outcome.
6. **[does not affect a conclusion]** Cell 29, `watson_williams`. The test treats spikes as independent, which inflates significance (78% of cells). The formula itself is correct (Zar), and reading (a) passes anyway.
7. **[does not affect a conclusion]** Cell 6, `_pick_pyramidal_channel`. In ec013.808 (channel 0, r = 0.893) and ec013.844 the session-mean principal-cell phase is 248–265°, against about 200–220° in other sessions (cell 33). This may mean the reference channel is off the pyramidal layer. Results by rat are robust to it.
8. **[does not affect a conclusion]** `figs16-open-field-smallest-shift`. The open-field unit–LFP frequency shift for CA1 that the criterion asks to be reported is missing.
9. **[does not affect a conclusion]** Cell 0, summary table. It says "fig3 EC and CA3/DG claims (5)"; there are 4 besides `fig3d-ec2-strongest-modulation`, which is listed separately. All 37 claims are still covered.
10. **[does not affect a conclusion]** Theta reference and epochs use the CA1 pyramidal-layer LFP instead of EC3, with the ratio threshold, speed threshold and pixel scale as assumptions. These are stated and varied, and outcomes are stable across the variants. For `figs7-individual-rats`, a single CA1 reference may make rats look more alike than the paper's EC3 reference would.

The helper functions behave correctly on synthetic inputs:
- **Phase methods:** a spike at the trough reads 180° under the maxima, minima and Hilbert methods.
- **Rayleigh test:** on uniform data it gives false positives at 0.94% for p < 0.01 and 5.1% for p < 0.05.
- **Rate, ISI and epoch helpers:** `inst_rate_count`, `isi_groups` and `in_epochs` give the expected outputs.
- **`waveform_features`:** returns a trough-to-peak latency of 0.35 ms for a 7-sample gap at 20 kHz.

## C. What I could not check

- **Table S1:** it is an image, and no PDF renderer is available here, so I could not see whether its "square" column is broken down by rat or includes i01. A per-rat Table S1 printout next to hc-2's per-rat counts would settle `tables1-cell-counts`.
- **Session coverage:** whether hc-2's 21 sessions are all of the paper's open-field sessions for these rats. A list of the paper's sessions is needed and is not public.
- **Data loading:** I could not check it against the raw files without downloading them. Printing the `.clu` header counts against the unique cluster ids would have helped.
- **Outputs that would have let me settle more** if added to the notebook:
  - `figs2-ripple-sequence` and `figs11-phase-time-agreement` rerun under `type_v3`;
  - per-cell fold-increase distributions for ripples;
  - mean rate against trough-to-peak latency for the "int" units;
  - the jitter test for monosynaptic pairs on CA1 (for `figs6-identified-cells`);
  - the CA1 open-field unit–LFP frequency shift (for `figs16-open-field-smallest-shift`);
  - the depth of the reference channel against the shank maps in hc-2's docs.
