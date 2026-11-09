# 000946 · verifier-1 · run 41255267042

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 464
drwxr-xr-x 6 runner runner    4096 Nov  1 00:16 .
drwxr-xr-x 7 runner runner    4096 Nov  1 00:16 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:05 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:05 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  1 00:16 .claude
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env.development
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env.local
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env.production
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env.test
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .env.test.local
drwx------ 2 runner runner    4096 Nov  1 00:16 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:05 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:05 .github
-rw-r--r-- 1 runner runner       0 Nov  1 00:16 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:05 .idea
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025) on dandiset 000946.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	# Source: the version of record (J Neurosci 45(23) e2218242025, PMC12139594), full text as served
5	# by PMC: Abstract, Introduction, Materials and Methods, Results, figure legends and Discussion.
6	# The paper has no supplement (no Extended Data is cited). No PDF was supplied. The equation that
7	# defines the directional spike time tiling coefficient (dSTTC) is missing from the text read; only
8	# its description in words survives (Methods, Directional spike time tiling coefficient), and the
9	# symbols in that description are stripped. The paper links no analysis code, so no code was read.
10	#
11	# Data the paper used, as it reports them. Male Wistar rats under isoflurane (2%). Group 1 (N = 16):
12	# two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5, 1 to 1.3 mm deep, layers III to V)
13	# and one in POm (AP -4.5, ML 2.6, 5.8 mm). Group 2 (N = 12): S1 and auditory cortex (AC, AP -4.5,
14	# ML 6.5). tFUS from a 128-element array (1.5 MHz) aimed at S1, about 88 kPa in situ. Each session
15	# is one parameter set: 500 trials, ultrasound duration (UD) 67 ms, intersonication interval 2.5 s
16	# with 10% jitter, order of conditions randomized. PRFs 30, 300, 1500, 3000, 4500 Hz; duty cycles
17	# (DC) 0.6, 6, 30, 60, 90%; DC = PRF x pulse duration (PD). The PRF series uses PD 200 us, so 30,
18	# 300, 1500, 3000 and 4500 Hz are 0.6, 6, 30, 60 and 90% DC. DC series at 3000 Hz and at 30 Hz,
19	# and a PRF series at 60% DC. Sham sessions have no tFUS; control sessions aim tFUS at cingulate
20	# cortex (CG1, AP 3, ML 0). The dandiset description says each session's identifier holds the PRF
[... 819 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "tfus.py"
}
```

```
1	"""Loading and spiking measures for dandiset 000946 (Gao, Ramachandran, Yu & He 2025).
2	
3	The dandiset holds one NWB file per recorded area and session: a units table with
4	spike times and a `celltype_label` column, and a trials table whose `start_time`
5	is taken as sonication onset (checked in the notebook). The session's parameters
6	are in `identifier` (`<rat>_<PRF>_<PD>_<UD>_<n>[_suffix]`), `general/notes`
7	(`Recording:<area>; stim at:<target>`) and `general/data_collection`
8	(`tFUS parameters {PRF:..Hz PD:..us UD:67ms}`).
9	
10	Where each parameter comes from:
11	
12	- `MIN_SPIKES = 2000`: Methods, Neuronal type classification ("Only neurons that
13	  fire >2,000 spikes for each session were considered"); the claims file header,
14	  Units.
15	- `WINDOWS` (67 ms bins from sonication onset, 0 to 268 ms) and the baseline
16	  [-67, 0) ms: claims file header, Windows, and Statistical analysis ("normalized
17	  to the pre-stim period (67 ms pre-stim)").
18	- `normalized_rates`, readings N1 and N2, and the comparison windows B1 and B2:
19	  claims file header, Normalized spiking rate and Test against baseline.
20	- `vs_baseline`: one-tailed two-sample Wilcoxon (rank-sum) test against the
[... 266 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 839
}
```

```
839	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 1; Figure 10B
840	  quote: When delivering 30 Hz ultrasound, S1 RSUs to POm FSUs higher correlated (p = 0.0058), while
841	    POm RSUs showed decreased correlation to S1 FSUs during sonication (p = 0.0058).
842	  statistics:
843	  - about: S1 RSU to POm FSU, increase
844	    test: one-tail two-sample Wilcoxon against prestimulation correlation
845	    p: 0.0058
846	  - about: POm RSU to S1 FSU, decrease
847	    test: one-tail two-sample Wilcoxon against prestimulation correlation
848	    p: 0.0058
849	  criterion: The header's dSTTC method on the 30 Hz, 200 us sessions, the first bin from 0 ms.
850	    Reproduced when, under every dSTTC reading (D1, A1/A2, W1/W2, S1/S2) and every cell-type
851	    reading, S1 RSU to POm FSU is above
852	    prestimulation and POm RSU to S1 FSU below it (one-tailed, p < 0.05); partially reproduced
853	    when one holds.
854	- id: fig10c-sttc-constant-pd
855	  statement: With constant 200 us PD, the S1 RSU to POm RSU correlation change during sonication
856	    shows no PRF dependence overall, though 1500 Hz gives a higher change than 30 Hz.
857	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10C
858	  quote: When applying tFUS with constant 200 μs PD, varying the DC and PRF, the correlation did not
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" *.yaml; python3 -c "
import json
nb=json.load(open('reproduce_gao_2025.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'=== [{i}] {c[\"cell_type\"]} ===')
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: t=''.join(o['text'])
            elif 'data' in o and 'text/plain' in o['data']: t=''.join(o['data']['text/plain'])
            elif o.get('output_type')=='error': t='ERROR '+o['ename']+o['evalue']
            else: t='<'+','.join(o.get('data',{}).keys())+'>'
            print('--- out ---'); print(t[:6000])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
10.1523-jneurosci.2218-24.2025.yaml:33
pnpm-lock.yaml:0
829 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	30
2	=== [0] markdown ===
3	# Reproducing Gao, Ramachandran, Yu & He (2025) from dandiset 000946
4	
5	Paper. Gao H, Ramachandran S, Yu K, He B (2025). Transcranial focused ultrasound modulates feedforward
6	and feedback cortico-thalamo-cortical pathways by selectively activating excitatory neurons. *J Neurosci*
7	45(23): e2218242025. [doi:10.1523/jneurosci.2218-24.2025](https://doi.org/10.1523/jneurosci.2218-24.2025).
8	The claims file (`claims/000946/10.1523-jneurosci.2218-24.2025.yaml`) was written from the version of
9	record as served by PubMed Central (PMC12139594): main text, Methods and figure legends; the paper has no
10	supplement and links no analysis code.
11	
12	Dandiset. [DANDI:000946](https://dandiarchive.org/dandiset/000946/0.250829.1249), version
13	0.250829.1249. The paper cites the dandiset without a version (Methods, Electrophysiological recordings:
14	"All experimental data has been made public in a repository at the DANDI Archive
15	(https://dandiarchive.org/dandiset/000946)"), so the most recent published version is pinned. The data
16	check below compares its file list with the earliest published version, 0.250711.1640; all six published
17	versions list the same 1920 files.
18	
19	What the dataset holds. One NWB file per recorded area and session, each with a units table (spike
20	times and a `celltype_label` column) and a trials table. There are no spike waveforms in any file, and
[... 810 more lines not kept]
```

**Agent**

Notebook read: 33 claims, only fig11b tested. Now checking the archive metadata and testing the helpers on synthetic inputs.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import requests,json
API="https://api.dandiarchive.org/api"
r=requests.get(f"{API}/dandisets/000946/versions/0.250829.1249/info/",timeout=60).json()
m=r['metadata']
print(m.get('description','')[:3000])
print(json.dumps(m.get('assetsSummary',{}),indent=0)[:1500])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/info/" -o info.json; python3 -c "
import json;m=json.load(open('info.json'))['metadata']
print(m.get('description','')[:3000]); print(json.dumps(m.get('assetsSummary',{}))[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json,subprocess,collections
url="https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=1000"
paths=[]
while url:
    js=json.loads(subprocess.check_output(["curl","-s",url]))
    paths+= [(a["path"],a["size"]) for a in js["results"]]; url=js["next"]
print(len(paths))
c=collections.Counter(p.split('/')[0] for p,_ in paths); print(c)
print(collections.Counter(p.rsplit('.',1)[-1] for p,_ in paths))
sz=[s for p,s in paths if not p.startswith('sub-STTC')]; print(min(sz),sorted(sz)[len(sz)//2],max(sz))
EOF
```

```
1920
Counter({'sub-BH528': 117, 'sub-BH511': 115, 'sub-BH513': 109, 'sub-BH538': 94, 'sub-BH535': 92, 'sub-BH539': 92, 'sub-BH553': 92, 'sub-BH547': 88, 'sub-BH551': 88, 'sub-BH532': 85, 'sub-BH501': 78, 'sub-BH558': 78, 'sub-BH499': 77, 'sub-BH495': 75, 'sub-BH537': 73, 'sub-BH530': 64, 'sub-BH494': 53, 'sub-BH510': 48, 'sub-BH500': 31, 'sub-STTC-BH528': 30, 'sub-STTC-BH513': 28, 'sub-STTC-BH510': 25, 'sub-STTC-BH535': 24, 'sub-STTC-BH495': 23, 'sub-STTC-BH511': 23, 'sub-STTC-BH538': 23, 'sub-STTC-BH553': 23, 'sub-STTC-BH499': 22, 'sub-STTC-BH547': 21, 'sub-STTC-BH551': 21, 'sub-STTC-BH501': 20, 'sub-STTC-BH532': 20, 'sub-STTC-BH530': 16, 'sub-STTC-BH537': 13, 'sub-STTC-BH494': 11, 'sub-STTC-BH539': 10, 'sub-STTC-BH558': 10, 'sub-STTC-BH500': 7, 'sub-BH594': 1})
Counter({'nwb': 1920})
228704 2503784 12566224
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, sys, types
for m in ["h5py","remfile","requests"]:
    sys.modules.setdefault(m, types.ModuleType(m))
import tfus
sp=np.array([0.0,0.066,0.067,0.1,0.2,0.267,0.268,-0.01,-0.067])
print(tfus.window_counts(sp,np.array([0.0]),(0,0.067)), tfus.window_counts(sp,np.array([0.0]),(-0.067,0)), tfus.window_counts(sp,np.array([0.0]),(0.201,0.268)))
c=dict(base=np.array([0,1,2,0]),pre=np.array([1,1,1,1]),w=np.array([2,2,2,2]))
print(tfus.normalized_rates(c,"w","N1"), tfus.normalized_rates(c,"w","N2"), tfus.normalized_rates(c,"base","N2"))
# N2 bias with Poisson no-stim
rng=np.random.default_rng(0); lam=0.5
b=rng.poisson(lam,500); x=rng.poisson(lam,500)
print("N1",tfus.normalized_rates(dict(base=b,w=x),"w","N1"),"N2",tfus.normalized_rates(dict(base=b,w=x),"w","N2"))
# vs_baseline null calibration under N1,B1 (baseline sample constant 100)
ps=[]
for k in range(500):
    units=[dict(base=rng.poisson(lam,500),w=rng.poisson(lam,500)) for _ in range(100)]
    x=[tfus.normalized_rates(u,"w","N1") for u in units]; base=[100.0]*100
    ps.append(tfus.vs_baseline(x,base,1)[1])
print("N1/B1 null false-positive rate at 0.01:", np.mean(np.array(ps)<0.01))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* ; which -a python3 python; pip --version 2>&1; ls ~/.venv* /opt 2>/dev/null | head
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/pip (python 3.13)
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && v/bin/pip -q install numpy scipy 2>&1 | tail -2; v/bin/python -c "import numpy,scipy;print(numpy.__version__,scipy.__version__)"
```

```
2.5.4 1.18.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, sys, types
for m in ["h5py","remfile","requests"]:
    sys.modules.setdefault(m, types.ModuleType(m))
import tfus
sp=np.array([0.0,0.066,0.067,0.1,0.2,0.267,0.268,-0.01,-0.067])
print(tfus.window_counts(sp,np.array([0.0]),(0,0.067)), tfus.window_counts(sp,np.array([0.0]),(-0.067,0)), tfus.window_counts(sp,np.array([0.0]),(0.201,0.268)))
c=dict(base=np.array([0,1,2,0]),pre=np.array([1,1,1,1]),w=np.array([2,2,2,2]))
print(tfus.normalized_rates(c,"w","N1"), tfus.normalized_rates(c,"w","N2"), tfus.normalized_rates(c,"base","N2"))
rng=np.random.default_rng(0); lam=0.5
b=rng.poisson(lam,500); x=rng.poisson(lam,500)
print("N1",tfus.normalized_rates(dict(base=b,w=x),"w","N1"),"N2",tfus.normalized_rates(dict(base=b,w=x),"w","N2"))
for B in ["B1","B2"]:
  ps=[]
  for k in range(300):
    units=[dict(base=rng.poisson(lam,500),pre=rng.poisson(lam,500),w=rng.poisson(lam,500)) for _ in range(100)]
    x=[tfus.normalized_rates(u,"w","N1") for u in units]; base=tfus.baseline_sample(units,"N1",B)
    ps.append(tfus.vs_baseline(x,base,1)[1])
  print(B,"N1 null false-positive rate at 0.01:", np.mean(np.array(ps)<0.01))
EOF
```

```
[2] [2] [1]
266.6666666666667 150.0 100.0
N1 86.47686832740213 N2 45.399698340874814
B1 N1 null false-positive rate at 0.01: 0.023333333333333334
B2 N1 null false-positive rate at 0.01: 0.0
```

**Agent**

**Verifier report, round 1: Gao et al. 2025 (J Neurosci), DANDI:000946 v0.250829.1249**

The claims file has 33 claims. The notebook tests one of them (fig11b) and treats the other 32 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig4-unit-counts | **not_reproduced** | The notebook calls this blocked, but its own totals in cell 17 decide it. POm units at 3000 Hz are 352 against 233+17 = 250, and at 30 Hz 315 against 232. Both are far outside 10%, so neither the "reproduced" outcome (eight counts in tolerance) nor the "partial" one (area totals within 10%) can be reached under any RSU/FSU split. |
| fig4a-s1-rsu-time-locked-3000 | blocked (data_missing) | Cell 4: `celltype_label` is 0 in all 1516 files that have it and absent in the other 34. No file has waveforms, and no acquisition, analysis or processing group has content. The archive agrees: variableMeasured is Units and ElectrodeGroup only, and unit files are at most 12.6 MB. |
| fig4b-pom-rsu-time-locked-3000 | blocked (data_missing) | Same: needs RSU typing. |
| fig4-postsonication-3000 | blocked (data_missing) | Same. |
| fig4-30hz-responses | blocked (data_missing) | Same. |
| fig4-fsu-no-change | blocked (data_missing) | Same: needs FSU typing. |
| fig5a-sham-no-change | blocked (data_missing) | No cell types. Cell 8: no identifier, note or data_collection field names sham or no tFUS. |
| fig5b-cg1-control-no-change | blocked (data_missing) | No cell types, and no session is aimed at CG1. Targets in the data are only S1, M1 and POm (cell 8). |
| fig6-unit-counts | **not_reproduced** | Cell 17 again. S1 totals are 986, 1726 or 2414 depending on the S1 selection, against 1297 ±10% (1167 to 1427). POm is 1470 against 1019 ±10%. No split can rescue either. |
| fig6a-s1-rsu-time-locked-prf | blocked (data_missing) | Needs RSU typing. |
| fig6a-s1-rsu-delayed-prf | blocked (data_missing) | Same. |
| fig6b-s1-fsu-prf | blocked (data_missing) | Same. |
| fig6c-pom-rsu-prf | blocked (data_missing) | Same. |
| fig6d-pom-fsu-prf | blocked (data_missing) | Same. |
| fig7a-s1-rsu-dc-3000 | blocked (data_missing) | Same. |
| fig7b-s1-fsu-dc-3000 | blocked (data_missing) | Same. |
| fig7c-pom-rsu-dc-3000 | blocked (data_missing) | Same. |
| fig7d-pom-fsu-dc-3000 | blocked (data_missing) | Same. |
| fig8a-s1-rsu-dc-30 | blocked (data_missing) | Same. |
| fig8b-s1-fsu-dc-30 | blocked (data_missing) | Same. |
| fig9a-s1-rsu-prf-60dc | blocked (data_missing) | Same. |
| fig9b-s1-fsu-prf-60dc | blocked (data_missing) | Same. |
| fig10a-dsttc-3000 | blocked (data_missing) | dSTTC between typed S1 and POm units. The stored STTC arrays carry no unit types (cell 19). |
| fig10b-dsttc-30 | blocked (data_missing) | Same. |
| fig10c-sttc-constant-pd | blocked (data_missing) | Needs S1 RSU to POm RSU STTC. The stored STTC is untyped and its dt is not stated (cell 19: array shape (10 windows, 499 trials, 20, 9), with no dt axis). |
| fig10d-sttc-60dc | blocked (data_missing) | Same. |
| fig10e-sttc-dc-30 | blocked (data_missing) | Same. |
| fig10f-sttc-dc-3000 | blocked (data_missing) | Same. |
| pathway-follows-local-prf | blocked (data_missing) | Depends on fig6a and fig10c, both blocked. |
| fig11b-ac-responses | **blocked (methods_underspecified)** | Cell 24: the four method readings give different outcomes. N1/B1 is partial (during-sonication set {1500, 3000, 4500}, one PRF too many). N1/B2 is not reproduced (300 Hz also above baseline during sonication). N2/B1 and N2/B2 are not reproduced (Kruskal-Wallis in 0–67 ms p = 0.0213). The claims header says that when readings differ, the claim is blocked as methods_underspecified with every result shown. No reading reproduces the claim. The unit count is 633 against 453 ±45.3, outside tolerance. |
| fig11c-ac-to-s1-30hz | blocked (data_missing) | The target units must be S1 RSUs, which are untyped. |
| fig11d-ac-to-s1-3000 | blocked (data_missing) | Needs S1 RSUs and S1 FSUs. |
| auditory-confound-low-prf | blocked (data_missing) | Depends on fig11c and fig11d. |

For the cell-type claims, I checked the archive itself (API metadata and the full asset list). Its 1920 files are all NWB: 1550 unit files and 370 STTC files, with nothing else. File sizes, at most 12.6 MB for unit files, are consistent with spike times only. Nothing would let any RSU/FSU claim be tested in part. The paper does not state a chance level for any selection, so there was none to compare.

### B. Problems

1. **[affects a conclusion]** Cell 0 table and cell 17: fig4-unit-counts and fig6-unit-counts are marked blocked. The totals the notebook prints already rule out both the reproduced and the partial outcome, so the criterion gives "not reproduced". This is subject to item 6.
2. **[affects a conclusion]** fig11b, cells 24–25: the four readings disagree, so the claims header's rule makes the outcome blocked (methods_underspecified). The notebook's `judge` gives a verdict per reading but never combines them under that rule. Any single verdict taken from the N1/B1 row ("partially reproduced") would break the claims file.
3. **[does not affect a conclusion]** Claims file, reading N2: averaging per-trial ratios over trials with a nonzero baseline is biased low. The notebook shows this: 50–62% at onsets shifted by 1 s, where there is no stimulus (cell 27). My synthetic Poisson test (λ = 0.5 per window, no effect) gives N1 ≈ 86% versus N2 ≈ 45%. N2 is therefore not a reasonable reading of "normalized to the pre-stim period". This is a claims-file problem, which I report and do not correct. Dropping N2 would not change fig11b, because N1/B1 and N1/B2 still disagree.
4. **[does not affect a conclusion]** Claims file, reading B1 under N1: the "baseline sample" is exactly 100 for every unit, so the rank-sum test is effectively a one-sample location test. On synthetic null data, `vs_baseline` with B1 had a false-positive rate of 2.3% at α = 0.01. With B2 it was 0%. The fig11b p-values are far from the threshold, so no decision changes.
5. **[does not affect a conclusion]** fig11b pooling, cells 23 and 28: each PRF comes from only 3 or 4 of 6 rats, and the rats differ by PRF. Single rats dominate some means; for example BH538 at 3000 Hz, 201–268 ms, averages 654% against a pooled 310.5%. So the Kruskal-Wallis across PRFs confounds PRF with rat. The paper probably pooled the same way, so this is a caveat, not an error.
6. **[could affect the count outcomes]** Cells 10 and 17, session selection: PD 200 µs, tFUS at S1, area exactly "S1", "POM" or "AC". This keeps identifiers with suffixes (POM_POM, NEAR, back, front, contra, NEW, _2, dep05, cell 8), which may be repeat or off-target placements the paper left out. It also drops the AC_1, AC_2 and S1_1 files of a seventh AC rat. The count verdicts in item 1 assume every such session counts. The criterion's wording ("sessions of the S1 and POm rats") supports that, but it was not checked.
7. **[does not affect a conclusion]** Cells 12–15: trial `start_time` is assumed to be sonication onset. The 1 s-shift control and the PSTHs show it is stimulus-locked, but not that it has zero latency. The notebook says this itself.
8. **[does not affect a conclusion]** Helpers checked on synthetic inputs: `window_counts` uses half-open windows [a, b) correctly, `normalized_rates` (N1 and N2) and `vs_baseline` (Bonferroni factor 5, as in reading C1) behave as described, and `dedupe` is confirmed by spike-time hashes (734 of 734 identical). No train/test split exists, so leakage does not apply.
9. **[does not affect a conclusion]** Cell 9: the dataset has 20 rats, while the paper reports 16 S1/POm rats and 12 S1/AC rats. It also holds M1 recordings and tFUS aimed at M1 or POm, which the paper does not describe. Despite having fewer AC rats (7 vs 12), it has more AC units (633 vs 453). The paper's selection evidently differs, and the notebook does not investigate why.

### C. What I could not check, and the output that would settle it

- **Whether suffixed sessions belong in the paper's sets** (items 1 and 6). I need the unit totals per area and PRF from cell 17, broken down by identifier suffix and by rat. That would show whether excluding repeat or off-target sessions could bring POm to about 250 and 232 at 3000 and 30 Hz, and 1019 over the PRF series.
- **The seventh AC rat.** I need the PRF, PD and unit counts of its AC_1, AC_2 and S1_1 recordings.
- **Whether any M1- or POm-aimed session matches the CG1 control.** No metadata gives probe or target coordinates. Even if one did, the cell-type block would remain.
- **fig11b at the rat level.** Results with each rat left out, under N1/B1 and N1/B2, would show whether the during-sonication sets and the "lowest at 300 Hz" part depend on BH537 or BH538.
- **SEMs for fig11b.** They are computed but not printed in cell 25. I could only see means and p-values.

## End of run

14 turns, 3 minutes, result: success.
