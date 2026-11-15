# sohn-2019 · author · run 43684558521

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries attempts claims paper tools; wc -l docs/*.md README.md
```

```
Sun Nov 15 06:20:20 UTC 2026
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
[... 1008 more lines not kept]
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
cat README.md | head -80; sed -n 1,280p docs/design.md | head -150
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

**Agent calls Bash**

```bash
ls -R entries/fouke-2025 | head -30; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -250
```

```
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "protocol: pilot-1[45]" attempts/*.yaml | head; ls schemas; sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -120
```

```
attempts/andrews-2024-01.yaml
attempts/asari-2009-01.yaml
attempts/brinke-2017-01.yaml
attempts/brudner-2026-01.yaml
attempts/burman-2023-01.yaml
attempts/dana-2016-01.yaml
attempts/danish-2017-01.yaml
attempts/dijk-2018-01.yaml
attempts/elie-2019-01.yaml
attempts/gao-2018-01.yaml
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
ls -t attempts/ | head -5; grep -l "protocol: pilot-15" attempts/*.yaml | head -3; python -c "import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
zhuang-2025-01.yaml
zheng-2022-01.yaml
zhu-2022-01.yaml
zhang-2021-01.yaml
zhai-2025-02.yaml
attempts/asari-2009-01.yaml
attempts/dana-2016-01.yaml
attempts/danish-2017-01.yaml
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "One attempt at reproducing the claims of a target",
 "description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "id",
  "datasets",
  "paper",
  "date",
[... 227 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['outcomes'],indent=1)); print(json.dumps(s['properties']['findings'],indent=1)[:3000])"; cat papers/datasets/sohn-2019.yaml; ls entries/dana-2016
```

```
{
 "description": "One per claim attempted.",
 "type": "array",
 "minItems": 1,
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "claim",
   "outcome"
  ],
  "properties": {
   "claim": {
    "description": "Claim id from the target's claims file.",
    "type": "string"
   },
   "outcome": {
    "enum": [
     "reproduced",
     "partially_reproduced",
[... 206 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "STAR\|Methods\|QUANTIFICATION" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 200 paper/10.1016-j.neuron.2019.06.012.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt; grep -n "Task and behavior\|Single-neuron\|Geometry and dynamics\|Encoding Bayesian\|Controlling speed\|Alternative\|curved manifold hypothesis\|Recurrent network\|STAR\|Generalized linear\|Dimensionality\|GPFA\|speed" $TMPDIR/paper.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

Let me read the Results and Methods.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 37,
 "limit": 115
}
```

```
37	with Bayesian integration. Results Task and behavior Two rhesus macaques performed a time-interval reproduction task, which we refer to as the Ready-Set-Go (RSG) task ( Figure 1A ). The task consists 
38	of an estimation epoch followed by a production epoch. In the estimation epoch, animals had to estimate a sample interval, t s , demarcated by two visual flashes (Ready followed by Set). In the 
39	production epoch, animals had to produce a matching interval by either initiating a saccade or by moving the joystick to the left or right (Go), depending on the location of a peripheral target. 
40	Monkeys received reward if the produced interval, t p , between Set and Go was sufficiently close to t s ( Figure 1B ). We manipulated the animals’ prior expectations by sampling t s from one of two 
41	uniform prior distributions, a ‘Short’ prior ranging between 480 and 800 ms, and a’Long’ prior ranging between 800 and 1200 ms Figure(1C) . The task enabled us to also manipulate sensory uncertainty 
42	since measurements of time intervals become more variable for longer intervals, a property known as ‘scalar variability’ ( Malapani and Fairhurst, 2002 ). Since the two prior distributions overlapped 
43	at t s = 800 ms, the task further offered the opportunity to characterize how neural representations are independently modulated by prior beliefs. The prior condition and the desired effector were 
44	switched across short blocks of trials (block length: 4.0 ± 4.4 trials; uniform hazard) and the trial type was explicitly cued throughout each trial ( Figure 1D ). The rationale for including two 
45	response modalities and two directions of response was to ensure that the neural correlates of Bayesian integration identified would generalize across multiple experimental conditions. To verify that 
46	animals learned to perform the task, we used a regression analysis to assess the dependence of t p on t s . The regression slopes were positive, indicating that animals were able to
[... 105 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 217,
 "limit": 100
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
[... 90 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 457,
 "limit": 70
}
```

```
457	10.1152/jn.90941.2008 PMC2712272 Figure 1. Task and behavior. (A) Schematic of a single trial of the Ready-Set-Go task. The animal has to estimate a sample interval, t s , between Ready and Set 
458	(estimation epoch), and produce a matching interval, t p , after Set with a delayed response (Go) via a saccade or a movement of the joystick (production epoch). (B) Reward as a function of relative 
459	error ( t p -t s )/ t s . (C) ‘Short’ and ‘Long’ prior distributions of t s . (D) Eight randomly interleaved trial types (see Methods ): 2 prior conditions (Short and Long) × 2 effectors (Eye and 
460	Hand) × 2 target directions (Left and Right). (E) Behavior. Top: A representative session for monkey H showing t p pooled across effectors and target directions (small dots: individual trials; large 
461	open circles: average t p per t s ; solid lines: Bayesian model; diagonal: unity line). The horizontal location of dots was jittered to facilitate visualization. Right: Histograms of t p for the 
462	overlapping t s (horizontal dashed line) for the two prior conditions (orange: Short; blue:Long; triangles: averages). Top-left inset: Average error (i.e., bias) for each t s (circles: data; solid 
463	lines: Bayesian model). Bottom-right inset: histogram of regression slopes relating t p to t s across sessions (red: Short; blue: Long; triangles: averages). Bottom: The same as top for Monkey G. 
464	Figure 2. Bayesian model and behavior. (A) Bayesian observer model. The measurement ( t m ) is the sample interval ( t s ) plus white noise with standard deviation proportional to t s . The Bayesian 
465	estimator is a sigmoidal function that maps t m to an optimal estimate ( t e ) (red: Short; blue: Long). t e is biased toward the mean of the prior (arrows). The production interval ( t p ) is t e 
466	plus scalar noise during production epoch. (B) The prior (top), the likelihood function (middle), the resulting posterior (bottom), and the posterior mean (circles) that represent
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.241017.1448/assets/?page_size=100" | python -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.241017.1448/info/" | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'));print(m.get('doi'));print(json.dumps(m.get('relatedResource'),indent=1));print(m.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas statsmodels scikit-learn matplotlib nbformat nbclient ipykernel 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"; sed -n 1,80p tools/entry.py | head -80
```

```
4.2.0
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

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
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
[... 62 more lines not kept]
```

**Agent**

Now open the files and list everything.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/survey.py <<'EOF'
import requests, remfile, h5py, pynwb, numpy as np, pandas as pd
V="0.241017.1448"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000130/versions/{V}/assets/").json()
for a in r["results"]:
    url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    f=h5py.File(remfile.File(requests.head(url,allow_redirects=True).url),"r")
    io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
    print("=====",a["path"]); print(nwb)
    print(nwb.subject); print(nwb.session_start_time, nwb.session_description, nwb.identifier)
    tr=nwb.trials.to_dataframe(); print(tr.shape); print(tr.dtypes); print(tr.head(8).T)
    print(tr.describe(include='all').T)
    u=nwb.units.to_dataframe(); print(u.shape); print(u.columns.tolist()); print(u.drop(columns=['spike_times']).head())
    for k in nwb.units.colnames: 
        c=nwb.units[k]; print(k, c.description if hasattr(c,'description') else '')
    for k in tr.columns: print(k, '|', nwb.trials[k].description)
    print(nwb.acquisition, nwb.processing, nwb.electrodes.to_dataframe().head() if nwb.electrodes is not None else None)
EOF
python $TMPDIR/survey.py 2>&1 | head -300
```

```
===== sub-Haydn/sub-Haydn_desc-test_ecephys.nwb
root pynwb.file.NWBFile at 0x127696923623504
Fields:
  devices: {
    electrode_probe_1 <class 'pynwb.device.Device'>,
    electrode_probe_2 <class 'pynwb.device.Device'>,
    electrode_probe_3 <class 'pynwb.device.Device'>
  }
  electrode_groups: {
    electrode_group_1 <class 'pynwb.ecephys.ElectrodeGroup'>,
    electrode_group_2 <class 'pynwb.ecephys.ElectrodeGroup'>,
    electrode_group_3 <class 'pynwb.ecephys.ElectrodeGroup'>
  }
  electrodes: electrodes <class 'pynwb.ecephys.ElectrodesTable'>
  experiment_description: Cognitive timing task in which subject attempts to reproduce interval between two cues
  experimenter: ['Hansem Sohn']
  file_create_date: [datetime.datetime(2021, 10, 29, 22, 31, 56, 620865, tzinfo=tzoffset(None, -14400))]
  identifier: 8d26aa92-3929-11ec-8077-43176b153428
  institution: Massachusetts Institute of Technology
  intervals: {
[... 234 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/survey2.py <<'EOF'
import requests, remfile, h5py, pynwb, numpy as np, pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_columns',50)
V="0.241017.1448"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000130/versions/{V}/assets/").json()
a=[x for x in r["results"] if 'train' in x['path']][0]
url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
f=h5py.File(remfile.File(requests.head(url,allow_redirects=True).url),"r")
nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
tr=nwb.trials.to_dataframe()
print(tr.split.value_counts())
print(pd.crosstab(tr.is_short, tr.iti))
done=tr.dropna(subset=['set_time','go_time'])
print('with set&go',len(done))
print('ts-(set-ready)', np.nanmax(np.abs((tr.set_time-tr.ready_time)*1000-tr.ts)))
d=(done.go_time-done.set_time)*1000-done.tp; print('tp-(go-set)', d.abs().describe())
print('tp<0 count', (tr.tp<0).sum(), 'tp nan', tr.tp.isna().sum())
print(pd.crosstab(tr.ts, tr.is_short))
print(pd.crosstab([done.is_short,done.is_eye,done.theta], done.ts))
print('outliers among done', done.is_outlier.sum(), 'outliers total', tr.is_outlier.sum())
print(pd.crosstab(tr.is_outlier, tr.set_time.notna()))
print(pd.crosstab(tr.is_outlier, tr.reward_time.notna()))
print(pd.crosstab(tr.split, tr.go_time.notna()))
g=done[~done.is_outlier]
print(pd.crosstab([g.is_short,g.is_eye,g.theta], g.ts))
print('bad_time with go', (tr.bad_time.notna()&tr.go_time.notna()).sum())
el=nwb.electrodes.to_dataframe(); print(el.columns.tolist()); print(el.head()); print(el.group_name.value_counts())
u=nwb.units
print(u.colnames, len(u))
oi=u['obs_intervals'][0]; print('obs', oi)
dur=sum(b-a for a,b in oi); print('obs dur', dur)
rates=[len(u['spike_times'][i])/dur for i in range(len(u))]
print(np.round(sorted(rates),2))
print('heldout', u['heldout'][:].sum())
st=u['spike_times'][0]; print('sorted', np.all(np.diff(st)>=0), st.min(), st.max())
print('units id', u.id[:])
print(nwb.units.electrodes if 'electrodes' in u.colnames else 'no electrodes col')
print(tr[['start_time','stop_time']].diff().describe())
print('trial times relative', (tr.ready_time-tr.start_time).describe())
EOF
python $TMPDIR/survey2.py 2>&1
```

```
split
train    748
val      258
none     154
Name: count, dtype: int64
iti       500.0   1220.0
is_short                
False        583       0
True           0     577
with set&go 1029
ts-(set-ready) 23.500000000140062
tp-(go-set) count    1029.000000
mean       28.582287
std       186.788770
min         0.142000
25%        17.232000
50%        17.882000
75%        21.338000
max      5322.000000
dtype: float64
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/env/bin/activate; uv pip install -q elephant 2>&1 | tail -2; python -c "import elephant, neo, quantities; print(elephant.__version__, neo.__version__)"; cat >> $TMPDIR/survey2.py <<'EOF'
g=tr[(~tr.is_outlier)&tr.set_time.notna()]
x=(g.set_time-g.ready_time)*1000-g.ts; print('set-ready - ts', x.describe(), np.round(np.percentile(x,[1,5,50,95,99]),2))
y=(g.go_time-g.set_time)*1000-g.tp; print('go-set - tp', y.describe(), np.round(np.percentile(y,[1,5,50,95,99]),2))
print(pd.crosstab(g.is_eye, pd.cut(y,[-100,0,10,15,17,19,25,40,100,1e5])))
print('good with bad_time', g.bad_time.notna().sum(), 'good tp min', g.tp.min(), g.tp.max())
print(g.groupby(['is_short','ts']).tp.agg(['mean','std','min','count']))
EOF
python $TMPDIR/survey2.py 2>&1 | tail -50
```

```
Sun Nov 15 06:23:13 UTC 2026
1.2.1 0.14.6
std       4.258823     4.287147
min       1.583000     0.566000
25%       3.550500     3.550000
50%       3.882500     3.916500
75%       4.283500     4.367000
max     126.751500   126.751500
trial times relative count    1060.000000
mean        1.306609
std         0.385635
min         0.800500
25%         1.034500
50%         1.217500
75%         1.467000
max         4.234000
dtype: float64
set-ready - ts count    9.830000e+02
mean    -1.422177e+00
std      6.681722e+00
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/sohn-2019; ls -la entries/sohn-2019; ls questions | grep sohn; ls entries/dana-2016; head -60 entries/dana-2016/cai2.py
```

```
total 16
drwxr-xr-x   2 runner runner  4096 Nov 15 06:23 .
drwxr-xr-x 301 runner runner 12288 Nov 15 06:23 ..
README.md
cai2.py
entry.yaml
reproduce_dana_2016.ipynb
requirements.in
requirements.lock.txt
"""Loading and measures for CRCNS data set cai-2 (Dana et al. 2016, eLife 5:e12727, Figure 4).

cai-2 holds simultaneous loose-seal cell-attached recordings and two-photon imaging of L2/3
neurons in mouse V1 expressing jRGECO1a (30 Hz frames) or jRCaMP1a (15 Hz frames). Each
recording is a MATLAB file inside one of two tar.gz archives in the public S3 bucket
crcnsarchive. The archives are streamed (decompressed as they are read, never written to disk)
and each recording is reduced, as it is read, to the soma and neuropil fluorescence, the frame
times and the detected spike times. The 10 kHz ephys traces are dropped after hashing them.

Where each parameter comes from:

[... 50 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/sohn-2019/rsg.py",
 "content": "\"\"\"Loading and measures for dandiset 000130 (Sohn, Narain, Meirhaeghe & Jazayeri 2019, Neuron 103:934).\n\nDandiset 000130 holds one session (2016-12-11) of monkey H (Haydn) in the Ready-Set-Go task,\nprepared for the Neural Latents Benchmark (NLB): a \"train\" file with the trial table and the\nspikes of 54 units over the session, and a \"test\" file with 283 further trials whose task\nvariables are withheld and whose spikes are given for 40 of the units only. Every analysis here\nuses the train file, streamed from the archive at the pinned version.\n\nWhere each parameter comes from (claims file claims/sohn-2019.yaml, its opening comment and the\ncriteria, unless said otherwise):\n\n- Trials: completed trials (Set and Go present, tp > 0) not flagged `is_outlier`, the file's\n  mixture-model flag (claims file, method choices). The neural analyses use the same trials (a\n  standard choice: the Methods do not say whether the behavioural outliers are dropped from the\n  neural averages).\n- Units: mean rate over the file of at least 1 spike/s and at least 5 trials in each of the 40\n  conditions (Methods, \"Analysis of single- and multi-unit activity\").\n- Rates: spike counts in 20 ms bins, averaged over trials, in spikes/s, smoothed by a Gaussian of\n  SD 40 ms (Methods, \"Principal component analysis\": \"bin size: 20 ms, Gaussian smoothing kernel\n  width: 40 ms\"; the claims file reads the width as the SD). The kernel is renormalised over the\n  bins of each trajectory, so that no bin outside the epoch enters (a standard choice).\n- Estimation epoch: from Ready to the prior's longest ts, each bin averaging the trials whose Set\n  comes at or after the end of the bin (attrition; Methods, \"Principal component analysis\").\n  Production epoch: from Set to the shortest tp of that ts (same passage).\n- PCA: per effector and direction (\"dataset\") and epoch, on the trajectories of both priors\n  concatenated, mean-centred, not normalised; the fewest components reaching 75% of the variance.\n- Encoding axis u: the mean of X(ts_max - d) - X(ts_min + d) for d = 0, 20, 40 ms ... while\n  ts_min + d < ts_max - d, normalised (Methods, \"Analysis of neural projection\"). The state at\n  time t is the bin that ends at t.\n- Bayesian observer: continuous uniform prior on each range, measurement noise SD wm*ts, the\n  posterior mean as te, production noise SD wp*te, an offset b per prior; wm, wp, bShort, bLong\n  fit by maximum likelihood per dataset (Methods, \"Analysis of behavior with a Bayesian model\").\n  Integrals are taken on grids of 301 points over +-5 SD of tm and over the prior range (a\n  standard choice).\n- GPFA: elephant's implementation of Yu et al. (2009), 20 ms bins, the latent dimensionality\n  chosen from 4 and 8 by 3-fold cross-validated log-likelihood (claims file), orthonormalised\n  latents. Seeds are fixed per claim.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport numpy as np\nimport pandas as pd\nimport requests\n\nDANDISET = \"000130\"\nVERSION = \"0.241017.1448\"\nTRAIN_PATH = \"sub-Haydn/sub-Haydn_desc-train_ecephys.nwb\"\nTEST_PATH = \"sub-Haydn/sub-Haydn_desc-test_ecephys.nwb\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nSHORT_TS = np.array([480, 560, 640, 720, 800])\nLONG_TS = np.array([800, 900, 1000, 1100, 1200])\nPRIOR_TS = {\"Short\": SHORT_TS, \"Long\": LONG_TS}\nBIN = 20  # ms\nSMOOTH_SD = 40  # ms\nVAR_THRESHOLD = 0.75\n\n# effector and direction: theta 0 is right and 180 is left (the file's description of `theta`)\nDATASETS = [(\"Eye\", \"Left\"), (\"Eye\", \"Right\"), (\"Hand\", \"Left\"), (\"Hand\", \"Right\")]\n\n\n# ---------------------------------------------------------------- loading\n\ndef asset_url(path: str) -> str:\n    \"\"\"S3 URL of an asset of the pinned version.\"\"\"\n    r = requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/\",\n                     params={\"path\": path}, timeout=60)\n    r.raise_for_status()\n    hits = [a for a in r.json()[\"results\"] if a[\"path\"] == path]\n    if len(hits) != 1:\n        raise RuntimeError(f\"{path} not found once in {DANDISET}/{VERSION}\")\n    head = requests.head(f\"{API}/assets/{hits[0]['asset_id']}/download/\", allow_redirects=True,\n                         timeout=60)\n    head.raise_for_status()\n    return head.url\n\n\ndef list_assets() -> pd.DataFrame:\n    r = requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/\",\n                     params={\"page_size\": 100}, timeout=60)\n    r.raise_for_status()\n    return pd.DataFrame(r.json()[\"results\"])[[\"path\", \"size\", \"asset_id\"]]\n\n\ndef open_nwb(path: str):\n    \"\"\"Stream an NWB file of the pinned version; returns (nwbfile, io).\"\"\"\n    import h5py\n    import pynwb\n    import remfile\n    h5 = h5py.File(remfile.File(asset_url(path)), \"r\")\n    io = pynwb.NWBHDF5IO(file=h5, load_namespaces=True)\n    return io.read(), io\n\n\ndef load_session(path: str = TRAIN_PATH) -> dict:\n    \"\"\"Trial table, spike times (s) of every unit, and the unit table of one file.\"\"\"\n    nwb, io = open_nwb(path)\n    trials = nwb.trials.to_dataframe().reset_index()\n    u = nwb.units\n    spikes = [np.asarray(u[\"spike_times\"][i]) for i in range(len(u))]\n    obs = [np.asarray(u[\"obs_intervals\"][i]) for i in range(len(u))]\n    units = pd.DataFrame({\"id\": u.id[:], \"heldout\": u[\"heldout\"][:]})\n    units[\"observed_s\"] = [float(np.sum(o[:, 1] - o[:, 0])) for o in obs]\n    units[\"n_spikes\"] = [len(s) for s in spikes]\n    units[\"rate\"] = units.n_spikes / units.observed_s\n    out = dict(nwb=nwb, io=io, trials=trials, spikes=spikes, units=units, obs=obs)\n    return out\n\n\ndef label_trials(trials: pd.DataFrame) -> pd.DataFrame:\n    t = trials.copy()\n    t[\"prior\"] = np.where(t.is_short, \"Short\", \"Long\")\n    t[\"effector\"] = np.where(t.is_eye, \"Eye\", \"Hand\")\n    t[\"direction\"] = t.theta.map({0.0: \"Right\", 180.0: \"Left\"})\n    t[\"dataset\"] = t.effector + \" \" + t.direction\n    return t\n\n\ndef good_trials(trials: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Completed trials not flagged by the mixture model (claims file, method choices).\"\"\"\n    t = label_trials(trials)\n    ok = t.set_time.notna() & t.go_time.notna() & (t.tp > 0) & ~t.is_outlier\n    return t[ok].reset_index(drop=True)\n\n\ndef select_units(sess: dict, good: pd.DataFrame, min_rate=1.0, min_trials=5) -> np.ndarray:\n    \"\"\"Indices of units with mean rate >= 1 spike/s and >= 5 trials in each of the 40 conditions.\n\n    All units are observed over the whole file (their obs_intervals), so the trial count per\n    condition is the same for every unit.\"\"\"\n    counts = good.groupby([\"prior\", \"ts\", \"effector\", \"direction\"]).size()\n    enough = len(counts) == 40 and counts.min() >= min_trials\n    keep = (sess[\"units\"].rate.values >= min_rate) & enough\n    return np.flatnonzero(keep)\n\n\n# ---------------------------------------------------------------- binning and rates\n\ndef bin_counts(spikes: list, align: np.ndarray, start_ms: float, stop_ms: float,\n               bin_ms: float = BIN) -> np.ndarray:\n    \"\"\"Spike counts, trials x bins x units, in bins [start, stop) relative to `align` (s).\"\"\"\n    edges_rel = np.arange(start_ms, stop_ms + bin_ms / 2, bin_ms) / 1000.0\n    nb = len(edges_rel) - 1\n    out = np.zeros((len(align), nb, len(spikes)), dtype=np.float32)\n    edges = align[:, None] + edges_rel[None, :]\n    for k, s in enumerate(spikes):\n        idx = np.searchsorted(s, edges)\n        out[:, :, k] = np.diff(idx, axis=1)\n    return out\n\n\ndef gauss_smooth(x: np.ndarray, sd_bins: float = SMOOTH_SD / BIN) -> np.ndarray:\n    \"\"\"Gaussian smoothing along axis 0, renormalised at the edges (no bins outside x).\"\"\"\n    n = x.shape[0]\n    t = np.arange(n)\n    w = np.exp(-0.5 * ((t[:, None] - t[None, :]) / sd_bins) ** 2)\n    w /= w.sum(axis=1, keepdims=True)\n    return np.tensordot(w, x, axes=(1, 0))\n\n\ndef estimation_rates(spikes, good_sub: pd.DataFrame, ts_max: float, smooth=True):\n    \"\"\"Trial-averaged rates (spikes/s) from Ready to ts_max with attrition.\n\n    Bin j covers [20j, 20j+20) ms after Ready and averages the trials with ts >= its end.\n    Returns (rates bins x units, bin end times in ms, trials per bin).\"\"\"\n    counts = bin_counts(spikes, good_sub.ready_time.values, 0, ts_max)\n    ends = np.arange(BIN, ts_max + 1, BIN)\n    valid = good_sub.ts.values[:, None] >= ends[None, :]\n    n = valid.sum(axis=0)\n    rates = (counts * valid[:, :, None]).sum(axis=0) / n[:, None] * (1000.0 / BIN)\n    if smooth:\n        rates = gauss_smooth(rates)\n    return rates, ends, n\n\n\ndef aligned_rates(spikes, align_s: np.ndarray, start_ms: float, stop_ms: float, smooth=True):\n    \"\"\"Trial-averaged rates (spikes/s), bins x units, aligned to align_s, over [start, stop).\"\"\"\n    counts = bin_counts(spikes, align_s, start_ms, stop_ms)\n    rates = counts.mean(axis=0) * (1000.0 / BIN)\n    return gauss_smooth(rates) if smooth else rates\n\n\ndef production_rates(spikes, good_sub: pd.DataFrame, prior: str, stop_ms=None):\n    \"\"\"Per ts of the prior: rates from Set to the shortest tp of that ts (or to stop_ms, using\n    trials with tp >= stop_ms). Returns dict ts -> (bins x units).\"\"\"\n    out = {}\n    for ts in PRIOR_TS[prior]:\n        sub = good_sub[(good_sub.prior == prior) & (good_sub.ts == ts)]\n        if stop_ms is None:\n            stop = np.floor(sub.tp.min() / BIN) * BIN\n        else:\n            stop = stop_ms\n            sub = sub[sub.tp >= stop_ms]\n        out[ts] = aligned_rates(spikes, sub.set_time.values, 0, stop)\n    return out\n\n\n# ---------------------------------------------------------------- PCA and geometry\n\ndef pca_fit(X: np.ndarray, threshold: float = VAR_THRESHOLD):\n    \"\"\"PCA of rows of X (mean-centred). Returns (mean, components k x units, k, explained ratio).\"\"\"\n    mu = X.mean(axis=0)\n    _, s, vt = np.linalg.svd(X - mu, full_matrices=False)\n    ev = s ** 2 / np.sum(s ** 2)\n    k = int(np.searchsorted(np.cumsum(ev), threshold - 1e-12) + 1)\n    return mu, vt[:k], k, ev\n\n\ndef project(X, mu, comps):\n    return (X - mu) @ comps.T\n\n\ndef encoding_axis(states: np.ndarray, ends: np.ndarray, ts_min: float, ts_max: float):\n    \"\"\"Unit vector u: mean of X(ts_max - d) - X(ts_min + d), d = 0, 20, ... while\n    ts_min + d < ts_max - d (Methods, \"Analysis of neural projection\").\"\"\"\n    pos = {int(round(e)): i for i, e in enumerate(ends)}\n    diffs = []\n    d = 0\n    while ts_min + d < ts_max - d:\n        diffs.append(states[pos[int(ts_max - d)]] - states[pos[int(ts_min + d)]])\n        d += BIN\n    v = np.mean(diffs, axis=0)\n    return v / np.linalg.norm(v)\n\n\ndef step_speed(traj: np.ndarray) -> float:\n    \"\"\"Mean Euclidean distance between successive states.\"\"\"\n    return float(np.mean(np.linalg.norm(np.diff(traj, axis=0), axis=1)))\n\n\n# ---------------------------------------------------------------- Bayesian observer\n\ndef _grid(lo, hi, n=301):\n    return np.linspace(lo, hi, n)\n\n\ndef te_of_tm(tm: np.ndarray, prior: str, wm: float) -> np.ndarray:\n    \"\"\"Posterior mean of ts given tm, continuous uniform prior over the prior's range.\"\"\"\n    lo, hi = PRIOR_TS[prior][0], PRIOR_TS[prior][-1]\n    s = _grid(lo, hi)\n    sd = wm * s\n    lik = np.exp(-0.5 * ((tm[..., None] - s) / sd) ** 2) / sd\n    return (lik * s).sum(-1) / lik.sum(-1)\n\n\ndef _tm_nodes(ts, wm, n=301):\n    z = np.linspace(-5, 5, n)\n    w = np.exp(-0.5 * z ** 2)\n    w /= w.sum()\n    return ts + z * wm * ts, w\n\n\ndef bayes_loglik(params, df: pd.DataFrame) -> float:\n    wm, wp, bS, bL = params\n    if wm <= 0.01 or wp <= 0.01 or wm > 1 or wp > 1:\n        return -np.inf\n    ll = 0.0\n    for (prior, ts), g in df.groupby([\"prior\", \"ts\"]):\n        tm, w = _tm_nodes(ts, wm)\n        te = te_of_tm(tm, prior, wm)\n        b = bS if prior == \"Short\" else bL\n        mu = te + b\n        sd = wp * te\n        tp = g.tp.values[:, None]\n        dens = (np.exp(-0.5 * ((tp - mu) / sd) ** 2) / (np.sqrt(2 * np.pi) * sd) * w).sum(1)\n        ll += np.sum(np.log(np.maximum(dens, 1e-300)))\n    return ll\n\n\ndef fit_bayes(df: pd.DataFrame) -> dict:\n    \"\"\"ML fit of wm, wp, bShort, bLong on the trials of one dataset.\"\"\"\n    from scipy.optimize import minimize\n    best = None\n    for wm0 in (0.08, 0.15):\n        x0 = np.array([wm0, 0.08, 0.0, 0.0])\n        res = minimize(lambda p: -bayes_loglik(p, df), x0, method=\"Nelder-Mead\",\n                       options=dict(xatol=1e-4, fatol=1e-3, maxiter=4000))\n        if best is None or res.fun < best.fun:\n            best = res\n    if not best.success:\n        raise RuntimeError(f\"Bayesian model fit failed: {best.message}\")\n    wm, wp, bS, bL = best.x\n    return dict(wm=wm, wp=wp, bShort=bS, bLong=bL, loglik=-best.fun)\n\n\ndef bayes_predict(ts: float, prior: str, p: dict):\n    \"\"\"Model mean and SD of tp, and mean te, for one ts.\"\"\"\n    tm, w = _tm_nodes(ts, p[\"wm\"])\n    te = te_of_tm(tm, prior, p[\"wm\"])\n    b = p[\"bShort\"] if prior == \"Short\" else p[\"bLong\"]\n    m = np.sum(w * (te + b))\n    second = np.sum(w * ((p[\"wp\"] * te) ** 2 + (te + b) ** 2))\n    return m, np.sqrt(second - m ** 2), np.sum(w * te)\n\n\ndef te_mean(t: np.ndarray, prior: str, wm: float) -> np.ndarray:\n    \"\"\"Mean Bayesian estimate for ts = t (no offset), integrating over tm.\"\"\"\n    out = []\n    for x in np.atleast_1d(t):\n        tm, w = _tm_nodes(x, wm)\n        out.append(np.sum(w * te_of_tm(tm, prior, wm)))\n    return np.array(out)\n\n\n# ---------------------------------------------------------------- regression helpers\n\ndef wls(y, x, w):\n    \"\"\"Weighted least squares y = a + b x. Returns a, b, fitted, weighted R2.\"\"\"\n    X = np.column_stack([np.ones_like(x), x])\n    W = np.asarray(w, float)\n    beta = np.linalg.solve(X.T @ (X * W[:, None]), X.T @ (W * y))\n    fit = X @ beta\n    ybar = np.sum(W * y) / np.sum(W)\n    r2 = 1 - np.sum(W * (y - fit) ** 2) / np.sum(W * (y - ybar) ** 2)\n    return beta[0], beta[1], fit, r2\n\n\n# ---------------------------------------------------------------- GPFA\n\ndef gpfa_fit(spikes, good_sub: pd.DataFrame, x_dims=(4, 8), n_folds=3, seed=0):\n    \"\"\"GPFA on single trials from Ready to Set (20 ms bins), units given by `spikes`.\n\n    The latent dimensionality is chosen from x_dims by n_folds-fold cross-validated\n    log-likelihood. Returns (chosen dim, cv log-likelihoods, list of orthonormalised latent\n    trajectories, each bins x dims, with bin j ending at 20(j+1) ms after Ready).\"\"\"\n    import neo\n    import quantities as pq\n    from elephant.gpfa import GPFA\n\n    def trains(sub):\n        out = []\n        for ready, ts in zip(sub.ready_time.values, sub.ts.values):\n            t1 = ready + ts / 1000.0\n            tr = []\n            for s in spikes:\n                i0, i1 = np.searchsorted(s, [ready, t1])\n                tr.append(neo.SpikeTrain((s[i0:i1] - ready) * pq.s, t_start=0 * pq.s,\n                                         t_stop=(t1 - ready) * pq.s))\n            out.append(tr)\n        return out\n\n    data = trains(good_sub)\n    rng = np.random.default_rng(seed)\n    order = rng.permutation(len(data))\n    folds = np.array_split(order, n_folds)\n    cv = {}\n    for d in x_dims:\n        ll = 0.0\n        for k in range(n_folds):\n            test = set(folds[k].tolist())\n            train = [data[i] for i in range(len(data)) if i not in test]\n            held = [data[i] for i in sorted(test)]\n            g = GPFA(bin_size=BIN * pq.ms, x_dim=d, verbose=False)\n            g.fit(train)\n            ll += g.score(held)\n        cv[d] = ll\n    best = max(cv, key=cv.get)\n    g = GPFA(bin_size=BIN * pq.ms, x_dim=best, verbose=False)\n    lat = g.fit_transform(data, returned_data=[\"latent_variable_orth\"])\n    return best, cv, [np.asarray(x).T for x in lat]\n"
}
```

```
File created successfully at: entries/sohn-2019/rsg.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && . $TMPDIR/env/bin/activate && python -c "
from elephant.gpfa import GPFA; print([m for m in dir(GPFA) if not m.startswith('_')])" && cat > $TMPDIR/t_gpfa.py <<'EOF'
import time, resource, numpy as np, rsg
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g); print(len(ui))
sp=[s['spikes'][i] for i in ui]
sub=g[g.dataset=='Hand Left']; print(len(sub))
t=time.time()
best,cv,lat=rsg.gpfa_fit(sp, sub, x_dims=(4,), n_folds=3)
print(best,cv,lat[0].shape, time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
python $TMPDIR/t_gpfa.py 2>&1 | grep -v Warn | tail -5
```

```
['fit', 'fit_transform', 'get_metadata_routing', 'get_params', 'score', 'set_fit_request', 'set_params', 'set_score_request', 'set_transform_request', 'transform']
Traceback (most recent call last):
  File "/tmp/claude-1001/t_gpfa.py", line 1, in <module>
    import time, resource, numpy as np, rsg
ModuleNotFoundError: No module named 'rsg'
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t_gpfa.py 2>&1 | grep -v Warn | tail -5
```

```
head.raise_for_status()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://dandiarchive.s3.amazonaws.com/blobs/73a/6f6/73a6f648-8e97-4c90-b323-a15844e4e3d4?response-content-disposition=attachment%3B%20filename%3D%22sub-Haydn_desc-train_ecephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261115%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261115T062442Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=6c6982fbc50e1a1b1f2e13413daea883022ea14ee5c6508063cc93baf991cd17
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sohn-2019/rsg.py",
 "old_string": "    head = requests.head(f\"{API}/assets/{hits[0]['asset_id']}/download/\", allow_redirects=True,\n                         timeout=60)\n    head.raise_for_status()\n    return head.url",
 "new_string": "    meta = requests.get(f\"{API}/assets/{hits[0]['asset_id']}/\", timeout=60)\n    meta.raise_for_status()\n    s3 = [u for u in meta.json()[\"contentUrl\"] if \"s3\" in u and \"amazonaws\" in u]\n    if not s3:\n        raise RuntimeError(f\"no S3 URL for {path}\")\n    return s3[0]"
}
```

```
The file entries/sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t_gpfa.py 2>&1 | grep -v Warn | tail -5
```

```
Fitting GPFA model...
Initializing parameters using factor analysis...

Fitting GPFA model...
4 {4: np.float64(-116182.8616193803)} (45, 4) 97.14993906021118 0.327308
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/proto1.py <<'EOF'
import time, numpy as np, pandas as pd, rsg, statsmodels.api as sm
from scipy import stats
t0=time.time()
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g); print(len(ui), time.time()-t0)
sp=[s['spikes'][i] for i in ui]
# beh-slopes
for (ds,prior),d in g.groupby(['dataset','prior']):
    v=d.groupby('ts').tp.var(); w=1/d.ts.map(v)
    m=sm.WLS(d.tp, sm.add_constant(d.ts), weights=w).fit(); ci=m.conf_int().loc['ts'].values
    m0=sm.WLS(d.tp, d.ts, weights=w).fit()
    print(ds,prior, round(m.params['ts'],3), np.round(ci,3), 'no-int', round(m0.params['ts'],3))
# bayes fits
t=time.time()
fits={}
for ds,d in g.groupby('dataset'):
    p=rsg.fit_bayes(d); fits[ds]=p
    ob=d.groupby(['prior','ts']).tp.agg(['mean','std']).reset_index()
    pr=np.array([rsg.bayes_predict(r.ts,r.prior,p)[:2] for r in ob.itertuples()])
    bo=ob['mean']-ob.ts; bp=pr[:,0]-ob.ts
    r2=1-np.sum((bo-bp)**2)/np.sum((bo-bo.mean())**2)
    print(ds, {k:round(v,3) for k,v in p.items()}, 'R2',round(r2,3),'r2corr',round(np.corrcoef(bo,bp)[0,1]**2,3),'sd r',round(np.corrcoef(ob['std'],pr[:,1])[0,1],3))
print('fit time', time.time()-t)
EOF
PYTHONPATH=. python $TMPDIR/proto1.py
```

```
48 1.7311365604400635
Eye Left Long 0.845 [0.743 0.948] no-int 0.996
Eye Left Short 1.011 [0.896 1.126] no-int 1.072
Eye Right Long 0.903 [0.769 1.038] no-int 1.027
Eye Right Short 1.11 [1.014 1.206] no-int 1.016
Hand Left Long 0.502 [0.369 0.636] no-int 0.923
Hand Left Short 0.612 [0.499 0.725] no-int 1.013
Hand Right Long 0.612 [0.488 0.736] no-int 1.032
Hand Right Short 0.861 [0.728 0.993] no-int 1.057
Eye Left {'wm': np.float64(0.032), 'wp': np.float64(0.11), 'bShort': np.float64(0.003), 'bLong': np.float64(-0.0), 'loglik': np.float64(-1546.132)} R2 -0.415 r2corr 0.139 sd r 0.814
Eye Right {'wm': np.float64(0.021), 'wp': np.float64(0.107), 'bShort': np.float64(0.001), 'bLong': np.float64(0.001), 'loglik': np.float64(-1620.644)} R2 -0.278 r2corr 0.156 sd r 0.905
Hand Left {'wm': np.float64(0.109), 'wp': np.float64(0.106), 'bShort': np.float64(-0.0), 'bLong': np.float64(-0.001), 'loglik': np.float64(-1313.852)} R2 0.349 r2corr 0.594 sd r 0.759
Hand Right {'wm': np.float64(0.089), 'wp': np.float64(0.113), 'bShort': np.float64(0.001), 'bLong': np.float64(-0.001), 'loglik': np.float64(-1357.332)} R2 -0.212 r2corr 0.845 sd r 0.271
fit time 4.7406439781188965
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sohn-2019/rsg.py",
 "old_string": "    from scipy.optimize import minimize\n    best = None\n    for wm0 in (0.08, 0.15):\n        x0 = np.array([wm0, 0.08, 0.0, 0.0])\n        res = minimize(lambda p: -bayes_loglik(p, df), x0, method=\"Nelder-Mead\",\n                       options=dict(xatol=1e-4, fatol=1e-3, maxiter=4000))\n        if best is None or res.fun < best.fun:\n            best = res\n    if not best.success:\n        raise RuntimeError(f\"Bayesian model fit failed: {best.message}\")\n    wm, wp, bS, bL = best.x",
 "new_string": "    from scipy.optimize import minimize\n\n    def unpack(z):  # log noise weights, offsets in units of 100 ms, so the simplex steps match\n        return np.exp(z[0]), np.exp(z[1]), 100 * z[2], 100 * z[3]\n\n    best = None\n    for wm0 in (0.05, 0.1, 0.2):\n        z0 = np.array([np.log(wm0), np.log(0.1), 0.2, 0.0])\n        res = minimize(lambda z: -bayes_loglik(unpack(z), df), z0, method=\"Nelder-Mead\",\n                       options=dict(xatol=1e-5, fatol=1e-4, maxiter=6000, maxfev=6000))\n        if best is None or res.fun < best.fun:\n            best = res\n    if not best.success or not np.isfinite(best.fun):\n        raise RuntimeError(f\"Bayesian model fit failed: {best.message}\")\n    wm, wp, bS, bL = unpack(best.x)"
}
```

```
The file entries/sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/proto1.py 2>&1 | tail -5
```

```
Eye Left {'wm': np.float64(0.025), 'wp': np.float64(0.103), 'bShort': np.float64(40.826), 'bLong': np.float64(1.693), 'loglik': np.float64(-1526.205)} R2 0.67 r2corr 0.678 sd r 0.807
Eye Right {'wm': np.float64(0.013), 'wp': np.float64(0.106), 'bShort': np.float64(6.397), 'bLong': np.float64(24.382), 'loglik': np.float64(-1616.147)} R2 0.122 r2corr 0.129 sd r 0.909
Hand Left {'wm': np.float64(0.116), 'wp': np.float64(0.09), 'bShort': np.float64(7.755), 'bLong': np.float64(-81.477), 'loglik': np.float64(-1288.994)} R2 0.978 r2corr 0.978 sd r 0.749
Hand Right {'wm': np.float64(0.073), 'wp': np.float64(0.104), 'bShort': np.float64(36.934), 'bLong': np.float64(50.362), 'loglik': np.float64(-1334.185)} R2 0.865 r2corr 0.869 sd r 0.277
fit time 29.526862621307373
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/env/bin/activate && cat > $TMPDIR/proto2.py <<'EOF'
import time, numpy as np, pandas as pd, rsg
from scipy import stats
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g)
sp=[s['spikes'][i] for i in ui]
fits={ds:rsg.fit_bayes(d) for ds,d in g.groupby('dataset')}
t=time.time()
rows=[]; spd=[]
for ds in g.dataset.unique():
    d=g[g.dataset==ds]
    est={}; 
    for prior in ['Short','Long']:
        dp=d[d.prior==prior]; est[prior]=rsg.estimation_rates(sp, dp, rsg.PRIOR_TS[prior][-1])
    Xe=np.vstack([est[p][0] for p in est]); mu,C,k,ev=rsg.pca_fit(Xe)
    prod={p:rsg.production_rates(sp,d,p) for p in ['Short','Long']}
    Xp=np.vstack([r for p in prod for r in prod[p].values()]); mup,Cp,kp,evp=rsg.pca_fit(Xp)
    print(ds,'k est',k,'k prod',kp)
    for prior in ['Short','Long']:
        R,ends,n=est[prior]; X=rsg.project(R,mu,C); tsv=rsg.PRIOR_TS[prior]
        u=rsg.encoding_axis(X,ends,tsv[0],tsv[-1])
        sel=(ends>=tsv[0])&(ends<=tsv[-1]); t_=ends[sel]; xu=X[sel]@u; w=n[sel]
        te=rsg.te_mean(t_,prior,fits[ds]['wm'])
        a,b,f,r2=rsg.wls(xu,te,w); a2,b2,f2,r2l=rsg.wls(xu,t_.astype(float),w)
        rm_b=np.sqrt(np.mean((xu-f)**2)); rm_l=np.sqrt(np.mean((xu-f2)**2))
        for ts in tsv:
            i=np.flatnonzero(ends==ts)[0]
            sp_=rsg.step_speed(rsg.project(prod[prior][ts],mup,Cp))
            mtp=d[(d.prior==prior)&(d.ts==ts)].tp.mean()
            spd.append((ds,prior,ts,X[i]@u,sp_,mtp))
        rows.append((ds,prior,r2,r2l,rm_b,rm_l,b2))
print(pd.DataFrame(rows,columns=['ds','prior','r2_te','r2_ts','rmse_b','rmse_l','slope_ts']))
S=pd.DataFrame(spd,columns=['ds','prior','ts','xu','speed','tp'])
for p,q in S.groupby('prior'):
    print(p, stats.pearsonr(q.xu,q.speed), stats.pearsonr(q.tp,q.speed))
print(S)
print(time.time()-t)
EOF
PYTHONPATH=. python $TMPDIR/proto2.py 2>&1 | tail -60
```

```
Sun Nov 15 06:27:42 UTC 2026
Hand Right k est 2 k prod 5
Hand Left k est 2 k prod 4
Eye Right k est 2 k prod 2
Eye Left k est 2 k prod 2
           ds  prior     r2_te     r2_ts    rmse_b    rmse_l  slope_ts
0  Hand Right  Short  0.973176  0.967017  0.727150  0.765171  0.046951
1  Hand Right   Long  0.994342  0.989671  0.400203  0.617787  0.048561
2   Hand Left  Short  0.995697  0.986827  0.659648  1.130395  0.077019
3   Hand Left   Long  0.977382  0.980815  0.582674  0.481294  0.027448
4   Eye Right  Short  0.957539  0.952457  3.222066  3.437276  0.190715
5   Eye Right   Long  0.970386  0.964697  2.923965  3.125385  0.117295
6    Eye Left  Short  0.908518  0.897877  6.358402  6.666802  0.229176
7    Eye Left   Long  0.986601  0.976310  1.803201  2.396004  0.123695
Long PearsonRResult(statistic=np.float64(-0.8740340379452237), pvalue=np.float64(4.759160787506469e-07)) PearsonRResult(statistic=np.float64(-0.7440457154736847), pvalue=np.float64(0.00016904786269921016))
Short PearsonRResult(statistic=np.float64(-0.9318555626832514), pvalue=np.float64(2.3460319655978386e-09)) PearsonRResult(statistic=np.float64(-0.719457862608176), pvalue=np.float64(0.0003494000238325113))
            ds  prior    ts         xu     speed           tp
0   Hand Right  Short   480   5.216094  6.017961   560.489190
1   Hand Right  Short   560   7.469991  5.279212   593.033886
2   Hand Right  Short   640  11.534317  5.064149   661.103500
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/proto3.py <<'EOF'
import time, numpy as np, pandas as pd, rsg, statsmodels.api as sm
from scipy import stats
import warnings; warnings.filterwarnings('ignore')
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g)
sp=[s['spikes'][i] for i in ui]
t=time.time()
# GLM
def windows(d, ends):
    rows=[]
    C=rsg.bin_counts(sp, d.ready_time.values, 0, max(ends), bin_ms=80) # bins [0,80)...; need windows ending at ends
    return None
def counts_at(d, ends):
    out=[]
    for e in ends:
        c=rsg.bin_counts(sp, d.ready_time.values, e-80, e, bin_ms=80)[:,0,:]
        ok=d.ts.values>=e
        df=pd.DataFrame({'time':e,'long':(d.prior=='Long').astype(int).values,'hand':(d.effector=='Hand').astype(int).values,'left':(d.direction=='Left').astype(int).values})
        out.append((df[ok], c[ok]))
    D=pd.concat([o[0] for o in out]); C=np.vstack([o[1] for o in out]); return D.reset_index(drop=True),C
def bic(y,X):
    m=sm.GLM(y,X,family=sm.families.Poisson()).fit(); return m.bic_llf if hasattr(m,'bic_llf') else m.bic
D,C=counts_at(g, rsg.SHORT_TS)
T=pd.get_dummies(D.time,prefix='t').astype(float)
Xf=pd.concat([T,D[['long','hand','left']]],axis=1); Xr=pd.concat([T,D[['hand','left']]],axis=1)
prior_dep=[bic(C[:,k],Xf)<bic(C[:,k],Xr) for k in range(C.shape[1])]
print('prior dep', np.mean(prior_dep), sum(prior_dep))
res={}
for reading in ['a','b']:
    tsdep=np.zeros(C.shape[1],bool)
    for prior in ['Short','Long']:
        d=g[g.prior==prior]
        ends=rsg.PRIOR_TS[prior] if reading=='a' else rsg.SHORT_TS
        D2,C2=counts_at(d,ends)
        T2=pd.get_dummies(D2.time,prefix='t').astype(float)
        X3=pd.concat([T2,D2[['hand','left']]],axis=1); X4=sm.add_constant(D2[['hand','left']].astype(float))
        tsdep|=np.array([bic(C2[:,k],X3)<bic(C2[:,k],X4) for k in range(C2.shape[1])])
    print(reading,'ts dep', tsdep.mean(), tsdep.sum())
print(time.time()-t)
EOF
PYTHONPATH=. python $TMPDIR/proto3.py 2>&1 | tail
```

```
prior dep 0.7916666666666666 38
a ts dep 0.4583333333333333 22
b ts dep 0.5 24
1.3751411437988281
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/proto4.py <<'EOF'
import time, numpy as np, pandas as pd, rsg
from scipy import stats
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g)
sp=[s['spikes'][i] for i in ui]
t=time.time()
# dfr
rng=np.random.default_rng(1)
edges=np.arange(-320,1441,160)
def rms_curve(perm=False):
    out=[]
    for ds in rsg.DATASETS:
        d=g[(g.dataset==' '.join(ds))&(g.ts==800)]
        C=rsg.bin_counts(sp,d.ready_time.values,-320,1440,bin_ms=160)/0.16
        lab=(d.prior=='Long').values
        if perm: lab=rng.permutation(lab)
        diff=C[lab].mean(0)-C[~lab].mean(0)
        out.append(np.sqrt((diff**2).mean(1)))
    return np.mean(out,0)
obs=rms_curve(); print(np.round(obs,2), edges[np.argmax(obs)])
null=[rms_curve(True).max() for _ in range(200)]; print('max',obs.max(),'p95',np.percentile(null,95))
# initial speed
rows=[]
for ds in rsg.DATASETS:
    d=g[g.dataset==' '.join(ds)]
    prod={p:rsg.production_rates(sp,d,p) for p in ['Short','Long']}
    Xp=np.vstack([r for p in prod for r in prod[p].values()]); mup,Cp,kp,_=rsg.pca_fit(Xp)
    for p in ['Short','Long']:
        ini=rsg.production_rates(sp,d,p,stop_ms=400)
        sv=np.array([rsg.step_speed(rsg.project(ini[ts],mup,Cp)) for ts in rsg.PRIOR_TS[p]])
        tsv=rsg.PRIOR_TS[p].astype(float)
        unb=sv[2]*tsv[2]/tsv
        rows.append((ds,p,stats.linregress(tsv,sv).slope,stats.linregress(tsv,unb).slope, np.round(sv,2)))
R=pd.DataFrame(rows,columns=['ds','p','meas','unb','sv']); print(R)
print(stats.wilcoxon(R.meas-R.unb))
# alt speed: full space
for p in ['Short','Long']:
    sl=[]
    for ds in rsg.DATASETS:
        d=g[(g.dataset==' '.join(ds))&(g.prior==p)]
        r,ends,n=rsg.estimation_rates(sp,d,rsg.PRIOR_TS[p][-1])
        v=np.linalg.norm(np.diff(r,axis=0),axis=1); te=ends[1:]
        sel=(te>rsg.PRIOR_TS[p][0])&(te<=rsg.PRIOR_TS[p][-1])
        sl.append(stats.linregress(te[sel],v[sel]).slope)
    print(p,np.round(sl,5),stats.wilcoxon(sl))
# transient
sl={'short':[], 'long':[]}
for ds in rsg.DATASETS:
    d=g[g.dataset==' '.join(ds)]
    tr={p:rsg.production_rates(sp,d,p,stop_ms=200) for p in ['Short','Long']}
    X=np.vstack([r for p in tr for r in tr[p].values()]); mu,C,k,_=rsg.pca_fit(X)
    for p in ['Short','Long']:
        tsv=rsg.PRIOR_TS[p]; mid=rsg.project(tr[p][tsv[2]],mu,C)
        for key,ts in [('short',tsv[0]),('long',tsv[-1])]:
            dist=np.linalg.norm(rsg.project(tr[p][ts],mu,C)-mid,axis=1)
            sl[key].append(stats.linregress(np.arange(len(dist))*20,dist).slope)
    print(ds,k)
for k_,v in sl.items(): print(k_,np.round(v,4),stats.wilcoxon(v))
# threshold
mins=[]
for ds in rsg.DATASETS:
    d=g[g.dataset==' '.join(ds)]
    tr={(p,ts):rsg.aligned_rates(sp,d[(d.prior==p)&(d.ts==ts)].go_time.values,-800,0) for p in ['Short','Long'] for ts in rsg.PRIOR_TS[p]}
    X=np.vstack(list(tr.values())); mu,C,k,_=rsg.pca_fit(X,0.60)
    for p in ['Short','Long']:
        tsv=rsg.PRIOR_TS[p]; mid=rsg.project(tr[(p,tsv[2])],mu,C)
        for ts in tsv[[0,1,3,4]]:
            dist=np.linalg.norm(rsg.project(tr[(p,ts)],mu,C)-mid,axis=1)
            mins.append(-800+20*np.argmin(dist)+20)
print('min times (bin end rel Go)', sorted(mins), np.median(mins))
print(time.time()-t)
EOF
PYTHONPATH=. python $TMPDIR/proto4.py 2>&1 | tail -40
```

```
[2.39 2.29 2.68 4.09 5.97 6.86 4.89 6.07 4.59 3.73 2.45] 480
max 6.861214 p95 3.1227858
              ds      p      meas       unb                              sv
0    (Eye, Left)  Short -0.008566 -0.012106  [8.55, 7.37, 7.33, 5.74, 5.94]
1    (Eye, Left)   Long -0.005620 -0.006749   [8.41, 7.25, 6.52, 6.25, 6.1]
2   (Eye, Right)  Short -0.008968 -0.011070   [7.6, 7.64, 6.71, 6.06, 4.81]
3   (Eye, Right)   Long -0.008232 -0.006542   [8.1, 7.04, 6.32, 5.66, 4.68]
4   (Hand, Left)  Short -0.006982 -0.007919    [6.1, 5.12, 4.8, 3.97, 3.88]
5   (Hand, Left)   Long -0.002274 -0.005079    [5.97, 4.6, 4.91, 4.87, 4.7]
6  (Hand, Right)  Short -0.004447 -0.008456  [6.02, 5.53, 5.12, 4.89, 4.56]
7  (Hand, Right)   Long -0.004819 -0.005403  [6.81, 5.67, 5.22, 4.63, 4.92]
WilcoxonResult(statistic=np.float64(4.0), pvalue=np.float64(0.0546875))
Short [ 0.00793  0.00295 -0.00141  0.00374] WilcoxonResult(statistic=np.float64(1.0), pvalue=np.float64(0.25))
Long [0.00025 0.00174 0.00366 0.00228] WilcoxonResult(statistic=np.float64(0.0), pvalue=np.float64(0.125))
('Eye', 'Left') 1
('Eye', 'Right') 2
('Hand', 'Left') 4
('Hand', 'Right') 3
short [-0.0643  0.0673 -0.0884  0.0623  0.0815  0.0992  0.0773  0.1082] WilcoxonResult(statistic=np.float64(8.0), pvalue=np.float64(0.1953125))
long [-0.0083  0.0089 -0.0154  0.0147 -0.003   0.0196 -0.034   0.0037] WilcoxonResult(statistic=np.float64(18.0), pvalue=np.float64(1.0))
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/proto5.py <<'EOF'
import numpy as np, pandas as pd, rsg
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g)
sp=[s['spikes'][i] for i in ui]
y=(g.direction=='Left').values
for shift in [0, 20, -20, 60]:
    C=rsg.bin_counts(sp, g.go_time.values+shift, -300, 100, bin_ms=400)[:,0,:]
    acc=cross_val_score(LogisticRegression(max_iter=2000), np.log1p(C), y, cv=5).mean()
    print('shift',shift,'dir acc',round(acc,3))
for shift in [0, 2.0]:
    R=rsg.bin_counts(sp, g.set_time.values+shift, -200, 400, bin_ms=50).mean(axis=(0,2))*20
    print('set psth', shift, np.round(R,2))
t=rsg.load_session(rsg.TEST_PATH)
print(t['trials'].columns.tolist(), len(t['trials']), len(t['units']), t['units'].heldout.sum())
# duplicates: does a test unit's spike pattern appear in train?
tid=t['units'].id.values; uid=s['units'].id.values
k=int(np.argmax(t['units'].n_spikes)); j=int(np.flatnonzero(uid==tid[k])[0])
ts_=t['spikes'][k]; tr_=s['spikes'][j]
isi_tr=np.round(np.diff(tr_),4)
hits=0
for i in range(0,len(ts_)-6,50):
    pat=np.round(np.diff(ts_[i:i+6]),4)
    w=np.lib.stride_tricks.sliding_window_view(isi_tr,5)
    hits+=np.any(np.all(w==pat,axis=1))
print('test unit',tid[k],'patterns tried',len(range(0,len(ts_)-6,50)),'found in train',hits)
print(t['trials'].head(3)); print(t['units'].head(3))
EOF
PYTHONPATH=. python $TMPDIR/proto5.py 2>&1 | tail -30
```

```
shift 0 dir acc 0.761
shift 20 dir acc 0.494
shift -20 dir acc 0.517
shift 60 dir acc 0.477
set psth 0 [ 9.9   9.88  9.73  9.7   9.62  9.71 11.73 13.62 12.54 11.54 10.66 10.14]
set psth 2.0 [6.1  6.13 6.09 6.1  6.1  6.07 6.11 6.21 6.17 6.21 6.31 6.4 ]
['id', 'start_time', 'stop_time', 'go_time', 'split'] 283 40 0
test unit 1104 patterns tried 234 found in train 0
   id  start_time  stop_time  go_time split
0   0         0.0        1.7      1.5  test
1   1         1.8        3.5      3.3  test
2   2         3.6        5.3      5.1  test
     id  heldout  observed_s  n_spikes       rate
0  1001    False       481.1      2591   5.385575
1  1002    False       481.1      6444  13.394305
2  1003    False       481.1      1039   2.159634
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/env/bin/activate && cat > $TMPDIR/proto6.py <<'EOF'
import time, resource, numpy as np, pandas as pd, rsg, warnings
warnings.filterwarnings('ignore')
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g)
sp=[s['spikes'][i] for i in ui]
t=time.time()
d=g[g.dataset=='Hand Left'].reset_index(drop=True)
best,cv,lat=rsg.gpfa_fit(sp,d,seed=0)
print(best,cv,time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
for p in ['Short','Long']:
    idx=np.flatnonzero(d.prior==p); tsv=rsg.PRIOR_TS[p]; nb=tsv[-1]//20
    L=np.full((len(idx),nb,best),np.nan)
    for r,i in enumerate(idx): L[r,:lat[i].shape[0]]=lat[i]
    avg=np.nanmean(L,0); ends=np.arange(20,tsv[-1]+1,20)
    u=rsg.encoding_axis(avg,ends,tsv[0],tsv[-1])
    xu=np.array([lat[i][-1]@u for i in idx]); tsi=d.ts.values[idx]
    z=(xu-xu.mean())/xu.std()
    var=np.array([z[tsi==x].var(ddof=1) for x in tsv]); m=np.array([xu[tsi==x].mean() for x in tsv])
    print(p, np.round(var,3), np.polyfit(tsv,var,2)[0], np.round(m,3))
EOF
PYTHONPATH=. python $TMPDIR/proto6.py 2>&1 | grep -v -i "fitting\|initializ" | tail
```

```
Sun Nov 15 06:29:34 UTC 2026







8 {4: np.float64(-116194.47730606451), 8: np.float64(-115587.76446387962)} 227.18195295333862 0.334024 GB
Short [0.81  1.246 0.894 0.399 0.845] -1.3786854368372113e-06 [-0.124 -0.172 -0.032  0.082  0.125]
Long [1.306 1.426 0.338 0.76  0.574] 6.412544555096476e-06 [-0.017  0.055  0.054  0.156  0.193]
```

**Agent calls Bash**

```bash
cd  && sed -n 80,200p tools/entry.py | grep -n "def \|sanity\|tag\|install" | head -30; python - <<'EOF'
import json
nb=json.load(open('entries/dana-2016/reproduce_dana_2016.ipynb'))
for c in nb['cells'][:6]:
    print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:600]); print('---')
EOF
```

```
1:    def error(self, where, message: str) -> None:
6:def dataset_id(record: dict) -> str | None:
15:def dataset_ids(record: dict) -> list[str]:
20:def claims_paths() -> list[Path]:
26:def claims_target(data: dict) -> tuple:
31:def lookup(index: dict, attempt: dict):
40:def schema(name: str) -> Draft202012Validator:
51:def _parsed(text: str):
59:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
65:def load(report: Report, path: Path):
73:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
82:def _plain(value):
93:def code_of(notebook_path: Path) -> str:
100:def check(entry_dir: Path) -> Report:
markdown {} # Dana et al. (2016), red calcium indicators: Figure 4 on CRCNS cai-2

Paper: Dana, Mohar, Sun et al. (2016), "Sensitive red protein calcium indicators for imaging
neural activity", eLife 5:e12727, doi:10.7554/elife.12727. The claims file
(`claims/dana-2016.yaml`) was written from the version of record (PMC4846379) with its Methods,
figure legends and Supplementary files 1 and 2.
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Sun Nov 15 06:33:48 UTC 2026
```

**Agent calls Bash**

```bash
cat >> entries/sohn-2019/rsg.py <<'EOF'


# ---------------------------------------------------------------- trial-averaged geometry

def dataset_geometry(spikes, d: pd.DataFrame, wm: float, smooth=True) -> dict:
    """Estimation and production trajectories, their PCA and the encoding-axis projections of
    one dataset (effector and direction). `wm` is the dataset's fitted measurement noise, used
    for te(t). Returns a dict with per-prior tables and the numbers of components."""
    est, out = {}, {"prior": {}}
    for prior in ("Short", "Long"):
        dp = d[d.prior == prior]
        est[prior] = estimation_rates(spikes, dp, PRIOR_TS[prior][-1], smooth=smooth)
    Xe = np.vstack([est[p][0] for p in est])
    mu, comps, k, ev = pca_fit(Xe)
    prod = {}
    for prior in ("Short", "Long"):
        tab = production_rates(spikes, d, prior)
        prod[prior] = tab if smooth else tab
    Xp = np.vstack([r for p in prod for r in prod[p].values()])
    mup, cp, kp, evp = pca_fit(Xp)
    out.update(k_est=k, k_prod=kp, ev_est=ev, ev_prod=evp, est_pca=(mu, comps),
               prod_pca=(mup, cp), est=est, prod=prod)
    for prior in ("Short", "Long"):
        R, ends, n = est[prior]
        X = project(R, mu, comps)
        tsv = PRIOR_TS[prior]
        u = encoding_axis(X, ends, tsv[0], tsv[-1])
        sel = (ends >= tsv[0]) & (ends <= tsv[-1])
        t = ends[sel].astype(float)
        xu = X[sel] @ u
        rows = []
        for ts in tsv:
            i = int(np.flatnonzero(ends == ts)[0])
            traj = project(prod[prior][ts], mup, cp)
            g = d[(d.prior == prior) & (d.ts == ts)]
            rows.append(dict(ts=ts, xu_set=float(X[i] @ u), speed=step_speed(traj),
                             duration_ms=len(traj) * BIN, mean_tp=g.tp.mean(), n_trials=len(g)))
        out["prior"][prior] = dict(X=X, ends=ends, n=n, u=u, t=t, xu=xu, w=n[sel],
                                   te=te_mean(t, prior, wm), per_ts=pd.DataFrame(rows))
    return out


def single_trial_speed(spikes, d: pd.DataFrame, prod_pca) -> np.ndarray:
    """Speed of each trial from Set to Go: smoothed single-trial rates (20 ms bins, SD 40 ms)
    projected into the dataset's production PC space, mean distance between successive bins."""
    mu, comps = prod_pca
    out = np.empty(len(d))
    for i, (st, tp) in enumerate(zip(d.set_time.values, d.tp.values)):
        stop = np.floor(tp / BIN) * BIN
        c = bin_counts(spikes, np.array([st]), 0, stop)[0] * (1000.0 / BIN)
        out[i] = step_speed(project(gauss_smooth(c), mu, comps))
    return out
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && python - <<'EOF'
p='rsg.py'; s=open(p).read()
s=s.replace('def production_rates(spikes, good_sub: pd.DataFrame, prior: str, stop_ms=None):','def production_rates(spikes, good_sub: pd.DataFrame, prior: str, stop_ms=None, smooth=True):')
s=s.replace('        out[ts] = aligned_rates(spikes, sub.set_time.values, 0, stop)','        out[ts] = aligned_rates(spikes, sub.set_time.values, 0, stop, smooth=smooth)')
s=s.replace('''        tab = production_rates(spikes, d, prior)
        prod[prior] = tab if smooth else tab''','''        prod[prior] = production_rates(spikes, d, prior, smooth=smooth)''')
open(p,'w').write(s)
EOF
grep -n "smooth=smooth" rsg.py
```

```
197:        out[ts] = aligned_rates(spikes, sub.set_time.values, 0, stop, smooth=smooth)
379:        est[prior] = estimation_rates(spikes, dp, PRIOR_TS[prior][-1], smooth=smooth)
384:        prod[prior] = production_rates(spikes, d, prior, smooth=smooth)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_main.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tag=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag]\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Sohn et al. (2019), Bayesian computation through cortical latent dynamics, on dandiset 000130\n\nPaper: Sohn, Narain, Meirhaeghe and Jazayeri (2019), \"Bayesian computation through cortical latent\ndynamics\", Neuron 103:934-947, doi:10.1016/j.neuron.2019.06.012. The claims file\n(`claims/sohn-2019.yaml`) was written from the accepted author manuscript in PubMed Central\n(PMC6805134): Results, figure legends and STAR Methods, without the supplementary tables.\n\nDataset: DANDI:000130 (\"DMFC_RSG\", prepared for the Neural Latents Benchmark), version\n**0.241017.1448**, the version this attempt was asked to use; it is also the most recent published\nversion, and the paper cites no version. Files are streamed from the archive with `remfile`; nothing\nis written to disk. The dataset holds one session (2016-12-11) of monkey H (Haydn): a train file with\nthe trial table and the spikes of 54 units, and a test file with 283 further trials whose task\nvariables are withheld.\n\nA \"dataset\" in the paper and here is one effector (Eye, Hand) and target direction (Left, Right): 4 in\nthis session, 8 in the paper (two animals). Loading and measures are in `rsg.py`, which says where each\nparameter comes from. The GPFA claims are in the second notebook, `gpfa_sohn_2019.ipynb`.\n\n| claim | tested here |\n|---|---|\n| beh-slopes, beh-overlap-prior, beh-sigmoid-increments, beh-long-more-bias, beh-bayes-model | tested |\n| glm-prior-ts, dfr-overlap-support, pca-dimensionality | tested |\n| encoding-r2, encoding-bayes-beats-linear, short-in-long-control, neural-long-more-bias | tested |\n| speed-vs-projection, initial-speed-biased, speed-predicts-tp | tested |\n| alt-speed-unmodulated, alt-transient-parallel, alt-threshold-monotonic | tested |\n| gpfa-variance-inverted-u, gpfa-mean-sigmoid | tested in `gpfa_sohn_2019.ipynb` |\n| rnn-curved-manifold, rnn-perturbation | blocked: the trained networks are not in the dataset nor public |\n| monkey-g | blocked: monkey G is not in the dataset |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nimport time, resource, warnings\nimport numpy as np\nimport pandas as pd\nimport yaml\nimport matplotlib.pyplot as plt\nimport statsmodels.api as sm\nfrom scipy import stats\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score\nimport rsg\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nT0 = time.time()\nDATASET = f\"dandi:{rsg.DANDISET}/{rsg.VERSION}\"\nCLAIMS = {c[\"id\"]: c for c in yaml.safe_load(open(\"../../claims/sohn-2019.yaml\"))[\"claims\"]}\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\n\n\ndef expected(cid):\n    return CLAIMS[cid].get(\"expected\", [])\n\n\ndef within(value, e):\n    return abs(value - e[\"value\"]) <= e[\"tolerance\"] + 1e-12\n\n\ndef quote(cid):\n    c = CLAIMS[cid]\n    print(f\"[{cid}] {c['statement']}\\nCriterion: {c.get('criterion', '(none)')}\")\n    for e in expected(cid):\n        print(f\"  expected {e['quantity']}: {e['value']} +- {e['tolerance']}\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nThe file list and metadata of the pinned version, then every column of the trial and unit tables of\nboth files.\n\"\"\")\n\ncode(r\"\"\"\nassets = rsg.list_assets()\nprint(DATASET)\nprint(assets.to_string())\nsess = rsg.load_session(rsg.TRAIN_PATH)\ntest = rsg.load_session(rsg.TEST_PATH)\nnwb = sess[\"nwb\"]\nprint(\"\\nsession:\", nwb.session_id, nwb.session_start_time, \"|\", nwb.session_description)\nprint(\"subject:\", nwb.subject.subject_id, nwb.subject.species, nwb.subject.age, nwb.subject.sex)\nprint(\"related publications:\", list(nwb.related_publications))\nprint(\"\\ntrial table columns and descriptions (train file):\")\nfor c in nwb.trials.colnames:\n    print(f\"  {c}: {nwb.trials[c].description}\")\nprint(\"unit table columns:\", sess[\"nwb\"].units.colnames)\nel = nwb.electrodes.to_dataframe()\nprint(\"electrodes:\", len(el), \"in groups\", el.group_name.value_counts().to_dict(),\n      \"| location\", el.location.unique(), \"| x, y, z all NaN:\", bool(el[[\"x\", \"y\", \"z\"]].isna().all().all()))\nprint(\"acquisition:\", list(nwb.acquisition), \"| processing:\", list(nwb.processing))\nprint(\"\\ntest file trial columns:\", test[\"trials\"].columns.tolist(), \"|\", len(test[\"trials\"]), \"trials,\",\n      len(test[\"units\"]), \"units (\", int(test[\"units\"].heldout.sum()), \"held out )\")\n\"\"\")\n\ncode(r\"\"\"\ntr = rsg.label_trials(sess[\"trials\"])\ngood = rsg.good_trials(sess[\"trials\"])\nunits = sess[\"units\"]\nui = rsg.select_units(sess, good)\nspikes = [sess[\"spikes\"][i] for i in ui]\n\nprint(\"== trials (train file)\")\nprint(\"all:\", len(tr), \"| split:\", tr.split.value_counts().to_dict())\nprint(\"with Ready:\", tr.ready_time.notna().sum(), \"| with Set:\", tr.set_time.notna().sum(),\n      \"| with Go:\", tr.go_time.notna().sum(), \"| tp <= 0:\", int((tr.tp <= 0).sum()),\n      \"| is_outlier:\", int(tr.is_outlier.sum()))\nprint(\"completed (Set and Go, tp > 0):\", int((tr.set_time.notna() & tr.go_time.notna() & (tr.tp > 0)).sum()),\n      \"| of them flagged is_outlier:\", int((tr.set_time.notna() & tr.go_time.notna() & (tr.tp > 0) & tr.is_outlier).sum()),\n      \"| analysed (completed, not outlier):\", len(good))\nprint(\"\\nanalysed trials by dataset, prior and ts:\")\nprint(pd.crosstab([good.effector, good.direction, good.prior], good.ts))\nprint(\"fewest analysed trials in any of the 40 conditions:\",\n      good.groupby([\"prior\", \"ts\", \"effector\", \"direction\"]).size().min())\n\nprint(\"\\n== ranges and units of the variables used\")\nfor c, unit in [(\"ts\", \"ms\"), (\"tp\", \"ms\")]:\n    print(f\"{c} ({unit}): {good[c].min():.1f} to {good[c].max():.1f}; ts values {sorted(good.ts.unique())}\" if c == \"ts\"\n          else f\"{c} ({unit}): {good[c].min():.1f} to {good[c].max():.1f}\")\nprint(\"theta values:\", sorted(tr.theta.unique()), \"| is_short x iti (ms):\")\nprint(pd.crosstab(tr.is_short, tr.iti))\ndts = (good.set_time - good.ready_time) * 1000 - good.ts\ndtp = (good.go_time - good.set_time) * 1000 - good.tp\nprint(\"(set_time - ready_time) in ms minus ts: median %.1f, 1st to 99th percentile %.1f to %.1f, range %.1f to %.1f\"\n      % (dts.median(), *np.percentile(dts, [1, 99]), dts.min(), dts.max()))\nprint(\"(go_time - set_time) in ms minus tp:    median %.1f, 1st to 99th percentile %.1f to %.1f, range %.1f to %.1f\"\n      % (dtp.median(), *np.percentile(dtp, [1, 99]), dtp.min(), dtp.max()))\n\nprint(\"\\n== units\")\nprint(\"train file:\", len(units), \"units,\", int(units.heldout.sum()), \"flagged heldout; observed\",\n      f\"{units.observed_s.iloc[0]:.1f} s in\", len(sess[\"obs\"][0]), \"intervals:\", np.round(sess[\"obs\"][0], 1).tolist())\nprint(\"all units share the same observation intervals:\", all(np.array_equal(o, sess[\"obs\"][0]) for o in sess[\"obs\"]))\nprint(\"spike times sorted in every unit:\", all(np.all(np.diff(s) >= 0) for s in sess[\"spikes\"]))\nprint(\"mean rates (spikes/s): %.2f to %.2f; units >= 1 spike/s: %d\" % (units.rate.min(), units.rate.max(), (units.rate >= 1).sum()))\nprint(\"units selected (>= 1 spike/s and >= 5 trials in each of the 40 conditions):\", len(ui))\nprint(\"test file:\", len(test[\"units\"]), \"units, ids a subset of the train file's:\",\n      set(test[\"units\"].id) <= set(units.id), \"| observed\", f\"{test['units'].observed_s.iloc[0]:.1f} s\")\n\"\"\", tag=\"sanity\")\n\nmd(r\"\"\"\n### Recordings deposited twice\n\nThe test file's trials could repeat segments of the train file. For the test unit with the most spikes,\nevery 50th run of five successive inter-spike intervals is searched for in the same unit's train-file\nspike train (to 0.1 ms).\n\"\"\")\n\ncode(r\"\"\"\ntid = test[\"units\"].id.values\nk = int(np.argmax(test[\"units\"].n_spikes.values))\nj = int(np.flatnonzero(units.id.values == tid[k])[0])\nisi_train = np.round(np.diff(sess[\"spikes\"][j]), 4)\nwindows = np.lib.stride_tricks.sliding_window_view(isi_train, 5)\nstarts = range(0, len(test[\"spikes\"][k]) - 6, 50)\nfound = sum(bool(np.any(np.all(windows == np.round(np.diff(test[\"spikes\"][k][i:i + 6]), 4), axis=1))) for i in starts)\nprint(f\"unit {tid[k]}: {len(starts)} test-file patterns searched, {found} found in the train file\")\ngaps = [(a[1], b[0]) for a, b in zip(sess[\"obs\"][0][:-1], sess[\"obs\"][0][1:])]\nprint(\"gaps between the train file's observation intervals (s):\", [round(b - a, 3) for a, b in gaps])\nprint(\"test-file trials: start\", test[\"trials\"].start_time.min(), \"to\", test[\"trials\"].stop_time.max(),\n      \"s, each\", np.unique(np.round(test[\"trials\"].stop_time - test[\"trials\"].start_time, 3)), \"s long, Go at\",\n      np.unique(np.round(test[\"trials\"].go_time - test[\"trials\"].start_time, 3)), \"s\")\n\"\"\")\n\nmd(r\"\"\"\n### Do spikes share the clock of the trial table?\n\nTwo checks. The target direction is randomised trial by trial (Methods, \"Trial structure\"), so it can\nbe decoded from spike counts around Go only when the spikes and the trial times share a clock; with the\ntrial times shifted by 20 s or more, the labels belong to other trials and decoding falls to chance.\nSecond, the population rate around Set, at the true times and 2 s later.\n\"\"\")\n\ncode(r\"\"\"\ny = (good.direction == \"Left\").values\nfor shift in [0.0, 20.0, -20.0, 60.0]:\n    C = rsg.bin_counts(spikes, good.go_time.values + shift, -300, 100, bin_ms=400)[:, 0, :]\n    acc = cross_val_score(LogisticRegression(max_iter=2000), np.log1p(C), y, cv=5).mean()\n    print(f\"direction decoded from counts Go-300 to Go+100 ms, times shifted by {shift:+.0f} s: accuracy {acc:.3f} (chance {max(y.mean(), 1 - y.mean()):.3f})\")\nfor name, col in [(\"Set\", \"set_time\"), (\"Ready\", \"ready_time\")]:\n    for shift in [0.0, 2.0]:\n        R = rsg.bin_counts(spikes, good[col].values + shift, -200, 400, bin_ms=50).mean(axis=(0, 2)) * 20\n        print(f\"mean rate around {name} (+{shift:.0f} s), 50 ms bins from -200 ms (spikes/s):\", np.round(R, 2))\n\"\"\")\n\n# ------------------------------------------------------------------ behaviour\nmd(\"## Behaviour\")\n\nmd(\"### beh-slopes\")\ncode(r\"\"\"\nquote(\"beh-slopes\")\n\n\ndef slopes(intercept=True):\n    rows = []\n    for (ds, prior), d in good.groupby([\"dataset\", \"prior\"]):\n        w = 1.0 / d.ts.map(d.groupby(\"ts\").tp.var())\n        X = sm.add_constant(d.ts.astype(float)) if intercept else d.ts.astype(float)\n        m = sm.WLS(d.tp.values, X, weights=w.values).fit()\n        lo, hi = m.conf_int().loc[\"ts\"].values\n        rows.append(dict(dataset=ds, prior=prior, slope=m.params[\"ts\"], ci_lo=lo, ci_hi=hi, n=len(d)))\n    return pd.DataFrame(rows)\n\n\nSLOPES = {\"with intercept\": slopes(True), \"through the origin\": slopes(False)}\nfor name, s in SLOPES.items():\n    s[\"in_0_1\"] = (s.slope > 0) & (s.slope < 1)\n    s[\"ci_excludes_0_1\"] = (s.ci_lo > 0) & (s.ci_hi < 1)\n    print(f\"\\nreading: tp = a + b ts ({name})\" if name == \"with intercept\" else f\"\\nreading: tp = b ts ({name}, the Methods' equation)\")\n    print(s.round(3).to_string(index=False))\n    print(f\"slopes in (0, 1): {s.in_0_1.sum()} of 8; intervals excluding 0 and 1: {s.ci_excludes_0_1.sum()} of 8\")\n\"\"\", tag=\"claim:beh-slopes\")\n\nmd(r\"\"\"\nThe criterion's regression has an intercept in the main reading; the Methods write `tp = beta ts + e`,\nrun as the second reading. Under both, the Eye Short slopes are at or above 1.\n\n**Result: not reproduced.** With an intercept, 6 of 8 slopes lie between 0 and 1; the Eye Left Short\n(1.011) and Eye Right Short (1.110) slopes do not, and only 4 of the 8 intervals exclude both 0 and 1.\nThrough the origin, 3 of 8 slopes are below 1. The Hand slopes (0.50 to 0.86) are below 1 with\nintervals that exclude 1.\n\"\"\")\n\nmd(\"### beh-overlap-prior\")\ncode(r\"\"\"\nquote(\"beh-overlap-prior\")\no = good[good.ts == 800]\nfor prior in [\"Short\", \"Long\"]:\n    x = o[o.prior == prior].tp - 800\n    print(f\"{prior}: n = {len(x)}, median tp - 800 = {x.median():.1f} ms, mean {x.mean():.1f} ms\")\np_all = stats.ranksums(o[o.prior == \"Short\"].tp, o[o.prior == \"Long\"].tp)\nprint(f\"rank-sum Short vs Long, pooled: z = {p_all.statistic:.2f}, p = {p_all.pvalue:.2e}\")\nfor ds, d in o.groupby(\"dataset\"):\n    a, b = d[d.prior == \"Short\"].tp, d[d.prior == \"Long\"].tp\n    r = stats.ranksums(a, b)\n    print(f\"  {ds}: Short median {a.median() - 800:+.1f}, Long median {b.median() - 800:+.1f} ms (n {len(a)}, {len(b)}); p = {r.pvalue:.3g}\")\n\"\"\", tag=\"claim:beh-overlap-prior\")\nmd(r\"\"\"\n**Result: reproduced.** At ts = 800 ms the median tp - 800 is +2.4 ms for Short and +36.6 ms for Long\nin this session, so the Short median is not negative; the criterion asks for a negative Short median.\n\"\"\")\n\nmd(\"### beh-sigmoid-increments\")\ncode(r\"\"\"\nquote(\"beh-sigmoid-increments\")\nrows = []\nfor (ds, prior), d in good.groupby([\"dataset\", \"prior\"]):\n    m = d.groupby(\"ts\").tp.mean().values\n    inc = np.diff(m)\n    rows.append(dict(dataset=ds, prior=prior, increments=np.round(inc, 1).tolist(),\n                     extreme=(inc[0] + inc[3]) / 2, middle=(inc[1] + inc[2]) / 2))\nINC = pd.DataFrame(rows)\nINC[\"middle_minus_extreme\"] = INC.middle - INC.extreme\nprint(INC.round(1).to_string(index=False))\nw = stats.wilcoxon(INC.middle, INC.extreme)\nprint(f\"middle > extreme in {int((INC.middle > INC.extreme).sum())} of 8; two-sided signed-rank p = {w.pvalue:.4f}\")\n\"\"\", tag=\"claim:beh-sigmoid-increments\")\nmd(\"**Result: ...**\")\n\nmd(\"### beh-long-more-bias\")\ncode(r\"\"\"\nquote(\"beh-long-more-bias\")\nfor name, s in SLOPES.items():\n    p = s.pivot(index=\"dataset\", columns=\"prior\", values=\"slope\")\n    p[\"Long_below_Short\"] = p.Long < p.Short\n    print(f\"\\n{name}:\")\n    print(p.round(3).to_string())\n    print(f\"Long slope below Short in {int(p.Long_below_Short.sum())} of 4 datasets\")\n\"\"\", tag=\"claim:beh-long-more-bias\")\nmd(\"**Result: ...**\")\n\nmd(\"### beh-bayes-model\")\ncode(r\"\"\"\nquote(\"beh-bayes-model\")\nt = time.time()\nFITS = {ds: rsg.fit_bayes(d) for ds, d in good.groupby(\"dataset\")}\nprint(f\"fits took {time.time() - t:.0f} s\")\nrows, pred_rows = [], []\nfor ds, d in good.groupby(\"dataset\"):\n    p = FITS[ds]\n    ob = d.groupby([\"prior\", \"ts\"]).tp.agg([\"mean\", \"std\", \"size\"]).reset_index()\n    pr = np.array([rsg.bayes_predict(r.ts, r.prior, p)[:2] for r in ob.itertuples()])\n    bias_o, bias_p = ob[\"mean\"] - ob.ts, pr[:, 0] - ob.ts\n    r2 = 1 - np.sum((bias_o - bias_p) ** 2) / np.sum((bias_o - bias_o.mean()) ** 2)\n    rsd = stats.pearsonr(ob[\"std\"], pr[:, 1])\n    rows.append(dict(dataset=ds, wm=p[\"wm\"], wp=p[\"wp\"], bShort=p[\"bShort\"], bLong=p[\"bLong\"],\n                     bias_R2=r2, bias_r_squared=stats.pearsonr(bias_o, bias_p)[0] ** 2,\n                     sd_r=rsd[0], sd_p=rsd[1], bias_range_ms=np.ptp(bias_o)))\n    for r, b, q in zip(ob.itertuples(), bias_p, pr[:, 1]):\n        pred_rows.append(dict(dataset=ds, prior=r.prior, ts=r.ts, n=r._5 if hasattr(r, \"_5\") else r.size,\n                              bias_obs=r.mean - r.ts, bias_model=b, sd_obs=r.std, sd_model=q))\nBAYES = pd.DataFrame(rows)\nprint(BAYES.round(3).to_string(index=False))\nprint(f\"bias R2 >= 0.8 in {int((BAYES.bias_R2 >= 0.8).sum())} of 4 (squared correlation >= 0.8 in {int((BAYES.bias_r_squared >= 0.8).sum())}); \"\n      f\"SD correlation positive in {int((BAYES.sd_r > 0).sum())} of 4\")\nprint(pd.DataFrame(pred_rows).round(1).to_string(index=False))\n\"\"\", tag=\"claim:beh-bayes-model\")\nmd(r\"\"\"\n\"R2 of the observed mean bias by the model's predicted bias\" is read as 1 - SS_res / SS_tot of the\nobserved biases around the predictions; the squared Pearson correlation is shown as the second reading.\n\n**Result: ...**\n\"\"\")\n\n# ------------------------------------------------------------------ single neurons\nmd(\"## Single neurons\")\nmd(r\"\"\"\n### glm-prior-ts\n\nCounts in the 80 ms before each of the Short prior's ts values, with attrition. For ts dependence the\ncriterion gives each prior \"that prior's 5 time indicators\". Reading (a): for the Long prior, windows\nending at the Long prior's ts values (800 to 1200 ms), as the Methods' \"Since values of ts were\ndifferent between the priors, we used two distinct GLMs\" suggests; reading (b): the same five windows\n(480 to 800 ms) in both priors.\n\"\"\")\ncode(r\"\"\"\nquote(\"glm-prior-ts\")\n\n\ndef window_counts(d, ends):\n    D, C = [], []\n    for e in ends:\n        c = rsg.bin_counts(spikes, d.ready_time.values, e - 80, e, bin_ms=80)[:, 0, :]\n        ok = d.ts.values >= e\n        D.append(pd.DataFrame({\"time\": e, \"long\": (d.prior == \"Long\").astype(float).values,\n                               \"hand\": (d.effector == \"Hand\").astype(float).values,\n                               \"left\": (d.direction == \"Left\").astype(float).values})[ok])\n        C.append(c[ok])\n    return pd.concat(D, ignore_index=True), np.vstack(C)\n\n\ndef bic(y, X):\n    return sm.GLM(y, X, family=sm.families.Poisson()).fit().bic_llf\n\n\ndef binom_ci(k, n):\n    lo = stats.beta.ppf(0.025, k, n - k + 1) if k > 0 else 0.0\n    hi = stats.beta.ppf(0.975, k + 1, n - k) if k < n else 1.0\n    return 100 * lo, 100 * hi\n\n\nD, C = window_counts(good, rsg.SHORT_TS)\nT = pd.get_dummies(D.time, prefix=\"t\").astype(float)\nfull = pd.concat([T, D[[\"long\", \"hand\", \"left\"]]], axis=1)\nred = pd.concat([T, D[[\"hand\", \"left\"]]], axis=1)\nprior_dep = np.array([bic(C[:, k], full) < bic(C[:, k], red) for k in range(C.shape[1])])\nprint(f\"observations per unit (trial x window, with attrition): {len(D)}\")\nnU = len(prior_dep)\nGLM = {}\nfor reading in [\"a\", \"b\"]:\n    ts_dep = np.zeros(nU, bool)\n    for prior in [\"Short\", \"Long\"]:\n        d = good[good.prior == prior]\n        ends = rsg.PRIOR_TS[prior] if reading == \"a\" else rsg.SHORT_TS\n        D2, C2 = window_counts(d, ends)\n        T2 = pd.get_dummies(D2.time, prefix=\"t\").astype(float)\n        X3 = pd.concat([T2, D2[[\"hand\", \"left\"]]], axis=1)\n        X4 = sm.add_constant(D2[[\"hand\", \"left\"]])\n        ts_dep |= np.array([bic(C2[:, k], X3) < bic(C2[:, k], X4) for k in range(nU)])\n    GLM[reading] = ts_dep\ne_prior, e_ts = expected(\"glm-prior-ts\")\nfp = 100 * prior_dep.mean()\nprint(f\"prior-dependent: {prior_dep.sum()} of {nU} = {fp:.1f}% (95% CI {binom_ci(prior_dep.sum(), nU)[0]:.1f} to {binom_ci(prior_dep.sum(), nU)[1]:.1f}); \"\n      f\"expected {e_prior['value']} +- {e_prior['tolerance']}: within {within(fp, e_prior)}\")\nfor reading, ts_dep in GLM.items():\n    f = 100 * ts_dep.mean()\n    lo, hi = binom_ci(ts_dep.sum(), nU)\n    print(f\"ts-dependent, reading ({reading}): {ts_dep.sum()} of {nU} = {f:.1f}% (95% CI {lo:.1f} to {hi:.1f}); \"\n          f\"expected {e_ts['value']} +- {e_ts['tolerance']}: within {within(f, e_ts)}\")\nprint(\"both prior- and ts-dependent (a):\", int((prior_dep & GLM['a']).sum()), \"| neither:\", int((~prior_dep & ~GLM['a']).sum()))\n\"\"\", tag=\"claim:glm-prior-ts\")\nmd(\"**Result: ...**\")\n\nmd(\"### dfr-overlap-support\")\ncode(r\"\"\"\nquote(\"dfr-overlap-support\")\nEDGES = np.arange(-320, 1441, 160)\nrng = np.random.default_rng(2019)\no800 = {ds: good[(good.dataset == ds) & (good.ts == 800)] for ds in good.dataset.unique()}\ncounts800 = {ds: rsg.bin_counts(spikes, d.ready_time.values, -320, 1440, bin_ms=160) / 0.16 for ds, d in o800.items()}\n\n\ndef rms_curve(shuffle=False):\n    out = []\n    for ds, d in o800.items():\n        lab = (d.prior == \"Long\").values\n        if shuffle:\n            lab = rng.permutation(lab)\n        diff = counts800[ds][lab].mean(0) - counts800[ds][~lab].mean(0)\n        out.append(np.sqrt((diff ** 2).mean(axis=1)))\n    return np.array(out)\n\n\nper_ds = rms_curve()\nobs = per_ds.mean(0)\nnull = np.array([rms_curve(True).mean(0).max() for _ in range(200)])\nprint(\"trials at ts = 800 (Short, Long):\", {ds: [int((d.prior == p).sum()) for p in [\"Short\", \"Long\"]] for ds, d in o800.items()})\ntab = pd.DataFrame(per_ds.T, columns=list(o800), index=[f\"{a} to {b}\" for a, b in zip(EDGES[:-1], EDGES[1:])])\ntab[\"mean\"] = obs\nprint(\"RMS over units of the Long - Short rate difference (spikes/s), by 160 ms bin after Ready:\")\nprint(tab.round(2).to_string())\ni = int(np.argmax(obs))\nprint(f\"largest mean RMS {obs[i]:.2f} spikes/s in bin {EDGES[i]} to {EDGES[i + 1]} ms; \"\n      f\"95th percentile of the shuffled maximum {np.percentile(null, 95):.2f} (range {null.min():.2f} to {null.max():.2f})\")\nprint(\"largest bin within 480 to 800 ms:\", EDGES[i] >= 480 and EDGES[i + 1] <= 800)\n\"\"\", tag=\"claim:dfr-overlap-support\")\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ population\nmd(r\"\"\"\n## Population trajectories\n\nPer dataset: estimation-epoch trajectories (Ready to the prior's longest ts, attrition) and\nproduction-epoch trajectories (Set to the shortest tp of each ts), PCA per epoch on both priors, and the\nencoding axis of each prior. Each dataset uses its own Bayesian fit (beh-bayes-model) for te(t).\n\"\"\")\ncode(r\"\"\"\nGEO = {ds: rsg.dataset_geometry(spikes, good[good.dataset == ds], FITS[ds][\"wm\"]) for ds in sorted(good.dataset.unique())}\nfor ds, g in GEO.items():\n    print(ds, \"| production windows (ms):\", {p: g[\"prior\"][p][\"per_ts\"].duration_ms.tolist() for p in [\"Short\", \"Long\"]})\n\"\"\")\n\nmd(\"### pca-dimensionality\")\ncode(r\"\"\"\nquote(\"pca-dimensionality\")\nrows = []\nfor ds, g in GEO.items():\n    rows.append(dict(dataset=ds, k_estimation=g[\"k_est\"], cum_var_est=np.round(np.cumsum(g[\"ev_est\"])[:5], 3).tolist(),\n                     k_production=g[\"k_prod\"], cum_var_prod=np.round(np.cumsum(g[\"ev_prod\"])[:12], 3).tolist()))\nPCA = pd.DataFrame(rows)\nprint(PCA.to_string(index=False))\nn_in = int(PCA.k_estimation.between(3, 4).sum() + PCA.k_production.between(5, 11).sum())\nprint(f\"estimation in 3 to 4: {int(PCA.k_estimation.between(3, 4).sum())} of 4; production in 5 to 11: \"\n      f\"{int(PCA.k_production.between(5, 11).sum())} of 4; total {n_in} of 8\")\nfor ds, g in GEO.items():\n    print(f\"{ds}: variance of 3 and 4 estimation PCs {np.cumsum(g['ev_est'])[2]:.3f}, {np.cumsum(g['ev_est'])[3]:.3f}\")\n\"\"\", tag=\"claim:pca-dimensionality\")\nmd(\"**Result: ...**\")\n\nmd(\"### encoding-r2\")\ncode(r\"\"\"\nquote(\"encoding-r2\")\nrng = np.random.default_rng(4)\nrows = []\nfor ds, g in GEO.items():\n    for prior in [\"Short\", \"Long\"]:\n        q = g[\"prior\"][prior]\n        a, b, fit_te, r2_te = rsg.wls(q[\"xu\"], q[\"te\"], q[\"w\"])\n        a2, b2, fit_ts, r2_ts = rsg.wls(q[\"xu\"], q[\"t\"], q[\"w\"])\n        sel = (q[\"ends\"] >= q[\"t\"][0]) & (q[\"ends\"] <= q[\"t\"][-1])\n        V = rng.normal(size=(1000, q[\"X\"].shape[1]))\n        V /= np.linalg.norm(V, axis=1, keepdims=True)\n        r2_rand = np.array([rsg.wls(q[\"X\"][sel] @ v, q[\"te\"], q[\"w\"])[3] for v in V])\n        rows.append(dict(dataset=ds, prior=prior, n_points=len(q[\"t\"]), k=q[\"X\"].shape[1], R2_te=r2_te, R2_ts=r2_ts,\n                         rand_median=np.median(r2_rand), rand_95=np.percentile(r2_rand, 95),\n                         frac_rand_ge=np.mean(r2_rand >= r2_te)))\nENC = pd.DataFrame(rows)\nprint(ENC.round(4).to_string(index=False))\neS, eL = expected(\"encoding-r2\")\nhl = ENC[ENC.dataset == \"Hand Left\"].set_index(\"prior\").R2_te\nmean = ENC.groupby(\"prior\").R2_te.mean()\nfor name, v in [(\"(a) Hand Left\", hl), (\"(b) mean of 4 datasets\", mean)]:\n    print(f\"{name}: Short {v['Short']:.4f} (within {within(v['Short'], eS)}), Long {v['Long']:.4f} (within {within(v['Long'], eL)})\")\n\"\"\", tag=\"claim:encoding-r2\")\ncode(r\"\"\"\nfig, axes = plt.subplots(2, 4, figsize=(14, 6))\nfor j, (ds, g) in enumerate(GEO.items()):\n    for i, prior in enumerate([\"Short\", \"Long\"]):\n        q = g[\"prior\"][prior]\n        a, b, fit, r2 = rsg.wls(q[\"xu\"], q[\"te\"], q[\"w\"])\n        ax = axes[i, j]\n        ax.plot(q[\"t\"], q[\"xu\"], \"o\", ms=3, color=\"C3\" if prior == \"Short\" else \"C0\")\n        ax.plot(q[\"t\"], fit, \"k-\", lw=1)\n        ax.set_title(f\"{ds} {prior}: R2 {r2:.3f}\", fontsize=9)\n        ax.set_xlabel(\"time after Ready (ms)\")\n        print(f\"{ds} {prior}: Xu from {q['xu'].min():.2f} to {q['xu'].max():.2f} spikes/s (all points shown)\")\naxes[0, 0].set_ylabel(\"Xu (spikes/s)\")\nplt.tight_layout()\nplt.show()\n\"\"\", tag=\"claim:encoding-r2\")\nmd(\"**Result: ...**\")\n\nmd(\"### encoding-bayes-beats-linear\")\ncode(r\"\"\"\nquote(\"encoding-bayes-beats-linear\")\nrows = []\nfor ds, g in GEO.items():\n    for prior in [\"Short\", \"Long\"]:\n        q = g[\"prior\"][prior]\n        _, _, f_te, _ = rsg.wls(q[\"xu\"], q[\"te\"], q[\"w\"])\n        _, _, f_ts, _ = rsg.wls(q[\"xu\"], q[\"t\"], q[\"w\"])\n        w = q[\"w\"] / q[\"w\"].sum()\n        rows.append(dict(dataset=ds, prior=prior,\n                         rmse_bayes=np.sqrt(np.mean((q[\"xu\"] - f_te) ** 2)), rmse_linear=np.sqrt(np.mean((q[\"xu\"] - f_ts) ** 2)),\n                         wrmse_bayes=np.sqrt(np.sum(w * (q[\"xu\"] - f_te) ** 2)), wrmse_linear=np.sqrt(np.sum(w * (q[\"xu\"] - f_ts) ** 2))))\nRM = pd.DataFrame(rows)\nRM[\"delta\"] = RM.rmse_bayes - RM.rmse_linear\nRM[\"w_delta\"] = RM.wrmse_bayes - RM.wrmse_linear\nprint(RM.round(3).to_string(index=False))\nfor prior in [\"Short\", \"Long\"]:\n    r = RM[RM.prior == prior]\n    print(f\"{prior}: Bayesian RMSE lower in {int((r.delta < 0).sum())} of 4 (weighted RMSE: {int((r.w_delta < 0).sum())} of 4); \"\n          f\"signed-rank p = {stats.wilcoxon(r.delta).pvalue:.3f}\")\n\"\"\", tag=\"claim:encoding-bayes-beats-linear\")\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### short-in-long-control\n\nLong-prior states from 480 to 800 ms after Ready, with an axis from the state at 480 to that at 800 ms.\nThe main reading builds the axis as u is built (the mean of the difference vectors; the Methods'\n\"applied the same projection analysis\"); the single difference X(800) - X(480) is the second reading.\n\"\"\")\ncode(r\"\"\"\nquote(\"short-in-long-control\")\nrows = []\nfor ds, g in GEO.items():\n    q = g[\"prior\"][\"Long\"]\n    t = np.arange(480, 801, 20)\n    idx = [int(np.flatnonzero(q[\"ends\"] == x)[0]) for x in t]\n    X = q[\"X\"][idx]\n    te_short = rsg.te_mean(t.astype(float), \"Short\", FITS[ds][\"wm\"])\n    w = q[\"n\"][idx]\n    for axis_name in [\"mean of differences\", \"single difference\"]:\n        if axis_name == \"mean of differences\":\n            u = rsg.encoding_axis(q[\"X\"], q[\"ends\"], 480, 800)\n        else:\n            u = (X[-1] - X[0]) / np.linalg.norm(X[-1] - X[0])\n        xu = X @ u\n        _, _, f_te, r2b = rsg.wls(xu, te_short, w)\n        _, _, f_ts, r2l = rsg.wls(xu, t.astype(float), w)\n        rows.append(dict(dataset=ds, axis=axis_name, rmse_bayes=np.sqrt(np.mean((xu - f_te) ** 2)),\n                         rmse_linear=np.sqrt(np.mean((xu - f_ts) ** 2)), R2_te=r2b, R2_ts=r2l))\nSIL = pd.DataFrame(rows)\nSIL[\"delta\"] = SIL.rmse_bayes - SIL.rmse_linear\nprint(SIL.round(4).to_string(index=False))\nfor axis_name, r in SIL.groupby(\"axis\"):\n    print(f\"{axis_name}: delta RMSE (Bayesian - linear) {np.round(r.delta.values, 3).tolist()}; \"\n          f\"two-sided signed-rank p = {stats.wilcoxon(r.delta).pvalue:.3f}\")\nsp_delta = RM[RM.prior == \"Short\"].delta.values\nprint(\"for comparison, Short prior delta RMSE:\", np.round(sp_delta, 3).tolist())\n\"\"\", tag=\"claim:short-in-long-control\")\nmd(\"**Result: ...**\")\n\nmd(\"### neural-long-more-bias\")\ncode(r\"\"\"\nquote(\"neural-long-more-bias\")\nrows = []\nfor ds, g in GEO.items():\n    r = {\"dataset\": ds}\n    for prior in [\"Short\", \"Long\"]:\n        q = g[\"prior\"][prior]\n        r[prior] = rsg.wls(q[\"xu\"], q[\"t\"], q[\"w\"])[1]\n    rows.append(r)\nNS = pd.DataFrame(rows)\nNS[\"Long_below_Short\"] = NS.Long < NS.Short\nNS[\"ratio_Long_Short\"] = NS.Long / NS.Short\nprint(\"slope of Xu on ts (spikes/s per ms):\")\nprint(NS.round(4).to_string(index=False))\nprint(f\"Long below Short in {int(NS.Long_below_Short.sum())} of 4; signed-rank p (Short - Long) = {stats.wilcoxon(NS.Short - NS.Long).pvalue:.3f}\")\n\"\"\", tag=\"claim:neural-long-more-bias\")\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### Robustness of the trajectory measures\n\nThe same measures with the outlier-flagged completed trials included, and without smoothing. These are\nvariants of standard choices (which trials, how rates are smoothed at the edges of an epoch), not\nreadings of the claims.\n\"\"\")\ncode(r\"\"\"\nall_completed = rsg.label_trials(sess[\"trials\"])\nall_completed = all_completed[all_completed.set_time.notna() & all_completed.go_time.notna() & (all_completed.tp > 0)].reset_index(drop=True)\nrows = []\nfor name, trials, smooth in [(\"main\", good, True), (\"with outlier trials\", all_completed, True), (\"unsmoothed\", good, False)]:\n    for ds in sorted(good.dataset.unique()):\n        g = GEO[ds] if name == \"main\" else rsg.dataset_geometry(spikes, trials[trials.dataset == ds], FITS[ds][\"wm\"], smooth=smooth)\n        r = dict(variant=name, dataset=ds, k_est=g[\"k_est\"], k_prod=g[\"k_prod\"])\n        for prior in [\"Short\", \"Long\"]:\n            q = g[\"prior\"][prior]\n            _, _, f_te, r2 = rsg.wls(q[\"xu\"], q[\"te\"], q[\"w\"])\n            _, slope, f_ts, _ = rsg.wls(q[\"xu\"], q[\"t\"], q[\"w\"])\n            r[f\"R2_{prior}\"] = r2\n            r[f\"dRMSE_{prior}\"] = np.sqrt(np.mean((q[\"xu\"] - f_te) ** 2)) - np.sqrt(np.mean((q[\"xu\"] - f_ts) ** 2))\n            r[f\"slope_{prior}\"] = slope\n        rows.append(r)\nROB = pd.DataFrame(rows)\nprint(ROB.round(4).to_string(index=False))\n\"\"\")\n\n# ------------------------------------------------------------------ speed\nmd(\"## Speed in the production epoch\")\nmd(\"### speed-vs-projection\")\ncode(r\"\"\"\nquote(\"speed-vs-projection\")\nSP = pd.concat([g[\"prior\"][p][\"per_ts\"].assign(dataset=ds, prior=p) for ds, g in GEO.items() for p in [\"Short\", \"Long\"]], ignore_index=True)\nSP[\"speed_per_s\"] = SP.speed / (SP.mean_tp / 1000.0)\nprint(SP[[\"dataset\", \"prior\", \"ts\", \"n_trials\", \"duration_ms\", \"xu_set\", \"speed\", \"speed_per_s\", \"mean_tp\"]].round(3).to_string(index=False))\neS, eL = expected(\"speed-vs-projection\")\nfor prior, e in [(\"Short\", eS), (\"Long\", eL)]:\n    q = SP[SP.prior == prior]\n    r = stats.pearsonr(q.xu_set, q.speed)\n    rv = stats.pearsonr(q.xu_set, q.speed_per_s)\n    within_ds = [stats.pearsonr(z.xu_set, z.speed)[0] for _, z in q.groupby(\"dataset\")]\n    print(f\"{prior}: r = {r[0]:.3f}, p = {r[1]:.2g} (expected {e['value']} +- {e['tolerance']}: within {within(r[0], e)}); \"\n          f\"variant speed / mean tp: r = {rv[0]:.3f}, p = {rv[1]:.2g}; within datasets {np.round(within_ds, 3).tolist()}\")\n\"\"\", tag=\"claim:speed-vs-projection\")\nmd(\"**Result: ...**\")\n\nmd(\"### initial-speed-biased\")\ncode(r\"\"\"\nquote(\"initial-speed-biased\")\nrows = []\nfor ds, g in GEO.items():\n    d = good[good.dataset == ds]\n    mu, comps = g[\"prod_pca\"]\n    for prior in [\"Short\", \"Long\"]:\n        ini = rsg.production_rates(spikes, d, prior, stop_ms=400)\n        tsv = rsg.PRIOR_TS[prior].astype(float)\n        sv = np.array([rsg.step_speed(rsg.project(ini[ts], mu, comps)) for ts in rsg.PRIOR_TS[prior]])\n        unb = sv[2] * tsv[2] / tsv\n        n = [int(((d.prior == prior) & (d.ts == ts) & (d.tp >= 400)).sum()) for ts in rsg.PRIOR_TS[prior]]\n        rows.append(dict(dataset=ds, prior=prior, speeds=np.round(sv, 2).tolist(), n_trials=n,\n                         slope_measured=stats.linregress(tsv, sv).slope, slope_unbiased=stats.linregress(tsv, unb).slope))\nINI = pd.DataFrame(rows)\nINI[\"shallower\"] = INI.slope_measured > INI.slope_unbiased\nprint(INI.to_string(index=False))\nw = stats.wilcoxon(INI.slope_measured - INI.slope_unbiased)\nprint(f\"measured slope shallower than unbiased in {int(INI.shallower.sum())} of 8; two-sided signed-rank p = {w.pvalue:.4f}\")\nprint(\"trials dropped for tp < 400 ms:\", int((good.tp < 400).sum()))\n\"\"\", tag=\"claim:initial-speed-biased\")\nmd(\"**Result: ...**\")\n\nmd(\"### speed-predicts-tp\")\ncode(r\"\"\"\nquote(\"speed-predicts-tp\")\neS, eL = expected(\"speed-predicts-tp\")\nfor prior, e in [(\"Short\", eS), (\"Long\", eL)]:\n    q = SP[SP.prior == prior]\n    r = stats.pearsonr(q.speed, q.mean_tp)\n    rv = stats.pearsonr(q.speed_per_s, q.mean_tp)\n    within_ds = [stats.pearsonr(z.speed, z.mean_tp)[0] for _, z in q.groupby(\"dataset\")]\n    print(f\"{prior}: r = {r[0]:.3f}, p = {r[1]:.2g} (expected {e['value']} +- {e['tolerance']}: within {within(r[0], e)}); \"\n          f\"variant speed / mean tp: r = {rv[0]:.3f}; within datasets {np.round(within_ds, 3).tolist()}\")\nprint(\"\\nvariant: trial-by-trial correlation of single-trial speed (Set to Go) with tp, per prior, effector and direction\")\nrows = []\nfor ds, g in GEO.items():\n    for prior in [\"Short\", \"Long\"]:\n        d = good[(good.dataset == ds) & (good.prior == prior)]\n        s = rsg.single_trial_speed(spikes, d, g[\"prod_pca\"])\n        r = stats.pearsonr(s, d.tp)\n        rows.append(dict(dataset=ds, prior=prior, n=len(d), r=r[0], p=r[1]))\nTT = pd.DataFrame(rows)\nprint(TT.round(4).to_string(index=False))\n\"\"\", tag=\"claim:speed-predicts-tp\")\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ alternatives\nmd(\"## Alternative mechanisms\")\nmd(\"### alt-speed-unmodulated\")\ncode(r\"\"\"\nquote(\"alt-speed-unmodulated\")\nrng = np.random.default_rng(5)\n\n\ndef support_speed_slope(d, prior):\n    r, ends, n = rsg.estimation_rates(spikes, d, rsg.PRIOR_TS[prior][-1])\n    v = np.linalg.norm(np.diff(r, axis=0), axis=1)\n    te = ends[1:]\n    sel = (te > rsg.PRIOR_TS[prior][0]) & (te <= rsg.PRIOR_TS[prior][-1])\n    return stats.linregress(te[sel], v[sel]).slope, v[sel].mean()\n\n\nrows = []\nfor ds in sorted(good.dataset.unique()):\n    for prior in [\"Short\", \"Long\"]:\n        d = good[(good.dataset == ds) & (good.prior == prior)]\n        slope, mean_speed = support_speed_slope(d, prior)\n        boot = []\n        for _ in range(200):\n            idx = np.concatenate([rng.choice(np.flatnonzero(d.ts.values == x), (d.ts == x).sum()) for x in rsg.PRIOR_TS[prior]])\n            boot.append(support_speed_slope(d.iloc[idx], prior)[0])\n        lo, hi = np.percentile(boot, [2.5, 97.5])\n        rows.append(dict(dataset=ds, prior=prior, slope=slope, ci_lo=lo, ci_hi=hi, mean_speed=mean_speed,\n                         change_over_support_pct=100 * slope * (rsg.PRIOR_TS[prior][-1] - rsg.PRIOR_TS[prior][0]) / mean_speed))\nALT1 = pd.DataFrame(rows)\nprint(\"slope of the step distance (spikes/s per 20 ms step) on time (ms) over the support, full 48-unit space:\")\nprint(ALT1.round(5).to_string(index=False))\nfor prior in [\"Short\", \"Long\"]:\n    s = ALT1[ALT1.prior == prior].slope\n    print(f\"{prior}: two-sided signed-rank of 4 slopes against 0, p = {stats.wilcoxon(s).pvalue:.3f}; positive in {int((s > 0).sum())} of 4\")\n\"\"\", tag=\"claim:alt-speed-unmodulated\")\nmd(\"**Result: ...**\")\n\nmd(\"### alt-transient-parallel\")\ncode(r\"\"\"\nquote(\"alt-transient-parallel\")\nrows = []\nfor ds in sorted(good.dataset.unique()):\n    d = good[good.dataset == ds]\n    tr200 = {p: rsg.production_rates(spikes, d, p, stop_ms=200) for p in [\"Short\", \"Long\"]}\n    X = np.vstack([r for p in tr200 for r in tr200[p].values()])\n    mu, comps, k, ev = rsg.pca_fit(X)\n    for prior in [\"Short\", \"Long\"]:\n        tsv = rsg.PRIOR_TS[prior]\n        mid = rsg.project(tr200[prior][tsv[2]], mu, comps)\n        for which, ts in [(\"shortest\", tsv[0]), (\"longest\", tsv[-1])]:\n            dist = np.linalg.norm(rsg.project(tr200[prior][ts], mu, comps) - mid, axis=1)\n            t = 20 * np.arange(1, len(dist) + 1)\n            rows.append(dict(dataset=ds, k=k, prior=prior, ts=which, slope=stats.linregress(t, dist).slope,\n                             dist_first=dist[0], dist_last=dist[-1]))\nALT2 = pd.DataFrame(rows)\nprint(ALT2.round(4).to_string(index=False))\nfor which in [\"shortest\", \"longest\"]:\n    s = ALT2[ALT2.ts == which].slope\n    print(f\"{which} ts: two-sided signed-rank of 8 slopes against 0, p = {stats.wilcoxon(s).pvalue:.3f}; \"\n          f\"median slope {s.median():.4f} per ms; median change over 200 ms {200 * s.median():.2f} against median distance \"\n          f\"{ALT2[ALT2.ts == which].dist_first.median():.2f}\")\n\"\"\", tag=\"claim:alt-transient-parallel\")\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### alt-threshold-monotonic\n\nTrajectories aligned to Go, from Go - 800 ms to Go, PCA per dataset at 60% of the variance (the legend's\nvalue); the same at 75% is shown as a variant (the legend: \"results remained unchanged when more PCs\nwere included\"). Times are the ends of 20 ms bins relative to Go, so the last bin ends at 0.\n\"\"\")\ncode(r\"\"\"\nquote(\"alt-threshold-monotonic\")\nrows = []\ncurves = {}\nfor thr in [0.60, 0.75]:\n    for ds in sorted(good.dataset.unique()):\n        d = good[good.dataset == ds]\n        trg = {(p, ts): rsg.aligned_rates(spikes, d[(d.prior == p) & (d.ts == ts)].go_time.values, -800, 0)\n               for p in [\"Short\", \"Long\"] for ts in rsg.PRIOR_TS[p]}\n        mu, comps, k, ev = rsg.pca_fit(np.vstack(list(trg.values())), thr)\n        for prior in [\"Short\", \"Long\"]:\n            tsv = rsg.PRIOR_TS[prior]\n            mid = rsg.project(trg[(prior, tsv[2])], mu, comps)\n            for ts in tsv[[0, 1, 3, 4]]:\n                dist = np.linalg.norm(rsg.project(trg[(prior, ts)], mu, comps) - mid, axis=1)\n                tmin = -800 + 20 * (int(np.argmin(dist)) + 1)\n                rows.append(dict(threshold=thr, dataset=ds, k=k, prior=prior, ts=ts, t_min=tmin,\n                                 dist_at_go=dist[-1], dist_min=dist.min()))\n                if thr == 0.60:\n                    curves[(ds, prior, ts)] = dist\nALT3 = pd.DataFrame(rows)\nfor thr, r in ALT3.groupby(\"threshold\"):\n    print(f\"variance {thr:.0%}: components per dataset {r.groupby('dataset').k.first().to_dict()}\")\n    print(f\"  time of minimum (ms before Go): median {r.t_min.median():.0f}; in last 40 ms {int((r.t_min >= -20).sum())} of 32; \"\n          f\"in last 200 ms {int((r.t_min >= -180).sum())} of 32; at the last bin {int((r.t_min == 0).sum())}\")\n    print(\"  \", sorted(r.t_min.tolist()))\n    print(\"  by prior:\", r.groupby(\"prior\").t_min.median().to_dict())\nfig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)\nt = np.arange(-780, 1, 20)\nfor (ds, prior, ts), dist in curves.items():\n    axes[0 if prior == \"Short\" else 1].plot(t, dist, lw=0.8, alpha=0.7)\nfor ax, p in zip(axes, [\"Short\", \"Long\"]):\n    ax.set_title(f\"{p}: distance to the middle ts trajectory (60% PCs)\")\n    ax.set_xlabel(\"time to Go (ms)\")\nallc = np.array(list(curves.values()))\nprint(f\"plotted distances range {allc.min():.2f} to {allc.max():.2f} (all shown)\")\nplt.tight_layout()\nplt.show()\n\"\"\", tag=\"claim:alt-threshold-monotonic\")\nmd(\"**Result: ...**\")\n\nmd(\"## Summary\")\nmd(\"(written after the run)\")\n\ncode(r\"\"\"\nprint(f\"runtime {time.time() - T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/sohn-2019/reproduce_sohn_2019.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_main.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_main.py'; s=open(p).read()
s=s.replace('n=r._5 if hasattr(r, "_5") else r.size','n=r.size')
a=s.index('md(r"""\n**Result: reproduced.** At ts = 800')
b=s.index('""")',a)+4
s=s[:a]+'md("**Result: ...**")\n'+s[b:]
open(p,'w').write(s)
EOF
. env/bin/activate && python build_main.py && cd entries/sohn-2019 && time jupyter nbconvert --to notebook --execute reproduce_sohn_2019.ipynb --output $TMPDIR/out_main.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -3
```

```
75 cells
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.068s
user	0m0.060s
sys	0m0.010s
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && uv pip install -q nbconvert && cd entries/sohn-2019 && time jupyter nbconvert --to notebook --execute reproduce_sohn_2019.ipynb --output-dir $TMPDIR --output out_main.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -15
cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c.get('metadata',{}).get('tags',[])
    print('=== cell', tags)
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text']))
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
        elif 'text/plain' in o.get('data',{}) and 'image/png' not in o['data']: print(''.join(o['data']['text/plain']))
EOF
```

```
[31m---------------------------------------------------------------------------[39m
[31mModuleNotFoundError[39m                       Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[1][39m[32m, line 6[39m
[32m      2[39m os.environ.setdefault([33m"OMP_NUM_THREADS"[39m, [33m"1"[39m)
[32m      3[39m [38;5;28;01mimport[39;00m time, resource, warnings
[32m      4[39m [38;5;28;01mimport[39;00m numpy [38;5;28;01mas[39;00m np
[32m      5[39m [38;5;28;01mimport[39;00m pandas [38;5;28;01mas[39;00m pd
[32m----> [39m[32m6[39m [38;5;28;01mimport[39;00m yaml
[32m      7[39m [38;5;28;01mimport[39;00m matplotlib.pyplot [38;5;28;01mas[39;00m plt
[32m      8[39m [38;5;28;01mimport[39;00m statsmodels.api [38;5;28;01mas[39;00m sm
[32m      9[39m [38;5;28;01mfrom[39;00m scipy [38;5;28;01mimport[39;00m stats

[31mModuleNotFoundError[39m: No module named 'yaml'


real	0m2.824s
user	0m2.095s
sys	0m0.173s
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && uv pip install -q pyyaml && cd entries/sohn-2019 && time jupyter nbconvert --to notebook --execute reproduce_sohn_2019.ipynb --output-dir $TMPDIR --output out_main.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v "^\[NbConvertApp\] Writing" | tail -15; python $TMPDIR/show.py $TMPDIR/out_main.ipynb
```

```
<persisted-output>
Output too large (42.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/ba60kcohk.txt

Preview (first 2KB):
[NbConvertApp] Converting notebook reproduce_sohn_2019.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	0m56.186s
user	0m53.023s
sys	0m0.448s
=== cell []
=== cell []
dandi:000130/0.241017.1448
                                         path      size                              asset_id
0   sub-Haydn/sub-Haydn_desc-test_ecephys.nwb   1553584  a2c3ced1-2869-4483-aa19-8815c2d18c91
1  sub-Haydn/sub-Haydn_desc-train_ecephys.nwb  14119912  c90cbccc-31a5-4815-88e6-822d8c5ca68c


session: 20161211 2016-12-11 00:00:00-05:00 | Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains continuous segments of the full session on 2016-12-11 that can be used for training models for the Neural Latents Benchmark.
subject: Haydn Macaca mulatta P4Y M
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/ba60kcohk.txt
```

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/bq6mcuw6g.txt

Preview (first 2KB):
  is_outlier: Whether a trial's tp is considered an outlier using probabilistic mixture model
  split: Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none"
unit table columns: ('heldout', 'spike_times', 'obs_intervals')
electrodes: 72 in groups {'electrode_group_1': 24, 'electrode_group_2': 24, 'electrode_group_3': 24} | location <StringArray>
['DMFC']
Length: 1, dtype: str | x, y, z all NaN: True
acquisition: [] | processing: []

test file trial columns: ['id', 'start_time', 'stop_time', 'go_time', 'split'] | 283 trials, 40 units ( 0 held out )

=== cell ['sanity']
== trials (train file)
all: 1160 | split: {'train': 748, 'val': 258, 'none': 154}
with Ready: 1060 | with Set: 1039 | with Go: 1029 | tp <= 0: 134 | is_outlier: 177
completed (Set and Go, tp > 0): 1026 | of them flagged is_outlier: 43 | analysed (completed, not outlier): 983

[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/bq6mcuw6g.txt",
 "offset": 25
}
```

```
25	                   Short      33      21      25      31      24       0       0       0       0
26	         Right     Long        0       0       0       0      19      17      30      21      25
27	                   Short      21      35      14      21      22       0       0       0       0
28	fewest analysed trials in any of the 40 conditions: 14
29	
30	== ranges and units of the variables used
31	ts (ms): 480.0 to 1200.0; ts values [np.float64(480.0), np.float64(560.0), np.float64(640.0), np.float64(720.0), np.float64(800.0), np.float64(900.0), np.float64(1000.0), np.float64(1100.0), np.float64(1200.0)]
32	tp (ms): 406.5 to 1462.9
33	theta values: [np.float64(0.0), np.float64(180.0)] | is_short x iti (ms):
34	iti       500.0   1220.0
35	is_short                
36	False        583       0
37	True           0     577
38	(set_time - ready_time) in ms minus ts: median 0.0, 1st to 99th percentile -20.0 to 17.0, range -23.5 to 23.5
39	(go_time - set_time) in ms minus tp:    median -17.9, 1st to 99th percentile -107.0 to -0.4, range -200.6 to -0.1
40	
41	== units
42	train file: 54 units, 14 flagged heldout; observed 4808.9 s in 6 intervals: [[0.0, 740.0], [740.1, 1519.5], [1519.6, 2277.3], [2277.4, 3054.6], [3054.7, 3792.0], [3792.1, 4809.3]]
43	all units share the same observation intervals: True
44	spike times sorted in every unit: True
[... 318 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/bq6mcuw6g.txt",
 "offset": 362
}
```

```
362
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; python $TMPDIR/show.py $TMPDIR/out_main.ipynb > $TMPDIR/main_out.txt; grep -n "speed-vs-projection\] Larger" $TMPDIR/main_out.txt; sed -n '/Hand Left Short  720        31/,$p' $TMPDIR/main_out.txt
```

```
366:[speed-vs-projection] Larger projections on the encoding axis at Set are followed by slower neural trajectories in the production epoch (Pearson correlation, rho Short = -0.74, rho Long = -0.51).
 Hand Left Short  720        31          560  16.164  3.656        5.337  685.139
 Hand Left Short  800        24          600  17.508  3.480        4.631  751.458
 Hand Left  Long  800        14          680  -0.941  4.760        5.889  808.309
 Hand Left  Long  900        24          700   0.733  3.673        4.210  872.599
 Hand Left  Long 1000        16          720   3.597  3.893        4.298  905.788
 Hand Left  Long 1100        16          780   6.399  3.694        3.746  986.246
 Hand Left  Long 1200        18          780  10.050  3.638        3.625 1003.612
Hand Right Short  480        21          400   5.216  6.018       10.737  560.489
Hand Right Short  560        35          460   7.470  5.279        8.902  593.034
Hand Right Short  640        14          440  11.534  5.064        7.660  661.104
Hand Right Short  720        21          540  16.403  4.154        5.507  754.223
Hand Right Short  800        22          660  19.608  3.722        4.554  817.430
Hand Right  Long  800        19          740   2.254  4.888        5.329  917.209
Hand Right  Long  900        17          820   6.778  4.072        4.198  969.975
Hand Right  Long 1000        30          900  12.993  3.496        3.286 1063.784
Hand Right  Long 1100        21         1000  16.588  3.094        2.737 1130.492
Hand Right  Long 1200        25          980  20.232  3.218        2.795 1151.263
Short: r = -0.932, p = 2.3e-09 (expected -0.74 +- 0.074: within False); variant speed / mean tp: r = -0.916, p = 1.4e-08; within datasets [-0.919, -0.995, -0.995, -0.984]
Long: r = -0.874, p = 4.8e-07 (expected -0.51 +- 0.051: within False); variant speed / mean tp: r = -0.925, p = 5.2e-09; within datasets [-0.93, -0.956, -0.669, -0.951]
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Sun Nov 15 06:37:55 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_gpfa.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tag=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag]\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Sohn et al. (2019) on dandiset 000130: single-trial GPFA analyses\n\nPaper: Sohn, Narain, Meirhaeghe and Jazayeri (2019), Neuron 103:934, doi:10.1016/j.neuron.2019.06.012;\nclaims file `claims/sohn-2019.yaml` (from the author manuscript, PMC6805134). Dataset: DANDI:000130,\nversion **0.241017.1448**, the version this attempt was asked to use (the most recent published one;\nthe paper cites none), streamed from the archive. The trial-averaged claims are in\n`reproduce_sohn_2019.ipynb`; this notebook tests the two GPFA claims, gpfa-variance-inverted-u and\ngpfa-mean-sigmoid (Figure 6C and 6D). The paper ran this analysis on \"high-yield sessions (N=48 for\nmonkey H)\"; this session has 48 units that pass the unit selection.\n\nGPFA is elephant's implementation of Yu et al. (2009). It is fit per dataset (effector and direction)\non single trials from Ready to Set, both priors, in 20 ms bins, with the latent dimensionality chosen\nfrom 4 and 8 by 3-fold cross-validated log-likelihood, as the criterion of gpfa-variance-inverted-u\ngives. Fitting takes about 4 minutes per dataset.\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nimport time, resource, warnings, logging\nimport numpy as np\nimport pandas as pd\nimport yaml\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport rsg\n\nwarnings.filterwarnings(\"ignore\")\nlogging.getLogger(\"elephant\").setLevel(logging.ERROR)\nT0 = time.time()\nDATASET = f\"dandi:{rsg.DANDISET}/{rsg.VERSION}\"\nCLAIMS = {c[\"id\"]: c for c in yaml.safe_load(open(\"../../claims/sohn-2019.yaml\"))[\"claims\"]}\npd.set_option(\"display.width\", 200)\n\n\ndef quote(cid):\n    c = CLAIMS[cid]\n    print(f\"[{cid}] {c['statement']}\\nCriterion: {c.get('criterion', '(none)')}\")\n\"\"\")\n\ncode(r\"\"\"\nsess = rsg.load_session(rsg.TRAIN_PATH)\ngood = rsg.good_trials(sess[\"trials\"])\nui = rsg.select_units(sess, good)\nspikes = [sess[\"spikes\"][i] for i in ui]\nprint(DATASET, rsg.TRAIN_PATH)\nprint(\"trials analysed (completed, not outlier):\", len(good), \"| units selected:\", len(ui), \"of\", len(sess[\"units\"]))\nprint(pd.crosstab([good.dataset, good.prior], good.ts))\nprint(\"Ready to Set (ms) from the trial table: %.1f to %.1f; ts values %s\" % (\n    ((good.set_time - good.ready_time) * 1000).min(), ((good.set_time - good.ready_time) * 1000).max(), sorted(good.ts.unique())))\nprint(\"spikes per trial from Ready to the ts-th ms: median %.0f\" % np.median(\n    [sum(np.searchsorted(s, r + t / 1000) - np.searchsorted(s, r) for s in spikes) for r, t in zip(good.ready_time[:50], good.ts[:50])]))\n\"\"\", tag=\"sanity\")\n\nmd(r\"\"\"\n## GPFA fits\n\nEach trial runs from Ready to Ready + ts (the bins end on the ts grid, every ts being a multiple of\n20 ms). The fold assignment is seeded.\n\"\"\")\ncode(r\"\"\"\nFITS = {}\nfor j, ds in enumerate(sorted(good.dataset.unique())):\n    t = time.time()\n    d = good[good.dataset == ds].reset_index(drop=True)\n    best, cv, lat = rsg.gpfa_fit(spikes, d, x_dims=(4, 8), n_folds=3, seed=100 + j)\n    lengths_ok = all(x.shape[0] == ts // rsg.BIN for x, ts in zip(lat, d.ts.values.astype(int)))\n    FITS[ds] = dict(d=d, dim=best, cv=cv, lat=lat)\n    print(f\"{ds}: {len(d)} trials; CV log-likelihood {({k: round(v, 1) for k, v in cv.items()})}; chosen dimensionality {best}; \"\n          f\"latent lengths match ts: {lengths_ok}; {time.time() - t:.0f} s\")\n\"\"\")\n\nmd(\"## gpfa-variance-inverted-u\")\ncode(r\"\"\"\nquote(\"gpfa-variance-inverted-u\")\nrows, PROJ = [], {}\nfor ds, F in FITS.items():\n    d, lat = F[\"d\"], F[\"lat\"]\n    for prior in [\"Short\", \"Long\"]:\n        tsv = rsg.PRIOR_TS[prior]\n        idx = np.flatnonzero(d.prior.values == prior)\n        nb = tsv[-1] // rsg.BIN\n        L = np.full((len(idx), nb, F[\"dim\"]), np.nan)\n        for r, i in enumerate(idx):\n            L[r, :lat[i].shape[0]] = lat[i]\n        avg = np.nanmean(L, axis=0)  # attrition: each bin averages the trials still before Set\n        ends = np.arange(rsg.BIN, tsv[-1] + 1, rsg.BIN)\n        u = rsg.encoding_axis(avg, ends, tsv[0], tsv[-1])\n        xu = np.array([lat[i][-1] @ u for i in idx])  # state in the last bin before Set\n        ts_i = d.ts.values[idx]\n        z = (xu - xu.mean()) / xu.std(ddof=1)\n        var = np.array([z[ts_i == x].var(ddof=1) for x in tsv])\n        mean = np.array([xu[ts_i == x].mean() for x in tsv])\n        n = [int((ts_i == x).sum()) for x in tsv]\n        quad = np.polyfit(tsv / 1000.0, var, 2)[0]\n        PROJ[(ds, prior)] = dict(xu=xu, ts=ts_i, var=var, mean=mean)\n        rows.append(dict(dataset=ds, prior=prior, dim=F[\"dim\"], n=n, var=np.round(var, 3).tolist(),\n                         quad_coef_per_s2=quad, extremes_mean_var=(var[0] + var[-1]) / 2, middle3_mean_var=var[1:4].mean()))\nVAR = pd.DataFrame(rows)\nprint(VAR.to_string(index=False))\nw = stats.wilcoxon(VAR.quad_coef_per_s2, alternative=\"less\")\nprint(f\"\\nquadratic coefficient below zero in {int((VAR.quad_coef_per_s2 < 0).sum())} of 8; one-tailed signed-rank (coefficient < 0) p = {w.pvalue:.4f}\")\nprint(f\"variance at the extremes below the mean of the middle three ts in {int((VAR.extremes_mean_var < VAR.middle3_mean_var).sum())} of 8\")\nallv = np.vstack(VAR[\"var\"].values)\nprint(\"mean variance profile over the 8 dataset-priors (by ts rank):\", np.round(allv.mean(0), 3).tolist())\n\"\"\", tag=\"claim:gpfa-variance-inverted-u\")\ncode(r\"\"\"\nfig, ax = plt.subplots(1, 2, figsize=(9, 3.2))\nfor (ds, prior), p in PROJ.items():\n    ax[0 if prior == \"Short\" else 1].plot(rsg.PRIOR_TS[prior], p[\"var\"], \"o-\", lw=0.8, label=ds)\nfor a, prior in zip(ax, [\"Short\", \"Long\"]):\n    a.set_title(f\"{prior}: variance of z-scored Xu\")\n    a.set_xlabel(\"ts (ms)\")\nax[0].legend(fontsize=7)\nplt.tight_layout()\nplt.show()\nprint(\"plotted variances range %.3f to %.3f (all shown)\" % (allv.min(), allv.max()))\n\"\"\", tag=\"claim:gpfa-variance-inverted-u\")\nmd(\"**Result: ...**\")\n\nmd(\"## gpfa-mean-sigmoid\")\ncode(r\"\"\"\nquote(\"gpfa-mean-sigmoid\")\nrows = []\nfor (ds, prior), p in PROJ.items():\n    tsv = rsg.PRIOR_TS[prior].astype(float)\n    inc = np.diff(p[\"mean\"])\n    rows.append(dict(dataset=ds, prior=prior, mean_xu=np.round(p[\"mean\"], 3).tolist(), increments=np.round(inc, 3).tolist(),\n                     extreme=(inc[0] + inc[3]) / 2, middle=(inc[1] + inc[2]) / 2, slope=stats.linregress(tsv, p[\"mean\"]).slope))\nMS = pd.DataFrame(rows)\nprint(MS.to_string(index=False))\nw = stats.wilcoxon(MS.middle, MS.extreme)\nprint(f\"\\nmiddle increment above extreme in {int((MS.middle > MS.extreme).sum())} of 8; two-sided signed-rank p = {w.pvalue:.4f}\")\nsl = MS.pivot(index=\"dataset\", columns=\"prior\", values=\"slope\")\nsl[\"Short_higher\"] = sl.Short > sl.Long\nprint(sl.to_string())\nprint(f\"Short slope above Long in {int(sl.Short_higher.sum())} of 4; one-tailed signed-rank p = {stats.wilcoxon(sl.Short, sl.Long, alternative='greater').pvalue:.4f}\")\n\"\"\", tag=\"claim:gpfa-mean-sigmoid\")\nmd(\"**Result: ...**\")\n\nmd(\"## Summary\")\nmd(\"(written after the run)\")\ncode(r\"\"\"\nprint(f\"runtime {time.time() - T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/sohn-2019/gpfa_sohn_2019.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_gpfa.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python build_gpfa.py && cd entries/sohn-2019 && time jupyter nbconvert --to notebook --execute gpfa_sohn_2019.ipynb --output-dir $TMPDIR --output out_gpfa.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | grep -v "Writing\|TCP" | tail -5; python $TMPDIR/show.py $TMPDIR/out_gpfa.ipynb | grep -v "^Fitting\|^Initializing\|^$"
```

```
<persisted-output>
Output too large (5.6MB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/bqt03n2wq.txt

Preview (first 2KB):
15 cells
[NbConvertApp] Converting notebook gpfa_sohn_2019.ipynb to notebook

real	8m26.156s
user	8m36.881s
sys	0m5.972s
=== cell []
=== cell ['sanity']
dandi:000130/0.241017.1448 sub-Haydn/sub-Haydn_desc-train_ecephys.nwb
trials analysed (completed, not outlier): 983 | units selected: 48 of 54
ts                480.0   560.0   640.0   720.0   800.0   900.0   1000.0  1100.0  1200.0
dataset    prior                                                                        
Eye Left   Long        0       0       0       0      36      29      30      29      31
           Short      21      28      17      17      22       0       0       0       0
Eye Right  Long        0       0       0       0      38      34      23      25      27
           Short      24      27      31      22      25       0       0       0       0
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "WARNING\|^Fitting\|^Initializing\|^$" /home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/bqt03n2wq.txt | tail -50
```

```
/tmp/claude-1001/env/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 2 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "
/tmp/claude-1001/env/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 2 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "
/tmp/claude-1001/env/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 2 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "
/tmp/claude-1001/env/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 2 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "
/tmp/claude-1001/env/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 2 last spike(s) of the input spiketrain
  warnings.warn("Binning discarded {} last spike(s) of the "
Hand Right: 225 trials; CV log-likelihood {4: np.float64(-124931.8), 8: np.float64(-124243.0)}; chosen dimensionality 8; latent lengths match ts: True; 116 s
=== cell ['claim:gpfa-variance-inverted-u']
[gpfa-variance-inverted-u] The variance across single trials of the GPFA neural state at Set projected on the encoding axis has an inverted-U profile over ts, lower at the extremes of each prior (one-tailed signed-rank test on quadratic coefficients, p = 0.0273, monkey H).
Criterion: GPFA (20 ms bins) per dataset on single trials from Ready to Set, both priors, units as selected above; the latent dimensionality chosen by 3-fold cross-validated log-likelihood from 4 and 8; orthonormalised latents. Per prior, u from the trial-averaged latents with attrition as above; each trial's latent state in its last bin before Set projected on u; Xu z-scored over the prior's trials; the variance at each ts; the quadratic coefficient of a polynomia
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/8e298786-9f2f-4b24-91f8-b24650bd9ce0/tool-results/bqt03n2wq.txt; grep -c "Binning discarded" $F; grep -o "discarded [0-9]* last" $F | sort | uniq -c; grep -c "rounding error" $F
```

```
84
     24 discarded 1 last
     18 discarded 2 last
31736
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='rsg.py'; s=open(p).read()
old='''    def trains(sub):
        out = []
        for ready, ts in zip(sub.ready_time.values, sub.ts.values):
            t1 = ready + ts / 1000.0
            tr = []
            for s in spikes:
                i0, i1 = np.searchsorted(s, [ready, t1])
                tr.append(neo.SpikeTrain((s[i0:i1] - ready) * pq.s, t_start=0 * pq.s,
                                         t_stop=(t1 - ready) * pq.s))
            out.append(tr)
        return out
'''
new='''    def trains(sub):  # in ms, so that ts / 20 ms is an exact number of bins
        out = []
        for ready, ts in zip(sub.ready_time.values, sub.ts.values):
            t1 = ready + ts / 1000.0
            tr = []
            for s in spikes:
                i0, i1 = np.searchsorted(s, [ready, t1])
                rel = np.minimum((s[i0:i1] - ready) * 1000.0, ts - 1e-6)
                tr.append(neo.SpikeTrain(rel * pq.ms, t_start=0 * pq.ms, t_stop=float(ts) * pq.ms))
            out.append(tr)
        return out
'''
assert old in s; s=s.replace(old,new)
old2='''    cv = {}
    for d in x_dims:'''
new2='''    quiet = contextlib.redirect_stdout(io.StringIO())  # elephant prints its progress
    quiet.__enter__()
    cv = {}
    for d in x_dims:'''
assert old2 in s; s=s.replace(old2,new2)
old3='''    lat = g.fit_transform(data, returned_data=["latent_variable_orth"])
'''
new3='''    lat = g.fit_transform(data, returned_data=["latent_variable_orth"])
    quiet.__exit__(None, None, None)
'''
assert old3 in s; s=s.replace(old3,new3)
s=s.replace('''    import neo
    import quantities as pq
    from elephant.gpfa import GPFA
''','''    import contextlib
    import io
    import neo
    import quantities as pq
    from elephant.gpfa import GPFA
''')
open(p,'w').write(s)
EOF
grep -n "t_stop\|quiet" rsg.py
```

```
347:                tr.append(neo.SpikeTrain(rel * pq.ms, t_start=0 * pq.ms, t_stop=float(ts) * pq.ms))
355:    quiet = contextlib.redirect_stdout(io.StringIO())  # elephant prints its progress
356:    quiet.__enter__()
371:    quiet.__exit__(None, None, None)
```

**Agent calls Read**

```json
{
 "file_path": "entries/sohn-2019/rsg.py",
 "offset": 322,
 "limit": 55
}
```

```
322	    return beta[0], beta[1], fit, r2
323	
324	
325	# ---------------------------------------------------------------- GPFA
326	
327	def gpfa_fit(spikes, good_sub: pd.DataFrame, x_dims=(4, 8), n_folds=3, seed=0):
328	    """GPFA on single trials from Ready to Set (20 ms bins), units given by `spikes`.
329	
330	    The latent dimensionality is chosen from x_dims by n_folds-fold cross-validated
331	    log-likelihood. Returns (chosen dim, cv log-likelihoods, list of orthonormalised latent
332	    trajectories, each bins x dims, with bin j ending at 20(j+1) ms after Ready)."""
333	    import contextlib
334	    import io
335	    import neo
336	    import quantities as pq
337	    from elephant.gpfa import GPFA
338	
339	    def trains(sub):  # in ms, so that ts / 20 ms is an exact number of bins
340	        out = []
341	        for ready, ts in zip(sub.ready_time.values, sub.ts.values):
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='rsg.py'; s=open(p).read()
a=s.index('    data = trains(good_sub)\n    rng')
b=s.index('    return best, cv, [np.asarray(x).T for x in lat]')
new='''    data = trains(good_sub)
    rng = np.random.default_rng(seed)
    folds = np.array_split(rng.permutation(len(data)), n_folds)
    cv = {}
    # elephant prints its progress and warns about bin rounding; both are silenced
    with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
        warnings.simplefilter("ignore")
        logging.getLogger("elephant").setLevel(logging.ERROR)
        for d in x_dims:
            ll = 0.0
            for k in range(n_folds):
                test = set(folds[k].tolist())
                train = [data[i] for i in range(len(data)) if i not in test]
                held = [data[i] for i in sorted(test)]
                g = GPFA(bin_size=BIN * pq.ms, x_dim=d, verbose=False)
                g.fit(train)
                ll += g.score(held)
            cv[d] = ll
        best = max(cv, key=cv.get)
        g = GPFA(bin_size=BIN * pq.ms, x_dim=best, verbose=False)
        lat = g.fit_transform(data, returned_data=["latent_variable_orth"])
'''
s=s[:a]+new+s[b:]
s=s.replace('''    import contextlib
    import io
    import neo''','''    import contextlib
    import io
    import logging
    import warnings
    import neo''')
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate; python -c "
import rsg,numpy as np,time
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g); sp=[s['spikes'][i] for i in ui]
d=g[g.dataset=='Hand Left'].reset_index(drop=True).iloc[:60]
t=time.time(); b,cv,lat=rsg.gpfa_fit(sp,d,x_dims=(4,),n_folds=2); print(b,cv,[x.shape for x in lat[:3]], d.ts.values[:3], time.time()-t)
" 2>&1 | tail -5
```

```
[2026-11-15 06:48:13,029] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 06:48:13,029] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 06:48:13,039] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
[2026-11-15 06:48:13,039] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.
4 {4: np.float64(-20308.115963753226)} [(45, 4), (60, 4), (55, 4)] [ 900. 1200. 1100.] 28.504315614700317
```

**Agent calls Bash**

```bash
grep -n "getLogger\|logging" $TMPDIR/env/lib/python3.13/site-packages/elephant/utils.py | head
```

```
15:import logging
38:logger = logging.getLogger(__file__)
39:log_handler = logging.StreamHandler()
41:    logging.Formatter(
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='rsg.py'; s=open(p).read()
s=s.replace('        logging.getLogger("elephant").setLevel(logging.ERROR)\n','        elephant_utils.logger.setLevel(logging.ERROR)\n')
s=s.replace('    from elephant.gpfa import GPFA\n','    from elephant import utils as elephant_utils\n    from elephant.gpfa import GPFA\n')
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate; python -c "
import rsg,numpy as np,time
s=rsg.load_session(); g=rsg.good_trials(s['trials']); ui=rsg.select_units(s,g); sp=[s['spikes'][i] for i in ui]
d=g[g.dataset=='Hand Left'].reset_index(drop=True).iloc[:40]
t=time.time(); b,cv,lat=rsg.gpfa_fit(sp,d,x_dims=(4,),n_folds=2); print(b,cv,[x.shape for x in lat[:3]], d.ts.values[:3], time.time()-t)
" 2>&1 | tail -5
```

```
4 {4: np.float64(-10169.859307060417)} [(45, 4), (60, 4), (55, 4)] [ 900. 1200. 1100.] 23.087669849395752
```

**Agent calls Bash**

```bash
cd  python -c "import json;s=json.load(open('schemas/entry.schema.json'));print(json.dumps(s['properties'],indent=0)[:2500]); print(s.get('required'))"; cat entries/dana-2016/entry.yaml; head -30 entries/dana-2016/README.md
```

```
{
"schema_version": {
"const": 1
},
"name": {
"description": "Unique across the registry, and the name of the entry's directory.",
"type": "string",
"pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
"maxLength": 100
},
"type": {
"enum": [
"orientation",
"reproduction",
"analysis"
]
},
"title": {
"type": "string",
"minLength": 1,
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && cat > requirements.in <<'EOF'
elephant
h5py
matplotlib
neo
numpy
pandas
pynwb
pyyaml
quantities
remfile
requests
scikit-learn
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: sohn-2019
type: reproduction
title: Bayesian timing and curved trajectories in macaque DMFC (Sohn et al. 2019)
description: Tests the findings of Sohn, Narain, Meirhaeghe and Jazayeri (2019) on dandiset 000130,
  which holds one session of monkey H in the Ready-Set-Go task with 54 units from dorsomedial frontal
  cortex, prepared for the Neural Latents Benchmark. It tests the behavioural biases and the Bayesian
  observer fits, the single-neuron GLM and prior effect, the dimensionality of population activity,
  the encoding axis and its match to the Bayesian estimate, the speed of production trajectories,
  the three alternative mechanisms, and the single-trial GPFA variance and mean profiles. The recurrent
  network models and monkey G are not in the dataset.
license: Apache-2.0
notebooks:
- path: reproduce_sohn_2019.ipynb
  title: Reproducing Sohn et al. (2019) from dandiset 000130, trial-averaged analyses
  runtime_minutes: 2
- path: gpfa_sohn_2019.ipynb
  title: Reproducing Sohn et al. (2019) from dandiset 000130, single-trial GPFA analyses
  runtime_minutes: 9
helpers:
- rsg.py
related:
- id: dandi:000130/0.241017.1448
  relation: uses_data
- id: doi:10.1016/j.neuron.2019.06.012
  relation: reproduces
EOF
cd ../.. && date -u && python tools/entry.py lock entries/sohn-2019 2>&1 | tail -3 && time python tools/entry.py all entries/sohn-2019 2>&1 | tail -15
```

```
Sun Nov 15 06:49:04 UTC 2026
wrote sohn-2019/requirements.lock.txt (Python 3.13, with hashes)
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (62 s)
pass  gpfa_sohn_2019.ipynb  (476 s)

real	9m7.846s
user	8m57.191s
sys	0m3.026s
```

**Agent calls Bash**

```bash
cd  ls executed/sohn-2019; . $TMPDIR/env/bin/activate; python $TMPDIR/show.py executed/sohn-2019/gpfa_sohn_2019.ipynb | sed -n '/GPFA fits/,$p' | tail -45; python $TMPDIR/show.py executed/sohn-2019/reproduce_sohn_2019.ipynb > $TMPDIR/main_exec.txt; diff <(grep -v "took\|runtime" $TMPDIR/main_out.txt) <(grep -v "took\|runtime" $TMPDIR/main_exec.txt) | head
```

```
gpfa_sohn_2019.ipynb
reproduce_sohn_2019.ipynb
result.json
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/env/bin/activate; python $TMPDIR/show.py executed/sohn-2019/gpfa_sohn_2019.ipynb | tail -50; wc -l $TMPDIR/main_exec.txt
```

```
Hand Left: 222 trials; CV log-likelihood {4: np.float64(-116062.8), 8: np.float64(-115549.5)}; chosen dimensionality 8; latent lengths match ts: True; 105 s

Hand Right: 225 trials; CV log-likelihood {4: np.float64(-124932.0), 8: np.float64(-124242.8)}; chosen dimensionality 8; latent lengths match ts: True; 109 s

=== cell ['claim:gpfa-variance-inverted-u']
[gpfa-variance-inverted-u] The variance across single trials of the GPFA neural state at Set projected on the encoding axis has an inverted-U profile over ts, lower at the extremes of each prior (one-tailed signed-rank test on quadratic coefficients, p = 0.0273, monkey H).
Criterion: GPFA (20 ms bins) per dataset on single trials from Ready to Set, both priors, units as selected above; the latent dimensionality chosen by 3-fold cross-validated log-likelihood from 4 and 8; orthonormalised latents. Per prior, u from the trial-averaged latents with attrition as above; each trial's latent state in its last bin before Set projected on u; Xu z-scored over the prior's trials; the variance at each ts; the quadratic coefficient of a polynomial fit of variance on ts. Reproduced when a one-tailed signed-rank test (coefficient below zero) over the 8 dataset-priors has p < 0.05; not reproduced otherwise.
   dataset prior  dim                    n                                 var  quad_coef_per_s2  extremes_mean_var  middle3_mean_var
  Eye Left Short    8 [21, 28, 17, 17, 22]  [0.41, 0.213, 0.585, 0.338, 0.167]         -6.320423           0.288554          0.378657
  Eye Left  Long    8 [36, 29, 30, 29, 31] [0.568, 0.902, 0.721, 0.456, 0.378]         -6.481265           0.473245          0.693026
 Eye Right Short    8 [24, 27, 31, 22, 25] [0.757, 0.501, 0.573, 0.408, 0.324]          1.201593           0.540557          0.493839
 Eye Right  Long    8 [38, 34, 23, 25, 27]  [0.937, 0.715, 0.956, 0.369, 0.41]         -2.151503           0.673909          0.680195
 Hand Left Short    8 [33, 21, 25, 31, 24] [0.791, 1.229, 0.881,
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && python - <<'EOF'
p='rsg.py'; s=open(p).read()
old='''        for d in x_dims:
            ll = 0.0'''
new='''        for d in (x_dims if len(x_dims) > 1 else ()):
            ll = 0.0'''
assert old in s; s=s.replace(old,new)
old='''        best = max(cv, key=cv.get)
        g = GPFA('''
new='''        best = max(cv, key=cv.get) if cv else x_dims[0]
        g = GPFA('''
assert old in s; s=s.replace(old,new)
s=s.replace('''    The latent dimensionality is chosen from x_dims by n_folds-fold cross-validated
    log-likelihood.''','''    The latent dimensionality is chosen from x_dims by n_folds-fold cross-validated
    log-likelihood (no cross-validation when x_dims holds one value). Spike times are given in
    ms so that ts / 20 ms is a whole number of bins.''')
open(p,'w').write(s)
EOF
date -u
```

```
Sun Nov 15 06:58:54 UTC 2026
```

**Agent**

Now I'll update the GPFA notebook builder with a projection function, the 4-dimension variant and the result texts.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_gpfa.py'; s=open(p).read()
a=s.index('md("## gpfa-variance-inverted-u")')
b=s.index('md("## Summary")')
new=r'''md("## gpfa-variance-inverted-u")
code(r"""
quote("gpfa-variance-inverted-u")


def projections(F):
    rows, proj = [], {}
    d, lat = F["d"], F["lat"]
    for prior in ["Short", "Long"]:
        tsv = rsg.PRIOR_TS[prior]
        idx = np.flatnonzero(d.prior.values == prior)
        nb = tsv[-1] // rsg.BIN
        L = np.full((len(idx), nb, lat[0].shape[1]), np.nan)
        for r, i in enumerate(idx):
            L[r, :lat[i].shape[0]] = lat[i]
        avg = np.nanmean(L, axis=0)  # attrition: each bin averages the trials still before Set
        ends = np.arange(rsg.BIN, tsv[-1] + 1, rsg.BIN)
        u = rsg.encoding_axis(avg, ends, tsv[0], tsv[-1])
        xu = np.array([lat[i][-1] @ u for i in idx])  # state in the last bin before Set
        ts_i = d.ts.values[idx]
        z = (xu - xu.mean()) / xu.std(ddof=1)
        var = np.array([z[ts_i == x].var(ddof=1) for x in tsv])
        mean = np.array([xu[ts_i == x].mean() for x in tsv])
        proj[prior] = dict(xu=xu, ts=ts_i, var=var, mean=mean)
        rows.append(dict(prior=prior, dim=lat[0].shape[1], n=[int((ts_i == x).sum()) for x in tsv],
                         var=np.round(var, 3).tolist(), quad_coef_per_s2=np.polyfit(tsv / 1000.0, var, 2)[0],
                         extremes_mean_var=(var[0] + var[-1]) / 2, middle3_mean_var=var[1:4].mean()))
    return rows, proj


rows, PROJ = [], {}
for ds, F in FITS.items():
    r, p = projections(F)
    rows += [dict(dataset=ds, **x) for x in r]
    PROJ.update({(ds, k): v for k, v in p.items()})
VAR = pd.DataFrame(rows)
print(VAR.to_string(index=False))
w = stats.wilcoxon(VAR.quad_coef_per_s2, alternative="less")
print(f"\nquadratic coefficient below zero in {int((VAR.quad_coef_per_s2 < 0).sum())} of 8; one-tailed signed-rank (coefficient < 0) p = {w.pvalue:.4f}")
print(f"variance at the extremes below the mean of the middle three ts in {int((VAR.extremes_mean_var < VAR.middle3_mean_var).sum())} of 8")
allv = np.vstack(VAR["var"].values)
print("mean variance profile over the 8 dataset-priors (by ts rank):", np.round(allv.mean(0), 3).tolist())
""", tag="claim:gpfa-variance-inverted-u")
code(r"""
fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
for (ds, prior), p in PROJ.items():
    ax[0 if prior == "Short" else 1].plot(rsg.PRIOR_TS[prior], p["var"], "o-", lw=0.8, label=ds)
for a, prior in zip(ax, ["Short", "Long"]):
    a.set_title(f"{prior}: variance of z-scored Xu")
    a.set_xlabel("ts (ms)")
ax[0].legend(fontsize=7)
plt.tight_layout()
plt.show()
print("plotted variances range %.3f to %.3f (all shown)" % (allv.min(), allv.max()))
""", tag="claim:gpfa-variance-inverted-u")
md(r"""
Variant: the cross-validation chose 8 latent dimensions in every dataset. The same analysis with 4
latent dimensions, the other value the criterion allows, shows how much the test depends on the fit.
""")
code(r"""
rows4 = []
for j, (ds, F) in enumerate(FITS.items()):
    t = time.time()
    _, _, lat4 = rsg.gpfa_fit(spikes, F["d"], x_dims=(4,), seed=200 + j)
    r, _ = projections(dict(d=F["d"], lat=lat4))
    rows4 += [dict(dataset=ds, **x) for x in r]
VAR4 = pd.DataFrame(rows4)
print(VAR4.to_string(index=False))
w4 = stats.wilcoxon(VAR4.quad_coef_per_s2, alternative="less")
print(f"\n4 latent dimensions: quadratic coefficient below zero in {int((VAR4.quad_coef_per_s2 < 0).sum())} of 8; "
      f"one-tailed signed-rank p = {w4.pvalue:.4f}")
""", tag="claim:gpfa-variance-inverted-u")
md(r"""
**Result: not reproduced.** With the 8 latent dimensions that cross-validation chose in all four
datasets, the quadratic coefficient is negative in 6 of the 8 dataset-priors, but the one-tailed
signed-rank test gives p = 0.098, above 0.05. The mean variance profile over the 8 dataset-priors
(0.79, 0.91, 0.85, 0.51, 0.45 by ts rank) is high at the short end and falls at the long end, not an
inverted U. The variances rest on 14 to 38 trials per ts.
""")

md("## gpfa-mean-sigmoid")
code(r"""
quote("gpfa-mean-sigmoid")
rows = []
for (ds, prior), p in PROJ.items():
    tsv = rsg.PRIOR_TS[prior].astype(float)
    inc = np.diff(p["mean"])
    rows.append(dict(dataset=ds, prior=prior, mean_xu=np.round(p["mean"], 3).tolist(), increments=np.round(inc, 3).tolist(),
                     extreme=(inc[0] + inc[3]) / 2, middle=(inc[1] + inc[2]) / 2, slope=stats.linregress(tsv, p["mean"]).slope))
MS = pd.DataFrame(rows)
print(MS.to_string(index=False))
w = stats.wilcoxon(MS.middle, MS.extreme)
print(f"\nmiddle increment above extreme in {int((MS.middle > MS.extreme).sum())} of 8; two-sided signed-rank p = {w.pvalue:.4f}")
sl = MS.pivot(index="dataset", columns="prior", values="slope")
sl["Short_higher"] = sl.Short > sl.Long
print(sl.to_string())
print(f"Short slope above Long in {int(sl.Short_higher.sum())} of 4; one-tailed signed-rank p = {stats.wilcoxon(sl.Short, sl.Long, alternative='greater').pvalue:.4f}")
""", tag="claim:gpfa-mean-sigmoid")
md(r"""
**Result: reproduced.** The middle increment of the mean projection exceeds the extreme one in 7 of
8 dataset-priors (two-sided signed-rank p = 0.0156), and the slope of the mean projection on ts is
higher for Short than for Long in all 4 datasets (one-tailed p = 0.0625, the paper's value).
""")

'''
s=s[:a]+new+s[b:]
s=s.replace('md("(written after the run)")', '''md(r"""
| claim | outcome |
|---|---|
| gpfa-variance-inverted-u | not reproduced: quadratic coefficient negative in 6 of 8, one-tailed p = 0.098 |
| gpfa-mean-sigmoid | reproduced: middle above extreme increments in 7 of 8 (p = 0.0156); Short slope higher in 4 of 4 |

The trial-averaged claims and the summary of the whole attempt are in `reproduce_sohn_2019.ipynb`.
The paper fit GPFA in MATLAB (Yu et al. 2009; Cowley et al. 2013); elephant's port is used here, with
the dimensionality rule and the 3-fold cross-validation of the claims file. The paper used one
high-yield session of 48 units for monkey H; this session also has 48 selected units, but whether it
is the same session cannot be told from the files.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.
""")''')
open(p,'w').write(s)
EOF
grep -n "Result" build_gpfa.py | head
```

```
163:**Result: not reproduced.** With the 8 latent dimensions that cross-validation chose in all four
189:**Result: reproduced.** The middle increment of the mean projection exceeds the extreme one in 7 of
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python build_gpfa.py && cd entries/sohn-2019 && jupyter nbconvert --to notebook --execute gpfa_sohn_2019.ipynb --output-dir $TMPDIR --output out_gpfa2.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | grep -v "Writing\|TCP\|Converting" | tail -5; python $TMPDIR/show.py $TMPDIR/out_gpfa2.ipynb | sed -n '/quadratic coefficient below/,$p'
```

```
17 cells
quadratic coefficient below zero in 6 of 8; one-tailed signed-rank (coefficient < 0) p = 0.0742
variance at the extremes below the mean of the middle three ts in 6 of 8
mean variance profile over the 8 dataset-priors (by ts rank): [0.786, 0.911, 0.846, 0.506, 0.456]

=== cell ['claim:gpfa-variance-inverted-u']
plotted variances range 0.168 to 1.530 (all shown)

=== cell ['claim:gpfa-variance-inverted-u']
   dataset prior  dim                    n                                 var  quad_coef_per_s2  extremes_mean_var  middle3_mean_var
  Eye Left Short    4 [21, 28, 17, 17, 22]  [0.446, 0.24, 0.632, 0.361, 0.167]         -7.134211           0.306345          0.410950
  Eye Left  Long    4 [36, 29, 30, 29, 31] [0.604, 0.917, 0.733, 0.489, 0.396]         -6.234079           0.499973          0.713145
 Eye Right Short    4 [24, 27, 31, 22, 25] [0.852, 0.511, 0.666, 0.425, 0.329]          1.042855           0.590506          0.534136
 Eye Right  Long    4 [38, 34, 23, 25, 27] [1.015, 0.719, 0.935, 0.389, 0.422]         -0.743006           0.718494          0.681028
 Hand Left Short    4 [33, 21, 25, 31, 24] [0.842, 1.313, 0.941, 0.407, 0.891]         -1.505252           0.866376          0.886621
 Hand Left  Long    4 [14, 24, 16, 16, 18] [1.333, 1.467, 0.271, 0.843, 0.667]          8.186039           0.999876          0.860697
Hand Right Short    4 [21, 35, 14, 21, 22] [0.871, 0.912, 1.491, 0.699, 0.538]        -19.818392           0.704583          1.034228
Hand Right  Long    4 [19, 17, 30, 21, 25] [0.738, 1.301, 1.319, 0.849, 0.412]        -17.774197           0.574682          1.156128

4 latent dimensions: quadratic coefficient below zero in 6 of 8; one-tailed signed-rank p = 0.0977
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -E "^(numpy|scipy|scikit-learn|elephant|neo|quantities)==" entries/sohn-2019/requirements.lock.txt; . $TMPDIR/env/bin/activate; uv pip list 2>/dev/null | grep -iE "^(numpy|scipy|scikit-learn|elephant|neo|quantities) "
```

```
elephant==1.2.1 \
neo==0.14.6 \
numpy==2.5.4 \
quantities==0.16.4 \
scikit-learn==1.9.1 \
scipy==1.18.1 \
elephant                  1.2.1
neo                       0.14.6
numpy                     2.5.4
quantities                0.16.4
scikit-learn              1.9.1
scipy                     1.18.1
```

**Agent calls Bash**

```bash
cd $TMPDIR/env/lib/python3.13/site-packages/elephant; grep -n "FactorAnalysis\|random" gpfa/gpfa_core.py gpfa/gpfa.py gpfa/gpfa_util.py | head -20
```

```
gpfa/gpfa_core.py:18:from sklearn.decomposition import FactorAnalysis
gpfa/gpfa_core.py:119:    fa = FactorAnalysis(n_components=x_dim, copy=True,
gpfa/gpfa.py:200:    independent Poisson spike trains recorded in 50 trials with randomized
gpfa/gpfa.py:210:    ...     firing_rates = np.random.randint(low=1, high=100,
gpfa/gpfa_util.py:144:            randOL = np.random.multinomial(totalOL, probs)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/env/lib/python3.13/site-packages/elephant/gpfa; sed -n 115,125p gpfa_core.py; sed -n 120,160p gpfa_util.py; grep -n "segment_by_seq\|cut_trials\|segment_length" gpfa.py | head
```

```
# ========================================
    print('Initializing parameters using factor analysis...')

    y_all = np.hstack(seqs_train_cut['y'])
    fa = FactorAnalysis(n_components=x_dim, copy=True,
                        noise_variance_init=np.diag(np.cov(y_all, bias=True)))
    fa.fit(y_all.T)
    params_init['d'] = y_all.mean(axis=1)
    params_init['C'] = fa.components_.T
    params_init['R'] = np.diag(fa.noise_variance_)

        seqOut = seq_in
        return seqOut

    dtype_seqOut = [('segId', int), ('T', int),
                    ('y', object)]
    seqOut_buff = []
    for n, seqIn_n in enumerate(seq_in):
        T = seqIn_n['T']

[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && python - <<'EOF'
p='rsg.py'; s=open(p).read()
old='''                g = GPFA(bin_size=BIN * pq.ms, x_dim=d, verbose=False)
                g.fit(train)'''
new='''                g = GPFA(bin_size=BIN * pq.ms, x_dim=d, verbose=False)
                np.random.seed(seed + 1 + k)  # elephant draws the segment overlaps from np.random
                g.fit(train)'''
assert old in s; s=s.replace(old,new)
old='''        g = GPFA(bin_size=BIN * pq.ms, x_dim=best, verbose=False)
        lat = g.fit_transform('''
new='''        g = GPFA(bin_size=BIN * pq.ms, x_dim=best, verbose=False)
        np.random.seed(seed)
        lat = g.fit_transform('''
assert old in s; s=s.replace(old,new)
old='''    ms so that ts / 20 ms is a whole number of bins.'''
new='''    ms so that ts / 20 ms is a whole number of bins. elephant fits on segments of 20 bins whose
    overlaps it draws from numpy's global generator, so each fit seeds it (from `seed`); the
    segment length is elephant's default, as in Yu et al.'s code.'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd $TMPDIR && python - <<'EOF'
p='build_gpfa.py'; s=open(p).read()
a=s.index('md(r"""\nVariant: the cross-validation chose 8')
b=s.index('md(r"""\n**Result: not reproduced.** With the 8 latent')
new=r'''md(r"""
Variants. elephant fits GPFA on 20-bin segments of the trials, with overlaps drawn at random, so the
fit depends on the seed. The same analysis is run with 8 latent dimensions (the cross-validated
choice) refit under three other seeds, and with 4 latent dimensions, the other value the criterion
allows.
""")
code(r"""
variants = [("8 dims, seed 1", 8, 1), ("8 dims, seed 2", 8, 2), ("8 dims, seed 3", 8, 3), ("4 dims, seed 0", 4, 0)]
vrows = []
for name, dim, seed in variants:
    t = time.time()
    rows_v = []
    for j, (ds, F) in enumerate(FITS.items()):
        _, _, lat_v = rsg.gpfa_fit(spikes, F["d"], x_dims=(dim,), seed=1000 * seed + 100 + j)
        r, _ = projections(dict(d=F["d"], lat=lat_v))
        rows_v += [dict(dataset=ds, **x) for x in r]
    V = pd.DataFrame(rows_v)
    vrows.append(dict(variant=name, n_negative=int((V.quad_coef_per_s2 < 0).sum()),
                      p_one_tailed=stats.wilcoxon(V.quad_coef_per_s2, alternative="less").pvalue,
                      quad_coefs=np.round(V.quad_coef_per_s2.values, 2).tolist(), seconds=round(time.time() - t)))
VARV = pd.DataFrame(vrows)
print(VARV.to_string(index=False))
print("main fit:", int((VAR.quad_coef_per_s2 < 0).sum()), "negative, p =", round(w.pvalue, 4),
      "| coefficients", np.round(VAR.quad_coef_per_s2.values, 2).tolist())
""", tag="claim:gpfa-variance-inverted-u")
'''
s=s[:a]+new+s[b:]
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/build_gpfa.py && date -u && jupyter nbconvert --to notebook --execute gpfa_sohn_2019.ipynb --output-dir $TMPDIR --output out_gpfa3.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | grep -v "Writing\|TCP\|Converting" | tail -5; python $TMPDIR/show.py $TMPDIR/out_gpfa3.ipynb | sed -n '/GPFA fits/,$p' | grep -v "^$" | head -80; date -u
```

```
17 cells
Sun Nov 15 07:09:29 UTC 2026

            > jupyter nbconvert --config mycfg.py

To see all available configurables, use `--help-all`.

Traceback (most recent call last):
  File "/tmp/claude-1001/show.py", line 2, in <module>
    nb=json.load(open(sys.argv[1]))
                 ~~~~^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude-1001/out_gpfa3.ipynb'
Sun Nov 15 07:09:30 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sohn-2019 && . $TMPDIR/env/bin/activate && jupyter nbconvert --to notebook --execute gpfa_sohn_2019.ipynb --output-dir $TMPDIR --output out_gpfa3.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | grep -v "Writing\|TCP\|Converting" | tail -5; python $TMPDIR/show.py $TMPDIR/out_gpfa3.ipynb | sed -n '/GPFA fits/,$p' | grep -v "^$" | head -80; date -u
```

```
Sun Nov 15 07:24:58 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python $TMPDIR/show.py $TMPDIR/out_gpfa3.ipynb | grep -v "^$" | sed -n '/chosen dimensionality/,$p' | grep -v "^Criterion\|^\[gpfa"
```

```
Eye Left: 260 trials; CV log-likelihood {4: np.float64(-164989.4), 8: np.float64(-164312.1)}; chosen dimensionality 8; latent lengths match ts: True; 132 s
Eye Right: 276 trials; CV log-likelihood {4: np.float64(-175289.6), 8: np.float64(-174689.0)}; chosen dimensionality 8; latent lengths match ts: True; 135 s
Hand Left: 222 trials; CV log-likelihood {4: np.float64(-116073.1), 8: np.float64(-115533.2)}; chosen dimensionality 8; latent lengths match ts: True; 111 s
Hand Right: 225 trials; CV log-likelihood {4: np.float64(-124944.6), 8: np.float64(-124250.6)}; chosen dimensionality 8; latent lengths match ts: True; 114 s
=== cell ['claim:gpfa-variance-inverted-u']
   dataset prior  dim                    n                                 var  quad_coef_per_s2  extremes_mean_var  middle3_mean_var
  Eye Left Short    8 [21, 28, 17, 17, 22]   [0.405, 0.214, 0.59, 0.34, 0.168]         -6.565173           0.286591          0.381385
  Eye Left  Long    8 [36, 29, 30, 29, 31]  [0.566, 0.898, 0.72, 0.452, 0.376]         -6.475176           0.470799          0.689956
 Eye Right Short    8 [24, 27, 31, 22, 25] [0.758, 0.495, 0.576, 0.406, 0.317]          1.057542           0.537140          0.492523
 Eye Right  Long    8 [38, 34, 23, 25, 27]  [0.94, 0.713, 0.959, 0.369, 0.411]         -2.130845           0.675177          0.680166
 Hand Left Short    8 [33, 21, 25, 31, 24] [0.779, 1.196, 0.858, 0.373, 0.853]         -0.238528           0.816173          0.809238
 Hand Left  Long    8 [14, 24, 16, 16, 18] [1.279, 1.402, 0.333, 0.761, 0.556]          5.997035           0.917449          0.832316
Hand Right Short    8 [21, 35, 14, 21, 22]  [0.819, 0.79, 1.407, 0.711, 0.598]        -16.515338           0.708525          0.969111
Hand Right  Long    8 [19, 17, 30, 21, 25] [0.709, 1.535, 1.324, 0.628, 0.348]        -19.266700           0.528411          1.162294
quadratic coefficient below zero in 6 of 8; one-tailed signed-rank (coefficient < 0) p = 0.0547
variance at the extremes b
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n 'Result' build_main.py
```

```
23:(PMC6805134): Results, figure legends and STAR Methods, without the supplementary tables.
235:**Result: not reproduced.** With an intercept, 6 of 8 slopes lie between 0 and 1; the Eye Left Short
255:md("**Result: ...**")
273:md("**Result: ...**")
285:md("**Result: ...**")
317:**Result: ...**
387:md("**Result: ...**")
422:md("**Result: ...**")
453:md("**Result: ...**")
496:md("**Result: ...**")
520:md("**Result: ...**")
558:md("**Result: ...**")
577:md("**Result: ...**")
623:md("**Result: ...**")
647:md("**Result: ...**")
671:md("**Result: ...**")
708:md("**Result: ...**")
735:md("**Result: ...**")
783:md("**Result: ...**")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results_main.py <<'PYEOF'
R = {}
R["beh-slopes"] = """**Result: not reproduced.** With an intercept, 6 of 8 slopes lie between 0 and 1; the Eye Left Short
(1.011) and Eye Right Short (1.110) slopes do not, and 5 of the 8 intervals exclude both 0 and 1.
Through the origin, 2 of 8 slopes are below 1. The four Hand slopes (0.50 to 0.86) are below 1 with
intervals that exclude 0 and 1 under the intercept reading."""
R["beh-overlap-prior"] = """**Result: not reproduced.** At ts = 800 ms the median of tp - 800 is +28.3 ms for Short (n = 93) and
+47.6 ms for Long (n = 107): both are positive, and the rank-sum test between priors gives p = 0.073.
Per dataset, only Hand Left has a negative Short median (-61.6 ms), the Long median is the larger in 2
of 4 datasets, and only Hand Right differs between priors at p < 0.05 (p = 0.00099). The paper's
p < 1e-43 pools 17 sessions; this is one."""
R["beh-sigmoid-increments"] = """**Result: reproduced.** The middle increment exceeds the extreme one in 7 of 8 conditions (Hand Left
Short is the exception, -10.7 ms); two-sided signed-rank p = 0.0156, the smallest but one that 8
conditions allow. The paper's p < 1e-11 pools 17 sessions."""
R["beh-long-more-bias"] = """**Result: reproduced, resting on an assumption.** With the intercept regression of beh-slopes, the Long
slope is below the Short slope in all 4 datasets (0.845 against 1.011, 0.903 against 1.110, 0.502
against 0.612, 0.612 against 0.861). Through the origin, the Methods' equation, it is below in 3 of 4
(Eye Right: 1.027 against 1.016), which would make the claim partially reproduced. The intercept
reading is adopted: a slope below 1 with an intercept is what the paper's "biased toward the mean of
the prior" describes, and a slope through the origin measures overall lengthening."""
R["beh-bayes-model"] = """
"R2 of the observed mean bias by the model's predicted bias" is read as 1 - SS_res / SS_tot of the
observed biases around the predictions; the squared Pearson correlation is shown as the second reading.

**Result: partially reproduced.** The correlation of observed and predicted SD of tp is positive in
all 4 datasets (0.807, 0.909, 0.749, 0.277; p = 0.44 for Hand Right), but the bias R2 reaches 0.8 in 2
of 4: Hand Left 0.978 and Hand Right 0.865, against Eye Left 0.670 and Eye Right 0.122. The squared
correlation gives the same count (0.678, 0.129, 0.978, 0.869). The Eye fits have small measurement
noise (wm 0.025 and 0.013, against 0.116 and 0.073 for Hand) and the observed Eye biases span 108 and
80 ms, against 265 and 166 ms for Hand. The fitted wp are 0.090 to 0.106.
"""
R["glm-prior-ts"] = """**Result: not reproduced.** 38 of 48 units (79.2%, 95% CI 65.0 to 89.5) are prior-dependent, against
65 +- 6.5%, and 22 of 48 (45.8%, 95% CI 31.4 to 60.8) are ts-dependent under reading (a), 24 of 48
(50.0%) under reading (b), against 27 +- 2.7%. Both fractions are above the paper's under both
readings."""
R["dfr-overlap-support"] = """**Result: reproduced.** The mean RMS difference is largest in the 480 to 640 ms bin (6.86 spikes/s),
above the 95th percentile of the shuffled maximum (3.15; the largest of 200 shuffles is 3.46). The
next largest are the bin after Set, 800 to 960 ms (6.07), and 320 to 480 ms (5.97). Per dataset, the
largest bin lies within 480 to 800 ms in 3 of 4 (Eye Right 9.14, Hand Left 4.88, Hand Right 4.39);
in Eye Left it is 800 to 960 ms (9.73)."""
R["pca-dimensionality"] = """**Result: not reproduced.** In the estimation epoch, 2 components reach 75% of the variance in all 4
datasets (0.80 to 0.86 with 2), so none is in 3 to 4; in the production epoch 2, 2, 4 and 5 components
do, so 1 of 4 is in 5 to 11. In all, 1 of 8 values is in range. Without smoothing (robustness table
below) the counts are 3 to 6 and 6 to 15, so they depend on the smoothing, which the claims file
fixes at an SD of 40 ms."""
R["encoding-r2"] = """**Result: reproduced.** Under reading (a), Hand Left, R2 is 0.996 for Short and 0.977 for Long; under
reading (b), the mean of the 4 datasets, 0.959 and 0.982. All four values are within tolerance. The
reference is weak in this space of 2 components: random unit vectors give median R2 of 0.69 to 0.99,
from 1.2% to 44.2% of them reach the R2 of u, and ts itself explains Xu almost as well as te (R2 0.898
to 0.990)."""
R["encoding-bayes-beats-linear"] = """**Result: partially reproduced.** The Bayesian fit has the lower RMSE in all 4 datasets for Short
(differences -0.04 to -0.47 spikes/s) and in 3 of 4 for Long; for Hand Left Long the linear fit is
better (0.481 against 0.583). The weighted RMSE gives the same counts. The signed-rank p over 4
datasets is 0.125 for Short and 0.25 for Long; 4 datasets cannot give the paper's 0.008."""
R["short-in-long-control"] = """**Result: reproduced.** The signed-rank test of the RMSE difference over the 4 datasets gives
p = 0.25 (single-difference axis: p = 0.125), so the paper's test finds no difference; with 4
datasets it cannot reach p < 0.05. The effect sizes do not show an absence: the Bayesian model fits
better in 3 of 4 datasets (differences -0.21, -0.12 and -0.11 spikes/s; Hand Left +0.05), of a size
like the Short prior's own (-0.04 to -0.47)."""
R["neural-long-more-bias"] = """**Result: partially reproduced.** The slope of Xu on ts is lower for Long in 3 of 4 datasets
(Long/Short ratios 0.54, 0.62 and 0.36); in Hand Right the Long slope is slightly higher (0.0486
against 0.0470). With the outlier trials included the count is the same; without smoothing the Long
slope is lower in all 4 (robustness table below)."""
R["speed-vs-projection"] = """**Result: partially reproduced.** Larger projections at Set go with slower trajectories in both
priors: r = -0.932 (p = 2.3e-09) for Short and -0.874 (p = 4.8e-07) for Long, both negative and
stronger than the paper's -0.74 and -0.51, outside tolerance. Within datasets r is -0.92 to -0.995
(Short) and -0.67 to -0.96 (Long). With speed divided by the mean tp, r is -0.916 and -0.925."""
R["initial-speed-biased"] = """**Result: not reproduced.** The measured slope is shallower than the unbiased one in 7 of 8
dataset-priors (Eye Right Long is the exception), but the two-sided signed-rank test gives p = 0.055,
above 0.05. No trial had tp below 400 ms."""
R["speed-predicts-tp"] = """**Result: partially reproduced.** Faster trajectories go with shorter mean tp: r = -0.719
(p = 0.00035) for Short and -0.744 (p = 0.00017) for Long, both negative with p < 0.05 and both
outside the tolerance around -0.58 and -0.52. Trial by trial, single-trial speed correlates negatively
with tp in all 8 prior, effector and direction groups (r -0.15 to -0.71), with p < 0.05 in 7."""
R["alt-speed-unmodulated"] = """**Result: reproduced.** The signed-rank tests of the 4 slopes against zero give p = 0.25 (Short) and
0.125 (Long), so the paper's test finds no modulation; with 4 datasets it cannot reach p < 0.05. The
effect sizes lean the other way: the slope is positive in 7 of 8 dataset-priors, the step distance
changes by -13% to +56% over the support, and the bootstrap interval excludes zero in 6 of 8. These
intervals sit mostly above the point estimates (Hand Right Short: 0.0037 within 0.0036 to 0.0120),
so they are biased upward and should not be read as a test."""
R["alt-transient-parallel"] = """**Result: reproduced.** The signed-rank tests of the 8 slopes against zero give p = 0.195 for the
shortest ts and 1.0 for the longest, so the paper's test finds no change. For the longest ts the
median change over 200 ms is 0.07 spikes/s against a median distance of 22.3. For the shortest ts
the distance grows in 6 of 8 dataset-priors (median change 14.5 against a median starting distance of
18.2): a divergence, not the convergence the transient hypothesis predicts."""
R["alt-threshold-monotonic"] = """**Result: not reproduced.** At 60% of the variance (1 to 3 components) the median time of the minimum
distance is 230 ms before Go; the minimum falls in the last 40 ms in 4 of 32 curves and in the last
200 ms in 13. At 75% (2 to 5 components) the median is 160 ms before Go, which would be partially
reproduced. In both, the minima spread from 760 ms before Go to Go."""
PYEOF
python - <<'EOF'
import re
exec(open('results_main.py').read())
s=open('build_main.py').read()
order=["beh-sigmoid-increments","beh-long-more-bias","beh-overlap-prior"]
# replace beh-slopes block
a=s.index('md(r"""\nThe criterion\'s regression has an intercept')
b=s.index('""")',a)+4
s=s[:a]+'md(r"""\nThe criterion\'s regression has an intercept in the main reading; the Methods write `tp = beta ts + e`,\nrun as the second reading.\n\n'+R["beh-slopes"]+'\n""")\n'+s[b:]
# bayes block
a=s.index('md(r"""\n"R2 of the observed mean bias')
b=s.index('""")',a)+4
s=s[:a]+'md(r"""'+R["beh-bayes-model"]+'""")\n'+s[b:]
# sequential placeholders
seq=["beh-overlap-prior","beh-sigmoid-increments","beh-long-more-bias","glm-prior-ts","dfr-overlap-support","pca-dimensionality","encoding-r2","encoding-bayes-beats-linear","short-in-long-control","neural-long-more-bias","speed-vs-projection","initial-speed-biased","speed-predicts-tp","alt-speed-unmodulated","alt-transient-parallel","alt-threshold-monotonic"]
for cid in seq:
    i=s.index('md("**Result: ...**")')
    s=s[:i]+'md(r"""\n'+R[cid]+'\n""")'+s[i+len('md("**Result: ...**")'):]
assert '**Result: ...**' not in s
open('build_main.py','w').write(s)
EOF
grep -c "Result:" build_main.py
```

```
18
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_main.py').read()
# after sanity cell: insert metadata check statement before "### Recordings deposited twice"
anchor='md(r"""\n### Recordings deposited twice'
check=r'''md(r"""
Checks of the description against the values:

- Trials: 1160 in the train file, of which 1026 are completed (Set and Go present, tp > 0) and 983 are
  completed and not flagged `is_outlier`. Every one of the 40 conditions has at least 14 analysed
  trials, so the unit rule's 5 trials per condition removes no unit; the rate rule keeps 48 of 54 units.
- `ts` takes the 9 values of the two priors, and `set_time - ready_time` matches it to within 23.5 ms
  (median 0), consistent with a 60 Hz display.
- `tp` is longer than `go_time - set_time` in every analysed trial, by a median of 17.9 ms (0.1 to
  200.6 ms). The files do not say which events `tp` is measured between. The behavioural claims use
  `tp`, as the claims file says; the neural alignment uses the event times.
- `iti`: the description says 500 ms for the Short prior and 1220 ms for Long; the values are the
  reverse (Short 1220 in all 577 Short trials, Long 500 in all 583), which is what the paper's Methods
  give. The data are trusted; this is recorded as a finding.
- `theta` is 0 or 180 and `is_eye` is boolean, as described. Electrode positions are all NaN and the
  unit table has no electrode column, so units cannot be placed on the three probes, and the files
  do not say which units are single units and which multi-units.
- The test file holds 283 trials of 1.7 s with only `go_time` (at 1.5 s into each), for 40 units; their
  prior, ts, effector and direction are withheld, so they cannot enter any analysis here.
""")

'''
i=s.index(anchor); s=s[:i]+check+s[i:]
# after clock check code: add statement
anchor2='# ------------------------------------------------------------------ behaviour'
clk=r'''md(r"""
The target direction is decoded from counts around Go with accuracy 0.761 at the true times and 0.477
to 0.517 with the times shifted by 20 or 60 s (chance 0.510), and the population rate rises within
100 ms of Set and of Ready at the true times only. The spikes share the clock of the trial table, in
the one session there is.
""")

'''
i=s.index(anchor2); s=s[:i]+clk+s[i:]
summary=r'''md(r"""
| claim | outcome |
|---|---|
| beh-slopes | not reproduced: Eye Short slopes 1.011 and 1.110 |
| beh-overlap-prior | not reproduced: Short median bias at 800 ms is +28.3 ms; p = 0.073 |
| beh-sigmoid-increments | reproduced: 7 of 8, p = 0.0156 |
| beh-long-more-bias | reproduced, resting on an assumption (regression with intercept): 4 of 4 |
| beh-bayes-model | partially reproduced: SD correlation positive in 4 of 4, bias R2 >= 0.8 in 2 of 4 |
| glm-prior-ts | not reproduced: 79.2% prior-dependent, 45.8% ts-dependent |
| dfr-overlap-support | reproduced: largest difference at 480 to 640 ms, above the shuffles |
| pca-dimensionality | not reproduced: 1 of 8 counts in range (2 estimation components everywhere) |
| encoding-r2 | reproduced: Hand Left 0.996 and 0.977 |
| encoding-bayes-beats-linear | partially reproduced: Short 4 of 4, Long 3 of 4 |
| short-in-long-control | reproduced (paper's test, p = 0.25), with Bayesian better in 3 of 4 |
| neural-long-more-bias | partially reproduced: 3 of 4 |
| speed-vs-projection | partially reproduced: r = -0.93 and -0.87, stronger than the paper's |
| initial-speed-biased | not reproduced: 7 of 8 shallower, p = 0.055 |
| speed-predicts-tp | partially reproduced: r = -0.72 and -0.74, stronger than the paper's |
| alt-speed-unmodulated | reproduced (paper's test, p = 0.25 and 0.125), slopes positive in 7 of 8 |
| alt-transient-parallel | reproduced: p = 0.195 and 1.0 |
| alt-threshold-monotonic | not reproduced: median minimum 230 ms before Go |
| gpfa-variance-inverted-u | not reproduced: 6 of 8 negative, p = 0.055 (`gpfa_sohn_2019.ipynb`) |
| gpfa-mean-sigmoid | reproduced (`gpfa_sohn_2019.ipynb`) |
| rnn-curved-manifold, rnn-perturbation | blocked: the networks are not in the dataset nor public |
| monkey-g | blocked: monkey G is not in the dataset |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

How the analysis differs from the paper's: it uses one session of monkey H, where the paper pools 17
sessions of H and 12 of G, so the behavioural tests have one session's power and the population tests
have 4 datasets in place of 8, which no signed-rank test over 4 values can bring below p = 0.125.
Within the session, the 283 test-file trials are unusable (no task variables), so about 80% of the
session's trials are analysed. Method details the claims file fixed are followed; the regression
intercept of the behavioural slopes is an assumption (beh-long-more-bias). GPFA is elephant's port,
not the paper's MATLAB code.

What was found about the dataset: it holds one of the paper's 29 sessions, and its test file withholds
the task variables of 283 trials and the spikes of 14 units on them. The `iti` description reverses
the two priors. `tp` exceeds `go_time - set_time` by a median of 17.9 ms, without a description of how
it is measured. Units have no electrode assignment and no single or multi-unit label. The spikes share
the clock of the trial table.
""")'''
s=s.replace('md("(written after the run)")', summary)
open('build_main.py','w').write(s)

g=open('build_gpfa.py').read()
a=g.index('md(r"""\n**Result: not reproduced.** With the 8 latent')
b=g.index('""")',a)+4
g=g[:a]+r'''md(r"""
**Result: not reproduced.** With the 8 latent dimensions that cross-validation chose in all four
datasets, the quadratic coefficient is negative in 6 of the 8 dataset-priors, and the one-tailed
signed-rank test gives p = 0.055, just above 0.05. The result is close to the threshold: refitting
under three other seeds gives p = 0.055, 0.039 and 0.055, and 4 latent dimensions give p = 0.098, with
6 of 8 coefficients negative every time. The mean variance profile over the 8 dataset-priors (0.78,
0.91, 0.85, 0.51, 0.45 by ts rank) falls toward the long end more than it dips at the short end. The
variances rest on 14 to 38 trials per ts.
""")
'''+g[b:]
g=g.replace('| gpfa-variance-inverted-u | not reproduced: quadratic coefficient negative in 6 of 8, one-tailed p = 0.098 |','| gpfa-variance-inverted-u | not reproduced: quadratic coefficient negative in 6 of 8, one-tailed p = 0.055 (0.039 to 0.098 in the variants) |')
open('build_gpfa.py','w').write(g)
EOF
grep -n "0.055\|0.098" build_gpfa.py | head
```

```
173:signed-rank test gives p = 0.055, just above 0.05. The result is close to the threshold: refitting
174:under three other seeds gives p = 0.055, 0.039 and 0.055, and 4 latent dimensions give p = 0.098, with
209:| gpfa-variance-inverted-u | not reproduced: quadratic coefficient negative in 6 of 8, one-tailed p = 0.055 (0.039 to 0.098 in the variants) |
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_main.py').read()
old='''to 0.517 with the times shifted by 20 or 60 s (chance 0.510), and the population rate rises within
100 ms of Set and of Ready at the true times only. The spikes share the clock of the trial table, in
the one session there is.'''
new='''to 0.517 with the times shifted by 20 or 60 s (chance 0.510). The mean population rate rises 100 to
200 ms after Set (from 9.7 to 13.6 spikes/s) and after Ready (from 6.7 to 10.9) at the true times, and
stays flat with the times shifted by 2 s. The spikes share the clock of the trial table, in the one
session there is.'''
assert old in s; s=s.replace(old,new); open('build_main.py','w').write(s)
EOF
. env/bin/activate && python build_main.py && python build_gpfa.py && cd  && date -u && python tools/entry.py all entries/sohn-2019 2>&1 | tail -6; date -u
```

```
77 cells
17 cells
Sun Nov 15 07:26:49 UTC 2026
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (60 s)
pass  gpfa_sohn_2019.ipynb  (895 s)
Sun Nov 15 07:42:56 UTC 2026
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/env/bin/activate; python $TMPDIR/show.py executed/sohn-2019/gpfa_sohn_2019.ipynb > $TMPDIR/g_final.txt; python $TMPDIR/show.py $TMPDIR/out_gpfa3.ipynb > $TMPDIR/g_local.txt; diff <(grep -v " s$\|seconds\|runtime\|; [0-9]* s" $TMPDIR/g_local.txt) <(grep -v " s$\|seconds\|runtime\|; [0-9]* s" $TMPDIR/g_final.txt) | head -20; grep "p = \|p_one\|seed" $TMPDIR/g_final.txt | head; python $TMPDIR/show.py executed/sohn-2019/reproduce_sohn_2019.ipynb > $TMPDIR/m_final.txt; diff <(grep -v "took\|runtime" $TMPDIR/main_exec.txt) <(grep -v "took\|runtime" $TMPDIR/m_final.txt) | head
```

```
44,47c44,47
< 8 dims, seed 1           6      0.054688 [-6.53, -6.56, 0.89, -2.27, -0.25, 6.19, -16.71, -19.45]      118
< 8 dims, seed 2           6      0.039062  [-6.47, -6.52, 0.77, -2.17, -0.92, 5.34, -16.1, -19.36]      118
< 8 dims, seed 3           6      0.054688   [-6.33, -6.4, 1.04, -2.25, -0.7, 6.17, -16.19, -19.13]      118
< 4 dims, seed 0           6      0.097656  [-7.23, -6.26, 0.95, -0.74, -1.27, 8.18, -19.86, -17.8]       74
---
> 8 dims, seed 1           6      0.054688 [-6.53, -6.56, 0.89, -2.27, -0.25, 6.19, -16.71, -19.45]      115
> 8 dims, seed 2           6      0.039062  [-6.47, -6.52, 0.77, -2.17, -0.92, 5.34, -16.1, -19.36]      114
> 8 dims, seed 3           6      0.054688   [-6.33, -6.4, 1.04, -2.25, -0.7, 6.17, -16.19, -19.13]      113
> 4 dims, seed 0           6      0.097656  [-7.23, -6.26, 0.95, -0.74, -1.27, 8.18, -19.86, -17.8]       71
[gpfa-variance-inverted-u] The variance across single trials of the GPFA neural state at Set projected on the encoding axis has an inverted-U profile over ts, lower at the extremes of each prior (one-tailed signed-rank test on quadratic coefficients, p = 0.0273, monkey H).
quadratic coefficient below zero in 6 of 8; one-tailed signed-rank (coefficient < 0) p = 0.0547
       variant  n_negative  p_one_tailed                                               quad_coefs  seconds
8 dims, seed 1           6      0.054688 [-6.53, -6.56, 0.89, -2.27, -0.25, 6.19, -16.71, -19.45]      115
8 dims, seed 2           6      0.039062  [-6.47, -6.52, 0.77, -2.17, -0.92, 5.34, -16.1, -19.36]      114
8 dims, seed 3           6      0.054688   [-6.33, -6.4, 1.04, -2.25, -0.7, 6.17, -16.19, -19.13]      113
4 dims, seed 0           6      0.097656  [-7.23, -6.26, 0.95, -0.74, -1.27, 8.18, -19.86, -17.8]       71
main fit: 6 negative, p = 0.0547 | coefficients [-6.57, -6.48, 1.06, -2.13, -0.24, 6.0, -16.52, -19.27]
[gpfa-mean-sigmoid] The mean of the single-trial GPFA projections is sigmoidal (signed-rank test on inc
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
grep -o -i ".\{200\}available.\{200\}" $TMPDIR/paper.txt | head -8; grep -o -i ".\{100\}github.\{100\}" $TMPDIR/paper.txt | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n -i "availab\|request\|DATA AND CODE\|KEY RESOURCES" paper/10.1016-j.neuron.2019.06.012.txt | cut -c1-50; python3 - <<'EOF'
import re
t=open('paper/10.1016-j.neuron.2019.06.012.txt').read()
for m in re.finditer(r'(?i)(availab|upon request|on request)', t):
    print(t[max(0,m.start()-250):m.end()+150].replace('\n',' ')); print('---')
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
for q in "ready-set-go" "Jazayeri" "DMFC" "time interval reproduction"; do echo "== $q"; curl -s "https://api.dandiarchive.org/api/dandisets/?search=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&page_size=50" | python3 -c "import json,sys;d=json.load(sys.stdin);[print(r['identifier'],r['most_recent_published_version']['name'] if r.get('most_recent_published_version') else r['draft_version']['name']) for r in d['results']]"; done
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "entries/sohn-2019/README.md",
 "content": "# Sohn et al. (2019) from dandiset 000130\n\nTests the findings of [Sohn, Narain, Meirhaeghe and Jazayeri (2019)](https://doi.org/10.1016/j.neuron.2019.06.012)\nthat can be tested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version\n0.241017.1448. The dandiset was prepared for the Neural Latents Benchmark and holds one session\n(2016-12-11) of monkey H in the Ready-Set-Go task: 1160 trials with their task variables and the spikes\nof 54 units from dorsomedial frontal cortex, and 283 further trials whose task variables are withheld.\nThe paper pools 17 sessions of monkey H and 12 of monkey G.\n\n`reproduce_sohn_2019.ipynb` holds the behavioural, single-neuron and trial-averaged population\nanalyses (about 1 minute); `gpfa_sohn_2019.ipynb` holds the single-trial GPFA analyses (about 15\nminutes). Loading and measures are in `rsg.py`.\n\n| Claim | Outcome |\n|---|---|\n| Behavioural slopes between 0 and 1 | Not reproduced (Eye Short slopes at or above 1) |\n| Opposite biases at the overlapping 800 ms | Not reproduced |\n| Smaller tp increments at the extremes of the prior | Reproduced |\n| Smaller slopes for the Long prior | Reproduced, resting on an assumption |\n| Bayesian observer fits bias and variance | Partially reproduced |\n| GLM: 65% prior-dependent, 27% ts-dependent units | Not reproduced (79% and 46%) |\n| Largest prior effect at 800 ms during the support of the prior | Reproduced |\n| 3 to 4 and 5 to 10 principal components | Not reproduced |\n| Encoding-axis projections match the Bayesian estimate (R2) | Reproduced |\n| Bayesian model better than linear for projections | Partially reproduced |\n| No sigmoidal representation in \"Short In Long\" | Reproduced (by the paper's test) |\n| More neural bias for the Long prior | Partially reproduced |\n| Projection at Set predicts speed | Partially reproduced (stronger correlations) |\n| Initial speed biased toward the middle | Not reproduced (p = 0.055) |\n| Speed predicts mean tp | Partially reproduced (stronger correlations) |\n| Speed unmodulated during the support | Reproduced (by the paper's test) |\n| Post-Set trajectories parallel | Reproduced |\n| Distances fall steadily to Go | Not reproduced |\n| Inverted-U variance of GPFA projections | Not reproduced (p = 0.055) |\n| Sigmoidal mean of GPFA projections | Reproduced |\n| Recurrent network claims (2) | Blocked: data missing |\n| Monkey G | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and\nthe differences from the paper's method.\n\nWith one session, the population tests run over 4 effector and direction datasets in place of the\npaper's 8, so no signed-rank test over datasets can fall below p = 0.125, and the three claims of\nabsence are reproduced by tests that cannot find an effect. In this session the eye responses are\nnearly unbiased (slopes 0.85 to 1.11), which drives several of the behavioural outcomes.\n\nFound about the dataset: the test file withholds the task variables of 283 of the session's 1443\ntrials; the `iti` description reverses the two priors; `tp` exceeds `go_time - set_time` by a median\nof 17.9 ms without a description of how it is measured; units have no electrode assignment and no\nsingle or multi-unit label.\n"
}
```

```
File created successfully at: entries/sohn-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -n 1,30p attempts/asari-2009-01.yaml; grep -n "^findings" -A12 attempts/asari-2009-01.yaml | head -30
```

```
schema_version: 3
id: asari-2009-01
datasets:
- archive: crcns
  id: ac-1
  version: unversioned
  doi: 10.6080/K0KW5CXR
  relation: primary
paper: doi:10.1152/jn.00577.2009
date: '2026-11-13'
entry: asari-2009
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-15
  runner:
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/record.py <<'PYEOF'
import yaml
NB = "reproduce_sohn_2019.ipynb"; GN = "gpfa_sohn_2019.ipynb"
ONE = ("One session of monkey H (2016-12-11), where the paper pools 17 sessions of H and 12 of G; the 283 "
       "test-file trials of the session have no task variables and are not used.")
FOUR = ("Population tests run over the 4 effector and direction datasets of one session, where the paper has 8 "
        "(two animals); a signed-rank test over 4 values cannot fall below p = 0.125.")
def o(claim, outcome, notes, nb=NB, measured=None, deviations=None, assumed=None, blocked_by=None):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if outcome != "blocked":
        d["notebook"] = nb; d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed: d["assumed"] = True
    return d

outcomes = [
o("beh-slopes", "not_reproduced",
  "With an intercept, 6 of 8 weighted slopes lie between 0 and 1 and 5 of 8 intervals exclude both 0 and 1. The Eye Left Short "
  "(1.011, 95% CI 0.896 to 1.126) and Eye Right Short (1.110, 1.014 to 1.206) slopes are not below 1. The four Hand slopes are 0.50 "
  "to 0.86 with intervals excluding 0 and 1, and the Eye Long slopes are 0.845 and 0.903. Through the origin (the Methods' equation "
  "tp = beta ts) 2 of 8 slopes are below 1. Both readings give the same outcome.",
  deviations=[ONE,
   "The criterion does not say whether the regression has an intercept; the Methods (Analysis of behavior, Model free analysis) "
   "write tp = beta ts + epsilon. Both readings were run and give the same outcome.",
   "Trials are the completed trials not flagged by the file's is_outlier column (claims file); the mixture model is the file's, "
   "not refit here."]),
o("beh-overlap-prior", "not_reproduced",
  "At ts = 800 ms the median of tp - 800 is +28.3 ms for Short (n 93) and +47.6 ms for Long (n 107); the Short median is not "
  "negative, and the two-sided rank-sum test between priors gives p = 0.073. Per dataset only Hand Left has a negative Short median "
  "(-61.6 ms), the Long median is the larger in 2 of 4, and only Hand Right differs at p < 0.05 (p = 0.00099). The Eye Short "
  "medians are +79.1 and +40.9 ms.",
  deviations=[ONE + " The paper's p < 1e-43 pools 17 sessions."]),
o("beh-sigmoid-increments", "reproduced",
  "The middle increment of mean tp exceeds the extreme one in 7 of 8 prior, effector and direction conditions (Hand Left Short is "
  "the exception, -10.7 ms); two-sided signed-rank p = 0.0156. The paper's p < 1e-11 pools 17 sessions of monkey H.",
  deviations=[ONE]),
o("beh-long-more-bias", "reproduced",
  "With the intercept regression of beh-slopes the Long slope is below the Short slope in all 4 datasets (Eye Left 0.845 and 1.011, "
  "Eye Right 0.903 and 1.110, Hand Left 0.502 and 0.612, Hand Right 0.612 and 0.861). Through the origin it is below in 3 of 4 "
  "(Eye Right 1.027 against 1.016), which would be partially reproduced. The outcome rests on the intercept reading. Question for "
  "the paper's authors, does the weighted regression of tp on ts (Methods, Model free analysis of behavior, tp = beta ts + epsilon) "
  "include an intercept? The two readings differ here in one dataset.",
  deviations=[ONE,
   "Assumed that the regression of tp on ts has an intercept. The Methods write tp = beta ts + epsilon, without one, but the Results "
   "read slopes below 1 as bias toward the mean of the prior (Results, Task and behavior, paragraph 3), which is what a slope with "
   "an intercept measures; a slope through the origin mostly measures the overall ratio of tp to ts. Both readings are shown."],
  assumed=True),
o("beh-bayes-model", "partially_reproduced",
  "The correlation of observed and predicted SD of tp over the 10 conditions is positive in all 4 datasets (Eye Left 0.807, Eye "
  "Right 0.909, Hand Left 0.749, Hand Right 0.277 with p = 0.44). The bias R2 (1 - SS_res/SS_tot) reaches 0.8 in 2 of 4 (Hand Left "
  "0.978, Hand Right 0.865; Eye Left 0.670, Eye Right 0.122); the squared correlation gives the same count. Fitted wm are 0.025, "
  "0.013, 0.116 and 0.073 and wp 0.103, 0.106, 0.090 and 0.104. The Eye biases span only 108 and 80 ms over the 10 conditions, "
  "against 265 and 166 ms for Hand. Table S3 was not available for comparison.",
  deviations=[ONE,
   "The prior is continuous uniform over each range (claims file), where the Methods describe 5 discrete values; production noise "
   "is wp times te and the offset b is added to te (Methods, Analysis of behavior with a Bayesian model).",
   "Fit per effector and direction of one session, where the paper pools sessions per animal, effector and direction.",
   "R2 is read as 1 - SS_res/SS_tot of the observed biases around the predicted ones; the squared Pearson correlation is shown as "
   "a second reading and gives the same outcome."]),
o("glm-prior-ts", "not_reproduced",
  "38 of 48 units (79.2%, binomial 95% CI 65.0 to 89.5) are prior-dependent, against 65 +- 6.5%. Under reading (a), Long-prior "
  "windows ending at the Long ts values (800 to 1200 ms), 22 of 48 (45.8%, 31.4 to 60.8) are ts-dependent; under reading (b), the "
  "same 480 to 800 ms windows in both priors, 24 of 48 (50.0%), against 27 +- 2.7%. Both fractions are higher than the paper's for "
  "monkey H under both readings. 19 units are both and 7 neither.",
  measured=[79.2, 45.8],
  deviations=[ONE + " The paper's 65% and 27% are over 536 units of monkey H; here 48 units.",
   "For ts dependence the criterion gives each prior that prior's 5 time indicators. Reading (a) places the Long-prior windows "
   "before the Long ts values, following the Methods' sentence that two GLMs were used since values of ts were different between "
   "the priors (Generalized linear model); reading (b) keeps the 480 to 800 ms windows. Both run; both give the same outcome.",
   "BIC is -2 log-likelihood + k ln n of statsmodels' Poisson GLM, with the observations of all windows (3921 per unit for the "
   "prior test)."]),
o("dfr-overlap-support", "reproduced",
  "The RMS over units of the Long - Short rate difference at ts = 800, averaged over the 4 datasets, is largest in the 480 to 640 "
  "ms bin (6.86 spikes/s), above the 95th percentile of the maximum over 200 shuffles of the prior labels (3.15; largest shuffle "
  "3.46). The bin after Set, 800 to 960 ms, is next (6.07). Per dataset the largest bin is within 480 to 800 ms in 3 of 4; in Eye "
  "Left it is 800 to 960 ms (9.73). The datasets have 14 to 38 trials per prior at ts = 800.",
  deviations=[ONE]),
o("pca-dimensionality", "not_reproduced",
  "In the estimation epoch 2 components reach 75% of the variance in all 4 datasets (0.80 to 0.86 with 2, 0.87 to 0.91 with 3), so "
  "none is in 3 to 4. In the production epoch 2, 2, 4 and 5 components do (Eye Left, Eye Right, Hand Left, Hand Right), so 1 of 4 is "
  "in 5 to 11. 1 of 8 values is in range. Without smoothing the counts are 3 to 6 and 6 to 15, so they depend on the smoothing.",
  deviations=[ONE + " 48 units, where the paper's datasets pool the units of all sessions of an animal (536 for H).",
   "The Gaussian kernel is renormalised over the bins of each epoch so that no bin outside it enters (a standard choice the "
   "Methods do not fix)."]),
o("encoding-r2", "reproduced",
  "Reading (a), Hand Left, gives R2 of Xu by te of 0.9957 for Short and 0.9774 for Long; reading (b), the mean of the 4 datasets, "
  "0.9587 and 0.9822. All are within tolerance. Per dataset R2 is 0.909 to 0.996. The comparison with random axes is weak in the "
  "2-component estimation space; random unit vectors give median R2 of 0.69 to 0.99, 1.2% to 44.2% of them reach the R2 of u, and "
  "a linear function of ts gives R2 of 0.898 to 0.990.",
  measured=[0.9957, 0.9774],
  deviations=[FOUR, "te(t) uses the dataset's own fitted wm from beh-bayes-model, where the paper fits per animal, effector and "
   "direction over sessions."]),
o("encoding-bayes-beats-linear", "partially_reproduced",
  "The Bayesian fit has the lower RMSE in all 4 datasets for Short (differences -0.31, -0.22, -0.47 and -0.04 spikes/s for Eye "
  "Left, Eye Right, Hand Left, Hand Right) and in 3 of 4 for Long (-0.59, -0.20, +0.10, -0.22); for Hand Left Long the linear fit "
  "is better (0.481 against 0.583). Weighted RMSE gives the same counts. Signed-rank p over 4 datasets is 0.125 (Short) and 0.25 "
  "(Long).",
  deviations=[FOUR, "RMSE is the unweighted root mean square residual of the weighted fits; the weighted RMSE is shown as a variant "
   "and gives the same outcome."]),
o("short-in-long-control", "reproduced",
  "By the paper's test, the two-sided signed-rank test of the RMSE difference (Bayesian - linear) over the 4 datasets gives p = 0.25 "
  "with the axis built as u is (mean of difference vectors) and 0.125 with the single difference X(800) - X(480); with 4 datasets "
  "the test cannot reach p < 0.05. The effect does not look absent. The Bayesian model fits better in 3 of 4 datasets (-0.21, "
  "-0.12, +0.05, -0.11 spikes/s), of a size like the Short prior's own differences (-0.04 to -0.47). The paper's ANOVA interaction "
  "was not run.",
  deviations=[FOUR, "The axis is built from the mean of difference vectors between 480 and 800 ms, as for u (Methods, Analysis of "
   "neural projection, 'we applied the same projection analysis'); the single difference the criterion names is shown and gives "
   "the same outcome."]),
o("neural-long-more-bias", "partially_reproduced",
  "The weighted slope of Xu on ts is lower for Long in 3 of 4 datasets (Eye Left 0.229 and 0.124, Eye Right 0.191 and 0.117, Hand "
  "Left 0.077 and 0.027 spikes/s per ms, Short then Long); in Hand Right the Long slope is slightly higher (0.0486 against 0.0470). "
  "With outlier trials included the count is the same; without smoothing it is 4 of 4. Signed-rank p over 4 datasets is 0.25.",
  deviations=[FOUR]),
o("speed-vs-projection", "partially_reproduced",
  "Pooled over the 4 datasets (20 points per prior), Xu at Set correlates negatively with the speed of the production trajectory, "
  "r = -0.932 (p = 2.3e-09) for Short and -0.874 (p = 4.8e-07) for Long, both stronger than the paper's -0.74 and -0.51 and "
  "outside tolerance. Within datasets r is -0.92 to -0.995 (Short) and -0.67 to -0.96 (Long). With speed divided by the mean tp "
  "(the Methods' wording) r is -0.916 and -0.925.",
  measured=[-0.932, -0.874],
  deviations=[FOUR + " Xu scales differ between datasets and are pooled as they are, as the criterion says."]),
o("initial-speed-biased", "not_reproduced",
  "The measured slope of initial speed (Set to Set + 400 ms) on ts is shallower than the unbiased profile's in 7 of 8 dataset-priors "
  "(Eye Right Long is the exception, -0.0082 against -0.0065), but the two-sided signed-rank test of the difference gives p = 0.055. "
  "No trial had tp below 400 ms. The paper's p < 1e-3 combines both animals.",
  deviations=[FOUR, "Initial speed is measured in the production PC space of the dataset (Set to the shortest tp), the space of "
   "speed-vs-projection; the claims file names the step distance, not the space."]),
o("speed-predicts-tp", "partially_reproduced",
  "Pooled over the 4 datasets, speed correlates negatively with mean tp, r = -0.719 (p = 0.00035) for Short and -0.744 (p = 0.00017) "
  "for Long, both outside tolerance around -0.58 and -0.52. Within datasets r is -0.94 to -0.99 (Short) and -0.78 to -0.97 (Long). "
  "Trial by trial, single-trial speed (Set to Go) correlates with tp at r = -0.15 to -0.71 in the 8 prior, effector and direction "
  "groups, with p < 0.05 in 7.",
  measured=[-0.719, -0.744],
  deviations=[FOUR, "The single-trial speed variant uses smoothed single-trial rates in the dataset's production PC space; the "
   "Neural Latents Benchmark's own computation was not used."]),
o("alt-speed-unmodulated", "reproduced",
  "By the paper's test, the two-sided signed-rank tests of the 4 slopes against zero give p = 0.25 (Short) and 0.125 (Long); with 4 "
  "datasets the test cannot reach p < 0.05. The effect sizes lean toward modulation. The slope of step distance on time is positive "
  "in 7 of 8 dataset-priors, the step distance changes by -13% to +56% over the support, and percentile bootstrap intervals over "
  "trials exclude zero in 6 of 8. These intervals sit mostly above the point estimates, so they are biased upward. Attrition halves "
  "and more the trials averaged across the support, which adds noise to the later steps; this may contribute to the positive "
  "slopes and was not tested.",
  deviations=[FOUR, "Bootstrap of trials within each ts, 200 resamples (a standard choice)."]),
o("alt-transient-parallel", "reproduced",
  "PCA on Set to Set + 200 ms keeps 1 to 4 components. The two-sided signed-rank tests of the 8 slopes against zero give p = 0.195 "
  "for the shortest ts and 1.0 for the longest. For the longest ts the median change over 200 ms is 0.07 spikes/s against a median "
  "distance of 22.3. For the shortest ts the distance grows in 6 of 8 dataset-priors (median change 14.5 against a median starting "
  "distance of 18.2), a divergence, not the convergence the transient hypothesis predicts.",
  deviations=[FOUR]),
o("alt-threshold-monotonic", "not_reproduced",
  "With 60% of the variance (1 to 3 components) the median time of the minimum distance to the middle-ts trajectory is 230 ms "
  "before Go; the minimum is in the last 40 ms in 4 of 32 curves and in the last 200 ms in 13. With 75% (2 to 5 components) the "
  "median is 160 ms before Go (8 of 32 in the last 40 ms), which would be partially reproduced. The minima spread from 760 ms before "
  "Go to Go.",
  deviations=[FOUR, "Times are bin ends of 20 ms bins aligned to Go; for Short trials the window starts before Set, as the "
   "Methods' window Go - 800 ms to Go implies."]),
o("gpfa-variance-inverted-u", "not_reproduced",
  "Cross-validation chose 8 latent dimensions in all 4 datasets. The quadratic coefficient of variance on ts is negative in 6 of 8 "
  "dataset-priors and the one-tailed signed-rank test gives p = 0.0547. The result sits at the threshold; refits with three other "
  "seeds give p = 0.055, 0.039 and 0.055, and 4 latent dimensions p = 0.098, with 6 of 8 negative each time. The mean variance "
  "profile by ts rank (0.78, 0.91, 0.85, 0.51, 0.45) falls toward the long end. Variances rest on 14 to 38 trials per ts.",
  nb=GN,
  deviations=[FOUR + " The paper used one high-yield session of 48 units for H; this session has 48 selected units, but whether it "
   "is that session is not stated.",
   "GPFA is elephant 1.2.1's port of Yu et al. (2009), not the paper's MATLAB code; it fits on 20-bin segments with random overlaps "
   "(elephant's default), seeded here."]),
o("gpfa-mean-sigmoid", "reproduced",
  "The middle increment of the mean GPFA projection exceeds the extreme one in 7 of 8 dataset-priors (two-sided signed-rank "
  "p = 0.0156), and the slope of the mean projection on ts is higher for Short than for Long in all 4 datasets (one-tailed "
  "p = 0.0625, the paper's value).",
  nb=GN, deviations=[FOUR]),
o("rnn-curved-manifold", "blocked",
  "The claim is about recurrent networks the authors trained; neither the networks nor their training code are in the dandiset, "
  "and the paper says the code is available from the corresponding author on request (Data and code availability). No other "
  "dandiset of this paper was found by searching the archive for Jazayeri, DMFC and the task.",
  blocked_by="data_missing"),
o("rnn-perturbation", "blocked",
  "Needs the trained recurrent networks, which are not public (see rnn-curved-manifold).", blocked_by="data_missing"),
o("monkey-g", "blocked",
  "The dandiset holds one session of monkey H only; monkey G's 12 sessions are not in it, and no other dandiset holding them was "
  "found by searching the archive.", blocked_by="data_missing"),
]

rec = {
 "schema_version": 3, "id": "sohn-2019-02",
 "datasets": [{"archive": "dandi", "id": "000130", "version": "0.241017.1448",
               "doi": "10.48324/dandi.000130/0.241017.1448", "relation": "primary"}],
 "paper": "doi:10.1016/j.neuron.2019.06.012", "date": "2026-11-15", "entry": "sohn-2019",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-15"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/43684558521"}},
 "inputs": [{"what": "GPFA implementation (Yu et al. 2009) used for the two GPFA claims, as the software package elephant 1.2.1, "
             "pinned in the entry's lock file; no data", "source": "https://pypi.org/project/elephant/1.2.1/"}],
 "outcomes": outcomes,
 "findings": [
  {"kind": "data_missing", "statement":
   "The dandiset holds one of the paper's 29 sessions (2016-12-11, monkey H). The other 16 sessions of monkey H, all 12 sessions of "
   "monkey G, and the trained recurrent networks are not in it, and no other dandiset holds them. Results that pool sessions or "
   "animals can be tested only on one session, and the monkey G and network findings not at all."},
  {"kind": "data_missing", "statement":
   "The test file's 283 trials (about 20% of the session's 1443) hold only a go_time per 1.7 s segment, for 40 of the 54 units. "
   "Their prior, ts, effector, direction and Ready and Set times are withheld for the Neural Latents Benchmark, so they cannot be "
   "used for any of the paper's analyses. Their spikes are not repeated in the train file."},
  {"kind": "metadata_error", "statement":
   "The description of the trial column iti says it is 500 ms for Short-prior trials and 1220 ms for Long-prior trials. The values "
   "are the reverse (1220 ms in all 577 Short trials, 500 ms in all 583 Long trials), as the paper's Methods give."},
  {"kind": "metadata_insufficient", "statement":
   "tp is longer than go_time - set_time in every analysed trial, by a median of 17.9 ms (0.1 to 200.6 ms), and set_time - "
   "ready_time differs from ts by up to 23.5 ms. The files do not say between which events tp is measured or how the event times "
   "were registered."},
  {"kind": "metadata_insufficient", "statement":
   "Units have no electrode or probe assignment (the unit table has no electrodes column and the 72 electrodes have no positions), "
   "and no label says which units are single units and which multi-units, a distinction the paper reports (196 single and 421 "
   "multi-units in monkey H)."},
  {"kind": "methods_unavailable", "statement":
   "The Methods give the behavioural regression as tp = beta ts + epsilon, without an intercept, while the Results read slopes "
   "below 1 as bias toward the prior mean. Does the regression include an intercept? In this session the two readings give "
   "different counts of datasets with a smaller Long-prior slope (4 of 4 with an intercept, 3 of 4 without). The attempt assumes "
   "an intercept."},
  {"kind": "paper_inconsistency", "statement":
   "The Data and code availability statement says the published article includes all datasets generated or analyzed, but the "
   "recordings of 28 of the 29 sessions are not public, and the dandiset the paper is linked to holds one session."},
 ],
}

class D(yaml.SafeDumper):
    pass
def str_rep(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)
D.add_representer(str, str_rep)
out = yaml.dump(rec, Dumper=D, sort_keys=False, width=110, allow_unicode=True)
open("attempts/sohn-2019-02.yaml", "w").write(out)
print(len(out))
PYEOF
. $TMPDIR/env/bin/activate; python $TMPDIR/record.py && cd  && grep -n "^- claim\|^  outcome" attempts/sohn-2019-02.yaml | head -50 | paste - - | head -30
```

```
23558
28:- claim: beh-slopes	29:  outcome: not_reproduced
44:- claim: beh-overlap-prior	45:  outcome: not_reproduced
55:- claim: beh-sigmoid-increments	56:  outcome: reproduced
65:- claim: beh-long-more-bias	66:  outcome: reproduced
83:- claim: beh-bayes-model	84:  outcome: partially_reproduced
102:- claim: glm-prior-ts	103:  outcome: not_reproduced
123:- claim: dfr-overlap-support	124:  outcome: reproduced
135:- claim: pca-dimensionality	136:  outcome: not_reproduced
149:- claim: encoding-r2	150:  outcome: reproduced
165:- claim: encoding-bayes-beats-linear	166:  outcome: partially_reproduced
178:- claim: short-in-long-control	179:  outcome: reproduced
193:- claim: neural-long-more-bias	194:  outcome: partially_reproduced
204:- claim: speed-vs-projection	205:  outcome: partially_reproduced
219:- claim: initial-speed-biased	220:  outcome: not_reproduced
231:- claim: speed-predicts-tp	232:  outcome: partially_reproduced
247:- claim: alt-speed-unmodulated	248:  outcome: reproduced
261:- claim: alt-transient-parallel	262:  outcome: reproduced
273:- claim: alt-threshold-monotonic	274:  outcome: not_reproduced
286:- claim: gpfa-variance-inverted-u	287:  outcome: not_reproduced
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('record.py').read()
s=s.replace('''Attrition halves "
  "and more the trials averaged across the support, which adds noise''','''Attrition reduces "
  "the trials averaged about five-fold across the support, which adds noise''')
a=s.index('  {"kind": "paper_inconsistency"'); b=s.index(' ],\n}',a)
s=s[:a]+s[b:]
a=s.index(' "inputs": ['); b=s.index(' "outcomes": outcomes,')
s=s[:a]+s[b:]
open('record.py','w').write(s)
EOF
. env/bin/activate; python record.py; cd  grep -n "five-fold\|paper_inconsistency\|inputs" attempts/sohn-2019-02.yaml; grep -c "^ *[a-z_]*: ['\"]" attempts/sohn-2019-02.yaml; grep -n ": '" attempts/sohn-2019-02.yaml | head; python -c "import yaml;yaml.safe_load(open('attempts/sohn-2019-02.yaml'))" && python tools/entry.py check entries/sohn-2019
```

```
23070
251:    mostly above the point estimates, so they are biased upward. Attrition reduces the trials averaged about five-fold
2
5:  id: '000130'
10:date: '2026-11-15'
0 error(s)
```

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" attempts/sohn-2019-02.yaml entries/sohn-2019/*.py entries/sohn-2019/*.md entries/sohn-2019/*.ipynb $TMPDIR/build_*.py | head; grep -o "\*\*[^*]*\*\*" entries/sohn-2019/*.ipynb entries/sohn-2019/README.md | sort | uniq -c | sort -rn | head
```

```
6 entries/sohn-2019/reproduce_sohn_2019.ipynb:**Result: reproduced.**
      6 entries/sohn-2019/reproduce_sohn_2019.ipynb:**Result: not reproduced.**
      5 entries/sohn-2019/reproduce_sohn_2019.ipynb:**Result: partially reproduced.**
      1 entries/sohn-2019/reproduce_sohn_2019.ipynb:**Result: reproduced, resting on an assumption.**
      1 entries/sohn-2019/reproduce_sohn_2019.ipynb:**0.241017.1448**
      1 entries/sohn-2019/reproduce_sohn_2019.ipynb:** 2)), rmse_linear=np.sqrt(np.mean((q[\"xu\"] - f_ts) **
      1 entries/sohn-2019/reproduce_sohn_2019.ipynb:** 2)) - np.sqrt(np.mean((q[\"xu\"] - f_ts) **
      1 entries/sohn-2019/reproduce_sohn_2019.ipynb:** 2) / np.sum((bias_o - bias_o.mean()) **
      1 entries/sohn-2019/gpfa_sohn_2019.ipynb:**Result: reproduced.**
      1 entries/sohn-2019/gpfa_sohn_2019.ipynb:**Result: not reproduced.**
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/version\n\*\*0.241017.1448\*\*/X/' build_main.py && python - <<'EOF'
for f in ['build_main.py','build_gpfa.py']:
    s=open(f).read(); s=s.replace('**0.241017.1448**','0.241017.1448'); open(f,'w').write(s)
