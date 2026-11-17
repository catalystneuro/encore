# wirth-2017 · author-revise-3 · run 43489143952

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/wirth-2017/verifier-3-report.md; ls entries/wirth-2017; grep -n "step 6\|^## \|^### " docs/protocol.md | head -50
```

```
Fri Nov 13 19:14:59 UTC 2026
# Round 3 verification: wirth-2017-01, proposed outcome changes

The attempt record has two `proposed` entries: direction-center-vs-periphery and direction-tuning-not-maintained. Both would move to blocked (metadata_insufficient). No other claim carries a proposal.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| direction-center-vs-periphery | blocked (metadata_insufficient), from partially_reproduced (assumed) | Yes | | The numbers in the proposal match cell 42. **Reading (a)** fails both levels. With permuted chunks there are 40 cells, IC p = 0.43 and sparsity p = 0.031. With shifted chunks there are 28 cells, p = 0.095 and 0.016. So both are not higher at p < 0.05, and neither reaches p < 0.001. **Reading (b)** needs the paper's responsive set, and that set needs the point-of-gaze space, which the uncalibrated eye signal cannot give. The three-space stand-in reaches the partial level only with permuted chunks (IC p = 0.045, sparsity p = 0.0074, 59 cells). With shifted chunks IC is p = 0.14. Over all 180 cells neither measure is higher (p = 0.31 and 0.29). A signed-rank result on a subset sets no bound on the result over a superset, so the paper's set could fall at any level, from not reproduced to reproduced. Reading (a) fails and reading (b) cannot be formed, so the "under one reading" criterion cannot be decided. This is the same basis on which landmark-identity-center was verified as blocked (cell 64). The change moves away from the favourable outcome, and the binning choice (about 200 common bins) was fixed before this round, so neither choice was made to reach the result. |
| direction-tuning-not-maintained | blocked (metadata_insufficient), from not_reproduced (assumed) | Yes | | The numbers match cell 45. **Reading (a)** fails on the number of cells tested: 40 (permuted) and 28 (shifted), against 56 ± 5.6. **Reading (b)** cannot be formed without the gaze space. The bounding chec
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 451,562p docs/protocol.md; sed -n 668,720p docs/protocol.md; ls attempts 2>/dev/null | head; find . -path ./node_modules -prune -o -name "*wirth-2017-01*" -print
```

```
### 5. Record the attempt

Write `attempts/<paper>-<nn>.yaml`, numbered after the paper's earlier attempts.

- **`datasets`**: every dataset the attempt used, each with `archive`, `id`,
  the pinned `version`, its `doi` where the archive gives one, and
  `relation` as `papers/datasets/<paper>.yaml` gives it (`primary` or
  `reuses`). Use as many of the paper's datasets as can be loaded.
