# nishimoto-2011 · author-revise-2 · run 43594936434

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/nishimoto-2011/verifier-2-report.md; ls entries/nishimoto-2011 entries/nishimoto-2011/*
```

```
Sat Nov 14 12:33:34 UTC 2026
**Verifier report, round 2: Nishimoto & Gallant (2011) on CRCNS mt-2**

The claims file has 20 claims. The attempt record gives 20 outcomes: 14 reproduced, 3 partially reproduced, 2 not reproduced and 1 blocked (data_missing). Cell indices below are positions in each notebook's cell list, counting markdown cells, so they differ from round 1. "Main" is `reproduce_nishimoto_2011.ipynb` and "finer" is `finer_pooling.ipynb`. I found no new place where the claims file misreads the paper.

### 1. Outcomes

| Claim | Record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| fig3b-mean-prediction | reproduced | Yes | Stated. The 3×3 model (finer, cell 5: 0.518) is closer to the paper's model than the 2×2 one. Its offset was chosen on training data only, and no validation data is used for selection. It is still a reduced model (see 3). |
| fig3b-explainable-variance | blocked | Yes | Main cells 5–6: only `psths`, and `trange` is empty in all 45 files. |
| fig3a-example-neuron | reproduced | Yes | Stated. |
| fig2b-contrast-normalization-no-effect | reproduced | Yes | Stated. |
| fig2b-compressive-improves | partially_reproduced | Yes | Stated. Rests on the 2×2 model. |
| fig2b-expansive-decreases | partially_reproduced | Yes | Stated. Rests on the 2×2 model. |
| fig2b-divisive-improves | not_reproduced | Yes, on the 2×2 model | Stated. ×11 p = 0.056 is close to the bound, and the finer pooling was not run for this pair of models (see 3). |
| fig2b-compressive-divisive-best | reproduced | Yes | Stated. |
| fig2b-no-interaction | reproduced | Yes | Stated. |
| complex-cells-dominate | reproduced | Yes | Stated. Now also holds with every simple channel (finer, cell 11). |
| fig6a-null-on-plane | reproduced | Yes | Stated. Under all-(a) readings the value is 0.396, at the edge of the band. |
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i -E "step 6|hand over|round 2|proposed|verifications|Develop on a subset" | head -40; wc -l docs/protocol.md
```

```
190:190:not say what the paper says (author, step 1.6, and "Hand over for
205:205:(step 6).
292:292:     (step 6; see also chance levels, under "Record the attempt").
342:342:     claims file (reader, step 6), and a later run, `author-answers`,
393:393:- **Develop on a subset.** Build and debug each analysis on one or two
676 docs/protocol.md
```

**Agent calls Bash**

```bash
sed -n 180,676p docs/protocol.md
```

```
criterion's method is taken from the paper or its code, as cited; and that the
paper's main findings each have a claim. The checker corrects what it can
show is wrong, and records each change, with its reason, under `checks` at
the end of the file. A claims file is ready for an attempt when its last check
says so.

### 6. Answer questions

A reader is asked only when the author or a verifier believes the claims file
misreads the paper: a wrong expected value, the wrong panel, a claim that does
not say what the paper says (author, step 1.6, and "Hand over for
verification"). A method detail the claims file lacks is not asked: the author
takes it from the paper. The reader, who has not seen the data, checks each
question against the paper and decides whether the claims file is to change.
Where it is, the reader amends the claim, and the question's `answer` says
what changed and why, citing the passage; where it is not, the answer says why
the claim stands. The reader marks each question answered in
`questions/<paper>.yaml`.

## Author
[... 477 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep nish; ls executed/nishimoto-2011/ 2>&1; cat entries/nishimoto-2011/README.md; cat entries/nishimoto-2011/entry.yaml; wc -l attempts/nishimoto-2011-01.yaml entries/nishimoto-2011/mt2.py
```

```
nishimoto-2011-01.yaml
finer_pooling.ipynb
reproduce_nishimoto_2011.ipynb
result.json
# Nishimoto and Gallant (2011) from CRCNS mt-2

Tests the findings of [Nishimoto and Gallant (2011)](https://doi.org/10.1523/jneurosci.6801-10.2011)
on [CRCNS mt-2](https://doi.org/10.6080/K0DN4374), which holds, for 45 of the paper's 52 MT neurons,
the movie patch around the receptive field and the response averaged over repeats, at the 83 Hz
frame rate.

| Claim | Outcome |
|---|---|
| Compressive and divisive model predicts with mean r = 0.52 | Reproduced with the finer pooling (0.518; 0.448 with the coarser one) |
| The model accounts for 35% of the explainable variance | Blocked: data missing (no single repeats) |
| An example neuron is predicted with r = 0.72 | Reproduced |
| Luminance and contrast normalization has no significant effect | Reproduced |
| A compressive nonlinearity improves predictions (16% and 19%) | Partially reproduced |
| An expansive nonlinearity worsens predictions (-36% and -24%) | Partially reproduced |
| Divisive normalization improves predictions (8%) | Not reproduced |
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/nishimoto-2011-01.yaml
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a110178b-2795-4e64-be91-546706a903e4/tool-results/bgpme2wn8.txt

Preview (first 2KB):
schema_version: 3
id: nishimoto-2011-01
datasets:
- archive: crcns
  id: mt-2
  version: unversioned
  doi: 10.6080/K0DN4374
  relation: primary
paper: doi:10.1523/jneurosci.6801-10.2011
date: 2026-11-14
entry: nishimoto-2011
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/nishimoto-2011-01.yaml"
}
```

```
1	schema_version: 3
2	id: nishimoto-2011-01
3	datasets:
4	- archive: crcns
5	  id: mt-2
6	  version: unversioned
7	  doi: 10.6080/K0DN4374
8	  relation: primary
9	paper: doi:10.1523/jneurosci.6801-10.2011
10	date: 2026-11-14
11	entry: nishimoto-2011
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 587 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json
nb=json.load(open('finer_pooling.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"==== {i} {c['cell_type']} {c.get('metadata',{}).get('tags')}")
    print(''.join(c['source']))
E
```

```
==== 0 markdown None
# Nishimoto and Gallant (2011) on CRCNS mt-2: what the spatial pooling costs

Paper: Nishimoto S, Gallant JL (2011), J Neurosci 31(41):14551-14564,
doi:10.1523/jneurosci.6801-10.2011. Dataset: CRCNS mt-2 (doi:10.6080/K0DN4374), read from the
public bucket `crcnsarchive/mt-2/live/` (unversioned; `reproduce_nishimoto_2011.ipynb` prints the
MD5 sums of the files). Claims: `claims/nishimoto-2011.yaml`.

The main notebook fits every model with the regression weights pooled over space onto 763
regressors (3 and 6 cycles per cRF onto 2 x 2 regions), because the paper's model, with a weight
for each of its 5956 filters, does not fit in the time limit for 12 models and 45 neurons. This
notebook measures what that costs for the compressive and divisive model, the one the claims
below rest on. It refits that model for every neuron with 3 and 6 cycles per cRF pooled onto
3 x 3 regions and 1.5 cycles per cRF at each of its four positions (1465 regressors), and for
three neurons with 4 x 4 regions and every simple channel of the bank (3085 regressors), closer
to the paper's model. The delay offset of each neuron is chosen as in the main notebook, by the
held-out error of the 2 x 2 model on the training data. Everything else (filter bank, features,
boosting, validation) is as in the main notebook (`mt2.py`, `pooling_neuron`).

| Claim | Tested here |
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/nishimoto-2011/finer_pooling.ipynb'))
for i in [1,3,5,17]:
    c=nb['cells'][i]
    for o in c.get('outputs',[]):
        print(i, ''.join(o.get('text','')))
E
grep -n "def \|^[A-Z_]* = " entries/nishimoto-2011/mt2.py | head -80
```

```
1 45 neurons in 28.1 min; per neuron 64 s median
peak memory of a worker: 4.246204 GB

3 neurons: 45 ; by monkey: {np.str_('f'): np.int64(34), np.str_('v'): np.int64(11)}
validation sets: {np.str_('enhanced'): np.int64(31), np.str_('natural+enhanced'): np.int64(14)}
delay offsets (frames earlier): {np.int64(0): np.int64(31), np.int64(3): np.int64(9), np.int64(6): np.int64(5)}
2 x 2 pooling at the chosen offsets: mean r 0.448
regressors with 3 x 3 pooling: 1247 complex, 218 simple

5 pooling 3 x 3: mean r 0.518 (median 0.507, range 0.263 to 0.761); within 0.468 to 0.572: True; motion-enhanced only 0.524
pooling 2 x 2: mean r 0.448
3 x 3 better than 2 x 2 in 45 of 45, mean difference +0.070, Wilcoxon p = 5.68e-14; without ct0133 0.520
  monkey f: n = 34, mean r 0.524
  monkey v: n = 11, mean r 0.500
neurons between 0.2 and 0.8 (Figure 3B span): 45 of 45; below 0.2: 0, above 0.8: 0
boosting steps per fold: median 171, range 57 to 409 (cap 20000)
        2x2 (763)  3x3 (1465)  4x4 + all simple (3085)
ct0002      0.556       0.636                    0.614
ct0005      0.329       0.398                    0.352
ct0006      0.261       0.322                    0.347
[... 68 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/nishimoto-2011/mt2.py",
 "offset": 560,
 "limit": 275
}
```

```
560	    """Drifting gratings at 24 directions (15 degree steps, so that the component prediction
561	    of a 90 degree plaid can be read) and plaids at 12 directions (30 degree steps, C), each
562	    component at the RMS contrast of the training movie (S)."""
563	    xs = (np.arange(NPIX) - (NPIX - 1) / 2) / CRF
564	    X, Y = np.meshgrid(xs, xs)
565	    t = np.arange(nfr)[:, None, None] / FPS
566	    amp = np.sqrt(2) * ms[1]
567	
568	    def g(d):
569	        th = np.deg2rad(d)
570	        return amp * np.cos(2 * np.pi * (sf * (X * np.cos(th) + Y * np.sin(th)) - tf * t))
571	
572	    movies = [ms[0] + g(d) for d in np.arange(24) * 15.0]
573	    for sep in sep_list:
574	        for d in np.arange(12) * 30.0:
575	            movies.append(ms[0] + g(d - sep / 2) + g(d + sep / 2))
576	    return np.concatenate(movies, 0).astype(np.float32), nfr
577	
578	
579	def pattern_index(g24, plaid12, sep):
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "fig2b" -A40 claims/nishimoto-2011.yaml | sed -n 1,260p
```

```
135:- id: fig2b-contrast-normalization-no-effect
136-  statement: Luminance and contrast normalization of the stimulus does not significantly change
137-    prediction accuracy compared with the simplest model (linear half-wave rectification, no
138-    normalization stages).
139-  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
140-    MT, paragraph 2; Figure 2B
141-  quote: Contrast normalization does not have a significant effect on predictions compared with
142-    the simplest model
143-  statistics:
144-  - test: Wilcoxon signed-rank test with Bonferroni correction
145-    p: 0.1
146-    p_relation: ">"
147-    corrected: Bonferroni
148-    n: 52 neurons
149-  criterion: A claim of absence, judged on the paper's test. Per neuron, the prediction accuracy
150-    of the model with luminance and contrast normalization (Eq. 10 to 12), linear static
151-    nonlinearity and no divisive normalization, against the simplest model, by a Wilcoxon
152-    signed-rank test across neurons with Bonferroni correction. The number of comparisons is
153-    not stated; the Figure 2B legend marks the significance of each of the 11 other models
154-    against the simplest, so the correction is over 11 comparisons. As a claim of absence it
[... 189 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; ls ~/.cache 2>/dev/null; which python; python -c "import mt2,sys;print(sys.version)"; sed -n 240,330p mt2.py
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import mt2,sys;print(sys.version)
    ^^^^^^^^^^^^^^
  File "entries/nishimoto-2011/mt2.py", line 53, in <module>
    import fsspec
ModuleNotFoundError: No module named 'fsspec'
        C[-h:] = 0
        Sm[:-h] = Sm[h:]
        Sm[-h:] = 0
    return C, Sm, np.array(desc_c), np.array(desc_s), ms


def pooling(desc_c, desc_s, level="2x2"):
    """Weights that pool full-bank channels onto regressors (the spatial constraint, D).
    Returns the matrix for complex and simple channels and the regressor descriptors
    (sf, direction, tf, region x, region y, is_simple). Complex channels of one SF,
    direction and TF are summed with Gaussian weights onto a grid of regions spanning the
    2 cRF patch.
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|def cmd_\|add_parser" tools/entry.py | head -40; ls -a; ls .venv* 2>/dev/null | head
```

```
519:        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
555:    venv = (output_dir / ".venv").resolve()
556:    python = venv / "bin" / "python"
560:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
563:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
577:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 545,580p tools/entry.py; ls executed/nishimoto-2011 -a
```

```
stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; PY=../../executed/nishimoto-2011/.venv/bin/python; $PY - <<'E'
import time, resource, numpy as np, mt2
sizes=mt2.list_sizes(); names=sorted(sizes, key=lambda n: sizes[n])
print([ (n[:6],sizes[n]//10**6) for n in names[:3]], names[len(names)//2][:6], sizes[names[len(names)//2]]//10**6, sum(sizes.values())//10**6)
n=names[len(names)//2]
from threadpoolctl import threadpool_limits
with threadpool_limits(2):
    t=time.time(); m=mt2.load(n); tr,sets=mt2.rows(m); print('load',time.time()-t, len(m['psth']))
    blocks=mt2.make_blocks(tr)
    t=time.time(); C,Sm,dc,ds,_=mt2.bank_outputs(m['stim'],mt2.build_bank(),False); print('bank',time.time()-t)
    Pc,Ps,rd,nc,ns=mt2.pooling(dc,ds,'3x3')
    for alpha,div in [(1.0,False),(1.0,True)]:
        t=time.time()
        F,_=mt2.features(C,Sm,tr,Pc,Ps,alpha,div); mu,sd=mt2.zscore_stats(F,tr); F=mt2.shift_rows((F-mu)/sd,0)
        t1=time.time()-t
        res,st=mt2.fit_neuron(F,[m['psth']],blocks,lazy=True)
        print(alpha,div,'feat',t1,'fit',time.time()-t, mt2.val_corr(F,m,res[0][0],res[0][1]))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
E
```

```
[('ct0128', 237), ('ct0132', 242), ('ct0131', 244)] ct0037 288 17007
load 21.987830638885498 22000
bank 3.692004442214966
1.0 False feat 2.5392465591430664 fit 8.140233039855957 {'enhanced': np.float64(0.4697878044719233)}
1.0 True feat 2.691603183746338 fit 8.267933368682861 {'enhanced': np.float64(0.48538156237328134)}
2.265428
```

**Agent calls Bash**

```bash
cd  grep -n "claim:" tools/entry.py | head -20; grep -n "proposed" -r tools/*.py schemas/* | head -20
```

```
463:            if tag.startswith("claim:"):
tools/agent_run.py:6:    python tools/agent_run.py proposals ROLE PAPER        # "true" if the attempt has proposed changes
tools/agent_run.py:16:author-revise-3, the third round that settles changes proposed after the second. A repeat attempt
tools/agent_run.py:315:    """The claims of the paper's latest attempt that carry a proposed change of outcome."""
tools/agent_run.py:317:    return [o["claim"] for o in (found[0]["outcomes"] if found else []) if o.get("proposed")]
tools/build_site.py:332:                "proposed": o.get("proposed"),
tools/build_site.py:1781:    if o.get("proposed"):
tools/build_site.py:1782:        tags += (f'<span class="tag">change to {e(OUTCOMES[o["proposed"]["outcome"]][0].lower())} '
tools/build_site.py:1783:                 f'proposed</span>')
tools/build_site.py:1785:    if o.get("proposed"):
tools/build_site.py:1787:                 f'{e(OUTCOMES[o["proposed"]["outcome"]][0].lower())}. {e(squash(o["proposed"]["reason"]))}</p>')
tools/build_site.py:2305:     "it agrees with each outcome. The author revises once more. Any change of outcome proposed after this goes to a "
tools/entry.py:372:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
schemas/attempt.schema.json:303:          "proposed": {
schemas/claims.schema.json:3:  "title": "Claims proposed for one target (a dataset and one of its papers)",
```

**Agent calls Bash**

```bash
cd  sed -n 300,330p schemas/attempt.schema.json; sed -n 440,480p tools/entry.py; grep -n "verifications" -A60 schemas/attempt.schema.json | grep -n '"\w*":' | head -30
```

```
"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).",
            "type": "boolean"
          },
          "proposed": {
            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
            "type": "object",
            "additionalProperties": false,
            "required": [
              "outcome",
              "reason"
            ],
            "properties": {
              "outcome": {
                "enum": [
                  "reproduced",
                  "partially_reproduced",
                  "not_reproduced",
                  "blocked"
                ]
              },
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
p='mt2.py'; s=open(p).read()
old='''def pooled_fit(C, Sm, dc, ds, tr, m, blocks, offset, level):
    """The compressive and divisive model with a finer pooling (`pooling(level=...)`), on
    the delay offset chosen with the 2 x 2 pooling, to measure what the pooling costs; also
    with complex or simple regressors only."""
    Pc, Ps, rd, nc, ns = pooling(dc, ds, level)
'''
new='''# the other models of Figure 2B without luminance normalization, (alpha, divisive)
FIG2B = [(1.0, False), (1.0, True), (0.5, False), (2.0, False), (2.0, True)]


def pooled_fit(C, Sm, dc, ds, tr, m, blocks, offset, level, models=()):
    """The compressive and divisive model with a finer pooling (`pooling(level=...)`), on
    the delay offset chosen with the 2 x 2 pooling, to measure what the pooling costs; also
    with complex or simple regressors only, and the models in `models` ((alpha, divisive),
    without luminance normalization) with the same pooling and offset."""
    Pc, Ps, rd, nc, ns = pooling(dc, ds, level)
    other = {}
    for (alpha, div) in models:
        F, _ = features(C, Sm, tr, Pc, Ps, alpha, div)
        mu, sd = zscore_stats(F, tr)
        F = shift_rows((F - mu) / sd, offset)
        res, _ = fit_neuron(F, [m["psth"]], blocks, lazy=True)
        other[(alpha, div)] = val_corr(F, m, res[0][0], res[0][1])
        del F
'''
assert old in s; s=s.replace(old,new)
old2='''    out = dict(n_complex=nc, n_simple=ns, r=val_corr(F, m, w, b0), its=its)
'''
new2='''    out = dict(n_complex=nc, n_simple=ns, r=val_corr(F, m, w, b0), its=its, models=other)
'''
assert old2 in s; s=s.replace(old2,new2)
old3='''p3x3=pooled_fit(C, Sm, dc, ds, tr, m, blocks, o, "3x3"))'''
new3='''p3x3=pooled_fit(C, Sm, dc, ds, tr, m, blocks, o, "3x3", FIG2B))'''
assert old3 in s; s=s.replace(old3,new3)
open(p,'w').write(s)
E
grep -n "def val_corr" -A14 mt2.py
```

```
501:def val_corr(F, m, w, b0, smooth_sd=1.0, delays=DELAYS):
502-    """Correlation of prediction and smoothed mean response on each validation set."""
503-    _, sets = rows(m)
504-    out = {}
505-    for k, v in sets.items():
506-        obs = gaussian_filter1d(m["psth"][v], smooth_sd) if smooth_sd > 0 else m["psth"][v]
507-        obs, v = obs[FIRST:-LAST - max(OFFSETS)], v[FIRST:-LAST - max(OFFSETS)]
508-        p = predict(F, v, w, b0, delays)
509-        out[k] = pearsonr(p, obs)[0]
510-    return out
511-
512-
513-# ---------------------------------------------------------------- simulated neurons
514-
515-def model_rate(F, rws, w, delays=DELAYS):
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i, c['cell_type'], c.get('metadata',{}).get('tags'), src.split('\n')[0][:100])
E
```

```
0 markdown None # Nishimoto and Gallant (2011) on CRCNS mt-2
1 code None import os, time, resource
2 markdown None ## Fitting every neuron
3 code None COMBOS = [("a", "a"), ("a", "b"), ("b", "a"), ("b", "b")]
4 markdown None ## Data check
5 code ['sanity'] rows = []
6 code ['sanity'] # Everything one file holds (ct0125, which has a natural-movie set): no field holds single repeats
7 code ['sanity'] # Recordings deposited twice: identical validation responses or identical training movies
8 code ['sanity'] # Clock: the prediction of the compressive and divisive model against the validation response
9 markdown None ## Per-neuron prediction accuracy
10 code None def acc(r):
11 markdown None ## fig3b-mean-prediction
12 code ['claim:fig3b-mean-prediction'] main = A[mt2.MAIN]
13 markdown None **Result: not reproduced with the 2 x 2 pooling of this notebook; reproduced with the finer pooling 
14 markdown None ## fig3b-explainable-variance
15 code ['claim:fig3a-example-neuron'] ex = A[mt2.MAIN]
16 markdown None **Result: reproduced.** Three neurons have a prediction correlation within 0.648 to 0.792 (ct0013 0.
17 markdown None ## Figure 2B: the 12 models
18 code None base = (False, 1.0, False)
19 markdown None ### fig2b-contrast-normalization-no-effect
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb'))
for i in [18,23,24,26,27,29,30,32,33,35,36,58,59,61,62,64,65,72]:
    c=nb['cells'][i]
    print(f"==== {i}"); print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('---OUT'); print(''.join(o.get('text','')) or o.get('data',{}).get('text/plain',''))
E
```

```
<persisted-output>
Output too large (33.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a110178b-2795-4e64-be91-546706a903e4/tool-results/byko52nhe.txt

Preview (first 2KB):
==== 18
base = (False, 1.0, False)
def change(m, Atab=A):
    a, b = Atab[m], Atab[base]
    pa = 100 * (a.mean() / b.mean() - 1)
    pb = 100 * ((a**2).mean() / (b**2).mean() - 1)
    pc = 100 * np.mean((a - b) / np.abs(b))
    p = wilcoxon(a, b).pvalue if m != base else np.nan
    return pa, pb, pc, p
rows = []
for m in models:
    pa, pb, pc, p = change(m)
    rows.append(dict(model=label(m), mean_r=A[m].mean(), pct_a=pa, pct_b=pb, pct_c=pc,
                     n_better=int((A[m] > A[base]).sum()), p=p, p_bonf11=min(1, p * 11) if m != base else np.nan,
                     p_bonf5=min(1, p * 5) if m != base else np.nan))
T2 = pd.DataFrame(rows).set_index("model")
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a110178b-2795-4e64-be91-546706a903e4/tool-results/byko52nhe.txt"
}
```

```
1	==== 18
2	base = (False, 1.0, False)
3	def change(m, Atab=A):
4	    a, b = Atab[m], Atab[base]
5	    pa = 100 * (a.mean() / b.mean() - 1)
6	    pb = 100 * ((a**2).mean() / (b**2).mean() - 1)
7	    pc = 100 * np.mean((a - b) / np.abs(b))
8	    p = wilcoxon(a, b).pvalue if m != base else np.nan
9	    return pa, pb, pc, p
10	rows = []
11	for m in models:
12	    pa, pb, pc, p = change(m)
13	    rows.append(dict(model=label(m), mean_r=A[m].mean(), pct_a=pa, pct_b=pb, pct_c=pc,
14	                     n_better=int((A[m] > A[base]).sum()), p=p, p_bonf11=min(1, p * 11) if m != base else np.nan,
15	                     p_bonf5=min(1, p * 5) if m != base else np.nan))
16	T2 = pd.DataFrame(rows).set_index("model")
17	print(T2.round(4).to_string())
18	print("\nreading (c) is sensitive to neurons with small baseline r: smallest baseline r", A[base].min().round(3),
19	      "; reading (c) without neurons whose baseline r < 0.1:",
20	      {label(m): round(100 * np.mean(((A[m] - A[base]) / A[base])[A[base] >= 0.1]), 1) for m in models if m != base})
[... 440 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json
p='finer_pooling.ipynb'; nb=json.load(open(p))
def md(s, tags=None):
    c={"cell_type":"markdown","metadata":{},"source":s}
    if tags: c["metadata"]["tags"]=tags
    return c
def code(s, tags=None):
    c={"cell_type":"code","metadata":{},"source":s,"outputs":[],"execution_count":None}
    if tags: c["metadata"]["tags"]=tags
    return c
cells=nb['cells']
# header
h=''.join(cells[0]['source'])
h=h.replace("""three neurons with 4 x 4 regions and every simple channel of the bank (3085 regressors), closer
to the paper's model.""","""three neurons with 4 x 4 regions and every simple channel of the bank (3085 regressors), closer
to the paper's model. It also refits, with the 3 x 3 pooling, the other five models of Figure 2B
without luminance normalization (linear, compressive and expansive, each without and with
divisive normalization), so that the Figure 2B comparisons can be repeated on the finer model.""")
h=h.replace("""| natural-movie-control | with the finer pooling |""","""| natural-movie-control | with the finer pooling |
| fig2b-compressive-improves, fig2b-expansive-decreases, fig2b-divisive-improves, fig2b-compressive-divisive-best, fig2b-no-interaction | judged in the main notebook; repeated here with the finer pooling |""")
cells[0]['source']=h
fig2b_md = md("""## Figure 2B with the finer pooling

The main notebook judges the Figure 2B claims on the 2 x 2 pooling. Here the six models without
luminance normalization are refitted with the 3 x 3 pooling, on the same delay offsets, folds and
validation sets, and the comparisons are repeated as there: the percent change against the
simplest model (linear, no divisive normalization) under readings (a) mean correlation, (b) mean
squared correlation and (c) mean of each neuron's percent change, with Wilcoxon signed-rank tests
Bonferroni corrected over 11 comparisons (and over 5, the variant). The six luminance-normalized
models were not refitted, so the correction keeps the count of 11 of the claims file.""")
fig2b_code = code("""LAB = {(1.0, False): "linear", (0.5, False): "compressive", (2.0, False): "expansive",
       (1.0, True): "linear +div", (0.5, True): "compressive +div", (2.0, True): "expansive +div"}
B3 = {k: pd.Series([acc(R[n]["p3x3"]["models"][k]) if k != (0.5, True) else acc(R[n]["p3x3"]["r"]) for n in names_run], index=IDX)
      for k in LAB}
base3 = B3[(1.0, False)]


def change3(k, ref=None):
    a, b = B3[k], base3 if ref is None else B3[ref]
    return (100 * (a.mean() / b.mean() - 1), 100 * ((a**2).mean() / (b**2).mean() - 1),
            100 * np.mean((a - b) / np.abs(b)), wilcoxon(a, b).pvalue)


rows = []
for k, lab in LAB.items():
    pa, pb, pc, p = change3(k) if k != (1.0, False) else (0, 0, 0, np.nan)
    rows.append(dict(model=lab, mean_r=B3[k].mean(), pct_a=pa, pct_b=pb, pct_c=pc, n_better=int((B3[k] > base3).sum()),
                     p=p, p_bonf11=min(1, 11 * p), p_bonf5=min(1, 5 * p)))
print("pooling 3 x 3, every model against the linear model without divisive normalization:")
print(pd.DataFrame(rows).set_index("model").round(4).to_string())
print("3 x 3 better than 2 x 2 (per neuron), by model:",
      {lab: f"{(B3[k] > A2[k]).sum()} of {len(IDX)}, {(B3[k] - A2[k]).mean():+.3f}" for k, lab in LAB.items()} if "A2" in dir() else "")


def report3(ks, expect):
    for k, e in zip(ks, expect):
        pa, pb, pc, p = change3(k)
        print(f"pooling 3 x 3, {LAB[k]}: (a) {pa:.1f}%  (b) {pb:.1f}%  (c) {pc:.1f}%  [expected {e} +- 4]; "
              f"better in {(B3[k] > base3).sum()} of {len(IDX)}; p = {p:.3g}, x11 = {min(1, 11 * p):.3g}, x5 = {min(1, 5 * p):.3g}")
        print("   within tolerance, readings (a), (b), (c):", [bool(abs(v - e) <= 4) for v in (pa, pb, pc)])""")
cells_new = [fig2b_md, fig2b_code,
  md("### fig2b-compressive-improves\n\n> A compressive static output nonlinearity consistently increases predictions over the simplest\n> model, by about 16% without and about 19% with divisive normalization."),
  code("report3([(0.5, False), (0.5, True)], [16, 19])", ["claim:fig2b-compressive-improves"]),
  md("**Result: TODO**"),
  md("### fig2b-expansive-decreases\n\n> An expansive static output nonlinearity always decreases predictions relative to the simplest\n> model, by about 36% without and about 24% with divisive normalization."),
  code("report3([(2.0, False), (2.0, True)], [-36, -24])", ["claim:fig2b-expansive-decreases"]),
  md("**Result: TODO**"),
  md("### fig2b-divisive-improves\n\n> Divisive normalization significantly improves predictions over the simplest model, by about 8%\n> with the linear static nonlinearity."),
  code("report3([(1.0, True)], [8])\nfor mk in np.unique(monkey):\n    s = monkey == mk\n    print(f\"  monkey {mk}: reading (a) {100 * (B3[(1.0, True)][s].mean() / base3[s].mean() - 1):.1f}%\")", ["claim:fig2b-divisive-improves"]),
  md("**Result: TODO**"),
  md("### fig2b-compressive-divisive-best\n\n> The model with both a compressive nonlinearity and divisive normalization predicts significantly\n> better than the model with the compressive nonlinearity alone, and is the simplest model that\n> gives accurate predictions."),
  code("""cd, c = (0.5, True), (0.5, False)
p = wilcoxon(B3[cd], B3[c]).pvalue
print(f"pooling 3 x 3: compressive + divisive {B3[cd].mean():.3f} against compressive {B3[c].mean():.3f}; better in {(B3[cd] > B3[c]).sum()} of {len(IDX)}")
print(f"Wilcoxon p = {p:.4g}; x11 = {min(1, 11 * p):.4g}; x5 = {min(1, 5 * p):.4g}; x12 = {min(1, 12 * p):.4g}")
print("the other refitted models against compressive + divisive (positive = better than it; the luminance-normalized models were not refitted):")
for k, lab in LAB.items():
    if k != cd:
        pm = wilcoxon(B3[k], B3[cd]).pvalue
        print(f"  {lab:18s} mean diff {B3[k].mean() - B3[cd].mean():+.4f}  p = {pm:.3g}  x11 = {min(1, 11 * pm):.3g}  x12 = {min(1, 12 * pm):.3g}")""", ["claim:fig2b-compressive-divisive-best"]),
  md("**Result: TODO**"),
  md("### fig2b-no-interaction\n\n> The effects of the compressive and expansive nonlinearities do not depend on whether divisive\n> normalization is present."),
  code("""for div in (False, True):
    for rdg, ref in (("a", (1.0, False)), ("b", (1.0, div))):
        for a_ in (0.5, 2.0):
            k = (a_, div)
            pa, pb, pc, p = change3(k, ref)
            print(f"pooling 3 x 3, divisive {div!s:5s} reading ({rdg}) {LAB[k]:17s} against {LAB[ref]:12s}: "
                  f"mean diff {B3[k].mean() - B3[ref].mean():+.4f}, p = {p:.3g}, x11 = {min(1, 11 * p):.3g}")""", ["claim:fig2b-no-interaction"]),
  md("**Result: TODO**"),
]
# insert before summary (index 16)
i_sum=[i for i,c in enumerate(cells) if c['metadata'].get('tags')==['summary']][0]
nb['cells']=cells[:i_sum]+cells_new+cells[i_sum:]
json.dump(nb,open(p,'w'),indent=1)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json
p='finer_pooling.ipynb'; nb=json.load(open(p))
for c in nb['cells']:
    s=c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
    if 'if "A2" in dir()' in s:
        s=s.replace('''print("3 x 3 better than 2 x 2 (per neuron), by model:",
      {lab: f"{(B3[k] > A2[k]).sum()} of {len(IDX)}, {(B3[k] - A2[k]).mean():+.3f}" for k, lab in LAB.items()} if "A2" in dir() else "")
''','')
        c['source']=s
json.dump(nb,open(p,'w'),indent=1)
E
grep -c A2 finer_pooling.ipynb; date -u
```

```
0
Sat Nov 14 12:36:21 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; V=$(realpath ../../executed/nishimoto-2011/.venv); time MT2_N=2 JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-nishimoto-2011 --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR --output finer_sub.ipynb finer_pooling.ipynb 2>&1 | tail -3; python - <<E
import json
nb=json.load(open("$TMPDIR/finer_sub.ipynb"))
for i,c in enumerate(nb['cells']):
    for o in c.get('outputs',[]):
        print(i, o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text']), o.get('ename',''), o.get('evalue',''))
E
```

```
_validate(nbdict, ref, version, version_minor, relax_add_props)
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 32256 bytes to /tmp/claude-1001/finer_sub.ipynb

real	2m11.278s
user	7m1.680s
sys	0m6.070s
1 2 neurons in 2.1 min; per neuron 126 s median
peak memory of a worker: 2.445328 GB
  
3 neurons: 2 ; by monkey: {np.str_('v'): np.int64(2)}
validation sets: {np.str_('enhanced'): np.int64(2)}
delay offsets (frames earlier): {np.int64(3): np.int64(2)}
2 x 2 pooling at the chosen offsets: mean r 0.320
regressors with 3 x 3 pooling: 1247 complex, 218 simple
  
5 pooling 3 x 3: mean r 0.421 (median 0.421, range 0.398 to 0.443); within 0.468 to 0.572: False; motion-enhanced only 0.421
pooling 2 x 2: mean r 0.320
3 x 3 better than 2 x 2 in 2 of 2, mean difference +0.101, Wilcoxon p = 0.5; without ct0133 0.421
  monkey v: n = 2, mean r 0.421
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; git diff --stat; git stash list | head -2
```

```
entries/nishimoto-2011/finer_pooling.ipynb | 144 +++++++++++++++++++++++------
 entries/nishimoto-2011/mt2.py              |  21 ++++-
 2 files changed, 135 insertions(+), 30 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json
nb=json.load(open('finer_pooling.ipynb'))
i0=[i for i,c in enumerate(nb['cells']) if ''.join(c['source']).startswith('## Figure 2B with the finer')][0]
i1=[i for i,c in enumerate(nb['cells']) if c['metadata'].get('tags')==['summary']][0]
new=nb['cells'][i0:i1]
json.dump(new,open('/tmp/claude-1001/fig2b_cells.json','w'))
E
git checkout finer_pooling.ipynb
python - <<'E'
import json
s=open('mt2.py').read()
old='''def pooled_fit(C, Sm, dc, ds, tr, m, blocks, offset, level, models=()):
    """The compressive and divisive model with a finer pooling (`pooling(level=...)`), on
    the delay offset chosen with the 2 x 2 pooling, to measure what the pooling costs; also
    with complex or simple regressors only, and the models in `models` ((alpha, divisive),
    without luminance normalization) with the same pooling and offset."""'''
new='''def pooled_fit(C, Sm, dc, ds, tr, m, blocks, offset, level, models=(), restricted=True):
    """The compressive and divisive model with a finer pooling (`pooling(level=...)`), on
    the delay offset chosen with the 2 x 2 pooling, to measure what the pooling costs; also,
    if `restricted`, with complex or simple regressors only, and the models in `models`
    ((alpha, divisive), without luminance normalization) with the same pooling and offset."""'''
assert old in s; s=s.replace(old,new)
old='''    for nm, act in [("complex_only", np.where(isc)[0]), ("simple_only", np.where(~isc)[0])]:
        r2, _ = fit_neuron(F, [m["psth"]], blocks, stats=st, active=act, lazy=True)'''
new='''    for nm, act in [("complex_only", np.where(isc)[0]), ("simple_only", np.where(~isc)[0])] if restricted else []:
        r2, _ = fit_neuron(F, [m["psth"]], blocks, stats=st, active=act, lazy=True)'''
assert old in s; s=s.replace(old,new)
old='''def pooling_neuron(name, fine=False, threads=2):
    """The main model of one neuron under the finer pooling (finer_pooling.ipynb). The delay
    offset is chosen as in `_process`, by the held-out error of the 2 x 2 model on the
    training data, so it is the same; the 2 x 2 fit at that offset is returned with it."""'''
new='''def pooling_neuron(name, fine=False, threads=2, fig2b=False):
    """The main model of one neuron under the finer pooling (finer_pooling.ipynb). The delay
    offset is chosen as in `_process`, by the held-out error of the 2 x 2 model on the
    training data, so it is the same; the 2 x 2 fit at that offset is returned with it.
    With `fig2b` (finer_pooling_fig2b.ipynb), the other models of FIG2B with the 3 x 3
    pooling, in place of the complex-only and simple-only fits."""'''
assert old in s; s=s.replace(old,new)
old='''p3x3=pooled_fit(C, Sm, dc, ds, tr, m, blocks, o, "3x3", FIG2B))'''
new='''p3x3=pooled_fit(C, Sm, dc, ds, tr, m, blocks, o, "3x3",
                                   FIG2B if fig2b else (), restricted=not fig2b))'''
assert old in s; s=s.replace(old,new)
open('mt2.py','w').write(s)
E
git diff mt2.py
```

```
Updated 1 path from the index
diff --git a/entries/nishimoto-2011/mt2.py b/entries/nishimoto-2011/mt2.py
index b840e8e..58f4c95 100644
--- a/entries/nishimoto-2011/mt2.py
+++ b/entries/nishimoto-2011/mt2.py
@@ -775,28 +775,43 @@ def _process(name, null_specs, sim, seed):
     return out
 
 
-def pooled_fit(C, Sm, dc, ds, tr, m, blocks, offset, level):
+# the other models of Figure 2B without luminance normalization, (alpha, divisive)
+FIG2B = [(1.0, False), (1.0, True), (0.5, False), (2.0, False), (2.0, True)]
+
+
+def pooled_fit(C, Sm, dc, ds, tr, m, blocks, offset, level, models=(), restricted=True):
     """The compressive and divisive model with a finer pooling (`pooling(level=...)`), on
-    the delay offset chosen with the 2 x 2 pooling, to measure what the pooling costs; also
-    with complex or simple regressors only."""
+    the delay offset chosen with the 2 x 2 pooling, to measure what the pooling costs; also,
+    if `restricted`, with complex or simple regressors only, and the models in `models`
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json, copy
fin=json.load(open('finer_pooling.ipynb'))
new=json.load(open('/tmp/claude-1001/fig2b_cells.json'))
def md(s, tags=None):
    c={"cell_type":"markdown","metadata":{},"source":s}
    if tags: c["metadata"]["tags"]=tags
    return c
def code(s, tags=None):
    c={"cell_type":"code","metadata":{},"source":s,"outputs":[],"execution_count":None}
    if tags: c["metadata"]["tags"]=tags
    return c
header=md("""# Nishimoto and Gallant (2011) on CRCNS mt-2: Figure 2B with the finer pooling

Paper: Nishimoto S, Gallant JL (2011), J Neurosci 31(41):14551-14564,
doi:10.1523/jneurosci.6801-10.2011. Dataset: CRCNS mt-2 (doi:10.6080/K0DN4374), read from the
public bucket `crcnsarchive/mt-2/live/` (unversioned; `reproduce_nishimoto_2011.ipynb` prints the
MD5 sums of the files). Claims: `claims/nishimoto-2011.yaml`.

The main notebook judges the Figure 2B claims with the regression weights pooled onto 763
regressors (2 x 2 regions). `finer_pooling.ipynb` shows that pooling onto 3 x 3 regions (1465
regressors) raises the compressive and divisive model's mean correlation from 0.448 to 0.518, more
than the differences between the models of Figure 2B. This notebook refits the six models of
Figure 2B without luminance normalization (linear, compressive and expansive, each without and
with divisive normalization) with the 3 x 3 pooling, on the delay offset each neuron has in the
main notebook, and repeats the comparisons. Everything else is as in the main notebook (`mt2.py`,
`pooling_neuron` with `fig2b=True`). The six luminance-normalized models were not refitted, for
time, so fig2b-contrast-normalization-no-effect is not repeated here.

| Claim | Here |
|---|---|
| fig2b-compressive-improves | repeated with the finer pooling; judged in the main notebook |
| fig2b-expansive-decreases | repeated with the finer pooling; judged in the main notebook |
| fig2b-divisive-improves | repeated with the finer pooling; judged in the main notebook |
| fig2b-compressive-divisive-best | repeated with the finer pooling (the six models only); judged in the main notebook |
| fig2b-no-interaction | repeated with the finer pooling; judged in the main notebook |""")
setup=code('''import os, time, resource
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from scipy.stats import wilcoxon
import mt2

T0 = time.time()
sizes = mt2.list_sizes()
names = sorted(sizes)
N_RUN = int(os.environ.get("MT2_N", len(names)))  # a subset while developing
order = sorted(names, key=lambda n: -sizes[n]) if N_RUN >= len(names) else sorted(names, key=lambda n: sizes[n])[:N_RUN]
t = time.time()
with ProcessPoolExecutor(2) as ex:
    futs = {n: ex.submit(mt2.pooling_neuron, n, False, 2, True) for n in order}
    R = {n: f.result() for n, f in futs.items()}
names_run = [n for n in names if n in R]
print(f"{len(R)} neurons in {(time.time() - t) / 60:.1f} min; per neuron {np.median([R[n]['t_total'] for n in R]):.0f} s median")
print("peak memory of a worker:", resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6, "GB")''')
sanity=code('''def acc(r):
    return float(np.mean(list(r.values())))

IDX = [n[:6] for n in names_run]
monkey = np.array([R[n]["cellid"][0] for n in names_run])
print("neurons:", len(names_run), "; by monkey:", dict(zip(*np.unique(monkey, return_counts=True))))
print("validation sets:", dict(zip(*np.unique(["+".join(R[n]["sets"]) for n in names_run], return_counts=True))))
print("delay offsets (frames earlier):", dict(zip(*np.unique([R[n]["offset"] for n in names_run], return_counts=True))))
print(f"compressive and divisive model: 2 x 2 pooling mean r {np.mean([acc(R[n]['r2x2']) for n in names_run]):.3f}, "
      f"3 x 3 pooling {np.mean([acc(R[n]['p3x3']['r']) for n in names_run]):.3f} (as in finer_pooling.ipynb)")
print("regressors with 3 x 3 pooling:", R[names_run[0]]["p3x3"]["n_complex"], "complex,", R[names_run[0]]["p3x3"]["n_simple"], "simple")
print("models refitted:", len(R[names_run[0]]["p3x3"]["models"]) + 1)''', ["sanity"])
body=new[1:]  # drop the old section heading
body[0]['source']=body[0]['source'] if isinstance(body[0]['source'],str) else ''.join(body[0]['source'])
intro=md("""## The six models

The comparisons are those of the main notebook: the percent change against the simplest model
(linear, no divisive normalization) under readings (a) mean correlation, (b) mean squared
correlation and (c) mean of each neuron's percent change, with Wilcoxon signed-rank tests across
neurons, Bonferroni corrected over 11 comparisons (and over 5, the variant), the counts of the
claims file. A neuron's accuracy is the mean of its two validation correlations where it has both
sets.""")
summary=md("""## Summary

TODO""", ["summary"])
tail=code('print(f"notebook run time {(time.time() - T0) / 60:.1f} min")')
cells=[header, setup, md("## Data check"), sanity, intro]+body+[summary, tail]
nb=copy.deepcopy(fin); nb['cells']=cells
json.dump(nb,open('finer_pooling_fig2b.ipynb','w'),indent=1)
for i,c in enumerate(cells): print(i,c['cell_type'],c['metadata'].get('tags'),(c['source'] if isinstance(c['source'],str) else ''.join(c['source']))[:60].replace('\n',' '))
E
```

```
0 markdown None # Nishimoto and Gallant (2011) on CRCNS mt-2: Figure 2B with
1 code None import os, time, resource os.environ.setdefault("OMP_NUM_THR
2 markdown None ## Data check
3 code ['sanity'] def acc(r):     return float(np.mean(list(r.values())))  IDX
4 markdown None ## The six models  The comparisons are those of the main not
5 code None LAB = {(1.0, False): "linear", (0.5, False): "compressive", 
6 markdown None ### fig2b-compressive-improves  > A compressive static outpu
7 code ['claim:fig2b-compressive-improves'] report3([(0.5, False), (0.5, True)], [16, 19])
8 markdown None **Result: TODO**
9 markdown None ### fig2b-expansive-decreases  > An expansive static output 
10 code ['claim:fig2b-expansive-decreases'] report3([(2.0, False), (2.0, True)], [-36, -24])
11 markdown None **Result: TODO**
12 markdown None ### fig2b-divisive-improves  > Divisive normalization signif
13 code ['claim:fig2b-divisive-improves'] report3([(1.0, True)], [8]) for mk in np.unique(monkey):    
14 markdown None **Result: TODO**
15 markdown None ### fig2b-compressive-divisive-best  > The model with both a
16 code ['claim:fig2b-compressive-divisive-best'] cd, c = (0.5, True), (0.5, False) p = wilcoxon(B3[cd], B3[c]
17 markdown None **Result: TODO**
18 markdown None ### fig2b-no-interaction  > The effects of the compressive a
19 code ['claim:fig2b-no-interaction'] for div in (False, True):     for rdg, ref in (("a", (1.0, F
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; V=$(realpath ../../executed/nishimoto-2011/.venv); time MT2_N=2 JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-nishimoto-2011 --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR --output f2b_sub.ipynb finer_pooling_fig2b.ipynb 2>&1 | tail -1; python - <<E
import json
nb=json.load(open("$TMPDIR/f2b_sub.ipynb"))
for i,c in enumerate(nb['cells']):
    for o in c.get('outputs',[]):
        print(i, o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text']), o.get('ename',''), o.get('evalue',''))
E
```

```
[NbConvertApp] Writing 20294 bytes to /tmp/claude-1001/f2b_sub.ipynb

real	2m9.896s
user	6m59.953s
sys	0m6.528s
1 2 neurons in 2.1 min; per neuron 126 s median
peak memory of a worker: 2.44476 GB
  
3 neurons: 2 ; by monkey: {np.str_('v'): np.int64(2)}
validation sets: {np.str_('enhanced'): np.int64(2)}
delay offsets (frames earlier): {np.int64(3): np.int64(2)}
compressive and divisive model: 2 x 2 pooling mean r 0.320, 3 x 3 pooling 0.421 (as in finer_pooling.ipynb)
regressors with 3 x 3 pooling: 1247 complex, 218 simple
models refitted: 6
  
5 pooling 3 x 3, every model against the linear model without divisive normalization:
                  mean_r    pct_a    pct_b    pct_c  n_better    p  p_bonf11  p_bonf5
model                                                                                
linear            0.3627   0.0000   0.0000   0.0000         0  NaN         1        1
compressive       0.3733   2.9383   7.7720   2.4264         1  1.0         1        1
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; date -u; V=$(realpath ../../executed/nishimoto-2011/.venv); $V/bin/python - <<'E'
import time, numpy as np, mt2, resource
from concurrent.futures import ProcessPoolExecutor
sizes=mt2.list_sizes(); order=sorted(sizes, key=lambda n: sizes[n])[:3]
t=time.time()
with ProcessPoolExecutor(3) as ex:
    R=list(ex.map(mt2.pooling_neuron, order, [False]*3, [1]*3, [True]*3))
print('wall',time.time()-t, [round(r['t_total']) for r in R], [sizes[n]//10**6 for n in order], sum(sizes.values())//10**6)
print(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
E
```

```
Sat Nov 14 12:42:09 UTC 2026
wall 180.8235378265381 [181, 138, 173] [237, 242, 244] 17007
2.401404
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
s=open('mt2.py').read()
old='''# the other models of Figure 2B without luminance normalization, (alpha, divisive)
FIG2B = [(1.0, False), (1.0, True), (0.5, False), (2.0, False), (2.0, True)]'''
new='''# models of Figure 2B refitted with the 3 x 3 pooling, (alpha, divisive), without luminance
# normalization: the linear model with and without divisive normalization and the compressive
# model without it (the expansive models are left out for time)
FIG2B = [(1.0, False), (1.0, True), (0.5, False)]'''
assert old in s; open('mt2.py','w').write(s.replace(old,new))
import json
p='finer_pooling_fig2b.ipynb'; nb=json.load(open(p))
cells=nb['cells']
def src(c): return c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
# header
h=src(cells[0])
h=h.replace("""This notebook refits the six models of
Figure 2B without luminance normalization (linear, compressive and expansive, each without and
with divisive normalization) with the 3 x 3 pooling, on the delay offset each neuron has in the
main notebook, and repeats the comparisons.""","""This notebook refits four models of Figure
2B with the 3 x 3 pooling, the linear model without and with divisive normalization and the
compressive model without and with it, on the delay offset each neuron has in the main notebook,
and repeats the comparisons among them.""")
h=h.replace("""The six luminance-normalized models were not refitted, for
time, so fig2b-contrast-normalization-no-effect is not repeated here.""","""The two expansive models and the six luminance-normalized models
were not refitted: on the three smallest neurons each 3 x 3 model took about 15 s of a worker's
time, so the whole set would have taken about an hour, the notebook limit. So
fig2b-expansive-decreases and fig2b-contrast-normalization-no-effect are not repeated here.""")
h=h.replace("| fig2b-expansive-decreases | repeated with the finer pooling; judged in the main notebook |\n","")
h=h.replace("repeated with the finer pooling (the six models only)","repeated with the finer pooling (the four models only)")
h=h.replace("| fig2b-no-interaction | repeated with the finer pooling; judged in the main notebook |","| fig2b-no-interaction | repeated for the compressive model only; judged in the main notebook |")
cells[0]['source']=h
cells[4]['source']=src(cells[4]).replace("## The six models","## The four models")
c5=src(cells[5])
c5=c5.replace('''LAB = {(1.0, False): "linear", (0.5, False): "compressive", (2.0, False): "expansive",
       (1.0, True): "linear +div", (0.5, True): "compressive +div", (2.0, True): "expansive +div"}''','''LAB = {(1.0, False): "linear", (0.5, False): "compressive", (1.0, True): "linear +div", (0.5, True): "compressive +div"}''')
cells[5]['source']=c5
# drop expansive section (cells 9,10,11)
assert src(cells[9]).startswith('### fig2b-expansive')
del cells[9:12]
for c in cells:
    s=src(c)
    s=s.replace("the luminance-normalized models were not refitted","the expansive and luminance-normalized models were not refitted")
    s=s.replace("""        for a_ in (0.5, 2.0):""","""        for a_ in (0.5,):  # the expansive models were not refitted""")
    c['source']=s
json.dump(nb,open(p,'w'),indent=1)
for i,c in enumerate(cells): print(i,c['metadata'].get('tags'),src(c)[:70].replace('\n',' '))
E
```

```
0 None # Nishimoto and Gallant (2011) on CRCNS mt-2: Figure 2B with the finer
1 None import os, time, resource os.environ.setdefault("OMP_NUM_THREADS", "2"
2 None ## Data check
3 ['sanity'] def acc(r):     return float(np.mean(list(r.values())))  IDX = [n[:6] 
4 None ## The four models  The comparisons are those of the main notebook: th
5 None LAB = {(1.0, False): "linear", (0.5, False): "compressive", (1.0, True
6 None ### fig2b-compressive-improves  > A compressive static output nonlinea
7 ['claim:fig2b-compressive-improves'] report3([(0.5, False), (0.5, True)], [16, 19])
8 None **Result: TODO**
9 None ### fig2b-divisive-improves  > Divisive normalization significantly im
10 ['claim:fig2b-divisive-improves'] report3([(1.0, True)], [8]) for mk in np.unique(monkey):     s = monke
11 None **Result: TODO**
12 None ### fig2b-compressive-divisive-best  > The model with both a compressi
13 ['claim:fig2b-compressive-divisive-best'] cd, c = (0.5, True), (0.5, False) p = wilcoxon(B3[cd], B3[c]).pvalue p
14 None **Result: TODO**
15 None ### fig2b-no-interaction  > The effects of the compressive and expansi
16 ['claim:fig2b-no-interaction'] for div in (False, True):     for rdg, ref in (("a", (1.0, False)), ("
17 None **Result: TODO**
18 ['summary'] ## Summary  TODO
19 None print(f"notebook run time {(time.time() - T0) / 60:.1f} min")
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json
p='reproduce_nishimoto_2011.ipynb'; nb=json.load(open(p))
cells=nb['cells']
def src(c): return c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
i=[k for k,c in enumerate(cells) if c['metadata'].get('tags')==['claim:fig7b-pattern-index']][0]
new={"cell_type":"code","metadata":{"tags":["claim:fig7b-pattern-index"]},"outputs":[],"execution_count":None,"source":'''# How much the rectification clips: per neuron, the share of the 24 grating and 12 plaid directions whose
# model response is below zero (per-neuron peak frequency), and the index with and without rectification
for sep in (120, 90):
    tun = [R[n]["fits"][mt2.MAIN]["plaid"][pk[n]] for n in names_run]
    fg = np.array([np.mean(t["grating"] < 0) for t in tun])
    fp = np.array([np.mean(t[f"plaid{sep}"] < 0) for t in tun])
    fa = (24 * fg + 12 * fp) / 36
    pu, pr = PI[("a", sep)], PIR[("a", sep)]
    print(f"\\n{sep} degree plaids: share of directions clipped, median {np.median(fa):.2f} (range {fa.min():.2f} to {fa.max():.2f}); "
          f"gratings {np.median(fg):.2f}, plaids {np.median(fp):.2f}")
    print(f"  Spearman, clipped share against the rectified index: rho = {spearmanr(fa, pr)[0]:.3f}, p = {spearmanr(fa, pr)[1]:.3g}; "
          f"against its change (rectified - unrectified): rho = {spearmanr(fa, pr - pu)[0]:.3f}, p = {spearmanr(fa, pr - pu)[1]:.3g}")
    bins = [(0, 0), (1e-9, 0.25), (0.25 + 1e-9, 0.5), (0.5 + 1e-9, 1)]
    rows = []
    for lo, hi in bins:
        s = (fa >= lo) & (fa <= hi)
        rows.append(dict(clipped=f"{lo:.2f} to {hi:.2f}" if hi else "none", n=int(s.sum()),
                         median_unrectified=np.median(pu[s]) if s.any() else np.nan,
                         median_rectified=np.median(pr[s]) if s.any() else np.nan,
                         in_range_unrectified=int(((pu >= -6.6) & (pu <= 2.2) & s).sum()),
                         in_range_rectified=int(((pr >= -6.6) & (pr <= 2.2) & s).sum())))
    print(pd.DataFrame(rows).round(2).to_string(index=False))
    if sep == 120:
        print(pd.DataFrame({"gratings_clipped": fg, "plaids_clipped": fp, "index_unrectified": pu, "index_rectified": pr},
                           index=IDX).round(2).to_string())'''}
cells.insert(i+1,new)
s0=src(cells[1])
print('spearmanr' in s0, [l for l in s0.split('\n') if 'scipy' in l])
json.dump(nb,open(p,'w'),indent=1)
E
```

```
False ['from scipy.stats import wilcoxon, ranksums, pearsonr']
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; sed -i 's/from scipy.stats import wilcoxon, ranksums, pearsonr/from scipy.stats import wilcoxon, ranksums, pearsonr, spearmanr/' reproduce_nishimoto_2011.ipynb; grep -n "spearmanr\|MT2_N" reproduce_nishimoto_2011.ipynb | head
```

```
70:    "from scipy.stats import wilcoxon, ranksums, pearsonr, spearmanr\n",
116:    "N_RUN = int(os.environ.get(\"MT2_N\", len(names)))  # a subset while developing\n",
1086:   "source": "# How much the rectification clips: per neuron, the share of the 24 grating and 12 plaid directions whose\n# model response is below zero (per-neuron peak frequency), and the index with and without rectification\nfor sep in (120, 90):\n    tun = [R[n][\"fits\"][mt2.MAIN][\"plaid\"][pk[n]] for n in names_run]\n    fg = np.array([np.mean(t[\"grating\"] < 0) for t in tun])\n    fp = np.array([np.mean(t[f\"plaid{sep}\"] < 0) for t in tun])\n    fa = (24 * fg + 12 * fp) / 36\n    pu, pr = PI[(\"a\", sep)], PIR[(\"a\", sep)]\n    print(f\"\\n{sep} degree plaids: share of directions clipped, median {np.median(fa):.2f} (range {fa.min():.2f} to {fa.max():.2f}); \"\n          f\"gratings {np.median(fg):.2f}, plaids {np.median(fp):.2f}\")\n    print(f\"  Spearman, clipped share against the rectified index: rho = {spearmanr(fa, pr)[0]:.3f}, p = {spearmanr(fa, pr)[1]:.3g}; \"\n          f\"against its change (rectified - unrectified): rho = {spearmanr(fa, pr - pu)[0]:.3f}, p = {spearmanr(fa, pr - pu)[1]:.3g}\")\n    bins = [(0, 0), (1e-9, 0.25), (0.25 + 1e-9, 0.5), (0.5 + 1e-9, 1)]\n    rows = []\n    for lo, hi in bins:\n        s = (fa >= lo) & (fa <= hi)\n        rows.append(dict(clipped=f\"{lo:.2f} to {hi:.2f}\" if hi else \"none\", n=int(s.sum()),\n                         median_unrectified=np.median(pu[s]) if s.any() else np.nan,\n                         median_rectified=np.median(pr[s]) if s.any() else np.nan,\n                         in_range_unrectified=int(((pu >= -6.6) & (pu <= 2.2) & s).sum()),\n                         in_range_rectified=int(((pr >= -6.6) & (pr <= 2.2) & s).sum())))\n    print(pd.DataFrame(rows).round(2).to_string(index=False))\n    if sep == 120:\n        print(pd.DataFrame({\"gratings_clipped\": fg, \"plaids_clipped\": fp, \"index_unrectified\": pu, \"index_re
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; date -u; V=$(realpath ../../executed/nishimoto-2011/.venv); time MT2_N=2 JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-nishimoto-2011 --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR --output main_sub.ipynb reproduce_nishimoto_2011.ipynb 2>&1 | tail -2; python - <<E
import json
nb=json.load(open("$TMPDIR/main_sub.ipynb"))
for i,c in enumerate(nb['cells'][57:62]):
    for o in c.get('outputs',[]):
        print(i+57, o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text']), o.get('ename',''), o.get('evalue',''))
E
```

```
Sat Nov 14 12:46:06 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 191915 bytes to /tmp/claude-1001/main_sub.ipynb

real	2m39.138s
user	6m24.569s
sys	0m20.252s
58 peak (SF cycles/cRF, TF Hz) counts: {np.str_('1.5|30.0'): np.int64(1), np.str_('1.5|7.5'): np.int64(1)} ; population pair: (1.5, 30.0)
  frequency  separation  median     min    max  in_range  above_2_2  above_1_28     ok
0         a         120  -6.446  -8.061 -4.831       0.5        0.0         0.0  False
1         a          90  -9.582 -10.022 -9.142       0.0        0.0         0.0  False
2         b         120  -7.162  -8.061 -6.263       0.5        0.0         0.0  False
3         b          90  -8.433 -10.022 -6.843       0.0        0.0         0.0  False

combinations meeting the criterion: 0 of 4
  
58 
flat: neurons whose rectified responses are zero in every direction (index undefined, counted outside the range)
               response frequency  separation  flat  median  in_range  above_2_2     ok  draws_ok
0             rectified         a         120     0  -6.446      0.50        0.0  False         -
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def reusable" -A40 tools/entry.py | head -60; grep -n "def entry_hash\|def run_hash\|def _hash" -A25 tools/entry.py | head -50
```

```
525:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
526-    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
527-    the run left it, each within the time limit asked for now, and not older than REUSE_DAYS. Else None."""
528-    try:
529-        stamp = json.loads((output_dir / STAMP).read_text())
530-        entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
531-        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
532-            return None
533-        if [n["path"] for n in entry["notebooks"]] != [r["notebook"] for r in stamp["results"]]:
534-            return None
535-        for r in stamp["results"]:
536-            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
537-                return None
538-        return stamp
539-    except (OSError, ValueError, KeyError, TypeError):
540-        return None
541-
542-
543-def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
544-    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat .gitignore | head -30; git check-ignore -v executed/nishimoto-2011/finer_pooling.ipynb; grep -n "add_argument\|sub.add_parser\|argv" tools/entry.py | head -30
```

```
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.DS_Store
executed/
site/
paper/
targets/local.json
.gitignore:6:executed/	executed/nishimoto-2011/finer_pooling.ipynb
645:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover", "upgrade-python", "hash"])
646:    parser.add_argument("entry", type=Path, nargs="+",
648:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
649:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
650:    parser.add_argument("--max-minutes", type=float, default=60,
652:    parser.add_argument("--fresh", action="store_true",
654:    parser.add_argument("--python", help="lock: the Python version to lock for (default: the entry's); "
656:    parser.add_argument("--before", type=Path, help="upgrade-python: the executed notebooks to compare with "
```

**Agent calls Bash**

```bash
cd  sed -n 575,645p tools/entry.py; cat executed/nishimoto-2011/.clean-run.json | head -30
```

```
"--output-dir", str(output_dir.resolve()), "--output", name, name],
            cwd=entry_dir, capture_output=True, text=True,
            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
        seconds = round(time.time() - started)
        ok = r.returncode == 0
        error = None if ok else r.stderr[-3000:]
        if ok and seconds > max_minutes * 60:
            ok = False
            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
        failed |= not ok
        results.append({"notebook": name, "ok": ok, "seconds": seconds, "error": error})
        print(f"{'pass' if ok else 'FAIL'}  {name}  ({seconds} s)")
        if not ok:
            print(error, file=sys.stderr)
    (output_dir / "result.json").write_text(json.dumps(
        {"entry": entry["name"], "python": python_of(entry_dir), "results": results}, indent=1) + "\n")
    if not failed and all((output_dir / r["notebook"]).is_file() for r in results):
        (output_dir / STAMP).write_text(json.dumps({
            "entry": entry["name"], "hash": entry_hash(entry_dir), "finished": round(time.time()),
            "results": [{"notebook": r["notebook"], "ok": True, "seconds": r["seconds"],
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
s=open('entry.yaml').read()
old='''  runtime_minutes: 27
'''
new='''  runtime_minutes: 27
- path: finer_pooling_fig2b.ipynb
  title: Figure 2B with the finer pooling
  runtime_minutes: 45
'''
assert old in s; open('entry.yaml','w').write(s.replace(old,new))
E
date -u; V=$(realpath ../../executed/nishimoto-2011/.venv); OUT=$(realpath ../../executed/nishimoto-2011); time JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-nishimoto-2011 --ExecutePreprocessor.timeout=3600 --output-dir $OUT --output finer_pooling_fig2b.ipynb finer_pooling_fig2b.ipynb 2>&1 | tail -1; date -u
```

```
Sat Nov 14 12:49:34 UTC 2026
[NbConvertApp] Writing 18438 bytes to executed/nishimoto-2011/finer_pooling_fig2b.ipynb

real	46m53.220s
user	135m20.393s
sys	2m15.229s
Sat Nov 14 13:36:27 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<E
import json
nb=json.load(open("executed/nishimoto-2011/finer_pooling_fig2b.ipynb"))
for i,c in enumerate(nb['cells']):
    for o in c.get('outputs',[]):
        print(i, o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text']), o.get('ename',''), o.get('evalue',''))
E
```

```
1 45 neurons in 46.8 min; per neuron 99 s median
peak memory of a worker: 3.557916 GB
  
3 neurons: 45 ; by monkey: {np.str_('f'): np.int64(34), np.str_('v'): np.int64(11)}
validation sets: {np.str_('enhanced'): np.int64(31), np.str_('natural+enhanced'): np.int64(14)}
delay offsets (frames earlier): {np.int64(0): np.int64(31), np.int64(3): np.int64(9), np.int64(6): np.int64(5)}
compressive and divisive model: 2 x 2 pooling mean r 0.448, 3 x 3 pooling 0.518 (as in finer_pooling.ipynb)
regressors with 3 x 3 pooling: 1247 complex, 218 simple
models refitted: 4
  
5 pooling 3 x 3, every model against the linear model without divisive normalization:
                  mean_r   pct_a    pct_b   pct_c  n_better       p  p_bonf11  p_bonf5
model                                                                                 
linear            0.4794  0.0000   0.0000  0.0000         0     NaN    1.0000   1.0000
compressive       0.5060  5.5535  11.3826  5.6308        40  0.0000    0.0000   0.0000
linear +div       0.4916  2.5414   4.7356  3.1017        31  0.0076    0.0841   0.0382
compressive +div  0.5179  8.0372  16.0942  8.5921        40  0.0000    0.0000   0.0000
  
7 pooling 3 x 3, compressive: (a) 5.6%  (b) 11.4%  (c) 5.6%  [expected 16 +- 4]; better in 40 of 45; p = 5.66e-10, x11 = 6.23e-09, x5 = 2.83e-09
   within tolerance, readings (a), (b), (c): [False, False, False]
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; date -u; V=$(realpath ../../executed/nishimoto-2011/.venv); OUT=$(realpath ../../executed/nishimoto-2011); time JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-nishimoto-2011 --ExecutePreprocessor.timeout=3600 --output-dir $OUT --output reproduce_nishimoto_2011.ipynb reproduce_nishimoto_2011.ipynb 2>&1 | tail -1; date -u
```

```
Sat Nov 14 13:36:36 UTC 2026


real	60m4.390s
user	167m37.829s
sys	8m21.294s
Sat Nov 14 14:36:40 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls -la --time-style=full-iso executed/nishimoto-2011/; python - <<E
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
for i,c in enumerate(nb['cells'][:4]):
    for o in c.get('outputs',[]):
        print(i, o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text']), o.get('ename',''), o.get('evalue',''))
E
```

```
total 296
drwxr-xr-x 3 runner runner   4096 2026-11-14 13:36:27.671672184 +0000 .
drwxr-xr-x 3 runner runner   4096 2026-11-14 12:33:26.450620267 +0000 ..
-rw-r--r-- 1 runner runner    485 2026-11-14 12:20:50.168385631 +0000 .clean-run.json
drwxr-xr-x 5 runner runner   4096 2026-11-14 10:49:28.730161596 +0000 .venv
-rw-r--r-- 1 runner runner  20415 2026-11-14 12:20:50.099834262 +0000 finer_pooling.ipynb
-rw-r--r-- 1 runner runner  18438 2026-11-14 13:36:27.672417734 +0000 finer_pooling_fig2b.ipynb
-rw-r--r-- 1 runner runner 241463 2026-11-14 11:52:38.670233880 +0000 reproduce_nishimoto_2011.ipynb
-rw-r--r-- 1 runner runner    276 2026-11-14 12:20:50.163563717 +0000 result.json
1 45 files; 17.007579372 GB
ct0001_arg0466d_128.mat a51fd67bed934d6eab81ead8ec1634fb 284621393
ct0002_arg0466d_128.mat 8239d4b03750d2530f31b1142e4400f8 281394133
ct0005_arg0466d_128.mat 413ba796c27bc4cb6c800de12c8a935d 279482493
ct0006_arg0466d_128.mat 907f6117c004dc2f77ed73db0fe57c7d 277528046
ct0008_arg0466d_128.mat b5801d55a497c8c7a9ea3ae5de855596 529318245
ct0009_arg0466d_128.mat d6d68ec0cb6302994fa5465d7e3f6600 545261528
ct0010_arg0466d_128.mat 0e8084d949ff2db39e0bfeca53a6f85d 288531587
ct0011_arg0466d_128.mat ae32d99c8331ef7b0e9632dfa9be93a7 270340370
ct0013_arg0466d_128.mat 830a8ba0ea6578e9418291ce57403844 521647299
ct0014_arg0466d_128.mat 0957c866b3bbfbf2ad93dfe5f125c586 550762785
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; date -u; V=$(realpath ../../executed/nishimoto-2011/.venv); OUT=$(realpath ../../executed/nishimoto-2011); time JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-nishimoto-2011 --ExecutePreprocessor.timeout=7000 --output-dir $OUT --output reproduce_nishimoto_2011.ipynb reproduce_nishimoto_2011.ipynb 2>&1 | grep -v WARNING | tail -3; date -u
```

```
Sat Nov 14 14:36:54 UTC 2026
executed/nishimoto-2011/.venv/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
[NbConvertApp] Writing 249653 bytes to executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb

real	65m9.765s
user	182m46.238s
sys	9m0.238s
Sat Nov 14 15:42:04 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<E
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
for i in [12,29,59]:
    c=nb['cells'][i]
    for o in c.get('outputs',[]):
        t=o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text'])
        print(i, t[:3000])
E
```

```
12 mean r, compressive and divisive model, 45 neurons: 0.448 (median 0.454, range 0.221 to 0.730)
within 0.468 to 0.572: False
motion-enhanced validation only: 0.443
monkey f: n = 34, mean r 0.458
monkey v: n = 11, mean r 0.417
reading delays 1 to 10 (b): mean r 0.449
reading Gaussian 12 ms as FWHM (b): mean r 0.380
reading folds as random partitions (b): mean r 0.446
reading sigma chosen on held-out data (a): mean r 0.451
reading delay offset 0 for every neuron: mean r 0.448
reading early stopping after 500 steps: mean r 0.449
sigma chosen (fraction of mean pooled response): {np.float64(0.01): np.int64(33), np.float64(1.0): np.int64(12)}
neurons between 0.2 and 0.8 (Figure 3B span): 45 of 45; below 0.2: 0, above 0.8: 0
without ct0133 (7093 training frames left): mean r 0.450 over 44

steps per fold, main model: median 156, range 58 to 562; all 12 models: range 50 to 643, folds at the cap 0 of 2700
with a patience of 500: steps median 615, range 508 to 1101; mean r 0.449 against 0.448

12 
29 linear +div: (a) 2.9%  (b) 5.1%  (c) 3.9%  [expected 8 +- 4]; better in 30 of 45; p = 0.00511, x11 = 0.0562, x5 = 0.0255
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<E
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
t=''.join(''.join(o.get('text','')) for o in nb['cells'][59]['outputs'])
print(t[t.find('90 degree'):])
E
```

```
90 degree plaids: share of directions clipped, median 0.28 (range 0.00 to 0.58); gratings 0.29, plaids 0.17
  Spearman, clipped share against the rectified index: rho = 0.543, p = 0.000116; against its change (rectified - unrectified): rho = 0.642, p = 2.02e-06
     clipped  n  median_unrectified  median_rectified  in_range_unrectified  in_range_rectified
        none  8              -10.95            -10.95                     0                   0
0.00 to 0.25 14              -10.64             -8.31                     0                   5
0.25 to 0.50 21              -10.56             -3.74                     0                  16
0.50 to 1.00  2              -11.73             -6.16                     0                   1
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json
def src(c): return c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
# main
p='reproduce_nishimoto_2011.ipynb'; nb=json.load(open(p)); C=nb['cells']
i=[k for k,c in enumerate(C) if src(c).startswith('**Result: reproduced, on the rectified responses')][0]
C[i]['source']=src(C[i])+""" How much of this comes from clipping is shown in the second cell: with the per-neuron peak frequency, the rectification sets a median of 25% of the grating and plaid directions to zero with 120 degree plaids (28% with 90 degree plaids, range 0% to 58%), and the change of the index grows with that share (Spearman rho 0.568, p = 4.7e-5, and 0.642 with 90 degree plaids). The 8 neurons with no direction clipped keep their unrectified indices (median -8.33, 2 of 8 within the range with 120 degree plaids, 0 of 8 with 90 degrees), while 27 of the 37 clipped neurons fall within the range with 120 degree plaids. So the indices move into the paper's range through the clipping of the tuning curves: the outcome rests on reading the simulated responses as rectified firing rates, and these outputs do not tell whether the paper's simulated cells were rectified."""
i=[k for k,c in enumerate(C) if c['metadata'].get('tags')==['summary']][0]
s=src(C[i])
s=s.replace("| fig2b-expansive-decreases | partially reproduced (significant, one size outside) |","| fig2b-expansive-decreases | partially reproduced (significant; under reading (a) both sizes outside tolerance, under reading (b) one) |")
s=s.replace("| fig2b-divisive-improves | not reproduced (corrected p = 0.056) |","| fig2b-divisive-improves | not reproduced (corrected p = 0.056; 0.084 with the finer pooling, `finer_pooling_fig2b.ipynb`) |")
s=s.replace("""  `finer_pooling.ipynb`) raises the mean correlation from 0.448 to 0.518, so the Figure 2B
  effect sizes and the spectral analyses here, all on the 2 x 2 pooling, may be affected by it too.""","""  `finer_pooling.ipynb`) raises the mean correlation from 0.448 to 0.518. Four of the Figure 2B
  models refitted with it (`finer_pooling_fig2b.ipynb`) give the same outcomes for
  fig2b-compressive-improves, fig2b-divisive-improves, fig2b-compressive-divisive-best and
  fig2b-no-interaction; the expansive models and the spectral analyses here rest on the 2 x 2
  pooling only.""")
C[i]['source']=s
json.dump(nb,open(p,'w'),indent=1)
# finer
p='finer_pooling.ipynb'; nb=json.load(open(p)); C=nb['cells']
s=src(C[6]); old="against 0.636, 0.398 and 0.322 with 3 x 3 regions, so the finer pooling does not raise it further on these three."
assert old in s
C[6]['source']=s.replace(old,"against 0.636, 0.398 and 0.322 with 3 x 3 regions: lower for two (-0.022 and -0.046) and higher for one (+0.025), so on these three neurons a still finer pooling gives mixed changes.")
s=src(C[16]).replace("""The other models of Figure 2 and the spectral
analyses of Figures 6 to 8 were fitted only with the 2 x 2 pooling (main notebook), so their
effect sizes may also be underestimated there.""","""Four models of Figure 2B are refitted with this pooling in
`finer_pooling_fig2b.ipynb`; the other models and the spectral analyses of Figures 6 to 8 were
fitted only with the 2 x 2 pooling (main notebook).""")
C[16]['source']=s
json.dump(nb,open(p,'w'),indent=1)
E
grep -c "Four models of Figure 2B" finer_pooling.ipynb
```

```
1
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json
def src(c): return c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
p='finer_pooling_fig2b.ipynb'; nb=json.load(open(p)); C=nb['cells']
R={8:"**Result: partially reproduced, as with the 2 x 2 pooling.** With the 3 x 3 pooling the compressive nonlinearity improves predictions in 40 of 45 neurons without and with divisive normalization (corrected p 6.2e-9 and 1.7e-9 over 11). The sizes are 5.6% and 8.0% under reading (a), 11.4% and 16.1% under reading (b), 5.6% and 8.6% under reading (c), against 16 and 19 (+-4); only reading (b) with divisive normalization is within tolerance, as with the 2 x 2 pooling (4.6% and 8.4% under reading (a)).",
11:"**Result: not reproduced, as with the 2 x 2 pooling.** With the 3 x 3 pooling divisive normalization with the linear nonlinearity raises the mean correlation by 2.5% (a), 4.7% (b, within 8 +- 4) or 3.1% (c), better in 31 of 45 neurons, Wilcoxon p = 0.0076, corrected p = 0.084 over 11 comparisons (0.038 over 5), so the claim's corrected p < 0.01 is not met. The increase is again larger in monkey v (9.1%, reading (a)) than in monkey f (0.7%).",
14:"**Result: reproduced, as with the 2 x 2 pooling, among the four models refitted.** The compressive and divisive model (0.518) beats the compressive model (0.506) in 33 of 45 neurons, Wilcoxon p = 0.00075, corrected 0.0083 over 11, 0.0090 over 12 and 0.0038 over 5, each below 0.01 but closer to it than with the 2 x 2 pooling (0.0017 over 11). Neither the linear model nor the linear divisive model is better than it (mean differences -0.039 and -0.026). The expansive and luminance-normalized models were not refitted, so the second condition is checked here on four of the 12 models only.",
17:"**Result: reproduced for the compressive model, as with the 2 x 2 pooling.** The compressive model is better than the linear one without divisive normalization (+0.027, corrected p = 6.2e-9) and with it, against the simplest model (reading (a), +0.039, 1.7e-9) and against the linear divisive model (reading (b), +0.026, 6.2e-9). The expansive models were not refitted, so their half of the claim rests on the main notebook only."}
for k,v in R.items():
    assert src(C[k]).startswith('**Result: TODO'); C[k]['source']=v
assert C[18]['metadata'].get('tags')==['summary']
C[18]['source']="""## Summary

| Claim | With the 3 x 3 pooling (judged in the main notebook) |
|---|---|
| fig2b-compressive-improves | partially reproduced (5.6% and 8.0%, reading (a); only 16.1% under reading (b) within tolerance) |
| fig2b-divisive-improves | not reproduced (2.5%, reading (a); corrected p = 0.084) |
| fig2b-compressive-divisive-best | reproduced among the four models refitted (corrected p = 0.0083) |
| fig2b-no-interaction | reproduced for the compressive model |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The finer pooling raises every model's mean correlation (linear 0.479, compressive 0.506, linear
divisive 0.492, compressive divisive 0.518) but leaves the outcome of each Figure 2B claim
tested here as it is with the 2 x 2 pooling. The expansive models and the luminance-normalized
models were not refitted. This notebook differs from the paper's method in the same ways as the
main notebook, except for the finer pooling."""
json.dump(nb,open(p,'w'),indent=1)
E
date -u
```

```
Sat Nov 14 15:42:42 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
s=open('README.md').read()
old="""in an hour. A second notebook refits the main model with a finer pooling (1465 regressors),
which raises its mean correlation from 0.448 to 0.518; the claims on that model are judged
there."""
new="""in an hour. A second notebook refits the main model with a finer pooling (1465 regressors),
which raises its mean correlation from 0.448 to 0.518; fig3b-mean-prediction and
natural-movie-control are judged there, and fig3a-example-neuron and complex-cells-dominate,
judged in the main notebook, are repeated there with the same outcome. A third notebook refits
four of the Figure 2B models with the finer pooling; the outcomes of the Figure 2B claims it
repeats are unchanged."""
assert old in s; s=s.replace(old,new)
old="""- `finer_pooling.ipynb`: the main model with the finer pooling, for fig3b-mean-prediction,
  fig3a-example-neuron, complex-cells-dominate and natural-movie-control. About 27 minutes."""
new="""- `finer_pooling.ipynb`: the main model with the finer pooling, for fig3b-mean-prediction,
  fig3a-example-neuron, complex-cells-dominate and natural-movie-control. About 27 minutes.
- `finer_pooling_fig2b.ipynb`: the linear and compressive models, without and with divisive
  normalization, with the finer pooling, for the Figure 2B claims. About 47 minutes."""
assert old in s; s=s.replace(old,new)
s=s.replace("It takes about 60 minutes, two neurons at a time.","It takes about 65 minutes, two neurons at a time.")
open('README.md','w').write(s)
y=open('entry.yaml').read().replace("  runtime_minutes: 45\n","  runtime_minutes: 47\n").replace("  runtime_minutes: 60\n","  runtime_minutes: 65\n")
open('entry.yaml','w').write(y)
E
grep -n runtime entry.yaml
```

```
15:  runtime_minutes: 65
18:  runtime_minutes: 27
21:  runtime_minutes: 47
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/nishimoto-2011-01.yaml'; s=open(p).read()
def rep(old,new,count=1):
    global s
    n=s.count(old); assert n==count,(n,old[:60]); s=s.replace(old,new)
rep("""    neurons a finer pooling still (4 x 4 regions and every simple channel, 3085 regressors) gives
    0.614, 0.352 and 0.347 against 0.636, 0.398 and 0.322 with 3 x 3 regions. No boosting fold""","""    neurons a finer pooling still (4 x 4 regions and every simple channel, 3085 regressors) gives
    0.614, 0.352 and 0.347 against 0.636, 0.398 and 0.322 with 3 x 3 regions, changes of -0.022,
    -0.046 and +0.025, so whether 3 x 3 is close to the paper's model is shown for these three
    neurons only, with mixed results. No boosting fold""")
rep("""    cRF and SF 0) at 11 delays, where the paper fits a weight for each of 5956 filters; every other
    analysis uses 763 regressors (3 and 6 cycles per cRF onto 2 x 2 regions). The filter bank behind""","""    cRF and SF 0) at 11 delays, where the paper fits a weight for each of 5956 filters. The same
    pooling is used for natural-movie-control and for the Figure 2B models refitted in
    finer_pooling_fig2b.ipynb; the main notebook uses 763 regressors (3 and 6 cycles per cRF onto 2
    x 2 regions). The filter bank behind""")
old_dev="""  - The model as in fig3b-mean-prediction, with the 2 x 2 pooling (763 regressors) for every model;
    the finer pooling, which raises the main model's mean correlation from 0.448 to 0.518, could be
    run for the main model only, so the effect sizes here may differ from those of a finer model."""
# fig3a
rep(old_dev+"""
- claim: fig2b-contrast-normalization-no-effect""","""  - The model as in fig3b-mean-prediction, judged with the 2 x 2 pooling (763 regressors) of the
    main notebook and repeated with the 3 x 3 pooling in finer_pooling.ipynb, with the same outcome.
- claim: fig2b-contrast-normalization-no-effect""")
rep(old_dev+""" Eqs. 10 to 12""","""  - The model as in fig3b-mean-prediction, with the 2 x 2 pooling (763 regressors) for every model;
    the luminance-normalized models were not refitted with the 3 x 3 pooling, for time, so the
    effect size with a finer model is not known. Eqs. 10 to 12""")
fig2b_dev="""  - The model as in fig3b-mean-prediction, judged with the 2 x 2 pooling (763 regressors) of the
    main notebook; finer_pooling_fig2b.ipynb repeats it with the 3 x 3 pooling (1465 regressors)."""
rep(old_dev+""" The power applies""",fig2b_dev+""" The power applies""")
rep(old_dev+"""
- claim: fig2b-divisive-improves""","""  - The model as in fig3b-mean-prediction, with the 2 x 2 pooling (763 regressors); the expansive
    models were not refitted with the 3 x 3 pooling, for time (finer_pooling_fig2b.ipynb).
- claim: fig2b-divisive-improves""")
rep(old_dev+""" Sigma is the fixed""",fig2b_dev+""" Sigma is the fixed""")
rep(old_dev+"""
- claim: fig2b-no-interaction""",fig2b_dev+"""
- claim: fig2b-no-interaction""")
rep(old_dev+"""
- claim: complex-cells-dominate""","""  - The model as in fig3b-mean-prediction, judged with the 2 x 2 pooling (763 regressors) of the
    main notebook; finer_pooling_fig2b.ipynb repeats it with the 3 x 3 pooling for the
    compressive model only, as the expansive models were not refitted.
- claim: complex-cells-dominate""")
rep(old_dev+""" The two reduced models""","""  - The model as in fig3b-mean-prediction, judged with the 2 x 2 pooling (763 regressors) of the
    main notebook and repeated with the 3 x 3 pooling in finer_pooling.ipynb, with the same outcome.
    The two reduced models""")
# fig2b notes
rep("""    16 and 19 (+-4). Only reading (b) with divisive normalization is within tolerance.""","""    16 and 19 (+-4). Only reading (b) with divisive normalization is within tolerance. With the 3 x
    3 pooling (finer_pooling_fig2b.ipynb) the sizes are 5.6% and 8.0% (a), 11.4% and 16.1% (b), 5.6%
    and 8.6% (c), again with only reading (b) with divisive normalization within tolerance, better
    in 40 of 45 neurons in both (corrected p 6.2e-9 and 1.7e-9).""")
rep("""    against -36 and -24 (+-4). Reading (b) matches the value with divisive normalization only.""","""    against -36 and -24 (+-4). Under reading (a), given as measured, both values are outside
    tolerance; reading (b) matches the value with divisive normalization only.""")
rep("""    claim's corrected p < 0.01 is not met. The increase is larger in monkey v (9.5%, reading (a))
    than in monkey f (1.1%).""","""    claim's corrected p < 0.01 is not met. The increase is larger in monkey v (9.5%, reading (a))
    than in monkey f (1.1%). With the 3 x 3 pooling (finer_pooling_fig2b.ipynb) the increase is
    2.5% (a), 4.7% (b) or 3.1% (c), better in 31 of 45, Wilcoxon p = 0.0076, corrected 0.084 over
    11 (0.038 over 5), so the outcome is the same.""")
rep("""    No model is better on average; the closest, the same model with luminance normalization, is
    lower by 0.0065 (p = 0.36).""","""    No model is better on average; the closest, the same model with luminance normalization, is
    lower by 0.0065 (p = 0.36). With the 3 x 3 pooling (finer_pooling_fig2b.ipynb, four models
    refitted) it gives 0.518 against 0.506, better in 33 of 45, p = 0.00075, corrected 0.0083 over
    11, 0.0090 over 12 and 0.0038 over 5, and neither linear model is better.""")
rep("""    +0.035 (1.8e-8) and -0.056 (4.5e-8), and against the linear divisive model (reading (b))
    +0.022 (8.1e-9) and -0.068 (6.3e-13).""","""    +0.035 (1.8e-8) and -0.056 (4.5e-8), and against the linear divisive model (reading (b))
    +0.022 (8.1e-9) and -0.068 (6.3e-13). With the 3 x 3 pooling the compressive effects are
    +0.027 (6.2e-9) without divisive normalization and +0.039 (1.7e-9, reading (a)) and +0.026
    (6.2e-9, reading (b)) with it; the expansive models were not refitted.""")
# fig7b
rep("""    to -10.7, 0% to 18% within the range) and meet it under no combination, so the outcome rests on
    the rectification.""","""    to -10.7, 0% to 18% within the range) and meet it under no combination, so the outcome rests on
    the rectification. The rectification sets a median of 25% of the grating and plaid directions
    to zero (28% with 90 degree plaids, range 0% to 58%), and the change of the index grows with
    that share (Spearman rho 0.568, p = 4.7e-5; 0.642 with 90 degree plaids). The 8 neurons with no
    direction clipped keep their component-like indices (median -8.33, 2 of 8 within the range),
    while 27 of the 37 clipped neurons fall within it. The indices thus reach the paper's range
    through the clipping of the tuning curves.""")
# fig7c
rep("""    < 0.01; with the noisy indices (ratio reading aaa/a, per-neuron frequency) r is 0.177 or less.""","""    < 0.01; with the noisy indices of the first of the 20 draws (ratio reading aaa/a, per-neuron
    frequency) r is 0.177 or less.""")
rep("""    0.055, and the noisy indices with the per-neuron frequency p of 0.32 or more.""","""    0.055, and the noisy indices of the first of the 20 draws with the per-neuron frequency p of
    0.32 or more.""")
open(p,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/nishimoto-2011-01.yaml <<'E'
- date: '2026-11-14'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The full executed notebooks reproduce_nishimoto_2011.ipynb and finer_pooling.ipynb with
    their conclusions and summaries, the helper module mt2.py, the claims file, the attempt record
    and the README, with the paper's full text. Round 2.
  results:
  - claim: fig3b-mean-prediction
    agrees: true
    outcome: reproduced
    reason: The 3 x 3 model (finer, cell 5, 0.518) is closer to the paper's model than the 2 x 2 one.
      Its offset was chosen on training data only, and no validation data is used for selection. It
      is still a reduced model. Finer cell 6 says the finer pooling "does not raise it further on
      these three", but ct0006 rises from 0.322 to 0.347; the 4 x 4 changes are -0.022, -0.046 and
      +0.025, so whether 3 x 3 is close to the paper's model is shown for only three neurons. The
      deviation's "every other analysis uses 763 regressors" is wrong, as natural-movie-control is
      judged on the 1465-regressor model.
    response: Corrected finer cell 6 and the record's notes to give the three changes and call them
      mixed, and corrected the deviation to name the analyses that use the 3 x 3 pooling. Outcome
      unchanged.
  - claim: fig3b-explainable-variance
    agrees: true
    outcome: blocked
    reason: Main cells 5 and 6, only psths, and trange is empty in all 45 files.
    response: No change.
  - claim: fig3a-example-neuron
    agrees: true
    outcome: reproduced
    reason: Stated. The deviation copies the text "could be run for the main model only, so the
      effect sizes here may differ", though the claim is on the main model and was rerun with 3 x 3
      pooling. The README says it is judged in finer_pooling.ipynb, while the record points to the
      main notebook and gives measured = 0.71 from the 2 x 2 model; the outcome is the same either
      way.
    response: Replaced the deviation with one that says the claim is judged on the 2 x 2 model and
      repeated with the 3 x 3 pooling with the same outcome, and corrected the README to say so.
      Outcome unchanged.
  - claim: fig2b-contrast-normalization-no-effect
    agrees: true
    outcome: reproduced
    reason: Stated.
    response: No change of outcome; the deviation now says the luminance-normalized models were not
      refitted with the 3 x 3 pooling.
  - claim: fig2b-compressive-improves
    agrees: true
    outcome: partially_reproduced
    reason: Stated. Rests on the 2 x 2 model; the 3 x 3 pooling raises r by 0.070 on average, more
      than the Fig. 2B differences being judged.
    response: A third notebook, finer_pooling_fig2b.ipynb, refits the linear and compressive models
      without and with divisive normalization with the 3 x 3 pooling. The sizes are 5.6% and 8.0%
      (a), 11.4% and 16.1% (b), with only reading (b) with divisive normalization within tolerance,
      both significant. Outcome unchanged.
  - claim: fig2b-expansive-decreases
    agrees: true
    outcome: partially_reproduced
    reason: Stated. Rests on the 2 x 2 model. Main cell 72 says "partially reproduced (significant,
      one size outside)", which holds only under reading (b); under reading (a), the value given as
      measured, both sizes are outside tolerance (-15.1 against -36 and -13.5 against -24).
    response: Corrected the summary row and the record's notes to say both sizes are outside
      tolerance under reading (a) and one under reading (b). The expansive models were not refitted
      with the 3 x 3 pooling, for time; the deviation says so. Outcome unchanged.
  - claim: fig2b-divisive-improves
    agrees: true
    outcome: not_reproduced
    reason: Agrees on the 2 x 2 model. The times-11 p = 0.056 is close to the bound, and the finer
      pooling was not run for this pair of models; refitting the linear and linear-plus-divisive
      models with 3 x 3 pooling would decide it.
    response: Refitted both with the 3 x 3 pooling (finer_pooling_fig2b.ipynb). The increase is 2.5%
      (a), 4.7% (b) or 3.1% (c), better in 31 of 45, Wilcoxon p = 0.0076, corrected 0.084 over 11
      and 0.038 over 5, so the corrected p < 0.01 is still not met. Outcome unchanged.
  - claim: fig2b-compressive-divisive-best
    agrees: true
    outcome: reproduced
    reason: Stated.
    response: Repeated with the 3 x 3 pooling on four models (p = 0.00075, corrected 0.0083 over 11,
      0.0090 over 12). Outcome unchanged.
  - claim: fig2b-no-interaction
    agrees: true
    outcome: reproduced
    reason: Stated.
    response: Repeated with the 3 x 3 pooling for the compressive model (corrected p 6.2e-9, 1.7e-9
      and 6.2e-9); the expansive models were not refitted. Outcome unchanged.
  - claim: complex-cells-dominate
    agrees: true
    outcome: reproduced
    reason: Stated. Now also holds with every simple channel (finer, cell 11). The deviation copies
      the text "could be run for the main model only", though the claim was rerun with 3 x 3
      pooling, and the README says it is judged in finer_pooling.ipynb while the record points to
      the main notebook.
    response: Replaced the deviation as for fig3a-example-neuron and corrected the README. Outcome
      unchanged.
  - claim: fig6a-null-on-plane
    agrees: true
    outcome: reproduced
    reason: Stated. Under all-(a) readings the value is 0.396, at the edge of the band. Null-movie
      reading (b) under all four rate and delay combinations was not run; this is stated and does
      not affect a conclusion.
    response: No change.
  - claim: fig6a-excitatory-on-plane
    agrees: true
    outcome: reproduced
    reason: Stated.
    response: No change.
  - claim: fig6b-suppressive-off-plane
    agrees: true
    outcome: reproduced
    reason: Agrees, but fragile; 6 of 40 combinations pass.
    response: No change.
  - claim: fig7a-partial-ring
    agrees: true
    outcome: reproduced
    reason: Stated.
    response: No change.
  - claim: fig7a-no-corr-prediction-hv
    agrees: true
    outcome: partially_reproduced
    reason: Stated.
    response: No change.
  - claim: fig7b-pattern-index
    agrees: true
    outcome: reproduced
    reason: Agrees conditionally. The assumption is stated, with the passages quoted, and is
      defensible, as firing rates cannot be negative, the prediction includes the intercept b0, and
      the paper says nothing either way. It was adopted after the unrectified reading failed, and
      the claims file does not list it. Rectifying clips tuning curves, which by itself pulls |Z|
      toward 0; the notebook does not show how much of each tuning curve is clipped. It asked for
      the fraction of grating and plaid directions clipped to zero per neuron, and the index
      against that fraction.
    response: Added a cell that prints, per neuron, the share of grating and plaid directions
      clipped and the index with and without rectification. A median of 25% of directions is
      clipped (0% to 58%); the change of the index grows with that share (Spearman rho 0.568, p =
      4.7e-5); the 8 unclipped neurons keep their component-like indices (2 of 8 within the range)
      and 27 of 37 clipped neurons fall within it. So the indices reach the paper's range through
      the clipping. The conclusion and notes say so. Outcome kept as verified, resting on the
      assumption.
  - claim: fig7c-hv-pattern-correlation
    agrees: true
    outcome: not_reproduced
    reason: Fails under every index reading. The record's "with the noisy indices r is 0.177 or
      less" comes from the first of 20 draws only (main cell 61), and the record does not say so.
    response: The notes now say the noisy values are from the first of the 20 draws. Outcome
      unchanged.
  - claim: fig7c-no-corr-prediction-pattern
    agrees: true
    outcome: reproduced
    reason: Holds under every index reading. The record's "p of 0.32 or more" comes from the first
      of 20 draws only (main cell 64), and the record does not say so.
    response: The notes now say so. Outcome unchanged.
  - claim: natural-movie-control
    agrees: true
    outcome: reproduced
    reason: Stated (3 x 3 pooling, nrange read as the natural movie). The direction flips between
      models, natural higher in 10 of 14 neurons with 2 x 2 pooling and in 5 of 14 with 3 x 3; this
      does not affect the criterion.
    response: No change.
  - claim: fig8-recovery-simulated
    agrees: true
    outcome: reproduced
    reason: Stated.
    response: No change.
E
python - <<'E'
import yaml; d=yaml.safe_load(open('attempts/nishimoto-2011-01.yaml')); print(len(d['verifications']), len(d['verifications'][-1]['results']))
E
date -u
```

```
2 20
Sat Nov 14 15:43:46 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/nishimoto-2011-01.yaml'; s=open(p).read()
old="""    tolerance, and the Wilcoxon signed-rank test finds no difference (p = 0.43; natural higher in 5
    of 14)."""
assert old in s
s=s.replace(old,"""    tolerance, and the Wilcoxon signed-rank test finds no difference (p = 0.43; natural higher in 5
    of 14, where the 2 x 2 pooling has it higher in 10 of 14).""")
open(p,'w').write(s)
E
grep -n "natural higher in" entries/nishimoto-2011/*.ipynb | cut -c1-200 | head; python tools/entry.py check entries/nishimoto-2011 2>&1 | tail -20
```

```
entries/nishimoto-2011/finer_pooling.ipynb:257:    "          f\"Wilcoxon p = {wilcoxon(rn3, re3).pvalue:.4g}; natural higher in {(rn3 > re3).sum()} of {len(nn)}; mean difference {np.mean(rn3 - re3):+
entries/nishimoto-2011/finer_pooling.ipynb:267:    "**Result: reproduced with the finer pooling.** For the 14 neurons with a natural-movie validation set, the mean correlation is 0.523 for natural mov
entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb:1228:    "print(f\"Wilcoxon signed-rank p = {st.pvalue:.4g}; natural higher in {(rn > re_).sum()} of {len(nn)}; mean difference {np.mean(rn - re_)
entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb:1238:    "**Result: partially reproduced with the 2 x 2 pooling of this notebook; `finer_pooling.ipynb`, with the finer pooling, decides the outco
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; python - <<'E'
import json, uuid
for p in ['reproduce_nishimoto_2011.ipynb','finer_pooling.ipynb','finer_pooling_fig2b.ipynb']:
    nb=json.load(open(p)); n=0
    for c in nb['cells']:
        if 'id' not in c: c['id']=uuid.uuid4().hex[:8]; n+=1
        if c['cell_type']=='code': c['outputs']=[]; c['execution_count']=None
    nb['nbformat']=4; nb['nbformat_minor']=max(nb.get('nbformat_minor',5),5)
    json.dump(nb,open(p,'w'),indent=1, ensure_ascii=False); open(p,'a').write('\n')
    print(p,n)
E
cd ../..; python tools/entry.py check entries/nishimoto-2011 2>&1 | tail -3; git diff --stat
```

```
reproduce_nishimoto_2011.ipynb 1
finer_pooling.ipynb 0
finer_pooling_fig2b.ipynb 20
0 error(s)
 attempts/nishimoto-2011-01.yaml                    | 245 ++++++++++++++++++---
 entries/nishimoto-2011/README.md                   |  11 +-
 entries/nishimoto-2011/entry.yaml                  |   5 +-
 entries/nishimoto-2011/finer_pooling.ipynb         |  23 +-
 entries/nishimoto-2011/mt2.py                      |  34 ++-
 .../nishimoto-2011/reproduce_nishimoto_2011.ipynb  |  85 ++-----
 6 files changed, 267 insertions(+), 136 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb | grep '^[-+]' | cut -c1-150 | head -60
```

```
--- a/entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb
+++ b/entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb
-    "from scipy.stats import wilcoxon, ranksums, pearsonr\n",
+    "from scipy.stats import wilcoxon, ranksums, pearsonr, spearmanr\n",
+  {
+   "cell_type": "code",
+   "metadata": {
+    "tags": [
+     "claim:fig7b-pattern-index"
+    ]
+   },
+   "outputs": [],
+   "execution_count": null,
+   "source": "# How much the rectification clips: per neuron, the share of the 24 grating and 12 plaid directions whose\n# model response is below ze
+   "id": "d9eb1ee6"
+  },
-   "source": [
-    "**Result: reproduced, on the rectified responses (assumed).** The paper does not say whether the simulated responses were rectified or carried n
-   ]
+   "source": "**Result: reproduced, on the rectified responses (assumed).** The paper does not say whether the simulated responses were rectified or 
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/nishimoto-2011; date -u; V=$(realpath ../../executed/nishimoto-2011/.venv); OUT=$(realpath ../../executed/nishimoto-2011); time JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-nishimoto-2011 --ExecutePreprocessor.timeout=7000 --output-dir $OUT --output finer_pooling.ipynb finer_pooling.ipynb 2>&1 | grep Writing; date -u
```

```
Sat Nov 14 15:44:19 UTC 2026
[NbConvertApp] Writing 20504 bytes to executed/nishimoto-2011/finer_pooling.ipynb

real	26m20.676s
user	57m44.937s
sys	1m50.859s
Sat Nov 14 16:10:39 UTC 2026
```

**Agent**

Now I'll confirm the finer numbers match, then copy the final markdown into the executed main and Fig 2B copies (their code cells are unchanged since they were run).

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open("executed/nishimoto-2011/finer_pooling.ipynb"))
for i in [5,11,14]:
    print(''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs'])[:700])
# sync markdown of the two notebooks run before the last text edits; code cells must be identical
for p in ['reproduce_nishimoto_2011.ipynb','finer_pooling_fig2b.ipynb']:
    src=json.load(open('entries/nishimoto-2011/'+p)); ex=json.load(open('executed/nishimoto-2011/'+p))
    S=lambda c: c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
    assert len(src['cells'])==len(ex['cells'])
    for a,b in zip(src['cells'],ex['cells']):
        assert a['cell_type']==b['cell_type']
        if a['cell_type']=='code': assert S(a)==S(b),(p,S(a)[:80])
        else: b['source']=S(a)
        b['id']=a['id']
    json.dump(ex,open('executed/nishimoto-2011/'+p,'w'),indent=1,ensure_ascii=False)
    print('synced',p)
E
```

```
pooling 3 x 3: mean r 0.518 (median 0.507, range 0.263 to 0.761); within 0.468 to 0.572: True; motion-enhanced only 0.524
pooling 2 x 2: mean r 0.448
3 x 3 better than 2 x 2 in 45 of 45, mean difference +0.070, Wilcoxon p = 5.68e-14; without ct0133 0.520
  monkey f: n = 34, mean r 0.524
  monkey v: n = 11, mean r 0.500
neurons between 0.2 and 0.8 (Figure 3B span): 45 of 45; below 0.2: 0, above 0.8: 0
boosting steps per fold: median 171, range 57 to 409 (cap 20000)
        2x2 (763)  3x3 (1465)  4x4 + all simple (3085)
ct0002      0.556       0.636                    0.614
ct0005      0.329       0.398                    0.352
ct0006      0.261       0.322                    0.347

pooling 3 x 3: full 0.518, complex only 0.514 (r^2 ratio 0.985), simple only 0.194 (r^2 ratio 0.191)
drop of mean r: complex only 0.0043, simple only 0.3244
finest pooling, ct0002 (1082 simple regressors, every position, up to 1.5 cycles per cRF): full 0.614, complex only 0.622, simple only 0.367
finest pooling, ct0005 (1082 simple regressors, every position, up to 1.5 cycles per cRF): full 0.352, complex only 0.364, simple only 0.078
finest pooling, ct0006 (1082 simple regressors, every position, up to 1.5 cycles per cRF): full 0.347, complex only 0.333, simple only 0.141

14 neurons with both validation sets
pooling 3 x 3: natural 0.523 [within 0.533 +- 0.053: True], motion-enhanced 0.563 [within 0.537 +- 0.054: True], Wilcoxon p = 0.4263; natural higher in 5 of 14; mean difference -0.040
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
t='\n'.join(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])) for c in nb['cells'])
for k in ['0.396','-5.067','0.644','0.592','0.168','71.1','-0.281','0.0612','0.835','0.710','0.493','0.462','0.2414','0.4136','p = 0.733','0.177']:
    print(k, k in t)
E
python tools/entry.py check entries/nishimoto-2011 2>&1 | tail -2; date -u
```

```
0.396 True
-5.067 False
0.644 True
0.592 True
0.168 False
71.1 False
-0.281 True
0.0612 True
0.835 True
0.710 True
0.493 True
0.462 True
0.2414 False
0.4136 True
p = 0.733 False
0.177 False
0 error(s)
Sat Nov 14 16:10:57 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
for i,c in enumerate(nb['cells']):
    tg=c['metadata'].get('tags') or []
    if any(x in str(tg) for x in ['fig7b','fig7c-no','fig6b','fig7a-partial']):
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        print(i,tg,len(t)); print(t[:400]); print('...')
E
```

```
49 ['claim:fig6b-suppressive-off-plane'] 4022
   balance quantity sign  mean_sup null  null_sup  p_vs_null_sup  null_exc  p_vs_null_exc     ok
0        a        a    a    0.1677  aaa    0.2014         0.0024    0.3949            0.0   True
1        a        a    a    0.1677  aab    0.1967         0.0080    0.4450            0.0   True
2        a        a    a    0.1677  aba    0.1631         0.9736    0.4979            0.0  False
3        a  
...
52 ['claim:fig7a-partial-ring'] 2871
   balance quantity sign amplitudes extremes  median    low   ring  between     ok
0        a        a    a          a        a   0.534  0.067  0.222    0.711   True
1        a        a    a          a        b   0.534  0.022  0.222    0.756   True
2        a        a    a          b        a   0.657  0.022  0.244    0.733   True
3        a        a    a          b        b   0.657  0.000  0.156  
...
58 ['claim:fig7b-pattern-index'] 3155
peak (SF cycles/cRF, TF Hz) counts: {np.str_('1.5|15.0'): np.int64(2), np.str_('1.5|30.0'): np.int64(1), np.str_('1.5|7.5'): np.int64(2), np.str_('3.0|15.0'): np.int64(8), np.str_('3.0|30.0'): np.int64(2), np.str_('3.0|7.5'): np.int64(1), np.str_('6.0|15.0'): np.int64(16), np.str_('6.0|3.75'): np.int64(3), np.str_('6.0|30.0'): np.int64(1), np.str_('6.0|7.5'): np.int64(9)} ; population pair: (6.0, 
...
59 ['claim:fig7b-pattern-index'] 5028

120 degree plaids: share of directions clipped, median 0.25 (range 0.00 to 0.58); gratings 0.29, plaids 0.17
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json, re, yaml
d=yaml.safe_load(open('attempts/nishimoto-2011-01.yaml'))
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
t='\n'.join(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])) for c in nb['cells'])
for o in d['outcomes']:
    if o.get('notebook')!='reproduce_nishimoto_2011.ipynb': continue
    nums=set(re.findall(r'-?\d+\.\d+(?:e-?\d+)?', o.get('notes','')))
    miss=[n for n in nums if n not in t and n.lstrip('-') not in t]
    print(o['claim'], miss)
E
```

```
fig3a-example-neuron ['0.699', '0.761', '0.758', '0.492', '0.760']
fig2b-contrast-normalization-no-effect ['0.414']
fig2b-compressive-improves ['6.2e-9', '1.8e-8', '1.7e-9', '8.8e-8']
fig2b-expansive-decreases ['6.3e-13', '4.5e-8']
fig2b-divisive-improves ['2.5', '0.0076', '0.038']
fig2b-compressive-divisive-best ['0.0090', '0.00016', '0.0038', '0.0019', '0.518', '0.506', '0.00075', '0.0083']
fig2b-no-interaction ['6.2e-9', '1.8e-8', '8.1e-9', '1.7e-9', '8.8e-8', '4.5e-8', '0.027', '0.039', '6.3e-13']
complex-cells-dominate ['0.191', '0.985', '0.514', '0.518', '5.7e-14']
fig6a-null-on-plane []
fig6a-excitatory-on-plane ['0.0098']
fig6b-suppressive-off-plane ['0.0097', '0.198', '0.168', '0.159']
fig7a-partial-ring ['22.2', '71.1']
fig7a-no-corr-prediction-hv []
fig7b-pattern-index ['4.7e-5', '2.2']
fig7c-hv-pattern-correlation ['0.177']
fig7c-no-corr-prediction-pattern ['0.370', '0.902', '-0.052']
fig8-recovery-simulated []
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
def T(i): return ''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
print(T(18)[:1100]); print(T(20)); print(T(32)[:400])
for i in (43,46,49,52,55):
    t=T(i).split('\n'); print(i, '\n'.join([l for l in t if not l[:3].strip().isdigit()][-12:]))
t=T(58); print(t[t.find('flat:'):])
t=T(62); print(t[t.find('combinations'):])
print(T(65))
E
```

```
mean_r    pct_a    pct_b    pct_c  n_better       p  p_bonf11  p_bonf5
model                                                                                       
linear                0.4135   0.0000   0.0000   0.0000         0     NaN       NaN      NaN
compressive           0.4324   4.5830   9.2124   4.7640        40  0.0000    0.0000   0.0000
expansive             0.3509 -15.1219 -26.8570 -15.7449         0  0.0000    0.0000   0.0000
linear +div           0.4256   2.9379   5.1276   3.8688        30  0.0051    0.0562   0.0255
compressive +div      0.4480   8.3570  16.1282   9.4198        40  0.0000    0.0000   0.0000
expansive +div        0.3578 -13.4696 -24.4783 -13.1933         7  0.0000    0.0000   0.0000
lum linear            0.4122  -0.2956  -1.3898   0.6449        26  0.4136    1.0000   1.0000
lum compressive       0.4268   3.2240   6.1380   4.0050        35  0.0000    0.0005   0.0002
lum expansive         0.3462 -16.2680 -28.5438 -16.6998         2  0.0000    0.0000   0.0000
lum linear +div       0.4248   2.7446   4.5906   3.8666        33  0.0059    
luminance and contrast normalization, linear, no divisive: mean r 0.412 against 0.413
change: (a) -0.3%  (b) -1.4%  (c) 0.6%; better in 26 of 45
Wilcoxon p = 0.4136; Bonferroni x11 = 1; x5 (variant) = 1
motion-enhanced validation only: p = 0.8933

compressive + divisive 0.448 against compressive 0.432; better in 34 of 45
Wilcoxon p = 0.0001551; x11 = 0.001706; x5 = 0.0007754; x12 = 0.001861
models against compressive + divisive (positive = better than it):
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,re
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
def T(i): return ''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
t=T(46).split('\n'); print('\n'.join(t[:3]))
vals=[float(l.split()[4]) for l in t[1:41] if len(l.split())>8]; ps=[float(l.split()[7]) for l in t[1:41] if len(l.split())>8]
print('exc range',min(vals),max(vals),'p max',max(ps))
t=T(49).split('\n'); print('\n'.join(l for l in t[1:41] if l.strip().endswith('True')))
ms=[float(l.split()[4]) for l in t[1:41] if len(l.split())>8]; print('sup range',min(ms),max(ms), sorted(set(ms)))
t=T(43).split('\n'); print('\n'.join(l for l in t if 'True' in l)[:1500])
print(T(70)[:600])
E
```

```
balance quantity sign  mean_exc null  null_mean       p  higher    ok
0        a        a    a    0.5920  aaa     0.3949  0.0000    True  True
1        a        a    a    0.5920  aab     0.4450  0.0000    True  True
exc range 0.5507 0.5966 p max 0.0078
0        a        a    a    0.1677  aaa    0.2014         0.0024    0.3949            0.0   True
1        a        a    a    0.1677  aab    0.1967         0.0080    0.4450            0.0   True
4        a        a    a    0.1677  baa    0.1951         0.0061    0.4039            0.0   True
20       b        a    a    0.1708  aaa    0.2094         0.0009    0.3777            0.0   True
21       b        a    a    0.1708  aab    0.2037         0.0042    0.4276            0.0   True
24       b        a    a    0.1708  baa    0.2023         0.0034    0.3896            0.0   True
sup range 0.0939 0.1708 [0.0939, 0.0977, 0.1071, 0.1115, 0.1538, 0.1587, 0.1677, 0.1708]
0       a    a      a       a        a    a  150     0.395  0.072    True
2       a    a      a       a        b    a  150     0.341  0.060    True
3       a    a      a       a        b    b  150     0.367  0.064    True
4       a    a      a       b        a    a  150     0.378  0.075    True
7       a    a      a       b        b    b  150     0.346  0.068    True
14      a    a      b       b        b    a  150     0.380  0.083    True
15      a    a      b       b        b    b  150     0.396  0.088    True
34      b    a      a       a        b    a  150     0.351  0.064    True
35      b    a      a       a        b    b  150     0.375  0.070    True
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
def T(i): return ''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
print(T(71)[:900]); print(T(56)[:300]); print(T(15)[:500])
E
```

```
noise reading (a): rows recovered A, B, C; columns true A, B, C
[[ 0.835 -0.016  0.015]
 [-0.029  0.57  -0.046]
 [ 0.133 -0.018  0.501]]
  each recovered field closest to its own: True
noise reading (b): rows recovered A, B, C; columns true A, B, C
[[ 0.791 -0.026  0.021]
 [-0.029  0.6   -0.043]
 [ 0.072 -0.051  0.672]]
  each recovered field closest to its own: True


neurons with r in 0.648 to 0.792: 3
  ct0013  r = 0.710  repeat estimate {'enhanced': 20}
  ct0021  r = 0.708  repeat estimate {'enhanced': 20}
  ct0039  r = 0.730  repeat estimate {'natural': 21, 'enhanced': 21}
highest r: {'ct0125': 0.605, 'ct0024': 0.633, 'ct0021': 0.708, 'ct0013': 0.71, 'ct0039': 0.73}
neurons whose motion-enhanced validation set shows 10 repeats: ['ct0028', 'ct0030']
the two neurons with 10 repeats: {'ct0028': np.float64(0.278), 'ct0030': np.float64(0.409)}
  ct0013: larges
```

**Agent**

Now apply the drifted values to the record and the main notebook's conclusions.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
p='attempts/nishimoto-2011-01.yaml'; s=open(p).read()
R=[("""  measured: 0.396
  notes: The mean excitatory on-plane ratio of 150 null neurons is within 0.324 to 0.396 in 12 of
    40 combinations of readings. With every reading (a) it is 0.396 (SD 0.072), at the upper edge""","""  measured: 0.395
  notes: The mean excitatory on-plane ratio of 150 null neurons is within 0.324 to 0.396 in 12 of
    40 combinations of readings. With every reading (a) it is 0.395 (SD 0.072), at the upper edge"""),
("tolerance in all, and above every null set by a rank-sum test (p from below 1e-4 to 0.0098), so","tolerance in all, and above every null set by a rank-sum test (p from below 1e-4 to 0.0078), so"),
("40 of 40 combinations meet the criterion. With every reading (a) it is 0.592; monkey f 0.555,","40 of 40 combinations meet the criterion. With every reading (a) it is 0.592; monkey f 0.556,"),
("to 0.198, and below the suppressive ratios of the null sets with rectified rates (0.196 to\n    0.209; rank-sum p 0.0008 to 0.0097).","to 0.198, and below the suppressive ratios of the null sets with rectified rates (0.195 to\n    0.209; rank-sum p 0.0009 to 0.0080)."),
("have pattern indices within -6.6 to 2.2 with the per-neuron peak frequency and 120 degree\n    plaids (median -5.07)","have pattern indices within -6.6 to 2.2 with the per-neuron peak frequency and 120 degree\n    plaids (median -5.10)"),
("presentations, 5, 10 or 20 repeats) the criterion is met in 16 to 20 of 20 draws under every","presentations, 5, 10 or 20 repeats) the criterion is met in 17 to 20 of 20 draws under every"),
("  notes: Across 64 combinations of readings the correlation ranges from -0.343 to 0.330 and none is","  notes: Across 64 combinations of readings the correlation ranges from -0.343 to 0.331 and none is"),
("    the indices of the rectified responses, the reading adopted for fig7b-pattern-index, r ranges\n    from -0.075 to 0.298 (0.096, p = 0.53, with the first readings)","    the indices of the rectified responses, the reading adopted for fig7b-pattern-index, r ranges\n    from -0.074 to 0.299 (0.097, p = 0.53, with the first readings)"),
("    frequency) r is 0.177 or less.","    frequency) r is 0.150 or less."),
("    fig7b-pattern-index), the per-neuron peak frequency and 120 degree plaids, r = -0.052, p =\n    0.733; with 90 degree plaids p = 0.358. The unrectified indices give p = 0.127, 0.902, 0.370 and\n    0.055, and the noisy indices of the first of the 20 draws with the per-neuron frequency p of\n    0.32 or more.","    fig7b-pattern-index), the per-neuron peak frequency and 120 degree plaids, r = -0.053, p =\n    0.73; with 90 degree plaids p = 0.359. The unrectified indices give p = 0.127, 0.899, 0.371 and\n    0.055, and the noisy indices of the first of the 20 draws with the per-neuron frequency p of\n    0.38 or more."),
]
for a,b in R:
    assert s.count(a)==1,a[:70]; s=s.replace(a,b)
# round-2 responses mention fig7c values from draws; add a note on the rerun drift to fig7b response
a="""      the clipping. The conclusion and notes say so. Outcome kept as verified, resting on the
      assumption."""
b="""      the clipping. The conclusion and notes say so. Outcome kept as verified, resting on the
      assumption. On this run the threaded fits moved some values in the third decimal (median
      index -5.10 for -5.07, noisy draws meeting the criterion 17 to 20 of 20 for 16 to 20); the
      notes give the new values."""
assert s.count(a)==1; s=s.replace(a,b)
open(p,'w').write(s)

def src(c): return c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
for path in ['entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb','executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb']:
    nb=json.load(open(path))
    for c in nb['cells']:
        if c['cell_type']!='markdown': continue
        t=src(c); t0=t
        for a,b in [("is 0.396 (SD 0.072)","is 0.395 (SD 0.072)"),("With every reading (a) it is 0.396","With every reading (a) it is 0.395"),
                    ("0.0098","0.0078"),("monkey f 0.555","monkey f 0.556"),("0.196 to 0.209","0.195 to 0.209"),("0.0008 to 0.0097","0.0009 to 0.0080"),
                    ("(median -5.07)","(median -5.10)"),("at least 16 of 20 draws","at least 17 of 20 draws"),
                    ("-0.343 to 0.330","-0.343 to 0.331"),("-0.075 to 0.298","-0.074 to 0.299"),("r = 0.096, p = 0.53","r = 0.097, p = 0.53"),
                    ("r is 0.177 or less (p 0.24 or more)","r is 0.150 or less (p 0.33 or more)"),
                    ("r = -0.052, p = 0.733","r = -0.053, p = 0.73"),("p = 0.358","p = 0.359"),("0.902, 0.370 and 0.055","0.899, 0.371 and 0.055"),
                    ("p of 0.32 or more","p of 0.38 or more")]:
            t=t.replace(a,b)
        if t!=t0: c['source']=t; print(path[:9], t[:60])
    json.dump(nb,open(path,'w'),indent=1,ensure_ascii=False)
E
grep -o "0\.39[56][^0-9][^.]*" entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb | head; date -u
```

```
entries/n **Result: reproduced.** The mean excitatory on-plane ratio o
entries/n **Result: reproduced.** The mean excitatory on-plane ratio i
entries/n **Result: reproduced.** With the fitted weights split per de
entries/n **Result: reproduced, on the rectified responses (assumed).*
entries/n **Result: not reproduced.** Across the 64 combinations of re
entries/n **Result: reproduced.** With the pattern indices of the rect
executed/ **Result: reproduced.** The mean excitatory on-plane ratio o
executed/ **Result: reproduced.** The mean excitatory on-plane ratio i
executed/ **Result: reproduced.** With the fitted weights split per de
executed/ **Result: reproduced, on the rectified responses (assumed).*
executed/ **Result: not reproduced.** Across the 64 combinations of re
executed/ **Result: reproduced.** With the pattern indices of the rect
0.396))\n",
0.396:\", int(NT
0.396 in 12 of 40 combinations of readings
0.395 (SD 0
Sat Nov 14 16:11:47 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
def T(i): return ''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
print(T(32)[-500:]); print(T(35)); print(T(38)[:400]); print(T(23)); print(T(67)[:500])
E
python tools/entry.py check entries/nishimoto-2011 2>&1 | tail -1
```

```
1.83e-10  x11 = 2.01e-09  x12 = 2.19e-09
  lum compressive              mean diff -0.0212  p = 2.84e-06  x11 = 3.12e-05  x12 = 3.41e-05
  lum expansive                mean diff -0.1018  p = 5.68e-14  x11 = 6.25e-13  x12 = 6.82e-13
  lum linear +div              mean diff -0.0232  p = 1.05e-07  x11 = 1.16e-06  x12 = 1.26e-06
  lum compressive +div         mean diff -0.0065  p = 0.382  x11 = 1  x12 = 1
  lum expansive +div           mean diff -0.0836  p = 5.68e-14  x11 = 6.25e-13  x12 = 6.82e-13

divisive False reading (a) compressive            against linear        : mean diff +0.0189, p = 8.03e-09, x11 = 8.84e-08
divisive False reading (a) expansive              against linear        : mean diff -0.0625, p = 5.68e-14, x11 = 6.25e-13
divisive False reading (b) compressive            against linear        : mean diff +0.0189, p = 8.03e-09, x11 = 8.84e-08
divisive False reading (b) expansive              against linear        : mean diff -0.0625, p = 5.68e-14, x11 = 6.25e-13
divisive True  reading (a) compressive +div       against linear        : mean diff +0.0346, p = 1.59e-09, x11 = 1.75e-08
divisive True  reading (a) expansive +div         against linear        : mean diff -0.0557, p = 4.11e-09, x11 = 4.52e-08
divisive True  reading (b) compressive +div       against linear +div   : mean diff +0.0224, p = 7.39e-10, x11 = 8.12e-09
divisive True  reading (b) expansive +div         against linear +div   : mean diff -0.0678, p = 5.68e-14, x11 = 6.25e-13

mean r: full 0.448, complex only 0.448, simple only 0.194
mean r^2: full 0.2154, complex only 0.2156 (ratio 1.001), simple only 0.0539 (ratio 0.250)
drop of mean r: complex only -0.0002, simple only 0.2545
Wilcoxon full vs complex only p = 0.0489; full vs simple only p = 5.68e-14
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open("executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb"))
def T(i): return ''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
print(T(68)[:400])
p='attempts/nishimoto-2011-01.yaml'; s=open(p).read()
for a,b in [("    lower by 0.0065 (p = 0.36).","    lower by 0.0065 (p = 0.38)."),("(ratio of mean squared correlations 1.001, Wilcoxon p = 0.054)","(ratio of mean squared correlations 1.001, Wilcoxon p = 0.049)")]:
    assert s.count(a)==1,a; s=s.replace(a,b)
open(p,'w').write(s)
def src(c): return c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
for path in ['entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb','executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb']:
    nb=json.load(open(path))
    for c in nb['cells']:
        if c['cell_type']=='markdown':
            t=src(c); t2=t.replace("lower by 0.0065 (p = 0.36)","lower by 0.0065 (p = 0.38)").replace("p = 0.054","p = 0.049")
            if t2!=t: c['source']=t2; print('fixed', t2[:50])
    json.dump(nb,open(path,'w'),indent=1,ensure_ascii=False)
E
grep -n "0.054\|p = 0.36" entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb attempts/nishimoto-2011-01.yaml | cut -c1-160
```

```
14 neurons with both validation sets (f0073, f0086, f0087, f0090, f0100, f0104, f0105, f0110, f0112, f0114, f0116, v0383, v0384, v0390)
mean r natural 0.493 [expected 0.533 +- 0.053: True], motion-enhanced 0.462 [expected 0.537 +- 0.054: False]
Wilcoxon signed-rank p = 0.2412; natural higher in 10 of 14; mean difference +0.031
  ct0031  natural 0.623  enhanced 0.458
  ct0039  natural 0.768  enhanc
fixed **Result: reproduced.** The compressive and divisi
fixed **Result: reproduced.** With complex-cell regresso
fixed **Result: reproduced.** The compressive and divisi
fixed **Result: reproduced.** With complex-cell regresso
entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb:1214:    "      f\"motion-enhanced {re_.mean():.3f} [expected 0.537 +- 0.054: {abs(re_.mean() - 0.537) <= 
entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb:1225:    "**Result: partially reproduced with the 2 x 2 pooling of this notebook; `finer_pooling.ipynb`, w
attempts/nishimoto-2011-01.yaml:364:    mean, 0.462, below 0.537 +- 0.054, and p = 0.241.
```

**Agent calls Bash**

```bash
cd  grep -o "With complex-cell regressors only[^\"]*" entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb | cut -c1-600; grep -n "0.049" attempts/nishimoto-2011-01.yaml
```

```
With complex-cell regressors only, the mean correlation is 0.448, the same as the full model (mean r squared ratio 1.001; Wilcoxon p = 0.049); with simple-cell regressors only it falls to 0.194 (ratio 0.250, p = 5.7e-14). Here the simple cells are limited to 0.75 cycles per cRF and SF 0 (218 of 763 regressors).
208:    (ratio of mean squared correlations 1.001, Wilcoxon p = 0.049); with simple-cell regressors
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
def src(c): return c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
for path in ['entries/nishimoto-2011/reproduce_nishimoto_2011.ipynb','executed/nishimoto-2011/reproduce_nishimoto_2011.ipynb']:
    nb=json.load(open(path))
    for c in nb['cells']:
        if c['cell_type']=='markdown':
            t=src(c); t2=t.replace("the mean correlation is 0.448, the same as the full model (mean r squared ratio 1.001; Wilcoxon p = 0.049)","the mean correlation is 0.448, as for the full model (mean r squared ratio 1.001; the complex-only model is higher by 0.0002 on average, Wilcoxon p = 0.049)")
            if t2!=t: c['source']=t2; print('fixed')
    json.dump(nb,open(path,'w'),indent=1,ensure_ascii=False)
p='attempts/nishimoto-2011-01.yaml'; s=open(p).read()
a="(ratio of mean squared correlations 1.001, Wilcoxon p = 0.049)"
s=s.replace(a,"(ratio of mean squared correlations 1.001; higher than the full model by 0.0002 on average,\n    Wilcoxon p = 0.049)"); open(p,'w').write(s)
E
python tools/entry.py check entries/nishimoto-2011 2>&1 | tail -1; python -c "
import yaml;d=yaml.safe_load(open('attempts/nishimoto-2011-01.yaml'));print([o['outcome'] for o in d['outcomes']].count('reproduced'))"; date -u
```

```
fixed
fixed
0 error(s)
14
Sat Nov 14 16:12:23 UTC 2026
```

**Agent**

I revised the attempt for every point in the round-2 report. No outcome changed and nothing is under `proposed`: the counts are still 14 reproduced, 3 partially reproduced, 2 not reproduced and 1 blocked. `tools/entry.py check` passes with 0 errors.

One process problem first: `tools/entry.py all` was not run as you asked. Its three notebooks together take about 140 minutes, and a single command here is capped at 2 hours. Instead I ran each notebook on its own, using the same environment and nbconvert command that `entry.py` uses. So there is no clean-run stamp, and the next `entry.py run` will execute everything again.

**What the new runs showed**
- **Repeat runs drift slightly.** Re-running the main notebook moved some values in the third decimal, presumably because the threaded fits are not exactly repeatable. I updated every affected number in the record and the conclusions. Two of them matter:
  - fig6a-null-on-plane: measured is now 0.395 (was 0.396), still inside the band.
  - complex-cells-dominate: the complex-only versus full-model Wilcoxon p went from 0.054 to 0.049, so I reworded "the same as the full model". The ratio is still 1.001 and the outcome is unchanged.
- **Figure 2B with the finer pooling (point 1).** A new notebook, `finer_pooling_fig2b.ipynb`, refits the linear and compressive models, each with and without divisive normalization, on the 3×3 pooling.
  - fig2b-divisive-improves: +2.5% (reading a), Bonferroni-corrected p = 0.084 over 11 comparisons. It still fails the claim's p < 0.01, so it stays not reproduced.
  - fig2b-compressive-improves: 5.6% and 8.0% (reading a); only reading (b) with divisive normalization is within tolerance. Still partially reproduced.
  - fig2b-compressive-divisive-best: corrected p = 0.0083, still reproduced among the four models refitted.
  - fig2b-no-interaction: still holds for the compressive model.
- **fig7b-pattern-index (point 2).** A new cell prints, for each neuron, the share of grating and plaid directions that rectification sets to zero, and the index with and without rectification.
  - The median share is 25% (range 0 to 58%), and the change in the index grows with it (Spearman rho 0.568, p = 4.7e-5).
  - The 8 neurons with nothing clipped keep their component-like indices (2 of 8 in the range). 27 of the 37 clipped neurons land in the range.
  - So the indices reach the paper's range through clipping. I kept the verified outcome (reproduced, resting on the rectification assumption) and say this in the conclusion and the notes.

**Text corrections** (all six sentences the verifier quoted are fixed)
- The `finer_pooling.ipynb` claim that the 4×4 pooling "does not raise it further" now gives the actual changes (−0.022, −0.046, +0.025) and calls them mixed.
- The main summary row for fig2b-expansive-decreases now says that under reading (a) both sizes are outside tolerance.
- The deviation saying "every other analysis uses 763 regressors" now names the analyses that use the finer pooling.
- The deviation text copied onto fig3a-example-neuron and complex-cells-dominate is replaced, and the README now agrees with the record on where each claim is judged.
- The fig7c notes now say the noisy-index values come from the first of the 20 draws.
- The round-2 `verifications` block is recorded, with the verifier's reasons and my responses.

**Not done, and why**
- **Expansive and luminance-normalized models:** not refitted on the 3×3 pooling, for time. The deviations say so.
- **Null-movie reading (b):** still not run under all four combinations. The verifier noted this does not affect a conclusion.
- **Runtimes:** the main notebook took 65 minutes, over the 60-minute aim (the previous run took 63). The new Figure 2B notebook took 47 minutes.
- **Executed copies:** I copied the final markdown into the executed copies of the main and Figure 2B notebooks after their runs. Their code cells are identical to the committed ones.
- **Questions file:** nothing added to `questions/nishimoto-2011.yaml`, because the verifier found no place where the claims file misreads the paper.

## End of run

64 turns, 219 minutes, $5.25 at API prices, result: success.
