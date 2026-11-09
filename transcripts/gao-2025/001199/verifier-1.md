# 001199 · verifier-1 · run 41364136501

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 264
drwxr-xr-x 6 runner runner    4096 Nov  1 23:56 .
drwxr-xr-x 7 runner runner    4096 Nov  1 23:56 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 23:51 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 23:51 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  1 23:56 .claude
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env.development
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env.local
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env.production
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env.test
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .env.test.local
drwx------ 2 runner runner    4096 Nov  1 23:56 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 23:51 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 23:51 .github
-rw-r--r-- 1 runner runner       0 Nov  1 23:56 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 23:51 .idea
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025, on dandiset 001199.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
3	# docs/protocol.md, version pilot-10.
4	#
5	# Text read: the version of record as served by PubMed Central (paper/10.1523-jneurosci.2218-24.2025.txt,
6	# fetched by paper-text-fetcher), with Abstract, Significance Statement, Introduction, Materials and
7	# Methods, Results, all eleven figure legends and Discussion. The paper has no supplement and no PDF
8	# was supplied. The text lost the equation of the directional STTC (Methods, Directional spike time
9	# tiling coefficient); only its verbal definition survives (see D below). The Fig. 6 legend prints the
10	# postsonication window as "201–28 ms" (201–268 ms in the Results), and the Fig. 11 legend labels two
11	# panels "C" (the second is Fig. 11B in the Results).
12	#
13	# Code. The paper links no analysis code and names none; it says the analysis was done in MATLAB
14	# R2022a after spike sorting in Offline Sorter (Plexon). No repository was read.
15	#
16	# Which dataset. The paper's Methods name dandiset 000946 as the repository of all its data. Dandiset
17	# 001199 has the same title and cites this paper, but its description differs from the paper. It
18	# describes S1 recordings with 64-channel Cambridge or NeuroNexus electrodes, tFUS delivered "either at
19	# S1 or PoM", and varied pressure levels (input voltage in the session identifier), none of which the
20	# paper reports, and it does not mention the auditory cortex recordings. Dandiset 000946's description
[... 791 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 812,
 "limit": 300
}
```

```
812	    p: 0.008
813	    corrected: Bonferroni
814	  - about: during, 30 against 1,500 Hz
815	    test: post hoc one-tail two-sample Wilcoxon test
816	    p: 0.006
817	    corrected: Bonferroni
818	  - about: during, 30 against 3,000 Hz
819	    test: post hoc one-tail two-sample Wilcoxon test
820	    p: 0.007
821	    corrected: Bonferroni
822	  - about: during, 30 against 4,500 Hz
823	    test: post hoc one-tail two-sample Wilcoxon test
824	    p: 0.0003
825	    corrected: Bonferroni
826	  criterion: S1 RSUs (U) of the five 60% DC sessions (30 Hz/20,000 us, 300/2,000, 1,500/400, 3,000/200,
827	    4,500/133 us), R in 0 to 67 and 201 to 268 ms, Kruskal-Wallis at p < 0.01, pairwise one-tailed
828	    rank-sum tests between PRFs under B1 (the five PRFs compared with baseline) and B2 (the ten pairs),
829	    corrected p < 0.01. The direction of the
830	    30 Hz difference is not stated; both directions are read, the claim holding under the one the
831	    data's means give. Reproduced when both Kruskal-Wallis tests are significant, 30 Hz differs from
[... 275 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat tfus.py; grep -c "^- id:" 10.1523-jneurosci.2218-24.2025.yaml
```

```
"""Loading and spiking measures for the tFUS recordings of dandiset 001199.

Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025,
doi:10.1523/jneurosci.2218-24.2025.

Each NWB file holds sorted units (spike times only; no waveforms) and a trial table whose
`start_time` is taken as the sonication onset (the notebook checks this). The condition of a file
is written in its `identifier` and `general/notes`, in two formats:

- files of rats BH590, BH594, BH596 and BH615 (recorded 2024): identifier
  `<rat>[_tag]_<PRF>_<PD>_<UD>_<voltage>[_tags]` or `<rat>_BASELINE`, notes
  `Recording:S1; stim at:S1|POM`, and in BH596 and BH615 a `celltype_label` column that holds the
  area (S1 or POm) of each unit;
- files of rats BH608 and BH646 to BH658 (recorded 2025): identifier `<PRF>_<PD>_<UD>` or
  `no tFUS`, notes `recording:<area>;stimulation:<target>`, one file per probe.

Files are streamed from the archive at the pinned version; nothing is written to disk. Spike
times are sorted per unit on reading, as 64 units in 16 files hold a few out of order.

Where the parameters come from:
[... 209 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep "^- id:" 10.1523-jneurosci.2218-24.2025.yaml | nl; python3 -c "
import json;nb=json.load(open('reproduce_gao_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  print('=== CELL',i,c['cell_type'])
  print(''.join(c['source']))
  for o in c.get('outputs',[]):
    if 'text' in o: print('--OUT--');print(''.join(o['text']))
    elif 'data' in o:
      d=o['data']
      if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain']))
      if 'image/png' in d: print('[image]')
    elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1	- id: subjects
     2	- id: fig2-target-artifact
     3	- id: fig4-unit-counts
     4	- id: fig4-timelocked-rsu-3000
     5	- id: fig4-postsonication-3000
     6	- id: fig4-30hz-responses
     7	- id: fig4-no-fsu-change
     8	- id: fig5-unit-counts
     9	- id: fig5a-sham-no-response
    10	- id: fig5b-cg1-control-no-response
    11	- id: fig6-unit-counts
    12	- id: fig6a-s1-rsu-timelocked-high-prf
    13	- id: fig6a-s1-rsu-delayed
    14	- id: fig6b-s1-fsu-prf
    15	- id: fig6c-pom-rsu-prf
    16	- id: fig6d-pom-fsu-prf
    17	- id: fig7-9-unit-counts
    18	- id: fig7a-s1-rsu-dc-3000
    19	- id: fig7b-s1-fsu-dc-3000
    20	- id: fig7c-pom-rsu-dc-3000
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== CELL 0 markdown
2	# Reproducing Gao et al. (2025) from dandiset 001199
3	
4	Paper. Gao H, Ramachandran S, Yu K, He B (2025). Transcranial Focused Ultrasound Modulates
5	Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory
6	Neurons. *J Neurosci* 45(23):e2218242025.
7	[doi:10.1523/jneurosci.2218-24.2025](https://doi.org/10.1523/jneurosci.2218-24.2025). The claims
8	file was written from the version of record in PubMed Central (PMC12139594), with its Methods and
9	all figure legends; the paper has no supplement.
10	
11	Dandiset. [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250), version
12	0.250829.1250. The paper does not cite this dandiset: its Methods name dandiset 000946 as the
13	repository of all its data, with no version. 001199 has four published versions (0.250712.1551,
14	0.250713.1101, 0.250828.1941, 0.250829.1250). The cell below shows that all four and the draft
15	hold the same 229 files (same paths and blobs) and differ only in metadata the analysis does not
16	use (the order of contributors). The most recent published version is pinned, as the protocol
17	says when the paper cites none.
18	
19	What the dandiset holds. Sorted units (spike times only) and trial tables for 13 rats, recorded
20	in August and September 2024 (4 rats) and February to July 2025 (9 rats). There are no spike
[... 791 more lines not kept]
```

**Agent**

Notebook, helper and claims file read (35 claims; the notebook tests 2 and blocks 33). Next I'm testing the helper functions on synthetic inputs and checking the archive metadata.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, tfus
rng=np.random.default_rng(0)
on=np.arange(1,1001)*2.5
# unit: 10 Hz baseline, 20 Hz during 0-67 ms
sp=[]
for t in on:
    sp+=list(t-0.067+rng.random(rng.poisson(0.67))*0.067)
    sp+=list(t+rng.random(rng.poisson(1.34))*0.067)
sp=np.sort(sp)
c=tfus.unit_counts([sp],on,tfus.WINDOWS)
df=tfus.normalized_rates(c,tfus.WINDOWS)
print(df[['pre_rate','rate_0-67','R1_0-67','R2_0-67','R1_67-134']].round(1).to_string())
# edge: spike exactly at onset counted in 0-67 not pre
c=tfus.unit_counts([np.array([10.0])],[10.0],{'w':(0,0.067)}); print(c['pre'],c['w'])
for s in ['BH596_3000_200_67_10','BH594_nocoating_3000_200_67_5','BH615_300_200_67_10_S1','3000_200_67','no tFUS','BH594_coating_BASELINE','BH590_30_2000_67_5','BH590_3000_20_67_5']:
    print(s, tfus.parse_condition(s,'recording:AC;stimulation:S1-6'))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, tfus
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls .claude; which -a python3 python; ls ~/.venv* /opt 2>/dev/null | head; pip --version 2>&1 | head -1
```

```
agents
commands
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
pipx
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
for p in /usr/bin/python3; do $p -c "import numpy, scipy, pandas; print('ok')"; done; pip install --target $TMPDIR/py numpy scipy pandas requests -q 2>&1 | tail -2
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, pandas; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  export PYTHONPATH=$TMPDIR/py; python3 -c "
import sys,types; sys.modules['h5py']=types.ModuleType('h5py'); sys.modules['remfile']=types.ModuleType('remfile')
import numpy as np, tfus
rng=np.random.default_rng(0)
on=np.arange(1,1001)*2.5
sp=[]
for t in on:
    sp+=list(t-0.067+rng.random(rng.poisson(0.67))*0.067)
    sp+=list(t+rng.random(rng.poisson(1.34))*0.067)
    sp+=list(t+0.067+rng.random(rng.poisson(0.67*3))*0.201)
sp=np.sort(sp)
c=tfus.unit_counts([sp],on,tfus.WINDOWS)
df=tfus.normalized_rates(c,tfus.WINDOWS)
print(df[['pre_rate','rate_0-67','R1_0-67','R2_0-67','R1_67-134','R2_67-134']].round(1).to_string())
c=tfus.unit_counts([np.array([10.0])],[10.0],{'w':(0,0.067)}); print(c['pre'],c['w'])
for s in ['BH596_3000_200_67_10','BH594_nocoating_3000_200_67_5','BH615_300_200_67_10_S1','3000_200_67','no tFUS','BH590_30_2000_67_5','BH590_3000_20_67_5']:
    print(s, tfus.parse_condition(s,'recording:AC;stimulation:S1-6'))
"
```

```
pre_rate  rate_0-67  R1_0-67  R2_0-67  R1_67-134  R2_67-134
0      10.6       19.3    182.9    104.7       97.3       57.7
[[0.]] [[1.]]
BH596_3000_200_67_10 {'prf': 3000, 'pd': 200, 'volt': 10, 'sham': False, 'rec': 'AC', 'target': 'S1-6', 'tags': ''}
BH594_nocoating_3000_200_67_5 {'prf': 3000, 'pd': 200, 'volt': 5, 'sham': False, 'rec': 'AC', 'target': 'S1-6', 'tags': 'nocoating'}
BH615_300_200_67_10_S1 {'prf': 300, 'pd': 200, 'volt': 10, 'sham': False, 'rec': 'AC', 'target': 'S1-6', 'tags': 'S1'}
3000_200_67 {'prf': 3000, 'pd': 200, 'volt': None, 'sham': False, 'rec': 'AC', 'target': 'S1-6', 'tags': ''}
no tFUS {'prf': None, 'pd': None, 'volt': None, 'sham': True, 'rec': 'AC', 'target': 'none', 'tags': ''}
BH590_30_2000_67_5 {'prf': None, 'pd': None, 'volt': None, 'sham': False, 'rec': 'AC', 'target': 'S1-6', 'tags': ''}
BH590_3000_20_67_5 {'prf': None, 'pd': None, 'volt': None, 'sham': False, 'rec': 'AC', 'target': 'S1-6', 'tags': ''}
```

**Agent calls Bash**

```bash
cd $TMPDIR; export PYTHONPATH=$TMPDIR/py; python3 -c "
import requests, json, collections
API='https://api.dandiarchive.org/api'
u=f'{API}/dandisets/001199/versions/0.250829.1250/assets/?page_size=1000'
r=requests.get(u,timeout=60).json(); a=r['results']; print(len(a), r['next'])
import statistics
print('sizes MB min/median/max', min(x['size'] for x in a)/1e6, statistics.median(x['size'] for x in a)/1e6, max(x['size'] for x in a)/1e6)
vm=collections.Counter(); keys=set()
for x in a[:229]:
    m=requests.get(f'{API}/dandisets/001199/versions/0.250829.1250/assets/{x[\"asset_id\"]}/',timeout=60).json()
    vm[tuple(sorted(v.get('value','') for v in m.get('variableMeasured',[])))]+=1
    keys|=set(m)
print(vm); print(sorted(keys))
print(json.dumps({k:m[k] for k in m if k in ('wasGeneratedBy','measurementTechnique','approach')},indent=0)[:1500])
"
```

```
229 None
sizes MB min/median/max 0.19496 0.850576 7.82628
Counter({('ElectrodeGroup', 'Units'): 229})
['@context', 'access', 'approach', 'blobDateModified', 'contentSize', 'contentUrl', 'dateModified', 'datePublished', 'digest', 'encodingFormat', 'id', 'identifier', 'measurementTechnique', 'path', 'publishedBy', 'schemaKey', 'schemaVersion', 'variableMeasured', 'wasAttributedTo', 'wasGeneratedBy']
{
"approach": [
{
"name": "electrophysiological approach",
"schemaKey": "ApproachType"
}
],
"wasGeneratedBy": [
{
"name": "Acquisition session",
"schemaKey": "Session",
"startDate": "2025-07-11T20:22:00-04:00",
"description": "Neural Spikes for neural pathways to tFUS"
},
{
"id": "urn:uuid:1f645574-841d-48f8-aea6-4836cdb13cea",
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "received|accepted|000946|dandi|another group|auditory confound|2,000 spikes" *.txt | head -20
```

```
204:To explore the neuronal responses in the CTC pathway to tFUS, multiunit activities were recorded from the S1 and POm (N = 16). Based on the rat brain atlas (Paxinos and Watson, 2006), the burr holes were made at S1 (AP: −2, ML: 2.5) and POm (AP: −4.5, ML: 2.6) in the skull for each rat. The dura covering the tissue in the hole was carefully removed. Two 32-channel NeuroNexus microelectrodes (A1 × 32-Poly3–10 mm-50–177, NeuroNexus) were used in each session due to the limited physical space for electrodes and transducer. To leave space for the transducer, the insertion of electrode into S1 was set at 40° from the left side of the head with 1–1.3 mm depth based on the observation of signal qualities which covered cortical layer III to layer V, and the electrode inserted to POm was conducted at 20° with the depth of 5.8 mm which was inserted from posterior of the head. To check the auditory confound, another group of rats was used (N = 12). According to the rat atlas (Paxinos and Watson, 2006), the electrodes were inserted into S1 using the same way mentioned before and AC (AP: −4.5, ML: 6.5) with 40° angle and 1–1.3 mm depth. After the insertion of electrodes, the transducer was set vertically over the skull and placed as close as possible to the target area.
224:All data were recorded using a commercial multichannel neural signal acquisition system (Tucker-Davis Technologies). For spike analysis, recorded MUAs were bandpass filtered between 300 Hz and 5 kHz. Spike sorting was performed using Offline Sorter (Plexon). Spike waveforms were detected beyond the threshold of −3.5 standard deviations from the Mean of Peak Heights Histogram, and clustering was performed using k-means. The spike waveforms and timestamps were stored for further analysis in MATLAB (R2022a, MathWorks). All experimental data has been made public in a repository at the DANDI Archive (https://dandiarchive.org/dandiset/000946).
229:Only neurons that fire >2,000 spikes for each session were consi
[... 6 more lines not kept]
```

**Agent**

**A. Outcomes** (the claims file has 35 claims; the notebook tests 2 and blocks 33)

| Claim | My outcome | Reason |
|---|---|---|
| subjects | not_reproduced | Cell 16 finds 6 rats with simultaneous S1 and POm recordings (paper: 16) and 6 with S1 and AC (paper: 12). The "partially reproduced" rule needs the dataset's rats to be a subset of the paper's with none extra. The evidence goes against that: every S1 recording here uses a 64-channel A1x64-Edge probe, where the paper used two 32-channel Poly3 probes (cell 4). Two rats (BH648, BH658) sit in both groups, where the paper says "another group of rats". Only BH594, which has no POm recording, also appears in the paper's named dandiset 000946. |
| fig2-target-artifact | blocked (data_missing) | There is no raw voltage, no waveforms and no target-determination trials. I confirmed this in the archive API: every one of the 229 assets measures only `ElectrodeGroup` and `Units`, and no file is over 7.8 MB. |
| fig4-unit-counts | not_reproduced | Upper bounds from cell 13 settle this without RSU/FSU types. The claims file excludes non-paper pressures, so only the 5 V files count (plus 2025 files, whose voltage is unknown). Those hold 76 POm units at 3,000 Hz (233 RSUs alone need at least 209.7), 53 POm units at 30 Hz (need at least 170.1), 201 S1 units at 3,000 Hz (need at least 280.8) and 186 S1 units at 30 Hz (RSUs plus FSUs need at least 188.1). So at least 4 of the 8 counts fail. Even counting all voltages, both POm RSU counts fail. |
| fig5-unit-counts | not_reproduced | Sham sessions hold 37 POm units in total, but 67 RSUs and 67 FSUs each need at least 60.3. CG1 sessions exist only at 300 and 4,500 Hz and hold 11 S1 and 8 POm units, below the lower bounds for control S1 FSUs (30.6), POm RSUs (49.5) and POm FSUs (37.8). So 5 or more of the 8 counts fail. |
| fig6-unit-counts | blocked (metadata_insufficient) | Units can't be typed. Full reproduction is ruled out anyway: 396 POm units over all voltages, where 913 RSUs need at least 821.7. With 5 V only, S1 has 756 units against at least 945 needed. "Partially reproduced" (2 of 4) stays possible. |
| fig7-9-unit-counts | blocked (data_missing) | No PD other than 200 µs exists (cell 6; the 26 files with no PD are exactly the 26 sham files). The bounds would also rule out a partial outcome (S1 at 3,000 Hz has 465 units, below the 580 needed). |
| fig4-timelocked-rsu-3000, fig4-postsonication-3000, fig4-30hz-responses, fig4-no-fsu-change, fig5a-sham-no-response, fig6a-s1-rsu-timelocked-high-prf, fig6a-s1-rsu-delayed, fig6b-s1-fsu-prf, fig6c-pom-rsu-prf, fig6d-pom-fsu-prf, fig10a-dsttc-3000-during, fig10a-dsttc-3000-post, fig10b-dsttc-30, fig10c-sttc-constant-pd, fig11c-ac-to-s1-30hz, fig11d-ac-to-s1-3000 | blocked (metadata_insufficient) | Each needs RSU/FSU types. `celltype_label` is described as "1 = RSU, 2 = FSU" but holds only 0, "S1" or "POm", and there are no waveforms (cells 4–5; the API agrees). No untyped part of these criteria can be tested. |
| fig5b-cg1-control-no-response | blocked (data_missing) | There are no CG1 sessions at 3,000 Hz (cell 6), and units also can't be typed. |
| fig7a, fig7b, fig7c, fig7d, fig8a, fig8b, fig9a, fig9b, fig10d-sttc-60dc, fig10e-sttc-30hz-dc, fig10f-sttc-3000-dc | blocked (data_missing) | The duty-cycle series (PDs other than 200 µs) are absent, and units also can't be typed. |
| fig11b-ac-responses | not_reproduced | There are 194 AC units against 453 ± 45.3. The Kruskal–Wallis p is 0.05 or 0.013 during sonication and 0.74 or 0.013 after it, none below 0.01. During sonication only 1,500 Hz is significant, and only under R1/T2; 3,000 Hz never is. Nothing is significant postsonication, and 300 Hz is never the lowest mean (cell 18; the variants in cell 19 change nothing). Confidence is low: see problem 4. |

The paper states no chance levels, so there were none to compare.

**B. Problems**

1. [affects a conclusion] Cell 0 table and cell 13. fig4-unit-counts and fig5-unit-counts are marked blocked, but cell 13's untyped totals are upper bounds on the RSU and FSU counts and already settle both claims as not_reproduced. They also rule out full reproduction for fig6-unit-counts. The notebook never uses this.
2. [affects a conclusion] Cell 13. The main count table pools the 5, 10 and 15 V sessions; the claims-file header excludes pressures other than the paper's. The 5 V restriction appears only as a variant. Separately, the 2025 files, which carry every AC unit used in fig11b and most of the subjects sessions, give no voltage. Treating them as the paper's 5 V is an assumption the notebook never states in those sections.
3. [affects a conclusion] Cell 16, subjects. The criterion's "none extra" condition is not checked. Two pieces of evidence against it go unused in this section: the 64-channel S1 probe in every session (cell 4), and the overlap of the two groups (BH648, BH658) despite the paper's "another group".
4. [affects a conclusion] Cells 10 and 12, and fig11b. Whether the 2025 trial starts are the sonication onsets is not established. Only 7 of 108 stimulated files show more modulation with the true starts than with shifted ones. Even S1 in those sessions shows none (0.035 vs 0.039), while 2024 S1 shows 0.39 vs 0.13. The fig11b null may come from the timing rather than the neurons. The notebook did not try other lags or check trial times against each file's spike-time range.
5. [does not affect a conclusion] Claims file, headers R and T (reported here, not corrected). Under R2, the per-trial ratio is biased downward at low counts. In my synthetic test with `normalized_rates`, a true doubling gave R2 = 105% (R1 = 183%), and an unchanged rate gave 58%. So R2 with T2 against 100% always returns p = 1, as cell 18 shows. R1 fails as well, so the fig11b outcome stands.
6. [does not affect a conclusion] `parse_condition` only recognises PD 200 and voltages of 5, 10 or 15 V, so a file with another PD would parse silently as NaN. I checked this: the 26 files with no PD are the 26 sham files.
7. [does not affect a conclusion] `sessions_table` (cell 16) assigns a session its areas from all units, not only units with more than 2,000 spikes as header U requires. That can only inflate the counts, which are already far short.
8. [does not affect a conclusion] fig11b includes BH654, which has no shared S1–AC session, and the unexplained "S1-6" target. Both have variants, with the same outcome. The Bonferroni factor of 10 is the author's own choice, but it is shown alongside the factors 5 and 15.
9. My checks of `unit_counts` passed on synthetic input: windows are half-open, so a spike exactly at onset falls in 0–67 ms and not in the prestimulus window.

**C. What I could not check, and the output that would settle it**

- Whether the 2025 trial times are onsets. Needed: per file, the trial-start range against the spike-time range, plus a population PSTH or a lagged cross-correlation for every 2025 session, not only BH648 at 4,500 Hz. An untyped S1 response test at 0–67 and 201–268 ms would serve as a positive control.
- Per-file `celltype_label` value counts, rather than only the sets of values, to confirm that no 1 or 2 appears anywhere.
- Voltage or pressure for the 2025 files: none is given in the metadata the notebook prints.
- Subject counts using only units with more than 2,000 spikes, and with the 2025 sessions left out.

## End of run

13 turns, 4 minutes, result: success.
