# zhang-2021 · author · run 43583052040

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

**Agent calls Bash**

```bash
cat README.md docs/design.md docs/archives.md; cat claims/zhang-2021.yaml
```

```
<persisted-output>
Output too large (69.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bwcjzrszk.txt

Preview (first 2KB):
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
[... 21 more lines not kept]
```

```
<persisted-output>
Output too large (55KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bw3ooiyre.txt

Preview (first 2KB):
Sat Nov 14 10:07:03 UTC 2026
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bw3ooiyre.txt"
}
```

```
1	Sat Nov 14 10:07:03 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 1593 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bwcjzrszk.txt"
}
```

```
1	# Encore Science: the registry
2	
3	Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
4	
5	Agents, and people, try to reproduce the key findings of papers from the open
6	data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
7	here: the notebooks when it works, and the reason when it does not.
8	
9	- **For the archive:** evidence of whether each dandiset is complete and
10	  accurate enough to support the findings of its paper.
11	- **For analysts:** working notebooks to build new analyses on.
12	
13	Status: pilot. All eight pilot targets have been attempted and checked by an
14	independent agent.
15	
16	**Dashboard:** <https://encorescience.org/>
17	
18	## Reading the outcomes
19	
20	An outcome says what one attempt could recover from the data in a dandiset,
[... 923 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/zhang-2021.yaml",
 "offset": 230
}
```

```
230	  statement: Held-out TRs of the attention task are classified into the 12 labels (four presence
231	    states by three attention conditions) from their position in the learned state space at
232	    48.4 +/- 7.6% across subjects, well above the chance of 8.3%.
233	  source: Results, The Voxel-Based State Space Method Recovers a State Space for Variables in
234	    the Attention Task, paragraph 3
235	  quote: Average performance across subjects is 48.4 ± 7.6% ( p < 1e-5, permutation test, chance =
236	    8.3%)
237	  statistics:
238	  - test: permutation test
239	    p: 1.0e-5
240	    p_relation: "<"
241	    n: 6 subjects, 10-fold cross-validation each
242	  expected:
243	  - quantity: mean classification accuracy across subjects, 12 labels
244	    value: 48.4
245	    tolerance: 7.6
246	    unit: percent
247	  criterion: Tolerance is the paper's stated spread across subjects. As in the Methods
248	    (Quantification of State Space Results, paragraph 2), per subject, 10-fold cross-validation
249	    over the stacked TRs of the three conditions; in each fold the state space (code's method)
[... 212 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/vim-4.data-description.txt; wc -c paper/*; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bmd1ezesy.txt"
}
```

```
1	Data descriptor: of the data set CRCNS:vim-4, not a paper. It describes the data set's files and how they were recorded.
2	Version: as published by CRCNS.org, https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/docs/crcns_vim-4_data_description.pdf
3	Source: the CRCNS data set's documentation (vim-4/live/docs/crcns_vim-4_data_description.pdf; vim-4/live/docs/attention_categories.txt)
4	Stored: 2026-11-06
5	Extracted: PyMuPDF, dehyphenated, NFKC
6	------------------------------------------------------------------------
7	##### vim-4/live/docs/crcns_vim-4_data_description.pdf
8	Page 1 of 4 
9	CRCNS.org vim-4 data description 
10	Version 0.8 (April 6, 2026) 
11	Whole-brain BOLD activity recorded by fMRI during a visual 
12	attention task and a video game task. 
13	Zhang, Tianjiao, James S. Gao, Tolga Cukur, and Jack L. Gallant 
14	 
15	Summary 
16	This dataset contains data from two tasks: a visual attention task, and a video game 
17	task. In both tasks, fMRI was used to record whole-brain BOLD activity with a 2.0045 s 
18	TR from healthy human subjects. 
19	 
20	In the visual attention task, subjects watched naturalistic movies in different attentional 
[... 1279 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p paper/10.3389-fnins.2020.565976.txt | cut -c1-2000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bv2ojskia.txt",
 "offset": 10
}
```

```
10	
11	## Introduction
12	
13	To maximize efficiency and statistical power, most neuroimaging experiments use simple parametric designs and highly focused data analysis. However, the results of such experiments often do not generalize to the real world ( Wu M. C. et al., 2006 ; Krakauer et al., 2017 ; Yarkoni and Westfall, 2017 ; Matusz et al., 2019 ). To address this problem, some neuroimaging experiments use more complex naturalistic conditions, such as watching movies ( Hasson et al., 2004 ; Nishimoto and Gallant, 2011 ; Huth et al., 2012 ), listening to stories ( Huth et al., 2016 ), or playing video games ( Mathiak and Weber, 2006 ; Spiers and Maguire, 2007 ; Mathiak et al., 2011 ). Neuroimaging data collected under naturalistic conditions elicit complex, dynamic patterns of brain activity across multiple functional networks that reflect the explicit and implicit task structure of the experiment ( Çukur et al., 2013b ). Therefore, such experiments dramatically increase the complexity of data analysis and modeling. For example, while watching movies selective attention to one target or another may change the representation of information in relevant functional networks ( Çukur et al., 2013b ), and while playing a video game the dynamic evolution of goals and subgoals over the course of the game might evoke activity in distinct functional networks over time ( Spiers and Maguire, 2006 ). Current methods for describing functional networks rely overwhelmingly on functional connectivity (FC) ( Friston, 1994 ). FC analysis has become popular for use in resting state studies, where the factors driving brain activity are unknown latent variables ( Shen et al., 2010 ; Van Dijk et al., 2010 ; Yeo et al., 2011 ; Blumensath et al., 2013 ; Buckner et al., 2013 ; Smith et al., 2013 ; Gordon et al., 2014 ). However, networks recovered by FC have no clear functional assignment. Therefore, there is a need for new methods of analysis that can efficiently describe whole-brain acti
[... 222 more lines not kept]
```

**Agent**

Now list the bucket.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=vim-4/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(int(s)/1e6, k)
print(re.findall(r'<IsTruncated>(.*?)<',t))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; curl -s $B/Mappers/old/README.txt; echo; cd $TMPDIR && git clone -q https://github.com/gallantlab/state-space && cd state-space && git log --oneline | head -3 && ls
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/state-space && cat StateSpace.py && python3 -c "
import json;nb=json.load(open('Example.ipynb'))
for c in nb['cells']:
  print('----',c['cell_type']);print(''.join(c['source']))
"
```

```
import numpy
from scipy import stats, signal
from sklearn.linear_model import RidgeCV
from sklearn.decomposition import PCA
from matplotlib.pyplot import figure as Figure


def make_delays(matrix, delays = range(5), fill = 0):
	"""
	Makes a version of the a matrix with delays
	:param matrix:
	:param delays:
	:param fill:
	:return:
	"""
	if (matrix.ndim == 1):
		matrix = matrix[...,None]
	out = numpy.ones((matrix.shape[0], matrix.shape[1] * len(delays)),
					 dtype = matrix.dtype) * fill

