All six author steps are done. The entry checks and runs from a clean environment, the attempt record is written, and the handover is built in `executed/001177-zhuang-2025/handover/`. Nothing is committed.

## 1. Outcomes (44 claims)

| Claim | Outcome |
|---|---|
| fig1fg-baseline-similar, fig1fg-delay-discounting, fig1f-ctrl-ppx-no-change, fig1g-park-ppx-fewer-large | reproduced |
| fig2d-ctrl-a77636-no-change, fig2e-park-a77636-fewer-large, fig2fgh-a77636-k-auc | reproduced |
| fig6b-ctrl-ppx-stable, fig6c-park-ppx-progressive, fig6de-a77636-persistent | reproduced |
| figs2de-omissions-low, fig5g-mcherry-no-change | reproduced |
| fig1c-rotarod, figs1d-snc-cells, figs6-dreadd-validation | reproduced |
| fig3b-k-no-correlation, figs4-a77636-no-correlation | reproduced |
| fig2bc-a77636-locomotion | reproduced (rests on an assumption) |
| fig1ijk-ppx-a-k-auc | partially reproduced: the rise in K is not significant by Dunn's test (p = 0.19) |
| figs2ijk-ppx-washout | partially reproduced |
| figs2gh-ppx-latency | partially reproduced |
| figs3-a77636-washout-latency | partially reproduced |
| fig1b-th-loss | partially reproduced: losses of 64% (DLS) and 57% (DMS) against 50 ± 5% |
| figs1-instrumental-learning | partially reproduced |
| fig5hi-dreadd-fewer-large | partially reproduced |
| fig5jl-dreadd-params | partially reproduced |
| fig5cf-cno-locomotion | partially reproduced (rests on an assumption) |
| fig3a-a-correlates-dms | not reproduced: r = 0.32, p = 0.13 against the paper's 0.51 |
| figs2abc-sex-similar | blocked (metadata_insufficient): no file gives each mouse's sex |
| figs1ef-ppx-locomotion | blocked (other): no PPX open field file was deposited |
| 14 electrophysiology claims (Figures 4, S5, 6F–I, S8) | blocked (data_missing) |

Totals: 18 reproduced, 9 partially reproduced, 1 not reproduced, 16 blocked.

Where the method could be checked, it matches the paper exactly. The A77636 Dunn's p-values (0.0053 and 0.0008) and the slice input-output result F(1, 32) = 17.64 come out identical to the paper's.

## 2. What was found about the data

**The dandiset (DANDI:001177, pinned at 0.250902.2127, the only published version):**
- It holds the paper's 18 mice (7 control, 11 parkinsonian) in 56 sessions: raw 30 kHz voltage, LFP and per-electrode threshold crossings.
- It has no sorted units, unit classes, optical labels, laser pulse times or injection times, so no electrophysiology claim can be tested.
- Two files have a `units` table with spike times only and no labels.
- Three sessions have start times in 2025, out of order with the same mice's other days.
- The subject descriptions are mis-encoded ("1.5â€¯microliters").

**The Zenodo deposit (doi:10.5281/zenodo.15258978), which holds all the tested data:**
- Mouse E6 has no PPX sessions, mouse R5.5 has no delay discounting files, and the PPX open field data are absent.
- Some logs are deposited twice: 233 are byte-identical between the PPX and DREADD folders, and 75 between the A77636 and DREADD folders.
- Two cohorts ran a different task from the Methods: the 2020 control cohort used delays of 0, 6, 12 and 18 s, and the 2021 cohort ran 30 free-choice trials per block instead of 20.
- The open field files have no injection mark.
- The SNc and instrumental-learning workbooks have labelling and column-shift errors.
- The Methods' stability rule passes only 12 of 47 mice on the deposited baseline sessions, so which baselines the paper used is undocumented.

**Assumptions** (marked `assumed: true` on fig2bc and fig5cf):
- Injection is taken at 20 min into each open field file, where 25 of 26 A77636 files lose tracking briefly.
- Mice missing from the A77636 control list are counted as parkinsonian; that leaves 16, the paper's N.

Other choices did not change any outcome: TH normalized per staining cohort (normalizing to all controls is also shown), and the drug-OFF condition averaging every washout session, following the paper's code.

**Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
1. When was the drug injected in each open field file?
2. Was striatal TH normalized to the controls of each staining cohort or to all controls?
3. Which test gives p = 0.03 for the PPX effect on K? Dunn's test gives 0.19 here; the Friedman test gives 0.032.

**Questions to a reader:** none.

## 3. Protocol gaps

1. A claim marked `data: elsewhere` whose data are not public anywhere (figs1ef) cannot be blocked as `data_missing`, because the entry check rejects it. I used `other` and recorded a `data_missing` finding.
2. Findings are defined as being about the dataset, but most findings here concern the outside deposit. I recorded them and labelled each as Zenodo.
3. Group labels for data elsewhere had to come from other files in the same deposit (the README lists, the histology workbook) or from the DANDI subjects. Link claims seem meant only for matching outside data to the dataset, so I added none and recorded the sources as deviations.
4. For fig5jl the criterion defines a partial outcome only for a case that did not occur. I recorded it as partial (the effects hold in part) and explained this in the notes.
5. When a claim's criterion says "as" another claim's, it is unclear whether that claim's readings carry over. For figs2de I used the four-session reading.
6. One expected value covered two quantities (fig1b, "DLS and DMS"). I recorded their mean as `measured` and gave both values in the notes.
7. archives.md has no Zenodo section. I streamed the files into memory with fsspec, as the CRCNS section describes.
8. The clock check could not be done for the electrophysiology because no session has trial or event tables. The notebook says so. For the behaviour data, the check confirmed that the block delays and the event times are consistent.

## 4. Runtime and failures

- The run went from 10:25 to 11:55 UTC.
- The notebook takes 17.7 minutes from a clean environment, over the 10-minute aim but under the 30-minute limit. Most of the time goes to opening all 56 NWB files and reading the open field workbooks.
- Nothing failed.
- After the final run I edited three markdown sentences (two wording fixes and the clock-check sentence) in both the source and the executed copy. I confirmed the two have identical cell sources and re-ran the check and the handover after the edits.
- The untracked dotfiles in the repository root are `/dev/null` mounts the sandbox created before this run. I left them alone.
