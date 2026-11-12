# brudner-2026 · verifier-1 · run 43166158634

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 208
drwxr-xr-x 6 runner runner    4096 Nov 12 06:26 .
drwxr-xr-x 8 runner runner    4096 Nov 12 06:26 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 06:09 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 06:09 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 12 06:26 .claude
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env.development
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env.local
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env.production
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env.test
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .env.test.local
drwx------ 2 runner runner    4096 Nov 12 06:26 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 06:09 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 06:09 .github
-rw-r--r-- 1 runner runner       0 Nov 12 06:26 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 06:09 .idea
[... 38 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "brudner-2026.yaml"
}
```

```
1	# Claims for Brudner, Zhou, Jayaram, Madeira Santana, Crimaldi, Clark & Emonet, "Fly navigational
2	# responses exploit plume-specific odor motion and gradient cues", PNAS 123(29) e2608896123 (2026),
3	# doi:10.1073/pnas.2608896123, on dandiset 001871.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-12,
6	# under docs/protocol.md version pilot-14 (Reader, steps 1 to 4). Nobody had analysed the dataset's
7	# data when these criteria were written; the reader saw only the dandiset's title and description.
8	#
9	# Text read: the version of record (PDF supplied by a person, published 14 July 2026), as extracted
10	# to paper/10.1073-pnas.2608896123.txt, with the SI Appendix (pnas.2608896123.sapp.pdf, appended to
11	# the same text file): Supplementary Methods, the legends of Figures S1 to S5 and of Movies S1 and S2.
12	# The main Methods section is a short summary that refers to the SI Appendix for every detail. PDF
13	# pages were opened to read the bar heights of Figures 2, 4 and 5 and the panels of Figure S5, and
14	# the upwind-turn formula of the SI agent simulations, which the text garbles. It reads
15	# P_upwind = 1 / (1 + exp(-(-0.49 + 1.5 R sin^2 theta))).
16	#
17	# Code read. The paper links github.com/emonetlab/GradientMotionMultiplePlumes; read at commit
18	# effc7b0317f6d3b62136c2a07bcba3e80e778575 (2026-07-14). It holds
19	#   - the Fig. 5E, 5F and S5D-E analysis (src/gradient_motion_panels/summary_tables.py,
20	#     scripts/generate_published_summary_tables.py, metadata/published_panel_params.json), written
[... 675 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_brudner_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (62KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/be1ad159-01ee-4f05-a030-f1141382798c/tool-results/bfaoqpg5a.txt

Preview (first 2KB):
==================== 0 markdown
# Reproducing Brudner, Zhou et al. (2026) from dandiset 001871

**Paper.** Brudner S, Zhou B, Jayaram V, Madeira Santana G, Crimaldi J, Clark DA, Emonet T (2026).
Fly navigational responses exploit plume-specific odor motion and gradient cues. *PNAS* 123(29)
e2608896123. [doi:10.1073/pnas.2608896123](https://doi.org/10.1073/pnas.2608896123). The claims file
(`claims/brudner-2026.yaml`) was written from the version of record and its SI Appendix; this attempt
read the same text, under `paper/`.

**Dandiset.** [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657), version
0.260630.1657. The paper cites no version. This is the only published version and the one the paper's
code (github.com/emonetlab/GradientMotionMultiplePlumes, commit effc7b0, `metadata/published_panel_params.json`)
names as the source of its Fig. 5 tables. The draft has the same 136 assets and total size.

**What the dandiset holds.** 131 behavior NWB files, one per trial of a fly cohort (83 smooth-plume
files, "nagel-smoke"; 24 "smoke-1a" and 24 "smoke-2a" complex-plume files), with per-trajectory
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/be1ad159-01ee-4f05-a030-f1141382798c/tool-results/bfaoqpg5a.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Brudner, Zhou et al. (2026) from dandiset 001871
3	
4	**Paper.** Brudner S, Zhou B, Jayaram V, Madeira Santana G, Crimaldi J, Clark DA, Emonet T (2026).
5	Fly navigational responses exploit plume-specific odor motion and gradient cues. *PNAS* 123(29)
6	e2608896123. [doi:10.1073/pnas.2608896123](https://doi.org/10.1073/pnas.2608896123). The claims file
7	(`claims/brudner-2026.yaml`) was written from the version of record and its SI Appendix; this attempt
8	read the same text, under `paper/`.
9	
10	**Dandiset.** [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657), version
11	0.260630.1657. The paper cites no version. This is the only published version and the one the paper's
12	code (github.com/emonetlab/GradientMotionMultiplePlumes, commit effc7b0, `metadata/published_panel_params.json`)
13	names as the source of its Fig. 5 tables. The draft has the same 136 assets and total size.
14	
15	**What the dandiset holds.** 131 behavior NWB files, one per trial of a fly cohort (83 smooth-plume
16	files, "nagel-smoke"; 24 "smoke-1a" and 24 "smoke-2a" complex-plume files), with per-trajectory
17	position, heading, velocities and the odor intensity, gradient and motion signals at the antennae,
18	and a table of turn events; the complex plume movie window (frames 300 to 1799 of smoke_1a_orig);
19	three freestream plume windows; and a compact asset of Fig. S1 panel inputs. The smooth plume movie
20	is not in it: it is on Dryad (doi:10.5061/dryad.g27mq71), which answers 401 to downloads without an
[... 675 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/be1ad159-01ee-4f05-a030-f1141382798c/tool-results/bfaoqpg5a.txt",
 "offset": 696
}
```

```
696	Gradient maps against the 3-pixel map:
697	 spacing px     r  r in mask  r, smoothed sigma 1.5 (variant)
698	          3 1.000      1.000                            1.000
699	          6 0.817      0.816                            0.968
700	          9 0.703      0.702                            0.911
701	         12 0.613      0.610                            0.809
702	
703	Motion maps (grad_dt) against the 3-pixel, 1-frame map; rows spacing (px), columns delay (frames):
704	       1      2      4      8      15
705	3   1.000  0.919  0.731  0.520  0.351
706	6   0.950  0.901  0.743  0.535  0.354
707	9   0.910  0.879  0.744  0.547  0.359
708	12  0.878  0.859  0.745  0.560  0.371
709	  in the Otsu mask:
710	       1      2      4      8      15
711	3   1.000  0.917  0.725  0.513  0.345
712	6   0.948  0.898  0.735  0.526  0.346
713	9   0.907  0.875  0.735  0.537  0.350
714	12  0.874  0.855  0.736  0.550  0.362
715	
[... 176 more lines not kept]
```

**Agent**

Notebook read. Fetching the full Fig. 5 tables that I cut off earlier.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_brudner_2026.ipynb'))
for i in (11,14):
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text',''))
        print(t[5500:] if i==11 else t[t.find('complex_1a  start 160-200    True           none'):])
"
```

```
0.0598    0.1464  0.0096 0.8477     0.3880
  complex_2a  start 150-210    True per_trajectory   1002           243 -0.1287   0.0544  0.0181    0.0037     0.0609    0.9515  0.0321 0.5726     0.9990
  complex_1a rule20 160-200   False           none    295           125  0.0200   0.0162  0.2166    0.0370     0.0186    0.0463  0.0058 0.2667    -0.4921
  complex_1a rule20 160-200   False         pooled    295           125  0.0955   0.0773  0.2166    0.2287     0.1148    0.0463  0.1097 0.2667    -0.4921
  complex_1a rule20 160-200   False per_trajectory    292           122  0.1015   0.0935  0.2779    0.4014     0.1415    0.0046  0.1098 0.2905    -0.7163
  complex_1a rule20 160-200    True           none    295           125  0.0200   0.0162  0.2166    0.0370     0.0186    0.0463  0.0058 0.2667    -0.4921
  complex_1a rule20 160-200    True         pooled    295           125  0.0955   0.0773  0.2166    0.2287     0.1148    0.0463  0.1097 0.2667    -0.4921
  complex_1a rule20 160-200    True per_trajectory    292           122  0.1015   0.0935  0.2779    0.4014     0.1415    0.0046  0.1098 0.2905    -0.7163
  complex_1a rule20 150-210   False           none    409           146  0.0251   0.0141  0.0736    0.0242     0.0143    0.0898  0.0057 0.2035     0.1139
  complex_1a rule20 150-210   False         pooled    409           146  0.1203   0.0672  0.0736    0.1495     0.0882    0.0898  0.1082 0.2035     0.1139
  complex_1a rule20 150-210   False per_trajectory    405           143  0.1255   0.0864  0.1465    0.2741     0.1104    0.0130  0.1066 0.2449    -0.3679
  complex_1a rule20 150-210    True           none    409           146  0.0251   0.0141  0.0736    0.0242     0.0143    0.0898  0.0057 0.2035     0.1139
  complex_1a rule20 150-210    True         pooled    409           146  0.1203   0.0672  0.0736    0.1495     0.0882    0.0898  0.1082 0.2035     0.1139
  complex_1a rule20 150-210    True per_trajectory    405           143  0.1255   0.0864  0.1465    0.2741   
[... 156 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "plumes.py"
}
```

```
1	"""Loading and measures for dandiset 001871 (Brudner, Zhou et al. 2026, PNAS, doi:10.1073/pnas.2608896123).
2	
3	The dandiset holds two kinds of NWB file, streamed here from the archive at the pinned version
4	into memory (nothing is written to disk):
5	
6	- Behavior files, one per recording session (trial) of a fly cohort. Per fly trajectory
7	  (`full_trjn`) they hold the centroid position (mm), heading `theta` and `theta_smooth`
8	  (degrees, 180 = upwind), `dtheta` (degrees/s), `vx`, `vy`, `spd` (mm/s), and the odor signals
9	  at the antennae, `signal` (intensity), `spatial_gradient` and `odor_velocity` (motion), all at
10	  60 Hz; and a `turn_events` table (start, stop, direction, heading, x, y, trajectory).
11	  Smooth-plume files have "nagel-smoke" in their path, complex-plume files "smoke-1a" or
12	  "smoke-2a".
13	- Plume movies: the complex smoke plume (frames 300 to 1799 of smoke_1a_orig, 1500 x 1088 x 1728,
14	  float32, 0 to 255) and three freestream plumes, with a compact asset of Fig. S1 panel inputs.
15	  The smooth plume is not in the dandiset.
16	
17	Where the parameters come from (claims file `claims/brudner-2026.yaml`, which cites the paper's
18	SI Appendix and the code github.com/emonetlab/GradientMotionMultiplePlumes at commit
19	effc7b0317f6d3b62136c2a07bcba3e80e778575, `src/gradient_motion_panels/summary_tables.py` and
20	`metadata/published_panel_params.json`):
[... 547 more lines not kept]
```

**Agent**

Notebook and helper read. Next: checking the paper for camera/turn-direction conventions, and the archive for the blocked claims.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "camera|projector|rightward|clockwise|turn direction|mirror|flipped|smoke.?1a|smoke.?2a|20%|onset" 10.1073-pnas.2608896123.txt | head -60
```

```
556:to the model by subtracting a mirror-symmetric version of the 
772:networks to extract directional cues from their bilateral odor histories in order to choose between clockwise and counterclockwise 
911:which reoriented flies by ~30° in the clockwise or counterclockwise 
925:onset to predict turn direction via logistic regression (permitting 
953:Fig. 5. Flies make turns consistent with plume-appropriate directional odor cues. (A) Apparatus uses a projector to generate spatiotemporally patterned 
988:simulated agents navigating in both plumes using a single turn direction algorithm that relied on a fixed linear combination of a 
991: ppendix, Supplementary Methods). Mirroring our analysis of the 
992:behaving flies, we used a logistic regression to predict the turn direction of upwind facing agents. We found that gradient cues were 
1081:modulated turn direction overall. Multiple factors likely affect the 
1176:turn direction. Detailed descriptions of plume construction, feature calculations, 
1705:Lighting) and recorded through an IR filter at 60 fps with a camera (FLIR Grasshopper USB 
1707:laminar airflow through the arena. We used a projector (DLP LightCrafter 4500) to deliver red 
1723:range of intensities we could deliver through our projector. We used a transformation of the 
1724:complex plume into projector intensities using the methods in [6]. This transformation includes a 
1726:and then linear scaling to fill the projector dynamic range. The nonlinear thresholding process 
1732:each plume’s projection was flipped across its centerline between successive trials. Individual fly 
1748:airflow, for 2 minutes prior to experiment onset. Each fly cohort navigated either smooth plume 
1770:the slope of projector intensity values across this slice as our gradient measure. Odor motion was 
1791:We modeled turn direction (left vs. right) using logistic regression. We used the smoothed and zscored estimates of olfactory cues intensity, gradient, and motion as pr
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1700,1800p 10.1073-pnas.2608896123.txt
```

```
(length) by 170mm (width) by 10mm (height). Laminar air (100mm/s) was introduced through 
an array of straws at the upwind side of the arena. A plastic mesh at the downwind side of the 
arena prevented flies from escaping. 
 
Flies in the arena were illuminated with side-mounted 850 nm IR LED strips (Waveform 
Lighting) and recorded through an IR filter at 60 fps with a camera (FLIR Grasshopper USB 
3.0). Dry air (Airgas) was passed through an array of aligned coffee straws to create 100mm/s 
laminar airflow through the arena. We used a projector (DLP LightCrafter 4500) to deliver red 
(627nm), csChrimson-activating light stimuli throughout the walking area. Stimuli updated at 
60Hz. 
 
The stimulus presentation and data recording operations were controlled in tandem by custom 
software written in Python 3.6.5. More detail about the control software is available in a prior 
publication [6]. 
 
Stimulus design 
 

 
6 
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001871/versions/0.260630.1657/assets/?page_size=200" -o assets.json; python3 -c "
import json;d=json.load(open('assets.json'));print(d['count'])
for a in d['results']:
    p=a['path']
    if 'figs1' in p or 'smooth' in p.lower() or 'nagel' not in p and 'smoke' not in p: print(a['asset_id'],p,a['size'])
"; curl -s "https://api.dandiarchive.org/api/dandisets/001871/versions/0.260630.1657/" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, plumes
# exp smooth equivalence
x=np.random.randn(500); a=plumes.exp_smooth(x,60,200); b=plumes._exp_smooth_fast(x,60,200); print('exp eq',np.abs(a-b).max())
# onset rule: previous opposite turn adjacent
t=np.arange(40)/60.; d=np.zeros(40); d[5:12]=-300; d[12:20]=[60,150,300,400,300,150,60,10]
print(plumes.onset_20pct(t,np.abs(d),t[13],t[18]))
# motion feature sign for rightward-moving pattern
T=200; s=np.random.rand(T+5); tr=np.zeros((T,1,2)); tr[:,0,0]=s[2:T+2]; tr[:,0,1]=s[0:T] # antenna1 lags antenna0 by 2 frames
F=plumes.window_features(tr*50+10,delays=(1,2)); print('motion2 mean',F['motion2'].mean(),'motion1',F['motion1'].mean())
# draw_samples mirror symmetry
F={'sum':np.random.rand(50,20),'gradient':np.random.randn(50,20),'motion1':np.random.randn(50,20)}
lab=(np.arange(20)>10).astype(int); rng=np.random.default_rng(0)
Xtr,ytr,Xte,yte=plumes.draw_samples(F,lab,'mirror',rng,n_train=8000,n_test=2000); print('mirror ytr mean',ytr.mean(), yte.mean())
Xtr,ytr,Xte,yte=plumes.draw_samples(F,lab,'location',rng,n_train=8000,n_test=2000)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, plumes
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls -d /usr/bin/python3* ~/.venv* /opt/*/bin/python* 2>/dev/null; which -a python python3 uv pip 2>/dev/null; python3 -m pip --version 2>&1 | head -1
```

```
/opt/az/bin/python-argcomplete-check-easy-install-script
/opt/az/bin/python3
/opt/az/bin/python3-config
/opt/az/bin/python3.14
/opt/az/bin/python3.14-config
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
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
/usr/bin/pip
/bin/pip
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for p in /usr/bin/python3 /opt/az/bin/python3; do $p -c "import numpy,scipy,pandas;print('$p ok')" 2>&1|tail -1; done
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
```

**Agent**

No Python environment with numpy exists; trying a temporary venv to run synthetic tests of the helpers.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && uv pip install -q --python v/bin/python numpy scipy pandas h5py requests 2>&1 | tail -2; v/bin/python -c "import numpy;print(numpy.__version__)"
```

```
2.5.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, plumes
x=np.random.randn(500); print('exp eq',np.abs(plumes.exp_smooth(x,60,200)-plumes._exp_smooth_fast(x,60,200)).max())
t=np.arange(40)/60.; d=np.zeros(40); d[5:12]=-300; d[12:20]=[60,150,300,400,300,150,60,10]
on,tp,pk,j,e=plumes.onset_20pct(t,np.abs(d),t[13],t[18]); print('onset idx',j,'peak idx',round(tp*60),'end',e,' (true onset of + turn = 12)')
print('int over SI-bounded', np.sum(d[j:e+1])/60)
s=np.random.rand(300); tr=np.zeros((290,1,2)); tr[:,0,0]=s[2:292]; tr[:,0,1]=s[0:290]
F=plumes.window_features(tr*50+10,delays=(1,2)); print('motion2 mean',F['motion2'].mean().round(3),'motion1',F['motion1'].mean().round(3))
F={'sum':np.random.rand(50,20),'gradient':np.random.randn(50,20),'motion1':np.random.randn(50,20)}
lab=(np.arange(20)>10).astype(int); rng=np.random.default_rng(0)
Xtr,ytr,Xte,yte=plumes.draw_samples(F,lab,'mirror',rng,n_train=8000,n_test=2000); print('mirror label means',ytr.mean(),yte.mean())
fr=np.arange(30.)[:,None]*np.ones((1,4))
for dd in (3,6): a,b=plumes._pair(fr,dd); print(dd,a[0,0],b[0,0],(a.shape))
"
```

```
exp eq 0.0
onset idx 13 peak idx 15 end 17  (true onset of + turn = 12)
int over SI-bounded 21.666666666666668
motion2 mean 0.355 motion1 0.01
mirror label means 0.493625 0.5255
3 5.0 8.0 (17, 4)
6 3.0 9.0 (17, 4)
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, plumes
t=np.arange(40)/60.; d=np.zeros(40); d[5:12]=-300; d[12:20]=[100,150,300,400,300,150,100,10]
on,tp,pk,j,e=plumes.onset_20pct(t,np.abs(d),t[13],t[18]); print('onset idx',j,'(true 12); integral',np.sum(d[j:e+1])/60, 'vs +turn only', np.sum(d[12:19])/60)
"
```

```
onset idx 5 (true 12); integral -10.0 vs +turn only 25.0
```

**Agent**

**Verifier report, brudner-2026, round 1 (DANDI:001871 @ 0.260630.1657)**

The claims file has 22 claims. The notebook tests 6, treats 16 as blocked, and its own table covers all 22.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig5e-cue-betas | not_reproduced | The criterion counts a claim as reproduced only if every reading gives that result; here the result depends on the reading. With the SI onset (`rule20`) and smoke-2a, both plumes pass with stored or pooled z-scored signals. Per-trajectory z-scoring fails both plumes: smooth motion p = 0.0066, complex motion p = 0.098 and 0.204 (cell 11). Under the code's readings the complex coefficients have the wrong sign and are out of tolerance (motion −0.0119 against +0.0441 ± 0.0159; cell 12). |
| fig5f-cue-dominance | reproduced | One reading gives both values within tolerance with the right signs: `rule20`, smoke-2a, heading 150–210, z none or pooled gives smooth 0.935 and complex −0.715 (cell 14). smoke-1a with the event start and heading 160–200 also gives 0.879 / −0.701. The result is fragile: under the code's readings the complex value is +0.388. |
| figs5c-turn-angles | reproduced (rests on an added reading) | With the files' event bounds, both readings in the claims file give medians of about ±21°, outside tolerance. Only the notebook's own turn bounds (20% crossings on the rising and falling edges) give −35.0 / +35.9, or −33.1 / +36.6 for the kept turns (cell 16). That rule has a bug (problem 2). |
| fig2c-complex-auc | partially_reproduced | Motion AUC is above gradient AUC under every reading. Under the two samplings the claims file names, the sum AUC is 0.63–0.67, which fails the sum condition. Only the added mirror sampling gives a sum AUC of 0.500. The values miss under every reading: motion 0.602 against 0.618 ± 0.005, gradient 0.554–0.560 against 0.537 ± 0.012 (cell 25). |
| fig2e-complex-weights | partially_reproduced | \|motion\| (0.415–0.424) is larger than \|gradient\| under every reading. The gradient weight (0.234–0.271) is outside 0.098 ± 0.041 under every reading (cell 25). |
| figs1fg-resolution-robustness | not_reproduced | Gradient r at 12 px is 0.613 without smoothing (0.809 with σ 1.5 smoothing, a variant). Motion r at a 4-frame delay is 0.73–0.82 against the required ≥0.8 at every spacing (0.729 at 3 px in both forms). The drop at 8 and 15 frames does hold (cell 21). |
| figs2c-one-frame-delay | blocked (data_missing) | The smooth plume was not read. The complex half holds: AUC at τ = 1 is 0.603, at τ = 15 is 0.505, and τ = 1 is the highest (cell 28). |
| methods-intensity-right-bias | blocked (metadata_insufficient) | The files do not say whether turn direction −1 is left or right. Both conditional outcomes can be stated from cell 11: the smooth intensity coefficient is −0.050 with p < 1e-4, and complex smoke-2a is n.s. So the claim holds if −1 is a right turn and fails if not. The notebook did not state this. |
| fig1eh-snapshot-organization, fig1il-zscore-reliability | blocked (data_missing) | Both need the smooth plume, which is on Dryad and was not staged. |
| figs1-antisymmetry-index, figs1-temporal-statistics | blocked (data_missing) only for the smooth comparison | The archive's dandiset description says the compact asset `sub-figs1-freestream-plumes…behavior.nwb` (57 MB) holds the mean gradient and motion maps and the exact plotted frequency/intermittency points for 5, 10 and 20 cm/s. The three freestream movies and the complex movie are also deposited. The freestream ordering and the "complex highest" parts could therefore be tested; the notebook did not test them. |
| fig2b-smooth-auc, fig2d-smooth-weights | blocked (data_missing) | Both are smooth-plume only. |
| fig3bc, fig3d, fig3e, fig3ij, fig4ef, discussion-ten-percent-gain, figs4, figs5fh | blocked (data_missing) | Each needs the smooth plume or a network trained on it. Some complex-only parts are testable in principle from the deposited movie: the complex MNM filter and its AUC of 0.517, and complex wind-only against complex-trained agents. The agent code is not in the paper's repository. |

### B. Problems

1. **[affects a conclusion]** The choice of complex file set (cells 10–14) is doubtful. The notebook takes smoke-2a as the main set because the claims file says the code selects it. But the archive's own dandiset description says smoke_1a_orig "was analyzed throughout the paper". smoke-1a with the event start and heading 160–200 reproduces the published Fig. 5E coefficients almost exactly: gradient 0.0174 against 0.0185, motion 0.0456 against 0.0441, motion p = 0.0059. smoke-2a gives motion coefficients of the opposite sign. Pooling the two sets passes 0 of 24 readings. Together these suggest the two sets differ in a sign or flip convention. This decides the fig5e and fig5f outcomes, and the notebook neither flags nor investigates it.
2. **[affects a conclusion]** `plumes.onset_20pct` scans runs of |dtheta| ≥ 20% of the peak, ignoring the sign of the rotation. A synthetic test showed the run crossing into an adjacent opposite-direction turn: the onset moved from frame 12 to frame 5, and the integral became −10° instead of +25°. The onset lead reaches 127 frames in cell 7, which is consistent with this. The bug affects every `rule20` reading of fig5e and fig5f, and the SI-bounded integral of figs5c. The rule should scan signed rotation in the turn's direction.
3. **[affects a conclusion]** fig2c passes its sum condition only under the added mirror sampling (`plumes.draw_samples`, "mirror"). The assumption is reasonable: the paper reports a sum AUC of 0.5 with SD 0 and a sum weight of 0 "as expected". But it is the author's own reading. Under the claims file's readings, fig2c is not_reproduced.
4. **[affects a conclusion]** In cell 21, the σ 1.5 smoothing variant was run for the gradient only, not for motion. Smoothing lifts the gradient r at 12 px from 0.61 to 0.81, so the figs1fg gradient part depends on this unstated choice. The motion part was not tried under the same variant.
5. **[affects a conclusion]** figs1-antisymmetry-index and figs1-temporal-statistics are declared wholly blocked. Their freestream and complex parts can be tested from deposited assets (see table A).
6. **[affects a conclusion]** methods-intensity-right-bias: the notebook does not report the outcome under each left/right mapping, although its cell 11 numbers settle it once the mapping is fixed.
7. **[does not affect a conclusion]** The movie is a background-subtracted preprocessing ("bgsub_gauss3…", cell 19), and the mean-map maximum is at row 571, not the centerline row 590. Either may explain the Fig. 2 value misses. The notebook notes the first, but does not test either.
8. **[does not affect a conclusion]** In `draw_samples` "random" and "mirror", 3 M draws with replacement come from about 1.47 M windows, so many test windows also appear in training. "location" sampling avoids this and gives the same AUCs.
9. **[does not affect a conclusion]** In `movie_pass1`, "grad_dt" uses a backward temporal difference, where Fig. 1 uses a centered one.
10. **[does not affect a conclusion]** In `keep`, heading is taken at onset − 50 ms, while position uses turn_x/turn_y at the event start.
11. **[does not affect a conclusion]** The margin readings are identical to no margin. I checked this against the percentiles in cell 5: the x/y region filters already lie inside the 15 mm margin, so the margin removes nothing. This is correct behaviour.
12. **[does not affect a conclusion]** Cell 26 still contains the author's "Result" conclusions. I formed my outcomes from the outputs alone.

### C. What I could not check

- **The paper's code repository.** I could not see `filter_published_turns` (heading column `theta` or `theta_smooth`, which complex substring it selects) or the published Fig. 5 tables' turn counts. An output comparing the kept-turn counts per group with the published `fig5e_*.csv` row counts would settle problem 1.
- **Why smoke-1a and smoke-2a differ in sign.** Output needed: session descriptions and vflip counts per group, and the motion coefficient fitted separately for vflip0 and vflip1 trials.
- **How many turns problem 2 affects.** Output needed: the fraction of turns whose 20% run contains a sign change of dtheta, and fig5e, fig5f and figs5c re-run with a signed onset rule.
- **figs1fg under smoothing.** Output needed: the motion map correlations with σ 1.5 smoothing.
- **The figs1 freestream parts.** Output needed: the index, frequency and intermittency medians from the compact freestream asset and the complex movie.
- **Smooth-plume access.** I did not verify the notebook's statement that Dryad returns 401 without a token. I did confirm through the DANDI API (136 assets and the dandiset description) that the smooth plume is not in the dandiset.

I tested the helpers on synthetic inputs in a temporary environment. `exp_smooth` and its fast version agree exactly, `_pair` aligns correctly, the motion feature has the expected sign, and mirror sampling balances the labels. The only failure found was the `onset_20pct` bug in problem 2.

## End of run

17 turns, 5 minutes, $1.56 at API prices, result: success.
