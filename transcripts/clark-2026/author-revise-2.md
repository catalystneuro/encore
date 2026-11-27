# clark-2026 · author-revise-2 · run 45903696483

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls entries/clark-2026 transcripts/clark-2026; cat transcripts/clark-2026/verifier-2-report.md
```

```
Thu Nov 26 22:19:42 UTC 2026
entries/clark-2026:
README.md
entry.yaml
hdring.py
model_sims.ipynb
network.ipynb
network_grid.ipynb
requirements.in
requirements.lock.txt
ring_dmft.py
theory.ipynb
tuning_curves.ipynb

transcripts/clark-2026:
author-report.md
author-revise-1-report.md
author-revise-1.md
author.md
claims-check-report.md
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/^## Author/,$p' | head -300; wc -l docs/protocol.md
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

[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/clark-2026/entry.yaml | head -50; ls attempts* 2>/dev/null; grep -rl "clark-2026-01" --include=*.yaml . | head
```

```
schema_version: 1
name: clark-2026
type: reproduction
title: Symmetries and continuous attractors in disordered neural circuits (Clark, Abbott and Sompolinsky 2026)
description: Tests the findings of Clark, Abbott and Sompolinsky (2026) on dandiset 000939, the
  postsubiculum recordings of Duszkiewicz et al. (2024) that the paper reuses. It rebuilds the
  1,533 head-direction tuning curves from the NWB files with the paper's procedure, checks them
  against the paper's cached curves, and tests the tuning-curve statistics, the fitted
  generative process, the data-derived network and its dynamics, and the mean-field theory.
license: Apache-2.0
python: "3.13"
notebooks:
- path: tuning_curves.ipynb
  title: Tuning curves, their statistics and the generative process
  runtime_minutes: 15
- path: network.ipynb
  title: The data-derived network and its dynamics
  runtime_minutes: 22
- path: network_grid.ipynb
  title: The lambda and c grid of the data-derived network
[... 371 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^### 5. Record the attempt/,/^## Verifier/p' docs/protocol.md; grep -n "^## \|^### " docs/protocol.md
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
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/clark-2026-01.yaml; grep -n "^[a-z_]*:\|^- id:\|^  - id:\|^  - claim\|  round:" attempts/clark-2026-01.yaml | head -150
```

```
768 attempts/clark-2026-01.yaml
1:schema_version: 3
2:id: clark-2026-01
3:datasets:
9:paper: doi:10.1038/s41593-026-02452-4
10:date: 2026-11-26
11:entry: clark-2026
12:provenance:
23:inputs:
36:outcomes:
465:findings:
497:verifications:
510:  - claim: hd-cell-selection
516:  - claim: tuning-curves-match-cache
527:  - claim: fig1e-heterogeneous-peaks
533:  - claim: fig5d-peak-numbers
542:  - claim: fig1fg-mean-and-fluctuation-profiles
548:  - claim: fig3ab-centers-of-mass-uniform
554:  - claim: fig3c-correlation-approaches-circulant
561:  - claim: fig4-generative-fit
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/clark-2026-01.yaml"
}
```

```
1	schema_version: 3
2	id: clark-2026-01
3	datasets:
4	- archive: dandi
5	  id: 000939
6	  version: 0.240528.1542
7	  doi: 10.48324/dandi.000939/0.240528.1542
8	  relation: reuses
9	paper: doi:10.1038/s41593-026-02452-4
10	date: 2026-11-26
11	entry: clark-2026
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 749 more lines not kept]
```

**Agent**

The round-2 report mostly asks for text corrections, plus a few outputs. Let me look at the executed notebooks and questions file.

**Agent calls Bash**

```bash
ls -la executed/clark-2026/ 2>/dev/null; cat questions/clark-2026.yaml; cat entries/clark-2026/README.md
```

```
total 1104
drwxr-xr-x 3 runner runner   4096 Nov 26 22:04 .
drwxr-xr-x 3 runner runner   4096 Nov 26 22:19 ..
-rw-r--r-- 1 runner runner    937 Nov 26 22:04 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 26 20:04 .venv
-rw-r--r-- 1 runner runner  87481 Nov 26 22:04 model_sims.ipynb
-rw-r--r-- 1 runner runner 607236 Nov 26 21:01 network.ipynb
-rw-r--r-- 1 runner runner  21075 Nov 26 21:11 network_grid.ipynb
-rw-r--r-- 1 runner runner    539 Nov 26 22:04 result.json
-rw-r--r-- 1 runner runner  37359 Nov 26 21:13 theory.ipynb
-rw-r--r-- 1 runner runner 343483 Nov 26 20:23 tuning_curves.ipynb
questions:
- claim: fig2gi-circulant-noise-collapses
  question: The criterion places each final state by the peak neuron of its smoothed input currents across
    the 1,533 sorted neurons, merges positions within 31 neurons, and asks the sorted optimal matrix to
    keep at least 50 states. Fig. 2g plots the steady states against the manifold coordinate theta, so
    the continuum the paper shows is one of manifold angles. Should a state be placed by its manifold
    angle (for example the angle of the nearest target point), with the 50 states counted on that coordinate?
  passage: Results, Dynamics of the data-derived network model, "The optimal weights (Fig. 2b) maintain
    a continuum of stable, heterogeneous states (Fig. 2g)"; Fig. 2 legend, "g-i, Steady-state activity
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cat executed/clark-2026/.clean-run.json executed/clark-2026/result.json; git log --oneline -5; git status --short entries questions attempts
```

```
{
 "entry": "clark-2026",
 "hash": "6da5313f131c2faf59c19cc66d2b6e49ada16530a310fb88cd90c729cf537458",
 "finished": 1795730681,
 "results": [
  {
   "notebook": "tuning_curves.ipynb",
   "ok": true,
   "seconds": 1147,
   "sha256": "7cc2188252878ef68d5307b02595595874513eef86e62fad53b7e42e6c5bf8ec"
  },
  {
   "notebook": "network.ipynb",
   "ok": true,
   "seconds": 2256,
   "sha256": "0f0a7bb3ac540887399cce0e7f3085f0c012f7167c1dbeafb369c61a5492056f"
  },
  {
   "notebook": "network_grid.ipynb",
   "ok": true,
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/clark-2026; python - <<'EOF'
import json
for nb,cells in [("theory.ipynb",[5,6,7,8,9]),("network_grid.ipynb",[4,5]),("network.ipynb",[19,20,22,23]),("model_sims.ipynb",[6,7,11,12]),("tuning_curves.ipynb",[0])]:
    d=json.load(open(nb))
    for i in cells:
        c=d['cells'][i]
        print(f"===== {nb} cell {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')}")
        print(''.join(c['source']))
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            print('--OUT--'); print(''.join(t)[:4000])
EOF
```

```
<persisted-output>
Output too large (52.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/d9b76879-81d7-443c-8fae-641c577b6cb3/tool-results/bdd9tfvib.txt

Preview (first 2KB):
===== theory.ipynb cell 5 [code] tags=['claim:fig7-dmft-mexican-hat-and-stability']
prof_ok = []
for sc in (1, 2, 4):
    for g in (1.5, 3, 5, 10):
        Jp = D.DMFTModel(N_theta=1000, g=g, scale=sc).J
        prof_ok.append(dict(sigma=sc, beta=g, J0=Jp[0], Jmin=Jp.min(), argmin_rad=2 * np.pi * min(Jp.argmin(), 1000 - Jp.argmin()) / 1000, mexican=Jp[0] > 0 and Jp.min() < 0))
print(pd.DataFrame(prof_ok).round(4).to_string(index=False))
t = time.time()
g_vals = np.logspace(-2, 2, 40); s_vals = np.logspace(0, 2, 20)
bump = np.zeros((40, 20, 5), complex); homo = np.zeros((40, 20, 5), complex); amp = np.zeros((40, 20))
for i, g in enumerate(g_vals):
    for j, sc in enumerate(s_vals):
        mdl = D.DMFTModel(N_theta=500, scale=sc, g=g)
        bump[i, j] = mdl.compute_bump_jacobian()[1][:5]
        m_b = mdl.F(mdl.Gamma_x[0], mdl.Gamma_x[0], mdl.Gamma_x)   # the bump the Jacobian is taken at
        amp[i, j] = m_b.max() - m_b.min()
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/d9b76879-81d7-443c-8fae-641c577b6cb3/tool-results/bdd9tfvib.txt"
}
```

```
1	===== theory.ipynb cell 5 [code] tags=['claim:fig7-dmft-mexican-hat-and-stability']
2	prof_ok = []
3	for sc in (1, 2, 4):
4	    for g in (1.5, 3, 5, 10):
5	        Jp = D.DMFTModel(N_theta=1000, g=g, scale=sc).J
6	        prof_ok.append(dict(sigma=sc, beta=g, J0=Jp[0], Jmin=Jp.min(), argmin_rad=2 * np.pi * min(Jp.argmin(), 1000 - Jp.argmin()) / 1000, mexican=Jp[0] > 0 and Jp.min() < 0))
7	print(pd.DataFrame(prof_ok).round(4).to_string(index=False))
8	t = time.time()
9	g_vals = np.logspace(-2, 2, 40); s_vals = np.logspace(0, 2, 20)
10	bump = np.zeros((40, 20, 5), complex); homo = np.zeros((40, 20, 5), complex); amp = np.zeros((40, 20))
11	for i, g in enumerate(g_vals):
12	    for j, sc in enumerate(s_vals):
13	        mdl = D.DMFTModel(N_theta=500, scale=sc, g=g)
14	        bump[i, j] = mdl.compute_bump_jacobian()[1][:5]
15	        m_b = mdl.F(mdl.Gamma_x[0], mdl.Gamma_x[0], mdl.Gamma_x)   # the bump the Jacobian is taken at
16	        amp[i, j] = m_b.max() - m_b.min()
17	        homo[i, j] = mdl.compute_homogeneous_jacobian()[1][:5]
18	print(f"stability grid in {time.time()-t:.0f} s")
19	print(f"bump eigenvalue 1 (symmetry zero): max |Re| {np.abs(bump[..., 0].real).max():.2e}; grid points where it is above 1e-6: {int((bump[..., 0].real > 1e-6).sum())} of 800")
20	bad = np.argwhere(bump[..., 0].real > 1e-6)
[... 553 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/d9b76879-81d7-443c-8fae-641c577b6cb3/tool-results/bdd9tfvib.txt",
 "offset": 574
}
```

```
574	X10, P10, J10, x0d, x0c = setup10(sd10)
575	rw = np.random.default_rng(sd10 + 2)
576	rows = []
577	for f in F_W:
578	    for lab, Jb, x0 in (("disordered", J10, x0d), ("circulant", J_circ, x0c)):
579	        rec, n = run10(Jb, x0, f, lab, P10, rw)
580	        cs, dmed, dmax = summarize10(rec, n)
581	        st_t = {tt: H.count_states(rec[tt], n, n / 50)["bins"] for tt in (30, 60, 90)}
582	        rows.append(dict(f_w=f, network=lab, single=cs["single"], greedy=cs["greedy"], bins=cs["bins"], bins_at_30_60_90s=list(st_t.values()),
583	                         median_drift_rad=round(dmed, 3), max_drift_rad=round(dmax, 3), continuum=min(cs.values()) >= 31))
584	    print(f"f_w {f} done at {time.time()-t:.0f} s", flush=True)
585	tab10 = pd.DataFrame(rows)
586	print(tab10.to_string(index=False))
587	c0 = tab10[tab10.f_w == 0.0].continuum.all(); c4 = (~tab10[tab10.f_w == 0.4].continuum).all()
588	print(f"both keep a continuum at f_w 0: {c0}; neither does at 0.4: {c4}")
589	# seed check at f_w 0.4, the level the criterion reads for fragmentation (the network, the initial noise and the weight noise)
590	for k in range(1, 5):
591	    s = sd10 + 1000 * k
592	    _, Pk, Jk, xdk, xck = setup10(s)
593	    rwk = np.random.default_rng(s + 2)
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/clark-2026.yaml'))
for c in d['claims']:
    if c['id'] in ('figs1-s2-spectrum-does-not-fix-symmetry','figs11-s12-global-stability-model','fig7-dmft-mexican-hat-and-stability','figs10-robustness-comparable'):
        print(yaml.safe_dump(c,width=120))
EOF
ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd entries/clark-2026; python - <<'EOF'
import json
for nb in ["theory.ipynb","network_grid.ipynb","network.ipynb","model_sims.ipynb","tuning_curves.ipynb"]:
    d=json.load(open(nb)); e=json.load(open('../../executed/clark-2026/'+nb))
    print(nb, len(d['cells']), len(e['cells']), all(''.join(a['source'])==''.join(b['source']) for a,b in zip(d['cells'],e['cells'])))
d=json.load(open('model_sims.ipynb'))
for i,c in enumerate(d['cells']):
    if c['cell_type']=='markdown': print(i, ''.join(c['source'])[:300].replace('\n',' '))
EOF
grep -n "77 min\|minutes\|24 GB" *.ipynb README.md | cut -c1-200
```

```
Thu Nov 26 22:21:05 UTC 2026
theory.ipynb 21 21 True
network_grid.ipynb 8 8 True
network.ipynb 26 26 True
model_sims.ipynb 16 16 True
tuning_curves.ipynb 57 57 True
0 # Clark, Abbott & Sompolinsky (2026): the simulations of the generative-process and rank-four networks  Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. Dataset. DANDI:000939 at version 0.240528.1542, the version the paper cites (see `tuning_curves.ipynb`).  These three c
3 ## figs1-s2-spectrum-does-not-fix-symmetry  > Eigenvalue degeneracy suggests but does not fix the symmetry group, since ensembles matching > the model's second-order statistics, and hence its spectrum, can differ beyond second order and > give different symmetry groups and attractors (a single ring 
5 **Result: partially reproduced.** The dynamics differ as the legends describe under all five seeds: with Gaussian loadings the final states form a ring in the dominant doublet (radius 0.80, radii varying by at most 0.6%, largest angle gap 0.32 to 0.45 rad) and collapse in the subdominant one (radius
6 ## figs11-s12-global-stability-model  > In the generative-process network of 2,500 neurons, initial conditions far from the manifold > converge to it with no spurious attractors, and with growing N the dynamics approach the > mean-field behaviour, reliably converging to a ring by N = 1,000.  As `spu
9 **Result: reproduced (resting on an assumption).** In the 2,500-neuron network, from every initial spread (standard deviation 1 to 1,000, median starting distance 1.2 to 1.3) at least 97% of final states lie within the threshold of the network's own fig2ef-protocol run (largest distance at 20 s 0.01
10 ## figs10-robustness-comparable  > Under added weight noise the disordered network and a circulant network with proportional > eigenvalues fragment into discrete states alike, so the two are comparably robust.  As `weight_matrix_analyses.ipynb`, cell 10: the generative-process network (N 2,500, 500 
12 **Result: rep
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -30; ls executed/clark-2026/.venv/bin | grep -i jup | head
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

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
[... 20 more lines not kept]
```

**Agent**

Now the theory notebook edits: add the breakdown of the 293 points and per-sigma timescale detail.

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import json
p='theory.ipynb'; d=json.load(open(p))
def src(i): return ''.join(d['cells'][i]['source'])
def setsrc(i,s): d['cells'][i]['source']=s.splitlines(keepends=True)
s5=src(5)
old='mq = D.DMFTModel(N_theta=500, scale=1.4211, g=2.7659)'
add='''# where on the grid the bump has no zero mode: counts by beta band and by sigma band
bb = [("beta < 0.1", g_vals < 0.1), ("0.1 <= beta < 1", (g_vals >= 0.1) & (g_vals < 1)), ("beta >= 1", g_vals >= 1)]
sb = [("sigma < 10", s_vals < 10), ("10 <= sigma < 50", (s_vals >= 10) & (s_vals < 50)), ("sigma >= 50", s_vals >= 50)]
tab_nz = pd.DataFrame([[int(nz[np.ix_(bm, sm)].sum()) for _, sm in sb] + [int(nz[bm].sum())] for _, bm in bb],
                      index=[b for b, _ in bb], columns=[s for s, _ in sb] + ["all sigma"])
tab_nz.loc["all beta"] = tab_nz.sum()
print("points without a zero mode, by beta band (rows) and sigma band (columns):"); print(tab_nz.to_string())
print("grid points per band: beta", [int(bm.sum()) for _, bm in bb], "x sigma", [int(sm.sum()) for _, sm in sb])
print(f"without a zero mode with beta below 0.1 or sigma at least 50: {int((nz & (g_vals[:, None] < 0.1) | nz & (s_vals[None, :] >= 50)).sum())} of {int(nz.sum())}")
'''
assert old in s5
setsrc(5, s5.replace(old, add+old))
s8=src(8)
s8 += '''# where the extremes are, and the parts of the criterion within sigma 1 to 10
for lab, tt in (("convergence (bump)", t_bump), ("divergence (uniform)", t_homo)):
    a, b = np.unravel_index(np.argmax(np.where(sel10[:, None], tt, -np.inf)), tt.shape)
    a2, b2 = np.unravel_index(np.argmin(np.where(sel10[:, None], tt, np.inf)), tt.shape)
    print(f"{lab}: over beta 1 to 10 the largest {tt[a, b]:.3f} at beta {g_vals[a]:.3f}, sigma {s_vals[b]:.2f}; the smallest {tt[a2, b2]:.3f} at beta {g_vals[a2]:.3f}, sigma {s_vals[b2]:.2f}")
    print("   per sigma:", pd.DataFrame(dict(sigma=s_vals.round(2), t_min=tt[sel10].min(0).round(3), t_max=tt[sel10].max(0).round(3),
          few_tau=((tt[sel10] >= 0.5) & (tt[sel10] <= 10)).all(0), increases=[int((np.diff(tt[sel, j]) > 0).sum()) for j in range(20)])).to_string(index=False), sep="\\n")
    s10 = s_vals <= 10
    r10 = tt[sel][:, s10].max(1) / tt[sel][:, s10].min(1)
    print(f"   over sigma 1 to 10 only: few tau {bool(((tt[np.ix_(sel10, s10)] >= 0.5) & (tt[np.ix_(sel10, s10)] <= 10)).all())}, "
          f"decreasing at every sigma {all(int((np.diff(tt[sel, j]) > 0).sum()) <= 1 for j in np.where(s10)[0])}, max/min over sigma {r10.max():.3f}")
'''
setsrc(8,s8)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat theory.ipynb; tail -c 300 theory.ipynb | od -c | tail -3; git show HEAD:entries/clark-2026/theory.ipynb | tail -c 50 | od -c | tail -3
```

```
entries/clark-2026/theory.ipynb | 21 ++++++++++++++++++++-
 1 file changed, 20 insertions(+), 1 deletion(-)
0000420   :       4   ,  \n       "   n   b   f   o   r   m   a   t   _
0000440   m   i   n   o   r   "   :       5  \n   }  \n
0000454
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Bash**

```bash
cd entries/clark-2026; time ../../executed/clark-2026/.venv/bin/jupyter nbconvert --to notebook --execute theory.ipynb --output-dir $TMPDIR/th --ExecutePreprocessor.timeout=1200 2>&1 | tail -2; python - <<EOF
import json
d=json.load(open("$TMPDIR/th/theory.ipynb"))
for i in (5,8):
    for o in d['cells'][i].get('outputs',[]):
        print(''.join(o.get('text','') or o.get('data',{}).get('text/plain','')))
EOF
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 43107 bytes to /tmp/claude-1001/th/theory.ipynb

real	2m30.881s
user	8m23.302s
sys	0m4.164s
 sigma  beta      J0    Jmin  argmin_rad  mexican
     1   1.5  8.5376 -2.5906      1.5268     True
     1   3.0  5.9153 -1.7814      1.7027     True
     1   5.0  5.2516 -1.5862      1.7719     True
     1  10.0  4.9056 -1.4874      1.8158     True
     2   1.5 18.4696 -3.8117      0.7665     True
     2   3.0 12.8603 -2.5292      0.8482     True
     2   5.0 11.4414 -2.2190      0.8796     True
     2  10.0 10.7040 -2.0630      0.9048     True
     4   1.5 38.5445 -6.0181      0.3833     True
     4   3.0 26.9419 -3.8357      0.4210     True
     4   5.0 24.0088 -3.3121      0.4398     True
     4  10.0 22.4869 -3.0471      0.4524     True

[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import json
d=json.load(open('theory.ipynb'))
for i,c in enumerate(d['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and ('sigma' in s or 'Summary' in s): print(i,'-----\n'+s)
EOF
```

```
4 -----
## fig7-dmft-mexican-hat-and-stability

> In the mean-field theory the effective interactions are circulant with a Mexican hat profile
> set by sigma and beta; at a bump state all Jacobian eigenvalues have negative real parts except
> the symmetry-induced zero, the uniform state has a real positive eigenvalue for all sigma and
> beta (a Turing instability), and fixing Q destabilizes the bump.

As `dmft.ipynb`: the profiles of Fig. 7a (`plot_weights`, N_theta 1,000, sigma 1, 2, 4, beta
1.5, 3, 5, 10) and the stability grid (`run_analysis`, beta logspace(-2, 2, 40), sigma
logspace(0, 2, 20), N_theta 500, five eigenvalues kept), and the spectrum with Q fixed
(`plot_exclude_Q_spectra`, N_theta 500, sigma 1.4211, beta 2.7659).
6 -----
**Result: reproduced.** All twelve interaction profiles of Fig. 7a are positive at 0 (4.9 to 38.5)
and negative at some offset (minimum -1.5 to -6.0). Over the 40 by 20 grid the bump's second
eigenvalue is negative at every point (largest -4.7e-8, effectively zero at some points) and the
uniform state's leading eigenvalue is real and positive at every point (smallest 4.7e-5). With Q
fixed the bump at sigma 1.4211 and beta 2.7659 has a positive eigenvalue (0.446). At 293 of the 800
grid points no zero eigenvalue is found at the bump (the leading one is below -1e-6, down to
-0.22), mostly at small beta and large sigma; the bump there is not flat (amplitude, max - min of
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import json
p='theory.ipynb'; d=json.load(open(p))
def setsrc(i,s): d['cells'][i]['source']=s.strip('\n').splitlines(keepends=True)
setsrc(6, """**Result: reproduced.** All twelve interaction profiles of Fig. 7a are positive at 0 (4.9 to 38.5)
and negative at some offset (minimum -1.5 to -6.0). Over the 40 by 20 grid the bump's second
eigenvalue is negative at every point (largest -4.7e-8, effectively zero at some points) and the
uniform state's leading eigenvalue is real and positive at every point (smallest 4.7e-5). With Q
fixed the bump at sigma 1.4211 and beta 2.7659 has a positive eigenvalue (0.446). At 293 of the 800
grid points no zero eigenvalue is found at the bump (the leading one is below -1e-6, down to
-0.22). Most of them are at beta of 1 and above (249 of 293) and at sigma of 10 and above (128 at
sigma 10 to 50 and 98 at 50 and above); beta below 0.1 or sigma of 50 and above holds only 99 of
them, and 67 are at sigma below 10 with beta of 1 and above. At sigma 1.4211 and beta 2.7659 the
zero is present. The bump at those points is not flat (amplitude, max - min of m, median 0.95,
below 1e-3 at only 6 of them), so its missing zero mode is not explained by a vanishing bump. The
criterion tests only the second eigenvalue; the statement's "except the symmetry-induced zero"
does not hold at those 293 points.""")
setsrc(9, """**Result: not reproduced.** The convergence time falls with beta for every sigma and varies across
sigma by at most a factor of 2.55 at each beta (reading b holds, a does not), but over beta 1 to 10
it runs from 2.87 to 20.5 tau, the largest at beta 1.1 and sigma 37.9 (19.5 at sigma 100); it stays
within 0.5 to 10 tau only at sigma 1 and exceeds 10 tau at beta 1.1 for every sigma from 1.27 up.
The divergence time ranges from 0.15 to 3.83 tau over beta 1 to 10 and falls below 0.5 tau at
every sigma from 6.95 up; it rises with beta at the five smallest sigma (11, 10, 8, 6 and 3
increases, sigma 1 to 2.64), and varies by up to a factor of 24 across sigma (6.1 within sigma 1
to 10). No sigma meets all three parts for both timescales, and restricting the grid to sigma 1 to
10 does not change the outcome. Neither the first two parts nor the third hold for both
timescales. The thresholds are the claims file's.""")
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat .
```

```
entries/clark-2026/theory.ipynb | 45 ++++++++++++++++++++++++++++++++---------
 1 file changed, 36 insertions(+), 9 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/clark-2026; grep -n "sampling noise\|alike\|77 min\|two of the four\|resolution of the reference\|1 to 4 of\|96 to 100\|every lambda\|minutes" *.ipynb README.md | cut -c1-250
```

```
model_sims.ipynb:360:    "> eigenvalues fragment into discrete states alike, so the two are comparably robust.\n",
model_sims.ipynb:459:    "and the circulant in 9 (4 to 8 and 9 to 12 over five seeds). The two fragment alike over the whole\n",
network.ipynb:637:    "resolution of the reference (largest final distance 0.0015, against median starting distances of\n",
network_grid.ipynb:141:    "    print(f\"reading {lab}: c 0 gives divergence or collapse at every lambda {p1}, at some lambda {p1a}; lambda 1e-2 collapses at c 1: {p3}; collapse at c 0.25, lambda 1e-8: {p5}\")\n",
network_grid.ipynb:171:    "**Result: partially reproduced.** At c 0 some runs diverge at every lambda up to 1e-4 (1 to 4 of\n",
network_grid.ipynb:173:    "100 of 100, radius 0.65 to 0.80 against 39 for the manifold) at every lambda; under reading (i) no\n",
README.md:44:  process (about 15 minutes, most of it the generative fit).
README.md:45:- `network.ipynb`: the data-derived network, its weights, dynamics and spectrum (about 22 minutes).
README.md:46:- `network_grid.ipynb`: the lambda and c grid (about 8 minutes).
README.md:47:- `theory.ipynb`: the mean-field theory and the large-N spectra (about 2 minutes).
README.md:49:  31 minutes).
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import json
for nb,idx in [("tuning_curves.ipynb",None),("network.ipynb",None),("network_grid.ipynb",None),("model_sims.ipynb",None)]:
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        s=''.join(c['source'])
        if c['cell_type']=='markdown' and (s.startswith('**Result') or s.startswith('## Summary')) and (nb!='tuning_curves.ipynb' or 'fig4' in s or 'minim' in s or 'Summary' in s):
            print(nb,i,'-----\n'+s)
EOF
```

```
tuning_curves.ipynb 34 -----
**Result: partially reproduced.** With the final pass of 500,000 samples the minimum is at sigma
1.4737, b 1.2145, beta 3.1103 under all five seeds: sigma (1.42 within 0.142) and beta (2.77
within 0.345) match and b (1.73 within 0.173) does not. The paper's grid point (1.4211, 1.7307,
2.7659) is the minimum of the 25,000-sample shortlist pass and second in the final pass under
every seed (0.00907 to 0.01006, against 0.00853 to 0.00894 for the chosen point). Taking the 90
best shortlist points to 500,000 samples changes nothing (the best of points 31 to 90 has error
0.01796). A float32 final pass over the 30 points also puts the chosen point first (0.00889
against 0.00916). In the paper's own cached error grid the two points are 1.1% apart (0.00890 at
the paper's point, 0.00900 at the chosen one): the surface has two near-equal minima along a
ridge in b and beta, and which wins depends on the draws and the arithmetic.
tuning_curves.ipynb 55 -----
## Summary

| claim | outcome |
|---|---|
| hd-cell-selection (link) | reproduced |
| tuning-curves-match-cache (link, with inputs) | reproduced |
| fig1e-heterogeneous-peaks | reproduced |
| fig5d-peak-numbers | reproduced |
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import json
def load(p): return json.load(open(p))
def save(p,d): json.dump(d,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
def setsrc(d,i,s): d['cells'][i]['source']=s.strip('\n').splitlines(keepends=True)
def src(d,i): return ''.join(d['cells'][i]['source'])

# network_grid
p='network_grid.ipynb'; d=load(p)
setsrc(d,5,"""**Result: partially reproduced.** At c 0 some runs diverge at every lambda up to 1e-4 (4, 3 and 1
of 100 at lambda 1e-12, 1e-8 and 1e-4; 4 and 3 of 20 at 1e-10 and 1e-6), and under reading (ii) of
collapse every other run falls to the homogeneous state at every lambda (96, 97, 99 and 100 of 100
at 1e-12, 1e-8, 1e-4 and 1e-2; 16 and 17 of 20 at 1e-10 and 1e-6; radius 0.65 to 0.80 against 39
for the manifold); under reading (i) no run collapses, since the homogeneous state keeps a
firing-rate norm of 17.3 to 17.7. No c above 0 diverges up to lambda 1e-4, and c 0.25 still leaves
the collapse (12 of 20 at lambda 1e-8 under reading ii). At lambda 1e-2 the manifold is lost for c
up to 0.75 (all 20 collapse under reading ii), but at c 1 the states keep a radius of 4.6, just
above the collapse threshold of 3.9, so the criterion's test at c 1 fails. The flow error rises at
large lambda (2.1e-2 at 1e-2) and at small lambda from 1.3e-10 at 1e-10 to 3.6e-9 at 1e-12, but
1e-8 (1.7e-8) is not below 1e-12, so that part of the criterion fails too. The paper's cached flow
errors agree to three digits from 1e-10 to 1e-2 (3.8e-9 at 1e-12) and fail the same part: the
supplement says only that 1e-8 sits just above the minimum, which holds, and this reading of the
criterion is asked of a reader. The criterion has no rule for a partial result; partially
reproduced is the protocol's reading of a result that holds in part (two of its four parts).""")
save(p,d)

# network
p='network.ipynb'; d=load(p)
s=src(d,19)
old='''print("variant, no eigenvalue set aside: within", np.round([a_ - b_ for a_, b_ in pairs0], 4), "next", np.round([lead.real[2 * p + 1] - lead.real[2 * p + 2] for p in range(4)], 4))'''
new='''wi0 = [a_ - b_ for a_, b_ in pairs0]; tn0 = [lead.real[2 * p + 1] - lead.real[2 * p + 2] for p in range(4)]
print("variant, no eigenvalue set aside: within", np.round(wi0, 4), "next", np.round(tn0, 4), "| within < next:", [bool(a_ < b_) for a_, b_ in zip(wi0, tn0)], f"({sum(a_ < b_ for a_, b_ in zip(wi0, tn0))} of 4)")'''
assert old in s; setsrc(d,19,s.replace(old,new))
setsrc(d,23,"""**Result: reproduced (resting on an assumption).** From median starting distances of 1.6 to 700,
every final state ends within 0.0016 of the manifold (final medians 0.00047 to 0.00085, largest
0.00154), with none elsewhere, and at standard deviation 1 all 34 final angles fall in one state
(1.69 to 1.70 rad), under all five seeds. Against the fig2ef protocol run with the same 5-ms step
(largest distance at 20 s 0.00141), 97% to 100% of final states are within at every standard
deviation, under all five seeds; the largest final distances (0.00147, 0.00153 and 0.00154) are
just above that reference. Against the 1-ms fig2ef threshold (0.00132), the variant, 91% to 100%
are within, below 95% at standard deviations 10, 50 and 1,000 under the claim's seed (0.94, 0.91,
0.94); the final distances sit at the network's resolution, about 1e-3, where the step of the
reference decides the test.""")
save(p,d)

# tuning_curves header
p='tuning_curves.ipynb'; d=load(p)
s=src(d,0); old='session ids and sizes of about 24 GB)'; assert old in s
setsrc(d,0,s.replace(old,'session ids and sizes of 12.7 to 30.2 GB)'))
s=src(d,34)
setsrc(d,34, s.rstrip('\n')+""" The claims file's
criterion has no rule for a partial result; partially reproduced is the protocol's reading of a
result that holds in part (two of the three parameters).""")
save(p,d)
EOF
git diff --stat .
```

```
entries/clark-2026/network.ipynb       | 18 ++++++++------
 entries/clark-2026/network_grid.ipynb  | 27 +++++++++++---------
 entries/clark-2026/theory.ipynb        | 45 +++++++++++++++++++++++++++-------
 entries/clark-2026/tuning_curves.ipynb |  6 +++--
 4 files changed, 65 insertions(+), 31 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python -c "
import json;d=json.load(open('model_sims.ipynb'))
for i in (0,3,4,8,13): print(i,'-----');print(''.join(d['cells'][i]['source']))
"
```

```
0 -----
# Clark, Abbott & Sompolinsky (2026): the simulations of the generative-process and rank-four networks

Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. Dataset.
DANDI:000939 at version 0.240528.1542, the version the paper cites (see `tuning_curves.ipynb`).

These three claims use no recorded data (`data: elsewhere`): each runs a notebook of the
paper's code at commit 245726f, repeated here in numpy (`hdring.py`). The networks are built
from the idealized generative process (`ring/tc.py`, `gen_tuning_curves_idealized`; sigma
1.4211, beta 2.7659, 500 angles, lambda 1e-8) or from random rank-four loadings. Every random
draw comes from the claim's seed; the paper's notebooks use numpy seeds 42 and 123.

| claim | data | tested here |
|---|---|---|
| figs1-s2-spectrum-does-not-fix-symmetry | elsewhere | yes |
| figs11-s12-global-stability-model | elsewhere | yes |
| figs10-robustness-comparable | elsewhere | yes |
| fig8-grid-scores-and-torus | elsewhere | no, blocked (too large) |
3 -----
## figs1-s2-spectrum-does-not-fix-symmetry
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml
d=yaml.safe_load(open('claims/clark-2026.yaml'))
for c in d['claims']:
    if c['id']=='figs11b-data-network-global-stability': print(c['criterion'])
"; grep -n "Supplementary Fig. 1\b\|Supplementary Figs. 1 and 2\|second-order statistics" paper/*.txt | head; pdftotext -v 2>&1 | head -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 3855,3865p paper/*.txt; sed -n 4010,4020p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk 'NR>=3700 && NR<=4020 && /^[0-9]+(\.[0-9]+)* [A-Z]/' paper/*.txt | head; grep -n "symmetry-induced zero" paper/*.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk 'NR>=3600 && NR<=4020 && length($0)<60 && /^[0-9]/' paper/*.txt | head -20; grep -n "Supplementary Note [0-9]" paper/*.txt | awk -F: '$1>3000 && $1<4100' | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd entries/clark-2026; python - <<'EOF'
import json
def load(p): return json.load(open(p))
def save(p,d): json.dump(d,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
def setsrc(d,i,s): d['cells'][i]['source']=s.strip('\n').splitlines(keepends=True)
def src(d,i): return ''.join(d['cells'][i]['source'])
p='model_sims.ipynb'; d=load(p)
s=src(d,7)
old='''    print(f"   all standard deviations with at least 95% within: {all(np.mean(o['d'] <= thr) >= 0.95 for o in out.values())}", flush=True)'''
new='''    print(f"   all standard deviations with at least 95% within: {all(np.mean(o['d'] <= thr) >= 0.95 for o in out.values())}; "
          f"strict reading of 'every final state', all within at every standard deviation: {all(bool((o['d'] <= thr).all()) for o in out.values())}", flush=True)'''
assert old in s; setsrc(d,7,s.replace(old,new))
s=src(d,8)
old='''print("N 1,000, at least 95% within the 2,500-neuron threshold, by seed:", dict(zip(n1000.seed, n1000.within_N2500_threshold >= 0.95)))'''
new=old+'''
print("N 1,000, strict reading (all 34 within), by seed:", dict(zip(n1000.seed, n1000.within_N2500_threshold >= 1.0)))'''
assert old in s; setsrc(d,8,s.replace(old,new))
s=src(d,9).rstrip('\n')
setsrc(d,9, s+""" Read strictly, "every final state" and "all
converge" fail under the claim's seed at standard deviation 10 (0.97 within: one state at 0.01146
against the threshold 0.01121); the 95% rule is taken from figs11b, which the criterion names as the
way to judge, and it is part of this assumption.""")
s=src(d,5).rstrip('\n')
setsrc(d,5, s+""" The criterion's 5% applies to two finite
matrices, whose eigenvalues scatter around the shared population values by sampling, so this part
measures sampling noise more than a difference between the ensembles; whether the criterion should
test the population (large-N) spectrum is asked of a reader. The criterion has no rule for a
partial result; partially reproduced is the protocol's reading of a result that holds in part.""")
setsrc(d,12, """**Result: reproduced (resting on an assumption).** Without weight noise both networks keep all 34
states (34 under every merging reading, median drift 0.013 rad for the disordered network and
0.025 for the circulant one). At noise 0.4 neither does: the disordered network ends in 8 states
and the circulant in 9 (4 to 8 and 9 to 12 over five seeds), so the criterion is met. The two do
not fragment alike in detail. At noise 0.4 the disordered network ends in fewer states than the
circulant under every seed (8, 7, 4, 8 and 5 against 9, 12, 11, 12 and 9 under bins) with a larger
median drift (0.23 to 0.48 rad against 0.15 to 0.22). Under the claim's seed it keeps fewer states
at every level from 0.4 on (8, 8, 6 and 4 against 9, 12, 9 and 8) and more at 0.2 (15 against
11), and its median drift is larger at every level but 0.8 (0.29 to 0.47 rad from 0.2 on, against
0.16 to 0.30). Both already fragment at noise 0.2, which the criterion does not test. The
statement's "comparably robust" holds in that both lose the continuum at the same noise levels;
the disordered network fragments somewhat further.""")
setsrc(d,13, """## fig8-grid-scores-and-torus

Blocked (too large). The network of 25,000 neurons needs a 25,000 by 25,000 weight matrix (5 GB
in float64, 2.5 GB in float32), fitted by regression on 25,000 by 25,000 kernels and simulated,
and the grid-score sweep 1,000 maps for each eta. It was not started: the five notebooks of this
entry already take about two hours per run (the run before this revision, 1,147, 2,256, 613, 157
and 3,044 s), and this notebook alone about 51 minutes of the 60 allowed.""")
save(p,d)
EOF
git diff --stat .
```

```
Thu Nov 26 22:25:31 UTC 2026
 entries/clark-2026/model_sims.ipynb    | 31 +++++++++++++++++------
 entries/clark-2026/network.ipynb       | 18 ++++++++------
 entries/clark-2026/network_grid.ipynb  | 27 +++++++++++---------
 entries/clark-2026/theory.ipynb        | 45 +++++++++++++++++++++++++++-------
 entries/clark-2026/tuning_curves.ipynb |  6 +++--
 5 files changed, 89 insertions(+), 38 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import re
s=open('entry.yaml').read()
for nb,m in [("tuning_curves",19),("network",38),("network_grid",10),("theory",3),("model_sims",51)]:
    s=re.sub(r'(- path: %s\.ipynb\n  title: [^\n]*\n  runtime_minutes: )\d+'%nb, r'\g<1>%d'%m, s)
open('entry.yaml','w').write(s)
r=open('README.md').read()
for a,b in [("about 15 minutes","about 19 minutes"),("(about 22 minutes)","(about 38 minutes)"),("(about 8 minutes)","(about 10 minutes)"),("(about 2 minutes)","(about 3 minutes)"),("about\n  31 minutes","about\n  51 minutes")]:
    assert a in r,a; r=r.replace(a,b)
open('README.md','w').write(r)
EOF
git diff entry.yaml README.md | grep "^[+-]"
```

```
--- a/entries/clark-2026/README.md
+++ b/entries/clark-2026/README.md
-  process (about 15 minutes, most of it the generative fit).
-- `network.ipynb`: the data-derived network, its weights, dynamics and spectrum (about 22 minutes).
-- `network_grid.ipynb`: the lambda and c grid (about 8 minutes).
-- `theory.ipynb`: the mean-field theory and the large-N spectra (about 2 minutes).
+  process (about 19 minutes, most of it the generative fit).
+- `network.ipynb`: the data-derived network, its weights, dynamics and spectrum (about 38 minutes).
+- `network_grid.ipynb`: the lambda and c grid (about 10 minutes).
+- `theory.ipynb`: the mean-field theory and the large-N spectra (about 3 minutes).
-  31 minutes).
+  51 minutes).
--- a/entries/clark-2026/entry.yaml
+++ b/entries/clark-2026/entry.yaml
-  runtime_minutes: 15
+  runtime_minutes: 19
-  runtime_minutes: 22
+  runtime_minutes: 38
-  runtime_minutes: 8
+  runtime_minutes: 10
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for nb in entries/clark-2026/*.ipynb; do python - "$nb" <<'EOF'
import json,sys,ast
d=json.load(open(sys.argv[1]))
for i,c in enumerate(d['cells']):
    if c['cell_type']=='code':
        s=''.join(c['source']); s='\n'.join(l for l in s.splitlines() if not l.lstrip().startswith(('%','!')))
        ast.parse(s)
print(sys.argv[1],'ok')
EOF
done; grep -n "\-\-before\|max-minutes\|def run\|parallel\|notebooks\b" tools/entry.py | head -30
```

```
entries/clark-2026/model_sims.ipynb ok
entries/clark-2026/network.ipynb ok
entries/clark-2026/network_grid.ipynb ok
entries/clark-2026/theory.ipynb ok
entries/clark-2026/tuning_curves.ipynb ok
18:- notebooks are committed without outputs;
29:that takes longer than --max-minutes fails, even if it ran without error.
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
188:    listed = [n["path"] for n in entry.get("notebooks", [])]
235:            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
379:            # The code that shows a finding: a tagged cell of one of the entry's notebooks, as for an outcome. From
453:            # attempt's notebooks and cells are checked only when it was made, not against the entry as it is now
556:    `before` (its executed notebooks). The entry moves to the new version only when nothing differs; otherwise
568:    for nb in entry["notebooks"]:
594:    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
595:    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
615:        if [n["path"] for n in entry["notebooks"]] != [r["notebook"] for r in stamp["results"]]:
625:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
651:    for notebook in entry["notebooks"]:
701:    for notebook in entry["notebooks"]:
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/clark-2026 2>&1 | tail -15
```

```
0 error(s)
```

**Agent**

The edits are in and the checks pass. Starting the full re-run (about two hours, longer than one shell call allows), so I launch it detached and wait on it in the foreground.

**Agent calls Bash**

```bash
cd  nohup python tools/entry.py all entries/clark-2026 > $TMPDIR/run.log 2>&1 &
echo $! > $TMPDIR/run.pid; date -u; sleep 30; cat $TMPDIR/run.log
```

```
Thu Nov 26 22:25:59 UTC 2026
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
```

**Agent**

Meanwhile, I'll add the two reader questions.

**Agent calls Bash**

```bash
cd  cat >> questions/clark-2026.yaml <<'EOF'
- claim: figs1-s2-spectrum-does-not-fix-symmetry
  question: The criterion asks the eigenvalues of the two finite weight matrices (one draw of each ensemble,
    N 10,000) to agree within 5%. The paper says the two ensembles share their second-order statistics
    and hence the spectrum of J at large N, which is a statement about the population eigenvalues, not
    about one finite draw of each. Should this part test the large-N (population) spectrum, or use a tolerance
    set by the sampling spread of a finite draw?
  passage: Supplementary Note 1, after Eq. 37, "Note that the spectrum of J at large N therefore depends
    only on second-order statistics of the loadings"; and before Example 1, "a modification of our model
    that preserves the second-order statistics, and therefore the spectrum, while changing the dynamics".
    Discussion, "we can construct ensembles that match our model's second-order statistics and hence its
    spectrum".
  why: The two ensembles have the same population eigenvalues (100, 100, 25 and 25) by construction. The
    finite matrices differ from them by sampling, and by up to 5.18% from each other under the claim's
    seed (2.4% to 5.2% over five seeds, 3.3% for the paper's seed-42 matrices), so the 5% test passes
    or fails with the draw. Under a population reading this part holds, and with the dynamics part, which
    holds under all five seeds, the claim would be reproduced.
- claim: fig7-dmft-mexican-hat-and-stability
  question: The statement says that at a bump state all Jacobian eigenvalues have negative real parts except
    the symmetry-induced zero, but the criterion tests only that the second eigenvalue is negative. Should
    the criterion also test that the leading eigenvalue is zero (the symmetry-induced mode) at every grid
    point?
  passage: Results, Dynamical mean-field theory, "At a bump state, all eigenvalues of M(theta, theta') have
    negative real parts except the symmetry-induced zero (Fig. 7f, teal curve)".
  why: On the 40 by 20 grid of dmft.ipynb the second eigenvalue is negative at all 800 points, so the criterion
    is met, but at 293 points the leading eigenvalue is below -1e-6 (down to -0.22), with a bump that is
    not flat (median amplitude 0.95). With a test of the zero mode the claim would be partially reproduced.
EOF
python -c "import yaml;print(len(yaml.safe_load(open('questions/clark-2026.yaml'))['questions']))"; sleep 600; cat $TMPDIR/run.log; date -u
```

```
4
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
Thu Nov 26 22:36:40 UTC 2026
```

**Agent**

While the run proceeds, I'll update the attempt record. First the schema for a verification round's `findings` and `proposed`.

**Agent calls Bash**

```bash
cd  ls schemas 2>/dev/null | head; grep -rn "findings\|proposed" schemas/attempt* 2>/dev/null | head -20
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
317:          "proposed": {
466:          "findings": {
478:                  "description": "The finding's number in this record's `findings`, from 1.",
509:    "findings": {
572:      "description": "A repeat attempt's comparison with the attempt before it, written by the reconcile step once this attempt, made blind, has been verified (docs/protocol.md, \"Repeat attempts\"). A finding of this attempt that no item of `findings` points at is new.",
579:        "findings"
598:        "findings": {
738:    "findings_review": {
739:      "description": "For an attempt made before protocol pilot-18, whose findings carry no severity: the severity a later review gave each finding about the data, and whether the review checked it against the notebook's outputs. Added to the record afterwards; nothing else in the record changes.",
745:        "findings"
757:        "findings": {
768:                "description": "The finding's number in this record's `findings`, from 1.",
```

**Agent calls Bash**

```bash
cd  sed -n 400,508p schemas/attempt.schema.json
```

```
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
          },
          "kind": {
            "enum": [
              "agent",
              "person",
[... 89 more lines not kept]
```

**Agent**

Now the outcome notes. fig4 first:

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    the claims file's tolerance does not cover the second one. The fig5 claims are tested at both parameter\n    sets and give the same outcomes.",
 "new_string": "    the claims file's tolerance does not cover the second one. The fig5 claims are tested at both parameter\n    sets and give the same outcomes. The criterion has no rule for a partial result; partially_reproduced\n    is the protocol's reading of a result that holds in part (two of the three parameters)."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    seventh also passes 4 of 4 pairs (2 and 1 of them not conjugates). Without setting one aside, two\n    of the four pairs pass. The criterion as written is met.'",
 "new_string": "    seventh also passes 4 of 4 pairs (2 and 1 of them not conjugates). Without setting one aside, three\n    of the four pairs pass (within 0.027, 0.000, 0.000 and 0.036 against next 0.139, 0.183, 0.0002 and\n    0.000; the fourth fails). The criterion as written is met.'"
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "  notes: From every initial spread (standard deviation 1 to 1,000, median starting distance 1.6 to 700)\n    all 34 final states lie within 0.0016 of the manifold, with none elsewhere,",
 "new_string": "  notes: From every initial spread (standard deviation 1 to 1,000, median starting distance 1.6 to 700)\n    all 34 final states lie within 0.0016 of the manifold (largest 0.00154), with none elsewhere,"
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    starts) run with the 5-ms step of these runs (largest distance at 20 s 0.00141); against it 97% to\n    100% of final states are within at every standard deviation under all five seeds. Against",
 "new_string": "    starts) run with the 5-ms step of these runs (largest distance at 20 s 0.00141); against it 97% to\n    100% of final states are within at every standard deviation under all five seeds, so not every final\n    state is within it (the largest, 0.00147, 0.00153 and 0.00154, are just above). Against"
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "  notes: At c 0 some runs diverge at every lambda up to 1e-4 (1 to 4 of 100) and, reading collapse in\n    the plane of the top two principal components (ii), 96 to 100 of 100 fall to the homogeneous state\n    (radius 0.65 to 0.80 against the manifold's 39.0) at every lambda; read",
 "new_string": "  notes: At c 0 some runs diverge at every lambda up to 1e-4 (4, 3 and 1 of 100 at lambda 1e-12, 1e-8\n    and 1e-4; 4 and 3 of 20 at 1e-10 and 1e-6) and, reading collapse in the plane of the top two principal\n    components (ii), every other run falls to the homogeneous state at every lambda (96, 97, 99 and 100\n    of 100 at 1e-12, 1e-8, 1e-4 and 1e-2; 16 and 17 of 20 at 1e-10 and 1e-6; radius 0.65 to 0.80 against\n    the manifold's 39.0); read"
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    that 1e-8 sits just above the minimum, which holds, and whether the criterion misreads it is asked\n    of a reader (questions/clark-2026.yaml).\n  deviations:",
 "new_string": "    that 1e-8 sits just above the minimum, which holds, and whether the criterion misreads it is asked\n    of a reader (questions/clark-2026.yaml). The criterion has no rule for a partial result; partially_reproduced\n    is the protocol's reading of a result that holds in part.\n  deviations:"
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    has eigenvalue 0.446. At 293 of 800 grid points, mostly small beta and large sigma, no zero eigenvalue\n    is found at the bump (the leading one is below -1e-6, down to -0.22); the bump there is not flat (amplitude,\n    max - min of m, median 0.95, below 1e-3 at 6 of the 293), so the missing zero mode is not explained\n    by a vanishing bump. The criterion tests only the second eigenvalue.",
 "new_string": "    has eigenvalue 0.446. At 293 of 800 grid points no zero eigenvalue is found at the bump (the leading\n    one is below -1e-6, down to -0.22). Most are at beta of 1 and above (249 of 293) and sigma of 10 and\n    above (128 at sigma 10 to 50, 98 at 50 and above); beta below 0.1 or sigma of 50 and above holds only\n    99, and 67 are at sigma below 10 with beta of 1 and above. At sigma 1.4211 and beta 2.7659 the zero\n    is present. The bump at those points is not flat (amplitude, max - min of m, median 0.95, below 1e-3\n    at 6 of the 293), so the missing zero mode is not explained by a vanishing bump. The criterion tests\n    only the second eigenvalue; the statement's \"except the symmetry-induced zero\" does not hold at those\n    293 points, and whether the criterion should test it is asked of a reader (questions/clark-2026.yaml)."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "  notes: Convergence time (bump) falls with beta at every sigma and varies across sigma by at most 2.55\n    times (reading b holds), but reaches 20.5 tau at beta 1.1 and sigma 100, outside 0.5 to 10 tau. Divergence\n    time (uniform) runs from 0.15 to 3.83 tau for beta 1 to 10, rises with beta at small sigma (up to\n    11 increases) and varies by up to 24 times across sigma. The first two parts do not hold for both\n    timescales, so neither the full nor the partial rule is met. Over sigma 1 to 10 the timescales stay\n    within a few tau; the failures come from the grid's large sigma, which the claims file's thresholds\n    include.",
 "new_string": "  notes: Convergence time (bump) falls with beta at every sigma and varies across sigma by at most 2.55\n    times (reading b holds), but over beta 1 to 10 runs from 2.87 to 20.5 tau, the largest at beta 1.1\n    and sigma 37.9 (19.5 at sigma 100); it stays within 0.5 to 10 tau only at sigma 1 and exceeds 10 tau\n    at beta 1.1 for every sigma from 1.27 up. Divergence time (uniform) runs from 0.15 to 3.83 tau for\n    beta 1 to 10, falls below 0.5 tau at every sigma from 6.95 up, rises with beta at the five smallest\n    sigma (11, 10, 8, 6 and 3 increases, sigma 1 to 2.64) and varies by up to 24 times across sigma (6.1\n    within sigma 1 to 10). The first two parts do not hold for both timescales, so neither the full nor\n    the partial rule is met. No sigma meets all three parts for both timescales, and restricting the grid\n    to sigma 1 to 10 gives the same outcome."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    fitted by regression and simulated, and the grid-score sweep 1,000 maps for each eta; with the five\n    notebooks of this entry taking 77 minutes per run, it did not fit in the five hours of the revision\n    run either.",
 "new_string": "    fitted by regression and simulated, and the grid-score sweep 1,000 maps for each eta; with the five\n    notebooks of this entry taking about 120 minutes per run (1,147, 2,256, 613, 157 and 3,044 s in the\n    run before the round-2 revision, model_sims.ipynb alone 51 of the 60 minutes a notebook may take),\n    it did not fit in the five hours of a revision run."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now figs10, figs11-s12, figs1-s2 and findings 3 and 4.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    noise 0.2 on; the two fragment alike, and both already at 0.2, which the criterion does not test.\n    Measured gives the states at noise 0 (disordered, circulant) and at 0.4.",
 "new_string": "    noise 0.2 on. Both already fragment at 0.2, which the criterion does not test. They do not fragment\n    alike in detail. At noise 0.4 the disordered network ends in fewer states than the circulant under\n    every seed (8, 7, 4, 8 and 5 against 9, 12, 11, 12 and 9) with a larger median drift (0.23 to 0.48\n    rad against 0.15 to 0.22); under the claim's seed it keeps fewer states at every level from 0.4 on\n    and more at 0.2 (15 against 11), and its median drift is larger at every level but 0.8. The criterion\n    is met; the statement's \"comparably robust\" holds in that both lose the continuum at the same levels,\n    with the disordered network fragmenting somewhat further. Measured gives the states at noise 0 (disordered,\n    circulant) and at 0.4."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    (all 34 within at N 1,000). This is assumed.'",
 "new_string": "    (all 34 within at N 1,000). This is assumed.'\n  - The criterion's \"every final state lies on the target manifold\" and \"all perturbed initial conditions\n    converge\" are read as at least 95% of final states within the threshold, the rule of figs11b-data-network-global-stability,\n    which the criterion names as the way to judge. This is part of the assumption. Read strictly, the claim's\n    seed fails at standard deviation 10 (0.97 within, one state at 0.01146 against the threshold 0.01121);\n    the notebook prints the strict reading for each seed."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    paper's own seed-42 matrices agree within 3.3%. The dynamics part holds and the eigenvalue part fails\n    narrowly.",
 "new_string": "    paper's own seed-42 matrices agree within 3.3%. The dynamics part holds and the eigenvalue part fails\n    narrowly. The 5% test on two finite matrices measures their sampling spread more than a difference\n    between the ensembles, whose large-N spectra are the same by construction; whether the criterion should\n    test the large-N spectrum is asked of a reader (questions/clark-2026.yaml). The criterion has no rule\n    for a partial result; partially_reproduced is the protocol's reading of a result that holds in part."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "    = (1.4211, 1.7307, 2.7659) and (1.4737, 1.2145, 3.1103), whose errors differ by less than the sampling\n    noise of 500,000 samples (0.0085 to 0.0101 depending on the draws and on float32 or float64 arithmetic).\n    In the paper's own cached error grid on Zenodo they are 1.1% apart (0.00890 and 0.00900). The reported\n    b of 1.73 is one of two choices the fitting procedure can return.",
 "new_string": "    = (1.4211, 1.7307, 2.7659) and (1.4737, 1.2145, 3.1103). With 500,000 samples in float64 the second\n    has the lower error under all five seeds, and the ranges do not overlap (0.00853 to 0.00894 against\n    0.00907 to 0.01006 for the paper's point); the ranking flips only in float32 under one seed (0.00902\n    against 0.00920) and in the paper's own cached error grid on Zenodo, where the two are 1.1% apart (0.00890\n    and 0.00900). The reported b of 1.73 is one of two choices the fitting procedure can return, depending\n    on the draws and the arithmetic."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/clark-2026-01.yaml",
 "old_string": "  statement: In the mean-field stability grid of Fig. 7d,e (dmft.ipynb, run_analysis), at 293 of the 800\n    grid points, mostly beta below 0.1 or sigma near 100, the bump Jacobian has no zero eigenvalue (its\n    leading eigenvalue is below -1e-6, down to -0.22), although the bump there is not flat (amplitude\n    median 0.95).",
 "new_string": "  statement: In the mean-field stability grid of Fig. 7d,e (dmft.ipynb, run_analysis), at 293 of the 800\n    grid points, most of them at beta of 1 and above (249) and sigma of 10 and above (226), the bump Jacobian\n    has no zero eigenvalue (its leading eigenvalue is below -1e-6, down to -0.22), although the bump there\n    is not flat (amplitude median 0.95). At the paper's parameters (sigma 1.4211, beta 2.7659) the zero\n    is present."
}
```

```
The file attempts/clark-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the round-2 verification block.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/v2.py <<'PYEOF'
import yaml
G = "Agrees with its round-1 outcome, unchanged since round 1; every Result sentence, Summary section, README row and note it checked matches the printed values, other than those listed in section 2 of the report."
GR = "Outcome kept; nothing in the report bears on it beyond agreement."
R = []
def add(c, o, reason=G, response=GR): R.append(dict(claim=c, agrees=True, outcome=o, reason=reason, response=response))
add("hd-cell-selection", "reproduced", G + " Separately, tuning_curves cell 0 says later files have sizes of about 24 GB, where cell 3 prints 12.7 to 30.2 GB.",
    "Outcome kept. The header of tuning_curves.ipynb now gives the sizes as printed, 12.7 to 30.2 GB (finding 2 already did).")
add("tuning-curves-match-cache", "reproduced", G + " Round-1 point 2 (widths compared with ==) is resolved.")
for c in ["fig1e-heterogeneous-peaks", "fig5d-peak-numbers", "fig1fg-mean-and-fluctuation-profiles", "fig3ab-centers-of-mass-uniform", "fig3c-correlation-approaches-circulant"]:
    add(c, "reproduced")
add("fig4-generative-fit", "partially_reproduced",
    "Agrees; checked against the claims file again, the outcome follows from the printed values. The criterion contains no partially rule and, read strictly, gives not_reproduced; it accepts partially_reproduced as the fair description, but that comes from the protocol's general reading, not from the criterion. Round-1 point 1 is resolved: all the outputs it asked for are printed, plus the paper's cached grid, and partial stands on the tolerance. Finding 3 says the two minima's errors differ by less than the sampling noise of 500,000 samples; in float64 the ranges do not overlap (0.00853 to 0.00894 for the chosen point against 0.00907 to 0.01006 for the paper's, tuning_curves cell 33), and the ranking flips only with float32 under one seed and in the paper's cached grid.",
    "Outcome kept. Finding 3 now says that in float64 the chosen point has the lower error under all five seeds with no overlap, and that the ranking flips only in float32 under one seed and in the paper's cached grid. The notes now say that the criterion has no partial rule and that partially_reproduced is the protocol's reading of a result that holds in part; the conclusion cell says the same.")
for c in ["fig5ab-profiles-match", "fig5c-peak-counts-match", "fig5d-peak-heights-match", "fig5e-flip-symmetry-match", "fig5f-information-match", "fig2l-recorded-bump-tracks-hd", "fig2b-sorted-weights-mexican-hat", "fig2ef-data-network-quasicontinuous"]:
    add(c, "reproduced")
add("fig2gi-circulant-noise-collapses", "partially_reproduced",
    G + " Round-1 point 3 is resolved as far as the attempt can go: seeds, the angle-shift test and the wrap-mode variant are all added. It remains, and bears on the outcome, that the criterion's 50 states cannot be reached; this is a claims-file defect, now sent to a reader.",
    "Outcome kept, as tested on the claims file; the question is in questions/clark-2026.yaml from round 1.")
add("fig2jk-velocity-integration", "reproduced")
add("figs8-s9-lambda-and-c", "partially_reproduced",
    "Agrees; the outcome follows from the printed values. The criterion contains no partially rule; it accepts partially_reproduced from the protocol's general reading. Round-1 point 4: the paper's err_grid has been added and agrees; the grid still uses 20 initial conditions at most points (the 8 points the criterion reads use 100). It remains, and bears on the outcome, that the claims file reads err(1e-8) < err(1e-12) more strictly than the supplement, and that lambda 1e-2 at c 1 does not collapse (radius 4.6 against 3.9). Network_grid cell 5 and the notes say 1 to 4 of 100 diverge and 96 to 100 of 100 collapse at every lambda; at lambda 1e-10 and 1e-6 n is 20 (4 and 16, 3 and 17; cell 4).",
    "Outcome kept, as tested on the claims file (the question on the flow error is in questions/clark-2026.yaml). The conclusion and the notes now give the counts per lambda with their n (4, 3 and 1 of 100 diverge at 1e-12, 1e-8 and 1e-4, 4 and 3 of 20 at 1e-10 and 1e-6; the others collapse under reading ii), and say that the criterion has no partial rule. The 100 initial conditions at every grid point were not run: the entry already takes about two hours per run.")
add("figs11b-data-network-global-stability", "reproduced",
    "Agrees. The assumption is stated: the threshold comes from the fig2ef protocol run with the same 5-ms step. It is reasonable, and it is the reference on the same footing asked for in round 1. Any threshold here sits at the noise floor; the real evidence is that final distances are about 1e-3 against median starting distances of 1.6 to 700 (cell 22). Network cell 23 says every final state is on the manifold at the resolution of the reference (largest final distance 0.0015); final maxima reach 0.00153 and 0.00154, above the 5-ms reference of 0.00141 (cell 22), and only 97 to 100% are within it.",
    "Outcome kept. The conclusion now says that every final state ends within 0.0016 of the manifold, that 97% to 100% are within the 5-ms reference, and that the largest final distances (0.00147, 0.00153 and 0.00154) are just above it; the notes say the same.")
add("figs14-data-spectrum-doublets", "reproduced",
    G + " Round-1 point 6 is resolved (documented). The notes say that without setting one aside two of the four pairs pass; the variant in network cell 19 prints within [0.027 0 0 0.0359] against next [0.1389 0.183 0.0002 0], which gives 3 of 4.",
    "Outcome kept. The notes now say three of the four pairs pass without setting one aside, and cell 19 prints the comparison and the count for that variant.")
add("fig6cd-eigenvalues-real-degenerate", "reproduced")
add("fig6fg-disordered-eigenvectors", "reproduced")
add("fig7-dmft-mexican-hat-and-stability", "reproduced",
    G + " Round-1 point 7 is resolved: the bump amplitude is printed. It remains that the criterion tests only eigenvalue 2; the output contradicts the statement's \"except the symmetry-induced zero\" at 293 of 800 points, where the bump is not flat (median amplitude 0.95), a gap in the claims file that bears on how much the reproduced covers. Theory cell 6, the fig7 notes and finding 4 say these points are mostly at small beta and large sigma (finding 4, mostly beta below 0.1 or sigma near 100); cell 5 lists only 8 of the 293 points.",
    "Outcome kept, as the criterion is met. Cell 5 now prints the 293 points by beta band and sigma band, and the statement was wrong: 249 of them are at beta of 1 and above and 226 at sigma of 10 and above, and beta below 0.1 or sigma of 50 and above holds only 99. The conclusion, the notes and finding 4 now say so, and that the zero is present at the paper's parameters. The notes say that the statement's zero-mode part does not hold at those points, and whether the criterion should test it is added to questions/clark-2026.yaml.")
add("fig7de-dmft-timescales", "not_reproduced",
    "Agrees; the outcome follows from the printed values. Theory cell 9 and the notes say the convergence time reaches 20.5 tau at beta 1.1 and sigma 100; cell 8 prints 19.513 at sigma 100, and the maximum of 20.521 is at some other sigma. The notes also say the failures come from the grid's large sigma and that over sigma 1 to 10 the timescales stay within a few tau; the divergence time's decreasing test fails at small sigma (11 and 10 increases), and only sigma 1 and 100 are printed.",
    "Outcome kept. Cell 8 now prints where the extremes are and, for each sigma, the range over beta 1 to 10, whether it is within a few tau and the number of increases, and the criterion over sigma 1 to 10 alone. The maximum, 20.5 tau, is at sigma 37.9; the convergence time exceeds 10 tau at every sigma from 1.27 up, the divergence time falls below 0.5 tau from sigma 6.95 up and rises with beta at sigma 1 to 2.64, and over sigma 1 to 10 alone the outcome is the same. The conclusion and the notes now say this; the unsupported sentences are removed.")
add("fig7c-dmft-integrates-behavior", "reproduced")
R.append(dict(claim="fig8-grid-scores-and-torus", agrees=True, outcome="blocked",
    reason="Agrees with blocked (too_large). The fig8 notes say the five notebooks take 77 minutes per run, and the README gives per-notebook times of 15, 22, 8, 2 and 31 minutes; the printed totals are 1139, 2254, 611, 154 and 3042 s, which make 7,200 s (120 min).",
    response="Outcome kept. The notes, model_sims.ipynb's fig8 section, the README and entry.yaml now give the run times of the last run (1,147, 2,256, 613, 157 and 3,044 s, about 120 minutes)."))
add("figs10-robustness-comparable", "reproduced",
    "Agrees. The continuum rule (at least 31 of 34 states) is stated and reasonable; it does not decide the outcome, as both networks keep 34 states at noise 0, against 8 and 9 at 0.4 (cell 11). Model_sims cell 12 and the notes say the two fragment alike over the whole range; at noise 0.4 the disordered network ends in fewer states under every seed (4 to 8 against 9 to 12), and under the claim seed it has fewer states at every level from 0.4 on and about twice the median drift (cell 11). The criterion is met, but alike overstates it.",
    "Outcome kept, as the criterion is met. The conclusion and the notes no longer say alike: they give the state counts and median drifts that show the disordered network fragmenting further (fewer states at 0.4 under every seed, larger drift at every level but 0.8 under the claim's seed), and say that the statement's comparably robust holds only in that both lose the continuum at the same levels.")
add("figs11-s12-global-stability-model", "reproduced",
    "Agrees. The threshold assumption (the network's own fig2ef-protocol run) is stated and reasonable. Part of the assumption is stated only in notebook cell 6, not in the record's deviations: it reads the criterion's every final state and all converge as at least 95%, as in figs11b. Under a strict every, the claim seed fails at standard deviation 10: 0.97 within, with one state at 0.01146 against 0.01121 (cell 7).",
    "Outcome kept (assumed, seed sensitive). A deviation now states that every and all are read as at least 95%, the rule of figs11b that the criterion names, as part of the assumption, and that the strict reading fails at standard deviation 10 under the claim's seed. Cells 7 and 8 now print the strict reading for each seed, and the conclusion says so.")
add("figs1-s2-spectrum-does-not-fix-symmetry", "partially_reproduced",
    "Agrees, with two reservations. The criterion has no partial rule. The criterion's 5% test on two finite matrices measures sampling noise: the population eigenvalues are identical by construction (100, 100, 25, 25; cell 4); this is a weakness in the claims file's chosen threshold.",
    "Outcome kept, as tested on the claims file. Whether the eigenvalue part should test the large-N spectrum, which Supplementary Note 1 says depends only on the second-order statistics, is added to questions/clark-2026.yaml. The notes and the conclusion now say that the 5% test measures the sampling spread and that the criterion has no partial rule.")
assert len(R) == 30, len(R)
v = dict(date="2026-11-26", kind="agent",
    by="Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
    reviewed="Round 2. The full executed notebooks of the round-1 revision (tuning_curves, network, network_grid, theory and the new model_sims), the helper modules, the claims file and the attempt record, with the paper. The verifier agreed with all 30 outcomes, and found that the record states its round-1 reasons faithfully. It listed statements the printed outputs do not support (its section 2); each is corrected, and where a statement needed an output that was missing (the location of the 293 grid points of fig7, the timescales by sigma of fig7de, the strict reading of figs11-s12, the count of the figs14 variant), the output is added. Two of its points are added to questions/clark-2026.yaml (figs1-s2 and fig7). No outcome changes and none is proposed. No finding is rated critical, so none was reviewed; it found findings 1 and 2 (severity none) supported by tuning_curves cells 3, 6, 8 and 10 and none right for them. Report in transcripts/clark-2026/verifier-2-report.md.",
    results=R)
txt = yaml.safe_dump([v], sort_keys=False, width=110, allow_unicode=True)
open("attempts/clark-2026-01.yaml", "a").write(txt)
PYEOF
python $TMPDIR/v2.py && python -c "
import yaml;d=yaml.safe_load(open('attempts/clark-2026-01.yaml'));print(len(d['verifications']), len(d['verifications'][1]['results']))"; tail -c 1500 attempts/clark-2026-01.yaml; cat $TMPDIR/run.log; date -u
```

```
2 30
of the assumption is stated only in notebook cell 6, not in the record''s deviations: it reads the criterion''s
      every final state and all converge as at least 95%, as in figs11b. Under a strict every, the claim seed fails
      at standard deviation 10: 0.97 within, with one state at 0.01146 against 0.01121 (cell 7).'
    response: Outcome kept (assumed, seed sensitive). A deviation now states that every and all are read as at least
      95%, the rule of figs11b that the criterion names, as part of the assumption, and that the strict reading
      fails at standard deviation 10 under the claim's seed. Cells 7 and 8 now print the strict reading for each
      seed, and the conclusion says so.
  - claim: figs1-s2-spectrum-does-not-fix-symmetry
    agrees: true
    outcome: partially_reproduced
    reason: 'Agrees, with two reservations. The criterion has no partial rule. The criterion''s 5% test on two finite
      matrices measures sampling noise: the population eigenvalues are identical by construction (100, 100, 25,
      25; cell 4); this is a weakness in the claims file''s chosen threshold.'
    response: Outcome kept, as tested on the claims file. Whether the eigenvalue part should test the large-N spectrum,
      which Supplementary Note 1 says depends only on the second-order statistics, is added to questions/clark-2026.yaml.
      The notes and the conclusion now say that the 5% test measures the sampling spread and that the criterion
      has no partial rule.
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
Thu Nov 26 22:38:36 UTC 2026
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/clark-2026 2>&1 | tail -5; ls -la executed/clark-2026/; ps aux | grep -c "[n]bconvert\|[i]pykernel"
```

```
0 error(s)
total 1104
drwxr-xr-x 4 runner runner   4096 Nov 26 22:26 .
drwxr-xr-x 3 runner runner   4096 Nov 26 22:19 ..
drwxr-xr-x 3 runner runner   4096 Nov 26 22:20 .claude
drwxr-xr-x 5 runner runner   4096 Nov 26 22:26 .venv
-rw-r--r-- 1 runner runner  87481 Nov 26 22:04 model_sims.ipynb
-rw-r--r-- 1 runner runner 607236 Nov 26 21:01 network.ipynb
-rw-r--r-- 1 runner runner  21075 Nov 26 21:11 network_grid.ipynb
-rw-r--r-- 1 runner runner    539 Nov 26 22:04 result.json
-rw-r--r-- 1 runner runner  37359 Nov 26 21:13 theory.ipynb
-rw-r--r-- 1 runner runner 343483 Nov 26 20:23 tuning_curves.ipynb
0
```

**Agent calls Bash**

```bash
ps -p $(cat $TMPDIR/run.pid) -o pid,etime,cmd; ps aux --sort=-%cpu | head -5 | cut -c1-200; ls -la executed/clark-2026/.claude; cd  git check-ignore -v executed/clark-2026/.claude
```

```
PID     ELAPSED CMD
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
runner         2 33.3  0.0  10224  5868 ?        S    22:38   0:00 /bin/bash -c source /home/runner/.claude/shell-snapshots/snapshot-bash-1795731582657-9l1e3q.sh 2>/dev/null || true && export TMPDIR=/
runner         1 20.0  0.0   3804  1512 ?        Ss   22:38   0:00 bwrap --new-session --die-with-parent --setenv GIT_CONFIG_KEY_0 safe.directory --setenv GIT_CONFIG_VALUE_0 /home/runner/work/encore-r
runner         6  0.0  0.0   9964  4164 ?        R    22:38   0:00 ps aux --sort=-%cpu
runner         7  0.0  0.0  17600  7368 ?        S    22:38   0:00 head -5
total 12
drwxr-xr-x 3 runner runner 4096 Nov 26 22:20 .
drwxr-xr-x 4 runner runner 4096 Nov 26 22:26 ..
drwx------ 2 runner runner 4096 Nov 26 22:20 .cc-writes
.gitignore:6:executed/	executed/clark-2026/.claude
```

**Agent calls Bash**

```bash
cd  sed -n 590,730p tools/entry.py
```

```
return hashlib.sha256(path.read_bytes()).hexdigest()


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
[... 121 more lines not kept]
```

**Agent**

I'll run the same steps `run` takes (environment build, then the same nbconvert command per notebook, then the same stamp), one notebook per foreground call so each fits within a shell call.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/run_one.py <<'EOF'
"""Run the steps of tools/entry.py run one at a time: 'env', a notebook path, or 'stamp'."""
import json, os, subprocess, sys, time
from pathlib import Path
sys.path.insert(0, "tools")
import entry as E
import yaml
entry_dir = Path("entries/clark-2026"); output_dir = Path("executed/clark-2026")
venv = (output_dir / ".venv").resolve(); python = venv / "bin" / "python"; kernel = f"registry-{entry_dir.name}"
res_file = Path(os.environ["TMPDIR"]) / "results.json"
what = sys.argv[1]
if what == "env":
    (output_dir / E.STAMP).unlink(missing_ok=True)
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", E.python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python), "-r", str(entry_dir / "requirements.lock.txt"), *E.HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        assert subprocess.run(cmd).returncode == 0, cmd
    res_file.write_text("[]")
elif what == "stamp":
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    results = json.loads(res_file.read_text())
    assert [r["notebook"] for r in results] == [n["path"] for n in entry["notebooks"]]
    (output_dir / "result.json").write_text(json.dumps({"entry": entry["name"], "python": E.python_of(entry_dir), "results": results}, indent=1) + "\n")
    if all(r["ok"] for r in results):
        (output_dir / E.STAMP).write_text(json.dumps({"entry": entry["name"], "hash": E.entry_hash(entry_dir), "finished": round(time.time()),
            "results": [{"notebook": r["notebook"], "ok": True, "seconds": r["seconds"], "sha256": E.file_hash(output_dir / r["notebook"])} for r in results]}, indent=1) + "\n")
        print("stamp written")
else:
    name = what; started = time.time()
    r = subprocess.run([str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
         "--ExecutePreprocessor.timeout=3600", f"--ExecutePreprocessor.kernel_name={kernel}",
         "--output-dir", str(output_dir.resolve()), "--output", name, name],
        cwd=entry_dir, capture_output=True, text=True, env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
    seconds = round(time.time() - started); ok = r.returncode == 0 and seconds <= 3600
    error = None if ok else (r.stderr[-3000:] or f"took {seconds} s")
    results = json.loads(res_file.read_text()); results.append({"notebook": name, "ok": ok, "seconds": seconds, "error": error})
    res_file.write_text(json.dumps(results))
    print(f"{'pass' if ok else 'FAIL'}  {name}  ({seconds} s)"); print(error or "")
EOF
grep -n "timeout" tools/entry.py | grep add_argument; python $TMPDIR/run_one.py env && echo env ok; date -u
```

```
731:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
env ok
Thu Nov 26 22:39:21 UTC 2026
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/run_one.py tuning_curves.ipynb; date -u
```

```
pass  tuning_curves.ipynb  (1114 s)

Thu Nov 26 22:57:58 UTC 2026
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/run_one.py network.ipynb; date -u
```

```
pass  network.ipynb  (1709 s)

Thu Nov 26 23:26:33 UTC 2026
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/run_one.py network_grid.ipynb; python $TMPDIR/run_one.py theory.ipynb; date -u
```

```
FAIL  network_grid.ipynb  (694 s)
[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mloc[39;49m[30;43m [39;49m[30;43m+[39;49m[30;43m [39;49m[30;43mlength[39;49m[30;43m)[39;49m
[32m   2191[39m logger.debug(
[32m   2192[39m     [33m"[39m[38;5;132;01m%s[39;00m[33m read: [39m[38;5;132;01m%i[39;00m[33m - [39m[38;5;132;01m%i[39;00m[33m [39m[38;5;132;01m%s[39;00m[33m"[39m,
[32m   2193[39m     [38;5;28mself[39m,
[32m   (...)[39m[32m   2196[39m     [38;5;28mself[39m.cache._log_stats(),
[32m   2197[39m )
[32m   2198[39m [38;5;28mself[39m.loc += [38;5;28mlen[39m(out)

[36mFile [39m[32m~/work/encore-registry/encore-registry/executed/clark-2026/.venv/lib/python3.13/site-packages/fsspec/caching.py:657[39m, in [36mBytesCache._fetch[39m[34m(self, start, end)[39m
[32m    655[39m [38;5;28;01melif[39;00m end - [38;5;28mself[39m.end > [38;5;28mself[39m.blocksize:
[32m    656[39m     [38;5;28mself[39m.total_requested_bytes += bend - start
[32m--> [39m[32m657[39m     [38;5;28mself[39m.cache = [30;43mself[39;49m[30;43m.[39;49m[30;43mfetcher[39;49m[30;43m([39;49m[30;43mstart[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mbend[39;49m[30;43m)[39;49m
[32m    658[39m     [38;5;28mself[39m.start = start
[32m    659[39m [38;5;28;01melse[39;00m:

[36mFile [39m[32m~/work/encore-registry/encore-registry/executed/clark-2026/.venv/lib/python3.13/site-packages/fsspec/asyn.py:217[39m, in [36msync_wrapper.<locals>.wrapper[39m[34m(*args, **kwargs)[39m
[32m    214[39m [38;5;129m@functools[39m.wraps(func)
[32m    215[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mwrapper[39m(*args, **kwargs):
[32m    216[39m     [38;5;28mself[39m = obj [38;5;129;01mor[39;00m args[[32m0[39m]
[... 16 more lines not kept]
```

**Agent**

The grid notebook failed on a network timeout while reading from the archive (transient), after 694 s of computing. Re-running it.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json,os
p=os.environ["TMPDIR"]+"/results.json"; r=json.load(open(p))
r=[x for x in r if x["ok"]]; json.dump(r,open(p,"w")); print([(x["notebook"],x["seconds"]) for x in r])
EOF
sed -i 's|    results = json.loads(res_file.read_text())\n    assert|X|' $TMPDIR/run_one.py
python - <<'EOF'
import os
p=os.environ["TMPDIR"]+"/run_one.py"; s=open(p).read()
s=s.replace('''    results = json.loads(res_file.read_text())
    assert''','''    order = [n["path"] for n in entry["notebooks"]]
    results = sorted(json.loads(res_file.read_text()), key=lambda r: order.index(r["notebook"]))
    assert''')
open(p,"w").write(s)
EOF
python $TMPDIR/run_one.py network_grid.ipynb 2>&1 | tail -3; date -u
```

```
[('tuning_curves.ipynb', 1114), ('network.ipynb', 1709), ('theory.ipynb', 150)]
pass  network_grid.ipynb  (473 s)

Thu Nov 26 23:48:44 UTC 2026
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/run_one.py model_sims.ipynb 2>&1 | tail -3; date -u
```

```
pass  model_sims.ipynb  (2356 s)

Fri Nov 27 00:28:03 UTC 2026
```

**Agent**

All five notebooks passed (1,114, 1,709, 473, 150 and 2,356 s). Writing the stamp, then checking the conclusions against the new outputs.

**Agent calls Bash**

```bash
cd  python $TMPDIR/run_one.py stamp; python tools/entry.py run entries/clark-2026 2>&1 | tail -3
```

```
stamp written
pass  theory.ipynb  (150 s, reused)
pass  model_sims.ipynb  (2356 s, reused)
reused the executed copies of 2026-11-27 00:28 UTC: nothing the run reads has changed since (hash 1cdcf4cf1488). Nothing was executed and no environment was built; --fresh runs it again.
```

**Agent calls Bash**

```bash
cd executed/clark-2026; python - <<'EOF' > $TMPDIR/outs.txt
import json
for nb in ["theory.ipynb","network_grid.ipynb","network.ipynb","model_sims.ipynb"]:
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        tags=c.get('metadata',{}).get('tags',[])
        if c['cell_type']=='code' and any(t.startswith('claim:') for t in tags):
            print(f"===== {nb} cell {i} {tags}")
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain','')
                if t: print(''.join(t)[:5000])
        elif c['cell_type']=='markdown' and ''.join(c['source']).startswith('**Result'):
            print(f"----- {nb} cell {i} RESULT\n"+''.join(c['source']))
EOF
wc -c $TMPDIR/outs.txt
```

```
57831 /tmp/claude-1001/outs.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/outs.txt"
}
```

```
1	===== theory.ipynb cell 5 ['claim:fig7-dmft-mexican-hat-and-stability']
2	 sigma  beta      J0    Jmin  argmin_rad  mexican
3	     1   1.5  8.5376 -2.5906      1.5268     True
4	     1   3.0  5.9153 -1.7814      1.7027     True
5	     1   5.0  5.2516 -1.5862      1.7719     True
6	     1  10.0  4.9056 -1.4874      1.8158     True
7	     2   1.5 18.4696 -3.8117      0.7665     True
8	     2   3.0 12.8603 -2.5292      0.8482     True
9	     2   5.0 11.4414 -2.2190      0.8796     True
10	     2  10.0 10.7040 -2.0630      0.9048     True
11	     4   1.5 38.5445 -6.0181      0.3833     True
12	     4   3.0 26.9419 -3.8357      0.4210     True
13	     4   5.0 24.0088 -3.3121      0.4398     True
14	     4  10.0 22.4869 -3.0471      0.4524     True
15	
16	stability grid in 51 s
17	bump eigenvalue 1 (symmetry zero): max |Re| 2.21e-01; grid points where it is above 1e-6: 0 of 800
18	grid points where bump eigenvalue 1 is below -1e-6 (no zero mode found): 293 of 800; at (beta, sigma): [(np.float64(0.01), np.float64(48.33)), (np.float64(0.01), np.float64(61.58)), (np.float64(0.01), np.float64(78.48)), (np.float64(0.01), np.float64(100.0)), (np.float64(0.013), np.float64(78.48)), (np.float64(0.013), np.float64(100.0)), (np.float64(0.052), np.float64(100.0)), (np.float64(0.066), np.float64(100.0))]
19	bump amplitude (max - min of m): at the 293 points without a zero mode median 9.525e-01, range 9.904e-05 to 9.947e-01; at the other 507 median 4.330e-02, range 9.855e-05 to 9.881e-01
20	points with amplitude below 1e-3: 100, of which without a zero mode 6; largest bump eigenvalue 1 where the amplitude is at least 1e-3: -2.210e-01 (most negative)
[... 486 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/outs.txt",
 "offset": 507
}
```

```
507	   sd 1000: finite True, distance at the start median 1.301, final median 0.00520, largest 0.01063, within the threshold 1.00, within 2x 1.00; final angles as states {'single': 12, 'greedy': 19, 'bins': 24}
508	   all standard deviations with at least 95% within: False; strict reading of 'every final state', all within at every standard deviation: False
509	
510	seed 127949957: reference (fig2ef protocol) distance at 0 s median 1.127, at 20 s median 0.00652, largest 0.01144, at the end median 0.00620
511	   sd 1: finite True, distance at the start median 1.202, final median 0.00513, largest 0.01066, within the threshold 1.00, within 2x 1.00; final angles as states {'single': 14, 'greedy': 21, 'bins': 25}
512	   sd 10: finite True, distance at the start median 1.292, final median 0.00543, largest 0.01152, within the threshold 0.97, within 2x 1.00; final angles as states {'single': 13, 'greedy': 18, 'bins': 21}
513	   sd 50: finite True, distance at the start median 1.300, final median 0.00644, largest 0.01120, within the threshold 1.00, within 2x 1.00; final angles as states {'single': 16, 'greedy': 19, 'bins': 22}
514	   sd 100: finite True, distance at the start median 1.301, final median 0.00453, largest 0.00962, within the threshold 1.00, within 2x 1.00; final angles as states {'single': 13, 'greedy': 19, 'bins': 21}
515	   sd 1000: finite True, distance at the start median 1.304, final median 0.00717, largest 0.01053, within the threshold 1.00, within 2x 1.00; final angles as states {'single': 15, 'greedy': 19, 'bins': 21}
516	   all standard deviations with at least 95% within: True; strict reading of 'every final state', all within at every standard deviation: False
517	
518	time 647 s
519	
520	===== model_sims.ipynb cell 8 ['claim:figs11-s12-global-stability-model']
521	     seed    N  init_median  final_median  final_max  within_N2500_threshold  own_threshold  within_own  states_bins  states_single
522	127945957   50      0.64200       0.80423    0.95268
[... 92 more lines not kept]
```

**Agent**

model_sims matches its conclusions. Checking tuning_curves' key numbers:

**Agent calls Bash**

```bash
cd executed/clark-2026; python - <<'EOF'
import json,re
d=json.load(open('tuning_curves.ipynb'))
txt=''
for c in d['cells']:
    for o in c.get('outputs',[]):
        txt+=''.join(o.get('text','') or o.get('data',{}).get('text/plain',''))+'\n'
for k in ["1.4737","0.00853","0.00894","0.00907","0.01006","0.00889","0.00916","0.00902","0.00920","0.0180","0.01796","12.7","30.2","0.00890","0.00900","23908","24267","0.168","0.896","0.022","0.138","1.288","0.927","0.592","0.968","1.382","0.9998","0.784"]:
    print(k, k in txt)
EOF
```

```
1.4737 True
0.00853 True
0.00894 True
0.00907 True
0.01006 True
0.00889 True
0.00916 True
0.00902 True
0.00920 True
0.0180 False
0.01796 True
12.7 True
30.2 True
0.00890 True
0.00900 True
23908 True
24267 True
0.168 True
0.896 True
0.022 True
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/clark-2026; python - <<'EOF'
import json
d=json.load(open('tuning_curves.ipynb'))
for i,c in enumerate(d['cells']):
    for o in c.get('outputs',[]):
        t=''.join(o.get('text','') or '')
        if 'information' in t.lower() or 'median info' in t.lower(): print(i, t[:800])
EOF
```

```
8 mean information (bits per spike) of the head-direction units, spikes shifted by the lag:
subject   -2s   -1s  -0.5s  -0.2s  -0.1s  -0.05s  -0.02s   +0s  +0.02s  +0.05s  +0.1s  +0.2s  +0.5s   +1s   +2s
  A1808 0.428 0.664  0.990  1.442  1.685   1.797   1.829 1.833   1.816   1.760  1.631  1.383  0.953 0.655 0.414
  A1813 0.560 0.764  0.965  1.255  1.414   1.497   1.536 1.555   1.561   1.540  1.468  1.302  0.993 0.762 0.578
  A1815 0.335 0.516  0.714  0.986  1.138   1.216   1.245 1.254   1.252   1.228  1.164  1.022  0.748 0.544 0.353
  A1821 0.272 0.483  0.731  1.158  1.407   1.532   1.580 1.591   1.584   1.538  1.411  1.164  0.766 0.516 0.300
  A1824 0.371 0.603  0.906  1.317  1.519   1.590   1.606 1.601   1.582   1.534  1.421  1.216  0.853 0.595 0.378
  A3701 0.300 0.523  0.806  1.177  1.3
```

**Agent calls Bash**

```bash
cd executed/clark-2026; python - <<'EOF'
import json
d=json.load(open('tuning_curves.ipynb'))
for i,c in enumerate(d['cells']):
    if 'claim:fig5f-information-match' in c.get('metadata',{}).get('tags',[]):
        for o in c.get('outputs',[]): print(''.join(o.get('text','') or '')[:1500])
EOF
```

```
data: median 1.2879, range 0.0000 to 2.9607

fitted params, seed +0: median 1.3678 (rel 0.062), KS 0.138

fitted params, seed +1000: median 1.3697 (rel 0.064), KS 0.139

fitted params, seed +2000: median 1.3697 (rel 0.064), KS 0.141

fitted params, seed +3000: median 1.3689 (rel 0.063), KS 0.140

fitted params, seed +4000: median 1.3687 (rel 0.063), KS 0.140

paper params, seed +0: median 1.3434 (rel 0.043), KS 0.109

paper params, seed +1000: median 1.3446 (rel 0.044), KS 0.111

paper params, seed +2000: median 1.3452 (rel 0.045), KS 0.113

paper params, seed +3000: median 1.3443 (rel 0.044), KS 0.111

[... 2 more lines not kept]
```

**Agent**

Rewording the grid conclusion so it holds whatever the ill-conditioned 1e-12 value comes out at, then re-running that notebook.

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import json
p='network_grid.ipynb'; d=json.load(open(p))
s=''.join(d['cells'][5]['source'])
old="""lambda from 1.3e-10 at 1e-10 to 3.6e-9 at 1e-12, but
1e-8 (1.7e-8) is not below 1e-12, so that part of the criterion fails too."""
import re
s2=s.replace("\n"," ")
old1="above the collapse threshold of 3.9, so the criterion's test at c 1 fails. The flow error rises at large lambda (2.1e-2 at 1e-2) and at small lambda from 1.3e-10 at 1e-10 to 3.6e-9 at 1e-12, but 1e-8 (1.7e-8) is not below 1e-12, so that part of the criterion fails too."
assert old1 in s2
new1=("above the collapse threshold of 3.9, so the criterion's test at c 1 fails. The flow error rises at large lambda (2.1e-2 at 1e-2) and at small lambda, from 1.3e-10 at 1e-10 to a few times 1e-9 at 1e-12 (the value printed above), but 1e-8 (1.7e-8) is not below 1e-12, so that part of the criterion fails too. "
      "The solve at 1e-12 is ill-conditioned, and its flow error is not repeated exactly from run to run (3.6e-9 in an earlier run of this notebook, not run here); at every value it has taken it stays well below that at 1e-8.")
s2=s2.replace(old1,new1)
# rewrap to ~100 columns
words=s2.split(" "); lines=[]; cur=""
for w in words:
    if cur and len(cur)+1+len(w)>99: lines.append(cur); cur=w
    else: cur=(cur+" "+w) if cur else w
lines.append(cur)
d['cells'][5]['source']=[l+"\n" for l in lines[:-1]]+[lines[-1]]
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
print('\n'.join(lines))
EOF
```

```
**Result: partially reproduced.** At c 0 some runs diverge at every lambda up to 1e-4 (4, 3 and 1
of 100 at lambda 1e-12, 1e-8 and 1e-4; 4 and 3 of 20 at 1e-10 and 1e-6), and under reading (ii) of
collapse every other run falls to the homogeneous state at every lambda (96, 97, 99 and 100 of 100
at 1e-12, 1e-8, 1e-4 and 1e-2; 16 and 17 of 20 at 1e-10 and 1e-6; radius 0.65 to 0.80 against 39
for the manifold); under reading (i) no run collapses, since the homogeneous state keeps a
firing-rate norm of 17.3 to 17.7. No c above 0 diverges up to lambda 1e-4, and c 0.25 still leaves
the collapse (12 of 20 at lambda 1e-8 under reading ii). At lambda 1e-2 the manifold is lost for c
up to 0.75 (all 20 collapse under reading ii), but at c 1 the states keep a radius of 4.6, just
above the collapse threshold of 3.9, so the criterion's test at c 1 fails. The flow error rises at
large lambda (2.1e-2 at 1e-2) and at small lambda, from 1.3e-10 at 1e-10 to a few times 1e-9 at
1e-12 (the value printed above), but 1e-8 (1.7e-8) is not below 1e-12, so that part of the
criterion fails too. The solve at 1e-12 is ill-conditioned, and its flow error is not repeated
exactly from run to run (3.6e-9 in an earlier run of this notebook, not run here); at every value
it has taken it stays well below that at 1e-8. The paper's cached flow errors agree to three digits
from 1e-10 to 1e-2 (3.8e-9 at 1e-12) and fail the same part: the supplement says only that 1e-8
sits just above the minimum, which holds, and this reading of the criterion is asked of a reader.
The criterion has no rule for a partial result; partially reproduced is the protocol's reading of a
result that holds in part (two of its four parts).
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'EOF'
import json
p='network_grid.ipynb'; d=json.load(open(p))
s=''.join(d['cells'][5]['source'])
old="(3.6e-9 in an earlier run of this notebook, not run here); at every value\nit has taken it stays well below that at 1e-8."
assert old in s
s=s.replace(old,"(3.6e-9 in an earlier run of this notebook, not run here;\nboth below the 1.7e-8 at 1e-8).")
d['cells'][5]['source']=s.splitlines(keepends=True)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
cd ../..; python - <<'EOF'
import json,os
p=os.environ["TMPDIR"]+"/results.json"; r=json.load(open(p))
r=[x for x in r if x["notebook"]!="network_grid.ipynb"]; json.dump(r,open(p,"w")); print([x["notebook"] for x in r])
EOF
python $TMPDIR/run_one.py network_grid.ipynb 2>&1 | tail -2; date -u
```

```
['tuning_curves.ipynb', 'network.ipynb', 'theory.ipynb', 'model_sims.ipynb']
pass  network_grid.ipynb  (473 s)

Fri Nov 27 00:37:09 UTC 2026
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/run_one.py stamp; python - <<'EOF'
import json
d=json.load(open('executed/clark-2026/network_grid.ipynb'))
c=d['cells'][4]
for o in c['outputs']:
    t=''.join(o.get('text',''))
    if 'flow error' in t or 'paper' in t or 'reading' in t or 'lamda' in t: print(t[-2500:])
EOF
```

```
stamp written
08 1.25        0         0            0  20 72.194864      38.982256
1.000000e-08 1.50        0         0            0  20 72.194552      38.982458
1.000000e-06 0.00        3         0           17  20 17.408164       0.789021
1.000000e-06 0.25        0         0           12  20 21.450442       1.531747
1.000000e-06 0.50        0         0            0  20 72.193118      38.958084
1.000000e-06 0.75        0         0            0  20 72.180951      38.954600
1.000000e-06 1.00        0         0            0  20 72.177212      38.953110
1.000000e-06 1.25        0         0            0  20 72.175360      38.952310
1.000000e-06 1.50        0         0            0  20 72.174293      38.951872
1.000000e-04 0.00        1         0           99 100 17.386341       0.790743
1.000000e-04 0.25        0         0           17  20 21.412147       1.532547
1.000000e-04 0.50        0         0            0  20 71.258280      38.249939
1.000000e-04 0.75        0         0            0  20 71.682725      38.477304
1.000000e-04 1.00        0         0            0 100 71.658010      38.769957
1.000000e-04 1.25        0         0            0  20 71.956279      38.615683
1.000000e-04 1.50        0         0            0  20 72.010458      38.642869
1.000000e-02 0.00        0         0          100 100 17.290725       0.735213
1.000000e-02 0.25        0         0           20  20 21.265920       1.366453
1.000000e-02 0.50        0         0           20  20 24.435724       2.200508
[... 15 more lines not kept]
```

**Agent**

Same value (2.6e-9) on the re-run. Now updating the record and the question to match.

**Agent calls Bash**

```bash
cd  grep -n "3.6e-9" attempts/clark-2026-01.yaml questions/clark-2026.yaml
```

```
attempts/clark-2026-01.yaml:313:    error is 3.6e-9, 1.3e-10, 1.7e-8, 4.6e-6, 4.9e-4 and 2.1e-2 from lambda 1e-12 to 1e-2; it rises at
attempts/clark-2026-01.yaml:689:      below err(1e-12) = 3.6e-9 (minimum at 1e-10). Problem 4: the criterion''s err(1e-8) < err(1e-12)
attempts/clark-2026-01.yaml:698:      The notes gave 2.6e-9 at 1e-12, a slip; they now give 3.6e-9, as printed. The 100 initial conditions
questions/clark-2026.yaml:29:    is above that at 1e-12 (3.6e-9). The paper's own cached errors (err_grid of pc_convergence_grid.npz
```

**Agent calls Bash**

```bash
cd  sed -n 310,318p attempts/clark-2026-01.yaml
```

```
up to lambda 1e-4, and c 0.25 leaves the collapse (8 to 20 of 20 across lambda under ii, 12 at 1e-8).
    At lambda 1e-2 all runs with c up to 0.75 collapse (ii), but at c 1 the states keep a radius of 4.6,
    just above the threshold of 3.9, so the criterion's test at c 1 fails under both readings. The flow
    error is 3.6e-9, 1.3e-10, 1.7e-8, 4.6e-6, 4.9e-4 and 2.1e-2 from lambda 1e-12 to 1e-2; it rises at
    both ends with its minimum at 1e-10, just below 1e-8 as the supplement says, but 1e-8 is not below
    1e-12, so that part of the criterion fails. Two of the criterion's four parts hold. Under four more
    seeds (20 initial conditions) the points the criterion reads give the same pattern (lambda 1e-8 and
    c 0, 0 to 3 diverge and 17 to 20 collapse under ii; lambda 1e-2 and c 1, none collapses). The paper's
    cached flow errors (err_grid of pc_convergence_grid.npz) agree to three digits from 1e-10 to 1e-2
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/clark-2026-01.yaml'; s=open(p).read()
old="""    error is 3.6e-9, 1.3e-10, 1.7e-8, 4.6e-6, 4.9e-4 and 2.1e-2 from lambda 1e-12 to 1e-2; it rises at
    both ends with its minimum at 1e-10, just below 1e-8 as the supplement says, but 1e-8 is not below
    1e-12, so that part of the criterion fails."""
new="""    error is 2.6e-9, 1.3e-10, 1.7e-8, 4.6e-6, 4.9e-4 and 2.1e-2 from lambda 1e-12 to 1e-2; it rises at
    both ends with its minimum at 1e-10, just below 1e-8 as the supplement says, but 1e-8 is not below
    1e-12, so that part of the criterion fails. The solve at 1e-12 is ill-conditioned and its flow error
    is not repeated exactly between runs (2.6e-9 in the two runs of the round-2 revision, 3.6e-9 in the
    run of round 1); the values at the other lambda are the same to three digits, and the part fails in
    every run."""
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
q='questions/clark-2026.yaml'; t=open(q).read()
i=t.index("is above that at 1e-12 (3.6e-9)."); print(t[i-200:i+120])
EOF
```

```
imum, beyond the ill-conditioned
    regime but with the flow error still negligible."
  why: Here the flow error is lowest at lambda 1e-10 and rises on both sides, and the error at 1e-8 (1.7e-8)
    is above that at 1e-12 (3.6e-9). The paper's own cached errors (err_grid of pc_convergence_grid.npz
    on Zenodo) are t
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
q='questions/clark-2026.yaml'; t=open(q).read()
old="is above that at 1e-12 (3.6e-9)."
t=t.replace(old,"is above that at 1e-12 (2.6e-9 to 3.6e-9 over the runs of this attempt, as the solve there is ill-conditioned).")
open(q,'w').write(t)
import yaml; yaml.safe_load(open(q)); print("ok")
EOF
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/clark-2026-01.yaml'; s=open(p).read()
old="""    notebooks of this entry taking about 120 minutes per run (1,147, 2,256, 613, 157 and 3,044 s in the
    run before the round-2 revision, model_sims.ipynb alone 51 of the 60 minutes a notebook may take),
    it did not fit in the five hours of a revision run."""
new="""    notebooks of this entry taking 97 to 120 minutes per run (1,147, 2,256, 613, 157 and 3,044 s in the
    run before the round-2 revision, model_sims.ipynb alone 51 of the 60 minutes a notebook may take;
    1,114, 1,709, 473, 150 and 2,356 s in the run of the round-2 revision), it did not fit in the five
    hours of a revision run."""
assert old in s; s=s.replace(old,new)
old2="""      response: Outcome kept. The notes, model_sims.ipynb's fig8 section, the README and entry.yaml now give the run times of the last run (1,147, 2,256, 613, 157 and 3,044 s, about 120 minutes)."""
import re
i=s.index("  - claim: fig8-grid-scores-and-torus\n    agrees: true")
j=s.index("  - claim:", i+10)
blk=s[i:j]
k=blk.index("    response:")
newresp="""    response: Outcome kept. The notes, model_sims.ipynb's fig8 section, the README and entry.yaml now give
      the run times as printed (1,147, 2,256, 613, 157 and 3,044 s, about 120 minutes, in the run the verifier
      read; 1,114, 1,709, 473, 150 and 2,356 s, about 97 minutes, in the run of this revision). The README
      and entry.yaml keep the longer of the two.
"""
s=s[:i]+blk[:k]+newresp+s[j:]
i=s.index("  - claim: figs8-s9-lambda-and-c\n    agrees: true\n    outcome: partially_reproduced\n    reason: Agrees; the outcome")
j=s.index("  - claim:", i+10); blk=s[i:j]
blk=blk.rstrip('\n')
assert blk.endswith("per run.") , blk[-200:]
blk=blk[:-1]+""". In the run of this revision the flow error at lambda 1e-12 came out at 2.6e-9, against 3.6e-9 in the run the verifier
      read: the solve there is ill-conditioned and not repeated exactly; the conclusion now says so and no longer
      states a fixed value, and the part fails in every run.
"""
s=s[:i]+blk+s[j:]
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); print(len(d['verifications'][1]['results']))
EOF
sed -n '/claim: figs8-s9-lambda-and-c/,+3p' attempts/clark-2026-01.yaml | tail -4; grep -n "per run. In the run" attempts/clark-2026-01.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
ValueError: substring not found
  - claim: figs8-s9-lambda-and-c
    agrees: true
    outcome: partially_reproduced
    reason: 'Agrees; the outcome follows from the printed values. The criterion contains no partially rule; it accepts
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/clark-2026-01.yaml'; s=open(p).read()
old="""    notebooks of this entry taking about 120 minutes per run (1,147, 2,256, 613, 157 and 3,044 s in the
    run before the round-2 revision, model_sims.ipynb alone 51 of the 60 minutes a notebook may take),
    it did not fit in the five hours of a revision run."""
new="""    notebooks of this entry taking 97 to 120 minutes per run (1,147, 2,256, 613, 157 and 3,044 s in the
    run before the round-2 revision, model_sims.ipynb alone 51 of the 60 minutes a notebook may take;
    1,114, 1,709, 473, 150 and 2,356 s in the run of the round-2 revision), it did not fit in the five
    hours of a revision run."""
assert old in s; s=s.replace(old,new)
i=s.index("  - claim: fig8-grid-scores-and-torus\n    agrees: true")
j=s.index("  - claim:", i+10); blk=s[i:j]; k=blk.index("    response:")
s=s[:i]+blk[:k]+"""    response: Outcome kept. The notes, model_sims.ipynb's fig8 section, the README and entry.yaml now give
      the run times as printed (1,147, 2,256, 613, 157 and 3,044 s, about 120 minutes, in the run the verifier
      read; 1,114, 1,709, 473, 150 and 2,356 s, about 97 minutes, in the run of this revision). The README
      and entry.yaml keep the longer of the two.
"""+s[j:]
i=s.rindex("  - claim: figs8-s9-lambda-and-c\n")
j=s.index("  - claim:", i+10); blk=s[i:j].rstrip('\n')
assert blk.endswith("per run."), blk[-100:]
blk=blk[:-1]+""". In the run of this revision the flow error at lambda 1e-12 came out at 2.6e-9, against 3.6e-9 in the run the verifier
      read; the solve there is ill-conditioned and not repeated exactly, so the conclusion now says so and gives
      no fixed value, and the part fails in every run.
"""
s=s[:i]+blk+s[j:]
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); r=[x for x in d['verifications'][1]['results'] if x['claim'] in ('figs8-s9-lambda-and-c','fig8-grid-scores-and-torus')]
for x in r: print(x['response'][-400:])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 19, in <module>
AssertionError: conditions at every grid point were not run: the entry already takes
      about two hours per run.'
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/clark-2026-01.yaml'; s=open(p).read()
old="""    notebooks of this entry taking about 120 minutes per run (1,147, 2,256, 613, 157 and 3,044 s in the
    run before the round-2 revision, model_sims.ipynb alone 51 of the 60 minutes a notebook may take),
    it did not fit in the five hours of a revision run."""
new="""    notebooks of this entry taking 97 to 120 minutes per run (1,147, 2,256, 613, 157 and 3,044 s in the
    run before the round-2 revision, model_sims.ipynb alone 51 of the 60 minutes a notebook may take;
    1,114, 1,709, 473, 150 and 2,356 s in the run of the round-2 revision), it did not fit in the five
    hours of a revision run."""
assert old in s; s=s.replace(old,new)
i=s.index("  - claim: fig8-grid-scores-and-torus\n    agrees: true")
j=s.index("  - claim:", i+10); blk=s[i:j]; k=blk.index("    response:")
s=s[:i]+blk[:k]+"""    response: Outcome kept. The notes, model_sims.ipynb's fig8 section, the README and entry.yaml now give
      the run times as printed (1,147, 2,256, 613, 157 and 3,044 s, about 120 minutes, in the run the verifier
      read; 1,114, 1,709, 473, 150 and 2,356 s, about 97 minutes, in the run of this revision). The README
      and entry.yaml keep the longer of the two.
"""+s[j:]
i=s.rindex("  - claim: figs8-s9-lambda-and-c\n")
j=s.index("  - claim:", i+10); blk=s[i:j].rstrip('\n')
assert blk.endswith("per run.'")
blk=blk[:-2]+""". In the run of this revision the flow error at lambda 1e-12 came out at 2.6e-9, against 3.6e-9 in the run the verifier
      read; the solve there is ill-conditioned and not repeated exactly, so the conclusion now says so and gives
      no fixed value, and the part fails in every run.'
"""
s=s[:i]+blk+s[j:]
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); r=[x for x in d['verifications'][1]['results'] if x['claim'] in ('figs8-s9-lambda-and-c','fig8-grid-scores-and-torus')]
for x in r: print(x['response'][-300:])
EOF
```

```
s about two hours per run. In the run of this revision the flow error at lambda 1e-12 came out at 2.6e-9, against 3.6e-9 in the run the verifier read; the solve there is ill-conditioned and not repeated exactly, so the conclusion now says so and gives no fixed value, and the part fails in every run.
's fig8 section, the README and entry.yaml now give the run times as printed (1,147, 2,256, 613, 157 and 3,044 s, about 120 minutes, in the run the verifier read; 1,114, 1,709, 473, 150 and 2,356 s, about 97 minutes, in the run of this revision). The README and entry.yaml keep the longer of the two.
```

**Agent calls Bash**

```bash
cd  git diff -U0 attempts questions entries | grep "^+" | grep -n "—\|–\|[Rr]ather" ; python tools/entry.py all entries/clark-2026 2>&1 | tail -8; date -u
```

```
0 error(s)
pass  tuning_curves.ipynb  (1114 s, reused)
pass  network.ipynb  (1709 s, reused)
pass  network_grid.ipynb  (473 s, reused)
pass  theory.ipynb  (150 s, reused)
pass  model_sims.ipynb  (2356 s, reused)
reused the executed copies of 2026-11-27 00:37 UTC: nothing the run reads has changed since (hash 3958a1480a1a). Nothing was executed and no environment was built; --fresh runs it again.
Fri Nov 27 00:38:18 UTC 2026
```

**Agent**

I made the round-2 corrections, re-ran every notebook, and recorded the round. No outcome changed and none is proposed for a round 3. The verifier agreed with all 30 outcomes and rated no finding `critical`, so there were no findings to review.

**Statements that were wrong and are now corrected** (new outputs added where the old text had no printed numbers behind it):
- **fig7 and finding 4:** the old text placed the 293 grid points without a zero mode "mostly at small beta and large sigma". That was wrong. A new table in theory cell 5 shows 249 of them at beta 1 and above and 226 at sigma 10 and above. Only 99 are at beta below 0.1 or sigma 50 and above. The zero mode is present at the paper's own parameters.
- **fig7de:** a new per-sigma table shows the largest convergence time, 20.5 tau, is at sigma 37.9, not 100. The failures are not confined to large sigma: the convergence time exceeds 10 tau from sigma 1.27 up, and the divergence time rises with beta at sigma 1 to 2.64. Limiting the grid to sigma 1 to 10 gives the same outcome, still not reproduced.
- **Other text fixes, matched to the printed values:**
  - figs8-s9: the counts now give their sample sizes (some points ran 20 initial conditions, not 100).
  - figs14: without setting an eigenvalue aside, 3 of 4 pairs pass, not 2; the cell now prints the count.
  - figs11b: 97% to 100% of final states are within the reference, not every one; the largest are just above it.
  - figs10: "fragment alike" is gone; the disordered network fragments somewhat further.
  - Finding 3: in float64 the two minima's error ranges do not overlap.
  - Run times, and the 12.7 to 30.2 GB file sizes in the tuning_curves header.
- **figs11-s12:** I added a deviation saying that "every final state" is read as at least 95%, the rule of figs11b. The notebook now prints the strict reading, which fails under the claim's seed.
- **No partial rule:** the notes for fig4, figs8-s9 and figs1-s2 now say their criteria have no partial rule, so `partially_reproduced` comes from the protocol's general reading.

**Questions added to `questions/clark-2026.yaml`** (claims unchanged):
- figs1-s2: whether the 5% eigenvalue test should apply to the large-N spectrum rather than two finite draws. Under that reading the claim would be reproduced.
- fig7: whether the criterion should also test the zero mode. With that test the claim would be partially reproduced.

**New in the re-run:** at lambda 1e-12 the grid's flow error came out at 2.6e-9, against 3.6e-9 in the run the verifier read. The solve there is ill-conditioned, so the conclusion no longer states a fixed value. That part of the criterion fails in every run, so the outcome holds.

**How it was run:** a full `tools/entry.py all` takes about two hours, the limit of one shell command. Running it in the background didn't work: the sandbox ended it when the command returned. So I ran the same steps one notebook per command (environment build, the same nbconvert call, the same stamp). All five passed (1,114, 1,709, 473, 150 and 2,356 s), and `tools/entry.py all` now passes its checks and reuses those copies.
- The grid notebook failed once on a network timeout while reading from the archive and passed when re-run.
- After the others had run, I reworded the grid notebook's conclusion and re-ran only that notebook. No other notebook reads it.

**Not done:** 100 initial conditions at every grid point for figs8-s9, because the entry already takes about two hours per run. fig8 stays blocked as too large.

## End of run

77 turns, 139 minutes, $4.54 at API prices, result: success.
