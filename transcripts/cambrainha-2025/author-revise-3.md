# cambrainha-2025 · author-revise-3 · run 46020175414

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/cambrainha-2025/verifier-3-report.md; ls entries/cambrainha-2025; grep -n "step 6" -A40 docs/protocol.md | head -80
```

```
Fri Nov 27 14:58:21 UTC 2026
**Verification report, round 3: Cambrainha et al. 2025 on DANDI:000713 (0.240702.1725)**

The attempt record proposes a change of outcome for one claim, and this round covers only that claim. All other outcomes are as verified in round 2.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| figs3-exponents-stable-with-threshold | partially_reproduced | Yes, provided it stays marked as assumed | — | See below (cells 81, 82, 83) |

**1. The numbers come from the data (cell 81, grid from 7 to 12 under CV (a), 101 points).**
- The code applies the criterion as written:
  - The SD is the across-session SD at the start of the grid (`per[0][e].std()`).
  - A grid point counts only if at least 10 sessions contribute (`notna().sum() >= 10`).
  - An exponent holds only if it holds in every phase.
- The printed table gives these results:
  - **α and β:** within one SD in all three phases. The largest departure is 0.036, against an SD of 0.048 or more.
  - **Active μ:** within (0.122 against 0.197, at 64 points from up to 32 sessions).
  - **Active and passive z:** within (0.028 against 0.045; 0.023 against 0.047).
  - **NNI z:** fails (0.083 against 0.058).
  - **Passive and NNI μ:** no point has 10 sessions (at most 7 and 6, cell 82).
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "verifications\|proposed" docs/protocol.md | head -40; grep -n "figs3-exponents-stable-with-threshold" -r entries/cambrainha-2025 attempts 2>/dev/null | head; ls
```

```
536:- **`proposed`**: on an outcome, a change of outcome found after the last
619:`verifications`, saying what was reviewed. Give the verifier's reasons in its
631:the change under `proposed` on that outcome, with the analysis behind it in
633:proposed changes, and `author-revise-3` applies those it agreed with and
771:### Round 3: proposed changes
773:Run only when the final revision proposed changes of outcome. Review each
775:with the proposed outcome. Nothing else is reviewed.
entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb:30:    "| figs3-exponents-stable-with-threshold | tested |\n",
entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb:333:    "The adopted reading of O6 (the largest surrogate kurtosis) puts kappa_surr_max at 34.29 in the active phase and 48.34 over all phases, above the plotted ranges, so the criteria's grids are empty. That maximum is set by a few surrogate windows (13 of 28335 above 15) (section \"The surrogate reference\"). The active maximum (34.29) comes from a window with 182 active units. The all-phase maximum (48.34) comes from a passive window of sub-545994 with 87 active units and 84 silent ones, and the next value (36.50) from a window of the same session with 12 active units; with at least 128 active units the all-phase maximum falls to 34.29. For the claims judged on a grid from kappa_surr_max, the criterion is therefore also applied with the grid started at every threshold from 3 up to the top of the plotted range, and at four named starts: the paper's value of about 7 (M4, read from Figures 3C, 3D and 4A), the 99th and 99.9th percentiles of the active surrogate kurtoses, and the maximum over windows with at least 128 active units. For four of these claims (fig3c-scaling-hit-rate-higher, fig3c-hit-rate-rises-with-threshold, fig4a-active-most-scaling, figs8-halves-and-phase-order) every start gives the same outcome, so the start does not matter. figs3-exponents-stable-with-threshold is run only at the named starts and o
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 530,545p docs/protocol.md; sed -n 610,640p docs/protocol.md; sed -n 765,800p docs/protocol.md
```

```
lists.
- **`seed_sensitive`**: `true` on an outcome that is not the same under all
  five seeds (step 3). The notes give the measured value under each.
- **`provenance: author_notes`**: the notes from the paper's authors that
  the attempt used, each by its issue's address (step 1, "Notes from the
  paper's authors").
