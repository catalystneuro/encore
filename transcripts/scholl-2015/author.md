# scholl-2015 · author · run 43640329576

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; wc -l docs/*.md README.md; ls entries/fouke-2025 claims attempts paper | head -50
```

```
Sat Nov 14 21:02:22 UTC 2026
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
[... 77 more lines not kept]
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
 "file_path": "claims/scholl-2015.yaml"
}
```

```
1	# Claims for Scholl, Pattadkal, Dilly, Priebe & Zemelman (2015), Neuron 87:424-436, "Local
2	# Integration Accounts for Weak Selectivity of Mouse Neocortical Parvalbumin Interneurons",
3	# doi:10.1016/j.neuron.2015.06.030, on CRCNS data set pvc-10 (doi:10.6080/K0GT5K3V).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14. The writer did not look at
6	# the data set's data or files; only its title and its data descriptor (paper/pvc-10.data-
7	# description.txt) were read, to know which experiments it is meant to hold.
8	#
9	# Text read: the version of record, as text extracted from the PDF under paper/ (main text,
10	# figure legends, Experimental Procedures) with the Supplemental Information (legends of
11	# Supplementary Figures 1 to 6) in the same file. The extraction prints micrometres as "mm",
12	# Greek lambda as "l" and minus signs as a replacement character; quotes copy the text as
13	# extracted. Equations in the Methods are garbled in the text; they were read in context.
14	#
15	# Code: the paper links no code. The Methods say images were analysed with custom MATLAB
16	# software, and cite CircStat (Berens, 2009) for the circular-linear correlation.
17	#
18	# Data the paper used. Six PV-Cre;Ai14 mice (P40-P60, urethane and chlorprothixene anaesthesia)
19	# with PV+ interneurons labelled by tdTomato, and two wild-type mice infected with
20	# rAAV CaMKIIa-nls-tdTomato (excitatory neurons labelled). V1 binocular zone bulk loaded with
[... 687 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | head -80; grep -n "CRCNS" -A60 docs/archives.md | head -120
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
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; cat paper/pvc-10.data-description.txt; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat papers/datasets/scholl-2015.yaml; ls entries | grep -i crcns; grep -l crcns entries/*/entry.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pvc-10/" -o l.xml; python3 -c "
import re
s=open('l.xml').read()
for k,sz in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',s): print(sz,k)
print('trunc', re.findall('<IsTruncated>(.*?)<',s))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-10; curl -s $B/live/filelist.txt | head -40; echo ----; curl -s $B/live/checksums.md5 | grep -v depth | head; curl -s $B/live/checksums.md5 | grep -c . ; curl -s $B/live/script/examplecode.m
```

```
# CRCNS.org 'pcv-10' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data/mouse10/mouse10depth125green.mat	1788544489 (1.6 GB)
 data/mouse10/mouse10depth125red.mat	1703662042 (1.5 GB)
 data/mouse10/mouse10depth125stim.mat	388
 data/mouse10/mouse10depth150green.mat	1461204862 (1.3 GB)
 data/mouse10/mouse10depth150red.mat	1387679300 (1.2 GB)
 data/mouse10/mouse10depth150stim.mat	352
 data/mouse10/mouse10depth175green.mat	1929789744 (1.7 GB)
 data/mouse10/mouse10depth175red.mat	1848378403 (1.7 GB)
 data/mouse10/mouse10depth175stim.mat	384
 data/mouse10/mouse10depth200green.mat	1637867244 (1.5 GB)
 data/mouse10/mouse10depth200red.mat	1559405726 (1.4 GB)
 data/mouse10/mouse10depth200stim.mat	369
 data/mouse10/mouse10depth225green.mat	1771452390 (1.6 GB)
 data/mouse10/mouse10depth225red.mat	1693880033 (1.5 GB)
 data/mouse10/mouse10depth225stim.mat	385
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "region|ROI|manual|identif|segment|custom|tdTomato expression|neuropil" paper/10.1016-j.neuron.2015.06.030.txt | head -60; wc -l paper/10.1016-j.neuron.2015.06.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 765,880p paper/10.1016-j.neuron.2015.06.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  date -u; python -c "import fsspec, h5py, scipy, numpy, aiohttp; print(fsspec.__version__, h5py.__version__, scipy.__version__)"; cat entries/fouke-2025/README.md | head -30; sed -n 1,60p tools/entry.py | head -60
```

```
Sat Nov 14 21:03:19 UTC 2026
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec, h5py, scipy, numpy, aiohttp; print(fsspec.__version__, h5py.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'fsspec'
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
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q sv && . sv/bin/activate && uv pip install -q fsspec aiohttp requests h5py scipy numpy matplotlib && python -c "import fsspec,h5py; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > peek.py <<'EOF'
import fsspec, io, scipy.io as sio, h5py
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-10/"
def head(p):
    with fsspec.open(B+p, block_size=2**16).open() as f:
        return f.read(140)
for p in ["live/data/mouse5/mouse5depth260green.mat","live/data/mouse5/mouse5depth260stim.mat","live/data/mouse5/mouse5stats.mat","live/script/cellmasks.mat","original/to_remove/binoc7PV.mat","original/to_remove/binoc10.mat","original/to_remove/binocmonocinds5.mat"]:
    print(p, head(p)[:120])
for p in ["live/data/mouse5/mouse5depth260stim.mat","live/data/mouse5/mouse5stats.mat"]+[f"live/data/mouse{m}/mouse{m}stats.mat" for m in (6,7,8,9,10)]:
    with fsspec.open(B+p).open() as f: d=sio.loadmat(io.BytesIO(f.read()))
    for k,v in d.items():
        if not k.startswith('__'): print(p,k,getattr(v,'shape',None)); print(v if v.size<40 else v[:12])
EOF
python peek.py
```

```
live/data/mouse5/mouse5depth260green.mat b'MATLAB 7.3 MAT-file, Platform: PCWIN64, Created on: Tue Jan 19 14:25:43 2016 HDF5 schema 1.00 .                     \x00\x00\x00\x00'
live/data/mouse5/mouse5depth260stim.mat b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Tue Jan 19 16:47:13 2016                                        \x00\x00\x00\x00'
live/data/mouse5/mouse5stats.mat b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Tue Feb 02 12:17:33 2016                                        \x00\x00\x00\x00'
live/script/cellmasks.mat b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Mon Feb 29 11:07:00 2016                                        \x00\x00\x00\x00'
original/to_remove/binoc7PV.mat b'MATLAB 7.3 MAT-file, Platform: MACI64, Created on: Sun Nov 23 02:12:02 2014 HDF5 schema 1.00 .                      \x00\x00\x00\x00'
original/to_remove/binoc10.mat b'MATLAB 7.3 MAT-file, Platform: MACI64, Created on: Sat Nov 22 15:48:38 2014 HDF5 schema 1.00 .                      \x00\x00\x00\x00'
original/to_remove/binocmonocinds5.mat b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Mon Nov 24 09:43:02 2014                                         \x00\x00\x00\x00'
live/data/mouse5/mouse5depth260stim.mat mouse5depth260stim (77, 2)
[[  91    2]
 [ 211    1]
 [ 329    5]
 [ 447    8]
 [ 565    4]
 [ 684    3]
 [ 802    6]
 [ 919    9]
 [1037    7]
 [1154   10]
 [1272   11]
 [1394    2]]
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > peek2.py <<'EOF'
import fsspec, h5py, time
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-10/"
def walk(p, maxshow=15):
    f=fsspec.open(B+p, block_size=2**20).open()
    h=h5py.File(f,'r')
    n=[0]
    def vis(name,obj):
        n[0]+=1
        if n[0]<=maxshow: print('  ',name, getattr(obj,'shape',''), getattr(obj,'dtype',''), dict(obj.attrs) if len(obj.attrs)<4 else '')
    h.visititems(vis); print('  total objects', n[0])
    return h
t=time.time()
h=walk("live/data/mouse5/mouse5depth260green.mat")
g=h['green']; print(g.shape,g.dtype, g.chunks, g.compression)
r=g[0,0] if g.shape[0]==1 else g[0,0]
d=h[r]; print('frame0', d.shape,d.dtype,d.chunks,d.compression, d[:].min(), d[:].max(), time.time()-t)
for p in ["original/to_remove/binoc7PV.mat","original/to_remove/binoc10.mat"]:
    print(p); walk(p, 40)
EOF
python peek2.py
```

```
#refs#   {'H5PATH': np.bytes_(b'/#refs#')}
   #refs#/0 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/0'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/00 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/00'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/00b (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/00b'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/01 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/01'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/01b (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/01b'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/02 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/02'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/02b (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/02b'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/03 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/03'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/03b (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/03b'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/04 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/04'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/04b (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/04b'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/05 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/05'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/05b (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/05b'), 'MATLAB_class': np.bytes_(b'double')}
   #refs#/06 (455, 256) float64 {'H5PATH': np.bytes_(b'/#refs#/06'), 'MATLAB_class': np.bytes_(b'double')}
  total objects 9438
(9435, 1) object (4717, 1) gzip
frame0 (455, 256) float64 (30, 256) gzip -501.0 2048.0 1781.5337762832642
original/to_remove/binoc7PV.mat
   #refs#   {'H5PATH': np.bytes_(b'/#refs#')}
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && date -u && cat > t3.py <<'EOF'
import fsspec, h5py, time, numpy as np
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-10/"
t=time.time()
f=fsspec.open(B+"live/data/mouse5/mouse5depth260green.mat", block_size=2**22, cache_type="readahead").open()
h=h5py.File(f,'r'); g=h['green']; refs=g[:,0]; print('open', time.time()-t, len(refs))
t=time.time()
for i in range(100):
    a=h[refs[i]][:]
print('100 frames', time.time()-t)
t=time.time()
for i in range(5000,5100):
    a=h[refs[i]][:]
print('100 frames later', time.time()-t)
print(h[refs[0]].id.get_offset(), h[refs[1]].id.get_offset(), h[refs[100]].id.get_offset())
EOF
python t3.py
```

```
Sat Nov 14 21:38:53 UTC 2026
open 1.2159545421600342 9435
100 frames 4.209931135177612
100 frames later 1.730595588684082
None None None
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > t4.py <<'EOF'
import fsspec, h5py, io, scipy.io as sio
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-10/"
f=fsspec.open(B+"original/to_remove/binoc7PV.mat", block_size=2**20).open()
h=h5py.File(f,'r')
for k in h.keys():
    if k.startswith('#'): continue
    o=h[k]; print(k, type(o).__name__, getattr(o,'shape',''), dict(o.attrs).get('MATLAB_class'))
    if isinstance(o,h5py.Group):
        for kk in o.keys(): print('   ',kk, o[kk].shape, o[kk].dtype)
for p in ["original/to_remove/binocmonocinds5.mat","original/to_remove/binocmonocinds5PV.mat","live/script/cellmasks.mat"]:
    with fsspec.open(B+p).open() as fh: d=sio.loadmat(io.BytesIO(fh.read()))
    for k,v in d.items():
        if not k.startswith('__'): print(p,k,v.shape,v.dtype, v.ravel()[:10] if v.ndim<3 else v.sum())
EOF
python t4.py
```

```
cePV Group  b'struct'
    Ftrace (99, 1) object
    cyc (99, 1) object
    date (99, 1) object
    depth (99, 1) object
    disparitypref (99, 1) object
    dsi (99, 1) object
    dsineuropil (99, 1) object
    filename (99, 1) object
    masks (99, 1) object
    neuropilcyc (99, 1) object
    neuropilpeaks (99, 1) object
    peakfit (99, 1) object
    peakfitparams (99, 1) object
    peaks (99, 1) object
    sampleG (99, 1) object
    sampleR (99, 1) object
    standard (99, 1) object
    windowlength (99, 1) object
    xy (99, 1) object
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p attempts/fouke-2025-01.yaml; grep -n "blocked_by\|kind: \|about:" attempts/fouke-2025-01.yaml | head -30; ls schemas; ls questions | head -3
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
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 195,330p attempts/fouke-2025-01.yaml; grep -l "crcns" attempts/*.yaml | head -2; grep -n -A8 "^datasets:" $(grep -l "archive: crcns" attempts/*.yaml | head -1); python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['provenance'],indent=0)[:1500])"
```

```
deviations:
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
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat entries/asari-2009/entry.yaml entries/asari-2009/requirements.in; ls entries/asari-2009; grep -n "python" entries/asari-2009/entry.yaml; grep -n -i "sanity\|tags" entries/asari-2009/*.ipynb | head -5
```

```
schema_version: 1
name: asari-2009
type: reproduction
title: Long-lasting context dependence in rat auditory cortex (Asari & Zador 2009)
description: Tests the findings of Asari and Zador (2009) on CRCNS ac-1, which holds their in vivo
  whole-cell recordings in rat A1 and cell-attached recordings in MGB, with natural and synthetic
  sound sequences, and the analysis code of the paper. It measures how long the response to a
  probe depends on the preceding sound, the response predictability without context, the
  dependence on sound properties, and the fast decay in thalamus. The voltage-clamp recordings of
  Figures 5 and 6 are not in the data set.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_asari_2009.ipynb
  title: Reproducing Asari & Zador (2009) from CRCNS ac-1
  runtime_minutes: 29
- path: strf_wehr.ipynb
  title: Figure 4 STRF and LN models of Wehr's recordings from CRCNS ac-1
  runtime_minutes: 22
helpers:
[... 28 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/scholl-2015/pvc10.py",
 "content": "\"\"\"Streaming access to CRCNS pvc-10 (Scholl et al. 2015, doi:10.6080/K0GT5K3V).\n\nThe data set is unversioned on CRCNS; the files read are those of its published\nfolder `pvc-10/live/`, at the MD5 sums its `checksums.md5` gives (printed by the\nnotebook). Files are read anonymously from the public S3 bucket `crcnsarchive`\nover range requests (fsspec), never downloaded to disk.\n\nWhat the published folder holds, per the data descriptor (docs/crcns_pvc-10_data_description.pdf):\n- `data/mouse<m>/mouse<m>depth<d>green.mat` and `...red.mat`: MATLAB 7.3 (HDF5) cell arrays\n  `green` / `red`, one 2-D frame per element;\n- `data/mouse<m>/mouse<m>depth<d>stim.mat`: two columns, the frame at which each stimulus\n  starts and its condition (1 blank, 2 to 9 binocular phases 0:45:315, 10 ipsilateral,\n  11 contralateral);\n- `data/mouse<m>/mouse<m>stats.mat`: per depth, the stimulus duration (s) and the x and y shift\n  (um) of the plane;\n- `script/cellmasks.mat`: 50 example cell masks for mouse5 depth 260 (descriptor, \"How to get\n  started\"; \"a mixture of responsive and nonresponsive cells\"), with no cell type.\n\nParameters and where they come from:\n- DARKNOISE = -160: the offset the data set's own examplecode.m subtracts from raw intensity\n  (\"based on our calibration experiments\"); used only in the data check.\n- F0_FRAMES = 10: frames before each stimulus onset used for Fo. The paper's Methods say only \"the\n  gray screen (Fo) immediately before the stimulus came on\"; examplecode.m defines a\n  pre-stimulus window `stim(i,1):(stim(i,1)+9)` of 10 frames. A standard choice for the data\n  check, which decides no claim.\n- RESP_WINDOW = 0.5 s centred on the average peak: Methods, Data Imaging Analysis (\"mean change\n  in fluorescence (DF/F) was calculated in a 0.5 s window, centered around the global average\n  peak\").\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nimport time\nimport urllib.request\n\nimport fsspec\nimport h5py\nimport numpy as np\nimport scipy.io as sio\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/\"\nDATASET = \"pvc-10\"\nVERSION = \"unversioned\"  # CRCNS data sets are not versioned (docs/archives.md, CRCNS)\nDOI = \"10.6080/K0GT5K3V\"\nLIVE = f\"{DATASET}/live/\"\n\nDARKNOISE = -160.0\nF0_FRAMES = 10\nRESP_WINDOW_S = 0.5\n\nCONDITIONS = {1: \"blank\", **{k: f\"binocular {45 * (k - 2)} deg\" for k in range(2, 10)},\n              10: \"ipsilateral\", 11: \"contralateral\"}\n\n\ndef list_bucket(prefix: str = f\"{DATASET}/\") -> list[tuple[str, int]]:\n    \"\"\"All (key, size) pairs under a prefix of the bucket, following continuation tokens.\"\"\"\n    out, token = [], None\n    while True:\n        url = f\"{BUCKET}?list-type=2&prefix={prefix}\"\n        if token:\n            url += \"&continuation-token=\" + urllib.parse.quote(token)\n        xml = urllib.request.urlopen(url).read().decode()\n        out += [(k, int(s)) for k, s in re.findall(r\"<Key>(.*?)</Key>.*?<Size>(\\d+)</Size>\", xml, re.S)]\n        m = re.search(r\"<NextContinuationToken>(.*?)</NextContinuationToken>\", xml)\n        if not m:\n            return out\n        token = m.group(1)\n\n\ndef read_text(path: str) -> str:\n    with fsspec.open(BUCKET + path, \"rb\").open() as f:\n        return f.read().decode(\"utf-8\", \"replace\")\n\n\ndef checksums() -> dict[str, str]:\n    \"\"\"MD5 sums published in live/checksums.md5, keyed by path relative to live/.\"\"\"\n    out = {}\n    for line in read_text(LIVE + \"checksums.md5\").splitlines():\n        parts = line.split()\n        if len(parts) == 2:\n            out[parts[1]] = parts[0]\n    return out\n\n\ndef load_small_mat(path: str) -> dict:\n    \"\"\"A MATLAB 5 file read whole into memory (stim, stats and mask files are a few kB).\"\"\"\n    with fsspec.open(BUCKET + path, \"rb\").open() as f:\n        d = sio.loadmat(io.BytesIO(f.read()))\n    return {k: v for k, v in d.items() if not k.startswith(\"__\")}\n\n\ndef planes() -> dict[int, list[int]]:\n    \"\"\"Depths with a green, red and stim file, per mouse, from the bucket listing of live/data.\"\"\"\n    keys = [k for k, _ in list_bucket(LIVE + \"data/\")]\n    out: dict[int, set] = {}\n    for k in keys:\n        m = re.search(r\"mouse(\\d+)depth(\\d+)(green|red|stim)\\.mat$\", k)\n        if m:\n            out.setdefault(int(m.group(1)), set()).add(int(m.group(2)))\n    return {m: sorted(d) for m, d in sorted(out.items())}\n\n\ndef plane_path(mouse: int, depth: int, kind: str) -> str:\n    return f\"{LIVE}data/mouse{mouse}/mouse{mouse}depth{depth}{kind}.mat\"\n\n\ndef stim_table(mouse: int, depth: int) -> np.ndarray:\n    \"\"\"(n, 2) int array: onset frame (1-based, MATLAB) and condition 1 to 11.\"\"\"\n    d = load_small_mat(plane_path(mouse, depth, \"stim\"))\n    (v,) = d.values()\n    return np.asarray(v, dtype=int)\n\n\ndef stats_table(mouse: int) -> np.ndarray:\n    \"\"\"(n, 4): depth (um), stimulus duration (s), x shift (um), y shift (um).\"\"\"\n    d = load_small_mat(f\"{LIVE}data/mouse{mouse}/mouse{mouse}stats.mat\")\n    (v,) = d.values()\n    return np.asarray(v, dtype=float)\n\n\nclass Movie:\n    \"\"\"One channel of one plane, opened in place over HTTP range requests.\n\n    MATLAB stores the cell array as a (n_frames, 1) array of object references, each frame\n    a (455, 256) float64 dataset in HDF5 order, i.e. 256 rows by 455 columns in MATLAB.\n    `frame(i)` returns it in MATLAB orientation (rows, columns) = (256, 455).\n    \"\"\"\n\n    def __init__(self, mouse: int, depth: int, channel: str = \"green\"):\n        self.path = plane_path(mouse, depth, channel)\n        self._fh = fsspec.open(BUCKET + self.path, \"rb\", block_size=2**22,\n                               cache_type=\"readahead\").open()\n        self._h5 = h5py.File(self._fh, \"r\")\n        self._var = self._h5[channel]\n        self.refs = self._var[:, 0]\n        self.n_frames = len(self.refs)\n\n    def frame_dataset(self, i: int):\n        return self._h5[self.refs[i]]\n\n    def frame(self, i: int) -> np.ndarray:\n        return self._h5[self.refs[i]][:].T\n\n    def close(self):\n        self._h5.close()\n        self._fh.close()\n\n\ndef mask_traces(movie: Movie, masks: np.ndarray, frames=None) -> tuple[np.ndarray, float]:\n    \"\"\"Mean intensity in each mask, per frame, minus DARKNOISE (as examplecode.m does).\n\n    masks: (256, 455, n) in MATLAB orientation. Returns (n, n_frames) and the seconds taken.\n    Holds one frame at a time in memory.\n    \"\"\"\n    frames = range(movie.n_frames) if frames is None else frames\n    m = masks.astype(bool)\n    n = m.shape[2]\n    flat = m.reshape(-1, n)\n    counts = flat.sum(0)\n    out = np.empty((n, len(frames)))\n    t0 = time.time()\n    for j, i in enumerate(frames):\n        f = movie.frame(i).reshape(-1)\n        out[:, j] = (f @ flat) / counts - DARKNOISE\n    return out, time.time() - t0\n\n\ndef trial_dff(trace: np.ndarray, stim: np.ndarray, n_post: int, shift: int = 0) -> np.ndarray:\n    \"\"\"dF/F for each trial: (F - Fo) / Fo, Fo the mean of F0_FRAMES frames before onset.\n\n    trace: (n_cells, n_frames); stim onsets are 1-based. `shift` moves every onset by that many\n    frames (used for the clock check). Returns (n_cells, n_trials, n_post).\n    \"\"\"\n    on = stim[:, 0] - 1 + shift\n    out = np.full((trace.shape[0], len(on), n_post), np.nan)\n    for k, o in enumerate(on):\n        if o - F0_FRAMES < 0 or o + n_post > trace.shape[1]:\n            continue\n        f0 = trace[:, o - F0_FRAMES:o].mean(1, keepdims=True)\n        out[:, k] = (trace[:, o:o + n_post] - f0) / f0\n    return out\n"
}
```

```
File created successfully at: entries/scholl-2015/pvc10.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/scholl-2015 && sed -i 's/^import urllib.request$/import urllib.parse\nimport urllib.request/' pvc10.py && . $TMPDIR/sv/bin/activate && date -u && python -c "
import pvc10, numpy as np, time
P=pvc10.planes(); print({m:len(d) for m,d in P.items()}, sum(len(d) for d in P.values()))
for m,ds in P.items():
    st=pvc10.stats_table(m); print('mouse',m,'stats depths',st[:,0].astype(int).tolist(), 'dur',set(st[:,1]))
    for d in ds:
        s=pvc10.stim_table(m,d); c=np.bincount(s[:,1],minlength=12)[1:]; isi=np.diff(s[:,0])
        print(m,d,len(s),c.tolist(),'isi med',np.median(isi),isi.min(),isi.max(), 'first',s[0,0],'last',s[-1,0])
"
```

```
Sat Nov 14 21:40:43 UTC 2026
{5: 15, 6: 9, 7: 15, 8: 6, 9: 7, 10: 6} 58
mouse 5 stats depths [180, 200, 220, 238, 260, 280, 300, 320, 340, 360, 380, 225, 265, 282, 315] dur {np.float64(1.5)}
5 180 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 120 first 95 last 9051
5 200 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 121 first 97 last 9052
5 220 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 121 first 92 last 9052
5 225 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 122 first 141 last 9109
5 238 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 120 first 125 last 9082
5 260 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 117 122 first 91 last 9065
5 265 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 127 first 126 last 9094
5 280 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 122 first 105 last 9070
5 282 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 120 first 190 last 9153
5 300 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 123 first 121 last 9097
5 315 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 121 first 91 last 9066
5 320 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 117 121 first 122 last 9086
5 340 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 126 first 116 last 9067
5 360 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 125 first 109 last 9079
5 380 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 118.0 116 123 first 135 last 9099
mouse 6 stats depths [200, 220, 240, 260, 280, 300, 320, 340, 360] dur {np.float64(1.5)}
6 200 77 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7] isi med 134.0 132 149 first 119 last 10350
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && date -u && python -c "
import pvc10, numpy as np, time, hashlib
print(pvc10.stats_table(5)); print(pvc10.stats_table(7))
t=time.time()
P=pvc10.planes()
for m,ds in list(P.items())[:1]:
    for d in ds[:4]:
        for ch in ('green','red'):
            mv=pvc10.Movie(m,d,ch); f0=mv.frame(0); ds_=mv.frame_dataset(0)
            print(m,d,ch,mv.n_frames,f0.shape,ds_.dtype,f0.min(),f0.max(),round(f0.mean(),2),hashlib.md5(f0.tobytes()).hexdigest()[:8], round(time.time()-t,1))
            mv.close()
"
```

```
Sat Nov 14 21:41:08 UTC 2026
[[ 180.     1.5    0.     0. ]
 [ 200.     1.5    0.     0. ]
 [ 220.     1.5    0.     0. ]
 [ 238.     1.5    0.     0. ]
 [ 260.     1.5    0.     0. ]
 [ 280.     1.5    0.     0. ]
 [ 300.     1.5    0.     0. ]
 [ 320.     1.5    0.     0. ]
 [ 340.     1.5    0.     0. ]
 [ 360.     1.5    0.     0. ]
 [ 380.     1.5    0.     0. ]
 [ 225.     1.5  300.  -300. ]
 [ 265.     1.5  300.  -300. ]
 [ 282.     1.5  300.  -300. ]
 [ 315.     1.5  300.  -300. ]]
[[180.   2.   0.   0.]
 [200.   2.   0.   0.]
 [220.   2.   0.   0.]
 [240.   2. 157. -70.]
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && date -u && cat > $TMPDIR/proto.py <<'EOF'
import pvc10, numpy as np, time, resource
m,d=5,260
masks=pvc10.load_small_mat(pvc10.LIVE+"script/cellmasks.mat")["cellmasks"]
mv=pvc10.Movie(m,d,"green"); print(mv.n_frames)
tr,sec=pvc10.mask_traces(mv,masks); print('sec',sec, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
np.save('/tmp/claude/tr.npy' if False else __import__('os').environ['TMPDIR']+'/tr.npy',tr)
EOF
python $TMPDIR/proto.py
```

```
Exit code 1
Sat Nov 14 21:41:28 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/proto.py", line 1, in <module>
    import pvc10, numpy as np, time, resource
ModuleNotFoundError: No module named 'pvc10'
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && cd entries/scholl-2015 && PYTHONPATH=. python $TMPDIR/proto.py; date -u
```

```
9435
sec 214.97987008094788 0.200856
Sat Nov 14 21:45:08 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && cd entries/scholl-2015 && cat > $TMPDIR/p2.py <<'EOF'
import pvc10, numpy as np, os
tr=np.load(os.environ['TMPDIR']+'/tr.npy')
stim=pvc10.stim_table(5,260)
NP=60  # 2 s at ~30 Hz
def contrast(shift, labels=None):
    x=pvc10.trial_dff(tr,stim,NP,shift)  # cells,trials,frames
    lab=stim[:,1] if labels is None else labels
    r=np.nanmean(x[:,:,5:50],axis=2)
    blank=r[:,lab==1]; st=r[:,lab!=1]
    return np.nanmean(st)-np.nanmean(blank), r, lab
for s in [-118,-90,-60,-30,-15,0,15,30,60,90]:
    c,_,_=contrast(s); print(s, round(c*100,3))
rng=np.random.default_rng(0)
cs=[contrast(0, rng.permutation(stim[:,1]))[0] for _ in range(100)]
print('perm', np.percentile(np.array(cs)*100,[2.5,50,97.5]))
# responsiveness index per cell
c,r,lab=contrast(0)
mb=r[:,lab==1].mean(1); sb=r[:,lab==1].std(1,ddof=1)/np.sqrt(7)
idx=np.stack([(r[:,lab==k].mean(1)-mb)/(r[:,lab==k].std(1,ddof=1)/np.sqrt(7)+sb) for k in range(2,12)],1)
print('cells with index>=1 any binoc',(idx[:,:8]>=1).any(1).sum(),'any monoc',(idx[:,8:]>=1).any(1).sum())
x=pvc10.trial_dff(tr,stim,118,0); avg=np.nanmean(x[:,stim[:,1]!=1],axis=(0,1)); print('avg time course peak frame', np.argmax(avg), np.round(avg[::6]*100,2))
EOF
PYTHONPATH=. python $TMPDIR/p2.py
```

```
/tmp/claude-1001/p2.py:8: RuntimeWarning: Mean of empty slice
  r=np.nanmean(x[:,:,5:50],axis=2)
-118 -0.223
-90 -0.54
-60 0.301
-30 0.48
-15 0.613
0 1.291
15 2.125
30 1.711
60 -0.456
90 -1.394
perm [-0.63115681  0.02599413  0.61752207]
cells with index>=1 any binoc 41 any monoc 15
avg time course peak frame 52 [-0.16  0.04 -0.19 -0.11  0.48  1.41  2.11  1.94  2.07  2.17  1.92  1.93
  1.77  2.13  1.78  1.28  0.89  0.44  0.28  0.2 ]
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && cd entries/scholl-2015 && date -u && python -c "
import pvc10, fsspec, h5py, scipy.io as sio, io, time
t=time.time()
for k,s in pvc10.list_bucket('pvc-10/original/'):
    if not k.endswith('.mat'): continue
    if 'binocmonocinds' in k:
        d=pvc10.load_small_mat(k); print(k, {a:v.size for a,v in d.items()}); continue
    f=fsspec.open(pvc10.BUCKET+k,'rb',block_size=2**20).open(); h=h5py.File(f,'r')
    for top in h.keys():
        if top.startswith('#'): continue
        o=h[top]
        if isinstance(o,h5py.Group):
            fs=list(o.keys()); print(k, s//10**6,'MB', top, 'n', o[fs[0]].shape, len(fs),'fields')
            if 'depth' in o:
                deps=[float(h[r][()].ravel()[0]) for r in o['depth'][:,0]]
                import collections; print('   depths', sorted(collections.Counter(deps).items()))
        else: print(k, top, o.shape)
    print('  t', round(time.time()-t,1))
"
```

```
Exit code 1
Sat Nov 14 21:45:35 UTC 2026
Traceback (most recent call last):
  File "<string>", line 8, in <module>
    f=fsspec.open(pvc10.BUCKET+k,'rb',block_size=2**20).open(); h=h5py.File(f,'r')
                                                                  ~~~~~~~~~^^^^^^^
  File "/tmp/claude-1001/sv/lib/python3.13/site-packages/h5py/_hl/files.py", line 555, in __init__
    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)
  File "/tmp/claude-1001/sv/lib/python3.13/site-packages/h5py/_hl/files.py", line 232, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 106, in h5py.h5f.open
OSError: Unable to synchronously open file (truncated file: eof = 1401290240, sblock->base_addr = 512, stored_eof = 1425407117)
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && cd entries/scholl-2015 && date -u && python -c "
import pvc10, fsspec, h5py, time, collections
t=time.time()
for k,s in pvc10.list_bucket('pvc-10/original/'):
    if not k.endswith('.mat'): continue
    if 'binocmonocinds' in k:
        d=pvc10.load_small_mat(k); print(k, {a:v.size for a,v in d.items()}); continue
    try:
        f=fsspec.open(pvc10.BUCKET+k,'rb',block_size=2**20).open(); h=h5py.File(f,'r')
    except OSError as e: print(k,'ERR',e); continue
    for top in h.keys():
        if top.startswith('#'): continue
        o=h[top]
        fs=list(o.keys()); print(k, s//10**6,'MB', top, 'n', o[fs[0]].shape, len(fs),'fields', fs if 'PV' not in k and '10' in k else '')
        if 'depth' in o:
            deps=[float(h[r][()].ravel()[0]) for r in o['depth'][:,0]]
            print('   depths', sorted(collections.Counter(deps).items()))
    print('  t', round(time.time()-t,1))
"
```

```
Sat Nov 14 21:45:42 UTC 2026
pvc-10/original/to_remove/1452382802_binoc7.mat ERR Unable to synchronously open file (truncated file: eof = 1401290240, sblock->base_addr = 512, stored_eof = 1425407117)
pvc-10/original/to_remove/binoc10.mat 154 MB ce n (84, 1) 20 fields ['Ftrace', 'cyc', 'date', 'depth', 'disparitypref', 'dsi', 'dsineuropil', 'filename', 'masks', 'neuropilcyc', 'neuropilpeaks', 'peakfit', 'peakfitparams', 'peaks', 'sampleG', 'sampleR', 'standard', 'windowlength', 'xy', 'xyshft']
   depths [(125.0, 8), (150.0, 14), (175.0, 16), (200.0, 11), (225.0, 25), (275.0, 10)]
  t 2.7
pvc-10/original/to_remove/binoc10PV.mat 25 MB cePV n (14, 1) 20 fields 
   depths [(125.0, 2), (150.0, 1), (175.0, 1), (200.0, 1), (225.0, 4), (275.0, 5)]
  t 4.0
pvc-10/original/to_remove/binoc7.mat ERR Unable to synchronously open file (truncated file: eof = 719584768, sblock->base_addr = 512, stored_eof = 1425407117)
pvc-10/original/to_remove/binoc7PV.mat 183 MB cePV n (99, 1) 20 fields 
   depths [(180.0, 7), (200.0, 2), (220.0, 8), (240.0, 6), (260.0, 5), (280.0, 4), (300.0, 10), (320.0, 4), (340.0, 6), (360.0, 7), (380.0, 6), (400.0, 7), (420.0, 8), (440.0, 10), (460.0, 9)]
  t 5.6
pvc-10/original/to_remove/binoc7new.mat ERR Unable to synchronously open file (truncated file: eof = 1399848448, sblock->base_addr = 512, stored_eof = 1425407117)
pvc-10/original/to_remove/binoc8.mat 131 MB ce n (72, 1) 20 fields ['Ftrace', 'cyc', 'date', 'depth', 'disparitypref', 'dsi', 'dsineuropil', 'filename', 'masks', 'neuropilcyc', 'neuropilpeaks', 'peakfit', 'peakfitparams', 'peaks', 'sampleG', 'sampleR', 'standard', 'windowlength', 'xy', 'xyshft']
   depths [(205.0, 5), (220.0, 6), (235.0, 12), (250.0, 21), (265.0, 12), (280.0, 16)]
  t 7.4
pvc-10/original/to_remove/binoc8PV.mat 44 MB cePV n (24, 1) 20 fields 
   depths [(205.0, 4), (220.0, 5), (235.0, 5), (250.0, 3), (265.0, 4), (280.0, 3)]
  t 9.0
pvc-10/original/to_remove/binoc9.mat 486 MB ce n (265, 1) 20 fields ['Ftrace', 'cyc', 'date', 
[... 17 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/scholl-2015/make_nb.py",
 "content": "import nbformat as nbf\n\nnb = nbf.v4.new_notebook()\nC = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s)\n    if tags:\n        c.metadata[\"tags\"] = tags\n    C.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s)\n    if tags:\n        c.metadata[\"tags\"] = tags\n    C.append(c)\n\n\nmd(\"\"\"# Scholl et al. (2015) on CRCNS pvc-10\n\nPaper: Scholl, Pattadkal, Dilly, Priebe and Zemelman (2015), \"Local Integration Accounts for Weak\nSelectivity of Mouse Neocortical Parvalbumin Interneurons\", Neuron 87:424-436,\ndoi:10.1016/j.neuron.2015.06.030. Claims file: `claims/scholl-2015.yaml`, written from the version\nof record (main text, Experimental Procedures and Supplemental Information legends).\n\nData set: CRCNS pvc-10, \"Disparity selectivity in mouse V1 measured using two-photon calcium\nimaging\", doi:10.6080/K0GT5K3V, read anonymously from the public S3 bucket `crcnsarchive`.\n\nVersion. CRCNS data sets are not versioned, so the version is recorded as `unversioned`. The files\nread are those of the data set's published folder `pvc-10/live/`, the only folder its file list\n(`live/filelist.txt`) and its `live/checksums.md5` describe; the MD5 sums of every file read are\nprinted below, so that a later change is detectable. The bucket also holds a folder\n`pvc-10/original/to_remove/` with older processed files that are in neither list and are marked for\nremoval. They are not a published version and cannot be pinned, so no result here uses them; the\nnotebook only lists what they hold, as a finding about the data set.\n\nOutcome in brief. The published folder holds the raw two-photon movies (green and red channels),\nthe stimulus tables and per-mouse plane shifts of 6 PV-Cre;Ai14 mice, and 50 example cell masks for\none plane. It holds no cell masks for the paper's 4,320 cells, no PV+/PV- labels, no responses or\nmeasures per cell, no neuropil patches, no histology and no CaMKIIa animals. Every claim rests on\nthe paper's hand-identified cells or on data not deposited, so every claim is blocked.\n\n| Claim | Outcome | Reason |\n|---|---|---|\n| fig1e-pv-tdtomato-colocalization | blocked | data_missing: no histology in the data set |\n| cell-counts-responsive | blocked | data_missing: the paper's cell masks and PV+/PV- labels are not deposited |\n| fig3abc-pv-more-binocular-fraction | blocked | data_missing, as above |\n| fig3c-contralateral-bias | blocked | data_missing, as above |\n| fig3-pv-lower-monocularity | blocked | data_missing, as above |\n| mi-per-animal | blocked | data_missing, as above |\n| fig3def-pv-weaker-disparity-selectivity | blocked | data_missing, as above |\n| mi-dsi-relation | blocked | data_missing, as above |\n| pv-larger-dff-low-dsi | blocked | data_missing, as above |\n| figs3-pv-distinct-from-neuropil | blocked | data_missing: cells and neuropil patches not deposited |\n| fig4ag-salt-and-pepper | blocked | data_missing, as above |\n| fig4d-pv-od-matches-local-50um | blocked | data_missing, as above |\n| fig4f-pv-od-spatial-decay | blocked | data_missing, as above |\n| fig4f-od-length-constant | blocked | data_missing, as above |\n| fig4ef-pvminus-od-unrelated | blocked | data_missing, as above |\n| figs6ab-pvminus-pv-like-od | blocked | data_missing, as above |\n| figs4-same-plane-control | blocked | data_missing, as above |\n| figs5-neuropil-no-relation | blocked | data_missing: neuropil patches not deposited |\n| fig5-camkii-responsive | blocked | data_missing: the CaMKIIa animals are not in the data set |\n| fig5e-camkii-od-unrelated | blocked | data_missing, as above |\n| fig4i-pv-disparity-matches-local | blocked | data_missing: cells and labels not deposited |\n| fig4k-pv-disparity-length-constant | blocked | data_missing, as above |\n| fig4jk-pvminus-disparity-weak | blocked | data_missing, as above |\n| figs6cd-pvminus-pv-like-disparity | blocked | data_missing, as above |\n| fig5f-camkii-disparity-unrelated | blocked | data_missing: the CaMKIIa animals are not in the data set |\n\"\"\")\n\ncode(\"\"\"import collections\nimport hashlib\nimport resource\nimport time\n\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nimport pvc10\n\nT0 = time.time()\nprint(\"dataset\", pvc10.DATASET, pvc10.VERSION, \"doi\", pvc10.DOI, \"folder\", pvc10.LIVE)\"\"\")\n\nmd(\"\"\"## Data check\n\n### Files in the bucket\n\nThe data descriptor (live/docs, Version 0.8, April 8, 2016) says the data are from 6 animals in\nfolders mouse5 to mouse10, with green and red channel movies and a stimulus file per plane and a\nstats file per mouse. It also says \"The dataset provided here contains information about the\nfluorescence traces, peak responses per condition, the measured binocular characteristics for each\ncell like its disparity selectivity index, preferred relative disparity, the position of the cell in\nthe imaging volume\". The listing below checks what is there.\"\"\")\n\ncode(\"\"\"listing = pvc10.list_bucket()\nby_folder = collections.defaultdict(lambda: [0, 0])\nfor k, s in listing:\n    if k.endswith(\"/\"):\n        continue\n    parts = k.split(\"/\")\n    folder = \"/\".join(parts[1:3]) if parts[1] == \"live\" else \"/\".join(parts[1:3])\n    if parts[1] == \"live\" and parts[2] == \"data\":\n        folder = \"live/data/\" + parts[3]\n    by_folder[folder][0] += 1\n    by_folder[folder][1] += s\nprint(f\"{'folder':28s} {'files':>6s} {'GB':>8s}\")\nfor f, (n, s) in sorted(by_folder.items()):\n    print(f\"{f:28s} {n:6d} {s / 1e9:8.2f}\")\nlive_data = [(k, s) for k, s in listing if k.startswith(pvc10.LIVE + \"data/\") and not k.endswith(\"/\")]\nprint(\"live/data total\", round(sum(s for _, s in live_data) / 1e9, 1), \"GB in\", len(live_data), \"files\")\n\nkinds = collections.Counter()\nfor k, _ in live_data:\n    name = k.rsplit(\"/\", 1)[1]\n    kind = (\"green\" if name.endswith(\"green.mat\") else \"red\" if name.endswith(\"red.mat\")\n            else \"stim\" if name.endswith(\"stim.mat\") else \"stats\" if name.endswith(\"stats.mat\") else \"other\")\n    kinds[kind] += 1\nprint(\"live/data files by kind\", dict(kinds))\nprint(\"files in live/ outside data/:\", [k.split(\"live/\")[1] for k, _ in listing\n                                         if k.startswith(pvc10.LIVE) and \"/data/\" not in k and not k.endswith(\"/\")])\"\"\",\n     tags=[\"sanity\"])\n\ncode(\"\"\"P = pvc10.planes()\nmd5 = pvc10.checksums()\nprint(\"planes per mouse:\", {m: len(d) for m, d in P.items()}, \"total\", sum(len(d) for d in P.values()))\nprint(\"paper: 6 animals, 6 to 15 focal planes each, 150 to 460 um below the pia\")\nfor m, ds in P.items():\n    st = pvc10.stats_table(m)\n    same = sorted(st[:, 0].astype(int).tolist()) == ds\n    shifts = sorted({(float(a), float(b)) for a, b in st[:, 2:]})\n    print(f\"mouse{m}: depths {ds[0]} to {ds[-1]} um; stats depths match file names: {same}; \"\n          f\"stimulus duration {sorted(set(st[:, 1]))} s; plane shifts (x, y um) {shifts}\")\nlisted = set(md5)\nmissing_md5 = [k for k, _ in live_data if k.split(\"live/\")[1] not in listed]\nprint(\"live/data files without an MD5 in checksums.md5:\", len(missing_md5))\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"### Stimulus tables\n\nEach stim file has two columns: the frame at which a stimulus starts and its condition (1 blank,\n2 to 9 the binocular phases 0 to 315 deg, 10 ipsilateral, 11 contralateral). The paper says 6 to\n7 repeats per focal plane, a 1.5 to 2 s stimulus followed by a 3 s blank, and imaging at 30 Hz.\"\"\")\n\ncode(\"\"\"stims = {}\nrows = []\nfor m, ds in P.items():\n    dur = pvc10.stats_table(m)[0, 1]\n    for d in ds:\n        s = pvc10.stim_table(m, d)\n        stims[(m, d)] = s\n        counts = np.bincount(s[:, 1], minlength=12)[1:]\n        isi = np.diff(s[:, 0])\n        rows.append((m, d, len(s), counts.min(), counts.max(), set(s[:, 1]) == set(range(1, 12)),\n                     np.median(isi), isi.min(), isi.max(), dur))\nprint(f\"{'mouse':>5s} {'depth':>5s} {'trials':>6s} {'rep min':>7s} {'rep max':>7s} {'11 conds':>8s} \"\n      f\"{'ISI med':>7s} {'min':>4s} {'max':>5s} {'stim s':>6s}\")\nfor r in rows:\n    print(f\"{r[0]:5d} {r[1]:5d} {r[2]:6d} {r[3]:7d} {r[4]:7d} {str(r[5]):>8s} {r[6]:7.0f} {r[7]:4d} {r[8]:5d} {r[9]:6.1f}\")\nreps = np.array([[r[3], r[4]] for r in rows])\nprint(\"planes with fewer than 6 repeats of some condition:\",\n      [(r[0], r[1], r[3]) for r in rows if r[3] < 6])\nprint()\nprint(\"Implied frame rate if each cycle is the stimulus plus a 3 s blank (Methods):\")\nfor m in P:\n    isi = np.median(np.concatenate([np.diff(stims[(m, d)][:, 0]) for d in P[m]]))\n    dur = pvc10.stats_table(m)[0, 1]\n    print(f\"  mouse{m}: median onset interval {isi:.0f} frames, cycle {dur + 3:.1f} s -> \"\n          f\"{isi / (dur + 3):.1f} frames/s; at 30 Hz the interval is {isi / 30:.2f} s\")\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"### Movies\n\nFor every plane, the frame count and frame shape of both channels, the range of the first frame,\nand a hash of the first green frame, to look for recordings deposited twice. Only the first frame\nof each file is read here.\"\"\")\n\ncode(\"\"\"t = time.time()\nmovies = {}\nfor m, ds in P.items():\n    for d in ds:\n        for ch in (\"green\", \"red\"):\n            mv = pvc10.Movie(m, d, ch)\n            f0 = mv.frame(0)\n            movies[(m, d, ch)] = dict(n=mv.n_frames, shape=f0.shape, dtype=str(mv.frame_dataset(0).dtype),\n                                      lo=f0.min(), hi=f0.max(), mean=f0.mean(),\n                                      h=hashlib.md5(f0.tobytes()).hexdigest(), img=f0[::4, ::4].copy())\n            mv.close()\nprint(f\"read {len(movies)} files in {time.time() - t:.0f} s\")\nprint(\"frame shapes (rows, columns):\", collections.Counter(v[\"shape\"] for v in movies.values()))\nprint(\"dtypes:\", collections.Counter(v[\"dtype\"] for v in movies.values()))\nfor ch in (\"green\", \"red\"):\n    lo = [v[\"lo\"] for k, v in movies.items() if k[2] == ch]\n    hi = [v[\"hi\"] for k, v in movies.items() if k[2] == ch]\n    mn = [v[\"mean\"] for k, v in movies.items() if k[2] == ch]\n    print(f\"{ch}: first-frame minimum {min(lo):.0f} to {max(lo):.0f}, maximum {min(hi):.0f} to {max(hi):.0f}, \"\n          f\"mean {min(mn):.1f} to {max(mn):.1f}\")\nmismatch = [(m, d) for m, ds in P.items() for d in ds if movies[(m, d, 'green')]['n'] != movies[(m, d, 'red')]['n']]\nprint(\"planes whose green and red frame counts differ:\", mismatch)\nshort = [(m, d) for m, ds in P.items() for d in ds\n         if stims[(m, d)][-1, 0] + np.median(np.diff(stims[(m, d)][:, 0])) > movies[(m, d, 'green')]['n']]\nprint(\"planes whose last stimulus cycle runs past the last frame:\", short)\nnf = [movies[(m, d, 'green')]['n'] for m, ds in P.items() for d in ds]\nprint(\"frames per plane:\", min(nf), \"to\", max(nf))\nhashes = collections.Counter(v[\"h\"] for k, v in movies.items())\nprint(\"first frames identical between files:\", [h for h, c in hashes.items() if c > 1])\n# similarity of first green frames between planes of the same mouse\nfor m, ds in P.items():\n    imgs = np.array([movies[(m, d, 'green')]['img'].ravel() for d in ds])\n    c = np.corrcoef(imgs)\n    np.fill_diagonal(c, np.nan)\n    print(f\"mouse{m}: highest correlation of first green frames between two planes {np.nanmax(c):.3f}\")\nprint(\"descriptor: frames of 255 by 456 pixels; paper: 256 by 455 pixels; 300 um field\")\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"### What the published files hold per cell\n\nThe paper's cells \"were identified by hand from structure images based on size, shape, and\nbrightness\" and PV+ cells \"by selecting OGB-1-filled neurons with co-localized tdTomato\nfluorescence\" (Experimental Procedures, Data Imaging Analysis). Every claim needs those cells,\ntheir masks and their PV+/PV- labels. The only masks in the published folder are the example ones\nin `live/script/cellmasks.mat`.\"\"\")\n\ncode(\"\"\"cm = pvc10.load_small_mat(pvc10.LIVE + \"script/cellmasks.mat\")\nfor k, v in cm.items():\n    print(k, v.shape, v.dtype, \"values\", np.unique(v).tolist(), \"pixels per mask\",\n          int(v.sum(axis=(0, 1)).min()), \"to\", int(v.sum(axis=(0, 1)).max()))\nprint(\"variables in every stim file:\", sorted({tuple(pvc10.load_small_mat(pvc10.plane_path(m, d, 'stim')).keys())[0][:5]\n                                               for m, d in list(stims)[:3]}), \"...\")\nprint(\"per-cell files in live/ (masks, labels, responses, positions):\",\n      [k for k, _ in listing if k.startswith(pvc10.LIVE) and any(w in k.lower() for w in (\"mask\", \"cell\", \"roi\", \"pv\", \"binoc\"))])\"\"\",\n     tags=[\"sanity\"])\n\nmd(\"\"\"The folder `original/to_remove/`, outside the published folder, holds MATLAB structs from\nNovember 2014. They are listed here, to describe the finding; no claim uses them.\"\"\")\n\ncode(\"\"\"t = time.time()\nimport fsspec, h5py\nfor k, s in pvc10.list_bucket(pvc10.DATASET + \"/original/\"):\n    if not k.endswith(\".mat\"):\n        continue\n    name = k.rsplit(\"/\", 1)[1]\n    if name.startswith(\"binocmonocinds\"):\n        d = pvc10.load_small_mat(k)\n        print(f\"{name:28s} {s:>11d} B  indices: {d['inds'].size}\")\n        continue\n    try:\n        fh = fsspec.open(pvc10.BUCKET + k, \"rb\", block_size=2**20).open()\n        h = h5py.File(fh, \"r\")\n    except OSError as e:\n        print(f\"{name:28s} {s:>11d} B  cannot be opened: {e}\")\n        continue\n    for top in [x for x in h.keys() if not x.startswith(\"#\")]:\n        g = h[top]\n        fields = list(g.keys())\n        deps = collections.Counter(float(h[r][()].ravel()[0]) for r in g[\"depth\"][:, 0])\n        print(f\"{name:28s} {s:>11d} B  struct {top}: {g[fields[0]].shape[0]} entries, depths {sorted(deps)}\")\n    h.close()\nprint(\"fields:\", fields)\nprint(f\"({time.time() - t:.0f} s)\")\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"### The clock of the stimulus table, on the example plane\n\nThe descriptor's example plane (mouse5, depth 260 um) is the only one with masks. Its green movie\nis streamed whole, the mean intensity in each of the 50 example masks is taken per frame (minus the\noffset of -160 that the data set's `examplecode.m` subtracts), and dF/F per trial is computed with\nFo the 10 frames before onset (a standard choice; see the helper). If the stimulus table shares the\nmovie's clock, stimulus trials should differ from blank trials in a window after onset, and the\ndifference should fall when the onsets are moved or the condition labels shuffled. This checks one\nplane of 58; the others are named as not checked.\"\"\")\n\ncode(\"\"\"M, D = 5, 260\nmasks = cm[\"cellmasks\"]\nmv = pvc10.Movie(M, D, \"green\")\ntraces, secs = pvc10.mask_traces(mv, masks)\nmv.close()\nstim = stims[(M, D)]\nsize_gb = dict(live_data)[pvc10.plane_path(M, D, \"green\")] / 1e9\nprint(f\"streamed {traces.shape[1]} frames ({size_gb:.2f} GB) in {secs:.0f} s, \"\n      f\"{size_gb * 1e3 / secs:.1f} MB/s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nprint(\"raw trace range\", round(traces.min(), 1), \"to\", round(traces.max(), 1))\n\nN_POST = 118  # one onset interval of this plane (median 118 frames)\nx = pvc10.trial_dff(traces, stim, N_POST)\nlab = stim[:, 1]\navg_stim = np.nanmean(x[:, lab != 1], axis=(0, 1)) * 100\navg_blank = np.nanmean(x[:, lab == 1], axis=(0, 1)) * 100\npeak = int(np.argmax(avg_stim))\nprint(f\"mean dF/F over cells and stimulus trials peaks at frame {peak} after onset, {avg_stim[peak]:.2f}%; \"\n      f\"blank trials at that frame {avg_blank[peak]:.2f}%\")\nprint(\"mean dF/F (%) every 6 frames, stimulus trials:\", np.round(avg_stim[::6], 2).tolist())\nprint(\"mean dF/F (%) every 6 frames, blank trials:   \", np.round(avg_blank[::6], 2).tolist())\n\n# the paper's 0.5 s window, centred on the average peak (Methods); 0.5 s is 15 frames at 30 Hz\nhalf = 7\nwin = slice(max(peak - half, 0), peak + half + 1)\n\n\ndef contrast(shift=0, labels=None):\n    xx = pvc10.trial_dff(traces, stim, N_POST, shift)\n    r = np.nanmean(xx[:, :, win], axis=2)\n    ll = lab if labels is None else labels\n    return (np.nanmean(r[:, ll != 1]) - np.nanmean(r[:, ll == 1])) * 100, r\n\n\nc0, R = contrast()\nrng = np.random.default_rng(20150630)\nnull = np.array([contrast(0, rng.permutation(lab))[0] for _ in range(200)])\nprint(f\"stimulus minus blank in the window (frames {win.start} to {win.stop - 1}): {c0:.2f}% dF/F; \"\n      f\"with shuffled labels 95% range {np.percentile(null, 2.5):.2f} to {np.percentile(null, 97.5):.2f}, \"\n      f\"p = {(np.sum(np.abs(null) >= abs(c0)) + 1) / (len(null) + 1):.3f}\")\nshifts = [-118, -90, -60, -30, 0, 30, 60, 90]\ncs = [contrast(s)[0] for s in shifts]\nfor s, c in zip(shifts, cs):\n    print(f\"  onsets moved by {s:+4d} frames: stimulus minus blank {c:6.2f}%\")\n\n# responsiveness index of the Methods per mask, without the neuropil requirement\nn = np.array([np.sum(lab == k) for k in range(1, 12)])\nmb, sb = R[:, lab == 1].mean(1), R[:, lab == 1].std(1, ddof=1) / np.sqrt(n[0])\nidx = np.stack([(R[:, lab == k].mean(1) - mb) / (R[:, lab == k].std(1, ddof=1) / np.sqrt(n[k - 1]) + sb)\n                for k in range(2, 12)], 1)\nprint(\"example masks with index >= 1 for some binocular condition:\", int((idx[:, :8] >= 1).any(1).sum()),\n      \"of 50; for some monocular condition:\", int((idx[:, 8:] >= 1).any(1).sum()),\n      \"(the descriptor calls them a mixture of responsive and non-responsive cells)\")\n\nfig, ax = plt.subplots(1, 2, figsize=(10, 3.2))\nax[0].plot(avg_stim, label=\"stimulus trials\")\nax[0].plot(avg_blank, label=\"blank trials\")\nax[0].axvspan(win.start, win.stop - 1, color=\"0.9\")\nax[0].set_xlabel(\"frames after onset\"); ax[0].set_ylabel(\"mean dF/F (%)\"); ax[0].legend()\nax[1].plot(shifts, cs, \"o-\")\nax[1].axhspan(np.percentile(null, 2.5), np.percentile(null, 97.5), color=\"0.9\")\nax[1].set_xlabel(\"onset shift (frames)\"); ax[1].set_ylabel(\"stimulus minus blank (%)\")\nplt.tight_layout(); plt.show()\nprint(f\"plotted ranges: left {min(avg_stim.min(), avg_blank.min()):.2f} to {max(avg_stim.max(), avg_blank.max()):.2f}%; \"\n      f\"right {min(cs):.2f} to {max(cs):.2f}%; nothing outside the axes\")\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"### Red channel of the example masks\n\nThe descriptor says the red channel \"can be used to identify if the cell is parvalbumin positive or\nnot\", but gives no labels. The mean red intensity in each example mask over the first 160 frames\n(the number `examplecode.m` averages) shows what a reader would have to threshold, with no rule from\nthe paper or the data set to do it.\"\"\")\n\ncode(\"\"\"mv = pvc10.Movie(M, D, \"red\")\nred, rsecs = pvc10.mask_traces(mv, masks, range(160))\nred_img = np.mean([mv.frame(i) for i in range(0, 160, 8)], axis=0)\nmv.close()\nr = red.mean(1)\nprint(f\"red mean in the 50 masks: {r.min():.1f} to {r.max():.1f} (median {np.median(r):.1f}); \"\n      f\"whole-frame median {np.median(red_img) - pvc10.DARKNOISE:.1f}\")\nprint(\"masks sorted by red intensity:\", np.round(np.sort(r), 0).astype(int).tolist())\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"### Size of a full re-analysis\n\nRe-running the paper's analysis would need the cells identified anew in all 58 planes (by hand, in\nthe paper) and both channels streamed. The rate measured above gives the time to stream the movies\nalone.\"\"\")\n\ncode(\"\"\"movie_bytes = sum(s for k, s in live_data if k.endswith(\"green.mat\") or k.endswith(\"red.mat\"))\nrate = size_gb * 1e9 / secs\nprint(f\"{sum(1 for k, _ in live_data if k.endswith(('green.mat', 'red.mat')))} movies, {movie_bytes / 1e9:.0f} GB; \"\n      f\"at {rate / 1e6:.1f} MB/s, {movie_bytes / rate / 3600:.1f} h to stream once, against a 1 h notebook limit\")\nprint(f\"notebook time so far {(time.time() - T0) / 60:.1f} min\")\"\"\")\n\nmd(\"\"\"## Claims\n\nNo claim is tested. Every finding of the paper rests on its hand-identified cells (4,320 in the\nsix PV-Cre mice), their PV+/PV- labels, the CaMKIIa mice, the neuropil patches or the histology,\nand none of these is in the published data set. The reasons are in the table in the header and in\nthe attempt record.\n\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| fig1e-pv-tdtomato-colocalization | blocked, data_missing (histology) |\n| cell-counts-responsive, fig3abc-pv-more-binocular-fraction, fig3c-contralateral-bias, fig3-pv-lower-monocularity, mi-per-animal, fig3def-pv-weaker-disparity-selectivity, mi-dsi-relation, pv-larger-dff-low-dsi | blocked, data_missing (cell masks and PV labels) |\n| fig4ag-salt-and-pepper, fig4d-pv-od-matches-local-50um, fig4f-pv-od-spatial-decay, fig4f-od-length-constant, fig4ef-pvminus-od-unrelated, figs6ab-pvminus-pv-like-od, figs4-same-plane-control, fig4i-pv-disparity-matches-local, fig4k-pv-disparity-length-constant, fig4jk-pvminus-disparity-weak, figs6cd-pvminus-pv-like-disparity | blocked, data_missing (cell masks and PV labels) |\n| figs3-pv-distinct-from-neuropil, figs5-neuropil-no-relation | blocked, data_missing (cells and neuropil patches) |\n| fig5-camkii-responsive, fig5e-camkii-od-unrelated, fig5f-camkii-disparity-unrelated | blocked, data_missing (CaMKIIa animals) |\n\nHow the analysis differs from the paper's: no analysis of the paper was run. The data check reads\nevery stimulus and stats file and the first frame of every movie, and streams one plane with the\ndata set's 50 example masks.\n\nWhat was found about the data set, from the outputs above:\n\n- The published folder holds raw movies (green and red), stimulus tables and plane shifts for 58\n  planes of 6 mice, and 50 example masks for one plane. It holds none of the per-cell data that its\n  descriptor says it contains (fluorescence traces, peak responses per condition, DSI, preferred\n  disparity, cell positions), and no masks or PV+/PV- labels for the paper's cells.\n- The CaMKIIa-nls-tdTomato mice, the neuropil patches and the anti-PV histology are not in it.\n- A folder outside the published one, `original/to_remove/`, holds processed per-cell structs\n  (masks, peaks, DSI, disparity preference, positions, neuropil responses) for mice 7 to 10 only;\n  three of the mouse 7 files are truncated and cannot be opened.\n- The descriptor gives frames of 255 by 456 pixels; the files hold 256 by 455, as the paper says.\n- No frame rate is given in the data set. The onset intervals (118 frames in mouse 5, 131 to 134 in\n  the others) fit 30 Hz only if each cycle lasts 3.9 to 4.5 s, against the stimulus plus 3 s blank\n  (4.5 or 5 s) of the Methods.\n- Several planes have fewer than the 6 to 7 repeats the paper states (mouse 10 has 4 to 5).\n- On the example plane, stimulus trials differ from blank trials after onset, and the difference\n  falls when onsets are moved, so the stimulus table is consistent with the movie's clock there.\n\"\"\")\n\nnb[\"cells\"] = C\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"reproduce_scholl_2015.ipynb\")\n"
}
```

```
File created successfully at: entries/scholl-2015/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('make_nb.py').read()
s=s.replace("""the attempt record.

## Summary
""","""the attempt record.
\"\"\")

md(\"\"\"## Summary
""")
open('make_nb.py','w').write(s)
EOF
grep -n '## Summary' -B3 make_nb.py | head; cat > requirements.in <<'EOF'
aiohttp
fsspec
h5py
matplotlib
numpy
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: scholl-2015
type: reproduction
title: Binocular selectivity of PV+ interneurons in mouse V1 (Scholl et al. 2015)
description: Attempts the findings of Scholl, Pattadkal, Dilly, Priebe and Zemelman (2015) on CRCNS
  pvc-10, which holds the raw two-photon movies, stimulus tables and plane shifts of six PV-Cre;Ai14
  mice. The data set holds no masks or PV+/PV- labels for the paper's hand-identified cells, and
  none of the per-cell measures its descriptor lists, so every claim is blocked. The notebook checks
  the files against the descriptor and the paper and streams one plane with the data set's example
  masks to check the stimulus clock.
license: Apache-2.0
notebooks:
- path: reproduce_scholl_2015.ipynb
  title: Scholl et al. (2015) on CRCNS pvc-10, data check
  runtime_minutes: 8
helpers:
- pvc10.py
related:
- id: crcns:pvc-10/unversioned
  relation: uses_data
- id: doi:10.1016/j.neuron.2015.06.030
  relation: reproduces
EOF
. $TMPDIR/sv/bin/activate; pip list 2>/dev/null | grep -i nbformat || uv pip install -q nbformat; python make_nb.py && ls
```

```
Exit code 1
370-the attempt record.
371-""")
372-
373:md("""## Summary
nbformat                  5.11.1
Traceback (most recent call last):
  File "entries/scholl-2015/make_nb.py", line 1, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
```

**Agent calls Bash**

```bash
python make_nb.py && mv make_nb.py $TMPDIR/ && cd  && date -u && python tools/entry.py lock entries/scholl-2015 2>&1 | tail -5 && python tools/entry.py check entries/scholl-2015 2>&1 | tail -20
```

```
Sat Nov 14 21:47:49 UTC 2026
wrote scholl-2015/requirements.lock.txt (Python 3.13, with hashes)
error: entries/scholl-2015/reproduce_scholl_2015.ipynb: names a local path; stream the data from the archive
1 error(s)
```

**Agent calls Bash**

```bash
grep -n "local path" -B25 tools/entry.py | grep -n "re\.\|compile\|LOCAL" | head
```

```
26:394:    """Whether a local path in the code is inside the dataset directory `encore check` gave (ENCORE_LOCAL_DATA):
28:396-    allowed = os.environ.get("ENCORE_LOCAL_DATA", "").rstrip("/")
37:405-    if any(not _local_data(code, m.start() + 1) for m in LOCAL_PATH.finditer(code)):
```

**Agent calls Bash**

```bash
grep -n "^LOCAL_PATH" -A4 tools/entry.py; python - <<'EOF'
import re,sys,json
sys.path.insert(0,'tools')
import entry
nb=json.load(open('entries/scholl-2015/reproduce_scholl_2015.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        s=''.join(c['source'])
        for m in entry.LOCAL_PATH.finditer(s): print(repr(s[max(0,m.start()-40):m.end()+20]))
EOF
```

```
72:LOCAL_PATH = re.compile(r"""["'](?:~/|/(?:Users|home|tmp|mnt|media|Volumes|data|scratch)/|[A-Za-z]:[\\/])""")
73-LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)
74-
75-
76-class Report:
'        if k.startswith(pvc10.LIVE) and "/data/" not in k and not k'
```

**Agent calls Bash**

```bash
cd entries/scholl-2015 && sed -i 's|and "/data/" not in k and not|and not k.startswith(pvc10.LIVE + "data") and not|' $TMPDIR/make_nb.py && python $TMPDIR/make_nb.py && cd ../.. && python tools/entry.py check entries/scholl-2015 2>&1 | tail -5 && date -u && time python tools/entry.py run entries/scholl-2015 2>&1 | tail -15
```

```
0 error(s)
Sat Nov 14 21:48:06 UTC 2026
Installed kernelspec registry-scholl-2015 in executed/scholl-2015/.venv/share/jupyter/kernels/registry-scholl-2015
pass  reproduce_scholl_2015.ipynb  (361 s)

real	6m4.978s
user	8m15.037s
sys	0m29.044s
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/scholl-2015/reproduce_scholl_2015.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:6000])
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
    print('=====')
EOF
```

```
dataset pvc-10 unversioned doi 10.6080/K0GT5K3V folder pvc-10/live/

=====
folder                        files       GB
live/checksums.md5                1     0.00
live/data/mouse10                19    20.30
live/data/mouse5                 46    67.46
live/data/mouse6                 28    42.25
live/data/mouse7                 46    68.43
live/data/mouse8                 19    23.48
live/data/mouse9                 22    29.85
live/docs                         2     0.00
live/filelist.txt                 1     0.00
live/script                       2     0.00
original/to_remove               22     4.58
live/data total 251.8 GB in 180 files
live/data files by kind {'green': 58, 'red': 58, 'stim': 58, 'stats': 6}
files in live/ outside data/: ['checksums.md5', 'docs/crcns_pvc-10_data_description.doc', 'docs/crcns_pvc-10_data_description.pdf', 'filelist.txt', 'script/cellmasks.mat', 'script/examplecode.m']

=====
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/scholl-2015 && python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/make_nb.py'
s=open(p).read()
old_start=s.index('print("variables in every stim file:"')
old_end=s.index('tags=["sanity"])', old_start)
new='''print("files in live/ whose names suggest per-cell data (mask, cell, roi, pv, binoc):",
      [k.split("live/")[1] for k, _ in listing if k.startswith(pvc10.LIVE) and not k.endswith("/")
       and any(w in k.rsplit("/", 1)[1].lower() for w in ("mask", "cell", "roi", "pv", "binoc"))])""",
     '''
s=s[:old_start]+new+s[old_end:]
s=s.replace("""- No frame rate is given in the data set. The onset intervals (118 frames in mouse 5, 131 to 134 in
  the others) fit 30 Hz only if each cycle lasts 3.9 to 4.5 s, against the stimulus plus 3 s blank
  (4.5 or 5 s) of the Methods.""","""- No frame rate is given in the data set. At the paper's 30 Hz, the median onset intervals give
  cycles of 3.93 s in mouse 5 and 4.37 to 4.43 s in mice 7 to 10, against the 4.5 s and 5 s of the
  stimulus plus a 3 s blank in the Methods; mouse 6 (4.43 s against 4.5 s) fits. Either the frame
  rate or the blank differs from the Methods in five of six mice.
- In mouse 5 four planes are shifted by 300 um in x and -300 um in y, and in mouse 7 the planes
  from 240 um down by 157 and -70 um: a second field of view, which the files name only by these
  shifts.
- In four planes the last stimulus cycle runs past the last frame.""")
s=s.replace("""- Several planes have fewer than the 6 to 7 repeats the paper states (mouse 10 has 4 to 5).""","""- Eight planes have fewer than the 6 to 7 repeats the paper states for some condition (all six
  planes of mouse 10 have 4 or 5).
- No two movies share a first frame, and the first green frames of two planes of one mouse
  correlate at most 0.52 to 0.76, so no recording was found deposited twice.""")
open(p,'w').write(s)
EOF
python $TMPDIR/make_nb.py && cd ../.. && python tools/entry.py check entries/scholl-2015 | tail -2
```

```
0 error(s)
```

**Agent calls Bash**

```bash
ls attempts | grep scholl; ls questions | grep scholl; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(list(s['properties'])); o=s['properties']['outcomes']['items'];print(list(o['properties'])); print(json.dumps(s['properties']['findings']['items'],indent=0)[:1500])"
```

```
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"statement"
],
"properties": {
"kind": {
"enum": [
"metadata_error",
"data_missing",
"identifier_missing",
"metadata_insufficient",
"selection_undocumented",
"methods_unavailable",
"format_error",
"code_mismatch",
[... 31 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/scholl-2015-01.yaml",
 "content": "schema_version: 3\nid: scholl-2015-01\ndatasets:\n- archive: crcns\n  id: pvc-10\n  version: unversioned\n  doi: 10.6080/K0GT5K3V\n  relation: primary\npaper: doi:10.1016/j.neuron.2015.06.030\ndate: '2026-11-14'\nentry: scholl-2015\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43640329576\noutcomes:\n- claim: fig1e-pv-tdtomato-colocalization\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The post hoc anti-PV immunostaining (Experimental Procedures, Immunohistochemical\n    Analysis) is not in the data set, whose published folder holds only two-photon movies,\n    stimulus tables, plane shifts and 50 example masks. The paper names no other deposit.\n- claim: cell-counts-responsive\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The counts are of the paper's cells, which \"were identified by hand from structure images\n    based on size, shape, and brightness\", with PV+ cells chosen by co-localized tdTomato\n    (Experimental Procedures, Data Imaging Analysis). The published folder (pvc-10/live/) holds no\n    cell masks for its 58 planes, no PV+/PV- labels and no per-cell responses; its only masks are 50\n    unlabelled examples for mouse5 depth 260. Places looked, besides live/; the paper links no code\n    or other deposit; the bucket's folder original/to_remove/, outside the published file list and\n    checksums and marked for removal, holds processed per-cell structs (masks, peaks, DSI, positions)\n    but only for mice 7 to 10, with the three mouse 7 PV- files truncated, and cannot be pinned, so it\n    was not used. Identifying cells anew would be a method the paper does not give beyond hand\n    selection, and streaming the 252 GB of movies once takes an estimated 6.2 h at the 11.2 MB/s\n    measured in the notebook, against the 1 h notebook limit (too_large as a second reason).\n- claim: fig3abc-pv-more-binocular-fraction\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs ODI of the paper's PV+ and PV- cells; the cells and their labels are not in the data\n    set (see cell-counts-responsive). Depends on cell-counts-responsive.\n- claim: fig3c-contralateral-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig3abc-pv-more-binocular-fraction; cells and labels not deposited.\n- claim: fig3-pv-lower-monocularity\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig3abc-pv-more-binocular-fraction; cells and labels not deposited.\n- claim: mi-per-animal\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig3-pv-lower-monocularity; cells and labels not deposited. The six animals\n    themselves are in the data set (mouse5 to mouse10).\n- claim: fig3def-pv-weaker-disparity-selectivity\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs DSI of the paper's PV+ and PV- cells; cells and labels not deposited. Depends on\n    cell-counts-responsive.\n- claim: mi-dsi-relation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig3-pv-lower-monocularity and fig3def-pv-weaker-disparity-selectivity.\n- claim: pv-larger-dff-low-dsi\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig3def-pv-weaker-disparity-selectivity; cells and labels not deposited.\n- claim: figs3-pv-distinct-from-neuropil\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the PV+ cells and the neuropil patches (Supplementary Figure 5A, ROIs drawn by hand);\n    neither is in the data set. Depends on cell-counts-responsive.\n- claim: fig4ag-salt-and-pepper\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the visually responsive cells and their positions; no cell masks or per-cell\n    positions are deposited (see cell-counts-responsive).\n- claim: fig4d-pv-od-matches-local-50um\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig3abc-pv-more-binocular-fraction; cells, labels and positions not deposited.\n- claim: fig4f-pv-od-spatial-decay\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4d-pv-od-matches-local-50um.\n- claim: fig4f-od-length-constant\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4f-pv-od-spatial-decay.\n- claim: fig4ef-pvminus-od-unrelated\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4d-pv-od-matches-local-50um.\n- claim: figs6ab-pvminus-pv-like-od\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4ef-pvminus-od-unrelated.\n- claim: figs4-same-plane-control\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4f-pv-od-spatial-decay.\n- claim: figs5-neuropil-no-relation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The 480 neuropil patches, drawn by hand (Supplementary Figure 5A legend), are not in the\n    data set. Depends on fig4f-pv-od-spatial-decay and fig4k-pv-disparity-length-constant.\n- claim: fig5-camkii-responsive\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The two wild-type mice infected with rAAV CaMKIIa-nls-tdTomato are not in the data set,\n    which holds six PV-Cre animals (descriptor, \"Data files organization\"; folders mouse5 to\n    mouse10). The paper names no other deposit.\n- claim: fig5e-camkii-od-unrelated\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig5-camkii-responsive; the CaMKIIa animals are not in the data set.\n- claim: fig4i-pv-disparity-matches-local\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig3def-pv-weaker-disparity-selectivity; cells, labels and positions not\n    deposited.\n- claim: fig4k-pv-disparity-length-constant\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4i-pv-disparity-matches-local.\n- claim: fig4jk-pvminus-disparity-weak\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4i-pv-disparity-matches-local.\n- claim: figs6cd-pvminus-pv-like-disparity\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4jk-pvminus-disparity-weak.\n- claim: fig5f-camkii-disparity-unrelated\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig5-camkii-responsive and fig4i-pv-disparity-matches-local; the CaMKIIa\n    animals are not in the data set.\nfindings:\n- kind: data_missing\n  statement: The published data set (pvc-10/live/) holds the raw green and red two-photon movies\n    of 58 planes in 6 mice, their stimulus tables and plane shifts, and 50 unlabelled example cell\n    masks for one plane (mouse5, depth 260). It holds no masks for the cells the paper analysed\n    (identified by hand, 338 PV+ and 3,982 PV-), no PV+/PV- labels and no per-cell responses or\n    positions, so none of the paper's findings can be tested from it without identifying and\n    classifying the cells anew.\n- kind: metadata_error\n  statement: The data descriptor says the data set \"contains information about the fluorescence\n    traces, peak responses per condition, the measured binocular characteristics for each cell like\n    its disparity selectivity index, preferred relative disparity, the position of the cell in the\n    imaging volume\". None of these per-cell data are among the published files.\n- kind: other\n  about: data\n  statement: The bucket holds a folder pvc-10/original/to_remove/, not in the data set's file list\n    or checksums, with MATLAB structs from November 2014 that look like the paper's processed\n    per-cell data (fields masks, peaks, dsi, disparitypref, xy, neuropilcyc and others). They cover\n    mice 7 to 10 only (mice 5 and 6 have index files alone), and the three mouse 7 PV- files are\n    truncated and cannot be opened. If these are the paper's cells, publishing a complete set would\n    make the data set usable for the paper's analyses.\n- kind: data_missing\n  statement: The two rAAV CaMKIIa-nls-tdTomato mice of Figure 5, the neuropil patches of\n    Supplementary Figures 3 and 5, and the anti-PV histology of Figure 1E are not in the data set,\n    and the descriptor does not say they were left out.\n- kind: metadata_error\n  statement: The descriptor gives frames of 255 by 456 pixels and converts positions with 300/456\n    and 300/255 um per pixel. Every frame in the files is 256 by 455 pixels, as the paper states.\n- kind: metadata_insufficient\n  statement: The data set gives no frame rate. At the paper's 30 Hz, the median stimulus onset\n    intervals give cycles of 3.93 s in mouse 5 and 4.37 to 4.43 s in mice 7 to 10, against the 4.5 s\n    and 5 s that the stimulus durations in the stats files plus the Methods' 3 s blank give; only\n    mouse 6 fits. Either the frame rate or the blank differs from the Methods in five of six mice.\n- kind: other\n  about: data\n  statement: Eight planes have fewer than the 6 to 7 repeats per condition the paper states (all six\n    planes of mouse 10 have 4 or 5), and in four planes (mouse6 240 and 300, mouse8 250, mouse10 200)\n    the last stimulus cycle runs past the last frame. Mouse 10 includes a plane at 125 um, above the\n    150 um the Methods give as the start.\n"
}
```

```
File created successfully at: attempts/scholl-2015-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "entries/scholl-2015/README.md",
 "content": "# Scholl, Pattadkal, Dilly, Priebe & Zemelman (2015) on CRCNS pvc-10\n\nAttempts the findings of [Scholl et al. (2015)](https://doi.org/10.1016/j.neuron.2015.06.030) on\n[CRCNS pvc-10](https://doi.org/10.6080/K0GT5K3V). The published data set holds the raw two-photon\nmovies (green and red channels), stimulus tables and plane shifts of six PV-Cre;Ai14 mice, and 50\nunlabelled example cell masks for one plane. It holds no masks or PV+/PV- labels for the paper's\nhand-identified cells and none of the per-cell measures its descriptor lists, and it does not\ninclude the CaMKIIa mice, the neuropil patches or the histology. All 25 claims are blocked\n(`data_missing`).\n\nThe notebook checks the files against the descriptor and the paper (planes, repeats, frame sizes,\nonset intervals, duplicates), streams one plane with the example masks to check that the stimulus\ntable shares the movie's clock, and estimates the time to stream all 252 GB of movies.\n\nThe attempt record, with the reasons and the findings about the data set, is\n[`attempts/scholl-2015-01.yaml`](../../attempts/scholl-2015-01.yaml).\n"
}
```

```
File created successfully at: entries/scholl-2015/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/the three mouse 7 PV- files are\n/X/' attempts/scholl-2015-01.yaml; python - <<'EOF'
p='attempts/scholl-2015-01.yaml'; s=open(p).read()
s=s.replace("with the three mouse 7 PV- files truncated","with the three mouse 7 files without the PV suffix truncated")
s=s.replace("and the three mouse 7 PV- files are\n    truncated and cannot be opened","and the three mouse 7 files without the PV suffix\n    are truncated and cannot be opened")
open(p,'w').write(s)
EOF
grep -n "PV suffix" attempts/scholl-2015-01.yaml; date -u; python tools/entry.py all entries/scholl-2015 2>&1 | tail -8
```

```
40:    but only for mice 7 to 10, with the three mouse 7 files without the PV suffix truncated, and cannot be pinned, so it
164:    mice 7 to 10 only (mice 5 and 6 have index files alone), and the three mouse 7 files without the PV suffix
Sat Nov 14 21:55:28 UTC 2026
Installed kernelspec registry-scholl-2015 in executed/scholl-2015/.venv/share/jupyter/kernels/registry-scholl-2015
0 error(s)
pass  reproduce_scholl_2015.ipynb  (346 s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/scholl-2015/reproduce_scholl_2015.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o:
            t=''.join(o['text'])
            if 'per-cell' in t or 'streamed' in t or 'GB;' in t or 'red mean' in t: print(t[:1500])
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
EOF
python tools/entry.py handover entries/scholl-2015 2>&1 | tail -3; git status --short
```

```
cellmasks (256, 455, 50) uint8 values [0, 1] pixels per mask 29 to 55
files in live/ whose names suggest per-cell data (mask, cell, roi, pv, binoc): ['docs/crcns_pvc-10_data_description.doc', 'docs/crcns_pvc-10_data_description.pdf', 'script/cellmasks.mat']

streamed 9435 frames (2.42 GB) in 210 s, 11.6 MB/s; peak memory 0.27 GB
raw trace range 97.8 to 1681.8
mean dF/F over cells and stimulus trials peaks at frame 52 after onset, 2.46%; blank trials at that frame -0.40%
mean dF/F (%) every 6 frames, stimulus trials: [-0.16, 0.04, -0.19, -0.11, 0.48, 1.41, 2.11, 1.94, 2.07, 2.17, 1.92, 1.93, 1.77, 2.13, 1.78, 1.28, 0.89, 0.44, 0.28, 0.2]
mean dF/F (%) every 6 frames, blank trials:    [-0.2, -0.58, 0.2, -0.61, -0.77, -0.11, -0.32, -0.45, -0.41, -0.2, -1.22, -0.69, -1.5, -0.69, -0.46, -0.9, -0.44, -0.57, -0.85, -1.04]

red mean in the 50 masks: 179.0 to 887.5 (median 266.3); whole-frame median 187.7
masks sorted by red intensity: [179, 192, 204, 205, 209, 215, 218, 218, 231, 233, 239, 239, 246, 247, 251, 251, 253, 256, 256, 257, 259, 260, 262, 265, 265, 267, 268, 273, 279, 279, 284, 285, 286, 288, 290, 291, 294, 295, 297, 297, 299, 300, 302, 307, 309, 310, 311, 314, 489, 887]

116 movies, 252 GB; at 11.6 MB/s, 6.0 h to stream once, against a 1 h notebook limit
notebook time so far 5.7 min

wrote executed/scholl-2015/handover
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/for w in ("mask", "cell", "roi", "pv", "binoc")/for w in ("mask", "cell", "roi", "binoc", "peak", "dsi")/; s/(mask, cell, roi, pv, binoc)/(mask, cell, roi, binoc, peak, dsi)/' $TMPDIR/make_nb.py && cd entries/scholl-2015 && python $TMPDIR/make_nb.py && cd ../.. && sed -i 's/runtime_minutes: 8/runtime_minutes: 6/' entries/scholl-2015/entry.yaml && python - <<'EOF'
p='attempts/scholl-2015-01.yaml'; s=open(p).read()
s=s.replace("streaming the 252 GB of movies once takes an estimated 6.2 h at the 11.2 MB/s\n    measured in the notebook","streaming the 252 GB of movies once takes an estimated 6 h at the rate of about\n    11 MB/s measured in the notebook")
open(p,'w').write(s)
EOF
grep -n "6 h" attempts/scholl-2015-01.yaml; date -u; python tools/entry.py all entries/scholl-2015 2>&1 | tail -3
```

```
42:    selection, and streaming the 252 GB of movies once takes an estimated 6 h at the rate of about
164:    mice 7 to 10 only (mice 5 and 6 have index files alone), and the three mouse 7 files without the PV suffix
Sat Nov 14 22:01:43 UTC 2026
Installed kernelspec registry-scholl-2015 in executed/scholl-2015/.venv/share/jupyter/kernels/registry-scholl-2015
0 error(s)
pass  reproduce_scholl_2015.ipynb  (352 s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/scholl-2015/reproduce_scholl_2015.ipynb'))
for c in nb['cells']:
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))
        if 'suggest per-cell' in t or 'to stream once' in t or 'shuffled labels' in t: print(t[:600])
        if o.get('output_type')=='error': print('ERR')
EOF
python tools/entry.py handover entries/scholl-2015 | tail -1; python tools/entry.py check entries/scholl-2015 | tail -1; ls entries/scholl-2015
```

```
cellmasks (256, 455, 50) uint8 values [0, 1] pixels per mask 29 to 55
files in live/ whose names suggest per-cell data (mask, cell, roi, binoc, peak, dsi): ['script/cellmasks.mat']

stimulus minus blank in the window (frames 45 to 59): 2.59% dF/F; with shuffled labels 95% range -1.12 to 1.15, p = 0.005
  onsets moved by -118 frames: stimulus minus blank  -0.76%
  onsets moved by  -90 frames: stimulus minus blank  -0.36%
  onsets moved by  -60 frames: stimulus minus blank   0.57%
  onsets moved by  -30 frames: stimulus minus blank   1.15%
  onsets moved by   +0 frames: stimulus minus blank   2.59%
  onsets moved by  +30 frames: stimulus minus blank   1.67%
  onsets moved by  +60 frames: stimulus minus blank  -1.42%
  onsets moved by  +90 frames: stimulus minus blank  -2.13
116 movies, 252 GB; at 11.3 MB/s, 6.2 h to stream once, against a 1 h notebook limit
notebook time so far 5.8 min

wrote executed/scholl-2015/handover
0 error(s)
README.md
__pycache__
entry.yaml
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
rm -rf entries/scholl-2015/__pycache__; date -u
```

```
Sat Nov 14 22:08:04 UTC 2026
```

**Agent**

None of the 25 claims could be tested: all are blocked as `data_missing`. The published dataset holds raw movies only, with no cells marked or labelled, and the paper's cells were identified by hand. The entry is in `entries/scholl-2015/` and the record is `attempts/scholl-2015-01.yaml`. `entry.py all` passes (the notebook runs in about 6 min) and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claims | Outcome | Reason |
|---|---|---|
| fig1e-pv-tdtomato-colocalization | blocked, data_missing | No histology in the dataset |
| cell-counts-responsive, fig3abc, fig3c, fig3 (MI), mi-per-animal, fig3def, mi-dsi-relation, pv-larger-dff-low-dsi (8 claims) | blocked, data_missing | No masks or PV+/PV- labels for the paper's hand-identified cells |
| fig4ag, fig4d, fig4f decay, fig4f length constant, fig4ef, figs6ab, figs4, fig4i, fig4k, fig4jk, figs6cd (11 claims) | blocked, data_missing | Same; no cells or positions |
| figs3, figs5 | blocked, data_missing | Neither the cells nor the hand-drawn neuropil patches are deposited |
| fig5-camkii-responsive, fig5e, fig5f | blocked, data_missing | The two CaMKIIa mice are not in the dataset |

For the claims on the paper's own cells, the notes give a second reason, `too_large`. Streaming the 252 GB of movies once takes about 6 h at the measured 11 MB/s, against the 1 h notebook limit.

## 2. Dataset

**What is in it.** The published folder `pvc-10/live/` holds:
- green and red movies for 58 planes across 6 mice;
- a stimulus table per plane and a stats file per mouse (stimulus duration and plane shifts);
- 50 unlabelled example masks for one plane (mouse 5, depth 260 µm).

**Findings recorded:**
- **Per-cell data missing.** The descriptor says the dataset contains per-cell traces, peak responses, DSI, preferred disparity and cell positions. None of these are among the published files.
- **Withdrawn files.** The bucket's `original/to_remove/` folder holds November 2014 structs that look like the paper's processed cells (masks, peaks, DSI, positions, neuropil). They cover only mice 7 to 10, and three of the mouse 7 files are truncated and cannot be opened. They are not in the file list or checksums, so I did not use them. The notebook only lists what they hold.
- **Other data the paper used is absent.** The CaMKIIa mice, the neuropil patches and the histology are not in the dataset.
- **Frame size.** The descriptor says 255 × 456 pixels; every file is 256 × 455, as the paper says.
- **Frame rate.** The dataset gives none. At the paper's 30 Hz, stimulus onset intervals fit the Methods' stimulus plus 3 s blank only in mouse 6.
- **Repeats and trials.** Eight planes have fewer than the 6 to 7 repeats the paper states (mouse 10 has 4 or 5). In four planes the last trial runs past the end of the movie. Mouse 10 has a plane at 125 µm, above the paper's "starting around 150 µm".

**Checks that passed:**
- No recording appears to be deposited twice.
- On the example plane, stimulus trials differ from blank trials after onset (2.59% dF/F, shuffle p = 0.005), and the difference shrinks when onsets are shifted. So the stimulus table is consistent with the movie's clock on that plane; the other 57 planes were not checked.

**Assumptions:** none (nothing was tested). **Questions for the paper's authors:** none recorded. **Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. It does not say what to do with unpublished files in the archive's own storage (`original/to_remove/`). I treated them as unpinnable and not published, did not use them, and recorded them as a finding.
2. It says claim-level data are `data_missing` when "not public anywhere else". These withdrawn files are publicly readable, but they cannot be pinned and are incomplete. I kept `data_missing` and said why in the notes.
3. It does not cover a dataset that holds raw movies but not the hand-made annotations (masks and cell types) that every claim depends on. I chose `data_missing` over `metadata_insufficient` because the masks are data the authors produced, not missing labels.
4. The notebook layout assumes some claims are tested. With none, I wrote a short "Claims" section explaining why and kept the "## Summary" heading so the handover strips it correctly.
5. The check tool flagged the string `"/data/"` as a local file path when it was only matching bucket keys. I rewrote the test.

## 4. Runtime and failures

- The run took about 70 minutes (20:59 to 22:08 UTC); each notebook run took about 6 minutes, and I ran it three times.
- Early on, walking every object in one movie file took about 30 minutes; I switched to reading frames by reference.
- Nothing failed in the final run.

## End of run

43 turns, 66 minutes, $3.04 at API prices, result: success.