[... 254 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q h5py fsspec aiohttp requests numpy scipy scikit-learn matplotlib pandas ipykernel 2>&1 | tail -2; python -c "import h5py,fsspec;print('ok')"; nproc; free -g
```

```
ok
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
Swap:              0           0           0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe.py <<'EOF'
import fsspec, h5py, numpy as np, time
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/"
def show(path):
    with fsspec.open(B+path, block_size=2**20) as f:
        h=h5py.File(f,'r')
        def v(name,obj):
            if isinstance(obj,h5py.Dataset):
                print(path,name,obj.shape,obj.dtype, dict(obj.attrs))
            else: print(path,name,'group',dict(obj.attrs))
        h.visititems(v); print(path,'root attrs',dict(h.attrs))
for p in ["VisualAttention/Stimuli/states.hdf","VisualAttention/Stimuli/semantics.hdf","VideoGame/Stimuli/S1.hdf","VideoGame/Stimuli/S7.hdf","Mappers/S1.hdf","Mappers/S7.hdf","VisualAttention/Data/deconv/S1.hdf","VisualAttention/Data/S1.hdf"]:
    show(p)
for s in ["S1","S7"]:
    with fsspec.open(B+f"VideoGame/Data/{s}.npy", block_size=2**16) as f:
        print(s, np.lib.format.read_magic(f), np.lib.format.read_array_header_1_0(f) if True else None)
EOF
python probe.py
```

```
VisualAttention/Stimuli/states.hdf human (900, 3) float64 {}
VisualAttention/Stimuli/states.hdf passive (900, 3) float64 {}
VisualAttention/Stimuli/states.hdf vehicle (900, 3) float64 {}
VisualAttention/Stimuli/states.hdf root attrs {}
VisualAttention/Stimuli/semantics.hdf attentive (900, 935) float64 {}
VisualAttention/Stimuli/semantics.hdf passive (3600, 935) float64 {}
VisualAttention/Stimuli/semantics.hdf passive_selection_indices (114, 2) int64 {}
VisualAttention/Stimuli/semantics.hdf root attrs {}
VideoGame/Stimuli/S1.hdf behavioural_state (1950, 9) bool {}
VideoGame/Stimuli/S1.hdf state_labels (9,) |S20 {}
VideoGame/Stimuli/S1.hdf root attrs {}
VideoGame/Stimuli/S7.hdf behavioural_state (1320, 9) float32 {}
VideoGame/Stimuli/S7.hdf state_labels (9,) |S20 {}
VideoGame/Stimuli/S7.hdf root attrs {}
Mappers/S1.hdf pixmap_data (1149053,) float64 {}
Mappers/S1.hdf pixmap_indices (1149053,) int32 {}
Mappers/S1.hdf pixmap_indptr (1155715,) int32 {}
Mappers/S1.hdf pixmap_shape (2,) int64 {}
Mappers/S1.hdf pixmask (1883, 1024) bool {}
Mappers/S1.hdf vox_to_fsavg_left_data (162133,) float64 {}
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe2.py <<'EOF'
import fsspec, h5py, numpy as np, time, resource
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/"
def rd(path,keys):
    with fsspec.open(B+path, block_size=2**24) as f:
        h=h5py.File(f,'r'); return {k:h[k][()] for k in keys}
st=rd("VisualAttention/Stimuli/states.hdf",["human","vehicle","passive"])
for k,v in st.items():
    print(k, [np.unique(v[:,j],return_counts=True) for j in range(3)])
    print(' 4-state counts', np.bincount((v[:,0]+2*v[:,1]).astype(int)))
print('human==vehicle states cols0-1', np.array_equal(st['human'][:,:2],st['vehicle'][:,:2]), np.array_equal(st['human'][:,:2],st['passive'][:,:2]))
for s in ["S1","S7"]:
    g=rd(f"VideoGame/Stimuli/{s}.hdf",["behavioural_state","state_labels"])
    X=g['behavioural_state'].astype(float)
    print(s,[l.decode() for l in g['state_labels']], X.sum(0), 'rows sum dist',np.bincount(X.sum(1).astype(int)), np.unique(X))
for s in ["S1","S2","S3","S4","S5","S6","S7"]:
    m=rd(f"Mappers/{s}.hdf",["vox_to_fsavg_left_shape","vox_to_fsavg_right_shape","pixmap_shape"])
    print(s,m)
t=time.time()
with fsspec.open(B+"VisualAttention/Data/deconv/S1.hdf", block_size=2**24) as f:
    h=h5py.File(f,'r'); print(h['human'].chunks, h['human'].compression)
    a=h['human'][()]
print('read 900x51608 f64', time.time()-t, a.mean(), a.std(), a.std(0)[:5], a.mean(0)[:5])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
python probe2.py
```

```
human [(array([0., 1.]), array([312, 588])), (array([0., 1.]), array([404, 496])), (array([-1.]), array([900]))]
 4-state counts [146 258 166 330]
vehicle [(array([0., 1.]), array([312, 588])), (array([0., 1.]), array([404, 496])), (array([1.]), array([900]))]
 4-state counts [146 258 166 330]
passive [(array([0., 1.]), array([312, 588])), (array([0., 1.]), array([404, 496])), (array([0.]), array([900]))]
 4-state counts [146 258 166 330]
human==vehicle states cols0-1 True True
S1 ['Flash', 'Engage close', 'engage far', 'safe explore', 'unsafe explore', 'run away', 'dead', 'round start', 'kill'] [  9.  72. 183. 488. 812.  53. 141. 208.  64.] rows sum dist [  20 1830  100] [0. 1.]
S7 ['Flash', 'Engage close', 'engage far', 'safe explore', 'unsafe explore', 'run away', 'dead', 'round start', 'kill'] [  0. 160. 199. 265. 414.  16.  75. 176. 119.] rows sum dist [198 854 234  34] [0. 1.]
S1 {'vox_to_fsavg_left_shape': array([163842,  51608]), 'vox_to_fsavg_right_shape': array([163842,  51608]), 'pixmap_shape': array([1155714,   51608])}
S2 {'vox_to_fsavg_left_shape': array([163842,  48819]), 'vox_to_fsavg_right_shape': array([163842,  48819]), 'pixmap_shape': array([1216515,   48819])}
S3 {'vox_to_fsavg_left_shape': array([163842,  47512]), 'vox_to_fsavg_right_shape': array([163842,  47512]), 'pixmap_shape': array([1118106,   47512])}
S4 {'vox_to_fsavg_left_shape': array([163842,  39708]), 'vox_to_fsavg_right_shape': array([163842,  39708]), 'pixmap_shape': array([1446877,   39708])}
S5 {'vox_to_fsavg_left_shape': array([163842,  52044]), 'vox_to_fsavg_right_shape': array([163842,  52044]), 'pixmap_shape': array([1069913,   52044])}
S6 {'vox_to_fsavg_left_shape': array([163842,  52349]), 'vox_to_fsavg_right_shape': array([163842,  52349]), 'pixmap_shape': array([1357326,   52349])}
S7 {'vox_to_fsavg_left_shape': array([163842,  87000]), 'vox_to_fsavg_right_shape': array([163842,  87000]), 'pixmap_shape': array([1442219,   87000])}
None None
read 900x51608 f64 4.759301185
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat papers/datasets/zhang-2021.yaml; ls questions | head -3; ls schemas; cat targets/crcns.json | head -40; sed -n 150,400p attempts/fouke-2025-01.yaml | grep -n -A40 "^findings" | head -80
```

```
Sat Nov 14 10:09:28 UTC 2026
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.3389/fnins.2020.565976
title: Voxel-Based State Space Modeling Recovers Task-Related Cognitive States in Naturalistic fMRI Experiments
datasets:
- archive: crcns
  id: vim-4
  relation: primary
README.md
asari-2009.yaml
ashworth-2025.yaml
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
{
 "schema_version": 1,
 "archive": "crcns",
 "generated": "2026-11-06T21:36:03+00:00",
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:9000])"
```

```
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
"provenance",
"outcomes"
],
"properties": {
"schema_version": {
"const": 3
},
"id": {
[... 455 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/zhang-2021 && cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import fsspec, h5py, numpy as np, time
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/"
for s in ["S1","S7"]:
    t=time.time()
    with fsspec.open(B+f"VideoGame/Data/{s}.npy", block_size=2**24) as f:
        v=np.lib.format.read_magic(f); shape,fo,dt=np.lib.format.read_array_header_1_0(f)
        Y=np.frombuffer(f.read(), dtype=dt).reshape(shape)
    print(s,time.time()-t, Y.mean(), Y.std(), 'zero cols',(Y.std(0)==0).sum(), 'col mean range',Y.mean(0).min(),Y.mean(0).max(),'col std range',Y.std(0).min(),Y.std(0).max(), np.isnan(Y).sum())
    g=h5py.File(fsspec.open(B+f"VideoGame/Stimuli/{s}.hdf").open(),'r')
    X=g['behavioural_state'][()].astype(float)
    one=X.sum(1)==1
    print(' single-state counts', X[one].sum(0))
    del Y
EOF
```

```
S1 13.483670473098755 -1.1600298394763006e-16 1.0 zero cols 0 col mean range -1.3324659039954831e-13 1.6093637106733966e-13 col std range 0.9999999999999977 1.0000000000000022 0
 single-state counts [  1.  58. 142. 477. 762.  41. 141. 208.   0.]
S7 5.671640872955322 -0.00097370334 0.99205726 zero cols 0 col mean range -0.059177693 0.024697714 col std range 0.093927756 1.0093673 0
 single-state counts [  0.  53. 122. 203. 305.   4.  42. 123.   2.]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/zhang-2021/statespace.py",
 "content": "\"\"\"Loading and state space measures for CRCNS vim-4 (Zhang, Gao, Cukur & Gallant 2021).\n\nThe data set is streamed from the public CRCNS bucket; nothing is written to disk.\n\nWhere each method comes from:\n\n- State space: the paper's Methods (\"Voxel-Based State Space Modeling\") and its\n  code, gallantlab/state-space at commit 6ffb3c3, `extract_state_space_positions`\n  (claims file, opening comment): OLS of the responses on the task variables\n  with an intercept column (pinv of the normal equations), PCA with 24\n  components on the [TR x voxel] responses, denoised weights U U^T B^T, the\n  first (variables) columns of Q from the QR of the denoised weights, positions\n  = responses x those columns, z-scored per dimension over the TRs fitted.\n- Computation in PC space (an exact rewrite, not a change of method): every\n  denoised weight vector lies in the span of the 24 components C (24 x voxels,\n  orthonormal rows), so with Z = Y C^T the OLS coefficients projected on the\n  components are pinv(P^T P) P^T Z, the QR of C^T M equals C^T times the QR of\n  M, and the positions are Z Q_M. The PCA itself is computed exactly from the\n  TR x TR Gram matrix Y Y^T (the eigenvectors of the centred Gram matrix); the\n  code's scikit-learn PCA(24) uses a randomized solver for this shape, which\n  approximates the same components. The notebook compares the two on one\n  subject.\n- JSD: the code's `JSD`, a Monte Carlo estimate from 1000 samples of each\n  normal, in log base 2; computed here in the log domain (log-sum-exp), which\n  gives the same values without the underflow of the code's ratio of\n  densities. CSI: the mean JSD over all pairs of clusters (Methods,\n  \"Quantification of State Space Results\", paragraph 1). Cluster normals use\n  the sample mean and covariance (ddof 1), a standard choice.\n- The JSD between two normals is unchanged by any invertible affine map applied\n  to both, so the CSI does not depend on the signs, order or z-scoring of the\n  state dimensions, only on the subspace they span.\n- Cross-validation: 10 folds, the state space refitted on the training TRs\n  (PCA included), held-out TRs projected and assigned to the nearest training\n  cluster (Methods, paragraph 2). Folds, distance and z-scoring of held-out TRs\n  are readings named in the claims file.\n\"\"\"\nimport fsspec\nimport h5py\nimport numpy as np\nfrom scipy import linalg\n\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/\"\nDOI = \"10.6080/K0668BDF\"\nVERSION = \"unversioned\"\nATT_SUBJECTS = [\"S1\", \"S2\", \"S3\", \"S5\", \"S6\"]  # S4 not released (data description)\nGAME_SUBJECTS = [\"S1\", \"S7\"]\nCONDITIONS = [\"passive\", \"human\", \"vehicle\"]  # stacking order of the code's Example.ipynb\nN_PCS = 24  # Methods, \"Voxel-Based State Space Modeling\", paragraph 3\nTABLE1_ORDER = [\"dead\", \"round start\", \"safe explore\", \"unsafe explore\", \"kill\",\n                \"engage close\", \"engage far\", \"flash\", \"run away\"]\nPRESENCE_NAMES = [\"neither\", \"humans only\", \"vehicles only\", \"both\"]\n\n\ndef _open(path, block_size=2**24):\n    return fsspec.open(BASE + path, block_size=block_size).open()\n\n\ndef read_hdf(path, keys=None):\n    \"\"\"Read whole datasets of a small HDF5 file into memory.\"\"\"\n    with _open(path) as f, h5py.File(f, \"r\") as h:\n        keys = list(h.keys()) if keys is None else keys\n        return {k: h[k][()] for k in keys}\n\n\ndef hdf_layout(path):\n    \"\"\"Names, shapes and dtypes of every dataset in an HDF5 file (no data read).\"\"\"\n    out = []\n    with _open(path, 2**20) as f, h5py.File(f, \"r\") as h:\n        h.visititems(lambda n, o: out.append((n, o.shape, str(o.dtype)))\n                     if isinstance(o, h5py.Dataset) else None)\n    return out\n\n\ndef npy_layout(path):\n    with _open(path, 2**16) as f:\n        np.lib.format.read_magic(f)\n        shape, _, dtype = np.lib.format.read_array_header_1_0(f)\n    return shape, str(dtype)\n\n\ndef load_attention_states():\n    \"\"\"[TR x 3] states per condition: human presence, vehicle presence, attention.\"\"\"\n    return read_hdf(\"VisualAttention/Stimuli/states.hdf\", CONDITIONS)\n\n\ndef presence_code(states):\n    \"\"\"0 neither, 1 humans only, 2 vehicles only, 3 both (as in Example.ipynb).\"\"\"\n    return (states[:, 0] + 2 * states[:, 1]).astype(int)\n\n\ndef gram_summary(Y):\n    \"\"\"Gram matrix and per-voxel summaries of a [TR x voxel] array.\"\"\"\n    sd = Y.std(0)\n    return {\"G\": Y @ Y.T, \"n_vox\": Y.shape[1], \"n_zero_vox\": int((sd == 0).sum()),\n            \"vox_mean_range\": (float(Y.mean(0).min()), float(Y.mean(0).max())),\n            \"vox_sd_range\": (float(sd[sd > 0].min()), float(sd.max())),\n            \"n_nan\": int(np.isnan(Y).sum())}\n\n\ndef load_attention_gram(subject):\n    \"\"\"Stream one subject's deconvolved responses, stacked passive, human, vehicle.\n\n    Returns the 2700 x 2700 Gram matrix and summaries; the voxel data are dropped.\n    \"\"\"\n    with _open(f\"VisualAttention/Data/deconv/{subject}.hdf\") as f, h5py.File(f, \"r\") as h:\n        Y = np.vstack([h[c][()] for c in CONDITIONS])\n    out = gram_summary(Y)\n    del Y\n    return out\n\n\ndef load_game(subject):\n    \"\"\"Stream one subject's video game BOLD (npy) and its state labels.\"\"\"\n    with _open(f\"VideoGame/Data/{subject}.npy\") as f:\n        np.lib.format.read_magic(f)\n        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)\n        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)\n    out = gram_summary(Y)\n    del Y\n    st = read_hdf(f\"VideoGame/Stimuli/{subject}.hdf\")\n    out[\"X\"] = st[\"behavioural_state\"].astype(float)\n    out[\"labels\"] = [s.decode().strip().lower() for s in st[\"state_labels\"]]\n    return out\n\n\n# ---------------------------------------------------------------- PCA from Gram\n\ndef pca_scores(G, train, test=None, k=N_PCS):\n    \"\"\"Scores on the top-k principal components fitted to the training TRs.\n\n    G is Y Y^T over all TRs. Training rows are centred on their own mean, as\n    scikit-learn's PCA does; held-out rows are centred with the training mean.\n    Returns (Z_train, Z_test or None, fraction of training variance explained).\n    \"\"\"\n    train = np.asarray(train)\n    Gtt = G[np.ix_(train, train)]\n    rs = Gtt.mean(1)\n    tot = rs.mean()\n    Gc = Gtt - rs[:, None] - rs[None, :] + tot\n    n = len(train)\n    w, U = linalg.eigh(Gc, subset_by_index=[n - k, n - 1])\n    w, U = w[::-1], U[:, ::-1]\n    Z_tr = U * np.sqrt(w)\n    Z_te = None\n    if test is not None:\n        test = np.asarray(test)\n        Gx = G[np.ix_(test, train)]\n        cross = Gx - Gx.mean(1)[:, None] - rs[None, :] + tot\n        Z_te = cross @ U / np.sqrt(w)\n    return Z_tr, Z_te, float(w.sum() / np.trace(Gc))\n\n\n# ---------------------------------------------------------------- state space\n\ndef state_directions(Z, X):\n    \"\"\"Q_M and R: the QR of the denoised weights in PC coordinates.\n\n    Z [TR x 24] PCA scores, X [TR x d] task variables. The intercept column is\n    last, as in the code, so it does not change the first d directions.\n    \"\"\"\n    P = np.column_stack([X, np.ones(len(X))])\n    coef = np.linalg.pinv(P.T @ P) @ (P.T @ Z)  # (d+1) x 24, = B C^T\n    Q, R = np.linalg.qr(coef.T)  # 24 x (d+1)\n    d = X.shape[1]\n    return Q[:, :d], R[:d, :d]\n\n\ndef positions(Z, X, sign=None):\n    \"\"\"Z-scored state space positions of the fitted TRs.\n\n    sign: None (as the QR returns), \"diag\" (diagonal of R made positive) or\n    \"own\" (each dimension oriented so its own variable's TRs, X[:, j] > 0, have\n    a positive mean position).\n    \"\"\"\n    Q, R = state_directions(Z, X)\n    if sign == \"diag\":\n        Q = Q * np.sign(np.diag(R))\n    pos = Z @ Q\n    pos = (pos - pos.mean(0)) / pos.std(0)\n    if sign == \"own\":\n        for j in range(X.shape[1]):\n            if X[:, j].any() and pos[X[:, j] > 0, j].mean() < 0:\n                pos[:, j] *= -1\n    return pos\n\n\n# ---------------------------------------------------------------- JSD and CSI\n\ndef _fit_normal(x):\n    m = x.mean(0)\n    c = np.cov(x, rowvar=False, ddof=1)\n    return m, linalg.cholesky(np.atleast_2d(c), lower=True)\n\n\ndef _logpdf(x, m, L):\n    sol = linalg.solve_triangular(L, (x - m).T, lower=True)\n    d = len(m)\n    return -0.5 * (sol ** 2).sum(0) - np.log(np.diag(L)).sum() - 0.5 * d * np.log(2 * np.pi)\n\n\ndef jsd(n1, n2, rng, samples=1000):\n    \"\"\"Monte Carlo JSD (bits) between two fitted normals (m, cholesky).\"\"\"\n    (m1, L1), (m2, L2) = n1, n2\n    d = len(m1)\n    s1 = m1 + rng.standard_normal((samples, d)) @ L1.T\n    s2 = m2 + rng.standard_normal((samples, d)) @ L2.T\n    # log2(p_a / ((p_a + p_b) / 2)) = 1 - log2(1 + p_b / p_a)\n    a = 1 - np.logaddexp(0, _logpdf(s1, m2, L2) - _logpdf(s1, m1, L1)) / np.log(2)\n    b = 1 - np.logaddexp(0, _logpdf(s2, m1, L1) - _logpdf(s2, m2, L2)) / np.log(2)\n    return 0.5 * (a.mean() + b.mean())\n\n\ndef csi(pos, members, rng, samples=1000):\n    \"\"\"Cluster separation index: mean pairwise JSD of the clusters' normals.\n\n    members: list of boolean or index arrays, one per cluster.\n    \"\"\"\n    normals = [_fit_normal(pos[m]) for m in members]\n    vals = [jsd(normals[i], normals[j], rng, samples)\n            for i in range(len(normals)) for j in range(i + 1, len(normals))]\n    return float(np.mean(vals))\n\n\n# ---------------------------------------------------------------- classification\n\ndef nearest_cluster(train_pos, train_lab, test_pos, classes, rule):\n    \"\"\"Assign each test point to the nearest training cluster.\n\n    rule \"euclid\": Euclidean distance to the cluster mean; \"density\": highest\n    density under the cluster's fitted normal.\n    \"\"\"\n    if rule == \"euclid\":\n        means = np.array([train_pos[train_lab == c].mean(0) for c in classes])\n        d2 = ((test_pos[:, None, :] - means[None]) ** 2).sum(-1)\n        return np.asarray(classes)[d2.argmin(1)]\n    ll = np.column_stack([_logpdf(test_pos, *_fit_normal(train_pos[train_lab == c]))\n                          for c in classes])\n    return np.asarray(classes)[ll.argmax(1)]\n\n\ndef folds(n, scheme, rng, k=10):\n    \"\"\"Test indices of k folds: \"contig\" (contiguous tenths) or \"random\".\"\"\"\n    idx = np.arange(n) if scheme == \"contig\" else rng.permutation(n)\n    return np.array_split(idx, k)\n\n\ndef fold_scores(G, test_sets):\n    \"\"\"PCA scores per fold: list of (train, test, Z_train, Z_test).\"\"\"\n    n = G.shape[0]\n    out = []\n    for te in test_sets:\n        tr = np.setdiff1d(np.arange(n), te)\n        Ztr, Zte, _ = pca_scores(G, tr, te)\n        out.append((tr, np.sort(te) if False else te, Ztr, Zte))\n    return out\n\n\ndef project_fold(Ztr, Zte, Xtr):\n    \"\"\"Training and held-out positions; held-out z-scored with training statistics.\"\"\"\n    Q, _ = state_directions(Ztr, Xtr)\n    ptr, pte = Ztr @ Q, Zte @ Q\n    m, s = ptr.mean(0), ptr.std(0)\n    return (ptr - m) / s, (pte - m) / s\n"
}
```

```
File created successfully at: entries/zhang-2021/statespace.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/zhang-2021 && python3 - <<'EOF'
p='statespace.py'; s=open(p).read()
s=s.replace("out.append((tr, np.sort(te) if False else te, Ztr, Zte))","out.append((tr, te, Ztr, Zte))")
s=s.replace('''def load_attention_gram(subject):
    """Stream one subject's deconvolved responses, stacked passive, human, vehicle.

    Returns the 2700 x 2700 Gram matrix and summaries; the voxel data are dropped.
    """
    with _open(f"VisualAttention/Data/deconv/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()] for c in CONDITIONS])
    out = gram_summary(Y)
    del Y
    return out''','''def code_positions(X, Y, num_PCs=N_PCS):
    """The paper's code, `extract_state_space_positions` (gallantlab/state-space
    at 6ffb3c3), on the full voxel data, kept as written to check the PC-space
    rewrite."""
    from scipy import stats
    from sklearn.decomposition import PCA
    parameters = np.ones([X.shape[0], X.shape[1] + 1])
    parameters[:, :-1] = X
    covar = parameters.T @ parameters
    coeffs = np.linalg.pinv(covar) @ (parameters.T @ Y)
    pca = PCA(num_PCs, random_state=0)
    pca.fit(Y)
    coeffs_denoised = pca.components_.T @ (pca.components_ @ coeffs.T)
    Q, _ = np.linalg.qr(coeffs_denoised)  # reduced QR: same first columns as 'full'
    return stats.zscore(Y @ Q[:, :X.shape[1]])


def load_attention_gram(subject, X_check=None):
    """Stream one subject's deconvolved responses, stacked passive, human, vehicle.

    Returns the 2700 x 2700 Gram matrix and summaries; the voxel data are
    dropped. With X_check, also the positions from the paper's code on the full
    voxel data.
    """
    with _open(f"VisualAttention/Data/deconv/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()] for c in CONDITIONS])
    out = gram_summary(Y)
    if X_check is not None:
        out["code_positions"] = code_positions(X_check, Y)
    del Y
    return out''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev1.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0,'entries/zhang-2021')
import statespace as ss
st=ss.load_attention_states(); X=np.vstack([st[c] for c in ss.CONDITIONS])
t=time.time(); d=ss.load_attention_gram("S2", X_check=X); print('load',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
np.save('G_S2.npy', d['G'])
G=d['G']; n=len(G)
Z,_,ve=ss.pca_scores(G,np.arange(n)); print('var expl',ve, {k:v for k,v in d.items() if k not in ('G','code_positions')})
pos=ss.positions(Z,X)
cp=d['code_positions']
print('corr per dim', [abs(np.corrcoef(pos[:,j],cp[:,j])[0,1]) for j in range(3)])
rng=np.random.default_rng(0)
pc=ss.presence_code(X)
t=time.time()
for ci,c in enumerate(ss.CONDITIONS):
    sl=slice(900*ci,900*ci+900)
    vals=[ss.csi(pos[sl],[pc[sl]==k for k in range(4)],np.random.default_rng(s)) for s in range(10)]
    valsc=[ss.csi(cp[sl],[pc[sl]==k for k in range(4)],np.random.default_rng(s)) for s in range(10)]
    print(c, np.mean(vals), np.std(vals), 'code pos', np.mean(valsc))
print('csi time', (time.time()-t)/60)
EOF
python dev1.py
```

```
load 22.6013240814209 2.879324
var expl 0.8966511422472413 {'n_vox': 48819, 'n_zero_vox': 0, 'vox_mean_range': (-0.3006130195544582, 0.30615446769290344), 'vox_sd_range': (0.8944871686623536, 1.203262397851351), 'n_nan': 0}
corr per dim [np.float64(0.9999999999824954), np.float64(0.9999999998379221), np.float64(0.16040396169056167)]
passive 0.6540714691697359 0.005390900937069868 code pos 0.6755943430481832
human 0.7325271504467175 0.006564378555499922 code pos 0.7379021761822345
vehicle 0.7660364209784865 0.006750581289699566 code pos 0.7233455309469161
csi time 0.002448586622873942
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "import sklearn;print(sklearn.__version__)" && cat > dev2.py <<'EOF'
import sys, time, numpy as np, fsspec, h5py
sys.path.insert(0,'entries/zhang-2021')
import statespace as ss
from sklearn.decomposition import PCA
from scipy import stats, linalg
st=ss.load_attention_states(); X=np.vstack([st[c] for c in ss.CONDITIONS]); pc=ss.presence_code(X)
with ss._open("VisualAttention/Data/deconv/S2.hdf") as f, h5py.File(f,'r') as h:
    Y=np.vstack([h[c][()] for c in ss.CONDITIONS])
for ci in range(3):
    m=Y[900*ci:900*ci+900].mean(0); print('cond',ci,'voxel mean abs', np.abs(m).mean(), 'sd', Y[900*ci:900*ci+900].std(0).mean())
P=np.column_stack([X,np.ones(len(X))]); coeffs=np.linalg.pinv(P.T@P)@(P.T@Y)
print('coef norms', np.linalg.norm(coeffs,axis=1))
def run(pca):
    pca.fit(Y); C=pca.components_
    D=C.T@(C@coeffs.T); Q,_=np.linalg.qr(D); pos=stats.zscore(Y@Q[:,:3])
    out=[]
    for ci in range(3):
        sl=slice(900*ci,900*ci+900)
        out.append(np.mean([ss.csi(pos[sl],[pc[sl]==k for k in range(4)],np.random.default_rng(s)) for s in range(5)]))
    return pos, out, pca.explained_variance_ratio_.sum()
ref=None
for name,p in [('full',PCA(24,svd_solver='full'))]+[(f'rand{s}',PCA(24,svd_solver='randomized',random_state=s)) for s in range(4)]:
    t=time.time(); pos,cs,ve=run(p)
    if ref is None: ref=pos
    print(name, round(time.time()-t,1), 'csi p/h/v', np.round(cs,3), 've',round(ve,3), 'corr to full', [round(abs(np.corrcoef(pos[:,j],ref[:,j])[0,1]),4) for j in range(3)])
EOF
python dev2.py
```

```
1.9.1
cond 0 voxel mean abs 0.302678846852084 sd 0.9771075692150026
cond 1 voxel mean abs 6.0909276215174335e-16 sd 1.0
cond 2 voxel mean abs 4.925812688347754e-16 sd 1.0
coef norms [1.21141915e+02 1.23641217e+02 1.26139697e-13 9.67592679e+01]
full 40.7 csi p/h/v [0.677 0.738 0.725] ve 0.897 corr to full [np.float64(1.0), np.float64(1.0), np.float64(1.0)]
rand0 4.5 csi p/h/v [0.677 0.738 0.725] ve 0.897 corr to full [np.float64(1.0), np.float64(1.0), np.float64(1.0)]
rand1 4.5 csi p/h/v [0.677 0.738 0.726] ve 0.897 corr to full [np.float64(1.0), np.float64(1.0), np.float64(1.0)]
rand2 4.1 csi p/h/v [0.677 0.738 0.725] ve 0.897 corr to full [np.float64(1.0), np.float64(1.0), np.float64(1.0)]
rand3 4.1 csi p/h/v [0.677 0.738 0.725] ve 0.897 corr to full [np.float64(1.0), np.float64(1.0), np.float64(1.0)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > dev3.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/zhang-2021')
import statespace as ss
st=ss.load_attention_states(); X=np.vstack([st[c] for c in ss.CONDITIONS]); pc=ss.presence_code(X)
G=np.load('G_S2.npy'); n=len(G)
Z,_,_=ss.pca_scores(G,np.arange(n))
P=np.column_stack([X,np.ones(n)]); coef=np.linalg.pinv(P.T@P)@(P.T@Z); print('coef norms PC', np.linalg.norm(coef,axis=1))
Q,R=ss.state_directions(Z,X)
rng=np.random.default_rng(1)
def csis(pos):
    return [np.mean([ss.csi(pos[900*c:900*c+900],[pc[900*c:900*c+900]==k for k in range(4)],np.random.default_rng(s)) for s in range(3)]) for c in range(3)]
p2=Z@Q[:,:2]; p2=(p2-p2.mean(0))/p2.std(0)
print('2D', np.round(csis(p2),3))
res=[]
for i in range(40):
    v=rng.standard_normal(24); v-=Q[:,:2]@(Q[:,:2].T@v); v/=np.linalg.norm(v)
    p=Z@np.column_stack([Q[:,:2],v]); p=(p-p.mean(0))/p.std(0); res.append(csis(p))
res=np.array(res); print('random 3rd: median',np.median(res,0).round(3),'5-95',np.percentile(res,[5,95],0).round(3))
EOF
python dev3.py
```

```
Sat Nov 14 10:14:40 UTC 2026
coef norms PC [1.20992300e+02 1.23296561e+02 1.43133880e-14 1.06868918e+02]
2D [0.631 0.663 0.669]
random 3rd: median [0.668 0.718 0.724] 5-95 [[0.648 0.694 0.693]
 [0.693 0.77  0.789]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/zhang-2021/statespace.py <<'EOF'


# ---------------------------------------------------------------- attention task

def att_positions(Z, X, third, rng=None):
    """Positions in the attention state space under a reading of its third axis.

    In the deposited deconvolved data each attentive condition is z-scored per
    voxel, so the attention variable (-1, 0, +1) has an OLS weight of zero up to
    rounding and the third QR direction is set by rounding noise.
    third: "qr" (as the QR returns it), "2d" (human and vehicle axes only) or
    "random" (a random unit direction in the PC space, orthogonal to the
    first two, drawn from rng).
    """
    Q, _ = state_directions(Z, X)
    if third == "2d":
        Q = Q[:, :2]
    elif third == "random":
        v = rng.standard_normal(Q.shape[0])
        v -= Q[:, :2] @ (Q[:, :2].T @ v)
        Q = np.column_stack([Q[:, :2], v / np.linalg.norm(v)])
    pos = Z @ Q
    return (pos - pos.mean(0)) / pos.std(0)


def cond_slices(n_per=900):
    return [slice(i * n_per, (i + 1) * n_per) for i in range(len(CONDITIONS))]


def att_csis(pos, pcode, rng, members=None):
    """CSI of the four presence clusters within each condition (passive, human, vehicle).

    members: optional list of three index arrays giving each condition's TRs.
    """
    members = cond_slices() if members is None else members
    out = []
    for m in members:
        p, c = pos[m], pcode[m]
        out.append(csi(p, [c == k for k in range(4)], rng))
    return np.array(out)


def shuffle_presence(X, reading, rng):
    """Permuted presence labels: "a" rows of (human, vehicle) shuffled over all
    TRs; "b" circularly shifted by a random lag within each condition."""
    Xp = X.copy()
    if reading == "a":
        Xp[:, :2] = X[rng.permutation(len(X)), :2]
    else:
        for s in cond_slices():
            Xp[s, :2] = np.roll(X[s, :2], rng.integers(1, s.stop - s.start), axis=0)
    return Xp
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev4.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/zhang-2021')
import statespace as ss
st=ss.load_attention_states(); X=np.vstack([st[c] for c in ss.CONDITIONS]); pc=ss.presence_code(X)
G=np.load('G_S2.npy'); n=len(G)
Z,_,_=ss.pca_scores(G,np.arange(n))
rng=np.random.default_rng(0)
t=time.time()
nulls=[]
for i in range(200):
    Xp=ss.shuffle_presence(X,'a',rng)
    pos=ss.att_positions(Z,Xp,'random',rng); nulls.append(ss.att_csis(pos,ss.presence_code(Xp),rng))
print('perm time each', (time.time()-t)/200, np.max(nulls,0))
t=time.time(); nb=[]
for i in range(200):
    Xp=ss.shuffle_presence(X,'b',rng)
    pos=ss.att_positions(Z,Xp,'random',rng); nb.append(ss.att_csis(pos,ss.presence_code(Xp),rng))
print('b', np.max(nb,0), np.mean(nb,0))
# classification timing
t=time.time()
lab12 = pc + 4*np.repeat(np.arange(3),900)
for scheme in ['contig','random']:
    fs=ss.fold_scores(G, ss.folds(n,scheme,np.random.default_rng(1)))
    print('folds pca', time.time()-t)
    for rule in ['euclid','density']:
        acc=[]
        for tr,te,Ztr,Zte in fs:
            ptr,pte=ss.project_fold(Ztr,Zte,X[tr])
            pred=ss.nearest_cluster(ptr,lab12[tr],pte,np.arange(12),rule)
            acc.append((pred==lab12[te]).mean())
        print(scheme,rule,np.mean(acc).round(3),np.round(acc,2))
    t=time.time()
    for i in range(20):
        for tr,te,Ztr,Zte in fs:
            perm=rng.permutation(len(tr))
            ptr,pte=ss.project_fold(Ztr,Zte,X[tr][perm])
            pred=ss.nearest_cluster(ptr,lab12[tr][perm],pte,np.arange(12),'density')
    print('null per perm (10 folds)', (time.time()-t)/20)
EOF
python dev4.py
```

```
perm time each 0.00784514307975769 [0.04804897 0.04228053 0.04087444]
b [0.07315305 0.30232881 0.11968241] [0.03514929 0.03280383 0.03527069]
folds pca 5.894564628601074
contig euclid 0.464 [0.33 0.55 0.52 0.53 0.45 0.4  0.49 0.54 0.49 0.33]
contig density 0.574 [0.52 0.64 0.67 0.63 0.62 0.48 0.53 0.6  0.61 0.45]
null per perm (10 folds) 0.01609419584274292
folds pca 6.223976373672485
random euclid 0.47 [0.48 0.44 0.41 0.46 0.5  0.5  0.51 0.48 0.39 0.51]
random density 0.58 [0.58 0.58 0.54 0.62 0.58 0.59 0.58 0.54 0.57 0.62]
null per perm (10 folds) 0.015724527835845947
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/zhang-2021/statespace.py <<'EOF'


def shuffle_conditions(n_per, scheme, rng):
    """Permuted condition membership for the passive-against-attentive test.

    Returns three index arrays (passive, human, vehicle). "matched": at each
    movie time point the three TRs showing the same frame are given the three
    conditions in random order, so every condition keeps the same presence
    labels; "global": TRs shuffled across all conditions. A standard choice for
    a detail the claims file does not fix; both are run.
    """
    n = n_per * 3
    if scheme == "global":
        p = rng.permutation(n)
        return [np.sort(p[i * n_per:(i + 1) * n_per]) for i in range(3)]
    order = np.argsort(rng.random((n_per, 3)), axis=1)  # condition of each copy
    t = np.arange(n_per)
    return [np.sort(np.concatenate([c * n_per + t[order[:, c] == k] for c in range(3)]))
            for k in range(3)]


def members_to_X(X, members):
    """State matrix with the attention column set by the permuted membership."""
    Xp = X.copy()
    for value, m in zip([0.0, -1.0, 1.0], members):
        Xp[m, 2] = value
    return Xp


# ---------------------------------------------------------------- video game

def game_matrix(X, labels, order):
    """State matrix with columns in dataset order or Table 1 order; states with
    no TRs are dropped (flash in S7), as Supplementary Figure 4 has no flash
    weights for that subject."""
    names = labels if order == "dataset" else [s for s in TABLE1_ORDER if s in labels]
    cols = [labels.index(s) for s in names]
    keep = [i for i, c in enumerate(cols) if X[:, c].any()]
    return X[:, [cols[i] for i in keep]], [names[i] for i in keep]


def game_members(X, names, reading):
    """Clusters for the video game CSI.

    "a" one per state, a TR in the cluster of every state it has; "b" one per
    state from TRs with exactly one state; "c" safe explore, engage close and
    all other TRs (Figure 3A). Clusters with no more TRs than dimensions are
    left out (no covariance can be fitted).
    """
    d = X.shape[1]
    if reading == "c":
        se, ec = X[:, names.index("safe explore")] > 0, X[:, names.index("engage close")] > 0
        mem, nm = [se, ec, ~se & ~ec], ["safe explore", "engage close", "other"]
    else:
        ok = np.ones(len(X), bool) if reading == "a" else X.sum(1) == 1
        mem = [(X[:, j] > 0) & ok for j in range(d)]
        nm = list(names)
    keep = [i for i, m in enumerate(mem) if m.sum() > d]
    dropped = [(nm[i], int(mem[i].sum())) for i in range(len(mem)) if i not in keep]
    return [mem[i] for i in keep], [nm[i] for i in keep], dropped


def projection_matrix(pos, X):
    """M[i, j]: mean position on dimension j of the TRs that have state i."""
    return np.array([pos[X[:, i] > 0].mean(0) for i in range(X.shape[1])])


def balanced_accuracy(true_sets, pred, classes):
    """Mean recall over classes present: for class c, the fraction of TRs whose
    label set contains c that are predicted as c."""
    rec = []
    for c in classes:
        has = np.array([c in s for s in true_sets])
        if has.any():
            rec.append((pred[has] == c).mean())
    return float(np.mean(rec))
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev5.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/zhang-2021')
import statespace as ss
for s in ['S7','S1']:
    t=time.time(); g=ss.load_game(s); print(s,'load',time.time()-t, g['labels'])
    np.save(f'Gg_{s}.npy',g['G']); np.save(f'Xg_{s}.npy',g['X'])
    G=g['G']; n=len(G); Z,_,ve=ss.pca_scores(G,np.arange(n)); print('ve',ve)
    for order in ['dataset','table1']:
        X,names=ss.game_matrix(g['X'],g['labels'],order)
        for sign in ['own','diag']:
            pos=ss.positions(Z,X,sign); M=ss.projection_matrix(pos,X)
            i,j=names.index('engage close'),names.index('safe explore')
            print(order,sign,'EC on SE',M[i,j].round(3),'SE on EC',M[j,i].round(3))
    X,names=ss.game_matrix(g['X'],g['labels'],'dataset'); pos=ss.positions(Z,X)
    for r in 'abc':
        mem,nm,dr=ss.game_members(X,names,r)
        t=time.time(); v=[ss.csi(pos,mem,np.random.default_rng(k)) for k in range(3)]
        print(r,np.round(v,3),dr,'t',(time.time()-t)/3)
    # label shift check
    for lag in [-4,-2,0,1,2,3,4,6,10]:
        Xs=np.roll(X,lag,axis=0); p=ss.positions(Z,Xs); mem,_,_=ss.game_members(Xs,names,'a')
        print('lag',lag, round(ss.csi(p,mem,np.random.default_rng(0)),3))
EOF
python dev5.py
```

```
S7 load 7.5292277336120605 ['flash', 'engage close', 'engage far', 'safe explore', 'unsafe explore', 'run away', 'dead', 'round start', 'kill']
ve 0.39769164155419
dataset own EC on SE -0.191 SE on EC -0.548
dataset diag EC on SE -0.191 SE on EC -0.548
table1 own EC on SE -0.552 SE on EC -0.018
table1 diag EC on SE -0.552 SE on EC -0.018
a [0.554 0.548 0.547] [] t 0.016576846440633137
b [0.585 0.581 0.575] [('run away', 4), ('kill', 2)] t 0.008572816848754883
c [0.395 0.378 0.389] [] t 0.0019641717274983725
lag -4 0.457
lag -2 0.494
lag 0 0.554
lag 1 0.57
lag 2 0.556
lag 3 0.559
lag 4 0.534
lag 6 0.53
lag 10 0.536
S1 load 15.291327476501465 ['flash', 'engage close', 'engage far', 'safe explore', 'unsafe explore', 'run away', 'dead', 'round start', 'kill']
ve 0.3215464157755711
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, numpy as np
sys.path.insert(0,'entries/zhang-2021')
import statespace as ss
sem=ss.read_hdf("VisualAttention/Stimuli/semantics.hdf")
sel=sem['passive_selection_indices']; print(sel[:5], (sel[:,1]-sel[:,0]).sum(), sel.min(), sel.max())
from scipy import signal
up=signal.resample(sem['passive'],7200)
sub=np.vstack([up[a:b] for a,b in sel]); down=signal.resample(sub,900)
a=sem['attentive']; print('corr subsampled passive vs attentive semantics', np.corrcoef(down.ravel(),a.ravel())[0,1])
# direct: per TR comparisons via seconds -> TR index
idx=np.concatenate([np.arange(a_,b_) for a_,b_ in sel])//2
print(len(idx), 'exact match fraction (TR rows)', np.mean([np.array_equal(sem['passive'][i],a[k//2]) for k,i in enumerate(idx[::2])]))
st=ss.load_attention_states()
pres=(a>0)
for col,name in [(0,'human'),(1,'vehicle')]:
    y=st['human'][:,col]
    r=[np.corrcoef(pres[:,j],y)[0,1] if pres[:,j].std()>0 else 0 for j in range(935)]
    cats=[l.strip() for l in open('paper/vim-4.data-description.txt').read().split('##### vim-4/live/docs/attention_categories.txt')[1].split()]
    o=np.argsort(r)[::-1][:5]; print(name,[(cats[j],round(r[j],2)) for j in o])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/gen_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip()))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS vim-4\n\nPaper: Zhang T, Gao JS, Cukur T, Gallant JL (2021). Voxel-Based State Space Modeling Recovers\nTask-Related Cognitive States in Naturalistic fMRI Experiments. Frontiers in Neuroscience\n14:565976. doi:10.3389/fnins.2020.565976.\n\nClaims: `claims/zhang-2021.yaml`, written from the version of record (PMC8145286) and its\nsupplement (Data_Sheet_1.DOCX), with the paper's code, gallantlab/state-space at commit 6ffb3c3.\n\nDataset: CRCNS vim-4, \"Whole-brain BOLD activity recorded by fMRI during a visual attention task\nand a video game task\", doi:10.6080/K0668BDF, streamed from the public bucket\n`s3://crcnsarchive/vim-4/live/`. Version: `unversioned`. CRCNS data sets have no versions; the\nfiles read are those under `vim-4/live/` as of 2026-11-14 (data description version 0.8 of\n2026-04-06), which is the only published copy of the data files (`vim-4/old/` holds only older\nversions of the description). The paper cites the data set by its DOI, with no version. The MD5\nsums of the files read, from the data set's `checksums.md5`, are:\n\n| file | MD5 |\n|---|---|\n| VisualAttention/Data/deconv/S1.hdf | 5989fd2bc00fadf058eac9e7e742ad7d |\n| VisualAttention/Data/deconv/S2.hdf | 94a06a22a634efb4370b3061b532744f |\n| VisualAttention/Data/deconv/S3.hdf | 16758cb38128a43182c495660ac77eb6 |\n| VisualAttention/Data/deconv/S5.hdf | 782fcf8c74b82812fb9fb8e7e106b285 |\n| VisualAttention/Data/deconv/S6.hdf | 57fc3c680adac346ca41461e1a891592 |\n| VisualAttention/Stimuli/states.hdf | 52e2cee2155281256192c2e9ded39383 |\n| VisualAttention/Stimuli/semantics.hdf | 54143a9de19a34d647856693588dfc9d |\n| VideoGame/Data/S1.npy | c0ea35bd959465d7e03cf5b369002640 |\n| VideoGame/Data/S7.npy | 0ed00d89f585636b9091d56fc1a9ed81 |\n| VideoGame/Stimuli/S1.hdf | d66b6a346ebfa13948b71da7a8d810a8 |\n| VideoGame/Stimuli/S7.hdf | b5b5bb06946d4d6df1eb9c813d3f5825 |\n\nThe notebook prints the bucket's current sums for these files below, so a change can be seen.\nOnly the layouts of the other files (non-deconvolved BOLD, mappers) are read.\n\n| claim | tested here |\n|---|---|\n| fig1-csi-s2 | tested |\n| att-csi-group | tested (5 of 6 subjects; S4 is not released) |\n| supp-csi-per-subject | tested (S4 left out, as the claim says) |\n| att-passive-lower | tested (5 of 6 subjects) |\n| att-classification | tested (5 of 6 subjects) |\n| att-weights-cortex | blocked: the paper's functional ROIs (localizer and retinotopy data) are not public |\n| game-csi | tested |\n| game-mutual-negative-projection | tested |\n| fig3b-state-relations | tested |\n| game-classification | tested |\n| game-weights-two-groups | blocked: the paper's ROIs are not public, and S1's game data have no matching mapper |\n\nMethod: the helper `statespace.py` says where each parameter comes from. The state space is the\ncode's `extract_state_space_positions`, computed exactly in the space of the 24 principal\ncomponents (checked against the code itself below).\n\"\"\")\n\ncode(r\"\"\"\nimport time, resource\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport requests\nimport statespace as ss\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nT0 = time.time()\ndef mem_gb():\n    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\n# Files in the data set and their current MD5 sums (checksums.md5 in the bucket)\nlisting = requests.get(\"https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=vim-4/\").text\nimport re\nfiles = [(k, int(s)) for k, s in re.findall(r\"<Key>(.*?)</Key>.*?<Size>(\\d+)</Size>\", listing) if not k.endswith(\"/\")]\nprint(f\"{len(files)} files under vim-4/\")\nfor k, s in files:\n    print(f\"  {s/1e6:10.2f} MB  {k}\")\nmd5 = dict(l.split()[::-1] for l in requests.get(ss.BASE + \"checksums.md5\").text.strip().splitlines())\nread_files = [\"VisualAttention/Data/deconv/S%d.hdf\" % i for i in (1, 2, 3, 5, 6)] + [\n    \"VisualAttention/Stimuli/states.hdf\", \"VisualAttention/Stimuli/semantics.hdf\",\n    \"VideoGame/Data/S1.npy\", \"VideoGame/Data/S7.npy\", \"VideoGame/Stimuli/S1.hdf\", \"VideoGame/Stimuli/S7.hdf\"]\nfor f in read_files:\n    print(md5[f], f)\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Layout of every data file: datasets, shapes and dtypes (no data read)\nfor f in [\"VisualAttention/Data/S%d.hdf\" % i for i in (1, 2, 3, 5, 6)] + \\\n         [\"VisualAttention/Data/deconv/S%d.hdf\" % i for i in (1, 2, 3, 5, 6)] + \\\n         [\"VisualAttention/Stimuli/states.hdf\", \"VisualAttention/Stimuli/semantics.hdf\",\n          \"VideoGame/Stimuli/S1.hdf\", \"VideoGame/Stimuli/S7.hdf\"] + \\\n         [\"Mappers/S%d.hdf\" % i for i in range(1, 8)]:\n    for name, shape, dtype in ss.hdf_layout(f):\n        print(f\"{f:42s} {name:28s} {str(shape):18s} {dtype}\")\nfor s in ss.GAME_SUBJECTS:\n    print(f\"VideoGame/Data/{s}.npy\", ss.npy_layout(f\"VideoGame/Data/{s}.npy\"))\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Attention task labels: states.hdf, and the semantic labels they should follow\nst = ss.load_attention_states()\nfor c in ss.CONDITIONS:\n    v = st[c]\n    print(c, v.shape, \"| human presence values\", np.unique(v[:, 0]), \"| vehicle\", np.unique(v[:, 1]),\n          \"| attention column values\", np.unique(v[:, 2]),\n          \"| presence counts (neither, humans, vehicles, both)\", np.bincount(ss.presence_code(v), minlength=4))\nprint(\"presence columns identical across the three conditions:\",\n      np.array_equal(st[\"human\"][:, :2], st[\"vehicle\"][:, :2]) and np.array_equal(st[\"human\"][:, :2], st[\"passive\"][:, :2]))\nX_att = np.vstack([st[c] for c in ss.CONDITIONS])\npcode = ss.presence_code(X_att)\n\nsem = ss.read_hdf(\"VisualAttention/Stimuli/semantics.hdf\")\nsel = sem[\"passive_selection_indices\"]\nprint(\"passive_selection_indices: %d sections, %d s selected in total (900 TRs x 2 s = 1800 s), range %d to %d s\"\n      % (len(sel), (sel[:, 1] - sel[:, 0]).sum(), sel.min(), sel.max()))\n# The code's subsample_passive_data applied to the passive semantic labels should give the attentive labels\nfrom scipy import signal\nup = signal.resample(sem[\"passive\"], 7200)\ndown = signal.resample(np.vstack([up[a:b] for a, b in sel]), 900)\nprint(\"correlation of the subsampled passive semantic labels with the attentive ones: %.3f\"\n      % np.corrcoef(down.ravel(), sem[\"attentive\"].ravel())[0, 1])\ncats = requests.get(ss.BASE + \"docs/attention_categories.txt\").text.split()\npres = sem[\"attentive\"] > 0\nfor col, name in [(0, \"human\"), (1, \"vehicle\")]:\n    y = st[\"human\"][:, col]\n    r = np.array([np.corrcoef(pres[:, j], y)[0, 1] if pres[:, j].std() > 0 else 0 for j in range(pres.shape[1])])\n    top = np.argsort(r)[::-1][:3]\n    print(f\"{name} presence: best matching semantic categories\", [(cats[j], round(r[j], 2)) for j in top])\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Load each attention subject's deconvolved data (stacked passive, human, vehicle), keep the\n# 2700 x 2700 Gram matrix, and run the paper's code itself on the full voxel data for comparison.\natt = {}\nfor s in ss.ATT_SUBJECTS:\n    t = time.time()\n    d = ss.load_attention_gram(s, X_check=X_att)\n    G = d[\"G\"]\n    # per-condition mean and SD of the voxels, from the Gram matrix diagonal blocks is not enough,\n    # so recompute from the summaries: sum of squares per TR\n    Z, _, ve = ss.pca_scores(G, np.arange(len(G)))\n    P = np.column_stack([X_att, np.ones(len(X_att))])\n    coef = np.linalg.pinv(P.T @ P) @ (P.T @ Z)\n    pos_rw = ss.att_positions(Z, X_att, \"qr\")\n    cp = d[\"code_positions\"]\n    corr = [abs(np.corrcoef(pos_rw[:, j], cp[:, j])[0, 1]) for j in range(3)]\n    # same-frame TRs across conditions: correlation of their voxel patterns (duplicate check)\n    nrm = np.sqrt(np.diag(G))\n    same = {f\"{a}-{b}\": float(np.mean([G[i + 900 * ia, i + 900 * ib] / nrm[i + 900 * ia] / nrm[i + 900 * ib] for i in range(900)]))\n            for ia, a in enumerate(ss.CONDITIONS) for ib, b in enumerate(ss.CONDITIONS) if ia < ib}\n    att[s] = dict(G=G, Z=Z, code_pos=cp, ve=ve)\n    print(f\"{s}: {d['n_vox']} voxels ({d['n_zero_vox']} constant, {d['n_nan']} NaN), voxel means {d['vox_mean_range'][0]:.3f} to \"\n          f\"{d['vox_mean_range'][1]:.3f}, SDs {d['vox_sd_range'][0]:.3f} to {d['vox_sd_range'][1]:.3f}; \"\n          f\"24 PCs explain {ve:.1%}; |weights| in PC space human {np.linalg.norm(coef[0]):.3g}, vehicle \"\n          f\"{np.linalg.norm(coef[1]):.3g}, attention {np.linalg.norm(coef[2]):.3g}; |r| rewrite vs code per axis \"\n          f\"{np.round(corr, 4)}; mean r of same-frame TRs {same}; {time.time()-t:.0f} s, peak memory {mem_gb():.1f} GB\")\nprint(\"voxels per subject: mean %.0f, SD %.0f (paper: 48,673 +/- 4,382 over six subjects)\"\n      % (np.mean([att[s]['G'].shape[0] * 0 + d['n_vox'] for s in [ss.ATT_SUBJECTS[-1]]]), 0) if False else \"\")\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Per-condition means of the voxels: the attentive conditions are z-scored per voxel within the condition,\n# so the attention variable (-1 human, 0 passive, +1 vehicle) carries no mean difference between them.\nfor s in ss.ATT_SUBJECTS:\n    G = att[s][\"G\"]\n    # the mean over voxels of each TR's squared norm, per condition, and the norm of each condition's mean pattern\n    msq = [np.mean(np.diag(G)[sl]) for sl in ss.cond_slices()]\n    mean_norm = [np.sqrt(G[sl, sl].sum()) / 900 for sl in ss.cond_slices()]\n    print(f\"{s}: mean squared norm per TR {np.round(msq, 0)}; norm of each condition's mean pattern \"\n          f\"(passive, human, vehicle) {np.round(mean_norm, 4)}\")\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Clock check for the attention task: CSI of the presence clusters when the presence labels are\n# shifted in time within each condition (refitted at each lag). Deconvolved data should peak at lag 0.\nlags = [-6, -3, -2, -1, 0, 1, 2, 3, 6, 20]\nrng = np.random.default_rng(100)\nrows = []\nfor s in ss.ATT_SUBJECTS:\n    Z = att[s][\"Z\"]\n    for lag in lags:\n        Xs = X_att.copy()\n        for sl in ss.cond_slices():\n            Xs[sl, :2] = np.roll(X_att[sl, :2], lag, axis=0)\n        pos = ss.att_positions(Z, Xs, \"2d\")\n        rows.append(dict(subject=s, lag=lag, csi=ss.att_csis(pos, ss.presence_code(Xs), rng).mean()))\nshift = pd.DataFrame(rows).pivot(index=\"subject\", columns=\"lag\", values=\"csi\")\nprint(\"mean CSI over conditions, human-vehicle plane, by label lag in TRs (positive: labels moved later)\")\nprint(shift.round(3))\nprint(\"lag of the peak per subject:\", shift.idxmax(axis=1).to_dict())\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Video game data\ngame = {}\nfor s in ss.GAME_SUBJECTS:\n    t = time.time()\n    g = ss.load_game(s)\n    G = g[\"G\"]\n    Z, _, ve = ss.pca_scores(G, np.arange(len(G)))\n    g[\"Z\"], g[\"ve\"] = Z, ve\n    game[s] = g\n    X = g[\"X\"]\n    nst = X.sum(1).astype(int)\n    print(f\"{s}: {X.shape[0]} TRs ({X.shape[0]*2.0045/60:.1f} min at TR 2.0045 s), {g['n_vox']} voxels \"\n          f\"({g['n_zero_vox']} constant, {g['n_nan']} NaN), voxel means {g['vox_mean_range'][0]:.3f} to {g['vox_mean_range'][1]:.3f}, \"\n          f\"SDs {g['vox_sd_range'][0]:.3f} to {g['vox_sd_range'][1]:.3f}; 24 PCs explain {ve:.1%}; {time.time()-t:.0f} s\")\n    print(\"   state labels (dataset order):\", g[\"labels\"])\n    print(\"   TRs per state:\", dict(zip(g[\"labels\"], X.sum(0).astype(int))))\n    print(\"   TRs with 0, 1, 2, 3 states:\", np.bincount(nst, minlength=4))\n    print(\"   TRs with exactly one state, per state:\", dict(zip(g[\"labels\"], X[nst == 1].sum(0).astype(int))))\n    print(\"   safe explore and engage close together in\", int(((X[:, g['labels'].index('safe explore')] > 0) & (X[:, g['labels'].index('engage close')] > 0)).sum()), \"TRs\")\nmapper_vox = {f\"S{i}\": ss.read_hdf(f\"Mappers/S{i}.hdf\", [\"vox_to_fsavg_left_shape\"])[\"vox_to_fsavg_left_shape\"][1] for i in range(1, 8)}\nprint(\"voxels per mapper:\", mapper_vox)\nprint(\"game voxels:\", {s: game[s][\"n_vox\"] for s in ss.GAME_SUBJECTS}, \"| attention voxels (deconv files):\",\n      {s: att[s][\"G\"].shape and ss.hdf_layout(f\"VisualAttention/Data/deconv/{s}.hdf\")[0][1][1] for s in ss.ATT_SUBJECTS})\nprint(f\"elapsed {time.time()-T0:.0f} s, peak memory {mem_gb():.1f} GB\")\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Clock check for the video game: CSI (one cluster per state) with the state matrix shifted in time\nrng = np.random.default_rng(101)\nrows = []\nfor s in ss.GAME_SUBJECTS:\n    X, names = ss.game_matrix(game[s][\"X\"], game[s][\"labels\"], \"dataset\")\n    for lag in [-10, -4, -2, -1, 0, 1, 2, 3, 4, 6, 10]:\n        Xs = np.roll(X, lag, axis=0)\n        mem, _, _ = ss.game_members(Xs, names, \"a\")\n        rows.append(dict(subject=s, lag=lag, csi=ss.csi(ss.positions(game[s][\"Z\"], Xs), mem, rng)))\ngshift = pd.DataFrame(rows).pivot(index=\"subject\", columns=\"lag\", values=\"csi\")\nprint(gshift.round(3))\nprint(\"lag of the peak per subject:\", gshift.idxmax(axis=1).to_dict())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nChecks of the description against the data, from the outputs above:\n\n- The deconvolved attention files hold 900 TRs per condition for S1, S2, S3, S5 and S6 (30 min each\n  at a 2 s TR, three 10-min runs as the paper says); S4 is absent, as the description says. The\n  passive deconvolved data are already subsampled to the 900 TRs of the attentive movies. The\n  selection indices cover 1800 s, and applying the code's subsampling to the passive semantic\n  labels reproduces the attentive labels (correlation printed above), which is consistent with\n  the passive data and labels sharing the attentive clock.\n- `states.hdf` has the same presence labels in all three conditions; the third column codes the\n  condition as -1 (attend humans), 0 (passive) and +1 (attend vehicles). The description does not\n  give this coding. The vehicle column follows the semantic category `vehicle.n.01` exactly, and\n  the human column follows `person.n.01` closely.\n- The attentive conditions are z-scored per voxel within each condition (voxel means of zero, so\n  the norm of each attentive condition's mean pattern is zero), while the passive TRs, subsampled\n  after z-scoring, are not. With the attention variable coded -1, 0, +1 and an intercept, its OLS\n  weight is the difference of the two attentive means, which is zero: the printed attention weight\n  is at the level of rounding (1e-13), so the third axis of the state space is set by rounding\n  noise. This is analysed in each attention claim below.\n- The PC-space rewrite gives the code's human and vehicle axes exactly (|r| = 1.0000); its third\n  axis differs, being noise in both. 24 PCs explain about 85 to 90% of the variance here, against\n  about 70% in the paper.\n- Labels and BOLD share a clock as far as shifted labels show: the attention CSI peaks at lag 0,\n  as deconvolved data should, and the game CSI peaks within one TR of lag 0. This is consistent\n  with, not proof of, aligned labels.\n- Video game: S7 has 1320 TRs (44 min, the paper's 45 min). S1 has 1950 TRs, 65 min, where the\n  paper says one subject played 90 min in six 15-min runs. The S7 data are float32 and not exactly\n  z-scored per voxel over the session; S1's are. No flash TRs in S7, as the paper says. The S1\n  game data have 73,594 voxels, which matches no mapper (S1's mapper has 51,608, as the S1\n  attention data), so S1's game weights cannot be put on fsaverage with the files given. S7's\n  data match S7's mapper. The game state columns are not in the order of Table 1.\n- No recording is deposited twice: same-frame TRs of different conditions are only weakly\n  correlated (printed above), and the subjects' voxel counts all differ.\n\"\"\")\n\nmd(r\"\"\"\n## Attention task: CSI per subject and condition\n\nShared by fig1-csi-s2, att-csi-group and supp-csi-per-subject. The CSI of the four presence\nclusters within each condition, in the state space fitted once on the three conditions stacked.\nBecause the third axis is undefined in these data, three readings are computed:\n\n- R3, \"code\": the paper's code run as written on the full voxel data (its third axis is whatever\n  rounding gives on this machine);\n- R2, \"random third axis\": the median over 100 random third axes, orthogonal to the human and\n  vehicle axes in the space of the 24 PCs (the distribution of what an arbitrary third axis gives);\n- R1, \"2D\": the human-vehicle plane alone.\n\nCSI values are means over 10 Monte Carlo seeds. The null refits the state space with permuted\npresence labels, 1000 times per reading of the claims file: (a) the (human, vehicle) rows shuffled\nover all TRs, and (b) circularly shifted by a random lag within each condition. Each null draw uses\na random third axis (for R3 and R2) or the plane (for R1) and one Monte Carlo seed.\n\"\"\")\n\ncode(r\"\"\"\nN_PERM = 1000\nrng = np.random.default_rng(1)\ncsi_obs, csi_null, csi_seedsd = {}, {}, {}\nfor s in ss.ATT_SUBJECTS:\n    t = time.time()\n    Z = att[s][\"Z\"]\n    r3 = np.array([ss.att_csis(att[s][\"code_pos\"], pcode, np.random.default_rng(k)) for k in range(10)])\n    r1 = np.array([ss.att_csis(ss.att_positions(Z, X_att, \"2d\"), pcode, np.random.default_rng(k)) for k in range(10)])\n    r2 = np.array([ss.att_csis(ss.att_positions(Z, X_att, \"random\", rng), pcode, rng) for _ in range(100)])\n    csi_obs[s] = {\"R3\": r3.mean(0), \"R2\": np.median(r2, 0), \"R1\": r1.mean(0),\n                  \"R2_lo\": np.percentile(r2, 5, axis=0), \"R2_hi\": np.percentile(r2, 95, axis=0)}\n    csi_seedsd[s] = {\"R3\": r3.std(0), \"R1\": r1.std(0)}\n    for reading in \"ab\":\n        n3, n2 = [], []\n        for _ in range(N_PERM):\n            Xp = ss.shuffle_presence(X_att, reading, rng)\n            pc_p = ss.presence_code(Xp)\n            n3.append(ss.att_csis(ss.att_positions(Z, Xp, \"random\", rng), pc_p, rng))\n            n2.append(ss.att_csis(ss.att_positions(Z, Xp, \"2d\"), pc_p, rng))\n        csi_null[s, reading, \"3d\"] = np.array(n3)\n        csi_null[s, reading, \"2d\"] = np.array(n2)\n    print(f\"{s} done in {time.time()-t:.0f} s\")\n\ndef pval(obs, null):\n    return (1 + (null >= obs).sum(0)) / (len(null) + 1)\n\nrows = []\nfor s in ss.ATT_SUBJECTS:\n    for ci, c in enumerate(ss.CONDITIONS):\n        row = dict(subject=s, condition=c, R3_code=csi_obs[s][\"R3\"][ci], R3_seed_sd=csi_seedsd[s][\"R3\"][ci],\n                   R2_median=csi_obs[s][\"R2\"][ci], R2_5pct=csi_obs[s][\"R2_lo\"][ci], R2_95pct=csi_obs[s][\"R2_hi\"][ci],\n                   R1_2d=csi_obs[s][\"R1\"][ci])\n        for reading in \"ab\":\n            row[f\"null3d_max_{reading}\"] = csi_null[s, reading, \"3d\"][:, ci].max()\n            row[f\"null2d_max_{reading}\"] = csi_null[s, reading, \"2d\"][:, ci].max()\n        rows.append(row)\ncsi_table = pd.DataFrame(rows)\nprint(csi_table.round(3).to_string())\nprint(f\"null p-values are at most 1/{N_PERM+1} = {1/(N_PERM+1):.4f} when the observed CSI exceeds every null value\")\nprint(f\"elapsed {time.time()-T0:.0f} s, peak memory {mem_gb():.1f} GB\")\n\"\"\")\n\nmd(r\"\"\"\n### fig1-csi-s2\n\n> In subject S2 the four presence states (neither, humans only, vehicles only, both) are\n> significantly separated in the attention-task state space, with a cluster separation index of\n> 0.75 for attend-humans, 0.69 for attend-vehicles and 0.67 for passive viewing.\n\"\"\")\n\ncode(r\"\"\"\nexp = {\"human\": (0.75, 0.075), \"vehicle\": (0.69, 0.069), \"passive\": (0.67, 0.067)}\nt = csi_table[csi_table.subject == \"S2\"].set_index(\"condition\")\nfor reading in [\"R3_code\", \"R2_median\", \"R1_2d\"]:\n    null = \"null2d\" if reading == \"R1_2d\" else \"null3d\"\n    for c in [\"human\", \"vehicle\", \"passive\"]:\n        v = t.loc[c, reading]; e, tol = exp[c]\n        print(f\"{reading:9s} {c:8s} CSI {v:.3f} (expected {e} +/- {tol}; within: {abs(v-e) <= tol}); \"\n              f\"above every null value: (a) {v > t.loc[c, null + '_max_a']} (max {t.loc[c, null + '_max_a']:.3f}), \"\n              f\"(b) {v > t.loc[c, null + '_max_b']} (max {t.loc[c, null + '_max_b']:.3f})\")\n    ok = all(abs(t.loc[c, reading] - exp[c][0]) <= exp[c][1] for c in exp)\n    print(f\"  -> {reading}: all three within tolerance: {ok}\")\nprint(\"R2 5 to 95% range over random third axes:\", {c: (round(t.loc[c, 'R2_5pct'], 3), round(t.loc[c, 'R2_95pct'], 3)) for c in exp})\n\"\"\", [\"claim:fig1-csi-s2\"])\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 3, figsize=(12, 4))\ncols = [\"#ff5100\", \"#0084ff\", \"#91d90d\", \"#a200ff\"]\npos = att[\"S2\"][\"code_pos\"]\nout = 0\nfor ax, (ci, c) in zip(axes, enumerate(ss.CONDITIONS)):\n    sl = ss.cond_slices()[ci]\n    p, k = pos[sl], pcode[sl]\n    sx = 1 if p[k == 3, 0].mean() > p[k == 0, 0].mean() else -1   # the code's sign rule\n    sy = 1 if p[k == 3, 1].mean() > p[k == 0, 1].mean() else -1\n    for j in range(4):\n        ax.scatter(sx * p[k == j, 0], sy * p[k == j, 1], s=4, alpha=0.4, c=cols[j], label=ss.PRESENCE_NAMES[j])\n        ax.scatter(sx * p[k == j, 0].mean(), sy * p[k == j, 1].mean(), marker=\"+\", s=300, c=\"k\")\n    out += int((np.abs(p[:, :2]) > 4).any(1).sum())\n    ax.set(xlim=(-4, 4), ylim=(-4, 4), title=f\"S2 {c}\", xlabel=\"human presence\", ylabel=\"vehicle presence\")\naxes[0].legend(markerscale=3, fontsize=7)\nplt.tight_layout(); plt.show()\nprint(f\"positions range {pos[:, :2].min():.2f} to {pos[:, :2].max():.2f}; {out} TRs outside the axes\")\n\"\"\", [\"claim:fig1-csi-s2\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### att-csi-group\n\n> Across subjects the presence states are distinctly and significantly separated in the\n> attention-task state space, with CSI 0.66 +/- 0.09 for attend-humans, 0.74 +/- 0.03 for\n> attend-vehicles and 0.53 +/- 0.24 for passive viewing (mean +/- std).\n\"\"\")\n\ncode(r\"\"\"\nexp = {\"human\": (0.66, 0.09), \"vehicle\": (0.74, 0.03), \"passive\": (0.53, 0.24)}\nfig_ref = {\"human\": np.mean([0.51, 0.75, 0.70, 0.66, 0.60]), \"vehicle\": np.mean([0.79, 0.69, 0.71, 0.74, 0.71]),\n           \"passive\": np.mean([0.64, 0.67, 0.05, 0.59, 0.61])}\nprint(\"second reference, means of the paper's per-subject values over the same five subjects:\",\n      {c: round(v, 3) for c, v in fig_ref.items()})\nfor reading in [\"R3_code\", \"R2_median\", \"R1_2d\"]:\n    null = \"2d\" if reading == \"R1_2d\" else \"3d\"\n    for c in [\"human\", \"vehicle\", \"passive\"]:\n        ci = ss.CONDITIONS.index(c)\n        v = csi_table[csi_table.condition == c][reading].values\n        e, tol = exp[c]\n        sig_a = {r: all(pval(csi_obs[s][reading.split('_')[0]][ci] if reading != 'R2_median' else csi_obs[s]['R2'][ci],\n                           csi_null[s, r, null][:, ci]) <= 1 / (N_PERM + 1) for s in ss.ATT_SUBJECTS) for r in \"ab\"}\n        grp_null = {r: np.mean([csi_null[s, r, null][:, ci] for s in ss.ATT_SUBJECTS], axis=0) for r in \"ab\"}\n        sig_b = {r: bool(v.mean() > grp_null[r].max()) for r in \"ab\"}\n        print(f\"{reading:9s} {c:8s} mean {v.mean():.3f} +/- {v.std(ddof=1):.3f} (SD over 5) (expected {e} +/- {tol}; \"\n              f\"within: {abs(v.mean()-e) <= tol}); every subject above every null value: {sig_a}; \"\n              f\"mean above every mean null value: {sig_b} (max mean null a {grp_null['a'].max():.3f}, b {grp_null['b'].max():.3f})\")\n\"\"\", [\"claim:att-csi-group\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### supp-csi-per-subject\n\n> In each subject and each attention condition the CSI is significant, with the values printed in\n> Supplementary Figures 1 and 2.\n\"\"\")\n\ncode(r\"\"\"\nsupp = {(\"S1\", \"human\"): 0.51, (\"S1\", \"vehicle\"): 0.79, (\"S1\", \"passive\"): 0.64,\n        (\"S3\", \"human\"): 0.70, (\"S3\", \"vehicle\"): 0.71, (\"S3\", \"passive\"): 0.05,\n        (\"S5\", \"human\"): 0.66, (\"S5\", \"vehicle\"): 0.74, (\"S5\", \"passive\"): 0.59,\n        (\"S6\", \"human\"): 0.60, (\"S6\", \"vehicle\"): 0.71, (\"S6\", \"passive\"): 0.61}\nfor reading in [\"R3_code\", \"R2_median\", \"R1_2d\"]:\n    null = \"null2d\" if reading == \"R1_2d\" else \"null3d\"\n    rows, n_in, n_sig = [], 0, {\"a\": 0, \"b\": 0}\n    for (s, c), e in supp.items():\n        r = csi_table[(csi_table.subject == s) & (csi_table.condition == c)].iloc[0]\n        tol = 0.1 * e\n        inside = abs(r[reading] - e) <= tol + 1e-12\n        n_in += inside\n        for rd in \"ab\":\n            n_sig[rd] += r[reading] > r[f\"{null}_max_{rd}\"]\n        rows.append(dict(subject=s, condition=c, expected=e, measured=round(r[reading], 3), within=inside,\n                         null_max_a=round(r[f\"{null}_max_a\"], 3), null_max_b=round(r[f\"{null}_max_b\"], 3)))\n    print(reading)\n    print(pd.DataFrame(rows).to_string(index=False))\n    print(f\"  {n_in} of 12 within tolerance; above every null value (p <= {1/(N_PERM+1):.4f} < 0.01): \"\n          f\"reading a {n_sig['a']} of 12, reading b {n_sig['b']} of 12\\n\")\ni = ss.CONDITIONS.index(\"passive\")\nprint(\"S3 passive: R3 mean over 10 seeds %.3f (seed SD %.3f); R2 5-95%% range %.3f to %.3f\"\n      % (csi_obs[\"S3\"][\"R3\"][i], csi_seedsd[\"S3\"][\"R3\"][i], csi_obs[\"S3\"][\"R2_lo\"][i], csi_obs[\"S3\"][\"R2_hi\"][i]))\n\"\"\", [\"claim:supp-csi-per-subject\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### att-passive-lower\n\n> Attention increases state separation; the CSI under passive viewing is significantly lower than\n> under the attentive conditions in five of the six subjects.\n\nReadings of the claims file: (a) passive against each attentive condition, both differences\nsignificant; (b) passive against the mean of the two attentive CSIs. Null: the condition labels\npermuted between TRs, presence labels kept, either (i) refitting the state space each time, or\n(ii) keeping the fitted positions. How the condition labels are permuted is not fixed; two schemes\nare run: \"matched\", where at each movie time point the three TRs showing the same frame get the\nthree conditions in random order (each condition keeps the same presence labels), and \"global\", a\nshuffle over all TRs. One-sided, passive lower; 1000 permutations, so a subject counts at the\npaper's threshold when its difference exceeds every null value (p <= 0.001, the bound reached).\nThe observed CSIs are those of R3 (the code's positions); for (i) the refitted null uses the\ncode's QR, which now gives the third axis a real weight. R1 (the plane) is shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(2)\ndef stats_ab(c):  # c: CSI (passive, human, vehicle)\n    return np.array([c[1] - c[0], c[2] - c[0], c[1:].mean() - c[0]])\npl_rows = []\nfor s in ss.ATT_SUBJECTS:\n    Z = att[s][\"Z\"]\n    for variant, obs_pos in [(\"R3\", att[s][\"code_pos\"]), (\"R1\", ss.att_positions(Z, X_att, \"2d\"))]:\n        obs_c = np.mean([ss.att_csis(obs_pos, pcode, np.random.default_rng(k)) for k in range(10)], axis=0)\n        obs = stats_ab(obs_c)\n        for scheme in [\"matched\", \"global\"]:\n            for refit in [\"i\", \"ii\"]:\n                null = []\n                for _ in range(N_PERM):\n                    mem = ss.shuffle_conditions(900, scheme, rng)\n                    if refit == \"i\":\n                        Xp = ss.members_to_X(X_att, mem)\n                        p = ss.att_positions(Z, Xp, \"qr\" if variant == \"R3\" else \"2d\")\n                    else:\n                        p = obs_pos\n                    null.append(stats_ab(ss.att_csis(p, pcode, rng, members=mem)))\n                null = np.array(null)\n                p_one = (1 + (null >= obs).sum(0)) / (N_PERM + 1)\n                pl_rows.append(dict(subject=s, variant=variant, scheme=scheme, null=refit,\n                                    passive=obs_c[0], human=obs_c[1], vehicle=obs_c[2],\n                                    d_human=obs[0], d_vehicle=obs[1], d_mean=obs[2],\n                                    p_human=p_one[0], p_vehicle=p_one[1], p_mean=p_one[2]))\npl = pd.DataFrame(pl_rows)\npmin = 1 / (N_PERM + 1)\npl[\"a_at_bound\"] = (pl.p_human <= pmin) & (pl.p_vehicle <= pmin)\npl[\"b_at_bound\"] = pl.p_mean <= pmin\npl[\"a_p05\"] = (pl.p_human < 0.05) & (pl.p_vehicle < 0.05)\npl[\"b_p05\"] = pl.p_mean < 0.05\nprint(pl.round(4).to_string(index=False))\ncnt = pl.groupby([\"variant\", \"scheme\", \"null\"])[[\"a_at_bound\", \"b_at_bound\", \"a_p05\", \"b_p05\"]].sum()\nprint(\"\\nsubjects of 5 with passive significantly lower:\")\nprint(cnt.to_string())\nprint(f\"elapsed {time.time()-T0:.0f} s\")\n\"\"\", [\"claim:att-passive-lower\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### att-classification\n\n> Held-out TRs of the attention task are classified into the 12 labels (four presence states by\n> three attention conditions) from their position in the learned state space at 48.4 +/- 7.6%\n> across subjects, well above the chance of 8.3%.\n\n10-fold cross-validation over the 2700 stacked TRs; in each fold the PCA and the state space are\nfitted on the training TRs (Methods, Quantification, paragraph 2), the held-out TRs are projected\nand z-scored with the training statistics, and assigned to the nearest of the 12 training\nclusters. Readings: folds (a) contiguous tenths or (b) random TRs; nearest cluster by (a) the\nEuclidean distance to the mean or (b) the density of the cluster's normal. Null: the training\nTRs' state rows permuted and the full fit repeated, 1000 times. In the training folds the two\nattentive conditions are no longer exactly zero-mean, so the third axis gets a small fitted weight.\n\"\"\")\n\ncode(r\"\"\"\nlab12 = pcode + 4 * np.repeat(np.arange(3), 900)\nclasses12 = np.arange(12)\nN_PERM_CLF = 1000\nrng = np.random.default_rng(3)\nclf_rows, clf_null = [], {}\nfor s in ss.ATT_SUBJECTS:\n    t = time.time()\n    for scheme in [\"contig\", \"random\"]:\n        fs = ss.fold_scores(att[s][\"G\"], ss.folds(2700, scheme, rng))\n        for rule in [\"euclid\", \"density\"]:\n            accs = []\n            for tr, te, Ztr, Zte in fs:\n                ptr, pte = ss.project_fold(Ztr, Zte, X_att[tr])\n                accs.append((ss.nearest_cluster(ptr, lab12[tr], pte, classes12, rule) == lab12[te]).mean())\n            null = np.zeros(N_PERM_CLF)\n            for k in range(N_PERM_CLF):\n                a = []\n                for tr, te, Ztr, Zte in fs:\n                    perm = rng.permutation(len(tr))\n                    ptr, pte = ss.project_fold(Ztr, Zte, X_att[tr][perm])\n                    a.append((ss.nearest_cluster(ptr, lab12[tr][perm], pte, classes12, rule) == lab12[te]).mean())\n                null[k] = np.mean(a)\n            clf_null[s, scheme, rule] = null\n            clf_rows.append(dict(subject=s, folds=scheme, rule=rule, accuracy=np.mean(accs), fold_sd=np.std(accs),\n                                 null_mean=null.mean(), null_max=null.max(), p=(1 + (null >= np.mean(accs)).sum()) / (N_PERM_CLF + 1)))\n    print(f\"{s} done in {time.time()-t:.0f} s\")\nclf = pd.DataFrame(clf_rows)\nprint((clf.assign(accuracy=100 * clf.accuracy, fold_sd=100 * clf.fold_sd, null_mean=100 * clf.null_mean,\n                  null_max=100 * clf.null_max)).round(2).to_string(index=False))\nprint(\"\\nacross subjects (percent):\")\nfor (scheme, rule), g in clf.groupby([\"folds\", \"rule\"]):\n    gnull = np.mean([clf_null[s, scheme, rule] for s in ss.ATT_SUBJECTS], axis=0)\n    m = 100 * g.accuracy.mean()\n    print(f\"  folds {scheme:6s} {rule:7s}: {m:.1f} +/- {100*g.accuracy.std(ddof=1):.1f} (SD over 5); within 48.4 +/- 7.6: \"\n          f\"{abs(m-48.4) <= 7.6}; chance under this procedure (mean null) {100*gnull.mean():.1f}; max of mean null {100*gnull.max():.1f}; \"\n          f\"above every null mean: {m > 100*gnull.max()}\")\nprint(f\"elapsed {time.time()-T0:.0f} s\")\n\"\"\", [\"claim:att-classification\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### att-weights-cortex (blocked)\n\n> The human-presence dimension of the attention-task state space has its weights in face and body\n> areas (FFA, OFA, EBA), MT+, LO, the frontal operculum and the inferior frontal sulcus; the\n> vehicle-presence dimension in RSC, PPA, OPA, IPS, FEF and around the inferior frontal sulcus.\n\nThe criterion compares mean weights within the subjects' functional ROIs, which the paper drew\nfrom functional localizer and retinotopic mapping data (Methods, Preprocessing and Visualization,\nparagraph 2). The data set holds no ROI, localizer or retinotopy files (listing in the data check),\nthe paper deposits them nowhere else, and the code repository has none. A group atlas would be a\nsubstitute for the paper's per-subject ROIs, not the input the paper relies on, so it is not\nused. The claim is blocked as data_missing; nothing is computed for it here.\n\"\"\")\n\nmd(r\"\"\"\n## Video game task\n\nStates with no TRs are dropped (flash in S7; Supplementary Figure 4 shows no flash weights for\nthat subject), so S7's state space has 8 dimensions. Because the JSD is unchanged by affine maps,\nthe CSI does not depend on the order or signs of the dimensions; the dataset's column order is used.\n\"\"\")\n\nmd(r\"\"\"\n### game-csi\n\n> In the video game task the behavioural states are distinctly and significantly separated in the\n> 9-dimensional state space, with CSI 0.72 in subject S1 and 0.62 in S7.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(4)\nexp_g = {\"S1\": (0.72, 0.072), \"S7\": (0.62, 0.062)}\ngame_csi = {}\nfor s in ss.GAME_SUBJECTS:\n    X, names = ss.game_matrix(game[s][\"X\"], game[s][\"labels\"], \"dataset\")\n    Z = game[s][\"Z\"]\n    pos = ss.positions(Z, X)\n    for reading in \"abc\":\n        mem, nm, dropped = ss.game_members(X, names, reading)\n        vals = [ss.csi(pos, mem, np.random.default_rng(k)) for k in range(10)]\n        null = []\n        for _ in range(N_PERM):\n            Xp = X[rng.permutation(len(X))]\n            memp, _, _ = ss.game_members(Xp, names, reading)\n            null.append(ss.csi(ss.positions(Z, Xp), memp, rng))\n        null = np.array(null)\n        game_csi[s, reading] = np.mean(vals)\n        e, tol = exp_g[s]\n        print(f\"{s} reading {reading}: {len(mem)} clusters (sizes {[int(m.sum()) for m in mem]}; dropped {dropped}); \"\n              f\"CSI {np.mean(vals):.3f} (seed SD {np.std(vals):.3f}); expected {e} +/- {tol}, within: {abs(np.mean(vals)-e) <= tol}; \"\n              f\"null mean {null.mean():.3f}, max {null.max():.3f}; above every null value: {np.mean(vals) > null.max()}\")\nprint(f\"elapsed {time.time()-T0:.0f} s\")\n\"\"\", [\"claim:game-csi\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### game-mutual-negative-projection\n\n> The mutually exclusive states engage close and safe explore each project negatively onto the\n> other's dimension of the video game state space.\n\nReadings of the claims file: sign (a) each dimension oriented so its own state's TRs have a\npositive mean, (b) the diagonal of R positive; order of the variables in the QR (i) Table 1, (ii)\nthe data set's columns. Null: the rows of the state matrix permuted and refitted, 20,000 times\n(shared with fig3b-state-relations), one-sided for a negative mean.\n\"\"\")\n\ncode(r\"\"\"\nN_PERM_G = 20000\nrng = np.random.default_rng(5)\nproj = {}\nfor s in ss.GAME_SUBJECTS:\n    Z = game[s][\"Z\"]\n    for order in [\"table1\", \"dataset\"]:\n        X, names = ss.game_matrix(game[s][\"X\"], game[s][\"labels\"], order)\n        perms = [rng.permutation(len(X)) for _ in range(N_PERM_G)]\n        for sign in [\"own\", \"diag\"]:\n            M = ss.projection_matrix(ss.positions(Z, X, sign), X)\n            null = np.array([ss.projection_matrix(ss.positions(Z, X[p], sign), X[p]) for p in perms])\n            proj[s, order, sign] = (M, null, names)\nrows = []\nfor (s, order, sign), (M, null, names) in proj.items():\n    i, j = names.index(\"engage close\"), names.index(\"safe explore\")\n    p1 = (1 + (null[:, i, j] <= M[i, j]).sum()) / (N_PERM_G + 1)\n    p2 = (1 + (null[:, j, i] <= M[j, i]).sum()) / (N_PERM_G + 1)\n    rows.append(dict(subject=s, order=order, sign=sign, ec_on_se=M[i, j], p_ec_on_se=p1, se_on_ec=M[j, i], p_se_on_ec=p2,\n                     both_negative_p05=(M[i, j] < 0) and (M[j, i] < 0) and p1 < 0.05 and p2 < 0.05))\nmn = pd.DataFrame(rows)\nprint(mn.round(5).to_string(index=False))\nprint(\"\\nreadings with both means negative and p < 0.05 in both subjects:\")\nprint(mn.groupby([\"order\", \"sign\"]).both_negative_p05.sum().to_string())\nprint(f\"elapsed {time.time()-T0:.0f} s\")\n\"\"\", [\"claim:game-mutual-negative-projection\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### fig3b-state-relations\n\n> States of the video game project at significant non-zero positions on other states' dimensions,\n> an asymmetric pattern found in both subjects that differs between them.\n\nFor each ordered pair of different states, the mean position of the row state's TRs on the column\nstate's dimension, two-sided permutation p from the same 20,000 permutations; Bonferroni over (a)\nthe off-diagonal pairs or (b) every cell, at 0.01.\n\"\"\")\n\ncode(r\"\"\"\nres3b = {}\nfor (s, order, sign), (M, null, names) in proj.items():\n    d = len(names)\n    p = (1 + (np.abs(null) >= np.abs(M)[None]).sum(0)) / (N_PERM_G + 1)\n    off = ~np.eye(d, dtype=bool)\n    for bonf, ntest in [(\"a\", d * (d - 1)), (\"b\", d * d)]:\n        sig = (p < 0.01 / ntest) & off\n        asym = int((sig != sig.T).sum() // 2)\n        res3b[s, order, sign, bonf] = (sig, names)\n        print(f\"{s} order {order:7s} sign {sign:4s} Bonferroni {bonf} ({ntest} tests, threshold {0.01/ntest:.2e}): \"\n              f\"{int(sig.sum())} significant off-diagonal pairs; pairs significant in one direction only: {asym}\")\nprint(f\"smallest attainable p: {1/(N_PERM_G+1):.2e}\")\nfor order in [\"table1\", \"dataset\"]:\n    for sign in [\"own\", \"diag\"]:\n        for bonf in \"ab\":\n            s1, n1 = res3b[\"S1\", order, sign, bonf]\n            s7, n7 = res3b[\"S7\", order, sign, bonf]\n            set1 = {(n1[i], n1[j]) for i, j in zip(*np.nonzero(s1))}\n            set7 = {(n7[i], n7[j]) for i, j in zip(*np.nonzero(s7))}\n            print(f\"order {order:7s} sign {sign:4s} Bonferroni {bonf}: S1 {len(set1)}, S7 {len(set7)}, shared {len(set1 & set7)}, \"\n                  f\"sets differ: {set1 != set7}\")\nM, null, names = proj[\"S1\", \"table1\", \"own\"]\nprint(\"\\nS1, Table 1 order, own sign: mean position of row state's TRs on column dimension\")\nprint(pd.DataFrame(M, index=names, columns=names).round(2).to_string())\nM, null, names = proj[\"S7\", \"table1\", \"own\"]\nprint(\"\\nS7, Table 1 order, own sign\")\nprint(pd.DataFrame(M, index=names, columns=names).round(2).to_string())\nfor s in ss.GAME_SUBJECTS:\n    sig, names = res3b[s, \"table1\", \"own\", \"a\"]\n    print(f\"\\n{s} significant pairs (Table 1 order, own sign, Bonferroni a), row state -> column dimension:\")\n    print(pd.DataFrame(np.where(sig, \"x\", \".\"), index=names, columns=names).to_string())\n\"\"\", [\"claim:fig3b-state-relations\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### game-classification\n\n> Held-out TRs of the video game task are classified into the nine behavioural states from their\n> position in the learned state space with balanced accuracy 32.8 +/- 3.8% in S1 and 30.4 +/- 4.2%\n> in S7, above the chance of 11%.\n\nFolds and distance as in att-classification. Labels: (a) TRs with exactly one state only; (b)\nevery labelled TR, a prediction correct for each of its states it names, recall per state over\nthe TRs that have it. The state space is fitted on all training TRs with the full state matrix.\nClasses with no TRs are left out; for the density rule, a class needs more training TRs than\ndimensions, so classes with fewer than 2 x (dimensions + 1) TRs under the label reading are left\nout of that rule (listed below). Null: training state rows permuted, 1000 times.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(6)\ngc_rows, gc_null = [], {}\nfor s in ss.GAME_SUBJECTS:\n    t = time.time()\n    X, names = ss.game_matrix(game[s][\"X\"], game[s][\"labels\"], \"dataset\")\n    n, d = X.shape\n    nst = X.sum(1)\n    for scheme in [\"contig\", \"random\"]:\n        fs = ss.fold_scores(game[s][\"G\"], ss.folds(n, scheme, rng))\n        for lab in \"ab\":\n            use = (nst == 1) if lab == \"a\" else (nst >= 1)\n            single = np.where(nst == 1, X.argmax(1), -1)\n            for rule in [\"euclid\", \"density\"]:\n                counts = X[use].sum(0)\n                minc = 1 if rule == \"euclid\" else 2 * (d + 1)\n                classes = [c for c in range(d) if counts[c] >= minc]\n                left = [names[c] for c in range(d) if counts[c] < minc]\n                def run(perm_rng=None):\n                    accs = []\n                    for tr, te, Ztr, Zte in fs:\n                        Xtr = X[tr] if perm_rng is None else X[tr][perm_rng.permutation(len(tr))]\n                        ptr, pte = ss.project_fold(Ztr, Zte, Xtr)\n                        if lab == \"a\":\n                            ntr = Xtr.sum(1)\n                            lab_tr = np.where(ntr == 1, Xtr.argmax(1), -1)\n                            cl = [c for c in classes if (lab_tr == c).sum() > (d if rule == \"density\" else 0)]\n                            pred = ss.nearest_cluster(ptr, lab_tr, pte, cl, rule)\n                        else:\n                            # one cluster per state from every training TR that has it\n                            if rule == \"euclid\":\n                                means = np.array([ptr[Xtr[:, c] > 0].mean(0) for c in classes])\n                                pred = np.asarray(classes)[((pte[:, None] - means[None]) ** 2).sum(-1).argmin(1)]\n                            else:\n                                ll = np.column_stack([ss._logpdf(pte, *ss._fit_normal(ptr[Xtr[:, c] > 0])) for c in classes])\n                                pred = np.asarray(classes)[ll.argmax(1)]\n                        m = use[te]\n                        true_sets = [set(np.nonzero(X[i])[0]) & set(classes) for i in te[m]]\n                        keep = np.array([len(ts) > 0 for ts in true_sets])\n                        accs.append(ss.balanced_accuracy([ts for ts, k in zip(true_sets, keep) if k], pred[m][keep], classes))\n                    return np.array(accs)\n                accs = run()\n                null = np.array([run(rng).mean() for _ in range(N_PERM_CLF)])\n                gc_null[s, scheme, lab, rule] = null\n                gc_rows.append(dict(subject=s, folds=scheme, labels=lab, rule=rule, n_classes=len(classes), left_out=left,\n                                    bal_acc=100 * accs.mean(), fold_sd=100 * accs.std(), chance=100 / len(classes),\n                                    null_mean=100 * null.mean(), null_max=100 * null.max(),\n                                    p=(1 + (null >= accs.mean()).sum()) / (N_PERM_CLF + 1)))\n    print(f\"{s} done in {time.time()-t:.0f} s\")\ngcl = pd.DataFrame(gc_rows)\nexp_c = {\"S1\": (32.8, 3.8), \"S7\": (30.4, 4.2)}\ngcl[\"within\"] = [abs(r.bal_acc - exp_c[r.subject][0]) <= exp_c[r.subject][1] for r in gcl.itertuples()]\ngcl[\"above_null\"] = gcl.bal_acc > gcl.null_max\nprint(gcl.round(4).to_string(index=False))\nprint(\"\\nreadings where both subjects are within tolerance and above every null value:\")\nboth = gcl.groupby([\"folds\", \"labels\", \"rule\"]).apply(lambda g: bool((g.within & g.above_null).all()), include_groups=False)\nprint(both.to_string())\nprint(f\"elapsed {time.time()-T0:.0f} s, peak memory {mem_gb():.1f} GB\")\n\"\"\", [\"claim:game-classification\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n### game-weights-two-groups (blocked)\n\n> The video game state dimensions fall into two groups, dead, round start, safe explore, unsafe\n> explore and flash in TPJ, precuneus and prefrontal cortex (default-mode areas), and kill, engage\n> close, engage far and run away in motor, premotor and supplementary motor areas, IPS, FEF and\n> SEF; the weights are largely consistent across the two subjects.\n\nThe criterion needs region definitions the data set does not hold (the paper's functional ROIs,\nwhich are not public), and for S1 the game data (73,594 voxels) match no mapper in the data set\n(S1's mapper has 51,608 voxels), so S1's weights cannot be placed on the cortex with the files\ngiven. Blocked as data_missing; nothing is computed for it here.\n\"\"\")\n\nmd(\"## Summary\\n\\n...\")\n\nnb = nbf.v4.new_notebook()\nnb[\"cells\"] = cells\nnb[\"metadata\"][\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/zhang-2021/reproduce_zhang_2021.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude/gen_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 - <<'EOF'
p='gen_nb.py'; s=open(p).read()
old_start = s.index('    att[s] = dict(G=G, Z=Z, code_pos=cp, ve=ve)')
old_end = s.index('""", ["sanity"])', old_start)
s = s[:old_start] + '''    att[s] = dict(G=G, Z=Z, code_pos=cp, ve=ve, n_vox=d["n_vox"])
    print(f"{s}: {d['n_vox']} voxels ({d['n_zero_vox']} constant, {d['n_nan']} NaN), voxel means {d['vox_mean_range'][0]:.3f} to "
          f"{d['vox_mean_range'][1]:.3f}, SDs {d['vox_sd_range'][0]:.3f} to {d['vox_sd_range'][1]:.3f}; "
          f"24 PCs explain {ve:.1%}; |weights| in PC space human {np.linalg.norm(coef[0]):.3g}, vehicle "
          f"{np.linalg.norm(coef[1]):.3g}, attention {np.linalg.norm(coef[2]):.3g}; |r| rewrite vs code per axis "
          f"{np.round(corr, 4)}; mean r of same-frame TRs {same}; {time.time()-t:.0f} s, peak memory {mem_gb():.1f} GB")
nv = [att[s]["n_vox"] for s in att]
print(f"voxels per subject: mean {np.mean(nv):.0f}, SD {np.std(nv, ddof=1):.0f} over {len(nv)} subjects (paper: 48,673 +/- 4,382 over six)")
''' + s[old_end:]
s = s.replace('''      {s: att[s]["G"].shape and ss.hdf_layout(f"VisualAttention/Data/deconv/{s}.hdf")[0][1][1] for s in ss.ATT_SUBJECTS})''','''      {s: att[s]["n_vox"] for s in att})''')
s = s.replace('''        sig_a = {r: all(pval(csi_obs[s][reading.split('_')[0]][ci] if reading != 'R2_median' else csi_obs[s]['R2'][ci],
                           csi_null[s, r, null][:, ci]) <= 1 / (N_PERM + 1) for s in ss.ATT_SUBJECTS) for r in "ab"}''','''        key = reading.split("_")[0]
        sig_a = {r: all(pval(csi_obs[s][key][ci], csi_null[s, r, null][:, ci]) <= 1 / (N_PERM + 1)
                        for s in ss.ATT_SUBJECTS) for r in "ab"}''')
s = s.replace('''    for (s, c), e in supp.items():
        r = csi_table''','''    for (s, c), e in supp.items():
        if s not in ss.ATT_SUBJECTS:
            continue
        r = csi_table''')
s = s.replace('''nbf.write(nb, "entries/zhang-2021/reproduce_zhang_2021.ipynb")''','''import sys
out = "entries/zhang-2021/reproduce_zhang_2021.ipynb"
if "dev" in sys.argv:
    for c in nb["cells"]:
        if c.cell_type == "code":
            c.source = (c.source.replace("N_PERM = 1000", "N_PERM = 20").replace("N_PERM_CLF = 1000", "N_PERM_CLF = 10")
                        .replace("N_PERM_G = 20000", "N_PERM_G = 200").replace("import statespace as ss", "import statespace as ss\\nss.ATT_SUBJECTS = ['S2', 'S3']"))
    out = "/tmp/claude/dev_nb.ipynb"
nbf.write(nb, out)''')
open(p,'w').write(s)
EOF
grep -n "pval\|key = " gen_nb.py | head; cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat nbconvert nbclient && python /tmp/claude/gen_nb.py dev && cp entries/zhang-2021/statespace.py /tmp/claude/ && cd /tmp/claude && date -u && time jupyter nbconvert --to notebook --execute dev_nb.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5; date -u
```

```
331:def pval(obs, null):
415:        key = reading.split("_")[0]
416:        sig_a = {r: all(pval(csi_obs[s][key][ci], csi_null[s, r, null][:, ci]) <= 1 / (N_PERM + 1)
46 cells
Sat Nov 14 10:20:12 UTC 2026
[NbConvertApp] Converting notebook dev_nb.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 231957 bytes to dev_out.ipynb

real	2m3.675s
user	4m12.725s
sys	0m6.176s
Sat Nov 14 10:22:16 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 -c "
import json;nb=json.load(open('dev_out.ipynb'))
for c in nb['cells']:
  if c['cell_type']!='code': continue
  for o in c.get('outputs',[]):
    t=o.get('text') or o.get('data',{}).get('text/plain') or o.get('ename','')+str(o.get('evalue',''))
    if isinstance(t,list): t=''.join(t)
    if 'image/png' in o.get('data',{}): t='[image]'
    print(t[:6000])
  print('=====')
" | grep -v "^  .*MB  vim"
```

```
<persisted-output>
Output too large (40.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bj73se3dh.txt

Preview (first 2KB):
=====
39 files under vim-4/
5989fd2bc00fadf058eac9e7e742ad7d VisualAttention/Data/deconv/S1.hdf
94a06a22a634efb4370b3061b532744f VisualAttention/Data/deconv/S2.hdf
16758cb38128a43182c495660ac77eb6 VisualAttention/Data/deconv/S3.hdf
782fcf8c74b82812fb9fb8e7e106b285 VisualAttention/Data/deconv/S5.hdf
57fc3c680adac346ca41461e1a891592 VisualAttention/Data/deconv/S6.hdf
52e2cee2155281256192c2e9ded39383 VisualAttention/Stimuli/states.hdf
54143a9de19a34d647856693588dfc9d VisualAttention/Stimuli/semantics.hdf
c0ea35bd959465d7e03cf5b369002640 VideoGame/Data/S1.npy
0ed00d89f585636b9091d56fc1a9ed81 VideoGame/Data/S7.npy
d66b6a346ebfa13948b71da7a8d810a8 VideoGame/Stimuli/S1.hdf
b5b5bb06946d4d6df1eb9c813d3f5825 VideoGame/Stimuli/S7.hdf

=====
VisualAttention/Data/S1.hdf                human                        (900, 51608)       float32
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/VisualAttention\/Stimuli\/states.hdf  /,$p' /home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bj73se3dh.txt | grep -v "Mappers/S" | cut -c1-400 | head -230
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: This Bash command contains multiple operations. The following part requires approval: sed -n '/VisualAttention\/Stimuli\/states.hdf  /,$p' /home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bj73se3dh.txt
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a6b0e348-b980-447f-8a58-17c6e985f193/tool-results/bj73se3dh.txt",
 "offset": 60
}
```

```
60	VideoGame/Stimuli/S7.hdf                   behavioural_state            (1320, 9)          float32
61	VideoGame/Stimuli/S7.hdf                   state_labels                 (9,)               |S20
62	
63	Mappers/S1.hdf                             pixmap_data                  (1149053,)         float64
64	Mappers/S1.hdf                             pixmap_indices               (1149053,)         int32
65	Mappers/S1.hdf                             pixmap_indptr                (1155715,)         int32
66	Mappers/S1.hdf                             pixmap_shape                 (2,)               int64
67	Mappers/S1.hdf                             pixmask                      (1883, 1024)       bool
68	Mappers/S1.hdf                             vox_to_fsavg_left_data       (162133,)          float64
69	Mappers/S1.hdf                             vox_to_fsavg_left_indices    (162133,)          int32
70	Mappers/S1.hdf                             vox_to_fsavg_left_indptr     (163843,)          int32
71	Mappers/S1.hdf                             vox_to_fsavg_left_shape      (2,)               int64
72	Mappers/S1.hdf                             vox_to_fsavg_right_data      (162350,)          float64
73	Mappers/S1.hdf                             vox_to_fsavg_right_indices   (162350,)          int32
74	Mappers/S1.hdf                             vox_to_fsavg_right_indptr    (163843,)          int32
75	Mappers/S1.hdf                             vox_to_fsavg_right_shape     (2,)               int64
76	
77	Mappers/S2.hdf                             pixmap_data                  (1194714,)         float64
78	Mappers/S2.hdf                             pixmap_indices               (1194714,)         int32
79	Mappers/S2.hdf                             pixmap_indptr                (1216516,)         int32
[... 390 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 - <<'EOF'
p='gen_nb.py'; s=open(p).read()
s=s.replace("mean_norm = [np.sqrt(G[sl, sl].sum()) / 900 for sl in ss.cond_slices()]",
            "mean_norm = [np.sqrt(max(G[sl, sl].sum(), 0.0)) / 900 for sl in ss.cond_slices()]  # rounding can make a zero sum slightly negative")
old_start=s.index("                def run(perm_rng=None):")
old_end=s.index("                accs = run()")
new='''                # held-out TRs scored under this label reading, and which of the classes each has
                scored = [(use[te], X[te][use[te]][:, classes] > 0) for tr, te, Ztr, Zte in fs]
                def run(perm_rng=None):
                    accs = []
                    for (tr, te, Ztr, Zte), (m, H) in zip(fs, scored):
                        Xtr = X[tr] if perm_rng is None else X[tr][perm_rng.permutation(len(tr))]
                        ptr, pte = ss.project_fold(Ztr, Zte, Xtr)
                        if lab == "a":
                            ntr = Xtr.sum(1)
                            lab_tr = np.where(ntr == 1, Xtr.argmax(1), -1)
                            cl = [c for c in classes if (lab_tr == c).sum() > (d if rule == "density" else 0)]
                            pred = ss.nearest_cluster(ptr, lab_tr, pte[m], cl, rule)
                        else:
                            # one cluster per state from every training TR that has it
                            if rule == "euclid":
                                means = np.array([ptr[Xtr[:, c] > 0].mean(0) for c in classes])
                                pred = np.asarray(classes)[((pte[m][:, None] - means[None]) ** 2).sum(-1).argmin(1)]
                            else:
                                ll = np.column_stack([ss._logpdf(pte[m], *ss._fit_normal(ptr[Xtr[:, c] > 0])) for c in classes])
                                pred = np.asarray(classes)[ll.argmax(1)]
                        accs.append(ss.balanced_accuracy(H, pred, classes))
                    return np.array(accs)
'''
s=s[:old_start]+new+s[old_end:]
open(p,'w').write(s)
EOF
cd entries/zhang-2021 && python3 - <<'EOF'
p='statespace.py'; s=open(p).read()
old_start=s.index("def balanced_accuracy(")
s=s[:old_start]+'''def balanced_accuracy(H, pred, classes):
    """Balanced accuracy (Brodersen et al. 2010, cited by the paper): the mean
    recall over the classes present. H [TR x classes] is True where a TR has
    the class (a TR may have several); the recall of class c is the fraction
    of the TRs that have c that are predicted as c."""
    rec = [(pred[H[:, k]] == c).mean() for k, c in enumerate(classes) if H[:, k].any()]
    return float(np.mean(rec))
'''
open(p,'w').write(s)
EOF
cp statespace.py /tmp/claude/; cd $TMPDIR && . dev/bin/activate && python /tmp/claude/gen_nb.py && cp entries/zhang-2021/reproduce_zhang_2021.ipynb /tmp/claude/full_nb.ipynb && python /tmp/claude/gen_nb.py dev && cd /tmp/claude && time jupyter nbconvert --to notebook --execute dev_nb.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARN | tail -3; python3 -c "
import json;nb=json.load(open('dev_out.ipynb'))
c=[c for c in nb['cells'] if c['cell_type']=='code'][-1]
print(''.join(o.get('text','') for o in c['outputs'])[:3000])"
```

```
Exit code 1
46 cells
46 cells
[NbConvertApp] Converting notebook dev_nb.ipynb to notebook
[NbConvertApp] Writing 231612 bytes to dev_out.ipynb

real	1m58.671s
user	4m7.560s
sys	0m5.879s
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    print(''.join(o.get('text','') for o in c['outputs'])[:3000])
          ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: sequence item 0: expected str instance, list found
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 -c "
import json;nb=json.load(open('dev_out.ipynb'))
c=[c for c in nb['cells'] if c['cell_type']=='code'][-1]
print(''.join(''.join(o.get('text','')) for o in c['outputs'])[:3000])"
```

```
S1 done in 7 s
S7 done in 4 s
subject  folds labels    rule  n_classes         left_out  bal_acc  fold_sd  chance  null_mean  null_max      p  within  above_null
     S1 contig      a  euclid          8           [kill]  45.8560   8.5907 12.5000    12.5557   16.1840 0.0909   False        True
     S1 contig      a density          7    [flash, kill]  44.0685   8.5189 14.2857    14.5566   17.1107 0.0909   False        True
     S1 contig      b  euclid          9               []  43.8204   7.6884 11.1111    10.3365   13.3072 0.0909   False        True
     S1 contig      b density          8          [flash]  42.7645  10.0310 12.5000    12.2398   15.4604 0.0909   False        True
     S1 random      a  euclid          8           [kill]  51.7523   3.2541 12.5000    13.1632   14.9328 0.0909   False        True
     S1 random      a density          7    [flash, kill]  56.0726   3.9690 14.2857    13.8153   17.5801 0.0909   False        True
     S1 random      b  euclid          9               []  46.8395   6.7300 11.1111    12.3957   14.2711 0.0909   False        True
     S1 random      b density          8          [flash]  50.6930   2.6067 12.5000    11.9686   13.4303 0.0909   False        True
     S7 contig      a  euclid          8               []  33.3724  12.1817 12.5000    12.0874   14.2719 0.0909    True        True
     S7 contig      a density          6 [run away, kill]  32.3700  14.5613 16.6667    16.9828   23.1333 0.0909    True        True
     S7 contig      b  euclid          8               []  27.5263   9.4400 12.5000    12.0466   15.8159 0.0909    True        True
     S7 contig      b density          7       [run away]  26.3924   8.8692 14.2857    14.9590   16.5197 0.0909    True        True
     S7 random      a  euclid          8               []  45.1389   9.2691 12.5000    13.2182   17.6588 0.0909   False        True
     S7 random      a density          6 [run away, kill]  45.4811   4.9419 16.6667    16.5908   22.1408 0.0909   False   
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021 && cat > entry.yaml <<'EOF'
schema_version: 1
name: zhang-2021
type: reproduction
title: Voxel-based state space modeling in a visual attention task and a video game (Zhang et al. 2021)
description: Tests the findings of Zhang, Gao, Cukur and Gallant (2021) on CRCNS data set vim-4, which
  holds deconvolved whole-cortex fMRI of five of the six subjects of a visual attention task and the
  BOLD data and behavioural state labels of the two subjects of a video game task. It recovers the
  supervised state space of each task, its cluster separation index, cross-validated classification
  and the projections between video game states. The functional ROIs behind the cortical maps are not
  in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_zhang_2021.ipynb
  title: Reproducing Zhang et al. (2021) from CRCNS vim-4
  runtime_minutes: 25
helpers:
- statespace.py
related:
- id: crcns:vim-4/unversioned
  relation: uses_data
- id: doi:10.3389/fnins.2020.565976
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
aiohttp
fsspec
h5py
matplotlib
numpy
pandas
requests
scikit-learn
scipy
EOF
date -u; cd /tmp/claude && . $TMPDIR/dev/bin/activate && time jupyter nbconvert --to notebook --execute full_nb.ipynb --output full_out.ipynb --ExecutePreprocessor.timeout=4000 2>&1 | grep -v WARN | tail -3; date -u
```

```
Sat Nov 14 10:25:05 UTC 2026
[NbConvertApp] Converting notebook full_nb.ipynb to notebook
[NbConvertApp] Writing 243019 bytes to full_out.ipynb

real	19m53.692s
user	62m57.069s
sys	0m11.766s
Sat Nov 14 10:44:59 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 -c "
import json;nb=json.load(open('full_out.ipynb'))
cs=[c for c in nb['cells'] if c['cell_type']=='code']
for c in cs[4:]:
  t=''.join(''.join(o.get('text','')) for o in c['outputs'] if 'text' in o)
  print(t[:7000]); print('=====')
" > full_out.txt; wc -c full_out.txt
```

```
36612 full_out.txt
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude/full_out.txt"
}
```

```
1	S1: 51608 voxels (14 constant, 0 NaN), voxel means -0.284 to 0.291, SDs 0.405 to 1.213; 24 PCs explain 84.1%; |weights| in PC space human 117, vehicle 106, attention 1.06e-14; |r| rewrite vs code per axis [1.     1.     0.4045]; mean r of same-frame TRs {'passive-human': 0.11415670411988853, 'passive-vehicle': 0.11058380055559039, 'human-vehicle': 0.23843833730092892}; 23 s, peak memory 3.1 GB
2	S2: 48819 voxels (0 constant, 0 NaN), voxel means -0.301 to 0.306, SDs 0.894 to 1.203; 24 PCs explain 89.7%; |weights| in PC space human 121, vehicle 123, attention 1.43e-14; |r| rewrite vs code per axis [1.     1.     0.1604]; mean r of same-frame TRs {'passive-human': 0.09946298979776792, 'passive-vehicle': 0.07050453268014109, 'human-vehicle': 0.2569188841368312}; 21 s, peak memory 3.1 GB
3	S3: 47512 voxels (0 constant, 0 NaN), voxel means -0.086 to 0.095, SDs 0.816 to 1.119; 24 PCs explain 68.4%; |weights| in PC space human 93.7, vehicle 102, attention 1.25e-14; |r| rewrite vs code per axis [1.    1.    0.328]; mean r of same-frame TRs {'passive-human': 0.0072509360900333145, 'passive-vehicle': 0.005253922148821592, 'human-vehicle': 0.2921646597226122}; 22 s, peak memory 3.1 GB
4	S5: 52044 voxels (4 constant, 0 NaN), voxel means -0.280 to 0.291, SDs 0.425 to 1.198; 24 PCs explain 89.1%; |weights| in PC space human 114, vehicle 111, attention 1.18e-14; |r| rewrite vs code per axis [1.     1.     0.3808]; mean r of same-frame TRs {'passive-human': 0.050547393407544314, 'passive-vehicle': 0.07425463953364086, 'human-vehicle': 0.19561385310929433}; 26 s, peak memory 3.4 GB
5	S6: 52349 voxels (0 constant, 0 NaN), voxel means -0.294 to 0.304, SDs 0.475 to 1.203; 24 PCs explain 85.3%; |weights| in PC space human 117, vehicle 114, attention 1.46e-14; |r| rewrite vs code per axis [1.     1.     0.0829]; mean r of same-frame TRs {'passive-human': 0.1106510302784783, 'passive-vehicle': 0.08418480006985153, 'human-vehicle': 0.18299585135107932}; 21 s, peak memory 3.4 GB
6	voxels p
[... 371 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 - <<'EOF'
p='gen_nb.py'; s=open(p).read()
s=s.replace('''        rows.append(dict(subject=s, condition=c, expected=e, measured=round(r[reading], 3), within=inside,
                         null_max_a=round(r[f"{null}_max_a"], 3), null_max_b=round(r[f"{null}_max_b"], 3)))''','''        key, ci = reading.split("_")[0], ss.CONDITIONS.index(c)
        nk = "2d" if reading == "R1_2d" else "3d"
        rows.append(dict(subject=s, condition=c, expected=e, measured=round(r[reading], 3), within=inside,
                         null_max_a=round(r[f"{null}_max_a"], 3), p_a=pval(csi_obs[s][key][ci], csi_null[s, "a", nk][:, ci]),
                         null_max_b=round(r[f"{null}_max_b"], 3), p_b=pval(csi_obs[s][key][ci], csi_null[s, "b", nk][:, ci])))''')
results = [
# fig1
r"""**Result: reproduced, resting on an assumption about the third axis.** With the paper's code (R3)
the S2 CSIs are 0.740 (attend-humans), 0.718 (attend-vehicles) and 0.676 (passive), all within
tolerance of 0.75, 0.69 and 0.67, and each exceeds every one of 1000 null values under both
permutation readings (null maxima 0.040 to 0.062 under (a), 0.322 to 0.352 under (b); p <= 0.001,
the bound 1000 permutations reach, not the paper's 1e-5). The median over random third axes (R2)
also matches (0.723, 0.718, 0.657). In the human-vehicle plane alone (R1) the attend-humans CSI is
0.664, outside tolerance. The third axis of the state space has no weight in these data, so the
values depend on it: over random third axes the attend-humans CSI ranges from 0.683 to 0.784 (5 to
95%).""",
# group
r"""**Result: reproduced, resting on an assumption about the third axis.** Over the five released
subjects, R3 gives mean CSIs of 0.665 +/- 0.103 (attend-humans), 0.729 +/- 0.022 (attend-vehicles)
and 0.525 +/- 0.260 (passive), all within the paper's spreads of 0.66 +/- 0.09, 0.74 +/- 0.03 and
0.53 +/- 0.24; R2 gives 0.658, 0.728 and 0.523. Under group reading (b), each mean exceeds the
maximum of the mean null CSIs (at most 0.110). Under reading (a), every subject is significant in
the attentive conditions but not in passive, where S3's CSI (0.061) does not exceed its null. In
the plane alone (R1) the attend-vehicles mean, 0.675, is outside tolerance. The second reference,
the means of the paper's own per-subject values over these subjects (0.644, 0.728, 0.512), is also
close to the R3 means.""",
# supp
r"""**Result: partially reproduced.** With R3, 10 of the 12 per-subject CSIs are within 10% of the
values in Supplementary Figures 1 and 2 (11 of 12 with R2, 10 of 12 with R1). The two outside are
S3 passive (0.061 against 0.05, a tolerance of 0.005) and S5 attend-humans (0.767 against 0.66,
within tolerance under R2 at 0.694). Eleven of the 12 exceed every null value (p <= 0.001), but
S3 passive does not: its CSI of 0.061 is at the level of its null (p printed above), where the
supplement reports every CSI significant at p < 0.01. The criterion needs both at least 10 values
within tolerance and every CSI significant, so the claim holds in part.""",
# passive
r"""**Result: not reproduced.** At the threshold that 1000 permutations allow (the difference
exceeding every null value), the passive CSI is significantly lower than the attentive CSIs in 2
or 3 of the 5 subjects under every combination of reading and null run with the code's positions
(R3), and in 1 with the plane (R1), where the criterion needs 4 of 5. At p < 0.05 the counts are
at most 3 with R3 and at most 4 with R1 (reading b, matched permutation, refitted). S3 and S5 show
the effect clearly. In S1 and S6 the attend-humans CSI is below the passive one (S1 0.518 against
0.622; S6 0.603 against 0.652), as in the paper's own figure values for these subjects, and the
mean of the two attentive CSIs is within 0.005 of passive. S2's differences (0.065 and 0.043) reach
p = 0.002 to 0.075.""",
# classification
r"""**Result: reproduced.** The mean accuracy over the five subjects is 44.4% (contiguous folds,
Euclidean), 53.4% (contiguous, density), 46.6% (random, Euclidean) and 56.3% (random, density),
against 48.4 +/- 7.6%; three of the four readings are within tolerance, and all four exceed every
one of 1000 mean null accuracies (maxima 9.7 to 12.5%). Chance under this procedure, the mean of
the null, is 7.8 to 9.1%, close to the paper's 8.3%. Per subject the accuracy is 40.8 to 60.6%.""",
# game csi
r"""**Result: reproduced under one reading of the clusters.** With one cluster per state from TRs
that have exactly one state (reading b), the CSI is 0.702 in S1 and 0.581 in S7, within tolerance
of 0.72 and 0.62, and both exceed every null value (null maxima 0.270 and 0.258). With every TR in
the cluster of each of its states (reading a), S1 is within (0.694) and S7 just outside (0.549,
tolerance down to 0.558). With the three groups of Figure 3A (reading c), both are lower (0.513 and
0.388). All six values exceed their nulls.""",
# mutual
r"""**Result: reproduced, resting on an assumption about the order of the variables.** With the
variables in the order of the data set's columns, engage-close TRs lie at -1.187 (S1) and -0.191
(S7) on the safe-explore dimension, and safe-explore TRs at -0.399 (S1) and -0.548 (S7) on the
engage-close dimension, all with p = 5e-5, the bound of 20,000 permutations, under both sign
readings. With the order of Table 1, S1 holds (-0.697 and -0.068, p = 5e-5) but in S7 safe explore
lies at -0.018 on the engage-close dimension (p = 0.937), so the claim would hold in one subject
only. The sign readings give the same values.""",
# fig3b
r"""**Result: reproduced.** Under every sign, order and Bonferroni reading, both subjects have
significant off-diagonal projections (S1 45 or 48 pairs, S7 20 or 32), some pairs are significant
in one direction only (10 to 20), and the two subjects' sets of significant pairs differ (12 to 26
shared). The figure's own matrix was not available to compare pair by pair.""",
# game class
r"""**Result: partially reproduced.** Every reading is far above its null (p <= 0.001; chance under
this procedure 10.8 to 16.4%, against the paper's 11%). S7's balanced accuracy is within the
paper's 30.4 +/- 4.2% with contiguous folds (26.4 to 33.4%) and above it with random folds (36.8 to
46.5%). S1's is above the paper's 32.8 +/- 3.8% under every reading (42.8 to 54.6%), so no reading
puts both subjects within tolerance. The S1 game data hold 65 min, where the paper reports 90 min
for one subject, so the data may not be those the paper analysed.""",
]
for r in results:
    s=s.replace('md("**Result: ...**")', 'md(r"""'+r+'""")', 1)
assert 'Result: ...' not in s
summary = r"""## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| claim | outcome |
|---|---|
| fig1-csi-s2 | reproduced (assumption: third axis as the code gives it) |
| att-csi-group | reproduced (same assumption) |
| supp-csi-per-subject | partially reproduced (10 of 12 values; S3 passive not significant) |
| att-passive-lower | not reproduced (2 or 3 of 5 subjects at the bound reached) |
| att-classification | reproduced |
| att-weights-cortex | blocked, data_missing (the paper's ROIs are not public) |
| game-csi | reproduced (one reading of the clusters) |
| game-mutual-negative-projection | reproduced (assumption: data set's column order) |
| fig3b-state-relations | reproduced |
| game-classification | partially reproduced (S1 above the paper's value) |
| game-weights-two-groups | blocked, data_missing (ROIs; no mapper for S1's game voxels) |

How the analysis differs from the paper's:

- Four of the six attention subjects of the paper's group values are tested as five: S4 is not
  released.
- The state space is the paper's code, computed exactly in the space of the 24 PCs; the code
  itself is run on the full voxels for the reported attention CSIs (R3).
- The attention variable has no weight in the deposited data, so the third axis of the attention
  state space is set by rounding; three readings are shown and the outcomes rest on the code's.
- Permutations: 1000 (20,000 for the game projections), so p-values reach 1e-3 (5e-5), not the
  paper's 1e-5. How labels are permuted, how folds are formed, the cluster distance, and how
  multi-state TRs enter are the claims file's readings, each run.
- S7's game state space has 8 dimensions (no flash TRs).

What was found about the data set:

- The attentive conditions of the deconvolved data are z-scored per voxel within each condition,
  so the attention variable (coded -1, 0, +1 in `states.hdf`, a coding the description does not
  give) carries no mean difference between them.
- S1's video game data hold 1950 TRs (65 min), where the paper and the description say one
  subject played 90 min; S7's hold 44 min, as stated.
- S1's video game data have 73,594 voxels, a voxel set no mapper in the data set matches.
- No functional ROI, localizer or retinotopy data are deposited.
- S7's video game BOLD is not z-scored per voxel over the session (voxel SDs 0.094 to 1.009),
  unlike S1's.
- The state columns of the video game files are not in the order of Table 1.
"""
s=s.replace('md("## Summary\\n\\n...")', 'md(r"""'+summary+'""")')
assert '## Summary\\n\\n...' not in s
open(p,'w').write(s)
EOF
grep -c "Result:" gen_nb.py; cd $TMPDIR && . dev/bin/activate && python /tmp/claude/gen_nb.py
```

```
9
46 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 - <<'EOF'
p='gen_nb.py'; s=open(p).read()
s=s.replace("""- Four of the six attention subjects of the paper's group values are tested as five: S4 is not
  released.""","""- The attention claims over subjects use five of the paper's six subjects: S4 is not released.""")
s=s.replace("mean of the two attentive CSIs is within 0.005 of passive","mean of the two attentive CSIs is within 0.006 of passive")
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python /tmp/claude/gen_nb.py && cat > entries/zhang-2021/README.md <<'EOF'
# Zhang et al. (2021) on CRCNS vim-4

Tests the findings of Zhang, Gao, Cukur and Gallant (2021), "Voxel-Based State Space Modeling
Recovers Task-Related Cognitive States in Naturalistic fMRI Experiments", Frontiers in Neuroscience
14:565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF), streamed from the public CRCNS bucket.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

- `reproduce_zhang_2021.ipynb`: the data check and one section per claim.
- `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
  principal components), the cluster separation index and the classifiers.

The notebook streams about 7 GB and runs in about 20 minutes with 4 GB of memory.
EOF
cd  && date -u && python tools/entry.py lock entries/zhang-2021 2>&1 | tail -5
```

```
46 cells
Sat Nov 14 10:46:37 UTC 2026
Traceback (most recent call last):
  File "tools/entry.py", line 59, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
uv run --help >/dev/null 2>&1; ls .venv 2>/dev/null | head -2; cat pyproject.toml | head -30
```

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "encore-science"
dynamic = ["version"]
description = "Check a dataset against the paper it came from: an AI agent reads the paper's claims and tests them on the data."
readme = "docs/encore.md"
license = "Apache-2.0"
requires-python = ">=3.10"
dependencies = [
  "pyyaml",
  "jsonschema",
  "nbformat",
  "uv",
  "pymupdf",
]

[project.urls]
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q pyyaml jsonschema nbformat && cd  && python tools/entry.py lock entries/zhang-2021 2>&1 | tail -5 && python tools/entry.py check entries/zhang-2021 2>&1 | tail -20
```

```
wrote zhang-2021/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/zhang-2021 2>&1 | tail -15; date -u
```

```
Sat Nov 14 10:46:49 UTC 2026
Installed kernelspec registry-zhang-2021 in executed/zhang-2021/.venv/share/jupyter/kernels/registry-zhang-2021
0 error(s)
pass  reproduce_zhang_2021.ipynb  (1194 s)
Sat Nov 14 11:06:49 UTC 2026
```

**Agent**

Now compare the executed copy's numbers with the dev run.

**Agent calls Bash**

```bash
ls executed/zhang-2021/; python3 -c "
import json
def outs(p):
    nb=json.load(open(p)); r=[]
    for c in nb['cells']:
        if c['cell_type']=='code':
            r.append(''.join(''.join(o.get('text','')) for o in c['outputs'] if 'text' in o))
    return r
a=outs('executed/zhang-2021/reproduce_zhang_2021.ipynb'); b=outs('/tmp/claude/full_out.ipynb')
import difflib,re
strip=lambda t: re.sub(r'(done in|elapsed|peak memory|; )\s*[\d.]+ (s|GB)','',t)
for i,(x,y) in enumerate(zip(a,b)):
    if i<4: continue
    d=[l for l in difflib.unified_diff(strip(y).splitlines(),strip(x).splitlines(),lineterm='',n=0) if not l.startswith(('---','+++','@@'))]
    if d: print('cell',i); print('\n'.join(d[:40]))
"
```

```
reproduce_zhang_2021.ipynb
result.json
cell 13
-subject condition  expected  measured  within  null_max_a  null_max_b
-     S1     human      0.51     0.518    True       0.045       0.336
-     S1   vehicle      0.79     0.737    True       0.053       0.088
-     S1   passive      0.64     0.622    True       0.055       0.334
-     S3     human      0.70     0.697    True       0.048       0.339
-     S3   vehicle      0.71     0.759    True       0.043       0.303
-     S3   passive      0.05     0.061   False       0.065       0.099
-     S5     human      0.66     0.767   False       0.042       0.126
-     S5   vehicle      0.74     0.730    True       0.096       0.340
-     S5   passive      0.59     0.614    True       0.094       0.347
-     S6     human      0.60     0.603    True       0.048       0.292
-     S6   vehicle      0.71     0.700    True       0.046       0.321
-     S6   passive      0.61     0.652    True       0.066       0.297
+subject condition  expected  measured  within  null_max_a      p_a  null_max_b      p_b
+     S1     human      0.51     0.518    True       0.045 0.000999       0.336 0.000999
+     S1   vehicle      0.79     0.737    True       0.053 0.000999       0.088 0.000999
+     S1   passive      0.64     0.622    True       0.055 0.000999       0.334 0.000999
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 - <<'EOF'
p='gen_nb.py'; s=open(p).read()
old='''        for rd in "ab":
            n_sig[rd] += r[reading] > r[f"{null}_max_{rd}"]
'''
assert old in s
s=s.replace(old,'')
s=s.replace('''                         null_max_b=round(r[f"{null}_max_b"], 3), p_b=pval(csi_obs[s][key][ci], csi_null[s, "b", nk][:, ci])))''','''                         null_max_b=round(r[f"{null}_max_b"], 3), p_b=pval(csi_obs[s][key][ci], csi_null[s, "b", nk][:, ci])))
        for rd in "ab":
            n_sig[rd] += rows[-1][f"p_{rd}"] < 0.01''')
s=s.replace('''    print(f"  {n_in} of 12 within tolerance; above every null value (p <= {1/(N_PERM+1):.4f} < 0.01): "
          f"reading a {n_sig['a']} of 12, reading b {n_sig['b']} of 12\\n")''','''    print(f"  {n_in} of 12 within tolerance; significant at p < 0.01 ({N_PERM} permutations): "
          f"reading a {n_sig['a']} of 12, reading b {n_sig['b']} of 12\\n")''')
assert "significant at p < 0.01 ({N_PERM}" in s
i=s.index('r"""**Result: partially reproduced.** With R3, 10 of the 12')
j=s.index('""",',i)
s=s[:i]+'''r"""**Result: reproduced, resting on an assumption about the third axis.** With R3, 10 of the 12
per-subject CSIs are within 10% of the values in Supplementary Figures 1 and 2 (11 of 12 with R2,
10 of 12 with R1). The two outside are S3 passive (0.061 against 0.05, a tolerance of 0.005) and
S5 attend-humans (0.767 against 0.66, within tolerance under R2 at 0.694). Under permutation
reading (a) all 12 R3 CSIs are significant at p < 0.01: eleven exceed every null value
(p = 0.001) and S3 passive has p = 0.002. Under reading (b) S3 passive has p = 0.042, so 11 of 12
are significant. The R1 counts are printed above. S3's passive CSI is close to the floor of the
measure, as in the paper (0.05).'''+s[j:]
s=s.replace("| supp-csi-per-subject | partially reproduced (10 of 12 values; S3 passive not significant) |","| supp-csi-per-subject | reproduced (10 of 12 values; all significant under reading a) |")
open(p,'w').write(s)
EOF
grep -n "supp-csi-per-subject |" /tmp/claude/gen_nb.py; cd $TMPDIR && . dev/bin/activate && python /tmp/claude/gen_nb.py; date -u
```

```
56:| supp-csi-per-subject | tested (S4 left out, as the claim says) |
825:| supp-csi-per-subject | reproduced (10 of 12 values; all significant under reading a) |
Traceback (most recent call last):
  File "/tmp/claude/gen_nb.py", line 481, in <module>
    md(r"""**Result: reproduced, resting on an assumption about the third axis.** With R3, 10 of the 12
    ~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    per-subject CSIs are within 10% of the values in Supplementary Figures 1 and 2 (11 of 12 with R2,
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<4 lines>...
    are significant. The R1 counts are printed above. S3's passive CSI is close to the floor of the
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    measure, as in the paper (0.05).""", ["claim:att-passive-lower"])
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: md() takes 1 positional argument but 2 were given
Sat Nov 14 11:07:11 UTC 2026
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude/gen_nb.py",
 "offset": 470,
 "limit": 30
}
```

```
470	        for rd in "ab":
471	            n_sig[rd] += rows[-1][f"p_{rd}"] < 0.01
472	    print(reading)
473	    print(pd.DataFrame(rows).to_string(index=False))
474	    print(f"  {n_in} of 12 within tolerance; significant at p < 0.01 ({N_PERM} permutations): "
475	          f"reading a {n_sig['a']} of 12, reading b {n_sig['b']} of 12\n")
476	i = ss.CONDITIONS.index("passive")
477	print("S3 passive: R3 mean over 10 seeds %.3f (seed SD %.3f); R2 5-95%% range %.3f to %.3f"
478	      % (csi_obs["S3"]["R3"][i], csi_seedsd["S3"]["R3"][i], csi_obs["S3"]["R2_lo"][i], csi_obs["S3"]["R2_hi"][i]))
479	""", ["claim:supp-csi-per-subject"])
480	
481	md(r"""**Result: reproduced, resting on an assumption about the third axis.** With R3, 10 of the 12
482	per-subject CSIs are within 10% of the values in Supplementary Figures 1 and 2 (11 of 12 with R2,
483	10 of 12 with R1). The two outside are S3 passive (0.061 against 0.05, a tolerance of 0.005) and
484	S5 attend-humans (0.767 against 0.66, within tolerance under R2 at 0.694). Under permutation
485	reading (a) all 12 R3 CSIs are significant at p < 0.01: eleven exceed every null value
486	(p = 0.001) and S3 passive has p = 0.002. Under reading (b) S3 passive has p = 0.042, so 11 of 12
487	are significant. The R1 counts are printed above. S3's passive CSI is close to the floor of the
488	measure, as in the paper (0.05).""", ["claim:att-passive-lower"])
489	
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python3 - <<'PYEOF'
p='gen_nb.py'; s=open(p).read()
bad='measure, as in the paper (0.05).""", ["claim:att-passive-lower"])\n'
assert bad in s
restore = 'measure, as in the paper (0.05).""")\n\n' + r'''md(r"""
### att-passive-lower

> Attention increases state separation; the CSI under passive viewing is significantly lower than
> under the attentive conditions in five of the six subjects.

Readings of the claims file: (a) passive against each attentive condition, both differences
significant; (b) passive against the mean of the two attentive CSIs. Null: the condition labels
permuted between TRs, presence labels kept, either (i) refitting the state space each time, or
(ii) keeping the fitted positions. How the condition labels are permuted is not fixed; two schemes
are run: "matched", where at each movie time point the three TRs showing the same frame get the
three conditions in random order (each condition keeps the same presence labels), and "global", a
shuffle over all TRs. One-sided, passive lower; 1000 permutations, so a subject counts at the
paper's threshold when its difference exceeds every null value (p <= 0.001, the bound reached).
The observed CSIs are those of R3 (the code's positions); for (i) the refitted null uses the
code's QR, which now gives the third axis a real weight. R1 (the plane) is shown as a variant.
""")

code(r"""
rng = np.random.default_rng(2)
def stats_ab(c):  # c: CSI (passive, human, vehicle)
    return np.array([c[1] - c[0], c[2] - c[0], c[1:].mean() - c[0]])
pl_rows = []
for s in ss.ATT_SUBJECTS:
    Z = att[s]["Z"]
    for variant, obs_pos in [("R3", att[s]["code_pos"]), ("R1", ss.att_positions(Z, X_att, "2d"))]:
        obs_c = np.mean([ss.att_csis(obs_pos, pcode, np.random.default_rng(k)) for k in range(10)], axis=0)
        obs = stats_ab(obs_c)
        for scheme in ["matched", "global"]:
            for refit in ["i", "ii"]:
                null = []
                for _ in range(N_PERM):
                    mem = ss.shuffle_conditions(900, scheme, rng)
                    if refit == "i":
                        Xp = ss.members_to_X(X_att, mem)
                        p = ss.att_positions(Z, Xp, "qr" if variant == "R3" else "2d")
                    else:
                        p = obs_pos
                    null.append(stats_ab(ss.att_csis(p, pcode, rng, members=mem)))
                null = np.array(null)
                p_one = (1 + (null >= obs).sum(0)) / (N_PERM + 1)
                pl_rows.append(dict(subject=s, variant=variant, scheme=scheme, null=refit,
                                    passive=obs_c[0], human=obs_c[1], vehicle=obs_c[2],
                                    d_human=obs[0], d_vehicle=obs[1], d_mean=obs[2],
                                    p_human=p_one[0], p_vehicle=p_one[1], p_mean=p_one[2]))
pl = pd.DataFrame(pl_rows)
pmin = 1 / (N_PERM + 1)
pl["a_at_bound"] = (pl.p_human <= pmin) & (pl.p_vehicle <= pmin)
pl["b_at_bound"] = pl.p_mean <= pmin
pl["a_p05"] = (pl.p_human < 0.05) & (pl.p_vehicle < 0.05)
pl["b_p05"] = pl.p_mean < 0.05
print(pl.round(4).to_string(index=False))
cnt = pl.groupby(["variant", "scheme", "null"])[["a_at_bound", "b_at_bound", "a_p05", "b_p05"]].sum()
print("\nsubjects of 5 with passive significantly lower:")
print(cnt.to_string())
print(f"elapsed {time.time()-T0:.0f} s")
""", ["claim:att-passive-lower"])
'''
s=s.replace(bad,restore)
open(p,'w').write(s)
PYEOF
cd $TMPDIR && . dev/bin/activate && python /tmp/claude/gen_nb.py && python3 -c "
import json
a=json.load(open('entries/zhang-2021/reproduce_zhang_2021.ipynb'))
b=json.load(open('/tmp/claude/full_nb.ipynb'))
import difflib
for x,y in zip(b['cells'],a['cells']):
    if x['source']!=y['source']:
        print('\n'.join(list(difflib.unified_diff(x['source'].splitlines(),y['source'].splitlines(),lineterm='',n=0))[:60])); print('----')
