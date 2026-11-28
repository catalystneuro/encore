# alonso-2020 · author-revise-1 · run 46100618858

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/alonso-2020/verifier-1-report.md; ls entries/alonso-2020 questions 2>/dev/null | head -50
```

```
Sat Nov 28 03:06:48 UTC 2026
**Verifier report, round 1: Alonso & Marder 2020 (doi:10.7554/elife.55470), Dryad m31b1h7 v94811**

The claims file has 23 claims. I checked the archive through Dryad's API: version 94811 is the only version and holds one zip of 99,026 bytes, whose MD5 matches the one the notebook checks. I ran the helper functions on synthetic spike trains and voltage traces. `bursts`, `burst_stats`, `classify_cell`, `triphasic`, `cycle_largest_isi`, `shares` and `spike_shapes` all behaved as documented. One gap: continuous irregular spiking with no gap over 200 ms is labelled "other".

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| deposit-models | not_reproduced | Cell 12: 3 of 38 models are within tolerance, against the 30 needed. The 0.20 variant gives 0 of 38, and mean frequency is 1.25 Hz. Cells 7, 8 and 10: 4 of the 21 named models are absent, the deposit holds 38 models (not 36), and those 38 contain only 27 distinct conductance sets. |
| fig1c-frequency-q10-phase-constant | partially_reproduced | Cell 17: the frequency Q10 of 4X6W66 is 1.93, 1.98 or 1.94 under readings a, b and c, all within 2±0.2. Constancy fails under both readings: the LP duty-cycle range is 0.11 (above 0.1) and its change from 10 °C is 34% (above 20%). |
| fig1s1-three-models | not_reproduced | Cell 19: frequency rises in all three models, but none is constant under either reading. 71G6LA misses reading (i) only on PY offset (range 0.102). |
| all-models-compensated | partially_reproduced | Cell 21: 36 of 38 models are triphasic at all 16 temperatures (35 with the strict order variant). ED50XO fails at 19 and 21 °C; MAXTTP fails at 10 and 14 °C, and MAXTTP is a paper model (Fig. 2–S1), so not every paper model passes. "Multiple Q10 sets for every conductance set" is unsupported: only 9 of the 27 conductance sets carry more than one Q10 set. |
| intermediate-temperature-failures | blocked (data_missing) | Confirmed: the archive is one zip with 38 parameter fil
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
813 docs/protocol.md
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
374:### 2. Check the data against its description
397:### 3. Write the entry
482:### 4. Lock, check and run
502:### 5. Record the attempt
633:### 6. Hand over for verification
671:## Repeat attempts
737:## Local and remote datasets
760:## Verifier
764:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,670p docs/protocol.md; sed -n 760,813p docs/protocol.md
```

```
<persisted-output>
Output too large (34.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9ce613b2-7ebd-4fac-930d-9e761b5a9292/tool-results/bu976f3gm.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-19`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9ce613b2-7ebd-4fac-930d-9e761b5a9292/tool-results/bu976f3gm.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 549 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep alonso; ls executed/alonso-2020 2>/dev/null; cat entries/alonso-2020/entry.yaml; cat entries/alonso-2020/README.md; wc -l entries/alonso-2020/*; git diff --stat; ls transcripts/alonso-2020
```

```
alonso-2020-01.yaml
ramps.ipynb
reproduce_alonso_2020.ipynb
result.json
voltage_distributions.ipynb
schema_version: 1
name: alonso-2020
type: reproduction
title: Temperature compensation in a model pyloric network (Alonso and Marder 2020)
description: Tests the findings of Alonso and Marder (2020) on Dryad m31b1h7, which holds the authors' Java model of a
  three-cell pyloric network, their Python scripts, and the parameters of 38 temperature-compensated models. Every
  claim is tested by simulating the deposited models with a port of the deposited Java, at fixed temperatures, on
  temperature ramps, with currents removed, and at high temperatures where the networks crash.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_alonso_2020.ipynb
  title: Reproducing Alonso and Marder (2020) from Dryad m31b1h7
  runtime_minutes: 15
- path: ramps.ipynb
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/alonso-2020-01.yaml
```

```
schema_version: 3
id: alonso-2020-01
datasets:
- archive: dryad
  id: m31b1h7
  version: "94811"
  doi: 10.5061/dryad.m31b1h7
  relation: primary
paper: doi:10.7554/elife.55470
date: 2026-11-27
entry: alonso-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-19
  runner:
[... 383 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/alonso-2020/pyloric.py"
}
```

```
1	"""Loading, simulation and measures for the temperature-compensated pyloric networks of Dryad m31b1h7.
2	
3	Alonso & Marder (2020), "Temperature compensation in a small rhythmic circuit", eLife 9:e55470,
4	doi:10.7554/eLife.55470. The dataset (doi:10.5061/dryad.m31b1h7, version id 94811, the only
5	published version) is one zip, alonso_marder_tempcomp_2019_root.zip, holding the authors' Java model,
6	their Python driver scripts, one initial-condition file (cis_network.txt) and one parameter file per
7	model (p-<NAME>.score.<score>.txt, 132 numbers each). Dryad needs a token to download, so the
8	workflow stages the file under /tmp/dryad/m31b1h7/94811/ before the run (docs/archives.md, "Dryad");
9	it is read there in place, into memory, and checked against the MD5 that Dryad's file list gives.
10	
11	Where things come from:
12	
13	- The model is a line-by-line port of the deposited Java classes
14	  PrinzNetworkWithTemperature_full_eu_slow_same_q10s_rk4.java (network, synapses, Q10 of the
15	  synapses), singleCompTemperature_slow_explicit.java (each cell) and Integrador.java (RK4), into
16	  numba. Parameter layout, per cell 37 numbers: 8 maximal conductances (Na, CaT, CaS, A, KCa, Kd, H,
17	  leak), EL, ENa, EK, EH, 23 Q10 values (indices 12 to 34), tau_Ca / 10 (index 35), injected
18	  current (36); then 7 synaptic conductances and 14 synaptic Q10 values, of which the Java uses
19	  0 (glutamatergic g), 1 (cholinergic g), 7 (glutamatergic tau) and 8 (cholinergic tau). As in the
20	  Java, the Q10 values of the PD (first) cell are used for all three cells. Choices kept from the
[... 663 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; python -c "
import json,sys
nb=json.load(open('ramps.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
"
```

```
=== cell 0 markdown None
# Alonso & Marder (2020), temperature ramps, from Dryad m31b1h7

Paper: Alonso LM, Marder E (2020), eLife 9:e55470, doi:10.7554/eLife.55470; claims in
`claims/alonso-2020.yaml` (version of record, main text, legends and Methods).

Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811 (the only published version, so the
one pinned), file `alonso_marder_tempcomp_2019_root.zip` (MD5 from Dryad's file list checked on
load; SHA-256 printed below). The models are simulated with the port in `pyloric.py`; the main
notebook, `reproduce_alonso_2020.ipynb`, compares it with the deposited Java and checks the data.

Two ramp protocols:

- up: 10 to 25 degrees C over 60 min (Results, Duty cycle and phase maintenance, paragraph 5,
  "ramps from 10 C to 25 C over 60 min"), model PLKTEM, for figs2-ramp-largest-isi;
- updown: 10 to 35 degrees C in 30 min and back to 10 degrees C at the same rate (Results,
  Hysteresis and multistability, paragraph 1), every deposited model (38), for
  fig8a-hysteresis-quiescence, fig8-up-down-ramps and fig8b-pathological-attractor.

The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
for nb in ['ramps','reproduce_alonso_2020','voltage_distributions']:
    d=json.load(open(f'executed/alonso-2020/{nb}.ipynb'))
    for c in d['cells'][-1:]:
        for o in c.get('outputs',[]): print(nb, o.get('text'))
EOF
grep -n "fig8-up-down-ramps" -A40 claims/alonso-2020.yaml | head -60; which javac java; nproc
```

```
ramps ['notebook run time 59.0 min; peak memory 0.36 GB\n']
reproduce_alonso_2020 ['notebook run time 23.6 min; peak memory 0.75 GB\n']
voltage_distributions ['notebook run time 23.4 min; peak memory 0.30 GB\n']
407:- id: fig8-up-down-ramps
408-  statement: In 34 of the 36 models the spiking patterns over the working range are similar
409-    but not identical on the up and down ramps, suggesting several stable attractors that
410-    differ slightly in their spiking patterns.
411-  source: Results, Hysteresis and multistability, paragraph 1; Figure 1, figure supplement 2E
412-  quote: In most models (34 of 36), the spiking patterns over the working temperature range are
413-    similar across the up and down ramps but are not identical
414-  expected:
415-  - quantity: models with similar but not identical patterns on the two ramps
416-    value: 34
417-    tolerance: 3
418-  criterion: All 36 models on the ramp of fig8a-hysteresis-quiescence, comparing the up and down
419-    ramps over 10 to 25 degrees C; the ramp of Figure 1, figure supplement 2 (10 to 25 degrees
420-    C over 60 min and back) is the alternative reading, as the supplement's legend is not in
421-    the text read. Per cell and per 1 degree window, the mean duty cycle, burst frequency and
422-    largest ISI on each ramp. Similar is all of these within 10% between the ramps in every
423-    window and the network triphasic on both (a standard bound); not identical is spike times
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && ls /tmp/dryad/m31b1h7/94811/ && python - <<'EOF'
import time, numpy as np, pyloric as P
Z=P.open_zip(P.read_zip_bytes()); M=P.load_models(Z); CI=P.load_ci(Z)
p=M['PLKTEM']
P.simulate(p,10,1,CI)
t=time.time(); P.simulate(p,10,60,CI,temp_end=12); print('1 proc 60 s sim:',time.time()-t)
t=time.time(); P.pmap(P.run_ramp,[(n,M[n],CI,[(10.,12.,60.)]) for n in list(M)[:8]]); print('4 procs 8x60 s:',time.time()-t)
EOF
```

```
Exit code 1
alonso_marder_tempcomp_2019_root.zip
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls -a; ls .venv* venv* 2>/dev/null | head; grep -n "def cmd_run\|venv\|def run" tools/entry.py | head -30
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
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 600,720p tools/entry.py; ls -a executed/alonso-2020/
```

```
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
    try:
        stamp = json.loads((output_dir / STAMP).read_text())
        entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
            return None
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && PY=executed/alonso-2020/.venv/bin/python; $PY - <<'EOF'
import time, numpy as np, pyloric as P
Z=P.open_zip(P.read_zip_bytes()); M=P.load_models(Z); CI=P.load_ci(Z)
p=M['PLKTEM']
P.simulate(p,10,1,CI)
t=time.time(); P.simulate(p,10,60,CI,temp_end=12); print('1 proc 60 s sim:',time.time()-t)
t=time.time(); P.pmap(P.run_ramp,[(n,M[n],CI,[(10.,12.,60.)]) for n in list(M)[:8]]); print('4 procs 8x60 s:',time.time()-t)
EOF
```

```
1 proc 60 s sim: 3.563997268676758
4 procs 8x60 s: 11.864813089370728
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python3 -c "
import json
nb=json.load(open('reproduce_alonso_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
" > $TMPDIR/main_src.txt; wc -l $TMPDIR/main_src.txt; grep -n "=== cell" $TMPDIR/main_src.txt | head -80
```

```
/bin/bash: line 1: cd: entries/alonso-2020: No such file or directory
wc: /tmp/claude-1001/main_src.txt: No such file or directory
grep: /tmp/claude-1001/main_src.txt: No such file or directory
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && python3 -c "
import json
nb=json.load(open('reproduce_alonso_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
" > $TMPDIR/main_src.txt; wc -l $TMPDIR/main_src.txt; grep -n "=== cell" $TMPDIR/main_src.txt | head -80
```

```
919 /tmp/claude-1001/main_src.txt
1:=== cell 0 markdown None
53:=== cell 1 code None
83:=== cell 2 markdown None
85:=== cell 3 code ['sanity']
113:=== cell 4 markdown None
117:=== cell 5 code None
141:=== cell 6 markdown None
147:=== cell 7 code None
181:=== cell 8 code ['finding-model-names']
186:=== cell 9 markdown None
191:=== cell 10 code ['finding-shared-conductances']
202:=== cell 11 markdown None
212:=== cell 12 code ['claim:deposit-models']
246:=== cell 13 code ['finding-frequency-at-10C']
249:=== cell 14 markdown None
257:=== cell 15 markdown None
263:=== cell 16 code None
318:=== cell 17 markdown None
327:=== cell 18 code ['claim:fig1c-frequency-q10-phase-constant']
[... 50 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main_src.txt"
}
```

```
1	=== cell 0 markdown None
2	# Reproducing Alonso & Marder (2020) from Dryad m31b1h7
3	
4	Paper: Alonso LM, Marder E (2020). Temperature compensation in a small rhythmic circuit. eLife
5	9:e55470, doi:10.7554/eLife.55470. The claims file, `claims/alonso-2020.yaml`, was written from
6	the version of record (main text, legends and Methods; the figure supplements' legends were not
7	in the text read).
8	
9	Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811, one file,
10	`alonso_marder_tempcomp_2019_root.zip` (99,026 bytes, MD5 37766522dabaaa620d4c44264e76e686 from
11	Dryad's file list; its SHA-256 is printed below). Version 94811 is pinned because it is the only
12	published version of the dataset (the versions list of the API gives one, published 2020-12-07),
13	and the paper cites the dataset by its DOI, which resolves to it. Dryad needs a token to
14	download, so the workflow stages the file before the run and the notebook reads it in place,
15	into memory (docs/archives.md, "Dryad").
16	
17	The paper has no recordings. The dataset holds the authors' Java model, Python driver scripts,
18	initial conditions and the parameters of each model network. Every claim is tested by simulating
19	the deposited models with a numba port of the deposited Java (`pyloric.py`), checked against the
20	Java below when a Java compiler is present.
[... 755 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main_src.txt",
 "offset": 776
}
```

```
776	
777	FGFKQS (Methods; also the deposit's script, "Fig. 13B") and J9U8SQ (legend), the same timings.
778	=== cell 59 code ['claim:fig9b-remove-kca-current']
779	fig9b = {}
780	for n in ["FGFKQS", "J9U8SQ"]:
781	    for tm, (ctl, aft) in TIMINGS.items():
782	        b10, a10, s1, s2 = removal(n, 4, 10.0, ctl, aft)
783	        f_before, f_after = mean_freq(s1, max(0.0, ctl - 10.0), ctl), mean_freq(s2, 2.0, aft)
784	        b25, a25, _, _ = removal(n, 4, 25.0, ctl, aft)
785	        ok10 = b10[3] == "triphasic" and a10[3] == "triphasic" and np.nanmean(f_after) < np.nanmean(f_before)
786	        ok25 = all(x == "quiescent" for x in a25[:3])
787	        fig9b[(n, tm)] = ok10 and ok25
788	        print(f"{n}, {tm}: 10 C before {b10} f {f_before}, after {a10} f {f_after}; 25 C after {a25}; "
789	              f"10 C part {ok10}, 25 C part {ok25}")
790	=== cell 60 markdown None
791	**Result: reproduced.** In FGFKQS (the Methods' model and the deposit's script), removing KCa at
792	10 C keeps the network triphasic and slows it (PD 1.061 to 0.904 Hz with the code's timing, 1.067
793	to 0.918 Hz with the Results' timing), and at 25 C all three cells are quiescent after removal.
794	The legend's timing (removal at 4 s, from the initial conditions) and J9U8SQ do not show it.
795	=== cell 61 markdown None
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python3 -c "
import json
nb=json.load(open('voltage_distributions.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
"
```

```
Sat Nov 28 03:08:38 UTC 2026
=== cell 0 markdown None
# Alonso & Marder (2020), membrane potential distributions, from Dryad m31b1h7

Paper: Alonso LM, Marder E (2020), eLife 9:e55470, doi:10.7554/eLife.55470; claims in
`claims/alonso-2020.yaml` (version of record, main text, legends and Methods).

Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811 (the only published version, so the
one pinned), file `alonso_marder_tempcomp_2019_root.zip` (MD5 from Dryad's file list checked on
load; SHA-256 printed below). The models are simulated with the port in `pyloric.py`, compared
with the deposited Java in `reproduce_alonso_2020.ipynb`.

Method (Materials and methods, Membrane potential and current shares distributions): each
temperature simulated from the deposited initial conditions for 30 s at dt = 0.001 ms; the last
10 s used; 5 x 10^5 samples per distribution, so V is kept every 20 steps (0.02 ms). Histograms
in 0.1 mV bins (a plotting choice).

The Methods use 101 temperatures. At dt = 0.001 ms one temperature costs about 1500 simulated
seconds at dt = 0.05 (50 times the steps), about 23 s of the runner's 4 CPUs, so 101
temperatures would take about 40 min. This notebook uses 26 temperatures, 10 to 25 degrees C in
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/alonso-2020.yaml'))
cl=d['claims'] if isinstance(d,dict) else d
for c in cl:
    if c['id'] in ('fig2-lp-spike-amplitude-threshold','fig4-currentscapes-reorganize','fig7-high-temperature-slow-timescales','fig10a-graded-removal','fig10b-complete-removal-differs','intermediate-temperature-failures','fig6s1-crash-mechanisms'):
        print(yaml.safe_dump(c,width=150,sort_keys=False))
EOF
```

```
id: intermediate-temperature-failures
statement: Of the Q10 solutions that met the target at the control temperatures, 2 in 40 did not display the correct activity at temperatures in between.
source: Materials and methods, Finding parameters, paragraph 6
quote: We found that if the system meets the target activity at the control temperatures, in the vast majority of the cases, the models also displayed the
  correct activity for temperatures in between, but there were exceptions (2 in 40 cases).
expected:
- quantity: solutions failing between control temperatures
  value: 2
  tolerance: 0
- quantity: solutions screened
  value: 40
  tolerance: 0
criterion: Testable only if the deposit holds the 40 solutions, including the 2 that were discarded. Each is scored at 15, 20 and 25 degrees C with the
  objective of Equation 6 and screened at the temperatures in between (1 degree steps from 10 to 25 degrees C, as in Figure 1C) with the network classification.
  Reproduced when 2 of the 40 fail between control temperatures and none of the other 38 do.

id: fig2-lp-spike-amplitude-threshold
statement: In the LP cell of the model of Figure 2, spike amplitude decreases and the spike threshold depolarizes as temperature rises from 10 to 25 degrees
  C.
source: Figure 2; Results, Changes in membrane potential over temperature, paragraph 1
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; f=$(ls paper/*.md paper/*.txt 2>/dev/null | head -1); echo $f; grep -n -i "remov\|search space\|uniform\|between 0 and\|\[0,\|threshold" $f | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 225,250p paper/10.7554-elife.55470.txt; echo ----; sed -n 405,445p paper/10.7554-elife.55470.txt; echo ----; sed -n 715,735p paper/10.7554-elife.55470.txt; echo; sed -n 490,497p paper/10.7554-elife.55470.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/alonso-2020; python3 - <<'EOF'
import zipfile
z=zipfile.ZipFile('/tmp/dryad/m31b1h7/94811/alonso_marder_tempcomp_2019_root.zip')
for i in z.infolist():
    if '__MACOSX' not in i.filename: print(i.filename, i.file_size)
for n in z.namelist():
    if 'remove' in n and n.endswith('.py') and '__MACOSX' not in n:
        print('=====',n); print(z.read(n).decode())
    if 'README' in n.upper() and '__MACOSX' not in n:
        print('=====',n); print(z.read(n).decode()[:3000])
EOF
```

```
alonso_marder_tempcomp_2019_root/ 0
alonso_marder_tempcomp_2019_root/.DS_Store 14340
alonso_marder_tempcomp_2019_root/compilejava.py 198
alonso_marder_tempcomp_2019_root/parameters_and_ci/ 0
alonso_marder_tempcomp_2019_root/parameters_and_ci/.DS_Store 6148
alonso_marder_tempcomp_2019_root/parameters_and_ci/cis_network.txt 106
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-0SHNMD.score.18.6198193193.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-2RO5K6.score.13.9094188223.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-4R2719.score.26.8426738694.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-4X6W66.score.32.736714734.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-71G6LA.score.44.0018579077.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-72TVF2.score.16.1275919617.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-B7SD0L.score.21.7288155631.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-CG4J30.score.10.2328432089.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-ED50XO.score.28.0070621408.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-EF84RN.score.19.4239593022.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-FGFKQS.score.18.291669674.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-G7P2WE.score.17.175833658.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-H5AIZR.score.11.2475822913.txt 3309
alonso_marder_tempcomp_2019_root/parameters_and_ci/p-HX40PF.score.25.7133642866.txt 3309
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; PY=../../executed/alonso-2020/.venv/bin/python; $PY - <<'EOF'
import numpy as np, pyloric as P, time
Z=P.open_zip(P.read_zip_bytes()); M=P.load_models(Z); CI=P.load_ci(Z)
for n,T in [("G7P2WE",35.0),("J9U8SQ",34.0)]:
    s=P.simulate(M[n],T,40.0,CI,rec_every=20)
    bad=np.where(~np.isfinite(s.rec).all(axis=1))[0]
    print(n,T,'first NaN at', bad[0]*s.rec_dt if len(bad) else None, 's')
EOF
```

```
G7P2WE 35.0 first NaN at 0.10300000000000001 s
J9U8SQ 34.0 first NaN at 0.41400000000000003 s
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; python3 - <<'EOF'
import re
s=open('pyloric.py').read()
s=s.replace("""  whose spikes peak well above 0 mV and whose slow waves stay below the -50 mV slow-wave threshold
  of the Methods; a variant at 0 mV is computed where the claims rest on it).""","""  whose spikes mostly peak above 0 mV and whose slow waves stay below the -50 mV slow-wave threshold
  of the Methods). The main notebook repeats the runs at 10 and 25 C and the graded removals of
  fig10a-graded-removal with a 0 mV threshold, as a variant; in some models the spikes peak below
  0 mV at 25 C, which that variant misses.""")
s=s.replace("""def run_fixed(task):
    \"\"\"task = (key, p, y0, temp, seconds, drop). Simulates at a fixed temperature and returns, for
    the window after `drop` seconds, the spike times and upward slow-wave crossings of each cell
    (times from the window start), the four classes, and the final state.\"\"\"
    key, p, y0, temp, seconds, drop = task
    s = simulate(p, temp, seconds, y0)""","""def run_fixed(task):
    \"\"\"task = (key, p, y0, temp, seconds, drop[, thr]). Simulates at a fixed temperature and returns,
    for the window after `drop` seconds, the spike times and upward slow-wave crossings of each cell
    (times from the window start), the four classes, and the final state. `thr` is the spike
    threshold (SPIKE_THRESHOLD when not given).\"\"\"
    key, p, y0, temp, seconds, drop = task[:6]
    thr = task[6] if len(task) > 6 else SPIKE_THRESHOLD
    s = simulate(p, temp, seconds, y0, thr=thr)""")
s=s.replace("""def run_states(task):""","""def run_removal(task):
    \"\"\"task = (key, p, y0, temp, control, current, fraction, seconds, drop). Simulates `control`
    seconds with every conductance intact, then scales one maximal conductance in all three cells
    and continues from the final state for `seconds`, as the deposit's
    integratePyloricSQ10s_remove_gA_onesteps_twotemps_RK4.py does (the Results, Figure 9: "20 s in
    control conditions and then IA was completely removed for the next 20 s"). Returns the four
    classes over the perturbed run after `drop` seconds.\"\"\"
    key, p, y0, temp, control, current, fraction, seconds, drop = task
    s1 = simulate(p, temp, control, y0)
    s2 = simulate(scaled(p, current, fraction), temp, seconds, s1.final)
    return dict(key=key, temp=temp, classes=classify(s2, drop, seconds))


def run_states(task):""")
s=s.replace("""def peaks_after(V, idx, n):""","""def slow_wave_bursts(V, spikes, dt, gap=BURST_GAP, level=SLOW_WAVE):
    \"\"\"Bursts bounded by the slow wave: for each burst of `spikes` (s, grouped with the 200 ms
    threshold), the sample indices of the last upward crossing of `level` before its first spike and
    of the first downward crossing after its last spike, in the trace V sampled every dt s (the
    Methods' -50 mV slow-wave threshold, Classification scheme). Bursts whose crossings fall outside
    the trace are dropped.\"\"\"
    up = np.where((V[:-1] < level) & (V[1:] >= level))[0] + 1
    down = np.where((V[:-1] >= level) & (V[1:] < level))[0] + 1
    out = []
    for s, e, k in zip(*bursts(spikes, gap)):
        i, j = int(s / dt), int(e / dt)
        u = up[up <= i]
        d = down[down > j]
        if len(u) and len(d):
            out.append((int(u[-1]), int(d[0]), int(k)))
    return out


def spike_region_start(hist, edges, frac, smooth=10):
    \"\"\"fig2-lp-spike-amplitude-threshold, threshold reading (b): the voltage at which the
    distribution's spike region begins, read as the upper edge of the densely occupied part of the
    distribution, the highest voltage whose occupancy (smoothed over `smooth` bins) is at least
    `frac` of the largest occupancy; above it the cell is only visited during spikes (an
    assumption: neither the paper nor the claims file says how the point is located).\"\"\"
    h = np.convolve(hist, np.ones(smooth) / smooth, mode="same")
    k = np.where(h >= frac * h.max())[0]
    centres = 0.5 * (edges[:-1] + edges[1:])
    return float(centres[k[-1]]) if len(k) else np.nan


def peaks_after(V, idx, n):""")
open('pyloric.py','w').write(s)
EOF
grep -n "updated every 20 steps" pyloric.py
```

```
27:  and the temperature factors are updated every 20 steps (1 ms), at the temperature of the middle
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; PY=../../executed/alonso-2020/.venv/bin/python; time $PY - <<'EOF'
import numpy as np, pyloric as P
Z=P.open_zip(P.read_zip_bytes()); M=P.load_models(Z); CI=P.load_ci(Z)
T=[10.0,14.8,19.6,25.0]
out=P.pmap(P.run_distribution,[(("G",t),M["G7P2WE"],CI,t,30.0,10.0,0.001,20) for t in T])
edges=-100+0.1*np.arange(1601)
for r in out:
    c=r['cells'][1]; h=c['hist']
    print(r['temp'], 'thr_a',round(c['thr'],2),'peak',round(c['peak'],1),'vmax',round(c['vmax'],1), [P.spike_region_start(h,edges,f) for f in (0.002,0.005,0.01,0.02,0.05)])
    # print coarse histogram above -60
    cc=0.5*(edges[:-1]+edges[1:])
    sel=(cc>-60)&(cc<0)
    hh=h[sel].reshape(-1,20).sum(1)
    print('   2mV bins -60..0:',hh.astype(int).tolist())
EOF
```

```
10.0 thr_a -27.79 peak 13.4 vmax 16.7 [15.550000000000004, 12.150000000000006, -30.349999999999994, -33.05, -36.14999999999999]
   2mV bins -60..0: [0, 0, 0, 2555, 169572, 67052, 29695, 47545, 44081, 44660, 37035, 19190, 10274, 5714, 3391, 2175, 1523, 1180, 937, 809, 732, 656, 619, 587, 555, 545, 541, 519, 536, 559]
14.8 thr_a -28.43 peak 9.3 vmax 13.6 [13.150000000000006, 7.650000000000006, -28.15, -31.25, -34.449999999999996]
   2mV bins -60..0: [0, 0, 0, 1958, 164596, 60565, 32262, 22265, 23759, 46885, 68772, 29379, 14527, 7837, 4568, 2894, 2013, 1498, 1214, 1027, 922, 834, 782, 722, 707, 709, 673, 697, 710, 770]
19.6 thr_a -28.6 peak 3.6 vmax 7.6 [7.750000000000007, 6.450000000000003, 2.3500000000000085, 1.6500000000000057, -30.849999999999994]
   2mV bins -60..0: [0, 0, 0, 41833, 113606, 57091, 35444, 27191, 26883, 19321, 21100, 72432, 34008, 13925, 7479, 4565, 3080, 2256, 1789, 1513, 1307, 1196, 1104, 1072, 1022, 1033, 1057, 1110, 1261, 1482]
25.0 thr_a -27.5 peak -6.8 vmax -1.8 [-1.8499999999999943, -3.249999999999993, -7.049999999999997, -7.449999999999996, -26.549999999999997]
   2mV bins -60..0: [0, 0, 0, 79267, 92126, 44778, 31305, 54061, 53811, 15122, 9244, 5659, 4818, 12196, 43944, 13485, 7555, 5023, 3792, 3072, 2663, 2442, 2383, 2441, 2830, 4716, 1940, 652, 648, 27]

real	2m31.249s
user	9m54.281s
sys	0m0.703s
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; python3 - <<'EOF'
s=open('pyloric.py').read()
old='''def spike_region_start(hist, edges, frac, smooth=10):
    """fig2-lp-spike-amplitude-threshold, threshold reading (b): the voltage at which the
    distribution's spike region begins, read as the upper edge of the densely occupied part of the
    distribution, the highest voltage whose occupancy (smoothed over `smooth` bins) is at least
    `frac` of the largest occupancy; above it the cell is only visited during spikes (an
    assumption: neither the paper nor the claims file says how the point is located)."""
    h = np.convolve(hist, np.ones(smooth) / smooth, mode="same")
    k = np.where(h >= frac * h.max())[0]
    centres = 0.5 * (edges[:-1] + edges[1:])
    return float(centres[k[-1]]) if len(k) else np.nan'''
new='''def spike_region_start(hist, edges, frac, smooth=10, below=SPIKE_THRESHOLD):
    """fig2-lp-spike-amplitude-threshold, threshold reading (b): the voltage at which the
    distribution's spike region begins, read as the upper edge of the densely occupied part of the
    distribution: the highest voltage below `below` whose occupancy (smoothed over `smooth` bins of
    0.1 mV) is at least `frac` of the largest occupancy. Above it the cell passes only during spikes.
    The search stops at the spike detection level, which every spike crosses, so that the dwell
    near the spike peaks is not taken for the slow wave. An assumption: neither the paper nor the
    claims file says how the point is located; the notebook gives three values of `frac`."""
    h = np.convolve(hist, np.ones(smooth) / smooth, mode="same")
    centres = 0.5 * (edges[:-1] + edges[1:])
    k = np.where((h >= frac * h.max()) & (centres < below))[0]
    return float(centres[k[-1]]) if len(k) else np.nan'''
assert old in s
s=s.replace(old,new)
open('pyloric.py','w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; cat > $TMPDIR/nbedit.py <<'EOF'
import json, sys
def load(p): return json.load(open(p))
def save(nb,p):
    json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
def src(c): return ''.join(c['source'])
def setsrc(c, text):
    lines = text.split('\n')
    c['source'] = [l + '\n' for l in lines[:-1]] + [lines[-1]]
def find(nb, start):
    hits=[i for i,c in enumerate(nb['cells']) if src(c).lstrip().startswith(start) or start in (c.get('metadata',{}).get('tags') or [])]
    assert len(hits)==1, (start, hits); return hits[0]
def newcell(kind, text, tags=None):
    c={'cell_type':kind,'metadata':{},'source':[]}
    if tags: c['metadata']['tags']=tags
    if kind=='code': c['outputs']=[]; c['execution_count']=None
    setsrc(c,text); return c
EOF
head -c 600 voltage_distributions.ipynb; tail -c 300 voltage_distributions.ipynb
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "497bb76f",
   "metadata": {},
   "source": [
    "# Alonso & Marder (2020), membrane potential distributions, from Dryad m31b1h7\n",
    "\n",
    "Paper: Alonso LM, Marder E (2020), eLife 9:e55470, doi:10.7554/eLife.55470; claims in\n",
    "`claims/alonso-2020.yaml` (version of record, main text, legends and Methods).\n",
    "\n",
    "Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811 (the only published version, so the\n",
    "one pinned), file `alonso_marder_tempcomp_2019_root.zip` (MD5 from Dryad's file list checked on\n",ak memory \"\n",
    "      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")"
   ]
  }
 ],
 "metadata": {
  "jupytext": {
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; cat >> $TMPDIR/nbedit.py <<'EOF'
import uuid
_old_newcell = newcell
def newcell(kind, text, tags=None):
    c = _old_newcell(kind, text, tags); c['id'] = uuid.uuid4().hex[:8]
    return {k: c[k] for k in ['cell_type','id','metadata'] + (['execution_count','outputs'] if kind=='code' else []) + ['source']}
def save(nb,p):
    open(p,'w').write(json.dumps(nb, indent=1, ensure_ascii=False) + '\n')
EOF
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/voltage_distributions.ipynb'
nb=load(p)
c=nb['cells'][0]; t=src(c)
t=t.replace("| fig2-lp-spike-amplitude-threshold | tested (26 of 101 temperatures) |","| fig2-lp-spike-amplitude-threshold | tested (26 of 101 temperatures) |")
setsrc(c,t)
i=find(nb,"## fig2-lp-spike-amplitude-threshold")
t=src(nb['cells'][i]).replace("""Threshold
reading (b), where the distribution's spike region begins, is not computed (see the summary).""","""Threshold
reading (b), where the distribution's spike region begins: neither the paper nor the claims file
says how that point is located, so it is read as the upper edge of the densely occupied part of
the distribution (`pyloric.spike_region_start`): the highest voltage below the -20 mV spike
detection level whose occupancy, smoothed over 1 mV, is at least a fraction of the largest
occupancy. Above it the cell passes only during spikes. The fraction is a choice; 2%, 5% and 10%
are shown, 5% as the main one (an assumption).""")
setsrc(nb['cells'][i],t)
j=find(nb,"claim:fig2-lp-spike-amplitude-threshold")
c=nb['cells'][j]; t=src(c)
t=t.replace('''print(lp.round(2).to_string())''','''for frac in (0.02, 0.05, 0.10):
    lp[f"threshold_b_{int(100 * frac)}"] = [P.spike_region_start(DIST[("G7P2WE", T)]["cells"][1]["hist"], -100 + 0.1 * np.arange(1601), frac)
                                         for T in T26]
print(lp.round(2).to_string())''')
t=t.replace('''print(f"\\nSpearman with temperature: amplitude (a) {r_amp_a:.3f}, upper envelope (b) {r_amp_b:.3f}, threshold (a) {r_thr_a:.3f}")''','''r_thr_b = {k: stats.spearmanr(lp.index, lp[k], nan_policy="omit")[0] for k in ("threshold_b_2", "threshold_b_5", "threshold_b_10")}
print(f"\\nSpearman with temperature: amplitude (a) {r_amp_a:.3f}, upper envelope (b) {r_amp_b:.3f}, threshold (a) {r_thr_a:.3f}")
print("Spearman with temperature, threshold (b) at fractions 2%, 5%, 10% of the largest occupancy:", {k: round(v, 3) for k, v in r_thr_b.items()})
for k in ("threshold_b_2", "threshold_b_5", "threshold_b_10"):
    print(f"   {k}: from {lp[k].iloc[0]:.1f} to {lp[k].iloc[-1]:.1f} mV (range {lp[k].min():.1f} to {lp[k].max():.1f}); "
          f"at the -20 mV search limit in {int((lp[k] > -20.2).sum())} of {len(lp)} temperatures")''')
t=t.replace('''ax[1].plot(lp.index, lp.amp_a, "o-", label="amplitude (a)"); ax[1].plot(lp.index, lp.threshold_a, "o-", label="threshold (a)")''','''ax[1].plot(lp.index, lp.amp_a, "o-", label="amplitude (a)"); ax[1].plot(lp.index, lp.threshold_a, "o-", label="threshold (a)")
ax[1].plot(lp.index, lp.threshold_b_5, "o-", label="threshold (b), 5%")''')
setsrc(c,t)
save(nb,p)
print(t)
EOF
```

```
lp = pd.DataFrame([dict(T=T, amp_a=DIST[("G7P2WE", T)]["cells"][1]["amp"], envelope_b=DIST[("G7P2WE", T)]["cells"][1]["vmax"],
                        threshold_a=DIST[("G7P2WE", T)]["cells"][1]["thr"], spikes=DIST[("G7P2WE", T)]["cells"][1]["spikes"],
                        peak=DIST[("G7P2WE", T)]["cells"][1]["peak"], mean_V=DIST[("G7P2WE", T)]["cells"][1]["mean"]) for T in T26]).set_index("T")
for frac in (0.02, 0.05, 0.10):
    lp[f"threshold_b_{int(100 * frac)}"] = [P.spike_region_start(DIST[("G7P2WE", T)]["cells"][1]["hist"], -100 + 0.1 * np.arange(1601), frac)
                                         for T in T26]
print(lp.round(2).to_string())
r_amp_a = stats.spearmanr(lp.index, lp.amp_a)[0]
r_amp_b = stats.spearmanr(lp.index, lp.envelope_b)[0]
r_thr_a = stats.spearmanr(lp.index, lp.threshold_a, nan_policy="omit")[0]
r_thr_b = {k: stats.spearmanr(lp.index, lp[k], nan_policy="omit")[0] for k in ("threshold_b_2", "threshold_b_5", "threshold_b_10")}
print(f"\nSpearman with temperature: amplitude (a) {r_amp_a:.3f}, upper envelope (b) {r_amp_b:.3f}, threshold (a) {r_thr_a:.3f}")
print("Spearman with temperature, threshold (b) at fractions 2%, 5%, 10% of the largest occupancy:", {k: round(v, 3) for k, v in r_thr_b.items()})
for k in ("threshold_b_2", "threshold_b_5", "threshold_b_10"):
    print(f"   {k}: from {lp[k].iloc[0]:.1f} to {lp[k].iloc[-1]:.1f} mV (range {lp[k].min():.1f} to {lp[k].max():.1f}); "
          f"at the -20 mV search limit in {int((lp[k] > -20.2).sum())} of {len(lp)} temperatures")
print(f"amplitude (a) from {lp.amp_a.iloc[0]:.1f} to {lp.amp_a.iloc[-1]:.1f} mV; envelope from {lp.envelope_b.iloc[0]:.1f} to "
      f"{lp.envelope_b.iloc[-1]:.1f} mV; threshold (a) from {lp.threshold_a.iloc[0]:.1f} to {lp.threshold_a.iloc[-1]:.1f} mV")
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
edges = -100 + 0.1 * np.arange(1601)
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/ramps.ipynb'
nb=load(p)
c=nb['cells'][0]; t=src(c)
old="""The deposit holds no ramp code; the temperature is updated at every step, linearly in time, and
each ramp starts from the deposited initial conditions at its first temperature (assumptions)."""
assert old in t
t=t.replace(old,"""The deposit holds no ramp code; the temperature changes linearly in time, the temperature
factors are updated every 20 steps (1 ms) at the temperature of the middle of those steps, and
each ramp starts from the deposited initial conditions at its first temperature (assumptions;
`pyloric.py`).""")
t=t.replace("""The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
reading, would add about 35 min to this notebook (38 models x 3600 s at about 67 simulated
seconds per second on 4 CPUs, measured on a subset); it is not run, and that claim is tested
in the main notebook on its variant, the 16 fixed temperatures.""","""The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
reading, and the second ramp reading of fig8-up-down-ramps (10 to 25 degrees C over 60 min and
back, every model) are not run: the cell timed in the fig8-up-down-ramps section estimates them
from a subset. figs3-duty-cycle-variable-across-models is tested in the main notebook on its
variant, the 16 fixed temperatures.""")
setsrc(c,t)
i=find(nb,"## Data check and the runs")
setsrc(nb['cells'][i],"""## Data check and the runs

The runs below take about 35 min on 4 otherwise idle CPUs (about 67 simulated seconds per second,
measured on a subset while preparing) and about an hour when the CPUs are shared; the run time
is printed.""")
i=find(nb,"claim:fig8-up-down-ramps")
timing = newcell('code', '''# The second ramp reading (10 to 25 C over 60 min and back, 7200 s per model) timed on a subset:
# four models, 120 s of each leg, run as the full reading would be (4 processes).
t0 = time.time()
sub = P.pmap(P.run_ramp, [(n, MODELS[n], CI, [(10.0, 10.5, 120.0), (10.5, 10.0, 120.0)]) for n in NAMES[:4]])
rate = 4 * 240.0 / (time.time() - t0)
print(f"subset: {rate:.0f} simulated seconds per second on 4 processes")
print(f"estimate for the second reading, 38 models x 7200 s: {38 * 7200 / rate / 60:.0f} min; "
      f"for the up legs alone (the main reading of figs3-duty-cycle-variable-across-models), 38 x 3600 s: {38 * 3600 / rate / 60:.0f} min")
print(f"this notebook has run for {(time.time() - T_START) / 60:.0f} min so far; the limit for a notebook is 60 min")''')
nb['cells'].insert(i+1, timing)
c=nb['cells'][i-1]; t=src(c)
t=t.replace("""The second ramp reading (10 to 25 degrees C over 60 min and back) is not run here (see the
summary).""","""The second ramp reading (10 to 25 degrees C over 60 min and back) is not run; the cell after the
comparison times it on a subset.""")
setsrc(c,t)
save(nb,p)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/ramps.ipynb'
nb=load(p)
for c in nb['cells']:
    if src(c).startswith("# The second ramp reading"): c['metadata']['tags']=['claim:fig8-up-down-ramps']
save(nb,p)

p='entries/alonso-2020/reproduce_alonso_2020.ipynb'
nb=load(p)
# (b) java check
i=[k for k,c in enumerate(nb['cells']) if src(c).startswith("def java_check")][0]
setsrc(nb['cells'][i], '''def java_check(name="4X6W66", seconds=3, temp=18):
    """Runs the deposited Java and the port from the deposited initial conditions; returns the largest
    difference in V over the samples where both are finite, and the first sample with NaN in each."""
    if not (shutil.which("javac") and shutil.which("java")):
        print("no Java compiler here; comparison not run")
        return None
    with tempfile.TemporaryDirectory() as d:
        src = [m for m in Z.namelist() if m.startswith(P.ROOT + "standaloneCodePyloricTempComp/") and m.endswith(".java")]
        pkg = Path(d) / "standaloneCodePyloricTempComp"
        pkg.mkdir()
        for m in src:
            (pkg / Path(m).name).write_bytes(Z.read(m))
        (Path(d) / "ci.txt").write_bytes(Z.read(P.ROOT + "parameters_and_ci/cis_network.txt"))
        (Path(d) / "p.txt").write_bytes(Z.read(FILES[name]))
        subprocess.run(["javac"] + [str(pkg / Path(m).name) for m in src], check=True, cwd=d)
        out = subprocess.run(["java", "-cp", d, "standaloneCodePyloricTempComp.integratePyloricNetwork_slow_full_temp_sameq10s_rk4",
                              "ci.txt", "p.txt", str(seconds), str(temp), "0.05"], cwd=d, capture_output=True,
                             text=True, check=True).stdout
    j = np.array([[float(x) for x in line.split()] for line in out.strip().splitlines()])
    s = P.simulate(MODELS[name], temp, seconds, CI, rec_every=1)
    n = min(len(j), len(s.rec))
    both = np.isfinite(j[:n]).all(axis=1) & np.isfinite(s.rec[:n]).all(axis=1)
    first_nan = [int(np.argmax(~np.isfinite(x[:n]).all(axis=1))) if (~np.isfinite(x[:n]).all(axis=1)).any() else None for x in (j, s.rec)]
    diff = np.abs(j[:n][both] - s.rec[:n][both]).max()
    print(f"{name}, {seconds} s at {temp} C: Java {j.shape}, port {s.rec.shape}; largest difference in V where both are finite "
          f"{diff:.2e} mV over {int(both.sum())} samples; first sample with NaN: Java {first_nan[0]}, port {first_nan[1]}")
    return diff

java_diff = java_check()
# Above the working range: a model that stays finite at 25 C, and the two runs that diverge in the port (Figure 7A shows
# J9U8SQ active at 34 C).
java_hot = {k: java_check(*k) for k in [("J9U8SQ", 3, 25), ("G7P2WE", 0.3, 35), ("J9U8SQ", 0.6, 34)]}''')
t=src(nb['cells'][i-1]).replace("""run for 3 s at 18 degrees C on one model, when a Java compiler is installed; the port's voltage
traces are compared with its output. The port was also checked this way while preparing.""","""run for 3 s at 18 degrees C on one model, when a Java compiler is installed; the port's voltage
traces are compared with its output. It is also compared above 18 degrees C: J9U8SQ for 3 s at 25
degrees C, and the two runs whose integration diverges in the port, G7P2WE at 35 degrees C and
J9U8SQ at 34 degrees C, over their first 0.3 and 0.6 s.""")
setsrc(nb['cells'][i-1],t)
# (a) parameters vs search space finding
i=find(nb,'finding-shared-conductances')
md=newcell('markdown','''### Parameters against the Methods' search space

The Methods (Finding parameters) list the search space: gNa and gKCa in [0, 10^3] uS, gCaT, gCaS,
gA, gKd and gH in [0, 10^2], gleak in [0, 10], tau_Ca in [0, 2 x 10^3] ms and every synaptic
conductance in [0, 5 x 10^-2] uS. The deposited values are compared with these bounds, tau_Ca both as
stored in the files and as the Java uses it (times 10).''')
fc=newcell('code','''# Deposited parameters against the search space of the Methods (Finding parameters).
BOUNDS = {"Na": 1e3, "CaT": 1e2, "CaS": 1e2, "A": 1e2, "KCa": 1e3, "Kd": 1e2, "H": 1e2, "Leak": 10}
for k, cur in enumerate(P.CURRENTS):
    v = np.array([P.conductances(MODELS[n])[:, k] for n in NAMES])
    print(f"g{cur:5s} bound {BOUNDS[cur]:7.0f}: deposited {v.min():8.2f} to {v.max():8.2f}; models with a cell above the bound "
          f"{int((v > BOUNDS[cur]).any(axis=1).sum())} of {len(NAMES)}")
tc = np.array([MODELS[n][[35, 72, 109]] for n in NAMES])
print(f"tau_Ca  bound 2000 ms: as stored {tc.min():.1f} to {tc.max():.1f} (above: {int((tc > 2000).any(axis=1).sum())} models); "
      f"as the Java uses it (x 10) {10 * tc.min():.0f} to {10 * tc.max():.0f} ms (above: {int((10 * tc > 2000).any(axis=1).sum())} models)")
gs = np.array([MODELS[n][111:118] for n in NAMES])
print(f"g syn   bound 0.05: deposited {gs.min():.4f} to {gs.max():.4f}; models with a synapse above the bound {int((gs > 0.05).any(axis=1).sum())} of {len(NAMES)}")''', tags=['finding-parameters-outside-search-space'])
nb['cells'][i+1:i+1]=[md,fc]
save(nb,p)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/reproduce_alonso_2020.ipynb'
nb=load(p)
# (c) intermediate
i=find(nb,"## intermediate-temperature-failures")
t=src(nb['cells'][i]).replace("""the count of models above is all that can be said.""","""the count of models above is all that can be said. The cell below prints what the deposit says
about its models: the README's lines that mention models or solutions, and the score in each file
name against the models that fail between 10 and 25 degrees C.""")
setsrc(nb['cells'][i],t)
ic=newcell('code','''readme = Z.read(P.ROOT + "README.txt").decode()
print("README lines that mention models, solutions, scores or counts:")
for line in readme.splitlines():
    if re.search(r"model|solution|score|discard|36|38|40", line, re.I):
        print("   ", line.strip()[:160])
sc = pd.Series({n: P.score_of(FILES[n]) for n in NAMES}).sort_values()
print("\\nscore in the file name, per model (ascending):")
print(sc.round(1).to_string())
print("\\nmodels not triphasic at some temperature from 10 to 25 C:", {n: round(sc[n], 1) for n in per_model[per_model > 0].index})
print("median score %.1f; the three largest: %s" % (sc.median(), sc.round(1).tail(3).to_dict()))''', tags=['claim:intermediate-temperature-failures'])
nb['cells'].insert(i+1, ic)
save(nb,p)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/reproduce_alonso_2020.ipynb'
nb=load(p)
i=find(nb,"## fig4-currentscapes-reorganize")
t=src(nb['cells'][i]).replace("""WWZ3CN, the same 3 s windows. A burst runs from its first to its last spike crossing (bursts
grouped with the 200 ms threshold).""","""WWZ3CN, the same 3 s windows. Where a burst starts and ends is open. Two bounds are run: (spikes)
from its first to its last spike crossing (bursts grouped with the 200 ms threshold), and (slow
wave) from the last upward crossing of the Methods' -50 mV slow-wave threshold before its first
spike to the first downward crossing after its last spike. Every leak reversal potential is
-50 mV, so the leak current is inward only below -50 mV, which the spike bounds exclude.""")
setsrc(nb['cells'][i],t)
j=find(nb,"claim:fig4-currentscapes-reorganize")
setsrc(nb['cells'][j],'''def burst_part_shares(r, name, c, frac, bounds="spikes"):
    cur = cell_currents(r, name, c)
    out_sh, in_sh = P.shares(cur)
    if bounds == "spikes":
        b = [(int(s / r["dt"]), int(e / r["dt"]), k) for s, e, k in zip(*P.bursts(r["spikes"][c]))]
    else:
        b = P.slow_wave_bursts(r["states"][:, 13 * c], r["spikes"][c], r["dt"])
    res = {"in start": [], "in end": [], "out start": [], "out end": []}
    for i, j, k in b:
        if k < 2:
            continue
        w = max(1, int((j - i) * frac))
        res["in start"].append(in_sh[:, i:i + w].mean(axis=1)); res["in end"].append(in_sh[:, j - w:j].mean(axis=1))
        res["out start"].append(out_sh[:, i:i + w].mean(axis=1)); res["out end"].append(out_sh[:, j - w:j].mean(axis=1))
    return {k: pd.Series(np.mean(v, axis=0), index=P.CURRENTS + ["Syn"]) for k, v in res.items()}, len(res["in start"])

fig4 = {}
for bounds in ("spikes", "slow wave"):
    for frac, label in [(1 / 3, "a, thirds"), (0.2, "b, 20%")]:
        sh = {(c, T): burst_part_shares(ST[("WWZ3CN", T)], "WWZ3CN", c, frac, bounds) for c in range(3) for T in (10.0, 25.0)}
        pd10, pd25 = sh[(0, 10.0)][0], sh[(0, 25.0)][0]
        with np.errstate(invalid="ignore", divide="ignore"):
            leak10 = pd10["in end"]["Leak"] / pd10["in start"]["Leak"]
            leak25 = pd25["in end"]["Leak"] / pd25["in start"]["Leak"]
        a10 = pd10["out start"]["A"] / pd10["out end"]["A"]
        a25 = pd25["out start"]["A"] / pd25["out end"]["A"]
        kca = {P.CELLS[c]: (sh[(c, 10.0)][0]["out end"]["KCa"], sh[(c, 25.0)][0]["out end"]["KCa"]) for c in range(3)}
        inc = {k: v[1] - v[0] for k, v in kca.items()}
        print(f"bounds ({bounds}), reading ({label}); bursts used per cell and temperature:", {f"{P.CELLS[c]} {int(T)}": sh[(c, T)][1] for c, T in sh})
        print(f"  PD leak inward share, end over start: 10 C {leak10:.3f} (start {pd10['in start']['Leak']:.4f}, end {pd10['in end']['Leak']:.4f}); "
              f"25 C {leak25:.3f} (start {pd25['in start']['Leak']:.4f}, end {pd25['in end']['Leak']:.4f})")
        print(f"  PD A outward share, start over end: 10 C {a10:.3f}; 25 C {a25:.3f}")
        print("  KCa outward share at the end of bursts (10 C, 25 C):", {k: tuple(round(x, 4) for x in v) for k, v in kca.items()})
        print("  increase:", {k: round(v, 4) for k, v in inc.items()})
        parts = {"leak": bool(leak25 < leak10), "A": bool((0.8 <= a10 <= 1.25) and a25 > a10),
                 "KCa": bool(all(v > 0 for v in inc.values()) and inc["LP"] > inc["PD"] and inc["PY"] > inc["PD"])}
        print("  parts that hold:", parts)
        fig4[(bounds, label)] = parts''')
save(nb,p)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/reproduce_alonso_2020.ipynb'
nb=load(p)
i=find(nb,"## fig6-crash-different-mechanisms")
t=src(nb['cells'][i]).replace("""FGFKQS and 71G6LA at 10, 25 and 30 degrees C. Classes from the 40 s runs (last 30 s); the
dominant currents from 13 s runs (last 3 s), largest mean inward and outward share in PD.""","""FGFKQS and 71G6LA at 10, 25 and 30 degrees C. Classes from the 40 s runs (last 30 s); the
dominant currents, the largest mean inward and outward share in PD, over the last 3 s of the same
40 s run (the run is deterministic, so it is repeated with the states recorded). The last 3 s of
a 13 s run, as the deposit's currentscape script takes them, are shown as a variant.""")
setsrc(nb['cells'][i],t)
j=find(nb,"claim:fig6-crash-different-mechanisms")
t=src(nb['cells'][j])
t=t.replace('''    r30 = states(n, 30.0)
    cl = {T: SCAN[(n, T)]["classes"] for T in (10.0, 25.0, 30.0)}
    pair = dominant_pair(r30, n, 0)''','''    r30 = states(n, 30.0, seconds=40.0)
    cl = {T: SCAN[(n, T)]["classes"] for T in (10.0, 25.0, 30.0)}
    pair = dominant_pair(r30, n, 0)
    pair13 = dominant_pair(states(n, 30.0), n, 0)''')
t=t.replace('''    print(n, cl, f"; PD spikes in the 30 s analysed at 30 C: {nspk}; PD dominant inward, outward at 30 C: {pair}")''','''    print(n, cl, f"; PD spikes in the 30 s analysed at 30 C: {nspk}; PD dominant inward, outward at 30 C: {pair} "
          f"(variant, last 3 s of a 13 s run: {pair13})")''')
setsrc(nb['cells'][j],t)
i=find(nb,"## fig6s1-crash-mechanisms")
t=src(nb['cells'][i]).replace("""in the deposit; B7SDOL is B7SD0L. The seven are tested.""","""in the deposit; B7SDOL is B7SD0L. The seven are tested. Each is taken at its crash temperature
from the 40 s runs, and the dominant currents are taken over the last 3 s of the same 40 s run;
the last 3 s of a 13 s run are a variant.""")
setsrc(nb['cells'][i],t)
j=find(nb,"claim:fig6s1-crash-mechanisms")
setsrc(nb['cells'][j],'''s6 = [M[n] for n in METHODS_NAMES["Figure 6-S1"] if isinstance(M[n], str)]
print("models tested:", s6)
pat, pat13 = {}, {}
for n in s6:
    T = crashT[n]
    if T is None:
        print(f"{n}: triphasic at every temperature up to 35 C"); continue
    r = states(n, T, seconds=40.0)
    pat[n] = tuple(dominant_pair(r, n, c) for c in range(3))
    pat13[n] = tuple(dominant_pair(states(n, T), n, c) for c in range(3))
    print(f"{n}: crashes at {T:.0f} C, classes {SCAN[(n, T)]['classes']}; dominant (inward, outward) per cell {pat[n]}; "
          f"variant (13 s run) {pat13[n]}")
distinct = len(set(pat.values()))
print(f"\\nmodels that crash below 35 C: {sum(crashT[n] is not None and crashT[n] < 35 for n in s6)} of {len(s6)}; "
      f"distinct patterns: {distinct} (variant, 13 s runs: {len(set(pat13.values()))})")
print("models sharing a pattern:", [(a, b) for a, b in combinations(pat, 2) if pat[a] == pat[b]])
print("variant, models sharing a pattern:", [(a, b) for a, b in combinations(pat13, 2) if pat13[a] == pat13[b]])''')
save(nb,p)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/reproduce_alonso_2020.ipynb'
nb=load(p)
i=find(nb,"## fig7-high-temperature-slow-timescales")
t=src(nb['cells'][i])+"""

Reading (a) is the longest interval without a spike in each cell; reading (b) the dominant period
of the slow voltage: V every 1 ms over the last 30 s of the 40 s run, spikes removed with a 50 ms
median filter (criterion), and the period of the largest peak of the periodogram (resolution
1/30 Hz)."""
setsrc(nb['cells'][i],t)
j=[k for k,c in enumerate(nb['cells']) if src(c).startswith("def longest_gaps")][0]
t=src(nb['cells'][j])
t=t.replace('''for n, T in [("J9U8SQ", 34.0), ("KMNLBC", 30.0), ("FGFKQS", 34.0)]:
    r = SCAN[(n, T)]
    print(f"{n} at {T:.0f} C: classes {r['classes']}; longest interval without a spike per cell (s, 30 s window, edges included): "
          f"{np.round(longest_gaps(r), 2)}")''','''from scipy import ndimage, signal

def slow_periods(name, temp):
    """Reading (b): dominant period (s) of each cell's median-filtered V over the last 30 s of a 40 s run."""
    s = P.simulate(MODELS[name], temp, 40.0, CI, rec_every=20, rec_from=10.0)
    if not s.finite:
        return None
    out = []
    for c in range(3):
        v = ndimage.median_filter(s.rec[:, c], size=51)
        f, pw = signal.periodogram(v - v.mean(), fs=1 / s.rec_dt)
        k = 1 + int(np.argmax(pw[1:]))
        out.append(1 / f[k])
    return out

for n, T in [("J9U8SQ", 34.0), ("KMNLBC", 30.0), ("FGFKQS", 34.0)]:
    r = SCAN[(n, T)]
    per = slow_periods(n, T)
    print(f"{n} at {T:.0f} C: classes {r['classes']}; (a) longest interval without a spike per cell (s, 30 s window, edges included): "
          f"{np.round(longest_gaps(r), 2)}; (b) dominant period of the slow voltage per cell (s): "
          f"{np.round(per, 2) if per is not None else 'not computed, the run diverged'}")''')
nb['cells'][j]['metadata']['tags']=['claim:fig7-high-temperature-slow-timescales']
setsrc(nb['cells'][j],t)
save(nb,p)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python3 - <<'EOF'
s=open('pyloric.py').read()
a=s.index("def run_removal(task):"); b=s.index("def run_states(task):")
s=s[:a]+s[b:]
open('pyloric.py','w').write(s)
EOF
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/reproduce_alonso_2020.ipynb'
nb=load(p)
i=find(nb,"## fig10a-graded-removal")
setsrc(nb['cells'][i],'''## fig10a-graded-removal

> In the model of Figure 10A, reducing gNa to 75% makes LP burst irregularly and the network
> non-triphasic at 10 degrees C but not at 25 degrees C; ...

4X6W66, each of gNa, gKCa, gCaT and gCaS at 100, 75, 50, 25 and 0% in all three cells, at 10 and
25 degrees C; each perturbed run 20 s, the first 10 s dropped (criterion). When the conductance is
changed is open for Figure 10, so two protocols are run:

- (control first) 20 s with every conductance intact from the deposited initial conditions, then
  the perturbed run from the final state. This is the protocol the Results give for the removals
  of Figure 9, in the same section ("the models were simulated for 20 s in control conditions and
  then IA was completely removed for the next 20 s"), and the one of the deposit's removal script
  (integratePyloricSQ10s_remove_gA_onesteps_twotemps_RK4.py: a control run, then the conductance
  scaled and the run continued from its final state). It is the main protocol (an assumption).
- (from t = 0) the perturbed model from the deposited initial conditions, a variant.

The grids are also given with a 0 mV spike threshold (variant).''')
j=find(nb,"claim:fig10a-graded-removal")
setsrc(nb['cells'][j],'''FR = [1.0, 0.75, 0.5, 0.25, 0.0]
CUR10 = {"Na": 0, "KCa": 4, "CaT": 1, "CaS": 2}
# Control runs, 20 s from the initial conditions: the final states of deposit-models at 10 C, and new runs at 25 C.
ctl25 = P.pmap(P.run_fixed, [(n, MODELS[n], CI, 25.0, 20.0, 10.0) for n in NAMES])
CTRL = {(r["key"], 10.0): r["final"] for r in r10}
CTRL.update({(r["key"], 25.0): r["final"] for r in ctl25})

def grid10a(start, thr=P.SPIKE_THRESHOLD):
    y0 = (lambda T: CTRL[("4X6W66", T)]) if start == "control first" else (lambda T: CI)
    tasks = [((cur, fr, T), P.scaled(MODELS["4X6W66"], k, fr), y0(T), T, 20.0, 10.0, thr)
             for cur, k in CUR10.items() for fr in FR for T in (10.0, 25.0)]
    return {r["key"]: r["classes"] for r in P.pmap(P.run_fixed, tasks)}

def checks10a(g):
    return {
        "Na 75% 10 C: LP irregular bursting, NET not triphasic": g[("Na", 0.75, 10.0)][1] == "irregular bursting" and g[("Na", 0.75, 10.0)][3] != "triphasic",
        "Na 75% 25 C: NET triphasic": g[("Na", 0.75, 25.0)][3] == "triphasic",
        "KCa every step 10 C: NET triphasic": all(g[("KCa", fr, 10.0)][3] == "triphasic" for fr in FR),
        "KCa 0% 25 C: all quiescent": all(x == "quiescent" for x in g[("KCa", 0.0, 25.0)][:3]),
        "CaT and CaS 0%: not triphasic at both, classes differ": all(
            g[(c, 0.0, 10.0)][3] != "triphasic" and g[(c, 0.0, 25.0)][3] != "triphasic" and g[(c, 0.0, 10.0)][:3] != g[(c, 0.0, 25.0)][:3]
            for c in ("CaT", "CaS")),
    }

G10 = {}
for start in ("control first", "from t = 0"):
    for thr in (P.SPIKE_THRESHOLD, 0.0):
        G10[(start, thr)] = grid10a(start, thr)
for start in ("control first", "from t = 0"):
    g = G10[(start, P.SPIKE_THRESHOLD)]
    print(f"=== protocol ({start}), spike threshold -20 mV")
    for cur in CUR10:
        for T in (10.0, 25.0):
            print(f"{cur} at {T:.0f} C")
            print(pd.DataFrame([g[(cur, fr, T)] for fr in FR], index=[f"{int(100 * fr)}%" for fr in FR],
                               columns=["PD", "LP", "PY", "NET"]).to_string())
checks10 = {}
for key, g in G10.items():
    checks10[key] = checks10a(g)
    print(f"\\nprotocol ({key[0]}), spike threshold {key[1]:.0f} mV:")
    for k, v in checks10[key].items():
        print(f"   {v!s:5s}  {k}")
    print("   matching:", sum(checks10[key].values()), "of 5")
g = G10[("control first", 0.0)]
print("\\nKCa at 10 C, protocol (control first), 0 mV threshold:", {f"{int(100 * fr)}%": g[("KCa", fr, 10.0)] for fr in FR})''')
i=find(nb,"## fig10b-complete-removal-differs")
setsrc(nb['cells'][i],'''## fig10b-complete-removal-differs

> Across the 36 models, the response to complete removal of a current differs between 10 and 25
> degrees C in about half of the models for most currents; most models respond differently for
> CaT, while removing H gives the same state (quiescence) at both temperatures.

All 38 deposited models, each current at 0% at 10 and 25 degrees C, the perturbed run 20 s with
the first 10 s dropped, under both protocols of fig10a-graded-removal (control first, the main
one; from t = 0, a variant).''')
j=find(nb,"claim:fig10b-complete-removal-differs")
setsrc(nb['cells'][j],'''t0 = time.time()
G0 = {}
for start in ("control first", "from t = 0"):
    y0 = (lambda n, T: CTRL[(n, T)]) if start == "control first" else (lambda n, T: CI)
    tasks = [((n, k, T), P.scaled(MODELS[n], k, 0.0), y0(n, T), T, 20.0, 10.0) for n in NAMES for k in range(8) for T in (10.0, 25.0)]
    G0[start] = {r["key"]: r["classes"] for r in P.pmap(P.run_fixed, tasks)}
print(f"{2 * len(tasks)} runs in {time.time() - t0:.0f} s")

def table10b(g0):
    rows = []
    for k, cur in enumerate(P.CURRENTS):
        diff_a = np.mean([g0[(n, k, 10.0)] != g0[(n, k, 25.0)] for n in NAMES])
        diff_b = np.mean([g0[(n, k, 10.0)][3] != g0[(n, k, 25.0)][3] for n in NAMES])
        sameq = sum(g0[(n, k, 10.0)] == g0[(n, k, 25.0)] and all(x == "quiescent" for x in g0[(n, k, 10.0)][:3]) for n in NAMES)
        rows.append(dict(current=cur, differ_all_classes=diff_a, differ_NET=diff_b, same_and_quiescent=sameq))
    return pd.DataFrame(rows).set_index("current")

def judge10b(t10b, col, currents):
    t = t10b.loc[currents]
    others = [c for c in currents if c not in ("CaT", "H")]
    cat = t[col].idxmax() == "CaT" and t.loc["CaT", col] > 0.5
    h = t.loc["H", "same_and_quiescent"] >= 33
    half = np.mean([0.3 <= t.loc[c, col] <= 0.7 for c in others])
    return cat, h, half

T10B = {}
for start, g0 in G0.items():
    t10b = T10B[start] = table10b(g0)
    print(f"\\n=== protocol ({start})")
    print(t10b.round(3).to_string())
    print("classes after complete removal of H:", Counter(tuple(g0[(n, 6, T)]) for n in NAMES for T in (10.0, 25.0)).most_common(5))
    for col in ("differ_all_classes", "differ_NET"):
        for label, cur in (("8 currents", P.CURRENTS), ("7 without leak", P.CURRENTS[:7])):
            cat, h, half = judge10b(t10b, col, cur)
            print(f"reading {col}, {label}: CaT largest and > 0.5 {cat}; H same and quiescent in >= 33 {h}; "
                  f"fraction of other currents in [0.3, 0.7] {half:.2f}")
g0 = G0["control first"]''')
# 0 mV threshold variant cell before summary
i=find(nb,"## Summary")
md=newcell('markdown','''## Spike threshold at 0 mV (variant)

Every model at 10 and 25 degrees C, 20 s with the first 10 s dropped, with spikes detected at
0 mV in place of -20 mV, and FGFKQS at 30 degrees C (fig6-crash-different-mechanisms). The cell
classes are compared with those at -20 mV from the same runs (deposit-models and the control
runs of fig10a-graded-removal; the 40 s run at 30 degrees C).''')
cc=newcell('code','''ref = {(r["key"], 10.0): r for r in r10}
ref.update({(r["key"], 25.0): r for r in ctl25})
z = {(r["key"], r["temp"]): r for r in P.pmap(P.run_fixed, [(n, MODELS[n], CI, T, 20.0, 10.0, 0.0) for n in NAMES for T in (10.0, 25.0)])}
changed = [(n, T, ref[(n, T)]["classes"], z[(n, T)]["classes"]) for n, T in ref if ref[(n, T)]["classes"] != z[(n, T)]["classes"]]
fewer = [(n, T, c, len(ref[(n, T)]["spikes"][c]), len(z[(n, T)]["spikes"][c])) for n, T in ref for c in range(3)
         if len(z[(n, T)]["spikes"][c]) != len(ref[(n, T)]["spikes"][c])]
print(f"runs whose classes differ between the -20 and 0 mV thresholds: {len(changed)} of {len(ref)}")
for row in changed:
    print("   ", row)
print(f"cells with a different spike count: {len(fewer)} of {3 * len(ref)}; largest differences (model, T, cell, -20 mV, 0 mV):",
      sorted(fewer, key=lambda x: x[3] - x[4])[-5:])
print("network triphasic at both temperatures, -20 mV:", sum(ref[(n, 10.0)]["classes"][3] == "triphasic" and ref[(n, 25.0)]["classes"][3] == "triphasic" for n in NAMES),
      "; 0 mV:", sum(z[(n, 10.0)]["classes"][3] == "triphasic" and z[(n, 25.0)]["classes"][3] == "triphasic" for n in NAMES), "of", len(NAMES))
f30 = P.run_fixed(("FGFKQS", MODELS["FGFKQS"], CI, 30.0, 40.0, 10.0, 0.0))
print("FGFKQS at 30 C, 0 mV threshold: classes", f30["classes"], "; PD spikes in 30 s", len(f30["spikes"][0]))''', tags=['spike-threshold-variant'])
nb['cells'][i:i]=[md,cc]
save(nb,p)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd entries/alonso-2020; PY=../../executed/alonso-2020/.venv/bin/python; cat > $TMPDIR/t1.py <<'EOF'
import json, re, os, shutil, subprocess, tempfile, time
from collections import Counter
from itertools import combinations
from pathlib import Path
import numpy as np, pandas as pd
from scipy import stats
import matplotlib; matplotlib.use("Agg")
import pyloric as P
raw = P.read_zip_bytes(); Z = P.open_zip(raw); MODELS = P.load_models(Z); FILES = P.model_files(Z); CI = P.load_ci(Z)
NAMES = list(MODELS)
nb = json.load(open("reproduce_alonso_2020.ipynb"))
src = lambda c: "".join(c["source"])
def cell(pred):
    return [src(c) for c in nb["cells"] if c["cell_type"] == "code" and pred(c)][0]
tag = lambda t: (lambda c: t in (c["metadata"].get("tags") or []))
starts = lambda s: (lambda c: src(c).startswith(s))
exec(cell(tag("finding-parameters-outside-search-space")))
exec(cell(starts("def java_check")))
exec(cell(starts("def states(")))   # ST for 6 models
exec(cell(tag("claim:fig4-currentscapes-reorganize")))
names9 = P.CURRENTS + ["Syn"]
SCAN = {}
for n, T in [("J9U8SQ", 34.0), ("KMNLBC", 30.0), ("FGFKQS", 34.0)]:
    SCAN[(n, T)] = P.run_fixed((n, MODELS[n], CI, T, 40.0, 10.0))
NAMES_ALL = NAMES
code = cell(starts("def longest_gaps"))
code = code[:code.index("cnt = Counter()")]
exec(code)
EOF
timeout 900 $PY $TMPDIR/t1.py
```

```
Exit code 1
Sat Nov 28 03:16:15 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 8, in <module>
    import pyloric as P
ModuleNotFoundError: No module named 'pyloric'
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; PY=../../executed/alonso-2020/.venv/bin/python; sed -i '1i import sys; sys.path.insert(0, ".")' $TMPDIR/t1.py; timeout 900 $PY $TMPDIR/t1.py
```

```
Exit code 1
gNa    bound    1000: deposited   794.00 to  1992.00; models with a cell above the bound 37 of 38
gCaT   bound     100: deposited     0.20 to    10.80; models with a cell above the bound 0 of 38
gCaS   bound     100: deposited     0.20 to    37.60; models with a cell above the bound 0 of 38
gA     bound     100: deposited     5.20 to   198.60; models with a cell above the bound 38 of 38
gKCa   bound    1000: deposited    10.00 to   116.00; models with a cell above the bound 0 of 38
gKd    bound     100: deposited    71.20 to   198.80; models with a cell above the bound 36 of 38
gH     bound     100: deposited     0.72 to    19.74; models with a cell above the bound 0 of 38
gLeak  bound      10: deposited     0.00 to     0.79; models with a cell above the bound 0 of 38
tau_Ca  bound 2000 ms: as stored 33.0 to 1898.1 (above: 0 models); as the Java uses it (x 10) 330 to 18981 ms (above: 38 models)
g syn   bound 0.05: deposited 0.0020 to 0.9930; models with a synapse above the bound 38 of 38
4X6W66, 3 s at 18 C: Java (60000, 3), port (60000, 3); largest difference in V where both are finite 3.09e-09 mV over 60000 samples; first sample with NaN: Java None, port None
J9U8SQ, 3 s at 25 C: Java (60000, 3), port (60000, 3); largest difference in V where both are finite 5.56e-02 mV over 60000 samples; first sample with NaN: Java None, port None
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 19, in <module>
    exec(cell(starts("def java_check")))
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 32, in <module>
  File "<string>", line 16, in java_check
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/subprocess.py", line 578, in run
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; PY=../../executed/alonso-2020/.venv/bin/python; f=reproduce_alonso_2020.ipynb; grep -c '("G7P2WE", 0.3, 35), ("J9U8SQ", 0.6, 34)' $f; sed -i 's/("G7P2WE", 0.3, 35), ("J9U8SQ", 0.6, 34)/("G7P2WE", 1, 35), ("J9U8SQ", 1, 34)/; s/J9U8SQ at 34 degrees C, over their first 0.3 and 0.6 s./J9U8SQ at 34 degrees C, over their first second (the Java takes whole seconds)./' $f; grep -c "first second" $f; timeout 900 $PY $TMPDIR/t1.py 2>&1 | tail -n +13
```

```
0
1
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 19, in <module>
    exec(cell(starts("def java_check")))
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 32, in <module>
  File "<string>", line 16, in java_check
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/subprocess.py", line 578, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['java', '-cp', '/tmp/claude-1001/tmpg_7aakzw', 'standaloneCodePyloricTempComp.integratePyloricNetwork_slow_full_temp_sameq10s_rk4', 'ci.txt', 'p.txt', '0.3', '35', '0.05']' returned non-zero exit status 1.
```

**Agent**

JSON escaping differs; I'll edit through the notebook helper.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
p='entries/alonso-2020/reproduce_alonso_2020.ipynb'
nb=load(p)
for c in nb['cells']:
    t=src(c)
    if '("G7P2WE", 0.3, 35)' in t:
        setsrc(c, t.replace('("G7P2WE", 0.3, 35), ("J9U8SQ", 0.6, 34)','("G7P2WE", 1, 35), ("J9U8SQ", 1, 34)')); print('ok')
save(nb,p)
EOF
cd entries/alonso-2020; timeout 900 ../../executed/alonso-2020/.venv/bin/python $TMPDIR/t1.py 2>&1 | tail -n +13
```

```
ok
G7P2WE, 1 s at 35 C: Java (20000, 3), port (20000, 3); largest difference in V where both are finite 0.00e+00 mV over 2041 samples; first sample with NaN: Java 2041, port 2041
J9U8SQ, 1 s at 34 C: Java (20000, 3), port (20000, 3); largest difference in V where both are finite 2.66e-09 mV over 8273 samples; first sample with NaN: Java 8273, port 8273
bounds (spikes), reading (a, thirds); bursts used per cell and temperature: {'PD 10': 3, 'PD 25': 9, 'LP 10': 3, 'LP 25': 9, 'PY 10': 3, 'PY 25': 9}
  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over end: 10 C 1.278; 25 C 1.348
  KCa outward share at the end of bursts (10 C, 25 C): {'PD': (np.float64(0.6174), np.float64(0.406)), 'LP': (np.float64(0.1542), np.float64(0.443)), 'PY': (np.float64(0.1573), np.float64(0.3818))}
  increase: {'PD': np.float64(-0.2114), 'LP': np.float64(0.2888), 'PY': np.float64(0.2246)}
  parts that hold: {'leak': False, 'A': False, 'KCa': False}
bounds (spikes), reading (b, 20%); bursts used per cell and temperature: {'PD 10': 3, 'PD 25': 9, 'LP 10': 3, 'LP 25': 9, 'PY 10': 3, 'PY 25': 9}
  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over end: 10 C 1.278; 25 C 1.385
  KCa outward share at the end of bursts (10 C, 25 C): {'PD': (np.float64(0.6537), np.float64(0.4496)), 'LP': (np.float64(0.1595), np.float64(0.499)), 'PY': (np.float64(0.1737), np.float64(0.4233))}
  increase: {'PD': np.float64(-0.2041), 'LP': np.float64(0.3396), 'PY': np.float64(0.2496)}
  parts that hold: {'leak': False, 'A': False, 'KCa': False}
bounds (slow wave), reading (a, thirds); bursts used per cell and temperature: {'PD 10': 2, 'PD 25': 8, 'LP 10': 3, 'LP 25': 9, 'PY 10': 2, 'PY 25': 9}
  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over e
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; cat > $TMPDIR/t2.py <<'EOF'
import sys; sys.path.insert(0, ".")
import json, time
from collections import Counter
import numpy as np, pandas as pd
import pyloric as P
raw = P.read_zip_bytes(); Z = P.open_zip(raw); MODELS = P.load_models(Z); CI = P.load_ci(Z)
NAMES = ["4X6W66", "FGFKQS"]
nb = json.load(open("reproduce_alonso_2020.ipynb"))
src = lambda c: "".join(c["source"])
cell = lambda t: [src(c) for c in nb["cells"] if t in (c["metadata"].get("tags") or [])][0]
r10 = P.pmap(P.run_fixed, [(n, MODELS[n], CI, 10.0, 20.0, 10.0) for n in NAMES])
t=time.time()
exec(cell("claim:fig10a-graded-removal")); print('fig10a', time.time()-t)
exec(cell("claim:fig10b-complete-removal-differs"))
exec(cell("spike-threshold-variant"))
EOF
timeout 1200 ../../executed/alonso-2020/.venv/bin/python $TMPDIR/t2.py 2>&1 | grep -v "^[A-Za-z]* at [0-9]* C$" | tail -60
```

```
protocol (from t = 0), spike threshold -20 mV:
   True   Na 75% 10 C: LP irregular bursting, NET not triphasic
   True   Na 75% 25 C: NET triphasic
   False  KCa every step 10 C: NET triphasic
   False  KCa 0% 25 C: all quiescent
   True   CaT and CaS 0%: not triphasic at both, classes differ
   matching: 3 of 5

protocol (from t = 0), spike threshold 0 mV:
   False  Na 75% 10 C: LP irregular bursting, NET not triphasic
   False  Na 75% 25 C: NET triphasic
   False  KCa every step 10 C: NET triphasic
   False  KCa 0% 25 C: all quiescent
   True   CaT and CaS 0%: not triphasic at both, classes differ
   matching: 1 of 5

KCa at 10 C, protocol (control first), 0 mV threshold: {'100%': ['regular bursting', 'quiescent', 'regular bursting', 'not triphasic'], '75%': ['regular bursting', 'quiescent', 'regular bursting', 'not triphasic'], '50%': ['regular bursting', 'single-spike bursting', 'regular bursting', 'triphasic'], '25%': ['regular bursting', 'regular bursting', 'regular bursting', 'triphasic'], '0%': ['regular bursting', 'regular bursting', 'regular bursting', 'triphasic']}
fig10a 81.9415442943573
64 runs in 32 s

[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; timeout 1200 ../../executed/alonso-2020/.venv/bin/python $TMPDIR/t2.py 2>&1 | sed -n '/protocol (control first), spike threshold -20 mV:/,/matching/p'
```

```
protocol (control first), spike threshold -20 mV:
   True   Na 75% 10 C: LP irregular bursting, NET not triphasic
   True   Na 75% 25 C: NET triphasic
   True   KCa every step 10 C: NET triphasic
   True   KCa 0% 25 C: all quiescent
   False  CaT and CaS 0%: not triphasic at both, classes differ
   matching: 4 of 5
```

**Agent calls Bash**

```bash
cd  grep -n "stamp\|STAMP\|stale\|executed" tools/entry.py | grep -v "^6[0-9][0-9]" | head -40
```

```
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
27:directory. The executed copies
28:go to --output-dir (default: executed/<name>/, which git ignores). A notebook
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
31:a hash of everything the run read (`hash` prints it) and of each executed
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
39:executed/<name>/handover/. Run the entry first.
65:STAMP = ".clean-run.json"                 # beside the executed copies: what they were made from (entry_hash)
67:REUSE_DAYS = 30                           # executed copies older than this are made again
544:    """The text each claim-tagged cell of an executed notebook printed, by tag."""
561:    `before` (its executed notebooks). The entry moves to the new version only when nothing differs; otherwise
576:            differ.append(f"{nb['path']}: no earlier executed copy in {before} to compare with")
707:        executed = output_dir / notebook["path"]
708:        if not executed.is_file():
709:            print(f"error: no executed copy of {notebook['path']} in {output_dir}; run the entry first",
712:        nb = strip_conclusions(nbformat.read(executed, as_version=4))
735:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
740:                        help="run: execute even when the executed copies were made from the entry as it is now")
743:    parser.add_argument("--before", type=Path, help="upgrade-python: the executed notebooks to compare with "
744:                                                    "(default: executed/<entry>)")
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python3 - <<'EOF'
s=open('pyloric.py').read()
old="""  whose spikes mostly peak above 0 mV and whose slow waves stay below the -50 mV slow-wave threshold
  of the Methods). The main notebook repeats the runs at 10 and 25 C and the graded removals of
  fig10a-graded-removal with a 0 mV threshold, as a variant; in some models the spikes peak below
  0 mV at 25 C, which that variant misses."""
new="""  whose slow waves stay below the -50 mV slow-wave threshold of the Methods). The main notebook
  repeats the runs at 10 and 25 C, the graded removals of fig10a-graded-removal and FGFKQS at 30 C
  with a 0 mV threshold, as a variant; the spikes of some cells peak below 0 mV, which that
  variant misses."""
assert old in s; s=s.replace(old,new); open('pyloric.py','w').write(s)
EOF
date -u; cd  && python tools/entry.py check entries/alonso-2020 2>&1 | tail -15
```

```
Sat Nov 28 03:21:55 UTC 2026
0 error(s)
```

**Agent calls Bash**

```bash
nohup setsid python tools/entry.py all entries/alonso-2020 > $TMPDIR/run_all.log 2>&1 < /dev/null & sleep 5; cat $TMPDIR/run_all.log; date -u
```

```
Sat Nov 28 03:22:25 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls questions/alonso-2020* 2>/dev/null; head -40 questions/asari-2009.yaml; grep -n "verifications" -A40 attempts/*.yaml | grep -v alonso | head -80
```

```
questions:
- claim: fig2-example-long-context
  question: The criterion says the example cell and probe are not identified and accepts any
    current-clamp cell with seven natural sound fragments and a probe tested after silence and
    two other fragments. Does the Figure 2 legend identify them? Figure 2A gives the cell's
    reliability (0.61 +/- 0.07 over its stimuli) and the probe's (0.74 +/- 0.08), and Figure 2B
    says its red trace is "the one shown in A". In the data set only 20051222-ha1-001-002 has
    those values (0.611 +/- 0.081, and 0.737 for probe 4), so its probe 4 would be the example.
    Should the criterion test that probe?
  passage: 'Figure 2 legend, "The neuron showed high trial-to-trial reliability (correlation
    coefficients across trials to this particular probe stimulus, 0.74 +- 0.08; and across trials
    across all natural sound stimuli examined in this cell, 0.61 +- 0.07; mean +- SD). B: the mean
    responses to the probe stimulus in 3 different contexts: red line for the one shown in A and
    blue and green lines for the one in response to the same probe stimulus but preceded by
    "silence" and another conditioning stimulus, respectively."'
  why: Under the criterion as written the claim is reproduced by probe 4 of 20060105-ha1-001-002,
    one of 20 candidates, from a cell whose mean reliability is 0.309, so it cannot be the paper's
    example. Probe 4 of 20051222-ha1-001-002 is significant up to 1.60 s, not from 1.60 to 3.97 s,
    and again from 3.97 to 4.60 s; its run at 3.97 s starts 30 ms inside the 2 to 4 s window, so
    it fails the strict test. Read as identifying that probe, the outcome would turn on how the
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; python3 - <<'EOF'
import json,glob
for f in glob.glob('schemas/*attempt*'):
    s=json.load(open(f)) if f.endswith('json') else None
    if s:
        v=s['properties'].get('verifications')
        print(f, json.dumps(v,indent=1)[:3000])
EOF
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/attempt.schema.json {
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
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
sleep 600; cat $TMPDIR/run_all.log; date -u; ls -la executed/alonso-2020/
```

```
Sat Nov 28 03:32:57 UTC 2026
total 424
drwxr-xr-x 3 runner runner   4096 Nov 28 02:47 .
drwxr-xr-x 3 runner runner   4096 Nov 28 03:06 ..
-rw-r--r-- 1 runner runner    641 Nov 28 02:47 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 28 01:01 .venv
-rw-r--r-- 1 runner runner  92259 Nov 28 02:23 ramps.ipynb
-rw-r--r-- 1 runner runner 236932 Nov 28 01:24 reproduce_alonso_2020.ipynb
-rw-r--r-- 1 runner runner    369 Nov 28 02:47 result.json
-rw-r--r-- 1 runner runner  80244 Nov 28 02:47 voltage_distributions.ipynb
```

**Agent calls Bash**

```bash
ps aux | grep -E "entry.py|nbconvert|ipykernel" | grep -v grep | head; uptime
```

```
03:33:01 up 34 min,  0 users,  load average: 0.07, 0.45, 0.96
```

**Agent calls Bash**

```bash
nohup setsid sleep 300 > /dev/null 2>&1 < /dev/null & disown; echo started
```

```
started
```

**Agent calls Bash**

```bash
ps aux | grep "sleep 300" | grep -v grep
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/alonso-2020 2>&1 | tail -30; date -u
```

```
Sat Nov 28 03:33:24 UTC 2026
Installed kernelspec registry-alonso-2020 in executed/alonso-2020/.venv/share/jupyter/kernels/registry-alonso-2020
0 error(s)
pass  reproduce_alonso_2020.ipynb  (1884 s)
pass  ramps.ipynb  (3472 s)
pass  voltage_distributions.ipynb  (1415 s)
Sat Nov 28 05:26:28 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/alonso-2020; python3 - <<'EOF' > $TMPDIR/out_main.txt
import json
for nbn in ['reproduce_alonso_2020','ramps','voltage_distributions']:
    nb=json.load(open(nbn+'.ipynb'))
    for i,c in enumerate(nb['cells']):
        if c['cell_type']!='code': continue
        tags=c['metadata'].get('tags')
        s=''.join(c['source'])[:60].replace('\n',' ')
        print(f'##### {nbn} cell {i} {tags} :: {s}')
        for o in c.get('outputs',[]):
            if 'text' in o: print(''.join(o['text']))
            elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/out_main.txt; grep -n "#####" $TMPDIR/out_main.txt
```

```
1231 /tmp/claude-1001/out_main.txt
1:##### reproduce_alonso_2020 cell 1 None :: import os import re import resource import shutil import sub
4:##### reproduce_alonso_2020 cell 3 ['sanity'] :: members = [i for i in Z.infolist() if not i.filename.startsw
118:##### reproduce_alonso_2020 cell 5 None :: def java_check(name="4X6W66", seconds=3, temp=18):     """Ru
127:##### reproduce_alonso_2020 cell 7 None :: METHODS_NAMES = {     "Figure 1": ["4?6W66"], "Figure 1-S1":
153:##### reproduce_alonso_2020 cell 8 ['finding-model-names'] :: # Four models the Methods name are not in the deposit, and f
163:##### reproduce_alonso_2020 cell 10 ['finding-shared-conductances'] :: key = {n: tuple(np.r_[P.conductances(MODELS[n]).ravel(), MOD
175:##### reproduce_alonso_2020 cell 12 ['finding-parameters-outside-search-space'] :: # Deposited parameters against the search space of the Metho
187:##### reproduce_alonso_2020 cell 14 ['claim:deposit-models'] :: r10 = P.pmap(P.run_fixed, [(n, MODELS[n], CI, 10.0, 20.0, 10
240:##### reproduce_alonso_2020 cell 15 ['finding-frequency-at-10C'] :: # Burst frequency at 10 C, 20 s simulated and the first 10 s
251:##### reproduce_alonso_2020 cell 18 None :: TEMPS = np.arange(10, 26).astype(float) t0 = time.time() sca
254:##### reproduce_alonso_2020 cell 20 ['claim:fig1c-frequency-q10-phase-constant'] :: t1, q1, rng1, rel1, rises1 = report(M["4?6W66"]) fig, ax = p
285:##### reproduce_alonso_2020 cell 23 ['claim:fig1s1-three-models'] :: s1 = {} for n in ["WWZ3CN", "FGFKQS", "71G6LA"]:     s1[n] =
375:##### reproduce_alonso_2020 cell 26 ['claim:all-models-compensated'] :: fails = pd.DataFrame({n: [SCAN[(n, T)]["classes"][3] != "tri
435:##### reproduce_alonso_2020 cell 29 ['claim:figs3-duty-cycle-variable-across-models'] :: DC = {n: np.concatenate([P.burst_stats(SCAN[(n, T)]["spikes"
493:##### reproduce_alonso_2020 cell 32 ['claim:intermediate-temperature-failures'] :: readme = Z.read(P.ROOT + "README.txt").decode() print("READM
551:##### reproduce_alonso_
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 118,126p out_main.txt; sed -n 175,186p out_main.txt; sed -n 493,551p out_main.txt; sed -n 695,748p out_main.txt
```

```
##### reproduce_alonso_2020 cell 5 None :: def java_check(name="4X6W66", seconds=3, temp=18):     """Ru
4X6W66, 3 s at 18 C: Java (60000, 3), port (60000, 3); largest difference in V where both are finite 3.09e-09 mV over 60000 samples; first sample with NaN: Java None, port None

J9U8SQ, 3 s at 25 C: Java (60000, 3), port (60000, 3); largest difference in V where both are finite 5.56e-02 mV over 60000 samples; first sample with NaN: Java None, port None

G7P2WE, 1 s at 35 C: Java (20000, 3), port (20000, 3); largest difference in V where both are finite 0.00e+00 mV over 2041 samples; first sample with NaN: Java 2041, port 2041

J9U8SQ, 1 s at 34 C: Java (20000, 3), port (20000, 3); largest difference in V where both are finite 2.66e-09 mV over 8273 samples; first sample with NaN: Java 8273, port 8273

##### reproduce_alonso_2020 cell 12 ['finding-parameters-outside-search-space'] :: # Deposited parameters against the search space of the Metho
gNa    bound    1000: deposited   794.00 to  1992.00; models with a cell above the bound 37 of 38
gCaT   bound     100: deposited     0.20 to    10.80; models with a cell above the bound 0 of 38
gCaS   bound     100: deposited     0.20 to    37.60; models with a cell above the bound 0 of 38
gA     bound     100: deposited     5.20 to   198.60; models with a cell above the bound 38 of 38
gKCa   bound    1000: deposited    10.00 to   116.00; models with a cell above the bound 0 of 38
gKd    bound     100: deposited    71.20 to   198.80; models with a cell above the bound 36 of 38
gH     bound     100: deposited     0.72 to    19.74; models with a cell above the bound 0 of 38
gLeak  bound      10: deposited     0.00 to     0.79; models with a cell above the bound 0 of 38
tau_Ca  bound 2000 ms: as stored 33.0 to 1898.1 (above: 0 models); as the Java uses it (x 10) 330 to 18981 ms (above: 38 models)
g syn   bound 0.05: deposited 0.0020 to 0.9930; models with a synapse above the bound 38 of 38
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 606,634p out_main.txt | grep -v "bursts used"; sed -n 890,1000p out_main.txt
```

```
##### reproduce_alonso_2020 cell 38 ['claim:fig4-currentscapes-reorganize'] :: def burst_part_shares(r, name, c, frac, bounds="spikes"):   
  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over end: 10 C 1.278; 25 C 1.348
  KCa outward share at the end of bursts (10 C, 25 C): {'PD': (np.float64(0.6174), np.float64(0.406)), 'LP': (np.float64(0.1542), np.float64(0.443)), 'PY': (np.float64(0.1573), np.float64(0.3818))}
  increase: {'PD': np.float64(-0.2114), 'LP': np.float64(0.2888), 'PY': np.float64(0.2246)}
  parts that hold: {'leak': False, 'A': False, 'KCa': False}

  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over end: 10 C 1.278; 25 C 1.385
  KCa outward share at the end of bursts (10 C, 25 C): {'PD': (np.float64(0.6537), np.float64(0.4496)), 'LP': (np.float64(0.1595), np.float64(0.499)), 'PY': (np.float64(0.1737), np.float64(0.4233))}
  increase: {'PD': np.float64(-0.2041), 'LP': np.float64(0.3396), 'PY': np.float64(0.2496)}
  parts that hold: {'leak': False, 'A': False, 'KCa': False}

  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over end: 10 C 1.364; 25 C 1.561
  KCa outward share at the end of bursts (10 C, 25 C): {'PD': (np.float64(0.3564), np.float64(0.7011)), 'LP': (np.float64(0.0486), np.float64(0.0783)), 'PY': (np.float64(0.148), np.float64(0.3313))}
  increase: {'PD': np.float64(0.3447), 'LP': np.float64(0.0297), 'PY': np.float64(0.1833)}
  parts that hold: {'leak': False, 'A': False, 'KCa': False}

  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 1000,1016p out_main.txt; sed -n 1095,1110p out_main.txt; sed -n 1136,1231p out_main.txt
```

```
parameters per model: {132} ; initial state: 46 numbers

ramps: 3435 s; peak memory 0.31 GB
runs that diverged (NaN): [] [('G7P2WE', 0), ('G7P2WE', 1), ('INPO74', 0), ('INPO74', 1), ('J9U8SQ', 0), ('J9U8SQ', 1), ('NJP4RT', 0), ('NJP4RT', 1), ('R00977', 0), ('R00977', 1), ('SJR46Y', 0), ('SJR46Y', 1)]
PLKTEM up ramp, spikes per cell: [54627, 68043, 94048]
spike counts per run and cell:
         up PD    up LP    up PY  down PD  down LP  down PY
count     38.0     38.0     38.0     38.0     38.0     38.0
mean   34628.0  37268.0  34855.0  28165.0  31266.0  28521.0
std    10487.0   8296.0   7794.0  16897.0  16636.0  14967.0
min    14120.0  16749.0  11253.0      0.0      0.0      0.0
25%    27590.0  33377.0  31720.0  21800.0  30160.0  25390.0
50%    31902.0  37352.0  37068.0  29482.0  35361.0  33362.0
75%    41149.0  43404.0  39359.0  36396.0  43137.0  38704.0
max    58056.0  51883.0  46591.0  66311.0  59807.0  46530.0

##### ramps cell 5 ['claim:figs2-ramp-largest-isi'] :: leg = UP["PLKTEM"]["legs"][0] res2 = {} for label, w in (("a
WWZ3CN             0.090                   True     True      51584        51404
X64GYZ             0.050                   True     True      56117        55991
XXKF5A             0.042                   True     True      64024        64053
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && cat > md_updates.py <<'PYEOF'
import sys; sys.path.insert(0,'.')
from nbedit import *
E='entries/alonso-2020/'
X='executed/alonso-2020/'
def apply(name, edits):
    """edits: list of (startswith, new_text) or (startswith, old, new) on markdown cells; applied to entry and executed copy."""
    for base in (E, X):
        nb=load(base+name)
        for e in edits:
            hits=[c for c in nb['cells'] if c['cell_type']=='markdown' and src(c).lstrip().startswith(e[0])]
            assert len(hits)==1,(name,e[0],len(hits))
            c=hits[0]
            if len(e)==2: setsrc(c,e[1])
            else:
                t=src(c); assert e[1] in t,(name,e[1][:50]); setsrc(c,t.replace(e[1],e[2]))
        save(nb,base+name)
PYEOF
echo ok
```

```
Sat Nov 28 05:26:54 UTC 2026
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from md_updates import *
apply('voltage_distributions.ipynb', [
 ("**Result: partially reproduced.**", """**Result: reproduced** (resting on the assumed reading of where the distribution's spike region
begins). In G7P2WE's LP cell the spike amplitude falls from 10 to 25 C under both readings (peak
minus trough 56.9 to 26.2 mV; upper envelope 16.7 to -1.8 mV; Spearman -1.000 each). The threshold
under reading (a) does not depolarize steadily (-27.8 to -27.5 mV, Spearman -0.197). Under reading
(b) it rises: the upper edge of the densely occupied part of the distribution goes from -36.1 to
-26.5 mV at 5% of the largest occupancy (Spearman 0.997), from -38.2 to -29.1 mV at 10% (0.996)
and from -33.0 to -20.0 mV at 2% (0.996; at the -20 mV search limit at 2 of 26 temperatures). 26
of the Methods' 101 temperatures were run."""),
 ("## Summary", """## Summary

| Claim | Outcome |
|---|---|
| fig2-lp-spike-amplitude-threshold | reproduced (assumed: threshold reading b) |
| fig2s1-peak-voltage-diverse | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: 26 temperatures (G7P2WE) and 6 (4X6W66, MAXTTP) in
place of 101; spike amplitude and threshold are read as stated in the claims file, and where the
distribution's spike region begins (threshold reading b) is located by an assumed rule, the upper
edge of the densely occupied part of the distribution below -20 mV. Nothing was found about the
dataset beyond the main notebook."""),
 ("# Alonso & Marder (2020), membrane", "| fig2-lp-spike-amplitude-threshold | tested (26 of 101 temperatures) |", "| fig2-lp-spike-amplitude-threshold | tested (26 of 101 temperatures; threshold reading b assumed) |"),
])
apply('ramps.ipynb', [
 ("# Alonso & Marder (2020), temperature ramps", "| fig8-up-down-ramps | blocked (too_large); the main ramp reading is shown |", "| fig8-up-down-ramps | blocked (too_large); the first ramp reading is shown, the second timed |"),
 ("**Result: blocked (too_large).**", """**Result: blocked (too_large).** On the first ramp reading (10 to 35 C and back over 60 min), 22
of 38 models are similar on the two legs (within 10% and triphasic in every 1 degree window; 9 at
5%, 28 at 20%), outside 34 +- 3, so this reading does not meet the criterion. Six models diverge
numerically on this ramp, MAXTTP's cells fire no spike on the down leg below 25 C, and 9 others
exceed the 10% bound or lose triphasic order. No model has identical spike counts on the two legs.
The criterion is met when either reading gives a count within tolerance, and the second reading
(10 to 25 C over 60 min and back) was not run: timed on a subset at 40 simulated seconds per
second, it would take 113 min, and this notebook had already run for 58 of its 60 min."""),
 ("## Summary", """## Summary

| Claim | Outcome |
|---|---|
| figs2-ramp-largest-isi | reproduced |
| fig8a-hysteresis-quiescence | reproduced |
| fig8-up-down-ramps | blocked (too_large; first reading 22 of 38, second reading estimated at 113 min) |
| fig8b-pathological-attractor | not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the deposit has no ramp code, so the temperature is
changed linearly and the factors updated every 20 steps (1 ms); each ramp starts from the
deposited initial conditions. The second ramp reading of fig8-up-down-ramps and the 60 min ramp
of every model for figs3-duty-cycle-variable-across-models were not run (113 and 57 min by the
timing on a subset). On the updown ramp the deposited integrator diverges (NaN) for G7P2WE,
INPO74, J9U8SQ, NJP4RT, R00977 and SJR46Y."""),
])
print('done')
EOF
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from md_updates import *
apply('reproduce_alonso_2020.ipynb', [
 ("# Reproducing Alonso", "| fig8-up-down-ramps | ramps | blocked (too_large); main reading shown |", "| fig8-up-down-ramps | ramps | blocked (too_large); first reading shown |"),
 ("# Reproducing Alonso", "| fig2-lp-spike-amplitude-threshold | voltage_distributions | tested |", "| fig2-lp-spike-amplitude-threshold | voltage_distributions | tested (threshold reading b assumed) |"),
 ("**Result: not reproduced.** In WWZ3CN the PD leak", """**Result: not reproduced.** In WWZ3CN the PD leak current has no inward share inside the bursts
at either temperature under either burst bound (0.0000 at start and end): every leak reversal
potential is -50 mV, so the leak is outward while V is above -50 mV, which holds between the
first and last spike and also between the slow-wave crossings. The leak part cannot hold under
any burst bound that keeps V above -50 mV. The PD A share at the start over the end of the burst is
1.278 at 10 C with spike bounds and 1.364 or 1.370 with slow-wave bounds, outside 0.8 to 1.25 in
every case. With spike bounds the KCa share at the end of bursts rises from 10 to 25 C in LP
(+0.29, +0.34) and PY (+0.22, +0.25) but falls in PD (-0.21, -0.20); with slow-wave bounds it rises
in all three cells but least in LP (+0.03, against PD +0.34 and +0.62), so the KCa part fails under
all four readings."""),
 ("**Result: not reproduced.** FGFKQS and 71G6LA", """**Result: not reproduced.** FGFKQS and 71G6LA are triphasic at 10 and 25 C. At 30 C, 71G6LA's PD
is quiescent (no spike in 30 s), but FGFKQS's PD fires 1005 spikes in 30 s (class other), so the
complete loss of PD activity holds in one model of two. The dominant PD currents at 30 C, from the
last 3 s of the same 40 s runs, differ (H and KCa in FGFKQS, H and Syn in 71G6LA), as they do in
the 13 s variant."""),
 ("**Result: not reproduced.** Seven of the eight", """**Result: not reproduced.** Seven of the eight models are in the deposit (Q8FBN1 is absent).
All seven stop being triphasic below 35 C (at 26 to 32 C), but their dominant (inward, outward)
currents, from the last 3 s of the same 40 s runs, form 5 distinct patterns: B7SD0L, J9U8SQ and
SJR46Y share H and Syn in all three cells. The 13 s variant also gives 5, with EF84RN in place of
SJR46Y. The criterion asks that no two share a pattern (reproduced) or at least six distinct among
eight (partially); with the eighth model at most six could be distinct, and Q8FBN1 cannot be shown
to crash."""),
 ("**Result: partially reproduced.** In 4X6W66, three of the five", """**Result: partially reproduced** (under both protocols). With the control period first (main
protocol), four of the five stated grid cells match: Na at 75% makes LP burst irregularly and the
network not triphasic at 10 C and leaves it triphasic at 25 C; KCa removal leaves the network
triphasic at every step at 10 C; KCa at 0% at 25 C makes every cell quiescent. CaT and CaS at 0%
fail: the network is not triphasic at both temperatures, but for one of the two currents the cell
classes are the same at 10 and 25 C. With the conductance changed from t = 0 (variant), three of
five match: the KCa parts fail (at 10 C, 25% and 0% give PD and PY quiescent with LP tonic; at
25 C, 0% leaves LP tonic) and the CaT and CaS part holds. With a 0 mV spike threshold, 2 (control
first) and 1 (from t = 0) of five match, as LP's spikes in 4X6W66 peak below 0 mV at 10 C (the
intact model has LP quiescent at 0 mV)."""),
 ("**Result: not reproduced.** Across the 38 models, CaT", """**Result: not reproduced** (under both protocols). With the control period first (main
protocol), CaT has the largest fraction of models that respond differently at 10 and 25 C under
both readings (0.895 all classes, 0.605 network class), and 5 of 6 other currents (8 currents) or 4
of 5 (without leak) fall within 0.3 to 0.7 under the four-class reading. But complete removal of H
gives the same, quiescent, state at both temperatures in 30 of 38 models, below the criterion's 33.
With the conductance removed from t = 0 (variant), H gives 31, CaT is the largest only under the
four-class reading (0.974; network class 0.474 against A 0.579), and 2 of 6 or 2 of 5 other
currents fall within 0.3 to 0.7. The H part fails under every reading and protocol; with 36 models
in place of 38, 30 or 31 cannot reach 33."""),
])
print('ok')
EOF
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 777,830p out_main.txt | grep -A7 "^CaT at\|^CaS at"
```

```
CaT at 10 C
                    PD                  LP                     PY            NET
100%  regular bursting    regular bursting       regular bursting      triphasic
75%   regular bursting    regular bursting       regular bursting      triphasic
50%   regular bursting  irregular bursting     irregular bursting  not triphasic
25%          quiescent           quiescent  single-spike bursting  not triphasic
0%           quiescent           quiescent  single-spike bursting  not triphasic
CaT at 25 C
                      PD                  LP                  PY            NET
100%    regular bursting    regular bursting    regular bursting      triphasic
75%     regular bursting    regular bursting    regular bursting      triphasic
50%     regular bursting    regular bursting    regular bursting      triphasic
25%   irregular bursting    regular bursting  irregular bursting  not triphasic
0%    irregular bursting  irregular bursting  irregular bursting  not triphasic
CaS at 10 C
                    PD                  LP                PY            NET
100%  regular bursting    regular bursting  regular bursting      triphasic
75%   regular bursting    regular bursting  regular bursting      triphasic
50%          quiescent  irregular bursting  regular bursting  not triphasic
25%          quiescent  irregular bursting  regular bursting  not triphasic
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk 'NR>=777 && NR<=900' out_main.txt | grep -n -A6 "^CaS at 25 C" | head -8
```

```
52:CaS at 25 C
53-                      PD                  LP                  PY            NET
54-100%    regular bursting    regular bursting    regular bursting      triphasic
55-75%     regular bursting    regular bursting    regular bursting      triphasic
56-50%   irregular bursting  irregular bursting  irregular bursting  not triphasic
57-25%     regular bursting  irregular bursting  irregular bursting  not triphasic
58-0%             quiescent    regular bursting    regular bursting  not triphasic
--
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from md_updates import *
apply('reproduce_alonso_2020.ipynb', [
 ("**Result: partially reproduced** (under both protocols). With the control", "fail: the network is not triphasic at both temperatures, but for one of the two currents the cell\nclasses are the same at 10 and 25 C.", "fail: the network is not triphasic at both temperatures, but for CaS the cell classes are the\nsame at 10 and 25 C (PD quiescent, LP and PY regular bursting)."),
 ("## Summary", """## Summary

| Claim | Outcome |
|---|---|
| deposit-models | not reproduced |
| fig1c-frequency-q10-phase-constant | partially reproduced |
| fig1s1-three-models | not reproduced |
| all-models-compensated | partially reproduced |
| intermediate-temperature-failures | blocked (data_missing) |
| figs2-ramp-largest-isi | reproduced (ramps notebook) |
| figs3-duty-cycle-variable-across-models | reproduced, variant reading |
| fig2-lp-spike-amplitude-threshold | reproduced, threshold reading b assumed (voltage_distributions notebook) |
| fig2s1-peak-voltage-diverse | reproduced (voltage_distributions notebook) |
| fig3-current-amplitudes | partially reproduced |
| fig4-currentscapes-reorganize | not reproduced |
| currentscapes-dominant-currents | reproduced |
| fig5-a-to-kca-tradeoff | reproduced |
| fig6-crash-different-mechanisms | not reproduced |
| fig6s1-crash-mechanisms | not reproduced (7 of 8 models) |
| fig7-high-temperature-slow-timescales | blocked (data_missing) |
| fig8a-hysteresis-quiescence | reproduced (ramps notebook) |
| fig8-up-down-ramps | blocked (too_large; first reading 22 of 38) |
| fig8b-pathological-attractor | not reproduced (ramps notebook) |
| fig9a-remove-a-current | partially reproduced |
| fig9b-remove-kca-current | reproduced |
| fig10a-graded-removal | partially reproduced |
| fig10b-complete-removal-differs | not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the models are simulated with a numba port of the
deposited Java, which matches it to 3e-9 mV over 3 s at 18 C, to 0.06 mV over 3 s at 25 C, and
gives NaN at the same step as the Java where the integration diverges (G7P2WE at 35 C, J9U8SQ at
34 C); spikes are upward crossings of -20 mV and the network order is judged on median phases
(assumptions, as the paper gives neither; a 0 mV threshold misses the spikes of cells that peak
below 0 mV and leaves 17 of 38 models triphasic at both 10 and 25 C, against 38); conductances are
changed after a 20 s control period for Figure 10, as the Results do for Figure 9 (assumed; the
change from t = 0 is shown too); the 38 deposited models are used where the paper says 36; the
figure supplements' legends were not read.

What was found about the dataset: 38 models where the paper says 36; 4 models named in the Methods
absent (Q8FBN1, G81PUL, G7EOZ8, SAXT8Y) and 4 filed under other spellings; 27 distinct sets of
maximal conductances; gNa, gA, gKd, the synaptic conductances and tau_Ca (as the Java uses it)
outside the search space the Methods give, in most or all models; the models' burst frequency at
10 C is 1.25 Hz on average, not the 1 Hz target; and the deposited integrator, the Java as well as
the port, diverges (NaN) for 6 models at some temperatures from 26 to 35 C."""),
])
print('ok')
EOF
cd  && sed -i 's/| Figure 2: LP spike amplitude falls and threshold depolarizes | Partially reproduced |/| Figure 2: LP spike amplitude falls and threshold depolarizes | Reproduced |/' entries/alonso-2020/README.md && grep -n "Figure 2: LP" entries/alonso-2020/README.md; date -u
```

```
ok
19:| Figure 2: LP spike amplitude falls and threshold depolarizes | Reproduced |
Sat Nov 28 05:27:48 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from md_updates import *
apply('reproduce_alonso_2020.ipynb', [
 ("## figs3-duty-cycle-variable-across-models", "which is not run (it would add\nabout 35 min; see `ramps.ipynb`).", "which is not run (57 min by the\ntiming on a subset in `ramps.ipynb`)."),
 ("**Result: reproduced** (on the criterion's variant", "conductances (largest p 0.025).", "conductances (largest p 0.025). The test pools autocorrelated per-burst values across\ntemperatures, so it detects small differences, and the outcome carries little more than that the\ndistributions are not identical."),
])
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
P='attempts/alonso-2020-01.yaml'
d=yaml.safe_load(open(P))
O={o['claim']:o for o in d['outcomes']}

o=O['deposit-models']
o['deviations'][1]=("The model is simulated with a numba port of the deposited Java, which matches the Java's voltages to "
 "3e-9 mV over 3 s (4X6W66 at 18 C), to 0.06 mV over 3 s (J9U8SQ at 25 C), and gives NaN at the same step as the Java "
 "where the integration diverges (G7P2WE at 35 C, step 2041; J9U8SQ at 34 C, step 8273); the notebook compiles and runs "
 "the Java when a compiler is present.")

o=O['all-models-compensated']
o['notes']+=(" MAXTTP, one of the two that fail, is a model the paper shows (Figure 2, figure supplement 1), so not every "
 "model the paper uses passes.")

o=O['intermediate-temperature-failures']
o['notes']+=(" The README describes how to compile and run the code and says nothing about which solutions were kept or "
 "discarded. The score in each file name runs from 7.8 to 160.8 (median 18.5); the two models that fail between 10 and "
 "25 C score 28.0 (ED50XO) and 160.8 (MAXTTP, the largest), and the next largest are R00977 (107.0) and J9U8SQ (91.9), "
 "which do not fail. That 2 of 38 fail is close to the paper's 2 in 40, but nothing in the files says that the 38 hold "
 "the paper's 2 failures, and MAXTTP is shown in Figure 2, figure supplement 1.")

o=O['figs3-duty-cycle-variable-across-models']
o['deviations'][0]=("The ramp reading (38 models, 3600 s each) was not run: timed on a subset in ramps.ipynb at 40 simulated "
 "seconds per second on 4 processes, it would take 57 min, and that notebook already takes 58 min. The outcome rests on "
 "the variant reading the criterion names.")
o['notes']+=(" The test pools autocorrelated per-burst values across temperatures, so it detects small differences; the "
 "outcome says that the distributions are not identical, little more.")

o=O['fig2-lp-spike-amplitude-threshold']
o['outcome']='reproduced'
o['assumed']=True
o['measured']=[-1.0, 0.997]
o['notes']=("G7P2WE, LP, 26 temperatures from 10 to 25 C, 30 s at dt = 0.001 ms with the last 10 s kept (5 x 10^5 samples, "
 "as the Methods say). The amplitude falls under both readings (peak minus trough 56.9 to 26.2 mV; upper envelope 16.7 "
 "to -1.8 mV; Spearman -1.000 each). The threshold under reading (a) stays near -28 mV (-27.8 to -27.5 mV, with a dip "
 "to -28.6 mV between; Spearman -0.197). Under reading (b), located as the upper edge of the densely occupied part of "
 "the distribution below -20 mV, the threshold rises from -36.1 to -26.5 mV at 5% of the largest occupancy (Spearman "
 "0.997), from -38.2 to -29.1 mV at 10% (0.996) and from -33.0 to -20.0 mV at 2% (0.996, at the search limit at 2 of 26 "
 "temperatures). Amplitude (a) and threshold (b) meet the criterion. The measured values are the Spearman correlations "
 "of amplitude (a) and threshold (b) at 5%. Where the spike region begins is assumed; the question is for the paper's "
 "authors (finding 6).")
o['deviations']=["26 of the Methods' 101 temperatures (steps of 0.6 C), as 101 at dt = 0.001 ms would take about 40 min.",
 ("Threshold reading (b) is located by an assumed rule (pyloric.spike_region_start): the highest voltage below the -20 mV "
  "spike detection level whose occupancy, smoothed over 1 mV, is at least 5% of the largest occupancy; above it the cell "
  "passes only during spikes. Neither the paper nor the claims file says how the point is found. The fractions 2% and "
  "10% give the same outcome.")]

o=O['fig4-currentscapes-reorganize']
o['notes']=("WWZ3CN, 3 s at 10 and 25 C (3 and 9 bursts per cell). Two burst bounds were run, from the first to the last "
 "spike and between the -50 mV slow-wave crossings, each with thirds and 20%. The PD leak current has no inward share "
 "inside the bursts under any of the four (0.0000 at start and end): all leak reversal potentials are -50 mV, and V "
 "stays above -50 mV within either bound, so the leak part cannot hold under any burst bound that keeps V above "
 "-50 mV. The PD A share at the start over the end of the burst is 1.278 at 10 C with spike bounds and 1.364 or 1.370 "
 "with slow-wave bounds, outside 0.8 to 1.25. With spike bounds the KCa share at the end of the burst rises in LP "
 "(+0.29, +0.34) and PY (+0.22, +0.25) but falls in PD (-0.21, -0.20); with slow-wave bounds it rises in all three but "
 "least in LP (+0.03 against PD +0.34 and +0.62). No part of the criterion holds under any reading.")
o['deviations']=[("Where a burst starts and ends is open; the bursts are bounded by their first and last spike and, as a "
 "second reading, by the last upward and the first downward crossing of the Methods' -50 mV slow-wave threshold around "
 "them. Both give the same outcome.")]

o=O['fig6-crash-different-mechanisms']
o['notes']=("FGFKQS and 71G6LA are triphasic at 10 and 25 C. At 30 C (40 s, last 30 s), 71G6LA's PD is quiescent (no "
 "spike), but FGFKQS's PD fires 1005 spikes (class other; V from -59.7 to 14.8 mV), so complete loss of PD activity holds "
 "in one of the two models, and the criterion requires both. The dominant PD currents at 30 C, over the last 3 s of the "
 "same 40 s runs, differ between the models (H and KCa in FGFKQS, H and Syn in 71G6LA), as they do over the last 3 s of "
 "13 s runs. With a 0 mV spike threshold FGFKQS's PD fires 336 spikes in the 30 s and the network is triphasic.")
o['deviations']=[("Each temperature is simulated from the deposited initial conditions, as the deposit's scripts do; how "
 "the paper reached 30 C (a ramp or a fresh start) is not stated, and the classes rest on the -20 mV spike threshold "
 "(assumed)."), "The dominant currents are taken over the last 3 s of the 40 s run that is classified."]

o=O['fig6s1-crash-mechanisms']
o['notes']=("Seven of the eight models are in the deposit; Q8FBN1 is not. All seven stop being triphasic below 35 C "
 "(B7SD0L 32, J9U8SQ 29, 4R2719 32, R3VIEW 30, RMZ8KZ 29, EF84RN 30, SJR46Y 26 C, skipping runs that diverged), but the "
 "dominant (inward, outward) current pairs per cell, over the last 3 s of the same 40 s runs, form 5 distinct patterns; "
 "B7SD0L, J9U8SQ and SJR46Y share H and Syn in all three cells. Over the last 3 s of 13 s runs there are also 5, with "
 "EF84RN in place of SJR46Y. Reproduction needs every pattern distinct, and the partial case at least six distinct among "
 "eight with every model crashing; with the missing model at most six could be, and Q8FBN1 cannot be shown to crash.")
o['deviations'][1]=("Crash temperatures come from simulations from the initial conditions at each temperature (40 s, last "
 "30 s); runs whose integration diverged are skipped. The dominant currents are taken over the last 3 s of the same 40 "
 "s run; window-averaged shares are dominated by the currents of the hyperpolarized phases, which makes shared patterns "
 "likely.")

o=O['fig7-high-temperature-slow-timescales']
o['notes']=("Three of the five models (G81PUL, G7EOZ8, SAXT8Y) are not in the deposit. Of the two that are, J9U8SQ at 34 "
 "C diverges numerically (NaN) from the initial conditions, at the same step in the deposited Java as in the port (step "
 "8273, 0.41 s), and KMNLBC (KNMLBC of the Methods) at 30 C is triphasic in the last 30 s of a 40 s run, with no gap "
 "between spikes longer than 0.68 s (reading a) and a dominant period of the slow voltage of 0.35, 0.35 and 0.29 s "
 "(reading b). So neither model present shows a time scale above 2 s, and the claim would not be reproduced even with "
 "the three missing models. FGFKQS at 34 C (the panel A variant) is quiescent. Over all 38 models at 26 to 35 C, 81 of "
 "the non-triphasic runs have all cells quiescent, 29 diverged, and the rest mix regular, irregular and other classes. "
 "That J9U8SQ, which Figure 7A shows active at 34 C, diverges in the deposited code suggests the paper's high-temperature "
 "runs used other settings.")

o=O['fig8-up-down-ramps']
o['notes']=("The criterion is met when either ramp reading gives a count within 34 +- 3. The first reading (10 to 35 C "
 "and back over 60 min) was run, and 22 of 38 models are similar on the two legs over 10 to 25 C (9 at a 5% bound, 28 "
 "at 20%), so that reading does not meet it. Six models diverge numerically on this ramp (G7P2WE, INPO74, J9U8SQ, "
 "NJP4RT, R00977, SJR46Y), MAXTTP fires no spike on the down leg below 25 C, and 9 others exceed 10% or lose triphasic "
 "order in some window. No model has the same spike count on both legs. The second reading (10 to 25 C over 60 min and "
 "back, 7200 s per model), which is the ramp of Figure 1, figure supplement 2 that the paper cites for this sentence, was "
 "timed in the notebook on a subset at 40 simulated seconds per second on 4 processes: 113 min for 38 models, while the "
 "notebook had already run 58 of its 60 min, and the run had about 1 h 50 min left for all three notebooks. It was not "
 "run, so the outcome cannot be decided; a run of the second reading alone, in a notebook of its own split over two or "
 "more notebooks, would settle it.")

o=O['fig10a-graded-removal']
o['measured']=4
o['notes']=("4X6W66, each perturbed run 20 s with the first 10 s dropped, under two protocols. With 20 s of control first "
 "and the conductance changed from its final state (main protocol), four of the five stated grid cells match: Na at 75% "
 "makes LP burst irregularly with the network not triphasic at 10 C and leaves it triphasic at 25 C; KCa removal keeps "
 "the network triphasic at every step at 10 C; KCa at 0% at 25 C makes every cell quiescent. The CaT and CaS part fails: "
 "the network is not triphasic at either temperature for both, but with CaS at 0% the cell classes are the same at 10 "
 "and 25 C (PD quiescent, LP and PY regular bursting). With the conductance changed from t = 0 (variant), three of five "
 "match: at 10 C, KCa at 25% and 0% gives PD and PY quiescent and LP tonic spiking, and at 25 C, KCa at 0% leaves LP "
 "tonic spiking, while the CaT and CaS part holds. Both protocols give partially reproduced. With a 0 mV spike threshold "
 "2 (control first) and 1 (from t = 0) of five match, as LP's spikes peak below 0 mV at 10 C.")
o['deviations']=[("The conductance is changed after 20 s of control from the deposited initial conditions (assumed). The "
 "paper does not say when for Figure 10; the Results give this protocol for the removals of Figure 9, in the same "
 "section (\"the models were simulated for 20 s in control conditions and then IA was completely removed for the next "
 "20 s\"), and the deposit's integratePyloricSQ10s_remove_gA_onesteps_twotemps_RK4.py also runs a control period and "
 "continues from its final state. The change from t = 0 is shown as a variant."),
 "The classes rest on the -20 mV spike threshold and the order test (assumed); a 0 mV threshold is shown as a variant."]

o=O['fig10b-complete-removal-differs']
o['notes']=("38 models, each current at 0% at 10 and 25 C, under both protocols of fig10a-graded-removal. With the control "
 "period first (main), CaT has the largest fraction responding differently under both readings (0.895 all classes, 0.605 "
 "network class), and 5 of the 6 other currents (8 currents; 4 of 5 without leak) fall within 0.3 to 0.7 under the "
 "four-class reading, but complete removal of H gives the same, quiescent, state at both temperatures in 30 of 38 models "
 "(the criterion asks at least 33). Fractions responding differently (four classes) Na 0.263, CaS 0.579, A 0.500, KCa "
 "0.658, Kd 0.474, H 0.184, leak 0.658. With removal from t = 0 (variant), H gives 31, CaT is the largest only under the "
 "four-class reading (0.974; network class 0.474 against A 0.579), and 2 of 6 other currents fall within 0.3 to 0.7. The "
 "H part fails under every reading and protocol, and with 36 models in place of 38 a count of 30 or 31 cannot reach 33.")
o['deviations']=["The 38 deposited models; the bound of 33 was set for 36.",
 "The conductance is removed after 20 s of control, as in fig10a-graded-removal (assumed); removal from t = 0 is shown.",
 "The classes rest on the -20 mV spike threshold and the order test (assumed)."]

F=d['findings']
F[4]['statement']=("The deposited integrator (RK4, dt = 0.05 ms, the deposited initial conditions) returns NaN for 6 of the "
 "38 models at some temperatures from 26 to 35 C (29 of 380 runs), and for the same 6 on the 10 to 35 C ramp. The "
 "deposited Java gives NaN at the same step as the port (G7P2WE at 35 C at step 2041, J9U8SQ at 34 C at step 8273). "
 "Results at those temperatures cannot be computed with the deposited code at the paper's time step, though Figure 7A "
 "shows J9U8SQ active at 34 C.")
F[5]['statement']=("Questions for the paper's authors. (1) What voltage threshold detects a spike? This attempt uses "
 "upward crossings of -20 mV; at 0 mV the spikes of some cells are missed and 17 of 38 models stay triphasic at 10 and "
 "25 C, against 38. (2) How is \"fired in the right order\" tested for the triphasic class? This attempt compares the "
 "median LP and PY burst onset phases within the PD cycle; requiring the order in every cycle changes the compensated "
 "count from 36 to 35 of 38. (3) How is the lag d between spike onset and the -50 mV crossing formed? This attempt takes "
 "the median over spikes of the time from the last upward crossing. (4) How were the temperature ramps run, and were "
 "high-temperature states (Figures 6 and 7) reached from a ramp or from the initial conditions? (5) Which 36 of the 38 "
 "deposited models are the paper's? (6) For Figure 10, was the conductance changed after a control period, as for Figure "
 "9, or from the start? This attempt uses a 20 s control period. (7) How is the spike threshold read from the voltage "
 "distribution in Figure 2? This attempt takes the upper edge of the densely occupied part of the distribution. These "
 "choices enter every outcome marked as assumed.")
F.append({'kind':'other','about':'data','severity':'minor','notebook':'reproduce_alonso_2020.ipynb',
 'output':'finding-parameters-outside-search-space',
 'statement':("The deposited parameters fall outside the search space the Methods give (Finding parameters). gNa reaches "
  "1992 uS against a bound of 1000 (37 of 38 models above it), gA 198.6 and gKd 198.8 against 100 (38 and 36 models), "
  "and the synaptic conductances 0.993 uS against 0.05 (all 38). tau_Ca is within its 2000 ms bound as stored (33 to "
  "1898) but not as the deposited Java uses it, times 10 (330 to 18,981 ms). The files may follow another convention or "
  "code version than the Methods describe; the deposited Java runs them as they are.")})
yaml.safe_dump(d, open(P,'w'), width=110, sort_keys=False, allow_unicode=True)
print('ok')
PYEOF
python3 $TMPDIR/rec.py && git diff --stat attempts/
```

```
ok
 attempts/alonso-2020-01.yaml | 466 +++++++++++++++++++++++--------------------
 1 file changed, 251 insertions(+), 215 deletions(-)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
P='attempts/alonso-2020-01.yaml'
d=yaml.safe_load(open(P))
O={o['claim']:o for o in d['outcomes']}
o=O['fig8-up-down-ramps']
o['notes']=o['notes'].replace(" while the notebook had already run 58 of its 60 min, and the run had about 1 h 50 min left for all three notebooks. It was not run, so the outcome cannot be decided; a run of the second reading alone, in a notebook of its own split over two or more notebooks, would settle it.",
 " while the notebook had already run 58 of its 60 min. It was not run, so the outcome cannot be decided; the second reading, run on its own and split over two notebooks to fit the limit, would settle it.")
assert "split over two notebooks" in o['notes']
R=[]
def r(claim, agrees, outcome, reason, response):
    R.append(dict(claim=claim, agrees=agrees, outcome=outcome, reason=reason, response=response))
r('deposit-models', True, 'not_reproduced',
  "Cell 12: 3 of 38 models are within tolerance, against the 30 needed. The 0.20 variant gives 0 of 38, and mean frequency is 1.25 Hz. Cells 7, 8 and 10: 4 of the 21 named models are absent, the deposit holds 38 models (not 36), and those 38 contain only 27 distinct conductance sets.",
  "No change of outcome. Problem 6: a new cell, finding-parameters-outside-search-space, compares the deposited parameters with the Methods' search space and a new finding (7) records that gNa, gA, gKd, the synaptic conductances and tau_Ca as the Java uses it fall outside it. Problem 5: the Java is now compared with the port at 25, 34 and 35 C (deviation updated).")
r('fig1c-frequency-q10-phase-constant', True, 'partially_reproduced',
  "Cell 17: the frequency Q10 of 4X6W66 is 1.93, 1.98 or 1.94 under readings a, b and c, all within 2+-0.2. Constancy fails under both readings: the LP duty-cycle range is 0.11 (above 0.1) and its change from 10 C is 34% (above 20%).",
  "No change.")
r('fig1s1-three-models', True, 'not_reproduced',
  "Cell 19: frequency rises in all three models, but none is constant under either reading. 71G6LA misses reading (i) only on PY offset (range 0.102).",
  "No change.")
r('all-models-compensated', True, 'partially_reproduced',
  "Cell 21: 36 of 38 models are triphasic at all 16 temperatures (35 with the strict order variant). ED50XO fails at 19 and 21 C; MAXTTP fails at 10 and 14 C, and MAXTTP is a paper model (Fig. 2-S1), so not every paper model passes. \"Multiple Q10 sets for every conductance set\" is unsupported: only 9 of the 27 conductance sets carry more than one Q10 set.",
  "No change of outcome. The notes now say that MAXTTP is a model the paper shows, so not every model the paper uses passes.")
r('intermediate-temperature-failures', True, 'blocked',
  "Confirmed: the archive is one zip with 38 parameter files and nothing marks which were screened or discarded. 38 files is 36 plus 2, and exactly two models (ED50XO and MAXTTP) fail between temperatures; printing the README and the file-name scores against the 36 would show whether part of this claim is testable. MAXTTP appears in Fig. 2-S1, which argues against it being a discarded solution.",
  "No change of outcome. A new cell prints the README's lines on models (it says nothing about kept or discarded solutions) and every file-name score: ED50XO scores 28.0 and MAXTTP 160.8, the largest, while R00977 (107.0) and J9U8SQ (91.9), the next largest, do not fail. Nothing ties the 38 to the 40 screened, so the claim stays blocked; the notes give these numbers.")
r('figs2-ramp-largest-isi', True, 'reproduced',
  "Ramps cell 5: under reading (a), Spearman is -1.0 in all three cells with 0 increases. Under reading (b) it is between -0.994 and -0.998.",
  "No change.")
r('figs3-duty-cycle-variable-across-models', True, 'reproduced',
  "Reproduced on the variant reading only. Cell 23: all 703 of 703 pairs differ at p < 0.05. The main ramp reading was not run. The KS test pools about 900 autocorrelated per-burst values across temperatures, so almost any difference is significant; even FGFKQS against EF84RN gives p = 0.025. The test follows the criterion, but it carries little information.",
  "No change of outcome. The ramp reading is now timed in the ramps notebook (57 min for 38 models at 40 simulated seconds per second), which does not fit beside that notebook's 58 min, so it stays not run. The notes and the conclusion now say that the test detects small differences and shows little more than that the distributions are not identical.")
r('fig2-lp-spike-amplitude-threshold', True, 'partially_reproduced',
  "Voltage cell 5: amplitude falls under both readings (rho = -1.0, from 56.9 to 26.2 mV). Threshold reading (a) gives rho = -0.197, flat at about -28 mV. Threshold reading (b) was not computed, so the claim might be fully reproduced under it.",
  "Outcome changed to reproduced, marked assumed. Threshold reading (b) is now computed (pyloric.spike_region_start), as the upper edge of the densely occupied part of the distribution below -20 mV: it rises from -36.1 to -26.5 mV at 5% of the largest occupancy (Spearman 0.997), and at 2% and 10% too (0.996 each). The rule for locating the point is an assumption, recorded as a deviation and asked of the authors (finding 6).")
r('fig2s1-peak-voltage-diverse', True, 'reproduced',
  "Voltage cell 7: at the 5 mV bound, G7P2WE falls 14-19 mV, 4X6W66 rises 6-7 mV in LP and PY, and MAXTTP changes by no more than 2.5 mV. Mean V rises in 8 cells and falls in 1. This is fragile: the only fall is 0.26 mV, and each of the 2 and 10 mV variants fails one part.",
  "No change; the notes already give the 2 and 10 mV variants and the 0.26 mV fall.")
r('fig3-current-amplitudes', True, 'partially_reproduced',
  "Cell 27: 4 of 5 checks hold under both peak readings. The KCa ratio in 4X6W66 is 8.9-9.1, against 6+-0.6. The swapped panel assignment gives 0 of 5.",
  "No change.")
r('fig4-currentscapes-reorganize', True, 'not_reproduced',
  "Cell 29: the KCa share at burst end falls in PD (0.62 to 0.41), so the KCa part fails under both readings. The A ratio at 10 C is 1.278, just outside 0.8-1.25. The leak part could not hold by construction (problem 4): bursts run from the first to the last spike crossing, V stays above EL = -50 mV there, so the leak's inward share is 0 at start and end; a burst bounded by the -50 mV slow-wave crossings is the reading under which the leak statement can be tested. The KCa part fails anyway, so the outcome probably stands.",
  "No change of outcome. Slow-wave bounds (last upward and first downward -50 mV crossing around each burst) are now run beside the spike bounds. The leak's inward share is still 0 at start and end, as V is above -50 mV between those crossings too, so no bound that keeps V above -50 mV can test it. With slow-wave bounds the A ratio at 10 C is 1.364 or 1.370 and the KCa increase is smallest in LP (+0.03), so no part holds under any of the four readings.")
r('currentscapes-dominant-currents', True, 'reproduced',
  "Cell 31: Na leads in 1.000 of 26,868 spikes and Kd in 1.000. H inward and synaptic outward hold the largest shares in 0.993 of 456 cases.",
  "No change.")
r('fig5-a-to-kca-tradeoff', True, 'reproduced',
  "Cell 33, FGFKQS: Spearman is -1.000 for A and +1.000 for KCa. A exceeds KCa at 10 C (0.31 vs 0.08) and KCa exceeds A at 25 C (0.58 vs 0.08). J9U8SQ has no crossover.",
  "No change.")
r('fig6-crash-different-mechanisms', True, 'not_reproduced',
  "Cell 38: at 30 C the PD cell of FGFKQS is not quiescent. It fires 1005 spikes in 30 s, class \"other\", with V from -59.7 to 14.9 mV. Both the reproduced and the partial criteria need PD quiescent in both models.",
  "No change of outcome. The dominant currents are now taken from the last 3 s of the same 40 s run that is classified (problem 10); they are unchanged (H and KCa in FGFKQS, H and Syn in 71G6LA). With a 0 mV threshold FGFKQS's PD is not quiescent either (336 spikes).")
r('fig6s1-crash-mechanisms', True, 'not_reproduced',
  "Cell 40: 7 of 8 models are present and all 7 crash, but there are only 5 distinct patterns, and B7SD0L, J9U8SQ and EF84RN share (H, Syn) in all three cells. Reproduced is ruled out. Partial would need the missing Q8FBN1 to supply a sixth pattern. The crash temperature is taken from the 40 s runs, but the dominant currents from separate 13 s runs (problem 10).",
  "No change of outcome. The dominant currents now come from the last 3 s of the same 40 s runs; there are still 5 distinct patterns, with SJR46Y in place of EF84RN among the models that share H and Syn in all cells. The 13 s runs are kept as a variant.")
r('fig7-high-temperature-slow-timescales', True, 'blocked',
  "Confirmed: G81PUL, G7EOZ8 and SAXT8Y are not in the deposit under any near spelling. Of the two present, KMNLBC at 30 C is triphasic with a longest gap of 0.68 s, and J9U8SQ at 34 C diverges to NaN (cell 42). Reproduced is therefore already ruled out.",
  "No change of outcome. Reading (b) is now computed for KMNLBC (dominant period of the slow voltage 0.35, 0.35 and 0.29 s), and the Java is shown to give NaN for J9U8SQ at 34 C at the same step as the port. The notes say that reproduced is ruled out even with the missing models.")
r('fig8a-hysteresis-quiescence', True, 'reproduced',
  "Ramps cell 7, 0SHNMD: the last PD spike on the way up is at 34.16 C and the first on the way down at 32.22 C, a difference of 1.94 C (within 2+-0.2), with PD quiescent across the top.",
  "No change.")
r('fig8-up-down-ramps', False, 'not_reproduced',
  "Not reproduced (provisional). Ramps cell 9: on the reading that was run, 22 of 38 models are similar, against 34+-3; it is 28 even at a 20% bound. The notebook calls this blocked (too_large), but the reason is compute time, not data size, and \"too_large\" is not a valid blocked reason for a run of about one hour. The alternative 60-minute 10-25 C ramp was not run, and that is the ramp the paper cites for this sentence (Fig. 1-S2E), so the reading left out may be the one the paper used.",
  "Kept blocked (too_large); the disagreement is recorded. The criterion is met when either reading is within tolerance, so the first reading's 22 cannot decide the outcome while the second is untested. The second reading is now timed in the notebook on a subset: 113 min for 38 models at 40 simulated seconds per second, beside a notebook that already takes 58 of its 60 min. The protocol (Author, Develop on a subset) names too_large for a computation estimated over the notebook limit or the time left. The notes say that the second reading is the ramp the paper cites, and that a run of it split over two notebooks would settle the claim.")
r('fig8b-pathological-attractor', True, 'not_reproduced',
  "Ramps cell 11, H5AIZR: PD returns to regular bursting at 17.08 C (target 20+-2) and the longest ISI between 25 and 35 min is 11.3 s (target 1+-0.1). Both numbers are out of tolerance, and partial allows only one. PD is already regular again from 32 C on the up ramp.",
  "No change.")
r('fig9a-remove-a-current', True, 'partially_reproduced',
  "Cell 45, \"Results\" timing: at 10 C the network is not triphasic and the cells are irregular. At 25 C PY bursts irregularly but PD and LP are also irregular, which is the partial clause. No timing gives PD and LP regular.",
  "No change.")
r('fig9b-remove-kca-current', True, 'reproduced',
  "Cell 47, FGFKQS, under both the \"code\" and \"Results\" timings: at 10 C the network stays triphasic and frequency drops from about 1.06 to about 0.91 Hz; at 25 C all three cells are quiescent.",
  "No change.")
r('fig10a-graded-removal', True, 'partially_reproduced',
  "Cell 49: 3 of 5 checks hold. Both KCa checks fail: at 10 C, KCa 25% and 0% give LP tonic spiking; at 25 C, KCa 0% leaves LP tonic. This depends on the removal protocol (problem 1): the conductance is removed from t = 0, while Fig. 9 removes it after a control period, as the deposit's removal script does, and the notebook's own outputs show the choice changes the result; both protocols should have been run, and the count could rise to 4 or 5.",
  "No change of outcome. Both protocols are now run. With 20 s of control first (the Results' protocol for Figure 9 and the deposit's script; adopted as the main one and marked assumed), 4 of 5 checks hold: both KCa checks now pass and the CaT and CaS check fails, as CaS at 0% gives the same cell classes at 10 and 25 C. From t = 0, 3 of 5. Both are partial. Measured changed from 3 to 4.")
r('fig10b-complete-removal-differs', True, 'not_reproduced',
  "Cell 51: the H part fails under every reading, with 31 models the same and quiescent against the 33 needed. Restricting to 36 models cannot raise that count. The CaT part fails under reading (b) (0.474). Problem 1 applies here too.",
  "No change of outcome. Both protocols are now run. With the control period first, H gives 30 same and quiescent, CaT is the largest under both readings (0.895, 0.605), and 5 of 6 other currents fall within 0.3 to 0.7 under the four-class reading; the H part still fails under every reading and protocol.")
ver=dict(date='2026-11-28', kind='agent',
 by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
 reviewed=("Round 1: the three executed notebooks with the conclusion cells and the summaries removed, the helper module "
  "and the claims file, with the paper's full text under paper/. The verifier checked the archive through Dryad's API "
  "(version 94811 is the only version; one zip of 99,026 bytes whose MD5 matches the one the notebook checks) and ran "
  "bursts, burst_stats, classify_cell, triphasic, cycle_largest_isi, shares and spike_shapes on synthetic spike trains "
  "and voltage traces. It found no place where the claims file misreads the paper. Its other points, answered in the "
  "responses or here: continuous irregular spiking with no gap over 200 ms is labelled other (kept; it does not decide "
  "an outcome, as every claim that meets it needs another class); the 0 mV threshold promised in the helper's docstring "
  "is now computed (spike-threshold-variant cell: 22 of 76 runs change class, as some cells peak below 0 mV); the ramp "
  "update is described the same way in the helper and the ramps notebook (every 20 steps); KNMLBC read as KMNLBC stays "
  "a stated assumption; which 36 of the 38 models the paper used cannot be told from the files (finding 3)."),
 results=R)
d.setdefault('verifications', [])
d['verifications'].append(ver)
yaml.safe_dump(d, open(P,'w'), width=110, sort_keys=False, allow_unicode=True)
print('ok')
PYEOF
cd  && python3 $TMPDIR/ver.py && python tools/entry.py check entries/alonso-2020 2>&1 | tail -20; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls tools; grep -ln "attempt.schema" tools/*.py | head
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_osf_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
build_zenodo_targets.py
changed_entries.py
claims_check.py
colab.py
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def check\b\|def check(\|attempts/\|verifications\|proposed" tools/entry.py | head -30; ls tests | head
```

```
179:def check(entry_dir: Path) -> Report:
414:        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
422:        for rnd in (attempt.get("verifications") or [])[1:]:
444:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
conftest.py
test_build_osf_targets.py
test_build_site.py
test_build_targets.py
test_build_zenodo_targets.py
test_intake.py
test_notify.py
test_protocol_pin.py
test_publish_site.py
test_readme_row.py
```

**Agent calls Bash**

```bash
cd  sed -n 380,470p tools/entry.py
```

```
f"the finding the one dataset they are of (`datasets:`)")
                if f.get("fixed_in") in (f.get("versions") or []):
                    report.error(where, f"finding {n}: version {f['fixed_in']} is both one it was seen in and the "
                                        f"one it was fixed in")
            # The code that shows a finding: a tagged cell of one of the entry's notebooks, as for an outcome. From
            # pilot-19 a critical or major finding about the data names its cell; an earlier attempt was not asked.
            shown, tag = f.get("notebook"), f.get("output")
            if bool(shown) != bool(tag):
                report.error(where, f"finding {n}: give the notebook that shows it and its cell together "
                                    f"(`notebook` and `output`)")
            if (version and int(version[1]) >= 19 and about == "data" and f.get("severity") in ("critical", "major")
                    and not shown):
                report.error(where, f"finding {n}: it is {f['severity']}; name the notebook and the tagged cell whose "
                                    f"output shows it (`notebook`, `output`)")
            # As for an outcome, only the latest attempt's cells are checked against the entry as it is now.
            if shown and path == mine[-1]:
                if shown not in listed:
                    report.error(where, f"finding {n}: notebook {shown!r} is not in the entry")
                elif shown in present and tag:
                    cells = nbformat.read(entry_dir / shown, as_version=4).cells
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" attempts/alonso-2020-01.yaml entries/alonso-2020/*.py entries/alonso-2020/*.ipynb entries/alonso-2020/README.md | head; git status --short; python - <<'EOF'
import yaml; d=yaml.safe_load(open('attempts/alonso-2020-01.yaml'))
print(len(d['outcomes']), len(d['findings']), len(d['verifications']), len(d['verifications'][0]['results']))
EOF
```

```
M attempts/alonso-2020-01.yaml
 M entries/alonso-2020/README.md
 M entries/alonso-2020/pyloric.py
 M entries/alonso-2020/ramps.ipynb
 M entries/alonso-2020/reproduce_alonso_2020.ipynb
 M entries/alonso-2020/voltage_distributions.ipynb
 M tools/build_site.py
 M tools/runner/chain.sh
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
23 7 1 23
```

**Agent calls Bash**

```bash
cd  git diff attempts/alonso-2020-01.yaml | grep "^[-+]" | grep -n "outcome:\|measured\|assumed" | head -20; date -u
```

```
14:-    for LP and PY. The measured values are the means over models and cells of burst frequency
24:+    0.2 +- 0.02 for PD duty cycle, 14 within 0.25 +- 0.025 for LP and PY. The measured values are the means over
130:-  - The ramp reading (38 models, 3600 s each) would add about 35 min to a notebook (measured on a
136:-  outcome: partially_reproduced
137:+  outcome: reproduced
151:+    the search limit at 2 of 26 temperatures). Amplitude (a) and threshold (b) meet the criterion. The measured
153:+    is assumed; the question is for the paper's authors (finding 6).
158:+  - 'Threshold reading (b) is located by an assumed rule (pyloric.spike_region_start): the highest voltage below
162:+  assumed: true
163:+  measured:
251:-    on the -20 mV spike threshold (assumed).
253:+    reached 30 C (a ramp or a fresh start) is not stated, and the classes rest on the -20 mV spike threshold (assumed).
309:-    processes, measured on a subset), over the notebook limit, and was not run, so the outcome
333:-    the down ramp; the classification rests on the -20 mV spike threshold (assumed).
335:+    classification rests on the -20 mV spike threshold (assumed).
348:-    spike threshold and the order test (assumed).
350:+    and the order test (assumed).
361:-  measured: 3
368:+  measured: 4
380:-    spike threshold and the order test (assumed).
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
P='attempts/alonso-2020-01.yaml'
d=yaml.safe_load(open(P))
o=[o for o in d['outcomes'] if o['claim']=='fig2-lp-spike-amplitude-threshold'][0]
o.pop('measured')
o['notes']=o['notes'].replace(" The measured values are the Spearman correlations of amplitude (a) and threshold (b) at 5%.","")
yaml.safe_dump(d, open(P,'w'), width=110, sort_keys=False, allow_unicode=True)
EOF
python tools/entry.py check entries/alonso-2020 2>&1 | tail -3
```

```
0 error(s)
```

**Agent**

I re-ran the entry once with `python tools/entry.py all entries/alonso-2020`, and all three notebooks passed: main 31 min, ramps 58 min, voltage 24 min. The checks pass with 0 errors. I wrote the conclusions after the run and copied the same markdown into the executed copies, so the entry's files are newer than the run stamp and the next run will execute fresh.

**Outcome changes**
- **fig2-lp-spike-amplitude-threshold:** now reproduced, marked assumed (was partially reproduced). Threshold reading (b) is now computed, as the upper edge of the densely occupied part of the voltage distribution below -20 mV. At the main setting (5%) it rises from -36.1 to -26.5 mV with Spearman 0.997, and the 2% and 10% settings agree. Amplitude still falls (Spearman -1.0). How to locate that point is my assumption, so I added it to the questions for the paper's authors.
- **fig8-up-down-ramps:** still blocked (too_large). I recorded the verifier's disagreement (it would give not_reproduced). The criterion passes if either ramp reading is within tolerance; the first gives 22 of 38, and the second is untested. The notebook now times the second reading on a subset at 113 min, while that notebook already takes 58 of its 60 min.
- All other outcomes are unchanged.

**Added or corrected, by verifier point**
1. **fig10a/fig10b:** both removal protocols now run. The main one, marked assumed, runs 20 s with every conductance intact first, as the Results do for Fig. 9 and as the deposit's removal script does; removal from t = 0 is the variant.
   - fig10a: 4 of 5 checks hold with the control period first, 3 of 5 from t = 0. Both are partial; measured changed from 3 to 4.
   - fig10b: the H part still fails under every reading and protocol (30 or 31 models, 33 needed).
2. **fig8 second reading:** not run; timed in the notebook (see above).
3. **fig2 threshold reading (b):** computed (see above).
4. **fig4:** added burst bounds at the -50 mV slow-wave crossings. The leak's inward share is still 0: V stays above -50 mV between those crossings, so no such bound can test it. No part of the criterion holds under any of the four readings.
5. **Java check:** the Java now matches the port at 25 °C (0.06 mV over 3 s). For G7P2WE at 35 °C and J9U8SQ at 34 °C it gives NaN at exactly the same step as the port, so the divergence is in the deposited code. Finding 5 now says so.
6. **Parameters:** a new cell compares the deposited values with the Methods' search space. gNa, gA, gKd, the synaptic conductances, and tau_Ca as the Java uses it fall outside it. Recorded as new finding 7 (minor, about the data), added at the end so the other findings keep their numbers.
7. **0 mV spike threshold:** now computed. It changes the cell classes in 22 of 76 runs, and only 17 of 38 models stay triphasic at both 10 and 25 °C. Some cells' spikes peak below 0 mV, which supports keeping -20 mV.
8. **Ramp update:** the notebook text now matches the helper (every 20 steps).
9. **figs3:** the notes now say the test detects small differences and shows little more than that the distributions differ.
10. **fig6/fig6s1:** the dominant currents now come from the same 40 s runs that are classified. fig6s1 still has 5 distinct patterns; the model sharing H and Syn with B7SD0L and J9U8SQ is now SJR46Y.

Other outputs the verifier asked for:
- **intermediate-temperature-failures:** the README and the file-name scores are printed. Nothing ties the 38 files to the 40 screened solutions, so the claim stays blocked.
- **fig7:** reading (b) for KMNLBC gives periods of 0.29 to 0.35 s, so no slow time scale appears.

The round is recorded under `verifications` with all 23 claims, and the questions for the paper's authors gained two (the Fig. 10 protocol and the Fig. 2 threshold).

**Not done**
- The second fig8 ramp reading and the per-model ramp for figs3. They would take 113 and 57 minutes and do not fit within the notebook limit.
- No questions were added to `questions/alonso-2020.yaml`: the verifier found no place where the claims file misreads the paper.
- No `findings` entry for round 2: the record has no finding rated critical.
- I left the classification of continuous irregular spiking as "other". It decides no outcome.
- I did not commit or push.

## End of run

71 turns, 144 minutes, $6.94 at API prices, result: success.
