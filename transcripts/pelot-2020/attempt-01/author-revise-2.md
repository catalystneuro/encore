# pelot-2020 · author-revise-2 · run 44240948829

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/pelot-2020/verifier-2-report.md; ls entries/pelot-2020 entries/pelot-2020/*; ls paper questions transcripts/pelot-2020
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
<persisted-output>
Output too large (41.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1d2cae69-cb13-458d-a737-1620a44524a9/tool-results/bf29bfs1g.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-16`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

```
Wed Nov 18 05:04:38 UTC 2026
**Round 2 verification: Pelot et al. (2020), attempt pelot-2020-01**

The claims file has 35 claims and the attempt record has 35 outcomes: 29 reproduced, 3 partially reproduced, 2 not reproduced and 1 blocked. Ten outcomes carry `assumed: true`.

## 1. Outcomes and their assumptions

I agree with 34 of the 35 outcomes. The exception is fascicles-larger-cervical, where I agree only with qualification.

**fascicles-larger-cervical** (reproduced, `assumed: true`). The record says Kenward-Roger is "JMP's test". The paper's own numbers do not support that. Solving each of the paper's reported (F, p) pairs for the denominator degrees of freedom gives:

| Effect | df implied by the paper | Notebook, Satterthwaite | Notebook, Kenward-Roger |
|---|---|---|---|
| Nerve diameter, level | 23.0 | 23.3 | 30.7 |
| Nerve diameter, interaction | 23.5 | 23.4 | 30.8 |
| Fascicle number, level | 19.4 | 19.3 | 17.1 |
| Fascicle number, interaction | 18.5 | 19.3 | 17.1 |
| Fascicle diameter, species | 21.1 | 20.6 | 35.8 |
| Fascicle diameter, interaction | 25.6 | 28.4 | 51.2 |

[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80
```

```
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
345:### 2. Check the data against its description
360:### 3. Write the entry
443:### 4. Lock, check and run
463:### 5. Record the attempt
538:### 6. Hand over for verification
576:## Repeat attempts
641:## Local and remote datasets
664:## Verifier
668:### Round 1: without the author's conclusions
693:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,345p docs/protocol.md; sed -n 443,580p docs/protocol.md; sed -n 693,740p docs/protocol.md
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

[... 287 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep pelot; wc -l attempts/pelot-2020-01.yaml; grep -n "fascicles-larger-cervical" -A60 attempts/pelot-2020-01.yaml | head -150
```

```
pelot-2020-01.yaml
932 attempts/pelot-2020-01.yaml
285:- claim: fascicles-larger-cervical
286-  outcome: reproduced
287-  notebook: reproduce_pelot_2020.ipynb
288:  output: claim:fascicles-larger-cervical
289-  notes: Cervical larger in each species; Tukey p with Kenward-Roger degrees of freedom human 0.000001,
290-    pig 0.012, rat 0.044 (paper < 0.0001, 0.0009, 0.0234); with the code's rat values rat 0.0089. Of the
291-    eight combinations of degrees of freedom and rat values printed, six give three species. Two give
292-    two (partially reproduced), subjects minus parameters with the largest fascicle (rat p = 0.068) and
293-    Satterthwaite with the code's rat values (pig p = 0.053). Residual degrees of freedom give pig 0.00001
294-    and rat 0.043, the bounded fit pig 0.00001 and rat 0.043. The pig contrast's Satterthwaite degrees
295-    of freedom (3.74, p = 0.048) come from the observed REML information, which differs from the expected
296-    information Kenward-Roger uses (7.55 degrees of freedom), mostly in the sample variance term (138257
297-    against 243007). A rat-only mixed model (unbounded REML, Kenward-Roger) gives p = 1.7e-07 for the
298-    largest fascicle and 0.00033 for the code's values; a paired t test on the 8 rats with both levels
299-    gives p = 8.0e-07.
300-  deviations:
301-  - The Methods fit the mixed models in JMP Pro 14.3.0 and do not give its settings. The fit here is REML
302-    with unbounded variance components, JMP's default, which statsmodels does not offer, and effects and
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "fascicles-larger-cervical" -B2 -A30 claims/pelot-2020.yaml | head -60; grep -n "^verifications\|^  - round\|^- round\|round:" attempts/pelot-2020-01.yaml; sed -n 1,20p attempts/pelot-2020-01.yaml
```

```
463-    subdiaphragmatic species pairs has p < 0.05 and the means are within the stated SDs; not
464-    reproduced when any pair differs. Effect sizes are reported either way.
465:- id: fascicles-larger-cervical
466-  statement: All three species have larger fascicles at the cervical than at the
467-    subdiaphragmatic level.
468-  source: Results, paragraph 5
469-  quote: All species had larger fascicles at the cervical level ( p < 0.0001 for humans; p =
470-    0.0009 for pigs; p = 0.0234 for rats).
471-  statistics:
472-  - about: humans, cervical against subdiaphragmatic
473-    test: Tukey's HSD
474-    p: 0.0001
475-    p_relation: "<"
476-  - about: pigs, cervical against subdiaphragmatic
477-    test: Tukey's HSD
478-    p: 0.0009
479-  - about: rats, cervical against subdiaphragmatic
480-    test: Tukey's HSD
481-    p: 0.0234
482-  data: with_inputs
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 640,700p attempts/pelot-2020-01.yaml; grep -n "^  - round\|^- round\|^  round\|reviewed:" attempts/pelot-2020-01.yaml
```

```
with the degrees of freedom (Kenward-Roger keeps all three below 0.05).
- kind: methods_unavailable
  statement: Question for the authors. What test supports 'the data did not suggest a difference in the
    relationship between perineurium thickness and fascicle diameter for cervical versus subdiaphragmatic
    nerves'? Fitting each level separately, the 95% bounds of the human slope (0.032 against 0.056) and
    of the pig intercept (5.3 against 3.2 um) do not overlap, and an F test of level terms gives p < 1e-6
    for both; only the rat fits agree.
- kind: methods_unavailable
  statement: Question for the authors. What test is behind 'our morphology metrics did not show trends
    with age' ? Supplement 6 shows the metrics against age without a test. Uncorrected Pearson correlations
    per species and level find 3 of 26 with p < 0.05, all in pigs, whose ages take four values.
verifications:
- date: '2026-11-18'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper under paper/. The verifier browsed SPARC:60 version
    5 on Pennsieve for the blocked claim and tested bwboundaries, polyarea, fit_poly1, reml_unbounded and
    tukey on synthetic inputs. Its report gave its own outcome for each of the 35 claims; all agree with
    the record as it then stood.
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; python -c "
import json
nb=json.load(open('reproduce_pelot_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(i,c['cell_type'],len(s),s[:150].replace('\n',' | '))
"; ls ../../executed/pelot-2020/ 2>/dev/null; wc -l vagus.py
```

```
0 markdown 5186 # Pelot et al. (2020), vagus nerve morphology of human, pig and rat, on SPARC:60 |  | **Paper.** Pelot, Goldhagen, Cariello, Musselman, Clissold, Ezzell a
1 code 353 import io | import time | import json | import hashlib | import resource |  | import numpy as np | import pandas as pd | import requests | from scipy import stats |  | impo
2 markdown 80 ## Data check |  | The dataset's files, its readme and the SDS sheets, every column.
3 code 485 m60 = v.manifest("60") | print(m60["name"], "version", m60["version"], m60["datePublished"], m60["@id"]) | print("related:", m60["relatedPublications"]) | f
4 code 532 subjects = v.excel("60", "files/subjects.xlsx") | samples = v.excel("60", "files/samples.xlsx") | desc = v.excel("60", "files/dataset_description.xlsx", h
5 markdown 171 The rat samples. The level comes from `specimen anatomical location` in samples.xlsx. | Each sample is measured from its primary traces with the paper's
6 code 1835 smp = samples.merge(subjects[["subject_id", "age", "body mass"]], on="subject_id", suffixes=("", "_subj")) | smp["sub"] = smp["subject_id"].str[4:].asty
7 markdown 211 Duplicates: no two traces are identical (the SHA-256 of each PeriMask's pixels), and the | files the analysis reads are the same S3 objects (same object
8 code 1484 hashes = {} | for _, row in smp.iterrows(): |     pre = v._prefix("60", row["sub"], row["sam"]) |     hashes[row["label"]] = hashlib.sha256(np.packbits(v.ti
9 markdown 309 The measurements against the output files the paper's code wrote. The code folder's | `RatVNMorphology_OutputMetrics.mat` (written 2020-09-05) holds the
10 code 1430 out_code = v.mat("60", "files/code/RatVNMorphology_OutputMetrics.mat") | out_der = v.mat("60", "files/derivative/RatVNMorphology_OutputMetrics.mat") | cmp
11 markdown 703 ### The human and pig data |  | Human: the 18 samples of the paper are those of `CadaverVNMorphology_OutputMetrics.mat` in | SPARC:65's code folder (written
12 code 2117 hum_code = v.mat("65
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/pelot-2020/reproduce_pelot_2020.ipynb'))
for i in [17,41,42,50,51,58,59,60,128]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('--- out'); print(''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain','')))
EOF
```

```
===== 17
### The mixed model tests

The mixed models are fitted by REML with unbounded variance components (`v.reml_unbounded`),
JMP's default, and each effect is tested with the Kenward-Roger F test (`v.kr_setup`,
`v.kr_test`), the test JMP reports for REML fits; Tukey's HSD uses the Kenward-Roger
adjusted covariance and degrees of freedom of each difference. Wald F tests with
Satterthwaite, residual and subject-based degrees of freedom are shown as variants. The
check below runs the Kenward-Roger code on a balanced split-plot design, where it must give
the exact F tests.
===== 41
print(tk_sp[tk_sp.pair.str.startswith("rat")].to_string(float_format=lambda x: "%.3g" % x))
for lv in ["cervical", "subdiaphragmatic"]:
    rm = by("rat", lv, "d_nerve_mm").mean()
    print(lv, "rat/human %.3f, rat/pig %.3f" % (rm / by("human", lv, "d_nerve_mm").mean(), rm / by("pig", lv, "d_nerve_mm").mean()))
print(tk_cell[tk_cell.pair.str.contains("'rat'")].to_string(float_format=lambda x: "%.3g" % x))
--- out
          pair  diff     se     t   df  p_tukey   p_satt  p_subject_df
1  rat - human -1.56 0.0596 -26.2 22.9 5.22e-15 4.12e-14      2.55e-15
2    rat - pig -1.68 0.0538 -31.2 18.2 1.22e-15  2.6e-12      2.55e-15
[... 201 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/pelot-2020/reproduce_pelot_2020.ipynb'))
for i in [18,35,36,38,39,44,45,47,48,53,54,56,57]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('--- out'); print(''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain','')))
EOF
```

```
===== 18
# Kenward-Roger check on a balanced split-plot design without random draws: 3 species x 6
# subjects, each subject at both levels, one value per cell. There the Kenward-Roger tests are
# the exact split-plot F tests: species against the between-subject error, level and the
# interaction against the within-subject error, each with 15 degrees of freedom.
k_ = np.arange(36)
toy = pd.DataFrame(dict(species=np.repeat(["a", "b", "c"], 12), subject=np.repeat(np.arange(18), 2), level=np.tile(["x", "y"], 18)))
toy["y"] = np.sin(1.7 * k_) + 0.8 * np.cos(2.3 * toy.subject) + 0.4 * (toy.level == "x") + 0.3 * (toy.species == "b")
tab_toy, _, _ = v.reml_unbounded(toy, "y", "subject")
sm_ = toy.groupby("subject").agg(species=("species", "first"), m=("y", "mean"))
d_ = toy.pivot(index="subject", columns="level", values="y")
d_ = (d_["x"] - d_["y"]).to_frame("d").join(sm_.species)
mse_ = sum(((g.d - g.d.mean()) ** 2).sum() for _, g in d_.groupby("species")) / 15
exact = [stats.f_oneway(*[g.m for _, g in sm_.groupby("species")]).statistic, d_.d.mean() ** 2 / (mse_ / 18),
         stats.f_oneway(*[g.d for _, g in d_.groupby("species")]).statistic]
print(tab_toy[["term", "df", "F_kr", "ddf_kr", "p_kr", "df_satt"]].assign(F_exact=exact, ddf_exact=15).round(4).to_string())

--- out
            term  df    F_kr  ddf_kr    p_kr  df_satt  F_exact  ddf_exact
0        species   2  0.5817    15.0  0.5711     15.0   0.5817         15
[... 249 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; grep -n "^def \|^    def " vagus.py; sed -n '/^def reml_dense/,/^def tukey/p' vagus.py
```

```
47:def manifest(ds):
57:def files(ds):
61:def read(ds, path):
78:def supplement4():
117:def supplement_zip():
131:def excel(ds, path, **kw):
135:def mat(ds, path):
139:def tif(ds, path):
147:def _label_colmajor(bw, conn):
154:def _trace(region, conn):
187:def _border(region, p):
197:def bwboundaries(bw):
209:def polyarea(rc):
214:def centroid(rc):
221:def eff_d(area):
225:def scale_um_per_px(scalemask, slength):
234:def analyze(outer, inner, nerve, um):
290:def _prefix(ds, sub, sam):
297:def rat_sample(sub, sam):
319:def human_sample(sub, sam):
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; sed -n 410,460p vagus.py; sed -n 506,682p vagus.py
```

```
def sm_fit(res):
    """The fixed effects of a statsmodels MixedLM fit, in the form tukey() takes."""
    names = list(res.fe_params.index)
    return dict(beta=res.fe_params, cov=res.cov_params().loc[names, names].values,
                dfres=int(res.model.nobs - len(names)))


def tukey(fit, df, pairs, which, factors=("species", "level")):
    """Tukey HSD on least squares means of a mixed model fit (dict of beta, cov, dfres).
    `which` is "a" for the main-effect means of the first factor (averaged over the levels
    of the second) or "cell" for the species by level cells. Each pair's t is the
    difference over its SE from the fixed-effect covariance; p from the studentized range
    with k means and dfres degrees of freedom, or, when fit["satt"] is set, the
    Satterthwaite degrees of freedom of each difference. When fit["use_kr"] is set, the SE
    comes from the Kenward-Roger adjusted covariance and the degrees of freedom are the
    Kenward-Roger ones of each difference (JMP's Tukey HSD on the least squares means of a
    REML fit; assumption, as the paper gives no settings)."""
    from scipy import stats
    import patsy
    a, b = factors
[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat executed/pelot-2020/result.json | head -30; python - <<'EOF'
import json
nb=json.load(open('executed/pelot-2020/reproduce_pelot_2020.ipynb'))
c=nb['cells'][127]
for o in c.get('outputs',[]): print(''.join(o.get('text',''))[:600])
EOF
```

```
{
 "entry": "pelot-2020",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_pelot_2020.ipynb",
   "ok": true,
   "seconds": 291,
   "error": null
  }
 ]
}
total time 284 s, max rss 0.93 GB
files read, SHA-256:
  SPARC:60 v5 files/code/RAbdominalAnteriorFemale.xlsx c3c48b2c7f737c5183de17da5f1005bc2755349576efba3f378b9457cc78d888
  SPARC:60 v5 files/code/RAbdominalAnteriorMale.xlsx 71844b006d8e5b8d7a2992363fbeb9444cfdcd533f0588cdfd0bd66bb49285dc
  SPARC:60 v5 files/code/RAbdominalPosteriorFemale.xlsx 584660a8161147786da8c27179879647457512e9659e9f52369ce66ee7161728
  SPARC:60 v5 files/code/RCervicalLeftFemale.xlsx 02797d79d9b4d9fdb5ba149453ef1f25ad29bfbffe258b3890a78c4c8610834f
  SPARC:60 v5 files/code/RCervicalLeftMale.xlsx 930a7f5883341ea6ed959a1
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/entry.py | head -80; ls -a executed/pelot-2020; ls ~/.cache 2>/dev/null | head
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; date -u; python - <<'EOF'
import json
nb=json.load(open('reproduce_pelot_2020.ipynb'))
src=[]
for i,c in enumerate(nb['cells'][:54]):
    if c['cell_type']=='code': src.append(''.join(c['source']))
src.append("import pickle,os; pickle.dump(dict(S=S,FA=FA,HP=HP), open(os.environ['TMPDIR']+'/pelot.pkl','wb'))")
open('/tmp/claude/proto.py','w').write('\n\n'.join(src)) if False else None
import os
open(os.environ['TMPDIR']+'/proto.py','w').write('\n\n'.join(src))
EOF
time ../../executed/pelot-2020/.venv/bin/python $TMPDIR/proto.py > $TMPDIR/proto.log 2>&1; tail -3 $TMPDIR/proto.log
```

```
Wed Nov 18 05:05:54 UTC 2026

real	0m1.164s
user	0m1.398s
sys	0m0.108s
  File "/tmp/claude-1001/proto.py", line 12, in <module>
    import vagus as v
ModuleNotFoundError: No module named 'vagus'
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; time PYTHONPATH=. ../../executed/pelot-2020/.venv/bin/python $TMPDIR/proto.py > $TMPDIR/proto.log 2>&1; tail -3 $TMPDIR/proto.log
```

```
real	2m48.397s
user	2m12.443s
sys	0m25.842s
0  ('human', 'cervical') - ('pig', 'cervical')  0.35512  0.06549  5.42270   32.70477  0.00007  21.40958  0.00024       0.00009     0.00000     0.00011          0.00033                0.00013          0.00000
1  ('rat', 'cervical') - ('human', 'cervical') -0.13210  0.09346 -1.41342  118.30082  0.71886  78.71922  0.71585       0.71593     0.71587     0.72435          0.72135                0.72128          0.73396
2    ('rat', 'cervical') - ('pig', 'cervical')  0.22302  0.08909  2.50336   98.06126  0.13319  64.20073  0.13739       0.15516     0.12311     0.14264          0.14722                0.16408          0.12354
```

**Agent**

Data tables are cached. Now I'm testing whether Kenward-Roger computed from the observed information gives the paper's degrees of freedom.

**Agent calls Bash**

```bash
cd entries/pelot-2020; cat > $TMPDIR/p2.py <<'EOF'
import pickle,os,numpy as np
from scipy import stats, optimize
import vagus as v
d=pickle.load(open(os.environ['TMPDIR']+'/pelot.pkl','rb')); S,FA,HP=d['S'],d['FA'],d['HP']
# implied ddf
def implied(F,q,p):
    return optimize.brentq(lambda m: stats.f.sf(F,q,m)-p, 1.01, 1e4)
paper={'nd':[('species',2,577.1,None),('level',1,11.01,0.0030),('species:level',2,2.445,0.1085)],
       'nf':[('species',1,213.8,None),('level',1,5.486,0.0300),('species:level',1,2.481,0.1322)],
       'fd':[('species',2,8.989,0.0015),('level',1,51.88,None),('species:level',2,5.273,0.0121)]}
fits={}
fits['nd']=v.reml_unbounded(S,"d_nerve_mm","subject")
fits['nf']=v.reml_unbounded(HP.assign(n_fasc=HP.n_fasc.astype(float)),"n_fasc","subject")
fits['fd']=v.reml_unbounded(FA,"log_d","subject",nested="sample")
fits['fdc']=v.reml_unbounded(FA,"log_d_code","subject",nested="sample",x0=fits['fd'][2]["theta"])
for k,(tab,vc,fit) in fits.items():
    th=fit['theta']; J=np.diag(np.r_[np.exp(th[0]),np.ones(len(th)-1)])
    Wobs=J@np.linalg.inv(fit['H'])@J
    s=dict(fit['kr']); s['W']=Wobs
    # recompute PhiA with Wobs: need Q terms; approximate by rebuilding
    print(k, 'W exp', np.round(fit['kr']['W'],6).tolist(), 'W obs', np.round(Wobs,6).tolist())
    names=list(fit['beta'].index); p=len(names)
    for i,row in tab.iterrows():
        idx=[j for j,n in enumerate(names) if (row.term=='species' and n.startswith('C(species') and ':' not in n) or (row.term=='level' and n.startswith('C(level') and ':' not in n) or (':' in row.term and ':' in n)]
        kr=v.kr_test(s, np.eye(p)[idx])
        pp=[x for x in paper.get(k,[]) if x[0]==row.term]
        imp=implied(pp[0][2],pp[0][1],pp[0][3]) if pp and pp[0][3] else None
        print('  %-14s Wald F %.3f satt %.2f | KR exp F %.3f ddf %.2f | KR obs(W only) F %.3f ddf %.2f p %.4g | paper F %s implied ddf %s'%(row.term,row.F,row.df_satt,row.F_kr,row.ddf_kr,kr['F'],kr['ddf'],kr['p'], pp[0][2] if pp else '', '%.2f'%imp if imp else ''))
EOF
PYTHONPATH=. ../../executed/pelot-2020/.venv/bin/python $TMPDIR/p2.py 2>&1 | grep -v Warn
```

```
nd W exp [[0.001185, -0.000606], [-0.000606, 0.000325]] W obs [[0.001638, -0.000897], [-0.000897, 0.000512]]
  species        Wald F 599.607 satt 14.10 | KR exp F 587.305 ddf 21.06 | KR obs(W only) F 587.058 ddf 14.14 p 2.487e-14 | paper F 577.1 implied ddf 
  level          Wald F 11.047 satt 23.30 | KR exp F 11.026 ddf 30.68 | KR obs(W only) F 11.026 ddf 23.30 p 0.002944 | paper F 11.01 implied ddf 22.97
  species:level  Wald F 2.455 satt 23.38 | KR exp F 2.450 ddf 30.76 | KR obs(W only) F 2.450 ddf 23.38 p 0.1082 | paper F 2.445 implied ddf 23.48
nf W exp [[181.718399, -127.654192], [-127.654192, 225.402067]] W obs [[150.790837, -87.790781], [-87.790781, 174.020758]]
  species        Wald F 216.679 satt 22.99 | KR exp F 212.857 ddf 21.03 | KR obs(W only) F 212.857 ddf 22.99 p 4.116e-13 | paper F 213.8 implied ddf 
  level          Wald F 5.788 satt 19.31 | KR exp F 5.393 ddf 17.07 | KR obs(W only) F 5.393 ddf 19.31 p 0.03129 | paper F 5.486 implied ddf 19.35
  species:level  Wald F 2.608 satt 19.31 | KR exp F 2.430 ddf 17.07 | KR obs(W only) F 2.430 ddf 19.31 p 0.1353 | paper F 2.481 implied ddf 18.47
fd W exp [[4e-06, -0.0, -0.0], [-0.0, 3.3e-05, -3e-06], [-0.0, -3e-06, 4e-06]] W obs [[4e-06, -1e-06, -0.0], [-1e-06, 6.2e-05, -1e-05], [-0.0, -1e-05, 9e-06]]
  species        Wald F 9.740 satt 20.61 | KR exp F 9.658 ddf 35.78 | KR obs(W only) F 9.647 ddf 21.26 p 0.001044 | paper F 8.989 implied ddf 21.11
  level          Wald F 48.031 satt 72.70 | KR exp F 47.327 ddf 132.68 | KR obs(W only) F 47.327 ddf 72.70 p 1.771e-09 | paper F 51.88 implied ddf 
  species:level  Wald F 5.457 satt 28.37 | KR exp F 5.203 ddf 51.18 | KR obs(W only) F 5.173 ddf 26.71 p 0.01262 | paper F 5.273 implied ddf 25.56
fdc W exp [[4e-06, -0.0, -0.0], [-0.0, 3.7e-05, -3e-06], [-0.0, -3e-06, 5e-06]] W obs [[4e-06, -1e-06, -0.0], [-1e-06, 6.9e-05, -1.1e-05], [-0.0, -1.1e-05, 1e-05]]
  species        Wald F 9.127 satt 20.55 | KR exp F 9.052 ddf 35.39 | KR obs(W only) F 9.042 ddf 21.16 p 0.00145
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; python - <<'EOF'
p='vagus.py'; s=open(p).read()
s=s.replace('''def kr_setup(X, y, G, lin):
    """The quantities''','''def kr_setup(X, y, G, lin, W=None):
    """The quantities''')
s=s.replace('''    it is computed here with dense matrices."""
    Vi = np.linalg.inv''','''    it is computed here with dense matrices. W may be given in place of the expected
    information's inverse, for the variant on the observed information."""
    Vi = np.linalg.inv''')
s=s.replace('''    W = np.linalg.inv(np.array([[0.5 * np.sum(PG[i] * PG[j].T) for j in range(k)] for i in range(k)]))
''','''    if W is None:
        W = np.linalg.inv(np.array([[0.5 * np.sum(PG[i] * PG[j].T) for j in range(k)] for i in range(k)]))
''')
s=s.replace('''    fit["kr"] = kr_setup(Xv, yv, G, np.r_[np.exp(th[0]), th[1:]])
''','''    fit["kr"] = kr_setup(Xv, yv, G, np.r_[np.exp(th[0]), th[1:]])
    # the same with the observed information (the Hessian H, mapped from theta to the linear
    # parameters), the information the Satterthwaite degrees of freedom use
    J = np.diag(np.r_[np.exp(th[0]), np.ones(k - 1)])
    fit["kr_obs"] = kr_setup(Xv, yv, G, np.r_[np.exp(th[0]), th[1:]], W=J @ np.linalg.inv(H) @ J)
''')
s=s.replace('''        row["F_kr"], row["ddf_kr"], row["p_kr"] = kr["F"], kr["ddf"], kr["p"]
''','''        row["F_kr"], row["ddf_kr"], row["p_kr"] = kr["F"], kr["ddf"], kr["p"]
        kro = kr_test(fit["kr_obs"], Lm)
        row["F_kr_obs"], row["ddf_kr_obs"], row["p_kr_obs"] = kro["F"], kro["ddf"], kro["p"]
''')
s=s.replace('''        if fit.get("use_kr"):
            se = float(np.sqrt(c @ fit["kr"]["PhiA"] @ c))
            dfp = kr_test(fit["kr"], c)["ddf"]''','''        if fit.get("use_kr"):
            krs = fit["kr_obs"] if fit["use_kr"] == "obs" else fit["kr"]
            se = float(np.sqrt(c @ krs["PhiA"] @ c))
            dfp = kr_test(krs, c)["ddf"]''')
open(p,'w').write(s)
EOF
grep -n "kr_obs\|use_kr" vagus.py
```

```
423:    Satterthwaite degrees of freedom of each difference. When fit["use_kr"] is set, the SE
444:        if fit.get("use_kr"):
445:            krs = fit["kr_obs"] if fit["use_kr"] == "obs" else fit["kr"]
610:    fit["kr_obs"] = kr_setup(Xv, yv, G, np.r_[np.exp(th[0]), th[1:]], W=J @ np.linalg.inv(H) @ J)
617:        kro = kr_test(fit["kr_obs"], Lm)
618:        row["F_kr_obs"], row["ddf_kr_obs"], row["p_kr_obs"] = kro["F"], kro["ddf"], kro["p"]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; cat > $TMPDIR/p3.py <<'EOF'
import pickle,os,numpy as np, pandas as pd
import vagus as v
d=pickle.load(open(os.environ['TMPDIR']+'/pelot.pkl','rb')); S,FA,HP=d['S'],d['FA'],d['HP']
pd.set_option('display.width',250)
cols=['term','F','df_satt','p_satt','F_kr','ddf_kr','p_kr','F_kr_obs','ddf_kr_obs','p_kr_obs']
tnd,_,fnd=v.reml_unbounded(S,"d_nerve_mm","subject"); print(tnd[cols].round(4))
tnf,_,fnf=v.reml_unbounded(HP.assign(n_fasc=HP.n_fasc.astype(float)),"n_fasc","subject"); print(tnf[cols].round(4))
tfd,_,ffd=v.reml_unbounded(FA,"log_d","subject",nested="sample"); print(tfd[cols].round(4))
tfc,_,ffc=v.reml_unbounded(FA,"log_d_code","subject",nested="sample",x0=ffd["theta"]); print(tfc[cols].round(4))
pairs_l = [((sp, "cervical"), (sp, "subdiaphragmatic")) for sp in ["human", "pig", "rat"]]
for nm,f in [('largest',ffd),('code',ffc)]:
    for mode in [True,'obs']:
        print(nm,mode); print(v.tukey(dict(f,use_kr=mode),FA,pairs_l,"cell")[0].round(5).to_string())
pairs_c = [(("human", "cervical"), ("pig", "cervical")), (("rat", "cervical"), ("human", "cervical")), (("rat", "cervical"), ("pig", "cervical"))]
pairs_a = [(("human", "subdiaphragmatic"), ("pig", "subdiaphragmatic")), (("human", "subdiaphragmatic"), ("rat", "subdiaphragmatic")),(("pig", "subdiaphragmatic"), ("rat", "subdiaphragmatic"))]
print(v.tukey(dict(ffd,use_kr='obs'),FA,pairs_c+pairs_a,"cell")[0].round(5).to_string())
print(v.tukey(dict(ffc,use_kr='obs'),FA,pairs_c+pairs_a,"cell")[0].round(5).to_string())
print(v.tukey(dict(fnd,use_kr='obs'),S,[("human", "pig"), ("rat", "human"), ("rat", "pig")],"a")[0].to_string())
EOF
PYTHONPATH=. ../../executed/pelot-2020/.venv/bin/python $TMPDIR/p3.py 2>&1 | grep -v Warn
```

```
term         F  df_satt  ...  F_kr_obs  ddf_kr_obs  p_kr_obs
0        species  599.6068  14.1041  ...  577.0403     14.1379    0.0000
1          level   11.0466  23.2961  ...   11.0076     23.2962    0.0030
2  species:level    2.4549  23.3808  ...    2.4455     23.3822    0.1085

[3 rows x 10 columns]
            term         F  df_satt  ...  F_kr_obs  ddf_kr_obs  p_kr_obs
0        species  216.6785  22.9898  ...  213.7939     22.9898    0.0000
1          level    5.7881  19.3107  ...    5.4860     19.3108    0.0300
2  species:level    2.6076  19.3107  ...    2.4715     19.3108    0.1322

[3 rows x 10 columns]
            term        F  df_satt  ...  F_kr_obs  ddf_kr_obs  p_kr_obs
0        species   9.7401  20.6143  ...    9.5883     21.2623    0.0011
1          level  48.0312  72.7024  ...   46.5291     72.7024    0.0000
2  species:level   5.4574  28.3653  ...    4.9336     26.7138    0.0150

[3 rows x 10 columns]
            term        F  df_satt  ...  F_kr_obs  ddf_kr_obs  p_kr_obs
0        species   9.1269  20.5479  ...    8.9892     21.1586    0.0015
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/pelot-2020.yaml'))
for cl in c['claims']:
    if cl['id'] in ['nerve-diameter-anova','human-pig-nerve-diameter-similar','rat-ten-times-smaller','nerve-cervical-larger','fascicle-number-human-pig','fascicle-diameter-anova','cervical-fascicle-diameter-species','subdiaphragmatic-fascicle-diameter-comparable']:
        print(cl['id'],'::',cl['criterion'],'\n')
EOF
../executed/pelot-2020/.venv/bin/python -c "
from scipy import stats, optimize
t=4.71728; q=t*2**.5
for df in [3.64,5,8,10,15,20,30,50,100]: print(df, stats.studentized_range.sf(q,6,df))
print(optimize.brentq(lambda d: stats.studentized_range.sf(q,6,d)-0.0009,4,1000))
t=4.76677; print(optimize.brentq(lambda d: stats.studentized_range.sf(t*2**.5,6,d)-0.0009,4,1000))
" 2>/dev/null || executed/pelot-2020/.venv/bin/python -c "
from scipy import stats, optimize
t=4.71728; q=t*2**.5
print(optimize.brentq(lambda d: stats.studentized_range.sf(q,6,d)-0.0009,4,1000))
t=4.76677; print(optimize.brentq(lambda d: stats.studentized_range.sf(t*2**.5,6,d)-0.0009,4,1000))
"
```

```
nerve-diameter-anova :: As in the Methods (Statistics and Data Analyses), a mixed model ANOVA of effective nerve diameter with fixed effects species, level and their interaction and a random effect of subject, on the 54 samples (rat from the dataset, human from Pelot et al. 2020a, pig MT from Pelot et al. 2020f), REML as the standard estimation choice. Reproduced when species and level have p < 0.05 and the interaction has p >= 0.05 (the absence is judged on this test). Partially reproduced when species and level hold but the interaction is significant. The F values are reported against the paper's. 

human-pig-nerve-diameter-similar :: A claim of absence, judged on the paper's test, Tukey's HSD after the model of nerve-diameter-anova. Reproduced when the means are within the stated SDs and the human against pig comparison has p >= 0.05. The paper prints one p for both levels, and the model has no detected interaction, so the test is read as the species main-effect contrast human against pig; human against pig at each level in the species by level Tukey is shown as a variant. The effect size is reported either way. 

rat-ten-times-smaller :: Tukey's HSD after the model of nerve-diameter-anova. The paper's "both comparisons of rat to larger species" are rat against human and rat against pig, one p for both levels, read as the species main-effect contrasts; the same contrasts at each level are shown as a variant. Reproduced when rat against human and rat against pig both have p < 0.0001 with rat smaller, and the ratio of the rat mean to each larger species' mean is between 0.05 and 0.2 at each level ("approximately ten times" read as a factor of 5 to 20, a choice of this file; 0.260/2.2 and 0.135/1.6 from the paper's means give 0.12 and 0.08). Partially reproduced when p < 0.05 but not below 0.0001. 

nerve-cervical-larger :: Reproduced when the level effect of nerve-diameter-anova has p < 0.05 with the cervical least squares mean larger, and the relative difference o
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; python - <<'EOF'
import json
nb=json.load(open('reproduce_pelot_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if any(k in s for k in ['Kenward','use_kr','p_kr','F_kr','Satterthwaite','JMP']):
        print('=====',i,c['cell_type']); print(s if c['cell_type']=='markdown' else '\n'.join(l for l in s.split('\n') if any(k in l for k in ['Kenward','use_kr','p_kr','F_kr','Satterthwaite','satt','JMP'])))
EOF
```

```
===== 0 markdown
# Pelot et al. (2020), vagus nerve morphology of human, pig and rat, on SPARC:60

**Paper.** Pelot, Goldhagen, Cariello, Musselman, Clissold, Ezzell and Grill (2020),
"Quantified Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig,
and Rat", Front. Neurosci. 14, 601479, doi:10.3389/fnins.2020.601479. The claims file
(`claims/pelot-2020.yaml`) was written from the version of record (Europe PMC, PMC7672126),
without the supplement and with Eqs. 1 to 4 lost in the text.

**Dataset.** SPARC:60, "Quantified morphology of the rat vagus nerve", version 5
(doi:10.26275/lg3c-1kjf, published 2025-02-24), read from the public SPARC bucket at the
object versions its manifest gives. Version 5 is the latest and the version the run was
given; the paper cites none. Versions 1 to 4 date from 2020; the data check below compares
the files the analysis reads in version 5 with version 4 (2020-09-30), the version current
when the paper was published.

**Sister datasets.** The paper's human and pig data are in three other SPARC datasets that
list the paper as `IsDescribedBy`: SPARC:65 (human anti-claudin-1 IHC), SPARC:64 (pig
Masson's trichrome) and SPARC:89 (pig anti-fibronectin IF), the paper's Pelot et al. (2020a,
f and b). They are used for the claims the claims file marks `with_inputs` or `elsewhere`.
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; python - <<'EOF'
import json
nb=json.load(open('reproduce_pelot_2020.ipynb'))
for i in [15,44,49,52,55]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
```

```
===== 15
### Tables used by the claims

One row per sample for nerve-level measures and one per fascicle for fascicle diameters.
Rat statistics use one fascicle per sample (Methods, "Imaging and Image Analysis",
paragraph 2: "for all statistics, we only used the largest fascicle in each rat sample,
using the outer perineurial boundary as the nerve boundary"). The largest fascicle is
taken here by endoneurial area. `DataPlotting_v4.m` takes the largest outer perineurium
for the nerve, but for the fascicle diameter the first inner trace in its order
(`fasc_ind == 1`), which in R22-1 and R23-1 is not the largest fascicle; the code's values
are shown as a variant wherever they differ.
===== 44
lsm = {}
for lv in ["cervical", "subdiaphragmatic"]:
    lsm[lv] = np.mean([means_cell[(sp, lv)] for sp in ["human", "pig", "rat"]])
print("level effect: Kenward-Roger F = %.3f, p = %.4g (Satterthwaite %.4g, residual df %.4g, subject df %.4g) | least squares means, cervical %.4f mm, subdiaphragmatic %.4f mm" %
      (tab_nd.F_kr[1], tab_nd.p_kr[1], tab_nd.p_satt[1], tab_nd.p_resid_df[1], tab_nd.p_subject_df[1], lsm["cervical"], lsm["subdiaphragmatic"]))
rel = {}
for sp in ["human", "pig", "rat"]:
    c, a = by(sp, "cervical", "d_nerve_mm").mean(), by(sp, "subdiaphragmatic", "d_nerve_mm").mean()
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; cat > $TMPDIR/ed1.py <<'EOF'
import json
p='reproduce_pelot_2020.ipynb'
nb=json.load(open(p))
def src(i): return ''.join(nb['cells'][i]['source'])
def setsrc(i,s): nb['cells'][i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))
rep(18,'print(tab_toy[["term", "df", "F_kr", "ddf_kr", "p_kr", "df_satt"]]','print(tab_toy[["term", "df", "F_kr_obs", "ddf_kr_obs", "F_kr", "ddf_kr", "p_kr", "df_satt"]]')
rep(38,'fit_nd_t = dict(fit_nd, use_kr=True)','fit_nd_t = dict(fit_nd, use_kr="obs")')
rep(38,'''tk_sp["p_satt"] =''','''tk_sp["p_kr_expected"] = v.tukey(dict(fit_nd, use_kr=True), S, [("human", "pig"), ("rat", "human"), ("rat", "pig")], "a")[0]["p_tukey"]
tk_sp["p_satt"] =''')
rep(44,'''print("level effect: Kenward-Roger F = %.3f, p = %.4g (Satterthwaite %.4g, residual df %.4g, subject df %.4g) | least squares means, cervical %.4f mm, subdiaphragmatic %.4f mm" %
      (tab_nd.F_kr[1], tab_nd.p_kr[1], tab_nd.p_satt[1],''','''print("level effect: Kenward-Roger (observed information) F = %.3f, p = %.4g (expected information %.4g, Satterthwaite %.4g, residual df %.4g, subject df %.4g) | least squares means, cervical %.4f mm, subdiaphragmatic %.4f mm" %
      (tab_nd.F_kr_obs[1], tab_nd.p_kr_obs[1], tab_nd.p_kr[1], tab_nd.p_satt[1],''')
rep(53,'tk_fd, means_fd = v.tukey(dict(fit_fd, use_kr=True)','tk_fd, means_fd = v.tukey(dict(fit_fd, use_kr="obs")')
rep(53,'''tk_satt_ = v.tukey(''','''tk_fd["p_kr_expected"] = v.tukey(dict(fit_fd, use_kr=True), FA, pairs_c + pairs_a + pairs_l, "cell")[0]["p_tukey"]
tk_satt_ = v.tukey(''')
rep(53,'''tk_fd["p_code_rat"] = v.tukey(dict(fit_fdc, use_kr=True), FA, pairs_c + pairs_a + pairs_l, "cell")[0]["p_tukey"]''',
'''tk_fd["p_code_rat"] = v.tukey(dict(fit_fdc, use_kr="obs"), FA, pairs_c + pairs_a + pairs_l, "cell")[0]["p_tukey"]
tk_fd["p_code_rat_kr_expected"] = v.tukey(dict(fit_fdc, use_kr=True), FA, pairs_c + pairs_a + pairs_l, "cell")[0]["p_tukey"]''')
rep(59,'''cols = ["pair", "diff", "df", "p_tukey", "df_satt", "p_satt", "p_resid_df", "p_subject_df", "p_tukey_bounded", "p_code_rat",
        "p_code_rat_satt", "p_code_rat_subject_df"]''','''cols = ["pair", "diff", "df", "p_tukey", "p_kr_expected", "df_satt", "p_satt", "p_resid_df", "p_subject_df", "p_tukey_bounded",
        "p_code_rat", "p_code_rat_kr_expected", "p_code_rat_satt", "p_code_rat_subject_df"]''')
rep(59,'''print("the pig contrast's degrees of freedom: Kenward-Roger (expected REML information) %.2f, Satterthwaite (observed information) %.2f"
      % (tl["df"].iloc[1], tl["df_satt"].iloc[1]))''','''pig_c = [c_ for c_ in [("pig", "cervical"), ("pig", "subdiaphragmatic")]]
print("the pig contrast's degrees of freedom: Kenward-Roger on the observed information %.2f, on the expected information %.2f, Satterthwaite %.2f"
      % (tl["df"].iloc[1], v.tukey(dict(fit_fd, use_kr=True), FA, [tuple(pig_c)], "cell")[0]["df"].iloc[0], tl["df_satt"].iloc[1]))
t_pig = abs(tl["t"].iloc[1])
print("degrees of freedom at which the pig Tukey p (t = %.3f, 6 means) would be the paper's 0.0009: %.1f"
      % (t_pig, optimize.brentq(lambda d_: stats.studentized_range.sf(t_pig * np.sqrt(2), 6, d_) - 0.0009, 3, 1000)))''')
rep(59,'"cervical minus subdiaphragmatic %.4f (log10), Kenward-Roger F','"cervical minus subdiaphragmatic %.4f (log10), Kenward-Roger (expected information) F')
# new cell after 51: paper's (F, p) against each test
new_md='''### Which test the paper's F and p come from

The paper gives F and p for nine effects (three models). Each (F, p) pair fixes the
denominator degrees of freedom the paper used. Below, those degrees of freedom are solved
for and set beside the Wald F with Satterthwaite degrees of freedom, the Kenward-Roger test
on the expected REML information (Kenward and Roger, 1997) and the Kenward-Roger test on
the observed information (the Hessian of the REML log-likelihood, the information the
Satterthwaite degrees of freedom use), for the fascicle diameter model with both rat rules.'''
new_code='''from scipy import optimize
paper_fp = {"nerve diameter": (tab_nd, [(577.1, None), (11.01, 0.0030), (2.445, 0.1085)]),
            "fascicle number": (tab_nf, [(213.8, None), (5.486, 0.0300), (2.481, 0.1322)]),
            "fascicle diameter, largest fascicle": (tab_fd, [(8.989, 0.0015), (51.88, None), (5.273, 0.0121)]),
            "fascicle diameter, code's rat values": (tab_fdc, [(8.989, 0.0015), (51.88, None), (5.273, 0.0121)])}
rows_fp = []
for model, (tab_, fp) in paper_fp.items():
    for (_, r_), (F_p, p_p) in zip(tab_.iterrows(), fp):
        ddf_p = optimize.brentq(lambda m: stats.f.sf(F_p, r_.df, m) - p_p, 1.01, 1e4) if p_p else np.nan
        rows_fp.append(dict(model=model, term=r_.term, F_paper=F_p, p_paper=p_p, ddf_paper=ddf_p, F_wald=r_.F, ddf_satt=r_.df_satt,
                            p_satt=r_.p_satt, F_kr_exp=r_.F_kr, ddf_kr_exp=r_.ddf_kr, p_kr_exp=r_.p_kr,
                            F_kr_obs=r_.F_kr_obs, ddf_kr_obs=r_.ddf_kr_obs, p_kr_obs=r_.p_kr_obs))
FP = pd.DataFrame(rows_fp)
pd.set_option("display.width", 250)
print(FP.round(4).to_string())
for col in ["F_wald", "F_kr_exp", "F_kr_obs"]:
    m_ = FP.model != "fascicle diameter, largest fascicle"
    print("%-9s largest relative difference from the paper's F (rat values as the code takes them): %.2f%%"
          % (col, 100 * (FP[m_][col] / FP[m_].F_paper - 1).abs().max()))'''
def mk(t,s):
    c={'cell_type':t,'metadata':{},'source':s.splitlines(keepends=True)}
    if t=='code': c.update(outputs=[],execution_count=None)
    return c
assert src(51).startswith('**Result: reproduced.** On log10')
nb['cells'][52:52]=[mk('markdown',new_md),mk('code',new_code)]
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; python $TMPDIR/ed1.py && git diff --stat
```

```
entries/pelot-2020/vagus.py | 19 ++++++++++++++-----
 1 file changed, 14 insertions(+), 5 deletions(-)
 entries/pelot-2020/reproduce_pelot_2020.ipynb | 70 ++++++++++++++++++++++-----
 entries/pelot-2020/vagus.py                   | 19 ++++++--
 2 files changed, 73 insertions(+), 16 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; python - <<'EOF'
p='vagus.py'; s=open(p).read()
a='''    Satterthwaite degrees of freedom of each difference. When fit["use_kr"] is set, the SE
    comes from the Kenward-Roger adjusted covariance and the degrees of freedom are the
    Kenward-Roger ones of each difference (JMP's Tukey HSD on the least squares means of a
    REML fit; assumption, as the paper gives no settings)."""'''
assert a in s
s=s.replace(a,'''    Satterthwaite degrees of freedom of each difference. When fit["use_kr"] is set, the SE
    comes from the Kenward-Roger adjusted covariance and the degrees of freedom are the
    Kenward-Roger ones of each difference, on the observed information when it is "obs"
    (the main test here, the one that gives the paper's F and p) and on the expected
    information otherwise (assumption, as the paper gives no settings)."""''')
a='''    variance components. Each effect is tested with the Kenward-Roger F (F_kr, ddf_kr,
    p_kr), JMP's test for REML fits and the main result; as variants, the Wald F with'''
assert a in s
s=s.replace(a,'''    variance components. Each effect is tested with the Kenward-Roger F on the observed
    information (F_kr_obs, ddf_kr_obs, p_kr_obs), the main result, which gives the paper's F
    and p; as variants, the Kenward-Roger F on the expected information (F_kr, ddf_kr,
    p_kr), the Wald F with''')
open(p,'w').write(s)
EOF
sed -n 506,525p vagus.py
```

```
def reml_unbounded(df, y, groups, factors=("species", "level"), nested=None, x0=None):
    """REML fit of the same mixed model with unbounded variance components: the subject
    (and sample) variance components may be negative, as long as each subject's covariance
    matrix stays positive definite. JMP's REML uses unbounded variance components by default
    (Fit Model, "Unbounded Variance Components"), which statsmodels does not offer; this
    is the replacement. Fixed effects by generalised least squares; each effect is tested
    with a Wald F (type III, sum-to-zero coding). Returns the fixed-effect table and the
    variance components. Each effect is tested with the Kenward-Roger F on the observed
    information (F_kr_obs, ddf_kr_obs, p_kr_obs), the main result, which gives the paper's F
    and p; as variants, the Kenward-Roger F on the expected information (F_kr, ddf_kr,
    p_kr), the Wald F with
    Satterthwaite degrees of freedom from the observed REML information (as lmerTest),
    with the residual degrees of freedom (n minus the number of fixed parameters), and with
    the number of subjects minus the number of fixed parameters, an ad hoc conservative
    bound."""
    import patsy
    from scipy import optimize, stats
    a, b = factors
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py run entries/pelot-2020 2>&1 | tail -5
```

```
Wed Nov 18 05:11:03 UTC 2026
Installed kernelspec registry-pelot-2020 in executed/pelot-2020/.venv/share/jupyter/kernels/registry-pelot-2020
pass  reproduce_pelot_2020.ipynb  (213 s)

real	3m41.462s
user	2m26.906s
sys	0m30.668s
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open('executed/pelot-2020/reproduce_pelot_2020.ipynb'))
for i in map(int,sys.argv[1:]):
    c=nb['cells'][i]
    print('=====',i, ''.join(c['source'])[:80])
    for o in c.get('outputs',[]):
        t=''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain',''))
        if 'Warning' in t and len(t)<400: continue
        print(t)
EOF
python $TMPDIR/show.py 18 35 38 41 44 47 50 53 54 56 58 61
```

```
===== 18 # Kenward-Roger check on a balanced split-plot design without random draws: 3 sp
            term  df  F_kr_obs  ddf_kr_obs    F_kr  ddf_kr    p_kr  df_satt  F_exact  ddf_exact
0        species   2    0.5817        15.0  0.5817    15.0  0.5711     15.0   0.5817         15
1          level   1    2.6863        15.0  2.6863    15.0  0.1220     15.0   2.6863         15
2  species:level   2    0.1788        15.0  0.1788    15.0  0.8380     15.0   0.1788         15

===== 35 tab_nd, vc_nd, fit_nd = v.reml_unbounded(S, "d_nerve_mm", "subject")
print("unbo
unbounded REML: variance components {'residual': 0.12664, 'subject': -0.05201} | converged: True
            term  df          F  p_resid_df  p_subject_df       F_kr    ddf_kr     p_kr   F_kr_obs  ddf_kr_obs  p_kr_obs   df_satt   p_satt
0        species   2  599.60677     0.00000       0.00000  587.30463  21.05968  0.00000  577.04027    14.13793   0.00000  14.10414  0.00000
1          level   1   11.04661     0.00171       0.00241   11.02577  30.67993  0.00233   11.00761    23.29617   0.00296  23.29612  0.00292
2  species:level   2    2.45488     0.09659       0.10353    2.44987  30.75990  0.10297    2.44550    23.38220   0.10854  23.38083  0.10771

variant, statsmodels REML (bounded): subject variance 0.00000
            term  df          F        p
0        species   2  283.82856  0.00000
1          level   1   21.06122  0.00000
2  species:level   2    3.71209  0.02443
paper: species F = 577.1 p < 0.0001; level F = 11.01 p = 0.0030; interaction F = 2.445 p = 0.1085
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py 55 | tail -5
```

```
pair     diff       se        t        df  p_tukey  p_kr_expected   df_satt   p_satt  p_subject_df  p_resid_df  p_code_rat  p_code_rat_kr_expected  p_code_rat_satt  p_code_rat_subject_df  p_tukey_bounded
0  ('human', 'cervical') - ('pig', 'cervical')  0.35512  0.06604  5.37716  21.40959  0.00030        0.00007  21.40958  0.00024       0.00009     0.00000     0.00039                 0.00011          0.00033                0.00013          0.00000
1  ('rat', 'cervical') - ('human', 'cervical') -0.13210  0.09380 -1.40837  78.71923  0.72189        0.71886  78.71922  0.71585       0.71593     0.71587     0.72729                 0.72435          0.72135                0.72128          0.73396
2    ('rat', 'cervical') - ('pig', 'cervical')  0.22302  0.08923  2.49934  64.20073  0.13963        0.13319  64.20073  0.13739       0.15516     0.12311     0.14947                 0.14264          0.14722                0.16408          0.12354
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/pelot-2020/reproduce_pelot_2020.ipynb'))
for i in [11,12,13,23,24,33,127,128]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source']) if c['cell_type']=='markdown' else ''.join(c['source'])[:1500])
    for o in c.get('outputs',[]):
        t=''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain',''))
        print('--out'); print(t[:2500])
EOF
```

```
===== 11
### The human and pig data

Human: the 18 samples of the paper are those of `CadaverVNMorphology_OutputMetrics.mat` in
SPARC:65's code folder (written 2020-09-05), each measured here from its traces
(PeriInnerMask, PeriExtMask, NerveMask), and checked against that file. Pig MT: the 18
samples of `PigVNMorphology_OutputMetrics.mat` in SPARC:64's code folder (nerve diameter,
every fascicle diameter, fascicle count). Pig IF: `PigIFMorphology.mat` in SPARC:89's code
folder (per sample, non-peanut fascicle diameters and perineurium thicknesses, and the
tissue proportions), whose sample levels are taken from its per-level lists
(`pigIF_thkperi_UniqueAges`), and SPARC:89's traces for the trace counts.
===== 12
hum_code = v.mat("65", "files/code/CadaverVNMorphology_OutputMetrics.mat")
hsub = pd.DataFrame(dict(label=hum_code["sub_sam"], level=hum_code["level"], sex=hum_code["sex"]))
hsub["sub"] = hsub["label"].str[1:].str.split("-").str[0].astype(int)
hsub["sam"] = hsub["label"].str.split("-").str[1].astype(int)
hsub["level"] = hsub["level"].map({"C": "cervical", "A": "subdiaphragmatic"})
hsubj = v.excel("65", "files/subjects.xlsx")
hsamp = v.excel("65", "files/samples.xlsx")
age_h = {int(s[4:]): (99 if (">=90" in a or "90+" in a) else int(str(a).split()[0])) for s, a in zip(hsubj["subject_id"], hsubj["age"])}
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "3.57\|invert" entries/pelot-2020/vagus.py attempts/pelot-2020-01.yaml entries/pelot-2020/README.md; grep -n "exactly, and the paper\|lie within each image\|2.1e-15\|1e-15" attempts/pelot-2020-01.yaml entries/pelot-2020/README.md
```

```
entries/pelot-2020/vagus.py:331:    inverted = bool(nerve_bw[0].all() and nerve_bw[-1].all() and nerve_bw[:, 0].all() and nerve_bw[:, -1].all())
entries/pelot-2020/vagus.py:332:    if inverted:
entries/pelot-2020/vagus.py:344:    r["nerve_mask_inverted"] = inverted
attempts/pelot-2020-01.yaml:128:  notes: Tukey rat against human p = 2.1e-15 and rat against pig p below 1e-15 (Satterthwaite 4.3e-14
attempts/pelot-2020-01.yaml:699:    response: Tukey p now with Kenward-Roger degrees of freedom (2.1e-15 and below 1e-15). Outcome unchanged.
```

**Agent calls Bash**

```bash
cd  sed -n 319,348p entries/pelot-2020/vagus.py; grep -n "C54-3\|NerveMask" attempts/pelot-2020-01.yaml | head
```

```
def human_sample(sub, sam):
    """A human sample of SPARC:65: separate masks of the inner (PeriInnerMask) and outer
    (PeriExtMask) perineurium and of the nerve (NerveMask). In the code the nerve is the
    first boundary of NerveMask; for C47-2, C54-3, C55-3 and C63-1 NerveMask is the
    inner nerve trace the Figure 2 legend says was quantified (the all-tissue trace is
    in a separate NerveMask_AllTissue file)."""
    pre = _prefix("65", sub, sam)
    inner_bw = tif("65", pre + "PeriInnerMask.tif")
    outer_bw = tif("65", pre + "PeriExtMask.tif")
    inner, _ = bwboundaries(inner_bw)
    outer, _ = bwboundaries(outer_bw)
    nerve_bw = tif("65", pre + "NerveMask.tif")
    inverted = bool(nerve_bw[0].all() and nerve_bw[-1].all() and nerve_bw[:, 0].all() and nerve_bw[:, -1].all())
    if inverted:
        # C54-3: the published NerveMask is the complement of a nerve mask (white outside
        # the nerve, filling the frame), so its first boundary is the image frame. The nerve
        # is taken as the largest component of its complement that does not touch the edge.
        lab, n = _label_colmajor(~nerve_bw, 8)
        edge = set(np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
        sizes = {k: (lab == k).sum() for k in range(1, n + 1) if k not in edge}
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; cat > $TMPDIR/ed2.py <<'EOF'
import json
p='reproduce_pelot_2020.ipynb'
nb=json.load(open(p))
C=nb['cells']
def find(prefix):
    m=[i for i,c in enumerate(C) if ''.join(c['source']).startswith(prefix)]
    assert len(m)==1,(prefix,m); return m[0]
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))
def setmd(prefix,new): setsrc(find(prefix),new)

rep(0,'''**Mixed models.** The paper fits them in JMP Pro 14.3.0 without giving its settings. They are
fitted here by REML with unbounded variance components, JMP's default, and tested with
Kenward-Roger F tests, the tests JMP reports for REML fits; with them the nerve diameter F
values are 587.3, 11.03 and 2.450 against the paper's 577.1, 11.01 and 2.445.
Satterthwaite, residual and subject-based degrees of freedom and a bounded fit are variants.''',
'''**Mixed models.** The paper fits them in JMP Pro 14.3.0 without giving its settings. They are
fitted here by REML with unbounded variance components, JMP's default, and tested with
Kenward-Roger F tests computed on the observed REML information (the Hessian of the REML
log-likelihood). This choice is an assumption, made because it gives the paper's F and p for
all nine effects the paper reports (to within 0.4% for F, and p to the digits printed, with
the rat fascicle values the paper's code takes; see "Which test the paper's F and p come
from"). Kenward-Roger on the expected information, Satterthwaite, residual and subject-based
degrees of freedom and a bounded fit are variants.''')

setmd('### The mixed model tests','''### The mixed model tests

The mixed models are fitted by REML with unbounded variance components (`v.reml_unbounded`),
JMP's default, and each effect is tested with the Kenward-Roger F test (`v.kr_setup`,
`v.kr_test`) computed on the observed REML information (`F_kr_obs`, `ddf_kr_obs`,
`p_kr_obs`); Tukey's HSD uses the adjusted covariance and degrees of freedom of each
difference from the same test. The choice is an assumption, made because it gives the
paper's F and p (see "Which test the paper's F and p come from", after
fascicle-diameter-anova). Kenward-Roger on the expected information, as Kenward and Roger
(1997) define it (`F_kr`, `ddf_kr`, `p_kr`), and Wald F tests with Satterthwaite, residual and
subject-based degrees of freedom are shown as variants. The check below runs the
Kenward-Roger code on a balanced split-plot design, where it must give the exact F tests.
''')
i=find('## nerve-diameter-anova')
rep(i,'''The Methods fit the models in JMP Pro 14.3.0, whose REML default allows negative variance
components ("Unbounded Variance Components"), and test effects with Kenward-Roger F tests.
The main fit here is REML with unbounded variance components (`vagus.reml_unbounded`),
tested by Kenward-Roger F (`F_kr`, `ddf_kr`, `p_kr`); Tukey tests use the Kenward-Roger
covariance and degrees of freedom of each difference. The Wald F with Satterthwaite degrees
of freedom (`p_satt`), with the residual degrees of freedom and with subjects minus fixed
parameters are variants, and so is the statsmodels REML fit, whose subject variance cannot
go below zero.''','''The Methods fit the models in JMP Pro 14.3.0, whose REML default allows negative variance
components ("Unbounded Variance Components"), and do not give its tests. The main fit here
is REML with unbounded variance components (`vagus.reml_unbounded`), tested by Kenward-Roger
F on the observed information (`F_kr_obs`, `ddf_kr_obs`, `p_kr_obs`); Tukey tests use the
covariance and degrees of freedom of each difference from the same test. Kenward-Roger on the
expected information (`F_kr`, `ddf_kr`, `p_kr`), the Wald F with Satterthwaite degrees of
freedom (`p_satt`), with the residual degrees of freedom and with subjects minus fixed
parameters are variants, and so is the statsmodels REML fit, whose subject variance cannot
go below zero.''')

setmd('**Result: reproduced (resting on an assumption).** With unbounded variance components','''**Result: reproduced (resting on an assumption).** With unbounded variance components (the
subject variance is estimated at -0.052, against a residual 0.127), the Kenward-Roger tests on
the observed information give species F = 577.0 (p < 0.0001), level F = 11.01 (p = 0.0030) and
interaction F = 2.446 (p = 0.1085), against the paper's 577.1, 11.01 (p = 0.0030) and 2.445
(p = 0.1085): species and level are significant and the interaction is not. Kenward-Roger on
the expected information gives level p = 0.0023 and interaction p = 0.103, Satterthwaite
0.0029 and 0.108. With the subject variance held at zero or above (statsmodels), the
interaction is significant (F = 3.71, p = 0.024), which would make the claim only partially
reproduced; the outcome rests on JMP's default of unbounded variance components, which
reproduces the paper's F values.
''')
setmd('**Result: reproduced.** Human 1.922 +/- 0.460','''**Result: reproduced.** Human 1.922 +/- 0.460 and pig 2.195 +/- 0.195 mm cervically,
1.677 +/- 0.316 and 1.638 +/- 0.161 mm subdiaphragmatically, each within the paper's mean and
SD. Tukey's test of the species means gives human against pig p = 0.179 (paper 0.1830);
with Kenward-Roger on the expected information 0.159, with Satterthwaite degrees of freedom
0.157, with subject-based ones 0.143; per level 0.144 and 0.989; with the bounded fit 0.343.
The difference of the human and pig means is 0.32 pooled SDs.
''')
setmd('**Result: reproduced.** Rat against human and rat against pig','''**Result: reproduced.** Rat against human and rat against pig both have Tukey p < 0.0001
(7.9e-14 and 3.1e-12; Kenward-Roger on the expected information 2.1e-15 and a value printed
as 0, Satterthwaite 4.3e-14 and 2.6e-12; values this small are at the precision of the
studentized range integral), with rat smaller, and the ratios of the rat mean to the human
and pig means are 0.134 and 0.117 cervically and 0.081 and 0.082 subdiaphragmatically, all
within 0.05 to 0.2. Per level, all four contrasts have p < 0.0001.
''')
setmd('**Result: reproduced (resting on an assumption).** The level effect has Kenward-Roger','''**Result: reproduced (resting on an assumption).** The level effect has Kenward-Roger
p = 0.0030 (on the expected information 0.0023, Satterthwaite 0.0029), and the cervical least
squares mean (1.425 mm) exceeds the subdiaphragmatic (1.131 mm). The relative difference of
means is 0.127 in humans, 0.254 in pigs and 0.475 in rats, so larger for pigs and rats than
for humans, the claims file's reading of "clearest". The rat part alone holds (0.258 against
0.135 mm).
''')
setmd('**Result: reproduced.** Pig 46.89 +/- 10.3','''**Result: reproduced.** Pig 46.89 +/- 10.3 and 38.22 +/- 7.08 fascicles, human 6.667 +/- 4.5
and 4.889 +/- 3.95, each within the paper's mean and SD. Kenward-Roger tests give species
F = 213.8 (p < 0.0001), level F = 5.486 (p = 0.0300) and interaction F = 2.471 (p = 0.1322),
against 213.8, 5.486 (p = 0.0300) and 2.481 (p = 0.1322); more fascicles cervically in both
species. Kenward-Roger on the expected information gives level p = 0.033 and interaction
p = 0.137, Satterthwaite 0.026 and 0.123. Pigs have 7.0 and 7.8 times the human mean.
''')
setmd('**Result: reproduced.** On log10 fascicle diameter','''**Result: reproduced.** On log10 fascicle diameter, the Kenward-Roger tests give species
F = 9.59 (p = 0.0011), level F = 46.5 (p < 0.0001) and interaction F = 4.93 (p = 0.015), all
below 0.05 (paper 8.989, p = 0.0015; 51.88; 5.273, p = 0.0121). With the rat fascicles as the
paper's code takes them, species F = 8.989 (p = 0.0015), level F = 51.88 and interaction
F = 5.273 (p = 0.0121), the paper's values. Kenward-Roger on the expected information, the
Satterthwaite and the bounded variants also give all three p below 0.05.
''')
setmd('**Result: reproduced.** Over fascicles, human 0.3548','''**Result: reproduced.** Over fascicles, human 0.3548 +/- 0.226 mm (60 fascicles) and pig
0.1545 +/- 0.0579 mm (422), within the paper's values; human against pig Tukey p = 0.00030
with human larger (paper 0.0002), rat against human p = 0.722 (0.7270) and rat against pig
p = 0.140 (0.1707). With Kenward-Roger on the expected information the three p are 0.00007,
0.719 and 0.133, with Satterthwaite degrees of freedom 0.00024, 0.716 and 0.137, with
subject-based ones 0.00009, 0.716 and 0.155, and with the code's rat values 0.00039, 0.727
and 0.149. The means of sample means (0.419 and 0.156 mm) are also within the SDs.
''')
setmd('**Result: reproduced.** Human 0.1635 +/- 0.146','''**Result: reproduced.** Human 0.1635 +/- 0.146 mm and pig 0.1101 +/- 0.0438 mm, within the
paper's values; no subdiaphragmatic pair differs (human against pig p = 0.300, human against
rat 0.996, pig against rat 0.884; paper 0.3049, 0.8960, 0.9947). The log10 differences are
0.146, 0.049 and -0.097, the largest human against pig, as the paper's "trended larger".
With the code's rat values the three pairs give 0.306, 0.899 and 0.995, the paper's values.
''')
setmd('**Result: reproduced (resting on an assumption).** Cervical fascicles are larger','''**Result: reproduced (the verified outcome, resting on an assumption); proposed: partially
reproduced.** Cervical fascicles are larger in all three species. With the test adopted
after round 2, Kenward-Roger on the observed information, which gives the paper's F and p
for the nine effects it reports, human p = 0.00002, pig p = 0.055 and rat p = 0.045 (paper
< 0.0001, 0.0009, 0.0234): two of three species have p < 0.05, so partially reproduced. With
the code's rat values, which give the paper's F values for this model, human 0.00003, pig
0.060 and rat 0.0093, again two of three. The outcome recorded and verified in rounds 1 and
2, reproduced, rested on Kenward-Roger on the expected information (pig p = 0.012, rat 0.044;
code's rat values pig 0.013, rat 0.0089), which the paper's degrees of freedom do not support
(see "Which test the paper's F and p come from"). Round 2 may not change an outcome, so the
change to partially reproduced is proposed for a third round. Of the ten combinations of test
and rat values printed, six give three species and four give two: Kenward-Roger on the
observed information with either rat rule (pig 0.055, 0.060), Satterthwaite with the code's
rat values (pig 0.053), and subjects minus parameters with the largest fascicle (rat 0.068).
The pig contrast has 3.74 degrees of freedom on the observed information and 7.55 on the
expected information, the difference lying mostly in the sample variance term (138257
against 243007). No variant gives the paper's pig p of 0.0009: with this contrast's t (4.77),
that p needs 24.6 degrees of freedom. The rat-only mixed model gives p = 1.7e-07 (largest
fascicle) and 0.00033 (code's values), and a paired t test on the 8 rats with both levels
p = 8.0e-07.
''')
# summary
i=find('## Summary')
rep(i,'| nerve-diameter-anova | reproduced, resting on an assumption (unbounded variance components, Kenward-Roger) |','| nerve-diameter-anova | reproduced, resting on an assumption (unbounded variance components) |')
rep(i,'| fascicles-larger-cervical | reproduced, resting on an assumption (Kenward-Roger degrees of freedom) |','| fascicles-larger-cervical | reproduced, resting on an assumption (the test); partially reproduced proposed (pig p = 0.055 under the test that gives the paper\'s F and p) |')
rep(i,'''unbounded variance components, JMP's default, and tested with Kenward-Roger F tests, written
here and checked on a balanced design; the F values are within 2.1% of the paper's for nerve
diameter and fascicle number.''','''unbounded variance components, JMP's default, and tested with Kenward-Roger F tests on the
observed REML information, written here and checked on a balanced design; this test gives
the paper's F and p for all nine effects it reports (F within 0.4%, with the code's rat
values for fascicle diameter), where Kenward-Roger on the expected information gives F up to
5.1% off and degrees of freedom up to twice the paper's.''')
rep(i,'''measuring them with the paper's method gives the numbers of the code folder's output file
exactly, and the paper's.''','''measuring them with the paper's method gives the values of the code folder's output file
exactly, and the paper's to rounding (rat nerve diameter 0.2577 and 0.1352 mm against 0.260
and 0.135); the rat subdiaphragmatic fascicle diameter is the paper's (0.121 mm) only under
the code's first-trace rule (0.1211 mm, against 0.1291 mm for the largest fascicle).''')
rep(i,'''In
SPARC:65 the NerveMask of C54-3 is inverted, so the published code would measure the image
frame (3.57 mm) in place of the nerve (1.62 mm).''','''In
SPARC:65 the NerveMask of C54-3 is inverted (white outside the nerve, filling the frame); it
is measured here from its complement, which gives the code folder's 1615 um.''')
rep(i,'''The derivative folder holds the 18 rat
micrographs (JPEG 2000) at the resolution of the traces, and the traces drawn over them lie within each image; the
other bundles of the carotid sheath in the cervical micrographs are not traced.''','''The derivative folder holds the rat
micrographs (JPEG 2000); the nine cervical ones were opened and drawn with their traces,
which lie within each image, and the other bundles of the carotid sheath in them are not
traced.''')
# markdown after the new F/p code cell
j=find('from scipy import optimize\npaper_fp')
md='''The Kenward-Roger test on the observed information gives the paper's F to within 0.4% and
its p to the digits printed for all nine effects, with the rat fascicle values the paper's
code takes for fascicle diameter, and its denominator degrees of freedom are within 1 of
those the paper's (F, p) pairs imply (23.0 and 23.5, 19.4 and 18.5, 21.1 and 25.6 against
23.3 and 23.4, 19.3 and 19.3, 21.2 and 25.4). Kenward-Roger on the expected information gives
F up to 5.1% off and degrees of freedom up to twice the paper's, the Wald F up to 9.8% off.
The observed-information test is therefore taken as the main test for every mixed model
claim, still as an assumption (JMP's settings are not given). With the largest fascicle in
place of the code's rat values, the fascicle diameter F values are 9.59, 46.5 and 4.93
against the paper's 8.989, 51.88 and 5.273, which shows again that the paper's statistics
used the code's rat values.
'''
C.insert(j+1,{'cell_type':'markdown','metadata':{},'source':md.splitlines(keepends=True)})
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
python $TMPDIR/ed2.py && git diff --stat
```

```
entries/pelot-2020/reproduce_pelot_2020.ipynb | 252 +++++++++++++++++---------
 entries/pelot-2020/vagus.py                   |  30 ++-
 2 files changed, 192 insertions(+), 90 deletions(-)
```

**Agent calls Bash**

```bash
cd  sed -i 's/interaction F = 2.446 (p = 0.1085), against/interaction F = 2.4455 (p = 0.1085), against/' entries/pelot-2020/reproduce_pelot_2020.ipynb; grep -c "2.4455 (p = 0.1085)" entries/pelot-2020/reproduce_pelot_2020.ipynb; cat questions/pelot-2020.yaml; cat questions/README.md | head -40
```

```
1
questions:
- claim: no-age-trend
  question: The criterion was written without Supplement 6 and says the claim rests on an assumption
    until Supplement 6 fixes the method. Supplement 6 is one figure (Figure 19, "Nerve morphology
    metrics versus age") with no test. Reading (a) applies an uncorrected Pearson test at p < 0.05
    to each of 26 per-species, per-level metrics. Does the paper's "did not show trends with age",
    judged on plots of 26 metrics, support a test that counts a single uncorrected p < 0.05 as a
    trend, or should the criterion correct for the number of tests (or judge the plots as the paper
    does)?
  passage: 'Discussion, paragraph 5, "Our morphology metrics did not show trends with age for any
    species ( Supplement 6 )"; Supplement 6 (Data_Sheet_1.pdf, page 16), "Figure 19. Nerve morphology
    metrics versus age. Note that all human subjects over 89 years old were plotted as 99 years old."'
  why: Under reading (a) as written, 3 of the 26 Pearson tests have p < 0.05 (all in pigs, 1.3 expected
    by chance) and the claim is not reproduced. With a Holm correction over the 26 tests, or within
    each species, no test is below 0.05 (smallest corrected p 0.499 and 0.154) and the claim would
    be reproduced.
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/pelot-2020.yaml'))
for cl in c['claims']:
    if cl['id'] in ['rat-carotid-sheath-bundles','rat-fascicle-diameter']:
        print(yaml.safe_dump(cl,sort_keys=False,width=100))
EOF
grep -n "largest fascicle\|largest rat\|fasc_ind" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat >> questions/pelot-2020.yaml <<'EOF'
- claim: fascicle-diameter-anova
  question: The criteria of fascicle-diameter-anova, rat-fascicle-diameter and the claims that use their
    model (cervical-fascicle-diameter-species, subdiaphragmatic-fascicle-diameter-comparable,
    fascicles-larger-cervical) take the rat fascicle as the largest fascicle of each sample, as the
    Methods say. The paper's own numbers come from its code's rule, the first inner trace in the code's
    order, which differs from the largest fascicle in R22-1 and R23-1. Should the criteria take the rat
    fascicle values the paper's statistics used (the code's rule), or keep the Methods' largest fascicle?
  passage: 'Methods, Imaging and Image Analysis, paragraph 2, "for all statistics, we only used the largest
    fascicle in each rat sample"; Results, paragraph 5, rat subdiaphragmatic fascicle diameter "0.121 ±
    0.032 mm"; DataPlotting_v4.m in SPARC:60 (fasc_ind == 1).'
  why: With the largest fascicle the rat subdiaphragmatic mean is 0.1291 mm, with the code's rule 0.1211
    mm, the paper's value. With the code's rule the fascicle diameter model gives the paper's F values
    (8.989, 51.88, 5.273), with the largest fascicle 9.59, 46.5 and 4.93. In this attempt no outcome
    differs between the two rules (fascicles-larger-cervical has two of three species under the test that
    gives the paper's F and p with either rule), but the values reported against the paper do, and a
    later test could.
- claim: rat-carotid-sheath-bundles
  question: The criterion says the claim is "Testable only if the dataset holds the cervical micrographs
    or traces of the other bundles", and also "Not testable when only the vagus is traced". SPARC:60 holds
    the nine cervical micrographs, which show the other bundles of the sheath, and traces only the vagus.
    Which condition decides? If the micrographs suffice, how are the bundles to be identified and counted,
    as the paper gives no rule and the dataset no label?
  passage: 'Discussion, paragraph 6, "we observed up to six fascicles within the carotid sheath (Supplementary
    Figure 16)"; Supplementary Figure 16 legend, "the cervical micrographs also show the common carotid
    artery, as well as other nerves in the carotid sheath".'
  why: Under the second condition the claim is blocked, as recorded. Under the first it would be tested by
    counting bundles by eye in the nine micrographs, which could give reproduced or not reproduced.
EOF
python -c "import yaml;print(len(yaml.safe_load(open('questions/pelot-2020.yaml'))['questions']))"
```

```
3
```

**Agent calls Bash**

```bash
cd  cat entries/pelot-2020/README.md; grep -n "Kenward\|JMP" attempts/pelot-2020-01.yaml | cut -c1-200
```

```
# Pelot et al. (2020), vagus nerve morphology of human, pig and rat, on SPARC dataset 60

Tests the findings of [Pelot et al. (2020)](https://doi.org/10.3389/fnins.2020.601479) on
[SPARC:60](https://sparc.science/datasets/60) version 5 (doi:10.26275/lg3c-1kjf), which holds
the segmented traces of nine left cervical and nine anterior subdiaphragmatic rat vagus nerve
samples and the paper's MATLAB code. The rat measures are taken from the traces with the
paper's method, and match the code's own output file exactly. The comparisons with human and
pig use the paper's sister datasets, SPARC:65 version 6 (human traces), SPARC:64 version 4
(pig Masson's trichrome output file) and SPARC:89 version 1 (pig anti-fibronectin output file
and traces), and the literature values of the paper's Supplement 4.

| Outcome | Claims |
|---|---|
| Reproduced (29) | Rat sample set, nerve and fascicle diameters, multifascicular samples and their tissue proportions, the three mixed model ANOVAs and their Tukey comparisons, tissue proportions, level ratios, variability, the perineurium fits, their order and trends, the Sunderland refit, pig IF against MT. Six rest on an assumption, among them the nerve diameter ANOVA (JMP's unbounded variance components) and the cervical against subdiaphragmatic fascicle comparison (Kenward-Roger degrees of freedom) |
| Partially reproduced (3) | The two literature comparisons; the counts of peanut fascicles (pig cervical 24, not 25) |
| Not reproduced (2) | No level difference in the perineurium relationship; no trend with age |
| Blocked (1) | Bundles of the rat carotid sheath: the micrographs are in the dataset, but only the vagus is traced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 55,284p attempts/pelot-2020-01.yaml
```

```
only a subdiaphragmatic one, as the Methods describe. No right cervical or posterior samples are deposited
    (the code's lists for them are empty). The 18 PeriMask arrays are all distinct. The readme gives ages
    65 to 268 days, subjects.xlsx 75 to 268.
- claim: nerve-diameter-anova
  outcome: reproduced
  notebook: reproduce_pelot_2020.ipynb
  output: claim:nerve-diameter-anova
  notes: Unbounded REML (subject variance -0.052, residual 0.127) with Kenward-Roger tests gives species
    F = 587.3 (p < 0.0001), level F = 11.03 (p = 0.0023) and interaction F = 2.450 (p = 0.103), against
    the paper's 577.1, 11.01 (p = 0.0030) and 2.445 (p = 0.1085). The Wald F values are 599.6, 11.05
    and 2.455; with Satterthwaite, residual or subject-based degrees of freedom the interaction p is 0.108,
    0.097 or 0.104. With the subject variance bounded at zero (statsmodels REML) the interaction is significant
    (F = 3.71, p = 0.024), which would make the claim partially reproduced; an ordinary ANOVA gives p
    = 0.035. The human data are measured here from the traces of SPARC:65 (version
    6) with the paper's method, and match its code's output file exactly; the pig MT values come from
    the per-fascicle output file of SPARC:64 (version 4, files/code/PigVNMorphology_OutputMetrics.mat),
    not from its traces.
  deviations:
  - The Methods fit the mixed models in JMP Pro 14.3.0 and do not give its settings. The fit here is REML
    with unbounded variance components, JMP's default, which statsmodels does not offer, and effects and
[... 210 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ed3.py <<'EOF'
p='attempts/pelot-2020-01.yaml'; s=open(p).read()
def rep(a,b,count=1):
    global s
    n=s.count(a); assert n==count,(n,a[:80]); s=s.replace(a,b)
oldDev='''  - The Methods fit the mixed models in JMP Pro 14.3.0 and do not give its settings. The fit here is REML
    with unbounded variance components, JMP's default, which statsmodels does not offer, and effects and
    Tukey contrasts are tested with Kenward-Roger F tests and degrees of freedom, the tests JMP reports
    for REML fits, both written in vagus.py and checked on a balanced split-plot design. Satterthwaite,
    residual and subject-based degrees of freedom and a bounded fit are variants. This is an assumption
    about the paper's settings; with it the nerve diameter F values are 587.3, 11.03 and 2.450 against
    the paper's 577.1, 11.01 and 2.445.
'''
newDev='''  - The Methods fit the mixed models in JMP Pro 14.3.0 and do not give its settings. The fit here is REML
    with unbounded variance components, JMP's default, which statsmodels does not offer, and effects and
    Tukey contrasts are tested with Kenward-Roger F tests and degrees of freedom computed on the observed
    REML information (the Hessian of the REML log-likelihood), written in vagus.py and checked on a balanced
    split-plot design. This is an assumption about the paper's settings, adopted after round 2 because
    it gives the paper's F and p for all nine effects the paper reports (F within 0.4%, p to the digits
    printed, degrees of freedom within 1 of those the paper's F and p imply; nerve diameter 577.0, 11.01
    and 2.4455 against 577.1, 11.01 and 2.445). Kenward-Roger on the expected information (the main test
    in round 2), Satterthwaite, residual and subject-based degrees of freedom and a bounded fit are variants.
'''
rep(oldDev,newDev,count=9)
rep('''  notes: Unbounded REML (subject variance -0.052, residual 0.127) with Kenward-Roger tests gives species
    F = 587.3 (p < 0.0001), level F = 11.03 (p = 0.0023) and interaction F = 2.450 (p = 0.103), against
    the paper's 577.1, 11.01 (p = 0.0030) and 2.445 (p = 0.1085). The Wald F values are 599.6, 11.05
    and 2.455; with Satterthwaite, residual or subject-based degrees of freedom the interaction p is 0.108,
    0.097 or 0.104.''','''  notes: Unbounded REML (subject variance -0.052, residual 0.127) with Kenward-Roger tests on the observed
    information gives species F = 577.0 (p < 0.0001), level F = 11.01 (p = 0.0030) and interaction F
    = 2.4455 (p = 0.1085), against the paper's 577.1, 11.01 (p = 0.0030) and 2.445 (p = 0.1085). On the
    expected information F = 587.3, 11.03 and 2.450 (interaction p = 0.103). The Wald F values are 599.6,
    11.05 and 2.455; with Satterthwaite, residual or subject-based degrees of freedom the interaction p
    is 0.108, 0.097 or 0.104.''')
rep('''Tukey on the species means, human against pig p = 0.159 (paper 0.1830); with
    Satterthwaite degrees of freedom 0.157, with subject-based ones 0.143; per level 0.138 and 0.988;
    bounded fit 0.343.''','''Tukey on the species means, human against pig p = 0.179 (paper 0.1830); with
    Kenward-Roger on the expected information 0.159, with Satterthwaite degrees of freedom 0.157, with
    subject-based ones 0.143; per level 0.144 and 0.989; bounded fit 0.343.''')
rep('''  - Tukey p from the studentized range with the Kenward-Roger covariance and degrees of freedom of each
    difference.''','''  - Tukey p from the studentized range with the Kenward-Roger covariance and degrees of freedom of each
    difference, on the observed information.''')
rep('''  notes: Tukey rat against human p = 2.1e-15 and rat against pig p below 1e-15 (Satterthwaite 4.3e-14
    and 2.6e-12); per level all four contrasts p < 1e-12.''','''  notes: Tukey rat against human p = 7.9e-14 and rat against pig p = 3.1e-12 (Kenward-Roger on the expected
    information 2.1e-15 and a value printed as 0, Satterthwaite 4.3e-14 and 2.6e-12; values this small
    are at the precision of the studentized range integral); per level all four contrasts p < 1e-11.''')
rep('''  notes: Level effect Kenward-Roger p = 0.0023 (Satterthwaite 0.0029)''','''  notes: Level effect Kenward-Roger p = 0.0030 (on the expected information 0.0023, Satterthwaite 0.0029)''')
rep('''Kenward-Roger
    tests give species F = 212.9 (p < 0.0001), level F = 5.39 (p = 0.033), interaction F = 2.43 (p = 0.137),
    against 213.8, 5.486 (p = 0.0300) and 2.481 (p = 0.1322). The Satterthwaite variant gives level p
    = 0.026 and interaction p = 0.123,''','''Kenward-Roger
    tests give species F = 213.8 (p < 0.0001), level F = 5.486 (p = 0.0300), interaction F = 2.471 (p =
    0.1322), against 213.8, 5.486 (p = 0.0300) and 2.481 (p = 0.1322). On the expected information level
    p = 0.033 and interaction p = 0.137, with Satterthwaite 0.026 and 0.123,''')
rep('''Kenward-Roger
    tests give species F = 9.66 (p = 0.00044), level F = 47.3 (p < 0.0001), interaction F = 5.20 (p = 0.0088);
    paper 8.989 (p = 0.0015), 51.88, 5.273 (p = 0.0121). With the code's rat values F = 9.05 (p = 0.00067),
    52.8 and 5.54 (p = 0.0067), closer to the paper's F values. The Satterthwaite and bounded variants
    agree.''','''Kenward-Roger
    tests give species F = 9.59 (p = 0.0011), level F = 46.5 (p < 0.0001), interaction F = 4.93 (p = 0.015);
    paper 8.989 (p = 0.0015), 51.88, 5.273 (p = 0.0121). With the code's rat values F = 8.989 (p = 0.0015),
    51.88 and 5.273 (p = 0.0121), the paper's values. Kenward-Roger on the expected information, Satterthwaite
    and bounded variants agree.''')
rep('''Tukey on the
    cells, human against pig p = 0.00007 with human larger (paper 0.0002), rat against human 0.719 (0.7270),
    rat against pig 0.133 (0.1707); with Satterthwaite degrees of freedom 0.00024, 0.716 and 0.137; with
    subject-based ones 0.00009, 0.716 and 0.155; with the code's rat values 0.00011, 0.724 and 0.143.''','''Tukey on the
    cells, human against pig p = 0.00030 with human larger (paper 0.0002), rat against human 0.722 (0.7270),
    rat against pig 0.140 (0.1707); on the expected information 0.00007, 0.719 and 0.133; with Satterthwaite
    degrees of freedom 0.00024, 0.716 and 0.137; with subject-based ones 0.00009, 0.716 and 0.155; with
    the code's rat values 0.00039, 0.727 and 0.149.''')
rep('''human against pig p =
    0.280, human against rat 0.995, pig against rat 0.884 (paper 0.3049, 0.8960, 0.9947); with the code''s
    rat values 0.286, 0.898 and 0.995; with Satterthwaite degrees of freedom 0.283, 0.995 and 0.883.''','''human against pig p =
    0.300, human against rat 0.996, pig against rat 0.884 (paper 0.3049, 0.8960, 0.9947); with the code''s
    rat values 0.306, 0.899 and 0.995; on the expected information 0.280, 0.995 and 0.884; with Satterthwaite
    degrees of freedom 0.283, 0.995 and 0.883.''')
# fascicles-larger-cervical
a=s.index('- claim: fascicles-larger-cervical\n  outcome: reproduced')
b=s.index('- claim: rat-diameter-like-fascicle', a)
new='''- claim: fascicles-larger-cervical
  outcome: reproduced
  notebook: reproduce_pelot_2020.ipynb
  output: claim:fascicles-larger-cervical
  notes: Cervical larger in each species. With Kenward-Roger on the observed information, the test that
    gives the paper's F and p, Tukey p human 0.00002, pig 0.055, rat 0.045 (paper < 0.0001, 0.0009, 0.0234),
    two of three species; with the code's rat values human 0.00003, pig 0.060, rat 0.0093, again two.
    The verified outcome rested on Kenward-Roger on the expected information, human 0.000001, pig 0.012,
    rat 0.044 (code's rat values pig 0.013, rat 0.0089). Of the ten combinations of test and rat values
    printed, six give three species and four give two (the observed-information test with either rat rule,
    Satterthwaite with the code's rat values, pig p = 0.053, and subjects minus parameters with the largest
    fascicle, rat p = 0.068). The pig contrast has 3.74 degrees of freedom on the observed information
    and 7.55 on the expected, mostly from the sample variance term (138257 against 243007). No variant
    gives the paper's pig p of 0.0009, which with this contrast's t of 4.77 would need 24.6 degrees of
    freedom. Residual degrees of freedom give pig 0.00001 and rat 0.043, the bounded fit pig 0.00001
    and rat 0.043. A rat-only mixed model (unbounded REML, Kenward-Roger) gives p = 1.7e-07 for the largest
    fascicle and 0.00033 for the code's values; a paired t test on the 8 rats with both levels gives p
    = 8.0e-07.
  deviations:
''' + newDev + '''  - The rat largest fascicle is the largest by endoneurial area, as the Methods say (Imaging and Image
    Analysis, paragraph 2). The paper's code (DataPlotting_v4.m) takes the first inner trace in its order,
    which differs in R22-1 and R23-1; the code's values, which Supplement 4's summaries and the fascicle
    diameter F values show the paper used, are run as a variant.
  - The outcome rests on the choice of test. In round 2 Kenward-Roger on the expected information was
    the assumption; the verifier showed the paper's degrees of freedom do not support it, and the test
    on the observed information, which reproduces the paper's F and p, is adopted in its place. Under
    it the outcome would be partially reproduced, proposed below.
  assumed: true
  proposed:
    outcome: partially_reproduced
    reason: Under Kenward-Roger on the observed REML information, the test that gives the paper's F and
      p for all nine effects it reports and degrees of freedom within 1 of those the paper's F and p imply,
      the pig contrast has Tukey p = 0.055 (0.060 with the code's rat values), human and rat below 0.05,
      so two of three species hold, the criterion's partially reproduced. The verified outcome rested on
      Kenward-Roger on the expected information (pig p = 0.012), whose degrees of freedom are up to twice
      the paper's. Shown in the notebook under "Which test the paper's F and p come from" and
      fascicles-larger-cervical.
'''
s=s[:a]+new+s[b:]
open(p,'w').write(s)
EOF
python $TMPDIR/ed3.py && sed -n 625,660p attempts/pelot-2020-01.yaml
```

```
- claim: rat-carotid-sheath-bundles
  outcome: blocked
  blocked_by: other
  notebook: reproduce_pelot_2020.ipynb
  output: claim:rat-carotid-sheath-bundles
  notes: The data are there in part. The derivative folder holds the nine cervical micrographs (JPEG 2000,
    files/derivative/sub-*/sam-*/*MT20x.jp2), which the notebook shows at 1/8 resolution with the traced
    vagus drawn over them; every trace lies within its image, and the legend of Supplementary Figure 16 says the micrographs also show other nerves of the carotid
    sheath. But each cervical PeriMask, and each Neurolucida file (MergeMask.xml), holds only the vagus,
    and the paper does not say how the other bundles were identified or counted. Counting them here would
    be the attempt's own visual judgement, not a measurement from the data, so the claim is not tested.
    A segmentation or labels of the other bundles would make it testable.
findings:
- kind: metadata_error
  statement: files/derivative/RatVNMorphology_OutputMetrics.mat, described in the derivative manifest
    as the rat morphology output metrics, is an older output (written 2020-03-03) that holds 54 samples
    of all three species (human C, pig P and rat R). Its rat values are not those of the primary traces
    or of the paper; cervical nerve diameters are up to 8.5 um larger (R22-3, 245.2 against 236.7 um)
    and the multifascicular samples use the connective tissue boundary. The code folder's file of the
    same name (2020-09-05) matches the traces and the paper.
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 660,690p attempts/pelot-2020-01.yaml
```

```
takes the first inner perineurium trace in its order as the rat fascicle diameter (it sorts only the
    outer diameters). In R22-1 that trace is 39.35 um against a largest fascicle of 105.76 um, and in
    R23-1 142.15 against 147.47 um. The paper's rat subdiaphragmatic fascicle diameter, 0.121 +/- 0.032
    mm, and its rat cervical against subdiaphragmatic p = 0.0234 rest on these values; with the largest
    fascicles they are 0.129 +/- 0.014 mm and p = 0.044 (Kenward-Roger) to 0.068.
- kind: paper_inconsistency
  statement: The Discussion's rat ratios of subdiaphragmatic to cervical means (endoneurial area 0.32,
    nerve diameter 0.68) are reproduced only with all segmented fascicles and the connective tissue boundary
    of the multifascicular samples (0.317 and 0.678), while the Methods say all rat statistics use the
    largest fascicle; with it the ratios are 0.270 and 0.525, and the Results' own means give 0.52.
- kind: methods_unavailable
  statement: Question for the authors. Which JMP settings were used for the mixed models? The nerve diameter
    F values (577.1, 11.01, 2.445) are matched (Kenward-Roger 587.3, 11.03, 2.450) only with unbounded
    variance components (the subject variance estimate is negative, -0.052); with the variance bounded
    at zero the interaction becomes significant (p = 0.024). Was Kenward-Roger used for the degrees of
    freedom? The rat and pig cervical against subdiaphragmatic fascicle comparisons change side of 0.05
    with the degrees of freedom (Kenward-Roger keeps all three below 0.05).
- kind: methods_unavailable
  statement: Question for the authors. What test supports 'the data did not suggest a difference in the
    relationship between perineurium thickness and fascicle diameter for cervical versus subdiaphragmatic
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ed4.py <<'EOF'
p='attempts/pelot-2020-01.yaml'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a[:80]; s=s.replace(a,b)
rep('''mm, and its rat cervical against subdiaphragmatic p = 0.0234 rest on these values; with the largest
    fascicles they are 0.129 +/- 0.014 mm and p = 0.044 (Kenward-Roger) to 0.068.''','''mm, and its fascicle diameter F values (8.989, 51.88, 5.273, reproduced here with the code's values)
    rest on these values; with the largest fascicles they are 0.129 +/- 0.014 mm and F = 9.59, 46.5
    and 4.93.''')
rep('''  statement: Question for the authors. Which JMP settings were used for the mixed models? The nerve diameter
    F values (577.1, 11.01, 2.445) are matched (Kenward-Roger 587.3, 11.03, 2.450) only with unbounded
    variance components (the subject variance estimate is negative, -0.052); with the variance bounded
    at zero the interaction becomes significant (p = 0.024). Was Kenward-Roger used for the degrees of
    freedom? The rat and pig cervical against subdiaphragmatic fascicle comparisons change side of 0.05
    with the degrees of freedom (Kenward-Roger keeps all three below 0.05).''','''  statement: Question for the authors. Which JMP settings were used for the mixed models? Unbounded variance
    components (the nerve diameter subject variance estimate is negative, -0.052) with Kenward-Roger tests
    computed on the observed REML information give the paper's F and p for all nine effects reported
    (nerve diameter 577.0, 11.01, 2.4455 against 577.1, 11.01, 2.445); with the variance bounded at zero
    the nerve diameter interaction becomes significant (p = 0.024). Is that what JMP did, and how was the
    pig cervical against subdiaphragmatic Tukey p of 0.0009 obtained? Under the same test it is 0.055
    (3.74 degrees of freedom), and it would need about 25 degrees of freedom to be 0.0009.''')
rep('''    be the attempt's own visual judgement, not a measurement from the data, so the claim is not tested.
    A segmentation or labels of the other bundles would make it testable.''','''    be the attempt's own visual judgement, not a measurement from the data, so the claim is not tested.
    A segmentation or labels of the other bundles would make it testable. The criterion's two conditions
    ("Testable only if the dataset holds the cervical micrographs", "Not testable when only the vagus
    is traced") disagree for this dataset; this is asked of a reader in questions/pelot-2020.yaml.''')
rep('''    the paper's numbers. Geometric means 0.2475 and 0.1284 mm.''','''    the paper's numbers. Geometric means 0.2475 and 0.1284 mm. Whether the criteria should take the code's
    rat values, which the paper's numbers use, is asked of a reader in questions/pelot-2020.yaml.''')
rep('''51.88 and 5.273 (p = 0.0121), the paper's values. Kenward-Roger on the expected information, Satterthwaite
    and bounded variants agree.''','''51.88 and 5.273 (p = 0.0121), the paper's values. Kenward-Roger on the expected information, Satterthwaite
    and bounded variants agree. Whether the criterion should take the code's rat values is asked of a
    reader in questions/pelot-2020.yaml.''')
open(p,'w').write(s)
EOF
python $TMPDIR/ed4.py && python -c "import yaml;yaml.safe_load(open('attempts/pelot-2020-01.yaml'))" && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  ls schemas 2>/dev/null; grep -rn "verifications" -A40 schemas/attempt*.json 2>/dev/null | grep -n "properties\|required\|\"[a-z_]*\": {" | head -40
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
1:390:    "verifications": {
3:392-      "items": {
6:395-        "required": [
12:401-        "properties": {
13:402-          "date": {
17:406-          "kind": {
24:413-          "by": {
27:416-          "results": {
29:418-            "items": {
32:421-              "required": [
36:425-              "properties": {
37:426-                "claim": {
40:429-                "agrees": {
```

**Agent calls Bash**

```bash
cd  sed -n 385,470p schemas/attempt.schema.json; grep -n '"proposed"' -A30 schemas/attempt.schema.json | head -40
```

```
}
          }
        ]
      }
    },
    "verifications": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "date",
          "kind",
          "by",
          "results"
        ],
        "properties": {
          "date": {
            "type": "string",
            "format": "date"
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z_]*:" attempts/pelot-2020-01.yaml; tail -5 attempts/pelot-2020-01.yaml; python -c "
import yaml;a=yaml.safe_load(open('attempts/pelot-2020-01.yaml'))
print([(o['claim'],o['outcome'],o.get('assumed',False)) for o in a['outcomes']])"
```

```
1:schema_version: 3
2:id: pelot-2020-01
3:datasets:
9:paper: doi:10.3389/fnins.2020.601479
10:date: '2026-11-18'
11:entry: pelot-2020
12:provenance:
23:inputs:
46:outcomes:
641:findings:
693:verifications:
      traced vagus drawn over each, and prints the Supplementary Figure 16 legend. blocked_by is changed
      from data_missing to other, as the micrographs are in the dataset. The claim stays blocked, which
      partly keeps the disagreement; the dataset holds no trace or label of the other bundles (the PeriMasks
      and the Neurolucida MergeMask.xml files hold the vagus only), the paper does not say how the bundles
      were identified or counted, and a count by eye would be the attempt's judgement, not a measurement.
[('rat-sample-set', 'reproduced', False), ('nerve-diameter-anova', 'reproduced', True), ('human-pig-nerve-diameter-similar', 'reproduced', False), ('rat-nerve-diameter', 'reproduced', False), ('rat-ten-times-smaller', 'reproduced', False), ('nerve-cervical-larger', 'reproduced', True), ('fascicle-number-human-pig', 'reproduced', False), ('rat-subdiaphragmatic-multifascicular', 'reproduced', False), ('rat-multifascicular-proportions', 'reproduced', False), ('fascicle-diameter-anova', 'reproduced', False), ('rat-fascicle-diameter', 'reproduced', False), ('cervical-fascicle-diameter-species', 'reproduced', False), ('subdiaphragmatic-fascicle-diameter-comparable', 'reproduced', False), ('fascicles-larger-cervical', 'reproduced', True), ('rat-diameter-like-fascicle', 'reproduced', False), ('human-pig-tissue-proportions', 'reproduced', False), ('rat-level-ratios', 'reproduced', False), ('human-pig-level-ratios', 'reproduced', False), ('human-variability', 'reproduced', True), ('literature-comparison-human-pig', 'partially_reproduced', True), ('rat-literature-comparison', 'partially_reproduced', True), ('perineurium-species-order', 'reproduced', False), ('perineurium-ratio-decreases', 'reproduced', False), ('human-perineurium-fit', 'reproduced', Fals
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ed5.py <<'EOF'
import yaml
p='attempts/pelot-2020-01.yaml'
a=yaml.safe_load(open(p))
out={o['claim']:o['outcome'] for o in a['outcomes']}
MM=("The main test is now Kenward-Roger on the observed REML information, which gives the paper's F and p for all "
    "nine effects it reports (see fascicles-larger-cervical); Kenward-Roger on the expected information is a variant. ")
R={}
def r(c,reason,response="No change."): R[c]=(reason,response)
default="One of the 34 outcomes the verifier agrees with; no point raised on it."
r('nerve-diameter-anova',"The assumption is stated and reasonable: unbounded variance components match the paper's F values.",
  MM+"F = 577.0, 11.01 and 2.4455 (p < 0.0001, 0.0030, 0.1085) against the paper's 577.1, 11.01 and 2.445. Outcome unchanged.")
r('human-pig-nerve-diameter-similar',default,MM+"Human against pig p = 0.179 (paper 0.1830). Outcome unchanged.")
r('rat-nerve-diameter',default+" The Summary's \"gives the numbers of the code folder's output file exactly, and the paper's\" "
  "is not supported: the rat cervical nerve diameter is 0.2577 mm against the paper's 0.260.",
  "The Summary now says the values equal the code's output file exactly and the paper's to rounding (0.2577 and 0.1352 "
  "against 0.260 and 0.135). Outcome unchanged.")
r('rat-ten-times-smaller',"Agrees. Cell 42 and the record's notes say \"2.1e-15 and below 1e-15 (Satterthwaite 4.3e-14)\", "
  "where cell 41 prints 5.22e-15 and 1.22e-15, and Satterthwaite 4.12e-14; this does not affect the conclusion.",
  MM+"The text now gives the printed values, 7.9e-14 and 3.1e-12 (expected information 2.1e-15 and a value printed as 0, "
  "Satterthwaite 4.3e-14 and 2.6e-12), and says values this small are at the precision of the studentized range integral. "
  "Outcome unchanged.")
r('nerve-cervical-larger',"The assumption is stated and reasonable: it uses the claims file's own reading.",
  MM+"Level p = 0.0030. Outcome unchanged.")
r('fascicle-number-human-pig',default,MM+"F = 213.8, 5.486 and 2.471 (p < 0.0001, 0.0300, 0.1322) against 213.8, 5.486 and 2.481. Outcome unchanged.")
r('fascicle-diameter-anova',default+" As in round 1, the fascicle-diameter criteria follow the Methods text (\"largest fascicle\"), "
  "while the paper's numbers come from the code's first-trace rule.",
  MM+"F = 9.59, 46.5 and 4.93 (p = 0.0011, < 0.0001, 0.015); with the code's rat values 8.989, 51.88 and 5.273, the paper's values. "
  "The claims file's reading is added to questions/pelot-2020.yaml as a question for a reader; the claim is not changed. Outcome unchanged.")
r('rat-fascicle-diameter',default+" The Summary's match with the paper holds for the rat subdiaphragmatic fascicle diameter only "
  "under the code's rule (0.1211 against 0.1291, cell 32); the fascicle-diameter criteria follow the Methods text, while the "
  "paper's numbers come from the code's first-trace rule.",
  "The Summary now says so. The question is added to questions/pelot-2020.yaml (claim fascicle-diameter-anova, naming this claim). Outcome unchanged.")
r('cervical-fascicle-diameter-species',default,MM+"Tukey p = 0.00030, 0.722 and 0.140 (code's rat values 0.00039, 0.727, 0.149). Outcome unchanged.")
r('subdiaphragmatic-fascicle-diameter-comparable',default,MM+"Tukey p = 0.300, 0.996 and 0.884 (code's rat values 0.306, 0.899, 0.995). Outcome unchanged.")
r('fascicles-larger-cervical',
  "Agrees only with qualification. The record says Kenward-Roger is \"JMP's test\", which the paper's numbers do not support: "
  "solving the paper's (F, p) pairs for the denominator degrees of freedom gives 23.0, 23.5, 19.4, 18.5, 21.1 and 25.6, at the "
  "notebook's Satterthwaite values (23.3, 23.4, 19.3, 19.3, 20.6, 28.4), not its Kenward-Roger ones (30.7, 30.8, 17.1, 17.1, "
  "35.8, 51.2). Under Satterthwaite with the code's rat values, which round 1 found to be the paper's actual values, the pig p "
  "is 0.0526 and only two of three species hold, which would be partially reproduced. No variant gives the paper's pig p of "
  "0.0009; Kenward-Roger gives 0.012. The assumption is stated, but not shown to be reasonable; the outcome should stay "
  "explicitly fragile.",
  "The notebook now solves the paper's (F, p) pairs for their degrees of freedom and sets them beside each test (new section "
  "\"Which test the paper's F and p come from\"). Kenward-Roger computed on the observed REML information (vagus.py, kr_setup "
  "with the Hessian in place of the expected information) gives the paper's F within 0.4% and its p to the digits printed for "
  "all nine effects, with the code's rat values, and degrees of freedom within 1 of the paper's; Kenward-Roger on the expected "
  "information gives F up to 5.1% off and degrees of freedom up to twice the paper's. The assumption is revised to the "
  "observed-information test for every mixed model claim. Under it this claim has pig p = 0.055 (code's rat values 0.060), "
  "human and rat below 0.05, two of three species. As round 2 may not change an outcome, the outcome stays reproduced and "
  "partially_reproduced is written under proposed, for a third round. The notebook also prints that the paper's pig p of "
  "0.0009 would need 24.6 degrees of freedom for this contrast, and the methods_unavailable finding now asks the authors how it was obtained.")
r('human-variability',"The assumption is stated and reasonable: it uses the claims file's own reading.")
r('literature-comparison-human-pig',"The assumption is stated and reasonable: the outcome is the same under both readings.")
r('rat-literature-comparison',"The assumption is stated and reasonable: the all-rows reading rests on the Results' \"including data "
  "published for both left/right and anterior/posterior VNs\". The outcome flips to reproduced with left-side rows only; this is "
  "stated and assumed, but it remains a reading-dependent outcome.",
  "No change; the dependence on the reading stays stated in the notes and the notebook.")
r('perineurium-no-level-difference',"The assumption is stated and reasonable: it uses the claims file's own reading.")
r('rat-perineurium-near-3-percent',"The assumption is stated and reasonable: it uses the claims file's own reading.")
r('human-pig-perineurium-thicker',"The assumption is stated and reasonable: it uses the claims file's own reading.")
r('no-age-trend',"The assumption is stated and reasonable: it uses the claims file's own reading. The outcome is not reproduced "
  "under the uncorrected test and reproduced under the Holm correction, which depends on the open question about the criterion.",
  "No change; the question about the criterion stays with a reader in questions/pelot-2020.yaml.")
r('rat-carotid-sheath-bundles',"Agrees with the block. Cell 125's image shows other bundles in all nine cervical micrographs, so a "
  "count by eye is possible, but it would be the attempt's own judgement. The claims file's criterion contradicts itself here: "
  "\"Testable only if the dataset holds the cervical micrographs\", which it does, and \"Not testable when only the vagus is "
  "traced\", which is also the case. The Summary's \"holds the 18 rat micrographs and the traces drawn over them lie within "
  "each image\" is not supported: only the nine cervical micrographs are drawn and checked.",
  "The contradiction is added to questions/pelot-2020.yaml as a question for a reader, and the notes say so; the claim is not "
  "changed. The Summary now says only the nine cervical micrographs were opened and drawn with their traces. Outcome unchanged.")
res=[]
for o in a['outcomes']:
    c=o['claim']; reason,resp=R.get(c,(default,"No change."))
    res.append(dict(claim=c,agrees=True,outcome=o['outcome'],reason=reason,response=resp))
entry=dict(date='2026-11-18',kind='agent',
  by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
  reviewed=("Round 2. The full executed notebook of the round-1 revision, with its conclusions and summary, the helper module, "
    "the claims file and the attempt record, with the paper under paper/. The verifier agreed with 34 of the 35 outcomes and "
    "with fascicles-larger-cervical only with qualification. It also found the Summary's sentence on C54-3 (\"the published code "
    "would measure the image frame (3.57 mm) in place of the nerve (1.62 mm)\") unsupported, as 3.57 appears in no output and "
    "cell 12 shows the code's own output file has 1615 um for C54-3; the Summary now says the mask is inverted and that its "
    "complement gives the code folder's 1615 um. Every other Result sentence, the rest of the Summary, the README and the "
    "record's notes it found to agree with the printed outputs, and the round-1 reasons to be stated accurately."),
  results=res)
txt=yaml.safe_dump([entry],sort_keys=False,width=110,allow_unicode=True)
s=open(p).read().rstrip('\n')+'\n'+txt
open(p,'w').write(s)
EOF
python $TMPDIR/ed5.py && python -c "
import yaml;a=yaml.safe_load(open('attempts/pelot-2020-01.yaml'));print(len(a['verifications']), len(a['verifications'][1]['results']))"; tail -30 attempts/pelot-2020-01.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='entries/pelot-2020/README.md'; s=open(p).read()
a="and the cervical against subdiaphragmatic fascicle comparison (Kenward-Roger degrees of freedom) |"
assert a in s
s=s.replace(a,"and the cervical against subdiaphragmatic fascicle comparison (the mixed model test). For that comparison a change to partially reproduced is proposed for a third verification round: under the test that gives the paper's F and p, the pig difference has p = 0.055 |")
a="match the traces. The attempt record"
s=s.replace(a,"""match the traces. The mixed models are tested with Kenward-Roger F tests on the observed
REML information, which give the paper's F and p for all nine effects it reports. The attempt record""")
open(p,'w').write(s)
EOF
date -u; python tools/entry.py all entries/pelot-2020 2>&1 | tail -15
```

```
Wed Nov 18 05:18:44 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-pelot-2020 in executed/pelot-2020/.venv/share/jupyter/kernels/registry-pelot-2020
0 error(s)
pass  reproduce_pelot_2020.ipynb  (230 s)
```

**Agent calls Bash**

```bash
cd entries/pelot-2020; python - <<'EOF'
import json,uuid
p='reproduce_pelot_2020.ipynb'; nb=json.load(open(p))
print(nb['nbformat'],nb['nbformat_minor'], sum('id' in c for c in nb['cells']), len(nb['cells']))
for c in nb['cells']:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
4 5 129 132
 attempts/pelot-2020-01.yaml                   | 476 +++++++++++++++++++++-----
 entries/pelot-2020/README.md                  |   5 +-
 entries/pelot-2020/reproduce_pelot_2020.ipynb | 255 +++++++++-----
 entries/pelot-2020/vagus.py                   |  30 +-
 questions/pelot-2020.yaml                     |  27 ++
 5 files changed, 607 insertions(+), 186 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/pelot-2020/reproduce_pelot_2020.ipynb | head -40; git diff entries/pelot-2020/reproduce_pelot_2020.ipynb | tail -15
```

```
diff --git a/entries/pelot-2020/reproduce_pelot_2020.ipynb b/entries/pelot-2020/reproduce_pelot_2020.ipynb
index fc17ddb..8ed5b16 100644
--- a/entries/pelot-2020/reproduce_pelot_2020.ipynb
+++ b/entries/pelot-2020/reproduce_pelot_2020.ipynb
@@ -39,9 +39,12 @@
     "\n",
     "**Mixed models.** The paper fits them in JMP Pro 14.3.0 without giving its settings. They are\n",
     "fitted here by REML with unbounded variance components, JMP's default, and tested with\n",
-    "Kenward-Roger F tests, the tests JMP reports for REML fits; with them the nerve diameter F\n",
-    "values are 587.3, 11.03 and 2.450 against the paper's 577.1, 11.01 and 2.445.\n",
-    "Satterthwaite, residual and subject-based degrees of freedom and a bounded fit are variants.\n",
+    "Kenward-Roger F tests computed on the observed REML information (the Hessian of the REML\n",
+    "log-likelihood). This choice is an assumption, made because it gives the paper's F and p for\n",
+    "all nine effects the paper reports (to within 0.4% for F, and p to the digits printed, with\n",
+    "the rat fascicle values the paper's code takes; see \"Which test the paper's F and p come\n",
+    "from\"). Kenward-Roger on the expected information, Satterthwaite, residual and subject-based\n",
+    "degrees of freedom and a bounded fit are variants.\n",
     "\n",
     "**Checksums.** Every file is checked against the SHA-256 of its version's manifest as it is\n",
     "read; the cell before the summary prints the SHA-256 of each file read.\n",
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff | grep "^+" | grep -n "—\|rather" ; echo; date -u; python tools/entry.py all entries/pelot-2020 2>&1 | tail -4
```

```
Wed Nov 18 05:22:59 UTC 2026
Installed kernelspec registry-pelot-2020 in executed/pelot-2020/.venv/share/jupyter/kernels/registry-pelot-2020
0 error(s)
pass  reproduce_pelot_2020.ipynb  (228 s)
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py 62 | grep -E "species with|pig contrast|24.6"; python $TMPDIR/show.py 53 | tail -3; git status --short
```

```
p_tukey                  species with p < 0.05: 2 of 3
p_kr_expected            species with p < 0.05: 3 of 3
p_satt                   species with p < 0.05: 3 of 3
p_resid_df               species with p < 0.05: 3 of 3
p_subject_df             species with p < 0.05: 2 of 3
p_tukey_bounded          species with p < 0.05: 3 of 3
p_code_rat               species with p < 0.05: 2 of 3
p_code_rat_kr_expected   species with p < 0.05: 3 of 3
p_code_rat_satt          species with p < 0.05: 2 of 3
p_code_rat_subject_df    species with p < 0.05: 3 of 3
the pig contrast's degrees of freedom: Kenward-Roger on the observed information 3.74, on the expected information 7.55, Satterthwaite 3.74
degrees of freedom at which the pig Tukey p (t = 4.767, 6 means) would be the paper's 0.0009: 24.6
F_kr_exp  largest relative difference from the paper's F (rat values as the code takes them): 5.09%
F_kr_obs  largest relative difference from the paper's F (rat values as the code takes them): 0.38%

 M attempts/pelot-2020-01.yaml
 M entries/pelot-2020/README.md
 M entries/pelot-2020/reproduce_pelot_2020.ipynb
 M entries/pelot-2020/vagus.py
 M questions/pelot-2020.yaml
[... 11 more lines not kept]
```

**Agent**

No outcome changed. I've proposed one change for a third verification round: fascicles-larger-cervical from reproduced to partially reproduced. `python tools/entry.py all entries/pelot-2020` passes (0 check errors, notebook ran in 228 s), and the text matches the new outputs. Nothing is committed.

**The main finding.** The verifier was right that Kenward-Roger as I had it was not the paper's test. Its degrees of freedom were up to twice the ones implied by the paper's own F and p values. I added a variant of Kenward-Roger that uses the observed information in place of the expected information (in `vagus.py`). It gives the paper's numbers for all nine effects the paper reports:
- F within 0.4% and p to the digits printed. For example, nerve diameter gives 577.0, 11.01 (p = 0.0030) and 2.4455 (p = 0.1085), against the paper's 577.1, 11.01 (0.0030) and 2.445 (0.1085).
- Degrees of freedom within 1 of those the paper implies.
- For fascicle diameter, the exact match needs the rat values the paper's code takes. This confirms again that the paper's statistics used the code's rule, not the "largest fascicle" of its Methods.

I made this the main test for every mixed-model claim, still marked as an assumption. The old Kenward-Roger test and the other variants are still shown. A new notebook section, "Which test the paper's F and p come from", sets the paper's implied degrees of freedom beside each test.

**Effect on the outcomes.**
- **fascicles-larger-cervical:** under the new test the pig contrast has p = 0.055 (0.060 with the code's rat values), so only two of three species hold. The verified outcome (reproduced) stays, and `proposed` gives partially_reproduced with the reason. No variant gives the paper's pig p of 0.0009. With this contrast's t it would need about 25 degrees of freedom, and I added that question to the existing finding that asks the authors about JMP's settings.
- **The seven other mixed-model claims** keep their outcomes; their numbers in the notebook, record and README are updated.

**Text corrected, as the verifier asked:**
- **rat-ten-times-smaller:** the p values now match what the notebook prints, with a note that values this small are at the limit of numerical precision.
- **Summary, rat values:** they now say they match the code's output file exactly and the paper only to rounding (0.2577 against 0.260 mm). The rat subdiaphragmatic fascicle diameter matches the paper only under the code's rule.
- **Summary, C54-3:** the unsupported "3.57 mm image frame" sentence is gone. The mask is inverted, and measuring the nerve from its complement gives the code output file's 1615 µm.
- **Summary, micrographs:** it now says only the nine cervical micrographs were opened and checked.

**Questions for a reader** (claims not changed), added to `questions/pelot-2020.yaml`:
- Should the fascicle-diameter criteria use the Methods' "largest fascicle" or the code's first-trace rule? It changes no outcome here but does change the values reported against the paper.
- The rat-carotid-sheath-bundles criterion contradicts itself for this dataset, which has the cervical micrographs but traces only the vagus.

**Round 2 recorded** under `verifications`, with all 35 claims marked as agreed as the verifier gave them; fascicles-larger-cervical is noted as "only with qualification". Each entry has its reason taken from the report and my response.

**Not changed:**
- rat-literature-comparison and no-age-trend still depend on a reading. Both are already stated and assumed, and the verifier did not ask for a change.
- The main rat rule stays the Methods' "largest fascicle", as agreed in round 1, even though the new test confirms the paper used the code's values.

## End of run

49 turns, 23 minutes, $3.20 at API prices, result: success.
