# rich-2014 · author-answers · run 43131845873

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls entries/rich-2014 entries/rich-2014/*; cat questions/rich-2014.yaml
```

```
Thu Nov 12 01:10:28 UTC 2026
entries/rich-2014/README.md
entries/rich-2014/entry.yaml
entries/rich-2014/reproduce_rich_2014.ipynb
entries/rich-2014/requirements.in
entries/rich-2014/requirements.lock.txt
entries/rich-2014/rich.py

entries/rich-2014:
README.md
entry.yaml
reproduce_rich_2014.ipynb
requirements.in
requirements.lock.txt
rich.py
# Questions from attempt rich-2014-01 (author, 2026-11-12) about the claims file
# claims/rich-2014.yaml, asked under docs/protocol.md, Author, step 1.6. The attempt tests each claim
# as the file has it and shows the other reading as a variant; the outcomes stay as tested.
paper: doi:10.1126/science.1255635
questions:
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i -E "^[0-9]+:[0-9]+:#|1\.6|settle|answer" | head -80; wc -l docs/protocol.md
```

```
29:29:workflow (roles `claims`, `claims-check` and `answer`), the only runs that
32:32:`author`, `author-answers` when a reader answered a question on the claims
63:63:open and the code settles it, follow the code and say so. Where they disagree,
112:112:     settled by its expected values alone ("similar", "many", "tended to").
135:135:     (author, step 1.6), with every result shown. An outcome that rests on a
186:186:### 6. Answer questions
190:190:not say what the paper says (author, step 1.6, and "Hand over for
194:194:Where it is, the reader amends the claim, and the question's `answer` says
195:195:what changed and why, citing the passage; where it is not, the answer says why
196:196:the claim stands. The reader marks each question answered in
318:318:   - When the readings give different outcomes, or the paper does not settle
342:342:     claims file (reader, step 6), and a later run, `author-answers`,
376:376:  passage of the paper it was taken from (author, step 1.6), an assumption
654 docs/protocol.md
```

**Agent calls Bash**

```bash
cd  sed -n 200,520p docs/protocol.md
```

```
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

1. List the dataset's files and read its metadata from the archive. Open a
   file and list everything it holds, including every column of every table.
[... 300 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 520,654p docs/protocol.md; grep -n "author-answers" -A12 docs/protocol.md | head -60
```

```
After the first round, fix what it found, re-run, and hand over the full
executed notebook for the second round. Record each round under
`verifications`, saying what was reviewed. Give the verifier's reasons in its
own words, and what you changed in reply under `response`. An outcome the verifier disagrees
with is either changed, with the reason, or left with the disagreement
recorded.

After round 1 the revision may change outcomes, and round 2 reviews them.
From round 2 on, an outcome may not differ from the one the latest
verification round of that claim agreed with: `tools/entry.py check` fails
if it does. A verifier's result is recorded as it gave it; never change
`agrees` to get past this check. The final
revision corrects text and adds the outputs the verifier asked for. If it
finds that an outcome should change, it keeps the verified outcome and writes
the change under `proposed` on that outcome, with the analysis behind it in
the notebook. A third round then settles it: `verifier-3` reviews only the
proposed changes, and `author-revise-3` applies those it agreed with and
records the round. A change that needs an analysis not yet run waits for a
new attempt.

[... 157 more lines not kept]
```

**Agent**

Now the claims file for these two claims and the attempt record.

**Agent calls Bash**

```bash
cd  ls attempts | grep rich; python - <<'E'
import yaml
c=yaml.safe_load(open('claims/rich-2014.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig4b-single-field-proportion','fig4c-active-subsets'):
        print(yaml.safe_dump(cl,sort_keys=False,width=110))
E
```

```
perich-2018-01.yaml
rich-2014-01.yaml
richardson-2018-01.yaml
id: fig4b-single-field-proportion
statement: Under the gamma-distributed propensities the proportion of cells with a single field would stay at about
  5 to 10% over a wide range of environment sizes, which could allow a simple readout of location.
source: Main text, page 817, paragraph 4; Figure 4B (figure and legend missing from the text read); Materials and
  Methods, Active subset simulation
quote: But with the observed gamma-distributed propensities, the proportion of cells with single fields would remain
  at ~5 to 10% over a wide range of environment sizes
expected:
- quantity: lowest single-field proportion over the range
  value: 5
  tolerance: 0.5
  unit: '%'
- quantity: highest single-field proportion over the range
  value: 10
  tolerance: 1
  unit: '%'
depends_on:
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/rich-2014-01.yaml; cat entries/rich-2014/entry.yaml
```

```
schema_version: 3
id: rich-2014-01
datasets:
- archive: crcns
  id: hc-31
  version: unversioned
  doi: 10.6080/K0BV7DT2
  relation: primary
paper: doi:10.1126/science.1255635
date: 2026-11-12
entry: rich-2014
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 394 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/rich-2014; python - <<'E'
import json
nb=json.load(open('reproduce_rich_2014.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'fig4b' in s or 'fig4c' in s or 'single' in s.lower() and 'field' in s.lower() and i>40 or c['cell_type']=='markdown' and ('Summary' in s[:200]):
        print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
        print(s)
E
```

```
=== cell 0 markdown None
# Reproducing Rich, Liaw & Lee (2014) from CRCNS hc-31

Paper. Rich PD, Liaw H-P, Lee AK (2014). Large environments reveal the statistical structure
governing hippocampal representations. *Science* 345:814-817.
[doi:10.1126/science.1255635](https://doi.org/10.1126/science.1255635). The claims file
(`claims/rich-2014.yaml`) was written from the version of record and its supplement (Materials and
Methods, Supplementary Text, Figs. S1 to S18); the last page of the article (Fig. 4 and its legend)
was damaged in the copy read.

Data set. [CRCNS hc-31](https://doi.org/10.6080/K0BV7DT2), "Extracellular CA1 activity from rats
during exploration of a novel 48m track", data description version 0.6 (Oct 30, 2022). CRCNS data
sets are not versioned, so the version is recorded as `unversioned` with the data set's DOI
10.6080/K0BV7DT2; this is the only published state of the data set and the paper cites none. The
analysis reads one file, `hc-31/live/data/resSave.mat`, streamed from the public bucket
`crcnsarchive` into memory. Its MD5 in the data set's `checksums.md5` is
`f97e58107878c688854474519fa6be72`, and the first cell checks the bytes read against it. The other
files are `csc_files.tar.gz` (8.8 GB, one wideband LFP channel per rat), the Neuralynx import code,
`example_script.m` and the readme. The LFP is not needed: the data set gives the PRE slow-wave sleep
periods (`intSWS`) that the paper detected.
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/rich-2014; python - <<'E'
import json
nb=json.load(open('reproduce_rich_2014.ipynb'))
for i in range(88,103):
    c=nb['cells'][i]
    print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
E
ls ../../executed/rich-2014 2>/dev/null
```

```
Exit code 2
=== cell 88 markdown None
## fig4b-single-field-proportion

> Under the gamma-distributed propensities the proportion of cells with a single field would stay at about 5 to 10% over a wide range of environment sizes, which could allow a simple readout of location.
=== cell 89 code ['claim:fig4b-single-field-proportion']
L = np.logspace(-1, 4, 2001)

def single_field(r, p, L, reading):
    pL = 1 / (1 + (L / 48) * (1 - p) / p)
    one = r * pL ** r * (1 - pL)
    return one if reading == "X-a" else one / (1 - pL ** r)

def widest(L, y, lo=4.5, hi=11.0):
    ok = (y >= lo) & (y <= hi)
    best = (np.nan, np.nan, 1.0)
    for s0, e0 in zip(*rich._runs(ok)):
        fac = L[e0 - 1] / L[s0]
        if fac > best[2] or np.isnan(best[0]):
            best = (L[s0], L[e0 - 1], fac)
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -rn -i -E "active subset|300 |exclusive|logarithm|log scale|S18" paper/* | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 370,392p paper/10.1126-science.1255635.txt; sed -n 740,760p paper/10.1126-science.1255635.txt; sed -n 1310,1330p paper/10.1126-science.1255635.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Both answers changed criteria. I'll prototype the two re-tests standalone with the fitted values before editing the notebook. First, a look at Fig. S18 itself for the spacing of sizes.

**Agent calls Bash**

```bash
cd  which pdftoppm pdftotext; pdftotext paper/10.1126-science.1255635.supp-rich.sm.pdf - | grep -n "Fig. S18" | head; python -c "
import fitz" 2>&1 | head -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import pypdf
r=pypdf.PdfReader('paper/10.1126-science.1255635.supp-rich.sm.pdf')
for i,p in enumerate(r.pages):
    t=p.extract_text() or ''
    if 'Fig. S18' in t: print(i, len(r.pages))
" 2>&1 | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.1255635.supp-rich.sm.pdf",
 "pages": "44-46"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Figures can't be rendered here, so the spacing stays open. Prototyping both claims with the P-a fit (r 0.559, p 0.152, mean 3.126):

**Agent calls Bash**

```bash
cd $TMPDIR; cat > proto.py <<'E'
import numpy as np, time
t=time.time()
def single_field(r,p,L,X):
    pL=1/(1+(L/48)*(1-p)/p); one=r*pL**r*(1-pL)
    return one if X=="X-a" else one/(1-pL**r)
L=np.logspace(-1,4,2001)
def widest(y):
    ok=(y>=4.5)&(y<=11); best=(0,0,1)
    idx=np.flatnonzero(np.diff(np.r_[0,ok.astype(int),0]))
    for s,e in zip(idx[::2],idx[1::2]):
        f=L[e-1]/L[s]
        if f>best[2]: best=(L[s],L[e-1],f)
    return best
for rp in [(0.57,0.14),(0.559,0.152)]:
    for X in ("X-a","X-b"): print(rp,X,widest(100*single_field(*rp,L,X)))
def xor(rates,sizes,rng):
    A=(rng.poisson(np.outer(rates,sizes))>0).astype(float)
    return (A.T@(1-A)+(1-A).T@A)/len(rates)
r,p,m=0.559,0.152,3.126
for G in ("G-a","G-b"):
    rng=np.random.default_rng(4)
    sizes=np.logspace(-1,np.log10(50),300) if G=="G-a" else np.linspace(0.1,50,300)
    gp=xor(rng.gamma(r,(1-p)/p/48,1000),sizes,rng); eq=xor(np.full(1000,m/48),sizes,rng)
    off=~np.eye(300,dtype=bool)
    for K in (0.1,0.2): print(G,K,np.mean(gp[off]>K),np.mean(eq[off]>K))
    for seed in range(5):
        rng=np.random.default_rng(100+seed)
        gp=xor(rng.gamma(r,(1-p)/p/48,1000),sizes,rng); eq=xor(np.full(1000,m/48),sizes,rng)
        print('  seed',seed,[(round(np.mean(gp[off]>K),3),round(np.mean(eq[off]>K),3)) for K in (0.1,0.2)])
print(time.time()-t)
E
python proto.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/proto.py", line 1, in <module>
    import numpy as np, time
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls -a; ls -d .venv* venv* executed 2>/dev/null; grep -n "venv\|def cmd_all\|def run" tools/entry.py | head -20
```

```
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
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 pv && uv pip install -q --python pv/bin/python numpy && pv/bin/python proto.py
```

```
(0.57, 0.14) X-a (np.float64(117.48975549395303), np.float64(649.3816315762114), np.float64(5.527134079444346))
(0.57, 0.14) X-b (np.float64(171.79083871575875), np.float64(745.5898720277816), np.float64(4.34010263644744))
(0.559, 0.152) X-a (np.float64(132.58671177605595), np.float64(754.2233958475707), np.float64(5.6885293084384125))
(0.559, 0.152) X-b (np.float64(196.11011754760474), np.float64(870.9635899560806), np.float64(4.441196613655889))
G-a 0.1 0.8204236343366779 0.8334448160535117
G-a 0.2 0.6614046822742475 0.7006243032329988
  seed 0 [(np.float64(0.808), np.float64(0.833)), (np.float64(0.639), np.float64(0.703))]
  seed 1 [(np.float64(0.813), np.float64(0.84)), (np.float64(0.638), np.float64(0.704))]
  seed 2 [(np.float64(0.827), np.float64(0.831)), (np.float64(0.663), np.float64(0.708))]
  seed 3 [(np.float64(0.819), np.float64(0.837)), (np.float64(0.652), np.float64(0.706))]
  seed 4 [(np.float64(0.817), np.float64(0.835)), (np.float64(0.649), np.float64(0.706))]
G-b 0.1 0.9994202898550725 0.9801560758082497
G-b 0.2 0.9475585284280936 0.8289409141583055
  seed 0 [(np.float64(0.999), np.float64(0.978)), (np.float64(0.977), np.float64(0.83))]
  seed 1 [(np.float64(0.999), np.float64(0.978)), (np.float64(0.984), np.float64(0.831))]
  seed 2 [(np.float64(0.999), np.float64(0.98)), (np.float64(0.946), np.float64(0.831))]
  seed 3 [(np.float64(0.999), np.float64(0.977)), (np.float64(0.958), np.float64(0.829))]
  seed 4 [(np.float64(0.999), np.float64(0.98)), (np.float64(0.976), np.float64(0.825))]
0.6527864933013916
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/rich-2014; cat README.md; grep -n "fig4\|def _runs" rich.py
```

```
# Rich, Liaw & Lee (2014) from CRCNS hc-31

Tests the findings of [Rich, Liaw & Lee (2014)](https://doi.org/10.1126/science.1255635) on
[CRCNS hc-31](https://doi.org/10.6080/K0BV7DT2), which holds the spikes, positions, PRE sleep periods
and the paper's own place fields for the 253 CA1 cells of five rats that explored a novel 48 m track
and an open field. Place fields are recomputed from spikes and position by the paper's method; the
data set's own fields are shown as a variant.

| Claim | Outcome |
|---|---|
| 253 cells, 63, 58, 24, 57 and 51 per animal | Reproduced |
| Field number uncorrelated with cluster quality (Fig. S3) | Blocked: data missing |
| New sections add fields to place cells and recruit silent cells | Reproduced |
| Single cells with six or more fields are Poisson (Fig. 2A) | Reproduced |
| No population bias in location or interval (Fig. 2B, C) | Reproduced |
| Cells with fewer than six fields uniform (Fig. S6) | Reproduced (assumption) |
| Field counts overdispersed against equal-rate Poisson | Reproduced |
| Mean fields per cell per animal (Fig. S7A) | Partially reproduced |
| Negative binomial r 0.57, p 0.14 | Reproduced |
| Recruitment about 65% at 48 m | Reproduced |
[... 26 more lines not kept]
```

**Agent**

Now the notebook edits: new judging code for both claims, plus the conclusions and summary.

**Agent calls Bash**

```bash
cd entries/rich-2014; cat > $TMPDIR/edit.py <<'E'
import json
P='reproduce_rich_2014.ipynb'
nb=json.load(open(P))
C=nb['cells']
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
assert 'fig4b' in ''.join(C[89]['metadata'].get('tags',[])) and 'fig4c' in ''.join(C[92]['metadata'].get('tags',[]))
setsrc(89,'''L = np.logspace(-1, 4, 2001)

def single_field(r, p, L, reading):
    pL = 1 / (1 + (L / 48) * (1 - p) / p)
    one = r * pL ** r * (1 - pL)
    return one if reading == "X-a" else one / (1 - pL ** r)

def widest(L, y, lo=4.5, hi=11.0):
    ok = (y >= lo) & (y <= hi)
    best = (np.nan, np.nan, 1.0)
    for s0, e0 in zip(*rich._runs(ok)):
        fac = L[e0 - 1] / L[s0]
        if fac > best[2] or np.isnan(best[0]):
            best = (L[s0], L[e0 - 1], fac)
    return best

# The criterion's threshold: the factor spanned by the printed parameters (r 0.57, p 0.14) under the
# same reading, less 10%; the claims file states 5.0 (X-a) and 3.9 (X-b).
NEED = {"X-a": 5.0, "X-b": 3.9}
for X in ("X-a", "X-b"):
    lo_, hi_, fac = widest(L, 100 * single_field(0.57, 0.14, L, X))
    print(f"printed parameters {X}: {lo_:.1f} to {hi_:.1f} m, factor {fac:.2f}, less 10% {0.9 * fac:.2f} "
          f"(claims file {NEED[X]})")
for k in MAIN + ["F-b"]:
    r, p = NB[k]
    for X in ("X-a", "X-b"):
        y = 100 * single_field(r, p, L, X)
        lo_, hi_, fac = widest(L, y)
        inside = y[(L >= lo_) & (L <= hi_)]
        print(f"{k} {X}: at 48 m {100 * single_field(r, p, np.array([48.0]), X)[0]:.1f}%; widest interval inside 4.5-11%: "
              f"{lo_:.1f} to {hi_:.1f} m, factor {fac:.2f} (needed {NEED[X]}, met {fac >= NEED[X]}), "
              f"proportion there {inside.min():.2f} to {inside.max():.2f}%; over 0.1 m to 10 km from {y.min():.2f} to {y.max():.2f}%")
''')
setsrc(90,'''**Result: reproduced.** With the P-a fit the proportion stays inside 4.5 to 11% from 133 to 754 m under X-a, a factor of 5.69 in size, above the 5.0 that the printed parameters less 10% set; X-b gives 196 to 871 m, a factor of 4.44, above 3.9. P-b gives the same (5.73 and 4.46). At 48 m the proportion is 16.5% (X-a), above the 5 to 10% band, so the band holds for environments of roughly 130 to 750 m, not for the track itself. The data set's fields give factors of 5.55 and 4.36.
''')
setsrc(92,'''def xor_matrix(rates_per_m, sizes, rng):
    active = rng.poisson(np.outer(rates_per_m, sizes)) > 0  # cells x environments
    A = active.astype(float)
    return (A.T @ (1 - A) + (1 - A).T @ A) / len(rates_per_m)

SPACING = {"G-a": lambda: np.logspace(-1, np.log10(50), 300), "G-b": lambda: np.linspace(0.1, 50, 300)}
LEVELS = {"K-a": 0.1, "K-b": 0.2}
off = ~np.eye(300, dtype=bool)
rows = []
for k in MAIN + ["F-b"]:
    r, p = NB[k]
    mean_per_m = COUNTS[k].mean() / 48
    for G in ("G-a", "G-b"):
        rng_4c = np.random.default_rng(4)
        sizes = SPACING[G]()
        big = np.outer(sizes > 10, sizes > 10)
        np.fill_diagonal(big, False)
        gp = xor_matrix(rng_4c.gamma(r, (1 - p) / p / 48, 1000), sizes, rng_4c)
        eq = xor_matrix(np.full(1000, mean_per_m), sizes, rng_4c)
        lo = xor_matrix(np.full(1000, mean_per_m / 2), sizes, rng_4c)
        hi = xor_matrix(np.full(1000, mean_per_m * 2), sizes, rng_4c)
        for K, lev in LEVELS.items():
            rows.append(dict(reading=k, G=G, K=K, gamma_poisson=np.mean(gp[off] > lev), equal_rate=np.mean(eq[off] > lev),
                             half_rate=np.mean(lo[off] > lev), twice_rate=np.mean(hi[off] > lev)))
        print(f"{k} {G}: reported, not judged: mean XOR over pairs both > 10 m: gamma-Poisson {gp[big].mean():.3f}, "
              f"equal-rate {eq[big].mean():.3f}, half rate {lo[big].mean():.3f}, twice rate {hi[big].mean():.3f}; "
              f"pairs both > 20 m, twice rate {hi[np.outer(sizes > 20, sizes > 20)].mean():.3f}")
        print(f"     share of cells active at 50 m: gamma-Poisson {np.mean(gp[-1, 0] >= 0):.0f} (see below), "
              f"equal-rate expected {1 - np.exp(-mean_per_m * 50):.3f}")
s4c = pd.DataFrame(rows)
s4c["difference"] = s4c.gamma_poisson - s4c.equal_rate
s4c["gamma_higher"] = s4c.difference > 0
print("Share of all pairs of different environments with an exclusive-OR proportion above the level:")
print(s4c.round(3).to_string(index=False))

# Seed check for the judged comparison (P-a fit): 10 further seeds per spacing.
r, p = NB["F-a/P-a"]
mean_per_m = COUNTS["F-a/P-a"].mean() / 48
for G in ("G-a", "G-b"):
    d = {K: [] for K in LEVELS}
    for seed in range(10):
        rng_seed = np.random.default_rng(400 + seed)
        sizes = SPACING[G]()
        gp = xor_matrix(rng_seed.gamma(r, (1 - p) / p / 48, 1000), sizes, rng_seed)
        eq = xor_matrix(np.full(1000, mean_per_m), sizes, rng_seed)
        for K, lev in LEVELS.items():
            d[K].append(np.mean(gp[off] > lev) - np.mean(eq[off] > lev))
    for K in LEVELS:
        print(f"F-a/P-a {G} {K}: gamma-Poisson minus equal-rate share over 10 seeds, {np.min(d[K]):.3f} to {np.max(d[K]):.3f}")

rng_4c = np.random.default_rng(4)
sizes = SPACING["G-a"]()
r, p = NB["F-a/P-a"]
gp_rates = rng_4c.gamma(r, (1 - p) / p / 48, 1000)
print("expected share of cells active at 50 m: gamma-Poisson", round(float(np.mean(1 - np.exp(-gp_rates * 50))), 3),
      "equal-rate", round(float(1 - np.exp(-COUNTS["F-a/P-a"].mean() / 48 * 50)), 3))
fig, ax = plt.subplots(1, 2, figsize=(8, 3.5))
for i, (name, rates) in enumerate([("gamma-Poisson", gp_rates),
                                    ("equal-rate", np.full(1000, COUNTS["F-a/P-a"].mean() / 48))]):
    M = xor_matrix(rates, sizes, rng_4c)
    im = ax[i].imshow(M, origin="lower", extent=[np.log10(0.1), np.log10(50)] * 2, vmin=0, vmax=0.6)
    ax[i].set_title(f"{name} (F-a/P-a, G-a)"); ax[i].set_xlabel("log10 size (m)")
    print(name, "XOR range", M.min().round(3), "to", M.max().round(3), "(colour scale 0 to 0.6)")
plt.colorbar(im)
plt.show()
''')
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
E
python $TMPDIR/edit.py && git diff --stat .
```

```
entries/rich-2014/reproduce_rich_2014.ipynb | 68 ++++++++++++++++++++++-------
 1 file changed, 52 insertions(+), 16 deletions(-)
```

**Agent**

I left a meaningless print in the loop; removing it.

**Agent calls Bash**

```bash
cd entries/rich-2014; python - <<'E'
import json
P='reproduce_rich_2014.ipynb'
raw=open(P).read()
nb=json.loads(raw)
src=nb['cells'][92]['source']
i=[j for j,l in enumerate(src) if 'share of cells active at 50 m: gamma-Poisson {' in l][0]
del src[i:i+2]
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
E
git diff . | head -5; tail -c 50 reproduce_rich_2014.ipynb | od -c | tail -3
```

```
diff --git a/entries/rich-2014/reproduce_rich_2014.ipynb b/entries/rich-2014/reproduce_rich_2014.ipynb
index cc7b914..eaa8352 100644
--- a/entries/rich-2014/reproduce_rich_2014.ipynb
+++ b/entries/rich-2014/reproduce_rich_2014.ipynb
@@ -1820,15 +1820,22 @@
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent**

Now lock and run the whole entry (recorded runtime about 3 minutes).

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py lock entries/rich-2014 2>&1 | tail -3; git diff --stat entries/rich-2014; time python tools/entry.py all entries/rich-2014 2>&1 | tail -20; date -u
```

```
Thu Nov 12 01:12:19 UTC 2026
wrote rich-2014/requirements.lock.txt (Python 3.13, with hashes)
 entries/rich-2014/reproduce_rich_2014.ipynb | 66 ++++++++++++++++++++++-------
 1 file changed, 50 insertions(+), 16 deletions(-)
Installed kernelspec registry-rich-2014 in executed/rich-2014/.venv/share/jupyter/kernels/registry-rich-2014
0 error(s)
pass  reproduce_rich_2014.ipynb  (213 s)

real	3m44.631s
user	3m36.750s
sys	0m5.030s
Thu Nov 12 01:16:05 UTC 2026
```

**Agent**

The full run passed in 213 s. Reading the outputs for the two claims:

**Agent calls Bash**

```bash
cd  ls executed/rich-2014; python - <<'E'
import json
nb=json.load(open('executed/rich-2014/reproduce_rich_2014.ipynb'))
for c in nb['cells']:
    t=c.get('metadata',{}).get('tags',[])
    if any(x in ('claim:fig4b-single-field-proportion','claim:fig4c-active-subsets','claim:fig3b-negbin-fit') for x in t):
        for o in c.get('outputs',[]):
            if 'text' in o: print(''.join(o['text']))
E
```

```
reproduce_rich_2014.ipynb
result.json
F-a/P-a: r 0.5592 (expected 0.57 +/- 0.057), p 0.1517 (expected 0.14 +/- 0.014), mean r(1-p)/p 3.126, observed mean 3.126, n 253
F-a/P-b: r 0.5548 (expected 0.57 +/- 0.057), p 0.1504 (expected 0.14 +/- 0.014), mean r(1-p)/p 3.134, observed mean 3.134, n 253
F-b: r 0.5653 (expected 0.57 +/- 0.057), p 0.1388 (expected 0.14 +/- 0.014), mean r(1-p)/p 3.506, observed mean 3.506, n 253
F-a/P-a fields 0..12, observed: [94, 31, 25, 19, 18, 9, 15, 4, 10, 4, 8, 3, 5]
     negative binomial: [88.1, 41.8, 27.6, 20.0, 15.1, 11.7, 9.2, 7.3, 5.8, 4.7, 3.8, 3.1, 2.5]
     equal-rate Poisson: [11.1, 34.7, 54.2, 56.5, 44.2, 27.6, 14.4, 6.4, 2.5, 0.9, 0.3, 0.1, 0.0]
F-a/P-b fields 0..12, observed: [94, 33, 24, 14, 22, 10, 9, 10, 8, 9, 4, 3, 6]
     negative binomial: [88.4, 41.7, 27.5, 19.9, 15.0, 11.6, 9.2, 7.3, 5.8, 4.7, 3.8, 3.1, 2.6]
     equal-rate Poisson: [11.0, 34.5, 54.1, 56.5, 44.3, 27.8, 14.5, 6.5, 2.5, 0.9, 0.3, 0.1, 0.0]
F-b fields 0..12, observed: [88, 33, 24, 14, 17, 16, 11, 8, 10, 5, 4, 7, 5]
     negative binomial: [82.9, 40.3, 27.2, 20.0, 15.4, 12.1, 9.7, 7.8, 6.3, 5.2, 4.3, 3.5, 2.9]
     equal-rate Poisson: [7.6, 26.6, 46.7, 54.5, 47.8, 33.5, 19.6, 9.8, 4.3, 1.7, 0.6, 0.2, 0.1]

x axis 0 to 24 fields; cells beyond: {'F-a/P-a': 0, 'F-a/P-b': 0, 'F-b': 2}

printed parameters X-a: 117.5 to 649.4 m, factor 5.53, less 10% 4.97 (claims file 5.0)
printed parameters X-b: 171.8 to 745.6 m, factor 4.34, less 10% 3.91 (claims file 3.9)
F-a/P-a X-a: at 48 m 16.5%; widest interval inside 4.5-11%: 132.6 to 749.9 m, factor 5.66 (needed 5.0, met True), proportion there 4.51 to 10.97%; over 0.1 m to 10 km from 0.64 to 20.21%
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 128,136p paper/10.1126-science.1255635.txt; sed -n 284,292p paper/10.1126-science.1255635.txt; grep -n "Fig. 3C\|Fig. 3.\s" paper/10.1126-science.1255635.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 334,345p paper/10.1126-science.1255635.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/rich-2014; cat > $TMPDIR/edit2.py <<'E'
import json
P='reproduce_rich_2014.ipynb'
nb=json.load(open(P)); C=nb['cells']
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
setsrc(90,'''**Result: reproduced.** With the P-a fit the proportion stays inside 4.5 to 11% from 133 to 750 m under X-a, a factor of 5.66 in size, above the 5.0 that the printed parameters less 10% set (they give 5.53); X-b gives 195 to 866 m, a factor of 4.44, above 3.9. P-b gives 5.75 and 4.49. At 48 m the proportion is 16.5% (X-a), above the 5 to 10% band, so the band holds for environments of roughly 130 to 750 m, not for the track itself. The data set's fields give factors of 5.59 and 4.39. The criterion was amended after a reader's answer (questions/rich-2014.yaml); under the earlier factor of 10 the outcome was not reproduced.''')
setsrc(93,'''**Result: not reproduced, resting on the assumption of logarithmic spacing (G-a).** The readings disagree. With logarithmic sizes the share of pairs of different environments with an exclusive-OR proportion above the level is lower for the gamma-Poisson model than for the fitted equal-rate model, 0.825 against 0.834 (K-a, 0.1) and 0.662 against 0.701 (K-b, 0.2), under the P-a fit; with linear sizes it is higher, 0.999 against 0.980 and 0.948 against 0.830. P-b and the data set's fields give the same signs, and over 10 further seeds the difference stays negative under G-a (-0.054 to -0.006) and positive under G-b (0.018 to 0.156). Logarithmic spacing is assumed, as the sizes span 0.1 to 50 m, nearly three orders of magnitude, and the paper describes recruitment "over spatial scales spanning several orders of magnitude". Reported, not judged: the expected share of cells active at 50 m is 0.669 for the gamma-Poisson and 0.961 for the fitted equal rate; the mean exclusive-OR proportion over pairs both larger than 10 m is 0.269 against 0.371 (G-a); with twice the fitted rate it is 0.153, and 0.043 between environments over 20 m, near zero as the Fig. S18 legend says of its high rate.''')
s=''.join(C[103]['source'])
s=s.replace('| fig4b-single-field-proportion | not reproduced |','| fig4b-single-field-proportion | reproduced |')
s=s.replace('| fig4c-active-subsets | not reproduced |','| fig4c-active-subsets | not reproduced (assumption G-a) |')
old='be reproduced. The track'
assert old in s
s=s.replace(old,'be reproduced. For fig4c-active-subsets the spacing of the 300 simulated environment sizes is\nopen; logarithmic spacing is assumed, and under linear spacing that claim would be reproduced. The track')
setsrc(103,s)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
r=open('README.md').read()
r=r.replace('| 5 to 10% single-field cells over a wide range of sizes (Fig. 4B) | Not reproduced |','| 5 to 10% single-field cells over a wide range of sizes (Fig. 4B) | Reproduced |')
r=r.replace('| Active subsets distinguish environments (Fig. 4C) | Not reproduced |','| Active subsets distinguish environments (Fig. 4C) | Not reproduced (assumption) |')
old='''leaves open; under the other reading those four claims would be reproduced.'''
assert old in r
r=r.replace(old,'''leaves open; under the other reading those four claims would be reproduced. For Fig. 4C it marks
the assumption that the simulated environment sizes are spaced logarithmically; with linear spacing
that claim would be reproduced.''')
open('README.md','w').write(r)
E
python $TMPDIR/edit2.py && git diff --stat .
```

```
entries/rich-2014/README.md                 |  8 +--
 entries/rich-2014/reproduce_rich_2014.ipynb | 75 +++++++++++++++++++++--------
 2 files changed, 60 insertions(+), 23 deletions(-)
```

**Agent**

Now the attempt record.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/rich-2014-01.yaml",
 "old_string": "  outcome: not_reproduced\n  notebook: reproduce_rich_2014.ipynb\n  output: claim:fig4b-single-field-proportion\n  measured:\n  - 4.51\n  - 10.97\n  notes: With the P-a fit under X-a the single-field proportion stays inside 4.5 to 11% from 133 to 750 m\n    (a factor of 5.7 in size; 4.51 to 10.97% there) and is 16.5% at 48 m; X-b gives 195 to 866 m (factor\n    4.4). The criterion asks for a factor of 10. The printed parameters give factors of 5.5 and 4.3, so\n    the paper's own fit would not meet the criterion either. The factor of 10 is asked of a reader\n    (questions/rich-2014.yaml).",
 "new_string": "  outcome: reproduced\n  notebook: reproduce_rich_2014.ipynb\n  output: claim:fig4b-single-field-proportion\n  measured:\n  - 4.51\n  - 10.97\n  notes: With the P-a fit under X-a the single-field proportion stays inside 4.5 to 11% from 133 to 750 m,\n    a factor of 5.66 in size (4.51 to 10.97% there), above the 5.0 the criterion asks; X-b gives 195 to\n    866 m, a factor of 4.44, above 3.9. P-b gives 5.75 and 4.49, the data set's fields 5.59 and 4.39, and\n    the printed parameters 5.53 and 4.34. At 48 m the proportion is 16.5% (X-a), so the band holds for\n    environments of about 130 to 750 m, not for the track itself. What the answer changed. The question\n    (questions/rich-2014.yaml) asked whether the criterion's factor of 10 came from the paper; the reader\n    found it did not and amended the criterion to the width the printed parameters give, less 10% (5.0\n    under X-a, 3.9 under X-b). The analysis is unchanged; under the earlier factor of 10 the outcome was\n    not reproduced, and under the amended one it is reproduced."
}
```

```
The file attempts/rich-2014-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/rich-2014-01.yaml",
 "old_string": "  outcome: not_reproduced\n  notebook: reproduce_rich_2014.ipynb\n  output: claim:fig4c-active-subsets\n  notes: For pairs of environments both larger than 10 m, the mean proportion of cells in different\n    states is 0.269 (logarithmic sizes) and 0.251 (linear) for the gamma-Poisson model against 0.371 and\n    0.301 for the fitted equal-rate model (P-a fit), so the criterion fails under both spacings. With\n    twice the fitted rate the equal-rate value is 0.153 and 0.098, and 0.043 and 0.036 for pairs over 20\n    m, consistent with the Fig. S18 legend's near-zero high-rate condition. With half the rate it is\n    0.499 and 0.482. The comparison the criterion uses is asked of a reader (questions/rich-2014.yaml).\n  deviations:\n  - The equal-rate model uses the observed mean count per cell (3.126 per 48 m under P-a); the half and\n    twice variants are those the criterion names, as Fig. S18's rates are not given.",
 "new_string": "  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_rich_2014.ipynb\n  output: claim:fig4c-active-subsets\n  notes: The share of all pairs of different environments with an exclusive-OR proportion above the\n    level, gamma-Poisson against the fitted equal rate (P-a fit), is 0.825 against 0.834 (K-a, 0.1) and\n    0.662 against 0.701 (K-b, 0.2) with logarithmic sizes (G-a), lower under both levels, and 0.999\n    against 0.980 and 0.948 against 0.830 with linear sizes (G-b), higher under both. P-b and the data\n    set's fields give the same signs, and over 10 further seeds the difference stays within -0.054 to\n    -0.006 under G-a and 0.018 to 0.156 under G-b. The readings disagree, so G-a is assumed (see\n    deviations) and the outcome under it is not reproduced; under G-b it would be reproduced. Reported,\n    not judged. The expected share of cells active at 50 m is 0.669 (gamma-Poisson) and 0.961 (fitted\n    equal rate). The mean exclusive-OR proportion over pairs both larger than 10 m is 0.269 against\n    0.371 (G-a) and 0.251 against 0.301 (G-b). With twice the fitted rate it is 0.153 and 0.098, and 0.043\n    and 0.036 for pairs over 20 m, near zero as the Fig. S18 legend says of its high rate; the share above\n    0.2 is then 0.781 (G-a) and 0.458 (G-b). What the answer changed. The question\n    (questions/rich-2014.yaml) asked whether the mean over pairs larger than 10 m against the fitted equal\n    rate was a reading of Fig. 4C. The reader kept the fitted equal rate as the comparison and replaced\n    the measure with the share of pairs above a level (K-a 0.1, K-b 0.2) under both spacings. Under the\n    earlier criterion the outcome was not reproduced under both spacings; under the amended one the\n    spacings disagree, and the outcome, not reproduced, now rests on the assumed spacing. The spacing of\n    the sizes is a question for the paper's authors (see findings).\n  deviations:\n  - The equal-rate model uses the observed mean count per cell (3.126 per 48 m under P-a); the half and\n    twice variants are those the criterion names, as Fig. S18's rates are not given.\n  - Assumed logarithmic spacing (G-a) of the 300 environment sizes, as G-a and G-b give different\n    outcomes. The Methods give only \"300 independent environments ranging in size from 0.1 m to 50 m\"\n    (Active subset simulation). The range spans nearly three orders of magnitude, its lower end 0.1 m is\n    the natural start of a logarithmic grid, the main text describes recruitment \"over spatial scales\n    spanning several orders of magnitude\" (page 816, on Fig. 3C), and the Fig. S18 legend compares\n    conditions on \"small environments\", of which a linear grid holds few (6 of 300 below 1 m).\n  - The levels K-a 0.1 and K-b 0.2 are the criterion's standard choices; the same sign holds at both\n    under each spacing."
}
```

```
The file attempts/rich-2014-01.yaml has been updated successfully.
```

**Agent**

The "6 of 300 below 1 m" figure isn't printed in the notebook yet, so I'll add it. I'm also dropping a page number I didn't check.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
P='entries/rich-2014/reproduce_rich_2014.ipynb'
nb=json.load(open(P)); src=nb['cells'][92]['source']
i=[j for j,l in enumerate(src) if l.startswith('s4c = pd.DataFrame(rows)')][0]
src.insert(i,'print("sizes below 1 m:", {G: int(np.sum(SPACING[G]() < 1)) for G in SPACING}, "of 300")\n')
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
a=open('attempts/rich-2014-01.yaml').read()
a=a.replace('spanning several orders of magnitude" (page 816, on Fig. 3C)','spanning several orders of magnitude" (main text, on Fig. 3C)')
a=a.replace('''conditions on "small environments", of which a linear grid holds few (6 of 300 below 1 m).''','''conditions on "small environments", of which a linear grid holds few (6 of 300 below 1 m, against 139
    for G-a).''')
old='''    corners at 45 and 90 degrees of a reconstructed centreline, which give the same result.\n'''
assert old in a
a=a.replace(old, old+'''- kind: methods_unavailable
  statement: Question for the paper's authors. How were the 300 environment sizes from 0.1 to 50 m of
    the active subset simulation (Fig. 4C, Methods, Active subset simulation) spaced, logarithmically or
    linearly, and what proportion of cells counts as distinguishing two environments? With the fitted
    parameters the gamma-Poisson model distinguishes a larger share of pairs than the fitted equal rate
    with linear spacing (0.948 against 0.830 above 0.2) and a smaller one with logarithmic spacing (0.662
    against 0.701), so the outcome of fig4c-active-subsets rests on the spacing; logarithmic spacing was
    assumed.
''')
open('attempts/rich-2014-01.yaml','w').write(a)
E
python -c "import numpy" 2>/dev/null; $TMPDIR/pv/bin/python -c "
import numpy as np; print(np.sum(np.logspace(-1,np.log10(50),300)<1), np.sum(np.linspace(.1,50,300)<1))"
```

```
111 6
```

**Agent**

The G-a count is 111, not the 139 I wrote; correcting it.

**Agent calls Bash**

```bash
cd  sed -i 's/(6 of 300 below 1 m, against 139$/(6 of 300 below 1 m, against 111/' attempts/rich-2014-01.yaml; grep -n "against 111" attempts/rich-2014-01.yaml; python -c "import yaml;yaml.safe_load(open('attempts/rich-2014-01.yaml'))" && echo ok; grep -rn "rich-2014-01\|attempt record\|outcomes" questions/rich-2014.yaml | head -3
```

```
337:    conditions on "small environments", of which a linear grid holds few (6 of 300 below 1 m, against 111
ok
1:# Questions from attempt rich-2014-01 (author, 2026-11-12) about the claims file
3:# as the file has it and shows the other reading as a variant; the outcomes stay as tested.
```

**Agent**

Re-running lock and the full entry with the final notebook:

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py lock entries/rich-2014 2>&1 | tail -1; python tools/entry.py all entries/rich-2014 2>&1 | tail -4; date -u
```

```
Thu Nov 12 01:17:50 UTC 2026
wrote rich-2014/requirements.lock.txt (Python 3.13, with hashes)
Installed kernelspec registry-rich-2014 in executed/rich-2014/.venv/share/jupyter/kernels/registry-rich-2014
0 error(s)
pass  reproduce_rich_2014.ipynb  (210 s)
Thu Nov 12 01:21:29 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/rich-2014/reproduce_rich_2014.ipynb'))
for c in nb['cells']:
    t=c.get('metadata',{}).get('tags',[])
    if any(x in ('claim:fig4b-single-field-proportion','claim:fig4c-active-subsets') for x in t):
        for o in c.get('outputs',[]):
            if 'text' in o: print(''.join(o['text']))
E
python tools/entry.py check entries/rich-2014 2>&1 | tail -3; python tools/entry.py handover entries/rich-2014 2>&1 | tail -3; git status --short
```

```
printed parameters X-a: 117.5 to 649.4 m, factor 5.53, less 10% 4.97 (claims file 5.0)
printed parameters X-b: 171.8 to 745.6 m, factor 4.34, less 10% 3.91 (claims file 3.9)
F-a/P-a X-a: at 48 m 16.5%; widest interval inside 4.5-11%: 132.6 to 749.9 m, factor 5.66 (needed 5.0, met True), proportion there 4.51 to 10.97%; over 0.1 m to 10 km from 0.64 to 20.21%
F-a/P-a X-b: at 48 m 25.4%; widest interval inside 4.5-11%: 195.0 to 866.0 m, factor 4.44 (needed 3.9, met True), proportion there 4.51 to 10.99%; over 0.1 m to 10 km from 1.10 to 99.10%
F-a/P-b X-a: at 48 m 16.5%; widest interval inside 4.5-11%: 131.8 to 758.6 m, factor 5.75 (needed 5.0, met True), proportion there 4.51 to 11.00%; over 0.1 m to 10 km from 0.64 to 20.15%
F-a/P-b X-b: at 48 m 25.3%; widest interval inside 4.5-11%: 196.1 to 881.0 m, factor 4.49 (needed 3.9, met True), proportion there 4.50 to 10.98%; over 0.1 m to 10 km from 1.12 to 99.09%
F-b X-a: at 48 m 15.9%; widest interval inside 4.5-11%: 117.5 to 656.9 m, factor 5.59 (needed 5.0, met True), proportion there 4.51 to 10.99%; over 0.1 m to 10 km from 0.72 to 20.31%
F-b X-b: at 48 m 23.7%; widest interval inside 4.5-11%: 172.8 to 758.6 m, factor 4.39 (needed 3.9, met True), proportion there 4.50 to 10.97%; over 0.1 m to 10 km from 1.00 to 99.00%

F-a/P-a G-a: reported, not judged: mean XOR over pairs both > 10 m: gamma-Poisson 0.269, equal-rate 0.371, half rate 0.499, twice rate 0.153; pairs both > 20 m, twice rate 0.043
F-a/P-a G-b: reported, not judged: mean XOR over pairs both > 10 m: gamma-Poisson 0.251, equal-rate 0.301, half rate 0.482, twice rate 0.098; pairs both > 20 m, twice rate 0.036

F-a/P-b G-a: reported, not judged: mean XOR over pairs both > 10 m: gamma-Poisson 0.266, equal-rate 0.371, half rate 0.498, twice rate 0.150; pairs both > 20 m, twice rate 0.043

F-a/P-b G-b: reported, not judged: mean XOR over pairs both > 10 m: gamma-Poisson 0.251, equal-rate 0.299, half rate 0.482, twice rate 0.097; pairs both > 20 m, twice rate 0.0
[... 50 more lines not kept]
```

**Agent**

The executed numbers match the conclusions and the record. The check reports 0 errors and the handover is built. One last check that the committed notebook carries no outputs:

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/rich-2014/reproduce_rich_2014.ipynb'));print(sum(len(c.get('outputs',[])) for c in nb['cells']))"; grep -c "—" attempts/rich-2014-01.yaml entries/rich-2014/README.md; date -u
```

```
0
attempts/rich-2014-01.yaml:0
entries/rich-2014/README.md:0
Thu Nov 12 01:22:02 UTC 2026
```

**Agent**

Both answered questions changed their claims. After the re-run, fig4b-single-field-proportion goes from not reproduced to reproduced. fig4c-active-subsets stays not reproduced, but the outcome now rests on an assumption I made about how the simulated environment sizes were spaced. With the other spacing it would be reproduced.

The entry is locked, `entry.py all` passes (notebook runs in 210 s, 0 errors), `check` reports 0 errors, and the handover is in `executed/rich-2014/handover/`. I did not verify my own work, and nothing is committed or pushed.

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| fig4b-single-field-proportion | not reproduced | reproduced |
| fig4c-active-subsets | not reproduced | not reproduced, `assumed: true` (logarithmic spacing) |

**Question 1, fig4b-single-field-proportion.** The criterion required the 5 to 10% band (widened to 4.5 to 11%) to hold over sizes spanning a factor of 10, which is not in the paper.
- **What the answer changed:** the reader agreed and amended the criterion. The required width is now what the paper's printed parameters give, less 10%: a factor of 5.0 when the proportion is of all cells (X-a), 3.9 when it is of place cells only (X-b).
- **Result:** the analysis is unchanged. With the main fit, the proportion stays in the band from 133 to 750 m under X-a, a factor of 5.66, and from 195 to 866 m under X-b, a factor of 4.44. Both pass.
- **Other readings:** the other definition of a "pass" through a field gives 5.75 and 4.49. The dataset's own fields give 5.59 and 4.39, and the printed parameters 5.53 and 4.34.
- **Caveat:** at the 48 m track itself the proportion is 16.5%, so the band holds for environments of roughly 130 to 750 m, not for the track.

**Question 2, fig4c-active-subsets.** The criterion compared the mean share of cells that tell two environments apart, over pairs both larger than 10 m, against the fitted equal-rate model.
- **What the answer changed:** the fitted equal-rate comparison stays. The measure is now the share of all pairs of environments in which more than a given fraction of cells tell them apart, at 0.1 (K-a) and 0.2 (K-b), under both log and linear spacing of the 300 sizes. The old mean is reported but not judged.
- **Result:** the spacings disagree, consistently across both fits, the dataset's fields, and 10 further seeds.

  | Spacing | Threshold | Gamma-Poisson | Equal rate |
  |---|---|---|---|
  | Log | 0.1 | 0.825 | 0.834 |
  | Log | 0.2 | 0.662 | 0.701 |
  | Linear | 0.1 | 0.999 | 0.980 |
  | Linear | 0.2 | 0.948 | 0.830 |

  The gamma-Poisson model is lower under log spacing and higher under linear.
- **Why log spacing:** following Author step 1.6, I assumed log spacing. The sizes run from 0.1 to 50 m, nearly three orders of magnitude. The paper describes recruitment "over spatial scales spanning several orders of magnitude", and the Fig. S18 legend discusses "small environments". A linear grid has only 6 of 300 sizes below 1 m, against 111 for log.
- **Recorded:** the assumption is a deviation in the record, and a new `methods_unavailable` finding asks the paper's authors how the sizes were spaced and what threshold they used.
- **Reported, not judged:** at 50 m the gamma-Poisson model has recruited 0.669 of cells and the equal-rate model 0.961. At twice the fitted rate, the share of cells telling apart environments over 20 m is 0.043, close to zero as the Fig. S18 legend says.

Each claim's notes in `attempts/rich-2014-01.yaml` say what the answer changed. I also updated the notebook's code, conclusions and summary for both claims, and the README rows. The `tools/` files were already modified before this run, and I left them alone.

## End of run

32 turns, 12 minutes, $1.31 at API prices, result: success.
