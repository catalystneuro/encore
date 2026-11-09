# 000637 · verifier-1 · run 41185565407

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 184
drwxr-xr-x 6 runner runner   4096 Oct 31 08:51 .
drwxr-xr-x 7 runner runner   4096 Oct 31 08:51 ..
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 31 08:39 .bash_profile
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 31 08:39 .bashrc
drwxr-xr-x 5 runner runner   4096 Oct 31 08:51 .claude
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env.development
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env.development.local
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env.local
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env.production
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env.production.local
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env.test
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .env.test.local
drwx------ 2 runner runner   4096 Oct 31 08:51 .git
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 31 08:39 .gitconfig
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 31 08:39 .github
-rw-r--r-- 1 runner runner      0 Oct 31 08:51 .gitmodules
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 31 08:39 .idea
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1523-jneurosci.2218-24.2025.yaml
```

```
<persisted-output>
Output too large (54.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/85274f26-f9c6-485b-a0f2-336700452987/tool-results/bs10lygxo.txt

Preview (first 2KB):
# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, on dandiset 000637.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
# Materials and Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt).
# The paper has no supplement. No PDF was supplied. The equation defining the directional spike time
# tiling coefficient (dSTTC) is lost in the text ("The definition for dSTTC is as follows:" is followed
# by the prose that defines its terms, without the formula); its form is treated as open below.
# The paper links no analysis code (no repository and no code availability statement in the text),
# so no code was read.
#
# Data the paper used (Materials and Methods). Male Wistar rats (Hsd WI), 250 to 350 g, 3 to 6 months,
# under 2% isoflurane. Group 1 (N = 16): two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5,
# 40 degrees, 1 to 1.3 mm deep, layers III to V) and one in POm (AP -4.5, ML 2.6, 20 degrees, 5.8 mm).
# Group 2 (N = 12, auditory confound): probes in S1 and auditory cortex (AC; AP -4.5, ML 6.5).
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, on dandiset 000637.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
6	# Materials and Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt).
7	# The paper has no supplement. No PDF was supplied. The equation defining the directional spike time
8	# tiling coefficient (dSTTC) is lost in the text ("The definition for dSTTC is as follows:" is followed
9	# by the prose that defines its terms, without the formula); its form is treated as open below.
10	# The paper links no analysis code (no repository and no code availability statement in the text),
11	# so no code was read.
12	#
13	# Data the paper used (Materials and Methods). Male Wistar rats (Hsd WI), 250 to 350 g, 3 to 6 months,
14	# under 2% isoflurane. Group 1 (N = 16): two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5,
15	# 40 degrees, 1 to 1.3 mm deep, layers III to V) and one in POm (AP -4.5, ML 2.6, 20 degrees, 5.8 mm).
16	# Group 2 (N = 12, auditory confound): probes in S1 and auditory cortex (AC; AP -4.5, ML 6.5).
17	# tFUS from a 128-element random array (H276, 1.5 MHz) steered to S1; ultrasound duration (UD) 67 ms;
18	# intersonication interval 2.5 s with 10% jitter; 500 trials per parameter; condition order randomized.
19	# Conditions: PRF 30, 300, 1500, 3000 and 4500 Hz at constant 200 us pulse duration (which gives DC 0.6,
20	# 6, 30, 60 and 90%); DC 0.6, 6, 30, 60 and 90% at 3000 Hz and at 30 Hz PRF; PRFs at constant 60% DC;
[... 828 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 849
}
```

```
849	    p: 0.0058
850	  - about: POm RSU to S1 FSU, decrease
851	    test: Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon
852	    p: 0.0058
853	  depends_on:
854	  - unit-counts
855	  criterion: Method D, pairs within the 30 Hz 0.6% DC sessions, window 0 to 67 ms against prestimulation. Reproduced
856	    when, under every reading, S1 RSU to POm FSU is significantly higher and POm RSU to S1 FSU significantly lower
857	    (one-tailed, p < 0.05); partially reproduced when one of the two holds.
858	- id: fig10c-sttc-constant-pd
859	  statement: At constant 200 us pulse duration, the S1 RSU to POm RSU correlation change during sonication does
860	    not depend on PRF, though 1500 Hz gives a higher change than 30 Hz.
861	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10C
862	  quote: When applying tFUS with constant 200 μs PD, varying the DC and PRF, the correlation did not show PRF-dependent
863	    change. A total of 1,500 Hz PRF did show a higher correlation change compared with 30 Hz PRF (Fig. 10C; p =
864	    0.02)
865	  statistics:
866	  - about: 1500 against 30 Hz
867	    test: post hoc one-tail two-sample Wilcoxon
868	    p: 0.02
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" *.yaml; cat tfus.py; python3 -c "
import json
nb=json.load(open('reproduce_gao_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
10.1523-jneurosci.2218-24.2025.yaml:31
pnpm-lock.yaml:0
"""Loading and spiking measures for dandiset 000637 (S1 spike times under tFUS).

Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, doi:10.1523/jneurosci.2218-24.2025.

Each NWB file holds one recording from one rat: a Units table with spike times only (no waveforms, no
electrode per unit, electrode locations "unknown"), and a trials table with start and stop times only.
The stimulation condition is coded in the file's identifier, `<subject>_<PRF Hz>_<PD us>_<UD ms>_<V>`
(for example BH401_1500_400_67_5V: PRF 1500 Hz, pulse duration 400 us, ultrasound duration 67 ms, 5 V),
with a trailing `_2`, `_3` on repeated recordings, and `<subject>_BASELINE` for recordings without a
condition. The dandiset's description says so for its sister dandiset 000946 ("in BH494_1500_200_67_5,
the PRF is 1500Hz and PD is 200us"); for 000637 it is read from the values, and the last field is read
as the input voltage (the paper's Methods use "5 V input voltage"). Files are streamed from the archive
at the pinned version; nothing is written to disk.

Where the parameters come from:

- Units with more than 2,000 spikes in the session (`MIN_SPIKES`): Methods, "Neuronal type
  classification and neuronal response quantification" ("Only neurons that fire >2,000 spikes for
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep "^- id:" *.yaml | nl; cat $TMPDIR/nb.txt
```

```
<persisted-output>
Output too large (33KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/85274f26-f9c6-485b-a0f2-336700452987/tool-results/b0jpo0asz.txt

Preview (first 2KB):
     1	10.1523-jneurosci.2218-24.2025.yaml:- id: unit-counts
     2	10.1523-jneurosci.2218-24.2025.yaml:- id: fig4-s1-rsu-timelocked-3000
     3	10.1523-jneurosci.2218-24.2025.yaml:- id: fig4-pom-rsu-timelocked-3000
     4	10.1523-jneurosci.2218-24.2025.yaml:- id: fig4-post-3000
     5	10.1523-jneurosci.2218-24.2025.yaml:- id: fig4-30hz-s1-rsu-inhibition
     6	10.1523-jneurosci.2218-24.2025.yaml:- id: fig4-30hz-pom-rsu-delayed
     7	10.1523-jneurosci.2218-24.2025.yaml:- id: fig4-fsu-no-change
     8	10.1523-jneurosci.2218-24.2025.yaml:- id: fig5-sham-no-response
     9	10.1523-jneurosci.2218-24.2025.yaml:- id: fig5-cg1-control-no-response
    10	10.1523-jneurosci.2218-24.2025.yaml:- id: fig6a-s1-rsu-timelocked-high-prf
    11	10.1523-jneurosci.2218-24.2025.yaml:- id: fig6a-s1-rsu-delayed
    12	10.1523-jneurosci.2218-24.2025.yaml:- id: fig6b-s1-fsu
    13	10.1523-jneurosci.2218-24.2025.yaml:- id: fig6c-pom-rsu-timelocked
    14	10.1523-jneurosci.2218-24.2025.yaml:- id: fig6c-pom-rsu-delayed
    15	10.1523-jneurosci.2218-24.2025.yaml:- id: fig6d-pom-fsu
    16	10.1523-jneurosci.2218-24.2025.yaml:- id: fig7a-s1-rsu-dc-3000
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Gao, Ramachandran, Yu & He (2025) on dandiset 000637
3	
4	**Paper.** Gao H, Ramachandran S, Yu K, He B (2025). Transcranial focused ultrasound modulates feedforward
5	and feedback cortico-thalamo-cortical pathways by selectively activating excitatory neurons.
6	*J Neurosci* 45(23):e2218242025, doi:10.1523/jneurosci.2218-24.2025.
7	
8	**Dataset.** DANDI:000637, version 0.250829.1249 (doi:10.48324/dandi.000637/0.250829.1249), streamed.
9	The paper cites no version of 000637 (its data statement names a different dandiset, 000946), so the
10	most recent published version is pinned. The five published versions (0.250711.1756 to 0.250829.1249)
11	are compared below: they hold the same files with the same digests, so the choice does not change the
12	data.
13	
14	**Claims file.** `claims/000637/10.1523-jneurosci.2218-24.2025.yaml`, written from the version of record
15	(PMC12139594), which has no supplement and links no code.
16	
17	**What the dataset holds.** 292 recordings from 25 rats, each with spike times of sorted units from one
18	32-channel probe in S1 and the trial start and stop times. The condition is coded only in the file's
19	identifier. There are no spike waveforms, no POm, auditory cortex or CG1-targeted recordings, and of the
20	duty-cycle series only the conditions that share pulse durations with the PRF series.
[... 509 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('10.1523-jneurosci.2218-24.2025.yaml'));print(len(d['claims']));print([c['id'] for c in d['claims']][27:])"
```

```
31
['fig10ef-sttc-dc', 'fig11b-ac-responses', 'fig11c-ac-s1-dsttc-30', 'fig11d-ac-s1-dsttc-3000']
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000637/versions/0.250829.1249/" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(json.dumps(d.get('assetsSummary'),indent=1));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
import requests
u="https://api.dandiarchive.org/api/dandisets/000637/versions/0.250829.1249/assets/?page_size=1000"
r=requests.get(u,timeout=120).json()
ps=[a['path'] for a in r['results']]
print(len(ps), r['next']); print(ps[:5]); 
import collections
print(collections.Counter(p.split('_')[-1] if '_' in p else p for p in ps).most_common(10))
print([p for p in ps if 'BASE' in p.upper() or 'sham' in p.lower() or 'pom' in p.lower() or 'ac' in p.lower().split('/')[-1][:3]])
a=r['results'][0]
m=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/",timeout=60).json()
print({k:m[k] for k in m if k in ('variableMeasured','wasDerivedFrom','measurementTechnique')})
print(m.get('wasGeneratedBy'))
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000637/versions/0.250829.1249/assets/?page_size=1000" > a.json; python3 - <<'E'
import json,collections,subprocess
r=json.load(open('a.json'))
ps=[a['path'] for a in r['results']]
print(len(ps), r['next']); print(ps[:4])
print([p for p in ps if any(k in p.lower() for k in ('base','sham','pom','cg1','audit','ac_'))])
aid=r['results'][0]['asset_id']
m=json.loads(subprocess.check_output(['curl','-s',f"https://api.dandiarchive.org/api/assets/{aid}/"]))
print(m.get('variableMeasured')); print(m.get('wasAttributedTo')); print([k for k in m])
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000637/versions/0.250829.1249/assets/?page_size=1000&metadata=1" > am.json; python3 - <<'E'
import json,collections
r=json.load(open('am.json'))
c=collections.Counter(); sz=[]
for a in r['results']:
    md=a['metadata']; c[tuple(sorted(v['value'] for v in md.get('variableMeasured',[])))]+=1; sz.append(md['contentSize'])
print(c); print(min(sz),max(sz),sum(sz))
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  grep -n -i -E "dandi|000946|000637|waveform|sham|2,000|baseline recording" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E' 2>&1 | tail -20
import numpy as np, sys
try:
    import tfus
except Exception as e:
    print("import fail", e); sys.exit()
sp=np.array([ -0.01, 0.0, 0.0669, 0.067, 0.2, 0.268])
print(tfus.window_counts(sp, np.array([0.0])))
print(tfus.parse_identifier("BH401_1500_400_67_55_2"), tfus.parse_identifier("BH458_BASELINE"))
rng=np.random.default_rng(0)
on=np.arange(500)*2.5+1
s=dict(identifier='x',subject='x',prf=1,pd_us=1,volt=5,baseline=False,trial_start=on,units=[np.sort(rng.uniform(0,1300,int(1300*3)))])
t=tfus.unit_table([s]); print(t[[c for c in t if c.startswith('n1') or c.startswith('n2')]].round(1).to_string())
E
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* ; which -a python3 pip pip3 uv conda 2>/dev/null; pip install --user numpy pandas 2>&1 | tail -1
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/pip
/usr/bin/pip
/bin/pip
/opt/hostedtoolcache/Python/3.13.17/x64/bin/pip3
/usr/bin/pip3
/bin/pip3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
```

**Agent calls Bash**

```bash
cd  python3 -c "import numpy" 2>&1; pip install --user -q numpy pandas 2>&1 | tail -2; python3 -c "import numpy, pandas; print('ok')"
```

```
ok
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/stub/dandi; touch $TMPDIR/stub/h5py.py $TMPDIR/stub/remfile.py $TMPDIR/stub/dandi/__init__.py; echo "DandiAPIClient=None" > $TMPDIR/stub/dandi/dandiapi.py; PYTHONPATH=$TMPDIR/stub:. python3 - <<'E' 2>&1 | tail -20
import numpy as np, tfus
sp=np.array([ -0.01, 0.0, 0.0669, 0.067, 0.2, 0.268])
print(tfus.window_counts(sp, np.array([0.0])))
print(tfus.parse_identifier("BH401_1500_400_67_55_2"))
rng=np.random.default_rng(0)
on=np.arange(500)*2.5+1
for rate in (3,30):
  s=dict(identifier='x',subject='x',prf=1,pd_us=1,volt=5,baseline=False,trial_start=on,units=[np.sort(rng.uniform(0,1300,int(1300*rate)))])
  t=tfus.unit_table([s]); print(rate,'Hz',t[[c for c in t if c.startswith('n1') or c.startswith('n2')]].round(1).to_string())
E
```

```
[[1 2 1 1 0]]
{'subject': 'BH401', 'prf': 1500, 'pd_us': 400, 'ud_ms': 67, 'volt': 5.5, 'repeat': 2, 'baseline': False}
3 Hz    n1_0-67  n2_0-67  n1_67-134  n2_67-134  n1_134-201  n2_134-201  n1_201-268  n2_201-268
0     69.2     15.9       82.1       23.3        88.9        18.4        79.5        18.4
30 Hz    n1_0-67  n2_0-67  n1_67-134  n2_67-134  n1_134-201  n2_134-201  n1_201-268  n2_201-268
0     97.2    108.0       97.9      114.8       100.4       111.4        95.7       110.0
```

**Agent**

**A. Outcomes**

The claims file has 31 claims. I mark all 31 as blocked. The notebook's own count of 30 (cell 0) is wrong; see B1.

| Claim id | Outcome | Reason |
|---|---|---|
| unit-counts | blocked (data_missing) | Every count is split into RSUs and FSUs, which needs waveforms. Every Units table has only `spike_times` (cell 7), and the archive lists only `Units` and `ElectrodeGroup` as measured for all 292 assets. There are no POm units. "Reproduced" can be ruled out anyway: cell 16 finds 4,642 / 1,088 / 862 S1 units, against the paper's RSU+FSU sums of 1,297 / 366 / 209. A two-cluster split puts every unit in one class, so at most one count of each S1 pair can match. |
| fig4-s1-rsu-timelocked-3000 | blocked (data_missing) | There are no waveforms, so there are no S1 RSUs to select. |
| fig4-pom-rsu-timelocked-3000 | blocked (data_missing) | There are no POm units: one probe per file, location "unknown", and the description says S1 only. |
| fig4-post-3000 | blocked (data_missing) | Needs POm RSUs and S1 cell types. |
| fig4-30hz-s1-rsu-inhibition | blocked (data_missing) | No cell types. The recordings exist: 26 at 30 Hz / 200 µs (cell 14). |
| fig4-30hz-pom-rsu-delayed | blocked (data_missing) | No POm units. |
| fig4-fsu-no-change | blocked (data_missing) | No FSUs and no POm units. |
| fig5-sham-no-response | blocked (data_missing) | No cell types and no POm units. Three files are named BASELINE, but nothing in them says they are sham sessions. |
| fig5-cg1-control-no-response | blocked (data_missing) | No identifier or metadata names a CG1 target. All 292 files have the same `session_description`, "Neural Spikes for S1 tFUS". |
| fig6a-s1-rsu-timelocked-high-prf | blocked (data_missing) | The conditions are present (PRF series at 200 µs), but there are no cell types. |
| fig6a-s1-rsu-delayed | blocked (data_missing) | Same as fig6a-s1-rsu-timelocked-high-prf. |
| fig6b-s1-fsu | blocked (data_missing) | No FSUs. |
| fig6c-pom-rsu-timelocked | blocked (data_missing) | No POm units. |
| fig6c-pom-rsu-delayed | blocked (data_missing) | No POm units. |
| fig6d-pom-fsu | blocked (data_missing) | No POm units. |
| fig7a-s1-rsu-dc-3000 | blocked (data_missing) | At 3000 Hz only 30% and 60% DC exist (100 and 200 µs). The 0.6, 6 and 90% DCs are missing, and there are no cell types. |
| fig7b-s1-fsu-dc-3000 | blocked (data_missing) | Same as fig7a. |
| fig7c-pom-rsu-dc-3000 | blocked (data_missing) | No POm units, and DCs are missing. |
| fig7d-pom-fsu-dc-3000 | blocked (data_missing) | No POm units, and DCs are missing. |
| fig8a-s1-rsu-dc-30 | blocked (data_missing) | At 30 Hz only 0.6% DC exists (cell 14), and there are no cell types. |
| fig8b-s1-fsu-dc-30 | blocked (data_missing) | Same as fig8a. |
| fig9a-s1-rsu-60dc | blocked (data_missing) | Only 1500 Hz and 3000 Hz at 60% DC exist, and there are no cell types. |
| fig9b-s1-fsu-60dc | blocked (data_missing) | Same as fig9a. |
| fig10a-dsttc-3000 | blocked (data_missing) | Needs S1–POm pairs. |
| fig10b-dsttc-30 | blocked (data_missing) | Needs S1–POm pairs. |
| fig10c-sttc-constant-pd | blocked (data_missing) | Needs S1–POm RSU pairs. |
| fig10d-sttc-60dc | blocked (data_missing) | Needs S1–POm RSU pairs; DCs are also missing. |
| fig10ef-sttc-dc | blocked (data_missing) | Needs S1–POm RSU pairs; DCs are also missing. |
| fig11b-ac-responses | blocked (data_missing) | No auditory-cortex units. This claim does not need cell types, but no file holds AC data. |
| fig11c-ac-s1-dsttc-30 | blocked (data_missing) | No AC units. |
| fig11d-ac-s1-dsttc-3000 | blocked (data_missing) | No AC units. |

**Archive check for the blocked claims.** I queried the API for version 0.250829.1249. It has 292 assets from 25 subjects, and every asset lists `variableMeasured` = [Units, ElectrodeGroup]. No asset path or metadata mentions POm, AC, CG1 or sham, and the files are 0.9 to 7 MB each. No part of any claim can be tested as the criteria state it. The only partial content is that the S1 recordings for the PRF-at-200 µs series, and for some DC conditions, are present.

**B. Problems**

1. [does not affect a conclusion] Cell 0 says "All 30 claims are blocked". The claims file has 31. The summary table does cover all 31 ids.
2. [does not affect a conclusion] Cells 0 and 16 never ask whether 000637 holds this paper's recordings at all.
   - The paper's data statement names DANDI:000946.
   - The dataset has 25 rats; the paper's two groups total 16 + 12 = 28.
   - The S1 unit totals are 3.6 times the paper's RSU+FSU sums.
   - The dataset may include the S1 probes of the auditory-confound group, or be different recordings.
   - The ratio is printed but not interpreted. Since all claims are blocked anyway, this changes no outcome.
3. [does not affect a conclusion] Cell 16 misses that the S1 totals already rule out "reproduced" for unit-counts, whatever the classification (argument in A). The outcome stays blocked because the six POm counts cannot be checked.
4. [does not affect a conclusion; this is a problem in the claims file, which I report and do not correct] Reading N2 of Method S (mean over trials of the per-trial ratio) is strongly biased downward for low-rate units.
   - On synthetic Poisson units with no response (`tfus.unit_table`), N2 came out at 16–23% at 3 Hz and about 110% at 30 Hz.
   - The notebook shows the same bias: mean N2 is about 60–80% in every window, including the BASELINE recordings (cells 18 and 21).
   - Under reading R2 (tests against 100%), N2 would produce spurious "decreases" and suppress increases. If the data had allowed testing, this would have pushed claims toward blocked or not_reproduced for an artefactual reason.
5. [does not affect a conclusion] In the cell 10 clock check, the "null" condition is not null: with onsets shifted by 1.2 s, all windows are significantly *below* the shifted pre-window (p down to 2e-76). Activity from the stimulus seems to persist, or trial structure seems to show, more than 1.1 s after onset. The contrast with the true onsets still supports trial start as the tFUS onset.
6. [does not affect a conclusion] Cell 21 is not discussed in the text: the BASELINE recordings show a pooled S1 increase at 134–201 ms (W2, p = 6e-9) and at 201–268 ms (W2, p = 1e-5), though not under W1. If these files were sham sessions, this would weigh against fig5-sham-no-response. The identity of the files and the missing cell types keep that claim blocked.
7. [does not affect a conclusion] `parse_identifier` assumes a two-digit voltage field means tenths of a volt ("55" read as 5.5 V). A "10" would become 1.0 V. This is not checked, but only 5, 55, 7 and 35 occur.
8. [does not affect a conclusion] Helpers tested on synthetic inputs:
   - `window_counts` uses half-open windows [a, b), which is correct.
   - The `>2000` spike rule is applied as "more than 2,000", which is correct.
   - `duty_cycle` is correct.

**C. What I could not check**

- **No waveforms anywhere in the files.** The notebook lists only the Units `colnames`, `acquisition` and `processing`. Two outputs would have settled this:
  - a full HDF5 tree per file (`f.visit`), covering `/analysis`, `/scratch`, `/stimulus`, extra Units datasets not listed in `colnames` (such as `waveform_mean`), and the electrodes-table columns;
  - the electrode-group descriptions.
- **No CG1 or sham sessions.** The notebook shows only identifiers and `session_description`. Printing `general/experiment_description`, `general/notes`, `general/stimulus` and the electrode-group `location` / `description` for every file would have settled this.
- **Whether the BASELINE files are sham, and whether 000637 is the subset of the paper's data the paper used.** This would need the same metadata fields, plus a per-subject comparison of unit counts against the paper's sham n of 31 + 53 S1 units.

## End of run

18 turns, 2 minutes, result: success.
