# 001326 · verifier-1 · run 41392281479

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 440
drwxr-xr-x 6 runner runner    4096 Nov  2 05:21 .
drwxr-xr-x 7 runner runner    4096 Nov  2 05:21 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 05:08 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 05:08 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  2 05:21 .claude
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env.development
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env.local
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env.production
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env.test
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .env.test.local
drwx------ 2 runner runner    4096 Nov  2 05:21 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 05:08 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 05:08 .github
-rw-r--r-- 1 runner runner       0 Nov  2 05:21 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 05:08 .idea
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1126-science.adt3971.yaml
```

```
<persisted-output>
Output too large (75.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/0fb545f1-2b5a-4c9d-81e9-ba88626aba43/tool-results/b5sq31blp.txt

Preview (first 2KB):
# Claims for Kauvar, Richman, Liu et al. (2025), Science 388, eadt3971, on dandiset 001326.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 (docs/protocol.md), Reader section.
#
# Text read: the accepted author manuscript as served by Europe PMC (PMC12286656, NIHMS2090574),
# main text and Materials and Methods, with its two supplements from the PMC Open Access set: the
# Supplementary Materials PDF (Supplemental Note 1, figs. S1 to S38, tables S1 to S3, the last being
# the summary of statistical analyses) and the MDAR checklist. Not the version of record. Figures
# were not opened; every number below is from the text, the legends or table S3.
#
# Code read:
# - Mouse electrophysiology and recorded-session behavior, the paper's ref. 103 at Zenodo
#   doi:10.5281/zenodo.14876694 (published 2025-02-15), a single file analysis.py (md5
#   6cc7aa5059737c3bd753aad1f116019d). It holds the analysis functions (unit selection, Leiden
#   clustering, regional rise and decay, emotion-like and coding dimensions, timescales, coupling,
#   the first-order model) but not the driver that calls them, so the list of excluded sessions,
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/0fb545f1-2b5a-4c9d-81e9-ba88626aba43/tool-results/b5sq31blp.txt"
}
```

```
1	# Claims for Kauvar, Richman, Liu et al. (2025), Science 388, eadt3971, on dandiset 001326.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
3	# pilot-10 (docs/protocol.md), Reader section.
4	#
5	# Text read: the accepted author manuscript as served by Europe PMC (PMC12286656, NIHMS2090574),
6	# main text and Materials and Methods, with its two supplements from the PMC Open Access set: the
7	# Supplementary Materials PDF (Supplemental Note 1, figs. S1 to S38, tables S1 to S3, the last being
8	# the summary of statistical analyses) and the MDAR checklist. Not the version of record. Figures
9	# were not opened; every number below is from the text, the legends or table S3.
10	#
11	# Code read:
12	# - Mouse electrophysiology and recorded-session behavior, the paper's ref. 103 at Zenodo
13	#   doi:10.5281/zenodo.14876694 (published 2025-02-15), a single file analysis.py (md5
14	#   6cc7aa5059737c3bd753aad1f116019d). It holds the analysis functions (unit selection, Leiden
15	#   clustering, regional rise and decay, emotion-like and coding dimensions, timescales, coupling,
16	#   the first-order model) but not the driver that calls them, so the list of excluded sessions,
17	#   the loading of z-scored rates and some window alignments are not in it.
18	# - brainwide-npix (refs. 17, 94), github.com/erichamc/brainwide-npix at commit 97cdf58 (tag v0.1,
19	#   Zenodo doi:10.5281/zenodo.14768678): loading, unit quality masks, binned firing rates with a
20	#   causal moving average.
[... 965 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/0fb545f1-2b5a-4c9d-81e9-ba88626aba43/tool-results/b5sq31blp.txt",
 "offset": 985
}
```

```
985	  criterion: Sessions. 11 sessions from 9 mice; the paper does not name the excluded animal, so
986	    each mouse with more than one session whose removal leaves 11 sessions from 9 mice is a
987	    reading, and the outcome must hold under all of them. Dimension (Methods, Emotion-like neural
988	    dimension, and analysis.py get_affective_projections), per session from puff-modulated units
989	    (sessions with at least 20). Target window is the 1 s starting 5 s after the last puff onset
990	    (Methods); the code's window falls 3 to 4 s after it (bins 400 to 500 of a post-series window
991	    that its plotting places 1 s before the last puff), shown as a variant. Reference is the 750
992	    ms ending 250 ms before the first puff. Weights are mean differences normalized by per-unit
993	    variance (Methods; the code divides by the variance pooled over all units, a variant), made
994	    orthogonal by QR to an eye-reflex dimension from the last four puffs (200 ms after against 200
995	    ms before onset), signed so that puff 8 exceeds puff 1 (code). Projections are baseline-
996	    subtracted per series with the 250 ms before the first puff. Reproduced when, for Pre, the 95%
997	    interval across sessions (1.96 s.e.m., table S3) of the mean projection in the 250 ms before
998	    puff 8 is above zero and higher than before puff 2, the projection 10 to 11 s after the last
999	    puff onset is still above zero and the last 5 s of the 45 s shown after the series include
1000	    zero; and, for Ketamine (series 23 to 32), the interval before puff 8 includes zero or lies
1001	    below the Pre mean.
1002	- id: fig5e-late-reduced
1003	  statement: On the first puff of a series, late emotion-like activity (2 to 3 s after onset) was
1004	    reduced by ketamine (0.546 to 0.005).
[... 453 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
for fn in ['reproduce_kauvar_2025.ipynb','reproduce_kauvar_2025_behavior.ipynb']:
    nb=json.load(open(fn))
    out=[]
    for i,c in enumerate(nb['cells']):
        out.append(f"\n===== CELL {i} [{c['cell_type']}] =====\n"+''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: out.append("--- out:\n"+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: out.append("--- out(data):\n"+''.join(d['text/plain']))
            elif o.get('output_type')=='error': out.append("--- ERR: "+o['ename']+' '+o['evalue'])
    open(fn+'.txt','w').write('\n'.join(out))
    print(fn,len(nb['cells']))
EOF
wc -l *.txt
```

```
reproduce_kauvar_2025.ipynb 57
reproduce_kauvar_2025_behavior.ipynb 38
  1931 reproduce_kauvar_2025.ipynb.txt
  1216 reproduce_kauvar_2025_behavior.ipynb.txt
  3147 total
```

**Agent calls Read**

```json
{
 "file_path": "reproduce_kauvar_2025.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Kauvar, Richman, Liu et al. (2025) on dandiset 001326
4	
5	- Paper: Kauvar, Richman, Liu et al., "Conserved brain-wide emergence of emotional response from sensory experience in humans and mice", Science 388, eadt3971 (2025), doi:10.1126/science.adt3971.
6	- Dataset: DANDI:001326, "Brain-wide mouse electrophysiology during aversive stimuli and ketamine", version 0.250528.1957 (doi:10.48324/dandi.001326/0.250528.1957), streamed from the archive.
7	- Version. The paper cites the dandiset without a version. 0.250528.1957 is its only published version; the draft holds the same 13 assets (same asset ids), so the most recent published version is pinned.
8	- Claims file: `claims/001326/10.1126-science.adt3971.yaml`, written from the accepted author manuscript (Europe PMC, PMC12286656) with its supplementary materials, and the paper's code (analysis.py, Zenodo doi:10.5281/zenodo.14876694; brainwide-npix at commit 97cdf58).
9	- Outside input: the Allen CCFv3 2017 structure tree (`structure_tree_safe_2017.csv`, the file brainwide-npix loads), from github.com/cortex-lab/allenCCF at commit e5a57fe7, used only to place the dataset's region acronyms in the Allen hierarchy.
10	
11	The dandiset holds the mouse Neuropixels recordings (13 sessions, 10 mice). The human data, the behavior-only mouse experiments and the eye closure of the recorded mice are in DANDI:001347; the claims on them that the data allow are tested in `reproduce_kauvar_2025_behavior.ipynb`.
12	
13	
14	| Claim | In this notebook |
15	|---|---|
16	| `fig1e-human-ketamine-late-closure` | tested in reproduce_kauvar_2025_behavior.ipynb (DANDI:001347) |
17	| `figs1b-human-early-closure-unchanged` | tested in reproduce_kauvar_2025_behavior.ipynb (DANDI:001347) |
18	| `fig1f-human-reports` | not tested (see the attempt record) |
19	| `fig2d-cadss-ketamine` | not tested (see the attempt record) |
20	| `fig2g-six-factors` | not tested (see the attempt record) |
[... 644 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kauvar.py"
}
```

```
1	"""Loading and measures for dandiset 001326 (Kauvar, Richman, Liu et al. 2025, Science 388, eadt3971).
2	
3	The dandiset holds the mouse Neuropixels sessions of the paper: per session, curated single units
4	(spike times, Allen CCFv3 acronym, SNR, spike count), the onsets of eyepuffs, tones and lights in
5	the table "Stimulus presentations", and the time of the ketamine infusion. Files are streamed from
6	the archive at the pinned version; nothing is written to disk.
7	
8	Where each parameter comes from:
9	
10	- Rates. "Firing rates were binned at 10 ms resolution and smoothed with a causal moving average
11	  filter over 50 ms" (Methods, Neuropixels recording and processing). Rates are in Hz as in
12	  brainwide-npix (refs. 17, 94) `firing_rates_over_recording` (count / 0.01 s), with its causal
13	  `moving_avg_filter` (first 4 bins left unsmoothed), then z-scored per unit over the session, as
14	  the paper's code works on session z-scored rates (claims file, opening comment).
15	- Peri-stimulus windows. -1 to 2 s around each onset, starting at
16	  `searchsorted(bins, onset) - 100` (analysis.py, get_cell_clusters).
17	- Epochs. Pre is puff series 1 to 20, Ketamine series 23 to 32, Post series 35 to 40 (claims file,
18	  opening comment, from analysis.py); the onset of ketamine in the code is 30 s after the last
19	  puff of series 20 (analysis.py ket_start_ts).
20	- Puff-modulated units. analysis.py `selective` (p <= 0.01, paired t-tests over the 160 Pre
[... 563 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "reproduce_kauvar_2025.ipynb.txt",
 "offset": 665,
 "limit": 640
}
```

```
665	                 "median over regions of median rise change (s)": np.median(med_change),
666	                 "regions with Pre median rise < 0.1 s": int((pre_rise < 0.1).sum()),
667	                 "within one bin": abs(np.median(med_change)) <= 0.01 + 1e-9})
668	print(pd.DataFrame(rows).to_string(index=False))
669	main = rt[(1.3, "code >30", "ket 23-32")]
670	print(pd.DataFrame({r: {"n": o["n"], "peak d'": round(o["peak_dprime"], 2), "Pre rise": np.nanmedian(o["pre_rise"]),
671	                        "Ket rise": np.nanmedian(o["ket_rise"]), "Pre decay": np.nanmedian(o["pre_decay"]),
672	                        "Ket decay": np.nanmedian(o["ket_decay"])} for r, o in main.items()}).T.sort_values("Pre decay").to_string())
673	--- out:
674	 d' threshold  region rule ketamine series  regions  median over regions of median rise change (s)  regions with Pre median rise < 0.1 s  within one bin
675	          1.3     code >30       ket 23-32       35                                      -0.004537                                    30            True
676	          1.3     code >30       ket 22-32       35                                      -0.006857                                    30            True
677	          1.3 Methods >=30       ket 23-32       35                                      -0.004537                                    30            True
678	          1.3 Methods >=30       ket 22-32       35                                      -0.006857                                    30            True
679	          2.0     code >30       ket 23-32       31                                      -0.004537                                    28            True
680	          2.0     code >30       ket 22-32       31                                      -0.006857                                    28            True
681	          2.0 Methods >=30       ket 23-32       31                                      -0.004537                                    28            
[... 623 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "reproduce_kauvar_2025.ipynb.txt",
 "offset": 1305,
 "limit": 630
}
```

```
1305	without sub-1 methods       STR        10 0.226 [0.075, 0.377]            -0.007  0.042 [-0.027, 0.112]   True
1306	without sub-1 methods        TH         6 0.735 [0.331, 1.139]             0.320  0.002 [-0.164, 0.169]   True
1307	without sub-1 methods        HY         6 0.411 [0.153, 0.669]            -0.035 -0.004 [-0.078, 0.071]   True
1308	without sub-1 methods        MB         5 0.444 [0.166, 0.723]             0.179  0.020 [-0.133, 0.172]   True
1309	without sub-1    code Isocortex        10 0.720 [0.472, 0.967]             0.376 -0.103 [-0.241, 0.036]   True
1310	without sub-1    code       OLF         8 0.204 [0.048, 0.360]             0.164 -0.081 [-0.246, 0.083]   True
1311	without sub-1    code       HPF         4 0.251 [0.156, 0.347]             0.099  0.047 [-0.167, 0.261]   True
1312	without sub-1    code       STR        10 0.287 [0.121, 0.454]             0.157 -0.018 [-0.100, 0.065]   True
1313	without sub-1    code        TH         6 0.909 [0.512, 1.307]             0.439  0.052 [-0.122, 0.226]   True
1314	without sub-1    code        HY         6 0.551 [0.273, 0.829]             0.122 -0.027 [-0.154, 0.101]   True
1315	without sub-1    code        MB         5 0.500 [0.139, 0.861]             0.193  0.036 [-0.154, 0.227]   True
1316	without sub-3 methods Isocortex        10 0.641 [0.437, 0.844]             0.268 -0.074 [-0.223, 0.074]   True
1317	without sub-3 methods       OLF         6 0.262 [0.115, 0.409]             0.099 -0.036 [-0.214, 0.141]   True
1318	without sub-3 methods       HPF         5 0.208 [0.028, 0.388]             0.077  0.049 [-0.073, 0.171]   True
1319	without sub-3 methods       STR         9 0.280 [0.116, 0.443]            -0.009 -0.020 [-0.085, 0.046]   True
1320	without sub-3 methods        TH         7 0.723 [0.368, 1.077]             0.334 -0.134 [-0.328, 0.060]   True
1321	without sub-3 methods        HY         7 0.381 [0.147, 0.615]            -0.054 -0.014 [-0.081, 0.053]   True
1322	without sub-3 methods  
[... 610 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "reproduce_kauvar_2025_behavior.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Reproducing the behavior of Kauvar, Richman, Liu et al. (2025) from dandiset 001347
4	
5	Paper. Kauvar IV, Richman EB, Liu TX, et al. (2025). Conserved brain-wide emergence of emotional
6	response from sensory experience in humans and mice. Science 388, eadt3971.
7	[doi:10.1126/science.adt3971](https://doi.org/10.1126/science.adt3971). The claims file
8	(`claims/001326/10.1126-science.adt3971.yaml`) was written from the full text with its supplement
9	(table S3).
10	
11	Dataset. [DANDI:001347](https://dandiarchive.org/dandiset/001347/0.250528.0702), version
12	0.250528.0702. The paper's data statement points to this dandiset for the human and mouse behavior
13	without naming a version; 0.250528.0702 is its only published version, so it is pinned. The mouse
14	Neuropixels sessions are in dandiset 001326 and are tested in the entry's other notebook; this
15	notebook reads 001326 (version 0.250528.1957) only for the stimulus tables, to link the recorded
16	mice's eye closure files to those sessions.
17	
18	What 001347 holds that is used here. The eye closure traces of the behavior-rig mice
19	(`sub-mouse`, one file per experiment id), the eye closure of the ten Neuropixels-recorded mice
20	(`sub-m<mouse>-<rec>`), and the per-trial eye closure of the four non-implanted participants
[... 563 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "reproduce_kauvar_2025_behavior.ipynb.txt",
 "offset": 584,
 "limit": 640
}
```

```
584	Methods (Pre 1-20, Ket 22-32), both divided by the Pre maximum, exclude sub-5 (no file; 10 sessions):
585	   Pre accumulation 0.200 [0.122, 0.279] (ddof=1: [0.117, 0.283]) n=10
586	   Ketamine accumulation 0.123 [0.042, 0.204] (ddof=1: [0.037, 0.208]) n=10
587	   Ketamine interval includes 0: False; lies below the Pre mean (0.200): False
588	
589	Methods (Pre 1-20, Ket 22-32), both divided by the Pre maximum, exclude sub-1 (8 sessions):
590	   Pre accumulation 0.167 [0.083, 0.252] (ddof=1: [0.077, 0.257]) n=8
591	   Ketamine accumulation 0.129 [0.043, 0.215] (ddof=1: [0.037, 0.221]) n=8
592	   Ketamine interval includes 0: False; lies below the Pre mean (0.167): False
593	
594	Methods (Pre 1-20, Ket 22-32), both divided by the Pre maximum, exclude sub-3 (9 sessions):
595	   Pre accumulation 0.202 [0.115, 0.290] (ddof=1: [0.110, 0.295]) n=9
596	   Ketamine accumulation 0.136 [0.050, 0.222] (ddof=1: [0.044, 0.227]) n=9
597	   Ketamine interval includes 0: False; lies below the Pre mean (0.202): False
598	
599	file ranges (Pre 1-20, Ket 23-30), raw, exclude sub-5 (no file; 10 sessions):
600	   Pre accumulation 0.058 [0.031, 0.085] (ddof=1: [0.030, 0.086]) n=10
601	   Ketamine accumulation 0.046 [0.017, 0.076] (ddof=1: [0.015, 0.077]) n=10
602	   Ketamine interval includes 0: False; lies below the Pre mean (0.058): False
603	
[... 614 more lines not kept]
```

**Agent**

Both notebooks are read. Next I'll query the DANDI API for the claims the notebook didn't test, and run quick synthetic checks on the helpers.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001347/versions/0.250528.0702/assets/?page_size=300" -o a1347.json; curl -s "https://api.dandiarchive.org/api/dandisets/001326/versions/0.250528.1957/assets/?page_size=300" -o a1326.json; python3 - <<'EOF'
import json,collections
for f in ['a1326.json','a1347.json']:
    d=json.load(open(f)); print(f, d.get('count'))
    rs=d['results']
    if f=='a1326.json':
        for r in rs: print(r['path'], round(r['size']/1e9,2),'GB')
    else:
        c=collections.defaultdict(list)
        for r in rs:
            if r['path'].startswith('sub-mouse'): continue
            print(r['path'], round(r['size']/1e6,1),'MB')
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json,urllib.request
d=json.load(open('a1347.json'))
tot=sum(r['size'] for r in d['results']); print('total GB',tot/1e9)
for r in d['results']:
    if r['path'].startswith('sub-H/') or 'SD211_ses-puff_behavior' in r['path']:
        m=json.load(urllib.request.urlopen(f"https://api.dandiarchive.org/api/dandisets/001347/versions/0.250528.0702/assets/{r['asset_id']}/"))
        print(r['path'], [v.get('value') for v in m.get('variableMeasured',[])], (m.get('description') or '')[:300])
v=json.load(urllib.request.urlopen("https://api.dandiarchive.org/api/dandisets/001347/versions/0.250528.0702/"))
print(v.get('description','')[:2000])
EOF
```

```
total GB 16.035455232
sub-H/sub-H_ses-ketChangePermutationClusterTest.nwb [] 
sub-H/sub-H_ses-sgramNMFLoadings.nwb [] 
sub-H/sub-H_ses-sgramNMFFactors.nwb [] 
sub-H/sub-H_ses-sgramPerChannel.nwb [] 
sub-H/sub-H_ses-sgramPerYeoPerTrial.nwb [] 
sub-H/sub-H_ses-sgramPerRegionPerTrial.nwb [] 
sub-SD211/sub-SD211_ses-puff_behavior.nwb [] 
sub-H/sub-H_ses-sgramPerChannelPerTrial.nwb [] 
Brain-wide human electrophysiology associated with Kauvar*, Richman*, Liu* et al Science (2025). 

Regarding data folders, subjects with prefix "SD" indicate iEEG human participants, "h" indicate non-iEEG eyepuff human participants, and "m" indicate mice. Notably, "H" and "mouse" folders include cross-participant aggregated data.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  grep -n "acquisition\|keys\|def \|assert" behavior.py | head -80
```

```
7:  (`acquisition/eye_closure`, 200 Hz), with no condition label. Trials are 16200 frames (81 s), the
150:def asset_urls(dandiset=DANDISET, version=VERSION):
159:def _open(url):
163:def _pmap(fn, items, workers=16):
170:def load_mouse(ids, urls, max_frames=None):
172:    def one(i):
174:        ts = f["acquisition/eye_closure"]
185:def by_trial(trace, ntrials, prox=True):
193:def win(tpuff, w, fps=FPS, t_first=T_FIRST):
199:def puff_measures(trials, puff):
208:def condition_table(data, conds, puff):
220:def paired(df, cond_a, phase_a, cond_b, phase_b, metric):
228:def fdr(p):
232:def mean_sem(x):
239:def survival_times(trace, ntrials, trials, fps=FPS):
253:def km_median(times, events):
270:def load_npx(urls):
272:    keys = ["fps", "ket_trial", "ket_puff", "w_pre", "w_post", "led_delay", "npuffs_per_trial"]
274:    def one(name):
276:        A = f["acquisition"]
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "behavior.py",
 "offset": 1,
 "limit": 480
}
```

```
1	"""Loading and measures for the behavior of Kauvar, Richman, Liu et al. 2025 (Science 388, eadt3971)
2	deposited in dandiset 001347, version 0.250528.0702.
3	
4	The dandiset holds three kinds of behavioral file used here:
5	
6	- `sub-mouse/sub-mouse_ses-<id>_behavior.nwb`: one eye closure trace per behavior-rig experiment
7	  (`acquisition/eye_closure`, 200 Hz), with no condition label. Trials are 16200 frames (81 s), the
8	  first puff of a trial 6 s after its start, eight puffs 3 s apart (mouse_eyepuff code below). The
9	  experiment ids per condition come from the paper's code, Zenodo doi:10.5281/zenodo.14920570
10	  (`EXPERIMENTS` below, with the file and line of each list).
11	- `sub-m<mouse>-<rec>/..._ses-puff_behavior.nwb`: eye closure of the Neuropixels-recorded mice
12	  (100 Hz), with the onset of each puff series (`events-on`, frames), `ket_trial`,
13	  `trial_range_preket`, `trial_range_ket` and per-trial and per-puff cut-outs.
14	- `sub-h0xx/sub-h0xx_ses-P50_behavior.nwb`: per-trial eye closure (800 samples) of the four
15	  non-implanted human participants, `pre_trials_data` and `post_trials_data`, 40 trials each, and
16	  the time axis `time_reference/tt`.
17	
18	Where each parameter comes from (Zenodo code paths are relative to kauvar-richman-liu-2025_zenodo/):
19	
20	- Session lists per condition (`EXPERIMENTS`): mouse_eyepuff/scripts/fig1_drugs.py:23-30 (saline,
[... 443 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' 2>&1 | grep -v Warn
import numpy as np, kauvar as K
print("int(47/BIN)", int(47/K.BIN), len(K._inputs), K._cut(K.model_system(1,1,1)).shape)
rng=np.random.default_rng(0)
# AR(1) timescale recovery, 30 s at 10 ms, with and without mean offset
for tau in (0.1,0.3,0.5):
    a=np.exp(-K.BIN/tau); est=[];est_off=[]
    for r in range(20):
        x=np.zeros(3000); e=rng.standard_normal(3000)
        for i in range(1,3000): x[i]=a*x[i-1]+e[i]
        est.append(K.extract_timescale(x)); est_off.append(K.extract_timescale(x+2*x.std()))
    print(f"tau {tau}: est median {np.nanmedian(est):.3f} range {np.nanmin(est):.3f}-{np.nanmax(est):.3f}; with offset {np.nanmedian(est_off):.3f} max {np.nanmax(est_off):.2f}")
for s in ["VPMpc","ORBvl2/3","CA1","CA3","PL1","SSp-bfd4","NLOT2","ACAd6a","RSPagl1","DG-mo","MOs5"]:
    print(s,"->",K.reduce_region(s), end="; ")
print()
# cd_weights sanity
x=rng.standard_normal((3,20)); x[0]+=2; y=rng.standard_normal((3,20))
print("cd unit",K.cd_weights(x,y).round(3), "pooled", K.cd_weights(x,y,'pooled').round(3))
# selective: unit with response at 0-200ms only
r=rng.standard_normal((4,20,8,300)); r[0,:,:,100:120]+=1.0; r[1,:,7,100:200]+=0.8
m,t=K.selective(r); print("selective",m,{k:v.tolist() for k,v in t.items()})
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls executed/001326-kauvar-2025/.venv/bin/python 2>&1; which -a python3 python; ls ~/.local/bin 2>/dev/null | head; uv --version 2>&1
```

```
ls: cannot access 'executed/001326-kauvar-2025/.venv/bin/python': No such file or directory
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
uv 0.13.6 (x86_64-unknown-linux-gnu)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && VIRTUAL_ENV=$TMPDIR/v uv pip install -q numpy scipy pandas h5py remfile 2>&1 | tail -2; $TMPDIR/v/bin/python -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"
```

```
2.5.4 1.18.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF' 2>&1 | grep -v Warn
import numpy as np, kauvar as K
print("int(47/BIN)", int(47/K.BIN), len(K._inputs), K._cut(K.model_system(1,1,1)).shape)
rng=np.random.default_rng(0)
for tau in (0.1,0.3,0.5):
    a=np.exp(-K.BIN/tau); est=[];est_off=[]
    for r in range(20):
        x=np.zeros(3000); e=rng.standard_normal(3000)
        for i in range(1,3000): x[i]=a*x[i-1]+e[i]
        est.append(K.extract_timescale(x)); est_off.append(K.extract_timescale(x+2*x.std()))
    print(f"tau {tau}: est median {np.nanmedian(est):.3f} range {np.nanmin(est):.3f}-{np.nanmax(est):.3f}; with offset median {np.nanmedian(est_off):.3f} max {np.nanmax(est_off):.2f}")
for s in ["VPMpc","ORBvl2/3","CA1","CA3","PL1","SSp-bfd4","NLOT2","ACAd6a","RSPagl1","DG-mo","MOs5"]:
    print(s,"->",K.reduce_region(s), end="; ")
print()
x=rng.standard_normal((3,20)); x[0]+=2; y=rng.standard_normal((3,20))
print("cd unit",K.cd_weights(x,y).round(3), "pooled", K.cd_weights(x,y,'pooled').round(3))
r=rng.standard_normal((4,20,8,300)); r[0,:,:,100:120]+=1.0; r[1,:,7,100:200]+=0.8
m,t=K.selective(r); print("selective",m,{k:v.tolist() for k,v in t.items()})
EOF
```

```
int(47/BIN) 4700 7100 (6825,)
tau 0.1: est median 0.114 range 0.078-0.166; with offset median 0.278 max 0.81
tau 0.3: est median 0.342 range 0.206-0.546; with offset median 0.501 max 0.89
tau 0.5: est median 0.495 range 0.208-1.084; with offset median 0.725 max 1.77
VPMpc -> VPM; ORBvl2/3 -> ORBvl; CA1 -> CA1; CA3 -> CA3; PL1 -> PL; SSp-bfd4 -> SSp-bfd4; NLOT2 -> NLOT2; ACAd6a -> ACAd; RSPagl1 -> RSPagl; DG-mo -> DG-mo; MOs5 -> MOs; 
cd unit [ 0.988  0.108 -0.11 ] pooled [ 0.989  0.105 -0.105]
selective [ True  True False False] {'pre vs 0-200 ms': [True, True, False, False], 'pre vs 300-800 ms': [False, True, False, False], 'pre vs 1-2 s': [False, False, False, False], 'baseline first vs last puff': [False, False, False, False], 'response first vs last puff': [False, True, False, False]}
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np
BIN=0.01
def dprime_abs(p):
    bm = p[..., :100].mean((-1, -2)); bs = np.nanstd(p[..., :100].reshape(p.shape[:-2] + (-1,)), -1)
    rm = p.mean(-2); rs = np.nanstd(p, -2)
    return np.abs(rm - bm[..., None]) / np.sqrt(0.5 * (bs[..., None] ** 2 + rs ** 2))
def rise_decay(p, thr=0.25):
    d = dprime_abs(p); d = d - d[..., :100].mean(-1, keepdims=True); d = d / d.max(-1, keepdims=True)
    post = d[..., 100:]; pk = post.argmax(-1); above = post > thr
    rise = np.where(above.any(-1), above.argmax(-1) * BIN, np.nan)
    idx = np.arange(post.shape[-1]); after = (post < thr) & (idx >= pk[..., None])
    decay = np.where(after.any(-1), after.argmax(-1) * BIN, np.nan)
    bad = pk > 75; rise[bad] = np.nan; decay[bad] = np.nan
    return rise, decay
rng=np.random.default_rng(1)
t=np.arange(300)*BIN-1
for amp in (0.3,0.6,1.0):
  for tau in (0.3,0.6):
    sig=np.where(t>=0, amp*np.exp(-np.clip(t,0,None)/tau)*(1-np.exp(-np.clip(t,0,None)/0.03)),0)
    out={}
    for nt in (40,20):
        data=sig+rng.standard_normal((nt,300))*1.0  # trial-level noise (cell-averaged)
        ix=rng.integers(0,nt,(1000,nt))
        r,d=rise_decay(data[ix])
        out[nt]=(np.nanmedian(d), np.isnan(d).mean())
    print(f"amp {amp} tau {tau}: decay median 40 trials {out[40][0]:.3f} (nan {out[40][1]:.2f}), 20 trials {out[20][0]:.3f} (nan {out[20][1]:.2f})")
EOF
```

```
amp 0.3 tau 0.3: decay median 40 trials 0.220 (nan 0.43), 20 trials 0.200 (nan 0.21)
amp 0.3 tau 0.6: decay median 40 trials 0.090 (nan 0.16), 20 trials 0.190 (nan 0.65)
amp 0.6 tau 0.3: decay median 40 trials 0.170 (nan 0.13), 20 trials 0.100 (nan 0.08)
amp 0.6 tau 0.6: decay median 40 trials 0.220 (nan 0.01), 20 trials 0.420 (nan 0.02)
amp 1.0 tau 0.3: decay median 40 trials 0.180 (nan 0.00), 20 trials 0.200 (nan 0.02)
amp 1.0 tau 0.6: decay median 40 trials 0.220 (nan 0.00), 20 trials 0.270 (nan 0.01)
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.1126-science.adt3971.yaml; grep "^- id:" 10.1126-science.adt3971.yaml | awk '{print $3}' | tr '\n' ' '
```

```
54
fig1e-human-ketamine-late-closure figs1b-human-early-closure-unchanged fig1f-human-reports fig2d-cadss-ketamine fig2g-six-factors fig2i-factors-1-2-ketamine fig3b-cluster-test-networks figs12-erp-not-blink figs14g-cadss-correlation fig6c-human-persistent fig6e-human-fast-unchanged fig6g-human-timescale fig6i-human-phase-locking fig1k-mouse-ketamine-late-closure fig1l-dissociatives-preinfusion figs2bc-mouse-early-late fig1m-accumulation-persistence figs2g-scaling-puff-number figs2h-dose-response fig1p-anesthesia-abolishes-both figs5-other-drugs figs6-vpm-muscimol figs4-reward-licking fig5hi-behavior-model-doses fig4-recordings-scale fig4b-recorded-eye-closure-ketamine fig5b-recorded-accumulation fig4de-response-clusters figs31b-cluster-overrepresentation fig4g-ketamine-alters-slow-clusters fig4i-rise-times-unchanged fig4h-decay-shortened fig4h-decay-anatomical-progression fig5d-emotion-dimension-accumulates fig5e-late-reduced fig5e-rapid-unchanged fig5g-tau-persist-model figs33-alternative-models figs32c-regional-emotion-dimension fig6b-persistent-dimension-distributed fig6d-mouse-persistent fig6f-mouse-fast-unchanged fig6h-mouse-timescale fig6j-mouse-coupling figs34c-tone-no-eye-closure figs34d-tone-fast-unchanged figs34e-tone-persistent figs34f-tone-shorter-than-puff figs34g-tone-timescale figs34h-tone-coupling figs30-correlation-structure figs29-rsp-oscillations link-001347-condition-labels link-001347-recorded-sessions
```

**Agent calls Bash**

```bash
cd paper; grep -n -o -i ".\{200\}emotion-like neural dimension.\{600\}" 10.1126-science.adt3971.txt | head -5; grep -n -o -i ".\{100\}10 minutes.\{200\}" 10.1126-science.adt3971.txt | head; grep -n -o -i ".\{150\}trials 22.\{200\}" 10.1126-science.adt3971.txt | head -3
```

```
7:ecay lasting tens of seconds following each eyepuff series before returning to baseline ( Fig. 5D ). The neurons contributing to this dimension exhibited broad spatial distribution ( fig. S32 ). This emotion-like neural dimension did not accumulate on ketamine ( Fig. 5D ), even though we observed transient increases along this dimension in response to each eyepuff ( Fig. 5 , D and E ). These transient increases on ketamine were not different from those prior to ketamine, whereas late changes along the emotion-like dimension (seconds after each eyepuff) were reduced ( Fig. 5E ). Fig. 5. Mouse eyepuff-triggered neural activity accumulates to a persistent state with first order system dynamics. ( A ) Eyepuff protocol during neural recording. Each trial consists of a series of eight regularly spaced puffs, with twenty tri
7:ely varying the model’s decay timescale, τ PERSIST , could capture the effects of ketamine on eyepuff-triggered emotional dynamics, and we therefore fit the parameters of the model to activity in the emotion-like neural dimension before and during ketamine infusion. Despite only varying the single parameter τ PERSIST across preinfusion and ketamine conditions, we observed a close match between the model and the experimental data ( Fig. 5G ). Fitting an alternative single-phase model (in which τ BROADCAST tracks equally with τ PERSIST ) resulted in symmetric rise and decay dynamics and did not fit the neural data ( fig. S33A ); other alternative models in which ketamine modulated the input scale S or the broadcast rate τ BROADCAST instead of τ PERSIST also did not fit the data well, failing to capture the peri-puff emo
7:y repeatedly sampling with replacement from the set of puff replicates in a given region. Regional rise and decay times were visualized by sorting regions by their time to decay ( Fig. 4 , H and I ). Emotion-like neural dimension. Simultaneously recorded neurons were analyzed for their firing rate activity along a neural dimension (
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -o -i "Regional correlation analysis.\{700\}" 10.1126-science.adt3971.txt | head -2; grep -n -o -i ".\{300\}Harderian.\{100\}" 10.1126-science.adt3971.txt | head -2
```

```
7:Regional correlation analysis. Pairwise Pearson correlation coefficients were quantified between individual units during the entirety of the pre-infusion period and during a 10-minute period following the onset of ketamine infusion. For visualization ( fig. S30 ), units were grouped by anatomical region assignment and further sorted by anatomical depth along the probe insertion trajectory. Significant modulation. Some analyses were restricted to neurons whose firing rates were significantly modulated by the air puff presentation. Significant modulation was defined by an uncorrected P-value of less than 0.01 in paired T-tests comparing average firing rates in any of the following windows: 1 s prepuff, 200 ms post puff; 1
7:e baseline corresponds to the pre-trial baseline eye closure averaged across the first two trials (when the eye should be fully open). For experiments with neural recording, in which the mice can be more stressed and there can be more variation in the eye closure across trials (including occasional Harderian secretion), DeepLabCut was used to precisely extract the eye size at each time point (using the sam
7: brainwide-npix python package ( 17 , 94 ) ( https://github.com/erichamc/brainwide-npix ). Firing rates were binned at 10 ms resolution and smoothed with a causal moving average filter over 50 ms. For cross-puff and population analyses, we excluded one animal that exhibited notable stress response (Harderian gland secretion) during the pre-ketamine epoch. Anatomical referencing. Following recordings, mice
```

**Agent**

**A. Outcomes** (54 claims in the claims file: 40 tested across the two notebooks, 14 not tested)

| Claim | My outcome | Reason |
|---|---|---|
| fig1e-human-ketamine-late-closure | reproduced | Saline 0.706, ketamine 0.426, both within tolerance; t = 3.703, p = 0.0342, the same as table S3 (behavior cell 35). |
| figs1b-human-early-closure-unchanged | reproduced | 0.839 against 0.777, p = 0.2032 ≥ 0.05 (behavior cell 37). |
| fig1k-mouse-ketamine-late-closure | reproduced | 0.262 against −0.068, t = 4.737, p = 0.009 (cell 14). |
| fig1l-dissociatives-preinfusion | reproduced | All six means within tolerance; corrected p 0.504, 0.002, 0.041, the same as the paper (cell 16). |
| figs2bc-mouse-early-late | reproduced | t = 6.854 and 4.951, the same as the paper. All values within tolerance, though late saline is 0.203 against 0.34 ± 0.14, just inside (cell 18). |
| fig1m-accumulation-persistence | partially_reproduced | Accumulation holds (puff 8: 0.517 against puff 1: 0.244, intervals do not overlap). Kaplan-Meier median is 13.05 s on the criterion's 100 preinfusion trials, outside 15.16 ± 1.5. It is within only on the code's 200 trials, which include infusion trials (cell 20). |
| figs2g-scaling-puff-number | reproduced | Puff 1 vs 8 corrected p 0.0038, 0.0001, 0.0000; pressure comparisons p ≥ 0.46; all six means within tolerance (cell 22). |
| figs2h-dose-response | reproduced | Under both FDR families, ketamine 35/50 and PCP 10/20 have q < 0.05 and every lower dose q ≥ 0.05 (PCP 5: 0.110 / 0.0735). Expected values within (cell 24). |
| fig1p-anesthesia-abolishes-both | reproduced | K/X q = 0.006 and 0.0016. All six values within tolerance, including ketamine reflexive 0.436 and PCP 0.428 (cell 26). |
| figs5-other-drugs | reproduced | q: ketamine 0.0053, PCP 0.0092, buprenorphine 0.934, diazepam 0.304, the same as table S3 (cell 28). |
| figs6-vpm-muscimol | reproduced | 0.602 against 0.105, both corrected p = 0.0289, the same as the paper; 0–40 ms closure unchanged (cell 30). |
| fig5hi-behavior-model-doses | reproduced | Variance explained 0.917 (ketamine) and 0.886 (PCP); τP falls at every dose step. The data assembly is an assumption the notebook states, and the ketamine τB sits at its 100 s bound (cell 32). |
| fig4b-recorded-eye-closure-ketamine | partially_reproduced | Without normalization, Pre − Ket = 0.026 [−0.030, 0.082]. With each condition divided by its own maximum it is 0.308 [0.243, 0.373]; divided by the Pre maximum it is −0.033. Only 10 of the 13 sessions are in 001347 (behavior cell 6). |
| fig5b-recorded-accumulation | partially_reproduced | Pre accumulation is above 0 in every reading. Without normalization, Ketamine accumulation (0.040 [0.012, 0.067]) neither includes 0 nor lies below the Pre mean. It meets the criterion only under per-condition max normalization (cell 8). |
| figs34c-tone-no-eye-closure | reproduced | Upper bound of tone closure ≤ 0.006 in every split, below the puff value and below 0.1. Only 6 of the 7 sessions are available (cell 10). |
| fig4-recordings-scale | reproduced | 13 sessions, 10 mice; 6698 puff-modulated units (6491 with the spike-count reading), both within 6969 ± 697; median 32 regions per session (cell 6). |
| fig4de-response-clusters | not_reproduced | 11 clusters, which is within ±1, but 7 of the 12 sizes are outside tolerance and the 12th is missing. Only 1 cluster is persistent where the criterion needs 3 (cell 8). |
| figs31b-cluster-overrepresentation | partially_reproduced | At FDR 0.05: PAG in cluster 5 (fast), VPM in cluster 2 (5th fastest of 11), frontal regions in slow clusters. At 0.01, VPM is only in cluster 8 (slow half). Problem 6 makes even the 0.05 result fragile (cell 10). |
| fig4g-ketamine-alters-slow-clusters | not_reproduced | Spearman ρ = −0.023 (p = 0.95) for cosine distance and −0.018 (p = 0.96) for the 1–2 s difference (cell 12). |
| fig4i-rise-times-unchanged | reproduced | Median change in rise time is −0.005 or −0.007 s under all 8 readings, within one bin; Pre rise < 0.1 s in 30/35 and 28/31 regions (cell 14). |
| fig4h-decay-shortened | reproduced | Median bootstrap change −0.18 to −0.19 s; 33/35 and 31/31 regions shorter (cell 16). Problem 5 is an unchecked risk to this result. |
| fig4h-decay-anatomical-progression | reproduced | Frontal/limbic 0.488 / 0.532 against midbrain 0.311; VPM 0.541 and MD 0.590, both above the overall median 0.445 (cell 18). |
| fig5d-emotion-dimension-accumulates | partially_reproduced | Before puff 8 > 0 and > puff 2, 10–11 s after > 0, and Ketamine includes 0, in all 24 readings. But "last 5 s includes 0" fails in all 24 (e.g., 0.303 [0.203, 0.403]) (cell 32). |
| fig5e-late-reduced | partially_reproduced | Holds with the code's 3–4 s target window: q = 0.0056–0.040 under pooled variance and unit-vector scaling. Fails in every session reading with the Methods 5–6 s window and per-unit variance (q = 0.105–0.113) (cell 34). |
| fig5e-rapid-unchanged | partially_reproduced | q ≥ 0.05 with the Methods window. With the code window and per-unit variance, q = 0.023, 0.031, 0.048, so the absence fails (cell 36). |
| fig5g-tau-persist-model | reproduced | Variance explained 0.81–0.95 and Ketamine τP (0.12–0.38 s) far below Pre (20–34 s) in all 24 readings (cell 40). |
| figs33-alternative-models | partially_reproduced | τP model best in 22 of 24 readings; saturation is best for sub-3 with the code window and pooled variance, by 0.001–0.006. The variance explained is also computed on the wrong segment (problem 1) (cell 42). |
| figs32c-regional-emotion-dimension | partially_reproduced | 7/7 areas pass with the notebook's mean-to-mean comparison with puff 2. Under the criterion's wording (the interval above the puff-2 value), some areas fail, e.g., OLF with the code window (lower bound 0.048 against 0.164), HPF and MB. Most still pass (cell 38). |
| fig6b-persistent-dimension-distributed | reproduced | Every division with ≥ 30 units holds top-10% units; the largest share is 0.21–0.32 (cell 26). |
| fig6d-mouse-persistent | partially_reproduced | Pre vs Ket q ≤ 0.002 everywhere, and means within tolerance with first-puff projections. Post vs Ket fails without sub-1 (q = 0.051), and under the Methods-literal epochs (cell 22). |
| fig6f-mouse-fast-unchanged | reproduced | Pre vs Ket q ≥ 0.27 in all 12 readings. Pre values (4.01–4.47) are partly outside 4.48 ± 0.25, which the criterion does not require (cell 24). |
| fig6h-mouse-timescale | partially_reproduced | Without sub-5, both ways of combining series pass (p ≤ 0.016) with means within tolerance. Without sub-1 or sub-3, per-series fits fail (p 0.34–0.56), driven by degenerate fits (problem 2) (cell 28). |
| fig6j-mouse-coupling | partially_reproduced | With pooled variance, both readings pass (p ≤ 0.013; ratio 0.51–0.59, within). With the Methods per-unit variance, reading (a) gives p = 0.086 and 0.058 in two session readings, ratio 0.75–0.82 (cell 30). |
| figs34d-tone-fast-unchanged | reproduced | Judged without sub-5, the only exclusion that leaves table S3's 7 tone sessions from 7 mice: q ≥ 0.14 everywhere. Without sub-1 the absence fails (q = 0.0275) (cell 44). |
| figs34e-tone-persistent | reproduced | Both q < 0.05 with Ketamine lowest under every reading except the code split with pooled variance without sub-1 or sub-3 (q = 0.054). Means within tolerance (cell 46). |
| figs34f-tone-shorter-than-puff | reproduced | Puff half-peak fall 0.90–0.99 s against tone 0.16–0.17 s; 1–2 s intervals do not overlap (cell 48). |
| figs34g-tone-timescale | partially_reproduced | Without sub-5, every test passes (p ≤ 0.037). Ketamine means are within tolerance only for concatenated fits; per-series Ketamine is 0.140–0.161 against 0.089 ± 0.024. Without sub-1 or sub-3, per-series fails (cell 50). |
| figs34h-tone-coupling | not_reproduced | Reading (a) p ≥ 0.28 in every case; reading (b) passes once. Only the notebook's extra (b′, puff windows) passes (cell 52). |
| figs30-correlation-structure | not_reproduced | Within-region change 0.0063, p = 0.052; between-region change −0.0001, p = 0.89. The RSP (9/10) and ORB (5/7) increases hold, but the Ketamine window may be wrong (problem 3) (cell 54). |
| figs29-rsp-oscillations | reproduced (marginal) | RSP has the largest pooled rise at 5 and 10 min. Per-session rises: 7/9 at 5 min, but only 5/9 at 10 min (the notebook prints 5 of 10) (cell 56). |
| link-001347-condition-labels | reproduced (notebook says not tested) | All 99 ids are present with the trial counts the code reads. fig. 1K t = 4.737 and fig. S5 C–E t values (8.4882, 6.0804, 0.0878, 1.6120, 8.6017, 12.0602) are the same as the paper (behavior cells 3, 14, 26, 28). |
| link-001347-recorded-sessions | partially_reproduced (notebook says not tested) | 10 of 13 sessions have a file, and every matched series is within 14 ms of the clock fit. sub-3_ses-20230225 and both sub-5 sessions have no file (behavior cell 3). |
| fig1f, fig2d, figs14g | blocked, data_missing (agree, with limits) | No CADSS or report data were found, but the notebook searched only the `sub-SD*_puff_behavior` files, not `sub-H` or the ecephys files. The API metadata lists no measured variables. |
| figs4-reward-licking | blocked, data_missing (unverified) | The statement "only eye_closure" in behavior cell 3 is a hard-coded print, not a computed check. |
| fig2g, fig2i | not blocked | 001347 holds `sub-H_ses-sgramNMFLoadings.nwb` and `sgramNMFFactors.nwb` (0.3 MB each) and `sgramPerChannelPerTrial` (5.2 GB). fig2i, and fig2g at least from the deposited factors, look testable. The notebook gives no reason. |
| fig3b | not blocked | `sub-H_ses-ketChangePermutationClusterTest.nwb` (1.9 MB), `sgramPerYeoPerTrial` (107 MB) and `sgramPerRegionPerTrial` (624 MB) are on the archive. |
| fig6c, fig6e, fig6g, fig6i, figs12 | not blocked by absence | iEEG ecephys per participant and session (Baseline, Pre-, Infusion, Postinfusion; 207–434 MB each; 16 GB for the whole dandiset) are deposited. Whether figs12's spontaneous-blink events are there is unknown. |

**B. Problems**

1. **[affects a conclusion]** figs33, cell 42: variance explained is computed on the whole Ketamine half, series plus 25–70 s afterwards. The criterion asks for the Ketamine puff-series segment only. The margins between models are 0.001–0.006, so this choice can change which model is best.
2. **[affects a conclusion]** fig6h and figs34g, cells 28 and 50, and `K.extract_timescale`:
   - The exponential fit is unbounded, so degenerate per-series fits (Ketamine b = 833 s and 1.71 s) enter the session means while the notebook reports "failed fits 0". These single fits decide reading (a) without sub-1 or sub-3.
   - The autocorrelation is taken without subtracting the mean. On synthetic AR(1) data with τ = 0.1 s, the zero-mean estimate is 0.114 s; with a 2 s.d. offset it is 0.278 s. A mean level that differs between conditions can therefore bias the timescale comparison.
3. **[affects a conclusion]** figs30, `process_session` and cell 54: the Ketamine window starts at the code's onset (30 s after the last puff of series 20). In every session that is 94–420 s before the file's "Ketamine infusion start" (cell 4), and the Methods say "10-minute period following the onset of ketamine infusion". The window therefore includes up to 7 min before infusion, and no variant using the file's infusion time was run. The claims file's choice of onset is itself a questionable reading of the paper.
4. **[affects a conclusion, unchecked]** Epochs in all Ketamine comparisons: the notebook never shows that series 23 starts after the file's infusion time. With infusion up to 420 s after the code's onset (sub-7, sub-1_ses-20230226), early Ketamine series could be pre-drug.
5. **[affects a conclusion]** fig4i and fig4h, `region_times` and `rise_decay` (cell 14):
   - A cluster whose rise or decay is NaN (peak after 750 ms, or no fall below 25%) adds 0 to the weighted sum through `nansum`, with no renormalization of weights. The criterion instead drops such regions.
   - NaN rates may differ between Pre (40 replicates) and Ketamine (20 replicates), so the −0.185 s decay change may be partly an artifact. NaN fractions are not printed.
6. **[affects a conclusion]** figs31b, cell 10: the fast/slow split ranks clusters by decay of `cluster_means`, while cell 12 uses `cluster_trace`. Under the latter, VPM's cluster 2 (0.40 s) ranks 6th and leaves the faster half, and figs31b would fail at both thresholds.
7. **[affects a conclusion]** `emo_checks` (cell 32), used by figs32c: "puff 8 above puff 2" compares means only. The criterion's interval wording drops OLF, HPF, MB or STR in some readings.
8. **[affects a conclusion]** fig4b and fig5b: the outcome depends entirely on dividing each condition's trace by its own maximum. Without normalization, or with both divided by the Pre maximum, the ketamine effect disappears. Also, 3 of the 13 sessions are absent from 001347.
9. **[does not affect a conclusion]** fig1m: the event that ends survival is taken from the code only. The paper leaves it open, and the result is sensitive to the trial set.
10. **[does not affect a conclusion]** Leakage: the persistent, fast and emotion-like dimensions are trained on the same Pre series they are scored on, while Ketamine is out of sample. This follows the paper but inflates Pre-vs-Ketamine contrasts (fig6d, figs34e). No held-out check was run.
11. **[does not affect a conclusion]** Cell 56 counts sub-7 (no value) in the denominator ("5 of 10"). Cell 4 shows every unit's spike times stored out of order in the files; they are sorted on load and the clock check passes. Behavior cell 3's "only eye_closure" is a hard-coded print.
12. **[does not affect a conclusion]** The chance level for figs31b is 1/11 here against the paper's 1/12, because 11 clusters were found. fig6f Pre values are outside the expected tolerance under the Methods weights.

**C. Not checked**

- That `extract_timescale`, the `nansum` weighting and the max normalization match analysis.py. The code was not available to me.
- Whether series 23 starts after the file's infusion time. Needed: a per-session table of each series onset minus the infusion time.
- Whether tone or light stimuli fall inside the 50 s post-series windows or the 30 s pre-series baselines. A table of onsets relative to the puff series would settle whether the fig5d "last 5 s includes 0" failure, fig6h and fig6j are contaminated.
- The bias from unequal replicate counts in fig4h and fig4i. Needed: NaN fractions per condition, and a control with Pre subsampled to 20 replicates.
- fig6h and figs34g with median or bounded fits, and with the mean subtracted before autocorrelation.
- figs33 variance explained on the Ketamine series segment only, and figs30 with the file's infusion time.
- The contents of the `sub-H` files, the `sub-SD` ecephys and behavior files, and one `sub-mouse` file. Their HDF5 key listings would settle the blocked human and lick claims; the API metadata lists no measured variables.

## End of run

24 turns, 8 minutes, $2.73 at API prices, result: success.
