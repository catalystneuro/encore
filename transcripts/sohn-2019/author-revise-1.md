# 000130 · author-revise-1 · run 38628850317

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; echo ----; cat transcripts/000130/verifier-1-report.md; echo ----; ls -R entries/000130-sohn-2019 | head -50
```

**Agent calls Bash**

```bash
ls docs; ls tools
```

```
agents
design.md
pilot-notes.md
protocol.md
agent_run.py
build_site.py
build_targets.py
entry.py
progress.py
site_assets
transcript.py
```

```
# Protocol for an attempt

Version: `pilot-6`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the eight pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

[... 379 more lines not kept]
```

**Agent calls Bash**

```bash
ls docs/agents; cat docs/agents/*author* 2>/dev/null | head -200; ls attempts | grep 000130; ls claims/000130; ls transcripts/000130
```

```
author-revise-3.md
author-revise.md
author.md
verifier-1.md
verifier-2.md
verifier-3.md
You are the author of the reproduction attempt `{attempt}` (entry `entries/{entry}`) in the reproduction registry, checked out in the current directory. The verifier has reviewed the changes you proposed after round 2; its round-3 report is `{report}`. Follow docs/protocol.md, step 6.

For each proposed change the verifier agreed with, set the claim's `outcome` (and `blocked_by`) to the proposed one and remove `proposed`. For each it did not agree with, keep the outcome and leave `proposed` with the verifier's view added to its reason. Change nothing else in the outcomes. Update the notebook's conclusions and summary, the entry README and the attempt notes to match, re-run with `python tools/entry.py all entries/{entry}`, and record round 3 under `verifications` with one result for each claim the verifier reviewed: whether it agreed, the outcome it would give, its reason in its own words, and your response. Do not commit or push: the workflow commits your changes.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": ".

Your final message is a short report of which outcomes changed and which proposals stand.

Run every command in the foreground and wait for it to finish, however long it takes: the run ends when you stop, and anything still running is lost.
You are the author of the reproduction attempt `{attempt}` (entry `entries/{entry}`) in the reproduction registry, checked out in the current directory. An independent verifier has reviewed it; its round-{round} report is `{report}`. Follow docs/protocol.md, step 6 ("Hand over for verification") and the rules it refers to.

For each point in the report: fix what it found, or say why not. Add any output it asked for. Where it disagrees with an outcome, either change the outcome and say why, or keep it and record the disagreement. In round 2, no outcome may change: if you find one sh
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000130-sohn-2019-01.yaml; echo ----; cat transcripts/000130/author-report.md
```

```
schema_version: 1
id: 000130-sohn-2019-01
dandiset: "000130"
dandiset_version: 0.241017.1448
paper: doi:10.1016/j.neuron.2019.06.012
date: 2026-10-14
entry: 000130-sohn-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-6
outcomes:
- claim: beh-slopes
  outcome: not_reproduced
  notebook: reproduce_sohn_2019.ipynb
  output: claim:beh-slopes
[... 344 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "verification" -A40 tools/entry.py | head -150; grep -ln "verifications:" attempts/*.yaml
```

```
220:        for rnd in attempt.get("verifications") or []:
221-            for r in rnd["results"]:
222-                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
223-        for outcome in attempt.get("outcomes", []):
224-            verified = agreed.get(outcome.get("claim"))
225-            if verified and outcome.get("outcome") != verified:
226-                report.error(where, f"claim {outcome.get('claim')!r} is {outcome.get('outcome')!r}, but the last "
227:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
228-                                    "and verify it in another round")
229-            if outcome.get("claim") not in known:
230-                report.error(path.relative_to(ROOT), f"claim {outcome.get('claim')!r} is not in the claims file")
231-            notebook = outcome.get("notebook")
232-            if notebook and notebook not in listed:
233-                report.error(path.relative_to(ROOT), f"notebook {notebook!r} is not in the entry")
234-            tag = outcome.get("output")
235-            if notebook in present and tag:
236-                nb = nbformat.read(entry_dir / notebook, as_version=4)
237-                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
238-                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
239-    return report
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^verifications:" -A40 attempts/001453-fouke-2025-01.yaml | head -60; ls schema* 2>/dev/null; ls; grep -rn "verifications" schemas/ 2>/dev/null | head
```

```
303:verifications:
304-- date: '2026-10-14'
305-  kind: agent
306-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
307-  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
308-    module and the claims file, with the paper's accepted manuscript (PMC12218792). The verifier
309-    listed the version's assets through the DANDI API and ran synthetic checks of angular_acceleration,
310-    trial_measures and the steadiness measure.
311-  results:
312-  - claim: stimulus-code-link
313-    agrees: true
314-    outcome: reproduced
315-    reason: All 13 codes the analysis uses are present. 17 of 18 species x stimulus speed medians are
316-      within 10% of the paper code's printed values; the one miss is DC static, 10.52 against 11.9.
317-      Angular velocities match to a median of 0.02 deg/s. ZF turning to code 9 is +0.02 deg/s and to
318-      code 11 is +1.59 deg/s, so the sign cannot settle which of them is lateral right. It asked for
319-      the code's static window and the DC static values it gives, and for per-fish turning time
320-      courses for codes 9 and 11 against medial codes 10 and 13, by species.
321-    response: Read the code's handling of code 20 in Fig1-S1.ipynb. It keeps the first 35 s of each
322-      code-20 trial number and measures from 3 s, the same frames as here; its exclusion of zero
[... 43 more lines not kept]
```

**Agent**

I've read the protocol, the verifier's report and the attempt record. Next I'll read the notebook and helper module to plan the fixes.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019; wc -l rsg.py; python -c "
import nbformat
nb=nbformat.read('reproduce_sohn_2019.ipynb',4)
for i,c in enumerate(nb.cells):
    print('=====',i,c.cell_type,c.metadata.get('tags'))
    print(c.source)
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
412 rsg.py
1106 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

**Agent calls Read**

```json
{
 "file_path": "entries/000130-sohn-2019/rsg.py"
}
```

```
1	"""Loading and measures for the Ready-Set-Go data of dandiset 000130.
2	
3	Sohn, Narain, Meirhaeghe & Jazayeri (2019), Neuron, doi:10.1016/j.neuron.2019.06.012.
4	
5	The dandiset is the DMFC_RSG set of the Neural Latents Benchmark: one session of monkey H
6	(Haydn, 2016-12-11). The train file holds the trial table with every task variable and the
7	spike times of 54 units; the test file holds 283 further trials without task variables and
8	only 40 of the units. Analyses use the train file. Files are streamed from the archive at the
9	pinned version; nothing is written to disk.
10	
11	Where the parameters come from:
12	
13	- From the paper's STAR Methods: units kept with a mean rate of at least 1 spike/s and at least
14	  5 trials per condition (`MIN_RATE`, `MIN_TRIALS`); 20 ms bins and a 40 ms Gaussian kernel for
15	  population rates (`BIN_MS`, `SMOOTH_MS`, read here as the kernel's SD); attrition in the
16	  estimation epoch; production rates up to the shortest tp of each ts; PCA keeping the
17	  components that explain 75% of the variance (`VAR_KEPT`); the encoding axis from difference
18	  vectors every 20 ms; the 80 ms GLM window before Set (`GLM_WINDOW_MS`) and BIC comparison;
19	  the Bayesian observer with scalar measurement and production noise, a uniform prior, the
20	  posterior mean, and an offset per prior; GPFA on single trials with cross-validation.
[... 393 more lines not kept]
```

```
1	===== 0 markdown None
2	# Reproducing Sohn et al. (2019) from dandiset 000130
3	
4	Paper. Sohn H, Narain D, Meirhaeghe N, Jazayeri M (2019). Bayesian computation through cortical
5	latent dynamics. *Neuron* 103(5):934-947.
6	[doi:10.1016/j.neuron.2019.06.012](https://doi.org/10.1016/j.neuron.2019.06.012). This attempt used
7	the full text of the accepted author manuscript in PubMed Central (PMC6805134). The supplementary
8	figures and tables (Tables S1 to S3) were not available to it.
9	
10	Dandiset. [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version
11	0.241017.1448. The paper cites no DANDI version (it predates the dandiset, which was made for the
12	Neural Latents Benchmark in 2021). Of the two published versions, 0.220113.0407 and 0.241017.1448,
13	this is the most recent. Both hold the same two files (same asset and blob ids and sizes), and
14	their metadata differ only in the publication date, the citation and the repository URL's trailing
15	slash, so neither matches the paper better.
16	
17	What the dandiset holds. One recording session (2016-12-11) of monkey H ("Haydn"), from the
18	Neural Latents Benchmark (NLB): a train file with the full trial table and the spikes of 54 units,
19	and a test file with 283 further trials of the same session that carry no task variables and only
20	40 of the units. The paper analyses 17 sessions of monkey H and 12 of monkey G. Monkey G is not in
[... 747 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 768
}
```

```
768	print(f"\nMeasured shallower than unbiased in {(ini.measured_minus_unbiased > 0).sum()} of 8; "
769	      f"two-sided signed-rank p = {w.pvalue:.4f}; trials dropped for tp < 400 ms: {dropped}")
770	print("Measured slope negative in", int((ini.slope_measured < 0).sum()), "of 8")
771	===== 56 markdown None
772	**Result: reproduced.** The initial speed falls with ts in all 8 dataset-priors, and its slope is
773	shallower than the unbiased 1/ts profile in 7 of 8 (two-sided signed-rank p = 0.039). Eye Right,
774	Long is the exception. No trial was dropped for tp < 400 ms.
775	===== 57 markdown None
776	### speed-predicts-tp
777	
778	> The speed of neural trajectories in the production epoch predicts the mean tp (Pearson
779	> correlation, rho Short = -0.58, rho Long = -0.52; Figure 4G).
780	===== 58 code ['claim:speed-predicts-tp']
781	for prior in ["Short", "Long"]:
782	    g = spd[spd.prior == prior]
783	    r, p = stats.pearsonr(g.speed, g.mean_tp)
784	    rb, pb = stats.pearsonr(g.speed_per_tp, g.mean_tp)
785	    within = [stats.pearsonr(h.speed, h.mean_tp)[0] for _, h in g.groupby("dataset")]
786	    print(f"{prior}: rho(speed, mean tp) = {r:.3f} (p = {p:.2g}), 20 points; variant speed / mean tp: {rb:.3f} (p = {pb:.2g}); "
787	          "within datasets: " + ", ".join(f"{x:.2f}" for x in within))
[... 320 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; cat claims/000130/10.1016-j.neuron.2019.06.012.yaml; ls paper/ 2>/dev/null; ls executed/ 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls executed/ executed/000130-sohn-2019 2>&1 | head; ls -a executed/000130-sohn-2019/.venv/lib/*/site-packages/elephant/gpfa 2>/dev/null; cat entries/000130-sohn-2019/entry.yaml entries/000130-sohn-2019/requirements.in
```

```
Exit code 1
ls: cannot access 'executed/': No such file or directory
ls: cannot access 'executed/000130-sohn-2019': No such file or directory
cat: entries/000130-sohn-2019/entry.yaml: No such file or directory
cat: entries/000130-sohn-2019/requirements.in: No such file or directory
```

**Agent calls Bash**

```bash
pwd; cd  ls executed 2>&1; cat entries/000130-sohn-2019/entry.yaml entries/000130-sohn-2019/requirements.in; grep -n "executed\|venv" tools/entry.py | head -30
```

```
entries/000130-sohn-2019
ls: cannot access 'executed': No such file or directory
schema_version: 1
name: 000130-sohn-2019
type: reproduction
title: Bayesian computation through cortical latent dynamics (Sohn et al. 2019)
description: Tests the findings of Sohn, Narain, Meirhaeghe and Jazayeri (2019) on dandiset 000130,
  the Neural Latents Benchmark's DMFC_RSG set, which holds one session of monkey H performing the
  Ready-Set-Go task with 54 units from dorsomedial frontal cortex. It tests the behaviour and the
  Bayesian observer model, single-unit sensitivity to the prior and elapsed time, the geometry and
  speed of population trajectories, the alternative mechanisms, and single-trial GPFA trajectories.
  Monkey G and the recurrent network models are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_sohn_2019.ipynb
  title: Reproducing Sohn et al. (2019) from dandiset 000130
  runtime_minutes: 7
helpers:
- rsg.py
related:
[... 32 more lines not kept]
```

**Agent**

There's no executed copy, so I'll build a working environment from the lock file to develop the new cells before the full run.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.12 dev && uv pip install -q --python dev/bin/python -r entries/000130-sohn-2019/requirements.lock.txt ipykernel 2>&1 | tail -3; grep -n PYTHON_VERSION tools/entry.py | head -2; ls dev/lib/python*/site-packages/elephant/gpfa/
```

```
57:PYTHON_VERSION = "3.13"
257:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
__init__.py
gpfa.py
gpfa_core.py
gpfa_util.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "fit_info\|log_likelihood\|em_tol\|def em\|lls" $TMPDIR/dev/lib/python*/site-packages/elephant/gpfa/gpfa.py $TMPDIR/dev/lib/python*/site-packages/elephant/gpfa/gpfa_core.py | head -40
```

```
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:126:    em_tol : float, optional
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:172:    fit_info : dict
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:178:        log_likelihoods : list
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:184:        log_likelihood : float
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:237:        em_tol=1.0e-8,
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:248:        self.em_tol = em_tol
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:267:        self.fit_info = dict()
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:365:            self.params_estimated, self.fit_info = gpfa_core.fit(
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:371:                em_tol=self.em_tol,
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:486:            self.transform_info["log_likelihood"] = ll
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:563:        log_likelihood : float
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py:567:        return self.transform_info["log_likelihood"]
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa_core.py:24:def fit(seqs_train, x_dim=3, bin_width=20.0, min_var_frac=0.01, em_tol=1.0E-8,
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa_core.py:51:    em_tol : float, optional
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa_core.py:90:    fit_info : dict
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa_core.py:140:        max_iters=em_max_iters, tol=em_tol, freq_ll=freq_ll, verbose=verbose)
/tmp/claude-1001/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa_core.py:142:    fit_info = {'iteration_time': iter_time, 
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 215,250p $TMPDIR/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa_core.py; sed -n 125,145p $TMPDIR/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa_core.py
```

