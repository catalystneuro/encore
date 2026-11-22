# kim-2025 · author · run 44962565814

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (64.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0e385112-f3b8-402b-9c7f-ae271ffb0715/tool-results/bwsfody5a.txt

Preview (first 2KB):
Sat Nov 21 23:41:57 UTC 2026
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0e385112-f3b8-402b-9c7f-ae271ffb0715/tool-results/bwsfody5a.txt"
}
```

```
1	Sat Nov 21 23:41:57 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-18`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 1440 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper entries/fouke-2025; cat claims/kim-2025.yaml; cat papers/datasets/kim-2025.yaml
```

```
<persisted-output>
Output too large (46KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0e385112-f3b8-402b-9c7f-ae271ffb0715/tool-results/b1dy8re0u.txt

Preview (first 2KB):
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.1101-2025.06.30.662469.txt
# Claims for Kim & Shin (2025), doi:10.1101/2025.06.30.662469, read for dandiset 000248.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: paper/10.1101-2025.06.30.662469.txt, the bioRxiv full text of the preprint posted
# July 04, 2025, under the title "Neural variability structure in primary visual cortex is optimal
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0e385112-f3b8-402b-9c7f-ae271ffb0715/tool-results/b1dy8re0u.txt"
}
```

```
1	entries/fouke-2025:
2	README.md
3	entry.yaml
4	omr.py
5	reproduce_fouke_2025.ipynb
6	requirements.in
7	requirements.lock.txt
8	
9	paper:
10	10.1101-2025.06.30.662469.txt
11	# Claims for Kim & Shin (2025), doi:10.1101/2025.06.30.662469, read for dandiset 000248.
12	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
13	# protocol as stated in docs/protocol.md (Reader).
14	#
15	# Text read: paper/10.1101-2025.06.30.662469.txt, the bioRxiv full text of the preprint posted
16	# July 04, 2025, under the title "Neural variability structure in primary visual cortex is optimal
17	# for robust representation of visual similarity". The registry lists the paper under a later
18	# title ("Intrinsic geometry of trial-to-trial variability in primary visual cortex is optimal for
19	# robust representation of visual similarity"); that later version was not supplied, and every
20	# claim here is from the July 2025 text. That text holds the Results, Discussion, Methods and the
[... 688 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -150; wc -l README.md docs/design.md
```

```
## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
  paper cites, or the latest published one. For a draft, record its
  modification time under `dataset: modified` in the attempt.
- **Reading.** List the assets and read metadata with the DANDI REST API
  (`https://api.dandiarchive.org/api/dandisets/<id>/versions/<version>/` and its
  `assets/` endpoint). Read NWB files by streaming them: open each asset's S3
  URL with `remfile` and `h5py`, and read it with `pynwb`. Do not download files
  to disk.
- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
  `related`. The helper module keeps the version in one constant.

## CRCNS
  139 README.md
  286 docs/design.md
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -60 entries/fouke-2025/omr.py
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
[... 149 more lines not kept]
```

**Agent**

Now the attempt format and the dataset.

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150; python -c "import pynwb, remfile, h5py, dandi; print('ok')"
```

```
Exit code 1
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
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/fouke-2025-01.yaml | grep -n -A30 "^findings\|^verifications" | head -60; cat tools/entry.py | grep -n "def \|python_version\|PYTHON" | head -40
```

```
95:findings:
96-- kind: data_missing
97-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
98-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
99-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
100-    notebooks only. Nine of the paper's main findings cannot be tested.
101-- kind: metadata_insufficient
102-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
103-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
104-    file of its stimulus software.
105-- kind: code_mismatch
106-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
107-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
108-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
109-    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
110-    only if the fish turn with lateral motion.
111-- kind: metadata_error
112-  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
113-    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
114-    only Danio rerio; the files hold 37 fish of two species.
[... 72 more lines not kept]
```

**Agent**