print(len(a['cells']),len(b['cells']))
"
```

```
Exit code 1
46 cells
Traceback (most recent call last):
  File "<string>", line 8, in <module>
    print('\n'.join(list(difflib.unified_diff(x['source'].splitlines(),y['source'].splitlines(),lineterm='',n=0))[:60])); print('----')
                                              ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'splitlines'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python3 -c "
import nbformat, difflib
a=nbformat.read('entries/zhang-2021/reproduce_zhang_2021.ipynb',4)
b=nbformat.read('/tmp/claude/full_nb.ipynb',4)
for x,y in zip(b.cells,a.cells):
    if x.source!=y.source:
        print('\n'.join(list(difflib.unified_diff(x.source.splitlines(),y.source.splitlines(),lineterm='',n=0))[:40])); print('----')
print(len(a.cells),len(b.cells))
"
```

```
--- 
+++ 
@@ -1 +1,9 @@
-**Result: ...**
+**Result: reproduced, resting on an assumption about the third axis.** With the paper's code (R3)
+the S2 CSIs are 0.740 (attend-humans), 0.718 (attend-vehicles) and 0.676 (passive), all within
+tolerance of 0.75, 0.69 and 0.67, and each exceeds every one of 1000 null values under both
+permutation readings (null maxima 0.040 to 0.062 under (a), 0.322 to 0.352 under (b); p <= 0.001,
+the bound 1000 permutations reach, not the paper's 1e-5). The median over random third axes (R2)
+also matches (0.723, 0.718, 0.657). In the human-vehicle plane alone (R1) the attend-humans CSI is
+0.664, outside tolerance. The third axis of the state space has no weight in these data, so the
+values depend on it: over random third axes the attend-humans CSI ranges from 0.683 to 0.784 (5 to
+95%).
----
--- 
+++ 
@@ -1 +1,9 @@
-**Result: ...**
+**Result: reproduced, resting on an assumption about the third axis.** Over the five released
+subjects, R3 gives mean CSIs of 0.665 +/- 0.103 (attend-humans), 0.729 +/- 0.022 (attend-vehicles)
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/zhang-2021 2>&1 | tail -4; date -u
```

```
Sat Nov 14 11:07:36 UTC 2026
Installed kernelspec registry-zhang-2021 in executed/zhang-2021/.venv/share/jupyter/kernels/registry-zhang-2021
0 error(s)
pass  reproduce_zhang_2021.ipynb  (1195 s)
Sat Nov 14 11:27:37 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
cs=[c for c in nb['cells'] if c['cell_type']=='code']
for i in [12,13]:
  print(''.join(''.join(o.get('text','')) for o in cs[i]['outputs'] if 'text' in o)[:4000])
"
```

```
second reference, means of the paper's per-subject values over the same five subjects: {'human': np.float64(0.644), 'vehicle': np.float64(0.728), 'passive': np.float64(0.512)}
R3_code   human    mean 0.665 +/- 0.103 (SD over 5) (expected 0.66 +/- 0.09; within: True); every subject above every null value: {'a': True, 'b': True}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.029, b 0.110)
R3_code   vehicle  mean 0.729 +/- 0.022 (SD over 5) (expected 0.74 +/- 0.03; within: True); every subject above every null value: {'a': True, 'b': True}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.032, b 0.098)
R3_code   passive  mean 0.525 +/- 0.260 (SD over 5) (expected 0.53 +/- 0.24; within: True); every subject above every null value: {'a': False, 'b': False}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.042, b 0.104)
R2_median human    mean 0.658 +/- 0.074 (SD over 5) (expected 0.66 +/- 0.09; within: True); every subject above every null value: {'a': True, 'b': True}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.029, b 0.110)
R2_median vehicle  mean 0.728 +/- 0.023 (SD over 5) (expected 0.74 +/- 0.03; within: True); every subject above every null value: {'a': True, 'b': True}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.032, b 0.098)
R2_median passive  mean 0.523 +/- 0.260 (SD over 5) (expected 0.53 +/- 0.24; within: True); every subject above every null value: {'a': False, 'b': False}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.042, b 0.104)
R1_2d     human    mean 0.602 +/- 0.074 (SD over 5) (expected 0.66 +/- 0.09; within: True); every subject above every null value: {'a': True, 'b': True}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.020, b 0.096)
R1_2d     vehicle  mean 0.675 +/- 0.033 (SD over 5) (expected 0.74 +/- 0.03; within: False); every subject above
[... 51 more lines not kept]
```

**Agent**

Executed copy matches the conclusions. Writing the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/zhang-2021-01.yaml",
 "content": "schema_version: 3\nid: zhang-2021-01\ndatasets:\n- archive: crcns\n  id: vim-4\n  version: unversioned\n  doi: 10.6080/K0668BDF\n  relation: primary\npaper: doi:10.3389/fnins.2020.565976\ndate: 2026-11-14\nentry: zhang-2021\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43583052040\noutcomes:\n- claim: fig1-csi-s2\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:fig1-csi-s2\n  measured:\n  - 0.740\n  - 0.718\n  - 0.676\n  notes: With the paper's code run on the full voxel data (R3), S2's CSIs are 0.740 (attend-humans),\n    0.718 (attend-vehicles) and 0.676 (passive), each within tolerance and above every one of 1000\n    null values under both permutation readings (p <= 0.001, the bound reached; the paper reports\n    p < 1e-5). The median over random third axes (R2) gives 0.723, 0.718 and 0.657, also within\n    tolerance. In the human-vehicle plane alone (R1) attend-humans is 0.664, outside tolerance.\n    Over random third axes the attend-humans CSI ranges from 0.683 to 0.784 (5 to 95%).\n  deviations:\n  - Assumed that the third axis of the attention state space is the one the paper's code gives. In\n    the deposited deconvolved data the attentive conditions are z-scored per voxel within each\n    condition, so the attention variable (-1, 0, +1) has an OLS weight of 1e-14, and the third QR\n    direction is set by rounding. The code is the paper's method and the paper's values were\n    presumably computed the same way; three readings are shown (code, random third axes, plane),\n    and the outcome holds under the first two.\n  - Permutations 1000 per reading of the claims file, so p reaches 0.001 and not 1e-5.\n  - The state space is computed exactly in the space of the 24 PCs (helper docstring); the code\n    itself is run for the observed values, and the human and vehicle axes of both agree to\n    |r| = 1.0000.\n- claim: att-csi-group\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:att-csi-group\n  measured:\n  - 0.665\n  - 0.729\n  - 0.525\n  notes: Over the five released subjects (R3) the mean CSIs are 0.665 +/- 0.103, 0.729 +/- 0.022 and\n    0.525 +/- 0.260 for attend-humans, attend-vehicles and passive, within the paper's spreads.\n    Under group reading (b) each mean exceeds the maximum of 1000 mean null CSIs (at most 0.110).\n    Under reading (a) every subject is significant at the bound in the attentive conditions but\n    S3's passive CSI (0.061) does not exceed every null value. R2 gives 0.658, 0.728 and 0.523; R1\n    gives 0.602, 0.675 (outside tolerance) and 0.492. The means of the paper's own per-subject\n    values over these subjects are 0.644, 0.728 and 0.512.\n  deviations:\n  - Five of the paper's six subjects; S4 is not released.\n  - Same assumption about the third axis as fig1-csi-s2.\n- claim: supp-csi-per-subject\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:supp-csi-per-subject\n  measured:\n  - 0.518\n  - 0.737\n  - 0.622\n  - 0.697\n  - 0.759\n  - 0.061\n  - 0.767\n  - 0.730\n  - 0.614\n  - 0.603\n  - 0.700\n  - 0.652\n  notes: With R3, 10 of 12 values are within 10% of the supplement's; outside are S3 passive (0.061\n    against 0.05, tolerance 0.005) and S5 attend-humans (0.767 against 0.66). Under permutation\n    reading (a) all 12 are significant at p < 0.01 (S3 passive p = 0.002, the others 0.001); under\n    reading (b) S3 passive has p = 0.042. R2 puts 11 of 12 within tolerance with the same\n    significance; R1 puts 10 within but S3 passive is not significant under either reading (p =\n    0.078 and 0.355), so R1 would make the claim partially reproduced.\n  deviations:\n  - Same assumption about the third axis as fig1-csi-s2.\n- claim: att-passive-lower\n  outcome: not_reproduced\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:att-passive-lower\n  measured: 2\n  notes: At the threshold 1000 permutations allow (the difference above every null value, p <=\n    0.001), the passive CSI is significantly lower in 2 of 5 subjects under reading (a) with the\n    code's positions (S3, S5), and 2 or 3 under reading (b), for every null (refitted or not) and\n    both permutation schemes; the criterion needs 4 of 5. At p < 0.05 the counts are at most 3\n    (R3) and at most 4 (R1, reading b, matched, refitted). In S1 and S6 attend-humans is below\n    passive (0.518 against 0.622; 0.603 against 0.652), as in the paper's own figure values for\n    these subjects, and the mean attentive CSI is within 0.006 of passive. S2's differences are\n    0.065 and 0.043 (p 0.002 to 0.075). Measured is the count under reading (a), null (i), matched\n    permutation.\n  deviations:\n  - Five of six subjects; S4 is not released.\n  - How condition labels are permuted is not fixed by the paper; two schemes were run (matched by\n    movie frame, and global), and the outcome is the same under both.\n  - Permutations 1000, so the bound reached is 0.001 and not the paper's 1e-5.\n- claim: att-classification\n  outcome: reproduced\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:att-classification\n  measured: 44.4\n  notes: Mean accuracy over the five subjects is 44.4% (contiguous folds, Euclidean), 53.4%\n    (contiguous, density), 46.6% (random, Euclidean) and 56.3% (random, density), against 48.4 +/-\n    7.6%; three readings are within tolerance and all exceed every one of 1000 mean null\n    accuracies (maxima 9.7 to 12.5%). Chance under this procedure (null mean) is 7.8 to 9.1%,\n    close to the paper's 8.3%. Per subject 40.8 to 60.6%.\n  deviations:\n  - Five of six subjects; S4 is not released.\n  - Held-out positions are z-scored with the training statistics, a standard choice the claims\n    file names.\n- claim: att-weights-cortex\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The criterion compares mean weights in the subjects' functional ROIs (FFA, OFA, EBA, RSC,\n    PPA, OPA and others), which the paper drew from functional localizer and retinotopic mapping\n    data (Methods, Preprocessing and Visualization, paragraph 2). The data set's 39 files hold no\n    ROI, localizer or retinotopy data, and the paper's code repository (gallantlab/state-space at\n    6ffb3c3) holds none. A group atlas on fsaverage would substitute for the paper's per-subject\n    ROIs, which is not an input the paper relies on, so none was used. The mappers to fsaverage\n    are present for S1 to S7.\n- claim: game-csi\n  outcome: reproduced\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:game-csi\n  measured:\n  - 0.702\n  - 0.581\n  notes: With one cluster per state from TRs with exactly one state (reading b), the CSI is 0.702\n    (S1) and 0.581 (S7), within tolerance of 0.72 and 0.62 and above every one of 1000 null values\n    (maxima 0.270 and 0.258). With multi-membership clusters (reading a) S1 is 0.694 and S7 0.549,\n    just below tolerance (0.558); with the three groups of Figure 3A (reading c) 0.513 and 0.388.\n    All are above their nulls. Clusters with no more TRs than dimensions are left out (S1 flash\n    under a and b, S1 kill and S7 run away and kill under b).\n  deviations:\n  - S7 has no flash TRs, so its state space has 8 dimensions.\n  - The S1 video game data hold 65 min, where the paper reports 90 min for one subject.\n- claim: game-mutual-negative-projection\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:game-mutual-negative-projection\n  notes: With the variables in the data set's column order, engage-close TRs lie at -1.187 (S1) and\n    -0.191 (S7) on the safe-explore dimension and safe-explore TRs at -0.399 and -0.548 on the\n    engage-close dimension, each p = 5e-5 (the bound of 20,000 permutations), under both sign\n    readings. With Table 1's order S1 holds (-0.697, -0.068, p = 5e-5) but S7's safe-explore TRs\n    lie at -0.018 on the engage-close dimension (p = 0.937), which would make the claim hold in one\n    subject only.\n  deviations:\n  - Assumed the order of the variables in the QR is the order of the data set's state columns,\n    since the paper's code takes the state matrix as it is stored and has no video game analysis;\n    under Table 1's order the outcome would be partially reproduced.\n- claim: fig3b-state-relations\n  outcome: reproduced\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:fig3b-state-relations\n  notes: Under every sign, order and Bonferroni reading, S1 has 45 or 48 and S7 20 or 32 significant\n    off-diagonal projections (p < 0.01 corrected, 20,000 permutations, smallest p 5e-5), 10 to 20\n    pairs are significant in one direction only, and the subjects share 12 to 26 of their\n    significant pairs. The paper's matrix could not be compared pair by pair.\n- claim: game-classification\n  outcome: partially_reproduced\n  notebook: reproduce_zhang_2021.ipynb\n  output: claim:game-classification\n  measured:\n  - 45.9\n  - 33.4\n  notes: Every reading is above its null (p = 0.001; chance under this procedure 10.8 to 16.4%,\n    against the paper's 11%). S7 is within 30.4 +/- 4.2% with contiguous folds (26.4 to 33.4%)\n    and above it with random folds (36.8 to 46.5%). S1 is above 32.8 +/- 3.8% under every reading\n    (42.8 to 54.6%), so no reading puts both within tolerance. The S1 data hold 65 min where the\n    paper reports 90 min for one subject, so they may not be the data the paper analysed. Measured\n    is the first reading (contiguous folds, Euclidean, single-state TRs).\n  deviations:\n  - Classes with fewer than 2 x (dimensions + 1) TRs are left out of the density rule (listed in\n    the notebook); kill has no single-state TRs in S1.\n- claim: game-weights-two-groups\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The criterion needs region definitions (TPJ, precuneus, prefrontal, motor, premotor and\n    supplementary motor cortex, IPS, FEF, SEF) from the paper's ROIs, which are not deposited\n    (see att-weights-cortex). In addition, S1's video game data have 73,594 voxels and no mapper in\n    the data set matches them (S1's mapper has 51,608, as its attention data), so S1's weights\n    cannot be placed on the cortex with the files given. S7's data match S7's mapper.\nfindings:\n- kind: other\n  about: data\n  statement: In the deconvolved attention files each attentive condition (human, vehicle) is z-scored\n    per voxel within the condition, while the passive TRs are not. With the attention state coded\n    -1, 0, +1 in states.hdf, its regression weight is the difference of the two attentive means,\n    which is zero (1e-14 in all five subjects), so the attention dimension of the paper's state\n    space cannot be recovered from the deposited files; the third axis is set by rounding and the\n    CSIs move by up to 0.1 with it.\n- kind: metadata_insufficient\n  statement: The data description does not say how the third column of states.hdf codes the\n    attention condition; the files use -1 for attend-humans, 0 for passive and +1 for\n    attend-vehicles.\n- kind: metadata_error\n  statement: The S1 video game data hold 1950 TRs (65 min at the 2.0045 s TR), where the data\n    description and the paper say one subject played for 90 minutes (six 15-min runs). S7's 1320\n    TRs (44 min) match the stated 45 minutes.\n- kind: data_missing\n  statement: No mapper matches the S1 video game data, which have 73,594 voxels; the S1 mapper has\n    51,608 voxels, the voxel set of S1's attention data. S1's game weights cannot be placed on\n    fsaverage or the flatmap with the files given.\n- kind: data_missing\n  statement: The functional ROIs, and the localizer and retinotopic mapping data the paper used to\n    define them, are not in the data set, so the cortical claims of Figures 2 and 4 cannot be\n    tested by region.\n- kind: other\n  about: data\n  statement: The S7 video game BOLD (float32) is not z-scored per voxel over the session (voxel SDs\n    0.094 to 1.009, means -0.059 to 0.025), unlike S1's, which is exactly z-scored; the paper says\n    responses were normalized to zero mean and unit variance.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. The attention variable has zero weight in the\n    deposited deconvolved data (attentive conditions z-scored per condition), so the third axis\n    of the attention state space, and with it the CSIs, depends on rounding. Was the paper's\n    analysis run on these files, and how was the attention dimension defined? This attempt adopted\n    the axis the published code gives and showed the plane and random third axes as readings.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. For the video game state space, in what order were\n    the nine variables entered into the QR decomposition? The safe-explore position of engage-close\n    TRs in S7 is negative and significant with the data set's column order and near zero with the\n    order of Table 1. This attempt adopted the column order.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. For the passive-against-attentive test (p < 1e-5 in\n    five of six subjects), what was compared (each attentive condition or their mean) and how\n    were labels permuted? In S1 and S6 the attend-humans CSI is below the passive one, in the\n    paper's figures and here.\n"
}
```