EOF
. env/bin/activate && python build_main.py && python build_gpfa.py && cd  && grep -c "\*\*0.24" entries/sohn-2019/*.ipynb; date -u; python tools/entry.py all entries/sohn-2019 2>&1 | tail -4; date -u
```

```
77 cells
17 cells
entries/sohn-2019/gpfa_sohn_2019.ipynb:0
entries/sohn-2019/reproduce_sohn_2019.ipynb:0
Sun Nov 15 07:45:14 UTC 2026
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (60 s)
pass  gpfa_sohn_2019.ipynb  (964 s)
Sun Nov 15 08:02:28 UTC 2026
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/env/bin/activate; python $TMPDIR/show.py executed/sohn-2019/gpfa_sohn_2019.ipynb > $TMPDIR/g2.txt; python $TMPDIR/show.py executed/sohn-2019/reproduce_sohn_2019.ipynb > $TMPDIR/m2.txt; diff <(grep -v "seconds\|runtime\| s$\|; [0-9]* s" $TMPDIR/g_final.txt) <(grep -v "seconds\|runtime\| s$\|; [0-9]* s" $TMPDIR/g2.txt) | grep -v "^[<>] [48] dims" | head; diff <(grep -v "took\|runtime" $TMPDIR/m_final.txt) <(grep -v "took\|runtime" $TMPDIR/m2.txt) | head; grep runtime $TMPDIR/g2.txt $TMPDIR/m2.txt; python tools/entry.py handover entries/sohn-2019 2>&1 | tail -5; ls executed/sohn-2019/handover
```

```
44,47c44,47
---
499a500
> 
/tmp/claude-1001/g2.txt:runtime 961 s; peak memory 0.41 GB
/tmp/claude-1001/m2.txt:runtime 53 s; peak memory 0.57 GB
wrote executed/sohn-2019/handover
gpfa_sohn_2019.ipynb
reproduce_sohn_2019.ipynb
rsg.py
sohn-2019.yaml
```

**Agent calls Bash**

```bash
sed -i 's/  runtime_minutes: 9/  runtime_minutes: 16/' entries/sohn-2019/entry.yaml && sed -i 's/GPFA analyses (about 15$/GPFA analyses (about 16/' entries/sohn-2019/README.md && grep -n "runtime_minutes" entries/sohn-2019/entry.yaml && grep -n "about 1[56]" entries/sohn-2019/README.md; python tools/entry.py run entries/sohn-2019 2>&1 | tail -3
```

```
17:  runtime_minutes: 2
20:  runtime_minutes: 16
11:analyses (about 1 minute); `gpfa_sohn_2019.ipynb` holds the single-trial GPFA analyses (about 16
Installed kernelspec registry-sohn-2019 in executed/sohn-2019/.venv/share/jupyter/kernels/registry-sohn-2019
pass  reproduce_sohn_2019.ipynb  (74 s)
pass  gpfa_sohn_2019.ipynb  (1098 s)
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/env/bin/activate; python $TMPDIR/show.py executed/sohn-2019/gpfa_sohn_2019.ipynb > $TMPDIR/g3.txt; python $TMPDIR/show.py executed/sohn-2019/reproduce_sohn_2019.ipynb > $TMPDIR/m3.txt; diff <(grep -v "seconds\|runtime\| s$\|; [0-9]* s\|dims, seed" $TMPDIR/g2.txt) <(grep -v "seconds\|runtime\| s$\|; [0-9]* s\|dims, seed" $TMPDIR/g3.txt); diff <(grep -v "took\|runtime" $TMPDIR/m2.txt) <(grep -v "took\|runtime" $TMPDIR/m3.txt); grep "dims, seed" $TMPDIR/g3.txt; python tools/entry.py check entries/sohn-2019 && python tools/entry.py handover entries/sohn-2019 | tail -1; git status --short 2>/dev/null | head; date -u
```

```
90a91
> 
96d96
< 
500d499
< 
8 dims, seed 1           6      0.054688 [-6.53, -6.56, 0.89, -2.27, -0.25, 6.19, -16.71, -19.45]      143
8 dims, seed 2           6      0.039062  [-6.47, -6.52, 0.77, -2.17, -0.92, 5.34, -16.1, -19.36]      139
8 dims, seed 3           6      0.054688   [-6.33, -6.4, 1.04, -2.25, -0.7, 6.17, -16.19, -19.13]      139
4 dims, seed 0           6      0.097656  [-7.23, -6.26, 0.95, -0.74, -1.27, 8.18, -19.86, -17.8]       88
0 error(s)
wrote executed/sohn-2019/handover
Sun Nov 15 08:22:59 UTC 2026
```

**Agent**

I've finished the blind repeat attempt on sohn-2019 (DANDI:000130, version 0.241017.1448) through handover. `entry.py check` reports 0 errors, both notebooks pass from a clean environment, and the verifier's package is built in `executed/sohn-2019/handover/`. I did not come across any earlier attempt's results.

## 1. Outcomes per claim

| claim | outcome | key numbers |
|---|---|---|
| beh-slopes | not reproduced | Eye Short slopes are 1.011 and 1.110; same outcome with or without an intercept |
| beh-overlap-prior | not reproduced | at ts = 800 ms the Short median bias is +28.3 ms, Long +47.6 ms; p = 0.073 |
| beh-sigmoid-increments | reproduced | 7 of 8, p = 0.0156 |
| beh-long-more-bias | reproduced, resting on an assumption | 4 of 4 with an intercept, 3 of 4 without |
| beh-bayes-model | partially reproduced | SD correlation positive in 4 of 4; bias R2 ≥ 0.8 in only 2 of 4 (the Eye datasets fail) |
| glm-prior-ts | not reproduced | 79.2% prior-dependent, 45.8% ts-dependent (expected 65% and 27%) |
| dfr-overlap-support | reproduced | peak in the 480–640 ms bin, 6.86 against a shuffle 95th percentile of 3.15 |
| pca-dimensionality | not reproduced | 1 of 8 counts in range; 2 estimation components in every dataset |
| encoding-r2 | reproduced | Hand Left 0.996 and 0.977 |
| encoding-bayes-beats-linear | partially reproduced | Short 4 of 4, Long 3 of 4 |
| short-in-long-control | reproduced (paper's test, p = 0.25) | but the Bayesian model fits better in 3 of 4 datasets |
| neural-long-more-bias | partially reproduced | 3 of 4 |
| speed-vs-projection | partially reproduced | r = −0.93 and −0.87, stronger than the paper's |
| initial-speed-biased | not reproduced | 7 of 8 shallower, p = 0.055 |
| speed-predicts-tp | partially reproduced | r = −0.72 and −0.74, stronger than the paper's |
| alt-speed-unmodulated | reproduced (paper's test) | but slopes are positive in 7 of 8 |
| alt-transient-parallel | reproduced | p = 0.195 and 1.0 |
| alt-threshold-monotonic | not reproduced | median minimum 230 ms before Go |
| gpfa-variance-inverted-u | not reproduced | 6 of 8 negative, p = 0.055; seed and dimension variants give 0.039 to 0.098 |
| gpfa-mean-sigmoid | reproduced | |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked, data_missing | |

## 2. Dataset, assumptions, questions

What I found about the dataset:
- **One session only.** It holds one of the paper's 29 sessions (monkey H, 2016-12-11).
- **Test-file trials unusable.** The test file's 283 trials have no task variables (prior, ts, effector, direction), so about 20% of the session cannot be analysed. Their spikes are not repeated in the train file.
- **`iti` description reversed.** It says 500 ms for Short and 1220 ms for Long; the values are the other way round, which matches the paper.
- **`tp` measurement undocumented.** `tp` is longer than `go_time − set_time` by a median of 17.9 ms, and the files don't say how it is measured.
- **Missing unit labels.** Units have no electrode assignment and no single-unit or multi-unit label.
- **Clock check passes.** Spikes share the trial clock: target direction decodes at 0.76 accuracy at the true times and about 0.5 when the times are shifted.

I made one assumption: the behavioural regression has an intercept. I recorded it as a question for the paper's authors (a `methods_unavailable` finding), because the Methods write `tp = β ts` without one. I asked readers no questions.

## 3. Where the protocol was unclear

1. **Absence claims that cannot fail.** The three absence claims are tested by a signed-rank test over 4 datasets, which cannot go below p = 0.125, so they are reproduced before any data are seen. I followed the criteria and reported effect sizes, which lean against absence.
2. **A seed that changes the outcome.** The protocol treats a random seed as unable to change an outcome, but elephant's GPFA draws random trial segments, and the result crossed p = 0.05 between runs. I seeded every fit, showed three other seeds plus the 4-dimension fit, and kept the main fit's outcome.
3. **How far to run standard choices.** Many small choices could matter for close calls: smoothing at epoch edges, where a time bin is placed, whether outlier trials enter the neural averages. Running every combination isn't practical, so I added one robustness table (outlier trials included; no smoothing).
4. **Where third-party method code goes.** The protocol doesn't say whether software implementing the paper's method (elephant's GPFA) belongs under `inputs`. I recorded it as a deviation instead.
5. **archives.md download step.** DANDI's signed download URL refuses HEAD requests (403), so the step in archives.md fails as written. I took the S3 URL from each asset's metadata.

## 4. Runtime and failures

- **Runtime.** The main notebook takes about 1 minute; the GPFA notebook takes 15 to 18 minutes. Peak memory was 0.6 GB. Work ran from 06:15 to about 08:25 UTC.
- **Fixed during development.** Early GPFA runs were not repeatable because elephant's random generator wasn't seeded; that is fixed, and the last three runs gave identical numbers. A smaller elephant time-bin rounding issue (spikes dropped at trial ends) is also fixed.
- **Nothing failed in the final run.**

Files are in `entries/sohn-2019/` and the record is `attempts/sohn-2019-02.yaml`.

## End of run

85 turns, 123 minutes, $7.45 at API prices, result: success.
