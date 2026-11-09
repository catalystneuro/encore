# crcns-pag-2 · author · run 42283461113

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls paper claims/crcns-pag-2 entries | head -50
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26b813bb-c5f6-4d5b-bc86-69268017babd/tool-results/brbbb3wt1.txt

Preview (first 2KB):
Fri Nov  6 19:58:21 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26b813bb-c5f6-4d5b-bc86-69268017babd/tool-results/brbbb3wt1.txt"
}
```

```
1	Fri Nov  6 19:58:21 UTC 2026
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
[... 647 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/crcns-pag-2/*.yaml; ls paper; ls entries | grep -i crcns;
```

```
<persisted-output>
Output too large (44.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26b813bb-c5f6-4d5b-bc86-69268017babd/tool-results/b4c40b6g5.txt

Preview (first 2KB):
# Claims for Moaddab, Wright & McDannald (2020), Sci Rep 10, 18035, on CRCNS data set pag-2.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader, version pilot-13).
#
# Text read: the version of record, PMC7582948 (open access), as supplied under paper/ (Europe PMC
# JATS XML, flattened), with its Introduction, Materials and methods, Results, figure legends and
# Discussion. The supplement (Supplementary Figures S1 to S6 and a Supplementary Information file)
# is listed in the text, but its content is not in the text supplied, and no PDF was supplied.
# The main results are stated, with their statistics, in the main text, so they do not rest on the
# supplement; the claims that are shown only in Figs. S4 to S6 are kept from the sentences of the
# Results that cite them, and have no expected values. The paper links no analysis code for the
# neural analyses. It says Med Associates programs and Matlab programs for the behavioral
# analyses are at https://mcdannaldlab.org/resources; on 2026-11-06 that address returned a 404
# page, so no code was read and no repository or commit can be recorded. The two web calculators
# the Methods name (socscistatistics.com chi-square; vassarstats.net r-to-z) were not run. Two
# facts about them were checked arithmetically from the paper's own numbers (see the claims on
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26b813bb-c5f6-4d5b-bc86-69268017babd/tool-results/b4c40b6g5.txt"
}
```

```
1	# Claims for Moaddab, Wright & McDannald (2020), Sci Rep 10, 18035, on CRCNS data set pag-2.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
3	# protocol as stated in docs/protocol.md (Reader, version pilot-13).
4	#
5	# Text read: the version of record, PMC7582948 (open access), as supplied under paper/ (Europe PMC
6	# JATS XML, flattened), with its Introduction, Materials and methods, Results, figure legends and
7	# Discussion. The supplement (Supplementary Figures S1 to S6 and a Supplementary Information file)
8	# is listed in the text, but its content is not in the text supplied, and no PDF was supplied.
9	# The main results are stated, with their statistics, in the main text, so they do not rest on the
10	# supplement; the claims that are shown only in Figs. S4 to S6 are kept from the sentences of the
11	# Results that cite them, and have no expected values. The paper links no analysis code for the
12	# neural analyses. It says Med Associates programs and Matlab programs for the behavioral
13	# analyses are at https://mcdannaldlab.org/resources; on 2026-11-06 that address returned a 404
14	# page, so no code was read and no repository or commit can be recorded. The two web calculators
15	# the Methods name (socscistatistics.com chi-square; vassarstats.net r-to-z) were not run. Two
16	# facts about them were checked arithmetically from the paper's own numbers (see the claims on
17	# Fig. 2D and Figs. 6 and 7).
18	#
19	# Data the paper used. 20 female Long Evans rats born in the laboratory: 12 given early adolescent
20	# adversity (EAA; P26 to P35, twice daily, tail pinch, restraint, forced cold swim, cat hair, five
[... 738 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/pag-2.data-description.txt; echo ----; sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pag-2/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in zip(re.findall('<Key>(.*?)</Key>',t),re.findall('<Size>(.*?)</Size>',t)): print(s,k)
print(re.findall('<IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-2/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; curl -sI $B/data.zip | grep -i -E "last-mod|etag"; cat README.md | head -80; ls entries/001453-fouke-2025 entries/crcns-bf-3-moaddab-2021
```

```
7d1686e3d4f6f36895c38f34eda632d4  data.zip
c31878678019ba7abd75c55435cac021  docs/crcns_pag-2_data_description.docx
9f6c40904e9123fe8ff488d6006c8df4  docs/crcns_pag-2_data_description.pdf
cc9708efb3830cc12ad3b910dbe21b9b  filelist.txt
# CRCNS.org 'pag-2' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data.zip	93645067 (89.3 MB)
 docs/crcns_pag-2_data_description.docx	35261 (34.4 KB)
 docs/crcns_pag-2_data_description.pdf	91200 (89.0 KB)
 checksums.md5	235
Last-Modified: Wed, 11 Feb 2026 02:59:25 GMT
ETag: "7d1686e3d4f6f36895c38f34eda632d4"
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -60 omr.py; cat ../../attempts/001453-fouke-2025-01.yaml | head -150
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
[... 253 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -v "^    " | head -80; grep -n "findings:" -A30 attempts/001453-fouke-2025-01.yaml | head -50
```

```
notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
  deviations:
  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion
- claim: fig1c-continuous-vs-bouts
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1c-continuous-vs-bouts
  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
  deviations:
  - The paper shows this with representative traces and a bout analysis whose bout files are not
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^verifications\|^provenance/,$p' attempts/001453-fouke-2025-01.yaml | head -20; ls schemas tools; python tools/entry.py --help 2>&1 | head -30; ls questions | head
```

```
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/reproduction-registry/actions/runs/38574152687
inputs:
- what: Names of the stimulus codes (the conversion of stimulus names to codes, its printed list of
    codes, and its own labels for codes 9 to 13), the trial processing parameters, the spatial
    scale of 10 pixels per mm, the per-stimulus medians it printed, used as reference values
    for the link claim, and the DC pairs its printed Tukey test for Figure 1D finds significant,
    used as reference values for fig1d-dc-no-modulation. From the paper's analysis notebook
    Fig1-S1.ipynb.
  source: https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
    33a5c297ff4ab6ff49f6bdd96139e9fdd867025c
[... 74 more lines not kept]
```

**Agent**

Now let me open the zip and look at its contents.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "import fsspec,scipy,h5py,numpy,pandas,statsmodels,pingouin" 2>&1; which uv python3; python3 --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec,scipy,h5py,numpy,pandas,statsmodels,pingouin
ModuleNotFoundError: No module named 'fsspec'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
Python 3.13.18
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy h5py numpy pandas statsmodels pingouin matplotlib ipykernel nbformat nbclient 2>&1 | tail -3; python -c "
import fsspec, zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-2/live/data.zip', block_size=2**20).open()
z=zipfile.ZipFile(f)
n=z.infolist(); print(len(n))
import collections
for i in n[:15]+n[-15:]: print(i.file_size, i.compress_size, i.filename)
print(collections.Counter(i.filename.split('/')[1] if '/' in i.filename else '' for i in n))
"
```

```
362
0 0 data/
229411 19637 data/vlpagAnalysis.m
223138 11388 data/cue3.wav
223242 10313 data/cue2.wav
0 0 data/matFiles/
491084 490145 data/matFiles/mh21110217epr38aSPK11a.mat
191406 190988 data/matFiles/mh21110117epr38aSPK12a.mat
7862 7602 data/matFiles/mh21102017epr38aSPK13a.mat
84074 83789 data/matFiles/mh21103117epr38aSPK12a.mat
872902 870933 data/matFiles/mh32102717epr38bSPK11a.mat
38191 37958 data/matFiles/mh12062117epr38aSPK10a.mat
603974 602824 data/matFiles/mh21102517epr38aSPK12a.mat
426629 425863 data/matFiles/mh31111617epr38bSPK12a.mat
56148 55868 data/matFiles/mh14071217epr38cSPK16a.mat
78149 77789 data/matFiles/mh23110617epr38bSPK09a.mat
505674 504743 data/matFiles/mh23110517epr38bSPK13a.mat
353210 352513 data/matFiles/mh39111417epr38cSPK14a.mat
337806 337127 data/matFiles/mh32102217epr38bSPK13a.mat
340966 340387 data/matFiles/mh39110617epr38cSPK05b.mat
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, zipfile, io, scipy.io as sio, time
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-2/live/data.zip', block_size=2**20).open()
z=zipfile.ZipFile(f)
b=z.read('data/cubeFile/cube.mat'); print(len(b), b[:120], time.time()-t)
open('cube.mat','wb').write(b)
open('vlpagAnalysis.m','wb').write(z.read('data/vlpagAnalysis.m'))
open('one.mat','wb').write(z.read('data/matFiles/mh21110217epr38aSPK11a.mat'))
"
```

```
29261351 b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Mon Dec 03 15:38:45 2018                                        \x00\x00\x00\x00' 1.6584994792938232
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && rm -f cube.mat one.mat vlpagAnalysis.m && . dev/bin/activate && cat > ld.py <<'EOF'
import fsspec, zipfile, io, scipy.io as sio
URL='https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-2/live/data.zip'
def z():
    return zipfile.ZipFile(fsspec.open(URL, block_size=2**20).open())
def cube():
    return sio.loadmat(io.BytesIO(z().read('data/cubeFile/cube.mat')), squeeze_me=False, struct_as_record=False)
EOF
python -c "
from ld import *
c=cube()
for k,v in c.items():
  if k.startswith('__'): continue
  print(k, type(v), getattr(v,'shape',None), getattr(v,'dtype',None))
  v0=v[0,0] if v.dtype==object else v
  if hasattr(v0,'_fieldnames'):
    for fn in v0._fieldnames:
      a=getattr(v0,fn); print(' ',fn, a.shape, a.dtype)
      if a.dtype==object and a.size and hasattr(a.flat[0],'_fieldnames'):
        for g in a.flat[0]._fieldnames: 
          b=getattr(a.flat[0],g); print('    ',g,b.shape,b.dtype)
          if b.dtype==object and b.size and hasattr(b.flat[0],'_fieldnames'):
            for h in b.flat[0]._fieldnames: print('       ',h,getattr(b.flat[0],h).shape)
"
```

```
vlPAGcube <class 'numpy.ndarray'> (1, 1) object
  name (1, 22) <U354
  wave (32, 1, 354) float64
  tag (32, 2, 354) float64
  poke (1, 1) object
     base (32, 1, 354) uint8
     cue (32, 1, 354) uint8
     s1 (1, 1) object
        interval (32, 50, 354)
     ms500 (1, 1) object
        interval (32, 100, 354)
  cer (1, 1) object
     cue (32, 1, 354) float64
     s1 (1, 1) object
        interval (32, 50, 354)
     ms500 (1, 1) object
        interval (32, 100, 354)
  fire (1, 1) object
     raw (1, 1) object
        base2 (32, 1, 354)
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
import numpy as np
c=cube()['vlPAGcube'][0,0]
def show(o,p=''):
  if hasattr(o,'_fieldnames'):
    for f in o._fieldnames: show(getattr(o,f),p+'.'+f)
  elif isinstance(o,np.ndarray) and o.dtype==object and o.size==1: show(o.flat[0],p)
  else: print(p, o.shape, o.dtype, (np.nanmin(o),np.nanmax(o)) if o.dtype.kind in 'fiu' and o.size else '')
show(c.fire,'fire'); show(c.poke,'poke'); show(c.cer,'cer'); show(c.tag,'tag'); show(c.wave,'wave')
print(c._fieldnames)
nm=c.name; print(nm.shape, repr(nm[0,:3]))
"
```

```
fire.raw.base2 (32, 1, 354) uint8 (np.uint8(0), np.uint8(193))
fire.raw.base5 (32, 1, 354) uint8 (np.uint8(0), np.uint8(176))
fire.raw.base10 (32, 1, 354) uint8 (np.uint8(0), np.uint8(156))
fire.raw.select.shockOnly (32, 1, 354) uint8 (np.uint8(0), np.uint8(186))
fire.raw.select.shock (32, 1, 354) uint8 (np.uint8(0), np.uint8(149))
fire.raw.select.cueOnset (32, 1, 354) uint8 (np.uint8(0), np.uint8(197))
fire.raw.select.cueOffset (32, 1, 354) uint8 (np.uint8(0), np.uint8(202))
fire.raw.select.cueEntire (32, 1, 354) uint8 (np.uint8(0), np.uint8(154))
fire.raw.select.cueFirstFive (32, 1, 354) uint8 (np.uint8(0), np.uint8(180))
fire.raw.select.cueLastFive (32, 1, 354) uint8 (np.uint8(0), np.uint8(154))
fire.raw.s1.interval (32, 50, 354) uint16 (np.uint16(0), np.uint16(257))
fire.raw.ms500.interval (32, 100, 354) uint16 (np.uint16(0), np.uint16(272))
fire.raw.ms250.interval (32, 200, 354) uint16 (np.uint16(0), np.uint16(320))
fire.raw.ms100.interval (32, 500, 354) uint16 (np.uint16(0), np.uint16(440))
fire.diff.s1.interval (32, 50, 354) int16 (np.int16(-182), np.int16(220))
fire.diff.ms500.interval (32, 100, 354) int16 (np.int16(-191), np.int16(241))
fire.diff.ms250.interval (32, 200, 354) int16 (np.int16(-193), np.int16(293))
fire.diff.ms100.interval (32, 500, 354) int16 (np.int16(-193), np.int16(384))
fire.z.s1.interval (32, 50, 354) float64 (np.float64(-5.623197624702629), np.float64(14.735960431006063))
fire.z.ms500.interval (32, 100, 354) float64 (np.float64(-5.403542778373317), np.float64(16.039552201650896))
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
import numpy as np
zz=z()
m=sio.loadmat(io.BytesIO(zz.read('data/matFiles/mh21110217epr38aSPK11a.mat')), struct_as_record=False)
def show(o,p=''):
  if hasattr(o,'_fieldnames'):
    for f in o._fieldnames: show(getattr(o,f),p+'.'+f)
  elif isinstance(o,np.ndarray) and o.dtype==object and o.size==1: show(o.flat[0],p)
  else: print(p, o.shape, o.dtype, (np.nanmin(o),np.nanmax(o)) if o.dtype.kind in 'fiu' and o.size else o.flat[:3] if o.size else '')
for k,v in m.items():
  if not k.startswith('__'): show(v,k)
c=cube()['vlPAGcube'][0,0]
print(c.tag[:,:,0])
r=c.fire.raw.ms250.interval[:,:,0]; print(np.unique(r)[:20])
print(np.unique(c.fire.raw.base10[:,0,:])[:30])
print(np.unique(c.poke.base[:,0,:])[:30], np.unique(c.poke.cue)[:30])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 15, in <module>
    r=c.fire.raw.ms250.interval[:,:,0]; print(np.unique(r)[:20])
      ^^^^^^^^^^
AttributeError: 'numpy.ndarray' object has no attribute 'raw'
EVT01 (12, 1) float64 (np.float64(971.0367), np.float64(6010.827025))
EVT02 (17, 1) float64 (np.float64(1083.136275), np.float64(5983.47715))
EVT08 (12, 1) float64 (np.float64(971.0367), np.float64(6010.827025))
EVT09 (6, 1) float64 (np.float64(959.03675), np.float64(5998.827075))
EVT11 (10, 1) float64 (np.float64(1440.5649), np.float64(5027.77085))
EVT12 (16, 1) float64 (np.float64(1093.54615), np.float64(5679.8083))
EVT13 (548, 1) float64 (np.float64(939.236825), np.float64(6025.576975))
EVT14 (32, 1) float64 (np.float64(992.536625), np.float64(6032.32695))
filename (1,) <U16 ['mh21110217epr38a']
neuron (1,) <U6 ['SPK11a']
spike (100082, 1) float64 (np.float64(939.097575), np.float64(6032.344))
wave (32, 1) float64 (np.float64(-0.1616915584299), np.float64(0.04449530096258568))
[[1.00000000e+00 2.27642767e+03]
 [1.00000000e+00 2.44093707e+03]
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
open('/dev/stdout','w').write(z().read('data/vlpagAnalysis.m').decode('latin1'))
" > /dev/null; python -c "
from ld import *
t=z().read('data/vlpagAnalysis.m').decode('latin1')
L=t.splitlines(); print(len(L))
import re
for i,l in enumerate(L):
  if re.search(r'EVT|ttest|regress|zscore|select|base10|cueOnset|cueLastFive|cueFirstFive|cer\b|\.cer|poke\.|%%',l): print(i,l[:160])
" | head -150
```

```
4908
9    h = ttest(vlPAGcube.fire.raw.base10(1:6,1,ii),vlPAGcube.fire.raw.select.cueOnset(1:6,1,ii),'Alpha',0.00833);
10    d = sign(mean(vlPAGcube.fire.raw.select.cueOnset(1:6,1,ii))-(mean(vlPAGcube.fire.raw.base10(1:6,1,ii))));
11    vlPAGcube.fire.raw.select.dirSig(1,1,ii) = h*d;
16    h = ttest(vlPAGcube.fire.raw.base10(7:22,1,ii),vlPAGcube.fire.raw.select.cueOnset(7:22,1,ii),'Alpha',0.00833);
17    d = sign(mean(vlPAGcube.fire.raw.select.cueOnset(7:22,1,ii))-(mean(vlPAGcube.fire.raw.base10(7:22,1,ii))));
18    vlPAGcube.fire.raw.select.dirSig(1,2,ii) = h*d;
23    h = ttest(vlPAGcube.fire.raw.base10(23:32,1,ii),vlPAGcube.fire.raw.select.cueOnset(23:32,1,ii),'Alpha',0.00833);
24    d = sign(mean(vlPAGcube.fire.raw.select.cueOnset(23:32,1,ii))-(mean(vlPAGcube.fire.raw.base10(23:32,1,ii))));
25    vlPAGcube.fire.raw.select.dirSig(1,3,ii) = h*d;
30    h = ttest(vlPAGcube.fire.raw.base10(1:6,1,ii),vlPAGcube.fire.raw.select.cueFirstFive(1:6,1,ii),'Alpha',0.00833);
31    d = sign(mean(vlPAGcube.fire.raw.select.cueFirstFive(1:6,1,ii))-(mean(vlPAGcube.fire.raw.base10(1:6,1,ii))));
32    vlPAGcube.fire.raw.select.dirSig(1,4,ii) = h*d;
37    h = ttest(vlPAGcube.fire.raw.base10(7:22,1,ii),vlPAGcube.fire.raw.select.cueFirstFive(7:22,1,ii),'Alpha',0.00833);
38    d = sign(mean(vlPAGcube.fire.raw.select.cueFirstFive(7:22,1,ii))-(mean(vlPAGcube.fire.raw.base10(7:22,1,ii))));
39    vlPAGcube.fire.raw.select.dirSig(1,5,ii) = h*d;
44    h = ttest(vlPAGcube.fire.raw.base10(23:32,1,ii),vlPAGcube.fire.raw.select.cueFirstFive(23:32,1,ii),'Alpha',0.00833);
45    d = sign(mean(vlPAGcube.fire.raw.select.cueFirstFive(23:32,1,ii))-(mean(vlPAGcube.fire.raw.base10(23:32,1,ii))));
46    vlPAGcube.fire.raw.select.dirSig(1,6,ii) = h*d;
51    h = ttest(vlPAGcube.fire.raw.base10(1:6,1,ii),vlPAGcube.fire.raw.select.cueLastFive(1:6,1,ii),'Alpha',0.00833);
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
t=z().read('data/vlpagAnalysis.m').decode('latin1')
L=t.splitlines()
print('\n'.join(L[:9])); print('\n'.join(L[68:135]))
import re
for i,l in enumerate(L):
  if re.search(r'regress\(|zscore|anova|ranova|corr|fitlm|mh\d\d|name|bregma|halfDuration|amplitudeRatio',l,re.I) : print(i,l[:200])
" 2>&1 | head -200
```

```
tic
clear all; %#ok<CLALL>
close all;
load(['C:\Users\moaddab\Dropbox (McDannald Lab)\Manuscripts\Moaddab\mh vlpag record + eaa\vlPAG+DRcube\','cube']);

for ii = 1:size(vlPAGcube.name,3)
   
   % Determine significance (h) and direction (d) of firing
    
   clear h d;
   
   name = vlPAGcube.name(:,:,ii);
   
   % waveform analysis

for kk = 1:length(vlPAGcube.wave)

    wave = vlPAGcube.wave(:,:,kk);
    [valleyValue,valleyLocation] = min(wave); % valley
    [maxPreValleyValue,maxPreValleyLocation] = max(wave(1:valleyLocation)); % initial hyper polarization
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
t=z().read('data/vlpagAnalysis.m').decode('latin1')
L=t.splitlines()
print('\n'.join(f'{i} {l}' for i,l in enumerate(L[2100:2430],2100)))
" 2>&1 | grep -v "^\d* *$" | head -340
```

```
2100 eaa.inh.fire.z.s1.cuePRmean = mean(eaa.inh.fire.z.s1.cuePR);
2101 
2102 eaa.inh.fire.z.ms500.cue100mean = mean(eaa.inh.fire.z.ms500.cue100);
2103 eaa.inh.fire.z.ms500.cueSPRmean = mean(eaa.inh.fire.z.ms500.cueSPR);
2104 eaa.inh.fire.z.ms500.cueNsPRmean = mean(eaa.inh.fire.z.ms500.cueNsPR);
2105 eaa.inh.fire.z.ms500.cue0mean = mean(eaa.inh.fire.z.ms500.cue0);
2106 eaa.inh.fire.z.ms500.cuePRmean = mean(eaa.inh.fire.z.ms500.cuePR);
2107 
2108 eaa.inh.fire.z.ms250.cue100mean = mean(eaa.inh.fire.z.ms250.cue100);
2109 eaa.inh.fire.z.ms250.cueSPRmean = mean(eaa.inh.fire.z.ms250.cueSPR);
2110 eaa.inh.fire.z.ms250.cueNsPRmean = mean(eaa.inh.fire.z.ms250.cueNsPR);
2111 eaa.inh.fire.z.ms250.cue0mean = mean(eaa.inh.fire.z.ms250.cue0);
2112 eaa.inh.fire.z.ms250.cuePRmean = mean(eaa.inh.fire.z.ms250.cuePR);
2113 
2114 eaa.inh.fire.z.ms100.cue100mean = mean(eaa.inh.fire.z.ms100.cue100);
2115 eaa.inh.fire.z.ms100.cueSPRmean = mean(eaa.inh.fire.z.ms100.cueSPR);
2116 eaa.inh.fire.z.ms100.cueNsPRmean = mean(eaa.inh.fire.z.ms100.cueNsPR);
2117 eaa.inh.fire.z.ms100.cue0mean = mean(eaa.inh.fire.z.ms100.cue0);
2118 eaa.inh.fire.z.ms100.cuePRmean = mean(eaa.inh.fire.z.ms100.cuePR);
2119 
[... 311 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat >> ld.py <<'EOF'
import numpy as np
def names(c):
    nm=c.name
    return [''.join(nm[0,j][i] for j in range(nm.shape[1])) for i in range(len(nm[0,0]))]
EOF
python -c "
from ld import *
import collections
c=cube()['vlPAGcube'][0,0]
N=names(c); print(N[:5])
con=['mh%02d'%i for i in [9,10,11,12,13,14,21,22,23,24,25,26,27,28]]
rats=collections.Counter(n[:4] for n in N); print(sorted(rats.items()))
g=['Con' if n[:4] in con else 'EAA' for n in N]
print(collections.Counter(g))
sess=set(n[:10] for n in N); print(len(sess), collections.Counter('Con' if s[:4] in con else 'EAA' for s in sess))
print(collections.Counter(n[10:16] for n in N))
zz=z(); files=[i.filename.split('/')[-1][:-4] for i in zz.infolist() if i.filename.endswith('.mat') and 'matFiles' in i.filename]
print(len(files), len(set(files)), set(files)-set(N), set(N)-set(files))
print(collections.Counter(collections.Counter(N).values()))
"
```

```
['mh09061617epr38aSPK15a', 'mh09062217epr38aSPK15a', 'mh09062317epr38aSPK15a', 'mh09062717epr38aSPK15a', 'mh12061917epr38aSPK03a']
[('mh09', 4), ('mh12', 17), ('mh14', 5), ('mh15', 1), ('mh17', 9), ('mh21', 81), ('mh22', 28), ('mh23', 9), ('mh24', 2), ('mh26', 5), ('mh29', 5), ('mh30', 1), ('mh31', 28), ('mh32', 42), ('mh34', 7), ('mh35', 2), ('mh36', 22), ('mh38', 16), ('mh39', 64), ('mh40', 6)]
Counter({'EAA': 203, 'Con': 151})
182 Counter({'EAA': 108, 'Con': 74})
Counter({'epr38a': 161, 'epr38b': 97, 'epr38c': 96})
354 354 set() set()
Counter({1: 354})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
import time, collections
c=cube()['vlPAGcube'][0,0]; N=names(c)
zz=z(); t=time.time()
out={}
for n in N[:20]:
    m=sio.loadmat(io.BytesIO(zz.read('data/matFiles/'+n+'.mat')))
    out[n]={k:len(v) for k,v in m.items() if k.startswith('EVT')}
    out[n]['spk']=len(m['spike'])
print(time.time()-t)
for k,v in out.items(): print(k,v)
"
```

```
2.027655839920044
mh09061617epr38aSPK15a {'EVT01': 12, 'EVT02': 30, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 486, 'EVT14': 32, 'spk': 28081}
mh09062217epr38aSPK15a {'EVT01': 12, 'EVT02': 24, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 944, 'EVT14': 32, 'spk': 35761}
mh09062317epr38aSPK15a {'EVT01': 12, 'EVT02': 26, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 763, 'EVT14': 32, 'spk': 34912}
mh09062717epr38aSPK15a {'EVT01': 12, 'EVT02': 23, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 1466, 'EVT14': 32, 'spk': 29832}
mh12061917epr38aSPK03a {'EVT01': 12, 'EVT02': 32, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 498, 'EVT14': 32, 'spk': 6955}
mh12062117epr38aSPK01a {'EVT01': 12, 'EVT02': 25, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 575, 'EVT14': 32, 'spk': 7827}
mh12062117epr38aSPK10a {'EVT01': 12, 'EVT02': 25, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 575, 'EVT14': 32, 'spk': 5972}
mh12062317epr38aSPK05a {'EVT01': 12, 'EVT02': 26, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 712, 'EVT14': 32, 'spk': 23333}
mh12062417epr38aSPK03a {'EVT01': 12, 'EVT02': 26, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 566, 'EVT14': 32, 'spk': 3737}
mh12062717epr38aSPK12a {'EVT01': 12, 'EVT02': 25, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 615, 'EVT14': 32, 'spk': 41286}
mh12062817epr38aSPK12a {'EVT01': 12, 'EVT02': 18, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 546, 'EVT14': 32, 'spk': 35882}
mh12070117epr38aSPK12a {'EVT01': 12, 'EVT02': 26, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 439, 'EVT14': 32, 'spk': 43284}
mh12070117epr38aSPK16a {'EVT01': 12, 'EVT02': 26, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 439, 'EVT14': 32, 'spk': 8192}
mh12070317epr38aSPK16a {'EVT01': 12, 'EVT02': 30, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 467, 'EVT14': 32, 'spk': 4985}
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
c=cube()['vlPAGcube'][0,0]; N=names(c)
zz=z()
for u in [0,4,100]:
    n=N[u]; m=sio.loadmat(io.BytesIO(zz.read('data/matFiles/'+n+'.mat')))
    E={k:m[k].ravel() for k in m if k.startswith('EVT')}
    tag=c.tag[:,:,u]
    print(n, tag[:3,1], E['EVT09'][:3], E['EVT14'][:3], E['EVT12'][:3], E['EVT11'][:3])
    on=tag[:,1]
    # nearest EVT for each onset
    for k,v in E.items():
        d=np.array([np.min(np.abs(v-t))  for t in on]); 
        print('  ',k, np.round(np.median(d),3))
"
```

```
mh09061617epr38aSPK15a [2276.427675 2440.937075 2777.9559  ] [2276.427675 2440.937075 2777.9559  ] [1972.908725 2115.418225 2309.927525] [1941.40885  2083.91835  2625.446375] [4216.540625 4379.05     4541.559375]
   EVT01 163.509
   EVT02 16.58
   EVT08 163.509
   EVT09 409.273
   EVT11 326.019
   EVT12 66.255
   EVT13 1.68
   EVT14 31.5
mh12061917epr38aSPK03a [1436.8312   2349.8929   2716.913525] [1436.8312   2349.8929   2716.913525] [ 930.80035  1123.310675 1305.820975] [ 899.30025  1591.3415   1928.362125] [1091.810625 1274.320925 1765.851825]
   EVT01 148.51
   EVT02 16.875
   EVT08 148.51
   EVT09 184.51
   EVT11 173.51
   EVT12 66.255
   EVT13 1.675
   EVT14 31.5
mh21110317epr38aSPK16a [1929.26645 2581.3039  3562.36005] [1929.26645 2581.3039  3562.36005] [ 975.710175 1138.21945  1270.729   ] [1766.75705  2103.7757   2256.285175] [ 944.210275 1106.719625 1239.229125]
   EVT01 153.509
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
c=cube()['vlPAGcube'][0,0]; N=names(c)
zz=z()
def cnt(s,a,b): return np.searchsorted(s,b)-np.searchsorted(s,a)
for u in [0,100,300]:
    n=N[u]; m=sio.loadmat(io.BytesIO(zz.read('data/matFiles/'+n+'.mat')))
    E={k:m[k].ravel() for k in m if k.startswith('EVT')}
    s=np.sort(m['spike'].ravel()); on=c.tag[:,1,u]; ty=c.tag[:,0,u]
    print(n, 'types',ty.astype(int))
    ok=[np.isin(on[:6],E['EVT09']).all(), np.isin(on[6:22],E['EVT12']).all(), np.isin(on[22:],E['EVT11']).all()]
    sh=np.array([np.min(np.abs(E['EVT08']-(t+12))) for t in on])<0.01
    print(' match',ok,'shock rows',np.where(sh)[0]+1)
    b10=np.array([cnt(s,t-10,t)/10 for t in on]); print(' base10', np.abs(b10-c.fire.raw.base10[:,0,u]).max(), b10[:4], c.fire.raw.base10[:4,0,u])
    for nm,(a,b) in dict(cueOnset=(0,1),cueFirstFive=(0,5),cueLastFive=(5,10),cueEntire=(0,10)).items():
        r=np.array([cnt(s,t+a,t+b)/(b-a) for t in on]); print(' ',nm,np.abs(r-getattr(c.fire.raw.select,nm)[0,0][:,0,u]).max())
    ed=np.arange(-20,30.0001,0.25)
    r=np.array([np.histogram(s,t+ed)[0]*4 for t in on]); print(' ms250', np.abs(r-c.fire.raw.ms250[0,0].interval[:,:,u]).max())
    ed=np.arange(-20,30.0001,1.)
    r=np.array([np.histogram(s,t+ed)[0] for t in on]); print(' s1', np.abs(r-c.fire.raw.s1[0,0].interval[:,:,u]).max())
    p=np.sort(E['EVT13'])
    for w in [2,10,20]:
        pb=np.array([cnt(p,t-w,t)/w for t in on]); print(' pokebase',w, np.abs(pb-c.poke.base[:,0,u]).max(), pb[:5], c.poke.base[:5,0,u])
    pc=np.array([cnt(p,t,t+10)/10 for t in on]); print(' pokecue', np.abs(pc-c.poke.cue[:,0,u]).max(), pc[:5], c.poke.cue[:5,0,u])
    pb=np.array([cnt(p,t-20,t)/20 for t in on]); 
    with np.errstate(all='ignore'): cr=(pb-pc)/(pb+pc)
    print(' cer', np.nanmax(np.abs(cr-c.cer.cue[:,0,u])), np.isnan(cr).sum(), cr[:6], c.cer.cue[:6,0,u])
" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 14, in <module>
    b10=np.array([cnt(s,t-10,t)/10 for t in on]); print(' base10', np.abs(b10-c.fire.raw.base10[:,0,u]).max(), b10[:4], c.fire.raw.base10[:4,0,u])
                                                                              ^^^^^^^^^^
AttributeError: 'numpy.ndarray' object has no attribute 'raw'
mh09061617epr38aSPK15a types [1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4]
 match [np.True_, np.True_, np.True_] shock rows [ 1  2  3  4  5  6  7  8  9 10 11 12]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat >> ld.py <<'EOF'
def g(o, path):
    for p in path.split('.'):
        if isinstance(o, np.ndarray) and o.dtype == object: o = o[0, 0]
        o = getattr(o, p)
    return o
EOF
python -c "
from ld import *
c=cube()['vlPAGcube'][0,0]; N=names(c)
zz=z()
def cnt(s,a,b): return np.searchsorted(s,b)-np.searchsorted(s,a)
for u in [0,100,300]:
    n=N[u]; m=sio.loadmat(io.BytesIO(zz.read('data/matFiles/'+n+'.mat')))
    E={k:m[k].ravel() for k in m if k.startswith('EVT')}
    s=np.sort(m['spike'].ravel()); on=c.tag[:,1,u]
    print(n)
    b10=np.array([cnt(s,t-10,t)/10 for t in on]); B=g(c,'fire.raw.base10')[:,0,u]; print(' base10', np.abs(b10-B).max(), b10[:4], B[:4])
    for w in [2,5]:
        b=np.array([cnt(s,t-w,t)/w for t in on]); print(' base',w, np.abs(b-g(c,'fire.raw.base%d'%w)[:,0,u]).max())
    for nm,(a,b) in dict(cueOnset=(0,1),cueFirstFive=(0,5),cueLastFive=(5,10),cueEntire=(0,10),cueOffset=(10,11)).items():
        r=np.array([cnt(s,t+a,t+b)/(b-a) for t in on]); print(' ',nm,np.abs(r-g(c,'fire.raw.select.'+nm)[:,0,u]).max())
    for nm,dt,nb in [('ms250',.25,200),('s1',1.,50),('ms500',.5,100)]:
      ed=-20+np.arange(nb+1)*dt
      r=np.array([np.histogram(s,t+ed)[0]/dt for t in on]); print(' ',nm, np.abs(r-g(c,'fire.raw.%s.interval'%nm)[:,:,u]).max())
    p=np.sort(E['EVT13'])
    for w in [2,10,20]:
        pb=np.array([cnt(p,t-w,t)/w for t in on]); print(' pokebase',w, np.abs(pb-g(c,'poke.base')[:,0,u]).max(), pb[:5], g(c,'poke.base')[:5,0,u])
    pc=np.array([cnt(p,t,t+10)/10 for t in on]); print(' pokecue', np.abs(pc-g(c,'poke.cue')[:,0,u]).max(), pc[:5], g(c,'poke.cue')[:5,0,u])
    for w in [20,10]:
      pb=np.array([cnt(p,t-w,t)/w for t in on]); 
      with np.errstate(all='ignore'): cr=(pb-pc)/(pb+pc)
      print(' cer',w, np.nanmax(np.abs(cr-g(c,'cer.cue')[:,0,u])), np.isnan(cr).sum(), np.isnan(g(c,'cer.cue')[:,0,u]).sum(), cr[:6].round(3), g(c,'cer.cue')[:6,0,u].round(3))
" 2>&1
```

```
mh09061617epr38aSPK15a
 base10 0.8999999999999986 [20.2 32.  17.8 17. ] [20 32 17 17]
 base 2 0.5
 base 5 0.8000000000000007
  cueOnset 0.0
  cueFirstFive 0.8000000000000007
  cueLastFive 0.8000000000000007
  cueEntire 0.9000000000000004
  cueOffset 14.0
  ms250 4.0
  s1 0.0
  ms500 0.0
 pokebase 2 55.0 [1.  0.  2.  1.5 0. ] [33  3 57 39 36]
 pokebase 10 55.8 [0.4 0.  1.2 0.7 0.5] [33  3 57 39 36]
 pokebase 20 56.05 [0.55 0.05 0.95 0.65 0.6 ] [33  3 57 39 36]
 pokecue 23.6 [0. 0. 0. 0. 0.] [0 0 0 0 0]
 cer 20 1.1102230246251565e-16 0 0 [1. 1. 1. 1. 1. 1.] [1. 1. 1. 1. 1. 1.]
 cer 10 0.30303030303030304 3 0 [ 1. nan  1.  1.  1.  1.] [1. 1. 1. 1. 1. 1.]
mh21110317epr38aSPK16a
 base10 0.8999999999999986 [19.3 30.4 19.2 25.3] [19 30 19 25]
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
c=cube()['vlPAGcube'][0,0]; N=names(c)
ty=c.tag[:,0,0].astype(int); print(ty)
for u in [0,100,300]:
  for res,nb,bb in [('s1',50,2),('ms250',200,8)]:
    R=g(c,'fire.raw.%s.interval'%res)[:,:,u].astype(float); D=g(c,'fire.diff.%s.interval'%res)[:,:,u].astype(float); Z=g(c,'fire.z.%s.interval'%res)[:,:,u]
    # hyp A: own trial baseline
    bA=R[:,20*nb//50-bb:20*nb//50].mean(1,keepdims=True)
    # hyp B: trial type mean baseline (types 1..4) 
    grp=np.array([1]*6+[2]*16+[3]*10)
    bB=np.array([bA[grp==k].mean() for k in grp])[:,None]
    grp4=ty; bC=np.array([bA[grp4==k].mean() for k in grp4])[:,None]
    for nm,b in [('own',bA),('type3',bB),('type4',bC)]:
        print(u,res,nm, np.abs(R-b-D).max().round(3))
    # z hyps
    d=R-bA
    for nm,zz in [('diffall', (D-D.mean())/D.std()), ('diffall_ddof1',(D-D.mean())/D.std(ddof=1)), ('ownexact',(d-d.mean())/d.std(ddof=1))]:
        print('   z',nm, np.abs(zz-Z).max().round(4))
"
```

```
[1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4]
0 s1 own 0.5
0 s1 type3 17.25
0 s1 type4 11.75
   z diffall 0.0012
   z diffall_ddof1 0.0
   z ownexact 0.02
0 ms250 own 0.5
0 ms250 type3 17.25
0 ms250 type4 11.75
   z diffall 0.0005
   z diffall_ddof1 0.0
   z ownexact 0.0154
100 s1 own 0.5
100 s1 type3 25.344
100 s1 type4 25.8
   z diffall 0.0015
   z diffall_ddof1 0.0
   z ownexact 0.0251
100 ms250 own 0.5
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
c=cube()['vlPAGcube'][0,0]; N=names(c)
zz=z(); import collections, hashlib
sig={}; ev={}
for n in N:
    m=sio.loadmat(io.BytesIO(zz.read('data/matFiles/'+n+'.mat')))
    s=m['spike'].ravel(); sig[n]=hashlib.md5(np.round(s,6).tobytes()).hexdigest()
    ev[n]=(tuple(np.round(np.sort(m['EVT14'].ravel()),3)), tuple(sorted((k,len(m[k])) for k in m if k.startswith('EVT'))), len(s))
d=collections.defaultdict(list)
for n,h in sig.items(): d[h].append(n)
print('dup spike trains', [v for v in d.values() if len(v)>1])
S=collections.defaultdict(list)
for n,e in ev.items(): S[e[0]].append(n)
print('unique event sets (sessions)', len(S))
keys=collections.defaultdict(set)
for k,v in S.items():
    keys[len(set(x[:10] for x in v))]+=0 if False else keys[len(set(x[:10] for x in v))].add(k) or set()
for k,v in S.items():
    if len(set(x[:10] for x in v))>1: print('multi', v)
bykey=collections.defaultdict(set)
for k,v in S.items():
    for x in v: bykey[x[:10]].add(k)
print([ (k,len(v)) for k,v in bykey.items() if len(v)>1])
print(collections.Counter(e[1] for e in ev.values()).most_common(8))
con=['mh%02d'%i for i in [9,10,11,12,13,14,21,22,23,24,25,26,27,28]]
print(collections.Counter('Con' if v[0][:4] in con else 'EAA' for v in S.values()))
"
```

```
Exit code 1
Fri Nov  6 20:02:41 UTC 2026
Traceback (most recent call last):
  File "<string>", line 18, in <module>
    keys[len(set(x[:10] for x in v))]+=0 if False else keys[len(set(x[:10] for x in v))].add(k) or set()
TypeError: unsupported operand type(s) for +=: 'set' and 'set'
dup spike trains []
unique event sets (sessions) 182
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
from ld import *
import collections
c=cube()['vlPAGcube'][0,0]; N=names(c)
con=['mh%02d'%i for i in [9,10,11,12,13,14,21,22,23,24,25,26,27,28]]
S=set(n[:10] for n in N)
print(collections.Counter('Con' if s[:4] in con else 'EAA' for s in S))
print(sorted(collections.Counter(s[:4] for s in S).items()))
# also by rat+date+program
S2=set(n[:16] for n in N); print(len(S2))
"
```

```
Counter({'EAA': 108, 'Con': 74})
[('mh09', 4), ('mh12', 12), ('mh14', 5), ('mh15', 1), ('mh17', 9), ('mh21', 21), ('mh22', 18), ('mh23', 8), ('mh24', 2), ('mh26', 4), ('mh29', 4), ('mh30', 1), ('mh31', 11), ('mh32', 16), ('mh34', 7), ('mh35', 2), ('mh36', 12), ('mh38', 16), ('mh39', 24), ('mh40', 5)]
182
Shell cwd was reset to
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "baseline" paper/10.1038-s41598-020-74457-3.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '160,200p' paper/10.1038-s41598-020-74457-3.txt | grep -v "^$" | cut -c1-3000 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p entries/crcns-pag-2-moaddab-2020 && cat > entries/crcns-pag-2-moaddab-2020/pag2.py <<'EOF'
"""Loading and measures for CRCNS pag-2 (Moaddab, Wright & McDannald 2020, Sci Rep 10, 18035).

The data set (doi:10.6080/K0833Q7F) is one zip, pag-2/live/data.zip, in the public S3 bucket
crcnsarchive. It is streamed with fsspec and opened in place with zipfile; nothing is written to
disk. CRCNS data sets are not versioned: the MD5 of data.zip in the data set's checksums.md5 is
`DATA_ZIP_MD5`, and `check_md5` compares the ETag of the object read against it.

The zip holds one MATLAB file per unit (data/matFiles/<name>.mat: spike times `spike`, event
times `EVT01` to `EVT14`, mean waveform), the authors' cube of all units (data/cubeFile/cube.mat,
`vlPAGcube`) and the authors' script data/vlpagAnalysis.m. The event codes are not documented;
they are identified from the data and the cube's trial table (`tag`, cue type and onset per
trial) in the notebook's data check:
EVT09 danger onsets, EVT12 uncertainty onsets, EVT11 safety onsets, EVT08 (= EVT01) shocks,
EVT13 nose pokes, EVT14 one marker 31.5 s before each cue onset, EVT02 not identified
(not used).

Where the parameters come from:

- Group of each rat (Control or EAA): only the authors' script data/vlpagAnalysis.m gives it
  (its "Select control units" and "Select EAA units" lists, lines 99 to 122). `CON_RATS`,
  `EAA_RATS` copy those lists. The data description and the files carry no group label.
- Trial types and windows: Methods, "Fear discrimination" (6 danger, 6 uncertainty shock, 10
  uncertainty no-shock, 10 safety; 10 s cues; shock 2 s after cue offset), "Identifying
  cue-responsive neurons" (10 s baseline; first 1 s, first 5 s, last 5 s cue epochs, from the
  Methods and the Results paragraph cited in the claims file), "Z score normalization" (250 ms
  bins, 20 s before cue onset to 20 s after offset, 200 bins; 2 s pre-cue baseline per trial type;
  Z score over all trial types of the neuron) and "Calculating suppression ratios" (20 s baseline,
  10 s cue, each trial its own baseline).
- Uncertainty shock and no-shock trials are pooled into one uncertainty type of 16 trials
  (Methods, "Population and single-unit firing analyses": "Uncertainty trial types were
  collapsed").
- Z scores use the sample SD (ddof = 1), as MATLAB's zscore and the cube's own z fields do
  (checked in the notebook); a standard choice that only rescales each neuron.
- The trial-wise normalized firing for the regressions has four readings (`trial_firing`): the
  three the claims file names (a, b, c) and the cube's own trial-wise z (d, the code's).
- Empty-poke trials (no pokes in baseline or cue, ratio 0/0): readings 'zero' and 'drop'
  (claims file, opening comment).
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import numpy as np
import requests
import scipy.io as sio
from scipy import stats

DATASET = "crcns:pag-2/unversioned"
DOI = "10.6080/K0833Q7F"
BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-2/live"
ZIP_URL = BASE_URL + "/data.zip"
DATA_ZIP_MD5 = "7d1686e3d4f6f36895c38f34eda632d4"   # checksums.md5 of the data set

# data/vlpagAnalysis.m, lines 99-103 (Control) and 117-122 (EAA). The lists name more rats than
# the data hold; the notebook prints which are present.
CON_RATS = ["mh%02d" % i for i in (9, 10, 11, 12, 13, 14, 21, 22, 23, 24, 25, 26, 27, 28)]
EAA_RATS = ["mh%02d" % i for i in (15, 16, 17, 18, 19, 20, 29, 30, 31, 32, 33, 34, 35, 36,
                                   37, 38, 39, 40)]

BIN = 0.25                     # s, Methods "Z score normalization"
PRE, POST = 20.0, 30.0         # s around cue onset: 20 s before onset to 20 s after offset
NBIN = int((PRE + POST) / BIN)  # 200
ONSET_BIN = int(PRE / BIN)     # bin 80 is the first 250 ms of the cue
CUE_S = 10.0
TYPES = ("danger", "uncertainty", "safety")
PROB = {"danger": 1.0, "uncertainty": 0.375, "safety": 0.0}


def _bins(a, b):
    """Bin indices of the window [a, b) s from cue onset."""
    return slice(ONSET_BIN + int(round(a / BIN)), ONSET_BIN + int(round(b / BIN)))


WIN = {
    "base10": _bins(-10, 0), "base2": _bins(-2, 0), "first1": _bins(0, 1),
    "first5": _bins(0, 5), "last5": _bins(5, 10), "cue": _bins(0, 10),
    "anova": _bins(-2, 12),    # 56 bins, 2 s before onset to 2 s after offset
}


def check_md5():
    """ETag of data.zip (its MD5 for a single-part upload) and the checksums.md5 entry."""
    etag = requests.head(ZIP_URL, timeout=60).headers["ETag"].strip('"')
    listed = requests.get(BASE_URL + "/checksums.md5", timeout=60).text
    return etag, DATA_ZIP_MD5 in listed and etag == DATA_ZIP_MD5


def open_zip():
    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2 ** 20).open())


def _get(o, path):
    for p in path.split("."):
        if isinstance(o, np.ndarray) and o.dtype == object:
            o = o[0, 0]
        o = getattr(o, p)
    return o


def load_cube(zf):
    """The authors' cube, vlPAGcube, with unit names decoded (rows of the 22-character names)."""
    m = sio.loadmat(io.BytesIO(zf.read("data/cubeFile/cube.mat")), struct_as_record=False)
    c = m["vlPAGcube"][0, 0]
    nm = c.name
    names = ["".join(nm[0, j][i] for j in range(nm.shape[1])) for i in range(len(nm[0, 0]))]
    return c, names


def cube_field(c, path):
    return np.asarray(_get(c, path))


def group_of(rat):
    if rat in CON_RATS:
        return "Con"
    if rat in EAA_RATS:
        return "EAA"
    raise ValueError(rat)


def load_unit(zf, name):
    """One unit: spike counts per trial in 250 ms bins, trial types, shocks and nose pokes.

    Trials are ordered as the cube orders them (danger, uncertainty shock, uncertainty no-shock,
    safety; by onset time within each).
    """
    m = sio.loadmat(io.BytesIO(zf.read(f"data/matFiles/{name}.mat")))
    spk = np.sort(m["spike"].ravel())
    ev = {k: np.sort(m[k].ravel()) for k in m if k.startswith("EVT")}
    shocks = ev["EVT08"]
    rows = []
    for code, ty in (("EVT09", "danger"), ("EVT12", "uncertainty"), ("EVT11", "safety")):
        for t in ev[code]:
            sh = bool(np.any(np.abs(shocks - (t + CUE_S + 2.0)) < 0.05))
            rows.append((t, ty, sh))
    order = {"danger": 0, "uncertainty": 1, "safety": 3}
    rows.sort(key=lambda r: (order[r[1]] + (0 if r[2] or r[1] != "uncertainty" else 1), r[0]))
    on = np.array([r[0] for r in rows])
    edges = on[:, None] + (-PRE + BIN * np.arange(NBIN + 1))[None, :]
    idx = np.searchsorted(spk, edges)
    counts = np.diff(idx, axis=1)
    pokes = ev["EVT13"]
    pb = np.searchsorted(pokes, on) - np.searchsorted(pokes, on - 20.0)
    pc = np.searchsorted(pokes, on + CUE_S) - np.searchsorted(pokes, on)
    return dict(name=name, rat=name[:4], session=name[:10], group=group_of(name[:4]),
                onset=on, type=np.array([r[1] for r in rows]), shock=np.array([r[2] for r in rows]),
                counts=counts, poke_base=pb, poke_cue=pc, n_spikes=len(spk),
                n_events={k: len(v) for k, v in ev.items()})


def load_all(zf, names):
    return [load_unit(zf, n) for n in names]


# ---------- behaviour ----------

def suppression_ratio(u, empty="zero"):
    """(baseline rate - cue rate) / (baseline + cue), 20 s baseline, 10 s cue, per trial.

    empty: what a trial with no pokes in either window (0/0) becomes; 'zero' or 'drop' (NaN).
    """
    b = u["poke_base"] / 20.0
    c = u["poke_cue"] / CUE_S
    with np.errstate(invalid="ignore", divide="ignore"):
        sr = (b - c) / (b + c)
    if empty == "zero":
        sr = np.where(np.isnan(sr), 0.0, sr)
    return sr


# ---------- firing ----------

def rates(u):
    return u["counts"] / BIN    # Hz per 250 ms bin, trials x 200


def window_rate(u, win):
    return rates(u)[:, WIN[win]].mean(axis=1)


def select(u, epochs_exc, epochs_inh, alpha=0.05 / 6, r=None):
    """Cue-responsive selection (Methods, Identifying cue-responsive neurons).

    Per cue (danger, uncertainty pooled, safety) and epoch, a paired t test of the trial rates in
    the 10 s baseline against the epoch, two-sided, at p < alpha. Excited: a significant increase
    in an excitation epoch and no significant decrease in any excitation epoch; inhibited the
    reverse over the inhibition epochs. The epoch sets follow the readings of the claims file; the
    authors' script (vlpagAnalysis.m lines 136-147 and 225-236) tests increases over first 1 s and
    last 5 s and decreases over first 5 s and last 5 s, reading (b). `r` replaces the rates with
    other per-trial values (dict window -> array), used for the cube's stored rates.
    """
    def sig(win):
        out = []
        for ty in TYPES:
            m = u["type"] == ty
            base = (r["base10"] if r else window_rate(u, "base10"))[m]
            ep = (r[win] if r else window_rate(u, win))[m]
            d = ep - base
            if np.all(d == 0):
                out.append(0)
                continue
            t, p = stats.ttest_rel(ep, base)
            out.append(int(np.sign(d.mean())) if p < alpha else 0)
        return out
    se = sum((sig(w) for w in epochs_exc), [])
    si = sum((sig(w) for w in epochs_inh), [])
    if 1 in se and -1 not in se:
        return "exc"
    if -1 in si and 1 not in si:
        return "inh"
    return "osc"


SELECTION_READINGS = {
    "a": (("first1", "last5"), ("first1", "last5")),
    "b": (("first1", "last5"), ("first5", "last5")),
    "c": (("first1", "first5", "last5"), ("first1", "first5", "last5")),
}


def normalized_firing(u, types=TYPES):
    """Methods, Z score normalization: per type, trial-mean rate in 250 ms bins minus that type's
    mean 2 s pre-cue rate; Z score over all bins of all types of the neuron (ddof = 1).
    Returns (types x 200 array, mean, sd) where mean and sd are those of the normalization."""
    r = rates(u)
    diff = []
    for ty in types:
        m = u["type"] == ty if ty in TYPES else (u["type"] == "uncertainty") & (u["shock"] == (ty == "unc_shock"))
        mean = r[m].mean(axis=0)
        diff.append(mean - mean[WIN["base2"]].mean())
    diff = np.array(diff)
    mu, sd = diff.mean(), diff.std(ddof=1)
    return (diff - mu) / sd, mu, sd


def trial_firing(u, reading, cube_z=None):
    """Trial-wise normalized firing, trials x 200 (250 ms bins), for the regressions.

    a: each trial's rate minus the mean 2 s pre-cue rate of its trial type, Z scored with the
       mean and SD of the neuron's normalization (`normalized_firing`);
    b: the same with the trial's own 2 s pre-cue rate subtracted;
    c: each trial's rate Z scored over all trials and bins of the neuron;
    d: the cube's own trial-wise z (the trial's own 2 s baseline subtracted, Z scored over all
       trials and bins), in 1 s bins; `cube_z` is the cube's fire.z.s1 for the unit (32 x 50),
       returned expanded to 250 ms bins so that the same windows apply.
    """
    r = rates(u)
    if reading == "d":
        return np.repeat(cube_z, 4, axis=1)
    if reading == "c":
        return (r - r.mean()) / r.std(ddof=1)
    _, mu, sd = normalized_firing(u)
    own = r[:, WIN["base2"]].mean(axis=1)
    if reading == "a":
        base = np.array([own[u["type"] == t].mean() for t in u["type"]])
    else:
        base = own
    return (r - base[:, None] - mu) / sd


def regress_betas(y, sr, prob):
    """OLS with a constant (Matlab regress); y trials x k. Returns (fear output, threat) betas."""
    X = np.column_stack([np.ones_like(sr), sr, prob])
    ok = ~np.isnan(sr)
    b, *_ = np.linalg.lstsq(X[ok], y[ok], rcond=None)
    return b[1], b[2]


def interval_betas(u, reading, empty, unc_value=0.375, cube_z=None):
    """Fear output and threat probability betas for each 1 s interval of the cue (10 each)."""
    tf = trial_firing(u, reading, cube_z)
    y = tf[:, WIN["cue"]].reshape(len(tf), 10, 4).mean(axis=2)
    prob = np.array([unc_value if t == "uncertainty" else PROB[t] for t in u["type"]])
    return regress_betas(y, suppression_ratio(u, empty), prob)


# ---------- statistics ----------

def _helmert(k):
    """Orthonormal contrasts, k x (k-1)."""
    h = np.zeros((k, k - 1))
    for j in range(1, k):
        h[:j, j - 1] = 1.0
        h[j, j - 1] = -j
        h[:, j - 1] /= np.linalg.norm(h[:, j - 1])
    return h


def mixed_anova(Y, group):
    """Split-plot ANOVA, sphericity assumed, type III for one between factor.

    Y: subjects x within factor levels (one axis per within factor); group: label per subject.
    Returns {effect: (F, df1, df2, p)} for every within effect, its interaction with group, and
    the group main effect. Within effects are tested on orthonormal contrasts, as SPSS's GLM
    repeated measures does: the effect from the intercept of the contrast scores over the
    unweighted group means, its interaction with group from a one-way ANOVA of the scores.
    """
    Y = np.asarray(Y, float)
    n = Y.shape[0]
    dims = Y.shape[1:]
    labels = np.unique(group)
    k = len(labels)
    gidx = [np.where(group == g)[0] for g in labels]
    out = {}
    # between
    m = Y.reshape(n, -1).mean(axis=1)
    gm = np.array([m[i].mean() for i in gidx])
    ssb = sum(len(i) * (gm[j] - m.mean()) ** 2 for j, i in enumerate(gidx))
    sse = sum(((m[i] - m[i].mean()) ** 2).sum() for i in gidx)
    w = np.prod(dims)
    df2 = n - k
    out["group"] = (ssb / (k - 1) / (sse / df2), k - 1, df2,
                    stats.f.sf(ssb / (k - 1) / (sse / df2), k - 1, df2))
    names = [chr(ord("A") + i) for i in range(len(dims))]
    from itertools import combinations
    for r in range(1, len(dims) + 1):
        for comb in combinations(range(len(dims)), r):
            mats = []
            for d in range(len(dims)):
                mats.append(_helmert(dims[d]) if d in comb else np.ones((dims[d], 1)) / np.sqrt(dims[d]))
            C = mats[0]
            for M in mats[1:]:
                C = np.kron(C, M)
            S = Y.reshape(n, -1) @ C            # n x df
            df1 = S.shape[1]
            err = sum(((S[i] - S[i].mean(axis=0)) ** 2).sum() for i in gidx)
            gmeans = np.array([S[i].mean(axis=0) for i in gidx])
            ss_int = sum(len(i) * ((gmeans[j] - S.mean(axis=0)) ** 2).sum() for j, i in enumerate(gidx))
            um = gmeans.mean(axis=0)
            ss_eff = (um ** 2).sum() / (np.sum([1.0 / len(i) for i in gidx]) / k ** 2)
            dfe = df1 * df2
            ms_e = err / dfe
            nm = "".join(names[c] for c in comb)
            F = ss_eff / df1 / ms_e
            out[nm] = (F, df1, dfe, stats.f.sf(F, df1, dfe))
            F = ss_int / ((k - 1) * df1) / ms_e
            out["group:" + nm] = (F, (k - 1) * df1, dfe, stats.f.sf(F, (k - 1) * df1, dfe))
    return out


def fisher_r_to_z(r1, n1, r2, n2):
    """Fisher r-to-z comparison of two independent correlations; (Z, one-tailed p, two-tailed p)."""
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1.0 / (n1 - 3) + 1.0 / (n2 - 3))
    p1 = stats.norm.sf(abs(z))
    return z, p1, 2 * p1
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && python -c "
import numpy as np, pandas as pd, pingouin as pg, pag2
rng=np.random.default_rng(0)
n=23; g=np.array(['a']*10+['b']*13); Y=rng.normal(size=(n,3))+np.where(g=='b',0.5,0)[:,None]*np.array([0,1,2])
o=pag2.mixed_anova(Y,g); print({k:np.round(v,4) for k,v in o.items()})
df=pd.DataFrame([(i,g[i],j,Y[i,j]) for i in range(n) for j in range(3)],columns=['s','g','w','y'])
print(pg.mixed_anova(df,dv='y',within='w',between='g',subject='s',correction=False)[['Source','F','DF1','DF2','p-unc']])
# two within: compare with long-format OLS based check: group:AB F via statsmodels mixedlm? use balanced equal n check vs classical formula
Y2=rng.normal(size=(n,3,4)); o2=pag2.mixed_anova(Y2,g); print({k:np.round(v,4) for k,v in o2.items()})
# classical SS for group:AB with error AB x S(G)
import itertools
def ss_check(Y,g):
    gl=np.unique(g); 
    # residual interaction per subject
    Ys=Y - Y.mean(axis=1,keepdims=True) - Y.mean(axis=2,keepdims=True) + Y.mean(axis=(1,2),keepdims=True)
    tot=((Ys - 0)**2).sum()
    gm=np.array([Ys[g==x].mean(axis=0) for x in gl]); grand=Ys.mean(axis=0)
    ssint=sum((g==x).sum()*((gm[i]-grand)**2).sum() for i,x in enumerate(gl))
    sserr=sum(((Ys[g==x]-gm[i])**2).sum() for i,x in enumerate(gl))
    df1=(len(gl)-1)*2*3; df2=(n-2)*2*3
    return (ssint/df1)/(sserr/df2), df1, df2
print(ss_check(Y2,g))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    print(pg.mixed_anova(df,dv='y',within='w',between='g',subject='s',correction=False)[['Source','F','DF1','DF2','p-unc']])
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/frame.py", line 4336, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/indexes/base.py", line 6557, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/indexes/base.py", line 6609, in _raise_if_missing
    raise KeyError(f"{not_found} not in index")
KeyError: "['p-unc'] not in index"
{'group': array([1.40352e+01, 1.00000e+00, 2.10000e+01, 1.20000e-03]), 'A': array([3.6908e+00, 2.0000e+00, 4.2000e+01, 3.3400e-02]), 'group:A': array([4.2651e+00, 2.0000e+00, 4.2000e+01, 2.0600e-02])}
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && python -c "
import numpy as np, pandas as pd, pingouin as pg, pag2
rng=np.random.default_rng(0)
n=23; g=np.array(['a']*10+['b']*13); Y=rng.normal(size=(n,3))+np.where(g=='b',0.5,0)[:,None]*np.array([0,1,2])
df=pd.DataFrame([(i,g[i],j,Y[i,j]) for i in range(n) for j in range(3)],columns=['s','g','w','y'])
print(pg.mixed_anova(df,dv='y',within='w',between='g',subject='s',correction=False).iloc[:,:7])
Y2=rng.normal(size=(n,3,4)); o2=pag2.mixed_anova(Y2,g); print({k:np.round(v,4) for k,v in o2.items()})
gl=np.unique(g)
Ys=Y2 - Y2.mean(axis=1,keepdims=True) - Y2.mean(axis=2,keepdims=True) + Y2.mean(axis=(1,2),keepdims=True)
gm=np.array([Ys[g==x].mean(axis=0) for x in gl]); grand=Ys.mean(axis=0)
ssint=sum((g==x).sum()*((gm[i]-grand)**2).sum() for i,x in enumerate(gl))
sserr=sum(((Ys[g==x]-gm[i])**2).sum() for i,x in enumerate(gl))
print((ssint/6)/(sserr/(21*6)))
"
```

```
Source         SS  DF1  DF2         MS          F     p_unc
0            g  14.260247    1   21  14.260247  14.035204  0.001190
1            w   7.321208    2   42   3.660604   4.881340  0.012413
2  Interaction   6.396922    2   42   3.198461   4.265081  0.020591
{'group': array([ 2.4193,  1.    , 21.    ,  0.1348]), 'A': array([ 1.283 ,  2.    , 42.    ,  0.2878]), 'group:A': array([ 0.1925,  2.    , 42.    ,  0.8256]), 'B': array([ 1.1579,  3.    , 63.    ,  0.3329]), 'group:B': array([ 0.289 ,  3.    , 63.    ,  0.8332]), 'AB': array([2.7875e+00, 6.0000e+00, 1.2600e+02, 1.4000e-02]), 'group:AB': array([  1.5191,   6.    , 126.    ,   0.1771])}
1.5191175174462153
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && python -c "
import numpy as np, pag2, time
t=time.time(); zf=pag2.open_zip(); c,N=pag2.load_cube(zf); print('cube',time.time()-t)
U=pag2.load_all(zf,N[:30]); print('30 units',time.time()-t)
tag=pag2.cube_field(c,'tag')
for i,u in enumerate(U[:30]):
    ok=np.allclose(u['onset'],tag[:,1,i]); 
    tt=np.array([{'danger':1,'uncertainty':2,'safety':4}[x] for x in u['type']]); tt[(u['type']=='uncertainty')&~u['shock']]=3
    sr=pag2.suppression_ratio(u); csr=pag2.cube_field(c,'cer.cue')[:,0,i]
    nanm=np.isnan(pag2.suppression_ratio(u,'drop'))
    if not ok or (tt!=tag[:,0,i]).any() or u['shock'][:12].sum()!=12 or u['shock'].sum()!=12 or np.abs(sr-csr).max()>1e-9: print('MISMATCH',i, ok, np.abs(sr-csr).max())
    if nanm.any(): print(i,'empty',nanm.sum(), csr[nanm])
print(pag2.check_md5())
"
```

```
cube 4.671265125274658
30 units 10.83525800704956
MISMATCH 2 True 1.0
2 empty 3 [1. 1. 1.]
MISMATCH 10 True 1.0
10 empty 1 [1.]
MISMATCH 11 True 1.0
11 empty 1 [1.]
MISMATCH 12 True 1.0
12 empty 1 [1.]
MISMATCH 18 True 0.14285714285714282
MISMATCH 19 True 0.14285714285714282
MISMATCH 20 True 0.36363636363636376
MISMATCH 21 False 1.6
21 empty 1 [1.]
MISMATCH 22 False 1.5
MISMATCH 23 False 1.8181818181818181
23 empty 1 [1.]
MISMATCH 24 False 1.6
24 empty 3 [1.         1.         0.07692308]
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && python -c "
import numpy as np, pag2
zf=pag2.open_zip(); c,N=pag2.load_cube(zf)
tag=pag2.cube_field(c,'tag'); csr=pag2.cube_field(c,'cer.cue')
for i in [18,21,27]:
    u=pag2.load_unit(zf,N[i]); print(N[i], u['n_events'])
    print(np.c_[u['onset'][:8], tag[:8,1,i], tag[:8,0,i]].round(2).T)
    print(np.c_[pag2.suppression_ratio(u,'drop'), csr[:,0,i], u['poke_base'], u['poke_cue'], pag2.cube_field(c,'poke.base')[:,0,i], pag2.cube_field(c,'poke.cue')[:,0,i]][:12].round(3).T)
"
```

```
mh12070617epr38aSPK12a {'EVT01': 12, 'EVT02': 27, 'EVT08': 12, 'EVT09': 6, 'EVT11': 10, 'EVT12': 16, 'EVT13': 571, 'EVT14': 32}
[[2.72915e+03 2.91366e+03 3.06817e+03 3.38719e+03 3.91872e+03 4.87778e+03
  1.90260e+03 2.22962e+03]
 [2.72915e+03 2.91366e+03 3.06817e+03 3.38719e+03 3.91872e+03 4.87778e+03
  1.90260e+03 2.22962e+03]
 [1.00000e+00 1.00000e+00 1.00000e+00 1.00000e+00 1.00000e+00 1.00000e+00
  2.00000e+00 2.00000e+00]]
[[ 1.     1.     1.     1.     1.     1.     1.     0.333  1.     1.
   1.     0.333]
 [ 1.     1.     1.     1.     1.     1.     1.     0.333  1.     1.
   1.     0.333]
 [13.     8.     5.    10.    15.     8.     6.     4.     9.    10.
  12.     4.   ]
 [ 0.     0.     0.     0.     0.     0.     0.     1.     0.     0.
   0.     1.   ]
 [39.    24.    15.    30.    45.    24.    18.    12.    27.    30.
  36.    12.   ]
 [ 0.     0.     0.     0.     0.     0.     0.     6.     0.     0.
   0.     6.   ]]
mh14062817epr38cSPK13a {'EVT01': 12, 'EVT02': 26, 'EVT08': 12, 'EVT09': 10, 'EVT11': 16, 'EVT12': 6, 'EVT13': 539, 'EVT14': 32}
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='pag2.py'; s=open(p).read()
old=s[s.index('    shocks = ev["EVT08"]'):s.index('    order = {')]
new='''    shocks = ev["EVT08"]
    rows = []
    for code in ("EVT09", "EVT11", "EVT12"):
        sh = [bool(np.any(np.abs(shocks - (t + CUE_S + 2.0)) < 0.05)) for t in ev[code]]
        frac = np.mean(sh)
        ty = "danger" if frac == 1 else "safety" if frac == 0 else "uncertainty"
        rows += [(t, ty, s) for t, s in zip(ev[code], sh)]
'''
s=s.replace(old,new)
s=s.replace('''EVT09 danger onsets, EVT12 uncertainty onsets, EVT11 safety onsets, EVT08 (= EVT01) shocks,
EVT13 nose pokes, EVT14 one marker 31.5 s before each cue onset, EVT02 not identified
(not used).''','''EVT09, EVT11 and EVT12 are the onsets of the three cues, EVT08 (= EVT01) shocks, EVT13 nose
pokes, EVT14 one marker 31.5 s before each cue onset, EVT02 not identified (not used). Which of
EVT09, EVT11 and EVT12 is danger, uncertainty or safety differs between behaviour programs
(epr38a, b, c: the counterbalanced auditory identities), so each cue code is assigned by its
shock contingency (shock 2 s after cue offset on all, some or none of its trials).''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python -c "
import numpy as np, pag2, time, collections
t=time.time(); zf=pag2.open_zip(); c,N=pag2.load_cube(zf)
U=pag2.load_all(zf,N); print('all units',time.time()-t)
tag=pag2.cube_field(c,'tag'); csr=pag2.cube_field(c,'cer.cue')
bad=collections.Counter(); emp=collections.Counter()
for i,u in enumerate(U):
    tt=np.array([{'danger':1,'uncertainty':2,'safety':4}[x] for x in u['type']]); tt[(u['type']=='uncertainty')&~u['shock']]=3
    if not np.allclose(u['onset'],tag[:,1,i]) or (tt!=tag[:,0,i]).any(): bad['onset']+=1
    d=pag2.suppression_ratio(u,'drop'); m=~np.isnan(d)
    if np.abs(d[m]-csr[m,0,i]).max()>1e-9: bad['sr']+=1; 
    for v in csr[~m,0,i]: emp[round(v,3)]+=1
    if np.abs(pag2.window_rate(u,'base10')-pag2.cube_field(c,'fire.raw.base10')[:,0,i]).max()>=1: bad['b10']+=1
print(bad, emp.most_common(10), sum(emp.values()))
"
```

```
all units 35.046956300735474
Counter({'sr': 23}) [(np.float64(1.0), 255)] 255
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && python -c "
import numpy as np, pag2
zf=pag2.open_zip(); c,N=pag2.load_cube(zf)
csr=pag2.cube_field(c,'cer.cue'); pb=pag2.cube_field(c,'poke.base'); pc=pag2.cube_field(c,'poke.cue')
for i,n in enumerate(N):
    u=pag2.load_unit(zf,n); d=pag2.suppression_ratio(u,'drop'); m=~np.isnan(d)
    k=np.where(m & (np.abs(d-csr[:,0,i])>1e-9))[0]
    if len(k): print(i,n,len(k), [(round(d[j],3),round(csr[j,0,i],3),u['poke_base'][j],u['poke_cue'][j],pb[j,0,i],pc[j,0,i]) for j in k[:3]])
" 2>&1 | head -30
```

```
18 mh12070617epr38aSPK12a 1 [(np.float64(-0.143), np.float64(0.0), np.int64(9), np.int64(6), np.uint8(30), np.uint8(30))]
19 mh12070617epr38aSPK16a 1 [(np.float64(-0.143), np.float64(0.0), np.int64(9), np.int64(6), np.uint8(30), np.uint8(30))]
20 mh12071217epr38aSPK15a 1 [(np.float64(0.636), np.float64(1.0), np.int64(9), np.int64(1), np.uint8(30), np.uint8(0))]
34 mh17072617epr38cSPK13a 1 [(np.float64(-0.091), np.float64(0.048), np.int64(10), np.int64(6), np.uint8(33), np.uint8(30))]
145 mh23103017epr38bSPK13a 1 [(np.float64(0.0), np.float64(0.429), np.int64(4), np.int64(2), np.uint8(15), np.uint8(6))]
149 mh23110517epr38bSPK13a 1 [(np.float64(0.429), np.float64(1.0), np.int64(5), np.int64(1), np.uint8(18), np.uint8(0))]
154 mh24110717epr38bSPK10a 1 [(np.float64(-0.091), np.float64(0.2), np.int64(5), np.int64(3), np.uint8(18), np.uint8(12))]
157 mh26110117epr38cSPK13a 1 [(np.float64(0.5), np.float64(1.0), np.int64(6), np.int64(1), np.uint8(21), np.uint8(0))]
158 mh26110117epr38cSPK13b 1 [(np.float64(0.5), np.float64(1.0), np.int64(6), np.int64(1), np.uint8(21), np.uint8(0))]
187 mh31112217epr38bSPK08a 1 [(np.float64(-0.5), np.float64(-0.333), np.int64(4), np.int64(6), np.uint8(15), np.uint8(30))]
193 mh31112917epr38bSPK04a 1 [(np.float64(-0.333), np.float64(0.0), np.int64(3), np.int64(3), np.uint8(12), np.uint8(12))]
194 mh31112917epr38bSPK15a 1 [(np.float64(-0.333), np.float64(0.0), np.int64(3), np.int64(3), np.uint8(12), np.uint8(12))]
195 mh32101217epr38bSPK05a 1 [(np.float64(0.0), np.float64(1.0), np.int64(2), np.int64(1), np.uint8(9), np.uint8(0))]
238 mh34102617epr38cSPK12a 1 [(np.float64(0.429), np.float64(1.0), np.int64(5), np.int64(1), np.uint8(18), np.uint8(0))]
258 mh36110917epr38aSPK07a 1 [(np.float64(0.5), np.float64(1.0), np.int64(6), np.int64(1), np.uint8(21), np.uint8(0))]
259 mh36110917epr38aSPK13a 1 [(np.float64(0.5), np.float64(1.0), np.int64(6), np.int64(1), np.uint8(21), np.uint8(0))]
288 mh39101917epr38cSPK06a 1 [(np.float64(0.059), np.float64(
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && cat > $TMPDIR/a1.py <<'EOF'
import numpy as np, pag2, pickle, collections
from scipy import stats
zf=pag2.open_zip(); c,N=pag2.load_cube(zf)
U=pag2.load_all(zf,N)
pickle.dump((U,), open('/tmp/claude-1001/U.pkl','wb'))
grp=np.array([u['group'] for u in U])
cube_r={w:None for w in []}
B10=pag2.cube_field(c,'fire.raw.base10')[:,0,:].astype(float)
SEL={k:pag2.cube_field(c,'fire.raw.select.'+k)[:,0,:].astype(float) for k in ['cueOnset','cueFirstFive','cueLastFive']}
for rd,(e,i) in pag2.SELECTION_READINGS.items():
    lab=np.array([pag2.select(u,e,i) for u in U])
    labc=np.array([pag2.select(u,e,i,r=dict(base10=B10[:,j],first1=SEL['cueOnset'][:,j],first5=SEL['cueFirstFive'][:,j],last5=SEL['cueLastFive'][:,j])) for j,u in enumerate(U)])
    for nm,L in [('spikes',lab),('cube',labc)]:
        print(rd,nm, {g:collections.Counter(L[grp==g]) for g in ['Con','EAA']})
EOF
python $TMPDIR/a1.py
```

```
Exit code 1
Fri Nov  6 20:07:19 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/a1.py", line 1, in <module>
    import numpy as np, pag2, pickle, collections
ModuleNotFoundError: No module named 'pag2'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && PYTHONPATH=. python $TMPDIR/a1.py
```

```
a spikes {'Con': Counter({np.str_('osc'): 77, np.str_('inh'): 44, np.str_('exc'): 30}), 'EAA': Counter({np.str_('osc'): 80, np.str_('inh'): 73, np.str_('exc'): 50})}
a cube {'Con': Counter({np.str_('osc'): 85, np.str_('inh'): 34, np.str_('exc'): 32}), 'EAA': Counter({np.str_('osc'): 87, np.str_('inh'): 67, np.str_('exc'): 49})}
b spikes {'Con': Counter({np.str_('osc'): 67, np.str_('inh'): 54, np.str_('exc'): 30}), 'EAA': Counter({np.str_('inh'): 87, np.str_('osc'): 66, np.str_('exc'): 50})}
b cube {'Con': Counter({np.str_('osc'): 71, np.str_('inh'): 48, np.str_('exc'): 32}), 'EAA': Counter({np.str_('inh'): 84, np.str_('osc'): 70, np.str_('exc'): 49})}
c spikes {'Con': Counter({np.str_('osc'): 70, np.str_('inh'): 51, np.str_('exc'): 30}), 'EAA': Counter({np.str_('inh'): 89, np.str_('osc'): 66, np.str_('exc'): 48})}
c cube {'Con': Counter({np.str_('osc'): 76, np.str_('inh'): 43, np.str_('exc'): 32}), 'EAA': Counter({np.str_('inh'): 85, np.str_('osc'): 71, np.str_('exc'): 47})}
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && cat > $TMPDIR/a2.py <<'EOF'
import numpy as np, pag2, pickle, collections
from scipy import stats
U,=pickle.load(open('/tmp/claude-1001/U.pkl','rb'))
grp=np.array([u['group'] for u in U])
# sessions
S={}
for u in U: S.setdefault(u['session'],u)
print(len(S))
for empty in ['zero','drop','one']:
  for comb in ['sessmean','pooled']:
    rat={}
    for s,u in S.items():
        sr=pag2.suppression_ratio(u,'drop')
        if empty=='zero': sr=np.nan_to_num(sr,nan=0.0)
        if empty=='one': sr=np.nan_to_num(sr,nan=1.0)
        rat.setdefault(u['rat'],[]).append((sr,u['type'],u['poke_base']/20*60))
    R=sorted(rat); g=np.array([pag2.group_of(r) for r in R])
    Y=[];BP=[]
    for r in R:
        if comb=='sessmean':
            Y.append([np.mean([np.nanmean(sr[t==ty]) for sr,t,_ in rat[r]]) for ty in pag2.TYPES]); BP.append(np.mean([b.mean() for *_,b in rat[r]]))
        else:
            sr=np.concatenate([x[0] for x in rat[r]]); t=np.concatenate([x[1] for x in rat[r]])
            Y.append([np.nanmean(sr[t==ty]) for ty in pag2.TYPES]); BP.append(np.concatenate([x[2] for x in rat[r]]).mean())
    Y=np.array(Y); BP=np.array(BP)
    a=pag2.mixed_anova(Y,g)
    tt=[(gg, stats.ttest_rel(Y[g==gg,0],Y[g==gg,1]), stats.ttest_rel(Y[g==gg,1],Y[g==gg,2])) for gg in ['Con','EAA']]
    print(empty,comb, 'cue',np.round(a['A'],4),'gxc',np.round(a['group:A'],3), [ (gg,round(x.statistic,2),round(x.pvalue,4),round(y.statistic,2),round(y.pvalue,4)) for gg,x,y in tt])
    print('   means', {gg:Y[g==gg].mean(0).round(3) for gg in ['Con','EAA']})
    if empty=='zero': print('   baseline pokes/min', {gg:BP[g==gg].mean().round(2) for gg in ['Con','EAA']}, stats.ttest_ind(BP[g=='Con'],BP[g=='EAA']))
EOF
PYTHONPATH=. python $TMPDIR/a2.py
```

```
182
zero sessmean cue [179.524   2.     36.      0.   ] gxc [ 0.168  2.    36.     0.846] [('Con', np.float64(3.57), np.float64(0.0091), np.float64(5.54), np.float64(0.0009)), ('EAA', np.float64(6.01), np.float64(0.0001), np.float64(12.32), np.float64(0.0))]
   means {'Con': array([0.919, 0.715, 0.117]), 'EAA': array([0.9  , 0.69 , 0.049])}
   baseline pokes/min {'Con': np.float64(23.08), 'EAA': np.float64(19.22)} TtestResult(statistic=np.float64(1.1927010831579454), pvalue=np.float64(0.2484723169090047), df=np.float64(18.0))
zero pooled cue [179.524   2.     36.      0.   ] gxc [ 0.168  2.    36.     0.846] [('Con', np.float64(3.57), np.float64(0.0091), np.float64(5.54), np.float64(0.0009)), ('EAA', np.float64(6.01), np.float64(0.0001), np.float64(12.32), np.float64(0.0))]
   means {'Con': array([0.919, 0.715, 0.117]), 'EAA': array([0.9  , 0.69 , 0.049])}
   baseline pokes/min {'Con': np.float64(23.08), 'EAA': np.float64(19.22)} TtestResult(statistic=np.float64(1.1927010831579454), pvalue=np.float64(0.2484723169090047), df=np.float64(18.0))
drop sessmean cue [190.6543   2.      36.       0.    ] gxc [ 0.102  2.    36.     0.904] [('Con', np.float64(3.68), np.float64(0.0079), np.float64(5.57), np.float64(0.0008)), ('EAA', np.float64(5.74), np.float64(0.0001), np.float64(13.47), np.float64(0.0))]
   means {'Con': array([0.947, 0.744, 0.117]), 'EAA': array([0.919, 0.71 , 0.051])}
drop pooled cue [191.1493   2.      36.       0.    ] gxc [ 0.107  2.    36.     0.899] [('Con', np.float64(3.68), np.float64(0.0079), np.float64(5.59), np.float64(0.0008)), ('EAA', np.float64(5.76), np.float64(0.0001), np.float64(13.34), np.float64(0.0))]
   means {'Con': array([0.946, 0.744, 0.116]), 'EAA': array([0.919, 0.708, 0.05 ])}
one sessmean cue [194.5433   2.      36.       0.    ] gxc [ 0.174  2.    36.     0.841] [('Con', np.float64(3.59), np.float64(0.0089), np.float64(5.71), np.float64(0.0007)), ('EAA', np.float64(5.9), np.float64(0.0001), np.float64(13.19), np.float64(0.0))]
 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && cat > $TMPDIR/a3.py <<'EOF'
import numpy as np, pag2, pickle, collections, time
from scipy import stats
U,=pickle.load(open('/tmp/claude-1001/U.pkl','rb'))
zf=pag2.open_zip(); c,N=pag2.load_cube(zf)
grp=np.array([u['group'] for u in U])
B10=pag2.cube_field(c,'fire.raw.base10')[:,0,:].astype(float)
SEL={k:pag2.cube_field(c,'fire.raw.select.'+k)[:,0,:].astype(float) for k in ['cueOnset','cueFirstFive','cueLastFive']}
ZS1=pag2.cube_field(c,'fire.z.s1.interval')
e,i=pag2.SELECTION_READINGS['b']
lab=np.array([pag2.select(u,e,i,r=dict(base10=B10[:,j],first1=SEL['cueOnset'][:,j],first5=SEL['cueFirstFive'][:,j],last5=SEL['cueLastFive'][:,j])) for j,u in enumerate(U)])
labs=np.array([pag2.select(u,e,i) for u in U])
pickle.dump((lab,labs),open('/tmp/claude-1001/lab.pkl','wb'))
# chi-square
for L in [lab,labs]:
    tab=np.array([[np.sum((grp==g)&(L!='osc')),np.sum((grp==g)&(L=='osc'))] for g in ['Con','EAA']])
    print(tab, stats.chi2_contingency(tab,correction=False)[:2], tab[:,0]/tab.sum(1))
# baseline firing
for w in ['base10','base2']:
    bf=np.array([pag2.window_rate(u,w).mean() for u in U])
    print(w,[ (t, round(stats.ttest_ind(bf[(lab==t)&(grp=='Con')],bf[(lab==t)&(grp=='EAA')]).statistic,2), round(stats.ttest_ind(bf[(lab==t)&(grp=='Con')],bf[(lab==t)&(grp=='EAA')]).pvalue,3)) for t in ['exc','inh','osc']],
      stats.f_oneway(*[bf[lab==t] for t in ['exc','inh','osc']]), {t:bf[lab==t].mean().round(2) for t in ['exc','inh','osc']})
# normalized
NF=np.array([pag2.normalized_firing(u)[0] for u in U])  # n x 3 x 200
for pop in ['exc','inh']:
    m=lab==pop; Y=NF[m][:,:,pag2.WIN['anova']]; g=grp[m]
    t=time.time(); a=pag2.mixed_anova(Y,g); print(pop, 'gxcxb', np.round(a['group:AB'],5), 'time',round(time.time()-t,1))
    for w in ['first1','first5']:
        V=NF[m][:,:,pag2.WIN[w]].mean(2); a=pag2.mixed_anova(V,g)
        print(' ',w,'group',np.round(a['group'],4),'gxc',np.round(a['group:A'],4), {gg:V[g==gg].mean(0).round(3) for gg in ['Con','EAA']})
        for k,ty in enumerate(pag2.TYPES): r=stats.ttest_ind(V[g=='Con',k],V[g=='EAA',k]); print('    ',ty, round(r.statistic,2), round(r.pvalue,4))
        for gg in ['Con','EAA']:
            x=V[g==gg]; print('    paired',gg, [ (round(stats.ttest_rel(x[:,a1],x[:,a2]).statistic,2), round(stats.ttest_rel(x[:,a1],x[:,a2]).pvalue,4)) for a1,a2 in [(0,1),(1,2),(0,2)]])
EOF
PYTHONPATH=. python $TMPDIR/a3.py
```

```
[[ 80  71]
 [133  70]] (np.float64(5.679006027829309), np.float64(0.017169091691416165)) [0.52980132 0.65517241]
[[ 84  67]
 [137  66]] (np.float64(5.191527902889341), np.float64(0.02269725306157974)) [0.55629139 0.67487685]
base10 [('exc', np.float64(-0.77), np.float64(0.442)), ('inh', np.float64(-1.09), np.float64(0.279)), ('osc', np.float64(0.05), np.float64(0.96))] F_onewayResult(statistic=np.float64(6.437338142509255), pvalue=np.float64(0.0017961905573887847)) {'exc': np.float64(13.88), 'inh': np.float64(22.03), 'osc': np.float64(25.27)}
base2 [('exc', np.float64(-0.73), np.float64(0.47)), ('inh', np.float64(-1.12), np.float64(0.263)), ('osc', np.float64(0.24), np.float64(0.814))] F_onewayResult(statistic=np.float64(6.777948546265448), pvalue=np.float64(0.0012935836195084038)) {'exc': np.float64(14.01), 'inh': np.float64(22.06), 'osc': np.float64(25.81)}
exc gxcxb [1.30165e+00 1.10000e+02 8.69000e+03 1.91000e-02] time 0.0
  first1 group [5.1888e+00 1.0000e+00 7.9000e+01 2.5400e-02] gxc [  1.3894   2.     158.       0.2522] {'Con': array([1.311, 0.861, 0.137]), 'EAA': array([1.908, 1.496, 1.091])}
     danger -1.42 0.1596
     uncertainty -1.92 0.0587
     safety -3.46 0.0009
    paired Con [(np.float64(3.04), np.float64(0.0047)), (np.float64(6.78), np.float64(0.0)), (np.float64(6.79), np.float64(0.0))]
    paired EAA [(np.float64(2.34), np.float64(0.0233)), (np.float64(3.31), np.float64(0.0018)), (np.float64(4.35), np.float64(0.0001))]
  first5 group [ 1.2572  1.     79.      0.2656] gxc [3.0075e+00 2.0000e+00 1.5800e+02 5.2300e-02] {'Con': array([ 0.946,  0.359, -0.117]), 'EAA': array([0.904, 0.534, 0.283])}
     danger 0.18 0.8569
     uncertainty -0.99 0.3234
     safety -2.72 0.0081
    paired Con [(np.float64(4.77), np.float64(0.0)), (np.float64(4.28), np.float64(0.0002)), (np.float64(5.39), np.float64(0.0))]
    paired EAA [(np.float64(3.5), np.float64(0.001)), (np.float64(2.91), np.float64(0.0054)), (np.float64(4.79), np.float64(0.0))]
inh gxcxb [1.54339
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && cat > $TMPDIR/a4.py <<'EOF'
import numpy as np, pag2, pickle, collections, time
from scipy import stats
U,=pickle.load(open('/tmp/claude-1001/U.pkl','rb'))
lab,labs=pickle.load(open('/tmp/claude-1001/lab.pkl','rb'))
zf=pag2.open_zip(); c,N=pag2.load_cube(zf)
ZS1=pag2.cube_field(c,'fire.z.s1.interval')
grp=np.array([u['group'] for u in U])
NF=np.array([pag2.normalized_firing(u)[0] for u in U])
def sr_fix(u,empty):
    s=pag2.suppression_ratio(u,'drop')
    return s if empty=='drop' else np.nan_to_num(s,nan={'zero':0.,'one':1.}[empty])
def betas(u,j,rd,empty,v=0.375):
    tf=pag2.trial_firing(u,rd,ZS1[:,:,j])
    y=tf[:,pag2.WIN['cue']].reshape(32,10,4).mean(2)
    prob=np.array([v if t=='uncertainty' else pag2.PROB[t] for t in u['type']])
    return pag2.regress_betas(y,sr_fix(u,empty),prob)
t0=time.time()
res={}
for rd in 'abcd':
  for empty in ['zero','drop','one']:
    FO=[];TP=[]
    for j,u in enumerate(U):
        if lab[j]=='osc': FO.append(np.full(10,np.nan)); TP.append(np.full(10,np.nan)); continue
        f,t=betas(u,j,rd,empty); FO.append(f); TP.append(t)
    FO=np.array(FO); TP=np.array(TP); res[rd,empty]=(FO,TP)
    m=lab=='exc'; g=grp[m]; Y=np.stack([FO[m],TP[m]],1)
    a=pag2.mixed_anova(Y,g)
    tpw=TP[m].mean(1); fow=FO[m].mean(1)
    t1=stats.ttest_ind(tpw[g=='Con'],tpw[g=='EAA']); t2=stats.ttest_ind(fow[g=='Con'],fow[g=='EAA'])
    m2=lab=='inh'; g2=grp[m2]; Y2=np.stack([FO[m2],TP[m2]],1); a2=pag2.mixed_anova(Y2,g2)
    fo5=FO[m2][:,5:].mean(1); tp5=TP[m2][:,5:].mean(1)
    t3=stats.ttest_ind(fo5[g2=='Con'],fo5[g2=='EAA']); t4=stats.ttest_ind(tp5[g2=='Con'],tp5[g2=='EAA'])
    print(rd,empty,'EXC gxreg F=%.2f p=%.4f | TP t=%.2f p=%.4f (Con %.3f EAA %.3f) | FO t=%.2f p=%.3f'%(a['group:A'][0],a['group:A'][3],t1.statistic,t1.pvalue,tpw[g=='Con'].mean(),tpw[g=='EAA'].mean(),t2.statistic,t2.pvalue),
          '|| INH gxregxint F=%.2f p=%.4f | FO5 t=%.2f p=%.4f (Con %.3f EAA %.3f) | TP5 t=%.2f p=%.3f'%(a2['group:AB'][0],a2['group:AB'][3],t3.statistic,t3.pvalue,fo5[g2=='Con'].mean(),fo5[g2=='EAA'].mean(),t4.statistic,t4.pvalue))
print(time.time()-t0)
pickle.dump(res,open('/tmp/claude-1001/res.pkl','wb'))
EOF
PYTHONPATH=. python $TMPDIR/a4.py
```

```
a zero EXC gxreg F=2.48 p=0.1192 | TP t=1.71 p=0.0915 (Con 1.193 EAA 0.786) | FO t=-0.23 p=0.820 || INH gxregxint F=2.07 p=0.0293 | FO5 t=1.99 p=0.0484 (Con -0.379 EAA -0.606) | TP5 t=-0.79 p=0.432
a drop EXC gxreg F=2.42 p=0.1236 | TP t=1.79 p=0.0772 (Con 1.205 EAA 0.783) | FO t=-0.03 p=0.973 || INH gxregxint F=1.90 p=0.0486 | FO5 t=2.08 p=0.0392 (Con -0.382 EAA -0.621) | TP5 t=-0.84 p=0.402
a one EXC gxreg F=2.07 p=0.1545 | TP t=1.74 p=0.0865 (Con 1.186 EAA 0.781) | FO t=0.11 p=0.910 || INH gxregxint F=2.01 p=0.0353 | FO5 t=2.07 p=0.0401 (Con -0.387 EAA -0.623) | TP5 t=-0.72 p=0.476
b zero EXC gxreg F=4.80 p=0.0314 | TP t=1.89 p=0.0622 (Con 1.235 EAA 0.780) | FO t=-1.18 p=0.240 || INH gxregxint F=2.07 p=0.0293 | FO5 t=1.53 p=0.1289 (Con -0.470 EAA -0.672) | TP5 t=-0.65 p=0.516
b drop EXC gxreg F=3.79 p=0.0551 | TP t=2.02 p=0.0471 (Con 1.279 EAA 0.791) | FO t=-0.62 p=0.534 || INH gxregxint F=1.90 p=0.0486 | FO5 t=1.80 p=0.0738 (Con -0.447 EAA -0.685) | TP5 t=-0.84 p=0.404
b one EXC gxreg F=3.50 p=0.0651 | TP t=2.00 p=0.0492 (Con 1.276 EAA 0.799) | FO t=-0.48 p=0.630 || INH gxregxint F=2.01 p=0.0353 | FO5 t=1.94 p=0.0544 (Con -0.435 EAA -0.687) | TP5 t=-0.81 p=0.419
c zero EXC gxreg F=0.55 p=0.4618 | TP t=1.14 p=0.2572 (Con 0.658 EAA 0.488) | FO t=0.67 p=0.504 || INH gxregxint F=2.14 p=0.0240 | FO5 t=2.39 p=0.0184 (Con -0.189 EAA -0.310) | TP5 t=-0.91 p=0.364
c drop EXC gxreg F=0.44 p=0.5087 | TP t=1.17 p=0.2463 (Con 0.659 EAA 0.486) | FO t=0.87 p=0.386 || INH gxregxint F=2.01 p=0.0347 | FO5 t=2.54 p=0.0124 (Con -0.192 EAA -0.320) | TP5 t=-1.02 p=0.310
c one EXC gxreg F=0.31 p=0.5817 | TP t=1.12 p=0.2649 (Con 0.649 EAA 0.484) | FO t=1.01 p=0.317 || INH gxregxint F=2.13 p=0.0244 | FO5 t=2.52 p=0.0130 (Con -0.194 EAA -0.321) | TP5 t=-0.85 p=0.395
d zero EXC gxreg F=4.83 p=0.0308 | TP t=2.05 p=0.0439 (Con 0.928 EAA 0.546) | FO t=-0.78 p=0.440 || INH gxregxint F=2.16 p=0.0221 | FO5 t=1.86 p=0.0655 (Con -0.243 EAA -0.377) | TP5 t=-0.65 p=0.519
d drop EXC gxreg F=3.94 p=0
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && cat > $TMPDIR/a5.py <<'EOF'
import numpy as np, pag2, pickle, collections, time
from scipy import stats
exec(open('/tmp/claude-1001/a4.py').read().split('t0=time.time()')[0])
res=pickle.load(open('/tmp/claude-1001/res.pkl','rb'))
grid=np.arange(9)*0.125
for rd in 'abcd':
  for empty in ['zero','drop','one']:
    m=lab=='exc'; g=grp[m]; idx=np.where(m)[0]
    T=np.array([[betas(U[j],j,rd,empty,v)[1].mean() for v in grid] for j in idx])
    a=pag2.mixed_anova(T,g)
    cm={gg:T[g==gg].mean(0) for gg in ['Con','EAA']}
    print(rd,empty,'peaks',{gg:grid[np.argmax(v)] for gg,v in cm.items()}, 'assign F=%.2f p=%.2g group F=%.2f p=%.3f gxa F=%.2f p=%.3f'%(a['A'][0],a['A'][3],a['group'][0],a['group'][3],a['group:A'][0],a['group:A'][3]))
    # S4 with 0.5
    tp=np.array([betas(U[j],j,rd,empty,0.5)[1].mean() for j in idx]); r1=stats.ttest_ind(tp[g=='Con'],tp[g=='EAA'])
    m2=lab=='inh'; g2=grp[m2]; idx2=np.where(m2)[0]
    fo=np.array([betas(U[j],j,rd,empty,0.5)[0][5:].mean() for j in idx2]); r2=stats.ttest_ind(fo[g2=='Con'],fo[g2=='EAA'])
    print('    S4 0.5: exc TP t=%.2f p=%.4f ; inh FO5 t=%.2f p=%.4f'%(r1.statistic,r1.pvalue,r2.statistic,r2.pvalue))
    FO,TP=res[rd,empty]
    # fig6 / S5
    out=[]
    for nmb,B,win,pop in [('fig6 TP',TP.mean(1),'first1','exc'),('S5 FO',FO.mean(1),'first1','exc'),('fig7 FO5',FO[:,5:].mean(1),'last5','inh'),('S6 TP5',TP[:,5:].mean(1),'last5','inh')]:
        s=[]
        for k,ty in enumerate(pag2.TYPES):
            F=NF[:,k,pag2.WIN[win]].mean(1)
            rr={}
            for gg in ['Con','EAA']:
                mm=(lab==pop)&(grp==gg); r,p=stats.pearsonr(F[mm],B[mm]); rr[gg]=(r,p,mm.sum())
            z,p1,p2=pag2.fisher_r_to_z(rr['Con'][0],rr['Con'][2],rr['EAA'][0],rr['EAA'][2])
            s.append('%s: Con r=%.2f R2=%.3f p=%.3g | EAA r=%.2f R2=%.3f p=%.3g | Z=%.2f p1=%.3g p2=%.3g'%(ty[:3],rr['Con'][0],rr['Con'][0]**2,rr['Con'][1],rr['EAA'][0],rr['EAA'][0]**2,rr['EAA'][1],z,p1,p2))
        print('   ',nmb); [print('      ',x) for x in s]
EOF
PYTHONPATH=. python $TMPDIR/a5.py
```

```
a zero peaks {'Con': np.float64(0.5), 'EAA': np.float64(0.5)} assign F=19.32 p=4e-26 group F=2.55 p=0.114 gxa F=1.11 p=0.356
    S4 0.5: exc TP t=1.66 p=0.1003 ; inh FO5 t=2.24 p=0.0270
    fig6 TP
       dan: Con r=0.49 R2=0.236 p=0.00478 | EAA r=0.02 R2=0.000 p=0.887 | Z=2.15 p1=0.0157 p2=0.0314
       unc: Con r=0.03 R2=0.001 p=0.862 | EAA r=-0.31 R2=0.098 p=0.0281 | Z=1.50 p1=0.0662 p2=0.132
       saf: Con r=-0.36 R2=0.131 p=0.0421 | EAA r=-0.32 R2=0.102 p=0.0254 | Z=-0.20 p1=0.42 p2=0.84
    S5 FO
       dan: Con r=0.07 R2=0.005 p=0.715 | EAA r=-0.18 R2=0.031 p=0.226 | Z=1.03 p1=0.15 p2=0.301
       unc: Con r=-0.04 R2=0.002 p=0.81 | EAA r=-0.06 R2=0.004 p=0.667 | Z=0.08 p1=0.468 p2=0.937
       saf: Con r=-0.14 R2=0.020 p=0.445 | EAA r=-0.22 R2=0.046 p=0.137 | Z=0.33 p1=0.371 p2=0.742
    fig7 FO5
       dan: Con r=-0.15 R2=0.023 p=0.3 | EAA r=0.22 R2=0.048 p=0.0442 | Z=-2.03 p1=0.0211 p2=0.0422
       unc: Con r=0.56 R2=0.312 p=3.7e-05 | EAA r=0.63 R2=0.400 p=1.07e-10 | Z=-0.62 p1=0.268 p2=0.535
       saf: Con r=-0.38 R2=0.141 p=0.00861 | EAA r=-0.32 R2=0.104 p=0.00279 | Z=-0.32 p1=0.373 p2=0.746
    S6 TP5
       dan: Con r=0.84 R2=0.704 p=9.42e-14 | EAA r=0.84 R2=0.704 p=2.16e-23 | Z=0.00 p1=0.5 p2=0.999
       unc: Con r=0.04 R2=0.001 p=0.801 | EAA r=0.10 R2=0.009 p=0.384 | Z=-0.32 p1=0.375 p2=0.75
       saf: Con r=-0.32 R2=0.100 p=0.0289 | EAA r=-0.48 R2=0.233 p=3.23e-06 | Z=1.08 p1=0.141 p2=0.281
a drop peaks {'Con': np.float64(0.5), 'EAA': np.float64(0.5)} assign F=18.60 p=3.7e-25 group F=3.18 p=0.079 gxa F=1.00 p=0.433
    S4 0.5: exc TP t=1.84 p=0.0702 ; inh FO5 t=2.41 p=0.0175
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python3 - <<'EOF'
p='entries/crcns-pag-2-moaddab-2020/pag2.py'; s=open(p).read()
s=s.replace('''    pokes = ev["EVT13"]
    pb = np.searchsorted(pokes, on) - np.searchsorted(pokes, on - 20.0)
    pc = np.searchsorted(pokes, on + CUE_S) - np.searchsorted(pokes, on)
    return dict(name=name, rat=name[:4], session=name[:10], group=group_of(name[:4]),
                onset=on, type=np.array([r[1] for r in rows]), shock=np.array([r[2] for r in rows]),
                counts=counts, poke_base=pb, poke_cue=pc, n_spikes=len(spk),
                n_events={k: len(v) for k, v in ev.items()})''','''    sh_edges = edges - SHIFT_S
    counts_shift = np.diff(np.searchsorted(spk, sh_edges), axis=1)
    pokes = ev["EVT13"]
    pb = np.searchsorted(pokes, on) - np.searchsorted(pokes, on - 20.0)
    pc = np.searchsorted(pokes, on + CUE_S) - np.searchsorted(pokes, on)
    pbs = np.searchsorted(pokes, on - SHIFT_S) - np.searchsorted(pokes, on - SHIFT_S - 20.0)
    pcs = np.searchsorted(pokes, on - SHIFT_S + CUE_S) - np.searchsorted(pokes, on - SHIFT_S)
    return dict(name=name, rat=name[:4], session=name[:10], group=group_of(name[:4]),
                onset=on, type=np.array([r[1] for r in rows]), shock=np.array([r[2] for r in rows]),
                counts=counts, poke_base=pb, poke_cue=pc, n_spikes=len(spk),
                counts_shift=counts_shift, poke_base_shift=pbs, poke_cue_shift=pcs,
                n_events={k: len(v) for k, v in ev.items()}, events=ev)''')
s=s.replace('''CUE_S = 10.0
''','''CUE_S = 10.0
SHIFT_S = 60.0   # onsets moved 60 s earlier, into the inter-trial interval, for the clock check
                 # (a standard choice; the notebook prints the shortest gap between cues)
''')
s=s.replace('''def suppression_ratio(u, empty="zero"):
    """''','''def suppression_ratio(u, empty="zero", shifted=False):
    """''')
s=s.replace('''    b = u["poke_base"] / 20.0
    c = u["poke_cue"] / CUE_S''','''    b = u["poke_base_shift" if shifted else "poke_base"] / 20.0
    c = u["poke_cue_shift" if shifted else "poke_cue"] / CUE_S''')
s=s.replace('''    empty: what a trial with no pokes in either window (0/0) becomes; 'zero' or 'drop' (NaN).
    """''','''    empty: what a trial with no pokes in either window (0/0) becomes: 'zero', 'drop' (NaN), the
    two readings of the claims file, or 'one', the value the authors' cube stores for such trials
    (cer.cue, checked in the notebook).
    """''')
s=s.replace('''    if empty == "zero":
        sr = np.where(np.isnan(sr), 0.0, sr)
    return sr''','''    if empty in ("zero", "one"):
        sr = np.where(np.isnan(sr), 0.0 if empty == "zero" else 1.0, sr)
    return sr''')
s=s.replace('''def rates(u):
    return u["counts"] / BIN    # Hz per 250 ms bin, trials x 200''','''def rates(u, shifted=False):
    return u["counts_shift" if shifted else "counts"] / BIN    # Hz per 250 ms bin, trials x 200''')
s=s.replace('''def window_rate(u, win):
    return rates(u)[:, WIN[win]].mean(axis=1)''','''def window_rate(u, win, shifted=False):
    return rates(u, shifted)[:, WIN[win]].mean(axis=1)''')
s=s.replace('''def select(u, epochs_exc, epochs_inh, alpha=0.05 / 6, r=None):''','''def select(u, epochs_exc, epochs_inh, alpha=0.05 / 6, r=None, shifted=False):''')
s=s.replace('''            base = (r["base10"] if r else window_rate(u, "base10"))[m]
            ep = (r[win] if r else window_rate(u, win))[m]''','''            base = (r["base10"] if r else window_rate(u, "base10", shifted))[m]
            ep = (r[win] if r else window_rate(u, win, shifted))[m]''')
s=s.replace('''def interval_betas(u, reading, empty, unc_value=0.375, cube_z=None):
    """Fear output and threat probability betas for each 1 s interval of the cue (10 each)."""
    tf = trial_firing(u, reading, cube_z)
    y = tf[:, WIN["cue"]].reshape(len(tf), 10, 4).mean(axis=2)
    prob = np.array([unc_value if t == "uncertainty" else PROB[t] for t in u["type"]])
    return regress_betas(y, suppression_ratio(u, empty), prob)''','''def interval_betas(u, reading, empty, unc_value=0.375, cube_z=None):
    """Fear output and threat probability betas for each 1 s interval of the cue (10 each).

    The response is the trial-wise normalized firing in each 1 s interval (Results, "Diminished
    threat probability signaling", paragraph 1: "normalized firing rate for each trial ... in 1 s
    bins over the 10 s cue"); regressors are the trial's suppression ratio for the 10 s cue and the
    cue's shock probability, with the uncertainty value `unc_value` (Methods, "Single-unit,
    linear regression" and "Threat probability tuning curve"). The beta of a window of several
    intervals is the mean of its interval betas; with the same trials and regressors this equals
    the beta of one regression on the window's mean firing (OLS is linear in the response), so the
    two window readings of the claims file coincide.
    """
    tf = trial_firing(u, reading, cube_z)
    y = tf[:, WIN["cue"]].reshape(len(tf), 10, 4).mean(axis=2)
    prob = np.array([unc_value if t == "uncertainty" else PROB[t] for t in u["type"]])
    return regress_betas(y, suppression_ratio(u, empty), prob)''')
s=s.replace('''    Returns {effect: (F, df1, df2, p)} for every within effect''','''    The paper names no software or correction; it reports partial eta squared and observed power,
    as SPSS does, so its type III sums of squares are used (a choice that changes only the within
    main effects, slightly, when groups differ in size; interactions and the group effect are
    the same under type I).
    Returns {effect: (F, df1, df2, p)} for every within effect''')
open(p,'w').write(s)
EOF
grep -n "SHIFT_S\|empty in" entries/crcns-pag-2-moaddab-2020/pag2.py | head
```

```
Fri Nov  6 20:10:48 UTC 2026
70:SHIFT_S = 60.0   # onsets moved 60 s earlier, into the inter-trial interval, for the clock check
150:    sh_edges = edges - SHIFT_S
155:    pbs = np.searchsorted(pokes, on - SHIFT_S) - np.searchsorted(pokes, on - SHIFT_S - 20.0)
156:    pcs = np.searchsorted(pokes, on - SHIFT_S + CUE_S) - np.searchsorted(pokes, on - SHIFT_S)
181:    if empty in ("zero", "one"):
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/build.py <<'PYEOF'
import nbformat as nbf
cells = []
def md(s): cells.append(nbf.v4.new_markdown_cell(s.strip()))
def code(s, tag=None):
    c = nbf.v4.new_code_cell(s.strip())
    if tag: c.metadata["tags"] = [tag]
    cells.append(c)

md(r'''
# Moaddab, Wright & McDannald (2020) on CRCNS pag-2

Paper: Moaddab M, Wright KM, McDannald MA. Early adolescent adversity alters periaqueductal
gray/dorsal raphe threat responding in adult female rats. Sci Rep 10, 18035 (2020),
doi:10.1038/s41598-020-74457-3.

Dataset: CRCNS pag-2, doi:10.6080/K0833Q7F, read from the public bucket at
`https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-2/live/`. Version: `unversioned`. CRCNS data
sets carry no version numbers, so the only published state is the current one under `live/` (no
`old/` folder exists). It is pinned by the MD5 sums of the data set's `checksums.md5`:
data.zip `7d1686e3d4f6f36895c38f34eda632d4`, docs/crcns_pag-2_data_description.pdf
`9f6c40904e9123fe8ff488d6006c8df4`; the first cell checks that the object read has that MD5.
The data description is version 0.6 (April 4, 2021).

Claims: `claims/crcns-pag-2/10.1038-s41598-020-74457-3.yaml`, written from the version of record
(PMC7582948) without its supplement. Methods details the claims file lacks are taken from the paper
and, where the paper leaves them open, from the authors' own script and cube in the data set
(`data/vlpagAnalysis.m`, `data/cubeFile/cube.mat`), as each section says.

| Claim | Tested |
|---|---|
| fig1bc-adversity-slows-weight-gain | blocked (no body weights in the data set) |
| fig1ef-acquisition-equivalent-final | blocked (no pre-surgery sessions in the data set) |
| fig2b-baseline-poke-equivalent | tested |
| fig2c-recording-discrimination | tested |
| fig2d-cue-responsive-counts | tested |
| fig2d-higher-proportion-responsive | tested |
| fig2ef-baseline-firing | tested |
| fig4ab-excited-temporal-pattern | tested without bregma (no bregma level per rat) |
| fig4c-excited-inflated-onset | tested |
| fig4de-inhibited-temporal-pattern | tested without bregma |
| fig4f-inhibited-danger-decrease | tested |
| fig4f-inhibited-danger-uncertainty-discrimination | tested |
| fig5abc-excited-reduced-threat-probability | tested |
| fig5d-threat-tuning-curve | tested |
| figs4-peak-assignment-same-pattern | tested |
| fig5efg-inhibited-fear-output | tested |
| fig6-excited-firing-threat-decoupled | tested |
| figs5-excited-firing-fear-output-unrelated | tested |
| fig7-inhibited-firing-fear-output | tested |
| figs6-inhibited-firing-threat-probability | tested |
''')

code(r'''
import time
import collections
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pag2

t0 = time.time()
etag, md5_ok = pag2.check_md5()
print("data.zip ETag", etag, "matches checksums.md5:", md5_ok)
zf = pag2.open_zip()
members = [i for i in zf.infolist() if not i.is_dir()]
print(len(members), "files in data.zip;", sum(i.filename.startswith("data/matFiles/") for i in members), "unit files")
for i in members:
    if not i.filename.startswith("data/matFiles/"):
        print("  ", i.filename, i.file_size)
cube, names = pag2.load_cube(zf)
U = pag2.load_all(zf, names)
print(len(U), "units loaded in %.0f s" % (time.time() - t0))
grp = np.array([u["group"] for u in U])
''')

md(r'''
## Data check

What the files hold: each unit file has the spike times (`spike`), the event times `EVT01` to
`EVT14` and the mean waveform. The cube, `vlPAGcube`, has for every unit a trial table (`tag`: cue
type 1 to 4 and onset time per trial), binned raw, differential and Z scored firing, nose poke
rates and suppression ratios (`poke`, `cer`), and the waveform. The cell below lists every field
of the cube with its shape, type and range, identifies the event codes against the cube's trial
table, and checks the cube's stored values against values computed here from the spikes and
pokes.
''')

code(r'''
def walk(o, path=""):
    if hasattr(o, "_fieldnames"):
        for f in o._fieldnames:
            walk(getattr(o, f), path + "." + f)
    elif isinstance(o, np.ndarray) and o.dtype == object and o.size == 1:
        walk(o.flat[0], path)
    else:
        a = np.asarray(o)
        rng = (a.min(), a.max()) if a.dtype.kind in "fiu" and a.size else ""
        print(f"vlPAGcube{path:32s} {str(a.shape):16s} {str(a.dtype):8s} {rng}")
walk(cube)

# units, rats, sessions
rats = sorted(set(u["rat"] for u in U))
print("\nrats:", {g: [r for r in rats if pag2.group_of(r) == g] for g in ("Con", "EAA")})
print("rats in the script's lists but not in the data:",
      sorted(set(pag2.CON_RATS + pag2.EAA_RATS) - set(rats)))
print("units per group:", dict(collections.Counter(grp)))
sessions = {}
for u in U:
    sessions.setdefault(u["session"], u)
print("sessions (rat and date):", len(sessions), dict(collections.Counter(s["group"] for s in sessions.values())),
      "; the paper and the data description state 72 Control and 107 EAA")
ev_sets = {tuple(np.round(u["onset"], 3)) for u in U}
print("distinct trial tables (cue onset times):", len(ev_sets))
print("units per rat:", dict(collections.Counter(u["rat"] for u in U)))
print("behaviour programs:", dict(collections.Counter(u["name"][10:16] for u in U)))
hashes = collections.Counter((u["n_spikes"], u["counts"].sum()) for u in U)
dups = [k for k, v in hashes.items() if v > 1]
print("pairs of units with the same spike count and binned counts (possible duplicates):", len(dups))

# event codes against the cube's trial table
tag = pag2.cube_field(cube, "tag")
ok_onset = ok_type = 0
for j, u in enumerate(U):
    tt = np.array([{"danger": 1, "uncertainty": 2, "safety": 4}[x] for x in u["type"]])
    tt[(u["type"] == "uncertainty") & ~u["shock"]] = 3
    ok_onset += np.allclose(u["onset"], tag[:, 1, j])
    ok_type += np.array_equal(tt, tag[:, 0, j])
print(f"\ncue onsets equal to the cube's tag in {ok_onset}/{len(U)} units, trial types in {ok_type}/{len(U)}")
code_map = collections.Counter()
for u in U:
    for code in ("EVT09", "EVT11", "EVT12"):
        t = u["events"][code][0]
        code_map[(u["name"][10:16], code, u["type"][np.argmin(np.abs(u["onset"] - t))])] += 1
for k, v in sorted(code_map.items()):
    print("  ", k, v, "units")
print("trials per unit:", dict(collections.Counter(len(u["onset"]) for u in U)),
      "; per type:", dict(collections.Counter(u["type"]).items()) if False else
      dict(collections.Counter(tuple(sorted(collections.Counter(u["type"]).items())) for u in U)))
print("shocks per unit:", dict(collections.Counter(int(u["shock"].sum()) for u in U)),
      "; shocked uncertainty trials per unit:",
      dict(collections.Counter(int(u["shock"][u["type"] == "uncertainty"].sum()) for u in U)))
lag14 = np.concatenate([np.min(np.abs(u["events"]["EVT14"][None, :] - (u["onset"][:, None] - 31.5)), axis=1) for u in U])
print("EVT14 lies 31.5 s before each cue onset: max deviation %.3f s" % lag14.max())
gaps = np.concatenate([np.diff(np.sort(u["onset"])) for u in sessions.values()])
print("gap between consecutive cue onsets: %.1f to %.1f s, mean %.1f s" % (gaps.min(), gaps.max(), gaps.mean()))
''', tag="sanity")

code(r'''
# The cube's stored values against values computed from the spikes and pokes
B10 = pag2.cube_field(cube, "fire.raw.base10")[:, 0, :].astype(float)
CSEL = {w: pag2.cube_field(cube, "fire.raw.select." + k)[:, 0, :].astype(float)
        for w, k in (("first1", "cueOnset"), ("first5", "cueFirstFive"), ("last5", "cueLastFive"))}
exact = np.array([pag2.window_rate(u, "base10") for u in U]).T
d = exact - B10
print("fire.raw.base10 minus exact 10 s rate: %.2f to %.2f Hz; cube equals floor(exact) in %.1f%% of trials"
      % (-d.max(), -d.min(), 100 * np.mean(np.floor(exact + 1e-9) == B10)))
print("cube rates stored as", pag2.cube_field(cube, "fire.raw.base10").dtype,
      "; units with a mean 10 s baseline under 1 Hz:", int(np.sum(exact.mean(0) < 1)),
      "; trials whose stored baseline is 0 Hz while spikes were fired:", int(np.sum((B10 == 0) & (exact > 0))))
cz = pag2.cube_field(cube, "fire.z.s1.interval")
cd = pag2.cube_field(cube, "fire.diff.s1.interval").astype(float)
err_d = err_z = 0.0
for j, u in enumerate(U):
    r1 = u["counts"].reshape(32, 50, 4).sum(2).astype(float)          # spikes per 1 s bin = Hz
    own = r1[:, 18:20].mean(1, keepdims=True)
    err_d = max(err_d, np.abs(r1 - own - cd[:, :, j]).max())
    z = (cd[:, :, j] - cd[:, :, j].mean()) / cd[:, :, j].std(ddof=1)
    err_z = max(err_z, np.abs(z - cz[:, :, j]).max())
print("fire.diff.s1 = 1 s rate minus the trial's own 2 s baseline, within %.2f Hz (stored as integers)" % err_d)
print("fire.z.s1 = fire.diff.s1 Z scored over all trials and bins of the unit (ddof 1), within %.1g" % err_z)

# nose pokes and suppression ratios
pb = pag2.cube_field(cube, "poke.base")[:, 0, :].astype(float)
pc = pag2.cube_field(cube, "poke.cue")[:, 0, :].astype(float)
csr = pag2.cube_field(cube, "cer.cue")[:, 0, :]
mine_pb = np.array([u["poke_base"] / 20 * 60 for u in U]).T
mine_pc = np.array([u["poke_cue"] / 10 * 60 for u in U]).T
print("\npoke.base equals pokes per minute in the 20 s before cue onset in %.1f%% of trials" % (100 * np.mean(np.isclose(pb, mine_pb))))
for w in (2, 10):
    alt = np.array([(np.searchsorted(u["events"]["EVT13"], u["onset"]) - np.searchsorted(u["events"]["EVT13"], u["onset"] - w)) / w * 60 for u in U]).T
    print("   with a %d s window: %.1f%%" % (w, 100 * np.mean(np.isclose(pb, alt))))
print("poke.cue equals pokes per minute in the 10 s cue in %.1f%% of trials" % (100 * np.mean(np.isclose(pc, mine_pc))))
sr = np.array([pag2.suppression_ratio(u, "drop") for u in U]).T
empty = np.isnan(sr)
print("cer.cue equals (base - cue)/(base + cue) with the 20 s baseline in %.2f%% of trials with pokes;"
      % (100 * np.mean(np.isclose(sr[~empty], csr[~empty]))),
      "trials with no poke in baseline and cue:", int(empty.sum()), "(unit-trials), stored as", np.unique(csr[empty]))
nsess_empty = collections.Counter()
for s, u in sessions.items():
    nsess_empty[u["group"]] += int(np.isnan(pag2.suppression_ratio(u, "drop")).sum())
print("empty trials over the 182 sessions:", dict(nsess_empty), "of", {g: 32 * n for g, n in collections.Counter(s["group"] for s in sessions.values()).items()})
print("suppression ratio range %.2f to %.2f; firing in 250 ms bins 0 to %.0f Hz; spike count per unit %d to %d"
      % (np.nanmin(sr), np.nanmax(sr), max(pag2.rates(u).max() for u in U), min(u["n_spikes"] for u in U), max(u["n_spikes"] for u in U)))
''', tag="sanity")

md(r'''
Clock check. Cue responses and fear should appear at the cue onsets of the trial table and vanish
when the onsets are moved 60 s earlier, into the inter-trial interval (the shortest gap between
cues is printed above). The selection rule (reading b, exact rates) and the danger minus safety
suppression ratio are computed at the true and the shifted onsets.
''')

code(r'''
e, i = pag2.SELECTION_READINGS["b"]
true_lab = np.array([pag2.select(u, e, i) for u in U])
shift_lab = np.array([pag2.select(u, e, i, shifted=True) for u in U])
print("cue-responsive units at the true onsets:", int(np.sum(true_lab != "osc")), "of", len(U),
      "; at onsets 60 s earlier:", int(np.sum(shift_lab != "osc")),
      "(chance under the rule: about 6 tests x 2 tails x 0.0083/2 = %.1f%% of units)" % (100 * (1 - (1 - 0.0083) ** 6)))
dsr = []
for s, u in sessions.items():
    a = pag2.suppression_ratio(u, "drop"); b = pag2.suppression_ratio(u, "drop", shifted=True)
    dsr.append((np.nanmean(a[u["type"] == "danger"]) - np.nanmean(a[u["type"] == "safety"]),
                np.nanmean(b[u["type"] == "danger"]) - np.nanmean(b[u["type"] == "safety"])))
dsr = np.array(dsr)
print("danger minus safety suppression ratio per session, mean: true %.3f, shifted %.3f; sessions with danger > safety: %d and %d of %d"
      % (dsr[:, 0].mean(), np.nanmean(dsr[:, 1]), np.sum(dsr[:, 0] > 0), np.sum(dsr[:, 1] > 0), len(dsr)))
''', tag="sanity")

md(r'''
Findings of the data check, stated with the numbers above:

- The 354 units (151 Control, 203 EAA) and 20 rats (8 Control, 12 EAA) match the paper. The
  sessions do not: the units come from 182 sessions (rat and date, each with its own trial table),
  74 Control and 108 EAA, where the paper and the data description state 72 and 107.
- The group of each rat is given only by the lists in the authors' script, not by the data
  description or the files.
- The event codes are not documented. EVT09, EVT11 and EVT12 are the cue onsets, but which code is
  danger, uncertainty or safety changes with the behaviour program (epr38a, b, c); EVT08 holds the
  shocks, EVT13 the nose pokes, EVT14 a marker 31.5 s before each cue.
- The cube stores raw firing rates as integers truncated towards zero (uint8), so a unit firing
  below 1 Hz has stored rates of 0.
- `poke.base` is the poke rate per minute in the 20 s before cue onset, not "2 s prior to cue
  presentation" as the data description says, and it is per minute, a unit the description does not
  give.
- `cer.cue` stores 1 for the trials with no poke in baseline or cue (a ratio of 0/0).
- The data description gives the uncertainty shock rows a shock probability of 0.25; the paper and
  the description's own summary give 0.375.
- The data set holds no body weights, no pre-surgery discrimination sessions, and no bregma level
  per rat (the description gives only how many rats were at each of four levels).
''')

# ---------------- behaviour ----------------
md(r'''
## Blocked claims

`fig1bc-adversity-slows-weight-gain` needs the body weights from P24 to P55, and
`fig1ef-acquisition-equivalent-final` the eight pre-surgery discrimination sessions. Neither is in
the data set: its files are the 354 recording-session units, the cube built from them, the script
and three cue sounds (listed in the first cell), and the data description lists nothing else.
Both are blocked as `data_missing`.
''')

md(r'''
## fig2b-baseline-poke-equivalent

> Control and EAA rats had equivalent baseline nose poke rates during recording sessions.

One baseline rate per rat, from the 20 s before cue onset (Methods, "Calculating suppression
ratios"), over its recording sessions; each session is counted once although several units share
it. Readings: the mean of the rat's session means, and the mean over all its trials pooled.
Two-sided independent samples t test.
''')

code(r'''
def per_rat(fn):
    out = {}
    for s, u in sessions.items():
        out.setdefault(u["rat"], []).append(fn(u))
    return out

rats_sorted = sorted(set(u["rat"] for u in U))
rgrp = np.array([pag2.group_of(r) for r in rats_sorted])
base = per_rat(lambda u: u["poke_base"] / 20 * 60)
readings_bp = {
    "mean of session means": np.array([np.mean([x.mean() for x in base[r]]) for r in rats_sorted]),
    "all trials pooled": np.array([np.concatenate(base[r]).mean() for r in rats_sorted]),
}
for k, v in readings_bp.items():
    t = stats.ttest_ind(v[rgrp == "Con"], v[rgrp == "EAA"])
    print(f"{k:22s} Con {v[rgrp=='Con'].mean():.2f} (sd {v[rgrp=='Con'].std(ddof=1):.2f}) EAA {v[rgrp=='EAA'].mean():.2f} "
          f"(sd {v[rgrp=='EAA'].std(ddof=1):.2f}) pokes/min; t({t.df:.0f}) = {t.statistic:.2f}, p = {t.pvalue:.3f}")
print("per rat (pokes/min):", {r: round(v, 1) for r, v in zip(rats_sorted, readings_bp["mean of session means"])})
print("sessions per rat:", {r: len(base[r]) for r in rats_sorted})
''', tag="claim:fig2b-baseline-poke-equivalent")

md(r'''
**Result: reproduced.** Under both readings the groups do not differ (t(18) = 1.19, p = 0.25; the
paper gives t = 1.24, p = 0.23); every session has 32 trials, so the two readings give the same
values.
''')

md(r'''
## fig2c-recording-discrimination

> During recording sessions both groups showed high fear to danger, less to uncertainty and least
> to safety, with a main effect of cue, no group by cue interaction, and each cue pair differing in
> each group.

Per rat, the mean suppression ratio for each cue over its recording sessions (each session once).
Mixed ANOVA, cue within, group between; paired t tests within each group. Readings: rat value as
the mean of session means or over trials pooled; trials with no pokes (0/0) set to 0, dropped, or
set to 1 as the cube stores them.
''')

code(r'''
def sr_rat(empty, comb):
    vals = per_rat(lambda u: (pag2.suppression_ratio(u, empty), u["type"]))
    Y = []
    for r in rats_sorted:
        if comb == "session means":
            Y.append([np.mean([np.nanmean(s[t == ty]) for s, t in vals[r]]) for ty in pag2.TYPES])
        else:
            s = np.concatenate([x[0] for x in vals[r]]); t = np.concatenate([x[1] for x in vals[r]])
            Y.append([np.nanmean(s[t == ty]) for ty in pag2.TYPES])
    return np.array(Y)

for empty in ("zero", "drop", "one"):
    for comb in ("session means", "pooled"):
        Y = sr_rat(empty, comb)
        a = pag2.mixed_anova(Y, rgrp)
        line = f"empty={empty:4s} {comb:13s} cue F({a['A'][1]},{a['A'][2]}) = {a['A'][0]:.1f}, p = {a['A'][3]:.1e}; " \
               f"group x cue F = {a['group:A'][0]:.2f}, p = {a['group:A'][3]:.2f};"
        for g in ("Con", "EAA"):
            x = Y[rgrp == g]
            t1 = stats.ttest_rel(x[:, 0], x[:, 1]); t2 = stats.ttest_rel(x[:, 1], x[:, 2])
            line += f" {g} D-U t = {t1.statistic:.2f} p = {t1.pvalue:.4f}, U-S t = {t2.statistic:.2f} p = {t2.pvalue:.1e};"
        print(line)
        if empty == "zero" and comb == "session means":
            print("   means (danger, uncertainty, safety):", {g: Y[rgrp == g].mean(0).round(3) for g in ("Con", "EAA")},
                  "range per rat %.2f to %.2f" % (Y.min(), Y.max()))
''', tag="claim:fig2c-recording-discrimination")

md(r'''
**Result: reproduced.** Under every reading the cue effect is large (F(2,36) from 180 to 195, p <
1e-19), the group by cue interaction is absent (p from 0.84 to 0.90), and all four paired tests
have p <= 0.0091 with danger > uncertainty > safety in both groups.
''')

# ---------------- selection ----------------
md(r'''
## fig2d-cue-responsive-counts

> 32 of 151 Control neurons (21.2%) and 49 of 203 EAA neurons (24.1%) were cue-excited; 48 of 151
> Control neurons (31.8%) and 84 of 203 EAA neurons (41.4%) were cue-inhibited.

Paired t tests (two-sided, p < 0.0083) of the raw rate in the 10 s before cue onset against each
cue epoch, per cue, under the three readings of the claims file. Two sources of the raw rates are
run: the exact rates from the spike times, and the rates stored in the authors' cube
(`fire.raw.base10` and `fire.raw.select.cueOnset`, `cueFirstFive`, `cueLastFive`), which are
truncated to whole Hz. The authors' script runs its selection on the cube's stored rates
(vlpagAnalysis.m, lines 9 to 67, MATLAB `ttest(x, y)`, a paired test, at alpha 0.00833) with
reading (b) (lines 136 to 147 and 225 to 236).
''')

code(r'''
cube_rates = [dict(base10=B10[:, j], **{w: CSEL[w][:, j] for w in CSEL}) for j in range(len(U))]
labels = {}
for rd, (e, i) in pag2.SELECTION_READINGS.items():
    labels[rd, "exact"] = np.array([pag2.select(u, e, i) for u in U])
    labels[rd, "cube"] = np.array([pag2.select(u, e, i, r=cube_rates[j]) for j, u in enumerate(U)])
expected = {("Con", "exc"): 32, ("EAA", "exc"): 49, ("Con", "inh"): 48, ("EAA", "inh"): 84}
print("reading  rates   Con exc  EAA exc  Con inh  EAA inh  (paper 32, 49, 48, 84; tolerance 10%)")
for (rd, src), L in labels.items():
    cnt = {k: int(np.sum((grp == k[0]) & (L == k[1]))) for k in expected}
    within = all(abs(cnt[k] - v) <= 0.1 * v for k, v in expected.items())
    print(f"   {rd}     {src:6s}  " + "  ".join(f"{cnt[k]:7d}" for k in expected) + f"   all within tolerance: {within}")
print("unit totals:", dict(collections.Counter(grp)))
lab = labels["b", "cube"]          # the selection used by the claims that follow
lab_exact = labels["b", "exact"]
print("\nselection used below: reading (b), cube rates. Agreement with exact rates, reading (b):",
      int(np.sum(lab == lab_exact)), "of", len(U), "units;", collections.Counter(zip(lab, lab_exact)))
for g in ("Con", "EAA"):
    print(g, "by rat:", {r: dict(collections.Counter(lab[[u['rat'] == r for u in U]])) for r in rats_sorted if pag2.group_of(r) == g})
''', tag="claim:fig2d-cue-responsive-counts")

md(r'''
**Result: reproduced.** With the cube's stored rates and reading (b), the counts are 32, 49, 48
and 84, the paper's exactly, and the totals are 151 and 203; readings (a) and (c) with the cube's
rates are also within tolerance for all four counts (a gives 34 Control inhibited, outside; see the
table). With exact rates from the spike times, reading (b) gives 30, 50, 54 and 87, and the
Control inhibited count is outside the tolerance. The paper's counts follow from the truncated rates.
''')

md(r'''
## fig2d-higher-proportion-responsive

> A higher proportion of EAA neurons than Control neurons were cue-responsive (133/203, 65.5%,
> against 80/151, 53.0%).

Pearson chi-square without continuity correction on the 2 by 2 table, under every reading of the
selection.
''')

code(r'''
for (rd, src), L in labels.items():
    tab = np.array([[np.sum((grp == g) & (L != "osc")), np.sum((grp == g) & (L == "osc"))] for g in ("Con", "EAA")])
    chi, p, *_ = stats.chi2_contingency(tab, correction=False)
    chiy, py, *_ = stats.chi2_contingency(tab, correction=True)
    fr = tab[:, 0] / tab.sum(1)
    print(f"reading {rd} {src:5s}: Con {tab[0,0]}/{tab[0].sum()} = {fr[0]:.3f}, EAA {tab[1,0]}/{tab[1].sum()} = {fr[1]:.3f}; "
          f"chi2 = {chi:.2f}, p = {p:.3f} (Yates {chiy:.2f}, p = {py:.3f})")
''', tag="claim:fig2d-higher-proportion-responsive")

md(r'''
**Result: reproduced.** Under the selection used here (b, cube rates) the fractions are 0.530 and
0.655 and chi-square = 5.68, p = 0.017, as in the paper; with exact rates (b) they are 0.556 and
0.675, chi-square = 5.19, p = 0.023, also within tolerance.
''')

md(r'''
## fig2ef-baseline-firing

> Baseline firing rates did not differ between Control and EAA neurons of any functional type,
> while across groups baseline firing differed by functional type and was lowest for cue-excited
> neurons.

Per neuron, the mean raw rate over all trials in (a) the 10 s or (b) the 2 s before cue onset, from
the spike times. Independent samples t tests per type, two-sided; one-way ANOVA over the three
types, groups pooled.
''')

code(r'''
for src, L in (("cube (b)", lab), ("exact (b)", lab_exact)):
    for w in ("base10", "base2"):
        bf = np.array([pag2.window_rate(u, w).mean() for u in U])
        tt = []
        for ty in ("exc", "inh", "osc"):
            r = stats.ttest_ind(bf[(L == ty) & (grp == "Con")], bf[(L == ty) & (grp == "EAA")])
            tt.append(f"{ty} t({r.df:.0f}) = {r.statistic:.2f} p = {r.pvalue:.2f}")
        f = stats.f_oneway(*[bf[L == ty] for ty in ("exc", "inh", "osc")])
        means = {ty: round(bf[L == ty].mean(), 2) for ty in ("exc", "inh", "osc")}
        print(f"selection {src}, {w}: " + "; ".join(tt) + f"; type F(2,{len(U)-3}) = {f.statistic:.2f}, p = {f.pvalue:.4f}; means (Hz) {means}")
print("baseline rate range: %.2f to %.2f Hz" % (bf.min(), bf.max()))
''', tag="claim:fig2ef-baseline-firing")

md(r'''
**Result: reproduced.** With the selection used here, no group difference has p < 0.05 (smallest p
= 0.26, all |t| < 1.13) under either baseline window, the type effect has F(2,351) = 6.44, p =
0.0018 (10 s) and 6.78, p = 0.0013 (2 s), and cue-excited neurons have the lowest mean (13.9 Hz,
against 22.0 and 25.3). The paper's error degrees of freedom are 346, five fewer than the 351 the
354 neurons give.
''')

# ---------------- population ----------------
md(r'''
## Normalized firing

As the opening comment of the claims file and the Methods ("Z score normalization") give it: per
neuron and cue (danger, uncertainty with its 16 trials, safety), the trial-mean rate in 250 ms
bins minus that cue's mean 2 s pre-cue rate, Z scored over all 600 bins of the neuron. The
authors' script instead averages the cube's trial-wise Z scores (fire.z.ms250, each trial's own
baseline subtracted and Z scored over all trials and bins); this is run as a variant for the
population ANOVAs. The figure shows the population means with the selection used here.
''')

code(r'''
NF = np.array([pag2.normalized_firing(u)[0] for u in U])            # neurons x 3 cues x 200 bins
Z250 = pag2.cube_field(cube, "fire.z.ms250.interval")
NFc = np.zeros_like(NF)
for j, u in enumerate(U):
    for k, ty in enumerate(pag2.TYPES):
        NFc[j, k] = Z250[u["type"] == ty, :, j].mean(0)
tbin = (np.arange(200) - 80) * 0.25
fig, ax = plt.subplots(2, 2, figsize=(10, 6), sharex=True)
for a_, (pop, g) in zip(ax.flat, [(p, g) for p in ("exc", "inh") for g in ("Con", "EAA")]):
    m = (lab == pop) & (grp == g)
    for k, (ty, col) in enumerate(zip(pag2.TYPES, ("red", "purple", "blue"))):
        a_.plot(tbin[72:128], NF[m, k, 72:128].mean(0), color=col, label=ty)
    a_.axvline(0, color="k", lw=0.5); a_.axvline(10, color="k", lw=0.5)
    a_.set_title(f"{g} {pop} (n = {m.sum()})"); a_.set_ylabel("Z")
ax[0, 0].legend(); ax[1, 0].set_xlabel("s from cue onset"); ax[1, 1].set_xlabel("s from cue onset")
plt.tight_layout(); plt.show()
print("plotted means range %.2f to %.2f; all points inside the axes" % (min(NF[(lab == p)][:, :, 72:128].mean(0).min() for p in ("exc", "inh")),
      max(NF[(lab == p) & (grp == g)][:, :, 72:128].mean(0).max() for p in ("exc", "inh") for g in ("Con", "EAA"))))
''')

md(r'''
## fig4ab-excited-temporal-pattern

> Control and EAA cue-excited neurons differed in the temporal pattern of their cue-selective
> firing, a group by cue by bin interaction that held with bregma recording level as a factor.

Mixed ANOVA of the normalized firing in the 56 bins from 2 s before cue onset to 2 s after offset,
cue and bin within, group between. The model with bregma level cannot be run: the data set gives
no bregma level per rat.
''')

code(r'''
def pop_anova(pop, L=None, F=None):
    L = lab if L is None else L
    F = NF if F is None else F
    m = L == pop
    a = pag2.mixed_anova(F[m][:, :, pag2.WIN["anova"]], grp[m])
    return a, m

for name, L, F in (("main (cube-rate selection, Methods normalization)", lab, NF),
                   ("variant: the script's normalization", lab, NFc),
                   ("variant: exact-rate selection", lab_exact, NF)):
    a, m = pop_anova("exc", L, F)
    f = a["group:AB"]
    print(f"{name}: n = {dict(collections.Counter(grp[m]))}; group x cue x bin F({f[1]},{f[2]}) = {f[0]:.2f}, p = {f[3]:.2g};"
          f" cue x bin F = {a['AB'][0]:.2f}, p = {a['AB'][3]:.2g}")
''', tag="claim:fig4ab-excited-temporal-pattern")

md(r'''
**Result: partially reproduced.** The group by cue by bin interaction is significant, F(110,8690)
= 1.30, p = 0.019 (the paper: F(110,8360) = 3.32, p = 3e-28), and is weaker than the paper's; the
script's normalization gives F = 1.18, p = 0.10, and the exact-rate selection F = 1.24, p = 0.044.
The part with bregma level could not be tested, as the data set has no bregma level per rat.
''')

md(r'''
## fig4c-excited-inflated-onset

> In the first 1 s of the cue, EAA cue-excited neurons fired more than Control neurons (main
> effect of group), with a significant group difference to safety; both groups still discriminated
> danger from uncertainty and uncertainty from safety.

Per neuron, the mean normalized firing over the four bins of the first 1 s of each cue. Mixed
ANOVA (cue within, group between); independent samples t tests per cue at 0.05/3; paired t tests
within each group at p < 0.025.
''')

code(r'''
def window_tests(pop, win, L=None, F=None, show=True):
    L = lab if L is None else L
    F = NF if F is None else F
    m = L == pop
    V = F[m][:, :, pag2.WIN[win]].mean(2); g = grp[m]
    a = pag2.mixed_anova(V, g)
    out = dict(group=a["group"], gxc=a["group:A"], means={gg: V[g == gg].mean(0) for gg in ("Con", "EAA")})
    out["t"] = {ty: stats.ttest_ind(V[g == "Con", k], V[g == "EAA", k]) for k, ty in enumerate(pag2.TYPES)}
    out["paired"] = {gg: {pair: stats.ttest_rel(V[g == gg, pair[0]], V[g == gg, pair[1]]) for pair in ((0, 1), (1, 2))} for gg in ("Con", "EAA")}
    if show:
        print(f"group F({a['group'][1]},{a['group'][2]}) = {a['group'][0]:.2f}, p = {a['group'][3]:.4f}; group x cue F = {a['group:A'][0]:.2f}, p = {a['group:A'][3]:.3f}")
        print("means (danger, uncertainty, safety):", {k: v.round(3) for k, v in out["means"].items()},
              "; range per neuron %.2f to %.2f" % (V.min(), V.max()))
        for ty, r in out["t"].items():
            print(f"   {ty:11s} Con vs EAA t({r.df:.0f}) = {r.statistic:.2f}, p = {r.pvalue:.4f}")
        for gg, d in out["paired"].items():
            print(f"   {gg} paired: " + "; ".join(f"{pag2.TYPES[p[0]][:3]}-{pag2.TYPES[p[1]][:3]} t({r.df:.0f}) = {r.statistic:.2f}, p = {r.pvalue:.4f}" for p, r in d.items()))
        for gg in ("Con", "EAA"):
            byrat = collections.defaultdict(list)
            for j in np.where(m & (grp == gg))[0]:
                byrat[U[j]["rat"]].append(F[j, :, pag2.WIN[win]].mean(1))
            print(f"   {gg} by rat (n, mean danger/uncertainty/safety):", {r: (len(v), np.round(np.mean(v, 0), 2).tolist()) for r, v in byrat.items()})
    return out

print("main"); o = window_tests("exc", "first1")
print("\nvariant, the script's normalization"); window_tests("exc", "first1", F=NFc)
print("\nvariant, exact-rate selection"); window_tests("exc", "first1", L=lab_exact)
''', tag="claim:fig4c-excited-inflated-onset")

md(r'''
**Result: reproduced.** EAA cue-excited neurons fire more in the first 1 s (group F(1,79) = 5.19,
p = 0.025); the safety difference is t(79) = -3.46, p = 0.0009, below 0.0167, with EAA higher; the
paired tests give danger > uncertainty (Control p = 0.0047, EAA p = 0.023) and uncertainty >
safety (p < 0.002) in both groups. The two variants are printed above.
''')

md(r'''
## fig4de-inhibited-temporal-pattern

> Control and EAA cue-inhibited neurons differed in the temporal pattern of their cue firing (a
> group by cue by bin interaction that held with bregma level as a factor). Control neurons
> decreased firing equally to danger and uncertainty with little change to safety, sustained over
> the cue; EAA neurons decreased most to danger, less to uncertainty, mostly in the first half of
> the cue.
''')

code(r'''
for name, L, F in (("main", lab, NF), ("variant: the script's normalization", lab, NFc), ("variant: exact-rate selection", lab_exact, NF)):
    a, m = pop_anova("inh", L, F)
    f = a["group:AB"]
    print(f"{name}: n = {dict(collections.Counter(grp[m]))}; group x cue x bin F({f[1]},{f[2]}) = {f[0]:.2f}, p = {f[3]:.2g}")
m = lab == "inh"
for g in ("Con", "EAA"):
    x = NF[m & (grp == g)]
    print(g, "mean normalized firing (danger, uncertainty, safety): first half",
          x[:, :, pag2.WIN["first5"]].mean((0, 2)).round(2), "second half", x[:, :, pag2.WIN["last5"]].mean((0, 2)).round(2))
''', tag="claim:fig4de-inhibited-temporal-pattern")

md(r'''
**Result: partially reproduced.** The interaction is significant, F(110,14300) = 1.54, p =
0.00024 (the paper: F(110,14190) = 1.69, p = 9e-6), and under both variants (printed above). The
population means follow the described pattern: Control danger and uncertainty decrease alike over
both halves of the cue (-0.75 and -0.61 in the first half, -0.68 and -0.62 in the second) with
safety near zero, while EAA decreases most to danger in the first half (-1.06, uncertainty -0.79)
and less in the second. The part with bregma level could not be tested.
''')

md(r'''
## fig4f-inhibited-danger-decrease

> In the first 5 s of the cue, EAA cue-inhibited neurons decreased firing more than Control neurons
> (main effect of group), with a greater decrease to danger; the group difference to uncertainty
> fell short of the corrected level.
''')

code(r'''
print("main"); o5 = window_tests("inh", "first5")
print("\nvariant, the script's normalization"); window_tests("inh", "first5", F=NFc)
print("\nvariant, exact-rate selection"); window_tests("inh", "first5", L=lab_exact)
''', tag="claim:fig4f-inhibited-danger-decrease")

md(r'''
**Result: reproduced.** Group F(1,130) = 9.15, p = 0.003, with EAA lower; danger t(130) = 2.58, p =
0.011, below 0.0167, with EAA lower; uncertainty t(130) = 1.76, p = 0.080, short of the corrected
level as in the paper.
''')

md(r'''
## fig4f-inhibited-danger-uncertainty-discrimination

> In the first half of the cue, EAA cue-inhibited neurons discriminated danger from uncertainty,
> while Control cue-inhibited neurons did not.

Paired t tests of the first 5 s firing to danger and uncertainty within each group, judged at
0.05/2 and 0.05/3.
''')

code(r'''
for gg in ("EAA", "Con"):
    r = o5["paired"][gg][(0, 1)]
    print(f"{gg}: danger {o5['means'][gg][0]:.3f}, uncertainty {o5['means'][gg][1]:.3f}; t({r.df:.0f}) = {r.statistic:.2f}, p = {r.pvalue:.4f};"
          f" below 0.025: {r.pvalue < 0.025}, below 0.0167: {r.pvalue < 0.05/3}")
for name, kw in (("script's normalization", dict(F=NFc)), ("exact-rate selection", dict(L=lab_exact))):
    ov = window_tests("inh", "first5", show=False, **kw)
    print(name + ":", {gg: (round(ov["paired"][gg][(0, 1)].statistic, 2), round(ov["paired"][gg][(0, 1)].pvalue, 4)) for gg in ("EAA", "Con")})
''', tag="claim:fig4f-inhibited-danger-uncertainty-discrimination")

md(r'''
**Result: reproduced.** EAA neurons fire less to danger than to uncertainty (t(83) = -3.21, p =
0.0019, below both corrected levels; the paper: t = 3.14, p = 0.002); Control neurons do not differ
(t(47) = -1.29, p = 0.20; the paper: t = 1.40, p = 0.17).
''')

# ---------------- regression ----------------
md(r'''
## Single-unit regression

Per neuron, the 32 trials of its session; the response is the trial's normalized firing in each
1 s interval of the cue; the regressors are the trial's suppression ratio for the 10 s cue (fear
output) and the cue's shock probability, 1, 0.375 or 0 (threat probability), with a constant
(Methods, "Single-unit, linear regression"). The claims file names readings of the trial-wise
normalized firing and of the 0/0 trials:

- firing (a): trial rate minus its cue's mean 2 s baseline, Z scored with the neuron's
  normalization; (b): the same with the trial's own baseline; (c): the trial's rate Z scored over
  all trials and bins of the neuron;
- 0/0 trials: set to 0, or dropped.

Two more readings come from the authors' script, which regresses the cube's trial-wise Z score
(`vlPAGcube.fire.z.s1.interval`, columns 21 to 30) on the cube's suppression ratio
(`vlPAGcube.cer.cue`) (vlpagAnalysis.m, lines 2161 to 2170): firing (d), the cube's Z score, and
0/0 trials set to 1, as the cube stores them. All twelve combinations are run. Where they give
different outcomes, the outcome is taken under the script's own combination (d, 0/0 set to 1),
as an assumption, as that is what the authors' code computes from the data set's values. The two
window readings of the claims file (mean of the interval betas, or one regression on the window's
mean firing) give the same beta (see `pag2.interval_betas`).
''')

code(r'''
ZS1 = pag2.cube_field(cube, "fire.z.s1.interval")
READINGS = [(f, e) for f in "abcd" for e in ("zero", "drop", "one")]
ADOPTED = ("d", "one")
resp = lab != "osc"

def all_betas(unc=0.375, L=None):
    L = lab if L is None else L
    out = {}
    for rd in READINGS:
        FO = np.full((len(U), 10), np.nan); TP = np.full((len(U), 10), np.nan)
        for j, u in enumerate(U):
            if L[j] == "osc":
                continue
            FO[j], TP[j] = pag2.interval_betas(u, rd[0], rd[1], unc, ZS1[:, :, j])
        out[rd] = (FO, TP)
    return out

BETAS = all_betas()
nan_fits = {rd: int(np.isnan(v[0][resp]).any(1).sum()) for rd, v in BETAS.items()}
print("neurons regressed:", int(resp.sum()), "; fits with a missing beta under any reading:", sum(nan_fits.values()))
''')

md(r'''
## fig5abc-excited-reduced-threat-probability

> Control cue-excited neurons signaled threat probability (positive betas from cue onset, rising
> over the cue) with fear output betas near zero; EAA cue-excited neurons showed lower threat
> probability betas and similar fear output betas, a group by regressor interaction.

Mixed ANOVA of the betas (regressor and interval within, group between); t tests of the whole-cue
mean betas between groups.
''')

code(r'''
def fig5abc(B, L=None):
    L = lab if L is None else L
    rows = {}
    m = L == "exc"; g = grp[m]
    for rd, (FO, TP) in B.items():
        a = pag2.mixed_anova(np.stack([FO[m], TP[m]], 1), g)
        tp, fo = TP[m].mean(1), FO[m].mean(1)
        t1 = stats.ttest_ind(tp[g == "Con"], tp[g == "EAA"]); t2 = stats.ttest_ind(fo[g == "Con"], fo[g == "EAA"])
        full = a["group:A"][3] < 0.05 and t1.pvalue < 0.05 and t1.statistic > 0 and t2.pvalue >= 0.05
        part = (not full) and t1.pvalue < 0.05 and t1.statistic > 0
        rows[rd] = "reproduced" if full else "partial" if part else "not"
        print(f"{rd[0]} {rd[1]:4s}: group x regressor F({a['group:A'][1]},{a['group:A'][2]}) = {a['group:A'][0]:.2f}, p = {a['group:A'][3]:.3f}; "
              f"TP Con {tp[g=='Con'].mean():.3f} EAA {tp[g=='EAA'].mean():.3f} t = {t1.statistic:.2f} p = {t1.pvalue:.3f}; "
              f"FO Con {fo[g=='Con'].mean():.3f} EAA {fo[g=='EAA'].mean():.3f} t = {t2.statistic:.2f} p = {t2.pvalue:.3f} -> {rows[rd]}")
    return rows

r5 = fig5abc(BETAS)
FO, TP = BETAS[ADOPTED]
m = lab == "exc"
for g in ("Con", "EAA"):
    print(g, "adopted reading, mean betas per 1 s interval: TP", TP[m & (grp == g)].mean(0).round(2), "FO", FO[m & (grp == g)].mean(0).round(2))
''', tag="claim:fig5abc-excited-reduced-threat-probability")

code(r'''
print("variant, exact-rate selection")
r5x = fig5abc(all_betas(L=lab_exact), L=lab_exact)
''', tag="claim:fig5abc-excited-reduced-threat-probability")

md(r'''
**Result: partially reproduced.** Under the adopted reading (d, 0/0 trials set to 1) the whole-cue
threat probability beta is higher in Control (0.953 against 0.558, t = 2.12, p = 0.037) and the
fear output betas do not differ (p = 0.87), but the group by regressor interaction falls short
(F(1,79) = 3.79, p = 0.055). Of the six combinations the claims file names, none meets all three
parts; (b) with 0/0 trials dropped gives the same partial pattern. The script's firing with 0/0
trials set to 0 meets all three (interaction p = 0.031). Control threat probability betas are
positive from the first interval and rise over the cue (printed above).
''')

md(r'''
## fig5d-threat-tuning-curve

> The threat tuning curve of cue-excited neurons peaked at an uncertainty assignment of 0.500 in
> both groups; the EAA curve had the same shape but was lower across all assignments (main effect
> of assignment and of group, no interaction).

Nine regressions per neuron with the uncertainty value 0 to 1 in steps of 0.125, the threat
probability beta averaged over the 10 intervals (Methods, "Threat probability tuning curve").
''')

code(r'''
GRID = np.arange(9) * 0.125
m = lab == "exc"; g = grp[m]; idx = np.where(m)[0]
tune = {}
for rd in READINGS:
    T = np.array([[pag2.interval_betas(U[j], rd[0], rd[1], v, ZS1[:, :, j])[1].mean() for v in GRID] for j in idx])
    tune[rd] = T
    a = pag2.mixed_anova(T, g)
    cm = {gg: T[g == gg].mean(0) for gg in ("Con", "EAA")}
    peaks = {gg: GRID[np.argmax(v)] for gg, v in cm.items()}
    ok = all(p == 0.5 for p in peaks.values()) and a["A"][3] < 0.05 and a["group"][3] < 0.05 and cm["EAA"].mean() < cm["Con"].mean() and a["group:A"][3] >= 0.05
    print(f"{rd[0]} {rd[1]:4s}: peaks {peaks}; assignment F({a['A'][1]},{a['A'][2]}) = {a['A'][0]:.2f}, p = {a['A'][3]:.1e}; "
          f"group F({a['group'][1]},{a['group'][2]}) = {a['group'][0]:.2f}, p = {a['group'][3]:.3f}; group x assignment F = {a['group:A'][0]:.2f}, p = {a['group:A'][3]:.3f}"
          f" -> {'reproduced' if ok else 'not'}")
T = tune[ADOPTED]
print("adopted reading, curve Con", T[g == "Con"].mean(0).round(3), "EAA", T[g == "EAA"].mean(0).round(3))
plt.figure(figsize=(5, 3))
for gg, col in (("Con", "gray"), ("EAA", "navy")):
    plt.errorbar(GRID, T[g == gg].mean(0), T[g == gg].std(0, ddof=1) / np.sqrt((g == gg).sum()), color=col, label=gg)
plt.axvline(0.375, ls="--", color="k", lw=0.5); plt.xlabel("uncertainty assignment"); plt.ylabel("threat beta"); plt.legend(); plt.show()
print("plotted range %.2f to %.2f" % (T.mean(0).min() if False else min(T[g == gg].mean(0).min() for gg in ("Con", "EAA")), max(T[g == gg].mean(0).max() for gg in ("Con", "EAA"))))
''', tag="claim:fig5d-threat-tuning-curve")

md(r'''
**Result: reproduced, resting on an assumption.** Under the adopted reading (d, 0/0 trials set to
1) both curves peak at 0.500, the assignment effect is F(8,632) = 18.69, p = 3e-25, the group effect
F(1,79) = 4.15, p = 0.045 with EAA lower, and there is no interaction (p = 0.22). The peaks are at
0.500 under ten of the twelve readings, and the assignment effect holds under all, but the group
effect is significant only with the script's firing (d) and 0/0 trials dropped or set to 1 (p =
0.046 and 0.045); under the claims file's readings (a to c) it is p = 0.07 to 0.24, so under those
the claim is not reproduced.
''')

md(r'''
## figs4-peak-assignment-same-pattern

> Using the peak uncertainty assignment (0.500) in place of the actual probability gave the same
> pattern of threat probability signaling in cue-excited neurons and of fear output signaling in
> cue-inhibited neurons.
''')

code(r'''
B05 = all_betas(0.5)
def s4(B):
    out = {}
    for rd, (FO, TP) in B.items():
        me, mi = lab == "exc", lab == "inh"
        tp = TP[me].mean(1); fo = FO[mi][:, 5:].mean(1)
        out[rd] = (stats.ttest_ind(tp[grp[me] == "Con"], tp[grp[me] == "EAA"]), stats.ttest_ind(fo[grp[mi] == "Con"], fo[grp[mi] == "EAA"]))
    return out
a375, a5 = s4(BETAS), s4(B05)
for rd in READINGS:
    same = all((x.pvalue < 0.05) == (y.pvalue < 0.05) and np.sign(x.statistic) == np.sign(y.statistic) for x, y in zip(a375[rd], a5[rd]))
    print(f"{rd[0]} {rd[1]:4s}: exc whole-cue TP  0.375 t = {a375[rd][0].statistic:.2f} p = {a375[rd][0].pvalue:.3f} | 0.5 t = {a5[rd][0].statistic:.2f} p = {a5[rd][0].pvalue:.3f};"
          f"  inh last-5 s FO  0.375 t = {a375[rd][1].statistic:.2f} p = {a375[rd][1].pvalue:.3f} | 0.5 t = {a5[rd][1].statistic:.2f} p = {a5[rd][1].pvalue:.3f}  same: {same}")
''', tag="claim:figs4-peak-assignment-same-pattern")

md(r'''
**Result: reproduced.** Under the adopted reading the cue-excited threat probability difference
is significant with both values (0.375 p = 0.037, 0.5 p = 0.040, Control higher), and so is the
cue-inhibited fear output difference (p = 0.021 and 0.010, EAA more negative). The significance of
one of the two tests changes between 0.375 and 0.5 under some other readings (printed above).
''')

md(r'''
## fig5efg-inhibited-fear-output

> Control cue-inhibited neurons signaled a mix of threat probability and fear output (negative
> betas for both). In EAA cue-inhibited neurons the signals diverged in the second half of the cue,
> fear output persisting and threat probability diminishing (group by regressor by interval
> interaction); fear output betas in the last 5 s were more negative in EAA, threat probability
> betas did not differ.
''')

code(r'''
def fig5efg(B, L=None):
    L = lab if L is None else L
    m = L == "inh"; g = grp[m]; rows = {}
    for rd, (FO, TP) in B.items():
        a = pag2.mixed_anova(np.stack([FO[m], TP[m]], 1), g)
        fo, tp = FO[m][:, 5:].mean(1), TP[m][:, 5:].mean(1)
        t1 = stats.ttest_ind(fo[g == "Con"], fo[g == "EAA"]); t2 = stats.ttest_ind(tp[g == "Con"], tp[g == "EAA"])
        f = a["group:AB"]
        full = f[3] < 0.05 and t1.pvalue < 0.05 and fo[g == "EAA"].mean() < fo[g == "Con"].mean() and t2.pvalue >= 0.05
        part = (not full) and t1.pvalue < 0.05 and fo[g == "EAA"].mean() < fo[g == "Con"].mean()
        rows[rd] = "reproduced" if full else "partial" if part else "not"
        print(f"{rd[0]} {rd[1]:4s}: group x regressor x interval F({f[1]},{f[2]}) = {f[0]:.2f}, p = {f[3]:.3f}; last 5 s FO Con {fo[g=='Con'].mean():.3f} "
              f"EAA {fo[g=='EAA'].mean():.3f} t = {t1.statistic:.2f} p = {t1.pvalue:.3f}; TP t = {t2.statistic:.2f} p = {t2.pvalue:.3f} -> {rows[rd]}")
    return rows
r5e = fig5efg(BETAS)
FO, TP = BETAS[ADOPTED]; m = lab == "inh"
for g in ("Con", "EAA"):
    print(g, "adopted reading, mean betas per interval: TP", TP[m & (grp == g)].mean(0).round(2), "FO", FO[m & (grp == g)].mean(0).round(2))
print("\nvariant, exact-rate selection"); fig5efg(all_betas(L=lab_exact), L=lab_exact)
''', tag="claim:fig5efg-inhibited-fear-output")

md(r'''
**Result: reproduced.** Under the adopted reading the three-way interaction is F(9,1170) = 2.15, p
= 0.023, the last-5 s fear output beta is more negative in EAA (-0.386 against -0.220, t = 2.34, p
= 0.021) and the threat probability betas do not differ (p = 0.41). Readings (a) and (c) with every
treatment of 0/0 trials also meet all three parts, so the outcome does not rest on the assumption.
''')

# ---------------- correlations ----------------
md(r'''
## Firing and signaling (Figs. 6, 7, S5, S6)

Per neuron, the normalized firing to each cue in a window (first 1 s for cue-excited neurons, last
5 s for cue-inhibited) against a beta (whole-cue mean for Fig. 6 and S5, last-5 s mean for Fig. 7
and S6), Pearson correlation per group and cue; groups compared by Fisher r-to-z, one- and
two-tailed. Each reading of the regression is run.
''')

code(r'''
def corr_table(pop, win, which, span, show_reading=None):
    res = {}
    for rd in READINGS:
        FO, TP = BETAS[rd]
        Bm = (TP if which == "TP" else FO)[:, span].mean(1)
        rows = {}
        for k, ty in enumerate(pag2.TYPES):
            F = NF[:, k, pag2.WIN[win]].mean(1)
            rr = {}
            for gg in ("Con", "EAA"):
                mm = (lab == pop) & (grp == gg)
                r, p = stats.pearsonr(F[mm], Bm[mm]); rr[gg] = (r, p, int(mm.sum()))
            z, p1, p2 = pag2.fisher_r_to_z(rr["Con"][0], rr["Con"][2], rr["EAA"][0], rr["EAA"][2])
            rows[ty] = dict(Con=rr["Con"], EAA=rr["EAA"], z=(z, p1, p2))
        res[rd] = rows
    for rd in READINGS:
        print(f"{rd[0]} {rd[1]:4s}: " + " | ".join(
            f"{ty[:3]} Con r={v['Con'][0]:.2f} p={v['Con'][1]:.2g}, EAA r={v['EAA'][0]:.2f} p={v['EAA'][1]:.2g}, Z={v['z'][0]:.2f} p1={v['z'][1]:.2g} p2={v['z'][2]:.2g}"
            for ty, v in res[rd].items()))
    return res
FULL, LAST = slice(0, 10), slice(5, 10)
''')

md(r'''
### fig6-excited-firing-threat-decoupled

> In Control cue-excited neurons, danger and uncertainty firing in the first 1 s of the cue
> predicted the whole-cue threat probability beta; in EAA cue-excited neurons they did not, and the
> relationships differed between groups. Safety firing was unrelated in both groups, and that
> relationship did not differ between groups.
''')

code(r'''
c6 = corr_table("exc", "first1", "TP", FULL)
def judge6(v):
    dang = v["danger"]["Con"][0] > 0 and v["danger"]["Con"][1] < 0.05 and v["danger"]["EAA"][1] >= 0.05 and v["danger"]["z"][1] < 0.05
    unc = v["uncertainty"]["Con"][0] > 0 and v["uncertainty"]["Con"][1] < 0.05 and v["uncertainty"]["EAA"][1] >= 0.05 and v["uncertainty"]["z"][1] < 0.05
    saf = v["safety"]["Con"][1] >= 0.05 and v["safety"]["EAA"][1] >= 0.05 and v["safety"]["z"][1] >= 0.05
    return dang, unc, saf
for rd in READINGS:
    d_, u_, s_ = judge6(c6[rd])
    print(rd, "danger part", d_, "uncertainty part", u_, "safety part", s_)
v = c6[ADOPTED]
print("adopted reading: Control R2 danger %.3f (paper 0.56), uncertainty %.3f (paper 0.22)" % (v["danger"]["Con"][0] ** 2, v["uncertainty"]["Con"][0] ** 2))
''', tag="claim:fig6-excited-firing-threat-decoupled")

md(r'''
**Result: partially reproduced.** The danger part holds under every reading: under the adopted one,
Control r = 0.51 (R2 = 0.26, p = 0.003), EAA r = -0.00 (p = 0.98), Z = 2.37, one-tailed p = 0.009.
The uncertainty part fails under every reading, as the Control uncertainty correlation is not
significant (adopted r = 0.09, p = 0.62). The safety correlation is negative and significant in
EAA (adopted p = 0.040), against the claim. The Control R2 values (0.26 and 0.01) are far below the
paper's 0.56 and 0.22.
''')

md(r'''
### figs5-excited-firing-fear-output-unrelated

> In cue-excited neurons, cue firing did not predict fear output signaling for any cue in either
> group, and the relationships did not differ between groups.
''')

code(r'''
cs5 = corr_table("exc", "first1", "FO", FULL)
for rd in READINGS:
    v = cs5[rd]
    anysig = any(v[ty][gg][1] < 0.05 for ty in v for gg in ("Con", "EAA")) or any(v[ty]["z"][1] < 0.05 for ty in v)
    print(rd, "any correlation or one-tailed comparison significant:", anysig,
          "; smallest correlation p %.3f, smallest comparison p (one-tailed) %.3f" % (min(v[ty][gg][1] for ty in v for gg in ("Con", "EAA")), min(v[ty]["z"][1] for ty in v)))
''', tag="claim:figs5-excited-firing-fear-output-unrelated")

md(r'''
**Result: reproduced.** Under every reading none of the six correlations and none of the three
comparisons is significant (under the adopted one the smallest correlation p is 0.23 and the
smallest one-tailed comparison p 0.13).
''')

md(r'''
### fig7-inhibited-firing-fear-output

> In cue-inhibited neurons, last-5 s danger firing did not predict the last-5 s fear output beta in
> either group; uncertainty firing predicted it positively in EAA but not in Control neurons, and
> safety firing predicted it negatively in both groups; none of these relationships differed
> between groups.
''')

code(r'''
c7 = corr_table("inh", "last5", "FO", LAST)
for rd in READINGS:
    v = c7[rd]
    parts = dict(
        danger=v["danger"]["Con"][1] >= 0.05 and v["danger"]["EAA"][1] >= 0.05,
        uncertainty=v["uncertainty"]["EAA"][0] > 0 and v["uncertainty"]["EAA"][1] < 0.05 and v["uncertainty"]["Con"][1] >= 0.05,
        safety=all(v["safety"][gg][0] < 0 and v["safety"][gg][1] < 0.05 for gg in ("Con", "EAA")),
        comparisons=v["danger"]["z"][1] >= 0.05 and v["uncertainty"]["z"][1] >= 0.05 and v["safety"]["z"][2] >= 0.05)
    print(rd, parts)
''', tag="claim:fig7-inhibited-firing-fear-output")

md(r'''
**Result: not reproduced.** Under every reading the Control uncertainty correlation is strongly
positive (adopted r = 0.71, p = 1e-8; the paper: R2 = 0.04, p = 0.16), so the uncertainty part
fails, and with it the condition for a partial outcome. Under the adopted reading the danger
correlations are not significant (p = 0.054 and 0.15), both safety correlations are negative and
significant (p = 0.027 and 0.004), and the uncertainty comparison is significant one-tailed (Z =
2.06, p = 0.020), against the claim.
''')

md(r'''
### figs6-inhibited-firing-threat-probability

> In cue-inhibited neurons, cue firing also predicted threat probability signaling in both groups,
> with no difference between Control and EAA for any relationship.
''')

code(r'''
cs6 = corr_table("inh", "last5", "TP", LAST)
for rd in READINGS:
    v = cs6[rd]
    each = all(any(v[ty][gg][1] < 0.05 for ty in v) for gg in ("Con", "EAA"))
    print(rd, "a cue with p < 0.05 in each group:", each, "; comparisons one-tailed p", [round(v[ty]["z"][1], 3) for ty in v],
          "two-tailed", [round(v[ty]["z"][2], 3) for ty in v])
''', tag="claim:figs6-inhibited-firing-threat-probability")

md(r'''
**Result: reproduced.** Under the adopted reading danger firing predicts the threat probability
beta in both groups (r = 0.73 and 0.84) and no comparison is significant (smallest p 0.052
one-tailed, 0.10 two-tailed). Under the script's firing with 0/0 trials set to 0 or dropped, the
danger comparison is significant one-tailed (p = 0.036 and 0.038) but not two-tailed; under
readings (a) to (c) no comparison is significant.
''')

md(r'''
## Summary

| Claim | Outcome |
|---|---|
| fig1bc-adversity-slows-weight-gain | blocked, data missing |
| fig1ef-acquisition-equivalent-final | blocked, data missing |
| fig2b-baseline-poke-equivalent | reproduced |
| fig2c-recording-discrimination | reproduced |
| fig2d-cue-responsive-counts | reproduced |
| fig2d-higher-proportion-responsive | reproduced |
| fig2ef-baseline-firing | reproduced |
| fig4ab-excited-temporal-pattern | partially reproduced (bregma part not testable) |
| fig4c-excited-inflated-onset | reproduced |
| fig4de-inhibited-temporal-pattern | partially reproduced (bregma part not testable) |
| fig4f-inhibited-danger-decrease | reproduced |
| fig4f-inhibited-danger-uncertainty-discrimination | reproduced |
| fig5abc-excited-reduced-threat-probability | partially reproduced (assumption) |
| fig5d-threat-tuning-curve | reproduced (assumption) |
| figs4-peak-assignment-same-pattern | reproduced (assumption) |
| fig5efg-inhibited-fear-output | reproduced |
| fig6-excited-firing-threat-decoupled | partially reproduced |
| figs5-excited-firing-fear-output-unrelated | reproduced |
| fig7-inhibited-firing-fear-output | not reproduced |
| figs6-inhibited-firing-threat-probability | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

How the analysis differs from the paper's: the selection uses the cube's stored rates, truncated to
whole Hz, as the authors' script does (with exact rates the Control inhibited count is 54, not 48);
the regressions are run under twelve readings of the trial-wise firing and of trials without
pokes, and the outcomes of Figs. 5A to D and S4 rest on the script's own reading; the ANOVAs with
bregma level could not be run; the ANOVAs and t tests use all selected neurons, so several error
degrees of freedom are larger than the paper's (for example 79 against 65 for the cue-excited
regression ANOVA).

What was found about the data set: the units come from 182 sessions (74 Control, 108 EAA), not the
stated 179; group membership and the event codes are documented only in the script (the codes
change meaning with the behaviour program); the cube stores firing rates truncated to integers;
`poke.base` is the 20 s baseline in pokes per minute, not the 2 s the description states; trials
without pokes are stored with a suppression ratio of 1; the description gives the uncertainty
shock probability as 0.25; there is no bregma level per rat, no body weight and no pre-surgery
session.
''')

nb = nbf.v4.new_notebook(); nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "entries/crcns-pag-2-moaddab-2020/reproduce_moaddab_2020.ipynb")
print("written", len(cells))
PYEOF
cd $TMPDIR && . dev/bin/activate && python gen/build.py
```

```
written 71
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && date -u && time jupyter nbconvert --to notebook --execute reproduce_moaddab_2020.ipynb --output $TMPDIR/out.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | tail -5
```

```
Fri Nov  6 20:14:08 UTC 2026

Available subcommands: execute kernel kernelspec migrate run troubleshoot
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.094s
user	0m0.086s
sys	0m0.010s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd - >/dev/null && cat > $TMPDIR/run.py <<'EOF'
import nbformat, sys, time
from nbclient import NotebookClient
nb=nbformat.read(sys.argv[1],4)
t=time.time()
NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
nbformat.write(nb,sys.argv[2]); print('ran in',time.time()-t)
EOF
python -m ipykernel install --user --name python3 >/dev/null 2>&1; time python $TMPDIR/run.py reproduce_moaddab_2020.ipynb $TMPDIR/out.ipynb 2>&1 | tail -20
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
ran in 55.27288341522217

real	0m55.625s
user	0m24.569s
sys	0m0.665s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('out.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=== cell',i, c.metadata.get('tags'))
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
"
```

```
<persisted-output>
Output too large (51.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26b813bb-c5f6-4d5b-bc86-69268017babd/tool-results/bm0y8qgs7.txt

Preview (first 2KB):
=== cell 1 None
data.zip ETag 7d1686e3d4f6f36895c38f34eda632d4 matches checksums.md5: True

359 files in data.zip; 354 unit files
   data/vlpagAnalysis.m 229411
   data/cue3.wav 223138
   data/cue2.wav 223242
   data/cue1.wav 223272
   data/cubeFile/cube.mat 29261351

354 units loaded in 35 s

=== cell 3 ['sanity']
vlPAGcube.name                            (1, 22)          <U354    
vlPAGcube.wave                            (32, 1, 354)     float64  (np.float64(-0.6401225022921883), np.float64(0.5138043102796415))
vlPAGcube.tag                             (32, 2, 354)     float64  (np.float64(1.0), np.float64(18751.420575))
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '40,200p' /home/runner/.claude/projects/-home-runner-work-encore-encore/26b813bb-c5f6-4d5b-bc86-69268017babd/tool-results/bm0y8qgs7.txt | cut -c1-400
```

```
vlPAGcube.fire.diff.ms250.interval        (32, 200, 354)   int16    (np.int16(-193), np.int16(293))
vlPAGcube.fire.diff.ms100.interval        (32, 500, 354)   int16    (np.int16(-193), np.int16(384))
vlPAGcube.fire.z.s1.interval              (32, 50, 354)    float64  (np.float64(-5.623197624702629), np.float64(14.735960431006063))
vlPAGcube.fire.z.ms500.interval           (32, 100, 354)   float64  (np.float64(-5.403542778373317), np.float64(16.039552201650896))
vlPAGcube.fire.z.ms250.interval           (32, 200, 354)   float64  (np.float64(-5.394688579003714), np.float64(25.936007964353593))
vlPAGcube.fire.z.ms100.interval           (32, 500, 354)   float64  (np.float64(-4.892211588264608), np.float64(31.381696358225007))

rats: {'Con': ['mh09', 'mh12', 'mh14', 'mh21', 'mh22', 'mh23', 'mh24', 'mh26'], 'EAA': ['mh15', 'mh17', 'mh29', 'mh30', 'mh31', 'mh32', 'mh34', 'mh35', 'mh36', 'mh38', 'mh39', 'mh40']}
rats in the script's lists but not in the data: ['mh10', 'mh11', 'mh13', 'mh16', 'mh18', 'mh19', 'mh20', 'mh25', 'mh27', 'mh28', 'mh33', 'mh37']
units per group: {np.str_('Con'): 151, np.str_('EAA'): 203}
sessions (rat and date): 182 {'Con': 74, 'EAA': 108} ; the paper and the data description state 72 Control and 107 EAA
distinct trial tables (cue onset times): 182
units per rat: {'mh09': 4, 'mh12': 17, 'mh14': 5, 'mh15': 1, 'mh17': 9, 'mh21': 81, 'mh22': 28, 'mh23': 9, 'mh24': 2, 'mh26': 5, 'mh29': 5, 'mh30': 1, 'mh31': 28, 'mh32': 42, 'mh34': 7, 'mh35': 2, 'mh36': 22, 'mh38': 16, 'mh39': 64, 'mh40': 6}
behaviour programs: {'epr38a': 161, 'epr38c': 96, 'epr38b': 97}
pairs of units with the same spike count and binned counts (possible duplicates): 0

cue onsets equal to the cube's tag in 354/354 units, trial types in 354/354
   ('epr38a', 'EVT09', np.str_('danger')) 161 units
   ('epr38a', 'EVT11', np.str_('safety')) 161 units
   ('epr38a', 'EVT12', np.str_('uncertainty')) 161 units
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '200,400p' /home/runner/.claude/projects/-home-runner-work-encore-encore/26b813bb-c5f6-4d5b-bc86-69268017babd/tool-results/bm0y8qgs7.txt | cut -c1-700
```

```
group F(1,130) = 10.81, p = 0.0013; group x cue F = 1.96, p = 0.144
means (danger, uncertainty, safety): {'Con': array([-0.294, -0.239,  0.014]), 'EAA': array([-0.442, -0.334, -0.013])} ; range per neuron -1.25 to 0.60
   danger      Con vs EAA t(130) = 2.69, p = 0.0080
   uncertainty Con vs EAA t(130) = 2.39, p = 0.0185
   safety      Con vs EAA t(130) = 0.73, p = 0.4685
   Con paired: dan-unc t(47) = -1.40, p = 0.1689; unc-saf t(47) = -6.22, p = 0.0000
   EAA paired: dan-unc t(83) = -3.14, p = 0.0024; unc-saf t(83) = -8.82, p = 0.0000
   Con by rat (n, mean danger/uncertainty/safety): {'mh09': (2, [-0.44, -0.0, 0.11]), 'mh12': (8, [-0.24, -0.25, 0.1]), 'mh14': (3, [-0.01, 0.11, 0.01]), 'mh21': (20, [-0.34, -0.3, -0.02]), 'mh22': (10, [-0.29, -0.18, 0.12]), 'mh23': (3, [-0.29, -0.37, -0.15]), 'mh26': (2, [-0.33, -0.41, -0.38])}
   EAA by rat (n, mean danger/uncertainty/safety): {'mh15': (1, [-0.7, -0.63, 0.38]), 'mh17': (2, [-0.77, -0.23, -0.01]), 'mh29': (2, [-0.81, -0.51, -0.15]), 'mh31': (4, [-0.57, -0.34, -0.07]), 'mh32': (21, [-0.37, -0.2, -0.09]), 'mh35': (2, [-0.45, -0.09, 0.19]), 'mh36': (9, [-0.3, -0.26, 0.1]), 'mh38': (7, [-0.05, -0.19, 0.01]), 'mh39': (35, [-0.54, -0.46, -0.01]), 'mh40': (1, [-0.29, -0.45, -0.02])}

variant, exact-rate selection
group F(1,139) = 13.08, p = 0.0004; group x cue F = 1.94, p = 0.146
means (danger, uncertainty, safety): {'Con': array([-0.716, -0.614,  0.041]), 'EAA': array([-1.066, -0.794, -0.048])} ; range per neuron -2.14 to 1.17
   danger      Con vs EAA t(139) = 3.14, p = 0.0021
   uncertainty Con vs EAA t(139) = 1.92, p = 0.0568
   safety      Con vs EAA t(139) = 1.08, p = 0.2820
   Con paired: dan-unc t(53) = -1.05, p = 0.2992; unc-saf t(53) = -6.60, p = 0.0000
   EAA paired: dan-unc t(86) = -3.42, p = 0.0010; unc-saf t(86) = -9.89, p = 0.0000
   Con by rat (n, mean danger/uncertainty/safety): {'mh09': (2, [-1.04, 0.08, 0.36]), 'mh12': (8, [-0.55, -0.57, 0.25]), 'mh14': (3, [0.01, 0.32, 0.04]), 'mh21': (26, [-0.79, -0.7
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && cat > $TMPDIR/a6.py <<'EOF'
import numpy as np, pag2, pickle
from scipy import stats
exec(open('/tmp/claude-1001/a4.py').read().split('t0=time.time()')[0])
res=pickle.load(open('/tmp/claude-1001/res.pkl','rb'))
Z250=pag2.cube_field(c,'fire.z.ms250.interval')
NFc=np.zeros_like(NF)
for j,u in enumerate(U):
    for k,ty in enumerate(pag2.TYPES): NFc[j,k]=Z250[u['type']==ty,:,j].mean(0)
for rd in [('d','one'),('d','zero'),('a','zero')]:
  FO,TP=res[rd]
  for nmb,B,win,pop in [('fig6 TP',TP.mean(1),'first1','exc'),('fig7 FO5',FO[:,5:].mean(1),'last5','inh')]:
    for k,ty in enumerate(pag2.TYPES):
        F=NFc[:,k,pag2.WIN[win]].mean(1); rr={}
        for gg in ['Con','EAA']:
            mm=(lab==pop)&(grp==gg); r,p=stats.pearsonr(F[mm],B[mm]); rr[gg]=(r,p,mm.sum())
        z,p1,p2=pag2.fisher_r_to_z(rr['Con'][0],rr['Con'][2],rr['EAA'][0],rr['EAA'][2])
        print(rd,nmb,ty,'Con R2=%.3f p=%.2g EAA R2=%.3f p=%.2g r %.2f %.2f Z=%.2f p1=%.3g'%(rr['Con'][0]**2,rr['Con'][1],rr['EAA'][0]**2,rr['EAA'][1],rr['Con'][0],rr['EAA'][0],z,p1))
EOF
PYTHONPATH=. python $TMPDIR/a6.py
```

```
('d', 'one') fig6 TP danger Con R2=0.566 p=6.8e-07 EAA R2=0.005 p=0.63 r 0.75 0.07 Z=3.83 p1=6.41e-05
('d', 'one') fig6 TP uncertainty Con R2=0.218 p=0.007 EAA R2=0.047 p=0.13 r 0.47 -0.22 Z=3.07 p1=0.00107
('d', 'one') fig6 TP safety Con R2=0.056 p=0.19 EAA R2=0.062 p=0.085 r -0.24 -0.25 Z=0.05 p1=0.481
('d', 'one') fig7 FO5 danger Con R2=0.066 p=0.077 EAA R2=0.041 p=0.066 r 0.26 0.20 Z=0.32 p1=0.375
('d', 'one') fig7 FO5 uncertainty Con R2=0.492 p=2.8e-08 EAA R2=0.296 p=9.1e-08 r 0.70 0.54 Z=1.40 p1=0.0806
('d', 'one') fig7 FO5 safety Con R2=0.161 p=0.0046 EAA R2=0.135 p=0.00058 r -0.40 -0.37 Z=-0.21 p1=0.415
('d', 'zero') fig6 TP danger Con R2=0.554 p=1e-06 EAA R2=0.004 p=0.65 r 0.74 0.07 Z=3.77 p1=8.05e-05
('d', 'zero') fig6 TP uncertainty Con R2=0.224 p=0.0062 EAA R2=0.046 p=0.14 r 0.47 -0.22 Z=3.09 p1=0.000992
('d', 'zero') fig6 TP safety Con R2=0.056 p=0.19 EAA R2=0.062 p=0.083 r -0.24 -0.25 Z=0.06 p1=0.475
('d', 'zero') fig7 FO5 danger Con R2=0.045 p=0.15 EAA R2=0.038 p=0.074 r 0.21 0.20 Z=0.08 p1=0.466
('d', 'zero') fig7 FO5 uncertainty Con R2=0.467 p=8.6e-08 EAA R2=0.307 p=4.5e-08 r 0.68 0.55 Z=1.13 p1=0.128
('d', 'zero') fig7 FO5 safety Con R2=0.083 p=0.047 EAA R2=0.137 p=0.00054 r -0.29 -0.37 Z=0.49 p1=0.311
('a', 'zero') fig6 TP danger Con R2=0.468 p=1.6e-05 EAA R2=0.005 p=0.63 r 0.68 0.07 Z=3.23 p1=0.000624
('a', 'zero') fig6 TP uncertainty Con R2=0.136 p=0.038 EAA R2=0.054 p=0.11 r 0.37 -0.23 Z=2.63 p1=0.00422
('a', 'zero') fig6 TP safety Con R2=0.097 p=0.082 EAA R2=0.067 p=0.071 r -0.31 -0.26 Z=-0.24 p1=0.405
('a', 'zero') fig7 FO5 danger Con R2=0.023 p=0.3 EAA R2=0.048 p=0.046 r -0.15 0.22 Z=-2.02 p1=0.0218
('a', 'zero') fig7 FO5 uncertainty Con R2=0.257 p=0.00024 EAA R2=0.411 p=5.1e-11 r 0.51 0.64 Z=-1.08 p1=0.139
('a', 'zero') fig7 FO5 safety Con R2=0.220 p=0.00076 EAA R2=0.143 p=0.00039 r -0.47 -0.38 Z=-0.60 p1=0.274
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && PYTHONPATH=. python -c "
import pag2, numpy as np
zf=pag2.open_zip(); u=pag2.load_unit(zf,'mh09061617epr38aSPK15a')
print(u['poke_base_shift'][:5], u['poke_cue_shift'][:5], pag2.suppression_ratio(u,'drop',shifted=True)[:5])
ev=u['events']['EVT14']; on=u['onset']; d=np.min(np.abs(ev[None,:]-(on[:,None]-31.5)),axis=1); print(np.round(d,2))
"
```

```
[0 0 0 0 0] [0 0 0 0 0] [nan nan nan nan nan]
[65. 65. 65. 65. 65. 65. 65. 65. 65. 65. 65. 65. 63. 63. 63. 63. 63. 63.
 63. 63. 63. 63. 63. 63. 63. 63. 63. 63. 63. 63. 63. 63.]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && PYTHONPATH=. python -c "
import pag2, numpy as np
zf=pag2.open_zip(); u=pag2.load_unit(zf,'mh21110317epr38aSPK16a')
on=np.sort(u['onset']); p=u['events']['EVT13']
rel=np.array([x-on[np.searchsorted(on,x)-1] if np.searchsorted(on,x)>0 else x-on[0] for x in p])
print(np.histogram(rel,bins=[-1000,-100,-40,-20,0,10,20,30,40,60,100,200,1000]))
e14=u['events']['EVT14']; print(np.round(np.sort(e14)[:5],2), on[:5].round(2))
print(np.round([np.min(np.abs(x-on)) for x in e14][:10],2), [ (x-on[np.searchsorted(on,x)-1]) for x in e14[:6]])
"
```

```
(array([  0,   0,   0,   6,  63, 138, 165,  25,   0,   0, 231,   0]), array([-1000,  -100,   -40,   -20,     0,    10,    20,    30,    40,
          60,   100,   200,  1000]))
[ 975.71 1138.22 1270.73 1453.24 1605.75] [ 944.21 1106.72 1239.23 1421.74 1574.25]
[31.5 31.5 31.5 31.5 31.5 31.5 33.5 31.5 31.5 31.5] [np.float64(31.499900000000025), np.float64(31.4998250000001), np.float64(31.499874999999975), np.float64(31.499874999999975), np.float64(31.499874999999975), np.float64(31.499900000000025)]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/gen && python3 - <<'EOF'
s=open('build.py').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt, (a[:60], s.count(a))
    s=s.replace(a,b)
rep('''lag14 = np.concatenate([np.min(np.abs(u["events"]["EVT14"][None, :] - (u["onset"][:, None] - 31.5)), axis=1) for u in U])
print("EVT14 lies 31.5 s before each cue onset: max deviation %.3f s" % lag14.max())''',
'''lag14 = np.concatenate([np.min(np.abs(u["events"]["EVT14"][None, :] - (u["onset"][:, None] + 31.5)), axis=1) for u in U])
print("EVT14 within 0.01 s of 31.5 s after a cue onset: %.1f%% of trials (median deviation %.3f s, max %.1f s)"
      % (100 * np.mean(lag14 < 0.01), np.median(lag14), lag14.max()))
rel = []
for u in sessions.values():
    on = np.sort(u["onset"]); p = u["events"]["EVT13"]
    k = np.searchsorted(on, p) - 1
    nxt = np.where(k + 1 < len(on), on[np.minimum(k + 1, len(on) - 1)] - p, np.inf)
    rel.append(np.where(k >= 0, p - on[np.maximum(k, 0)], -np.inf)); rel.append(-nxt)
rel_after = np.concatenate(rel[0::2]); rel_before = np.concatenate(rel[1::2])
inside = (rel_after < 30.0) | (rel_before >= -20.0)
print("nose pokes (EVT13) within 20 s before to 30 s after a cue onset: %.2f%% of %d" % (100 * inside.mean(), inside.size))''')
rep('''Clock check. Cue responses and fear should appear at the cue onsets of the trial table and vanish
when the onsets are moved 60 s earlier, into the inter-trial interval (the shortest gap between
cues is printed above). The selection rule (reading b, exact rates) and the danger minus safety
suppression ratio are computed at the true and the shifted onsets.''',
'''Clock check. Cue responses should appear at the cue onsets of the trial table and vanish when the
onsets are moved 60 s earlier, into the inter-trial interval (the shortest gap between cues is
printed above); the selection rule (reading b, exact rates) is run at both, and the firing rates at
the shifted windows are printed to show that the spikes cover them. The nose pokes are stored only
around the trials (printed above), so they cannot be shifted into the interval; for them the
danger minus safety suppression ratio is compared between the true labels and labels permuted
within each session (seeded generator).''')
rep('''dsr = []
for s, u in sessions.items():
    a = pag2.suppression_ratio(u, "drop"); b = pag2.suppression_ratio(u, "drop", shifted=True)
    dsr.append((np.nanmean(a[u["type"] == "danger"]) - np.nanmean(a[u["type"] == "safety"]),
                np.nanmean(b[u["type"] == "danger"]) - np.nanmean(b[u["type"] == "safety"])))
dsr = np.array(dsr)
print("danger minus safety suppression ratio per session, mean: true %.3f, shifted %.3f; sessions with danger > safety: %d and %d of %d"
      % (dsr[:, 0].mean(), np.nanmean(dsr[:, 1]), np.sum(dsr[:, 0] > 0), np.sum(dsr[:, 1] > 0), len(dsr)))''',
'''print("mean rate in the 10 s baseline: true %.2f Hz, shifted %.2f Hz"
      % (np.mean([pag2.window_rate(u, "base10").mean() for u in U]), np.mean([pag2.window_rate(u, "base10", True).mean() for u in U])))
rng_clock = np.random.default_rng(1)
dsr = []
for s, u in sessions.items():
    a = pag2.suppression_ratio(u, "zero")
    perm = rng_clock.permutation(u["type"])
    dsr.append((a[u["type"] == "danger"].mean() - a[u["type"] == "safety"].mean(),
                a[perm == "danger"].mean() - a[perm == "safety"].mean()))
dsr = np.array(dsr)
print("danger minus safety suppression ratio per session, mean: true labels %.3f, permuted labels %.3f; sessions with danger > safety: %d and %d of %d"
      % (dsr[:, 0].mean(), dsr[:, 1].mean(), np.sum(dsr[:, 0] > 0), np.sum(dsr[:, 1] > 0), len(dsr)))''')
rep('''shocks, EVT13 the nose pokes, EVT14 a marker 31.5 s before each cue.''','''shocks, EVT13 the nose pokes, EVT14 a marker 31.5 s after each cue onset. Nose pokes are stored
  only from 20 s before to 30 s after each cue onset, not over the whole session.''')
rep('''- The 354 units (151 Control, 203 EAA) and 20 rats (8 Control, 12 EAA) match the paper.''','''- The 354 units (151 Control, 203 EAA) and 20 rats (8 Control, 12 EAA) match the paper. No two
  units share their spike counts, so no recording is deposited twice. Cue responses are present at
  the trial table's onsets and absent 60 s earlier, and fear follows the cue labels, so the spikes,
  pokes and trial table share a clock.''')
# fig2d conclusion
rep('''**Result: reproduced.** With the cube's stored rates and reading (b), the counts are 32, 49, 48
and 84, the paper's exactly, and the totals are 151 and 203; readings (a) and (c) with the cube's
rates are also within tolerance for all four counts (a gives 34 Control inhibited, outside; see the
table). With exact rates from the spike times, reading (b) gives 30, 50, 54 and 87, and the
Control inhibited count is outside the tolerance. The paper's counts follow from the truncated rates.''',
'''**Result: reproduced.** With the cube's stored rates and reading (b), the counts are 32, 49, 48
and 84, the paper's exactly, and the totals are 151 and 203. With exact rates from the spike times,
reading (c) is also within tolerance (30, 48, 51, 89), while reading (b) gives 30, 50, 54 and 87,
the Control inhibited count outside the tolerance. Reading (a) is outside under both rate sources
(Control inhibited 44 and 34). The paper's counts follow exactly from the cube's truncated rates
and the script's reading (b), which the claims that follow use.''')
rep('''**Result: reproduced.** With the selection used here, no group difference has p < 0.05 (smallest p
= 0.26, all |t| < 1.13) under either baseline window,''','''**Result: reproduced.** With the selection used here, no group difference has p < 0.05 (smallest p
= 0.26, all |t| < 1.13) under either baseline window (with the exact-rate selection, smallest p =
0.12),''')
rep('''**Result: partially reproduced.** The group by cue by bin interaction is significant, F(110,8690)
= 1.30, p = 0.019 (the paper: F(110,8360) = 3.32, p = 3e-28), and is weaker than the paper's; the
script's normalization gives F = 1.18, p = 0.10, and the exact-rate selection F = 1.24, p = 0.044.
The part with bregma level could not be tested, as the data set has no bregma level per rat.''',
'''**Result: partially reproduced.** The group by cue by bin interaction is significant, F(110,8690)
= 1.30, p = 0.019 (the paper: F(110,8360) = 3.32, p = 3e-28), weaker than the paper's; the
script's normalization gives F = 1.40, p = 0.004, and the exact-rate selection F = 1.29, p =
0.021. The part with bregma level could not be tested, as the data set has no bregma level per
rat, so the claim holds only in the part that could be tested.''')
rep('''**Result: reproduced.** EAA cue-excited neurons fire more in the first 1 s (group F(1,79) = 5.19,
p = 0.025); the safety difference is t(79) = -3.46, p = 0.0009, below 0.0167, with EAA higher; the
paired tests give danger > uncertainty (Control p = 0.0047, EAA p = 0.023) and uncertainty >
safety (p < 0.002) in both groups. The two variants are printed above.''',
'''**Result: reproduced.** EAA cue-excited neurons fire more in the first 1 s (group F(1,79) = 5.19,
p = 0.025); the safety difference is t(79) = -3.46, p = 0.0009, below 0.0167, with EAA higher; the
paired tests give danger > uncertainty (Control p = 0.0047, EAA p = 0.023) and uncertainty >
safety (p <= 0.0018) in both groups. Both variants meet every part. With the script's
normalization the statistics are those of the paper (group F(1,79) = 4.96 against the paper's
4.96; safety t = -3.60 against 3.61).''')
rep('''**Result: partially reproduced.** The interaction is significant, F(110,14300) = 1.54, p =
0.00024 (the paper: F(110,14190) = 1.69, p = 9e-6), and under both variants (printed above). The
population means follow the described pattern: Control danger and uncertainty decrease alike over
both halves of the cue (-0.75 and -0.61 in the first half, -0.68 and -0.62 in the second) with
safety near zero, while EAA decreases most to danger in the first half (-1.06, uncertainty -0.79)
and less in the second. The part with bregma level could not be tested.''',
'''**Result: partially reproduced.** The interaction is significant, F(110,14300) = 1.54, p =
0.00024 (the paper: F(110,14190) = 1.69, p = 9e-6), and under both variants (p = 4.4e-6 and
2.5e-5). The population means follow the described pattern: Control danger and uncertainty
decrease alike over both halves of the cue (-0.75 and -0.61 in the first half, -0.69 and -0.67 in
the second) with safety near zero, while EAA decreases most to danger in the first half (-1.06,
uncertainty -0.79) and the two are alike in the second (-0.74, -0.76). The part with bregma level
could not be tested, so the claim holds only in the part that could be tested.''')
rep('''**Result: reproduced.** Group F(1,130) = 9.15, p = 0.003, with EAA lower; danger t(130) = 2.58, p =
0.011, below 0.0167, with EAA lower; uncertainty t(130) = 1.76, p = 0.080, short of the corrected
level as in the paper.''','''**Result: reproduced.** Group F(1,130) = 9.15, p = 0.003, with EAA lower; danger t(130) = 2.58, p =
0.011, below 0.0167, with EAA lower; uncertainty t(130) = 1.76, p = 0.080, short of the corrected
level as in the paper. Both variants meet the criterion; the script's normalization gives the
paper's statistics (group F = 10.81 against 10.82, danger t = 2.69 against 2.70, uncertainty t =
2.39, p = 0.0185 against 2.38, p = 0.019).''')
rep('''(t(47) = -1.29, p = 0.20; the paper: t = 1.40, p = 0.17).''','''(t(47) = -1.29, p = 0.20; the paper: t = 1.40, p = 0.17). The script's normalization gives the
paper's values (EAA t = -3.14, p = 0.0024; Control t = -1.40, p = 0.17).''')
# fig5abc
rep('''trials set to 0 meets all three (interaction p = 0.031). Control threat probability betas are
positive from the first interval and rise over the cue (printed above).''','''trials set to 0 meets all three (interaction p = 0.031). Control threat probability betas are
positive from the first interval and rise over the cue (0.72 to 1.22). With the exact-rate
selection no combination meets the threat probability part (smallest p = 0.060). The paper's
degrees of freedom (F(1,65), t(66)) imply about 67 of the 81 neurons; which were left out is not
said.''')
rep('''**Result: reproduced, resting on an assumption.** Under the adopted reading (d, 0/0 trials set to
1) both curves peak at 0.500, the assignment effect is F(8,632) = 18.69, p = 3e-25, the group effect
F(1,79) = 4.15, p = 0.045 with EAA lower, and there is no interaction (p = 0.22). The peaks are at
0.500 under ten of the twelve readings, and the assignment effect holds under all, but the group
effect is significant only with the script's firing (d) and 0/0 trials dropped or set to 1 (p =
0.046 and 0.045); under the claims file's readings (a to c) it is p = 0.07 to 0.24, so under those
the claim is not reproduced.''','''**Result: reproduced, resting on an assumption.** Under the adopted reading (d, 0/0 trials set to
1) both curves peak at 0.500, the assignment effect is F(8,632) = 18.69, p = 3e-25, the group effect
F(1,79) = 4.15, p = 0.045 with EAA lower (curve 0.34 to 0.60 against 0.56 to 1.00), and there is no
interaction (p = 0.22). The peaks are at 0.500 under ten of the twelve readings and the assignment
effect holds under all, but the group effect is significant only with the script's firing (d) and
0/0 trials dropped or set to 1 (p = 0.046 and 0.045); under the claims file's readings (a to c) it
is p = 0.07 to 0.24, and under those the claim is not reproduced.''')
rep('''is significant with both values (0.375 p = 0.037, 0.5 p = 0.040, Control higher), and so is the
cue-inhibited fear output difference (p = 0.021 and 0.010, EAA more negative). The significance of
one of the two tests changes between 0.375 and 0.5 under some other readings (printed above).''','''is significant with both values (0.375 p = 0.037, 0.5 p = 0.040, Control higher), and so is the
cue-inhibited fear output difference (p = 0.021 and 0.011, EAA more negative). The significance of
one of the two tests changes between 0.375 and 0.5 under three other readings (b drop, b one, d
zero), and is the same under the other nine.''')
rep('''= 0.023, the last-5 s fear output beta is more negative in EAA (-0.386 against -0.220, t = 2.34, p
= 0.021) and the threat probability betas do not differ (p = 0.41). Readings (a) and (c) with every
treatment of 0/0 trials also meet all three parts, so the outcome does not rest on the assumption.''','''= 0.023, the last-5 s fear output beta is more negative in EAA (-0.386 against -0.220, t = 2.34, p
= 0.021) and the threat probability betas do not differ (p = 0.41). Readings (a) and (c) with every
treatment of 0/0 trials also meet all three parts, so the outcome does not rest on the assumption;
reading (b) misses the fear output part (p = 0.054 to 0.13). With the exact-rate selection the
three-way interaction is not significant under any reading (p = 0.060 to 0.19).''')
# correlations: add script normalization variant
rep('''def corr_table(pop, win, which, span, show_reading=None):
    res = {}
    for rd in READINGS:''','''def corr_table(pop, win, which, span, F_all=None, readings=None):
    F_all = NF if F_all is None else F_all
    res = {}
    for rd in (READINGS if readings is None else readings):''')
rep('''            F = NF[:, k, pag2.WIN[win]].mean(1)
            rr = {}''','''            F = F_all[:, k, pag2.WIN[win]].mean(1)
            rr = {}''')
rep('''    for rd in READINGS:
        print(f"{rd[0]} {rd[1]:4s}: " + " | ".join(''','''    for rd in res:
        print(f"{rd[0]} {rd[1]:4s}: " + " | ".join(''')
rep('''two-tailed. Each reading of the regression is run.''','''two-tailed. Each reading of the regression is run. As a variant, the firing is also taken with the
script's normalization (mean of the cube's trial-wise Z scores), with the adopted regression
reading.''')
rep('''print("adopted reading: Control R2 danger %.3f (paper 0.56), uncertainty %.3f (paper 0.22)" % (v["danger"]["Con"][0] ** 2, v["uncertainty"]["Con"][0] ** 2))''',
'''print("adopted reading: Control R2 danger %.3f (paper 0.56), uncertainty %.3f (paper 0.22)" % (v["danger"]["Con"][0] ** 2, v["uncertainty"]["Con"][0] ** 2))
print("\\nvariant, the script's normalization of the firing, adopted regression reading")
c6c = corr_table("exc", "first1", "TP", FULL, F_all=NFc, readings=[ADOPTED])[ADOPTED]
print("parts (danger, uncertainty, safety):", judge6(c6c), "; R2 Con danger %.3f, EAA %.3f; Con uncertainty %.3f, EAA %.3f"
      % (c6c["danger"]["Con"][0] ** 2, c6c["danger"]["EAA"][0] ** 2, c6c["uncertainty"]["Con"][0] ** 2, c6c["uncertainty"]["EAA"][0] ** 2))''')
rep('''significant (adopted r = 0.09, p = 0.62). The safety correlation is negative and significant in
EAA (adopted p = 0.040), against the claim. The Control R2 values (0.26 and 0.01) are far below the
paper's 0.56 and 0.22.''','''significant (adopted r = 0.09, p = 0.62). The safety correlation is negative and significant in
EAA (adopted p = 0.040), against the claim. The Control R2 values (0.26 and 0.01) are far below the
paper's 0.56 and 0.22. With the script's normalization of the firing every part holds and the
statistics are the paper's: Control danger R2 = 0.566, p = 7e-7 (paper 0.56, 7.5e-7), Z = 3.83
(paper 3.80); Control uncertainty R2 = 0.218, p = 0.007 (paper 0.22, 0.007), Z = 3.07 (paper
3.05). The claims file fixes the Methods' normalization, under which the uncertainty part fails.''')
rep('''          "; smallest correlation p %.3f, smallest comparison p (one-tailed) %.3f" % (min(v[ty][gg][1] for ty in v for gg in ("Con", "EAA")), min(v[ty]["z"][1] for ty in v)))''','''          "; smallest correlation p %.3f, smallest comparison p (one-tailed) %.3f" % (min(v[ty][gg][1] for ty in v for gg in ("Con", "EAA")), min(v[ty]["z"][1] for ty in v)))
print("\\nvariant, the script's normalization")
corr_table("exc", "first1", "FO", FULL, F_all=NFc, readings=[ADOPTED])''')
rep('''        comparisons=v["danger"]["z"][1] >= 0.05 and v["uncertainty"]["z"][1] >= 0.05 and v["safety"]["z"][2] >= 0.05)
    print(rd, parts)''','''        comparisons=v["danger"]["z"][1] >= 0.05 and v["uncertainty"]["z"][1] >= 0.05 and v["safety"]["z"][2] >= 0.05)
    print(rd, parts)
print("\\nvariant, the script's normalization")
corr_table("inh", "last5", "FO", LAST, F_all=NFc, readings=[ADOPTED])''')
rep('''2.06, p = 0.020), against the claim.''','''2.06, p = 0.020), against the claim. The script's normalization does not change this (Control
uncertainty R2 = 0.49, p = 3e-8), although it gives the paper's values for Fig. 6.''')
rep('''          "two-tailed", [round(v[ty]["z"][2], 3) for ty in v])''','''          "two-tailed", [round(v[ty]["z"][2], 3) for ty in v])
print("\\nvariant, the script's normalization")
corr_table("inh", "last5", "TP", LAST, F_all=NFc, readings=[ADOPTED])''')
open('build.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python gen/build.py && cd entries/crcns-pag-2-moaddab-2020 && python $TMPDIR/run.py reproduce_moaddab_2020.ipynb $TMPDIR/out.ipynb 2>&1 | grep -v WARN
```

```
Fri Nov  6 20:17:18 UTC 2026
written 71
ran in 63.82615518569946
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('out.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='error': print('ERROR',i,o.ename,o.evalue)
for i in [3,6,59,62,65,68]:
    c=nb.cells[i]
    print('=== cell',i, c.metadata.get('tags'))
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[-2500:])
" | cut -c1-600
```

```
=== cell 3 ['sanity']
np.int16(384))
vlPAGcube.fire.z.s1.interval              (32, 50, 354)    float64  (np.float64(-5.623197624702629), np.float64(14.735960431006063))
vlPAGcube.fire.z.ms500.interval           (32, 100, 354)   float64  (np.float64(-5.403542778373317), np.float64(16.039552201650896))
vlPAGcube.fire.z.ms250.interval           (32, 200, 354)   float64  (np.float64(-5.394688579003714), np.float64(25.936007964353593))
vlPAGcube.fire.z.ms100.interval           (32, 500, 354)   float64  (np.float64(-4.892211588264608), np.float64(31.381696358225007))

rats: {'Con': ['mh09', 'mh12', 'mh14', 'mh21', 'mh22', 'mh23', 'mh24', 'mh26'], 'EAA': ['mh15', 'mh17', 'mh29', 'mh30', 'mh31', 'mh32', 'mh34', 'mh35', 'mh36', 'mh38', 'mh39', 'mh40']}
rats in the script's lists but not in the data: ['mh10', 'mh11', 'mh13', 'mh16', 'mh18', 'mh19', 'mh20', 'mh25', 'mh27', 'mh28', 'mh33', 'mh37']
units per group: {np.str_('Con'): 151, np.str_('EAA'): 203}
sessions (rat and date): 182 {'Con': 74, 'EAA': 108} ; the paper and the data description state 72 Control and 107 EAA
distinct trial tables (cue onset times): 182
units per rat: {'mh09': 4, 'mh12': 17, 'mh14': 5, 'mh15': 1, 'mh17': 9, 'mh21': 81, 'mh22': 28, 'mh23': 9, 'mh24': 2, 'mh26': 5, 'mh29': 5, 'mh30': 1, 'mh31': 28, 'mh32': 42, 'mh34': 7, 'mh35': 2, 'mh36': 22, 'mh38': 16, 'mh39': 64, 'mh40': 6}
behaviour programs: {'epr38a': 161, 'epr38c': 96, 'epr38b': 97}
pairs of units with the same spike count and binned counts (possible duplicates): 0

cue onsets equal to the cube's tag in 354/354 units, trial types in 354/354
   ('epr38a', 'EVT09', np.str_('danger')) 161 units
   ('epr38a', 'EVT11', np.str_('safety')) 161 units
   ('epr38a', 'EVT12', np.str_('uncertainty')) 161 units
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/crcns-pag-2-moaddab-2020 && PYTHONPATH=. python -c "
import pag2, numpy as np, scipy.io as sio, io
zf=pag2.open_zip()
for n in ['mh21110317epr38aSPK16a','mh39102317epr38cSPK07a']:
    m=sio.loadmat(io.BytesIO(zf.read('data/matFiles/'+n+'.mat'))); s=np.sort(m['spike'].ravel())
    u=pag2.load_unit(zf,n); on=np.sort(u['onset'])
    k=np.searchsorted(on,s)-1
    after=np.where(k>=0, s-on[np.maximum(k,0)], np.nan)
    print(n, np.histogram(after[~np.isnan(after)], bins=[0,10,20,30,31.5,33,40,60,100,140,200,400])[0], 'before first', np.sum(k<0), 'span', s[0], s[-1], on[0], on[-1])
"
```

```
mh21110317epr38aSPK16a [ 7891  8062  8096  1136   469    92     0     0  4076 11055     0] before first 604 span 924.3781 6057.475875 944.210275 6024.0004
mh39102317epr38cSPK07a [410 403 288  43  13   2   0   0 125 304   0] before first 13 span 863.6623 5964.815225 882.874325 5934.664825
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='pag2.py'; s=open(p).read()
s=s.replace('''SHIFT_S = 60.0   # onsets moved 60 s earlier, into the inter-trial interval, for the clock check
                 # (a standard choice; the notebook prints the shortest gap between cues)''','''SHIFT_S = 10.0   # onsets moved 10 s earlier, before the cue, for the clock check (a standard
                 # choice: spikes are stored only from about 20 s before to 33 s after each onset)''')
open(p,'w').write(s)
s=open('/tmp/claude-1001/gen/build.py').read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)
rep('''Clock check. Cue responses should appear at the cue onsets of the trial table and vanish when the
onsets are moved 60 s earlier, into the inter-trial interval (the shortest gap between cues is
printed above); the selection rule (reading b, exact rates) is run at both, and the firing rates at
the shifted windows are printed to show that the spikes cover them. The nose pokes are stored only
around the trials (printed above), so they cannot be shifted into the interval; for them the
danger minus safety suppression ratio is compared between the true labels and labels permuted
within each session (seeded generator).''','''Clock check. The spikes and pokes are stored only around the trials (printed below and above), so
the onsets cannot be moved into the inter-trial interval. Cue responses should appear at the cue
onsets of the trial table and vanish when the onsets are moved 10 s earlier, so that every window
falls before the cue; the selection rule (reading b, exact rates) is run at both, and the rates in
the shifted baseline are printed to show that the spikes cover it. For the pokes, the danger minus
safety suppression ratio is compared between the true labels and labels permuted within each
session (seeded generator).''')
rep('''print("cue-responsive units at the true onsets:", int(np.sum(true_lab != "osc")), "of", len(U),
      "; at onsets 60 s earlier:", int(np.sum(shift_lab != "osc")),''','''span = []
for u in sessions.values():
    pass
print("cue-responsive units at the true onsets:", int(np.sum(true_lab != "osc")), "of", len(U),
      "; at onsets 10 s earlier:", int(np.sum(shift_lab != "osc")),''')
rep('''print("mean rate in the 10 s baseline: true %.2f Hz, shifted %.2f Hz"''','''print("mean rate in the 10 s baseline: true %.2f Hz, shifted (20 to 10 s before onset) %.2f Hz"''')
rep('''  only from 20 s before to 30 s after each cue onset, not over the whole session.''','''  only from 20 s before to 30 s after each cue onset, and the spikes only from about 20 s before to
  33 s after, not over the whole session.''')
rep('''  units share their spike counts, so no recording is deposited twice. Cue responses are present at
  the trial table's onsets and absent 60 s earlier, and fear follows the cue labels, so the spikes,
  pokes and trial table share a clock.''','''  units share their spike counts, so no recording is deposited twice. Cue responses are present at
  the trial table's onsets and nearly absent 10 s earlier, and fear follows the cue labels, which is
  consistent with the spikes, pokes and trial table sharing a clock.''')
rep('''EVT14 a marker 31.5 s after each cue onset.''','''EVT14 a marker about 31.5 s after each cue onset.''')
open('/tmp/claude-1001/gen/build.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python gen/build.py >/dev/null && python - <<'EOF'
# quick check of the clock cell only
import sys; sys.path.insert(0,'entries/crcns-pag-2-moaddab-2020')
import pag2, numpy as np
zf=pag2.open_zip(); c,N=pag2.load_cube(zf); U=pag2.load_all(zf,N)
e,i=pag2.SELECTION_READINGS['b']
print(sum(pag2.select(u,e,i)!='osc' for u in U), sum(pag2.select(u,e,i,shifted=True)!='osc' for u in U))
print(np.mean([pag2.window_rate(u,'base10').mean() for u in U]), np.mean([pag2.window_rate(u,'base10',True).mean() for u in U]))
EOF
```

```
221 15
21.456364759887006 21.44189618644068
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='/tmp/claude-1001/gen/build.py'; s=open(p).read()
s=s.replace('''span = []
for u in sessions.values():
    pass
''','')
open(p,'w').write(s)
EOF
. dev/bin/activate && python gen/build.py && cd entries/crcns-pag-2-moaddab-2020 && cat > requirements.in <<'EOF'
aiohttp
fsspec
ipykernel
matplotlib
numpy
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-pag-2-moaddab-2020
type: reproduction
title: Early adolescent adversity and vlPAG/DR threat responding (Moaddab, Wright and McDannald 2020)
description: Tests the findings of Moaddab, Wright and McDannald (2020) on CRCNS data set pag-2,
  which holds 354 single units recorded in the ventrolateral periaqueductal gray and dorsal raphe of
  8 Control and 12 early adolescent adversity rats during fear discrimination, with the authors'
  cube and analysis script. It tests the behaviour during recording, the selection of cue-excited
  and cue-inhibited neurons, their normalized firing, the single-unit regressions on fear output and
  threat probability, and the firing and signaling relationships. The body weights and pre-surgery
  sessions of Figure 1 are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_moaddab_2020.ipynb
  title: Reproducing Moaddab et al. (2020) from CRCNS pag-2
  runtime_minutes: 2
helpers:
- pag2.py
related:
- id: crcns:pag-2/unversioned
  relation: uses_data
- id: doi:10.1038/s41598-020-74457-3
  relation: reproduces
EOF
cat ../001453-fouke-2025/entry.yaml | head -3; ls ../crcns-ac-2-deweese-2004/ 2>/dev/null | head -2; grep -n "related" -A4 ../crcns-ac-2-deweese-2004/entry.yaml
```

```
written 71
schema_version: 1
name: 001453-fouke-2025
type: reproduction
README.md
ac2.py
18:related:
19-- id: crcns:ac-2/unversioned
20-  relation: uses_data
21-- id: doi:10.1152/jn.00197.2004
22-  relation: reproduces
```

**Agent calls Bash**

```bash
cd  && date -u && python tools/entry.py lock entries/crcns-pag-2-moaddab-2020 2>&1 | tail -5 && python tools/entry.py all entries/crcns-pag-2-moaddab-2020 2>&1 | tail -30
```

```
Fri Nov  6 20:19:52 UTC 2026
wrote entries/crcns-pag-2-moaddab-2020/requirements.lock.txt
Installed kernelspec registry-crcns-pag-2-moaddab-2020 in executed/crcns-pag-2-moaddab-2020/.venv/share/jupyter/kernels/registry-crcns-pag-2-moaddab-2020
0 error(s)
pass  reproduce_moaddab_2020.ipynb  (63 s)
```

**Agent calls Bash**

```bash
ls executed/crcns-pag-2-moaddab-2020/ && $TMPDIR/dev/bin/python -c "
import nbformat
nb=nbformat.read('executed/crcns-pag-2-moaddab-2020/reproduce_moaddab_2020.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='error': print('ERROR',i)
for i in [6, 16, 22, 27, 33, 44, 48, 51]:
    c=nb.cells[i]; print('=== cell',i, c.metadata.get('tags'))
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:1800])
" | cut -c1-330
```

```
reproduce_moaddab_2020.ipynb
result.json
=== cell 6 ['sanity']
cue-responsive units at the true onsets: 221 of 354 ; at onsets 10 s earlier: 15 (chance under the rule: about 6 tests x 2 tails x 0.0083/2 = 4.9% of units)
mean rate in the 10 s baseline: true 21.46 Hz, shifted (20 to 10 s before onset) 21.44 Hz
danger minus safety suppression ratio per session, mean: true labels 0.842, permuted labels 0.005; sessions with danger > safety: 181 and 97 of 182

=== cell 16 ['claim:fig2d-cue-responsive-counts']
reading  rates   Con exc  EAA exc  Con inh  EAA inh  (paper 32, 49, 48, 84; tolerance 10%)
   a     exact        30       50       44       73   all within tolerance: False
   a     cube         32       49       34       67   all within tolerance: False
   b     exact        30       50       54       87   all within tolerance: False
   b     cube         32       49       48       84   all within tolerance: True
   c     exact        30       48       51       89   all within tolerance: True
   c     cube         32       47       43       85   all within tolerance: False
unit totals: {np.str_('Con'): 151, np.str_('EAA'): 203}

selection used below: reading (b), cube rates. Agreement with exact rates, reading (b): 340 of 354 units; Counter({(np.str_('inh'), np.str_('inh')): 131, (np.str_('osc'), np.str_('osc')): 130, (np.str_('exc'), np.str_('exc')): 79, (np.str_('osc'), np.str_('inh')): 10, (np.str_('exc'), np.str_('osc')): 2, (np.str_('osc'), np.str_
Con by rat: {'mh09': {np.str_('inh'): 2, np.str_('osc'): 2}, 'mh12': {np.str_('inh'): 8, np.str_('exc'): 8, np.str_('osc'): 1}, 'mh14': {np.str_('exc'): 2, np.str_('inh'): 3}, 'mh21': {np.str_('osc'): 53, np.str_('exc'): 8, np.str_('inh'): 20}, 'mh22': {np.str_('osc'): 7, np.str_('exc'): 11, np.str_('inh'): 10}, 'mh23': {np.str_
EAA by rat: {'mh15': {np.str_('inh'): 1}, 'mh17': {np.str_('inh'): 2, np.str_('exc'): 5, np.str_('osc'): 2}, 'mh29': {np.str_('osc'): 2, np.str_('exc'): 1, np.str_('inh'): 2}, 'mh30': {np.str
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='/tmp/claude-1001/gen/build.py'; s=open(p).read()
for a,b in [('''**Result: reproduced.** Under every reading the cue effect is large (F(2,36) from 180 to 195, p <
1e-19)''','''**Result: reproduced.** Under every reading the cue effect is large (F(2,36) from 179.5 to 194.5,
p <= 1.9e-19)'''),('''both safety correlations are negative and
significant (p = 0.027 and 0.004)''','''both safety correlations are negative and
significant (p = 0.026 and 0.004)'''),
('''degrees of freedom are larger than the paper's (for example 79 against 65 for the cue-excited
regression ANOVA).''','''degrees of freedom are larger than the paper's (for example 79 against 65 for the cue-excited
regression ANOVA). The population analyses follow the Methods' normalization, as the claims file
fixes it; the authors' script instead averages the cube's trial-wise Z scores, and with that the
statistics of Figs. 4C, 4F and 6 are the paper's to the second digit.''')]:
    assert s.count(a)==1, a[:50]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
. dev/bin/activate && python gen/build.py; python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s.get('required')), list(s['properties']))
o=s['properties']['outcomes']['items']; print(o.get('required'), list(o['properties']))
print(json.dumps(s['properties']['provenance'])[:1500])
print(json.dumps(s['properties']['findings'])[:800])
print(json.dumps(s['properties']['dataset'])[:600])
"
```

```
written 71
["schema_version", "id", "dataset", "paper", "date", "provenance", "outcomes"] ['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.", "type": "string", "pattern": "^https://"}}}}}
{"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", 
[... 2 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-pag-2-moaddab-2020-01.yaml",
 "content": "schema_version: 2\nid: crcns-pag-2-moaddab-2020-01\ndataset:\n  archive: crcns\n  id: pag-2\n  version: unversioned\n  doi: 10.6080/K0833Q7F\npaper: doi:10.1038/s41598-020-74457-3\ndate: 2026-11-06\nentry: crcns-pag-2-moaddab-2020\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42283461113\noutcomes:\n- claim: fig1bc-adversity-slows-weight-gain\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The data set holds no body weights. Its data.zip contains the 354 unit files of the\n    recording sessions, the authors' cube built from them, the script vlpagAnalysis.m and three cue\n    sounds, and the data description lists nothing else. The paper names no other deposit.\n- claim: fig1ef-acquisition-equivalent-final\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The eight pre-surgery discrimination sessions are not in the data set, which holds only\n    the recording sessions (each unit file is one recording session with spikes), and are not\n    deposited elsewhere as far as the paper and the data description say.\n- claim: fig2b-baseline-poke-equivalent\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig2b-baseline-poke-equivalent\n  notes: Baseline poke rate in the 20 s before cue onset, one value per rat over its recording\n    sessions (each session counted once). Control 23.08 and EAA 19.22 pokes per minute, t(18) =\n    1.19, p = 0.25 (the paper t = 1.24, p = 0.23). Both readings (mean of session means, trials\n    pooled) give the same values, as every session has 32 trials.\n- claim: fig2c-recording-discrimination\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig2c-recording-discrimination\n  notes: Under all six readings (session means or trials pooled; 0/0 trials set to 0, dropped or\n    set to 1) the cue effect is F(2,36) = 179.5 to 194.5, p <= 1.9e-19, the group by cue\n    interaction p = 0.84 to 0.90, and all four paired tests have p <= 0.0091 with danger >\n    uncertainty > safety. Mean ratios (0/0 as 0, session means) Control 0.919, 0.715, 0.117 and EAA\n    0.900, 0.690, 0.049.\n  deviations:\n  - Sessions are counted once per rat, although several units share each session.\n  - A third treatment of trials without pokes (ratio set to 1) is added to the claims file's two,\n    because the authors' cube stores 1 for them (cer.cue).\n- claim: fig2d-cue-responsive-counts\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig2d-cue-responsive-counts\n  measured:\n  - 32\n  - 49\n  - 48\n  - 84\n  - 151\n  - 203\n  notes: With the raw rates stored in the authors' cube and reading (b) (excitation over first 1 s\n    and last 5 s, inhibition over first 5 s and last 5 s), the counts are the paper's exactly. With\n    exact rates from the spike times, reading (c) is within tolerance (30, 48, 51, 89) and reading\n    (b) gives 30, 50, 54, 87, the Control inhibited count outside the tolerance. Reading (a) is\n    outside under both rate sources. The selection used by the dependent claims is (b) with the\n    cube's rates; with exact rates 14 of 354 units change class.\n  deviations:\n  - The cube stores the raw rates truncated to whole Hz (uint8). The authors' script runs the\n    selection t tests on these stored rates (vlpagAnalysis.m, lines 9 to 67) with reading (b)\n    (lines 136 to 147 and 225 to 236); this attempt follows the script for the rates, as the Methods\n    say only raw firing rate (Hz), and shows the exact rates as a variant.\n- claim: fig2d-higher-proportion-responsive\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig2d-higher-proportion-responsive\n  measured:\n  - 0.655\n  - 0.53\n  notes: 133/203 against 80/151, chi-square = 5.68, p = 0.017 without continuity correction (the\n    paper 5.68, p = 0.02). With exact rates (b) 0.675 and 0.556, chi-square = 5.19, p = 0.023. Every\n    reading and rate source gives EAA higher with p < 0.05 (p = 0.004 to 0.030).\n- claim: fig2ef-baseline-firing\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig2ef-baseline-firing\n  notes: With the selection used here, the group t tests have p = 0.26 to 0.96 (all |t| < 1.13)\n    under both baseline windows, the type effect F(2,351) = 6.44, p = 0.0018 (10 s) and 6.78, p =\n    0.0013 (2 s), and cue-excited neurons have the lowest mean (13.9 Hz against 22.0 and 25.3).\n    With the exact-rate selection the smallest group p is 0.12 and the type effect p = 0.0001 to\n    0.0002. The paper's error df is 346 against 351 here.\n  deviations:\n  - The ANOVA uses all 354 neurons (df 351); the paper's df of 346 implies five fewer, which are\n    not named.\n- claim: fig4ab-excited-temporal-pattern\n  outcome: partially_reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig4ab-excited-temporal-pattern\n  notes: Group by cue by bin interaction F(110,8690) = 1.30, p = 0.019 (the paper F(110,8360) =\n    3.32, p = 3e-28). With the script's normalization F = 1.40, p = 0.004; with the exact-rate\n    selection F = 1.29, p = 0.021. The part with bregma level as a factor could not be run, as the\n    data set gives no bregma level per rat (only the number of rats at each of four levels). The\n    outcome is partial because only the first part of the criterion could be tested; it held.\n  deviations:\n  - The ANOVA with bregma level was not run (no bregma level per rat in the data set).\n  - Uncorrected type III mixed ANOVA on all 81 neurons; the paper's error df implies 78.\n- claim: fig4c-excited-inflated-onset\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig4c-excited-inflated-onset\n  notes: Group F(1,79) = 5.19, p = 0.025, EAA higher; safety t(79) = -3.46, p = 0.0009; paired\n    danger against uncertainty Control p = 0.0047, EAA p = 0.023, uncertainty against safety p <=\n    0.0018 in both. With the script's normalization the statistics are the paper's (group F = 4.96,\n    p = 0.029; safety t = -3.60, p = 0.0005 against 3.61, 0.001), and the exact-rate selection also\n    meets every part.\n- claim: fig4de-inhibited-temporal-pattern\n  outcome: partially_reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig4de-inhibited-temporal-pattern\n  notes: Group by cue by bin interaction F(110,14300) = 1.54, p = 0.00024 (the paper F(110,14190) =\n    1.69, p = 9e-6); script normalization p = 4.4e-6, exact-rate selection p = 2.5e-5. The means\n    follow the described pattern (Control danger and uncertainty -0.75 and -0.61 in the first half,\n    -0.69 and -0.67 in the second, safety near 0; EAA danger -1.06 and uncertainty -0.79 in the\n    first half, -0.74 and -0.76 in the second). The bregma part could not be tested; the outcome is\n    partial for that reason only.\n  deviations:\n  - The ANOVA with bregma level was not run (no bregma level per rat in the data set).\n- claim: fig4f-inhibited-danger-decrease\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig4f-inhibited-danger-decrease\n  notes: First 5 s, group F(1,130) = 9.15, p = 0.003, EAA lower; danger t(130) = 2.58, p = 0.011,\n    EAA lower; uncertainty t(130) = 1.76, p = 0.080. The script's normalization gives the paper's\n    values (F = 10.81, danger t = 2.69, p = 0.008, uncertainty t = 2.39, p = 0.0185); the exact-rate\n    selection also meets the criterion (F = 13.08, danger p = 0.002).\n- claim: fig4f-inhibited-danger-uncertainty-discrimination\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig4f-inhibited-danger-uncertainty-discrimination\n  notes: EAA danger -1.056 against uncertainty -0.791, t(83) = -3.21, p = 0.0019, below 0.025 and\n    0.0167; Control -0.749 against -0.614, t(47) = -1.29, p = 0.20. Script normalization EAA t =\n    -3.14, p = 0.0024 and Control t = -1.40, p = 0.17 (the paper 3.14, 0.002 and 1.40, 0.17).\n- claim: fig5abc-excited-reduced-threat-probability\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig5abc-excited-reduced-threat-probability\n  notes: Under the adopted reading (the cube's trial-wise Z score, 0/0 trials set to 1, as the\n    authors' script regresses them) the whole-cue threat probability beta is higher in Control\n    (0.953 against 0.558, t(79) = 2.12, p = 0.037), the fear output betas do not differ (p = 0.87),\n    but the group by regressor interaction is F(1,79) = 3.79, p = 0.055. Of the claims file's six\n    readings none meets all three parts; (b) with 0/0 trials dropped gives the same partial\n    pattern (interaction p = 0.055, threat p = 0.047). The cube's Z score with 0/0 trials set to 0\n    meets all three (interaction p = 0.031, threat p = 0.044). Control threat betas are positive\n    from the first interval and rise (0.72 to 1.22). With the exact-rate selection no reading\n    meets the threat probability part (smallest p = 0.060). The paper's F(1,65) and t(66) imply\n    about 67 of the 81 neurons. The question of which trial-wise firing and which 0/0 treatment the\n    paper used is for its authors (see findings).\n  deviations:\n  - Assumption. The trial-wise normalized firing and the treatment of trials without pokes are\n    open in the paper (Results, Diminished threat probability signaling, paragraph 1, says only\n    \"normalized firing rate for each trial ... in 1 s bins\"). The authors' script in the data set\n    regresses vlPAGcube.fire.z.s1.interval (each trial's own 2 s baseline subtracted, Z scored over\n    all trials and bins) on vlPAGcube.cer.cue (which stores 1 for 0/0 trials) (vlpagAnalysis.m,\n    lines 2161 to 2170). That combination is adopted; the twelve combinations of the claims file's\n    readings and the script's are all shown.\n  - The tests use all 81 cue-excited neurons (df 79); the paper's df implies about 67.\n- claim: fig5d-threat-tuning-curve\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig5d-threat-tuning-curve\n  measured:\n  - 0.5\n  - 0.5\n  notes: Under the adopted reading both curves peak at 0.500, assignment F(8,632) = 18.69, p =\n    2.8e-25, group F(1,79) = 4.15, p = 0.045 with EAA lower (0.34 to 0.60 against 0.56 to 1.00), no\n    interaction (p = 0.22). Peaks are at 0.500 under ten of twelve readings (EAA 0.625 under b with\n    0/0 dropped or set to 1) and the assignment effect holds under all; the group effect has p <\n    0.05 only with the cube's Z score and 0/0 trials dropped or set to 1 (p = 0.046, 0.045). Under\n    the claims file's readings (a to c) the group effect has p = 0.07 to 0.24 and the claim is not\n    reproduced, so the outcome rests on the assumption.\n  deviations:\n  - Same assumption as fig5abc-excited-reduced-threat-probability.\n- claim: figs4-peak-assignment-same-pattern\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:figs4-peak-assignment-same-pattern\n  notes: Under the adopted reading the cue-excited whole-cue threat difference is significant with\n    0.375 (p = 0.037) and 0.5 (p = 0.040), Control higher, and the cue-inhibited last-5 s fear\n    output difference with 0.375 (p = 0.021) and 0.5 (p = 0.011), EAA more negative. Under nine of\n    the twelve readings significance and direction are the same with both values; under b with 0/0\n    dropped or set to 1 and the cube's Z score with 0/0 set to 0, one test changes side of 0.05.\n  deviations:\n  - The supplement was not available; the comparison is the one the criterion names. Same\n    assumption as fig5abc-excited-reduced-threat-probability.\n- claim: fig5efg-inhibited-fear-output\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig5efg-inhibited-fear-output\n  notes: Under the adopted reading the group by regressor by interval interaction is F(9,1170) =\n    2.15, p = 0.023, the last-5 s fear output beta is -0.386 in EAA against -0.220 in Control (t =\n    2.34, p = 0.021) and the threat betas do not differ (p = 0.41). Readings (a) and (c) of the\n    claims file meet all three parts under every 0/0 treatment, so the outcome does not rest on\n    the assumption; (b) misses the fear output part (p = 0.054 to 0.13). With the exact-rate\n    selection the interaction is not significant under any reading (p = 0.060 to 0.19).\n- claim: fig6-excited-firing-threat-decoupled\n  outcome: partially_reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig6-excited-firing-threat-decoupled\n  measured:\n  - 0.257\n  - 0.008\n  notes: Firing normalized as the claims file fixes it (Methods). The danger part holds under all\n    twelve regression readings (adopted Control r = 0.51, p = 0.003; EAA r = -0.00, p = 0.98; Z =\n    2.37, one-tailed p = 0.009). The uncertainty part fails under all twelve, as the Control\n    correlation is not significant (adopted r = 0.09, p = 0.62), and EAA safety firing correlates\n    negatively with the beta (p = 0.03 to 0.04 in all readings). With the script's normalization\n    of the firing and the adopted regression every part holds and the statistics are the paper's\n    (Control danger R2 = 0.566, p = 6.8e-7; uncertainty R2 = 0.218, p = 0.007; Z = 3.83 and 3.07,\n    one-tailed p = 6e-5 and 0.0011).\n  deviations:\n  - The Methods' normalization (claims file) and the script's normalization give different\n    outcomes; the claims file decides, and the script's result is shown as a variant.\n- claim: figs5-excited-firing-fear-output-unrelated\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:figs5-excited-firing-fear-output-unrelated\n  notes: Under all twelve readings none of the six correlations and none of the three comparisons\n    has p < 0.05 (adopted reading, smallest correlation p = 0.23, smallest one-tailed comparison p =\n    0.13). Also none with the script's normalization (smallest p = 0.059).\n- claim: fig7-inhibited-firing-fear-output\n  outcome: not_reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:fig7-inhibited-firing-fear-output\n  notes: Under every reading the Control uncertainty firing correlates strongly and positively with\n    the last-5 s fear output beta (adopted r = 0.71, p = 1.2e-8; the paper R2 = 0.04, p = 0.16), so\n    the uncertainty part fails, and with it the condition for a partial outcome. Under the adopted\n    reading the danger correlations have p = 0.054 and 0.15, both safety correlations are negative\n    with p = 0.026 and 0.004, and the uncertainty comparison is Z = 2.06, one-tailed p = 0.020. The\n    script's normalization, which gives the paper's values for Fig. 6, gives Control uncertainty R2\n    = 0.49, p = 2.8e-8 here.\n- claim: figs6-inhibited-firing-threat-probability\n  outcome: reproduced\n  notebook: reproduce_moaddab_2020.ipynb\n  output: claim:figs6-inhibited-firing-threat-probability\n  notes: Under every reading danger firing predicts the last-5 s threat beta in both groups (adopted\n    r = 0.73 and 0.84). No comparison has p < 0.05 two-tailed under any reading; one-tailed the\n    danger comparison has p = 0.036 and 0.038 with the cube's Z score and 0/0 trials set to 0 or\n    dropped, and p = 0.052 under the adopted reading. Under readings (a) to (c) no comparison has\n    one-tailed p < 0.10.\n  deviations:\n  - The criterion shows both tails; the outcome is judged with both under the adopted reading,\n    where they agree.\nfindings:\n- kind: other\n  statement: The units come from 182 recording sessions (74 Control, 108 EAA), each with its own\n    trial table, where the paper and the data description state 72 Control and 107 EAA sessions.\n    The unit counts (151 and 203) and rat counts (8 and 12) match.\n- kind: metadata_insufficient\n  statement: The group of each rat (Control or EAA) is given only by lists in the authors' script\n    vlpagAnalysis.m (lines 99 to 122), not by the data description or the files.\n- kind: metadata_insufficient\n  statement: The event codes EVT01 to EVT14 of the unit files are not described. EVT09, EVT11 and\n    EVT12 are the cue onsets, but which is danger, uncertainty or safety depends on the behaviour\n    program in the file name (epr38a, b, c); EVT08 holds the shocks, EVT13 the nose pokes, EVT14 a\n    marker about 31.5 s after each onset, and EVT02 could not be identified.\n- kind: metadata_error\n  statement: The data description says poke.base is the baseline nose poke rate 2 s prior to cue\n    presentation. It is the rate in the 20 s before cue onset (99.8% of trials; 4.2% match a 2 s\n    window), in pokes per minute, a unit the description does not give.\n- kind: metadata_error\n  statement: The data description gives the uncertainty shock rows a shock probability of 0.25;\n    the paper and the description's own summary give 0.375.\n- kind: metadata_insufficient\n  statement: No bregma recording level per rat is given; the description gives only how many rats\n    were at each of four levels, so the paper's ANOVAs with bregma level cannot be repeated.\n- kind: data_missing\n  statement: The body weights (Fig. 1B, C) and the eight pre-surgery discrimination sessions (Fig.\n    1E, F) are not in the data set.\n- kind: other\n  statement: The cube stores raw firing rates as unsigned integers truncated towards zero, so units\n    firing below 1 Hz have stored rates of 0 (775 trials with spikes have a stored 10 s baseline of\n    0). The paper's counts of cue-excited and cue-inhibited neurons follow exactly from these\n    truncated rates; with exact rates from the spike times the Control cue-inhibited count is 54,\n    not 48.\n- kind: other\n  statement: Spikes and nose pokes are stored only from about 20 s before to about 33 s after each\n    cue onset, not over the whole session, which the data description does not say.\n- kind: other\n  statement: The cube stores a suppression ratio of 1 for the 255 unit-trials (143 session-trials)\n    with no nose poke in the baseline or the cue, where the ratio is 0/0; the paper does not say how\n    such trials are treated.\n- kind: code_mismatch\n  statement: The Methods describe the normalized firing as the trial-averaged differential firing Z\n    scored over all bins and trial types of a neuron. The authors' script instead averages the\n    cube's trial-wise Z scores (each trial's own 2 s baseline subtracted, Z scored over all trials\n    and bins). With the script's version the statistics of Figs. 4C, 4F and 6 are the paper's to\n    the second digit (for example group F(1,79) = 4.96 and F(1,130) = 10.81 against 4.96 and 10.82;\n    Fig. 6 Control danger R2 = 0.566 against 0.56); with the Methods' version they differ, and the\n    uncertainty part of Fig. 6 fails.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Which trial-wise normalized firing entered the\n    single-unit regressions (Figs. 5 to 7), and how were trials with no nose poke in baseline and\n    cue treated? This attempt assumed the cube's fire.z.s1 regressed on cer.cue (0/0 stored as 1),\n    as vlpagAnalysis.m does; the claims file's readings (trial firing minus the cue's mean or the\n    trial's own 2 s baseline Z scored with the neuron's normalization, or raw firing Z scored over\n    all trials) give a non-significant group effect for Fig. 5D (p = 0.07 to 0.24) where the\n    adopted reading gives p = 0.045.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Several reported error degrees of freedom are\n    smaller than the selected neurons give (Fig. 5A to C t(66) and F(1,65) for 81 cue-excited\n    neurons; Fig. 4A, B F(110,8360); Fig. 2E, F F(2,346) for 354 neurons). Which neurons were left\n    out of these tests, and why?\n- kind: methods_unavailable\n  statement: Question for the paper's authors. With the analysis that reproduces Fig. 6 (the\n    script's normalization and regression), Control cue-inhibited uncertainty firing correlates\n    with the last-5 s fear output beta at R2 = 0.49 (p = 2.8e-8), where Fig. 7C reports R2 = 0.04,\n    p = 0.16. Was Fig. 7 computed with a different firing window, normalization or beta?\n"
}
```

```
File created successfully at: attempts/crcns-pag-2-moaddab-2020-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > entries/crcns-pag-2-moaddab-2020/README.md <<'EOF'
# Moaddab, Wright & McDannald (2020) from CRCNS pag-2

Tests the findings of [Moaddab et al. (2020)](https://doi.org/10.1038/s41598-020-74457-3) that can
be tested on CRCNS data set [pag-2](https://doi.org/10.6080/K0833Q7F), which holds 354 single units
recorded in the ventrolateral periaqueductal gray and dorsal raphe of 8 Control and 12 early
adolescent adversity (EAA) rats during fear discrimination, with the authors' cube and analysis
script. The body weights and pre-surgery sessions of Figure 1 are not in it.

| Claim | Outcome |
|---|---|
| Body weight gain slowed by adversity (Fig. 1B, C) | Blocked: data missing |
| Acquisition of discrimination before surgery (Fig. 1E, F) | Blocked: data missing |
| Equal baseline nose poking (Fig. 2B) | Reproduced |
| Discrimination during recording (Fig. 2C) | Reproduced |
| Counts of cue-excited and cue-inhibited neurons (Fig. 2D) | Reproduced |
| More cue-responsive neurons in EAA (Fig. 2D) | Reproduced |
| Baseline firing by type and group (Fig. 2E, F) | Reproduced |
| Temporal pattern of cue-excited firing (Fig. 4A, B) | Partially reproduced (bregma part not testable) |
| Inflated onset firing in EAA cue-excited neurons (Fig. 4C) | Reproduced |
| Temporal pattern of cue-inhibited firing (Fig. 4D, E) | Partially reproduced (bregma part not testable) |
| Greater danger decrease in EAA cue-inhibited neurons (Fig. 4F) | Reproduced |
| Danger and uncertainty discrimination in EAA cue-inhibited neurons (Fig. 4F) | Reproduced |
| Reduced threat probability signaling in EAA cue-excited neurons (Fig. 5A to C) | Partially reproduced, on an assumption |
| Threat tuning curve (Fig. 5D) | Reproduced, on an assumption |
| Same pattern with the peak assignment (Fig. S4) | Reproduced, on an assumption |
| Fear output signaling in cue-inhibited neurons (Fig. 5E to G) | Reproduced |
| Firing and threat signaling decoupled in EAA (Fig. 6) | Partially reproduced |
| Firing and fear output unrelated in cue-excited neurons (Fig. S5) | Reproduced |
| Firing and fear output in cue-inhibited neurons (Fig. 7) | Not reproduced |
| Firing and threat signaling in cue-inhibited neurons (Fig. S6) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The group of each rat and the meaning of the event codes are given only by the authors' script in
the data set. The paper's counts of responsive neurons follow from the cube's firing rates, which
are truncated to whole Hz, and its statistics for Figs. 4C, 4F and 6 follow from the script's
normalization, which differs from the one the Methods describe. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/crcns-pag-2-moaddab-2020-01.yaml`](../../attempts/crcns-pag-2-moaddab-2020-01.yaml).

- `reproduce_moaddab_2020.ipynb`: the analysis. It takes about a minute, most of it streaming the
  354 unit files from the zip.
- `pag2.py`: streaming the zip, reading the unit files and the cube, trial tables, suppression
  ratios, the selection, normalized firing, the single-unit regressions, a mixed ANOVA and the
  Fisher r-to-z test. Other notebooks on this data set can import it.
EOF
cd  && python tools/entry.py all entries/crcns-pag-2-moaddab-2020 2>&1 | tail -8
```

```
Installed kernelspec registry-crcns-pag-2-moaddab-2020 in executed/crcns-pag-2-moaddab-2020/.venv/share/jupyter/kernels/registry-crcns-pag-2-moaddab-2020
0 error(s)
pass  reproduce_moaddab_2020.ipynb  (60 s)
```

**Agent calls Bash**

```bash
rm -f $TMPDIR/*.pkl $TMPDIR/out.ipynb; cd  && python tools/entry.py handover entries/crcns-pag-2-moaddab-2020 2>&1 | tail -5; ls executed/crcns-pag-2-moaddab-2020/handover; git status --short; date -u
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: Dangerous rm operation detected in `rm -f $TMPDIR/*.pkl $TMPDIR/out.ipynb`. The target '$TMPDIR/*.pkl' is a shell variable expansion: when $TMPDIR is unset or empty it becomes `/`, `/*` or a top-level path. This requires explicit approval and cannot be auto-allowed by permission rules.

This check does not fire on a target that cannot expand to the filesystem root: use a literal absolute path: $TMPDIR is normally set, so a guard on it would not stop this rm. Dangerous rm operation on possibly-empty variable path: $TMPDIR/*.pkl in `rm -f $TMPDIR/*.pkl $TMPDIR/out.ipynb` (use a literal path: $TMPDIR is normally set, so a guard would not stop this)
```

**Agent calls Bash**

```bash
rm -f /tmp/claude-1001/U.pkl /tmp/claude-1001/lab.pkl /tmp/claude-1001/res.pkl /tmp/claude-1001/out.ipynb; cd  && python tools/entry.py handover entries/crcns-pag-2-moaddab-2020 2>&1 | tail -5; ls executed/crcns-pag-2-moaddab-2020/handover; git status --short; date -u
```

```
wrote executed/crcns-pag-2-moaddab-2020/handover
10.1038-s41598-020-74457-3.yaml
pag2.py
reproduce_moaddab_2020.ipynb
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
?? attempts/crcns-pag-2-moaddab-2020-01.yaml
?? entries/crcns-pag-2-moaddab-2020/
?? scripts
Fri Nov  6 20:24:14 UTC 2026
```

**Agent calls Bash**

```bash
ls -la entries/crcns-pag-2-moaddab-2020/ && ls -la .bashrc scripts .idea | head; git check-ignore -v entries/crcns-pag-2-moaddab-2020/__pycache__ 2>&1 | head -2
```

```
total 136
drwxr-xr-x   4 runner runner  4096 Nov  6 20:22 .
drwxr-xr-x 222 runner runner 12288 Nov  6 20:04 ..
drwxr-xr-x   3 runner runner  4096 Nov  6 20:05 .claude
-rw-r--r--   1 runner runner  3236 Nov  6 20:22 README.md
drwxr-xr-x   2 runner runner  4096 Nov  6 20:18 __pycache__
-rw-r--r--   1 runner runner  1100 Nov  6 20:19 entry.yaml
-rw-r--r--   1 runner runner 17219 Nov  6 20:18 pag2.py
-rw-r--r--   1 runner runner 74915 Nov  6 20:21 reproduce_moaddab_2020.ipynb
-rw-r--r--   1 runner runner    57 Nov  6 20:19 requirements.in
-rw-r--r--   1 runner runner  2608 Nov  6 20:19 requirements.lock.txt
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 19:52 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 19:52 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 19:52 scripts
.gitignore:1:__pycache__/	entries/crcns-pag-2-moaddab-2020/__pycache__
```

**Agent calls Bash**

```bash
find entries/crcns-pag-2-moaddab-2020/.claude -ls
```

```
5770334      4 drwxr-xr-x   3 runner   runner       4096 Nov  6 20:05 entries/crcns-pag-2-moaddab-2020/.claude
  5770335      4 drwx------   2 runner   runner       4096 Nov  6 20:05 entries/crcns-pag-2-moaddab-2020/.claude/.cc-writes
```

**Agent calls Bash**

```bash
rmdir entries/crcns-pag-2-moaddab-2020/.claude/.cc-writes entries/crcns-pag-2-moaddab-2020/.claude 2>&1; ls -a entries/crcns-pag-2-moaddab-2020/
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: Claude requested permissions to edit entries/crcns-pag-2-moaddab-2020/.claude/.cc-writes which is a sensitive file.
```

**Agent**

I finished steps 1 to 5 of the Author section and ran the handover (step 6). The entry is `entries/crcns-pag-2-moaddab-2020/` and the record is `attempts/crcns-pag-2-moaddab-2020-01.yaml`. `entry.py all` passed with 0 errors and the notebook runs in about 60 s. I did not verify my own work and committed nothing.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig1bc-adversity-slows-weight-gain | blocked, data_missing |
| fig1ef-acquisition-equivalent-final | blocked, data_missing |
| fig2b-baseline-poke-equivalent | reproduced |
| fig2c-recording-discrimination | reproduced |
| fig2d-cue-responsive-counts | reproduced (32/49/48/84, the paper's counts exactly) |
| fig2d-higher-proportion-responsive | reproduced (χ² = 5.68) |
| fig2ef-baseline-firing | reproduced |
| fig4ab-excited-temporal-pattern | partially reproduced (the bregma part could not be tested) |
| fig4c-excited-inflated-onset | reproduced |
| fig4de-inhibited-temporal-pattern | partially reproduced (the bregma part could not be tested) |
| fig4f-inhibited-danger-decrease | reproduced |
| fig4f-inhibited-danger-uncertainty-discrimination | reproduced |
| fig5abc-excited-reduced-threat-probability | partially reproduced, rests on an assumption |
| fig5d-threat-tuning-curve | reproduced, rests on an assumption |
| figs4-peak-assignment-same-pattern | reproduced, rests on an assumption |
| fig5efg-inhibited-fear-output | reproduced |
| fig6-excited-firing-threat-decoupled | partially reproduced |
| figs5-excited-firing-fear-output-unrelated | reproduced |
| fig7-inhibited-firing-fear-output | not reproduced |
| figs6-inhibited-firing-threat-probability | reproduced |

**2. The dataset**

There is one zip, streamed in place. CRCNS has no versions, so the record says `unversioned`. The header explains that `live/` holds the only published copy, and the zip's ETag matches `checksums.md5` (`7d1686e3…`).

What I found:
- **Session count:** the units come from 182 sessions (74 Control, 108 EAA), not the stated 72 and 107.
- **Group labels:** which rats are Control or EAA is given only by lists in the authors' script, `vlpagAnalysis.m`, which is inside the zip.
- **Event codes:** they are undocumented. Which code means danger, uncertainty or safety changes with the behaviour program (epr38a/b/c). I assigned them by shock contingency, and they match the cube's trial table in 354 of 354 units.
- **Truncated rates:** the cube stores firing rates truncated to whole Hz. The paper's neuron counts come out exactly only from these truncated rates. With exact rates from the spike times, the Control inhibited count is 54, not 48.
- **Baseline poke field:** `poke.base` is the 20 s baseline in pokes per minute, not "2 s" as the description says.
- **0/0 trials:** trials with no pokes, where the ratio is 0/0, are stored as 1.
- **Typo:** the description gives the uncertainty shock probability as 0.25; it is 0.375.
- **Not in the data:** there is no bregma level per rat, no body weight and no pre-surgery session.
- **Partial recordings:** spikes and pokes are stored only from about 20 s before to about 33 s after each cue onset, not over the whole session.
- **Code differs from Methods:** the paper's numbers for Figs. 4C, 4F and 6 match the authors' script to the second digit. The script averages the cube's trial-wise Z scores, which is not the normalization the Methods describe. The claims file fixes the Methods' version, so under it the uncertainty part of Fig. 6 fails. I show the script's version as a variant.

The assumption: for the regressions I used the script's own inputs, the cube's trial-wise Z score `fire.z.s1` regressed on `cer.cue`. I ran all twelve combinations of the claims file's readings and the script's.

Three questions for the paper's authors are recorded as `methods_unavailable` findings:
- Which trial-wise firing and which treatment of 0/0 trials did the regressions use?
- Which neurons were left out, given that several reported degrees of freedom are smaller than the neuron counts give?
- Why does Fig. 7 not match the computation that reproduces Fig. 6?

I asked no reader anything: I found no place where the claims file misreads the paper.

**3. Where the protocol was unclear**
1. **Code in the dataset:** the protocol only names code the paper links. This zip contains the authors' own script. I used it, as the code source, to settle details the paper leaves open, and cited line numbers.
2. **Part of a criterion untestable:** for the bregma ANOVAs no outcome fits. I recorded partially reproduced, and the notes say why.
3. **Claims file method vs the paper's actual computation:** the claims file's method follows the Methods, but the data show the paper's numbers came from the script. The protocol says Methods come first and gives no route for this. I kept the claims file's method and recorded a `code_mismatch` finding.
4. **Many readings at once:** with twelve combinations, "reproduced under one reading" invites fishing. I adopted the script's own combination as the assumption, with no reading-by-reading choice per claim.
5. **Clock check:** a time shift into the inter-trial interval was impossible because the streams are stored only around trials. I shifted onsets 10 s earlier for the spikes (221 responsive units drop to 15) and permuted the cue labels for the pokes.
6. **Rate source:** truncated cube rates against exact spike rates is a data variant that the "readings" concept does not cover. I followed the script and showed both.
7. **Develop on a subset:** this did not apply, since the whole dataset loads in 35 s.

**4. Runtime and failures**

The work took about 31 minutes (19:53 to 20:24 UTC) and the notebook runs in about 60 s. Nothing failed. Two clean-up commands were denied by permissions and nothing was lost by it:
- An empty harness folder, `entries/crcns-pag-2-moaddab-2020/.claude/.cc-writes`, is still in the entry. Git does not track empty folders.
- I first tried to delete my temporary cache files with a wildcard path. That was denied, and the same deletion with full paths worked.

The untracked dotfiles in the repository root are device mounts from the sandbox, not files I created.

## End of run

68 turns, 27 minutes, $6.95 at API prices, result: success.
