# sohn-2019 · author · run 43715053400

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs entries attempts claims paper tools; wc -l docs/*.md README.md
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

```
Sun Nov 15 12:47:34 UTC 2026
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
[... 1010 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/sohn-2019.yaml; ls questions | grep sohn; cat papers/datasets/sohn-2019.yaml 2>/dev/null
```

```
# Claims for Sohn, Narain, Meirhaeghe & Jazayeri (2019) on dandiset 000130.
# Source: the accepted author manuscript in PubMed Central (PMC6805134), full text, read from its
# Results, figure legends and STAR Methods. The supplementary tables and figures were not
# available to this attempt. The paper's analysis code is "available on request"; the dandiset
# links only the Neural Latents Benchmark, whose code (nlb_tools) loads the data and scores
# models but holds none of the paper's analyses.
#
# When these criteria were written, the author had seen the data check only: the file list and
# metadata, the columns of the trial table and their consistency with the event times, the
# counts of trials per condition, the firing rate of each unit (48 of 54 units reach 1 spike/s),
# and the time one GPFA fit takes. No claim's analysis had been run.
#
# The dandiset holds one recording session (2016-12-11) of monkey H, one of the 17 sessions of H
# and 29 of both monkeys. Its 54 units were recorded together. A "dataset" here, as in the paper,
# is one effector and target direction (4 in this session; the paper has 8, from two animals).
#
# Method choices fixed here, where the Methods leave them open:
# - Behaviour uses completed trials not flagged by the file's `is_outlier` column (the paper's
#   mixture model), and the `tp` and `ts` columns.
# - Units: mean firing rate over the file of at least 1 spike/s and at least 5 trials in every
[... 439 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | head -80; sed -n 1,280p docs/design.md | head -150
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 210 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "^## |^### ",
 "path": "docs/archives.md",
 "output_mode": "content"
}
```

```
16:## DANDI
33:## CRCNS
60:## EBRAINS
85:## Dryad
134:## Figshare
177:## OpenNeuro
253:## SPARC
319:## Local and remote (`encore check`)
328:## Adding an archive
```

**Agent calls Bash**

```bash
cd  sed -n 1,33p docs/archives.md; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls schemas
```

```
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/fouke-2025-01.yaml | head -150; cat entries/fouke-2025/README.md
```

```
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z]" attempts/fouke-2025-01.yaml; awk '/^findings:/,/^verifications:/' attempts/fouke-2025-01.yaml | head -40; grep -n "blocked_by\|assumed" attempts/fouke-2025-01.yaml | head; python -c "import json;d=json.load(open('schemas/attempt.schema.json'));print(list(d['properties']));print(json.dumps(d['properties']['outcomes'],indent=0)[:3000])"
```

```
1:schema_version: 3
2:id: fouke-2025-01
3:datasets:
9:paper: doi:10.1016/j.cub.2025.04.027
10:date: 2026-10-14
11:entry: fouke-2025
12:provenance:
23:inputs:
35:outcomes:
244:findings:
314:verifications:
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
[... 202 more lines not kept]
```

**Agent**

Now the paper's Methods, then the dataset.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; grep -n -i "STAR\|METHOD DETAILS\|QUANTIFICATION\|^[A-Z][A-Za-z ]*$" paper/10.1016-j.neuron.2019.06.012.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1016-j.neuron.2019.06.012.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt; grep -n -i "method details\|Generalized linear\|Bayesian observer model\|Analysis of neural\|GPFA\|kernel\|speed" $TMPDIR/paper.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 225,
 "limit": 90
}
```

```
225	of both behavioral and spiking data was performed using custom MATLAB code (Mathworks, MA). METHOD DETAILS Two-prior time-interval reproduction task Task contingencies. Animals were trained on an 
226	interval-timing task that we refer to as the Ready-Set-Go (RSG) in which they had to measure a sample interval, t s , and produce a matching interval t p by initiating a saccade or by moving a 
227	joystick. Each experimental session consisted of 8 randomly interleaved conditions, 2 effectors (Hand and Eye), 2 movement targets (Left and Right), and 2 prior distributions of t s (Long and Short). 
228	Trial structure. Each trial began with the presentation of a circle (diameter: 0.5 deg) and a square (side: 0.5 deg) immediately below it. Animals had to fixate the circle and hold their gaze within 
229	3.5 deg of it. The square instructed animals to move the joystick to the central location. To aid the hand fixation, we briefly presented a cursor whose instantaneous position was proportional to the 
230	joystick’s angle and removed it after successful hand fixation. Upon successful fixation and after a random delay (500 ms plus a random sample from an exponential distribution with mean of 250 ms), a 
231	white movement target was presented 10 deg to the left or right of the circle (diameter: 0.5 deg). After another random delay (250 ms plus a random sample from an exponential distribution with mean 
232	of 250 ms), the Ready and Set stimuli were flashed sequentially around the fixation cues (outer diameter: 2.2 deg; thickness: 0.1 deg; duration: 100 ms). The animal had to measure the sample 
233	interval, t s , demarcated by Ready and Set, and produce a matching interval, t p , after Set by making a saccade or by moving the joystick toward the movement target presented earlier (Go). Across 
234	trials, t s was sampled from one of two discrete uniform prior distributions, each with 5 equidistant samples, a “Short” distribution between 480 and 800 ms (µ Short = 640 ms, 
[... 80 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 40,
 "limit": 112
}
```

```
40	Monkeys received reward if the produced interval, t p , between Set and Go was sufficiently close to t s ( Figure 1B ). We manipulated the animals’ prior expectations by sampling t s from one of two 
41	uniform prior distributions, a ‘Short’ prior ranging between 480 and 800 ms, and a’Long’ prior ranging between 800 and 1200 ms Figure(1C) . The task enabled us to also manipulate sensory uncertainty 
42	since measurements of time intervals become more variable for longer intervals, a property known as ‘scalar variability’ ( Malapani and Fairhurst, 2002 ). Since the two prior distributions overlapped 
43	at t s = 800 ms, the task further offered the opportunity to characterize how neural representations are independently modulated by prior beliefs. The prior condition and the desired effector were 
44	switched across short blocks of trials (block length: 4.0 ± 4.4 trials; uniform hazard) and the trial type was explicitly cued throughout each trial ( Figure 1D ). The rationale for including two 
45	response modalities and two directions of response was to ensure that the neural correlates of Bayesian integration identified would generalize across multiple experimental conditions. To verify that 
46	animals learned to perform the task, we used a regression analysis to assess the dependence of t p on t s . The regression slopes were positive, indicating that animals were able to estimate t s , 
47	and were less than unity, indicating that responses were biased toward to the mean of the prior ( Figure 1E and S1 , Table S1 ). The effect of the prior was most conspicuous at the overlapping t s 
48	for which biases were in opposite directions for the two prior conditions (rank-sum test, p<10 −43 in animal H, p<10 −75 in G; Figure 1E , Table S2 ). This effect was present immediately after block 
49	transitions ( Figure S2 ), indicating that animals rapidly switched between priors. These results indicate that animals learned the task contingencies and relied on their prior 
[... 102 more lines not kept]
```

**Agent**

Now the figure legends.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 460,
 "limit": 60
}
```

```
460	Hand) × 2 target directions (Left and Right). (E) Behavior. Top: A representative session for monkey H showing t p pooled across effectors and target directions (small dots: individual trials; large 
461	open circles: average t p per t s ; solid lines: Bayesian model; diagonal: unity line). The horizontal location of dots was jittered to facilitate visualization. Right: Histograms of t p for the 
462	overlapping t s (horizontal dashed line) for the two prior conditions (orange: Short; blue:Long; triangles: averages). Top-left inset: Average error (i.e., bias) for each t s (circles: data; solid 
463	lines: Bayesian model). Bottom-right inset: histogram of regression slopes relating t p to t s across sessions (red: Short; blue: Long; triangles: averages). Bottom: The same as top for Monkey G. 
464	Figure 2. Bayesian model and behavior. (A) Bayesian observer model. The measurement ( t m ) is the sample interval ( t s ) plus white noise with standard deviation proportional to t s . The Bayesian 
465	estimator is a sigmoidal function that maps t m to an optimal estimate ( t e ) (red: Short; blue: Long). t e is biased toward the mean of the prior (arrows). The production interval ( t p ) is t e 
466	plus scalar noise during production epoch. (B) The prior (top), the likelihood function (middle), the resulting posterior (bottom), and the posterior mean (circles) that represent the estimate. (C) 
467	Comparison of t p bias relative to t s between model and behavior across animals and conditions. (D) Same as C for variability. Individual trials were pooled across sessions for each condition to 
468	compute the variance. (E) The sigmoidal Bayesian estimator predicts that the average t p difference across neighboring t s (∆ t p ) should be larger around the mean of the prior distribution (∆ t p 
469	(middle)), compared to its extrema, ∆ t p (extreme) (average of ∆ t p (max) and ∆ t p (min)). (F) ∆ t p (extreme) as a function ∆ t p (middle) for each session and condition (p
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; which python; python -c "import pynwb, remfile, h5py, scipy, sklearn, statsmodels; print(pynwb.__version__)"; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.241017.1448/assets/?page_size=100" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -30; grep -n "python_version\|PYTHON\|3\.1[0-9]" tools/entry.py | head -20
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -p 3.13 dev >/dev/null 2>&1; source dev/bin/activate; uv pip install pynwb remfile h5py dandi numpy scipy pandas matplotlib statsmodels scikit-learn ipykernel nbformat nbclient 2>&1 | tail -2; date -u
```

```
+ zarr==3.4.2
 + zarr-checksum==0.4.7
Sun Nov 15 12:48:08 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  source $TMPDIR/dev/bin/activate; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.241017.1448/" | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d[k] for k in ['name','description','relatedResource','assetsSummary','version','doi'] if k in d},indent=1))"; cat > $TMPDIR/survey.py <<'EOF'
import remfile,h5py,pynwb,requests
v="0.241017.1448"
for aid,name in [("c90cbccc-31a5-4815-88e6-822d8c5ca68c","train"),("a2c3ced1-2869-4483-aa19-8815c2d18c91","test")]:
    url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
    r=requests.head(url,allow_redirects=True); s3=r.url
    f=remfile.File(s3); h=h5py.File(f,'r')
    io=pynwb.NWBHDF5IO(file=h,load_namespaces=True); nwb=io.read()
    print("=====",name, nwb.identifier, nwb.session_start_time, nwb.session_description)
    print(nwb.subject)
    print("acq",list(nwb.acquisition), "proc", {k:list(v.data_interfaces) for k,v in nwb.processing.items()})
    print("intervals",list(nwb.intervals))
    tr=nwb.trials.to_dataframe()
    print(tr.shape); print(tr.dtypes); print(tr.head(3).T); print(tr.describe(include='all').T)
    u=nwb.units.to_dataframe()
    print(u.shape, u.columns.tolist()); print(u.head(3))
    print(nwb.electrodes.to_dataframe().head() if nwb.electrodes is not None else None)
    print(nwb.experiment_description, nwb.lab, nwb.institution, nwb.related_publications)
    for c in nwb.trials.columns: print(c.name, '|', c.description)
    for c in nwb.units.columns: print('unit',c.name, '|', c.description)
EOF
python $TMPDIR/survey.py 2>&1 | head -300
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  source $TMPDIR/dev/bin/activate; cat > $TMPDIR/survey2.py <<'EOF'
import remfile,h5py,pynwb,requests,numpy as np,pandas as pd
url="https://api.dandiarchive.org/api/assets/c90cbccc-31a5-4815-88e6-822d8c5ca68c/download/"
s3=requests.head(url,allow_redirects=True).url
h=h5py.File(remfile.File(s3),'r'); nwb=pynwb.NWBHDF5IO(file=h,load_namespaces=True).read()
tr=nwb.trials.to_dataframe(); u=nwb.units.to_dataframe()
print(tr.split.value_counts())
print(pd.crosstab(tr.split, tr.set_time.notna()))
print(pd.crosstab(tr.split, tr.go_time.notna()))
print(pd.crosstab(tr.split, tr.is_outlier))
print(nwb.electrodes.to_dataframe().columns.tolist(), len(nwb.electrodes)); print(nwb.electrodes.to_dataframe().iloc[0])
print(nwb.electrode_groups)
print("heldout", u.heldout.sum())
oi=u.obs_intervals.iloc[0]; print(len(oi), oi[:5], oi[-3:])
print("all units same obs:", all(np.array_equal(np.asarray(x),np.asarray(oi)) for x in u.obs_intervals))
oi=np.asarray(oi); gaps=oi[1:,0]-oi[:-1,1]; print("gaps", np.round(np.sort(gaps)[-20:],3), "covered", (oi[:,1]-oi[:,0]).sum())
for c in ['ready_time','set_time','go_time']:
    t=tr[c].dropna().values
    inside=np.array([((oi[:,0]<=x)&(oi[:,1]>=x)).any() for x in t]); print(c, inside.mean(), (~inside).sum())
st=u.spike_times; print("sorted", all(np.all(np.diff(s)>=0) for s in st), "n spikes", [len(s) for s in st][:10])
print("fr", np.round(np.array([len(s) for s in st])/ (oi[:,1]-oi[:,0]).sum(),2))
print(u.index.tolist())
# tp vs go-set
m=tr.go_time.notna()&tr.set_time.notna()
d=(tr.go_time-tr.set_time)[m]*1000-tr.tp[m]; print("tp-(go-set) ms", d.describe())
d=(tr.set_time-tr.ready_time)*1000-tr.ts; print("ts-(set-ready)", d.describe())
print(tr[~m].tp.describe())
print(pd.crosstab([tr.is_short,tr.ts],[tr.is_eye,tr.theta]))
c=tr[m & ~tr.is_outlier]; print(len(c)); print(pd.crosstab([c.is_short,c.ts],[c.is_eye,c.theta]))
print(tr.bad_time.notna().groupby(tr.go_time.notna()).sum())
print(tr[m].reward_time.isna().sum())
EOF
python $TMPDIR/survey2.py 2>&1
```

```
split
train    748
val      258
none     154
Name: count, dtype: int64
set_time  False  True 
split                 
none        121     33
train         0    748
val           0    258
go_time  False  True 
split                
none       131     23
train        0    748
val          0    258
is_outlier  False  True 
split                   
none           17    137
train         720     28
val           246     12
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd  source $TMPDIR/dev/bin/activate; cat > $TMPDIR/survey3.py <<'EOF'
import remfile,h5py,pynwb,requests,numpy as np,pandas as pd
url="https://api.dandiarchive.org/api/assets/c90cbccc-31a5-4815-88e6-822d8c5ca68c/download/"
s3=requests.head(url,allow_redirects=True).url
h=h5py.File(remfile.File(s3),'r'); nwb=pynwb.NWBHDF5IO(file=h,load_namespaces=True).read()
tr=nwb.trials.to_dataframe()
c=tr[tr.go_time.notna()]
d=((c.set_time-c.ready_time)*1000-c.ts).round(1); print(d.value_counts().head(15))
e=((c.go_time-c.set_time)*1000-c.tp).round(1); print(e.describe()); print(e.value_counts().head(10))
print(c[(e.abs()>60)][['split','is_outlier','ts','tp','set_time','go_time','target_acq_time','reward_time','bad_time']])
print(c[c.split=='none'][['is_outlier','ts','tp','reward_time','bad_time','start_time']])
print(tr.iloc[-5:][['split','start_time','set_time','go_time']])
# gaps between trials, test trials location
st=tr.start_time.values; print(np.sort(np.diff(st))[-10:])
EOF
python $TMPDIR/survey3.py 2>&1
```

```
-0.0     521
 3.5      64
-3.5      62
 6.5      59
-6.5      55
-16.5     50
 7.0      42
-17.0     27
-3.0      27
-7.0      21
 3.0      19
 0.5      14
-10.0     14
-13.5      9
-20.0      7
Name: count, dtype: int64
count    1029.000000
mean      -10.735083
std       188.659620
min      -200.600000
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; source dev/bin/activate; uv pip install elephant 2>&1 | tail -3; python -c "import elephant, neo, quantities; print(elephant.__version__)"; date -u
```

```
+ elephant==1.2.1
 + neo==0.14.6
 + quantities==0.16.4
1.2.1
Sun Nov 15 12:50:15 UTC 2026
Shell cwd was reset to
```

**Agent**

Data surveyed: one session (monkey H, 2016-12-11), 54 units, 1160 trials in the train file; the test file holds 283 unlabelled NLB test trials. Writing the helper module now.

**Agent calls Write**

```json
{
 "file_path": "entries/sohn-2019/rsg.py",
 "content": "\"\"\"Loading and measures for DANDI:000130 (Sohn, Narain, Meirhaeghe & Jazayeri 2019, Neuron).\n\nThe dandiset holds one session of monkey H (Haydn, 2016-12-11) of the Ready-Set-Go task with\ntwo priors of the sample interval ts, split for the Neural Latents Benchmark into a train file\n(trials with behaviour, 54 units) and a test file (unlabelled 1.7 s segments, 40 units).\n\nWhere each parameter comes from:\n\n- Trials: completed (Set and Go present, no failure time, tp > 0) and not flagged by\n  `is_outlier`, the file's flag from the paper's mixture model. Claims file, header.\n- Units: mean rate over the file of at least 1 spike/s and at least 5 trials in every one of the\n  40 conditions. Claims file, header; Methods, \"Analysis of single- and multi-unit activity\".\n- Rates: 20 ms bins averaged over trials, in spikes/s, then smoothed with a Gaussian of SD 40 ms.\n  Claims file, header (Methods, \"Principal component analysis\": \"bin size: 20 ms, Gaussian\n  smoothing kernel width: 40 ms\"). The kernel is truncated at the ends of a window and\n  renormalised there: a standard choice for edges, which the paper does not describe.\n- Attrition: in the estimation epoch, the bin ending at t averages the trials whose nominal ts\n  is at least t. Claims file, header; Methods (\"firing rate at time t was computed from spikes in\n  all trials in which Set occurred after t\"). The nominal ts is used, as Set - Ready differs from\n  it by at most 23.5 ms in the file (a standard choice; it keeps the five attrition groups).\n- PCA: per dataset (effector and direction) and epoch, on the trajectories of both priors\n  concatenated, keeping the fewest components that reach 75% of the variance. Claims file,\n  header; Methods, \"Principal component analysis\".\n- Encoding axis: mean of X(ts_max - d) - X(ts_min + d), d = 0, 20, ... while\n  ts_min + d < ts_max - d, normalised. Claims file, header; Methods, \"Analysis of neural\n  projection\".\n- Bayesian observer: continuous uniform prior, measurement SD wm*ts, posterior-mean estimate,\n  production SD wp*te, offset b per prior; fit by maximum likelihood. Claims file, header;\n  Methods, \"Analysis of behavior with a Bayesian model\". Integration grids (241 points for tm,\n  201 for the prior) are a standard numerical choice.\n- GLM: Poisson, counts in the 80 ms before 480 ... 800 ms after Ready, BIC comparison. Claims\n  file, glm-prior-ts; Methods, \"Generalized linear model\".\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\n\nDANDISET_ID = \"000130\"\nVERSION = \"0.241017.1448\"\nTRAIN_PATH = \"sub-Haydn/sub-Haydn_desc-train_ecephys.nwb\"\nTEST_PATH = \"sub-Haydn/sub-Haydn_desc-test_ecephys.nwb\"\n\nBIN_MS = 20\nSMOOTH_SD_MS = 40\nDATASETS = [\"Eye Left\", \"Eye Right\", \"Hand Left\", \"Hand Right\"]\nPRIORS = [\"Short\", \"Long\"]\nTS = {\"Short\": [480, 560, 640, 720, 800], \"Long\": [800, 900, 1000, 1100, 1200]}\n\n\n# ---------------------------------------------------------------- loading\n\ndef asset_url(path):\n    \"\"\"S3 URL of an asset of the pinned version.\"\"\"\n    from dandi.dandiapi import DandiAPIClient\n\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, VERSION)\n        return ds.get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)\n\n\ndef open_nwb(path):\n    \"\"\"Stream an NWB file of the pinned version; returns (nwbfile, io).\"\"\"\n    import h5py\n    import pynwb\n    import remfile\n\n    f = remfile.File(asset_url(path))\n    io = pynwb.NWBHDF5IO(file=h5py.File(f, \"r\"), load_namespaces=True)\n    return io.read(), io\n\n\ndef load_session():\n    \"\"\"Trials table and spike times of the train file.\n\n    Returns a dict with `trials` (DataFrame with added columns), `spikes` (list of arrays, s),\n    `unit_ids`, `heldout`, `obs_intervals` and `duration` (s observed).\"\"\"\n    nwb, io = open_nwb(TRAIN_PATH)\n    tr = nwb.trials.to_dataframe()\n    u = nwb.units\n    spikes = [np.asarray(u[\"spike_times\"][i]) for i in range(len(u))]\n    obs = [np.asarray(u[\"obs_intervals\"][i]) for i in range(len(u))]\n    unit_ids = np.asarray(u.id[:])\n    heldout = np.asarray(u[\"heldout\"][:])\n    tr[\"prior\"] = np.where(tr.is_short, \"Short\", \"Long\")\n    tr[\"effector\"] = np.where(tr.is_eye, \"Eye\", \"Hand\")\n    tr[\"direction\"] = np.where(tr.theta == 180, \"Left\", \"Right\")\n    tr[\"dataset\"] = tr.effector + \" \" + tr.direction\n    tr[\"completed\"] = (tr.set_time.notna() & tr.go_time.notna() & tr.bad_time.isna()\n                       & (tr.tp > 0))\n    tr[\"valid\"] = tr.completed & ~tr.is_outlier\n    tr[\"ts\"] = tr.ts.round().astype(int)\n    meta = dict(session_start=str(nwb.session_start_time), subject=nwb.subject.subject_id,\n                species=nwb.subject.species, description=nwb.session_description)\n    io.close()\n    duration = np.sum(obs[0][:, 1] - obs[0][:, 0])\n    return dict(trials=tr, spikes=spikes, unit_ids=unit_ids, heldout=heldout,\n                obs_intervals=obs, duration=duration, meta=meta)\n\n\ndef select_units(sess, min_rate=1.0, min_trials=5):\n    \"\"\"Units with mean rate >= 1 spike/s over the file and >= 5 valid trials in each of the 40\n    conditions (all units are observed over the whole session, so the trial rule applies to the\n    session as a whole). Returns a boolean mask and the per-unit rates.\"\"\"\n    rates = np.array([len(s) for s in sess[\"spikes\"]]) / sess[\"duration\"]\n    v = sess[\"trials\"][sess[\"trials\"].valid]\n    counts = v.groupby([\"prior\", \"ts\", \"effector\", \"direction\"]).size()\n    enough = (len(counts) == 40) and (counts.min() >= min_trials)\n    return (rates >= min_rate) & enough, rates\n\n\n# ---------------------------------------------------------------- binning and rates\n\ndef bin_counts(spikes, align, edges_ms):\n    \"\"\"Spike counts, array (trials, units, bins), for windows align + edges (align in s).\"\"\"\n    edges = np.asarray(align)[:, None] + np.asarray(edges_ms)[None, :] / 1000.0\n    out = np.empty((edges.shape[0], len(spikes), edges.shape[1] - 1))\n    for j, s in enumerate(spikes):\n        idx = np.searchsorted(s, edges)\n        out[:, j, :] = np.diff(idx, axis=1)\n    return out\n\n\ndef smooth(x, sd_ms=SMOOTH_SD_MS, bin_ms=BIN_MS, axis=0):\n    \"\"\"Gaussian smoothing along `axis`, kernel truncated at the edges and renormalised.\"\"\"\n    x = np.moveaxis(np.asarray(x, float), axis, 0)\n    n = x.shape[0]\n    sd = sd_ms / bin_ms\n    t = np.arange(n)\n    k = np.exp(-0.5 * ((t[:, None] - t[None, :]) / sd) ** 2)\n    k /= k.sum(axis=1, keepdims=True)\n    y = np.tensordot(k, x, axes=(1, 0))\n    return np.moveaxis(y, 0, axis)\n\n\ndef estimation_rates(spikes, trials, ts_max, attrition=True):\n    \"\"\"Trial-averaged rates (bins x units, spikes/s) aligned to Ready, bins ending at\n    20, 40, ..., ts_max ms; with attrition the bin ending at t uses trials with ts >= t.\n    Returns (rates, n_trials_per_bin, bin_end_times_ms).\"\"\"\n    edges = np.arange(0, ts_max + BIN_MS, BIN_MS)\n    c = bin_counts(spikes, trials.ready_time.values, edges)\n    ends = edges[1:]\n    if attrition:\n        use = trials.ts.values[:, None] >= ends[None, :]\n    else:\n        use = np.ones((len(trials), len(ends)), bool)\n    n = use.sum(0)\n    tot = np.einsum(\"tub,tb->bu\", c, use.astype(float))\n    r = tot / np.maximum(n, 1)[:, None] / (BIN_MS / 1000.0)\n    return smooth(r), n, ends\n\n\ndef aligned_rates(spikes, align_s, start_ms, stop_ms):\n    \"\"\"Trial-averaged smoothed rates (bins x units) for align + [start, stop) in 20 ms bins.\"\"\"\n    edges = np.arange(start_ms, stop_ms + 1e-9, BIN_MS)\n    c = bin_counts(spikes, align_s, edges)\n    r = c.mean(0).T / (BIN_MS / 1000.0)\n    return smooth(r), edges[1:]\n\n\ndef production_rates(spikes, trials):\n    \"\"\"Per ts: rates from Set to the shortest tp of that ts (whole 20 ms bins), as a dict\n    ts -> (rates, bin_end_times_ms, n_trials, shortest_tp).\"\"\"\n    out = {}\n    for ts, g in trials.groupby(\"ts\"):\n        tmin = g.tp.min()\n        stop = int(np.floor(tmin / BIN_MS) * BIN_MS)\n        r, ends = aligned_rates(spikes, g.set_time.values, 0, stop)\n        out[ts] = (r, ends, len(g), tmin)\n    return out\n\n\n# ---------------------------------------------------------------- PCA and geometry\n\ndef pca(blocks, frac=0.75):\n    \"\"\"PCA on concatenated (time x units) blocks. Returns dict with mean, components (k x units),\n    explained ratio (all), and k, the fewest components reaching `frac`.\"\"\"\n    X = np.vstack(blocks)\n    mu = X.mean(0)\n    U, S, Vt = np.linalg.svd(X - mu, full_matrices=False)\n    ev = S ** 2 / np.sum(S ** 2)\n    k = int(np.searchsorted(np.cumsum(ev), frac) + 1)\n    return dict(mean=mu, components=Vt, explained=ev, k=k)\n\n\ndef project(p, R, k=None):\n    k = p[\"k\"] if k is None else k\n    return (R - p[\"mean\"]) @ p[\"components\"][:k].T\n\n\ndef encoding_axis(X, times, t_min, t_max):\n    \"\"\"Mean of X(t_max - d) - X(t_min + d) for d = 0, 20, ... while t_min + d < t_max - d,\n    normalised. X rows are states at `times` (ms).\"\"\"\n    times = list(times)\n    vecs = []\n    d = 0\n    while t_min + d < t_max - d:\n        vecs.append(X[times.index(t_max - d)] - X[times.index(t_min + d)])\n        d += BIN_MS\n    u = np.mean(vecs, 0)\n    return u / np.linalg.norm(u), len(vecs)\n\n\ndef mean_step(X):\n    \"\"\"Mean Euclidean distance between successive states (rows).\"\"\"\n    return float(np.mean(np.linalg.norm(np.diff(X, axis=0), axis=1)))\n\n\n# ---------------------------------------------------------------- statistics\n\ndef wls(x, y, w):\n    \"\"\"Weighted least squares y = a + b x. Returns dict a, b, se_b, r2 (weighted), rmse\n    (unweighted residuals), wrmse (weighted), resid.\"\"\"\n    x, y, w = (np.asarray(v, float) for v in (x, y, w))\n    W = w / w.sum()\n    xm, ym = np.sum(W * x), np.sum(W * y)\n    b = np.sum(W * (x - xm) * (y - ym)) / np.sum(W * (x - xm) ** 2)\n    a = ym - b * xm\n    res = y - (a + b * x)\n    r2 = 1 - np.sum(W * res ** 2) / np.sum(W * (y - ym) ** 2)\n    return dict(a=a, b=b, r2=r2, rmse=float(np.sqrt(np.mean(res ** 2))),\n                wrmse=float(np.sqrt(np.sum(W * res ** 2))), resid=res)\n\n\ndef increments(means):\n    \"\"\"Extreme (mean of first and last) and middle (mean of second and third) increments of a\n    5-point profile.\"\"\"\n    d = np.diff(np.asarray(means, float))\n    return (d[0] + d[3]) / 2, (d[1] + d[2]) / 2\n\n\n# ---------------------------------------------------------------- Bayesian observer\n\ndef _grids(ts, wm, lo, hi, n_tm=241, n_prior=201):\n    \"\"\"tm grid and Gaussian weights for one ts; te(tm) for a uniform prior on [lo, hi].\"\"\"\n    sd = wm * ts\n    tm = np.linspace(max(ts - 5 * sd, 1.0), ts + 5 * sd, n_tm)\n    w = np.exp(-0.5 * ((tm - ts) / sd) ** 2)\n    w /= w.sum()\n    sp = np.linspace(lo, hi, n_prior)\n    lik = np.exp(-0.5 * ((tm[:, None] - sp[None, :]) / (wm * sp[None, :])) ** 2) / (wm * sp[None, :])\n    te = (lik * sp[None, :]).sum(1) / lik.sum(1)\n    return tm, w, te\n\n\ndef bls_predict(ts, wm, wp, b, lo, hi):\n    \"\"\"Mean estimate te(ts), predicted mean tp and SD of tp for a scalar ts.\"\"\"\n    _, w, te = _grids(ts, wm, lo, hi)\n    m_te = np.sum(w * te)\n    m = m_te + b\n    v = np.sum(w * ((wp * te) ** 2 + (te + b) ** 2)) - m ** 2\n    return m_te, m, np.sqrt(v)\n\n\ndef bls_nll(params, data):\n    \"\"\"Negative log-likelihood; params = (log wm, log wp, bShort, bLong); data = list of\n    (prior, ts, tp array).\"\"\"\n    wm, wp = np.exp(params[0]), np.exp(params[1])\n    bs = {\"Short\": params[2], \"Long\": params[3]}\n    nll = 0.0\n    for prior, ts, tp in data:\n        lo, hi = TS[prior][0], TS[prior][-1]\n        _, w, te = _grids(ts, wm, lo, hi)\n        mu = te + bs[prior]\n        sd = wp * te\n        p = (w[None, :] * np.exp(-0.5 * ((tp[:, None] - mu[None, :]) / sd[None, :]) ** 2)\n             / (np.sqrt(2 * np.pi) * sd[None, :])).sum(1)\n        nll -= np.sum(np.log(np.maximum(p, 1e-300)))\n    return nll\n\n\ndef fit_bls(trials):\n    \"\"\"Maximum-likelihood fit of (wm, wp, bShort, bLong) to the valid trials of one dataset.\"\"\"\n    from scipy.optimize import minimize\n\n    data = [(p, ts, g.tp.values) for (p, ts), g in trials.groupby([\"prior\", \"ts\"])]\n    best = None\n    for x0 in ([np.log(0.1), np.log(0.06), 0, 0], [np.log(0.2), np.log(0.1), 20, 20]):\n        r = minimize(bls_nll, x0, args=(data,), method=\"Nelder-Mead\",\n                     options=dict(maxiter=4000, xatol=1e-4, fatol=1e-4))\n        if best is None or r.fun < best.fun:\n            best = r\n    wm, wp = np.exp(best.x[:2])\n    return dict(wm=wm, wp=wp, bShort=best.x[2], bLong=best.x[3], nll=best.fun,\n                success=bool(best.success))\n\n\n# ---------------------------------------------------------------- GLM\n\ndef glm_bic(y, X):\n    \"\"\"BIC = k log n - 2 logL of a Poisson GLM (statsmodels); None if the fit fails.\"\"\"\n    import statsmodels.api as sm\n\n    try:\n        r = sm.GLM(y, X, family=sm.families.Poisson()).fit()\n    except Exception:\n        return None\n    if not np.isfinite(r.llf):\n        return None\n    return X.shape[1] * np.log(len(y)) - 2 * r.llf\n"
}
```

```
File created successfully at: entries/sohn-2019/rsg.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; cat > $TMPDIR/dev1.py <<'EOF'
import sys, time, pickle, os
sys.path.insert(0,'.')
import rsg, numpy as np, pandas as pd
p=os.environ['TMPDIR']+'/sess.pkl'
if os.path.exists(p): sess=pickle.load(open(p,'rb'))
else:
    t=time.time(); sess=rsg.load_session(); print('load',time.time()-t); pickle.dump(sess,open(p,'wb'))
tr=sess['trials']; v=tr[tr.valid]
print(tr.completed.sum(), tr.valid.sum(), (tr.completed & tr.bad_time.notna()).sum())
m,rates=rsg.select_units(sess); print(m.sum())
t=time.time()
for ds,g in v.groupby('dataset'):
    f=rsg.fit_bls(g); print(ds, {k:round(float(x),4) for k,x in f.items()}, round(time.time()-t,1))
EOF
python $TMPDIR/dev1.py
```

```
load 4.812375068664551
1025 982 0
48
Eye Left {'wm': 0.0252, 'wp': 0.1027, 'bShort': 40.8376, 'bLong': 1.6911, 'nll': 1526.2056, 'success': 1.0} 1.5
Eye Right {'wm': 0.0138, 'wp': 0.1063, 'bShort': 6.1169, 'bLong': 24.2855, 'nll': 1610.5756, 'success': 1.0} 3.0
Hand Left {'wm': 0.1166, 'wp': 0.09, 'bShort': 7.7494, 'bLong': -81.479, 'nll': 1289.0002, 'success': 1.0} 4.3
Hand Right {'wm': 0.0736, 'wp': 0.1044, 'bShort': 36.9319, 'bLong': 50.3587, 'nll': 1334.1907, 'success': 1.0} 5.6
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; cat > $TMPDIR/dev2.py <<'EOF'
import sys, pickle, os
sys.path.insert(0,'.')
import rsg, numpy as np, pandas as pd
from scipy.optimize import minimize
sess=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
tr=sess['trials']; v=tr[tr.valid]
print(v.groupby(['dataset','prior','ts']).tp.agg(['mean','std','count']).round(1).unstack('dataset'))
for ds,g in v.groupby('dataset'):
    data=[(p,ts,gg.tp.values) for (p,ts),gg in g.groupby(['prior','ts'])]
    res=[]
    for wm0 in [0.03,0.08,0.15,0.25]:
        for wp0 in [0.03,0.06,0.1]:
            r=minimize(rsg.bls_nll,[np.log(wm0),np.log(wp0),0,0],args=(data,),method='Nelder-Mead',options=dict(maxiter=4000,xatol=1e-4,fatol=1e-4))
            res.append((round(r.fun,2),np.round(np.exp(r.x[:2]),3),np.round(r.x[2:],1)))
    res.sort(key=lambda x:x[0]); print(ds,res[:4])
EOF
python $TMPDIR/dev2.py
```

```
mean                      ...                               
dataset    Eye Left Eye Right Hand Left  ... Eye Right Hand Left Hand Right
prior ts                                 ...                               
Long  800     821.3     844.3     808.3  ...        38        14         19
      900     916.0     922.3     872.6  ...        34        24         17
      1000   1006.7    1002.4     905.8  ...        23        16         30
      1100   1094.7    1156.2     986.2  ...        25        16         21
      1200   1156.0    1176.5    1003.6  ...        27        18         25
Short 480     539.5     496.9     548.7  ...        24        33         21
      560     580.0     543.7     594.5  ...        27        21         35
      640     666.9     630.6     661.5  ...        31        25         14
      720     772.1     752.0     685.1  ...        22        31         21
      800     864.0     835.9     751.5  ...        24        24         22

[10 rows x 12 columns]
Eye Left [(np.float64(1526.21), array([0.025, 0.103]), array([40.8,  1.7])), (np.float64(1526.21), array([0.025, 0.103]), array([40.8,  1.7])), (np.float64(1526.21), array([0.025, 0.103]), array([40.8,  1.7])), (np.float64(1526.21), array([0.025, 0.103]), array([40.8,  1.7]))]
Eye Right [(np.float64(1610.58), array([0.014, 0.106]), array([ 6.1, 24.3])), (np.float64(1610.58), array([0.014, 0.106]), array([ 6.1, 24.3])), (np.float64(1610.58), array([0.014, 0.106]), array([ 6.1, 24.3])), (np.float64(1614.97), array([0.021, 0.107]), array([0., 0.]))]
Hand Left [(np.float64(1313.86), array([0.11 , 0.106]), array([ 0., -0.])), (np.float64(1313.86), array([0.11 , 0.106]), array([0., 0.])), (np.float64(1313.86), array([0.11 , 0.106]), array([ 0., -0.])), (np.float64(1313.86), array([0.11 , 0.106]), array([0., 0.]))]
Hand Right [(np.float64(1334.19), array([0.074, 0.104]), array([36.9, 50.4])), (np.float64(1334.19), array([0.074, 0.104]), array([36.9, 50.4])), (np.float64(1357.33), array([0.089, 0
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; python - <<'EOF'
import re
s=open('rsg.py').read()
s=s.replace('''    """Negative log-likelihood; params = (log wm, log wp, bShort, bLong); data = list of
    (prior, ts, tp array)."""
    wm, wp = np.exp(params[0]), np.exp(params[1])
    bs = {"Short": params[2], "Long": params[3]}''','''    """Negative log-likelihood; params = (log wm, log wp, bShort/100, bLong/100) (offsets in
    units of 100 ms, so that the simplex moves them); data = list of (prior, ts, tp array)."""
    wm, wp = np.exp(params[0]), np.exp(params[1])
    bs = {"Short": 100 * params[2], "Long": 100 * params[3]}''')
s=s.replace('''    """Maximum-likelihood fit of (wm, wp, bShort, bLong) to the valid trials of one dataset."""
    from scipy.optimize import minimize

    data = [(p, ts, g.tp.values) for (p, ts), g in trials.groupby(["prior", "ts"])]
    best = None
    for x0 in ([np.log(0.1), np.log(0.06), 0, 0], [np.log(0.2), np.log(0.1), 20, 20]):
        r = minimize(bls_nll, x0, args=(data,), method="Nelder-Mead",
                     options=dict(maxiter=4000, xatol=1e-4, fatol=1e-4))
        if best is None or r.fun < best.fun:
            best = r
    wm, wp = np.exp(best.x[:2])
    return dict(wm=wm, wp=wp, bShort=best.x[2], bLong=best.x[3], nll=best.fun,
                success=bool(best.success))''','''    """Maximum-likelihood fit of (wm, wp, bShort, bLong) to the valid trials of one dataset,
    by Nelder-Mead from 8 starting points (wm 0.05 or 0.15, wp 0.05 or 0.1, offsets 10 or
    -10 ms); the best of the 8 is kept. The starting points are a standard numerical choice."""
    from scipy.optimize import minimize

    data = [(p, ts, g.tp.values) for (p, ts), g in trials.groupby(["prior", "ts"])]
    best = None
    for wm0 in (0.05, 0.15):
        for wp0 in (0.05, 0.1):
            for b0 in (0.1, -0.1):
                r = minimize(bls_nll, [np.log(wm0), np.log(wp0), b0, b0], args=(data,),
                             method="Nelder-Mead",
                             options=dict(maxiter=4000, xatol=1e-5, fatol=1e-4))
                if best is None or r.fun < best.fun:
                    best = r
    wm, wp = np.exp(best.x[:2])
    return dict(wm=wm, wp=wp, bShort=100 * best.x[2], bLong=100 * best.x[3], nll=best.fun,
                success=bool(best.success))''')
open('rsg.py','w').write(s)
EOF
python $TMPDIR/dev1.py
```

```
1025 982 0
48
Eye Left {'wm': 0.0252, 'wp': 0.1027, 'bShort': 40.8376, 'bLong': 1.6911, 'nll': 1526.2056, 'success': 1.0} 9.7
Eye Right {'wm': 0.0138, 'wp': 0.1063, 'bShort': 6.1167, 'bLong': 24.2854, 'nll': 1610.5756, 'success': 1.0} 18.9
Hand Left {'wm': 0.1166, 'wp': 0.09, 'bShort': 7.7494, 'bLong': -81.4791, 'nll': 1289.0002, 'success': 1.0} 27.0
Hand Right {'wm': 0.0736, 'wp': 0.1044, 'bShort': 36.9319, 'bLong': 50.3588, 'nll': 1334.1907, 'success': 1.0} 35.7
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; cat > $TMPDIR/dev3.py <<'EOF'
import sys, pickle, os, time, resource
sys.path.insert(0,'.')
import rsg, numpy as np, pandas as pd, neo, quantities as pq
from elephant.gpfa import GPFA
sess=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
tr=sess['trials']; v=tr[tr.valid]; m,_=rsg.select_units(sess)
sp=[s for s,k in zip(sess['spikes'],m) if k]
g=v[v.dataset=='Hand Left']
trials=[]
for _,r in g.iterrows():
    T=np.floor((r.set_time-r.ready_time)*1000/20)*20/1000
    trials.append([neo.SpikeTrain((s[(s>=r.ready_time)&(s<r.ready_time+T)]-r.ready_time)*pq.s,t_start=0*pq.s,t_stop=T*pq.s) for s in sp])
print(len(trials))
for xd in [4,8]:
    t=time.time(); gp=GPFA(bin_size=20*pq.ms,x_dim=xd,em_max_iters=500)
    gp.fit(trials); print(xd,'fit',time.time()-t, 'iters',len(gp.fit_info['log_likelihoods']))
    t=time.time(); print('score',gp.score(trials[:20]),time.time()-t)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
timeout 1200 python $TMPDIR/dev3.py 2>&1 | grep -v Warning
```

```
<persisted-output>
Output too large (318.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d40c9d99-a391-4d0c-b49a-a20db4a2fd4b/tool-results/by7k7axwt.txt

Preview (first 2KB):
[2026-11-15 12:53:52,402] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,402] utils - WARNING: Correcting 2 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,403] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,403] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,403] utils - WARNING: Correcting 3 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,403] utils - WARNING: Correcting 2 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,403] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,409] utils - WARNING: Correcting a rounding error in the calculation of the number of bins by incrementing the value by 1. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,409] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 12:53:52,410] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. Y
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "WARNING" /home/runner/.claude/projects/-home-runner-work-encore-encore/d40c9d99-a391-4d0c-b49a-a20db4a2fd4b/tool-results/by7k7axwt.txt | tail -20; date -u
```

```
warnings.warn("Binning discarded {} last spike(s) of the "
  warnings.warn("Binning discarded {} last spike(s) of the "
  warnings.warn("Binning discarded {} last spike(s) of the "
  warnings.warn("Binning discarded {} last spike(s) of the "
  warnings.warn("Binning discarded {} last spike(s) of the "
222
Initializing parameters using factor analysis...

Fitting GPFA model...
4 fit 34.08015727996826 iters 500
score -7288.762038619481 0.23862147331237793
Initializing parameters using factor analysis...

Fitting GPFA model...
8 fit 52.82339262962341 iters 500
score -7155.728534679706 0.3067331314086914
0.284492 GB
Sun Nov 15 12:55:22 UTC 2026
```

**Agent**

GPFA (elephant) takes about 4 min per dataset with cross-validation, so it fits; I'll put it in a second notebook. Now prototyping the trial-averaged population analyses.

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; cat > $TMPDIR/dev4.py <<'EOF'
import sys, pickle, os, time
sys.path.insert(0,'.')
import rsg, numpy as np, pandas as pd
from scipy import stats
sess=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
tr=sess['trials']; v=tr[tr.valid]; m,_=rsg.select_units(sess)
sp=[s for s,k in zip(sess['spikes'],m) if k]
fits={ds:rsg.fit_bls(g) for ds,g in v.groupby('dataset')} if not os.path.exists(os.environ['TMPDIR']+'/fits.pkl') else pickle.load(open(os.environ['TMPDIR']+'/fits.pkl','rb'))
pickle.dump(fits,open(os.environ['TMPDIR']+'/fits.pkl','wb'))
t0=time.time()
rows=[]
for ds in rsg.DATASETS:
    g=v[v.dataset==ds]; f=fits[ds]
    est={}
    for p in rsg.PRIORS:
        gp=g[g.prior==p]; est[p]=rsg.estimation_rates(sp,gp,rsg.TS[p][-1])
    pe=rsg.pca([est[p][0] for p in rsg.PRIORS])
    prod=rsg.production_rates(sp,g)
    pp=rsg.pca([prod[ts][0] for ts in sorted(prod)])
    out=dict(ds=ds,k_est=pe['k'],k_prod=pp['k'])
    for p in rsg.PRIORS:
        r,n,ends=est[p]; X=rsg.project(pe,r)
        lo,hi=rsg.TS[p][0],rsg.TS[p][-1]
        u,_=rsg.encoding_axis(X,ends,lo,hi)
        sel=(ends>=lo)&(ends<=hi); t=ends[sel]; xu=X[sel]@u; w=n[sel]
        te=np.array([rsg.bls_predict(tt,f['wm'],f['wp'],f['b'+p],lo,hi)[0] for tt in t])
        fb=rsg.wls(te,xu,w); fl=rsg.wls(t,xu,w)
        out[p+'_r2']=fb['r2']; out[p+'_rmseB']=fb['rmse']; out[p+'_rmseL']=fl['rmse']; out[p+'_wrB']=fb['wrmse']; out[p+'_wrL']=fl['wrmse']
        out[p+'_slope']=fl['b']
        # speed
        xs=[X[list(ends).index(ts)]@u for ts in rsg.TS[p]]
        spd=[rsg.mean_step(rsg.project(pp,prod[ts][0])) for ts in rsg.TS[p]]
        out[p+'_xu']=np.round(xs,1); out[p+'_spd']=np.round(spd,2)
    # short in long
    r,n,ends=est['Long']; X=rsg.project(pe,r); sel=(ends>=480)&(ends<=800); t=ends[sel]
    u=X[list(ends).index(800)]-X[list(ends).index(480)]; u/=np.linalg.norm(u); xu=X[sel]@u
    te=np.array([rsg.bls_predict(tt,f['wm'],f['wp'],f['bShort'],480,800)[0] for tt in t])
    out['SiL_dRMSE']=rsg.wls(te,xu,n[sel])['rmse']-rsg.wls(t,xu,n[sel])['rmse']
    rows.append(out)
print(time.time()-t0)
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
print(pd.DataFrame(rows).T)
EOF
python $TMPDIR/dev4.py
```

```
0.2860238552093506
                                            0                                 1                               2                               3
ds                                   Eye Left                         Eye Right                       Hand Left                      Hand Right
k_est                                       2                                 2                               2                               2
k_prod                                      2                                 2                               4                               4
Short_r2                             0.908429                           0.95603                        0.995686                        0.973101
Short_rmseB                          6.362049                          3.265361                        0.660137                        0.728052
Short_rmseL                          6.666802                          3.493819                        1.130395                        0.765171
Short_wrB                            6.587133                          3.572788                        0.445747                        0.701324
Short_wrL                            6.956315                          3.787402                        0.778963                        0.776596
Short_slope                          0.229176                          0.190423                        0.077019                        0.046951
Short_xu     [-44.6, -45.4, -24.6, 6.4, 20.0]  [-41.2, -37.1, -18.6, 2.3, 11.9]    [-3.1, 2.4, 9.0, 16.2, 17.5]    [5.2, 7.5, 11.5, 16.4, 19.6]
Short_spd      [8.64, 7.26, 6.59, 4.98, 5.87]     [7.61, 7.54, 6.3, 5.28, 5.05]  [5.87, 5.03, 4.56, 3.64, 3.75]  [5.46, 4.93, 4.78, 3.92, 3.86]
Long_r2                              0.986605                          0.970751                        0.977365                         0.99435
Long_rmseB                           1.801743                          2.906252                        0.5827
[... 7 more lines not kept]
```

**Agent**

Trial-averaged analyses run in under a second per dataset. Now writing the main notebook (all claims but the two GPFA ones, which go in a second notebook).

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_nb1.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Sohn, Narain, Meirhaeghe & Jazayeri (2019) on DANDI:000130\n\nPaper: Sohn H, Narain D, Meirhaeghe N, Jazayeri M (2019). Bayesian computation through cortical\nlatent dynamics. *Neuron* 103, 934-947. doi:10.1016/j.neuron.2019.06.012.\n\nDataset: [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version\n0.241017.1448 (doi:10.48324/dandi.000130/0.241017.1448). This version was asked for in the\nprompt of this attempt; it is also the dandiset's published version. The paper cites no version\nof the dandiset, which was made later for the Neural Latents Benchmark.\n\nClaims: `claims/sohn-2019.yaml`, written from the accepted author manuscript (PMC6805134):\nResults, figure legends and STAR Methods; the supplementary tables and figures were not\navailable to the reader. This is a blind repeat attempt: it was made without the earlier\nattempts on this dataset.\n\nThe dandiset holds one session (2016-12-11) of monkey H, one of the paper's 17 sessions of H and\n29 of both animals. A \"dataset\" here, as in the paper, is one effector and target direction (4\nhere; the paper has 8, from two animals). The GPFA claims are in the second notebook,\n`gpfa_sohn_2019.ipynb`.\n\n| Claim | Tested here |\n|---|---|\n| beh-slopes, beh-overlap-prior, beh-sigmoid-increments, beh-long-more-bias, beh-bayes-model | yes |\n| glm-prior-ts, dfr-overlap-support | yes |\n| pca-dimensionality, encoding-r2, encoding-bayes-beats-linear, short-in-long-control, neural-long-more-bias | yes |\n| speed-vs-projection, initial-speed-biased, speed-predicts-tp | yes |\n| alt-speed-unmodulated, alt-transient-parallel, alt-threshold-monotonic | yes |\n| gpfa-variance-inverted-u, gpfa-mean-sigmoid | yes, in `gpfa_sohn_2019.ipynb` |\n| rnn-curved-manifold, rnn-perturbation | blocked: the networks are not in the dandiset (data_missing) |\n| monkey-g | blocked: monkey G is not in the dandiset (data_missing) |\n\nMethod details that the claims file leaves open are taken from the paper, with the passage cited\nin the cell or in `rsg.py`; every random generator is seeded per section.\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nimport time\nimport resource\nimport warnings\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport statsmodels.api as sm\nimport rsg\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nT0 = time.time()\nprint(\"dandiset\", rsg.DANDISET_ID, \"version\", rsg.VERSION)\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nsess = rsg.load_session()\ntr = sess[\"trials\"]\nprint(sess[\"meta\"])\nprint(\"trials in the train file:\", len(tr), \"| by NLB split:\", tr.split.value_counts().to_dict())\nprint(\"units:\", len(sess[\"spikes\"]), \"| held out for NLB:\", int(sess[\"heldout\"].sum()))\nprint(\"observation intervals identical for all units:\",\n      all(np.array_equal(o, sess[\"obs_intervals\"][0]) for o in sess[\"obs_intervals\"]),\n      \"| observed\", round(sess[\"duration\"], 1), \"s in\", len(sess[\"obs_intervals\"][0]), \"intervals\")\ngaps = sess[\"obs_intervals\"][0][1:, 0] - sess[\"obs_intervals\"][0][:-1, 1]\nprint(\"gaps between observation intervals (s):\", np.round(gaps, 3))\nprint(\"spike times sorted in every unit:\", all(np.all(np.diff(s) >= 0) for s in sess[\"spikes\"]))\nprint(\"spike time range (s):\", round(min(s[0] for s in sess[\"spikes\"]), 3), \"to\",\n      round(max(s[-1] for s in sess[\"spikes\"]), 3))\n\ntest, io = rsg.open_nwb(rsg.TEST_PATH)\ntt = test.trials.to_dataframe()\nprint(\"test file: trials\", len(tt), \"columns\", list(tt.columns), \"units\", len(test.units),\n      \"| segment length (s):\", np.unique(np.round(tt.stop_time - tt.start_time, 3)))\nio.close()\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\nprint(\"completed (Set and Go present, no bad_time, tp > 0):\", int(tr.completed.sum()))\nprint(\"completed and flagged is_outlier:\", int((tr.completed & tr.is_outlier).sum()))\nprint(\"valid (completed, not outlier):\", int(tr.valid.sum()))\nprint(\"trials with Go and a bad_time (left out):\", int((tr.go_time.notna() & tr.bad_time.notna()).sum()))\nv = tr[tr.valid].copy()\nprint(\"valid trials by split:\", v.split.value_counts().to_dict())\nprint(\"ts values:\", sorted(v.ts.unique()), \"| iti by prior (ms):\",\n      v.groupby(\"prior\").iti.unique().to_dict())\nprint(\"theta values:\", sorted(tr.theta.unique()), \"| is_eye:\", sorted(tr.is_eye.unique()))\nprint(\"tp range (ms):\", round(v.tp.min(), 1), \"to\", round(v.tp.max(), 1))\ncounts = v.groupby([\"prior\", \"ts\", \"effector\", \"direction\"]).size().unstack([\"effector\", \"direction\"])\nprint(\"valid trials per condition (min\", int(counts.values.min()), \", max\", int(counts.values.max()), \"):\")\nprint(counts)\n\n# Event times against the interval columns\nd_ts = (v.set_time - v.ready_time) * 1000 - v.ts\nd_tp = (v.go_time - v.set_time) * 1000 - v.tp\nprint(\"\\n(Set - Ready) - ts, ms: min\", round(d_ts.min(), 1), \"median\", round(d_ts.median(), 1),\n      \"max\", round(d_ts.max(), 1))\nprint(\"(Go - Set) - tp, ms: min\", round(d_tp.min(), 1), \"median\", round(d_tp.median(), 1),\n      \"max\", round(d_tp.max(), 1), \"| |difference| > 60 ms in\", int((d_tp.abs() > 60).sum()), \"trials\")\nprint(\"prior and iti agree (Short 500, Long 1220):\",\n      bool(((v.prior == \"Short\") == (v.iti == 500)).all()))\n\nunit_mask, unit_rate = rsg.select_units(sess)\nprint(\"\\nunit mean rates (spikes/s): min\", round(unit_rate.min(), 2), \"max\", round(unit_rate.max(), 2))\nprint(\"units below 1 spike/s:\", list(sess[\"unit_ids\"][unit_rate < 1]), np.round(unit_rate[unit_rate < 1], 2))\nprint(\"units selected:\", int(unit_mask.sum()), \"of\", len(unit_mask))\nspikes = [s for s, k in zip(sess[\"spikes\"], unit_mask) if k]\nprint(\"run time so far\", round(time.time() - T0), \"s\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n### Do the spikes share the clock of the trial table?\n\nTarget direction is randomised trial by trial (Methods, \"Trial structure\"), so it is a contrast\nthat an offset between the spike clock and the trial table would destroy. Direction is decoded\n(5-fold cross-validated logistic regression, all 54 units) from spike counts in 200 ms windows\naround Go, with the true event times and with the times shifted by 10 s, which moves the windows\ninto other trials. A standard choice of decoder; it is a check of the data, not a claim.\n\"\"\")\n\ncode(r\"\"\"\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score, StratifiedKFold\n\nrng = np.random.default_rng(0)\nyv = (v.direction == \"Left\").values.astype(int)\ncv = StratifiedKFold(5, shuffle=True, random_state=0)\nrows = []\nfor start in [-1000, -600, -200, 0, 200]:\n    for shift in [0.0, 10.0]:\n        c = rsg.bin_counts(sess[\"spikes\"], v.go_time.values + shift, [start, start + 200])[:, :, 0]\n        acc = cross_val_score(LogisticRegression(max_iter=2000), np.sqrt(c), yv, cv=cv).mean()\n        rows.append(dict(window_from_go_ms=start, shift_s=shift, accuracy=round(acc, 3)))\nclock = pd.DataFrame(rows).pivot(index=\"window_from_go_ms\", columns=\"shift_s\", values=\"accuracy\")\nprint(\"direction decoding accuracy (chance about\", round(max(yv.mean(), 1 - yv.mean()), 3), \")\")\nprint(clock)\n\n# Set-evoked population response: mean rate of all units around Set, true and shifted times\nedges = np.arange(-400, 401, 20)\nfor shift in [0.0, 10.0]:\n    c = rsg.bin_counts(sess[\"spikes\"], v.set_time.values + shift, edges)\n    pop = c.mean((0, 1)) / 0.02\n    print(f\"shift {shift:4.1f} s: population rate 200 ms before Set {pop[:20][-10:].mean():.2f}, \"\n          f\"0-200 ms after {pop[20:30].mean():.2f} spikes/s; peak at {edges[1:][np.argmax(pop)]} ms\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## Behaviour\n\n### beh-slopes\n\n> Regression slopes of tp on ts are positive and less than one in every condition, so the animals\n> estimated ts and their responses were biased toward the mean of the prior.\n\nCriterion: per prior, effector and direction (8 conditions) a weighted regression of tp on ts,\neach trial weighted by 1 over the variance of tp at its ts; all 8 slopes in (0, 1) with 95%\nintervals excluding 0 and 1. The Methods write the regression as \"tp = β ts + ε\" (Methods,\n\"Model free analysis of behavior\"). A slope below 1 can only show a bias toward the mean if the\nline has an intercept, so the fit with an intercept is the main reading; the fit through the\norigin is shown as the other reading.\n\"\"\")\n\ncode(r\"\"\"\ndef slope_table(v):\n    rows = []\n    for (ds, prior), g in v.groupby([\"dataset\", \"prior\"]):\n        w = 1 / g.groupby(\"ts\").tp.transform(\"var\")\n        r = sm.WLS(g.tp, sm.add_constant(g.ts.astype(float)), weights=w).fit()\n        r0 = sm.WLS(g.tp, g.ts.astype(float), weights=w).fit()\n        lo, hi = r.conf_int().loc[\"ts\"]\n        lo0, hi0 = r0.conf_int().loc[\"ts\"]\n        rows.append(dict(dataset=ds, prior=prior, n=len(g), slope=r.params[\"ts\"], ci_lo=lo, ci_hi=hi,\n                         intercept=r.params[\"const\"], slope_origin=r0.params[\"ts\"],\n                         ci_lo_origin=lo0, ci_hi_origin=hi0))\n    return pd.DataFrame(rows)\n\nslopes = slope_table(v)\nprint(slopes.round(3))\nin_ci = ((slopes.ci_lo > 0) & (slopes.ci_hi < 1))\nin_01 = ((slopes.slope > 0) & (slopes.slope < 1))\nprint(\"with intercept: slopes in (0,1):\", int(in_01.sum()), \"of 8; intervals excluding 0 and 1:\", int(in_ci.sum()), \"of 8\")\nin_01o = ((slopes.slope_origin > 0) & (slopes.slope_origin < 1))\nin_cio = ((slopes.ci_lo_origin > 0) & (slopes.ci_hi_origin < 1))\nprint(\"through the origin: slopes in (0,1):\", int(in_01o.sum()), \"of 8; intervals excluding 0 and 1:\", int(in_cio.sum()), \"of 8\")\n\"\"\", tags=[\"claim:beh-slopes\"])\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 4, figsize=(14, 3.2), sharey=True)\nfor ax, ds in zip(axes, rsg.DATASETS):\n    g = v[v.dataset == ds]\n    for prior, col in [(\"Short\", \"tab:red\"), (\"Long\", \"tab:blue\")]:\n        gp = g[g.prior == prior]\n        ax.plot(gp.ts + rng.uniform(-10, 10, len(gp)), gp.tp, \".\", ms=2, color=col, alpha=0.4)\n        m = gp.groupby(\"ts\").tp.mean()\n        ax.plot(m.index, m.values, \"o-\", color=col)\n    ax.plot([450, 1250], [450, 1250], \"k--\", lw=0.8)\n    ax.set_title(ds); ax.set_xlabel(\"ts (ms)\")\naxes[0].set_ylabel(\"tp (ms)\")\naxes[0].set_ylim(300, 1700)\nprint(\"tp outside the axes (300 to 1700 ms):\", int(((v.tp < 300) | (v.tp > 1700)).sum()), \"trials\")\nplt.tight_layout(); plt.show()\n\"\"\", tags=[\"claim:beh-slopes\"])\n\nmd(r\"\"\"\n**Result: ...** (filled after the run)\n\"\"\")\n\nmd(r\"\"\"\n### beh-overlap-prior\n\n> At the overlapping ts of 800 ms, biases were in opposite directions for the two priors.\n\nCriterion: ts = 800 trials pooled over effector and direction; median of tp - 800 negative for\nShort and positive for Long, and a two-sided rank-sum test of tp between priors with p < 0.05.\n\"\"\")\n\ncode(r\"\"\"\no = v[v.ts == 800]\nrows = []\nfor name, g in [(\"pooled\", o)] + list(o.groupby(\"dataset\")):\n    s, l = g[g.prior == \"Short\"].tp, g[g.prior == \"Long\"].tp\n    p = stats.mannwhitneyu(s, l, alternative=\"two-sided\").pvalue\n    rows.append(dict(set=name, n_short=len(s), n_long=len(l), median_bias_short=np.median(s - 800),\n                     median_bias_long=np.median(l - 800), mean_bias_short=np.mean(s - 800),\n                     mean_bias_long=np.mean(l - 800), p_ranksum=p))\nprint(pd.DataFrame(rows).round(4))\n\"\"\", tags=[\"claim:beh-overlap-prior\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### beh-sigmoid-increments\n\n> Increments of tp between neighbouring ts are smaller at the extremes of the prior than near its\n> mean.\n\nCriterion: per condition (8), mean tp at each ts; extreme increment = mean of first and last,\nmiddle = mean of second and third; middle exceeds extreme in most conditions, and a two-sided\nsigned-rank test over the 8 conditions has p < 0.05.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (ds, prior), g in v.groupby([\"dataset\", \"prior\"]):\n    m = g.groupby(\"ts\").tp.mean().reindex(rsg.TS[prior]).values\n    ext, mid = rsg.increments(m)\n    rows.append(dict(dataset=ds, prior=prior, inc=np.round(np.diff(m), 1), extreme=ext, middle=mid))\ninc = pd.DataFrame(rows)\nprint(inc.round(1))\nprint(\"middle > extreme in\", int((inc.middle > inc.extreme).sum()), \"of 8\")\nw = stats.wilcoxon(inc.middle, inc.extreme)\nprint(\"two-sided signed-rank: statistic\", w.statistic, \"p =\", round(w.pvalue, 4),\n      \"| median middle - extreme\", round(np.median(inc.middle - inc.extreme), 1), \"ms\")\n\"\"\", tags=[\"claim:beh-sigmoid-increments\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### beh-long-more-bias\n\n> Biases are larger for the Long prior than for the Short prior, as scalar variability predicts;\n> regression slopes are smaller for Long.\n\nCriterion: with the slopes of beh-slopes, Long below Short in all 4 datasets.\n\"\"\")\n\ncode(r\"\"\"\ncmp = slopes.pivot(index=\"dataset\", columns=\"prior\", values=\"slope\")\ncmp[\"long_below_short\"] = cmp.Long < cmp.Short\ncmp0 = slopes.pivot(index=\"dataset\", columns=\"prior\", values=\"slope_origin\")\ncmp[\"origin_long_below_short\"] = cmp0.Long < cmp0.Short\nprint(cmp.round(3))\nprint(\"Long below Short (with intercept):\", int(cmp.long_below_short.sum()), \"of 4;\",\n      \"through the origin:\", int(cmp.origin_long_below_short.sum()), \"of 4\")\n\"\"\", tags=[\"claim:beh-long-more-bias\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### beh-bayes-model\n\n> A Bayesian observer model with scalar measurement and production noise fit to the behaviour\n> captures the bias and the variance of tp in all conditions.\n\nCriterion: the model fit per dataset (wm, wp, bShort, bLong); across the 10 prior and ts\nconditions the R2 of the observed mean bias by the predicted bias (at least 0.8) and the Pearson\ncorrelation of observed and predicted SD of tp (positive), in all 4 datasets. The R2 is computed\nas 1 - SSres/SStot of the observed biases around the predicted ones; the squared correlation is\nshown as the other reading.\n\"\"\")\n\ncode(r\"\"\"\nfits = {}\nrows = []\nfor ds in rsg.DATASETS:\n    g = v[v.dataset == ds]\n    f = rsg.fit_bls(g)\n    fits[ds] = f\n    obs_b, pred_b, obs_sd, pred_sd = [], [], [], []\n    for prior in rsg.PRIORS:\n        lo, hi = rsg.TS[prior][0], rsg.TS[prior][-1]\n        for ts in rsg.TS[prior]:\n            x = g[(g.prior == prior) & (g.ts == ts)].tp\n            _, m, sd = rsg.bls_predict(ts, f[\"wm\"], f[\"wp\"], f[\"b\" + prior], lo, hi)\n            obs_b.append(x.mean() - ts); pred_b.append(m - ts); obs_sd.append(x.std()); pred_sd.append(sd)\n    obs_b, pred_b = np.array(obs_b), np.array(pred_b)\n    r2 = 1 - np.sum((obs_b - pred_b) ** 2) / np.sum((obs_b - obs_b.mean()) ** 2)\n    rows.append(dict(dataset=ds, wm=f[\"wm\"], wp=f[\"wp\"], bShort=f[\"bShort\"], bLong=f[\"bLong\"],\n                     converged=f[\"success\"], bias_R2=r2, bias_r2_corr=stats.pearsonr(obs_b, pred_b)[0] ** 2,\n                     sd_r=stats.pearsonr(obs_sd, pred_sd)[0], sd_p=stats.pearsonr(obs_sd, pred_sd)[1],\n                     obs_sd_range=f\"{min(obs_sd):.0f}-{max(obs_sd):.0f}\",\n                     pred_sd_range=f\"{min(pred_sd):.0f}-{max(pred_sd):.0f}\"))\nbayes = pd.DataFrame(rows)\nprint(bayes.round(3))\nprint(\"bias R2 >= 0.8 in\", int((bayes.bias_R2 >= 0.8).sum()), \"of 4; SD correlation > 0 in\",\n      int((bayes.sd_r > 0).sum()), \"of 4\")\n\"\"\", tags=[\"claim:beh-bayes-model\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## Single neurons\n\n### glm-prior-ts\n\n> About 30% of neurons were modulated by elapsed time (27% in monkey H) and more than 60% were\n> sensitive to the prior (65% in monkey H), by a Poisson GLM of spike counts before Set compared\n> by BIC.\n\nCriterion: selected units; counts in the 80 ms before 480, 560, 640, 720 and 800 ms after Ready\nfrom every trial whose Set comes at or after that time (attrition), both priors. Prior model:\nlog rate = 5 time indicators + prior + effector + direction, against the model without prior.\nts model per prior: 5 time indicators + effector + direction against intercept + effector +\ndirection; ts-dependent when BIC favours the full model in either prior. Expected 65 ± 6.5% and\n27 ± 2.7%.\n\nThe attrition rule includes the window that ends at Set itself (ts = t), which is the \"80-ms\nwindow immediately before Set\" of the Methods (\"Generalized linear model\").\n\"\"\")\n\ncode(r\"\"\"\nwin_end = np.array(rsg.TS[\"Short\"])\nrows_obs = []\nfor j, t in enumerate(win_end):\n    g = v[v.ts >= t]\n    c = rsg.bin_counts(spikes, g.ready_time.values, [t - 80, t])[:, :, 0]\n    rows_obs.append(dict(j=np.full(len(g), j), prior=(g.prior == \"Long\").values.astype(float),\n                         eff=(g.effector == \"Hand\").values.astype(float),\n                         dirn=(g.direction == \"Left\").values.astype(float), counts=c))\nJ = np.concatenate([r[\"j\"] for r in rows_obs])\nPRI = np.concatenate([r[\"prior\"] for r in rows_obs])\nEFF = np.concatenate([r[\"eff\"] for r in rows_obs])\nDIR = np.concatenate([r[\"dirn\"] for r in rows_obs])\nY = np.concatenate([r[\"counts\"] for r in rows_obs])\nTI = (J[:, None] == np.arange(5)[None, :]).astype(float)\nprint(\"observations:\", len(J), \"| per window:\", np.bincount(J), \"| Long share:\", round(PRI.mean(), 3))\n\nres = []\nfor i in range(Y.shape[1]):\n    y = Y[:, i]\n    full = rsg.glm_bic(y, np.column_stack([TI, PRI, EFF, DIR]))\n    red = rsg.glm_bic(y, np.column_stack([TI, EFF, DIR]))\n    ts_dep, fails = False, 0\n    for pv in (0.0, 1.0):\n        s = PRI == pv\n        b1 = rsg.glm_bic(y[s], np.column_stack([TI[s], EFF[s], DIR[s]]))\n        b0 = rsg.glm_bic(y[s], np.column_stack([np.ones(s.sum()), EFF[s], DIR[s]]))\n        if b1 is None or b0 is None:\n            fails += 1\n        elif b1 < b0:\n            ts_dep = True\n    res.append(dict(prior_dep=(full is not None and red is not None and full < red), ts_dep=ts_dep,\n                    fails=fails + (full is None) + (red is None), mean_count=y.mean()))\nglm = pd.DataFrame(res)\nn = len(glm)\ndef binom_ci(k, n):\n    ci = stats.binomtest(int(k), n).proportion_ci(0.95)\n    return round(100 * ci.low, 1), round(100 * ci.high, 1)\nkp, kt = int(glm.prior_dep.sum()), int(glm.ts_dep.sum())\nprint(\"units\", n, \"| failed fits\", int(glm.fails.sum()))\nprint(f\"prior-dependent: {kp}/{n} = {100*kp/n:.1f}%  95% CI {binom_ci(kp, n)}  (expected 65 +/- 6.5)\")\nprint(f\"ts-dependent:    {kt}/{n} = {100*kt/n:.1f}%  95% CI {binom_ci(kt, n)}  (expected 27 +/- 2.7)\")\nprint(\"both:\", int((glm.prior_dep & glm.ts_dep).sum()), \"| neither:\", int((~glm.prior_dep & ~glm.ts_dep).sum()))\n\"\"\", tags=[\"claim:glm-prior-ts\"])\n\ncode(r\"\"\"\n# Variants: (i) the ts model on Long trials uses the same 5 windows; (ii) all 54 units;\n# (iii) without attrition (each window only from trials of ts >= 800, i.e. same trials for all windows).\ndef glm_fracs(Y, TI, PRI, EFF, DIR):\n    kp = kt = 0\n    for i in range(Y.shape[1]):\n        y = Y[:, i]\n        f, r = rsg.glm_bic(y, np.column_stack([TI, PRI, EFF, DIR])), rsg.glm_bic(y, np.column_stack([TI, EFF, DIR]))\n        kp += (f is not None and r is not None and f < r)\n        dep = False\n        for pv in (0.0, 1.0):\n            s = PRI == pv\n            b1 = rsg.glm_bic(y[s], np.column_stack([TI[s], EFF[s], DIR[s]]))\n            b0 = rsg.glm_bic(y[s], np.column_stack([np.ones(s.sum()), EFF[s], DIR[s]]))\n            dep |= (b1 is not None and b0 is not None and b1 < b0)\n        kt += dep\n    return round(100 * kp / Y.shape[1], 1), round(100 * kt / Y.shape[1], 1)\n\nYall = np.concatenate([rsg.bin_counts(sess[\"spikes\"], v[v.ts >= t].ready_time.values, [t - 80, t])[:, :, 0]\n                       for t in win_end])\nprint(\"all 54 units: prior %, ts % =\", glm_fracs(Yall, TI, PRI, EFF, DIR))\ng8 = v[v.ts >= 800]\nrows = [rsg.bin_counts(spikes, g8.ready_time.values, [t - 80, t])[:, :, 0] for t in win_end]\nJn = np.repeat(np.arange(5), len(g8))\nTIn = (Jn[:, None] == np.arange(5)[None, :]).astype(float)\nrep = lambda a: np.tile(a, 5)\nprint(\"no attrition (trials with ts >= 800 only): prior %, ts % =\",\n      glm_fracs(np.vstack(rows), TIn, rep((g8.prior == \"Long\").values.astype(float)),\n                rep((g8.effector == \"Hand\").values.astype(float)), rep((g8.direction == \"Left\").values.astype(float))))\n\"\"\", tags=[\"claim:glm-prior-ts\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### dfr-overlap-support\n\n> At the overlapping ts of 800 ms, firing rates differ between priors, with the largest\n> difference during the support of the prior, between 480 and 800 ms after Ready.\n\nCriterion: per dataset, selected units, ts = 800 trials; per unit the difference of mean rates\nbetween priors in 160 ms bins from 320 ms before Ready to 640 ms after Set; RMS over units,\naveraged over the 4 datasets; the largest value in a bin within 480 to 800 ms after Ready and\nabove the 95th percentile of the largest value over 200 shuffles of the prior labels among\nts = 800 trials (within dataset).\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(7)\nedges = np.arange(-320, 800 + 640 + 1, 160)\ncenters = (edges[:-1] + edges[1:]) / 2\ndat = {}\nfor ds in rsg.DATASETS:\n    g = v[(v.dataset == ds) & (v.ts == 800)]\n    c = rsg.bin_counts(spikes, g.ready_time.values, edges) / 0.16\n    dat[ds] = (c, (g.prior == \"Long\").values)\n\ndef rms_curve(labels):\n    out = []\n    for ds in rsg.DATASETS:\n        c, _ = dat[ds]\n        L = labels[ds]\n        d = c[L].mean(0) - c[~L].mean(0)\n        out.append(np.sqrt((d ** 2).mean(0)))\n    return np.array(out)\n\nper_ds = rms_curve({ds: dat[ds][1] for ds in rsg.DATASETS})\ncurve = per_ds.mean(0)\nnull_max = []\nfor _ in range(200):\n    null_max.append(rms_curve({ds: rng.permutation(dat[ds][1]) for ds in rsg.DATASETS}).mean(0).max())\nthr = np.percentile(null_max, 95)\ntab = pd.DataFrame(per_ds.T, index=[f\"{a}..{b}\" for a, b in zip(edges[:-1], edges[1:])], columns=rsg.DATASETS)\ntab[\"mean\"] = curve\nprint(\"RMS of the prior difference (spikes/s), bins in ms from Ready (Set at 800):\")\nprint(tab.round(2))\nprint(\"trials per dataset (Short, Long):\", {ds: (int((~dat[ds][1]).sum()), int(dat[ds][1].sum())) for ds in rsg.DATASETS})\nkmax = int(np.argmax(curve))\nprint(\"largest value\", round(curve[kmax], 2), \"in bin\", tab.index[kmax], \"ms; shuffle 95th percentile of the maximum\",\n      round(thr, 2), \"(median\", round(np.median(null_max), 2), \")\")\nprint(\"largest bin within 480-800 ms:\", bool(edges[kmax] >= 480 and edges[kmax + 1] <= 800))\nprint(\"bins above the shuffle threshold:\", list(tab.index[curve > thr]))\n\"\"\", tags=[\"claim:dfr-overlap-support\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## Population trajectories\n\nRates, PCA and the encoding axis follow the claims file's header (see `rsg.py`). Estimation\nepoch: per prior, the trajectory from Ready to the prior's longest ts, each 20 ms bin averaging\nthe trials whose ts is at least the end of the bin. Production epoch: per ts, from Set to the\nshortest tp of that ts. The state at time t is the bin ending at t.\n\"\"\")\n\ncode(r\"\"\"\ngeo = {}\nfor ds in rsg.DATASETS:\n    g = v[v.dataset == ds]\n    est = {p: rsg.estimation_rates(spikes, g[g.prior == p], rsg.TS[p][-1]) for p in rsg.PRIORS}\n    pe = rsg.pca([est[p][0] for p in rsg.PRIORS])\n    prod = rsg.production_rates(spikes, g)\n    pp = rsg.pca([prod[ts][0] for ts in sorted(prod)])\n    geo[ds] = dict(g=g, est=est, pe=pe, prod=prod, pp=pp)\n    print(ds, \"| estimation bins\", {p: len(est[p][2]) for p in rsg.PRIORS},\n          \"| production bins per ts\", {ts: len(prod[ts][1]) for ts in sorted(prod)},\n          \"| shortest tp per ts\", {ts: round(prod[ts][3]) for ts in sorted(prod)})\nr_all = np.concatenate([np.vstack([geo[ds][\"est\"][p][0] for p in rsg.PRIORS]) for ds in rsg.DATASETS])\nprint(\"smoothed rates (spikes/s), estimation epoch: min\", round(r_all.min(), 2), \"max\", round(r_all.max(), 2))\n\"\"\")\n\nmd(r\"\"\"\n### pca-dimensionality\n\n> Population activity is low dimensional; 3 to 4 principal components in the estimation epoch\n> and 5 to 10 in the production epoch explain about 75% of the variance.\n\nCriterion: components needed for 75% per dataset and epoch; reproduced when all 8 fall in 3-4\n(estimation) and 5-11 (production); partially when at least 4 do. Rates are not normalised\n(claims file header). As variants, the counts after soft normalisation (rate / (range + 5\nspikes/s), a common choice in this literature, not stated in the paper) and after z-scoring are\nshown; they do not decide the outcome.\n\"\"\")\n\ncode(r\"\"\"\ndef k_for(blocks, frac=0.75, norm=None):\n    X = np.vstack(blocks)\n    if norm == \"soft\":\n        X = X / (X.max(0) - X.min(0) + 5)\n    elif norm == \"z\":\n        X = (X - X.mean(0)) / (X.std(0) + 1e-9)\n    return rsg.pca([X], frac)\n\nrows = []\nfor ds in rsg.DATASETS:\n    G = geo[ds]\n    eb = [G[\"est\"][p][0] for p in rsg.PRIORS]\n    pb = [G[\"prod\"][ts][0] for ts in sorted(G[\"prod\"])]\n    rows.append(dict(dataset=ds, k_est=G[\"pe\"][\"k\"], k_prod=G[\"pp\"][\"k\"],\n                     cum_est_3=np.cumsum(G[\"pe\"][\"explained\"])[2], cum_prod_5=np.cumsum(G[\"pp\"][\"explained\"])[4],\n                     k_est_soft=k_for(eb, norm=\"soft\")[\"k\"], k_prod_soft=k_for(pb, norm=\"soft\")[\"k\"],\n                     k_est_z=k_for(eb, norm=\"z\")[\"k\"], k_prod_z=k_for(pb, norm=\"z\")[\"k\"]))\ndims = pd.DataFrame(rows)\nprint(dims.round(3))\nok = ((dims.k_est >= 3) & (dims.k_est <= 4)).sum() + ((dims.k_prod >= 5) & (dims.k_prod <= 11)).sum()\nprint(\"values in range:\", int(ok), \"of 8\")\nfor ds in rsg.DATASETS:\n    print(ds, \"estimation cumulative variance of PCs 1-5:\", np.round(np.cumsum(geo[ds][\"pe\"][\"explained\"])[:5], 3),\n          \"| production:\", np.round(np.cumsum(geo[ds][\"pp\"][\"explained\"])[:6], 3))\n\"\"\", tags=[\"claim:pca-dimensionality\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### encoding-r2\n\n> Projections of estimation-epoch neural states onto the encoding axis match the Bayesian\n> estimates from the model fitted to the behaviour (R2 = 0.993 Short, 0.996 Long, monkey H, Hand\n> Left).\n\nCriterion: weighted regression Xu = a + b te over the 20 ms time points of the prior's support,\neach point weighted by the number of trials it averages; te(t) is the model's mean estimate for\nts = t from the fit of beh-bayes-model to the same dataset. Readings: (a) Hand Left; (b) mean\nover the 4 datasets. Reproduced when under one reading both R2 are within tolerance (at least\n0.894 and 0.896). The R2 for 1000 random unit vectors in the same PC space is the reference.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(11)\nenc = {}\nrows = []\nfor ds in rsg.DATASETS:\n    G, f = geo[ds], fits[ds]\n    for p in rsg.PRIORS:\n        r, n, ends = G[\"est\"][p]\n        X = rsg.project(G[\"pe\"], r)\n        lo, hi = rsg.TS[p][0], rsg.TS[p][-1]\n        u, nvec = rsg.encoding_axis(X, ends, lo, hi)\n        sel = (ends >= lo) & (ends <= hi)\n        t, xu, w = ends[sel], X[sel] @ u, n[sel]\n        te = np.array([rsg.bls_predict(tt, f[\"wm\"], f[\"wp\"], f[\"b\" + p], lo, hi)[0] for tt in t])\n        fb, fl = rsg.wls(te, xu, w), rsg.wls(t.astype(float), xu, w)\n        # random axes in the same PC space\n        R = rng.standard_normal((1000, X.shape[1]))\n        R /= np.linalg.norm(R, axis=1, keepdims=True)\n        r2_rand = np.array([rsg.wls(te, X[sel] @ q, w)[\"r2\"] for q in R])\n        enc[(ds, p)] = dict(t=t, xu=xu, w=w, te=te, u=u, X=X, ends=ends, fb=fb, fl=fl)\n        rows.append(dict(dataset=ds, prior=p, k=X.shape[1], n_axis_vectors=nvec, points=len(t),\n                         weights=f\"{w.min()}-{w.max()}\", R2_bayes=fb[\"r2\"],\n                         R2_unweighted=stats.pearsonr(te, xu)[0] ** 2,\n                         R2_random_median=np.median(r2_rand), R2_random_95=np.percentile(r2_rand, 95),\n                         frac_random_ge=np.mean(r2_rand >= fb[\"r2\"])))\nencr = pd.DataFrame(rows)\nprint(encr.round(4))\na = encr[encr.dataset == \"Hand Left\"].set_index(\"prior\").R2_bayes\nb = encr.groupby(\"prior\").R2_bayes.mean()\nprint(\"(a) Hand Left: Short\", round(a[\"Short\"], 4), \"Long\", round(a[\"Long\"], 4))\nprint(\"(b) mean of 4: Short\", round(b[\"Short\"], 4), \"Long\", round(b[\"Long\"], 4))\nprint(\"within tolerance (Short >= 0.894, Long >= 0.896): (a)\", bool(a[\"Short\"] >= 0.894 and a[\"Long\"] >= 0.896),\n      \"(b)\", bool(b[\"Short\"] >= 0.894 and b[\"Long\"] >= 0.896))\n\"\"\", tags=[\"claim:encoding-r2\"])\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 4, figsize=(14, 3), sharex=True)\nfor ax, ds in zip(axes, rsg.DATASETS):\n    for p, col in [(\"Short\", \"tab:red\"), (\"Long\", \"tab:blue\")]:\n        e = enc[(ds, p)]\n        fb = e[\"fb\"]\n        ax.plot(e[\"t\"], (e[\"xu\"] - fb[\"a\"]) / fb[\"b\"], \"o\", ms=3, color=col)\n        ax.plot(e[\"t\"], e[\"te\"], \"-\", color=col)\n    ax.plot([480, 1200], [480, 1200], \"k--\", lw=0.6)\n    ax.set_title(ds); ax.set_xlabel(\"t after Ready (ms)\")\naxes[0].set_ylabel(\"Xu mapped to te (ms); line: te\")\nplt.tight_layout(); plt.show()\nprint(\"all points are inside the axes (autoscaled)\")\n\"\"\", tags=[\"claim:encoding-r2\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### encoding-bayes-beats-linear\n\n> Neural projections are better explained by the Bayesian model than by a linear function of ts\n> with the same number of parameters, for both priors.\n\nCriterion: RMSE of the weighted fits Xu = a + b te and Xu = a + b ts, per dataset and prior;\nreproduced when the Bayesian RMSE is lower in all 4 datasets for both priors, partially when for\none prior. \"RMSE\" is read as the root mean squared residual of the weighted fit (Methods: \"RMSE\nbetween the actual and predicted Xu\"); the weighted RMSE is shown as the other reading.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (ds, p), e in enc.items():\n    rows.append(dict(dataset=ds, prior=p, rmse_bayes=e[\"fb\"][\"rmse\"], rmse_linear=e[\"fl\"][\"rmse\"],\n                     d_rmse=e[\"fb\"][\"rmse\"] - e[\"fl\"][\"rmse\"],\n                     wrmse_bayes=e[\"fb\"][\"wrmse\"], wrmse_linear=e[\"fl\"][\"wrmse\"],\n                     d_wrmse=e[\"fb\"][\"wrmse\"] - e[\"fl\"][\"wrmse\"]))\nbl = pd.DataFrame(rows)\nprint(bl.round(4))\nfor p in rsg.PRIORS:\n    s = bl[bl.prior == p]\n    print(p, \"| Bayesian lower in\", int((s.d_rmse < 0).sum()), \"of 4 (RMSE);\", int((s.d_wrmse < 0).sum()),\n          \"of 4 (weighted RMSE); signed-rank p =\", round(stats.wilcoxon(s.d_rmse).pvalue, 3))\n\"\"\", tags=[\"claim:encoding-bayes-beats-linear\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### short-in-long-control\n\n> In the Long prior during the period matched to the support of the Short prior, there is no\n> sigmoidal representation; the Bayesian model is not better than the linear one.\n\nCriterion (absence, on the paper's test): Long-prior states from 480 to 800 ms after Ready; an\naxis from the state at 480 to that at 800 ms; compared with the Short prior's te and with ts as\nabove; reproduced when a two-sided signed-rank test of the RMSE difference over the 4 datasets\nhas p >= 0.05. With 4 datasets the smallest possible two-sided p is 0.125, so the test cannot find\nthe effect; the per-dataset differences are the effect size. The Methods say \"the same projection\nanalysis\", which would average the difference vectors as for u; that axis is shown too.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor ds in rsg.DATASETS:\n    G, f = geo[ds], fits[ds]\n    r, n, ends = G[\"est\"][\"Long\"]\n    X = rsg.project(G[\"pe\"], r)\n    sel = (ends >= 480) & (ends <= 800)\n    t, w = ends[sel], n[sel]\n    te = np.array([rsg.bls_predict(tt, f[\"wm\"], f[\"wp\"], f[\"bShort\"], 480, 800)[0] for tt in t])\n    ends_l = list(ends)\n    u1 = X[ends_l.index(800)] - X[ends_l.index(480)]; u1 /= np.linalg.norm(u1)\n    u2, _ = rsg.encoding_axis(X, ends, 480, 800)\n    row = dict(dataset=ds, weights=f\"{w.min()}-{w.max()}\")\n    for name, u in [(\"single\", u1), (\"averaged\", u2)]:\n        xu = X[sel] @ u\n        fb, fl = rsg.wls(te, xu, w), rsg.wls(t.astype(float), xu, w)\n        row[f\"d_rmse_{name}\"] = fb[\"rmse\"] - fl[\"rmse\"]\n        row[f\"r2_bayes_{name}\"] = fb[\"r2\"]\n        row[f\"r2_linear_{name}\"] = fl[\"r2\"]\n    s = enc[(ds, \"Short\")]\n    row[\"d_rmse_short_prior\"] = s[\"fb\"][\"rmse\"] - s[\"fl\"][\"rmse\"]\n    rows.append(row)\nsil = pd.DataFrame(rows)\nprint(sil.round(4))\nfor name in [\"single\", \"averaged\"]:\n    print(name, \"axis: signed-rank p =\", round(stats.wilcoxon(sil[f\"d_rmse_{name}\"]).pvalue, 3),\n          \"| mean d_RMSE\", round(sil[f\"d_rmse_{name}\"].mean(), 4))\nprint(\"Short prior mean d_RMSE for comparison:\", round(sil.d_rmse_short_prior.mean(), 4))\n\"\"\", tags=[\"claim:short-in-long-control\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### neural-long-more-bias\n\n> Neural projections show more bias for the Long prior than for the Short prior, as a smaller\n> regression slope of Xu on ts.\n\nCriterion: slope of the weighted regression of Xu (spikes/s, in the dataset's shared PC space)\non ts (ms), per dataset and prior; Long below Short in all 4 datasets.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor ds in rsg.DATASETS:\n    rows.append(dict(dataset=ds, slope_short=enc[(ds, \"Short\")][\"fl\"][\"b\"], slope_long=enc[(ds, \"Long\")][\"fl\"][\"b\"]))\nnl = pd.DataFrame(rows)\nnl[\"long_below_short\"] = nl.slope_long < nl.slope_short\nnl[\"ratio_long_short\"] = nl.slope_long / nl.slope_short\nprint(nl.round(4))\nprint(\"Long below Short in\", int(nl.long_below_short.sum()), \"of 4; signed-rank p =\",\n      round(stats.wilcoxon(nl.slope_long - nl.slope_short).pvalue, 3))\n\"\"\", tags=[\"claim:neural-long-more-bias\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## Production epoch: speed\n\nSpeed is the mean Euclidean distance between successive 20 ms states in the production PC space,\nfrom Set to the shortest tp of that ts (claims file header). The Methods' \"divided by the\nduration separating Set and the time of Go\" is shown as a variant: that mean divided by the mean\ntp of the ts.\n\n### speed-vs-projection\n\n> Larger projections on the encoding axis at Set are followed by slower neural trajectories in\n> the production epoch (rho Short = -0.74, rho Long = -0.51).\n\nCriterion: per prior, Xu at t = ts against the speed of that ts, pooled over the 4 datasets (20\npoints); reproduced when both correlations are within tolerance (-0.74 ± 0.074, -0.51 ±\n0.051); partially when both are negative with p < 0.05 but one is outside, or when only one is\nwithin tolerance.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor ds in rsg.DATASETS:\n    G = geo[ds]\n    for p in rsg.PRIORS:\n        e = enc[(ds, p)]\n        ends_l = list(e[\"ends\"])\n        for ts in rsg.TS[p]:\n            rr, en, ntr, tmin = G[\"prod\"][ts]\n            Xp = rsg.project(G[\"pp\"], rr)\n            g = G[\"g\"][(G[\"g\"].prior == p) & (G[\"g\"].ts == ts)]\n            rows.append(dict(dataset=ds, prior=p, ts=ts, xu=e[\"X\"][ends_l.index(ts)] @ e[\"u\"],\n                             speed=rsg.mean_step(Xp), speed_per_tp=rsg.mean_step(Xp) / g.tp.mean(),\n                             mean_tp=g.tp.mean(), n=ntr, bins=len(en)))\nspd = pd.DataFrame(rows)\nprint(spd.round(3).to_string())\n\ndef corr_rows(xcol, ycol):\n    out = []\n    for p in rsg.PRIORS:\n        s = spd[spd.prior == p]\n        r, pv = stats.pearsonr(s[xcol], s[ycol])\n        out.append(dict(prior=p, set=\"pooled 20\", r=r, p=pv))\n        for ds in rsg.DATASETS:\n            q = s[s.dataset == ds]\n            r, pv = stats.pearsonr(q[xcol], q[ycol])\n            out.append(dict(prior=p, set=ds, r=r, p=pv))\n        z = s.groupby(\"dataset\")[[xcol, ycol]].transform(lambda c: (c - c.mean()) / c.std())\n        r, pv = stats.pearsonr(z[xcol], z[ycol])\n        out.append(dict(prior=p, set=\"pooled, z-scored per dataset\", r=r, p=pv))\n    return pd.DataFrame(out)\n\nprint(\"\\nXu at Set against speed\")\nprint(corr_rows(\"xu\", \"speed\").round(4))\nprint(\"\\nvariant: speed divided by mean tp\")\nprint(corr_rows(\"xu\", \"speed_per_tp\").round(4))\n\"\"\", tags=[\"claim:speed-vs-projection\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### initial-speed-biased\n\n> The initial speed of production trajectories (Set to Set + 400 ms) is biased toward the middle\n> of the prior; its dependence on ts is shallower than the unbiased profile proportional to 1/ts.\n\nCriterion: per dataset and prior, the mean step distance between Set and Set + 400 ms (trials with\ntp of at least 400 ms), projected in the production PC space; the slope of its regression on ts;\nthe slope of the unbiased profile speed(middle ts) x middle ts / ts. Reproduced when the measured\nslope is shallower (less negative) than the unbiased one in most of the 8 and a two-sided\nsigned-rank test of the difference has p < 0.05.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor ds in rsg.DATASETS:\n    G = geo[ds]\n    for p in rsg.PRIORS:\n        sp_ = []\n        for ts in rsg.TS[p]:\n            g = G[\"g\"][(G[\"g\"].prior == p) & (G[\"g\"].ts == ts) & (G[\"g\"].tp >= 400)]\n            rr, _ = rsg.aligned_rates(spikes, g.set_time.values, 0, 400)\n            sp_.append(rsg.mean_step(rsg.project(G[\"pp\"], rr)))\n        sp_ = np.array(sp_); tsv = np.array(rsg.TS[p], float)\n        unb = sp_[2] * tsv[2] / tsv\n        m_slope = np.polyfit(tsv, sp_, 1)[0]; u_slope = np.polyfit(tsv, unb, 1)[0]\n        rows.append(dict(dataset=ds, prior=p, speeds=np.round(sp_, 3), slope_measured=m_slope,\n                         slope_unbiased=u_slope, shallower=m_slope > u_slope))\nini = pd.DataFrame(rows)\nprint(ini.to_string())\nd = ini.slope_measured - ini.slope_unbiased\nprint(\"measured shallower than unbiased in\", int(ini.shallower.sum()), \"of 8; signed-rank p =\",\n      round(stats.wilcoxon(d).pvalue, 4), \"| median difference\", f\"{np.median(d):.2e}\")\n\"\"\", tags=[\"claim:initial-speed-biased\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### speed-predicts-tp\n\n> The speed of neural trajectories in the production epoch predicts the mean tp (rho Short =\n> -0.58, rho Long = -0.52).\n\nCriterion: per prior, the mean tp of each dataset and ts against the speed of that ts, pooled over\nthe 4 datasets (20 points); same rule as speed-vs-projection. Variant: trial-by-trial, within\neach prior, effector and direction, the speed of each trial's smoothed rates (projected in the\nproduction PC space, from Set to that trial's Go) against its tp, both z-scored within ts (the\nMethods' trial-by-trial analysis, \"Analysis of neural state variance\", uses z-scoring within ts;\nGPFA is not used for this variant).\n\"\"\")\n\ncode(r\"\"\"\nprint(\"mean tp against speed\")\nprint(corr_rows(\"mean_tp\", \"speed\").round(4))\nprint(\"\\nvariant: speed divided by mean tp\")\nprint(corr_rows(\"mean_tp\", \"speed_per_tp\").round(4))\n\nrows = []\nfor ds in rsg.DATASETS:\n    G = geo[ds]\n    for p in rsg.PRIORS:\n        g = G[\"g\"][G[\"g\"].prior == p]\n        sps = []\n        for _, tr_ in g.iterrows():\n            stop = int(np.floor(tr_.tp / rsg.BIN_MS) * rsg.BIN_MS)\n            c = rsg.bin_counts(spikes, [tr_.set_time], np.arange(0, stop + 1, rsg.BIN_MS))[0].T / 0.02\n            sps.append(rsg.mean_step(rsg.project(G[\"pp\"], rsg.smooth(c))))\n        g = g.assign(speed=sps)\n        z = g.groupby(\"ts\")[[\"speed\", \"tp\"]].transform(lambda c: (c - c.mean()) / c.std())\n        r, pv = stats.pearsonr(z.speed, z.tp)\n        rows.append(dict(dataset=ds, prior=p, n=len(g), r_trial=r, p=pv))\ntt_ = pd.DataFrame(rows)\nprint(\"\\nvariant: trial by trial, z-scored within ts\")\nprint(tt_.round(4))\n\"\"\", tags=[\"claim:speed-predicts-tp\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## Alternative mechanisms\n\n### alt-speed-unmodulated\n\n> Instantaneous speed of neural trajectories in the full neural space is not modulated during\n> the support of each prior.\n\nCriterion (absence, on the paper's test): per dataset and prior, the distance between successive\n20 ms states of the smoothed rates of all selected units over the support (with attrition),\nregressed on time; reproduced when a two-sided signed-rank test of the 4 slopes against zero has\np >= 0.05 for each prior. With 4 slopes the test cannot reach p < 0.05; the slopes and their\nbootstrap intervals over trials (200 resamples of trials within each ts) are the effect size.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(21)\n\ndef support_slope(c, tsv, ends, lo, hi):\n    use = tsv[:, None] >= ends[None, :]\n    n = use.sum(0)\n    r = rsg.smooth(np.einsum(\"tub,tb->bu\", c, use.astype(float)) / np.maximum(n, 1)[:, None] / 0.02)\n    sel = (ends >= lo) & (ends <= hi)\n    steps = np.linalg.norm(np.diff(r[sel], axis=0), axis=1)\n    tt = ends[sel][1:]\n    return np.polyfit(tt, steps, 1)[0], steps\n\nrows = []\nfor ds in rsg.DATASETS:\n    g = v[v.dataset == ds]\n    for p in rsg.PRIORS:\n        gp = g[g.prior == p]\n        lo, hi = rsg.TS[p][0], rsg.TS[p][-1]\n        edges = np.arange(0, hi + rsg.BIN_MS, rsg.BIN_MS)\n        c = rsg.bin_counts(spikes, gp.ready_time.values, edges)\n        tsv = gp.ts.values\n        slope, steps = support_slope(c, tsv, edges[1:], lo, hi)\n        groups = [np.where(tsv == t)[0] for t in rsg.TS[p]]\n        boots = []\n        for _ in range(200):\n            idx = np.concatenate([rng.choice(ix, len(ix)) for ix in groups])\n            boots.append(support_slope(c[idx], tsv[idx], edges[1:], lo, hi)[0])\n        rows.append(dict(dataset=ds, prior=p, slope_per_s=slope * 1000, ci_lo=np.percentile(boots, 2.5) * 1000,\n                         ci_hi=np.percentile(boots, 97.5) * 1000, mean_step=steps.mean(),\n                         step_range=f\"{steps.min():.2f}-{steps.max():.2f}\"))\nasp = pd.DataFrame(rows)\nprint(\"slopes of step distance (spikes/s per 20 ms step) on time, per s:\")\nprint(asp.round(3))\nfor p in rsg.PRIORS:\n    s = asp[asp.prior == p]\n    print(p, \"signed-rank p =\", round(stats.wilcoxon(s.slope_per_s).pvalue, 3), \"| slopes > 0:\",\n          int((s.slope_per_s > 0).sum()), \"of 4 | intervals excluding 0:\", int(((s.ci_lo > 0) | (s.ci_hi < 0)).sum()),\n          \"| mean slope relative to mean step, per s:\", round((s.slope_per_s / s.mean_step).mean(), 3))\n\"\"\", tags=[\"claim:alt-speed-unmodulated\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### alt-transient-parallel\n\n> In the first 200 ms after Set, trajectories for different ts run parallel; their distance to\n> the middle ts trajectory does not change.\n\nCriterion (absence, on the paper's test): PCA per dataset on Set to Set + 200 ms, both priors, at\nleast 75% of variance; per dataset and prior the distance from the shortest and the longest ts\ntrajectory to the middle one at each 20 ms bin, regressed on time; reproduced when two-sided\nsigned-rank tests of the 8 slopes against zero have p >= 0.05 for both.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor ds in rsg.DATASETS:\n    g = v[v.dataset == ds]\n    tr_rates = {}\n    for p in rsg.PRIORS:\n        for ts in rsg.TS[p]:\n            gg = g[(g.prior == p) & (g.ts == ts)]\n            tr_rates[(p, ts)], ends = rsg.aligned_rates(spikes, gg.set_time.values, 0, 200)\n    pt = rsg.pca(list(tr_rates.values()))\n    for p in rsg.PRIORS:\n        mid = rsg.project(pt, tr_rates[(p, rsg.TS[p][2])])\n        for which, ts in [(\"shortest\", rsg.TS[p][0]), (\"longest\", rsg.TS[p][-1])]:\n            dist = np.linalg.norm(rsg.project(pt, tr_rates[(p, ts)]) - mid, axis=1)\n            rows.append(dict(dataset=ds, prior=p, which=which, k=pt[\"k\"], slope_per_s=np.polyfit(ends, dist, 1)[0] * 1000,\n                             dist_first=dist[0], dist_last=dist[-1], dist_mean=dist.mean()))\natp = pd.DataFrame(rows)\nprint(atp.round(3))\nfor which in [\"shortest\", \"longest\"]:\n    s = atp[atp.which == which]\n    print(which, \"| signed-rank p =\", round(stats.wilcoxon(s.slope_per_s).pvalue, 4), \"| slopes < 0:\",\n          int((s.slope_per_s < 0).sum()), \"of 8 | median relative change over 200 ms:\",\n          round(np.median((s.dist_last - s.dist_first) / s.dist_mean), 3))\n\"\"\", tags=[\"claim:alt-transient-parallel\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### alt-threshold-monotonic\n\n> Aligned to the response, distances between trajectories for different ts decrease steadily up\n> to movement initiation, without the converging then diverging pattern a ts-dependent threshold\n> would produce.\n\nCriterion: PCA per dataset on Go - 800 ms to Go, both priors, keeping 60% of the variance (Figure\n5F legend); per dataset, prior and non-middle ts (32 curves) the distance to the middle ts\ntrajectory at each 20 ms bin and the time of its minimum. Reproduced when the median time of the\nminimum is in the last 40 ms before Go; partially when in the last 200 ms. A bin's time is its end\n(the last bin ends at Go). 75% of the variance is shown as a variant (the legend: \"results remained\nunchanged when more PCs were included\").\n\"\"\")\n\ncode(r\"\"\"\ndef threshold_minima(frac):\n    rows = []\n    for ds in rsg.DATASETS:\n        g = v[v.dataset == ds]\n        rr = {}\n        for p in rsg.PRIORS:\n            for ts in rsg.TS[p]:\n                gg = g[(g.prior == p) & (g.ts == ts)]\n                rr[(p, ts)], ends = rsg.aligned_rates(spikes, gg.go_time.values, -800, 0)\n        pt = rsg.pca(list(rr.values()), frac)\n        for p in rsg.PRIORS:\n            mid = rsg.project(pt, rr[(p, rsg.TS[p][2])])\n            for ts in rsg.TS[p]:\n                if ts == rsg.TS[p][2]:\n                    continue\n                dist = np.linalg.norm(rsg.project(pt, rr[(p, ts)]) - mid, axis=1)\n                rows.append(dict(dataset=ds, prior=p, ts=ts, k=pt[\"k\"], t_min=ends[np.argmin(dist)],\n                                 d_start=dist[0], d_min=dist.min(), d_end=dist[-1],\n                                 monotonic_frac=np.mean(np.diff(dist) <= 0)))\n    return pd.DataFrame(rows)\n\nthr60 = threshold_minima(0.60)\nprint(thr60.round(2).to_string())\nfor name, df in [(\"60%\", thr60), (\"75%\", threshold_minima(0.75))]:\n    print(name, \"| components\", sorted(df.k.unique()), \"| median time of minimum\", df.t_min.median(), \"ms\",\n          \"| in last 40 ms:\", int((df.t_min >= -20).sum()), \"of 32 | in last 200 ms:\", int((df.t_min >= -180).sum()),\n          \"| mean fraction of decreasing steps\", round(df.monotonic_frac.mean(), 3))\n\"\"\", tags=[\"claim:alt-threshold-monotonic\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## Claims not tested\n\n- rnn-curved-manifold, rnn-perturbation: the recurrent networks are the paper's simulations; no\n  network, weights or code are in the dandiset or named as public by the paper. Blocked,\n  data_missing.\n- monkey-g: the dandiset holds one session of monkey H only. Blocked, data_missing.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"total run time\", round(time.time() - T0), \"s; peak memory\",\n      round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2), \"GB\")\n\"\"\")\n\nmd(\"## Summary\\n\\n(filled after the run)\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/sohn-2019/reproduce_sohn_2019.ipynb\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; python $TMPDIR/make_nb1.py && date -u && time jupyter nbconvert --to notebook --execute reproduce_sohn_2019.ipynb --output $TMPDIR/nb1_out.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | tail -3
```

```
Sun Nov 15 12:59:16 UTC 2026
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.078s
user	0m0.067s
sys	0m0.013s
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; uv pip install nbconvert 2>&1 | tail -1; time jupyter nbconvert --to notebook --execute reproduce_sohn_2019.ipynb --output $TMPDIR/nb1_out.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | tail -30
```

```
+ webencodings==0.6.1
[NbConvertApp] Converting notebook reproduce_sohn_2019.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 266393 bytes to /tmp/claude-1001/nb1_out.ipynb

real	0m54.864s
user	0m49.320s
sys	0m0.589s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dump.py <<'EOF'
import nbformat,sys
nb=nbformat.read(sys.argv[1],4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    print(f"===== cell {i} {tags}")
    for o in c.get('outputs',[]):
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
        elif 'text/plain' in o.get('data',{}) and 'image/png' not in o['data']: print(o['data']['text/plain'][:3000])
EOF
source $TMPDIR/dev/bin/activate; python $TMPDIR/dump.py $TMPDIR/nb1_out.ipynb
```

```
===== cell 1 []
dandiset 000130 version 0.241017.1448

===== cell 3 ['sanity']
{'session_start': '2016-12-11 00:00:00-05:00', 'subject': 'Haydn', 'species': 'Macaca mulatta', 'description': 'Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains continuous segments of the full session on 2016-12-11 that can be used for training models for the Neural Latents Benchmark.'}
trials in the train file: 1160 | by NLB split: {'train': 748, 'val': 258, 'none': 154}
units: 54 | held out for NLB: 14
observation intervals identical for all units: True | observed 4808.9 s in 6 intervals
gaps between observation intervals (s): [0.09  0.138 0.105 0.072 0.072]
spike times sorted in every unit: True
spike time range (s): 0.003 to 4809.331

test file: trials 283 columns ['start_time', 'stop_time', 'go_time', 'split'] units 40 | segment length (s): [1.7]

===== cell 4 ['sanity']
completed (Set and Go present, no bad_time, tp > 0): 1025
completed and flagged is_outlier: 43
valid (completed, not outlier): 982
trials with Go and a bad_time (left out): 4
valid trials by split: {'train': 720, 'val': 246, 'none': 16}
[... 397 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_nb2.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Sohn et al. (2019) on DANDI:000130: single-trial GPFA\n\nPaper: Sohn H, Narain D, Meirhaeghe N, Jazayeri M (2019). Bayesian computation through cortical\nlatent dynamics. *Neuron* 103, 934-947. doi:10.1016/j.neuron.2019.06.012.\n\nDataset: [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version\n0.241017.1448, the version asked for in the prompt of this attempt and the dandiset's published\nversion. Claims: `claims/sohn-2019.yaml`, written from the accepted author manuscript\n(PMC6805134).\n\nThis notebook tests the two GPFA claims, gpfa-variance-inverted-u and gpfa-mean-sigmoid; the\nother claims are in `reproduce_sohn_2019.ipynb`. The paper ran GPFA on \"high-yield sessions\n(N=48 for monkey H ...)\" (Results, \"The curved manifold hypothesis captures the variance\"). This\nsession has 48 units that pass the unit rule, which suggests it is that session of H; nothing in\nthe files says so.\n\n| Claim | Tested here |\n|---|---|\n| gpfa-variance-inverted-u | yes |\n| gpfa-mean-sigmoid | yes |\n\nGPFA is the implementation of Yu et al. (2009) in Elephant (`elephant.gpfa.GPFA`), with its\ndefaults (at most 500 EM iterations) and 20 ms bins. The paper used its own MATLAB code (\"custom\nMATLAB code\", STAR Methods), which is not public.\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"2\")\nimport time\nimport resource\nimport logging\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport quantities as pq\nimport neo\nfrom elephant.gpfa import GPFA\nfrom sklearn.model_selection import KFold\nimport rsg\n\nwarnings.filterwarnings(\"ignore\")\nlogging.getLogger(\"elephant\").setLevel(logging.ERROR)\nlogging.disable(logging.WARNING)\npd.set_option(\"display.width\", 200)\nT0 = time.time()\nprint(\"dandiset\", rsg.DANDISET_ID, \"version\", rsg.VERSION)\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nsess = rsg.load_session()\ntr = sess[\"trials\"]\nv = tr[tr.valid].copy()\nunit_mask, unit_rate = rsg.select_units(sess)\nspikes = [s for s, k in zip(sess[\"spikes\"], unit_mask) if k]\nprint(sess[\"meta\"][\"subject\"], sess[\"meta\"][\"session_start\"])\nprint(\"trials\", len(tr), \"| valid (completed, not is_outlier)\", len(v))\nprint(\"units\", len(unit_mask), \"| selected (>= 1 spike/s, >= 5 trials in each of 40 conditions)\", int(unit_mask.sum()))\nprint(\"valid trials per dataset and prior:\")\nprint(v.groupby([\"dataset\", \"prior\"]).size().unstack())\nd = (v.set_time - v.ready_time) * 1000\nprint(\"Set - Ready (ms): min\", round(d.min(), 1), \"max\", round(d.max(), 1),\n      \"| largest |(Set - Ready) - ts|\", round((d - v.ts).abs().max(), 1), \"ms\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## GPFA per dataset\n\nCriterion (gpfa-variance-inverted-u): GPFA with 20 ms bins per dataset on single trials from\nReady to Set, both priors, selected units; latent dimensionality chosen by 3-fold cross-validated\nlog-likelihood from 4 and 8; orthonormalised latents. Each trial is cut at the last whole 20 ms bin\nbefore its Set. Folds are formed over trials with a fixed seed (a standard choice).\n\nThe trial-averaged latent trajectory of a prior averages, in each bin, the trials that reach that\nbin (attrition, \"firing rate at time t was computed from spikes in all trials in which Set\noccurred after t\", Methods); u is computed from it as in `rsg.encoding_axis`, between the\nprior's shortest and longest ts.\n\"\"\")\n\ncode(r\"\"\"\ndef trial_spiketrains(g):\n    out, nb = [], []\n    for _, r in g.iterrows():\n        n = int(np.floor((r.set_time - r.ready_time) * 1000 / rsg.BIN_MS + 1e-6))\n        T = n * rsg.BIN_MS / 1000.0\n        out.append([neo.SpikeTrain((s[(s >= r.ready_time) & (s < r.ready_time + T)] - r.ready_time) * pq.s,\n                                   t_start=0 * pq.s, t_stop=T * pq.s) for s in spikes])\n        nb.append(n)\n    return out, np.array(nb)\n\ngp_res = {}\ncv_rows = []\nfor i_ds, ds in enumerate(rsg.DATASETS):\n    t1 = time.time()\n    g = v[v.dataset == ds]\n    sts, nbins = trial_spiketrains(g)\n    kf = KFold(3, shuffle=True, random_state=100 + i_ds)\n    ll = {4: 0.0, 8: 0.0}\n    for k_tr, k_te in kf.split(sts):\n        for xd in (4, 8):\n            np.random.seed(1000 + i_ds)\n            m = GPFA(bin_size=rsg.BIN_MS * pq.ms, x_dim=xd, verbose=False)\n            m.fit([sts[j] for j in k_tr])\n            ll[xd] += m.score([sts[j] for j in k_te])\n    xd = max(ll, key=ll.get)\n    np.random.seed(2000 + i_ds)\n    m = GPFA(bin_size=rsg.BIN_MS * pq.ms, x_dim=xd, verbose=False)\n    lat = m.fit_transform(sts, returned_data=[\"latent_variable_orth\"])\n    lat = [np.asarray(x) for x in lat]\n    assert all(x.shape[1] == n for x, n in zip(lat, nbins))\n    gp_res[ds] = dict(g=g, lat=lat, nbins=nbins, x_dim=xd, n_iter=len(m.fit_info[\"log_likelihoods\"]))\n    cv_rows.append(dict(dataset=ds, trials=len(sts), cv_ll_4=ll[4], cv_ll_8=ll[8], chosen=xd,\n                        em_iterations=gp_res[ds][\"n_iter\"], seconds=round(time.time() - t1)))\n    print(cv_rows[-1])\ncvt = pd.DataFrame(cv_rows)\nprint(cvt)\n\"\"\")\n\ncode(r\"\"\"\nproj_rows = []\nfor ds in rsg.DATASETS:\n    R = gp_res[ds]\n    g, lat, nbins = R[\"g\"], R[\"lat\"], R[\"nbins\"]\n    for p in rsg.PRIORS:\n        idx = np.where(g.prior.values == p)[0]\n        nmax = nbins[idx].max()\n        S = np.zeros((nmax, R[\"x_dim\"])); N = np.zeros(nmax)\n        for j in idx:\n            S[:nbins[j]] += lat[j].T; N[:nbins[j]] += 1\n        avg = S / N[:, None]\n        ends = np.arange(1, nmax + 1) * rsg.BIN_MS\n        lo, hi = rsg.TS[p][0], rsg.TS[p][-1]\n        u, _ = rsg.encoding_axis(avg, ends, lo, hi)\n        for j in idx:\n            proj_rows.append(dict(dataset=ds, prior=p, ts=int(g.ts.values[j]), xu=lat[j][:, -1] @ u,\n                                  n_bins=int(nbins[j]), n_at_hi=int(N[list(ends).index(hi)])))\nproj = pd.DataFrame(proj_rows)\nproj[\"xu_z\"] = proj.groupby([\"dataset\", \"prior\"]).xu.transform(lambda x: (x - x.mean()) / x.std())\nprint(\"single-trial projections:\", len(proj), \"| xu range\", round(proj.xu.min(), 3), \"to\", round(proj.xu.max(), 3))\nprint(\"trials averaged in the last bin of the support (ts_max):\",\n      proj.groupby([\"dataset\", \"prior\"]).n_at_hi.first().to_dict())\n\"\"\")\n\nmd(r\"\"\"\n### gpfa-variance-inverted-u\n\n> The variance across single trials of the GPFA neural state at Set projected on the encoding\n> axis has an inverted-U profile over ts, lower at the extremes of each prior.\n\nCriterion: Xu z-scored over the prior's trials; the variance at each ts; the quadratic\ncoefficient of a polynomial fit of variance on ts; reproduced when a one-tailed signed-rank test\n(coefficient below zero) over the 8 dataset-priors has p < 0.05.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (ds, p), q in proj.groupby([\"dataset\", \"prior\"]):\n    var = q.groupby(\"ts\").xu_z.var().reindex(rsg.TS[p])\n    coef = np.polyfit(np.array(rsg.TS[p], float), var.values, 2)[0]\n    rows.append(dict(dataset=ds, prior=p, var=np.round(var.values, 3), n=q.groupby(\"ts\").size().reindex(rsg.TS[p]).tolist(),\n                     quad_coef=coef, inverted_u=coef < 0,\n                     extremes_below_middle=(var.values[[0, 4]].mean() < var.values[1:4].mean())))\nvq = pd.DataFrame(rows)\nprint(vq.to_string())\nw = stats.wilcoxon(vq.quad_coef, alternative=\"less\")\nprint(\"quadratic coefficient < 0 in\", int(vq.inverted_u.sum()), \"of 8; one-tailed signed-rank p =\", round(w.pvalue, 4))\nprint(\"mean variance at the extremes below the middle three in\", int(vq.extremes_below_middle.sum()), \"of 8\")\n\"\"\", tags=[\"claim:gpfa-variance-inverted-u\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### gpfa-mean-sigmoid\n\n> The mean of the single-trial GPFA projections is sigmoidal and has a higher slope for the Short\n> prior.\n\nCriterion: with the projections above, not z-scored; the mean Xu at each ts; increments as in\nbeh-sigmoid-increments, compared by a two-sided signed-rank test over the 8 dataset-priors\n(sigmoidal when middle exceeds extreme with p < 0.05); the slope of mean Xu on ts per dataset and\nprior (higher for Short in all 4 datasets). Reproduced when both parts hold; partially when one\ndoes.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (ds, p), q in proj.groupby([\"dataset\", \"prior\"]):\n    m = q.groupby(\"ts\").xu.mean().reindex(rsg.TS[p]).values\n    ext, mid = rsg.increments(m)\n    rows.append(dict(dataset=ds, prior=p, mean_xu=np.round(m, 3), extreme=ext, middle=mid,\n                     slope_per_s=np.polyfit(np.array(rsg.TS[p], float), m, 1)[0] * 1000))\nmq = pd.DataFrame(rows)\nprint(mq.to_string())\nw = stats.wilcoxon(mq.middle, mq.extreme)\nprint(\"middle > extreme in\", int((mq.middle > mq.extreme).sum()), \"of 8; two-sided signed-rank p =\", round(w.pvalue, 4))\nsl = mq.pivot(index=\"dataset\", columns=\"prior\", values=\"slope_per_s\")\nsl[\"short_higher\"] = sl.Short > sl.Long\nprint(sl.round(4))\nprint(\"Short slope higher in\", int(sl.short_higher.sum()), \"of 4; one-tailed signed-rank p =\",\n      round(stats.wilcoxon(sl.Short - sl.Long, alternative=\"greater\").pvalue, 4))\n\"\"\", tags=[\"claim:gpfa-mean-sigmoid\"])\n\nmd(\"**Result: ...**\")\n\ncode(r\"\"\"\nprint(\"total run time\", round(time.time() - T0), \"s; peak memory\",\n      round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2), \"GB\")\n\"\"\")\n\nmd(\"## Summary\\n\\n(filled after the run)\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/sohn-2019/gpfa_sohn_2019.ipynb\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; python $TMPDIR/make_nb2.py && sed -e 's/verbose=False)/verbose=False, em_max_iters=15)/g' gpfa_sohn_2019.ipynb > $TMPDIR/gp_test.ipynb && cp rsg.py $TMPDIR/ && cd $TMPDIR && time jupyter nbconvert --to notebook --execute gp_test.ipynb --output $TMPDIR/gp_test_out.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | tail -2; python $TMPDIR/dump.py $TMPDIR/gp_test_out.ipynb | tail -60
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 25990 bytes to /tmp/claude-1001/gp_test_out.ipynb

real	1m28.395s
user	2m10.795s
sys	0m0.721s
Fitting GPFA model...

Initializing parameters using factor analysis...

Fitting GPFA model...

Initializing parameters using factor analysis...

Fitting GPFA model...

Initializing parameters using factor analysis...

Fitting GPFA model...

[... 47 more lines not kept]
```

**Agent**

GPFA notebook works on a 15-iteration test. Running it in full now (estimated ~18 min) to get the numbers for the conclusions.

**Agent calls Bash**

```bash
cd entries/sohn-2019; source $TMPDIR/dev/bin/activate; date -u; time jupyter nbconvert --to notebook --execute gpfa_sohn_2019.ipynb --output $TMPDIR/nb2_out.ipynb --ExecutePreprocessor.timeout=4000 2>&1 | tail -1; python $TMPDIR/dump.py $TMPDIR/nb2_out.ipynb | grep -v "^Initializing\|^Fitting\|^$" | tail -50
```

```
Sun Nov 15 13:03:15 UTC 2026
[NbConvertApp] Writing 25941 bytes to /tmp/claude-1001/nb2_out.ipynb

real	10m9.291s
user	27m55.065s
sys	0m2.973s
Eye Left     155    105
Eye Right    147    128
Hand Left     88    134
Hand Right   112    113
Set - Ready (ms): min 466.5 max 1200.5 | largest |(Set - Ready) - ts| 23.5 ms
===== cell 5 []
{'dataset': 'Eye Left', 'trials': 260, 'cv_ll_4': np.float64(-164187.10285920056), 'cv_ll_8': np.float64(-163618.32957105397), 'chosen': 8, 'em_iterations': 500, 'seconds': 171}
{'dataset': 'Eye Right', 'trials': 275, 'cv_ll_4': np.float64(-173156.49228412766), 'cv_ll_8': np.float64(-172503.25879582213), 'chosen': 8, 'em_iterations': 500, 'seconds': 173}
{'dataset': 'Hand Left', 'trials': 222, 'cv_ll_4': np.float64(-115222.78209391938), 'cv_ll_8': np.float64(-114550.40197277072), 'chosen': 8, 'em_iterations': 500, 'seconds': 126}
{'dataset': 'Hand Right', 'trials': 225, 'cv_ll_4': np.float64(-124463.59965064633), 'cv_ll_8': np.float64(-123760.44526415704), 'chosen': 8, 'em_iterations': 500, 'seconds': 132}
      dataset  trials        cv_ll_4        cv_ll_8  chosen  em_iterations  seconds
0    Eye Left     260 -164187.102859 -163618.329571       8            500      171
1   Eye Right     275 -173156.492284 -172503.258796       8            500      173
2   Hand Left     222 -115222.782094 -114550.401973       8            500      126
[... 36 more lines not kept]
```

**Agent**

GPFA run took 10 min. Outcomes are now clear for all tested claims. Writing the conclusions and summaries into the notebooks.

**Agent calls Bash**

```bash
cd $TMPDIR; date -u; grep -n 'Result: \.\.\.\|filled after' make_nb1.py make_nb2.py | cut -c1-80; grep -n "prior and iti agree" make_nb1.py
```

```
Sun Nov 15 13:13:56 UTC 2026
make_nb1.py:227:**Result: ...** (filled after the run)
make_nb1.py:251:md("**Result: ...**")
make_nb1.py:278:md("**Result: ...**")
make_nb1.py:299:md("**Result: ...**")
make_nb1.py:341:md("**Result: ...**")
make_nb1.py:439:md("**Result: ...**")
make_nb1.py:491:md("**Result: ...**")
make_nb1.py:558:md("**Result: ...**")
make_nb1.py:624:md("**Result: ...**")
make_nb1.py:653:md("**Result: ...**")
make_nb1.py:699:md("**Result: ...**")
make_nb1.py:723:md("**Result: ...**")
make_nb1.py:782:md("**Result: ...**")
make_nb1.py:819:md("**Result: ...**")
make_nb1.py:860:md("**Result: ...**")
make_nb1.py:917:md("**Result: ...**")
make_nb1.py:956:md("**Result: ...**")
make_nb1.py:1003:md("**Result: ...**")
make_nb1.py:1019:md("## Summary\n\n(filled after the run)")
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > fill.py <<'PYEOF'
import re
s = open('make_nb1.py').read()
s = s.replace('''print("prior and iti agree (Short 500, Long 1220):",
      bool(((v.prior == "Short") == (v.iti == 500)).all()))''', '''print("iti as the column description states (Short 500, Long 1220):",
      bool(((v.prior == "Short") == (v.iti == 500)).all()),
      "| as the Methods state (Short 1220, Long 500):", bool(((v.prior == "Short") == (v.iti == 1220)).all()))''')
R1 = [
"""**Result: not reproduced.** With an intercept, 6 of 8 slopes lie between 0 and 1 (0.502 to
0.903), and both Eye Short slopes do not (1.011 and 1.107); 5 of 8 intervals exclude 0 and 1.
Through the origin, 2 of 8 slopes lie between 0 and 1. The slopes are clearly below 1 for the
Hand datasets (0.502 to 0.861) and near 1 for the Eye datasets (0.845 to 1.107).""",
"""**Result: not reproduced.** At ts = 800 ms the median bias is +27.8 ms for Short and +47.6 ms
for Long, both positive, and the rank-sum test gives p = 0.068 (92 Short, 107 Long trials). Long
tp is the longer of the two in 3 of 4 datasets by the mean; only Hand Right differs at p < 0.05
(p = 0.001), and in Hand Left the medians are -61.6 (Short) and -2.8 ms (Long).""",
"""**Result: reproduced.** The middle increment exceeds the extreme one in 7 of 8 conditions
(median difference 31.3 ms), two-sided signed-rank p = 0.0156; the exception is Hand Left Short.""",
"""**Result: reproduced, on the assumption that the regression has an intercept.** The Long slope
is below the Short slope in 4 of 4 datasets (0.845 against 1.011, 0.903 against 1.107, 0.502
against 0.612, 0.612 against 0.861). Through the origin it is in 3 of 4, which would be partially
reproduced.""",
"""**Result: partially reproduced.** The predicted SD of tp correlates positively with the
observed SD in all 4 datasets (r = 0.28 to 0.91), but the bias R2 reaches 0.8 in 2 of 4: 0.978
(Hand Left) and 0.865 (Hand Right) against 0.671 (Eye Left) and 0.128 (Eye Right). The squared
correlation gives the same split (0.679, 0.135, 0.978, 0.868). In the Eye datasets the fitted
measurement noise is small (wm = 0.025 and 0.014, against 0.117 and 0.074 for Hand), so the model
predicts little bias.""",
"""**Result: not reproduced.** 38 of 48 units (79.2%, 95% interval 65.0 to 89.5%) are
prior-dependent and 24 of 48 (50.0%, 35.2 to 64.8%) are ts-dependent, against 65 ± 6.5% and
27 ± 2.7%; no fit failed. Both fractions are above the paper's, and the interval of the ts
fraction excludes 27%. With all 54 units the fractions are 75.9% and 48.1%; without attrition
60.4% and 43.8%.""",
"""**Result: reproduced.** The mean RMS difference between priors at ts = 800 ms is largest in the
480 to 640 ms bin (6.88 spikes/s), above the 95th percentile of the shuffled maximum (3.13
spikes/s). Seven bins, from 160 to 1280 ms after Ready, exceed that threshold, so the difference
extends beyond the support of the prior; the two bins of the support are the 1st and 4th largest
(6.88 and 4.87 spikes/s).""",
"""**Result: not reproduced.** 0 of 8 values fall in their ranges: 2 components reach 75% of the
variance in the estimation epoch of every dataset (3 to 4 expected) and 2, 2, 4 and 4 in the
production epoch (5 to 11 expected). The first 3 components explain 0.868 to 0.907 of the
estimation-epoch variance. With z-scored rates the counts are 3 to 4 and 5 to 8, inside the
ranges; that is a variant the claim does not use.""",
"""**Result: reproduced.** Under reading (a), Hand Left, R2 = 0.9957 (Short) and 0.9774 (Long);
under reading (b), the mean of 4 datasets, 0.9583 and 0.9823; both readings are within tolerance.
Random axes in the same 2-dimensional PC space give high R2 as well (median 0.716 to 0.987 per
dataset and prior), and the fraction of random axes at least as good as u ranges from 0.018 to
0.419, so the fit is not specific to u in this low-dimensional space.""",
"""**Result: partially reproduced.** The Bayesian RMSE is lower than the linear one in 4 of 4
datasets for Short and 3 of 4 for Long; in Hand Left Long it is higher (0.583 against 0.481). The
weighted RMSE gives the same counts.""",
"""**Result: reproduced.** By the paper's test the Bayesian model is not better than the linear one
in the Short In Long period: signed-rank p = 0.125 with the single axis and 0.25 with the averaged
axis. The test cannot reach p < 0.05 with 4 datasets. The Bayesian RMSE is still lower in 4 of 4
datasets with the single axis (mean difference -0.096, against -0.260 for the Short prior), so
the data show a smaller version of the Short-prior effect, not its absence.""",
"""**Result: partially reproduced.** The Long slope is below the Short slope in 3 of 4 datasets
(ratios 0.54, 0.62 and 0.36); in Hand Right they are nearly equal (0.0486 against 0.0470).""",
"""**Result: partially reproduced.** Larger projections at Set go with slower trajectories in both
priors: pooled r = -0.921 (Short) and -0.840 (Long), both p < 1e-4, stronger than the paper's
-0.74 and -0.51 and outside the tolerance. Within datasets r ranges from -0.84 to -0.99, except
Hand Left Long (-0.25). With speed divided by the mean tp, r = -0.932 and -0.947.""",
"""**Result: not reproduced.** The measured slope is shallower than the unbiased one in 7 of 8
dataset-priors, but the signed-rank test gives p = 0.0547, above 0.05.""",
"""**Result: partially reproduced.** Pooled over datasets, r = -0.608 for Short (within -0.58 ±
0.058) and -0.631 for Long (outside -0.52 ± 0.052), both p < 0.005. With speed divided by the mean
tp, r = -0.815 and -0.830. Trial by trial, z-scored within ts, r is negative in all 8
dataset-priors (-0.05 to -0.42) and p < 0.05 in the 4 Eye ones.""",
"""**Result: reproduced.** By the paper's test the slopes do not differ from zero: p = 0.25 (Short)
and 0.125 (Long); with 4 datasets the test cannot reach p < 0.05. The slopes are positive in 3 of
4 (Short) and 4 of 4 (Long), and the bootstrap intervals exclude zero in 2 and 3, so the step
distance tends to grow over the support. Part of that growth can come from noise, as the number of
trials averaged falls about five-fold across the support.""",
"""**Result: reproduced.** By the paper's test neither set of slopes differs from zero: p = 0.195
for the shortest ts and 1.0 for the longest. The distance of the shortest ts trajectory from the
middle one still grows in 6 of 8 dataset-priors (median +49% of its mean over 200 ms), while that
of the longest does not change (median -5%).""",
"""**Result: not reproduced.** With 60% of the variance (1 to 3 components) the median time of the
minimum distance is 250 ms before Go; 4 of 32 minima are in the last 40 ms and 12 in the last 200
ms. With 75% (2 to 5 components) the median is 160 ms before Go, which would be partially
reproduced. About 57% of the 20 ms steps decrease the distance.""",
]
SUM1 = """## Summary

| Claim | Outcome |
|---|---|
| beh-slopes | not reproduced (2 Eye Short slopes above 1) |
| beh-overlap-prior | not reproduced (both biases positive, p = 0.068) |
| beh-sigmoid-increments | reproduced (7 of 8, p = 0.0156) |
| beh-long-more-bias | reproduced (4 of 4), assuming an intercept |
| beh-bayes-model | partially reproduced (bias R2 >= 0.8 in 2 of 4) |
| glm-prior-ts | not reproduced (79.2% and 50.0%) |
| dfr-overlap-support | reproduced |
| pca-dimensionality | not reproduced (0 of 8; 2 and 2 to 4 components) |
| encoding-r2 | reproduced (0.9957 and 0.9774, Hand Left) |
| encoding-bayes-beats-linear | partially reproduced (Short 4 of 4, Long 3 of 4) |
| short-in-long-control | reproduced (p = 0.125) |
| neural-long-more-bias | partially reproduced (3 of 4) |
| speed-vs-projection | partially reproduced (r = -0.92 and -0.84) |
| initial-speed-biased | not reproduced (7 of 8, p = 0.0547) |
| speed-predicts-tp | partially reproduced (r = -0.61 and -0.63) |
| alt-speed-unmodulated | reproduced (p = 0.25 and 0.125) |
| alt-transient-parallel | reproduced (p = 0.195 and 1.0) |
| alt-threshold-monotonic | not reproduced (median minimum 250 ms before Go) |
| gpfa-variance-inverted-u, gpfa-mean-sigmoid | see `gpfa_sohn_2019.ipynb` |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked, data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's:

- One session of monkey H (48 selected units, 982 valid trials, 4 datasets), where the paper uses
  17 sessions of H and 12 of G (8 datasets). The paper's PCA, GLM fractions and Bayesian fits pool
  sessions (Methods); here everything comes from one session, so the population has 48 units.
- Rates are not normalised and the kernel is truncated at the edges of each window (claims file
  and `rsg.py`).
- The behavioural regression is fitted with an intercept; the Methods write "tp = β ts + ε".

What was found about the dataset:

- The `iti` column's description gives 500 ms for Short and 1220 ms for Long; the data hold 1220
  ms for Short and 500 ms for Long, as the Methods state.
- `tp` is longer than Go - Set in every completed trial, by 0.1 to 153.3 ms (median 17.9 ms); the
  files do not say how `tp` was measured.
- The test file holds 283 NLB test segments of 1.7 s with no Ready, Set, ts, tp or condition, and
  40 of the 54 units; those trials cannot enter any analysis here.
- The dandiset holds one of the paper's 29 sessions; monkey G and the networks are not in it. The
  units carry no single- or multi-unit label and no electrode, and the electrodes have no
  positions.
- Event times and spikes share a clock: target direction is decoded at 0.62 to 0.75 from windows
  around Go and at chance (0.47 to 0.52) when the windows are shifted by 10 s.
"""
for r in R1:
    i = s.index('md("**Result: ...**")') if 'md("**Result: ...**")' in s else None
    j = s.index('**Result: ...** (filled after the run)') if '**Result: ...** (filled after the run)' in s else None
    if j is not None:
        s = s.replace('**Result: ...** (filled after the run)', r, 1)
    else:
        s = s.replace('md("**Result: ...**")', 'md(r"""\n' + r + '\n""")', 1)
assert '**Result: ...**' not in s
s = s.replace('md("## Summary\\n\\n(filled after the run)")', 'md(r"""\n' + SUM1 + '\n""")')
assert 'filled after' not in s
open('make_nb1.py', 'w').write(s)

s = open('make_nb2.py').read()
R2 = [
"""**Result: not reproduced.** The quadratic coefficient is negative in 5 of 8 dataset-priors and
the one-tailed signed-rank test gives p = 0.0742, above 0.05. The mean variance at the two
extreme ts is below that of the middle three in 5 of 8.""",
"""**Result: reproduced.** The middle increment of the mean projection exceeds the extreme one in 7
of 8 dataset-priors (two-sided signed-rank p = 0.0156), and the slope of the mean projection on ts
is higher for Short in 4 of 4 datasets (one-tailed signed-rank p = 0.0625, the smallest possible
with 4).""",
]
SUM2 = """## Summary

| Claim | Outcome |
|---|---|
| gpfa-variance-inverted-u | not reproduced (5 of 8 negative, p = 0.0742) |
| gpfa-mean-sigmoid | reproduced (7 of 8, p = 0.0156; Short higher in 4 of 4) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's: GPFA is Elephant's implementation, not the paper's
MATLAB code; cross-validation chose 8 latent dimensions in all 4 datasets. The data are the 48
selected units of the one session in the dandiset, with about 220 to 275 trials per dataset.
"""
for r in R2:
    s = s.replace('md("**Result: ...**")', 'md(r"""\n' + r + '\n""")', 1)
s = s.replace('md("## Summary\\n\\n(filled after the run)")', 'md(r"""\n' + SUM2 + '\n""")')
assert 'Result: ...' not in s and 'filled after' not in s
open('make_nb2.py', 'w').write(s)
PYEOF
python fill.py && source dev/bin/activate && python make_nb1.py && python make_nb2.py && ls -la entries/sohn-2019
```

```
total 128
drwxr-xr-x   4 runner runner  4096 Nov 15 13:01 .
drwxr-xr-x 302 runner runner 12288 Nov 15 12:51 ..
drwxr-xr-x   3 runner runner  4096 Nov 15 12:52 .claude
drwxr-xr-x   2 runner runner  4096 Nov 15 12:53 __pycache__
-rw-r--r--   1 runner runner 13817 Nov 15 13:14 gpfa_sohn_2019.ipynb
-rw-r--r--   1 runner runner 71009 Nov 15 13:14 reproduce_sohn_2019.ipynb
-rw-r--r--   1 runner runner 13147 Nov 15 12:53 rsg.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sohn-2019; find .claude -type f | head; ls -la .claude
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Nov 15 12:52 .
drwxr-xr-x 4 runner runner 4096 Nov 15 13:01 ..
drwx------ 2 runner runner 4096 Nov 15 12:52 .cc-writes
```

**Agent**

Now the entry files.

**Agent calls Bash**

```bash
cd entries/sohn-2019; rm -rf __pycache__; rmdir .claude/.cc-writes .claude 2>&1; cat > requirements.in <<'EOF'
dandi
elephant
h5py
matplotlib
neo
numpy
pandas
pynwb
quantities
remfile
scikit-learn
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: sohn-2019
type: reproduction
title: Bayesian computation through cortical latent dynamics (Sohn et al. 2019)
description: Tests the findings of Sohn, Narain, Meirhaeghe and Jazayeri (2019) on dandiset 000130,
  which holds one session of monkey H in the Ready-Set-Go task with two priors of the sample
  interval, 54 units of dorsomedial frontal cortex. It tests the behaviour and the Bayesian observer
  model, single-unit modulation by prior and elapsed time, the curved population trajectories and
  their encoding axis, the speed of production-epoch trajectories, the three alternative mechanisms,
  and the single-trial GPFA analysis. Monkey G and the recurrent networks are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_sohn_2019.ipynb
  title: Reproducing Sohn et al. (2019) from dandiset 000130
  runtime_minutes: 2
- path: gpfa_sohn_2019.ipynb
  title: Single-trial GPFA analysis of Sohn et al. (2019) on dandiset 000130
  runtime_minutes: 11
helpers:
- rsg.py
related:
- id: dandi:000130/0.241017.1448
  relation: uses_data
- id: doi:10.1016/j.neuron.2019.06.012
  relation: reproduces
EOF
cd ../..; python tools/entry.py lock entries/sohn-2019 2>&1 | tail -5; date -u
```

```
wrote sohn-2019/requirements.lock.txt (Python 3.13, with hashes)
Sun Nov 15 13:14:54 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/sohn-2019/README.md",
 "content": "# Sohn, Narain, Meirhaeghe & Jazayeri (2019) from dandiset 000130\n\nTests the findings of [Sohn et al. (2019)](https://doi.org/10.1016/j.neuron.2019.06.012) that can be\ntested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), which holds one\nsession of monkey H (2016-12-11) in the Ready-Set-Go task with two priors of the sample interval:\n54 units of dorsomedial frontal cortex and 1160 trials, prepared for the Neural Latents Benchmark.\nThe paper analyses 29 sessions of two monkeys; monkey G and the paper's recurrent networks are not\nin the dandiset.\n\n| Claim | Outcome |\n|---|---|\n| Regression slopes of tp on ts lie between 0 and 1 | Not reproduced |\n| Biases in opposite directions at the overlapping ts | Not reproduced |\n| tp increments smaller at the extremes of the prior | Reproduced |\n| Larger biases (smaller slopes) for the Long prior | Reproduced, on an assumption |\n| Bayesian observer captures bias and variance | Partially reproduced |\n| GLM: 65% prior-dependent and 27% ts-dependent units | Not reproduced |\n| Prior difference at ts = 800 largest in the support | Reproduced |\n| 3 to 4 and 5 to 10 PCs explain 75% of the variance | Not reproduced |\n| Projections on the encoding axis match the Bayesian estimate (R2) | Reproduced |\n| Bayesian model better than linear for the projections | Partially reproduced |\n| No sigmoidal representation in \"Short In Long\" | Reproduced |\n| Smaller neural slope for the Long prior | Partially reproduced |\n| Projection at Set predicts production speed | Partially reproduced |\n| Initial speed biased toward the middle of the prior | Not reproduced |\n| Production speed predicts mean tp | Partially reproduced |\n| Speed unmodulated during the support (H1) | Reproduced |\n| Parallel trajectories after Set (H2) | Reproduced |\n| Distances fall steadily to Go (H3) | Not reproduced |\n| Inverted-U variance of single-trial GPFA projections | Not reproduced |\n| Sigmoidal mean of single-trial GPFA projections | Reproduced |\n| Recurrent network claims (two) and monkey G | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nEvery analysis here uses one session with 48 selected units, where the paper pools 17 sessions\nof monkey H and 12 of monkey G. The attempt record, with the reasons and the differences from the\npaper's method, is [`attempts/sohn-2019-02.yaml`](../../attempts/sohn-2019-02.yaml).\n\n- `reproduce_sohn_2019.ipynb`: behaviour, the Bayesian model, the GLM, PCA, encoding axis, speed\n  and the alternative mechanisms. It takes about a minute.\n- `gpfa_sohn_2019.ipynb`: the single-trial GPFA analysis (Elephant's GPFA). It takes about ten\n  minutes.\n- `rsg.py`: loading the files, unit and trial selection, rates, PCA, the encoding axis and the\n  Bayesian observer model. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/sohn-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -n 196,215p attempts/fouke-2025-01.yaml; grep -n "methods_unavailable" -A6 attempts/*.yaml | head -20; python -c "
import json;d=json.load(open('schemas/attempt.schema.json'));p=d['properties'];print(json.dumps(p['findings'],indent=0)[:1500]);print(json.dumps(p['provenance'],indent=0)[:1500])"
```

```
- The paper shows this with representative traces and a bout analysis whose bout files are not
    in the dandiset; the measure was chosen here before the analysis.
- claim: fig1cef-representative-values
  outcome: blocked
  blocked_by: metadata_insufficient
  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
    dandiset gives no mapping from those folders to its subjects, nor the original file names.
- claim: fig2d-shared-architecture
  outcome: blocked
  blocked_by: data_missing
  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
    notebooks only, and no other dandiset of this lab or paper was found on the archive.
- claim: fig2g-dsi-similar
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2h-fewer-motion-responsive
  outcome: blocked
[... 142 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/sohn-2019-02.yaml",
 "content": "schema_version: 3\nid: sohn-2019-02\ndatasets:\n- archive: dandi\n  id: \"000130\"\n  version: 0.241017.1448\n  doi: 10.48324/dandi.000130/0.241017.1448\n  relation: primary\npaper: doi:10.1016/j.neuron.2019.06.012\ndate: 2026-11-15\nentry: sohn-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43715053400\noutcomes:\n- claim: beh-slopes\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-slopes\n  notes: With an intercept, 6 of 8 slopes lie between 0 and 1 and 5 of 8 95% intervals exclude 0\n    and 1. The two Eye Short slopes are 1.011 (0.896 to 1.126) and 1.107 (1.009 to 1.204). The\n    Hand slopes are 0.502 to 0.861 and the Eye Long slopes 0.845 and 0.903. Through the origin, 2\n    of 8 slopes lie between 0 and 1. Both readings give not reproduced.\n  deviations:\n  - One session of monkey H (4 conditions per prior), where the paper reports slopes over 17\n    sessions of H and 12 of G.\n  - The Methods write the regression as \"tp = β ts + ε\" (STAR Methods, Model free analysis of\n    behavior). The fit with an intercept is the main reading, as a slope below 1 shows a bias\n    toward the mean only with an intercept; the fit through the origin is shown and gives the\n    same outcome.\n- claim: beh-overlap-prior\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-overlap-prior\n  notes: At ts = 800 ms, pooled over effector and direction (92 Short, 107 Long trials), the median\n    of tp - 800 is +27.8 ms for Short and +47.6 ms for Long, both positive; the two-sided rank-sum\n    test gives p = 0.068. Long tp is longer than Short tp by the mean in 3 of 4 datasets; per\n    dataset p is 0.0515 (Eye Left), 0.778 (Eye Right), 0.0718 (Hand Left) and 0.0010 (Hand\n    Right). Only Hand Left has a negative Short median (-61.6 ms), and its Long median is also\n    negative (-2.8 ms). The paper's p < 1e-43 pools 17 sessions.\n  deviations:\n  - One session, where the paper pools 17 sessions of H.\n- claim: beh-sigmoid-increments\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-sigmoid-increments\n  notes: The middle increment exceeds the extreme one in 7 of 8 conditions (median difference 31.3\n    ms); two-sided signed-rank p = 0.0156 over the 8 conditions. Hand Left Short is the exception\n    (middle 45.3, extreme 56.1 ms).\n  deviations:\n  - Tested over the 8 conditions of one session; the paper's p < 1e-11 is over the sessions and\n    conditions of H.\n- claim: beh-long-more-bias\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-long-more-bias\n  notes: With an intercept the Long slope is below the Short slope in 4 of 4 datasets (0.845 against\n    1.011, 0.903 against 1.107, 0.502 against 0.612, 0.612 against 0.861). Through the origin it\n    is below in 3 of 4 (Eye Right is the exception), which would be partially reproduced. Question\n    for the authors, in the findings - was the regression of Table S1 and Figure 2H fitted with an\n    intercept?\n  deviations:\n  - Assumed that the regression of tp on ts has an intercept. The Methods write \"tp = β ts + ε\"\n    (STAR Methods, Model free analysis of behavior), and the Results read slopes below 1 as a bias\n    toward the mean of the prior (Results, Task and behavior, paragraph 3), which holds only for a\n    line with an intercept. The two readings give different outcomes here (4 of 4 against 3 of 4).\n- claim: beh-bayes-model\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-bayes-model\n  notes: The predicted SD of tp correlates positively with the observed SD in all 4 datasets (r =\n    0.807, 0.911, 0.749, 0.277). The bias R2 (1 - SSres/SStot of observed against predicted bias)\n    is 0.671 (Eye Left), 0.128 (Eye Right), 0.978 (Hand Left) and 0.865 (Hand Right), so at least\n    0.8 in 2 of 4; the squared correlation gives the same split. Fitted wm are 0.025, 0.014, 0.117\n    and 0.074, and wp 0.103, 0.106, 0.090 and 0.104; all fits converged. In the Eye datasets the\n    behaviour is nearly unbiased and the model fits a small wm. Table S3 was not available.\n  deviations:\n  - The model is fit per dataset on one session; the paper pools sessions per animal, effector and\n    direction (STAR Methods, Analysis of behavior with a Bayesian model).\n  - Numerical integration on fixed grids (241 points of tm, 201 of the prior) and Nelder-Mead from 8\n    starting points; standard numerical choices.\n- claim: glm-prior-ts\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:glm-prior-ts\n  measured:\n  - 79.2\n  - 50.0\n  notes: Of 48 selected units, 38 are prior-dependent (79.2%, binomial 95% interval 65.0 to 89.5%)\n    and 24 ts-dependent (50.0%, 35.2 to 64.8%); expected 65 ± 6.5% and 27 ± 2.7%. No fit failed.\n    With all 54 units the fractions are 75.9% and 48.1%, and without attrition 60.4% and 43.8%.\n  deviations:\n  - 48 units of one session, where the paper's fractions are over 536 units of 17 sessions of H.\n  - The window that ends at Set (ts = t) is included in the attrition rule, as the Methods' \"80-ms\n    window immediately before Set\" (STAR Methods, Generalized linear model).\n- claim: dfr-overlap-support\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:dfr-overlap-support\n  notes: The mean RMS of the prior difference over the 4 datasets is largest in the 480 to 640 ms\n    bin (6.88 spikes/s), above the 95th percentile of the shuffled maximum (3.13 spikes/s, 200\n    shuffles). Seven of 11 bins (160 to 1280 ms after Ready) exceed that threshold; the second\n    largest is 800 to 960 ms (6.04), after Set, and the other bin of the support (640 to 800 ms) is\n    4th (4.87).\n  deviations:\n  - Four datasets of one session, where the paper's figure averages 8 datasets of two animals.\n- claim: pca-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:pca-dimensionality\n  notes: 0 of 8 values in range. 2 components reach 75% of the variance in the estimation epoch of\n    every dataset (expected 3 or 4) and 2, 2, 4 and 4 in the production epoch (expected 5 to 11).\n    The first 2 estimation components explain 0.799 to 0.857 of the variance. As variants not used\n    by the claim, z-scored rates need 3 to 4 and 5 to 8 components, and soft-normalised rates 3\n    and 4 to 6.\n  deviations:\n  - The population is 48 units of one session; the paper's PCA is on each of 8 data matrices, one\n    per animal, effector and direction (STAR Methods, Principal component analysis), which pool the\n    units of an animal's sessions. A smaller population can need fewer components.\n- claim: encoding-r2\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:encoding-r2\n  measured:\n  - 0.9957\n  - 0.9774\n  notes: Reading (a), Hand Left, gives R2 = 0.9957 (Short) and 0.9774 (Long); reading (b), the mean of\n    4 datasets, 0.9583 and 0.9823. Both are within tolerance. The PC space has 2 dimensions in\n    every dataset, and 1000 random unit vectors in it give median R2 of 0.716 to 0.987 per dataset\n    and prior; the fraction of random axes at least as good as u is 0.018 to 0.419, so the fit is\n    not specific to u here.\n  deviations:\n  - te comes from the Bayesian model fitted to the same dataset of this session, where the paper's\n    model is fitted to pooled sessions.\n- claim: encoding-bayes-beats-linear\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:encoding-bayes-beats-linear\n  notes: The Bayesian RMSE is lower in 4 of 4 datasets for Short (differences -0.037 to -0.470) and 3\n    of 4 for Long; in Hand Left Long it is higher (0.583 against 0.481). The weighted RMSE gives the\n    same counts.\n  deviations:\n  - RMSE is read as the root mean squared residual of the weighted fit (STAR Methods, Analysis of\n    neural projection, \"RMSE between the actual and predicted Xu\"); the weighted RMSE is shown and\n    gives the same outcome.\n- claim: short-in-long-control\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:short-in-long-control\n  notes: The two-sided signed-rank test of the RMSE difference over the 4 datasets gives p = 0.125\n    with the axis from the state at 480 to that at 800 ms and p = 0.25 with averaged difference\n    vectors; with 4 datasets p cannot fall below 0.125. With the single axis the Bayesian RMSE is\n    lower in 4 of 4 datasets (mean difference -0.096, against -0.260 for the Short prior); with the\n    averaged axis in 3 of 4. The test does not find the effect, but the data show a smaller version\n    of the Short-prior effect in this period.\n  deviations:\n  - The Methods' \"same projection analysis\" (STAR Methods, Analysis of neural projection) would\n    average the difference vectors; that axis is shown and gives the same outcome.\n- claim: neural-long-more-bias\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:neural-long-more-bias\n  notes: The Long slope is below the Short slope in 3 of 4 datasets (Long/Short ratios 0.54, 0.62,\n    0.36); in Hand Right the slopes are 0.0486 (Long) and 0.0470 (Short).\n- claim: speed-vs-projection\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:speed-vs-projection\n  measured:\n  - -0.9209\n  - -0.8398\n  notes: Pooled over 4 datasets (20 points per prior), r = -0.921 for Short and -0.840 for Long, both\n    p < 1e-4; both are more negative than -0.74 ± 0.074 and -0.51 ± 0.051. Within datasets r is\n    -0.84 to -0.99 except Hand Left Long (-0.25, p = 0.68). With speed divided by the mean tp (the\n    Methods' wording) r = -0.932 and -0.947; z-scored within dataset, -0.950 and -0.787.\n  deviations:\n  - The production PC space has 2 to 4 dimensions, where the paper's has 5 to 10.\n- claim: initial-speed-biased\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:initial-speed-biased\n  notes: The measured slope of initial speed on ts is shallower than the unbiased one in 7 of 8\n    dataset-priors (Eye Right Long is the exception), but the two-sided signed-rank test gives p =\n    0.0547; the criterion requires p < 0.05. The paper's p < 1e-3 combines both animals.\n  deviations:\n  - Initial speed is computed in the production-epoch PC space of each dataset (claims file header,\n    speed in the production PC space).\n- claim: speed-predicts-tp\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:speed-predicts-tp\n  measured:\n  - -0.6082\n  - -0.6306\n  notes: Pooled over 4 datasets, r = -0.608 for Short (within -0.58 ± 0.058) and -0.631 for Long\n    (outside -0.52 ± 0.052), p = 0.0044 and 0.0029. With speed divided by the mean tp, r = -0.815\n    and -0.830. Trial by trial within each prior, effector and direction (z-scored within ts), r is\n    -0.05 to -0.42, negative in all 8 and p < 0.05 in the 4 Eye dataset-priors.\n  deviations:\n  - The trial-by-trial variant uses smoothed single-trial rates in the production PC space, not\n    GPFA or a benchmark model.\n- claim: alt-speed-unmodulated\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-speed-unmodulated\n  notes: The two-sided signed-rank test of the 4 slopes against zero gives p = 0.25 (Short) and 0.125\n    (Long); with 4 slopes it cannot reach 0.05. The slopes are positive in 3 of 4 (Short) and 4 of\n    4 (Long), and their bootstrap intervals over trials exclude zero in 2 and 3 of 4; the mean\n    slope is 0.65 and 0.71 of the mean step per second. The number of trials averaged falls about\n    five-fold across the support, which adds noise to the later states and can lengthen their\n    steps.\n  deviations:\n  - Four datasets of one session, where the paper's test has 8.\n- claim: alt-transient-parallel\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-transient-parallel\n  notes: The signed-rank tests of the 8 slopes against zero give p = 0.195 (shortest ts) and 1.0\n    (longest ts). The distance of the shortest ts trajectory to the middle one grows in 6 of 8\n    (median change +49% of its mean over 200 ms); that of the longest does not (median -5%). The\n    PC spaces have 1 to 4 components.\n- claim: alt-threshold-monotonic\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-threshold-monotonic\n  notes: With 60% of the variance (1 to 3 components) the median time of the minimum distance over\n    the 32 curves is 250 ms before Go; 4 of 32 are in the last 40 ms and 12 in the last 200 ms.\n    With 75% (2 to 5 components) the median is 160 ms before Go, which would be partially\n    reproduced. 57% of 20 ms steps decrease the distance. With one component (Eye datasets at 60%)\n    the distance is the absolute difference on one axis.\n  deviations:\n  - The PC spaces have 1 to 3 components at 60%; the paper's legend gives about 60% of the\n    variance of a larger population.\n- claim: gpfa-variance-inverted-u\n  outcome: not_reproduced\n  notebook: gpfa_sohn_2019.ipynb\n  output: claim:gpfa-variance-inverted-u\n  notes: The quadratic coefficient of variance on ts is negative in 5 of 8 dataset-priors; the\n    one-tailed signed-rank test gives p = 0.0742. The mean variance at the extreme ts is below that\n    of the middle three in 5 of 8. Cross-validation chose 8 latent dimensions in all 4 datasets.\n  deviations:\n  - GPFA is Elephant's implementation (elephant.gpfa, 500 EM iterations), not the paper's MATLAB\n    code, which is not public.\n  - The paper ran GPFA on high-yield sessions (N = 48 units for H); this session has 48 selected\n    units, which suggests it is that session, but the files do not say so.\n- claim: gpfa-mean-sigmoid\n  outcome: reproduced\n  notebook: gpfa_sohn_2019.ipynb\n  output: claim:gpfa-mean-sigmoid\n  notes: The middle increment of the mean projection exceeds the extreme one in 7 of 8\n    dataset-priors (two-sided signed-rank p = 0.0156), and the slope of the mean projection on ts is\n    higher for Short in 4 of 4 datasets (one-tailed signed-rank p = 0.0625, the smallest possible\n    with 4, as the paper's).\n  deviations:\n  - GPFA is Elephant's implementation, as for gpfa-variance-inverted-u.\n- claim: rnn-curved-manifold\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The recurrent networks are the paper's simulations. The dandiset holds no network, weights\n    or training code, and the paper names none as public (its code is \"available on request\").\n- claim: rnn-perturbation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: As for rnn-curved-manifold; the trained networks are not public.\n- claim: monkey-g\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds one session of monkey H (Haydn); no session of monkey G is in it or in\n    another dandiset that names the paper.\nfindings:\n- kind: metadata_error\n  statement: The description of the trials column `iti` says it is 500 ms for Short-prior trials and\n    1220 ms for Long-prior trials. The data hold 1220 ms for every Short trial and 500 ms for every\n    Long trial, as the paper's Methods state.\n- kind: metadata_insufficient\n  statement: The `tp` column is longer than go_time - set_time in every completed trial, by 0.1 to\n    153.3 ms (median 17.9 ms; more than 60 ms in 13 trials). The files do not say how tp was measured\n    or which of the two is the produced interval. set_time - ready_time differs from `ts` by up to\n    23.5 ms in either direction.\n- kind: data_missing\n  statement: The dandiset holds one session of monkey H (2016-12-11, 54 units, 1160 trials), one of\n    the paper's 17 sessions of H and 29 of both monkeys. Monkey G is not in it. The paper's\n    population analyses pool units over sessions, so its PCA dimensionality and GLM fractions\n    cannot be repeated on the same population.\n- kind: other\n  about: data\n  statement: The test file holds 283 segments of 1.7 s from the same session with only start, stop and\n    Go times, and 40 of the 54 units; their Ready, Set, ts, tp, prior, effector and direction are\n    withheld for the Neural Latents Benchmark. These trials cannot be used for any analysis by\n    condition, so the dandiset has fewer trials of the session than the recording.\n- kind: metadata_insufficient\n  statement: The units carry no single- or multi-unit label (the paper reports both) and no electrode\n    or probe; the electrodes table has no positions or impedances (x, y, z and imp are NaN for all\n    72). Nothing in the files says which of the paper's sessions this is; its 48 units that pass the\n    paper's unit rule match the GPFA session of H the Results describe (N = 48).\n- kind: methods_unavailable\n  statement: Question for the authors. Was the weighted regression of tp on ts (Table S1, Figures 1E\n    and 2H) fitted with an intercept? The Methods write \"tp = β ts + ε\". In this session the Long\n    slope is below the Short slope in 4 of 4 conditions with an intercept and 3 of 4 through the\n    origin, and through the origin 6 of 8 slopes exceed 1.\n- kind: methods_unavailable\n  about: paper\n  statement: The paper's analysis code is \"available on request\" and not public, and the\n    supplementary tables S1 to S3 were not available to this attempt, so the per-session slopes,\n    model parameters and the GPFA settings could not be compared.\n"
}
```

```
File created successfully at: attempts/sohn-2019-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  ls -a entries/sohn-2019; python tools/entry.py check entries/sohn-2019 2>&1 | tail -20; date -u
```

```
.
..
README.md
entry.yaml
gpfa_sohn_2019.ipynb
reproduce_sohn_2019.ipynb
requirements.in
requirements.lock.txt
rsg.py
0 error(s)
Sun Nov 15 13:16:19 UTC 2026
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/sohn-2019 2>&1 | tail -20; date -u
```

```
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (60 s)
pass  gpfa_sohn_2019.ipynb  (686 s)

real	12m36.944s
user	32m45.563s
sys	0m5.783s
Sun Nov 15 13:28:58 UTC 2026
```

**Agent**

Both notebooks pass in the clean environment (60 s and 686 s). Checking that the executed numbers match the conclusions.

**Agent calls Bash**

```bash
cd  ls executed/sohn-2019; source $TMPDIR/dev/bin/activate; python $TMPDIR/dump.py executed/sohn-2019/reproduce_sohn_2019.ipynb > $TMPDIR/e1.txt; python $TMPDIR/dump.py $TMPDIR/nb1_out.ipynb > $TMPDIR/d1.txt; diff $TMPDIR/d1.txt $TMPDIR/e1.txt; python $TMPDIR/dump.py executed/sohn-2019/gpfa_sohn_2019.ipynb | grep -v "^Initializing\|^Fitting\|^$" > $TMPDIR/e2.txt; python $TMPDIR/dump.py $TMPDIR/nb2_out.ipynb | grep -v "^Initializing\|^Fitting\|^$" > $TMPDIR/d2.txt; diff $TMPDIR/d2.txt $TMPDIR/e2.txt
```

```
gpfa_sohn_2019.ipynb
reproduce_sohn_2019.ipynb
result.json
41c41
< prior and iti agree (Short 500, Long 1220): False
---
> iti as the column description states (Short 500, Long 1220): False | as the Methods state (Short 1220, Long 500): True
46c46
< run time so far 5 s
---
> run time so far 7 s
316d315
< 
417c416
< total run time 48 s; peak memory 0.6 GB
---
> total run time 51 s; peak memory 0.65 GB
16,19c16,19
< {'dataset': 'Eye Left', 'trials': 260, 'cv_ll_4': np.float64(-164187.10285920056), 'cv_ll_8': np.float64(-163618.32957105397), 'chosen': 8, 'em_iterations': 500, 'seconds': 171}
< {'dataset': 'Eye Right', 'trials': 275, 'cv_ll_4': np.float64(-173156.49228412766), 'cv_ll_8': np.float64(-172503.25879582213), 'chosen': 8, 'em_iterations': 500, 'seconds': 173}
[... 21 more lines not kept]
```

**Agent**

Executed outputs match the development run exactly. Building the verifier's handover.

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/sohn-2019 2>&1 | tail -5; ls executed/sohn-2019/handover; python tools/entry.py check entries/sohn-2019 2>&1 | tail -2; ls -a entries/sohn-2019; date -u
```

```
wrote executed/sohn-2019/handover
gpfa_sohn_2019.ipynb
reproduce_sohn_2019.ipynb
rsg.py
sohn-2019.yaml
0 error(s)
.
..
README.md
__pycache__
entry.yaml
gpfa_sohn_2019.ipynb
reproduce_sohn_2019.ipynb
requirements.in
requirements.lock.txt
rsg.py
Sun Nov 15 13:29:28 UTC 2026
```

**Agent calls Bash**

```bash
cd  git check-ignore -v entries/sohn-2019/__pycache__ 2>&1 | head -2; grep -c "Result:" executed/sohn-2019/handover/*.ipynb; grep -c "## Summary" executed/sohn-2019/handover/*.ipynb
```

```
fatal: not a git repository (or any of the parent directories): .git
executed/sohn-2019/handover/gpfa_sohn_2019.ipynb:0
executed/sohn-2019/handover/reproduce_sohn_2019.ipynb:0
executed/sohn-2019/handover/gpfa_sohn_2019.ipynb:0
executed/sohn-2019/handover/reproduce_sohn_2019.ipynb:0
```

**Agent calls Bash**

```bash
cd  grep -n "pycache" .gitignore; rm -rf entries/sohn-2019/__pycache__; python tools/entry.py check entries/sohn-2019 2>&1 | tail -1
```

```
1:__pycache__/
0 error(s)
```

**Agent**

I finished steps 1 to 6 for `sohn-2019`. The entry is at `entries/sohn-2019/` and the record at `attempts/sohn-2019-02.yaml`. Both notebooks passed `entry.py all` in a clean environment, `check` reports 0 errors, and the handover is built. I did not come across any earlier attempt. Nothing is committed.

**(1) Outcomes** (20 tested, 3 blocked)

| Claim | Outcome |
|---|---|
| beh-slopes | not reproduced: the two Eye Short slopes are 1.011 and 1.107, above 1 |
| beh-overlap-prior | not reproduced: at ts = 800 both median biases are positive (+27.8 and +47.6 ms), p = 0.068 |
| beh-sigmoid-increments | reproduced: 7 of 8, p = 0.0156 |
| beh-long-more-bias | reproduced, resting on an assumption (4 of 4) |
| beh-bayes-model | partially reproduced: bias R2 ≥ 0.8 in only 2 of 4 datasets; SD correlation positive in 4 of 4 |
| glm-prior-ts | not reproduced: 79.2% prior-dependent and 50.0% ts-dependent units, against 65% and 27% |
| dfr-overlap-support | reproduced |
| pca-dimensionality | not reproduced: 0 of 8 in range (2 components for estimation, 2 to 4 for production) |
| encoding-r2 | reproduced: 0.9957 and 0.9774 (Hand Left); random axes also score high R2 |
| encoding-bayes-beats-linear | partially reproduced: Short 4 of 4, Long 3 of 4 |
| short-in-long-control | reproduced: p = 0.125; with 4 datasets the test cannot reach 0.05 |
| neural-long-more-bias | partially reproduced: 3 of 4 |
| speed-vs-projection | partially reproduced: r = −0.92 and −0.84, stronger than the paper's |
| initial-speed-biased | not reproduced: 7 of 8 in the right direction, but p = 0.0547 |
| speed-predicts-tp | partially reproduced: Short −0.61 within tolerance, Long −0.63 outside |
| alt-speed-unmodulated | reproduced: p = 0.25 and 0.125, though slopes lean positive |
| alt-transient-parallel | reproduced: p = 0.195 and 1.0 |
| alt-threshold-monotonic | not reproduced: median minimum 250 ms before Go |
| gpfa-variance-inverted-u | not reproduced: 5 of 8, p = 0.074 |
| gpfa-mean-sigmoid | reproduced: 7 of 8, p = 0.0156; Short slope higher in 4 of 4 |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked, data_missing |

**(2) Dataset, assumptions, questions**
- **What is in it:** one session of monkey H (2016-12-11), 54 units (48 pass the paper's unit rule) and 982 usable trials. The paper uses 29 sessions from two monkeys, and its population analyses pool units across sessions. Monkey G and the paper's recurrent networks are absent.
- **Wrong description:** the `iti` column's description swaps the priors. The data match the paper's Methods (Short 1220 ms, Long 500 ms).
- **Undocumented `tp`:** it is longer than Go − Set by 0.1 to 153 ms (median 17.9 ms), and the files don't say how it was measured.
- **Test file:** its 283 trials hold no behaviour or condition labels and only 40 units, so they can't be used.
- **Missing unit metadata:** units have no single/multi-unit label and no electrode; electrode positions are NaN.
- **Clock check:** spikes and trial events share a clock. Target direction decodes at 0.62 to 0.75 around Go, and at chance with the windows shifted by 10 s.
- **Assumption (beh-long-more-bias):** I assumed the slope regression has an intercept. The Methods write "tp = β ts + ε", but the paper reads slopes below 1 as bias toward the mean, which only works with an intercept. Through the origin the result would be 3 of 4. This is recorded as a question for the authors (`methods_unavailable`).
- **Reader questions:** none asked.

**(3) Protocol points**
1. The claims file has no `checks` section, though the protocol says a file is ready when its last check says so. The prompt said it was checked, so I went ahead.
2. Three absence claims are tested by signed-rank tests over 4 datasets, which can never reach p < 0.05, so they are reproduced whatever the data show. I reported effect sizes; two of them point toward the effect being present.
3. There is no rule for expected values that depend on population size, such as PCA dimensions or GLM fractions computed from pooled sessions. I recorded the difference as a deviation and still judged the claims.
4. Any edit triggers a full re-run, so `runtime_minutes` has to be written before the final run. I left the GPFA notebook at 11 minutes; it took 11.4.

**(4) Runtime and failures**
- The whole run took about 50 minutes (12:41 to about 13:30 UTC).
- Main notebook: about 60 s. GPFA notebook (Elephant's implementation): 686 s. Peak memory 0.65 GB.
- Nothing failed: no fit failed, and the executed numbers match the development run exactly.

## End of run

48 turns, 42 minutes, $4.58 at API prices, result: success.
