# hiraoka-2025 · author-revise-2 · run 44986625428

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/hiraoka-2025/verifier-2-report.md; ls entries/hiraoka-2025 entries/hiraoka-2025/*; wc -l docs/protocol.md
```

```
Sun Nov 22 04:54:56 UTC 2026
**Verifier report, round 2: hiraoka-2025-01 (doi:10.1063/5.0296506, DANDI:000044 0.210812.1516)**

**1. Outcomes**

The claims file has 14 claims and the attempt record has 14 outcomes: 12 tested, 2 blocked. Cell indices below are main = `reproduce_hiraoka_2025.ipynb`, on = `other_neurons.ipynb`, cap3 = `other_neurons_cap3.ipynb`, model = `model.ipynb`.

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| fig2-neuron-representative-sequence | reproduced | yes | main 9 |
| fig2-iet-broad | reproduced | yes | main 12 |
| fig2-neuron-burst-size-heavy-tail | reproduced | yes | 8/8 and 40/40 under both KS fits, capped or not (main 18) |
| fig2-neuron-beta-stable | not_reproduced | yes | Range 1.079; capped KS ranges 0.552–0.705 (main 21) |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | yes | Part (2) rests on 6 points at p = 0.0416 (main 33), and the record says so |
| fig2-neuron-merging-heavy-tail | reproduced | yes, now | My round-1 objection is answered. Without the cap, ks_discrete IQR is 0.378 and 0.415, with 13/15 and 70/76 supported (main 24). |
| fig2-neuron-merging-collapse | not_reproduced, `assumed: true` | yes, with a caveat | The assumption (unbounded exponent) is stated and is methodologically reasonable. The result is knife-edge: 0.538 unbounded against 0.490 capped, band 0.5 (main 27). O3(a) says "the powerlaw package's default", and the locked 2.0.0 default is the capped fit, so a literal O3 reading would give reproduced. The outcome is best read as undetermined between the two. |
| fig2-exponents-above-two | reproduced | yes | main 30 |
| fig2-other-neurons-similar | reproduced | yes, under the one-reading rule; fragile | Passes only under x1_continuous (0.883–0.906, on 5). That reading also passes for inhibitory (0.781–0.836) and all units (0.872–0.893), so the pass does not depend on the pyramidal restriction or on the cap (cap3 5). |
| fig2-wikipedia-beta | blocked (too_large) | blocked, yes | The record an
[... 62 more lines not kept]
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
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,240p docs/protocol.md; sed -n 490,640p docs/protocol.md; sed -n 726,779p docs/protocol.md
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

[... 228 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep hiraoka; ls questions | grep hiraoka; wc -l attempts/hiraoka-2025-01.yaml; cat questions/hiraoka-2025.yaml
```

```
hiraoka-2025-01.yaml
hiraoka-2025.yaml
502 attempts/hiraoka-2025-01.yaml
questions:
- claim: fig2-other-neurons-similar
  question: The criterion reads the set of other neurons as the pyramidal units, of session
    Achilles-10252013 or of every session. The paper's own representative unit (unit 9 of
    Achilles-10252013, found by its spike count and IETs as row 9 of the units table) is labelled
    inhibitory in the version the paper cites and interneuron in the latest. Since the paper's
    "other sequences in the datasets" are compared with a unit the files call inhibitory, should
    the set be all units of the recordings, or include the inhibitory units, and not the
    pyramidal units alone?
  passage: Section III, paragraphs 2 and 5. "The first dataset consists of neuronal firing
    obtained from electrophysiological recordings of pyramidal cell activity in rat
    hippocampus" and "we show the results for a representative event sequence for each dataset
    ... unit 9 in the Achilles-10252013 session ... Other sequences in the datasets show similar
    patterns."
  why: The paper calls all its neuronal data pyramidal, but the unit it shows is not labelled so,
    which suggests it analysed every unit without the cell types. The fraction of units showing
    the pattern differs by class. With the exponent unbounded, under the KS fits it is 0.68 to
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/hiraoka-2025-01.yaml
```

```
<persisted-output>
Output too large (34.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/34b76c27-aae0-447f-99b3-996d602b1aab/tool-results/bs0nsx5gv.txt

Preview (first 2KB):
schema_version: 3
id: hiraoka-2025-01
datasets:
- archive: dandi
  id: '000044'
  version: 0.210812.1516
  doi: 10.48324/dandi.000044/0.210812.1516
  relation: reuses
paper: doi:10.1063/5.0296506
date: 2026-11-21
entry: hiraoka-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/hiraoka-2025-01.yaml"
}
```

```
1	schema_version: 3
2	id: hiraoka-2025-01
3	datasets:
4	- archive: dandi
5	  id: '000044'
6	  version: 0.210812.1516
7	  doi: 10.48324/dandi.000044/0.210812.1516
8	  relation: reuses
9	paper: doi:10.1063/5.0296506
10	date: 2026-11-21
11	entry: hiraoka-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 483 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | grep hiraoka; grep -n -i -B2 -A12 "O3\b\|^  - id: O3\|default" claims/hiraoka-2025.yaml | head -120
```

```
hiraoka-2025.yaml
52-#   periods and the maze), so the reading taken is all spikes of the session. The epochs taken
53-#   separately are a variant.
54:# - O3, the fit. The paper fixes neither the lower cutoff xmin nor whether the data are treated
55:#   as discrete. The readings are (a) the powerlaw package's default, with xmin chosen by
56-#   minimizing the Kolmogorov-Smirnov distance (Clauset et al.), (b) xmin = 1, each with
57:#   discrete = True and with the package's default continuous fit. A claim on an exponent is
58-#   reproduced if it holds under one of these readings, and all of them are shown. The
59-#   likelihood ratio test is powerlaw's distribution_compare('power_law', 'exponential'). A
60-#   power law is supported when R > 0 and p < 0.05.
61-# - O4, the grid of delta. The paper does not give it. The Figure 2 legend says the values of
62-#   delta and delta' shown "span the entire range of relevant timescales", so for the neuron
63-#   that range is about 55 to 6300 ms. The delta' labels (55, 100, 180, 330, 590 ms) step by
64-#   about 1.82, but the burst-size labels (55, 140, 370, 940, 2400, 6300 ms) step by about 2.55,
65-#   which is not a whole power of 1.82. The grid is therefore finer than the labels, and its
66-#   density can change the criteria that count timescales or pairs ("more than half", "at
67-#   least three grid points"). Two readings are run. (a) A geometric grid of ratio 1.82 from
68-#   the lower end of the relevant range. (b) A geometric grid with log10 step about 0.052 (one
69-#   fifth of that ratio, which holds both sets of labels). The pairs keep the ratios 3.3, 5.9
--
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A22 "id: fig4-model-heavy-tails\|id: fig4-model-iet-shapes\|id: model-decremental-equivalent" claims/hiraoka-2025.yaml | grep -v "^--$" | head -90
```

```
262:- id: fig4-model-heavy-tails
263-  statement: Event sequences generated by the incremental dynamic algorithm, with linear,
264-    quadratic or exponential timescale series, show heavy-tailed burst-size and merging-number
265-    distributions over a wide range of timescales, with stable exponents.
266-  source: Section IV, paragraphs 9 and 10; Figure 4
267-  quote: For all of the three timescale series, the generated ... show heavy-tailed distributions
268-    of burst sizes b for a wide range of timescales δ ... numbers k are also heavy-tailed across
269-    different pairs of timescales δ and δ′, even though these timescales do not coincide with the
270-    preset series of timescales δl ... the power-law exponent values of the heavy tails in Pδ(b)
271-    and Pδδ′(k) are stable across timescales
272-  data: elsewhere
273-  where: Not deposited; generated by the paper's Algorithm 2 (Section IV), for which no code is
274-    linked
275-  criterion: Not testable on the dandiset. Algorithm 2 is run with n = 10^6, a zeta merging
276-    distribution with gamma = 2.5 (memory function of Eq. 16), delta_0 = 1 and uniform IETs
277-    (Eq. 10). The timescales are linear with w = 100, quadratic with w = 100, or exponential
278-    with w = 2 (Section IV). Bursts, the fit and the test are as for Figure 2. The pairs are
279-    those of the Figure 4 legends, delta = 1.8, 2.4 and 3.3 delta' (linear), 3.3, 5.9 and 11
280-    delta' (quadratic), and 5.3, 12 and 28 delta' (exponential). Reproduced when, for each
281-    series, the power law is supported (R > 0, p < 0.05) at more than half of the relevant
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/hiraoka-2025/README.md; cat entries/hiraoka-2025/entry.yaml; python tools/entry.py --help 2>&1 | head -30; ls executed/hiraoka-2025 2>/dev/null
```

```
# Hiraoka and Jo (2025) on DANDI:000044

Tests the findings of T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in
event sequences" (doi:10.1063/5.0296506), on dandiset 000044 version 0.210812.1516, the version the
paper cites: the hippocampal recordings of Grosmark and Buzsaki (2016). The claims are in
`claims/hiraoka-2025.yaml` and the record in `attempts/hiraoka-2025-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

- `reproduce_hiraoka_2025.ipynb`: the data check, the paper's representative unit (row 9 of
  session Achilles-10252013), and its bursty trains, merging numbers and power-law fits (Figure 2).
- `other_neurons.ipynb`: the same pattern in every unit of the eight sessions, pyramidal and
  inhibitory (about 45 minutes on 4 processes).
- `other_neurons_cap3.ipynb`: the same test with the power-law exponent capped at 3, the default
  of the locked powerlaw 2.0.0, as a variant (about 11 minutes on 4 processes).
- `model.ipynb`: the paper's two generative algorithms (Section IV, Figure 4), simulated here.
- `bursttree.py`: loading, bursts, merging numbers, fits and the algorithms, with the source of
  each parameter.

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python -c "
import json
nb=json.load(open('reproduce_hiraoka_2025.ipynb'))
for i in [14,15,38]:
    c=nb['cells'][i]; print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags')); print(''.join(c['source']))
"; python -c "
import json
nb=json.load(open('../../executed/hiraoka-2025/reproduce_hiraoka_2025.ipynb'))
c=nb['cells'][15]
for o in c.get('outputs',[]): print(''.join(o.get('text','')))
"
```

```
=== cell 14 markdown None
## Bursts and merging numbers of the representative unit

Relevant timescales, grids, bursts and fits as in the Methods and in O3 and O4 of the claims
file (the helper says where each detail comes from). Both grids are run under the four fit
readings, each with the exponent unbounded (adopted) and capped at 3 (suffix `_cap3`, the default of
the locked powerlaw 2.0.0; helper, `READINGS`). The pairs of Figure 2 (delta' = 55, 100, 180, 330, 590 ms; delta = 3.3, 5.9 and 11
delta') are added as fixed pairs for fig2-neuron-merging-collapse.
=== cell 15 code None
FIG2_PAIRS = [(dp, r * dp, r) for dp in (55, 100, 180, 330, 590) for r in bt.NEURON_RATIOS]
t1 = time.time()
RES = {g: bt.analyse_sequence(spk, g, extra_pairs=FIG2_PAIRS if g == "b" else ()) for g in bt.GRIDS}
print(f"fits done in {time.time() - t1:.0f} s")
lo, hi = RES["a"]["lo"], RES["a"]["hi"]
print(f"relevant timescales: {lo:.2f} ms (smallest delta with a burst of >= 100 events) to {hi:.2f} ms (the 99th largest IET; delta must stay below it for >= 100 bursts)")
print(f"paper (Figure 2 labels): about 55 to 6300 ms")
for g in bt.GRIDS:
    print(f"grid ({g}): {len(RES[g]['grid'])} points, step log10 {np.log10(RES[g]['grid'][1] / RES[g]['grid'][0]):.4f}:", RES[g]["grid"].round(1))
B = pd.concat([pd.DataFrame(RES[g]["bursts"]).assign(grid=g) for g in bt.GRIDS], ignore_index=True)
P = pd.concat([pd.DataFrame(RES[g]["pairs"]).assign(grid=g) for g in bt.GRIDS], ignore_index=True)
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; grep -n "def make_grid\|def grid\|GRIDS\|0.052\|n_steps\|hi)" bursttree.py | head -30
```

```
/bin/bash: line 1: cd: entries/hiraoka-2025: No such file or directory
36:# Claims file, O4: grid (a) geometric with ratio 1.82, grid (b) log10 step 0.052,
38:GRIDS = {"a": np.log10(1.82), "b": 0.052}
150:    return float(lo), float(hi)
153:def grid(lo: float, hi: float, grid_name: str) -> np.ndarray:
156:    Grid (a): ratio 1.82 from the lower end. Grid (b): log10 step "about 0.052" (O4), made
167:    step = GRIDS[grid_name]
395:def unit_all_patterns(times_ms, readings=ADOPTED_READINGS, grids=tuple(GRIDS)) -> list[dict]:
```

**Agent calls Read**

```json
{
 "file_path": "entries/hiraoka-2025/bursttree.py",
 "offset": 125,
 "limit": 60
}
```

```
125	    """Merging numbers k_j: bursts at delta' that make up the j-th burst at delta (Eqs. 2-3).
126	
127	    Within a burst at delta, every IET in (delta', delta] separates two bursts at delta', so
128	    k_j = 1 + the number of such IETs inside burst j.
129	    """
130	    assert dprime < delta
131	    burst_of_iet = np.r_[0, np.cumsum(tau > delta)][:-1]
132	    inside = tau <= delta
133	    m = int((tau > delta).sum()) + 1
134	    k = 1 + np.bincount(burst_of_iet[inside], weights=(tau[inside] > dprime), minlength=m)
135	    return k.astype(np.int64)
136	
137	
138	def relevant_range(tau: np.ndarray) -> tuple[float, float]:
139	    """Relevant timescales (Methods), computed exactly from the IETs.
140	
141	    Lower end: the smallest delta with max burst size >= 100, the smallest over all runs of
142	    100 consecutive events of their largest IET. Upper end: delta must stay below the 99th
143	    largest IET for m_delta >= 100; the returned bound is that IET (exclusive).
144	    """
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python -c "
import json
nb=json.load(open('reproduce_hiraoka_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'spk =' in s or 'tau =' in s or 'spk=' in s: print('=== cell',i); print(s[:1500])
"; grep -n "def analyse_sequence" -A25 bursttree.py | head -40
```

```
=== cell 9
U = units["Achilles-10252013"]
def stats(i):
    s = U["spikes"][i] * 1e3; d = np.diff(s)
    return dict(row=i, id=int(U["id"][i]), cell_type=U["cell_type"][i], shank_id=int(U["shank_id"][i]), n=len(s),
                tau_min_ms=round(d.min(), 3), tau_max_ms=round(d.max(), 1),
                match=bool(abs(len(s) - 228356) <= 22835.6 and abs(d.min() - 1.05) <= 0.105 and abs(d.max() - 18200) <= 1820))
o1 = []
o1 += [dict(reading="(a) id 9", **stats(i)) for i in np.flatnonzero(U["id"] == 9)]
o1 += [dict(reading="(b) row 9 from 0", **stats(9))]
o1 += [dict(reading="(c) ninth from 1", **stats(8))]
o1 += [dict(reading="(d) shank_id 9", **stats(i)) for i in np.flatnonzero(U["shank_id"] == 9)]
o1 = pd.DataFrame(o1); print(o1.to_string())
REP = 9
print("units in the session matching all three values:", [int(U["id"][i]) for i in range(len(U["id"])) if stats(i)["match"]])
# the same row in the latest version
print("latest version, row 9:", dict(id=int(UL["id"][9]), cell_type=UL["cell_type"][9], n=len(UL["spikes"][9])),
      "; ids equal to 9 in latest:", int((UL["id"] == 9).sum()))
spk = U["spikes"][REP] * 1e3
tau = bt.iets(spk)
[... 27 more lines not kept]
```

**Agent**

Now I'll edit cell 15 to print the burst counts at 6300 ms and at the upper end.

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python - <<'EOF'
import json
p='reproduce_hiraoka_2025.ipynb'
nb=json.load(open(p))
c=nb['cells'][15]
s=''.join(c['source'])
old='print(f"paper (Figure 2 labels): about 55 to 6300 ms")\n'
assert old in s
new=old+'print("bursts (m_delta) at delta = 6282.75 ms (the upper end, excluded) and at the 6300 ms label of Figure 2:",\n      int((tau > hi).sum()) + 1, "and", int((tau > 6300).sum()) + 1, "(at least 100 needed)")\n'
s=s.replace(old,new)
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; python -c "
import json;nb=json.load(open('reproduce_hiraoka_2025.ipynb'));print(''.join(nb['cells'][15]['source'])[:900])"
```

```
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb | 2 ++
 1 file changed, 2 insertions(+)
FIG2_PAIRS = [(dp, r * dp, r) for dp in (55, 100, 180, 330, 590) for r in bt.NEURON_RATIOS]
t1 = time.time()
RES = {g: bt.analyse_sequence(spk, g, extra_pairs=FIG2_PAIRS if g == "b" else ()) for g in bt.GRIDS}
print(f"fits done in {time.time() - t1:.0f} s")
lo, hi = RES["a"]["lo"], RES["a"]["hi"]
print(f"relevant timescales: {lo:.2f} ms (smallest delta with a burst of >= 100 events) to {hi:.2f} ms (the 99th largest IET; delta must stay below it for >= 100 bursts)")
print(f"paper (Figure 2 labels): about 55 to 6300 ms")
print("bursts (m_delta) at delta = 6282.75 ms (the upper end, excluded) and at the 6300 ms label of Figure 2:",
      int((tau > hi).sum()) + 1, "and", int((tau > 6300).sum()) + 1, "(at least 100 needed)")
for g in bt.GRIDS:
    print(f"grid ({g}): {len(RES[g]['grid'])} points, step log10 {np.log10(RES[g]['grid'][1] / RES[g]['grid'][0]):.4f}:", RES[g]["grid"].round(1))
B =
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/entry.py | head -5; grep -n "def run\b\|def cmd_run\|nbconvert\|nbclient\|papermill" tools/entry.py | head
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
64:HARNESS = ["ipykernel", "nbconvert"]      # needed to execute, not part of the entry
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
611:    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
626:            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
```

**Agent calls Bash**

```bash
cd  sed -n 596,660p tools/entry.py; ls -d .venv* executed/hiraoka-2025/.venv* 2>/dev/null; ls ~/.cache 2>/dev/null | head
```

```
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
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
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; V=executed/hiraoka-2025/.venv; date -u; JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=registry-hiraoka-2025 --output-dir $TMPDIR --output main.ipynb reproduce_hiraoka_2025.ipynb 2>&1 | tail -3; date -u; python -c "
import json,os
nb=json.load(open(os.environ['TMPDIR']+'/main.ipynb'))
for o in nb['cells'][15]['outputs']: print(''.join(o.get('text',''))[:600])"
```

```
Sun Nov 22 04:56:29 UTC 2026
[NbConvertApp] Converting notebook reproduce_hiraoka_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 238167 bytes to /tmp/claude-1001/main.ipynb
Sun Nov 22 04:59:48 UTC 2026
fits done in 104 s
relevant timescales: 55.25 ms (smallest delta with a burst of >= 100 events) to 6282.75 ms (the 99th largest IET; delta must stay below it for >= 100 bursts)
paper (Figure 2 labels): about 55 to 6300 ms
bursts (m_delta) at delta = 6282.75 ms (the upper end, excluded) and at the 6300 ms label of Figure 2: 99 and 99 (at least 100 needed)
grid (a): 8 points, step log10 0.2601: [  55.2  100.6  183.   333.1  606.2 1103.3 2008.  3654.5]
grid (b): 40 points, step log10 0.0514: [  55.2   62.2   70.    78.8   88.7   99.8  112.4  126.5  142.4  160.3
  180.4  203.1  228.6  257.3  289.6
```

**Agent calls Bash**

```bash
cd  grep -rn "41 \|0.083\|45 min\|99 bursts\|0\.08 " entries/hiraoka-2025/*.ipynb entries/hiraoka-2025/*.md entries/hiraoka-2025/*.py questions/hiraoka-2025.yaml attempts/hiraoka-2025-01.yaml | cut -c1-250
```

```
entries/hiraoka-2025/other_neurons.ipynb:15:    "unit and is kept apart for its run time (about 45 minutes on 4 processes). Every unit of the\n",
entries/hiraoka-2025/other_neurons.ipynb:166:    "0.342 and 0.292, 0.117 and 0.083, and 0.017. The pass is fragile: the continuous fit from\n",
entries/hiraoka-2025/other_neurons.ipynb:214:    "and 0.083. In the inhibitory units of all sessions the parts hold in 0.906 and 0.977 (burst sizes)\n",
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb:832:    "| fig2-other-neurons-similar | reproduced | continuous fit from xmin = 1 alone (0.883 to 0.906); KS fits 0.083 to 0.454 (`other_neurons.ipynb`) |\n",
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb:852:    "  6300 ms, which has 99 bursts by this count.\n",
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb:866:    "- The epochs are longer than the paper's description of the maze session (45 minutes): the maze\n",
entries/hiraoka-2025/README.md:14:  inhibitory (about 45 minutes on 4 processes).
questions/hiraoka-2025.yaml:18:    0.74 for the 128 inhibitory units against 0.08 to 0.45 for the 562 pyramidal ones, and 0.32
attempts/hiraoka-2025-01.yaml:166:    and 0.292, 0.117 and 0.083, and 0.017. The pass is fragile: the continuous fit from xmin = 1 treats
attempts/hiraoka-2025-01.yaml:329:    absolute r of 0.043 beyond 60 s). The epochs differ from the paper's description of 45 minutes of
attempts/hiraoka-2025-01.yaml:338:    to 0.74 of 128 against 0.08 to 0.45 of 562).
attempts/hiraoka-2025-01.yaml:354:    "other sequences in the datasets"? The Figure 2 labels fit 41 log-spaced points over the relevant
attempts/hiraoka-2025-01.yaml:446:      x1_continuous (0.89). ks_discrete, the natural fit for integer data, gives 0.08 to 0.23. The set
```

**Agent calls Bash**

```bash
cd  python -c "
import json
nb=json.load(open('executed/hiraoka-2025/other_neurons.ipynb'))
for i in [5,8]:
  for o in nb['cells'][i].get('outputs',[]): print(''.join(o.get('text',''))[:5000])
"
```

```
690 units fitted (unbounded exponent, both grids) in 49.8 min

set (a) pyramidal, Achilles-10252013:
                    units   used  pattern  frac_pattern  median_b_frac  median_k_frac  beta_q25  beta_median  beta_q75
grid reading                                                                                                          
a    ks_continuous  120.0  120.0     41.0         0.342          0.750          0.408     2.487        2.784     3.211
     ks_discrete    120.0  120.0     14.0         0.117          0.750          0.111     2.345        2.580     2.930
     x1_continuous  120.0  120.0    107.0         0.892          1.000          0.867     1.667        1.774     1.914
     x1_discrete    120.0  120.0      2.0         0.017          0.500          0.000     1.501        1.562     1.636
b    ks_continuous  120.0  120.0     35.0         0.292          0.753          0.359     2.467        2.755     3.165
     ks_discrete    120.0  120.0     10.0         0.083          0.723          0.086     2.331        2.600     2.945
     x1_continuous  120.0  120.0    106.0         0.883          1.000          0.845     1.616        1.744     1.856
     x1_discrete    120.0  120.0      2.0         0.017          0.533          0.000     1.471        1.546     1.607

set (b) pyramidal, all sessions:
                    units   used  pattern  frac_pattern  median_b_frac  median_k_frac  beta_q25  beta_median  beta_q75
grid reading                                                                                                          
a    ks_continuous  562.0  554.0    249.0         0.449          0.778          0.500     2.365        2.636     3.018
     ks_discrete    562.0  554.0    129.0         0.233          0.800          0.222     2.216        2.471     2.789
     x1_continuous  562.0  554.0    502.0         0.906          1.000          1.000     1.672        1.778     1.920
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; sed -n 10,18p other_neurons.ipynb; sed -n 208,218p other_neurons.ipynb
```

```
"Paper: T. Hiraoka and H.-H. Jo, \"Hierarchical organization of bursty trains in event\n",
    "sequences\", doi:10.1063/5.0296506, read from the arXiv preprint body under `paper/`.\n",
    "Dataset: DANDI:000044 version 0.210812.1516, the version the paper cites (ref. 39); see the\n",
    "header of `reproduce_hiraoka_2025.ipynb` for the choice of version and the claims table.\n",
    "This notebook tests one claim, `fig2-other-neurons-similar`, which needs a fit of every\n",
    "unit and is kept apart for its run time (about 45 minutes on 4 processes). Every unit of the\n",
    "eight sessions is fitted, so that the claim's pyramidal sets can be shown beside the\n",
    "inhibitory units and all units (the paper's representative unit is labelled inhibitory)."
   ]
   "id": "aeb82f67",
   "metadata": {},
   "source": [
    "**Result (parts).** With the exponent unbounded and the discrete KS fit, the burst-size part of the\n",
    "pattern holds in 0.744 and 0.770 of the pyramidal units of set (b), and the merging-number part in\n",
    "0.251 and 0.249: it is the merging numbers that fail. In set (a) the merging part holds in 0.117\n",
    "and 0.083. In the inhibitory units of all sessions the parts hold in 0.906 and 0.977 (burst sizes)\n",
    "and 0.781 and 0.695 (merging numbers)."
   ]
  }
 ],
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python - <<'EOF'
import re
def sub(p, old, new):
    s=open(p).read(); assert s.count(old)==1, (p, old); open(p,'w').write(s.replace(old,new))
sub('other_neurons.ipynb', 'about 45 minutes on 4 processes', 'about 50 minutes on 4 processes')
sub('README.md', 'about 45 minutes on 4 processes', 'about 50 minutes on 4 processes')
sub('entry.yaml', 'runtime_minutes: 45', 'runtime_minutes: 50')
m='reproduce_hiraoka_2025.ipynb'
sub(m, "KS fits 0.083 to 0.454 (`other_neurons.ipynb`) |", "KS fits 0.233 to 0.454 over the pyramidal units of all sessions, 0.083 to 0.342 in Achilles-10252013 (`other_neurons.ipynb`) |")
sub(m, "  6300 ms, which has 99 bursts by this count.\\n", "  6300 ms, which has 99 bursts by this count, below the 100 the Methods ask for (printed with the grids).\\n")
EOF
grep -n "40 of\|whole number of log steps" reproduce_hiraoka_2025.ipynb
```

```
451:    "law is supported at every relevant timescale on both grids (8 of 8 on grid (a), 40 of 40 on grid\n",
758:    "pairs with delta < 3000 ms, beta(delta') < gamma in 40 of 57 under both KS fits with the\n",
847:    "- The grid of delta is not given in the paper. Grid (b) fits a whole number of log steps (40 of\n",
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; sed -n 845,853p reproduce_hiraoka_2025.ipynb
```

```
"  the exponent unbounded (an assumption), and the capped fits are shown beside them. The cap\n",
    "  decides one outcome, fig2-neuron-merging-collapse.\n",
    "- The grid of delta is not given in the paper. Grid (b) fits a whole number of log steps (40 of\n",
    "  0.0514 for the representative unit) between the ends of the relevant range; every 5th point\n",
    "  then gives the delta' labels of Figure 2 and every 8th the delta labels. Grid (a) has ratio 1.82\n",
    "  (O4).\n",
    "- The relevant range is computed exactly from the IETs (55.25 to 6282.75 ms here); Figure 2 shows\n",
    "  6300 ms, which has 99 bursts by this count, below the 100 the Methods ask for (printed with the grids).\n",
    "\n",
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python - <<'EOF'
p='reproduce_hiraoka_2025.ipynb'
s=open(p).read()
old='''    "  0.0514 for the representative unit) between the ends of the relevant range; every 5th point\\n",
    "  then gives the delta' labels of Figure 2 and every 8th the delta labels. Grid (a) has ratio 1.82\\n",'''
new='''    "  0.0514 for the representative unit) between the ends of the relevant range, and drops the upper\\n",
    "  end, which has fewer than 100 bursts, so it has 40 points from 55.2 to 5581.5 ms; every 5th point\\n",
    "  then gives the delta' labels of Figure 2 and every 8th the delta labels. Grid (a) has ratio 1.82\\n",'''
assert s.count(old)==1; open(p,'w').write(s.replace(old,new))
EOF
python -c "import json;json.load(open('reproduce_hiraoka_2025.ipynb'));json.load(open('other_neurons.ipynb'))" && echo ok; date -u
```

```
ok
Sun Nov 22 05:00:19 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python -c "
import json
nb=json.load(open('model.ipynb'))
for i in [5,9,12,15]:
    print('=== cell',i); print(''.join(nb['cells'][i]['source']))
for i,c in enumerate(nb['cells']):
    if ''.join(c['source']).startswith('## Summary'): print('=== summary',i); print(''.join(c['source']))
"
```

```
=== cell 5
**Result: partially reproduced under the claim's seed, and seed sensitive.** With the exponent
unbounded, no single reading of the fit holds for all three series under the claim's seed, on
either grid. Under the discrete KS fit the linear and quadratic series hold on grid (a), and the
exponential series has heavy tails (supported at 8 of 11 timescales and 17 of 20 pairs on grid
(a), 42 of 52 and 79 of 94 on grid (b)) but its gamma has an interquartile range of 0.544 and
0.508, above 0.5; on grid (b) the linear series also fails (gamma interquartile range 0.511). The
fits from xmin = 1 hold for the exponential series but not the quadratic one (beta interquartile
range 0.508 to 0.953). Capped at 3 (grid (a)), the discrete KS fit gives 0.522 for the
exponential gamma and still fails. Under the four further seeds the discrete KS fit holds for all
three series under seeds + 1000, + 2000 and + 3000, and not under + 4000, where the linear series
fails; the exponential gamma interquartile range runs from 0.203 to 0.544 over the five seeds.
Taking for each series whichever reading holds, every series holds under every seed on grid (a);
the claim is judged under one reading for all three series.
=== cell 9
**Result: partially reproduced, and seed sensitive.** Under the claim's seed tau_max is 1711.4
(linear, rel_diff -0.127 from 1960), 21 390.9 (quadratic, within 10% of 20 800) and 61 320.3
(exponential, rel_diff -0.249 from 81 600). tau_max is an IET of the highest level the sequence
reaches, which varies from seed to seed (levels 14 to 18 linear, 14 to 16 quadratic, 13 to 18
exponential, against 19, 14 and 16 for the paper's values); over the five seeds the values are
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python - <<'EOF'
import json
p='model.ipynb'
nb=json.load(open(p))
def add(i, old_end, extra):
    s=''.join(nb['cells'][i]['source']); assert s.endswith(old_end), s[-80:]
    nb['cells'][i]['source']=(s+extra).splitlines(keepends=True)
add(5, "the claim is judged under one reading for all three series.",
 " The criterion defines no partial\noutcome. Partially reproduced is the protocol's outcome for a result that holds only in part, and\nhere the criterion holds for two of its three series under the adopted reading. This differs from\nfig2-neuron-beta-stable, which is not reproduced because no reading meets its single condition.")
add(9, "the comparison with the earthquake and Wikipedia sequences cannot be made here.",
 " The criterion\ndefines no partial outcome; partially reproduced is used, as the protocol defines it, because one\nof the three expected values is within its tolerance and two are not.")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
cd ../..; git diff --stat
```

```
entries/hiraoka-2025/README.md                    | 2 +-
 entries/hiraoka-2025/entry.yaml                   | 2 +-
 entries/hiraoka-2025/model.ipynb                  | 9 +++++++--
 entries/hiraoka-2025/other_neurons.ipynb          | 2 +-
 entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb | 9 ++++++---
 5 files changed, 16 insertions(+), 8 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python -c "
import json
nb=json.load(open('reproduce_hiraoka_2025.ipynb'))
print(''.join(nb['cells'][28]['source']))"
```

```
**Result: not reproduced with the exponent unbounded (an assumption); reproduced only when it is
capped at 3.** Reading (b): with the exponent unbounded, the gamma of the 15 pairs of Figure 2
lie up to 0.538 from their median under the discrete KS fit (median 2.610), 1.742 under the
continuous KS fit, 0.521 under the discrete fit from xmin = 1 and 1.249 under the continuous one,
all outside the band of 0.5. The deviation of 0.538 is the pair delta' 180 ms, delta 594 ms
(gamma 3.148), which the cap holds at 2.843, giving the 0.490 of the capped discrete KS fit, the
only fit within the band. Reading (a) fails: the CCDFs of k / <k> differ by up to a factor of
12.54 (median 1.63) where all exceed 10^-3. One pair of Figure 2 (delta' 590 ms, delta 6490 ms)
lies above the relevant range, with 89 bursts.
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025; python - <<'EOF'
import json
p='reproduce_hiraoka_2025.ipynb'
nb=json.load(open(p))
s=''.join(nb['cells'][28]['source']); end="lies above the relevant range, with 89 bursts."
assert s.endswith(end)
s+=(" The margin is small (0.538 and 0.490 against\n0.5), and O3 (a) names the package's default, which in the locked powerlaw 2.0.0 is the capped\n"
    "fit: read that way the claim would be reproduced. The unbounded exponent is kept because the method\n"
    "the paper cites has no cap and the cap clips the very estimate that decides the band; whether the\n"
    "paper's fits were capped is asked of the authors (record, findings).")
nb['cells'][28]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
cd ../..; git diff --stat | tail -1; date -u
```

```
5 files changed, 21 insertions(+), 9 deletions(-)
Sun Nov 22 05:00:40 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls schemas 2>/dev/null; grep -rn "findings" schemas/*attempt* 2>/dev/null | head -20
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
cd  sed -n 395,510p schemas/attempt.schema.json; grep -n '"proposed"' -A30 schemas/attempt.schema.json | head -40
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
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/hiraoka-2025 2>&1 | tail -5
```

```
0 error(s)
```

**Agent**

Checks pass. Starting the full re-run (about 95 minutes by the recorded runtimes).

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/hiraoka-2025 2>&1 | tail -15; date -u
```

```
Sun Nov 22 05:01:00 UTC 2026
Installed kernelspec registry-hiraoka-2025 in executed/hiraoka-2025/.venv/share/jupyter/kernels/registry-hiraoka-2025
0 error(s)
pass  reproduce_hiraoka_2025.ipynb  (203 s)
pass  other_neurons.ipynb  (2972 s)
pass  other_neurons_cap3.ipynb  (649 s)
pass  model.ipynb  (1040 s)
Sun Nov 22 06:22:15 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/hiraoka-2025; python - <<'EOF'
import json,re
nums={'reproduce_hiraoka_2025.ipynb':['228356','17362','1.079','2.354','3.349','0.538','0.490','12.54','0.378','0.415','0.0416','-0.829','99 and 99','5581.5','0.642','0.546'],
 'other_neurons.ipynb':['0.906','0.893','0.449','0.454','0.233','0.240','0.719','0.680','0.742','49.','50.'],
 'other_neurons_cap3.ipynb':['0.547','0.906'],
 'model.ipynb':['1711.4','21390.9','61320.3','0.544','0.508','0.511','0.4487','0.1874','0.0079','566721','0.203']}
for nb,ns in nums.items():
    d=json.load(open(nb)); txt=''
    for c in d['cells']:
        for o in c.get('outputs',[]):
            txt+=''.join(o.get('text',''))+json.dumps(o.get('data',{}).get('text/plain',''))
    print(nb,[n for n in ns if n not in txt.replace(' ','') and n not in txt])
EOF
python -c "
import json
nb=json.load(open('other_neurons.ipynb'))
for c in nb['cells']:
  for o in c.get('outputs',[]):
    t=''.join(o.get('text',''))
    if 'min' in t and ('fitted' in t or 'notebook time' in t): print(t[:200])
"
```

```
reproduce_hiraoka_2025.ipynb []
other_neurons.ipynb []
other_neurons_cap3.ipynb []
model.ipynb []
690 units fitted (unbounded exponent, both grids) in 48.9 min

set (a) pyramidal, Achilles-10252013:
                    units   used  pattern  frac_pattern  median_b_frac  median_k_frac  beta_q25  be

set (a) pyramidal, Achilles-10252013:
                    used  burst_ok  merge_ok      both
grid reading                                          
a    ks_continuous   120     0.750     0.350  0.341
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/hiraoka-2025-01.yaml'
s=open(p).read()
def sub(old,new):
    global s
    assert s.count(old)==1, old
    s=s.replace(old,new)
sub("""    to 0.74 of 128 against 0.08 to 0.45 of 562).""","""    to 0.74 of 128 against 0.23 to 0.45 of 562; in Achilles-10252013 alone 0.76 to 0.88 of 17 against
    0.08 to 0.34 of 120).""")
sub("""    "other sequences in the datasets"? The Figure 2 labels fit 41 log-spaced points over the relevant
    range, which this attempt used; whether all units or the pyramidal ones were analysed is not said.""",
"""    "other sequences in the datasets"? The Figure 2 labels fit a log-spaced grid of 40 steps of 0.0514
    over the relevant range; this attempt used its 40 points below the upper end (55.2 to 5581.5 ms),
    since the upper end has fewer than 100 bursts. Whether all units or the pyramidal ones were analysed
    is not said.""")
sub("""- kind: format_error
  severity: major""","""- kind: format_error
  severity: minor""")
# merging-collapse caveat
sub("""    10^-3. One pair of Figure 2 (delta'' 590 ms, delta 6490 ms) lies above the relevant range, with 89
    bursts.'""","""    10^-3. One pair of Figure 2 (delta'' 590 ms, delta 6490 ms) lies above the relevant range, with 89
    bursts. The margin is small (0.538 unbounded and 0.490 capped, against 0.5). O3 (a) names the package''s
    default, which in the locked powerlaw 2.0.0 is the capped fit, and read that way the claim would be
    reproduced; the verifier reads the outcome as undetermined between the two. The unbounded exponent
    is kept, as the method the paper cites has no cap and the cap clips the estimate that decides the
    band, and whether the paper''s fits were capped is asked of the authors (findings).'""")
# fig4 heavy tails
sub("""    five seeds. Each series holds under some reading under every seed on grid (a).""",
"""    five seeds. Each series holds under some reading under every seed on grid (a). The criterion defines
    no partial outcome; partially reproduced is the protocol's outcome for a result that holds only in
    part, and the criterion holds for two of its three series under the adopted reading. This differs
    from fig2-neuron-beta-stable, which is not reproduced because no reading meets its single condition.""")
sub("""    tau = 10.
- claim: model-decremental-equivalent""","""    tau = 10. The criterion defines no partial outcome; partially reproduced is used, as the protocol
    defines it, because one of the three expected values is within its tolerance and two are not.
- claim: model-decremental-equivalent""")
sub("""    not decide the outcome.'
  deviations:""","""    not decide the outcome. Whether the criterion''s test can decide equivalence, since it rejects two
    runs of one algorithm, is asked of a reader (questions); the outcome stands under the calibrated
    test as well, as L differs there in all three series.'
  deviations:""")
open(p,'w').write(s)
EOF
python -c "import yaml;yaml.safe_load(open('attempts/hiraoka-2025-01.yaml'))" && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='questions/hiraoka-2025.yaml'
s=open(p).read()
old="0.74 for the 128 inhibitory units against 0.08 to 0.45 for the 562 pyramidal ones"
assert s.count(old)==1
s=s.replace(old,"0.74 for the 128 inhibitory units against 0.23 to 0.45 for the 562 pyramidal ones")
s+="""- claim: model-decremental-equivalent
  question: The criterion reads "statistically equivalent" as two-sample Kolmogorov-Smirnov tests
    of the burst sizes at each relevant timescale, none differing at p < 0.05 after Bonferroni
    correction. On the model's sequences this test rejects two independent runs of the same
    algorithm (Algorithm 2 against itself, 4 and 11 of the relevant timescales on the two grids
    under the claim's seed), as the bursts of one sequence at nearby timescales are not
    independent samples and n = 10^6 gives the test great power. Should equivalence be read with
    a test whose level is checked on two runs of one algorithm, such as one that takes
    independent runs of each algorithm as the units?
  passage: Section IV, paragraph 9. "We omit the results for event sequences generated by the
    decremental algorithm since it produces statistically equivalent sequences as the incremental
    one."
  why: A criterion that rejects identical algorithms cannot show that two algorithms are
    equivalent, so it could only give not reproduced. The outcome here does not turn on it, as the
    literal set-up of Section IV also differs under a test calibrated across five runs (p = 0.0079
    in each series, where two runs of one algorithm give p 0.373 to 0.913), but under the set-up
    with both algorithms on the zeta distribution the calibrated test finds them equivalent and
    the criterion does not.
"""
open(p,'w').write(s)
EOF
python -c "import yaml;print(len(yaml.safe_load(open('questions/hiraoka-2025.yaml'))['questions']))"; grep -rn "questions" docs/protocol.md | head -5; ls schemas
```

```
2
186:### 6. Answer questions
197:`questions/<paper>.yaml`.
345:     do not change the claim. Add a question to `questions/<paper>.yaml`
612:revision adds it to `questions/<paper>.yaml` as a question for a reader, as in
646:  questions, transcripts or notes, and not the repository's history.
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Bash**

```bash
cd  cat >> attempts/hiraoka-2025-01.yaml <<'EOF'
- date: '2026-11-22'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: 'Round 2: the full executed notebooks of the revised run (reproduce_hiraoka_2025.ipynb, other_neurons.ipynb,
    other_neurons_cap3.ipynb, model.ipynb) with their conclusions and summary, the helper module, the claims
    file and this attempt record, with the paper under paper/.'
  results:
  - claim: fig2-neuron-representative-sequence
    agrees: true
    outcome: reproduced
    reason: Agrees (main 9).
    response: No change.
  - claim: fig2-iet-broad
    agrees: true
    outcome: reproduced
    reason: Agrees (main 12).
    response: No change.
  - claim: fig2-neuron-burst-size-heavy-tail
    agrees: true
    outcome: reproduced
    reason: 8/8 and 40/40 under both KS fits, capped or not (main 18).
    response: No change.
  - claim: fig2-neuron-beta-stable
    agrees: true
    outcome: not_reproduced
    reason: Range 1.079; capped KS ranges 0.552 to 0.705 (main 21).
    response: No change.
  - claim: fig2-neuron-beta-decrease-follows-gamma
    agrees: true
    outcome: reproduced
    reason: Part (2) rests on 6 points at p = 0.0416 (main 33), and the record says so.
    response: No change.
  - claim: fig2-neuron-merging-heavy-tail
    agrees: true
    outcome: reproduced
    reason: The round-1 objection is answered. Without the cap, ks_discrete IQR is 0.378 and 0.415, with
      13/15 and 70/76 supported (main 24).
    response: No change.
  - claim: fig2-neuron-merging-collapse
    agrees: true
    outcome: not_reproduced
    reason: Agrees, with a caveat. The assumption (unbounded exponent) is stated and is methodologically
      reasonable. The result is knife-edge, 0.538 unbounded against 0.490 capped, band 0.5 (main 27). O3(a)
      says "the powerlaw package's default", and the locked 2.0.0 default is the capped fit, so a literal
      O3 reading would give reproduced. The outcome is best read as undetermined between the two.
    response: No change of outcome, and none proposed, as the verifier agrees with it and finds the assumption
      reasonable. The caveat is now in the notes and in the result cell (main 28) - the margin, the literal
      reading of O3 (a) under which the claim would be reproduced, and why the unbounded exponent is kept.
      The question of the cap is already put to the authors (findings).
  - claim: fig2-exponents-above-two
    agrees: true
    outcome: reproduced
    reason: Agrees (main 30).
    response: No change.
  - claim: fig2-other-neurons-similar
    agrees: true
    outcome: reproduced
    reason: Agrees under the one-reading rule; fragile. Passes only under x1_continuous (0.883 to 0.906,
      on 5). That reading also passes for inhibitory (0.781 to 0.836) and all units (0.872 to 0.893), so
      the pass does not depend on the pyramidal restriction or on the cap (cap3 5). It rests solely on x1_continuous,
      a poor fit for integer data whose median beta is about 1.75 against the paper's 2.35. The claims file
      restricts the claim to pyramidal units, but the paper's own representative unit is labelled inhibitory.
    response: No change. The fragility is stated in the notes, and the question of the set is in questions/hiraoka-2025.yaml.
      The summary table now gives the KS fractions per set (0.233 to 0.454 over the pyramidal units of
      all sessions, 0.083 to 0.342 in Achilles-10252013).
  - claim: fig2-wikipedia-beta
    agrees: true
    outcome: blocked
    reason: Blocked, yes. The record answers the data_missing objection with a protocol rule the verifier
      cannot see, and the disagreement is recorded.
    response: No change. The rule is the protocol's (author, step 1.4) for a claim with data elsewhere.
  - claim: fig2-earthquake-beta
    agrees: true
    outcome: blocked
    reason: The pinning rationale is stated and the disagreement is recorded. The earthquake n is not resolved;
      the author declined, citing the pinning rule.
    response: No change; the catalog has no versioned release, so the count was not made.
  - claim: fig4-model-heavy-tails
    agrees: true
    outcome: partially_reproduced
    reason: The assumption (one fit reading applied to all three series) is stated and reasonable (model
      4). The criterion defines no partial outcome, while the author's response on beta-stable changed
      that outcome for exactly that reason. By that logic this claim would be not_reproduced under the
      adopted reading. The record should say why "partially" is used here.
    response: 'No change of outcome. The notes and the result cell (model 5) now say why: partially reproduced
      is the protocol''s outcome for a result that holds only in part, and the criterion holds for two of
      its three series under the adopted reading, while fig2-neuron-beta-stable is not reproduced because
      no reading meets its single condition.'
  - claim: fig4-model-iet-shapes
    agrees: true
    outcome: partially_reproduced
    reason: 1 of 3 values within tolerance (model 8). The same caveat about an undefined partial outcome
      applies.
    response: No change of outcome. The notes and the result cell (model 9) now say that partially reproduced
      is used because one of the three expected values is within its tolerance and two are not.
  - claim: model-decremental-equivalent
    agrees: true
    outcome: not_reproduced
    reason: Under L every test rejects, and the calibrated variant also rejects in 3/3 series at p = 0.0079
      (model 11, 14). The KS criterion rejects two runs of the same algorithm (N, 4 and 11 rejections, model
      11), so it cannot test equivalence; the outcome stands only because L also fails the calibrated test.
    response: No change of outcome. The point on the criterion is added to questions/hiraoka-2025.yaml as
      a question for a reader, and the notes say so; the claim is not changed.
  findings:
  - finding: 1
    agrees: false
    severity: minor
    reason: No finding is rated critical. On finding 1 (format_error, rated major), main 3 and on 3 show
      it as stated; three unit-id-2 trains are two sorted runs, broken after index 65 535 (131 071 in Gatsby-08022013).
      The fault shows in the values (negative IETs, min_iet -2x10^7 ms in main 3), so it would rate it minor.
      Excluding the units changes no fraction by more than 0.003 (on 5). Major is defensible only on the
      grounds that whether each train holds one unit's spikes cannot be checked.
    response: Severity changed to minor, the verifier's. What the outputs show is spike times that need sorting,
      evident from the values, and the protocol rates what was shown where the data cannot settle more.
EOF
python -c "import yaml;yaml.safe_load(open('attempts/hiraoka-2025-01.yaml'))" && echo ok
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/hiraoka-2025-01.yaml'
s=open(p).read()
old="result cell (main 28) - the margin,"
assert s.count(old)==1
s=s.replace(old,"result cell (main 28), which give the margin,")
open(p,'w').write(s)
EOF
python - <<'EOF'
import re
lines=open('attempts/hiraoka-2025-01.yaml').read().splitlines()
start=[i for i,l in enumerate(lines) if l.startswith("- date: '2026-11-22'")][-1]
for i,l in enumerate(lines[start:],start):
    m=re.match(r"^\s*(?:- )?[a-z_]+: (.*)$",l)
    body = m.group(1) if m else l.strip()
    if ': ' in body and not body.startswith(("'",'"')): print(i+1,l)
for f in ['attempts/hiraoka-2025-01.yaml','questions/hiraoka-2025.yaml']:
    t=open(f).read(); print(f, '—' in t, 'rather' in t.lower())
EOF
python tools/entry.py check entries/hiraoka-2025 2>&1 | tail -3
```

```
attempts/hiraoka-2025-01.yaml False False
questions/hiraoka-2025.yaml False False
0 error(s)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -c "—" entries/hiraoka-2025/*.ipynb entries/hiraoka-2025/README.md | grep -v ":0"; date -u
```

```
M attempts/hiraoka-2025-01.yaml
 M entries/hiraoka-2025/README.md
 M entries/hiraoka-2025/entry.yaml
 M entries/hiraoka-2025/model.ipynb
 M entries/hiraoka-2025/other_neurons.ipynb
 M entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb
 M questions/hiraoka-2025.yaml
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
Sun Nov 22 06:23:30 UTC 2026
```

**Agent**

No outcome changed and none is proposed. The verifier agreed with all 14 outcomes in round 2. I re-ran the whole entry with `python tools/entry.py all entries/hiraoka-2025`: all four notebooks passed, the checks report 0 errors, and the numbers I spot-checked match the previous run.

**Corrected or added, point by point:**
- **Finding 6:** the numbers were wrong. It now says 0.23 to 0.45 of the 562 pyramidal units (not 0.08), and gives the Achilles-10252013 figures on their own (0.08 to 0.34 of 120 pyramidal units, 0.76 to 0.88 of 17 inhibitory). The same error is fixed in the existing question in `questions/hiraoka-2025.yaml`.
- **Grid finding:** "41 points" is replaced. The grid has 40 steps of 0.0514, the upper end is dropped because it has fewer than 100 bursts, and 40 points are used, from 55.2 to 5581.5 ms. The summary in the main notebook now says the same.
- **Burst count at 6300 ms:** the verifier asked for this output. Cell 15 of the main notebook now prints it: 99 bursts at both 6282.75 and 6300 ms, so the summary sentence is now backed by an output.
- **Summary table:** the KS fractions are now split by set: 0.233 to 0.454 over the pyramidal units of all sessions, 0.083 to 0.342 in Achilles-10252013.
- **Run time:** `other_neurons.ipynb` takes about 50 minutes, not 45. The README, its own header and `entry.yaml` now say so.
- **fig2-neuron-merging-collapse:** the verifier's caveat is now in the notes and in the result cell. The margin is small (0.538 with the exponent unbounded, 0.490 capped, against a band of 0.5). A literal reading of the claims file's "package default" would use the capped fit and give reproduced. The notes say why the unbounded exponent is kept. I proposed no change because the verifier agrees with the outcome and calls the assumption reasonable.
- **fig4-model-heavy-tails and fig4-model-iet-shapes:** the verifier asked why these are "partially reproduced" when the criteria define no partial outcome. The notes and result cells now explain it. For heavy tails, the criterion holds for 2 of its 3 series. For the inter-event-time shapes, 1 of the 3 expected values is within tolerance. fig2-neuron-beta-stable is different: no reading meets its single condition, so it is not reproduced.
- **New question for a reader:** the model-decremental-equivalent criterion rejects two runs of the same algorithm, so it cannot show equivalence. This is now a question in `questions/hiraoka-2025.yaml`; the claim is not changed. The outcome does not depend on this point, because the literal set-up also fails the calibrated test.
- **Finding 1 (unsorted spike trains):** severity lowered from major to minor, as the verifier rated it. The fault shows in the values (negative gaps between spikes) and only needs sorting.
- **Round 2 record:** added under `verifications`, with the verifier's reasons, my response to each claim, and its view on finding 1 under `findings`.

**Not done:**
- I did not count the earthquakes, because the earthquake catalogue has no pinned version. The disagreement was already recorded and is kept.
- Which circles are filled in Figures 2 and 4 is still open, because there is no PDF of the figures.

Nothing is committed.

## End of run

38 turns, 89 minutes, $2.07 at API prices, result: success.