- **`proposed`**: on an outcome, a change of outcome found after the last
  verification round, with its `reason` (see "Hand over for verification").
- **`inputs`**: everything used that is not in the dataset, each with where
  it came from (a DOI, or a repository at a commit).
- **`findings`**: what the attempt found, whatever the outcomes. Each is
  about one of two things, and is shown where it belongs:
  - **the data** (`about: data`): the dataset's files or metadata. Something
    is wrong, missing, undocumented or mislabelled, or differs from what the
    paper says the files hold. These are for the data owner and the archive,
    on the dataset's page. A mismatch between the files and the paper is about
method detail the author took from the paper against the passage the author
cites. A place where the claims file misreads the paper is reported; the
revision adds it to `questions/<paper>.yaml` as a question for a reader, as in
step 1.6, and does not change the claim. A reader answers it after the
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/cambrainha-2025-01.yaml
```

```
<persisted-output>
Output too large (48KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/3e339a01-235a-4584-bee9-64eac42aa518/tool-results/bnakvb5df.txt

Preview (first 2KB):
schema_version: 3
id: cambrainha-2025-01
datasets:
- archive: dandi
  id: "000713"
  version: 0.240702.1725
  doi: 10.48324/dandi.000713/0.240702.1725
  relation: primary
paper: doi:10.1103/w49n-2vz8
date: 2026-11-27
entry: cambrainha-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd attempts; sed -n 250,300p cambrainha-2025-01.yaml; grep -n "^[a-z_]*:" cambrainha-2025-01.yaml; grep -n "round: 2" -A12 cambrainha-2025-01.yaml | head -40
```

```
values, p = 2.5e-33 for each). Distances from the trivial values are ordered active > passive >
    NNI for alpha (0.481, 0.465, 0.398) and beta (0.240, 0.236, 0.164). z is 0.156 active, 0.152
    passive and 0.192 NNI, so it does not move away from 0 from active to passive. The surrogate
    exponents use the claim seed of the fig3a surrogate only; the Wilcoxon reading needs no
    surrogate and gives the same outcome. Paired by session with its surrogate (Wilcoxon
    signed-rank, 97 sessions), alpha exceeds the surrogate value by 0.413 and beta falls short of it
    by 0.208, p = 1.2e-17 for each.