```
File created successfully at: attempts/zhang-2021-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python tools/entry.py check entries/zhang-2021 2>&1 | tail -5; python -c "
import yaml,jsonschema,json
d=yaml.safe_load(open('attempts/zhang-2021-01.yaml'))
jsonschema.validate(d,json.load(open('schemas/attempt.schema.json')));print('schema ok', len(d['outcomes']))
c=yaml.safe_load(open('claims/zhang-2021.yaml')); print(sorted(x['id'] for x in c['claims'])==sorted(o['claim'] for o in d['outcomes']))
"; grep -n "—\|rather" attempts/zhang-2021-01.yaml entries/zhang-2021/* | head; ls tools | head -40
```

```
0 error(s)
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    jsonschema.validate(d,json.load(open('schemas/attempt.schema.json')));print('schema ok', len(d['outcomes']))
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/jsonschema/validators.py", line 1332, in validate
    raise error
jsonschema.exceptions.ValidationError: datetime.date(2026, 11, 14) is not of type 'string'

Failed validating 'type' in schema['properties']['date']:
    {'type': 'string', 'format': 'date'}

On instance['date']:
    datetime.date(2026, 11, 14)
grep: entries/zhang-2021/__pycache__: Is a directory
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
rm -rf entries/zhang-2021/__pycache__; . $TMPDIR/dev/bin/activate && python -c "
import yaml,jsonschema,json
d=yaml.safe_load(open('attempts/zhang-2021-01.yaml')); d['date']=str(d['date'])
jsonschema.validate(d,json.load(open('schemas/attempt.schema.json')));print('schema ok', len(d['outcomes']))
c=yaml.safe_load(open('claims/zhang-2021.yaml')); print(sorted(x['id'] for x in c['claims'])==sorted(o['claim'] for o in d['outcomes']))
"; ls tests | head; grep -ln "attempts/" tests/*.py | head
```

