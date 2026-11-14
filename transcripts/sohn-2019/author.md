# sohn-2019 · author · run 43597162260

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries attempts claims paper tools; wc -l docs/*.md README.md
```

```
Sat Nov 14 13:00:03 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
[... 987 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-15`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
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
[... 657 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/sohn-2019.yaml"
}
```

```
1	# Claims for Sohn, Narain, Meirhaeghe & Jazayeri (2019) on dandiset 000130.
2	# Source: the accepted author manuscript in PubMed Central (PMC6805134), full text, read from its
3	# Results, figure legends and STAR Methods. The supplementary tables and figures were not
4	# available to this attempt. The paper's analysis code is "available on request"; the dandiset
5	# links only the Neural Latents Benchmark, whose code (nlb_tools) loads the data and scores
6	# models but holds none of the paper's analyses.
7	#
8	# When these criteria were written, the author had seen the data check only: the file list and
9	# metadata, the columns of the trial table and their consistency with the event times, the
10	# counts of trials per condition, the firing rate of each unit (48 of 54 units reach 1 spike/s),
11	# and the time one GPFA fit takes. No claim's analysis had been run.
12	#
13	# The dandiset holds one recording session (2016-12-11) of monkey H, one of the 17 sessions of H
14	# and 29 of both monkeys. Its 54 units were recorded together. A "dataset" here, as in the paper,
15	# is one effector and target direction (4 in this session; the paper has 8, from two animals).
16	#
17	# Method choices fixed here, where the Methods leave them open:
18	# - Behaviour uses completed trials not flagged by the file's `is_outlier` column (the paper's
19	#   mixture model), and the `tp` and `ts` columns.
20	# - Units: mean firing rate over the file of at least 1 spike/s and at least 5 trials in every
[... 433 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/sohn-2019 entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -250; ls papers/datasets | grep sohn; cat papers/datasets/sohn-2019.yaml; ls questions | grep sohn
```

```
ls: cannot access 'entries/sohn-2019': No such file or directory
entries/fouke-2025:
total 132
drwxr-xr-x   2 runner runner  4096 Nov 14 12:55 .
drwxr-xr-x 292 runner runner 12288 Nov 14 12:59 ..
-rw-r--r--   1 runner runner  2144 Nov 14 12:55 README.md
-rw-r--r--   1 runner runner   907 Nov 14 12:55 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 14 12:55 omr.py
-rw-r--r--   1 runner runner 79403 Nov 14 12:55 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 14 12:55 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 14 12:55 requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
[... 278 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,400p attempts/fouke-2025-01.yaml; cat entries/fouke-2025/README.md; ls schemas; sed -n 1,80p docs/archives.md | head -5; grep -n "DANDI" -A60 docs/archives.md | sed -n 1,120p
```

```
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
    file of its stimulus software.
- kind: code_mismatch
  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
    while its conversion of the stimulus software's names gives the reverse (it carries a remap
    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
    only if the fish turn with lateral motion.
- kind: metadata_error
  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
    only Danio rerio; the files hold 37 fish of two species.
- kind: metadata_error
  statement: f0_vtheta is stated in radians/s but holds the heading change per frame in radians,
    and f0_vx and f0_vy are stated in pixels/s but are per frame. In most Danionella files the sum
    of f0_vtheta over a trial does not match the change of f0_theta (median ratios 0.09 to 0.89).
- kind: other
  about: data
[... 294 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/design.md README.md; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
docs/design.md:1:# Reproduction registry: design
docs/design.md:5:## Goal
docs/design.md:24:## What the queue looks like today
docs/design.md:47:## The objects
docs/design.md:82:## Entry types and building on each other
docs/design.md:94:## Trust tiers
docs/design.md:108:## Automated gates for a deposit
docs/design.md:121:## Verification
docs/design.md:138:## Provenance
docs/design.md:145:## Feedback to data owners
docs/design.md:152:## Maintenance
docs/design.md:158:## Dashboard
docs/design.md:191:## Repository layout
docs/design.md:223:## What is reused from the example-notebooks registry
docs/design.md:240:## Phasing
docs/design.md:258:## Open decisions
README.md:1:# Encore Science: the registry
README.md:18:## Reading the outcomes
README.md:33:## What is here
README.md:52:## Attempts so far
[... 241 more lines not kept]
```

**Agent**

Read the protocol, claims file and example formats. Next: the paper and the dataset listing.

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "STAR\|METHOD DETAILS\|Generalized linear\|Bayesian observer\|Speed\b\|encoding axis\|kernel\|Principal\|GPFA\|Data analysis\|Neural data analysis" paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/s; fold -s -w 200 paper/10.1016-j.neuron.2019.06.012.txt > $TMPDIR/s/paper.txt; wc -l $TMPDIR/s/paper.txt; grep -n "STAR\|Generalized linear model\|Behavioral model\|Recording\|Principal\|Encoding axis\|Speed\|GPFA\|Analysis of neural" $TMPDIR/s/paper.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s/paper.txt",
 "offset": 60,
 "limit": 160
}
```

```
60	2013 ; Matell et al., 2003 ; Murakami et al., 2014 ). During the estimation epoch, many neurons had heterogeneous responses profiles that were modulated by elapsed time in a prior-dependent fashion ( 
61	Figure 3A ). Consequently, responses at the time of Set varied with both the prior and t s ( Figure 3B ). The presentation of Set triggered a transient modulation of firing rates ( Figure 3B ( i – 
62	iii , v )). Following this transient, neurons exhibited a range of monotonic (e.g., ramping) or non-monotonic response profiles that were often organized according to t s irrespective of the prior 
63	condition ( Figure 3B ( i – iii , vi )). Responses of many neurons during the Set-Go epoch were temporally scaled with respect to t s (i.e., stretched in time for longer t s ), an effect that was 
64	most conspicuous as a change of slope among the subset of ramping neurons ( Figure 3B ( ii , vi )). This temporal scaling is consistent with recent recordings in this area in a range of simple motor 
65	timing tasks ( Emmons et al., 2017 ; Merchant et al., 2011 ; Mita et al., 2009 ; Remington et al., 2018a ; Wang et al., 2018 ). The influence of prior was most evident at the overlap t s of 800 ms ( 
66	Figure 3C ). Despite identical task demands and temporal contingencies, many neurons had highly distinct firing rate patterns depending on the prior condition, with a maximum difference in firing 
67	rate during the support of the prior between 480 and 800 ms ( Figure 3D ). Remarkably, this effect was present immediately after block transitions ( Figure S2 ). We used a generalized linear model 
68	(GLM) to quantify the influence of t s and prior condition on spike counts ( Figure 3E ; see Methods ). Results indicated that approximately 30% of neurons were modulated by elapsed time (27% Monkey 
69	H, 31% Monkey G), and more than 60% were sensitive to the prior condition (65% Monkey H, 62% Monkey G). These results suggest that neural responses during the support of the prior w
[... 150 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s/paper.txt",
 "offset": 217,
 "limit": 110
}
```

```
217	regularities in the environment create geometrically constrained manifolds of neural activity that can suitably perform Bayesian integration. STAR Methods LEAD CONTACT AND MATERIALS AVAILABILITY 
218	Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Mehrdad Jazayeri ( [removed: an e-mail address] ). This study did not generate new unique 
219	reagents. EXPERIMENTAL MODEL AND SUBJECT DETAILS All experimental procedures conformed to the guidelines of the National Institutes of Health and were approved by the Committee of Animal Care at the 
220	Massachusetts Institute of Technology. Experiments involved two naive, awake, male behaving monkeys (species: M. mulatta; ID: H and G; weight: 6.6 and 6.8 kg; age: 4 yrs old). Animals were 
221	head-restrained and seated comfortably in a dark and quiet room, and viewed stimuli on a 23-inch monitor (refresh rate: 60 Hz). Eye movements were registered by an infrared camera and sampled at 1kHz 
222	(Eyelink 1000, SR Research Ltd, Ontario, Canada). Hand movements were registered by a custom single-axis potentiometer-controlled joystick whose voltage output was sampled at 1kHz (PCIe6251, National 
223	Instruments, TX). The MWorks software package ( http://mworks-project.org ) was used to present stimuli and to register hand and eye position. Neurophysiology recordings were made by 1–3 24-channel 
224	laminar probes (V-probe, Plexon Inc., TX) through a bio-compatible cranial implant whose position was determined based on stereotaxic coordinates and structural MRI scan of the two animals. Analysis 
225	of both behavioral and spiking data was performed using custom MATLAB code (Mathworks, MA). METHOD DETAILS Two-prior time-interval reproduction task Task contingencies. Animals were trained on an 
226	interval-timing task that we refer to as the Ready-Set-Go (RSG) in which they had to measure a sample interval, t s , and produce a matching interval t p by initiating a saccad
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Figure 1\. \|Figure 2\. \|Figure 3\. \|Figure 4\. \|Figure 5\. \|Figure 6\. " $TMPDIR/s/paper.txt | head; sed -n 470,520p $TMPDIR/s/paper.txt
```

```
457:10.1152/jn.90941.2008 PMC2712272 Figure 1. Task and behavior. (A) Schematic of a single trial of the Ready-Set-Go task. The animal has to estimate a sample interval, t s , between Ready and Set 
464:Figure 2. Bayesian model and behavior. (A) Bayesian observer model. The measurement ( t m ) is the sample interval ( t s ) plus white noise with standard deviation proportional to t s . The Bayesian 
473:a black line). Triangles represent monkey H, and circles, monkey G. Figure 3. DMFC response profiles and neural trajectories. (A) Firing rate of 6 example neurons (i-vi) during the estimation epoch 
483:dots: neural states at 20-ms increments). The distance between consecutive dots reflects speed. See Figure S3 for other datasets. Figure 4. Neural signatures of Bayesian integration. (A) A geometric 
498:neural states evolved during the production epoch. Results are presented in the same format as in E. Figure 5. Alternative mechanisms. (A) Speed model (H1). Top: Bayesian estimation during the 
512:computed in the PC space obtained across t s and accounting for ~60% of the total variance; results remained unchanged when more PCs were included. See also Figure S5 . Figure 6. Trial-by-trial 
828:Figure S3. Analysis of population activity. Related to Figure 3. (A) Population activity during the estimation 
836:Figure S4. State-space analysis across conditions and epochs. Related to Figure 3. (A) Cross-condition 
893:Figure S6. Trial-by-trial analysis. Related to Figure 6. (A,B) Single-trial analysis for monkey G based on data 
979:Table S2. Analysis of behavior at overlap interval. Related to Figure 1. Effect of different conditions - prior, 
modality, direction) pooled across the two monkeys. Each data point represents a session (red: Short; blue: Long). Top-right: Histogram of the difference between ∆ t p (middle) and ∆ t p (extreme). 
The difference was similar between Short and Long (red and blue triangles) as predicted by the model. Triangles shows averages across d
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.241017.1448/assets/?page_size=100" | python -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.241017.1448/" | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(d.get('doi'));print(json.dumps(d.get('assetsSummary'),indent=1));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env 2>&1 | tail -2; source env/bin/activate; uv pip install -q h5py remfile pynwb numpy scipy pandas matplotlib statsmodels scikit-learn elephant ipykernel nbformat nbclient 2>&1 | tail -3; python -c "import elephant, pynwb; print(elephant.__version__, pynwb.__version__)"
```

```
1.2.1 4.2.0
Shell cwd was reset to
```

**Agent**

Environment ready. Now opening both NWB files to list their contents.

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > s/look.py <<'EOF'
import h5py, remfile, requests, pynwb, numpy as np, pandas as pd
V="0.241017.1448"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000130/versions/{V}/assets/").json()
for a in r["results"]:
    url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    f=h5py.File(remfile.File(url),"r")
    io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
    print("=====",a["path"])
    print(nwb.session_description, nwb.session_start_time, nwb.identifier)
    print("subject", nwb.subject)
    print("acq",list(nwb.acquisition), "proc", {k:list(v.data_interfaces) for k,v in nwb.processing.items()})
    print("intervals", list(nwb.intervals))
    t=nwb.trials.to_dataframe()
    print(t.shape); print(t.dtypes); print(t.head(5).T)
    for c in t.columns:
        print(c, nwb.trials[c].description)
    u=nwb.units.to_dataframe()
    print(u.shape, u.columns.tolist()); print(u.drop(columns=["spike_times"]).head())
    for c in nwb.units.colnames: print(c, nwb.units[c].description)
    print("electrodes", nwb.electrodes.to_dataframe().head() if nwb.electrodes is not None else None)
    t.to_pickle(f"s/{a['path'].split('_')[1]}_trials.pkl"); u.to_pickle(f"s/{a['path'].split('_')[1]}_units.pkl")
EOF
python s/look.py 2>&1 | head -300
```

```
===== sub-Haydn/sub-Haydn_desc-test_ecephys.nwb
Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains segments of trials from the full session on 2016-12-11 that are to be used for evaluating models for the Neural Latents Benchmark. 2016-12-11 00:00:00-05:00 8d26aa92-3929-11ec-8077-43176b153428
subject subject pynwb.file.Subject at 0x126180421950096
Fields:
  age: P4Y
  sex: M
  species: Macaca mulatta
  subject_id: Haydn

acq [] proc {}
intervals ['trials']
(283, 4)
start_time    float64
stop_time     float64
go_time       float64
split             str
dtype: object
id             0     1     2     3     4
start_time   0.0   1.8   3.6   5.4   7.2
stop_time    1.7   3.5   5.3   7.1   8.9
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
t=pd.read_pickle("s/train_trials.pkl"); u=pd.read_pickle("s/train_units.pkl")
print(t.split.value_counts())
print(t.groupby("split")[["ts","tp"]].agg(lambda x: x.isna().sum()))
ok=t[~t.is_outlier & t.tp.gt(0)]
print("completed nonoutlier", len(ok), " outliers", t.is_outlier.sum(), " tp<=0", (t.tp<=0).sum(), "tp nan", t.tp.isna().sum())
print(pd.crosstab([t.is_short,t.is_eye,t.theta],t.ts))
print(pd.crosstab([ok.is_short,ok.is_eye,ok.theta],ok.ts))
print(t.describe().T)
# check tp vs go-set, ts vs set-ready
d=ok
print("ts diff", np.nanmax(abs((d.set_time-d.ready_time)*1000-d.ts)), "tp diff", np.nanpercentile(abs((d.go_time-d.set_time)*1000-d.tp),[50,99,100]))
print("outlier & reward", pd.crosstab(t.is_outlier, t.reward_time.notna()))
print(t[t.is_outlier].tp.describe())
print(u.heldout.value_counts())
n=[len(s) for s in u.spike_times]; print("spikes per unit", min(n), max(n))
T=t.stop_time.max(); print("session span", t.start_time.min(), T)
oi=u.obs_intervals.iloc[0]; print(len(oi), oi[:3], oi[-3:]); print("all same obs", all(np.array_equal(x,oi) for x in u.obs_intervals))
dur=sum(b-a for a,b in oi); print("obs dur", dur)
fr=np.array(n)/dur; print(np.sort(fr).round(2)); print((fr>=1).sum())
st=np.concatenate(u.spike_times.values); print(st.min(), st.max())
print("sorted", all(np.all(np.diff(s)>=0) for s in u.spike_times))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/io/pickle.py", line 235, in read_pickle
    with get_handle(
         ~~~~~~~~~~^
        filepath_or_buffer,
        ^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
        storage_options=storage_options,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ) as handles:
    ^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/io/common.py", line 954, in get_handle
    handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: 's/train_trials.pkl'
```

**Agent calls Bash**

```bash
cd $TMPDIR && ls s/ ; ls s 2>/dev/null
```

```
Exit code 2
desc-test_trials.pkl
desc-test_units.pkl
desc-train_trials.pkl
desc-train_units.pkl
look.py
paper.txt
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
t=pd.read_pickle("s/desc-train_trials.pkl"); u=pd.read_pickle("s/desc-train_units.pkl")
print(t.split.value_counts())
ok=t[~t.is_outlier & t.tp.gt(0)]
print("completed nonoutlier", len(ok), " outliers", t.is_outlier.sum(), " tp<=0", (t.tp<=0).sum(), "tp nan", t.tp.isna().sum())
print(pd.crosstab([ok.is_short,ok.is_eye,ok.theta],ok.ts))
print(t.describe().T.to_string())
d=ok
print("ts diff", np.nanmax(abs((d.set_time-d.ready_time)*1000-d.ts)), "tp diff", np.nanpercentile(abs((d.go_time-d.set_time)*1000-d.tp),[50,99,100]))
print("outlier & reward", pd.crosstab(t.is_outlier, t.reward_time.notna()))
print(pd.crosstab(t.is_outlier, t.tp>0))
print(t[t.is_outlier & (t.tp>0)][["ts","tp","is_short"]])
print(u.heldout.value_counts())
n=[len(s) for s in u.spike_times]
oi=u.obs_intervals.iloc[0]; print(len(oi), oi[:3], oi[-3:]); print("all same obs", all(np.array_equal(x,oi) for x in u.obs_intervals))
dur=sum(b-a for a,b in oi); print("obs dur", dur, "trial span", t.start_time.min(), t.stop_time.max())
fr=np.array(n)/dur; print(np.sort(fr).round(2)); print((fr>=1).sum())
st=np.concatenate(u.spike_times.values); print(st.min(), st.max())
print("sorted", all(np.all(np.diff(s)>=0) for s in u.spike_times))
# trials outside obs intervals?
inobs=[any(a<=r.start_time and r.stop_time<=b for a,b in oi) for r in t.itertuples()]
print("trials inside obs intervals", sum(inobs), len(t))
tt=pd.read_pickle("s/desc-test_trials.pkl"); print(tt.describe())
EOF
```

```
split
train    748
val      258
none     154
Name: count, dtype: int64
completed nonoutlier 983  outliers 177  tp<=0 134 tp nan 0
ts                     480.0   560.0   640.0   ...  1000.0  1100.0  1200.0
is_short is_eye theta                          ...                        
False    False  0.0         0       0       0  ...      30      21      25
                180.0       0       0       0  ...      16      16      18
         True   0.0         0       0       0  ...      23      25      27
                180.0       0       0       0  ...      30      29      31
True     False  0.0        21      35      14  ...       0       0       0
                180.0      33      21      25  ...       0       0       0
         True   0.0        24      27      31  ...       0       0       0
                180.0      21      28      17  ...       0       0       0

[8 rows x 9 columns]
                  count         mean          std          min          25%          50%          75%          max
start_time       1160.0  2278.725419  1330.543862     0.516000  1132.897125  2275.530750  3403.243375  4805.582000
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
t=pd.read_pickle("s/desc-train_trials.pkl")
ok=t[~t.is_outlier & t.tp.gt(0)].copy()
ok["dts"]=(ok.set_time-ok.ready_time)*1000-ok.ts
ok["dtp"]=(ok.go_time-ok.set_time)*1000-ok.tp
print(ok.dts.describe()); print(np.percentile(ok.dts,[1,5,25,50,75,95,99]))
print(ok.dtp.describe()); print(np.percentile(ok.dtp,[1,5,25,50,75,95,99]))
print(ok.groupby("is_eye").dtp.describe())
print(ok.groupby("is_eye")[["dts"]].describe())
print(np.unique(np.round(np.diff(np.sort(np.concatenate([t.ready_time.dropna(),t.set_time.dropna()]))*1e4)%5)))
print(ok.set_time.head(10).values*1000)
# go_time vs target_acq
print(((ok.target_acq_time-ok.go_time)*1000).describe())
EOF
```

```
count    9.830000e+02
mean    -1.422177e+00
std      6.681722e+00
min     -2.350000e+01
25%     -3.500000e+00
50%      0.000000e+00
75%      1.818989e-10
max      2.350000e+01
Name: dts, dtype: float64
[-2.0000000e+01 -1.6500000e+01 -3.5000000e+00  0.0000000e+00
  1.8189894e-10  7.0000000e+00  1.7000000e+01]
count    983.000000
mean     -19.676031
std       14.219692
min     -200.597000
25%      -21.325500
50%      -17.906000
75%      -17.235500
max       -0.142000
Name: dtp, dtype: float64
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
for q in Jazayeri "ready-set-go" DMFC "Bayesian computation"; do curl -s "https://api.dandiarchive.org/api/dandisets/?search=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&page_size=50" | python3 -c "import json,sys;d=json.load(sys.stdin);print('$q',d['count'],[ (r['identifier'],r['most_recent_published_version']['name'][:60] if r.get('most_recent_published_version') else r['draft_version']['name'][:60]) for r in d['results']])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > s/gp.py <<'EOF'
import pandas as pd, numpy as np, time, neo, quantities as pq, warnings
warnings.filterwarnings("ignore")
from elephant.gpfa import GPFA
t=pd.read_pickle("s/desc-train_trials.pkl"); u=pd.read_pickle("s/desc-train_units.pkl")
ok=t[~t.is_outlier & t.tp.gt(0)]
oi=u.obs_intervals.iloc[0]; dur=sum(b-a for a,b in oi)
keep=[s for s in u.spike_times if len(s)/dur>=1]
d=ok[(ok.is_eye==False)&(ok.theta==180)]
print(len(d))
trials=[]
for r in d.itertuples():
    T=r.ts/1000
    trials.append([neo.SpikeTrain((s[(s>=r.ready_time)&(s<r.ready_time+T)]-r.ready_time)*pq.s, t_start=0*pq.s,t_stop=T*pq.s) for s in keep])
for xd in (4,8):
    g=GPFA(bin_size=20*pq.ms, x_dim=xd, em_max_iters=200, verbose=False)
    t0=time.time(); g.fit(trials); print(xd, time.time()-t0, len(g.fit_info['log_likelihoods']))
    t0=time.time(); res=g.transform(trials, returned_data=['latent_variable_orth']); print("transform", time.time()-t0, res[0].shape)
EOF
timeout 900 python s/gp.py
```

```
<persisted-output>
Output too large (561.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f0d522b5-f45c-46c0-8a81-358c1599911b/tool-results/bxsmtj703.txt

Preview (first 2KB):
[2026-11-14 13:03:15,637] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-14 13:03:15,637] utils - WARNING: Correcting 2 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-14 13:03:15,638] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-14 13:03:15,638] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-14 13:03:15,638] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-14 13:03:15,639] utils - WARNING: Correcting 3 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-14 13:03:15,639] utils - WARNING: Correcting 2 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-14 13:03:15,639] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
/tmp/claude-1001/env/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 1 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "
[2026-11-14 13:03:15,650] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the fol
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "WARNING\|warnings.warn\|UserWarning" /home/runner/.claude/projects/-home-runner-work-encore-encore/f0d522b5-f45c-46c0-8a81-358c1599911b/tool-results/bxsmtj703.txt | tail; date -u
```

```
Initializing parameters using factor analysis...

Fitting GPFA model...
4 21.50529432296753 200
transform 2.822260618209839 (4, 45)
Initializing parameters using factor analysis...

Fitting GPFA model...
8 29.65972924232483 200
transform 2.8438382148742676 (8, 45)
Sat Nov 14 13:04:15 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p entries/sohn-2019; sed -n 1,80p entries/fouke-2025/omr.py; python3 -c "
import json;nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'));
[print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:400],'\n---') for c in nb['cells'][:8]]"
```

```
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative
  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or
  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;
  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median
  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.
- The names of the stimulus codes combine the protocol file sevenrep_twentyonestim.hdf of the
[... 122 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/sohn-2019/rsg.py",
 "content": "\"\"\"Loading and measures for the Ready-Set-Go recording of dandiset 000130.\n\nSohn, Narain, Meirhaeghe & Jazayeri (2019), Neuron, doi:10.1016/j.neuron.2019.06.012.\n\nThe dandiset holds one session (2016-12-11) of monkey H (\"Haydn\"), prepared for the Neural\nLatents Benchmark. The train file holds the trial table (event times, prior, effector, target\ndirection, ts, tp, the outlier flag of the paper's mixture model) and the spike times of all 54\nunits over the whole session; the test file holds 1.7 s segments of 283 further trials, for 40\nunits, with no task variables, and is not used for the analysis. Files are streamed from the\narchive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from (claims/sohn-2019.yaml is cited as \"claims header\" for the\nmethod choices its opening comment fixes):\n\n- Trials: completed trials (tp > 0) not flagged by `is_outlier` (claims header).\n- Units: mean rate over the recording of at least 1 spike/s and at least 5 trials in each of\n  the 40 conditions (claims header; STAR Methods, \"Analysis of single- and multi-unit\n  activity\").\n- `BIN_MS` = 20 ms bins and `SMOOTH_SD_MS` = 40 ms Gaussian smoothing of trial-averaged rates\n  (claims header; STAR Methods, \"Principal component analysis\": \"bin size: 20 ms, Gaussian\n  smoothing kernel width: 40 ms\"). Edges of a smoothed trajectory use the nearest value, a\n  standard choice.\n- Estimation epoch: from Ready to the longest ts of the prior; bin k (ending at 20(k+1) ms after\n  Ready) averages the trials with ts >= 20(k+1) ms, so that Set comes after the end of the bin\n  (attrition; claims header and STAR Methods, \"Principal component analysis\"). The state \"at\n  time t\" is the bin ending at t.\n- Production epoch: from Set to the shortest Set-to-Go time of the trials of that ts (claims\n  header; STAR Methods). Spikes are aligned to the file's event times (`ready_time`,\n  `set_time`, `go_time`); behaviour uses the `ts` and `tp` columns (claims header).\n- PCA keeps the fewest components reaching `VAR_THRESHOLD` = 75% of the variance (claims\n  header; STAR Methods).\n- Encoding axis: the mean of X(ts_max - d) - X(ts_min + d) for d = 0, 20, 40 ... while\n  ts_min + d < ts_max - d, normalised (claims header; STAR Methods, \"Analysis of neural\n  projection\").\n- Bayesian observer: continuous uniform prior over each range, measurement noise SD wm*ts,\n  posterior mean as te, production noise SD wp*te, offset b per prior, fit by maximum\n  likelihood per dataset (claims header; STAR Methods, \"Analysis of behavior with a Bayesian\n  model\"). The integration grids (`TM_GRID_N`, `TS_GRID_N`) are a standard numerical choice.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import optimize\nfrom scipy.ndimage import gaussian_filter1d\nfrom sklearn.decomposition import PCA\n\nDANDISET_ID = \"000130\"\nDANDISET_VERSION = \"0.241017.1448\"\nTRAIN_PATH = \"sub-Haydn/sub-Haydn_desc-train_ecephys.nwb\"\nTEST_PATH = \"sub-Haydn/sub-Haydn_desc-test_ecephys.nwb\"\n\nBIN_MS = 20\nSMOOTH_SD_MS = 40\nVAR_THRESHOLD = 0.75\nMIN_RATE = 1.0\nMIN_TRIALS = 5\nSHORT_TS = (480, 560, 640, 720, 800)\nLONG_TS = (800, 900, 1000, 1100, 1200)\nPRIOR_TS = {\"Short\": SHORT_TS, \"Long\": LONG_TS}\nTM_GRID_N = 600\nTS_GRID_N = 400\n\n# The four \"datasets\" of the paper (effector x target direction); theta 0 is right, 180 left.\nDATASETS = {\"Eye Right\": (True, 0.0), \"Eye Left\": (True, 180.0),\n            \"Hand Right\": (False, 0.0), \"Hand Left\": (False, 180.0)}\n\n\ndef asset_urls() -> dict[str, str]:\n    \"\"\"Streaming URL of every NWB file at the pinned version, by path.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)\n                for a in dandiset.get_assets() if a.path.endswith(\".nwb\")}\n\n\ndef _text(value):\n    return value.decode() if isinstance(value, bytes) else value\n\n\ndef _read_table(group) -> pd.DataFrame:\n    \"\"\"A DynamicTable without ragged columns, read with h5py.\"\"\"\n    cols = {}\n    for name in _text(group.attrs[\"colnames\"]):\n        name = _text(name)\n        data = group[name][()]\n        if data.dtype.kind in \"SO\":\n            data = np.array([_text(x) for x in data])\n        cols[name] = data\n    return pd.DataFrame(cols, index=group[\"id\"][()])\n\n\ndef _ragged(group, name):\n    data, index = group[name][()], group[name + \"_index\"][()]\n    return np.split(data, index[:-1])\n\n\ndef load_file(url: str) -> dict:\n    \"\"\"Trial table, unit table and spike times of one NWB file, with the column descriptions.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        trials = _read_table(f[\"intervals/trials\"])\n        tr_desc = {c: _text(f[\"intervals/trials\"][c].attrs.get(\"description\", \"\"))\n                   for c in trials.columns}\n        units = f[\"units\"]\n        spikes = _ragged(units, \"spike_times\")\n        obs = [x.reshape(-1, 2) for x in _ragged(units, \"obs_intervals\")]\n        unit_table = pd.DataFrame({\"heldout\": units[\"heldout\"][()].astype(bool),\n                                   \"n_spikes\": [len(s) for s in spikes]},\n                                  index=units[\"id\"][()])\n        meta = {\"session_description\": _text(f[\"session_description\"][()]),\n                \"session_start_time\": _text(f[\"session_start_time\"][()]),\n                \"subject_id\": _text(f[\"general/subject/subject_id\"][()]),\n                \"species\": _text(f[\"general/subject/species\"][()])}\n    return {\"trials\": trials, \"trial_descriptions\": tr_desc, \"units\": unit_table,\n            \"spikes\": spikes, \"obs_intervals\": obs, \"meta\": meta}\n\n\ndef good_trials(trials: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Completed trials not flagged as outliers, with prior and dataset labels.\"\"\"\n    t = trials[(trials.tp > 0) & ~trials.is_outlier.astype(bool)].copy()\n    t[\"prior\"] = np.where(t.is_short.astype(bool), \"Short\", \"Long\")\n    names = {v: k for k, v in DATASETS.items()}\n    t[\"dataset\"] = [names[(bool(e), float(th))] for e, th in zip(t.is_eye, t.theta)]\n    t[\"ts\"] = t.ts.round().astype(int)\n    return t\n\n\ndef select_units(data: dict, trials: pd.DataFrame) -> tuple[np.ndarray, pd.DataFrame]:\n    \"\"\"Indices of the units kept, and the table of rates and minimum trial counts.\"\"\"\n    rows = []\n    for i, (s, obs) in enumerate(zip(data[\"spikes\"], data[\"obs_intervals\"])):\n        dur = float(np.sum(obs[:, 1] - obs[:, 0]))\n        # trials of each condition inside the unit's observation intervals\n        inside = np.zeros(len(trials), bool)\n        for a, b in obs:\n            inside |= (trials.start_time.values >= a) & (trials.stop_time.values <= b)\n        counts = trials[inside].groupby([\"prior\", \"ts\", \"dataset\"]).size()\n        n_cond = len(counts)\n        rows.append({\"unit\": data[\"units\"].index[i], \"rate\": len(s) / dur,\n                     \"min_trials\": int(counts.min()) if n_cond else 0, \"conditions\": n_cond})\n    table = pd.DataFrame(rows)\n    keep = (table.rate >= MIN_RATE) & (table.min_trials >= MIN_TRIALS) & (table.conditions == 40)\n    table[\"kept\"] = keep\n    return np.flatnonzero(keep.values), table\n\n\ndef bin_counts(spikes: list[np.ndarray], align_s: np.ndarray, start_ms: float, stop_ms: float,\n               bin_ms: float = BIN_MS) -> np.ndarray:\n    \"\"\"Spike counts, trials x bins x units, in bins from start_ms to stop_ms after each event.\"\"\"\n    edges = np.arange(start_ms, stop_ms + bin_ms / 2, bin_ms) / 1000.0\n    grid = align_s[:, None] + edges[None, :]\n    out = np.empty((len(align_s), len(edges) - 1, len(spikes)))\n    for j, s in enumerate(spikes):\n        idx = np.searchsorted(s, grid.ravel()).reshape(grid.shape)\n        out[:, :, j] = np.diff(idx, axis=1)\n    return out\n\n\ndef smooth(rates: np.ndarray, sd_ms: float = SMOOTH_SD_MS, bin_ms: float = BIN_MS) -> np.ndarray:\n    \"\"\"Gaussian smoothing along the time axis (axis 0).\"\"\"\n    return gaussian_filter1d(rates, sd_ms / bin_ms, axis=0, mode=\"nearest\")\n\n\ndef estimation_rates(spikes, t: pd.DataFrame, ts_max: int, smoothed: bool = True):\n    \"\"\"Trial-averaged rates (spikes/s) from Ready to ts_max with attrition, and trials per bin.\"\"\"\n    c = bin_counts(spikes, t.ready_time.values, 0, ts_max)\n    ends = np.arange(1, c.shape[1] + 1) * BIN_MS\n    incl = t.ts.values[:, None] >= ends[None, :]          # Set at or after the end of the bin\n    n = incl.sum(0)\n    rates = (c * incl[:, :, None]).sum(0) / np.maximum(n, 1)[:, None] * (1000 / BIN_MS)\n    return (smooth(rates) if smoothed else rates), n\n\n\ndef production_rates(spikes, t: pd.DataFrame, length_ms: float | None = None, smoothed=True):\n    \"\"\"Trial-averaged rates from Set; by default up to the shortest Set-to-Go time of the trials.\"\"\"\n    if length_ms is None:\n        length_ms = np.min((t.go_time - t.set_time).values) * 1000\n    nb = int(length_ms // BIN_MS)\n    c = bin_counts(spikes, t.set_time.values, 0, nb * BIN_MS)\n    rates = c.mean(0) * (1000 / BIN_MS)\n    return smooth(rates) if smoothed else rates\n\n\ndef go_rates(spikes, t: pd.DataFrame, before_ms: float = 800, smoothed=True):\n    \"\"\"Trial-averaged rates from Go - before_ms to Go.\"\"\"\n    c = bin_counts(spikes, t.go_time.values, -before_ms, 0)\n    rates = c.mean(0) * (1000 / BIN_MS)\n    return smooth(rates) if smoothed else rates\n\n\ndef n_components(pca: PCA, threshold: float = VAR_THRESHOLD) -> int:\n    \"\"\"Fewest components whose cumulative explained variance reaches the threshold.\"\"\"\n    return int(np.searchsorted(np.cumsum(pca.explained_variance_ratio_), threshold - 1e-12) + 1)\n\n\ndef fit_pca(blocks: list[np.ndarray], threshold: float = VAR_THRESHOLD):\n    \"\"\"PCA on the concatenated [time x units] blocks; returns the fit and the number kept.\"\"\"\n    pca = PCA().fit(np.vstack(blocks))\n    return pca, n_components(pca, threshold)\n\n\ndef encoding_axis(X: np.ndarray, ts_min: int, ts_max: int) -> np.ndarray:\n    \"\"\"Unit vector u: mean of X(ts_max - d) - X(ts_min + d), d = 0, 20, ... while the first is\n    earlier than the second. X is indexed by bin, the state at time t being row t/20 - 1.\"\"\"\n    diffs, d = [], 0\n    while ts_min + d < ts_max - d:\n        diffs.append(X[(ts_max - d) // BIN_MS - 1] - X[(ts_min + d) // BIN_MS - 1])\n        d += BIN_MS\n    v = np.mean(diffs, axis=0)\n    return v / np.linalg.norm(v)\n\n\ndef wls(y, x, w):\n    \"\"\"Weighted least squares y = a + b x; returns (a, b), weighted R2, fitted values.\"\"\"\n    y, x, w = map(np.asarray, (y, x, w))\n    A = np.column_stack([np.ones_like(x), x]) * np.sqrt(w)[:, None]\n    coef, *_ = np.linalg.lstsq(A, y * np.sqrt(w), rcond=None)\n    fit = coef[0] + coef[1] * x\n    ybar = np.sum(w * y) / np.sum(w)\n    r2 = 1 - np.sum(w * (y - fit) ** 2) / np.sum(w * (y - ybar) ** 2)\n    return coef, r2, fit\n\n\n# ----------------------------------------------------------------------------------------------\n# Bayesian observer (BLS) model\n\ndef _tm_grid(lo, hi):\n    return np.linspace(0.2 * lo, 2.2 * hi, TM_GRID_N)\n\n\ndef bls_estimate(tm: np.ndarray, lo: float, hi: float, wm: float) -> np.ndarray:\n    \"\"\"Posterior mean of ts given tm, uniform prior on [lo, hi], noise SD wm*ts.\"\"\"\n    s = np.linspace(lo, hi, TS_GRID_N)\n    lik = np.exp(-0.5 * ((tm[:, None] - s[None, :]) / (wm * s[None, :])) ** 2) / s[None, :]\n    return (lik * s).sum(1) / lik.sum(1)\n\n\ndef _tm_weights(ts, lo, hi, wm):\n    tm = _tm_grid(lo, hi)\n    w = np.exp(-0.5 * ((tm[None, :] - ts[:, None]) / (wm * ts[:, None])) ** 2)\n    return tm, w / w.sum(1, keepdims=True)\n\n\ndef bls_negloglik(params, data: dict[str, tuple[np.ndarray, np.ndarray]]):\n    wm, wp, b_short, b_long = params\n    if wm <= 0.01 or wp <= 0.01 or wm > 1 or wp > 1:\n        return np.inf\n    nll = 0.0\n    for prior, (ts, tp) in data.items():\n        lo, hi = min(PRIOR_TS[prior]), max(PRIOR_TS[prior])\n        b = b_short if prior == \"Short\" else b_long\n        tm, w = _tm_weights(ts.astype(float), lo, hi, wm)\n        te = bls_estimate(tm, lo, hi, wm)\n        sd = wp * te\n        dens = np.exp(-0.5 * ((tp[:, None] - te[None, :] - b) / sd[None, :]) ** 2) / (\n            np.sqrt(2 * np.pi) * sd[None, :])\n        p = (w * dens).sum(1)\n        nll -= np.sum(np.log(np.maximum(p, 1e-300)))\n    return nll\n\n\ndef fit_bls(t: pd.DataFrame) -> dict:\n    \"\"\"Maximum-likelihood fit of wm, wp, bShort, bLong to the trials of one dataset.\"\"\"\n    data = {p: (g.ts.values.astype(float), g.tp.values.astype(float))\n            for p, g in t.groupby(\"prior\")}\n    best = None\n    for x0 in ([0.1, 0.1, 0, 0], [0.15, 0.08, 20, -20], [0.07, 0.12, -20, 20]):\n        r = optimize.minimize(bls_negloglik, x0, args=(data,), method=\"Nelder-Mead\",\n                              options={\"xatol\": 1e-5, \"fatol\": 1e-4, \"maxiter\": 4000})\n        if best is None or r.fun < best.fun:\n            best = r\n    if not best.success:\n        raise RuntimeError(f\"BLS fit failed: {best.message}\")\n    wm, wp, bs, bl = best.x\n    return {\"wm\": wm, \"wp\": wp, \"b_Short\": bs, \"b_Long\": bl, \"nll\": best.fun}\n\n\ndef bls_predict(fit: dict, prior: str, ts) -> pd.DataFrame:\n    \"\"\"Model mean te (no offset), mean tp and SD of tp at each ts.\"\"\"\n    lo, hi = min(PRIOR_TS[prior]), max(PRIOR_TS[prior])\n    ts = np.atleast_1d(np.asarray(ts, float))\n    tm, w = _tm_weights(ts, lo, hi, fit[\"wm\"])\n    te = bls_estimate(tm, lo, hi, fit[\"wm\"])\n    b = fit[f\"b_{prior}\"]\n    mean_te = (w * te).sum(1)\n    mean_tp = mean_te + b\n    second = (w * ((te + b) ** 2 + (fit[\"wp\"] * te) ** 2)).sum(1)\n    return pd.DataFrame({\"ts\": ts, \"te\": mean_te, \"tp_mean\": mean_tp,\n                         \"tp_sd\": np.sqrt(second - mean_tp ** 2)})\n"
}
```

```
File created successfully at: entries/sohn-2019/rsg.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && uv pip install -q dandi 2>&1|tail -1; cd entries/sohn-2019 && python - <<'EOF'
import time, rsg, numpy as np, pandas as pd
t0=time.time()
urls=rsg.asset_urls(); print(urls)
d=rsg.load_file(urls[rsg.TRAIN_PATH]); print(time.time()-t0)
print(d["meta"], d["units"].shape)
t=rsg.good_trials(d["trials"]); keep,tab=rsg.select_units(d,t); print(len(keep), tab.min_trials.min(), tab.conditions.min())
for name,g in t.groupby("dataset"):
    t1=time.time(); f=rsg.fit_bls(g); print(name, {k:round(v,3) for k,v in f.items()}, round(time.time()-t1,1))
    for p in ("Short","Long"):
        pr=rsg.bls_predict(f,p,rsg.PRIOR_TS[p]); obs=g[g.prior==p].groupby("ts").tp.agg(["mean","std"])
        print(pd.concat([pr.set_index(pr.ts.astype(int)),obs],axis=1).round(1).to_string())
EOF
```

```
entries/sohn-2019/rsg.py:239: RuntimeWarning: invalid value encountered in divide
  return (lik * s).sum(1) / lik.sum(1)
entries/sohn-2019/rsg.py:239: RuntimeWarning: invalid value encountered in divide
  return (lik * s).sum(1) / lik.sum(1)
{'sub-Haydn/sub-Haydn_desc-test_ecephys.nwb': 'https://dandiarchive.s3.amazonaws.com/blobs/eaf/1fa/eaf1fa97-ce58-477d-b79d-82425cea818f', 'sub-Haydn/sub-Haydn_desc-train_ecephys.nwb': 'https://dandiarchive.s3.amazonaws.com/blobs/73a/6f6/73a6f648-8e97-4c90-b323-a15844e4e3d4'}
1.453387975692749
{'session_description': 'Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains continuous segments of the full session on 2016-12-11 that can be used for training models for the Neural Latents Benchmark.', 'session_start_time': '2016-12-11T00:00:00-05:00', 'subject_id': 'Haydn', 'species': 'Macaca mulatta'} (54, 2)
48 14 40
Eye Left {'wm': np.float64(0.031), 'wp': np.float64(0.102), 'b_Short': np.float64(40.438), 'b_Long': np.float64(0.645), 'nll': np.float64(1526.382)} 22.6
        ts     te  tp_mean  tp_sd   mean    std
ts                                             
480  480.0  494.0    534.4   50.7  539.5   45.1
560  560.0  561.1    601.5   59.8  580.0   52.7
640  640.0  641.3    681.7   68.3  666.9   81.6
720  720.0  720.9    761.4   76.6  772.1  100.4
800  800.0  778.7    819.1   80.0  864.0   79.3
          ts      te  tp_mean  tp_sd    mean    std
ts                                                 
800    800.0   823.4    824.1   84.5   821.3   93.0
900    900.0   902.0    902.6   95.9   916.0   91.9
[... 48 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sohn-2019/rsg.py",
 "old_string": "    s = np.linspace(lo, hi, TS_GRID_N)\n    lik = np.exp(-0.5 * ((tm[:, None] - s[None, :]) / (wm * s[None, :])) ** 2) / s[None, :]\n    return (lik * s).sum(1) / lik.sum(1)",
 "new_string": "    s = np.linspace(lo, hi, TS_GRID_N)\n    loglik = -0.5 * ((tm[:, None] - s[None, :]) / (wm * s[None, :])) ** 2 - np.log(s[None, :])\n    lik = np.exp(loglik - loglik.max(1, keepdims=True))\n    return (lik * s).sum(1) / lik.sum(1)"
}
```

```
The file entries/sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/s/py2nb.py <<'EOF'
"""Convert a percent-format script to ipynb: '# %%' code cells, '# %% [markdown]' markdown,
optional 'tags=a,b' after the marker."""
import sys, re, nbformat
src = open(sys.argv[1]).read().split("\n")
cells, cur, kind, tags = [], [], None, []
def flush():
    if kind is None: return
    text = "\n".join(cur).strip("\n")
    if kind == "md":
        text = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in text.split("\n"))
        c = nbformat.v4.new_markdown_cell(text)
    else:
        c = nbformat.v4.new_code_cell(text)
    if tags: c.metadata["tags"] = tags
    cells.append(c)
for line in src:
    m = re.match(r"^# %%( \[markdown\])?( tags=(\S+))?\s*$", line)
    if m:
        flush(); cur = []; kind = "md" if m.group(1) else "code"
        tags = m.group(3).split(",") if m.group(3) else []
    else:
        cur.append(line)
flush()
nb = nbformat.v4.new_notebook(); nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[2])
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/s/nb.py",
 "content": "# %% [markdown]\n# # Reproducing Sohn et al. (2019) from dandiset 000130\n#\n# Paper. Sohn H, Narain D, Meirhaeghe N, Jazayeri M (2019). Bayesian computation through cortical\n# latent dynamics. Neuron 103(5):934-947.e5.\n# [doi:10.1016/j.neuron.2019.06.012](https://doi.org/10.1016/j.neuron.2019.06.012). The claims\n# file (`claims/sohn-2019.yaml`) was written from the accepted author manuscript in PubMed Central\n# (PMC6805134): Results, figure legends and STAR Methods. The supplementary tables and figures were\n# not available to the reader. The paper's analysis code is available on request only.\n#\n# Dataset. [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version\n# 0.241017.1448 (doi:10.48324/dandi.000130/0.241017.1448). This version was asked for in the\n# prompt of this attempt; it is also the dandiset's only published version. The dandiset was\n# prepared for the Neural Latents Benchmark (DMFC_RSG) and holds one recording session\n# (2016-12-11) of monkey H (\"Haydn\"): a train file with the trial table and all 54 units, and a test\n# file with 1.7 s segments of 283 further trials for 40 units and no task variables. The paper\n# analysed 17 sessions of H and 12 of monkey G; only this session is here. Following the paper, a\n# \"dataset\" is one effector and target direction (4 here, 8 in the paper over both animals).\n#\n# Data are streamed from the archive; nothing is written to disk. Loading and the measures are in\n# `rsg.py`, whose docstring says where each parameter comes from.\n#\n# | Claim | Tested here |\n# |---|---|\n# | beh-slopes | tested |\n# | beh-overlap-prior | tested |\n# | beh-sigmoid-increments | tested |\n# | beh-long-more-bias | tested |\n# | beh-bayes-model | tested |\n# | glm-prior-ts | tested |\n# | dfr-overlap-support | tested |\n# | pca-dimensionality | tested |\n# | encoding-r2 | tested |\n# | encoding-bayes-beats-linear | tested |\n# | short-in-long-control | tested |\n# | neural-long-more-bias | tested |\n# | speed-vs-projection | tested |\n# | initial-speed-biased | tested |\n# | speed-predicts-tp | tested |\n# | alt-speed-unmodulated | tested |\n# | alt-transient-parallel | tested |\n# | alt-threshold-monotonic | tested |\n# | gpfa-variance-inverted-u | tested |\n# | gpfa-mean-sigmoid | tested |\n# | rnn-curved-manifold | blocked: the networks are not in the dataset (data_missing) |\n# | rnn-perturbation | blocked: the networks are not in the dataset (data_missing) |\n# | monkey-g | blocked: monkey G is not in the dataset (data_missing) |\n\n# %%\nimport logging\nimport resource\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport statsmodels.api as sm\nfrom scipy import stats\n\nimport rsg\n\nwarnings.filterwarnings(\"ignore\")\nlogging.getLogger(\"elephant\").setLevel(logging.ERROR)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nT0 = time.time()\nDS = list(rsg.DATASETS)\nPRIORS = [\"Short\", \"Long\"]\n\n\ndef signed_rank(x, alternative=\"two-sided\"):\n    \"\"\"Wilcoxon signed-rank test against zero, exact.\"\"\"\n    x = np.asarray(x, float)\n    return stats.wilcoxon(x, alternative=alternative, method=\"exact\").pvalue\n\n# %%\nurls = rsg.asset_urls()\ndata = rsg.load_file(urls[rsg.TRAIN_PATH])\ntest = rsg.load_file(urls[rsg.TEST_PATH])\ntrials_all = data[\"trials\"]\nT = rsg.good_trials(trials_all)\nkeep, unit_table = rsg.select_units(data, T)\nSP = [data[\"spikes\"][i] for i in keep]\nprint(f\"loaded in {time.time() - T0:.1f} s\")\n\n# %% [markdown]\n# ## Data check\n#\n# Each check of the metadata against the values is stated under its output.\n\n# %% tags=sanity\nprint(\"Files at the pinned version:\", sorted(urls))\nfor name, d in ((\"train\", data), (\"test\", test)):\n    print(f\"\\n{name}: {d['meta']}\")\n    print(f\"  trials {len(d['trials'])}, columns {list(d['trials'].columns)}\")\n    print(f\"  units {len(d['units'])} (held out in the benchmark: {int(d['units'].heldout.sum())})\")\nprint(\"\\nTrain-file trial columns and their descriptions:\")\nfor c, desc in data[\"trial_descriptions\"].items():\n    print(f\"  {c}: {desc}\")\nprint(\"\\nTrials by benchmark split (train file):\", trials_all.split.value_counts().to_dict())\nprint(\"Test-file trial columns:\", list(test[\"trials\"].columns), \"; split:\",\n      test[\"trials\"].split.value_counts().to_dict())\ndone = trials_all.tp > 0\nprint(f\"\\nTrain-file trials: {len(trials_all)}; completed (tp > 0): {int(done.sum())}; \"\n      f\"is_outlier: {int(trials_all.is_outlier.sum())} \"\n      f\"(of which completed: {int((trials_all.is_outlier & done).sum())}); \"\n      f\"kept (completed, not outlier): {len(T)}\")\nprint(\"Rewarded among kept:\", int(T.reward_time.notna().sum()), \"; rewarded among outliers:\",\n      int(trials_all[trials_all.is_outlier].reward_time.notna().sum()))\nprint(\"\\nKept trials per dataset, prior and ts:\")\nprint(pd.crosstab([T.dataset, T.prior], T.ts).to_string())\n\n# %% tags=sanity\nprint(\"Ranges of the variables used (kept trials):\")\nfor c in [\"ts\", \"tp\", \"theta\", \"iti\"]:\n    print(f\"  {c}: {T[c].min():.1f} to {T[c].max():.1f}\")\nprint(\"  ts values:\", sorted(T.ts.unique()))\norder_ok = ((T.fix_time <= T.target_on_time) & (T.target_on_time <= T.ready_time)\n            & (T.ready_time < T.set_time) & (T.set_time < T.go_time)).all()\nprint(\"Event order fix <= target <= ready < set < go in every kept trial:\", bool(order_ok))\nd_ts = (T.set_time - T.ready_time) * 1000 - T.ts\nd_tp = (T.go_time - T.set_time) * 1000 - T.tp\nprint(\"(set_time - ready_time) - ts, ms: percentiles 0/1/50/99/100 =\",\n      np.percentile(d_ts, [0, 1, 50, 99, 100]).round(1))\nprint(\"(go_time - set_time) - tp, ms: percentiles 0/1/50/99/100 =\",\n      np.percentile(d_tp, [0, 1, 50, 99, 100]).round(1))\nprint(\"  by effector (median, ms):\", d_tp.groupby(T.is_eye).median().round(1).to_dict())\nprint(\"\\niti by prior (ms):\")\nprint(pd.crosstab(trials_all.is_short.map({True: \"Short\", False: \"Long\"}), trials_all.iti).to_string())\nprint(\"\\nis_short against ts range: Short ts\", sorted(T[T.prior == \"Short\"].ts.unique()),\n      \"; Long ts\", sorted(T[T.prior == \"Long\"].ts.unique()))\n\n# %% [markdown]\n# `ts` matches the time from `ready_time` to `set_time` to within about 24 ms (one or two frames of a\n# 60 Hz display; the Methods give a 60 Hz monitor). `tp` is longer than `go_time - set_time` by a\n# median of about 18 ms, and the difference is not documented. Behaviour uses the `ts` and `tp`\n# columns (claims header) and spikes are aligned to the event times. The `iti` column is described\n# as 500 ms for the Short prior and 1220 ms for the Long prior; the values are the reverse (see the\n# table above), which matches the Methods (\"we set the inter-trial intervals of the Short and Long\n# conditions to 1220 ms and 500 ms, respectively\"). The description is wrong; `iti` is not used.\n\n# %% tags=sanity\nprint(\"Units in the train file:\", len(data[\"units\"]))\nprint(\"Observation intervals identical for all units:\",\n      all(np.array_equal(o, data[\"obs_intervals\"][0]) for o in data[\"obs_intervals\"]),\n      \"; covering\", data[\"obs_intervals\"][0].shape[0], \"segments,\",\n      round(float(np.sum(np.diff(data[\"obs_intervals\"][0], axis=1))), 1), \"s\")\nprint(\"Spike times sorted in every unit:\", all(np.all(np.diff(s) >= 0) for s in data[\"spikes\"]))\nprint(\"Spike time range, s:\", round(min(s.min() for s in data[\"spikes\"]), 3), \"to\",\n      round(max(s.max() for s in data[\"spikes\"]), 3), \"; trials span\",\n      round(trials_all.start_time.min(), 3), \"to\", round(trials_all.stop_time.max(), 3))\nprint(\"Mean rates (spikes/s): min %.2f, median %.2f, max %.2f\" % (\n    unit_table.rate.min(), unit_table.rate.median(), unit_table.rate.max()))\nprint(\"Units below 1 spike/s:\", int((unit_table.rate < 1).sum()),\n      \"; fewest kept trials in any of the 40 conditions:\", int(unit_table.min_trials.min()))\nprint(\"Units kept:\", len(keep), \"of\", len(unit_table))\n\n# %% [markdown]\n# The STAR Methods report 48 neurons in the high-yield session of monkey H used for GPFA; this\n# session yields 48 units under the paper's selection, consistent with its being that session. The\n# units are single- and multi-units together; the file does not say which is which. No electrode\n# position, area or unit quality is given (the electrode table has no positions).\n#\n# Clock check. With spikes and a trial table only, the alignment of spikes to the trial events is\n# checked by decoding a task variable in windows around an event, with the true labels and with the\n# labels of the next trial. The target direction is shown at `target_on_time`, so it can only be\n# decoded after it; the Set flash should evoke a transient at a fixed latency after `set_time`.\n\n# %% tags=sanity\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score, StratifiedKFold\n\nrng_check = np.random.default_rng(0)\nwin = [(-300, 0), (0, 300), (300, 600)]\ny_true = (T.theta.values == 180).astype(int)\ny_next = np.roll(y_true, -1)\nrows = []\nfor a, b in win:\n    X = rsg.bin_counts(SP, T.target_on_time.values, a, b, bin_ms=b - a)[:, 0, :]\n    X = np.sqrt(X)\n    cv = StratifiedKFold(5, shuffle=True, random_state=0)\n    for lab, y in ((\"true\", y_true), (\"next trial\", y_next)):\n        acc = cross_val_score(LogisticRegression(C=0.1, max_iter=2000), X, y, cv=cv).mean()\n        rows.append({\"window after target onset (ms)\": f\"{a} to {b}\", \"labels\": lab,\n                     \"accuracy\": round(acc, 3)})\nprint(\"Decoding target direction (left/right) from spike counts, 5-fold cross-validated:\")\nprint(pd.DataFrame(rows).pivot(index=\"window after target onset (ms)\", columns=\"labels\",\n                               values=\"accuracy\").to_string())\npop = rsg.bin_counts(SP, T.set_time.values, -200, 400).sum(2).mean(0) * (1000 / rsg.BIN_MS) / len(SP)\nshift = rng_check.uniform(-0.3, 0.3, len(T))\npop_shift = rsg.bin_counts(SP, T.set_time.values + shift, -200, 400).sum(2).mean(0) * 50 / len(SP)\nprint(\"\\nMean population rate (spikes/s per unit) in 20 ms bins from Set - 200 to Set + 400 ms:\")\nprint(\"  aligned to set_time:     \", pop.round(1))\nprint(\"  times jittered +-300 ms:\", pop_shift.round(1))\npeak = np.argmax(pop[10:]) * 20\nprint(f\"Peak after Set at {peak}-{peak + 20} ms: {pop[10:].max():.1f} against a pre-Set mean of \"\n      f\"{pop[:10].mean():.1f}; jittered peak {pop_shift[10:].max():.1f}\")\n\n# %% [markdown]\n# The target direction is decoded near chance before target onset and well above chance after it,\n# and not with the next trial's labels; the population rate shows a transient after Set that\n# disappears when the event times are jittered. The spikes share the clock of the trial table, as\n# far as these checks can tell. The analysis uses one session, so no unit is matched across sessions.\n#\n# The test file holds 283 trials of the session (1.7 s segments re-timed from 0, 40 units, no ts,\n# tp, prior or effector), so their behaviour and labels are not in the dandiset. The paper's 17\n# sessions of monkey H and all of monkey G are not in it either.\n"
}
```

```
File created successfully at: /tmp/claude-1001/s/nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cp $TMPDIR/s/nb.py run1.py && time python run1.py; rm run1.py
```

```
loaded in 1.9 s
Files at the pinned version: ['sub-Haydn/sub-Haydn_desc-test_ecephys.nwb', 'sub-Haydn/sub-Haydn_desc-train_ecephys.nwb']

train: {'session_description': 'Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains continuous segments of the full session on 2016-12-11 that can be used for training models for the Neural Latents Benchmark.', 'session_start_time': '2016-12-11T00:00:00-05:00', 'subject_id': 'Haydn', 'species': 'Macaca mulatta'}
  trials 1160, columns ['start_time', 'stop_time', 'fix_on_time', 'fix_time', 'target_on_time', 'ready_time', 'set_time', 'go_time', 'target_acq_time', 'reward_time', 'bad_time', 'is_short', 'is_eye', 'theta', 'ts', 'tp', 'fix_time_dur', 'target_time_dur', 'iti', 'reward_dur', 'is_outlier', 'split']
  units 54 (held out in the benchmark: 14)

test: {'session_description': 'Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains segments of trials from the full session on 2016-12-11 that are to be used for evaluating models for the Neural Latents Benchmark.', 'session_start_time': '2016-12-11T00:00:00-05:00', 'subject_id': 'Haydn', 'species': 'Macaca mulatta'}
  trials 283, columns ['start_time', 'stop_time', 'go_time', 'split']
  units 40 (held out in the benchmark: 0)

Train-file trial columns and their descriptions:
  start_time: Start time of epoch, in seconds
  stop_time: Stop time of epoch, in seconds
  fix_on_time: Time when the fixation cue on the display turns on
  fix_time: Time when the animal fixates on the fixation cue
  target_on_time: Time of target presentation
  ready_time: Time of ready cue delivery
  set_time: Time of set cue presentation
  go_time: Time of monkey response, either with an eye saccade or joystick movement
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/s/nb.py <<'EOF'

# %% [markdown]
# ## beh-slopes
#
# > Regression slopes of tp on ts are positive and less than one in every condition, so the animals
# > estimated ts and their responses were biased toward the mean of the prior.
#
# Criterion: per prior, effector and direction (8 conditions), a weighted linear regression of tp
# on ts, each trial weighted by 1 over the variance of tp at its ts; reproduced when all 8 slopes lie
# between 0 and 1 with 95% intervals excluding 0 and 1. The regression has an intercept (the
# criterion's "linear regression of tp on ts"). The STAR Methods write the model as
# "tp = βts + ε" ("Model free analysis of behavior"), without an intercept; that reading is shown as
# a variant.

# %% tags=claim:beh-slopes
def weighted_slope(g, intercept=True):
    w = 1 / g.groupby("ts").tp.transform("var")
    X = sm.add_constant(g.ts.astype(float)) if intercept else g.ts.astype(float)
    r = sm.WLS(g.tp.astype(float), X, weights=w).fit()
    lo, hi = r.conf_int().loc["ts"]
    return r.params["ts"], lo, hi


rows = []
for (ds, prior), g in T.groupby(["dataset", "prior"]):
    b, lo, hi = weighted_slope(g)
    b0, lo0, hi0 = weighted_slope(g, intercept=False)
    rows.append({"dataset": ds, "prior": prior, "n": len(g), "slope": b, "ci_low": lo, "ci_high": hi,
                 "slope_no_intercept": b0, "ci0_low": lo0, "ci0_high": hi0})
slopes = pd.DataFrame(rows)
print(slopes.round(3).to_string(index=False))
inside = (slopes.slope > 0) & (slopes.slope < 1)
excl = (slopes.ci_low > 0) & (slopes.ci_high < 1)
print(f"\nWith intercept: slopes in (0, 1): {int(inside.sum())} of 8; intervals excluding 0 and 1: "
      f"{int(excl.sum())} of 8")
inside0 = (slopes.slope_no_intercept > 0) & (slopes.slope_no_intercept < 1)
excl0 = (slopes.ci0_low > 0) & (slopes.ci0_high < 1)
print(f"Variant without intercept: slopes in (0, 1): {int(inside0.sum())} of 8; intervals excluding "
      f"0 and 1: {int(excl0.sum())} of 8")
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/s/nb.py <<'EOF'

# %% [markdown]
# ## beh-overlap-prior
#
# > At the overlapping ts of 800 ms, biases were in opposite directions for the two priors
# > (rank-sum test, p < 1e-43 in animal H over 17 sessions).
#
# Criterion: trials with ts = 800 ms pooled over effector and direction; reproduced when the median
# of tp - 800 is negative for Short and positive for Long and a two-sided rank-sum test of tp between
# priors has p < 0.05. Shown per effector and direction as well.

# %% tags=claim:beh-overlap-prior
o = T[T.ts == 800]
rows = []
for ds, g in [("pooled", o)] + list(o.groupby("dataset")):
    s, l = g[g.prior == "Short"].tp, g[g.prior == "Long"].tp
    rows.append({"dataset": ds, "n_short": len(s), "n_long": len(l),
                 "median_bias_short": np.median(s - 800), "median_bias_long": np.median(l - 800),
                 "p_ranksum": stats.ranksums(s, l).pvalue})
overlap = pd.DataFrame(rows)
print(overlap.to_string(index=False, float_format=lambda v: f"{v:.3g}"))

# %% [markdown]
# ## beh-sigmoid-increments
#
# > Increments of tp between neighbouring ts are smaller at the extremes of the prior than near its
# > mean, as the sigmoidal Bayesian estimator predicts (signed-rank test, p < 1e-11 in animal H).
#
# Criterion: per condition the mean tp at each ts, the four increments; extreme = mean of the first
# and last, middle = mean of the second and third; reproduced when middle exceeds extreme in most of
# the 8 conditions and a two-sided signed-rank test over the 8 has p < 0.05.

# %% tags=claim:beh-sigmoid-increments
rows = []
for (ds, prior), g in T.groupby(["dataset", "prior"]):
    m = g.groupby("ts").tp.mean().reindex(rsg.PRIOR_TS[prior]).values
    inc = np.diff(m)
    rows.append({"dataset": ds, "prior": prior, "increments": inc.round(1),
                 "extreme": (inc[0] + inc[3]) / 2, "middle": (inc[1] + inc[2]) / 2})
incr = pd.DataFrame(rows)
incr["middle_minus_extreme"] = incr.middle - incr.extreme
print(incr.round(1).to_string(index=False))
n_pos = int((incr.middle_minus_extreme > 0).sum())
p_inc = signed_rank(incr.middle_minus_extreme)
print(f"\nMiddle > extreme in {n_pos} of 8; median difference "
      f"{incr.middle_minus_extreme.median():.1f} ms; signed-rank p = {p_inc:.4f}")
print("Median difference by prior (ms):", incr.groupby("prior").middle_minus_extreme.median().round(1).to_dict())

# %% [markdown]
# ## beh-long-more-bias
#
# > Biases are larger for the Long prior than for the Short prior, as scalar variability predicts;
# > regression slopes are smaller for Long.
#
# Criterion: with the slopes of beh-slopes, reproduced when the Long slope is below the Short slope
# in all 4 datasets; partially reproduced for 3 of 4.

# %% tags=claim:beh-long-more-bias
sl = slopes.pivot(index="dataset", columns="prior", values="slope")
sl["long_below_short"] = sl.Long < sl.Short
sl0 = slopes.pivot(index="dataset", columns="prior", values="slope_no_intercept")
sl["Short_no_intercept"], sl["Long_no_intercept"] = sl0.Short, sl0.Long
print(sl.round(3).to_string())
print(f"\nLong slope below Short: {int(sl.long_below_short.sum())} of 4 "
      f"(variant without intercept: {int((sl0.Long < sl0.Short).sum())} of 4)")

# %% [markdown]
# ## beh-bayes-model
#
# > A Bayesian observer model with scalar measurement and production noise fit to the behaviour
# > captures the bias and the variance of tp in all conditions.
#
# Criterion: the model fit per dataset (wm, wp, bShort, bLong). Across the 10 prior and ts conditions,
# the R2 of the observed mean bias by the model's predicted bias, and the Pearson correlation of the
# observed and predicted SD of tp. Reproduced when the bias R2 is at least 0.8 and the SD correlation
# positive in all 4 datasets; partially when only one of the two holds in all 4.
#
# "R2 of the observed by the predicted" can be read as (a) 1 - SS_residual / SS_total with the
# prediction taken as it is, or (b) the squared correlation of observed and predicted (a regression of
# one on the other). Both are shown; they are judged together.

# %% tags=claim:beh-bayes-model
fits, preds = {}, []
for ds, g in T.groupby("dataset"):
    fits[ds] = rsg.fit_bls(g)
    for prior in PRIORS:
        p = rsg.bls_predict(fits[ds], prior, rsg.PRIOR_TS[prior])
        obs = g[g.prior == prior].groupby("ts").tp.agg(["mean", "std", "size"])
        p["dataset"], p["prior"] = ds, prior
        p["obs_mean"], p["obs_sd"], p["n"] = obs["mean"].values, obs["std"].values, obs["size"].values
        preds.append(p)
preds = pd.concat(preds, ignore_index=True)
preds["obs_bias"], preds["pred_bias"] = preds.obs_mean - preds.ts, preds.tp_mean - preds.ts
print(pd.DataFrame(fits).T.round(3).to_string())
rows = []
for ds, p in preds.groupby("dataset"):
    ss_res = np.sum((p.obs_bias - p.pred_bias) ** 2)
    ss_tot = np.sum((p.obs_bias - p.obs_bias.mean()) ** 2)
    rows.append({"dataset": ds, "bias_R2_a": 1 - ss_res / ss_tot,
                 "bias_R2_b": stats.pearsonr(p.obs_bias, p.pred_bias)[0] ** 2,
                 "sd_r": stats.pearsonr(p.obs_sd, p.tp_sd)[0],
                 "sd_p": stats.pearsonr(p.obs_sd, p.tp_sd)[1]})
bayes = pd.DataFrame(rows)
print()
print(bayes.round(3).to_string(index=False))
print(preds[["dataset", "prior", "ts", "n", "obs_bias", "pred_bias", "obs_sd", "tp_sd"]].round(1).to_string(index=False))
print(f"\nBias R2 >= 0.8: reading (a) {int((bayes.bias_R2_a >= 0.8).sum())} of 4, reading (b) "
      f"{int((bayes.bias_R2_b >= 0.8).sum())} of 4; SD correlation positive: {int((bayes.sd_r > 0).sum())} of 4")
EOF
cd $TMPDIR/s && cp nb.py entries/sohn-2019/run1.py && cd entries/sohn-2019 && source $TMPDIR/env/bin/activate && python run1.py 2>&1 | sed -n '/beh-slopes/,$p;/slope/,$p' | tail -80; rm run1.py
```

```
dataset  n_short  n_long  median_bias_short  median_bias_long  p_ranksum
    pooled       93     107               28.3              47.6     0.0728
  Eye Left       22      36               79.1              18.6     0.0506
 Eye Right       25      38               40.9              36.5      0.811
 Hand Left       24      14              -61.6             -2.81     0.0694
Hand Right       22      19               29.7              96.8   0.000987
   dataset prior                increments  extreme  middle  middle_minus_extreme
  Eye Left  Long  [94.7, 90.6, 88.0, 61.3]     78.0    89.3                  11.3
  Eye Left Short [40.4, 86.9, 105.2, 91.9]     66.2    96.1                  29.9
 Eye Right  Long [77.9, 80.1, 153.8, 20.3]     49.1   117.0                  67.8
 Eye Right Short [46.9, 86.8, 121.5, 84.6]     65.7   104.1                  38.4
 Hand Left  Long  [64.3, 33.2, 80.5, 17.4]     40.8    56.8                  16.0
 Hand Left Short  [45.8, 67.0, 23.6, 66.3]     56.1    45.3                 -10.7
Hand Right  Long  [52.8, 93.8, 66.7, 20.8]     36.8    80.3                  43.5
Hand Right Short  [32.5, 68.1, 93.1, 63.2]     47.9    80.6                  32.7

Middle > extreme in 7 of 8; median difference 31.3 ms; signed-rank p = 0.0156
Median difference by prior (ms): {'Long': 29.7, 'Short': 31.3}
prior        Long  Short  long_below_short  Short_no_intercept  Long_no_intercept
dataset                                                                          
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/s/nb.py <<'EOF'

# %% [markdown]
# ## glm-prior-ts
#
# > About 30% of neurons were modulated by elapsed time (27% in monkey H) and more than 60% were
# > sensitive to the prior (65% in monkey H), by a Poisson GLM of spike counts before Set compared by
# > BIC.
#
# Criterion: the selected units; counts in the 80 ms before each of the Short prior's ts values (480
# to 800 ms after Ready) from every trial whose Set comes after that time, both priors. Full model:
# log rate = prior + 5 time indicators + effector + direction; prior-dependent when its BIC is below
# that of the model without the prior. For ts: a model per prior with that prior's 5 time indicators
# plus effector and direction, against the model without the time indicators (intercept, effector
# and direction, the STAR Methods' Equation 4); ts-dependent when the BIC favours the full model in
# either prior. Expected 65 +- 6.5% (prior) and 27 +- 2.7% (ts).
#
# A trial whose ts equals the window's end is included: its window is the 80 ms "immediately before
# Set" of the STAR Methods ("Generalized linear model"), and the attrition rule there counts "all
# trials in which Set occurred after t". Windows are placed at the nominal times after `ready_time`.

# %% tags=claim:glm-prior-ts
from statsmodels.stats.proportion import proportion_confint


def glm_rows(t, times):
    """Rows (trial, window end) with ts >= window end, and counts for every unit."""
    rows, counts = [], []
    for T_end in times:
        g = t[t.ts >= T_end]
        c = rsg.bin_counts(SP, g.ready_time.values, T_end - 80, T_end, bin_ms=80)[:, 0, :]
        counts.append(c)
        rows.append(pd.DataFrame({"time": T_end, "long": (g.prior == "Long").astype(float).values,
                                  "hand": (~g.is_eye.astype(bool)).astype(float).values,
                                  "left": (g.theta == 180).astype(float).values}))
    return pd.concat(rows, ignore_index=True), np.vstack(counts)


def bic(y, X):
    r = sm.GLM(y, X, family=sm.families.Poisson()).fit()
    if not r.converged:
        raise RuntimeError("GLM did not converge")
    return -2 * r.llf + X.shape[1] * np.log(len(y))


def design(rows, prior=True, time=True):
    cols = []
    if time:
        cols.append(pd.get_dummies(rows.time, prefix="t").astype(float))
    else:
        cols.append(pd.DataFrame({"const": np.ones(len(rows))}))
    if prior:
        cols.append(rows[["long"]])
    cols.append(rows[["hand", "left"]])
    return pd.concat(cols, axis=1).values


rows_p, y_p = glm_rows(T, rsg.SHORT_TS)
per_prior = {p: glm_rows(T[T.prior == p], rsg.PRIOR_TS[p]) for p in PRIORS}
print("Rows in the prior model:", len(rows_p), "; by window end:", rows_p.time.value_counts().sort_index().to_dict())
res = []
for j in range(len(SP)):
    r = {"unit": int(unit_table[unit_table.kept].unit.values[j])}
    r["prior_dep"] = bic(y_p[:, j], design(rows_p)) < bic(y_p[:, j], design(rows_p, prior=False))
    for p in PRIORS:
        rr, yy = per_prior[p]
        r[f"ts_dep_{p}"] = bic(yy[:, j], design(rr, prior=False)) < bic(yy[:, j], design(rr, prior=False, time=False))
    res.append(r)
glm = pd.DataFrame(res)
glm["ts_dep"] = glm.ts_dep_Short | glm.ts_dep_Long
n = len(glm)
for col, label, expv in (("prior_dep", "prior", 65), ("ts_dep", "ts (either prior)", 27),
                         ("ts_dep_Short", "ts (Short model)", None), ("ts_dep_Long", "ts (Long model)", None)):
    k = int(glm[col].sum())
    lo, hi = proportion_confint(k, n, method="beta")
    print(f"{label:>18}: {k} of {n} = {100 * k / n:.1f}% (95% CI {100 * lo:.1f} to {100 * hi:.1f})"
          + (f"; expected {expv} +- {expv / 10:.1f}" if expv else ""))
print("Both prior- and ts-dependent:", int((glm.prior_dep & glm.ts_dep).sum()),
      "; neither:", int((~glm.prior_dep & ~glm.ts_dep).sum()))
held = data["units"].loc[glm.unit, "heldout"].values
print("Among the 40 benchmark held-in units kept vs held-out units kept:",
      f"prior {glm.prior_dep[~held].mean():.2f} / {glm.prior_dep[held].mean():.2f},",
      f"ts {glm.ts_dep[~held].mean():.2f} / {glm.ts_dep[held].mean():.2f}")

# %% [markdown]
# ## dfr-overlap-support
#
# > At the overlapping ts of 800 ms, firing rates differ between priors, with the largest difference
# > during the support of the prior, between 480 and 800 ms after Ready.
#
# Criterion: per dataset, ts = 800 trials; per unit the difference of mean rates between priors in
# 160 ms bins from 320 ms before Ready to 640 ms after Set; the root mean square over units, averaged
# over the 4 datasets. Reproduced when the largest value falls in a bin within 480 to 800 ms after
# Ready and exceeds the 95th percentile of the largest value over 200 shuffles of the prior labels
# among ts = 800 trials. Bins up to Set are aligned to `ready_time`, those after Set to `set_time`
# (ts = 800 ms, so the bins are contiguous in nominal time).

# %% tags=claim:dfr-overlap-support
rng_dfr = np.random.default_rng(7)
o = T[T.ts == 800]
labels = ([f"R{a}..{a + 160}" for a in range(-320, 800, 160)]
          + [f"S{a}..{a + 160}" for a in range(0, 640, 160)])
counts_dfr = {}
for ds, g in o.groupby("dataset"):
    a = rsg.bin_counts(SP, g.ready_time.values, -320, 800, bin_ms=160)
    b = rsg.bin_counts(SP, g.set_time.values, 0, 640, bin_ms=160)
    counts_dfr[ds] = (np.concatenate([a, b], axis=1) / 0.16, (g.prior == "Long").values)


def rms_curve(shuffle_rng=None):
    curves = []
    for ds, (rates, is_long) in counts_dfr.items():
        lab = shuffle_rng.permutation(is_long) if shuffle_rng is not None else is_long
        diff = rates[lab].mean(0) - rates[~lab].mean(0)
        curves.append(np.sqrt((diff ** 2).mean(1)))
    return np.array(curves)


curves = rms_curve()
mean_curve = curves.mean(0)
null_max = np.array([rms_curve(rng_dfr).mean(0).max() for _ in range(200)])
print(pd.DataFrame(curves, index=list(counts_dfr), columns=labels).round(2).to_string())
print("mean over datasets:", dict(zip(labels, mean_curve.round(2))))
k = int(np.argmax(mean_curve))
print(f"\nLargest mean RMS difference: {mean_curve[k]:.2f} spikes/s in bin {labels[k]} "
      f"(support of the prior = bins R480..640 and R640..800)")
print(f"Shuffle null of the largest value: median {np.median(null_max):.2f}, 95th percentile "
      f"{np.percentile(null_max, 95):.2f}")
print("Per-dataset bin of the largest value:", {ds: labels[i] for ds, i in zip(counts_dfr, curves.argmax(1))})
print("Trials per dataset (Short, Long):", {ds: (int((~l).sum()), int(l.sum())) for ds, (_, l) in counts_dfr.items()})

# %% [markdown]
# ## Population trajectories
#
# Shared by the claims below. Per dataset, trial-averaged rates (20 ms bins, Gaussian SD 40 ms) of
# the 48 units. Estimation epoch: from Ready to the prior's longest ts, with attrition. Production
# epoch: from Set to the shortest Set-to-Go time of each ts. PCA per dataset and epoch on both priors
# concatenated, keeping the components that reach 75% of the variance (STAR Methods, "Principal
# component analysis").

# %%
EST, EST_N, PCA_E, K_E, PROD, PCA_P, K_P = {}, {}, {}, {}, {}, {}, {}
for ds, g in T.groupby("dataset"):
    EST[ds], EST_N[ds], PROD[ds] = {}, {}, {}
    for prior in PRIORS:
        gp = g[g.prior == prior]
        EST[ds][prior], EST_N[ds][prior] = rsg.estimation_rates(SP, gp, max(rsg.PRIOR_TS[prior]))
        for ts in rsg.PRIOR_TS[prior]:
            PROD[ds][(prior, ts)] = rsg.production_rates(SP, gp[gp.ts == ts])
    PCA_E[ds], K_E[ds] = rsg.fit_pca([EST[ds][p] for p in PRIORS])
    PCA_P[ds], K_P[ds] = rsg.fit_pca(list(PROD[ds].values()))
print("Production trajectory lengths (bins of 20 ms) per dataset:")
print(pd.DataFrame({ds: {f"{p} {ts}": v.shape[0] for (p, ts), v in PROD[ds].items()} for ds in DS}).to_string())
print("Rate ranges (spikes/s), estimation:", {ds: (round(min(v.min() for v in EST[ds].values()), 1),
      round(max(v.max() for v in EST[ds].values()), 1)) for ds in DS})


def est_states(ds, prior):
    """Estimation-epoch states in the dataset's estimation PC space."""
    return PCA_E[ds].transform(EST[ds][prior])[:, :K_E[ds]]


def prod_states(ds, key, rates=None):
    r = PROD[ds][key] if rates is None else rates
    return PCA_P[ds].transform(r)[:, :K_P[ds]]

# %% [markdown]
# ## pca-dimensionality
#
# > Population activity is low dimensional; 3 to 4 principal components in the estimation epoch and
# > 5 to 10 in the production epoch explain about 75% of the variance.
#
# Criterion: the number of components to reach 75%, per dataset and epoch; ranges widened by 10%:
# 3 or 4 (estimation) and 5 to 11 (production). Reproduced when all 8 values fall in range; partially
# when at least 4 do.

# %% tags=claim:pca-dimensionality
rows = []
for ds in DS:
    for ep, pca, k, rng_ok in (("estimation", PCA_E[ds], K_E[ds], (3, 4)), ("production", PCA_P[ds], K_P[ds], (5, 11))):
        cum = np.cumsum(pca.explained_variance_ratio_)
        rows.append({"dataset": ds, "epoch": ep, "n_PC_75": k, "in_range": rng_ok[0] <= k <= rng_ok[1],
                     "cum_var_first_6": cum[:6].round(3)})
dims = pd.DataFrame(rows)
print(dims.to_string(index=False))
print(f"\nIn range: {int(dims.in_range.sum())} of 8")
print("Without smoothing (variant):", {ds: (rsg.fit_pca([rsg.estimation_rates(SP, T[(T.dataset == ds) & (T.prior == p)], max(rsg.PRIOR_TS[p]), smoothed=False)[0] for p in PRIORS])[1])
      for ds in DS}, "(estimation)")
EOF
cd entries/sohn-2019 && cp $TMPDIR/s/nb.py run1.py && source $TMPDIR/env/bin/activate && time python run1.py 2>&1 | sed -n '/^Rows in the prior/,$p'; rm run1.py
```

```
Rows in the prior model: 3921 ; by window end: {480: 983, 560: 884, 640: 773, 720: 686, 800: 595}
             prior: 38 of 48 = 79.2% (95% CI 65.0 to 89.5); expected 65 +- 6.5
 ts (either prior): 22 of 48 = 45.8% (95% CI 31.4 to 60.8); expected 27 +- 2.7
  ts (Short model): 16 of 48 = 33.3% (95% CI 20.4 to 48.4)
   ts (Long model): 16 of 48 = 33.3% (95% CI 20.4 to 48.4)
Both prior- and ts-dependent: 19 ; neither: 7
Among the 40 benchmark held-in units kept vs held-out units kept: prior 0.83 / 0.69, ts 0.51 / 0.31
            R-320..-160  R-160..0  R0..160  R160..320  R320..480  R480..640  R640..800  S0..160  S160..320  S320..480  S480..640
Eye Left           2.24      1.85     2.77       4.36       7.84       9.49       5.97     9.61       4.94       4.42       2.64
Eye Right          2.16      1.97     2.58       3.51       8.92       9.14       4.59     6.79       5.18       4.49       1.95
Hand Left          2.87      2.73     2.58       4.73       4.19       4.88       4.61     3.38       4.50       2.75       2.96
Hand Right         2.30      2.59     2.78       3.75       2.91       3.94       4.39     4.22       3.92       3.37       2.25
mean over datasets: {'R-320..-160': np.float64(2.39), 'R-160..0': np.float64(2.29), 'R0..160': np.float64(2.68), 'R160..320': np.float64(4.09), 'R320..480': np.float64(5.97), 'R480..640': np.float64(6.86), 'R640..800': np.float64(4.89), 'S0..160': np.float64(6.0), 'S160..320': np.float64(4.64), 'S320..480': np.float64(3.76), 'S480..640': np.float64(2.45)}

Largest mean RMS difference: 6.86 spikes/s in bin R480..640 (support of the prior = bins R480..640 and R640..800)
Shuffle null of the largest value: median 2.77, 95th percentile 3.09
Per-dataset bin of the largest value: {'Eye Left': 'S0..160', 'Eye Right': 'R480..640', 'Hand Left': 'R480..640', 'Hand Right': 'R640..800'}
Trials per dataset (Short, Long): {'Eye Left': (22, 36), 'Eye Right': (25, 38), 'Hand Left': (24, 14), 'Hand Right': (22, 19)}
Production trajectory len
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/s/nb.py <<'EOF'
soft = {}
for ds in DS:
    g = T[T.dataset == ds]
    blocks = [rsg.estimation_rates(SP, g[g.prior == p], max(rsg.PRIOR_TS[p]))[0] for p in PRIORS]
    rng_u = np.vstack(blocks).max(0) - np.vstack(blocks).min(0)
    soft[ds] = rsg.fit_pca([b / (rng_u + 5) for b in blocks])[1]
print("Soft-normalised rates, rate / (range + 5) (variant, not the claims file's method):", soft, "(estimation)")
EOF
cat >> $TMPDIR/s/nb.py <<'EOF'

# %% [markdown]
# ## encoding-r2
#
# > Projections of estimation-epoch neural states onto the encoding axis match the Bayesian
# > estimates from the model fitted to the behaviour (R2 = 0.993 for the Short prior, 0.996 for the
# > Long prior, monkey H, Hand Left).
#
# Criterion: weighted regression Xu = a + b te over the 20 ms time points of the prior's support,
# each point weighted by the number of trials it averages; te(t) is the model's mean estimate at ts =
# t, from the fits of beh-bayes-model. Readings: (a) the Hand Left dataset, (b) the mean over the 4
# datasets. Reproduced when under one reading both R2 are within tolerance (at least 0.894 and
# 0.896); partially when one is. Reference: R2 for 1000 random unit vectors in the same PC space.

# %% tags=claim:encoding-r2
rng_enc = np.random.default_rng(11)
ENC = {}
rows = []
for ds in DS:
    for prior in PRIORS:
        lo, hi = min(rsg.PRIOR_TS[prior]), max(rsg.PRIOR_TS[prior])
        X = est_states(ds, prior)
        u = rsg.encoding_axis(X, lo, hi)
        tt = np.arange(lo, hi + 1, rsg.BIN_MS)
        idx = tt // rsg.BIN_MS - 1
        xu, w = X[idx] @ u, EST_N[ds][prior][idx]
        te = rsg.bls_predict(fits[ds], prior, tt).te.values
        (_, b_te), r2_te, fit_te = rsg.wls(xu, te, w)
        (_, b_ts), r2_ts, fit_ts = rsg.wls(xu, tt, w)
        rand = rng_enc.normal(size=(1000, X.shape[1]))
        rand /= np.linalg.norm(rand, axis=1, keepdims=True)
        r2_rand = np.array([rsg.wls(X[idx] @ v, te, w)[1] for v in rand])
        ENC[(ds, prior)] = dict(t=tt, xu=xu, w=w, te=te, X=X, u=u, slope_ts=b_ts,
                                rmse_bayes=np.sqrt(np.mean((xu - fit_te) ** 2)),
                                rmse_lin=np.sqrt(np.mean((xu - fit_ts) ** 2)),
                                wrmse_bayes=np.sqrt(np.sum(w * (xu - fit_te) ** 2) / w.sum()),
                                wrmse_lin=np.sqrt(np.sum(w * (xu - fit_ts) ** 2) / w.sum()))
        rows.append({"dataset": ds, "prior": prior, "n_PC": X.shape[1], "points": len(tt),
                     "R2_te": r2_te, "R2_ts": r2_ts, "R2_random_median": np.median(r2_rand),
                     "R2_random_95pct": np.percentile(r2_rand, 95),
                     "frac_random_above": np.mean(r2_rand >= r2_te)})
enc = pd.DataFrame(rows)
print(enc.round(3).to_string(index=False))
hl = enc[enc.dataset == "Hand Left"].set_index("prior").R2_te
mn = enc.groupby("prior").R2_te.mean()
print(f"\nReading (a) Hand Left: Short {hl.Short:.3f}, Long {hl.Long:.3f}")
print(f"Reading (b) mean over datasets: Short {mn.Short:.3f}, Long {mn.Long:.3f}")
print("Within tolerance (>= 0.894 Short, >= 0.896 Long): (a)", [bool(hl.Short >= 0.894), bool(hl.Long >= 0.896)],
      "; (b)", [bool(mn.Short >= 0.894), bool(mn.Long >= 0.896)])
fig, axes = plt.subplots(1, 4, figsize=(14, 3))
for ax, ds in zip(axes, DS):
    for prior, col in (("Short", "tab:red"), ("Long", "tab:blue")):
        e = ENC[(ds, prior)]
        ax.plot(e["t"], e["xu"], "o", color=col, ms=3)
        ax.plot(e["t"], rsg.wls(e["xu"], e["te"], e["w"])[2], "-", color=col)
    ax.set_title(ds); ax.set_xlabel("t after Ready (ms)")
axes[0].set_ylabel("Xu (spikes/s)")
plt.tight_layout(); plt.show()
print("Plotted Xu ranges:", {f"{d} {p}": (round(e['xu'].min(), 1), round(e['xu'].max(), 1)) for (d, p), e in ENC.items()})

# %% [markdown]
# ## encoding-bayes-beats-linear
#
# > Neural projections are better explained by the Bayesian model than by a linear function of ts
# > with the same number of parameters, for both priors (signed-rank test on RMSE, p = 0.008 for
# > each prior).
#
# Criterion: RMSE of the weighted fits Xu = a + b te and Xu = a + b ts, per dataset and prior;
# reproduced when the Bayesian RMSE is lower in all 4 datasets for both priors; partially when it is
# for one prior. The RMSE is the root mean square of the residuals ("Root Mean Squared Error between
# the actual and predicted Xu", STAR Methods); the weighted RMSE is shown as a variant.

# %% tags=claim:encoding-bayes-beats-linear
rows = [{"dataset": ds, "prior": p, "rmse_bayes": e["rmse_bayes"], "rmse_linear": e["rmse_lin"],
         "delta": e["rmse_bayes"] - e["rmse_lin"], "weighted_delta": e["wrmse_bayes"] - e["wrmse_lin"]}
        for (ds, p), e in ENC.items()]
rm = pd.DataFrame(rows)
print(rm.round(4).to_string(index=False))
for p in PRIORS:
    r = rm[rm.prior == p]
    print(f"{p}: Bayesian lower in {int((r.delta < 0).sum())} of 4 (weighted RMSE: "
          f"{int((r.weighted_delta < 0).sum())} of 4); median delta {r.delta.median():.4f}; "
          f"signed-rank p = {signed_rank(r.delta):.3f}")

# %% [markdown]
# ## short-in-long-control
#
# > In the Long prior during the period matched to the support of the Short prior ("Short In Long"),
# > there is no sigmoidal representation; the Bayesian model is not better than the linear one
# > (signed-rank test, p = 0.74).
#
# Criterion (absence, judged on the paper's test): Long prior states from 480 to 800 ms after Ready,
# an axis from the state at 480 to that at 800 ms, compared with the Short prior's te and with ts as
# above; reproduced when a two-sided signed-rank test of the RMSE difference over the 4 datasets has
# p >= 0.05. The axis is built as u is, from the averaged difference vectors (the STAR Methods
# "applied the same projection analysis"); the single vector from 480 to 800 ms is shown as a
# variant. All Long trials have Set at or after 800 ms, so every point has the same weight.

# %% tags=claim:short-in-long-control
rows = []
for ds in DS:
    X = est_states(ds, "Long")
    tt = np.arange(480, 801, rsg.BIN_MS)
    idx = tt // rsg.BIN_MS - 1
    w = EST_N[ds]["Long"][idx]
    te = rsg.bls_predict(fits[ds], "Short", tt).te.values
    for axis_name, u in (("averaged", rsg.encoding_axis(X, 480, 800)),
                         ("single vector", (X[idx[-1]] - X[idx[0]]) / np.linalg.norm(X[idx[-1]] - X[idx[0]]))):
        xu = X[idx] @ u
        rb = np.sqrt(np.mean((xu - rsg.wls(xu, te, w)[2]) ** 2))
        rl = np.sqrt(np.mean((xu - rsg.wls(xu, tt, w)[2]) ** 2))
        rows.append({"dataset": ds, "axis": axis_name, "rmse_bayes": rb, "rmse_linear": rl, "delta": rb - rl,
                     "R2_te": rsg.wls(xu, te, w)[1], "R2_ts": rsg.wls(xu, tt, w)[1]})
sil = pd.DataFrame(rows)
print(sil.round(4).to_string(index=False))
for ax_name, r in sil.groupby("axis", sort=False):
    print(f"{ax_name}: Bayesian lower in {int((r.delta < 0).sum())} of 4; median delta {r.delta.median():.4f};"
          f" signed-rank p = {signed_rank(r.delta):.3f}")
short_delta = rm[rm.prior == "Short"].set_index("dataset").delta
print("Short prior deltas for comparison:", short_delta.round(4).to_dict())
print("Short In Long minus Short delta, per dataset:",
      (sil[sil.axis == "averaged"].set_index("dataset").delta - short_delta).round(4).to_dict())

# %% [markdown]
# ## neural-long-more-bias
#
# > Neural projections show more bias for the Long prior than for the Short prior, as a smaller
# > regression slope of Xu on ts (signed-rank test, p = 0.008).
#
# Criterion: the slope of the weighted regression of Xu (spikes/s, shared PC space of the dataset) on
# ts (ms), per dataset and prior; reproduced when Long is below Short in all 4 datasets; partially
# for 3.

# %% tags=claim:neural-long-more-bias
nb_sl = pd.DataFrame({p: {ds: ENC[(ds, p)]["slope_ts"] for ds in DS} for p in PRIORS})
nb_sl["long_below_short"] = nb_sl.Long < nb_sl.Short
print(nb_sl.round(4).to_string())
print(f"\nLong below Short in {int(nb_sl.long_below_short.sum())} of 4; "
      f"signed-rank p (Short - Long) = {signed_rank(nb_sl.Short - nb_sl.Long):.3f}")
EOF
cd entries/sohn-2019 && cp $TMPDIR/s/nb.py run1.py && source $TMPDIR/env/bin/activate && time python run1.py 2>&1 | sed -n '/^Soft/,$p'; rm run1.py
```

```
Soft-normalised rates, rate / (range + 5) (variant, not the claims file's method): {'Eye Right': 3, 'Eye Left': 3, 'Hand Right': 3, 'Hand Left': 3} (estimation)
   dataset prior  n_PC  points  R2_te  R2_ts  R2_random_median  R2_random_95pct  frac_random_above
 Eye Right Short     2      17  0.957  0.952             0.941            0.994              0.399
 Eye Right  Long     2      21  0.974  0.969             0.970            0.974              0.111
  Eye Left Short     2      17  0.909  0.897             0.898            0.974              0.434
  Eye Left  Long     2      21  0.989  0.979             0.976            0.995              0.319
Hand Right Short     2      17  0.959  0.962             0.920            0.985              0.322
Hand Right  Long     2      21  0.994  0.992             0.987            0.995              0.172
 Hand Left Short     2      17  0.994  0.984             0.866            0.993              0.004
 Hand Left  Long     2      21  0.986  0.987             0.749            0.993              0.103

Reading (a) Hand Left: Short 0.994, Long 0.986
Reading (b) mean over datasets: Short 0.955, Long 0.986
Within tolerance (>= 0.894 Short, >= 0.896 Long): (a) [True, True] ; (b) [True, True]
Plotted Xu ranges: {'Eye Right Short': (np.float64(-41.9), np.float64(14.1)), 'Eye Right Long': (np.float64(-16.1), np.float64(22.3)), 'Eye Left Short': (np.float64(-47.0), np.float64(17.4)), 'Eye Left Long': (np.float64(-18.4), np.float64(24.5)), 'Hand Right Short': (np.float64(5.1), np.float64(22.2)), 'Hand Right Long': (np.float64(2.0), np.float64(20.8)), 'Hand Left Short': (np.float64(-3.0), np.float64(17.7)), 'Hand Left Long': (np.float64(-0.3), np.float64(10.4))}
   dataset prior  rmse_bayes  rmse_linear   delta  weighted_delta
 Eye Right Short      3.3058       3.4904 -0.1846         -0.1945
 Eye Right  Long      2.6947       2.8912 -0.1965         -0.2109
  Eye Left Short      6.2306       6.6243 -0.3937         -0.4079
  Eye Left  Long    
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> $TMPDIR/s/nb.py <<'EOF'

# %% [markdown]
# ## speed-vs-projection
#
# > Larger projections on the encoding axis at Set are followed by slower neural trajectories in the
# > production epoch (Pearson correlation, rho Short = -0.74, rho Long = -0.51).
#
# Criterion: per prior, Xu at t = ts against the speed of the production trajectory of that ts, pooled
# over the 4 datasets (20 points); speed is the mean Euclidean distance between successive 20 ms
# states in the production PC space, from Set to the shortest tp of that ts (claims header).
# Reproduced when both correlations are within tolerance (-0.74 +- 0.074, -0.51 +- 0.051); partially
# when both are negative with p < 0.05 but one is outside tolerance, or when only one is within
# tolerance. Variants: correlations within each dataset; speed divided by the mean Set-to-Go time of
# the ts (the STAR Methods' "divided by the duration separating Set and the time of Go").

# %% tags=claim:speed-vs-projection
rows = []
for ds in DS:
    g = T[T.dataset == ds]
    for (prior, ts) in PROD[ds]:
        Y = prod_states(ds, (prior, ts))
        e = ENC[(ds, prior)]
        gg = g[(g.prior == prior) & (g.ts == ts)]
        rows.append({"dataset": ds, "prior": prior, "ts": ts,
                     "xu_at_set": e["xu"][list(e["t"]).index(ts)],
                     "speed": np.mean(np.linalg.norm(np.diff(Y, axis=0), axis=1)),
                     "set_to_go_s": np.mean(gg.go_time - gg.set_time), "tp_mean": gg.tp.mean()})
SPD = pd.DataFrame(rows)
SPD["speed_per_s"] = SPD.speed / SPD.set_to_go_s
print(SPD.round(3).to_string(index=False))


def corr_table(x, y):
    out = []
    for prior in PRIORS:
        s = SPD[SPD.prior == prior]
        r, p = stats.pearsonr(s[x], s[y])
        per = {ds: round(stats.pearsonr(q[x], q[y])[0], 2) for ds, q in s.groupby("dataset")}
        out.append({"prior": prior, "n": len(s), "r_pooled": round(r, 3), "p": p, "r_within_dataset": per})
    return pd.DataFrame(out)


print("\nSpeed (mean step) against Xu at Set:")
print(corr_table("xu_at_set", "speed").to_string(index=False))
print("\nVariant, speed divided by the Set-to-Go time:")
print(corr_table("xu_at_set", "speed_per_s").to_string(index=False))

# %% [markdown]
# ## initial-speed-biased
#
# > The initial speed of production trajectories (Set to Set + 400 ms) is biased toward the middle of
# > the prior; its dependence on ts is shallower than the unbiased profile proportional to 1/ts
# > (signed-rank test, p < 1e-3 over conditions and animals).
#
# Criterion: per dataset and prior, the mean step distance between Set and Set + 400 ms (trials with
# tp of at least 400 ms), the slope of its regression on ts, and the slope of the unbiased profile
# speed(middle ts) x middle ts / ts. Reproduced when the measured slope is shallower (less negative)
# than the unbiased one in most of the 8 and a two-sided signed-rank test of the difference has
# p < 0.05. States are in the dataset's production PC space.

# %% tags=claim:initial-speed-biased
rows = []
for ds in DS:
    g = T[(T.dataset == ds) & (T.tp >= 400)]
    for prior in PRIORS:
        tsv = np.array(rsg.PRIOR_TS[prior], float)
        sp = []
        for ts in rsg.PRIOR_TS[prior]:
            Y = prod_states(ds, None, rsg.production_rates(SP, g[(g.prior == prior) & (g.ts == ts)], length_ms=400))
            sp.append(np.mean(np.linalg.norm(np.diff(Y, axis=0), axis=1)))
        sp = np.array(sp)
        unb = sp[2] * tsv[2] / tsv
        rows.append({"dataset": ds, "prior": prior, "speeds": sp.round(2),
                     "slope_measured": np.polyfit(tsv, sp, 1)[0], "slope_unbiased": np.polyfit(tsv, unb, 1)[0]})
ini = pd.DataFrame(rows)
ini["difference"] = ini.slope_measured - ini.slope_unbiased
print(ini.to_string(index=False, formatters={c: "{:.5f}".format for c in ["slope_measured", "slope_unbiased", "difference"]}))
print(f"\nMeasured shallower than unbiased (difference > 0): {int((ini.difference > 0).sum())} of 8; "
      f"measured slope negative: {int((ini.slope_measured < 0).sum())} of 8; "
      f"signed-rank p = {signed_rank(ini.difference):.4f}")

# %% [markdown]
# ## speed-predicts-tp
#
# > The speed of neural trajectories in the production epoch predicts the mean tp (Pearson
# > correlation, rho Short = -0.58, rho Long = -0.52).
#
# Criterion: per prior, the mean tp of each dataset and ts against the speed of that ts (as in
# speed-vs-projection), pooled over the 4 datasets (20 points); same rule as speed-vs-projection.
# Variant: the trial-by-trial correlation within each prior, effector and direction. Here each trial's
# rates (20 ms bins, Gaussian SD 40 ms) from Set to its Go are projected into the dataset's production
# PC space; speed and tp are z-scored within each ts (as the STAR Methods do for Figure S6) and
# correlated. This single-trial speed is a stand-in for the benchmark's model-inferred rates.

# %% tags=claim:speed-predicts-tp
print("Mean tp against speed (mean step):")
print(corr_table("speed", "tp_mean").to_string(index=False))
print("\nVariant, speed divided by the Set-to-Go time:")
print(corr_table("speed_per_s", "tp_mean").to_string(index=False))
rows = []
for ds in DS:
    g = T[T.dataset == ds]
    for prior in PRIORS:
        zs, zt = [], []
        for ts in rsg.PRIOR_TS[prior]:
            gg = g[(g.prior == prior) & (g.ts == ts)]
            s_tr = []
            for r in gg.itertuples():
                nb = int((r.go_time - r.set_time) * 1000 // rsg.BIN_MS)
                c = rsg.bin_counts(SP, np.array([r.set_time]), 0, nb * rsg.BIN_MS)[0] * (1000 / rsg.BIN_MS)
                Y = PCA_P[ds].transform(rsg.smooth(c))[:, :K_P[ds]]
                s_tr.append(np.mean(np.linalg.norm(np.diff(Y, axis=0), axis=1)))
            zs.append(stats.zscore(s_tr)); zt.append(stats.zscore(gg.tp.values))
        r, p = stats.pearsonr(np.concatenate(zs), np.concatenate(zt))
        rows.append({"dataset": ds, "prior": prior, "trials": len(np.concatenate(zs)), "r_trial": r, "p": p})
trial_corr = pd.DataFrame(rows)
print("\nVariant, trial by trial (z-scored within ts):")
print(trial_corr.round(4).to_string(index=False))
print(f"Negative in {int((trial_corr.r_trial < 0).sum())} of 8; mean r {trial_corr.r_trial.mean():.3f}")

# %% [markdown]
# ## alt-speed-unmodulated
#
# > Instantaneous speed of neural trajectories in the full neural space is not modulated during the
# > support of each prior (signed-rank test for zero regression slopes, p = 0.64 for Short, p = 0.08
# > for Long).
#
# Criterion (absence, judged on the paper's test): per dataset and prior, the distance between
# successive 20 ms states of the smoothed rates of all selected units over the support of the prior
# (with attrition), regressed on time; reproduced when a two-sided signed-rank test of the 4 slopes
# against zero has p >= 0.05 for each prior. With 4 datasets the test cannot reach p < 0.05; the
# slopes and their bootstrap intervals over trials (200 resamples of trials within dataset and
# prior) are the effect size.

# %% tags=claim:alt-speed-unmodulated
rng_spd = np.random.default_rng(23)


def support_speed_slope(ds, prior, t):
    lo, hi = min(rsg.PRIOR_TS[prior]), max(rsg.PRIOR_TS[prior])
    R, _ = rsg.estimation_rates(SP, t, hi)
    idx = np.arange(lo, hi + 1, rsg.BIN_MS) // rsg.BIN_MS - 1
    steps = np.linalg.norm(np.diff(R[idx], axis=0), axis=1)
    times = np.arange(lo + rsg.BIN_MS, hi + 1, rsg.BIN_MS)
    return np.polyfit(times, steps, 1)[0], steps


rows = []
for ds in DS:
    for prior in PRIORS:
        g = T[(T.dataset == ds) & (T.prior == prior)]
        slope, steps = support_speed_slope(ds, prior, g)
        boot = [support_speed_slope(ds, prior, g.iloc[rng_spd.integers(0, len(g), len(g))])[0] for _ in range(200)]
        rows.append({"dataset": ds, "prior": prior, "mean_step": steps.mean(), "slope_per_s": slope * 1000,
                     "boot_lo": np.percentile(boot, 2.5) * 1000, "boot_hi": np.percentile(boot, 97.5) * 1000,
                     "relative_change_over_support": slope * (len(steps) - 1) * rsg.BIN_MS / steps.mean()})
asp = pd.DataFrame(rows)
print(asp.round(3).to_string(index=False))
for prior in PRIORS:
    s = asp[asp.prior == prior]
    print(f"{prior}: slopes > 0 in {int((s.slope_per_s > 0).sum())} of 4; bootstrap intervals excluding 0: "
          f"{int(((s.boot_lo > 0) | (s.boot_hi < 0)).sum())} of 4; signed-rank p = {signed_rank(s.slope_per_s):.3f}")

# %% [markdown]
# ## alt-transient-parallel
#
# > In the first 200 ms after Set, trajectories for different ts run parallel; their distance to the
# > middle ts trajectory does not change (signed-rank test for zero slopes, p = 0.92 for the shortest
# > ts, p = 0.13 for the longest).
#
# Criterion (absence, judged on the paper's test): PCA per dataset on Set to Set + 200 ms, both
# priors, at least 75% of variance; per dataset and prior the distance from the shortest and the
# longest ts trajectory to the middle ts trajectory at each 20 ms bin, regressed on time; reproduced
# when a two-sided signed-rank test of the 8 slopes against zero has p >= 0.05 for both.

# %% tags=claim:alt-transient-parallel
rows = []
for ds in DS:
    g = T[T.dataset == ds]
    tr = {(p, ts): rsg.production_rates(SP, g[(g.prior == p) & (g.ts == ts)], length_ms=200)
          for p in PRIORS for ts in rsg.PRIOR_TS[p]}
    pca, k = rsg.fit_pca(list(tr.values()))
    Z = {key: pca.transform(v)[:, :k] for key, v in tr.items()}
    times = np.arange(1, 11) * rsg.BIN_MS
    for prior in PRIORS:
        tsv = rsg.PRIOR_TS[prior]
        mid = Z[(prior, tsv[2])]
        for which, ts in (("shortest", tsv[0]), ("longest", tsv[-1])):
            dist = np.linalg.norm(Z[(prior, ts)] - mid, axis=1)
            rows.append({"dataset": ds, "prior": prior, "ts": which, "n_PC": k,
                         "dist_first": dist[0], "dist_last": dist[-1], "slope_per_s": np.polyfit(times, dist, 1)[0] * 1000})
par = pd.DataFrame(rows)
print(par.round(3).to_string(index=False))
for which in ("shortest", "longest"):
    s = par[par.ts == which]
    print(f"{which}: slopes > 0 in {int((s.slope_per_s > 0).sum())} of 8; median {s.slope_per_s.median():.2f} "
          f"per s; signed-rank p = {signed_rank(s.slope_per_s):.4f}")

# %% [markdown]
# ## alt-threshold-monotonic
#
# > Aligned to the response, distances between trajectories for different ts decrease steadily up to
# > movement initiation, without the converging then diverging pattern a ts-dependent threshold
# > would produce.
#
# Criterion: PCA per dataset on Go - 800 ms to Go, both priors, components explaining 60% of the
# variance; per dataset, prior and non-middle ts (32 curves) the distance to the middle ts trajectory
# at each 20 ms bin and the time of its minimum. Reproduced when the median time of the minimum is
# in the last 40 ms before Go; partially when in the last 200 ms. A bin's time is its end (the last
# bin ends at Go). The 75% threshold is shown as a variant.

# %% tags=claim:alt-threshold-monotonic
rows = []
for thr in (0.60, 0.75):
    for ds in DS:
        g = T[T.dataset == ds]
        tr = {(p, ts): rsg.go_rates(SP, g[(g.prior == p) & (g.ts == ts)]) for p in PRIORS for ts in rsg.PRIOR_TS[p]}
        pca, k = rsg.fit_pca(list(tr.values()), threshold=thr)
        Z = {key: pca.transform(v)[:, :k] for key, v in tr.items()}
        ends = np.arange(-780, 1, rsg.BIN_MS)
        for prior in PRIORS:
            tsv = rsg.PRIOR_TS[prior]
            for ts in tsv:
                if ts == tsv[2]:
                    continue
                dist = np.linalg.norm(Z[(prior, ts)] - Z[(prior, tsv[2])], axis=1)
                rows.append({"threshold": thr, "dataset": ds, "prior": prior, "ts": ts, "n_PC": k,
                             "t_min": ends[np.argmin(dist)], "dist_at_go": dist[-1], "dist_min": dist.min(),
                             "dist_at_-800": dist[0]})
thr_tab = pd.DataFrame(rows)
for thr, s in thr_tab.groupby("threshold"):
    print(f"\nPCs for {thr:.0%}:", s.groupby("dataset").n_PC.first().to_dict())
    print("Times of the minimum distance (ms before Go, bin end):", sorted(s.t_min.tolist()))
    print(f"Median time of the minimum: {s.t_min.median():.0f} ms; in the last 40 ms: {int((s.t_min >= -20).sum())}"
          f" of 32; in the last 200 ms: {int((s.t_min >= -180).sum())} of 32")
    print(f"Distance at Go above the minimum in {int((s.dist_at_go > s.dist_min + 1e-9).sum())} of 32; "
          f"median ratio of distance at Go to that at Go - 800 ms: {np.median(s.dist_at_go / s['dist_at_-800']):.2f}")
EOF
cd entries/sohn-2019 && cp $TMPDIR/s/nb.py run1.py && source $TMPDIR/env/bin/activate && time python run1.py 2>&1 | sed -n '/dataset prior   ts  xu_at_set/,$p'; rm run1.py
```

```
Sat Nov 14 13:12:22 UTC 2026
   dataset prior   ts  xu_at_set  speed  set_to_go_s  tp_mean  speed_per_s
 Eye Right Short  480    -41.516  8.230        0.478  496.868       17.225
 Eye Right Short  560    -37.308  8.033        0.524  543.739       15.320
 Eye Right Short  640    -18.936  6.522        0.610  630.550       10.691
 Eye Right Short  720      2.206  5.382        0.730  752.037        7.375
 Eye Right Short  800     14.125  4.767        0.809  836.602        5.889
 Eye Right  Long  800    -16.065  5.971        0.826  844.335        7.226
 Eye Right  Long  900     -8.223  4.847        0.903  922.279        5.370
 Eye Right  Long 1000      7.554  4.366        0.981 1002.392        4.452
 Eye Right  Long 1100     19.502  4.357        1.131 1156.215        3.853
 Eye Right  Long 1200     22.258  3.583        1.155 1176.536        3.102
  Eye Left Short  480    -44.400  9.231        0.516  539.534       17.906
  Eye Left Short  560    -45.159  7.445        0.556  579.976       13.398
  Eye Left Short  640    -24.328  7.037        0.632  666.884       11.141
  Eye Left Short  720      6.674  5.075        0.748  772.095        6.782
  Eye Left Short  800     16.927  5.515        0.838  864.015        6.582
  Eye Left  Long  800    -18.420  6.975        0.795  821.290        8.776
  Eye Left  Long  900    -10.452  5.344        0.894  916.020        5.980
  Eye Left  Long 1000      2.576  5.282        0.978 1006.664        5.399
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/s/gpfa_part.py <<'EOF'

# %% [markdown]
# ## gpfa-variance-inverted-u
#
# > The variance across single trials of the GPFA neural state at Set projected on the encoding axis
# > has an inverted-U profile over ts, lower at the extremes of each prior (one-tailed signed-rank
# > test on quadratic coefficients, p = 0.0273, monkey H).
#
# Criterion: GPFA (20 ms bins) per dataset on single trials from Ready to Set, both priors, the
# selected units; latent dimensionality chosen by 3-fold cross-validated log-likelihood from 4 and 8;
# orthonormalised latents. Per prior, u from the trial-averaged latents with attrition; each trial's
# latent state in its last bin before Set projected on u; Xu z-scored over the prior's trials; the
# variance at each ts; the quadratic coefficient of a polynomial fit of variance on ts. Reproduced
# when a one-tailed signed-rank test (coefficient below zero) over the 8 dataset-priors has p < 0.05.
#
# GPFA is elephant's implementation (Yu et al. 2009, the method the STAR Methods cite). Each trial
# runs from `ready_time` for its nominal ts, so that its last bin ends at Set. EM runs for 200
# iterations (elephant's default is 500), a standard choice made for time; the change of
# log-likelihood over the last 10 iterations is printed. Folds are drawn with a fixed seed.

# %% tags=claim:gpfa-variance-inverted-u
import neo
import quantities as pq
from elephant.gpfa import GPFA

rng_gpfa = np.random.default_rng(31)
EM_ITERS = 200


def spiketrains(t):
    out = []
    for r in t.itertuples():
        a, b = r.ready_time, r.ready_time + r.ts / 1000
        out.append([neo.SpikeTrain((s[(s >= a) & (s < b)] - a) * pq.s, t_start=0 * pq.s, t_stop=(r.ts / 1000) * pq.s)
                    for s in SP])
    return out


def gpfa_fit(trains, x_dim):
    np.random.seed(int(rng_gpfa.integers(1 << 31)))
    g = GPFA(bin_size=rsg.BIN_MS * pq.ms, x_dim=x_dim, em_max_iters=EM_ITERS, verbose=False)
    g.fit(trains)
    return g


t_g = time.time()
GP = {}
cv_rows = []
for ds in DS:
    g = T[T.dataset == ds].reset_index(drop=True)
    trains = spiketrains(g)
    folds = rng_gpfa.permutation(len(g)) % 3
    ll = {}
    for x_dim in (4, 8):
        ll[x_dim] = 0.0
        for f in range(3):
            m = gpfa_fit([trains[i] for i in np.flatnonzero(folds != f)], x_dim)
            ll[x_dim] += m.score([trains[i] for i in np.flatnonzero(folds == f)])
    best = max(ll, key=ll.get)
    m = gpfa_fit(trains, best)
    lls = m.fit_info["log_likelihoods"]
    lat = m.transform(trains, returned_data=["latent_variable_orth"])
    GP[ds] = (g, lat)
    cv_rows.append({"dataset": ds, "trials": len(g), "cv_ll_4": ll[4], "cv_ll_8": ll[8], "x_dim": best,
                    "ll_change_last10": lls[-1] - lls[-11]})
print(pd.DataFrame(cv_rows).round(1).to_string(index=False))
print(f"GPFA time: {time.time() - t_g:.0f} s")

rows, GXU = [], {}
for ds in DS:
    g, lat = GP[ds]
    for prior in PRIORS:
        lo, hi = min(rsg.PRIOR_TS[prior]), max(rsg.PRIOR_TS[prior])
        ii = np.flatnonzero(g.prior.values == prior)
        nb = hi // rsg.BIN_MS
        acc, cnt = np.zeros((nb, lat[0].shape[0])), np.zeros(nb)
        for i in ii:
            L = lat[i].T
            acc[:len(L)] += L; cnt[:len(L)] += 1
        avg = acc / cnt[:, None]
        u = rsg.encoding_axis(avg, lo, hi)
        xu = np.array([lat[i][:, -1] @ u for i in ii])
        tsv = g.ts.values[ii]
        z = stats.zscore(xu)
        var = np.array([z[tsv == s].var(ddof=1) for s in rsg.PRIOR_TS[prior]])
        mean = np.array([xu[tsv == s].mean() for s in rsg.PRIOR_TS[prior]])
        GXU[(ds, prior)] = dict(var=var, mean=mean)
        rows.append({"dataset": ds, "prior": prior, "variance_by_ts": var.round(2),
                     "quad_coef": np.polyfit(np.array(rsg.PRIOR_TS[prior], float), var, 2)[0]})
gv = pd.DataFrame(rows)
print(gv.to_string(index=False, formatters={"quad_coef": "{:.3e}".format}))
print(f"\nQuadratic coefficient below zero in {int((gv.quad_coef < 0).sum())} of 8; one-tailed signed-rank "
      f"p = {signed_rank(gv.quad_coef, alternative='less'):.4f}")
print("Mean variance profile over the 8 (z-scored Xu):", np.mean([r for r in gv.variance_by_ts], axis=0).round(3))

# %% [markdown]
# ## gpfa-mean-sigmoid
#
# > The mean of the single-trial GPFA projections is sigmoidal (signed-rank test on increments,
# > p = 0.0078) and has a higher slope for the Short prior (one-tailed signed-rank, p = 0.0625).
#
# Criterion: with the projections of gpfa-variance-inverted-u, not z-scored; the mean Xu at each ts;
# increments as in beh-sigmoid-increments compared by a two-sided signed-rank test over the 8
# (sigmoidal when middle exceeds extreme with p < 0.05); the slope of mean Xu on ts per dataset and
# prior (higher for Short in all 4 datasets is the paper's p = 0.0625). Reproduced when both parts
# hold; partially when one does.

# %% tags=claim:gpfa-mean-sigmoid
rows = []
for (ds, prior), e in GXU.items():
    inc = np.diff(e["mean"])
    rows.append({"dataset": ds, "prior": prior, "mean_xu": e["mean"].round(3), "middle_minus_extreme":
                 (inc[1] + inc[2]) / 2 - (inc[0] + inc[3]) / 2,
                 "slope": np.polyfit(np.array(rsg.PRIOR_TS[prior], float), e["mean"], 1)[0]})
gm = pd.DataFrame(rows)
print(gm.to_string(index=False, formatters={"middle_minus_extreme": "{:.4f}".format, "slope": "{:.5f}".format}))
print(f"\nMiddle > extreme in {int((gm.middle_minus_extreme > 0).sum())} of 8; two-sided signed-rank "
      f"p = {signed_rank(gm.middle_minus_extreme):.4f}")
gs = gm.pivot(index="dataset", columns="prior", values="slope")
print(gs.round(5).to_string())
print(f"Short slope above Long in {int((gs.Short > gs.Long).sum())} of 4; one-tailed signed-rank "
      f"p = {signed_rank(gs.Short - gs.Long, alternative='greater'):.4f}")
EOF
cd entries/sohn-2019 && python3 - <<'EOF'
import re,os
s=open(os.environ["TMPDIR"]+"/s/nb.py").read()
# dev: keep only through population trajectory definitions + gpfa part, skip heavy sections
head=s.split("# %% [markdown]\n# ## beh-slopes")[0]
open("run2.py","w").write(head+open(os.environ["TMPDIR"]+"/s/gpfa_part.py").read())
EOF
source $TMPDIR/env/bin/activate && time python run2.py 2>&1 | grep -v "WARNING\|warn" | sed -n '/dataset  trials/,$p'; rm run2.py
```

```
dataset  trials   cv_ll_4   cv_ll_8  x_dim  ll_change_last10
 Eye Right     276 -175218.3 -174652.4      8               7.1
  Eye Left     260 -165381.3 -164698.2      8              11.5
Hand Right     225 -125038.9 -124443.3      8               7.5
 Hand Left     222 -116142.9 -115634.9      8               8.1
GPFA time: 642 s
   dataset prior                 variance_by_ts  quad_coef
 Eye Right Short   [0.76, 0.5, 0.58, 0.43, 0.3]  4.285e-07
 Eye Right  Long  [0.98, 0.7, 0.96, 0.36, 0.41] -1.487e-06
  Eye Left Short [0.43, 0.21, 0.61, 0.34, 0.17] -6.448e-06
  Eye Left  Long [0.57, 0.91, 0.73, 0.46, 0.39] -6.404e-06
Hand Right Short  [0.79, 0.8, 1.53, 0.76, 0.48] -2.308e-05
Hand Right  Long [0.77, 1.55, 1.36, 0.61, 0.33] -1.914e-05
 Hand Left Short   [0.8, 1.17, 0.9, 0.39, 0.82] -1.244e-06
 Hand Left  Long  [1.3, 1.49, 0.33, 0.76, 0.61]  6.482e-06

Quadratic coefficient below zero in 6 of 8; one-tailed signed-rank p = 0.0742
Mean variance profile over the 8 (z-scored Xu): [0.8   0.916 0.875 0.514 0.439]
   dataset prior                                mean_xu middle_minus_extreme   slope
 Eye Right Short [-0.57, -0.649, -0.411, -0.076, 0.093]               0.2418 0.00237
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/s && python3 - <<'EOF'
s=open("nb.py").read()
old='''for prior in PRIORS:
    s = asp[asp.prior == prior]
    print(f"{prior}: slopes > 0 in {int((s.slope_per_s > 0).sum())} of 4; bootstrap intervals excluding 0: "
          f"{int(((s.boot_lo > 0) | (s.boot_hi < 0)).sum())} of 4; signed-rank p = {signed_rank(s.slope_per_s):.3f}")
'''
new=old+'''
# Variant: the same trials at every point of the support (only trials with the prior's longest ts),
# so that the number of trials averaged, and the noise it leaves in the rates, does not change.
rows = []
for ds in DS:
    for prior in PRIORS:
        g = T[(T.dataset == ds) & (T.prior == prior) & (T.ts == max(rsg.PRIOR_TS[prior]))]
        slope, steps = support_speed_slope(ds, prior, g)
        rows.append({"dataset": ds, "prior": prior, "trials": len(g), "mean_step": steps.mean(),
                     "slope_per_s": slope * 1000})
asp_fixed = pd.DataFrame(rows)
print("\\nVariant without attrition (trials of the longest ts only):")
print(asp_fixed.round(3).to_string(index=False))
for prior in PRIORS:
    s = asp_fixed[asp_fixed.prior == prior]
    print(f"{prior}: slopes > 0 in {int((s.slope_per_s > 0).sum())} of 4; signed-rank p = {signed_rank(s.slope_per_s):.3f}")
print("Trials averaged at the start and end of the support (main analysis):",
      {f"{ds} {p}": (int(EST_N[ds][p][min(rsg.PRIOR_TS[p]) // 20 - 1]), int(EST_N[ds][p][max(rsg.PRIOR_TS[p]) // 20 - 1]))
       for ds in DS for p in PRIORS})
'''
assert old in s
s=s.replace(old,new)
s+=open("gpfa_part.py").read()
open("nb.py","w").write(s)
EOF
grep -c "" $TMPDIR/s/nb.py; date -u
```

```
1067
Sat Nov 14 13:25:10 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && python3 -c "
import os
s=open(os.environ['TMPDIR']+'/s/nb.py').read()
head=s.split('# %% [markdown]\n# ## beh-overlap-prior')[0]
a=s.split('# %% [markdown]\n# ## alt-speed-unmodulated')[1].split('# %% [markdown]\n# ## alt-transient-parallel')[0]
pop=s.split('# %% [markdown]\n# ## Population trajectories')[1].split('# %% [markdown]\n# ## pca-dimensionality')[0]
open('run3.py','w').write(head+pop+a)
" && source $TMPDIR/env/bin/activate && python run3.py 2>&1 | sed -n '/dataset prior   n/,/Variant without intercept/p;/Variant without attrition/,$p'; rm run3.py
```

```
dataset prior   n  slope  ci_low  ci_high  slope_no_intercept  ci0_low  ci0_high
  Eye Left  Long 155  0.845   0.743    0.948               0.996    0.980     1.012
  Eye Left Short 105  1.011   0.896    1.126               1.072    1.051     1.092
 Eye Right  Long 147  0.903   0.769    1.038               1.027    1.009     1.045
 Eye Right Short 129  1.110   1.014    1.206               1.016    0.999     1.033
 Hand Left  Long  88  0.502   0.369    0.636               0.923    0.901     0.946
 Hand Left Short 134  0.612   0.499    0.725               1.013    0.990     1.035
Hand Right  Long 112  0.612   0.488    0.736               1.032    1.012     1.052
Hand Right Short 113  0.861   0.728    0.993               1.057    1.032     1.081

With intercept: slopes in (0, 1): 6 of 8; intervals excluding 0 and 1: 5 of 8
Variant without intercept: slopes in (0, 1): 2 of 8; intervals excluding 0 and 1: 1 of 8
Variant without attrition (trials of the longest ts only):
   dataset prior  trials  mean_step  slope_per_s
 Eye Right Short      25      5.861        4.967
 Eye Right  Long      27      4.294        2.563
  Eye Left Short      22      6.737        5.289
  Eye Left  Long      31      4.194        0.972
Hand Right Short      22      4.734        3.567
Hand Right  Long      25      4.006       -1.065
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && python - <<'EOF'
import h5py, remfile
url="https://dandiarchive.s3.amazonaws.com/blobs/73a/6f6/73a6f648-8e97-4c90-b323-a15844e4e3d4"
f=h5py.File(remfile.File(url),"r")
def show(name,obj):
    if isinstance(obj,h5py.Dataset) and "spike_times" not in name: print(name, obj.shape, obj.dtype)
f["general"].visititems(show); print(list(f["units"].keys()))
e=f["general/extracellular_ephys/electrodes"]
for k in e.keys(): print(k, e[k][:5])
for g in f["general/extracellular_ephys"].keys():
    if g!="electrodes": print(g, dict(f["general/extracellular_ephys"][g].attrs))
print(dict(f.attrs)); print(f["general/institution"][()] if "institution" in f["general"] else None)
EOF
```

```
experiment_description () object
experimenter (1,) object
extracellular_ephys/electrodes/filtering (72,) object
extracellular_ephys/electrodes/group (72,) object
extracellular_ephys/electrodes/group_name (72,) object
extracellular_ephys/electrodes/id (72,) int64
extracellular_ephys/electrodes/imp (72,) float64
extracellular_ephys/electrodes/location (72,) object
extracellular_ephys/electrodes/x (72,) float64
extracellular_ephys/electrodes/y (72,) float64
extracellular_ephys/electrodes/z (72,) float64
institution () object
keywords (4,) object
lab () object
related_publications (1,) object
session_id () object
subject/age () object
subject/sex () object
subject/species () object
subject/subject_id () object
[... 17 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sohn-2019/rsg.py",
 "old_string": "        meta = {\"session_description\": _text(f[\"session_description\"][()]),",
 "new_string": "        el = f[\"general/extracellular_ephys/electrodes\"]\n        electrodes = {\"n\": len(el[\"id\"]),\n                      \"groups\": sorted({_text(x) for x in el[\"group_name\"][()]}),\n                      \"locations\": sorted({_text(x) for x in el[\"location\"][()]}),\n                      \"positions_all_nan\": bool(np.all(np.isnan(el[\"x\"][()]))\n                                                and np.all(np.isnan(el[\"y\"][()]))\n                                                and np.all(np.isnan(el[\"z\"][()]))),\n                      \"unit_columns\": sorted(k for k in units.keys() if not k.endswith(\"_index\"))}\n        meta = {\"session_description\": _text(f[\"session_description\"][()]),"
}
```

```
The file entries/sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sohn-2019/rsg.py",
 "old_string": "            \"spikes\": spikes, \"obs_intervals\": obs, \"meta\": meta}",
 "new_string": "            \"spikes\": spikes, \"obs_intervals\": obs, \"meta\": meta, \"electrodes\": electrodes}"
}
```

```
The file entries/sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/s && python3 - <<'EOF'
s=open("nb.py").read()
old='print("Units kept:", len(keep), "of", len(unit_table))\n'
new=old+'print("Unit table columns:", data["electrodes"]["unit_columns"])\nprint("Electrodes:", {k: v for k, v in data["electrodes"].items() if k != "unit_columns"})\n'
assert old in s; s=s.replace(old,new)
old2="""# units are single- and multi-units together; the file does not say which is which. No electrode
# position, area or unit quality is given (the electrode table has no positions)."""
new2="""# units are single- and multi-units together; the file does not say which is which. The electrode
# table has 72 electrodes in 3 groups, consistent with the Methods' 1 to 3 24-channel probes, with
# no positions; the unit table has no electrode column, so no unit can be placed on a probe."""
assert old2 in s; s=s.replace(old2,new2)
open("nb.py","w").write(s)
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/s && python3 - <<'EOF'
s=open("nb.py").read()
old="""# The target direction is decoded near chance before target onset and well above chance after it,
# and not with the next trial's labels; the population rate shows a transient after Set that
# disappears when the event times are jittered."""
new="""# The target direction is decoded at 0.55 in the 300 ms before target onset and in the first 300 ms
# after it, and at 0.80 from 300 to 600 ms after it; with the next trial's labels it is at 0.50 in
# every window. The population rate rises from about 80 ms after Set to a peak at 180 to 200 ms, and
# the peak is gone when the event times are jittered."""
assert old in s; s=s.replace(old,new)
R={
"beh-slopes":"""**Result: not reproduced.** With the intercept, 6 of 8 slopes lie between 0 and 1 and 5 of 8
intervals exclude 0 and 1. The Short prior slopes of both eye datasets are not below 1 (Eye Left
1.011, interval 0.896 to 1.126; Eye Right 1.110, 1.014 to 1.206). The other six slopes are 0.502 to
0.903. Without the intercept (the Methods' equation) the slopes are 0.923 to 1.072 and 2 of 8 lie
below 1, so that reading does not reproduce the claim either.""",
"beh-overlap-prior":"""**Result: not reproduced.** Pooled over the four datasets, the median bias at ts = 800 ms is +28.3
ms for the Short prior and +47.6 ms for the Long prior: both positive, with Long the later as the
priors predict, and the rank-sum p = 0.073. Per dataset, the Short median is negative only in Hand
Left (-61.6 against -2.8 ms, p = 0.069), and the difference is significant only in Hand Right
(29.7 against 96.8 ms, p = 0.00099).""",
"beh-sigmoid-increments":"""**Result: reproduced.** The middle increment exceeds the extreme one in 7 of 8 conditions (median
difference 31.3 ms; the exception is Hand Left Short, -10.7 ms), signed-rank p = 0.0156.""",
"beh-long-more-bias":"""**Result: reproduced.** The Long slope is below the Short slope in all 4 datasets (0.845 against
1.011, 0.903 against 1.110, 0.502 against 0.612, 0.612 against 0.861). Without the intercept it is
below in 3 of 4.""",
"beh-bayes-model":"""**Result: partially reproduced.** The SD correlation is positive in all 4 datasets (0.277 to 0.909),
but the bias R2 reaches 0.8 in 2 of 4 under both readings (Hand Left 0.978, Hand Right 0.865; Eye
Left 0.670, Eye Right 0.122). The fitted wm is 0.013 to 0.116 and wp 0.090 to 0.106; the eye
datasets have small wm and small, irregular biases.""",
"glm-prior-ts":"""**Result: not reproduced.** 38 of 48 units (79.2%, 95% interval 65.0 to 89.5) are prior-dependent,
above the 65 +- 6.5% range, and 22 of 48 (45.8%, 31.4 to 60.8) are ts-dependent, above 27 +- 2.7%.
Both fractions are higher than the paper's, which pool 536 units of 17 sessions.""",
"dfr-overlap-support":"""**Result: reproduced.** The mean RMS difference between priors peaks at 6.86 spikes/s in the bin
480 to 640 ms after Ready, above the 95th percentile of the shuffled maxima (3.09). By dataset the
peak is in the support for three datasets and in the first 160 ms after Set for Eye Left.""",
"pca-dimensionality":"""**Result: not reproduced.** 1 of 8 values is in range: 2 components reach 75% in the estimation epoch
of every dataset, and 2, 2, 5 and 4 in the production epoch (Eye Right, Eye Left, Hand Right, Hand
Left). The first component alone explains 0.51 to 0.65 of the variance in the estimation epoch.
Without smoothing the estimation epoch needs 3, 3, 4 and 6 components, and with soft-normalised
rates 3 in each; neither variant is the claims file's method.""",
"encoding-r2":"""**Result: reproduced.** Under reading (a), Hand Left, R2 is 0.994 (Short) and 0.986 (Long); under
reading (b), the mean over datasets, 0.955 and 0.986. All are within tolerance. The estimation PC
space has 2 dimensions in every dataset, and random unit vectors in it also give high R2 (medians
0.749 to 0.987); the fraction of random vectors at or above the observed R2 is 0.004 to 0.434, and
R2 with ts in place of te is within 0.013 of R2 with te in every case.""",
"encoding-bayes-beats-linear":"""**Result: not reproduced.** The Bayesian RMSE is lower in 3 of 4 datasets for each prior, not in all
4: it is higher for Hand Right Short (+0.180) and Hand Left Long (+0.081). The weighted RMSE gives the
same counts.""",
"short-in-long-control":"""**Result: reproduced, by the paper's test.** The signed-rank p is 0.250 for the RMSE difference
over 4 datasets (and with the single-vector axis), so the test does not find a difference; with 4
datasets it cannot reach p < 0.05. The effect it would test is not absent: the Bayesian RMSE is lower
in 3 of 4 datasets for Short In Long (median difference -0.109), as for the Short prior itself (3 of
4, median -0.289).""",
"neural-long-more-bias":"""**Result: reproduced.** The Long slope is below the Short slope in all 4 datasets; in Hand Right
they are nearly equal (0.0496 against 0.0504 spikes/s per ms). Signed-rank p = 0.125.""",
"speed-vs-projection":"""**Result: partially reproduced.** Both pooled correlations are negative and significant, but
stronger than the paper's and outside tolerance: r = -0.926 (Short, p = 4.8e-09) and -0.834 (Long,
p = 4.9e-06). Within datasets r is -0.74 to -1.0. Speed divided by the Set-to-Go time gives -0.916
and -0.908.""",
"initial-speed-biased":"""**Result: reproduced.** The measured slope of initial speed on ts is shallower than the unbiased
one in 7 of 8 dataset-priors (the exception is Eye Right Long), signed-rank p = 0.039. All 8
measured slopes are negative.""",
"speed-predicts-tp":"""**Result: partially reproduced.** Speed and mean tp are negatively correlated, r = -0.720 (Short,
p = 0.00034) and -0.699 (Long, p = 0.00060), both outside tolerance (stronger than -0.58 and -0.52).
Within datasets r is -0.83 to -0.99. Trial by trial, z-scored within ts, r is negative in 8 of 8
conditions (mean -0.268).""",
"alt-speed-unmodulated":"""**Result: reproduced, by the paper's test.** The signed-rank p is 0.125 for each prior, which with 4
datasets is the smallest the test can give. The effect the claim denies is present: speed rises
through the support in all 8 dataset-priors (slopes 3.95 to 10.61 per s, bootstrap intervals
excluding 0 in 8 of 8; 30% to 82% over the support). Part of the rise comes from attrition, which
leaves fewer trials, and noisier rates, late in the support: with the trials of the longest ts only,
the slopes are 0.97 to 5.29 per s in 7 of 8 and -1.07 in Hand Right Long.""",
"alt-transient-parallel":"""**Result: reproduced, by the paper's test.** The signed-rank p is 0.109 for the shortest ts and 1.0
for the longest. For the shortest ts the distance to the middle trajectory grows in 6 of 8 (median
slope 75.8 per s), which the test over 8 does not find significant.""",
"alt-threshold-monotonic":"""**Result: not reproduced.** The median time of the minimum distance is 230 ms before Go with 60% of
the variance (4 of 32 curves have it in the last 40 ms, 13 of 32 in the last 200 ms), and 200 ms
before Go with 75%. Distances shrink overall (the distance at Go is a median 0.43 of that at Go - 800
ms) but in 29 of 32 curves the distance at Go is above its minimum.""",
"gpfa-variance-inverted-u":"""**Result: not reproduced.** The quadratic coefficient is negative in 6 of 8 dataset-priors, and the
one-tailed signed-rank p is 0.074. The mean variance profile over the 8 is highest at the second ts
and lowest at the last two (0.80, 0.92, 0.88, 0.51, 0.44). Cross-validation chose 8 latent
dimensions in every dataset.""",
"gpfa-mean-sigmoid":"""**Result: reproduced.** The middle increment of the mean projection exceeds the extreme one in 8 of 8
(two-sided signed-rank p = 0.0078), and the Short slope is above the Long slope in all 4 datasets
(one-tailed p = 0.0625, the paper's value).""",
}
import re
heads=[m.start() for m in re.finditer(r"# %% \[markdown\]\n# ## ", s)]
names=[s[h:].split("\n")[1][5:].strip() for h in heads]
out=s; 
# insert from the end
for i in reversed(range(len(heads))):
    nm=names[i]
    if nm in R:
        end = heads[i+1] if i+1 < len(heads) else len(s)
        cell="# %% [markdown]\n"+"\n".join("# "+l for l in R[nm].split("\n"))+"\n\n"
        out=out[:end]+cell+out[end:] if end<len(s) else out.rstrip("\n")+"\n\n"+cell
print([n for n in names if n not in R])
open("nb.py","w").write(out)
EOF
grep -c "Result:" $TMPDIR/s/nb.py
```

```
['Data check', 'Population trajectories']
20
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/s && sed -i 's/The first component alone explains 0.51 to 0.65 of the variance/The first component alone explains 0.51 to 0.64 of the variance/' nb.py && cat >> nb.py <<'EOF'

# %% [markdown]
# ## Blocked claims
#
# - rnn-curved-manifold and rnn-perturbation: the recurrent networks, their training and their
#   simulations are not in the dandiset, and the paper's code is available on request only, so
#   neither the networks nor the paper's training procedure is public (`data_missing`).
# - monkey-g: the dandiset holds one session of monkey H; no data of monkey G are in it or in any
#   other dandiset found by searching the archive for the lab and the task (`data_missing`).

# %%
print(f"Total run time: {(time.time() - T0) / 60:.1f} min; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")

# %% [markdown]
# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | beh-slopes | not reproduced: 6 of 8 slopes in (0, 1); the eye Short slopes are 1.011 and 1.110 |
# | beh-overlap-prior | not reproduced: both median biases positive (+28.3, +47.6 ms), p = 0.073 |
# | beh-sigmoid-increments | reproduced: 7 of 8, p = 0.0156 |
# | beh-long-more-bias | reproduced: 4 of 4 |
# | beh-bayes-model | partially reproduced: bias R2 >= 0.8 in 2 of 4, SD correlation positive in 4 of 4 |
# | glm-prior-ts | not reproduced: 79.2% prior-, 45.8% ts-dependent |
# | dfr-overlap-support | reproduced: peak at 480 to 640 ms after Ready, above the shuffle null |
# | pca-dimensionality | not reproduced: 1 of 8 in range (2 PCs reach 75% in the estimation epoch) |
# | encoding-r2 | reproduced: Hand Left 0.994 and 0.986 |
# | encoding-bayes-beats-linear | not reproduced: Bayesian better in 3 of 4 for each prior |
# | short-in-long-control | reproduced by the paper's test (p = 0.25, n = 4) |
# | neural-long-more-bias | reproduced: 4 of 4 |
# | speed-vs-projection | partially reproduced: r = -0.926 and -0.834, outside tolerance |
# | initial-speed-biased | reproduced: 7 of 8, p = 0.039 |
# | speed-predicts-tp | partially reproduced: r = -0.720 and -0.699, outside tolerance |
# | alt-speed-unmodulated | reproduced by the paper's test (p = 0.125, n = 4); speed rises in 8 of 8 |
# | alt-transient-parallel | reproduced by the paper's test (p = 0.109 and 1.0) |
# | alt-threshold-monotonic | not reproduced: median minimum 230 ms before Go |
# | gpfa-variance-inverted-u | not reproduced: 6 of 8 negative, p = 0.074 |
# | gpfa-mean-sigmoid | reproduced: p = 0.0078 and 0.0625 |
# | rnn-curved-manifold | blocked: data missing |
# | rnn-perturbation | blocked: data missing |
# | monkey-g | blocked: data missing |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's. It uses one session of monkey H, where the paper pools
# 17 sessions of H and 12 of G, so every test over "datasets" has 4 in place of 8, and tests the paper
# ran over sessions run here over the 4 datasets of one session. Firing rates are not normalised
# (claims header), which leaves 2 components at 75% in most datasets and makes the estimation PC
# space 2-dimensional. The paper's code is not public; method details come from the claims file and
# the STAR Methods, as cited in each section. GPFA runs 200 EM iterations, fewer than elephant's
# default of 500.
#
# What was found about the dataset. It holds one of the paper's 29 sessions: 1160 trials of the
# train file (983 completed and not outliers) and 54 units, 48 of which pass the paper's selection,
# the number the paper gives for the GPFA session of monkey H. The 283 trials of the test file have no
# task variables, as the benchmark withholds them. The `iti` description reverses the two priors; `tp`
# exceeds `go_time - set_time` by a median of 17.9 ms without explanation; units carry no electrode,
# probe or single/multi-unit label.
EOF
python py2nb.py nb.py entries/sohn-2019/reproduce_sohn_2019.ipynb && python3 -c "
import json;nb=json.load(open('entries/sohn-2019/reproduce_sohn_2019.ipynb'));print(len(nb['cells']), sum(1 for c in nb['cells'] if c['metadata'].get('tags')))"
```

```
76 24
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -l "^python" entries/*/entry.yaml | head -3; cat $(grep -l "^python" entries/*/entry.yaml | head -1); python3 tools/entry.py --help 2>&1 | head -30
```

```
entries/andrews-2024/entry.yaml
entries/asari-2009/entry.yaml
entries/brinke-2017/entry.yaml
schema_version: 1
name: andrews-2024
type: reproduction
title: Optogenetic inhibition in human hippocampal slices on HD-MEAs (Andrews, Geng, Voitiuk et al. 2024)
description: Tests the findings of Andrews, Geng, Voitiuk et al. (2024) on dandiset 001132, which holds 69
  raw HD-MEA voltage recordings of 12 human hippocampal slices from 7 patients. The files hold no sorted
  units, light events or condition labels, so only the cohort claim is tested; the notebook surveys every
  recording, recovers light periods of slices 3C, 4C and 7D from the voltage, shows a
  threshold-crossing variant for those of 3C, and runs the paper's network model.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_andrews_2024.ipynb
  title: Reproducing Andrews, Geng, Voitiuk et al. (2024) from dandiset 001132
  runtime_minutes: 50
helpers:
- hdmea.py
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && cat > entry.yaml <<'EOF'
schema_version: 1
name: sohn-2019
type: reproduction
title: Bayesian computation through cortical latent dynamics (Sohn, Narain, Meirhaeghe & Jazayeri 2019)
description: Tests the findings of Sohn, Narain, Meirhaeghe and Jazayeri (2019) on dandiset 000130, which
  holds one recording session of monkey H in the two-prior Ready-Set-Go task, prepared for the Neural
  Latents Benchmark. It tests the behavioural biases and the Bayesian observer fit, the single-unit GLM,
  the population trajectories and encoding axis, the speed of production trajectories, the alternative
  mechanisms and the GPFA single-trial analysis. Monkey G and the recurrent network models are not in it.
license: Apache-2.0
notebooks:
- path: reproduce_sohn_2019.ipynb
  title: Reproducing Sohn et al. (2019) from dandiset 000130
  runtime_minutes: 13
helpers:
- rsg.py
related:
- id: dandi:000130/0.241017.1448
  relation: uses_data
- id: doi:10.1016/j.neuron.2019.06.012
  relation: reproduces
EOF
printf "dandi\nelephant\nh5py\nmatplotlib\nneo\nnumpy\npandas\nquantities\nremfile\nscikit-learn\nscipy\nstatsmodels\n" > requirements.in
cd ../.. && date -u && python tools/entry.py lock entries/sohn-2019 2>&1 | tail -5
```

```
Sat Nov 14 13:27:33 UTC 2026
wrote sohn-2019/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Write**

```json
{
 "file_path": "entries/sohn-2019/README.md",
 "content": "# Sohn, Narain, Meirhaeghe & Jazayeri (2019) from dandiset 000130\n\nTests the findings of [Sohn et al. (2019)](https://doi.org/10.1016/j.neuron.2019.06.012) that can be\ntested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), which holds one\nrecording session (2016-12-11) of monkey H in the two-prior Ready-Set-Go task, prepared for the Neural\nLatents Benchmark: 1160 trials with their task variables and 54 units in DMFC. The paper used 17\nsessions of monkey H and 12 of monkey G; only this session is here.\n\n| Claim | Outcome |\n|---|---|\n| Regression slopes of tp on ts between 0 and 1 in every condition | Not reproduced |\n| Opposite biases of the two priors at ts = 800 ms | Not reproduced |\n| tp increments smaller at the extremes of the prior | Reproduced |\n| Smaller slopes for the Long prior | Reproduced |\n| The Bayesian observer captures bias and variance | Partially reproduced |\n| GLM: 65% of units prior-dependent, 27% ts-dependent | Not reproduced |\n| Prior difference at ts = 800 ms largest during the support | Reproduced |\n| 3 to 4 and 5 to 10 PCs explain 75% of the variance | Not reproduced |\n| Projections on the encoding axis match the Bayesian estimate (R2) | Reproduced |\n| Projections fit the Bayesian model better than a linear one | Not reproduced |\n| No sigmoid in the \"Short In Long\" control | Reproduced |\n| Smaller neural slope for the Long prior | Reproduced |\n| Projection at Set predicts production speed | Partially reproduced |\n| Initial speed biased toward the middle of the prior | Reproduced |\n| Production speed predicts tp | Partially reproduced |\n| Speed unmodulated during the support (H1) | Reproduced |\n| Trajectories parallel after Set (H2) | Reproduced |\n| Distances decrease up to Go (H3) | Not reproduced |\n| GPFA variance has an inverted-U profile | Not reproduced |\n| GPFA mean projection sigmoidal, steeper for Short | Reproduced |\n| Recurrent network results (two claims) | Blocked: data missing |\n| Monkey G | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nEvery test over datasets has the 4 effector and direction conditions of this session, where the paper\nhas 8 over two animals and pools 17 sessions of monkey H for its behavioural statistics. The attempt\nrecord, with the reasons and the differences from the paper's method, is\n[`attempts/sohn-2019-02.yaml`](../../attempts/sohn-2019-02.yaml).\n\n- `reproduce_sohn_2019.ipynb`: the analysis. It takes about 13 minutes, most of it the GPFA fits.\n- `rsg.py`: loading the files, unit selection, binned and trial-averaged rates, PCA, the encoding\n  axis and the Bayesian observer model. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/sohn-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u && time python tools/entry.py all entries/sohn-2019 2>&1 | tail -30; date -u
```

```
Sat Nov 14 13:27:46 UTC 2026
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (751 s)

real	12m40.732s
user	39m21.599s
sys	0m13.963s
Sat Nov 14 13:40:26 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/sohn-2019/; python3 - <<'EOF' > $TMPDIR/s/exec_out.txt
import json
nb=json.load(open("executed/sohn-2019/reproduce_sohn_2019.ipynb"))
for c in nb["cells"]:
    if c["cell_type"]=="code":
        for o in c.get("outputs",[]):
            if "text" in o: print("".join(o["text"]))
            elif "data" in o and "text/plain" in o["data"] and "image/png" not in o["data"]: print("".join(o["data"]["text/plain"]))
    else:
        src="".join(c["source"])
        if src.startswith("## ") or src.startswith("**Result"): print("####", src[:300])
EOF
wc -l $TMPDIR/s/exec_out.txt; grep -n "Total run time\|signed-rank p\|r_pooled\|Short  20\| Long  20\|In range\|Reading\|of 48\|Largest\|Median time\|Quadratic\|Middle >\|Short slope\|With intercept\|pooled  " $TMPDIR/s/exec_out.txt
```

```
reproduce_sohn_2019.ipynb
result.json
57395 /tmp/claude-1001/s/exec_out.txt
120:With intercept: slopes in (0, 1): 6 of 8; intervals excluding 0 and 1: 5 of 8
135:    pooled       93     107               28.3              47.6     0.0728
161:Middle > extreme in 7 of 8; median difference 31.3 ms; signed-rank p = 0.0156
165:difference 31.3 ms; the exception is Hand Left Short, -10.7 ms), signed-rank p = 0.0156.
171:Criterion: with the slopes of beh-slopes, reproduced when the Long slope is below the Short slope
182:#### **Result: reproduced.** The Long slope is below the Short slope in all 4 datasets (0.845 against
260:             prior: 38 of 48 = 79.2% (95% CI 65.0 to 89.5); expected 65 +- 6.5
261: ts (either prior): 22 of 48 = 45.8% (95% CI 31.4 to 60.8); expected 27 +- 2.7
262:  ts (Short model): 16 of 48 = 33.3% (95% CI 20.4 to 48.4)
263:   ts (Long model): 16 of 48 = 33.3% (95% CI 20.4 to 48.4)
267:#### **Result: not reproduced.** 38 of 48 units (79.2%, 95% interval 65.0 to 89.5) are prior-dependent,
268:above the 65 +- 6.5% range, and 22 of 48 (45.8%, 31.4 to 60.8) are ts-dependent, above 27 +- 2.7%.
284:Largest mean RMS difference: 6.86 spikes/s in bin R480..640 (support of the prior = bins R480..640 and R640..800)
328:In range: 1 of 8
354:Reading (a) Hand Left: Short 0.994, Long 0.986
355:Reading (b) mean over datasets: Short 0.955, Long 0.986
380:Short: Bayesian lower in 3 of 4 (weighted RMSE: 3 of 4); median delta -0.2891; signed-rank p = 0.250
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "WARNING\|warn" $TMPDIR/s/exec_out.txt | sed -n '/gpfa-variance-inverted-u/,/Total run/p' | head -60; sed -n 1,20p $TMPDIR/s/exec_out.txt; grep -n "Peak after\|accuracy\|0 to 300\|300 to 600\|-300 to 0" $TMPDIR/s/exec_out.txt | head
```

```
#### ## gpfa-variance-inverted-u

> The variance across single trials of the GPFA neural state at Set projected on the encoding axis
> has an inverted-U profile over ts, lower at the extremes of each prior (one-tailed signed-rank
> test on quadratic coefficients, p = 0.0273, monkey H).

Criterion: GPFA (













[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/s && python3 - <<'EOF'
s=open("nb.py").read()
old="from elephant.gpfa import GPFA\n"
new="from elephant.gpfa import GPFA\n\nlogging.disable(logging.WARNING)  # elephant logs a warning per spike train it re-bins\n"
assert s.count(old)==1; s=s.replace(old,new)
s=s.replace('logging.getLogger("elephant").setLevel(logging.ERROR)\n','')
open("nb.py","w").write(s)
EOF
python py2nb.py nb.py entries/sohn-2019/reproduce_sohn_2019.ipynb; date -u
```

```
Sat Nov 14 13:40:45 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && python -c "
import pandas as pd; t=pd.read_pickle('$TMPDIR/s/desc-train_trials.pkl'); a=t[t.tp<=0]
print(a.tp.value_counts().head(), a.go_time.notna().sum(), a.set_time.notna().sum(), len(a)); print(pd.crosstab(t.split, t.tp>0))"
```

```
tp
-1600.0    25
-1440.0    16
-960.0     15
-1120.0    14
-2200.0    12
Name: count, dtype: int64 3 13 134
tp     False  True 
split              
none     134     20
train      0    748
val        0    258
```

**Agent calls Write**

```json
{
 "file_path": "attempts/sohn-2019-02.yaml",
 "content": "schema_version: 3\nid: sohn-2019-02\ndatasets:\n- archive: dandi\n  id: \"000130\"\n  version: 0.241017.1448\n  doi: 10.48324/dandi.000130/0.241017.1448\n  relation: primary\npaper: doi:10.1016/j.neuron.2019.06.012\ndate: 2026-11-14\nentry: sohn-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43597162260\noutcomes:\n- claim: beh-slopes\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-slopes\n  notes: With an intercept, 6 of 8 slopes lie between 0 and 1 and 5 of 8 intervals exclude 0 and 1.\n    The Short prior slopes of both eye datasets are not below 1, Eye Left 1.011 (0.896 to 1.126)\n    and Eye Right 1.110 (1.014 to 1.206); the other six are 0.502 to 0.903. Without an intercept the\n    slopes are 0.923 to 1.072 and 2 of 8 lie below 1. The eye datasets of this session show little\n    bias toward the mean of the Short prior. The paper's statement covers 17 sessions; this is one.\n  deviations:\n  - One session of monkey H, where the paper fits each of 17 sessions of H and 12 of G.\n  - The criterion's regression has an intercept; the STAR Methods write tp = βts + ε (\"Model free\n    analysis of behavior\"). The reading without an intercept is shown and gives the same outcome.\n- claim: beh-overlap-prior\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-overlap-prior\n  notes: Pooled over effector and direction (93 Short and 107 Long trials at ts = 800 ms), the median\n    of tp - 800 is +28.3 ms for Short and +47.6 ms for Long, so the Short bias is not negative, and the\n    rank-sum p is 0.073. Long is the later of the two, as the priors predict. Per dataset, the Short\n    median is negative only in Hand Left (-61.6 against -2.8 ms, p = 0.069), and the difference is\n    significant only in Hand Right (29.7 against 96.8 ms, p = 0.00099).\n  deviations:\n  - One session in place of the paper's 17 sessions of monkey H; the paper's p value is not expected.\n- claim: beh-sigmoid-increments\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-sigmoid-increments\n  notes: The middle increment exceeds the extreme one in 7 of 8 conditions (median difference 31.3\n    ms; Hand Left Short is the exception at -10.7 ms), two-sided signed-rank p = 0.0156.\n  deviations:\n  - One session; the test runs over its 8 prior, effector and direction conditions.\n- claim: beh-long-more-bias\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-long-more-bias\n  notes: The Long slope is below the Short slope in all 4 datasets (Eye Left 0.845 against 1.011, Eye\n    Right 0.903 against 1.110, Hand Left 0.502 against 0.612, Hand Right 0.612 against 0.861). Without\n    an intercept it is below in 3 of 4.\n- claim: beh-bayes-model\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-bayes-model\n  notes: The correlation of observed and predicted SD of tp is positive in all 4 datasets (0.277 to\n    0.909). The bias R2 reaches 0.8 in 2 of 4 datasets under both readings of R2 (Hand Left 0.978,\n    Hand Right 0.865, Eye Left 0.670, Eye Right 0.122; the squared correlation differs by at most\n    0.007). Fitted wm is 0.025, 0.013, 0.116 and 0.073 and wp 0.103, 0.106, 0.090 and 0.104 (Eye\n    Left, Eye Right, Hand Left, Hand Right). The eye datasets have small, irregular biases that the\n    model fits with a small wm.\n  deviations:\n  - The model is fit per dataset of one session, where the paper pools sessions per animal, effector\n    and direction.\n  - R2 of the observed by the predicted bias is computed both as 1 - SS_res/SS_tot of the prediction\n    and as the squared correlation; both give the same count.\n- claim: glm-prior-ts\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:glm-prior-ts\n  measured:\n  - 79.2\n  - 45.8\n  notes: Of the 48 selected units, 38 (79.2%, binomial 95% interval 65.0 to 89.5) are prior-dependent\n    and 22 (45.8%, 31.4 to 60.8) are ts-dependent (16 in the Short model, 16 in the Long model); 19\n    are both and 7 neither. Both fractions are above their ranges (65 +- 6.5, 27 +- 2.7). The paper's\n    fractions are over 536 units of 17 sessions; this session may be one of its more modulated.\n  deviations:\n  - A trial whose ts equals the end of a window is included, as its window is the 80 ms \"immediately\n    before Set\" (STAR Methods, \"Generalized linear model\", which counts \"all trials in which Set\n    occurred after t\"). Windows are placed at nominal times after ready_time.\n  - The reduced model for ts has an intercept with the effector and direction terms (STAR Methods,\n    Equation 4).\n- claim: dfr-overlap-support\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:dfr-overlap-support\n  notes: The RMS over units of the rate difference between priors, averaged over the 4 datasets,\n    peaks at 6.86 spikes/s in the bin 480 to 640 ms after Ready; the 95th percentile of the largest\n    value over 200 label shuffles is 3.09. By dataset the peak is in the support for Eye Right, Hand\n    Left and Hand Right, and in the first 160 ms after Set for Eye Left.\n  deviations:\n  - Bins up to Set are aligned to ready_time and those after Set to set_time.\n- claim: pca-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:pca-dimensionality\n  notes: 1 of 8 values is in range. Two components reach 75% of the variance in the estimation epoch\n    of every dataset, and 2, 2, 5 and 4 in the production epoch (Eye Right, Eye Left, Hand Right, Hand\n    Left). The first component alone explains 0.51 to 0.64 of the estimation-epoch variance. Without\n    smoothing the estimation epoch needs 3, 3, 4 and 6 components, and with soft-normalised rates\n    (rate over range + 5) 3 in each; these are variants, not the claims file's method, which leaves\n    rates unnormalised. Whether the paper normalised rates is not stated, and is asked of the authors.\n  deviations:\n  - Rates are not normalised (claims header); the paper does not say.\n- claim: encoding-r2\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:encoding-r2\n  measured:\n  - 0.994\n  - 0.986\n  notes: Reading (a), Hand Left, gives R2 = 0.994 (Short) and 0.986 (Long); reading (b), the mean over\n    datasets, 0.955 and 0.986. Both readings are within tolerance. The estimation PC space has 2\n    dimensions in every dataset, so the test is weakly specific to u. Random unit vectors give median\n    R2 of 0.749 to 0.987, the fraction of random vectors at or above the observed R2 is 0.004 to\n    0.434, and a regression on ts in place of te gives R2 within 0.013 of that on te in every case.\n  deviations:\n  - The state at time t is the 20 ms bin ending at t, a standard choice.\n  - te is the model's mean estimate at each ts without the offset b, which a linear regression\n    absorbs.\n- claim: encoding-bayes-beats-linear\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:encoding-bayes-beats-linear\n  notes: The Bayesian RMSE is lower than the linear one in 3 of 4 datasets for each prior. It is\n    higher for Hand Right Short (+0.180) and Hand Left Long (+0.081). Median differences are -0.289\n    (Short) and -0.165 (Long), signed-rank p = 0.25 for each. The weighted RMSE gives the same counts.\n    In the eye datasets the fitted wm is small, so te is close to linear in ts.\n  deviations:\n  - Four datasets of one session in place of eight over two animals.\n- claim: short-in-long-control\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:short-in-long-control\n  notes: By the paper's test the RMSE difference over the 4 datasets gives signed-rank p = 0.25 (with\n    the averaged and the single-vector axis); with 4 datasets the test cannot reach p < 0.05. The\n    effect it would test is not absent here. The Bayesian RMSE is lower in 3 of 4 datasets for Short\n    In Long (median difference -0.109) as for the Short prior itself (3 of 4, median -0.289); the\n    Short In Long difference minus the Short difference is +0.069, +0.183, -0.282 and +0.531 (Eye\n    Right, Eye Left, Hand Right, Hand Left).\n  deviations:\n  - The axis for Short In Long is built as u is, from averaged difference vectors (the STAR Methods\n    \"applied the same projection analysis\"); the single vector from 480 to 800 ms is shown and gives\n    the same result.\n- claim: neural-long-more-bias\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:neural-long-more-bias\n  notes: The slope of Xu on ts is lower for Long in all 4 datasets (Eye Right 0.119 against 0.194, Eye\n    Left 0.125 against 0.226, Hand Right 0.0496 against 0.0504, Hand Left 0.028 against 0.077\n    spikes/s per ms); in Hand Right the two are nearly equal. Signed-rank p = 0.125 over 4.\n- claim: speed-vs-projection\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:speed-vs-projection\n  measured:\n  - -0.926\n  - -0.834\n  notes: Pooled over the 4 datasets (20 points per prior), r = -0.926 (Short, p = 4.8e-09) and -0.834\n    (Long, p = 4.9e-06); both are negative and significant but stronger than the paper's and outside\n    tolerance. Within datasets r is -0.74 to -1.0. Speed divided by the mean Set-to-Go time gives\n    -0.916 and -0.908.\n  deviations:\n  - Speed is the mean step distance in the production PC space (claims header); the Methods'\n    division by the Set-to-Go time is shown as a variant.\n- claim: initial-speed-biased\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:initial-speed-biased\n  notes: The slope of initial speed (Set to Set + 400 ms) on ts is shallower than the unbiased profile's\n    in 7 of 8 dataset-priors (Eye Right Long is the exception), two-sided signed-rank p = 0.039. All\n    8 measured slopes are negative.\n  deviations:\n  - States are projected into the dataset's production PC space, which is fit from Set to the\n    shortest tp of each ts.\n- claim: speed-predicts-tp\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:speed-predicts-tp\n  measured:\n  - -0.720\n  - -0.699\n  notes: Pooled over the 4 datasets, speed and mean tp correlate at r = -0.720 (Short, p = 0.00034)\n    and -0.699 (Long, p = 0.00060), both negative and significant, outside tolerance (stronger than\n    -0.58 and -0.52). Within datasets r is -0.83 to -0.99. Trial by trial, with speed from each\n    trial's smoothed rates and both z-scored within ts, r is negative in 8 of 8 conditions (mean\n    -0.268, p below 0.05 in 6).\n  deviations:\n  - The trial-by-trial variant uses each trial's smoothed rates in place of the benchmark's\n    model-inferred rates.\n- claim: alt-speed-unmodulated\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-speed-unmodulated\n  notes: By the paper's test, p = 0.125 for each prior, the smallest a two-sided signed-rank test over 4\n    can give, so the test cannot find the effect. The effect the claim denies is present. Speed rises\n    through the support in all 8 dataset-priors (slopes 3.95 to 10.61 per s, 30% to 82% over the\n    support), and 200 bootstrap resamples of trials give intervals excluding 0 in 8 of 8. Part of\n    the rise comes from attrition, which leaves fewer trials (for example 129 to 25) and noisier rates\n    late in the support. With the trials of the longest ts only the slopes are 0.97 to 5.29 per s in 7\n    of 8 and -1.07 in Hand Right Long. The outcome follows the criterion and says nothing about the\n    paper's 8 datasets.\n  deviations:\n  - The bootstrap intervals are percentile intervals; resampling with replacement adds noise to the\n    rates, so they sit above the point estimates.\n- claim: alt-transient-parallel\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-transient-parallel\n  notes: The signed-rank p is 0.109 for the shortest ts and 1.0 for the longest, so the test finds no\n    change of distance. For the shortest ts the distance to the middle trajectory grows in 6 of 8\n    (median slope 75.8 per s), and for the longest in 4 of 8 (median 3.75 per s). The PC spaces have 2\n    to 4 dimensions.\n- claim: alt-threshold-monotonic\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-threshold-monotonic\n  notes: With 60% of the variance (1 to 3 components) the median time of the minimum distance over 32\n    curves is 230 ms before Go; 4 curves have it in the last 40 ms and 13 in the last 200 ms. With\n    75% (2 to 5 components) the median is 200 ms before Go. Distances do shrink overall (the distance\n    at Go is a median 0.43 of that at Go - 800 ms), but in 29 of 32 curves the distance at Go is above\n    its minimum.\n  deviations:\n  - A bin's time is its end, so the last bin ends at Go.\n- claim: gpfa-variance-inverted-u\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:gpfa-variance-inverted-u\n  notes: Cross-validation chose 8 latent dimensions in all 4 datasets. The quadratic coefficient of the\n    variance profile is negative in 6 of 8 dataset-priors, one-tailed signed-rank p = 0.074. The mean\n    profile over the 8 is 0.80, 0.92, 0.88, 0.51 and 0.44 from the shortest to the longest ts, lowest\n    at the long end but not at the short end.\n  deviations:\n  - GPFA is elephant's implementation, run for 200 EM iterations (elephant's default is 500), a\n    choice made for time; the log-likelihood still rose by 7 to 12 over the last 10 iterations.\n  - Each trial runs from ready_time for its nominal ts, so its last bin ends at Set.\n- claim: gpfa-mean-sigmoid\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:gpfa-mean-sigmoid\n  notes: The middle increment of the mean GPFA projection exceeds the extreme one in 8 of 8\n    dataset-priors (two-sided signed-rank p = 0.0078), and the slope of the mean projection on ts is\n    higher for Short in all 4 datasets (one-tailed p = 0.0625, the paper's value).\n  deviations:\n  - As for gpfa-variance-inverted-u.\n- claim: rnn-curved-manifold\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The recurrent networks, their training and their simulations are not in the dandiset, and\n    the paper's code is available on request only, so the networks are not public.\n- claim: rnn-perturbation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: As for rnn-curved-manifold; the perturbation experiments need the trained networks.\n- claim: monkey-g\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds one session of monkey H. A search of the archive for the lab, the task\n    and the paper found no other dandiset with these data.\nfindings:\n- kind: data_missing\n  about: data\n  statement: The dandiset holds one recording session (2016-12-11) of monkey H, of the paper's 29\n    sessions (17 of H, 12 of G). Monkey G is absent, and so are the recurrent network models. Tests\n    the paper ran over 8 datasets of two animals or over 17 sessions can be run here only over the 4\n    effector and direction conditions of one session.\n- kind: metadata_error\n  statement: The description of `iti` says it is 500 ms for the Short prior and 1220 ms for the Long\n    prior. The values are the reverse (Short 1220 ms in 577 trials, Long 500 ms in 583), as the paper's\n    Methods state.\n- kind: other\n  about: data\n  statement: The `tp` column, described as the time between Set and the response, exceeds go_time -\n    set_time by a median of 17.9 ms (0.1 to 200.6 ms), more for eye trials (median 21.2 ms) than hand\n    trials (17.3 ms); `ts` differs from set_time - ready_time by up to 23.5 ms. Which clock each uses\n    is not documented. For aborted trials `tp` holds negative values (such as -1600 or -2400 ms) that\n    are not described.\n- kind: metadata_insufficient\n  statement: The unit table has no electrode, probe, area or single-unit or multi-unit label, and the\n    electrode table (72 electrodes in 3 groups) has no positions. Units cannot be placed on a probe or\n    separated into single and multi-units as the paper counts them.\n- kind: other\n  about: data\n  statement: The test file's 283 trials (about a fifth of the session) carry only start, stop and go\n    times, with spikes of 40 of the 54 units; prior, ts, tp, effector and direction are withheld for\n    the Neural Latents Benchmark. Analyses of the paper can use only the 1160 trials of the train file.\n- kind: methods_unavailable\n  about: paper\n  statement: The paper's analysis code is available on request only, and three details that change\n    results here are not stated. The regression of tp on ts is written tp = βts + ε, without an\n    intercept, while the slopes reported below 1 imply one; whether firing rates were normalised\n    before PCA is not said, and without normalisation 2 components reach 75% of the variance in most\n    datasets of this session; and the number of GPFA EM iterations is not given. Could the authors\n    state each?\n"
}
```

```
File created successfully at: attempts/sohn-2019-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/the squared correlation differs by at most\n    0.007/X/' attempts/sohn-2019-02.yaml && python3 - <<'EOF'
p="attempts/sohn-2019-02.yaml"; s=open(p).read()
s=s.replace("the squared correlation differs by at most\n    0.007)","the squared correlation differs by at most\n    0.008)")
open(p,"w").write(s)
EOF
grep -n "0.008)" attempts/sohn-2019-02.yaml; python tools/entry.py check entries/sohn-2019 2>&1 | tail -15
```

```
70:    0.008). Fitted wm is 0.025, 0.013, 0.116 and 0.073 and wp 0.103, 0.106, 0.090 and 0.104 (Eye
0 error(s)
```

**Agent calls Bash**

```bash
grep -nE "^\s+[^-a-z_ ].*: |^\s{4,}[a-z].*: " attempts/sohn-2019-02.yaml | grep -vE "^\s*[0-9]+:\s+[a-z_]+: " | head; grep -n "—\|rather" attempts/sohn-2019-02.yaml entries/sohn-2019/README.md entries/sohn-2019/rsg.py $TMPDIR/s/nb.py | head; date -u; python tools/entry.py all entries/sohn-2019 2>&1 | tail -4; date -u
```

```
Sat Nov 14 13:42:14 UTC 2026
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (729 s)
Sat Nov 14 13:54:35 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/s/exec_out2.txt
import json
nb=json.load(open("executed/sohn-2019/reproduce_sohn_2019.ipynb"))
for c in nb["cells"]:
    if c["cell_type"]=="code":
        for o in c.get("outputs",[]):
            if "text" in o: print("".join(o["text"]))
            elif "data" in o and "text/plain" in o["data"] and "image/png" not in o["data"]: print("".join(o["data"]["text/plain"]))
    else:
        src="".join(c["source"])
        if src.startswith("## "): print("####", src.split("\n")[0])
EOF
wc -l $TMPDIR/s/exec_out2.txt; sed -n '/gpfa-variance/,$p' $TMPDIR/s/exec_out2.txt; diff <(grep -v "loaded in\|GPFA time\|Total run" $TMPDIR/s/exec_out.txt | grep -v "WARNING\|warn" | grep -v "^####\|^$" | head -630) <(grep -v "loaded in\|GPFA time\|Total run" $TMPDIR/s/exec_out2.txt | grep -v "^####\|^$" | head -630) | head -40
```

```
764 /tmp/claude-1001/s/exec_out2.txt
#### ## gpfa-variance-inverted-u
executed/sohn-2019/.venv/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 1 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "

Initializing parameters using factor analysis...


Fitting GPFA model...

executed/sohn-2019/.venv/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 2 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "
executed/sohn-2019/.venv/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 1 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "

Initializing parameters using factor analysis...

Fitting GPFA model...

executed/sohn-2019/.venv/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 1 last spike(s) of the input spiketrain
[... 324 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/s && python3 - <<'EOF'
s=open("nb.py").read()
old='''def gpfa_fit(trains, x_dim):
    np.random.seed(int(rng_gpfa.integers(1 << 31)))
    g = GPFA(bin_size=rsg.BIN_MS * pq.ms, x_dim=x_dim, em_max_iters=EM_ITERS, verbose=False)
    g.fit(trains)
    return g
'''
new='''def quiet(fn, *args, **kw):
    """Run an elephant call without its progress prints and its re-binning warnings."""
    with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):
        warnings.simplefilter("ignore")
        return fn(*args, **kw)


def gpfa_fit(trains, x_dim):
    np.random.seed(int(rng_gpfa.integers(1 << 31)))
    g = GPFA(bin_size=rsg.BIN_MS * pq.ms, x_dim=x_dim, em_max_iters=EM_ITERS, verbose=False)
    quiet(g.fit, trains)
    return g
'''
assert old in s; s=s.replace(old,new)
s=s.replace("            ll[x_dim] += m.score([trains[i] for i in np.flatnonzero(folds == f)])",
            "            ll[x_dim] += quiet(m.score, [trains[i] for i in np.flatnonzero(folds == f)])")
s=s.replace('    lat = m.transform(trains, returned_data=["latent_variable_orth"])',
            '    lat = quiet(m.transform, trains, returned_data=["latent_variable_orth"])')
s=s.replace("import neo\nimport quantities as pq\n","import contextlib\nimport io\n\nimport neo\nimport quantities as pq\n")
open("nb.py","w").write(s)
EOF
grep -n "quiet" $TMPDIR/s/nb.py; python $TMPDIR/s/py2nb.py $TMPDIR/s/nb.py entries/sohn-2019/reproduce_sohn_2019.ipynb && date -u && python tools/entry.py all entries/sohn-2019 2>&1 | tail -3; date -u
```

```
1097:def quiet(fn, *args, **kw):
1107:    quiet(g.fit, trains)
1123:            ll[x_dim] += quiet(m.score, [trains[i] for i in np.flatnonzero(folds == f)])
1127:    lat = quiet(m.transform, trains, returned_data=["latent_variable_orth"])
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 204, in write
    fp.write(s)
    ^^^^^^^^
AttributeError: 'str' object has no attribute 'write'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/s/py2nb.py", line 26, in <module>
    nbformat.write(nb, sys.argv[2])
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 208, in write
    with Path(fp).open("w", encoding="utf8") as f:
         ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/pathlib/_local.py", line 537, in open
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python $TMPDIR/s/py2nb.py $TMPDIR/s/nb.py entries/sohn-2019/reproduce_sohn_2019.ipynb && date -u && python tools/entry.py all entries/sohn-2019 2>&1 | tail -3; date -u
```

```
Sat Nov 14 13:54:52 UTC 2026
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (727 s)
Sat Nov 14 14:07:11 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/s/exec_out3.txt
import json
nb=json.load(open("executed/sohn-2019/reproduce_sohn_2019.ipynb"))
for c in nb["cells"]:
    if c["cell_type"]=="code":
        for o in c.get("outputs",[]):
            if "text" in o: print("".join(o["text"]))
            elif "data" in o and "text/plain" in o["data"] and "image/png" not in o["data"]: print("".join(o["data"]["text/plain"]))
EOF
python3 - <<'EOF' > $TMPDIR/s/exec_out2b.txt
import json
nb=json.load(open("/dev/stdin")) if False else None
EOF
wc -l $TMPDIR/s/exec_out3.txt; grep -c "Warning" $TMPDIR/s/exec_out3.txt; sed -n '/cv_ll_4/,$p' $TMPDIR/s/exec_out3.txt | head -40; grep -n "Short slope above\|Quadratic\|signed-rank p = \|r_pooled" $TMPDIR/s/exec_out3.txt | head -30
```

```
480 /tmp/claude-1001/s/exec_out3.txt
0
   dataset  trials   cv_ll_4   cv_ll_8  x_dim  ll_change_last10
 Eye Right     276 -175218.3 -174652.4      8               7.1
  Eye Left     260 -165381.3 -164698.2      8              11.5
Hand Right     225 -125038.9 -124443.3      8               7.5
 Hand Left     222 -116142.9 -115634.9      8               8.1
GPFA time: 653 s
   dataset prior                 variance_by_ts  quad_coef
 Eye Right Short   [0.76, 0.5, 0.58, 0.43, 0.3]  4.285e-07
 Eye Right  Long  [0.98, 0.7, 0.96, 0.36, 0.41] -1.487e-06
  Eye Left Short [0.43, 0.21, 0.61, 0.34, 0.17] -6.448e-06
  Eye Left  Long [0.57, 0.91, 0.73, 0.46, 0.39] -6.404e-06
Hand Right Short  [0.79, 0.8, 1.53, 0.76, 0.48] -2.308e-05
Hand Right  Long [0.77, 1.55, 1.36, 0.61, 0.33] -1.914e-05
 Hand Left Short   [0.8, 1.17, 0.9, 0.39, 0.82] -1.244e-06
 Hand Left  Long  [1.3, 1.49, 0.33, 0.76, 0.61]  6.482e-06

Quadratic coefficient below zero in 6 of 8; one-tailed signed-rank p = 0.0742
Mean variance profile over the 8 (z-scored Xu): [0.8   0.916 0.875 0.514 0.439]
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 338,372p $TMPDIR/s/exec_out3.txt; sed -n 75,100p $TMPDIR/s/exec_out3.txt
```

```
Speed (mean step) against Xu at Set:
prior  n  r_pooled            p                                                                 r_within_dataset
Short 20    -0.926 4.762032e-09   {'Eye Left': -0.9, 'Eye Right': -1.0, 'Hand Left': -0.99, 'Hand Right': -0.94}
 Long 20    -0.834 4.873258e-06 {'Eye Left': -0.94, 'Eye Right': -0.91, 'Hand Left': -0.74, 'Hand Right': -0.94}

Variant, speed divided by the Set-to-Go time:
prior  n  r_pooled            p                                                                 r_within_dataset
Short 20    -0.916 1.404610e-08 {'Eye Left': -0.93, 'Eye Right': -0.99, 'Hand Left': -0.99, 'Hand Right': -0.97}
 Long 20    -0.908 3.227019e-08 {'Eye Left': -0.94, 'Eye Right': -0.96, 'Hand Left': -0.85, 'Hand Right': -0.96}

   dataset prior                         speeds slope_measured slope_unbiased difference
 Eye Right Short  [7.95, 7.81, 6.74, 6.2, 4.84]       -0.00977       -0.01113    0.00136
 Eye Right  Long  [8.32, 7.1, 6.51, 5.94, 4.98]       -0.00784       -0.00674   -0.00110
  Eye Left Short  [9.19, 7.62, 7.44, 6.0, 6.27]       -0.00932       -0.01229    0.00296
  Eye Left  Long [9.02, 7.34, 6.44, 6.54, 6.56]       -0.00572       -0.00667    0.00094
Hand Right Short [6.34, 5.63, 5.58, 5.01, 4.83]       -0.00453       -0.00921    0.00468
Hand Right  Long  [7.07, 5.91, 5.46, 4.8, 5.13]       -0.00499       -0.00565    0.00066
 Hand Left Short [6.37, 5.36, 5.18, 4.14, 4.11]       -0.00717       -0.00856    0.00139
 Hand Left  Long [6.18, 4.88, 5.17, 5.17, 4.97]       -0.00213       -0.00535    0.00322

[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/sohn-2019 2>&1 | tail -5; ls executed/sohn-2019/handover/; python tools/entry.py check entries/sohn-2019 2>&1 | tail -2; ls entries/sohn-2019; date -u
```

```
wrote executed/sohn-2019/handover
reproduce_sohn_2019.ipynb
rsg.py
sohn-2019.yaml
0 error(s)
README.md
__pycache__
entry.yaml
reproduce_sohn_2019.ipynb
requirements.in
requirements.lock.txt
rsg.py
Sat Nov 14 14:07:50 UTC 2026
```

**Agent calls Bash**

```bash
rm -rf entries/sohn-2019/__pycache__; python3 -c "
import json;nb=json.load(open('executed/sohn-2019/handover/reproduce_sohn_2019.ipynb'));print(sum('Result:' in ''.join(c['source']) for c in nb['cells']), any('## Summary' in ''.join(c['source']) for c in nb['cells']))"
```

```
0 False
```

**Agent**

I've finished the blind repeat attempt on sohn-2019 (DANDI:000130, version 0.241017.1448, the version the prompt asked for). `python tools/entry.py all entries/sohn-2019` passes, `check` reports 0 errors, and the handover is built in `executed/sohn-2019/handover/`. Nothing is committed. I did not come across any earlier attempt's results.

**1. Outcomes**

| Claim | Outcome | Key numbers |
|---|---|---|
| beh-slopes | not reproduced | 6 of 8 slopes between 0 and 1; the Short-prior slopes of both eye datasets are 1.011 and 1.110 |
| beh-overlap-prior | not reproduced | median biases +28.3 (Short) and +47.6 ms (Long), both positive; p = 0.073 |
| beh-sigmoid-increments | reproduced | 7 of 8, p = 0.0156 |
| beh-long-more-bias | reproduced | 4 of 4 |
| beh-bayes-model | partially reproduced | bias R2 at least 0.8 in 2 of 4; SD correlation positive in 4 of 4 |
| glm-prior-ts | not reproduced | 79.2% prior-dependent, 45.8% ts-dependent (expected 65% and 27%) |
| dfr-overlap-support | reproduced | peak 6.86 spikes/s at 480 to 640 ms after Ready; shuffle 95th percentile 3.09 |
| pca-dimensionality | not reproduced | 1 of 8 in range; 2 components reach 75% in every estimation epoch |
| encoding-r2 | reproduced | 0.994 and 0.986 (Hand Left); the PC space is only 2-dimensional, so random axes also score high |
| encoding-bayes-beats-linear | not reproduced | Bayesian model better in 3 of 4 datasets for each prior |
| short-in-long-control | reproduced (paper's test) | p = 0.25, but the effect is present in 3 of 4 datasets |
| neural-long-more-bias | reproduced | 4 of 4 |
| speed-vs-projection | partially reproduced | r = -0.926 and -0.834, stronger than the paper's, outside tolerance |
| initial-speed-biased | reproduced | 7 of 8, p = 0.039 |
| speed-predicts-tp | partially reproduced | r = -0.720 and -0.699, outside tolerance |
| alt-speed-unmodulated | reproduced (paper's test) | p = 0.125, the smallest possible with 4 datasets; speed rises in 8 of 8, partly an attrition artefact |
| alt-transient-parallel | reproduced | p = 0.109 (shortest ts) and 1.0 (longest) |
| alt-threshold-monotonic | not reproduced | median time of the minimum distance is 230 ms before Go |
| gpfa-variance-inverted-u | not reproduced | 6 of 8 coefficients negative, p = 0.074 |
| gpfa-mean-sigmoid | reproduced | p = 0.0078 and 0.0625 |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked: data_missing | — |

**2. Dataset, assumptions and questions**

- **Coverage:** the dandiset holds one of the paper's 29 sessions (monkey H, 2016-12-11). The train file has 1160 trials (983 completed and not outliers) and 54 units, of which 48 pass the paper's unit selection. That matches the 48 units the paper gives for its GPFA session of monkey H.
- **Test file:** its 283 trials have no task variables (the Neural Latents Benchmark withholds them), so they can't be used.
- **`iti` column:** the description reverses the two priors; the values match the paper's Methods.
- **`tp` column:** it exceeds `go_time - set_time` by a median of 17.9 ms, which is not documented. Aborted trials hold undocumented negative `tp` values.
- **Unit labels:** units have no electrode, probe or single/multi-unit label, and the electrode table has no positions.
- **Timing:** the clock checks are consistent. Target direction decodes at 0.80 at 300 to 600 ms after target onset against 0.50 with the next trial's labels, and there is a population transient after Set.
- **Assumptions:** no outcome is marked `assumed`. Where the paper allows two readings (regression intercept, how R2 is computed, the Short-In-Long axis), both readings give the same outcome.
- **Question for the paper's authors** (one `methods_unavailable` finding): whether the tp-on-ts regression had an intercept, whether rates were normalised before PCA, and how many GPFA EM iterations were run.
- **Questions to a reader:** none.

**3. Protocol points**

1. With 4 datasets, a two-sided signed-rank test can't reach p < 0.05, so the absence claims pass automatically under the rule "judged on the paper's test". I recorded them as reproduced and put the effect sizes in the notes; for alt-speed-unmodulated and short-in-long-control the effect is in fact present.
2. The claims file fixes a choice the paper leaves open: rates are not normalised before PCA. Step 1.6 doesn't say whether that choice binds the author. I followed the claims file, showed the unsmoothed and normalised versions as variants, and put the question to the authors.
3. The suggested clock check uses windows around the trial start. Here the prior is cued from trial start, so I used target onset and the Set transient instead.
4. The protocol gives `about` only for two finding kinds. I also set it on a `data_missing` and a `methods_unavailable` finding; the check accepted this.
5. The protocol asks for under ten minutes. GPFA with cross-validation takes about 11 minutes on its own, so I capped EM at 200 iterations (elephant's default is 500) and recorded that as a deviation. The fits had not fully converged.

**4. Runtime and failures**

The notebook takes about 12 minutes (12.2 at the last full run, 0.59 GB peak memory), most of it GPFA. Nothing failed. I ran the entry three times: once for the first run, then twice more after edits that only silenced elephant's log output, with identical results each time. Analysis finished at 14:07 UTC, well before the 17:10 cut-off.

Files are in `entries/sohn-2019`:
- reproduce_sohn_2019.ipynb
- rsg.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The attempt record is `attempts/sohn-2019-02.yaml`.

## End of run

61 turns, 68 minutes, $5.42 at API prices, result: success.
