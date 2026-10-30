**A. Outcomes** (the claims file has 33 claims; the ids and reasons below come from it)

| claim | my outcome | reason |
|---|---|---|
| fig4-unit-counts | not_reproduced | The RSU/FSU split can't be tested, but the criterion's partial clause needs only the per-area totals, which don't depend on typing. Cell 16: 3000 Hz S1 320 vs 366, POm 339 vs 250; 30 Hz S1 390 vs 209, POm 315 vs 232. None is within 10%. |
| fig4a-s1-rsu-time-locked-3000, fig4b-pom-rsu-time-locked-3000, fig4-postsonication-3000, fig4-30hz-responses, fig4-fsu-no-change | blocked (metadata_insufficient) | Cell 9: all 22,617 `celltype_label` values are 0, 33 recordings have no such column, and the units tables hold only spike_times. Without waveforms, IP and AHP can't be computed. |
| fig5a-sham-no-change | blocked (data_missing) | Cell 11: `general/notes` gives only S1, M1 and POm as targets, and no identifier suffix marks a sham. The voltage field was not checked (see C). |
| fig5b-cg1-control-no-change | blocked (data_missing) | Sessions are aimed at M1, none at CG1 (cell 11). |
| fig6-unit-counts | not_reproduced | Untyped totals over five PRFs: S1 1648 vs 1297 (+27%), POm 1429 vs 1019 (+40%). Both are outside the 10% the partial clause allows, under any typing. |
| fig6a-s1-rsu-time-locked-prf, fig6a-s1-rsu-delayed-prf, fig6b, fig6c, fig6d, fig7a–d, fig8a, fig8b, fig9a, fig9b | blocked (metadata_insufficient) | All need RSU/FSU types (see cell 9). |
| fig10a–fig10f | blocked (metadata_insufficient) | Pairs are defined by type. The stored STTC files were never opened beyond their shape, so whether they carry types is unchecked. |
| pathway-follows-local-prf | blocked (metadata_insufficient) | Depends on fig6a and fig10c. |
| fig11b-ac-responses | blocked (methods_underspecified) | With the claims file's readings (N1/N2 × B1/B2, Bonferroni C1 = ×5), cells 20 and 21 give: N1/B1 partial (during 1500, 3000 and 4500; 4500 is one extra); N1/B2 not reproduced (during adds 300 and 4500, two extras); N2/B1 and N2/B2 not reproduced (KW during p = 0.021). The readings disagree and none reproduces. Units: 633 vs 453 ± 45 (per PRF 112/138/167/127 vs 83/107/104/100). |
| fig11c-ac-to-s1-30hz, fig11d-ac-to-s1-3000 | blocked (metadata_insufficient) | Both need S1 RSU/FSU types. The untyped pair counts (the 1421 "all pairs" reading and 1714) could have been computed but decide nothing. |
| auditory-confound-low-prf | blocked (metadata_insufficient) | Depends on fig11c and fig11d. |

**B. Problems**