```
schema ok 11
True
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
tests/test_agent_run.py
tests/test_encore.py
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python tools/entry.py handover entries/zhang-2021 2>&1 | tail -5; ls executed/zhang-2021/handover/; git status --short; date -u
```

```
wrote executed/zhang-2021/handover
reproduce_zhang_2021.ipynb
statespace.py
zhang-2021.yaml
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
?? attempts/zhang-2021-01.yaml
?? entries/zhang-2021/
?? scripts
Sat Nov 14 11:28:54 UTC 2026
```

**Agent**

All 11 claims have an outcome, the entry passes `check` and a clean `all` run (1195 s), and the handover package is built in `executed/zhang-2021/handover/`. Nothing is committed. Work ran from 09:59 to 11:29 UTC, well before the 14:14 cutoff.

**(1) Outcomes**

| claim | outcome | key numbers (paper) |
|---|---|---|
| fig1-csi-s2 | reproduced, assumed | 0.740 / 0.718 / 0.676 (0.75 / 0.69 / 0.67); p ≤ 0.001 |
| att-csi-group | reproduced, assumed | 0.665 / 0.729 / 0.525 over 5 subjects (0.66 / 0.74 / 0.53) |
| supp-csi-per-subject | reproduced, assumed | 10 of 12 within tolerance; all significant at p < 0.01 under permutation reading (a) |
| att-passive-lower | not reproduced | 2 or 3 of 5 subjects significant at the bound 1000 permutations allow; 4 needed |
| att-classification | reproduced | 44.4 to 56.3% across the four readings (48.4 ± 7.6); chance under this procedure 7.8 to 9.1% |
| att-weights-cortex | blocked, data_missing | the paper's per-subject ROIs and localizer data are not public |
| game-csi | reproduced | 0.702 / 0.581 with single-state clusters (0.72 / 0.62) |
| game-mutual-negative-projection | reproduced, assumed | all negative, p = 5e-5, with the dataset's column order; Table 1 order fails in S7 |
| fig3b-state-relations | reproduced | under every reading |
| game-classification | partially reproduced | S1 42.8 to 54.6% (32.8 ± 3.8); S7 within tolerance with contiguous folds |
| game-weights-two-groups | blocked, data_missing | no ROIs, and no mapper for S1's game voxels |

