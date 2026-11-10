# burman-2023 · verifier-1 · run 42780709977

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 360
drwxr-xr-x 6 runner runner    4096 Nov 10 08:51 .
drwxr-xr-x 7 runner runner    4096 Nov 10 08:51 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 08:11 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 08:11 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 10 08:51 .claude
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.development
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.local
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.production
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.test
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.test.local
drwx------ 2 runner runner    4096 Nov 10 08:51 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 08:11 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 08:11 .github
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 08:11 .idea
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat burman-2023.yaml
```

```
<persisted-output>
Output too large (49.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/66ad31e9-b4e6-4309-b34c-5620a7a0c791/tool-results/bm6lb4x02.txt

Preview (first 2KB):
# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,
# "Active cortical networks promote shunting fast synaptic inhibition in vivo", on dandiset 000458.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),
# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of
# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.
# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF
# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is
# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7
# rest on the main-text sentences that cite them, and their tests are not known here.
#
# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision
# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads
# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "burman-2023.yaml"
}
```

```
1	# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,
2	# "Active cortical networks promote shunting fast synaptic inhibition in vivo", on dandiset 000458.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
5	#
6	# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),
7	# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of
8	# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.
9	# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF
10	# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is
11	# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7
12	# rest on the main-text sentences that cite them, and their tests are not known here.
13	#
14	# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision
15	# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads
16	# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,
17	# per unit, evoked firing rate, peri-stimulus histogram entropy and synchrony for the awake and
18	# isoflurane epochs. It does not hold the exclusion step, the statistics or the plots.
19	# (2) gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f, revision
20	# f6a05661c10051560aa381e334099efd8521617b, burman_et_al_2023_neuronal_network_simulation.py: the
[... 874 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
for fn in ['reproduce_burman_2023.ipynb']:
    nb=json.load(open(fn))
    for i,c in enumerate(nb['cells']):
        print(f"===== [{i}] {c['cell_type']}")
        print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain']))
                else: print('--OUT-- keys',list(d))
            elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
```

```
<persisted-output>
Output too large (48.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/66ad31e9-b4e6-4309-b34c-5620a7a0c791/tool-results/b0n95gz4y.txt

Preview (first 2KB):
===== [0] markdown
# Reproducing Burman et al. (2023) on DANDI:000458: Neuropixels claims

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Dataset.** [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version
0.230317.0039 (doi:10.48324/dandi.000458/0.230317.0039), the Allen Institute recordings of Claar et
al. (2023) that the paper reuses (Figure 4A to 4D, Figure S6). This is the only published version
of the dandiset, and the one the paper's analysis code names in its docstring
(gist a77bcf5e, revision 43a13d89), so it is pinned. The draft has the same 24 assets (checked below).

**Text the claims were written from.** The version of record (Europe PMC, PMC11913778), with STAR
Methods; the supplement (Figures S1 to S7) was not available (claims file, opening comment).

[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/66ad31e9-b4e6-4309-b34c-5620a7a0c791/tool-results/b0n95gz4y.txt"
}
```

```
1	===== [0] markdown
2	# Reproducing Burman et al. (2023) on DANDI:000458: Neuropixels claims
3	
4	**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
5	promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
6	[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)
7	
8	**Dataset.** [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version
9	0.230317.0039 (doi:10.48324/dandi.000458/0.230317.0039), the Allen Institute recordings of Claar et
10	al. (2023) that the paper reuses (Figure 4A to 4D, Figure S6). This is the only published version
11	of the dandiset, and the one the paper's analysis code names in its docstring
12	(gist a77bcf5e, revision 43a13d89), so it is pinned. The draft has the same 24 assets (checked below).
13	
14	**Text the claims were written from.** The version of record (Europe PMC, PMC11913778), with STAR
15	Methods; the supplement (Figures S1 to S7) was not available (claims file, opening comment).
16	
17	**What this notebook tests.** The claims on the dandiset. The network model claims are in
18	`network_model.ipynb`. The patch-clamp claims (Figures 1 to 3, S1 to S5) rest on recordings that
19	are not in the dandiset nor deposited anywhere ("available on request"), and are blocked.
20	
[... 733 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('reproduce_burman_2023.ipynb'));print(len(nb['cells']))"; cat npx.py
```

```
28
"""Loading DANDI:000458 (Claar et al. 2023) and the per-unit measures of Burman et al. (2023),
Figure 4A to 4D and Figure S6.

Every method choice is the claims file's (claims/burman-2023.yaml, opening comment N1 to N8),
which takes it from the paper's Methods ("Pre-processing of Neuropixels dataset",
"Characterization of stimulus-evoked spiking responses") and the paper's analysis gist,
gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf at revision
43a13d89441b7f56e835e84fa5811d9567917daf (burman_et_al_2023_neuropixel_data_analysis.py):

- SESSIONS: the 17 recordings the gist lists (N1).
- Units (N2): waveform_duration >= 0.4 ms (Methods; the gist's > 0.4 is a variant). Area reading
  A1, the Methods: location "SSp-ll" or "SSp-tr" when SSp was stimulated, "MOs" when MOs was;
  reading A2, the gist: location[:3] among the session's estim_target_region values of its
  electrical trials.
- Trials (N3): stimulus_type "electrical", is_valid true, behavioral_epoch "awake" or
  "isoflurane", all currents and depths pooled, times from stop_time (gist).
- Window (N4): spikes 2 to 12 ms after the stimulus, 1 ms bins.
- Entropy (N5), synchrony (N6) and the evoked rate (N7, readings F1 and F2) as the gist computes
  them; see each function.
[... 313 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
for fn in ['network_model.ipynb']:
    nb=json.load(open(fn))
    for i,c in enumerate(nb['cells']):
        print(f"===== [{i}] {c['cell_type']}")
        print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text'])[:6000])
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[:6000])
            elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
cat network.py
```

```
===== [0] markdown
# Reproducing Burman et al. (2023): the network model (Figures 4E to 4H, S7)

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Data.** These claims are `data: elsewhere`: their data are generated by the paper's simulation
code, gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision
f6a05661c10051560aa381e334099efd8521617b, transcribed in `network.py` (its docstring lists the
differences, none of which changes the model). They use nothing from DANDI:000458 (version
0.230317.0039, read in `reproduce_burman_2023.ipynb`; the version constant is `npx.VERSION`).

**Text the claims were written from.** The version of record (PMC11913778) with STAR Methods; the
supplement (Figure S7) was not available.

| Claim | Here |
|---|---|
| fig4f-model-hyperpolarizing-less-activity | tested |
| fig4h-model-synchrony | tested |
[... 497 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;c=yaml.safe_load(open('burman-2023.yaml'))['claims'];print(len(c));
nt=[x['id'] for x in c if x['criterion'].startswith('Not testable')];print(len(nt));print([x['id'] for x in c if x['id'] not in nt])"
curl -s "https://api.dandiarchive.org/api/dandisets/000458/versions/0.230317.0039/assets/?page_size=200" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d['count']);[print(a['path'],a['size']) for a in d['results']]"
for q in Burman Akerman gramicidin; do curl -s "https://api.dandiarchive.org/api/dandisets/?search=$q&page_size=50" | python3 -c "
import json,sys;d=json.load(sys.stdin);print('$q',d['count'],[(x['identifier'],x.get('most_recent_published_version',x.get('draft_version'))['name']) for x in d['results']])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000458/versions/0.230317.0039/" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, pandas as pd, npx
from scipy.stats import entropy
# 2 units, 3 trials
trials=pd.DataFrame(dict(stimulus_type=['electrical']*3,behavioral_epoch=['awake']*3,is_valid=[True]*3,
  estim_target_region=['MOs']*3,start_time=[1,5,9],stop_time=[1.0004,5.0004,9.0004]))
# spikes: (trial idx, ms after stop)
sp={0:np.array([[0,2.5],[0,3.5],[1,2.2],[2,11.9],[2,12.0],[2,1.9]]),1:np.array([[0,2.7],[1,5.5]])}
s=dict(trials=trials,spikes=sp,units=pd.DataFrame(dict(location=['MOs','MOs'],waveform_duration=[0.5,0.5])))
m=npx.measures(s,np.array([0,1]),npx.condition_trials(trials,'awake'))
print(m)
# expected unit0 spikes in [2,12): 2.5,3.5,2.2,11.9 -> count 4; F1=4/(3*0.01)=133.3; F2=sum(20.1)/(3*0.01)=670
h=np.zeros(10);h[[0,1,0,9]]+=0
print('ent0',entropy([2,1,0,0,0,0,0,0,0,1]))
# synchrony unit0: trial0 pop spikes bins 0,1,0 -> hist [2,1]/3; unit0 spikes at bin0 (2/3), bin1(1/3); trial1 pop bins 0,3 -> each 1/2; unit0 bin0 -> 1/2; trial2 pop bin9 only ->1
print('syn0',np.mean([2/3,1/3,1/2,1]))
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
ls /usr/bin/python3* ; which -a python python3; ls ~/.venv* /opt 2>/dev/null | head; pip --version 2>&1|head -1
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
for p in /opt/hostedtoolcache/Python/*/x64/bin/python3 /usr/bin/python3.14; do $p -c "import numpy,pandas,scipy;print('$p ok')" 2>&1|tail -1; done
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'. Did you mean: 'runpy'?
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && v/bin/pip -q install numpy pandas scipy requests h5py 2>&1 | tail -2; v/bin/python -c "import numpy, pandas, scipy; print('ok')"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/pip -q install remfile 2>&1|tail -1; $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, pandas as pd, npx
from scipy.stats import entropy
trials=pd.DataFrame(dict(stimulus_type=['electrical']*3,behavioral_epoch=['awake']*3,is_valid=[True]*3,
  estim_target_region=['MOs']*3,start_time=[1,5,9],stop_time=[1.0004,5.0004,9.0004]))
sp={0:np.array([[0,2.5],[0,3.5],[1,2.2],[2,11.9],[2,12.0],[2,1.9]]),1:np.array([[0,2.7],[1,5.5]])}
s=dict(trials=trials,spikes=sp,units=pd.DataFrame(dict(location=['MOs','MOs'],waveform_duration=[0.5,0.5])))
m=npx.measures(s,np.array([0,1]),npx.condition_trials(trials,'awake'))
print(m.to_string())
print('exp F1', 4/0.03, 'F2', (2.5+3.5+2.2+11.9)/0.03, 'ent0',entropy([2,1,0,0,0,0,0,0,0,1]))
print('syn0',np.mean([2/3,1/3,1/2,1]),'syn1',np.mean([1/3,1/2]))
print('ent1', entropy([1,0,0,1]))
EOF
```

```
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
   row  count     rate_F1     rate_F2   entropy  synchrony
0    0      4  133.333333  670.000000  1.039721   0.625000
1    1      2   66.666667  273.333333  0.693147   0.583333
exp F1 133.33333333333334 F2 670.0000000000001 ent0 1.0397207708399179
syn0 0.625 syn1 0.41666666666666663
ent1 0.6931471805599453
```

**Agent calls Grep**

```json
{
 "pattern": "synchron|entropy|0\\.1 Hz|waveform|regress",
 "path": "paper/10.1016-j.neuron.2023.08.005.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -E ".{300}(Pre-processing of Neuropixels|Characterization of stimulus-evoked|regressing out|0\.1 Hz).{700}" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -E ".{400}(2 ms|2–12|2-12|12 ms).{300}" paper/*.txt | head; grep -o -E "we sub-selected.{700}" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python -c "
import numpy as np
s=np.array([.8909,.8767,.8813,.8825,.8840,.8800,.8661,.8791,.8804,.8740,.8721,.8777,.8817,.8817,.8690,.8781,.8749,.8833,.8864,.8781])
e=np.array([.1798,.2042,.1986,.1955,.1932,.1998,.2217,.2014,.1982,.2091,.2147,.2012,.1945,.1962,.2200,.2033,.2072,.1952,.1883,.2050])
for x,ref in ((s,.881),(e,.197)): se=x.std(ddof=1)/np.sqrt(20); print(x.mean(), se, (x.mean()-ref)/se)"
```

```
0.8789 0.0012969397177891298 -1.6191963058852292
0.201355 0.0022514495330786346 1.9343094020166491
```

**Agent**

**Verifier report, round 1: Burman et al. 2023 on DANDI:000458**

The claims file has 35 claims. Ten are tested: six in `reproduce_burman_2023.ipynb` and four in `network_model.ipynb`. The other 25 are marked "Not testable": 24 patch-clamp claims, plus figs4-intrinsic-properties.

### A. Outcomes

| Claim id | My outcome | Reason |
|---|---|---|
| dataset-sessions-link | reproduced | Cell 13: all 17 gist sessions are assets of 0.230317.0039, each has every units and trials field, and each has both epochs. Cell 4: 16 subjects. |
| fig4c-sample | partially_reproduced | Cell 15, A1F1 (the Methods reading): 721 kept (inside 662 ± 66.2), but 144 excluded (outside 203 ± 20.3). Per-recording minimum is 7 against 1; 17 recordings, 16 mice; the total of 865 matches. Under the variant A1F2 every number matches the paper exactly (662/203, median 34, 1 to 93), so this is a deviation, not a failure of the data. |
| fig4d-synchrony-lower-awake | partially_reproduced | Cell 18, A1F1: awake 0.3188 is just outside 0.320–0.330; isoflurane 0.3862 is inside. Awake is lower, p = 1.45e-32. A1F2 matches exactly (0.3253 / 0.3928). |
| fig4d-entropy-higher-awake | partially_reproduced | Cell 22, A1F1: awake 1.3887 and isoflurane 1.1502 are both outside tolerance. Awake is higher, p = 3.3e-30, n = 656. A1F2 matches exactly (1.3474 / 1.1106). |
| fig4-rate-higher-awake | reproduced | Cell 24, A1F1: 14.0 Hz awake against 7.59 Hz isoflurane, paired t = 12.4, p far below 0.05. Holds under every reading; 15 of 17 recordings go the same way. |
| figs6-rate-regressed | reproduced | Cell 26, A1F1: synchrony is negative and entropy positive under R1, R2 and R3, all p < 1e-10. Same under every variant. |
| fig4f-model-hyperpolarizing-less-activity | reproduced | Model cell 11: 8.785 Hz hyperpolarizing against 19.468 Hz shunting, paired p ≈ 0; lower in 20 of 20 runs. |
| fig4h-model-synchrony | partially_reproduced | Model cell 7: shunting 0.7833 is inside tolerance; hyperpolarizing 0.8789 is outside (0.880–0.882). Shunting is lower, p ≈ 0, in 20 of 20 runs. See B2. |
| fig4h-model-entropy | partially_reproduced | Model cell 9: shunting 0.4516 is inside tolerance; hyperpolarizing 0.2014 is outside (0.195–0.199). Shunting is higher, p ≈ 0, in 20 of 20 runs. See B2. |
| figs7-model-decoding | reproduced | Model cell 13: accuracy 0.985 shunting against 0.932 hyperpolarizing. D1: p = 1.1e-12. D2: higher in 20 of 20 runs. Chance is 0.01 (100 patterns). |
| 24 patch-clamp claims (fig1b-perforation-rs, fig1h-vu-egaba, fig1i-vu-rmp, fig1j-vu-df, figs2-ramp-equals-step, figs3-egaba-unrelated-amplitude-rs, rm-awake-lower, fig2c-vm-depolarized, fig2d-subthreshold-fluctuation, fig2f-response-polarity, fig2h-egaba-depolarized, fig2i-rmp-depolarized, fig2j-df-depolarized, fig2j-awake-df-zero, fig2k-conductance-same, figs5-within-anesthetized, rm-nbqx-higher, fig3c-nbqx-vm, fig3d-nbqx-fluctuation, fig3e-nbqx-polarity, fig3g-nbqx-egaba, fig3h-nbqx-rmp, fig3i-nbqx-df, fig3j-nbqx-conductance-same) | blocked: data_missing | I queried the archive. The version has 24 assets, all `*_behavior+ecephys.nwb`. The measured variables are Units, ElectricalSeries, LFP and behavior, with no intracellular recordings. A DANDI search for "Burman", "Akerman" and "gramicidin" returns 0 dandisets. No part can be tested. |
| figs4-intrinsic-properties | blocked: methods_underspecified | The measure and test are only in the Figure S4 legend, which was not supplied. The notebook gives the reason as "other"; methods_underspecified fits better. The NEURON model (commit a404c3e) is linked, so a qualitative partial test may have been possible (B3). |

### B. Problems

1. **[affects a conclusion]** Cells 15, 18 and 22: the A1F1 rule against an exact A1F2 match (a point about the claims file, not the code). The claims file (N7) judges every Neuropixels claim under F1. Under F2, the gist's `get_firing_rate`, every published number is reproduced exactly: 662/203, median 34, range 1 to 93, synchrony 0.3253/0.3928, entropy 1.3474/1.1106. That is strong evidence that the paper's numbers were made with the gist's summed-latency rate. The three partial outcomes therefore reflect a bug in the paper's own code, not the data. I am reporting this, not overriding the rule; the outcomes should be recorded as deviations.
2. **[affects a conclusion]** fig4h criteria: the tolerance is too tight for runs with different seeds (a point about the claims file). The tolerance is the paper's SEM over 16,000 pooled neurons (0.001 and 0.002). The run-to-run SE of a 20-run mean, which I computed from model cell 4's per-run means, is 0.0013 for synchrony and 0.0023 for entropy. The hyperpolarizing misses are 1.6 and 1.9 of these SEs. With seeds that differ from the paper's (the gist sets none), that is seed noise, so the partial outcomes come from the criterion, not the model.
3. **[does not affect a conclusion]** Notebook cell 0, figs4: the "other" reason does not mention that the NEURON model code is available. The notebook neither attempts nor argues against simulating ramp E_GABA estimates under anesthetized and awake membrane properties.
4. **[does not affect a conclusion]** Cells 19 and 24: p-values print as `0.00e+00` because they are rounded with `.round(4)` / `.round(3)` before formatting. The true values are tiny, so nothing changes.
5. **[does not affect a conclusion]** Cell 8: the clock check uses off-pulse windows on only 2 of 17 files. For the other 15 it relies on the evoked-count contrast.
6. **[does not affect a conclusion]** Readings collapse. Cells 6 and 7 show that A1 equals A2 (only SSp-ll and SSp-tr occur) and that ≥ 0.4 equals > 0.4 (no unit has exactly 0.4 ms). In effect only F1 against F2 matters. This is handled correctly.
7. **[does not affect a conclusion]** `network.simulate`: a neuron with one spike gets entropy 0, not NaN, as in the gist. This differs from N5 for the data, but no neuron is affected (0 dropped; every neuron spikes).
8. **[does not affect a conclusion]** `npx.measures` and `npx.histogram`: I tested them on a synthetic 2-unit, 3-trial session. F1, F2, entropy and synchrony (unit included in its own population; spikes at 12.0 and 1.9 ms excluded) all match hand calculation. `read_session` assigns each spike to the latest electrical stop, which is safe with inter-pulse intervals of 3.5–4.5 s.
9. **[does not affect a conclusion]** `npx.paired`: the t tests pool neurons across 17 recordings and ignore clustering, as the paper does. The per-recording breakdowns (15 of 17 recordings in the expected direction for synchrony, entropy and rate) support the direction.

### C. What I could not check

- **Data-analysis gist.** I could not see it, so I cannot confirm that npx's F2 denominator (trial position within the condition's valid trials, in table order) and its trial ordering match it. The exact A1F2 match makes this likely but does not prove it. A cell running the gist's own functions on one session and comparing per unit with npx would settle it.
- **Simulation gist.** `network.py` is checked only against its own whole-run-stimulus mode (model cell 3), not against the gist. One unmodified gist run at a fixed seed, compared spike for spike, would check the transcription.
- **Brian 2 learning rate.** Whether Brian 2 rereads `eta` from the mutated `syn_ns` dict is supported only indirectly: the summed weights do not change after balancing. That is good evidence, but it is not a direct printout of `eta` per run.
- **Supplement (Figures S4, S6, S7 legends).** Not available, so I could not see which regression and decoding test the paper used. Its text would show whether R1–R3 and D1/D2 include the paper's method.

## End of run

19 turns, 3 minutes, $1.33 at API prices, result: success.