- claim: figs3-exponents-stable-with-threshold
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_cambrainha_2025.ipynb
  output: claim:figs3-exponents-stable-with-threshold
  proposed:
    outcome: partially_reproduced
    reason: The criterion asks for stability "at every grid point with at least 10 sessions
      contributing", which holds vacuously for an exponent with no such point; the verified outcome
      counted such an exponent as not shown stable, a convention the criterion does not state. Read
      literally, the grid from 7 (CV (a)) fails for NNI z alone (0.083 against an SD of 0.058), so
      three of four exponents hold, which is partially reproduced (resting on CV (a) and the start of
      7). Passive and NNI mu are then not tested, as no grid point has 10 sessions with a mu (at most
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 432,2000p attempts/cambrainha-2025-01.yaml | grep -n "round\|figs3" | head; awk 'NR>=432' attempts/cambrainha-2025-01.yaml | grep -n "round: 2" -A30 | head -50
```

```
126:  - claim: figs3-exponents-stable-with-threshold
182:  reviewed: The full executed notebook after the round-1 revision, the helper module criticality.py,
274:  - claim: figs3-exponents-stable-with-threshold
287:      summary's "give the same outcome at every start except figs3" overstates, as figs3 was run only
289:    response: In round 2 the outcome may not change, so it stays not reproduced and the change to
290:      partially reproduced is proposed (`proposed`), for a third round. The convention is now stated
```

**Agent calls Bash**

```bash
cd  sed -n 432,445p attempts/cambrainha-2025-01.yaml; echo ----; sed -n 600,740p attempts/cambrainha-2025-01.yaml
```

```
verifications:
- date: 2026-11-27
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module criticality.py and the claims file, with the paper's full text. The verifier tested the
    helpers on synthetic data and checked the session files on the DANDI API. Report in
    transcripts/cambrainha-2025/verifier-1-report.md.
  results:
  - claim: sessions-selected
    agrees: true
    outcome: not_reproduced
    reason: All V1 units give 97 sessions and 68 mice with more than 128 units (98 with at least
----
      fig3c and fig3d tests still fail. O5 is asked of a reader (questions file); outcomes are
      tested on O5 as written. Outcome unchanged.
  - claim: figs8-halves-and-phase-order
    agrees: false
    outcome: not_reproduced
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/cambrainha-2025-01.yaml'
s=open(p).read()
start=s.index('- claim: figs3-exponents-stable-with-threshold\n  outcome: not_reproduced')
end=s.index('- claim: figs4-initial-kurtosis-poor-predictor')
new='''- claim: figs3-exponents-stable-with-threshold
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_cambrainha_2025.ipynb
  output: claim:figs3-exponents-stable-with-threshold
  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty. From the paper's
    value of 7 to 12 (CV (a), 101 points, every point evaluated), alpha and beta stay within one SD
    of their all-window values in every phase, mu in the active phase (largest departure 0.122
    against an SD of 0.197) and z in the active and passive phases. In NNI (a) z departs by 0.083
    against an SD of 0.058. In the passive and NNI phases mu has no grid point with 10 sessions
    contributing (at most 7 and 6, against 32 active), so the criterion, which asks for stability
    "at every grid point with at least 10 sessions contributing", holds vacuously there. Passive
    and NNI mu are therefore not actually tested; only 1.7% of windows pass the r^2 rule. z alone
    fails, so three of four exponents hold, which is partially reproduced. The NNI z failure is
    narrow; its departure of 0.083 is the same at every start, and whether it fails depends only on
    the SD at the start of the grid. The 99th percentile start (6.51) gives the same as 7; the 99.9th
    percentile start (10.43), and CV (b) from 8.55 and 10.30, give reproduced, as z stays within one
    SD there. On thresholds 4 to 12 in steps of 0.5 (CV (a)) NNI z departs by 0.083 against an SD of
    0.056 (partially reproduced). Counting an exponent with no evaluable point as not shown stable
    (the convention of rounds 1 and 2) would give not reproduced from 7 and from the 99th
    percentile. Question for the authors, as for fig3c-scaling-hit-rate-higher. What is
    kappa_surr_max, the start of the Figure S3 range?
  deviations:
  - The grid from kappa_surr_max (O6) is empty under CV (a) and (c). The grid starts disagree (7 and
    the 99th percentile give partially reproduced, the 99.9th percentile reproduced), so the paper's
    value of about 7 for kappa_surr_max, read from Figures 3C, 3D and 4A (claims file, M4), is
    adopted as an assumption.
  - CV reading (a) is adopted as an assumption, as for fig3a-kurtosis-broader-than-surrogate.
  - The criterion is applied as written. An exponent with no grid point where 10 sessions
    contribute meets the condition vacuously (round 3; the outcome was not reproduced in rounds 1
    and 2, which counted such an exponent as not shown stable).
'''
s=s[:start]+new+s[end:]
open(p,'w').write(s)
EOF
grep -n "figs3\|not reproduced (assumed)\|exponent" attempts/cambrainha-2025-01.yaml | sed -n 1,60p | grep -v "^2[5-9][0-9]:"
```

```
196:- claim: fig4-exponents-active
199:  output: claim:fig4-exponents-active
217:- claim: fig4-exponents-passive
220:  output: claim:fig4-exponents-passive
231:- claim: fig4-exponents-nni
234:  output: claim:fig4-exponents-nni
244:- claim: fig4bc-static-exponents-trend
247:  output: claim:fig4bc-static-exponents-trend
380:    below it, and a fifth (figs3-exponents-stable-with-threshold) at named starts. Question for the authors. Is kappa_surr_max the maximum over every surrogate window of
393:    Question for the authors. Over which K and ranks are the exponents fitted?
518:  - claim: fig4-exponents-active
530:  - claim: fig4-exponents-passive
536:  - claim: fig4-exponents-nni
542:  - claim: fig4bc-static-exponents-trend
551:  - claim: figs3-exponents-stable-with-threshold
677:  - claim: fig4-exponents-active
683:  - claim: fig4-exponents-passive
688:  - claim: fig4-exponents-nni
693:  - claim: fig4bc-static-exponents-trend
699:  - claim: figs3-exponents-stable-with-threshold
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 370,392p attempts/cambrainha-2025-01.yaml; tail -8 attempts/cambrainha-2025-01.yaml; head -30 transcripts/cambrainha-2025/verifier-3-report.md | grep -i "by\|agent" ; ls transcripts/cambrainha-2025
```

```
normalised when the kurtosis is computed (Eq. 5 prints phi_i inside the sum), is the covariance
    or the correlation matrix diagonalised, and how are silent units handled?
- kind: methods_unavailable
  statement: The surrogate maximum kappa_surr_max (about 7 in Figure 3) is, as defined here, set by a
    few windows (34.29 in the active phase, 24.45 to 35.46 over seeds; 13 of 28335 surrogate windows
    above 15), which leaves every plotted threshold range empty. The active maximum (34.29) comes from
    a window with 182 active units. The all-phase maximum (48.34) comes from a passive window of
    sub-545994 with 87 active and 84 silent units, and the next value (36.50) from a window of the
    same session with 12 active units; with at least 128 active units the all-phase maximum falls to
    34.29. Four claims are judged with the range started at every threshold
    below it, and a fifth (figs3-exponents-stable-with-threshold) at named starts. Question for the authors. Is kappa_surr_max the maximum over every surrogate window of
    all sessions, one surrogate per window, or another summary?
- kind: methods_unavailable
  statement: The CV of Appendix 1 ("of the activity across the window") is not defined. The CV of
    the population count never exceeds 5 here (no window excluded), the pooled unit-bin CV excludes
    209 of 11639 active windows, and the mean unit CV excludes 9702. Question for the authors. Which
    activity is the CV computed on?
- kind: methods_unavailable
  statement: The real-space details are not given. The K range of the fits, how P_silence is
    averaged over clusters, which spectra enter the fit of mu, and the r^2 rule (which only 1.7% of
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> attempts/cambrainha-2025-01.yaml <<'EOF'
- date: 2026-11-27
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The change of outcome proposed for figs3-exponents-stable-with-threshold after round 2
    and the notebook cells behind it (cells 81 to 83), with the claims file and the paper's full
    text. Report in transcripts/cambrainha-2025/verifier-3-report.md.
  results:
  - claim: figs3-exponents-stable-with-threshold
    agrees: true
    outcome: partially_reproduced
    reason: Agrees, provided it stays marked as assumed. Cell 81 applies the criterion as written
      (SD across sessions at the grid start, at least 10 sessions per point, every phase). alpha and
      beta hold in all three phases, active mu holds (0.122 against 0.197), active and passive z hold,
      and NNI z fails (0.083 against 0.058). Passive and NNI mu have no point with 10 sessions (at
      most 7 and 6), so the condition holds vacuously, and three of four exponents hold. The literal
      reading came from the verifier's round-2 report, not from the author, and under it no start
      gives not reproduced. The outcome still depends on the start of 7 and on CV (a), so `assumed`
      must be kept. The notes should keep that passive and NNI mu are not actually tested (1.7% of
      windows pass the r^2 rule) and that the NNI z failure is narrow, depending only on the SD at
      the grid start. No misreading of the paper by the claims file.
    response: Changed to partially_reproduced, `assumed` kept, `proposed` removed. The notes and
      deviations now apply the criterion as written, say that passive and NNI mu are not actually
      tested and that the NNI z failure depends only on the SD at the grid start. The notebook
      conclusions and summary, the README and the attempt notes are updated to match.
EOF
grep -n "figs3\|not reproduced (assumed)" -n entries/cambrainha-2025/README.md
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  cat entries/cambrainha-2025/README.md; grep -n "^  [a-z_]*:\|^[a-z_]*:" entries/cambrainha-2025/entry.yaml
```

```
# Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025) from dandiset 000713

Tests the findings of [Cambrainha et al. (2025)](https://doi.org/10.1103/w49n-2vz8), "Criticality
at Work: Scaling in the Mouse Cortex Enhances Performance", on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual
Behavior Neuropixels data. For each 30-s window of V1 spiking it computes the kurtosis after
momentum-space coarse graining and an ISI-shuffled surrogate, relates it to the hit rate of the
change-detection task, compares the active, passive and non-natural image phases, and fits the
real-space renormalization exponents.

| Claim | Outcome |
|---|---|
| 62 sessions (44 mice) have more than 128 V1 units | Not reproduced |
| Kurtosis spans a broad range above the surrogates, lowest surrogates around 6 | Partially reproduced (assumed) |
| Hit rate over scaling windows is higher than over no-scaling windows and the shuffle | Not reproduced (assumed) |
| Hit rate over scaling windows rises with the threshold | Not reproduced (assumed) |
| Relative performance gain reaches 24% | Not reproduced |
| Similar results with 10-s and 60-s windows | Not reproduced |
| Similar results with strictly sorted units (43 sessions) | Not reproduced (assumed) |
| More windows above threshold in active than passive than non-natural images | Not reproduced (assumed) |
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='entries/cambrainha-2025/README.md'
s=open(p).read()
s=s.replace("| Exponents stable with the kurtosis threshold | Not reproduced (assumed) |","| Exponents stable with the kurtosis threshold | Partially reproduced (assumed) |")
old="""stability of the exponents, is judged from a few named starts, which disagree, and from the paper's
value of about 7; a change of its outcome to partially reproduced, under a literal reading of its
criterion, is proposed for a third verification round. Over"""
new="""stability of the exponents, is judged from a few named starts, which disagree, and from the paper's
value of about 7, from which it is partially reproduced (the exponent mu is not actually tested in
the passive and non-natural image phases, as too few sessions have a fit). Over"""
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
python - <<'EOF'
import json
nb=json.load(open('entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if c['cell_type']=='markdown' and ('figs3' in src or 'propos' in src or 'exponent' in src.lower()):
        print('=====',i, c.get('metadata',{}).get('tags'))
        print(src[:4000])
EOF
```

```
===== 0 None
# Reproducing Cambrainha et al. (2025) from dandiset 000713

Paper. Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), "Criticality at Work: Scaling in the Mouse Cortex Enhances Performance", PRX Life, doi:10.1103/w49n-2vz8. The claims file (`claims/cambrainha-2025.yaml`) was written from the arXiv preprint 2410.23508 version 2 (15 Sep 2025), with its Appendix and Supplemental Material; codes M1 to M8 and O1 to O11 below refer to the method notes at its top.

Dataset. DANDI:000713 (Allen Institute, Visual Behavior Neuropixels), version 0.240702.1725 (doi:10.48324/dandi.000713/0.240702.1725). The paper cites the Allen dataset (its ref. 60) without a DANDI version; this is the only published version of the dandiset, and its draft has not changed since (both modified 2024-07-02), so it is pinned as the most recent published version. The files are streamed from the archive; nothing is downloaded.

What is read. Per session file: the units table (peak channel, quality metrics, spike times of V1 units only), the electrodes table (structure of each channel), the stimulus presentation tables (stimulus blocks, image onsets and omitted flashes) and the trials table. The probe LFP files are not read.

| claim | tested or blocked |
|---|---|
| sessions-selected | tested |
| fig3a-kurtosis-broader-than-surrogate | tested |
| fig3c-scaling-hit-rate-higher | tested |
| fig3c-hit-rate-rises-with-threshold | tested |
| fig3d-relative-gain-24 | tested |
| figs1-other-window-lengths | tested |
| figs2-strict-units | tested |
| fig4a-active-most-scaling | tested |
| fig4-exponents-active | tested |
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i in [81,82]:
    c=nb['cells'][i]
    print('=====',i,c['cell_type'],c.get('metadata'))
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('--out--', ''.join(o.get('text',''))[-3000:])
EOF
```

```
===== 81 code {'tags': ['claim:figs3-exponents-stable-with-threshold']}


def stable_eval(cv, g, reading=("a", "a", "a"), phases=("active", "passive", "nni_a")):
    """The criterion at every point of the grid g (session values computed once per point)."""
    rows = []
    for ph in phases:
        base = SV[(ph, cv, reading, "a")]
        per = [session_values(ph, cv, reading, "a", kmin=th) for th in g]
        for e in EXP:
            allv = base[e].mean()
            sd = per[0][e].std() if len(g) and len(per[0]) else np.nan
            dep = [abs(s_[e].mean() - allv) for s_ in per if len(s_) and s_[e].notna().sum() >= 10]
            most = max([int(s_[e].notna().sum()) for s_ in per if len(s_)] or [0])
            worst = max(dep) if dep else 0.0
            rows.append(dict(cv=cv, phase=ph, exponent=e, all_windows=allv, sd_at_lo=sd, points=len(dep),
                             most_sessions=most, largest_departure=worst,
                             within=bool(len(dep) > 0 and worst <= sd)))
    return pd.DataFrame(rows)

[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|argparse\|add_parser\|'all'\|\"all\"" tools/entry.py | head -60
```

```
47:import argparse
77:    def __init__(self):
80:    def error(self, where, message: str) -> None:
85:def dataset_id(record: dict) -> str | None:
94:def dataset_ids(record: dict) -> list[str]:
99:def claims_paths() -> list[Path]:
105:def claims_target(data: dict) -> tuple:
110:def lookup(index: dict, attempt: dict):
119:def schema(name: str) -> Draft202012Validator:
130:def _parsed(text: str):
138:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
144:def load(report: Report, path: Path):
152:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
161:def _plain(value):
172:def code_of(notebook_path: Path) -> str:
179:def check(entry_dir: Path) -> Report:
467:def _local_data(code: str, start: int) -> bool:
480:def _derivation_checks(report: Report, where, code: str) -> None:
499:def python_of(entry_dir: Path) -> str:
513:def set_python(entry_dir: Path, version: str) -> None:
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 593,682p tools/entry.py; sed -n 740,800p tools/entry.py
```

```
def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
    the run left it, each within the time limit asked for now, and not older than REUSE_DAYS. Else None."""
    try:
        stamp = json.loads((output_dir / STAMP).read_text())
        entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la executed/cambrainha-2025/ 2>&1; cat executed/cambrainha-2025/result.json 2>&1; grep -rn "seconds\|minutes" transcripts/cambrainha-2025/author-revise-2-report.md | head
```

```
total 460
drwxr-xr-x 3 runner runner   4096 Nov 27 14:47 .
drwxr-xr-x 3 runner runner   4096 Nov 27 14:58 ..
-rw-r--r-- 1 runner runner    325 Nov 27 14:47 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 27 14:21 .venv
-rw-r--r-- 1 runner runner 448577 Nov 27 14:47 reproduce_cambrainha_2025.ipynb
-rw-r--r-- 1 runner runner    179 Nov 27 14:47 result.json
{
 "entry": "cambrainha-2025",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_cambrainha_2025.ipynb",
   "ok": true,
   "seconds": 1510,
   "error": null
  }
 ]
}
```

**Agent**

Applied the verifier's agreed change in the attempt record and README; now updating the notebook's markdown, then re-running (the last run took about 25 min).

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
p='entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb'
raw=open(p).read()
nb=json.loads(raw)
def setsrc(i,old,new):
    c=nb['cells'][i]; s=''.join(c['source']); assert old in s,(i,old); s=s.replace(old,new)
    lines=s.split('\n'); c['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
setsrc(11,"from 7 and from the 99th percentile it is not reproduced, from the 99.9th percentile partially reproduced.",
 "from 7 and from the 99th percentile it is partially reproduced, from the 99.9th percentile reproduced.")
c=nb['cells'][83]
s83="""**Result: partially reproduced**, resting on CV (a) and on the grid start of 7, the paper's value of kappa_surr_max (M4), both assumptions. The criterion's grid from kappa_surr_max (34.29) is empty under CV (a) and (c). From 7 to 12 (101 points, every point evaluated), alpha and beta stay within one SD of their all-window values in every phase, mu in the active phase (largest departure 0.122 against an SD of 0.197), and z in the active and passive phases; in NNI (a), z departs by 0.083 against an SD of 0.058. In the passive and NNI phases mu has no grid point with 10 sessions contributing (at most 7 and 6, last cell), so the criterion, which asks for stability "at every grid point with at least 10 sessions contributing", holds vacuously there (verifier, rounds 2 and 3). z alone fails, so three of four exponents hold, which is partially reproduced. The starts disagree: from the 99th percentile (6.51) the outcome is the same, from the 99.9th (10.43) and under CV (b) z also holds (reproduced; last cell, column `verdict_literal`).

Two caveats. Passive and NNI mu are not actually tested, since only 1.7% of windows pass the r^2 rule, so the outcome rests partly on a condition that holds vacuously. The NNI z failure is narrow: its departure of 0.083 is the same at every start, and whether it fails depends only on the SD at the start of the grid. The verdicts printed in the cell above (and in the column `verdict_no_point_fails` of the last cell) count an exponent with no evaluable point as not shown stable, the convention of rounds 1 and 2, which the criterion does not state; under it the grid from 7 gives not reproduced."""
lines=s83.split('\n'); c['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
setsrc(84,"| figs3-exponents-stable-with-threshold | not reproduced (assumed) |","| figs3-exponents-stable-with-threshold | partially reproduced (assumed) |")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb
```

```
entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-)
```

**Agent calls Bash**

```bash
cd  sed -i 's/The verdicts printed in the cell above (and/The verdicts printed two cells above (and/' entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb; grep -n "propos\|third verification\|third round" entries/cambrainha-2025/* attempts/cambrainha-2025-01.yaml | grep -v "^attempts.*verif" | cut -c1-250
```

```
attempts/cambrainha-2025-01.yaml:715:      partially reproduced is proposed (`proposed`), for a third round. The convention is now stated
attempts/cambrainha-2025-01.yaml:772:  reviewed: The change of outcome proposed for figs3-exponents-stable-with-threshold after round 2
attempts/cambrainha-2025-01.yaml:789:    response: Changed to partially_reproduced, `assumed` kept, `proposed` removed. The notes and
```

**Agent calls Bash**

```bash
cd  grep -rln "cambrainha" summaries questions papers 2>/dev/null; grep -rn "figs3" questions/cambrainha-2025.yaml 2>/dev/null | cut -c1-200
```

```
papers/keys.yaml
29:    figs3-exponents-stable-with-threshold.
36:    session counts of the mu tests and for figs3-exponents-stable-with-threshold, where mu has no
```

**Agent calls Bash**

```bash
cd  sed -n 25,40p questions/cambrainha-2025.yaml; python tools/entry.py check entries/cambrainha-2025
```

```
0.85 that the paper uses to discard poor fits. Does the paper's fit of Eq. 9 cover the whole
    spectrum, or only its upper ranks (for example ranks up to K/2, as in other phenomenological
    renormalization analyses), so that O9 should name that reading? The question bears on
    fig4-exponents-active, fig4-exponents-passive, fig4-exponents-nni and
    figs3-exponents-stable-with-threshold.
  passage: The spectrum of eigenvalues of the covariance matrix [Eq. 2] when ordered in descending
    order should follow lambda = A (K/rank)^mu. (Eq. 9) ... Time windows with a fit quality of r2 <
    0.85 for this power-law have their corresponding exponent discarded (Appendix 4c)
  why: With ranks 1 to K/2, 99.9% of windows pass the r^2 rule and mu is 1.06 in the active phase,
    against 1.58 under reading (a) and 0.73 in the paper. Here it does not change any outcome, as mu
    stays outside tolerance, but it decides how many sessions carry a mu, which matters for the
    session counts of the mu tests and for figs3-exponents-stable-with-threshold, where mu has no
    threshold with 10 sessions under the claims file's readings.
0 error(s)
```

**Agent**

Checks pass. Running the full entry now.

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/cambrainha-2025 2>&1 | tail -20; date -u
```

```
Fri Nov 27 15:00:09 UTC 2026
Installed kernelspec registry-cambrainha-2025 in executed/cambrainha-2025/.venv/share/jupyter/kernels/registry-cambrainha-2025
0 error(s)
pass  reproduce_cambrainha_2025.ipynb  (1599 s)
Fri Nov 27 15:26:57 UTC 2026
```

**Agent**

Verify that the executed figs3 outputs still match the numbers quoted.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
c=nb['cells'][82]
for o in c.get('outputs',[]): print(''.join(o.get('text','')))
EOF
```

```
cv   start verdict_no_point_fails failing      verdict_literal failing_literal                      no_point
 b  O6 (a)   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 b  O6 (b)   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 a paper 7         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 a     p99         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 a   p99.9   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 c paper 7         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 c     p99         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 c   p99.9   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 a 4 to 12         not_reproduced    mu,z partially_reproduced               z                      nni_a:mu

most sessions with a mu at any grid point, start 7, cv a:
  phase  points  most_sessions
 active      64             32
passive       0              7
  nni_a       0              6
```

**Agent**

Round 3 is recorded and the entry re-ran cleanly: the notebook passed in 1599 s and `tools/entry.py` found 0 errors. Nothing is committed.

**Outcome changed**
- `figs3-exponents-stable-with-threshold` goes from not reproduced to **partially reproduced**, still marked `assumed: true`, and `proposed` is removed. The verifier agreed on condition that it stays marked as assumed, because the outcome rests on CV (a) and on starting the grid at 7.
  - From 7 to 12, only NNI z fails (0.083 against an SD of 0.058). Passive and NNI μ pass only because no grid point has 10 sessions, so the condition holds vacuously.
  - The notes now state the verifier's two caveats. Passive and NNI μ are not actually tested, since only 1.7% of windows pass the r² rule. The NNI z failure is narrow and depends only on the SD at the start of the grid.
  - The deviations now apply the criterion as written.
  - The re-run printed the same verdicts as before. Starting at 7 or the 99th percentile gives partially reproduced; starting at the 99.9th percentile or using CV (b) gives reproduced.
  - In those reproduced cases, active μ also has no point with 10 sessions, so μ is vacuous in every phase there.

**Proposals still standing:** none. This was the only proposal.

**Other updates**
- In the notebook, the "How readings decide" section, the result cell for this claim and the summary table now match the new outcome.
- The verdict printed in the cell tagged for this claim (cell 81) still uses the old rule, under which an exponent with no evaluable point fails. The literal verdict is in the next cell. I left the code alone because the verifier reviewed those cells as they are; the result text explains which column is which.
- The README table and paragraph are updated.
- Round 3 is added under `verifications` in the attempt record: agreed, partially reproduced, the verifier's reason and my response.

## End of run

23 turns, 29 minutes, $0.68 at API prices, result: success.
