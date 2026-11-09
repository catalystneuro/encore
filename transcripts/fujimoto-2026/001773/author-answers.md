# 001773 · author-answers · run 41677257629

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls entries/001773-fujimoto-2026 entries/001773-fujimoto-2026/*; cat questions/001773.yaml
```

```
Tue Nov  3 16:49:10 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/^## Author/,/^## [A-Z]/p' docs/protocol.md | head -300; ls attempts | grep 001773; ls attempts/001773* ; ls claims | grep 1773
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "author-answers\|answers" docs/protocol.md | head -30; cat attempts/001773-fujimoto-2026-01.yaml; git diff HEAD~1 --stat; git show HEAD --stat
```

```
32:`author`, `author-answers` when a reader answered a question on the claims
322:     claims file (reader, step 6), and a later run, `author-answers`,
474:step 1.6, and does not change the claim. A reader answers it after the
505:- **Blind.** The author's runs (author, author-answers and each
schema_version: 2
id: 001773-fujimoto-2026-01
dataset:
  archive: dandi
  id: "001773"
  version: 0.260416.1939
  doi: 10.48324/dandi.001773/0.260416.1939
paper: doi:10.1038/s41593-026-02301-4
date: 2026-11-03
entry: 001773-fujimoto-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 425 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff HEAD~1 -- claims/; sed -n 1,80p docs/protocol.md | grep -n -A10 "author-answers"
```

```
diff --git a/claims/001773/10.1038-s41593-026-02301-4.yaml b/claims/001773/10.1038-s41593-026-02301-4.yaml
index 9b5ddfd99a..aa8401581d 100644
--- a/claims/001773/10.1038-s41593-026-02301-4.yaml
+++ b/claims/001773/10.1038-s41593-026-02301-4.yaml
@@ -88,9 +88,10 @@
 #   The LIM count in Fig. 5c (821) equals the Methods list (803) plus area 25 (18), and the
 #   Extended Data Fig. 9 legend counts SCC as a LIM hub; so LIM is open, (a) with area 25 (the
 #   reported n) and (b) without (the Methods).
-# - Whole-brain connectome (Fig. 4): AFNI 3dNetCorr on CHARM and SARM level 4 ROIs, 122 ROIs as
-#   listed in Supplementary Tables 3 and 4 (hemispheres not separated in those lists; whether
-#   left and right ROIs are merged is not stated), Fisher Z per run, averaged per condition, post
+# - Whole-brain connectome (Fig. 4): AFNI 3dNetCorr on CHARM and SARM level 4 ROIs, 123 ROIs as
+#   listed in Supplementary Tables 3 and 4, each with 122 values, the legends' n = 122
+#   (hemispheres not separated in those lists; whether left and right ROIs are merged is not
+#   stated), Fisher Z per run, averaged per condition, post
 #   minus pre per subject, averaged across subjects.
 #
 # Paper inconsistencies found while reading (for the author's notes, not claims):
@@ -99,8 +100,8 @@
 #   example area_25 r_rb = -0.164) are far too small for the P values of Supplementary Table 1
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; python - <<'EOF'
import json
nb=json.load(open('reproduce_fujimoto_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'fig4b' in s or '122' in s or 'fig4c' in s or 'Summary' in s[:200] or i<3:
        print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'));print(s)
EOF
grep -n "def .*rank\|ranksum\|nrois\|0.05\|def roi" dbs.py | head -40
```

```
===== 0 markdown None
# Reproducing Fujimoto et al. (2026) from dandiset 001773

**Paper.** Fujimoto S, Fujimoto A, Elorette C, et al. (2026). Deep brain stimulation induces white
matter remodeling and functional changes to brain-wide networks. *Nature Neuroscience*.
[doi:10.1038/s41593-026-02301-4](https://doi.org/10.1038/s41593-026-02301-4). The claims file was
written from the version of record (open access, PMC13337501), with its Methods, Extended Data
legends and Supplementary Information.

**Dandiset.** [DANDI:001773](https://dandiarchive.org/dandiset/001773/0.260416.1939), version
0.260416.1939. This is the version the paper cites in its Code availability statement
(doi:10.48324/dandi.001773/0.260416.1939), as the claims file gives it. A later version,
0.260615.1838, holds the same 54 assets with the same asset ids (shown in the data check), so the
choice does not change the data.

The dandiset holds the paper's derived values as Excel sheets (voxel FA, voxel seed connectivity,
group connectomes, cell counts, g-ratios, behavior bins) and its MATLAB analysis scripts. The
sheets are read into memory from the archive; the analyses follow the scripts (see `dbs.py`). No
random numbers are used anywhere.

[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; python - <<'EOF'
import json
nb=json.load(open('reproduce_fujimoto_2026.ipynb'))
for i in [52,54,55]:
    c=nb['cells'][i];print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'));print(''.join(c['source']))
EOF
sed -n 20,40p dbs.py; cat entry.yaml; ls ../../executed 2>/dev/null | head
```

```
===== 52 code ['claim:fig4b-roi-changes-counts']
p_code = pvals[("DBS", False)]["code rank-sum change vs zeros"]
sig = p_code < 0.05 / 123
print(f"code's reading, DBS: largest P among the significant ROIs {p_code[sig].max():.2e}; smallest P among the others {p_code[~sig].min():.2e}")
print(f"DBS significant ROIs, cortical {int(sig[:54].sum())} of 54, subcortical {int(sig[54:].sum())} of 69; "
      f"of them with negative mean change {int((sig & (np.array([dbs.offdiag(conn['DBS']['diff'], i).mean() for i in range(123)]) < 0)).sum())}")
pc = pvals[("CTRL", False)]["code rank-sum change vs zeros"]
print(f"code's reading, controls: largest significant P {pc[pc < 0.05 / 123].max():.2e}; smallest P among the others {pc[pc >= 0.05 / 123].min():.2e}")
===== 54 markdown None
## fig4-nonsurgical-no-pattern

> In the nonsurgical control animals, scans 6 to 7 weeks apart showed no systematic pattern of
> functional connectivity change.

The measure of fig4a-cortical-down-subcortical-up on the control group's difference connectome
(column CTRL of the table above).
===== 55 code ['claim:fig4-nonsurgical-no-pattern']
print(block_table[["DBS", "CTRL"]].round(4).to_string())
ctrl = block_table.CTRL
for r in ["a", "b"]:
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; python - <<'EOF'
import json
p='reproduce_fujimoto_2026.ipynb'
nb=json.load(open(p))
C=nb['cells']
def setsrc(i,s):
    C[i]['source']=s.strip('\n').splitlines(keepends=True)
assert C[50]['source'][0].startswith('## fig4b')
setsrc(50,'''
## fig4b-roi-changes-counts

> Per ROI, functional connectivity changed significantly between pre and post scans in 69 of the
> 123 CHARM and SARM ROIs in the DBS group and in 44 of 123 in the nonsurgical control group.

The criterion, amended after the reader's answer of 2026-11-03, is the test of the paper's Fig. 4
script: for each of the 123 ROIs, a two-sided rank-sum of its 122 off-diagonal changes against 122
zeros, `ranksum(sbj_data_mean, zeros(length(sbj_data_mean),1))`, counted when P < 0.05/123 (the
script's 0.05/nrois). The rank-sum is computed as MATLAB `ranksum` does for these sample sizes
(normal approximation with tie correction and continuity correction, `scipy.stats.mannwhitneyu`,
method "asymptotic"). The tolerance is 62.1 to 75.9 (DBS) and 39.6 to 48.4 (controls).

Reported as variants, not judged on: the Methods' threshold P < 0.01/123, a rank-sum of the ROI's
pre values against its post values, and a signed-rank test of its changes against zero; also the
thresholds 0.01/122 and 0.01 uncorrected, and the values with the ROI's own diagonal, which the
earlier criterion named.
''')
setsrc(52,'''
p_code = pvals[("DBS", False)]["code rank-sum change vs zeros"]
pc = pvals[("CTRL", False)]["code rank-sum change vs zeros"]
n_dbs, n_ctrl = int((p_code < 0.05 / 123).sum()), int((pc < 0.05 / 123).sum())
print(f"criterion (rank-sum of the 122 off-diagonal changes against zeros, P < 0.05/123): DBS {n_dbs} (tolerance 62.1 to 75.9), "
      f"controls {n_ctrl} (39.6 to 48.4); both in tolerance: {62.1 <= n_dbs <= 75.9 and 39.6 <= n_ctrl <= 48.4}")
sig = p_code < 0.05 / 123
print(f"DBS: largest P among the significant ROIs {p_code[sig].max():.2e}; smallest P among the others {p_code[~sig].min():.2e}")
print(f"DBS significant ROIs, cortical {int(sig[:54].sum())} of 54, subcortical {int(sig[54:].sum())} of 69; "
      f"of them with negative mean change {int((sig & (np.array([dbs.offdiag(conn['DBS']['diff'], i).mean() for i in range(123)]) < 0)).sum())}")
print(f"controls: largest significant P {pc[pc < 0.05 / 123].max():.2e}; smallest P among the others {pc[pc >= 0.05 / 123].min():.2e}")
print(f"thresholds: 0.05/123 = {0.05 / 123:.2e}, 0.01/123 = {0.01 / 123:.2e}")
''')
setsrc(53,'''
**Result: reproduced.** Under the amended criterion, the rank-sum of each ROI's 122 changes against
zeros at P < 0.05/123 gives 69 ROIs in the DBS group and 44 in the controls, the reported counts
(with the diagonal, 69 and 44 as well). The largest P counted as significant is 3.88e-04 in both
groups, the largest value in Supplementary Tables 1 and 2 (3.9e-4). Of the variants, the same test
at the Methods' threshold 0.01/123 gives 62 and 36, the pre against post rank-sum 10 to 44 (DBS)
and 4 to 15 (controls), and the signed-rank test 60 to 85 and 27 to 49.
''')
for i in (0,105):
    s=''.join(C[i]['source'])
    s=s.replace('| fig4b-roi-changes-counts | reproduced, resting on an assumption |','| fig4b-roi-changes-counts | reproduced |')
    s=s.replace("""The per-ROI connectome counts rest on the test and
threshold of the paper's Fig. 4 script (rank-sum of the changes against zeros, P < 0.05/123),
which differ from the Methods' "P < 0.01 with Bonferroni correction".""","""The per-ROI connectome counts use the test and
threshold of the paper's Fig. 4 script (rank-sum of the changes against zeros, P < 0.05/123), as
the claims file has them since a reader's answer; they differ from the Methods' "P < 0.01 with
Bonferroni correction".""")
    s=s.replace("""The connectomes have 123 ROIs, so each ROI has
122 values, the n of the Fig. 4b legend; the claims file reads that n as the number of ROIs.""","""The connectomes have 123 ROIs, so each ROI has
122 values, the n of the Fig. 4b legend.""")
    C[i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; grep -n "assum\|122\|fig4b" README.md
```

```
.../reproduce_fujimoto_2026.ipynb                  | 55 ++++++++++++----------
 1 file changed, 31 insertions(+), 24 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; git diff reproduce_fujimoto_2026.ipynb | grep "^[-+]" | grep -v fig4b | head -30; cat README.md | head -40
```

```
--- a/entries/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb
+++ b/entries/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb
-    "> 122 CHARM and SARM ROIs in the DBS group and in 44 of 122 in the nonsurgical control group.\n",
+    "> 123 CHARM and SARM ROIs in the DBS group and in 44 of 123 in the nonsurgical control group.\n",
-    "The criterion's readings: (a) rank-sum of the ROI's pre values against its post values; (b)\n",
-    "signed-rank of its changes against zero; thresholds P < 0.01/122 (the same as adjusted P < 0.01)\n",
-    "and P < 0.01 uncorrected; with and without the ROI's own diagonal. The rank-sum is computed as\n",
-    "MATLAB `ranksum` does for these sample sizes (normal approximation with tie correction and\n",
-    "continuity correction, `scipy.stats.mannwhitneyu`, method \"asymptotic\"). The Fig. 4 script's own\n",
-    "test, `ranksum(changes, zeros(n,1)) < 0.05/nrois` with nrois = 123, is shown as the code's reading;\n",
-    "with 0.01/123 too. The tolerance is 62.1 to 75.9 (DBS) and 39.6 to 48.4 (controls)."
+    "The criterion, amended after the reader's answer of 2026-11-03, is the test of the paper's Fig. 4\n",
+    "script: for each of the 123 ROIs, a two-sided rank-sum of its 122 off-diagonal changes against 122\n",
+    "zeros, `ranksum(sbj_data_mean, zeros(length(sbj_data_mean),1))`, counted when P < 0.05/123 (the\n",
+    "script's 0.05/nrois). The rank-sum is computed as MATLAB `ranksum` does for these sample sizes\n",
+    "(normal approximation with tie correction and continuity correction, `scipy.stats.mannwhitneyu`,\n",
+    "method \"asymptotic\"). The tolerance is 62.1 to 75.9 (DBS) and 39.6 to 48.4 (controls).\n",
+    "\n",
+    "Reported as variants, not judged on: the Methods' threshold P < 0.01/123, a rank-sum of the ROI's\n",
+    "pre values against its post values, and a signed-rank test of its changes against zero; also the\n",
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; grep -c "as\\\\n\|since a reader" reproduce_fujimoto_2026.ipynb; grep -n "since a reader\|reads that n\|resting on an assumption" reproduce_fujimoto_2026.ipynb
```

```
4
1770:    "the claims file has them since a reader's answer; they differ from the Methods' \"P < 0.01 with\n",
```

**Agent**

Notebook updated. Now the README row and the attempt record.

**Agent calls Bash**

```bash
cd entries/001773-fujimoto-2026; python - <<'EOF'
p='README.md'; s=open(p).read()
s=s.replace("| Reproduced (the counts rest on the test of the paper's script) |","| Reproduced |")
open(p,'w').write(s)
EOF
git diff README.md | grep "^[-+]"
```

```
--- a/entries/001773-fujimoto-2026/README.md
+++ b/entries/001773-fujimoto-2026/README.md
-| Connectome patterns and per-ROI counts, DBS group and nonsurgical controls (3 claims) | Reproduced (the counts rest on the test of the paper's script) |
+| Connectome patterns and per-ROI counts, DBS group and nonsurgical controls (3 claims) | Reproduced |
```

**Agent calls Bash**

```bash
cd  grep -n "verifications\|proposed\|answers\|questions" schemas/*attempt* | head -30; grep -n -B2 -A12 "author-answers\|### Answers\|## Answers" docs/protocol.md | sed -n 1,80p
```

```
252:          "proposed": {
334:    "verifications": {
30-write the claims file. The other runs are made with the
31-[Agent run](../.github/workflows/attempt.yml) workflow, one role at a time:
32:`author`, `author-answers` when a reader answered a question on the claims
33-file, `verifier-1`, `author-revise-1`, `verifier-2`, `author-revise-2`, and,
34-when the last of these proposes changes of outcome, `verifier-3` and `author-revise-3`. Each run's
35-transcript and final report are kept in
36-[`transcripts/<folder>/`](../transcripts). A dataset's folder is its identifier
37-on DANDI and `<archive>-<id>` otherwise ([archives.md](archives.md)). The
38-pipeline is described in [pipeline.md](pipeline.md).
39-
40-## Reader
41-
42-### 1. Get the paper
43-
44-The workflow puts the paper's full text, and its PDF where there is one, under
--
320-     paper's reading as a variant where it can be run, and say in the
321-     claim's notes that it is asked. A reader decides whether to amend the
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/001773-fujimoto-2026-01.yaml'; s=open(p).read()
start=s.index('- claim: fig4b-roi-changes-counts'); end=s.index('- claim: fig4c-network-sorted-reduction')
new='''- claim: fig4b-roi-changes-counts
  outcome: reproduced
  notebook: reproduce_fujimoto_2026.ipynb
  output: claim:fig4b-roi-changes-counts
  measured:
  - 69
  - 44
  notes: Under the amended criterion, the paper's Fig. 4 script's test (rank-sum of each ROI's 122
    off-diagonal changes against 122 zeros, significant at P < 0.05/123), computed as MATLAB's
    ranksum (tie and continuity corrected), gives 69 ROIs for the DBS group (41 of 54 cortical, 28
    of 69 subcortical) and 44 for the controls, the reported counts, with or without the diagonal.
    The largest P counted is 3.88e-04 in both groups, the largest value listed in Supplementary
    Tables 1 and 2 (3.9e-4). Of the variants, the same test at the Methods' threshold 0.01/123
    gives 62 and 36, the pre against post rank-sum 10 to 44 (DBS) and 4 to 15 (controls), and the
    signed-rank of the changes 60 to 85 and 27 to 49. What the answer changed. The earlier
    criterion named only the pre against post rank-sum and the signed-rank, at 0.01/122 or 0.01,
    none of which puts both counts in tolerance, so the outcome rested on an assumption that the
    script's test and threshold are the paper's (reproduced, assumed). The reader's answer of
    2026-11-03 (questions/001773.yaml) made the script's test and threshold the criterion and
    changed the statement's 122 ROIs to 123. The outcome stays reproduced, the counts are the same,
    and it no longer rests on an assumption.
  deviations:
  - The matrices have 123 ROIs, so each ROI has 122 values, the n of the legend; the threshold
    uses 123 as the script and the amended criterion do (0.01/122 is also shown).
'''
s=s[:start]+new+s[end:]
old='''  notes: The criterion blocks the claim without an assignment of the connectome's ROIs to
    networks.'''
assert old in s
s=s.replace(old,'''  notes: The criterion blocks the claim without an assignment of the connectome's ROIs to
    networks. The reader's answer of 2026-11-03 changed the criterion's 122 ROIs to 123, the
    number the deposited connectomes have; this does not change the block.''')
open(p,'w').write(s)
EOF
python -c "import yaml;yaml.safe_load(open('attempts/001773-fujimoto-2026-01.yaml'))" && echo ok; date -u
```

```
ok
Tue Nov  3 16:49:59 UTC 2026
```

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/001773-fujimoto-2026 2>&1 | tail -5; time python tools/entry.py all entries/001773-fujimoto-2026 2>&1 | tail -30
```

```
wrote entries/001773-fujimoto-2026/requirements.lock.txt
Installed kernelspec registry-001773-fujimoto-2026 in executed/001773-fujimoto-2026/.venv/share/jupyter/kernels/registry-001773-fujimoto-2026
0 error(s)
pass  reproduce_fujimoto_2026.ipynb  (24 s)

real	0m31.804s
user	0m28.029s
sys	0m4.019s
```

**Agent calls Bash**

```bash
cd  ls executed/001773-fujimoto-2026/; python - <<'EOF'
import json,glob
nb=json.load(open('executed/001773-fujimoto-2026/reproduce_fujimoto_2026.ipynb'))
for c in nb['cells']:
    if 'claim:fig4b-roi-changes-counts' in (c.get('metadata',{}).get('tags') or []) or 'claim:fig4-nonsurgical-no-pattern' in (c.get('metadata',{}).get('tags') or []):
        for o in c.get('outputs',[]): print(''.join(o.get('text','')))
EOF
git status --short
```

```
reproduce_fujimoto_2026.ipynb
result.json
group                                                             CTRL  DBS  DBS_in_tol  CTRL_in_tol
values            test                          threshold                                           
122 off-diagonal  a rank-sum pre vs post        0.01 uncorrected    15   44       False        False
                                                0.01/122             4   11       False        False
                                                0.01/123             4   11       False        False
                                                0.05/123 (code)      5   18       False        False
                  b signed-rank change vs 0     0.01 uncorrected    49   85       False        False
                                                0.01/122            27   60       False        False
                                                0.01/123            27   60       False        False
                                                0.05/123 (code)     35   68        True        False
                  code rank-sum change vs zeros 0.01 uncorrected    56   81       False        False
                                                0.01/122            36   62       False        False
                                                0.01/123            36   62       False        False
                                                0.05/123 (code)     44   69        True         True
123 with diagonal a rank-sum pre vs post        0.01 uncorrected    15   43       False        False
                                                0.01/122             4   10       False        False
                                                0.01/123             4   10       False        False
                                                0.05/123 (code)      5   17       False        False
[... 43 more lines not kept]
```

**Agent**

Numbers match the conclusions (69 and 44; variants as stated). Building the handover.

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/001773-fujimoto-2026 2>&1 | tail -5; ls executed/001773-fujimoto-2026/handover; python tools/entry.py check entries/001773-fujimoto-2026 2>&1 | tail -3; date -u
```

```
wrote executed/001773-fujimoto-2026/handover
10.1038-s41593-026-02301-4.yaml
dbs.py
reproduce_fujimoto_2026.ipynb
0 error(s)
Tue Nov  3 16:50:57 UTC 2026
```

**Agent**

There was one question, and its answer changed one claim's outcome basis and one blocked claim's wording. The entry is locked, checked (0 errors) and ran clean from a fresh environment in 24 s. The handover is in `executed/001773-fujimoto-2026/handover/`. I did not verify my own work, and nothing is committed or pushed.

## Question: `fig4b-roi-changes-counts` (questions/001773.yaml)

I asked whether the criterion should include the test and threshold from the paper's Fig. 4 script. The script runs a rank-sum of each ROI's changes against zeros and counts an ROI at P < 0.05/123. I also asked whether "of the 122 ROIs" was right, given that the deposited connectomes have 123 ROIs.

**What the answer changed.** The reader said yes to both and amended the claim:
- The criterion now judges only the script's test, with the diagonal excluded and P < 0.05/123.
- The Methods' threshold (P < 0.01 Bonferroni), the pre-against-post rank-sum and the signed-rank test are kept as reported variants. They no longer decide the outcome.
- The statement and the header now say 123 ROIs, and so does the criterion of `fig4c-network-sorted-reduction`.
- The expected counts (69 and 44) did not change.

**What I updated.**
- **Notebook:** the fig4b section quotes the amended statement and describes the new criterion and the variants. It now prints the judged count against the tolerance and the thresholds. The Result line and the summary row now say "reproduced", without "resting on an assumption".
- **README:** the matching row no longer has the qualifier.
- **Attempt record:** `assumed: true` and the assumption deviation are removed, and both claims' notes say what the answer changed. I kept the `code_mismatch` finding, because the Methods' "P < 0.01" still disagrees with the script.

## Outcome per affected claim

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| fig4b-roi-changes-counts | reproduced, resting on an assumption (`assumed: true`) | reproduced, no longer resting on an assumption: 69 (DBS) and 44 (controls), both within tolerance |
| fig4c-network-sorted-reduction | blocked (methods_underspecified) | blocked (methods_underspecified), unchanged: going from 122 to 123 ROIs does not give the ROIs network labels |

For fig4b, the largest P counted as significant is 3.88e-04 in both groups, which matches the 3.9e-4 in Supplementary Tables 1 and 2. None of the variants puts both counts in tolerance:

| Variant | DBS (target 62.1 to 75.9) | Controls (target 39.6 to 48.4) |
|---|---|---|
| Same test at the Methods' 0.01/123 | 62 | 36 |
| Pre-against-post rank-sum | 10 to 44 | 4 to 15 |
| Signed-rank of the changes | 60 to 85 | 27 to 49 |

No other claim was affected, and its outcome did not change. The executed notebook's numbers for `fig4-nonsurgical-no-pattern` are unchanged, including the controls' count of 44.

## End of run

16 turns, 2 minutes, $0.65 at API prices, result: success.
