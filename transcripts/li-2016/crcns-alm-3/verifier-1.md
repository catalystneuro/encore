# crcns-alm-3 · verifier-1 · run 42413602512

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; find . -maxdepth 2 -type f | head -50
```

```
total 344
drwxr-xr-x 6 runner runner    4096 Nov  7 21:10 .
drwxr-xr-x 7 runner runner    4096 Nov  7 21:10 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 20:57 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 20:57 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  7 21:10 .claude
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env.development
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env.local
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env.production
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env.test
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .env.test.local
drwx------ 2 runner runner    4096 Nov  7 21:10 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 20:57 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 20:57 .github
-rw-r--r-- 1 runner runner       0 Nov  7 21:10 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 20:57 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 20:57 .mcp.json
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1038-nature17643.yaml
```

```
<persisted-output>
Output too large (53.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/9fa35cac-9d5d-4fe9-86f6-c747e3c3feb0/tool-results/bt4vytg3a.txt

Preview (first 2KB):
# Claims for Li, Daie, Svoboda & Druckmann (2016), Nature 532, 459-464, "Robust neuronal dynamics
# in premotor cortex during motor planning", doi:10.1038/nature17643, on CRCNS data set alm-3
# (doi:10.6080/K0RB72JW).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the accepted author manuscript in PubMed Central (PMC5081260, NIHMS767125), as supplied
# under paper/ (Europe PMC): main text, Methods, and the legends of Figures 1 to 6 and Extended Data
# Figures 1 to 10. The paper has no separate Supplementary Information. No PDF of the paper was
# supplied, so values printed only inside figures (per-condition performance in Fig. 1d and 5b,
# fractions in ED Fig. 8a and 8b) were not read; claims on those panels rest on the text and
# legends. The version of record was not read. The record lists a corrigendum
# (doi:10.1038/nature18623) whose text was not supplied or read.
#
# Code. The paper links no analysis or simulation code. The CRCNS data set's description says it
# holds MATLAB analysis scripts that reproduce the paper's figures; they are files of the data set
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/9fa35cac-9d5d-4fe9-86f6-c747e3c3feb0/tool-results/bt4vytg3a.txt"
}
```

```
1	# Claims for Li, Daie, Svoboda & Druckmann (2016), Nature 532, 459-464, "Robust neuronal dynamics
2	# in premotor cortex during motor planning", doi:10.1038/nature17643, on CRCNS data set alm-3
3	# (doi:10.6080/K0RB72JW).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the accepted author manuscript in PubMed Central (PMC5081260, NIHMS767125), as supplied
8	# under paper/ (Europe PMC): main text, Methods, and the legends of Figures 1 to 6 and Extended Data
9	# Figures 1 to 10. The paper has no separate Supplementary Information. No PDF of the paper was
10	# supplied, so values printed only inside figures (per-condition performance in Fig. 1d and 5b,
11	# fractions in ED Fig. 8a and 8b) were not read; claims on those panels rest on the text and
12	# legends. The version of record was not read. The record lists a corrigendum
13	# (doi:10.1038/nature18623) whose text was not supplied or read.
14	#
15	# Code. The paper links no analysis or simulation code. The CRCNS data set's description says it
16	# holds MATLAB analysis scripts that reproduce the paper's figures; they are files of the data set
17	# and were not read here. Every method below is from the paper's text.
18	#
19	# Data the paper used. 33 mice (age > P60). Electrophysiology during behaviour, left ALM, 12 mice
20	# (5 VGAT-ChR2-EYFP, 7 PV-ires-cre x ReaChR), NeuroNexus 32-channel probes: 1012 single units in 58
[... 836 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_li_2016.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    print('=== CELL',i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT data--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
2554 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	67
2	=== CELL 0 markdown
3	# Reproducing Li, Daie, Svoboda & Druckmann (2016) from CRCNS alm-3
4	
5	**Paper.** Li N, Daie K, Svoboda K, Druckmann S (2016). Robust neuronal dynamics in premotor cortex
6	during motor planning. *Nature* 532, 459-464.
7	[doi:10.1038/nature17643](https://doi.org/10.1038/nature17643). The claims file was written from the
8	accepted author manuscript in PubMed Central (PMC5081260): main text, Methods and the legends of
9	Figures 1 to 6 and Extended Data Figures 1 to 10.
10	
11	**Data set.** CRCNS alm-3, [doi:10.6080/K0RB72JW](https://doi.org/10.6080/K0RB72JW), "Data and
12	simulations related to: Robust neuronal dynamics in premotor cortex during motor planning",
13	data description version 0.71 (April 19, 2018). Files are streamed from the public S3 bucket
14	`crcnsarchive`, under `alm-3/live/`. Version: `unversioned`. CRCNS data sets have no versions, and
15	the paper cites none, so the pinned version is the live copy, the only copy of the data files
16	(`alm-3/orig/` holds only documentation); the MD5 sums of the 91 session files read, from the
17	data set's `checksums.md5`, are printed in the data check, so that a later change can be
18	detected. The raw voltage traces (`data/RawVoltageTraces/`, 6 to 12 GB per session) are not used.
19	
20	**Methods from the authors' code.** The data set holds the authors' MATLAB analysis scripts
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	        late = float(ratio[np.argmin(np.abs(GT + stamp_shift - (-0.2)))])
701	        rows.append({"condition": c, "label": alm3.STIM_LABELS[c], "neurons": len(ks), "mice": len({units[k]["mouse"] for k in ks}),
702	                     "recovery_ms": mean * 1000, "sd_ms": sd * 1000, "frac_boot_recovered": frac, "censored_ms": cens * 1000,
703	                     "deficit_at_-0.2s": late})
704	    return pd.DataFrame(rows), ks
705	
706	def mean_rate_traces(exp, conds, fr_min=1.0, min_ctrl=8, min_stim=3, experiments=None):
707	    """Population mean rate (spikes/s, 200 ms boxcar) on control and photoinhibition trials, lick
708	    right and lick left averaged per neuron; neurons as in the code's Fig. 1f and 2d sections."""
709	    exps = experiments or [exp]
710	    out = {}
711	    for c in conds:
712	        ks = [k for k, u in enumerate(units) if EXP[u["session"]] in exps and u["cell_type"] == "pyramidal"
713	              and M[k]["nR"] > min_ctrl and M[k]["nL"] > min_ctrl and c in M[k]["cond"]
714	              and M[k]["cond"][c]["nR"] > min_stim and M[k]["cond"][c]["nL"] > min_stim and M[k]["fr_mean"] > fr_min]
715	        ctrl = np.array([(M[k]["psth_ctrl_all"][1] + M[k]["psth_ctrl_all"][-1]) / 2 for k in ks])
716	        stim = np.array([(M[k]["cond"][c]["psth"][1] + M[k]["cond"][c]["psth"][-1]) / 2 for k in ks])
717	        P = np.array([M[k]["cond"][c]["p_rate"] for k in ks])
718	        out[c] = {"ks": ks, "ctrl": ctrl, "stim": stim, "p": P}
719	    return out
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1400,
 "limit": 700
}
```

```
1400	=== CELL 37 code
1401	for by in ("mouse_pooled", "session_mean"):
1402	    t, n = performance_table(["unilateral"], [1, 2, 3], by=by)
1403	    print(f"Performance (% correct) per mouse, {by}:")
1404	    print(t.round(1).to_string())
1405	    for paired in (True, False):
1406	        print(f"  {'paired' if paired else 'unpaired'} t-test against control:")
1407	        print(perf_tests(t, [2, 3, 1], paired=paired).round(4).to_string(index=False))
1408	print("\nTrials per mouse and condition:")
1409	print(n.to_string())
1410	--OUT--
1411	Performance (% correct) per mouse, mouse_pooled:
1412	stim        0.0   1.0   2.0   3.0
1413	mouse                            
1414	ANM255200  79.2  78.3  73.8  80.9
1415	ANM255201  85.1  90.9  83.5  81.0
1416	ANM255203  74.2  69.0  60.0  70.8
1417	ANM257772  79.5  82.2  80.6  66.9
1418	  paired t-test against control:
1419	 condition                            label  mice  control_%  photoinhibition_%    drop       t      p
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 2100,
 "limit": 460
}
```

```
2100	    for P in pops:
2101	        if which == "cd":
2102	            proj, _, _ = cd_projections(P, kind, "inside")
2103	        else:
2104	            proj = which(P)
2105	        lick_right = np.where(P["hit"], P["side"] == 1, P["side"] == -1)
2106	        for c in [0] + conds:
2107	            idx = np.r_[P["test"][1], P["test"][-1]] if c == 0 else np.r_[P["groups"][(c, 1)], P["groups"][(c, -1)]]
2108	            for i in idx:
2109	                rows.append({"session": P["session"], "mouse": P["mouse"], "condition": c, "proj": proj[i, t_index],
2110	                             "lick_right": bool(lick_right[i]), "instructed_right": P["side"][i] == 1, "hit": bool(P["hit"][i])})
2111	    return pd.DataFrame(rows)
2112	
2113	def prediction_table(df):
2114	    rows = []
2115	    for c, d in df.groupby("condition"):
2116	        pred = d.proj > 0
2117	        correct = int((pred == d.lick_right).sum())
2118	        b = stats.binomtest(correct, len(d), 0.5, alternative="greater")
2119	        lr = sm.Logit(d.lick_right.astype(float), sm.add_constant(d.proj.values)).fit(disp=0)
[... 436 more lines not kept]
```

**Agent**

I've read the notebook outputs. Next I'm reading the helper modules and the truncated ed8a table, and testing helpers on synthetic inputs.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_li_2016.ipynb'))
c=nb['cells'][52]
for o in c['outputs']:
    if 'text' in o: print(''.join(o['text'])[5500:])
"
```

```
98.3          0.3     95.8          0.9       False      False
      all  half meandiff    trial squared        17    68.2         4.1    43.3         5.0     95.0          0.8     92.0          1.7       False      False
      all  half meandiff    trial     rms        17    81.9         2.6    63.9         4.0     97.4          0.4     95.9          0.9       False      False
      all  half      lda      pre squared        17    62.3         4.9    36.9         5.1     96.6          0.6     91.8          1.7       False       True
      all  half      lda      pre     rms        17    77.8         3.2    58.5         4.0     98.3          0.3     95.8          0.9       False      False
      all  half      lda    trial squared        17    62.3         4.9    38.4         4.8     94.8          0.9     91.9          1.7       False       True
      all  half      lda    trial     rms        17    77.8         3.2    59.9         3.9     97.4          0.5     95.8          0.9       False      False
      all   loo meandiff      pre squared        17    74.6         3.9    42.7         5.0     97.6          0.4     93.5          1.7       False      False
      all   loo meandiff      pre     rms        17    85.8         2.5    63.5         3.8     98.8          0.2     96.6          0.9       False      False
      all   loo meandiff    trial squared        17    74.6         3.9    43.2         4.6     95.9          0.7     93.5          1.7       False      False
      all   loo meandiff    trial     rms        17    85.8         2.5    64.1         3.7     97.9          0.4     96.6          0.9       False      False
      all   loo      lda      pre squared        17    69.5         4.5    38.6         4.9     97.5          0.4     93.4          1.7       False       True
      all   loo      lda      pre     rms        17    82.6         2.9    60.2         3.8     98.7          0.2     96.6          0.9       False      False
      all   loo      lda    t
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "alm3.py"
}
```

```
1	"""Loading and measures for CRCNS data set alm-3 (Li, Daie, Svoboda & Druckmann 2016, Nature 532,
2	459-464, doi:10.1038/nature17643).
3	
4	The data set holds one MATLAB file per recording session (`data/data_structure_files/`), each a
5	structure `obj` with the trial table, the photostimulus type of each trial, the lick and laser
6	traces, and the spike times of the sorted single units. Files are streamed from the public S3
7	bucket `crcnsarchive` into memory and reduced as they load; nothing is written to disk. CRCNS data
8	sets are not versioned; the files read are those under `alm-3/live/` with the MD5 sums of the data
9	set's `checksums.md5`.
10	
11	Where the parameters come from. "Code" is the authors' MATLAB analysis scripts deposited in the
12	data set (`alm-3/live/analyses_scripts/`), which the data set's description says reproduce the
13	paper's figures; the claims file did not read them. They are cited by file name.
14	
15	- Trials (`trial_mask`): correct and error trials grouped by instructed movement (HitR or ErrR is
16	  lick right, HitL or ErrL lick left), lick-early trials and trials marked GoodTrials = 0 dropped,
17	  and only trials between the unit's first and last trial with a spike (the unit's stable
18	  trials). Code, analysis_compile_all_data_unilateral.m, "index the behavioral trials" and "index
19	  stable trials"; the Methods, Electrophysiology data analysis, say selectivity under
20	  photoinhibition uses "all trials, correct and incorrect, grouped by instructed movement".
[... 650 more lines not kept]
```

**Agent**

Notebook and helper read. Now checking `models.py`, the paper passages on ED Fig. 4 and the spike-width/sampling details, and the archive listing for the blocked claims.

**Agent calls Read**

```json
{
 "file_path": "models.py"
}
```

```
1	"""Network models of Li, Daie, Svoboda & Druckmann (2016), Methods, "Modeling and simulation",
2	and Extended Data Fig. 1f-i. No recorded data are used.
3	
4	Every network follows tau dr/dt = -r + W f(r) + I(t) + T + xi(t), simulated for 2 s by Euler
5	steps; photoinhibition holds the silenced neurons at zero for 0.2 s < t < 1.0 s (Methods).
6	Parameters are the Methods' unless said otherwise:
7	
8	- Modular attractor (Fig. 6b): two modules of two neurons; self weight 0.5235, within-module
9	  -0.5235, each neuron coupled to its same-preference partner in the other module with 0.3;
10	  tau = 100 ms; f(x) = g(x) - g(0), g(x) = 1.4 / (1 + exp(-(x - 0.5) / 0.3)); transient input
11	  0.1 to the neurons preferring the trial type for 0.05 s < t < 0.1 s; tonic input 0.5; noise of
12	  variance 0.01. Whether the variance is per step or per unit time is not stated; both are run
13	  (`noise="step"`: xi drawn each step with variance 0.01; `noise="time"`: white noise of
14	  intensity 0.01 per second). That the partner is the same-preference neuron is an assumption
15	  (the Methods say "one partner").
16	- Modular integrator (Fig. 6c): the printed 8 x 8 matrix, linear synapses, rates kept
17	  non-negative, tau = 10 ms, input +-0.04 to the right and left preferring neurons of both
18	  modules for 0.1 s < t < 1.9 s (persistent input, Methods), tonic 40 to the four integrator
19	  neurons, no noise.
20	- Simple integrator (ED Fig. 1f): N = 100, tau = 100 ms, linear, connectivity with one non-zero
[... 158 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "Extended Data Figure 4|27 neurons|corrective|integrator|0\\.5235|tonic|8 x 8|W =|modular",
 "path": "paper/10.1038-nature17643.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; sed -n 7p 10.1038-nature17643.txt | fold -w 4000 > $TMPDIR/p.txt; wc -c $TMPDIR/p.txt; grep -o -i -E ".{400}(Extended Data Fig(ure)?\.? 4|27 neurons|eigenvalue|0\.5235|tonic input|modular integrator|persistent input|inter-module|subset of 10|spike rate during photoinhibition|time-matched).{600}" 10.1038-nature17643.txt | head -30
```

```
88577 /tmp/claude-1001/p.txt
overshoots in spike rate after photoinhibition (i.e. “rebound”). First, we used photostimuli optimized to minimize rebound 3 ( Extended Data Fig. 2c ). Second, selectivity also recovered, so that activity reached the appropriate spike rate for each trial type. Finally, neurons that normally did not exhibit increasing ramps during the delay epoch also recovered their activity ( Fig. 1e , neuron 3; Extended Data Fig. 4 ). Within 400 ms after photoinhibition, spike rates became indistinguishable from the unperturbed condition in 90% of the neurons; only 10% of neurons retained a sustained change in spike rate ( Fig. 1f ). ALM neurons recovered > 80% of their selectivity relative to the unperturbed trials within 514 ms after photoinhibition ( Fig. 1g ). In separate experiments we transiently (500 ms) photostimulated a subset of layer 5 pyramidal neurons ( Extended Data Fig. 5 ) 30 . After photostimulus offset, ALM activity and selectivity recovered with a time-course that was similar to recovery after photoin
Figs 1 , 2 ) to predictions from network models ( Extended Data Fig. 1 ). After ipsilateral photoinhibition ALM activity rapidly recovered to the unperturbed trajectory ( Figs 1 , 3 ). This is inconsistent with attractors with a pair of fixed points (one for each choice condition) 29 . Upon release from perturbation these models decay to the final fixed point and do not return to the trajectory ( Extended Data Fig. 4c ). Integrator models with a continuum of fixed points generate ramping activity by integrating their inputs 5 , 41 28 37 ; these models predict an activity offset compared to the unperturbed trajectories, inconsistent with the data ( Extended Data Fig. 1f, g ). We also tested randomly connected recurrent networks trained to produce ramping triggered by a transient input 22 - 24 (“trained RRNs”). These models failed to recover from perturbations ( Extended Data Fig. 1h, i ). Overall, all “monolithic” models consisting of on
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -E "(27 neuro|Experiment 3, data|Extended Data Figure 7|Recovery of selectivity after unilateral|preferred trial type|Neurons were tested for|Electrophysiology data analysis|Figure 1 |selective neurons tested|Fig. 2e|e. Selectivity|f. Fraction|g. Selectivity).{900}" 10.1038-nature17643.txt | head -20
```

```
Fig. 2e ) recovered 600 ms after ipsilateral perturbation. ALM activity was hardly affected by contralateral photoinhibition ( Fig. 2c, d ; Extended Data Fig. 2e ). After bilateral photoinhibition neurons recovered their spike rate on average ( Fig. 2c, d ), but selectivity failed to recover ( Fig. 2c-e ). Bilateral photoinhibition with one laser spot produced a larger persistent change in selectivity than unilateral photoinhibiton with four laser spots ( Extended Data Fig. 7 ). Recovery of selectivity after unilateral photoinhibition was less robust with larger photoinhibition size ( Extended Data Fig. 7e ), similar to behavior ( Fig. 2b ). Robustness to perturbation results from redundancy within the bilateral ALM network. Robustness along the coding direction Robust systems maintain critical functions in response to perturbations, whereas non-critical features may remain uncorrected 26 . We 
Figs 2e , 8d ) implies further that ALM hemispheres function as “modules”, maintaining preparatory activity independently 28 . After unilateral perturbation, information from the unperturbed side helps recover function of the perturbed side. To directly test the role of contralateral ALM input as the corrective signal, we bisected the ALM corpus callosum (CC) (n=7 mice) ( Fig. 5a , Methods), sparing pyramidal tract and corticothalamic axons ( Extended Data Fig 10 ). Remarkably, behavioral performance was unaffected ( Fig. 5b , control trials, before vs. after callosotomy, p>0.05, two-tailed t-test), with normal performance 17 hours after callosotomy ( Extended Data Fig. 10b ). However, behavioral performance was now highly sensitive to transient unilateral photoinhibition ( Fig 2b , 1 laser spot: p=0.0019, two-tailed t-test against control). There was a significant interaction between callosoto
Figs 2e , 8d ). However, after the perturbation, activity in the unperturbed hemisphere is critical to restore the perturbed preparatory activity in the opposite hemisphere. Preparator
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o -E "Modular integrator \(<xref.{2500}" 10.1038-nature17643.txt | head -2; grep -o -E "Modular FORCE.{300}|(Fig. 6c|Fig\. 6 c).{0,10}" 10.1038-nature17643.txt | head
```

```
Modular integrator (<xref ref-type="fig" rid="F6">Fig. 6c</xref>) This network consisted of two modules with inter-module connections tuned to produce robustness against unilateral inactivations. Each module consisted of four neurons: Right preferring integrator neuron (1); left preferring integrator neuron (2); recovery neuron (3); inhibitory neuron (4). Integration was produced by positive feedback achieved through mutual inhibition between neurons 1 and 2 with strength −1. This integrating pair is represented schematically by one circle labeled “∫” in Figure 6c . The network received constant sensory input I i (t) with amplitude 0.04 to the right preferring neuron and −0.04 to the left preferring neuron during “lick right” trials. The signs of the inputs were flipped for “lick left” trials. In addition, each integrator neuron received non-selective tonic input T i (t) with amplitude 40.0 to establish baseline activity at 20.0. To establish robustness the two modules were coupled via the recovery (labeled “R”; Fig. 6C ) and inhibitory (labeled “I”; Fig. 6C ) neurons. These neurons receive positive feedback from the right preferring neuron and negative feedback from the left preferring neuron. The role of the recovery neuron is to restore the activity of the contralateral integrator neurons upon removal of inhibition. This restorative connection has strength 0.5. To avoid excessive feedback during normal function the recovery neuron is strongly inhibited by the inhibitory neuron with strength − 6.0. The full connectivity matrix is shown below. For one module, indices 1-4 correspond to the right preferring, left preferring, recovery and inhibitory neurons. Indices 5-8 are part of the second module. For example, element W 1,7 is the connection from the recovery neuron in module 2 (neuron 7) onto the right preferring neuron of module 1 (neuron 1). W = ( 0 − 1 0 0 0 0 0.5 0 − 1 0 0 0 0 0 − 0.5 0 1 − 1 0 0 0 0 0 − 6 1 − 1 0 0 0 0 0 0 0 0 0.5 0 0 − 1 0 0 0 0 − 0.5 0 − 1 
[... 3 more lines not kept]
```

**Agent**

Paper passages checked. Now running cheap synthetic tests of `recovery_time`, `boundary`, `auc`, `binned_window`, and the integrator asymmetry.

**Agent calls Bash**

```bash
cd  timeout 600 python3 -c "
import numpy as np, alm3, models
# recovery_time: ctrl selectivity 1, stim deficit decays linearly to 0 by 0.5 s after offset
t=np.round(np.arange(-1,0.01,0.01),3); off=-0.8
ctrl=np.ones((50,len(t))); stim=ctrl.copy()
d=np.clip(1-(t-off)/0.5,0,1); d[t<=off]=1
stim=ctrl-d
print('recovery (expect ~0.4 s):',alm3.recovery_time(ctrl,stim,t,off,0.0,np.random.default_rng(0),n_boot=50))
# boundary
print('boundary eq var (expect 0):',alm3.boundary(np.array([1.,2,3]),np.array([-1.,-2,-3])))
print('auc (expect 1, 0.5):',alm3.auc(np.array([2.,3]),np.array([0.,1])), alm3.auc(np.array([1.,1]),np.array([1.,1])))
# binned_window: 1 spike in each 10ms bin
b=np.ones((2,alm3.NB10),dtype=np.uint8)
print('binned_window 0.4 s (expect 40):',alm3.binned_window(b,[-0.2,0.2],0.4))
# integrator asymmetry
for tr in (1,-1):
    o=models.run_integrator(tr,None); p=models.run_integrator(tr,[0,1,2,3])
    print('integrator trial',tr,'R-L unpert',round(o[-1,0]-o[-1,1],2),'pert',round(p[-1,0]-p[-1,1],2),'module2 pert',round(p[-1,4]-p[-1,5],2), 'recovery neurons max after release', p[1000:,[2,6]].max(0).round(2))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, alm3, models
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls node_modules; which -a python3 python uv pip3 conda 2>/dev/null; ls ~/.venv* /opt 2>/dev/null | head
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip3
/usr/bin/pip3
/bin/pip3
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
for p in /usr/bin/python3; do $p -c "import numpy, scipy; print('$p ok', numpy.__version__)"; done 2>&1; cd $TMPDIR && uv venv -q v 2>&1 | tail -1; uv pip install -q --python v/bin/python numpy scipy requests fsspec 2>&1 | tail -2; v/bin/python -c "import numpy, scipy; print('venv ok')"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy; print('/usr/bin/python3 ok', numpy.__version__)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
venv ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  timeout 900 $TMPDIR/v/bin/python -c "
import numpy as np, alm3, models
t=np.round(np.arange(-1,0.01,0.01),3); off=-0.8
ctrl=np.ones((50,len(t)))
d=np.clip(1-(t-off)/0.5,0,1); d[t<=off]=1
stim=ctrl-d
print('recovery (expect ~0.4 s):',alm3.recovery_time(ctrl,stim,t,off,0.0,np.random.default_rng(0),n_boot=50))
print('boundary eq var (expect 0):',alm3.boundary(np.array([1.,2,3]),np.array([-1.,-2,-3])))
print('auc (expect 1, 0.5):',alm3.auc(np.array([2.,3]),np.array([0.,1])), alm3.auc(np.array([1.,1]),np.array([1.,1])))
b=np.ones((2,alm3.NB10),dtype=np.uint8)
print('binned_window 0.4 s (expect 40):',alm3.binned_window(b,[-0.2,0.2],0.4))
for tr in (1,-1):
    o=models.run_integrator(tr,None); p=models.run_integrator(tr,[0,1,2,3])
    print('integrator trial',tr,'R-L unpert',round(o[-1,0]-o[-1,1],2),'pert',round(p[-1,0]-p[-1,1],2),'module2 pert',round(p[-1,4]-p[-1,5],2), 'recovery neurons max after release', p[1000:,[2,6]].max(0).round(2))
# lda sign
rng=np.random.default_rng(1); XR=rng.normal(1,1,(50,5)); XL=rng.normal(0,1,(50,5))
print('lda dir', alm3.lda_direction(XR,XL).round(2))
"
```

```
recovery (expect ~0.4 s): (0.3999999999999999, 1.1214946133455537e-16, 1.0, 0.3999999999999999)
boundary eq var (expect 0): 0.0
auc (expect 1, 0.5): 1.0 0.5
binned_window 0.4 s (expect 40): [[40 40]
 [40 40]]
integrator trial 1 R-L unpert 14.4 pert 13.62 module2 pert 14.4 recovery neurons max after release [0.   7.12]
integrator trial -1 R-L unpert -14.4 pert -7.2 module2 pert -14.4 recovery neurons max after release [0. 0.]
lda dir [0.56 0.36 0.42 0.34 0.51]
```

**Agent**

Helpers behave correctly on synthetic input; the integrator's left-trial failure is a property of the printed matrix with rectification. Now querying the archive listing for the blocked claims.

**Agent calls Bash**

```bash
cd  timeout 300 $TMPDIR/v/bin/python -c "
import alm3, collections
f=alm3.list_files()
print(len(f))
d=collections.Counter()
for k,v in f.items():
    parts=k.split('/')
    d['/'.join(parts[:5])]+=1
for k,v in sorted(d.items()): print(v,k)
print([k for k in f if 'data_structure' not in k and 'RawVoltage' not in k][:200])
"
```

```
224
1 alm-3/
1 alm-3/live/
1 alm-3/live/analyses_scripts/
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral.mat
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateralCCX.mat
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateralCCX_FR.mat
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_FR.mat
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_activityModes.mat
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_activityModesCCX.mat
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_predictBehavior.mat
1 alm-3/live/analyses_scripts/ALM_compiled_all_data_unilateral.mat
1 alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral.m
1 alm-3/live/analyses_scripts/analysis_compile_all_data_bilateralCCX.m
1 alm-3/live/analyses_scripts/analysis_compile_all_data_bilateralCCX_FR.m
1 alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_FR.m
1 alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_activityModes.m
1 alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_activityModesCCX.m
1 alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_predictBehavior.m
1 alm-3/live/analyses_scripts/analysis_compile_all_data_unilateral.m
[... 206 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "lick|behavior only|behaviou?ral sessions|photoactivation|not included|simulat|sampl(ed|ing) (rate|at)|kHz|cellType|spike width" alm-3.data-description.txt | head -40
```

```
34:The extracellular recording traces were band-pass filtered (300-6 kHz).  Events that exceeded an 
36:sorting to extract single units.  Spike widths were computed as the trough-to-peak interval in the 
37:mean spike waveform.  Units with spike width < 0.35 ms were defined as fast-spiking (FS) 
38:neurons and units with spike widths > 0.45 ms as putative pyramidal neurons. Units with 
47:Li, Daie, Svoboda, Druckman (2016); Data and simulations related to: Robust neuronal 
85:trialTypeMat: each column describes one trial by the description in trialTypeMat (e.g. a “lick 
86:left” trial in which the animal correctly reported choice will have a entry of “1” for “Correct lick 
87:left” and “0” for “Error lick left”.  A phostostimulation trial will have “1” for “StimTrial”).  The 
149:idStr: e.g. {'lick_trace'  'aom_input_trace' ‘laser_power’}, description of the time series data 
151:Channel 1 is typically licking traces.   
175:waveform: snippets of spike waveform.  Each snippets is 29 samples long (sampled at 
180:cellType: {“pyramidal” or “FS”}.  “Pyramidal”, putative pyramidal neuron identified by 
236:A: These are the trials in which mice licked early, which led to pauses during the 
237:trial.  These lick early trials should be excluded from all analyses. You will find 
238:these trials in 'obj.trialTypeStr' marked as 'LickEarly'
```

**Agent calls Bash**

```bash
cd paper; sed -n 1,60p alm-3.data-description.txt; sed -n 140,200p alm-3.data-description.txt; sed -n 225,260p alm-3.data-description.txt
```

```
Data descriptor: of the data set CRCNS:alm-3, not a paper. It describes the data set's files and how they were recorded.
Version: as published by CRCNS.org, https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-3/live/docs/crcns_alm-3_data_description.pdf
Source: the CRCNS data set's documentation (alm-3/live/docs/crcns_alm-3_data_description.pdf; alm-3/live/docs/crcns_alm-3_FAQ.pdf; alm-3/orig/README.txt)
Stored: 2026-11-05
Extracted: PyMuPDF, dehyphenated, NFKC
------------------------------------------------------------------------
##### alm-3/live/docs/crcns_alm-3_data_description.pdf
Page 1 of 5 
CRCNS.org alm-3 data description 
Version 0.71 (April 19, 2018) 
 
 
Summary 
These experiments measure neuronal responses after transiently silencing parts of mouse 
premotor cortex (anterior lateral motor cortex, ALM).  The data represent extracellular 
recordings from ALM neurons of adult mice performing pole location discrimination.  Data from 
91 recording sessions are included in this release.  
This dataset contains data from 19 mice (age > P60).  5 VGAT-ChR2-EYFP mice 
(Jackson laboratory, JAX Stock#014548) and 7 PV-ires-cre crossed to Rosa26-LSL-ReaChR, 
red-shifted channelrhodopsin reporter mice (JAX 24846), were used for simultaneous 
[... 137 more lines not kept]
```

**Agent**

**Verifier report, round 1: Li et al. 2016 (doi:10.1038/nature17643) on CRCNS alm-3**

The claims file has 29 claims and the notebook covers all 29. My outcomes: 9 reproduced, 7 partially reproduced, 8 not reproduced, 5 blocked.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| units-and-sessions | not_reproduced | Cell 12: units 1012, sessions 20 + 38, mice 12 and pyramidal 890 match exactly. FS is 89 by label, 98 by width and 104 upsampled, against 72; intermediate is 33 or 24 against 50. The criterion only allows partial if class counts are within 10%, and they are not. |
| ed1-selective-fraction | reproduced | Cell 14, correct trials, lick-early excluded: 633, 176, 336, 493 (1.3 s response) and 635, 176, 336, 490 (1.5 s, reading b). All four counts are within 10%. |
| fig1d-late-delay-ipsilateral-bias | blocked (data_missing) | Cell 7: no recorded condition ends at the cue (latest offset is −0.31 s). The FAQ and the archive listing confirm that behaviour-only sessions are not deposited. |
| fig1d-earlier-photoinhibition-minimal | reproduced | Cell 37: early delay p = 0.23 and middle delay p = 0.22 (paired, pooled); every reading gives p ≥ 0.18, so none reaches p < 0.05. Performance drops 4.6 to 5.4 points over only 4 mice, and these are recording sessions, not the paper's behaviour sessions. Power is low. |
| ed3-recovery-interval | blocked (data_missing) | See item 4 below. |
| ed2b-silencing | reproduced | Cell 26, window (a): ipsilateral and bilateral reductions are 0.885 to 0.962 in every experiment. Exp 2 ipsilateral by line: VGAT 0.845, PV 0.951. Contralateral normalized rate 0.945, 0.986 and 1.152, all within 0.8 to 1.2. Under window (b) Exp 3 contralateral is 1.222 and fails. VGAT exp2b is 0.75 (item 8 below). |
| ed2d-spatial-extent | blocked (data_missing) | There are no recordings from untrained mice in the archive listing. |
| ed2e-no-rebound | not_reproduced | Cell 28: the population mean is not above control (p = 0.57 and 0.62). In the first 400 ms, though, 24 neurons are significantly excited against 9 suppressed, and the criterion needs fewer excited than suppressed. See item 13(i) on how the criterion reads the paper. |
| fig1f-rate-recovery | partially_reproduced | Cell 18: neuron counts are exactly 168, 168, 175. The fraction is 0.18, 0.20, 0.11 under reading (a) and 0.13, 0.14, 0.09 under reading (b), with means 0.161 and 0.122. Neither is within 0.10 ± 0.01; all are below 0.2. |
| fig1g-selectivity-recovery | partially_reproduced | Cell 20: with 200 ms windows stamped at their centre, all three recovery times are within tolerance in all four readings (e.g. 347, 420, 236 ms), and nearly every resample recovers. But the neuron count is 70 to 87 against 55 ± 5.5 in every reading, so this is not the paper's neuron set. |
| ed4-return-to-trajectory | not_reproduced | Cell 30, decreasing neurons, early delay: the RMS to time-matched control (0.526) is larger than the RMS to the end point (0.463), p = 0.019, the opposite direction, with 14 of 47 favouring time-matched. Pooled conditions: p = 0.18. n = 55 against 27. The window may be biased (item 2). |
| ed5-photoactivation | blocked (data_missing) | The FAQ says the photoactivation data were not published, and no such files are in the listing. |
| fig2b-bilateral-behaviour | partially_reproduced | Cell 39: ipsilateral 1 spot 69.3% is within tolerance. Ipsilateral 4 spots 75.6%, bilateral 1 spot 65.8% and bilateral 4 spots 58.1% are outside. Ipsi 4 spots against control p = 0.15, and bilateral 1 spot against ipsi 4 spots p = 0.12, with only 3 mice. The order control > unilateral > bilateral 1 spot > bilateral 4 spots holds. |
| ed6-bilateral-bias-inconsistent | reproduced | Cell 58: 8 sessions are biased, 6 towards lick right and 2 towards lick left. The sign agrees with the nearer control mean (reading b) in 0.88 with pyramidal neurons; it is 0.75 with all units and 0.62 under reading (a). This passes on one reading only, with n = 8. |
| fig2-bilateral-recovery | not_reproduced | Cell 22: ipsilateral rate recovers (ratio 0.958, 9.4% of neurons still changed). But ipsilateral selectivity reaches 80% before the cue in only 1 to 30% of resamples, and the deficit at −0.2 s is 0.48 to 0.58 in every reading. The rows flagged "within tolerance" are misleading (item 1). Contralateral (240 ms) and bilateral (no recovery) agree with the paper. Bilateral rate is 1.114 at the cue, outside 10%. |
| ed7-unilateral-4-spots-bilateral-1-spot | not_reproduced | Cell 24: bilateral 1 spot reaches 80% of control before the cue in 51 to 80% of resamples (335 to 557 ms), and the claim needs it not to. Neurons: 32 or 29 against 40 ± 4. Bilateral delta selectivity is larger than ipsi 4 spots, but p = 0.53. |
| ed7e-size-and-roc | not_reproduced | Cell 48: bilateral 1-spot ROC is 0.598 to 0.642, above the 0.594 limit (0.54 ± 0.054), in every reading. It passes only with the 0.08 variant tolerance. Ipsi 4 spots (0.62) is below Exp 2 ipsi 1 spot (0.71). Only 4 or 5 sessions. |
| fig3-cd-roc | reproduced | Cell 44: 16 sessions. Pyramidal neurons, leave-one-out split: 0.731, 0.713, 0.742, 0.592, all within tolerance but at the edges. Only 2 of 16 readings pass. |
| ed8-roc-during-photoinhibition | reproduced | Cell 46, reading (b), all units, code split: 0.703, 0.534, 0.642, 0.539, all within tolerance. Only 3 of 32 readings pass. |
| ed9b-cd-stability | reproduced | Cell 50: 0.590 ± 0.075 (pyramidal) and 0.622 (all units), both within 0.61 ± 0.05. |
| ed8a-mode-variance | partially_reproduced | Cell 52: the two cd values are within tolerance in several readings (e.g. pyramidal, random-half split, squared norms: 67.1 and 39.9). No reading has modes 1 to 5 at ≥ 98.0 variance and ≥ 94.6 selectivity together. |
| fig3-cd-predicts-movement | reproduced | Cell 54: in all four conditions accuracy is 0.67 to 0.73, binomial p ≤ 7e-12 and logistic p ≤ 2.5e-10. |
| fig3-other-modes | not_reproduced | Cell 56: the persistent and ramping modes predict control behaviour (binomial p = 0.003 and 0.002, pyramidal, code split). The ipsilateral persistent-mode shift (−2.09) lies inside the control s.e.m. band (2.17). No reading meets every condition. |
| ed9f-reaction-time | blocked (data_missing) | Cells 9 and 62: all 26 Exp 2 lick traces are noise-like (range 0.0018, against 0.05 in sessions that show licks). Part could be tested (item 4). |
| fig5b-callosotomy-behaviour | partially_reproduced | Cell 41: after the cut, unilateral photoinhibition lowers performance with p = 0.0033 (paired; 0.0071 using the mean over sessions), to 59.1%, within 58.0 ± 5.8. The before/after test and the interaction are blocked, as there are no sessions before the cut in the archive. |
| fig5-callosotomy-recovery | reproduced | Cells 34 and 60: ipsilateral rate is back within 10% (1.05 to 1.08), ipsilateral selectivity does not recover (0.3% of resamples), contralateral recovers in 297 ms (also 260 to 278), bilateral does not. Ipsilateral cd ROC 0.566 is reduced against both references (p = 0.006 and 0.003). 125 neurons against 129; 16 sessions. |
| ed10e-callosotomy-preparatory-activity | not_reproduced | Cell 32: 519 callosotomy pyramidal neurons against 496 (tolerance 0). The selective fraction is 12.7 to 14.3 points below control mice, more than the 10 allowed. The selective count (259 with all trials) is within tolerance. |
| models-monolithic-fail | partially_reproduced | Cell 64: the simple integrator (0.212, just over the 0.2 threshold), the monolithic attractor and the FORCE network all fail to recover in 3 of 3 draws. The corrective-feedback integrator and the tamed-chaos network were not simulated (methods_underspecified). |
| fig6-modular-models-robust | not_reproduced | Cell 66: the modular integrator does not recover on left trials (−7.2 against −14.4); the printed matrix causes this (item 5). The attractor's step-noise result passes, but the bilateral "random fixed point" check rests on states that have not settled. |

**B. Problems**

1. [affects a conclusion] Cells 16 and 22, `recovery_readings`. `within_tol` compares `recovery_ms` with the paper and ignores `frac_boot_recovered`. `recovery_ms` is the mean over only those resamples that recover. The two fig2 ipsilateral rows marked within tolerance (637 and 533 ms) come from 30% and 16% of resamples; the mean that counts non-recovering resamples is 821 to 840 ms. The same applies to fig5 contralateral (81% of resamples) and ed7.
2. [affects a conclusion] Cell 30, `ed4_rows`. The RMS window starts just after photoinhibition offset, but it uses 200 ms windows centred on each time, so the first 100 ms still includes photoinhibition and the ramp. For decreasing neurons this inflates the time-matched RMS and favours the end point; for increasing neurons it does the reverse. That may explain why the two directions come out opposite. Also, the end point is the window from −0.3 to −0.1 s, not the last 400 ms of the delay as the criterion says.
3. [affects a conclusion] Cell 15, `selection`. It counts a neuron as selective on the sample or delay epoch only, following the authors' code, and adds a filter |preference| > 1. The claims file (M3) defines selective as any of sample, delay or response. The counts for fig1g (70 to 87 against 55) and ed7 (32 against 40) are not explained.
4. [affects a conclusion] Cells 10, 16 and 20, the selectivity-trace method (M4). Each experiment runs only one screening rule: 5 trials per type for Exp 1, 10 per type elsewhere. The other screening reading, and setting the preference from the epoch where the neuron is most selective, were never run, although the claims file asks for "M4 with all readings". So the not_reproduced outcomes for fig2 and ed7 have not been checked under every reading.
5. [affects a conclusion] Cell 66 and `models.py`.
   - After bilateral silencing, 80 to 83% of attractor runs have not settled by 2 s. The sign of an unsettled state is close to a coin flip, so the 25 to 75% "wrong fixed point" test passes trivially.
   - The integrator's failure on left trials comes from the printed matrix itself: the recovery neuron only ever receives R − L, which is clipped at zero. I confirmed this by simulation. The Fig. 6c gating neurons do not appear in the 8 × 8 matrix, so the Methods may be underspecified here.
   - Under the per-unit-time noise reading, even unperturbed runs end on the wrong side 45 to 49% of the time, so that reading tells us nothing about recovery.
6. [could affect a conclusion] Cell 52, `modes_for`. Modes 2 and 3 and the lick right and lick left mean responses use correct and error trials; the claims file says correct trials. Modes 1 to 5 fall short by small margins (97.6 against ≥ 98.0, 94.3 against ≥ 94.6), so this could move ed8a.
7. [does not affect a conclusion] `alm3.population_session` drops a session only when a trial group has fewer than 5 trials, so it keeps groups of exactly 5. M6 says more than 5. The session count still matches (16).
8. [does not affect a conclusion] Cell 8. In four sessions the pyramidal rate after laser onset is 0.71 to 2.18 times the rate before, i.e. no silencing. These sessions are flagged but kept in every analysis without investigation, and probably drive the low VGAT exp2b reduction (0.75).
9. [does not affect a conclusion] Cell 62. The exp3 and exp2b sessions have lick traces that show licks, but ed9f was not run on them. It was run on callosotomy sessions instead, which are outside the claim; there it gives r = −0.025, p = 0.66, no relationship.
10. [does not affect a conclusion] fig3-cd-roc and ed8 pass on 2 of 16 and 3 of 32 readings, at the edges of tolerance. These are fragile passes, not robust agreement.
11. [does not affect a conclusion] I tested `recovery_time`, `boundary`, `auc`, `binned_window` and `lda_direction` on synthetic inputs, and all behave correctly. Laser timings in cell 7 match the onsets and offsets the notebook uses.
12. [does not affect a conclusion] The notebook takes method details from the authors' MATLAB scripts in the archive (e.g. the 1.3 s response epoch, the 5 or 10 screening trials). It says so, and each one sits within, or is shown alongside, the claims file's readings.
13. Possible misreadings in the claims file (reported, not corrected):
    - (i) ed2e: the criterion turns "a low level of sustained inhibition in a larger proportion" into a count of neurons suppressed at p < 0.01. Low-level inhibition need not reach per-neuron significance, and this decides the outcome.
    - (ii) The ED Fig. 2b legend gives Exp 3 n = 52, 52, 102. The 102 suggests the bilateral 1-spot neurons from the exp2b sessions were pooled into the paper's Exp 3. The claims file and the notebook use the exp3 sessions only, which bears on ed7 and ed7e.
    - (iii) ED Fig. 2b and ED Fig. 4 say Exp 1 used 6 mice. The data hold 4 unilateral mice, and neither the claims file nor the notebook mentions this.

**C. Blocked claims and what I could not check**

Blocked claims, checked against the archive's file list (224 keys) and the FAQ:
- **fig1d-late-delay, ed2d, ed5:** nothing in the archive can test them.
- **ed3:** the part on 0.5 s photoinhibition ending 0.8 s and 1.6 s before the cue can be tested with the recording sessions. Cell 37 already has it: p = 0.23 and 0.81, no significant effect. The 1.3 s photoinhibition and the condition ending at the cue are missing.
- **ed9f:** the 4 exp3 population sessions (and the exp2b sessions) have lick traces that show licks, so part could be tested.

What I could not check, and the output that would settle it:
- **ed10e:** whether 496 follows from a width-based class, because cell 12's width counts were not printed for the callosotomy units.
- **fig1g and ed7 neuron counts:** where the extra neurons come from. A count of neurons removed at each selection step would show it.
- **ed4:** whether the result is caused by the window problem (item 2). Re-running with the window starting at offset + 0.1 s, or with 400 ms end-stamped windows, would settle it.
- **fig2:** the control and ipsilateral selectivity traces at a few time points, and the two M4 readings that were never run.
- **ed2b:** the result with the four non-silenced sessions excluded, and the neuron counts against the legend's (117, 110, 109; 300, 294, 301; 52, 52, 102).
- **ed9f:** the `ts_channels` of the Exp 2 sessions, to confirm no other lick channel exists, and the test run on the exp3 sessions.
- **fig6:** the bilateral attractor run long enough to settle (e.g. 4 s), and the share of runs ending at each fixed point.

## End of run

23 turns, 7 minutes, $2.70 at API prices, result: success.
