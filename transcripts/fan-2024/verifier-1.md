# 000959 · verifier-1 · run 41258811666

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 320
drwxr-xr-x 6 runner runner    4096 Nov  1 01:09 .
drwxr-xr-x 7 runner runner    4096 Nov  1 01:09 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:54 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:54 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  1 01:09 .claude
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env.development
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env.local
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env.production
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env.test
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .env.test.local
drwx------ 2 runner runner    4096 Nov  1 01:09 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:54 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:54 .github
-rw-r--r-- 1 runner runner       0 Nov  1 01:09 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 00:54 .idea
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2024.05.004.yaml"
}
```

```
1	# Claims for Fan, Dal Monte, Nair, Fagan & Chang (2024) on dandiset 000959.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the accepted author manuscript in PubMed Central (PMC11309918, NIHMS1994226),
6	# main text, figure legends and STAR Methods, with its one supplement
7	# (NIHMS1994226-supplement-1.pdf, Table S1 and the legends of Figures S1 to S4). The version of
8	# record (Neuron 112(15) 2631-2644.e6) was not read. The Results point to "Supplementary
9	# Results" for the Mouth stimulation experiments and the post-gaze window; the supplement holds
10	# no such section, and these results are given in the STAR Methods of the manuscript
11	# ("Gaze distance analyses" and "Gaze distance analyses (Mouth stimulation)"), which were read.
12	#
13	# Code read: github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994 (2024-10-15),
14	# the analysis code named in Data and code availability (also Zenodo doi:10.5281/zenodo.11110139).
15	# It holds MATLAB scripts for every analysis of the paper ("Scripts for social attention":
16	# Get data, Overall gaze behavior and number of stims, Heatmap, Spatial dimension, Temporal
17	# dimension, Inter-individual dynamics, Saccade kinematics) and older scripts (stim/, script/).
18	# It starts from intermediate files (fixation events, ROIs, positions, stimulation and sham
19	# times) made by an upstream pipeline that is not in the repository, and it calls functions
20	# of outside packages (bfw, shared_utils, dsp3). The causal decomposition itself was run
[... 910 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "microstim.py"
}
```

```
1	"""Loading and measures for the closed-loop microstimulation gaze data of dandiset 000959.
2	
3	Fan, Dal Monte, Nair, Fagan & Chang (2024), Neuron 112, 2631-2644,
4	doi:10.1016/j.neuron.2024.05.004. The claims file is claims/000959/10.1016-j.neuron.2024.05.004.yaml.
5	
6	Each NWB file holds one 300-s run (a "session" in the paper) of one day: M1's gaze (pixels,
7	1 kHz), in social runs M2's gaze, pupil size, the stimulation and sham times
8	(`stimulation_events`), the ROIs of the day (`roi_definitions`), and fixation events as
9	interval tables (`m1_all`, `m1_eye`, `m1_wholeface`, ..., `m2_*`, `mutual_*`). The
10	`session_description` names the date, run, subject, stimulated region, triggering ROI (Eyes or
11	Mouth) and condition (Social, or Dot for the non-social RDM control). Files are read over HTTP
12	into memory at the pinned version; nothing is written to disk.
13	
14	Where the parameters come from:
15	
16	- Trial selection (the claims file's opening comment, from the paper's code): a trial is kept
17	  when its time lies within the valid run (non-NaN `t`) and more than 5 s before the run's last
18	  valid sample; the first trial of each run is dropped. Trials are grouped by their own label.
19	- Post-gaze epoch: fixations whose start lies in [0, 1.5) s after the trial (claims file,
20	  opening comment; STAR Methods, Fixation density map, "within 1.5 sec after the onset").
[... 355 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2024.05.004.yaml",
 "offset": 930
}
```

```
930	    test: Wilcoxon signed rank, two-sided
931	    p: 0.757
932	  - about: contralateral
933	    test: Wilcoxon signed rank, two-sided
934	    p: 0.882
935	  - about: ipsilateral
936	    test: Wilcoxon signed rank, two-sided
937	    p: 0.098
938	  depends_on:
939	  - figs4a-causal-strength-no-stim-effect
940	  - epoch-days-76-of-81
941	  criterion: A claim of absence, judged on the paper's test. From the Methods and
942	    S3_Gaze_Correlation_by_Epoch.m. For each day and epoch, an ordinary least squares fit (fitlm)
943	    of relative causal strength on social gaze distance (in degrees) over the stimulation trials
944	    of the epoch; distance is the trial mean over fixations in the post-gaze epoch, overall,
945	    contralateral or ipsilateral. Late against early slopes, signed-rank over OFC days.
946	    Reproduced when no test gives p < 0.05, under each reading of figs4a-causal-strength-no-stim-effect.
947	- id: fig4c-dmpfc-slope-late-greater
948	  statement: For dmPFC, the slope of the relation between contralateral social gaze distance and
949	    relative causal strength was larger in the late than in the early epoch (p = 0.054, at the
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.1016-j.neuron.2024.05.004.yaml; python3 - <<'E'
import json
nb=json.load(open('reproduce_fan_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== [{i}] {c['cell_type']}")
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
E
```

```
<persisted-output>
Output too large (82.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/73048ef3-a141-43ab-89a3-3b1217fe5337/tool-results/bdfp35eh8.txt

Preview (first 2KB):
36
===== [0] markdown
# Reproducing Fan et al. (2024) from dandiset 000959

**Paper.** Fan, Dal Monte, Nair, Fagan & Chang (2024), "Closed-loop microstimulations of the
orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention",
Neuron 112, 2631-2644, doi:10.1016/j.neuron.2024.05.004.

**Claims.** `claims/000959/10.1016-j.neuron.2024.05.004.yaml`, written from the accepted author
manuscript (PMC11309918) with its supplement, and the paper's code
(github.com/changlabneuro/microstim-ofc-social-attention at cc0bf994).

**Dataset.** DANDI:000959, version 0.261020.0242. The paper cites the dandiset without a
version. Two versions are published, 0.260531.2104 and 0.261020.0242; the most recent is pinned,
as the protocol asks when the paper cites none. The data check below compares the two asset
lists: both hold the same 1705 assets with the same identifiers, paths and sizes, so the choice
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/73048ef3-a141-43ab-89a3-3b1217fe5337/tool-results/bdfp35eh8.txt"
}
```

```
1	36
2	===== [0] markdown
3	# Reproducing Fan et al. (2024) from dandiset 000959
4	
5	**Paper.** Fan, Dal Monte, Nair, Fagan & Chang (2024), "Closed-loop microstimulations of the
6	orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention",
7	Neuron 112, 2631-2644, doi:10.1016/j.neuron.2024.05.004.
8	
9	**Claims.** `claims/000959/10.1016-j.neuron.2024.05.004.yaml`, written from the accepted author
10	manuscript (PMC11309918) with its supplement, and the paper's code
11	(github.com/changlabneuro/microstim-ofc-social-attention at cc0bf994).
12	
13	**Dataset.** DANDI:000959, version 0.261020.0242. The paper cites the dandiset without a
14	version. Two versions are published, 0.260531.2104 and 0.261020.0242; the most recent is pinned,
15	as the protocol asks when the paper cites none. The data check below compares the two asset
16	lists: both hold the same 1705 assets with the same identifiers, paths and sizes, so the choice
17	does not change the data.
18	
19	Each file is one 300-s run (a "session" in the paper) and holds M1's gaze and pupil at 1 kHz,
20	M2's gaze and pupil in social runs, the stimulation and sham times, the day's ROIs, and
[... 851 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/73048ef3-a141-43ab-89a3-3b1217fe5337/tool-results/bdfp35eh8.txt",
 "offset": 872
}
```

```
872	   OFC       T 12        3.615     -10.19  0.6221           0.1422
873	 dmPFC       L 15        10.29      23.04 0.04791            0.405
874	 dmPFC       T 12        -6.91     -15.61  0.2334          -0.2719
875	  ACCg       L 15       -15.32     -14.76   0.107          -0.6027
876	  ACCg       T 12        15.53      9.436  0.5186           0.6112
877	
878	===== [32] code
879	hd = hemi_table({h: ddot[h][1] for h in ["contra", "ipsi"]}, AREAS)
880	print(hd.to_string(index=False, float_format=lambda v: f"{v:.4g}"))
881	--OUT--
882	region subject  n_contra  contra_median  contra_p  n_ipsi  ipsi_median  ipsi_p  n_cvi  contra_minus_ipsi_median   cvi_p
883	   OFC    both        27         -6.805    0.1624      27       -7.688  0.4133     27                    -26.77  0.4553
884	   OFC       L        15         -20.93     0.073      15        9.694  0.8904     15                    -36.99 0.06372
885	   OFC       T        12          0.188         1      12       -30.09  0.2036     12                     15.61  0.4697
886	 dmPFC    both        27          3.945    0.3361      27        2.025  0.5619     27                    -3.035  0.7676
887	 dmPFC       L        15          13.39   0.03534      15         16.9  0.2524     15                    -3.035  0.3028
888	 dmPFC       T        12         -3.976    0.4238      12       0.4997   0.791     12                    -6.519  0.6772
889	  ACCg    both        27          2.255    0.7496      27       0.2689  0.9717     27                      3.54  0.2792
890	  ACCg       L        15         -4.747    0.4887      15       -10.03  0.5614     15                     1.986  0.6387
891	  ACCg       T        12          24.12    0.3394      12        14.66  0.5693     12                     14.88  0.5693
[... 700 more lines not kept]
```

**Agent**

Notebook and claims read (36 claims). Now testing helper functions on synthetic inputs and checking the archive for the blocked claims.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import numpy as np, pandas as pd, microstim as ms
# window_pairs synthetic
tr = pd.DataFrame({"run_id":[0,0,1],"time":[10.0,20.0,10.0]}, index=[5,7,9])
ev = pd.DataFrame({"run_id":[0,0,0,1,1,1],"start":[9.9,10.0,11.4,10.2,11.6,25.0],"stop":[10.5,10.3,11.6,10.4,11.8,25.2],
                   "x":[0.,3,4,6,8,0],"y":[0.,4,0,8,0,0],"eyes_x":[0.]*6,"eyes_y":[0.]*6,"hemi":["c"]*6})
p = ms.window_pairs(tr, ev, 0.0, 1.5); print(p[["trial","start","lag"]])
print("dist", list(ms.trial_distance(tr, ev)))
print("lat", list(ms.first_latency(tr, ev)))
# reciprocation: m2 at 0.1, m2 at 0.3, m1 at 0.5, m2 at 1.0, m1 at 1.2 -> lats 0.4, 0.2 -> 0.3
t2 = pd.DataFrame({"run_id":[0],"time":[0.0]}, index=[0])
m1 = pd.DataFrame({"run_id":[0,0],"start":[0.5,1.2],"stop":[0.6,1.3]})
m2 = pd.DataFrame({"run_id":[0,0,0],"start":[0.1,0.3,1.0],"stop":[0.2,0.4,1.1]})
print("recip", list(ms.reciprocation(t2, m1, m2)))
# tie: mutual event with equal starts in both lists
m1b = pd.DataFrame({"run_id":[0],"start":[0.5],"stop":[0.6]}); m2b=pd.DataFrame({"run_id":[0,0],"start":[0.1,0.5],"stop":[0.2,0.6]})
print("recip tie", list(ms.reciprocation(t2, m1b, m2b)))
print(ms.DEG_PER_PX*768)
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls executed/000959-fan-2024/.venv/bin/python 2>&1; which python3 uv pip 2>&1; python3 -m pip --version 2>&1 | head -1
```

```
ls: cannot access 'executed/000959-fan-2024/.venv/bin/python': No such file or directory
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/pip
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && VIRTUAL_ENV=$TMPDIR/v uv pip install -q numpy pandas scipy h5py requests 2>&1 | tail -2; ls v/bin/python
```

```
v/bin/python
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'E'
import numpy as np, pandas as pd, microstim as ms
tr = pd.DataFrame({"run_id":[0,0,1],"time":[10.0,20.0,10.0]}, index=[5,7,9])
ev = pd.DataFrame({"run_id":[0,0,0,1,1,1],"start":[9.9,10.0,11.4,10.2,11.6,25.0],"stop":[10.5,10.3,11.6,10.4,11.8,25.2],
                   "x":[0.,3,4,6,8,0],"y":[0.,4,0,8,0,0],"eyes_x":[0.]*6,"eyes_y":[0.]*6,"hemi":["c"]*6})
p = ms.window_pairs(tr, ev, 0.0, 1.5); print(p[["trial","start","lag"]])
print("dist", list(ms.trial_distance(tr, ev)))
print("lat", list(ms.first_latency(tr, ev)))
t2 = pd.DataFrame({"run_id":[0],"time":[0.0]}, index=[0])
m1 = pd.DataFrame({"run_id":[0,0],"start":[0.5,1.2],"stop":[0.6,1.3]})
m2 = pd.DataFrame({"run_id":[0,0,0],"start":[0.1,0.3,1.0],"stop":[0.2,0.4,1.1]})
print("recip", list(ms.reciprocation(t2, m1, m2)))
m1b = pd.DataFrame({"run_id":[0],"start":[0.5],"stop":[0.6]}); m2b=pd.DataFrame({"run_id":[0,0],"start":[0.1,0.5],"stop":[0.2,0.6]})
print("recip tie (m2 .1, mutual .5 both):", list(ms.reciprocation(t2, m1b, m2b)))
# scipy exact vs MATLAB-style normal approx for n=27
from scipy.stats import wilcoxon, norm
n=27; rng=np.random.default_rng(0)
for target in [0.0436,0.046,0.058,0.0187]:
    best=None
    for _ in range(20000):
        d=rng.normal(0.4,1,n)
        pe=wilcoxon(d).pvalue
        if abs(pe-target)<0.001:
            r=pd.Series(np.abs(d)).rank().values; W=r[d>0].sum()
            mu=n*(n+1)/4; sd=np.sqrt(n*(n+1)*(2*n+1)/24)
            z=(W-mu-0.5*np.sign(W-mu))/sd; pa=2*norm.sf(abs(z))
            print(target, "exact",round(pe,4),"approx(cc)",round(pa,4)); break
E
```

```
trial  start  lag
0      5   10.0  0.0
1      5   11.4  1.4
2      9   10.2  0.2
dist [4.5, nan, 10.0]
lat [1.4000000000000004, nan, 0.1999999999999993]
recip [0.3]
recip tie (m2 .1, mutual .5 both): [0.4]
0.0436 exact 0.0436 approx(cc) 0.0448
0.046 exact 0.0463 approx(cc) 0.0475
0.058 exact 0.0585 approx(cc) 0.0593
0.0187 exact 0.0187 approx(cc) 0.0204
```

**Agent**

Helpers behave correctly on synthetic inputs; MATLAB's normal approximation would not flip any near-threshold p. Now the archive check for blocked claims.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/v/bin/python - <<'E'
import requests, json
API="https://api.dandiarchive.org/api"
v=requests.get(f"{API}/dandisets/000959/versions/0.261020.0242/info/",timeout=60).json()
md=v.get("metadata",{})
print(md.get("name")); print(md.get("description","")[:3000])
am=md.get("assetsSummary",{}); print(json.dumps(am,indent=0)[:2000])
a=requests.get(f"{API}/dandisets/000959/versions/0.261020.0242/assets/?page_size=3",timeout=60).json()["results"]
for x in a[:1]:
    m=requests.get(f"{API}/dandisets/000959/versions/0.261020.0242/assets/{x['asset_id']}/",timeout=60).json()
    print(x["path"]); print(json.dumps(m.get("variableMeasured"),indent=0)[:1500]); print(m.get("measurementTechnique"))
E
```

```
Closed-loop microstimulations of the orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention
These are the raw and processed data accompanying our manuscript "Closed-loop microstimulations of the orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention". In this paradigm, two animals face each-other and freely gaze at one another while their gaze positions are continuously tracked in real-time. One animal ("M1") receives a low-amplitude microstimulation to one of three prefrontal areas (OFC, ACCg, and dmPFC) that is triggered contingently by specific gaze events, such as looking at the other animal's ("M2") eyes. These data consist of the continuous gaze positions and pupil sizes from each animal; the stimulation event times; and multiple gaze ROIs of each animal.
{
"species": [
{
"name": "Macaca mulatta - Rhesus monkey",
"schemaKey": "SpeciesType",
"identifier": "http://purl.obolibrary.org/obo/NCBITaxon_9544"
}
],
"approach": [
{
"name": "behavioral approach",
"schemaKey": "ApproachType"
}
],
"schemaKey": "AssetsSummary",
"dataStandard": [
{
"name": "Neurodata Without Borders (NWB)",
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "bootstrap|Month stimulation|non-social control sessions|inter-looking interval was|Otero" 10.1016-j.neuron.2024.05.004.txt | cut -c1-600
```

```
170:Each data collection day consisted of a total of alternating 10 live social gaze sessions and 5 non-social control sessions on average for monkey L (9-11 social and 4-8 control sessions across all days) and alternating 15 live social gaze sessions and 5 non-social control sessions on average for monkey T (14-15 social and 5 control sessions across all days). Each session lasted 300 sec. During live social gaze sessions, pairs of monkeys were allowed to freely interact with each other using gaze (Fig. 1A, left). During non-social control sessions, M1 was allowed to freely examine the space 
178:On each day before data collection, a guide tube was used to penetrate intact dura and to guide a microstimulation electrode (median impedance 50 kΩ, FHC Inc.) and a recording electrode (tungsten, FHC Inc.), which were remotely lowered by using a motorized multi-electrode microdrive system (NaN Instruments) at the speed of 0.02 mm/sec. After the two electrodes reached target site, we ensured that we positioned the electrodes in the grey matter and waited 30 min for the tissue to settle for signal stability before starting experiment. The microstimulation site was usually positioned within 
187:In our main Eyes stimulation experiments, on each day, we identified the following regions of interest (ROIs): Eyes and non-eye Face (the rest of the face excluding the Eyes regions) in the live social gaze condition, and RDM stimulus in the non-social control condition (same location and size as Eyes ROI). In some analyses, we examined whole Face which is the union of Eyes and non-eye Face ROIs. Based on each day’s calibration, whole Face ROI was defined by the four corners of a monkey’s face and the Eyes ROI was defined by adding a padding of to the center of each eye. Fixations were ide
201:Similarly, for Mouth stimulation, we examined social gaze distance (defined as the average Euclidean distance between each fixation during the post-gaze epoch and the center of partner’s Mouth)
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 201,203p 10.1016-j.neuron.2024.05.004.txt | cut -c1-2500
```

```
Similarly, for Mouth stimulation, we examined social gaze distance (defined as the average Euclidean distance between each fixation during the post-gaze epoch and the center of partner’s Mouth) and non-social gaze distance (defined as the average Euclidean distance between each fixation and the center of the corresponding RDM stimulus). Wilcoxon signed rank test was used to compare social gaze distance between microstimulation and sham trial types. On the day level, none of the three brain regions had any microstimulation effect on social gaze distance (OFC: p = 1; dmPFC: p = 1; ACCg: p = 0.125; Wilcoxon signed rank, two-sided; when considering fixations in the ipsilateral hemifield and the contralateral hemifield separately, all p > 0.18) or non-social gaze distance (OFC: p = 1; dmPFC: p = 0.188; ACCg: p = 0.188; when considering fixations in the ipsilateral hemifield and the contralateral hemifield separately, all p > 0.06). Moreover, to control for unbalanced sample size between Eyes stimulation (n = 27 per area in total; n = 15 from monkey L and n = 12 from monkey T) and Mouth stimulation (n = 5 per area from monkey T), we first bootstrapped by randomly selecting 5 days with replacement from all the available data (n = 27) in Eyes stimulation for 1,000 times and compared the 1,000 medians to the true median in Month stimulation. For fixations in the contralateral hemifield, microstimulation effect (stimulation minus sham) of OFC led to significantly smaller social gaze distance in Eyes stimulation compared to Month stimulation (p = 0.009), while no effect was observed for fixations in the ipsilateral hemifield (p = 0.724) or when both hemifields combined (p = 0.799). To be more precise, we bootstrapped by randomly selecting 5 days with replacement from monkey T’s data only (n = 12) in Eyes stimulation for 1,000 times and compared the 1,000 medians to the true median in Mouth stimulation and the differences were even more significant (p = 0.005 for contralateral;
[... 2 more lines not kept]
```

**Agent**

# Verifier report, round 1: Fan et al. 2024 (DANDI:000959, version 0.261020.0242)

The claims file holds 36 claims. My outcomes: 23 reproduced, 4 partially reproduced, 2 not reproduced and 7 blocked.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| design-days-per-area | reproduced | Cell 7 gives 15/15/15 days for L Eyes, 12/12/12 for T Eyes and 5/5/5 for T Mouth. Every count matches. |
| design-sessions-per-day | partially_reproduced | Cell 9: monkey L has a mean of 6.02 control runs per day, against an expected 5 ± 0.5. Every other mean, range and the duration hold (L social 10.0, range 9–11; T social 14.0, range 14; T control 5; about 296 s). |
| fig1e-stim-counts-comparable | reproduced | Cell 12: the smallest FDR-corrected p is 0.908 for stimulations and 0.942 for shams, so all exceed 0.90. |
| figs1d-stim-counts-nonsocial | reproduced | Cell 13: no corrected p is below 0.05. Not all exceed 0.10, though: shams between monkeys give corrected p = 0.082 (OFC and dmPFC). |
| figs1e-eyes-more-than-face | reproduced | Cell 16: under both readings and both event sets, the corrected p ranges from 1.1e-7 to 4.4e-5, which is below 10⁻⁴. Eyes are higher in every case. |
| figs1e-eyes-vs-rdm-comparable | not_reproduced | Cell 17: under the deciding reading (a, the day's total), Eyes exceed RDM with corrected p of 0.0004, 0.00003 and 0.0004. Reading (b, the mean per run) gives p of 0.40–0.52 (see B1). |
| fig2a-density-map-ofc | reproduced | Cell 21: the OFC stimulation-minus-sham sum is positive in the Face and in the Eyes, under both normalisations (z-score 7.47 and 3.71; total 0.0093 and 0.0046). |
| fig2c-ofc-social-gaze-distance | reproduced | Cell 23, Methods reading: combined p = 0.00021, L p = 0.0067, T p = 0.016, all with negative medians. |
| fig2c-dmpfc-accg-no-distance-effect | reproduced | Cell 25: dmPFC p = 0.21, ACCg p = 0.39. |
| fig2e-ofc-contralateral | reproduced | Cell 28, Methods reading: contralateral p = 0.00048 (negative), ipsilateral p = 0.058, contralateral vs ipsilateral p = 0.046 with contralateral more negative. Per monkey: L 0.018/0.073, T 0.012/0.30, against the paper's 0.015/0.073 and 0.012/0.204. |
| fig2e-dmpfc-accg-no-hemifield-effect | reproduced | Cell 29: all six p are 0.10 or higher. |
| fig2f-nonsocial-no-distance-effect | reproduced | Cell 31: OFC 0.22, dmPFC 0.64, ACCg 0.50. |
| fig2gh-nonsocial-no-hemifield-effect | reproduced | Cell 32: all nine combined tests give p of 0.16 or higher. |
| methods-ofc-distance-longer-windows | reproduced | Cell 34, Methods reading. 2 s: combined 0.003, L 0.012, T 0.23. 3 s: combined 0.003, L 0.007, T 0.20. |
| methods-ofc-no-change-in-fixation-number | reproduced | Cell 37, reading (a): no per-monkey test is below 0.05 (smallest 0.121). |
| methods-ofc-longer-face-looking | partially_reproduced | Cell 39 (a): all the tests hold (OFC whole Face 0.0025, dmPFC 0.80, ACCg 0.93, OFC Eyes 0.039). Under the median reading the combined (52.8 ms) and monkey L (65.1 ms) differences fall within tolerance, but monkey T's (46.2 ms, against 39.5 ± 3.95) does not. Under the mean reading none of the three falls within tolerance. |
| methods-mouth-stimulation-no-effect | reproduced | Cell 41: 0 of 27 tests give p < 0.05, and the values are close to the paper's (1, 1, 0.19; 1, 0.125, 0.19). With 5 days this test cannot fall below 0.0625, so it is uninformative (B11). |
| methods-eyes-vs-mouth-bootstrap | not_reproduced | Cell 43: the contralateral test over all Eyes days gives p = 0.078 (a) or 0.156 (b), robust across seeds (0.059–0.070). Both hemifields combined gives 0.043 (a), where the paper has 0.799, so the pattern is inverted. Neither reading satisfies the rule. |
| fig3b-ofc-inter-looking-interval | reproduced | Cell 47: OFC p = 0.044 (stimulation shorter), dmPFC 0.77, ACCg 0.34. The result is fragile (B5). |
| ili-nonsocial-no-effect | reproduced | Cell 49: OFC 0.70, dmPFC 0.13, ACCg 0.84. |
| ili-missing-trials-41 | reproduced | Cell 51: 41.3% under reading (a) and 39.9% under (b), both within 41 ± 4.1. |
| figs3b-ili-trial-level | reproduced | Cell 54: OFC p = 0.017 (stimulation shorter), dmPFC 0.39, ACCg 0.62. |
| figs3c-reciprocation-day-level-none | reproduced | Cell 58: OFC 0.11, dmPFC 0.56, ACCg 0.32. Trials with no sequence: 86.4% (a) and 85.1% (b), both within 86 ± 8.6. |
| fig3d-ofc-reciprocation-latency | reproduced | Cell 60: OFC p = 0.023 (stimulation shorter), dmPFC 0.72, ACCg 0.36. |
| partner-monkey-unchanged | partially_reproduced | Cell 62: under reading (a) of the M2 reciprocation latency, dmPFC gives p = 0.044. The criterion needs no p < 0.05 under every reading. The distance and inter-looking-interval tests, and reading (b), all hold. |
| figs4a-causal-strength-no-stim-effect | blocked (too_large) | Cell 66 estimates 680 CPU hours with PyEMD. That is plausible, but the estimate was not done for the subsets these claims actually need (B3). |
| figs4b-causal-strength-no-epoch-effect | blocked (too_large) | Same as above. |
| epoch-days-76-of-81 | reproduced | Cell 64, reading (a): 76 days, and the five excluded are exactly the dates the code names. |
| ofc-slope-unchanged-by-epoch | blocked (too_large) | Same as above. |
| fig4c-dmpfc-slope-late-greater | blocked (too_large) | Same as above. |
| fig4d-dmpfc-slope-permutation | blocked (too_large) | Same as above. |
| dmpfc-slope-positive | blocked (too_large) | Same as above. |
| fig5a-trigger-duration-unchanged | partially_reproduced | Cell 68: OFC holds (p = 0.61 / 0.36), but dmPFC triggering fixations are longer after stimulation under both readings (p = 0.019 / 0.028; paper 0.269). |
| fig5b-pupil-unchanged | reproduced | Cell 70: 0 of 70 bins below 0.05 in each area (smallest p: 0.31, 0.51, 0.11). |
| fig5cd-saccade-counts-unchanged | blocked (other) | The archive holds no saccade events. Its metadata lists variableMeasured as SpatialSeries and EyeTracking only, and the interval tables are fixations. Gaze at 1 kHz is present, so the claim could be tested after an Otero-Millan detection run. The notebook's reason, "not_runnable", is not an allowed reason. |
| fig5e-h-saccade-kinematics-unchanged | blocked (other) | Same as above. |

## B. Problems

1. **[affects a conclusion]** Claims file, figs1e-eyes-vs-rdm-comparable. The deciding reading (a) compares day totals over 10–15 social runs with totals over about 5 control runs. That comparison is bound to differ. The paper's "all p > 0.30" fits only the per-run mean, reading (b), which gives p of 0.40–0.52 here. This looks like a misreading in the claims file. I report it and have not corrected it.
2. **[affects a conclusion]** Cell 0, saccade claims. The block reason "not_runnable" is not an allowed reason. The claims file prescribes a with_inputs run of the Otero-Millan detection, the archive holds raw 1 kHz gaze for both monkeys, and the detection software is public (listed in the paper's key resources). This was not attempted or costed.
3. **[affects a conclusion]** Cell 66, causal-decomposition cost:
   - The estimate times one 100-ensemble, single-threaded PyEMD run, multiplies it by 10, and applies it to all 19,474 social trials.
   - The epoch and slope claims (ofc-slope, fig4c, fig4d, dmpfc-slope-positive) need only the first 90 stimulation trials per day. That is about 6,840 trials over 76 days, or about 2,430 for the OFC days alone.
   - Reading (b), the Yang et al. defaults, was never timed.
   - Running in parallel, or with a faster EMD implementation, was not considered.
   
   "too_large" is plausible but not demonstrated.
4. **[does not affect a conclusion]** Cell 43. The bootstrap runs only the Methods fixation reading. The opening comment says the code's M1-only reading is shown for every distance claim. Under that reading the gap is larger (contralateral: Eyes −30.2 against Mouth −1.6 px), so the variant might differ.
5. **[does not affect a conclusion]** Cell 47, fig3b. OFC p = 0.044 depends on excluding events that start at the trial sample, which applies to 91 trials. Counting them gives p = 0.058. The strict choice follows the criterion ("starts after it"), but the result sits at the threshold.
6. **[does not affect a conclusion]** Cell 68, fig5a. 29% of trials (5,695 of 19,474) have no M1 Eyes event in progress at the trial time, even though every trial was triggered online by an Eyes fixation. The clock check (cell 5) also finds only 70.8% of trials inside an Eyes event, with 65 runs below 0.5. This selection is left uninvestigated, and the failing dmPFC test depends on it.
7. **[does not affect a conclusion]** Cell 21. The x-axis label "contra <- -> ipsi for L" is reversed: for monkey L, left (negative dx) is ipsilateral (`IPSI_SIDE`).
8. **[does not affect a conclusion]** Cell 21. The ROI masks use the first social run of each day, while the distances use each run's own ROIs. Three recalibrated days are affected.
9. **[does not affect a conclusion]** Cell 37. The combined two-monkey whole-Face fixation count at 1.5 s changes with OFC stimulation (p = 0.025, reading a). That test is outside the per-monkey criterion and the paper does not report it.
10. **[does not affect a conclusion]** `signrank`. scipy uses the exact test where MATLAB uses a normal approximation for n > 15. In a synthetic check at n = 27, the near-threshold p-values moved from 0.0436 to 0.0448, 0.0463 to 0.0475, 0.0585 to 0.0593 and 0.0187 to 0.0204. None crosses 0.05.
11. **[does not affect a conclusion]** Claims file, methods-mouth-stimulation-no-effect. With n = 5 the smallest exact two-sided p is 0.0625, so this claim of absence cannot fail.
12. **[does not affect a conclusion]** `window_pairs` offsets times by run_id × 10⁶ s. This is valid only if all times lie in [0, 10⁶) s, and the notebook never prints them. The clock-check contrast (0.708 at the true times against 0.05 when shifted) indicates the pairing is correct.
13. **[does not affect a conclusion]** `reciprocation`. When a mutual event's M1 and M2 starts are equal, the stable sort places M1 first. The tie rule is unspecified. On synthetic inputs, `window_pairs`, `trial_distance`, `first_latency` and `reciprocation` otherwise gave the expected values.

## C. Not checked, and the output that would have allowed it

- **Time magnitudes:** I could not confirm the range of trial and event times that problem 12 depends on. Printing `meta.t_first` and `meta.t_last`, and the min and max of `events.start`, would settle it.
- **Saccade data in the files:** I could not confirm there are no saccade or processing tables. Printing the set of `intervals` and `processing` group names in a file would settle it.
- **Mutual-event tables:** I could not check whether `mutual_face` means the non-eye Face (excluding Mouth) as `m1_neface` does. Comparing counts of `mutual_wholeface` with the sum of `mutual_eye`, `mutual_face` and `mutual_mouth` would show this.
- **Trigger events (fig5a):** I could not tell whether the trials with no Eyes event in progress are spread evenly. A breakdown of those trials by area and trial type would show it.
- **Bootstrap under the code reading:** this was not run, so I could not judge the variant (problem 4).
- **Causal decomposition cost:** I could not judge whether the blocked claims could have been run. Timings for reading (b), and a cost for the stimulation-trial subsets per area, would show it.
- **Extra control runs for monkey L:** I could not tell whether L's 6.02 control runs per day include runs the paper did not analyse. A per-day listing of control-run numbers for the 14 L days with 8 control runs would show it.

## End of run

15 turns, 4 minutes, result: success.