**(2) What was found about the dataset**
- The attend-human and attend-vehicle conditions are each z-scored per voxel in the deconvolved files. With the attention state coded -1/0/+1, its regression weight is zero (about 1e-14 in all five subjects). The third axis of the state space is therefore set by rounding, and the CSIs move by up to about 0.1 with it.
- The -1/0/+1 coding of that column is not documented.
- S1's game data hold 65 min, where the paper and the data description say 90 min. S1's game voxels (73,594) match no mapper. S7's game data are not z-scored per voxel, unlike S1's.
- The game state columns are not in Table 1 order.
- No duplicate recordings. Labels and BOLD line up: the attention CSI peaks at lag 0 and the game CSI at 1 TR.
- Version: unversioned, DOI 10.6080/K0668BDF. The MD5 sums of every file read are in the notebook header.

Assumptions:
- The attention third axis is the one the paper's code gives. The 2D plane and random third axes are shown as readings, and R1 (the plane) would change two of the CSI claims.
- The game variables enter the QR in the dataset's column order.
- Two ways of permuting condition labels for att-passive-lower were run (matched by movie frame, and global). Both give the same outcome.

Questions for the paper's authors are recorded as three `methods_unavailable` findings:
- How was the attention dimension defined, given the per-condition z-scoring?
- In what order did the nine game variables enter the QR?
- What exactly did the passive-versus-attentive test compare, and how were labels permuted?