```
list of log likelihoods after each EM iteration
    iter_time : list
        lisf of computation times (in seconds) for each EM iteration
    """
    params = params_init
    t = seqs_train['T']
    y_dim, x_dim = params['C'].shape
    lls = []
    ll_old = ll_base = ll = 0.0
    iter_time = []
    var_floor = min_var_frac * np.diag(np.cov(np.hstack(seqs_train['y'])))
    seqs_latent = None

    # Loop once for each iteration of EM algorithm
    for iter_id in trange(1, max_iters + 1, desc='EM iteration',
                          disable=not verbose):
        if verbose:
            print()
        tic = time.time()
        get_ll = (np.fmod(iter_id, freq_ll) == 0) or (iter_id <= 2)
[... 36 more lines not kept]
```

**Agent**

I'll write a small dev runner that executes the notebook's cells (skipping the slow GPFA ones when not needed) followed by draft code, so I can iterate on the new variants quickly.

**Agent calls Bash**

```bash
cat > $TMPDIR/runner.py <<'EOF'
import sys, os, time, pickle
import matplotlib; matplotlib.use("Agg")
import nbformat
os.chdir("entries/000130-sohn-2019")
sys.path.insert(0, ".")
nb = nbformat.read("reproduce_sohn_2019.ipynb", 4)
skip_gpfa = "--gpfa" not in sys.argv
ns = {}
for i, c in enumerate(nb.cells):
    if c.cell_type != "code":
        continue
    tags = c.metadata.get("tags", [])
    if skip_gpfa and any("gpfa" in t for t in tags):
        continue
    if "--quiet" in sys.argv:
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            exec(c.source, ns)
    else:
        print(f"----- cell {i} {tags}")
        exec(c.source, ns)
for f in [a for a in sys.argv[1:] if a.endswith(".py")]:
    print(f"===== {f}")
    exec(open(f).read(), ns)
EOF
cd $TMPDIR && time dev/bin/python runner.py 2>&1 | tail -80
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/runner.py", line 3, in <module>
    import nbformat
ModuleNotFoundError: No module named 'nbformat'

real	0m0.527s
user	0m0.686s
sys	0m0.042s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv pip install -q --python dev/bin/python nbformat && time dev/bin/python runner.py 2>&1 | tail -150
```

```
Hand Right  0.0484  0.0497              True

Long below Short in 4 of 4 datasets; ratio Long / Short: 0.55, 0.63, 0.34, 0.97
----- cell 52 ['claim:speed-vs-projection']
   dataset prior   ts  xu_at_set  speed  duration_ms  mean_tp  trials  speed_per_tp
 Eye Right Short  480    -41.591  7.926          400  496.868      24         0.016
 Eye Right Short  560    -37.181  7.723          440  543.739      27         0.014
 Eye Right Short  640    -19.017  6.358          500  630.550      31         0.010
 Eye Right Short  720      1.280  5.299          640  752.037      22         0.007
 Eye Right Short  800     13.480  4.379          720  836.602      25         0.005
 Eye Right  Long  800    -15.897  5.908          700  844.335      38         0.007
 Eye Right  Long  900     -7.900  4.806          760  922.279      34         0.005
 Eye Right  Long 1000      8.071  4.158          840 1002.392      23         0.004
 Eye Right  Long 1100     19.829  3.902          920 1156.215      25         0.003
 Eye Right  Long 1200     23.605  3.392          880 1176.536      27         0.003
  Eye Left Short  480    -44.640  9.128          460  539.534      21         0.017
  Eye Left Short  560    -44.994  7.389          460  579.976      28         0.013
  Eye Left Short  640    -23.645  6.881          540  666.884      17         0.010
  Eye Left Short  720      8.176  5.069          580  772.095      17         0.007
  Eye Left Short  800     16.639  5.195          700  864.015      22         0.006
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/cells; cd $TMPDIR/cells
cat > glm_null.py <<'EOF'
# Chance levels: the same BIC rule with the prior labels shuffled across trials within each
# effector and direction, and with the time points shuffled among the rows of each trial.
rng_glm = np.random.default_rng(7)
N_SHUFFLES = 5


def shuffled_prior(df, trs):
    lab = trs.is_short.to_numpy().copy()
    for _, idx in trs.reset_index(drop=True).groupby(["is_eye", "theta"]).groups.items():
        lab[idx] = rng_glm.permutation(lab[idx])
    out = df.copy()
    out["prior"] = (~lab[df.trial.to_numpy()]).astype(float)
    return out


def shuffled_time(df):
    out = df.copy()
    t = out.t.to_numpy().copy()
    for idx in out.groupby("trial").indices.values():
        t[idx] = rng_glm.permutation(t[idx])
    out["t"] = t
    return out


null_rows = []
for s in range(N_SHUFFLES):
    dfs = shuffled_prior(df_all, good)
    dft = {short: shuffled_time(dfp) for short, (dfp, _) in per_prior.items()}
    n_prior = n_ts_s = n_ts_l = n_ts = 0
    for j in range(len(units)):
        y = Y_all[:, j]
        lf, kf = fit(y, design(dfs))
        lr, kr = fit(y, design(dfs, with_prior=False))
        n_prior += bic(lr, kr, len(y)) - bic(lf, kf, len(y)) > 0
        dep = {}
        for short, (_, Yp) in per_prior.items():
            yp = Yp[:, j]
            lf, kf = fit(yp, design(dft[short], with_prior=False))
            lr, kr = fit(yp, design(dft[short], with_t=False, with_prior=False))
            dep[short] = bic(lr, kr, len(yp)) - bic(lf, kf, len(yp)) > 0
        n_ts_s += dep[True]
        n_ts_l += dep[False]
        n_ts += dep[True] or dep[False]
    null_rows.append({"shuffle": s, "prior_dep_pct": 100 * n_prior / len(units), "ts_dep_short_pct": 100 * n_ts_s / len(units),
                      "ts_dep_long_pct": 100 * n_ts_l / len(units), "ts_dep_either_pct": 100 * n_ts / len(units)})
glm_null = pd.DataFrame(null_rows)
print("Fractions of units passing the BIC rule with shuffled labels (%):")
print(glm_null.round(1).to_string(index=False))
print(f"\nObserved: prior {100 * glm.prior_dep.mean():.1f}%, ts in Short {100 * (glm.ts_dBIC_short > 0).mean():.1f}%, "
      f"ts in Long {100 * (glm.ts_dBIC_long > 0).mean():.1f}%, ts in either {100 * glm.ts_dep.mean():.1f}%")
print(f"Shuffled, maximum over {N_SHUFFLES}: prior {glm_null.prior_dep_pct.max():.1f}%, ts in either {glm_null.ts_dep_either_pct.max():.1f}%")
EOF
cat > dfr_boot.py <<'EOF'
# Stability of the peak: resample trials with replacement within each dataset and prior, and
# find the bin of the largest mean RMS difference.
rng_dfr_boot = np.random.default_rng(8)
peaks = []
for _ in range(200):
    per = []
    for cnt, lab in cnts.values():
        i = np.concatenate([rng_dfr_boot.choice(np.flatnonzero(lab == v), (lab == v).sum()) for v in (True, False)])
        per.append(rms_dfr(cnt[i], lab[i]))
    peaks.append(int(np.argmax(np.mean(per, axis=0))))
peaks = pd.Series(peaks).map(lambda k: f"{edges[k]} to {edges[k + 1]}")
print("Bin of the largest mean RMS over 200 bootstrap samples of trials (ms after Ready):")
print(peaks.value_counts().to_string())
in_support = peaks.isin(["480 to 640", "640 to 800"]).mean()
print(f"Fraction of samples with the peak between 480 and 800 ms: {in_support:.2f}")
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet cells/dfr_boot.py 2>&1 | tail -20
```

```
===== cells/dfr_boot.py
Traceback (most recent call last):
  File "/tmp/claude-1001/runner.py", line 24, in <module>
    exec(open(f).read(), ns)
         ^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'cells/dfr_boot.py'
Shell cwd was reset to
```

**Agent**

Runner chdirs; I'll use absolute paths.

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/dfr_boot.py 2>&1 | tail -20
```

```
===== /tmp/claude-1001/cells/dfr_boot.py
Bin of the largest mean RMS over 200 bootstrap samples of trials (ms after Ready):
480 to 640    192
800 to 960      8
Fraction of samples with the peak between 480 and 800 ms: 0.96
Shell cwd was reset to
```

**Agent**

Peak is stable (96% of bootstrap samples in 480 to 800 ms). Next the GLM null, which needs a trial index in the GLM rows.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
c=nb.cells[29]
old='rows.append({"t": k, "prior"'
assert old in c.source
c.source=c.source.replace(old,'rows.append({"trial": i, "t": k, "prior"')
nbformat.write(nb,p)
EOF
cd $TMPDIR && time dev/bin/python runner.py --quiet $TMPDIR/cells/glm_null.py 2>&1 | tail -20
```

```
===== /tmp/claude-1001/cells/glm_null.py
Fractions of units passing the BIC rule with shuffled labels (%):
 shuffle  prior_dep_pct  ts_dep_short_pct  ts_dep_long_pct  ts_dep_either_pct
       0            0.0               2.1              0.0                2.1
       1            4.2               0.0              0.0                0.0
       2            0.0               0.0              0.0                0.0
       3            8.3               0.0              0.0                0.0
       4            0.0               2.1              0.0                2.1

Observed: prior 75.0%, ts in Short 31.2%, ts in Long 33.3%, ts in either 45.8%
Shuffled, maximum over 5: prior 8.3%, ts in either 2.1%

real	0m14.724s
user	0m22.262s
sys	0m0.262s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && cat >> glm_null.py <<'EOF'

# Slow drift can mimic a prior effect when the priors come in blocks. Shift the prior labels
# along the session (as in the clock check) so that the block structure is kept.
print("\nPrior labels shifted along the session, block structure kept:")
for shift in [50, 100, 200]:
    lab = np.roll(good.is_short.to_numpy(), shift)
    dfs = df_all.copy()
    dfs["prior"] = (~lab[df_all.trial.to_numpy()]).astype(float)
    n_prior = 0
    for j in range(len(units)):
        y = Y_all[:, j]
        lf, kf = fit(y, design(dfs))
        lr, kr = fit(y, design(dfs, with_prior=False))
        n_prior += bic(lr, kr, len(y)) - bic(lf, kf, len(y)) > 0
    print(f"   shifted by {shift} trials: labels unchanged on {100 * (lab == good.is_short.to_numpy()).mean():.0f}% of trials; "
          f"prior-dependent {100 * n_prior / len(units):.1f}%")
runs = (good.is_short.to_numpy()[1:] != good.is_short.to_numpy()[:-1]).sum() + 1
print(f"Prior blocks in the session (runs of one prior over used trials): {runs}; median length "
      f"{np.median(np.diff(np.r_[0, np.flatnonzero(np.diff(good.is_short.to_numpy().astype(int))) + 1, len(good)])):.0f} trials")
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/glm_null.py 2>&1 | tail -8
```

```
Observed: prior 75.0%, ts in Short 31.2%, ts in Long 33.3%, ts in either 45.8%
Shuffled, maximum over 5: prior 8.3%, ts in either 2.1%

Prior labels shifted along the session, block structure kept:
   shifted by 50 trials: labels unchanged on 56% of trials; prior-dependent 10.4%
   shifted by 100 trials: labels unchanged on 53% of trials; prior-dependent 14.6%
   shifted by 200 trials: labels unchanged on 48% of trials; prior-dependent 2.1%
Prior blocks in the session (runs of one prior over used trials): 87; median length 9 trials
Shell cwd was reset to
```

**Agent**

GLM chance levels are 0 to 15%, far below the observed 75% and 46%. Next: normalised-rate variants for PCA dimensionality and the encoding-axis specificity.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
p="rsg.py"
s=open(p).read()
old='''class PCA:
    """PCA on stacked rate matrices, keeping the components that reach `kept` of the variance."""

    def __init__(self, matrices: list, kept: float = VAR_KEPT):
        data = np.vstack(matrices)
        self.mean = data.mean(0)
        _, s, vt = np.linalg.svd(data - self.mean, full_matrices=False)
        self.explained = s ** 2 / np.sum(s ** 2)
        self.n = int(np.searchsorted(np.cumsum(self.explained), kept - 1e-12) + 1)
        self.components = vt[: self.n]
'''
new='''class PCA:
    """PCA on stacked rate matrices, keeping the components that reach `kept` of the variance,
    and at least `min_n`."""

    def __init__(self, matrices: list, kept: float = VAR_KEPT, min_n: int = 1):
        data = np.vstack(matrices)
        self.mean = data.mean(0)
        _, s, vt = np.linalg.svd(data - self.mean, full_matrices=False)
        self.explained = s ** 2 / np.sum(s ** 2)
        self.n = max(int(np.searchsorted(np.cumsum(self.explained), kept - 1e-12) + 1), min_n)
        self.components = vt[: self.n]


def unit_scale(matrices: list, how: str) -> np.ndarray:
    """Divisor per unit for normalised rates, from the stacked matrices (bins x units):
    `soft`, the range plus 5 spikes/s (soft normalisation, a common choice; the Methods do
    not say whether rates were normalised), or `z`, the SD."""
    data = np.vstack(matrices)
    if how == "soft":
        return np.ptp(data, axis=0) + 5.0
    return np.maximum(data.std(0), 1e-9)
'''
assert old in s
open(p,"w").write(s.replace(old,new))
EOF
cat > $TMPDIR/cells/pca_norm.py <<'EOF'
# Variants: rates normalised per unit before PCA (soft normalisation, and z-scoring), with the
# components reaching 75% of the variance. Estimation and production scales are taken from the
# trajectories that enter each PCA.
rng_norm = np.random.default_rng(9)
rows, enc_rows = [], []
for e, th, name in DS:
    E, P = EST[name], PROD[name]
    est_m = [E[True]["rate"], E[False]["rate"]]
    prod_m = [v["rate"] for v in P["traj"].values()]
    for how in ["soft", "z"]:
        se, sp = rsg.unit_scale(est_m, how), rsg.unit_scale(prod_m, how)
        pe = rsg.PCA([m / se for m in est_m])
        pp = rsg.PCA([m / sp for m in prod_m])
        rows.append({"dataset": name, "normalisation": how, "est_PCs_75": pe.n, "prod_PCs_75": pp.n})
        for short in [True, False]:
            lo, hi = min(rsg.prior_ts(short)), max(rsg.prior_ts(short))
            X, t = pe(E[short]["rate"] / se), E[short]["t"]
            u = rsg.encoding_axis(X, t, lo, hi)
            sel = (t >= lo - 1e-6) & (t <= hi + 1e-6)
            w, te = E[short]["n"][sel], PROJ[(name, short)]["te"]
            r2 = rsg.weighted_fit(te, X[sel] @ u, w)[2]
            rand = []
            for _ in range(1000):
                v = rng_norm.standard_normal(X.shape[1])
                rand.append(rsg.weighted_fit(te, X[sel] @ (v / np.linalg.norm(v)), w)[2])
            enc_rows.append({"dataset": name, "prior": "Short" if short else "Long", "normalisation": how, "PCs": X.shape[1],
                             "R2_bayes": r2, "random_R2_median": np.median(rand), "frac_random_above": np.mean(np.array(rand) >= r2)})
