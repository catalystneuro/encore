# hasnain-2025 · author · run 44974161321

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
[... 760 more lines not kept]
```

```
Sun Nov 22 02:05:07 UTC 2026
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
[... 1113 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/hasnain-2025.yaml"
}
```

```
1	# Claims for Hasnain, Han & Economo (2025), "Mapping neural subspace dynamics onto the structure
2	# of the mouse descending motor system", bioRxiv doi:10.1101/2025.10.17.682917, tested on
3	# DANDI:000363 (Mesoscale Activity Map Dataset), which the paper reuses.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-22,
5	# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
6	#
7	# Text read. The preprint (version 1, posted 2025-10-17), full text from PMC (PMC12632980), in
8	# paper/10.1101-2025.10.17.682917.txt: Abstract, Introduction, Results, Discussion, Methods, the
9	# legends of Extended Data Figures 1 to 3, and the legends of Figures 1 to 4. The paper has no
10	# separate supplement (PMC lists none); the Extended Data legends are in the text. No PDF was
11	# supplied, so no figure was read; every claim rests on the text.
12	#
13	# Code read. github.com/economolab/subspaceID, commit d593949fef8a39fe0a6eb54a21fc05cbca7bae84,
14	# the only code the paper links ("Code for identifying movement-null and movement-potent
15	# subspaces"). It holds orthogonal_subspaces.m (the manopt optimization of the Methods'
16	# objective, each term normalized by the sum of the top-d eigenvalues of its covariance, with a
17	# regularization weight alpha that example.m sets to 0), example.m (z-scores each neuron over all
18	# bins and trials, takes the covariance of stationary and of moving bins, fixes 15 dimensions per
19	# subspace, rng(101)), and a Python port (funcs.py, example.ipynb). It holds none of the paper's
20	# other analyses (session selection, movement masks, dimensionality, variance explained,
[... 508 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md paper/*; ls entries/fouke-2025; cat papers/datasets/hasnain-2025.yaml; ls questions | grep hasn; ls papers/author-notes 2>/dev/null | grep hasn
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.17.682917.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1101-2025.10.17.682917.txt').read()
i=s.find('Neural net', 54000)
print(s[i:i+30000])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/692f4cef-ab29-4885-8c4d-04ce2c48eac9/tool-results/bsv0dkitd.txt"
}
```

```
1	Neural network models Neural network models were trained to predict single trial neural firing rates from orofacial movements ( Fig. 3a ). Orofacial movements were provided to the network as input in the form of singular vectors of video data and motion energy data. Video data from both the side view and the bottom view were concatenated so that both movement direction and amplitude could be captured. 100 video and 100 motion energy singular vectors (SV) were obtained through the Facemap GUI 68 . Training data consisted of 70% of trials and the remaining trials were used for testing. Before splitting the data into train/test sets, the number of left and right trials were sampled without replacement equal to the minimum number of trials between the trial types. The neural network architecture was kept the same as in ref 68 , consisting of an initial one-dimensional convolutional layer that learned ten temporal filters from the input data, followed by a 2-layer feedforward network with ReLU nonlinearity, and a final readout layer that transformed learned features to predictions of single trial firing rates. The feedforward layers had dimensionalities of 50 and 256. The readout layer was a fully-connected layer with output dimensions equal to the number of neurons in a session. Dropout with a probability of 0.2 was added to the feedforward layers. Individual networks were trained to predict neural activity from each session over 1000 epochs or until the test loss decreased by less than 1 × 10 −5 for 20 consecutive epochs. The learning rate was initialized at 1 × 10 −2 and decreased by 10% if the test loss increased for 5 consecutive epochs. Optimization was performed using the AdamW optimizer in PyTorch. Equal numbers of left and right trials were sampled and subsequently divided into an 80/20 train/test split. The variance explained of a single neuron’s firing rates were calculated as: V E = 1 - ∑ t x t - x ^ t 2 ∑ t x t - x ¯ 2 where x t is the single trial firing 
[... 1 more lines not kept]
```

**Agent**

Paper read. Now the example entry format and archive docs.

**Agent calls Bash**

```bash
cd  cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in entries/fouke-2025/README.md; cat attempts/fouke-2025-01.yaml; head -60 entries/fouke-2025/omr.py; grep -n "DANDI" -A60 docs/archives.md | head -120
```

```
<persisted-output>
Output too large (49.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/692f4cef-ab29-4885-8c4d-04ce2c48eac9/tool-results/bzfei3dlz.txt

Preview (first 2KB):
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
  runtime_minutes: 6
helpers:
- omr.py
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/692f4cef-ab29-4885-8c4d-04ce2c48eac9/tool-results/bzfei3dlz.txt"
}
```

```
1	schema_version: 1
2	name: fouke-2025
3	type: reproduction
4	title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
5	description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
6	  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
7	  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
8	  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
9	  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
10	license: Apache-2.0
11	notebooks:
12	- path: reproduce_fouke_2025.ipynb
13	  title: Reproducing Fouke et al. (2025) from dandiset 001453
14	  runtime_minutes: 6
15	helpers:
16	- omr.py
17	related:
18	- id: dandi:001453/0.250518.1950
19	  relation: uses_data
20	- id: doi:10.1016/j.cub.2025.04.027
[... 873 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000363/versions/" | python3 -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000363/" | python3 -m json.tool | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000363/versions/" | python3 -c "
import json,sys; [print(r['version'],r['asset_count'],r['size'],r['created']) for r in json.load(sys.stdin)['results']]"
curl -s "https://api.dandiarchive.org/api/dandisets/000363/versions/0.231012.2129/assets/?page_size=200" > assets.json
python3 -c "
import json; d=json.load(open('assets.json')); print(d['count'])
for a in d['results']: print(a['path'], round(a['size']/1e9,2))
" | head -200
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && source env/bin/activate && uv pip install -q dandi pynwb remfile h5py numpy scipy scikit-learn pandas matplotlib umap-learn pymanopt 2>&1 | tail -3; python -c "import pynwb, remfile, umap, pymanopt; print(pynwb.__version__, pymanopt.__version__)"
```

```
4.2.0 2.2.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > probe.py <<'EOF'
import time, h5py, remfile, json, sys
from dandi.dandiapi import DandiAPIClient
t=time.time()
c=DandiAPIClient(); ds=c.get_dandiset("000363","0.231012.2129")
path=sys.argv[1]
a=ds.get_asset_by_path(path)
url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),"r")
def walk(g,pre=""):
    for k in g:
        o=g[k]
        if isinstance(o,h5py.Dataset):
            print(pre+k, o.shape, o.dtype)
        else:
            attrs={kk:(v if not hasattr(v,'shape') or v.size<5 else '...') for kk,v in o.attrs.items() if kk in('neurodata_type','description','colnames','unit','rate','conversion')}
            print(pre+k+"/", attrs)
            if k in ('acquisition',) : 
                for kk in o: print(pre+"  "+kk, dict(o[kk].attrs).get('neurodata_type'))
                continue
            walk(o,pre+"  ")
walk(f)
print("time",time.time()-t)
EOF
python probe.py sub-440956/sub-440956_ses-20190208T133600_behavior+ecephys+ogen.nwb 2>&1 | head -300
```

```
acquisition/ {}
  BehavioralEvents BehavioralEvents
  BehavioralTimeSeries BehavioralTimeSeries
analysis/ {}
file_create_date (1,) object
general/ {}
  data_collection () object
  devices/ {}
    18005110031 (neuropixels 1.0 - 3B)/ {'description': 'neuropixels 1.0 - 3B', 'neurodata_type': 'Device'}
    18005117122 (neuropixels 1.0 - 3B)/ {'description': 'neuropixels 1.0 - 3B', 'neurodata_type': 'Device'}
    18005117412 (neuropixels 1.0 - 3B)/ {'description': 'neuropixels 1.0 - 3B', 'neurodata_type': 'Device'}
    18005118502 (neuropixels 1.0 - 3B)/ {'description': 'neuropixels 1.0 - 3B', 'neurodata_type': 'Device'}
    OBIS470/ {'neurodata_type': 'Device'}
  experiment_description () object
  experimenter (1,) object
  extracellular_ephys/ {}
    18005110031 1-281/ {'description': '{"probe": "18005110031", "probe_type": "neuropixels 1.0 - 3B", "electrode_config_name": "1-281", "subject_id": 440956, "session": 2, "insertion_number": 1, "probe_comment": "", "electrode_config_hash": "1497a7be87e3c11ebd33da9f574200d9"}', 'neurodata_type': 'ElectrodeGroup'}
      device/ {'description': 'neuropixels 1.0 - 3B', 'neurodata_type': 'Device'}
    18005117122 1-384/ {'description': '{"probe": "18005117122", "probe_type": "neuropixels 1.0 - 3B", "electrode_config_name": "1-384", "subject_id": 440956, "session": 2, "insertion_number": 4, "probe_comment": "", "electrode_config_hash": "4ae1f6ed4687467836d43369e548fe00"}', 'neurodata_type': 'ElectrodeGroup'}
      device/ {'description': 'neuropixels 1.0 - 3B', 'neurodata_type': 'Device'}
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > probe2.py <<'EOF'
import time, h5py, remfile, sys, numpy as np, collections
from dandi.dandiapi import DandiAPIClient
t=time.time()
ds=DandiAPIClient().get_dandiset("000363","0.231012.2129")
a=ds.get_asset_by_path(sys.argv[1])
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),"r")
print("open",time.time()-t)
for g in ['acquisition/BehavioralEvents','acquisition/BehavioralTimeSeries']:
    for k in f[g]:
        o=f[g][k]; print(g,k,dict((kk,v) for kk,v in o.attrs.items() if kk in('description','comments')))
        for kk in o: print('   ',kk,o[kk].shape, dict(o[kk].attrs))
for k in f['processing']: print('proc',k,list(f['processing'][k]))
u=f['units']
dec=lambda x:[v.decode() if isinstance(v,bytes) else v for v in x]
for col in ['unit_quality','classification','anno_name']:
    print(col, collections.Counter(dec(u[col][:])).most_common(40))
print(f['general/session_description'][()], f['general/experiment_description'][()] if 'experiment_description' in f['general'] else '')
print(f['session_description'][()])
tr=f['intervals/trials']
for col in ['outcome','trial_instruction','early_lick','task','photostim_duration','photostim_onset']:
    print(col, collections.Counter(dec(tr[col][:])).most_common(10))
print(tr['start_time'][:5], tr['stop_time'][:5])
print(dict(tr.attrs))
for k in tr: print(k, dict(tr[k].attrs).get('description'))
print("total",time.time()-t)
EOF
python probe2.py sub-440956/sub-440956_ses-20190208T133600_behavior+ecephys+ogen.nwb 2>&1 | head -150
```

```
open 0.9243366718292236
acquisition/BehavioralEvents delay_start_times {'comments': 'no comments', 'description': 'Timestamps for event type: delay - Start Time'}
    data (505,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
    timestamps (505,) {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/BehavioralEvents delay_stop_times {'comments': 'no comments', 'description': 'Timestamps for event type: delay - Stop Time'}
    data (505,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
    timestamps (505,) {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/BehavioralEvents go_start_times {'comments': 'no comments', 'description': 'Timestamps for event type: go - Start Time'}
    data (480,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
    timestamps (480,) {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/BehavioralEvents go_stop_times {'comments': 'no comments', 'description': 'Timestamps for event type: go - Stop Time'}
    data (480,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
    timestamps (480,) {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/BehavioralEvents left_lick_times {'comments': 'no comments', 'description': 'Timestamps for event type: left lick'}
    data (3130,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
    timestamps (3130,) {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/BehavioralEvents photostim_start_times {'comments': 'no comments', 'description': 'Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied'}
    control (126,) {}
    control_description (2,) {}
    data (126,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mW
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > probe3.py <<'EOF'
import time, h5py, remfile, sys, numpy as np, collections
from dandi.dandiapi import DandiAPIClient
ds=DandiAPIClient().get_dandiset("000363","0.231012.2129")
a=ds.get_asset_by_path(sys.argv[1])
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),"r")
dec=lambda x:[v.decode() if isinstance(v,bytes) else v for v in x]
e=f['general/extracellular_ephys/electrodes']
loc=dec(e['location'][:])
print(collections.Counter(loc).most_common(8))
print(dec(e['group_name'][:3]), e['x'][:3], e['y'][:3], e['z'][:3], e['rel_x'][:3])
for k in e: print(k, dict(e[k].attrs).get('description'))
u=f['units']
for k in u: print('U',k, dict(u[k].attrs).get('description'))
q=np.array(dec(u['unit_quality'][:])); c=np.array(dec(u['classification'][:])); an=np.array(dec(u['anno_name'][:]))
print(collections.Counter(zip(q,c)))
print('anno empty vs class', collections.Counter(zip(an=='',c)))
eg=u['electrode_group'][:]
print(eg[:3])
print(collections.Counter([f[r].name for r in eg]))
el=u['electrodes'][:]; print(el[:5], u['electrodes_index'][:5])
print(collections.Counter([loc[i] for i in el]).most_common(10))
print(f['general/session_description'] if 'session_description' in f['general'] else '', f['general/experiment_description'][()])
tr=f['intervals/trials']
for col in ['outcome','trial_instruction','early_lick','task','photostim_duration','photostim_onset','free_water','auto_water','task_protocol']:
    print(col, collections.Counter(dec(tr[col][:])).most_common(10))
print(tr['start_time'][:5], tr['stop_time'][:5])
for k in tr: print('T',k, dict(tr[k].attrs).get('description'))
print(u['is_good_trials'][0,:20], u['obs_intervals'][:3])
print(f['general/related_publications'][()], f['general/data_collection'][()])
EOF
python probe3.py sub-440956/sub-440956_ses-20190208T133600_behavior+ecephys+ogen.nwb 2>&1 | head -150
```

```
[('{"brain_regions": "left Striatum", "skull_reference": "Bregma", "ap_location": "0.00", "ml_location": "-2500.00", "depth": "-4300.00", "theta": "10.00", "phi": "180.00", "beta": "120.00"}', 384), ('{"brain_regions": "right Striatum", "skull_reference": "Bregma", "ap_location": "0.00", "ml_location": "2500.00", "depth": "-4000.00", "theta": "10.00", "phi": "0.00", "beta": "60.00"}', 384), ('{"brain_regions": "left ALM", "skull_reference": "Bregma", "ap_location": "2500.00", "ml_location": "-1500.00", "depth": "-2700.00", "theta": "15.00", "phi": "135.00", "beta": "-135.00"}', 281), ('{"brain_regions": "right ALM", "skull_reference": "Bregma", "ap_location": "2500.00", "ml_location": "1500.00", "depth": "-2700.00", "theta": "15.00", "phi": "45.00", "beta": "-45.00"}', 281)]
['18005110031 1-281', '18005110031 1-281', '18005110031 1-281'] [6300. 6300. 6300.] [4220. 4220. 4200.] [3240. 3240. 3240.] [16. 48.  0.]
electrode electrode index, starts at 0
filtering description of hardware filtering, including the filter name and frequency cutoffs
group a reference to the ElectrodeGroup this electrode is a part of
group_name the name of the ElectrodeGroup this electrode is a part of
id None
imp the impedance of the electrode, in ohms
location the location of channel within the subject e.g. brain region
rel_x the x coordinate within the electrode group
rel_y the y coordinate within the electrode group
rel_z the z coordinate within the electrode group
shank shank index, starts at 0, advance left to right
shank_col column index, starts at 0, advance left to right
shank_row row index, starts at 0, advance tip to tail
x the x coordinate of the position (+x is posterior)
y the y coordinate of the position (+y is inferior)
z the z coordinate of the position (+z is right)
U amplitude_cutoff Estimate of miss rate based on amplitude histogram
U anno_name brain region annotation of the classified unit
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey.py <<'EOF'
import time, h5py, remfile, sys, json, numpy as np, collections
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
ds=DandiAPIClient().get_dandiset("000363","0.231012.2129")
assets=[(a.path,a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]
if len(sys.argv)>1: assets=assets[:int(sys.argv[1])]
dec=lambda x:[v.decode() if isinstance(v,bytes) else v for v in x]
def one(pa):
    p,url=pa
    t=time.time()
    try:
        f=h5py.File(remfile.File(url),"r")
        e=f['general/extracellular_ephys/electrodes']
        loc=dec(e['location'][:])
        u=f['units']
        el=u['electrodes'][:]; idx=u['electrodes_index'][:]
        first=np.r_[0,idx[:-1]]
        tgt=[json.loads(loc[el[i]])['brain_regions'] for i in first]
        out=dict(path=p, target=tgt, cls=dec(u['classification'][:]), q=dec(u['unit_quality'][:]), anno=dec(u['anno_name'][:]),
                 ntr=int(f['intervals/trials/start_time'].shape[0]),
                 beh=list(f['acquisition/BehavioralTimeSeries']) if 'BehavioralTimeSeries' in f['acquisition'] else [],
                 t=time.time()-t)
        return out
    except Exception as ex:
        return dict(path=p, err=repr(ex), t=time.time()-t)
t0=time.time()
with ThreadPoolExecutor(8) as ex: res=list(ex.map(one,assets))
json.dump(res,open('survey.json','w'))
print(len(res), 'errors', sum('err' in r for r in res), 'time', time.time()-t0, 'max per file', max(r['t'] for r in res))
EOF
python survey.py 12
```

```
12 errors 0 time 17.980594873428345 max per file 16.169606685638428
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python survey.py && python - <<'EOF'
import json, collections
res=json.load(open('survey.json'))
print([r for r in res if 'err' in r][:3])
tg=collections.Counter(); an=collections.Counter()
for r in res:
    if 'err' in r: continue
    tg.update(set(r['target']))
    an.update(a for a in r['anno'] if a)
print(tg.most_common())
print([ (a,n) for a,n in an.most_common() if 'eticular' in a or 'Medulla' in a.lower()])
print(collections.Counter(tuple(r['beh']) for r in res if 'beh' in r))
EOF
```

```
Exit code 1
174 errors 0 time 267.1854639053345 max per file 19.97773575782776
[]
[('left ALM', 108), ('right ALM', 103), ('right Midbrain', 68), ('left Midbrain', 68), ('right Striatum', 57), ('left Striatum', 54), ('left Thalamus', 45), ('right Thalamus', 36), ('right Medulla', 24), ('left Medulla', 23), ('left ECT', 18), ('right ECT', 14), ('left BLA', 9), ('right BLA', 8)]
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
TypeError: argument of type 'float' is not iterable
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json, collections, math
res=json.load(open('survey.json'))
an=collections.Counter()
for r in res:
    an.update(str(a) for a in r['anno'])
print([ (a,n) for a,n in an.most_common() if 'eticular' in a or 'edulla' in a or a in ('nan','')])
print([ (a,n) for a,n in an.most_common() if 'econdary motor' in a])
print(collections.Counter(tuple(r['beh']) for r in res))
# per session: good-classified MOs in left/right ALM probe; medullary good units
RN=lambda a: any(k in a for k in ['Intermediate reticular','Gigantocellular reticular','Parvicellular reticular'])
rows=[]
for r in res:
    d=collections.Counter()
    for tg,c,q,a in zip(r['target'],r['cls'],r['q'],r['anno']):
        a=str(a)
        if 'ALM' in tg and 'Secondary motor' in a and c=='good': d[tg.split()[0]+'ALM_good']+=1
        if 'ALM' in tg: d[tg.split()[0]+'ALM_all']+=1
        if 'ALM' in tg and q=='good': d[tg.split()[0]+'ALM_q']+=1
        if RN(a) and c=='good': d['RN_good']+=1
        if 'Medulla' in tg: d['Med_all']+=1
        if 'Medulla' in tg and q=='good': d['Med_q']+=1
    rows.append((r['path'].split('/')[1][:30],dict(d),r['ntr']))
for x in rows:
    d=x[1]
    if (d.get('leftALM_good',0)>=30 and d.get('rightALM_good',0)>=30) or ((d.get('leftALM_good',0)>=30 or d.get('rightALM_good',0)>=30) and d.get('RN_good',0)>=30): print(x)
EOF
```

```
[('', 200922), ('Midbrain reticular nucleus', 2208), ('nan', 1852), ('Gigantocellular reticular nucleus', 704), ('Medulla', 332), ('Substantia nigra, reticular part', 332), ('Reticular nucleus of the thalamus', 301), ('Intermediate reticular nucleus', 279), ('Magnocellular reticular nucleus', 275), ('Pontine reticular nucleus', 259), ('Parvicellular reticular nucleus', 190), ('Paragigantocellular reticular nucleus, lateral part', 84), ('Midbrain reticular nucleus, retrorubral area', 68), ('Medullary reticular nucleus, ventral part', 52), ('Medullary reticular nucleus, dorsal part', 20), ('Lateral reticular nucleus, magnocellular part', 12), ('Tegmental reticular nucleus', 5)]
[('Secondary motor area, layer 5', 4311), ('Secondary motor area, layer 6a', 1504), ('Secondary motor area, layer 2/3', 1367), ('Secondary motor area, layer 1', 150), ('Secondary motor area, layer 6b', 14)]
Counter({('Camera0_side_JawTracking', 'Camera0_side_NoseTracking', 'Camera0_side_TongueTracking'): 147, ('Camera0_side_JawTracking', 'Camera0_side_NoseTracking', 'Camera0_side_TongueTracking', 'Camera0_side_WhiskerTracking_whisker'): 20, ('Camera0_side_JawTracking', 'Camera0_side_LickPortTracking', 'Camera0_side_NoseTracking', 'Camera0_side_TongueTracking'): 4, ('Camera0_side_JawTracking', 'Camera0_side_NoseTracking', 'Camera0_side_TongueTracking', 'Camera3_side_JawTracking', 'Camera3_side_NoseTracking', 'Camera3_side_TongueTracking'): 3})
('sub-440956_ses-20190208T133600', {'leftALM_all': 534, 'leftALM_q': 264, 'leftALM_good': 50, 'rightALM_all': 397, 'rightALM_q': 239, 'rightALM_good': 33}, 480)
('sub-440956_ses-20190207T120657', {'leftALM_all': 674, 'leftALM_q': 411, 'leftALM_good': 51, 'rightALM_all': 409, 'rightALM_q': 257, 'rightALM_good': 40}, 368)
('sub-440958_ses-20190217T154414', {'leftALM_all': 379, 'leftALM_q': 214, 'leftALM_good': 31, 'rightALM_all': 381, 'rightALM_q': 251, 'rightALM_good': 48}, 590)
('sub-440957_ses-20190211T143614', {'leftALM_all': 602, 'leftALM_q': 402, 'left
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json, collections
res=json.load(open('survey.json'))
RNk=['Intermediate reticular','Gigantocellular reticular','Parvicellular reticular']
def cnt(r, unitsel, alm_needs_target=True):
    d=collections.Counter()
    for tg,c,q,a in zip(r['target'],r['cls'],r['q'],r['anno']):
        a=str(a)
        if not unitsel(c,q): continue
        side=tg.split()[0]
        if 'Secondary motor' in a and ('ALM' in tg or not alm_needs_target): d[side+'ALM']+=1
        if any(k in a for k in RNk): d['RN']+=1
        if any(k in a for k in RNk) and 'Medulla' in tg: d['RNmedprobe']+=1
    return d
for name,sel in [('cls good',lambda c,q:c=='good'),('cls good & q good',lambda c,q:c=='good' and q=='good')]:
  for tgtreq in [True,False]:
    bil=[];am=[]
    for r in res:
        d=cnt(r,sel,tgtreq)
        if d['leftALM']>=30 and d['rightALM']>=30: bil.append((r['path'].split('/')[0],d['rightALM'],d['leftALM']))
        if d['RN']>=30 and (d['leftALM']>=30 or d['rightALM']>=30): am.append((r['path'].split('/')[0],d['leftALM']+d['rightALM'],d['RN'],d['leftALM'],d['rightALM']))
    print(name,'target req',tgtreq,'bilateral',len(bil),len(set(x[0] for x in bil)),'R',sum(x[1] for x in bil),'L',sum(x[2] for x in bil))
    print('   ALM+med',len(am),len(set(x[0] for x in am)),'ALM',sum(x[1] for x in am),'RN',sum(x[2] for x in am), am)
EOF
```

```
cls good target req True bilateral 17 9 R 858 L 1001
   ALM+med 5 4 ALM 300 RN 340 [('sub-456774', 85, 128, 85, 0), ('sub-460436', 81, 65, 0, 81), ('sub-460436', 48, 60, 0, 48), ('sub-484676', 46, 31, 0, 46), ('sub-484677', 40, 56, 0, 40)]
cls good target req False bilateral 17 9 R 858 L 1001
   ALM+med 5 4 ALM 300 RN 340 [('sub-456774', 85, 128, 85, 0), ('sub-460436', 81, 65, 0, 81), ('sub-460436', 48, 60, 0, 48), ('sub-484676', 46, 31, 0, 46), ('sub-484677', 40, 56, 0, 40)]
cls good & q good target req True bilateral 15 9 R 700 L 778
   ALM+med 4 3 ALM 227 RN 266 [('sub-456774', 68, 116, 68, 0), ('sub-460436', 74, 50, 0, 74), ('sub-460436', 47, 54, 0, 47), ('sub-484677', 38, 46, 0, 38)]
cls good & q good target req False bilateral 15 9 R 700 L 778
   ALM+med 4 3 ALM 227 RN 266 [('sub-456774', 68, 116, 68, 0), ('sub-460436', 74, 50, 0, 74), ('sub-460436', 47, 54, 0, 47), ('sub-484677', 38, 46, 0, 38)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sI http://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/ccf_2017/annotation_25.nrrd | head -5; curl -sI https://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/ccf_2017/annotation_25.nrrd | head -5; curl -s "http://api.brain-map.org/api/v2/structure_graph_download/1.json" | head -c 300
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && uv pip install -q pynrrd && cat > atlas.py <<'EOF'
import io, json, urllib.request, numpy as np, nrrd, h5py, remfile, collections, tempfile
from dandi.dandiapi import DandiAPIClient
raw=urllib.request.urlopen("https://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/ccf_2017/annotation_25.nrrd").read()
tf=tempfile.NamedTemporaryFile(suffix='.nrrd'); tf.write(raw); tf.flush()
ann,hdr=nrrd.read(tf.name); print(ann.shape, hdr.get('space directions'))
g=json.load(urllib.request.urlopen("http://api.brain-map.org/api/v2/structure_graph_download/1.json"))['msg'][0]
names={}
def w(n):
    names[n['id']]=n['name']; [w(c) for c in n['children']]
w(g)
ds=DandiAPIClient().get_dandiset("000363","0.231012.2129")
a=ds.get_asset_by_path("sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),"r")
e=f['general/extracellular_ephys/electrodes']; X=np.c_[e['x'][:],e['y'][:],e['z'][:]]
u=f['units']; el=u['electrodes'][:]; idx=u['electrodes_index'][:]; first=el[np.r_[0,idx[:-1]]]
dec=lambda x:[v.decode() if isinstance(v,bytes) else v for v in x]
an=dec(u['anno_name'][:]); cl=dec(u['classification'][:])
xyz=X[first]
vox=np.round(xyz/25).astype(int)
ok=(vox>=0).all(1)&(vox<np.array(ann.shape)).all(1)
lab=['out' if not o else names.get(int(ann[tuple(v)]),'?') for v,o in zip(vox,ok)]
m=[(a,l) for a,l,c in zip(an,lab,cl) if c=='good']
print('agree', np.mean([a==l for a,l in m]), len(m))
print(collections.Counter(m).most_common(15))
print(collections.Counter(l for l,c in zip(lab,cl) if c!='good').most_common(15))
print(X.min(0), X.max(0))
EOF
python atlas.py
```

```
(528, 320, 456) [[25.  0.  0.]
 [ 0. 25.  0.]
 [ 0.  0. 25.]]
agree 0.0 279
[(('Gigantocellular reticular nucleus', '?'), 65), (('Gigantocellular reticular nucleus', 'out'), 45), (('Magnocellular reticular nucleus', '?'), 36), (('Secondary motor area, layer 5', 'Field CA1'), 22), (('Secondary motor area, layer 5', 'Field CA3'), 19), (('Intermediate reticular nucleus', 'out'), 18), (('Paragigantocellular reticular nucleus, lateral part', 'out'), 16), (('Secondary motor area, layer 5', 'Field CA2'), 12), (('Secondary motor area, layer 5', 'lateral ventricle'), 11), (('Secondary motor area, layer 5', 'alveus'), 11), (('Magnocellular reticular nucleus', 'out'), 9), (('Secondary motor area, layer 6a', 'Field CA3'), 5), (('Secondary motor area, layer 5', 'corpus callosum, splenium'), 4), (('Frontal pole, layer 5', 'lateral ventricle'), 3), (('Medulla', 'out'), 2)]
[('out', 408), ('?', 298), ('Field CA3', 87), ('Field CA1', 58), ('lateral ventricle', 30), ('corpus callosum, splenium', 19), ('alveus', 12), ('Field CA2', 9), ('fimbria', 5)]
[nan nan nan] [nan nan nan]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json, collections
res=json.load(open('survey.json'))
RNk=['Intermediate reticular','Gigantocellular reticular','Parvicellular reticular']
for name,sel in [('probe target, unit_quality good',lambda c,q:q=='good'),('probe target, all units',lambda c,q:True),('probe target, cls good',lambda c,q:c=='good')]:
    bil=[];am=[]
    for r in res:
        d=collections.Counter()
        for tg,c,q,a in zip(r['target'],r['cls'],r['q'],r['anno']):
            if sel(c,q): d[tg]+=1
        if d['left ALM']>=30 and d['right ALM']>=30: bil.append((r['path'].split('/')[0],d['right ALM'],d['left ALM']))
        med=d['left Medulla']+d['right Medulla']
        if (d['left Medulla']>=30 or d['right Medulla']>=30) and (d['left ALM']>=30 or d['right ALM']>=30): am.append((r['path'].split('/')[0],d['left ALM']+d['right ALM'],med))
    print(name,'bil',len(bil),len(set(x[0] for x in bil)),sum(x[1] for x in bil),sum(x[2] for x in bil),'| ALM+med',len(am),len(set(x[0] for x in am)),sum(x[1] for x in am),sum(x[2] for x in am))
# sessions with both ALM and medulla probes at all
both=[r['path'] for r in res if any('Medulla' in t for t in r['target']) and any('ALM' in t for t in r['target'])]
print('sessions with ALM and Medulla probes', len(both), len(set(p.split('/')[0] for p in both)))
bothALM=[r['path'] for r in res if 'left ALM' in r['target'] and 'right ALM' in r['target']]
print('sessions with both ALM probes', len(bothALM), len(set(p.split('/')[0] for p in bothALM)))
EOF
```

```
probe target, unit_quality good bil 60 18 16024 16322 | ALM+med 36 8 10235 12554
probe target, all units bil 60 18 27679 28178 | ALM+med 36 8 17877 25592
probe target, cls good bil 52 16 6933 7618 | ALM+med 34 8 5031 4688
sessions with ALM and Medulla probes 36 8
sessions with both ALM probes 60 18
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > beh.py <<'EOF'
import h5py, remfile, numpy as np, time
from dandi.dandiapi import DandiAPIClient
t=time.time()
ds=DandiAPIClient().get_dandiset("000363","0.231012.2129")
a=ds.get_asset_by_path("sub-460436/sub-460436_ses-20200109T111437_behavior+ecephys+image+ogen.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),"r")
j=f['acquisition/BehavioralTimeSeries/Camera0_side_JawTracking']
ts=j['timestamps'][:]; d=j['data'][:]
print('load',time.time()-t, ts.shape)
dt=np.diff(ts); print('dt pct', np.percentile(dt,[1,50,99]), (dt>0.1).sum(), (dt<0).sum())
print('data range', np.nanmin(d,0), np.nanmax(d,0), np.isnan(d).mean(0))
tr=f['intervals/trials']; st=tr['start_time'][:]; sp=tr['stop_time'][:]
go=f['acquisition/BehavioralEvents/go_start_times/timestamps'][:]
print(len(st),len(go), np.all((go>=st)&(go<=sp)), np.percentile(go-st,[0,50,100]))
print('ts range', ts[0], ts[-1], st[0], sp[-1])
gaps=np.where(dt>0.1)[0]; print('n segments', len(gaps)+1, 'seg start vs trial start', (ts[gaps[:5]+1]), st[1:6])
ss=f['acquisition/BehavioralEvents/sample_start_times/timestamps'][:]
print(len(ss))
print(time.time()-t)
EOF
python beh.py
```

```
load 2.050401449203491 (1009384,)
dt pct [0.0034 0.0034 0.0034] 516 0
data range [8.35368156e-01 6.17112637e-01 3.59849793e-07] [256.65223122 344.89587235   1.        ] [0. 0. 0.]
517 517 True [2.1291 3.1557 7.0681]
ts range 0.0 3777.4873010161923 0.0 3775.9881
n segments 517 seg start vs trial start [ 8.1427 15.1227 20.984  27.6383 34.3564] [ 8.1427 15.1227 20.984  27.6383 34.3564]
537
2.5381598472595215
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://raw.githubusercontent.com/economolab/subspaceID/d593949fef8a39fe0a6eb54a21fc05cbca7bae84/funcs.py | head -150; date -u
```

Result: the fetched text is not kept.

**Agent**

Clock is 02:15. Plan: one helper module (loading, rates, movement masks, subspaces, dimensionality, VE, decoding, selectivity) and one notebook. Writing the helper now.

**Agent calls Bash**

```bash
mkdir -p entries/hasnain-2025; cd $TMPDIR && source env/bin/activate && python -c "
import pymanopt, inspect
from pymanopt.optimizers import TrustRegions
print(inspect.signature(TrustRegions.__init__)); print(inspect.signature(TrustRegions.run))
import pymanopt.function as F; print([x for x in dir(F) if not x.startswith('_')])
"
```

```
(self, miniter=3, kappa=0.1, theta=1.0, rho_prime=0.1, use_rand=False, rho_regularization=1000.0, *args, **kwargs)
(self, problem, *, initial_point=None, mininner=1, maxinner=None, Delta_bar=None, Delta0=None) -> pymanopt.optimizers.optimizer.OptimizerResult
['autograd', 'jax', 'numpy', 'pytorch', 'tensorflow']
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/hasnain-2025/map_subspace.py",
 "content": "\"\"\"Loading and measures for the MAP recordings of dandiset 000363, as Hasnain, Han & Economo (2025)\nuse them for Figure 4 (bioRxiv doi:10.1101/2025.10.17.682917).\n\nEach NWB file holds one session: units with spike times, a quality label (`unit_quality`, good or\nmulti), a classification (`classification`, good or unlabelled) and a CCF annotation (`anno_name`,\nfilled only for units classified good); electrodes whose `location` JSON names the probe's target\n(\"left ALM\", \"right Medulla\"); a trial table; go cue times (`go_start_times`); and side-camera\nkeypoint tracking of the jaw and nose (about 294 Hz, one segment per trial). Files are streamed from\nthe archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from. \"Claims\" is the claims file `claims/hasnain-2025.yaml`, whose header\nitems M1 to M10 cite the paper; \"Methods\" is a passage of the paper's Methods.\n\n- Session and unit selection (M1, M2; Methods, \"Curation of Mesoscale Activity Map Dataset\"): units\n  classified 'good' whose CCF label is MOs on a probe described as targeting ALM, and units in IRN,\n  GRN or PARN; sessions with at least 30 such units in each region of interest.\n- Trials. \"X moving and X stationary contained data from all correct and error trials\" (Methods,\n  \"Subspace identification\"): outcome hit or miss. Ignore trials, photostimulation trials and\n  early-lick trials are left out: an assumption, as the paper's own task has no photostimulation and\n  the paper does not say how MAP's early-lick and photostimulation trials were treated.\n- Rates: 5 ms bins, causal Gaussian kernel of 20 ms s.d. (Methods, both sections). The kernel is\n  truncated at 4 s.d., a standard choice.\n- Z-scoring: baseline -2.1 to -1.85 s before the go cue (Methods, \"Subspace identification\"); mean and\n  s.d. over the baseline bins of all trials. A unit with zero baseline s.d. is scaled by its s.d. over\n  all bins (a standard choice, counted in the notebook). `zscore_mode=\"all\"` is example.m's z-score\n  over all bins and trials (claims, M3 variant).\n- Trial windows (claims, M3): W1 -2.15 to +1.5 s around the go cue, W2 -1.8 to +1.5 s.\n- Movement (claims, M4; Methods, \"Curation...\"): the mean of the jaw and nose speed, binned at 5 ms.\n  The threshold sits between the two modes of the session's histogram; here Otsu's threshold on\n  log10 speed, a standard automatic choice for the value separating two modes (the paper set it by\n  hand). Bouts are runs of at least 100 ms; bouts 50 ms or less apart are merged. B1: shorter\n  supra-threshold runs are stationary; B2: they are moving.\n- Subspaces (claims, M5; Methods; subspaceID orthogonal_subspaces.m at commit d593949): maximise the\n  Methods' objective on the Stiefel manifold with pymanopt's trust regions, each term normalised by\n  the sum of the top-d eigenvalues of its covariance, from a random start drawn from the claim's seed.\n- Dimensionality (claims, M5 and M9; Methods, \"Dimensionality of subspaces\"): eigenvalues above the\n  95th percentile of eigenvalues from data with each neuron's time bins shuffled. To fit the time\n  limit the shuffle uses `N_SHUFFLE` = 100 shuffles (the paper uses 1000) and every 4th 5 ms bin (20\n  ms apart, the kernel's s.d.); both are deviations, recorded in the attempt.\n- Variance explained (claims, M6): readings V1, V2, V3.\n- Decoding (claims, M8; Methods, \"Cross-region decoding\"): ridge, lambda 0.01, source projections at t\n  and the 8 preceding bins, 70/30 split of trials, R2 per bin over -1.8 to +1.5 s, averaged.\n- Selectivity (claims, M7; Methods, \"Identifying selective neurons\"): AUROC per epoch, 1000 label\n  shuffles, equal random samples of correct left and right trials.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport json\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.signal import lfilter\n\nDANDISET_ID = \"000363\"\nDANDISET_VERSION = \"0.231012.2129\"\n\nBIN = 0.005\nSIGMA = 0.020\nBASELINE = (-2.1, -1.85)\nWINDOWS = {\"W1\": (-2.15, 1.5), \"W2\": (-1.8, 1.5)}\nTASK_SPAN = (-1.8, 1.5)\nEPOCHS = {\"sample\": (-1.8, -1.2), \"early_delay\": (-1.2, -0.5), \"late_delay\": (-0.5, 0.0),\n          \"early_response\": (0.0, 0.5), \"late_response\": (0.5, 1.5)}\nMIN_UNITS = 30\nMEDULLA_NUCLEI = (\"Intermediate reticular nucleus\", \"Gigantocellular reticular nucleus\",\n                  \"Parvicellular reticular nucleus\")\nMIN_BOUT_BINS = 20      # 100 ms\nMERGE_GAP_BINS = 10     # 50 ms\nN_SHUFFLE = 100\nSHUFFLE_STEP = 4\nRIDGE_LAMBDA = 0.01\nN_LAGS = 9\nD_CAP = 20\n\n\ndef _dec(values):\n    return [v.decode() if isinstance(v, bytes) else v for v in values]\n\n\ndef asset_urls():\n    \"\"\"(path, S3 url) of every asset of the pinned version.\"\"\"\n    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)\n    return [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]\n\n\ndef open_file(url):\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef unit_table(url):\n    \"\"\"Per unit: probe target, classification, quality, CCF annotation, from the units table.\"\"\"\n    f = open_file(url)\n    loc = _dec(f[\"general/extracellular_ephys/electrodes/location\"][:])\n    u = f[\"units\"]\n    el = u[\"electrodes\"][:]\n    idx = u[\"electrodes_index\"][:]\n    first = el[np.r_[0, idx[:-1]]]\n    target = [json.loads(loc[i])[\"brain_regions\"] for i in first]\n    anno = [a if isinstance(a, str) else \"\" for a in _dec(u[\"anno_name\"][:])]\n    tr = f[\"intervals/trials\"]\n    return dict(target=target, classification=_dec(u[\"classification\"][:]),\n                quality=_dec(u[\"unit_quality\"][:]), anno=anno,\n                n_trials=int(tr[\"start_time\"].shape[0]),\n                subject=f[\"general/subject/subject_id\"][()].decode())\n\n\ndef survey(assets, threads=8):\n    with ThreadPoolExecutor(threads) as ex:\n        tables = list(ex.map(lambda pa: unit_table(pa[1]), assets))\n    return {p: t for (p, _), t in zip(assets, tables)}\n\n\ndef region_of(target, anno):\n    \"\"\"'left ALM', 'right ALM' or 'medulla' under the paper's CCF rule, else None.\"\"\"\n    if \"ALM\" in target and anno.startswith(\"Secondary motor area\"):\n        return target\n    if anno in MEDULLA_NUCLEI:\n        return \"medulla\"\n    return None\n\n\ndef select_sessions(tables, min_units=MIN_UNITS):\n    \"\"\"Sessions and units under M1 and M2 (U1): units classified good with a CCF region.\"\"\"\n    bilateral, alm_med = {}, {}\n    for path, t in tables.items():\n        regions = {}\n        for i, (tg, cl, an) in enumerate(zip(t[\"target\"], t[\"classification\"], t[\"anno\"])):\n            if cl != \"good\":\n                continue\n            r = region_of(tg, an)\n            if r:\n                regions.setdefault(r, []).append(i)\n        n = {r: len(v) for r, v in regions.items()}\n        if n.get(\"left ALM\", 0) >= min_units and n.get(\"right ALM\", 0) >= min_units:\n            bilateral[path] = {\"right ALM\": regions[\"right ALM\"], \"left ALM\": regions[\"left ALM\"]}\n        alm = [r for r in (\"left ALM\", \"right ALM\") if n.get(r, 0) >= min_units]\n        if n.get(\"medulla\", 0) >= min_units and alm:\n            alm_med[path] = {\"ALM\": sorted(sum((regions[r] for r in alm), [])),\n                             \"medulla\": regions[\"medulla\"], \"alm_sides\": alm}\n    return bilateral, alm_med\n\n\ndef load_session(url, unit_ids):\n    \"\"\"Spike times of the given units, the trial table, go cue times and jaw and nose tracking.\"\"\"\n    f = open_file(url)\n    u = f[\"units\"]\n    idx = u[\"spike_times_index\"][:]\n    st_all = u[\"spike_times\"]\n    spikes = {}\n    lo = min(unit_ids)\n    hi = max(unit_ids)\n    a0 = 0 if lo == 0 else int(idx[lo - 1])\n    block = st_all[a0:int(idx[hi])]\n    for i in unit_ids:\n        s0 = (0 if i == 0 else int(idx[i - 1])) - a0\n        spikes[i] = np.sort(block[s0:int(idx[i]) - a0])\n    tr = f[\"intervals/trials\"]\n    trials = {k: _dec(tr[k][:]) for k in (\"outcome\", \"trial_instruction\", \"early_lick\", \"photostim_duration\")}\n    trials[\"start_time\"] = tr[\"start_time\"][:]\n    trials[\"stop_time\"] = tr[\"stop_time\"][:]\n    go = f[\"acquisition/BehavioralEvents/go_start_times/timestamps\"][:]\n    bts = f[\"acquisition/BehavioralTimeSeries\"]\n    track = {}\n    for part in (\"Jaw\", \"Nose\"):\n        g = bts[f\"Camera0_side_{part}Tracking\"]\n        track[part] = (g[\"timestamps\"][:], g[\"data\"][:, :2])\n    return dict(spikes=spikes, trials=trials, go=go, track=track)\n\n\ndef go_times(sess):\n    \"\"\"Go cue time per trial: the go_start_time inside each trial's interval.\"\"\"\n    st, sp, go = sess[\"trials\"][\"start_time\"], sess[\"trials\"][\"stop_time\"], sess[\"go\"]\n    j = np.searchsorted(go, st)\n    out = np.full(len(st), np.nan)\n    ok = j < len(go)\n    jj = j[ok]\n    inside = (go[jj] >= st[ok]) & (go[jj] <= sp[ok])\n    out[np.where(ok)[0][inside]] = go[jj[inside]]\n    return out\n\n\ndef trial_mask(sess, correct_only=False):\n    t = sess[\"trials\"]\n    out = np.array(t[\"outcome\"])\n    ok = np.isin(out, [\"hit\"] if correct_only else [\"hit\", \"miss\"])\n    ok &= np.array(t[\"photostim_duration\"]) == \"N/A\"\n    ok &= np.array(t[\"early_lick\"]) == \"no early\"\n    ok &= np.isfinite(go_times(sess))\n    return ok\n\n\ndef causal_kernel():\n    lags = np.arange(0, int(4 * SIGMA / BIN) + 1)\n    k = np.exp(-0.5 * (lags * BIN / SIGMA) ** 2)\n    return k / k.sum()\n\n\ndef rates(spike_list, align, window):\n    \"\"\"Smoothed single-trial rates (Hz), array (trials, bins, units), bins of BIN from window[0].\"\"\"\n    k = causal_kernel()\n    pad = len(k)\n    nb = int(round((window[1] - window[0]) / BIN))\n    edges = align[:, None] + window[0] + BIN * np.arange(-pad, nb + 1)[None, :]\n    out = np.empty((len(align), nb, len(spike_list)), dtype=np.float32)\n    for j, s in enumerate(spike_list):\n        c = np.diff(np.searchsorted(s, edges.ravel()).reshape(edges.shape), axis=1) / BIN\n        out[:, :, j] = lfilter(k, [1.0], c, axis=1)[:, pad:]\n    return out\n\n\ndef speed_bins(sess, align, window):\n    \"\"\"Mean jaw and nose speed (pixels/s) per 5 ms bin; NaN where there is no tracking.\"\"\"\n    nb = int(round((window[1] - window[0]) / BIN))\n    per_part = []\n    for part in (\"Jaw\", \"Nose\"):\n        ts, xy = sess[\"track\"][part]\n        dt = np.diff(ts)\n        sp = np.hypot(*np.diff(xy, axis=0).T) / dt\n        sp[dt > 0.05] = np.nan\n        tmid = ts[1:]\n        res = np.full((len(align), nb), np.nan)\n        for i, a in enumerate(align):\n            lo, hi = np.searchsorted(tmid, [a + window[0], a + window[1]])\n            if hi <= lo:\n                continue\n            b = ((tmid[lo:hi] - a - window[0]) / BIN).astype(int)\n            v = sp[lo:hi]\n            good = np.isfinite(v) & (b >= 0) & (b < nb)\n            s = np.bincount(b[good], v[good], minlength=nb)\n            n = np.bincount(b[good], minlength=nb)\n            with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n                res[i] = np.where(n > 0, s / n, np.nan)\n        per_part.append(res)\n    return np.nanmean(np.stack(per_part), axis=0) if True else None\n\n\ndef otsu_threshold(values, nbins=200):\n    \"\"\"Otsu's threshold of a 1-d sample.\"\"\"\n    h, e = np.histogram(values, nbins)\n    c = 0.5 * (e[1:] + e[:-1])\n    w0 = np.cumsum(h)\n    w1 = w0[-1] - w0\n    m0 = np.cumsum(h * c) / np.maximum(w0, 1)\n    m1 = (np.sum(h * c) - np.cumsum(h * c)) / np.maximum(w1, 1)\n    between = w0 * w1 * (m0 - m1) ** 2\n    return c[np.argmax(between[:-1])]\n\n\ndef _runs(b):\n    \"\"\"Start and end (exclusive) of runs of True in a 1-d bool array.\"\"\"\n    d = np.diff(np.r_[0, b.astype(int), 0])\n    return np.where(d == 1)[0], np.where(d == -1)[0]\n\n\ndef movement_mask(speed, log_threshold, short_runs_move=False):\n    \"\"\"1 moving, 0 stationary, -1 no tracking; per trial and bin (claims, M4).\"\"\"\n    out = np.full(speed.shape, -1, dtype=np.int8)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        above = np.log10(speed) > log_threshold\n    for i in range(speed.shape[0]):\n        valid = np.isfinite(speed[i])\n        a = above[i] & valid\n        s, e = _runs(a)\n        long_ = (e - s) >= MIN_BOUT_BINS\n        mv = np.zeros(len(a), bool)\n        bs, be = s[long_], e[long_]\n        for k in range(len(bs)):\n            mv[bs[k]:be[k]] = True\n            if k + 1 < len(bs) and bs[k + 1] - be[k] <= MERGE_GAP_BINS:\n                mv[be[k]:bs[k + 1]] = True\n        if short_runs_move:\n            mv |= a\n        out[i] = np.where(valid, mv.astype(np.int8), -1)\n    return out\n\n\ndef zscore(r, window, mode=\"baseline\"):\n    \"\"\"Z-score each unit (claims, M3). Returns z and the number of units scaled by the fallback.\"\"\"\n    if mode == \"all\":\n        flat = r.reshape(-1, r.shape[2])\n        mu, sd = flat.mean(0), flat.std(0)\n        n_fallback = 0\n    else:\n        b0 = int(round((BASELINE[0] - window[0]) / BIN))\n        b1 = int(round((BASELINE[1] - window[0]) / BIN))\n        if b0 < 0:\n            raise ValueError(\"window does not hold the baseline\")\n        base = r[:, b0:b1].reshape(-1, r.shape[2])\n        mu, sd = base.mean(0), base.std(0)\n        allsd = r.reshape(-1, r.shape[2]).std(0)\n        bad = sd <= 1e-9\n        n_fallback = int(bad.sum())\n        sd = np.where(bad, allsd, sd)\n    sd = np.where(sd <= 1e-9, 1.0, sd)\n    return ((r - mu) / sd).astype(np.float32), n_fallback\n\n\ndef cov(x):\n    x = x - x.mean(0)\n    return (x.T @ x / (len(x) - 1)).astype(np.float64)\n\n\ndef eig_desc(c):\n    return np.sort(np.linalg.eigvalsh(c))[::-1]\n\n\ndef shuffle_dimension(x, rng, n_shuffle=N_SHUFFLE, step=SHUFFLE_STEP):\n    \"\"\"Eigenvalues above the 95th percentile of the time-shuffled null, counted (Methods).\"\"\"\n    x = np.asarray(x[::step], dtype=np.float32)\n    ev = eig_desc(cov(x))\n    null = np.empty((n_shuffle, x.shape[1]))\n    xs = x.copy()\n    for s in range(n_shuffle):\n        for j in range(x.shape[1]):\n            xs[:, j] = x[rng.permutation(len(x)), j]\n        null[s] = eig_desc(cov(xs))\n    thr = np.percentile(null, 95, axis=0)\n    return int(np.sum(ev > thr)), ev\n\n\ndef cap_dims(d_null, d_pot, n, mode):\n    \"\"\"D1: d_null + d_pot no larger than n; D2: each capped at 20 as well.\"\"\"\n    if mode == \"D2\":\n        d_null, d_pot = min(d_null, D_CAP), min(d_pot, D_CAP)\n    d_null, d_pot = max(d_null, 1), max(d_pot, 1)\n    while d_null + d_pot > n:\n        if d_null >= d_pot:\n            d_null -= 1\n        else:\n            d_pot -= 1\n    return d_null, d_pot\n\n\ndef orthogonal_subspaces(c_stat, c_mov, d_null, d_pot, rng):\n    \"\"\"Q_null, Q_pot maximising the Methods' objective (subspaceID, orthogonal_subspaces.m).\"\"\"\n    import pymanopt\n    from pymanopt.manifolds import Stiefel\n    from pymanopt.optimizers import TrustRegions\n\n    n = c_stat.shape[0]\n    norm_null = eig_desc(c_stat)[:d_null].sum()\n    norm_pot = eig_desc(c_mov)[:d_pot].sum()\n    a = c_mov / norm_pot\n    b = c_stat / norm_null\n    manifold = Stiefel(n, d_pot + d_null)\n\n    @pymanopt.function.numpy(manifold)\n    def cost(q):\n        qp, qn = q[:, :d_pot], q[:, d_pot:]\n        return -0.5 * np.trace(qp.T @ a @ qp) - 0.5 * np.trace(qn.T @ b @ qn)\n\n    @pymanopt.function.numpy(manifold)\n    def egrad(q):\n        return -np.hstack([a @ q[:, :d_pot], b @ q[:, d_pot:]])\n\n    @pymanopt.function.numpy(manifold)\n    def ehess(q, u):\n        return -np.hstack([a @ u[:, :d_pot], b @ u[:, d_pot:]])\n\n    q0, _ = np.linalg.qr(rng.standard_normal((n, d_pot + d_null)))\n    problem = pymanopt.Problem(manifold, cost, euclidean_gradient=egrad, euclidean_hessian=ehess)\n    q = TrustRegions(verbosity=0).run(problem, initial_point=q0).point\n    return q[:, d_pot:], q[:, :d_pot]\n\n\ndef variance_explained(q, c, d=None):\n    \"\"\"Tr(Q'CQ) / sum of the top-d eigenvalues of C (Methods); d defaults to Q's width.\"\"\"\n    d = q.shape[1] if d is None else d\n    return float(np.trace(q.T @ c @ q) / eig_desc(c)[:d].sum())\n\n\ndef participation_ratio(c):\n    ev = eig_desc(c)\n    return float(ev.sum() ** 2 / (ev ** 2).sum())\n\n\ndef lagged(p, lags=N_LAGS):\n    \"\"\"Predictors at bin t: p[t], p[t-1], ..., p[t-lags+1]; (trials, bins, dims*lags).\"\"\"\n    out = [np.roll(p, k, axis=1) for k in range(lags)]\n    return np.concatenate(out, axis=2)\n\n\ndef ridge_r2(src, tgt, train, test, bins, standardize, pooled):\n    \"\"\"R2 on the test trials at each bin (claims, M8). src, tgt: (trials, bins, dims).\"\"\"\n    xl = lagged(src)\n    r2 = np.empty(len(bins))\n    for k, t in enumerate(bins):\n        xtr, ytr = xl[train, t].astype(np.float64), tgt[train, t].astype(np.float64)\n        xte, yte = xl[test, t].astype(np.float64), tgt[test, t].astype(np.float64)\n        mx, my = xtr.mean(0), ytr.mean(0)\n        sx = xtr.std(0, ddof=1) if standardize else np.ones(xtr.shape[1])\n        sx = np.where(sx > 0, sx, 1.0)\n        z = (xtr - mx) / sx\n        w = np.linalg.solve(z.T @ z + RIDGE_LAMBDA * np.eye(z.shape[1]), z.T @ (ytr - my))\n        pred = ((xte - mx) / sx) @ w + my\n        res = ((yte - pred) ** 2).sum(0)\n        tot = ((yte - yte.mean(0)) ** 2).sum(0)\n        r2[k] = 1 - res.sum() / tot.sum() if pooled else np.mean(1 - res / tot)\n    return r2\n\n\ndef auroc(x_right, x_left):\n    \"\"\"P(right > left), ties 0.5.\"\"\"\n    allx = np.r_[x_right, x_left]\n    from scipy.stats import rankdata\n    r = rankdata(allx)\n    n1, n2 = len(x_right), len(x_left)\n    return (r[:n1].sum() - n1 * (n1 + 1) / 2) / (n1 * n2)\n\n\ndef selectivity_p(x, is_right, rng, n_shuffle=1000):\n    \"\"\"AUROC and the share of label shuffles at least as far from 0.5 (Methods).\"\"\"\n    from scipy.stats import rankdata\n    r = rankdata(x)\n    n1 = int(is_right.sum())\n    n2 = len(x) - n1\n    obs = (r[is_right].sum() - n1 * (n1 + 1) / 2) / (n1 * n2)\n    perms = np.array([rng.permutation(len(x)) for _ in range(n_shuffle)])\n    lab = is_right[perms]\n    sh = ((r[None, :] * lab).sum(1) - n1 * (n1 + 1) / 2) / (n1 * n2)\n    p = np.mean(np.abs(sh - 0.5) >= abs(obs - 0.5))\n    return obs, p\n"
}
```

```
File created successfully at: entries/hasnain-2025/map_subspace.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/hasnain-2025/map_subspace.py",
 "old_string": "    return np.nanmean(np.stack(per_part), axis=0) if True else None",
 "new_string": "    with np.errstate(invalid=\"ignore\"), warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\", RuntimeWarning)\n        return np.nanmean(np.stack(per_part), axis=0)"
}
```

```
The file entries/hasnain-2025/map_subspace.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/hasnain-2025/map_subspace.py",
 "old_string": "import json\nfrom concurrent",
 "new_string": "import json\nimport warnings\nfrom concurrent"
}
```

```
The file entries/hasnain-2025/map_subspace.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > proto.py <<'EOF'
import sys, time, json, resource, zlib, numpy as np
sys.path.insert(0,'entries/hasnain-2025')
import map_subspace as ms
t=time.time()
res=json.load(open('survey.json'))
tables={r['path']:dict(target=r['target'],classification=r['cls'],quality=r['q'],anno=[a if isinstance(a,str) else '' for a in r['anno']]) for r in res}
bil,am=ms.select_sessions(tables)
print(len(bil),len(am))
urls=dict(ms.asset_urls()); print('urls',time.time()-t)
path=sorted(am)[0]; sel=am[path]; print(path, {k:len(v) if isinstance(v,list) else v for k,v in sel.items()})
ids=sel['ALM']+sel['medulla']
sess=ms.load_session(urls[path], ids); print('load',time.time()-t)
mask=ms.trial_mask(sess); go=ms.go_times(sess)[mask]; print('trials',mask.sum(), len(mask))
W=ms.WINDOWS['W1']
sp=ms.speed_bins(sess, go, W); print('speed',time.time()-t, np.isnan(sp).mean())
lt=ms.otsu_threshold(np.log10(sp[np.isfinite(sp)&(sp>0)])); print('log thr',lt)
mv=ms.movement_mask(sp, lt); print('moving frac',(mv==1).mean(),(mv==0).mean(),(mv==-1).mean())
rng=np.random.default_rng(1)
for reg in ['ALM','medulla']:
    r=ms.rates([sess['spikes'][i] for i in sel[reg]], go, W)
    z,nf=ms.zscore(r,W); print(reg,'rates',r.shape,time.time()-t,'fallback',nf)
    X=z.reshape(-1,z.shape[2]); m=mv.ravel()
    Xs,Xm=X[m==0],X[m==1]
    t1=time.time(); dn,_=ms.shuffle_dimension(Xs,rng); dp,_=ms.shuffle_dimension(Xm,rng); print('dims',dn,dp,'shuffle time',time.time()-t1)
    dn,dp=ms.cap_dims(dn,dp,X.shape[1],'D1')
    Cs,Cm,C=ms.cov(Xs),ms.cov(Xm),ms.cov(X)
    t1=time.time(); qn,qp=ms.orthogonal_subspaces(Cs,Cm,dn,dp,rng); print('opt',time.time()-t1, dn,dp)
    print('V1',ms.variance_explained(qn,C),ms.variance_explained(qp,C),'V2',np.trace(qn.T@C@qn)/np.trace(C),np.trace(qp.T@C@qp)/np.trace(C),'V3',ms.variance_explained(qn,Cs),ms.variance_explained(qp,Cm))
print('mem MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3, 'total',time.time()-t)
EOF
python proto.py
```

```
17 5
urls 6.421784400939941
sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb {'ALM': 85, 'medulla': 128, 'alm_sides': 1}
load 14.21315622329712
trials 149 570
speed 14.301488399505615 0.0
log thr 2.171317314381781
moving frac 0.020235359014434125 0.9797646409855659 0.0
ALM rates (149, 730, 85) 14.725144147872925 fallback 0
dims 8 8 shuffle time 5.333131551742554
opt 0.16307592391967773 8 8
V1 0.8092486358390071 0.4938442695209242 V2 0.3128345606063103 0.19090740252326768 V3 0.8202425794819458 0.7643179925241796
medulla rates (149, 730, 128) 21.04049301147461 fallback 1
dims 4 4 shuffle time 12.3315110206604
opt 0.17398357391357422 4 4
V1 0.5554337429644473 0.54480708145969 V2 0.36990274302868814 0.3628256950645736 V3 0.5650135885100606 0.7442339379758879
mem MB 801.016 total 33.622647523880005
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > proto2.py <<'EOF'
import sys, json, numpy as np, collections
sys.path.insert(0,'entries/hasnain-2025')
import map_subspace as ms
urls=dict(ms.asset_urls())
path="sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb"
sess=ms.load_session(urls[path],[0])
t=sess['trials']
print(collections.Counter(zip(t['outcome'],t['photostim_duration'],t['early_lick'])).most_common(12))
mask=ms.trial_mask(sess); go=ms.go_times(sess)[mask]
sp=ms.speed_bins(sess,go,ms.WINDOWS['W1'])
l=np.log10(sp[np.isfinite(sp)&(sp>0)])
print('zeros',(sp==0).mean(), np.percentile(l,[1,5,25,50,75,95,99]))
h,e=np.histogram(l,40); 
for a,b in zip(h,e): print(round(b,2),a)
prof=np.nanmean(sp,0); tt=np.arange(sp.shape[1])*0.005-2.15
for k in range(0,730,40): print(round(tt[k],2), round(prof[k],1))
EOF
python proto2.py
```

```
[(('ignore', 'N/A', 'no early'), 295), (('hit', 'N/A', 'no early'), 123), (('ignore', '0.5000', 'no early'), 72), (('miss', 'N/A', 'no early'), 26), (('hit', '0.5000', 'no early'), 22), (('miss', '0.5000', 'no early'), 16), (('hit', 'N/A', 'early'), 11), (('ignore', 'N/A', 'early'), 3), (('hit', '0.5000', 'early'), 1), (('ignore', '0.5000', 'early'), 1)]
zeros 0.0 [1.69983469 1.87763137 2.0779889  2.19961614 2.31460288 2.47751549
 2.58817886]
0.78 1
0.86 0
0.94 0
1.02 1
1.09 3
1.17 13
1.25 19
1.33 29
1.4 79
1.48 155
1.56 307
1.64 645
1.71 1286
1.79 2531
1.87 4921
1.95 8468
2.02 13361
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > proto3.py <<'EOF'
import sys, json, numpy as np, h5py
sys.path.insert(0,'entries/hasnain-2025')
import map_subspace as ms
from scipy.ndimage import median_filter, gaussian_filter1d
urls=dict(ms.asset_urls())
path="sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb"
f=ms.open_file(urls[path])
sess=ms.load_session(urls[path],[0])
mask=ms.trial_mask(sess); go=ms.go_times(sess)[mask]
ll=np.sort(np.r_[f['acquisition/BehavioralEvents/left_lick_times/timestamps'][:],f['acquisition/BehavioralEvents/right_lick_times/timestamps'][:]])
first=np.array([ll[np.searchsorted(ll,g)]-g if np.searchsorted(ll,g)<len(ll) else np.nan for g in go])
print('first lick latency', np.nanpercentile(first,[10,50,90]))
tg=f['acquisition/BehavioralTimeSeries/Camera0_side_TongueTracking']; ts=tg['timestamps'][:]; lik=tg['data'][:,2]
tt=np.arange(-0.5,1.0,0.025)
prof=[]
for g in go:
    i=np.searchsorted(ts,g+tt); i=np.clip(i,0,len(ts)-1); prof.append(lik[i])
prof=np.mean(prof,0)
for a,b in zip(tt[::2],prof[::2]): print(round(a,3),round(b,2))
# tongue onset after go per trial
on=[]
for g in go:
    lo,hi=np.searchsorted(ts,[g,g+1]); k=np.where(lik[lo:hi]>0.9)[0]
    on.append(ts[lo+k[0]]-g if len(k) else np.nan)
print('tongue visible latency', np.nanpercentile(on,[10,50,90]))
for part in ['Jaw','Nose']:
    ts2,xy=sess['track'][part]
    seg=np.r_[0,np.where(np.diff(ts2)>0.05)[0]+1,len(ts2)]
    xs=np.empty_like(xy)
    for a,b in zip(seg[:-1],seg[1:]): xs[a:b]=gaussian_filter1d(xy[a:b],sigma=3,axis=0,mode='nearest')
    sp=np.hypot(*np.diff(xs,axis=0).T)/np.diff(ts2); sp[np.diff(ts2)>0.05]=np.nan
    l=np.log10(sp[np.isfinite(sp)&(sp>0)])
    h,e=np.histogram(l,30); print(part, list(zip(np.round(e[:-1],2),h)))
EOF
python proto3.py
```

```
first lick latency [0.19806 0.4239  0.74812]
-0.5 0.0
-0.45 0.0
-0.4 0.0
-0.35 0.0
-0.3 0.0
-0.25 0.0
-0.2 0.01
-0.15 0.0
-0.1 0.01
-0.05 0.01
0.0 0.01
0.05 0.01
0.1 0.11
0.15 0.24
0.2 0.36
0.25 0.34
0.3 0.36
0.35 0.39
0.4 0.38
[... 15 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/hasnain-2025/map_subspace.py",
 "old_string": "        ts, xy = sess[\"track\"][part]\n        dt = np.diff(ts)\n        sp = np.hypot(*np.diff(xy, axis=0).T) / dt",
 "new_string": "        ts, xy = sess[\"track\"][part]\n        dt = np.diff(ts)\n        seg = np.r_[0, np.where(dt > 0.05)[0] + 1, len(ts)]\n        xs = np.empty_like(xy)\n        for a, b in zip(seg[:-1], seg[1:]):\n            xs[a:b] = gaussian_filter1d(xy[a:b], TRACK_SMOOTH_FRAMES, axis=0, mode=\"nearest\")\n        sp = np.hypot(*np.diff(xs, axis=0).T) / dt"
}
```

```
The file entries/hasnain-2025/map_subspace.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/hasnain-2025/map_subspace.py",
 "old_string": "from scipy.signal import lfilter",
 "new_string": "from scipy.ndimage import gaussian_filter1d\nfrom scipy.signal import lfilter"
}
```

```
The file entries/hasnain-2025/map_subspace.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/hasnain-2025/map_subspace.py",
 "old_string": "D_CAP = 20\n",
 "new_string": "D_CAP = 20\nTRACK_SMOOTH_FRAMES = 3   # Gaussian s.d. in frames (about 10 ms) on keypoint positions\n"
}
```

```
The file entries/hasnain-2025/map_subspace.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/hasnain-2025/map_subspace.py",
 "old_string": "- Movement (claims, M4; Methods, \"Curation...\"): the mean of the jaw and nose speed, binned at 5 ms.",
 "new_string": "- Movement (claims, M4; Methods, \"Curation...\"): the mean of the jaw and nose speed, binned at 5 ms.\n  Keypoint positions are first smoothed with a Gaussian of 3 frames s.d. (about 10 ms), a standard\n  choice: unsmoothed, the frame-to-frame jitter of the tracking makes the speed histogram unimodal\n  around 150 pixels/s, and no threshold separates movement from rest."
}
```

```
The file entries/hasnain-2025/map_subspace.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python proto.py 2>&1 | grep -v Warning
```

```
17 5
urls 5.833104610443115
sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb {'ALM': 85, 'medulla': 128, 'alm_sides': 1}
load 13.303019046783447
trials 149 570
speed 13.395830631256104 0.0
log thr 1.3884583887191562
moving frac 0.3291256780362232 0.6708743219637768 0.0
ALM rates (149, 730, 85) 13.797994613647461 fallback 0
dims 11 8 shuffle time 5.051767349243164
opt 0.17989778518676758 11 8
V1 0.5780404731807918 0.7279702013337477 V2 0.2556174643880648 0.28141442318604776 V3 0.880900312067299 0.8662322304770523
medulla rates (149, 730, 128) 19.839282512664795 fallback 1
dims 12 6 shuffle time 10.312210083007812
opt 0.46590304374694824 12 6
V1 0.3413564746133161 0.7623641140697479 V2 0.2684127330352099 0.5412000526488023 V3 0.6951820382728473 0.8830335924422098
mem MB 801.412 total 30.702332735061646
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025 && cat >> map_subspace.py <<'EOF'


def fit_region(z, mv, rng, dim_mode="D1", dims=None):
    """Subspaces of one region (claims, M5). z: (trials, bins, units) z-scored rates; mv: movement
    mask (trials, bins). `dims` reuses (d_null, d_pot) from the shuffle; else they are estimated."""
    x = z.reshape(-1, z.shape[2])
    m = mv.ravel()
    xs, xm = x[m == 0], x[m == 1]
    if dims is None:
        dn_raw, _ = shuffle_dimension(xs, rng)
        dp_raw, _ = shuffle_dimension(xm, rng)
    else:
        dn_raw, dp_raw = dims
    dn, dp = cap_dims(dn_raw, dp_raw, x.shape[1], dim_mode)
    cs, cm, c = cov(xs), cov(xm), cov(x)
    qn, qp = orthogonal_subspaces(cs, cm, dn, dp, rng)
    return dict(d_raw=(dn_raw, dp_raw), d=(dn, dp), qn=qn, qp=qp, C=c, Cs=cs, Cm=cm,
                n_stat=len(xs), n_mov=len(xm))


def ve_readings(fit):
    """Null, potent and both, under V1, V2 and V3 (claims, M6)."""
    qn, qp, c = fit["qn"], fit["qp"], fit["C"]
    both = np.hstack([qn, qp])
    tot = np.trace(c)
    return {"V1": (variance_explained(qn, c), variance_explained(qp, c), variance_explained(both, c)),
            "V2": tuple(float(np.trace(q.T @ c @ q) / tot) for q in (qn, qp, both)),
            "V3": (variance_explained(qn, fit["Cs"]), variance_explained(qp, fit["Cm"]), np.nan)}
EOF
date -u
```

```
Sun Nov 22 02:19:35 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "# %% [markdown]\n# # Hasnain, Han & Economo (2025) on the MAP dataset, DANDI:000363\n#\n# Paper: Hasnain M. A., Han Y. & Economo M. N., \"Mapping neural subspace dynamics onto the structure\n# of the mouse descending motor system\", bioRxiv doi:10.1101/2025.10.17.682917 (preprint version 1).\n# The claims file `claims/hasnain-2025.yaml` was written from the preprint's full text (PMC12632980);\n# it fixes what is tested.\n#\n# Dataset: DANDI:000363 (Mesoscale Activity Map Dataset, Chen et al. 2024), version **0.231012.2129**,\n# streamed from the archive. The paper cites the dandiset without a version\n# (\"https://dandiarchive.org/dandiset/000363\"), so the most recent published version is pinned. The\n# earlier versions hold the same 174 sessions; the versions before 0.231012.2129 total 19 to 67 GB and\n# this one 65.7 TB, as it adds the raw recordings. The cell \"Version check\" compares the units of one\n# session between this version and 0.230822.0128.\n#\n# The paper reuses the MAP data for Figure 4 only. Its own recordings (Figures 1 to 3, Extended Data\n# Figures 2 and 3) are not public, so those eleven claims are blocked.\n#\n# | Claim | Tested here |\n# |---|---|\n# | own-recordings-cohort, fig1i-selectivity-proportions, fig2c-subspace-variance, fig2e-potent-only-units, fig2f-letn-preference-like-un, fig2gh-letn-span-subspaces, ed2f-false-negatives, fig3c-network-beats-linear, fig3d-letn-un-movement-encoding, ed3-letn-fast-switch, ed3a-cd-early-un-not-letn | Blocked: the paper's own recordings are not public |\n# | map-session-selection | Tested |\n# | fig4b-medulla-selectivity | Tested |\n# | fig4c-alm-null-potent-similar | Tested |\n# | fig4c-medulla-null-smaller | Tested |\n# | fig4d-alm-predicts-medulla-null | Tested |\n# | fig4d-decoding-asymmetry | Tested |\n# | fig4e-medulla-null-lower-dimension | Tested |\n# | fig4f-medulla-null-not-spanning-alm | Tested |\n#\n# The methods are those of the claims file (header items M1 to M10, which cite the paper) and, where\n# it lacks a detail, the paper's Methods; the helper `map_subspace.py` says where each parameter comes\n# from.\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"2\")\nimport collections\nimport resource\nimport time\nimport zlib\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport map_subspace as ms\n\nT0 = time.time()\nKEY = \"hasnain-2025\"\n\n\ndef seed(claim, k=0):\n    return zlib.crc32(f\"{KEY}/{claim}\".encode()) + k\n\n\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\n\n# %% [markdown]\n# ## Data check\n#\n# Every file's units table is read (probe target from the electrodes' `location`, `classification`,\n# `unit_quality`, `anno_name`), then the sessions are selected as in M1 and M2.\n\n# %% tags=[\"sanity\"]\nassets = ms.asset_urls()\ntables = ms.survey(assets)\nprint(\"files:\", len(tables), \" subjects:\", len({t[\"subject\"] for t in tables.values()}))\nn_units = sum(len(t[\"target\"]) for t in tables.values())\nprint(\"units:\", n_units)\ncls_q = collections.Counter((c, q) for t in tables.values() for c, q in zip(t[\"classification\"], t[\"quality\"]))\nprint(\"classification x unit_quality:\", dict(cls_q))\nanno_by_cls = collections.Counter((c, a != \"\") for t in tables.values() for c, a in zip(t[\"classification\"], t[\"anno\"]))\nprint(\"(classification, has CCF annotation):\", dict(anno_by_cls))\ntargets = collections.Counter(tg for t in tables.values() for tg in set(t[\"target\"]))\nprint(\"sessions per probe target:\", dict(targets))\nboth_alm = [p for p, t in tables.items() if {\"left ALM\", \"right ALM\"} <= set(t[\"target\"])]\nalm_medulla_probes = [p for p, t in tables.items()\n                      if any(\"ALM\" in x for x in t[\"target\"]) and any(\"Medulla\" in x for x in t[\"target\"])]\nprint(\"sessions with probes in both ALMs:\", len(both_alm), \"from\", len({p.split('/')[0] for p in both_alm}), \"mice\")\nprint(\"sessions with an ALM and a medulla probe:\", len(alm_medulla_probes), \"from\",\n      len({p.split('/')[0] for p in alm_medulla_probes}), \"mice\")\nanno_counts = collections.Counter(a for t in tables.values() for a in t[\"anno\"] if a)\nprint(\"units in the medullary nuclei of M2:\", {k: anno_counts[k] for k in ms.MEDULLA_NUCLEI})\nprint(\"units labelled MOs (any probe):\", sum(v for k, v in anno_counts.items() if k.startswith(\"Secondary motor area\")))\nmos_off_alm = sum(1 for t in tables.values() for tg, a in zip(t[\"target\"], t[\"anno\"])\n                  if a.startswith(\"Secondary motor area\") and \"ALM\" not in tg)\nprint(\"units labelled MOs on probes not targeting ALM:\", mos_off_alm)\n\n# %% [markdown]\n# ### Version check\n#\n# One session's units in the pinned version and in 0.230822.0128, the last version without the raw\n# recordings.\n\n# %% tags=[\"sanity\"]\nfrom dandi.dandiapi import DandiAPIClient\nprobe_path = \"sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb\"\nold = DandiAPIClient().get_dandiset(ms.DANDISET_ID, \"0.230822.0128\")\nold_paths = {a.path: a for a in old.get_assets()}\nprint(\"assets in 0.230822.0128:\", len(old_paths), \" same paths as pinned:\", len(set(old_paths) & set(tables)))\ncmp = {}\nfor label, url in [(\"0.231012.2129\", dict(assets)[probe_path]),\n                   (\"0.230822.0128\", old_paths[probe_path].get_content_url(follow_redirects=1, strip_query=True))]:\n    f = ms.open_file(url)\n    u = f[\"units\"]\n    cmp[label] = dict(units=u[\"id\"].shape[0], spikes=u[\"spike_times\"].shape[0],\n                      good=int(sum(np.array(ms._dec(u[\"classification\"][:])) == \"good\")),\n                      first_spikes=np.round(u[\"spike_times\"][:5], 6).tolist(),\n                      acquisition=sorted(f[\"acquisition\"].keys()))\nprint(pd.DataFrame(cmp).T)\n\n# %% [markdown]\n# ### Selection (M1, M2)\n#\n# Units classified 'good' (`classification`), with a CCF label of MOs on a probe described as\n# targeting ALM, or a label of IRN, GRN or PARN. `anno_name` is filled only for units classified good,\n# so no other reading of \"classified as 'good'\" can place units in the CCF.\n\n# %% tags=[\"sanity\"]\nbilateral, alm_med = ms.select_sessions(tables)\nrows = []\nfor p, s in bilateral.items():\n    rows.append(dict(kind=\"bilateral ALM\", session=p.split(\"/\")[1][:30], subject=p.split(\"/\")[0],\n                     right_ALM=len(s[\"right ALM\"]), left_ALM=len(s[\"left ALM\"])))\nfor p, s in alm_med.items():\n    rows.append(dict(kind=\"ALM and medulla\", session=p.split(\"/\")[1][:30], subject=p.split(\"/\")[0],\n                     ALM=len(s[\"ALM\"]), ALM_side=\"+\".join(s[\"alm_sides\"]), medulla=len(s[\"medulla\"])))\nsel_table = pd.DataFrame(rows)\nprint(sel_table.to_string())\n\n# %% [markdown]\n# ### Trials, movement and clocks\n#\n# For each selected session: the trials kept (hit or miss, no photostimulation, no early lick), the\n# go cue inside each trial, the jaw and nose speed and the movement threshold. Clock checks: the\n# tongue becomes visible to the side camera, and the first lick is logged, shortly after the go cue\n# (behaviour clock against trial table); and lick direction is decoded from the selected units' spike\n# counts in 200 ms windows around the go cue, against the same decoder with the trial labels shuffled\n# (spike clock against trial table).\n\n# %% tags=[\"sanity\"]\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score\n\nurls = dict(assets)\nW = ms.WINDOWS[\"W1\"]\nsessions = {}\ncheck_rows = []\nrng_check = np.random.default_rng(seed(\"map-session-selection\"))\nfor p in list(alm_med) + list(bilateral):\n    if p in sessions:\n        continue\n    regions = alm_med[p] if p in alm_med else bilateral[p]\n    ids = sorted(set(sum((v for k, v in regions.items() if k != \"alm_sides\"), [])))\n    s = ms.load_session(urls[p], ids)\n    gos = ms.go_times(s)\n    keep = ms.trial_mask(s)\n    go = gos[keep]\n    speed = ms.speed_bins(s, go, W)\n    finite = speed[np.isfinite(speed) & (speed > 0)]\n    log_thr = ms.otsu_threshold(np.log10(finite))\n    # tongue visibility and first lick\n    f = ms.open_file(urls[p])\n    tg = f[\"acquisition/BehavioralTimeSeries/Camera0_side_TongueTracking\"]\n    tts, tlik = tg[\"timestamps\"][:], tg[\"data\"][:, 2]\n    licks = np.sort(np.r_[f[\"acquisition/BehavioralEvents/left_lick_times/timestamps\"][:],\n                          f[\"acquisition/BehavioralEvents/right_lick_times/timestamps\"][:]])\n    hit = np.array(s[\"trials\"][\"outcome\"])[keep] == \"hit\"\n    tongue_lat, lick_lat, tongue_pre = [], [], []\n    for g in go[hit]:\n        lo, hi = np.searchsorted(tts, [g, g + 1.0])\n        k = np.where(tlik[lo:hi] > 0.9)[0]\n        tongue_lat.append(tts[lo + k[0]] - g if len(k) else np.nan)\n        lo2, hi2 = np.searchsorted(tts, [g - 0.5, g])\n        tongue_pre.append(np.mean(tlik[lo2:hi2] > 0.9) if hi2 > lo2 else np.nan)\n        j = np.searchsorted(licks, g)\n        lick_lat.append(licks[j] - g if j < len(licks) else np.nan)\n    # decoding lick direction from spike counts\n    right = np.array(s[\"trials\"][\"trial_instruction\"])[keep] == \"right\"\n    acc = {}\n    for w0 in (-2.0, -1.0, -0.4, 0.2, 0.8):\n        X = np.stack([np.diff(np.searchsorted(s[\"spikes\"][i], np.c_[go + w0, go + w0 + 0.2]), axis=1)[:, 0]\n                      for i in ids], axis=1)\n        clf = LogisticRegression(C=0.1, max_iter=2000)\n        acc[w0] = cross_val_score(clf, X, right, cv=5).mean()\n        acc[f\"{w0} shuffled\"] = cross_val_score(clf, X, rng_check.permutation(right), cv=5).mean()\n    sessions[p] = dict(sess=s, keep=keep, go=go, speed=speed, log_thr=log_thr, regions=regions)\n    check_rows.append(dict(session=p.split(\"/\")[1][:30], trials=len(keep), kept=int(keep.sum()),\n                           hits=int(hit.sum()), right=int(right.sum()),\n                           go_in_trial=int(np.isfinite(gos).sum()),\n                           speed_thr=round(10 ** log_thr, 1), moving_frac=None,\n                           tongue_lat_ms=round(1000 * np.nanmedian(tongue_lat)),\n                           tongue_pre_go=round(np.nanmean(tongue_pre), 3),\n                           lick_lat_ms=round(1000 * np.nanmedian(lick_lat)),\n                           **{f\"acc {k}\": round(v, 2) for k, v in acc.items()}))\n    del f\nchecks = pd.DataFrame(check_rows)\nprint(checks.to_string())\nprint(\"trials kept per session: %d to %d\" % (checks.kept.min(), checks.kept.max()))\nprint(\"median tongue latency over sessions: %d ms; first lick %d ms\" % (checks.tongue_lat_ms.median(), checks.lick_lat_ms.median()))\nprint(\"elapsed %.0f s\" % (time.time() - T0))\n\n# %% tags=[\"sanity\"]\nfig, ax = plt.subplots(1, 2, figsize=(10, 3.2))\ntax = W[0] + ms.BIN * np.arange(sessions[probe_path][\"speed\"].shape[1])\nspd_all = np.array([np.nanmean(v[\"speed\"], 0) for v in sessions.values()])\nax[0].plot(tax, spd_all.T, lw=0.6)\nax[0].axvline(0, color=\"k\", lw=0.5)\nax[0].set(xlabel=\"time from go cue (s)\", ylabel=\"jaw and nose speed (pixels/s)\", title=\"mean per session\")\nv = sessions[probe_path]\nax[1].hist(np.log10(v[\"speed\"][np.isfinite(v[\"speed\"]) & (v[\"speed\"] > 0)]), 100)\nax[1].axvline(v[\"log_thr\"], color=\"r\")\nax[1].set(xlabel=\"log10 speed\", title=\"one session, Otsu threshold in red\")\nplt.tight_layout()\nprint(\"mean speed range over sessions and bins: %.1f to %.1f pixels/s\" % (np.nanmin(spd_all), np.nanmax(spd_all)))\nprint(\"speed in\", probe_path.split('/')[1][:30], \"pre-go %.1f, 0 to 1 s after go %.1f pixels/s\" % (\n    np.nanmean(v[\"speed\"][:, (tax > -1) & (tax < 0)]), np.nanmean(v[\"speed\"][:, (tax > 0) & (tax < 1)])))\n\n# %% [markdown]\n# ## Claim map-session-selection\n#\n# > In the MAP dataset, the paper's selection gives 20 bilateral ALM sessions from 10 mice (961 right\n# > and 1055 left ALM units) and ALM and medulla sessions with 604 ALM units and 724 medullary\n# > reticular nucleus units.\n#\n# Criterion: session counts match S1 (16) or S2 (11) for ALM and medulla and 20 bilateral, and every\n# unit count within tolerance under one reading of M2. U1 (good units in the regions) is the main\n# reading. U2 (all units in those regions) cannot place units in the CCF, since only good units carry\n# a CCF label; its nearest form, all units on the region's probe, is shown.\n\n# %% tags=[\"claim:map-session-selection\"]\nbil = sel_table[sel_table.kind == \"bilateral ALM\"]\nam = sel_table[sel_table.kind == \"ALM and medulla\"]\nmeasured_sel = dict(bilateral_sessions=len(bil), bilateral_mice=bil.subject.nunique(),\n                    right_ALM=int(bil.right_ALM.sum()), left_ALM=int(bil.left_ALM.sum()),\n                    alm_med_sessions=len(am), alm_med_mice=am.subject.nunique(),\n                    ALM=int(am.ALM.sum()), medulla=int(am.medulla.sum()))\nexpected_sel = dict(bilateral_sessions=(20, 2), right_ALM=(961, 96.1), left_ALM=(1055, 105.5),\n                    ALM=(604, 60.4), medulla=(724, 72.4))\nfor k, (v, tol) in expected_sel.items():\n    print(f\"{k:20s} measured {measured_sel[k]:6d}  expected {v} +- {tol}  within: {abs(measured_sel[k] - v) <= tol}\")\nprint(\"bilateral mice\", measured_sel[\"bilateral_mice\"], \"(paper 10); ALM and medulla sessions\",\n      measured_sel[\"alm_med_sessions\"], \"from\", measured_sel[\"alm_med_mice\"], \"mice (paper S1 16, S2 11 from 7)\")\nprint(\"bilateral units\", measured_sel[\"right_ALM\"] + measured_sel[\"left_ALM\"], \"(Methods 2016, Results 1116)\")\n\n# U2-like variant: every unit on the probe, sessions as selected\nvar_rows = []\nfor p, s in list(bilateral.items()) + list(alm_med.items()):\n    t = tables[p]\n    tg = np.array(t[\"target\"])\n    q = np.array(t[\"quality\"])\n    row = dict(session=p.split(\"/\")[1][:30], kind=\"bilateral\" if p in bilateral else \"ALM and medulla\")\n    for side in (\"left ALM\", \"right ALM\", \"left Medulla\", \"right Medulla\"):\n        row[side + \" all\"] = int((tg == side).sum())\n        row[side + \" quality good\"] = int(((tg == side) & (q == \"good\")).sum())\n    var_rows.append(row)\nvar = pd.DataFrame(var_rows).groupby(\"kind\").sum(numeric_only=True)\nprint(var.T)\n\n# thresholds on the count of good units: sessions selected\nfor thr in (20, 25, 30):\n    b2, a2 = ms.select_sessions(tables, min_units=thr)\n    print(f\"at least {thr} good units: bilateral {len(b2)} sessions, ALM and medulla {len(a2)} sessions\")\n\n# %% [markdown]\n# ## Per-region subspaces, ALM and medulla sessions\n#\n# For each ALM and medulla session and region: z-scored rates, the movement mask, the dimensions\n# from the shuffle, and the subspaces. The main reading is W1, B1, D1 and the baseline z-score;\n# the readings W2, B2, D2 and the z-score of example.m are each run with the others held at the main\n# reading. The subspace generator uses the seed of fig4c-alm-null-potent-similar, the first claim\n# that uses it.\n\n# %%\nREADINGS = {\"main\": dict(W=\"W1\", B=\"B1\", D=\"D1\", Z=\"baseline\"),\n            \"W2\": dict(W=\"W2\", B=\"B1\", D=\"D1\", Z=\"baseline\"),\n            \"B2\": dict(W=\"W1\", B=\"B2\", D=\"D1\", Z=\"baseline\"),\n            \"D2\": dict(W=\"W1\", B=\"B1\", D=\"D2\", Z=\"baseline\"),\n            \"Zall\": dict(W=\"W1\", B=\"B1\", D=\"D1\", Z=\"all\")}\n\n\ndef prepare(p, region_ids, reading, keep_mask=None):\n    v = sessions[p]\n    s, go = v[\"sess\"], v[\"go\"]\n    win = ms.WINDOWS[reading[\"W\"]]\n    r = ms.rates([s[\"spikes\"][i] for i in region_ids], go, ms.WINDOWS[\"W1\"])\n    off = int(round((win[0] - ms.WINDOWS[\"W1\"][0]) / ms.BIN))\n    r = r[:, off:]\n    if reading[\"Z\"] == \"baseline\":\n        # the baseline lies before W2's start, so it is always taken from the W1 rates\n        rw1 = ms.rates([s[\"spikes\"][i] for i in region_ids], go, ms.WINDOWS[\"W1\"]) if off else r\n        b0 = int(round((ms.BASELINE[0] - ms.WINDOWS[\"W1\"][0]) / ms.BIN))\n        b1 = int(round((ms.BASELINE[1] - ms.WINDOWS[\"W1\"][0]) / ms.BIN))\n        base = rw1[:, b0:b1].reshape(-1, r.shape[2])\n        mu, sd = base.mean(0), base.std(0)\n        allsd = r.reshape(-1, r.shape[2]).std(0)\n        nfb = int((sd <= 1e-9).sum())\n        sd = np.where(sd <= 1e-9, np.where(allsd > 0, allsd, 1.0), sd)\n        z = ((r - mu) / sd).astype(np.float32)\n    else:\n        z, nfb = ms.zscore(r, win, mode=\"all\")\n    mv = ms.movement_mask(v[\"speed\"][:, off:], v[\"log_thr\"], short_runs_move=reading[\"B\"] == \"B2\")\n    return z, mv, nfb\n\n\nfits = {}        # (session, region, reading) -> fit\nfit_rows = []\nrng_sub = np.random.default_rng(seed(\"fig4c-alm-null-potent-similar\"))\nfor p, s in alm_med.items():\n    for reg in (\"ALM\", \"medulla\"):\n        dims_main = None\n        for rname, rd in READINGS.items():\n            z, mv, nfb = prepare(p, s[reg], rd)\n            dims = fits[(p, reg, \"main\")][\"d_raw\"] if rname == \"D2\" else None\n            fit = ms.fit_region(z, mv, rng_sub, dim_mode=rd[\"D\"], dims=dims)\n            fit[\"n_fallback\"] = nfb\n            fit[\"moving_frac\"] = float((mv == 1).sum() / (mv >= 0).sum())\n            if rname == \"main\":\n                fit[\"z\"] = z\n                fit[\"mv\"] = mv\n            fits[(p, reg, rname)] = fit\n            ve = ms.ve_readings(fit)\n            fit_rows.append(dict(session=p.split(\"/\")[1][:30], region=reg, reading=rname, units=z.shape[2],\n                                 d_null=fit[\"d\"][0], d_pot=fit[\"d\"][1], d_null_raw=fit[\"d_raw\"][0],\n                                 d_pot_raw=fit[\"d_raw\"][1], moving=round(fit[\"moving_frac\"], 3),\n                                 fallback=nfb,\n                                 **{f\"{k} {n}\": 100 * x for k, vv in ve.items() for n, x in zip((\"null\", \"pot\", \"both\"), vv)}))\n    print(p.split(\"/\")[1][:30], \"done, elapsed %.0f s\" % (time.time() - T0))\nfit_df = pd.DataFrame(fit_rows)\nprint(fit_df.round(1).to_string())\nprint(\"peak memory %.0f MB\" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))\n\n# %% [markdown]\n# ## Claim fig4b-medulla-selectivity\n#\n# > Medullary reticular nucleus units are selective for lick direction in each epoch, most in the\n# > response epoch (sample 7%, delay 21%, response 49% of 724 units).\n#\n# Correct trials only, equal random samples of right and left trials (the smaller count; M7), AUROC in\n# each of the five epochs, 1000 label shuffles. Readings E1 (a unit counts for an epoch if selective\n# in either sub-epoch) and E2 (each sub-epoch alone); Bonferroni (p < 0.01) and uncorrected (p < 0.05).\n# Firing rates are the smoothed 5 ms rates (not z-scored) averaged over the epoch's bins.\n\n# %% tags=[\"claim:fig4b-medulla-selectivity\"]\ndef selectivity(rng):\n    out = []\n    for p, s in alm_med.items():\n        v = sessions[p]\n        trials = v[\"sess\"][\"trials\"]\n        out_arr = np.array(trials[\"outcome\"])[v[\"keep\"]]\n        instr = np.array(trials[\"trial_instruction\"])[v[\"keep\"]]\n        r_idx = np.where((out_arr == \"hit\") & (instr == \"right\"))[0]\n        l_idx = np.where((out_arr == \"hit\") & (instr == \"left\"))[0]\n        n = min(len(r_idx), len(l_idx))\n        pick = np.r_[rng.choice(r_idx, n, replace=False), rng.choice(l_idx, n, replace=False)]\n        is_right = np.r_[np.ones(n, bool), np.zeros(n, bool)]\n        r = ms.rates([v[\"sess\"][\"spikes\"][i] for i in s[\"medulla\"]], v[\"go\"][pick], ms.WINDOWS[\"W1\"])\n        tax = ms.WINDOWS[\"W1\"][0] + ms.BIN * np.arange(r.shape[1])\n        for j in range(r.shape[2]):\n            row = dict(session=p.split(\"/\")[1][:30], unit=s[\"medulla\"][j], n_per_side=n)\n            for ep, (a, b) in ms.EPOCHS.items():\n                x = r[:, (tax >= a) & (tax < b), j].mean(1)\n                auc, pv = ms.selectivity_p(x, is_right, rng)\n                row[ep] = pv\n                row[ep + \"_auc\"] = auc\n            out.append(row)\n    return pd.DataFrame(out)\n\n\ndef summarize_sel(df, alpha):\n    sig = {ep: df[ep] < alpha for ep in ms.EPOCHS}\n    e1 = {\"sample\": sig[\"sample\"], \"delay\": sig[\"early_delay\"] | sig[\"late_delay\"],\n          \"response\": sig[\"early_response\"] | sig[\"late_response\"]}\n    res = {f\"E1 {k}\": 100 * v.mean() for k, v in e1.items()}\n    res.update({f\"E2 {k}\": 100 * v.mean() for k, v in sig.items()})\n    return res\n\n\nsel_runs = {}\nfor k in SEED_OFFSETS:\n    sel_runs[k] = selectivity(np.random.default_rng(seed(\"fig4b-medulla-selectivity\", k)))\nsel_main = sel_runs[0]\nprint(\"medulla units:\", len(sel_main), \" trials per side per session:\", sel_main.groupby(\"session\").n_per_side.first().to_dict())\ntab = pd.DataFrame({(off, a): summarize_sel(df, a) for off, df in sel_runs.items() for a in (0.01, 0.05)}).T\ntab.index.names = [\"seed offset\", \"alpha\"]\nprint(tab.round(1).to_string())\nprint(\"expected: sample 7 +- 0.7, delay 21 +- 2.1, response 49 +- 4.9\")\nby_sess = sel_main.groupby(\"session\").apply(lambda d: pd.Series(summarize_sel(d, 0.01)))\nprint(\"by session (main seed, Bonferroni):\")\nprint(by_sess.round(1).to_string())\n# the false-positive rate of the test, with labels shuffled before the test\nrng_null = np.random.default_rng(seed(\"fig4b-medulla-selectivity\", 1))\n\n# %% [markdown]\n# ## Claims fig4c-alm-null-potent-similar and fig4c-medulla-null-smaller\n#\n# Variance explained per session (M6) under V1, V2 and V3, for each reading of M3 to M5; paired\n# two-sided t test of null against potent over the ALM and medulla sessions.\n\n# %% tags=[\"claim:fig4c-alm-null-potent-similar\", \"claim:fig4c-medulla-null-smaller\"]\nve_rows = []\nfor (rname, reg), d in fit_df.groupby([\"reading\", \"region\"]):\n    for V in (\"V1\", \"V2\", \"V3\"):\n        a, b = d[f\"{V} null\"].values, d[f\"{V} pot\"].values\n        t, pv = stats.ttest_rel(a, b)\n        ve_rows.append(dict(region=reg, reading=rname, V=V, n=len(a), null_mean=a.mean(), null_sd=a.std(ddof=1),\n                            pot_mean=b.mean(), pot_sd=b.std(ddof=1), diff=(a - b).mean(), t=t, p=pv,\n                            both=d[f\"{V} both\"].mean()))\nve_tab = pd.DataFrame(ve_rows).sort_values([\"region\", \"reading\", \"V\"])\nprint(ve_tab.round(3).to_string())\nprint(\"expected ALM null 36.0 +- 7.4, potent 37.1 +- 8.7 (p = 0.15); medulla null 26.4 +- 3.9, potent 44.8 +- 7.12 (p = 1.9e-9)\")\nalm_ok = ve_tab[(ve_tab.region == \"ALM\") & (abs(ve_tab.null_mean - 36.0) <= 7.4) & (abs(ve_tab.pot_mean - 37.1) <= 8.7)]\nmed_ok = ve_tab[(ve_tab.region == \"medulla\") & (abs(ve_tab.null_mean - 26.4) <= 3.9) & (abs(ve_tab.pot_mean - 44.8) <= 7.12)]\nprint(\"ALM readings with both means in tolerance:\")\nprint(alm_ok[[\"reading\", \"V\", \"null_mean\", \"pot_mean\", \"p\"]].round(4).to_string())\nprint(\"medulla readings with both means in tolerance:\")\nprint(med_ok[[\"reading\", \"V\", \"null_mean\", \"pot_mean\", \"p\"]].round(4).to_string())\nprint(\"per session, main reading:\")\nprint(fit_df[fit_df.reading == \"main\"][[\"session\", \"region\", \"units\", \"d_null\", \"d_pot\", \"moving\",\n                                         \"V1 null\", \"V1 pot\", \"V2 null\", \"V2 pot\", \"V3 null\", \"V3 pot\"]].round(1).to_string())\n\n# %% [markdown]\n# Seed check for fig4c and fig4e: the main reading again under the claim's seed plus 1000 to 4000\n# (dimension shuffles and the optimizer's start).\n\n# %% tags=[\"claim:fig4c-alm-null-potent-similar\", \"claim:fig4c-medulla-null-smaller\"]\nseed_rows = []\nfor k in SEED_OFFSETS[1:]:\n    rng_k = np.random.default_rng(seed(\"fig4c-alm-null-potent-similar\", k))\n    for p, s in alm_med.items():\n        for reg in (\"ALM\", \"medulla\"):\n            f0 = fits[(p, reg, \"main\")]\n            fit = ms.fit_region(f0[\"z\"], f0[\"mv\"], rng_k)\n            ve = ms.ve_readings(fit)\n            seed_rows.append(dict(offset=k, session=p, region=reg, d_null=fit[\"d\"][0], d_pot=fit[\"d\"][1],\n                                  **{f\"{V} {n}\": 100 * x for V, vv in ve.items() for n, x in zip((\"null\", \"pot\", \"both\"), vv)}))\nfor p, s in alm_med.items():\n    for reg in (\"ALM\", \"medulla\"):\n        fit = fits[(p, reg, \"main\")]\n        ve = ms.ve_readings(fit)\n        seed_rows.append(dict(offset=0, session=p, region=reg, d_null=fit[\"d\"][0], d_pot=fit[\"d\"][1],\n                              **{f\"{V} {n}\": 100 * x for V, vv in ve.items() for n, x in zip((\"null\", \"pot\", \"both\"), vv)}))\nseed_df = pd.DataFrame(seed_rows)\nsrows = []\nfor (off, reg), d in seed_df.groupby([\"offset\", \"region\"]):\n    for V in (\"V1\", \"V2\", \"V3\"):\n        t, pv = stats.ttest_rel(d[f\"{V} null\"], d[f\"{V} pot\"])\n        srows.append(dict(offset=off, region=reg, V=V, null=d[f\"{V} null\"].mean(), pot=d[f\"{V} pot\"].mean(), p=pv,\n                          mean_d_null=d.d_null.mean()))\nprint(pd.DataFrame(srows).round(4).to_string())\nprint(\"elapsed %.0f s\" % (time.time() - T0))\n\n# %% [markdown]\n# ## Claim fig4e-medulla-null-lower-dimension\n#\n# > The movement-null subspace has lower dimensionality in the medullary reticular nuclei than in ALM\n# > (paired t test, p = 7.4e-5).\n#\n# N1: the shuffle dimension of the stationary activity (before any cap); N2: the participation ratio\n# of the covariance of the movement-null projections. Paired two-sided t test over the ALM and\n# medulla sessions.\n\n# %% tags=[\"claim:fig4e-medulla-null-lower-dimension\"]\ndim_rows = []\nfor p, s in alm_med.items():\n    row = dict(session=p.split(\"/\")[1][:30])\n    for reg in (\"ALM\", \"medulla\"):\n        fit = fits[(p, reg, \"main\")]\n        row[f\"{reg} units\"] = len(s[reg])\n        row[f\"{reg} N1\"] = fit[\"d_raw\"][0]\n        row[f\"{reg} N2\"] = ms.participation_ratio(fit[\"qn\"].T @ fit[\"C\"] @ fit[\"qn\"])\n        row[f\"{reg} N2 per unit\"] = row[f\"{reg} N2\"] / len(s[reg])\n    dim_rows.append(row)\ndim_df = pd.DataFrame(dim_rows)\nprint(dim_df.round(2).to_string())\nfor m in (\"N1\", \"N2\", \"N2 per unit\"):\n    t, pv = stats.ttest_rel(dim_df[f\"medulla {m}\"], dim_df[f\"ALM {m}\"])\n    print(f\"{m}: medulla mean {dim_df[f'medulla {m}'].mean():.2f}, ALM mean {dim_df[f'ALM {m}'].mean():.2f}, \"\n          f\"t = {t:.2f}, p = {pv:.3g}, medulla lower in {(dim_df[f'medulla {m}'] < dim_df[f'ALM {m}']).sum()} of {len(dim_df)}\")\nfor off, d in seed_df.groupby(\"offset\"):\n    a = d[d.region == \"ALM\"].d_null.values\n    b = d[d.region == \"medulla\"].d_null.values\n    # N1 before the cap is not stored per seed; the capped d_null equals it unless the cap applied\n    t, pv = stats.ttest_rel(b, a)\n    print(f\"seed offset {off}: N1 (capped) medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {pv:.3g}\")\nfor rname in READINGS:\n    d = fit_df[fit_df.reading == rname]\n    a = d[d.region == \"ALM\"].d_null_raw.values\n    b = d[d.region == \"medulla\"].d_null_raw.values\n    t, pv = stats.ttest_rel(b, a)\n    print(f\"reading {rname}: N1 medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {pv:.3g}\")\n\n# %% [markdown]\n# ## Bilateral ALM sessions: subspaces for the decoding reference\n#\n# Main reading only (W1, B1, D1, baseline z-score); each hemisphere's subspaces from its own units.\n\n# %%\nfor p, s in bilateral.items():\n    for reg in (\"right ALM\", \"left ALM\"):\n        z, mv, nfb = prepare(p, s[reg], READINGS[\"main\"])\n        fit = ms.fit_region(z, mv, rng_sub)\n        fit[\"proj\"] = (z @ fit[\"qn\"]).astype(np.float32)\n        fit[\"n_fallback\"] = nfb\n        fits[(p, reg, \"main\")] = fit\n    print(p.split(\"/\")[1][:30], [fits[(p, r, \"main\")][\"d\"] for r in (\"right ALM\", \"left ALM\")],\n          \"elapsed %.0f s\" % (time.time() - T0))\nfor p, s in alm_med.items():\n    for reg in (\"ALM\", \"medulla\"):\n        f0 = fits[(p, reg, \"main\")]\n        f0[\"proj\"] = (f0[\"z\"] @ f0[\"qn\"]).astype(np.float32)\nprint(\"peak memory %.0f MB\" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))\n\n# %% [markdown]\n# ## Claims fig4d-alm-predicts-medulla-null and fig4d-decoding-asymmetry\n#\n# Ridge (lambda 0.01) from the source's movement-null projections at t and the 8 preceding bins to\n# all target movement-null dimensions at t; 70/30 split of trials; R2 per bin from -1.8 to +1.5 s,\n# averaged (M8). Readings: T1 all trials, T2 correct only; R1 pooled R2, R2 mean over dimensions;\n# predictors standardized or not; A1 mean of both ALM directions, A2 each direction.\n\n# %% tags=[\"claim:fig4d-alm-predicts-medulla-null\", \"claim:fig4d-decoding-asymmetry\"]\nbins = np.arange(int(round((ms.TASK_SPAN[0] - ms.WINDOWS[\"W1\"][0]) / ms.BIN)),\n                 int(round((ms.TASK_SPAN[1] - ms.WINDOWS[\"W1\"][0]) / ms.BIN)))\n\n\ndef decode(rng, readings):\n    rows = []\n    for kind, sess_map, pairs in ((\"ALM-medulla\", alm_med, [(\"ALM\", \"medulla\"), (\"medulla\", \"ALM\")]),\n                                  (\"ALM-ALM\", bilateral, [(\"right ALM\", \"left ALM\"), (\"left ALM\", \"right ALM\")])):\n        for p in sess_map:\n            v = sessions[p]\n            hit = np.array(v[\"sess\"][\"trials\"][\"outcome\"])[v[\"keep\"]] == \"hit\"\n            for T in (\"T1\", \"T2\"):\n                idx = np.arange(len(hit)) if T == \"T1\" else np.where(hit)[0]\n                perm = rng.permutation(idx)\n                ntr = int(round(0.7 * len(perm)))\n                train, test = perm[:ntr], perm[ntr:]\n                for src, tgt in pairs:\n                    xs, xt = fits[(p, src, \"main\")][\"proj\"], fits[(p, tgt, \"main\")][\"proj\"]\n                    for stdz, pooled in readings:\n                        r2 = ms.ridge_r2(xs, xt, train, test, bins, stdz, pooled)\n                        rows.append(dict(kind=kind, session=p, T=T, src=src, tgt=tgt,\n                                         std=stdz, R=\"R1\" if pooled else \"R2\", r2=100 * r2.mean(),\n                                         d_src=xs.shape[2], d_tgt=xt.shape[2], n_train=len(train)))\n    return pd.DataFrame(rows)\n\n\nALL_READ = [(s_, p_) for s_ in (False, True) for p_ in (True, False)]\ndec_main = decode(np.random.default_rng(seed(\"fig4d-alm-predicts-medulla-null\")), ALL_READ)\n\n\ndef dec_summary(df):\n    out = []\n    for (T, stdz, R), d in df.groupby([\"T\", \"std\", \"R\"]):\n        am_ = d[(d.kind == \"ALM-medulla\") & (d.src == \"ALM\")].set_index(\"session\").r2\n        ma_ = d[(d.kind == \"ALM-medulla\") & (d.src == \"medulla\")].set_index(\"session\").r2\n        aa = d[d.kind == \"ALM-ALM\"]\n        a1 = aa.groupby(\"session\").r2.mean()\n        rl = aa[aa.src == \"right ALM\"].r2\n        lr = aa[aa.src == \"left ALM\"].r2\n        sem = lambda x: x.std(ddof=1) / np.sqrt(len(x))\n        t, pv = stats.ttest_rel(am_.loc[ma_.index], ma_)\n        out.append(dict(T=T, std=stdz, R=R, ALM_to_med=am_.mean(), sem1=sem(am_), med_to_ALM=ma_.mean(),\n                        sem2=sem(ma_), p_asym=pv, ALM_ALM_A1=a1.mean(), sem3=sem(a1), R_to_L=rl.mean(),\n                        L_to_R=lr.mean()))\n    return pd.DataFrame(out)\n\n\ndsum = dec_summary(dec_main)\nprint(dsum.round(4).to_string())\nprint(\"expected ALM to medulla 40 +- 8.1, ALM to ALM 54 +- 7.0, medulla to ALM 21 +- 6.7 (p = 1.2e-4)\")\nprint(\"per session, T1, unstandardized, R1:\")\nprint(dec_main[(dec_main[\"T\"] == \"T1\") & (~dec_main[\"std\"]) & (dec_main.R == \"R1\")][\n    [\"kind\", \"session\", \"src\", \"tgt\", \"d_src\", \"d_tgt\", \"n_train\", \"r2\"]].round(1).to_string())\n\n# %% tags=[\"claim:fig4d-alm-predicts-medulla-null\", \"claim:fig4d-decoding-asymmetry\"]\nseed_dec = []\nfor k in SEED_OFFSETS:\n    d = decode(np.random.default_rng(seed(\"fig4d-alm-predicts-medulla-null\", k)), [(False, True), (True, True)]) if k else dec_main\n    s_ = dec_summary(d)\n    s_[\"offset\"] = k\n    seed_dec.append(s_[s_.R == \"R1\"])\nseed_dec = pd.concat(seed_dec)\nprint(seed_dec[[\"offset\", \"T\", \"std\", \"ALM_to_med\", \"med_to_ALM\", \"p_asym\", \"ALM_ALM_A1\"]].round(4).to_string())\nprint(\"elapsed %.0f s\" % (time.time() - T0))\n\n# %% [markdown]\n# ## Claim fig4f-medulla-null-not-spanning-alm\n#\n# > In a joint UMAP embedding of movement-null activity, medullary units do not span the set of\n# > movement-null activity patterns seen in ALM.\n#\n# M10: equal numbers of left and right correct trials, half to train and half to test; trial-averaged\n# movement-null reconstructions (X Q Q') of both trial types concatenated in time; z-scored per unit on\n# the training set; UMAP (2 components, 30 neighbours, min_dist 0.3, cosine), fitted on the training\n# data of ALM and medulla units together, test data transformed. The paper judges by inspection; the\n# numbers below describe the test embedding: for each unit, whether any of its 10 nearest neighbours\n# is from the other region, against the same count with the region labels shuffled (1000 times).\n\n# %% tags=[\"claim:fig4f-medulla-null-not-spanning-alm\"]\nimport umap\nfrom sklearn.neighbors import NearestNeighbors\n\n\ndef umap_run(rng, random_state):\n    train_rows, test_rows, region = [], [], []\n    for p, s in alm_med.items():\n        v = sessions[p]\n        trials = v[\"sess\"][\"trials\"]\n        out_arr = np.array(trials[\"outcome\"])[v[\"keep\"]]\n        instr = np.array(trials[\"trial_instruction\"])[v[\"keep\"]]\n        r_idx = rng.permutation(np.where((out_arr == \"hit\") & (instr == \"right\"))[0])\n        l_idx = rng.permutation(np.where((out_arr == \"hit\") & (instr == \"left\"))[0])\n        n = min(len(r_idx), len(l_idx))\n        r_idx, l_idx = r_idx[:n], l_idx[:n]\n        h = n // 2\n        for reg in (\"ALM\", \"medulla\"):\n            f0 = fits[(p, reg, \"main\")]\n            rec = f0[\"z\"] @ f0[\"qn\"] @ f0[\"qn\"].T\n            tr = np.concatenate([rec[r_idx[:h]].mean(0), rec[l_idx[:h]].mean(0)], axis=0)\n            te = np.concatenate([rec[r_idx[h:]].mean(0), rec[l_idx[h:]].mean(0)], axis=0)\n            mu, sd = tr.mean(0), tr.std(0)\n            sd = np.where(sd > 0, sd, 1.0)\n            train_rows.append(((tr - mu) / sd).T)\n            test_rows.append(((te - mu) / sd).T)\n            region += [reg] * tr.shape[1]\n    Xtr, Xte = np.vstack(train_rows), np.vstack(test_rows)\n    model = umap.UMAP(n_components=2, n_neighbors=30, min_dist=0.3, metric=\"cosine\", random_state=random_state)\n    model.fit(Xtr)\n    return model.transform(Xte), np.array(region)\n\n\ndef nn_stats(emb, region, rng, k=10, n_shuffle=1000):\n    nn = NearestNeighbors(n_neighbors=k + 1).fit(emb)\n    _, ind = nn.kneighbors(emb)\n    ind = ind[:, 1:]\n\n    def frac(lab):\n        other = lab[ind] != lab[:, None]\n        alm_alone = np.mean(~other[lab == \"ALM\"].any(1))\n        med_with_alm = np.mean(other[lab == \"medulla\"].any(1))\n        return alm_alone, med_with_alm\n\n    obs = frac(region)\n    null = np.array([frac(rng.permutation(region)) for _ in range(n_shuffle)])\n    return obs, null\n\n\numap_res = {}\nfor k in SEED_OFFSETS:\n    sd_ = seed(\"fig4f-medulla-null-not-spanning-alm\", k)\n    rng_u = np.random.default_rng(sd_)\n    emb, region = umap_run(rng_u, random_state=sd_ % (2 ** 31))\n    obs, null = nn_stats(emb, region, rng_u)\n    umap_res[k] = (emb, region, obs, null)\n    print(f\"seed offset {k}: ALM units with no medulla unit among 10 neighbours {100 * obs[0]:.1f}% \"\n          f\"(shuffled labels {100 * null[:, 0].mean():.1f}%, 95th pct {100 * np.percentile(null[:, 0], 95):.1f}%); \"\n          f\"medulla units with an ALM neighbour {100 * obs[1]:.1f}% (shuffled {100 * null[:, 1].mean():.1f}%)\")\nemb, region, obs, null = umap_res[0]\nfig, ax = plt.subplots(figsize=(5, 4.5))\nfor reg, c in ((\"ALM\", \"tab:blue\"), (\"medulla\", \"tab:orange\")):\n    ax.scatter(*emb[region == reg].T, s=6, c=c, label=f\"{reg} ({(region == reg).sum()})\", alpha=0.7)\nax.legend()\nax.set(title=\"Test-set UMAP of movement-null reconstructions\", xlabel=\"UMAP 1\", ylabel=\"UMAP 2\")\nprint(\"embedding range: x %.2f to %.2f, y %.2f to %.2f; all points shown\" % (emb[:, 0].min(), emb[:, 0].max(), emb[:, 1].min(), emb[:, 1].max()))\n# extent: the share of the ALM points' 2-d spread covered by medulla points\nfor reg in (\"ALM\", \"medulla\"):\n    e = emb[region == reg]\n    print(reg, \"5th to 95th percentile: x %.2f to %.2f, y %.2f to %.2f\" % (*np.percentile(e[:, 0], [5, 95]), *np.percentile(e[:, 1], [5, 95])))\ngrid = np.floor((emb - emb.min(0)) / ((emb.max(0) - emb.min(0)) / 10 + 1e-12)).astype(int)\ncells_alm = {tuple(g) for g, r in zip(grid, region) if r == \"ALM\"}\ncells_med = {tuple(g) for g, r in zip(grid, region) if r == \"medulla\"}\nprint(\"10 x 10 grid cells holding ALM units: %d, of which hold no medulla unit: %d; medulla cells outside ALM cells: %d of %d\"\n      % (len(cells_alm), len(cells_alm - cells_med), len(cells_med - cells_alm), len(cells_med)))\nprint(\"elapsed %.0f s, peak memory %.0f MB\" % (time.time() - T0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''# the false-positive rate of the test, with labels shuffled before the test
rng_null = np.random.default_rng(seed("fig4b-medulla-selectivity", 1))
''','')
s=s.replace("speed_thr=round(10 ** log_thr, 1), moving_frac=None,","speed_thr=round(10 ** log_thr, 1),")
open('nb_src.py','w').write(s)
d=s.replace("tables = ms.survey(assets)","import json\nres=json.load(open('/tmp/claude-1001/survey.json'))\ntables={r['path']:dict(target=r['target'],classification=r['cls'],quality=r['q'],anno=[a if isinstance(a,str) else '' for a in r['anno']],subject=r['path'].split('/')[0],n_trials=r['ntr']) for r in res}")
d=d.replace("bilateral, alm_med = ms.select_sessions(tables)\n","bilateral, alm_med = ms.select_sessions(tables)\nbilateral=dict(list(bilateral.items())[:2]); alm_med=dict(list(alm_med.items())[:3])\n",1)
d=d.replace("for k in SEED_OFFSETS[1:]:","for k in SEED_OFFSETS[1:2]:")
d=d.replace("for k in SEED_OFFSETS:\n    d = decode","for k in SEED_OFFSETS[:2]:\n    d = decode")
d=d.replace("for k in SEED_OFFSETS:\n    sd_ =","for k in SEED_OFFSETS[:2]:\n    sd_ =")
d=d.replace("for k in SEED_OFFSETS:\n    sel_runs","for k in SEED_OFFSETS[:2]:\n    sel_runs")
d=d.replace("plt.tight_layout()","plt.tight_layout(); plt.close('all')")
open('dev.py','w').write(d)
EOF
grep -n "probe_path\b" dev.py | head -3
```

```
103:probe_path = "sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb"
108:for label, url in [("0.231012.2129", dict(assets)[probe_path]),
109:                   ("0.230822.0128", old_paths[probe_path].get_content_url(follow_redirects=1, strip_query=True))]:
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025 && source $TMPDIR/env/bin/activate && date -u && MPLBACKEND=Agg PYTHONWARNINGS=ignore timeout 3000 python $TMPDIR/dev.py 2>&1 | tail -150; date -u
```

```
Sun Nov 22 02:22:00 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/dev.py", line 48, in <module>
    import map_subspace as ms
ModuleNotFoundError: No module named 'map_subspace'
Sun Nov 22 02:22:03 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && MPLBACKEND=Agg PYTHONWARNINGS=ignore PYTHONPATH=. timeout 3000 python $TMPDIR/dev.py 2>&1 | tail -150; date -u
```

```
files: 174  subjects: 28
units: 272227
classification x unit_quality: {('unlabelled', 'multi'): 108153, ('good', 'good'): 60978, ('unlabelled', 'good'): 92769, ('good', 'multi'): 8475, (nan, 'multi'): 651, (nan, 'good'): 1201}
(classification, has CCF annotation): {('unlabelled', False): 200922, ('good', True): 69453, (nan, False): 1852}
sessions per probe target: {'right Striatum': 57, 'left ALM': 108, 'left Striatum': 54, 'right ALM': 103, 'right Midbrain': 68, 'right Thalamus': 36, 'left Thalamus': 45, 'left Midbrain': 68, 'right Medulla': 24, 'left Medulla': 23, 'left ECT': 18, 'right ECT': 14, 'right BLA': 8, 'left BLA': 9}
sessions with probes in both ALMs: 60 from 18 mice
sessions with an ALM and a medulla probe: 36 from 8 mice
units in the medullary nuclei of M2: {'Intermediate reticular nucleus': 279, 'Gigantocellular reticular nucleus': 704, 'Parvicellular reticular nucleus': 190}
units labelled MOs (any probe): 7346
units labelled MOs on probes not targeting ALM: 0
assets in 0.230822.0128: 174  same paths as pinned: 103
Traceback (most recent call last):
  File "/tmp/claude-1001/dev.py", line 109, in <module>
    ("0.230822.0128", old_paths[probe_path].get_content_url(follow_redirects=1, strip_query=True))]:
                      ~~~~~~~~~^^^^^^^^^^^^
KeyError: 'sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb'
Sun Nov 22 02:22:14 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
for fn in ['nb_src.py','dev.py']:
    s=open(fn).read()
    s=s.replace('''old_paths = {a.path: a for a in old.get_assets()}
print("assets in 0.230822.0128:", len(old_paths), " same paths as pinned:", len(set(old_paths) & set(tables)))''','''old_paths = {a.path: a for a in old.get_assets()}
ses_key = lambda p: p.split("_behavior")[0]
old_by_ses = {ses_key(p): a for p, a in old_paths.items()}
print("assets in 0.230822.0128:", len(old_paths), " same paths as pinned:", len(set(old_paths) & set(tables)),
      " same sessions:", len(set(old_by_ses) & {ses_key(p) for p in tables}))
print("example path there:", next(p for p in old_paths if ses_key(p) == ses_key(probe_path)))''')
    s=s.replace('old_paths[probe_path].get_content_url','old_by_ses[ses_key(probe_path)].get_content_url')
    open(fn,'w').write(s)
EOF
cd entries/hasnain-2025 && source $TMPDIR/env/bin/activate && MPLBACKEND=Agg PYTHONWARNINGS=ignore PYTHONPATH=. timeout 3000 python $TMPDIR/dev.py 2>&1 | tail -150; date -u
```

```
13  sub-460436_ses-20200109T111437      ALM      D2     81       4      4           4          4     0.5         1     54.4    74.3     97.3     18.0    24.6     42.5     75.8    82.1      NaN
14  sub-460436_ses-20200109T111437      ALM    Zall     81      23     13          23         13     0.5         0     73.4    89.7     97.3     29.8    25.0     54.8     94.4    98.7      NaN
15  sub-460436_ses-20200109T111437  medulla    main     65       1      1           1          1     0.5         0     81.1    38.7     98.4     37.6    18.0     55.5     83.9    45.6      NaN
16  sub-460436_ses-20200109T111437  medulla      W2     65       1      1           1          1     0.5         0     92.4    28.2     99.0     43.1    13.1     56.2     94.0    35.4      NaN
17  sub-460436_ses-20200109T111437  medulla      B2     65       8      1           8          1     0.6         0     36.5    97.9     94.7     27.6    45.4     73.0     59.8    99.0      NaN
18  sub-460436_ses-20200109T111437  medulla      D2     65       1      1           1          1     0.5         0     81.1    38.7     98.4     37.6    18.0     55.5     83.9    45.6      NaN
19  sub-460436_ses-20200109T111437  medulla    Zall     65      12     12          12         12     0.5         0     62.8    72.0     98.5     30.7    35.2     65.9     88.1    85.7      NaN
20  sub-460436_ses-20200110T142717      ALM    main     48       8      5           8          5     0.5         0     30.1    92.6     98.8     18.6    51.1     69.7     51.6    94.9      NaN
21  sub-460436_ses-20200110T142717      ALM      W2     48       8      5           8          5     0.6         0     29.7    92.6     99.1     18.9    52.5     71.4     48.8    94.6      NaN
22  sub-460436_ses-20200110T142717      ALM      B2     48      10      6          10          6     0.7         0     29.7    93.0     97.7     19.5    53.7     73.1     67.8    94.2      NaN
23  sub-460436_ses-20200110T142717      ALM      D2     48       8    
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cat > $TMPDIR/dbg.py <<'EOF'
import numpy as np, json, map_subspace as ms
urls=dict(ms.asset_urls())
res=json.load(open('/tmp/claude-1001/survey.json'))
tables={r['path']:dict(target=r['target'],classification=r['cls'],quality=r['q'],anno=[a if isinstance(a,str) else '' for a in r['anno']]) for r in res}
bil,am=ms.select_sessions(tables)
p=list(bil)[0]; ids=bil[p]['right ALM']
s=ms.load_session(urls[p],ids); keep=ms.trial_mask(s); go=ms.go_times(s)[keep]
r=ms.rates([s['spikes'][i] for i in ids],go,ms.WINDOWS['W1'])
b=r[:,10:60].reshape(-1,r.shape[2]); sd=b.std(0); mu=b.mean(0)
print(np.sort(sd)[:10]); print(np.sort(mu)[:10])
z,nf=ms.zscore(r,ms.WINDOWS['W1']); print('z absmax per unit top', np.sort(np.abs(z).max((0,1)))[-10:])
# per-trial baseline mean sd across trials
bt=r[:,10:60].mean(1); print('sd of trial means', np.sort(bt.std(0))[:10])
fr=np.array([len(s['spikes'][i]) for i in ids])/ (s['trials']['stop_time'][-1]); print('rates', np.sort(fr)[:10])
EOF
python $TMPDIR/dbg.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dbg.py", line 1, in <module>
    import numpy as np, json, map_subspace as ms
ModuleNotFoundError: No module named 'map_subspace'
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cd entries/hasnain-2025 && PYTHONPATH=. python $TMPDIR/dbg.py
```

```
[0.         0.         0.5643209  0.56437206 0.7894492  0.7982724
 0.9743991  1.7083294  1.7190126  1.7330017 ]
[0.         0.         0.0118866  0.01197605 0.02212343 0.0239521
 0.03536327 0.10624571 0.10968948 0.114092  ]
z absmax per unit top [ 34.484642  40.577904  40.837967  41.75562   42.143406 129.65149
 133.7997   139.25488  177.71028  277.72467 ]
sd of trial means [0.         0.         0.21686138 0.2185418  0.2860107  0.30860186
 0.3659518  0.63020575 0.65348285 0.71066105]
rates [0.07009238 0.07494493 0.08357168 0.08438044 0.09597264 0.11106946
 0.13829765 0.15743826 0.18924942 0.18951901]
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cd entries/hasnain-2025 && cat > $TMPDIR/dbg2.py <<'EOF'
import numpy as np, json, map_subspace as ms
urls=dict(ms.asset_urls())
res=json.load(open('/tmp/claude-1001/survey.json'))
tables={r['path']:dict(target=r['target'],classification=r['cls'],quality=r['q'],anno=[a if isinstance(a,str) else '' for a in r['anno']]) for r in res}
bil,am=ms.select_sessions(tables)
p=list(bil)[0]; W=ms.WINDOWS['W1']
s=ms.load_session(urls[p],bil[p]['right ALM']+bil[p]['left ALM']); keep=ms.trial_mask(s); go=ms.go_times(s)[keep]
sp=ms.speed_bins(s,go,W); lt=ms.otsu_threshold(np.log10(sp[np.isfinite(sp)&(sp>0)])); mv=ms.movement_mask(sp,lt)
rng=np.random.default_rng(0); P={}
for reg in ['right ALM','left ALM']:
    z,_=ms.zscore(ms.rates([s['spikes'][i] for i in bil[p][reg]],go,W),W)
    fit=ms.fit_region(z,mv,rng); P[reg]=z@fit['qn']; print(reg, fit['d'], np.abs(P[reg]).max(), P[reg].std((0,1)))
bins=np.arange(70,730)
perm=rng.permutation(len(go)); tr,te=perm[:int(.7*len(go))],perm[int(.7*len(go)):]
r2=ms.ridge_r2(P['right ALM'],P['left ALM'],tr,te,bins,False,True)
print('mean',r2.mean(),'median',np.median(r2), np.percentile(r2,[1,5,25,75,95]))
xl=ms.lagged(P['right ALM']); print('lagged shape', xl.shape)
# without lags
for lam in [0.01,1,100,1e4]:
    ms.RIDGE_LAMBDA=lam
    r2=ms.ridge_r2(P['right ALM'],P['left ALM'],tr,te,bins,True,True); print(lam,'mean',r2.mean(),'median',np.median(r2))
EOF
PYTHONPATH=. python $TMPDIR/dbg2.py
```

```
right ALM (6, 5) 205.9854062972124 [12.54291519  2.01150617  9.11698789  2.55834076  1.51798492  1.91594178]
left ALM (8, 8) 203.1111774781807 [3.92784363 3.02581443 1.77477742 6.72576681 4.48663241 2.43559744
 4.14503661 2.19854572]
mean -334.89802450247504 median -93.52967720805701 [-4.66347624e+03 -1.24517818e+03 -2.75918773e+02 -2.62340220e+01
 -3.47235808e+00]
lagged shape (334, 730, 54)
0.01 mean -138.49132063224891 median -42.72106316782098
1 mean -7.393088297842347 median -2.4193921027952126
100 mean -0.15594955950067899 median 0.03346974963417615
10000.0 mean 0.07789642128273598 median 0.058215421623592944
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cd entries/hasnain-2025 && python - <<'EOF'
import re
s=open('/tmp/claude-1001/dbg2.py').read()
s=s.replace("z,_=ms.zscore(ms.rates([s['spikes'][i] for i in bil[p][reg]],go,W),W)","z,_=ms.zscore(ms.rates([s['spikes'][i] for i in bil[p][reg]],go,W),W,mode='all')")
open('/tmp/claude-1001/dbg3.py','w').write(s)
EOF
PYTHONPATH=. python $TMPDIR/dbg3.py
```

```
right ALM (5, 6) 32.81365660604775 [1.27681883 1.043102   1.04991187 1.21886922 1.61078737]
left ALM (7, 10) 19.340931178303627 [1.00489675 2.10925261 1.06773338 1.16948294 1.10407058 1.41140917
 1.09054366]
mean -57.78412475707963 median -28.13871994784901 [-308.86167533 -217.5768745   -81.90851373   -9.27539124   -1.36340128]
lagged shape (334, 730, 45)
0.01 mean -47.52705085354148 median -25.960156430443988
1 mean -3.7581153765733792 median -2.3950638856157167
100 mean 0.15002858539745048 median 0.19838314670247736
10000.0 mean 0.1268365252594679 median 0.11291764439456092
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cd entries/hasnain-2025 && cat >> $TMPDIR/dbg3.py <<'EOF'
ms.RIDGE_LAMBDA=0.01
for lags in [1,2,9]:
    ms.N_LAGS=lags
    old=ms.lagged
    r2=ms.ridge_r2(P['right ALM'],P['left ALM'],tr,te,bins,True,True); print('lags',lags,'mean',r2.mean(),'median',np.median(r2))
ms.N_LAGS=9
xl=ms.lagged(P['right ALM'],9)[:,400].astype(float); print('cond', np.linalg.cond(np.corrcoef(xl[tr].T)))
yt=P['left ALM'][:,400]
# per-bin: train R2 and test R2 at bin 400
import numpy.linalg as la
x=xl[tr]-xl[tr].mean(0); y=yt[tr]-yt[tr].mean(0); w=la.lstsq(x,y,rcond=None)[0]
print('train R2', 1-((y-x@w)**2).sum()/(y**2).sum())
xe=xl[te]-xl[tr].mean(0); ye=yt[te]-yt[tr].mean(0); print('test R2', 1-((ye-xe@w)**2).sum()/((yt[te]-yt[te].mean(0))**2).sum())
print('corr2', np.mean([np.corrcoef((xe@w)[:,j],ye[:,j])[0,1]**2 for j in range(ye.shape[1])]))
EOF
PYTHONPATH=. python $TMPDIR/dbg3.py 2>&1 | tail -8
```

```
10000.0 mean 0.1268365252594679 median 0.11291764439456092
lags 1 mean -47.52705085354148 median -25.960156430443988
lags 2 mean -47.52705085354148 median -25.960156430443988
lags 9 mean -47.52705085354148 median -25.960156430443988
cond 3091481.9676656676
train R2 0.728329148934803
test R2 -24.378711092138698
corr2 0.043547985617017115
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cd entries/hasnain-2025 && cat >> $TMPDIR/dbg3.py <<'EOF'
x1=P['right ALM'][:,:, :]
for L in [1,3,9]:
    xl=np.concatenate([np.roll(x1,k,axis=1) for k in range(L)],axis=2)
    out=[]
    for t in bins[::10]:
        a=xl[tr,t].astype(float); b=P['left ALM'][tr,t].astype(float)
        ma,mb=a.mean(0),b.mean(0); sa=a.std(0,ddof=1)
        z=(a-ma)/sa; w=np.linalg.solve(z.T@z+0.01*np.eye(z.shape[1]), z.T@(b-mb))
        pr=((xl[te,t]-ma)/sa)@w+mb; yy=P['left ALM'][te,t]
        out.append(1-((yy-pr)**2).sum()/((yy-yy.mean(0))**2).sum())
    print('L',L,'mean',np.mean(out),'median',np.median(out))
# outliers in test predictors
a=P['right ALM'][tr]; b=P['right ALM'][te]; print('train absmax',np.abs(a).max((0,1)),'test absmax',np.abs(b).max((0,1)))
EOF
PYTHONPATH=. python $TMPDIR/dbg3.py 2>&1 | tail -4
```

```
L 1 mean -0.30128558322708354 median 0.13650157033702598
L 3 mean -8.5199892202654 median -1.281963442859804
L 9 mean -48.9373199027878 median -26.539782142101732
train absmax [28.31687885 32.32860023 23.43991728 25.80129826 28.15131393] test absmax [32.81365661 18.22111387 19.15221406 25.09395261 29.09102181]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('map_subspace.py').read()
s=s.replace('def ridge_r2(src, tgt, train, test, bins, standardize, pooled):','def ridge_r2(src, tgt, train, test, bins, standardize, pooled, lam=None):')
s=s.replace('''    xl = lagged(src)
    r2 = np.empty(len(bins))''','''    lam = RIDGE_LAMBDA if lam is None else lam
    xl = lagged(src)
    r2 = np.empty(len(bins))''')
s=s.replace('w = np.linalg.solve(z.T @ z + RIDGE_LAMBDA * np.eye(z.shape[1]), z.T @ (ytr - my))','w = np.linalg.solve(z.T @ z + lam * np.eye(z.shape[1]), z.T @ (ytr - my))')
s=s.replace('''def auroc(x_right, x_left):
    """P(right > left), ties 0.5."""
    allx = np.r_[x_right, x_left]
    from scipy.stats import rankdata
    r = rankdata(allx)
    n1, n2 = len(x_right), len(x_left)
    return (r[:n1].sum() - n1 * (n1 + 1) / 2) / (n1 * n2)


''','')
open('map_subspace.py','w').write(s)
s=open('/tmp/claude-1001/nb_src.py').read()
add='''
# %% [markdown]
# Variants, not readings of the claim: the claim fixes lambda = 0.01. The lagged projections of the
# smoothed rates are nearly collinear, so the variants show the same decoding with larger penalties,
# and the median over bins next to the mean (main seed plus 1, T1, standardized predictors, R1).

# %% tags=["claim:fig4d-alm-predicts-medulla-null", "claim:fig4d-decoding-asymmetry"]
p0 = next(iter(bilateral))
xl0 = ms.lagged(fits[(p0, "right ALM", "main")]["proj"])[:, bins[300]].astype(float)
print("condition number of the predictor correlation matrix, one bilateral session, one bin: %.3g"
      % np.linalg.cond(np.corrcoef(xl0.T)))
lam_rows = []
for lam in (0.01, 1.0, 100.0, 1e4):
    rng_l = np.random.default_rng(seed("fig4d-alm-predicts-medulla-null", 1))
    for kind, sess_map, pairs in (("ALM-medulla", alm_med, [("ALM", "medulla"), ("medulla", "ALM")]),
                                  ("ALM-ALM", bilateral, [("right ALM", "left ALM"), ("left ALM", "right ALM")])):
        for p in sess_map:
            perm = rng_l.permutation(len(sessions[p]["go"]))
            ntr = int(round(0.7 * len(perm)))
            for src, tgt in pairs:
                r2 = ms.ridge_r2(fits[(p, src, "main")]["proj"], fits[(p, tgt, "main")]["proj"],
                                 perm[:ntr], perm[ntr:], bins, True, True, lam=lam)
                lam_rows.append(dict(lam=lam, kind=kind, session=p, src=src, mean=100 * r2.mean(), median=100 * np.median(r2)))
lam_df = pd.DataFrame(lam_rows)
lam_df["dir"] = np.where(lam_df.kind == "ALM-ALM", "ALM to ALM", np.where(lam_df.src == "ALM", "ALM to medulla", "medulla to ALM"))
lam_sum = lam_df.groupby(["lam", "session", "dir"])[["mean", "median"]].mean().groupby(["lam", "dir"]).agg(["mean", "sem"])
print(lam_sum.round(2).to_string())
for lam, d in lam_df.groupby("lam"):
    a = d[d.dir == "ALM to medulla"].set_index("session")["mean"]
    b = d[d.dir == "medulla to ALM"].set_index("session")["mean"]
    t, pv = stats.ttest_rel(a, b.loc[a.index])
    print(f"lambda {lam:g}: ALM to medulla minus medulla to ALM {(a - b.loc[a.index]).mean():.2f} points, paired t p = {pv:.3g}")
'''
s=s.replace('''print("elapsed %.0f s" % (time.time() - T0))

# %% [markdown]
# ## Claim fig4f''', '''print("elapsed %.0f s" % (time.time() - T0))
'''+add+'''
# %% [markdown]
# ## Claim fig4f''')
open('/tmp/claude-1001/nb_src.py','w').write(s)
EOF
grep -n "Variants, not readings" $TMPDIR/nb_src.py; date -u
```

```
595:# Variants, not readings of the claim: the claim fixes lambda = 0.01. The lagged projections of the
Sun Nov 22 02:33:24 UTC 2026
```

**Agent calls Bash**

```bash
cd  && sed -i 's/                                 fallback=nfb,/                                 fallback=nfb, z_absmax=float(np.abs(z).max()),/' $TMPDIR/nb_src.py && grep -n "z_absmax" $TMPDIR/nb_src.py; python3 tools/entry.py --help 2>&1 | head -20; grep -n "def cmd_\|runtime_minutes\|tags\|sanity\|claim:" tools/entry.py | head -40
```

```
334:                                 fallback=nfb, z_absmax=float(np.abs(z).max()),
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
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/entry.py; sed -n 200,330p tools/entry.py
```

```
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025 && cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
pymanopt
remfile
scikit-learn
scipy
umap-learn
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: hasnain-2025
type: reproduction
title: Movement-null subspaces in ALM and the medullary reticular nuclei (Hasnain, Han & Economo 2025)
description: Tests the findings of Hasnain, Han and Economo (2025) on the Mesoscale Activity Map dataset,
  DANDI:000363, which the paper reuses for its Figure 4. It selects the bilateral ALM and the ALM and
  medulla sessions, then tests lick-direction selectivity in the medullary reticular nuclei, the variance
  in movement-null and movement-potent subspaces in each region, cross-region decoding of movement-null
  activity, the dimensionality of the movement-null subspaces and a joint UMAP embedding. The paper's own
  cell-type-specific recordings (Figures 1 to 3) are not public.
license: Apache-2.0
notebooks:
- path: reproduce_hasnain_2025.ipynb
  title: Reproducing the MAP analyses of Hasnain et al. (2025) from dandiset 000363
  runtime_minutes: 30
helpers:
- map_subspace.py
related:
- id: dandi:000363/0.231012.2129
  relation: uses_data
- id: doi:10.1101/2025.10.17.682917
  relation: reproduces
EOF
cat > $TMPDIR/build_nb.py <<'EOF'
import re, nbformat
src=open('/tmp/claude-1001/nb_src.py').read()
chunks=re.split(r'^# %%(.*)$', src, flags=re.M)
nb=nbformat.v4.new_notebook()
nb.metadata={"kernelspec":{"name":"python3","display_name":"Python 3","language":"python"},"language_info":{"name":"python"}}
for head, body in zip(chunks[1::2], chunks[2::2]):
    body=body.strip('\n')
    tags=re.findall(r'tags=\[(.*)\]', head)
    tags=[t.strip().strip('"') for t in tags[0].split(',')] if tags else []
    if '[markdown]' in head:
        text='\n'.join(l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.splitlines())
        c=nbformat.v4.new_markdown_cell(text)
    else:
        c=nbformat.v4.new_code_cell(body)
    if tags: c.metadata['tags']=tags
    nb.cells.append(c)
nbformat.write(nb,'entries/hasnain-2025/reproduce_hasnain_2025.ipynb')
print(len(nb.cells))
EOF
python3 $TMPDIR/build_nb.py && cd  && python3 tools/entry.py lock entries/hasnain-2025 2>&1 | tail -5
```

```
32
wrote hasnain-2025/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
d=s.replace("tables = ms.survey(assets)","import json\nres=json.load(open('/tmp/claude-1001/survey.json'))\ntables={r['path']:dict(target=r['target'],classification=r['cls'],quality=r['q'],anno=[a if isinstance(a,str) else '' for a in r['anno']],subject=r['path'].split('/')[0],n_trials=r['ntr']) for r in res}")
d=d.replace("bilateral, alm_med = ms.select_sessions(tables)\n","bilateral, alm_med = ms.select_sessions(tables)\nbilateral=dict(list(bilateral.items())[:2]); alm_med=dict(list(alm_med.items())[:3])\n",1)
for a in ["for k in SEED_OFFSETS[1:]:","for k in SEED_OFFSETS:\n    d = decode","for k in SEED_OFFSETS:\n    sd_ =","for k in SEED_OFFSETS:\n    sel_runs"]:
    d=d.replace(a,a.replace("SEED_OFFSETS[1:]","SEED_OFFSETS[1:2]").replace("SEED_OFFSETS:","SEED_OFFSETS[:2]:"))
d=d.replace("plt.tight_layout()","plt.tight_layout(); plt.close('all')")
open('dev.py','w').write(d)
EOF
cd entries/hasnain-2025 && source $TMPDIR/env/bin/activate && MPLBACKEND=Agg PYTHONWARNINGS=ignore PYTHONPATH=. python $TMPDIR/dev.py 2>&1 | sed -n '/condition number/,/lambda 10000/p'; date -u
```

```
condition number of the predictor correlation matrix, one bilateral session, one bin: 1.26e+06
                             mean             median         
                             mean       sem     mean      sem
lam      dir                                                 
0.01     ALM to ALM     -11644.88  11476.97 -2817.59  2755.24
         ALM to medulla   -313.53    266.85  -217.85   200.81
         medulla to ALM   -455.45    288.47  -145.07   104.11
1.00     ALM to ALM       -378.45    344.65  -127.00   111.50
         ALM to medulla    -24.01     15.04   -16.76    17.29
         medulla to ALM    -39.83     30.72   -13.53    11.13
100.00   ALM to ALM          0.73      9.34     6.67     1.39
         ALM to medulla     27.32      9.40    25.15    10.17
         medulla to ALM      7.41     12.43    12.60     6.93
10000.00 ALM to ALM          5.78      2.48     3.86     2.40
         ALM to medulla      9.65      2.61     8.12     2.68
         medulla to ALM      4.52      2.35     3.96     2.66
lambda 0.01: ALM to medulla minus medulla to ALM 141.92 points, paired t p = 0.757
lambda 1: ALM to medulla minus medulla to ALM 15.82 points, paired t p = 0.621
lambda 100: ALM to medulla minus medulla to ALM 19.90 points, paired t p = 0.0253
lambda 10000: ALM to medulla minus medulla to ALM 5.12 points, paired t p = 0.171
[... 1 more lines not kept]
```

**Agent**

Subset runs cleanly. Starting the full run through the entry tool (estimated 30 to 35 minutes).

**Agent calls Bash**

```bash
cd  && date -u && python3 tools/entry.py all entries/hasnain-2025 2>&1 | tail -30; date -u
```

```
Sun Nov 22 02:40:20 UTC 2026
Installed kernelspec registry-hasnain-2025 in executed/hasnain-2025/.venv/share/jupyter/kernels/registry-hasnain-2025
0 error(s)
pass  reproduce_hasnain_2025.ipynb  (1812 s)
Sun Nov 22 03:10:45 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/out.txt
import nbformat
nb=nbformat.read('executed/hasnain-2025/reproduce_hasnain_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f'===== cell {i} tags {c.metadata.get("tags")}')
    for o in c.outputs:
        if o.output_type=='stream': print(o.text)
        elif 'data' in o and 'text/plain' in o.data and 'image/png' not in o.data: print(o.data['text/plain'])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
wc -l $TMPDIR/out.txt; sed -n 1,140p $TMPDIR/out.txt
```

```
<persisted-output>
Output too large (125.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/692f4cef-ab29-4885-8c4d-04ce2c48eac9/tool-results/b0z421ibu.txt

Preview (first 2KB):
479 /tmp/claude-1001/out.txt
===== cell 1 tags None
===== cell 3 tags ['sanity']
files: 174  subjects: 28
units: 272227
classification x unit_quality: {('unlabelled', 'multi'): 108153, ('good', 'good'): 60978, ('unlabelled', 'good'): 92769, ('good', 'multi'): 8475, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cut -c1-400 $TMPDIR/out.txt | sed -n 4,200p
```

```
units: 272227
classification x unit_quality: {('unlabelled', 'multi'): 108153, ('good', 'good'): 60978, ('unlabelled', 'good'): 92769, ('good', 'multi'): 8475, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float
(classification, has CCF annotation): {('unlabelled', False): 200922, ('good', True): 69453, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan),
sessions per probe target: {'left ALM': 108, 'left Striatum': 54, 'right ALM': 103, 'right Striatum': 57, 'right Midbrain': 68, 'right Thalamus': 36, 'left Midbrain': 68, 'left Thalamus': 45, 'left Medulla': 23, 'right Medulla': 24, 'right ECT': 14, 'left ECT': 18, 'left BLA': 9, 'right BLA': 8}
sessions with probes in both ALMs: 60 from 18 mice
sessions with an ALM and a medulla probe: 36 from 8 mice
units in the medullary nuclei of M2: {'Intermediate reticular nucleus': 279, 'Gigantocellular reticular nucleus': 704, 'Parvicellular reticular nucleus': 190}
units labelled MOs (any probe): 7346
units labelled MOs on probes not targeting ALM: 0

===== cell 5 tags ['sanity']
assets in 0.230822.0128: 174  same paths as pinned: 103  same sessions: 174
example path there: sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+ogen.nwb

              units    spikes good                                       first_spikes                                        acquisition
0.231012.2129  1205  24087958  279  [0.000342, 0.051943, 0.078377, 0.116145, 0.130...  [BehavioralEvents, BehavioralTimeSeries, Elect...
0.230822.0128  1205  24087958  279  [0.000342, 0.051943, 0.07837
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cut -c1-300 $TMPDIR/out.txt | sed -n 200,480p
```

```
20      ALM    Zall  V3  5     90.862    4.930    93.513   3.731  -2.652 -1.449  0.221     NaN
24      ALM    main  V1  5     54.486   15.438    77.333  11.780 -22.848 -1.929  0.126  98.602
25      ALM    main  V2  5     23.969    5.373    34.134  11.774 -10.165 -1.616  0.181  58.103
26      ALM    main  V3  5     73.789   13.902    85.999   7.720 -12.211 -1.362  0.245     NaN
3   medulla      B2  V1  5     38.819    9.569    85.307   8.101 -46.488 -6.734  0.003  96.855
4   medulla      B2  V2  5     28.489    6.535    51.175   5.621 -22.686 -4.647  0.010  79.664
5   medulla      B2  V3  5     72.773   15.886    89.915   6.579 -17.142 -2.059  0.109     NaN
9   medulla      D2  V1  5     54.641   17.378    66.875  15.887 -12.234 -0.846  0.445  98.893
10  medulla      D2  V2  5     33.990    4.594    41.613  13.899  -7.623 -0.985  0.380  75.603
11  medulla      D2  V3  5     71.016   10.169    76.594  17.592  -5.579 -0.481  0.656     NaN
15  medulla      W2  V1  5     58.014   21.705    63.705  20.018  -5.690 -0.310  0.772  99.161
16  medulla      W2  V2  5     35.132    6.188    40.510  15.886  -5.378 -0.559  0.606  75.642
17  medulla      W2  V3  5     73.671   12.783    73.122  21.549   0.549  0.037  0.973     NaN
21  medulla    Zall  V1  5     62.700    8.295    70.080   6.213  -7.380 -1.319  0.258  98.781
22  medulla    Zall  V2  5     31.510    4.804    37.904   5.027  -6.393 -2.959  0.042  69.414
23  medulla    Zall  V3  5     84.135    6.375    84.467   1.038  -0.332 -0.108  0.919     NaN
27  medulla    main  V1  5     54.641   17.378    66.875  15.887 -12.234 -0.846  0.445  98.893
28  medulla    main  V2  5     33.990    4.594    41.613  13.899  -7.623 -0.985  0.380  75.603
29  medulla    main  V3  5     71.016   10.169    76.594  17.592  -5.578 -0.481  0.656     NaN
expected ALM null 36.0 +- 7.4, potent 37.1 +- 8.7 (p = 0.15); medulla null 26.4 +- 3.9, potent 44.8 +- 7.12 (p = 1.9e-9)
[... 259 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat, base64
nb=nbformat.read('executed/hasnain-2025/reproduce_hasnain_2025.ipynb',4)
k=0
for i,c in enumerate(nb.cells):
    for o in c.get('outputs',[]):
        if 'data' in o and 'image/png' in o.data:
            open(f'/tmp/claude-1001/fig{i}.png','wb').write(base64.b64decode(o.data['image/png'])); print(i)
EOF
date -u
```

```
10
31
Sun Nov 22 03:11:37 UTC 2026
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig31.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig10.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd entries/hasnain-2025 && python3 - <<'EOF'
s=open('map_subspace.py').read()
s=s.replace('''    return dict(target=target, classification=_dec(u["classification"][:]),''','''    classification = [c if isinstance(c, str) else "missing" for c in _dec(u["classification"][:])]
    return dict(target=target, classification=classification,''')
open('map_subspace.py','w').write(s)
EOF
grep -n '"missing"' map_subspace.py
```

```
111:    classification = [c if isinstance(c, str) else "missing" for c in _dec(u["classification"][:])]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
old_start=s.index('# %% tags=["claim:fig4c-alm-null-potent-similar", "claim:fig4c-medulla-null-smaller"]\nseed_rows = []')
old_end=s.index('# %% [markdown]\n# ## Claim fig4e')
new='''# %% tags=["claim:fig4c-alm-null-potent-similar", "claim:fig4c-medulla-null-smaller"]
seed_rows = []
for rname in ("main", "B2"):
    for k in SEED_OFFSETS:
        rng_k = np.random.default_rng(seed("fig4c-alm-null-potent-similar", k))
        for p, s in alm_med.items():
            for reg in ("ALM", "medulla"):
                f0 = fits[(p, reg, "main")]
                if k == 0:
                    fit = fits[(p, reg, rname)]
                else:
                    mv = f0["mv"] if rname == "main" else ms.movement_mask(sessions[p]["speed"], sessions[p]["log_thr"], short_runs_move=True)
                    fit = ms.fit_region(f0["z"], mv, rng_k)
                ve = ms.ve_readings(fit)
                seed_rows.append(dict(reading=rname, offset=k, session=p, region=reg, d_null=fit["d"][0], d_pot=fit["d"][1],
                                      d_null_raw=fit["d_raw"][0],
                                      **{f"{V} {n}": 100 * x for V, vv in ve.items() for n, x in zip(("null", "pot", "both"), vv)}))
seed_df = pd.DataFrame(seed_rows)
srows = []
for (rname, off, reg), d in seed_df.groupby(["reading", "offset", "region"]):
    for V in ("V1", "V2", "V3"):
        t, pv = stats.ttest_rel(d[f"{V} null"], d[f"{V} pot"])
        srows.append(dict(reading=rname, offset=off, region=reg, V=V, null=d[f"{V} null"].mean(), pot=d[f"{V} pot"].mean(), p=pv,
                          mean_d_null=d.d_null.mean()))
seed_tab = pd.DataFrame(srows)
print(seed_tab.round(4).to_string())
print("elapsed %.0f s" % (time.time() - T0))

'''
s=s[:old_start]+new+s[old_end:]
s=s.replace('''for off, d in seed_df.groupby("offset"):
    a = d[d.region == "ALM"].d_null.values
    b = d[d.region == "medulla"].d_null.values
    # N1 before the cap is not stored per seed; the capped d_null equals it unless the cap applied
    t, pv = stats.ttest_rel(b, a)
    print(f"seed offset {off}: N1 (capped) medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {pv:.3g}")''','''for off, d in seed_df[seed_df.reading == "main"].groupby("offset"):
    a = d[d.region == "ALM"].d_null_raw.values
    b = d[d.region == "medulla"].d_null_raw.values
    t, pv = stats.ttest_rel(b, a)
    print(f"seed offset {off}: N1 medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {pv:.3g}")''')
s=s.replace("Seed check for fig4c and fig4e: the main reading again under the claim's seed plus 1000 to 4000\n# (dimension shuffles and the optimizer's start).",
 "Seed check for fig4c and fig4e: the main reading and reading B2 again under the claim's seed plus\n# 1000 to 4000 (dimension shuffles and the optimizer's start).")
open('nb_src.py','w').write(s)
EOF
grep -n "Seed check" -A2 $TMPDIR/nb_src.py
```

```
429:# Seed check for fig4c and fig4e: the main reading and reading B2 again under the claim's seed plus
430-# 1000 to 4000 (dimension shuffles and the optimizer's start).
431-
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025 && source $TMPDIR/env/bin/activate && cat > $TMPDIR/b2seed.py <<'EOF'
import json, zlib, numpy as np, pandas as pd
from scipy import stats
import map_subspace as ms
res=json.load(open('/tmp/claude-1001/survey.json'))
tables={r['path']:dict(target=r['target'],classification=[c if isinstance(c,str) else 'missing' for c in r['cls']],quality=r['q'],anno=[a if isinstance(a,str) else '' for a in r['anno']]) for r in res}
bil,am=ms.select_sessions(tables); urls=dict(ms.asset_urls()); W=ms.WINDOWS['W1']
data={}
for p,s in am.items():
    se=ms.load_session(urls[p],sorted(s['ALM']+s['medulla'])); keep=ms.trial_mask(se); go=ms.go_times(se)[keep]
    sp=ms.speed_bins(se,go,W); lt=ms.otsu_threshold(np.log10(sp[np.isfinite(sp)&(sp>0)]))
    for reg in ('ALM','medulla'):
        z,_=ms.zscore(ms.rates([se['spikes'][i] for i in s[reg]],go,W),W)
        data[(p,reg)]=(z,ms.movement_mask(sp,lt,True))
rows=[]
for k in [1000,2000,3000,4000]:
    rng=np.random.default_rng(zlib.crc32(b"hasnain-2025/fig4c-alm-null-potent-similar")+k)
    for p in am:
        for reg in ('ALM','medulla'):
            z,mv=data[(p,reg)]; fit=ms.fit_region(z,mv,rng); ve=ms.ve_readings(fit)
            rows.append(dict(k=k,reg=reg,V1n=ve['V1'][0],V1p=ve['V1'][1],V2n=ve['V2'][0],V2p=ve['V2'][1]))
df=pd.DataFrame(rows)
for (k,reg),d in df.groupby(['k','reg']):
    print(k,reg,'V1',round(100*d.V1n.mean(),1),round(100*d.V1p.mean(),1),'p=%.4f'%stats.ttest_rel(d.V1n,d.V1p)[1],'V2',round(100*d.V2n.mean(),1),round(100*d.V2p.mean(),1),'p=%.4f'%stats.ttest_rel(d.V2n,d.V2p)[1])
EOF
PYTHONPATH=. PYTHONWARNINGS=ignore python $TMPDIR/b2seed.py; date -u
```

```
1000 ALM V1 43.9 85.0 p=0.0236 V2 20.1 39.0 p=0.0262
1000 medulla V1 38.8 85.3 p=0.0025 V2 28.5 51.2 p=0.0097
2000 ALM V1 43.8 84.8 p=0.0233 V2 19.9 38.9 p=0.0259
2000 medulla V1 38.8 85.3 p=0.0025 V2 28.5 51.2 p=0.0097
3000 ALM V1 44.5 84.4 p=0.0267 V2 20.1 38.6 p=0.0261
3000 medulla V1 38.8 85.3 p=0.0025 V2 28.5 51.2 p=0.0097
4000 ALM V1 43.9 85.0 p=0.0236 V2 20.1 39.0 p=0.0262
4000 medulla V1 38.8 85.3 p=0.0025 V2 28.5 51.2 p=0.0097
Sun Nov 22 03:18:14 UTC 2026
```

**Agent**

Seed checks are stable for both readings. Writing the conclusion cells and summary now.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
def after(marker, text):
    global s
    i=s.index(marker); j=s.index('# %%', i+len(marker))
    s=s[:j]+text+'\n'+s[j:]
def md(t):
    return '# %% [markdown]\n'+'\n'.join('# '+l if l else '#' for l in t.strip().split('\n'))+'\n\n'
after('print(f"at least {thr} good units: bilateral {len(b2)} sessions, ALM and medulla {len(a2)} sessions")', md('''
**Result: not reproduced.** With the dataset's CCF labels, the paper's rule gives 17 bilateral ALM
sessions from 9 mice (paper 20 from 10) and 5 ALM and medulla sessions from 4 mice (paper 16 or 11
from 7). The left ALM count (1001) is within tolerance of 1055; the right ALM count (858 against 961),
the ALM count of the ALM and medulla sessions (300 against 604) and the medulla count (340 against
724) are not. Only units classified good carry a CCF label, so the reading with all units of a region
cannot be formed; the nearest form, every unit on the region's probe, gives counts several times the
paper's (for example 3668 units on medulla probes). With a threshold of 20 good units the ALM and
medulla sessions number 14, with 25 they number 9.
'''))
after('print(by_sess.round(1).to_string())', md('''
**Result: partially reproduced.** Of 340 medulla units, under E1 with the Bonferroni threshold 34.1%
are selective in the sample epoch, 52.9% in the delay epoch and 86.5% in the response epoch (paper 7,
21 and 49%). The order holds (response highest, sample lowest) under every reading and seed, but no
reading brings a value within tolerance: E2 sub-epochs give 31.2 to 67.4%, and the uncorrected
threshold gives higher values. Over the five seeds the E1 Bonferroni values range from 31.8 to 34.7%
(sample), 51.5 to 52.9% (delay) and 85.9 to 87.1% (response). The selection holds 340 units where the
paper has 724, so the units differ from the paper's.
'''))
after('print("elapsed %.0f s" % (time.time() - T0))\n\n', '')  # no-op guard
s=s.replace('''print(seed_tab.round(4).to_string())
print("elapsed %.0f s" % (time.time() - T0))
''','''print(seed_tab.round(4).to_string())
print("elapsed %.0f s" % (time.time() - T0))

'''+md('''
**Result (fig4c-alm-null-potent-similar): partially reproduced.** Over the 5 ALM and medulla
sessions, the paired t test finds no difference between null and potent variance in ALM under the
main reading (V1 54.5 against 77.3%, p = 0.126; V2 24.0 against 34.1%, p = 0.181; V3 p = 0.245), nor
under W2 or D2, but no reading of M3 to M6 puts both means within tolerance of 36.0 and 37.1%. Under
B2 the test finds potent above null (V1 p = 0.024, V2 p = 0.023), with means out of tolerance. Only
the z-score of example.m, a variant in the claims file, matches in full (V2 30.7 against 29.1%,
p = 0.119). With 5 sessions the test has little power: the main-reading V1 difference is 22.8 points.
The values are the same under the five seeds (V1 p 0.099 to 0.126; B2 V1 p 0.023 to 0.027).

**Result (fig4c-medulla-null-smaller): reproduced, resting on reading B2.** Under B2 (supra-threshold
runs shorter than 100 ms counted as moving) with V2, the medulla null subspace explains 28.5% and the
potent subspace 51.2% (tolerances 26.4 +- 3.9 and 44.8 +- 7.12), paired t p = 0.0097, the same under the
five seeds. Under the main reading B1 the difference is not significant (V1 54.6 against 66.9%,
p = 0.445; V2 p = 0.380), nor under W2 or D2; under the example.m z-score V2 gives p = 0.042 with the
null mean outside tolerance. The criterion accepts any one reading, so the claim is reproduced under
B2, which also makes the ALM difference significant.
'''))
after('print(f"reading {rname}: N1 medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {pv:.3g}")', md('''
**Result: not reproduced.** The medulla's movement-null dimensionality is not lower than ALM's under
either reading. N1 (shuffle dimension): medulla 6.8, ALM 7.4, p = 0.646, lower in 2 of 5 sessions, and
p = 0.577 to 0.646 over the five seeds; the other readings of M3 to M5 give p = 0.077 to 0.646 (B2 has
the medulla higher). N2 (participation ratio): medulla 3.13, ALM 5.09, p = 0.0915, lower in 4 of 5;
divided by the unit count, p = 0.31. The medulla has fewer units than ALM in 2 sessions and more in 3.
'''))
s=s.replace('''    print(f"lambda {lam:g}: ALM to medulla minus medulla to ALM {(a - b.loc[a.index]).mean():.2f} points, paired t p = {pv:.3g}")
''','''    print(f"lambda {lam:g}: ALM to medulla minus medulla to ALM {(a - b.loc[a.index]).mean():.2f} points, paired t p = {pv:.3g}")

'''+md('''
**Result (fig4d-alm-predicts-medulla-null): not reproduced.** With lambda = 0.01 the decoder fails on
held-out trials under every reading: mean R2 from -228.5 to -149.8% for ALM to medulla and from
-7333 to -2712% for ALM to ALM (A1), against 40 and 54%, and the same under the five seeds. The nine
lagged copies of the smoothed projections are nearly collinear (condition number about 1e6), and
lambda = 0.01 barely regularizes them. In the variants with larger penalties R2 is at most 21.3% (ALM
to medulla, lambda 100), and ALM to ALM (5.8%) stays below ALM to medulla, the reverse of the paper.

**Result (fig4d-decoding-asymmetry): not reproduced.** Under every reading the paired t test of ALM to
medulla against medulla to ALM gives p = 0.47 to 0.90 over the 5 sessions, and medulla to ALM R2 is
-378 to -185%, against 21 +- 6.7%. In the lambda = 100 variant ALM to medulla exceeds medulla to ALM
by 13.5 points (p = 0.040), with medulla to ALM at 7.8%.
'''))
after('print("elapsed %.0f s, peak memory %.0f MB" % (time.time() - T0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))', md('''
**Result: partially reproduced.** In the test-set embedding 20.0% of ALM units have no medulla unit
among their 10 nearest neighbours (shuffled labels 0.1%), 20.0 to 25.7% over the five seeds, so part
of the ALM movement-null patterns has no medulla counterpart, as the paper reports. The second part
of the criterion does not hold: only 55.9% of medulla units have an ALM unit among their neighbours
(shuffled 99.8%; 52.1 to 60.6% over seeds), and 7 of the 39 grid cells that hold medulla units hold
no ALM unit, so the medulla units do not fall within the region occupied by ALM units. The judgment
rests on these neighbour counts and the plot, as the paper's rests on inspection.
'''))
s+='\n'+md('''
## Summary

| Claim | Outcome |
|---|---|
| Eleven claims on the paper's own recordings (Figures 1 to 3, Extended Data Figures 2 and 3) | Blocked: data missing |
| map-session-selection | Not reproduced |
| fig4b-medulla-selectivity | Partially reproduced |
| fig4c-alm-null-potent-similar | Partially reproduced |
| fig4c-medulla-null-smaller | Reproduced, resting on reading B2 |
| fig4d-alm-predicts-medulla-null | Not reproduced |
| fig4d-decoding-asymmetry | Not reproduced |
| fig4e-medulla-null-lower-dimension | Not reproduced |
| fig4f-medulla-null-not-spanning-alm | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

How the analysis differs from the paper's:

- The selection gives 5 ALM and medulla sessions (paper 16 or 11) and 17 bilateral sessions (paper
  20), so every Figure 4 test runs on fewer sessions and units than the paper's.
- The movement threshold is Otsu's threshold on the log speed of the smoothed keypoints, where the
  paper set it by hand; the keypoints are smoothed (3 frames) first.
- Ignore, photostimulation and early-lick trials are left out.
- The dimension shuffle uses 100 shuffles on every 4th bin (the paper 1000 on all bins).
- UMAP runs in umap-learn, not MATLAB's run_umap.
- The readings of the claims file were each run with the others held at the main reading, not in
  every combination.

What was found about the dataset:

- `anno_name` (the CCF label) is filled only for units whose `classification` is good (69453 of
  272227 units); 1852 units have no `classification`. The paper's rule for the regions can only be
  applied to good units.
- The units table holds units with very low baseline rates among those classified good, so the
  baseline z-score of the Methods gives values up to 213 s.d. in a region.
- The jaw and nose tracking are in pixels, sampled at about 294 Hz in one segment per trial; their
  frame-to-frame jitter (about 150 pixels/s unsmoothed) hides movement unless smoothed.
- Clocks: in every selected session the tongue becomes visible a median 56 to 271 ms after the go cue
  and is rarely visible before it, and lick direction is decoded from spike counts above the shuffled
  labels after the go cue (accuracy 0.58 to 0.97 at +0.8 s, shuffled 0.48 to 0.61).
- The units of the session compared are identical in versions 0.230822.0128 and 0.231012.2129.
''')
open('nb_src.py','w').write(s)
EOF
grep -c "Result" $TMPDIR/nb_src.py
```

```
Traceback (most recent call last):
  File "<stdin>", line 74, in <module>
  File "<stdin>", line 4, in after
ValueError: substring not found
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n 'reading {rname}\|elapsed %.0f s, peak' $TMPDIR/nb_src.py
```

```
497:    print(f"reading {rname}: N1 medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {pv:.3g}")
714:print("elapsed %.0f s, peak memory %.0f MB" % (time.time() - T0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'PYEOF'
import re
# reconstruct the previous edit script from the shell history is not possible; re-run with fixed helper
PYEOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/conc.py",
 "content": "s = open('/tmp/claude-1001/nb_src.py').read()\n\n\ndef md(t):\n    return '# %% [markdown]\\n' + '\\n'.join('# ' + l if l else '#' for l in t.strip().split('\\n')) + '\\n\\n'\n\n\ndef after(marker, text):\n    global s\n    i = s.index(marker)\n    j = s.find('# %%', i + len(marker))\n    if j == -1:\n        s = s.rstrip('\\n') + '\\n\\n' + text\n    else:\n        s = s[:j] + text + s[j:]\n\n\nafter('print(f\"at least {thr} good units: bilateral {len(b2)} sessions, ALM and medulla {len(a2)} sessions\")', md('''\n**Result: not reproduced.** With the dataset's CCF labels, the paper's rule gives 17 bilateral ALM\nsessions from 9 mice (paper 20 from 10) and 5 ALM and medulla sessions from 4 mice (paper 16 or 11\nfrom 7). The left ALM count (1001) is within tolerance of 1055; the right ALM count (858 against 961),\nthe ALM count of the ALM and medulla sessions (300 against 604) and the medulla count (340 against\n724) are not. Only units classified good carry a CCF label, so the reading with all units of a region\ncannot be formed; the nearest form, every unit on the region's probe, gives counts several times the\npaper's (3668 units on the medulla probes of the 5 sessions). With a threshold of 20 good units the\nALM and medulla sessions number 14, with 25 they number 9.\n'''))\nafter('print(by_sess.round(1).to_string())', md('''\n**Result: partially reproduced.** Of 340 medulla units, under E1 with the Bonferroni threshold 34.1%\nare selective in the sample epoch, 52.9% in the delay epoch and 86.5% in the response epoch (paper 7,\n21 and 49%). The order holds (response highest, sample lowest) under every reading and seed, but no\nreading brings a value within tolerance: the E2 sub-epochs give 31.2 to 67.4%, and the uncorrected\nthreshold gives higher values. Over the five seeds the E1 Bonferroni values range from 31.8 to 34.7%\n(sample), 51.5 to 52.9% (delay) and 85.9 to 87.1% (response). The selection holds 340 units where the\npaper has 724, so the units differ from the paper's.\n'''))\nafter('print(seed_tab.round(4).to_string())', md('''\n**Result (fig4c-alm-null-potent-similar): partially reproduced.** Over the 5 ALM and medulla\nsessions, the paired t test finds no difference between null and potent variance in ALM under the\nmain reading (V1 54.5 against 77.3%, p = 0.126; V2 24.0 against 34.1%, p = 0.181; V3 p = 0.245), nor\nunder W2 or D2, but no reading of M3 to M6 puts both means within tolerance of 36.0 and 37.1%. Under\nB2 the test finds potent above null (V1 p = 0.024, V2 p = 0.023), with means out of tolerance. Only\nthe z-score of example.m, a variant in the claims file, matches in full (V2 30.7 against 29.1%,\np = 0.119). With 5 sessions the test has little power: the main-reading V1 difference is 22.8 points.\nOver the five seeds the main-reading V1 p ranges from 0.099 to 0.126, and the B2 V1 p from 0.023 to\n0.027.\n\n**Result (fig4c-medulla-null-smaller): reproduced, resting on reading B2.** Under B2 (supra-threshold\nruns shorter than 100 ms counted as moving) with V2, the medulla null subspace explains 28.5% and the\npotent subspace 51.2% (tolerances 26.4 +- 3.9 and 44.8 +- 7.12), paired t p = 0.0097, the same under the\nfive seeds. Under the main reading B1 the difference is not significant (V1 54.6 against 66.9%,\np = 0.445; V2 p = 0.380), nor under W2 or D2; under the example.m z-score V2 gives p = 0.042 with the\nnull mean outside tolerance. The criterion accepts any one reading, so the claim is reproduced under\nB2, which also makes the ALM difference significant.\n'''))\nafter('print(f\"reading {rname}: N1 medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {pv:.3g}\")', md('''\n**Result: not reproduced.** The medulla's movement-null dimensionality is not lower than ALM's under\neither reading. N1 (shuffle dimension): medulla 6.8, ALM 7.4, p = 0.646, lower in 2 of 5 sessions, and\np = 0.577 to 0.646 over the five seeds; the other readings of M3 to M5 give p = 0.077 to 0.646 (under\nB2 the medulla is higher). N2 (participation ratio): medulla 3.13, ALM 5.09, p = 0.0915, lower in 4\nof 5; divided by the unit count, p = 0.31. The medulla has fewer units than ALM in 2 sessions and more\nin 3.\n'''))\nafter('''    print(f\"lambda {lam:g}: ALM to medulla minus medulla to ALM {(a - b.loc[a.index]).mean():.2f} points, paired t p = {pv:.3g}\")''', md('''\n**Result (fig4d-alm-predicts-medulla-null): not reproduced.** With lambda = 0.01 the decoder fails on\nheld-out trials under every reading: mean R2 from -228.5 to -149.8% for ALM to medulla and from\n-7333 to -2712% for ALM to ALM (A1), against 40 and 54%, and it stays negative under the five seeds.\nThe nine lagged copies of the smoothed projections are nearly collinear (condition number about\n1e6), and lambda = 0.01 barely regularizes them. In the variants with larger penalties R2 is at most\n21.3% (ALM to medulla, lambda 100), and ALM to ALM (5.8%) stays below ALM to medulla, the reverse of\nthe paper.\n\n**Result (fig4d-decoding-asymmetry): not reproduced.** Under every reading the paired t test of ALM to\nmedulla against medulla to ALM gives p = 0.46 to 0.90 over the 5 sessions, and medulla to ALM R2 is\n-378 to -185%, against 21 +- 6.7%. In the lambda = 100 variant ALM to medulla exceeds medulla to ALM\nby 13.5 points (p = 0.040), with medulla to ALM at 7.8%.\n'''))\nafter('print(\"elapsed %.0f s, peak memory %.0f MB\" % (time.time() - T0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))', md('''\n**Result: partially reproduced.** In the test-set embedding 20.0% of ALM units have no medulla unit\namong their 10 nearest neighbours (shuffled labels 0.1%), 20.0 to 25.7% over the five seeds, so part\nof the ALM movement-null patterns has no medulla counterpart, as the paper reports. The second part\nof the criterion does not hold: only 55.9% of medulla units have an ALM unit among their neighbours\n(shuffled 99.8%; 52.1 to 60.6% over the seeds), and 7 of the 39 grid cells that hold medulla units\nhold no ALM unit, so the medulla units do not all fall within the region occupied by ALM units. The\njudgment rests on these neighbour counts and the plot, as the paper's rests on inspection.\n'''))\ns = s.rstrip('\\n') + '\\n\\n' + md('''\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| Eleven claims on the paper's own recordings (Figures 1 to 3, Extended Data Figures 2 and 3) | Blocked: data missing |\n| map-session-selection | Not reproduced |\n| fig4b-medulla-selectivity | Partially reproduced |\n| fig4c-alm-null-potent-similar | Partially reproduced |\n| fig4c-medulla-null-smaller | Reproduced, resting on reading B2 |\n| fig4d-alm-predicts-medulla-null | Not reproduced |\n| fig4d-decoding-asymmetry | Not reproduced |\n| fig4e-medulla-null-lower-dimension | Not reproduced |\n| fig4f-medulla-null-not-spanning-alm | Partially reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and\nthe differences from the paper's method.\n\nHow the analysis differs from the paper's:\n\n- The selection gives 5 ALM and medulla sessions (paper 16 or 11) and 17 bilateral sessions (paper\n  20), so every Figure 4 test runs on fewer sessions and units than the paper's.\n- The movement threshold is Otsu's threshold on the log speed, where the paper set it by hand; the\n  keypoint positions are smoothed (3 frames) first.\n- Ignore, photostimulation and early-lick trials are left out.\n- The dimension shuffle uses 100 shuffles on every 4th bin (the paper 1000 on all bins).\n- UMAP runs in umap-learn, not MATLAB's run_umap.\n- The readings of the claims file were each run with the others held at the main reading, not in\n  every combination.\n\nWhat was found about the dataset:\n\n- `anno_name` (the CCF label) is filled only for units whose `classification` is good (69453 of\n  272227 units), and 1852 units have no `classification`. The paper's rule for the regions can only\n  be applied to good units.\n- Some units classified good have near-silent baselines, so the baseline z-score of the Methods gives\n  values up to 213 s.d. in a region.\n- The jaw and nose tracking are in pixels, at about 294 Hz, in one segment per trial; unsmoothed, their\n  frame-to-frame jitter hides movement.\n- Clocks: in every selected session the tongue becomes visible a median 56 to 271 ms after the go cue\n  and is rarely visible before it, and lick direction is decoded from spike counts above the shuffled\n  labels after the go cue, so the spike, video and trial clocks are consistent.\n- The units of the session compared are identical in versions 0.230822.0128 and 0.231012.2129.\n''')\nopen('/tmp/claude-1001/nb_src.py', 'w').write(s)\nprint(s.count('**Result'))\n"
}
```

```
File created successfully at: /tmp/claude-1001/conc.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 $TMPDIR/conc.py && python3 $TMPDIR/build_nb.py && cd  && date -u && python3 tools/entry.py all entries/hasnain-2025 2>&1 | tail -5; date -u
```

```
8
39
Sun Nov 22 03:19:36 UTC 2026
Installed kernelspec registry-hasnain-2025 in executed/hasnain-2025/.venv/share/jupyter/kernels/registry-hasnain-2025
0 error(s)
pass  reproduce_hasnain_2025.ipynb  (2060 s)
Sun Nov 22 03:54:11 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/out2.txt
import nbformat
nb=nbformat.read('executed/hasnain-2025/reproduce_hasnain_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f'===== cell {i} tags {c.metadata.get("tags")}')
    for o in c.outputs:
        if o.output_type=='stream': print(o.text)
        elif 'data' in o and 'text/plain' in o.data and 'image/png' not in o.data: print(o.data['text/plain'])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
grep -v "Warning\|warn(\|model.fit\|tqdm" $TMPDIR/out.txt | sed 's/elapsed [0-9]* s//; s/peak memory [0-9]* MB//' | grep -v "^===== cell" > $TMPDIR/a.txt
grep -v "Warning\|warn(\|model.fit\|tqdm" $TMPDIR/out2.txt | sed 's/elapsed [0-9]* s//; s/peak memory [0-9]* MB//' | grep -v "^===== cell" > $TMPDIR/b.txt
diff $TMPDIR/a.txt $TMPDIR/b.txt | cut -c1-250 | head -80
```

```
3,5c3,5
< classification x unit_quality: {('unlabelled', 'multi'): 108153, ('good', 'good'): 60978, ('unlabelled', 'good'): 92769, ('good', 'multi'): 8475, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'multi'): 1, (np.float64(nan), 'good'): 1, (np.float6
< (classification, has CCF annotation): {('unlabelled', False): 200922, ('good', True): 69453, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float64(nan), False): 1, (np.float6
< sessions per probe target: {'left ALM': 108, 'left Striatum': 54, 'right ALM': 103, 'right Striatum': 57, 'right Midbrain': 68, 'right Thalamus': 36, 'left Midbrain': 68, 'left Thalamus': 45, 'left Medulla': 23, 'right Medulla': 24, 'right ECT': 14
---
> classification x unit_quality: {('unlabelled', 'multi'): 108153, ('good', 'good'): 60978, ('unlabelled', 'good'): 92769, ('good', 'multi'): 8475, ('missing', 'multi'): 651, ('missing', 'good'): 1201}
> (classification, has CCF annotation): {('unlabelled', False): 200922, ('good', True): 69453, ('missing', False): 1852}
> sessions per probe target: {'left Striatum': 54, 'right Striatum': 57, 'right ALM': 103, 'left ALM': 108, 'right Midbrain': 68, 'right Thalamus': 36, 'left Thalamus': 45, 'left Midbrain': 68, 'right Medulla': 24, 'left Medulla': 23, 'left ECT': 18,
229,259c229,289
<     offset   region   V     null      pot       p  mean_d_null
< 0        0      ALM  V1  54.4855  77.3332  0.1259          7.4
< 1        0      ALM  V2  23.9688  34.1343  0.1814          7.4
< 2        0      ALM  V3  73.7886  85.9991  0.2449          7.4
< 3        0  medulla  V1  54.6412  66.8749  0.4450          6.8
< 4        0  medulla  V2  33.9901  41.6132  0.3803          6.8
< 5        0  medulla  V3  71.0158  76.5943  0.6556          6.8
< 6     1000      ALM  V1  53.7059  78.0426  0.1143          7.4
< 7     1000      ALM  V2  23.5854  34.4831  0.1655          7.4
< 8     1000      ALM  V3  73.1158  86.6607  0.2207         
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
diff $TMPDIR/a.txt $TMPDIR/b.txt | cut -c1-200 | sed -n 80,200p; date -u
```

```
> 37    main    1000      ALM  V2  23.5854  34.4831  0.1655          7.4
> 38    main    1000      ALM  V3  73.1158  86.6607  0.2207          7.4
> 39    main    1000  medulla  V1  54.6411  66.8750  0.4450          6.8
> 40    main    1000  medulla  V2  33.9901  41.6132  0.3803          6.8
> 41    main    1000  medulla  V3  71.0158  76.5944  0.6556          6.8
> 42    main    2000      ALM  V1  53.0144  78.8217  0.0987          7.6
> 43    main    2000      ALM  V2  23.6739  34.7405  0.1591          7.6
> 44    main    2000      ALM  V3  72.6911  87.3413  0.1862          7.6
> 45    main    2000  medulla  V1  54.5477  66.9939  0.4389          6.8
> 46    main    2000  medulla  V2  33.9283  41.4680  0.3838          6.8
> 47    main    2000  medulla  V3  70.8997  76.7869  0.6403          6.8
> 48    main    3000      ALM  V1  53.0144  78.8217  0.0987          7.6
> 49    main    3000      ALM  V2  23.6739  34.7405  0.1591          7.6
> 50    main    3000      ALM  V3  72.6911  87.3413  0.1862          7.6
> 51    main    3000  medulla  V1  54.6412  66.8750  0.4450          6.8
> 52    main    3000  medulla  V2  33.9901  41.6132  0.3803          6.8
> 53    main    3000  medulla  V3  71.0158  76.5943  0.6556          6.8
> 54    main    4000      ALM  V1  53.7940  78.1122  0.1093          7.6
> 55    main    4000      ALM  V2  24.0573  34.3916  0.1746          7.6
> 56    main    4000      ALM  V3  73.3639  86.6797  0.2069          7.6
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['required']));print(list(s['properties']))
o=s['properties']['outcomes']['items'];print(json.dumps(o.get('required')),list(o['properties']))
print(json.dumps(s['properties']['findings'],indent=0)[:1500])
print(json.dumps(s['properties']['provenance'],indent=0)[:1500])
"
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
["schema_version", "id", "datasets", "paper", "date", "provenance", "outcomes"]
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
["claim", "outcome"] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
{
"description": "What the attempt found, whatever the outcomes: about the dataset itself (`about: data`, for its owner and the archive, shown on the dataset's page) or about the paper (`about: paper`, shown on the paper's page).",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"statement"
],
"properties": {
"kind": {
"enum": [
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
for q in Hasnain Economo "subspace" "extratelencephalic"; do echo "== $q"; curl -s "https://api.dandiarchive.org/api/dandisets/?search=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&page_size=50" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for r in d['results']:
    v=r.get('most_recent_published_version') or r.get('draft_version'); print(r['identifier'], v['name'][:100])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/001472/versions/draft/info/" | python3 -c "
import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('description','')[:1200]); print([r.get('identifier') or r.get('url') for r in m.get('relatedResource',[])]); print(d.get('asset_count'))"
```

Result: the fetched text is not kept.

**Agent**

Now writing the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/hasnain-2025-01.yaml",
 "content": "schema_version: 3\nid: hasnain-2025-01\ndatasets:\n- archive: dandi\n  id: \"000363\"\n  version: 0.231012.2129\n  doi: 10.48324/dandi.000363/0.231012.2129\n  relation: reuses\npaper: doi:10.1101/2025.10.17.682917\ndate: 2026-11-22\nentry: hasnain-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44974161321\noutcomes:\n- claim: own-recordings-cohort\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The paper's own cell-type-specific recordings (9 mice, 27 sessions in ALM and tjM1) are not in\n    DANDI:000363, which holds the MAP recordings of Chen et al. (2024) only. The paper says \"Data will be\n    made publicly available upon publication\". A search of the DANDI archive for Hasnain, Economo,\n    subspace and extratelencephalic found no dandiset with them; DANDI:001472 holds the data of the\n    authors' earlier paper (ref 39, Nat Neurosci 2025), not these recordings.\n- claim: fig1i-selectivity-proportions\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own L-ETN and UN recordings, which are not public (see own-recordings-cohort).\n- claim: fig2c-subspace-variance\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings and video, which are not public (see own-recordings-cohort).\n- claim: fig2e-potent-only-units\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings, which are not public (see own-recordings-cohort).\n- claim: fig2f-letn-preference-like-un\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the phototagged L-ETNs of the paper's own recordings, which are not public (see\n    own-recordings-cohort).\n- claim: fig2gh-letn-span-subspaces\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings, which are not public (see own-recordings-cohort).\n- claim: ed2f-false-negatives\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings and raw waveforms, which are not public (see\n    own-recordings-cohort).\n- claim: fig3c-network-beats-linear\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings and the 400 Hz videos, which are not public (see\n    own-recordings-cohort).\n- claim: fig3d-letn-un-movement-encoding\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings and videos, which are not public (see own-recordings-cohort).\n- claim: ed3-letn-fast-switch\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings and tongue tracking, which are not public (see\n    own-recordings-cohort).\n- claim: ed3a-cd-early-un-not-letn\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's own recordings, which are not public (see own-recordings-cohort).\n- claim: map-session-selection\n  outcome: not_reproduced\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:map-session-selection\n  measured:\n  - 17\n  - 858\n  - 1001\n  - 300\n  - 340\n  notes: Units classified good (`classification`) with a CCF label of MOs on a probe described as\n    targeting ALM, or of IRN, GRN or PARN; sessions with at least 30 such units in each region. This\n    gives 17 bilateral ALM sessions from 9 mice (paper 20 from 10), with 858 right and 1001 left ALM\n    units (paper 961 and 1055; the left count is within tolerance, the right is not), and 5 ALM and\n    medulla sessions from 4 mice (paper 16 in the Results, 11 from 7 mice in the Methods), with 300\n    ALM and 340 medulla units (paper 604 and 724). The session counts match neither reading, so the\n    claim is not reproduced. Reading U2 (all units of a region) cannot be formed, as only good units\n    carry a CCF label; all units on the region's probes give 3668 medulla-probe units in the 5\n    sessions and 18784 ALM-probe units in the 17 bilateral sessions, far above the paper's counts.\n    With 20 good units as the threshold there are 31 bilateral and 14 ALM and medulla sessions, with\n    25 there are 26 and 9. The dataset holds 60 sessions with probes in both ALMs (18 mice) and 36\n    with an ALM and a medulla probe (8 mice).\n  deviations:\n  - The claims file's U1 is applied with `classification` as the 'good' label, the only label whose\n    units carry a CCF annotation; `unit_quality` also has a value 'good' but its units have no CCF\n    label unless `classification` is good.\n- claim: fig4b-medulla-selectivity\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:fig4b-medulla-selectivity\n  measured:\n  - 34.1\n  - 52.9\n  - 86.5\n  notes: 340 medulla units of the 5 ALM and medulla sessions, correct trials, 60 to 157 trials per side\n    per session. Under E1 with the Bonferroni threshold (p < 0.01) 34.1% are selective in the sample\n    epoch, 52.9% in the delay epoch and 86.5% in the response epoch (paper 7, 21 and 49%). The order\n    holds (response highest, sample lowest) under every reading and seed, so the claim is partially\n    reproduced; no reading puts a value within tolerance (E2 sub-epochs 31.2 to 67.4%; uncorrected\n    p < 0.05 higher still). Over the five seeds E1 Bonferroni gives 31.8 to 34.7%, 51.5 to 52.9% and\n    85.9 to 87.1%. By session the sample value runs from 1.7% to 48.4%. The selection holds fewer\n    sessions and units than the paper's (map-session-selection), so the units differ from the paper's.\n  deviations:\n  - Ignore, photostimulation and early-lick trials are left out (assumed; the paper does not say how\n    MAP's photostimulation and early-lick trials were treated).\n  - Epoch rates are the means of the smoothed 5 ms rates (Methods, \"Identifying selective neurons\"),\n    not z-scored.\n- claim: fig4c-alm-null-potent-similar\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:fig4c-alm-null-potent-similar\n  measured:\n  - 54.5\n  - 77.3\n  notes: 5 sessions, 40 to 85 ALM units each. Under the main reading (W1, B1, D1, baseline z-score) the\n    paired t test of null against potent variance finds no difference (V1 54.5 against 77.3%,\n    p = 0.126; V2 24.0 against 34.1%, p = 0.181; V3 73.8 against 86.0%, p = 0.245), nor under W2 or D2,\n    but no reading of M3 to M6 puts both means within tolerance, so the absence holds and the values do\n    not, a partial reproduction. Under B2 the test finds potent above null (V1 43.9 against 84.9%,\n    p = 0.024; V2 p = 0.023), with means out of tolerance, which the criterion does not count against\n    the claim. The z-score of example.m, a variant in the claims file, matches in full under V2 (30.7\n    against 29.1%, p = 0.119). With 5 sessions the test has little power; the main-reading V1\n    difference is 22.8 points. Over the five seeds the main-reading V1 p is 0.099 to 0.126, the B2 V1\n    p 0.023 to 0.027. Movement-null dimensions are 4 to 11, potent 4 to 9; 30 to 50% of bins are\n    moving.\n  deviations:\n  - 5 sessions where the paper has 16 (map-session-selection).\n  - The movement threshold is Otsu's threshold on log10 speed, a standard choice for the value between\n    the two modes that the paper set by hand; the keypoint positions are first smoothed with a Gaussian\n    of 3 frames, as unsmoothed tracking jitter makes the speed histogram unimodal.\n  - Ignore, photostimulation and early-lick trials are left out (assumed).\n  - The dimensions come from 100 shuffles of every 4th 5 ms bin, where the paper uses 1000 shuffles, to\n    fit the time limit.\n  - The readings W2, B2, D2 and the example.m z-score were each run with the others at the main\n    reading, not in every combination.\n- claim: fig4c-medulla-null-smaller\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:fig4c-medulla-null-smaller\n  measured:\n  - 28.5\n  - 51.2\n  notes: Reproduced under reading B2 (supra-threshold runs shorter than 100 ms counted as moving) with\n    V2, as the criterion accepts any one reading. There the medulla null subspace explains 28.5% and the\n    potent 51.2% (tolerances 26.4 +- 3.9 and 44.8 +- 7.12), paired t p = 0.0097 over 5 sessions, the same\n    under the five seeds; V1 gives p = 0.0025 with the potent mean (85.3%) out of tolerance. Under the\n    main reading B1 the difference is not significant (V1 54.6 against 66.9%, p = 0.445; V2 34.0\n    against 41.6%, p = 0.380), nor under W2 or D2; the example.m z-score gives V2 p = 0.042 with the\n    null mean (31.5%) out of tolerance. The outcome therefore rests on B2, which the paper does not\n    settle; under B2 the ALM difference is also significant (fig4c-alm-null-potent-similar). 31 to 128\n    medulla units per session.\n  deviations:\n  - The outcome rests on reading B2 of M4 and V2 of M6, which the paper leaves open (asked of the\n    authors under findings).\n  - 5 sessions where the paper has 16; the threshold, trial and shuffle deviations of\n    fig4c-alm-null-potent-similar apply.\n- claim: fig4d-alm-predicts-medulla-null\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:fig4d-alm-predicts-medulla-null\n  measured:\n  - -228.5\n  - -4585.2\n  notes: With lambda = 0.01, as the Methods give it, held-out R2 is far below zero under every reading\n    (T1 or T2, R1 or R2, standardized or not), from -228.5 to -149.8% for ALM to medulla (5 sessions)\n    and from -7333 to -2712% for ALM to ALM (A1, 17 sessions), against 40 and 54%; the values given as\n    measured are T1, unstandardized, R1. It stays negative under the five seeds. The nine lagged copies\n    of the smoothed projections are nearly collinear (condition number 1e6 in one bin), so the fit\n    barely regularized overfits the training trials. As variants with larger penalties, standardized\n    and pooled, R2 is at most 21.3% (ALM to medulla, lambda 100), with ALM to ALM at 5.8%, below ALM\n    to medulla, the reverse of the paper.\n  deviations:\n  - Subspaces from the main reading only; the bilateral sessions are 17, not 20.\n  - Larger penalties are shown as variants only; the claim's lambda decides the outcome.\n- claim: fig4d-decoding-asymmetry\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:fig4d-decoding-asymmetry\n  measured: -346.3\n  notes: Under every reading the paired t test of ALM to medulla against medulla to ALM gives p = 0.46 to\n    0.90 over 5 sessions, and medulla to ALM R2 is -378 to -185% (T1, unstandardized, R1 -346.3%),\n    against 21 +- 6.7%. In the lambda = 100 variant ALM to medulla exceeds medulla to ALM by 13.5 points\n    (p = 0.040), with medulla to ALM at 7.8%, outside tolerance.\n  deviations:\n  - As for fig4d-alm-predicts-medulla-null.\n- claim: fig4e-medulla-null-lower-dimension\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:fig4e-medulla-null-lower-dimension\n  notes: N1 (shuffle dimension of the stationary activity) is 6.8 in the medulla and 7.4 in ALM, p = 0.646,\n    lower in 2 of 5 sessions; 0.577 to 0.646 over the five seeds, and p = 0.077 to 0.646 under the other\n    readings of M3 to M5 (under B2 the medulla is higher, 10.0 against 8.0). N2 (participation ratio of\n    the movement-null covariance) is 3.13 against 5.09, p = 0.0915, lower in 4 of 5; per unit p = 0.31.\n    Neither reading gives p < 0.05. The medulla has 31 to 128 units and ALM 40 to 85; the medulla has\n    fewer units in 2 sessions.\n  deviations:\n  - 5 sessions; dimensions from 100 shuffles of every 4th bin.\n  - N2 is the claims file's stand-in for the scale-dependent measure of ref 70, which the paper does not\n    specify.\n- claim: fig4f-medulla-null-not-spanning-alm\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_hasnain_2025.ipynb\n  output: claim:fig4f-medulla-null-not-spanning-alm\n  notes: Test-set UMAP of 300 ALM and 340 medulla units. 20.0% of ALM units have no medulla unit among\n    their 10 nearest neighbours (0.1% with shuffled labels; 20.0 to 25.7% over the five seeds), so ALM\n    holds patterns without a medulla counterpart, as the paper reports. The criterion's second part does\n    not hold; only 55.9% of medulla units have an ALM neighbour (shuffled 99.8%; 52.1 to 60.6% over\n    seeds) and 7 of the 39 grid cells that hold medulla units hold no ALM unit, so the medulla also\n    occupies regions without ALM units. The judgment rests on these counts and the plot.\n  deviations:\n  - umap-learn with the Methods' parameters stands in for MATLAB's run_umap (claims, M10); the\n    neighbour counts are this attempt's description of the embedding, the paper judges by inspection.\n  - Units pooled over the 5 sessions; subspaces from the main reading.\nfindings:\n- kind: other\n  about: data\n  severity: major\n  statement: With the dataset's own CCF labels and quality classification, the paper's selection (at least\n    30 good units in each region) gives 5 ALM and medulla sessions from 4 mice, with 300 ALM and 340\n    medullary reticular units, where the paper reports 16 sessions (or 11 from 7 mice) with 604 and 724\n    units; and 17 bilateral ALM sessions from 9 mice where the paper reports 20 from 10. The files do not\n    hold the CCF labels that would let a user recover the paper's selection.\n- kind: metadata_insufficient\n  severity: minor\n  statement: The units' CCF annotation (`anno_name`) is filled only for units whose `classification` is\n    good (69453 of 272227 units); the others have an empty label and only the probe's target region. The\n    column description does not say this.\n- kind: metadata_insufficient\n  severity: minor\n  statement: Units carry two quality labels, `unit_quality` (good or multi, no description) and\n    `classification` (good or unlabelled), with no statement of how they differ; 1852 units have no\n    `classification` value.\n- kind: metadata_insufficient\n  severity: minor\n  statement: The jaw, nose and tongue tracking are stored with unit 'a.u.'; the values are pixel positions\n    of the side camera (about 294 Hz, one segment per trial) and a likelihood.\n- kind: other\n  about: data\n  severity: none\n  statement: The spike, video and trial clocks agree in all 22 selected sessions. The tongue becomes\n    visible a median 56 to 271 ms after the go cue, lick direction is decoded from spike counts after\n    the go cue well above shuffled labels, and jaw and nose speed rises at the go cue. The units of the\n    session compared are the same in versions 0.230822.0128 and 0.231012.2129.\n- kind: paper_inconsistency\n  statement: The paper gives two counts for the ALM and medulla sessions of the MAP data (16 sessions in\n    the Results and the Figure 4 statistics, 11 sessions from 7 mice in the Methods), two counts for the\n    bilateral ALM units (1116 in the Results, 2016 in the Methods), and two decoding windows (the\n    previous 40 ms in the Results, t and 8 preceding 5 ms bins, 45 ms, in the Methods).\n- kind: methods_unavailable\n  statement: Cross-region decoding (Figure 4d). With ridge lambda = 0.01 and the source projections at t\n    and 8 preceding bins of 20 ms-smoothed rates, the predictors are nearly collinear and held-out R2 is\n    far below zero on these data. Was lambda applied to standardized predictors, was R2 computed on\n    held-out single trials at each bin, and were trials or bins pooled before the fit?\n- kind: methods_unavailable\n  statement: Movement and stationary bins in the MAP data (Figure 4c to f). How was the hand-set\n    threshold placed, were the keypoints smoothed before taking velocity, and do supra-threshold runs\n    shorter than 100 ms count as moving? The medulla null against potent result here holds only when\n    they count as moving.\n- kind: methods_unavailable\n  statement: MAP trials and units. Were photostimulation, early-lick and ignore trials used, and is the\n    'good' label of the selection the `classification` or the `unit_quality` column, with CCF regions\n    assigned to which units?\n- kind: methods_unavailable\n  statement: Variance explained and dimensionality (Figure 4c, e). Which covariance and which d normalise\n    the variance explained of each subspace (the reported null and potent values add to the total, which\n    the Methods' formula does not give), and which measure of dimensionality, at which scale, does\n    Figure 4e use?\n- kind: methods_unavailable\n  statement: The baseline z-score (Methods, Subspace identification) divides by the baseline s.d. across\n    trials; for MAP units with near-silent baselines this gives values up to 213 s.d. Were such units\n    excluded, or was a floor applied?\n"
}
```

```
File created successfully at: attempts/hasnain-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
old="""# - Clocks: in every selected session the tongue becomes visible a median 56 to 271 ms after the go cue
#   and is rarely visible before it, and lick direction is decoded from spike counts above the shuffled
#   labels after the go cue, so the spike, video and trial clocks are consistent."""
assert old in s
s=s.replace(old,"""# - Clocks: in every selected session the tongue becomes visible a median 56 to 271 ms after the go cue
#   and is visible in at most 18% of the frames of the 0.5 s before it, and lick direction is decoded
#   from spike counts after the go cue above the shuffled labels (0.63 to 0.97 at +0.8 s, shuffled 0.48
#   to 0.61), so the spike, video and trial clocks are consistent.""")
open('nb_src.py','w').write(s)
EOF
python3 $TMPDIR/build_nb.py
cat > entries/hasnain-2025/README.md <<'EOF'
# Hasnain, Han & Economo (2025) from dandiset 000363

Tests the findings of [Hasnain, Han and Economo (2025)](https://doi.org/10.1101/2025.10.17.682917)
that can be tested on [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the
Mesoscale Activity Map recordings (Chen et al. 2024) that the paper reuses for its Figure 4. The
paper's own cell-type-specific recordings (Figures 1 to 3) are not public.

| Claim | Outcome |
|---|---|
| The paper's selection gives 20 bilateral ALM and 16 (or 11) ALM and medulla sessions | Not reproduced |
| Medullary units are selective, most in the response epoch (7, 21, 49%) | Partially reproduced |
| In ALM, null and potent subspaces explain comparable variance | Partially reproduced |
| In the medulla, the null subspace explains less variance than the potent | Reproduced, resting on one reading |
| ALM predicts medullary null activity nearly as well as the other ALM | Not reproduced |
| Medulla predicts ALM less well than ALM predicts the medulla | Not reproduced |
| The medullary null subspace has lower dimensionality than ALM's | Not reproduced |
| Medullary units do not span ALM's null activity patterns (UMAP) | Partially reproduced |
| Eleven claims on the paper's own recordings | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

With the dataset's CCF labels, which only units classified good carry, the paper's selection gives 5
ALM and medulla sessions, not 16 or 11, so the Figure 4 tests run on fewer sessions and units than
the paper's. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/hasnain-2025-01.yaml`](../../attempts/hasnain-2025-01.yaml).

- `reproduce_hasnain_2025.ipynb`: the analysis. It takes about 35 minutes, most of it streaming the
  units tables of all 174 files and fitting subspaces.
- `map_subspace.py`: loading, firing rates, movement masks, subspace identification, dimensionality,
  variance explained, cross-region decoding and selectivity, with where each parameter comes from.
  Other notebooks on this dandiset can import it.
EOF
cd  && sed -i 's/  runtime_minutes: 30/  runtime_minutes: 35/' entries/hasnain-2025/entry.yaml && python3 tools/entry.py check entries/hasnain-2025 2>&1 | tail -15; date -u
```

```
39
0 error(s)
Sun Nov 22 03:56:47 UTC 2026
```

**Agent**

Check passes. Final run with the corrected summary text.

**Agent calls Bash**

```bash
date -u && python3 tools/entry.py all entries/hasnain-2025 2>&1 | tail -4; date -u
```

```
Sun Nov 22 03:56:51 UTC 2026
Installed kernelspec registry-hasnain-2025 in executed/hasnain-2025/.venv/share/jupyter/kernels/registry-hasnain-2025
0 error(s)
pass  reproduce_hasnain_2025.ipynb  (2081 s)
Sun Nov 22 04:31:47 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/out3.txt
import nbformat
nb=nbformat.read('executed/hasnain-2025/reproduce_hasnain_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='stream': print(o.text)
        elif 'data' in o and 'text/plain' in o.data and 'image/png' not in o.data: print(o.data['text/plain'])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
grep -v "Warning\|warn(\|model.fit\|tqdm" $TMPDIR/out3.txt | sed 's/elapsed [0-9]* s//; s/peak memory [0-9]* MB//' > $TMPDIR/c.txt
diff $TMPDIR/b.txt $TMPDIR/c.txt | head; grep -c ERROR $TMPDIR/out3.txt; python3 tools/entry.py handover entries/hasnain-2025 2>&1 | tail -3; ls executed/hasnain-2025/handover; git status --short | head
```

```
5c5
< sessions per probe target: {'left Striatum': 54, 'right Striatum': 57, 'right ALM': 103, 'left ALM': 108, 'right Midbrain': 68, 'right Thalamus': 36, 'left Thalamus': 45, 'left Midbrain': 68, 'right Medulla': 24, 'left Medulla': 23, 'left ECT': 18, 'right ECT': 14, 'right BLA': 8, 'left BLA': 9}
---
> sessions per probe target: {'right ALM': 103, 'left ALM': 108, 'left Striatum': 54, 'right Striatum': 57, 'right Midbrain': 68, 'right Thalamus': 36, 'left Midbrain': 68, 'left Thalamus': 45, 'right Medulla': 24, 'left Medulla': 23, 'left ECT': 18, 'right ECT': 14, 'right BLA': 8, 'left BLA': 9}
0
wrote executed/hasnain-2025/handover
hasnain-2025.yaml
map_subspace.py
reproduce_hasnain_2025.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
```

**Agent calls Bash**

```bash
git status --short | grep -v "^?? \.\(bash\|git\|idea\|mcp\|profile\|ripgrep\|vscode\|zprofile\|zshrc\)"; git check-ignore executed && echo executed-ignored; date -u
```

```
?? attempts/hasnain-2025-01.yaml
?? entries/hasnain-2025/
?? scripts
executed
executed-ignored
Sun Nov 22 04:32:15 UTC 2026
```

**Agent calls Bash**

```bash
ls -a entries/hasnain-2025; git status --short scripts | head -3; ls scripts | head
```

```
.
..
.claude
README.md
__pycache__
entry.yaml
map_subspace.py
reproduce_hasnain_2025.ipynb
requirements.in
requirements.lock.txt
?? scripts
scripts
```

**Agent calls Bash**

```bash
ls -la entries/hasnain-2025/.claude scripts; git check-ignore -v entries/hasnain-2025/__pycache__ entries/hasnain-2025/.claude
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 22 02:01 scripts

entries/hasnain-2025/.claude:
total 12
drwxr-xr-x 3 runner runner 4096 Nov 22 02:21 .
drwxr-xr-x 4 runner runner 4096 Nov 22 03:56 ..
drwx------ 2 runner runner 4096 Nov 22 02:21 .cc-writes
.gitignore:1:__pycache__/	entries/hasnain-2025/__pycache__
```

**Agent calls Bash**

```bash
find entries/hasnain-2025/.claude | head; git status --short --untracked-files=all entries/hasnain-2025
```

```
entries/hasnain-2025/.claude
entries/hasnain-2025/.claude/.cc-writes
?? entries/hasnain-2025/README.md
?? entries/hasnain-2025/entry.yaml
?? entries/hasnain-2025/map_subspace.py
?? entries/hasnain-2025/reproduce_hasnain_2025.ipynb
?? entries/hasnain-2025/requirements.in
?? entries/hasnain-2025/requirements.lock.txt
```

**Agent**

I've completed steps 1 to 5 of the Author section and built the handover package (step 6). Of the 19 claims, 11 are blocked because the paper's own recordings are not public. Of the 8 tested on the MAP data, 1 is reproduced (resting on one reading of an open method detail), 3 are partially reproduced and 4 are not reproduced. The entry is locked, `check` passes with 0 errors and the notebook ran cleanly from a fresh environment. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| own-recordings-cohort, fig1i, fig2c, fig2e, fig2f, fig2gh, ed2f, fig3c, fig3d, ed3, ed3a (11 claims) | Blocked: data_missing |
| map-session-selection | Not reproduced |
| fig4b-medulla-selectivity | Partially reproduced (assumed) |
| fig4c-alm-null-potent-similar | Partially reproduced (assumed) |
| fig4c-medulla-null-smaller | Reproduced (assumed: only under readings B2 and V2) |
| fig4d-alm-predicts-medulla-null | Not reproduced (assumed) |
| fig4d-decoding-asymmetry | Not reproduced (assumed) |
| fig4e-medulla-null-lower-dimension | Not reproduced (assumed) |
| fig4f-medulla-null-not-spanning-alm | Partially reproduced (assumed) |

No outcome changes across the five seeds.

**2. What was found**

- **Version:** I pinned 0.231012.2129, the latest published version, because the paper cites the dandiset without a version. The units of the session I compared are identical in 0.230822.0128.
- **Session selection:** only units classified `good` carry a brain-region label (`anno_name`): 69,453 of 272,227. With these labels the paper's rule gives:
  - 17 bilateral ALM sessions from 9 mice; the paper has 20 from 10.
  - 5 ALM and medulla sessions from 4 mice, with 300 ALM and 340 medulla units; the paper has 16 or 11 sessions, with 604 and 724 units.

  I recorded this as a major finding about the data.
- **Labels:** 1,852 units have no `classification`. `unit_quality` has no description, and the tracking data are stored as 'a.u.' but hold pixel positions.
- **Clocks:** spikes, video and trial times agree in all 22 sessions.
- **Decoding:** the method as written (ridge, lambda 0.01, 9 lagged smoothed bins) gives held-out R2 far below zero, because the lagged predictors are nearly collinear (condition number about 1e6). Larger penalties are shown only as variants.
- **Medulla selectivity:** far higher than the paper's (34, 53 and 87% against 7, 21 and 49%).

Assumptions, recorded as deviations:
- Ignore, photostimulation and early-lick trials are left out.
- The movement threshold is Otsu's threshold on log speed, since the paper set it by hand.
- Keypoints are smoothed over 3 frames before taking speed; unsmoothed, the tracking jitter hides movement.
- The dimensionality shuffle uses 100 shuffles on every 4th bin, where the paper uses 1000, to fit the time limit.

Questions for the paper's authors, recorded as `methods_unavailable` findings:
- How R2 and the lambda were computed for the cross-region decoding.
- How the movement threshold was set, and whether movement runs shorter than 100 ms count as moving.
- Which trials were used, and which 'good' label selects units.
- How variance explained is normalized, and which dimensionality measure Figure 4e uses.
- How the z-score handles units that are nearly silent at baseline (values reach 213 s.d.).

I also recorded a `paper_inconsistency`: 16 against 11 sessions, 1116 against 2016 units, and 40 against 45 ms.

I asked no reader questions. DANDI:001472 holds the data of the authors' earlier paper, not this one, so the paper does not need listing on it.

**3. Where the protocol was unclear**

1. The claims file's readings multiply into dozens of combinations. I ran each reading against the main one, one factor at a time, and recorded that.
2. Whether a "variant" named in the claims file can decide an outcome. The example.m z-score fully matches fig4c-ALM; I did not let it decide.
3. A criterion where neither the "reproduced" nor the "not reproduced" branch applies (fig4c-ALM: p ≥ 0.05 but the means are off). I chose partially reproduced.
4. Reader step 3 says "reproduced under any reading", while author step 1.6 says to adopt the best-supported reading. For fig4c-medulla I followed the criterion and set `assumed: true`.
5. Per-claim seeds when several claims share one computation (the subspace fits). I used fig4c-ALM's seed for the shared generator.
6. Seed checks for every reading multiply the runtime. I ran them for the main reading and the deciding reading (B2) only.
7. `assumed` when an assumption, such as the trial exclusions, applies to every claim. I marked all tested Figure 4 outcomes except the session selection.
8. During the survey I tried to check the electrode coordinates against the Allen atlas outside the notebook. I dropped it and nothing from it is in the record, as the protocol requires.

**4. Runtime and failures**

The run took about 2.5 hours (02:02 to 04:33 UTC). The notebook takes 35 minutes, which is under the 60-minute limit but over the 10-minute aim; peak memory was about 3.8 GB. Nothing failed in the final run.

Files are in `entries/hasnain-2025/`:
- `reproduce_hasnain_2025.ipynb`
- `map_subspace.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

The handover is in `executed/hasnain-2025/handover/` and the record is `attempts/hasnain-2025-01.yaml`.

## End of run

82 turns, 148 minutes, $7.73 at API prices, result: success.