Set up a scratch environment and survey dandiset 000248.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 kenv && . kenv/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas scikit-learn networkx matplotlib 2>&1 | tail -2; python -c "import pynwb; print(pynwb.__version__)"
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000248/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000248/versions/" | python -m json.tool | grep -E '"version"|"created"|"status"|"asset_count"|"size"'
```

```
4.2.0
Shell cwd was reset to
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000248/versions/0.240502.2344/assets/?page_size=200" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['path'], round(a['size']/1e9,2), a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, pynwb, time, sys
from dandi.dandiapi import DandiAPIClient
t=time.time()
c=DandiAPIClient(); ds=c.get_dandiset("000248","0.240502.2344")
a=ds.get_asset_by_path(sys.argv[1])
url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name, obj.shape, obj.dtype)
f.visititems(show)
print(time.time()-t)
EOF
python survey.py sub-630506/sub-630506_ses-1192952695_ogen.nwb 2>&1 | grep -v "^acquisition/.*/data\b" | head -300
```

```
acquisition/EyeTracking/corneal_reflection_tracking/angle (538426,) float64
acquisition/EyeTracking/corneal_reflection_tracking/area (538426,) float64
acquisition/EyeTracking/corneal_reflection_tracking/area_raw (538426,) float64
acquisition/EyeTracking/corneal_reflection_tracking/height (538426,) float64
acquisition/EyeTracking/corneal_reflection_tracking/reference_frame () object
acquisition/EyeTracking/corneal_reflection_tracking/width (538426,) float64
acquisition/EyeTracking/eye_tracking/angle (538426,) float64
acquisition/EyeTracking/eye_tracking/area (538426,) float64
acquisition/EyeTracking/eye_tracking/area_raw (538426,) float64
acquisition/EyeTracking/eye_tracking/height (538426,) float64
acquisition/EyeTracking/eye_tracking/reference_frame () object
acquisition/EyeTracking/eye_tracking/timestamps (538426,) float64
acquisition/EyeTracking/eye_tracking/width (538426,) float64
acquisition/EyeTracking/pupil_tracking/angle (538426,) float64
acquisition/EyeTracking/pupil_tracking/area (538426,) float64
acquisition/EyeTracking/pupil_tracking/area_raw (538426,) float64
acquisition/EyeTracking/pupil_tracking/height (538426,) float64
acquisition/EyeTracking/pupil_tracking/reference_frame () object
acquisition/EyeTracking/pupil_tracking/width (538426,) float64
acquisition/raw_running_wheel_rotation/timestamps (435300,) float64
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python survey.py sub-630506/sub-630506_ses-1192952695_ogen.nwb 2>&1 | grep -E "^units|^stimulus/templates/ICwcfg1|^general/extracellular_ephys/probe|^intervals/[a-z]" | grep -v templates | head -80
```

```
intervals/invalid_times/id (1,) int64
intervals/invalid_times/start_time (1,) float64
intervals/invalid_times/stop_time (1,) float64
intervals/invalid_times/tags (3,) object
intervals/invalid_times/tags_index (1,) uint8
intervals/sizeCI_presentations/Mask (960,) object
intervals/sizeCI_presentations/color (960,) object
intervals/sizeCI_presentations/contrast (960,) float64
intervals/sizeCI_presentations/id (960,) int64
intervals/sizeCI_presentations/opacity (960,) float64
intervals/sizeCI_presentations/orientation (960,) float64
intervals/sizeCI_presentations/phase (960,) object
intervals/sizeCI_presentations/size (960,) object
intervals/sizeCI_presentations/spatial_frequency (960,) object
intervals/sizeCI_presentations/start_time (960,) float64
intervals/sizeCI_presentations/stimulus_block (960,) float64
intervals/sizeCI_presentations/stimulus_index (960,) float64
intervals/sizeCI_presentations/stimulus_name (960,) object
intervals/sizeCI_presentations/stop_time (960,) float64
intervals/sizeCI_presentations/tags (960,) object
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > s2.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd, time, collections
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); ds=c.get_dandiset("000248","0.240502.2344")
a=ds.get_asset_by_path("sub-630506/sub-630506_ses-1192952695_ogen.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),'r')
g=f['intervals/ICwcfg1_presentations']
df=pd.DataFrame({k:g[k][:] for k in ['frame','start_time','stop_time','stimulus_block','stimulus_index']})
df['name']=[x.decode() if isinstance(x,bytes) else x for x in g['stimulus_name'][:]]
print(df.head(10)); print(df.name.value_counts().head())
print(df.groupby('stimulus_block').size())
print(df.frame.value_counts().sort_index())
print((df.stop_time-df.start_time).describe())
print(np.diff(df.start_time.values)[:20])
print(g.attrs.get('description'))
for k in ['session_description','general/stimulus','general/session_id']: print(k, f[k][()])
e=f['general/extracellular_ephys/electrodes']
loc=np.array([x.decode() for x in e['location'][:]])
print(collections.Counter(loc))
print(f['units/quality'][:10], collections.Counter(f['units/quality'][:]))
print([ (k, f['units'][k].attrs.get('description')) for k in ['quality','firing_rate','isi_violations']])
EOF
python s2.py
```

```
frame  start_time  stop_time  stimulus_block  stimulus_index     name
0    0.0    62.94815   63.34845             0.0             0.0  ICwcfg1
1    0.0    63.34845   63.74881             0.0             0.0  ICwcfg1
2    0.0    63.74881   64.14913             0.0             0.0  ICwcfg1
3    0.0    64.14913   64.54947             0.0             0.0  ICwcfg1
4    0.0    64.54947   64.94978             0.0             0.0  ICwcfg1
5    0.0    64.94978   65.35015             0.0             0.0  ICwcfg1
6    0.0    65.35015   65.75051             0.0             0.0  ICwcfg1
7    0.0    65.75051   66.15082             0.0             0.0  ICwcfg1
8    0.0    66.15082   66.55116             0.0             0.0  ICwcfg1
9    0.0    66.55116   66.95150             0.0             0.0  ICwcfg1
name
ICwcfg1    10720
Name: count, dtype: int64
stimulus_block
0.0    10720
dtype: int64
frame
0.0     5820
1.0      400
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i "illusion\|openscope\|000248\|400 ms\|Isomap\|orthogonal variance" *.txt | head -60
```

```
729 10.1101-2025.06.30.662469.txt
50:(C) Log-mean vs. log-variance slope manipulation and dimensionality reduction of 3 example stimulus manifolds. Top: Log-mean vs. log-variance scatterplots of an example session and a stimulus are shown (250ms presentations, 50 repeats). The black dots (each corresponding to a single neuron) are the as-is data (no slope manipulation) and the black line is the line fit by linear regression of the black dots (same across all four plots). The orange dots and lines show slope-changed data, where only the variance was manipulated. Bottom: Isomap embedding of 3 example stimulus manifolds is shown (400ms presentations, 400 repeats). Each of the 3 colors is one stimulus manifold in an example session, and each dot corresponds to a trial.
110:To visualize the neural state space, we applied a nonlinear dimensionality reduction method called Isomap29, which aims to preserve the geodesic distances in the lower dimension (Figure 1C bottom). As the slope increases from 0 to 2, the stimulus manifolds become increasingly overlapping. At slope 0, the stimulus manifolds appear discontinuous with one another, hindering smooth transitions between stimuli. At slope 2, the stimulus manifolds are hard to discriminate due to the large overlap. The stimulus manifolds appear to strike a balance when slope is near 1, such that they are continuous with minimal overlap in the original ‘as-is’ data.
118:(A) Histogram of slopes for linear regression fits to log-mean vs. log-variance of spike counts across V1 neurons in the natural movie data. Mean and variance of spike counts are calculated for each time bin; 75 time bins corresponding to 400 ms windows for ‘natural movie one’ in 23 sessions are pooled from the Allen Brain Visual Coding Neuropixels dataset.
120:(B) Dimensionality reduction of V1 manifold for a natural movie. UMAP embedding of spike count vectors in 400 ms bins of ‘natural movie one’ is plotted for an example session. Each dot corresponds to a t
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/jhk4839/Neural_variability_robustness/contents?ref=ac3300b007c2348ccda73c0c87fb02f557791089; curl -s "https://api.github.com/repos/jhk4839/Neural_variability_robustness/contents?ref=ac3300b007c2348ccda73c0c87fb02f557791089" | python -c "import json,sys; [print(x['name'],x['size']) for x in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p code && cd code && for f in fit_slope_openscope.ipynb visualize_manifold.ipynb box_and_overlap.py compute_geo_ortho.py ortho_variance.ipynb dimensionality_tangent.ipynb local_global_alignment.py; do curl -sL -o $f https://raw.githubusercontent.com/jhk4839/Neural_variability_robustness/ac3300b007c2348ccda73c0c87fb02f557791089/$f; done; ls -la; python3 -c "
import json
nb=json.load(open('fit_slope_openscope.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code': print('----',i); print(''.join(c['source'])[:3000])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > s3.py <<'EOF'
import h5py, remfile, numpy as np, collections
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); ds=c.get_dandiset("000248","0.240502.2344")
a=ds.get_asset_by_path("sub-630506/sub-630506_ses-1192952695_ogen.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),'r')
g=f['intervals/ICwcfg1_presentations']
fr=g['frame'][:].astype(int); st=g['start_time'][:]
print(fr[:60])
# run lengths of zeros
runs=[];i=0
while i<len(fr):
    if fr[i]==0:
        j=i
        while j<len(fr) and fr[j]==0: j+=1
        runs.append((j-i,i)); i=j
    else: i+=1
print(collections.Counter(r for r,_ in runs))
print([r for r in runs if r[0]>3][:10])
print(np.unique(np.diff(st).round(2),return_counts=True))
EOF
python s3.py
```

```
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
Counter({1: 4535, 3: 335, 5: 23, 7: 5, 60: 1, 9: 1, 61: 1})
[(60, 0), (5, 1341), (5, 1373), (5, 1405), (5, 1451), (5, 1615), (7, 2525), (5, 2777), (5, 2933), (5, 3015)]
(array([0.4]), array([10719]))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > s4.py <<'EOF'
import h5py, remfile, numpy as np, collections
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); ds=c.get_dandiset("000248","0.240502.2344")
assets=[a for a in ds.get_assets() if a.path.endswith('ogen.nwb')]
def one(a):
    f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),'r')
    out=[a.path]
    out.append('ICwcfg1' if 'ICwcfg1_presentations' in f['intervals'] else 'noICwcfg1')
    if 'units' in f:
        loc=np.array([x.decode() for x in f['general/extracellular_ephys/electrodes/location'][:]])
        eid=f['general/extracellular_ephys/electrodes/id'][:]
        m=dict(zip(eid,loc))
        pk=f['units/peak_channel_id'][:]
        ul=np.array([m[p] for p in pk])
        v1=np.array([('VISp' in l) and ('VISpm' not in l) for l in ul])
        q=(f['units/isi_violations'][:]<0.5)&(f['units/amplitude_cutoff'][:]<0.1)&(f['units/presence_ratio'][:]>0.9)
        out += [len(pk), int(v1.sum()), int((v1&q).sum())]
        if 'ICwcfg1_presentations' in f['intervals']:
            fr=f['intervals/ICwcfg1_presentations/frame'][:].astype(int)
            out.append(dict(collections.Counter(fr)).get(1))
            out.append(len(fr))
    else: out.append('nounits')
    return out
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(one, assets): print(r)
EOF
python s4.py; curl -s https://api.dandiarchive.org/api/dandisets/000021/ | python -c "import json,sys; d=json.load(sys.stdin); print(d['most_recent_published_version']['version'], d['most_recent_published_version']['name'], d['most_recent_published_version']['asset_count'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000021/versions/" | python -c "import json,sys; [print(v['version'],v['created'][:10],v['asset_count']) for v in json.load(sys.stdin)['results']]"; curl -s "https://api.dandiarchive.org/api/dandisets/000021/versions/0.251116.2246/assets/?page_size=400" | python -c "
import json,sys; d=json.load(sys.stdin)
s=[a for a in d['results'] if 'probe' not in a['path']]
print(len(d['results']), len(s)); [print(a['path'], round(a['size']/1e9,2)) for a in s[:50]]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "def \|percentile\|cdist\|<=\|polyfit\|log10\|sqrt" box_and_overlap.py | head -80
```

```
21:from scipy.spatial.distance import cdist
47:def compute_mean_var_trial(label_cnt_dict, rate_sorted):    
68:def compute_mean_var_trial_collapse(label_cnt_dict, rate_sorted):    
89:def compute_percent_filled(point_cloud, point_cloud_cri, min_box_size, max_box_size, num_box_sizes=1):
110:    bool_withinrange = np.all((point_cloud >= axis_ranges[:, 0].reshape(-1, 1)) & (point_cloud <= axis_ranges[:, 1].reshape(-1, 1)), axis=0)
114:    box_sizes = np.logspace(np.log10(min_box_size), np.log10(max_box_size), num=num_box_sizes, endpoint=True, base=10)
134:    log_box_sizes = np.log10(box_sizes)
140:def compute_filling_boxcount(slope_ind, target_slope):
198:            offset = pow(10, (list_slopes_dr.iloc[0, :]-target_slope) * np.nanmean(np.log10(rate_sorted_mean_coll), axis=0) + list_slopes_dr.iloc[1, :]) 
201:                pow(10, np.log10(rate_sorted_var_coll).sub(list_slopes_dr.iloc[1, :], axis=1)\
202:                    .div(list_slopes_dr.iloc[0, :], axis=1).mul(target_slope).add(np.log10(np.array(offset)), axis=1)) # collapsed
207:            # rate_resid_RRneuron_dr = rate_sorted_resid_dr.div(np.sqrt(rate_sorted_var))\
208:            #     .mul(np.sqrt(rate_sorted_mean)).mul(np.sqrt(FF_estim_dr), axis=1)
209:            rate_resid_RRneuron_dr = rate_sorted_resid_dr.div(np.sqrt(rate_sorted_var))\
210:                .mul(np.sqrt(var_rs_noisy))
234:def compute_overlap_stimpairs_consis(sess_ind):
284:            pwdist_tt1 = cdist(rate_sorted.loc[neu_div_inds1, trial_type].T, rate_sorted.loc[neu_div_inds1, trial_type].T, 'euclidean')
285:            pwdist_tt2 = cdist(rate_sorted.loc[neu_div_inds2, trial_type].T, rate_sorted.loc[neu_div_inds2, trial_type].T, 'euclidean')
286:            list_pwdist[0, trial_type_ind, 0] = np.percentile(pwdist_tt1, 5)
288:            list_pwdist[1, trial_type_ind, 0] = np.percentile(pwdist_tt2, 5)
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 400,540p box_and_overlap.py
```

```
def compute_overlap_stimpairs(sess_ind):

    c_proc = mp.current_process()
    print("Running on Process", c_proc.name, "PID", c_proc.pid)

    list_target_slopes = np.linspace(0, 2, 21, endpoint=True)
    num_trial_types = 119

    print(f'sess_ind: {sess_ind}')
    
    rate_sorted = list_rate_all[sess_ind].sort_index(axis=1)
    stm = rate_sorted.columns.copy()
    num_neurons = rate_sorted.shape[0]

    # Multiply by delta t to convert to spike counts
    rate_sorted = rate_sorted * 0.25 

    # Create a counting dictionary for each stimulus
    all_stm_unique, all_stm_counts = np.unique(stm, return_counts=True) 
    stm_cnt_dict = dict(zip(all_stm_unique, all_stm_counts))
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "ortho\|norm\|var(\|dot\|Isomap\|dist_matrix" compute_geo_ortho.py | head -40; python3 -c "
import json
nb=json.load(open('visualize_manifold.ipynb'))
c=nb['cells'][8]; print(''.join(c['source'])[:5000])"
```

```
15:from scipy.stats import wilcoxon, norm, kruskal, tukey_hsd, mode, sem
30:from sklearn.manifold import Isomap
31:from sklearn.preprocessing import normalize as normr
50:        trial_var = np.var(trial_rate, axis=1, ddof=1, dtype=np.longdouble)
71:        trial_var = np.var(trial_rate, axis=1, ddof=1, dtype=np.longdouble)
88:    # dot_xy = np.dot(x, y)
89:    # norm_x, norm_y = np.linalg.norm(x), np.linalg.norm(y)
91:    # cos_sim = np.dot(normr(np.squeeze(np.squeeze(x).reshape(1, -1))), \
92:    #                  normr(np.squeeze(np.squeeze(y).reshape(1, -1))))
94:    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
97:# Function to compute orthogonal & parallel distance
101:    mat_orth1 = np.array(mat1.apply(lambda x : np.dot(x, mean_vector), axis=0).div(np.dot(mean_vector, mean_vector)))[:, np.newaxis].T * np.array(mean_vector)[:, np.newaxis]
107:# ABO Neuropixels mean similarity vs. orthogonal variance (RRneuron) (all neurons)
109:def compute_meansim_orthopar_ABO_RRneuron(slope_ind, target_slope, adjacency_type='geodesic'):
122:    list_orthopar2_ABO_one_tt = np.zeros((num_sess, num_trial_types, num_trial_types-1, 2)) # ortho, par
195:        isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)
198:        mean_dist_mat_RRneuron = isomap.dist_matrix_[rate_RRneuron_dr.shape[1]:, rate_RRneuron_dr.shape[1]:].copy() # inter-centroid geodesic distance matrix
202:        list_orthopar_one_tt = np.zeros((num_trial_types, num_trial_types-1, 2))
212:            # compute orthogonal variance against partner stimulus manifold
219:                list_orthopar_one_tt[trial_type_ind, partner_ind] = [np.var(np.linalg.norm(mat_orth, axis=0), ddof=1), \
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 95,106p compute_geo_ortho.py; sed -n 200,226p compute_geo_ortho.py
```

```
# %%
# Function to compute orthogonal & parallel distance
def compute_orth_par_dist(manifold_name1, manifold_name2, rate_12, rate_sorted_mean_coll):
    mean_vector = rate_sorted_mean_coll.loc[:, manifold_name2] - rate_sorted_mean_coll.loc[:, manifold_name1] # mean vector
    mat1 = rate_12.loc[:, manifold_name1].sub(rate_sorted_mean_coll.loc[:, manifold_name1], axis=0) # trial vector
    mat_orth1 = np.array(mat1.apply(lambda x : np.dot(x, mean_vector), axis=0).div(np.dot(mean_vector, mean_vector)))[:, np.newaxis].T * np.array(mean_vector)[:, np.newaxis]
    mat_par1 = mat_orth1 - mat1

    return mat_orth1, mat_par1

# %%
        # Iterate over all stimuli (~25 min)
        list_mean_sim_one_tt = np.zeros((num_trial_types, num_trial_types-1))
        list_orthopar_one_tt = np.zeros((num_trial_types, num_trial_types-1, 2))
        list_tot_var_one_tt = np.zeros((num_trial_types, num_trial_types-1, 2))
        for trial_type_ind, trial_type in enumerate(rate_sorted_mean_coll.columns):
            print(f'trial type ind {trial_type_ind}')

            bool_not_tt = rate_sorted_mean_coll.columns != trial_type

[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > s5.py <<'EOF'
import h5py, remfile, numpy as np, time, resource
from dandi.dandiapi import DandiAPIClient
t=time.time()
c=DandiAPIClient(); ds=c.get_dandiset("000248","0.240502.2344")
a=ds.get_asset_by_path("sub-625555/sub-625555_ses-1183070926_ogen.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),'r')
loc=np.array([x.decode() for x in f['general/extracellular_ephys/electrodes/location'][:]])
m=dict(zip(f['general/extracellular_ephys/electrodes/id'][:],loc))
ul=np.array([m[p] for p in f['units/peak_channel_id'][:]])
v1=np.where([('VISp' in l) and ('VISpm' not in l) for l in ul])[0]
idx=f['units/spike_times_index'][:]
print(len(v1), v1[:10], v1[-10:], f['units/spike_times'].chunks)
starts=np.r_[0,idx][v1]; ends=idx[v1]
print('total spikes', (ends-starts).sum())
t1=time.time()
st=f['units/spike_times']
lo,hi=starts.min(),ends.max()
print('span', hi-lo)
tot=0
for s,e in zip(starts,ends):
    x=st[s:e]; tot+=len(x)
print(time.time()-t1, tot, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
python s5.py
```

```
364 [1028 1029 1030 1031 1032 1033 1034 1035 1036 1037] [1395 1396 1397 1398 1399 1400 1401 1402 1403 1404] None
total spikes 10747004
span 11028214
2.7260842323303223 10747004 0.28882
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > s6.py <<'EOF'
import h5py, remfile, numpy as np, collections, time
from dandi.dandiapi import DandiAPIClient
t=time.time()
c=DandiAPIClient(); ds=c.get_dandiset("000021","0.251116.2246")
a=ds.get_asset_by_path("sub-699733573/sub-699733573_ses-715093703.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),'r')
print(list(f['intervals'].keys()))
print(list(f['units'].keys()))
print(list(f['processing'].keys()), list(f['acquisition'].keys()))
for k in f['processing']: print(k, list(f['processing'][k].keys()))
g=f['intervals/natural_scenes_presentations']; print(list(g.keys()))
fr=g['frame'][:]; print(len(fr), collections.Counter(fr).most_common(3), min(fr), max(fr))
st=g['start_time'][:]; sp=g['stop_time'][:]; print(np.median(sp-st), np.unique(np.diff(st).round(2),return_counts=True))
print(len(f['units/id']), f['units/spike_times'].shape)
loc=np.array([x.decode() for x in f['general/extracellular_ephys/electrodes/location'][:]])
print(collections.Counter(loc).most_common(40))
print(time.time()-t)
EOF
python s6.py
```

```
['drifting_gratings_presentations', 'flashes_presentations', 'gabors_presentations', 'invalid_times', 'natural_movie_one_presentations', 'natural_movie_three_presentations', 'natural_scenes_presentations', 'spontaneous_presentations', 'static_gratings_presentations']
['PT_ratio', 'amplitude', 'amplitude_cutoff', 'cluster_id', 'cumulative_drift', 'd_prime', 'firing_rate', 'id', 'isi_violations', 'isolation_distance', 'l_ratio', 'local_index', 'max_drift', 'nn_hit_rate', 'nn_miss_rate', 'peak_channel_id', 'presence_ratio', 'quality', 'recovery_slope', 'repolarization_slope', 'silhouette_score', 'snr', 'spike_amplitudes', 'spike_amplitudes_index', 'spike_times', 'spike_times_index', 'spread', 'velocity_above', 'velocity_below', 'waveform_duration', 'waveform_halfwidth', 'waveform_mean', 'waveform_mean_index']
['eye_tracking_rig_metadata', 'optotagging', 'running', 'stimulus'] ['raw_running_wheel_rotation', 'running_wheel_signal_voltage', 'running_wheel_supply_voltage']
eye_tracking_rig_metadata ['eye_tracking_rig_metadata']
optotagging ['optogenetic_stimulation', 'optotagging']
running ['running_speed', 'running_speed_end_times', 'running_wheel_rotation']
stimulus ['timestamps']
['frame', 'id', 'start_time', 'stimulus_block', 'stimulus_index', 'stimulus_name', 'stop_time', 'tags', 'tags_index', 'timeseries', 'timeseries_index']
5950 [(np.float64(5.0), 50), (np.float64(114.0), 50), (np.float64(13.0), 50)] -1.0 117.0
0.2502088598721457 (array([2.5000e-01, 2.7000e-01, 3.0050e+02, 8.7098e+02]), array([5946,    1,    1,    1]))
2779 (131242535,)
[(np.str_(''), 483), (np.str_('CA1'), 383), (np.str_('grey'), 265), (np.str_('VISrl'), 174), (np.str_('DG'), 169), (np.str_('LP'), 138), (np.str_('LGd'), 122), (np.str_('APN'), 112), (np.str_('VISp'), 93), (np.str_('VISl'), 83), (np.str_('VISam'), 82), (np.str_('CA3'), 67), (np.str_('VISpm'), 65), (np.str_('PO'), 57), (np.str_('MB'), 10), (np.str_('PoT'), 1)]
3.316917896270752
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/kim-2025/kim2025.py",
 "content": "\"\"\"Loading and measures for Kim & Shin (2025), doi:10.1101/2025.06.30.662469.\n\nTwo datasets are streamed from the DANDI Archive at pinned versions; nothing is written to disk.\n\n- Dandiset 000248 (Allen Institute OpenScope Illusion project), the dataset under test. Each\n  session's `*_ogen.nwb` file holds the units table (spike times, Allen quality metrics, peak\n  channel) and the `ICwcfg1_presentations` table. That table lists every 400 ms frame of the\n  block, including the gray inter-trial frames, with the image code in `frame` (0 to 21) and no\n  name for the codes.\n- Dandiset 000021 (Allen Brain Observatory Visual Coding Neuropixels, Brain Observatory 1.1\n  sessions), the paper's main dataset (claims `data: elsewhere`). Each session file holds the\n  units table and `natural_scenes_presentations` (frame -1 is the gray image, 0 to 117 the\n  scenes).\n\nWhere the parameters come from (the claims file is claims/kim-2025.yaml; \"code\" is\ngithub.com/jhk4839/Neural_variability_robustness at commit ac3300b007c2348ccda73c0c87fb02f557791089):\n\n- V1 units of the Illusion data: peak-channel location containing \"VISp\" and not \"VISpm\"\n  (claims file, header O3 reading a, from fit_slope_openscope.ipynb cell 5). Reading b adds the\n  Allen quality criteria of the Methods (isi_violations < 0.5, amplitude_cutoff < 0.1,\n  presence_ratio > 0.9; Methods, \"Main dataset and visual stimuli\").\n- Illusion spike counts: spikes in the 400 ms from stimulus onset (Methods, \"Visualization of\n  stimulus manifold geometry\", paragraph 2). The trial slots of ICwcfg1 are recovered from the\n  alternation of trials and gray inter-trial frames (see `illusion_trials`); a gray frame in a\n  trial slot is a Blank trial. This is how the code's 12 stimuli with 400 repeats arise (its\n  trialorder comes from a post-processed copy that is not public).\n- Names of the image codes: the code's map, dict_trial_type in fit_slope_openscope.ipynb\n  cell 5 (claims file header), `ILLUSION_NAMES`.\n- Natural scenes counts: spikes in the 250 ms from onset; units in VISp passing the Allen\n  quality criteria (Methods, \"Main dataset and visual stimuli\").\n- Slope fit (M1), slope manipulation (M2), overlap (M3), geodesic distance (M5), orthogonal\n  variance, effective dimensionality: as the claims file header and criteria give them, checked\n  against box_and_overlap.py and compute_geo_ortho.py of the code.\n- Isomap uses n_neighbors 5 (code). Isomap's eigen-solver is deterministic for the dense\n  solver, which is set (`eigen_solver=\"dense\"`), a standard choice that cannot change a result\n  beyond numerical precision.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport h5py\nimport networkx as nx\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.spatial.distance import cdist\nfrom sklearn.manifold import Isomap\n\nDANDISET_ID = \"000248\"\nDANDISET_VERSION = \"0.240502.2344\"\nABO_ID = \"000021\"\nABO_VERSION = \"0.251116.2246\"\n\n# The paper code's order of the Illusion subjects; index 6 is its example session.\nCODE_SUBJECTS = [\"619296\", \"620333\", \"620334\", \"625545\", \"625554\", \"625555\", \"630506\",\n                 \"631510\", \"631570\", \"633229\", \"637484\"]\nEXAMPLE_SUBJECT = \"630506\"\n\nILLUSION_NAMES = {0: \"Blank\", 1: \"X\", 2: \"Tc1\", 3: \"Ic1\", 4: \"Lc1\", 5: \"Tc2\", 6: \"Lc2\", 7: \"Ic2\",\n                  8: \"Ire1\", 9: \"Ire2\", 10: \"Tre1\", 11: \"Tre2\", 12: \"Xre1\", 13: \"Xre2\",\n                  14: \"BR_in\", 15: \"BL_in\", 16: \"TL_in\", 17: \"TR_in\", 18: \"BR_out\",\n                  19: \"BL_out\", 20: \"TL_out\", 21: \"TR_out\"}\nILLUSION_WINDOW = 0.4\nSCENES_WINDOW = 0.25\nTARGET_SLOPES = np.round(np.linspace(0, 2, 21), 1)\nQUALITY = dict(isi_violations=0.5, amplitude_cutoff=0.1, presence_ratio=0.9)\n\n_client = None\n\n\ndef _dandiset(dandiset_id, version):\n    global _client\n    if _client is None:\n        _client = DandiAPIClient()\n    return _client.get_dandiset(dandiset_id, version)\n\n\ndef asset_paths(dandiset_id=DANDISET_ID, version=DANDISET_VERSION):\n    return sorted(a.path for a in _dandiset(dandiset_id, version).get_assets())\n\n\ndef open_nwb(path, dandiset_id=DANDISET_ID, version=DANDISET_VERSION):\n    asset = _dandiset(dandiset_id, version).get_asset_by_path(path)\n    url = asset.get_content_url(follow_redirects=1, strip_query=True)\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _str(values):\n    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])\n\n\ndef units_table(f):\n    \"\"\"Units with their peak-channel location and the Allen quality metrics.\"\"\"\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    loc = dict(zip(e[\"id\"][:], _str(e[\"location\"][:])))\n    u = f[\"units\"]\n    df = pd.DataFrame({\n        \"id\": u[\"id\"][:],\n        \"location\": [loc[p] for p in u[\"peak_channel_id\"][:]],\n        \"quality\": _str(u[\"quality\"][:]),\n        \"isi_violations\": u[\"isi_violations\"][:],\n        \"amplitude_cutoff\": u[\"amplitude_cutoff\"][:],\n        \"presence_ratio\": u[\"presence_ratio\"][:],\n        \"firing_rate\": u[\"firing_rate\"][:],\n    })\n    df[\"passes_quality\"] = ((df.isi_violations < QUALITY[\"isi_violations\"])\n                            & (df.amplitude_cutoff < QUALITY[\"amplitude_cutoff\"])\n                            & (df.presence_ratio > QUALITY[\"presence_ratio\"]))\n    return df\n\n\ndef is_v1(locations, exact=False):\n    \"\"\"VISp and not VISpm (code); with exact=True the location must be exactly 'VISp' (000021).\"\"\"\n    locs = pd.Series(locations)\n    if exact:\n        return (locs == \"VISp\").to_numpy()\n    return (locs.str.contains(\"VISp\") & ~locs.str.contains(\"VISpm\")).to_numpy()\n\n\ndef spike_counts(f, unit_rows, onsets, window):\n    \"\"\"Counts (trials x units) of spikes in [onset, onset + window) for the given unit rows.\"\"\"\n    idx = f[\"units/spike_times_index\"][:]\n    starts = np.r_[0, idx[:-1]]\n    st = f[\"units/spike_times\"]\n    onsets = np.asarray(onsets)\n    out = np.zeros((len(onsets), len(unit_rows)), dtype=np.float64)\n    for j, r in enumerate(unit_rows):\n        s = st[starts[r]:idx[r]]\n        out[:, j] = np.searchsorted(s, onsets + window, \"left\") - np.searchsorted(s, onsets, \"left\")\n    return out\n\n\ndef illusion_trials(f, block=\"ICwcfg1_presentations\"):\n    \"\"\"Trial slots of an Illusion block: (onset times, image codes, report dict).\n\n    Presentations last 400 ms with no gap. After the leading gray frames, trials and gray\n    inter-trial frames alternate, so the trial slots are every other presentation starting at\n    the first non-gray one; a gray frame (code 0) in a trial slot is a Blank trial. The report\n    says whether every non-gray frame falls in a trial slot and every slot is followed by a gray\n    frame, which checks the reading.\n    \"\"\"\n    g = f[\"intervals\"][block]\n    frame = g[\"frame\"][:].astype(int)\n    start = g[\"start_time\"][:]\n    first = int(np.argmax(frame != 0))\n    last = int(len(frame) - 1 - np.argmax(frame[::-1] != 0))\n    slots = np.arange(first, last + 1, 2)\n    off = np.setdiff1d(np.arange(first, last + 1), slots)\n    report = {\n        \"presentations\": len(frame),\n        \"leading_gray\": first,\n        \"trailing_gray\": len(frame) - 1 - last,\n        \"non_gray_outside_slots\": int((frame[off] != 0).sum()),\n        \"slots\": len(slots),\n        \"duration_range_s\": (float(np.min(g[\"stop_time\"][:] - start)),\n                             float(np.max(g[\"stop_time\"][:] - start))),\n    }\n    return start[slots], frame[slots], report\n\n\ndef illusion_session(path, quality=False):\n    \"\"\"V1 spike counts (trials x units) and image codes for the 12 stimuli with 400 repeats.\"\"\"\n    f = open_nwb(path)\n    units = units_table(f)\n    keep = is_v1(units.location)\n    if quality:\n        keep &= units.passes_quality.to_numpy()\n    rows = np.where(keep)[0]\n    onsets, codes, report = illusion_trials(f)\n    counts = spike_counts(f, rows, onsets, ILLUSION_WINDOW)\n    vals, n = np.unique(codes, return_counts=True)\n    use = np.isin(codes, vals[n == 400])\n    order = np.argsort(codes[use], kind=\"stable\")\n    X = counts[use][order]\n    labels = codes[use][order]\n    report.update(units_total=len(units), v1_units=int(is_v1(units.location).sum()),\n                  units_used=len(rows), codes_with_400=list(vals[n == 400]),\n                  counts_per_code=dict(zip(vals.tolist(), n.tolist())))\n    f.close()\n    return X, labels, report\n\n\n# ---------------------------------------------------------------- measures\n\ndef fit_slopes(X, labels):\n    \"\"\"M1: per stimulus, OLS of log10 variance (ddof 1) on log10 mean over neurons with mean > 0.\n\n    Returns a DataFrame indexed by stimulus with slope, intercept and the number of neurons.\n    \"\"\"\n    rows = []\n    for c in np.unique(labels):\n        Y = X[labels == c]\n        m, v = Y.mean(0), Y.var(0, ddof=1)\n        ok = (m > 0) & (v > 0)\n        s, i = np.polyfit(np.log10(m[ok]), np.log10(v[ok]), 1)\n        rows.append((c, s, i, int(ok.sum())))\n    return pd.DataFrame(rows, columns=[\"stimulus\", \"slope\", \"intercept\", \"n\"]).set_index(\"stimulus\")\n\n\ndef manipulate(X, labels, target, fits=None):\n    \"\"\"M2: rescale each trial's residual so that the stimulus's log-mean vs log-variance slope\n    becomes `target`, keeping the mean log variance over neurons (box_and_overlap.py).\"\"\"\n    if fits is None:\n        fits = fit_slopes(X, labels)\n    out = np.zeros_like(X, dtype=np.float64)\n    for c in np.unique(labels):\n        sel = labels == c\n        Y = X[sel]\n        m, v = Y.mean(0), Y.var(0, ddof=1)\n        ok = (m > 0) & (v > 0)\n        s, i = fits.loc[c, \"slope\"], fits.loc[c, \"intercept\"]\n        logm = np.log10(m[ok])\n        new_logv = (np.log10(v[ok]) - i) / s * target + (s - target) * logm.mean() + i\n        Z = np.repeat(m[None, :], Y.shape[0], 0)\n        Z[:, ok] = m[ok] + (Y[:, ok] - m[ok]) / np.sqrt(v[ok]) * np.sqrt(10 ** new_logv)\n        out[sel] = Z\n    return out\n\n\ndef overlap_matrix(X, labels, variant=\"methods\"):\n    \"\"\"M3: O[b, a] = fraction of a's trials whose nearest trial of b lies within the 5th\n    percentile of b's within-manifold pairwise distances.\n\n    variant \"methods\": the percentile over pairs of distinct trials, distances < threshold.\n    variant \"code\": the percentile over the full self-distance matrix with its zero diagonal,\n    distances <= threshold (box_and_overlap.py). The diagonal (self-overlap) is set to 1.\n    \"\"\"\n    stims = np.unique(labels)\n    groups = [X[labels == c] for c in stims]\n    thr = np.zeros(len(stims))\n    for k, G in enumerate(groups):\n        D = cdist(G, G)\n        if variant == \"methods\":\n            thr[k] = np.percentile(D[np.triu_indices(len(G), 1)], 5)\n        else:\n            thr[k] = np.percentile(D, 5)\n    O = np.ones((len(stims), len(stims)))\n    for b, Gb in enumerate(groups):\n        for a, Ga in enumerate(groups):\n            if a == b:\n                continue\n            nn = cdist(Ga, Gb).min(1)\n            O[b, a] = np.mean(nn < thr[b]) if variant == \"methods\" else np.mean(nn <= thr[b])\n    return O, stims\n\n\ndef largest_scc(O, nodes=None):\n    \"\"\"Size of the largest strongly connected component; edge a -> b when O[b, a] > 0.\"\"\"\n    n = O.shape[0]\n    nodes = range(n) if nodes is None else nodes\n    g = nx.DiGraph()\n    g.add_nodes_from(nodes)\n    for b in nodes:\n        for a in nodes:\n            if a != b and O[b, a] > 0:\n                g.add_edge(a, b)\n    return max(len(c) for c in nx.strongly_connected_components(g))\n\n\ndef mean_offdiag(O, nodes=None):\n    nodes = list(range(O.shape[0])) if nodes is None else list(nodes)\n    sub = O[np.ix_(nodes, nodes)]\n    return float(sub[~np.eye(len(nodes), dtype=bool)].mean())\n\n\ndef effective_dimensionality(X, labels):\n    \"\"\"Participation ratio of the covariance eigenvalues over N, per stimulus (Methods).\"\"\"\n    out = []\n    for c in np.unique(labels):\n        ev = np.clip(np.linalg.eigvalsh(np.cov(X[labels == c], rowvar=False)), 0, None)\n        out.append(ev.sum() ** 2 / (ev ** 2).sum() / X.shape[1])\n    return np.array(out)\n\n\ndef isomap_embed(X, n_components=2):\n    iso = Isomap(n_neighbors=5, n_components=n_components, eigen_solver=\"dense\")\n    return iso.fit_transform(X)\n\n\ndef centroid_geodesics(X, labels):\n    \"\"\"M5: geodesic distances among stimulus centroids, Isomap (n_neighbors 5) fitted on all\n    trials with the centroids appended (compute_geo_ortho.py).\"\"\"\n    stims = np.unique(labels)\n    C = np.array([X[labels == c].mean(0) for c in stims])\n    iso = Isomap(n_neighbors=5, n_components=1, eigen_solver=\"arpack\")\n    iso.fit(np.vstack([X, C]))\n    return iso.dist_matrix_[len(X):, len(X):], stims\n\n\ndef orthogonal_variance(X, labels, a, b):\n    \"\"\"Variance (ddof 1) over a's trials of the length of each trial's deviation from a's\n    centroid projected on the line from a's centroid to b's, over a's summed per-neuron\n    variance (Methods, \"Orthogonal variance\"; compute_geo_ortho.py).\"\"\"\n    A = X[labels == a]\n    ca, cb = A.mean(0), X[labels == b].mean(0)\n    d = cb - ca\n    proj = np.abs((A - ca) @ d) / np.linalg.norm(d)\n    return proj.var(ddof=1) / A.var(0, ddof=1).sum()\n"
}
```

```
File created successfully at: entries/kim-2025/kim2025.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/kim-2025 && python - <<'EOF'
import re
p='kim2025.py'; s=open(p).read()
s=s.replace('''    stims = np.unique(labels)
    C = np.array([X[labels == c].mean(0) for c in stims])
    iso = Isomap(n_neighbors=5, n_components=1, eigen_solver="arpack")
    iso.fit(np.vstack([X, C]))
    return iso.dist_matrix_[len(X):, len(X):], stims''','''    stims = np.unique(labels)
    C = np.array([X[labels == c].mean(0) for c in stims])
    # Isomap's own geodesic step: a 5-nearest-neighbour distance graph and undirected shortest
    # paths (sklearn.manifold.Isomap.dist_matrix_), without its eigendecomposition.
    graph = kneighbors_graph(np.vstack([X, C]), n_neighbors=5, mode="distance")
    D = shortest_path(graph, directed=False, indices=np.arange(len(X), len(X) + len(C)))
    return D[:, len(X):], stims''')
s=s.replace("from scipy.spatial.distance import cdist\n","from scipy.sparse.csgraph import shortest_path\nfrom scipy.spatial.distance import cdist\n")
s=s.replace("from sklearn.manifold import Isomap\n","from sklearn.manifold import Isomap\nfrom sklearn.neighbors import kneighbors_graph\n")
open(p,'w').write(s)
EOF
cd $TMPDIR && . kenv/bin/activate && cat > t1.py <<'EOF'
import sys, time, numpy as np, resource
sys.path.insert(0,'entries/kim-2025')
import kim2025 as K
t=time.time()
X,lab,rep=K.illusion_session("sub-630506/sub-630506_ses-1192952695_ogen.nwb")
print(rep, X.shape, time.time()-t)
fits=K.fit_slopes(X,lab); print(fits)
for tgt in [None,0,1,2]:
    Y = X if tgt is None else K.manipulate(X,lab,tgt,fits)
    t=time.time()
    O,st=K.overlap_matrix(Y,lab)
    nodes=[list(st).index(c) for c in (3,4,10)]
    print(tgt, K.largest_scc(O,nodes), K.mean_offdiag(O,nodes), K.largest_scc(O), K.mean_offdiag(O), K.effective_dimensionality(Y,lab).mean(), time.time()-t)
t=time.time(); D,st=K.centroid_geodesics(X,lab); print(time.time()-t); print(D.round(1))
print(K.orthogonal_variance(X,lab,4,3), K.orthogonal_variance(X,lab,4,11))
t=time.time(); E=K.isomap_embed(X); print('iso',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
python t1.py
```

```
{'presentations': 10720, 'leading_gray': 60, 'trailing_gray': 61, 'non_gray_outside_slots': 0, 'slots': 5300, 'duration_range_s': (0.3999699999999393, 0.4007200000000921), 'units_total': 2517, 'v1_units': 75, 'units_used': 75, 'codes_with_400': [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(10), np.int64(11), np.int64(12), np.int64(13)], 'counts_per_code': {0: 400, 1: 400, 2: 400, 3: 400, 4: 400, 5: 400, 6: 400, 7: 400, 8: 50, 9: 50, 10: 400, 11: 400, 12: 400, 13: 400, 14: 50, 15: 50, 16: 50, 17: 50, 18: 50, 19: 50, 20: 50, 21: 50}} (4800, 75) 4.108797550201416
             slope  intercept   n
stimulus                         
0         1.124433   0.339782  64
1         1.084268   0.255134  67
2         1.089295   0.246451  66
3         1.099014   0.295721  67
4         1.083337   0.255059  66
5         1.098870   0.268588  68
6         1.108977   0.288520  67
7         1.097775   0.248408  67
10        1.113504   0.255389  67
11        1.099500   0.259477  69
12        1.111871   0.252157  66
13        1.079346   0.260068  65
None 3 0.22125000000000003 12 0.3584280303030303 0.1155954906670491 0.32911086082458496
0 1 0.0 7 0.08365530303030304 0.31095402959615076 0.3269648551940918
1 3 0.18416666666666667 12 0.323844696969697 0.1285673978800573 0.3284006118774414
2 3 0.31749999999999995 12 0.46744318181818184 0.04815664156228442 0.3363022804260254
0.10372614860534668
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t2.py <<'EOF'
import sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0,'entries/kim-2025')
import kim2025 as K
f=K.open_nwb("sub-630506/sub-630506_ses-1192952695_ogen.nwb")
g=f['stimulus/templates/ICwcfg1_presentations']
print(dict(g.attrs)); print({k:dict(g[k].attrs) for k in ['ICwcfg1_presentations0','ICwcfg1_presentations3']})
fig,ax=plt.subplots(4,6,figsize=(18,9))
for k in range(22):
    im=g[f'ICwcfg1_presentations{k}'][::8,::8]
    a=ax.flat[k]; a.imshow(im,cmap='gray',vmin=0,vmax=255); a.set_title(f'{k} {K.ILLUSION_NAMES[k]}'); a.axis('off')
plt.tight_layout(); plt.savefig('tmpl.png',dpi=60)
EOF
python t2.py
```

```
{'description': 'movie', 'namespace': 'core', 'neurodata_type': 'Images', 'object_id': 'bd6dbabc-a427-475c-a5e7-0ac375c6bd76'}
{'ICwcfg1_presentations0': {'description': 'movie', 'namespace': 'core', 'neurodata_type': 'GrayscaleImage', 'object_id': '1d79b4be-5128-434e-aaa1-dc493ea2d1f5'}, 'ICwcfg1_presentations3': {'description': 'movie', 'namespace': 'core', 'neurodata_type': 'GrayscaleImage', 'object_id': 'e3651119-40b2-497a-a1aa-68f6bd8c3f54'}}
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/tmpl.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd entries/kim-2025 && python - <<'EOF'
p='kim2025.py'; s=open(p).read()
old=s[s.index('def illusion_session'):s.index('# ---------------------------------------------------------------- measures')]
new='''def illusion_session(path):
    """V1 spike counts (trials x units) and image codes for the 12 stimuli with 400 repeats.

    Returns X (all V1 units, reading a), labels, a per-unit mask of the Allen quality criteria
    (reading b is X[:, mask]), and a report of what was loaded.
    """
    f = open_nwb(path)
    units = units_table(f)
    rows = np.where(is_v1(units.location))[0]
    onsets, codes, report = illusion_trials(f)
    counts = spike_counts(f, rows, onsets, ILLUSION_WINDOW)
    vals, n = np.unique(codes, return_counts=True)
    use = np.isin(codes, vals[n == 400])
    order = np.argsort(codes[use], kind="stable")
    X = counts[use][order]
    labels = codes[use][order]
    mask = units.passes_quality.to_numpy()[rows]
    st = f["units/spike_times"]
    idx = f["units/spike_times_index"][:]
    first = st[int(np.r_[0, idx][rows[0]]):int(idx[rows[0]])] if len(rows) else np.array([])
    report.update(units_total=len(units), v1_units=len(rows), v1_quality=int(mask.sum()),
                  v1_good_label=int((units.quality.to_numpy()[rows] == "good").sum()),
                  v1_locations=dict(units.location.iloc[rows].value_counts()),
                  codes_with_400=[int(v) for v in vals[n == 400]],
                  counts_per_code=dict(zip(vals.tolist(), n.tolist())),
                  first_onset=float(onsets[0]), total_spikes=int(st.shape[0]),
                  first_unit_sorted=bool(np.all(np.diff(first) >= 0)),
                  isi_violations_range=(float(units.isi_violations.min()),
                                        float(units.isi_violations.max())))
    f.close()
    return X, labels, mask, report


def illusion_psth(path, bins=np.arange(-0.2, 0.6001, 0.01)):
    """Population V1 rate (spikes/s per unit) around trial onsets, Blank and non-Blank trials,
    for the clock check."""
    f = open_nwb(path)
    units = units_table(f)
    rows = np.where(is_v1(units.location))[0]
    onsets, codes, _ = illusion_trials(f)
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    st = f["units/spike_times"]
    out = {}
    for name, sel in (("blank", codes == 0), ("image", codes != 0)):
        h = np.zeros(len(bins) - 1)
        for r in rows:
            s = st[starts[r]:idx[r]]
            for o in onsets[sel]:
                a, b = np.searchsorted(s, [o + bins[0], o + bins[-1]])
                h += np.histogram(s[a:b] - o, bins)[0]
        out[name] = h / (sel.sum() * len(rows) * np.diff(bins))
    f.close()
    return bins, out


'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='kim2025.py'; s=open(p).read()
old='''        h = np.zeros(len(bins) - 1)
        for r in rows:
            s = st[starts[r]:idx[r]]
            for o in onsets[sel]:
                a, b = np.searchsorted(s, [o + bins[0], o + bins[-1]])
                h += np.histogram(s[a:b] - o, bins)[0]
'''
new='''        h = np.zeros(len(bins) - 1)
        edges = onsets[sel][:, None] + bins[None, :]
        for r in rows:
            s = st[starts[r]:idx[r]]
            h += np.diff(np.searchsorted(s, edges), axis=1).sum(0)
'''
s=s.replace(old,new); open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov 21 23:48:10 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && uv pip install -q nbformat nbclient ipykernel 2>&1 | tail -1; python -c "import nbformat; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nbgen.py",
 "content": "\"\"\"Build a notebook from a cell list file: cells separated by lines '# %% [kind] tags'.\"\"\"\nimport sys, re, nbformat\n\nsrc, out = sys.argv[1], sys.argv[2]\ntext = open(src).read()\nparts = re.split(r\"^# %% ?(\\[\\w+\\])?(.*)$\", text, flags=re.M)\nnb = nbformat.v4.new_notebook()\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\ni = 1\nwhile i < len(parts):\n    kind, tags, body = parts[i], parts[i + 1].strip(), parts[i + 2].strip(\"\\n\")\n    i += 3\n    if kind == \"[md]\":\n        cell = nbformat.v4.new_markdown_cell(body)\n    else:\n        cell = nbformat.v4.new_code_cell(body)\n    if tags:\n        cell.metadata[\"tags\"] = tags.split()\n    nb.cells.append(cell)\nnbformat.write(nb, out)\nprint(len(nb.cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nbgen.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/illusion.py",
 "content": "# %% [md]\n# Reproducing Kim & Shin (2025) on dandiset 000248: the OpenScope Illusion data\n\nPaper: Kim, J. H. & Shin, H. (2025). \"Neural variability structure in primary visual cortex is optimal for robust representation of visual similarity\", bioRxiv doi:10.1101/2025.06.30.662469 (preprint of July 2025, the text the claims file was written from; the registry lists the later title \"Intrinsic geometry of trial-to-trial variability in primary visual cortex is optimal for robust representation of visual similarity\").\n\nDataset: DANDI 000248, \"Allen Institute Openscope - Illusion project\", version 0.240502.2344, streamed from the archive. The paper cites the dandiset without a version. This is the only published version, so it is pinned. The paper's code read a post-processed copy dated 2024-01-30 (\"OpenScopeData_00248_v240130_postprocessed\"), before this version was published on 2024-05-02; no other published version exists to compare with.\n\nThe paper uses this dandiset only for the Isomap pictures of Figures 1C, 3A, 3E and 3F and for one sentence of the Methods. Its main analyses are on the Allen Visual Coding Neuropixels data, which are tested in the second notebook of this entry (`reproduce_kim_2025_allen.ipynb`).\n\n| Claim | Data | Tested here |\n|---|---|---|\n| illusion-data-link | with_labels | yes |\n| illusion-fig1c-isomap-geometry | dataset | yes |\n| illusion-fig3a-orthogonal-variance-example | dataset | yes |\n| illusion-geometry-similar-across-datasets | dataset | yes |\n| all other claims | elsewhere (Allen Visual Coding Neuropixels) | second notebook |\n\nNo result here depends on random draws (Isomap uses its dense eigensolver, and the decoding check uses unshuffled folds), so no seed is needed.\n\n# %%\nimport time\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy.stats import wilcoxon, spearmanr\nfrom sklearn.discriminant_analysis import LinearDiscriminantAnalysis\nfrom sklearn.model_selection import StratifiedKFold, cross_val_score\n\nimport kim2025 as K\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\nNAMES = K.ILLUSION_NAMES\npaths = [p for p in K.asset_paths() if p.endswith(\"_ogen.nwb\")]\nprint(f\"dandiset {K.DANDISET_ID} version {K.DANDISET_VERSION}: {len(K.asset_paths())} assets, \"\n      f\"{len(paths)} session files (*_ogen.nwb)\")\nfor p in paths:\n    print(\" \", p)\n\n# %% [md]\n## Data check\n\nEvery session file is opened; the V1 units (location containing VISp and not VISpm) are kept, with a flag for the Allen quality criteria, and spikes are counted in the 400 ms from the onset of each trial of the ICwcfg1 block.\n\n# %% sanity\nsessions = {}\nfor p in paths:\n    subj = p.split(\"/\")[0].replace(\"sub-\", \"\")\n    X, lab, mask, rep = K.illusion_session(p)\n    sessions[subj] = dict(X=X, labels=lab, mask=mask, rep=rep, path=p)\nrows = []\nfor subj, s in sessions.items():\n    r = s[\"rep\"]\n    rows.append(dict(subject=subj, in_code_list=subj in K.CODE_SUBJECTS,\n                     presentations=r[\"presentations\"], lead_gray=r[\"leading_gray\"],\n                     trail_gray=r[\"trailing_gray\"], trial_slots=r[\"slots\"],\n                     nongray_off_slot=r[\"non_gray_outside_slots\"],\n                     blank_trials=r[\"counts_per_code\"].get(0),\n                     n_codes_400=len(r[\"codes_with_400\"]), units=r[\"units_total\"],\n                     v1_units=r[\"v1_units\"], v1_quality=r[\"v1_quality\"],\n                     v1_good_label=r[\"v1_good_label\"], first_onset_s=round(r[\"first_onset\"], 2),\n                     total_spikes=r[\"total_spikes\"],\n                     dur_min=round(r[\"duration_range_s\"][0], 4), dur_max=round(r[\"duration_range_s\"][1], 4)))\nsummary = pd.DataFrame(rows).set_index(\"subject\")\nprint(summary.to_string())\nprint(\"\\nrepeats per image code (example session):\", sessions[K.EXAMPLE_SUBJECT][\"rep\"][\"counts_per_code\"])\nprint(\"codes with 400 repeats in every session:\",\n      sorted(set.intersection(*[set(s[\"rep\"][\"codes_with_400\"]) for s in sessions.values()])))\nprint(\"V1 locations, example session:\", sessions[K.EXAMPLE_SUBJECT][\"rep\"][\"v1_locations\"])\nallX = np.concatenate([s[\"X\"].ravel() for s in sessions.values()])\nprint(f\"spike counts per 400 ms trial: min {allX.min():.0f}, max {allX.max():.0f}, mean {allX.mean():.2f}\")\nprint(\"first V1 unit's spike times sorted, per session:\", {k: s[\"rep\"][\"first_unit_sorted\"] for k, s in sessions.items()})\nprint(\"duplicate check: distinct total spike counts\", summary.total_spikes.nunique(), \"of\", len(summary),\n      \"; distinct first onsets\", summary.first_onset_s.nunique())\n\n# %% [md]\nClock check. The gray inter-trial frame shows the same image as the Blank stimulus (template 0, four disks), so a Blank trial changes nothing on the screen while the other images do. If spikes and the trial table share a clock, the V1 population rate should rise some tens of ms after the onset of image trials and not after Blank trials, and the image identity should be decodable from counts in the 400 ms after onset and not from counts in the 400 ms before it (the previous inter-trial frame).\n\n# %% sanity\nbins, ps = K.illusion_psth(sessions[K.EXAMPLE_SUBJECT][\"path\"])\ncenters = (bins[:-1] + bins[1:]) / 2\nbase = ps[\"image\"][centers < 0].mean()\nprint(f\"example session, rate (spikes/s/unit) before onset {base:.2f}; peak after image onset \"\n      f\"{ps['image'].max():.2f} at {1000 * centers[ps['image'].argmax()]:.0f} ms; Blank trials peak \"\n      f\"{ps['blank'][(centers > 0) & (centers < 0.2)].max():.2f}\")\nlat = centers[(centers > 0) & (ps[\"image\"] > base + 0.5 * (ps[\"image\"].max() - base))][0]\nprint(f\"first 10 ms bin above half the peak response: {1000 * lat:.0f} ms after onset\")\nfig, ax = plt.subplots(figsize=(6, 3))\nax.plot(1000 * centers, ps[\"image\"], label=\"image trials\")\nax.plot(1000 * centers, ps[\"blank\"], label=\"Blank trials\")\nax.axvline(0, color=\"k\", lw=0.5); ax.set_xlabel(\"ms from onset\"); ax.set_ylabel(\"spikes/s per unit\"); ax.legend()\nprint(f\"plotted range: image {ps['image'].min():.2f} to {ps['image'].max():.2f}, blank {ps['blank'].min():.2f} to {ps['blank'].max():.2f}\")\nplt.show()\n\n# %% sanity\ndef decode_shift(path, shift):\n    f = K.open_nwb(path)\n    units = K.units_table(f)\n    rows_ = np.where(K.is_v1(units.location))[0]\n    onsets, codes, _ = K.illusion_trials(f)\n    keep = np.isin(codes, sessions[K.EXAMPLE_SUBJECT][\"rep\"][\"codes_with_400\"])\n    C = K.spike_counts(f, rows_, onsets[keep] + shift, K.ILLUSION_WINDOW)\n    f.close()\n    cv = StratifiedKFold(5, shuffle=False)\n    return cross_val_score(LinearDiscriminantAnalysis(), C, codes[keep], cv=cv).mean()\n\nfor shift in (0.0, -0.4):\n    print(f\"window shifted by {shift:+.1f} s: 12-way LDA accuracy {decode_shift(sessions[K.EXAMPLE_SUBJECT]['path'], shift):.3f} (chance {1/12:.3f})\")\n\n# %% [md]\n## illusion-data-link\n\n> Dandiset 000248 holds the OpenScope Illusion recordings the paper used for its Isomap pictures, an ICwcfg1 block in which stimuli are repeated 400 times, with V1 units, in the example session the paper's code uses.\n\nThe dandiset gives the image codes 0 to 21 and an image template for each, but no names. The names come from the code's map (claims file header). The templates are drawn below so that the map can be checked against what each image shows.\n\n# %% claim:illusion-data-link\nf = K.open_nwb(sessions[K.EXAMPLE_SUBJECT][\"path\"])\ng = f[\"stimulus/templates/ICwcfg1_presentations\"]\ntab = f[\"intervals/ICwcfg1_presentations\"]\nprint(\"ICwcfg1 table description:\", tab.attrs.get(\"description\"))\nprint(\"stimulus_name values:\", sorted(set(K._str(tab[\"stimulus_name\"][:]))))\nprint(\"columns:\", list(tab.keys()))\nfig, axes = plt.subplots(4, 6, figsize=(15, 6))\nfor k in range(22):\n    im = g[f\"ICwcfg1_presentations{k}\"][::8, ::8]\n    axes.flat[k].imshow(im, cmap=\"gray\", vmin=0, vmax=255)\n    axes.flat[k].set_title(f\"{k}: {NAMES[k]}\", fontsize=9)\nfor a in axes.flat:\n    a.axis(\"off\")\nplt.tight_layout(); plt.show()\nf.close()\nex = sessions[K.EXAMPLE_SUBJECT]\nprint(\"(i) sub-630506 present:\", K.EXAMPLE_SUBJECT in sessions,\n      \"| ICwcfg1 block present | stimuli with 400 repeats:\", len(ex[\"rep\"][\"codes_with_400\"]),\n      [NAMES[c] for c in ex[\"rep\"][\"codes_with_400\"]])\nprint(\"(ii) Ic1, Lc1, Tre1, Tre2 among them:\",\n      all(c in ex[\"rep\"][\"codes_with_400\"] for c in (3, 4, 10, 11)), \"(codes 3, 4, 10, 11 by the code's map)\")\nprint(\"(iii) V1 units in sub-630506:\", ex[\"rep\"][\"v1_units\"], \"; passing the Allen quality criteria:\", ex[\"rep\"][\"v1_quality\"])\nprint(\"code's 11 subjects present:\", [s for s in K.CODE_SUBJECTS if s in sessions], \"missing:\", [s for s in K.CODE_SUBJECTS if s not in sessions])\nprint(\"sessions in the dandiset but not in the code's list:\", [s for s in sessions if s not in K.CODE_SUBJECTS])\nprint(\"400-repeat stimuli per session:\", {k: len(s[\"rep\"][\"codes_with_400\"]) for k, s in sessions.items()})\n\n# %% [md]\n## illusion-fig1c-isomap-geometry\n\n> In an example session of the Illusion data, three stimulus manifolds of V1 activity appear continuous with little overlap in the as-is data, discontinuous at slope 0 and heavily overlapping at slope 2.\n\nSession sub-630506, the 12 stimuli with 400 repeats, slopes changed by residual rescaling (M2) after an M1 fit on these stimuli. Among Ic1, Lc1 and Tre1: (i) at slope 0 not one strongly connected component, (ii) as-is one, (iii) mean of the six directed overlaps larger at slope 2 than as-is, and as-is than at slope 0. Readings: the full N-neuron space and the 2D Isomap coordinates (claims file); the overlap threshold over distinct pairs (Methods, main) and over the full self-distance matrix with `<=` (code, variant); units all VISp (O3 a, main) and with the Allen quality criteria (O3 b).\n\n# %% claim:illusion-fig1c-isomap-geometry\nTRIO = (3, 4, 10)  # Ic1, Lc1, Tre1\n\ndef conditions(X, lab, slopes=(0, 1, 2)):\n    fits = K.fit_slopes(X, lab)\n    out = {\"as-is\": X}\n    for s in slopes:\n        out[f\"slope {s}\"] = K.manipulate(X, lab, s, fits)\n    return out, fits\n\ndef trio_tests(conds, lab, space, variant):\n    res = {}\n    embeds = {}\n    for name, Y in conds.items():\n        if space == \"isomap2d\":\n            E = K.isomap_embed(Y, 2)\n            embeds[name] = E\n            Y = E\n        O, stims = K.overlap_matrix(Y, lab, variant)\n        nodes = [list(stims).index(c) for c in TRIO]\n        res[name] = dict(scc_trio=K.largest_scc(O, nodes), mean_overlap_trio=K.mean_offdiag(O, nodes),\n                         scc_all12=K.largest_scc(O), mean_overlap_all12=K.mean_offdiag(O))\n    r = pd.DataFrame(res).T\n    i_ = r.loc[\"slope 0\", \"scc_trio\"] < 3\n    ii = r.loc[\"as-is\", \"scc_trio\"] == 3\n    iii = r.loc[\"slope 2\", \"mean_overlap_trio\"] > r.loc[\"as-is\", \"mean_overlap_trio\"] > r.loc[\"slope 0\", \"mean_overlap_trio\"]\n    return r, (bool(i_), bool(ii), bool(iii)), embeds\n\nfig1c = {}\nfor units in (\"all VISp\", \"quality\"):\n    X = ex[\"X\"] if units == \"all VISp\" else ex[\"X\"][:, ex[\"mask\"]]\n    conds, fits = conditions(X, ex[\"labels\"])\n    print(f\"--- units: {units} ({X.shape[1]}); M1 slopes of the 12 stimuli {fits.slope.min():.3f} to {fits.slope.max():.3f}\")\n    for space in (\"N-space\", \"isomap2d\"):\n        for variant in (\"methods\", \"code\"):\n            r, tests, emb = trio_tests(conds, ex[\"labels\"], space, variant)\n            fig1c[(units, space, variant)] = (r, tests, emb)\n            print(f\"[{space}, threshold {variant}] tests (i, ii, iii) = {tests}, {sum(tests)} of 3\")\n            print(r.round(4).to_string())\n\n# %% claim:illusion-fig1c-isomap-geometry\nr, tests, emb = fig1c[(\"all VISp\", \"isomap2d\", \"methods\")]\ncols = {3: \"tab:green\", 4: \"tab:orange\", 10: \"tab:blue\"}\nfig, axes = plt.subplots(1, 4, figsize=(16, 4))\nlab = ex[\"labels\"]\nfor a, (name, E) in zip(axes, emb.items()):\n    for c in TRIO:\n        a.scatter(E[lab == c, 0], E[lab == c, 1], s=3, c=cols[c], label=NAMES[c])\n    a.set_title(name); a.set_aspect(\"equal\")\n    print(f\"{name}: Isomap ranges x {E[:, 0].min():.1f} to {E[:, 0].max():.1f}, y {E[:, 1].min():.1f} to {E[:, 1].max():.1f}\")\naxes[0].legend(markerscale=4)\nplt.tight_layout(); plt.show()\n\n# %% [md]\nOther sessions (variant): the same three tests in the N-neuron space, Methods threshold, all VISp units.\n\n# %% claim:illusion-fig1c-isomap-geometry\nrows = []\nfor subj, s in sessions.items():\n    conds, _ = conditions(s[\"X\"], s[\"labels\"])\n    r, tests, _ = trio_tests(conds, s[\"labels\"], \"N-space\", \"methods\")\n    rows.append(dict(subject=subj, units=s[\"X\"].shape[1], i=tests[0], ii=tests[1], iii=tests[2],\n                     **{f\"ov_{k}\": round(v, 3) for k, v in r.mean_overlap_trio.items()},\n                     **{f\"scc12_{k}\": v for k, v in r.scc_all12.items()}))\nother = pd.DataFrame(rows).set_index(\"subject\")\nprint(other.to_string())\nprint(\"sessions with all three tests holding:\", int((other.i & other.ii & other.iii).sum()), \"of\", len(other))\n\n# %% [md]\n## illusion-fig3a-orthogonal-variance-example\n\n> In the example session of the Illusion data, the Lc1 manifold has larger orthogonal variance toward the faraway Ic1 manifold than toward the nearby Tre2 manifold.\n\nAs-is data of sub-630506, the 12 stimuli. Geodesic distance between centroids by M5; orthogonal variance as the Methods define it.\n\n# %% claim:illusion-fig3a-orthogonal-variance-example\nLC1, IC1, TRE2 = 4, 3, 11\nfor units in (\"all VISp\", \"quality\"):\n    X = ex[\"X\"] if units == \"all VISp\" else ex[\"X\"][:, ex[\"mask\"]]\n    D, stims = K.centroid_geodesics(X, ex[\"labels\"])\n    st = list(stims)\n    g_ic, g_tre = D[st.index(LC1), st.index(IC1)], D[st.index(LC1), st.index(TRE2)]\n    ov_ic = K.orthogonal_variance(X, ex[\"labels\"], LC1, IC1)\n    ov_tre = K.orthogonal_variance(X, ex[\"labels\"], LC1, TRE2)\n    geo, ov = [], []\n    for a in stims:\n        for b in stims:\n            if a != b:\n                geo.append(D[st.index(a), st.index(b)]); ov.append(K.orthogonal_variance(X, ex[\"labels\"], a, b))\n    rho, p = spearmanr(geo, ov)\n    print(f\"units {units} ({X.shape[1]}): geodesic Lc1-Ic1 {g_ic:.2f}, Lc1-Tre2 {g_tre:.2f}; \"\n          f\"orthogonal variance of Lc1 toward Ic1 {ov_ic:.4f}, toward Tre2 {ov_tre:.4f} (ratio {ov_ic / ov_tre:.2f})\")\n    print(f\"   Ic1 farther: {g_ic > g_tre}; variance larger toward Ic1: {ov_ic > ov_tre}; \"\n          f\"variant, Spearman over {len(geo)} ordered pairs rho = {rho:.3f}, p = {p:.2g}; finite geodesics {np.isfinite(D).all()}\")\n\n# %% [md]\n## illusion-geometry-similar-across-datasets\n\n> The changes in manifold geometry that come with changing the slope are qualitatively the same in the Illusion data as in the natural scenes data.\n\nEvery session with an ICwcfg1 block (12), V1 units, the 12 stimuli with 400 repeats, M2 at slopes 0 to 2. Per session, effective dimensionality averaged over stimuli and overlap (M3, Methods threshold) averaged over the 132 ordered pairs. Reproduced when the across-session mean dimensionality decreases and the mean overlap increases by the O2 reading, with the Wilcoxon signed-rank test (slopes 0 and 2 against as-is, across sessions, p < 0.05).\n\n# %% claim:illusion-geometry-similar-across-datasets\nt = time.time()\ngeom = {}\nfor units in (\"all VISp\", \"quality\"):\n    dims, ovs = {}, {}\n    for subj, s in sessions.items():\n        X = s[\"X\"] if units == \"all VISp\" else s[\"X\"][:, s[\"mask\"]]\n        fits = K.fit_slopes(X, s[\"labels\"])\n        d, o = {\"as-is\": K.effective_dimensionality(X, s[\"labels\"]).mean()}, {\"as-is\": K.mean_offdiag(K.overlap_matrix(X, s[\"labels\"])[0])}\n        for sl in K.TARGET_SLOPES:\n            Y = K.manipulate(X, s[\"labels\"], sl, fits)\n            d[sl] = K.effective_dimensionality(Y, s[\"labels\"]).mean()\n            o[sl] = K.mean_offdiag(K.overlap_matrix(Y, s[\"labels\"])[0])\n        dims[subj], ovs[subj] = d, o\n    geom[units] = (pd.DataFrame(dims).T, pd.DataFrame(ovs).T)\nprint(f\"computed in {time.time() - t:.0f} s\")\n\ndef o2(df, direction):\n    m = df.mean()\n    a0, a1, a2 = m[0.0], m[1.0], m[2.0]\n    order = (a2 < a1 < a0) if direction == \"decrease\" else (a2 > a1 > a0)\n    p0 = wilcoxon(df[0.0], df[\"as-is\"]).pvalue\n    p2 = wilcoxon(df[2.0], df[\"as-is\"]).pvalue\n    side0 = (m[0.0] > m[\"as-is\"]) if direction == \"decrease\" else (m[0.0] < m[\"as-is\"])\n    side2 = (m[2.0] < m[\"as-is\"]) if direction == \"decrease\" else (m[2.0] > m[\"as-is\"])\n    steps = np.diff(m[list(K.TARGET_SLOPES)].to_numpy())\n    strict = bool(np.all(steps < 0)) if direction == \"decrease\" else bool(np.all(steps > 0))\n    return dict(mean_slope0=a0, mean_slope1=a1, mean_slope2=a2, mean_asis=m[\"as-is\"], order=order,\n                p_slope0=p0, p_slope2=p2, direction_0_2_vs_asis=bool(side0 and side2), strict_every_step=strict,\n                holds=bool(order and p0 < 0.05 and p2 < 0.05 and side0 and side2))\n\nfor units, (dim, ov) in geom.items():\n    print(f\"--- units {units}, n = {len(dim)} sessions\")\n    print(\"dimensionality (decrease):\", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in o2(dim, \"decrease\").items()})\n    print(\"overlap (increase):\", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in o2(ov, \"increase\").items()})\n    print(\"sessions where dimensionality at slope 2 < slope 0:\", int((dim[2.0] < dim[0.0]).sum()),\n          \"; overlap at slope 2 > slope 0:\", int((ov[2.0] > ov[0.0]).sum()))\n\ndim, ov = geom[\"all VISp\"]\nprint(\"\\nper-session values, all VISp units (as-is, slopes 0, 1, 2):\")\nprint(pd.concat({\"dim\": dim[[\"as-is\", 0.0, 1.0, 2.0]], \"overlap\": ov[[\"as-is\", 0.0, 1.0, 2.0]]}, axis=1).round(3).to_string())\nprint(\"\\nexample session alone (variant):\", dict(dim=dim.loc[K.EXAMPLE_SUBJECT, [\"as-is\", 0.0, 1.0, 2.0]].round(3).to_dict(),\n                                           overlap=ov.loc[K.EXAMPLE_SUBJECT, [\"as-is\", 0.0, 1.0, 2.0]].round(3).to_dict()))\nfig, axes = plt.subplots(1, 2, figsize=(10, 3.5))\nfor a, df, name in ((axes[0], dim, \"effective dimensionality\"), (axes[1], ov, \"mean overlap\")):\n    m = df[list(K.TARGET_SLOPES)]\n    a.errorbar(K.TARGET_SLOPES, m.mean(), m.sem(), marker=\"o\"); a.axhline(df[\"as-is\"].mean(), color=\"k\", ls=\"--\", label=\"as-is\")\n    a.set_xlabel(\"slope\"); a.set_title(name); a.legend()\n    print(f\"{name}: plotted means {m.mean().min():.3f} to {m.mean().max():.3f}\")\nplt.tight_layout(); plt.show()\nprint(f\"notebook time so far {(time.time() - T0) / 60:.1f} min\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/illusion.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && mkdir -p work && cp entries/kim-2025/kim2025.py work/ && python nbgen.py illusion.py work/ill.ipynb && cd work && time python -c "
import nbformat, nbclient
nb=nbformat.read('ill.ipynb',4)
c=nbclient.NotebookClient(nb, timeout=3000, kernel_name='python3', resources={'metadata':{'path':'.'}})
try: c.execute()
finally: nbformat.write(nb,'ill_out.ipynb')
" 2>&1 | tail -5
```

```
18 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	8m20.793s
user	11m15.923s
sys	0m2.830s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && python3 -c "
import json
nb=json.load(open('ill_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i, c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text'])[:6000])
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
"
```

```
=== cell 1 None
dandiset 000248 version 0.240502.2344: 78 assets, 12 session files (*_ogen.nwb)
  sub-619293/sub-619293_ses-1184980079_ogen.nwb
  sub-619296/sub-619296_ses-1187930705_ogen.nwb
  sub-620333/sub-620333_ses-1188137866_ogen.nwb
  sub-620334/sub-620334_ses-1189887297_ogen.nwb
  sub-625545/sub-625545_ses-1182865981_ogen.nwb
  sub-625554/sub-625554_ses-1181330601_ogen.nwb
  sub-625555/sub-625555_ses-1183070926_ogen.nwb
  sub-630506/sub-630506_ses-1192952695_ogen.nwb
  sub-631510/sub-631510_ses-1196157974_ogen.nwb
  sub-631570/sub-631570_ses-1194857009_ogen.nwb
  sub-633229/sub-633229_ses-1199247593_ogen.nwb
  sub-637484/sub-637484_ses-1208667752_ogen.nwb

=== cell 3 ['sanity']
         in_code_list  presentations  lead_gray  trail_gray  trial_slots  nongray_off_slot  blank_trials  n_codes_400  units  v1_units  v1_quality  v1_good_label  first_onset_s  total_spikes  dur_min  dur_max
subject                                                                                                                                                                                                         
619293          False          10720         60          61         5300                 0           400           12   2136       102          23             74         262.24     103597302   0.4000   0.4007
619296           True          10720         60          61         5300                 0           400           12   1918       204          89            165          86.31     102057384   0.4001   0.4005
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kim-2025 && python - <<'EOF'
p='kim2025.py'; s=open(p).read()
old='''    first = int(np.argmax(frame != 0))
    last = int(len(frame) - 1 - np.argmax(frame[::-1] != 0))
    slots = np.arange(first, last + 1, 2)'''
new='''    first_image = int(np.argmax(frame != 0))
    last = int(len(frame) - 1 - np.argmax(frame[::-1] != 0))
    # The block opens with PRE_GRAY gray frames; when the first trial is a Blank trial the
    # leading gray run is longer by that trial and its inter-trial frame (two frames each).
    first = PRE_GRAY if first_image >= PRE_GRAY and (first_image - PRE_GRAY) % 2 == 0 else first_image
    slots = np.arange(first, last + 1, 2)'''
assert old in s
s=s.replace(old,new)
s=s.replace('''        "leading_gray": first,''','''        "leading_gray": first_image,
        "first_slot": first,''')
s=s.replace('''TARGET_SLOPES = np.round''','''PRE_GRAY = 60  # gray frames before the first trial slot of ICwcfg1 (shown in the data check)
TARGET_SLOPES = np.round''')
s=s.replace('''    Presentations last 400 ms with no gap. After the leading gray frames, trials and gray
    inter-trial frames alternate, so the trial slots are every other presentation starting at
    the first non-gray one;''','''    Presentations last 400 ms with no gap. After PRE_GRAY leading gray frames, trials and gray
    inter-trial frames alternate, so the trial slots are every other presentation from there;''')
open(p,'w').write(s)
EOF
grep -n "first_slot\|PRE_GRAY" kim2025.py; date -u
```

```
68:PRE_GRAY = 60  # gray frames before the first trial slot of ICwcfg1 (shown in the data check)
140:    Presentations last 400 ms with no gap. After PRE_GRAY leading gray frames, trials and gray
150:    # The block opens with PRE_GRAY gray frames; when the first trial is a Blank trial the
152:    first = PRE_GRAY if first_image >= PRE_GRAY and (first_image - PRE_GRAY) % 2 == 0 else first_image
158:        "first_slot": first,
Sat Nov 21 23:58:10 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && curl -sL -o RSA_decoding.py https://raw.githubusercontent.com/jhk4839/Neural_variability_robustness/ac3300b007c2348ccda73c0c87fb02f557791089/RSA_decoding.py && grep -n "combinations\|cosine\|def \|spearman\|SVC\|StratifiedKFold\|shuffle\|random" RSA_decoding.py | head -50; sed -n 89,138p box_and_overlap.py
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 99,120p RSA_decoding.py; sed -n 186,215p RSA_decoding.py; sed -n 612,660p RSA_decoding.py
```

```
def cos_sim(x, y):
    # x and y are 1D vectors

    # Remove NaN
    x, y = np.array(x), np.array(y)
    bool_notnan = np.logical_and(~np.isnan(x), ~np.isnan(y))
    x, y = x[bool_notnan].copy(), y[bool_notnan].copy()

    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

# %%
# Function for column normalization
def normc(matrix):
    '''For 2D matrix'''

    matrix_normalized = matrix / np.linalg.norm(matrix, axis=0)

    return matrix_normalized

# %%
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kim-2025 && cat >> kim2025.py <<'EOF'


# ---------------------------------------------------------------- Allen Visual Coding (000021)

ABO_AREAS = {"V1": "VISp", "LM": "VISl", "RL": "VISrl", "AL": "VISal", "PM": "VISpm", "AM": "VISam"}
SILENT_TRIAL_LIMIT = 0.10  # Methods: sessions with more than 10% of trials silent in all V1 units


def abo_session(path):
    """Natural scenes spike counts (250 ms from onset) of the units of V1 and the five higher
    visual areas that pass the Allen quality criteria, trials sorted by stimulus (frame -1 is
    the gray image). Also the mean running speed (cm/s) of each trial over the same window."""
    f = open_nwb(path, ABO_ID, ABO_VERSION)
    units = units_table(f)
    area = np.full(len(units), "", dtype=object)
    for name, acr in ABO_AREAS.items():
        area[(units.location == acr).to_numpy()] = name
    rows = np.where((area != "") & units.passes_quality.to_numpy())[0]
    g = f["intervals/natural_scenes_presentations"]
    frame = g["frame"][:].astype(int)
    onsets = g["start_time"][:]
    order = np.lexsort((onsets, frame))
    counts = spike_counts(f, rows, onsets[order], SCENES_WINDOW)
    rs = f["processing/running/running_speed"]
    rt, rv = rs["timestamps"][:], rs["data"][:]
    a = np.searchsorted(rt, onsets[order])
    b = np.searchsorted(rt, onsets[order] + SCENES_WINDOW)
    csum = np.r_[0, np.cumsum(rv)]
    with np.errstate(invalid="ignore"):
        speed = (csum[b] - csum[a]) / (b - a)
    info = dict(path=path, units_total=len(units),
                area_units_all={k: int((units.location == v).sum()) for k, v in ABO_AREAS.items()},
                running_unit=rs["data"].attrs.get("unit"), trials=len(frame),
                isi_range=(float(units.isi_violations.min()), float(units.isi_violations.max())))
    f.close()
    return dict(X=counts, labels=frame[order], area=area[rows], speed=speed, info=info)


def silent_fraction(X):
    return float(np.mean(X.sum(1) == 0))


def overlap_matrix_fast(X, labels, variant="methods"):
    """overlap_matrix for equal numbers of trials per stimulus, with one distance matrix."""
    stims, n = np.unique(labels, return_counts=True)
    if len(set(n)) > 1:
        return overlap_matrix(X, labels, variant)
    S, R = len(stims), n[0]
    order = np.argsort(labels, kind="stable")
    Xs = X[order]
    D = cdist(Xs, Xs)
    iu = np.triu_indices(R, 1)
    thr = np.zeros(S)
    for k in range(S):
        block = D[k * R:(k + 1) * R, k * R:(k + 1) * R]
        thr[k] = np.percentile(block[iu], 5) if variant == "methods" else np.percentile(block, 5)
    nn = D.reshape(S * R, S, R).min(2)          # trial of a x stimulus b
    hit = nn < thr[None, :] if variant == "methods" else nn <= thr[None, :]
    O = hit.reshape(S, R, S).mean(1).T          # O[b, a]
    np.fill_diagonal(O, 1.0)
    return O, stims


def rsm(X, labels, n_trials=None):
    """Mean over unordered pairs of trial indices (r1 < r2) of the cosine similarity between
    stimulus i's trial r1 and stimulus j's trial r2, ignoring zero vectors as the code's
    nanmean does (RSA_decoding.py). X rows sorted by stimulus; n_trials keeps the first n."""
    stims = np.unique(labels)
    R = min(np.sum(labels == s) for s in stims) if n_trials is None else n_trials
    T = np.stack([X[labels == s][:R] for s in stims])          # S x R x N
    norm = np.linalg.norm(T, axis=2, keepdims=True)
    valid = (norm[..., 0] > 0).astype(float)
    U = np.divide(T, norm, out=np.zeros_like(T), where=norm > 0)
    cumU = np.cumsum(U[:, ::-1], axis=1)[:, ::-1]               # sum over r2 >= r
    cumV = np.cumsum(valid[:, ::-1], axis=1)[:, ::-1]
    later_U = np.concatenate([cumU[:, 1:], np.zeros_like(cumU[:, :1])], axis=1)
    later_V = np.concatenate([cumV[:, 1:], np.zeros_like(cumV[:, :1])], axis=1)
    num = np.einsum("irn,jrn->ij", U, later_U)
    den = np.einsum("ir,jr->ij", valid, later_V)
    return num / den


def shuffle_within_stimulus(X, labels, rng):
    """Permute the trial order within each stimulus (all neurons together)."""
    Y = X.copy()
    for s in np.unique(labels):
        idx = np.where(labels == s)[0]
        Y[idx] = X[rng.permutation(idx)]
    return Y


def pc1_fraction(X, labels):
    """Fraction of variance on the first principal component of each stimulus manifold."""
    out = []
    for c in np.unique(labels):
        ev = np.clip(np.linalg.eigvalsh(np.cov(X[labels == c], rowvar=False)), 0, None)
        out.append(ev[-1] / ev.sum() if ev.sum() > 0 else np.nan)
    return np.array(out)


def occupied_voxels(Y, Xref):
    """Unit voxels (edge 1 spike) occupied by the points of Y inside the box of Xref
    (min - 1 to max + 1 per neuron), compute_percent_filled in box_and_overlap.py."""
    lo, hi = Xref.min(0) - 1, Xref.max(0) + 1
    inside = np.all((Y >= lo) & (Y <= hi), axis=1)
    P = Y[inside]
    if len(P) == 0:
        return 0
    return len(np.unique(np.floor(P - P.min(0)), axis=0))


def across_stimulus_slopes(X, labels):
    """Per neuron, OLS of log10 variance on log10 mean across stimuli with mean > 0
    (Methods, "Log-mean vs. log-variance relationship across stimuli")."""
    stims = np.unique(labels)
    M = np.array([X[labels == s].mean(0) for s in stims])
    V = np.array([X[labels == s].var(0, ddof=1) for s in stims])
    out = []
    for j in range(X.shape[1]):
        ok = (M[:, j] > 0) & (V[:, j] > 0)
        out.append(np.polyfit(np.log10(M[ok, j]), np.log10(V[ok, j]), 1)[0] if ok.sum() >= 2 else np.nan)
    return np.array(out)
EOF
cd $TMPDIR && . kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && cat > t3.py <<'EOF'
import sys, time, numpy as np, resource
sys.path.insert(0,'work')
import kim2025 as K
from sklearn.svm import SVC
t=time.time()
s=K.abo_session("sub-699733573/sub-699733573_ses-715093703.nwb")
print(time.time()-t, s['X'].shape, s['info'], {a:(s['area']==a).sum() for a in K.ABO_AREAS})
v1=s['area']=='V1'; X=s['X'][:,v1]; lab=s['labels']
print('silent', K.silent_fraction(X), np.nanmean(s['speed']), np.nanmax(s['speed']))
t=time.time(); O,st=K.overlap_matrix_fast(X,lab); print('overlap',time.time()-t, K.mean_offdiag(O))
t=time.time(); R=K.rsm(X,lab); print('rsm',time.time()-t, R.shape, np.nanmean(R))
t=time.time(); D,st=K.centroid_geodesics(X,lab); print('geo',time.time()-t)
t=time.time(); m=X.mean(0); clf=SVC(kernel='linear').fit(X[:5355]-m, lab[:5355]); print('svc fit', time.time()-t)
t=time.time(); print(K.occupied_voxels(X,X), time.time()-t)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
python t3.py
```

```
15.578777313232422 (5950, 284) {'path': 'sub-699733573/sub-699733573_ses-715093703.nwb', 'units_total': 2779, 'area_units_all': {'V1': 160, 'LM': 160, 'RL': 280, 'AL': 0, 'PM': 139, 'AM': 93}, 'running_unit': 'cm/s', 'trials': 5950, 'isi_range': (0.0, 2850.54104594518)} {'V1': np.int64(62), 'LM': np.int64(50), 'RL': np.int64(85), 'AL': np.int64(0), 'PM': np.int64(53), 'AM': np.int64(34)}
silent 0.1215126050420168 6.987916083247753 62.121779752476144
overlap 0.491030216217041 0.33826093149124054
rsm 0.0158843994140625 (119, 119) 0.7828302961421955
geo 0.15430974960327148
svc fit 0.9790651798248291
5228 0.024525880813598633
0.789624
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 140,196p box_and_overlap.py | grep -v "^\s*#" | head -40; sed -n 212,232p box_and_overlap.py; grep -n "PCA\|pca\|components_\|nearest\|argmin\|argsort" local_global_alignment.py | head -20
```

```
def compute_filling_boxcount(slope_ind, target_slope):

    c_proc = mp.current_process()
    print("Running on Process", c_proc.name, "PID", c_proc.pid)

    num_sess = 32
    num_box_sizes = 1

    list_box_ratios_asis = np.zeros((num_sess, num_box_sizes))
    list_box_ratios_RRneuron = np.zeros((num_sess, num_box_sizes))

    list_box_ratios_asis_isomap = np.zeros((num_sess, num_box_sizes))
    list_box_ratios_RRneuron_isomap = np.zeros((num_sess, num_box_sizes))

    for sess_ind, rate in enumerate(list_rate_all):
            print(f'target_slope = {target_slope:.1f}, session index: {sess_ind}')
            
            rate_sorted = rate.sort_index(axis=1)
            stm = rate_sorted.columns.copy()

[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kim-2025 && python - <<'EOF'
p='kim2025.py'; s=open(p).read()
old=s[s.index('def overlap_matrix_fast'):s.index('def rsm(')]
new='''def overlap_matrices_fast(X, labels):
    """Both readings of overlap_matrix (methods, code) from one squared-distance matrix, for
    equal numbers of trials per stimulus. Returns (O_methods, O_code, stims)."""
    stims, n = np.unique(labels, return_counts=True)
    if len(set(n)) > 1:
        return overlap_matrix(X, labels, "methods")[0], overlap_matrix(X, labels, "code")[0], stims
    S, R = len(stims), n[0]
    Xs = X[np.argsort(labels, kind="stable")].astype(np.float64)
    sq = (Xs ** 2).sum(1)
    D2 = sq[:, None] + sq[None, :] - 2 * Xs @ Xs.T
    np.maximum(D2, 0, out=D2)
    iu = np.triu_indices(R, 1)
    thr_m, thr_c = np.zeros(S), np.zeros(S)
    for k in range(S):
        block = D2[k * R:(k + 1) * R, k * R:(k + 1) * R].copy()
        np.fill_diagonal(block, 0)
        block = np.sqrt(block)
        thr_m[k] = np.percentile(block[iu], 5)
        thr_c[k] = np.percentile(block, 5)
    nn = np.sqrt(D2.reshape(S * R, S, R).min(2))     # trial of a x stimulus b
    O_m = (nn < thr_m[None, :]).reshape(S, R, S).mean(1).T
    O_c = (nn <= thr_c[None, :]).reshape(S, R, S).mean(1).T
    np.fill_diagonal(O_m, 1.0)
    np.fill_diagonal(O_c, 1.0)
    return O_m, O_c, stims


'''
s=s.replace(old,new)
s += '''

def orthogonal_variances(X, labels):
    """orthogonal_variance for every ordered pair: V[a, b] (diagonal NaN)."""
    stims = np.unique(labels)
    C = np.array([X[labels == c].mean(0) for c in stims])
    V = np.full((len(stims), len(stims)), np.nan)
    for i, a in enumerate(stims):
        A = X[labels == a]
        d = C - C[i]
        nrm = np.linalg.norm(d, axis=1)
        nrm[i] = 1.0
        proj = np.abs((A - C[i]) @ d.T) / nrm
        v = proj.var(0, ddof=1) / A.var(0, ddof=1).sum()
        v[i] = np.nan
        V[i] = v
    return V


def pc1_vectors(X, labels):
    """First principal component of each stimulus manifold and of all other stimuli's trials."""
    stims = np.unique(labels)
    own, rest = [], []
    for c in stims:
        A, B = X[labels == c], X[labels != c]
        own.append(np.linalg.eigh(np.cov(A, rowvar=False))[1][:, -1])
        rest.append(np.linalg.eigh(np.cov(B, rowvar=False))[1][:, -1])
    return np.array(own), np.array(rest)


def _abs_cos(u, v):
    return np.abs(np.sum(u * v, 1)) / (np.linalg.norm(u, axis=1) * np.linalg.norm(v, axis=1))


def _offdiag(M):
    return M[~np.eye(M.shape[0], dtype=bool)]


def session_measures(X, labels, seeds, areas=None, n_partitions=10, slopes=TARGET_SLOPES,
                     do_halves=True):
    """All per-session measures of the natural scenes claims, for the as-is data and each
    target slope. `seeds` maps a claim id to its seed (zlib.crc32 of "kim-2025/<claim id>");
    `areas` maps an area name to its own count matrix (higher visual areas, Figure S6).

    The nearest-neighbour manifold for local alignment is taken from the as-is geodesic
    distances, as local_global_alignment.py does (the per-slope neighbour is a variant).
    """
    from scipy.stats import spearmanr
    stims, n = np.unique(labels, return_counts=True)
    R = n.min()
    fits = fit_slopes(X, labels)
    conds = ["as-is"] + [float(s) for s in slopes]
    out = {k: {} for k in ("dim", "pc1", "O_m", "O_c", "vox", "geo_rho", "local", "local_slope_nn",
                           "global", "rsm", "rsm_half", "ov_half", "ov_half_off", "nc_maxdiff")}
    out["area_rsm"], out["area_rsm_half"] = {}, {}
    rng_trials = np.random.default_rng(seeds["fig4e-rsm-similarity-across-mice"])
    perm = {c: rng_trials.permutation(np.sum(labels == c))[:R] for c in stims}
    def take_rsm(Y, lab):
        Z = np.concatenate([Y[lab == c][perm[c]] for c in stims])
        return rsm(Z, np.repeat(stims, R))
    rng_part = np.random.default_rng(seeds["fig4c-rsm-similarity-within-mice"])
    parts = [rng_part.permutation(X.shape[1]) for _ in range(n_partitions)]
    rng_ov = np.random.default_rng(seeds["fig4a-overlap-consistency-within-mice"])
    parts_ov = [rng_ov.permutation(X.shape[1]) for _ in range(n_partitions)]
    h = X.shape[1] // 2
    D0, _ = centroid_geodesics(X, labels)
    nn_asis = np.array([np.argmin(np.where(np.eye(len(stims))[i] > 0, np.inf, D0[i])) for i in range(len(stims))])
    nc_asis = None
    area_fits = {a: fit_slopes(Xa, labels) for a, Xa in (areas or {}).items()}
    for c in conds:
        Y = X if c == "as-is" else manipulate(X, labels, c, fits)
        out["dim"][c] = effective_dimensionality(Y, labels)
        out["pc1"][c] = pc1_fraction(Y, labels)
        O_m, O_c, _ = overlap_matrices_fast(Y, labels)
        out["O_m"][c], out["O_c"][c] = O_m.astype(np.float32), O_c.astype(np.float32)
        out["vox"][c] = occupied_voxels(Y, X)
        D, _ = centroid_geodesics(Y, labels)
        V = orthogonal_variances(Y, labels)
        out["geo_rho"][c] = spearmanr(_offdiag(D), _offdiag(V)).statistic
        own, rest = pc1_vectors(Y, labels)
        nn_c = np.array([np.argmin(np.where(np.eye(len(stims))[i] > 0, np.inf, D[i])) for i in range(len(stims))])
        out["local"][c] = _abs_cos(own, own[nn_asis]).mean()
        out["local_slope_nn"][c] = _abs_cos(own, own[nn_c]).mean()
        out["global"][c] = _abs_cos(own, rest).mean()
        out["rsm"][c] = take_rsm(Y, labels).astype(np.float32)
        rh = []
        for pmt in parts:
            a, b = pmt[:h], pmt[h:2 * h]
            rh.append(spearmanr(take_rsm(Y[:, a], labels).ravel(), take_rsm(Y[:, b], labels).ravel(),
                                nan_policy="omit").statistic)
        out["rsm_half"][c] = float(np.mean(rh))
        if do_halves:
            oh, oh_off = [], []
            for pmt in parts_ov:
                a, b = pmt[:h], pmt[h:2 * h]
                Oa, Ob = overlap_matrices_fast(Y[:, a], labels)[0], overlap_matrices_fast(Y[:, b], labels)[0]
                oh.append(spearmanr(Oa.ravel(), Ob.ravel()).statistic)
                oh_off.append(spearmanr(_offdiag(Oa), _offdiag(Ob)).statistic)
            out["ov_half"][c], out["ov_half_off"][c] = float(np.mean(oh)), float(np.mean(oh_off))
        if c in ("as-is", 0.0, 1.0, 2.0):
            nc = []
            for s_ in stims:
                with np.errstate(invalid="ignore", divide="ignore"):
                    nc.append(np.corrcoef(Y[labels == s_], rowvar=False))
            nc = np.array(nc)
            if c == "as-is":
                nc_asis = nc
            else:
                out["nc_maxdiff"][c] = float(np.nanmax(np.abs(nc - nc_asis)))
        for a, Xa in (areas or {}).items():
            Ya = Xa if c == "as-is" else manipulate(Xa, labels, c, area_fits[a])
            out["area_rsm"].setdefault(a, {})[c] = take_rsm(Ya, labels).astype(np.float32)
            ha = Xa.shape[1] // 2
            rng_a = np.random.default_rng(seeds["figs6-higher-areas-consistency"])
            rh = []
            for _ in range(n_partitions):
                pmt = rng_a.permutation(Xa.shape[1])
                rh.append(spearmanr(take_rsm(Ya[:, pmt[:ha]], labels).ravel(),
                                    take_rsm(Ya[:, pmt[ha:2 * ha]], labels).ravel(), nan_policy="omit").statistic)
            out["area_rsm_half"].setdefault(a, {})[c] = float(np.mean(rh))
    out["asis_geo"], out["asis_ortho"] = D0, orthogonal_variances(X, labels)
    out["fits"] = fits
    return out
'''
open(p,'w').write(s)
EOF
cd $TMPDIR && cp entries/kim-2025/kim2025.py work/ && . kenv/bin/activate && cat > t4.py <<'EOF'
import os; os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"
import sys, time, numpy as np, resource, zlib
sys.path.insert(0,'work')
import kim2025 as K
s=K.abo_session("sub-703279277/sub-703279277_ses-719161530.nwb")
v1=s['area']=='V1'; X=s['X'][:,v1]; lab=s['labels']
print(X.shape, K.silent_fraction(X))
seeds={k: zlib.crc32(f"kim-2025/{k}".encode()) for k in ["fig4e-rsm-similarity-across-mice","fig4c-rsm-similarity-within-mice","fig4a-overlap-consistency-within-mice","figs6-higher-areas-consistency"]}
areas={a: s['X'][:, s['area']==a] for a in ("LM","PM") if (s['area']==a).sum()>=2}
t=time.time()
m=K.session_measures(X,lab,seeds,areas=areas,slopes=[0.0,1.0,2.0])
print('4 conds', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
for k in ['geo_rho','local','global','rsm_half','ov_half','ov_half_off','vox','nc_maxdiff','area_rsm_half']: print(k, m[k])
print({c: K.mean_offdiag(m['O_m'][c]) for c in m['O_m']}, {c: m['dim'][c].mean() for c in m['dim']})
EOF
python t4.py
```

```
(5950, 56) 0.0
4 conds 16.21569013595581 0.972524
geo_rho {'as-is': np.float64(0.28636525332254076), 0.0: np.float64(0.23209096082966174), 1.0: np.float64(0.28502066031738826), 2.0: np.float64(0.27700111693410484)}
local {'as-is': np.float64(0.8073338049225304), 0.0: np.float64(0.7509634727435135), 1.0: np.float64(0.8075482784760523), 2.0: np.float64(0.7715771871697843)}
global {'as-is': np.float64(0.8125310547165878), 0.0: np.float64(0.7128767045601396), 1.0: np.float64(0.8112755981937942), 2.0: np.float64(0.7598935341817876)}
rsm_half {'as-is': 0.3765584837464885, 0.0: 0.3308343011794843, 1.0: 0.33209267657386815, 2.0: 0.20103379512876235}
ov_half {'as-is': 0.6345424291776613, 0.0: 0.4222416980995806, 1.0: 0.6509772088252486, 2.0: 0.27372472778722207}
ov_half_off {'as-is': 0.6251637856646974, 0.0: 0.40691648946890685, 1.0: 0.6420204308098371, 2.0: 0.25512117412472063}
vox {'as-is': 5950, 0.0: 5716, 1.0: 5950, 2.0: 567}
nc_maxdiff {0.0: 3.0531133177191805e-15, 1.0: 3.552713678800501e-15, 2.0: 3.4416913763379853e-15}
area_rsm_half {'LM': {'as-is': 0.09689664024885832, 0.0: 0.10861168815045526, 1.0: 0.07385042779112608, 2.0: -0.051050218401498815}, 'PM': {'as-is': 0.12753548622184685, 0.0: 0.10895136179523288, 1.0: 0.06519281374940857, 2.0: -0.06211556835202733}}
{'as-is': 0.31454208493232727, 0.0: 0.08033327758312225, 1.0: 0.3037857711315155, 2.0: 0.4689388871192932} {'as-is': np.float64(0.15249674695788648), 0.0: np.float64(0.31678295908498655), 1.0: np.float64(0.15936374498934008), 2.0: np.float64(0.07499278242379509)}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/code && curl -sL -o dec.ipynb https://raw.githubusercontent.com/jhk4839/Neural_variability_robustness/ac3300b007c2348ccda73c0c87fb02f557791089/decode_noise_corr.ipynb && python3 -c "
import json
nb=json.load(open('dec.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'StratifiedKFold(' in s or 'SVC(' in s or 'cross_val' in s:
        for l in s.split('\n'):
            if any(k in l for k in ['StratifiedKFold(','SVC(','cross_val','min_num_trials','random','mean(axis','sub(']): print(i, l.strip()[:200])
" | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "SVC\|StratifiedKFold\|n_splits\|shuffle\|random_state\|def decode\|mean(axis=1)\|fit(" RSA_decoding.py | head -30
```

```
35:from sklearn.model_selection import cross_val_score, cross_validate, train_test_split, KFold, StratifiedKFold
632:                # random.shuffle(tt_pairs) 
667:            # random.shuffle(tt_pairs) 
832:                        # random.shuffle(tt_pairs) 
867:                    # random.shuffle(tt_pairs) 
913:def decode_ABO(sess_ind, decoder_type):
927:        n_splits = 10
982:        kfold = KFold(n_splits=n_splits)
983:        stkfold = StratifiedKFold(n_splits=n_splits)
990:        kfold = KFold(n_splits=n_splits)
991:        stkfold = StratifiedKFold(n_splits=n_splits)
993:        list_confusion_test = np.full((n_splits, len(train_stimuli), len(train_stimuli)), np.nan)
994:        list_accuracy = np.full(n_splits, np.nan)
1007:                    clf = svm.SVC(kernel='linear')
1015:                clf.fit(X_train, y_train) # SVC fitting to train data
1031:        mean_confusion_test_asis = sum(list_confusion_test) / n_splits
1084:            kfold = KFold(n_splits=n_splits)
1085:            stkfold = StratifiedKFold(n_splits=n_splits)
1087:            list_confusion_test = np.full((n_splits, len(train_stimuli), len(train_stimuli)), np.nan)
1088:            list_accuracy = np.full(n_splits, np.nan)
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 930,1030p RSA_decoding.py | grep -v "^\s*#" | grep -v "^\s*$" | head -70
```

```
list_target_slopes = np.linspace(0, 2, 21, endpoint=True)
        np.random.seed(0)
        all_stimuli = np.arange(-1, 118, 1).astype(int) # include grayscreen trials
        probe_stimuli = np.array([5, 12, 24, 34, 36, 44, 47, 78, 83, 87, 104, 111, 114, 115])
        train_stimuli = all_stimuli.copy()
        rate = list_rate_all[sess_ind].copy()
        stm = rate.columns.copy()
        rate = rate * 0.25
        all_stm_unique, all_stm_counts = np.unique(stm, return_counts=True) 
        stm_cnt_dict = dict(zip(all_stm_unique, all_stm_counts))
        min_num_trials = np.min(all_stm_counts) # session 4 has heterogeneous numbers of trials (minimum 47)
        list_rate_tt = [None] * num_trial_types
        for trial_type_ind, trial_type in enumerate(all_stimuli):
            list_rate_tt[trial_type_ind] = rate.loc[:, trial_type].iloc[:, :min_num_trials].copy()
        rate = np.stack(list_rate_tt, axis=2)
        rate_sorted = np.transpose(rate, (0, 2, 1)) # num_neurons x num_trial_types x min_num_trials
        rate_shuf = np.zeros_like(rate_sorted)
        for neu_ind in range(rate_sorted.shape[0]):
            shuf_inds = np.random.permutation(rate_sorted.shape[2])
            rate_shuf[neu_ind] = rate_sorted[neu_ind, :, shuf_inds].T.copy() 
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kim-2025 && python - <<'EOF'
p='kim2025.py'; s=open(p).read()
s=s.replace('''    info = dict(path=path, units_total=len(units),''','''    info = dict(path=path, units_total=len(units),
                eye_tracking=("EyeTracking" in f["acquisition"]) or any("eye" in k.lower() and "rig" not in k.lower()
                                                                     for k in f["processing"].keys()),''')
s += '''

def random_measures(X, labels, seeds, areas=None, n_partitions=10, slopes=TARGET_SLOPES):
    """The RSM-based measures of session_measures alone (Figures 4C, 4E, S6), for the seed checks."""
    from scipy.stats import spearmanr
    stims, n = np.unique(labels, return_counts=True)
    R = n.min()
    fits = fit_slopes(X, labels)
    rng_trials = np.random.default_rng(seeds["fig4e-rsm-similarity-across-mice"])
    perm = {c: rng_trials.permutation(np.sum(labels == c))[:R] for c in stims}
    def take_rsm(Y, lab):
        Z = np.concatenate([Y[lab == c][perm[c]] for c in stims])
        return rsm(Z, np.repeat(stims, R))
    rng_part = np.random.default_rng(seeds["fig4c-rsm-similarity-within-mice"])
    parts = [rng_part.permutation(X.shape[1]) for _ in range(n_partitions)]
    h = X.shape[1] // 2
    area_fits = {a: fit_slopes(Xa, labels) for a, Xa in (areas or {}).items()}
    out = {"rsm": {}, "rsm_half": {}, "area_rsm": {}, "area_rsm_half": {}}
    for c in ["as-is"] + [float(s) for s in slopes]:
        Y = X if c == "as-is" else manipulate(X, labels, c, fits)
        out["rsm"][c] = take_rsm(Y, labels).astype(np.float32)
        out["rsm_half"][c] = float(np.mean([spearmanr(take_rsm(Y[:, p[:h]], labels).ravel(),
                                                      take_rsm(Y[:, p[h:2 * h]], labels).ravel(),
                                                      nan_policy="omit").statistic for p in parts]))
        for a, Xa in (areas or {}).items():
            Ya = Xa if c == "as-is" else manipulate(Xa, labels, c, area_fits[a])
            out["area_rsm"].setdefault(a, {})[c] = take_rsm(Ya, labels).astype(np.float32)
            ha = Xa.shape[1] // 2
            rng_a = np.random.default_rng(seeds["figs6-higher-areas-consistency"])
            rh = []
            for _ in range(n_partitions):
                pmt = rng_a.permutation(Xa.shape[1])
                rh.append(spearmanr(take_rsm(Ya[:, pmt[:ha]], labels).ravel(),
                                    take_rsm(Ya[:, pmt[ha:2 * ha]], labels).ravel(), nan_policy="omit").statistic)
            out["area_rsm_half"].setdefault(a, {})[c] = float(np.mean(rh))
    return out


def decode_session(X, labels, target, seed, n_splits=10, shuffle_neurons=False):
    """Linear SVC (sklearn SVC, kernel linear, default C) accuracy of stimulus identity, 10-fold
    StratifiedKFold without shuffling after a random reordering of trials within stimulus, counts
    centred by the training mean per fold (RSA_decoding.py, decode_ABO). Trials are cut to the
    smallest repeat count. With shuffle_neurons, each neuron's trials are permuted within
    stimulus before the slope change (Figure S4C). target None is the as-is data."""
    from sklearn.model_selection import StratifiedKFold
    from sklearn.svm import SVC
    rng = np.random.default_rng(seed)
    stims, n = np.unique(labels, return_counts=True)
    R = n.min()
    T = np.stack([X[labels == c][:R] for c in stims])           # S x R x N
    if shuffle_neurons:
        for j in range(T.shape[2]):
            for i in range(T.shape[0]):
                T[i, :, j] = T[i, rng.permutation(R), j]
    Xc = T.reshape(-1, T.shape[2])
    lab = np.repeat(stims, R)
    if target is not None:
        Xc = manipulate(Xc, lab, target)
    T = Xc.reshape(len(stims), R, -1)
    for i in range(len(stims)):
        T[i] = T[i, rng.permutation(R)]
    Xc = T.reshape(-1, T.shape[2])
    acc = []
    for tr, te in StratifiedKFold(n_splits).split(Xc, lab):
        m = Xc[tr].mean(0)
        acc.append(SVC(kernel="linear").fit(Xc[tr] - m, lab[tr]).score(Xc[te] - m, lab[te]))
    return float(np.mean(acc))
'''
open(p,'w').write(s)
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='kim2025.py'; s=open(p).read()
old='''        for j in range(T.shape[2]):
            for i in range(T.shape[0]):
                T[i, :, j] = T[i, rng.permutation(R), j]'''
new='''        for j in range(T.shape[2]):            # one permutation per neuron, as the code
            T[:, :, j] = T[:, rng.permutation(R), j]'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/allen.py",
 "content": "# %% [md]\n# Reproducing Kim & Shin (2025) on its main dataset: Allen Visual Coding Neuropixels natural scenes\n\nPaper: Kim, J. H. & Shin, H. (2025), bioRxiv doi:10.1101/2025.06.30.662469 (July 2025 preprint, the text the claims file was written from).\n\nThe registry tests this paper on dandiset 000248, which the paper uses only for pictures (first notebook). Its findings rest on the Allen Brain Observatory Visual Coding Neuropixels data, \"Brain Observatory 1.1\" sessions, which the paper reads through AllenSDK without naming a release. These claims are `data: elsewhere`. Here they are tested on the same sessions as deposited on DANDI: dandiset 000021, \"Allen Institute - Visual Coding - Neuropixels (Brain Observatory 1.1 Stimulus Set)\", version 0.251116.2246 (doi:10.48324/dandi.000021/0.251116.2246), the only published version, streamed from the archive. The 32 session files it holds match the paper's 32 Brain Observatory 1.1 sessions in number.\n\nUnits: those whose peak channel lies in the area (VISp for V1; VISl, VISrl, VISal, VISpm, VISam for LM, RL, AL, PM, AM) and that pass the Allen quality criteria of the Methods (isi_violations < 0.5, amplitude_cutoff < 0.1, presence_ratio > 0.9). Counts are spikes in the 250 ms from each natural scenes onset (Methods). Sessions with more than 10% of trials silent in all V1 units are excluded (Methods).\n\n| Claim | Tested here |\n|---|---|\n| data-v1-units, fig1b-across-neuron-slope-near-1, fig1b-across-stimulus-slope, figs3-higher-visual-areas | yes |\n| figs4ab-noise-correlation-under-manipulation, fig1d-dimensionality-falls-with-slope, figs5c-space-occupancy-peak | yes |\n| fig2a-overlap-rises-with-slope, fig2c-continuity-from-slope-1 | yes |\n| fig3bc-geodesic-orthogonal-correlation, fig3d-correlation-peaks-near-1, fig3e-local-alignment-peaks-near-1, fig3f-global-alignment-peaks-near-1 | yes |\n| fig4a-overlap-consistency-within-mice, fig4c-rsm-similarity-within-mice, fig4d-overlap-consistency-across-mice, fig4e-rsm-similarity-across-mice, figs6-higher-areas-consistency | yes |\n| figs2-behavioral-state | locomotion part only; the pupil part is blocked (see that section) |\n| fig2b-decoding-falls-with-slope | third notebook, `reproduce_kim_2025_decoding.ipynb` |\n| figs1-gain-variance, figs4c-shuffling-alters-dependence, fig2d-tangent-angle-rises-below-1, figs5a-movie-slope-near-1 | blocked (attempt record) |\n\nSeeds: each random result uses the seed of its claim, `zlib.crc32(b\"kim-2025/<claim id>\")`, and the RSM-based results are repeated under the seed plus 1000, 2000, 3000 and 4000.\n\n# %%\nimport os\nos.environ[\"OMP_NUM_THREADS\"] = \"1\"\nos.environ[\"OPENBLAS_NUM_THREADS\"] = \"1\"\nos.environ[\"MKL_NUM_THREADS\"] = \"1\"\nimport time, zlib, itertools, resource\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom concurrent.futures import ProcessPoolExecutor\nimport multiprocessing as mp\nfrom scipy.stats import wilcoxon, mannwhitneyu, kruskal, spearmanr\n\nimport kim2025 as K\n\nT0 = time.time()\npd.set_option(\"display.width\", 220)\nSLOPES = [float(s) for s in K.TARGET_SLOPES]\ndef seed(claim):\n    return zlib.crc32(f\"kim-2025/{claim}\".encode())\npaths = [p for p in K.asset_paths(K.ABO_ID, K.ABO_VERSION) if \"probe\" not in p]\nprint(f\"dandiset {K.ABO_ID} version {K.ABO_VERSION}: {len(paths)} session files\")\n\n# %% [md]\n## Data check\n\n# %% sanity\nS = []\nfor p in paths:\n    S.append(K.abo_session(p))\nprint(f\"loaded in {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nrows = []\nfor i, s in enumerate(S):\n    v1 = s[\"area\"] == \"V1\"\n    lab = s[\"labels\"]\n    _, n = np.unique(lab, return_counts=True)\n    rows.append(dict(index=i, session=s[\"info\"][\"path\"].split(\"/\")[0], trials=s[\"info\"][\"trials\"], stimuli=len(n),\n                     repeats_min=n.min(), repeats_max=n.max(),\n                     **{f\"{a}_q\": int((s[\"area\"] == a).sum()) for a in K.ABO_AREAS},\n                     V1_all=s[\"info\"][\"area_units_all\"][\"V1\"],\n                     silent_V1=round(K.silent_fraction(s[\"X\"][:, v1]), 4),\n                     speed_mean=round(float(np.nanmean(s[\"speed\"])), 2), eye=s[\"info\"][\"eye_tracking\"]))\ntab = pd.DataFrame(rows).set_index(\"index\")\ntab[\"included\"] = tab.silent_V1 <= K.SILENT_TRIAL_LIMIT\nprint(tab.to_string())\nprint(\"frame codes:\", np.unique(S[1][\"labels\"])[[0, 1, -1]], \"(-1 is the gray image)\")\nprint(\"running speed unit:\", {s[\"info\"][\"running_unit\"] for s in S}, \"; trial-mean speed range\",\n      f\"{min(np.nanmin(s['speed']) for s in S):.1f} to {max(np.nanmax(s['speed']) for s in S):.1f}\")\nallc = np.concatenate([s[\"X\"].ravel() for s in S])\nprint(f\"spike counts per 250 ms: min {allc.min():.0f}, max {allc.max():.0f}, mean {allc.mean():.3f}\")\nkeep = [i for i in tab.index if tab.loc[i, \"included\"]]\nprint(\"excluded sessions:\", [i for i in tab.index if i not in keep], \"; included:\", len(keep))\nprint(\"duplicate check: distinct V1 count vectors\", len({tuple(S[i][\"X\"][:, S[i][\"area\"] == \"V1\"].sum(0)) for i in tab.index}), \"of\", len(S))\n\n# %% [md]\nClock check: the image identity is decoded from V1 counts in the 250 ms after onset and in a window shifted 2 s later (several presentations later in the random sequence), in one session.\n\n# %% sanity\nfrom sklearn.discriminant_analysis import LinearDiscriminantAnalysis\nfrom sklearn.model_selection import StratifiedKFold, cross_val_score\ni0 = keep[0]\nf = K.open_nwb(S[i0][\"info\"][\"path\"], K.ABO_ID, K.ABO_VERSION)\nu = K.units_table(f)\nrows_v1 = np.where((u.location == \"VISp\").to_numpy() & u.passes_quality.to_numpy())[0]\ng = f[\"intervals/natural_scenes_presentations\"]\nfr, on = g[\"frame\"][:].astype(int), g[\"start_time\"][:]\nfor shift in (0.0, 2.0):\n    C = K.spike_counts(f, rows_v1, on + shift, 0.25)\n    acc = cross_val_score(LinearDiscriminantAnalysis(), C, fr, cv=StratifiedKFold(5, shuffle=False)).mean()\n    print(f\"session {i0}, window shifted {shift:+.1f} s: 119-way accuracy {acc:.3f} (chance {1/119:.4f})\")\nf.close()\n\n# %% [md]\n## data-v1-units\n\n> The main analysis uses V1 units from 30 sessions of 30 mice, 64 +- 25 units per session (14 to 110), 1920 units in all, with 119 stimuli per session (3570 stimulus fits).\n\n# %% claim:data-v1-units\nnv1 = tab.loc[keep, \"V1_q\"]\nprint(f\"sessions {len(keep)} (of {len(S)}); V1 units per session mean {nv1.mean():.1f}, SD {nv1.std(ddof=1):.1f} (ddof 1; ddof 0 {nv1.std(ddof=0):.1f}), \"\n      f\"range {nv1.min()} to {nv1.max()}, total {nv1.sum()}; stimuli per session {set(tab.loc[keep, 'stimuli'])}; fits {119 * len(keep)}\")\nprint(\"mice: one session per subject folder,\", tab.loc[keep, \"session\"].nunique(), \"distinct subjects\")\n\n# %% [md]\n## fig1b-across-neuron-slope-near-1 and fig1b-across-stimulus-slope\n\n# %% claim:fig1b-across-neuron-slope-near-1\nfits = {i: K.fit_slopes(S[i][\"X\"][:, S[i][\"area\"] == \"V1\"], S[i][\"labels\"]) for i in keep}\nan = pd.concat([fits[i].assign(session=i) for i in keep])\nprint(f\"across-neuron slopes: n {len(an)}, mean {an.slope.mean():.4f}, SEM {an.slope.sem():.4f}, SD {an.slope.std(ddof=1):.4f}, \"\n      f\"median {an.slope.median():.4f}, range {an.slope.min():.3f} to {an.slope.max():.3f}\")\nprint(\"per-session mean slope range:\", round(an.groupby('session').slope.mean().min(), 3), \"to\", round(an.groupby('session').slope.mean().max(), 3))\nprint(\"neurons per fit (mean > 0): median\", an.n.median(), \", min\", an.n.min())\n\n# %% claim:fig1b-across-stimulus-slope\nast = np.concatenate([K.across_stimulus_slopes(S[i][\"X\"][:, S[i][\"area\"] == \"V1\"], S[i][\"labels\"]) for i in keep])\ndropped = int(np.isnan(ast).sum()); ast = ast[~np.isnan(ast)]\nmw = mannwhitneyu(ast, an.slope, alternative=\"two-sided\")\nprint(f\"across-stimulus slopes: n {len(ast)} ({dropped} neurons without 2 stimuli of nonzero mean dropped), mean {ast.mean():.4f}, SD {ast.std(ddof=1):.4f}, median {np.median(ast):.4f}\")\nprint(f\"across-neuron: mean {an.slope.mean():.4f}, median {an.slope.median():.4f}; rank-sum (Mann-Whitney U, two-sided) U = {mw.statistic:.0f}, p = {mw.pvalue:.3g}\")\nfig, ax = plt.subplots(figsize=(5, 3))\nax.hist(an.slope, bins=np.linspace(0, 3, 61), alpha=0.6, density=True, label=\"across neurons\")\nax.hist(ast, bins=np.linspace(0, 3, 61), alpha=0.6, density=True, label=\"across stimuli\"); ax.legend(); ax.set_xlabel(\"slope\")\nprint(\"points outside 0 to 3:\", int((an.slope < 0).sum() + (an.slope > 3).sum()), \"across-neuron,\", int((ast < 0).sum() + (ast > 3).sum()), \"across-stimulus\")\nplt.show()\n\n# %% [md]\n## figs2-behavioral-state\n\n> The across-neuron slope is slightly but significantly modulated by behavioral state, smallest when the mouse runs and when its pupils are dilated, while staying near 1.\n\nLocomotion: trial mean running speed >= 1 cm/s is moving; M1 per session, stimulus and state, pooled; stimulus and state cells with fewer than 2 trials cannot give a variance and are dropped. Pupil: the session files of dandiset 000021 hold no eye tracking (column `eye` of the data check), so the pupil part cannot be run here.\n\n# %% claim:figs2-behavioral-state\nst_rows = []\nfor i in keep:\n    X, lab, sp = S[i][\"X\"][:, S[i][\"area\"] == \"V1\"], S[i][\"labels\"], S[i][\"speed\"]\n    for state, sel in ((\"moving\", sp >= 1), (\"stationary\", sp < 1)):\n        for c in np.unique(lab):\n            m = (lab == c) & sel\n            if m.sum() < 2:\n                continue\n            Y = X[m]; mu, v = Y.mean(0), Y.var(0, ddof=1); ok = (mu > 0) & (v > 0)\n            if ok.sum() >= 2:\n                st_rows.append((i, state, c, np.polyfit(np.log10(mu[ok]), np.log10(v[ok]), 1)[0], m.sum()))\nbs = pd.DataFrame(st_rows, columns=[\"session\", \"state\", \"stim\", \"slope\", \"trials\"])\nprint(bs.groupby(\"state\").slope.describe().round(4).to_string())\nmv, stn = bs[bs.state == \"moving\"].slope, bs[bs.state == \"stationary\"].slope\nprint(f\"moving vs stationary: medians {mv.median():.4f} vs {stn.median():.4f}; Mann-Whitney two-sided p = {mannwhitneyu(mv, stn).pvalue:.3g}\")\nprint(\"sessions with moving fits:\", bs[bs.state == \"moving\"].session.nunique(), \"; fraction of trials moving:\",\n      round(float(np.mean(np.concatenate([S[i][\"speed\"] >= 1 for i in keep]))), 3))\nprint(\"per-session median slope, moving minus stationary:\",\n      (bs.groupby([\"session\", \"state\"]).slope.median().unstack().dropna().pipe(lambda d: d.moving - d.stationary)).describe().round(4).to_dict())\n\n# %% [md]\n## figs3-higher-visual-areas\n\n> The across-neuron slope is concentrated around 1 in the five higher visual areas as in V1.\n\nM1 per area in every session with at least two quality units in the area (a line needs two neurons), over all 32 sessions and over the 30 included sessions.\n\n# %% claim:figs3-higher-visual-areas\nfor label, idx in ((\"all 32 sessions\", list(tab.index)), (\"30 included sessions\", keep)):\n    out = {}\n    for a in K.ABO_AREAS:\n        sl, ns = [], 0\n        for i in idx:\n            m = S[i][\"area\"] == a\n            if m.sum() >= 2:\n                ns += 1\n                sl.append(K.fit_slopes(S[i][\"X\"][:, m], S[i][\"labels\"]).slope.to_numpy())\n        sl = np.concatenate(sl)\n        out[a] = dict(sessions=ns, sessions_any_unit=int(sum((S[i][\"area\"] == a).sum() > 0 for i in idx)), fits=len(sl),\n                      median=round(float(np.median(sl)), 4), mean=round(float(sl.mean()), 4),\n                      within_0_9_1_1=bool(0.9 <= np.median(sl) <= 1.1))\n    print(label); print(pd.DataFrame(out).T.to_string())\n\n# %% [md]\n## Measures under slope manipulation\n\nFor every included session, V1 units, the as-is data and the 21 target slopes 0 to 2, `K.session_measures` computes the effective dimensionality, the PC1 fraction, pairwise noise correlations, the overlap matrices (Methods and code thresholds), occupied voxels, geodesic distances and orthogonal variances, local and global alignment, the RSM, and the half-split consistencies; and, for LM and PM, the RSM and its half-split consistency. Sessions run in 4 processes.\n\n# %%\nSEEDS = {k: seed(k) for k in [\"fig4e-rsm-similarity-across-mice\", \"fig4c-rsm-similarity-within-mice\",\n                              \"fig4a-overlap-consistency-within-mice\", \"figs6-higher-areas-consistency\"]}\ndef job(i, seeds=SEEDS, halves=True):\n    s = S[i]\n    areas = {a: s[\"X\"][:, s[\"area\"] == a] for a in (\"LM\", \"PM\") if (s[\"area\"] == a).sum() >= 2}\n    return K.session_measures(s[\"X\"][:, s[\"area\"] == \"V1\"], s[\"labels\"], seeds, areas=areas, do_halves=halves)\nt = time.time()\nwith ProcessPoolExecutor(4, mp_context=mp.get_context(\"fork\")) as ex:\n    M = dict(zip(keep, ex.map(job, keep)))\nprint(f\"measures for {len(M)} sessions in {(time.time() - t) / 60:.1f} min\")\nCONDS = [\"as-is\"] + SLOPES\n\ndef curve(key, f=lambda v: v):\n    return pd.DataFrame({i: {c: f(M[i][key][c]) for c in CONDS} for i in M}).T\n\ndef o1(df, label, n_label=\"sessions\"):\n    m = df[SLOPES].mean()\n    peak = m.idxmax()\n    p0, p2 = wilcoxon(df[0.0], df[\"as-is\"]).pvalue, wilcoxon(df[2.0], df[\"as-is\"]).pvalue\n    lower = bool(m[0.0] < df[\"as-is\"].mean() and m[2.0] < df[\"as-is\"].mean())\n    res = dict(peak_slope=peak, peak_mean=round(m.max(), 4), mean_asis=round(df[\"as-is\"].mean(), 4), mean_slope0=round(m[0.0], 4),\n               mean_slope1=round(m[1.0], 4), mean_slope2=round(m[2.0], 4), p_slope0=float(f\"{p0:.3g}\"), p_slope2=float(f\"{p2:.3g}\"),\n               ends_lower=lower, reading_a=bool(0.8 <= peak <= 1.2 and lower and p0 < 0.05 and p2 < 0.05),\n               reading_b=bool(0.7 <= peak <= 1.3 and lower and p0 < 0.05 and p2 < 0.05))\n    print(f\"{label} (n = {len(df)} {n_label}):\", res)\n    print(\"   curve:\", \" \".join(f\"{c}:{v:.3f}\" for c, v in m.items()))\n    return res\n\ndef o2(df, direction, label):\n    m = df[SLOPES].mean()\n    a0, a1, a2, asis = m[0.0], m[1.0], m[2.0], df[\"as-is\"].mean()\n    order = (a2 < a1 < a0) if direction == \"decrease\" else (a2 > a1 > a0)\n    p0, p2 = wilcoxon(df[0.0], df[\"as-is\"]).pvalue, wilcoxon(df[2.0], df[\"as-is\"]).pvalue\n    steps = np.diff(m.to_numpy())\n    strict = bool(np.all(steps < 0)) if direction == \"decrease\" else bool(np.all(steps > 0))\n    res = dict(mean_asis=round(asis, 4), mean_slope0=round(a0, 4), mean_slope1=round(a1, 4), mean_slope2=round(a2, 4),\n               order=order, p_slope0=float(f\"{p0:.3g}\"), p_slope2=float(f\"{p2:.3g}\"), strict_every_step=strict,\n               holds=bool(order and p0 < 0.05 and p2 < 0.05))\n    print(f\"{label} (n = {len(df)} sessions):\", res)\n    print(\"   curve:\", \" \".join(f\"{c}:{v:.3f}\" for c, v in m.items()))\n    return res\n\n# %% [md]\n## figs4ab-noise-correlation-under-manipulation\n\n> Rescaling residuals to change the slope leaves pairwise noise correlations unchanged but changes population-wise noise correlation.\n\n# %% claim:figs4ab-noise-correlation-under-manipulation\nncd = pd.DataFrame({i: M[i][\"nc_maxdiff\"] for i in M}).T\nprint(\"largest |noise correlation change| over sessions, stimuli and pairs, at slopes 0, 1, 2:\", ncd.max().to_dict())\npc = curve(\"pc1\")\nfor sl in (0.0, 2.0):\n    frac = [np.mean(np.abs(M[i][\"pc1\"][sl] - M[i][\"pc1\"][\"as-is\"]) > 1e-9) for i in M]\n    print(f\"slope {sl}: fraction of stimuli whose PC1 variance fraction differs from as-is, per session min {min(frac):.3f}, mean {np.mean(frac):.3f}; \"\n          f\"pooled mean PC1 fraction {np.mean([np.nanmean(M[i]['pc1'][sl]) for i in M]):.4f} vs as-is {np.mean([np.nanmean(M[i]['pc1']['as-is']) for i in M]):.4f}\")\nex7 = keep[7] if len(keep) > 7 else keep[0]\nprint(f\"example (session index {ex7}): mean PC1 fraction as-is {np.nanmean(M[ex7]['pc1']['as-is']):.4f}, slope 0 {np.nanmean(M[ex7]['pc1'][0.0]):.4f}, slope 2 {np.nanmean(M[ex7]['pc1'][2.0]):.4f}\")\n\n# %% [md]\n## fig1d-dimensionality-falls-with-slope\n\n# %% claim:fig1d-dimensionality-falls-with-slope\ndim = curve(\"dim\", np.mean)\nr_dim = o2(dim, \"decrease\", \"effective dimensionality\")\n\n# %% [md]\n## figs5c-space-occupancy-peak\n\n# %% claim:figs5c-space-occupancy-peak\nvox = curve(\"vox\").astype(float)\nr_vox = o1(vox, \"occupied unit voxels\")\nprint(\"sessions where the as-is count equals the number of trials (every trial in its own voxel):\",\n      int(sum(vox.loc[i, 'as-is'] == len(S[i]['labels']) for i in M)), \"of\", len(M))\nprint(\"sessions whose maximum over slopes is reached at more than one slope:\", int(sum((vox.loc[i, SLOPES] == vox.loc[i, SLOPES].max()).sum() > 1 for i in M)))\n\n# %% [md]\n## fig2a-overlap-rises-with-slope and fig2c-continuity-from-slope-1\n\n# %% claim:fig2a-overlap-rises-with-slope\nov = curve(\"O_m\", K.mean_offdiag)\nr_ov = o2(ov, \"increase\", \"overlap, distinct pairs, Methods threshold (main)\")\nov_code = curve(\"O_c\", lambda O: float(O.mean()))\nr_ov_code = o2(ov_code, \"increase\", \"overlap, code variant (code threshold, full matrix with diagonal)\")\nov_c2 = curve(\"O_c\", K.mean_offdiag)\no2(ov_c2, \"increase\", \"overlap, code threshold, distinct pairs\")\n\n# %% claim:fig2c-continuity-from-slope-1\nscc = curve(\"O_m\", K.largest_scc).astype(float)\nscc_c = curve(\"O_c\", K.largest_scc).astype(float)\nfor name, df in ((\"Methods threshold\", scc), (\"code threshold\", scc_c)):\n    m = df[SLOPES].mean()\n    full = [c for c in SLOPES if m[c] >= 119]\n    first = full[0] if full else None\n    try:\n        p0 = wilcoxon(df[0.0], df[\"as-is\"]).pvalue\n    except ValueError:\n        p0 = float(\"nan\")\n    print(f\"{name}: mean largest SCC size by slope\", \" \".join(f\"{c}:{v:.1f}\" for c, v in m.items()), f\"| as-is {df['as-is'].mean():.1f}\")\n    print(f\"   first slope with mean 119: {first}; reading a (0.8-1.2): {first is not None and 0.8 <= first <= 1.2}; reading b (0.7-1.3): {first is not None and 0.7 <= first <= 1.3}; \"\n          f\"slope 0 mean {m[0.0]:.1f}, Wilcoxon vs as-is p = {p0:.3g}; sessions at 119 as-is {int((df['as-is'] == 119).sum())} of {len(df)}\")\n    print(\"   sessions reaching 119 by slope:\", \" \".join(f\"{c}:{int((df[c] == 119).sum())}\" for c in SLOPES))\n\n# %% [md]\n## fig3bc-geodesic-orthogonal-correlation, fig3d, fig3e, fig3f\n\n# %% claim:fig3bc-geodesic-orthogonal-correlation\ngeo = curve(\"geo_rho\")\nrho = geo[\"as-is\"]\nw = wilcoxon(rho, alternative=\"greater\")\nprint(f\"as-is Spearman rho per session: mean {rho.mean():.4f}, range {rho.min():.4f} to {rho.max():.4f}, positive in {(rho > 0).sum()} of {len(rho)}; \"\n      f\"one-sided Wilcoxon against 0 p = {w.pvalue:.3g}; pairs per session {int(np.isfinite(K._offdiag(M[keep[0]]['asis_ortho'])).sum())}\")\nprint(\"sessions with non-finite geodesics:\", int(sum(~np.isfinite(M[i][\"asis_geo\"]).any() == False for i in M) - len(M)) * -1)\n\n# %% claim:fig3d-correlation-peaks-near-1\nr_geo = o1(geo, \"geodesic-orthogonal variance Spearman\")\n\n# %% claim:fig3e-local-alignment-peaks-near-1\nr_loc = o1(curve(\"local\"), \"local alignment (as-is neighbour, code)\")\no1(curve(\"local_slope_nn\"), \"local alignment (variant, neighbour from the slope-changed data)\")\n\n# %% claim:fig3f-global-alignment-peaks-near-1\nr_glo = o1(curve(\"global\"), \"global alignment\")\n\n# %% [md]\n## fig4a, fig4c, fig4d, fig4e, figs6\n\n# %% claim:fig4a-overlap-consistency-within-mice\nr_4a = o1(curve(\"ov_half\"), \"overlap consistency within session, full matrices (code, main)\")\no1(curve(\"ov_half_off\"), \"overlap consistency within session, off-diagonal (variant)\")\n\n# %% claim:fig4c-rsm-similarity-within-mice\nr_4c = o1(curve(\"rsm_half\"), \"RSM similarity within session\")\n\n# %% claim:fig4d-overlap-consistency-across-mice\npairs = list(itertools.combinations(keep, 2))\ndef across(key, f):\n    return pd.DataFrame({p: {c: f(M[p[0]][key][c], M[p[1]][key][c]) for c in CONDS} for p in pairs}).T\nfull_sp = lambda A, B: spearmanr(A.ravel(), B.ravel()).statistic\noff_sp = lambda A, B: spearmanr(K._offdiag(A), K._offdiag(B)).statistic\nr_4d = o1(across(\"O_m\", full_sp), \"overlap consistency across sessions, full matrices (main)\", \"session pairs\")\no1(across(\"O_m\", off_sp), \"overlap consistency across sessions, off-diagonal (variant)\", \"session pairs\")\n\n# %% claim:fig4e-rsm-similarity-across-mice\nrsm_sp = lambda A, B: spearmanr(A.ravel(), B.ravel(), nan_policy=\"omit\").statistic\nr_4e = o1(across(\"rsm\", rsm_sp), \"RSM similarity across sessions\", \"session pairs\")\n\n# %% claim:figs6-higher-areas-consistency\ndef near_max(df, n_label):\n    m, se = df[SLOPES].mean(), df[SLOPES].sem()\n    peak = m.idxmax()\n    a = bool(m[1.0] >= m.max() - se[peak])\n    b = bool(0.8 <= peak <= 1.2)\n    b2 = bool(0.7 <= peak <= 1.3)\n    return dict(n=len(df), peak=peak, mean_at_1=round(m[1.0], 4), max=round(m.max(), 4), sem_at_peak=round(se[peak], 4),\n                reading_a=a, reading_b_08_12=b, reading_b_07_13=b2)\ns6 = {}\nfor a in (\"LM\", \"PM\"):\n    ids = [i for i in M if a in M[i][\"area_rsm_half\"]]\n    within = pd.DataFrame({i: M[i][\"area_rsm_half\"][a] for i in ids}).T\n    pa = list(itertools.combinations(ids, 2))\n    acr = pd.DataFrame({p: {c: rsm_sp(M[p[0]][\"area_rsm\"][a][c], M[p[1]][\"area_rsm\"][a][c]) for c in CONDS} for p in pa}).T\n    s6[(a, \"S6B within\")] = near_max(within, \"sessions\")\n    s6[(a, \"S6C across\")] = near_max(acr, \"pairs\")\n    print(a, \"within curve:\", \" \".join(f\"{c}:{v:.3f}\" for c, v in within[SLOPES].mean().items()))\n    print(a, \"across curve:\", \" \".join(f\"{c}:{v:.3f}\" for c, v in acr[SLOPES].mean().items()))\nprint(pd.DataFrame(s6).T.to_string())\n\n# %% [md]\n### Seed check for the RSM-based results (fig4c, fig4e, figs6)\n\n# %%\ndef rjob(args):\n    i, off = args\n    s = S[i]\n    areas = {a: s[\"X\"][:, s[\"area\"] == a] for a in (\"LM\", \"PM\") if (s[\"area\"] == a).sum() >= 2}\n    return K.random_measures(s[\"X\"][:, s[\"area\"] == \"V1\"], s[\"labels\"], {k: v + off for k, v in SEEDS.items()}, areas=areas)\nt = time.time()\nseed_res = {}\nfor off in (1000, 2000, 3000, 4000):\n    with ProcessPoolExecutor(4, mp_context=mp.get_context(\"fork\")) as ex:\n        seed_res[off] = dict(zip(keep, ex.map(rjob, [(i, off) for i in keep])))\nprint(f\"seed checks in {(time.time() - t) / 60:.1f} min\")\n\n# %% claim:fig4c-rsm-similarity-within-mice claim:fig4e-rsm-similarity-across-mice claim:figs6-higher-areas-consistency\nrows = []\nfor off, R_ in seed_res.items():\n    c4 = pd.DataFrame({i: R_[i][\"rsm_half\"] for i in R_}).T[SLOPES].mean()\n    e4 = pd.DataFrame({p: {c: rsm_sp(R_[p[0]][\"rsm\"][c], R_[p[1]][\"rsm\"][c]) for c in SLOPES} for p in pairs}).T.mean()\n    row = dict(offset=off, fig4c_peak=c4.idxmax(), fig4c_max=round(c4.max(), 4), fig4e_peak=e4.idxmax(), fig4e_max=round(e4.max(), 4))\n    for a in (\"LM\", \"PM\"):\n        ids = [i for i in R_ if a in R_[i][\"area_rsm_half\"]]\n        wa = pd.DataFrame({i: R_[i][\"area_rsm_half\"][a] for i in ids}).T[SLOPES]\n        pa = list(itertools.combinations(ids, 2))\n        aa = pd.DataFrame({p: {c: rsm_sp(R_[p[0]][\"area_rsm\"][a][c], R_[p[1]][\"area_rsm\"][a][c]) for c in SLOPES} for p in pa}).T\n        row[f\"{a}_within_peak\"], row[f\"{a}_within_1_vs_max_minus_sem\"] = wa.mean().idxmax(), bool(wa.mean()[1.0] >= wa.mean().max() - wa.sem()[wa.mean().idxmax()])\n        row[f\"{a}_across_peak\"], row[f\"{a}_across_1_vs_max_minus_sem\"] = aa.mean().idxmax(), bool(aa.mean()[1.0] >= aa.mean().max() - aa.sem()[aa.mean().idxmax()])\n    rows.append(row)\nprint(pd.DataFrame(rows).set_index(\"offset\").to_string())\nprint(f\"notebook time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/allen.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='allen.py'; s=open(p).read()
s=s.replace('''print("sessions with non-finite geodesics:", int(sum(~np.isfinite(M[i]["asis_geo"]).any() == False for i in M) - len(M)) * -1)''','''print("sessions with non-finite geodesics:", int(sum((~np.isfinite(M[i]["asis_geo"])).any() for i in M)))''')
s=s.replace('''import kim2025 as K
''','''import kim2025 as K

def wilcoxon(x, y=None, **kw):
    """scipy's Wilcoxon signed-rank test, with p = 1 when every difference is zero."""
    from scipy.stats import wilcoxon as _w
    d = np.asarray(x) - (0 if y is None else np.asarray(y))
    if np.all(d == 0):
        return type("R", (), {"pvalue": 1.0, "statistic": 0.0})()
    return _w(x, y, **kw) if y is not None else _w(x, **kw)
''',1)
s=s.replace("from scipy.stats import wilcoxon, mannwhitneyu","from scipy.stats import mannwhitneyu")
open(p,'w').write(s)
EOF
sed 's/^paths = \[p for p in K.asset_paths(K.ABO_ID, K.ABO_VERSION) if "probe" not in p\]/paths = [p for p in K.asset_paths(K.ABO_ID, K.ABO_VERSION) if "probe" not in p][:6]/' allen.py > allen_sub.py && grep -c "\[:6\]" allen_sub.py && . kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && python nbgen.py allen_sub.py work/al.ipynb && cd work && time python -c "
import nbformat, nbclient
nb=nbformat.read('al.ipynb',4)
c=nbclient.NotebookClient(nb, timeout=3000, kernel_name='python3', resources={'metadata':{'path':'.'}})
try: c.execute()
finally: nbformat.write(nb,'al_out.ipynb')
" 2>&1 | tail -5; python3 -c "
import json
nb=json.load(open('al_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i, c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text'])[:3000])
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'], ''.join(o['traceback'])[-1500:])
"
```

```
1
40 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	6m56.327s
user	14m48.359s
sys	1m26.167s
=== cell 1 None
dandiset 000021 version 0.251116.2246: 6 session files

=== cell 3 ['sanity']
loaded in 1.5 min; peak memory 0.67 GB
             session  trials  stimuli  repeats_min  repeats_max  V1_q  LM_q  RL_q  AL_q  PM_q  AM_q  V1_all  silent_V1  speed_mean    eye  included
index                                                                                                                                              
0      sub-699733573    5950      119           50           50    62    50    85     0    53    34     160     0.1215        6.99  False     False
1      sub-703279277    5950      119           50           50    56    42    18    10    21    40     134     0.0000       11.37  False      True
2      sub-707296975    5950      119           50           50    42    30    50    38     0    41     133     0.0000       13.25  False      True
3      sub-716813540    5950      119           50           50    19    37    73     0     0    60      67     0.0000        3.80  False      True
4      sub-717038285    5950      119           50           50   113    40    66    89    68     0     259     0.0000       19.49  False      True
5      sub-718643564    5950      119           50           50    45    25    72     0    15     0     136     0.0000       20.58  False      True
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; nproc; free -g | head -2
```

```
Sun Nov 22 00:11:15 UTC 2026
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
```

**Agent calls Bash**

```bash
cd entries/kim-2025 && python - <<'EOF'
p='kim2025.py'; s=open(p).read()
old='''def abo_session(path):'''
new='''def abo_session(path, areas=tuple(ABO_AREAS)):'''
s=s.replace(old,new)
old='''    for name, acr in ABO_AREAS.items():
        area[(units.location == acr).to_numpy()] = name'''
new='''    for name in areas:
        area[(units.location == ABO_AREAS[name]).to_numpy()] = name'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
cat > $TMPDIR/decoding.py <<'EOF'
# %% [md]
# Kim & Shin (2025): decoding image identity under slope manipulation (fig2b)

Paper: Kim, J. H. & Shin, H. (2025), bioRxiv doi:10.1101/2025.06.30.662469 (July 2025 preprint). Data: Allen Visual Coding Neuropixels, Brain Observatory 1.1 sessions, as deposited in dandiset 000021, version 0.251116.2246 (the only published version), streamed; the claim is `data: elsewhere` (see the second notebook for the choice of dataset). This notebook holds only the decoding of Figure 2B because it is the slowest analysis.

| Claim | Tested here |
|---|---|
| fig2b-decoding-falls-with-slope | yes |

Method (claims file criterion, and RSA_decoding.py `decode_ABO` at commit ac3300b for details it lacks): V1 units passing the Allen quality criteria, spikes in 250 ms, the 30 sessions with no more than 10% of trials silent in all V1 units; trials cut to the smallest repeat count of the session (47 in one session); trial order randomized within stimulus (the code does so with `np.random.choice` before its folds); `StratifiedKFold(10)` without shuffling; counts centred by the training mean per fold; `sklearn.svm.SVC(kernel="linear")` with default C; mean accuracy over folds. The slope is changed on the cut data. The seed is the claim's, `zlib.crc32(b"kim-2025/fig2b-decoding-falls-with-slope")`. The four further seeds the protocol asks for were not run: each repeat costs about 25 minutes on 4 CPUs (stated in the record).

# %%
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import time, zlib, resource
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
from scipy.stats import wilcoxon

import kim2025 as K

T0 = time.time()
SEED = zlib.crc32(b"kim-2025/fig2b-decoding-falls-with-slope")
SLOPES = [float(s) for s in K.TARGET_SLOPES]
paths = [p for p in K.asset_paths(K.ABO_ID, K.ABO_VERSION) if "probe" not in p]

# %% sanity
S = {}
for i, p in enumerate(paths):
    s = K.abo_session(p, areas=("V1",))
    S[i] = s
keep = [i for i in S if K.silent_fraction(S[i]["X"]) <= K.SILENT_TRIAL_LIMIT]
print(f"loaded {len(S)} sessions in {(time.time() - T0) / 60:.1f} min; included {len(keep)}; excluded {[i for i in S if i not in keep]}")
for i in keep:
    _, n = np.unique(S[i]["labels"], return_counts=True)
    if n.min() != n.max():
        print(f"session {i} ({S[i]['info']['path'].split('/')[0]}): repeats {n.min()} to {n.max()}, cut to {n.min()}")
print("V1 units per included session:", [S[i]["X"].shape[1] for i in keep])

# %% claim:fig2b-decoding-falls-with-slope
def job(args):
    i, c = args
    return i, c, K.decode_session(S[i]["X"], S[i]["labels"], None if c == "as-is" else c, SEED)
jobs = [(i, c) for i in keep for c in ["as-is"] + SLOPES]
t = time.time()
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    res = list(ex.map(job, jobs, chunksize=1))
acc = pd.DataFrame([(i, c, a) for i, c, a in res], columns=["session", "cond", "acc"]).pivot(index="session", columns="cond", values="acc")
acc = acc[["as-is"] + SLOPES]
print(f"{len(jobs)} decodings in {(time.time() - t) / 60:.1f} min")
m = acc[SLOPES].mean()
steps = np.diff(m.to_numpy())
p0, p2 = wilcoxon(acc[0.0], acc["as-is"]).pvalue, wilcoxon(acc[2.0], acc["as-is"]).pvalue
print("mean accuracy by slope:", " ".join(f"{c}:{v:.4f}" for c, v in m.items()), f"| as-is {acc['as-is'].mean():.4f}")
print(f"slope 0 {m[0.0]:.4f} > as-is {acc['as-is'].mean():.4f} > slope 2 {m[2.0]:.4f}: {m[0.0] > acc['as-is'].mean() > m[2.0]}; "
      f"Wilcoxon slope 0 vs as-is p = {p0:.3g}, slope 2 vs as-is p = {p2:.3g}")
print(f"order slope 2 < 1 < 0: {m[2.0] < m[1.0] < m[0.0]}; strict decrease at every 0.1 step: {bool(np.all(steps < 0))} "
      f"(steps that do not decrease: {[SLOPES[k + 1] for k in np.where(steps >= 0)[0]]})")
print(f"chance 1/119 = {1/119:.4f}; lowest session accuracy at any slope {acc.min().min():.4f}; all above chance: {bool((acc > 1/119).all().all())}")
print("sessions with accuracy at slope 2 below slope 0:", int((acc[2.0] < acc[0.0]).sum()), "of", len(acc))
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.errorbar(SLOPES, m, acc[SLOPES].sem(), marker="o"); ax.axhline(acc["as-is"].mean(), ls="--", color="k", label="as-is")
ax.axhline(1 / 119, color="gray", label="chance"); ax.set_xlabel("slope"); ax.set_ylabel("accuracy"); ax.legend()
print(f"plotted means {m.min():.4f} to {m.max():.4f}")
plt.show()
print(f"notebook time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
EOF
cd $TMPDIR && . kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && python - <<'EOF'
import os; os.environ["OMP_NUM_THREADS"]="1"
import sys,time; sys.path.insert(0,'work'); import kim2025 as K
t=time.time(); s=K.abo_session("sub-703279277/sub-703279277_ses-719161530.nwb", areas=("V1",)); print('load',time.time()-t, s['X'].shape)
t=time.time(); print(K.decode_session(s['X'],s['labels'],None,1), time.time()-t)
t=time.time(); print(K.decode_session(s['X'],s['labels'],2.0,1), time.time()-t)
EOF
```

```
load 5.849817276000977 (5950, 56)
0.37478991596638656 10.977940320968628
0.20941176470588233 108.31719779968262
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && curl -sL -o fsh.ipynb https://raw.githubusercontent.com/jhk4839/Neural_variability_robustness/ac3300b007c2348ccda73c0c87fb02f557791089/fit_slope_histogram.ipynb && python3 -c "
import json
nb=json.load(open('fsh.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'nelder' in s.lower() or 'gain' in s.lower() and 'def ' in s:
        print('----',i); print(s[:2500])
" | head -120
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && ls -la fsh.ipynb && python3 -c "
import json
nb=json.load(open('fsh.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if any(k in s for k in ['minimize','nbinom','gammaln','Nelder','supralinear']):
        print('----',i); print(s[:2000])
" | head -100; curl -s https://api.dandiarchive.org/api/dandisets/000022/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['most_recent_published_version'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/kim-2025 && cat >> kim2025.py <<'EOF'


FC_ID = "000022"
FC_VERSION = "0.251116.2247"
MOVIE_BIN_FRAMES = 12  # Methods: 12-frame (400 ms) bins of natural movie one, 75 bins


def movie_session(path):
    """V1 (VISp, quality criteria) spike counts in each 12-frame bin of every repeat of natural
    movie one, Functional Connectivity session of dandiset 000022. Returns counts (repeats*bins x
    units), bin labels, and a report; a repeat is kept only when it holds all 900 frames in order."""
    f = open_nwb(path, FC_ID, FC_VERSION)
    units = units_table(f)
    rows = np.where((units.location == "VISp").to_numpy() & units.passes_quality.to_numpy())[0]
    g = f["intervals/natural_movie_one_presentations"]
    frame = g["frame"][:].astype(int)
    start, stop = g["start_time"][:], g["stop_time"][:]
    heads = np.where(frame == 0)[0]
    reps, bad = [], 0
    for h in heads:
        seg = frame[h:h + 900]
        if len(seg) == 900 and np.array_equal(seg, np.arange(900)):
            reps.append(h)
        else:
            bad += 1
    nb = 900 // MOVIE_BIN_FRAMES
    on, off, lab = [], [], []
    for h in reps:
        for b in range(nb):
            on.append(start[h + b * MOVIE_BIN_FRAMES]); off.append(stop[h + (b + 1) * MOVIE_BIN_FRAMES - 1]); lab.append(b)
    on, off = np.array(on), np.array(off)
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    st = f["units/spike_times"]
    X = np.zeros((len(on), len(rows)))
    for j, r in enumerate(rows):
        s = st[starts[r]:idx[r]]
        X[:, j] = np.searchsorted(s, off, "left") - np.searchsorted(s, on, "left")
    rep = dict(path=path, repeats_complete=len(reps), repeats_incomplete=bad, v1_units=len(rows),
               bin_s=(float(np.min(off - on)) if len(on) else np.nan, float(np.max(off - on)) if len(on) else np.nan))
    f.close()
    return X, np.array(lab), rep
EOF
cd $TMPDIR && . kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && python - <<'EOF'
import sys,time; sys.path.insert(0,'work'); import kim2025 as K
ps=[p for p in K.asset_paths(K.FC_ID,K.FC_VERSION) if 'probe' not in p]; print(len(ps), ps[:3])
t=time.time(); X,lab,rep=K.movie_session(ps[0]); print(time.time()-t, X.shape, rep)
f=K.fit_slopes(X,lab); print(f.slope.describe())
EOF
```

```
Exit code 1
26 ['sub-744912845/sub-744912845_ses-766640955.nwb', 'sub-753795604/sub-753795604_ses-767871931.nwb', 'sub-754477355/sub-754477355_ses-768515987.nwb']
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/tmp/claude-1001/work/kim2025.py", line 674, in movie_session
    g = f["intervals/natural_movie_one_presentations"]
        ~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/kenv/lib/python3.13/site-packages/h5py/_hl/group.py", line 407, in __getitem__
    return self._get(name)
           ~~~~~~~~~^^^^^^
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "/tmp/claude-1001/kenv/lib/python3.13/site-packages/h5py/_hl/group.py", line 421, in _get
    oid = h5o.open(self.id, self._e(name), lapl=lapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5o.pyx", line 255, in h5py.h5o.open
KeyError: "Unable to synchronously open object (object 'natural_movie_one_presentations' doesn't exist)"
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python - <<'EOF'
import sys,time,numpy as np, collections; sys.path.insert(0,'work'); import kim2025 as K
f=K.open_nwb('sub-744912845/sub-744912845_ses-766640955.nwb',K.FC_ID,K.FC_VERSION)
print(list(f['intervals'].keys()))
for k in f['intervals']:
    if 'movie' in k:
        g=f['intervals'][k]; print(k, list(g.keys())); fr=g['frame'][:]; print(len(fr), fr[:5], fr.max(), (fr==0).sum())
        if 'stimulus_name' in g: print(collections.Counter(K._str(g['stimulus_name'][:])))
EOF
```

```
['dot_motion_presentations', 'drifting_gratings_75_repeats_presentations', 'drifting_gratings_contrast_presentations', 'flashes_presentations', 'gabors_presentations', 'natural_movie_one_more_repeats_presentations', 'natural_movie_one_shuffled_presentations', 'spontaneous_presentations']
natural_movie_one_more_repeats_presentations ['color', 'contrast', 'frame', 'id', 'opacity', 'orientation', 'size', 'start_time', 'stimulus_block', 'stimulus_index', 'stimulus_name', 'stop_time', 'tags', 'tags_index', 'timeseries', 'timeseries_index', 'units']
54000 [0. 1. 2. 3. 4.] 899.0 60
Counter({np.str_('natural_movie_one_more_repeats'): 54000})
natural_movie_one_shuffled_presentations ['color', 'contrast', 'frame', 'id', 'opacity', 'orientation', 'size', 'start_time', 'stimulus_block', 'stimulus_index', 'stimulus_name', 'stop_time', 'tags', 'tags_index', 'timeseries', 'timeseries_index', 'units']
18000 [0. 1. 2. 3. 4.] 899.0 20
Counter({np.str_('natural_movie_one_shuffled'): 18000})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/kim-2025 && sed -i 's|    g = f\["intervals/natural_movie_one_presentations"\]|    g = f["intervals/natural_movie_one_more_repeats_presentations"]  # 60 repeats, the "natural movie one" block of these sessions|' kim2025.py && cd $TMPDIR && . kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && python - <<'EOF'
import sys,time; sys.path.insert(0,'work'); import kim2025 as K
ps=[p for p in K.asset_paths(K.FC_ID,K.FC_VERSION) if 'probe' not in p]
t=time.time(); X,lab,rep=K.movie_session(ps[0]); print(time.time()-t, X.shape, rep)
f=K.fit_slopes(X,lab); print(f.slope.describe())
EOF
```

```
3.9674177169799805 (4500, 60) {'path': 'sub-744912845/sub-744912845_ses-766640955.nwb', 'repeats_complete': 60, 'repeats_incomplete': 0, 'v1_units': 60, 'bin_s': (0.38365276777767576, 0.41701526552333235)}
count    75.000000
mean      1.117361
std       0.038518
min       1.024394
25%       1.092304
50%       1.116866
75%       1.144835
max       1.214283
Name: slope, dtype: float64
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='allen.py'; s=open(p).read()
s=s.replace('''| fig2b-decoding-falls-with-slope | third notebook, `reproduce_kim_2025_decoding.ipynb` |
| figs1-gain-variance, figs4c-shuffling-alters-dependence, fig2d-tangent-angle-rises-below-1, figs5a-movie-slope-near-1 | blocked (attempt record) |''','''| figs5a-movie-slope-near-1 | yes, on the Functional Connectivity sessions of dandiset 000022 |
| fig2b-decoding-falls-with-slope, figs4c-shuffling-alters-dependence | blocked as too large; the timing that decides it is at the end |
| figs1-gain-variance, fig2d-tangent-angle-rises-below-1 | blocked (attempt record) |''')
s += '''
# %% [md]
## figs5a-movie-slope-near-1

> In the natural movie data the across-neuron log-mean against log-variance relation is also linear with slope near 1.

The paper's natural movie data are the Allen "Functional Connectivity" sessions, deposited as dandiset 000022, version 0.251116.2247 (the only published version; doi:10.48324/dandi.000022/0.251116.2247), streamed. In these files the 60-repeat block of natural movie one is `natural_movie_one_more_repeats_presentations` (a 20-repeat shuffled version is a separate table). Each repeat is cut into 75 bins of 12 frames; V1 units by the Allen quality criteria; M1 per bin and session. Sessions are excluded when a repeat is incomplete (the Methods' "truncated movies") or when they have no V1 units.

# %% claim:figs5a-movie-slope-near-1
fc_paths = [p for p in K.asset_paths(K.FC_ID, K.FC_VERSION) if "probe" not in p]
mv_rows, mv_slopes = [], []
for p in fc_paths:
    Xm, labm, repm = K.movie_session(p)
    ok = repm["repeats_incomplete"] == 0 and repm["v1_units"] >= 2
    mv_rows.append(dict(session=p.split("/")[0], **{k: v for k, v in repm.items() if k != "path"}, used=ok))
    if ok:
        mv_slopes.append(K.fit_slopes(Xm, labm).slope.to_numpy())
mvt = pd.DataFrame(mv_rows)
print(mvt.to_string())
ms = np.concatenate(mv_slopes)
print(f"sessions {len(fc_paths)}, used {int(mvt.used.sum())}; bins per session {set(len(x) for x in mv_slopes)}; fits {len(ms)}")
print(f"pooled slopes: median {np.median(ms):.4f}, mean {ms.mean():.4f}, SD {ms.std(ddof=1):.4f}, range {ms.min():.3f} to {ms.max():.3f}")
print(f"reading 1 (median in 0.9 to 1.1): {0.9 <= np.median(ms) <= 1.1}; reading 2 (0.85 to 1.15): {0.85 <= np.median(ms) <= 1.15}")

# %% [md]
## Timing that blocks fig2b-decoding-falls-with-slope (and figs4c-shuffling-alters-dependence)

The decoding of Figure 2B (sklearn `SVC(kernel="linear")`, 119 classes, 10 folds, RSA_decoding.py `decode_ABO`) is timed here on one included session, as-is and at slope 2, to estimate the whole: 30 sessions times 22 conditions.

# %%
i1 = keep[0]
times = {}
for c in (None, 2.0):
    t = time.time()
    a = K.decode_session(S[i1]["X"][:, S[i1]["area"] == "V1"], S[i1]["labels"], c, seed("fig2b-decoding-falls-with-slope"))
    times[c] = time.time() - t
    print(f"session {i1}, {'as-is' if c is None else f'slope {c}'}: accuracy {a:.3f}, {times[c]:.0f} s")
lo, hi = 22 * len(keep) * times[None], 22 * len(keep) * times[2.0]
print(f"estimate for {22 * len(keep)} session-conditions: {lo / 3600:.1f} to {hi / 3600:.1f} CPU hours, "
      f"{lo / 4 / 60:.0f} to {hi / 4 / 60:.0f} min on 4 CPUs; Figure S4C doubles it with the shuffled data")
print(f"notebook time {(time.time() - T0) / 60:.1f} min")
'''
open(p,'w').write(s)
EOF
. kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && python nbgen.py allen.py work/al.ipynb && cd work && date -u && time python -c "
import nbformat, nbclient
nb=nbformat.read('al.ipynb',4)
c=nbclient.NotebookClient(nb, timeout=4000, kernel_name='python3', resources={'metadata':{'path':'.'}})
try: c.execute()
finally: nbformat.write(nb,'al_out.ipynb')
" 2>&1 | tail -3; date -u
```

```
44 cells
Sun Nov 22 00:15:15 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	43m27.168s
user	102m26.011s
sys	8m37.103s
Sun Nov 22 00:58:42 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && python3 -c "
import json
nb=json.load(open('al_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i, c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text'])[:4500])
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'], ''.join(o['traceback'])[-1500:])
"
```

```
=== cell 1 None
dandiset 000021 version 0.251116.2246: 32 session files

=== cell 3 ['sanity']
loaded in 7.2 min; peak memory 1.17 GB
             session  trials  stimuli  repeats_min  repeats_max  V1_q  LM_q  RL_q  AL_q  PM_q  AM_q  V1_all  silent_V1  speed_mean    eye  included
index                                                                                                                                              
0      sub-699733573    5950      119           50           50    62    50    85     0    53    34     160     0.1215        6.99  False     False
1      sub-703279277    5950      119           50           50    56    42    18    10    21    40     134     0.0000       11.37  False      True
2      sub-707296975    5950      119           50           50    42    30    50    38     0    41     133     0.0000       13.25  False      True
3      sub-716813540    5950      119           50           50    19    37    73     0     0    60      67     0.0000        3.80  False      True
4      sub-717038285    5950      119           50           50   113    40    66    89    68     0     259     0.0000       19.49  False      True
5      sub-718643564    5950      119           50           50    45    25    72     0    15     0     136     0.0000       20.58  False      True
6      sub-719817799    5950      119           50           50    39    33    32    43     0     0     126     0.0000        0.75   True      True
7      sub-719828686    5950      119           50           50   112    14    48    34    25    67     233     0.0000        3.14   True      True
8      sub-722882751    5950      119           50           50    59    20    76     0     0    58     157     0.0000        1.10   True      True
9      sub-723627600    5950      119           50           50    35    54    83    49    23     0     158     0.1800        0.76   True     False
10     sub-726141242    5950      119           50           50    70    41    52    74   
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python - <<'EOF'
import sys,numpy as np; sys.path.insert(0,'work'); import kim2025 as K
f=K.open_nwb('sub-719817799/sub-719817799_ses-744228101.nwb',K.ABO_ID,K.ABO_VERSION)
def show(n,o):
    import h5py
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict(o.attrs).get('unit'))
f['acquisition/EyeTracking'].visititems(show)
a=f['acquisition/EyeTracking/pupil_tracking/area'][:]; print(np.nanmin(a),np.nanmax(a),np.isnan(a).mean())
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
  File "/tmp/claude-1001/kenv/lib/python3.13/site-packages/h5py/_hl/group.py", line 407, in __getitem__
    return self._get(name)
           ~~~~~~~~~^^^^^^
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "/tmp/claude-1001/kenv/lib/python3.13/site-packages/h5py/_hl/group.py", line 421, in _get
    oid = h5o.open(self.id, self._e(name), lapl=lapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5o.pyx", line 255, in h5py.h5o.open
KeyError: "Unable to synchronously open object (object 'EyeTracking' doesn't exist)"
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python - <<'EOF'
import sys,numpy as np, h5py; sys.path.insert(0,'work'); import kim2025 as K
f=K.open_nwb('sub-719817799/sub-719817799_ses-744228101.nwb',K.ABO_ID,K.ABO_VERSION)
print(list(f['acquisition'].keys()), list(f['processing'].keys()))
for k in f['processing']:
    if 'eye' in k.lower() or 'pupil' in k.lower(): 
        def show(n,o):
            if isinstance(o,h5py.Dataset): print(k,n,o.shape,o.dtype, dict(o.attrs).get('unit'))
        f['processing'][k].visititems(show)
EOF
```

```
['raw_running_wheel_rotation', 'running_wheel_signal_voltage', 'running_wheel_supply_voltage'] ['eye_tracking', 'eye_tracking_rig_metadata', 'filtered_gaze_mapping', 'optotagging', 'raw_gaze_mapping', 'running', 'stimulus']
eye_tracking cr_ellipse_fits/center_x (288734,) float64 None
eye_tracking cr_ellipse_fits/center_y (288734,) float64 None
eye_tracking cr_ellipse_fits/height (288734,) float64 None
eye_tracking cr_ellipse_fits/id (288734,) int64 None
eye_tracking cr_ellipse_fits/phi (288734,) float64 None
eye_tracking cr_ellipse_fits/timestamps (288734,) float64 None
eye_tracking cr_ellipse_fits/width (288734,) float64 None
eye_tracking eye_ellipse_fits/center_x (288734,) float64 None
eye_tracking eye_ellipse_fits/center_y (288734,) float64 None
eye_tracking eye_ellipse_fits/height (288734,) float64 None
eye_tracking eye_ellipse_fits/id (288734,) int64 None
eye_tracking eye_ellipse_fits/phi (288734,) float64 None
eye_tracking eye_ellipse_fits/timestamps (288734,) float64 None
eye_tracking eye_ellipse_fits/width (288734,) float64 None
eye_tracking pupil_ellipse_fits/center_x (288734,) float64 None
eye_tracking pupil_ellipse_fits/center_y (288734,) float64 None
eye_tracking pupil_ellipse_fits/height (288734,) float64 None
eye_tracking pupil_ellipse_fits/id (288734,) int64 None
eye_tracking pupil_ellipse_fits/phi (288734,) float64 None
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python - <<'EOF'
import sys,numpy as np, h5py; sys.path.insert(0,'work'); import kim2025 as K
f=K.open_nwb('sub-719817799/sub-719817799_ses-744228101.nwb',K.ABO_ID,K.ABO_VERSION)
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict(o.attrs).get('unit'))
f['processing/filtered_gaze_mapping'].visititems(show)
g=f['processing/filtered_gaze_mapping']
for k in g:
    print(k, dict(g[k].attrs).get('description'))
EOF
```

```
eye_area/data (288734,) float64 Pixels ^ 2
eye_area/timestamps (288734,) float64 seconds
pupil_area/data (288734,) float64 Pixels ^ 2
pupil_area/timestamps (288734,) float64 seconds
screen_coordinates/data (288734, 2) float64 Centimeters
screen_coordinates/timestamps (288734,) float64 seconds
screen_coordinates_spherical/data (288734, 2) float64 Degrees
screen_coordinates_spherical/timestamps (288734,) float64 seconds
eye_area no description
pupil_area no description
screen_coordinates no description
screen_coordinates_spherical no description
Shell cwd was reset to
```

**Agent**

Pupil area exists for most sessions. Adding the pupil part, the `good`-label variant, then the final run.

**Agent calls Bash**

```bash
cd entries/kim-2025 && cat >> kim2025.py <<'EOF'


def abo_pupil(path, onsets, window=SCENES_WINDOW):
    """Mean pupil area (pixels^2, `processing/filtered_gaze_mapping/pupil_area`, the blink-filtered
    series AllenSDK serves as pupil area) over [onset, onset + window) of each trial; None when
    the session has no eye tracking."""
    f = open_nwb(path, ABO_ID, ABO_VERSION)
    if "filtered_gaze_mapping" not in f["processing"]:
        f.close()
        return None
    g = f["processing/filtered_gaze_mapping/pupil_area"]
    t, v = g["timestamps"][:], g["data"][:]
    f.close()
    a = np.searchsorted(t, onsets)
    b = np.searchsorted(t, onsets + window)
    ok = np.isfinite(v)
    cs = np.r_[0, np.cumsum(np.where(ok, v, 0))]
    cn = np.r_[0, np.cumsum(ok)]
    with np.errstate(invalid="ignore", divide="ignore"):
        return (cs[b] - cs[a]) / (cn[b] - cn[a])


def abo_onsets(path):
    """Natural scenes onsets in the order abo_session sorts its trials."""
    f = open_nwb(path, ABO_ID, ABO_VERSION)
    g = f["intervals/natural_scenes_presentations"]
    frame, onsets = g["frame"][:].astype(int), g["start_time"][:]
    good = units_table(f)
    f.close()
    return onsets[np.lexsort((onsets, frame))]
EOF
python - <<'EOF'
p='kim2025.py'; s=open(p).read()
# drop unused 'good' line in abo_onsets
s=s.replace('''    good = units_table(f)
    f.close()
    return onsets[np.lexsort((onsets, frame))]''','''    f.close()
    return onsets[np.lexsort((onsets, frame))]''')
s=s.replace('''    return dict(X=counts, labels=frame[order], area=area[rows], speed=speed, info=info)''','''    return dict(X=counts, labels=frame[order], area=area[rows], speed=speed, info=info,
                good=(units.quality.to_numpy()[rows] == "good"))''')
open(p,'w').write(s)
EOF
grep -n "good=" kim2025.py
```

```
379:                good=(units.quality.to_numpy()[rows] == "good"))
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='allen.py'; s=open(p).read()
s=s.replace('''| figs2-behavioral-state | locomotion part only; the pupil part is blocked (see that section) |''','''| figs2-behavioral-state | yes (pupil in the sessions with eye tracking) |''')
old='''print("mice: one session per subject folder,", tab.loc[keep, "session"].nunique(), "distinct subjects")'''
new=old+'''
ng = pd.Series({i: int(((S[i]["area"] == "V1") & S[i]["good"]).sum()) for i in keep})
print(f"variant, also requiring the units table's quality label 'good': mean {ng.mean():.1f}, SD {ng.std(ddof=1):.1f}, range {ng.min()} to {ng.max()}, total {ng.sum()}")'''
assert old in s; s=s.replace(old,new)
old='''print("neurons per fit (mean > 0): median", an.n.median(), ", min", an.n.min())'''
new=old+'''
an_g = pd.concat([K.fit_slopes(S[i]["X"][:, (S[i]["area"] == "V1") & S[i]["good"]], S[i]["labels"]) for i in keep])
print(f"variant, units also labelled 'good': n {len(an_g)}, mean {an_g.slope.mean():.4f}, SEM {an_g.slope.sem():.4f}, SD {an_g.slope.std(ddof=1):.4f}")'''
assert old in s; s=s.replace(old,new)
old='''Locomotion: trial mean running speed >= 1 cm/s is moving; M1 per session, stimulus and state, pooled; stimulus and state cells with fewer than 2 trials cannot give a variance and are dropped. Pupil: the session files of dandiset 000021 hold no eye tracking (column `eye` of the data check), so the pupil part cannot be run here.'''
new='''Locomotion: trial mean running speed >= 1 cm/s is moving; M1 per session, stimulus and state, pooled; stimulus and state cells with fewer than 2 trials cannot give a variance and are dropped. Pupil: trial mean of the blink-filtered pupil area (`processing/filtered_gaze_mapping/pupil_area`), present in the sessions marked `eye` in the data check; tertiles over the trials of all sessions pooled (code, fit_slope_histogram.ipynb cell 67), per-session tertiles as a variant; Kruskal-Wallis across the three groups of slopes.'''
assert old in s; s=s.replace(old,new)
old='''print("per-session median slope, moving minus stationary:",'''
new='''pup = {i: K.abo_pupil(S[i]["info"]["path"], K.abo_onsets(S[i]["info"]["path"])) for i in keep}
pup = {i: v for i, v in pup.items() if v is not None}
allp = np.concatenate([v for v in pup.values()])
edges = np.nanpercentile(allp, [100 / 3, 200 / 3])
print(f"pupil: {len(pup)} included sessions with eye tracking; trials without a pupil value {np.isnan(allp).mean():.3f}; pooled tertile edges {edges.round(1)} pixels^2")
for label, per_session in (("pooled tertiles (code)", False), ("per-session tertiles (variant)", True)):
    pr = []
    for i, pv in pup.items():
        X, lab = S[i]["X"][:, S[i]["area"] == "V1"], S[i]["labels"]
        e = np.nanpercentile(pv, [100 / 3, 200 / 3]) if per_session else edges
        tert = np.where(np.isnan(pv), -1, np.digitize(pv, e))
        for t_ in range(3):
            for c in np.unique(lab):
                m = (lab == c) & (tert == t_)
                if m.sum() < 2:
                    continue
                Y = X[m]; mu, v = Y.mean(0), Y.var(0, ddof=1); ok = (mu > 0) & (v > 0)
                if ok.sum() >= 2:
                    pr.append((i, t_, np.polyfit(np.log10(mu[ok]), np.log10(v[ok]), 1)[0]))
    pdf = pd.DataFrame(pr, columns=["session", "tertile", "slope"])
    meds = pdf.groupby("tertile").slope.median()
    kw = kruskal(*[pdf[pdf.tertile == t_].slope for t_ in range(3)])
    print(f"{label}: fits per tertile {pdf.groupby('tertile').size().to_dict()}, median slope per tertile {meds.round(4).to_dict()}, "
          f"largest tertile lowest: {bool(meds.idxmin() == 2)}, Kruskal-Wallis p = {kw.pvalue:.3g}, medians in 0.9-1.1: {bool(meds.between(0.9, 1.1).all())}")
print("per-session median slope, moving minus stationary:",'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
. kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && python - <<'EOF'
import sys,time,numpy as np,pandas as pd; sys.path.insert(0,'work'); import kim2025 as K
from scipy.stats import kruskal
t=time.time()
paths=[p for p in K.asset_paths(K.ABO_ID,K.ABO_VERSION) if 'probe' not in p]
p=paths[6]; on=K.abo_onsets(p); pv=K.abo_pupil(p,on); print(time.time()-t, np.nanmin(pv), np.nanmax(pv), np.isnan(pv).mean())
print(K.abo_pupil(paths[1],K.abo_onsets(paths[1])))
EOF
```

```
4.086904287338257 0.0020941348263444786 0.01067648128429255 0.16554621848739495
None
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t5.py <<'EOF'
import sys,time,numpy as np,pandas as pd; sys.path.insert(0,'work'); import kim2025 as K
from scipy.stats import kruskal
paths=[p for p in K.asset_paths(K.ABO_ID,K.ABO_VERSION) if 'probe' not in p]
S={}
for i,p in enumerate(paths):
    s=K.abo_session(p,areas=("V1",))
    if K.silent_fraction(s['X'])<=0.1: S[i]=s
keep=list(S)
ng = pd.Series({i: int(S[i]["good"].sum()) for i in keep})
print(f"good variant: mean {ng.mean():.1f}, SD {ng.std(ddof=1):.1f}, range {ng.min()} to {ng.max()}, total {ng.sum()}")
an_g = pd.concat([K.fit_slopes(S[i]["X"][:, S[i]["good"]], S[i]["labels"]) for i in keep])
print(f"variant good: n {len(an_g)}, mean {an_g.slope.mean():.4f}, SEM {an_g.slope.sem():.4f}, SD {an_g.slope.std(ddof=1):.4f}")
pup = {i: K.abo_pupil(S[i]["info"]["path"], K.abo_onsets(S[i]["info"]["path"])) for i in keep}
pup = {i: v for i, v in pup.items() if v is not None}
allp = np.concatenate([v for v in pup.values()])
edges = np.nanpercentile(allp, [100 / 3, 200 / 3])
print(f"pupil: {len(pup)} sessions; nan {np.isnan(allp).mean():.3f}; edges {edges}")
for label, per_session in (("pooled", False), ("per-session", True)):
    pr = []
    for i, pv in pup.items():
        X, lab = S[i]["X"], S[i]["labels"]
        e = np.nanpercentile(pv, [100 / 3, 200 / 3]) if per_session else edges
        tert = np.where(np.isnan(pv), -1, np.digitize(pv, e))
        for t_ in range(3):
            for c in np.unique(lab):
                m = (lab == c) & (tert == t_)
                if m.sum() < 2: continue
                Y = X[m]; mu, v = Y.mean(0), Y.var(0, ddof=1); ok = (mu > 0) & (v > 0)
                if ok.sum() >= 2: pr.append((i, t_, np.polyfit(np.log10(mu[ok]), np.log10(v[ok]), 1)[0]))
    pdf = pd.DataFrame(pr, columns=["session", "tertile", "slope"])
    meds = pdf.groupby("tertile").slope.median()
    kw = kruskal(*[pdf[pdf.tertile == t_].slope for t_ in range(3)])
    print(label, pdf.groupby('tertile').size().to_dict(), meds.round(4).to_dict(), meds.idxmin()==2, kw.pvalue, meds.between(0.9,1.1).all())
EOF
python t5.py; date -u
```

```
good variant: mean 66.9, SD 25.5, range 14 to 112, total 2008
variant good: n 3570, mean 1.0489, SEM 0.0011, SD 0.0665
pupil: 25 sessions; nan 0.105; edges [0.00155269 0.00258929]
pooled {0: 2228, 1: 2521, 2: 2116} {0: 1.0769, 1: 1.0528, 2: 1.0394} True 1.960530689502132e-46 True
per-session {0: 2975, 1: 2974, 2: 2975} {0: 1.0745, 1: 1.053, 2: 1.0427} True 2.733292733417201e-42 True
Sun Nov 22 01:05:33 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
curl -sL https://raw.githubusercontent.com/AllenInstitute/AllenSDK/master/allensdk/brain_observatory/ecephys/ecephys_session.py | grep -n "filter_by_validity\|quality\] == \|\"good\"\|'good'\|noise" | head -20; curl -s https://api.github.com/repos/AllenInstitute/AllenSDK/commits/master | python3 -c "import json,sys; print(json.load(sys.stdin)['sha'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.github.com/search/code?q=filter_by_validity+repo:AllenInstitute/AllenSDK" | python3 -c "import json,sys; d=json.load(sys.stdin); [print(x['path']) for x in d.get('items',[])]" ; for f in allensdk/brain_observatory/ecephys/_units.py allensdk/brain_observatory/ecephys/_behavior_ecephys_session.py allensdk/brain_observatory/ecephys/ecephys_session_api/ecephys_nwb_session_api.py; do echo "== $f"; curl -sL https://raw.githubusercontent.com/AllenInstitute/AllenSDK/a56bd8ea7613a812334602b64746cdd30c325a96/$f | grep -n "filter_by_validity\|== \"good\"\|== 'good'\|quality" | head -10; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL https://raw.githubusercontent.com/AllenInstitute/AllenSDK/a56bd8ea7613a812334602b64746cdd30c325a96/allensdk/brain_observatory/ecephys/ecephys_session_api/ecephys_nwb_session_api.py | sed -n 125,175p; curl -sL https://raw.githubusercontent.com/AllenInstitute/AllenSDK/a56bd8ea7613a812334602b64746cdd30c325a96/allensdk/brain_observatory/ecephys/ecephys_session_api/ecephys_nwb1_session_api.py | grep -n "good\|validity" | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL https://raw.githubusercontent.com/AllenInstitute/AllenSDK/a56bd8ea7613a812334602b64746cdd30c325a96/allensdk/brain_observatory/ecephys/_probes.py | grep -n -B2 -A8 "filter_by_validity" | grep -n "good\|valid\|quality\|def " | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for f in allensdk/brain_observatory/ecephys/probes.py allensdk/brain_observatory/ecephys/_units.py allensdk/brain_observatory/ecephys/units.py; do echo "== $f"; curl -sL https://raw.githubusercontent.com/AllenInstitute/AllenSDK/a56bd8ea7613a812334602b64746cdd30c325a96/$f | grep -n "filter_by_validity\|good" | head -8; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='illusion.py'; s=open(p).read()
s=s.replace('''                     blank_trials=r["counts_per_code"].get(0),''','''                     first_slot=r["first_slot"], blank_trials=r["counts_per_code"].get(0),''')
def ins(before, text):
    global s
    assert before in s, before[:60]
    s=s.replace(before, "# %% [md]\n"+text.strip()+"\n\n"+before, 1)
ins('''# %% [md]
## illusion-fig1c-isomap-geometry''', '''**Result: reproduced.** Session sub-630506 is in the dandiset with an ICwcfg1 block whose 12 stimuli with 400 repeats are the 11 image codes 1 to 7 and 10 to 13 and the Blank trials (code 0 in a trial slot), as the code expects; Ic1, Lc1, Tre1 and Tre2 (codes 3, 4, 10, 11) are among them; and it has 75 V1 units (22 by the Allen quality criteria). The dandiset names no code: the names come from the code's map, and the templates drawn above agree with it in kind (codes 8 to 13 carry a real bar, 14 to 21 a single inducer at the named corner, pointing in or out). All 11 subjects of the code are present, and a twelfth session (sub-619293) is in the dandiset but not in the code's list. Every session has 400 Blank trials and 12 stimuli with 400 repeats.''')
ins('''# %% [md]
## illusion-fig3a-orthogonal-variance-example''', '''**Result: reproduced.** Among Ic1, Lc1 and Tre1 in sub-630506, at slope 0 the largest strongly connected component has 1 member (no overlap between the three), as-is it has all 3, and the mean directed overlap is 0.000 at slope 0, 0.221 as-is and 0.318 at slope 2. All three tests hold in every reading: the N-neuron space and the 2D Isomap coordinates, the Methods and the code thresholds, all VISp units and the units passing the quality criteria (in the 2D Isomap of the quality units the slope-0 component has 2 members, still fewer than 3). Over the other sessions (variant), all three tests hold in 9 of 12; in the other 3 the three stimuli still overlap at slope 0, while the overlap rises with slope in all 12.''')
ins('''# %% [md]
## illusion-geometry-similar-across-datasets''', '''**Result: reproduced.** In sub-630506 the geodesic distance from Lc1 to Ic1 (60.0) is larger than to Tre2 (17.6), and the orthogonal variance of Lc1 toward Ic1 (0.0270) is larger than toward Tre2 (0.0161). The same holds with the quality units (40.1 against 25.8; 0.0436 against 0.0295). Over all 132 ordered pairs of the 12 stimuli the Spearman correlation between geodesic distance and orthogonal variance is weakly positive and not significant (0.150, p = 0.086; 0.163, p = 0.061 with the quality units).''')
s += '''
# %% [md]
**Result: reproduced.** Across the 12 sessions, the mean effective dimensionality falls from 0.242 at slope 0 to 0.081 at slope 1 and 0.033 at slope 2 (as-is 0.073), and the mean overlap rises from 0.148 to 0.403 and 0.606 (as-is 0.433), in every 0.1 step; slopes 0 and 2 differ from as-is by the Wilcoxon signed-rank test (p = 0.0005 each). The same holds in each of the 12 sessions and with the quality units. These are the directions the paper reports for Figures 1D and 2A of the natural scenes data.

# %% [md]
## Summary

| Claim | Outcome | Rests on |
|---|---|---|
| illusion-data-link | reproduced | the code's names for the image codes (the dandiset has none); Blank trials recovered from the trial sequence |
| illusion-fig1c-isomap-geometry | reproduced | every reading |
| illusion-fig3a-orthogonal-variance-example | reproduced | every reading |
| illusion-geometry-similar-across-datasets | reproduced | every reading |

How the analysis differs from the paper's: the paper's code read a post-processed MATLAB copy of the dandiset ("v240130") that is not public. Here the counts are made from the NWB spike times, and the Blank trials are recovered from the alternation of trials and gray inter-trial frames. The code applies no unit filter, and the quality-filtered units are run as a second reading. The claims on the 2D Isomap picture are judged with the paper's overlap and connectivity measures, as the claims file sets out.

What was found about the dataset: the ICwcfg1 table lists every 400 ms frame, including the inter-trial gray frames, which show the same image as the Blank stimulus (template 0), under one column `frame`. Nothing marks which gray frames are Blank trials, and the image codes have no names. The trial structure can be recovered: 60 leading gray frames, then trials and gray frames alternating, with 400 Blank trials in every session. The spikes share the clock of the table: the V1 response rises 75 ms after image onsets and not after Blank onsets, and the image identity is decodable from the 400 ms after onset (0.576, chance 0.083) and not from the 400 ms before (0.089). The units table describes none of its columns ("no description"). No session is deposited twice. Twelve sessions hold the block; the paper's code lists 11 and leaves out sub-619293.
'''
open(p,'w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cp entries/kim-2025/kim2025.py work/ && python nbgen.py illusion.py work/ill.ipynb && cd work && python -c "
import nbformat, nbclient
nb=nbformat.read('ill.ipynb',4)
c=nbclient.NotebookClient(nb, timeout=3000, kernel_name='python3', resources={'metadata':{'path':'.'}})
try: c.execute()
finally: nbformat.write(nb,'ill_out.ipynb')
" 2>&1 | grep -v WARNING | tail -3; python3 -c "
import json
nb=json.load(open('ill_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    if i<4: continue
    print('=== cell',i, c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text'])[:2500])
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
" | grep -v "Warning\|_fit_transform\|_set_intXint"; python3 -c "
import json
nb=json.load(open('$TMPDIR/work/ill_out.ipynb'))
print(''.join(nb['cells'][3]['outputs'][0]['text'])[:2500])"
```

```
23 cells
=== cell 5 ['sanity']
example session, rate (spikes/s/unit) before onset 5.35; peak after image onset 10.99 at 85 ms; Blank trials peak 4.91
first 10 ms bin above half the peak response: 75 ms after onset
plotted range: image 3.98 to 10.99, blank 4.09 to 6.29

=== cell 6 ['sanity']
window shifted by +0.0 s: 12-way LDA accuracy 0.576 (chance 0.083)

window shifted by -0.4 s: 12-way LDA accuracy 0.089 (chance 0.083)

=== cell 8 ['claim:illusion-data-link']
ICwcfg1 table description: Presentation times and stimuli details for 'ICwcfg1' stimuli. 
Note: image_name references control_description in stimulus/templates

stimulus_name values: [np.str_('ICwcfg1')]
columns: ['frame', 'id', 'start_time', 'stimulus_block', 'stimulus_index', 'stimulus_name', 'stop_time', 'tags', 'tags_index', 'timeseries', 'timeseries_index']

(i) sub-630506 present: True | ICwcfg1 block present | stimuli with 400 repeats: 12 ['Blank', 'X', 'Tc1', 'Ic1', 'Lc1', 'Tc2', 'Lc2', 'Ic2', 'Tre1', 'Tre2', 'Xre1', 'Xre2']
(ii) Ic1, Lc1, Tre1, Tre2 among them: True (codes 3, 4, 10, 11 by the code's map)
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='illusion.py'; s=open(p).read()
old='''the mean effective dimensionality falls from 0.242 at slope 0 to 0.081 at slope 1 and 0.033 at slope 2 (as-is 0.073), and the mean overlap rises from 0.148 to 0.403 and 0.606 (as-is 0.433)'''
new='''the mean effective dimensionality falls from 0.243 at slope 0 to 0.081 at slope 1 and 0.033 at slope 2 (as-is 0.073), and the mean overlap rises from 0.142 to 0.398 and 0.603 (as-is 0.429)'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)

p='allen.py'; s=open(p).read()
def ins(before, text):
    global s
    assert before in s, before[:70]
    s=s.replace(before, "# %% [md]\n"+text.strip()+"\n\n"+before, 1)
ins('''# %% [md]
## fig1b-across-neuron-slope-near-1 and fig1b-across-stimulus-slope''', '''AllenSDK, through which the paper read these data, keeps only units whose `quality` label is "good" in its default units table (`filter_by_validity=True`; allensdk/brain_observatory/ecephys/probes.py, lines 128 to 129, at commit a56bd8ea7613a812334602b64746cdd30c325a96), on top of the three criteria the Methods name. The NWB files hold all units with the label, so both readings are shown.

**Result: reproduced, resting on the AllenSDK reading of the unit selection.** Two of 32 sessions have more than 10% of trials silent in all V1 units (indices 0 and 9 here, the first and seventh by session id, which is how AllenSDK orders them; the code drops indices 0 and 6), leaving 30 sessions of 30 mice, each with 119 stimuli (3570 fits). With the Methods' three criteria alone there are 71.1 +- 27.1 V1 units per session (14 to 113), 2133 in all: the mean and the total are outside their tolerances (57.6 to 70.4; 1728 to 2112). Also requiring the label "good", as AllenSDK does by default, gives 66.9 +- 25.5 (14 to 112), 2008 in all, every value within tolerance.''')
ins('''# %% claim:fig1b-across-stimulus-slope''', '''**Result (fig1b-across-neuron-slope-near-1): reproduced, resting on the AllenSDK reading of the unit selection.** With the units AllenSDK serves (quality criteria and label "good") the 3570 across-neuron slopes have mean 1.0489 (SEM 0.0011) and SD 0.0665, within 1.048 +- 0.001 and 0.07 +- 0.007. With the Methods' three criteria alone the mean is 1.0552 (SEM 0.0011), outside the tolerance, and the SD 0.0655 is within it. The slopes lie between 0.605 and 1.381.''')
ins('''# %% [md]
## figs2-behavioral-state''', '''**Result (fig1b-across-stimulus-slope): reproduced.** The 2133 across-stimulus slopes have mean 1.134 and SD 0.206 (expected 1.13 +- 0.21 and 0.21 +- 0.021), larger than the across-neuron slopes in mean (1.134 against 1.055) and median (1.149 against 1.058), and the two-sided rank-sum test gives p = 5e-105. These use the Methods' three unit criteria; the "good" reading was not run for this claim.''')
ins('''# %% [md]
## figs3-higher-visual-areas''', '''**Result: reproduced.** Moving trials (44.6% of trials) give lower slopes than stationary ones (medians 0.999 against 1.067, rank-sum p = 1.5e-303). Over the 25 included sessions with eye tracking, the largest pupil tertile has the lowest median slope (1.039, against 1.077 and 1.053), Kruskal-Wallis p = 2e-46 with pooled tertiles (per-session tertiles, 1.043 against 1.075 and 1.053, p = 3e-42). Every state's median slope lies between 0.9 and 1.1. Five included sessions have no eye tracking, and 10.5% of trials in the others have no pupil value.''')
ins('''# %% [md]
## Measures under slope manipulation''', '''**Result: reproduced.** Over all 32 sessions, the sessions with at least two quality units are LM 24, RL 28, AL 24, PM 20 and AM 26, each within tolerance of 24, 27, 24, 20 and 26, and the median slopes are 1.058, 1.061, 1.046, 1.004 and 1.026, all between 0.9 and 1.1 (V1 1.063). Over the 30 included sessions the counts are 22, 26, 23, 18 and 25 and the medians again lie between 0.9 and 1.1.''')
ins('''# %% [md]
## fig1d-dimensionality-falls-with-slope''', '''**Result: reproduced.** Over the 30 sessions, every stimulus's pairwise noise correlations at slopes 0, 1 and 2 equal the as-is values to within 7.3e-15, and the fraction of variance on the first principal component differs from as-is for every stimulus at slopes 0 and 2 (pooled mean 0.160 at slope 0 and 0.505 at slope 2, against 0.333 as-is).''')
ins('''# %% [md]
## figs5c-space-occupancy-peak''', '''**Result: reproduced.** The mean effective dimensionality falls at every 0.1 step from 0.282 at slope 0 to 0.124 at slope 1 and 0.061 at slope 2 (as-is 0.120); slopes 0 and 2 differ from as-is by the Wilcoxon signed-rank test (p = 1.9e-09 each).''')
ins('''# %% [md]
## fig2a-overlap-rises-with-slope and fig2c-continuity-from-slope-1''', '''**Result: reproduced.** The mean count of occupied unit voxels peaks at slope 0.8 (5949.9), within both windows, and is lower at slope 0 (5674.3) and slope 2 (340.7) than as-is (5949.9), with p = 1.7e-06 for each. The measure is at its ceiling near the peak: in 28 of 30 sessions every as-is trial occupies a voxel of its own, and the maximum is shared by more than one slope, so the peak at 0.8 marks the middle of a plateau that runs from about 0.7 to 1.0.''')
ins('''# %% claim:fig2c-continuity-from-slope-1''', '''**Result (fig2a-overlap-rises-with-slope): reproduced.** The mean overlap over ordered pairs of distinct stimuli rises at every 0.1 step from 0.062 at slope 0 to 0.276 at slope 1 and 0.425 at slope 2 (as-is 0.286), with p = 1.9e-09 for slopes 0 and 2 against as-is. The code's variant (its threshold, the full matrix with the diagonal) gives 0.047, 0.222 and 0.321 (p = 1.9e-09 and 3.2e-07), also rising at every step.''')
ins('''# %% [md]
## fig3bc-geodesic-orthogonal-correlation, fig3d, fig3e, fig3f''', '''**Result (fig2c-continuity-from-slope-1): reproduced.** The mean size of the largest strongly connected component first reaches 119 at slope 1.1 (Methods threshold; 1.2 with the code's threshold), inside both windows; at slope 0 it is 107.2 (103.0) and differs from as-is (118.9, 29 of 30 sessions complete) with p = 5.7e-05 (4.0e-05). The number of sessions whose component covers all stimuli grows from 9 at slope 0 to 29 at slope 1 and 30 from 1.1.''')
ins('''# %% claim:fig3d-correlation-peaks-near-1''', '''**Result (fig3bc-geodesic-orthogonal-correlation): reproduced.** The as-is Spearman correlation between inter-centroid geodesic distance and orthogonal variance over the 14042 ordered pairs is positive in all 30 sessions (mean 0.323, 0.034 to 0.558), and the one-sided Wilcoxon test against 0 gives p = 9.3e-10.''')
ins('''# %% claim:fig3e-local-alignment-peaks-near-1''', '''**Result (fig3d-correlation-peaks-near-1): reproduced.** The mean correlation peaks at slope 1.2 (0.330), inside both windows; it is lower at slope 0 (0.223) and slope 2 (0.305) than as-is (0.323), with p = 2.6e-07 and 0.011.''')
ins('''# %% claim:fig3f-global-alignment-peaks-near-1''', '''**Result (fig3e-local-alignment-peaks-near-1): reproduced.** Mean local alignment peaks at slope 1.0 (0.830); slope 0 (0.728) and slope 2 (0.804) are lower than as-is (0.830), p = 1.0e-06 and 0.0047. With the neighbour taken from the slope-changed data (variant) the peak is also at 1.0.''')
ins('''# %% [md]
## fig4a, fig4c, fig4d, fig4e, figs6''', '''**Result (fig3f-global-alignment-peaks-near-1): reproduced.** Mean global alignment peaks at slope 1.1 (0.844); slope 0 (0.697) and slope 2 (0.806) are lower than as-is (0.844), p = 8.0e-08 and 0.00046.''')
ins('''# %% claim:fig4c-rsm-similarity-within-mice''', '''**Result (fig4a-overlap-consistency-within-mice): reproduced.** The mean Spearman correlation between the overlap matrices of two random halves of the neurons peaks at slope 0.9 (0.650, with 0.650 at 1.0); slope 0 (0.419) and slope 2 (0.369) are lower than as-is (0.643), p = 1.9e-09 each. The off-diagonal variant also peaks at 0.9. Only the claim's seed was run for this measure.''')
ins('''# %% claim:fig4d-overlap-consistency-across-mice''', '''**Result (fig4c-rsm-similarity-within-mice): reproduced.** The mean half-split RSM correlation peaks at slope 1.1 (0.448); slope 0 (0.418) and slope 2 (0.231) are lower than as-is (0.471), p = 1.2e-04 and 3.5e-08. The as-is value is higher than at any changed slope. Under the four further seeds the peak is at 1.1 each time (seed check below).''')
ins('''# %% claim:fig4e-rsm-similarity-across-mice''', '''**Result (fig4d-overlap-consistency-across-mice): reproduced.** Over the 435 session pairs, the mean Spearman correlation between overlap matrices peaks at slope 1.2 (0.431); slope 0 (0.248) and slope 2 (0.352) are lower than as-is (0.412), p = 5.7e-70 and 6.3e-31. The off-diagonal variant also peaks at 1.2.''')
ins('''# %% claim:figs6-higher-areas-consistency''', '''**Result (fig4e-rsm-similarity-across-mice): reproduced.** Over the 435 session pairs the mean RSM correlation peaks at slope 1.1 (0.397); slope 0 (0.356) and slope 2 (0.185) are lower than as-is (0.406), p = 1.9e-51 and 3.3e-72. The as-is value is higher than at any changed slope. Under the four further seeds the peak is at 1.1 each time.''')
ins('''# %% [md]
### Seed check for the RSM-based results (fig4c, fig4e, figs6)''', '''**Result (figs6-higher-areas-consistency): reproduced under reading (a).** For LM and PM, within sessions (S6B; 22 and 18 sessions) and across session pairs (S6C; 231 and 153 pairs), the mean at slope 1 lies within one SEM of the curve's maximum in all four panels (reading a). Under reading (b) the maximum lies in the window only across pairs (LM 1.2, PM 1.0); within sessions the curves are nearly flat from slope 0 to 1.1 and peak at 0.3 (LM) and 0.4 (PM). Reading (a) holds in all four panels under every seed checked below.''')
ins('''# %% [md]
## Timing that blocks fig2b-decoding-falls-with-slope (and figs4c-shuffling-alters-dependence)''', '''**Result: partially reproduced.** Of the 26 Functional Connectivity sessions, none has an incomplete repeat of the movie and 2 have no V1 units, so 24 are used where the paper used 23 (the expected count is exact); each gives 75 bins. The 1800 pooled slopes have median 1.131: outside 0.9 to 1.1 (reading 1) and inside 0.85 to 1.15 (reading 2), so the slope is near 1 under one of the criterion's readings, while the session count differs by one.''')
s += '''
# %% [md]
**Result (fig2b-decoding-falls-with-slope): blocked, too large.** One decoding (10 folds) takes 11 s as-is and 108 s at slope 2 in one session, so the 660 session-conditions of Figure 2B would need 2.0 to 19.8 CPU hours, 30 to 297 minutes on the runner's 4 CPUs, over the sixty-minute limit of a notebook; Figure S4C (figs4c-shuffling-alters-dependence) repeats it on shuffled data.

# %% [md]
## Summary

All claims here are `data: elsewhere`: they are tested on the Allen data as deposited in dandisets 000021 and 000022, not on dandiset 000248.

| Claim | Outcome |
|---|---|
| data-v1-units | reproduced (assumed: AllenSDK's default "good" unit label) |
| fig1b-across-neuron-slope-near-1 | reproduced (same assumption) |
| fig1b-across-stimulus-slope | reproduced |
| figs2-behavioral-state | reproduced |
| figs3-higher-visual-areas | reproduced |
| figs4ab-noise-correlation-under-manipulation | reproduced |
| fig1d-dimensionality-falls-with-slope | reproduced |
| figs5c-space-occupancy-peak | reproduced |
| fig2a-overlap-rises-with-slope | reproduced |
| fig2c-continuity-from-slope-1 | reproduced |
| fig3bc-geodesic-orthogonal-correlation | reproduced |
| fig3d-correlation-peaks-near-1 | reproduced |
| fig3e-local-alignment-peaks-near-1 | reproduced |
| fig3f-global-alignment-peaks-near-1 | reproduced |
| fig4a-overlap-consistency-within-mice | reproduced |
| fig4c-rsm-similarity-within-mice | reproduced |
| fig4d-overlap-consistency-across-mice | reproduced |
| fig4e-rsm-similarity-across-mice | reproduced |
| figs6-higher-areas-consistency | reproduced (reading a) |
| figs5a-movie-slope-near-1 | partially reproduced |
| fig2b-decoding-falls-with-slope | blocked, too large |
| figs4c-shuffling-alters-dependence | blocked, too large (depends on fig2b) |
| figs1-gain-variance, fig2d-tangent-angle-rises-below-1 | blocked (not run in this attempt; see the record) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the data are read from the DANDI copies of the Allen release with h5py, not through AllenSDK. The units follow the Methods' three quality criteria in every analysis; AllenSDK's default also drops units not labelled "good" (125 of 2133 V1 units), which is shown as a reading for the two counting claims only. The slope fits, slope changes, overlap, geodesic distances, orthogonal variance, alignment and RSMs follow the claims file and the paper's code at commit ac3300b, including the code's as-is nearest neighbour for local alignment. The random neuron partitions and trial orders use this attempt's seeds, not the code's `np.random.seed(0)` sequence.

What was found about the data: the 32 Brain Observatory 1.1 sessions of dandiset 000021 match the paper's 32, the exclusion rule removes the same two sessions as the paper's code, and the counts of units, sessions per area and slopes match the paper once AllenSDK's "good" label is applied. In dandiset 000022, 24 of 26 sessions have V1 units and complete movie repeats, one more than the paper's 23. The pupil area in `filtered_gaze_mapping` is labelled "Pixels ^ 2" but holds values near 0.002 to 0.01. Five of the 30 included sessions have no eye tracking.
'''
open(p,'w').write(s)
EOF
date -u
```

```
Sun Nov 22 01:16:23 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='allen.py'; s=open(p).read()
old='''The pupil area in `filtered_gaze_mapping` is labelled "Pixels ^ 2" but holds values near 0.002 to 0.01.'''
new='''The pupil area in `filtered_gaze_mapping` is labelled "Pixels ^ 2" but holds values of the order of 0.001 (pooled tertile edges 0.0016 and 0.0026), too small for an area in pixels.'''
assert old in s; s=s.replace(old,new)
old='''and the counts of units, sessions per area and slopes match the paper once AllenSDK's "good" label is applied.'''
new='''the sessions per higher visual area match the paper, and the V1 unit counts and the across-neuron slope match it once AllenSDK's "good" label is applied.'''
assert old in s; s=s.replace(old,new)
old='''print(f"pupil: {len(pup)} included sessions with eye tracking; trials without a pupil value {np.isnan(allp).mean():.3f}; pooled tertile edges {edges.round(1)} pixels^2")'''
new='''print(f"pupil: {len(pup)} included sessions with eye tracking; trials without a pupil value {np.isnan(allp).mean():.3f}; "
      f"pooled tertile edges {edges[0]:.4f} and {edges[1]:.4f}; range {np.nanmin(allp):.4g} to {np.nanmax(allp):.4g} (labelled pixels^2)")'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
. kenv/bin/activate && E=entries/kim-2025 && python nbgen.py illusion.py $E/reproduce_kim_2025.ipynb && python nbgen.py allen.py $E/reproduce_kim_2025_allen.ipynb && cat > $E/requirements.in <<'EOF'
dandi
h5py
matplotlib
networkx
numpy
pandas
remfile
scikit-learn
scipy
EOF
cat > $E/entry.yaml <<'EOF'
schema_version: 1
name: kim-2025
type: reproduction
title: Trial-to-trial variability geometry in mouse V1 (Kim and Shin 2025)
description: Tests Kim and Shin (2025) on dandiset 000248, the Allen OpenScope Illusion data the
  paper uses for its Isomap pictures, and, as data elsewhere, on the Allen Visual Coding
  Neuropixels sessions of its main analyses, as deposited in dandisets 000021 and 000022. It
  changes the slope of the log-mean against log-variance relation of V1 spike counts by
  rescaling residuals and measures manifold overlap, continuity, dimensionality, geodesic
  geometry, alignment and representational consistency.
license: Apache-2.0
notebooks:
- path: reproduce_kim_2025.ipynb
  title: Kim and Shin (2025) on dandiset 000248 (Illusion data)
  runtime_minutes: 9
- path: reproduce_kim_2025_allen.ipynb
  title: Kim and Shin (2025) on the Allen Visual Coding Neuropixels data (dandisets 000021 and 000022)
  runtime_minutes: 45
helpers:
- kim2025.py
related:
- id: dandi:000248/0.240502.2344
  relation: uses_data
- id: dandi:000021/0.251116.2246
  relation: uses_data
- id: dandi:000022/0.251116.2247
  relation: uses_data
- id: doi:10.1101/2025.06.30.662469
  relation: reproduces
EOF
cat entries/../../../encore/entries/fouke-2025/README.md 2>/dev/null | head -30; cat entries/fouke-2025/README.md | head -30
```

```
23 cells
66 cells
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
[... 12 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/kim-2025/README.md",
 "content": "# Kim & Shin (2025) from dandiset 000248, with the Allen Visual Coding data\n\nTests the findings of [Kim & Shin (2025)](https://doi.org/10.1101/2025.06.30.662469) on\n[DANDI:000248](https://dandiarchive.org/dandiset/000248/0.240502.2344), the Allen OpenScope\nIllusion recordings the paper uses for its Isomap pictures (`reproduce_kim_2025.ipynb`). The\npaper's main analyses use the Allen Visual Coding Neuropixels sessions; those claims are tested,\nas data elsewhere, on the copies in [DANDI:000021](https://dandiarchive.org/dandiset/000021/0.251116.2246)\nand [DANDI:000022](https://dandiarchive.org/dandiset/000022/0.251116.2247)\n(`reproduce_kim_2025_allen.ipynb`).\n\n| Claim | Data | Outcome |\n|---|---|---|\n| Dandiset 000248 holds the Illusion block, stimuli and units the paper's code uses | 000248 | Reproduced |\n| Isomap manifolds: discontinuous at slope 0, overlapping at slope 2 | 000248 | Reproduced |\n| Orthogonal variance of Lc1 larger toward faraway Ic1 than nearby Tre2 | 000248 | Reproduced |\n| Geometry changes with slope as in the natural scenes data | 000248 | Reproduced |\n| Unit and session counts; across-neuron slope near 1 | elsewhere | Reproduced (assumed AllenSDK unit label) |\n| Across-stimulus slope, behavioural state, higher visual areas | elsewhere | Reproduced |\n| Noise correlations, dimensionality, occupancy, overlap, continuity | elsewhere | Reproduced |\n| Geodesic and orthogonal variance, local and global alignment | elsewhere | Reproduced |\n| Representational consistency within and across mice, LM and PM | elsewhere | Reproduced |\n| Natural movie slope near 1 | elsewhere | Partially reproduced |\n| Decoding, and its change with shuffling | elsewhere | Blocked: too large |\n| Gain variance, tangent space angle | elsewhere | Blocked: not run |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/kim-2025-01.yaml`](../../attempts/kim-2025-01.yaml).\n"
}
```

```
File created successfully at: entries/kim-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py lock entries/kim-2025 2>&1 | tail -5 && python tools/entry.py check entries/kim-2025 2>&1 | tail -20; date -u
```

```
wrote kim-2025/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
Sun Nov 22 01:16:56 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/kim-2025 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-kim-2025 in executed/kim-2025/.venv/share/jupyter/kernels/registry-kim-2025
0 error(s)
pass  reproduce_kim_2025.ipynb  (525 s)
pass  reproduce_kim_2025_allen.ipynb  (2689 s)
Sun Nov 22 02:10:43 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/kim-2025/; cd executed/kim-2025 && python3 -c "
import json
for nbn in ['reproduce_kim_2025.ipynb','reproduce_kim_2025_allen.ipynb']:
    nb=json.load(open(nbn))
    for i,c in enumerate(nb['cells']):
        if c['cell_type']!='code': continue
        for o in c.get('outputs',[]):
            t=''.join(o.get('text',''))
            if o['output_type']=='error': print('ERROR',nbn,i)
            for l in t.split('\n'):
                if any(k in l for k in ['variant, also','variant, units','pupil:','pooled tertiles','per-session tertiles','sessions with all three','accuracy','first slope','peak_slope','mean largest','pooled slopes','estimate','moving vs','sessions 30']): print(nbn[:22], i, l[:260])
"
```

```
reproduce_kim_2025.ipynb
reproduce_kim_2025_allen.ipynb
result.json
reproduce_kim_2025.ipy 6 window shifted by +0.0 s: 12-way LDA accuracy 0.576 (chance 0.083)
reproduce_kim_2025.ipy 6 window shifted by -0.4 s: 12-way LDA accuracy 0.089 (chance 0.083)
reproduce_kim_2025.ipy 14 sessions with all three tests holding: 9 of 12
reproduce_kim_2025_all 5 session 1, window shifted +0.0 s: 119-way accuracy 0.442 (chance 0.0084)
reproduce_kim_2025_all 5 session 1, window shifted +2.0 s: 119-way accuracy 0.009 (chance 0.0084)
reproduce_kim_2025_all 7 sessions 30 (of 32); V1 units per session mean 71.1, SD 27.1 (ddof 1; ddof 0 26.6), range 14 to 113, total 2133; stimuli per session {119}; fits 3570
reproduce_kim_2025_all 7 variant, also requiring the units table's quality label 'good': mean 66.9, SD 25.5, range 14 to 112, total 2008
reproduce_kim_2025_all 10 variant, units also labelled 'good': n 3570, mean 1.0489, SEM 0.0011, SD 0.0665
reproduce_kim_2025_all 15 moving vs stationary: medians 0.9990 vs 1.0667; Mann-Whitney two-sided p = 1.52e-303
reproduce_kim_2025_all 15 pupil: 25 included sessions with eye tracking; trials without a pupil value 0.105; pooled tertile edges 0.0016 and 0.0026; range 0.000188 to 0.01165 (labelled pixels^2)
reproduce_kim_2025_all 15 pooled tertiles (code): fits per tertile {0: 2228, 1: 2521, 2: 2116}, median slope per tertile {0: 1.0769, 1: 1.0528, 2: 1.0394}, largest tertile lowest: True, Kruskal-Wallis p = 1.96e-46, medians in 0.9-1.1: True
reproduce_kim_2025_all 15 per-session tertiles (variant): fits per tertile {0: 2975, 1: 2974, 2: 2975}, median slope per tertile {0: 1.0745, 1: 1.053, 2: 1.0427}, largest tertile lowest: True, Kruskal-Wallis p = 2.73e-42, medians in 0.9-1.1: True
reproduce_kim_2025_all 29 occupied unit voxels (n = 30 sessions): {'peak_slope': 0.8, 'peak_mean': np.float64(5949.9), 'mean_asis': np.float64(5949.9333), 'mean_slope0': np.float64(5674.3333), 'mean_slope1': np.float64(5946.7), 'mean_slope2': np.float64(340.7333), 'p_
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='allen.py'; s=open(p).read()
old='''**Result (fig2b-decoding-falls-with-slope): blocked, too large.** One decoding (10 folds) takes 11 s as-is and 108 s at slope 2 in one session, so the 660 session-conditions of Figure 2B would need 2.0 to 19.8 CPU hours, 30 to 297 minutes on the runner's 4 CPUs, over the sixty-minute limit of a notebook; Figure S4C (figs4c-shuffling-alters-dependence) repeats it on shuffled data.'''
new='''**Result (fig2b-decoding-falls-with-slope): blocked, too large.** One decoding (10 folds) takes about 11 s as-is and about 110 s at slope 2 in one session (the exact times printed above vary from run to run), so the 660 session-conditions of Figure 2B would need about 2 to 20 CPU hours, about 30 to 300 minutes on the runner's 4 CPUs, over the sixty-minute limit of a notebook; Figure S4C (figs4c-shuffling-alters-dependence) repeats it on shuffled data.'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
. kenv/bin/activate && python nbgen.py allen.py entries/kim-2025/reproduce_kim_2025_allen.ipynb; ls questions/ | head -3; ls schemas/
```

```
66 cells
README.md
asari-2009.yaml
ashworth-2025.yaml
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']
print(json.dumps(o.get('properties',{}),indent=0)[:2500]); print(o.get('required'))
print(s.get('required')); print(list(s['properties'].keys()))
print(json.dumps(s['properties']['findings'],indent=0)[:1500])
print(json.dumps(s['properties'].get('missing_datasets',{}))[:300])
print(json.dumps(s['properties']['inputs'])[:600])
"
```

```
{
"claim": {
"description": "Claim id from the target's claims file.",
"type": "string"
},
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
],
"description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
},
"blocked_by": {
"description": "Required when outcome is blocked.",
"enum": [
"data_missing",
"metadata_insufficient",
"methods_underspecified",
[... 136 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/kim-2025-01.yaml",
 "content": "schema_version: 3\nid: kim-2025-01\ndatasets:\n- archive: dandi\n  id: \"000248\"\n  version: 0.240502.2344\n  doi: 10.48324/dandi.000248/0.240502.2344\n  relation: reuses\npaper: doi:10.1101/2025.06.30.662469\ndate: 2026-11-21\nentry: kim-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44962565814\ninputs:\n- what: Allen Brain Observatory Visual Coding Neuropixels, Brain Observatory 1.1 sessions (32 session\n    files, natural scenes, units, running speed and pupil area), the paper's main dataset, for the\n    claims with data elsewhere. Streamed at the pinned version, the only published one.\n  source: doi:10.48324/dandi.000021/0.251116.2246\n- what: Allen Brain Observatory Visual Coding Neuropixels, Functional Connectivity sessions (26 session\n    files, natural movie one), for figs5a-movie-slope-near-1. Streamed at the pinned version, the only\n    published one.\n  source: doi:10.48324/dandi.000022/0.251116.2247\n- what: The paper's analysis code, for method details the claims file and the Methods leave open\n    (names of the Illusion image codes, the example session, slope manipulation, overlap, geodesic\n    distance, orthogonal variance, alignment, RSM and decoding procedures).\n  source: https://github.com/jhk4839/Neural_variability_robustness at commit\n    ac3300b007c2348ccda73c0c87fb02f557791089\n- what: AllenSDK's default unit filter (units with quality label \"good\" only, filter_by_validity), the\n    software through which the paper read the Allen data, for the unit selection of data-v1-units and\n    fig1b-across-neuron-slope-near-1.\n  source: https://github.com/AllenInstitute/AllenSDK at commit a56bd8ea7613a812334602b64746cdd30c325a96\n    (allensdk/brain_observatory/ecephys/probes.py, lines 128 to 129)\noutcomes:\n- claim: illusion-data-link\n  outcome: reproduced\n  notebook: reproduce_kim_2025.ipynb\n  output: claim:illusion-data-link\n  notes: Session sub-630506 (the code's index 6) is in the dandiset with an ICwcfg1 block. Its trial\n    slots hold 12 stimuli with 400 repeats, the image codes 1 to 7 and 10 to 13 and 400 Blank trials,\n    as the code expects (num_trial_types 12). Codes 3, 4, 10 and 11 (Ic1, Lc1, Tre1, Tre2 by the\n    code's map) are among them, and the session has 75 V1 units (22 by the Allen quality criteria). The\n    dandiset names no image code; the 22 templates drawn in the notebook agree in kind with the\n    code's names (codes 8 to 13 carry a real bar, 14 to 21 one inducer at the named corner, in or out),\n    which cannot tell the variants 1 and 2 apart. All 11 subjects of the code are present, each with\n    12 stimuli of 400 repeats; a twelfth session, sub-619293, is in the dandiset and not in the code's\n    list.\n  deviations:\n  - The Blank trials are not marked in the files. They are recovered as gray frames (code 0) in trial\n    slots, after 60 leading gray frames, from the alternation of trials and gray inter-trial frames;\n    every session then has 400 Blank trials and no image frame outside a trial slot. The code read a\n    post-processed copy (v240130) that is not public.\n- claim: illusion-fig1c-isomap-geometry\n  outcome: reproduced\n  notebook: reproduce_kim_2025.ipynb\n  output: claim:illusion-fig1c-isomap-geometry\n  notes: Among Ic1, Lc1 and Tre1 in sub-630506 (75 V1 units), the largest strongly connected component\n    has 1 member at slope 0 and 3 as-is, and the mean of the six directed overlaps is 0.000 at slope 0,\n    0.221 as-is and 0.318 at slope 2 (N-neuron space, Methods threshold). All three tests hold under\n    every reading run, the N-neuron space and the 2D Isomap coordinates, the Methods and the code's\n    overlap threshold, all VISp units and the 22 quality units (in the 2D Isomap of the quality units\n    the slope-0 component has 2 members). Over all 12 sessions (variant) the three tests hold in 9; in\n    sub-619293, sub-620333 and sub-631570 the three stimuli still overlap at slope 0, while their\n    overlap rises with slope.\n- claim: illusion-fig3a-orthogonal-variance-example\n  outcome: reproduced\n  notebook: reproduce_kim_2025.ipynb\n  output: claim:illusion-fig3a-orthogonal-variance-example\n  notes: In sub-630506 the geodesic distance from Lc1 to Ic1 is 60.0 and to Tre2 17.6; the orthogonal\n    variance of Lc1 is 0.0270 toward Ic1 and 0.0161 toward Tre2 (ratio 1.67). With the 22 quality units,\n    40.1 against 25.8 and 0.0436 against 0.0295. The variant over all 132 ordered stimulus pairs gives a\n    weak Spearman correlation between geodesic distance and orthogonal variance (0.150, p = 0.086; 0.163,\n    p = 0.061 with the quality units).\n- claim: illusion-geometry-similar-across-datasets\n  outcome: reproduced\n  notebook: reproduce_kim_2025.ipynb\n  output: claim:illusion-geometry-similar-across-datasets\n  notes: Over the 12 sessions with an ICwcfg1 block, the mean effective dimensionality falls from 0.243\n    at slope 0 to 0.081 at slope 1 and 0.033 at slope 2 (as-is 0.073), and the mean overlap rises from\n    0.142 to 0.398 and 0.603 (as-is 0.429), at every 0.1 step; slopes 0 and 2 differ from as-is by the\n    Wilcoxon signed-rank test, p = 0.0005 each. The directions hold in each session and with the quality\n    units. The example session alone gives the same directions.\n  deviations:\n  - All 12 sessions of the dandiset are used, including sub-619293, which the paper's code does not list.\n- claim: data-v1-units\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:data-v1-units\n  measured:\n  - 30\n  - 66.9\n  - 25.5\n  - 2008\n  notes: Tested on the DANDI copy of the Allen data (dandiset 000021). Two of 32 sessions have more than\n    10% of natural scenes trials silent in all V1 units (index 0 and 9 in DANDI order, the first and\n    seventh by session id, the order AllenSDK uses; the code drops indices 0 and 6), leaving 30 sessions\n    of 30 mice with 119 stimuli each. With the units AllenSDK serves by default (the three criteria of\n    the Methods and the quality label good) there are 66.9 +- 25.5 V1 units per session, 14 to 112, 2008\n    in all, every value within tolerance. With the three criteria alone, 71.1 +- 27.1, 14 to 113, 2133 in\n    all; the mean and the total are outside their tolerances (57.6 to 70.4, 1728 to 2112) and the SD and\n    range inside.\n  deviations:\n  - Assumed that the paper's units are those of AllenSDK's default units table, which keeps only units\n    labelled good (filter_by_validity, AllenSDK probes.py lines 128 to 129) in addition to the three\n    criteria of the Methods. The paper reads the data through AllenSDK (Methods, Main dataset and visual\n    stimuli; its code's pickles are named allensdk) and states only the three criteria. The two readings\n    give different outcomes; both are shown.\n- claim: fig1b-across-neuron-slope-near-1\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig1b-across-neuron-slope-near-1\n  measured:\n  - 1.0489\n  - 0.0665\n  - 3570\n  notes: With AllenSDK's default units, the 3570 across-neuron slopes have mean 1.0489 (SEM 0.0011) and SD\n    0.0665, within 1.048 +- 0.001 and 0.07 +- 0.007. With the Methods' three criteria alone, mean 1.0552\n    (SEM 0.0011), outside the tolerance, and SD 0.0655, within it. Slopes range from 0.605 to 1.381.\n  deviations:\n  - The same assumption about the unit selection as data-v1-units.\n- claim: fig1b-across-stimulus-slope\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig1b-across-stimulus-slope\n  measured:\n  - 1.1344\n  - 0.2057\n  notes: Over 2133 V1 units (Methods' three criteria), across-stimulus slopes have mean 1.134 and SD 0.206,\n    larger than the across-neuron slopes in mean (1.134 against 1.055) and median (1.149 against 1.058);\n    two-sided Mann-Whitney U test p = 5e-105. No neuron was dropped.\n  deviations:\n  - Units by the Methods' three criteria; the AllenSDK reading with the label good was not run for this\n    claim.\n- claim: figs2-behavioral-state\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:figs2-behavioral-state\n  notes: Moving trials (trial mean speed >= 1 cm/s, 44.6% of trials) give lower across-neuron slopes than\n    stationary ones (medians 0.999 against 1.067, two-sided Mann-Whitney p = 1.5e-303; 3550 and 3264\n    fits). Over the 25 included sessions with eye tracking, pupil tertiles pooled over sessions (code)\n    give medians 1.077, 1.053 and 1.039, the largest tertile lowest, Kruskal-Wallis p = 2e-46; per-session\n    tertiles give 1.075, 1.053 and 1.043, p = 3e-42. All state medians lie in 0.9 to 1.1. Five included\n    sessions have no eye tracking and 10.5% of trials in the others have no pupil value. The pupil area\n    (processing/filtered_gaze_mapping/pupil_area) is labelled Pixels ^ 2 but ranges from 0.0002 to 0.012,\n    which cannot be pixels; the tertiles do not depend on the scale.\n  deviations:\n  - Pupil area is the blink-filtered series of the DANDI files, averaged over the 250 ms window; the\n    Methods say trial mean pupil area without naming the series. Stimulus and state cells with fewer\n    than 2 trials are dropped.\n- claim: figs3-higher-visual-areas\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:figs3-higher-visual-areas\n  measured:\n  - 24\n  - 28\n  - 24\n  - 20\n  - 26\n  notes: Over all 32 sessions, sessions with at least two quality units are LM 24, RL 28, AL 24, PM 20 and\n    AM 26, all within tolerance; median slopes 1.058, 1.061, 1.046, 1.004 and 1.026, all within 0.9 to\n    1.1. Over the 30 included sessions, 22, 26, 23, 18 and 25 sessions, medians also within 0.9 to 1.1.\n  deviations:\n  - A session counts for an area when it has at least two quality units there, the fewest a line can be\n    fitted to; with one unit or more the counts are the same.\n- claim: figs4ab-noise-correlation-under-manipulation\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:figs4ab-noise-correlation-under-manipulation\n  notes: Over 30 sessions, every pairwise noise correlation per stimulus at slopes 0, 1 and 2 equals the\n    as-is value to within 7.3e-15. The fraction of variance on PC1 differs from as-is for every stimulus\n    of every session at slopes 0 and 2 (pooled means 0.160 and 0.505 against 0.333 as-is).\n- claim: fig1d-dimensionality-falls-with-slope\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig1d-dimensionality-falls-with-slope\n  notes: Mean effective dimensionality falls at every 0.1 step, 0.282 at slope 0, 0.124 at slope 1, 0.061\n    at slope 2 (as-is 0.120); slopes 0 and 2 against as-is p = 1.9e-09 each (30 sessions).\n- claim: figs5c-space-occupancy-peak\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:figs5c-space-occupancy-peak\n  notes: The mean number of occupied unit voxels peaks at slope 0.8 (5949.9, of 5950 trials), inside both\n    windows; slope 0 (5674.3) and slope 2 (340.7) are lower than as-is (5949.9), p = 1.7e-06 each. The\n    measure is at its ceiling near the peak; in 28 of 30 sessions every as-is trial has a voxel of its\n    own and the maximum is shared by several slopes, so the peak marks a plateau from about 0.7 to 1.0.\n- claim: fig2a-overlap-rises-with-slope\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig2a-overlap-rises-with-slope\n  notes: Mean overlap over ordered pairs of distinct stimuli rises at every 0.1 step, 0.062 at slope 0,\n    0.276 at slope 1, 0.425 at slope 2 (as-is 0.286); p = 1.9e-09 for slopes 0 and 2 against as-is. The\n    code's variant (its threshold, the full matrix with the diagonal) gives 0.047, 0.222 and 0.321, also\n    rising at every step (p = 1.9e-09 and 3.2e-07).\n- claim: fig2c-continuity-from-slope-1\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig2c-continuity-from-slope-1\n  notes: The mean size of the largest strongly connected component first reaches 119 at slope 1.1 (1.2\n    with the code's threshold), inside both windows; at slope 0 it is 107.2 (103.0), against 118.9 as-is,\n    p = 5.7e-05 (4.0e-05). Sessions with all 119 stimuli connected rise from 9 at slope 0 to 29 at slope 1\n    and 30 from 1.1; 29 of 30 as-is.\n- claim: fig3bc-geodesic-orthogonal-correlation\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig3bc-geodesic-orthogonal-correlation\n  notes: The as-is Spearman correlation over 14042 ordered pairs is positive in all 30 sessions (mean 0.323,\n    0.034 to 0.558); one-sided Wilcoxon against 0 p = 9.3e-10.\n  deviations:\n  - Geodesic distances are the shortest paths of the 5-nearest-neighbour graph of trials and centroids,\n    the step of sklearn's Isomap that the code reads (dist_matrix_), computed without the embedding.\n- claim: fig3d-correlation-peaks-near-1\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig3d-correlation-peaks-near-1\n  notes: The mean correlation peaks at slope 1.2 (0.330); slope 0 (0.223) and slope 2 (0.305) are lower\n    than as-is (0.323), p = 2.6e-07 and 0.011.\n- claim: fig3e-local-alignment-peaks-near-1\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig3e-local-alignment-peaks-near-1\n  notes: Mean local alignment peaks at slope 1.0 (0.830); slope 0 (0.728) and slope 2 (0.804) are lower\n    than as-is (0.830), p = 1.0e-06 and 0.0047. With the neighbour taken from the slope-changed data the\n    peak is also at 1.0.\n  deviations:\n  - The nearest neighbour manifold is taken from the as-is geodesic distances at every slope, as\n    local_global_alignment.py does (lines 168 and 249 at ac3300b); the per-slope neighbour is a variant.\n- claim: fig3f-global-alignment-peaks-near-1\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig3f-global-alignment-peaks-near-1\n  notes: Mean global alignment peaks at slope 1.1 (0.844); slope 0 (0.697) and slope 2 (0.806) are lower\n    than as-is (0.844), p = 8.0e-08 and 0.00046.\n- claim: fig4a-overlap-consistency-within-mice\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig4a-overlap-consistency-within-mice\n  notes: The mean Spearman correlation between the overlap matrices of two random halves of the neurons\n    (10 partitions) peaks at slope 0.9 (0.650; 0.650 at 1.0); slope 0 (0.419) and slope 2 (0.369) are\n    lower than as-is (0.643), p = 1.9e-09 each. The off-diagonal variant also peaks at 0.9.\n  deviations:\n  - Only the claim's seed was run. The four further seeds the protocol asks for would have added about\n    30 minutes on 4 CPUs to a notebook already at 45 minutes; how much the seed matters is not known for\n    this claim. The curve is flat between 0.9 and 1.0 and the windows reach 0.7 and 0.8.\n  - Overlap matrices of the halves use the Methods threshold over distinct pairs.\n- claim: fig4c-rsm-similarity-within-mice\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig4c-rsm-similarity-within-mice\n  notes: The mean half-split RSM correlation peaks at slope 1.1 (0.448); slope 0 (0.418) and slope 2\n    (0.231) are lower than as-is (0.471), p = 1.2e-04 and 3.5e-08. The as-is value exceeds every changed\n    slope. Under the seed plus 1000, 2000, 3000 and 4000 the peak is at 1.1 each time (maximum 0.447 to\n    0.455).\n- claim: fig4d-overlap-consistency-across-mice\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig4d-overlap-consistency-across-mice\n  notes: Over 435 session pairs, the mean Spearman correlation of the full overlap matrices peaks at slope\n    1.2 (0.431); slope 0 (0.248) and slope 2 (0.352) are lower than as-is (0.412), p = 5.7e-70 and\n    6.3e-31. The off-diagonal variant also peaks at 1.2.\n- claim: fig4e-rsm-similarity-across-mice\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:fig4e-rsm-similarity-across-mice\n  notes: Over 435 session pairs, the mean RSM correlation peaks at slope 1.1 (0.397); slope 0 (0.356) and\n    slope 2 (0.185) are lower than as-is (0.406), p = 1.9e-51 and 3.3e-72. The as-is value exceeds every\n    changed slope. Under the four further seeds the peak is at 1.1 each time (maximum 0.397).\n  deviations:\n  - The RSM averages all 1225 unordered pairs of trial indices; the code samples at most 10000, which is\n    all of them. Trial order is randomized within stimulus with the claim's seed, not the code's\n    np.random.seed(0) sequence.\n- claim: figs6-higher-areas-consistency\n  outcome: reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:figs6-higher-areas-consistency\n  notes: Under reading (a) the mean at slope 1 lies within one SEM of the maximum in all four panels (LM\n    and PM, within sessions over 22 and 18 sessions, across 231 and 153 session pairs). Under reading\n    (b) the maximum lies in the window across pairs only (LM 1.2, PM 1.0); within sessions the curves are\n    nearly flat from slope 0 to 1.1 and peak at 0.3 (LM) and 0.4 (PM), so reading (b) holds in 2 of 4\n    panels. Reading (a) holds in all four panels under all five seeds; the within-session LM peak moves\n    between 0.2 and 1.0 with the seed.\n  deviations:\n  - Sessions with at least two quality units in the area are used.\n- claim: figs5a-movie-slope-near-1\n  outcome: partially_reproduced\n  notebook: reproduce_kim_2025_allen.ipynb\n  output: claim:figs5a-movie-slope-near-1\n  measured:\n  - 24\n  - 75\n  notes: Of the 26 Functional Connectivity sessions in dandiset 000022, none has an incomplete movie repeat\n    and 2 have no V1 quality units, so 24 are used where the paper used 23 (expected exactly); each has 75\n    bins. The 1800 pooled slopes have median 1.131, outside 0.9 to 1.1 (reading 1) and inside 0.85 to 1.15\n    (reading 2). The slope holds under one reading of the criterion and the session count differs by one.\n  deviations:\n  - The 60-repeat block of natural movie one is the table natural_movie_one_more_repeats_presentations in\n    these files. Bins run from the onset of their first frame to the end of their twelfth (0.37 to 0.50 s).\n  - The paper's third excluded session could not be identified; the \"good\" label was not applied here.\n- claim: fig2b-decoding-falls-with-slope\n  outcome: blocked\n  blocked_by: too_large\n  notebook: reproduce_kim_2025_allen.ipynb\n  notes: Timed in the notebook on one session; one 10-fold linear SVC decoding takes about 11 s as-is and\n    about 107 s at slope 2, so the 660 session-conditions need about 2 to 20 CPU hours, about 30 to 290\n    minutes on 4 CPUs, over the sixty-minute notebook limit. The four further seeds would multiply it by\n    five.\n- claim: figs4c-shuffling-alters-dependence\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig2b-decoding-falls-with-slope, blocked as too large; the shuffled decoding doubles that\n    computation. The RSM parts were not run separately.\n- claim: figs1-gain-variance\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Not run within this attempt's five-hour limit. The negative binomial fits (poisson_multi_rs.py in\n    the paper's code) were not ported; the data they need, V1 counts of the 30 sessions, are loaded in the\n    notebook.\n- claim: fig2d-tangent-angle-rises-below-1\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Not run within this attempt's five-hour limit. The tangent space angle (tangent_angle.py in the\n    paper's code, points of tangency, local PCA, weighted angle) was not ported; the geodesic neighbours\n    it needs are computed in the notebook.\nfindings:\n- kind: metadata_insufficient\n  severity: major\n  statement: The ICwcfg1 presentations table lists every 400 ms frame of the block, including the gray\n    inter-trial frames, under one column frame. The gray frames show the same image as the Blank stimulus\n    (template 0), and nothing marks which of them are Blank trials. The image codes 0 to 21 have no names\n    in the files or the dandiset metadata; the names come only from the paper's code. The trials can be\n    recovered from the sequence (60 leading gray frames, then trial and gray frame alternating, 400 Blank\n    trials in every session), and the templates agree in kind with the code's names.\n- kind: metadata_insufficient\n  severity: minor\n  statement: The units table describes none of its columns (quality, isi_violations, firing_rate and the\n    others read \"no description\").\n- kind: other\n  about: data\n  severity: none\n  statement: The spikes share the clock of the ICwcfg1 table. The V1 population rate rises 75 ms after image\n    onsets and not after Blank onsets, and the image identity is decoded from the 400 ms after onset\n    (0.576, chance 0.083) and not from the 400 ms before (0.089). No session is deposited twice. All 11\n    sessions the paper's code lists are present, with a twelfth (sub-619293) that it does not list.\n- kind: methods_unavailable\n  statement: The Methods select units by isi_violations, amplitude_cutoff and presence_ratio. The unit counts\n    (64 +- 25, 1920 in all) and the across-neuron slope (1.048) match only when units not labelled good are\n    also dropped, as AllenSDK does by default (filter_by_validity). Question for the authors, were the\n    units those of AllenSDK's default units table? This attempt assumed so for data-v1-units and\n    fig1b-across-neuron-slope-near-1.\n- kind: methods_unavailable\n  statement: The paper excludes 3 of 26 Functional Connectivity sessions for truncated movies or no V1 units.\n    In dandiset 000022 no session has an incomplete repeat of natural movie one and 2 have no V1 quality\n    units. Question for the authors, which was the third session and why was it excluded?\n"
}
```

```
File created successfully at: attempts/kim-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import yaml,re
t=open('attempts/kim-2025-01.yaml').read()
d=yaml.safe_load(t)
print(len(d['outcomes']), {o['outcome'] for o in d['outcomes']})
for i,l in enumerate(t.split('\n')):
    s=l.strip().lstrip('- ')
    m=re.match(r'^[a-z_]+: ',s)
    rest=s[m.end():] if m else s
    if ': ' in rest: print(i+1, l)
c=yaml.safe_load(open('claims/kim-2025.yaml'))
ids=[x['id'] for x in c['claims']]; got=[o['claim'] for o in d['outcomes']]
print(set(ids)-set(got), set(got)-set(ids))
EOF
python tools/entry.py check entries/kim-2025 2>&1 | tail -5; date -u
```

```
28 {'partially_reproduced', 'reproduced', 'blocked'}
set() set()
0 error(s)
Sun Nov 22 02:12:50 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "attempts/\|attempt.schema" tools/entry.py | head -5; ls tools | head -40
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
ls tools | sed -n 40,80p; ls tests | head; grep -rln "attempt.schema" tools tests | head
```

```
transcript.py
test_agent_run.py
test_build_site.py
test_build_targets.py
test_claims_check.py
test_datasets.py
test_encore.py
test_entry_tool.py
test_flagged.py
test_notify.py
test_paper_match.py
tools/build_site.py
tests/test_build_site.py
tests/test_agent_run.py
```

**Agent calls Bash**

```bash
uv run --with jsonschema --with pyyaml python - <<'EOF' 2>&1 | tail -5
import json,yaml
from jsonschema import Draft202012Validator
s=json.load(open('schemas/attempt.schema.json'))
d=yaml.safe_load(open('attempts/kim-2025-01.yaml'))
errs=list(Draft202012Validator(s).iter_errors(d))
for e in errs: print(list(e.path), e.message[:200])
print(len(errs),'errors')
EOF
```

```
If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 24 packages in 1.51s
['date'] datetime.date(2026, 11, 21) is not of type 'string'
1 errors
```

**Agent calls Bash**

```bash
sed -i "s/^date: 2026-11-21$/date: '2026-11-21'/" attempts/kim-2025-01.yaml && grep -n "^date" attempts/kim-2025-01.yaml && python tools/entry.py all entries/kim-2025 2>&1 | tail -5; date -u
```

```
10:date: '2026-11-21'
Installed kernelspec registry-kim-2025 in executed/kim-2025/.venv/share/jupyter/kernels/registry-kim-2025
0 error(s)
pass  reproduce_kim_2025.ipynb  (515 s)
pass  reproduce_kim_2025_allen.ipynb  (2698 s)
Sun Nov 22 03:06:57 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/kim-2025 && python3 -c "
import json
nb=json.load(open('reproduce_kim_2025_allen.ipynb'))
for c in nb['cells']:
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))
        if 'session 1,' in t or 'estimate' in t or o['output_type']=='error': print(t[:400])
nb=json.load(open('reproduce_kim_2025.ipynb'))
print(sum(o['output_type']=='error' for c in nb['cells'] for o in c.get('outputs',[])), 'errors in illusion')
"; cd ../.. && python tools/entry.py handover entries/kim-2025 2>&1 | tail -3; ls executed/kim-2025/handover; git status --short | head; date -u
```

```
session 1, window shifted +0.0 s: 119-way accuracy 0.442 (chance 0.0084)
session 1, window shifted +2.0 s: 119-way accuracy 0.009 (chance 0.0084)

session 1, as-is: accuracy 0.376, 11 s

session 1, slope 2.0: accuracy 0.213, 108 s
estimate for 660 session-conditions: 2.0 to 19.9 CPU hours, 30 to 298 min on 4 CPUs; Figure S4C doubles it with the shuffled data
notebook time 44.9 min

0 errors in illusion
wrote executed/kim-2025/handover
kim-2025.yaml
kim2025.py
reproduce_kim_2025.ipynb
reproduce_kim_2025_allen.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/kim-2025-01.yaml'; s=open(p).read()
old='''    about 107 s at slope 2, so the 660 session-conditions need about 2 to 20 CPU hours, about 30 to 290
    minutes on 4 CPUs, over the sixty-minute notebook limit.'''
new='''    about 108 s at slope 2, so the 660 session-conditions need about 2 to 20 CPU hours, about 30 to 300
    minutes on 4 CPUs, over the sixty-minute notebook limit.'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
git status --short entries attempts executed | head; python tools/entry.py check entries/kim-2025 | tail -1
```

```
?? attempts/kim-2025-01.yaml
?? entries/kim-2025/
0 error(s)
```

**Agent**

I've finished steps 1 to 6: the entry and the attempt record are written, both notebooks pass `entry.py all`, and the handover is built. Nothing is committed.

## 1. Outcome per claim

| Claim | Data | Outcome |
|---|---|---|
| illusion-data-link | 000248 (with_labels) | reproduced |
| illusion-fig1c-isomap-geometry | 000248 | reproduced (every reading) |
| illusion-fig3a-orthogonal-variance-example | 000248 | reproduced |
| illusion-geometry-similar-across-datasets | 000248 | reproduced |
| data-v1-units | elsewhere (000021) | reproduced, rests on an assumption |
| fig1b-across-neuron-slope-near-1 | elsewhere | reproduced, rests on an assumption |
| fig1b-across-stimulus-slope, figs2, figs3, figs4ab, fig1d, figs5c, fig2a, fig2c, fig3bc, fig3d, fig3e, fig3f, fig4a, fig4c, fig4d, fig4e | elsewhere | reproduced |
| figs6-higher-areas-consistency | elsewhere | reproduced under reading (a); reading (b) holds in only 2 of 4 panels |
| figs5a-movie-slope-near-1 | elsewhere (000022) | partially reproduced: 24 sessions where the paper has 23; median slope 1.131 |
| fig2b-decoding-falls-with-slope | elsewhere | blocked, too_large (about 30 to 300 min on 4 CPUs, timed in the notebook) |
| figs4c-shuffling-alters-dependence | elsewhere | blocked, too_large (depends on fig2b) |
| figs1-gain-variance, fig2d-tangent-angle-rises-below-1 | elsewhere | blocked, not_runnable (not ported within the time limit) |

## 2. Dataset, assumptions, questions

**Dataset 000248**, pinned at 0.240502.2344, the only published version:
- The ICwcfg1 table lists every 400 ms frame, including the gray frames between trials. Those gray frames show the same image as the Blank stimulus, and nothing marks which of them are Blank trials. The image codes have no names; I took them from the paper's code (finding rated major).
- The trials can be recovered from the sequence: 60 leading gray frames, then trial and gray frame alternate. Every session then has 400 Blank trials and the 12 stimuli with 400 repeats that the code expects.
- The spikes share the clock of the table: the V1 response rises at 75 ms after image onsets, and decoding gives 0.576 after onset against 0.089 before it.
- The units table columns have no descriptions (minor).
- No session is deposited twice. All 11 subjects the code lists are present, plus a twelfth, sub-619293, that the code does not use.

**Allen data**: I used the DANDI copies, 000021 at 0.251116.2246 and 000022 at 0.251116.2247, as inputs. The exclusion rule drops the same two sessions as the paper's code.

**Assumption**: the paper's V1 units are AllenSDK's default units. That means the three quality criteria the Methods name, plus the "good" label AllenSDK requires by default (checked in `probes.py` at commit a56bd8e). With the label the counts match the paper (66.9 ± 25.5, 2008 units, slope 1.0489). Without it they do not (71.1, 2133 units, slope 1.0552). The other Allen claims use the three criteria alone, which is stated in the record.

**Questions for the paper's authors**, recorded as findings: whether the units are AllenSDK's default set, and which third movie session was excluded.

**Questions to a reader**: none.

## 3. Where the protocol was unclear or did not fit

1. Claims marked "elsewhere" make up most of the paper. Testing 24 of them took most of the run, and the protocol gives no priority between them and the dataset's own claims. I tested all I could and blocked the rest.
2. The rule of five seeds is too costly for fig4a's overlap halves and for the decoding. For fig4a I ran only the claim's seed and recorded it as a deviation; the RSM-based claims ran all five seeds.
3. There is no block reason for "not attempted within the time limit" that is not about the computation's size. I used `not_runnable` for figs1 and fig2d.
4. A finding about an input dataset (000021 pupil area labelled "Pixels ^ 2" but holding values from 0.0002 to 0.012) has no place in the record, since it is not the attempt's dataset. I put it in the claim's notes.
5. The protocol says nothing on whether to apply defaults of the software the paper used to read the data (AllenSDK's "good" filter). I treated it like the paper's code: run both readings, adopt the best-supported one as an assumption.
6. Timings printed in the notebook change from run to run, so a conclusion that quotes them exactly breaks on re-run. I wrote them as approximate values.

## 4. Runtime and failures

- The run took about 3 h 32 min (23:36 to 03:08 UTC).
- Final executed run: Illusion notebook 515 s, Allen notebook 2698 s (about 45 min), peak memory under 2 GB.
- One bug was caught and fixed before the final run. Three sessions start with a Blank trial, and my first trial-slot rule missed it.
- No command failed in the final run.
- Untracked dotfiles (`.bashrc`, `.idea`, and others) show up in the repository root. I did not create them and left them alone.

## End of run

89 turns, 206 minutes, $8.42 at API prices, result: success.
