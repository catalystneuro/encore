# crcns-apl-1 · author · run 42478340998

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims/crcns-apl-1 entries | head -50
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7790d7ff-46c7-456a-840e-811d9320deb8/tool-results/bazu7wl2i.txt

Preview (first 2KB):
Sun Nov  8 12:05:50 UTC 2026
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7790d7ff-46c7-456a-840e-811d9320deb8/tool-results/bazu7wl2i.txt"
}
```

```
1	Sun Nov  8 12:05:50 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 683 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/crcns-apl-1/10.7554-elife.27342.yaml; ls -la paper; cat paper/apl-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7790d7ff-46c7-456a-840e-811d9320deb8/tool-results/bq2s29vua.txt"
}
```

```
1	# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
2	# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
5	#
6	# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
7	# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
8	# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
9	# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
10	# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
11	# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
12	# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
13	# holds; no claim comes from it.
14	#
15	# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
16	# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
17	# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence
18	# analysis (Analyse_by_Recurrence_Points.m, LocalLinearDynamics.m, recurrence_point_results_Viz.m),
19	# manifold comparisons (Are_sequential_attractors_the_same.m and _CommonAxes.m,
20	# Initial_Conditions.m), perturbations (Are_jumps_perturbations_or_transitions2.m), period change
[... 805 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md | head -120; ls entries/001453-fouke-2025 claims/001453; wc -l README.md docs/design.md
```

```
## CRCNS

- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
  `hc-3`), with a DOI of its own (`10.6080/...`). The registry's list is
  `targets/crcns.json`, written by hand; for now it holds one data set, to test
  the pipeline beyond DANDI.
- **Versions.** CRCNS data sets are not versioned. Record the version as
  `unversioned`, with the data set's DOI under `dataset: doi`, and give in the
  notebook header the MD5 sums from the data set's `checksums.md5` for the
  files read, so a later change is detectable.
- **Reading.** The files are in the public S3 bucket `crcnsarchive` (region
  us-west-2), under `<id>/`, readable without an account at
  `https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/<file>`; list a data
  set with `?list-type=2&prefix=<id>/` on the bucket's address. The site
  crcns.org asks for a login to download; the bucket does not. Most data sets
  are zip files of MATLAB or other files: open the zip in place with
  `fsspec.open(url, block_size=2**20).open()` and Python's `zipfile`, which
  read only the parts needed over range requests (`remfile` lacks what
  `zipfile` needs to read a member), and load members in memory
  (`scipy.io.loadmat`, or `h5py` for MATLAB 7.3 files). Do not download whole
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:8]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('----')
"; cat ../../attempts/001453-fouke-2025-01.yaml | head -150
```

```
schema_version: 1
name: 001453-fouke-2025
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
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 386 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/^findings/,$p' attempts/001453-fouke-2025-01.yaml | head -60; grep -n "blocked_by\|assumed\|measured" attempts/001453-fouke-2025-01.yaml | head; ls questions | head; ls schemas
```

```
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
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
[... 64 more lines not kept]
```

**Agent**

Now list the bucket.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=apl-1/" | python -c "
import sys,re
t=sys.stdin.read()
for k,s,d in re.findall(r'<Key>(.*?)</Key>.*?<LastModified>(.*?)</LastModified>.*?<Size>(.*?)</Size>',t): print(k,d,s)
print(re.findall('IsTruncated>(.*?)<',t))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; curl -s $B/plot_maps.m; curl -s $B/plot_rasters.m; python -c "import fsspec,scipy,numpy,h5py,sklearn,statsmodels;print('ok')"; which uv python; python --version
```

```
53a98c4b9f2a35be299180699321ad16  Coordinates.mat
a94b5040b265b276e2b0ef684277f2ad  diode_template.mat
f08d0f8ce220ad18b9629bfe1f31019e  docs/crcns_apl-1_data_description.docx
387115831fee4b7ca9941e087456c8e0  docs/crcns_apl-1_data_description.pdf
d01451b227a6c4a0dc2a620bd9bbbcf9  ExtracellularData.mat
be5b00182e7d601afa5255d5dbf0b397  filelist.txt
27437d5d4063cd9827f1f1ffa67f36d4  FileTable.mat
c78b779ea9f5da5eb90fc2531e16b29e  load_raw_data.m
873e61ff32d4cc550df4b0b6a446704d  plot_maps.m
5c25711387cbea1b9e36d51ae987ad0c  plot_rasters.m
b65c1713a97d8147749c53d5721606c6  rawdata.tar.gz
8657665316d5006677891922bdd0a1d8  SpikeData.mat
# CRCNS.org 'apl-1' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 Coordinates.mat	35121 (34.2 KB)
 diode_template.mat	2621 (2.5 KB)
 docs/crcns_apl-1_data_description.docx	32731 (31.9 KB)
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy h5py matplotlib pandas statsmodels jupyter nbconvert ipykernel 2>&1 | tail -2; python -c "import fsspec;print(fsspec.__version__)"
```

```
2026.9.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, scipy.io as sio, io, numpy as np
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/'
def L(n):
    with fsspec.open(B+n,'rb') as f: return sio.loadmat(io.BytesIO(f.read()),squeeze_me=True,struct_as_record=False)
ft=L('FileTable.mat'); print({k:v for k,v in ft.items() if not k.startswith('__')})
sd=L('SpikeData.mat'); print([k for k in sd if not k.startswith('__')])
S=sd['SpikeData']; print(type(S),S.shape)
for i,s in enumerate(S):
    sp=s.spks; ids=np.unique(sp[:,0])
    print(i,s._fieldnames, s.filename if hasattr(s,'filename') else '', getattr(s,'bout',None) , sp.shape, ids.min(),ids.max(),len(ids), sp[:,1].min().round(3), sp[:,1].max().round(2), (np.unique(sp[sp[:,1]>=30,0])).size)
"
```

```
{'FileTable': array([['Prep ID', 'Left or Right ganglion',
        '# of neurons after spike-sorting',
        'Trials with successful P10 recordings'],
       ['Jun0214da01.mat', 'Left', 136, 'xxx'],
       ['Jun0414Bda01.mat', 'Left', 105, array([1, 2, 3], dtype=uint8)],
       ['Jun0514da01.mat', 'Right', 160, 'xxx'],
       ['Jun0914da01.mat', 'Left', 151, array([1, 2, 3], dtype=uint8)],
       ['Jun1114da01.mat', 'Right', 94, array([1, 2, 3], dtype=uint8)],
       ['May2214da01.mat', 'Right', 121, 'xxx'],
       ['Nov0514da01.mat', 'unreliable coordinates', 75, 'xxx'],
       ['Oct1514da01.mat', 'unreliable coordinates', 102, 'xxx'],
       ['Sep2414da01.mat', 'Right', 104, 'xxx'],
       ['Sep2914da01.mat', 'Left', 83, 'xxx']], dtype=object)}
['SpikeData']
<class 'numpy.ndarray'> (30,)
0 ['spks', 'filename', 'Bout'] Jun0214da01.mat None (23681, 2) 1.0 136.0 136 0.021 122.72 136
1 ['spks', 'filename', 'Bout'] Jun0214da02.mat None (25768, 2) 1.0 136.0 136 0.001 122.72 136
2 ['spks', 'filename', 'Bout'] Jun0214da03.mat None (27178, 2) 1.0 136.0 136 0.018 122.72 136
3 ['spks', 'filename', 'Bout'] Jun0414Bda01.mat None (13961, 2) 1.0 105.0 105 0.102 122.72 105
4 ['spks', 'filename', 'Bout'] Jun0414Bda02.mat None (13846, 2) 1.0 105.0 105 0.01 122.71 105
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, scipy.io as sio, io, numpy as np
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/'
def L(n):
    with fsspec.open(B+n,'rb') as f: return sio.loadmat(io.BytesIO(f.read()),squeeze_me=True,struct_as_record=False)
e=L('ExtracellularData.mat'); print([k for k in e if not k.startswith('__')])
for s in e['ExtracellularData']:
    sp=s.spks; print(s._fieldnames, s.filename, s.Bout, sp.shape, np.unique(sp[:,0]), sp[:,1].min(), sp[:,1].max(), np.diff(sp[:,1]).min())
c=L('Coordinates.mat'); print([k for k in c if not k.startswith('__')])
for i,s in enumerate(c['Coordinates']):
    print(i, s._fieldnames, [ (f, np.shape(getattr(s,f))) for f in s._fieldnames])
    print('  x',np.nanmin(s.x),np.nanmax(s.x),' y',np.nanmin(s.y),np.nanmax(s.y))
d=L('diode_template.mat'); print({k:(np.shape(v)) for k,v in d.items() if not k.startswith('__')}); t=d['diode_template']; print(t.dtype, np.unique(t), t.sum())
"
```

```
['ExtracellularData']
['spks', 'filename', 'Bout'] Jun0414da01p10.mat 1 (5902, 2) [1.] 4.251089157513653 122.63054549917162 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun0414da02p10.mat 2 (16374, 2) [1.] 0.48291096520832055 122.64895379517702 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun0414da03p10.mat 3 (9538, 2) [1.] 0.0625882064183592 122.67349818985089 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun0914da01p10.mat 1 (14904, 2) [1.] 0.26507946247775666 122.24703933239246 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun0914da02p10.mat 2 (13337, 2) [1.] 1.192857581149905 122.6630668221145 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun0914da03p10.mat 3 (9637, 2) [1.] 0.44057188439590106 119.81407621034546 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun1114da01p10.mat 1 (4257, 2) [1.] 0.705037737006811 122.58882002822605 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun1114da02p10.mat 2 (6552, 2) [1.] 0.37368840890961524 122.70847395226114 0.0006136098668463319
['spks', 'filename', 'Bout'] Jun1114da03p10.mat 3 (8757, 2) [1.] 0.34116708596674233 122.62502301037 0.0006136098668463319
['Coordinates']
0 ['x', 'xstd', 'y', 'ystd', 'filename', 'ganglion'] [('x', (136,)), ('xstd', (136,)), ('y', (136,)), ('ystd', (136,)), ('filename', ()), ('ganglion', ())]
  x 6.570092036895972 45.67852780283527  y 1.0 49.0
1 ['x', 'xstd', 'y', 'ystd', 'filename', 'ganglion'] [('x', (105,)), ('xstd', (105,)), ('y', (105,)), ('ystd', (105,)), ('filename', ()), ('ganglion', ())]
  x 4.591099926017381 41.61541521328064  y 1.668095519857586 48.3790026798408
2 ['x', 'xstd', 'y', 'ystd', 'filename', 'ganglion'] [('x', (160,)), ('xstd', (160,)), ('y', (160,)), ('ystd', (160,)), ('filename', ()), ('ganglion', ())]
  x 5.428406659307961 46.08714750309025  y 1.0 49.0
3 ['x', 'xstd', 'y', 'ystd', 'filename', 'ganglion'] [('x', (151,)), ('xstd', (151,)), ('y', (151,)), ('ystd', (151,)), ('filename', ()), ('ganglion', ())]
  x 5.300470623486753 43.70615
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, scipy.io as sio, io, numpy as np
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/'
with fsspec.open(B+'Coordinates.mat','rb') as f: c=sio.loadmat(io.BytesIO(f.read()),squeeze_me=True,struct_as_record=False)
for s in c['Coordinates']: print(s.filename, s.ganglion, np.isnan(s.x).sum())
"; grep -n "^" paper/10.7554-elife.27342.txt | grep -n -i "materials and methods\|^[0-9]*:[A-Z][a-z ]*$" | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

The data set is small (4 MB of spikes). The file table gives 75 to 160 neurons per preparation, 1131 in total. Next I'll read the paper's Methods.

**Agent calls Bash**

```bash
sed -n '303,420p' paper/10.7554-elife.27342.txt | cut -c1-6000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "caudo\|rostr\|Figure 8\b\|lateral\|medial" paper/10.7554-elife.27342.txt | cut -c1-1500 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^Participation maps\|Figure 8\.\|Figure 7\.\|Figure 6—figure supplement 1\.\|Figure 7—figure supplement 2\.\|Figure 3\.\|Figure 2\.\|Figure 4\.\|Figure 6\." paper/10.7554-elife.27342.txt | cut -c1-200; grep -n -i "ventral\|dorsal\|orient" paper/10.7554-elife.27342.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk 'NR>=40 && NR<=300 && length($0)>0 {print NR": "substr($0,1,2500)}' paper/10.7554-elife.27342.txt | grep -v "DOI: http" | sed -n '1,200p' > $TMPDIR/res.txt; wc -c $TMPDIR/res.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/res.txt"
}
```

```
1	41: Here we demonstrate the essential properties of a periodic attractor network. ( A ) Top: a simple neuronal implementation of a periodic attractor network using three mutually inhibitory neurons. Bottom: model neurons are not endogenous oscillators - if uncoupled, they do not oscillate in response to constant input. The oscillatory activity we show here is an emergent property of the model network. ( B ) The underlying periodic attractor is revealed by the recurrence of the neurons’ joint activity. Top: given sustained input, the three neurons rapidly settle into an alternating oscillatory rhythm. Bottom: projection of the three neurons’ firing rates onto the first two principal components (PCs). Starting from time zero (black dot), the joint activity of the network rapidly converges to a recurrent trajectory, where each corner of the triangle - extending into the short diagonal line - corresponds to the maximum rate of one neuron. The space containing the repeated trajectory is the attractor’s manifold. ( C ) Convergence to the manifold from different initial conditions. From three different initial conditions for the neurons (coloured dots), each corresponding joint activity converges to the attractor manifold. ( D ) Transient perturbations cause a divergence and return to the attractor’s manifold. Top: A brief increase in input to one neuron (black bar) perturbs the ongoing oscillation, which is rapidly recovered. Bottom: in the PC projection, the initial recurrent trajectory (in black) is moved away from the manifold by the perturbation (red); removing the perturbing input rapidly moves the joint activity back to the manifold (blue). ( E ) Sustained perturbations move the network to a new attractor. Top: A sustained change in input (black bar) causes one neuron (purple) to become silent and the others to change their oscillation pattern. Bottom: in the PC projection, the perturbation causes the joint activity of the network to move from the initial stable m
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/mdhumphries/AplysiaAttractorAnalysis && cd AplysiaAttractorAnalysis && git log -1 --format='%H %ad' && find . -name "*.m" | head -100 | tr '\n' ' '; date -u
```

```
e5f28e986eb3165df1441a49eee4e07c25ee01fe Wed Jul 11 09:57:57 2018 +0100
./Analysis/Mapping/brewermap.m ./Analysis/Mapping/ParticipationMapsSummary.m ./Analysis/P10_analysis/P10_ID_motorneurons.m ./Analysis/P10_analysis/Best_P10_StateSpace_GLMmodels.m ./Analysis/P10_analysis/DecodeP10_statespace.m ./Analysis/DataSet_Properties.m ./Analysis/Classify_attractors/Toy3DOscillator.m ./Analysis/Classify_attractors/Analyse_by_Recurrence_Points.m ./Analysis/Classify_attractors/Does_Oscillation_Period_Change.m ./Analysis/Classify_attractors/Initial_Conditions.m ./Analysis/Classify_attractors/Quantifying_Participation_by_PCA_Contribution.m ./Analysis/Classify_attractors/RobustnessOfAttractor_to_single_neuron_variability.m ./Analysis/Classify_attractors/Are_sequential_attractors_the_same.m ./Analysis/Classify_attractors/What_is_Participation.m ./Analysis/Classify_attractors/LocalLinearDynamics.m ./Analysis/Classify_attractors/Dimensionality_of_Projections.m ./Analysis/Classify_attractors/Are_sequential_attractors_the_same_CommonAxes.m ./Analysis/Classify_attractors/recurrence_point_results_Viz.m ./Analysis/Classify_attractors/Are_jumps_perturbations_or_transitions2.m ./Analysis/Classify_attractors/Check_All_Real_Eigenvalues.m ./Analysis/Classify_attractors/Quantify_attractors_by_recurrence_plot_lines.m ./Analysis/Classify_attractors/RecurrencePlot_LineCounting.m ./Analysis/Classify_attractors/CatalogueAttractors_by_recurrence.m ./Analysis/Ensembles/Change_of_Firing_Rates_StaticEnsembles.m ./Analysis/Ensembles/StaticEnsembles.m ./Analysis/Ensembles/Analyse_Spike_Train_Properties.m ./Analysis/Ensembles/Types_of_Ensemble_Across_Dataset.m ./Analysis/Ensembles/Consistency_of_Types_Across_Programs.m ./Functions/MIpartitions.m ./Functions/bimodalGammaPDF.m ./Functions/allevsplitConTransitive.m ./Functions/shadedErrorBar.m ./Functions/expectedA.m ./Functions/discreteinvrnd.m ./Functions/VIpartitions.m ./Functions/LinkedUnivariateScatterPlots.m ./Functions/consensusmatrix.m ./Functions/A
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && cat Analysis/DataSet_Properties.m Functions/convolve_spiketrains.m | grep -v "^\s*%" | grep -v "^\s*$" | head -250
```

```
clear all
close all
addpath ../Functions/
if ismac
    gpath = genpath('[removed: a home directory path]/Dropbox/My Toolboxes/Other tools/chronux/');
