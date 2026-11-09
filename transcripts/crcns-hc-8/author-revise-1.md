# crcns-hc-8 · author-revise-1 · run 42621754996

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-hc-8/verifier-1-report.md; ls entries/crcns-hc-8-timme-2016 entries/crcns-hc-8-timme-2016/*
```

```
Mon Nov  9 13:07:10 UTC 2026
**Verifier report, round 1: Timme et al. (2016), CRCNS hc-8**

The claims file has 28 claims. The notebooks test 22, mark 5 as blocked (fig7ab, fig7a, figs2, fig7d, fig8-exponents-match-literature), and on review I judge one of those blocked claims, fig7ab, to be testable.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| fig3-chain-model-complexity | reproduced | Complexity is 0 at c = 0 and c = 1 and 0.431 bits at c = 0.8. Integration is 0, 5.84 and 11 bits for c = 0, 0.8, 1 (models.ipynb cell 4). |
| fig5d-bethe-small-avalanches | reproduced (fragile) | The size fit is accepted (p 0.338), but only over sizes 4 to 12. Corrected complexity is 0.00637 > 0. The same network states gave 0.00001 in cell 10, so "above zero" is within the estimator's noise (B1). |
| fig5e-shuffle-removes-complexity | reproduced (unreliable) | Size distribution identical; shuffled/original complexity ratio is 0.003 (cell 8). The original value is itself at noise level (B1). With the no-cut variant the complexity is also removed (−0.050 vs 0.271). |
| fig5f-network-state-poisson-keeps-complexity | not_reproduced (unreliable) | Relative change in complexity is 0.998 against a criterion of < 0.05; the size distribution did change (cell 10). The network states are the same before and after, so the miss comes from the estimator's noise (B1). The no-cut (0.049) and raw (0.020) variants pass. |
| fig6-cb-distribution-curvature | partially_reproduced | Durations pass all three parts (−1.23 at 0.2, +1.39 at 0.3, smallest at 0.25). Sizes fail: +0.087 ± 0.51 at 0.2, and the smallest magnitude is at 0.2/0.21 (cell 12). |
| fig7ab-cb-complexity-susceptibility-peak | not_reproduced (notebook: blocked, too_large) | The susceptibility half was computed by the criterion's method. It rises monotonically to the edge of the range (0.3) under both readings and has no interior peak (cell 16), so the claim fails whatever the complexity shows. The complexity half is u
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i -E "^[0-9]+:[0-9]+:#|step 6|Hand over|verifications|proposed" | head -60
```

```
176:176:not say what the paper says (author, step 1.6, and "Hand over for
191:191:(step 6).
278:278:     (step 6; see also chance levels, under "Record the attempt").
325:325:     claims file (reader, step 6), and a later run, `author-answers`,
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
625 docs/protocol.md
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
56:### 2. Read the paper's code
66:### 3. Write the claims file
151:### 4. Data from outside the paper's own recordings
159:### 5. Check
172:### 6. Answer questions
185:## Author
201:### 1. Establish what can be tested
328:### 2. Check the data against its description
343:### 3. Write the entry
411:### 4. Lock, check and run
422:### 5. Record the attempt
473:### 6. Hand over for verification
511:## Repeat attempts
553:## Local and remote datasets
576:## Verifier
580:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 185,200p docs/protocol.md; sed -n 343,625p docs/protocol.md
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

### 3. Write the entry

An entry is a directory `entries/<folder>-<first author>-<year>/` holding
`entry.yaml`, `requirements.in`, one or more notebooks, and usually a helper
[... 279 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep hc-8; cat attempts/crcns-hc-8-timme-2016-01.yaml | head -150; wc -l attempts/crcns-hc-8-timme-2016-01.yaml; cat entries/crcns-hc-8-timme-2016/entry.yaml; git status --short; git diff --stat
```

```
crcns-hc-8-timme-2016-01.yaml
schema_version: 2
id: crcns-hc-8-timme-2016-01
dataset:
  archive: crcns
  id: hc-8
  version: unversioned
  doi: 10.6080/K0PC308P
paper: doi:10.3389/fphys.2016.00425
date: 2026-11-09
entry: crcns-hc-8-timme-2016
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,340p attempts/crcns-hc-8-timme-2016-01.yaml
```

```
the duration range from 0.663 to 0.211 (corrected p about 4e-141). 10-bin jitter lengthens them
    to 0.740 and 0.732 (corrected p 0.000135 and 5e-06, significant). 100-bin jitter and wrap
    shorten both significantly, and 1-bin jitter changes neither (corrected p 0.455 and 0.398), so
    the legend's wider statement holds for three of the four other randomizations.
- claim: fig11bd-exponents-randomization
  outcome: partially_reproduced
  notebook: culture_criticality.ipynb
  output: claim:fig11bd-exponents-randomization
  notes: Tau rises significantly under 10-bin jitter, 100-bin jitter, wrap and Poisson (median 2.50
    to 4.53 under Poisson) and falls under 1-bin jitter (2.39, corrected p 0.0108). Alpha rises
    significantly under 100-bin jitter, wrap and Poisson; 1-bin and 10-bin jitter do not change it
    significantly (corrected p 0.107 and 0.401). Under Poisson the median largest fitted size falls
    from 44 to 21, consistent with the paper's explanation.
- claim: fig10a-complexity-randomization
  outcome: partially_reproduced
  notebook: complexity_culture.ipynb
  output: claim:fig10a-complexity-randomization
  notes: Over 180 recordings, the toolbox's complexity (correction and cut) has median 0.00192
    bits/neuron in the real data; 1-bin, 10-bin and 100-bin jitter, wrap and Poisson lower it to
    medians of 0.00022 to 0.00131 with corrected p from 0.00925 to 5e-31, and Poisson is among the
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; wc -l hc8.py models.py; grep -n "^def \|N_SUBSETS\|n_subsets" hc8.py models.py
```

```
875 hc8.py
  213 models.py
 1088 total
hc8.py:73:def _zip():
hc8.py:78:def recording_names() -> list[str]:
hc8.py:84:def culture_div(name: str) -> tuple[int, int]:
hc8.py:89:def load(name: str, zf: zipfile.ZipFile | None = None) -> dict:
hc8.py:101:def open_zip() -> zipfile.ZipFile:
hc8.py:109:def first_window(spikes: list[np.ndarray], nbins: int = ANALYSIS_BINS) -> list[np.ndarray]:
hc8.py:114:def network_isi_bins(spikes: list[np.ndarray]) -> float:
hc8.py:122:def rebin(spikes: list[np.ndarray], factor: int, nbins: int = ANALYSIS_BINS):
hc8.py:128:def activity(raster: list[np.ndarray], nbins: int) -> np.ndarray:
hc8.py:136:def avalanches(act: np.ndarray):
hc8.py:153:def apply_cuts(x: np.ndarray) -> np.ndarray:
hc8.py:229:def pvcalc(pl: _PLData, xmin: int, xmax: int, tau: float, rng: np.random.Generator,
hc8.py:242:def support_order(x: np.ndarray) -> np.ndarray:
hc8.py:254:def plparams(x: np.ndarray, rng: np.random.Generator, screen: float = 1.2, chunk: int = 2000):
hc8.py:289:def plmle_full(x: np.ndarray) -> float:
hc8.py:298:def sizegivdur(size: np.ndarray, dur: np.ndarray, durmin, durmax) -> float:
hc8.py:318:def mean_profiles(act: np.ndarray, size, dur, starts, min_dur: int = 4, min_count: int = 20):
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; sed -n 1,72p hc8.py; sed -n 355,470p hc8.py; sed -n 830,875p hc8.py
```

```
"""Loading and measures for CRCNS hc-8, the culture recordings of Timme et al. (2016).

Timme, Marshall, Bennett, Ripp, Lautzenhiser & Beggs (2016), "Criticality Maximizes Complexity in
Neural Tissue", Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425. Data set doi:10.6080/K0PC308P.

The data set is one zip, hc-8/live/Data.zip, of 435 MATLAB files CultureXDIVY.mat, each with a
struct `data` whose `spikes` is a cell array of spike times per neuron in 0.05 ms bins. The zip is
read in place from the public S3 bucket over range requests; nothing is written to disk.

The measures port the NCC MATLAB toolbox that the paper cites (Marshall et al., 2016; "NCC Toolbox
Version 1", June 14th, 2016, from the Software page of nicholastimme.com, zip sha256
b7c912f8154f70fc82b13ab1725ed191935ed2877256cadd7e39f66737be294b, the version the claims file
read). Each function names the toolbox function it ports. Where the parameters come from:

- First 59 min of each recording, rebinning to the mean network-wide ISI, avalanches as runs of
  active bins: Methods 2.2 and 2.3 (claims file, common method). The ISI is rounded to a whole
  number of 0.05 ms bins, as `rebin.m` requires (claims file, common detail 1, a standard choice).
- Cuts before power-law fits (values >= 4 seen at least 20 times), MLE on tau in [1, 5] to 0.001,
  500 surrogates and p >= 0.2, the support search largest range first: Methods 2.7, `plparams.m`,
  `plmle.m`, `pvcalc.m`.
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p entries/crcns-hc-8-timme-2016/requirements.in; ls executed/ 2>/dev/null | head; ls executed/crcns-hc-8-timme-2016 2>/dev/null; which python; python -c "import numpy, scipy, pandas, fsspec; print('ok')"; nproc; free -g
```

```
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scipy
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, pandas, fsspec; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|def cmd_\|executed" tools/entry.py | head -40; ls ~/.cache 2>/dev/null; ls -d .venv* 2>/dev/null
```

```
Exit code 2
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
27:directory. The executed copies
28:go to --output-dir (default: executed/<name>/, which git ignores). A notebook
32:(docs/protocol.md): the executed notebooks with the conclusions removed (every
35:executed/<name>/handover/. Run the entry first.
345:    venv = (output_dir / ".venv").resolve()
346:    python = venv / "bin" / "python"
350:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
353:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
367:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
405:        executed = output_dir / notebook["path"]
406:        if not executed.is_file():
407:            print(f"error: no executed copy of {notebook['path']} in {output_dir}; run the entry first",
410:        nb = strip_conclusions(nbformat.read(executed, as_version=4))
431:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
456:    output_dir = args.output_dir or ROOT / "executed" / entry_dir.name
```

**Agent calls Bash**

```bash
cd  sed -n 335,375p tools/entry.py; uv venv --quiet --python 3.12 $TMPDIR/dev 2>&1 | tail -2; uv pip install --quiet --python $TMPDIR/dev/bin/python -r entries/crcns-hc-8-timme-2016/requirements.lock.txt nbconvert ipykernel 2>&1 | tail -3; $TMPDIR/dev/bin/python -c "import numpy; print(numpy.__version__)"
```

```
r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        print(f"wrote {(entry_dir / 'requirements.lock.txt').relative_to(ROOT)}")
    return r.returncode


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
[... 22 more lines not kept]
```

**Agent**

The dev environment is ready. Next I profile the complexity estimator on one recording to see what 100 subsets per size would cost.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json
for nb in ["complexity_culture.ipynb","models.ipynb"]:
    d=json.load(open(nb))
    print("=====",nb, len(d["cells"]))
    for i,c in enumerate(d["cells"]):
        print(f"--- cell {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')}")
        print("".join(c["source"])[:2500])
EOF
```

```
===== complexity_culture.ipynb 19
--- cell 0 [markdown] tags=None
# Timme et al. (2016) on CRCNS hc-8: complexity of the culture recordings

Paper: Timme et al. (2016), Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425; claims file
`claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` (version of record, PMC5037237, with the
supplement). Dataset: CRCNS hc-8, doi:10.6080/K0PC308P, `hc-8/live/Data.zip` (MD5
`bd4e2a8685df3e55e1a3c04fbe09d9ce` in the data set's `checksums.md5`), version `unversioned`: CRCNS
data sets carry no versions and this is the only published copy (see `culture_criticality.ipynb`).

Complexity (Methods 2.9, `complexity.m` of the NCC toolbox): on the avalanche bins of the rebinned
first 59 min, with the sub-sampling correction (the integration curve of data whose neurons are
each permuted in time is subtracted, and the curve is cut at the first peak of I(k)/(k-1)). The
paper uses up to 100 random subsets per subset size; this notebook uses 10, to fit the time limit
of 8 conditions), and runs on 180 of the 435 recordings drawn with a fixed seed. Two variants are shown: the corrected curve without the cut, and
no correction. The randomized data are the same as in `culture_criticality.ipynb` (same
generators).

| claim | here |
|---|---|
[... 396 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; cat > $TMPDIR/prof.py <<'EOF'
import time, numpy as np, hc8
names = hc8.recording_names()
t=time.time(); d = hc8.load(names[5]); p = hc8.prepare(d); print("load", time.time()-t)
act=p["act"]; bins=np.flatnonzero(act)+1
X=hc8.raster_matrix(p["raster"], bins)
X=X[:, np.asarray(X.sum(0)).ravel()>0]
U,cnt=hc8._unique_rows(X, np.random.default_rng(0))
print("N",X.shape, "unique", U.shape)
import pickle; pickle.dump((X,), open(__import__('os').environ['TMPDIR']+"/X.pkl","wb"))
for ns in (10,):
    t=time.time(); c=hc8._integration_curve(U,cnt,X.shape[0],ns,np.random.default_rng(1)); print(ns, time.time()-t)
EOF
$TMPDIR/dev/bin/python $TMPDIR/prof.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/prof.py", line 1, in <module>
    import time, numpy as np, hc8
ModuleNotFoundError: No module named 'hc8'
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/prof.py
```

```
load 0.7226243019104004
N (304194, 90) unique (32189, 90)
10 0.5383524894714355
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; cat > $TMPDIR/prof2.py <<'EOF'
import time, os, pickle, numpy as np, hc8, cProfile, pstats
(X,)=pickle.load(open(os.environ['TMPDIR']+"/X.pkl","rb"))
t=time.time()
cProfile.run("hc8.complexity(X, 10, np.random.default_rng(1), return_variants=True)", os.environ['TMPDIR']+"/p.out")
print(time.time()-t)
pstats.Stats(os.environ['TMPDIR']+"/p.out").sort_stats("tottime").print_stats(12)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/prof2.py 2>&1 | head -45
```

```
1.7562406063079834
Mon Nov  9 13:08:22 2026    /tmp/claude-1001/p.out

         215044 function calls (214882 primitive calls) in 1.755 seconds

   Ordered by: internal time
   List reduced from 224 to 12 due to restriction <12>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1762    0.670    0.000    0.712    0.000 /tmp/claude-1001/dev/lib/python3.12/site-packages/pandas/core/algorithms.py:727(factorize_array)
        1    0.337    0.337    1.754    1.754 entries/crcns-hc-8-timme-2016/hc8.py:420(complexity)
     1762    0.287    0.000    0.287    0.000 {built-in method scipy.sparse._sparsetools.csc_matvec}
        2    0.271    0.136    1.344    0.672 entries/crcns-hc-8-timme-2016/hc8.py:390(_integration_curve)
        3    0.038    0.013    0.038    0.013 {method 'argsort' of 'numpy.ndarray' objects}
     3534    0.012    0.000    0.012    0.000 {built-in method numpy.zeros}
     3738    0.010    0.000    0.010    0.000 {method 'reduce' of 'numpy.ufunc' objects}
    35587    0.010    0.000    0.021    0.000 {built-in method builtins.isinstance}
        2    0.006    0.003    0.006    0.003 {built-in method scipy.sparse._sparsetools.csr_matvec}
        1    0.006    0.006    0.006    0.006 {built-in method scipy.sparse._sparsetools.coo_tocsr}
     1764    0.005    0.000    0.314    0.000 /tmp/claude-1001/dev/lib/python3.12/site-packages/scipy/sparse/_compressed.py:387(_matmul_vector)
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -il "permutations" paper/* | head; grep -o -i ".\{600\}100 randomly chosen.\{600\}" paper/*.md paper/*.txt 2>/dev/null | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "permutation" paper/10.3389-fphys.2016.00425.txt | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-hc-8-timme-2016/hc8.py",
 "old_string": "    curve = np.zeros(N)\n    w_all = rng.integers(1, 2**62, size=N, dtype=np.int64)\n    Ud = U.tocsc()\n    from math import comb\n    for k in range(2, N + 1):\n        if comb(N, k) <= n_subsets:\n            from itertools import combinations\n            subsets = [np.array(c) for c in combinations(range(N), k)]\n        else:\n            subsets = [rng.permutation(N)[:k] for _ in range(n_subsets)]\n        vals = np.empty(len(subsets))\n        for i, sub in enumerate(subsets):\n            w = np.zeros(N, dtype=np.int64)\n            w[sub] = w_all[sub]\n            inv, _ = pd.factorize(Ud @ w)\n            p = np.bincount(inv, weights=cnt) / nT\n            vals[i] = ent[sub].sum() + np.sum(p * np.log2(p))\n        curve[k - 1] = vals.mean()\n    return curve",
 "new_string": "    curve = np.zeros(N)\n    w_all = rng.integers(1, 2**62, size=N, dtype=np.int64)\n    Ur = U.tocsr()\n    from math import comb\n    for k in range(2, N + 1):\n        if comb(N, k) <= n_subsets:\n            from itertools import combinations\n            subsets = [np.array(c) for c in combinations(range(N), k)]\n        else:\n            subsets = [rng.permutation(N)[:k] for _ in range(n_subsets)]\n        W = np.zeros((N, len(subsets)), dtype=np.int64)\n        for i, sub in enumerate(subsets):\n            W[sub, i] = w_all[sub]\n        H = Ur @ W                      # hash of each unique state restricted to each subset\n        vals = np.empty(len(subsets))\n        for i, sub in enumerate(subsets):\n            # states silent on the subset form one group (hash 0); only the others are factorized\n            h = H[:, i]\n            nz = h != 0\n            inv, _ = pd.factorize(h[nz])\n            p = np.bincount(inv, weights=cnt[nz]) / nT\n            p0 = (nT - cnt[nz].sum()) / nT\n            vals[i] = ent[sub].sum() + np.sum(p * np.log2(p)) + (p0 * np.log2(p0) if p0 > 0 else 0.0)\n        curve[k - 1] = vals.mean()\n    return curve"
}
```

```
The file entries/crcns-hc-8-timme-2016/hc8.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; git stash -q -- hc8.py 2>/dev/null; cp hc8.py $TMPDIR/hc8_old.py; git stash pop -q; cat > $TMPDIR/prof3.py <<'EOF'
import time, os, pickle, sys, numpy as np, importlib.util
sys.path.insert(0, os.environ['TMPDIR']); import hc8_old
import hc8
(X,)=pickle.load(open(os.environ['TMPDIR']+"/X.pkl","rb"))
for mod in (hc8_old, hc8):
    t=time.time(); r=mod.complexity(X, 10, np.random.default_rng(1), return_variants=True); print(mod.__name__, round(time.time()-t,2), r)
t=time.time(); r=hc8.complexity(X, 100, np.random.default_rng(1), return_variants=True); print("100:", round(time.time()-t,2), r)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/prof3.py
```

```
hc8_old 1.69 {'cut': 0.0007048529509128792, 'uncut': 0.09620270155294376, 'raw': 0.24964441891930583, 'k_kept': 10, 'N': 90}
hc8 2.04 {'cut': 0.0007048529509128757, 'uncut': 0.0962027015529441, 'raw': 0.24964441891930586, 'k_kept': 10, 'N': 90}
100: 16.9 {'cut': 0.0005516041029213777, 'uncut': 0.09353170690490463, 'raw': 0.2472150470110065, 'k_kept': 12, 'N': 90}
```

**Agent**

Values match the old code exactly. A first finding: on this recording, 100 subsets still keep only 12 of 90 sizes after the cut, so more subsets may not move the cut much. Now I'll profile the speed.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; cat > $TMPDIR/prof4.py <<'EOF'
import time, os, pickle, numpy as np, hc8, cProfile, pstats
(X,)=pickle.load(open(os.environ['TMPDIR']+"/X.pkl","rb"))
cProfile.run("hc8.complexity(X, 30, np.random.default_rng(1), return_variants=True)", os.environ['TMPDIR']+"/p.out")
pstats.Stats(os.environ['TMPDIR']+"/p.out").sort_stats("tottime").print_stats(10)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/prof4.py 2>&1 | grep -A14 ncalls
```

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    2.432    1.216    5.056    2.528 entries/crcns-hc-8-timme-2016/hc8.py:390(_integration_curve)
     5282    1.813    0.000    1.938    0.000 /tmp/claude-1001/dev/lib/python3.12/site-packages/pandas/core/algorithms.py:727(factorize_array)
      176    0.478    0.003    0.478    0.003 {built-in method scipy.sparse._sparsetools.csr_matvecs}
        1    0.330    0.330    5.455    5.455 entries/crcns-hc-8-timme-2016/hc8.py:426(complexity)
      366    0.058    0.000    0.058    0.000 {built-in method numpy.zeros}
    16060    0.054    0.000    0.054    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        3    0.037    0.012    0.037    0.012 {method 'argsort' of 'numpy.ndarray' objects}
    90663    0.025    0.000    0.056    0.000 {built-in method builtins.isinstance}
     5282    0.014    0.000    1.990    0.000 /tmp/claude-1001/dev/lib/python3.12/site-packages/pandas/core/algorithms.py:837(factorize)
    47538    0.013    0.000    0.031    0.000 /tmp/claude-1001/dev/lib/python3.12/site-packages/pandas/core/dtypes/generic.py:45(_instancecheck)
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; python3 - <<'EOF'
s=open("hc8.py").read()
s=s.replace("""        H = Ur @ W                      # hash of each unique state restricted to each subset
        vals = np.empty(len(subsets))
        for i, sub in enumerate(subsets):
            # states silent on the subset form one group (hash 0); only the others are factorized
            h = H[:, i]
""","""        H = np.ascontiguousarray((Ur @ W).T)   # hash of each unique state restricted to each subset
        vals = np.empty(len(subsets))
        for i, sub in enumerate(subsets):
            # states silent on the subset form one group (hash 0); only the others are factorized
            h = H[i]
""")
open("hc8.py","w").write(s)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/prof4.py 2>&1 | grep -A6 ncalls
```

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    2.064    1.032    4.952    2.476 entries/crcns-hc-8-timme-2016/hc8.py:390(_integration_curve)
     5282    1.829    0.000    1.951    0.000 /tmp/claude-1001/dev/lib/python3.12/site-packages/pandas/core/algorithms.py:727(factorize_array)
      176    0.427    0.002    0.427    0.002 {built-in method scipy.sparse._sparsetools.csr_matvecs}
        1    0.332    0.332    5.354    5.354 entries/crcns-hc-8-timme-2016/hc8.py:426(complexity)
      178    0.309    0.002    0.309    0.002 {built-in method numpy.ascontiguousarray}
    16060    0.053    0.000    0.053    0.000 {method 'reduce' of 'numpy.ufunc' objects}
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; python3 - <<'EOF'
s=open("hc8.py").read()
old=s[s.index("        H = np.ascontiguousarray"):s.index("        curve[k - 1] = vals.mean()")]
new='''        H = np.ascontiguousarray((Ur @ W).T)   # hash of each unique state restricted to each subset
        vals = np.empty(len(subsets))
        for i, sub in enumerate(subsets):
            inv, _ = pd.factorize(H[i])
            p = np.bincount(inv, weights=cnt) / nT
            vals[i] = ent[sub].sum() + np.sum(p * np.log2(p))
'''
s=s.replace(old,new); open("hc8.py","w").write(s)
EOF
sed -n 388,420p hc8.py; cat > $TMPDIR/prof5.py <<'EOF'
import time, sys, resource, numpy as np, hc8
names=hc8.recording_names()
for i in (int(sys.argv[1]),):
    t=time.time(); r=hc8.complexity_record((i, names[i], 20161, 100)); 
    print(i, r["n_neurons"], round(time.time()-t,1), {k: (round(r[f"C_{k}"],5), r[f"kkept_{k}"], round(r[f"Cuncut_{k}"],4)) for k in ["real"]+hc8.RANDOMIZATIONS}, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
time PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/prof5.py 5
```

```
def _integration_curve(U: sparse.csr_matrix, cnt: np.ndarray, nT: int, n_subsets: int,
                       rng: np.random.Generator) -> np.ndarray:
    """Mean integration of random k-subsets for k = 1..N (k = 1 is 0), as complexity.m."""
    N = U.shape[1]
    nsp = np.asarray(U.multiply(cnt[:, None]).sum(axis=0)).ravel().astype(float)
    p1 = nsp / nT
    with np.errstate(divide="ignore", invalid="ignore"):
        ent = -(p1 * np.log2(p1)) - ((1 - p1) * np.log2(1 - p1))
    ent = np.nan_to_num(ent)
    curve = np.zeros(N)
    w_all = rng.integers(1, 2**62, size=N, dtype=np.int64)
    Ur = U.tocsr()
    from math import comb
    for k in range(2, N + 1):
        if comb(N, k) <= n_subsets:
            from itertools import combinations
            subsets = [np.array(c) for c in combinations(range(N), k)]
        else:
            subsets = [rng.permutation(N)[:k] for _ in range(n_subsets)]
        W = np.zeros((N, len(subsets)), dtype=np.int64)
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; cat > $TMPDIR/bethe.py <<'EOF'
import time, numpy as np, hc8, models
SEED=20162
rng5 = np.random.default_rng([SEED, 5])
fs_full, fd_full, fprof = models.bethe_full_sizes(10**4, rng5)
fit_full = hc8.plparams(hc8.apply_cuts(fs_full), rng5)
raster5, nb5, sizes5 = models.bethe_small_raster(10**4, rng5)
act5 = hc8.activity(raster5, nb5)
bins5 = np.flatnonzero(act5) + 1
X5 = hc8.raster_matrix(raster5, bins5)
keep5 = np.asarray(X5.sum(axis=0)).ravel() > 0
print(X5.shape, keep5.sum())
for ns in (10, 100):
  for s in (51, 1, 2):
    t=time.time(); cx5 = hc8.complexity(X5[:, keep5], ns, np.random.default_rng([SEED, s]), return_variants=True); print(ns, s, round(time.time()-t,1), cx5)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/bethe.py
```

```
(20035, 255) 245
10 51 0.4 {'cut': 0.006371779768596379, 'uncut': 0.2710356067799899, 'raw': 0.373981984991991, 'k_kept': 20, 'N': 245}
10 1 0.4 {'cut': 0.013662649187279859, 'uncut': 0.2707904718581722, 'raw': 0.37537485520169733, 'k_kept': 30, 'N': 245}
10 2 0.4 {'cut': 0.014350438345305588, 'uncut': 0.27348975050732593, 'raw': 0.37755902779234934, 'k_kept': 24, 'N': 245}
100 51 3.2 {'cut': 0.002998192595699139, 'uncut': 0.26451192765728737, 'raw': 0.37415983170050027, 'k_kept': 24, 'N': 245}
100 1 3.0 {'cut': 0.0021873524707698073, 'uncut': 0.26509328041226926, 'raw': 0.3717838528094878, 'k_kept': 21, 'N': 245}
100 2 3.0 {'cut': 0.0016467523399054768, 'uncut': 0.26872254334487966, 'raw': 0.37417739940819555, 'k_kept': 14, 'N': 245}
```

**Agent**

The Bethe raster is cheap: 3 s per call at 100 subsets. Across seeds the cut complexity is 0.0016 to 0.0030 and keeps 14 to 24 of 245 sizes. Next I read the claims for the affected items.

**Agent calls Bash**

```bash
cd  ls claims/crcns-hc-8/ questions/ | grep -i hc-8; python3 - <<'EOF'
import yaml
d=yaml.safe_load(open("claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml"))
print(d.keys())
for c in d["claims"]:
    if c["id"] in ("fig5d-bethe-small-avalanches","fig5e-shuffle-removes-complexity","fig5f-network-state-poisson-keeps-complexity","fig7ab-cb-complexity-susceptibility-peak","fig7d-cb-branching-ratio-near-1","figs2-recording-length","fig7a-complexity-boundary-rise","fig2e-avalanche-count"):
        print(yaml.safe_dump(c, width=120))
EOF
```

```
claims/crcns-hc-8/:
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
criterion: A simulation, not a test on recorded data. Bethe lattice of Methods 2.4 (two outgoing connections per neuron, p_trans
  = 0.5, activity stopped at layer 10^4, one neuron active in the first layer per run), as in the toolbox's bethelattice.m.
  The number of runs is not stated; a standard choice of 10^4 runs is used and cannot change the direction of the result.
  Small avalanches are those that stop on or before layer 8; each run is one time series of network states over the neurons
  of layers 1 to 8. Reproduced when the size distribution of the small avalanches is accepted as a truncated power law by
  plparams (p at least 0.2) and their complexity (toolbox complexity, sub-sampling correction on) is above zero.
id: fig5d-bethe-small-avalanches
quote: In the original small avalanches, the sizes of the avalanches were power-law distributed and a non-zero complexity
  was observed
source: Results 3.1, paragraph 1; Figure 5B to 5D
statement: In the critical Bethe lattice model (p_trans = 0.5), avalanche sizes are power-law distributed and show shape collapse,
  and the small avalanches (stopped by the 8th layer) are power-law distributed in size and have non-zero complexity.

criterion: A simulation, not a test on recorded data. Neuron shuffling as in Methods 2.5 (at each time bin the active count
  kept and the identities drawn uniformly over all neurons). Reproduced when the shuffled size distribution equals the original
  and the complexity falls to below 10% of the original value ("removed" read as near zero; 10% is a choice the paper does
  not make).
depends_on:
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; sed -n 120,213p models.py; sed -n 572,612p hc8.py
```

```
# ----------------------------------------------------------------------------------------------
# Cortical branching model

def cb_simulate(p_trans: float, n_models: int, rng, t_steps: int = 3 * 10 ** 5,
                side: int = 10, p_spont: float = 1e-4):
    """n_models independent cortical branching models run together; returns packed states
    (t_steps x n_models x ceil(side^2 / 8) uint8). The first step is silent, as cbmodel.m."""
    n = side * side
    probconv = np.zeros(5)
    probconv[0] = p_spont
    for j in range(4):
        probconv[j + 1] = probconv[j] + p_trans - probconv[j] * p_trans
    packed = np.zeros((t_steps, n_models, (n + 7) // 8), dtype=np.uint8)
    state = np.zeros((n_models, side, side), dtype=bool)
    for it in range(1, t_steps):
        s = state.view(np.int8)
        cnt = (np.roll(s, 1, 1) + np.roll(s, -1, 1) + np.roll(s, 1, 2) + np.roll(s, -1, 2))
        state = rng.random((n_models, side, side)) < probconv[cnt]
        packed[it] = np.packbits(state.reshape(n_models, n), axis=1)
    return packed
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "refractor" paper/10.3389-fphys.2016.00425.txt | head -5; cd entries/crcns-hc-8-timme-2016; cat > $TMPDIR/cbt.py <<'EOF'
import time, numpy as np, hc8, models
from scipy import sparse
for p in (0.25, 0.3):
    pk = models.cb_simulate(p, 1, np.random.default_rng(1))
    R = models.cb_raster(pk, 0)
    X = sparse.csr_matrix(R.astype(np.int64))
    X = X[:, np.asarray(X.sum(0)).ravel() > 0]
    t=time.time(); r = hc8.complexity(X, 100, np.random.default_rng(2), return_variants=True); print(p, X.shape, round(time.time()-t,1), r)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/cbt.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; date -u; sed -i 's/(i, names\[i\], 20161, 100)/(i, names[i], 20161, int(sys.argv[2]))/' $TMPDIR/prof5.py; PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/prof5.py 5 10; PYTHONPATH=. $TMPDIR/dev/bin/python -c "
import hc8,numpy as np
names=hc8.recording_names(); idx=sorted(np.random.default_rng([20161,0]).choice(len(names),size=180,replace=False).tolist()); print(idx[:12])"
```

```
Mon Nov  9 13:15:59 UTC 2026
5 90 16.3 {'real': (8e-05, 5, 0.0907), 'jitter1': (0.00026, 6, 0.0865), 'jitter10': (0.00022, 6, 0.0843), 'jitter100': (0.00039, 8, 0.0704), 'wrap': (5e-05, 3, 0.0645), 'poisson': (0.00044, 11, 0.0652), 'swap': (0.0, 3, 0.0843), 'shuffle': (0.00248, 33, 0.0433)} 0.323868
[1, 3, 4, 9, 10, 16, 25, 30, 33, 34, 35, 36]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; cat > $TMPDIR/cal.py <<'EOF'
import time, multiprocessing as mp, numpy as np, hc8
if __name__ == "__main__":
    names=hc8.recording_names(); idx=sorted(np.random.default_rng([20161,0]).choice(len(names),size=40,replace=False).tolist())
    print(idx)
    t=time.time()
    with mp.get_context("spawn").Pool(4) as pool:
        recs=list(pool.imap(hc8.complexity_record,[(i,names[i],20161,100) for i in idx[:4]]))
    print("wall", time.time()-t)
    for r in recs: print(r["n_neurons"], r["nbins_real"], {k:(round(r[f"C_{k}"],5), r[f"kkept_{k}"]) for k in ["real","swap","shuffle","poisson"]})
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/cal.py
```

```
[2, 50, 53, 54, 59, 67, 73, 89, 99, 102, 107, 122, 142, 159, 163, 173, 180, 190, 196, 219, 220, 222, 254, 267, 269, 270, 282, 288, 295, 297, 308, 319, 330, 332, 344, 373, 374, 381, 392, 402]
wall 201.72725677490234
87 416416 {'real': (0.00085, 10), 'swap': (0.0031, 21), 'shuffle': (0.16893, 87), 'poisson': (0.00051, 12)}
66 93104 {'real': (0.04178, 16), 'swap': (0.0223, 12), 'shuffle': (0.23181, 48), 'poisson': (0.0006, 10)}
66 241770 {'real': (0.00115, 5), 'swap': (0.00142, 8), 'shuffle': (0.23897, 66), 'poisson': (0.00419, 25)}
65 170744 {'real': (0.00034, 5), 'swap': (0.02311, 29), 'shuffle': (0.17269, 65), 'poisson': (0.00187, 16)}
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-hc-8-timme-2016/hc8.py",
 "old_string": "        out[f\"nbins_{kind}\"] = int(bins.size)\n    return out",
 "new_string": "        out[f\"nbins_{kind}\"] = int(bins.size)\n    return out\n\n\ndef complexity_seeds(args) -> list[dict]:\n    \"\"\"Notebook 2, one recording: the complexity of the real data repeated with several generators\n    for the random subsets and the time permutation of the correction, at each number of subsets\n    per size, to show the estimator's spread. args = (index, name, seed, n_subsets_list, n_seeds).\"\"\"\n    i, name, seed, n_subsets_list, n_seeds = args\n    p = prepare(load(name, _worker_zip()))\n    X = raster_matrix(p[\"raster\"], np.flatnonzero(p[\"act\"]) + 1)\n    out = []\n    for ns in n_subsets_list:\n        for s in range(n_seeds):\n            cv = complexity(X, ns, np.random.default_rng([seed, i, 500, ns, s]), return_variants=True)\n            out.append(dict(name=name, n_subsets=ns, rep=s, C=cv[\"cut\"], Cuncut=cv[\"uncut\"],\n                            Craw=cv[\"raw\"], k_kept=cv[\"k_kept\"], N=cv[\"N\"]))\n    return out"
}
```

```
The file entries/crcns-hc-8-timme-2016/hc8.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json
d=json.load(open("culture_criticality.ipynb"))
print(len(d["cells"]))
for i,c in enumerate(d["cells"]):
    src="".join(c["source"])
    if i in (0,1,4,9,10,11) or c["cell_type"]=="markdown" and src.startswith("## Summary"):
        print(f"--- cell {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')}"); print(src[:3000])
EOF
```

```
49
--- cell 0 [markdown] tags=None
# Timme et al. (2016) on CRCNS hc-8: avalanches, exponents, branching ratio and randomizations

Paper: Timme, Marshall, Bennett, Ripp, Lautzenhiser & Beggs (2016), "Criticality Maximizes
Complexity in Neural Tissue", Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425. The claims file
`claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` was written from the version of record
(PMC5037237) with its supplement, and checked by a second reader.

Dataset: CRCNS hc-8, doi:10.6080/K0PC308P, read from the public bucket
`crcnsarchive/hc-8/live/Data.zip` (435 files `Data/CultureXDIVY.mat`). Version: CRCNS data sets
are not versioned, so the version is `unversioned` (docs/archives.md). The zip read is the one
whose MD5 the data set's `checksums.md5` gives as `bd4e2a8685df3e55e1a3c04fbe09d9ce`; the data
description is version 0.9 (Sept. 28, 2016). This is the only published copy (the bucket's
`hc-8/orig/` holds a draft description, no data), and the paper names no version, so it is the
one pinned.

This notebook covers the culture claims that do not need the complexity. The complexity claims are
in `complexity_culture.ipynb` and the model claims in `models.ipynb`. The measures port the NCC
MATLAB toolbox the paper cites (see `hc8.py`).
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json
d=json.load(open("culture_criticality.ipynb"))
for i in (12,13,14):
    c=d["cells"][i]; print(f"--- cell {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')}"); print("".join(c["source"]))
EOF
```

```
--- cell 12 [code] tags=['claim:fig2e-avalanche-count']
nav = meas["real"].n_av.values
mode_nav, k_nav = hc8.terrell_scott_mode(nav)
print(f"avalanches per recording (first 59 min, rebinned to the network ISI): (a) median {np.median(nav):.0f}; "
      f"(b) Terrell-Scott mode {mode_nav:.0f} ({k_nav} bins); expected 10000 +/- 1000")
print(f"range {nav.min()} to {nav.max()}; 5th to 95th percentile {np.percentile(nav, 5):.0f} to {np.percentile(nav, 95):.0f}")
print("recordings with 9000 to 11000 avalanches:", int(np.sum((nav >= 9000) & (nav <= 11000))))
print("by culture (median):", meas["real"].groupby(base.culture).n_av.median().astype(int).to_dict())
plt.figure(figsize=(4, 3)); plt.hist(nav, bins=k_nav); plt.xlabel("avalanches per recording"); plt.show()
--- cell 13 [markdown] tags=None
**Result: not reproduced.** After rebinning the first 59 min to the network ISI, the median number of avalanches per recording is 83289 and the histogram mode 81707, about eight times the stated 10,000; only 2 of 435 recordings have 9000 to 11000 avalanches.
--- cell 14 [markdown] tags=None
## fig8-subsampling-exponents

> In the culture recordings, sub-sampling extrapolation gives lower values of tau and alpha with
> lower errors than the search algorithm on the full system, while 1/sigma nu z changes little
> between the two.

Full system: tau and alpha by the range search of `plparams.m` after the cuts, 1/sigma nu z from
size given duration over the fitted duration range and from the shape collapse. Sub-sampling
[... 6 more lines not kept]
```

**Agent**

I'm adding the log10 avalanche-count histogram the verifier asked for (fig2e), then the models changes.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json
d=json.load(open("culture_criticality.ipynb"))
c=d["cells"][12]
src="".join(c["source"])
src=src.replace('plt.figure(figsize=(4, 3)); plt.hist(nav, bins=k_nav); plt.xlabel("avalanches per recording"); plt.show()',
'''lnav = np.log10(nav)
counts, edges = np.histogram(lnav, bins=np.arange(3.0, 6.01, 0.25))
print("log10 avalanches per recording, histogram (bins of 0.25 decades):")
print(pd.Series(counts, index=[f"{a:.2f}-{b:.2f}" for a, b in zip(edges[:-1], edges[1:])]).to_string())
print(f"recordings with 10^3.5 to 10^4.5 avalanches (within half a decade of 10,000): {int(np.sum((lnav >= 3.5) & (lnav <= 4.5)))}; "
      f"median log10 {np.median(lnav):.2f}")
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].hist(nav, bins=k_nav); ax[0].set_xlabel("avalanches per recording")
ax[1].hist(lnav, bins=edges); ax[1].set_xlabel("log10 avalanches per recording"); ax[1].axvline(4, color="k", ls="--", lw=.8)
plt.tight_layout(); plt.show()''')
c["source"]=src.splitlines(keepends=True)
json.dump(d, open("culture_criticality.ipynb","w"), indent=1, ensure_ascii=False); open("culture_criticality.ipynb","a").write("\n")
EOF
git diff --stat
```

```
.../culture_criticality.ipynb                      | 11 ++++++++-
 entries/crcns-hc-8-timme-2016/hc8.py               | 26 ++++++++++++++++++----
 tools/build_site.py                                |  8 +++++--
 3 files changed, 38 insertions(+), 7 deletions(-)
```

**Agent**

Now the complexity notebook: 100 subsets, 40 recordings, and a seed-stability cell.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json, copy
f="complexity_culture.ipynb"
d=json.load(open(f))
C=d["cells"]
def setsrc(c, s): c["source"]=s.splitlines(keepends=True)
s="".join(C[0]["source"])
s=s.replace("""The
paper uses up to 100 random subsets per subset size; this notebook uses 10, to fit the time limit
of 8 conditions), and runs on 180 of the 435 recordings drawn with a fixed seed.""","""It uses
100 random subsets per subset size, as Methods 2.9 give, and runs on 40 of the 435 recordings drawn
with a fixed seed, to fit the time limit of a notebook. A first version used 10 subsets on 180
recordings; the verifier found the cut unstable at 10 subsets, and the spread of the estimate over
repeated draws is shown below at 10 and 100 subsets.""")
setsrc(C[0], s)
s="".join(C[1]["source"])
s=s.replace('N_SUBSETS = 10        # Methods 2.9 give up to 100; 10 to fit the time limit (a deviation)',
            'N_SUBSETS = 100       # Methods 2.9: "the lesser of either all possible permutations of neurons or 100"')
s=s.replace("""# 180 of the 435 recordings, drawn with a fixed seed: all 435 would take about 68 min with 4
# processes (37 s per recording in development), over the 60 min limit of a notebook
N_RECORDINGS = 180""","""# 40 of the 435 recordings, drawn with a fixed seed: with 100 subsets per size one recording (8
# conditions) took 50 s of wall time with 4 processes in development, so all 435 would take about
# 6 h, over the 60 min limit of a notebook
N_RECORDINGS = 40""")
setsrc(C[1], s)
md=copy.deepcopy(C[3]); setsrc(md, """## Spread of the estimate over repeated draws

The verifier of the first version asked how much the toolbox's complexity (correction and cut)
varies with the random draws (the subsets and the time permutation of the correction). The real
data of 10 of the recordings above are run three times with different generators, at 10 and at 100
subsets per size. No claim is decided here.""")
md["metadata"]={}
code=copy.deepcopy(C[2]); code["metadata"]={}; code["outputs"]=[]; code["execution_count"]=None
setsrc(code, """t1 = time.time()
with mp.get_context("spawn").Pool(4) as pool:
    parts = pool.map(hc8.complexity_seeds, [(i, names[i], SEED, (10, N_SUBSETS), 3) for i in idx[:10]], chunksize=1)
sd = pd.DataFrame([r for part in parts for r in part])
print(f"{sd.name.nunique()} recordings x 3 draws x 2 subset numbers in {(time.time() - t1) / 60:.1f} min")
for ns, g in sd.groupby("n_subsets"):
    per = g.groupby("name").agg(C_min=("C", "min"), C_max=("C", "max"), C_mean=("C", "mean"),
                                k_min=("k_kept", "min"), k_max=("k_kept", "max"), N=("N", "first"),
                                Cuncut_min=("Cuncut", "min"), Cuncut_max=("Cuncut", "max"))
    per["C_cv"] = g.groupby("name").C.std() / per.C_mean
    print(f"\\n{ns} subsets per size, per recording (complexity in bits/neuron):")
    print(per.to_string(float_format=lambda v: f"{v:.5f}"))
    print(f"median over recordings of the coefficient of variation of the cut complexity: {per.C_cv.median():.2f}; "
          f"of max/min: {(per.C_max / per.C_min).median():.2f}")
    print(f"subset sizes kept by the cut, all runs: median {g.k_kept.median():.0f}, range {g.k_kept.min()} to {g.k_kept.max()} "
          f"(of N {g.N.min()} to {g.N.max()}); kept/N median {(g.k_kept / g.N).median():.2f}")
""")
C[3:3]=[md, code]
json.dump(d, open(f,"w"), indent=1, ensure_ascii=False); open(f,"a").write("\n")
EOF
git diff --stat complexity_culture.ipynb
```

```
.../crcns-hc-8-timme-2016/complexity_culture.ipynb | 55 +++++++++++++++++++---
 1 file changed, 48 insertions(+), 7 deletions(-)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-hc-8-timme-2016/hc8.py",
 "old_string": "    X = raster_matrix(p[\"raster\"], np.flatnonzero(p[\"act\"]) + 1)\n    out = []",
 "new_string": "    X = raster_matrix(p[\"raster\"], np.flatnonzero(p[\"act\"]) + 1)\n    X = X[:, np.asarray(X.sum(axis=0)).ravel() > 0]\n    out = []"
}
```

```
The file entries/crcns-hc-8-timme-2016/hc8.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; python3 - <<'EOF'
s=open("models.py").read()
s=s.replace("""    (both readings) extrapolated the same way, and B_new (delays 1 to 8, A(t) <= 5, no
    sub-sampling, Methods 2.11). args = (p_trans, n_models, t_steps, seed).""","""    (both readings) extrapolated the same way, and B_new (delays 1 to 8, A(t) <= 5, no
    sub-sampling, Methods 2.11). For comparison with 4 p_trans, the mean avalanche size, B_basic
    (Eq. 11) and the one-step ratio sum A(t+1) / sum A(t) over bins with A(t) > 0.
    args = (p_trans, n_models, t_steps, seed).""")
s=s.replace("""                   quad_size=_quad_coef(s), quad_dur=_quad_coef(d))
""","""                   quad_size=_quad_coef(s), quad_dur=_quad_coef(d), mean_size=float(s.mean()),
                   br_basic=hc8.branching_basic(A))
        on = A[:-1] > 0
        rec["one_step"] = float(A[1:][on].sum() / A[:-1][on].sum())
""")
open("models.py","w").write(s)
EOF
git diff models.py | head -30
```

```
diff --git a/entries/crcns-hc-8-timme-2016/models.py b/entries/crcns-hc-8-timme-2016/models.py
index 955253b3b8..948b228517 100644
--- a/entries/crcns-hc-8-timme-2016/models.py
+++ b/entries/crcns-hc-8-timme-2016/models.py
@@ -165,7 +165,9 @@ def cb_point(args) -> list[dict]:
     distributions, the shape collapse curvature of the full model and extrapolated by sub-sampling
     (30 sub-samples from 40 to 100 neurons, sizes evenly spaced, Methods 2.10), the susceptibility
     (both readings) extrapolated the same way, and B_new (delays 1 to 8, A(t) <= 5, no
-    sub-sampling, Methods 2.11). args = (p_trans, n_models, t_steps, seed)."""
+    sub-sampling, Methods 2.11). For comparison with 4 p_trans, the mean avalanche size, B_basic
+    (Eq. 11) and the one-step ratio sum A(t+1) / sum A(t) over bins with A(t) > 0.
+    args = (p_trans, n_models, t_steps, seed)."""
     import hc8
     p_trans, n_models, t_steps, seed = args
     rng = np.random.default_rng(seed)
@@ -177,7 +179,10 @@ def cb_point(args) -> list[dict]:
         A = R.sum(axis=1).astype(np.int32)
         s, d, st = hc8.avalanches(A)
         rec = dict(p_trans=p_trans, model=m, n_av=int(s.size), active_frac=float((A > 0).mean()),
-                   quad_size=_quad_coef(s), quad_dur=_quad_coef(d))
[... 7 more lines not kept]
```

**Agent**

Now the notebook cells.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json, copy
f="models.ipynb"
d=json.load(open(f)); C=d["cells"]
src=lambda i: "".join(C[i]["source"])
def setsrc(c, s): c["source"]=s.splitlines(keepends=True)
# cell 0 table
s=src(0)
old=s[s.index("| fig7c-cb-curvature-no-peak"):]
setsrc(C[0], s.replace(old, """| fig7c-cb-curvature-no-peak | tested on both p_trans grids |
| fig7ab-cb-complexity-susceptibility-peak | tested on its susceptibility half, both grids; the complexity of 30 sub-samples per model was not computed (too large) |
| fig7a-complexity-boundary-rise | blocked, too_large (needs the complexity of fig7ab) |
| figs2-recording-length | blocked, too_large |
| fig7d-cb-branching-ratio-near-1 | tested against the peaks found in fig7ab |
"""))
# cell 1 setup
s=src(1)
s=s.replace('N_SUBSETS = 10      # random subsets per size for complexity (Methods 2.9 give up to 100)',
 'N_SUBSETS = 100     # random subsets per size for complexity (Methods 2.9)\nN_DRAWS = 5         # repeated draws of the complexity estimate for the Bethe claims (spread only)')
s=s.replace('GRID = np.round(np.arange(0.20, 0.30 + 1e-9, 0.01), 2)  # claims file, p_trans grid reading (b)',
 'GRID = np.round(np.arange(0.20, 0.30 + 1e-9, 0.005), 3)  # claims file, p_trans grid reading (a); reading (b) is every other value')
s=s.replace('[(float(p), CB_MODELS, CB_STEPS, [SEED, j]) for j, p in enumerate(GRID)]',
 '[(float(p), CB_MODELS, CB_STEPS, [SEED, int(round(p * 1000))]) for p in GRID]')
s=s.replace('cb = pd.DataFrame([r for part in cb_parts for r in part])',
 'cb = pd.DataFrame([r for part in cb_parts for r in part])\ncb["grid_b"] = np.isclose(np.round(cb.p_trans * 100), cb.p_trans * 100)   # on the 0.01 grid')
s+='''

def draws(X, key):
    """The complexity estimate repeated N_DRAWS times with other generators (subsets and correction)."""
    return pd.DataFrame([hc8.complexity(X, N_SUBSETS, np.random.default_rng([SEED, key, r]), return_variants=True)
                         for r in range(N_DRAWS)])


def interior_maxima(m):
    """Grid values whose mean is above both neighbours."""
    v = m.values
    return [float(m.index[i]) for i in range(1, len(v) - 1) if v[i] > v[i - 1] and v[i] > v[i + 1]]


GRIDS = {"(a) 0.005": slice(None), "(b) 0.01": "grid_b"}
on_grid = lambda df, g: df if GRIDS[g] == slice(None) else df[df[GRIDS[g]]]'''
setsrc(C[1], s)
# fig5d cell 7
s=src(7)
s+='''
d5 = draws(X5[:, keep5], 51)
print(f"repeated draws ({N_DRAWS}): cut complexity {d5['cut'].min():.5f} to {d5['cut'].max():.5f} (mean {d5['cut'].mean():.5f}), "
      f"sizes kept {d5.k_kept.min()} to {d5.k_kept.max()} of {cx5['N']}; no cut {d5.uncut.min():.4f} to {d5.uncut.max():.4f}; "
      f"above zero in {int((d5['cut'] > 0).sum())} of {N_DRAWS}")'''
setsrc(C[7], s)
# fig5e cell 10
s=src(10)
s+='''
ds = draws(Xs[:, ks], 53)
print(f"repeated draws: shuffled cut complexity {ds['cut'].min():.5f} to {ds['cut'].max():.5f} (sizes kept {ds.k_kept.min()} to {ds.k_kept.max()}); "
      f"ratio of the means {ds['cut'].mean() / d5['cut'].mean():.3f}; largest shuffled / smallest original {ds['cut'].max() / d5['cut'].min():.3f}")'''
setsrc(C[10], s)
# fig5f cell 13
s=src(13)
s+='''
dp = draws(Xp[:, kp], 55)
rel = lambda a, b: abs(a - b) / b
print(f"repeated draws: permuted cut complexity {dp['cut'].min():.5f} to {dp['cut'].max():.5f} (sizes kept {dp.k_kept.min()} to {dp.k_kept.max()}); "
      f"relative difference of the means {rel(dp['cut'].mean(), d5['cut'].mean()):.3f}; no cut {rel(dp.uncut.mean(), d5.uncut.mean()):.3f}; "
      f"no correction {rel(dp.raw.mean(), d5.raw.mean()):.3f}")
print(f"spread of the original's own draws: largest relative difference from their mean {(d5['cut'] - d5['cut'].mean()).abs().max() / d5['cut'].mean():.3f}")'''
setsrc(C[13], s)
# fig6 cell 16
setsrc(C[16], '''q = cb.groupby("p_trans")[["quad_size", "quad_dur"]].agg(["mean", "std", "count"])
print(q.round(4).to_string())
for g in GRIDS:
    for col in ("quad_size", "quad_dur"):
        m = on_grid(cb, g).groupby("p_trans")[col].mean()
        print(f"grid {g}, {col}: p 0.2 {m[0.2]:.4f} (negative: {m[0.2] < 0}), p 0.3 {m[0.3]:.4f} (positive: {m[0.3] > 0}), "
              f"p 0.25 {m[0.25]:.4f}; smallest magnitude among 0.2, 0.25, 0.3 at {m.loc[[0.2, 0.25, 0.3]].abs().idxmin()}; "
              f"over the grid at {m.abs().idxmin()}")''')
# fig7c cell 19
setsrc(C[19], '''cv = cb.groupby("p_trans")[["curv_ss", "curv_full"]].agg(["mean", "std"])
print(cv.round(3).to_string())
for g in GRIDS:
    m = on_grid(cb, g).groupby("p_trans").curv_ss.mean()
    peaks = interior_maxima(m)
    near = [p for p in peaks if abs(p - 0.25) <= 0.02 or abs(p - 0.265) <= 0.02]
    mf = on_grid(cb, g).groupby("p_trans").curv_full.mean()
    print(f"grid {g}: extrapolated |curvature| p 0.2 {m[0.2]:.3f} vs p 0.3 {m[0.3]:.3f} (0.2 larger: {m[0.2] > m[0.3]}); "
          f"interior maxima at {peaks}; within 0.02 of 0.25 or 0.265: {near}; largest at {m.idxmax()}; "
          f"full 100-neuron system largest at {mf.idxmax()}, interior maxima {interior_maxima(mf)}")
print("models with a failed shape collapse (NaN):", int(cb.curv_ss.isna().sum()))''')
# replace cells 21, 22 by fig7ab and fig7d sections
h7ab=copy.deepcopy(C[18]); setsrc(h7ab, """## fig7ab-cb-complexity-susceptibility-peak

> Across cortical branching models, the complexity and the susceptibility (both extrapolated to
> infinite size by sub-sampling) peak near p_trans 0.265, close to the infinite system critical
> point of 0.25.

The criterion needs both peaks within 0.0265 of 0.265. The susceptibility, extrapolated by
sub-sampling (layout reading a), is computed for both readings of Eq. 14 and both grids. The
complexity of 30 sub-samples of each model was not computed: with 100 subsets per size, one
whole-system complexity of a model at p_trans 0.3 took 134 s in development, and the claim needs
about 18,900 sub-sample computations on reading (a) of the grid.""")
c7ab=copy.deepcopy(C[19]); c7ab["metadata"]={"tags":["claim:fig7ab-cb-complexity-susceptibility-peak"]}; c7ab["outputs"]=[]; c7ab["execution_count"]=None
setsrc(c7ab, '''print(cb.groupby("p_trans")[["chi_a_ss", "chi_b_ss", "chi_a_full", "chi_b_full"]].mean().to_string(float_format=lambda v: f"{v:.5g}"))
chi_peaks = {}
for g in GRIDS:
    for col, lab in (("chi_a_ss", "reading (a) var(A/N)"), ("chi_b_ss", "reading (b) N var(A/N)")):
        m = on_grid(cb, g).groupby("p_trans")[col].mean()
        peaks = interior_maxima(m)
        chi_peaks[(g, col)] = peaks
        inc = bool(np.all(np.diff(m.values) > 0))
        print(f"grid {g}, extrapolated susceptibility {lab}: largest at p_trans {m.idxmax()}; interior maxima {peaks}; "
              f"within 0.0265 of 0.265: {[p for p in peaks if abs(p - 0.265) <= 0.0265]}; rises at every step: {inc}")
    mf = on_grid(cb, g).groupby("p_trans").chi_b_full.mean()
    print(f"grid {g}, whole 100-neuron system N var(A/N): largest at {mf.idxmax()}, interior maxima {interior_maxima(mf)}")''')
r7ab=copy.deepcopy(C[20]); setsrc(r7ab, "**Result: ...** (written after the run)")
h7d=copy.deepcopy(C[18]); setsrc(h7d, """## fig7d-cb-branching-ratio-near-1

> The cortical branching model's branching ratio is closest to 1 near the same transmission
> probability at which complexity and susceptibility peak.

B_new from the whole system (delays 1 to 8, A(t) <= 5), compared with the peaks found under
fig7ab-cb-complexity-susceptibility-peak. For comparison with the model's design (four neighbours,
critical at p_trans 0.25), the mean avalanche size, B_basic (Eq. 11) and the one-step ratio
sum A(t+1) / sum A(t) are printed against 4 p_trans.""")
c7d=copy.deepcopy(c7ab); c7d["metadata"]={"tags":["claim:fig7d-cb-branching-ratio-near-1"]}
setsrc(c7d, '''ref = cb.groupby("p_trans")[["B_new", "br_basic", "one_step", "mean_size", "n_av"]].mean()
ref["4 p_trans"] = 4 * ref.index.values
print(ref.to_string(float_format=lambda v: f"{v:.4f}"))
for g in GRIDS:
    b = on_grid(cb, g).groupby("p_trans").B_new.mean()
    pb = float((b - 1).abs().idxmin())
    pk = sorted({p for (gg, _), ps in chi_peaks.items() if gg == g for p in ps})
    print(f"grid {g}: mean B_new closest to 1 at p_trans {pb} ({b[pb]:.4f}); susceptibility interior maxima {pk}; "
          f"within 0.0265 of one of them: {[p for p in pk if abs(p - pb) <= 0.0265]}; within 0.0265 of the paper's 0.265: {abs(pb - 0.265) <= 0.0265}")
print(f"run time of this notebook so far: {(time.time() - t0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")''')
r7d=copy.deepcopy(r7ab)
C[21:23]=[h7ab, c7ab, r7ab, h7d, c7d, r7d]
json.dump(d, open(f,"w"), indent=1, ensure_ascii=False); open(f,"a").write("\n")
for i,c in enumerate(d["cells"]): print(i, c["cell_type"], c.get("metadata",{}).get("tags"), "".join(c["source"])[:60].replace("\n"," "))
EOF
```

```
0 markdown None # Timme et al. (2016): the model claims (chain model, Bethe 
1 code None import os for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS
2 code ['sanity'] print("chain model: 12 neurons, c in {0, 0.8, 1}, exact join
3 markdown None ## fig3-chain-model-complexity  > In the 12-neuron chain mod
4 code ['claim:fig3-chain-model-complexity'] for c in (0.0, 0.8, 1.0):     curve = models.chain_integrati
5 markdown None **Result: reproduced.** The whole-system integration is 0 bi
6 markdown None ## fig5d-bethe-small-avalanches  > In the critical Bethe lat
7 code ['claim:fig5d-bethe-small-avalanches'] rng5 = np.random.default_rng([SEED, 5]) fs_full, fd_full, fp
8 markdown None **Result: reproduced.** 7018 of 10000 runs end by layer 8. T
9 markdown None ## fig5e-shuffle-removes-complexity  > In the Bethe lattice 
10 code ['claim:fig5e-shuffle-removes-complexity'] rsh = hc8.rand_shuffle(raster5, nb5, np.random.default_rng([
11 markdown None **Result: reproduced.** Shuffling leaves A(t), and so the si
12 markdown None ## fig5f-network-state-poisson-keeps-complexity  > In the Be
13 code ['claim:fig5f-network-state-poisson-keeps-complexity'] perm = np.random.default_rng([SEED, 54]).permutation(nb5)   
14 markdown None **Result: not reproduced.** Permuting the network states cha
15 markdown None ## fig6-cb-distribution-curvature  > In the cortical branchi
16 code ['claim:fig6-cb-distribution-curvature'] q = cb.groupby("p_trans")[["quad_size", "quad_dur"]].agg(["m
17 markdown None **Result: partially reproduced.** For durations the mean qua
18 markdown None ## fig7c-cb-curvature-no-peak  > The shape collapse curvatur
19 code ['claim:fig7c-cb-curvature-no-peak'] cv = cb.groupby("p_trans")[["curv_ss", "curv_full"]].agg(["m
[... 8 more lines not kept]
```

**Agent**

Quick test of both changed notebooks on small subsets.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; date -u; export PATH=$TMPDIR/dev/bin:$PATH; time MODELS_QUICK=1 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/q models.ipynb 2>&1 | tail -3
```

```
Mon Nov  9 13:21:50 UTC 2026

[31mValueError[39m: Encountered all NA values


real	1m43.767s
user	2m22.315s
sys	0m1.892s
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; export PATH=$TMPDIR/dev/bin:$PATH; MODELS_QUICK=1 jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/q models.ipynb 2>&1 | tail -1; python - <<'EOF'
import json,os
d=json.load(open(os.environ["TMPDIR"]+"/q/models.ipynb"))
for i,c in enumerate(d["cells"]):
    if c["cell_type"]=="code":
        for o in c["outputs"]:
            t=o.get("text") or "".join(o.get("traceback",[]))[-1500:] if o.get("output_type")!="display_data" else ""
            print(i, "".join(t)[-1800:] if isinstance(t,list) else t[-1800:])
EOF
```

```
[NbConvertApp] Writing 51612 bytes to /tmp/claude-1001/q/models.ipynb
1 cortical branching models: 42 (2 per p_trans, 21 values, 30000 steps) in 0.3 min

2 chain model: 12 neurons, c in {0, 0.8, 1}, exact joint distribution
Bethe lattice: 10000 runs, p_trans 0.5, stop layer 10^4; small avalanches end by layer 8 (255 neurons)
cortical branching model: 100 neurons (10 x 10 torus), p_spont 1e-4, 30000 steps, 2 models per p_trans
p_trans                     0.200    0.205    0.210    0.215    0.220    0.225    0.230    0.235   0.240    0.245   0.250    0.255    0.260    0.265    0.270   0.275   0.280    0.285    0.290    0.295    0.300
avalanches (median)       278.500  308.000  286.000  266.500  275.500  302.000  297.500  314.500  272.00  275.500  283.50  274.000  264.500  265.000  273.000  268.50  255.00  224.500  224.000  180.500  129.000
active fraction (median)    0.031    0.034    0.034    0.031    0.034    0.042    0.042    0.049    0.05    0.052    0.06    0.067    0.073    0.072    0.109    0.12    0.17    0.221    0.264    0.376    0.556

4 c = 0.0: whole-system integration 0.000000 bits; integration at k = 2, 6, 12: [0. 0. 0.]; complexity 0.00000000 bits

4 c = 0.8: whole-system integration 5.841048 bits; integration at k = 2, 6, 12: [0.1966 1.9476 5.841 ]; complexity 0.43126968 bits

4 c = 1.0: whole-system integration 11.000000 bits; integration at k = 2, 6, 12: [ 1.  5. 11.]; complexity 0.00000000 bits

7 full model: 10000 runs, largest size 49506953, longest 10000 layers; size fit after cuts: tau 1.402, range 4 to 43, p 0.368
full model shape collapse (durations >= 4 seen >= 20 times): 1/sigma nu z 1.598, curvature -3.056

7 small avalanches: 7018 of 10000 runs; sizes 1 to 32; avalanches in the raster 7018 (sizes match the runs: True)
[... 141 more lines not kept]
```

**Agent**

Quick mode runs through except for NaN guards that the short simulations need (all-NaN columns in fig6/fig7c). I'll add those guards.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json
f="models.ipynb"; d=json.load(open(f)); C=d["cells"]
def edit(i, a, b, count=1):
    s="".join(C[i]["source"]); assert s.count(a)>=1, (i,a); s=s.replace(a,b); C[i]["source"]=s.splitlines(keepends=True)
edit(1, 'on_grid = lambda df, g:', 'arg_min = lambda s: s.dropna().idxmin() if s.notna().any() else None\narg_max = lambda s: s.dropna().idxmax() if s.notna().any() else None\non_grid = lambda df, g:')
edit(16, 'm.loc[[0.2, 0.25, 0.3]].abs().idxmin()', 'arg_min(m.loc[[0.2, 0.25, 0.3]].abs())')
edit(16, 'm.abs().idxmin()', 'arg_min(m.abs())')
edit(19, 'm.idxmax()', 'arg_max(m)'); edit(19, 'mf.idxmax()', 'arg_max(mf)')
edit(22, 'm.idxmax()', 'arg_max(m)'); edit(22, 'mf.idxmax()', 'arg_max(mf)')
json.dump(d, open(f,"w"), indent=1, ensure_ascii=False); open(f,"a").write("\n")
EOF
export PATH=$TMPDIR/dev/bin:$PATH; MODELS_QUICK=1 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/q models.ipynb 2>&1 | tail -1
```

```
[NbConvertApp] Writing 40908 bytes to /tmp/claude-1001/q/models.ipynb
```

**Agent**

Models notebook passes in quick mode. Now a quick run of the complexity notebook on 2 recordings.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; export PATH=$TMPDIR/dev/bin:$PATH; date -u; HC8_SUBSET=2 jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/q complexity_culture.ipynb 2>&1 | tail -1; python - <<'EOF'
import json,os
d=json.load(open(os.environ["TMPDIR"]+"/q/complexity_culture.ipynb"))
for i,c in enumerate(d["cells"][:6]):
    if c["cell_type"]=="code":
        for o in c["outputs"]:
            if o.get("output_type")=="stream": print(i, "".join(o["text"])[-2500:])
            if o.get("output_type")=="error": print(i, "ERROR", o["ename"], o["evalue"])
EOF
date -u
```

```
Mon Nov  9 13:27:18 UTC 2026
[NbConvertApp] Writing 95652 bytes to /tmp/claude-1001/q/complexity_culture.ipynb
1 2 recordings in 2.7 min; peak memory of this process 0.20 GB

2 recordings: 2 | cultures: 2 | neurons analysed: 153
avalanche bins per recording (real): 93104 to 416416
real       complexity (bits/neuron) median 0.02131, range 0.00085 to 0.04178; subset sizes kept by the cut: median 13 of 76; NaN 0
jitter1    complexity (bits/neuron) median 0.01566, range 0.00116 to 0.03016; subset sizes kept by the cut: median 12 of 76; NaN 0
jitter10   complexity (bits/neuron) median 0.00077, range 0.00067 to 0.00087; subset sizes kept by the cut: median 7 of 76; NaN 0
jitter100  complexity (bits/neuron) median 0.00216, range 0.00145 to 0.00287; subset sizes kept by the cut: median 15 of 76; NaN 0
wrap       complexity (bits/neuron) median 0.00145, range 0.00041 to 0.00250; subset sizes kept by the cut: median 16 of 76; NaN 0
poisson    complexity (bits/neuron) median 0.00056, range 0.00051 to 0.00060; subset sizes kept by the cut: median 11 of 76; NaN 0
swap       complexity (bits/neuron) median 0.01270, range 0.00310 to 0.02230; subset sizes kept by the cut: median 16 of 76; NaN 0
shuffle    complexity (bits/neuron) median 0.20037, range 0.16893 to 0.23181; subset sizes kept by the cut: median 68 of 76; NaN 0
neurons left without a spike by shuffling (dropped): 0 recordings
recordings kept under exclusion reading (a): 2 of 2

4 2 recordings x 3 draws x 2 subset numbers in 1.2 min

10 subsets per size, per recording (complexity in bits/neuron):
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p tools/entry.py; sed -n 425,500p tools/entry.py
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
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json
f="models.ipynb"; d=json.load(open(f)); C=d["cells"]
def edit(i, a, b):
    s="".join(C[i]["source"]); assert a in s, (i,a); s=s.replace(a,b); C[i]["source"]=s.splitlines(keepends=True)
def setsrc(i, s): C[i]["source"]=s.splitlines(keepends=True)
edit(0, "| fig7c-cb-curvature-no-peak | tested on both p_trans grids |", "| fig7c-cb-curvature-no-peak | tested on the 0.01 grid (reading b) |")
edit(0, "tested on its susceptibility half, both grids;", "tested on its susceptibility half, 0.01 grid (reading b);")
edit(1, 'GRID = np.round(np.arange(0.20, 0.30 + 1e-9, 0.005), 3)  # claims file, p_trans grid reading (a); reading (b) is every other value',
        'GRID = np.round(np.arange(0.20, 0.30 + 1e-9, 0.01), 2)  # claims file, p_trans grid reading (b)')
edit(1, '[(float(p), CB_MODELS, CB_STEPS, [SEED, int(round(p * 1000))]) for p in GRID]', '[(float(p), CB_MODELS, CB_STEPS, [SEED, j]) for j, p in enumerate(GRID)]')
edit(1, '\ncb["grid_b"] = np.isclose(np.round(cb.p_trans * 100), cb.p_trans * 100)   # on the 0.01 grid', '')
edit(1, '''arg_max = lambda s: s.dropna().idxmax() if s.notna().any() else None
on_grid = lambda df, g: df if GRIDS[g] == slice(None) else df[df[GRIDS[g]]]''', 'arg_max = lambda s: s.dropna().idxmax() if s.notna().any() else None')
edit(1, '''

GRIDS = {"(a) 0.005": slice(None), "(b) 0.01": "grid_b"}''', '')
setsrc(16, '''q = cb.groupby("p_trans")[["quad_size", "quad_dur"]].agg(["mean", "std", "count"])
print(q.round(4).to_string())
for col in ("quad_size", "quad_dur"):
    m = cb.groupby("p_trans")[col].mean()
    print(f"{col}: p 0.2 {m[0.2]:.4f} (negative: {m[0.2] < 0}), p 0.3 {m[0.3]:.4f} (positive: {m[0.3] > 0}), "
          f"p 0.25 {m[0.25]:.4f}; smallest magnitude among 0.2, 0.25, 0.3 at {arg_min(m.loc[[0.2, 0.25, 0.3]].abs())}; "
          f"over the grid at {arg_min(m.abs())}")''')
setsrc(19, '''cv = cb.groupby("p_trans")[["curv_ss", "curv_full"]].agg(["mean", "std"])
print(cv.round(3).to_string())
m = cb.groupby("p_trans").curv_ss.mean()
peaks = interior_maxima(m)
near = [p for p in peaks if abs(p - 0.25) <= 0.02 or abs(p - 0.265) <= 0.02]
print(f"extrapolated |curvature|: p 0.2 {m[0.2]:.3f} vs p 0.3 {m[0.3]:.3f} (0.2 larger: {m[0.2] > m[0.3]}); interior maxima at {peaks}; "
      f"within 0.02 of 0.25 or 0.265: {near}")
mf = cb.groupby("p_trans").curv_full.mean()
print(f"full 100-neuron system: p 0.2 {mf[0.2]:.3f} vs 0.3 {mf[0.3]:.3f}; largest at {arg_max(mf)}, interior maxima {interior_maxima(mf)}")
print("models with a failed shape collapse (NaN):", int(cb.curv_ss.isna().sum()))''')
setsrc(22, '''print(cb.groupby("p_trans")[["chi_a_ss", "chi_b_ss", "chi_a_full", "chi_b_full"]].mean().to_string(float_format=lambda v: f"{v:.5g}"))
chi_peaks = []
for col, lab in (("chi_a_ss", "reading (a) var(A/N)"), ("chi_b_ss", "reading (b) N var(A/N)")):
    m = cb.groupby("p_trans")[col].mean()
    peaks = interior_maxima(m)
    chi_peaks += peaks
    print(f"extrapolated susceptibility {lab}: largest at p_trans {arg_max(m)}; interior maxima {peaks}; "
          f"within 0.0265 of 0.265: {[p for p in peaks if abs(p - 0.265) <= 0.0265]}; rises at every step: {bool(np.all(np.diff(m.values) > 0))}")
mf = cb.groupby("p_trans").chi_b_full.mean()
print(f"whole 100-neuron system N var(A/N): largest at {arg_max(mf)}, interior maxima {interior_maxima(mf)}")''')
setsrc(25, '''ref = cb.groupby("p_trans")[["B_new", "br_basic", "one_step", "mean_size", "n_av"]].mean()
ref["4 p_trans"] = 4 * ref.index.values
print(ref.to_string(float_format=lambda v: f"{v:.4f}"))
pb = float((ref.B_new - 1).abs().idxmin())
pk = sorted(set(chi_peaks))
print(f"mean B_new closest to 1 at p_trans {pb} ({ref.B_new[pb]:.4f}); susceptibility interior maxima {pk}; "
      f"within 0.0265 of one of them: {[p for p in pk if abs(p - pb) <= 0.0265]}; within 0.0265 of the paper's 0.265: {abs(pb - 0.265) <= 0.0265}")
print(f"run time of this notebook so far: {(time.time() - t0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")''')
edit(21, "computed for both readings of Eq. 14 and both grids.", "computed for both readings of Eq. 14 on the 0.01 grid (reading b).")
edit(21, "about 18,900 sub-sample computations on reading (a) of the grid.", "9,900 sub-sample computations on this grid and 18,900 on the 0.005 grid.")
json.dump(d, open(f,"w"), indent=1, ensure_ascii=False); open(f,"a").write("\n")
EOF
grep -n "GRIDS\|on_grid\|grid_b" models.ipynb; export PATH=$TMPDIR/dev/bin:$PATH; MODELS_QUICK=1 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/q models.ipynb 2>&1 | tail -1
```

```
[NbConvertApp] Writing 36074 bytes to /tmp/claude-1001/q/models.ipynb
```

**Agent**

Quick test passes. Running the entry check, then the full run.

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -5; date -u
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: DuplicateCellId: Non-unique cell id 'cebc6b1c' detected. Corrected to 'b01e93d0'.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: DuplicateCellId: Non-unique cell id '345e3060' detected. Corrected to 'd94f8be3'.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
Mon Nov  9 13:33:37 UTC 2026
```

**Agent**

Duplicate cell ids from copying cells; I'll give the new cells fresh ids, then start the full run.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json, uuid
for f in ("models.ipynb","complexity_culture.ipynb","culture_criticality.ipynb"):
    d=json.load(open(f)); seen=set(); n=0
    for c in d["cells"]:
        if c.get("id") in seen: c["id"]=uuid.uuid4().hex[:8]; n+=1
        seen.add(c.get("id"))
    json.dump(d, open(f,"w"), indent=1, ensure_ascii=False); open(f,"a").write("\n"); print(f, n)
EOF
cd ../..; python tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -2
```

```
models.ipynb 6
complexity_culture.ipynb 2
culture_criticality.ipynb 0
0 error(s)
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/crcns-hc-8-timme-2016 2>&1 | tail -15; date -u
```
