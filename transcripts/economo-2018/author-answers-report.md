I've taken up all 15 answers, re-run the entry, updated the notebook, README and attempt record, and built the handover. Nothing is committed or pushed, and I haven't verified my own work.

**Two problems outside the attempt:**
- **The claims file was broken, and I edited it.** The answer commit deleted four `- id:` lines (pt-retrograde-sublaminae, pt-projection-cluster-mapping, pt-types-account-for-all-pt, pt-marker-genes). With those gone, YAML merged each claim into the one above it, so the file parsed to 27 claims, and `pt-types-shared-targets` carried the smFISH statement. I put the four lines back where they were before; no statement, expected value or criterion changed. Please confirm this edit is acceptable.
- **`entry.py all` still stops at the check.** All 22 errors are in the deprecated `-01` record, which lacks outcomes for claims the rewritten file added. The `-02` record passes. As in the earlier run, I ran `entry.py run` directly. It passed (628 s), with outputs identical to the run I wrote the conclusions from apart from timings.

**What one answer changed for every electrophysiology claim:** the selection is now the code's per-unit rule (44 PTupper and 56 PTlower units, since the dandiset lacks 11 of the paper's sessions). Each unit's own trial range is used, and the session rule and "all trials" are now variants.

| Question (claim asked about) | What the answer changed | Affected claim: now (before) |
|---|---|---|
| pt-tagged-units | Use the code's rule when neither reading matches | pt-tagged-units: not reproduced (not reproduced); pt-spike-rates-similar: **not reproduced** (blocked), peak rates differ, p = 0.030; pt-variance-explained: **reproduced** (blocked), ratios at most 1.08 and 1.23, within the 1.3 bound; the other 11 electrophysiology claims keep their outcomes |
| pt-single-neuron-early-selectivity | Use the unit's own trial range | **reproduced** (blocked): 0.410 against 0.237, t-test p = 0.0012, Mann-Whitney p = 0.0041 |
| pt-upper-early-preparatory | The paper gives no rule for "larger", so both rules stay | blocked (blocked): rule (i) gives partially reproduced and rule (ii) not reproduced, in all 8 combinations. Its dependents stay blocked: pt-upper-persistent, pt-cohort-control, pt-types-differ-in-timing |
| pt-cd-change-at-go-cue | No level is fixed, so both stay | blocked (blocked): reproduced at level 0.5, partially reproduced at 0.75 |
| pt-lower-movement-termination | No windows are fixed; the rebuilt last lick is acceptable only if leaving out the trials where it disagrees with the paper's processed data doesn't change the outcome | blocked (blocked). The windows and the mouse readings give different outcomes. I ran the requested check: leaving out the 1.7% and 2.0% of trials where the rebuilt last lick disagrees changes the outcome in one combination (window (a), 4 and 8 mice, projection (a)), so there the rebuilt lick is not shown to be harmless |
| pt-depth | The unit depth decides | reproduced (reproduced): 636 against 1004 µm |
| pt-lower-heterogeneous-rates | Dependency moved to pt-tagged-units | **reproduced** (blocked by its dependency): Bartlett p = 0.0019 for baseline, p < 0.0001 for peak |
| pt-types-transcriptomic | Counting rule fixed | reproduced (reproduced): 27 clusters |
| pt-projection-cluster-mapping | The code's grouping named as reading (a) | reproduced (reproduced): 62 and 91 under reading (b); the code's grouping gives 58 and 89 |
| pt-bulk-sc-fold-change-correlation | The legend's log2(CPM + 1) is the measure | reproduced (reproduced): r = 0.874; the code's version, 0.867, is now a variant |
| pt-upper-thalamus-projection | Three readings, count holds if one matches | **reproduced** (blocked): 8 under "more termini in the thalamus than the medulla" |
| pt-lower-medulla-projection | Same, for "bypassed the thalamus" | **reproduced** (blocked): 4, all with termini in the intermediate reticular nucleus |
| pt-types-account-for-all-pt | The 18 are listed in Supplementary table 1 | partially reproduced (partially reproduced): the same 18 neurons; 17 of 18 reach the superior colliculus, AA0134 does not |
| pt-marker-genes | Data now `dataset` | blocked as data missing (blocked as other) |
| pt-retrograde-sublaminae | No counting method exists | blocked, methods underspecified (unchanged) |
| pt-types-shared-targets | The test on the reconstructions is only a variant | **blocked, methods underspecified** (reproduced): the first part holds (12 of 12 reach the superior colliculus), but the second part's intended test is bulk images the paper gives no method to analyse |

pt-types-differ-in-timing stays blocked through pt-upper-early-preparatory and pt-upper-persistent, though one of the claims it summarises (pt-single-neuron-early-selectivity) is now reproduced.

Changed files:
- `entries/000006-economo-2018/alm.py`
- `entries/000006-economo-2018/reproduce_economo_2018.ipynb`
- `entries/000006-economo-2018/README.md`
- `attempts/000006-economo-2018-02.yaml`
- `claims/000006/10.1038-s41586-018-0642-9.yaml` (the four restored id lines)

The handover is in `executed/000006-economo-2018/handover/`.