- **`missing_datasets`**: each dataset the paper's claims rest on that this
  attempt could not use, with `archive` and `id` where it has them, and
  `why` (not in any open archive, not yet converted, unreadable). A missing
  dataset does not stop the attempt: test what the others allow, and block
  each claim that needs a missing one with `dataset_missing`. The site flags
  the attempt, so that a later one can add the dataset.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
  - `reproduced`: the result matches the claim.
  - `partially_reproduced`: the effect is present but weaker, or holds only in
    part.
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/wirth-2017-01.yaml
```

```
<persisted-output>
Output too large (51.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0276ff23-22ab-4fe3-86be-fdf70e65a1d6/tool-results/bxkr3ew31.txt

Preview (first 2KB):
schema_version: 3
id: wirth-2017-01
datasets:
- archive: crcns
  id: hc-21
  version: unversioned
  doi: 10.6080/K0GX48R9
  relation: primary
- archive: crcns
  id: hc-12
  version: unversioned
  doi: 10.6080/K0R49NQV
  relation: primary
paper: doi:10.1371/journal.pbio.2001045
date: 2026-11-13
entry: wirth-2017
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd attempts; grep -n "^- claim\|^  outcome\|proposed\|^[a-z_]*:\|^  blocked_by\|^- round\|^  round" wirth-2017-01.yaml | head -120
```

```
1:schema_version: 3
2:id: wirth-2017-01
3:datasets:
14:paper: doi:10.1371/journal.pbio.2001045
15:date: 2026-11-13
16:entry: wirth-2017
17:provenance:
28:outcomes:
29:- claim: gaze-anticipates-action
30:  outcome: reproduced
62:- claim: gaze-anticipates-landmarks
63:  outcome: reproduced
82:- claim: learning-trials
83:  outcome: reproduced
98:- claim: learning-to-90
99:  outcome: reproduced
111:- claim: probe-transfer
112:  outcome: not_reproduced
133:- claim: probe-faster-criterion
134:  outcome: blocked
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd attempts; sed -n 180,260p wirth-2017-01.yaml; sed -n 330,340p wirth-2017-01.yaml; sed -n 466,475p wirth-2017-01.yaml; sed -n 640,810p wirth-2017-01.yaml
```

```
- claim: multi-space-coding
  outcome: blocked
  blocked_by: metadata_insufficient
  notes: Depends on responsive-cells (the gaze space). Of the 59 cells responsive in the three spaces
    computed, 46 are significant in two or more; cells responsive only in gaze space would add to the
    denominator, so the fraction over the paper's set cannot be bounded above one half.
- claim: direction-center-vs-periphery
  outcome: partially_reproduced
  notebook: reproduce_wirth_2017.ipynb
  output: claim:direction-center-vs-periphery
  notes: For the 40 cells with significant direction IC (reading a, permuted chunks) normalized sparsity
    is higher in the centre than on return paths (median difference 0.020, 25 of 40, Wilcoxon p = 0.031)
    and IC is not (0.012, p = 0.43); with shifted chunks (28 cells) p = 0.016 and 0.095. Reading (a) meets
    neither level. Over the 59 three-space responsive cells, which stand in for reading (b), IC and sparsity
    are both higher with p = 0.045 and 0.0074, the partial level; with shifted chunks (51 cells) IC is
    not (p = 0.14, sparsity p = 0.013). No reading reaches p < 0.001. The outcome rests on the stand-in
    for reading (b) and on permuted chunks. Over all 180 cells with both maps neither is higher (IC p
    = 0.31, sparsity p = 0.29, permuted chunks), so a signed-rank result over the 59 cells puts no bound
    on the result over the paper's responsive set; a change to blocked is proposed.
  deviations:
[... 253 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 810,900p attempts/wirth-2017-01.yaml; grep -n "round\|verifications" tools/entry.py | head -40; ls attempts | xargs -I{} grep -l "proposed\|round: 3" attempts/{} | head
```

```
outcome: not_reproduced
    reason: 'Cell 50: the overall test is significant (p <= 0.00043) and the per-cell counts are 3 to 11,
      against 15 +- 1.5.'
    response: No change.
  - claim: sparsity-gaze-vs-state
    agrees: true
    outcome: blocked
    reason: Agreed, no further comment.
    response: No change.
  - claim: state-space-selectivity
    agrees: true
    outcome: not_reproduced
    reason: 'Agreed as an assumption, which is stated and reasonable: the Results say "randomly shuffling
      periods of spiking activity in time" and the Methods say the 5 s chunks were "randomly shifted";
      under shifted chunks the claim cannot be decided (cell 56), and without the assumption the outcome
      would be blocked. The README row drops the qualifier "permuted chunks; open under shifted chunks".'
    response: Added the qualifier to the README row. Outcome unchanged.
  - claim: landmark-identity-distance
    agrees: true
    outcome: not_reproduced
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -ln "proposed changes\|Round 3\|round 3" attempts/*.yaml | head -3; f=$(grep -ln "reviewed: .*[Pp]roposed" attempts/*.yaml | head -1); echo $f; grep -n "reviewed: .*[Pp]roposed" -A30 $f | head -50
```

```
attempts/bech-2026-01.yaml
attempts/bennett-2024-01.yaml
attempts/brudner-2026-01.yaml
attempts/bech-2026-01.yaml
1245:  reviewed: Round 3. Only the four changes of outcome proposed after round 2 (fig3h-rsc-first-context-discrimination and
1246-    the three fig4b claims), with the re-executed notebook, the claims file and the paper. Report in transcripts/001847/verifier-3-report.md.
1247-  results:
1248-  - claim: fig3h-rsc-first-context-discrimination
1249-    agrees: true
1250-    outcome: blocked
1251-    reason: Cell 76 derives the result from the data. In the ROI version RSC is first and alone under every baseline (50,
1252-      250 and 100 ms) and both exclusion readings; in the smoothed pixel version RSC is first at 40 ms with no tie with the
1253-      50 ms baseline, and RSC and wM1 tie at 50 ms with the 250 ms baseline. The criterion asks for "the outcome … they all
1254-      give, otherwise methods_underspecified", and the two baselines it names give reproduced and partially reproduced, so
1255-      read as written it gives blocked (methods_underspecified). The paper states both baselines (Methods, Computation of
1256-      ΔF/F0, 250 ms for Figures 3 and 4; Methods, Figures 3E&F, 50 ms, whose d' Figure 3H uses), so the claims file reads
1257-      the paper correctly. The proposal gives up a favourable outcome, so it was not chosen to reach a result. Minor, the
1258-      notes say "22.1 GB read in 2.0 min", but this run's cell 76 prints 1.9 min (189 MB/s).
1259-    response: Outcome set to blocked (methods_underspecified) and the proposal removed; as the outcome no longer rests on the
1260-      50 ms baseline, assumed is removed and the deviation now says both baselines are run. The notebook's conclusion and summary,
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/wirth-2017-01.yaml'
s=open(p).read()
old1="""- claim: direction-center-vs-periphery
  outcome: partially_reproduced
"""
new1="""- claim: direction-center-vs-periphery
  outcome: blocked
  blocked_by: metadata_insufficient
"""
assert s.count(old1)==1; s=s.replace(old1,new1)
old2="""- claim: direction-tuning-not-maintained
  outcome: not_reproduced
"""
new2="""- claim: direction-tuning-not-maintained
  outcome: blocked
  blocked_by: metadata_insufficient
"""
assert s.count(old2)==1; s=s.replace(old2,new2)
# notes
o="""    neither level. Over the 59 three-space responsive cells, which stand in for reading (b), IC and sparsity
    are both higher with p = 0.045 and 0.0074, the partial level; with shifted chunks (51 cells) IC is
    not (p = 0.14, sparsity p = 0.013). No reading reaches p < 0.001. The outcome rests on the stand-in
    for reading (b) and on permuted chunks. Over all 180 cells with both maps neither is higher (IC p
    = 0.31, sparsity p = 0.29, permuted chunks), so a signed-rank result over the 59 cells puts no bound
    on the result over the paper's responsive set; a change to blocked is proposed.
"""
n="""    neither level. Reading (b) needs the paper's responsive set, which needs the point-of-gaze space.
    Over the 59 three-space responsive cells, which it contains, IC and sparsity are both higher with
    p = 0.045 and 0.0074, the partial level; with shifted chunks (51 cells) IC is not (p = 0.14, sparsity
    p = 0.013). Over all 180 cells with both maps neither is higher (IC p = 0.31, sparsity p = 0.29, permuted
    chunks), so a signed-rank result over the 59 cells puts no bound on the result over the paper's set,
    which may lie at any level. No set reaches p < 0.001. Reading (a) fails and reading (b) cannot be
    formed, so the claim cannot be decided, as for landmark-identity-center.
"""
assert s.count(o)==1; s=s.replace(o,n)
i=s.index("  proposed:\n    outcome: blocked\n    blocked_by: metadata_insufficient\n    reason: Reading (a) meets")
j=s.index("- claim: direction-tuning-not-maintained")
s=s[:i]+s[j:]
o="""    1e-10). The criterion has no partial level. Reading (a) fails on the number of cells (40 and 28).
    Under reading (b) the outcome rests on the three-space stand-in. The paper's responsive set lies
"""
n="""    1e-10). The criterion has no partial level. Reading (a) fails on the number of cells (40 and 28).
    Reading (b) needs the paper's responsive set, which needs the point-of-gaze space. That set lies
"""
assert s.count(o)==1; s=s.replace(o,n)
o="""    high 3), so over the paper's set the criterion is not excluded; a change to blocked is proposed.
"""
n="""    high 3). A set that meets the criterion and one that fails it (the stand-in) both exist, so the claim
    cannot be decided.
"""
assert s.count(o)==1; s=s.replace(o,n)
i=s.index("  proposed:\n    outcome: blocked\n    blocked_by: metadata_insufficient\n    reason: Reading (a) fails")
j=s.index("- claim: state-space-ic-higher")
s=s[:i]+s[j:]
open(p,'w').write(s)
EOF
grep -n "proposed" attempts/wirth-2017-01.yaml | head; sed -n 186,245p attempts/wirth-2017-01.yaml
```

```
770:      insufficient) is proposed, as reading (b) cannot be formed and reading (a) fails.
783:      The verified outcome is kept, and a change to blocked (metadata insufficient) is proposed.
- claim: direction-center-vs-periphery
  outcome: blocked
  blocked_by: metadata_insufficient
  notebook: reproduce_wirth_2017.ipynb
  output: claim:direction-center-vs-periphery
  notes: For the 40 cells with significant direction IC (reading a, permuted chunks) normalized sparsity
    is higher in the centre than on return paths (median difference 0.020, 25 of 40, Wilcoxon p = 0.031)
    and IC is not (0.012, p = 0.43); with shifted chunks (28 cells) p = 0.016 and 0.095. Reading (a) meets
    neither level. Reading (b) needs the paper's responsive set, which needs the point-of-gaze space.
    Over the 59 three-space responsive cells, which it contains, IC and sparsity are both higher with
    p = 0.045 and 0.0074, the partial level; with shifted chunks (51 cells) IC is not (p = 0.14, sparsity
    p = 0.013). Over all 180 cells with both maps neither is higher (IC p = 0.31, sparsity p = 0.29, permuted
    chunks), so a signed-rank result over the 59 cells puts no bound on the result over the paper's set,
    which may lie at any level. No set reaches p < 0.001. Reading (a) fails and reading (b) cannot be
    formed, so the claim cannot be decided, as for landmark-identity-center.
  deviations:
  - Centre and return maps at one common angular resolution per session, chosen so the number of bins
    valid in both is closest to 200 (median 151 centre and 157.5 return bins valid); the paper does not
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -40 questions/wirth-2017.yaml; grep -n "56\|reading (b)\|responsive cells" papers/claims/wirth-2017.yaml 2>/dev/null | head; ls papers | head
```

```
# Questions from attempt wirth-2017-01 (author revision after verification round 2, 2026-11-13)
# about claims/wirth-2017.yaml, asked under docs/protocol.md, "Hand over for verification". The
# claim is tested as the claims file has it.
dataset: crcns:hc-12
paper: doi:10.1371/journal.pbio.2001045
questions:
- claim: gaze-anticipates-landmarks
  asked: 2026-11-13
  question: The claim says that on being relocated the monkeys gazed proactively at where the landmarks
    would appear. The criterion compares the mean horizontal eye position over the whole passive return,
    turning right against left. During any rotation of the view the mean eye position shifts toward the
    side the view turns to, so this measure cannot tell anticipation from the eye position that goes
    with the rotation itself. Should the criterion restrict the window to the part of the return before
    the landmarks enter the field of view, or compare against a reference that rotates without landmarks
    to come, so that it tests the proactive part of the claim? Or does the S2C legend, which shows the
    mean over the whole return, fix the measure as the claims file has it?
  passage: Results, Animals use direction and compute trajectory, paragraph 2, "Similarly, when being
    relocated to a new entry, monkeys proactively gazed at the location at which the landmarks would
    appear (see S2 Fig and S1 Appendix A2) (Wilcoxon test, p < 0.001)"; S2C legend, "Mean horizontal
    eye position during the passive return journey towards the right or the left".
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims | grep wirth; grep -n "direction-tuning-not-maintained" -A25 claims/wirth-2017.yaml | head -45
```

```
wirth-2017.yaml
358:- id: direction-tuning-not-maintained
359-  statement: Direction tuning was not maintained across positions; the correlation between
360-    directional tuning in the center and on return paths was significantly low in 20 of 56 cells
361-    (36%), more than chance, and significantly high in only 3, consistent with chance.
362-  source: Results, Direction selectivity, paragraph 1; Fig 3C inset
363-  quote: "the correlation between direction selectivity in the center and in the return paths was
364-    significantly lower in 20 out of 56 cells (inset in Fig 3C , blue bars). This represents 36% of
365-    the population and is higher than what is expected by chance ( p < 0.001, binomial test; note
366-    that correlation was only significantly higher in 3 cells, consistent with chance: p = 0.16,
367-    binomial test)"
368-  statistics:
369-  - about: cells with significantly low correlation
370-    test: binomial test
371-    p: 0.001
372-    p_relation: "<"
373-    n: 20 of 56 cells
374-  - about: cells with significantly high correlation
375-    test: binomial test
376-    p: 0.16
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 383,400p claims/wirth-2017.yaml; grep -n "Fig 3C\|responsive cells" claims/wirth-2017.yaml | head
```

```
value: 56
    tolerance: 5.6
  - quantity: cells with significantly high correlation
    value: 3
    tolerance: 0.3
  datasets:
  - crcns-hc-12
  criterion: Method W. Per cell, the uncentered correlation of center and return-path directional
    rates over the directional bins valid in both (Methods, Directional correlations); its
    significance from the surrogates, bilateral, at 0.05 per test with 0.025 per tail as the
    binomial chance rate (reading (b) of Method W, the one that gives p = 0.16 for 3 of 56).
    The 56 cells are read as the cells of direction-center-vs-periphery with enough common
    valid bins; the cell readings of that claim apply. Reproduced when, under one reading, the
    counts are within tolerance (the high count within 2 to 4, as a count of 3 cannot carry a
    10% tolerance) and the low count passes the binomial test at p < 0.001.
  depends_on:
  - direction-center-vs-periphery
- id: state-space-ic-higher
57:#  - Cells. The 189 cells with more than 100 spikes per session; responsive cells are those
274:    189 cells (59%, responsive cells).
[... 8 more lines not kept]
```

**Agent**

Both proposals were agreed by the verifier; I've set both outcomes to blocked (metadata_insufficient). Now recording round 3, the verifier's claims-file point as a question, then notebook and README.

**Agent calls Bash**

```bash
cd  cat >> questions/wirth-2017.yaml <<'EOF'
- claim: direction-tuning-not-maintained
  asked: 2026-11-13
  question: The criterion reads the 56 cells as the cells of direction-center-vs-periphery with enough
    common valid bins, and that claim has two cell readings, (a) the direction-selective cells and (b)
    all responsive cells. The paper's responsive set is 111 cells, so under reading (b) about half of
    them would need to lack enough common valid bins, while in this attempt 181 of 186 cells have at
    least 10 and a minimum of 2 changes nothing. Should the 56 be read as the direction-selective cells
    only (reading a), which the Results wording "for each direction-selective cell" also suggests, and
    reading (b) be dropped for this claim?
  passage: Results, Direction selectivity, paragraph 1, "for each direction-selective cell" and "the
    correlation between direction selectivity in the center and in the return paths was significantly
    lower in 20 out of 56 cells"; Fig 3C legend, "the responsive cells".
  why: Under reading (a) the claim fails on the number of cells (40 and 28 against 56 +- 5.6); reading
    (b) needs the point-of-gaze space and cannot be decided here, which is why the outcome is blocked.
    Dropping reading (b) would give not reproduced. The verifier of round 3 reported this point.
EOF
cat >> attempts/wirth-2017-01.yaml <<'EOF'
- date: '2026-11-13'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 3. Only the two changes of outcome proposed after round 2 (direction-center-vs-periphery
    and direction-tuning-not-maintained), with the executed notebook, the claims file and the paper.
    Report in transcripts/wirth-2017/verifier-3-report.md. It also reported that the claims file's reading
    of the 56 cells of direction-tuning-not-maintained fits reading (a) better than reading (b), and said
    this changes neither verdict; the point is added to questions/wirth-2017.yaml.
  results:
  - claim: direction-center-vs-periphery
    agrees: true
    outcome: blocked
    reason: 'The numbers in the proposal match cell 42. Reading (a) fails both levels: with permuted chunks
      40 cells, IC p = 0.43 and sparsity p = 0.031; with shifted chunks 28 cells, p = 0.095 and 0.016.
      Reading (b) needs the paper''s responsive set, and that set needs the point-of-gaze space, which
      the uncalibrated eye signal cannot give. The three-space stand-in reaches the partial level only
      with permuted chunks (IC p = 0.045, sparsity p = 0.0074, 59 cells); with shifted chunks IC is p
      = 0.14; over all 180 cells neither measure is higher (p = 0.31 and 0.29). A signed-rank result on
      a subset sets no bound on the result over a superset, so the paper''s set could fall at any level.
      Reading (a) fails and reading (b) cannot be formed, so the "under one reading" criterion cannot
      be decided, the same basis on which landmark-identity-center was verified as blocked (cell 64).
      The change moves away from the favourable outcome, and the binning choice was fixed before this
      round.'
    response: Outcome set to blocked (metadata_insufficient) and the proposal removed. The notes, the
      notebook's conclusion and summary and the README say blocked.
  - claim: direction-tuning-not-maintained
    agrees: true
    outcome: blocked
    reason: 'The numbers match cell 45. Reading (a) fails on the number of cells tested: 40 (permuted)
      and 28 (shifted), against 56 +- 5.6. Reading (b) cannot be formed without the gaze space. The bounding
      check in cell 45 is correct. With permuted chunks exactly one combination meets the criterion (n
      61, low 18, high 4); it needs exactly 2 gaze-only cells, both significantly low, which is narrow
      but possible, as 9 of the 122 cells outside the three-space set are low. With shifted chunks 13
      combinations meet it, for example n 55, low 18, high 3. A set meeting the criterion exists under
      both surrogate readings, and a set failing it (the stand-in) also exists, so the claim cannot be
      decided, consistent with landmark-identity-center and spatial-selectivity-fraction.'
    response: Outcome set to blocked (metadata_insufficient) and the proposal removed. The notes, the
      notebook's conclusion and summary and the README say blocked. The verifier's point on the reading
      of the 56 cells is added to questions/wirth-2017.yaml; the claim stays tested as the claims file
      has it.
EOF
python -c "import yaml;yaml.safe_load(open('attempts/wirth-2017-01.yaml'));yaml.safe_load(open('questions/wirth-2017.yaml'))"
```

```
(Bash completed with no output)
```

**Agent**

Now the notebook and README.

**Agent calls Bash**

```bash
cd entries/wirth-2017; grep -n "direction-center\|direction-tuning\|proposed\|not reproduced\|partially\|failure to reproduce" README.md; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and any(k in s for k in ['direction-center','direction-tuning','propos','Summary','## Summary']):
        print('=== cell',i, c.get('metadata',{}).get('tags')); print(s[:6000])
EOF
```

```
16:| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced (both with the three-space responsive cells standing in for the paper's set) |
25:A failure to reproduce here may be a failure of this attempt, not of the paper: see the
=== cell 0 None
# Reproducing Wirth et al. (2017) from CRCNS hc-12

Paper. Wirth S, Baraduc P, Plante A, Pinede S, Duhamel JR (2017). Gaze-informed, task-situated
representation of space in primate hippocampus during virtual navigation. PLoS Biology 15(2):
e2001045. [doi:10.1371/journal.pbio.2001045](https://doi.org/10.1371/journal.pbio.2001045).
The claims file (`claims/wirth-2017.yaml`) was written from the version of record (PMC5328243),
Results, Methods and the legends of Figs 1 to 7 and S1 to S7; S1 Appendix was not available.

Datasets. CRCNS [hc-12](https://doi.org/10.6080/K0R49NQV) (189 cells, the new-maze sessions;
every claim rests on it) and CRCNS [hc-21](https://doi.org/10.6080/K0GX48R9) (101 cells, a
familiar and a new maze per file), streamed from the public bucket `crcnsarchive`
(`hc-12/live/data.tar.gz`, `hc-21/live/data.tar.gz`). CRCNS data sets are not versioned; the
version is recorded as `unversioned`, and the MD5 sums from each data set's `checksums.md5`
for the files read are: hc-12 `data.tar.gz` 426c7d00c0358f2cc9873e0dbb331e2f (descriptor
version 0.7, 17 Jan 2017); hc-21 `data.tar.gz` dee5e8aa4a7b3c44b61b8cecfe622a0a (descriptor
version 0.52, 21 Dec 2018). Each data set has one published state (`live/`, with only
documentation under `orig/`), so the version pinned is the only one there is, and hc-12 is the
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
p='reproduce_wirth_2017.ipynb'
nb=json.load(open(p))
def setsrc(i,text):
    lines=text.split('\n'); nb['cells'][i]['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
def rep(i,old,new):
    s=''.join(nb['cells'][i]['source']); assert s.count(old)==1,(i,old); setsrc(i,s.replace(old,new))
rep(0,"| direction-center-vs-periphery, direction-tuning-not-maintained | tested |",
      "| direction-center-vs-periphery, direction-tuning-not-maintained | tested; reading (a) fails, reading (b) needs the responsive set, bounded |")
setsrc(43,"""**Result: blocked (metadata insufficient).** For the 40 direction-selective cells (reading a,
permuted chunks) normalized sparsity is higher in the centre (median difference 0.020,
p = 0.031) but IC is not (0.012, p = 0.43); with shifted chunks, 28 cells, p = 0.016 and 0.095.
Under reading (a) neither the reproduced level nor the partial level is met. Reading (b) needs
the paper's responsive set, which needs the gaze space. Over the cells responsive in the three
spaces computed here, which it contains, IC and sparsity are both higher in the centre with
p = 0.045 and 0.0074 (59 cells, permuted chunks), the criterion's partial level; with shifted
chunks (51 cells) IC is not (p = 0.14, sparsity p = 0.013). Over all 180 cells with both maps
neither IC nor sparsity is higher in the centre (p = 0.31 and 0.29, permuted chunks). The
signed-rank result changes with the cell set, and the result over a subset puts no bound on the
one over a larger set, so the paper's set may give any level. No set reaches p < 0.001. As
reading (a) fails and reading (b) cannot be formed, the claim cannot be decided. The verifier
agreed with this outcome in round 3.""")
setsrc(46,"""**Result: blocked (metadata insufficient).** Among the 40 direction-selective cells (permuted
chunks), 15 have a significantly low centre-return correlation (38%, binomial p = 2.1e-14 at
chance 0.025) and 4 a significantly high one (p = 0.017). The proportion of low cells is close
to the paper's 36% and the high count is inside 2 to 4, but 40 cells are tested (expected
56 +- 5.6) and the low count of 15 is outside 20 +- 2; with shifted chunks 28 cells are tested,
2 high and 11 low. Reading (a) fails on the number of cells. Reading (b) needs the paper's
responsive set, which needs the gaze space. Over the three-space responsive cells, 59 are tested
(inside the tolerance), 4 are high and 16 low; with shifted chunks 51 are tested, 3 high and 14
low. Over these sets the low count misses 18 to 22, although more cells than chance have a low
correlation under all of them (binomial p below 1e-10). The minimum of common bins (10 or 2)
changes nothing. The paper's responsive set contains the three-space responsive cells and lies
within all cells (181 tested, 25 low and 8 high with permuted chunks; 18 low and 7 high with
shifted chunks). A set between the two can meet the criterion under both readings of the
surrogates: with permuted chunks in one combination (n 61, low 18, high 4), with shifted chunks
in 13 (for example n 55, low 18, high 3). A set that meets the criterion and one that fails it
both exist, so the claim cannot be decided. The verifier agreed with this outcome in round 3.""")
rep(68,"| direction-center-vs-periphery | partially reproduced (three-space responsive cells for reading b, permuted chunks; blocked proposed) |",
       "| direction-center-vs-periphery | blocked: metadata insufficient (reading a fails; reading b needs the responsive set) |")
rep(68,"| direction-tuning-not-maintained | not reproduced (three-space responsive cells for reading b; blocked proposed, as the paper's set could meet the criterion) |",
       "| direction-tuning-not-maintained | blocked: metadata insufficient (reading a fails on the cell count; the paper's set could meet the criterion) |")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat .; sed -n 10,30p README.md
```

```
entries/wirth-2017/reproduce_wirth_2017.ipynb | 65 +++++++++++++--------------
 1 file changed, 32 insertions(+), 33 deletions(-)
| Gaze anticipates the turn, and the side where landmarks will appear | Reproduced (sign of the eye signal assumed, supported by the slow phases) |
| Learning in about a dozen trials; fewer than 10 more trials to 90% | Reproduced |
| Performance after new entries in probe sessions | Not reproduced (monkey K only) |
| Faster learning after new entries | Blocked: methods underspecified |
| 189 cells analysed of 270 recorded | Partially reproduced |
| State space has the most responsive cells (84) | Not reproduced |
| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced (both with the three-space responsive cells standing in for the paper's set) |
| Higher information in state space than in position and direction space | Partially reproduced (the gaze comparison cannot be made) |
| Sparser in state space than in direction space | Reproduced (full-trial window) |
| Sparsity, state against position space | Not reproduced |
| State-space selectivity in the centre | Not reproduced (assuming permuted chunks; open under shifted chunks) |
| Landmark identity and distance (two-way ANOVA) | Not reproduced |
| Claims that need the point-of-gaze space or the paper's responsive set (11 claims) | Blocked: metadata insufficient |
| Number of fields, control for dimensionality | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
p='README.md'; s=open(p).read()
s=s.replace("| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced (both with the three-space responsive cells standing in for the paper's set) |\n","")
o="| Claims that need the point-of-gaze space or the paper's responsive set (11 claims) | Blocked: metadata insufficient |"
assert o in s
s=s.replace(o,"| Claims that need the point-of-gaze space or the paper's responsive set (13 claims, including the centre against return-path direction maps) | Blocked: metadata insufficient |")
open(p,'w').write(s)
EOF
grep -c "metadata_insufficient" ../../attempts/wirth-2017-01.yaml; grep -n "^  outcome: blocked" -A1 ../../attempts/wirth-2017-01.yaml | grep -c metadata_insufficient; date -u
```

```
16
13
Fri Nov 13 19:16:22 UTC 2026
```

**Agent calls Bash**

```bash
cd  sed -n 380,470p attempts/wirth-2017-01.yaml | grep -n -i "direction\|propos"; grep -n "direction-c\|direction-t\|propos" entries/wirth-2017/wirth.py | head; grep -n "all)" -A3 tools/entry.py | head; grep -n "Develop on a subset" -A12 docs/protocol.md | head -20
```

```
53:    42 or 37 without), sparsity-state-vs-direction holds only with the returns, and state-space-selectivity
393:- **Develop on a subset.** Build and debug each analysis on one or two
394-  sessions, or a few units, and run it on the whole dataset once, when it
395-  works; do not re-run whole notebooks to test a change. Time the subset and
396-  measure its peak memory (`resource.getrusage(resource.RUSAGE_SELF).ru_maxrss`,
397-  in kilobytes on Linux), and estimate the whole. If the estimate is over the
398-  notebook limit, over the time left (see "Time" above), or over 12 GB of
399-  memory, record the claim as blocked, `too_large`, with the estimate, and do
400-  not run it. To survey the dataset, read each file's
401-  metadata and array shapes, not its data.
402-
403-The notebook has these parts, in this order:
404-
405-1. **Header.** The paper, the dataset and version, the text the claims file
```

**Agent calls Bash**

```bash
cd  ls executed/wirth-2017/ 2>/dev/null; cat executed/wirth-2017/*.json 2>/dev/null | head -20; grep -rn "seconds\|minutes" transcripts/wirth-2017/*.md 2>/dev/null | grep -i "run\|notebook" | tail -3
```

```
reproduce_wirth_2017.ipynb
result.json
{
 "entry": "wirth-2017",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_wirth_2017.ipynb",
   "ok": true,
   "seconds": 1794,
   "error": null
  }
 ]
}
transcripts/wirth-2017/author.md:2457:  runtime_minutes: 30
transcripts/wirth-2017/author.md:2980:The author run is complete: 28 claims recorded, the entry's checks pass with 0 errors, and the handover is built. The notebook ran from a clean environment in 1,178 s (about 20 minutes), with peak memory around 1 GB.
transcripts/wirth-2017/author.md:3039:The run took about 1 h 50 min, 11:51 to 13:42 UTC. Two full runs of the entry passed: 1,231 s, then 1,178 s. During development the loader failed twice, on files whose camera data or eye channels sit in other layouts; I fixed both and nothing failed after. `entry.yaml` still says 30 minutes of runtime where the actual run takes about 20; I left it so as not to invalidate the executed copy. As instructed, nothing was committed or pushed.
```

**Agent**

The previous full run took about 30 min, well inside the time left. Running it now.

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/wirth-2017 2>&1 | tail -30
```

```
error: attempts/wirth-2017-01.yaml: outcomes/10/outcome: 'blocked' should not be valid under {'const': 'blocked'}
error: attempts/wirth-2017-01.yaml: outcomes/11/outcome: 'blocked' should not be valid under {'const': 'blocked'}
2 error(s)

real	0m6.533s
user	0m6.340s
sys	0m0.170s
```

**Agent calls Bash**

```bash
cd  grep -rn "const.*blocked" -B8 -A8 schemas/ 2>/dev/null | head -60 || grep -rln '"blocked"' --include=*.json . | head
```

```
schemas/attempt.schema.json-337-            }
schemas/attempt.schema.json-338-          }
schemas/attempt.schema.json-339-        },
schemas/attempt.schema.json-340-        "allOf": [
schemas/attempt.schema.json-341-          {
schemas/attempt.schema.json-342-            "if": {
schemas/attempt.schema.json-343-              "properties": {
schemas/attempt.schema.json-344-                "outcome": {
schemas/attempt.schema.json:345:                  "const": "blocked"
schemas/attempt.schema.json-346-                }
schemas/attempt.schema.json-347-              }
schemas/attempt.schema.json-348-            },
schemas/attempt.schema.json-349-            "then": {
schemas/attempt.schema.json-350-              "required": [
schemas/attempt.schema.json-351-                "blocked_by",
schemas/attempt.schema.json-352-                "notes"
schemas/attempt.schema.json-353-              ]
--
schemas/attempt.schema.json-369-                "deviations"
schemas/attempt.schema.json-370-              ],
[... 15 more lines not kept]
```

**Agent**

The schema does not allow `assumed: true` on a blocked outcome, so I'm removing `assumed` from both claims. The deviations stay.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/wirth-2017-01.yaml'; s=open(p).read()
o="""    cells, which it contains, stand in for it, an assumption.
  assumed: true
- claim: direction-tuning-not-maintained"""
assert s.count(o)==1; s=s.replace(o,o.replace("  assumed: true\n",""))
o="""  - 4
  assumed: true
  notes: Of 40 direction-selective"""
assert s.count(o)==1; s=s.replace(o,o.replace("  assumed: true\n",""))
for a,b in [("""    response: Outcome set to blocked (metadata_insufficient) and the proposal removed. The notes, the
      notebook's conclusion and summary and the README say blocked.
  - claim: direction-tuning""","""    response: Outcome set to blocked (metadata_insufficient) and the proposal removed; assumed is removed,
      as a blocked outcome carries none, and the deviations stay. The notes, the notebook's conclusion
      and summary and the README say blocked.
  - claim: direction-tuning"""),("""    response: Outcome set to blocked (metadata_insufficient) and the proposal removed. The notes, the
      notebook's conclusion and summary and the README say blocked. The verifier's""","""    response: Outcome set to blocked (metadata_insufficient) and the proposal removed; assumed is removed,
      as a blocked outcome carries none, and the deviations stay. The notes, the notebook's conclusion
      and summary and the README say blocked. The verifier's""")]:
    assert s.count(a)==1; s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/entry.py check entries/wirth-2017 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/wirth-2017 2>&1 | tail -30
```

```
Fri Nov 13 19:16:56 UTC 2026
Installed kernelspec registry-wirth-2017 in executed/wirth-2017/.venv/share/jupyter/kernels/registry-wirth-2017
0 error(s)
pass  reproduce_wirth_2017.ipynb  (1589 s)

real	26m40.179s
user	19m49.903s
sys	2m57.123s
```

**Agent**

The run passed. Checking that the re-executed outputs still give the numbers the text cites.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/wirth-2017/reproduce_wirth_2017.ipynb'))
for i in (42,45):
    out=''.join(''.join(o.get('text','')) if 'text' in o else ''.join(o.get('data',{}).get('text/plain','')) for o in nb['cells'][i].get('outputs',[]))
    print('== cell',i); print(out[-3000:])
EOF
```

```
== cell 42
   surrogates                       cells   measure    n  median centre  median return  median diff  centre higher         p
0     permute   (a) direction IC p < 0.01        IC   40          0.091          0.062        0.012             21  0.427972
1     permute   (a) direction IC p < 0.01  sparsity   40          0.062          0.018        0.020             25  0.030970
2     permute  (b) three-space responsive        IC   59          0.079          0.031        0.019             34  0.045477
3     permute  (b) three-space responsive  sparsity   59          0.060          0.014        0.022             39  0.007373
4     permute       all cells (reference)        IC  180          0.036          0.008        0.012             99  0.311157
5     permute       all cells (reference)  sparsity  180          0.021          0.010        0.008             99  0.287228
6       shift   (a) direction IC p < 0.01        IC   28          0.096          0.070        0.027             16  0.094564
7       shift   (a) direction IC p < 0.01  sparsity   28          0.074          0.023        0.040             20  0.015633
8       shift  (b) three-space responsive        IC   51          0.084          0.050        0.018             29  0.136124
9       shift  (b) three-space responsive  sparsity   51          0.052          0.019        0.030             34  0.013339
10      shift       all cells (reference)        IC  180          0.019          0.013        0.005             95  0.739257
11      shift       all cells (reference)  sparsity  180          0.014          0.006        0.007             99  0.212372

Valid direction bins: centre median 151.0 , return median 157.5

== cell 45
   surrogates                       cells  min common bins    n  low  high   p binom low  p binom high  median corr
0     permute   (a) direction IC p < 0.01               10   40   15     4  2.072054e-14      0.017449        0.589
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/wirth-2017 2>&1 | tail -2; git status --short
```

```
0 error(s)
 M attempts/wirth-2017-01.yaml
 M entries/wirth-2017/README.md
 M entries/wirth-2017/reproduce_wirth_2017.ipynb
 M questions/wirth-2017.yaml
 M tools/build_site.py
 M tools/site_assets/app.css
 M tools/site_assets/list.js
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
?? scripts
```

**Agent**

The verifier agreed with both proposals in round 3, so neither proposal is still open.

**Outcomes changed**
- **direction-center-vs-periphery**: changed from partially_reproduced to blocked (`metadata_insufficient`). Reading (a), the direction-selective cells, meets neither level. Reading (b) needs the paper's set of responsive cells, which needs the point-of-gaze space. The three-space cells and the full set of cells give different results, so the paper's set could land at any level.
- **direction-tuning-not-maintained**: changed from not_reproduced to blocked (`metadata_insufficient`). Reading (a) fails on the number of cells tested: 40 or 28, against 56 ± 5.6. Under reading (b), sets that meet the criterion and sets that fail it both exist between the two bounds.

On both claims I removed `proposed`. I also removed `assumed: true`, which goes beyond "change nothing else": the entry's check failed because the schema does not allow `assumed` on a blocked outcome. The deviations stay, and the round-3 responses say why `assumed` went. No other outcome changed.

**Other updates**
- I updated the notes, the notebook's two conclusion cells, the header table and the summary, and the README. The blocked row in the README now counts 13 claims, up from 11.
- Round 3 is recorded under `verifications`, with one result per claim. Each gives agrees: true, outcome blocked, the verifier's reason and my response.
- The verifier also said the claims file's reading of the 56 cells fits reading (a) better than reading (b). It said this changes neither verdict. Following the protocol, I added it as a question in `questions/wirth-2017.yaml` and did not change the claim.

`python tools/entry.py all entries/wirth-2017` passed with 0 errors, and the notebook ran in 1,589 s. The re-executed cells 42 and 45 give the same numbers the text cites. Nothing is committed. The changes to `tools/` and the untracked dotfiles were there before this run, and I did not touch them.

## End of run

24 turns, 29 minutes, $0.75 at API prices, result: success.