dims_norm = pd.DataFrame(rows)
print(dims_norm.to_string(index=False))
for how, g in dims_norm.groupby("normalisation"):
    print(f"{how}: in range (estimation 3 or 4, production 5 to 11) {g.est_PCs_75.between(3, 4).sum() + g.prod_PCs_75.between(5, 11).sum()} of 8")
enc_norm = pd.DataFrame(enc_rows)
EOF
cat > $TMPDIR/cells/enc_norm.py <<'EOF'
print("Encoding axis with normalised rates (75% of variance):")
print(enc_norm.round(4).to_string(index=False))
for how, g in enc_norm.groupby("normalisation"):
    hl = g[g.dataset == "Hand Left"].set_index("prior").R2_bayes
    print(f"{how}: Hand Left R2 Short {hl['Short']:.4f}, Long {hl['Long']:.4f}; mean of 4 Short {g[g.prior == 'Short'].R2_bayes.mean():.4f}, "
          f"Long {g[g.prior == 'Long'].R2_bayes.mean():.4f}; above 95% of random axes in {(g.frac_random_above < 0.05).sum()} of 8")
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/pca_norm.py $TMPDIR/cells/enc_norm.py 2>&1 | tail -40
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/runner.py", line 18, in <module>
    exec(c.source, ns)
  File "<string>", line 7, in <module>
TypeError: 'PCA' object is not callable
Shell cwd was reset to
```

**Agent**

I put the new function in the middle of the class. Fixing the placement.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
p="rsg.py"
s=open(p).read()
i=s.index("\n\ndef unit_scale"); j=s.index("    def __call__")
block=s[i:j]; s=s[:i]+"\n"+s[j:]
k=s.index("\n\ndef encoding_axis")
s=s[:k]+block.rstrip("\n")+"\n"+s[k:]
open(p,"w").write(s)
EOF
sed -n 188,225p rsg.py; cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/pca_norm.py $TMPDIR/cells/enc_norm.py 2>&1 | tail -40
```

```
# --- population measures -------------------------------------------------------------------

class PCA:
    """PCA on stacked rate matrices, keeping the components that reach `kept` of the variance,
    and at least `min_n`."""

    def __init__(self, matrices: list, kept: float = VAR_KEPT, min_n: int = 1):
        data = np.vstack(matrices)
        self.mean = data.mean(0)
        _, s, vt = np.linalg.svd(data - self.mean, full_matrices=False)
        self.explained = s ** 2 / np.sum(s ** 2)
        self.n = max(int(np.searchsorted(np.cumsum(self.explained), kept - 1e-12) + 1), min_n)
        self.components = vt[: self.n]

    def __call__(self, x: np.ndarray) -> np.ndarray:
        return (x - self.mean) @ self.components.T


def unit_scale(matrices: list, how: str) -> np.ndarray:
    """Divisor per unit for normalised rates, from the stacked matrices (bins x units):
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper 2>&1; ls entries/000130-sohn-2019/paper 2>&1
```

```
Exit code 2
ls: cannot access 'paper': No such file or directory
ls: cannot access 'entries/000130-sohn-2019/paper': No such file or directory
```

**Agent calls Bash**

```bash
mkdir -p paper && curl -s -o paper/PMC6805134_bioc.json "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC6805134/unicode" && ls -la paper && python3 -c "
import json
d=json.load(open('paper/PMC6805134_bioc.json'))
d=d[0] if isinstance(d,list) else d
txt='\n\n'.join(p['text'] for doc in d['documents'] for p in doc['passages'])
open('paper/PMC6805134.txt','w').write(txt)
print(len(txt))
"; grep -n -i "normali\|z-scor\|soft" paper/PMC6805134.txt | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat > $TMPDIR/cells/speed_null.py <<'EOF'
# Attrition adds noise: later bins average fewer trials, and noisier rates give larger steps.
# Variant 1: only the trials with the longest ts of the prior, which last the whole support, so
# the number of trials is the same in every bin. Null: units firing as Poisson processes at a
# constant rate (each unit's mean over the support in these trials), with the same trials and
# Set times, measured both ways. The point estimate of the main measure is also compared with
# the median of its bootstrap.
rng_null = np.random.default_rng(10)
rows = []
for e, th, name in DS:
    g = good[(good.is_eye == e) & (good.theta == th)]
    for short in [True, False]:
        gg = g[g.is_short == short]
        lo, hi = min(rsg.prior_ts(short)), max(rsg.prior_ts(short))
        c_ = rsg.counts(spikes, units, gg.ready_time.to_numpy(), 0, hi)
        el = ((gg.set_time - gg.ready_time) * 1000).to_numpy()
        ends = np.arange(1, c_.shape[1] + 1) * rsg.BIN_MS
        full = gg.ts.to_numpy() == hi
        fixed = support_slope(rsg.smooth(c_[full].mean(0) * 1000 / rsg.BIN_MS), ends, short)[0]
        lam = c_[:, ends > lo].mean((0, 1))           # counts per bin, per unit
        null_main, null_fixed = [], []
        for _ in range(100):
            sim = rng_null.poisson(lam, size=c_.shape).astype(float)
            sim[ends[None, :] > el[:, None] + rsg.BIN_MS] = 0    # beyond Set; excluded by attrition anyway
            null_main.append(support_slope(rsg.attrition_rates(sim, el)[0], ends, short)[0])
            null_fixed.append(support_slope(rsg.smooth(sim[full].mean(0) * 1000 / rsg.BIN_MS), ends, short)[0])
        main = asp[(asp.dataset == name) & (asp.prior == ("Short" if short else "Long"))].iloc[0]
        rows.append({"dataset": name, "prior": "Short" if short else "Long", "slope_main": main.slope_per_100ms,
                     "null_main_mean": np.mean(null_main), "null_main_95": np.percentile(null_main, 95),
                     "trials_full": int(full.sum()), "slope_fixed": fixed, "null_fixed_mean": np.mean(null_fixed),
                     "null_fixed_2.5": np.percentile(null_fixed, 2.5), "null_fixed_97.5": np.percentile(null_fixed, 97.5)})
spn = pd.DataFrame(rows)
spn["excess_main"] = spn.slope_main - spn.null_main_mean
print("Slopes of speed per 100 ms of the support; Poisson null of constant rates, 100 simulations:")
print(spn.round(3).to_string(index=False))
for prior, g in spn.groupby("prior", sort=False):
    print(f"{prior}: main slope above the null's 95th percentile in {(g.slope_main > g.null_main_95).sum()} of 4; "
          f"fixed trials, slope outside the null's 95% range in {((g.slope_fixed < g['null_fixed_2.5']) | (g.slope_fixed > g['null_fixed_97.5'])).sum()} of 4, "
          f"positive in {(g.slope_fixed > 0).sum()} of 4; signed-rank p (fixed trials) = {stats.wilcoxon(g.slope_fixed).pvalue:.3f}")
print("\nBootstrap of the main measure: point estimate below the bootstrap 2.5th percentile in",
      int((asp.slope_per_100ms < asp.boot_low).sum()), "of 8, so the bootstrap is biased upward and its intervals are not used.")
EOF
cd $TMPDIR && time dev/bin/python runner.py --quiet $TMPDIR/cells/speed_null.py 2>&1 | tail -20
```

```
===== /tmp/claude-1001/cells/speed_null.py
Slopes of speed per 100 ms of the support; Poisson null of constant rates, 100 simulations:
   dataset prior  slope_main  null_main_mean  null_main_95  trials_full  slope_fixed  null_fixed_mean  null_fixed_2.5  null_fixed_97.5  excess_main
 Eye Right Short       1.008           1.671         2.240           25        0.497            0.609           0.020            1.222       -0.663
 Eye Right  Long       0.579           1.070         1.384           27        0.256            0.415           0.010            0.782       -0.491
  Eye Left Short       1.270           1.846         2.533           22        0.529            0.809           0.126            1.475       -0.576
  Eye Left  Long       0.478           1.031         1.287           31        0.097            0.432           0.096            0.845       -0.554
Hand Right Short       0.890           1.573         2.047           22        0.357            0.613           0.002            1.244       -0.683
Hand Right  Long       0.578           0.985         1.220           25       -0.106            0.366           0.043            0.713       -0.407
 Hand Left Short       0.826           1.473         1.972           24        0.288            0.593           0.058            1.288       -0.648
 Hand Left  Long       0.668           1.162         1.481           18        0.137            0.432           0.069            0.855       -0.494
Short: main slope above the null's 95th percentile in 0 of 4; fixed trials, slope outside the null's 95% range in 0 of 4, positive in 4 of 4; signed-rank p (fixed trials) = 0.125
Long: main slope above the null's 95th percentile in 0 of 4; fixed trials, slope outside the null's 95% range in 1 of 4, positive in 3 of 4; signed-rank p (fixed trials) = 0.375

Bootstrap of the main measure: point estimate below the bootstrap 2.5th percentile in 2 of 8, so the bootstrap is biased upward and its intervals are not used.

real	0m15.588s
[... 3 more lines not kept]
```

**Agent**

The null has two bugs: zeroing counts past Set creates a jump at the end of the fixed-trial window, and the rate used for the null includes post-Set counts. Fixing both.

**Agent calls Bash**

```bash
cd $TMPDIR/cells && python3 - <<'EOF'
p="speed_null.py"; s=open(p).read()
s=s.replace("""        lam = c_[:, ends > lo].mean((0, 1))           # counts per bin, per unit
""","""        use = (el[:, None] >= ends[None, :] - 1e-6) & (ends[None, :] > lo)
        lam = c_[use].mean(0)                          # counts per bin and unit, before Set, in the support
""")
s=s.replace("""            sim[ends[None, :] > el[:, None] + rsg.BIN_MS] = 0    # beyond Set; excluded by attrition anyway
""","")
s=s.replace("(each unit's mean over the support in these trials)","(each unit's mean over the support before Set)")
open(p,"w").write(s)
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/speed_null.py 2>&1 | tail -16
```

```
===== /tmp/claude-1001/cells/speed_null.py
Slopes of speed per 100 ms of the support; Poisson null of constant rates, 100 simulations:
   dataset prior  slope_main  null_main_mean  null_main_95  trials_full  slope_fixed  null_fixed_mean  null_fixed_2.5  null_fixed_97.5  excess_main
 Eye Right Short       1.008           1.683         2.262           25        0.497            0.694           0.067            1.476       -0.675
 Eye Right  Long       0.579           0.999         1.275           27        0.256            0.389           0.020            0.853       -0.420
  Eye Left Short       1.270           1.813         2.278           22        0.529            0.801           0.012            1.492       -0.543
  Eye Left  Long       0.478           0.905         1.192           31        0.097            0.359           0.017            0.785       -0.428
Hand Right Short       0.890           1.430         1.872           22        0.357            0.555           0.067            1.074       -0.540
Hand Right  Long       0.578           0.949         1.318           25       -0.106            0.345          -0.040            0.648       -0.371
 Hand Left Short       0.826           1.461         1.940           24        0.288            0.591          -0.021            1.149       -0.636
 Hand Left  Long       0.668           1.130         1.531           18        0.137            0.418          -0.103            0.835       -0.462
Short: main slope above the null's 95th percentile in 0 of 4; fixed trials, slope outside the null's 95% range in 0 of 4, positive in 4 of 4; signed-rank p (fixed trials) = 0.125
Long: main slope above the null's 95th percentile in 0 of 4; fixed trials, slope outside the null's 95% range in 1 of 4, positive in 3 of 4; signed-rank p (fixed trials) = 0.375

Bootstrap of the main measure: point estimate below the bootstrap 2.5th percentile in 2 of 8, so the bootstrap is biased upward and its intervals are not used.
Shell cwd was r
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/cells/transient.py <<'EOF'
def transient_slopes(kept=rsg.VAR_KEPT, norm=None):
    rows = []
    for e, th, name in DS:
        g = good[(good.is_eye == e) & (good.theta == th)]
        traj = {}
        for short in [True, False]:
            for ts in rsg.prior_ts(short):
                gg = g[(g.is_short == short) & (g.ts == ts)]
                traj[(short, ts)] = rsg.aligned_rates(spikes, units, gg.set_time.to_numpy(), -100, 300)[5:15]  # Set to Set + 200 ms
        if norm:
            sc = rsg.unit_scale(list(traj.values()), norm)
            traj = {k: v / sc for k, v in traj.items()}
        pca_t = rsg.PCA(list(traj.values()), kept) if kept else (lambda x: x)
        t = np.arange(1, 11) * rsg.BIN_MS
        for short in [True, False]:
            ts_v = rsg.prior_ts(short)
            ref = pca_t(traj[(short, ts_v[2])])
            for which, ts in [("shortest", ts_v[0]), ("longest", ts_v[-1])]:
                dist = np.linalg.norm(pca_t(traj[(short, ts)]) - ref, axis=1)
                rows.append({"dataset": name, "prior": "Short" if short else "Long", "ts": which,
                             "PCs": getattr(pca_t, "n", len(units)), "mean_distance": dist.mean(),
                             "slope_per_100ms": np.polyfit(t, dist, 1)[0] * 100})
    out = pd.DataFrame(rows)
    out["slope_rel_pct"] = 100 * out.slope_per_100ms / out.mean_distance
    return out


tr_ = transient_slopes()
print(tr_.round(3).to_string(index=False))
for which, g in tr_.groupby("ts"):
    w = stats.wilcoxon(g.slope_per_100ms)
    print(f"{which} ts: signed-rank p = {w.pvalue:.3f}; positive slopes {(g.slope_per_100ms > 0).sum()} of 8; "
          f"median relative slope {g.slope_rel_pct.median():+.1f}% per 100 ms")
print("\nVariants (signed-rank p for the shortest and the longest ts; PCs kept per dataset):")
for kept, norm, lab in [(0.60, None, "60% of variance"), (0.90, None, "90% of variance"), (None, None, "full space"),
                        (0.75, "z", "z-scored rates, 75%"), (0.75, "soft", "soft-normalised rates, 75%")]:
    v = transient_slopes(kept, norm)
    ps = {w: stats.wilcoxon(g.slope_per_100ms).pvalue for w, g in v.groupby("ts")}
    pos = {w: int((g.slope_per_100ms > 0).sum()) for w, g in v.groupby("ts")}
    print(f"   {lab}: shortest p = {ps['shortest']:.3f} ({pos['shortest']} of 8 positive), longest p = {ps['longest']:.3f} "
          f"({pos['longest']} of 8 positive); PCs {v.groupby('dataset', sort=False).PCs.first().tolist()}")
EOF
cat > $TMPDIR/cells/threshold.py <<'EOF'
for kept, min_n, lab in [(0.60, 2, "60% of variance, at least 2 components"), (0.60, 3, "60% of variance, at least 3 components")]:
    v, _, _ = go_curves(kept, min_n)
    print(f"Variant, {lab}: median time of the minimum {v.t_min.median():.0f} ms; in the last 40 ms {(v.t_min >= -20).sum()} of {len(v)}; "
          f"in the last 200 ms {(v.t_min >= -180).sum()}")
one = thr_tab[thr_tab.PCs == 1]
print(f"Main, datasets with 1 component: {len(one)} curves, median time of the minimum {one.t_min.median():.0f} ms, "
      f"distance at Go over minimum above 10 in {(one.d_at_go_over_min > 10).sum()}")
EOF
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
c=nb.cells[68]
s=c.source
s=s.replace("def go_curves(kept):","def go_curves(kept, min_n=1):")
s=s.replace("pca_g = rsg.PCA(list(traj.values()), kept) if kept","pca_g = rsg.PCA(list(traj.values()), kept, min_n) if kept")
c.source=s
nbformat.write(nb,p)
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/transient.py $TMPDIR/cells/threshold.py 2>&1 | tail -16
```