I asked a reader nothing.

**(3) Where the protocol was unclear or missing something**
1. It has no case for a method that is well defined in the paper but undefined on the deposited data (the zero-weight attention axis). I treated it as an assumption with three readings.
2. The claims file says "the author decides whether an outside ROI source can be used". Protocol step 4 allows outside data only when the paper relies on it. I followed the protocol and blocked both cortex claims.
3. It does not say which value goes under `measured` when no reading matches. I used the first reading the criterion lists and said so in the notes.
4. The criteria need at least 1000 permutations (20,000 for the Bonferroni matrix), which puts the run at 20 minutes against the 10-minute aim. Nothing says how to trade these off.
5. Conclusions can only be written after seeing results, and any edit forces a full re-run, so every fix costs another 20 minutes. I developed on a 2-subject subset, ran the full notebook outside the entry, then ran `all` twice.
6. The schema wants `date` as a string, but an unquoted YAML date parses as a date. I kept the existing records' convention.
7. archives.md says CRCNS data sets are mostly zips. This one is plain HDF5 and npy, which streamed fine with fsspec.

**(4) Runtime and failures**
- The notebook takes about 20 minutes with a peak of 3.9 GB.
- I first counted supp-csi-per-subject significance against "exceeds every null value" when the criterion says p < 0.01. I caught it from the printed p-values, fixed it, and re-ran. The outcome changed from partially reproduced to reproduced.
- One generator edit deleted a notebook section by accident. I restored it and checked the diff before re-running.
- One shell command needing approval was denied (reading a saved output file with `sed`); I read the same file with the Read tool.
- The working tree also has untracked dotfiles and folders (`.bashrc`, `.idea`, `.vscode`, `scripts` and others) that I did not create or touch. The workflow may commit them.

## End of run

52 turns, 82 minutes, $5.84 at API prices, result: success.