1. [affects a conclusion] The notebook was written against a different claims file. Cell 0 lists 37 claims with ids such as fig11-ac-unit-counts, methods-insitu-pressure and synthesis-prf-pathway, and `tfus.py` and cell 19 use labels M1, M3, M4 and O2–O4. The supplied file has 33 claims with readings N1/N2, B1/B2/B3 and C1/C2. As a result, the criteria actually applied in `judge()` are not this file's.
2. [affects a conclusion] `judge()` (cell 20) applies the wrong partial rule. It uses `kw_ok and sum(named) >= 4`, but the claims file's rule is "sets differ by one PRF in one window or the 300 Hz part fails". This labels N1/B2 ×5 as partial even though its during-sonication set has two extra PRFs (300 and 4500). The notebook also never applies the header rule that disagreeing readings make the claim blocked as methods_underspecified.
3. [affects a conclusion] Cell 16 / blocked table: fig4-unit-counts and fig6-unit-counts are marked blocked. The totals that decide "partial vs not" are untyped and already computed, so the outcome is determinable.
4. [does not affect a conclusion] `judge()`, `lowest_300` requires 300 Hz to be lowest in both windows; the claims file says at least one. Under N2, 300 Hz is lowest postsonication (55.5%). This doesn't change the outcome because KW during fails under N2.
5. [does not affect a conclusion] `judge()` and O4 use Bonferroni ×2 (two windows), which is not a reading in the claims file. C1 is ×5 (parameter levels), and C2 does not apply. The ×5 results are shown, so I used those.
6. [does not affect a conclusion] `baseline_test` reading O3c is a one-sample signed-rank test of normalized rates against 100. It is not the claims file's B3 (a paired signed-rank test on raw rates), and B3 is a variant that decides nothing, yet `judge()` lets O3c decide outcomes.
7. [does not affect a conclusion] This is a problem with the claims file, reported and not corrected. Its N2 reading (per-trial ratio, zero-baseline trials dropped) is biased by firing rate. I tested `tfus.normalized_rate` on synthetic Poisson units with no stimulus effect: N2 gives about 33%, 89% and 121% at 5, 15 and 40 Hz. The notebook's own `pre2_b` is 54–66% for every PRF. N2 against B1 (100%) therefore can't detect an increase, and the KW on N2 values is confounded by rate differences between sessions. The blocked outcome stands anyway, because N1/B1 and N1/B2 already disagree.
8. [does not affect a conclusion] The claims file may misread the paper for fig11b. The Results say Fig. 11B compared AC responses "with varying combination of PRFs and DCs", while the claims file restricts it to PD 200 µs. The notebook's all-PD variant (cell 22) reproduces even less: 300 Hz is significant and not lowest, with 5745 units.
9. [does not affect a conclusion] Cells 18–21: AC data come from 7 subjects (the paper has 12) with 3–4 sessions per PRF. Single sessions dominate, for example BH538 at 3000 Hz post 654% and BH537 at 1500 Hz during 302%, while the tests treat units as independent. This follows the paper, but it makes the p-values fragile.
10. [does not affect a conclusion] Cell 8 deduplicates with `drop_duplicates("signature")`, which keeps an arbitrary copy. One group stores the same spikes under both an S1 and a POm label (BH499_300_200), so one of the two area labels is wrong. That touches the S1/POm counts but not the AC analysis.
11. [does not affect a conclusion] `window_counts` uses `searchsorted`, which assumes sorted spike times. Sortedness is never checked.

**C. What I could not check, and what would have let me**

- **Sham sessions.** I couldn't rule them out: the identifier's voltage field (`volt`) was never tabulated (a 0 V session would be a sham), and the 5 files with an empty area are unexplained. Needed: `recs.volt.value_counts()` and the identifiers and notes of files with `area == ""`. DANDI asset metadata does not expose identifiers, so I couldn't check this through the API.
- **Whether "M1" sessions are the paper's CG1 control.** The notes say M1, so this can't be resolved from the data.
- **Stored STTC files** (370 files, 60 GB). Their content was never inspected for pair or type information. Needed: the dataset and attribute listing of one file.
- **Session list behind the S1/POm counts.** Needed: cell 16's `cp` broken down by subject and session. Ten subjects contribute 14–17 sessions per PRF, so some subjects have repeat sessions.
- **Spike-time ordering.** Needed: a check that `np.diff(u) >= 0` for every unit.
- **A results table restricted to the claims file's readings** (N1/N2 × B1/B2 × C1) and its partial rule, plus the untyped AC–S1 pair counts for fig11c and fig11d.
- **Archive checks I did run.** Through the API, I confirmed that 000463 lists no Units (variables: LFP and ElectricalSeries) and that 000946 has 39 subject folders: 19 data folders, 19 STTC folders and BH594, which is consistent with the notebook's 19 subjects.