```
Hand Left Short  longest    4         15.348           -2.504        -16.318
 Hand Left  Long shortest    4         14.481            8.189         56.549
 Hand Left  Long  longest    4         15.418            0.311          2.019
longest ts: signed-rank p = 0.039; positive slopes 2 of 8; median relative slope -15.3% per 100 ms
shortest ts: signed-rank p = 0.078; positive slopes 6 of 8; median relative slope +26.7% per 100 ms

Variants (signed-rank p for the shortest and the longest ts; PCs kept per dataset):
   60% of variance: shortest p = 0.078 (6 of 8 positive), longest p = 0.016 (1 of 8 positive); PCs [1, 1, 2, 2]
   90% of variance: shortest p = 0.109 (5 of 8 positive), longest p = 0.039 (2 of 8 positive); PCs [5, 4, 6, 8]
   full space: shortest p = 0.078 (6 of 8 positive), longest p = 0.023 (1 of 8 positive); PCs [48, 48, 48, 48]
   z-scored rates, 75%: shortest p = 0.742 (5 of 8 positive), longest p = 0.039 (1 of 8 positive); PCs [6, 5, 7, 8]
   soft-normalised rates, 75%: shortest p = 0.312 (5 of 8 positive), longest p = 0.055 (2 of 8 positive); PCs [4, 4, 5, 6]
===== /tmp/claude-1001/cells/threshold.py
Variant, 60% of variance, at least 2 components: median time of the minimum -230 ms; in the last 40 ms 8 of 32; in the last 200 ms 14
Variant, 60% of variance, at least 3 components: median time of the minimum -70 ms; in the last 40 ms 13 of 32; in the last 200 ms 23
Main, datasets with 1 component: 16 curves, median time of the minimum -150 ms, distance at Go over minimum above 10 in 5
Shell cwd was reset to
```

**Agent**

Transient result holds across all variants for the longest ts except soft normalisation (p = 0.055). Now partial correlations given ts and the weighted RMSE.

**Agent calls Bash**

```bash
cat > $TMPDIR/cells/partial.py <<'EOF'
# Both quantities depend on ts. Variant: residuals of each on ts (linear, within dataset and
# prior), pooled, so that only the variation not explained by ts is correlated.
def resid_on_ts(d, col):
    return d.groupby("dataset")[[col, "ts"]].apply(
        lambda h: pd.Series(h[col] - np.polyval(np.polyfit(h.ts, h[col], 1), h.ts), index=h.index)).droplevel(0)


for prior in ["Short", "Long"]:
    g = spd[spd.prior == prior]
    r, p = stats.pearsonr(resid_on_ts(g, "xu_at_set").loc[g.index], resid_on_ts(g, "speed").loc[g.index])
    print(f"{prior}: rho of residuals on ts = {r:.3f} (p = {p:.2g}, 20 points, 12 residual degrees of freedom)")
EOF
cat > $TMPDIR/cells/partial_tp.py <<'EOF'
for prior in ["Short", "Long"]:
    g = spd[spd.prior == prior]
    r, p = stats.pearsonr(resid_on_ts(g, "speed").loc[g.index], resid_on_ts(g, "mean_tp").loc[g.index])
    print(f"{prior}: rho of residuals on ts (speed, mean tp) = {r:.3f} (p = {p:.2g})")

# Trial by trial, with speed and tp z-scored within each ts (the paper's control for their
# co-dependence on ts, Methods), in the benchmark-style variant above.
EOF
cat > $TMPDIR/cells/wrmse.py <<'EOF'
# Variant: RMSE weighted by the number of trials in each bin, as in the fit.
def wrmse(x, y, w):
    a, b, _, _ = rsg.weighted_fit(x, y, w)
    return float(np.sqrt(np.sum(w * (y - a - b * x) ** 2) / np.sum(w)))


enc["dWRMSE"] = [wrmse(PROJ[(r.dataset, r.prior == "Short")]["te"], PROJ[(r.dataset, r.prior == "Short")]["xu"], PROJ[(r.dataset, r.prior == "Short")]["w"])
                 - wrmse(PROJ[(r.dataset, r.prior == "Short")]["t"], PROJ[(r.dataset, r.prior == "Short")]["xu"], PROJ[(r.dataset, r.prior == "Short")]["w"])
                 for r in enc.itertuples()]
for prior, g in enc.groupby("prior", sort=False):
    print(f"Weighted RMSE, {prior}: Bayesian lower in {(g.dWRMSE < 0).sum()} of 4; differences " + ", ".join(f"{x:+.3f}" for x in g.dWRMSE))
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/partial.py $TMPDIR/cells/partial_tp.py $TMPDIR/cells/wrmse.py 2>&1 | tail -16
```

```
===== /tmp/claude-1001/cells/partial.py
Short: rho of residuals on ts = -0.195 (p = 0.41, 20 points, 12 residual degrees of freedom)
Long: rho of residuals on ts = 0.069 (p = 0.77, 20 points, 12 residual degrees of freedom)
===== /tmp/claude-1001/cells/partial_tp.py
Short: rho of residuals on ts (speed, mean tp) = 0.084 (p = 0.72)
Long: rho of residuals on ts (speed, mean tp) = -0.283 (p = 0.23)
===== /tmp/claude-1001/cells/wrmse.py
Weighted RMSE, Short: Bayesian lower in 3 of 4; differences -0.192, -0.424, +0.031, -0.052
Weighted RMSE, Long: Bayesian lower in 4 of 4; differences -0.204, -0.509, -0.103, -0.050
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -A14 "id: speed-vs-projection\|id: speed-predicts-tp\|id: encoding-bayes\|id: dfr-overlap\|id: pca-dim\|id: encoding-r2\|id: glm-prior" claims/000130/10.1016-j.neuron.2019.06.012.yaml | grep -v "^--$" | head -120
```

```
89:- id: glm-prior-ts
90-  statement: About 30% of neurons were modulated by elapsed time (27% in monkey H) and more than
91-    60% were sensitive to the prior (65% in monkey H), by a Poisson GLM of spike counts before
92-    Set compared by BIC.
93-  source: Results, Single-neuron response profiles; Figure 3E; Methods, Generalized linear model
94-  expected:
95-  - quantity: Fraction of units sensitive to the prior, monkey H
96-    value: 65
97-    tolerance: 6.5
98-    unit: percent
99-  - quantity: Fraction of units sensitive to ts (elapsed time), monkey H
100-    value: 27
101-    tolerance: 2.7
102-    unit: percent
103-  criterion: Units as selected above. Counts in the 80 ms before each of the Short prior's ts
112:- id: dfr-overlap-support
113-  statement: At the overlapping ts of 800 ms, firing rates differ between priors, with the
114-    largest difference during the support of the prior, between 480 and 800 ms after Ready.
115-  source: Results, Single-neuron response profiles; Figure 3C and 3D
116-  criterion: Per dataset, units as selected above, ts = 800 trials; per unit the difference of
[... 73 more lines not kept]
```

**Agent**

Outcomes stay as the criteria fix them; the variants go into notes. Now the trial-by-trial z-scored variant for speed-predicts-tp.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
c=nb.cells[58]
s=c.source
old="""rows = []
for e, th, name in DS:"""
new="""rows, trial_rows = [], []
for e, th, name in DS:"""
assert old in s; s=s.replace(old,new)
old="""        r, p = stats.pearsonr(sp, gg.tp)
"""
new="""        r, p = stats.pearsonr(sp, gg.tp)
        trial_rows += [{"dataset": name, "prior": "Short" if short else "Long", "ts": a, "tp": b, "speed": s_}
                       for a, b, s_ in zip(gg.ts, gg.tp, sp)]
"""
assert old in s; s=s.replace(old,new)
c.source=s
nbformat.write(nb,p)
EOF
cat > $TMPDIR/cells/zts.py <<'EOF'
# Variant: the paper's control for co-dependence on ts (Methods), trial by trial; speed and tp
# z-scored within each dataset, prior and ts, then correlated.
tt_ = pd.DataFrame(trial_rows)
for col in ["speed", "tp"]:
    tt_[f"z_{col}"] = tt_.groupby(["dataset", "prior", "ts"])[col].transform(lambda x: (x - x.mean()) / x.std())
zr = tt_.groupby(["dataset", "prior"], sort=False).apply(lambda h: pd.Series(stats.pearsonr(h.z_speed, h.z_tp), index=["r", "p"]))
print("Trial by trial, z-scored within ts:")
print(zr.round(3).to_string())
for prior, g in tt_.groupby("prior", sort=False):
    r, p = stats.pearsonr(g.z_speed, g.z_tp)
    print(f"{prior}, pooled over datasets: r = {r:.3f} (p = {p:.2g}, {len(g)} trials); negative in "
          f"{int((zr.loc[(slice(None), prior), 'r'] < 0).sum())} of 4, p < 0.05 and negative in "
          f"{int(((zr.loc[(slice(None), prior), 'r'] < 0) & (zr.loc[(slice(None), prior), 'p'] < 0.05)).sum())}")
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet $TMPDIR/cells/zts.py 2>&1 | tail -16
```

```
===== /tmp/claude-1001/cells/zts.py
Trial by trial, z-scored within ts:
                      r      p
dataset    prior              
Eye Right  Short -0.437  0.000
           Long  -0.251  0.002
Eye Left   Short -0.377  0.000
           Long  -0.232  0.004
Hand Right Short -0.261  0.005
           Long  -0.173  0.068
Hand Left  Short -0.203  0.018
           Long  -0.096  0.372