else
    gpath = genpath('C:\Users\mqbssmhg.DS\Dropbox\My Toolboxes\Other tools\chronux\');  % PC
end
addpath(gpath)
spikepath = '../Data/Spikes/'; % path
fname_Pre = '';  % prefix
stimset = 'da03';  % 'da01': first; 'da02': second; and 'da03' : third
stimstart = 30; % 30 s into recording
stimoff = 32.5; % 2.5 s stimulation
Qt = 0.01;
VarExplained = 0.95;  % 95%
params.Fs = 1000; % sampling time-step is 1 ms
params.trialave = 1; % average over all spike-trains
params.fpass = [0 1];
params.err = [2 0.05];
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && for f in Functions/spike_train_from_times.m Analysis/Classify_attractors/Analyse_by_Recurrence_Points.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -v "^\s*$" | grep -v "^\s*figure\|^\s*plot\|xlabel\|ylabel\|title(\|axis\|colormap\|hold on\|subplot" ; done
```

```
=== Functions/spike_train_from_times.m
function [y,bins] = spike_train_from_times(times,bin_size,T)
time_seconds = T(2) - T(1);
bins = T(1)+bin_size/2:bin_size:T(2)-bin_size/2;
y = hist(times(times<T(2)),bins);
=== Analysis/Classify_attractors/Analyse_by_Recurrence_Points.m
clear all; close all
addpath ../../Functions/
fname = 'da03';
prefix = ''; % '5HT';  % ''; for main data
load(['../' prefix fname '_DataProperties_FunctionAndWindowSize'],'PCAdata','Data','SDF')
nfiles = numel(PCAdata);
pars.stimstart = 30; % (s)
pars.T0 = 35;  % start counting after stim (s)
pars.maxWindow = 10;  % stop before end of time-series (s)
pars.VarExplained = 0.80;    % how many PCs to keep
pars.prctTheta = [2 5 10]; %[1,3,5]; %  % of distance distribution to use as threshold; max distance to check (spikes/s)
pars.bstep = 1;  % s
pars.bins = 0:pars.bstep:50;  % recurrence time pars.bins (s);
pars.tmin = 5;  % s; minimum recurrence time to count as a peak
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && for f in Analysis/Classify_attractors/LocalLinearDynamics.m Analysis/Classify_attractors/recurrence_point_results_Viz.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -v "^\s*$" | grep -v "^\s*figure\|^\s*plot\|xlabel\|ylabel\|title(\|axis\|colormap\|hold on\|subplot\|exportPPT\|line(\|set(gca\|text(\|xlim\|ylim\|bar(\|errorbar\|scatter\|print\|stairs\|hist(\|legend\|caxis\|imagesc\|colorbar\|clf\|drawnow\|figure(" ; done
```

```
=== Analysis/Classify_attractors/LocalLinearDynamics.m
function [Emax,Egs,RotPeriod,Npts,Cond,R2] = LocalLinearDynamics(IDs,statespace,ix0,Theta,NeighbourD,DT)
dims = size(statespace,2); 
Egs = zeros(numel(IDs),dims);
if isempty(gcp('nocreate'))
    parpool('local',10);
end
for iN = 1:numel(IDs)
    ixRecr = IDs(iN);
    pt0 = statespace(ix0+ixRecr,:);  % x_i of recurrence point (ix0 is first sampled point in state-space)
    D = sqrt(sum(bsxfun(@minus,statespace,pt0).^2,2)); % Euclidean distance to all points
    currixs = find(D <= NeighbourD * Theta);  % all distances within Theta neighbourhood
    back = 0; fwd=numel(currixs+1);
    ixPt = find(currixs == ix0+ixRecr);  % recurrence point's location within the neighbourhood
    ixshift = abs(currixs - ixPt);  
    dshift = diff(ixshift); % difference between adjacent indices in neighbourhood
    back = find(dshift(1:ixPt-1) > 1,1,'last'); if isempty(back) back = 0; end
    fwd = find(dshift(ixPt:end) > 1,1,'first')+ixPt; if isempty(fwd) fwd = numel(currixs)+1; end
    Npts(iN) = numel(currixs(back+1:fwd-1));
    ixPtshft = ixPt - back+1; % index of current point within retained contiguous portion
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && strip(){ grep -v "^\s*%" "$1" | sed 's/%.*$//' | grep -v "^\s*$" | grep -iv "^\s*figure\|^\s*plot\|xlabel\|ylabel\|title(\|^\s*axis\|colormap\|hold on\|subplot\|exportPPT\|^\s*line(\|set(gca\|^\s*text(\|xlim\|ylim\|^\s*bar(\|errorbar\|scatter\|^\s*print\|stairs\|legend\|caxis\|imagesc\|colorbar\|^\s*clf\|drawnow\|'Color'\|FontSize\|^\s*end\s*$\|^\s*box\|^\s*tic\|^\s*toc" ; }; for f in Analysis/Classify_attractors/Are_sequential_attractors_the_same.m Analysis/Classify_attractors/Are_jumps_perturbations_or_transitions2.m Analysis/Classify_attractors/Does_Oscillation_Period_Change.m Functions/WeightedCorrelation.m; do echo "=== $f"; strip $f; done
```

```
=== Analysis/Classify_attractors/Are_sequential_attractors_the_same.m
clear all; close all
addpath ../../Functions/
spars.stimstart = 30;  
spars.VmaxD = 3;  
spars.minDens = 0; 
spars.ixT = 3; 
spars.minRecur = 90; 
spars.manifoldT = 5; 
spars.divPeriod = 0;  
spars.nShuffles = 100;  
fname_Pre = '';
load ../da01_DataProperties_FunctionAndWindowSize FileTable
nfiles = numel(FileTable);
load RecurrenceStats RcrStats
fnames = {'da01','da02','da03'};
ixExample = 1;
feature('numCores');
if isempty(gcp('nocreate'))
    parpool('local',10);
[... 388 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/AplysiaAttractorAnalysis && strip(){ grep -v "^\s*%" "$1" | sed 's/%.*$//' | grep -v "^\s*$" | grep -iv "^\s*figure\|^\s*plot\|xlabel\|ylabel\|title(\|^\s*axis\|colormap\|hold on\|subplot\|exportPPT\|^\s*line(\|set(gca\|^\s*text(\|xlim\|ylim\|^\s*bar(\|errorbar\|scatter\|^\s*print\|stairs\|legend\|caxis\|imagesc\|colorbar\|^\s*clf\|drawnow\|'Color'\|FontSize\|^\s*end\s*$\|^\s*box\|^\s*tic\|^\s*toc\|^\s*set(\|^\s*h.*=.*plot\|LinkedUni\|UnpairedUni" ; }; for f in Analysis/Classify_attractors/Check_All_Real_Eigenvalues.m Analysis/Classify_attractors/Quantifying_Participation_by_PCA_Contribution.m Functions/iterateoutliers.m Analysis/Classify_attractors/What_is_Participation.m Analysis/Classify_attractors/RobustnessOfAttractor_to_single_neuron_variability.m Analysis/Classify_attractors/Initial_Conditions.m; do echo "=== $f"; strip $f; done
```

```
Sun Nov  8 12:08:36 UTC 2026
=== Analysis/Classify_attractors/Check_All_Real_Eigenvalues.m
clear all; close all;
addpath ../../Functions/
Eigpars.ixT = 3; 
Eigpars.Same = 1e-7;
load da01_RecurrencePointsData_FilterPts RcrPtData
fname_Pre = '';
fnames = {'da01','da02','da03'};
nPreps = numel(RcrPtData);
cmap = brewermap(10,'Paired'); 
Msize = [3 9 5];   
Msize = [4 4 4];
for iPrep = 1:nPreps
   for iStim = 1:numel(fnames) 
       load([fname_Pre fnames{iStim} '_RecurrencePointsData_FilterPts'],'RcrPtData','pars');
       load(['../' fname_Pre  fnames{iStim} '_DataProperties_FunctionAndWindowSize'],'Data','FileTable')
       nPoints = [RcrPtData(iPrep).Orbit(Eigpars.ixT).Period(:).nPoints];
       ixPrd = find(nPoints == max(nPoints));  
       usedPts = RcrPtData(iPrep).Orbit(Eigpars.ixT).Period(ixPrd).Npts >= pars.minNeighbours;
[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && strip(){ grep -v "^\s*%" "$1" | sed 's/%.*$//' | grep -v "^\s*$" | grep -iv "^\s*figure\|^\s*plot\|xlabel\|ylabel\|title(\|^\s*axis\|colormap\|hold on\|subplot\|exportPPT\|^\s*line(\|set(gca\|^\s*text(\|xlim\|ylim\|^\s*bar(\|errorbar\|^\s*print\|stairs\|legend\|caxis\|imagesc\|colorbar\|^\s*clf\|drawnow\|'Color'\|FontSize\|^\s*end\s*$\|^\s*box\|^\s*tic\|^\s*toc\|^\s*set(\|^\s*h.*=.*plot\|LinkedUni\|UnpairedUni" ; }; for f in Analysis/P10_analysis/P10_ID_motorneurons.m Analysis/P10_analysis/DecodeP10_statespace.m Analysis/P10_analysis/Best_P10_StateSpace_GLMmodels.m Analysis/Ensembles/StaticEnsembles.m; do echo "=== $f"; strip $f; done
```

```
=== Analysis/P10_analysis/P10_ID_motorneurons.m
clear all; close all
datapath = '../../Data/P10/';
spikepath = '../../Data/Spikes/';
addpath ../../Functions/
MNpars.stimstart = 30;
MNpars.endwin = 123;  
MNpars.strtMatch = 33;  
MNpars.GaussQt = 0.001;  
MNpars.GaussSD = 0.002;
MNpars.Tvar = 0.002;  
MNpars.d = [0:0.001:0.025];  
MNpars.dbins = round(MNpars.d ./ MNpars.GaussQt); 
files = dir(datapath); files(1:2) = []; 
ixda01 = find(arrayfun(@(x) any(findstr(x.name,'da01')),files)); 
ixda02 = find(arrayfun(@(x) any(findstr(x.name,'da02')),files)); 
ixda03 = find(arrayfun(@(x) any(findstr(x.name,'da03')),files)); 
ixall = [ixda01; ixda02; ixda03];
seqall = [ones(numel(ixda01),1); ones(numel(ixda02),1)+1; ones(numel(ixda03),1)+2];
nfiles = numel(ixall); 
[... 345 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && strip(){ grep -v "^\s*%" "$1" | sed 's/%.*$//' | grep -v "^\s*$" | grep -iv "xlabel\|ylabel\|title(\|colormap\|hold on\|exportPPT\|set(gca\|xlim\|ylim\|legend\|caxis\|colorbar\|^\s*clf\|drawnow\|FontSize\|^\s*end\s*$\|^\s*box\|^\s*tic\|^\s*toc\|^\s*set(" ; }; strip Analysis/Mapping/ParticipationMapsSummary.m | head -120; echo ====; strip Figures/Figure_LinearDynamics.m | grep -i "patch\|vertices\|exp\|2\*pi\|mEig\|0\.0" | head -30; echo ===; diff <(strip Analysis/Classify_attractors/Are_sequential_attractors_the_same.m) <(strip Analysis/Classify_attractors/Are_sequential_attractors_the_same_CommonAxes.m) | head -80
```

```
clear all; close all
load Participation
load MapCoords
load diode_template_adjusted
load FileTable
LEFT = [1,2,4,10];
RIGHT = [3,5,6,9];
Mscale = 25;  
Rscale = 50;
xtiles = 5;  
Group = LEFT;
FileTable{LEFT}
FileTable{RIGHT}
nPreps = numel(Participation);
for  i = 1:nPreps
    ParticipationRange{i} = max(Participation(i).Normalised) - min(Participation(i).Normalised);
for i = 1:nPreps
    MaxR(i) = max(max(ParticipationRange{1,i}));
for i = 1:nPreps
    MinR(i) = min(min(ParticipationRange{1,i}));
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AplysiaAttractorAnalysis && cat Functions/expectedA.m | grep -v "^\s*%"; wc -l Functions/consensus_cluster_spike_data_binless.m Analysis/Ensembles/Analyse_Spike_Train_Properties.m; ls Analysis/Ensembles; grep -rn "Analyse_Spike_Train_Properties\|function" Analysis/Ensembles/Analyse_Spike_Train_Properties.m | head
```

```
function P = expectedA(A)

[n c] = size(A);
inks = sum(A);
outks = sum(A');
m = sum(inks);  % number of edges

P = (outks' * inks) ./ m;
  323 Functions/consensus_cluster_spike_data_binless.m
  246 Analysis/Ensembles/Analyse_Spike_Train_Properties.m
  569 total
Analyse_Spike_Train_Properties.m
Change_of_Firing_Rates_StaticEnsembles.m
Consistency_of_Types_Across_Programs.m
StaticEnsembles.m
Types_of_Ensemble_Across_Dataset.m
26:addpath ../../Functions/  % add list of local functions to path
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p entries/crcns-apl-1-bruno-2017 && date -u
```

```
Sun Nov  8 12:11:25 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-apl-1-bruno-2017/apl.py",
 "content": "\"\"\"Loading and measures for CRCNS data set apl-1 (Bruno & Frost 2017).\n\nBruno, Frost & Humphries (2017), \"A spiral attractor network drives rhythmic locomotion\",\neLife 6:e27342, doi:10.7554/elife.27342. The data set (doi:10.6080/K0SN074B) holds the spike\ntimes of 30 voltage-sensitive dye recordings (10 preparations, 3 evoked bouts each), the P10\nnerve spikes of 9 of them, and neuron coordinates on the photodiode array. Files are streamed\nfrom the public S3 bucket ``crcnsarchive`` and read in memory; nothing is written to disk.\n\nWhere the parameters come from. \"Methods\" is the paper's Materials and methods; \"code\" is the\npaper's analysis code, https://github.com/mdhumphries/AplysiaAttractorAnalysis at commit\ne5f28e986eb3165df1441a49eee4e07c25ee01fe, as cited by the claims file.\n\n- Stimulation onset 30 s, offset 32.5 s: Methods (Imaging) and the data description.\n- Spike-density functions: 10 ms grid, Gaussian kernel to +/-5 SD with unit area (Methods,\n  Spike-train analysis; code DataSet_Properties.m). The SD is open (claim fig2b-dimensions):\n  ``sd_mode`` 'sqrt12' (median ISI / sqrt(12)), 'twelve' (median ISI / 12, as the extracted\n  text prints), 'own' (median ISI of the recording, the code's choice of width) and 'pooled'\n  (the code's running median over the recordings of the same bout number read so far). The\n  median ISI uses the ISIs of every neuron after stimulation onset (code).\n- PCA on the covariance of the post-onset spike-density functions, mean-centred (Methods,\n  Recurrence analysis; code princomp). Number of PCs: ``count`` 'min80' (smallest number\n  reaching 80%, Methods) or 'le80' (number whose cumulative variance is at most 80%, code\n  Analyse_by_Recurrence_Points.m).\n- Recurrence: theta at the 2nd, 5th and 10th percentiles of all distances between post-onset\n  points; points checked from 35 s to 10 s before the end; the first contiguous run within theta\n  after the point is dropped; histogram of delays in 1 s bins on 0..50 s; peaks are runs of\n  non-empty bins at 5 s or more with at least 100 points; 5 s windows stepped by 1 s (Methods,\n  Recurrence analysis; code Analyse_by_Recurrence_Points.m for the bins, the 100-point rule\n  and the windows).\n- Local linear models: the contiguous run of points within 2.5 theta around each point of the\n  dominant orbit, least squares of the first difference on the points, points with at least 100\n  neighbours averaged (Methods, Statistical estimation of the attractor's parameters; code\n  LocalLinearDynamics.m). The \"maximum eigenvalue\" is the one of largest modulus, as MATLAB's\n  max orders complex numbers (code); ties between a conjugate pair go to the one with positive\n  imaginary part, as MATLAB breaks ties by phase angle.\n- Multitaper spectra: a port of Chronux mtspectrumpt with its default tapers [3 5], 1 ms\n  sampling, fpass 0..1 Hz (Methods, Spike-train analysis; code DataSet_Properties.m).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\nfrom scipy.signal.windows import dpss\nfrom scipy.spatial import cKDTree\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/\"\nFILES = [\"FileTable.mat\", \"SpikeData.mat\", \"ExtracellularData.mat\", \"Coordinates.mat\",\n         \"diode_template.mat\"]\nSTIM_ON, STIM_OFF = 30.0, 32.5\nDT = 0.01\nTHETA_PRCT = (2, 5, 10)\nT0 = 35.0           # start checking recurrence (code pars.T0; Methods \"5 s after stimulation\")\nMAX_WINDOW = 10.0   # stop 10 s before the end\nTMIN = 5.0          # minimum delay for a peak\nNMIN = 100          # minimum points in a peak (code pars.Nmin)\nWIN_L, WIN_STEP = 5.0, 1.0\nNEIGHBOUR_D = 2.5\nMIN_NEIGHBOURS = 100\n\n\ndef _read(name):\n    with fsspec.open(BUCKET + name, \"rb\", block_size=2**20) as f:\n        return f.read()\n\n\ndef load():\n    \"\"\"Stream the data set's MATLAB files. Returns a dict with the raw bytes' MD5 sums,\n    the archive's checksums.md5, and the parsed contents.\"\"\"\n    raw = {n: _read(n) for n in FILES}\n    md5 = {n: hashlib.md5(b).hexdigest() for n, b in raw.items()}\n    listed = {}\n    for line in _read(\"checksums.md5\").decode().splitlines():\n        if line.strip():\n            h, n = line.split()\n            listed[n] = h\n    mats = {n: sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)\n            for n, b in raw.items()}\n    ft = mats[\"FileTable.mat\"][\"FileTable\"]\n    preps = []\n    for i, row in enumerate(ft[1:]):\n        p10 = row[3]\n        preps.append({\"prep\": i + 1, \"file\": str(row[0]), \"name\": str(row[0]).replace(\"da01.mat\", \"\"),\n                      \"side\": str(row[1]), \"n_neurons_table\": int(row[2]),\n                      \"p10_bouts\": [] if isinstance(p10, str) else [int(x) for x in np.atleast_1d(p10)]})\n    recs = []\n    for s in mats[\"SpikeData.mat\"][\"SpikeData\"]:\n        fn = str(s.filename)\n        name = fn[:-8]\n        bout = int(fn[-5])\n        prep = next(p[\"prep\"] for p in preps if p[\"name\"] == name)\n        spks = np.asarray(s.spks, float)\n        recs.append({\"file\": fn, \"prep\": prep, \"bout\": bout, \"Bout_field\": s.Bout,\n                     \"ids\": spks[:, 0].astype(int), \"t\": spks[:, 1]})\n    p10 = []\n    for s in mats[\"ExtracellularData.mat\"][\"ExtracellularData\"]:\n        fn = str(s.filename)\n        spks = np.atleast_2d(np.asarray(s.spks, float))\n        # The P10 file names lack the \"B\" of prep Jun0414B; the code matches on the first 7\n        # characters (DecodeP10_statespace.m), as here.\n        prep = next(p[\"prep\"] for p in preps if p[\"name\"][:7] == fn[:7])\n        p10.append({\"file\": fn, \"prep\": prep, \"bout\": int(s.Bout), \"ids\": spks[:, 0],\n                    \"t\": np.sort(spks[:, 1]), \"sorted\": bool(np.all(np.diff(spks[:, 1]) >= 0))})\n    coords = []\n    for s in mats[\"Coordinates.mat\"][\"Coordinates\"]:\n        coords.append({\"file\": str(s.filename), \"ganglion\": str(s.ganglion),\n                       \"x\": np.asarray(s.x, float), \"y\": np.asarray(s.y, float)})\n    return {\"md5\": md5, \"listed_md5\": listed, \"preps\": preps, \"recs\": recs, \"p10\": p10,\n            \"coords\": coords, \"template\": mats[\"diode_template.mat\"][\"diode_template\"]}\n\n\ndef neuron_trains(rec):\n    \"\"\"Spike times per neuron id 1..N (ids as stored).\"\"\"\n    n = int(rec[\"ids\"].max())\n    return [np.sort(rec[\"t\"][rec[\"ids\"] == i]) for i in range(1, n + 1)]\n\n\ndef post_onset_isis(rec):\n    out = []\n    for tr in neuron_trains(rec):\n        tr = tr[tr >= STIM_ON]\n        if tr.size > 1:\n            out.append(np.diff(tr))\n    return np.concatenate(out)\n\n\ndef gaussian_sds(recs):\n    \"\"\"Kernel SD (s) per recording under each reading of the Methods and the code.\"\"\"\n    own = np.array([np.median(post_onset_isis(r)) for r in recs])\n    pooled = np.zeros(len(recs))\n    for bout in (1, 2, 3):\n        acc = []\n        for i in sorted([i for i, r in enumerate(recs) if r[\"bout\"] == bout],\n                        key=lambda i: recs[i][\"file\"]):\n            acc.append(post_onset_isis(recs[i]))\n            pooled[i] = np.median(np.concatenate(acc))\n    return {\"sqrt12\": own / np.sqrt(12), \"twelve\": own / 12, \"own\": own, \"pooled\": pooled}\n\n\ndef kernel(sd):\n    sig = sd / DT\n    x = np.arange(-5 * sig, 5 * sig + 1e-9, 1.0)\n    h = np.exp(-x**2 / (2 * sig**2))\n    return h / h.sum()\n\n\ndef sdf_matrix(trains, sd, t_end):\n    \"\"\"Spike-density functions (spikes/s) on the grid 0, 0.01, ..., t_end; one column per train.\"\"\"\n    nb = int(np.floor(t_end / DT + 1e-9)) + 1\n    h = kernel(sd)\n    half = (h.size - 1) / 2\n    out = np.zeros((nb, len(trains)))\n    for j, tr in enumerate(trains):\n        k = np.round(tr / DT).astype(int)\n        k = k[(k >= 0) & (k < nb)]\n        c = np.bincount(k, minlength=nb).astype(float)\n        y = np.convolve(c, h)\n        s = int(np.floor(half))\n        out[:, j] = y[s:s + nb]\n    return out / DT\n\n\ndef pca(x):\n    \"\"\"Mean-centred PCA. Returns coeffs (columns), centred projections, eigenvalues (descending).\"\"\"\n    xc = x - x.mean(0)\n    cov = xc.T @ xc / (x.shape[0] - 1)\n    ev, vec = np.linalg.eigh(cov)\n    o = np.argsort(ev)[::-1]\n    ev, vec = np.clip(ev[o], 0, None), vec[:, o]\n    return vec, xc @ vec, ev\n\n\ndef n_pcs(ev, frac=0.8, rule=\"min80\"):\n    cum = np.cumsum(ev) / ev.sum()\n    if rule == \"min80\":\n        return int(np.argmax(cum >= frac - 1e-12) + 1)\n    return int(np.sum(cum <= frac))\n\n\nclass Program:\n    \"\"\"One recording: spike-density functions, PCA, and the recurrence analysis.\"\"\"\n\n    def __init__(self, rec, sd, rule=\"min80\"):\n        self.rec, self.sd, self.rule = rec, sd, rule\n        self.trains = neuron_trains(rec)\n        self.t_end = rec[\"t\"].max()\n        self.sdf = sdf_matrix(self.trains, sd, self.t_end)\n        self.bins = np.arange(self.sdf.shape[0]) * DT\n        self.ix_stim = np.flatnonzero(self.bins >= STIM_ON - 1e-9)\n        self.stimbins = self.bins[self.ix_stim]\n        self.coeffs, self.proj, self.ev = pca(self.sdf[self.ix_stim])\n        self.d = max(n_pcs(self.ev, 0.8, rule), 1)\n        self.pcs = self.proj[:, :self.d]\n\n    # ---------------- recurrence ----------------\n    def recurrence(self, prct=THETA_PRCT):\n        X = self.pcs\n        n = X.shape[0]\n        # all pairwise distances, for the percentiles of theta\n        sq = (X**2).sum(1)\n        thetas = []\n        dists = []\n        for a in range(0, n, 1500):\n            g = sq[a:a + 1500, None] + sq[None, :] - 2 * X[a:a + 1500] @ X.T\n            np.maximum(g, 0, out=g)\n            for r in range(g.shape[0]):\n                dists.append(np.sqrt(g[r, a + r + 1:]))\n        dists = np.concatenate(dists)\n        self.theta = np.percentile(dists, prct)\n        del dists\n        ix0 = int(np.argmin(np.abs(self.stimbins - T0)))\n        ix_end = int(np.argmin(np.abs(self.stimbins - (self.stimbins[-1] - MAX_WINDOW))))\n        self.ix0, self.ix_end = ix0, ix_end\n        pts = np.arange(ix0 + 1, ix_end + 1)       # code: points ix0+1 .. ixEnd\n        delay = np.full((pts.size, len(prct)), np.nan)\n        for a in range(0, pts.size, 500):\n            p = pts[a:a + 500]\n            g = sq[p, None] + sq[None, :] - 2 * X[p] @ X.T\n            g = np.sqrt(np.maximum(g, 0))\n            for r, i in enumerate(p):\n                row = g[r, i + 1:]\n                for k, th in enumerate(self.theta):\n                    idx = np.flatnonzero(row <= th)\n                    if idx.size == 0:\n                        continue\n                    gaps = np.flatnonzero(np.diff(idx) > 1)\n                    if gaps.size == 0:\n                        continue\n                    delay[a + r, k] = (idx[gaps[0] + 1] + 1) * DT\n        self.delay = delay\n        self.pt_index = pts           # index into stimbins of each checked point\n        self.pt_time = self.stimbins[pts]\n        return delay\n\n    def peaks(self, k=-1):\n        \"\"\"Peaks of the delay histogram at threshold k. Returns list of dicts (index arrays).\"\"\"\n        dl = self.delay[:, k]\n        edges = np.arange(0, 51)\n        h = np.zeros(51)\n        v = dl[~np.isnan(dl)]\n        v = v[(v >= 0) & (v <= 50)]\n        bi = np.minimum(np.floor(v + 1e-9).astype(int), 50)\n        np.add.at(h, bi, 1)\n        filled = np.flatnonzero(h[5:] > 0) + 5\n        out = []\n        if filled.size == 0:\n            return out\n        runs = np.split(filled, np.flatnonzero(np.diff(filled) > 1) + 1)\n        for run in runs:\n            lo, hi = edges[run[0]], edges[run[-1]] + 1\n            ids = np.flatnonzero((dl >= lo) & (dl <= hi))\n            if ids.size >= NMIN:\n                out.append({\"ids\": ids, \"mean\": float(np.mean(dl[ids])),\n                            \"median\": float(np.median(dl[ids])), \"n\": int(ids.size),\n                            \"lo\": float(lo), \"hi\": float(hi)})\n        return out\n\n    def dominant(self, k=-1):\n        pk = self.peaks(k)\n        if not pk:\n            return None, pk\n        return max(pk, key=lambda p: p[\"n\"]), pk\n\n    def windows(self, k=-1):\n        \"\"\"5 s windows stepped by 1 s: start index (stimbins), mid time, density of recurrent\n        points, mean and SD of delays (code AllRecurrentPoint).\"\"\"\n        win = int(round(WIN_L / DT))\n        step = int(round(WIN_STEP / DT))\n        starts = np.arange(self.ix0, self.ix_end - win + 1, step)\n        dl = self.delay[:, k]\n        rel = self.pt_index - self.ix0     # 1..nTs\n        dens, md, sdd, mids = [], [], [], []\n        for s in starts:\n            m = (rel > s - self.ix0) & (rel <= s + win - self.ix0)\n            v = dl[m]\n            ok = ~np.isnan(v)\n            dens.append(ok.sum() / win)\n            md.append(np.mean(v[ok]) if ok.any() else np.nan)\n            sdd.append(np.std(v[ok], ddof=1) if ok.sum() > 1 else np.nan)\n            mids.append(self.stimbins[int(round(s + win / 2))])\n        return {\"start\": starts, \"start_t\": self.stimbins[starts], \"mid_t\": np.array(mids),\n                \"dens\": np.array(dens), \"mdelay\": np.array(md), \"sddelay\": np.array(sdd)}\n\n    # ---------------- local linear dynamics ----------------\n    def local_linear(self, ids, k=-1):\n        \"\"\"Local linear models around the checked points ``ids`` (rows of self.delay).\"\"\"\n        X = self.pcs\n        th = self.theta[k] * NEIGHBOUR_D\n        out_eigs = np.full((len(ids), self.d), np.nan, complex)\n        npts = np.zeros(len(ids), int)\n        sq = (X**2).sum(1)\n        for a in range(0, len(ids), 500):\n            chunk = ids[a:a + 500]\n            p = self.pt_index[chunk]\n            g = sq[p, None] + sq[None, :] - 2 * X[p] @ X.T\n            within = g <= th**2\n            for r, i in enumerate(p):\n                w = within[r]\n                # contiguous run of within-neighbourhood points containing the point\n                lo = i\n                while lo > 0 and w[lo - 1]:\n                    lo -= 1\n                hi = i\n                while hi < len(w) - 1 and w[hi + 1]:\n                    hi += 1\n                seg = X[lo:hi + 1]\n                npts[a + r] = seg.shape[0]\n                if seg.shape[0] < 3:\n                    continue\n                A, *_ = np.linalg.lstsq(seg[:-1], np.diff(seg, axis=0), rcond=None)\n                e = np.linalg.eigvals(A)\n                # MATLAB sort(...,'descend') on complex: by modulus, then phase angle\n                o = np.lexsort((-np.angle(e), -np.abs(e)))\n                out_eigs[a + r] = e[o]\n        return out_eigs, npts\n\n\ndef emax_stats(eigs, npts):\n    \"\"\"Mean real and imaginary part of the maximum eigenvalue over points with enough\n    neighbours (code recurrence_point_results_Viz.m).\"\"\"\n    use = npts >= MIN_NEIGHBOURS\n    em = eigs[use, 0]\n    rot = 2 * np.pi / np.imag(em) * DT\n    rot[~np.isfinite(rot)] = 0\n    return {\"a\": float(np.mean(em.real)), \"b\": float(np.mean(em.imag)),\n            \"sd_a\": float(np.std(em.real, ddof=1)), \"sd_b\": float(np.std(em.imag, ddof=1)),\n            \"n_used\": int(use.sum()), \"n_all\": int(len(npts)), \"mrot\": float(np.mean(rot)),\n            \"eigs\": eigs[use]}\n\n\ndef hausdorff_dirs(A, B):\n    \"\"\"Directed max-min distances (A to B, B to A).\"\"\"\n    da = cKDTree(B).query(A)[0]\n    db = cKDTree(A).query(B)[0]\n    return da.max(), db.max()\n\n\n# ---------------- multitaper spectrum (Chronux mtspectrumpt port) ----------------\ndef mtspectrumpt(trains, fs=1000.0, fpass=(0.0, 1.0), tapers=(3, 5)):\n    \"\"\"Port of Chronux mtspectrumpt with trialave=1: point-process multitaper spectrum,\n    averaged over the trains. Time grid from the earliest to the latest spike, minus and plus\n    one sample, as Chronux's minmaxsptimes.\"\"\"\n    allt = np.concatenate([t for t in trains if t.size])\n    dt = 1 / fs\n    t = np.arange(allt.min() - dt, allt.max() + dt + dt / 2, dt)\n    N = t.size\n    nfft = max(int(2 ** np.ceil(np.log2(N))), N)\n    f = np.arange(nfft) * fs / nfft\n    findx = (f >= fpass[0]) & (f <= fpass[1])\n    f = f[findx]\n    tp = dpss(N, tapers[0], tapers[1]).T * np.sqrt(fs)    # N x K\n    w = 2 * np.pi * f\n    # H = fft of tapers at the retained frequencies\n    H = np.exp(-1j * np.outer(w, np.arange(N) * dt)) @ tp  # nf x K\n    S = np.zeros(f.size)\n    for tr in trains:\n        d = tr[(tr >= t.min()) & (tr <= t.max())]\n        msp = d.size / N\n        if d.size == 0:\n            continue\n        proj = np.column_stack([np.interp(d, t, tp[:, k]) for k in range(tp.shape[1])])\n        ex = np.exp(-1j * np.outer(w, d - t[0]))\n        J = ex @ proj - H * msp\n        S += np.mean(np.abs(J) ** 2, axis=1)\n    return f, S / len(trains)\n\n\ndef peak_frequency(f, S):\n    \"\"\"Code DataSet_Properties.m: power-weighted mean frequency of the region more than 2 SD\n    above the spectrum's mean.\"\"\"\n    hi = S > S.mean() + 2 * S.std(ddof=1)\n    return float(np.sum(f[hi] * S[hi]) / S[hi].sum())\n"
}
```

```
File created successfully at: entries/crcns-apl-1-bruno-2017/apl.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-apl-1-bruno-2017 && python - <<'EOF'
import re
s=open('apl.py').read()
s=s.replace("""    # H = fft of tapers at the retained frequencies
    H = np.exp(-1j * np.outer(w, np.arange(N) * dt)) @ tp  # nf x K
""","""    H = np.fft.fft(tp, nfft, axis=0)[findx]                # fft of tapers, retained frequencies
""")
s=s.replace("""        sq = (X**2).sum(1)
        thetas = []
        dists = []
        for a in range(0, n, 1500):
            g = sq[a:a + 1500, None] + sq[None, :] - 2 * X[a:a + 1500] @ X.T
            np.maximum(g, 0, out=g)
            for r in range(g.shape[0]):
                dists.append(np.sqrt(g[r, a + r + 1:]))
        dists = np.concatenate(dists)
        self.theta = np.percentile(dists, prct)
        del dists
""","""        sq = (X**2).sum(1)
        dists = pdist(X)
        self.theta = np.percentile(dists, prct)
        del dists
""")
s=s.replace("from scipy.spatial import cKDTree","from scipy.spatial import cKDTree\nfrom scipy.spatial.distance import pdist")
open('apl.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-apl-1-bruno-2017 && python - <<'EOF'
import time, numpy as np, apl, resource
t=time.time(); D=apl.load(); print('load',time.time()-t)
print({k:(v==D['listed_md5'].get(k)) for k,v in D['md5'].items()})
recs=D['recs']
sds=apl.gaussian_sds(recs)
for k,v in sds.items(): print(k, np.round(v,3))
t=time.time()
for mode in sds:
  ds=[]
  for i,r in enumerate(recs):
    P=apl.Program(r, sds[mode][i])
    ds.append((apl.n_pcs(P.ev,0.8,'min80'), apl.n_pcs(P.ev,0.8,'le80'), len(P.trains)))
  ds=np.array(ds); print(mode, ds[:,0].tolist(), ds[:,1].tolist())
print('time',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
load 2.451535224914551
{'FileTable.mat': True, 'SpikeData.mat': True, 'ExtracellularData.mat': True, 'Coordinates.mat': True, 'diode_template.mat': True}
sqrt12 [0.098 0.092 0.088 0.117 0.123 0.091 0.114 0.095 0.091 0.093 0.106 0.099
 0.08  0.083 0.069 0.077 0.075 0.078 0.106 0.103 0.085 0.109 0.125 0.114
 0.12  0.124 0.117 0.115 0.106 0.101]
twelve [0.028 0.026 0.026 0.034 0.035 0.026 0.033 0.028 0.026 0.027 0.031 0.028
 0.023 0.024 0.02  0.022 0.022 0.023 0.031 0.03  0.025 0.031 0.036 0.033
 0.035 0.036 0.034 0.033 0.031 0.029]
own [0.341 0.317 0.306 0.404 0.426 0.314 0.394 0.331 0.317 0.323 0.368 0.342
 0.276 0.287 0.238 0.268 0.26  0.271 0.369 0.357 0.296 0.377 0.432 0.396
 0.416 0.43  0.404 0.4   0.366 0.352]
pooled [0.341 0.317 0.306 0.363 0.347 0.309 0.374 0.34  0.312 0.363 0.349 0.32
 0.342 0.337 0.306 0.325 0.322 0.298 0.328 0.325 0.298 0.337 0.337 0.309
 0.347 0.347 0.315 0.35  0.349 0.317]
sqrt12 [28, 30, 35, 22, 24, 25, 40, 36, 41, 25, 32, 35, 29, 29, 33, 36, 32, 36, 24, 22, 27, 32, 31, 36, 32, 30, 29, 28, 28, 31] [27, 29, 34, 21, 23, 24, 39, 35, 40, 24, 31, 34, 28, 28, 32, 35, 31, 35, 23, 21, 26, 31, 30, 35, 31, 29, 28, 27, 27, 30]
twelve [66, 66, 72, 47, 49, 49, 73, 71, 75, 64, 70, 76, 50, 49, 49, 64, 64, 66, 36, 34, 36, 52, 51, 57, 57, 55, 53, 45, 43, 45] [65, 65, 71, 46, 48, 48, 72, 70, 74, 63, 69, 75, 49, 48, 48, 63, 63, 65, 35, 33, 35, 51, 50, 56, 56, 54, 52, 44, 42, 44]
own [7, 7, 8, 4, 5, 5, 8, 7, 7, 5, 4, 5, 5, 5, 6, 6, 5, 6, 7, 6, 8, 5, 6, 7, 6, 6, 6, 6, 6, 7] [6, 6, 7, 3, 4, 4, 7, 6, 6, 4, 3, 4, 4, 4, 5, 5, 4, 5, 6, 5, 7, 4, 5, 6, 5, 5, 5, 5, 5, 6]
pooled [7, 7, 8, 5, 6, 5, 9, 7, 7, 5, 4, 5, 4, 5, 5, 5, 5, 6, 7, 6, 8, 6, 7, 8, 7, 7, 7, 6, 6, 8] [6, 6, 7, 4, 5, 4, 8, 6, 6, 4, 3, 4, 3, 4, 4, 4, 4, 5, 6, 5, 7, 5, 6, 7, 6, 6, 6, 5, 5, 7]
time 10.641669034957886 0.270716
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-apl-1-bruno-2017 && python - <<'EOF'
import time, numpy as np, apl, resource
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
for i in [0,9]:
  for rule in ['min80','le80']:
    t=time.time(); P=apl.Program(recs[i], sds['pooled'][i], rule); P.recurrence(); t1=time.time()-t
    dom,pk=P.dominant()
    w=P.windows()
    t=time.time(); e,n=P.local_linear(dom['ids']); t2=time.time()-t
    st=apl.emax_stats(e,n)
    rec=~np.isnan(P.delay[:,-1])
    print(i,rule,'d',P.d,'theta',P.theta.round(2),'rec t',round(t1,1),'lld t',round(t2,1),'npeaks',len(pk),[(p['n'],round(p['mean'],2),round(p['median'],2)) for p in pk],'prop rec',rec.mean().round(3),
      'coal', w['mid_t'][np.argmax(w['dens']>0.9)] if (w['dens']>0.9).any() else None, {k:st[k] for k in ['a','b','n_used','n_all','mrot']}, 2*np.pi/st['b']*0.01)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
entries/crcns-apl-1-bruno-2017/apl.py:321: RuntimeWarning: divide by zero encountered in divide
  rot = 2 * np.pi / np.imag(em) * DT
0 min80 d 7 theta [ 4.94  7.56 10.05] rec t 1.6 lld t 8.7 npeaks 4 [(117, 6.94, 7.16), (5137, 14.98, 15.24), (262, 24.5, 24.44), (188, 30.55, 30.01)] prop rec 0.842 coal 42.5 {'a': -0.0002859967101665408, 'b': 0.007876242790988707, 'n_used': 5137, 'n_all': 5137, 'mrot': 9.315105972729116} 7.977389059626558
0 le80 d 6 theta [4.65 7.1  9.35] rec t 1.6 lld t 6.3 npeaks 4 [(277, 7.75, 7.62), (4981, 15.0, 15.13), (110, 25.01, 25.79), (147, 30.22, 29.93)] prop rec 0.844 coal 42.5 {'a': -0.0004663052591537126, 'b': 0.00748184873593937, 'n_used': 4981, 'n_all': 4981, 'mrot': 9.62720692612308} 8.397904754473377
9 min80 d 5 theta [2.12 3.15 4.36] rec t 1.5 lld t 3.0 npeaks 1 [(2777, 10.47, 8.89)] prop rec 0.582 coal 79.5 {'a': 0.0004497505268784448, 'b': 0.008687193865069576, 'n_used': 2777, 'n_all': 2777, 'mrot': 9.948753059450777} 7.232698388882178
9 le80 d 4 theta [1.58 2.47 3.56] rec t 1.5 lld t 2.1 npeaks 1 [(2657, 11.35, 12.58)] prop rec 0.622 coal 79.5 {'a': 0.001443836986666043, 'b': 0.005723679663392769, 'n_used': 2657, 'n_all': 2657, 'mrot': 16.72955363634859} 10.977527878377394
0.946216
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('apl.py').read()
old=s[s.index("            for r, i in enumerate(p):\n                w = within[r]"):s.index("                seg = X[lo:hi + 1]")]
new='''            for r, i in enumerate(p):
                w = within[r]
                # contiguous run of within-neighbourhood points containing the point
                before = np.flatnonzero(~w[:i])
                after = np.flatnonzero(~w[i + 1:])
                lo = before[-1] + 1 if before.size else 0
                hi = i + after[0] if after.size else len(w) - 1
'''
s=s.replace(old,new)
s=s.replace('''    rot = 2 * np.pi / np.imag(em) * DT
    rot[~np.isfinite(rot)] = 0''','''    with np.errstate(divide="ignore"):
        rot = 2 * np.pi / np.imag(em) * DT
    rot[~np.isfinite(rot)] = 0       # code: inf (no rotation) set to 0''')
s+='''

def analyse_program(args):
    """Recurrence analysis of one recording under one reading; with ``lld`` also the local
    linear models of the dominant orbit at the 10% threshold. Returns plain arrays."""
    rec, sd, rule, lld = args
    P = Program(rec, sd, rule)
    P.recurrence()
    out = {"file": rec["file"], "prep": rec["prep"], "bout": rec["bout"], "sd": sd, "rule": rule,
           "d": P.d, "ev": P.ev, "theta": P.theta, "delay": P.delay, "pt_index": P.pt_index,
           "pt_time": P.pt_time, "ix0": P.ix0, "ix_end": P.ix_end, "t_end": P.t_end,
           "n_neurons": len(P.trains)}
    out["peaks"] = [P.peaks(k) for k in range(len(THETA_PRCT))]
    out["windows"] = [P.windows(k) for k in range(len(THETA_PRCT))]
    if lld:
        dom, _ = P.dominant(-1)
        if dom is not None:
            out["eigs"], out["npts"] = P.local_linear(dom["ids"])
    return out


def run_all(recs, sds, rule, lld=True, workers=3):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    jobs = [(r, float(s), rule, lld) for r, s in zip(recs, sds)]
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        return list(ex.map(analyse_program, jobs))
'''
open('apl.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python - <<'EOF'
import time, numpy as np, apl, resource, os
os.environ['OMP_NUM_THREADS']='1'
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
t=time.time(); P=apl.Program(recs[0], sds['pooled'][0], 'min80'); P.recurrence(); dom,pk=P.dominant()
t=time.time(); e,n=P.local_linear(dom['ids']); print('lld',time.time()-t, apl.emax_stats(e,n)['a'])
t=time.time(); out=apl.run_all(recs[:6], sds['pooled'][:6], 'min80'); print('6 recs', time.time()-t)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
EOF
```

```
lld 3.684957981109619 -0.0002859967101665408
6 recs 23.749779224395752
0.872528 0.873676
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python - <<'EOF'
import time, numpy as np, apl, pickle, os
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
res={}
for mode in ['own','pooled']:
  for rule in ['min80','le80']:
    t=time.time(); res[(mode,rule)]=apl.run_all(recs, sds[mode], rule, True, workers=4); print(mode,rule,time.time()-t, flush=True)
pickle.dump(res, open(os.environ['TMPDIR']+'/res_c.pkl','wb'))
EOF
date -u
```

```
own min80 38.75413155555725
own le80 33.33482813835144
pooled min80 40.93587374687195
pooled le80 35.63585710525513
Sun Nov  8 12:17:29 UTC 2026
```

**Agent calls Bash**

```bash
cat >> apl.py <<'EOF'


# ---------------- summaries of the recurrence analysis ----------------
def summarise(o, k=-1):
    """Dominant orbit, density and coalescence of one analysed program at threshold k."""
    pk = o["peaks"][k]
    dl = o["delay"][:, k]
    rec = ~np.isnan(dl)
    hist_n = int(np.sum(rec & (dl >= TMIN) & (dl <= 50)))
    s = {"file": o["file"], "prep": o["prep"], "bout": o["bout"], "d": o["d"],
         "n_peaks": len(pk), "prop_recurrent": float(rec.mean()), "n_points": int(dl.size)}
    if pk:
        dom = max(pk, key=lambda p: p["n"])
        s.update(period_mean=dom["mean"], period_median=dom["median"], dom_n=dom["n"],
                 prop_dom_hist=dom["n"] / hist_n, prop_dom_all=dom["n"] / int(rec.sum()))
    else:
        s.update(period_mean=np.nan, period_median=np.nan, dom_n=0, prop_dom_hist=np.nan,
                 prop_dom_all=np.nan)
    w = o["windows"][k]
    hi = np.flatnonzero(w["dens"] > 0.9)
    s["coalesce_t"] = float(w["mid_t"][hi[0]]) if hi.size else np.nan
    if hi.size:
        after = np.flatnonzero(w["pt_after"] if False else (o["pt_time"] >= w["mid_t"][hi[0]]))
        s["prop_recurrent_after"] = float(rec[after].mean()) if after.size else np.nan
    else:
        s["prop_recurrent_after"] = np.nan
    return s


def divergences(o, period, k=-1, cycles=2.0):
    """Divergent periods after coalescence (Methods, Testing return to the same manifold):
    runs of 5 s windows with recurrence density below 90% that fall below 50% at least once.
    Returns one dict per period with the divergent point (window of lowest density), whether
    density returns above 90%, whether it lies within ``cycles`` periods of the end, and the
    proportions for the same-manifold test."""
    w = o["windows"][k]
    dens = w["dens"]
    hi = np.flatnonzero(dens > 0.9)
    if not hi.size:
        return []
    first = hi[0]
    low = dens < 0.9
    low[:first + 1] = False
    out = []
    idx = np.flatnonzero(low)
    if not idx.size:
        return out
    runs = np.split(idx, np.flatnonzero(np.diff(idx) > 1) + 1)
    t_end = o["t_end"]
    dl = o["delay"][:, k]
    win = int(round(WIN_L / DT))
    rel = o["pt_index"] - o["ix0"]
    for run in runs:
        if dens[run].min() >= 0.5:
            continue
        ip = run[np.argmin(dens[run])]
        returned = run[-1] + 1 < dens.size        # a later window is above 90%
        t_point = float(w["mid_t"][ip])
        near_end = (t_end - t_point) < cycles * period
        d = {"start_win": int(run[0]), "end_win": int(run[-1]), "point_win": int(ip),
             "t_point": t_point, "min_dens": float(dens[ip]), "returned": bool(returned),
             "near_end": bool(near_end)}
        if returned:
            before = run[0] - 1                    # final window before the divergent period
            s = w["start"][before]
            m = (rel > s - o["ix0"]) & (rel <= s + win - o["ix0"])
            nxt = o["pt_time"][m] + dl[m]
            nxt = nxt[~np.isnan(nxt)]
            t_return = float(w["start_t"][run[-1] + 1])   # start of the first window back above 90%
            d.update(t_return=t_return, n_before=int(nxt.size),
                     p_after_end=float(np.mean(nxt > t_return)) if nxt.size else np.nan,
                     p_after_point=float(np.mean(nxt > t_point)) if nxt.size else np.nan)
        out.append(d)
    return out


def weighted_r(x, y, w):
    sw = w.sum()
    mx, my = (w * x).sum() / sw, (w * y).sum() / sw
    cxx = (w * (x - mx) ** 2).sum() / sw
    cyy = (w * (y - my) ** 2).sum() / sw
    cxy = (w * (x - mx) * (y - my)).sum() / sw
    return cxy / np.sqrt(cxx * cyy)


def _ranks(v):
    r = np.empty(v.size)
    r[np.argsort(v, kind="stable")] = np.arange(1, v.size + 1)
    return r


def weighted_spearman(x, y, w, n_perm=10000, rng=None, pooled=False):
    """Weighted Spearman correlation (Methods, Tracking changes in periodicity; code
    WeightedCorrelation.m, which ranks without averaging ties) with a permutation p-value.
    ``pooled=False``: y is permuted against x, two-sided (the Methods give only "a permutation
    test with 10000 permutations"). ``pooled=True``: the code's test, which permutes the pooled
    x and y values and is one-sided in the direction of rho."""
    ok = ~(np.isnan(x) | np.isnan(y))
    x, y, w = x[ok], y[ok], w[ok]
    rx, ry = _ranks(x), _ranks(y)
    r = weighted_r(rx, ry, w)
    rng = rng or np.random.default_rng(0)
    perm = np.empty(n_perm)
    n = x.size
    pool = np.concatenate([x, y])
    for i in range(n_perm):
        if pooled:
            p = rng.permutation(2 * n)
            perm[i] = weighted_r(_ranks(pool[p[:n]]), _ranks(pool[p[n:]]), w)
        else:
            perm[i] = weighted_r(rx, ry[rng.permutation(n)], w)
    if pooled:
        p = np.mean(perm > r) if r > 0 else np.mean(perm < r)
    else:
        p = (np.sum(np.abs(perm) >= abs(r)) + 1) / (n_perm + 1)
    return float(r), float(p), int(n)
EOF
sed -i 's/        after = np.flatnonzero(w\["pt_after"\] if False else (o\["pt_time"\] >= w\["mid_t"\]\[hi\[0\]\]))/        after = np.flatnonzero(o["pt_time"] >= w["mid_t"][hi[0]])/' apl.py; grep -n "after = np.flatnonzero" apl.py
```

```
299:                after = np.flatnonzero(~w[i + 1:])
418:        after = np.flatnonzero(o["pt_time"] >= w["mid_t"][hi[0]])
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python - <<'EOF'
import pickle, os, numpy as np, pandas as pd, apl
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
res=pickle.load(open(os.environ['TMPDIR']+'/res_c.pkl','rb'))
for key,outs in res.items():
    S=pd.DataFrame([apl.summarise(o) for o in outs])
    S['coal_from_on']=S.coalesce_t-30
    S['in_range_mean']=S.period_mean.between(9,16.5); S['in_range_med']=S.period_median.between(9,16.5)
    st=[apl.emax_stats(o['eigs'],o['npts']) for o in outs]
    S['a']=[x['a'] for x in st]; S['b']=[x['b'] for x in st]
    S['lin_period']=2*np.pi/S.b*0.01
    print(key, 'periods in 9-16.5 mean',S.in_range_mean.sum(),'median',S.in_range_med.sum(),
          'dom>50% hist',(S.prop_dom_hist>0.5).sum(),'all',(S.prop_dom_all>0.5).sum(),
          'coal<=period', (S.coal_from_on<=S.period_mean).sum(), (S.coal_from_on<=S.period_median).sum(), 'nan coal',S.coalesce_t.isna().sum(),
          'prop rec after>0.5',(S.prop_recurrent_after>0.5).sum(),
          'mean a',S.a.mean(),'mean b',S.b.mean(),'spiral', ((S.a<-1e-4)&(S.b>5e-4)).sum(), 'lin period mean', S.lin_period.mean())
    if key==('own','min80'): print(S.round(3).to_string())
EOF
```

```
('own', 'min80') periods in 9-16.5 mean 26 median 23 dom>50% hist 29 all 27 coal<=period 12 12 nan coal 0 prop rec after>0.5 30 mean a -0.0003621042933919175 mean b 0.00728588114961008 spiral 21 lin period mean 10.44963717481776
                file  prep  bout  d  n_peaks  prop_recurrent  n_points  period_mean  period_median  dom_n  prop_dom_hist  prop_dom_all  coalesce_t  prop_recurrent_after  coal_from_on  in_range_mean  in_range_med      a      b  lin_period
0    Jun0214da01.mat     1     1  7        4           0.842      7772       14.977         15.240   5137          0.898         0.785        42.5                 0.896          12.5           True          True -0.000  0.008       7.977
1    Jun0214da02.mat     1     2  7        2           0.823      7772       17.281         17.710   4957          0.973         0.775        50.5                 0.938          20.5          False         False -0.000  0.006       9.920
2    Jun0214da03.mat     1     3  8        4           0.817      7772       14.144         13.650   4449          0.805         0.700        52.5                 0.908          22.5           True          True  0.000  0.006       9.837
3   Jun0414Bda01.mat     2     1  4        2           0.722      7771       12.211         10.570   4886          0.918         0.870        42.5                 0.747          12.5           True          True -0.002  0.004      14.485
4   Jun0414Bda02.mat     2     2  5        2           0.788      7770       15.156         12.750   5127          0.907         0.837        44.5                 0.841          14.5           True          True -0.000  0.007       8.725
5   Jun0414Bda03.mat     2     3  5        1           0.907      7769       14.764         15.860   6508          0.993         0.923        38.5                 0.918           8.5           True          True -0.000  0.009       7.129
6    Jun0514da01.mat     3     1  8        2           0.695      7768       10.143         10.270   3881
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> apl.py <<'EOF'


# ---------------- comparisons between the programs of a preparation ----------------
PAIRS = [(0, 1), (0, 2), (1, 2)]


def point_sets(o, k=-1):
    """Two readings of the points compared between programs, as indices into the post-onset
    grid: 'recurrent', every checked point that recurs (Methods, Testing convergence to the
    same manifold); 'code', every point of the 5 s windows with at least 90% recurrent points
    (code Are_sequential_attractors_the_same.m, ixAdPts)."""
    dl = o["delay"][:, k]
    rec = o["pt_index"][~np.isnan(dl)]
    w = o["windows"][k]
    win = int(round(WIN_L / DT))
    ok = np.flatnonzero(w["dens"] >= 0.9)
    code = np.unique(np.concatenate([np.arange(w["start"][i], w["start"][i] + win + 1) for i in ok])) \
        if ok.size else np.array([], int)
    return {"recurrent": rec, "code": code}


def _hausdorff_with_control(XA, XB, ia, ib, coeffs, sdfA, sdfB, rng, n_shuffle):
    """Hausdorff distance between point sets ia (of A) and ib (of B), and its control: the
    same with the target program's neurons shuffled before projection (Methods; code)."""
    PA, PB = XA[ia], XB[ib]
    dAB = cKDTree(PB).query(PA)[0].max()
    dBA = cKDTree(PA).query(PB)[0].max()
    ctrl = np.empty(n_shuffle)
    for s in range(n_shuffle):
        cB = (sdfB[:, rng.permutation(sdfB.shape[1])] @ coeffs)[ib]
        cA = (sdfA[:, rng.permutation(sdfA.shape[1])] @ coeffs)[ia]
        ctrl[s] = max(cKDTree(cB).query(PA)[0].max(), cKDTree(cA).query(PB)[0].max())
    return float(max(dAB, dBA)), ctrl


def manifold_prep(args):
    """For the three programs of one preparation: Hausdorff distances with controls on the
    axes of program 1 and on common axes, under both point sets; the distances of Figure 3D;
    the similarity-matrix correlations of Figure 3F."""
    recs, sds, outs, seed, n_shuffle = args
    rng = np.random.default_rng(seed)
    progs = [Program(r, s, "min80") for r, s in zip(recs, sds)]
    sdfs = [p.sdf[p.ix_stim] for p in progs]
    res = {"prep": recs[0]["prep"]}
    # axes of program 1, smallest number of its PCs reaching 80% (code nPCsVAF80)
    k1 = n_pcs(progs[0].ev, 0.8, "min80")
    C1 = progs[0].coeffs[:, :k1]
    # common axes: PCA of the concatenated post-onset functions, PCs at most 80% (code CommonAxes)
    cat = np.vstack(sdfs)
    Cc, _, evc = pca(cat)
    kc = max(n_pcs(evc, 0.8, "le80"), 1)
    Cc = Cc[:, :kc]
    res["k_prog1"], res["k_common"] = k1, kc
    sets = [point_sets(o) for o in outs]
    for axes, C in (("prog1", C1), ("common", Cc)):
        X = [s @ C for s in sdfs]
        for ps in ("recurrent", "code"):
            for (i, j) in PAIRS:
                ia, ib = sets[i][ps], sets[j][ps]
                if ps == "code" and ia.size and ib.size:
                    start = max(ia.min(), ib.min())     # from the later program's first point
                    ia, ib = ia[ia >= start], ib[ib >= start]
                if ia.size == 0 or ib.size == 0:
                    res[(axes, ps, i, j)] = (np.nan, np.full(n_shuffle, np.nan))
                    continue
                res[(axes, ps, i, j)] = _hausdorff_with_control(X[i], X[j], ia, ib, C, sdfs[i],
                                                                sdfs[j], rng, n_shuffle)
    # Figure 3D (code Initial_Conditions.m), common axes
    X = [s @ Cc for s in sdfs]
    for (i, j) in PAIRS:
        ci = summarise(outs[i])["coalesce_t"] - STIM_ON
        cj = summarise(outs[j])["coalesce_t"] - STIM_ON
        A = X[i][:int(round(ci / DT))]
        B = X[j][:int(round(cj / DT))]
        onset = float(np.linalg.norm(X[i][0] - X[j][0]))
        trans = float(np.sqrt(((A[:, None, :] - B[None, ::5, :]) ** 2).sum(-1)).max()) if A.size and B.size else np.nan
        res[("ic", i, j)] = (onset, trans)
    # Figure 3F: similarity matrices
    S, E = [], []
    for s in sdfs:
        c = np.corrcoef(s.T)
        c[c < 0] = 0
        np.fill_diagonal(c, 0)
        S.append(c)
        tot = c.sum(0)
        E.append(np.outer(c.sum(1), tot) / tot.sum())
    res["sim"] = (S, E)
    return res


def run_manifold(recs, sds, outs, n_shuffle=100, seed=1, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    jobs = []
    for prep in sorted({r["prep"] for r in recs}):
        ix = sorted([i for i, r in enumerate(recs) if r["prep"] == prep], key=lambda i: recs[i]["bout"])
        jobs.append(([recs[i] for i in ix], [float(sds[i]) for i in ix], [outs[i] for i in ix],
                     seed * 1000 + prep, n_shuffle))
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        return list(ex.map(manifold_prep, jobs))
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import pickle, os, time, numpy as np, apl
res=pickle.load(open(os.environ['TMPDIR']+'/res_c.pkl','rb'))
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
t=time.time()
m=apl.manifold_prep(([recs[i] for i in range(3)], [sds['own'][i] for i in range(3)], res[('own','min80')][:3], 1, 10))
print('time 10 shuffles', time.time()-t)
for k,v in m.items():
    if isinstance(k,tuple) and k[0] in ('prog1','common'): print(k, round(v[0],2), np.nanmean(v[1]).round(2))
    elif isinstance(k,tuple): print(k,v)
EOF
```

```
time 10 shuffles 52.54562330245972
('prog1', 'recurrent', 0, 1) 14.29 22.96
('prog1', 'recurrent', 0, 2) 17.55 23.06
('prog1', 'recurrent', 1, 2) 16.62 22.61
('prog1', 'code', 0, 1) 12.05 23.09
('prog1', 'code', 0, 2) 11.01 23.3
('prog1', 'code', 1, 2) 12.82 22.53
('common', 'recurrent', 0, 1) 13.61 23.22
('common', 'recurrent', 0, 2) 18.36 24.79
('common', 'recurrent', 1, 2) 19.16 23.67
('common', 'code', 0, 1) 13.47 22.67
('common', 'code', 0, 2) 15.14 24.2
('common', 'code', 1, 2) 17.04 23.83
('ic', 0, 1) (7.738489595247617, 58.50222936824424)
('ic', 0, 2) (6.862782809639562, 61.93935605476304)
('ic', 1, 2) (11.170189305611375, 58.07416822033254)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python - <<'EOF'
import numpy as np, time
from scipy.spatial.distance import directed_hausdorff
from scipy.spatial import cKDTree
rng=np.random.default_rng(0)
A=np.cumsum(rng.normal(size=(7000,7)),0)*0.1; B=np.cumsum(rng.normal(size=(7000,7)),0)*0.1
t=time.time(); print(cKDTree(B).query(A)[0].max(), time.time()-t)
t=time.time(); print(directed_hausdorff(A,B)[0], time.time()-t)
EOF
```

```
21.63476568445399 0.0771474838256836
21.63476568445399 0.0018236637115478516
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('apl.py').read()
s=s.replace('''    PA, PB = XA[ia], XB[ib]
    dAB = cKDTree(PB).query(PA)[0].max()
    dBA = cKDTree(PA).query(PB)[0].max()
    ctrl = np.empty(n_shuffle)
    for s in range(n_shuffle):
        cB = (sdfB[:, rng.permutation(sdfB.shape[1])] @ coeffs)[ib]
        cA = (sdfA[:, rng.permutation(sdfA.shape[1])] @ coeffs)[ia]
        ctrl[s] = max(cKDTree(cB).query(PA)[0].max(), cKDTree(cA).query(PB)[0].max())''','''    PA, PB = XA[ia], XB[ib]
    dAB = directed_hausdorff(PA, PB)[0]
    dBA = directed_hausdorff(PB, PA)[0]
    ctrl = np.empty(n_shuffle)
    for s in range(n_shuffle):
        cB = (sdfB[:, rng.permutation(sdfB.shape[1])] @ coeffs)[ib]
        cA = (sdfA[:, rng.permutation(sdfA.shape[1])] @ coeffs)[ia]
        ctrl[s] = max(directed_hausdorff(PA, cB)[0], directed_hausdorff(PB, cA)[0])''')
s=s.replace("from scipy.spatial.distance import pdist","from scipy.spatial.distance import directed_hausdorff, pdist")
s=s.replace('''def hausdorff_dirs(A, B):
    """Directed max-min distances (A to B, B to A)."""
    da = cKDTree(B).query(A)[0]
    db = cKDTree(A).query(B)[0]
    return da.max(), db.max()


''','')
s=s.replace("from scipy.spatial import cKDTree\n","")
open('apl.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import pickle, os, time, numpy as np, apl
res=pickle.load(open(os.environ['TMPDIR']+'/res_c.pkl','rb'))
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
t=time.time()
m=apl.manifold_prep(([recs[i] for i in range(3)], [sds['own'][i] for i in range(3)], res[('own','min80')][:3], 1, 100))
print('time 100 shuffles', time.time()-t)
for k,v in m.items():
    if isinstance(k,tuple) and k[0] in ('prog1','common'): print(k, round(v[0],2), np.nanmean(v[1]).round(2))
EOF
```

```
time 100 shuffles 11.719584226608276
('prog1', 'recurrent', 0, 1) 14.29 22.83
('prog1', 'recurrent', 0, 2) 17.55 23.35
('prog1', 'recurrent', 1, 2) 16.62 22.68
('prog1', 'code', 0, 1) 12.05 22.89
('prog1', 'code', 0, 2) 11.01 23.28
('prog1', 'code', 1, 2) 12.82 22.3
('common', 'recurrent', 0, 1) 13.61 23.01
('common', 'recurrent', 0, 2) 18.36 24.39
('common', 'recurrent', 1, 2) 19.16 23.9
('common', 'code', 0, 1) 13.47 23.21
('common', 'code', 0, 2) 15.14 24.28
('common', 'code', 1, 2) 17.04 23.57
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import pickle, os, time, numpy as np, apl
res=pickle.load(open(os.environ['TMPDIR']+'/res_c.pkl','rb'))
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
man={}
for key in res:
    t=time.time(); man[key]=apl.run_manifold(recs, sds[key[0]], res[key]); print(key, time.time()-t, flush=True)
pickle.dump(man, open(os.environ['TMPDIR']+'/man.pkl','wb'))
for key,M in man.items():
  for axes in ('prog1','common'):
    for ps in ('recurrent','code'):
      n=0; fails=[]
      for m in M:
        for (i,j) in apl.PAIRS:
          h,c=m[(axes,ps,i,j)]
          if h< np.mean(c): n+=1
          else: fails.append((m['prep'],i+1,j+1))
      print(key,axes,ps,n,fails)
EOF
```

```
('own', 'min80') 49.82051396369934
('own', 'le80') 51.74152898788452
('pooled', 'min80') 51.399452924728394
('pooled', 'le80') 51.24553561210632
('own', 'min80') prog1 recurrent 29 [(4, 1, 2)]
('own', 'min80') prog1 code 28 [(4, 1, 2), (4, 1, 3)]
('own', 'min80') common recurrent 30 []
('own', 'min80') common code 28 [(4, 1, 2), (4, 1, 3)]
('own', 'le80') prog1 recurrent 29 [(4, 1, 2)]
('own', 'le80') prog1 code 28 [(4, 1, 2), (4, 1, 3)]
('own', 'le80') common recurrent 30 []
('own', 'le80') common code 27 [(4, 1, 2), (4, 1, 3), (8, 2, 3)]
('pooled', 'min80') prog1 recurrent 29 [(4, 1, 2)]
('pooled', 'min80') prog1 code 28 [(4, 1, 2), (4, 1, 3)]
('pooled', 'min80') common recurrent 30 []
('pooled', 'min80') common code 28 [(4, 1, 2), (4, 1, 3)]
('pooled', 'le80') prog1 recurrent 29 [(4, 1, 2)]
('pooled', 'le80') prog1 code 28 [(4, 1, 2), (4, 1, 3)]
('pooled', 'le80') common recurrent 30 []
('pooled', 'le80') common code 28 [(4, 1, 2), (4, 1, 3)]
```

**Agent calls Bash**

```bash
cat >> apl.py <<'EOF'


# ---------------- eigenvalues of the local models ----------------
def eig_dimensions(eigs):
    """Code Check_All_Real_Eigenvalues.m: per point, the real part of each unique eigenvalue
    dimension (a conjugate pair counted once), in the order of the sorted eigenvalues; the
    proportion of points with a complex eigenvalue among the top one or two."""
    is_real = np.abs(eigs.imag) < np.finfo(float).eps * np.abs(eigs.real)
    n, d = eigs.shape
    max_dom = int(np.max((~is_real).sum(1)) / 2 + d % 2)
    U = np.zeros((n, max_dom))
    for p in range(n):
        c = 0
        for k in range(max_dom):
            if c >= d:
                U[p, k] = np.nan
                continue
            U[p, k] = eigs[p, c].real
            c += 1 if is_real[p, c] else 2
    return {"mean_unique": np.nanmean(U, 0), "p_complex1": float(np.mean(~is_real[:, 0])),
            "p_complex12": float(np.mean(~is_real[:, 0] | (~is_real[:, 1] if d > 1 else False)))}


# ---------------- participation ----------------
def participation(coeffs, ev, d):
    """Methods, Single neuron participation: sum over the d principal axes of the absolute
    eigenvalue-weighted weights, and the same normalised to the program's maximum."""
    raw = np.abs(coeffs[:, :d] * ev[:d][None, :]).sum(1)
    return raw, raw / raw.max()


def iterate_outliers(x):
    """Code iterateoutliers.m: fit a Gaussian, drop the point furthest from the mean (all ties),
    refit, and stop when the log likelihood falls; returns (mu, sd) of the last fit before the
    fall. MATLAB fitdist uses the unbiased SD."""
    from scipy.stats import norm
    keep = np.ones(x.size, bool)
    mu, sd = x.mean(), x.std(ddof=1)
    ll = norm.logpdf(x, mu, sd).sum()
    while keep.sum() > 3:
        dist = np.abs(x - mu)
        dist[~keep] = -1
        keep2 = keep & (dist < dist.max())
        y = x[keep2]
        mu2, sd2 = y.mean(), y.std(ddof=1)
        ll2 = norm.logpdf(y, mu2, sd2).sum()
        if ll2 < ll:
            break
        keep, mu, sd, ll = keep2, mu2, sd2, ll2
    return float(mu), float(sd), int((~keep).sum())


def hellinger(p, q, bins=np.arange(0, 1.0001, 0.05)):
    """Hellinger distance between histograms of normalised participation on MATLAB hist
    centres 0:0.05:1 (code RobustnessOfAttractor_to_single_neuron_variability.m)."""
    edges = np.concatenate([[-np.inf], (bins[:-1] + bins[1:]) / 2, [np.inf]])
    a = np.histogram(p, edges)[0].astype(float)
    b = np.histogram(q, edges)[0].astype(float)
    a, b = a / a.sum(), b / b.sum()
    return float(np.sqrt(np.sum((np.sqrt(a) - np.sqrt(b)) ** 2)) / np.sqrt(2))
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import pickle, os, time, numpy as np, pandas as pd, apl
from scipy import stats
res=pickle.load(open(os.environ['TMPDIR']+'/res_c.pkl','rb'))
man=pickle.load(open(os.environ['TMPDIR']+'/man.pkl','rb'))
key=('own','min80'); outs=res[key]; M=man[key]
# fig3f
for ctl in ['first','larger']:
  for meth in ['spearman','pearson']:
    n=0; fails=[]
    for m in M:
        S,E=m['sim']
        f=(lambda a,b: stats.spearmanr(a,b)[0]) if meth=='spearman' else (lambda a,b: np.corrcoef(a,b)[0,1])
        cs=[f(S[i].ravel(),E[i].ravel()) for i in range(3)]
        for (i,j) in apl.PAIRS:
            dat=f(S[i].ravel(),S[j].ravel()); c=cs[i] if ctl=='first' else max(cs[i],cs[j])
            if dat>c: n+=1
            else: fails.append((m['prep'],i+1,j+1,round(dat,3),round(c,3)))
    print('3f',ctl,meth,n,fails)
# fig3d
rows=[]
for m in M:
  for (i,j) in apl.PAIRS:
    on,tr=m[('ic',i,j)]; co=m[('common','code',i,j)][0]; cr=m[('common','recurrent',i,j)][0]
    rows.append((m['prep'],i+1,j+1,on,tr,co,cr))
T=pd.DataFrame(rows,columns=['prep','i','j','onset','transient','coal_code','coal_rec'])
print('3d transient > both (code)',((T.transient>T.onset)&(T.transient>T.coal_code)).sum(), T[['onset','transient','coal_code','coal_rec']].median().round(2).to_dict())
# perturbations
S=pd.DataFrame([apl.summarise(o) for o in outs])
allv=[]
for o,s in zip(outs,S.itertuples()):
    for per in ('period_mean','period_median'):
        pass
    dv=apl.divergences(o, s.period_mean)
    for d in dv: d.update(file=o['file']); allv.append(d)
V=pd.DataFrame(allv); print(V.round(3).to_string())
Vk=V[~V.near_end]; print('kept',len(Vk),'returned',Vk.returned.sum(), 'same end>0.2',(Vk.p_after_end>0.2).sum(),'same point>0.2',(Vk.p_after_point>0.2).sum())
EOF
```

```
3f first spearman 29 [(4, 1, 3, np.float64(0.597), np.float64(0.622))]
3f first pearson 30 []
3f larger spearman 27 [(4, 1, 3, np.float64(0.597), np.float64(0.622)), (7, 1, 3, np.float64(0.65), np.float64(0.735)), (7, 2, 3, np.float64(0.708), np.float64(0.735))]
3f larger pearson 28 [(7, 1, 3, np.float64(0.685), np.float64(0.779)), (7, 2, 3, np.float64(0.751), np.float64(0.779))]
3d transient > both (code) 30 {'onset': 9.31, 'transient': 45.44, 'coal_code': 14.51, 'coal_rec': 13.88}
    start_win  end_win  point_win  t_point  min_dens  returned  near_end              file  t_return  n_before  p_after_end  p_after_point
0          68       72         72    109.5     0.128     False      True   Jun0214da01.mat       NaN       NaN          NaN            NaN
1          70       72         72    109.5     0.492     False      True   Jun0214da02.mat       NaN       NaN          NaN            NaN
2          21       34         29     66.5     0.000      True     False  Jun0414Bda01.mat      70.0     483.0        0.002          0.830
3          57       69         62     99.5     0.000      True      True  Jun0414Bda01.mat     105.0     500.0        1.000          1.000
4          12       20         16     53.5     0.322      True     False  Jun0414Bda02.mat      56.0     463.0        1.000          1.000
5          69       72         72    109.5     0.134     False      True  Jun0414Bda02.mat       NaN       NaN          NaN            NaN
6          68       72         72    109.5     0.290     False      True  Jun0414Bda03.mat       NaN       NaN          NaN            NaN
7          24       31         27     64.5     0.354      True     False   Jun0514da01.mat      67.0     470.0        0.889          0.889
8          55       63         59     96.5     0.096      True     False   Jun0514da02.mat      99.0     500.0        0.778          0.778
9          68       72         72    109.5     0.000     False      True   Jun0514da03.mat       NaN       NaN          Na
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import pickle, os, time, numpy as np, pandas as pd, apl
from scipy import stats
res=pickle.load(open(os.environ['TMPDIR']+'/res_c.pkl','rb'))
key=('own','min80'); outs=res[key]
S=pd.DataFrame([apl.summarise(o) for o in outs])
rows=[]
t=time.time()
for o,s in zip(outs,S.itertuples()):
    st=apl.emax_stats(o['eigs'],o['npts']); ed=apl.eig_dimensions(st['eigs'])
    mu=ed['mean_unique']
    w=o['windows'][-1]
    i0=np.flatnonzero(w['dens']>0.9)[0]; i1=np.flatnonzero(w['dens']>0.9)[-1]
    sl=slice(i0,i1+1)
    wt=1/w['sddelay']; wt[~np.isfinite(wt)]=0; wt=wt*w['dens']
    r,p,n=apl.weighted_spearman(w['mid_t'][sl], w['mdelay'][sl], wt[sl], 10000, np.random.default_rng(s.Index))
    rows.append(dict(file=o['file'],a=st['a'],b=st['b'],allneg=bool(np.all(mu<0)),npos=int(np.sum(mu>0)),pos_first=bool(mu[0]>0),pc12=ed['p_complex12'],pc1=ed['p_complex1'],rho=r,p=p,nwin=n))
print(time.time()-t)
R=pd.DataFrame(rows); print(R.round(4).to_string())
print('allneg',R.allneg.sum(),'one pos not first',((R.npos==1)&~R.pos_first).sum(),'pc12>0.5',(R.pc12>0.5).sum())
print('rho>0 p<.01',((R.rho>0)&(R.p<0.01)).sum(),'rho<0',((R.rho<0)&(R.p<0.01)).sum(),'ns',(R.p>=0.01).sum(),'nwin',R.nwin.min(),R.nwin.max())
print(stats.pearsonr(R.rho,R.a))
EOF
```

```
5.8380045890808105
                file       a       b  allneg  npos  pos_first    pc12     pc1     rho       p  nwin
0    Jun0214da01.mat -0.0003  0.0079    True     0      False  1.0000  1.0000  0.4389  0.0002    63
1    Jun0214da02.mat -0.0002  0.0063    True     0      False  1.0000  0.9407  0.5869  0.0001    57
2    Jun0214da03.mat  0.0003  0.0064   False     3       True  1.0000  1.0000  0.1638  0.3210    56
3   Jun0414Bda01.mat -0.0020  0.0043   False     1      False  0.8715  0.6474  0.6202  0.0001    66
4   Jun0414Bda02.mat -0.0002  0.0072   False     1      False  1.0000  0.9427  0.4103  0.0262    62
5   Jun0414Bda03.mat -0.0003  0.0088   False     2      False  0.9877  0.9644  0.6447  0.0001    67
6    Jun0514da01.mat -0.0003  0.0074    True     0      False  1.0000  1.0000 -0.5273  0.0013    50
7    Jun0514da02.mat -0.0000  0.0074   False     1      False  1.0000  0.9923 -0.6177  0.0001    60
8    Jun0514da03.mat -0.0001  0.0115   False     1      False  1.0000  0.9630  0.7709  0.0001    57
9    Jun0914da01.mat  0.0005  0.0094   False     2       True  0.9655  0.9476 -0.4079  0.0312    31
10   Jun0914da02.mat -0.0011  0.0057   False     1      False  0.9720  0.7934  0.9597  0.0001    60
11   Jun0914da03.mat  0.0002  0.0062   False     3       True  0.9707  0.8395  0.2681  0.1843    37
12   Jun1114da01.mat -0.0006  0.0120    True     0      False  0.9963  0.9112  0.4109  0.0015    69
13   Jun1114da02.mat -0.0008  0.0070    True     0      False  0.9567  0.8139 -0.0359  0.7909    66
14   Jun1114da03.mat -0.0005  0.0139    True     0      False  0.9939  0.9251 -0.7906  0.0001    64
15   May2214da01.mat -0.0005  0.0119    True     0      False  1.0000  0.9814  0.9202  0.0001    72
16   May2214da02.mat -0.0010  0.0093   False     1      False  1.0000  0.9489  0.8558  0.0001    69
17   May2214da03.mat  0.0001  0.0106   False     1       True  1.0000  0.9963  0.8917  0.0001    70
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import pickle, os, time, numpy as np, pandas as pd, apl
from scipy import stats
import statsmodels.api as sm
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
man=pickle.load(open(os.environ['TMPDIR']+'/man.pkl','rb'))
t=time.time()
progs=[apl.Program(r, s, 'min80') for r,s in zip(recs, sds['own'])]
print('progs',time.time()-t)
part={}
for reading in ['own','common']:
  for prep in range(1,11):
    ix=[i for i,r in enumerate(recs) if r['prep']==prep]; ix=sorted(ix,key=lambda i: recs[i]['bout'])
    if reading=='common':
        cat=np.vstack([progs[i].sdf[progs[i].ix_stim] for i in ix]); _,_,evc=apl.pca(cat); d=[apl.n_pcs(evc,0.8,'le80')]*3
    else: d=[apl.n_pcs(progs[i].ev,0.8,'min80') for i in ix]
    P=np.array([apl.participation(progs[i].coeffs, progs[i].ev, dd)[1] for i,dd in zip(ix,d)])
    part[(reading,prep)]=P
for reading in ['own','common']:
  sk=[];half=[]
  for prep in range(1,11):
    for P in part[(reading,prep)]: sk.append(stats.skew(P)); half.append(np.mean(P>0.5))
  sk=np.array(sk); half=np.array(half)
  print(reading,'7a skew>0',(sk>0).sum(),'frac>0.5 <0.5', (half<0.5).sum(), sk.min().round(2), half.max().round(3))
  # 7f
  for pool in ['all','consec']:
    nv=[]
    for prep in range(1,11):
      P=part[(reading,prep)]; dP=np.column_stack([P[0]-P[1],P[1]-P[2],P[0]-P[2]])
      data=dP.ravel(order='F') if pool=='all' else dP[:,:2].ravel(order='F')
      mu,sd,nout=apl.iterate_outliers(data)
      thr=max(abs(mu-3*sd),abs(mu+3*sd)); mx=np.abs(dP[:,:2]).max(1)
      nv.append(int((mx>=thr).sum()))
    print(reading,pool,'strongly variable per prep',nv)
  # halving
  for rd in ['top1','top10']:
    preps=0
    for prep in range(1,11):
      P=part[(reading,prep)]; hit=False
      for a in range(3):
        sel=[np.argmax(P[a])] if rd=='top1' else np.argsort(P[a])[::-1][:int(np.ceil(0.1*P.shape[1]))]
        for b in range(3):
          if b!=a and np.any(P[b][sel] < 0.5*P[a][sel]): hit=True
      preps+=hit
    print(reading,rd,'preps with halving',preps)
  # 7s1
  for rate in ['offset','onset']:
    r2=[];dr2=[];dr2c=[]
    for prep in range(1,11):
      ix=sorted([i for i,r in enumerate(recs) if r['prep']==prep],key=lambda i: recs[i]['bout'])
      P=part[(reading,prep)]
      t0=32.5 if rate=='offset' else 30
      rates=np.array([[np.sum(tr>=t0)/(progs[i].t_end-t0) for tr in progs[i].trains] for i in ix])
      for a in range(3): r2.append(np.corrcoef(P[a],rates[a])[0,1]**2)
      dR=np.column_stack([rates[0]-rates[1],rates[0]-rates[2],rates[1]-rates[2]])
      dPm=np.column_stack([P[0]-P[1],P[0]-P[2],P[1]-P[2]]); dPc=np.column_stack([P[0]-P[1],P[1]-P[2],P[0]-P[2]])
      for c in range(3): dr2.append(np.corrcoef(dR[:,c],dPm[:,c])[0,1]**2); dr2c.append(np.corrcoef(dR[:,c],dPc[:,c])[0,1]**2)
    print(reading,rate,'7s1 mean R2',np.mean(r2).round(3),'change matched',np.mean(dr2).round(3),'code pairing',np.mean(dr2c).round(3))
EOF
```

```
progs 2.663236379623413
own 7a skew>0 30 frac>0.5 <0.5 30 0.5 0.394
own all strongly variable per prep [11, 14, 25, 17, 22, 6, 16, 20, 4, 18]
own consec strongly variable per prep [8, 16, 32, 29, 24, 8, 22, 6, 10, 19]
own top1 preps with halving 6
own top10 preps with halving 9
own offset 7s1 mean R2 0.491 change matched 0.239 code pairing 0.205
own onset 7s1 mean R2 0.514 change matched 0.265 code pairing 0.221
common 7a skew>0 30 frac>0.5 <0.5 30 0.49 0.404
common all strongly variable per prep [8, 18, 35, 18, 24, 6, 20, 17, 4, 18]
common consec strongly variable per prep [7, 21, 41, 28, 37, 8, 23, 7, 10, 13]
common top1 preps with halving 6
common top10 preps with halving 9
common offset 7s1 mean R2 0.499 change matched 0.244 code pairing 0.209
common onset 7s1 mean R2 0.522 change matched 0.27 code pairing 0.226
```

**Agent calls Bash**

```bash
cat >> apl.py <<'EOF'


# ---------------- P10 nerve ----------------
def p10_locking(neuron, p10, start=33.0, delays=np.arange(0, 0.0255, 0.001), jitter=0.002):
    """Code P10_ID_motorneurons.m: the proportion of a neuron's spikes after ``start`` followed
    by a P10 spike at each delay, within +/- jitter; returns the maximum over delays."""
    ts = neuron[neuron > start]
    if ts.size == 0:
        return np.nan, 0
    best = 0.0
    for d in delays:
        lo = np.searchsorted(p10, ts + d - jitter - 1e-12, "left")
        hi = np.searchsorted(p10, ts + d + jitter + 1e-12, "right")
        best = max(best, float(np.mean(hi > lo)))
    return best, int(ts.size)


def poisson_glm(X, y, iters=50, tol=1e-8):
    """Poisson GLM with log link by iteratively reweighted least squares (as MATLAB glmfit);
    X includes the intercept column. y may be non-integer, as the code fits a rate."""
    beta = np.zeros(X.shape[1])
    beta[0] = np.log(max(y.mean(), 1e-6))
    dev_old = np.inf
    for _ in range(iters):
        eta = np.clip(X @ beta, -30, 30)
        mu = np.exp(eta)
        z = eta + (y - mu) / mu
        W = mu
        XtW = X.T * W
        try:
            beta_new = np.linalg.solve(XtW @ X + 1e-10 * np.eye(X.shape[1]), XtW @ z)
        except np.linalg.LinAlgError:
            break
        beta = beta_new
        mu = np.exp(np.clip(X @ beta, -30, 30))
        with np.errstate(divide="ignore", invalid="ignore"):
            dev = 2 * np.sum(np.where(y > 0, y * np.log(y / mu), 0) - (y - mu))
        if abs(dev_old - dev) < tol * (abs(dev) + 0.1):
            break
        dev_old = dev
    return beta


def lagged(pcs, rows, n_hist):
    """Design matrix: intercept and the PCs at lags 1..n_hist time steps before each row."""
    cols = [np.ones(rows.size)]
    for h in range(1, n_hist + 1):
        cols.append(pcs[rows - h])
    return np.column_stack([cols[0]] + [c for c in cols[1:]]) if n_hist else cols[0][:, None]


def decode_p10(pcs, p10_rate, stimbins, hist_steps, train_s=40.0, test_s=10.0, step_s=1.0,
               start=33.0, train_frac=None):
    """Fit the P10 rate from the lagged PCs in a training window and forecast the next
    ``test_s`` s, windows stepped by ``step_s`` from ``start`` (Methods, Decoding motor output).
    With ``train_frac`` the training window is that fraction of the series after ``start``
    (the code's reading). Returns per-window forecast R, MAE, training R and MAE."""
    t_last = stimbins[-1]
    if train_frac is not None:
        train_s = round((t_last - start) * train_frac)
    out = []
    s0 = start
    n_test = int(round(test_s / DT))
    while True:
        i0 = int(np.searchsorted(stimbins, s0 - 1e-9))
        i1 = int(np.searchsorted(stimbins, s0 + train_s - 1e-9))
        if i1 + n_test > stimbins.size:
            break
        rows = np.arange(max(i0, hist_steps), i1)
        X = lagged(pcs, rows, hist_steps)
        y = p10_rate[rows]
        b = poisson_glm(X, y)
        fit = np.exp(np.clip(X @ b, -30, 30))
        rf = np.arange(i1, i1 + n_test)
        Xf = lagged(pcs, rf, hist_steps)
        fc = np.exp(np.clip(Xf @ b, -30, 30))
        yf = p10_rate[rf]
        with np.errstate(invalid="ignore"):
            out.append({"t": s0, "R": np.corrcoef(yf, fc)[0, 1], "MAE": np.median(np.abs(yf - fc)),
                        "R_train": np.corrcoef(y, fit)[0, 1], "MAE_train": np.median(np.abs(y - fit))})
        s0 += step_s
    return out
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import os, time, numpy as np, pandas as pd, apl
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
# motorneuron test
t=time.time(); mx=[]
for q in D['p10']:
    r=next(r for r in recs if r['prep']==q['prep'] and r['bout']==q['bout'])
    for i,tr in enumerate(apl.neuron_trains(r)):
        v,n=apl.p10_locking(tr,q['t']); mx.append((q['prep'],q['bout'],i+1,v,n))
M=pd.DataFrame(mx,columns=['prep','bout','neuron','maxP','n']); print('locking',time.time()-t, M.maxP.max(), (M.maxP>=0.9).sum()); print(M.sort_values('maxP').tail(5))
# decoding test one program
q=D['p10'][0]; i=next(i for i,r in enumerate(recs) if r['prep']==q['prep'] and r['bout']==q['bout'])
P=apl.Program(recs[i], sds['own'][i], 'min80')
rate=apl.sdf_matrix([q['t']], sds['own'][i], P.t_end)[P.ix_stim,0]
for hs in [5,10,20]:
    t=time.time(); o=apl.decode_p10(P.pcs, rate, P.stimbins, hs); O=pd.DataFrame(o)
    print(hs, len(O), time.time()-t, O.R.mean().round(3), O.R.std().round(3), O.MAE.mean().round(3), O.R_train.mean().round(3))
EOF
```

```
locking 0.6884777545928955 0.5217391304347826 0
     prep  bout  neuron      maxP   n
401     4     1      87  0.461538  26
183     2     2      79  0.476190  21
431     4     1     117  0.500000   2
406     4     1      92  0.521739  46
179     2     2      75       NaN   0
5 40 0.7805776596069336 0.362 0.519 8.401 0.937
10 40 1.6083016395568848 0.359 0.522 8.664 0.94
20 40 3.996242046356201 0.351 0.521 8.905 0.941
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('apl.py').read()
s=s.replace('''def poisson_glm(X, y, iters=50, tol=1e-8):''','''def poisson_glm(X, y, iters=50, tol=1e-8, beta=None):''')
s=s.replace('''    beta = np.zeros(X.shape[1])
    beta[0] = np.log(max(y.mean(), 1e-6))
    dev_old = np.inf''','''    if beta is None:
        beta = np.zeros(X.shape[1])
        beta[0] = np.log(max(y.mean(), 1e-6))
    else:
        beta = beta.copy()
    dev_old = np.inf''')
s=s.replace('''    out = []
    s0 = start
    n_test = int(round(test_s / DT))''','''    out = []
    s0 = start
    n_test = int(round(test_s / DT))
    b = None''')
s=s.replace('''        b = poisson_glm(X, y)
        fit''','''        b = poisson_glm(X, y, beta=b)     # warm start from the previous window
        fit''')
open('apl.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import os, time, numpy as np, pandas as pd, apl
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
q=D['p10'][0]; i=next(i for i,r in enumerate(recs) if r['prep']==q['prep'] and r['bout']==q['bout'])
P=apl.Program(recs[i], sds['own'][i], 'min80')
rate=apl.sdf_matrix([q['t']], sds['own'][i], P.t_end)[P.ix_stim,0]
d90=apl.n_pcs(P.ev,0.9,'min80'); print('d80',P.d,'d90',d90)
for hs in [5,20]:
  for pcs in [P.pcs, P.proj[:,:d90]]:
    t=time.time(); o=apl.decode_p10(pcs, rate, P.stimbins, hs); O=pd.DataFrame(o)
    print(hs, pcs.shape[1], len(O), round(time.time()-t,1), O.R.mean().round(3), O.MAE.mean().round(3))
EOF
```

```
d80 4 d90 8
5 4 40 0.9 0.362 8.399
5 8 40 1.6 0.488 7.584
20 4 40 3.9 0.351 8.903
20 8 40 12.4 0.191 581937613158.413
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import time, numpy as np, apl
rng=np.random.default_rng(0)
X=np.column_stack([np.ones(4000), rng.normal(size=(4000,80))*0.3]); y=np.exp(X@rng.normal(size=81)*0.3)
import cProfile, pstats
t=time.time()
for k in range(10): b=apl.poisson_glm(X,y)
print('per fit',(time.time()-t)/10)
cnt=[0]
orig=np.linalg.solve
def s(*a,**k): cnt[0]+=1; return orig(*a,**k)
np.linalg.solve=s; apl.poisson_glm(X,y); print('iters',cnt[0])
EOF
```

```
per fit 0.014711499214172363
iters 6
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import os, time, numpy as np, apl
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
q=D['p10'][0]; i=next(i for i,r in enumerate(recs) if r['prep']==q['prep'] and r['bout']==q['bout'])
P=apl.Program(recs[i], sds['own'][i], 'min80')
rate=apl.sdf_matrix([q['t']], sds['own'][i], P.t_end)[P.ix_stim,0]
print(rate.min(), rate.max(), rate.mean())
cnt=[0]; orig=np.linalg.solve
def s(*a,**k): cnt[0]+=1; return orig(*a,**k)
np.linalg.solve=s
t=time.time(); o=apl.decode_p10(P.pcs, rate, P.stimbins, 20); print(time.time()-t, cnt[0]/len(o))
EOF
```

```
0.0008083402886064624 655.6293818301167 59.30946035164362
3.95298171043396 48.9
```

**Agent calls Bash**

```bash
sed -i 's/def poisson_glm(X, y, iters=50, tol=1e-8, beta=None):/def poisson_glm(X, y, iters=100, tol=1e-6, beta=None):/' apl.py && python - <<'EOF'
s=open('apl.py').read()
old=s[s.index("        beta = beta_new\n        mu = np.exp"):s.index("    return beta\n\n\ndef lagged")]
new='''        done = np.all(np.abs(beta_new - beta) <= tol * np.maximum(np.sqrt(np.finfo(float).eps), np.abs(beta)))
        beta = beta_new
        if done:          # glmfit's convergence rule on the coefficients
            break
'''
s=s.replace(old,new); s=s.replace("    dev_old = np.inf\n    for _ in range(iters):","    for _ in range(iters):")
open('apl.py','w').write(s)
EOF
sed -n '/def poisson_glm/,/return beta/p' apl.py; cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import os, time, numpy as np, apl, pandas as pd
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
q=D['p10'][0]; i=next(i for i,r in enumerate(recs) if r['prep']==q['prep'] and r['bout']==q['bout'])
P=apl.Program(recs[i], sds['own'][i], 'min80')
rate=apl.sdf_matrix([q['t']], sds['own'][i], P.t_end)[P.ix_stim,0]
cnt=[0]; orig=np.linalg.solve
def s(*a,**k): cnt[0]+=1; return orig(*a,**k)
np.linalg.solve=s
for hs in [5,20]:
  cnt[0]=0; t=time.time(); o=apl.decode_p10(P.pcs, rate, P.stimbins, hs); O=pd.DataFrame(o); print(hs,time.time()-t, cnt[0]/len(o), O.R.mean().round(3), O.MAE.mean().round(3))
EOF
```

```
def poisson_glm(X, y, iters=100, tol=1e-6, beta=None):
    """Poisson GLM with log link by iteratively reweighted least squares (as MATLAB glmfit);
    X includes the intercept column. y may be non-integer, as the code fits a rate."""
    if beta is None:
        beta = np.zeros(X.shape[1])
        beta[0] = np.log(max(y.mean(), 1e-6))
    else:
        beta = beta.copy()
    for _ in range(iters):
        eta = np.clip(X @ beta, -30, 30)
        mu = np.exp(eta)
        z = eta + (y - mu) / mu
        W = mu
        XtW = X.T * W
        try:
            beta_new = np.linalg.solve(XtW @ X + 1e-10 * np.eye(X.shape[1]), XtW @ z)
        except np.linalg.LinAlgError:
            break
        done = np.all(np.abs(beta_new - beta) <= tol * np.maximum(np.sqrt(np.finfo(float).eps), np.abs(beta)))
        beta = beta_new
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('apl.py').read()
s=s.replace("def poisson_glm(X, y, iters=100, tol=1e-6, beta=None):","def poisson_glm(X, y, iters=25, tol=1e-6, beta=None):")
s=s.replace('''    X includes the intercept column. y may be non-integer, as the code fits a rate."""''','''    X includes the intercept column. y may be non-integer, as the code fits a rate. Stops when
    the deviance changes by less than ``tol`` relatively, or after ``iters`` iterations (a
    standard choice; the forecasts agree to three decimals with 100 iterations)."""''')
s=s.replace('''        done = np.all(np.abs(beta_new - beta) <= tol * np.maximum(np.sqrt(np.finfo(float).eps), np.abs(beta)))
        beta = beta_new
        if done:          # glmfit's convergence rule on the coefficients
            break
''','''        beta = beta_new
        mu = np.exp(np.clip(X @ beta, -30, 30))
        with np.errstate(divide="ignore", invalid="ignore"):
            dev = 2 * np.sum(np.where(y > 0, y * np.log(y / mu), 0) - (y - mu))
        if abs(dev_old - dev) < tol * (abs(dev) + 0.1):
            break
        dev_old = dev
''')
s=s.replace("        beta = beta.copy()\n    for _ in range(iters):","        beta = beta.copy()\n    dev_old = np.inf\n    for _ in range(iters):")
open('apl.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import os, time, numpy as np, apl, pandas as pd
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
q=D['p10'][0]; i=next(i for i,r in enumerate(recs) if r['prep']==q['prep'] and r['bout']==q['bout'])
P=apl.Program(recs[i], sds['own'][i], 'min80')
rate=apl.sdf_matrix([q['t']], sds['own'][i], P.t_end)[P.ix_stim,0]
for hs in [5,20]:
  t=time.time(); o=apl.decode_p10(P.pcs, rate, P.stimbins, hs); O=pd.DataFrame(o); print(hs,time.time()-t, O.R.mean().round(3), O.MAE.mean().round(3))
EOF
date -u
```

```
5 0.18727445602416992 0.362 8.4
20 1.7411892414093018 0.351 8.899
Sun Nov  8 12:27:28 UTC 2026
```

**Agent calls Bash**

```bash
cat >> apl.py <<'EOF'


HISTORIES_METHODS = list(range(5, 21))      # 50..200 ms in 10 ms steps (Methods)
HISTORIES_CODE = [5, 10, 15, 20, 25]         # 50..250 ms (code DecodeP10_statespace.m)


def decode_program(args):
    """Decoding of one P10 program under one windowing and dimension count; the history with
    the smallest mean forecast MAE is kept (Methods: "the smallest median absolute error";
    code Best_P10_StateSpace_GLMmodels.m takes the mean over windows of the per-window
    median absolute error)."""
    rec, p10_t, sd, frac, windowing, hists = args
    P = Program(rec, sd, "min80")
    d = n_pcs(P.ev, frac, "min80")
    pcs = P.proj[:, :d]
    rate = sdf_matrix([p10_t], sd, P.t_end)[P.ix_stim, 0]
    res = {}
    for h in hists:
        if windowing == "methods":
            o = decode_p10(pcs, rate, P.stimbins, h)
        else:
            o = decode_p10(pcs, rate, P.stimbins, h, step_s=0.2, train_frac=0.5)
        res[h] = o
    best = min(res, key=lambda h: np.nanmean([w["MAE"] for w in res[h]]))
    return {"file": rec["file"], "prep": rec["prep"], "bout": rec["bout"], "d": d, "best": best,
            "windows": res[best], "by_history": {h: (np.nanmean([w["R"] for w in v]),
                                                      np.nanmean([w["MAE"] for w in v]))
                                                  for h, v in res.items()}}


def run_decoding(jobs, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        return list(ex.map(decode_program, jobs))
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import os, time, numpy as np, apl, pandas as pd, pickle
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
jobs={}
for frac in (0.8,0.9):
  for win,h in (('methods',apl.HISTORIES_METHODS),('code',apl.HISTORIES_CODE)):
    J=[]
    for q in D['p10']:
        i=next(i for i,r in enumerate(recs) if r['prep']==q['prep'] and r['bout']==q['bout'])
        J.append((recs[i], q['t'], float(sds['own'][i]), frac, win, h))
    jobs[(frac,win)]=J
dec={}
for k,J in jobs.items():
    t=time.time(); dec[k]=apl.run_decoding(J); print(k, time.time()-t, flush=True)
    for o in dec[k]:
        R=np.array([w['R'] for w in o['windows']]); print('  ',o['file'],o['d'],o['best'],len(R),np.nanmean(R).round(3),(np.nanmean(R)-2*np.nanstd(R,ddof=1)/np.sqrt(np.isfinite(R).sum())).round(3), np.nanmean([w['MAE'] for w in o['windows']]).round(2))
pickle.dump(dec,open(os.environ['TMPDIR']+'/dec.pkl','wb'))
EOF
date -u
```

```
(0.8, 'methods') 92.71736812591553
   Jun0414Bda01.mat 4 5 40 0.362 0.198 8.4
   Jun0414Bda02.mat 5 12 40 0.373 0.239 27.79
   Jun0414Bda03.mat 5 17 40 0.806 0.756 15.15
   Jun0914da01.mat 5 5 40 -0.06 -0.127 19.46
   Jun0914da02.mat 4 13 40 0.894 0.875 19.84
   Jun0914da03.mat 5 20 40 0.605 0.505 29.46
   Jun1114da01.mat 5 5 40 0.873 0.849 4.36
   Jun1114da02.mat 5 17 40 0.828 0.79 6.64
   Jun1114da03.mat 6 5 40 0.89 0.871 11.84
(0.8, 'code') 213.2697319984436
   Jun0414Bda01.mat 4 5 174 0.291 0.212 8.47
   Jun0414Bda02.mat 5 10 174 0.46 0.401 26.56
   Jun0414Bda03.mat 5 10 174 0.809 0.783 15.74
   Jun0914da01.mat 5 5 174 -0.102 -0.131 13.28
   Jun0914da02.mat 4 10 174 0.877 0.863 22.84
   Jun0914da03.mat 5 25 174 0.579 0.529 26.29
   Jun1114da01.mat 5 15 174 0.866 0.852 4.05
   Jun1114da02.mat 5 15 174 0.814 0.793 6.58
   Jun1114da03.mat 6 5 174 0.908 0.9 10.84
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('apl.py').read()
s=s.replace('''            "windows": res[best], "by_history": {h: (np.nanmean([w["R"] for w in v]),
                                                      np.nanmean([w["MAE"] for w in v]))
                                                  for h, v in res.items()}}''','''            "windows": res[best], "by_history": {h: (np.array([w["R"] for w in v]),
                                                      np.array([w["MAE"] for w in v]))
                                                  for h, v in res.items()}}''')
open('apl.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && OMP_NUM_THREADS=1 python - <<'EOF'
import time, apl, numpy as np
D=apl.load(); recs=D['recs']; sds=apl.gaussian_sds(recs)
t=time.time(); o=apl.analyse_program((recs[0], float(sds['twelve'][0]), 'min80', False)); print(time.time()-t, o['d'], apl.summarise(o)['period_mean'])
t=time.time(); o=apl.analyse_program((recs[0], float(sds['sqrt12'][0]), 'min80', False)); print(time.time()-t, o['d'], apl.summarise(o)['period_mean'])
EOF
```

```
2.393902063369751 66 17.153170347003154
1.8875212669372559 28 12.804674922600618
```

**Agent calls Bash**

```bash
cd  && python tools/entry.py --help 2>&1 | head -30; grep -n "def cmd_\|timeout\|runtime\|sanity\|claim:\|executed" tools/entry.py | head -60
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]

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
tied to the data:

[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,240p tools/entry.py; sed -n 342,400p tools/entry.py
```

```
report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")

    listed = [n["path"] for n in entry.get("notebooks", [])]
    present = sorted(p.name for p in entry_dir.glob("*.ipynb"))
    for name in sorted(set(present) - set(listed)):
        report.error(rel / name, "notebook is not listed in entry.yaml")
    for name in sorted(set(listed) - set(present)):
        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
    helpers = entry.get("helpers", [])
    for name in helpers:
        if not (entry_dir / name).is_file():
            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")

    requirements, lock = entry_dir / "requirements.in", entry_dir / "requirements.lock.txt"
    if not requirements.is_file():
        report.error(rel, "no requirements.in")
    elif not lock.is_file():
        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
    else:
        pinned = {re.split(r"[=<>!~\[ ]", line, maxsplit=1)[0].lower().replace("_", "-")
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-apl-1-bruno-2017 && sed -i 's|^BUCKET = |DATASET = "apl-1"            # CRCNS data set, doi:10.6080/K0SN074B\nVERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5 sums are checked\nBUCKET = |' apl.py && grep -n "^DATASET\|^VERSION\|^BUCKET" apl.py && date -u
```

```
51:DATASET = "apl-1"            # CRCNS data set, doi:10.6080/K0SN074B
52:VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5 sums are checked
53:BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/"
Sun Nov  8 12:58:30 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build.py",
 "content": "\"\"\"Builds the notebook of entries/crcns-apl-1-bruno-2017 from cell sources.\"\"\"\nimport json\nimport sys\n\nimport nbformat\n\nRESULTS = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}\nOUT = \"entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb\"\ncells = []\n\n\ndef md(s):\n    cells.append(nbformat.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tag=None):\n    c = nbformat.v4.new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag]\n    cells.append(c)\n\n\ndef result(cid):\n    if cid in RESULTS:\n        md(RESULTS[cid])\n\n\nmd(RESULTS.get(\"header\", \"# Header placeholder\"))\n\ncode('''\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport time\nimport resource\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport statsmodels.api as sm\nfrom scipy import stats\n\nimport apl\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nstarted = time.time()\nD = apl.load()\nrecs, preps = D[\"recs\"], D[\"preps\"]\nprint(f\"CRCNS data set {apl.DATASET}, version {apl.VERSION}; read {len(D['md5'])} files from {apl.BUCKET} \"\n      f\"in {time.time() - started:.0f} s\")\n''')\n\nmd('''\n## Data check\n\nEach check of the description against the values is stated under its output.\n''')\n\ncode('''\nprint(\"MD5 of each file read, against the data set's checksums.md5:\")\nfor name, h in D[\"md5\"].items():\n    print(f\"  {name:24s} {h}  {'matches' if D['listed_md5'].get(name) == h else 'DIFFERS from ' + str(D['listed_md5'].get(name))}\")\ninfo = pd.DataFrame([{\n    \"prep\": r[\"prep\"], \"bout\": r[\"bout\"], \"file\": r[\"file\"], \"Bout_field\": r[\"Bout_field\"],\n    \"neurons\": int(np.unique(r[\"ids\"]).size), \"max_id\": int(r[\"ids\"].max()),\n    \"spikes\": r[\"t\"].size, \"first_spike_s\": r[\"t\"].min().round(3), \"last_spike_s\": r[\"t\"].max().round(2),\n    \"neurons_spiking_after_30s\": int(np.unique(r[\"ids\"][r[\"t\"] >= 30]).size)} for r in recs])\nprint(\"\\\\nRecordings per preparation:\", info.groupby(\"prep\").size().to_dict())\nprint(info.to_string(index=False))\npt = pd.DataFrame(preps)\npt[\"neurons_in_spikes\"] = [int(info[info.prep == p].neurons.iloc[0]) for p in pt.prep]\npt[\"coord_points\"] = [c[\"x\"].size for c in D[\"coords\"]]\npt[\"coord_file\"] = [c[\"file\"] for c in D[\"coords\"]]\npt[\"coord_ganglion\"] = [c[\"ganglion\"] for c in D[\"coords\"]]\nprint(\"\\\\nFileTable.mat against the spike and coordinate files:\")\nprint(pt.to_string(index=False))\nprint(\"\\\\nNeurons per preparation: min\", pt.n_neurons_table.min(), \"max\", pt.n_neurons_table.max(),\n      \"total\", pt.n_neurons_table.sum(), \"(description: 75 to 160, 1131 in total)\")\nprint(\"Same neuron count in all three bouts of every preparation:\",\n      bool(info.groupby(\"prep\").neurons.nunique().eq(1).all()))\n''', \"sanity\")\n\nmd('''\nThe data set holds 30 recordings, three bouts in each of 10 preparations, in the order of\nFileTable.mat, which the description says is the paper's numbering. Every neuron id from 1 to N is\npresent in every bout of its preparation, and every neuron spikes after 30 s. The spike files carry\nno bout number (`Bout` is empty); the bout is read from the file name (da01, da02, da03). The\nneuron counts of FileTable.mat match the spike files and the coordinate files. The MD5 sums printed\nabove are the version pinned (CRCNS data sets are not versioned).\n''')\n\ncode('''\n# Units, ranges, the clock of the stimulus, and recordings deposited twice.\nrows = []\nfor r in recs:\n    t = r[\"t\"]\n    pre = np.sum((t >= 25) & (t < 30)) / 5\n    stim = np.sum((t >= 30) & (t < 32.5)) / 2.5\n    post = np.sum((t >= 32.5) & (t < 37.5)) / 5\n    rows.append({\"file\": r[\"file\"], \"pop_rate_25_30\": round(pre, 1), \"pop_rate_30_32.5\": round(stim, 1),\n                 \"pop_rate_32.5_37.5\": round(post, 1)})\nclock = pd.DataFrame(rows)\nprint(\"Population spike rate (spikes/s) before, during and after the stimulus at 30 to 32.5 s:\")\nprint(clock.to_string(index=False))\nprint(\"Recordings whose rate after 32.5 s exceeds that before 30 s:\",\n      int((clock[\"pop_rate_32.5_37.5\"] > clock[\"pop_rate_25_30\"]).sum()), \"of\", len(clock))\n# P10 nerve recordings\nrows = []\nfor q in D[\"p10\"]:\n    t = q[\"t\"]\n    rows.append({\"file\": q[\"file\"], \"prep\": q[\"prep\"], \"bout\": q[\"bout\"], \"spikes\": t.size,\n                 \"ids\": np.unique(q[\"ids\"]).tolist(), \"time_sorted\": q[\"sorted\"],\n                 \"range_s\": f\"{t.min():.2f} to {t.max():.2f}\",\n                 \"min_interval_ms\": round(np.diff(t).min() * 1000, 3),\n                 \"rate_25_30\": round(np.sum((t >= 25) & (t < 30)) / 5, 1),\n                 \"rate_32.5_37.5\": round(np.sum((t >= 32.5) & (t < 37.5)) / 5, 1)})\nprint(\"\\\\nP10 recordings:\")\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"Smallest P10 interval as a sampling period: 1 /\", round(1 / np.diff(D[\"p10\"][0][\"t\"]).min(), 1), \"Hz\")\n# duplicate recordings: identical spike trains between any two recordings\nsig = {}\nfor r in recs:\n    for i, tr in enumerate(apl.neuron_trains(r)):\n        if tr.size > 5:\n            sig.setdefault(tuple(np.round(tr, 4)), []).append((r[\"file\"], i + 1))\ndup = [v for v in sig.values() if len(v) > 1]\nprint(\"\\\\nNeuron spike trains (more than 5 spikes) found identical in two places:\", len(dup), dup[:5])\nwhole = {}\nfor r in recs:\n    whole.setdefault((r[\"t\"].size, round(float(r[\"t\"].sum()), 3)), []).append(r[\"file\"])\nprint(\"Recordings with identical spike counts and sums:\", [v for v in whole.values() if len(v) > 1])\npd10 = {}\nfor q in D[\"p10\"]:\n    pd10.setdefault((q[\"t\"].size, round(float(q[\"t\"].sum()), 3)), []).append(q[\"file\"])\nprint(\"P10 recordings deposited twice:\", [v for v in pd10.values() if len(v) > 1])\n''', \"sanity\")\n\ncode('''\n# Is the P10 nerve on the clock of the population? Cross-correlation of 1 s binned rates after the\n# stimulus, against the same with the P10 series shifted by a random amount (circularly).\nrng = np.random.default_rng(11)\nrows = []\nfor q in D[\"p10\"]:\n    r = next(r for r in recs if r[\"prep\"] == q[\"prep\"] and r[\"bout\"] == q[\"bout\"])\n    edges = np.arange(33, 122, 0.5)\n    pop = np.histogram(r[\"t\"], edges)[0].astype(float)\n    nerve = np.histogram(q[\"t\"], edges)[0].astype(float)\n    lags = np.arange(-10, 11)\n    cc = [np.corrcoef(np.roll(pop, l), nerve)[0, 1] for l in lags]\n    shuffled = [np.corrcoef(np.roll(pop, int(rng.integers(20, len(pop) - 20))), nerve)[0, 1] for _ in range(200)]\n    rows.append({\"file\": q[\"file\"], \"peak_lag_s\": lags[int(np.nanargmax(np.abs(cc)))] * 0.5,\n                 \"r_at_lag_0\": round(cc[10], 3), \"max_abs_r\": round(np.nanmax(np.abs(cc)), 3),\n                 \"shifted_95pct_abs_r\": round(np.nanpercentile(np.abs(shuffled), 95), 3)})\nprint(\"Population rate against P10 rate, 0.5 s bins from 33 s, lags of -5 to 5 s:\")\nprint(pd.DataFrame(rows).to_string(index=False))\n# Are neuron ids the same neurons across bouts? Per-neuron rates after onset, correlated between\n# bouts of a preparation, against the same with the ids permuted.\nrows = []\nfor p in range(1, 11):\n    rs = [np.array([np.sum(tr >= 30) for tr in apl.neuron_trains(r)]) for r in recs if r[\"prep\"] == p]\n    for a, b in apl.PAIRS:\n        rho = stats.spearmanr(rs[a], rs[b])[0]\n        null = [stats.spearmanr(rs[a], rng.permutation(rs[b]))[0] for _ in range(200)]\n        rows.append({\"prep\": p, \"pair\": f\"{a + 1},{b + 1}\", \"spearman\": round(rho, 3),\n                     \"permuted_95pct\": round(np.percentile(null, 95), 3)})\nidt = pd.DataFrame(rows)\nprint(\"\\\\nRank correlation of neurons' post-onset spike counts between bouts (same id):\")\nprint(idt.pivot(index=\"prep\", columns=\"pair\", values=\"spearman\").to_string())\nprint(\"Pairs above the 95th percentile of permuted ids:\", int((idt.spearman > idt.permuted_95pct).sum()), \"of\", len(idt))\n''', \"sanity\")\n\ncode('''\n# Coordinates: units and ranges, against the 501 x 501 diode template (plot_maps.m plots x*10, y*10)\nfor c, p in zip(D[\"coords\"], preps):\n    print(f\"prep {p['prep']:2d} {c['file']:14s} {c['ganglion']:24s} n={c['x'].size:3d} x {np.nanmin(c['x']):5.1f} to {np.nanmax(c['x']):5.1f}  \"\n          f\"y {np.nanmin(c['y']):5.1f} to {np.nanmax(c['y']):5.1f}  missing {int(np.isnan(c['x']).sum())}\")\ntpl = D[\"template\"]\nys, xs = np.nonzero(tpl)\nprint(\"Diode template\", tpl.shape, \"nonzero x\", xs.min(), \"to\", xs.max(), \"y\", ys.min(), \"to\", ys.max())\n''', \"sanity\")\n\nmd(RESULTS.get(\"datacheck\", \"Data check notes placeholder\"))\n\n# ---------------------------------------------------------------- dataset-size\nmd('''\n## dataset-size\n\n> Three bouts of fictive locomotion were evoked in each of 10 isolated preparations (30 population\n> responses); each recorded population held 120 to 180 neurons, 1131 neurons in all.\n''')\ncode('''\nn_preps = info.prep.nunique()\nn_recs = len(info)\nper_prep = info.groupby(\"prep\").neurons.first()\nprint(\"preparations\", n_preps, \"| recordings\", n_recs, \"| neurons over preparations\", int(per_prep.sum()))\nprint(\"neurons per recording: min\", info.neurons.min(), \"max\", info.neurons.max())\nprint(\"recordings with 108 to 198 neurons:\", int(info.neurons.between(108, 198).sum()), \"of\", n_recs)\nprint(\"variant, neurons spiking after onset: min\", info.neurons_spiking_after_30s.min(), \"max\",\n      info.neurons_spiking_after_30s.max(), \"total over preparations\",\n      int(info.groupby(\"prep\").neurons_spiking_after_30s.first().sum()))\nprint(\"per preparation:\", per_prep.to_dict())\n''', \"claim:dataset-size\")\nresult(\"dataset-size\")\n\n# ---------------------------------------------------------------- fig1d\nmd('''\n## fig1d-slow-oscillation\n\n> After stimulation the spike-train power spectra of the populations are dominated by a slow\n> oscillation at or below 0.1 Hz.\n\nChronux `mtspectrumpt` (ported in `apl.mtspectrumpt`, default tapers [3 5], 1 ms, fpass 0 to 1 Hz)\nof each neuron's spikes after onset, averaged over the neurons of a recording.\n''')\ncode('''\nt0 = time.time()\nspectra = []\nfor r in recs:\n    trains = [tr[tr >= apl.STIM_ON] for tr in apl.neuron_trains(r)]\n    f, S = apl.mtspectrumpt(trains)\n    spectra.append(S)\nspectra = np.array(spectra)\ngrand = spectra.mean(0)\nfpk = np.array([apl.peak_frequency(f, S) for S in spectra])\nfmax = np.array([f[1:][np.argmax(S[1:])] for S in spectra])\nprint(f\"spectra in {time.time() - t0:.0f} s; frequency grid {f[0]:.4f} to {f[-1]:.4f} Hz, step {f[1] - f[0]:.4f} Hz\")\nprint(\"grand mean spectrum: weighted peak\", round(apl.peak_frequency(f, grand), 4), \"Hz; maximum above 0 Hz at\",\n      round(f[1:][np.argmax(grand[1:])], 4), \"Hz\")\nprint(\"per recording, weighted peak (code): min\", fpk.min().round(4), \"median\", np.median(fpk).round(4), \"max\", fpk.max().round(4))\nprint(\"recordings with weighted peak above 0 and at or below 0.11 Hz:\", int(((fpk > 0) & (fpk <= 0.11)).sum()), \"of 30\")\nprint(\"variant, frequency of maximum power above 0 Hz: min\", fmax.min().round(4), \"median\", np.median(fmax).round(4),\n      \"max\", fmax.max().round(4), \"; at or below 0.11 Hz:\", int((fmax <= 0.11).sum()), \"of 30\")\nprint(pd.DataFrame({\"file\": [r[\"file\"] for r in recs], \"weighted_peak_Hz\": fpk.round(4), \"max_power_Hz\": fmax.round(4)}).to_string(index=False))\nfig, ax = plt.subplots(figsize=(5, 3))\nfor S in spectra:\n    ax.plot(f, S, color=\"0.7\", lw=0.5)\nax.plot(f, grand, \"k\")\nax.set_xlabel(\"frequency (Hz)\"); ax.set_ylabel(\"power\"); ax.set_title(\"post-onset spectra (all points shown)\")\nplt.show()\n''', \"claim:fig1d-slow-oscillation\")\nresult(\"fig1d-slow-oscillation\")\n\n# ---------------------------------------------------------------- fig1e\nmd('''\n## fig1e-decaying-rate\n\n> The population firing rate decays slowly after the stimulus, decreasing in most evoked responses.\n''')\ncode('''\nrows = []\nfor r in recs:\n    t = r[\"t\"]\n    starts = np.arange(30, r[\"t\"].max() - 20 + 1e-9, 5)\n    counts = np.array([np.sum((t >= s) & (t < s + 20)) for s in starts])\n    R = np.corrcoef(starts + 10, counts)[0, 1]\n    edges = np.arange(32.5, r[\"t\"].max(), 1.0)\n    rate = np.histogram(t, edges)[0]\n    slope = np.polyfit(edges[:-1] + 0.5, rate, 1)[0]\n    rows.append({\"prep\": r[\"prep\"], \"bout\": r[\"bout\"], \"R_20s_windows\": R, \"n_windows\": len(starts), \"slope_spikes_per_s2\": slope})\nrate_tab = pd.DataFrame(rows)\nprint(rate_tab.round(3).to_string(index=False))\nprint(\"(a) decreasing, R < -0.2:\", int((rate_tab.R_20s_windows < -0.2).sum()), \"of 30; increasing, R > 0.2:\",\n      int((rate_tab.R_20s_windows > 0.2).sum()))\nprint(\"(b) negative slope from 32.5 s:\", int((rate_tab.slope_spikes_per_s2 < 0).sum()), \"of 30\")\nprint(\"per preparation, (a) decreasing:\", rate_tab.assign(dec=rate_tab.R_20s_windows < -0.2).groupby(\"prep\").dec.sum().to_dict())\n''', \"claim:fig1e-decaying-rate\")\nresult(\"fig1e-decaying-rate\")\n\n# ---------------------------------------------------------------- fig2b\nmd('''\n## fig2b-dimensions\n\n> Capturing 80% of the population variance needs 4 to 8 embedding dimensions in the evoked\n> responses, a reduction by more than a factor of 10 from the number of neurons.\n\nThe Gaussian SD is read four ways (helper docstring) and the count two ways, as the criterion\nlists them.\n''')\ncode('''\nsds = apl.gaussian_sds(recs)\nprint(\"Gaussian SD (s) by reading: \", {k: (round(v.min(), 3), round(v.max(), 3)) for k, v in sds.items()})\ndims = {}\nt0 = time.time()\nfor mode in [\"sqrt12\", \"twelve\", \"own\", \"pooled\"]:\n    evs = [apl.Program(r, s).ev for r, s in zip(recs, sds[mode])]\n    for rule in [\"min80\", \"le80\"]:\n        dims[(mode, rule)] = np.array([apl.n_pcs(ev, 0.8, rule) for ev in evs])\nprint(f\"PCA under every reading in {time.time() - t0:.0f} s\")\nnn = info.neurons.values\nrows = []\nfor (mode, rule), d in dims.items():\n    rows.append({\"sd\": mode, \"count\": rule, \"min\": d.min(), \"max\": d.max(), \"in_3.6_to_8.8\": int(((d >= 3.6) & (d <= 8.8)).sum()),\n                 \"min_neurons_over_dims\": round((nn / d).min(), 1), \"ratio_over_10\": int((nn / d > 10).sum())})\ndim_tab = pd.DataFrame(rows)\nprint(dim_tab.to_string(index=False))\nprint(\"\\\\ncounts per recording (min80 | le80) for the code's width (own median ISI):\")\nprint(pd.DataFrame({\"file\": info.file, \"own_min80\": dims[(\"own\", \"min80\")], \"own_le80\": dims[(\"own\", \"le80\")],\n                    \"pooled_min80\": dims[(\"pooled\", \"min80\")], \"pooled_le80\": dims[(\"pooled\", \"le80\")], \"neurons\": nn}).to_string(index=False))\n''', \"claim:fig2b-dimensions\")\nresult(\"fig2b-dimensions\")\n\n# ---------------------------------------------------------------- recurrence\nmd('''\n## The recurrence analysis\n\nRun once per reading of the width and the count. The local linear models (claims fig4 to fig5)\nare fitted for the four readings with the code's width; the two narrow widths give 22 to 75\ndimensions (claim fig2b-dimensions) and are carried only through the dominant period\n(fig2ef-periodic-recurrence). The adopted reading, used where one reading has to be chosen, is\n`own/min80`: the median ISI of the recording (the width the code uses; the Methods compute it\n\"in population\", the recording) and the smallest number of PCs reaching 80% (the Methods, \"at least\n80% of the variance\"). The other readings are shown with it.\n''')\ncode('''\nt0 = time.time()\nRUNS = {}\nfor mode in [\"own\", \"pooled\"]:\n    for rule in [\"min80\", \"le80\"]:\n        RUNS[f\"{mode}/{rule}\"] = apl.run_all(recs, sds[mode], rule, lld=True, workers=4)\nfor mode in [\"sqrt12\", \"twelve\"]:\n    for rule in [\"min80\", \"le80\"]:\n        RUNS[f\"{mode}/{rule}\"] = apl.run_all(recs, sds[mode], rule, lld=False, workers=4)\nSUM = {k: pd.DataFrame([apl.summarise(o) for o in v]) for k, v in RUNS.items()}\nprint(f\"recurrence analysis of 30 recordings under {len(RUNS)} readings in {time.time() - t0:.0f} s; \"\n      f\"peak memory {resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6:.2f} GB per worker\")\nADOPT = \"own/min80\"\nprint(\"checked points per recording:\", SUM[ADOPT].n_points.min(), \"to\", SUM[ADOPT].n_points.max(), \"(Methods: around 7770)\")\n''')\n\nmd('''\n## fig2ef-periodic-recurrence\n\n> The evoked low-dimensional activity recurs with a regular period; strongly periodic recurrence on\n> the scale of 10 to 15 s is found in many but not all of the 30 responses.\n''')\ncode('''\nrows = []\nfor k, S in SUM.items():\n    for stat in [\"period_mean\", \"period_median\"]:\n        v = S[stat].values\n        rows.append({\"reading\": k, \"period\": stat, \"n_with_peak\": int(np.isfinite(v).sum()),\n                     \"in_9_to_16.5\": int(((v >= 9) & (v <= 16.5)).sum()), \"min\": np.nanmin(v).round(2),\n                     \"median\": np.nanmedian(v).round(2), \"max\": np.nanmax(v).round(2)})\nper_tab = pd.DataFrame(rows)\nper_tab[\"reproduced\"] = (per_tab[\"in_9_to_16.5\"] > 15) & (per_tab[\"in_9_to_16.5\"] < 30)\nprint(per_tab.to_string(index=False))\nS = SUM[ADOPT]\nprint(\"\\\\nadopted reading, per recording:\")\nprint(S[[\"prep\", \"bout\", \"d\", \"n_peaks\", \"prop_recurrent\", \"period_mean\", \"period_median\"]].round(3).to_string(index=False))\nprint(\"by preparation, mean period:\", S.groupby(\"prep\").period_mean.mean().round(2).to_dict())\n''', \"claim:fig2ef-periodic-recurrence\")\nresult(\"fig2ef-periodic-recurrence\")\n\nmd('''\n## fig2e-single-dominant-orbit\n\n> Almost all populations are dominated by a single periodic orbit; the majority of programs have\n> more than 50% of their recurrent points in the dominant peak.\n''')\ncode('''\nrows = []\nfor k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]:\n    S = SUM[k]\n    rows.append({\"reading\": k, \"over_50pct_hist\": int((S.prop_dom_hist > 0.5).sum()),\n                 \"over_50pct_all_recurrent\": int((S.prop_dom_all > 0.5).sum()),\n                 \"peaks_min\": S.n_peaks.min(), \"peaks_max\": S.n_peaks.max(),\n                 \"peaks_counts\": S.n_peaks.value_counts().sort_index().to_dict()})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\\\nadopted reading:\")\nprint(SUM[ADOPT][[\"prep\", \"bout\", \"n_peaks\", \"dom_n\", \"prop_dom_hist\", \"prop_dom_all\"]].round(3).to_string(index=False))\n''', \"claim:fig2e-single-dominant-orbit\")\nresult(\"fig2e-single-dominant-orbit\")\n\nmd('''\n## fig2s2-threshold-robust\n\n> The periodic orbits are robust to the threshold for recurrence, with similar periodicity at\n> thresholds of 10%, 5% and 2%.\n''')\ncode('''\nrows = []\nfor k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]:\n    P = {th: pd.DataFrame([apl.summarise(o, i) for o in RUNS[k]]) for i, th in enumerate(apl.THETA_PRCT)}\n    for stat in [\"period_mean\", \"period_median\"]:\n        p10 = P[10][stat].values\n        for th in (5, 2):\n            pl = P[th][stat].values\n            ok = np.isfinite(p10) & np.isfinite(pl)\n            rho, p = stats.spearmanr(p10[ok], pl[ok])\n            mad = np.median(np.abs(pl[ok] - p10[ok]))\n            rows.append({\"reading\": k, \"period\": stat, \"theta\": f\"{th}%\", \"n_both\": int(ok.sum()),\n                         \"spearman\": round(rho, 3), \"p\": p, \"(a)\": bool(rho > 0 and p < 0.05),\n                         \"median_abs_diff_s\": round(mad, 2), \"10pct_of_median\": round(0.1 * np.median(p10[ok]), 2),\n                         \"(b)\": bool(mad < 0.1 * np.median(p10[ok]))})\nthr_tab = pd.DataFrame(rows)\nprint(thr_tab.to_string(index=False))\nP = {th: pd.DataFrame([apl.summarise(o, i) for o in RUNS[ADOPT]]) for i, th in enumerate(apl.THETA_PRCT)}\nprint(\"\\\\nadopted reading, mean dominant period at each threshold:\")\nprint(pd.DataFrame({th: P[th].period_mean.round(2) for th in P}).assign(file=info.file).to_string(index=False))\n''', \"claim:fig2s2-threshold-robust\")\nresult(\"fig2s2-threshold-robust\")\n\nmd('''\n## fig3a-coalescence\n\n> Almost all evoked responses reach a state of high recurrence within one oscillation period of\n> stimulation and are thereafter dominated by recurrence.\n\nThe coalescence time is the mid-point of the first 5 s window with more than 90% recurrent points.\nWindows start at 35 s, where the checked points start (Methods), so the earliest possible value is\n37.5 s, 7.5 s after onset.\n''')\ncode('''\nrows = []\nfor k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]:\n    S = SUM[k]\n    c_on = S.coalesce_t - apl.STIM_ON\n    for stat in [\"period_mean\", \"period_median\"]:\n        rows.append({\"reading\": k, \"period\": stat, \"within_period_from_onset\": int((c_on <= S[stat]).sum()),\n                     \"within_period_from_offset\": int((c_on - 2.5 <= S[stat]).sum()),\n                     \"recurrent_after_over_50pct\": int((S.prop_recurrent_after > 0.5).sum()),\n                     \"never_coalesced\": int(S.coalesce_t.isna().sum())})\nprint(pd.DataFrame(rows).to_string(index=False))\nS = SUM[ADOPT].assign(coal_from_onset=lambda d: d.coalesce_t - 30)\nprint(\"\\\\nadopted reading: coalescence from onset, s: min\", S.coal_from_onset.min(), \"median\", S.coal_from_onset.median(),\n      \"max\", S.coal_from_onset.max(), \"; proportion recurrent after it: min\", S.prop_recurrent_after.min().round(3),\n      \"median\", S.prop_recurrent_after.median().round(3))\nprint(S[[\"prep\", \"bout\", \"coal_from_onset\", \"period_mean\", \"period_median\", \"prop_recurrent_after\"]].round(3).to_string(index=False))\n''', \"claim:fig3a-coalescence\")\nresult(\"fig3a-coalescence\")\n\n# ---------------------------------------------------------------- manifold\nmd('''\n## Comparisons between the programs of a preparation\n\nHausdorff distances on the axes of program 1 (claim fig3c) and on common axes (fig3s1a), with 100\nneuron shuffles each way as control; the distances of Figure 3D; the similarity matrices of\nFigure 3F. Run for the four readings with the code's width (the point sets come from each\nreading's recurrence analysis).\n''')\ncode('''\nt0 = time.time()\nMAN = {k: apl.run_manifold(recs, sds[k.split(\"/\")[0]], RUNS[k], n_shuffle=100, seed=1)\n       for k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]}\nprint(f\"comparisons in {time.time() - t0:.0f} s\")\ndef haus_table(k, axes, ps):\n    rows = []\n    for m in MAN[k]:\n        for (i, j) in apl.PAIRS:\n            h, c = m[(axes, ps, i, j)]\n            rows.append({\"prep\": m[\"prep\"], \"pair\": f\"{i + 1},{j + 1}\", \"H\": h, \"ctrl_mean\": np.mean(c),\n                         \"ctrl_2sem\": 2 * np.std(c, ddof=1) / np.sqrt(c.size), \"dims\": m[\"k_prog1\" if axes == \"prog1\" else \"k_common\"]})\n    return pd.DataFrame(rows)\n''')\n\nmd('''\n## fig3c-same-manifold\n\n> Sequentially evoked responses of a preparation fall on the same manifold; their distance is below\n> that of random projections for all pairs except two, pairs (1,2) and (1,3) of preparation 4.\n''')\ncode('''\nrows = []\nfor k in MAN:\n    for ps in [\"recurrent\", \"code\"]:\n        T = haus_table(k, \"prog1\", ps)\n        below = T.H < T.ctrl_mean\n        rows.append({\"reading\": k, \"points\": ps, \"pairs_below_control\": int(below.sum()),\n                     \"failing_pairs\": [(p, q) for p, q in zip(T.prep[~below], T.pair[~below])]})\nprint(pd.DataFrame(rows).to_string(index=False))\nT = haus_table(ADOPT, \"prog1\", \"recurrent\")\nprint(\"\\\\nadopted reading, recurrent points:\")\nprint(T.assign(ratio=T.H / T.ctrl_mean).round(3).to_string(index=False))\nT = haus_table(ADOPT, \"prog1\", \"code\")\nprint(\"\\\\nadopted reading, the code's point sets:\")\nprint(T.assign(ratio=T.H / T.ctrl_mean).round(3).to_string(index=False))\n''', \"claim:fig3c-same-manifold\")\nresult(\"fig3c-same-manifold\")\n\nmd('''\n## fig3s1a-common-axes\n\n> The convergence of sequential responses to the same manifold holds when the three programs are\n> projected onto common axes from a PCA of their concatenated activity.\n''')\ncode('''\nrows = []\nfor k in MAN:\n    for ps in [\"recurrent\", \"code\"]:\n        T = haus_table(k, \"common\", ps)\n        below = T.H < T.ctrl_mean\n        rows.append({\"reading\": k, \"points\": ps, \"pairs_below_control\": int(below.sum()),\n                     \"failing_pairs\": [(p, q) for p, q in zip(T.prep[~below], T.pair[~below])],\n                     \"dims\": sorted(set(T.dims))})\nprint(pd.DataFrame(rows).to_string(index=False))\nT = haus_table(ADOPT, \"common\", \"code\")\nprint(\"\\\\nadopted reading, the code's point sets:\")\nprint(T.assign(ratio=T.H / T.ctrl_mean).round(3).to_string(index=False))\n''', \"claim:fig3s1a-common-axes\")\nresult(\"fig3s1a-common-axes\")\n\nmd('''\n## fig3d-initial-conditions\n\n> Stimulation drives responses of the same preparation far apart before coalescence, more than at\n> stimulus onset or after both have coalesced, so the same manifold is reached from different\n> initial conditions.\n\nThe transient distance is the largest distance between a point of one program and a point of the\nother between onset and their coalescence; for speed every fifth point of the second program is\nused (a standard choice: neighbouring points 10 ms apart are nearly equal).\n''')\ncode('''\nrows = []\nfor k in MAN:\n    for ps in [\"code\", \"recurrent\"]:\n        for m in MAN[k]:\n            for (i, j) in apl.PAIRS:\n                on, tr = m[(\"ic\", i, j)]\n                rows.append({\"reading\": k, \"points\": ps, \"prep\": m[\"prep\"], \"pair\": f\"{i + 1},{j + 1}\",\n                             \"onset\": on, \"transient\": tr, \"coalesced\": m[(\"common\", ps, i, j)][0]})\nIC = pd.DataFrame(rows)\nsumm = IC.groupby([\"reading\", \"points\"]).apply(lambda d: pd.Series({\n    \"transient_over_both\": int(((d.transient > d.onset) & (d.transient > d.coalesced)).sum()),\n    \"median_onset\": d.onset.median(), \"median_transient\": d.transient.median(), \"median_coalesced\": d.coalesced.median()}))\nprint(summ.round(2).to_string())\nprint(\"\\\\nadopted reading, code's point sets:\")\nprint(IC[(IC.reading == ADOPT) & (IC.points == \"code\")].drop(columns=[\"reading\", \"points\"]).round(2).to_string(index=False))\n''', \"claim:fig3d-initial-conditions\")\nresult(\"fig3d-initial-conditions\")\n\nmd('''\n## fig3f-pairwise-similarity\n\n> Pairwise similarity between neurons is preserved across responses of the same preparation, above a\n> null model, except for pairs (1,3) and (2,3) of preparation 7.\n''')\ncode('''\nrows, detail = [], []\nfor k in MAN:\n    for meth in [\"spearman\", \"pearson\"]:\n        corr = (lambda a, b: stats.spearmanr(a, b)[0]) if meth == \"spearman\" else (lambda a, b: np.corrcoef(a, b)[0, 1])\n        for ctl in [\"first\", \"larger\"]:\n            n, fails = 0, []\n            for m in MAN[k]:\n                Sm, Em = m[\"sim\"]\n                cs = [corr(Sm[i].ravel(), Em[i].ravel()) for i in range(3)]\n                for (i, j) in apl.PAIRS:\n                    dat = corr(Sm[i].ravel(), Sm[j].ravel())\n                    c = cs[i] if ctl == \"first\" else max(cs[i], cs[j])\n                    if dat > c:\n                        n += 1\n                    else:\n                        fails.append((m[\"prep\"], f\"{i + 1},{j + 1}\"))\n                    if k == ADOPT and ctl == \"first\":\n                        detail.append({\"corr\": meth, \"prep\": m[\"prep\"], \"pair\": f\"{i + 1},{j + 1}\", \"data\": dat,\n                                       \"control_first\": cs[i], \"control_second\": cs[j]})\n            rows.append({\"reading\": k, \"corr\": meth, \"control\": ctl, \"pairs_above\": n, \"failing\": fails})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\\\nadopted reading:\")\nprint(pd.DataFrame(detail).round(3).to_string(index=False))\n''', \"claim:fig3f-pairwise-similarity\")\nresult(\"fig3f-pairwise-similarity\")\n\nmd('''\n## fig3h-perturbations-return\n\n> Of 19 spontaneous divergences from the trajectory, 17 (90%) returned to a recurrent state; the two\n> that did not were consistent with the end of the evoked locomotion.\n\nA divergent period (Methods) is a run of windows after coalescence with recurrence density below\n90% that falls below 50%; \"returned\" means a later window is above 90%. Periods whose divergent\npoint lies within two dominant periods of the end are removed (Methods), with the dominant period\nread as the mean or the median of the peak. The code removes only periods that never return\n(`Are_jumps_perturbations_or_transitions2.m`); that is shown as a variant.\n''')\ncode('''\nDIV = {}\nrows = []\nfor k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]:\n    for stat in [\"period_mean\", \"period_median\"]:\n        allv = []\n        for o, s in zip(RUNS[k], SUM[k].itertuples()):\n            for d in apl.divergences(o, getattr(s, stat)):\n                d.update(prep=o[\"prep\"], bout=o[\"bout\"])\n                allv.append(d)\n        V = pd.DataFrame(allv)\n        DIV[(k, stat)] = V\n        kept = V[~V.near_end]\n        code_kept = V[V.returned | ~V.near_end]\n        rows.append({\"reading\": k, \"period\": stat, \"all_periods\": len(V), \"kept\": len(kept),\n                     \"returned\": int(kept.returned.sum()), \"fraction\": round(kept.returned.mean(), 3),\n                     \"code_rule_kept\": len(code_kept), \"code_rule_returned\": int(code_kept.returned.sum())})\nprint(pd.DataFrame(rows).to_string(index=False))\nV = DIV[(ADOPT, \"period_mean\")]\nprint(\"\\\\nadopted reading, mean period:\")\nprint(V[[\"prep\", \"bout\", \"t_point\", \"min_dens\", \"returned\", \"near_end\"]].round(3).to_string(index=False))\n''', \"claim:fig3h-perturbations-return\")\nresult(\"fig3h-perturbations-return\")\n\nmd('''\n## fig3i-same-manifold-after\n\n> Of the 17 divergences that returned to a recurrent state, all but three returned to the same\n> manifold; the three appeared to move to a different periodic attractor.\n''')\ncode('''\nrows = []\nfor (k, stat), V in DIV.items():\n    kept = V[~V.near_end & V.returned]\n    rows.append({\"reading\": k, \"period\": stat, \"returned\": len(kept),\n                 \"same_(a)_after_end\": int((kept.p_after_end > 0.2).sum()),\n                 \"same_(b)_after_point\": int((kept.p_after_point > 0.2).sum())})\nprint(pd.DataFrame(rows).to_string(index=False))\nV = DIV[(ADOPT, \"period_mean\")]\nprint(\"\\\\nadopted reading, returned periods:\")\nprint(V[~V.near_end & V.returned][[\"prep\", \"bout\", \"t_point\", \"t_return\", \"n_before\", \"p_after_end\", \"p_after_point\"]].round(3).to_string(index=False))\n''', \"claim:fig3i-same-manifold-after\")\nresult(\"fig3i-same-manifold-after\")\n\n# ---------------------------------------------------------------- eigenvalues\nmd('''\n## fig4bc-stable-spiral\n\n> The evoked responses have highly clustered maximum eigenvalues of the local linear dynamics,\n> dominated by negative complex values, so the pedal ganglion implements a contracting periodic\n> orbit, a stable spiral attractor, found in every preparation.\n''')\ncode('''\nEIG = {}\nrows = []\nfor k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]:\n    E = pd.DataFrame([{**{x: y for x, y in apl.emax_stats(o[\"eigs\"], o[\"npts\"]).items() if x != \"eigs\"},\n                       \"prep\": o[\"prep\"], \"bout\": o[\"bout\"]} for o in RUNS[k]])\n    E[\"spiral\"] = (E.a < -0.0001) & (E.b > 0.0005)\n    EIG[k] = E\n    per_prep = E.groupby(\"prep\").spiral.sum()\n    rows.append({\"reading\": k, \"mean_a\": E.a.mean(), \"mean_b\": E.b.mean(), \"sd_a\": E.a.std(), \"sd_b\": E.b.std(),\n                 \"grand_mean_spiral\": bool(E.a.mean() < -0.0001 and E.b.mean() > 0.0005),\n                 \"responses_spiral\": int(E.spiral.sum()), \"preps_2of3\": int((per_prep >= 2).sum()),\n                 \"used_points_min\": E.n_used.min(), \"dropped_points\": int((E.n_all - E.n_used).sum())})\nprint(pd.DataFrame(rows).to_string(index=False))\nE = EIG[ADOPT]\nprint(\"\\\\nadopted reading:\")\nprint(E[[\"prep\", \"bout\", \"a\", \"b\", \"sd_a\", \"sd_b\", \"n_used\", \"n_all\", \"spiral\"]].to_string(index=False))\nprint(\"spiral responses per preparation:\", E.groupby(\"prep\").spiral.sum().to_dict())\nfig, ax = plt.subplots(figsize=(4, 3.5))\nax.scatter(E.b, E.a, c=E.prep, cmap=\"tab10\", s=15)\nax.axhline(-0.0001, color=\"0.6\", lw=0.5); ax.axvline(0.0005, color=\"0.6\", lw=0.5)\nax.set_xlabel(\"mean imaginary part b\"); ax.set_ylabel(\"mean real part a\")\nax.set_title(f\"all 30 shown; a {E.a.min():.4f} to {E.a.max():.4f}\")\nplt.show()\n''', \"claim:fig4bc-stable-spiral\")\nresult(\"fig4bc-stable-spiral\")\n\nmd('''\n## fig4c-orbital-period\n\n> The linear model estimates a mean orbital period of about 10 s, consistent with the period from\n> the recurrent points.\n''')\ncode('''\nrows = []\nfor k, E in EIG.items():\n    lin = 2 * np.pi / E.b * 0.01\n    S = SUM[k]\n    r_mean = stats.pearsonr(lin, S.period_mean)\n    r_med = stats.pearsonr(lin, S.period_median)\n    rows.append({\"reading\": k, \"mean_linear_period_s\": lin.mean(), \"variant_mean_of_mRot_s\": E.mrot.mean(),\n                 \"pearson_r_vs_mean_recurrence\": r_mean[0], \"p\": r_mean[1], \"pearson_r_vs_median_recurrence\": r_med[0], \"p_med\": r_med[1],\n                 \"min\": lin.min(), \"max\": lin.max()})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n''', \"claim:fig4c-orbital-period\")\nresult(\"fig4c-orbital-period\")\n\nmd('''\n## fig4s1a-contracting-dimensions\n\n> In most responses the trajectory contracts in all embedding dimensions; a few responses have a\n> positive real eigenvalue in one low-variance dimension, a minor expansion.\n''')\ncode('''\nrows, detail = [], []\nfor k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]:\n    allneg = one_pos_later = 0\n    for o in RUNS[k]:\n        st = apl.emax_stats(o[\"eigs\"], o[\"npts\"])\n        ed = apl.eig_dimensions(st[\"eigs\"])\n        mu = ed[\"mean_unique\"]\n        allneg += bool(np.all(mu < 0))\n        one_pos_later += bool(np.sum(mu > 0) == 1 and mu[0] < 0)\n        if k == ADOPT:\n            detail.append({\"prep\": o[\"prep\"], \"bout\": o[\"bout\"], \"unique_dims\": mu.size, \"positive\": int(np.sum(mu > 0)),\n                           \"first_positive\": bool(mu[0] > 0), \"means\": np.round(mu * 1000, 3).tolist()})\n    rows.append({\"reading\": k, \"all_negative\": allneg, \"one_positive_not_first\": one_pos_later})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\\\nadopted reading (means x 1000):\")\nprint(pd.DataFrame(detail).to_string(index=False))\n''', \"claim:fig4s1a-contracting-dimensions\")\nresult(\"fig4s1a-contracting-dimensions\")\n\nmd('''\n## fig4s1b-rotation-dominant\n\n> Local trajectories were dominated by rotation throughout; in every preparation most local models\n> have a complex eigenvalue among their top two.\n''')\ncode('''\nrows, detail = [], []\nfor k in [\"own/min80\", \"own/le80\", \"pooled/min80\", \"pooled/le80\"]:\n    pc = []\n    for o in RUNS[k]:\n        st = apl.emax_stats(o[\"eigs\"], o[\"npts\"])\n        ed = apl.eig_dimensions(st[\"eigs\"])\n        pc.append({\"prep\": o[\"prep\"], \"bout\": o[\"bout\"], \"p_complex12\": ed[\"p_complex12\"], \"p_complex1\": ed[\"p_complex1\"]})\n    pc = pd.DataFrame(pc)\n    maj = pc.assign(o=pc.p_complex12 > 0.5).groupby(\"prep\").o.sum()\n    rows.append({\"reading\": k, \"responses_over_0.5\": int((pc.p_complex12 > 0.5).sum()), \"min\": pc.p_complex12.min(),\n                 \"preps_with_majority\": int((maj >= 2).sum())})\n    if k == ADOPT:\n        detail = pc\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(detail.round(4).to_string(index=False))\n''', \"claim:fig4s1b-rotation-dominant\")\nresult(\"fig4s1b-rotation-dominant\")\n\nmd('''\n## fig5b-period-changes\n\n> Over a response the orbital period may slow, speed up or not change; all three occur among the 30\n> responses.\n''')\ncode('''\nt0 = time.time()\nPC = {}\nrows = []\nfor k in [\"own/min80\", \"pooled/le80\", \"own/le80\", \"pooled/min80\"]:\n    out = []\n    for n, o in enumerate(RUNS[k]):\n        w = o[\"windows\"][-1]\n        hi = np.flatnonzero(w[\"dens\"] > 0.9)\n        sl = slice(hi[0], hi[-1] + 1)\n        wt = 1 / w[\"sddelay\"]\n        wt[~np.isfinite(wt)] = 0\n        wt = wt * w[\"dens\"]\n        r, p, nw = apl.weighted_spearman(w[\"mid_t\"][sl], w[\"mdelay\"][sl], wt[sl], 10000, np.random.default_rng(500 + n))\n        row = {\"prep\": o[\"prep\"], \"bout\": o[\"bout\"], \"rho\": r, \"p\": p, \"n_windows\": nw}\n        if k == ADOPT:\n            rc, pcode, _ = apl.weighted_spearman(w[\"mid_t\"][sl], w[\"mdelay\"][sl], wt[sl], 100000, np.random.default_rng(900 + n), pooled=True)\n            row.update(p_code=pcode)\n        out.append(row)\n    X = pd.DataFrame(out)\n    PC[k] = X\n    rows.append({\"reading\": k, \"slowing_p<0.01\": int(((X.rho > 0) & (X.p < 0.01)).sum()),\n                 \"speeding_p<0.01\": int(((X.rho < 0) & (X.p < 0.01)).sum()), \"no_change\": int((X.p >= 0.01).sum()),\n                 \"windows_min\": X.n_windows.min(), \"windows_max\": X.n_windows.max()})\nprint(f\"permutation tests in {time.time() - t0:.0f} s\")\nprint(pd.DataFrame(rows).to_string(index=False))\nX = PC[ADOPT]\nprint(\"\\\\nadopted reading; p from 10000 permutations of the delays (two-sided), p_code from the code's 100000 pooled permutations (one-sided):\")\nprint(X.round(4).to_string(index=False))\nprint(\"code test: slowing\", int(((X.rho > 0) & (X.p_code < 0.01)).sum()), \"speeding\", int(((X.rho < 0) & (X.p_code < 0.01)).sum()),\n      \"no change\", int((X.p_code >= 0.01).sum()))\n''', \"claim:fig5b-period-changes\")\nresult(\"fig5b-period-changes\")\n\nmd('''\n## fig5c-no-relation-contraction\n\n> There is no relationship between the change in orbital period over a response and its rate of\n> contraction, as a stable spiral predicts.\n''')\ncode('''\nrows = []\nfor k, X in PC.items():\n    E = EIG[k]\n    r, p = stats.pearsonr(X.rho, E.a)\n    contraction = np.exp(100 * E.a) * 100 - 100\n    r2, p2 = stats.pearsonr(X.rho, contraction)\n    rows.append({\"reading\": k, \"R_rho_vs_a\": r, \"p\": p, \"R_rho_vs_contraction_pct\": r2, \"p_contraction\": p2})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n''', \"claim:fig5c-no-relation-contraction\")\nresult(\"fig5c-no-relation-contraction\")\n\n# ---------------------------------------------------------------- P10\nmd('''\n## fig6s1-no-p10-motorneurons\n\n> No recorded neuron is a P10 motorneuron; no neuron comes close to one-to-one locking of its spikes\n> with P10 spikes at any delay, nor locks consistently across programs.\n''')\ncode('''\nrows = []\nfor q in D[\"p10\"]:\n    r = next(r for r in recs if r[\"prep\"] == q[\"prep\"] and r[\"bout\"] == q[\"bout\"])\n    for i, tr in enumerate(apl.neuron_trains(r)):\n        v, n = apl.p10_locking(tr, q[\"t\"])\n        rows.append({\"prep\": q[\"prep\"], \"bout\": q[\"bout\"], \"neuron\": i + 1, \"maxP\": v, \"spikes_after_33s\": n})\nMN = pd.DataFrame(rows)\nprint(\"neuron-program values:\", len(MN), \"; without spikes after 33 s:\", int(MN.maxP.isna().sum()))\nprint(\"largest maximum locking:\", round(MN.maxP.max(), 3), \"; at or above 0.9:\", int((MN.maxP >= 0.9).sum()))\ntwo = MN[MN.maxP >= 0.9].groupby([\"prep\", \"neuron\"]).size()\nprint(\"neurons at or above 0.9 in two programs:\", int((two >= 2).sum()))\nprint(\"largest values:\")\nprint(MN.sort_values(\"maxP\", ascending=False).head(8).round(3).to_string(index=False))\nfor c in (0.5, 0.7):\n    print(f\"neuron-program values at or above {c}:\", int((MN.maxP >= c).sum()))\nprint(\"per preparation, max:\", MN.groupby(\"prep\").maxP.max().round(3).to_dict())\n''', \"claim:fig6s1-no-p10-motorneurons\")\nresult(\"fig6s1-no-p10-motorneurons\")\n\nmd('''\n## fig6d-decode-p10\n\n> P10 nerve activity can be fitted and forecast from the low-dimensional trajectory in all nine\n> responses with P10 recordings, so the trajectory encodes muscle commands.\n\nAdopted width (median ISI of the recording); PCs for 80% (smallest number reaching it). The\nMethods' windowing (fit 40 s, forecast 10 s, step 1 s, from 33 s; histories 50 to 200 ms) is the\nmain reading; the code's (training on 50% of the series, 0.2 s steps, histories 50 to 250 ms) is a\nvariant. The 90% models of claim fig6s2 use the Methods' windowing with histories of 50, 100, 150 and\n200 ms only, to fit the time limit.\n''')\ncode('''\nt0 = time.time()\ndef p10_jobs(frac, windowing, hists):\n    J = []\n    for q in D[\"p10\"]:\n        i = next(i for i, r in enumerate(recs) if r[\"prep\"] == q[\"prep\"] and r[\"bout\"] == q[\"bout\"])\n        J.append((recs[i], q[\"t\"], float(sds[\"own\"][i]), frac, windowing, hists))\n    return J\nDEC = {(\"80\", \"methods\"): apl.run_decoding(p10_jobs(0.8, \"methods\", apl.HISTORIES_METHODS)),\n       (\"80\", \"code\"): apl.run_decoding(p10_jobs(0.8, \"code\", apl.HISTORIES_CODE)),\n       (\"90\", \"methods\"): apl.run_decoding(p10_jobs(0.9, \"methods\", [5, 10, 15, 20]))}\nprint(f\"decoding in {time.time() - t0:.0f} s\")\ndef dec_table(res, hists=None):\n    rows = []\n    for o in res:\n        if hists is None:\n            R = np.array([w[\"R\"] for w in o[\"windows\"]]); MAE = np.array([w[\"MAE\"] for w in o[\"windows\"]]); best = o[\"best\"]\n        else:\n            best = min(hists, key=lambda h: np.nanmean(o[\"by_history\"][h][1]))\n            R, MAE = o[\"by_history\"][best]\n        ok = np.isfinite(R)\n        sem = np.nanstd(R, ddof=1) / np.sqrt(ok.sum())\n        rows.append({\"prep\": o[\"prep\"], \"bout\": o[\"bout\"], \"dims\": o[\"d\"], \"history_ms\": best * 10, \"windows\": len(R),\n                     \"undefined_R\": int((~ok).sum()), \"mean_R\": np.nanmean(R), \"mean_R_minus_2sem\": np.nanmean(R) - 2 * sem,\n                     \"mean_R2\": np.nanmean(R ** 2), \"mean_MAE\": np.nanmean(MAE),\n                     \"train_R\": np.nanmean([w[\"R_train\"] for w in o[\"windows\"]]) if hists is None else np.nan})\n    return pd.DataFrame(rows)\nfor name, res, h in [(\"Methods windowing, 80%\", DEC[(\"80\", \"methods\")], None),\n                     (\"variant: histories up to 100 ms\", DEC[(\"80\", \"methods\")], list(range(5, 11))),\n                     (\"variant: code windowing\", DEC[(\"80\", \"code\")], None)]:\n    T = dec_table(res, h)\n    print(f\"\\\\n{name}: responses with mean R - 2 s.e.m. > 0: {int((T.mean_R_minus_2sem > 0).sum())} of 9; windows in all {T.windows.sum()}\")\n    print(T.round(3).to_string(index=False))\n''', \"claim:fig6d-decode-p10\")\nresult(\"fig6d-decode-p10\")\n\nmd('''\n## fig6s2-dimensions-p10\n\n> The nine recordings with P10 activity need only 3 to 5 embedding dimensions for 80% variance, and\n> at least double that for 90%; using the 90% dimensions does not improve the P10 forecasts.\n''')\ncode('''\np10_idx = [next(i for i, r in enumerate(recs) if r[\"prep\"] == q[\"prep\"] and r[\"bout\"] == q[\"bout\"]) for q in D[\"p10\"]]\nrows = []\nfor mode in [\"sqrt12\", \"twelve\", \"own\", \"pooled\"]:\n    evs = [apl.Program(recs[i], sds[mode][i]).ev for i in p10_idx]\n    for rule in [\"min80\", \"le80\"]:\n        d80 = np.array([apl.n_pcs(ev, 0.8, rule) for ev in evs])\n        d90 = np.array([apl.n_pcs(ev, 0.9, rule) for ev in evs])\n        rows.append({\"sd\": mode, \"count\": rule, \"d80\": d80.tolist(), \"d90\": d90.tolist(),\n                     \"all_in_2.7_to_5.5\": bool(np.all((d80 >= 2.7) & (d80 <= 5.5))), \"d90_at_least_2x\": bool(np.all(d90 >= 2 * d80))})\nprint(pd.DataFrame(rows).to_string(index=False))\nT80 = dec_table(DEC[(\"80\", \"methods\")]); T90 = dec_table(DEC[(\"90\", \"methods\")])\ncmp = pd.DataFrame({\"prep\": T80.prep, \"bout\": T80.bout, \"dims80\": T80.dims, \"dims90\": T90.dims,\n                    \"MAE80\": T80.mean_MAE, \"MAE90\": T90.mean_MAE, \"R2_80\": T80.mean_R2, \"R2_90\": T90.mean_R2})\nprint(cmp.round(3).to_string(index=False))\nw_mae = stats.wilcoxon(cmp.MAE90, cmp.MAE80)\nw_r2 = stats.wilcoxon(cmp.R2_90, cmp.R2_80)\nprint(\"Wilcoxon signed-rank, MAE 90% against 80%: p =\", round(w_mae.pvalue, 4), \"; 90% lower in\", int((cmp.MAE90 < cmp.MAE80).sum()), \"of 9;\",\n      \"median difference\", round(float(np.median(cmp.MAE90 - cmp.MAE80)), 3))\nprint(\"Wilcoxon signed-rank, R2 90% against 80%: p =\", round(w_r2.pvalue, 4), \"; 90% higher in\", int((cmp.R2_90 > cmp.R2_80).sum()), \"of 9;\",\n      \"median difference\", round(float(np.median(cmp.R2_90 - cmp.R2_80)), 3))\n''', \"claim:fig6s2-dimensions-p10\")\nresult(\"fig6s2-dimensions-p10\")\n\n# ---------------------------------------------------------------- participation\nmd('''\n## Participation\n\nPer program, from its own PCA under the adopted width; d is (a) the program's own count for 80%\n(Methods) or (b) the count from the PCA of the three programs concatenated, at most 80%, used for\nall three (code). Normalised to the program's maximum.\n''')\ncode('''\nprogs = [apl.Program(r, s, \"min80\") for r, s in zip(recs, sds[\"own\"])]\nPART = {}\nfor reading in [\"a_own\", \"b_common\"]:\n    for p in range(1, 11):\n        ix = sorted([i for i, r in enumerate(recs) if r[\"prep\"] == p], key=lambda i: recs[i][\"bout\"])\n        if reading == \"b_common\":\n            _, _, evc = apl.pca(np.vstack([progs[i].sdf[progs[i].ix_stim] for i in ix]))\n            ds = [apl.n_pcs(evc, 0.8, \"le80\")] * 3\n        else:\n            ds = [apl.n_pcs(progs[i].ev, 0.8, \"min80\") for i in ix]\n        PART[(reading, p)] = (np.array([apl.participation(progs[i].coeffs, progs[i].ev, d)[1] for i, d in zip(ix, ds)]), ds)\nprint({k: v[1] for k, v in PART.items()})\n''')\n\nmd('''\n## fig7a-long-tailed-participation\n\n> Every response has a long-tailed distribution of single-neuron participation, a minority of\n> neurons dominating its dynamics.\n''')\ncode('''\nrows = []\nfor (reading, p), (P, ds) in PART.items():\n    for b in range(3):\n        rows.append({\"reading\": reading, \"prep\": p, \"bout\": b + 1, \"skew\": stats.skew(P[b]), \"frac_over_half\": np.mean(P[b] > 0.5),\n                     \"median\": np.median(P[b])})\nPA = pd.DataFrame(rows)\nprint(PA.groupby(\"reading\").apply(lambda d: pd.Series({\"skew_positive\": int((d.skew > 0).sum()), \"skew_min\": d.skew.min(),\n      \"frac_over_half_below_0.5\": int((d.frac_over_half < 0.5).sum()), \"frac_over_half_max\": d.frac_over_half.max(),\n      \"median_participation_median\": d[\"median\"].median()})).round(3).to_string())\nprint(PA[PA.reading == \"a_own\"].round(3).to_string(index=False))\n''', \"claim:fig7a-long-tailed-participation\")\nresult(\"fig7a-long-tailed-participation\")\n\nmd('''\n## fig7f-strongly-variable-neurons\n\n> Neurons with high participation in one response often have low participation in another; every\n> preparation contains neurons whose change in participation well exceeds that predicted by a\n> noise model.\n''')\ncode('''\nrows = []\nfor (reading, p), (P, ds) in PART.items():\n    dP = np.column_stack([P[0] - P[1], P[1] - P[2], P[0] - P[2]])\n    mx = np.abs(dP[:, :2]).max(1)\n    for pool in [\"all_pairs\", \"consecutive\"]:\n        data = dP.ravel(order=\"F\") if pool == \"all_pairs\" else dP[:, :2].ravel(order=\"F\")\n        mu, sd, nout = apl.iterate_outliers(data)\n        thr = max(abs(mu - 3 * sd), abs(mu + 3 * sd))\n        nv = int((mx >= thr).sum())\n        rows.append({\"reading\": reading, \"pool\": pool, \"prep\": p, \"neurons\": P.shape[1], \"mu\": mu, \"sd\": sd, \"dropped\": nout,\n                     \"threshold\": thr, \"strongly_variable\": nv, \"proportion\": nv / P.shape[1]})\nSV = pd.DataFrame(rows)\nprint(SV.groupby([\"reading\", \"pool\"]).apply(lambda d: pd.Series({\"preps_with_one\": int((d.strongly_variable > 0).sum()),\n      \"min_count\": d.strongly_variable.min(), \"proportion_range\": f\"{d.proportion.min():.3f} to {d.proportion.max():.3f}\"})).to_string())\nprint(SV.round(4).to_string(index=False))\n''', \"claim:fig7f-strongly-variable-neurons\")\nresult(\"fig7f-strongly-variable-neurons\")\n\nmd('''\n## halving-participation\n\n> Even the most strongly participating neurons in a response could more than halve their\n> participation in other evoked responses.\n''')\ncode('''\nrows = []\nfor (reading, p), (P, ds) in PART.items():\n    for sel_name in [\"top_neuron\", \"top_10pct\"]:\n        hit, examples = False, []\n        for a in range(3):\n            sel = [int(np.argmax(P[a]))] if sel_name == \"top_neuron\" else list(np.argsort(P[a])[::-1][:int(np.ceil(0.1 * P.shape[1]))])\n            for b in range(3):\n                if b == a:\n                    continue\n                lo = [n for n in sel if P[b][n] < 0.5 * P[a][n]]\n                if lo:\n                    hit = True\n                    examples.append((a + 1, b + 1, len(lo), round(float(min(P[b][n] / P[a][n] for n in lo)), 3)))\n        rows.append({\"reading\": reading, \"selection\": sel_name, \"prep\": p, \"halves\": hit, \"examples\": examples[:3]})\nHV = pd.DataFrame(rows)\nprint(HV.groupby([\"reading\", \"selection\"]).halves.sum().to_string())\nprint(HV[HV.reading == \"a_own\"].to_string(index=False))\n''', \"claim:halving-participation\")\nresult(\"halving-participation\")\n\nmd('''\n## fig7s1-rate-synchrony\n\n> A neuron's participation reflects both its firing rate and its synchrony; firing rate explains on\n> average 50% of the variation in participation within a response, and rate changes 23% of the\n> change in participation between responses.\n''')\ncode('''\nrows = []\nfor reading in [\"a_own\", \"b_common\"]:\n    for rate_from in [32.5, 30.0]:\n        r2, dr2, dr2_code = [], [], []\n        for p in range(1, 11):\n            ix = sorted([i for i, r in enumerate(recs) if r[\"prep\"] == p], key=lambda i: recs[i][\"bout\"])\n            P = PART[(reading, p)][0]\n            rates = np.array([[np.sum(tr >= rate_from) / (progs[i].t_end - rate_from) for tr in progs[i].trains] for i in ix])\n            r2 += [np.corrcoef(P[b], rates[b])[0, 1] ** 2 for b in range(3)]\n            dR = np.column_stack([rates[0] - rates[1], rates[0] - rates[2], rates[1] - rates[2]])\n            dPm = np.column_stack([P[0] - P[1], P[0] - P[2], P[1] - P[2]])\n            dPc = np.column_stack([P[0] - P[1], P[1] - P[2], P[0] - P[2]])\n            dr2 += [np.corrcoef(dR[:, c], dPm[:, c])[0, 1] ** 2 for c in range(3)]\n            dr2_code += [np.corrcoef(dR[:, c], dPc[:, c])[0, 1] ** 2 for c in range(3)]\n        rows.append({\"reading\": reading, \"rate_from_s\": rate_from, \"mean_R2_within\": np.mean(r2), \"range_within\": f\"{min(r2):.2f} to {max(r2):.2f}\",\n                     \"mean_R2_change_matched\": np.mean(dr2), \"mean_R2_change_code_pairing\": np.mean(dr2_code), \"n_programs\": len(r2), \"n_pairs\": len(dr2)})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n''', \"claim:fig7s1-rate-synchrony\")\nresult(\"fig7s1-rate-synchrony\")\n\nmd('''\n## fig7gh-robust-to-participation\n\n> The distance between a pair of responses does not correlate with the total change in neuron\n> participation between them nor with the distance between their participation distributions; the\n> program is robust to the participation of single neurons.\n''')\ncode('''\nrows = []\nfor k in [\"own/min80\", \"pooled/le80\"]:\n    for ps in [\"recurrent\", \"code\"]:\n        T = haus_table(k, \"prog1\", ps)\n        T[\"norm_dist\"] = T.H / T.ctrl_mean\n        for reading in [\"a_own\", \"b_common\"]:\n            tc, hd = [], []\n            for row in T.itertuples():\n                P = PART[(reading, row.prep)][0]\n                i, j = [int(x) - 1 for x in row.pair.split(\",\")]\n                tc.append(np.abs(P[i] - P[j]).sum())\n                hd.append(apl.hellinger(P[i], P[j]))\n            T[\"total_change\"], T[\"hellinger\"] = tc, hd\n            keep = ~((T.prep == 4) & T.pair.isin([\"1,2\", \"1,3\"]))\n            for x in [\"total_change\", \"hellinger\"]:\n                X = sm.add_constant(T.loc[keep, x]); y = T.loc[keep, \"norm_dist\"]\n                ols = sm.OLS(y, X).fit()\n                rob = sm.RLM(y, X, M=sm.robust.norms.TukeyBiweight()).fit()\n                ck = T.norm_dist < 1\n                ols_code = sm.OLS(T.loc[ck, \"norm_dist\"], sm.add_constant(T.loc[ck, x])).fit()\n                rows.append({\"reading\": k, \"points\": ps, \"participation\": reading, \"x\": x, \"n\": int(keep.sum()),\n                             \"slope\": ols.params.iloc[1], \"p\": ols.pvalues.iloc[1], \"R2\": ols.rsquared,\n                             \"robust_slope\": rob.params.iloc[1], \"robust_p\": rob.pvalues.iloc[1],\n                             \"code_exclusion_n\": int(ck.sum()), \"code_exclusion_p\": ols_code.pvalues.iloc[1]})\nRB = pd.DataFrame(rows)\nprint(RB.round(4).to_string(index=False))\n''', \"claim:fig7gh-robust-to-participation\")\nresult(\"fig7gh-robust-to-participation\")\n\nmd(RESULTS.get(\"fig7s2\", \"## fig7s2-no-invariant-core\\n\\nplaceholder\"))\n\nmd('''\n## fig8-caudolateral\n\n> Neurons with strong participation across the three responses, and those with highly variable\n> participation, lie mainly in the caudo-lateral quadrant of the ganglion.\n\nBlocked (see the header): neither the data set, its documentation nor the paper's text says which\ndirections of the array's x and y axes are caudal and lateral. The counts by quadrant of the array\ncoordinates are shown so that the claim can be judged once the orientation is known; they decide\nnothing here.\n''')\ncode('''\nrows = []\nfor side, group in [(\"left\", [1, 2, 4, 10]), (\"right\", [3, 5, 6, 9])]:\n    vals_max, vals_rng, xs, ys = [], [], [], []\n    for p in group:\n        P = PART[(\"a_own\", p)][0]\n        vals_max.append(P.max(0)); vals_rng.append(P.max(0) - P.min(0))\n        xs.append(D[\"coords\"][p - 1][\"x\"]); ys.append(D[\"coords\"][p - 1][\"y\"])\n    allmax = np.concatenate([PART[(\"a_own\", p)][0].max(0) for p in [1, 2, 3, 4, 5, 6, 9, 10]])\n    allrng = np.concatenate([np.ptp(PART[(\"a_own\", p)][0], 0) for p in [1, 2, 3, 4, 5, 6, 9, 10]])\n    x, y = np.concatenate(xs), np.concatenate(ys)\n    cx, cy = 25.0, 25.0     # centre of the 501 x 501 template, in coordinate units\n    for name, v, allv in [(\"max\", np.concatenate(vals_max), allmax), (\"range\", np.concatenate(vals_rng), allrng)]:\n        edges = np.linspace(allv.min(), allv.max(), 6)\n        top = v >= edges[-2]\n        q = np.where(x >= cx, \"x+\", \"x-\").astype(object) + np.where(y >= cy, \"y+\", \"y-\")\n        counts = pd.Series(q[top]).value_counts().to_dict()\n        rows.append({\"side\": side, \"measure\": name, \"neurons\": v.size, \"top_fifth\": int(top.sum()), \"by_quadrant\": counts})\nprint(pd.DataFrame(rows).to_string(index=False))\n''')\n\nmd(RESULTS.get(\"summary\", \"## Summary\\n\\nplaceholder\"))\n\ncode('''\nprint(f\"notebook run time {(time.time() - started) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB (main process)\")\n''')\n\nnb = nbformat.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbformat.write(nb, OUT)\nprint(\"wrote\", OUT, len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python build.py && cd entries/crcns-apl-1-bruno-2017 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir $TMPDIR/exec --output run1.ipynb reproduce_bruno_2017.ipynb 2>&1 | tail -20; date -u
```

```
wrote entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb 76 cells
[32m   (...)[39m[32m   1450[39m [33;03m        data after applying f[39;00m
[32m   1451[39m [33;03m    """[39;00m
[32m-> [39m[32m1452[39m     values, mutated = [30;43mself[39;49m[30;43m.[39;49m[30;43m_grouper[39;49m[30;43m.[39;49m[30;43mapply_groupwise[39;49m[30;43m([39;49m[30;43mf[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdata[39;49m[30;43m)[39;49m
[32m   1453[39m     [38;5;28;01mif[39;00m not_indexed_same [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
[32m   1454[39m         not_indexed_same = mutated

[36mFile [39m[32m/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/groupby/ops.py:1207[39m, in [36mBaseGrouper.apply_groupwise[39m[34m(self, f, data)[39m
[32m   1205[39m [38;5;66;03m# group might be modified[39;00m
[32m   1206[39m group_axes = group.axes
[32m-> [39m[32m1207[39m res = [30;43mf[39;49m[30;43m([39;49m[30;43mgroup[39;49m[30;43m)[39;49m
[32m   1208[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m mutated [38;5;129;01mand[39;00m [38;5;129;01mnot[39;00m _is_indexed_like(res, group_axes):
[32m   1209[39m     mutated = [38;5;28;01mTrue[39;00m

[36mCell[39m[36m [39m[32mIn[32][39m[32m, line 7[39m, in [36m<lambda>[39m[34m(d)[39m
[32m----> [39m[32m7[39m print(PA.groupby("reading").apply(lambda d: pd.Series({"skew_positive": int((d.skew > 0).sum()), "skew_min": d.skew.min(),
[32m      8[39m       [33m"frac_over_half_below_0.5"[39m: int((d.frac_over_half < [32m0.5[39m).sum()), [33m"frac_over_half_max"[39m: d.frac_over_half.max(),
[32m      9[39m       [33m"median_participation_median"[39m: d[[33m"median"[39m].median()})).round([32m3[39m).to_string())

[31mTypeError[39m: '>' not supported between instances of 'method' and 'int'
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/"skew": stats.skew(P\[b\])/"skewness": stats.skew(P[b])/; s/int((d.skew > 0).sum()), "skew_min": d.skew.min()/int((d.skewness > 0).sum()), "skew_min": d.skewness.min()/' build.py && . dev/bin/activate && python build.py >/dev/null && cd entries/crcns-apl-1-bruno-2017 && OMP_NUM_THREADS=1 python - <<'EOF'
import nbformat, pickle, os
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
src=[c.source for c in nb.cells if c.cell_type=='code']
# find cells
i0=next(i for i,s in enumerate(src) if s.startswith('progs = [apl.Program'))
ihaus=next(i for i,s in enumerate(src) if 'def haus_table' in s)
g={}
exec(src[0], g)
exec("sds = apl.gaussian_sds(recs)\nimport pickle,os\nman=pickle.load(open(os.environ['TMPDIR']+'/man.pkl','rb'))\nMAN={f'{a}/{b}':v for (a,b),v in man.items()}\nADOPT='own/min80'", g)
hs=src[ihaus].split('def haus_table',1)[1]; exec('def haus_table'+hs, g)
for s in src[i0:]:
    exec(s, g)
EOF
```

```
CRCNS data set apl-1, version unversioned; read 5 files from https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/ in 2 s
{('a_own', 1): [7, 7, 8], ('a_own', 2): [4, 5, 5], ('a_own', 3): [8, 7, 7], ('a_own', 4): [5, 4, 5], ('a_own', 5): [5, 5, 6], ('a_own', 6): [6, 5, 6], ('a_own', 7): [7, 6, 8], ('a_own', 8): [5, 6, 7], ('a_own', 9): [6, 6, 6], ('a_own', 10): [6, 6, 7], ('b_common', 1): [8, 8, 8], ('b_common', 2): [6, 6, 6], ('b_common', 3): [10, 10, 10], ('b_common', 4): [5, 5, 5], ('b_common', 5): [8, 8, 8], ('b_common', 6): [6, 6, 6], ('b_common', 7): [8, 8, 8], ('b_common', 8): [7, 7, 7], ('b_common', 9): [6, 6, 6], ('b_common', 10): [7, 7, 7]}
          skew_positive  skew_min  frac_over_half_below_0.5  frac_over_half_max  median_participation_median
reading                                                                                                     
a_own              30.0     0.498                      30.0               0.394                        0.245
b_common           30.0     0.495                      30.0               0.404                        0.250
reading  prep  bout  skewness  frac_over_half  median
  a_own     1     1     1.119           0.110   0.290
  a_own     1     2     1.635           0.066   0.279
  a_own     1     3     2.509           0.022   0.236
  a_own     2     1     2.372           0.019   0.166
  a_own     2     2     2.394           0.029   0.158
  a_own     2     3     1.640           0.048   0.209
  a_own     3     1     0.897           0.238   0.354
  a_own     3     2     1.002           0.169   0.309
  a_own     3     3     1.240           0.069   0.242
  a_own     4     1     1.251           0.060   0.215
  a_own     4     2     1.074           0.146   0.277
  a_own     4     3     1.173           0.179   0.332
  a_own     5     1     0.537           0.223   0.394
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600 --output-dir $TMPDIR/exec --output run2.ipynb reproduce_bruno_2017.ipynb 2>&1 | tail -3; date -u
```

```
[NbConvertApp] Converting notebook reproduce_bruno_2017.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 245201 bytes to /tmp/claude-1001/exec/run2.ipynb

real	18m2.751s
user	55m22.903s
sys	1m28.898s
Sun Nov  8 13:38:17 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF' > $TMPDIR/out2.txt
import json
nb=json.load(open('exec/run2.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': 
        print(f'---- [{i}] MD', c['source'][:80] if isinstance(c['source'],str) else ''.join(c['source'])[:80]); continue
    print(f'==== [{i}] tags={c["metadata"].get("tags")}')
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text']))
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
        elif 'text/plain' in o.get('data',{}): print(''.join(o['data']['text/plain'])[:300])
EOF
wc -c $TMPDIR/out2.txt; grep -n "ERROR" $TMPDIR/out2.txt
```

```
85170 /tmp/claude-1001/out2.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out2.txt",
 "limit": 330
}
```

```
1	---- [0] MD # Header placeholder
2	==== [1] tags=None
3	CRCNS data set apl-1, version unversioned; read 5 files from https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/ in 2 s
4	
5	---- [2] MD ## Data check
6	
7	Each check of the description against the values is stated under 
8	==== [3] tags=['sanity']
9	MD5 of each file read, against the data set's checksums.md5:
10	  FileTable.mat            27437d5d4063cd9827f1f1ffa67f36d4  matches
11	  SpikeData.mat            8657665316d5006677891922bdd0a1d8  matches
12	  ExtracellularData.mat    d01451b227a6c4a0dc2a620bd9bbbcf9  matches
13	  Coordinates.mat          53a98c4b9f2a35be299180699321ad16  matches
14	  diode_template.mat       a94b5040b265b276e2b0ef684277f2ad  matches
15	
16	Recordings per preparation: {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3}
17	 prep  bout             file  Bout_field  neurons  max_id  spikes  first_spike_s  last_spike_s  neurons_spiking_after_30s
18	    1     1  Jun0214da01.mat           1      136     136   23681          0.021        122.72                        136
19	    1     2  Jun0214da02.mat           2      136     136   25768          0.001        122.72                        136
20	    1     3  Jun0214da03.mat           3      136     136   27178          0.018        122.72                        136
[... 310 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out2.txt",
 "offset": 330,
 "limit": 400
}
```

```
330	
331	adopted reading, per recording:
332	 prep  bout  d  n_peaks  prop_recurrent  period_mean  period_median
333	    1     1  7        4           0.842       14.977         15.240
334	    1     2  7        2           0.823       17.281         17.710
335	    1     3  8        4           0.817       14.144         13.650
336	    2     1  4        2           0.722       12.211         10.570
337	    2     2  5        2           0.788       15.156         12.750
338	    2     3  5        1           0.907       14.764         15.860
339	    3     1  8        2           0.695       10.143         10.270
340	    3     2  7        2           0.748       11.489         11.830
341	    3     3  7        1           0.784       12.972         12.350
342	    4     1  5        1           0.595       10.785          9.870
343	    4     2  4        1           0.822       14.980         14.690
344	    4     3  5        1           0.633       13.330         13.860
345	    5     1  5        2           0.912       12.001         11.780
346	    5     2  5        1           0.862       12.142         12.050
347	    5     3  6        2           0.924       11.395         11.070
348	    6     1  6        1           0.972        9.408          9.260
349	    6     2  5        1           0.909        9.808          9.060
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out2.txt",
 "offset": 760,
 "limit": 420
}
```

```
760	 pearson     6  1,2 0.866          0.334           0.511
761	 pearson     6  1,3 0.862          0.334           0.514
762	 pearson     6  2,3 0.926          0.511           0.514
763	 pearson     7  1,2 0.860          0.634           0.747
764	 pearson     7  1,3 0.685          0.634           0.779
765	 pearson     7  2,3 0.751          0.747           0.779
766	 pearson     8  1,2 0.868          0.597           0.538
767	 pearson     8  1,3 0.866          0.597           0.583
768	 pearson     8  2,3 0.815          0.538           0.583
769	 pearson     9  1,2 0.931          0.352           0.312
770	 pearson     9  1,3 0.814          0.352           0.357
771	 pearson     9  2,3 0.820          0.312           0.357
772	 pearson    10  1,2 0.840          0.412           0.409
773	 pearson    10  1,3 0.811          0.412           0.374
774	 pearson    10  2,3 0.887          0.409           0.374
775	
776	---- [37] MD ## fig3h-perturbations-return
777	
778	> Of 19 spontaneous divergences from the trajecto
779	==== [38] tags=['claim:fig3h-perturbations-return']
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build.py').read()
s=s.replace('''print("by preparation, mean period:", S.groupby("prep").period_mean.mean().round(2).to_dict())''','''print("by preparation, mean period:", S.groupby("prep").period_mean.mean().round(2).to_dict())
print("adopted reading, quartiles of the dominant period (mean of the peak):", np.percentile(S.period_mean, [25, 75]).round(2),
      "; outside 9 to 16.5 s:", S[~S.period_mean.between(9, 16.5)][["prep", "bout", "period_mean"]].round(2).values.tolist())''')
open('build.py','w').write(s)
EOF
grep -n "quartiles" build.py | head -2; date -u
```

```
355:print("adopted reading, quartiles of the dominant period (mean of the peak):", np.percentile(S.period_mean, [25, 75]).round(2),
Sun Nov  8 13:39:47 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-apl-1-bruno-2017 && python -c "
import pickle,os,numpy as np,pandas as pd,apl
res=pickle.load(open(os.environ['TMPDIR']+'/res_c.pkl','rb'))
S=pd.DataFrame([apl.summarise(o) for o in res[('own','min80')]])
print(np.percentile(S.period_mean,[25,75]).round(2), S[~S.period_mean.between(9,16.5)][['prep','bout','period_mean']].round(2).values.tolist())
"
```

```
[11.06 14.98] [[1.0, 2.0, 17.28], [7.0, 1.0, 22.23], [7.0, 2.0, 8.75], [8.0, 1.0, 19.94]]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/results.py",
 "content": "import json\n\nR = {}\nR[\"header\"] = \"\"\"# Reproducing Bruno, Frost & Humphries (2017) from CRCNS data set apl-1\n\n**Paper.** Bruno AM, Frost WN, Humphries MD (2017). A spiral attractor network drives rhythmic\nlocomotion. *eLife* 6:e27342. [doi:10.7554/elife.27342](https://doi.org/10.7554/elife.27342). The\nclaims file was written from the version of record (PMC5546814): main text, Materials and methods\nand all figure legends and supplement legends.\n\n**Data set.** CRCNS apl-1, [doi:10.6080/K0SN074B](https://doi.org/10.6080/K0SN074B), streamed from\nthe public bucket `crcnsarchive` under `apl-1/live/`. Version: `unversioned`. CRCNS data sets carry\nno versions (docs/archives.md), and the bucket holds one copy of the processed files (`live/`; the\n`orig/` folder holds only one raw optical file). That copy is pinned by the MD5 sums printed in the\ndata check, which match the data set's `checksums.md5`. The paper cites the data set's DOI and no\nversion. Files read: FileTable.mat, SpikeData.mat, ExtracellularData.mat, Coordinates.mat and\ndiode_template.mat; the 6.9 GB raw optical archive is not needed.\n\n**Method.** The claims file decides what is tested. Where it leaves a detail open, the detail is\ntaken from the paper's Methods or from its code (github.com/mdhumphries/AplysiaAttractorAnalysis at\ncommit e5f28e98), cited in `apl.py`. Two details recur in almost every claim: the width of the\nGaussian kernel and the rule for the number of PCs. Each is run under every reading the criteria\nlist. Where one reading has to be chosen, the adopted reading is `own/min80`: the median ISI of the\nrecording, after onset, as the kernel SD, and the smallest number of PCs reaching 80% of the\nvariance. Outcomes that rest on this choice are marked as assumed in the record.\n\n| Claim | Tested or blocked |\n|---|---|\n| dataset-size, fig1d-slow-oscillation, fig1e-decaying-rate, fig2b-dimensions | tested |\n| fig2ef-periodic-recurrence, fig2e-single-dominant-orbit, fig2s2-threshold-robust, fig3a-coalescence | tested |\n| fig3c-same-manifold, fig3s1a-common-axes, fig3d-initial-conditions, fig3f-pairwise-similarity | tested |\n| fig3h-perturbations-return, fig3i-same-manifold-after | tested |\n| fig4bc-stable-spiral, fig4c-orbital-period, fig4s1a-contracting-dimensions, fig4s1b-rotation-dominant | tested |\n| fig5b-period-changes, fig5c-no-relation-contraction | tested |\n| fig6s1-no-p10-motorneurons, fig6d-decode-p10, fig6s2-dimensions-p10 | tested |\n| fig7a-long-tailed-participation, fig7f-strongly-variable-neurons, halving-participation, fig7s1-rate-synchrony, fig7gh-robust-to-participation | tested |\n| fig7s2-no-invariant-core | blocked: not runnable (the ensemble toolbox is MATLAB) |\n| fig8-caudolateral | blocked: metadata insufficient (orientation of the array not given) |\n\"\"\"\n\nR[\"datacheck\"] = \"\"\"**Checks of the description against the data.** Consistent with the description: 30\nrecordings, three per preparation; 75 to 160 neurons per preparation, 1131 in all; the stimulus at\n30 to 32.5 s (in every recording the population rate during the stimulus is 2.6 to 11 times the rate\nbefore it, and the rate after 32.5 s exceeds the rate before 30 s in 30 of 30); recordings end at\n122.7 s; P10 spikes in nine recordings of preparations 2, 4 and 5 (FileTable lists bouts 1 to 3 for\nthose three). The P10 intervals are multiples of 0.614 ms, a sampling rate of 1629.7 Hz, which\nagrees with the description's 1630 Hz and not with the paper's 1600 Hz. The P10 files of\npreparation 2 are named `Jun0414`, its spike file `Jun0414B`; they are matched on the first seven\ncharacters, as the code does. No neuron spike train and no recording appears twice.\n\nThe P10 rate and the population rate are correlated after the stimulus at lags of 0 to 5 s in every\nP10 recording; in 7 of 9 the largest correlation exceeds the 95th percentile of circularly shifted\nseries. This is consistent with a shared clock; the lag of a few seconds is expected for a nerve\nthat fires in one phase of a 10 s cycle, so it does not show the clocks agree to better than a few\nseconds. In Jun1114da01 and Jun1114da02 the check does not separate the data from shifted series.\n\nThe description says the recordings were concatenated before spike sorting, so that a neuron id\nnames the same neuron in all three bouts. Consistent with this, per-neuron spike counts after onset\ncorrelate between bouts of a preparation (Spearman 0.63 to 0.96) above the 95th percentile of\npermuted ids in 30 of 30 pairs. This is taken as an assumption for the participation claims, which\ncompare neurons across bouts; their results are given per preparation and bout.\n\nCoordinates hold one (x, y) per neuron, on a 0 to 50 scale (plot_maps.m multiplies by 10 to plot\nthem on the 501 by 501 diode template). Preparations 7 and 8 are marked unreliable, as the\ndescription says, and preparation 7 has 5 missing positions. No unit is given, and nothing in the\nfiles or the documentation says which direction of x or y is rostral, caudal, medial or lateral.\"\"\"\n\nR[\"dataset-size\"] = \"\"\"**Result: partially reproduced.** The counts match: 10 preparations, 30 recordings and 1131\nneurons. The range does not: recordings hold 75 to 160 neurons, and only 12 of 30 lie in 108 to 198\n(the paper's 120 to 180 widened by 10%). Counting only neurons that spike after onset changes\nnothing (75 to 160, 1131). The paper's range cannot hold with its own total: ten preparations of at\nleast 120 neurons would hold at least 1200.\"\"\"\n\nR[\"fig1d-slow-oscillation\"] = \"\"\"**Result: reproduced.** The grand mean spectrum's power-weighted peak is at 0.0486 Hz, and\nthe peaks of all 30 recordings lie above 0 and at or below 0.11 Hz (0.0131 to 0.0789 Hz). The\nvariant, the frequency of maximum power above 0 Hz, lies at 0.0076 to 0.0992 Hz, also 30 of 30 at or\nbelow 0.11 Hz.\"\"\"\n\nR[\"fig1e-decaying-rate\"] = \"\"\"**Result: reproduced.** Under reading (a), all 30 responses are decreasing (Pearson R of\nwindow time against count from -0.992 to -0.774, all below -0.2) and none is increasing; under\nreading (b) all 30 slopes are negative. Every preparation has three decreasing responses.\"\"\"\n\nR[\"fig2b-dimensions\"] = \"\"\"**Result: reproduced, under the readings with the code's width and the code's count.** With\nthe median ISI as the SD and the count of PCs whose cumulative variance is at most 80% (own/le80),\n28 of 30 counts lie in 3.6 to 8.8 (3 to 7) and the number of neurons divided by the count exceeds\n10 in all 30 (lowest 10.7); pooled/le80 gives the same. With the Methods' count (smallest number\nreaching 80%) the counts are 4 to 8 for own/min80, the paper's range, all 30 in 3.6 to 8.8, but the\nratio exceeds 10 in 29 of 30 (lowest 9.4, 75 neurons and 8 PCs). The Methods' printed width (median\nISI / 12, or / sqrt(12)) gives 22 to 76 dimensions and ratios of 1.8 to 2.8 at the lowest; it\ncannot give the paper's counts.\"\"\"\n\nR[\"fig2ef-periodic-recurrence\"] = \"\"\"**Result: reproduced.** Under the adopted reading, 26 of 30 dominant periods (mean of the\npeak) lie in 9 to 16.5 s, and 4 do not (17.28, 22.23, 8.75 and 19.94 s); the quartiles are 11.06\nand 14.98 s. With the median of the peak 23 of 30 do. All four readings with the code's width give\n22 to 26 of 30, and so do the readings with the narrow widths except twelve/le80 with the mean (13\nof 30); every reading but that one meets the criterion.\"\"\"\n\nR[\"fig2e-single-dominant-orbit\"] = \"\"\"**Result: reproduced.** Under the adopted reading, 29 of 30 responses have more than 50% of\ntheir recurrent points (delays of 5 to 50 s) in the dominant peak, and 27 of 30 counting all\nrecurrent points (the code's propInMaxPeriod). Responses have 1 to 4 peaks, as the Methods say;\n12 have one. The other readings give 29 to 30 and 24 to 27.\"\"\"\n\nR[\"fig2s2-threshold-robust\"] = \"\"\"**Result: reproduced.** Under every reading, the dominant periods at the 5% and 2%\nthresholds correlate with those at 10% (Spearman 0.70 to 0.97, all p < 2e-5), so reading (a) holds\nfor both lower thresholds. Reading (b) holds at 5% in every case and fails at 2% in five of eight\ncases (median absolute difference 1.30 s against 1.27 s for the adopted reading with the mean).\"\"\"\n\nR[\"fig3a-coalescence\"] = \"\"\"**Result: not reproduced.** Under the adopted reading, the coalescence time is within one\ndominant period of stimulation onset in 12 of 30 responses (18 of 30 measured from offset), where\nthe criterion asks for 27; the other readings give 11 to 14 (16 to 20 from offset). Coalescence\ncomes 7.5 to 49.5 s after onset (median 14.5 s). The second part holds: after coalescence more than\n50% of the points recur in 30 of 30 responses (60.8% to 98.6%, median 86%). Because the checked\npoints start at 35 s, the earliest possible coalescence is 7.5 s after onset, close to the shortest\nperiods (8.7 to 9.4 s).\"\"\"\n\nR[\"fig3c-same-manifold\"] = \"\"\"**Result: reproduced.** With the code's point sets, 28 of 30 pairs are closer than their\nrandom-projection control under every reading, and the two that fail are pairs (1,2) and (1,3) of\npreparation 4, as the paper names them (distance 1.19 and 1.17 times the control under the adopted\nreading). With the recurrent points (the Methods), 29 of 30 pass under every reading and only pair\n(1,2) of preparation 4 fails (1.04 times the control). The control's 2 s.e.m. is 0.11 to 0.36,\nsmall against the differences.\"\"\"\n\nR[\"fig3s1a-common-axes\"] = \"\"\"**Result: reproduced.** On common axes (5 to 10 PCs), 28 of 30 pairs pass with the code's\npoint sets (failing: preparation 4, pairs (1,2) and (1,3)) under three readings, and 27 under\nown/le80 (also preparation 8, pair (2,3), at 0.99 of its control in the adopted reading's table).\nWith the recurrent points all 30 pass under every reading.\"\"\"\n\nR[\"fig3d-initial-conditions\"] = \"\"\"**Result: reproduced.** In 30 of 30 pairs, under every reading and both point sets, the\nlargest distance between onset and coalescence exceeds both the distance at onset and the\ncoalesced Hausdorff distance. Under the adopted reading the medians are 9.31 at onset, 45.44 in the\ntransient and 14.51 after coalescence (code's point sets).\"\"\"\n\nR[\"fig3f-pairwise-similarity\"] = \"\"\"**Result: reproduced.** Under every reading of width and count, the data correlation exceeds\nthe control in 29 of 30 pairs (Spearman, control of the first program), 30 (Pearson, first), 27\n(Spearman, larger control) or 28 (Pearson, larger control); all are at least 26. With Pearson\ncorrelation and the larger control the two failing pairs are (1,3) and (2,3) of preparation 7, as\nthe paper names them. With the first program's control the Spearman reading fails pair (1,3) of\npreparation 4 instead (0.597 against 0.622).\"\"\"\n\nR[\"fig3h-perturbations-return\"] = \"\"\"**Result: partially reproduced, resting on the adopted reading.** Under the adopted reading\nwith the Methods' period (mean of the dominant peak), 34 divergent periods are found and 16 remain\nafter removing those within two periods of the end; 15 of 16 (0.938) returned above 90%. The fraction\nmatches (at least 80%), and so does the count of returns (15, within 15.3 to 18.7? no: 15 is below\n15.3), but 16 divergent periods is below 17.1. With the median period (the code's) 17 remain and 16\nreturn (0.941), all within tolerance. Over the four readings 14 to 19 periods remain and 13 to 17\nreturn, 0.875 to 0.941. The code's rule (dropping only the periods that never return) keeps 17 to 21.\"\"\"\n\nR[\"fig3i-same-manifold-after\"] = \"\"\"**Result: reproduced under reading (b).** Of the 15 returned divergences of the adopted\nreading, 13 have more than 20% of the recurrences of the final window before them falling after the\ndivergent point (reading (b), the code's blnSame), within 12.6 to 15.4; under reading (a), after the\nend of the divergent period, 10 do. With the median period, 14 of 16 under (b) and 11 under (a). Over\nthe four readings, (b) gives 11 to 17 and (a) 9 to 14.\"\"\"\n\nR[\"fig4bc-stable-spiral\"] = \"\"\"**Result: partially reproduced.** The mean over the 30 responses is a stable spiral under\nevery reading (adopted: a = -0.000362, b = 0.00729), but responses are not all spirals: 21 of 30\nare in the stable-spiral region, and 8 of 10 preparations have at least two of three (preparations 3\nand 4 have one each). The other readings give 20 to 23 responses and 6 to 9 preparations. The\nspread across responses is large against the mean of a (SD 0.00058 against -0.00036; SD of b\n0.0028 against 0.0073). No point of the dominant orbits had fewer than 100 neighbours.\"\"\"\n\nR[\"fig4c-orbital-period\"] = \"\"\"**Result: reproduced, resting on the adopted reading.** The mean over the 30 responses of\n2 pi / b times 0.01 s is 10.45 s under the adopted reading (9 to 11 s required); the variant, the\nmean of the per-point rotation periods, is 10.24 s. Under the code's count rule the means are 13.55\ns (own/le80) and 12.22 s (pooled/le80), outside the tolerance. The per-response linear periods do\nnot correlate with the recurrence periods (Pearson r = -0.063, p = 0.74, adopted; -0.12 to 0.03 for\nthe other readings), so the statement's \"consistent with\" holds for the means only (10.45 s against\na median recurrence period of 12.73 s).\"\"\"\n\nR[\"fig4s1a-contracting-dimensions\"] = \"\"\"**Result: not reproduced.** Only 11 of 30 responses have negative mean real parts in all\nunique dimensions under the adopted reading (8 to 11 under the others), where the criterion asks for\nmore than 15. The second part holds: 10 responses (9 to 12) have exactly one positive mean, in a\ndimension other than the first, which is at least one and fewer than half. In 8 responses the first\ndimension's mean is positive.\"\"\"\n\nR[\"fig4s1b-rotation-dominant\"] = \"\"\"**Result: reproduced.** In all 30 responses, under every reading, more than half of the\nlocal models have a complex eigenvalue among their top two (adopted: 0.87 to 1.00).\"\"\"\n\nR[\"fig5b-period-changes\"] = \"\"\"**Result: reproduced.** Under the adopted reading, 12 responses slow (rho > 0, p < 0.01), 4\nspeed up (rho < 0, p < 0.01) and 14 do not change at that level; the code's pooled one-sided test\ngives 13, 4 and 13. The number of windows per response is 31 to 73, within 27.9 to 79.2. The other\nreadings give 10 to 14 slowing, 4 to 7 speeding and 11 to 15 unchanged.\"\"\"\n\nR[\"fig5c-no-relation-contraction\"] = \"\"\"**Result: reproduced.** Across the 30 responses, Pearson's R between the weighted rho and the\nmean real part of the maximum eigenvalue is -0.342 (p = 0.064) under the adopted reading, and\n-0.343 (p = 0.063) with the contraction in %/s. The other readings give R = -0.14 to -0.34 (p = 0.067\nto 0.46). The test does not find the relation at p < 0.05, but the effect is moderate and p is close\nto the threshold under two readings.\"\"\"\n\nR[\"fig6s1-no-p10-motorneurons\"] = \"\"\"**Result: reproduced.** Of 1050 neuron-program values (1 neuron without spikes after 33 s),\nthe largest maximum locking is 0.522 (preparation 4, program 1, a neuron with 46 spikes); none\nreaches 0.9, so none does so in two programs. Only 2 values reach 0.5 and none 0.7.\"\"\"\n\nR[\"fig6d-decode-p10\"] = \"\"\"**Result: partially reproduced.** With the Methods' windowing, 8 of 9 responses have mean\nforecast R minus 2 s.e.m. above 0 (mean R 0.36 to 0.89); response 1 of preparation 4 does not (mean\nR -0.060, lower bound -0.127). Histories up to 100 ms and the code's windowing give the same 8 of 9\n(the code's windowing gives mean R -0.102 for that response). Training fits are good in all nine\n(mean training R 0.91 to 0.97). The Methods' windowing gives 40 forecast windows per response (360 in\nall), the code's 174 per response (1566); the paper's N = 173 is close to the code's count per\nresponse. Preparation 4's first response is the one the paper describes as apparently chaotic\n(Figure 3, figure supplement 1B).\"\"\"\n\nR[\"fig6s2-dimensions-p10\"] = \"\"\"**Result: partially reproduced.** Under the code's count rule the nine 80% counts lie in 3 to\n5 (own/le80; 3 to 5 for pooled/le80), and the 90% counts are at least twice them in each. Under the\nadopted reading (own/min80) the counts are 4 to 6, and one (6) is outside 2.7 to 5.5; the 90% counts\n(8 to 17) are at least double. Forecasts with the 90% dimensions are not better: the mean MAE is\nhigher with 90% in 7 of 9 (Wilcoxon p = 0.0195, median difference +1.56, so worse, not better), and\nthe mean R-squared is higher in 3 of 9 (p = 0.25). So the absence holds under the adopted reading,\nwhere the counts fail in one response; the decoding was not run with the code's count rule, under\nwhich the counts hold.\"\"\"\n\nR[\"fig7a-long-tailed-participation\"] = \"\"\"**Result: reproduced.** Under both readings of d, every one of the 30 responses has positive\nskewness of participation (0.50 to 4.36, reading (a)) and fewer than half its neurons above 50% of\nthe maximum (at most 39.4%).\"\"\"\n\nR[\"fig7f-strongly-variable-neurons\"] = \"\"\"**Result: reproduced.** Under both readings of d and both poolings, all 10 preparations have\nstrongly variable neurons: at least 4 per preparation (reading (a), all pairs), 3.8% to 23.4% of the\nneurons; with consecutive pairs (the code) 5.9% to 29.3%.\"\"\"\n\nR[\"halving-participation\"] = \"\"\"**Result: reproduced.** The neuron at 100% in a program has under half that participation in\nanother program of its preparation in 6 of 10 preparations (reading (a)); a neuron of a program's\ntop 10% does so in 9 of 10. Both readings of d give the same counts.\"\"\"\n\nR[\"fig7s1-rate-synchrony\"] = \"\"\"**Result: reproduced.** With participation reading (a), the rate from stimulation offset and\nmatched pairs, the mean R-squared is 0.491 within responses (0.45 to 0.55 required; range 0.29 to\n0.74) and 0.239 for changes between responses (0.207 to 0.253 required). The rate from onset gives\n0.514 and 0.265 (the second outside); the code's mismatched pairing gives 0.205 and 0.221; reading\n(b) gives 0.499 and 0.244.\"\"\"\n\nR[\"fig7gh-robust-to-participation\"] = \"\"\"**Result: not reproduced, resting on the adopted reading.** Under the adopted width and count,\neach set of distances finds one significant slope: with the recurrent points (Methods), the\nnormalised distance rises with the total change in participation (slope 0.0127, p = 0.031, R-squared\n0.17, 28 pairs) and not with the Hellinger distance (p = 0.35); with the code's point sets, it rises\nwith the Hellinger distance (p = 0.028) and not with the total change (p = 0.11). Participation\nreading (b) gives the same pattern (p = 0.032 and 0.017). Under the code's width and count\n(pooled/le80) no slope is significant (p = 0.12 to 0.86). The outcome depends on the reading.\"\"\"\n\nR[\"fig7s2\"] = \"\"\"## fig7s2-no-invariant-core\n\n> No small invariant core of strongly participating, phasically active neurons, such as a classic\n> central pattern generator, is found across preparations.\n\nBlocked, `not_runnable`. The criterion needs the ensembles and their dynamical types (tonic,\noscillator, burster, pauser) from the paper's MATLAB toolbox (`consensus_cluster_spike_data_binless.m`,\n323 lines, and `Analyse_Spike_Train_Properties.m`, 246 lines, with their dependencies). MATLAB\ncannot be installed in the entry's locked environment, and a port of the consensus clustering and\nthe autocorrelogram typing was not attempted within this run's time.\"\"\"\n\nR[\"summary\"] = \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| dataset-size | partially reproduced |\n| fig1d-slow-oscillation | reproduced |\n| fig1e-decaying-rate | reproduced |\n| fig2b-dimensions | reproduced (under the code's count rule) |\n| fig2ef-periodic-recurrence | reproduced |\n| fig2e-single-dominant-orbit | reproduced |\n| fig2s2-threshold-robust | reproduced |\n| fig3a-coalescence | not reproduced |\n| fig3c-same-manifold | reproduced |\n| fig3s1a-common-axes | reproduced |\n| fig3d-initial-conditions | reproduced |\n| fig3f-pairwise-similarity | reproduced |\n| fig3h-perturbations-return | partially reproduced (assumed) |\n| fig3i-same-manifold-after | reproduced (reading (b)) |\n| fig4bc-stable-spiral | partially reproduced |\n| fig4c-orbital-period | reproduced (assumed) |\n| fig4s1a-contracting-dimensions | not reproduced |\n| fig4s1b-rotation-dominant | reproduced |\n| fig5b-period-changes | reproduced |\n| fig5c-no-relation-contraction | reproduced |\n| fig6s1-no-p10-motorneurons | reproduced |\n| fig6d-decode-p10 | partially reproduced |\n| fig6s2-dimensions-p10 | partially reproduced |\n| fig7a-long-tailed-participation | reproduced |\n| fig7f-strongly-variable-neurons | reproduced |\n| halving-participation | reproduced |\n| fig7s1-rate-synchrony | reproduced |\n| fig7gh-robust-to-participation | not reproduced (assumed) |\n| fig7s2-no-invariant-core | blocked, not runnable |\n| fig8-caudolateral | blocked, metadata insufficient |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\n**How the analysis differs from the paper's.** It is a Python port of the paper's MATLAB code,\nfollowing the Methods where they fix a detail and the code where they do not. The Methods' kernel\nwidth as printed (median ISI / 12) gives 22 to 76 dimensions, and the analysis uses the code's width\n(the median ISI) for everything after claim fig2b. The code computes that median over the recordings\nof the same bout number read so far; the adopted reading uses the recording's own. The number of PCs\nis the smallest reaching 80% (Methods) in the adopted reading; the code's rule (at most 80%) is run\nalongside and changes some outcomes (fig4c, fig6s2, fig7gh). The local models use the contiguous run\nof neighbours as the Methods describe. The permutation test of fig5b permutes the delays against time\n(10000 permutations); the code's test is shown too. The decoding uses a numpy IRLS for MATLAB's\nglmfit, and the 90% models were fitted with four histories only.\n\n**What was found about the data set.** The files match their checksums and the description: 30\nrecordings of 75 to 160 neurons, 1131 in all, P10 for nine, coordinates for all ten preparations.\nThe paper's 120 to 180 neurons per recording cannot be right with its own total of 1131. The P10\nsampling (1629.7 Hz) agrees with the description's 1630 Hz, not the paper's 1600 Hz. The P10 file\nnames of preparation 2 drop the \"B\" of its spike file. The coordinates have no unit and no\norientation, so which part of the array is caudo-lateral cannot be told from the data set.\"\"\"\n\njson.dump(R, open(\"/tmp/claude-1001/results.json\", \"w\"), indent=1)\n"
}
```

```
File created successfully at: /tmp/claude-1001/results.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('results.py').read()
s=s.replace("""(in every recording the population rate during the stimulus is 2.6 to 11 times the rate
before it, and the rate after 32.5 s exceeds the rate before 30 s in 30 of 30)""","""(in every recording the population rate during the stimulus exceeds the rate before it, and
the rate after 32.5 s exceeds the rate before 30 s in 30 of 30)""")
s=s.replace("""matches (at least 80%), and so does the count of returns (15, within 15.3 to 18.7? no: 15 is below
15.3), but 16 divergent periods is below 17.1. With""","""matches (at least 80%), but both counts fall just short of their tolerances: 16 divergent periods
against 17.1 to 20.9, and 15 returns against 15.3 to 18.7. With""")
s=s.replace("cases (median absolute difference 1.30 s against 1.27 s","cases (median absolute difference 1.30 s against 1.27 s")
s=s.replace("for both lower thresholds. Reading (b) holds at 5% in every case and fails at 2% in five of eight","for both lower thresholds. Reading (b) holds at 5% in every case and fails at 2% in six of eight")
s=s.replace("""22 to 26 of 30, and so do the readings with the narrow widths except twelve/le80 with the mean (13
of 30); every reading but that one meets the criterion.""","""22 to 26 of 30, and the readings with the narrow widths 13 to 29; every reading but twelve/le80
with the mean (13 of 30) meets the criterion.""")
s=s.replace("dimension other than the first, which is at least one and fewer than half. In 8 responses the first","dimension other than the first, which is at least one and fewer than half. In 7 responses the first")
open('results.py','w').write(s)
EOF
python results.py && . dev/bin/activate && python build.py && cd entries/crcns-apl-1-bruno-2017 && cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-apl-1-bruno-2017
type: reproduction
title: Spiral attractor in the Aplysia pedal ganglion (Bruno, Frost and Humphries 2017)
description: Tests the findings of Bruno, Frost and Humphries (2017) on CRCNS data set apl-1, which
  holds the spike times of 30 voltage-sensitive dye recordings of the pedal ganglion (three evoked
  bouts of fictive locomotion in each of 10 preparations), the P10 nerve spikes of nine of them and
  the neurons' positions on the photodiode array. It ports the paper's recurrence analysis, local
  linear models, manifold comparisons, P10 decoding and participation measures from the paper's
  MATLAB code, under every reading of the kernel width and the number of dimensions.
license: Apache-2.0
notebooks:
- path: reproduce_bruno_2017.ipynb
  title: Reproducing Bruno, Frost and Humphries (2017) from CRCNS apl-1
  runtime_minutes: 19
helpers:
- apl.py
related:
- id: crcns:apl-1/unversioned
  relation: uses_data
- id: doi:10.7554/elife.27342
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/crcns-apl-1-bruno-2017 2>&1 | tail -3 && python tools/entry.py check entries/crcns-apl-1-bruno-2017 2>&1 | tail -15; date -u
```

```
wrote entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb 76 cells
wrote entries/crcns-apl-1-bruno-2017/requirements.lock.txt
0 error(s)
Sun Nov  8 13:42:00 UTC 2026
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/crcns-apl-1-bruno-2017 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-crcns-apl-1-bruno-2017 in executed/crcns-apl-1-bruno-2017/.venv/share/jupyter/kernels/registry-crcns-apl-1-bruno-2017
0 error(s)
pass  reproduce_bruno_2017.ipynb  (1078 s)

real	18m6.265s
user	55m9.701s
sys	1m34.144s
Sun Nov  8 14:00:11 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF' > out3.txt
import json
nb=json.load(open('executed/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f'==== tags={c["metadata"].get("tags")}')
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text']))
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
EOF
python - <<'EOF' > out2b.txt
import json
nb=json.load(open('/tmp/claude-1001/exec/run2.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f'==== tags={c["metadata"].get("tags")}')
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text']))
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
EOF
diff out2b.txt out3.txt | head -60
```

```
284c284
< recurrence analysis of 30 recordings under 8 readings in 262 s; peak memory 1.09 GB per worker
---
> recurrence analysis of 30 recordings under 8 readings in 266 s; peak memory 1.11 GB per worker
338a339
> adopted reading, quartiles of the dominant period (mean of the peak): [11.06 14.98] ; outside 9 to 16.5 s: [[1.0, 2.0, 17.28], [7.0, 1.0, 22.23], [7.0, 2.0, 8.75], [8.0, 1.0, 19.94]]
477c478
< comparisons in 221 s
---
> comparisons in 218 s
931c932
< permutation tests in 122 s
---
> permutation tests in 123 s
998c999
< decoding in 440 s
---
> decoding in 429 s
1106d1106
< 
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s.get('required'),indent=0)); print(list(s['properties'].keys()))
o=s['properties']['outcomes']['items']; print(o.get('required'), list(o['properties'].keys()))
print(json.dumps(s['properties']['provenance'],indent=0)[:1500])
print(json.dumps(s['properties']['dataset'],indent=0)[:800])
print(s['properties']['findings']['items'].get('required'), list(s['properties']['findings']['items']['properties']))
"
```

```
[
"schema_version",
"id",
"dataset",
"paper",
"date",
"provenance",
"outcomes"
]
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"accountable"
],
"properties": {
"kind": {
[... 97 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "content": "schema_version: 2\nid: crcns-apl-1-bruno-2017-01\ndataset:\n  archive: crcns\n  id: apl-1\n  version: unversioned\n  doi: 10.6080/K0SN074B\npaper: doi:10.7554/elife.27342\ndate: 2026-11-08\nentry: crcns-apl-1-bruno-2017\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42478340998\noutcomes:\n- claim: dataset-size\n  outcome: partially_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:dataset-size\n  measured:\n  - 10\n  - 30\n  - 1131\n  notes: 10 preparations, 30 recordings and 1131 neurons, all as the paper gives. Recordings hold\n    75 to 160 neurons and only 12 of 30 lie in 108 to 198 (120 to 180 widened by 10%), as the data\n    set's description (75 to 160) says. Counting only neurons that spike after onset gives the same\n    numbers. The paper's range cannot hold with its total, as ten preparations of at least 120\n    neurons would hold at least 1200.\n- claim: fig1d-slow-oscillation\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig1d-slow-oscillation\n  measured: 0.0486\n  notes: Power-weighted peak of the grand mean spectrum 0.0486 Hz; per recording 0.0131 to 0.0789\n    Hz, 30 of 30 above 0 and at or below 0.11 Hz. Variant, frequency of maximum power above 0 Hz,\n    0.0076 to 0.0992 Hz, 30 of 30 at or below 0.11 Hz. The frequency grid step is 0.0076 Hz.\n  deviations:\n  - Chronux mtspectrumpt is ported to Python (apl.mtspectrumpt) with its defaults, tapers [3 5], the\n    time grid from the first to the last spike, the mean rate subtracted; it was not checked against\n    MATLAB output.\n- claim: fig1e-decaying-rate\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig1e-decaying-rate\n  notes: Reading (a), 30 of 30 decreasing (R from -0.992 to -0.774) and none increasing; reading\n    (b), 30 of 30 negative slopes. Every preparation has three decreasing responses.\n- claim: fig2b-dimensions\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig2b-dimensions\n  measured:\n  - 3\n  - 7\n  notes: Reproduced under reading (c) with the recording's own median ISI and count (ii), at most\n    80% (own/le80), the first reading the criterion lists that matches; 28 of 30 counts in 3.6 to\n    8.8 (3 to 7) and neurons divided by count above 10 in all 30 (lowest 10.7). The code's pooled\n    median with count (ii) gives the same 28 and 30. With count (i), smallest reaching 80%, the\n    counts are 4 to 8 (the paper's range; 30 of 30 in range) but the ratio is 9.4 in one recording\n    (75 neurons, 8 PCs), so the criterion fails there by one response. The readings (a) median ISI /\n    sqrt(12) and (b) median ISI / 12 give 21 to 76 dimensions and ratios of 1.8 to 2.8 at the lowest.\n  deviations:\n  - The kernel width is read four ways (median ISI / sqrt(12), / 12, the median ISI of the recording,\n    and the code's running median over the recordings of the same bout number), each with both\n    count rules, as the criterion lists.\n- claim: fig2ef-periodic-recurrence\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig2ef-periodic-recurrence\n  measured:\n  - 11.06\n  - 14.98\n  notes: Measured gives the quartiles of the 30 dominant periods under the adopted reading (own/min80,\n    mean of the peak). 26 of 30 periods lie in 9 to 16.5 s, and 4 do not (17.28, 22.23, 8.75 and\n    19.94 s); with the median of the peak 23 of 30. The four readings with the code's width give 22\n    to 26 of 30, the narrow widths 13 to 29; every reading except twelve/le80 with the mean (13 of 30)\n    meets the criterion.\n  deviations:\n  - Recurrence follows Analyse_by_Recurrence_Points.m (points from 35 s to 10 s before the end, the\n    first contiguous run within theta dropped, bins of 1 s on 0 to 50 s, peaks of at least 100\n    points), as the claims file's opening comment gives it.\n- claim: fig2e-single-dominant-orbit\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig2e-single-dominant-orbit\n  measured: 29\n  notes: Adopted reading, 29 of 30 responses above 50% with delays of 5 to 50 s, 27 of 30 counting\n    all recurrent points (propInMaxPeriod). 1 to 4 peaks per response (12 with one), as the Methods\n    say. Other readings 29 to 30 and 24 to 27.\n  assumed: true\n  deviations:\n  - Rests on the adopted reading of width and count (own/min80); the other three readings with the\n    code's width give the same outcome.\n- claim: fig2s2-threshold-robust\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig2s2-threshold-robust\n  notes: Reading (a) holds for both lower thresholds under every reading of width, count and\n    period (Spearman 0.70 to 0.97, all p below 2e-5, 30 responses with a peak at both thresholds).\n    Reading (b) holds at 5% in all eight cases and fails at 2% in six (adopted, mean period, median\n    absolute difference 1.30 s against 1.27 s).\n- claim: fig3a-coalescence\n  outcome: not_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig3a-coalescence\n  measured: 12\n  notes: Coalescence within one dominant period of onset in 12 of 30 responses (adopted reading),\n    11 to 14 under the others, against 27 required; from offset 18 of 30 (16 to 20). Coalescence 7.5\n    to 49.5 s after onset, median 14.5 s. The stability part holds, more than 50% of points recur\n    after coalescence in 30 of 30 (60.8% to 98.6%). As the checked points start 5 s after onset\n    (Methods), the earliest possible coalescence is 7.5 s after onset, near the shortest periods\n    (8.7 to 9.4 s).\n  deviations:\n  - A window counts as coalesced when more than 90% of its points recur (the code's PrctWnone below\n    10), where the Methods say at least 90%; with 500 points per window the two differ only at\n    exactly 450 points.\n- claim: fig3c-same-manifold\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig3c-same-manifold\n  measured: 29\n  notes: Reading (a), recurrent points, 29 of 30 pairs below their control mean under every\n    reading, failing pair (1,2) of preparation 4 (1.04 times its control). Reading (b), the code's\n    point sets, 28 of 30 under every reading, failing pairs (1,2) and (1,3) of preparation 4 (1.19\n    and 1.17), the pairs the paper names. 100 shuffles each way; 2 s.e.m. of the control 0.11 to\n    0.36.\n  deviations:\n  - The Hausdorff distances use scipy's exact directed_hausdorff in place of the code's loops.\n- claim: fig3s1a-common-axes\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig3s1a-common-axes\n  measured: 30\n  notes: On common axes (5 to 10 PCs, at most 80%), recurrent points 30 of 30 under every reading;\n    the code's point sets 28 of 30 (failing preparation 4, pairs (1,2) and (1,3)) under three\n    readings and 27 under own/le80 (also preparation 8, pair (2,3)).\n- claim: fig3d-initial-conditions\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig3d-initial-conditions\n  notes: The transient distance exceeds both the onset and the coalesced distance in 30 of 30 pairs\n    under every reading and both point sets. Adopted reading, medians 9.31 (onset), 45.44\n    (transient) and 14.51 (coalesced, code's point sets).\n  deviations:\n  - The transient distance uses every fifth point of the second program of the pair, to save time;\n    points 10 ms apart are nearly equal, so the maximum changes little.\n- claim: fig3f-pairwise-similarity\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig3f-pairwise-similarity\n  measured: 29\n  notes: Data correlation above control in 29 of 30 pairs (Spearman, first program's control), 30\n    (Pearson, first), 27 (Spearman, larger control) and 28 (Pearson, larger control), the same under\n    every reading of width and count. With Pearson and the larger control the failing pairs are\n    (1,3) and (2,3) of preparation 7, as the paper names them; with Spearman and the first control\n    pair (1,3) of preparation 4 fails (0.597 against 0.622).\n  deviations:\n  - The similarity matrix is the correlation of the post-onset spike-density functions, as the\n    criterion says; the code takes it from its clustering toolbox's convolved trains, which use the\n    same kernel width.\n- claim: fig3h-perturbations-return\n  outcome: partially_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig3h-perturbations-return\n  measured:\n  - 16\n  - 15\n  assumed: true\n  notes: Adopted reading with the Methods' period (mean of the peak), 34 divergent periods, 16 kept\n    after removing those within two periods of the end, 15 returned (0.938). The fraction meets the\n    criterion and both counts fall just below their tolerances (17.1 to 20.9 and 15.3 to 18.7). With\n    the median of the peak (the code's period) 17 kept and 16 returned (0.941), all within\n    tolerance. Over the four readings 14 to 19 kept, 13 to 17 returned, fractions 0.875 to 0.941.\n    The code's rule, removing only periods that never return, keeps 17 to 21.\n  deviations:\n  - Divergent periods follow the Methods' definition (runs of windows below 90% after coalescence\n    that fall below 50%), computed directly; the code's loop in recurrence_point_results_Viz.m finds\n    the same kind of run.\n  - Assumed, the period for the two-cycle rule is the Methods' mean of the dominant peak; the\n    outcome under the code's median is reproduced. Question for the authors under findings.\n- claim: fig3i-same-manifold-after\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig3i-same-manifold-after\n  measured: 13\n  notes: Reading (b), recurrences after the divergent point (the code's blnSame), 13 of the 15\n    returned divergences exceed 0.2 under the adopted reading, within 12.6 to 15.4; reading (a), after\n    the end of the divergent period (Methods), 10. With the median period 14 of 16 under (b) and 11\n    under (a). Over the four readings (b) gives 11 to 17 and (a) 9 to 14. It depends on claim\n    fig3h-perturbations-return, whose counts are just short; the returned divergences tested here\n    are those it finds.\n- claim: fig4bc-stable-spiral\n  outcome: partially_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig4bc-stable-spiral\n  measured:\n  - -0.000362\n  - 0.00729\n  notes: The grand mean is a stable spiral under every reading (adopted a = -0.000362, b =\n    0.00729). 21 of 30 responses lie in the stable-spiral region; 8 of 10 preparations have at\n    least two of three (preparations 3 and 4 have one each); other readings 20 to 23 responses and\n    6 to 9 preparations. Spread, SD of a 0.00058 and of b 0.0028 across responses. No point of a\n    dominant orbit had fewer than 100 neighbours.\n  deviations:\n  - The maximum eigenvalue is the one of largest modulus, as MATLAB's max orders complex numbers in\n    LocalLinearDynamics.m; the Methods do not say how the maximum is taken.\n  - The local neighbourhood is the contiguous run of points within 2.5 theta around the point, as\n    the Methods describe. The code's run detection subtracts the point's position in the\n    neighbourhood from the time indices (abs(currixs - ixPt)), which can miss gaps before the point;\n    that quirk is not reproduced.\n- claim: fig4c-orbital-period\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig4c-orbital-period\n  measured: 10.45\n  assumed: true\n  notes: Mean over responses of 2 pi / b times 0.01 s, 10.45 s under the adopted reading; the\n    variant mean of per-point rotation periods 10.24 s. With count (ii) (the code's) 13.55 s\n    (own/le80) and 12.22 s (pooled/le80), outside tolerance. The per-response linear periods do not\n    correlate with the recurrence periods (Pearson r = -0.063, p = 0.74; -0.12 to 0.03 under the\n    other readings), so consistency holds only for the means (10.45 s against a median recurrence\n    period of 12.73 s).\n  deviations:\n  - Assumed, the Methods' count rule (smallest number of PCs reaching 80%); the code's rule gives a\n    mean period outside the tolerance. Question for the authors under findings.\n- claim: fig4s1a-contracting-dimensions\n  outcome: not_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig4s1a-contracting-dimensions\n  measured: 11\n  notes: All unique-dimension means negative in 11 of 30 responses (8 to 11 under the other\n    readings), where more than 15 are required. The second part holds, 10 responses (9 to 12) have\n    exactly one positive mean, in a dimension other than the first. In 7 responses the first\n    dimension's mean is positive.\n- claim: fig4s1b-rotation-dominant\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig4s1b-rotation-dominant\n  notes: Proportion of local models with a complex eigenvalue among the top two above 0.5 in all 30\n    responses under every reading (adopted 0.87 to 1.00).\n- claim: fig5b-period-changes\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig5b-period-changes\n  measured:\n  - 31\n  - 73\n  notes: Adopted reading, 12 slowing, 4 speeding and 14 unchanged at p < 0.01 (10000 permutations of\n    the window delays, two-sided); the code's pooled one-sided test with 100000 permutations gives\n    13, 4 and 13. Windows per response 31 to 73. Other readings 10 to 14 slowing, 4 to 7 speeding,\n    11 to 15 unchanged.\n  deviations:\n  - The Methods do not say what the permutation test permutes; the main test permutes the mean\n    delays against window time, keeping the weights with the windows, and is two-sided. The code's\n    test, which permutes the pooled time and delay values and is one-sided, is shown as the claims\n    file's variant. Ranks are assigned without averaging ties, as in WeightedCorrelation.m.\n- claim: fig5c-no-relation-contraction\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig5c-no-relation-contraction\n  measured: -0.342\n  notes: Pearson R = -0.342, p = 0.064 between weighted rho and mean real part (adopted reading);\n    -0.343, p = 0.063 with the contraction in %/s. Other readings R = -0.14 to -0.34, p = 0.067 to\n    0.46. No relation at p < 0.05, but the effect is moderate and p is near the threshold.\n- claim: fig6s1-no-p10-motorneurons\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig6s1-no-p10-motorneurons\n  measured: 0.522\n  notes: 1050 neuron-program values (1 neuron without spikes after 33 s); largest maximum locking\n    0.522; none at 0.9 or more, none in two programs; 2 values reach 0.5, none 0.7.\n- claim: fig6d-decode-p10\n  outcome: partially_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig6d-decode-p10\n  notes: Methods' windowing, mean forecast R minus 2 s.e.m. above 0 in 8 of 9 responses (mean R\n    0.36 to 0.89); response 1 of preparation 4 fails (mean R -0.060, bound -0.127). Histories up to\n    100 ms and the code's windowing give the same 8 of 9. Training R 0.91 to 0.97 in all nine.\n    Forecast windows, 40 per response with the Methods' windowing (360), 174 per response with the\n    code's (1566); the paper's N = 173 is close to the code's count per response. The failing\n    response is the one the paper describes as apparently chaotic.\n  deviations:\n  - The Poisson GLM is fitted by a numpy IRLS in place of MATLAB's glmfit, at most 25 iterations\n    with a relative deviance change of 1e-6 (a standard choice; the forecasts of one program agreed\n    to three decimals with 100 iterations).\n  - The kernel width and PCs are those of the adopted reading (own/min80).\n  - Each window's fit starts from the previous window's coefficients, which changes only the\n    starting point of the iterations.\n- claim: fig6s2-dimensions-p10\n  outcome: partially_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig6s2-dimensions-p10\n  measured:\n  - 3\n  - 5\n  notes: Under count (ii) the nine 80% counts are 3 to 5 (own/le80 and pooled/le80) and the 90%\n    counts at least double them in each, so the counts hold. Under the adopted reading (own/min80)\n    the counts are 4 to 6 and one (6) is outside 2.7 to 5.5; 90% counts 8 to 17, at least double.\n    The 90% forecasts (adopted reading) are not better, mean MAE higher in 7 of 9 (Wilcoxon p =\n    0.0195, median difference +1.56, worse) and mean R-squared higher in 3 of 9 (p = 0.25), so the\n    absence holds under the adopted reading. The decoding was not run under count (ii), where the\n    counts hold, so no single reading shows both parts.\n  deviations:\n  - The 90% models use histories of 50, 100, 150 and 200 ms only (the 80% models all 16 of the\n    Methods' grid), to fit the time limit; the 90% decoding with the full grid took 7.7 minutes in\n    development.\n- claim: fig7a-long-tailed-participation\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig7a-long-tailed-participation\n  notes: Both readings of d, 30 of 30 responses with positive skewness (0.50 to 4.36, reading (a))\n    and fewer than half the neurons above 50% of the maximum (at most 39.4%).\n  deviations:\n  - Participation uses the adopted kernel width (the recording's median ISI).\n- claim: fig7f-strongly-variable-neurons\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig7f-strongly-variable-neurons\n  notes: All 10 preparations have strongly variable neurons under both readings of d and both\n    poolings; reading (a) with all pairs at least 4 per preparation, 3.8% to 23.4% of neurons;\n    consecutive pairs 5.9% to 29.3%.\n  deviations:\n  - Neuron ids are taken to name the same neuron in all bouts, as the data description says\n    (recordings concatenated before spike sorting); per-neuron spike counts correlate between bouts\n    above permuted ids in 30 of 30 pairs, which is consistent with it.\n- claim: halving-participation\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:halving-participation\n  measured: 6\n  notes: Reading (a), the neuron at 100%, halves in another program in 6 of 10 preparations; reading\n    (b), the top 10%, in 9 of 10; the same under both readings of d.\n- claim: fig7s1-rate-synchrony\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig7s1-rate-synchrony\n  measured:\n  - 0.491\n  - 0.239\n  notes: Participation (a), rate from stimulation offset, matched pairs, mean R-squared 0.491 within\n    responses and 0.239 for changes. Rate from onset 0.514 and 0.265; the code's mismatched pairing\n    0.205 and 0.221; participation (b) 0.499 and 0.244.\n- claim: fig7gh-robust-to-participation\n  outcome: not_reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig7gh-robust-to-participation\n  assumed: true\n  notes: Adopted width and count. With recurrent points the normalised distance rises with the\n    total change in participation (slope 0.0127, p = 0.031, R-squared 0.17, 28 pairs) but not the\n    Hellinger distance (p = 0.35); with the code's point sets it rises with the Hellinger distance\n    (p = 0.028) but not the total change (p = 0.11). Participation reading (b) gives the same pattern\n    (p = 0.032 and 0.017). Under the code's width and count (pooled/le80) no slope is significant (p\n    = 0.12 to 0.86), so the outcome depends on the reading. The robust fits agree with the ordinary\n    ones in significance except one (code points, reading (a), Hellinger, robust p = 0.063).\n  deviations:\n  - Assumed, the adopted reading of width and count (own/min80); under the code's pooled width and\n    count (ii) the claim is reproduced. The test is the code's linear regression slope, as the\n    criterion says.\n- claim: fig7s2-no-invariant-core\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: The criterion needs the ensembles and types from the paper's MATLAB toolbox\n    (consensus_cluster_spike_data_binless.m and Analyse_Spike_Train_Properties.m, about 570 lines\n    with dependencies). MATLAB cannot be installed in the locked environment, and a Python port of\n    the consensus clustering and autocorrelogram typing was not attempted within the run's time.\n- claim: fig8-caudolateral\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The criterion needs the orientation of the array. The paper's text, the code\n    (ParticipationMapsSummary.m plots the coordinates on the diode template without labels), the\n    data description and the files (Coordinates.mat, diode_template.mat, plot_maps.m) do not say\n    which direction of x or y is rostral, caudal, medial or lateral. The notebook prints the counts\n    of top-fifth neurons by quadrant of the array coordinates, which decide nothing without it.\nfindings:\n- kind: paper_inconsistency\n  statement: The paper gives 120 to 180 neurons per recorded population and 1131 neurons in all over\n    10 preparations; ten preparations of at least 120 would hold at least 1200. The data set holds\n    75 to 160 neurons per preparation, 1131 in all, as its description says.\n- kind: metadata_insufficient\n  statement: Coordinates.mat gives each neuron's x and y on a 0 to 50 scale without a unit, and\n    neither the files, plot_maps.m nor the data description say which directions of the array are\n    rostral, caudal, medial or lateral, so the paper's caudo-lateral quadrant cannot be located.\n- kind: other\n  statement: The P10 spike times are on a grid of 0.614 ms (1629.7 Hz), which agrees with the data\n    description's 1630 Hz sampling; the paper says 1600 Hz.\n- kind: identifier_missing\n  statement: The P10 files of preparation 2 are named Jun0414da0Np10.mat while its spike and\n    coordinate files are Jun0414B; they can be matched only by the first seven characters, as the\n    paper's code does.\n- kind: methods_unavailable\n  statement: Question for the authors. The Methods give the Gaussian width as the median ISI divided\n    by 12 (the extracted text; possibly the square root of 12), but the code uses the median ISI\n    itself, computed as a running median over the recordings of the same bout number read so far.\n    With median ISI / 12 or / sqrt(12) the recordings need 21 to 76 PCs for 80% of the variance, not\n    the paper's 4 to 8. Which width was used for the published figures, and was the median meant to\n    be per recording?\n- kind: methods_unavailable\n  statement: Question for the authors. The Methods say the projection kept the dimensions needed for\n    at least 80% of the variance; the recurrence and participation code keeps those whose cumulative\n    variance is at most 80% (one fewer), while the manifold code keeps the smallest number reaching\n    80%. Which rule produced Figures 2 to 5? The linear-model period of Figure 4C is 10.45 s under\n    the first and 12.2 to 13.6 s under the second.\n- kind: methods_unavailable\n  statement: Question for the authors. For removing divergent periods within two oscillation cycles\n    of the end, is the cycle the mean or the median recurrence time of the dominant peak, and is the\n    rule applied to all divergent periods (Methods) or only to those that never return (code)? The\n    counts change from 16 to 21 kept periods with these choices.\n- kind: methods_unavailable\n  statement: Question for the authors. The permutation test of the weighted Spearman correlation\n    (Tracking changes in periodicity) is not described beyond 10000 permutations; the code permutes\n    the pooled time and period values with 100000 permutations and tests one side. Which test gave\n    Figure 5B?\n- kind: code_mismatch\n  statement: Figure 6D reports N = 173 forecast windows. The Methods' windowing (40 s fit, 10 s\n    forecast, 1 s steps from 33 s) gives 40 windows per response here; the code's windowing\n    (training on 50% of the series, 0.2 s steps) gives 174 per response, close to 173, so the\n    figure appears to use the code's windowing, not the Methods'.\n- kind: code_mismatch\n  statement: In What_is_Participation.m the rate changes are ordered (1,2), (1,3), (2,3) and the\n    participation changes (1,2), (2,3), (1,3), so two of three pairs are mismatched in the\n    correlation behind Figure 7, figure supplement 1D. With matched pairs the mean R-squared is\n    0.239, with the code's pairing 0.205.\n- kind: code_mismatch\n  statement: LocalLinearDynamics.m finds the contiguous neighbourhood of a point from\n    abs(currixs - ixPt), the time indices minus the point's position within the neighbourhood, so\n    gaps among neighbours earlier than that position are not detected and the fitted run can extend\n    past them. The Methods describe a run contiguous in time.\n"
}
```

```
File created successfully at: attempts/crcns-apl-1-bruno-2017-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/crcns-apl-1-bruno-2017-01.yaml'
s=open(p).read()
s=s.replace("""    say. Other readings 29 to 30 and 24 to 27.
  assumed: true
  deviations:
  - Rests on the adopted reading of width and count (own/min80); the other three readings with the
    code's width give the same outcome.
""","""    say. The other three readings with the code's width give 29 to 30 and 24 to 27, the same
    outcome.
""")
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); print(len(d['outcomes']), [o['outcome'] for o in d['outcomes']].count('reproduced'))
EOF
grep -n ": " attempts/crcns-apl-1-bruno-2017-01.yaml | grep -v "^[0-9]*:\s*-\?\s*[a-z_]*: " | head
```

```
30 20
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-apl-1-bruno-2017/README.md",
 "content": "# Bruno, Frost & Humphries (2017) from CRCNS apl-1\n\nTests the findings of [Bruno, Frost & Humphries (2017)](https://doi.org/10.7554/elife.27342),\n\"A spiral attractor network drives rhythmic locomotion\", on CRCNS data set\n[apl-1](https://doi.org/10.6080/K0SN074B): spike times of 30 voltage-sensitive dye recordings of the\nAplysia pedal ganglion (three evoked bouts in each of 10 preparations), P10 nerve spikes for nine of\nthem, and neuron positions on the photodiode array.\n\n| Claim | Outcome |\n|---|---|\n| Counts of preparations, recordings and neurons; 120 to 180 neurons per recording | Partially reproduced |\n| Slow (at most 0.1 Hz) oscillation in the spectra | Reproduced |\n| Decaying population rate | Reproduced |\n| 4 to 8 dimensions for 80% of the variance | Reproduced (under the code's count rule) |\n| Periodic recurrence at 10 to 15 s in many responses | Reproduced |\n| A single dominant orbit | Reproduced |\n| Periods robust to the recurrence threshold | Reproduced |\n| Coalescence within one period of stimulation | Not reproduced |\n| Same manifold across bouts (two axis choices) | Reproduced (2 claims) |\n| Different initial conditions | Reproduced |\n| Pairwise similarity preserved | Reproduced |\n| 17 of 19 perturbations return | Partially reproduced (assumed) |\n| Return to the same manifold | Reproduced |\n| Stable spiral in every preparation | Partially reproduced |\n| Linear-model period of about 10 s | Reproduced (assumed) |\n| Contraction in all dimensions in most responses | Not reproduced |\n| Rotation dominates | Reproduced |\n| Period slows, speeds up or is unchanged | Reproduced |\n| No relation between period change and contraction | Reproduced |\n| No P10 motorneurons recorded | Reproduced |\n| P10 decoded in all nine responses | Partially reproduced |\n| 3 to 5 dimensions for the P10 recordings; 90% no better | Partially reproduced |\n| Long-tailed, variable participation (three claims) | Reproduced |\n| Rate explains 50% of participation, 23% of its change | Reproduced |\n| Distance between bouts unrelated to participation change | Not reproduced (assumed) |\n| No invariant core of oscillator neurons | Blocked: not runnable |\n| Strong participation in the caudo-lateral quadrant | Blocked: metadata insufficient |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nSeveral outcomes depend on two details the paper leaves open: the width of the Gaussian kernel\n(the Methods' printed formula gives 21 to 76 dimensions; the code uses the median ISI) and whether\nthe number of PCs is the smallest reaching 80% (Methods) or the largest at most 80% (code). The\nnotebook runs every reading. The attempt record, with the reasons and the differences from the\npaper's method, is [`attempts/crcns-apl-1-bruno-2017-01.yaml`](../../attempts/crcns-apl-1-bruno-2017-01.yaml).\n\n- `reproduce_bruno_2017.ipynb`: the analysis, about 18 minutes on 4 CPUs (the recurrence analysis\n  under eight readings, the manifold comparisons with 100 shuffles, and the P10 decoding).\n- `apl.py`: streaming the files from the CRCNS bucket, spike-density functions, PCA, the\n  recurrence analysis, local linear models, Hausdorff comparisons, a port of Chronux\n  `mtspectrumpt`, P10 decoding and participation. Other notebooks on this data set can import it.\n"
}
```

```
File created successfully at: entries/crcns-apl-1-bruno-2017/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/runtime_minutes: 19/runtime_minutes: 18/' entries/crcns-apl-1-bruno-2017/entry.yaml && python tools/entry.py check entries/crcns-apl-1-bruno-2017 2>&1 | tail -8 && python tools/entry.py handover entries/crcns-apl-1-bruno-2017 2>&1 | tail -5; ls executed/crcns-apl-1-bruno-2017/handover/; git status --short; date -u
```

```
0 error(s)
wrote executed/crcns-apl-1-bruno-2017/handover
10.7554-elife.27342.yaml
apl.py
reproduce_bruno_2017.ipynb
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
?? attempts/crcns-apl-1-bruno-2017-01.yaml
?? entries/crcns-apl-1-bruno-2017/
?? scripts
Sun Nov  8 14:02:58 UTC 2026
```

**Agent**

I've finished the attempt (steps 1 to 6). The entry `entries/crcns-apl-1-bruno-2017/` passes `tools/entry.py check` with 0 errors and ran from a clean environment in 1078 s (18 min). The handover is built in `executed/crcns-apl-1-bruno-2017/handover/`. Nothing is committed.

## 1. Outcomes per claim (30 claims)

| Claim | Outcome |
|---|---|
| dataset-size | partially reproduced: 10 preparations, 30 recordings and 1131 neurons match; recordings hold 75 to 160 neurons, so only 12 of 30 fall in 108 to 198 |
| fig1d, fig1e, fig2b, fig2ef, fig2e, fig2s2 | reproduced |
| fig3a-coalescence | not reproduced: coalesces within one period in 12 of 30, where the criterion needs 27 (the "dominated by recurrence" part holds in 30 of 30) |
| fig3c, fig3s1a, fig3d, fig3f | reproduced; the failing pairs are the ones the paper names (prep 4: pairs 1,2 and 1,3; prep 7: pairs 1,3 and 2,3) |
| fig3h-perturbations-return | partially reproduced, assumed: 15 of 16 return; both counts fall just below tolerance under the Methods' mean period, and are within it under the median |
| fig3i | reproduced, under reading (b) |
| fig4bc-stable-spiral | partially reproduced: the grand mean is a stable spiral, but only 8 of 10 preparations have 2 of 3 responses in the region |
| fig4c | reproduced, assumed (10.45 s) |
| fig4s1a | not reproduced: all dimensions contract in 11 of 30 |
| fig4s1b, fig5b, fig5c, fig6s1 | reproduced |
| fig6d-decode-p10 | partially reproduced: 8 of 9 (prep 4, response 1 fails) |
| fig6s2 | partially reproduced |
| fig7a, fig7f, halving, fig7s1 | reproduced |
| fig7gh | not reproduced, assumed: the outcome flips with the reading (see below) |
| fig7s2 | blocked, `not_runnable`: the ensemble-typing toolbox is MATLAB and porting it would not fit the time |
| fig8 | blocked, `metadata_insufficient`: nothing says how the photodiode array is oriented, so the caudo-lateral quadrant can't be located |

Totals: 20 reproduced, 5 partially reproduced, 3 not reproduced, 2 blocked.

## 2. What was found about the dataset

**Dataset**
- **Version pinned:** CRCNS data sets have no versions, so the version is `unversioned`. The bucket holds a single processed copy under `live/`; I pinned it by the MD5 sums of the files read, which match the dataset's own `checksums.md5`.
- **Matches its description:** 30 recordings, 1131 neurons, the stimulus at 30 s, P10 nerve recordings for preps 2, 4 and 5, no recording deposited twice.
- **Paper contradicts itself:** it gives 120 to 180 neurons per recording and 1131 in all. Ten preparations of at least 120 would hold at least 1200.
- **Sampling rate:** the P10 timing grid is 1629.7 Hz, which agrees with the description's 1630 Hz, not the paper's 1600 Hz.
- **File names:** the P10 files of prep 2 drop the "B" of `Jun0414B`.
- **Coordinates:** no unit and no orientation are given.
- **Clock:** the population and P10 rates are correlated after the stimulus, which is consistent with a shared clock, but the check doesn't separate the data from shifted series in 2 of 9 recordings.
- **Same neurons across bouts:** neuron identity across bouts is consistent with the data (30 of 30 bout pairs above permuted ids), and I used it as an assumption.

**Code mismatches**
- Figure 6D's N = 173 forecast windows matches the code's windowing (174 per response), not the Methods' (40 per response).
- `What_is_Participation.m` mismatches two of the three pairs.
- `LocalLinearDynamics.m` detects contiguous runs with a quirk that can miss gaps.

**Assumptions.** I adopted one reading where a single one had to be chosen: the kernel SD is the recording's own median ISI, and the number of PCs is the smallest reaching 80%. The Methods' printed width (median ISI / 12, or / √12) gives 21 to 76 dimensions, so it can't produce the paper's 4 to 8. Every reading is run in the notebook. The outcome changes with the reading for fig3h, fig4c and fig7gh. For fig7gh, the code's exact width and count rule would make it reproduced.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which kernel width was used, and was the median ISI per recording?
- Which PC-count rule produced Figures 2 to 5?
- For dropping divergences near the recording's end, is the cycle the mean or the median period, and does the rule apply to all of them or only to those that never return?
- Which permutation test gave Figure 5B?

**Questions to a reader:** none.

## 3. Where the protocol was unclear
1. The protocol doesn't say how far readings of an early detail (kernel width, PC count) must be carried into the claims that depend on it. I carried four readings through every claim, and the two unusable narrow widths only as far as fig2ef.
2. It doesn't say what `measured` should be for a claim stated as a range ("10 to 15 s"). I recorded the quartiles and let the criterion's count decide.
3. The clock check is described for trial tables. For continuous spikes plus a nerve recording I used cross-correlation against circular shifts, which is weak for a 10 s rhythm.
4. There's no rule for when a criterion's parts hold under different readings. fig6s2's dimension counts hold under the code's count rule, while its decoding part was run under the adopted one; I called it partial.
5. There's no rule choosing between partial and not reproduced when one part of a multi-part criterion fails. I used not reproduced when the main part failed (fig3a, fig4s1a).
6. For claims of absence the protocol says readings don't apply, but the inputs to the test (distances, participation) still have readings. For fig7gh I adopted one reading and marked it assumed.
7. The 10-minute aim conflicts with running every reading. The notebook takes 18 minutes, and the 90%-variance P10 models use 4 history lengths instead of the full grid.

## 4. Runtime and failures
- About 2 h in all (12:03 to 14:03 UTC). The notebook takes 18 min with peak memory about 1.3 GB.
- A development run of the 90% decoding with the code's windowing took 17 min, so it was left out of the notebook.
- One cell failed on the first development run (a pandas column name); it was fixed, and the final run's numbers are identical to the development run's.
- Untracked dotfiles (`.bashrc`, `.idea` and others) appeared in the repository root. They aren't mine and I left them alone.

## End of run

73 turns, 118 minutes, $8.42 at API prices, result: success.
