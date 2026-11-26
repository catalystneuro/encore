# pasquereau-2013 · verifier-1 · run 45863880761

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 164
drwxr-xr-x 6 runner runner   4096 Nov 26 17:22 .
drwxr-xr-x 8 runner runner   4096 Nov 26 17:22 ..
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 26 17:00 .bash_profile
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 26 17:00 .bashrc
drwxr-xr-x 5 runner runner   4096 Nov 26 17:22 .claude
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env.development
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env.development.local
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env.local
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env.production
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env.production.local
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env.test
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .env.test.local
drwx------ 2 runner runner   4096 Nov 26 17:22 .git
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 26 17:00 .gitconfig
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 26 17:00 .github
-rw-r--r-- 1 runner runner      0 Nov 26 17:22 .gitmodules
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 26 17:00 .idea
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "pasquereau-2013.yaml"
}
```

```
1	# Claims for Pasquereau & Turner (2013) on dandiset 001636.
2	# Source: the full text in PubMed Central (PMC3840326, open access, CC BY), read from its Methods,
3	# Results, Table 1 and figure legends, and its supplementary data sheet (DataSheet1.PDF), whose
4	# table gives the neuronal results for each monkey separately.
5	# Quotes and statistics added 2026-10-19 from the full text (Europe PMC PMC3840326).
6	#
7	# When these criteria were written, the author had seen the data check only: the file list and
8	# metadata, the contents of the files, the counts of units by subject, MPTP state and projection
9	# type, the number of torque perturbations per direction (none in any monkey L file), the timing
10	# of the torque command against the trials table, the sign of the joint angle, which EMG channels
11	# hold data, and the cross-referenced and repeated files. These counts showed that the monkey V
12	# units with at least 5 perturbations per direction number 112 before and 159 after MPTP, with
13	# 49 and 54 PTNs and 31 and 48 CSNs, as in the supplementary table. No SDF, response detection,
14	# kinematic measure or EMG response had been computed.
15	#
16	# The dandiset marks no torque perturbation in any monkey L file, so every claim is tested on
17	# monkey V (elbow), and the expected values are the paper's monkey V values where it gives them
18	# (supplementary table). Where the paper gives only values pooled over both monkeys, these are
19	# the expected values and the difference is a deviation.
20	#
[... 760 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "pasq.py"
}
```

```
1	"""Loading and measures for the torque perturbation data of dandiset 001636 (monkey V).
2	
3	Pasquereau & Turner (2013), Front. Syst. Neurosci. 7:98, doi:10.3389/fnsys.2013.00098.
4	
5	Each NWB file holds one recording (one or two units) with a trials table whose
6	`torque_perturbation_type` and `torque_perturbation_onset_time` mark the perturbations, the elbow
7	angle and the torque command at 1 kHz, and up to six EMG channels. Files are streamed from the
8	archive at the pinned version with remfile and h5py (reading the NWB paths directly is much
9	faster than building the pynwb objects of 291 files); nothing is written to disk. Only windows
10	around each perturbation are kept.
11	
12	Where the parameters come from. "Claims" means the opening comment and criteria of
13	claims/pasquereau-2013.yaml, which cite the paper's Methods; "Methods" means the paper's
14	Methods, Data analysis.
15	
16	- Cells studied: units with at least 5 perturbations of each direction (Methods, "for neurons
17	  studied during at least 5 repetitions of each torque direction"; claims).
18	- SDF: spikes convolved at 1 ms with a gamma kernel, k = 1.5, theta = 20 ms (Methods). The
19	  kernel is truncated at 400 ms, where its tail is below 1e-7 of its mass (a standard choice
20	  that cannot change a result).
[... 433 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain']))
            else: print('--OUT-- [',list(d.keys()),']')
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (50.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/a86358e7-52b1-496a-92b7-878dc37d7b28/tool-results/b6lpogtr0.txt

Preview (first 2KB):
==================== 0 markdown
# Pasquereau & Turner (2013) on DANDI:001636

Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
neuronal responses to muscle stretch. *Front. Syst. Neurosci.* 7:98,
[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098).

Dataset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), version
`0.261124.1906` (doi:10.48324/dandi.001636/0.261124.1906). This version was asked for in the
prompt of this attempt; it is also the newest published version (published 2026-11-24). The
paper cites no version.

Claims: `claims/pasquereau-2013.yaml`, written from the full text in PubMed Central
(PMC3840326), its Methods, Results, Table 1, figure legends and supplementary data sheet
(DataSheet1.PDF), whose table gives the results for each monkey.

[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/a86358e7-52b1-496a-92b7-878dc37d7b28/tool-results/b6lpogtr0.txt"
}
```

```
1	==================== 0 markdown
2	# Pasquereau & Turner (2013) on DANDI:001636
3	
4	Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
5	neuronal responses to muscle stretch. *Front. Syst. Neurosci.* 7:98,
6	[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098).
7	
8	Dataset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), version
9	`0.261124.1906` (doi:10.48324/dandi.001636/0.261124.1906). This version was asked for in the
10	prompt of this attempt; it is also the newest published version (published 2026-11-24). The
11	paper cites no version.
12	
13	Claims: `claims/pasquereau-2013.yaml`, written from the full text in PubMed Central
14	(PMC3840326), its Methods, Results, Table 1, figure legends and supplementary data sheet
15	(DataSheet1.PDF), whose table gives the results for each monkey.
16	
17	The files of monkey L mark no torque perturbation, so every claim is tested on monkey V
18	(Venus, elbow), as the claims file says.
19	
20	| Claim | Tested or blocked |
[... 898 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n -i -E "torque|deg|velocity|rectif|EMG|DSI|gamma|threshold|single.trial|trial-by-trial|latenc" 10.3389-fnsys.2013.00098.txt | head -150
```

```
<persisted-output>
Output too large (71.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/a86358e7-52b1-496a-92b7-878dc37d7b28/tool-results/b62if2ski.txt

Preview (first 2KB):
120971 10.3389-fnsys.2013.00098.txt
7:642 frontsysneuro Frontiers in Systems Neuroscience Front Syst Neurosci Frontiers Media SA PMC3840326 3840326 3840326 24324412 10.3389/fnsys.2013.00098 Primary motor cortex of the parkinsonian monkey: altered neuronal responses to muscle stretch Pasquereau Benjamin 1 Turner Robert S 1 * 1 Department of Neurobiology, Center for Neuroscience and The Center for the Neural Basis of Cognition, University of Pittsburgh, Pittsburgh, PA, USA Edited by: Hagai Bergman, The Hebrew University of Jerusalem, Israel Reviewed by: M. Gustavo Murer, Universidad de Buenos Aires, Argentina; Yifat Prut, The Hebrew University of Jerusalem, Israel; Joshua Goldberg, The Hebrew University of Jerusalem, Israel ✉ *Correspondence: Robert S. Turner, Department of Neurobiology, Center for Neuroscience and The Center for the Neural Basis of Cognition, University of Pittsburgh, 4047 BST-3, 3501 Fifth Avenue, Pittsburgh, PA 15261, USA e-mail: [removed: an e-mail address] This article was submitted to the journal Frontiers in Systems Neuroscience. 26 11 2013 7 98 98 9 12 2013 Copyright © 2013 Pasquereau and Turner. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms. Abstract Exaggeration of the long-latency stretch reflex (LLSR) is a characteristic neurophysiologic feature of Parkinson's disease (PD) that contributes to parkinsonian rigidity. To explore one frequently-hypothesized mechanism
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'EOF'
import re
t=open('10.3389-fnsys.2013.00098.txt').read()
s=re.split(r'(?<=[.!?])\s+',t)
keys=['Nm','rectif','spike density','gamma','threshold','DSI','directional selectivity','trial-by-trial','single-trial','single trial','trial by trial','displacement','5 deg','onset of','Velmax','m2max','EMG signals','Hamming','low-pass','reciprocal','bi-directional','bidirectional','non-directional']
for i,x in enumerate(s):
    if any(k.lower() in x.lower() for k in keys):
        print(i, x[:700]); print()
EOF
```

```
12 This was accompanied by a shortening of M1 neuronal response latencies and a degradation of directional selectivity, but surprisingly, no increase in single unit response magnitudes.

19 In neurologically-intact animals, the stretch reflex appears to regulate limb stiffness to maintain precise control of multi-joint posture during interactions with an unstable environment (Rothwell, 1990 ; Shemmell et al., 2010 ; Pruszynski et al., 2011a ).

59 On two-thirds of the trials (selected at random), single flexing or extending torque impulses (0.1 Nm–50 ms duration) were applied to the manipulandum by a DC brushless torque motor (TQ40W, Aerotech Inc., Pittsburgh PA) at an unpredictable time beginning 1–2 s (uniform randomized distribution) after initial capture of the center target.

60 Each square-wave torque impulse induced an angular displacement of the joint (mean = 10-deg) causing a sudden stretch of arm extensor or flexor muscles.

88 EMG signals were differentially amplified (gain = 10-K), band-pass filtered (20-Hz to 5-kHz), rectified and then low-pass filtered (100-Hz).

101 The digitized signal reflecting manipulandum angle was filtered and differentiated [low-pass 25-Hz (Hamming, 1983 )].

102 The onset of torque-evoked movement, peak velocity, and movement termination were detected automatically using angle, velocity, and duration criteria.

103 A velocity threshold of 5-deg/s was used to detect movement.

106 For each muscle, peri-torque means of the digitized EMG signals were constructed for all valid torque perturbations in each direction (flexion and extension).

107 The signal was normalized by subtracting the background activity recorded 200-ms prior to the onset of the torque perturbation.

[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'EOF'
import re
t=open('10.3389-fnsys.2013.00098.txt').read()
s=re.split(r'(?<=[.!?])\s+',t)
for i in list(range(56,64))+list(range(86,112))+list(range(113,146))+list(range(160,176))+list(range(240,252)):
    print(i, s[i][:900]); print()
EOF
```

```
56 The monkey maintained this position for the duration of a start-position hold period (random duration, 2–5 s), during which the animal could not predict the location of the upcoming lateral target.

57 The target then shifted to the left or right (chosen at random), and the animal moved the cursor to capture the lateral target.

58 The animal received a drop of juice for successful completion of the task.

59 On two-thirds of the trials (selected at random), single flexing or extending torque impulses (0.1 Nm–50 ms duration) were applied to the manipulandum by a DC brushless torque motor (TQ40W, Aerotech Inc., Pittsburgh PA) at an unpredictable time beginning 1–2 s (uniform randomized distribution) after initial capture of the center target.

60 Each square-wave torque impulse induced an angular displacement of the joint (mean = 10-deg) causing a sudden stretch of arm extensor or flexor muscles.

61 The animals were not trained to produce a specific response to these unpredictable perturbations, but the animals naturally adopted a strategy that returned the joint to its initial pre-impulse position.

62 Later aspects of the behavioral trial, which evaluated instruction-related neuronal activity, are irrelevant to the current study.

63 Surgery The animals were prepared surgically using aseptic techniques under Isoflurane inhalation anesthesia (Pasquereau and Turner, 2011 ).

86 The action potentials of single neurons (sampled at 60-kHz) were discriminated on-line using template-based spike sorting (MultiSpike Detector, Alpha Omega Engineering, Nazareth, Israel).

87 The timing of detected spikes and of relevant task events was sampled digitally at 1 kHz and saved to disk for offline analysis.

[... 170 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, pasq
rng=np.random.default_rng(0)
def sim(rate, ntr, resp=None):
    trials=[]
    for _ in range(ntr):
        t=np.sort(rng.uniform(-1.5,0.5,rng.poisson(rate*2)))
        if resp:
            extra=rng.uniform(0.03,0.08,rng.poisson(resp*0.05)); t=np.sort(np.r_[t,extra])
        trials.append(t)
    return pasq.sdf_trials(trials).mean(0)
for rate in [3,10,20]:
  for ntr in [8,15]:
    fp=[pasq.detect(sim(rate,ntr),0)['any_crossing'] for _ in range(300)]
    fr=[pasq.detect(sim(rate,ntr),0)['responds'] for _ in range(300)]
    print(rate,ntr,'any crossing %.3f'%np.mean(fp),'respond20-60 %.3f'%np.mean(fr))
m=sim(10,15,resp=200); r=pasq.detect(m,0); print({k:r[k] for k in ['responds','onset','offset','sign','max_change','fwhm']} if r['responds'] else r)
# kinematics: synthetic step in velocity starting at 10 ms
t=np.arange(-200,400)
ang=np.where(t>10, 5*(1-np.exp(-(t-10)/30.)),0.0)
print(pasq.kinematics(ang[None,:], np.array(['flexion'])))
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
ls ~/.venv* /opt 2>/dev/null; which -a python python3 uv pip 2>/dev/null; python3 -m pip --version
```

```
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
pipx_bin
post-generation
primer
runner-cache
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy scipy pandas h5py remfile dandi 2>&1 | tail -2; python -c "import numpy,scipy,pandas;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, pasq
rng=np.random.default_rng(0)
def sim(rate, ntr, resp=None):
    trials=[]
    for _ in range(ntr):
        t=np.sort(rng.uniform(-1.5,0.5,rng.poisson(rate*2)))
        if resp:
            extra=rng.uniform(0.03,0.08,rng.poisson(resp*0.05)); t=np.sort(np.r_[t,extra])
        trials.append(t)
    return pasq.sdf_trials(trials).mean(0)
for rate in [3,10,20]:
  for ntr in [8,15]:
    fp=[];fr=[]
    for _ in range(300):
        r=pasq.detect(sim(rate,ntr),0); fp.append(r['any_crossing']); fr.append(r['responds'])
    print(rate,ntr,'any crossing %.3f'%np.mean(fp),'respond20-60 %.3f'%np.mean(fr))
m=sim(10,15,resp=200); r=pasq.detect(m,0); print({k:r.get(k) for k in ['responds','onset','offset','sign','max_change','fwhm']})
t=np.arange(-200,400)
ang=np.where(t>10, 5*(1-np.exp(-(t-10)/30.)),0.0)
print(pasq.kinematics(ang[None,:], np.array(['flexion'])))
ang2=ang+0.0
print(pasq.kinematics(np.vstack([ang*3]), np.array(['flexion'])))
EOF
```

```
3 8 any crossing 0.223 respond20-60 0.087
3 15 any crossing 0.200 respond20-60 0.060
10 8 any crossing 0.157 respond20-60 0.037
10 15 any crossing 0.167 respond20-60 0.030
20 8 any crossing 0.137 respond20-60 0.037
20 15 any crossing 0.190 respond20-60 0.043
{'responds': True, 'onset': 34, 'offset': 153, 'sign': 1.0, 'max_change': 179.7256600380569, 'fwhm': 55.0}
   latency  peak_velocity  amplitude
0      0.0     104.415202   5.026857
   latency  peak_velocity  amplitude
0      0.0     313.245607  15.080571
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, pasq
from scipy import signal
t=np.arange(-200,400)
for amp in [1,3,10]:
    ang=np.where(t>10, amp*(1-np.exp(-(t-10)/30.)),0.0)
    f=signal.filtfilt(pasq._FIR,[1.0],ang); v=np.gradient(f)*1000
    print(amp,'first t with vel>5:', t[np.argmax(v>5)], 'ms; true onset 10 ms')
EOF
```

```
1 first t with vel>5: 1 ms; true onset 10 ms
3 first t with vel>5: -3 ms; true onset 10 ms
10 first t with vel>5: -5 ms; true onset 10 ms
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001636/versions/0.261124.1906/info/" | $TMPDIR/v/bin/python -c "
import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(d['asset_count'],d['size']);print(m.get('description','')[:3000]);print(json.dumps(m.get('assetsSummary',{}))[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/v/bin/python - <<'EOF'
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("001636","0.261124.1906")
    leu=[a for a in ds.get_assets() if a.path.startswith("sub-Leu/")]
    post=[a for a in leu if "PostMPTP" in a.path]
    print(len(leu),len(post))
    md=post[0].get_raw_metadata()
    print(post[0].path, md.get('variableMeasured'), md.get('description','')[:500])
    print([w.get('name') for w in md.get('wasGeneratedBy',[])])
EOF
```

```
148 50
sub-Leu/sub-Leu_ses-Leu++l12701++PostMPTP++Depth23150um++19930612_behavior+ecephys.nwb [{'value': 'ElectrodeGroup', 'schemaKey': 'PropertyValue'}, {'value': 'SpatialSeries', 'schemaKey': 'PropertyValue'}, {'value': 'Units', 'schemaKey': 'PropertyValue'}, {'value': 'ProcessingModule', 'schemaKey': 'PropertyValue'}] 
['Leu++l12701++PostMPTP++Depth23150um++19930612', 'Metadata generation']
Shell cwd was reset to
```

**Agent**

**Verifier report, round 1: Pasquereau & Turner 2013 on DANDI:001636 (0.261124.1906)**

The claims file has 28 claims. I re-ran the helpers `detect`, `sdf_trials` and `kinematics` on synthetic inputs and queried the archive's metadata; I did not download data or re-run the notebook.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| cell-counts | reproduced | Cell 20: 115/157 cells, 51/54 PTNs, 32/48 CSNs, 3 dual-projecting. All are within tolerance. |
| monkey-l-perturbations | blocked (data_missing) | Cell 15: all 5952 Leu trials are `not_available`. The dandiset description confirms "The Leu files contain no perturbation times". |
| baseline-rate | reproduced | Cell 24: all six means are within tolerance (PTN pre 18.49 vs 20.3±2.46). PTN p = 0.0198 (< 0.05), CSN p = 0.651 (≥ 0.05). The M1 test gives p = 0.0022, below the paper's 0.05/2. |
| ptn-faster-than-csn | reproduced | Cell 26: PTN 18.5 vs CSN 3.5 spikes/s, Mann-Whitney p = 6.3e-12. |
| antidromic-latency | partially_reproduced | Cell 28: all four means are within tolerance (CSN post 6.85 vs 6.1±0.89) and PTN p = 0.68 holds. The CSN test fails: p = 0.019, above 0.05/3 = 0.0167. The variant adding Leu units gives p = 0.0072. |
| false-positive-rate | blocked (methods_underspecified) | Cell 30: the pseudo-onset rate is 0.230, outside 0.0033–0.03. My synthetic test shows the claims file's procedure gives this rate on pure noise (B1). Only the `trial_sd` reading (0.013) falls in range. |
| torque-related-fractions | blocked (methods_underspecified) | Blocked through false-positive-rate, as the claims file's opening comment requires. For information only: under the blocked detection 2 of 6 are within tolerance (cell 32). |
| prevalence-unchanged | blocked (methods_underspecified) | Same gate. Cell 33 would give p > 0.39 for all three groups. |
| ptn-more-responsive | blocked (methods_underspecified) | Same gate. Cell 34: 70.5% vs 17.5%, χ² = 49. |
| one-direction-half | blocked (methods_underspecified) | Same gate. Cell 35: 52.8% vs 44±4.4%. |
| excitatory-majority | blocked (methods_underspecified) | Same gate (cell 36). |
| magnitude-unchanged | blocked (methods_underspecified) | Same gate. Cell 37 would be not reproduced: all 12 tests have p < 0.05. |
| venus-response-magnitudes | blocked (methods_underspecified) | Same gate (cell 38). |
| latency-shorter | blocked (methods_underspecified) | Same gate. Cell 39 shows all four KS tests p < 0.011 with post-MPTP latencies shorter, and 7 of 8 means within tolerance. |
| latency-not-training | blocked (methods_underspecified) | Same gate. Cell 40: pooled ρ = −0.26, p = 0.0016. |
| fwhm-shorter-ptn | blocked (methods_underspecified) | Same gate (cell 41). |
| dsi-reduced | blocked (methods_underspecified) | Same gate (cell 42: p = 0.09). |
| venus-dsi | blocked (methods_underspecified) | Same gate (cell 43). |
| dsi-not-baseline | blocked (methods_underspecified) | Same gate (cell 44: p = 0.31). |
| kinematics-slower | not_reproduced | Cell 48: peak velocity changes by +28.1% pooled and +29.7% flexion; amplitude by +14.8% and +11.1%. Both rise after MPTP under both readings. The matched-command variant (cell 50) also rises (+47%, +40%). |
| kinematic-latency-unchanged | blocked (other: the onset measure in `kinematics` is invalid) | Cell 52 gives F = 709, but the post-MPTP flexion mean onset (3.05 ms) comes before the command leaves rest (4 ms, cell 12). My synthetic test shows the measure finds onset at −5 to +1 ms for a true onset at 10 ms, then clips it to 0 (B2). The output does not test the claim. |
| emg-m2-larger | reproduced (by the criterion; confounded) | Cell 55: m2 is higher after MPTP in all three triceps channels, KS p ≤ 4e-15, under both inclusion rules. The torque was about 3× larger after MPTP, which this comparison does not control (B3). |
| emg-duration-longer | partially_reproduced | Cell 56: durations are longer after MPTP with KS p = 5e-33, but both means are outside tolerance: 22.2 vs 57±6 ms and 51.5 vs 79±3 ms. |
| emg-onset-unchanged | not_reproduced | Cell 57: onset 44.2 → 25.0 ms, KS p = 6e-22. Both inclusion rules give the same result. |
| emg-m1-weak | partially_reproduced | Cell 58: pre-MPTP m2 > m1 in 74.0% of channel-sessions (the criterion needs 75%; median m1/m2 = 0.14). Post-MPTP passes (98.3%, 0.25). The raw_sd rule gives 74.3% pre. |
| velocity-matched-magnitude | blocked (methods_underspecified via the gate; also data) | Only 2 of 581 session-directions have mean peak velocity in 130–200 deg/s (cell 17), leaving 0 or 1 responses (cell 45). It would stay untestable without the gate. |
| session-correlations | blocked (methods_underspecified) | Same gate. Cell 46 would be not reproduced: m2 ρ = −0.38, p = 0.0076 < 0.0125. |
| trial-correlations | blocked (methods_underspecified) | Methods (sentence 144 of the paper text) uses "trial-to-trial response latency" but never defines it. Detection is defined only on the trial-averaged SDF. |

**B. Problems**

1. [affects a conclusion] `detect`, cells 29–30. The false-positive gate could not have passed under the claims file's procedure. On stationary Poisson spike trains (3–20 spikes/s, 8–15 trials), `detect` gives an any-crossing rate of 0.14–0.22, close to the 0.230 found in the data. The paper's 0.01 is an analytic argument that ignores autocorrelation and the error in estimating the SD.
   - The `trial_sd` reading meets the gate (0.013, cell 30), but the notebook never ran the 15 dependent claims under it. The paper leaves the threshold's SD open, so this reading could change their outcome from blocked to tested. At the torque onset it flags only 20% of cell-directions, so torque-related-fractions would likely fail.
   - Possible misreading in the claims file, reported only: Methods (sentence 122) describes a "2-tailed t-test" of SDF values ms by ms against baseline. That matches the notebook's `ttest` variant, not the deciding mean ± t·SD band. The variant's rate (0.465) is worse, so the blocked outcome stands.
2. [affects a conclusion] `kinematics`, cells 48, 50 and 52. The forwards-backwards FIR spreads the velocity rise earlier in time. The 0–200 ms search has no requirement that velocity start below threshold, so early crossings are clipped to 0 ms. Larger, faster post-MPTP displacements are pulled earlier more, so the pre/post latency difference is partly a measurement artifact. Peak velocity and amplitude are not affected.
3. [affects a conclusion] Cells 16, 50 and 55–58. The torque command pulse is about 3× larger after MPTP (median 45.7 vs 181.6 a.u.). The paper reports one 0.1 Nm pulse, and the dandiset description does not mention the difference. For the kinematics a matched-command variant was run; for the EMG claims none was, so the m2, duration and onset differences cannot be separated from stimulus size. Pre-MPTP m2 is also tiny (median about 5 a.u. against 165–301 after), and many pre-MPTP channels have baseline SD below 1 a.u., which suggests the two periods may have different gain or signal quality. The notebook does not check this.
4. [affects a conclusion] Cell 17. The data's displacements (about 3 deg, 46–75 deg/s) are about a third of the paper's (mean 10 deg; 130–200 deg/s for velocity-matched sessions). The angle calibration was never compared with the file's `processing/behavior/ElbowVelocity` or the trials table's `derived_peak_velocity` and `derived_movement_amplitude`. A scale error would not flip the sign in kinematics-slower, but it does make velocity-matched-magnitude untestable.
5. [does not affect a conclusion] Cells 6 and 20. The notebook counts 115/157 cells; the claims file's data check found 112/159 exactly. The claims file says repeated files exist and should be left out of the session measures. The notebook's duplicate check (cell 10) finds none, and it loads `source_file` but never uses it. The counts are within tolerance either way.
6. [does not affect a conclusion] Cell 28 and the claims file. The paper corrects subset tests with Bonferroni–Holm (sentence 138); the criterion uses a flat 0.05/3. Under Holm, CSN would still be the smallest p tested against 0.0167, so the outcome is unchanged.
7. [does not affect a conclusion] Cell 15 and `load_meta`. The notebook computes `torque_cmd_steps` for the 34 post-MPTP Leu files that have a finite torque command but never prints it, so it is not shown whether perturbations could be recovered from the command in those files (B, C).
8. [does not affect a conclusion] Checked and correct: the `gamma_kernel` normalisation (spikes/s, causal), the offset, area and FWHM logic in `detect` (synthetic response: onset 34 ms, offset 153 ms), Yates correction in the 2×2 tables, the DSI formula and categories against Methods (sentences 134–137), and the type II ANOVA.

**C. What I could not check, and the output that would settle it**

- monkey-l-perturbations: the archive confirms no Leu perturbation times. Pre-MPTP stays blocked. Post-MPTP could be partly testable only if the torque command in the 34 Leu files shows pulses. Needed: `torque_cmd_steps` per Leu file, and one plotted command trace.
- The 15 claims blocked by the gate: needed are their results under the `trial_sd` reading (B1).
- Kinematic latency: needed are the latency distribution per state (fraction at exactly 0 ms), the velocity at t = 0, and onsets from a causal filter or with a below-threshold requirement before onset.
- Angle scale: needed is the computed per-trial peak velocity plotted against `derived_peak_velocity` or `ElbowVelocity`.
- EMG confound: needed are the EMG claims rerun on perturbations with matched command size (60–250 a.u.), and grand-average pre and post traces per channel.
- Repeated files and the 112 vs 115 discrepancy: needed are the files sharing a `source_file` value, and the units that differ from the claims file's data-check selection.

## End of run

16 turns, 5 minutes, $1.50 at API prices, result: success.