Short, pooled over datasets: r = -0.317 (p = 1.1e-12, 481 trials); negative in 4 of 4, p < 0.05 and negative in 4
Long, pooled over datasets: r = -0.201 (p = 5.5e-06, 502 trials); negative in 4 of 4, p < 0.05 and negative in 2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
p="rsg.py"; s=open(p).read()
i=s.index("def fit_gpfa("); j=s.index("def gpfa_transform(")
new='''def gpfa_folds(n: int, rng: np.random.Generator) -> np.ndarray:
    """Fold (0, 1 or 2) of each of `n` trials for 3-fold cross-validation."""
    return rng.permutation(n) % 3


def gpfa_cv_score(spiketrains, folds: np.ndarray, dim: int) -> float:
    """Summed test log-likelihood of GPFA with `dim` latents over the folds."""
    import contextlib
    import io
    import warnings

    import quantities as pq
    from elephant.gpfa import GPFA

    _quiet_elephant()
    total = 0.0
    with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):
        warnings.simplefilter("ignore")
        for k in range(3):
            train = [s for s, f in zip(spiketrains, folds) if f != k]
            test = [s for s, f in zip(spiketrains, folds) if f == k]
            m = GPFA(bin_size=BIN_MS * pq.ms, x_dim=dim, em_max_iters=GPFA_EM_ITERS)
            m.fit(train)
            total += m.score(test)
    return total


def gpfa_model(spiketrains, dim: int):
    """GPFA with `dim` latents fit on all trials. Its `fit_info["log_likelihoods"]` holds the
    training log-likelihood every fifth EM iteration (elephant's default)."""
    import contextlib
    import io
    import warnings

    import quantities as pq
    from elephant.gpfa import GPFA

    _quiet_elephant()
    with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):
        warnings.simplefilter("ignore")
        model = GPFA(bin_size=BIN_MS * pq.ms, x_dim=dim, em_max_iters=GPFA_EM_ITERS)
        model.fit(spiketrains)
    return model


def fit_gpfa(spiketrains, rng: np.random.Generator):
    """GPFA with the latent dimensionality from `GPFA_DIMS` chosen by 3-fold cross-validated
    log-likelihood. Returns the model fit on all trials, the chosen dimensionality, the
    cross-validated scores and the folds."""
    folds = gpfa_folds(len(spiketrains), rng)
    scores = {dim: gpfa_cv_score(spiketrains, folds, dim) for dim in GPFA_DIMS}
    best = max(scores, key=scores.get)
    return gpfa_model(spiketrains, best), best, scores, folds


'''
s=s[:i]+new+s[j:]
open(p,"w").write(s)
EOF
grep -n "freq_ll" $TMPDIR/dev/lib/python3.12/site-packages/elephant/gpfa/gpfa.py | head -3
```

```
138:    freq_ll : int, optional
139:        data likelihood is computed at every freq_ll EM iterations. freq_ll = 1
239:        freq_ll=5,
```

**Agent**

Now I'll restructure the GPFA cell so the variant can reuse the projection code, and draft the variant cell.

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
c=nb.cells[72]
c.source='''rng_gpfa = np.random.default_rng(6)
t_gpfa = time.time()


def gpfa_rows(name, g, lat):
    rows = []
    for short in [True, False]:
        mask = g.is_short.to_numpy() == short
        L = [lat[i] for i in np.flatnonzero(mask)]
        nb = max(x.shape[1] for x in L)
        mean = np.array([np.mean([x[:, k] for x in L if x.shape[1] > k], axis=0) for k in range(nb)])
        tt = np.arange(1, nb + 1) * rsg.BIN_MS
        ts_v = rsg.prior_ts(short)
        u = rsg.encoding_axis(mean, tt, min(ts_v), max(ts_v))
        xu = np.array([x[:, -1] @ u for x in L])
        ts_tr = g.ts.to_numpy()[mask]
        z = (xu - xu.mean()) / xu.std()
        var = np.array([z[ts_tr == t].var(ddof=1) for t in ts_v])
        mxu = np.array([xu[ts_tr == t].mean() for t in ts_v])
        rows.append({"dataset": name, "prior": "Short" if short else "Long", **{f"var_{t}": v for t, v in zip(ts_v, var)},
                     "quad_coef": np.polyfit(np.array(ts_v, float), var, 2)[0],
                     "mean_xu": mxu, "slope_xu": np.polyfit(np.array(ts_v, float), mxu, 1)[0]})
    return rows


GP, rows = {}, []
for e, th, name in DS:
    g = good[(good.is_eye == e) & (good.theta == th)]
    sts = rsg.estimation_spiketrains(spikes, units, g)
    model, dim, scores, folds = rsg.fit_gpfa(sts, rng_gpfa)
    lat = rsg.gpfa_transform(model, sts)
    GP[name] = {"lat": lat, "trials": g, "dim": dim, "sts": sts, "folds": folds, "scores": scores, "model": model}
    print(f"{name}: {len(g)} trials, latent dimensionality {dim} (cross-validated log-likelihood "
          + ", ".join(f"{k}: {v:.0f}" for k, v in scores.items()) + ")")
    rows += gpfa_rows(name, g, lat)
gp = pd.DataFrame(rows)
print(f"GPFA fits took {time.time() - t_gpfa:.0f} s")
print(gp.drop(columns=["mean_xu"]).to_string(index=False, float_format=lambda x: f"{x:.3g}"))
w = stats.wilcoxon(gp.quad_coef, alternative="less")
print(f"\\nQuadratic coefficient negative in {(gp.quad_coef < 0).sum()} of 8; one-tailed signed-rank p = {w.pvalue:.4f}")'''
nbformat.write(nb,p)
EOF
cat > $TMPDIR/cells/gpfa_var.py <<'EOF'
# Convergence: the training log-likelihood of each final model over its EM iterations
# (computed every fifth iteration), and the relative gain over the last 25 iterations.
print("Training log-likelihood of the final models:")
for name, G in GP.items():
    ll = np.array(G["model"].fit_info["log_likelihoods"], float)
    it = np.flatnonzero(~np.isnan(ll)) + 1
    ll = ll[~np.isnan(ll)]
    late = ll[it >= it[-1] - 25][0]
    print(f"   {name}: {len(G['model'].fit_info['log_likelihoods'])} iterations; at iteration 50 {ll[it == 50][0]:.0f}, "
          f"75 {ll[it == 75][0]:.0f}, {it[-1]} {ll[-1]:.0f}; gain over the last 25 iterations {100 * (ll[-1] - late) / abs(ll[-1]):.3f}%")

# Variant: a wider grid; 12 latents scored on the same folds. Where 12 wins, the variance test
# is repeated with the 12-latent model.
t_var = time.time()
rows_12, wins = [], []
for name, G in GP.items():
    s12 = rsg.gpfa_cv_score(G["sts"], G["folds"], 12)
    best = max({**G["scores"], 12: s12}.items(), key=lambda kv: kv[1])[0]
    print(f"{name}: cross-validated log-likelihood with 12 latents {s12:.0f} (chosen {G['dim']}: {G['scores'][G['dim']]:.0f}); best of 4, 8, 12: {best}")
    if best == 12:
        wins.append(name)
        lat12 = rsg.gpfa_transform(rsg.gpfa_model(G["sts"], 12), G["sts"])
        rows_12 += gpfa_rows(name, G["trials"], lat12)
    else:
        rows_12 += [r.to_dict() for _, r in gp[gp.dataset == name].iterrows()]
gp12 = pd.DataFrame(rows_12)
w12 = stats.wilcoxon(gp12.quad_coef, alternative="less")
print(f"With the grid 4, 8, 12 ({len(wins)} datasets refit with 12): quadratic coefficient negative in "
      f"{(gp12.quad_coef < 0).sum()} of 8; one-tailed signed-rank p = {w12.pvalue:.4f}")
inc12 = np.array([np.subtract(*rsg.increments(m)[::-1]) for m in gp12.mean_xu])
sg12 = gp12.pivot(index="dataset", columns="prior", values="slope_xu")
print(f"Mean projections with this grid: middle increment above extreme in {(inc12 > 0).sum()} of 8 "
      f"(two-sided p = {stats.wilcoxon(inc12).pvalue:.4f}); Short slope above Long in {int((sg12.Short > sg12.Long).sum())} of 4")
print(f"Variant took {time.time() - t_var:.0f} s")
EOF
cd $TMPDIR && time dev/bin/python runner.py --gpfa --quiet $TMPDIR/cells/gpfa_var.py 2>&1 | tail -20
```

```
===== /tmp/claude-1001/cells/gpfa_var.py
Training log-likelihood of the final models:
   Eye Right: 100 iterations; at iteration 50 -207547, 75 -207290, 100 -207119; gain over the last 25 iterations 0.083%
   Eye Left: 100 iterations; at iteration 50 -193177, 75 -192953, 100 -192802; gain over the last 25 iterations 0.078%
   Hand Right: 100 iterations; at iteration 50 -147699, 75 -147544, 100 -147431; gain over the last 25 iterations 0.077%
   Hand Left: 100 iterations; at iteration 50 -140599, 75 -140476, 100 -140383; gain over the last 25 iterations 0.066%
Eye Right: cross-validated log-likelihood with 12 latents -173639 (chosen 8: -173783); best of 4, 8, 12: 12
Eye Left: cross-validated log-likelihood with 12 latents -163631 (chosen 8: -163759); best of 4, 8, 12: 12
Hand Right: cross-validated log-likelihood with 12 latents -123674 (chosen 8: -123805); best of 4, 8, 12: 12
Hand Left: cross-validated log-likelihood with 12 latents -114716 (chosen 8: -114858); best of 4, 8, 12: 12
With the grid 4, 8, 12 (4 datasets refit with 12): quadratic coefficient negative in 5 of 8; one-tailed signed-rank p = 0.1250
Mean projections with this grid: middle increment above extreme in 8 of 8 (two-sided p = 0.0078); Short slope above Long in 4 of 4
Variant took 168 s

real	5m54.355s
user	20m53.338s
sys	0m0.576s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && python3 - <<'EOF'
s=open("partial.py").read()
s=s.replace('(p = {p:.2g}, 20 points, 12 residual degrees of freedom)','(nominal p = {p:.2g}, not adjusted for the 8 fitted lines)')
open("partial.py","w").write(s)
s=open("partial_tp.py").read()
s=s.replace('(p = {p:.2g})")','(nominal p = {p:.2g})")')
s=s.replace("""
# Trial by trial, with speed and tp z-scored within each ts (the paper's control for their
# co-dependence on ts, Methods), in the benchmark-style variant above.
""","")
open("partial_tp.py","w").write(s)
EOF
cat $TMPDIR/cells/partial_tp.py; cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
C="/tmp/claude-1001/cells/"
rd=lambda f: open(C+f).read().strip()
def code(src, tag):
    c=nbformat.v4.new_code_cell(src); c.metadata["tags"]=[tag]; return c
# sanity: check expected cells
assert nb.cells[65].metadata["tags"]==["claim:alt-transient-parallel"]
nb.cells[65].source=rd("transient.py")
ins=[(73,code(rd("gpfa_var.py"),"claim:gpfa-variance-inverted-u")),
     (68,code(rd("threshold.py"),"claim:alt-threshold-monotonic")),
     (62,code(rd("speed_null.py"),"claim:alt-speed-unmodulated")),
     (58,code(rd("partial_tp.py")+"\n\n"+rd("zts.py"),"claim:speed-predicts-tp")),
     (52,code(rd("partial.py"),"claim:speed-vs-projection")),
     (43,code(rd("wrmse.py"),"claim:encoding-bayes-beats-linear")),
     (40,code(rd("enc_norm.py"),"claim:encoding-r2")),
     (36,code(rd("pca_norm.py"),"claim:pca-dimensionality")),
     (33,code(rd("dfr_boot.py"),"claim:dfr-overlap-support")),
     (29,code(rd("glm_null.py"),"claim:glm-prior-ts"))]
for after,c in ins:  # descending order
    nb.cells.insert(after+1,c)
nbformat.write(nb,p)
for i,c in enumerate(nb.cells):
    print(i,c.cell_type,c.metadata.get("tags"),c.source[:60].replace("\n"," | "))
EOF
```

```
for prior in ["Short", "Long"]:
    g = spd[spd.prior == prior]
    r, p = stats.pearsonr(resid_on_ts(g, "speed").loc[g.index], resid_on_ts(g, "mean_tp").loc[g.index])
    print(f"{prior}: rho of residuals on ts (speed, mean tp) = {r:.3f} (nominal p = {p:.2g})")
0 markdown None # Reproducing Sohn et al. (2019) from dandiset 000130 |  | Paper
1 code None import os | import time | import warnings |  | import matplotlib.pyp
2 markdown None ## Data check |  | Each check of the metadata against the values
3 code ['sanity'] for key, f in [("train", S), ("test", T)]: |     print(f"{key}
4 markdown None The dandiset summary says one subject (Rhesus monkey) and 2 
5 code ['sanity'] c = trials[trials.set_time.notna() & trials.go_time.notna()]
6 markdown None `ts` is the nominal interval; the event times give intervals
7 code ['sanity'] print("Units: rate over the observed intervals, spikes/s") | p
8 markdown None The 48 units kept by the Methods' rate rule match the paper'
9 code ['sanity'] # Do spikes share the clock of the trial table? Decode "befo
10 markdown None Decoding of "before against after" is best at an offset of +
11 markdown None ## Behaviour |  | ### beh-slopes |  | > Regression slopes of tp on t
12 code ['claim:beh-slopes'] rows = [] | for e, th, name in DS: |     for short in [True, Fal
13 code ['claim:beh-slopes'] fig, axes = plt.subplots(1, 4, figsize=(14, 3.4), sharey=Tru
14 markdown None **Result: not reproduced.** Six of the 8 slopes lie between 
15 markdown None ### beh-overlap-prior |  | > At the overlapping ts of 800 ms, bi
[... 73 more lines not kept]
```

**Agent**

Cells are in place. Now I'll update the conclusion cells and summary to the new numbers (from the dev run; I'll check them against the clean run afterwards).

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
def app(i, start, text):
    c=nb.cells[i]; assert c.cell_type=="markdown" and c.source.startswith(start), (i, c.source[:40])
    c.source=c.source.rstrip()+" "+text
app(31,"**Result: not reproduced.** By the GLM","""Both fractions are far above chance. With the prior labels shuffled within effector and direction, 0 to 8.3% of units pass the prior test; with the labels shifted along the session by 50 to 200 trials, which keeps the blocks of the priors, 2.1 to 14.6%. With the time points shuffled within trials, 0 to 2.1% pass the ts test in either prior. Counting ts dependence in either prior's test gives 45.8%; the Short test alone gives 31.2% and the Long test alone 33.3%, both still above 27 +/- 2.7%.""")
app(36,"**Result: reproduced.** At ts = 800","""Over 200 bootstrap samples of trials the peak is in 480 to 640 ms in 192 and in 800 to 960 ms in 8, so it lies within 480 to 800 ms in 96% of samples.""")
app(40,"**Result: not reproduced.** Two components","""The count depends on normalisation, which the Methods do not mention. With rates z-scored per unit, 3 or 4 components reach 75% in the estimation epoch and 6 to 10 in the production epoch, so all 8 values are in range; with soft normalisation (range plus 5 spikes/s) 6 of 8 are (production 4 in both eye datasets). The outcome is judged on unnormalised rates, as the claims file fixed before the analysis.""")
app(45,"**Result: reproduced.** Under reading (a)","""With normalised rates (3 or 4 PCs) R2 stays above 0.94 in every dataset-prior (Hand Left 0.984 and 0.975 with soft normalisation, 0.990 and 0.960 z-scored), but the R2 on u exceeds that of 95% of random axes in 2 of 8 dataset-priors with soft normalisation and in 0 of 8 with z-scoring. The match to te is reproduced; its specificity to u is not shown in this session.""")
app(49,"**Result: partially reproduced.** The Bayesian model has","""With the RMSE weighted by trial counts, as in the fit, the counts are the same (Long 4 of 4, Short 3 of 4, Hand Right Short +0.031). In the matched control period of the Long prior (short-in-long-control) the Bayesian model is also better in 3 of 4 datasets, so in this session its advantage is not specific to the support of the prior.""")
app(59,"**Result: partially reproduced.** Larger projections","""Both quantities change with ts. With the residuals of each on ts within each dataset and prior, the correlation is -0.195 for Short and +0.069 for Long (nominal p = 0.41 and 0.77), so across conditions the relation is carried by their common dependence on ts. The paper's control for this, z-scoring within ts, applies to single-trial GPFA states of the production epoch, which are not computed here.""")
app(67,"**Result: partially reproduced.** Faster production","""With the residuals on ts within each dataset and prior the correlation is +0.084 (Short) and -0.283 (Long), nominal p = 0.72 and 0.23. Trial by trial, with speed and tp z-scored within each ts as in the paper's control, faster trials go with shorter tp: r = -0.317 (Short, 481 trials, p = 1.1e-12) and -0.201 (Long, 502 trials, p = 5.5e-06), negative in all 8 dataset-priors and with p < 0.05 in 6 (4 Short, 2 Long).""")
c=nb.cells[71]; assert c.source.startswith("**Result: reproduced by the paper's test")
c.source="""**Result: reproduced by the paper's test, which cannot detect an effect here.** The signed-rank test
over 4 datasets gives p = 0.125 for each prior, the smallest value it can give, so the outcome
carries no evidence for the absence of modulation. All 8 slopes of speed on time are positive, but
noise alone produces positive slopes of this size: later bins average fewer trials, and noisier
rates give larger steps. For units firing as Poisson processes at constant rates, with the same
trials and Set times, the mean null slope is above the observed slope in all 8 dataset-priors, and
no observed slope exceeds the null's 95th percentile. With only the trials of the longest ts, which
last the whole support, the slopes are -0.106 to +0.529 per 100 ms and fall outside the null's 95%
range in 1 of 8 (Hand Right Long, below it). The bootstrap intervals over trials are biased upward
(the point estimate is below the interval in 2 of 8) and are not used. This session shows no speed
modulation beyond what noise produces, and the test has little power to show one."""
app(74,"**Result: not reproduced.** For the longest ts","""The result holds for the longest ts with other numbers of components: p = 0.016 with 60% of the variance, 0.039 with 90%, 0.023 in the full space of 48 units and 0.039 with z-scored rates (75%); with soft-normalised rates it is 0.055. For the shortest ts p is 0.078 to 0.742 across these variants.""")
app(79,"**Result: not reproduced.** With the components","""In the eye datasets, with 1 component (16 curves), the minima are crossings: the distance at Go is more than 10 times the minimum in 5 of these curves. Requiring at least 2 components gives a median minimum 230 ms before Go, and at least 3 gives 70 ms before Go, within the 200 ms of a partial reproduction. The outcome is judged on the criterion's 60% of the variance.""")
app(84,"**Result: not reproduced.** The quadratic","""Cross-validation does not settle the dimensionality: 12 latents, scored on the same folds as a variant, beat 8 in all 4 datasets. With 12 latents the quadratic coefficient is negative in 5 of 8 and p = 0.125, the same result. After 100 EM iterations the training log-likelihood was still rising, by 0.066 to 0.083% over the last 25 iterations, so the fits are close to convergence but not at it.""")
app(87,"**Result: reproduced.** The mean single-trial","""With 12 latents the middle increments exceed the extreme ones in 8 of 8 (p = 0.0078) and the Short slope is higher in 4 of 4.""")
s=nb.cells[88].source
reps=[("| pca-dimensionality | Not reproduced (2 PCs in the estimation epoch) |","| pca-dimensionality | Not reproduced (2 PCs in the estimation epoch; 8 of 8 in range with z-scored rates, a variant) |"),
("| encoding-r2 | Reproduced (0.998 and 0.996, Hand Left), not specific to u in 5 of 8 |","| encoding-r2 | Reproduced (0.998 and 0.996, Hand Left); above 95% of random axes in only 3 of 8 |"),
("| glm-prior-ts | Not reproduced (75.0% and 45.8% against 65% and 27%) |","| glm-prior-ts | Not reproduced (75.0% and 45.8% against 65% and 27%; chance at most 14.6%) |"),
("| alt-speed-unmodulated | Reproduced by the paper's test, which cannot detect an effect; all 8 slopes positive |","| alt-speed-unmodulated | Reproduced by the paper's test, which cannot detect an effect; slopes no larger than noise gives |"),
("| rnn-curved-manifold, rnn-perturbation | Blocked: model results, no data in the dandiset |","| rnn-curved-manifold, rnn-perturbation | Blocked: data missing (the trained networks and their code are not public) |"),
("""from 4 and 8 only, with 100 EM iterations. The outlier flag is the file's.""","""from 4 and 8 only, with 100 EM iterations; 12 latents score better, and the conclusions do not change
with them. The outlier flag is the file's. Rates are not normalised before PCA, as the Methods do not
say; z-scoring them brings the PCA dimensionality into the paper's ranges and removes the encoding
axis's advantage over random axes."""),
]
for a,b in reps:
    assert a in s, a
    s=s.replace(a,b)
