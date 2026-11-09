# crcns-fcx-2 · recorder · run 42572326770

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/crcns-fcx-2/ claims/crcns-fcx-2/; python tools/readme_row.py crcns-fcx-2; cat attempts/crcns-fcx-2-johnson-2018-01.yaml; grep -n -A12 '"CRCNS:fcx-2"' targets/dandisets.json
```

```
<persisted-output>
Output too large (48.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8dd292e5-a789-471e-bdc1-58312530e32d/tool-results/b28d69ged.txt

Preview (first 2KB):
docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md
docs/pilot-notes/crcns-apl-1-bruno-2017-01.md
docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
docs/pilot-notes/crcns-hc-28-jadhav-2016-01.md
docs/pilot-notes/crcns-hc-13-yu-2017-01.md
claims/crcns-fcx-2/:
10.1371-journal.pbio.2004274.yaml

transcripts/crcns-fcx-2/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/8dd292e5-a789-471e-bdc1-58312530e32d/tool-results/b28d69ged.txt | tail -n +30
```

```
id: crcns-fcx-2-johnson-2018-01
dataset:
  archive: crcns
  id: fcx-2
  version: unversioned
  doi: 10.6080/K0VX0DQD
paper: doi:10.1371/journal.pbio.2004274
date: 2026-11-08
entry: crcns-fcx-2-johnson-2018
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/42521152357
[... 351 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,900p /home/runner/.claude/projects/-home-runner-work-encore-encore/8dd292e5-a789-471e-bdc1-58312530e32d/tool-results/b28d69ged.txt
```

```
notes: >-
    Blocked for the reason given under pac-mtl-spatial (no defensible selection of phase-directing
    units). On the code's selection (not judged; 49 PFC and 47 OFC electrodes) the PFC spatial model
    has a condition x frequency effect below 0.05/7 (p = 8.3e-05, surrogate a).
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-mtl-pfc-spatial
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-mtl-pfc-spatial
  notes: >-
    Blocked for the reason given under pac-mtl-spatial. On the code's selection (not judged; 105 MTL
    to PFC pairs) the spatial condition effect is p = 0.23 (surrogate a).
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-mtl-pfc-temporal
  outcome: blocked
[... 481 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 900,1100p /home/runner/.claude/projects/-home-runner-work-encore-encore/8dd292e5-a789-471e-bdc1-58312530e32d/tool-results/b28d69ged.txt
```

```
the real data (56%), and its selection rates are of the order of the paper's counts of
    phase-directing units (31% to 49%). The Methods' PSI passes 0% to 0.1% with trials shuffled.
- kind: code_mismatch
  statement: >-
    subtracterp.m with ncond = 3 selects the temporal trials by trialinfo column 5 == 2 (the delay
    length column, 900 or 1150), so the temporal condition is empty; pacanalysis.m sizes its
    amplitude matrix with an undefined variable `freq`; and dirpac_compute.m calls pacanalysis with
    six arguments while it takes four, so the deposited PAC scripts cannot run as given.
- kind: paper_inconsistency
  statement: >-
    The Methods describe PSI from sliding 3-cycle windows (dt = 3/f) at 3 to 7 Hz on 900 ms segments;
    a 3-cycle window at 3 Hz is 1 s long and cannot be placed in the segment. The deposited code uses
    one Hanning window over the segment.
- kind: paper_inconsistency
  statement: >-
    The behavioural models are said to have "3 condition-fixed effects" but are reported as F(1,28);
    with one value per subject and condition, F(1,28) is what condition as a single numeric term
    gives, and on summary_file.csv that reading gives the paper's p > 0.12 for response time.
- kind: methods_unavailable
  statement: >-
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in crcns-fcx-3-johnson-2019-01 crcns-apl-1-bruno-2017-01 crcns-ssc-10-lemessurier-2019-01 crcns-hc-28-jadhav-2016-01 crcns-hc-13-yu-2017-01; do echo "== $f"; cat docs/pilot-notes/$f.md; echo; cat summaries/$f.md 2>/dev/null; echo; done; head -5 docs/pilot-notes/001754-knierim-2000-02.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
  if 'fcx-2' in json.dumps(x): print(json.dumps(x,indent=1))"
```

```
<persisted-output>
Output too large (46KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8dd292e5-a789-471e-bdc1-58312530e32d/tool-results/b7g2rac56.txt

Preview (first 2KB):
== crcns-fcx-3-johnson-2019-01
# crcns-fcx-3, Johnson et al. 2019

Six claims reproduced, four partially, seven not reproduced and none blocked;
five outcomes rest on an assumption, `erp-no-condition-difference`,
`power-low-frequencies`, `fig4c-alpha-beta-shift`,
`fig5a-spatiotemporal-bidirectional` and `fig5b-alpha-beta-no-sustained`. The
first verification round agreed with all 17 outcomes as they stood, the second
agreed with 16 and disagreed on fig4c, and a third round, on the three changes
proposed after the second (fig4c to not reproduced, fig5a-spatiotemporal to
reproduced, fig5b to partial), agreed with all three. CRCNS does not version
data sets, so the version is recorded as unversioned with the data set's DOI
(10.6080/K06971S9) and the MD5 sums in the notebook header. The paper, Johnson,
King-Stephens, Weber, Laxer, Lin and Knight in Frontiers in Systems
Neuroscience (12:65), records intracranial EEG over lateral prefrontal (PFC)
and parietal cortex in seven adults with epilepsy during a visuospatial working
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8dd292e5-a789-471e-bdc1-58312530e32d/tool-results/b7g2rac56.txt"
}
```

```
1	== crcns-fcx-3-johnson-2019-01
2	# crcns-fcx-3, Johnson et al. 2019
3	
4	Six claims reproduced, four partially, seven not reproduced and none blocked;
5	five outcomes rest on an assumption, `erp-no-condition-difference`,
6	`power-low-frequencies`, `fig4c-alpha-beta-shift`,
7	`fig5a-spatiotemporal-bidirectional` and `fig5b-alpha-beta-no-sustained`. The
8	first verification round agreed with all 17 outcomes as they stood, the second
9	agreed with 16 and disagreed on fig4c, and a third round, on the three changes
10	proposed after the second (fig4c to not reproduced, fig5a-spatiotemporal to
11	reproduced, fig5b to partial), agreed with all three. CRCNS does not version
12	data sets, so the version is recorded as unversioned with the data set's DOI
13	(10.6080/K06971S9) and the MD5 sums in the notebook header. The paper, Johnson,
14	King-Stephens, Weber, Laxer, Lin and Knight in Frontiers in Systems
15	Neuroscience (12:65), records intracranial EEG over lateral prefrontal (PFC)
16	and parietal cortex in seven adults with epilepsy during a visuospatial working
17	memory task of 120 trials split between identity, spatial and temporal
18	conditions, and reports that accuracy does not differ by condition while
19	identity responses are slower, that ERPs do not differ between conditions,
20	that processing-interval power differs by condition in most subjects, mostly at
[... 598 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B2 -A12 'fcx-2' targets/dandisets.json | head -40; wc -w transcripts/crcns-fcx-2/*-report.md; cat transcripts/crcns-fcx-2/author-report.md
```

```
192 transcripts/crcns-fcx-2/answer-report.md
  527 transcripts/crcns-fcx-2/author-answers-report.md
  871 transcripts/crcns-fcx-2/author-report.md
  572 transcripts/crcns-fcx-2/author-revise-1-report.md
  609 transcripts/crcns-fcx-2/author-revise-2-report.md
  493 transcripts/crcns-fcx-2/claims-check-report.md
  557 transcripts/crcns-fcx-2/claims-report.md
 1554 transcripts/crcns-fcx-2/verifier-1-report.md
 1310 transcripts/crcns-fcx-2/verifier-2-report.md
 6685 total
I tested all 21 claims on fcx-2. Five are reproduced and 16 are not; none are blocked. The entry passes `check`, the full notebook ran in 35.5 minutes from a clean environment, and the handover package is built. Nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| behavior-proficient | reproduced (accuracy 0.792 to 0.967) |
| behavior-no-difficulty-difference | not reproduced (response time differs by condition) |
| electrode-counts | reproduced (36, 116, 102; 9 and 7 subjects) |
| correct-trial-counts | reproduced |
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i 'fcx' targets/dandisets.json | head; for f in answer author-answers verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat transcripts/crcns-fcx-2/$f-report.md; done
```

```
=== answer
I answered the one question and changed the claims file. `claims_check.py` reports 0 problems (21 claims, 21 quotes, 33 statistical values).

**behavior-no-difficulty-difference**: claims file changed. The printed F(1,28) fits only one model: condition entered as a single numeric term on 30 values (10 subjects × 3 conditions), which leaves 28 residual degrees of freedom. The two readings in the criterion would print F(2,27) for a 3-level factor and F(1,18) for one condition against identity, using MATLAB's default residual denominator. The paper ran its statistics in MATLAB.

The criterion now judges the claim on that numeric reading, now (c). It codes identity 1, spatial 2, temporal 3, in the paper's order, and states this as an assumption, since the Methods say only "3 condition-fixed effects and 10 subject-random effects". Readings (a) and (b) are still reported but not judged. The change rests on the printed degrees of freedom, not on the results quoted in the question.

The question has `answered: 2026-11-08`. Only `claims/crcns-fcx-2/` and `questions/crcns-fcx-2.yaml` are modified, and nothing is committed. `git status` also lists untracked files at the repo root (dotfiles, `.idea`, `.vscode`, `scripts`). I didn't create them and left them alone.
=== author-answers
The one answered question flipped behavior-no-difficulty-difference from not reproduced to reproduced. That result depends on which of the dataset's two response-time sources is used. The entry passes `check`, the full notebook ran clean in 31.6 minutes with no errors, and the handover package is built. Nothing is committed or pushed, and I did not verify my own work.

## The question

behavior-no-difficulty-difference: should the criterion include the reading where condition enters the models as one numeric term?

**What the answer changed.** The reader amended the claims file. The criterion now judges the claim on reading (c): condition as one numeric term, coded identity 1, spatial 2, 
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i 'crcns' targets/dandisets.json | head -5; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
print(type(d), (list(d)[:5] if isinstance(d,dict) else d[:1]))
E
ls targets/
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
crcns.json
dandisets.json
description_papers.yaml
dryad.json
ebrains.json
figshare.json
openneuro.json
pilot.yaml
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('targets/crcns.json'))
print(list(d))
for t in d.get('targets',[]):
    if 'fcx-2' in json.dumps(t): print(json.dumps(t,indent=1)[:3000])
E
grep -n -i 'catalystneuro\|crcns.json\|dandisets.json' docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md | head
```

```
['schema_version', 'archive', 'generated', 'source', 'note', 'counts', 'targets']
{
 "id": "fcx-2",
 "name": "Intracranial EEG recordings of medial temporal, lateral frontal, and orbitofrontal regions in 10 human adults performing a visuospatial working memory task.",
 "url": "http://crcns.org/data-sets/fcx/fcx-2",
 "doi": "10.6080/K0VX0DQD",
 "published_version": null,
 "asset_count": 18,
 "size_gb": 12.41,
 "data_standards": [
  "compressed archives"
 ],
 "species": [
  "Human"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml; head -60 $f; grep -n -E '^\s*- id:|^\s+(id|figure|location|source|where|section):' $f | head -80; wc -l $f
```

```
# Claims for Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin & Knight (2018),
# PLoS Biology 16, e2004274, "Dynamic frontotemporal systems process space and time in working
# memory", doi:10.1371/journal.pbio.2004274, on CRCNS data set fcx-2 (doi:10.6080/K0VX0DQD).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, open access, PMC5895055, as supplied under paper/ (Europe PMC
# full-text XML, flattened): Introduction, Results, Discussion, Materials and methods, the legends
# of Figures 1 to 8 and the captions of the supporting information. No PDF was supplied. The
# supporting information is S1 and S2 Fig (legends read) and S1 to S4 Table (DOCX files: group
# mixed-effects model outputs with degrees of freedom). Only the captions of the four tables were
# supplied; their contents were not read. Every claim below rests on a p-value the main text
# prints, so no claim needs the tables, but the full model outputs (degrees of freedom, F values
# of the PAC models) they hold were not available. Values shown only in figures (the percentages
# of Fig 4B, the grand means of Fig 8A, the per-subject PSI of Fig 3B) were not read.
#
# Code. The Data Availability statement says the "custom-built MATLAB codes" are deposited with
# the data on CRCNS (doi:10.6080/K0VX0DQD). The data descriptor says they are in the data set's
# analysis_scripts directory (one <metric>_compute script per analysis, with subfunctions, using
# FieldTrip). Being among the data set's files, they were not read in this run. Where a criterion
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml; sed -n 100,124p $f; python - <<E
import yaml
d=yaml.safe_load(open('$f'))
for c in d['claims']:
    print(c['id'],'|',c.get('source'),'|',str(c.get('statement'))[:400]); print()
E
```

```
#   removed per condition, theta phase in the M8 band and amplitudes at 9.5 to 152.5 Hz (128 Hz
#   Oslo) by Hilbert, circular-linear Pearson correlation across the trials of a condition at
#   each time and amplitude frequency (PAC section, paragraph 2). Null, 100 shuffles; z as in M5.
#   The shuffle "randomly shuffled the amplitude frequencies across trials" is not fixed.
#   Readings, (a) amplitude values shuffled across trials relative to the phase (trial labels
#   permuted), (b) the amplitude frequency labels shuffled within each trial. Down-sampled to
#   50 ms.
# M10. PAC group models. Per region and directional system, z-scored PAC in two models (spatial
#   against identity, temporal against identity), fixed effects condition (2 levels), amplitude
#   frequency (16 levels, 9.5 to 128 Hz) and time (19 levels), all interactions, random effects
#   subject and electrode or pair. Direction models add direction (2 levels) as a fourth fixed
#   effect, on the MTL -> frontal and frontal -> MTL data together. Significance at Bonferroni
#   0.05/m, m the number of main and interaction effects (7 in three-factor models, 15 in the
#   four-factor direction models) (PAC section, last paragraph). Not fixed: whether frequency and
#   time enter as categorical factors (read as categorical, from "16 amplitude frequency" and "19
#   time-fixed effects") and the random-effects structure (random intercepts, pairs nested in
#   subject). The direction of a condition effect is read from the sign of the condition
#   coefficient or the condition means (spatial or temporal minus identity).
schema_version: 2
dataset:
[... 46 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-fcx-2-johnson-2018-01.md",
 "content": "# crcns-fcx-2, Johnson et al. 2018\n\nFive claims reproduced, none partially, seven not reproduced and nine blocked,\nall for methods underspecified; three outcomes rest on an assumption,\n`behavior-no-difficulty-difference`, `erp-no-condition-difference` and\n`psi-theta-shift`. The first verification round agreed with 19 of the 21\noutcomes and disagreed on behavior-no-difficulty-difference and psi-theta-shift,\nboth of which it held partial, and the second agreed with all 21, though it\nquestioned the label of the nine blocked claims; nothing was proposed after the\nsecond, so there was no third round. CRCNS does not version data sets, so the\nversion is recorded as unversioned with the data set's DOI (10.6080/K0VX0DQD)\nand the MD5 sums in the notebook header. The paper, Johnson, Adams, Solbakk,\nEndestad, Larsson, Ivanovic, Meling, Lin and Knight in PLoS Biology (16,\ne2004274), records intracranial EEG from the medial temporal lobe (MTL), lateral\nprefrontal cortex (PFC) and orbitofrontal cortex (OFC) in ten adults with\nepilepsy during a visuospatial working memory task of 120 trials split between\nidentity, spatial and temporal conditions, and reports that accuracy and\nresponse time do not differ by condition, that ERPs do not either, that theta\npower is sustained over encoding and delay, that phase locking peaks in theta\nwithin the MTL and between MTL and frontal electrodes, that theta phase slope\nindex (PSI) shifts from frontal leads before the test cue towards MTL leads\nafter it, that theta phase comes to lead higher-frequency amplitude after the\ntest cue in counts of electrodes and pairs, and that theta phase-amplitude\ncoupling (PAC) carries spatial and temporal information from the MTL to frontal\ncortex; the data set holds, per subject, the filtered continuous data, the\npreprocessed bipolar segments with trial information, electrode MNI\ncoordinates, a per-trial table, a behaviour table, the channels analysed per\nregion and the analysis scripts. The claims were written from the version of\nrecord (PMC5895055) as flattened Europe PMC XML with the legends of Figures 1\nto 8 but without a PDF, the contents of S1 to S4 Table or the analysis\nscripts, for 21 claims. Reproduced are `behavior-proficient` (0.792 to 0.967),\n`electrode-counts` (36, 116 and 102, exact), `correct-trial-counts`,\n`plv-theta-peak`, on a rule one subject per group satisfies, and\nbehavior-no-difficulty-difference, which holds only with the response times of\n`docs/summary_file.csv` (F(1,28) = 2.41, p = 0.13), while the trial tables'\nresponse times give F(1,28) = 12.33, p = 0.0015. Not reproduced are\nerp-no-condition-difference (1 of 254 electrodes significant, 0 with a\nper-trial baseline), `power-theta-sustained` (theta sustained in 1 of 10, 0 of\n9 and 0 of 9 subjects), `power-condition-exclusions` (7 electrodes in 4\nsubjects against 8 in 4), psi-theta-shift, which would be partial in the\ndeposited code's windows, `crossspectral-shift` (1 of 7 systems),\n`phase-directing-counts` (0, 0, 0, 0, 1, 3 and 2 units) and `theta-peak-bands`\n(overlap 4 of 10). Blocked are `crossspectral-equal-strength` and the eight PAC\nclaims, as no defensible selection of phase-directing units is left. The\nauthor's first run had 4 reproduced and 17 not reproduced by its outcome table,\nthough its report gives 5 and 16. The author asked one question of a reader,\nwhether the behaviour criterion should include condition as one numeric term;\nthe reader judged the claim on that reading, which the printed F(1,28) fits,\nand the author-answers run moved behavior-no-difficulty-difference to\nreproduced on it. Round 1 held that every neural outcome rested on an unchecked\ntime axis, that the response times of summary_file.csv were of unknown\nprovenance, that the code's form of PSI gave z SD 27 on independent pink noise,\nthat cross-spectral PSI had not been run with sliding windows and that the ERP\nbaseline was unclear; in reply a delay-jitter test made the trial table's\nwindow placement the main reading, a trial-shuffle calibration showed the\ncode's form passing 57% of units against 56% on real data, which moved the\nnine claims from not reproduced to blocked, the deposited scripts were quoted,\nthe source of the response times was searched (9 of 30 values matched) and the\nsliding-window reading was run. Round 2 raised edge effects under the table's\nplacement, asked the record to say that the paper's numbers would come from the\ncode's windows if the deposited scripts produced them, and found sentences the\noutputs did not support, among them one on the PAC direction patterns; in reply\nan edge check on joined traces left the outcomes as they were, the model was\nrun on the 5 MTL-OFC pairs the sliding windows select (not judged), and the\nsentences were corrected. The notebook ran in 35.5 min at first, with peak\nmemory 5.9 GB, 31.6 min after the author-answers run, 47 min after round 1 and\n53.6 min after round 2. Nothing failed in the final runs; after the last run one\nsentence of the notebook's text was filled in by hand in the source and the\nexecuted copy.\n\nThe data set's derived time axes put each segment's first sample at -1.5 s,\nand that sample is the trial table's epoch start, so the task events lie 1.5 s\nearlier than 0 s suggests; the deposited scripts cut their windows as if 0 s\nwere the event, and the 900 and 1150 ms delay trials part where the table puts\nthe first delay-dependent event (proc ERPs from -0.25 to 0.75 s, p down to\n0.005) and not where the scripts' windows put it (p 0.29 to 0.94). The deposited\npsianalysis.m multiplies the Fourier coefficients without conjugating one of\nthem and z-scores per-trial PSI against a null built from trial-averaged\ncoherency; with the conjugate added it passes z > 1.96 for 57% of units with\ntrials shuffled, as many as on the real data (56%), while the Methods' PSI\npasses 0% to 0.1%. subtracterp.m selects the temporal trials by the delay\ncolumn, so that condition is empty, pacanalysis.m uses an undefined variable\nand dirpac_compute.m calls it with six arguments where it takes four, so the\nPAC scripts cannot run as given. The response times of docs/summary_file.csv,\ndescribed as calculated on all correct trials, differ from the trial tables'\nmean over correct trials in 7 of 10 subjects (s1 identity 1948 against 2348\nms), and the paper's condition means are those of the file; its accuracies do\nequal the trial tables. For s10 the trial table's epoch columns are not on the\nderived data's sample grid, and its trialinfo does not equal the table's\ncolumns. The descriptor gives fsample 1000 for the derived structures, where s8\nand s9 are at 512 Hz. The Methods' sliding 3-cycle PSI windows cannot fit a 900\nms segment at 3 Hz, and the behavioural models are described with 3 condition\nfixed effects but reported as F(1,28). Questions are put to the paper's authors:\nhow the behavioural models coded condition and on which response times they\nwere fitted, and which form of PSI and which spectral window produced the\nreported PSI values and phase-directing counts, and whether the analysis windows\nwere cut 1.5 s later on the derived time axes than the trial table places the\nevents.\n\nThe author's points on the protocol: the clock check does not say what to do\nwhen the time axes and the trial table disagree and the data have no\ntask-locked response; it does not say what to do when the Methods describe a\nmethod that cannot run and the code differs; it does not say whether a claim\nwhose selection is empty under the main reading is blocked or may take another\nreading; `docs/archives.md` says to use fsspec, while the files are tar.gz,\nwhich streamed about 5 times faster with requests (46 against 10 MB/s); \"do not\ndownload to disk\" does not address development caches, which were kept in\n`$TMPDIR`, and one 210 MB member was briefly saved while exploring and deleted;\nand judging absence on \"the paper's test alone\" does not help when the paper's\ntest is unclear, so a reader was asked.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-fcx-2-johnson-2018-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat > summaries/crcns-fcx-2-johnson-2018-01.md <<'E'
In this intracranial dataset the paper's behavioural results and the theta peak in medial temporal and frontal phase locking held up, while sustained theta power and the shift of theta directionality after the test cue did not. The directionality result rests on placing windows where the trial table puts the task events; in the deposited code's windows, 1.5 s later, it holds in part. The phase-amplitude coupling findings could not be tested, as the Methods' phase-slope index selects almost no phase-directing units and the code's version selects as many from shuffled data. Equal response times across conditions hold only with the dataset's summary file, not its trial tables. Electrode and trial counts matched.
E
wc -w summaries/crcns-fcx-2-johnson-2018-01.md; git status --short
```

```
113 summaries/crcns-fcx-2-johnson-2018-01.md
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? docs/pilot-notes/crcns-fcx-2-johnson-2018-01.md
?? scripts
?? summaries/crcns-fcx-2-johnson-2018-01.md
```

**Agent**

I wrote both files and committed nothing. One note on the sources: CRCNS:fcx-2 has no entry in `targets/dandisets.json`. Its entry is in `targets/crcns.json`, and its `catalystneuro` field is empty, so the second paragraph does not open with the CatalystNeuro sentence. There was no third verification round, because round 2 proposed no changes. The untracked dotfiles, `.idea`, `.vscode` and `scripts` at the repo root were there before this run, and I left them alone.

**docs/pilot-notes/crcns-fcx-2-johnson-2018-01.md**

# crcns-fcx-2, Johnson et al. 2018

Five claims reproduced, none partially, seven not reproduced and nine blocked, all for methods underspecified; three outcomes rest on an assumption, `behavior-no-difficulty-difference`, `erp-no-condition-difference` and `psi-theta-shift`. The first verification round agreed with 19 of the 21 outcomes and disagreed on behavior-no-difficulty-difference and psi-theta-shift, both of which it held partial, and the second agreed with all 21, though it questioned the label of the nine blocked claims; nothing was proposed after the second, so there was no third round. CRCNS does not version data sets, so the version is recorded as unversioned with the data set's DOI (10.6080/K0VX0DQD) and the MD5 sums in the notebook header. The paper, Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin and Knight in PLoS Biology (16, e2004274), records intracranial EEG from the medial temporal lobe (MTL), lateral prefrontal cortex (PFC) and orbitofrontal cortex (OFC) in ten adults with epilepsy during a visuospatial working memory task of 120 trials split between identity, spatial and temporal conditions, and reports that accuracy and response time do not differ by condition, that ERPs do not either, that theta power is sustained over encoding and delay, that phase locking peaks in theta within the MTL and between MTL and frontal electrodes, that theta phase slope index (PSI) shifts from frontal leads before the test cue towards MTL leads after it, that theta phase comes to lead higher-frequency amplitude after the test cue in counts of electrodes and pairs, and that theta phase-amplitude coupling (PAC) carries spatial and temporal information from the MTL to frontal cortex; the data set holds, per subject, the filtered continuous data, the preprocessed bipolar segments with trial information, electrode MNI coordinates, a per-trial table, a behaviour table, the channels analysed per region and the analysis scripts. The claims were written from the version of record (PMC5895055) as flattened Europe PMC XML with the legends of Figures 1 to 8 but without a PDF, the contents of S1 to S4 Table or the analysis scripts, for 21 claims. Reproduced are `behavior-proficient` (0.792 to 0.967), `electrode-counts` (36, 116 and 102, exact), `correct-trial-counts`, `plv-theta-peak`, on a rule one subject per group satisfies, and behavior-no-difficulty-difference, which holds only with the response times of `docs/summary_file.csv` (F(1,28) = 2.41, p = 0.13), while the trial tables' response times give F(1,28) = 12.33, p = 0.0015. Not reproduced are erp-no-condition-difference (1 of 254 electrodes significant, 0 with a per-trial baseline), `power-theta-sustained` (theta sustained in 1 of 10, 0 of 9 and 0 of 9 subjects), `power-condition-exclusions` (7 electrodes in 4 subjects against 8 in 4), psi-theta-shift, which would be partial in the deposited code's windows, `crossspectral-shift` (1 of 7 systems), `phase-directing-counts` (0, 0, 0, 0, 1, 3 and 2 units) and `theta-peak-bands` (overlap 4 of 10). Blocked are `crossspectral-equal-strength` and the eight PAC claims, as no defensible selection of phase-directing units is left. The author's first run had 4 reproduced and 17 not reproduced by its outcome table, though its report gives 5 and 16. The author asked one question of a reader, whether the behaviour criterion should include condition as one numeric term; the reader judged the claim on that reading, which the printed F(1,28) fits, and the author-answers run moved behavior-no-difficulty-difference to reproduced on it. Round 1 held that every neural outcome rested on an unchecked time axis, that the response times of summary_file.csv were of unknown provenance, that the code's form of PSI gave z SD 27 on independent pink noise, that cross-spectral PSI had not been run with sliding windows and that the ERP baseline was unclear; in reply a delay-jitter test made the trial table's window placement the main reading, a trial-shuffle calibration showed the code's form passing 57% of units against 56% on real data, which moved the nine claims from not reproduced to blocked, the deposited scripts were quoted, the source of the response times was searched (9 of 30 values matched) and the sliding-window reading was run. Round 2 raised edge effects under the table's placement, asked the record to say that the paper's numbers would come from the code's windows if the deposited scripts produced them, and found sentences the outputs did not support, among them one on the PAC direction patterns; in reply an edge check on joined traces left the outcomes as they were, the model was run on the 5 MTL-OFC pairs the sliding windows select (not judged), and the sentences were corrected. The notebook ran in 35.5 min at first, with peak memory 5.9 GB, 31.6 min after the author-answers run, 47 min after round 1 and 53.6 min after round 2. Nothing failed in the final runs; after the last run one sentence of the notebook's text was filled in by hand in the source and the executed copy.

The data set's derived time axes put each segment's first sample at -1.5 s, and that sample is the trial table's epoch start, so the task events lie 1.5 s earlier than 0 s suggests; the deposited scripts cut their windows as if 0 s were the event, and the 900 and 1150 ms delay trials part where the table puts the first delay-dependent event (proc ERPs from -0.25 to 0.75 s, p down to 0.005) and not where the scripts' windows put it (p 0.29 to 0.94). The deposited psianalysis.m multiplies the Fourier coefficients without conjugating one of them and z-scores per-trial PSI against a null built from trial-averaged coherency; with the conjugate added it passes z > 1.96 for 57% of units with trials shuffled, as many as on the real data (56%), while the Methods' PSI passes 0% to 0.1%. subtracterp.m selects the temporal trials by the delay column, so that condition is empty, pacanalysis.m uses an undefined variable and dirpac_compute.m calls it with six arguments where it takes four, so the PAC scripts cannot run as given. The response times of docs/summary_file.csv, described as calculated on all correct trials, differ from the trial tables' mean over correct trials in 7 of 10 subjects (s1 identity 1948 against 2348 ms), and the paper's condition means are those of the file; its accuracies do equal the trial tables. For s10 the trial table's epoch columns are not on the derived data's sample grid, and its trialinfo does not equal the table's columns. The descriptor gives fsample 1000 for the derived structures, where s8 and s9 are at 512 Hz. The Methods' sliding 3-cycle PSI windows cannot fit a 900 ms segment at 3 Hz, and the behavioural models are described with 3 condition fixed effects but reported as F(1,28). Questions are put to the paper's authors: how the behavioural models coded condition and on which response times they were fitted, and which form of PSI and which spectral window produced the reported PSI values and phase-directing counts, and whether the analysis windows were cut 1.5 s later on the derived time axes than the trial table places the events.

The author's points on the protocol: the clock check does not say what to do when the time axes and the trial table disagree and the data have no task-locked response; it does not say what to do when the Methods describe a method that cannot run and the code differs; it does not say whether a claim whose selection is empty under the main reading is blocked or may take another reading; `docs/archives.md` says to use fsspec, while the files are tar.gz, which streamed about 5 times faster with requests (46 against 10 MB/s); "do not download to disk" does not address development caches, which were kept in `$TMPDIR`, and one 210 MB member was briefly saved while exploring and deleted; and judging absence on "the paper's test alone" does not help when the paper's test is unclear, so a reader was asked.

**summaries/crcns-fcx-2-johnson-2018-01.md** (113 words)

In this intracranial dataset the paper's behavioural results and the theta peak in medial temporal and frontal phase locking held up, while sustained theta power and the shift of theta directionality after the test cue did not. The directionality result rests on placing windows where the trial table puts the task events; in the deposited code's windows, 1.5 s later, it holds in part. The phase-amplitude coupling findings could not be tested, as the Methods' phase-slope index selects almost no phase-directing units and the code's version selects as many from shuffled data. Equal response times across conditions hold only with the dataset's summary file, not its trial tables. Electrode and trial counts matched.

## End of run

15 turns, 2 minutes, $1.03 at API prices, result: success.