nb.cells[88].source=s
c=nb.cells[0]
a="| rnn-curved-manifold, rnn-perturbation: recurrent network models | Fig. 7 | Blocked (no model in the dandiset; code on request) |"
assert a in c.source
c.source=c.source.replace(a,"| rnn-curved-manifold, rnn-perturbation: recurrent network models | Fig. 7 | Blocked, data missing (no model in the dandiset; code on request) |")
nbformat.write(nb,p)
EOF
sed -i 's/runtime_minutes: 7/runtime_minutes: 10/' entry.yaml; cat README.md
```

```
# Sohn, Narain, Meirhaeghe & Jazayeri (2019) from dandiset 000130

Tests the findings of [Sohn et al. (2019)](https://doi.org/10.1016/j.neuron.2019.06.012) that can
be tested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), the Neural
Latents Benchmark's DMFC_RSG set. It holds one recording session of monkey H in the Ready-Set-Go
task, with 54 units from dorsomedial frontal cortex. The paper uses 17 sessions of monkey H and 12
of monkey G; monkey G and the recurrent network models are not in the dandiset.

| Claim | Outcome |
|---|---|
| Slopes of tp on ts between 0 and 1 in every condition | Not reproduced |
| Opposite biases of the two priors at ts = 800 ms | Not reproduced |
| Smaller tp increments at the extremes of the prior | Reproduced |
| Smaller slopes for the Long prior | Reproduced |
| The Bayesian observer captures bias and variance | Partially reproduced |
| 65% of units prior-dependent and 27% ts-dependent | Not reproduced |
| Prior difference at 800 ms largest during the support | Reproduced |
| 3 to 4 and 5 to 10 PCs explain 75% of the variance | Not reproduced |
| Projections on the encoding axis match the Bayesian estimate | Reproduced |
| Bayesian model better than linear for the projections | Partially reproduced |
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p="README.md"; s=open(p).read()
reps=[("| Speed unmodulated during the support | Reproduced (the test cannot detect an effect; the speed rises in all 8) |","| Speed unmodulated during the support | Reproduced (the test cannot detect an effect; the slopes are no larger than noise gives) |"),
("| Recurrent network models (two claims) | Blocked |","| Recurrent network models (two claims) | Blocked: data missing |"),
("It takes about seven minutes, most of it fitting GPFA.","It takes about ten minutes, most of it fitting GPFA."),
("population rates with attrition, PCA, the encoding\n  axis,","population rates with attrition, PCA and normalisation, the encoding\n  axis,")]
for a,b in reps:
    assert a in s, a; s=s.replace(a,b)
open(p,"w").write(s)
EOF
sed -n 1,30p rsg.py
```

```
"""Loading and measures for the Ready-Set-Go data of dandiset 000130.

Sohn, Narain, Meirhaeghe & Jazayeri (2019), Neuron, doi:10.1016/j.neuron.2019.06.012.

The dandiset is the DMFC_RSG set of the Neural Latents Benchmark: one session of monkey H
(Haydn, 2016-12-11). The train file holds the trial table with every task variable and the
spike times of 54 units; the test file holds 283 further trials without task variables and
only 40 of the units. Analyses use the train file. Files are streamed from the archive at the
pinned version; nothing is written to disk.

Where the parameters come from:

- From the paper's STAR Methods: units kept with a mean rate of at least 1 spike/s and at least
  5 trials per condition (`MIN_RATE`, `MIN_TRIALS`); 20 ms bins and a 40 ms Gaussian kernel for
  population rates (`BIN_MS`, `SMOOTH_MS`, read here as the kernel's SD); attrition in the
  estimation epoch; production rates up to the shortest tp of each ts; PCA keeping the
  components that explain 75% of the variance (`VAR_KEPT`); the encoding axis from difference
  vectors every 20 ms; the 80 ms GLM window before Set (`GLM_WINDOW_MS`) and BIC comparison;
  the Bayesian observer with scalar measurement and production noise, a uniform prior, the
  posterior mean, and an offset per prior; GPFA on single trials with cross-validation.
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p="rsg.py"; s=open(p).read()
a="""  read as SD; rates averaged per 20 ms bin and then smoothed; no normalisation of rates before
  PCA; difference"""
b="""  read as SD; rates averaged per 20 ms bin and then smoothed; no normalisation of rates before
  PCA (soft normalisation and z-scoring, `unit_scale`, are variants); difference"""
assert a in s; open(p,"w").write(s.replace(a,b))
EOF
cd  && time python tools/entry.py all entries/000130-sohn-2019 2>&1 | tail -30
```

```
for _ in range(1000):
                v = rng_norm.standard_normal(X.shape[1])
                rand.append(rsg.weighted_fit(te, X[sel] @ (v / np.linalg.norm(v)), w)[2])
            enc_rows.append({"dataset": name, "prior": "Short" if short else "Long", "normalisation": how, "PCs": X.shape[1],
                             "R2_bayes": r2, "random_R2_median": np.median(rand), "frac_random_above": np.mean(np.array(rand) >= r2)})
dims_norm = pd.DataFrame(rows)
print(dims_norm.to_string(index=False))
for how, g in dims_norm.groupby("normalisation"):
    print(f"{how}: in range (estimation 3 or 4, production 5 to 11) {g.est_PCs_75.between(3, 4).sum() + g.prod_PCs_75.between(5, 11).sum()} of 8")
enc_norm = pd.DataFrame(enc_rows)
------------------


[31m---------------------------------------------------------------------------[39m
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[19][39m[32m, line 20[39m
[32m     16[39m             lo, hi = min(rsg.prior_ts(short)), max(rsg.prior_ts(short))
[32m     17[39m             X, t = pe(E[short][[33m"rate"[39m] / se), E[short][[33m"t"[39m]
[32m     18[39m             u = rsg.encoding_axis(X, t, lo, hi)
[32m     19[39m             sel = (t >= lo - [32m1e-6[39m) & (t <= hi + [32m1e-6[39m)
[... 14 more lines not kept]
```

**Agent**

The normalisation cell uses the encoding results, which come later in the notebook. I'll split it: dimensionality in the PCA section, the encoding-axis part in the encoding section.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
assert nb.cells[39].source.startswith("# Variants: rates normalised") and nb.cells[44].source.startswith('print("Encoding axis with normalised')
nb.cells[39].source='''# Variants: rates normalised per unit before PCA (soft normalisation, and z-scoring), with the
# components reaching 75% of the variance. Estimation and production scales are taken from the
# trajectories that enter each PCA.
rows = []
for e, th, name in DS:
    E, P = EST[name], PROD[name]
    est_m = [E[True]["rate"], E[False]["rate"]]
    prod_m = [v["rate"] for v in P["traj"].values()]
    for how in ["soft", "z"]:
        se, sp = rsg.unit_scale(est_m, how), rsg.unit_scale(prod_m, how)
        pe = rsg.PCA([m / se for m in est_m])
        pp = rsg.PCA([m / sp for m in prod_m])
        E[f"pca_{how}"], E[f"scale_{how}"] = pe, se
        rows.append({"dataset": name, "normalisation": how, "est_PCs_75": pe.n, "prod_PCs_75": pp.n})
dims_norm = pd.DataFrame(rows)
print(dims_norm.to_string(index=False))
for how, g in dims_norm.groupby("normalisation"):
    print(f"{how}: in range (estimation 3 or 4, production 5 to 11) {g.est_PCs_75.between(3, 4).sum() + g.prod_PCs_75.between(5, 11).sum()} of 8")'''
nb.cells[44].source='''# Variant: the encoding axis in the PC spaces of normalised rates (pca-dimensionality).
rng_norm = np.random.default_rng(9)
enc_rows = []
for e, th, name in DS:
    E = EST[name]
    for how in ["soft", "z"]:
        pe, se = E[f"pca_{how}"], E[f"scale_{how}"]
        for short in [True, False]:
            lo, hi = min(rsg.prior_ts(short)), max(rsg.prior_ts(short))
            X, t = pe(E[short]["rate"] / se), E[short]["t"]
            u = rsg.encoding_axis(X, t, lo, hi)
            sel = (t >= lo - 1e-6) & (t <= hi + 1e-6)
            w, te = E[short]["n"][sel], PROJ[(name, short)]["te"]
            r2 = rsg.weighted_fit(te, X[sel] @ u, w)[2]
            rand = []
            for _ in range(1000):
                v = rng_norm.standard_normal(X.shape[1])
                rand.append(rsg.weighted_fit(te, X[sel] @ (v / np.linalg.norm(v)), w)[2])
            enc_rows.append({"dataset": name, "prior": "Short" if short else "Long", "normalisation": how, "PCs": X.shape[1],
                             "R2_bayes": r2, "random_R2_median": np.median(rand), "frac_random_above": np.mean(np.array(rand) >= r2)})
enc_norm = pd.DataFrame(enc_rows)
''' + nb.cells[44].source
nbformat.write(nb,p)
EOF
cd $TMPDIR && dev/bin/python runner.py --quiet 2>&1 | tail -3; dev/bin/python - <<'EOF'
# show the enc_norm cell output quickly
EOF
cd  && time python tools/entry.py all entries/000130-sohn-2019 2>&1 | tail -15
```

```
Installed kernelspec registry-000130-sohn-2019 in executed/000130-sohn-2019/.venv/share/jupyter/kernels/registry-000130-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (417 s)

real	7m4.927s
user	23m41.244s
sys	0m3.510s
```

**Agent**

The full run passes in 417 s. I'll reset the runtime back to seven minutes and check every new number in the executed copy against the conclusions.

**Agent calls Bash**

```bash
sed -i 's/runtime_minutes: 10/runtime_minutes: 7/' entries/000130-sohn-2019/entry.yaml; sed -i 's/It takes about ten minutes/It takes about seven minutes/' entries/000130-sohn-2019/README.md
python3 - <<'EOF'
import nbformat
nb=nbformat.read("executed/000130-sohn-2019/reproduce_sohn_2019.ipynb",4)
for i in [30,35,39,44,48,51,58,65,70,73,77,81,83,86]:
    c=nb.cells[i]
    out="".join(o.get("text","") for o in c.outputs if o.output_type=="stream")
    print("=====",i,c.metadata.get("tags")); print(out[-2500:])
EOF
```

```
===== 30 ['claim:glm-prior-ts']
Fractions of units passing the BIC rule with shuffled labels (%):
 shuffle  prior_dep_pct  ts_dep_short_pct  ts_dep_long_pct  ts_dep_either_pct
       0            0.0               2.1              0.0                2.1
       1            4.2               0.0              0.0                0.0
       2            0.0               0.0              0.0                0.0
       3            8.3               0.0              0.0                0.0
       4            0.0               2.1              0.0                2.1

Observed: prior 75.0%, ts in Short 31.2%, ts in Long 33.3%, ts in either 45.8%
Shuffled, maximum over 5: prior 8.3%, ts in either 2.1%

Prior labels shifted along the session, block structure kept:
   shifted by 50 trials: labels unchanged on 56% of trials; prior-dependent 10.4%
   shifted by 100 trials: labels unchanged on 53% of trials; prior-dependent 14.6%
   shifted by 200 trials: labels unchanged on 48% of trials; prior-dependent 2.1%
Prior blocks in the session (runs of one prior over used trials): 87; median length 9 trials

===== 35 ['claim:dfr-overlap-support']
Bin of the largest mean RMS over 200 bootstrap samples of trials (ms after Ready):
[... 179 more lines not kept]
```

**Agent**

All numbers match the conclusions, except the GPFA log-likelihood gain, which is now 0.066 to 0.084% (I wrote 0.083). Fixing that, then checking the schema for the verifications block.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && $TMPDIR/dev/bin/python - <<'EOF'
import nbformat
p="reproduce_sohn_2019.ipynb"
nb=nbformat.read(p,4)
c=nb.cells[84]; assert "0.066 to 0.083%" in c.source
c.source=c.source.replace("0.066 to 0.083%","0.066 to 0.084%")
nbformat.write(nb,p)
EOF
cd ../..; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['verifications'],indent=1))
print(json.dumps(s.get('\$defs',s.get('definitions',{})).get('proposed', s['properties']['outcomes']['items']['properties'].get('proposed')),indent=1))"
```

```
{
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
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 84 more lines not kept]
```

**Agent**

Now the attempt record: notes for the claims with new outputs, the RNN blocking reason, and the round-1 verification block.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p="attempts/000130-sohn-2019-01.yaml"; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""    to 77.1% at p < 0.01 and 0.05).
""","""    to 77.1% at p < 0.01 and 0.05). Chance levels by the same BIC rule are far lower; prior labels
    shuffled within effector and direction give 0 to 8.3% and labels shifted along the session by 50
    to 200 trials, which keeps the prior blocks, 2.1 to 14.6%; time points shuffled within trials
    give 0 to 2.1% ts-dependent. The ts test in the Short prior alone gives 31.2% and in the Long
    prior alone 33.3%, both above 27 +/- 2.7%.
""")
rep("""  - The GLM design with attrition (rows for every trial whose Set comes after each time point) is
    read from the Methods; the paper's code was not available.
""","""  - The GLM design with attrition (rows for every trial whose Set comes after each time point) is
    read from the Methods; the paper's code was not available.
  - The Long prior's ts test uses the Long ts as time points (800 to 1200 ms after Ready); Eq. 3 of
    the paper does not say which time points were used, and a unit counts as ts-dependent when
    either prior's test finds it.
""")
rep("""    mean is also high just after Set (6.07 at 800 to 960 ms).
""","""    mean is also high just after Set (6.07 at 800 to 960 ms). Over 200 bootstrap samples of trials
    the peak is in 480 to 640 ms in 192 and in 800 to 960 ms in 8 (96% within 480 to 800 ms).
""")
rep("""    86 to 90%), and 2, 2, 5 and 4 in the production epoch; 1 of 8 values is in range. The activity is
    lower dimensional than reported.
""","""    86 to 90%), and 2, 2, 5 and 4 in the production epoch; 1 of 8 values is in range. The count
    depends on normalisation, which the Methods do not mention; with rates z-scored per unit (a
    variant) the counts are 3 or 4 and 6 to 10, all 8 in range, and with soft normalisation (range
    plus 5 spikes/s) 6 of 8 are in range. The outcome is judged on unnormalised rates, as the
    claims file fixed.
""")
rep("""    dataset-priors (Hand Right Long and both Hand Left), so the paper's statement that the match is
    specific to u (Figure S5) holds only for those.
""","""    dataset-priors (Hand Right Long and both Hand Left), so the paper's statement that the match is
    specific to u (Figure S5) holds only for those. With normalised rates (3 or 4 PCs) R2 stays above
    0.94 in every dataset-prior, and u beats 95% of random axes in 2 of 8 (soft normalisation) and 0
    of 8 (z-scored).
""")
rep("""    0.99 against 0.80). Differences are 0.045 to 0.573 spikes/s.
""","""    0.99 against 0.80). Differences are 0.045 to 0.573 spikes/s. With the RMSE weighted by trial
    counts, as in the fit, the counts are the same. In the matched control period of the Long prior
    (short-in-long-control) the Bayesian model is also better in 3 of 4 datasets, so in this
    session the advantage is not specific to the support of the prior.
""")
rep("""    dataset -0.759 and -0.779, and the speed divided by mean tp gives -0.917 and -0.923.
""","""    dataset -0.759 and -0.779, and the speed divided by mean tp gives -0.917 and -0.923. Both
    quantities change with ts; with the residuals of each on ts within dataset and prior the
    correlation is -0.195 (Short) and +0.069 (Long), so the pooled relation is carried by the common
    dependence on ts. The paper's control (z-scoring within ts) is on single-trial GPFA states of
    the production epoch, not computed here.
""")
rep("""    conditions with p < 0.05.
""","""    conditions with p < 0.05. With speed and tp z-scored within each ts trial by trial, as in the
    paper's control, r = -0.317 (Short, 481 trials, p = 1.1e-12) and -0.201 (Long, 502 trials, p =
    5.5e-06), negative in 8 of 8 dataset-priors and p < 0.05 in 6. Residuals on ts of the 20 condition
    means give +0.084 and -0.283.
""")
rep("""  notes: Judged on the paper's test as the claims file fixes; signed-rank p = 0.125 for each prior,
    the smallest a test over 4 datasets can give. The data show modulation; all 8 slopes are positive
    (speed rising 13 to 24% of its mean per 100 ms of the support) and all 8 bootstrap intervals over
    trials exclude zero. The outcome reflects the test's lack of power at this sample size, not an
    absence of modulation in this session.
""","""  notes: Judged on the paper's test as the claims file fixes; signed-rank p = 0.125 for each prior,
    the smallest a test over 4 datasets can give, so the outcome carries no evidence for the absence
    of modulation. All 8 slopes are positive, but noise produces slopes of this size, as later bins
    average fewer trials. For Poisson units at constant rates with the same trials and Set times,
    the mean null slope is above the observed one in 8 of 8 and no observed slope exceeds the null's
    95th percentile. With only the trials of the longest ts, which last the whole support, slopes
    are -0.106 to +0.529 per 100 ms and outside the null's 95% range in 1 of 8 (below it). The
    bootstrap intervals over trials are biased upward (the point estimate is below the interval in
    2 of 8) and are not used. The session shows no modulation beyond what noise produces.
""")
rep("""    for the shortest ts p = 0.078 (6 of 8 rising, median +26.7%). The PCA kept 1 to 4 components, one
    in Eye Left.
""","""    for the shortest ts p = 0.078 (6 of 8 rising, median +26.7%). The PCA kept 1 to 4 components, one
    in Eye Left. For the longest ts p = 0.016 with 60% of the variance, 0.039 with 90%, 0.023 in the
    full space and 0.039 with z-scored rates; with soft-normalised rates 0.055.
""")
rep("""    which would meet the criterion, so the outcome depends on the number of components; with one
    component (eye datasets) the distance reaches zero where trajectories cross.
""","""    which would meet the criterion, so the outcome depends on the number of components. With one
    component (eye datasets, 16 curves) the minima are crossings; the distance at Go is more than 10
    times the minimum in 5 of these. With at least 2 components the median minimum is 230 ms before
    Go, with at least 3 it is 70 ms before Go.
""")
rep("""    candidate. GPFA values vary in the third significant digit between runs; the counts and p values
    did not change over four runs.
""","""    candidate. GPFA values vary in the third significant digit between runs; the counts and p values
    did not change over four runs. 12 latents, scored on the same folds as a variant, beat 8 in all 4
    datasets; with them the coefficient is negative in 5 of 8, p = 0.125. After 100 EM iterations the
    training log-likelihood still rose by 0.066 to 0.084% over the last 25 iterations.
""")
rep("""    0.0625), the paper's values; the mean rises with ts in 8 of 8.
""","""    0.0625), the paper's values; the mean rises with ts in 8 of 8. With 12 latents, 8 of 8 (p =
    0.0078) and 4 of 4.
""")
rep("""  blocked_by: other
  notes: The claim is about recurrent networks trained in silico. It uses no recorded data, so the
    dandiset cannot bear on it, and the trained networks and the training code are not public (the
    code is available from the corresponding author on request).
""","""  blocked_by: data_missing
  notes: The claim is about recurrent networks trained in silico. The dandiset holds only the two
    NWB files of spikes and trials, and the trained networks and the training code are not public
    (the code is available from the corresponding author on request). Training new networks from
    the Methods would be a new study, not a test against this data.
""")
rep("""- claim: rnn-perturbation
  outcome: blocked
  blocked_by: other
""","""- claim: rnn-perturbation
  outcome: blocked
  blocked_by: data_missing
""")
open(p,"w").write(s)
EOF
grep -n "^findings:\|^verifications" attempts/000130-sohn-2019-01.yaml; tail -5 attempts/000130-sohn-2019-01.yaml
```

```
301:findings:
  statement: The paper's analysis code is available only on request. The code the dandiset links
    (nlb_tools) loads the data and scores benchmark models, and holds none of the paper's analyses.
- kind: paper_inconsistency
  statement: The Results give the GPFA sessions as N = 48 for monkey H and N = 107 for monkey G, the
    Methods as N = 48 in H and 96 in G.
```

**Agent**

Now the round-1 verifications block, with the verifier's reasons in its own words and my responses.

**Agent calls Bash**

```bash
cat >> attempts/000130-sohn-2019-01.yaml <<'EOF'
verifications:
- date: '2026-10-14'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's accepted manuscript (PMC6805134). The verifier
    checked the archive's asset list and metadata for the blocked claims and ran synthetic checks of
    weighted_slope, PCA, encoding_axis, increments, BayesObserver and attrition_rates.
  results:
  - claim: beh-slopes
    agrees: true
    outcome: not_reproduced
    reason: 6 of 8 slopes lie between 0 and 1. Eye Right Short is 1.110 [1.014, 1.206] and Eye Left
      Short is 1.011.
    response: No change.
  - claim: beh-overlap-prior
    agrees: true
    outcome: not_reproduced
    reason: The median of tp - 800 is +28.3 ms for Short and +47.6 ms for Long, so both are positive,
      and p = 0.073. Removing the 18 ms tp offset would not change either sign.
    response: No change.
  - claim: beh-sigmoid-increments
    agrees: true
    outcome: reproduced
    reason: The middle increment is larger in 7 of 8 conditions, two-sided signed-rank p = 0.0156.
    response: No change.
  - claim: beh-long-more-bias
    agrees: true
    outcome: reproduced
    reason: The Long slope is below the Short slope in 4 of 4 datasets (weighted and unweighted).
    response: No change.
  - claim: beh-bayes-model
    agrees: true
    outcome: partially_reproduced
    reason: The SD correlation is positive in 4 of 4, but bias R2 >= 0.8 holds in only 2 of 4 (Eye
      Right 0.12, Eye Left 0.67). In the Eye datasets wm sits near its lower bound (0.013, 0.025),
      consistent with slopes of about 1 in the behaviour itself.
    response: No change. Tables S1 to S3 remain unavailable, so wm and wp are still not compared
      with the paper's.
  - claim: glm-prior-ts
    agrees: true
    outcome: not_reproduced
    reason: Prior-dependent 75.0% (interval 61 to 85%) against 65 +/- 6.5; ts-dependent 45.8%
      (interval 33 to 60%) against 27 +/- 2.7. Neither is within tolerance. The Long ts GLM uses the
      Long ts times, and Eq. 3 is ambiguous on this point; requiring ts dependence in either of two
      tests raises the rate, and the notebook computes no false-positive baseline.
    response: Added chance levels by the same BIC rule, with the prior labels shuffled within
      effector and direction (0 to 8.3%), shifted along the session to keep the prior blocks (2.1 to
      14.6%), and with time points shuffled within trials (0 to 2.1% ts-dependent). Reported the ts
      fractions of each prior's test alone (31.2% and 33.3%, both still above tolerance) and recorded
      the choice of Long time points as a deviation. Outcome unchanged.
  - claim: dfr-overlap-support
    agrees: true
    outcome: reproduced
    reason: The largest mean RMS, 6.86 spikes/s, is in the 480 to 640 ms bin and exceeds the
      shuffled-maximum 95th percentile of 3.11. The margin is thin; neighbouring bins reach 5.97 and
      6.07, and the per-dataset peaks fall in three different bins. A bootstrap over trials of the
      argmax bin is missing.
    response: Added the bootstrap over trials; the peak is in 480 to 640 ms in 192 of 200 samples and
      in 800 to 960 ms in 8. Outcome unchanged.
  - claim: pca-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: 1 of 8 values is in range. The paper ran PCA on units pooled across 17 sessions; here 48
      simultaneously recorded units with unnormalised rates yield 2 PCs per epoch, which likely drives
      the failure. It asked for a variant with soft-normalised or z-scored rates.
    response: Added both variants (rsg.unit_scale). With z-scored rates all 8 counts are in range, with
      soft normalisation 6 of 8. The outcome stays as the claims file's criterion fixes it
      (unnormalised rates, chosen before the analysis); the notes and the conclusion state the
      dependence on normalisation.
  - claim: encoding-r2
    agrees: true
    outcome: reproduced
    reason: Reading (a) gives 0.9982 and 0.9960 and reading (b) 0.959 and 0.989; both pass. The test
      has little specificity; the space has 2 PCs, random axes give median R2 of 0.73 to 0.98, and the
      fraction of random axes scoring above the encoding axis is 0.03 to 0.48. The paper's random-axes
      check passes only for Hand Left.
    response: Added the R2 and the random-axes comparison in the PC spaces of normalised rates (3 or
      4 PCs). R2 stays above 0.94, and u beats 95% of random axes in 2 of 8 (soft) and 0 of 8
      (z-scored). The notes now say the match is reproduced and its specificity to u is not shown.
      Outcome unchanged.
  - claim: encoding-bayes-beats-linear
    agrees: true
    outcome: partially_reproduced
    reason: The Bayesian RMSE is lower in 4 of 4 for Long and 3 of 4 for Short (Hand Right Short
      +0.186). weighted_fit fits by weighted least squares but reports unweighted RMSE; the Methods
      do not specify which. The short-in-long control shows the same Bayesian advantage as the real
      test, which undercuts this claim.
    response: Added the weighted RMSE as a variant; the counts are the same (Long 4 of 4, Short 3 of
      4). The notes and conclusion now say the control period shows the same advantage, so it is not
      specific to the support. Outcome unchanged.
  - claim: short-in-long-control
    agrees: true
    outcome: reproduced
    reason: Reproduced, but the result carries no information. p = 0.25 >= 0.05, and with 4 datasets
      the smallest possible p is 0.125, so this criterion cannot fail. The effect size points against
      the claim; Bayesian lower in 3 of 4, median dRMSE -0.108, close to the Short prior's -0.120.
    response: No change; the notes already said the test could not detect an effect and that the
      effect sizes do not show the paper's contrast. The protocol judges a claim of absence on the
      paper's test alone.
  - claim: neural-long-more-bias
    agrees: true
    outcome: reproduced
    reason: Long below Short in 4 of 4. Hand Right is nearly a tie (ratio 0.97).
    response: No change.
  - claim: speed-vs-projection
    agrees: true
    outcome: partially_reproduced
    reason: rho = -0.941 (Short) and -0.878 (Long), both with p < 1e-6, both outside tolerance. Xu at
      Set rises with ts by construction and speed falls with ts, so the pooled rho mostly reflects
      shared dependence on ts, which probably explains why both values are larger than the paper's.
    response: Added the correlation of residuals on ts within dataset and prior (-0.195 and +0.069);
      the notes now say the pooled relation is carried by the common dependence on ts. Outcome
      unchanged.
  - claim: initial-speed-biased
    agrees: true
    outcome: reproduced
    reason: Shallower than the unbiased profile in 7 of 8, p = 0.039.
    response: No change.
  - claim: speed-predicts-tp
    agrees: true
    outcome: partially_reproduced
    reason: rho = -0.733 and -0.744, both with p < 0.001, both outside tolerance. The same shared
      dependence on ts applies; the paper's z-scoring per ts applies to its single-trial variant,
      which the notebook does not run.
    response: Added the trial-by-trial correlation with speed and tp z-scored within each ts (-0.317
      and -0.201, negative in 8 of 8) and the residual correlation of the condition means (+0.084 and
      -0.283). Outcome unchanged.
  - claim: alt-speed-unmodulated
    agrees: true
    outcome: reproduced
    reason: Reproduced, but the result carries no information. p = 0.125 for both priors, the minimum
      possible, so the criterion cannot fail. A synthetic null of 48 constant-rate Poisson units with
      the session's trial counts and attrition gives slopes of the same size as observed, so the
      positive slopes and the bootstrap intervals that exclude 0 are what fewer trials alone produce.
      The bootstrap is also biased upward (Eye Right Long 0.579, interval 0.583 to 1.430). The
      effect-size evidence is invalid in both directions.
    response: Agreed. Added a Poisson null with each unit's rate and the same trials and Set times,
      and a variant with only the trials that last the whole support. Observed slopes are below the
      null mean in 8 of 8, and the fixed-trial slopes are outside the null range in 1 of 8. Withdrew
      the statement that the data show modulation and stopped using the bootstrap intervals. Outcome
      unchanged.
  - claim: alt-transient-parallel
    agrees: true
    outcome: not_reproduced
    reason: Longest ts p = 0.039 (2 of 8 slopes positive); shortest ts p = 0.078. It asked for the
      test in the full space and at other variance thresholds, and whether it depends on
      unnormalised rates.
    response: Added 60% and 90% of the variance, the full space and normalised rates. For the longest
      ts p is 0.016 to 0.039 in all but soft normalisation (0.055). Outcome unchanged.
  - claim: alt-threshold-monotonic
    agrees: true
    outcome: not_reproduced
    reason: At 60% variance the median time of the minimum is -210 ms, just outside the 200 ms window.
      The result depends on dimensionality; 75% gives -80 ms and the full space -40 ms. At 60% the Eye
      datasets keep 1 PC, the distance becomes |x - ref|, and its minima are zero crossings, not
      convergence.
    response: Added variants with at least 2 and 3 components (-230 and -70 ms) and a count of the
      one-component curves whose minima are crossings. Outcome unchanged, as the criterion's 60% fixes
      it.
  - claim: gpfa-variance-inverted-u
    agrees: true
    outcome: not_reproduced
    reason: The quadratic coefficient is negative in 5 of 8, one-tailed p = 0.125. Cross-validation
      picks 8 latents, the top of the grid, in all 4 datasets with 100 EM iterations; the
      dimensionality was never really chosen and convergence is unchecked.
    response: Added the training log-likelihood over EM iterations (still rising by 0.066 to 0.084%
      over the last 25) and 12 latents scored on the same folds. 12 beats 8 in all 4 datasets, and
      with 12 the result is the same (5 of 8, p = 0.125). Outcome unchanged.
  - claim: gpfa-mean-sigmoid
    agrees: true
    outcome: reproduced
    reason: The middle increment is larger in 8 of 8 (p = 0.0078), and the Short slope is above Long
      in 4 of 4 (p = 0.0625).
    response: No change; with 12 latents both parts still hold.
  - claim: rnn-curved-manifold
    agrees: true
    outcome: blocked
    reason: Blocked by data_missing. The API lists 2 assets, both NWB spike and trial files, and
      wasGeneratedBy is empty. There are no network models or code. Training new RNNs from the
      Methods would be a new study, not a test against this data.
    response: Changed blocked_by from other to data_missing, which fits the protocol's definition
      (something the claim needs is not in the dandiset and not public); the notes say so.
  - claim: rnn-perturbation
    agrees: true
    outcome: blocked
    reason: Blocked by data_missing, as for rnn-curved-manifold.
    response: Changed blocked_by from other to data_missing.
  - claim: monkey-g
    agrees: true
    outcome: blocked
    reason: The API reports numberOfSubjects 1, and the only path is sub-Haydn/. No part can be
      tested.
    response: No change.
EOF
python tools/entry.py check entries/000130-sohn-2019 2>&1 | tail -5
```

```
0 error(s)
```

**Agent**

Check passes. Quick prose check for em dashes and "rather", then a final clean run, since I edited one conclusion cell after the last one.

**Agent calls Bash**

```bash
grep -n "—\|rather" attempts/000130-sohn-2019-01.yaml entries/000130-sohn-2019/README.md entries/000130-sohn-2019/rsg.py; grep -c "—\|rather" entries/000130-sohn-2019/reproduce_sohn_2019.ipynb; python3 -c "import yaml;yaml.safe_load(open('attempts/000130-sohn-2019-01.yaml'))" && echo yaml ok; python tools/entry.py all entries/000130-sohn-2019 2>&1 | tail -3
```

```
0
yaml ok
Installed kernelspec registry-000130-sohn-2019 in executed/000130-sohn-2019/.venv/share/jupyter/kernels/registry-000130-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (408 s)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat
nb=nbformat.read("executed/000130-sohn-2019/reproduce_sohn_2019.ipynb",4)
for i in [30,35,39,44,81,83,86]:
    out="".join(o.get("text","") for o in nb.cells[i].outputs if o.output_type=="stream")
    print(i, [l for l in out.splitlines() if any(k in l for k in ["Observed","maximum","Fraction","of 8","gain","p = "])][:8])
nb2=nbformat.read("entries/000130-sohn-2019/reproduce_sohn_2019.ipynb",4)
print("outputs in committed notebook:", sum(len(c.get("outputs",[])) for c in nb2.cells if c.cell_type=="code"))
EOF
git status --short
```

```
30 ['Fractions of units passing the BIC rule with shuffled labels (%):', 'Observed: prior 75.0%, ts in Short 31.2%, ts in Long 33.3%, ts in either 45.8%', 'Shuffled, maximum over 5: prior 8.3%, ts in either 2.1%']
35 ['Fraction of samples with the peak between 480 and 800 ms: 0.96']
39 ['soft: in range (estimation 3 or 4, production 5 to 11) 6 of 8', 'z: in range (estimation 3 or 4, production 5 to 11) 8 of 8']
44 ['soft: Hand Left R2 Short 0.9842, Long 0.9749; mean of 4 Short 0.9671, Long 0.9859; above 95% of random axes in 2 of 8', 'z: Hand Left R2 Short 0.9900, Long 0.9596; mean of 4 Short 0.9648, Long 0.9686; above 95% of random axes in 0 of 8']
81 ['Quadratic coefficient negative in 5 of 8; one-tailed signed-rank p = 0.1250']
83 ['   Eye Right: 100 iterations; at iteration 50 -207348, 75 -207095, 100 -206919; gain over the last 25 iterations 0.085%', '   Eye Left: 100 iterations; at iteration 50 -193276, 75 -193053, 100 -192900; gain over the last 25 iterations 0.079%', '   Hand Right: 100 iterations; at iteration 50 -148014, 75 -147860, 100 -147748; gain over the last 25 iterations 0.076%', '   Hand Left: 100 iterations; at iteration 50 -140769, 75 -140649, 100 -140558; gain over the last 25 iterations 0.065%', 'With the grid 4, 8, 12 (4 datasets refit with 12): quadratic coefficient negative in 5 of 8; one-tailed signed-rank p = 0.1250', 'Mean projections with this grid: middle increment above extreme in 8 of 8 (two-sided p = 0.0078); Short slope above Long in 4 of 4']
86 ['Middle increment above extreme in 8 of 8; two-sided signed-rank p = 0.0078', 'Short slope above Long in 4 of 4; one-tailed signed-rank p = 0.0625', 'Mean Xu rises with ts (positive slope) in 8 of 8']
outputs in committed notebook: 0
 M attempts/000130-sohn-2019-01.yaml
 M entries/000130-sohn-2019/README.md
 M entries/000130-sohn-2019/reproduce_sohn_2019.ipynb
 M entries/000130-sohn-2019/rsg.py
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vsc
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat
for p in ["entries/000130-sohn-2019/reproduce_sohn_2019.ipynb","executed/000130-sohn-2019/reproduce_sohn_2019.ipynb"]:
    nb=nbformat.read(p,4)
    c=nb.cells[84]; assert "by 0.066 to 0.084% over the last 25 iterations" in c.source
    c.source=c.source.replace("by 0.066 to 0.084% over the last 25 iterations","by less than 0.1% over the last 25 iterations (0.065 to 0.085% in this run; GPFA values vary slightly between runs)")
    nbformat.write(nb,p)
p="attempts/000130-sohn-2019-01.yaml"; s=open(p).read()
a="""    training log-likelihood still rose by 0.066 to 0.084% over the last 25 iterations.
"""
b="""    training log-likelihood still rose by less than 0.1% over the last 25 iterations.
"""
assert a in s; s=s.replace(a,b)
a="""    response: Added the training log-likelihood over EM iterations (still rising by 0.066 to 0.084%
      over the last 25) and"""
b="""    response: Added the training log-likelihood over EM iterations (still rising, by less than 0.1%
      over the last 25) and"""
assert a in s; s=s.replace(a,b)
open(p,"w").write(s)
EOF
python tools/entry.py check entries/000130-sohn-2019 2>&1 | tail -1; git diff --stat
```

```
0 error(s)
 attempts/000130-sohn-2019-01.yaml                  | 272 ++++++++++-
 entries/000130-sohn-2019/README.md                 |   6 +-
 entries/000130-sohn-2019/reproduce_sohn_2019.ipynb | 531 ++++++++++++++++++---
 entries/000130-sohn-2019/rsg.py                    |  80 +++-
 4 files changed, 783 insertions(+), 106 deletions(-)
```

**Agent**

No outcome changed, but I changed the blocking reason on two claims. The verifier agreed with all 23 outcomes. The entry passes `python tools/entry.py all` (408 s) and `check` (0 errors). Round 1 is recorded under `verifications` in `attempts/000130-sohn-2019-01.yaml`, and nothing is committed.

**Outcome changes**
- **Two RNN claims** (`rnn-curved-manifold`, `rnn-perturbation`): still blocked, but the reason is now `data_missing` in place of `other`, as the verifier proposed. The trained networks and their code are not in the dandiset and are not public.

**Added or corrected in reply to the report**
- **alt-speed-unmodulated (problem 1):** I added a Poisson null (units firing at constant rates, same trials and Set times) and a variant that keeps a fixed set of trials.
  - The observed slopes are below the null mean in 8 of 8, and only 1 of 8 fixed-trial slopes falls outside the null range.
  - I withdrew "the data show the speed is modulated" and stopped using the bootstrap intervals, which are biased upward.
- **Normalised rates (problem 2):** I added soft-normalised and z-scored variants (new helper `rsg.unit_scale`).
  - With z-scored rates, all 8 PCA counts fall in the paper's ranges, against 1 of 8 in the main analysis. The outcome stays `not_reproduced` because the claims file fixed unnormalised rates before the analysis; the notes state the dependence.
  - For encoding-r2, the encoding axis beats 95% of random axes in only 2 of 8 (soft) and 0 of 8 (z-scored) cases. The notes now say the match to the Bayesian estimate is reproduced but its specificity to the axis is not shown.
- **encoding-bayes-beats-linear (problems 3 and 6):** the notes now say the matched control period shows the same Bayesian advantage. RMSE weighted by trial counts gives the same counts.
- **alt-threshold-monotonic (problem 4):** added variants with at least 2 and 3 components (230 and 70 ms before Go), and noted that in the 1-component datasets the minima are trajectory crossings.
- **speed-vs-projection and speed-predicts-tp (problem 5):** correlations of the residuals after removing ts are near zero, so the pooled correlations come from the shared dependence on ts. The paper's control (z-scoring within ts, trial by trial) still gives r = -0.32 (Short) and -0.20 (Long).
- **gpfa claims (problem 7):** cross-validation prefers 12 latents over 8 in all 4 datasets, and the log-likelihood is still rising slightly after 100 iterations. Both GPFA results are unchanged with 12 latents.
- **glm-prior-ts (problem 9):** chance levels are 0 to 14.6% for the prior test (including shifts that keep the prior blocks) and 0 to 2.1% for the ts test. Each prior's ts test alone gives 31.2% and 33.3%, still above tolerance. The choice of Long time points is now recorded as a deviation.
- **dfr-overlap-support:** a bootstrap puts the peak within 480 to 800 ms in 96% of samples.
- **alt-transient-parallel:** the longest-ts result holds in all variants (p = 0.016 to 0.039) except soft normalisation (p = 0.055).
- I updated the conclusions, summary, README and the helper's docstring to match.

**Not done**
- Problem 8 (`tp` offset, `is_outlier` flags, inverted `iti` description) needed no change; the notebook already documented all three.
- The paper's Tables S1 to S3 and supplementary figures are still unavailable, so the fitted model parameters and the paper's random-axis values are not compared.
- A trial-by-trial GPFA analysis of production speed, which is where the paper applies its control for ts, was not run; it is a new analysis.

The re-downloaded paper text is in `paper/`, which git does not track. The untracked dotfiles and `scripts` at the repo root come from the sandbox, not from me.

## End of run

47 turns, 32 minutes, result: success.
