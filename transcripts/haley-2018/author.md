# haley-2018 · author · run 45733226000

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools | head -80; wc -l docs/protocol.md README.md docs/design.md docs/archives.md
```

```
Thu Nov 26 01:13:29 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
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
protocol.lock
[... 95 more lines not kept]
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
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 794 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -450;
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 414 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "OSF" -A60 docs/archives.md | head -150
```

```
319:## OSF
320-
321:- **Datasets.** A public project, component or registration on OSF
322-  (`osf.io`), the Open Science Framework of the Center for Open Science, named
323:  by its GUID: `https://osf.io/qpc2d/` is `OSF:qpc2d`, in folders `osf-qpc2d`.
324-  GUIDs are five characters and ignore case. A project's DOI, when its owners
325:  have had one minted, is `10.17605/OSF.IO/<GUID>`; a registration always has
326:  one. Most public OSF projects hold study materials, preregistrations or
327-  course pages rather than data, so the registry's list, `targets/osf.json`,
328-  is built from chosen GUIDs by `tools/build_osf_targets.py`, which reads each
329:  project's metadata, files and papers from OSF's public API v2. A project
330-  rarely names its paper in its metadata. The builder takes the papers from a
331-  registration's article DOI and from the preprints (PsyArXiv and the other
332:  OSF preprint servers) that name the project as their supplemental
333-  materials, with the journal article each preprint was published as;
334-  otherwise give the paper's DOI to the builder (`<GUID>=<paper DOI>`). A
335-  preprint's GUID may also be given: the builder takes the project it links.
336-- **Components.** A project can hold components, each a node with its own
337-  GUID, files, contributors and sometimes its own DOI, nested to any depth. A
338-  dataset is often spread across them (one component per experiment, or one
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/haley-2018.yaml; ls paper; ls entries/fouke-2025; cat papers/datasets/haley-2018.yaml; ls questions | grep haley
```

```
<persisted-output>
Output too large (49.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/b4fpv1b4m.txt

Preview (first 2KB):
# Claims for Haley, Hampton & Marder (2018), "Two central pattern generators from the crab,
# Cancer borealis, respond robustly and differentially to extreme extracellular pH", eLife
# 7:e41877, doi:10.7554/elife.41877, tested on OSF:r7aes.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-26, protocol pilot-19 as stated in docs/protocol.md.
#
# Text read. paper/10.7554-elife.41877.txt, the version of record as served by Europe PMC
# (PMC6328273, open access JATS, flattened). It holds the main text, all figure legends, the
# legends of the figure supplements, Materials and methods, and the Data availability
# statement. No PDF was supplied. The four statistics tables (Figure 3, 4, 7 and 8, figure
# supplement 1) are images in the article; only their legends are in the text, so no F, t or
# exact p-value is available, and the statistics below record only the bounds the legends
# print (*p<0.05) and the words "significant" of the Results. The source data files of
# Figures 2, 3, 4, 6, 7 and 8 are not in the text read.
#
# Code read. github.com/jesshaley/haley_hampton_marder_2018 at commit 83f5904 (8 January
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/haley-2018.yaml"
}
```

```
1	# Claims for Haley, Hampton & Marder (2018), "Two central pattern generators from the crab,
2	# Cancer borealis, respond robustly and differentially to extreme extracellular pH", eLife
3	# 7:e41877, doi:10.7554/elife.41877, tested on OSF:r7aes.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-26, protocol pilot-19 as stated in docs/protocol.md.
6	#
7	# Text read. paper/10.7554-elife.41877.txt, the version of record as served by Europe PMC
8	# (PMC6328273, open access JATS, flattened). It holds the main text, all figure legends, the
9	# legends of the figure supplements, Materials and methods, and the Data availability
10	# statement. No PDF was supplied. The four statistics tables (Figure 3, 4, 7 and 8, figure
11	# supplement 1) are images in the article; only their legends are in the text, so no F, t or
12	# exact p-value is available, and the statistics below record only the bounds the legends
13	# print (*p<0.05) and the words "significant" of the Results. The source data files of
14	# Figures 2, 3, 4, 6, 7 and 8 are not in the text read.
15	#
16	# Code read. github.com/jesshaley/haley_hampton_marder_2018 at commit 83f5904 (8 January
17	# 2019), the repository the Data availability statement names. It holds abfload.m and
18	# LoadAbf.m (read .abf), spikenburst.s2s and batchImp.s2s (Spike2 scripts for manual threshold
19	# spike and burst detection), readSpikeOutput.m and extracellularAnalysis.m (burst measures per
20	# experiment), analyzeWaveform.m and intracellularAnalysis.m (intracellular waveforms),
[... 699 more lines not kept]
```

**Agent**

Claims file read (30 claims). Next: the OSF target list and the example entry's format.

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/osf.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else len(d))
" ; grep -n '"r7aes"' -i targets/osf.json | head
```

```
<class 'dict'> ['schema_version', 'archive', 'generated', 'source', 'note']
12:   "id": "r7aes",
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/osf.json'))
print(d.keys())
t=[x for x in d['targets'] if x['id']=='r7aes'][0]
f=t.pop('files',None)
print(json.dumps(t,indent=1)[:4000])
print(len(f)); import collections
print(json.dumps(f[:3],indent=1))
print(sum(x.get('size') or 0 for x in f)/1e9)
c=collections.Counter(x['path'].rsplit('.',1)[-1] for x in f); print(c)
"
```

```
dict_keys(['schema_version', 'archive', 'generated', 'source', 'note', 'counts', 'targets'])
{
 "id": "r7aes",
 "name": "Recordings of stomatogastric and cardiac ganglia of C. borealis at varying pH",
 "url": "https://osf.io/r7aes/",
 "doi": "10.17605/osf.io/r7aes",
 "api_type": "nodes",
 "kind": "project",
 "category": "data",
 "published_version": "2019-01-08T14:49:50",
 "published": "2018-09-21",
 "withdrawn": false,
 "license": {
  "name": "CC-By Attribution 4.0 International",
  "url": "https://creativecommons.org/licenses/by/4.0/legalcode"
 },
 "contributors": [
  "Jessica A Haley",
  "David Hampton",
  "Eve Marder"
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json,collections;d=json.load(open('targets/osf.json'))
t=[x for x in d['targets'] if x['id']=='r7aes'][0]
f=t['files']
g=collections.defaultdict(list)
for x in f: g[x['path'].split('/')[0] if '/' in x['path'] else '.'].append(x)
for k in sorted(g): print(k, len(g[k]), round(sum(x['size'] for x in g[k])/1e9,2), sorted(set(x['path'].rsplit('.',1)[-1] for x in g[k])), set(x['version'] for x in g[k]))
for x in f:
  if x['path'].endswith('txt'): print(x['path'],x['size'],x['download'],x['version'])
"
```

```
877_093 12 2.27 ['abf', 'txt'] {1, 3}
877_101 13 2.37 ['abf', 'txt'] {1, 2}
877_121 13 2.63 ['abf', 'txt'] {1}
877_141 13 2.21 ['abf', 'txt'] {1}
877_149 13 1.38 ['abf', 'txt'] {1}
887_005 12 3.03 ['abf', 'txt'] {1}
887_011 13 1.34 ['abf', 'txt'] {1}
887_049 14 3.61 ['abf', 'txt'] {1}
887_061 16 1.15 ['abf', 'txt'] {1}
887_065 13 1.03 ['abf', 'txt'] {1}
887_069 12 3.8 ['abf', 'txt'] {1}
887_073 13 1.07 ['abf', 'txt'] {1}
887_093 13 1.28 ['abf', 'txt'] {1}
887_097 13 2.54 ['abf', 'txt'] {1}
887_105 13 2.56 ['abf', 'txt'] {1}
887_127 13 2.64 ['abf', 'txt'] {1}
887_137 13 4.27 ['abf', 'txt'] {1}
887_141 14 3.95 ['abf', 'txt'] {1}
887_145 13 5.39 ['abf', 'txt'] {1}
887_149 12 1.09 ['abf', 'txt'] {1}
[... 35 more lines not kept]
```

**Agent**

Data is 118 GB of raw ABF in 32 experiment folders. Two listed experiments (877_127 STG, 887_017 CG) have no folder. Reading the READMEs.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "import fsspec,pyabf" 2>&1; which uv; python3 --version; cd  python3 - <<'EOF'
import json,hashlib,urllib.request
d=json.load(open('targets/osf.json'))
t=[x for x in d['targets'] if x['id']=='r7aes'][0]
for x in t['files']:
  if x['path'].endswith('txt'):
    b=urllib.request.urlopen(x['download']+f"?version={x['version']}").read()
    print('==',x['path'], hashlib.sha256(b).hexdigest()==x['sha256'])
    print(b.decode(errors='replace'))
EOF
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec,pyabf
ModuleNotFoundError: No module named 'fsspec'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
Python 3.13.18
== 877_093/README.txt True
Experiment ID: 877_093
Experiment Date: 04/25/16

Electrodes:
IN 9: dgn
IN 10: mvn
IN 11: pyn
IN 12: pdn
IN 13: lvn
Vm1: LP
Vm1_2: PD
pH
temp
[... 617 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -c 3000 entries/fouke-2025/*.py | head -60; sed -n 1,80p attempts/fouke-2025-01.yaml
```

```
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
  runtime_minutes: 6
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,400p attempts/fouke-2025-01.yaml; python3 -c "
import json;nb=json.load(open('entries/fouke-2025/fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('----')
"
```

```
Exit code 1
  notes: All four readings put both values within tolerance; (a) median of stimulus medians DC
    10.02 and ZF 6.39 mm/s, (b) median of fish and stimulus values 9.87 and 6.41 (given as
    measured), (c) median of fish medians 9.36 and 6.33, (d) median of trials 9.88 and 6.28.
    Species effect F = 20.8, p = 7.5e-06. With 30 Hz positions DC 9.43 to 10.15 and ZF 6.07 to
    6.30 (p = 0.0011). Without the trial rejection (4487 trials in place of 4458) readings (a) to
    (c) are unchanged and (d) gives DC 9.85 and ZF 6.30 (p = 6.7e-06).
  deviations:
  - The paper does not say how the overall median is taken; four readings are shown, and all
    match.
  - 25 ZF, where the paper states 26.
  - Speeds rely on the code's scale of 10 pixels per mm, which the dandiset does not state.
- claim: fig1d-zf-forward-faster-than-static
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1d-zf-forward-faster-than-static
  measured:
  - 4.84
  - 8.78
  notes: ZF static 4.84 mm/s over 18 fish and forward 8.78 mm/s over 25 fish. Of 18 fish with
[... 135 more lines not kept]
```

**Agent**

Now a dev environment, and a test of streaming speed and ABF headers.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests pyabf numpy scipy pandas statsmodels matplotlib pingouin 2>&1 | tail -3; python -c "import pyabf,fsspec;print(pyabf.__version__, fsspec.__version__)"
```

```
2.3.8 2026.9.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pyabf, inspect
src=inspect.getsource(pyabf.ABF.__init__)
print(src[:3000])
EOF
```

```
def __init__(self,
                 abfFilePath: Union[str, pathlib.Path],
                 loadData: bool = True,
                 cacheStimulusFiles: bool = True,
                 stimulusFileFolder: bool = None):
        """
        Load header and sweep data from an ABF file.

        ### Parameters

        1. abfFilePath -- path to the ABF file.

        2. loadData -- whether or not to load sweep data values from the file immediately on instantiation.
        Set this to False if you intent to iterate many ABF files rapidly and only inspect their headers.

        3. cacheStimulusFiles -- Some ABF files use a source ABF as a stimulus file to control its DAC.
        This module automatically loads the stimulus waveform from disk if it is available.
        This parameter controls whether stimulus files should be stored in memory at the module level.
        Set to False to prevent memory issues if you intend to iterate very large numbers of ABFs with
        unique stimulus waveforms.
[... 47 more lines not kept]
```

**Agent**

pyabf's header readers take a file handle, so I can stream through fsspec. Testing on one file.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe.py <<'EOF'
import json, time, fsspec, pyabf, numpy as np
d=json.load(open('targets/osf.json'))
F={x['path']:x for x in [t for t in d['targets'] if t['id']=='r7aes'][0]['files']}
def hdr(path):
    x=F[path]; url=x['download']+f"?version={x['version']}"
    fs=fsspec.filesystem("http")
    fh=fs.open(url, block_size=2**20, size=x['size'])
    a=pyabf.ABF.__new__(pyabf.ABF)
    a.abfFilePath=path; a._preLoadData=False; a._cacheStimulusFiles=False; a.stimulusFileFolder=None; a.abfFolderPath=''; a.abfID=path
    sig=fh.read(4); fh.seek(0)
    a.abfVersion={'major':2 if sig==b'ABF2' else 1}
    (a._readHeadersV2 if sig==b'ABF2' else a._readHeadersV1)(fh)
    return a, fh
import sys
for p in sys.argv[1:]:
    t=time.time(); a,fh=hdr(p)
    print(p, a.abfVersion, a.dataRate, a.channelCount, a.adcNames, a.adcUnits, a.dataPointCount, a.dataByteStart, a.dataPointByteSize, a.dataPointCount/a.channelCount/a.dataRate/60, 'min', a.abfDateTime, round(time.time()-t,2))
EOF
python probe.py 897_037/897_037_0002.abf 877_149/877_149_0001.abf 903_046/$(python -c "
import json;d=json.load(open('targets/osf.json'))
print(sorted(x['path'] for x in [t for t in d['targets'] if t['id']=='r7aes'][0]['files'] if x['path'].startswith('903_046'))[0].split('/')[1])")
```

```
897_037/897_037_0002.abf {'major': 2, 'minor': 5, 'bugfix': 0, 'build': 0} 20000 13 ['VM1', 'VM2_1', 'VM1_2', 'Temp', 'pH', 'IN 8', 'IN 9', 'IN 10', 'IN 11', 'IN 12', 'IN 13', 'IN 14', 'IN 15'] ['mV', 'mV', 'mV', 'C', 'pH', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'] 335582208 7168 2 21.511680000000002 min 2017-07-07 13:20:57.080000 2.14
877_149/877_149_0001.abf {'major': 2, 'minor': 5, 'bugfix': 0, 'build': 0} 10000 5 ['Temp', 'pH', 'IN 11', 'IN 13', 'IN 14'] ['C', 'pH', 'V', 'V', 'V'] 45038080 6144 2 15.012693333333335 min 2016-07-01 11:51:21.762000 1.18
903_046/903_046_0002.abf {'major': 2, 'minor': 5, 'bugfix': 0, 'build': 0} 20000 13 ['PY1', 'LP3', 'stn', 'PD4', 'lgn', 'lvn', 'dgn', 'mvn', 'aln', 'pyn', 'pdn', 'pH', 'Tmp'] ['mV', 'mV', 'V', 'mV', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'mV', 'C'] 346072064 7168 2 22.184106666666665 min 2018-03-15 15:37:17.653000 1.5
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import time
exec(open('probe.py').read().split('import sys')[0])
a,fh=hdr('897_037/897_037_0002.abf')
t=time.time(); fh.seek(a.dataByteStart); b=fh.read(200_000_000); dt=time.time()-t
print(len(b)/1e6/dt,'MB/s')
EOF
```

```
22.651615217455408 MB/s
Shell cwd was reset to
```

**Agent**

Single-stream reads run at about 22 MB/s. I'll test parallel throughput and fetch the paper's code, which the claims file pins, at the same time.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && (git clone -q https://github.com/jesshaley/haley_hampton_marder_2018 code && cd code && git checkout -q 83f5904 && ls) ; python - <<'EOF'
import time
from concurrent.futures import ThreadPoolExecutor
exec(open('probe.py').read().split('import sys')[0])
ps=['897_037/897_037_0003.abf','897_037/897_037_0004.abf','897_037/897_037_0005.abf','897_037/897_037_0006.abf','897_037/897_037_0007.abf','897_037/897_037_0008.abf','897_037/897_037_0009.abf','897_037/897_037_0010.abf']
def rd(p):
    a,fh=hdr(p); fh.seek(a.dataByteStart); return len(fh.read(100_000_000))
t=time.time()
with ThreadPoolExecutor(8) as ex: n=sum(ex.map(rd,ps))
print(n/1e6/(time.time()-t),'MB/s with 8 threads')
EOF
```

```
LICENSE
LoadAbf.m
README.md
abfload.m
analyzeWaveform.m
batchImp.s2s
comparisonBarPlots.m
extracellularAnalysis.m
formatStatTables.m
intracellularAnalysis.m
pHCumulative.m
pHCumulativePTX.m
readSpikeOutput.m
rectanglePlots.m
spikenburst.s2s
stackedBarPlots.m
statistics.R
violinPlots.m
violinPlotsControl.m
95.85602709507671 MB/s with 8 threads
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat extracellularAnalysis.m readSpikeOutput.m | head -250; sed -n 1,200p pHCumulative.m
```

```
function [ ] = extracellularAnalysis ( )
%Compiles data from a single experiment
%   INPUTS:
%       Choose folder containing unit_bursts.txt files from the output of
%       spikenbursts.s2s as well as .abf files
%   OUTPUTS:
%       data: structure containing all analyzed variables
%   ACCESSORY FILES
%       readSpikeOutput.m: takes .txt files outputted from spikenbursts.s2s
%       and outputs a data structure wity many variables
%       LoadAbf.m: loads abf files into structure

% Query User for Experiment Information
directory=uigetdir(); % get directory

% get burst and abf file names
info.burstFiles = dir(strcat(directory,'/*bursts*.txt')); % find burst files in the directory
info.abfFiles = dir(strcat(directory,'/*_*.abf')); %find abf files in the directory
experimentName = info.abfFiles(1).name(1:7);
for i = 1:length(info.abfFiles) % pull out file names
[... 383 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 200,400p pHCumulative.m | grep -n -i -A3 "csv\|NaN" | head -60; sed -n 1,120p statistics.R
```

```
52:%% Export csvs for statistical analysis in R
53-
54-pH_vars = {'pH78_1' 'pH55' 'pH61' 'pH67' 'pH72' 'pH78_2' 'pH78_3' 'pH83'...
55-    'pH88' 'pH93' 'pH98' 'pH104' 'pH78_4'};
--
62:    writetable(array2table(output.(measures{i}),'VariableNames',pH_vars),[path,measures{i},'.csv']);
63-end
64-
65-state.STG_CG_health = [repmat({'STG'},length(exp.STG),1),num2cell(state.STG_prepHealth);...
--
67:writetable(array2table(state.STG_prepHealth,'VariableNames',pH_vars),[path,'STG_states.csv']);
68:writetable(array2table(state.CG_prepHealth,'VariableNames',pH_vars),[path,'CG_states.csv']);
69:writetable(array2table(state.STG_CG_health,'VariableNames',['Ganglion',pH_vars]),[path,'STG_CG_states.csv']);
70-
71-%% Save data
72-
# Statistics Code for Haley, Hampton & Marder 2018
# Last Edited 08.28.18 by JAH
# ------------------------------------------------------------------
# 1. One-Way Repeated Measures ANOVA w/ Paired Samples T-Tests (Bonferroni)
[... 117 more lines not kept]
```

**Agent**

The paper's code turns a missing pH step into zeros (empty bins count as 0), which matters because several experiments lack a step. Now comparing each folder's files with its README.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json,collections,re,urllib.request
d=json.load(open('targets/osf.json'))
f=[t for t in d['targets'] if t['id']=='r7aes'][0]['files']
g=collections.defaultdict(list)
for x in f: g[x['path'].split('/')[0]].append(x)
for k in sorted(g):
    abf=sorted(x['path'].split('/')[1] for x in g[k] if x['path'].endswith('abf'))
    rd=[x for x in g[k] if x['path'].endswith('txt')]
    if rd:
        txt=urllib.request.urlopen(rd[0]['download']+f"?version={rd[0]['version']}").read().decode()
        listed=re.findall(r'(\S+\.abf): pH ([\d.]+)',txt)
        names=[a for a,_ in listed]
        print(k, 'files',len(abf),'readme',len(names), 'notinreadme',[a for a in abf if a not in names], 'missingfiles',[a for a in names if a not in abf])
    else:
        print(k,'files',len(abf),abf)
EOF
```

```
Thu Nov 26 01:16:12 UTC 2026
877_093 files 11 readme 11 notinreadme [] missingfiles []
877_101 files 12 readme 12 notinreadme [] missingfiles []
877_121 files 12 readme 12 notinreadme [] missingfiles []
877_141 files 12 readme 12 notinreadme [] missingfiles []
877_149 files 12 readme 12 notinreadme ['877_149_0010.abf'] missingfiles ['877_149_00010.abf']
887_005 files 11 readme 11 notinreadme [] missingfiles []
887_011 files 12 readme 11 notinreadme ['887_011_0001.abf'] missingfiles []
887_049 files 13 readme 12 notinreadme ['887_049_0026.abf'] missingfiles []
887_061 files 15 readme 15 notinreadme [] missingfiles []
887_065 files 12 readme 12 notinreadme [] missingfiles []
887_069 files 11 readme 11 notinreadme [] missingfiles []
887_073 files 12 readme 12 notinreadme [] missingfiles []
887_093 files 12 readme 12 notinreadme [] missingfiles []
887_097 files 12 readme 12 notinreadme [] missingfiles []
887_105 files 12 readme 12 notinreadme [] missingfiles []
887_127 files 12 readme 12 notinreadme [] missingfiles []
887_137 files 12 readme 12 notinreadme [] missingfiles []
887_141 files 13 readme 13 notinreadme [] missingfiles []
887_145 files 12 readme 12 notinreadme ['887_145_0001.abf', '887_145_0002.abf', '887_145_0003.abf', '887_145_0004.abf', '887_145_0005.abf', '887_145_0008.abf', '887_145_0009.abf', '887_145_0010.abf', '887_145_0011.abf', '887_145_0012.abf', '887_145_0013.abf', '887_145_0014.abf'] missingfiles ['887_149_0001.abf', '887_149_0002.abf', '887_149_0003.abf', '887_149_0004.abf', '887_149_0005.abf', '887_149_0008.abf', '887_149_0009.abf', '887_149_0010.abf', '887_149_0011.abf', '887_149_0012.abf', '887_149_0013.abf', '887_149_0014.abf']
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import json, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
exec(open('probe.py').read().split('import sys')[0])
def tail(p, sec=2):
    a,fh=hdr(p)
    nch=a.channelCount; n=a.dataPointCount//nch
    k=int(sec*a.dataRate)
    fh.seek(a.dataByteStart+(n-k)*nch*2)
    raw=np.frombuffer(fh.read(k*nch*2),dtype=np.int16).reshape(k,nch)
    out={}
    for i,nm in enumerate(a.adcNames):
        if nm.lower() in ('ph','temp','tmp'):
            out[nm.lower()[:2]]=float(np.mean(raw[:,i]*a._dataGain[i]+a._dataOffset[i]))
    return dict(path=p, rate=a.dataRate, nch=nch, names=' '.join(a.adcNames), units=' '.join(a.adcUnits), minutes=n/a.dataRate/60, start=str(a.abfDateTime), **out)
ps=sorted(x for x in F if x.endswith('abf'))
with ThreadPoolExecutor(16) as ex: rows=list(ex.map(tail,ps))
df=pd.DataFrame(rows); df.to_csv('survey.csv',index=False)
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',120)
print(df.drop(columns=['names','units']).to_string())
print(df.groupby(df.path.str[:7])[['names','units']].agg(lambda s: s.nunique()).query('names>1 or units>1'))
EOF
time python survey.py
```

```
<persisted-output>
Output too large (43.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/baybaaj6n.txt

Preview (first 2KB):
                         path   rate  nch    minutes                       start         te          ph         tm
0    877_093/877_093_0001.abf  10000    9  30.025387  2016-04-25 18:10:58.685000  13.425531   -0.750767        NaN
1    877_093/877_093_0002.abf  10000    9  15.005867  2016-04-25 18:41:01.346000  13.547042   -1.056557        NaN
2    877_093/877_093_0003.abf  10000    9  15.007573  2016-04-25 18:56:02.792000  13.423326   -1.341965        NaN
3    877_093/877_093_0004.abf  10000    9  15.005867  2016-04-25 19:11:04.580000  13.437792   -1.610436        NaN
4    877_093/877_093_0005.abf  10000    9  15.015253  2016-04-25 19:26:06.250000  13.402447   -1.886642        NaN
5    877_093/877_093_0006.abf  10000    9  15.006720  2016-04-25 19:41:08.400000  13.414643   -2.117624        NaN
6    877_093/877_093_0007.abf  10000    9  30.005760  2016-04-25 19:56:09.754000  13.550457   -0.770423        NaN
7    877_093/877_093_0008.abf  10000    9  14.988800  2016-04-25 20:26:10.916000  13.857209   -0.396535        NaN
8    877_093/877_093_0009.abf  10000    9  15.014400  2016-04-25 20:41:11.630000  13.890881   -0.040843        NaN
9    877_093/877_093_0010.abf  10000    9  15.312213  2016-04-25 20:56:13.655000  13.838164    0.236224        NaN
10   877_093/877_093_0011.abf  10000    9  30.021120  2016-04-25 21:11:33.151000  13.540506   -0.761056        NaN
11   877_101/877_101_0000.abf  20000    5  15.268693  2016-04-26 16:22:51.252000        NaN         NaN  12.420179
12   877_101/877_101_0001.abf  20000    5  15.123627  2016-04-26 16:38:17.488000        NaN         NaN  12.534675
13   877_101/877_101_0002.abf  20000    5  15.062187  2016-04-26 16:53:31.179000        NaN         NaN  12.340695
14   877_101/877_101_0003.abf  20000    5
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pandas as pd
df=pd.read_csv('survey.csv'); df['exp']=df.path.str[:7]; df['f']=df.path.str[-8:-4]
for e,g in df.groupby('exp'):
    print(e, g.rate.unique(), g.names.unique())
    print('   ', ' '.join(f"{r.f}:{r.ph:.2f}/{r.minutes:.0f}m" for r in g.itertuples()))
EOF
```

```
877_093 [10000] <StringArray>
['VM1 VM1_2 Temp pH IN 9 IN 10 IN 11 IN 12 IN 13']
Length: 1, dtype: str
    0001:-0.75/30m 0002:-1.06/15m 0003:-1.34/15m 0004:-1.61/15m 0005:-1.89/15m 0006:-2.12/15m 0007:-0.77/30m 0008:-0.40/15m 0009:-0.04/15m 0010:0.24/15m 0011:-0.76/30m
877_101 [20000] <StringArray>
['ME1_Vx extra1 extra2 extra3 Tmp']
Length: 1, dtype: str
    0000:nan/15m 0001:nan/15m 0002:nan/15m 0003:nan/15m 0004:nan/15m 0005:nan/30m 0006:nan/15m 0007:nan/15m 0008:nan/15m 0009:nan/15m 0010:nan/15m 0011:nan/16m
877_121 [10000] <StringArray>
['VM1 VM1_2 Temp pH IN 9 IN 10 IN 11 IN 12 IN 13']
Length: 1, dtype: str
    0004:-0.63/16m 0005:-0.35/15m 0006:0.03/15m 0007:0.30/16m 0008:0.54/15m 0009:-0.65/60m 0010:-1.04/16m 0011:-1.33/15m 0012:-1.60/15m 0013:-1.85/16m 0014:-2.04/15m 0015:-0.69/30m
877_141 [10000] <StringArray>
['VM1_2 Temp pH IN 9 IN 11 IN 12 IN 13 IN 14 IN 15']
Length: 1, dtype: str
    0001:-0.61/15m 0002:-0.32/15m 0003:0.03/15m 0004:0.30/15m 0005:0.56/15m 0006:-0.61/30m 0007:-1.00/15m 0008:-1.28/15m 0009:-1.54/15m 0010:-1.80/15m 0011:-1.98/15m 0012:-0.63/24m
877_149 [10000] <StringArray>
['Temp pH IN 11 IN 13 IN 14', 'Temp pH IN 9 IN 11 IN 13 IN 14']
Length: 2, dtype: str
    0001:-0.59/15m 0002:-0.31/15m 0003:0.03/15m 0004:0.30/15m 0006:0.55/12m 0007:-0.57/27m 0008:-1.00/15m 0009:-1.28/15m 0010:-1.54/15m 0011:-1.81/15m 0012:-1.97/15m 0013:-0.63/27m
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat analyzeWaveform.m; grep -v "^\s*%" intracellularAnalysis.m | sed -n 1,200p | head -150
```

```
function [ data ] = analyzeWaveform ( Vm, sampleFreq, params )
%Given the membrane potential and sampling frequency, this code analyzes 
%the waveform and computes various measures
%   INPUTS:
%       Vm: array of voltage (mV)
%       sampleFreq: sampling frequency (Hz)
%   OUTPUTS:
%       data: structure with the following fields:
%           spikeTime: time of spike peak (ms)
%           spikeMin: voltage of spike trough (mV)
%           spikeMax: voltage of spike peak (mV)
%           spikeAmp: amplitude of spike (mV)
%           spikeFreq: instantaneous frequency of spikes (Hz)
%           waveTime: time of slow wave peak (ms)
%           waveMin: voltage of slow wave trough (mV)
%           waveMax: voltage of slow wave peak (mV)
%           waveAmp: amplitude of slow wave (mV)
%           waveFreq: instantaneous frequency of slow waves (Hz)
%           minVm: minimum Vm for each second of data (mV)
%           parameters: structure containing parameters used for analysis
[... 189 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" pHCumulativePTX.m | sed -n 1,140p; grep -n -i "minimum\|last minute\|threshold\|PTX\|picrotoxin\|8 min\|10 s bin\|bins" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent**

Next I'll check what `tools/entry.py check` rejects, so I know how to pin the file table.

**Agent calls Bash**

```bash
grep -n "def check\|embedded\|literal\|LITERAL\|max_\|MAX\|csv\|suffix\|allowed" tools/entry.py | head -60
```

```
22:- no notebook or helper embeds a large literal array or an encoded image, or
68:MAX_LITERAL_NUMBERS = 200                 # more numbers than this in one literal is "embedded data"
73:LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)
179:def check(entry_dir: Path) -> Report:
470:    allowed = os.environ.get("ENCORE_LOCAL_DATA", "").rstrip("/")
471:    return bool(allowed) and code.startswith(allowed, start) and code[start + len(allowed):start + len(allowed) + 1] in ("/", "'", '"')
489:    if LONG_LITERAL.search(code):
490:        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
554:                   max_minutes: float) -> int:
560:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
607:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
618:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
625:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
627:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
663:        if ok and seconds > max_minutes * 60:
665:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
731:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
773:                              args.timeout, args.max_minutes)
783:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
```

**Agent calls Bash**

```bash
sed -n 179,300p tools/entry.py
```

```
def check(entry_dir: Path) -> Report:
    report = Report()
    rel = entry_dir.relative_to(ROOT)
    entry = validate(report, entry_dir / "entry.yaml", "entry")
    if entry is None:
        return report
    if entry.get("name") != entry_dir.name:
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

[... 103 more lines not kept]
```

**Agent**

Before writing the helper I need to see the signals to pick a spike-detection rule. Plotting a few seconds of a PD nerve (897_037) and a CG trunk (877_149).

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > look.py <<'EOF'
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, sys
exec(open('probe.py').read().split('import sys')[0])
def seg(p, chans, t0, dur):
    a,fh=hdr(p); nch=a.channelCount; r=a.dataRate
    i0=int(t0*r) if t0>=0 else a.dataPointCount//nch+int(t0*r)
    fh.seek(a.dataByteStart+i0*nch*2); raw=np.frombuffer(fh.read(int(dur*r)*nch*2),np.int16).reshape(-1,nch)
    out={}
    for c in chans:
        i=a.adcNames.index(c); out[c]=raw[:,i]*a._dataGain[i]+a._dataOffset[i]
    return out, r
jobs=[(sys.argv[i], sys.argv[i+1].split(',')) for i in range(1,len(sys.argv),2)]
fig,axs=plt.subplots(sum(len(c) for _,c in jobs),1,figsize=(16,2.2*sum(len(c) for _,c in jobs)))
k=0
for p,ch in jobs:
    o,r=seg(p,ch,-30,8)
    for c in ch:
        x=o[c]; t=np.arange(len(x))/r
        axs[k].plot(t,x,lw=0.4); axs[k].set_title(f'{p} {c} med {np.median(x):.3f} mad {np.median(abs(x-np.median(x))):.4f}',fontsize=8); k+=1
plt.tight_layout(); plt.savefig('look.png',dpi=70)
EOF
python look.py 897_037/897_037_0002.abf "IN 13,IN 15,VM1,VM1_2" 877_149/877_149_0001.abf "IN 11,IN 13" 877_149/877_149_0006.abf "IN 11"
```

```
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/look.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
date -u; mkdir -p entries/haley-2018; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json
d=json.load(open('targets/osf.json'))
f=[t for t in d['targets'] if t['id']=='r7aes'][0]['files']
lines=[f"{x['path']} {x['download'].rstrip('/').rsplit('/',1)[1]} {x['version']} {x['size']} {x['sha256']}" for x in sorted(f,key=lambda x:x['path'])]
open('pinned.txt','w').write('\n'.join(lines)+'\n')
print(len(lines), lines[0])
EOF
```

```
Thu Nov 26 01:20:30 UTC 2026
408 877_093/877_093_0001.abf 5w9tz 1 324280832 47277a452f25b9e739850a503eac6c4dc50ab8d22df9fd86f21ab2dd43ae9a0e
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
lines=open('pinned.txt').read()
open('pinned_block.txt','w').write(lines)
EOF
wc -c $TMPDIR/pinned_block.txt
```

```
51088 /tmp/claude-1001/pinned_block.txt
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/haley-2018 && python3 - <<'EOF'
import os
block=open(os.environ.get('TMPDIR','/tmp')+'/pinned_block.txt').read()
open('r7aes_files.py','w').write('''"""The files of OSF project r7aes as the registry's target list read them (targets/osf.json,
built when the project was last modified 2019-01-08T14:49:50).

One line per file: path, download key (https://osf.io/download/<key>/), OSF Storage version,
size in bytes and SHA-256. Every file is read at this version, and its SHA-256 is checked
against this table when the file is read whole.
"""

PUBLISHED_VERSION = "2019-01-08T14:49:50"

PINNED = """\\
''' + block + '''"""


def table():
    rows = {}
    for line in PINNED.split("\\n"):
        if line.strip():
            path, key, version, size, sha = line.split()
            rows[path] = dict(key=key, version=int(version), size=int(size), sha256=sha)
    return rows
''')
EOF
python3 -c "import sys;sys.path.insert(0,'entries/haley-2018');import r7aes_files as r;print(len(r.table()))" 2>&1 || (cd  && python3 -c "import sys;sys.path.insert(0,'entries/haley-2018');import r7aes_files as r;print(len(r.table()))")
```

```
408
```

**Agent**

Now the main helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/haley-2018/crabph.py",
 "content": "\"\"\"Loading and measures for OSF project r7aes, the raw recordings of Haley, Hampton & Marder (2018),\n\"Two central pattern generators from the crab, Cancer borealis, respond robustly and differentially\nto extreme extracellular pH\", eLife 7:e41877, doi:10.7554/elife.41877.\n\nThe project holds one folder per experiment, each with Axon .abf files (one per pH step) and, for the\nSTG and CG experiments, a README.txt naming each file's pH and each channel's nerve. Files are read\nanonymously from OSF Storage at the version pinned in r7aes_files.py, streamed into memory with\nfsspec and never written to disk. A file read whole has its SHA-256 checked against that table.\n\nWhere the parameters come from (claims/haley-2018.yaml names the methods [EXT], [STATE], [INTRA],\n[RM] and [MIX] in its header; \"paper\" is paper/10.7554-elife.41877.txt; \"code\" is\ngithub.com/jesshaley/haley_hampton_marder_2018 at commit 83f5904):\n\n- Experiments and units: the 15 STG experiments, the 15 CG experiment and unit pairs and the 9 PTX\n  experiments are the lists of pHCumulative.m and pHCumulativePTX.m (claims header). A CG unit\n  \"CGnL\" is the Large Cell unit on the trunk channel the README names \"CGn (trunk)\".\n- Conditions: the code's 13 columns (pHCumulative.m, `pH_vars`): recovery from acid, 5.5, 6.1,\n  6.7, 7.2, control before acid, control before base, 8.3, 8.8, 9.3, 9.8, 10.4, recovery from base.\n  The pH of a file is the README's; for the PTX folders, which have no README, it is assigned from\n  the bath pH channel recorded in each file (assumption, as nothing else names it; see\n  `assign_ptx_conditions`). Where a README lists several consecutive control files, the last\n  one of at least 8 min stands for the condition (a standard choice; the code takes one file).\n- [EXT] spikes: spikes are found by thresholding the extracellular trace (paper, Methods, \"Data\n  acquisition and analysis\", paragraph 4). The paper set thresholds by hand in Spike2\n  (spikenburst.s2s); here they are automatic, an assumption: the trace is high-passed at\n  `HIGHPASS_HZ` (a standard choice for extracellular spikes), the polarity is that of the larger\n  extreme, and the threshold of a file is the larger of `NOISE_K` times the robust noise (median\n  absolute deviation / 0.6745) and `AMP_FRAC` times the `AMP_PCTL` percentile of the event heights\n  of the unit in its first control file, so that a unit is followed across files while the smaller\n  units (the Small Cells on the CG trunk) stay under it.\n- [EXT] bursts: Spike2 BurstMake with 0.3 s maximum interspike interval and at least 2 spikes per\n  burst (spikenburst.s2s starting values, claims header [EXT]; `MAX_ISI_S`, `MIN_SPIKES`).\n  Frequency 1 / (onset of the previous burst to this onset), duty cycle = (first to last spike) /\n  that period, spikes per burst, as readSpikeOutput.m. Duty cycles above 0.4 and spike counts\n  above 15 (STG) or 30 (CG) are discarded (extracellularAnalysis.m). Means in 10 s bins, 48 bins\n  over the last 8 min of the file (paper, Methods paragraphs 2 and 4); an empty bin counts as 0\n  (pHCumulative.m). The value of a preparation and condition is the mean of its 48 bins\n  (pHCumulative.m csv export). Variant (code): 48 bins from the first burst of the file\n  (`window=\"code\"`; claims header [EXT]).\n- [STATE] proxy: the manual state annotations are not in the dataset. `rhythmic_fraction` gives,\n  per second of the last 8 min, whether the pacemaker unit (PD, or LC) is bursting rhythmically:\n  the second lies between two burst onsets no more than `RHYTHM_GAP_FACTOR` times the unit's median\n  period in its first control step apart (an assumption; see the notebook). Runs shorter than 10 s\n  are merged into their surroundings, as the paper notes a transition only after 10 s in the new\n  state (Methods paragraph 3).\n- [INTRA]: last minute of each file (paper, Methods paragraph 5); slow wave = Vm minus its high-pass\n  (2nd order Butterworth at 10 Hz, zero phase), slow-wave peaks and troughs with prominence 1 mV and\n  minimum distance 1/maxBurstFreq, spikes as peaks of the high-passed trace with prominence of at\n  least minSpikeHeight, amplitude = peak minus trough, troughs and peaks paired in order\n  (analyzeWaveform.m). maxBurstFreq and minSpikeHeight take the code's starting values (2 Hz and 10\n  mV for PD, 10 Hz and 3 mV for LP; intracellularAnalysis.m), which the authors adjusted by hand.\n  Minimum membrane potential: Methods reading, the minimum of the unfiltered Vm between successive\n  slow-wave peaks (per second when there are none); code reading, the slow-wave troughs, and in a\n  bin with none, the mean of the per-second minima of the slow wave (pHCumulativePTX.m). PD burst\n  frequency from trough-to-trough intervals (Methods; peak-to-peak in the code, a variant). LP\n  firing rate = 1 / interspike interval. Six 10 s bins; empty bins of frequency or amplitude are 0.\n- [RM] and [MIX]: `rm_anova` and `mixed_anova` fit the multivariate linear model of car::Anova\n  (orthonormal within-subject contrasts) and give the univariate F (sphericity assumed, as\n  statistics.R reads `univariate.tests`) and Pillai's trace for the multivariate reading.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport json\nimport re\nimport urllib.request\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport fsspec\nimport numpy as np\nimport pandas as pd\nimport pyabf\nfrom scipy import signal, stats\n\nimport r7aes_files\n\nOSF_NODE = \"r7aes\"\nPUBLISHED_VERSION = r7aes_files.PUBLISHED_VERSION\nFILES = r7aes_files.table()\n\nSTG_EXPERIMENTS = [\"877_093\", \"877_101\", \"877_121\", \"877_127\", \"877_141\", \"887_005\", \"887_049\",\n                   \"887_069\", \"887_097\", \"887_105\", \"887_137\", \"887_141\", \"887_145\", \"897_005\",\n                   \"897_037\"]\nCG_UNITS = [(\"877_149\", \"CG1L\"), (\"877_149\", \"CG2L\"), (\"887_005\", \"CG2L\"), (\"887_011\", \"CG3L\"),\n            (\"887_017\", \"CG3L\"), (\"887_061\", \"CG1L\"), (\"887_065\", \"CG2L\"), (\"887_073\", \"CG2L\"),\n            (\"887_093\", \"CG2L\"), (\"887_127\", \"CG1L\"), (\"887_149\", \"CG1L\"), (\"887_149\", \"CG2L\"),\n            (\"897_041\", \"CG1L\"), (\"897_041\", \"CG3L\"), (\"897_041\", \"CG7L\")]\nPTX_EXPERIMENTS = [\"903_046\", \"903_048\", \"903_050\", \"903_052\", \"903_054\", \"903_056\", \"903_058\",\n                   \"903_060\", \"903_064\"]\nSTG_EXAMPLE, CG_EXAMPLE = \"897_037\", (\"877_149\", \"CG2L\")\n\n# The code's 13 columns (pHCumulative.m, pH_vars).\nCOLUMNS = [\"rec_acid\", \"5.5\", \"6.1\", \"6.7\", \"7.2\", \"ctl_acid\", \"ctl_base\", \"8.3\", \"8.8\", \"9.3\",\n           \"9.8\", \"10.4\", \"rec_base\"]\nACID = [\"5.5\", \"6.1\", \"6.7\", \"7.2\", \"ctl_acid\"]\nBASE = [\"ctl_base\", \"8.3\", \"8.8\", \"9.3\", \"9.8\", \"10.4\"]\nACID_STEPS, BASE_STEPS = [\"7.2\", \"6.7\", \"6.1\", \"5.5\"], [\"8.3\", \"8.8\", \"9.3\", \"9.8\", \"10.4\"]\n\nWINDOW_S, BIN_S = 480, 10           # paper, Methods: last 8 min, 10 s bins\nINTRA_S = 60                        # paper, Methods: last minute\nCODE_WINDOW_S = 600                 # kept from the start of each file for the code's window variant\nHIGHPASS_HZ = 100.0                 # standard choice for extracellular spikes\nNOISE_K = 6.0                       # assumption: threshold at least 6 robust SDs of noise\nAMP_FRAC, AMP_PCTL = 0.35, 99.0     # assumption: unit followed at 35% of its control amplitude\nMAX_ISI_S, MIN_SPIKES = 0.3, 2      # spikenburst.s2s starting values\nMAX_SPIKES = {\"STG\": 15, \"CG\": 30}  # extracellularAnalysis.m\nMAX_DUTY = 0.4                      # extracellularAnalysis.m\nRHYTHM_GAP_FACTOR = 3.0             # assumption for the [STATE] proxy\nMIN_STATE_S = 10                    # paper, Methods paragraph 3\nINTRA_PARAMS = {\"PD\": (2.0, 10.0), \"LP\": (10.0, 3.0)}   # intracellularAnalysis.m starting values\nWAVE_HP_HZ = 10.0                   # analyzeWaveform.m\n\n\n# ----------------------------------------------------------------------------------------------\n# Reading\n\ndef url(path):\n    f = FILES[path]\n    return f\"https://osf.io/download/{f['key']}/?version={f['version']}\"\n\n\ndef open_file(path):\n    \"\"\"An fsspec file of a pinned file, with its size from the target list (docs/archives.md).\"\"\"\n    return fsspec.filesystem(\"http\").open(url(path), block_size=2**20, size=FILES[path][\"size\"])\n\n\ndef read_text(path):\n    data = open_file(path).read()\n    assert hashlib.sha256(data).hexdigest() == FILES[path][\"sha256\"], path\n    return data.decode()\n\n\ndef abf_header(fh, path):\n    \"\"\"pyabf's header readers applied to an open stream (pyabf.ABF itself wants a local path).\"\"\"\n    a = pyabf.ABF.__new__(pyabf.ABF)\n    a.abfFilePath, a.abfID, a.abfFolderPath = path, path, \"\"\n    a._preLoadData, a._cacheStimulusFiles, a.stimulusFileFolder = False, False, None\n    fh.seek(0)\n    sig = fh.read(4)\n    fh.seek(0)\n    a.abfVersion = {\"major\": 2 if sig == b\"ABF2\" else 1}\n    (a._readHeadersV2 if sig == b\"ABF2\" else a._readHeadersV1)(fh)\n    return a\n\n\ndef header_info(path):\n    with open_file(path) as fh:\n        a = abf_header(fh, path)\n    n = a.dataPointCount // a.channelCount\n    return dict(path=path, rate=a.dataRate, nch=a.channelCount, channels=list(a.adcNames),\n                units=list(a.adcUnits), seconds=n / a.dataRate, start=a.abfDateTime,\n                dtype_bytes=a.dataPointByteSize)\n\n\ndef stream_abf(path, keep, whole=True, chunk_mb=32):\n    \"\"\"Read an ABF file and keep windows of chosen channels.\n\n    keep: {channel: [(t0, t1), ...]} with times in seconds, negative counting from the end.\n    whole: read the whole file and check its SHA-256; otherwise read only the windows.\n    Returns (dict channel -> list of float32 arrays, header info, sha256 ok or None).\n    \"\"\"\n    with open_file(path) as fh:\n        a = abf_header(fh, path)\n        nch, rate = a.channelCount, a.dataRate\n        assert a.dataPointByteSize == 2\n        n = a.dataPointCount // nch\n        idx = {c: a.adcNames.index(c) for c in keep}\n        wins = {}\n        for c, ws in keep.items():\n            wins[c] = []\n            for t0, t1 in ws:\n                i0 = int(round((t0 if t0 >= 0 else n / rate + t0) * rate))\n                i1 = int(round((t1 if t1 > 0 else n / rate + t1) * rate)) if t1 is not None else n\n                wins[c].append((max(0, i0), min(n, i1)))\n        out = {c: [np.empty(i1 - i0, np.float32) for i0, i1 in wins[c]] for c in keep}\n        gain = {c: a._dataGain[idx[c]] for c in keep}\n        offs = {c: a._dataOffset[idx[c]] for c in keep}\n\n        def take(raw, f0):\n            f1 = f0 + raw.shape[0]\n            for c in keep:\n                for k, (i0, i1) in enumerate(wins[c]):\n                    lo, hi = max(i0, f0), min(i1, f1)\n                    if lo < hi:\n                        out[c][k][lo - i0:hi - i0] = raw[lo - f0:hi - f0, idx[c]] * gain[c] + offs[c]\n\n        ok = None\n        if whole:\n            h = hashlib.sha256()\n            fh.seek(0)\n            head = fh.read(a.dataByteStart)\n            h.update(head)\n            frame = nch * 2\n            step = max(1, (chunk_mb << 20) // frame) * frame\n            f0, left = 0, n * frame\n            while left > 0:\n                buf = fh.read(min(step, left))\n                if not buf:\n                    break\n                h.update(buf)\n                usable = len(buf) - len(buf) % frame\n                raw = np.frombuffer(buf[:usable], np.int16).reshape(-1, nch)\n                take(raw, f0)\n                f0 += raw.shape[0]\n                left -= len(buf)\n            h.update(fh.read())\n            ok = h.hexdigest() == FILES[path][\"sha256\"]\n        else:\n            spans = sorted({w for c in wins for w in wins[c]})\n            for i0, i1 in spans:\n                fh.seek(a.dataByteStart + i0 * nch * 2)\n                raw = np.frombuffer(fh.read((i1 - i0) * nch * 2), np.int16).reshape(-1, nch)\n                take(raw, i0)\n    info = dict(path=path, rate=rate, seconds=n / rate, channels=list(a.adcNames),\n                units=list(a.adcUnits))\n    return out, info, ok\n\n\n# ----------------------------------------------------------------------------------------------\n# Experiments, conditions and channels\n\ndef parse_readme(text):\n    files = re.findall(r\"(\\S+\\.abf):\\s*pH\\s*([\\d.]+)\", text)\n    elec = re.findall(r\"^(IN \\d+|extra\\d+|Vm[\\w_]*|ME\\d_Vx):\\s*(.+?)\\s*$\", text, flags=re.M)\n    notes = text.split(\"Notes:\")[1].strip() if \"Notes:\" in text else \"\"\n    return [(f, p) for f, p in files], [(k, v) for k, v in elec], notes\n\n\ndef experiment_files(exp):\n    return sorted(p for p in FILES if p.startswith(exp + \"/\") and p.endswith(\".abf\"))\n\n\ndef protocol_columns(seq):\n    \"\"\"Map an ordered list of (file, pH label) to the code's 13 columns.\n\n    Consecutive files at 7.8 form one control block; the block between the two step protocols is\n    both the recovery from the first and the control before the second. A pH repeated within a\n    protocol (887_061 steps back up through 6.1 to 7.2) keeps its first file. Returns\n    ({column: file}, order \"AB\" or \"BA\").\n    \"\"\"\n    blocks, cur = [], None\n    for f, p in seq:\n        kind = \"ctl\" if p == \"7.8\" else (\"acid\" if float(p) < 7.8 else \"base\")\n        if cur is None or cur[0] != kind:\n            cur = (kind, [])\n            blocks.append(cur)\n        cur[1].append((f, p))\n    kinds = [k for k, _ in blocks]\n    steps = [k for k in kinds if k != \"ctl\"]\n    order = \"AB\" if steps and steps[0] == \"acid\" else \"BA\"\n    cols = {}\n    ctl_blocks = [b for k, b in blocks if k == \"ctl\"]\n    for k, b in blocks:\n        if k in (\"acid\", \"base\"):\n            for f, p in b:\n                cols.setdefault(p, f)\n    first, middle, last = (ctl_blocks + [None, None, None])[:3]\n    pick = lambda b: None if not b else b[-1][0]\n    if order == \"AB\":\n        cols[\"ctl_acid\"], cols[\"rec_acid\"], cols[\"ctl_base\"], cols[\"rec_base\"] = (\n            pick(first), pick(middle), pick(middle), pick(last))\n    else:\n        cols[\"ctl_base\"], cols[\"rec_base\"], cols[\"ctl_acid\"], cols[\"rec_acid\"] = (\n            pick(first), pick(middle), pick(middle), pick(last))\n    return {c: cols.get(c) for c in COLUMNS}, order\n\n\ndef control_block_files(seq):\n    return [f for f, p in seq if p == \"7.8\"]\n\n\ndef assign_ptx_conditions(ph_values):\n    \"\"\"pH labels for a PTX folder (no README) from the bath pH channel of each file.\n\n    ph_values: list of (file, mean pH electrode signal in mV over the last minute). Files within\n    `tol` mV of the first file are control (7.8); a run of files above (acid) or below (base) is\n    labelled by its estimated pH, 7.8 minus the change from the preceding control over a slope of\n    0.82 x 56.4 mV per pH unit (the Nernst slope at 11 C, scaled to the electrode's response\n    between the 7.8 and the extreme solutions in the complete runs), taken to the nearest nominal\n    step. Returns list of (file, label, estimated pH).\n    \"\"\"\n    ctl = ph_values[0][1]\n    tol, slope = 10.0, 0.82 * 56.4\n    out, last_ctl = [], ctl\n    for f, v in ph_values:\n        if abs(v - ctl) < tol:\n            out.append((f, \"7.8\", 7.8))\n            last_ctl = v\n            continue\n        est = 7.8 - (v - last_ctl) / slope\n        nominal = ACID_STEPS if est < 7.8 else BASE_STEPS\n        lab = min(nominal, key=lambda s: abs(float(s) - est))\n        out.append((f, lab, est))\n    return out\n\n\n# ----------------------------------------------------------------------------------------------\n# Spikes, bursts and binned measures\n\ndef highpass(x, fs, hz=HIGHPASS_HZ):\n    sos = signal.butter(2, hz, \"highpass\", fs=fs, output=\"sos\")\n    return signal.sosfiltfilt(sos, x.astype(np.float64)).astype(np.float32)\n\n\ndef events(x, fs, polarity=None, k=4.0):\n    \"\"\"Peaks of the high-passed trace above k robust SDs: times (s), heights, noise SD, polarity.\"\"\"\n    y = highpass(x, fs)\n    sd = float(np.median(np.abs(y)) / 0.6745)\n    if polarity is None:\n        polarity = -1 if -np.percentile(y, 0.01) > np.percentile(y, 99.99) else 1\n    pk, pr = signal.find_peaks(polarity * y, height=k * sd, distance=max(1, int(0.003 * fs)))\n    return pk / fs, pr[\"peak_heights\"].astype(np.float32), sd, polarity\n\n\ndef bursts_from_spikes(t, max_isi=MAX_ISI_S, min_spikes=MIN_SPIKES):\n    \"\"\"Group spikes with intervals up to max_isi; keep groups of at least min_spikes.\n    Returns DataFrame: tstart, tend, spikes, duration, period, hz, duty (readSpikeOutput.m).\"\"\"\n    if len(t) == 0:\n        return pd.DataFrame(columns=[\"tstart\", \"tend\", \"spikes\", \"duration\", \"period\", \"hz\", \"duty\"])\n    brk = np.where(np.diff(t) > max_isi)[0]\n    starts = np.r_[0, brk + 1]\n    ends = np.r_[brk, len(t) - 1]\n    n = ends - starts + 1\n    keep = n >= min_spikes\n    b = pd.DataFrame({\"tstart\": t[starts[keep]], \"tend\": t[ends[keep]], \"spikes\": n[keep]})\n    b[\"duration\"] = b.tend - b.tstart\n    b[\"period\"] = b.tstart.diff()\n    b[\"hz\"] = 1 / b.period\n    b[\"duty\"] = b.duration / b.period\n    return b.reset_index(drop=True)\n\n\ndef burst_bins(b, t0, ganglion, nbins=WINDOW_S // BIN_S):\n    \"\"\"48 bin means of hz, spikes and duty from t0, with the code's discards; empty bins are 0.\"\"\"\n    b = b.copy()\n    b.loc[b.duty > MAX_DUTY, \"duty\"] = np.nan\n    b.loc[b.spikes > MAX_SPIKES[ganglion], \"spikes\"] = np.nan\n    rel = b.tstart.to_numpy() - t0\n    out = {}\n    for m in [\"hz\", \"spikes\", \"duty\"]:\n        v = b[m].to_numpy(dtype=float)\n        vals = np.zeros(nbins)\n        for i in range(nbins):\n            sel = (rel >= BIN_S * i) & (rel < BIN_S * (i + 1))\n            if sel.any() and np.isfinite(v[sel]).any():\n                vals[i] = np.nanmean(v[sel])\n        out[m] = vals\n    return out\n\n\ndef rhythmic_seconds(onsets, t0, t1, max_gap):\n    \"\"\"Per second in [t0, t1): 1 when the second lies between two burst onsets at most max_gap\n    apart, then runs shorter than MIN_STATE_S merged into the state before them.\"\"\"\n    n = int(round(t1 - t0))\n    r = np.zeros(n, bool)\n    on = np.asarray(onsets)\n    for a, b in zip(on[:-1], on[1:]):\n        if b - a <= max_gap:\n            i0, i1 = int(np.floor(a - t0)), int(np.ceil(b - t0))\n            r[max(0, i0):max(0, min(n, i1))] = True\n    # merge runs shorter than MIN_STATE_S\n    s = r.copy()\n    i = 0\n    while i < n:\n        j = i\n        while j < n and r[j] == r[i]:\n            j += 1\n        if j - i < MIN_STATE_S and i > 0:\n            s[i:j] = s[i - 1]\n        i = j\n    return s\n\n\n# ----------------------------------------------------------------------------------------------\n# Intracellular\n\ndef waveform(vm, fs, unit):\n    \"\"\"[INTRA] measures of one minute of Vm (analyzeWaveform.m, with the Methods' minimum).\"\"\"\n    max_burst_hz, min_spike = INTRA_PARAMS[unit]\n    b, a = signal.butter(2, WAVE_HP_HZ, \"highpass\", fs=fs)\n    vm = vm.astype(np.float64)\n    spk = signal.filtfilt(b, a, vm)\n    wave = vm - spk\n    dist = max(1, int(fs / max_burst_hz))\n    p1, _ = signal.find_peaks(wave, distance=dist, prominence=1)\n    p2, _ = signal.find_peaks(-wave, distance=dist, prominence=1)\n    p3, _ = signal.find_peaks(spk, prominence=min_spike)\n    p4, _ = signal.find_peaks(-spk, prominence=min_spike)\n    nw, ns = min(len(p1), len(p2)), min(len(p3), len(p4))\n    secs = int(len(vm) // fs)\n    per_sec_wave = np.array([wave[int(i * fs):int((i + 1) * fs)].min() for i in range(secs)])\n    per_sec_raw = np.array([vm[int(i * fs):int((i + 1) * fs)].min() for i in range(secs)])\n    # Methods: minimum of the unfiltered Vm between successive slow-wave peaks\n    if len(p1) >= 2:\n        between = [(p1[i] + np.argmin(vm[p1[i]:p1[i + 1]])) for i in range(len(p1) - 1)]\n        raw_min_t = np.array(between) / fs\n        raw_min_v = vm[np.array(between)]\n    else:\n        raw_min_t, raw_min_v = np.array([]), np.array([])\n    return dict(\n        wave_t=p1[:nw] / fs, wave_max=wave[p1[:nw]], wave_min=wave[p2[:nw]],\n        wave_amp=wave[p1[:nw]] - wave[p2[:nw]],\n        trough_t=p2 / fs, trough_v=wave[p2], peak_t=p1 / fs,\n        spike_t=p3[:ns] / fs, spike_amp=spk[p3[:ns]] - spk[p4[:ns]],\n        raw_min_t=raw_min_t, raw_min_v=raw_min_v,\n        per_sec_wave=per_sec_wave, per_sec_raw=per_sec_raw, mean_vm=float(vm.mean()))\n\n\ndef _bin6(t, v, empty):\n    out = np.zeros(INTRA_S // BIN_S)\n    for i in range(len(out)):\n        sel = (t >= BIN_S * i) & (t < BIN_S * (i + 1))\n        out[i] = np.nanmean(v[sel]) if sel.any() else (empty(i) if callable(empty) else empty)\n    return out\n\n\ndef intra_measures(w):\n    \"\"\"Per preparation values (means of six 10 s bins) of one unit's [INTRA] measures.\"\"\"\n    sec_mean = lambda arr: (lambda i: float(np.mean(arr[BIN_S * i:BIN_S * (i + 1)])))\n    r = {}\n    r[\"vmin_methods\"] = _bin6(w[\"raw_min_t\"], w[\"raw_min_v\"], sec_mean(w[\"per_sec_raw\"])).mean()\n    r[\"vmin_code\"] = _bin6(w[\"trough_t\"], w[\"trough_v\"], sec_mean(w[\"per_sec_wave\"])).mean()\n    r[\"spike_amp\"] = _bin6(w[\"spike_t\"], w[\"spike_amp\"], 0.0).mean()\n    tt = w[\"trough_t\"]\n    r[\"burst_hz_trough\"] = _bin6(tt[1:], 1 / np.diff(tt), 0.0).mean() if len(tt) > 1 else 0.0\n    pt = w[\"wave_t\"]\n    r[\"burst_hz_peak\"] = _bin6(pt[:-1], 1 / np.diff(pt), 0.0).mean() if len(pt) > 1 else 0.0\n    st = w[\"spike_t\"]\n    r[\"spike_hz\"] = _bin6(st[:-1], 1 / np.diff(st), 0.0).mean() if len(st) > 1 else 0.0\n    r[\"wave_amp\"] = _bin6(w[\"wave_t\"], w[\"wave_amp\"], 0.0).mean()\n    r[\"n_spikes\"] = len(st)\n    r[\"n_waves\"] = len(pt)\n    r[\"mean_vm\"] = w[\"mean_vm\"]\n    return r\n\n\n# ----------------------------------------------------------------------------------------------\n# Statistics\n\ndef _orth_contrasts(k):\n    c = np.zeros((k, k - 1))\n    for j in range(1, k):\n        c[:j, j - 1] = 1\n        c[j, j - 1] = -j\n    return c / np.linalg.norm(c, axis=0)\n\n\ndef _mlm_tests(Y, X, L):\n    \"\"\"Within-subject tests of a multivariate linear model Y ~ X for hypothesis L on B (rows of\n    X's coefficients), with orthonormal contrasts over Y's columns. Returns univariate F, df1, df2,\n    p (sphericity assumed) and Pillai's trace with its F approximation.\"\"\"\n    n, k = Y.shape\n    C = _orth_contrasts(k)\n    Z = Y @ C\n    XtX_inv = np.linalg.pinv(X.T @ X)\n    B = XtX_inv @ X.T @ Z\n    R = Z - X @ B\n    E = R.T @ R\n    dfe = n - np.linalg.matrix_rank(X)\n    LB = L @ B\n    H = LB.T @ np.linalg.pinv(L @ XtX_inv @ L.T) @ LB\n    q, p = L.shape[0], k - 1\n    F = (np.trace(H) / (q * p)) / (np.trace(E) / (dfe * p))\n    df1, df2 = q * p, dfe * p\n    pu = stats.f.sf(F, df1, df2)\n    ev = np.real(np.linalg.eigvals(H @ np.linalg.pinv(E)))\n    V = float(np.sum(ev / (1 + ev)))\n    s, m_, nn = min(p, q), (abs(p - q) - 1) / 2, (dfe - p - 1) / 2\n    Fp = (2 * nn + s + 1) / (2 * m_ + s + 1) * V / (s - V) if s - V > 0 else np.inf\n    d1, d2 = s * (2 * m_ + s + 1), s * (2 * nn + s + 1)\n    return dict(F=F, df1=df1, df2=df2, p=pu, pillai=V, F_pillai=Fp, p_pillai=stats.f.sf(Fp, d1, d2) if d2 > 0 else np.nan)\n\n\ndef rm_anova(df, cols):\n    \"\"\"One-way repeated-measures ANOVA over the columns (rows with any NaN dropped).\"\"\"\n    Y = df[cols].dropna().to_numpy(float)\n    X = np.ones((len(Y), 1))\n    r = _mlm_tests(Y, X, np.array([[1.0]]))\n    r[\"n\"] = len(Y)\n    return r\n\n\ndef posthoc_paired(df, control, steps, factor):\n    rows = []\n    for s in steps:\n        d = df[[control, s]].dropna()\n        t, p = stats.ttest_rel(d[control], d[s])\n        rows.append(dict(step=s, n=len(d), mean_control=d[control].mean(), mean_step=d[s].mean(),\n                         diff=d[s].mean() - d[control].mean(), t=t, p=p, p_corr=min(1.0, p * factor)))\n    return pd.DataFrame(rows)\n\n\ndef rm_family(df, label=\"\"):\n    \"\"\"[RM]: acid and base ANOVAs and the corrected paired t-tests against each control.\"\"\"\n    a, b = rm_anova(df, ACID), rm_anova(df, BASE)\n    ta = posthoc_paired(df, \"ctl_acid\", ACID_STEPS, 4)\n    tb = posthoc_paired(df, \"ctl_base\", BASE_STEPS, 5)\n    return a, b, pd.concat([ta, tb], ignore_index=True)\n\n\ndef mixed_anova(df_a, df_b, cols, coding=\"sum\"):\n    \"\"\"[MIX]: ganglion (between, two groups) by pH (within). Returns a table of the univariate and\n    multivariate tests of pH, ganglion and their interaction under the given contrast coding.\"\"\"\n    Ya, Yb = df_a[cols].dropna().to_numpy(float), df_b[cols].dropna().to_numpy(float)\n    Y = np.vstack([Ya, Yb])\n    g = np.r_[np.zeros(len(Ya)), np.ones(len(Yb))]\n    if coding == \"sum\":\n        X = np.c_[np.ones(len(Y)), np.where(g == 0, 1.0, -1.0)]\n    else:   # R's treatment coding, first level (alphabetical: CG) as reference\n        X = np.c_[np.ones(len(Y)), g]\n    ph = _mlm_tests(Y, X, np.array([[1.0, 0.0]]))\n    inter = _mlm_tests(Y, X, np.array([[0.0, 1.0]]))\n    # between-subject effect of ganglion on the mean over conditions (independent of coding)\n    m = Y.mean(axis=1)\n    fg, pg = stats.f_oneway(m[g == 0], m[g == 1])\n    return dict(pH=ph, interaction=inter, ganglion=dict(F=fg, df1=1, df2=len(Y) - 2, p=pg),\n                n=(len(Ya), len(Yb)))\n\n\n# ----------------------------------------------------------------------------------------------\n# The OSF listing\n\ndef osf_listing():\n    \"\"\"Every file in the project's OSF Storage now, walked through the API (docs/archives.md).\"\"\"\n    def get(u):\n        with urllib.request.urlopen(u) as r:\n            return json.load(r)\n    rows = []\n    prov = get(f\"https://api.osf.io/v2/nodes/{OSF_NODE}/files/\")\n    todo = [p[\"relationships\"][\"files\"][\"links\"][\"related\"][\"href\"] for p in prov[\"data\"]]\n    providers = [p[\"attributes\"][\"provider\"] for p in prov[\"data\"]]\n    while todo:\n        u = todo.pop()\n        while u:\n            page = get(u + (\"&\" if \"?\" in u else \"?\") + \"page[size]=100\" if \"page[size]\" not in u else u)\n            for it in page[\"data\"]:\n                at = it[\"attributes\"]\n                if at[\"kind\"] == \"folder\":\n                    todo.append(it[\"relationships\"][\"files\"][\"links\"][\"related\"][\"href\"])\n                else:\n                    rows.append(dict(path=at[\"materialized_path\"].lstrip(\"/\"), provider=at[\"provider\"],\n                                     version=at.get(\"current_version\"), size=at[\"size\"],\n                                     sha256=(at.get(\"extra\") or {}).get(\"hashes\", {}).get(\"sha256\")))\n            u = page[\"links\"].get(\"next\")\n    return pd.DataFrame(rows), providers\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Testing the OSF listing walk and the ANOVA code against pingouin.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, numpy as np, pandas as pd, pingouin as pg
import crabph as C
t=time.time(); L,prov=C.osf_listing(); print(prov, len(L), round(time.time()-t,1),'s')
m=L.set_index('path')
bad=[p for p,f in C.FILES.items() if p not in m.index or m.loc[p,'version']!=f['version'] or m.loc[p,'sha256']!=f['sha256'] or m.loc[p,'size']!=f['size']]
print('mismatch',bad, 'extra', sorted(set(m.index)-set(C.FILES)))
rng=np.random.default_rng(0)
Y=rng.normal(size=(12,5))+np.arange(5)*0.3
df=pd.DataFrame(Y,columns=C.ACID)
print(C.rm_anova(df,C.ACID))
long=df.reset_index().melt(id_vars='index')
print(pg.rm_anova(long,dv='value',within='variable',subject='index',correction=False))
Y2=rng.normal(size=(10,5))
long2=pd.concat([df.assign(g='STG'),pd.DataFrame(Y2,columns=C.ACID).assign(g='CG')]).reset_index(drop=True).reset_index().melt(id_vars=['index','g'])
print(pg.mixed_anova(long2,dv='value',within='variable',between='g',subject='index',correction=False))
print(C.mixed_anova(df,pd.DataFrame(Y2,columns=C.ACID),C.ACID,'sum'))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "entries/haley-2018/crabph.py", line 536, in osf_listing
    page = get(u + ("&" if "?" in u else "?") + "page[size]=100" if "page[size]" not in u else u)
  File "entries/haley-2018/crabph.py", line 527, in get
    with urllib.request.urlopen(u) as r:
         ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 495, in open
    response = meth(req, response)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 533, in error
    return self._call_chain(*args)
           ~~~~~~~~~~~~~~~~^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 466, in _call_chain
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import urllib.request,json
for u in ["https://api.osf.io/v2/nodes/r7aes/files/","https://api.osf.io/v2/nodes/r7aes/files/osfstorage/?page%5Bsize%5D=100"]:
    for ua in [None,"Mozilla/5.0 encore-registry"]:
        try:
            req=urllib.request.Request(u,headers={"User-Agent":ua} if ua else {})
            d=json.load(urllib.request.urlopen(req)); print(u,ua,'ok',len(d['data']))
        except Exception as e: print(u,ua,e)
EOF
```

```
https://api.osf.io/v2/nodes/r7aes/files/ None ok 2
https://api.osf.io/v2/nodes/r7aes/files/ Mozilla/5.0 encore-registry ok 2
https://api.osf.io/v2/nodes/r7aes/files/osfstorage/?page%5Bsize%5D=100 None ok 32
https://api.osf.io/v2/nodes/r7aes/files/osfstorage/?page%5Bsize%5D=100 Mozilla/5.0 encore-registry ok 32
```

**Agent**

Two storage providers, not one. Fixing the URL encoding and checking which providers there are.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import re
s=open('crabph.py').read()
s=s.replace('''            page = get(u + ("&" if "?" in u else "?") + "page[size]=100" if "page[size]" not in u else u)''','''            page = get(u if "page" in u else u + ("&" if "?" in u else "?") + "page%5Bsize%5D=100")''')
open('crabph.py','w').write(s)
import urllib.request,json
d=json.load(urllib.request.urlopen("https://api.osf.io/v2/nodes/r7aes/files/"))
for p in d['data']: print(p['attributes']['provider'], p['attributes']['name'])
EOF
```

```
Exit code 1
osfstorage osfstorage
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
KeyError: 'name'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import urllib.request,json
d=json.load(urllib.request.urlopen("https://api.osf.io/v2/nodes/r7aes/files/"))
for p in d['data']: print(json.dumps(p['attributes'])[:400], p['relationships']['files']['links']['related']['href'])
EOF
```

```
{"kind": "folder", "name": "osfstorage", "path": "/", "node": "r7aes", "provider": "osfstorage"} https://api.osf.io/v2/nodes/r7aes/files/osfstorage/
{"kind": "folder", "path": "/", "node": "r7aes", "provider": "github"} https://api.osf.io/v2/nodes/r7aes/files/github/
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import urllib.request,json
try:
    d=json.load(urllib.request.urlopen("https://api.osf.io/v2/nodes/r7aes/files/github/"))
    print(len(d['data'])); [print(x['attributes']['materialized_path'], x['attributes'].get('size')) for x in d['data']]
except Exception as e: print(e)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, crabph as C
t=time.time(); L,prov=C.osf_listing(); print(prov, len(L), round(time.time()-t,1),'s', L.provider.value_counts().to_dict())
m=L[L.provider=='osfstorage'].set_index('path')
bad=[p for p,f in C.FILES.items() if p not in m.index or m.loc[p,'version']!=f['version'] or m.loc[p,'sha256']!=f['sha256'] or m.loc[p,'size']!=f['size']]
print('mismatch',bad, 'extra', sorted(set(m.index)-set(C.FILES)))
print(L[L.provider!='osfstorage'])
EOF
```

```
Exit code 1
HTTP Error 403: Forbidden
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "entries/haley-2018/crabph.py", line 536, in osf_listing
    page = get(u if "page" in u else u + ("&" if "?" in u else "?") + "page%5Bsize%5D=100")
  File "entries/haley-2018/crabph.py", line 527, in get
    with urllib.request.urlopen(u) as r:
         ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 495, in open
    response = meth(req, response)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 533, in error
    return self._call_chain(*args)
           ~~~~~~~~~~~~~~~~^^^^^^^
[... 5 more lines not kept]
```

**Agent**

The GitHub add-on listing returns 403 to an anonymous reader. I'll record that per provider and walk OSF Storage.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
old=s[s.index('    rows = []\n    prov = get('):s.index('    return pd.DataFrame(rows), providers')]
new='''    rows, providers = [], {}
    prov = get(f"https://api.osf.io/v2/nodes/{OSF_NODE}/files/")
    for p in prov["data"]:
        name = p["attributes"]["provider"]
        todo = [p["relationships"]["files"]["links"]["related"]["href"]]
        try:
            while todo:
                u = todo.pop()
                while u:
                    page = get(u if "page" in u else u + ("&" if "?" in u else "?") + "page%5Bsize%5D=100")
                    for it in page["data"]:
                        at = it["attributes"]
                        if at["kind"] == "folder":
                            todo.append(it["relationships"]["files"]["links"]["related"]["href"])
                        else:
                            rows.append(dict(path=at["materialized_path"].lstrip("/"), provider=name,
                                             version=at.get("current_version"), size=at["size"],
                                             sha256=(at.get("extra") or {}).get("hashes", {}).get("sha256")))
                    u = page["links"].get("next")
            providers[name] = "listed"
        except urllib.error.HTTPError as e:
            providers[name] = f"HTTP {e.code} {e.reason}"
'''
s=s.replace(old,new).replace("import urllib.request\n","import urllib.error\nimport urllib.request\n")
open('crabph.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, crabph as C, numpy as np, pandas as pd, pingouin as pg
t=time.time(); L,prov=C.osf_listing(); print(prov, len(L), round(time.time()-t,1),'s')
m=L[L.provider=='osfstorage'].set_index('path')
bad=[p for p,f in C.FILES.items() if p not in m.index or m.loc[p,'version']!=f['version'] or m.loc[p,'sha256']!=f['sha256'] or m.loc[p,'size']!=f['size']]
print('mismatch',bad, 'extra', sorted(set(m.index)-set(C.FILES)))
rng=np.random.default_rng(0)
Y=rng.normal(size=(12,5))+np.arange(5)*0.3
df=pd.DataFrame(Y,columns=C.ACID)
print(C.rm_anova(df,C.ACID))
long=df.reset_index().melt(id_vars='index')
print(pg.rm_anova(long,dv='value',within='variable',subject='index',correction=False)[['F','p-unc']])
Y2=rng.normal(size=(10,5))
long2=pd.concat([df.assign(g='STG'),pd.DataFrame(Y2,columns=C.ACID).assign(g='CG')]).reset_index(drop=True).reset_index().melt(id_vars=['index','g'])
print(pg.mixed_anova(long2,dv='value',within='variable',between='g',subject='index',correction=False)[['Source','F','p-unc']])
print(C.mixed_anova(pd.DataFrame(Y2,columns=C.ACID),df,C.ACID,'sum'))
EOF
```

```
Exit code 1
{'osfstorage': 'HTTP 500 Internal Server Error', 'github': 'HTTP 500 Internal Server Error'} 12 32.9 s
mismatch ['877_093/877_093_0001.abf', '877_093/877_093_0002.abf', '877_093/877_093_0003.abf', '877_093/877_093_0004.abf', '877_093/877_093_0005.abf', '877_093/877_093_0006.abf', '877_093/877_093_0007.abf', '877_093/877_093_0008.abf', '877_093/877_093_0009.abf', '877_093/877_093_0010.abf', '877_093/877_093_0011.abf', '877_093/README.txt', '877_101/877_101_0000.abf', '877_101/877_101_0001.abf', '877_101/877_101_0002.abf', '877_101/877_101_0003.abf', '877_101/877_101_0004.abf', '877_101/877_101_0005.abf', '877_101/877_101_0006.abf', '877_101/877_101_0007.abf', '877_101/877_101_0008.abf', '877_101/877_101_0009.abf', '877_101/877_101_0010.abf', '877_101/877_101_0011.abf', '877_101/README.txt', '877_121/877_121_0004.abf', '877_121/877_121_0005.abf', '877_121/877_121_0006.abf', '877_121/877_121_0007.abf', '877_121/877_121_0008.abf', '877_121/877_121_0009.abf', '877_121/877_121_0010.abf', '877_121/877_121_0011.abf', '877_121/877_121_0012.abf', '877_121/877_121_0013.abf', '877_121/877_121_0014.abf', '877_121/877_121_0015.abf', '877_121/README.txt', '877_141/877_141_0001.abf', '877_141/877_141_0002.abf', '877_141/877_141_0003.abf', '877_141/877_141_0004.abf', '877_141/877_141_0005.abf', '877_141/877_141_0006.abf', '877_141/877_141_0007.abf', '877_141/877_141_0008.abf', '877_141/877_141_0009.abf', '877_141/877_141_0010.abf', '877_141/877_141_0011.abf', '877_141/877_141_0012.abf', '877_141/README.txt', '877_149/877_149_0001.abf', '877_149/877_149_0002.abf', '877_149/877_149_0003.abf', '877_149/877_149_0004.abf', '877_149/877_149_0006.abf', '877_149/877_149_0007.abf', '877_149/877_149_0008.abf', '877_149/877_149_0009.abf', '877_149/877_149_0010.abf', '877_149/877_149_0011.abf', '877_149/877_149_0012.abf', '877_149/877_149_0013.abf', '877_149/README.txt', '887_005/887_005_0001.abf', '887_005/887_005_0002.abf', '887_005/887_005_0003.abf', '887_005/887_005_0004.abf', '
[... 16 more lines not kept]
```

**Agent**

The OSF API now returns 500 (it may be throttling after my many requests). I'll add retries and report a failed listing as not checked. Finishing the ANOVA comparison.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
s=s.replace('''    def get(u):
        with urllib.request.urlopen(u) as r:
            return json.load(r)''','''    def get(u):
        for attempt in range(6):
            try:
                with urllib.request.urlopen(u, timeout=60) as r:
                    return json.load(r)
            except urllib.error.HTTPError as e:
                if e.code < 500 or attempt == 5:
                    raise
                time.sleep(5 * 2 ** attempt)''').replace("import re\n","import re\nimport time\n")
open('crabph.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import crabph as C, numpy as np, pandas as pd, pingouin as pg
rng=np.random.default_rng(0)
Y=rng.normal(size=(12,5))+np.arange(5)*0.3
df=pd.DataFrame(Y,columns=C.ACID)
long=df.reset_index().melt(id_vars='index')
print(pg.rm_anova(long,dv='value',within='variable',subject='index',correction=False).iloc[:, :8])
Y2=rng.normal(size=(10,5))
long2=pd.concat([df.assign(g='STG'),pd.DataFrame(Y2,columns=C.ACID).assign(g='CG')]).reset_index(drop=True).reset_index().melt(id_vars=['index','g'])
print(pg.mixed_anova(long2,dv='value',within='variable',between='g',subject='index',correction=False).iloc[:, :8])
r=C.mixed_anova(pd.DataFrame(Y2,columns=C.ACID),df,C.ACID,'sum')
print({k:(round(v['F'],4),v['p']) for k,v in r.items() if k!='n'})
r=C.mixed_anova(pd.DataFrame(Y2,columns=C.ACID),df,C.ACID,'treatment')
print({k:(round(v['F'],4),v['p']) for k,v in r.items() if k!='n'})
EOF
```

```
Source  ddof1  ddof2        F     p_unc       ng2       eps
0  variable      4     44  5.51204  0.001097  0.252607  0.832455
        Source         SS  DF1  DF2         MS         F     p_unc       np2
0            g  11.524368    1   20  11.524368  9.194162  0.006581  0.314932
1     variable  11.624322    4   80   2.906081  3.462035  0.011630  0.147559
2  Interaction  14.255260    4   80   3.563815  4.245599  0.003624  0.175108
{'pH': (np.float64(3.3054), np.float64(0.014697831859808164)), 'interaction': (np.float64(4.2456), np.float64(0.0036241600236471662)), 'ganglion': (np.float64(9.1942), np.float64(0.006580763397373696))}
{'pH': (np.float64(2.9925), np.float64(0.02347387287654809)), 'interaction': (np.float64(4.2456), np.float64(0.0036241600236471476)), 'ganglion': (np.float64(9.1942), np.float64(0.006580763397373696))}
```

**Agent calls Bash**

```bash
cat >> entries/haley-2018/crabph.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# The experiments as the READMEs and the recorded pH describe them

def abf_channel(readme_key, names):
    """The ABF channel a README electrode key names ("Vm1_1" is VM1 in files that have no VM1_1)."""
    k = readme_key.upper() if readme_key.lower().startswith("vm") else readme_key
    if k in names:
        return k
    if k.endswith("_1") and k[:-2] in names:
        return k[:-2]
    return None


def describe_experiment(exp):
    """README of an STG or CG experiment: ordered (file, pH) and electrodes."""
    text = read_text(f"{exp}/README.txt")
    files, elec, notes = parse_readme(text)
    return dict(exp=exp, files=files, electrodes=elec, notes=notes, text=text)


def pd_channel(desc, names):
    for k, v in desc["electrodes"]:
        if v.strip().lower() == "pdn" and abf_channel(k, names):
            return abf_channel(k, names)
    return None


def intra_channels(desc, names):
    out = {}
    for k, v in desc["electrodes"]:
        if v.strip() in ("PD", "LP") and abf_channel(k, names):
            out.setdefault(v.strip(), abf_channel(k, names))
    return out


def cg_channel(desc, unit, names):
    want = unit[:-1]       # "CG2L" -> "CG2"
    for k, v in desc["electrodes"]:
        if v.split()[0] == want and abf_channel(k, names):
            return abf_channel(k, names)
    return None


def ph_channel(names):
    return next(c for c in names if c.lower() == "ph") if any(c.lower() == "ph" for c in names) else None


def process_file(job):
    """Stream one file; return spike events of the extracellular channels in the analysis windows,
    the last minute of the intracellular channels reduced to [INTRA] measures, and the pH signal."""
    path, ext, intra, whole = job["path"], job["ext"], job["intra"], job["whole"]
    info = header_info(path)
    names = info["channels"]
    keep = {}
    for c in ext:
        keep[c] = [(0, min(CODE_WINDOW_S, info["seconds"])), (-WINDOW_S, None)]
    for unit, c in intra.items():
        keep.setdefault(c, [])
        keep[c] = keep[c] + [(-INTRA_S, None)]
    phc = ph_channel(names)
    if phc:
        keep.setdefault(phc, [])
        keep[phc] = keep[phc] + [(-INTRA_S, None)]
    data, info, ok = stream_abf(path, keep, whole=whole)
    fs = info["rate"]
    res = dict(path=path, seconds=info["seconds"], rate=fs, sha_ok=ok, ext={}, intra={}, ph=None)
    for c in ext:
        early, late = data[c][0], data[c][1]
        e0 = events(early, fs)
        e1 = events(late, fs, polarity=e0[3])
        res["ext"][c] = dict(early=(e0[0], e0[1]), late=(e1[0] + info["seconds"] - len(late) / fs, e1[1]),
                             sd_early=e0[2], sd_late=e1[2], polarity=e0[3], late_start=info["seconds"] - len(late) / fs)
    for unit, c in intra.items():
        vm = data[c][-1]
        res["intra"][unit] = intra_measures(waveform(vm, fs, unit))
        res["intra"][unit]["channel"] = c
    if phc:
        res["ph"] = float(np.mean(data[phc][-1]))
    return res


def run_jobs(jobs, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(process_file, jobs))


def unit_threshold(ref_heights, sd, heights):
    """Spike threshold of one file: the larger of NOISE_K x noise, AMP_FRAC x the file's AMP_PCTL
    height, and half of AMP_FRAC x the unit's control AMP_PCTL height."""
    big = heights[heights >= NOISE_K * sd]
    p_file = np.percentile(big, AMP_PCTL) if len(big) >= 20 else 0.0
    return max(NOISE_K * sd, AMP_FRAC * p_file, 0.5 * AMP_FRAC * ref_heights)


def unit_measures(results_by_file, channel, columns, ganglion, ref_file):
    """Per condition column: bins of the Methods window and of the code window, rhythmic seconds,
    burst table, thresholds. results_by_file: {file path: process_file result}."""
    r0 = results_by_file[ref_file]["ext"][channel]
    sd0 = r0["sd_late"]
    h0 = r0["late"][1]
    big0 = h0[h0 >= NOISE_K * sd0]
    ref = np.percentile(big0, AMP_PCTL) if len(big0) else 0.0
    out = {}
    ctl_period = None
    for col in COLUMNS:
        f = columns.get(col)
        if f is None or f not in results_by_file:
            out[col] = None
            continue
        r = results_by_file[f]["ext"][channel]
        sec = results_by_file[f]["seconds"]
        thr = unit_threshold(ref, r["sd_late"], r["late"][1])
        t_late = r["late"][0][r["late"][1] >= thr]
        b_late = bursts_from_spikes(np.sort(t_late))
        thr_e = unit_threshold(ref, r["sd_early"], r["early"][1])
        t_early = r["early"][0][r["early"][1] >= thr_e]
        b_early = bursts_from_spikes(np.sort(t_early))
        t0 = r["late_start"]
        bins = burst_bins(b_late, t0, ganglion)
        if len(b_early):
            code_bins = burst_bins(b_early, b_early.tstart.iloc[0], ganglion)
        else:
            code_bins = {m: np.zeros(WINDOW_S // BIN_S) for m in ["hz", "spikes", "duty"]}
        out[col] = dict(file=f, seconds=sec, thr=thr, sd=r["sd_late"], n_spikes=len(t_late),
                        bursts=b_late, bins=bins, code_bins=code_bins,
                        window_s=min(WINDOW_S, sec))
    first = columns.get("ctl_acid") if columns.get("ctl_acid") == ref_file else columns.get("ctl_base")
    ctl = out.get("ctl_acid") if out.get("ctl_acid") and out["ctl_acid"]["file"] == ref_file else out.get("ctl_base")
    ctl_period = float(np.nanmedian(ctl["bursts"]["period"])) if ctl and len(ctl["bursts"]) > 2 else np.nan
    for col, v in out.items():
        if v is None:
            continue
        gap = RHYTHM_GAP_FACTOR * ctl_period if np.isfinite(ctl_period) else 0
        sec = v["seconds"]
        v["rhythmic"] = rhythmic_seconds(v["bursts"]["tstart"].to_numpy(), sec - v["window_s"], sec, gap)
    return out, ref, ctl_period
EOF
```

```
(Bash completed with no output)
```

**Agent**

Testing on one CG experiment (877_149) and one STG experiment (877_141), timed.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import sys, time, resource, numpy as np, pandas as pd
sys.path.insert(0,'entries/haley-2018')
import crabph as C
pd.set_option('display.width',250)
t=time.time()
exps={'877_149':[('CG','CG1L'),('CG','CG2L')],'877_141':[('STG','PD')]}
jobs=[];descs={}
for e,units in exps.items():
    d=C.describe_experiment(e); descs[e]=d
    names=C.header_info(f"{e}/{d['files'][0][0]}")['channels']
    for f,ph in d['files']:
        path=f"{e}/{f}" if f"{e}/{f}" in C.FILES else None
        if path is None: print('missing',e,f); continue
        nm=C.header_info(path)['channels']
        ext=[]
        for g,u in units:
            ext.append(C.pd_channel(d,nm) if g=='STG' else C.cg_channel(d,u,nm))
        jobs.append(dict(path=path,ext=sorted(set(ext)),intra=C.intra_channels(d,nm) if any(g=='STG' for g,_ in units) else {},whole=True))
print(len(jobs), [j['ext'] for j in jobs][:3])
res=C.run_jobs(jobs, workers=12)
print('time',time.time()-t,'maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
import pickle; pickle.dump((descs,res),open('t1.pkl','wb'))
print([r['sha_ok'] for r in res])
EOF
python t1.py
```

```
missing 877_149 877_149_00010.abf
23 [['IN 11', 'IN 13'], ['IN 11', 'IN 13'], ['IN 11', 'IN 13']]
time 54.890036821365356 maxrss MB 2511.46
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
Shell cwd was reset to
```

**Agent**

Hashes match for all 23 files; about 65 MB/s. The full STG and CG set (57 GB) should take about 15 min. Now checking the burst measures.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/haley-2018')
import crabph as C
descs,res=pickle.load(open('t1.pkl','rb'))
R={r['path']:r for r in res}
def fixname(e,f):
    p=f"{e}/{f}"
    if p in C.FILES: return p
    n=int(f.rsplit('_',1)[1].split('.')[0]); 
    for q in C.experiment_files(e):
        if int(q.rsplit('_',1)[1].split('.')[0])==n: return q
for e,units in [('877_149',['CG1L','CG2L']),('877_141',['PD'])]:
    d=descs[e]; seq=[(fixname(e,f),p) for f,p in d['files']]
    cols,order=C.protocol_columns(seq)
    print(e,order,{k:(v.split('_')[-1] if v else None) for k,v in cols.items()})
    for u in units:
        nm=R[seq[0][0]]['ext'].keys()
        ch=C.pd_channel(d,R[seq[0][0]] and C.header_info(seq[0][0])['channels']) if u=='PD' else C.cg_channel(d,u,C.header_info(seq[0][0])['channels'])
        out,ref,cp=C.unit_measures(R,ch,cols,'STG' if u=='PD' else 'CG',seq[0][0])
        print(u,ch,'ref',ref,'ctl period',cp)
        rows=[]
        for col in C.COLUMNS:
            v=out[col]
            if v is None: rows.append(dict(col=col)); continue
            rows.append(dict(col=col,thr=v['thr'],sd=v['sd'],nsp=v['n_spikes'],nb=len(v['bursts']),hz=v['bins']['hz'].mean(),spikes=v['bins']['spikes'].mean(),duty=v['bins']['duty'].mean(),hz_code=v['code_bins']['hz'].mean(),rhy=v['rhythmic'].mean(), med_spk=v['bursts'].spikes.median()))
        print(pd.DataFrame(rows).round(3).to_string())
    for f,_ in seq:
        if f in R and R[f]['intra']: print(f, {u:{k:round(float(x),2) for k,x in m.items() if k!='channel'} for u,m in R[f]['intra'].items()}, R[f]['ph'])
EOF
python t2.py
```

```
Exit code 1
877_149 AB {'rec_acid': '0007.abf', '5.5': '0006.abf', '6.1': '0004.abf', '6.7': '0003.abf', '7.2': '0002.abf', 'ctl_acid': '0001.abf', 'ctl_base': '0007.abf', '8.3': '0008.abf', '8.8': '0009.abf', '9.3': '0010.abf', '9.8': '0011.abf', '10.4': '0012.abf', 'rec_base': '0013.abf'}
CG1L IN 13 ref 0.20553179 ctl period 3.832200000000057
         col    thr     sd     nsp     nb     hz  spikes   duty  hz_code    rhy  med_spk
0   rec_acid  0.679  0.005   114.0    3.0  0.000   0.521  0.000    0.123  0.000      8.0
1        5.5  0.713  0.005   760.0   48.0  0.091  14.229  0.058    0.076  0.769     15.0
2        6.1  0.771  0.005   340.0   80.0  0.204   3.858  0.036    0.174  0.862      3.0
3        6.7  0.781  0.005   155.0   23.0  0.055   1.104  0.009    0.001  0.194      3.0
4        7.2  0.398  0.005    32.0    2.0  0.037   0.083  0.001    0.000  0.000      4.0
5   ctl_acid  0.072  0.005   657.0  122.0  0.326   2.429  0.058    0.342  1.000      2.0
6   ctl_base  0.679  0.005   114.0    3.0  0.000   0.521  0.000    0.123  0.000      8.0
7        8.3  0.696  0.005   243.0   28.0  0.039   3.094  0.012    0.007  0.115      4.0
8        8.8  0.678  0.005   343.0   34.0  0.057   6.500  0.033    0.048  0.200     10.5
9        9.3    NaN    NaN     NaN    NaN    NaN     NaN    NaN      NaN    NaN      NaN
10       9.8  0.579  0.005   602.0   69.0  0.146   8.865  0.098    0.123  0.996      8.0
11      10.4  0.544  0.005   206.0   55.0  0.106   2.208  0.025    0.155  0.619      3.0
12  rec_base  0.496  0.006  1047.0   98.0  0.215  10.990  0.122    0.079  0.994     12.0
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 19, in <module>
    out,ref,cp=C.unit_measures(R,ch,cols,'STG' if u=='PD' else 'CG',seq[0][0])
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, pickle, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
descs,res=pickle.load(open('t1.pkl','rb'))
fig,axs=plt.subplots(3,1,figsize=(14,10))
for ax,(exp,ch) in zip(axs,[('877_149','IN 13'),('877_149','IN 11'),('877_141','IN 9')]):
    rs=[r for r in res if r['path'].startswith(exp) and ch in r['ext']]
    for i,r in enumerate(sorted(rs,key=lambda r:r['path'])):
        h=r['ext'][ch]['late'][1]
        ax.scatter(np.full(len(h),i)+np.random.uniform(-.3,.3,len(h)),h,s=1,alpha=.3)
        ax.text(i,0.001,r['path'][-8:-4]+f"\n{len(h)}",fontsize=7)
    ax.set_yscale('log'); ax.set_title(f'{exp} {ch}')
plt.tight_layout(); plt.savefig('h.png',dpi=65)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/h.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd entries/haley-2018 && . $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
old=s[s.index('def unit_threshold('):s.index('def unit_measures(')]
new='''def otsu_log(heights, bins=100):
    """Otsu's two-class split of log10 event heights; returns the threshold height."""
    x = np.log10(heights)
    hist, edges = np.histogram(x, bins=bins)
    mids = (edges[:-1] + edges[1:]) / 2
    w = np.cumsum(hist)
    m = np.cumsum(hist * mids)
    tot, mt = w[-1], m[-1]
    w0, w1 = w[:-1], tot - w[:-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        between = (mt * w0 / tot - m[:-1]) ** 2 / (w0 * w1 / tot)
    between = np.nan_to_num(between)
    return 10 ** edges[1:-1][np.argmax(between)]


def unit_threshold(sd, heights, floor):
    """Spike threshold of one file: the larger of NOISE_K x noise, the Otsu split of the log event
    heights (the unit against noise and smaller units), and the floor (FLOOR_FRAC x the unit's
    median spike height in its control file), so that smaller units are not taken for a unit that
    has fallen silent. An assumption: the paper set thresholds by hand."""
    big = heights[heights >= OTSU_MIN_K * sd]
    split = otsu_log(big) if len(big) >= 20 else 0.0
    return max(NOISE_K * sd, split, floor)


'''
s=s.replace(old,new)
s=s.replace('''NOISE_K = 6.0                       # assumption: threshold at least 6 robust SDs of noise
AMP_FRAC, AMP_PCTL = 0.35, 99.0     # assumption: unit followed at 35% of its control amplitude''','''NOISE_K = 6.0                       # assumption: threshold at least 6 robust SDs of noise
OTSU_MIN_K = 4.0                    # events taken into the height split
FLOOR_FRAC = 0.4                    # assumption: floor at 40% of the unit's control spike height''')
old=s[s.index('    r0 = results_by_file[ref_file]["ext"][channel]'):s.index('    out = {}\n    ctl_period = None')]
new='''    r0 = results_by_file[ref_file]["ext"][channel]
    h0 = r0["late"][1]
    thr0 = unit_threshold(r0["sd_late"], h0, 0.0)
    ref = float(np.median(h0[h0 >= thr0])) if (h0 >= thr0).any() else 0.0
    floor = FLOOR_FRAC * ref
'''
s=s.replace(old,new)
s=s.replace('thr = unit_threshold(ref, r["sd_late"], r["late"][1])','thr = unit_threshold(r["sd_late"], r["late"][1], floor)')
s=s.replace('thr_e = unit_threshold(ref, r["sd_early"], r["early"][1])','thr_e = unit_threshold(r["sd_early"], r["early"][1], floor)')
old=s[s.index('def cg_channel('):s.index('def ph_channel(')]
new='''def cg_channel(desc, unit, names_per_file):
    """The trunk channel of a CG unit: the first README electrode for "CGn (trunk)" that every file
    of the experiment holds."""
    want = unit[:-1]       # "CG2L" -> "CG2"
    for k, v in desc["electrodes"]:
        if v.split()[0] == want and all(abf_channel(k, n) for n in names_per_file):
            return abf_channel(k, names_per_file[0])
    return None


'''
s=s.replace(old,new)
old=s[s.index('def pd_channel('):s.index('def intra_channels(')]
new='''def pd_channel(desc, names_per_file):
    """The pdn channel (the PD unit, pHCumulative.m) that every file of the experiment holds."""
    for k, v in desc["electrodes"]:
        if v.strip().lower() == "pdn" and all(abf_channel(k, n) for n in names_per_file):
            return abf_channel(k, names_per_file[0])
    return None


'''
s=s.replace(old,new)
open('crabph.py','w').write(s)
EOF
grep -n "AMP_" crabph.py
```

```
28:  absolute deviation / 0.6745) and `AMP_FRAC` times the `AMP_PCTL` percentile of the event heights
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/haley-2018/crabph.py",
 "old_string": "  `HIGHPASS_HZ` (a standard choice for extracellular spikes), the polarity is that of the larger\n  extreme, and the threshold of a file is the larger of `NOISE_K` times the robust noise (median\n  absolute deviation / 0.6745) and `AMP_FRAC` times the `AMP_PCTL` percentile of the event heights\n  of the unit in its first control file, so that a unit is followed across files while the smaller\n  units (the Small Cells on the CG trunk) stay under it.",
 "new_string": "  `HIGHPASS_HZ` (a standard choice for extracellular spikes), the polarity is that of the larger\n  extreme, and the threshold of a file is the largest of `NOISE_K` times the robust noise (median\n  absolute deviation / 0.6745), Otsu's split of the log heights of the events above `OTSU_MIN_K`\n  noise SDs (the unit against noise and smaller units, such as the Small Cells on the CG trunk),\n  and `FLOOR_FRAC` times the unit's median spike height in its first control file, so that smaller\n  units are not counted when the unit falls silent."
}
```

```
The file entries/haley-2018/crabph.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
s=open('t2.py').read()
s=s.replace("""        nm=R[seq[0][0]]['ext'].keys()
        ch=C.pd_channel(d,R[seq[0][0]] and C.header_info(seq[0][0])['channels']) if u=='PD' else C.cg_channel(d,u,C.header_info(seq[0][0])['channels'])""","""        nmf=[C.header_info(f)['channels'] for f,_ in seq if f]
        ch=C.pd_channel(d,nmf) if u=='PD' else C.cg_channel(d,u,nmf)
        if ch not in R[seq[0][0]]['ext']: print('skip',u,ch); continue""")
open('t2.py','w').write(s)
EOF
python t2.py
```

```
Exit code 1
877_149 AB {'rec_acid': '0007.abf', '5.5': '0006.abf', '6.1': '0004.abf', '6.7': '0003.abf', '7.2': '0002.abf', 'ctl_acid': '0001.abf', 'ctl_base': '0007.abf', '8.3': '0008.abf', '8.8': '0009.abf', '9.3': '0010.abf', '9.8': '0011.abf', '10.4': '0012.abf', 'rec_base': '0013.abf'}
CG1L IN 13 ref 0.08394312113523483 ctl period 3.661299999999983
         col    thr     sd     nsp     nb     hz  spikes   duty  hz_code    rhy  med_spk
0   rec_acid  0.286  0.005   123.0    4.0  0.001   0.729  0.000    0.309  0.000      6.5
1        5.5  0.285  0.005  1309.0   48.0  0.091  21.250  0.058    0.076  0.654     27.0
2        6.1  0.317  0.005   384.0   80.0  0.204   4.601  0.039    0.391  0.825      3.0
3        6.7  0.105  0.005   695.0  111.0  0.267   5.938  0.060    0.233  0.996      5.0
4        7.2  0.124  0.005    32.0    2.0  0.037   0.083  0.001    0.000  0.000      4.0
5   ctl_acid  0.049  0.005   674.0  125.0  0.323   2.425  0.059    0.342  1.000      2.0
6   ctl_base  0.286  0.005   123.0    4.0  0.001   0.729  0.000    0.309  0.000      6.5
7        8.3  0.172  0.005   546.0  112.0  0.293   4.299  0.027    0.257  0.894      2.0
8        8.8  0.169  0.005   918.0   62.0  0.134   4.969  0.055    0.477  0.473      4.0
9        9.3    NaN    NaN     NaN    NaN    NaN     NaN    NaN      NaN    NaN      NaN
10       9.8  0.107  0.005  2926.0   69.0  0.146   8.667  0.104    0.140  0.996     39.0
11      10.4  0.099  0.005   931.0  110.0  0.249   8.712  0.047    0.190  0.998      6.5
12  rec_base  0.097  0.006  4794.0   98.0  0.215   5.448  0.138    0.288  0.994     55.0
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 20, in <module>
    out,ref,cp=C.unit_measures(R,ch,cols,'STG' if u=='PD' else 'CG',seq[0][0])
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> crabph.py <<'EOF'


def resolve_file(exp, name):
    """The folder's file for a README file name; a name the folder lacks is matched by its number
    (877_149's README lists 877_149_00010.abf, the folder holds 877_149_0010.abf), else None."""
    p = f"{exp}/{name}"
    if p in FILES:
        return p
    try:
        n = int(name.rsplit("_", 1)[1].split(".")[0])
    except (IndexError, ValueError):
        return None
    hits = [q for q in experiment_files(exp) if int(q.rsplit("_", 1)[1].split(".")[0]) == n]
    return hits[0] if len(hits) == 1 else None


def pick_controls(seq, seconds):
    """Within each block of consecutive 7.8 files keep the last one of at least 8 min (else the
    longest), so that the 8 min window lies in one file."""
    out, block = [], []
    def flush():
        if block:
            long = [f for f, _ in block if seconds.get(f, 0) >= WINDOW_S]
            keep = long[-1] if long else max(block, key=lambda x: seconds.get(x[0], 0))[0]
            out.append((keep, "7.8"))
    for f, p in seq:
        if p == "7.8":
            block.append((f, p))
        else:
            flush()
            block = []
            out.append((f, p))
    flush()
    return out


def plan_extracellular(stg=STG_EXPERIMENTS, cg=CG_UNITS):
    """Per experiment present in the project: README, file sequence, condition columns, channels.
    Returns (plans, missing experiments, file jobs)."""
    folders = {p.split("/")[0] for p in FILES}
    exps = sorted(set(stg) | {e for e, _ in cg})
    plans, missing = {}, []
    for e in exps:
        if e not in folders:
            missing.append(e)
            continue
        d = describe_experiment(e)
        seq_raw = [(resolve_file(e, f), p) for f, p in d["files"]]
        heads = {f: header_info(f) for f, _ in seq_raw if f}
        seconds = {f: h["seconds"] for f, h in heads.items()}
        seq = pick_controls([(f, p) for f, p in seq_raw if f], seconds)
        cols, order = protocol_columns(seq)
        names = [heads[f]["channels"] for f, _ in seq]
        units = {}
        if e in stg:
            units["PD"] = ("STG", pd_channel(d, names))
        for ee, u in cg:
            if ee == e:
                units[u] = ("CG", cg_channel(d, u, names))
        intra = {}
        if e in stg:
            for unit in ("PD", "LP"):
                chans = [intra_channels(d, n).get(unit) for n in names]
                if chans and all(chans) and len(set(chans)) == 1:
                    intra[unit] = chans[0]
        plans[e] = dict(desc=d, seq_raw=seq_raw, seq=seq, columns=cols, order=order, units=units,
                        intra=intra, heads=heads, unlisted=[f for f in experiment_files(e)
                                                            if f not in {x for x, _ in seq_raw}])
    jobs = []
    for e, pl in plans.items():
        ext = sorted({c for _, c in pl["units"].values() if c})
        for f, _ in pl["seq"]:
            jobs.append(dict(path=f, ext=ext, intra=pl["intra"], whole=True))
    return plans, missing, jobs


def ptx_job(path):
    """A PTX file: the last minute of the PD and LP intracellular channels, the pdn and the pH."""
    names = header_info(path)["channels"]
    intra = {u: next(c for c in names if c.upper().startswith(u)) for u in ("PD", "LP")
             if any(c.upper().startswith(u) for c in names)}
    return dict(path=path, ext=[], intra=intra, whole=False,
                pdn="pdn" if "pdn" in names else None)


def process_ptx(job):
    """Last minute of a PTX file: [INTRA] measures of PD and LP, the pH signal, and the fraction of
    PD intracellular spikes that fall within 5 ms of a pdn spike (a check of the PD label)."""
    path, intra = job["path"], job["intra"]
    keep = {c: [(-INTRA_S, None)] for c in intra.values()}
    names = header_info(path)["channels"]
    phc = ph_channel(names)
    keep[phc] = [(-INTRA_S, None)]
    if job["pdn"]:
        keep["pdn"] = [(-INTRA_S, None)]
    data, info, _ = stream_abf(path, keep, whole=False)
    fs = info["rate"]
    res = dict(path=path, seconds=info["seconds"], channels=names, intra={}, ph=float(np.mean(data[phc][0])))
    ws = {}
    for unit, c in intra.items():
        w = waveform(data[c][0], fs, unit)
        ws[unit] = w
        res["intra"][unit] = intra_measures(w)
        res["intra"][unit]["channel"] = c
    if job["pdn"]:
        t, h, sd, pol = events(data["pdn"][0], fs, k=NOISE_K)
        for unit, w in ws.items():
            st = w["spike_t"]
            if len(st) and len(t):
                j = np.searchsorted(t, st)
                d = np.minimum(np.abs(t[np.clip(j, 0, len(t) - 1)] - st), np.abs(t[np.clip(j - 1, 0, len(t) - 1)] - st))
                res["intra"][unit]["pdn_match"] = float(np.mean(d < 0.005))
            else:
                res["intra"][unit]["pdn_match"] = np.nan
    return res
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, crabph as C
t=time.time()
plans,missing,jobs=C.plan_extracellular()
print('missing',missing, len(jobs), round(time.time()-t,1),'s')
for e,p in plans.items():
    print(e,p['order'],{k:v for k,v in p['units'].items()},p['intra'],'unlisted',[u[-8:] for u in p['unlisted']], 'cols missing',[c for c,v in p['columns'].items() if v is None])
EOF
```

```
missing ['877_127', '887_017'] 274 264.2 s
877_093 BA {'PD': ('STG', 'IN 12')} {'PD': 'VM1_2', 'LP': 'VM1'} unlisted [] cols missing ['5.5']
877_101 AB {'PD': ('STG', None)} {} unlisted [] cols missing []
877_121 AB {'PD': ('STG', 'IN 13')} {} unlisted [] cols missing []
877_141 AB {'PD': ('STG', 'IN 9')} {'PD': 'VM1_2'} unlisted [] cols missing []
877_149 AB {'CG1L': ('CG', 'IN 13'), 'CG2L': ('CG', 'IN 11')} {} unlisted [] cols missing []
887_005 BA {'PD': ('STG', 'IN 13'), 'CG2L': ('CG', 'IN 11')} {'PD': 'VM1', 'LP': 'VM1_2'} unlisted [] cols missing ['10.4']
887_011 BA {'CG3L': ('CG', 'IN 11')} {} unlisted ['0001.abf'] cols missing ['10.4']
887_049 AB {'PD': ('STG', 'IN 11')} {'PD': 'VM1', 'LP': 'VM1_2'} unlisted ['0026.abf'] cols missing []
887_061 AB {'CG1L': ('CG', 'IN 12')} {} unlisted [] cols missing []
887_065 AB {'CG2L': ('CG', 'IN 13')} {} unlisted [] cols missing []
887_069 AB {'PD': ('STG', 'IN 11')} {'PD': 'VM1_1'} unlisted [] cols missing ['5.5']
887_073 BA {'CG2L': ('CG', 'IN 12')} {} unlisted [] cols missing []
887_093 AB {'CG2L': ('CG', 'IN 12')} {} unlisted [] cols missing []
887_097 BA {'PD': ('STG', 'IN 13')} {} unlisted [] cols missing []
887_105 BA {'PD': ('STG', 'IN 13')} {} unlisted [] cols missing []
887_127 AB {'CG1L': ('CG', 'IN 8')} {} unlisted [] cols missing []
887_137 AB {'PD': ('STG', 'IN 11')} {'PD': 'VM1_1'} unlisted [] cols missing []
887_141 BA {'PD': ('STG', 'extra5')} {'LP': 'ME3_Vx'} unlisted [] cols missing []
887_145 AB {'PD': ('STG', 'extra1')} {'PD': 'ME1_Vx'} unlisted [] cols missing []
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/haley-2018 && . $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
old='''    folders = {p.split("/")[0] for p in FILES}
    exps = sorted(set(stg) | {e for e, _ in cg})
    plans, missing = {}, []
    for e in exps:
        if e not in folders:
            missing.append(e)
            continue
        d = describe_experiment(e)
        seq_raw = [(resolve_file(e, f), p) for f, p in d["files"]]
        heads = {f: header_info(f) for f, _ in seq_raw if f}
'''
new='''    folders = {p.split("/")[0] for p in FILES}
    exps = sorted(set(stg) | {e for e, _ in cg})
    plans, missing = {}, [e for e in exps if e not in folders]
    exps = [e for e in exps if e in folders]
    with ThreadPoolExecutor(16) as ex:
        descs = dict(zip(exps, ex.map(describe_experiment, exps)))
        paths = sorted({resolve_file(e, f) for e in exps for f, _ in descs[e]["files"]} - {None})
        all_heads = dict(zip(paths, ex.map(header_info, paths)))
    for e in exps:
        d = descs[e]
        seq_raw = [(resolve_file(e, f), p) for f, p in d["files"]]
        heads = {f: all_heads[f] for f, _ in seq_raw if f}
'''
assert old in s
s=s.replace(old,new)
open('crabph.py','w').write(s)
EOF
cd $TMPDIR && cat > full.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/haley-2018')
import crabph as C
t=time.time()
plans,missing,jobs=C.plan_extracellular()
print('plan',round(time.time()-t,1)); sys.stdout.flush()
res=C.run_jobs(jobs, workers=12)
print('ext',round(time.time()-t,1),'maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3); sys.stdout.flush()
pickle.dump((plans,missing,jobs,res),open('full_ext.pkl','wb'))
ptx=[p for e in C.PTX_EXPERIMENTS for p in C.experiment_files(e)]
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(12) as ex:
    pj=list(ex.map(C.ptx_job,ptx)); pr=list(ex.map(C.process_ptx,pj))
print('ptx',round(time.time()-t,1),'maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
pickle.dump((pj,pr),open('full_ptx.pkl','wb'))
EOF
timeout 3000 python full.py 2>&1 | tail -20
```

```
Thu Nov 26 01:33:44 UTC 2026
plan 25.1
ext 507.5 maxrss MB 3305.888
ptx 568.8 maxrss MB 3305.888
Shell cwd was reset to
```

**Agent**

Full extraction finished in 9.5 min with a 3.3 GB memory peak: 274 STG and CG files read whole, and the last minute of the 106 PTX files. Now checking hashes, conditions and the PTX pH assignment.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/haley-2018')
import crabph as C
plans,missing,jobs,res=pickle.load(open('full_ext.pkl','rb'))
pj,pr=pickle.load(open('full_ptx.pkl','rb'))
print('sha ok', sum(r['sha_ok'] for r in res), 'of', len(res), [r['path'] for r in res if not r['sha_ok']])
# PTX conditions
for e in C.PTX_EXPERIMENTS:
    rs=[r for r in pr if r['path'].startswith(e)]
    lab=C.assign_ptx_conditions([(r['path'],r['ph']) for r in rs])
    print(e, ' '.join(f"{f[-8:-4]}:{l}({est:.2f},{r['seconds']/60:.0f}m)" for (f,l,est),r in zip(lab,rs)))
    print('   chans', {r['path'][-8:-4]:(r['intra'].get('PD',{}).get('channel'),round(r['intra'].get('PD',{}).get('pdn_match',np.nan),2),r['intra'].get('LP',{}).get('channel'),round(r['intra'].get('LP',{}).get('pdn_match',np.nan),2)) for r in rs})
EOF
```

```
sha ok 274 of 274 []
903_046 0002:7.8(7.80,22m) 0005:7.2(7.05,9m) 0006:6.7(6.46,10m) 0008:5.5(5.38,10m) 0010:7.8(7.80,6m) 0011:8.3(8.27,10m) 0012:8.8(8.71,10m) 0013:9.3(9.23,10m) 0014:9.8(9.70,10m) 0015:10.4(10.16,11m) 0016:7.8(7.80,8m)
   chans {'0002': ('PD4', nan, 'LP3', 0.62), '0005': ('PD3', 0.61, 'LP4', 0.14), '0006': ('PD3', 0.31, 'LP4', 0.1), '0008': ('PD3', nan, 'LP4', nan), '0010': ('PD3', 0.73, 'LP4', 0.15), '0011': ('PD3', 0.63, 'LP4', 0.13), '0012': ('PD3', 0.47, 'LP4', 0.09), '0013': ('PD3', 0.12, 'LP4', 0.25), '0014': ('PD3', 0.65, 'LP4', 0.14), '0015': ('PD3', 0.61, 'LP4', 0.15), '0016': ('PD3', 0.41, 'LP4', 0.16)}
903_048 0003:7.8(7.80,41m) 0004:8.3(8.27,11m) 0006:8.8(8.72,10m) 0007:9.3(9.25,10m) 0008:9.8(9.69,10m) 0009:10.4(10.13,10m) 0010:7.8(7.80,31m) 0011:7.2(7.16,12m) 0012:6.7(6.58,10m) 0013:6.1(5.98,10m) 0014:5.5(5.48,10m) 0015:7.8(7.80,34m)
   chans {'0003': ('PD4', 0.3, 'LP1', 0.1), '0004': ('PD4', 0.55, 'LP1', 0.1), '0006': ('PD4', 0.41, 'LP1', 0.08), '0007': ('PD4', 0.68, 'LP1', 0.04), '0008': ('PD4', 0.49, 'LP1', 0.0), '0009': ('PD4', 0.22, 'LP1', 0.2), '0010': ('PD4', 0.53, 'LP1', 0.09), '0011': ('PD4', 0.47, 'LP1', 0.15), '0012': ('PD4', 0.18, 'LP1', 0.19), '0013': ('PD4', nan, 'LP1', nan), '0014': ('PD4', nan, 'LP1', 0.04), '0015': ('PD4', 0.12, 'LP1', 0.06)}
903_050 0003:7.8(7.80,35m) 0004:7.2(7.13,11m) 0005:6.7(6.51,10m) 0006:6.1(5.92,10m) 0007:5.5(5.41,14m) 0008:7.8(7.80,30m) 0009:8.3(8.28,11m) 0010:8.8(8.74,10m) 0011:9.3(9.27,10m) 0012:9.8(9.75,10m) 0013:10.4(10.21,10m) 0014:7.8(7.80,11m) 0015:7.8(7.80,22m)
   chans {'0003': ('PD3', 0.03, 'LP4', 0.12), '0004': ('PD3', 0.05, 'LP4', 0.12), '0005': ('PD3', 0.12, 'LP4', 0.14), '0006': ('PD3', 0.04, 'LP4', 0.14), '0007': ('PD3', nan, 'LP4', nan), '0008': ('PD3', 0.12, 'LP4', 0.08), '0009': ('PD3', 0.49, 'LP4', 0.1), '0010': ('PD3', 0.36, 'LP4', 0.09), '0011': ('PD3', 0.13, 'LP4', nan), '0012': ('PD3', 0.23, 'LP4', nan), '0013': ('PD3', 0.48, 'LP4', nan), '0014': ('PD3', 0.36, 'LP4', 0.0
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/haley-2018 && . $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
old=s[s.index('    ctl = ph_values[0][1]\n    tol, slope'):s.index('# ----------------------------------------------------------------------------------------------\n# Spikes, bursts')]
new='''    ctl = ph_values[0][1]
    tol, slope = 10.0, 0.82 * 56.4
    est, last_ctl = [], ctl
    for f, v in ph_values:
        if abs(v - ctl) < tol:
            est.append((f, None, 7.8))
            last_ctl = v
        else:
            est.append((f, "run", 7.8 - (v - last_ctl) / slope))
    out, i = [], 0
    while i < len(est):
        if est[i][1] is None:
            out.append((est[i][0], "7.8", 7.8))
            i += 1
            continue
        j = i
        while j < len(est) and est[j][1] == "run":
            j += 1
        run = est[i:j]
        nominal = ACID_STEPS if run[0][2] < 7.8 else BASE_STEPS
        if len(run) == len(nominal):     # a complete run: steps by rank of the measured pH
            ranked = sorted(run, key=lambda r: -r[2] if nominal is ACID_STEPS else r[2])
            lab = {r[0]: s for r, s in zip(ranked, nominal)}
            out += [(f, lab[f], e) for f, _, e in run]
        else:                            # a step missing: nearest nominal step
            out += [(f, min(nominal, key=lambda s: abs(float(s) - e)), e) for f, _, e in run]
        i = j
    return out


'''
s=s.replace(old,new)
s=s.replace('''    labelled by its estimated pH, 7.8 minus the change from the preceding control over a slope of
    0.82 x 56.4 mV per pH unit (the Nernst slope at 11 C, scaled to the electrode's response
    between the 7.8 and the extreme solutions in the complete runs), taken to the nearest nominal
    step.''','''    a run of four acid or five base files takes the nominal steps in the order of its measured pH;
    a shorter run takes for each file the nominal step nearest its estimated pH, 7.8 minus the
    change from the preceding control over 0.82 x 56.4 mV per pH unit (the Nernst slope at 11 C,
    scaled to the electrode's response between 7.8 and the extreme solutions in complete runs).''')
old=s[s.index('def ptx_job(path):'):s.index('def process_ptx(job):')]
new='''def ptx_jobs(exp):
    """The files of a PTX experiment, each with its PD and LP intracellular channels. The channels
    are chosen by input position, with the label most files of the experiment give that position
    (903_046_0002 names the two electrodes the other way round from the other ten files)."""
    paths = experiment_files(exp)
    names = [header_info(p)["channels"] for p in paths]
    width = min(len(n) for n in names)
    pos = {}
    for i in range(width):
        labels = [n[i] for n in names if i < len(n)]
        top = max(set(labels), key=labels.count)
        for u in ("PD", "LP"):
            if top.upper().startswith(u) and u not in pos:
                pos[u] = i
    jobs = []
    for p, n in zip(paths, names):
        jobs.append(dict(path=p, ext=[], intra={u: n[i] for u, i in pos.items()}, whole=False,
                         pdn="pdn" if "pdn" in n else None,
                         labels={u: n[i] for u, i in pos.items()}))
    return jobs


'''
s=s.replace(old,new)
open('crabph.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import pickle,sys,crabph as C
pj,pr=pickle.load(open(__import__('os').environ['TMPDIR']+'/full_ptx.pkl','rb'))
for e in ['903_052','903_046','903_060']:
    rs=[r for r in pr if r['path'].startswith(e)]
    print(e,[(f[-8:-4],l) for f,l,_ in C.assign_ptx_conditions([(r['path'],r['ph']) for r in rs])])
print([ (j['path'][-8:],j['intra']) for j in C.ptx_jobs('903_046')][:3])
EOF
```

```
903_052 [('0003', '7.8'), ('0004', '8.3'), ('0005', '8.8'), ('0006', '9.3'), ('0007', '9.8'), ('0008', '10.4'), ('0009', '7.8'), ('0010', '7.2'), ('0011', '6.7'), ('0012', '6.1'), ('0013', '5.5'), ('0014', '7.8')]
903_046 [('0002', '7.8'), ('0005', '7.2'), ('0006', '6.7'), ('0008', '5.5'), ('0010', '7.8'), ('0011', '8.3'), ('0012', '8.8'), ('0013', '9.3'), ('0014', '9.8'), ('0015', '10.4'), ('0016', '7.8')]
903_060 [('0001', '7.8'), ('0002', '8.3'), ('0003', '9.3'), ('0004', '8.8'), ('0005', '9.8'), ('0006', '7.8'), ('0007', '7.2'), ('0008', '6.7'), ('0009', '6.1'), ('0010', '5.5'), ('0011', '7.8')]
[('0002.abf', {'PD': 'LP3', 'LP': 'PD4'}), ('0005.abf', {'PD': 'PD3', 'LP': 'LP4'}), ('0006.abf', {'PD': 'PD3', 'LP': 'LP4'})]
```

**Agent**

PTX assignment is fixed (903_052 is now in order, and 903_046 and 903_060 each show their one missing step). Now writing the analysis layer, which builds the tables per unit and condition.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
old=s[s.index('def rhythmic_seconds('):s.index('# ----------------------------------------------------------------------------------------------\n# Intracellular')]
new='''def rhythmic_seconds(onsets, t0, t1, max_gap):
    """Per second in [t0, t1): True when the second lies between two burst onsets at most max_gap
    apart (the window's edges count as onsets when the first or last onset is within max_gap of
    them); then runs shorter than MIN_STATE_S are merged into the state before them."""
    n = int(round(t1 - t0))
    r = np.zeros(n, bool)
    on = np.sort(np.asarray(onsets, float))
    if len(on):
        if on[0] - t0 <= max_gap:
            on = np.r_[t0, on]
        if t1 - on[-1] <= max_gap:
            on = np.r_[on, t1]
    for a, b in zip(on[:-1], on[1:]):
        if b - a <= max_gap:
            i0, i1 = int(np.floor(a - t0)), int(np.ceil(b - t0))
            r[max(0, i0):max(0, min(n, i1))] = True
    s = r.copy()
    i = 0
    while i < n:
        j = i
        while j < n and r[j] == r[i]:
            j += 1
        if j - i < MIN_STATE_S and i > 0:
            s[i:j] = s[i - 1]
        i = j
    return s


'''
s=s.replace(old,new)
s+='''

# ----------------------------------------------------------------------------------------------
# Tables per unit and condition

def ext_units(plans, results):
    """Every extracellular unit (STG PD per experiment, CG units) with its measures per condition."""
    R = {r["path"]: r for r in results}
    units = []
    for e, pl in plans.items():
        for u, (g, ch) in pl["units"].items():
            row = dict(ganglion=g, exp=e, unit=u, channel=ch, order=pl["order"],
                       label=f"{e} {u}" if g == "CG" else e)
            if ch is None:
                row.update(out=None)
            else:
                out, ref, cp = unit_measures(R, ch, pl["columns"], g, pl["seq"][0][0])
                row.update(out=out, ref=ref, ctl_period=cp)
            units.append(row)
    return units


def measure_frame(units, ganglion, measure, window="methods", missing="zero"):
    """Per unit and condition, the mean of the 48 bins. missing: "zero" (a step the experiment
    lacks counts as 0, as pHCumulative.m gives it) or "nan" (left out)."""
    rows = {}
    for u in units:
        if u["ganglion"] != ganglion or u["out"] is None:
            continue
        key = "bins" if window == "methods" else "code_bins"
        rows[u["label"]] = {c: (u["out"][c][key][measure].mean() if u["out"][c] is not None
                                else (0.0 if missing == "zero" else np.nan)) for c in COLUMNS}
    return pd.DataFrame(rows).T[COLUMNS]


def rhythmic_frame(units, ganglion, missing="zero"):
    rows = {}
    for u in units:
        if u["ganglion"] != ganglion or u["out"] is None:
            continue
        rows[u["label"]] = {c: (u["out"][c]["rhythmic"].mean() if u["out"][c] is not None
                                else (0.0 if missing == "zero" else np.nan)) for c in COLUMNS}
    return pd.DataFrame(rows).T[COLUMNS]


def bins_frame(units, ganglion, measure, column):
    """The 48 bin values of every unit at one condition (long form)."""
    rows = []
    for u in units:
        if u["ganglion"] != ganglion or u["out"] is None or u["out"][column] is None:
            continue
        for i, v in enumerate(u["out"][column]["bins"][measure]):
            rows.append(dict(unit=u["label"], bin=i, value=v))
    return pd.DataFrame(rows)


def ptx_tables(ptx_results):
    """PTX experiments: condition per file from the recorded pH, and per unit and measure a frame
    of preparations by condition (a step the experiment lacks is NaN)."""
    files, frames = [], {}
    for exp in PTX_EXPERIMENTS:
        rs = sorted([r for r in ptx_results if r["path"].startswith(exp + "/")], key=lambda r: r["path"])
        lab = assign_ptx_conditions([(r["path"], r["ph"]) for r in rs])
        seq = [(f, l) for f, l, _ in lab]
        cols, order = protocol_columns(pick_controls(seq, {r["path"]: 1e9 for r in rs}))
        byp = {r["path"]: r for r in rs}
        for (f, l, est), r in zip(lab, rs):
            files.append(dict(exp=exp, file=f, label=l, est_pH=est, ph_signal=r["ph"], minutes=r["seconds"] / 60,
                              order=order, used=f in cols.values(),
                              PD_channel=r["intra"].get("PD", {}).get("channel"),
                              LP_channel=r["intra"].get("LP", {}).get("channel"),
                              PD_pdn_match=r["intra"].get("PD", {}).get("pdn_match", np.nan),
                              LP_pdn_match=r["intra"].get("LP", {}).get("pdn_match", np.nan)))
        for unit in ("PD", "LP"):
            for c in COLUMNS:
                f = cols.get(c)
                m = byp[f]["intra"].get(unit) if f else None
                for k in ("vmin_methods", "vmin_code", "spike_amp", "burst_hz_trough", "burst_hz_peak",
                          "spike_hz", "wave_amp", "n_spikes", "n_waves", "mean_vm", "isi_cv"):
                    frames.setdefault((unit, k), {}).setdefault(exp, {})[c] = (m.get(k, np.nan) if m else np.nan)
    frames = {k: pd.DataFrame(v).T[COLUMNS] for k, v in frames.items()}
    return pd.DataFrame(files), frames


def intact_intra_frames(plans, results):
    """Intact STG preparations with intracellular PD or LP: [INTRA] measures per condition."""
    R = {r["path"]: r for r in results}
    frames = {}
    for e, pl in plans.items():
        for unit in pl["intra"]:
            for c in COLUMNS:
                f = pl["columns"].get(c)
                m = R[f]["intra"].get(unit) if f else None
                for k in ("vmin_methods", "vmin_code", "wave_amp", "n_spikes", "spike_amp", "mean_vm"):
                    frames.setdefault((unit, k), {}).setdefault(e, {})[c] = m[k] if m else np.nan
    return {k: pd.DataFrame(v).T[COLUMNS] for k, v in frames.items()}
'''
# isi cv in intra_measures
s=s.replace('''    r["n_spikes"] = len(st)''','''    r["n_spikes"] = len(st)
    isi = np.diff(st)
    r["isi_cv"] = float(isi.std() / isi.mean()) if len(isi) > 2 else np.nan''')
open('crabph.py','w').write(s)
EOF
date -u
```

```
Thu Nov 26 01:45:09 UTC 2026
```

**Agent**

Re-running the PTX pass with the fixed channel choice (about 1 min), then a first look at every claim's numbers.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, time, pickle
sys.path.insert(0,'entries/haley-2018')
import crabph as C
from concurrent.futures import ThreadPoolExecutor
t=time.time()
with ThreadPoolExecutor(12) as ex:
    pj=[j for js in ex.map(C.ptx_jobs,C.PTX_EXPERIMENTS) for j in js]
    pr=list(ex.map(C.process_ptx,pj))
print(time.time()-t)
pickle.dump((pj,pr),open('full_ptx.pkl','wb'))
EOF
```

```
59.602988958358765
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > dev.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/haley-2018')
import crabph as C
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
plans,missing,jobs,res=pickle.load(open('full_ext.pkl','rb'))
pj,pr=pickle.load(open('full_ptx.pkl','rb'))
units=C.ext_units(plans,res)
EOF
python - <<'EOF'
exec(open('dev.py').read())
for g in ['STG','CG']:
    for m in ['hz','spikes','duty']:
        df=C.measure_frame(units,g,m)
        print(g,m); print(df.round(2).to_string())
        a,b,t=C.rm_family(df)
        print(' acid F=%.2f p=%.4f n=%d | base F=%.2f p=%.4f n=%d'%(a['F'],a['p'],a['n'],b['F'],b['p'],b['n']))
        print(t.round(4).to_string())
    r=C.rhythmic_frame(units,g); print(g,'rhythmic'); print(r.round(2).to_string())
    a,b,t=C.rm_family(r); print(' acid F=%.2f p=%.4f | base F=%.2f p=%.4f'%(a['F'],a['p'],b['F'],b['p'])); print(t.round(4).to_string())
EOF
```

```
STG hz
         rec_acid   5.5   6.1   6.7   7.2  ctl_acid  ctl_base   8.3   8.8   9.3   9.8  10.4  rec_base
877_093      1.57  0.00  0.57  1.87  1.79      1.71      1.52  1.36  0.96  0.05  0.00  0.27      1.71
877_121      1.12  0.99  1.24  1.12  1.20      1.17      1.12  1.16  0.64  0.22  0.00  0.00      0.00
877_141      1.45  1.11  1.38  1.63  1.56      1.45      1.45  1.46  1.44  1.39  1.33  1.33      1.50
887_005      1.46  0.00  1.69  1.51  1.48      1.45      1.22  1.15  1.25  1.24  1.60  0.00      1.45
887_049      1.82  1.25  1.94  1.90  1.85      1.83      1.82  1.92  1.89  1.76  1.68  1.65      1.77
887_069      1.17  0.00  0.05  1.42  1.37      1.41      1.17  1.28  1.22  1.25  1.18  1.28      1.58
887_097      0.91  0.14  1.41  1.20  1.17      1.18      1.17  1.16  1.13  1.03  0.92  0.89      1.18
887_105      0.59  0.00  0.69  0.77  0.75      0.76      0.79  0.80  0.82  0.81  0.71  0.58      0.76
887_137      1.11  0.00  1.37  1.31  1.29      1.43      1.11  1.09  1.09  0.96  0.27  0.58      1.03
887_141      0.89  1.08  1.23  0.58  1.20      1.30      1.23  1.24  1.35  1.40  1.22  1.17      1.30
887_145      1.17  0.00  0.97  1.29  1.32      1.34      1.17  1.14  1.10  1.11  1.02  1.03      0.91
897_005      1.20  0.74  1.83  1.55  1.43      1.26      1.29  1.31  1.33  1.25  1.26  1.26      1.26
897_037      1.42  1.50  1.57  1.40  1.32      1.38      1.42  1.37  1.36  1.29  1.23  1.15      1.41
 acid F=13.70 p=0.0000 n=13 | base F=5.28 p=0.0004 n=13
   step   n  mean_control  mean_step    diff       t       p  p_corr
0   7.2  13        1.3609     1.3637  0.0029 -0.1238  0.9035  1.0000
1   6.7  13        1.3609     1.3500 -0.0108  0.1638  0.8726  1.0000
2   6.1  13        1.3609     1.2261 -0.1347  0.8915  0.3902  1.0000
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > look2.py <<'EOF'
exec(open('dev.py').read())
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
U={u['label']:u for u in units}
cases=[('887_005 CG2L','ctl_acid'),('887_073 CG2L','10.4'),('887_127 CG1L','9.8'),('897_041 CG1L','ctl_acid'),('887_065 CG2L','ctl_base'),('887_093 CG2L','8.3'),('887_127 CG1L','ctl_acid')]
fig,axs=plt.subplots(len(cases),1,figsize=(16,2.6*len(cases)))
for ax,(lab,col) in zip(axs,cases):
    u=U[lab]; v=u['out'][col]; f=v['file']
    out,info,_=C.stream_abf(f,{u['channel']:[(-60,-40)]},whole=False)
    fs=info['rate']; y=C.highpass(out[u['channel']][0],fs)
    t=np.arange(len(y))/fs
    ax.plot(t,y,lw=.3); pol=res[[r['path'] for r in res].index(f)]['ext'][u['channel']]['polarity']
    ax.axhline(pol*v['thr'],color='r'); ax.set_title(f"{lab} {col} {f} thr {v['thr']:.3f} ref {u['ref']:.3f} pol {pol}",fontsize=8)
plt.tight_layout(); plt.savefig('cg.png',dpi=60)
EOF
python look2.py
```

```
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/cg.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd entries/haley-2018 && . $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
old=s[s.index('def unit_threshold('):s.index('def unit_measures(')]
new='''def unit_threshold(sd, heights, floor, ganglion="STG"):
    """Spike threshold of one file (an assumption: the paper set thresholds by hand).

    STG (PD on the pdn, which carries only the PD axons): the larger of NOISE_K x noise, Otsu's
    split of the log event heights (PD against noise and pickup), and the floor.
    CG (LC on the trunk, the largest unit there): the larger of NOISE_K x noise, LC_FRAC x the
    LC_PCTL percentile of the event heights (the Small Cells far outnumber the LC spikes, so a
    split by counts finds the SC), and the floor.
    The floor is FLOOR_FRAC x the unit's median spike height in its first control file, so that
    smaller units are not counted when the unit falls silent."""
    big = heights[heights >= OTSU_MIN_K * sd]
    if ganglion == "CG":
        split = LC_FRAC * np.percentile(big, LC_PCTL) if len(big) >= 20 else 0.0
    else:
        split = otsu_log(big) if len(big) >= 20 else 0.0
    return max(NOISE_K * sd, split, floor)


'''
s=s.replace(old,new)
s=s.replace('''FLOOR_FRAC = 0.4                    # assumption: floor at 40% of the unit's control spike height''','''FLOOR_FRAC = 0.4                    # assumption: floor at 40% of the unit's control spike height
LC_FRAC, LC_PCTL = 0.4, 99.5        # assumption: LC threshold at 40% of the largest events''')
s=s.replace('thr0 = unit_threshold(r0["sd_late"], h0, 0.0)','thr0 = unit_threshold(r0["sd_late"], h0, 0.0, ganglion)')
s=s.replace('thr = unit_threshold(r["sd_late"], r["late"][1], floor)','thr = unit_threshold(r["sd_late"], r["late"][1], floor, ganglion)')
s=s.replace('thr_e = unit_threshold(r["sd_early"], r["early"][1], floor)','thr_e = unit_threshold(r["sd_early"], r["early"][1], floor, ganglion)')
s=s.replace('''  noise SDs (the unit against noise and smaller units, such as the Small Cells on the CG trunk),
  and `FLOOR_FRAC` times''','''  noise SDs for the PD on the pdn (the unit against noise and pickup) or `LC_FRAC` times the
  `LC_PCTL` percentile of those heights for the LC on the CG trunk (the LC is the largest unit
  there, and the Small Cells outnumber it), and `FLOOR_FRAC` times''')
open('crabph.py','w').write(s)
EOF
grep -n "LC_FRAC\|OTSU_MIN_K\|smaller units are not" crabph.py | head; cd $TMPDIR && python look2.py && python - <<'EOF'
exec(open('dev.py').read())
for m in ['hz','spikes','duty']:
    df=C.measure_frame(units,'CG',m); print(m); print(df.round(2).to_string())
print(C.rhythmic_frame(units,'CG').round(2).to_string())
EOF
```

```
28:  absolute deviation / 0.6745), Otsu's split of the log heights of the events above `OTSU_MIN_K`
29:  noise SDs for the PD on the pdn (the unit against noise and pickup) or `LC_FRAC` times the
109:OTSU_MIN_K = 4.0                    # events taken into the height split
111:LC_FRAC, LC_PCTL = 0.4, 99.5        # assumption: LC threshold at 40% of the largest events
697:    CG (LC on the trunk, the largest unit there): the larger of NOISE_K x noise, LC_FRAC x the
701:    smaller units are not counted when the unit falls silent."""
702:    big = heights[heights >= OTSU_MIN_K * sd]
704:        split = LC_FRAC * np.percentile(big, LC_PCTL) if len(big) >= 20 else 0.0
hz
              rec_acid   5.5   6.1   6.7   7.2  ctl_acid  ctl_base   8.3   8.8   9.3   9.8  10.4  rec_base
877_149 CG1L      0.00  0.09  0.20  0.06  0.04      0.06      0.00  0.04  0.06  0.10  0.15  0.11      0.21
877_149 CG2L      0.15  0.12  0.13  0.15  0.15      0.15      0.15  0.19  0.19  0.21  0.20  0.19      0.27
887_005 CG2L      0.17  0.29  0.29  0.31  0.31      0.32      0.29  0.28  0.30  0.17  0.01  0.00      0.32
887_011 CG3L      0.00  0.11  0.19  0.23  0.26      0.29      0.23  0.24  0.18  0.00  0.00  0.00      0.29
887_061 CG1L      0.30  0.34  0.35  0.36  0.36      0.38      0.30  0.31  0.30  0.26  0.19  0.12      0.40
887_065 CG2L      1.36  0.16  0.21  0.24  0.25      0.23      1.36  0.19  0.17  0.05  0.00  0.00      0.22
887_073 CG2L      0.00  0.21  0.03  0.00  0.01      0.17      0.00  0.00  0.00  0.00  0.00  0.00      0.17
887_093 CG2L      0.12  0.04  0.00  0.02  0.01      0.00      0.12  0.18  0.21  0.01  0.00  0.00      0.18
887_127 CG1L      0.41  0.15  0.18  0.67  0.97      0.22      0.41  0.23  0.20  0.26  0.12  0.64      0.06
887_149 CG1L      0.06  0.00  0.17  0.05  0.10      0.13      0.01  0.00  0.00  0.00  0.00  0.00      0.13
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/cg.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
exec(open('dev.py').read())
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,axs=plt.subplots(3,1,figsize=(16,8))
for ax,(f,ch,t0) in zip(axs,[('887_073/887_073_0001.abf','IN 12',-60),('887_073/887_073_0001.abf','IN 12',-200),('887_073/887_073_0002.abf','IN 12',-60)]):
    out,info,_=C.stream_abf(f,{ch:[(t0,t0+30)]},whole=False)
    y=C.highpass(out[ch][0],info['rate']); ax.plot(np.arange(len(y))/info['rate'],y,lw=.3); ax.set_title(f+' '+str(t0))
r=[x for x in res if x['path']=='887_073/887_073_0001.abf'][0]['ext']['IN 12']
h=r['late'][1]; print(r['sd_late'], np.percentile(h,[50,90,99,99.5,99.9]), len(h))
plt.tight_layout(); plt.savefig('c73.png',dpi=60)
EOF
```

```
0.00608458649367094 [0.0567 0.1768 1.7916 1.849  1.8807] 12902
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c73.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd entries/haley-2018 && . $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('crabph.py').read()
s=s.replace('''MAX_ISI_S, MIN_SPIKES = 0.3, 2      # spikenburst.s2s starting values''','''MAX_ISI_S, MIN_SPIKES = 0.3, 2      # spikenburst.s2s starting values
# Burst rules per ganglion (maximum interspike interval in s, minimum spikes). STG: the
# spikenburst.s2s starting values. CG: an assumption, as the LC fires as few as one or two spikes,
# up to about 0.5 s apart, in each Small Cell burst, and the paper's CG state 1 counts one LC spike
# per SC burst (Results, cardiac rhythm, paragraph 3); the starting values are a variant.
BURST_RULES = {"STG": (MAX_ISI_S, MIN_SPIKES), "CG": (1.0, 1)}''')
s=s.replace('''def unit_measures(results_by_file, channel, columns, ganglion, ref_file):''','''def unit_measures(results_by_file, channel, columns, ganglion, ref_file, burst_rule=None):''')
s=s.replace('''    out = {}
    ctl_period = None
    for col in COLUMNS:''','''    max_isi, min_spikes = burst_rule or BURST_RULES[ganglion]
    out = {}
    ctl_period = None
    for col in COLUMNS:''')
s=s.replace('b_late = bursts_from_spikes(np.sort(t_late))','b_late = bursts_from_spikes(np.sort(t_late), max_isi, min_spikes)')
s=s.replace('b_early = bursts_from_spikes(np.sort(t_early))','b_early = bursts_from_spikes(np.sort(t_early), max_isi, min_spikes)')
s=s.replace('''def ext_units(plans, results):
    """Every extracellular unit (STG PD per experiment, CG units) with its measures per condition."""''','''def ext_units(plans, results, cg_rule=None):
    """Every extracellular unit (STG PD per experiment, CG units) with its measures per condition.
    cg_rule: a (max ISI, min spikes) burst rule for the CG units in place of BURST_RULES["CG"]."""''')
s=s.replace('''out, ref, cp = unit_measures(R, ch, pl["columns"], g, pl["seq"][0][0])''','''out, ref, cp = unit_measures(R, ch, pl["columns"], g, pl["seq"][0][0],
                                             cg_rule if g == "CG" else None)''')
s=s.replace('''- [EXT] bursts: Spike2 BurstMake with 0.3 s maximum interspike interval and at least 2 spikes per
  burst (spikenburst.s2s starting values, claims header [EXT]; `MAX_ISI_S`, `MIN_SPIKES`).''','''- [EXT] bursts: Spike2 BurstMake with 0.3 s maximum interspike interval and at least 2 spikes per
  burst (spikenburst.s2s starting values, claims header [EXT]; `MAX_ISI_S`, `MIN_SPIKES`), which
  the authors adjusted per file; for the CG, 1.0 s and 1 spike (`BURST_RULES`, an assumption).''')
open('crabph.py','w').write(s)
EOF
cd $TMPDIR && python - <<'EOF'
exec(open('dev.py').read())
for m in ['hz','spikes','duty']:
    df=C.measure_frame(units,'CG',m); print(m); print(df.round(2).to_string())
    a,b,t=C.rm_family(df); print(' acid F=%.2f p=%.4f | base F=%.2f p=%.4f'%(a['F'],a['p'],b['F'],b['p'])); print(t[['step','diff','p_corr']].round(4).T.to_string())
r=C.rhythmic_frame(units,'CG'); print(r.round(2).to_string())
a,b,t=C.rm_family(r); print(' acid F=%.2f p=%.4f | base F=%.2f p=%.4f'%(a['F'],a['p'],b['F'],b['p'])); print(t[['step','diff','p_corr']].round(4).T.to_string())
EOF
```

```
hz
              rec_acid   5.5   6.1   6.7   7.2  ctl_acid  ctl_base   8.3   8.8   9.3   9.8  10.4  rec_base
877_149 CG1L      0.22  0.17  0.31  0.26  0.03      0.42      0.22  0.27  0.14  0.15  0.15  0.25      0.21
877_149 CG2L      0.14  0.11  0.13  0.14  0.15      0.15      0.14  0.19  0.19  0.21  0.20  0.18      0.27
887_005 CG2L      0.17  0.29  0.29  0.31  0.31      0.32      0.29  0.28  0.26  0.19  0.03  0.00      0.32
887_011 CG3L      0.17  0.11  0.19  0.21  0.25      0.29      0.23  0.24  0.18  0.01  0.00  0.00      0.29
887_061 CG1L      0.30  0.34  0.35  0.36  0.36      0.38      0.30  0.31  0.30  0.26  0.19  0.12      0.40
887_065 CG2L      0.15  0.16  0.21  0.24  0.25      0.24      0.15  0.16  0.17  0.05  0.00  0.00      0.22
887_073 CG2L      0.20  0.21  0.23  0.24  0.24      0.25      0.25  0.25  0.25  0.26  0.21  0.01      0.25
887_093 CG2L      0.12  0.04  0.08  0.15  0.16      0.18      0.12  0.18  0.15  0.07  0.00  0.00      0.18
887_127 CG1L      0.14  0.15  0.18  0.17  0.18      0.17      0.14  0.16  0.20  0.30  0.09  0.05      0.12
887_149 CG1L      0.28  0.35  0.24  0.30  0.32      0.32      0.28  0.29  0.16  0.01  0.00  0.00      0.32
887_149 CG2L      0.23  0.26  0.29  0.31  0.34      0.34      0.29  0.26  0.14  0.00  0.00  0.00      0.34
897_041 CG1L      0.01  0.00  0.01  0.02  0.03      0.04      0.01  0.01  0.01  0.00  0.00  0.00      0.02
897_041 CG3L      0.08  0.11  0.13  0.11  0.04      0.05      0.08  0.08  0.09  0.37  0.51  0.71      0.12
897_041 CG7L      0.16  0.13  0.14  0.16  0.16      0.11      0.16  0.12  0.10  0.02  0.00  0.03      0.15
 acid F=2.77 p=0.0367 | base F=2.29 p=0.0555
             0       1       2       3       4      5       6       7       8
step       7.2     6.7     6.1     5.5     8.3    8.8     9.3     9.8    10.4
diff   -0.0313 -0.0192 -0.0348 -0.0588  0.0099 -0.021 -0.0536 -0.0902 -0.0923
[... 64 more lines not kept]
```

**Agent**

With the CG burst rule changed, the CG measures look plausible. Quick check of the PTX and intact intracellular tables before I write the notebook.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
exec(open('dev.py').read())
files,fr=C.ptx_tables(pr)
for k in [('PD','vmin_methods'),('LP','vmin_methods'),('PD','vmin_code'),('PD','spike_amp'),('LP','spike_amp'),('PD','burst_hz_trough'),('LP','spike_hz'),('PD','wave_amp'),('LP','isi_cv')]:
    df=fr[k]; print(k); print(df.round(2).to_string())
    a,b,t=C.rm_family(df); print(' acid F=%.2f p=%.4f n=%d| base F=%.2f p=%.4f n=%d'%(a['F'],a['p'],a['n'],b['F'],b['p'],b['n'])); print(t[['step','n','diff','p_corr']].round(4).T.to_string())
it=C.intact_intra_frames(plans,res)
for k in [('PD','vmin_methods'),('LP','vmin_methods')]:
    print(k); print(it[k].round(1).to_string())
EOF
```

```
('PD', 'vmin_methods')
         rec_acid    5.5    6.1    6.7    7.2  ctl_acid  ctl_base    8.3    8.8    9.3    9.8   10.4  rec_base
903_046    -47.33 -28.08    NaN -44.73 -48.41    -50.98    -47.33 -44.22 -36.35 -31.92 -51.91 -52.22    -32.82
903_048    -45.88 -25.79 -24.13 -29.85 -41.05    -45.62    -38.96 -41.24 -44.26 -45.73 -45.65 -45.89    -45.62
903_050    -44.83 -25.21 -40.13 -42.05 -42.93    -42.40    -44.83 -47.30 -47.30 -44.16 -42.16 -43.04    -45.10
903_052    -37.90 -24.19 -27.68 -33.31 -39.27    -40.55    -25.21 -46.72 -53.54 -41.87 -48.71 -47.42    -40.55
903_054    -42.44 -22.10 -35.93 -42.68 -43.55    -44.66    -42.44 -45.82 -44.89 -44.81 -46.01 -44.91    -44.05
903_056    -51.62 -27.80 -44.99 -48.48 -49.80    -51.17    -52.40 -53.51 -51.64 -52.23 -53.12 -53.77    -51.17
903_058    -43.73 -24.86 -35.62 -37.87 -37.51    -38.24    -43.73 -42.52 -46.96 -45.35 -49.08 -48.11    -45.32
903_060    -53.22 -36.96 -35.21 -52.97 -55.99    -56.20    -56.89 -59.09 -57.13 -58.36 -55.90    NaN    -56.20
903_064    -47.03 -32.93 -31.29 -41.48 -47.81    -49.12    -47.03 -50.15 -52.55 -53.17 -52.58 -52.04    -48.69
 acid F=31.00 p=0.0000 n=8| base F=1.85 p=0.1277 n=8
             0       1        2        3       4       5      6       7       8
step       7.2     6.7      6.1      5.5     8.3     8.8    9.3     9.8    10.4
n            9       9        8        9       9       9      9       9       8
diff    1.4002  5.0566  11.6221  19.0003 -3.5266 -3.9784 -2.087 -5.1442 -5.6854
p_corr  0.0826  0.0575   0.0164      0.0  0.8656     1.0    1.0  0.3821  0.3023
('LP', 'vmin_methods')
         rec_acid    5.5    6.1    6.7    7.2  ctl_acid  ctl_base    8.3    8.8    9.3    9.8   10.4  rec_base
903_046    -44.30 -37.14    NaN -38.01 -38.90    -44.48    -44.30 -44.86 -49.04 -54.16 -56.95 -57.47    -48.75
[... 155 more lines not kept]
```

**Agent**

The PTX results line up closely with the paper's descriptions. The clock reads about 02:10. Writing the notebook now, as a cell-marked source file that I convert with nbformat.

**Agent calls Bash**

```bash
cat >> entries/haley-2018/crabph.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# Reporting

def rm_report(df, label, show=True):
    """[RM] on a frame of preparations by condition; prints the ANOVAs and the t-tests."""
    a, b, t = rm_family(df)
    if show:
        print(f"{label}: acid ANOVA F({a['df1']},{a['df2']}) = {a['F']:.2f}, p = {a['p']:.3g} (n = {a['n']}); "
              f"base ANOVA F({b['df1']},{b['df2']}) = {b['F']:.2f}, p = {b['p']:.3g} (n = {b['n']})")
        print(t.assign(mean_control=t.mean_control.round(3), mean_step=t.mean_step.round(3),
                       diff=t["diff"].round(3), t=t.t.round(2), p=t.p.map("{:.3g}".format),
                       p_corr=t.p_corr.map("{:.3g}".format)).to_string(index=False))
    return a, b, t.set_index("step")


def spearman_sign(row, cols, ph):
    r = stats.spearmanr([ph[c] for c in cols], [row[c] for c in cols])
    return r.statistic


PH_OF = {"ctl_acid": 7.8, "ctl_base": 7.8, "7.2": 7.2, "6.7": 6.7, "6.1": 6.1, "5.5": 5.5,
         "8.3": 8.3, "8.8": 8.8, "9.3": 9.3, "9.8": 9.8, "10.4": 10.4}
EOF
date -u
```

```
Thu Nov 26 01:49:11 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "# %% md\n# Reproducing Haley, Hampton & Marder (2018) from OSF project r7aes\n\n**Paper.** Haley JA, Hampton D, Marder E (2018). Two central pattern generators from the crab, *Cancer borealis*, respond robustly and differentially to extreme extracellular pH. eLife 7:e41877, doi:10.7554/elife.41877.\n\n**Dataset.** OSF project r7aes, \"Recordings of stomatogastric and cardiac ganglia of C. borealis at varying pH\" (doi:10.17605/osf.io/r7aes), files in OSF Storage. An OSF project is not versioned as a whole; each file is read at the OSF Storage version the registry's target list pinned (`r7aes_files.py`, built when the project was last modified, 2019-01-08T14:49:50), and the SHA-256 of every file read whole is checked against it. The paper cites the project without a version; these are the current versions of every file (checked against the live OSF listing below), and no file has a later version, so the choice is the only one.\n\n**Text read.** The claims file `claims/haley-2018.yaml` was written from the version of record (Europe PMC, PMC6328273) and the paper's code, github.com/jesshaley/haley_hampton_marder_2018 at commit 83f5904. Methods it does not fix are taken from the paper and cited where they are used, and in the helper module `crabph.py`.\n\n**What the dataset holds.** One folder per experiment, each with one Axon .abf file per pH step. The STG and CG folders have a README naming each file's pH and each channel's nerve; the nine picrotoxin (PTX) folders have none. The manual state annotations (`stateData_STG.xlsx`, `stateData_CG.xlsx`), the Spike2 spike and burst output and the gastric annotations are not in the project.\n\n| Claim | Tested here |\n|---|---|\n| fig2a-stg1-traces | tested; states by a proxy (assumption) |\n| fig2bcd-stg1-measures | tested |\n| fig3a-stg-variability-examples | blocked: needs the states 1 and 2 apart, which the proxy cannot tell |\n| fig3c-stg-rhythmic-fraction | tested; states by a proxy |\n| stg-state-transitions | blocked: needs the full manual state annotation |\n| fig3d-stg-frequency, fig3e-stg-spikes-per-burst, fig3f-stg-duty-cycle | tested |\n| fig3s2-stg-control-variability | tested |\n| fig4a-ptx-example, fig4bc-membrane-potential, fig4de-spike-amplitude, fig4fg-ptx-frequency | tested |\n| gastric-like-rhythm-counts, gastric-conditions-co-occur, fig5-gastric-recovery-example | blocked: gastric rhythms were identified by eye, with no criterion |\n| fig6-cg1-measures, fig6a-cg2-less-rhythmic | tested; states by a proxy |\n| fig7b-cg-rhythmic-fraction | tested; states by a proxy |\n| cg-state-transitions | blocked: needs the full manual state annotation |\n| fig7c-cg-frequency, fig7d-cg-spikes-per-burst, fig7e-cg-duty-cycle, fig7s2-cg-control-variability | tested |\n| fig8a-ganglion-difference, fig8b-individual-preparations, fig8b-cross-predictive | tested; states by a proxy |\n| baseline-frequency-correlations, robust-6-1-to-8-8, intact-depolarize-in-acid | tested |\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport time, resource\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport crabph as C\n\npd.set_option(\"display.width\", 250)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 400)\nT0 = time.time()\nprint(\"OSF project\", C.OSF_NODE, \"files pinned as of\", C.PUBLISHED_VERSION, \"-\", len(C.FILES), \"files\")\n\n# %% md\n## The files on OSF now, against the pinned list\n\nThe listing walks every storage provider of the project through the OSF API (docs/archives.md, \"OSF\").\n\n# %%\ntry:\n    listing, providers = C.osf_listing()\n    print(\"providers:\", providers)\n    now = listing[listing.provider == \"osfstorage\"].set_index(\"path\")\n    changed = [p for p, f in C.FILES.items() if p not in now.index or now.loc[p, \"version\"] != f[\"version\"]\n               or now.loc[p, \"sha256\"] != f[\"sha256\"] or now.loc[p, \"size\"] != f[\"size\"]]\n    print(f\"osfstorage files now: {len(now)}; pinned: {len(C.FILES)}; changed or gone since pinned: {len(changed)}; \"\n          f\"new: {len(set(now.index) - set(C.FILES))}\")\nexcept Exception as e:     # the listing is a check of the pin, not an input to any result\n    print(\"OSF listing could not be read:\", repr(e), \"- the pin was not checked against OSF in this run\")\n\n# %% md\n## The experiments: READMEs, files, conditions and channels\n\nThe claims file lists 15 STG experiments, 15 CG units and 9 PTX experiments, from the paper's code. For each STG and CG experiment the README gives the file of each pH step; the code's 13 conditions are formed from that order (`crabph.protocol_columns`). The PD unit is read on the pdn and a CG unit \"CGnL\" on the trunk channel the README calls \"CGn (trunk)\".\n\n# %%\nplans, missing_exps, jobs = C.plan_extracellular()\nprint(\"experiments listed by the paper's code and absent from the project:\", missing_exps)\nrows = []\nfor e, pl in plans.items():\n    rows.append(dict(exp=e, order=pl[\"order\"], files_in_readme=len(pl[\"seq_raw\"]), files_used=len(pl[\"seq\"]),\n                     not_in_readme=\", \".join(f.split(\"/\")[1] for f in pl[\"unlisted\"]),\n                     readme_names_not_in_folder=\", \".join(f\"{e}: {p}\" for f, p in zip([x for x, _ in pl[\"desc\"][\"files\"]], [y for _, y in pl[\"seq_raw\"]]) if False),\n                     missing_conditions=\", \".join(c for c, v in pl[\"columns\"].items() if v is None),\n                     units=\", \".join(f\"{u}:{ch}\" for u, (g, ch) in pl[\"units\"].items()),\n                     intracellular=\", \".join(f\"{u}:{ch}\" for u, ch in pl[\"intra\"].items()),\n                     notes=pl[\"desc\"][\"notes\"]))\nexp_table = pd.DataFrame(rows).drop(columns=\"readme_names_not_in_folder\")\nprint(exp_table.to_string(index=False))\n\n# %% md\n## Read the data\n\nEvery STG and CG file is streamed whole once, its SHA-256 checked, and the channels kept that the analysis uses: the unit channels in the first 10 min (for the code's window variant) and the last 8 min, the intracellular channels in the last minute, and the bath pH signal. Spikes are found as each file is read, so only event times and heights are held. The PTX files are read only over their last minute (the [INTRA] window), so their hashes are not checked. On the author's runner this took about 10 min and 3.3 GB.\n\n# %%\nt = time.time()\next_results = C.run_jobs(jobs, workers=12)\nprint(f\"STG and CG: {len(ext_results)} files in {(time.time() - t) / 60:.1f} min\")\nt = time.time()\nfrom concurrent.futures import ThreadPoolExecutor\nwith ThreadPoolExecutor(12) as ex:\n    ptx_jobs = [j for js in ex.map(C.ptx_jobs, C.PTX_EXPERIMENTS) for j in js]\n    ptx_results = list(ex.map(C.process_ptx, ptx_jobs))\nprint(f\"PTX: {len(ptx_results)} files in {(time.time() - t) / 60:.1f} min; \"\n      f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% [sanity]\nprint(\"SHA-256 of the STG and CG files read whole:\", sum(r[\"sha_ok\"] for r in ext_results), \"match of\", len(ext_results),\n      \"; mismatches:\", [r[\"path\"] for r in ext_results if not r[\"sha_ok\"]])\nheads = {f: h for pl in plans.values() for f, h in pl[\"heads\"].items()}\nH = pd.DataFrame(heads.values())\nprint(\"sampling rates (Hz) by experiment:\", H.groupby(H.path.str[:7]).rate.unique().map(list).to_dict())\nprint(\"file lengths: %.1f to %.1f min (median %.1f)\" % (H.seconds.min() / 60, H.seconds.max() / 60, H.seconds.median() / 60))\nprint(\"files shorter than the 8 min window:\", [(r[\"path\"], round(r[\"seconds\"] / 60, 1)) for r in ext_results if r[\"seconds\"] < C.WINDOW_S])\nused = sorted({ch for pl in plans.values() for _, ch in pl[\"units\"].values() if ch} | {ch for pl in plans.values() for ch in pl[\"intra\"].values()})\nunit_of = {}\nfor h in heads.values():\n    for c, u in zip(h[\"channels\"], h[\"units\"]):\n        if c in used:\n            unit_of.setdefault((c, u), 0)\n            unit_of[(c, u)] += 1\nprint(\"units of the channels used (channel, unit): files:\", unit_of)\nprint(\"STG experiments with a PD unit:\", sum(1 for pl in plans.values() for u, (g, ch) in pl[\"units\"].items() if g == \"STG\" and ch),\n      \"of\", len(C.STG_EXPERIMENTS), \"listed; CG units:\", sum(1 for pl in plans.values() for u, (g, ch) in pl[\"units\"].items() if g == \"CG\" and ch),\n      \"of\", len(C.CG_UNITS), \"listed; PTX experiments:\", len({r['path'][:7] for r in ptx_results}))\n# the bath pH signal against the README's pH, per experiment (Spearman over the files of the step protocols)\nR = {r[\"path\"]: r for r in ext_results}\nrows = []\nfor e, pl in plans.items():\n    pairs = [(float(p), R[f][\"ph\"]) for f, p in pl[\"seq\"] if R[f][\"ph\"] is not None]\n    if len(pairs) > 3:\n        rho = stats.spearmanr([a for a, _ in pairs], [b for _, b in pairs]).statistic\n        rows.append(dict(exp=e, n_files=len(pairs), spearman_readme_pH_vs_signal=round(rho, 3)))\n    else:\n        rows.append(dict(exp=e, n_files=len(pairs), spearman_readme_pH_vs_signal=None))\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"All channels of a file share its sampling clock (one interleaved ABF data block), and every measure is taken within a file, \"\n      \"so no stream has to be aligned with another.\")\n\n# %% md\nThe bath pH electrode signal is uncalibrated (its sign and scale differ between rigs), so it is compared with the README by rank: a negative correlation means the signal falls as the README's pH rises, as it does for a pH electrode in these recordings. The PTX folders have no README; the conditions of their files are taken from that signal (`crabph.assign_ptx_conditions`).\n\n# %%\nptx_files, ptx = C.ptx_tables(ptx_results)\nprint(ptx_files.assign(est_pH=ptx_files.est_pH.round(2), ph_signal=ptx_files.ph_signal.round(1), minutes=ptx_files.minutes.round(1),\n                       PD_pdn_match=ptx_files.PD_pdn_match.round(2), LP_pdn_match=ptx_files.LP_pdn_match.round(2)).to_string(index=False))\n\n# %% [finding-missing-experiments]\nfolders = sorted({p.split(\"/\")[0] for p in C.FILES})\nlisted = sorted(set(C.STG_EXPERIMENTS) | {e for e, _ in C.CG_UNITS} | set(C.PTX_EXPERIMENTS))\nprint(\"experiments in the paper's code:\", len(listed), \"; folders in the project:\", len(folders))\nprint(\"in the code, not in the project:\", sorted(set(listed) - set(folders)))\nprint(\"STG 877_127 is one of the 15 STG preparations; CG 887_017 (unit CG3L) one of the 15 CG units.\")\n\n# %% [finding-missing-steps]\nfor e, pl in plans.items():\n    miss = [c for c, v in pl[\"columns\"].items() if v is None]\n    if miss:\n        print(e, \"README lists\", len(pl[\"seq_raw\"]), \"files; no file for pH\", miss)\nfor e in C.PTX_EXPERIMENTS:\n    f = ptx_files[ptx_files.exp == e]\n    have = set(f.label)\n    miss = [s for s in C.ACID_STEPS + C.BASE_STEPS if s not in have]\n    if miss:\n        print(e, \"(PTX, from the recorded pH)\", len(f), \"files; no file for pH\", miss)\n\n# %% [finding-readme-mismatch]\nfor e, pl in plans.items():\n    names = [f for f, _ in pl[\"desc\"][\"files\"]]\n    absent = [f for f in names if f\"{e}/{f}\" not in C.FILES]\n    if absent:\n        print(e, \"README names files not in the folder:\", absent[:3], \"...\" if len(absent) > 3 else \"\",\n              \"-> matched by number to\", [r.split('/')[1] for r, _ in pl[\"seq_raw\"] if r][:3])\n    if pl[\"unlisted\"]:\n        print(e, \"folder holds files the README does not list:\", [f.split(\"/\")[1] for f in pl[\"unlisted\"]])\n    keys = [k for k, _ in pl[\"desc\"][\"electrodes\"] if k.startswith((\"IN\", \"extra\"))]\n    chans = set(pl[\"heads\"][pl[\"seq\"][0][0]][\"channels\"])\n    lacking = [k for k in keys if k not in chans]\n    if lacking:\n        print(e, \"README electrodes not among the file's channels:\", lacking, \"; file channels:\", sorted(c for c in chans if c.startswith((\"IN\", \"extra\"))))\n\n# %% [finding-ptx-order]\nprint(\"PTX folders have no README; pH per file from the recorded bath pH signal (mV):\")\nfor e in [\"903_058\", \"903_060\"]:\n    f = ptx_files[ptx_files.exp == e]\n    print(e, [(r.file.split(\"_\")[-1][:4], r.label, round(r.ph_signal, 1)) for r in f.itertuples()])\nprint(\"In both, the file recorded after 8.3 sits at the 9.3 level and the next at the 8.8 level.\")\n\n# %% [finding-ptx-label-swap]\nf = ptx_files[ptx_files.exp == \"903_046\"]\nfor j in [j for j in ptx_jobs if j[\"path\"].startswith(\"903_046\")][:3]:\n    print(j[\"path\"], \"channel names\", C.header_info(j[\"path\"])[\"channels\"][:4])\nprint(f[[\"file\", \"PD_channel\", \"LP_channel\", \"PD_pdn_match\", \"LP_pdn_match\"]].round(2).to_string(index=False))\nprint(\"The input the other files call PD3 is named LP3 in 903_046_0002; its spikes coincide with the pdn spikes there too.\")\n\n# %% [finding-no-pdn]\npl = plans[\"877_101\"]\nprint(\"877_101 electrodes:\", pl[\"desc\"][\"electrodes\"], \"; file channels:\", pl[\"heads\"][pl[\"seq\"][0][0]][\"channels\"])\nprint(\"No pdn, and the intracellular channel ME1_Vx is not named in the README: the PD unit cannot be isolated by threshold.\")\n\n# %% md\n## Extracellular units: spikes, bursts and the state proxy\n\nEach unit's threshold, burst rule and the proxy for rhythmic activity are in `crabph` (its docstring gives the source of each parameter). The table gives, per unit, the threshold in its first control file, the median spike height there, and the median burst period at control. A step an experiment lacks is 0 in the main reading, as the paper's code gives it (a condition marked missing in `extracellularAnalysis.m` has no bursts, and `pHCumulative.m` sets an empty bin to 0; its state is NaN, which counts as no time in any state), and is left out in the variant.\n\n# %%\nunits = C.ext_units(plans, ext_results)\nU = {u[\"label\"]: u for u in units}\nrows = []\nfor u in units:\n    if u[\"out\"] is None:\n        rows.append(dict(unit=u[\"label\"], ganglion=u[\"ganglion\"], channel=u[\"channel\"], note=\"no channel\")); continue\n    ref_col = next(c for c in (\"ctl_acid\", \"ctl_base\") if u[\"out\"][c] and u[\"out\"][c][\"file\"] == plans[u[\"exp\"]][\"seq\"][0][0])\n    v = u[\"out\"][ref_col]\n    rows.append(dict(unit=u[\"label\"], ganglion=u[\"ganglion\"], channel=u[\"channel\"], order=u[\"order\"], thr_control=round(v[\"thr\"], 4),\n                     noise_sd=round(v[\"sd\"], 4), median_spike_height=round(u[\"ref\"], 4), control_period_s=round(u[\"ctl_period\"], 3),\n                     control_bursts=len(v[\"bursts\"])))\nprint(pd.DataFrame(rows).to_string(index=False))\nmeasures = {(g, m, miss): C.measure_frame(units, g, m, missing=miss) for g in (\"STG\", \"CG\") for m in (\"hz\", \"spikes\", \"duty\") for miss in (\"zero\", \"nan\")}\ncode_measures = {(g, m): C.measure_frame(units, g, m, window=\"code\") for g in (\"STG\", \"CG\") for m in (\"hz\", \"spikes\", \"duty\")}\nrhythm = {(g, miss): C.rhythmic_frame(units, g, missing=miss) for g in (\"STG\", \"CG\") for miss in (\"zero\", \"nan\")}\nfor g in (\"STG\", \"CG\"):\n    for m in (\"hz\", \"spikes\", \"duty\"):\n        df = measures[(g, m, \"zero\")]\n        print(f\"{g} {m}: range {df.values.min():.3f} to {df.values.max():.3f}; preparations {len(df)}\")\n        print(df.round(3).to_string())\n    print(f\"{g} fraction of the last 8 min rhythmic (proxy)\")\n    print(rhythm[(g, \"zero\")].round(2).to_string())\n\n# %% md\nThe state proxy and its parameter. The paper's states were annotated by hand from all units (STG: PD, LP and PY; CG: Small and Large Cells). The proxy uses only the pacemaker unit the dataset lets us follow: a second counts as rhythmic when it lies between two PD (or LC) burst onsets no more than `RHYTHM_GAP_FACTOR` (3) control periods apart, with runs under 10 s merged (Methods, paragraph 3). For the CG this is close to state 1 (LC spikes with each SC burst); for the STG it counts state 3 (intermittent triphasic, PD still bursting) as rhythmic, so it can only overstate the STG's rhythmic fraction. The variants with factors 2 and 5 are computed for the claims that use the proxy.\n\n# %%\ndef proxy_frames(factor):\n    old = C.RHYTHM_GAP_FACTOR\n    C.RHYTHM_GAP_FACTOR = factor\n    try:\n        us = C.ext_units(plans, ext_results)\n    finally:\n        C.RHYTHM_GAP_FACTOR = old\n    return {g: C.rhythmic_frame(us, g) for g in (\"STG\", \"CG\")}\nproxy_var = {f: proxy_frames(f) for f in (2.0, 5.0)}\nproxy_var[3.0] = {g: rhythm[(g, \"zero\")] for g in (\"STG\", \"CG\")}\nfor f in (2.0, 3.0, 5.0):\n    print(f\"factor {f}: mean fraction rhythmic per condition\")\n    print(pd.DataFrame({g: proxy_var[f][g].mean() for g in (\"STG\", \"CG\")}).T.round(3).to_string())\nunits_cg03 = C.ext_units(plans, ext_results, cg_rule=(C.MAX_ISI_S, C.MIN_SPIKES))\ncg03 = {m: C.measure_frame(units_cg03, \"CG\", m) for m in (\"hz\", \"spikes\", \"duty\")}\ncg03_rhythm = C.rhythmic_frame(units_cg03, \"CG\")\n\n# %% md\n## fig2a-stg1-traces\n\n> In the example acid-first STG preparation, the pyloric rhythm stayed triphasic in acid until the most acidic pH, 5.5; in base it stayed triphasic up to 10.4 with fewer spikes per burst and smaller slow waves at 10.4, and it recovered in control saline after each protocol.\n\nCriterion: on 897_037, state 1 or 2 for most of each step from 7.2 to 6.1 and 8.3 to 10.4 and each recovery; at 10.4 lower PD spikes per burst ([EXT]) and lower PD slow-wave amplitude ([INTRA] filtering, last minute) than at the control before the base steps. States by the proxy (assumption). The PD intracellular channel is VM1_2 (README \"Vm1_2: PD\").\n\n# %% [claim:fig2a-stg1-traces]\nex = C.STG_EXAMPLE\nfr = rhythm[(\"STG\", \"zero\")].loc[ex]\nprint(\"order\", plans[ex][\"order\"], \"; fraction rhythmic (proxy) per condition:\"); print(fr.round(3).to_string())\nneed = [\"7.2\", \"6.7\", \"6.1\", \"8.3\", \"8.8\", \"9.3\", \"9.8\", \"10.4\", \"rec_acid\", \"rec_base\"]\nok_states = all(fr[c] > 0.5 for c in need)\nprint(\"most of each step 7.2 to 6.1, 8.3 to 10.4 and both recoveries rhythmic:\", ok_states, \"; at 5.5:\", round(fr[\"5.5\"], 3))\nfor f in (2.0, 5.0):\n    print(f\"  proxy factor {f}:\", {c: round(proxy_var[f]['STG'].loc[ex, c], 2) for c in need + ['5.5']})\nsp = measures[(\"STG\", \"spikes\", \"zero\")].loc[ex]\nprint(f\"PD spikes per burst: control before base {sp['ctl_base']:.2f}, 10.4 {sp['10.4']:.2f}\")\nintact = C.intact_intra_frames(plans, ext_results)\nwa = intact[(\"PD\", \"wave_amp\")].loc[ex]\nprint(f\"PD slow-wave amplitude (mV, last minute): control before base {wa['ctl_base']:.2f}, 10.4 {wa['10.4']:.2f}\")\nprint(\"all parts hold:\", ok_states and sp[\"10.4\"] < sp[\"ctl_base\"] and wa[\"10.4\"] < wa[\"ctl_base\"])\n\n# %% md\n**Result: reproduced, on the proxy for states.** 897_037 is rhythmic by the proxy for the whole of every step from 7.2 to 6.1 and from 8.3 to 10.4 and in both recoveries, and also at 5.5 (reading (a) of the criterion). At 10.4, PD spikes per burst (12.43 against 13.10) and the PD slow-wave amplitude are lower than at the control before the base steps. The proxy cannot tell normal from weak triphasic, so \"triphasic\" rests on PD bursting alone.\n\n## fig2bcd-stg1-measures\n\n> In the example STG preparation, pyloric burst frequency increased in acid and decreased in base, PD spikes per burst decreased at pH 5.5, and PD duty cycle decreased slightly in base.\n\nCriterion: 897_037, 48 bin means per step; reading (a) the extreme step against the control before that protocol, (b) the sign of the Spearman correlation of the step means with pH over the control and the steps.\n\n# %% [claim:fig2bcd-stg1-measures]\ndef example_readings(g, label, frames):\n    hz, spk, duty = (frames[m].loc[label] for m in (\"hz\", \"spikes\", \"duty\"))\n    acid_cols, base_cols = [\"ctl_acid\"] + C.ACID_STEPS, [\"ctl_base\"] + C.BASE_STEPS\n    out = {}\n    out[\"a\"] = dict(hz_acid=hz[\"5.5\"] - hz[\"ctl_acid\"], hz_base=hz[\"10.4\"] - hz[\"ctl_base\"],\n                    spikes_acid=spk[\"5.5\"] - spk[\"ctl_acid\"], duty_acid=duty[\"5.5\"] - duty[\"ctl_acid\"],\n                    duty_base=duty[\"10.4\"] - duty[\"ctl_base\"], spikes_base=spk[\"10.4\"] - spk[\"ctl_base\"])\n    sp = lambda s, cols: C.spearman_sign(s, cols, C.PH_OF)\n    # Spearman with pH: a negative value means the measure rises as pH falls (acid) or falls as pH rises (base)\n    out[\"b\"] = dict(hz_acid=sp(hz, acid_cols), hz_base=sp(hz, base_cols), spikes_acid=sp(spk, acid_cols),\n                    duty_acid=sp(duty, acid_cols), duty_base=sp(duty, base_cols), spikes_base=sp(spk, base_cols))\n    return pd.DataFrame(out).round(3)\n\nstg_frames = {m: measures[(\"STG\", m, \"zero\")] for m in (\"hz\", \"spikes\", \"duty\")}\nr = example_readings(\"STG\", ex, stg_frames)\nprint(\"(a) extreme minus control; (b) Spearman rho of step means with pH\")\nprint(r.to_string())\nprint(\"step means:\"); print(pd.DataFrame({m: stg_frames[m].loc[ex] for m in stg_frames}).T.round(3).to_string())\nok_a = r.loc[\"hz_acid\", \"a\"] > 0 and r.loc[\"hz_base\", \"a\"] < 0 and r.loc[\"spikes_acid\", \"a\"] < 0 and r.loc[\"duty_base\", \"a\"] < 0\nok_b = r.loc[\"hz_acid\", \"b\"] > 0 and r.loc[\"hz_base\", \"b\"] < 0 and r.loc[\"spikes_acid\", \"a\"] < 0 and r.loc[\"duty_base\", \"b\"] < 0\nprint(\"reading (a) holds:\", ok_a, \"; reading (b) holds:\", ok_b,\n      \"(in (b) 'frequency higher in acid' is a positive... see note)\")\ncode_frames = {m: code_measures[(\"STG\", m)] for m in (\"hz\", \"spikes\", \"duty\")}\nprint(\"code window variant:\"); print(example_readings(\"STG\", ex, code_frames).to_string())\n\n# %% md\n## fig3a-stg-variability-examples\n\nBlocked (`metadata_insufficient`). The criterion needs the STG states 1 (normal) and 2 (weak triphasic) apart at 10.4, and in state 2, 3 or 4 at 5.5. The manual annotation is not in the dataset, and the proxy, built on PD alone, cannot separate them.\n\n## fig3c-stg-rhythmic-fraction\n\n> Both acid and base significantly decreased the fraction of time STG preparations were rhythmic (normal or weak triphasic), and the rhythm was significantly less triphasic at pH 5.5 and 10.4 than at control.\n\nCriterion: per-preparation fraction rhythmic over the last 8 min, [RM]; both ANOVAs p < 0.05 and corrected t-tests at 5.5 and 10.4 p < 0.05, lower. Fraction rhythmic from the proxy (assumption).\n\n# %% [claim:fig3c-stg-rhythmic-fraction]\ndef rm_claim(df, label):\n    a, b, t = C.rm_report(df, label)\n    return a, b, t\nprint(\"STG preparations with the proxy:\", len(rhythm[(\"STG\", \"zero\")]))\na, b, t = rm_claim(rhythm[(\"STG\", \"zero\")], \"STG fraction rhythmic, missing steps as 0\")\nfig3c = dict(a=a, b=b, t=t)\nprint(\"criterion:\", a[\"p\"] < 0.05, b[\"p\"] < 0.05, t.loc[\"5.5\", \"p_corr\"] < 0.05 and t.loc[\"5.5\", \"diff\"] < 0, t.loc[\"10.4\", \"p_corr\"] < 0.05 and t.loc[\"10.4\", \"diff\"] < 0)\nC.rm_report(rhythm[(\"STG\", \"nan\")], \"variant: missing steps left out\")\nfor f in (2.0, 5.0):\n    C.rm_report(proxy_var[f][\"STG\"], f\"variant: proxy factor {f}\")\n\n# %% md\n## stg-state-transitions\n\nBlocked (`metadata_insufficient`). The criterion counts transitions among the four STG states over whole recordings; the annotation is not in the dataset, and the proxy has two states.\n\n## fig3d-stg-frequency\n\n> Mean pyloric burst frequency was relatively invariant across acid steps but varied significantly across base steps, being significantly slower than control at pH 9.3 and 10.4.\n\nCriterion: [RM] on PD burst frequency; acid ANOVA p ≥ 0.05 (absence), base ANOVA p < 0.05, corrected t-tests at 9.3 and 10.4 p < 0.05, lower.\n\n# %% [claim:fig3d-stg-frequency]\nprint(\"STG preparations:\", len(measures[(\"STG\", \"hz\", \"zero\")]), \"(877_101 has no pdn; 877_127 is not in the project)\")\na, b, t = rm_claim(measures[(\"STG\", \"hz\", \"zero\")], \"PD burst frequency (Hz), missing steps as 0\")\nprint(\"criterion: acid p >= 0.05:\", a[\"p\"] >= 0.05, \"; base p < 0.05:\", b[\"p\"] < 0.05,\n      \"; 9.3:\", t.loc[\"9.3\", \"p_corr\"] < 0.05 and t.loc[\"9.3\", \"diff\"] < 0, \"; 10.4:\", t.loc[\"10.4\", \"p_corr\"] < 0.05 and t.loc[\"10.4\", \"diff\"] < 0)\nC.rm_report(measures[(\"STG\", \"hz\", \"nan\")], \"variant: missing steps left out\")\nC.rm_report(code_measures[(\"STG\", \"hz\")], \"variant: the code's window (480 s from the first burst)\")\ndf = measures[(\"STG\", \"hz\", \"zero\")]\nC.rm_report(df[df[\"5.5\"] > 0], \"variant: preparations still bursting at 5.5 only\")\n\n# %% md\n## fig3e-stg-spikes-per-burst\n\n> Acid and base both significantly affected the number of PD spikes per burst, which was significantly reduced at pH 5.5.\n\n# %% [claim:fig3e-stg-spikes-per-burst]\na, b, t = rm_claim(measures[(\"STG\", \"spikes\", \"zero\")], \"PD spikes per burst, missing steps as 0\")\nprint(\"criterion:\", a[\"p\"] < 0.05, b[\"p\"] < 0.05, t.loc[\"5.5\", \"p_corr\"] < 0.05 and t.loc[\"5.5\", \"diff\"] < 0)\nC.rm_report(measures[(\"STG\", \"spikes\", \"nan\")], \"variant: missing steps left out\")\nC.rm_report(code_measures[(\"STG\", \"spikes\")], \"variant: the code's window\")\n\n# %% md\n## fig3f-stg-duty-cycle\n\n> Acid and base both significantly affected PD duty cycle, with a slight increase from control pH 7.8 to pH 6.1.\n\n# %% [claim:fig3f-stg-duty-cycle]\na, b, t = rm_claim(measures[(\"STG\", \"duty\", \"zero\")], \"PD duty cycle, missing steps as 0\")\nprint(\"criterion:\", a[\"p\"] < 0.05, b[\"p\"] < 0.05, t.loc[\"6.1\", \"p_corr\"] < 0.05 and t.loc[\"6.1\", \"diff\"] > 0)\nC.rm_report(measures[(\"STG\", \"duty\", \"nan\")], \"variant: missing steps left out\")\nC.rm_report(code_measures[(\"STG\", \"duty\")], \"variant: the code's window\")\n\n# %% md\n## fig3s2-stg-control-variability\n\n> Pyloric frequency, PD spikes per burst and PD duty cycle vary widely between the 15 STG preparations at control pH, as widely as the pooled distributions across pH.\n\nCriterion: the 48 bins of each preparation in its first control step (condition 1 of the code); (a) the range of the preparation means at control spans at least half the range of the pooled bin values over all steps, for each measure; (b) Kruskal-Wallis of the bins on preparation p < 0.05 for each measure.\n\n# %% [claim:fig3s2-stg-control-variability]\ndef control_variability(g):\n    out = {}\n    for m in (\"hz\", \"spikes\", \"duty\"):\n        ctl_bins, pooled = [], []\n        for u in units:\n            if u[\"ganglion\"] != g or u[\"out\"] is None:\n                continue\n            first = plans[u[\"exp\"]][\"seq\"][0][0]\n            col = next(c for c in (\"ctl_acid\", \"ctl_base\") if u[\"out\"][c] and u[\"out\"][c][\"file\"] == first)\n            ctl_bins.append(u[\"out\"][col][\"bins\"][m])\n            for c in C.COLUMNS[1:5] + [\"ctl_acid\", \"ctl_base\"] + C.COLUMNS[7:12]:\n                if u[\"out\"][c] is not None:\n                    pooled.append(u[\"out\"][c][\"bins\"][m])\n        means = np.array([b.mean() for b in ctl_bins])\n        pooled = np.concatenate(pooled)\n        kw = stats.kruskal(*ctl_bins)\n        out[m] = dict(n=len(ctl_bins), prep_mean_min=means.min(), prep_mean_max=means.max(),\n                      prep_range=np.ptp(means), pooled_min=pooled.min(), pooled_max=pooled.max(), pooled_range=np.ptp(pooled),\n                      ratio=np.ptp(means) / np.ptp(pooled), reading_a=np.ptp(means) >= 0.5 * np.ptp(pooled),\n                      kruskal_H=kw.statistic, kruskal_p=kw.pvalue, reading_b=kw.pvalue < 0.05)\n    return pd.DataFrame(out).T\nv = control_variability(\"STG\")\nprint(v.to_string())\nprint(\"reading (a) for all three:\", bool(v.reading_a.all()), \"; reading (b) for all three:\", bool(v.reading_b.all()))\n\n# %% md\n## fig4a-ptx-example\n\n> In an example preparation with PTX, the PD neuron lost most of its slow wave at pH 6.7, became silent and depolarized at 5.5, kept its burst at 8.8 and fired single-spike bursts at 10.4; the LP neuron fired tonically from 6.7 to 10.4 and lost activity at 5.5.\n\nCriterion: at least one PTX preparation with PD slow-wave amplitude at 6.7 below half its PTX control, no PD spikes and minimum Vm above control at 5.5, one spike per PD burst at 10.4, LP spiking without slow-wave bursts from 6.7 to 10.4, no LP spikes at 5.5. Readings of the words taken here: \"one spike per PD burst\" is a ratio of PD spikes to slow-wave peaks of at most 1.5 (and above 0), and \"without slow-wave bursts\" is LP firing with an interspike-interval coefficient of variation below 1 (tonic firing, as opposed to bursts of spikes separated by long gaps). The PTX control is the control before the acid steps.\n\n# %% [claim:fig4a-ptx-example]\nrows = []\nfor e in C.PTX_EXPERIMENTS:\n    g = lambda u, k, c: ptx[(u, k)].loc[e, c]\n    ratio104 = g(\"PD\", \"n_spikes\", \"10.4\") / g(\"PD\", \"n_waves\", \"10.4\") if g(\"PD\", \"n_waves\", \"10.4\") else np.nan\n    lp_tonic = [(g(\"LP\", \"n_spikes\", c) > 0) and (g(\"LP\", \"isi_cv\", c) < 1) for c in [\"6.7\", \"8.3\", \"8.8\", \"9.3\", \"9.8\", \"10.4\"]]\n    rows.append(dict(exp=e,\n                     pd_wave_67_over_ctl=g(\"PD\", \"wave_amp\", \"6.7\") / g(\"PD\", \"wave_amp\", \"ctl_acid\"),\n                     pd_spikes_55=g(\"PD\", \"n_spikes\", \"5.5\"), pd_vmin_55_minus_ctl=g(\"PD\", \"vmin_methods\", \"5.5\") - g(\"PD\", \"vmin_methods\", \"ctl_acid\"),\n                     pd_spikes_per_wave_104=ratio104, pd_wave_88_over_ctl=g(\"PD\", \"wave_amp\", \"8.8\") / g(\"PD\", \"wave_amp\", \"ctl_base\"),\n                     lp_tonic_67_to_104=f\"{sum(lp_tonic)}/6\", lp_spikes_55=g(\"LP\", \"n_spikes\", \"5.5\")))\nfa = pd.DataFrame(rows)\nfa[\"all\"] = ((fa.pd_wave_67_over_ctl < 0.5) & (fa.pd_spikes_55 == 0) & (fa.pd_vmin_55_minus_ctl > 0) & (fa.pd_spikes_per_wave_104 > 0)\n             & (fa.pd_spikes_per_wave_104 <= 1.5) & (fa.lp_tonic_67_to_104 == \"6/6\") & (fa.lp_spikes_55 == 0))\nprint(fa.round(3).to_string(index=False))\nprint(\"PTX preparations meeting every part:\", int(fa[\"all\"].sum()))\nparts = {\"PD wave at 6.7 < half\": (fa.pd_wave_67_over_ctl < 0.5), \"PD silent at 5.5\": fa.pd_spikes_55 == 0, \"PD depolarized at 5.5\": fa.pd_vmin_55_minus_ctl > 0,\n         \"one spike per PD burst at 10.4\": (fa.pd_spikes_per_wave_104 > 0) & (fa.pd_spikes_per_wave_104 <= 1.5),\n         \"LP tonic 6.7 to 10.4\": fa.lp_tonic_67_to_104 == \"6/6\", \"LP silent at 5.5\": fa.lp_spikes_55 == 0}\nprint({k: int(v.sum()) for k, v in parts.items()})\nprint(\"parts met per preparation:\", dict(zip(fa.exp, sum(v.astype(int) for v in parts.values()))))\n\n# %% md\n## fig4bc-membrane-potential\n\n> With PTX, the PD neuron depolarized significantly in extreme acid (pH 5.5 and 6.1) while LP stayed relatively constant, and in base PD stayed relatively constant while LP hyperpolarized significantly at pH 8.8, 9.3, 9.8 and 10.4.\n\nCriterion: minimum membrane potential ([INTRA]; Methods reading, the minimum of the unfiltered Vm between bursts), [RM]. A PTX preparation lacking a step is left out of that protocol's ANOVA and of that t-test (the paper's PTX code has no rule for a missing step).\n\n# %% [claim:fig4bc-membrane-potential]\nres4bc = {}\nfor k in (\"vmin_methods\", \"vmin_code\"):\n    print(\"==\", k)\n    pa, pb, pt = C.rm_report(ptx[(\"PD\", k)], f\"PD minimum Vm ({k})\")\n    la, lb, lt = C.rm_report(ptx[(\"LP\", k)], f\"LP minimum Vm ({k})\")\n    tests = {\"PD 5.5\": pt.loc[\"5.5\", \"p_corr\"] < 0.05 and pt.loc[\"5.5\", \"diff\"] > 0, \"PD 6.1\": pt.loc[\"6.1\", \"p_corr\"] < 0.05 and pt.loc[\"6.1\", \"diff\"] > 0}\n    for s in (\"8.8\", \"9.3\", \"9.8\", \"10.4\"):\n        tests[f\"LP {s}\"] = lt.loc[s, \"p_corr\"] < 0.05 and lt.loc[s, \"diff\"] < 0\n    res4bc[k] = dict(pd_acid=pa[\"p\"], lp_base=lb[\"p\"], lp_acid=la[\"p\"], pd_base=pb[\"p\"], tests=tests)\n    print(\"PD acid ANOVA p < 0.05:\", pa[\"p\"] < 0.05, \"; LP base ANOVA p < 0.05:\", lb[\"p\"] < 0.05, \"; t-tests:\", tests,\n          f\"; absence: LP acid ANOVA p = {la['p']:.3g}, PD base ANOVA p = {pb['p']:.3g}\")\n\n# %% md\n## fig4de-spike-amplitude\n\n> With PTX, acid significantly affected spike amplitude of both PD and LP, and base affected LP but not PD; amplitude was significantly reduced at pH 5.5 in both, and LP amplitude also at pH 6.1.\n\n# %% [claim:fig4de-spike-amplitude]\npa, pb, pt = C.rm_report(ptx[(\"PD\", \"spike_amp\")], \"PD spike amplitude (mV)\")\nla, lb, lt = C.rm_report(ptx[(\"LP\", \"spike_amp\")], \"LP spike amplitude (mV)\")\ncrit = {\"PD acid\": pa[\"p\"] < 0.05, \"LP acid\": la[\"p\"] < 0.05, \"LP base\": lb[\"p\"] < 0.05, \"PD base absent\": pb[\"p\"] >= 0.05,\n        \"PD 5.5\": pt.loc[\"5.5\", \"p_corr\"] < 0.05 and pt.loc[\"5.5\", \"diff\"] < 0, \"LP 5.5\": lt.loc[\"5.5\", \"p_corr\"] < 0.05 and lt.loc[\"5.5\", \"diff\"] < 0,\n        \"LP 6.1\": lt.loc[\"6.1\", \"p_corr\"] < 0.05 and lt.loc[\"6.1\", \"diff\"] < 0}\nprint(crit)\n\n# %% md\n## fig4fg-ptx-frequency\n\n> With PTX, acid and base both significantly affected PD burst frequency and LP firing rate; PD burst frequency was significantly lower at pH 5.5, and LP firing rate was significantly lower at pH 5.5, 6.1, 8.3, 9.3, 9.8 and 10.4 than at control.\n\nPD burst frequency from slow-wave trough-to-trough intervals (Methods); the code's peak-to-peak is a variant.\n\n# %% [claim:fig4fg-ptx-frequency]\nfor k in (\"burst_hz_trough\", \"burst_hz_peak\"):\n    pa, pb, pt = C.rm_report(ptx[(\"PD\", k)], f\"PD burst frequency ({k})\")\n    la, lb, lt = C.rm_report(ptx[(\"LP\", \"spike_hz\")], \"LP firing rate (Hz)\", show=(k == \"burst_hz_trough\"))\n    tt = {\"PD 5.5\": pt.loc[\"5.5\", \"p_corr\"] < 0.05 and pt.loc[\"5.5\", \"diff\"] < 0}\n    for s in (\"5.5\", \"6.1\", \"8.3\", \"9.3\", \"9.8\", \"10.4\"):\n        tt[f\"LP {s}\"] = lt.loc[s, \"p_corr\"] < 0.05 and lt.loc[s, \"diff\"] < 0\n    print(k, \"ANOVAs < 0.05:\", [pa[\"p\"] < 0.05, pb[\"p\"] < 0.05, la[\"p\"] < 0.05, lb[\"p\"] < 0.05], \"; t-tests:\", tt, \"; held:\", sum(tt.values()), \"of 7\")\n\n# %% md\n## gastric-like-rhythm-counts, gastric-conditions-co-occur, fig5-gastric-recovery-example\n\nBlocked (`methods_underspecified`). The paper identified gastric-like rhythms by eye (Results, \"Rhythmic gastric-like activity ...\", paragraphs 2 and 3) and coded them as 8.x in its manual STG annotation, which is not in the dataset. The criterion's fallback, rhythmic LG bursting alternating with DG bursting, has no period, burst or alternation thresholds in the paper or its code, and the dataset has no LG, DG, GM or MCN1 unit labels beyond the nerve names, so any detector would rest on thresholds of this attempt alone. The co-occurrence claim uses the counts, and the Figure 5 example is not named and rests on the same identification.\n\n## fig6-cg1-measures\n\n> In the example cardiac ganglion, the rhythm persisted over the whole pH range; cardiac frequency decreased in acid and increased in base, LC spikes per burst increased in acid, and LC duty cycle decreased slightly in acid and in base.\n\nCriterion: 877_149 CG2L, readings (a) and (b) as for fig2bcd; and CG state 1 (proxy) for most of every step.\n\n# %% [claim:fig6-cg1-measures]\ncx = \" \".join(C.CG_EXAMPLE)\ncg_frames = {m: measures[(\"CG\", m, \"zero\")] for m in (\"hz\", \"spikes\", \"duty\")}\nr = example_readings(\"CG\", cx, cg_frames)\nprint(r.to_string())\nprint(\"step means:\"); print(pd.DataFrame({m: cg_frames[m].loc[cx] for m in cg_frames}).T.round(3).to_string())\nfr = rhythm[(\"CG\", \"zero\")].loc[cx]\nprint(\"fraction rhythmic (proxy):\", fr.round(2).to_dict())\ndef cg1_ok(r, rd):\n    s = 1 if rd == \"a\" else -1   # in (b) a rise in acid is a negative rho with pH\n    if rd == \"a\":\n        return dict(hz_acid_lower=r.loc[\"hz_acid\", \"a\"] < 0, hz_base_higher=r.loc[\"hz_base\", \"a\"] > 0, spikes_acid_higher=r.loc[\"spikes_acid\", \"a\"] > 0,\n                    duty_acid_lower=r.loc[\"duty_acid\", \"a\"] < 0, duty_base_lower=r.loc[\"duty_base\", \"a\"] < 0)\n    return dict(hz_acid_lower=r.loc[\"hz_acid\", \"b\"] > 0, hz_base_higher=r.loc[\"hz_base\", \"b\"] > 0, spikes_acid_higher=r.loc[\"spikes_acid\", \"b\"] < 0,\n                duty_acid_lower=r.loc[\"duty_acid\", \"b\"] > 0, duty_base_lower=r.loc[\"duty_base\", \"b\"] < 0)\nfor rd in (\"a\", \"b\"):\n    print(\"reading\", rd, cg1_ok(r, rd))\nprint(\"rhythmic for most of every step:\", bool((fr[C.COLUMNS] > 0.5).all()))\nprint(\"variant, CG burst rule 0.3 s and 2 spikes:\"); print(example_readings(\"CG\", cx, cg03).to_string())\nprint(\"variant, code window:\"); print(example_readings(\"CG\", cx, {m: code_measures[(\"CG\", m)] for m in (\"hz\", \"spikes\", \"duty\")}).to_string())\n\n# %% md\n## fig6a-cg2-less-rhythmic\n\n> A second example cardiac ganglion became less rhythmic at pH 5.5 and at pH 9.8 and above, and recovered a normal bursting rhythm in control saline.\n\nCriterion: among acid-first CG units other than 877_149 CG2L, one whose fraction in state 1 (proxy) is below its control at 5.5, 9.8 and 10.4, higher at each step from 6.1 to 9.3 than at each of 5.5, 9.8 and 10.4, and above half in the final recovery.\n\n# %% [claim:fig6a-cg2-less-rhythmic]\ndef cg2_table(fr):\n    rows = []\n    for u in units:\n        if u[\"ganglion\"] != \"CG\" or u[\"order\"] != \"AB\" or u[\"label\"] == cx or u[\"out\"] is None:\n            continue\n        x = fr.loc[u[\"label\"]]\n        low = [x[\"5.5\"], x[\"9.8\"], x[\"10.4\"]]\n        mid = [x[c] for c in (\"6.1\", \"6.7\", \"7.2\", \"8.3\", \"8.8\", \"9.3\")]\n        rows.append(dict(unit=u[\"label\"], ctl=x[\"ctl_acid\"], f55=x[\"5.5\"], f98=x[\"9.8\"], f104=x[\"10.4\"], mid_min=min(mid), rec=x[\"rec_base\"],\n                         below_ctl=all(v < x[\"ctl_acid\"] for v in low), mid_above=min(mid) > max(low), recovered=x[\"rec_base\"] > 0.5))\n    t = pd.DataFrame(rows)\n    t[\"all\"] = t.below_ctl & t.mid_above & t.recovered\n    return t\nt = cg2_table(rhythm[(\"CG\", \"zero\")])\nprint(t.round(2).to_string(index=False)); print(\"units meeting the criterion:\", list(t.unit[t[\"all\"]]))\nfor f in (2.0, 5.0):\n    tv = cg2_table(proxy_var[f][\"CG\"]); print(f\"proxy factor {f}: units meeting it:\", list(tv.unit[tv[\"all\"]]))\n\n# %% md\n## fig7b-cg-rhythmic-fraction\n\n> Acid and base both significantly affected the fraction of time cardiac preparations were rhythmic (SC and LC bursting together), which was significantly lower at pH 5.5, 9.3, 9.8 and 10.4 than at control.\n\n# %% [claim:fig7b-cg-rhythmic-fraction]\na, b, t = rm_claim(rhythm[(\"CG\", \"zero\")], \"CG fraction rhythmic (proxy), missing steps as 0\")\ntt = {s: t.loc[s, \"p_corr\"] < 0.05 and t.loc[s, \"diff\"] < 0 for s in (\"5.5\", \"9.3\", \"9.8\", \"10.4\")}\nprint(\"criterion: ANOVAs\", a[\"p\"] < 0.05, b[\"p\"] < 0.05, \"; t-tests\", tt)\nC.rm_report(rhythm[(\"CG\", \"nan\")], \"variant: missing steps left out\")\nC.rm_report(cg03_rhythm, \"variant: CG burst rule 0.3 s, 2 spikes\")\nfor f in (2.0, 5.0):\n    C.rm_report(proxy_var[f][\"CG\"], f\"variant: proxy factor {f}\")\n\n# %% md\n## cg-state-transitions\n\nBlocked (`metadata_insufficient`): the criterion counts transitions among CG states 1 to 3 (SC and LC, SC only, silent) over whole recordings. The annotation is not in the dataset, and the proxy follows the LC only, so it cannot tell state 2 from state 3.\n\n## fig7c-cg-frequency\n\n> Cardiac rhythm frequency declined in both acidic and basic saline and was significantly slower at pH 10.4.\n\nCriterion: readings (a) both ANOVAs p < 0.05; (b) base ANOVA p < 0.05 and the mean at 5.5 below the acid control; reproduced when under one reading the corrected t-test at 10.4 has p < 0.05, lower.\n\n# %% [claim:fig7c-cg-frequency]\nfor lab, df in [(\"main\", measures[(\"CG\", \"hz\", \"zero\")]), (\"missing steps left out\", measures[(\"CG\", \"hz\", \"nan\")]),\n                (\"code window\", code_measures[(\"CG\", \"hz\")]), (\"CG burst rule 0.3 s, 2 spikes\", cg03[\"hz\"])]:\n    a, b, t = C.rm_report(df, f\"LC burst frequency (Hz), {lab}\", show=(lab == \"main\"))\n    ra = a[\"p\"] < 0.05 and b[\"p\"] < 0.05\n    rb = b[\"p\"] < 0.05 and t.loc[\"5.5\", \"diff\"] < 0\n    t104 = t.loc[\"10.4\", \"p_corr\"] < 0.05 and t.loc[\"10.4\", \"diff\"] < 0\n    print(f\"{lab}: acid p = {a['p']:.3g}, base p = {b['p']:.3g}; reading (a) {ra}, (b) {rb}; 10.4 diff {t.loc['10.4', 'diff']:.3f} p_corr {t.loc['10.4', 'p_corr']:.3g} -> {t104}\")\n\n# %% md\n## fig7d-cg-spikes-per-burst\n\n> Acid and base both significantly affected LC spikes per burst, which increased significantly at pH 5.5 and 6.1 and decreased at pH 9.8 and 10.4.\n\n# %% [claim:fig7d-cg-spikes-per-burst]\nfor lab, df in [(\"main\", measures[(\"CG\", \"spikes\", \"zero\")]), (\"missing steps left out\", measures[(\"CG\", \"spikes\", \"nan\")]),\n                (\"code window\", code_measures[(\"CG\", \"spikes\")]), (\"CG burst rule 0.3 s, 2 spikes\", cg03[\"spikes\"])]:\n    a, b, t = C.rm_report(df, f\"LC spikes per burst, {lab}\", show=(lab == \"main\"))\n    tt = {\"5.5 up\": t.loc[\"5.5\", \"p_corr\"] < 0.05 and t.loc[\"5.5\", \"diff\"] > 0, \"6.1 up\": t.loc[\"6.1\", \"p_corr\"] < 0.05 and t.loc[\"6.1\", \"diff\"] > 0,\n          \"9.8 down\": t.loc[\"9.8\", \"p_corr\"] < 0.05 and t.loc[\"9.8\", \"diff\"] < 0, \"10.4 down\": t.loc[\"10.4\", \"p_corr\"] < 0.05 and t.loc[\"10.4\", \"diff\"] < 0}\n    print(f\"{lab}: acid p = {a['p']:.3g}, base p = {b['p']:.3g}; t-tests {tt}\")\n\n# %% md\n## fig7e-cg-duty-cycle\n\n> Base, but not acid, had a significant effect on LC duty cycle.\n\n# %% [claim:fig7e-cg-duty-cycle]\nfor lab, df in [(\"main\", measures[(\"CG\", \"duty\", \"zero\")]), (\"missing steps left out\", measures[(\"CG\", \"duty\", \"nan\")]),\n                (\"code window\", code_measures[(\"CG\", \"duty\")]), (\"CG burst rule 0.3 s, 2 spikes\", cg03[\"duty\"])]:\n    a, b, t = C.rm_report(df, f\"LC duty cycle, {lab}\", show=(lab == \"main\"))\n    print(f\"{lab}: base p = {b['p']:.3g} (< 0.05: {b['p'] < 0.05}); acid p = {a['p']:.3g} (>= 0.05: {a['p'] >= 0.05}); \"\n          f\"acid diffs {t.loc[C.ACID_STEPS, 'diff'].round(3).to_dict()}\")\n\n# %% md\n## fig7s2-cg-control-variability\n\n> Cardiac frequency, LC spikes per burst and LC duty cycle vary widely between preparations at control pH, independent of pH.\n\n# %% [claim:fig7s2-cg-control-variability]\nv = control_variability(\"CG\")\nprint(v.to_string())\nprint(\"reading (a) for all three:\", bool(v.reading_a.all()), \"; reading (b) for all three:\", bool(v.reading_b.all()))\n\n# %% md\n## fig8a-ganglion-difference\n\n> The fraction of time with a normal rhythm peaks near control in both ganglia, but the CG is more sensitive to extreme base and the STG to extreme acid; pH, ganglion and their interaction all had significant effects in both acid and base, and the pyloric rhythm was significantly less rhythmic than the cardiac at pH 5.5 and more rhythmic at pH 9.3 and 9.8.\n\nCriterion: [MIX] on the per-preparation fraction rhythmic (proxy) of both ganglia, readings (a) sum-to-zero and (b) treatment contrasts for ganglion, each with (c) univariate and (d) multivariate tests; Welch t-tests per pH, corrected by 4 (acid) or 5 (base).\n\n# %% [claim:fig8a-ganglion-difference]\ndef fig8a(stg, cg, show=True):\n    out = {}\n    for coding in (\"sum\", \"treatment\"):\n        for proto, cols in ((\"acid\", C.ACID), (\"base\", C.BASE)):\n            m = C.mixed_anova(cg, stg, cols, coding)\n            for eff in (\"pH\", \"ganglion\", \"interaction\"):\n                r = m[eff]\n                out[(coding, proto, eff)] = dict(F_uni=r[\"F\"], p_uni=r[\"p\"], pillai=r.get(\"pillai\", np.nan), p_multi=r.get(\"p_pillai\", r[\"p\"]), n=m[\"n\"])\n    tab = pd.DataFrame(out).T\n    welch = {}\n    for s, k in ((\"5.5\", 4), (\"9.3\", 5), (\"9.8\", 5), (\"6.1\", 4), (\"6.7\", 4), (\"7.2\", 4), (\"8.3\", 5), (\"8.8\", 5), (\"10.4\", 5)):\n        tt = stats.ttest_ind(stg[s], cg[s], equal_var=False)\n        welch[s] = dict(stg=stg[s].mean(), cg=cg[s].mean(), t=tt.statistic, p_corr=min(1.0, tt.pvalue * k))\n    welch = pd.DataFrame(welch).T\n    if show:\n        print(tab.assign(F_uni=tab.F_uni.astype(float).round(2), p_uni=tab.p_uni.map(\"{:.3g}\".format), pillai=tab.pillai.astype(float).round(3),\n                         p_multi=tab.p_multi.map(\"{:.3g}\".format)).to_string())\n        print(welch.round(4).to_string())\n    return tab, welch\nstg_r, cg_r = rhythm[(\"STG\", \"zero\")], rhythm[(\"CG\", \"zero\")]\ntab, welch = fig8a(stg_r, cg_r)\ntt_ok = welch.loc[\"5.5\", \"stg\"] < welch.loc[\"5.5\", \"cg\"] and welch.loc[\"5.5\", \"p_corr\"] < 0.05\ntt_ok = [tt_ok] + [welch.loc[s, \"stg\"] > welch.loc[s, \"cg\"] and welch.loc[s, \"p_corr\"] < 0.05 for s in (\"9.3\", \"9.8\")]\nfor coding in (\"sum\", \"treatment\"):\n    for col in (\"p_uni\", \"p_multi\"):\n        sig = [tab.loc[(coding, p, e), col] < 0.05 for p in (\"acid\", \"base\") for e in (\"pH\", \"ganglion\", \"interaction\")]\n        print(f\"{coding} contrasts, {col}: effects p < 0.05 = {sum(sig)} of 6\")\nprint(\"t-tests (STG lower at 5.5, higher at 9.3 and 9.8):\", tt_ok)\nprint(\"mean fraction rhythmic, STG:\", stg_r.mean().round(3).to_dict()); print(\"CG:\", cg_r.mean().round(3).to_dict())\nfor f in (2.0, 5.0):\n    print(f\"variant proxy factor {f}:\"); fig8a(proxy_var[f][\"STG\"], proxy_var[f][\"CG\"])\n\n# %% md\n## fig8b-individual-preparations\n\n> All preparations were rhythmic at control; 14 of 15 STG preparations stopped firing after 15 min at pH 5.5, only 6 of 15 CG preparations lost rhythmic activity at pH 5.5, and 3 of 15 CG preparations kept a normal rhythm in every pH condition.\n\nExpected counts 14 (± 1.4), 6 (± 0.6), 3 (± 0.3). Readings as in the criterion. \"Ceased firing\" (a) state 4 at the end of the step is read as no PD spikes in the last 10 s; (b) no PD bursts in the last minute; (c) fraction rhythmic 0. The STG preparations lacking 5.5 (877_093, 887_069) count as not firing under the code's zero rule and are shown apart.\n\n# %% [claim:fig8b-individual-preparations]\nrows = []\nfor u in units:\n    if u[\"ganglion\"] != \"STG\" or u[\"out\"] is None:\n        continue\n    v = u[\"out\"][\"5.5\"]\n    if v is None:\n        rows.append(dict(prep=u[\"label\"], has_55=False)); continue\n    r = R[v[\"file\"]][\"ext\"][u[\"channel\"]]\n    spikes_last10 = int(((r[\"late\"][0] >= v[\"seconds\"] - 10) & (r[\"late\"][1] >= v[\"thr\"])).sum())\n    bursts_lastmin = int((v[\"bursts\"].tstart >= v[\"seconds\"] - 60).sum())\n    rows.append(dict(prep=u[\"label\"], has_55=True, spikes_last10s=spikes_last10, bursts_last_min=bursts_lastmin, frac_rhythmic=v[\"rhythmic\"].mean()))\ns55 = pd.DataFrame(rows)\nprint(s55.round(3).to_string(index=False))\nhave = s55[s55.has_55]\ncease = {\"a\": int((have.spikes_last10s == 0).sum()), \"b\": int((have.bursts_last_min == 0).sum()), \"c\": int((have.frac_rhythmic == 0).sum())}\nn_missing = int((~s55.has_55).sum())\nprint(\"STG ceased at 5.5, of\", len(have), \"with a 5.5 file:\", cease, f\"; plus {n_missing} without a 5.5 file (counted as 0 by the code's rule)\")\ncg = rhythm[(\"CG\", \"zero\")]\nred = {\"a\": int((cg[\"5.5\"] < 1).sum()), \"b\": int((cg[\"5.5\"] < cg[\"ctl_acid\"]).sum())}\nnormal = {\"a\": int((cg[C.COLUMNS] >= 1).all(axis=1).sum()), \"b\": int((cg[[\"5.5\", \"ctl_acid\", \"10.4\"]] >= 1).all(axis=1).sum())}\nctl = {\"STG a\": int((stg_r[\"ctl_acid\"] >= 1).sum()), \"STG b\": int((stg_r[\"ctl_acid\"] >= 0.5).sum()), \"CG a\": int((cg[\"ctl_acid\"] >= 1).sum()), \"CG b\": int((cg[\"ctl_acid\"] >= 0.5).sum())}\nprint(\"CG with reduced rhythm at 5.5 (of\", len(cg), \"):\", red, \"; CG normal in every condition:\", normal)\nprint(\"rhythmic at control before acid (counts):\", ctl, \"of\", len(stg_r), \"STG and\", len(cg), \"CG\")\nprint(\"Figure 8B STG control column is the recovery from acid in pHCumulative.m:\", int((stg_r[\"rec_acid\"] >= 1).sum()), \"of\", len(stg_r), \"STG fully rhythmic there\")\nfor f in (2.0, 5.0):\n    cgv, stv = proxy_var[f][\"CG\"], proxy_var[f][\"STG\"]\n    print(f\"proxy factor {f}: CG reduced at 5.5 (a) {int((cgv['5.5'] < 1).sum())}, (b) {int((cgv['5.5'] < cgv['ctl_acid']).sum())}; \"\n          f\"CG normal everywhere (a) {int((cgv[C.COLUMNS] >= 1).all(axis=1).sum())}, (b) {int((cgv[['5.5', 'ctl_acid', '10.4']] >= 1).all(axis=1).sum())}; \"\n          f\"STG fraction 0 at 5.5 {int((stv.loc[have.prep, '5.5'] == 0).sum())}\")\n\n# %% md\n## fig8b-cross-predictive\n\n> STG preparations with reduced activity in base were very susceptible to loss of activity in extreme acid, while in the CG it was the reverse, activity in acid predicting activity in base.\n\nCriterion reading (a): every STG preparation with fraction below 1 at 10.4 has fraction 0 at 5.5, every CG preparation below 1 at 5.5 is below 1 at 10.4, and the reverse implication fails in each ganglion for at least one preparation; (b) Fisher tables shown.\n\n# %% [claim:fig8b-cross-predictive]\ndef cross(fr, g):\n    red55, red104 = fr[\"5.5\"] < 1, fr[\"10.4\"] < 1\n    tab = pd.crosstab(red55.rename(\"reduced at 5.5\"), red104.rename(\"reduced at 10.4\"))\n    print(g); print(tab.to_string())\n    full = np.array([[((~red55) & (~red104)).sum(), ((~red55) & red104).sum()], [(red55 & ~red104).sum(), (red55 & red104).sum()]])\n    print(\"Fisher exact p:\", stats.fisher_exact(full).pvalue)\n    return red55, red104\nr55, r104 = cross(stg_r, \"STG\")\nstg_imp = bool((stg_r.loc[r104, \"5.5\"] == 0).all()); stg_rev_fails = bool(((stg_r[\"5.5\"] == 0) & ~r104).any())\nprint(\"STG: every one reduced at 10.4 has 0 at 5.5:\", stg_imp, list(stg_r.index[r104]), \"; reverse fails for one:\", stg_rev_fails)\nc55, c104 = cross(cg_r, \"CG\")\ncg_imp = bool(c104[c55].all()); cg_rev_fails = bool((c104 & ~c55).any())\nprint(\"CG: every one reduced at 5.5 is reduced at 10.4:\", cg_imp, \"; reverse fails for one:\", cg_rev_fails)\nprint(\"reading (a) holds:\", stg_imp and stg_rev_fails and cg_imp and cg_rev_fails)\n\n# %% md\n## baseline-frequency-correlations\n\n> Frequency at control correlates strongly with frequency in extreme acid and in extreme base for PD neurons, and LC frequency at control correlates strongly with LC frequency in extreme acid but not in extreme base.\n\nReadings: PD data (a) extracellular STG, (b) PTX PD burst frequency; correlation Pearson or Spearman; \"strong\" (a) positive with p < 0.05, (b) r ≥ 0.7. Control just before each protocol against 5.5 and 10.4. A missing step is left out of its correlation.\n\n# %% [claim:baseline-frequency-correlations]\ndef corr(df, ctl, ext):\n    d = df[[ctl, ext]].dropna()\n    return dict(n=len(d), pearson=stats.pearsonr(d[ctl], d[ext]), spearman=stats.spearmanr(d[ctl], d[ext]))\nsets = {\"PD (a) extracellular\": measures[(\"STG\", \"hz\", \"nan\")], \"PD (b) PTX\": ptx[(\"PD\", \"burst_hz_trough\")], \"LC\": measures[(\"CG\", \"hz\", \"nan\")]}\nrows = []\nfor name, df in sets.items():\n    for proto, ctl, ext in ((\"acid\", \"ctl_acid\", \"5.5\"), (\"base\", \"ctl_base\", \"10.4\")):\n        c = corr(df, ctl, ext)\n        for kind in (\"pearson\", \"spearman\"):\n            rr = c[kind]\n            rows.append(dict(data=name, protocol=proto, method=kind, n=c[\"n\"], r=rr.statistic, p=rr.pvalue))\ncr = pd.DataFrame(rows)\nprint(cr.assign(r=cr.r.round(3), p=cr.p.map(\"{:.3g}\".format)).to_string(index=False))\ndef strong(r, p, rule): return (r > 0 and p < 0.05) if rule == \"a\" else r >= 0.7\ncombos = []\nfor pdset in (\"PD (a) extracellular\", \"PD (b) PTX\"):\n    for kind in (\"pearson\", \"spearman\"):\n        for rule in (\"a\", \"b\"):\n            g = lambda d, pr: cr[(cr.data == d) & (cr.protocol == pr) & (cr.method == kind)].iloc[0]\n            ok = (strong(g(pdset, \"acid\").r, g(pdset, \"acid\").p, rule) and strong(g(pdset, \"base\").r, g(pdset, \"base\").p, rule)\n                  and strong(g(\"LC\", \"acid\").r, g(\"LC\", \"acid\").p, rule) and not strong(g(\"LC\", \"base\").r, g(\"LC\", \"base\").p, rule))\n            combos.append(dict(pd_data=pdset, method=kind, strong=rule, holds=ok))\nprint(pd.DataFrame(combos).to_string(index=False))\n\n# %% md\n## robust-6-1-to-8-8\n\n> Both the pyloric and cardiac rhythms remained robust from about pH 6.1 to pH 8.8.\n\nCriterion: a claim of absence on the paper's tests: in [RM] of fraction rhythmic (proxy) for each ganglion, no corrected paired t-test at 6.1, 6.7, 7.2, 8.3 or 8.8 shows a significant decrease.\n\n# %% [claim:robust-6-1-to-8-8]\nfor g in (\"STG\", \"CG\"):\n    a, b, t = C.rm_report(rhythm[(g, \"zero\")], f\"{g} fraction rhythmic\", show=False)\n    sub = t.loc[[\"6.1\", \"6.7\", \"7.2\", \"8.3\", \"8.8\"]]\n    print(g, \"means:\", sub.mean_step.round(3).to_dict(), \"; corrected p:\", sub.p_corr.round(3).to_dict(),\n          \"; significant decreases:\", int(((sub.p_corr < 0.05) & (sub[\"diff\"] < 0)).sum()))\n    for f in (2.0, 5.0):\n        _, _, tv = C.rm_report(proxy_var[f][g], \"\", show=False)\n        print(f\"   proxy factor {f}: significant decreases 6.1 to 8.8:\", int(((tv.loc[['6.1', '6.7', '7.2', '8.3', '8.8'], 'p_corr'] < 0.05) & (tv.loc[['6.1', '6.7', '7.2', '8.3', '8.8'], 'diff'] < 0)).sum()))\n\n# %% md\n## intact-depolarize-in-acid\n\n> In intact (no PTX) preparations both PD and LP neurons depolarized in acid, unlike the semi-isolated neurons where only PD did.\n\nCriterion: intact STG preparations with intracellular PD and LP, minimum membrane potential of [INTRA] in the last minute, [RM] on the acid protocol; readings (a) acid ANOVA p < 0.05 and higher mean at 5.5 than control, (b) higher at 5.5 than control in most preparations; for both neurons. Preparations lacking 5.5 are left out of the ANOVA.\n\n# %% [claim:intact-depolarize-in-acid]\nfor unit in (\"PD\", \"LP\"):\n    for k in (\"vmin_methods\", \"vmin_code\"):\n        df = intact[(unit, k)]\n        a, b, t = C.rm_report(df, f\"intact {unit} minimum Vm ({k})\", show=(k == \"vmin_methods\"))\n        d = (df[\"5.5\"] - df[\"ctl_acid\"]).dropna()\n        print(f\"{unit} {k}: preparations {len(df)} ({list(df.index)}); with 5.5: {len(d)}; acid ANOVA p = {a['p']:.3g}; \"\n              f\"mean 5.5 minus control {d.mean():.2f} mV; higher at 5.5 in {int((d > 0).sum())} of {len(d)}; \"\n              f\"(a) {a['p'] < 0.05 and d.mean() > 0}; (b) {(d > 0).sum() > len(d) / 2}\")\n\n# %%\nprint(f\"notebook ran {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% md\n## Summary\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''ok_b = r.loc["hz_acid", "b"] > 0 and r.loc["hz_base", "b"] < 0 and r.loc["spikes_acid", "a"] < 0 and r.loc["duty_base", "b"] < 0
print("reading (a) holds:", ok_a, "; reading (b) holds:", ok_b,
      "(in (b) 'frequency higher in acid' is a positive... see note)")''','''# (b): a rise in acid is a negative rho with pH over the acid steps; a fall in base is a negative rho over the base steps
ok_b = r.loc["hz_acid", "b"] < 0 and r.loc["hz_base", "b"] < 0 and r.loc["spikes_acid", "a"] < 0 and r.loc["duty_base", "b"] < 0
print("reading (a) holds:", ok_a, "; reading (b) holds:", ok_b, "(spikes at 5.5 against control is the same in both)")''')
i=s.index('# %% md\n**Result: reproduced, on the proxy for states.**')
j=s.index('## fig2bcd-stg1-measures')
s=s[:i]+'# %% md\n'+s[j:]
open('nb_src.py','w').write(s)
EOF
cat > $TMPDIR/devrun.py <<'EOF'
import re, sys, pickle, time
sys.path.insert(0,'entries/haley-2018')
src=open(sys.argv[1]).read()
cells=re.split(r'^# %%(.*)$', src, flags=re.M)
g={}
stop=sys.argv[2] if len(sys.argv)>2 else None
for hdr,body in zip(cells[1::2],cells[2::2]):
    if hdr.strip().startswith('md'): continue
    if 'C.osf_listing()' in body: continue
    if 'ext_results = C.run_jobs' in body:
        body="plans,missing_exps,jobs,ext_results=pickle.load(open('full_ext.pkl','rb'))\nptx_jobs,ptx_results=pickle.load(open('full_ptx.pkl','rb'))\nimport pickle\n"
        body="import pickle\n"+body
    if 'plans, missing_exps, jobs = C.plan_extracellular()' in body:
        body=body.replace('plans, missing_exps, jobs = C.plan_extracellular()',"import pickle\nplans,missing_exps,jobs,_=pickle.load(open('full_ext.pkl','rb'))")
    print('\n########', hdr.strip()); sys.stdout.flush()
    exec(body,g)
EOF
cd $TMPDIR && timeout 1200 python devrun.py nb_src.py 2>&1 | tail -c 60000
```

```
<persisted-output>
Output too large (64.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/bnv7l4nu0.txt

Preview (first 2KB):
        unit ganglion channel order  thr_control  noise_sd  median_spike_height  control_period_s  control_bursts       note
     877_093      STG   IN 12    BA       0.1645    0.0060               0.4112             0.657           729.0        NaN
     877_101      STG     NaN   NaN          NaN       NaN                  NaN               NaN             NaN no channel
     877_121      STG   IN 13    AB       0.2060    0.0128               0.5150             0.852           564.0        NaN
     877_141      STG    IN 9    AB       0.1057    0.0071               0.2641             0.688           698.0        NaN
877_149 CG1L       CG   IN 13    AB       0.0867    0.0053               0.1367             2.492           173.0        NaN
877_149 CG2L       CG   IN 11    AB       0.1521    0.0038               0.2444             6.582            74.0        NaN
     887_005      STG   IN 13    BA       0.0934    0.0068               0.1585             0.822           585.0        NaN
887_005 CG2L       CG   IN 11    BA       1.4403    0.0042               3.3455             3.489           137.0        NaN
887_011 CG3L       CG   IN 11    BA       1.2438    0.0041               2.8558             4.380           111.0        NaN
     887_049      STG   IN 11    AB       0.0600    0.0044               0.0912             0.547           877.0        NaN
887_061 CG1L       CG   IN 12    AB       0.1536    0.0055               0.3166             2.615           183.0        NaN
887_065 CG2L       CG   IN 13    AB       0.2152    0.0053               0.5180             4.187           115.0        NaN
     887_069      STG   IN 11    AB       0.0882    0.0048               0.2205             0.709           678.0        NaN
887_073 CG2L    
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "Error\|Traceback\|########" /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/bnv7l4nu0.txt | head -60; tail -30 /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/bnv7l4nu0.txt
```

```
155:######## 
169:######## [claim:fig2a-stg1-traces]
191:######## [claim:fig2bcd-stg1-measures]
215:######## [claim:fig3c-stg-rhythmic-fraction]
263:######## [claim:fig3d-stg-frequency]
311:######## [claim:fig3e-stg-spikes-per-burst]
347:######## [claim:fig3f-stg-duty-cycle]
383:######## [claim:fig3s2-stg-control-variability]
390:######## [claim:fig4a-ptx-example]
405:######## [claim:fig4bc-membrane-potential]
455:######## [claim:fig4de-spike-amplitude]
480:######## [claim:fig4fg-ptx-frequency]
517:######## [claim:fig6-cg1-measures]
551:######## [claim:fig6a-cg2-less-rhythmic]
565:######## [claim:fig7b-cg-rhythmic-fraction]
623:######## [claim:fig7c-cg-frequency]
640:######## [claim:fig7d-cg-spikes-per-burst]
657:######## [claim:fig7e-cg-duty-cycle]
674:######## [claim:fig7s2-cg-control-variability]
681:######## [claim:fig8a-ganglion-difference]
[... 37 more lines not kept]
```

**Agent**

All cells run on the cached data. Reading the outputs claim by claim.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/bnv7l4nu0.txt",
 "offset": 1,
 "limit": 160
}
```

```
1	        unit ganglion channel order  thr_control  noise_sd  median_spike_height  control_period_s  control_bursts       note
2	     877_093      STG   IN 12    BA       0.1645    0.0060               0.4112             0.657           729.0        NaN
3	     877_101      STG     NaN   NaN          NaN       NaN                  NaN               NaN             NaN no channel
4	     877_121      STG   IN 13    AB       0.2060    0.0128               0.5150             0.852           564.0        NaN
5	     877_141      STG    IN 9    AB       0.1057    0.0071               0.2641             0.688           698.0        NaN
6	877_149 CG1L       CG   IN 13    AB       0.0867    0.0053               0.1367             2.492           173.0        NaN
7	877_149 CG2L       CG   IN 11    AB       0.1521    0.0038               0.2444             6.582            74.0        NaN
8	     887_005      STG   IN 13    BA       0.0934    0.0068               0.1585             0.822           585.0        NaN
9	887_005 CG2L       CG   IN 11    BA       1.4403    0.0042               3.3455             3.489           137.0        NaN
10	887_011 CG3L       CG   IN 11    BA       1.2438    0.0041               2.8558             4.380           111.0        NaN
11	     887_049      STG   IN 11    AB       0.0600    0.0044               0.0912             0.547           877.0        NaN
12	887_061 CG1L       CG   IN 12    AB       0.1536    0.0055               0.3166             2.615           183.0        NaN
13	887_065 CG2L       CG   IN 13    AB       0.2152    0.0053               0.5180             4.187           115.0        NaN
14	     887_069      STG   IN 11    AB       0.0882    0.0048               0.2205             0.709           678.0        NaN
15	887_073 CG2L       CG   IN 12    BA       0.7396    0.0061               1.8379             4.078           118.0        NaN
16	887_093 CG2L       CG   IN 12    AB       0.8289    0.0058               1.6294       
[... 144 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/bnv7l4nu0.txt",
 "offset": 160,
 "limit": 260
}
```

```
160	factor 3.0: mean fraction rhythmic per condition
161	     rec_acid    5.5    6.1    6.7    7.2  ctl_acid  ctl_base    8.3    8.8    9.3    9.8   10.4  rec_base
162	STG     1.000  0.393  0.859  0.958  1.000       1.0     1.000  1.000  0.955  0.846  0.766  0.771     0.923
163	CG      0.986  0.817  0.964  1.000  0.929       1.0     0.991  0.987  0.912  0.550  0.399  0.326     0.980
164	factor 5.0: mean fraction rhythmic per condition
165	     rec_acid    5.5    6.1   6.7    7.2  ctl_acid  ctl_base  8.3    8.8    9.3    9.8   10.4  rec_base
166	STG     1.000  0.401  0.876  0.97  1.000       1.0     1.000  1.0  0.971  0.847  0.785  0.787     0.923
167	CG      0.994  0.892  1.000  1.00  0.939       1.0     0.998  1.0  0.975  0.692  0.457  0.384     0.994
168	
169	######## [claim:fig2a-stg1-traces]
170	order AB ; fraction rhythmic (proxy) per condition:
171	rec_acid    1.0
172	5.5         1.0
173	6.1         1.0
174	6.7         1.0
175	7.2         1.0
176	ctl_acid    1.0
177	ctl_base    1.0
178	8.3         1.0
179	8.8         1.0
[... 240 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9624b1f7-5218-4a07-9bc7-7d6b41450948/tool-results/bnv7l4nu0.txt",
 "offset": 419,
 "limit": 420
}
```

```
419	step  n  mean_control  mean_step    diff     t        p   p_corr
420	 7.2  9       -35.815    -34.392   1.423 -2.23   0.0566    0.227
421	 6.7  9       -35.815    -34.487   1.328 -1.26    0.243    0.971
422	 6.1  8       -34.732    -33.076   1.656 -1.28    0.243    0.972
423	 5.5  9       -35.815    -35.210   0.605 -0.32    0.757        1
424	 8.3  9       -35.418    -35.540  -0.122  0.34    0.744        1
425	 8.8  9       -35.418    -37.637  -2.219  4.00  0.00396   0.0198
426	 9.3  9       -35.418    -44.953  -9.535  5.62 0.000499  0.00249
427	 9.8  9       -35.418    -47.472 -12.054  7.49 7.01e-05 0.000351
428	10.4  8       -34.616    -47.192 -12.577  9.13  3.9e-05 0.000195
429	PD acid ANOVA p < 0.05: True ; LP base ANOVA p < 0.05: True ; t-tests: {'PD 5.5': np.True_, 'PD 6.1': np.True_, 'LP 8.8': np.True_, 'LP 9.3': np.True_, 'LP 9.8': np.True_, 'LP 10.4': np.True_} ; absence: LP acid ANOVA p = 0.648, PD base ANOVA p = 0.128
430	== vmin_code
431	PD minimum Vm (vmin_code): acid ANOVA F(4,28) = 31.02, p = 6.4e-10 (n = 8); base ANOVA F(5,35) = 2.03, p = 0.0986 (n = 8)
432	step  n  mean_control  mean_step   diff      t        p   p_corr
433	 7.2  9       -46.217    -44.844  1.373  -2.81   0.0228   0.0913
434	 6.7  9       -46.217    -41.071  5.147  -3.22   0.0123   0.0491
435	 6.1  8       -45.667    -34.052 11.615  -4.18  0.00416   0.0166
436	 5.5  9       -46.217    -27.244 18.973 -16.59 1.76e-07 7.05e-07
437	 8.3  9       -43.692    -47.506 -3.814   1.59     0.15     0.75
438	 8.8  9       -43.692    -47.967 -4.275   1.22    0.256        1
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && grep -n "^# %% md$" nb_src.py | head -80 | wc -l
```

```
Thu Nov 26 01:53:43 UTC 2026
32
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results_md.py <<'PYEOF'
R = {
"fig2a-stg1-traces": """**Result: reproduced, on the state proxy (assumed).** 897_037 is rhythmic by the proxy over the whole of every step from 7.2 to 6.1 and from 8.3 to 10.4 and in both recoveries, and also at 5.5 (reading (a)), under gap factors 2, 3 and 5. At 10.4 PD spikes per burst (12.43 against 13.10) and the PD slow-wave amplitude (17.65 against 18.03 mV) are lower than at the control before the base steps, both by small margins. The proxy follows PD only, so "triphasic" rests on PD bursting.""",
"fig2bcd-stg1-measures": """**Result: reproduced (assumed: automatic spike thresholds).** In 897_037 frequency is higher at 5.5 than at its control (+0.118 Hz) and lower at 10.4 (-0.266 Hz); its Spearman rho with pH is -0.80 over the acid steps and -1.00 over the base steps. PD spikes per burst at 5.5 are 5.40 below control, and duty cycle at 10.4 is 0.048 below control (rho -0.94 over the base steps). Both readings hold. In the code's window the frequency and spike parts hold, and duty cycle in base falls by 0.023 (rho -0.54).""",
"fig3c-stg-rhythmic-fraction": """**Result: partially reproduced, on the state proxy (assumed).** With 13 STG preparations, both ANOVAs are significant (acid p = 1.0e-07, base p = 0.021). The corrected t-test at 5.5 is significant (fraction 0.393 against 1.0, p = 0.0013), and the one at 10.4 is not (0.771, p = 0.31). The same split holds with missing steps left out and with gap factors 2 and 5 (10.4: p = 0.22 to 0.61). The proxy counts intermittent triphasic activity as rhythmic, which can only raise the STG's fraction in base.""",
"fig3d-stg-frequency": """**Result: partially reproduced (assumed: automatic spike thresholds).** The base part holds in part: base ANOVA p = 4.4e-04, and frequency at 10.4 is lower than control (-0.407 Hz, corrected p = 0.047), while 9.3 is not significant (-0.206 Hz, p = 0.65). The acid ANOVA is significant (p = 1.6e-07), driven by 5.5 (-0.837 Hz, p = 0.0011), where several preparations fall silent and their empty bins count as 0. The claim of absence in acid therefore fails under the Methods window. In the code's window (480 s from the first burst of each file), the acid ANOVA gives p = 0.061, as the paper reports, but no base t-test is significant there.""",
"fig3e-stg-spikes-per-burst": """**Result: reproduced (assumed: automatic spike thresholds).** Acid ANOVA p = 1.6e-11 and base ANOVA p = 1.0e-06 (13 preparations). PD spikes per burst at 5.5 are 2.24 against 9.43 at control (corrected p = 3.2e-05). The result holds with missing steps left out and in the code's window.""",
"fig3f-stg-duty-cycle": """**Result: partially reproduced (assumed: automatic spike thresholds).** Both ANOVAs are significant (acid p = 2.3e-09, base p = 3.6e-10). The duty cycle at 6.1 is 0.023 lower than control, not higher (corrected p = 0.93). In the code's window it is 0.041 higher at 6.1 (p = 0.09).""",
"fig3s2-stg-control-variability": """**Result: reproduced under reading (b) (assumed: automatic spike thresholds).** At the first control step, a Kruskal-Wallis test of the 48 bins on preparation gives p < 1e-100 for frequency, spikes per burst and duty cycle (H 606, 545 and 491; 13 preparations). Under reading (a), the range of the preparation means is 0.48, 0.75 and 0.37 of the pooled range for the three measures, so (a) holds for spikes per burst only.""",
"fig4a-ptx-example": """**Result: reproduced (assumed: the readings of "one spike per burst" and "tonic" named above).** One PTX preparation, 903_052, meets every part. Its PD slow wave at 6.7 is 0.41 of control, and at 5.5 PD is silent and depolarized by 16.4 mV. At 10.4 it fires 1.0 spikes per slow wave, and LP fires tonically at all six steps from 6.7 to 10.4 and is silent at 5.5. Every preparation has a silent, depolarized PD at 5.5, while the other parts hold in two to seven of the nine.""",
"fig4bc-membrane-potential": """**Result: reproduced (assumed: the code's starting parameters for the waveform analysis and the conditions of the PTX files taken from their recorded pH).** PD acid ANOVA p = 6.4e-10 and LP base ANOVA p = 8.9e-14 (8 complete preparations of 9). PD is depolarized at 5.5 (+19.0 mV, corrected p = 7.9e-07) and 6.1 (+11.6 mV, p = 0.016). LP is hyperpolarized at 8.8 (-2.2 mV, p = 0.020), 9.3 (-9.5 mV, p = 0.0025), 9.8 (-12.1 mV, p = 3.5e-04) and 10.4 (-12.6 mV, p = 2.0e-04). The parts claimed relatively constant are not significant: LP acid ANOVA p = 0.65 and PD base ANOVA p = 0.13. The code's slow-wave troughs give the same outcome.""",
"fig4de-spike-amplitude": """**Result: partially reproduced (assumed, as fig4bc).** The acid ANOVAs are significant for PD (p = 1.5e-06) and LP (p = 0.0015), and the PD base ANOVA is not (p = 0.26), as claimed. Amplitude at 5.5 is lower for PD (corrected p = 7.8e-04) and LP (p = 0.0044). The LP base ANOVA is not significant (p = 0.095), and the fall in LP amplitude at 6.1 (-3.4 mV) is not significant (p = 0.11).""",
"fig4fg-ptx-frequency": """**Result: partially reproduced (assumed, as fig4bc).** All four ANOVAs are significant: PD acid p = 7.0e-08, PD base p = 0.0016, LP acid p = 7.3e-09, LP base p = 7.3e-10. Six of the seven named t-tests hold, including PD burst frequency at 5.5 (-1.26 Hz, p = 0.0034) and LP rate at 5.5, 6.1, 9.3, 9.8 and 10.4. LP rate at 8.3 is higher than control, not lower (+2.2 Hz, p = 0.098). The code's peak-to-peak PD frequency gives the same counts.""",
"fig6-cg1-measures": """**Result: partially reproduced (assumed: automatic spike thresholds, the CG burst rule and the state proxy).** In 877_149 CG2L the cardiac frequency is lower at 5.5 than control (-0.044 Hz) and higher at 10.4 (+0.040 Hz), and the duty cycle is lower at 5.5 (-0.133). The unit is rhythmic by the proxy over every step. LC spikes per burst fall in acid (-6.05 at 5.5, rho +0.80 with pH), and the duty cycle in base does not fall (+0.018 at 10.4, rho +0.20). Both parts fail under both readings, the 0.3 s burst rule and the code's window.""",
"fig6a-cg2-less-rhythmic": """**Result: reproduced, on the state proxy (assumed).** Of the 8 other acid-first CG units, one, 887_093 CG2L, meets the criterion under gap factors 2, 3 and 5. Its rhythmic fraction is 0.38 at 5.5 and 0 at 9.8 and 10.4, against 1.0 at control. Every step from 6.1 to 9.3 is at least 0.63, and the final recovery is 1.0.""",
"fig7b-cg-rhythmic-fraction": """**Result: not reproduced, on the state proxy (assumed).** The base ANOVA is significant (p = 9.9e-10), and so are the decreases at 9.3, 9.8 and 10.4 (fraction 0.55, 0.40 and 0.33 against 0.99; corrected p 0.012 to 5.9e-04). The acid ANOVA is not (p = 0.058), and the fall at 5.5 (0.82 against 1.0) is not significant (p = 0.25). So neither the criterion's full nor its partial condition (both ANOVAs) is met. With gap factor 2 the acid ANOVA gives p = 0.023, and 5.5 is still not significant (p = 0.12).""",
"fig7c-cg-frequency": """**Result: not reproduced (assumed: automatic spike thresholds and the CG burst rule).** The mean LC frequency at 10.4 is 0.092 Hz below control, but the corrected t-test is not significant (p = 0.84). The base ANOVA gives p = 0.056, and neither reading's ANOVA condition holds. No variant (missing steps left out, the code's window, the 0.3 s burst rule) makes 10.4 significant (p = 0.18 to 1). Frequency at 5.5 is 0.059 Hz below the acid control.""",
"fig7d-cg-spikes-per-burst": """**Result: not reproduced (assumed: automatic spike thresholds and the CG burst rule).** The base ANOVA is significant (p = 3.7e-05), and LC spikes per burst fall at 10.4 (-2.84, corrected p = 9.2e-04). The acid ANOVA is not (p = 0.54). The increases at 5.5 (+1.27) and 6.1 (+0.61) and the fall at 9.8 (-2.06, p = 0.26) are not significant. One of the four t-tests holds, and the acid ANOVA fails, under every variant.""",
"fig7e-cg-duty-cycle": """**Result: reproduced (assumed: automatic spike thresholds and the CG burst rule).** Base ANOVA p = 4.8e-05 and acid ANOVA p = 0.52 (14 units), and the outcome is the same under every variant shown (base p 5.0e-04 to 0.0091; acid p 0.13 to 0.52). The acid effects are at most 0.014 in duty cycle.""",
"fig7s2-cg-control-variability": """**Result: reproduced under reading (b) (assumed, as fig7c).** The Kruskal-Wallis test of the control bins on unit gives p < 1e-90 for all three measures (14 units). Under reading (a), the preparation means span 0.39, 0.79 and 0.62 of the pooled range, so (a) fails for frequency.""",
"fig8a-ganglion-difference": """**Result: not reproduced, on the state proxy (assumed).** With sum-to-zero contrasts, all six effects are significant under both univariate and multivariate tests: pH (p = 5.9e-10 acid, 2.8e-12 base), ganglion (0.034, 0.015) and interaction (5.7e-04, 0.0040). With treatment contrasts, the acid pH effect is not (p = 0.15). The STG is less rhythmic than the CG at 5.5 (0.39 against 0.82, corrected p = 0.042). It is more rhythmic at 9.3 (0.85 against 0.55) and 9.8 (0.77 against 0.40), but not significantly (p = 0.36 and 0.21). The criterion needs all three t-tests, and its partial condition also needs them. With gap factor 2, 9.8 becomes significant (p = 0.023) but 5.5 does not (p = 0.090).""",
"fig8b-individual-preparations": """**Result: not reproduced, on the state proxy (assumed).** Of 11 STG preparations with a 5.5 file, 6 have no PD spikes in its last 10 s (reading a) and 6 no PD bursts in its last minute (b). 4 have a rhythmic fraction of 0 (c). Counting the 2 preparations that lack 5.5 as silent gives at most 8 of 13, against 14 of 15 (tolerance 1.4). 877_141, 887_141 and 897_037 burst throughout 5.5. Of 14 CG units, 5 have a reduced fraction at 5.5 (expected 6 ± 0.6), and 2 are fully rhythmic in every condition (expected 3 ± 0.3; 3 under gap factor 5, reading a). Every preparation is fully rhythmic at control.""",
"fig8b-cross-predictive": """**Result: not reproduced, on the state proxy (assumed).** Of the 4 STG preparations reduced at 10.4, 877_093, 877_121, 887_005 and 887_137, not all have a fraction of 0 at 5.5. In the CG, 1 of 5 units reduced at 5.5 is not reduced at 10.4. Neither Fisher test is significant (p = 1.0 in both ganglia).""",
"baseline-frequency-correlations": """**Result: not reproduced (assumed: automatic spike thresholds).** LC frequency at control correlates with LC frequency at 5.5 (Pearson r = 0.73, p = 0.0033; 14 units) and not at 10.4 (r = -0.16, p = 0.66), as claimed. For PD, the extracellular frequencies correlate weakly and not significantly (r = 0.40 at 5.5, 0.48 at 10.4; p 0.22 and 0.12). In the PTX preparations the correlation at 5.5 is negative (r = -0.81) and at 10.4 r = 0.34. No combination of readings makes both PD correlations strong.""",
"robust-6-1-to-8-8": """**Result: reproduced, on the state proxy (assumed).** No corrected t-test from 6.1 to 8.8 shows a significant decrease, in either ganglion (STG smallest corrected p 0.53, CG 0.68), under gap factors 2, 3 and 5. The mean fractions there are 0.86 to 1.0 (STG) and 0.91 to 1.0 (CG).""",
"intact-depolarize-in-acid": """**Result: reproduced (assumed: the code's starting parameters for the waveform analysis).** In intact preparations, PD (7 with 5.5 of 9) and LP (5 of 6) are depolarized at 5.5 against the acid control, by 18.2 and 11.7 mV. Every preparation is depolarized, and the acid ANOVAs give p = 2.9e-11 (PD) and 6.9e-05 (LP). The code's slow-wave troughs give the same outcome.""",
}
PYEOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('results_md.py').read()
s=s.replace("a Kruskal-Wallis test of the 48 bins on preparation gives p < 1e-100 for frequency, spikes per burst and duty cycle (H 606, 545 and 491; 13 preparations)","a Kruskal-Wallis test of the 48 bins on preparation gives H = 606, 545 and 491 for frequency, spikes per burst and duty cycle (13 preparations; p prints as 0, below double precision)")
s=s.replace("The Kruskal-Wallis test of the control bins on unit gives p < 1e-90 for all three measures (14 units).","The Kruskal-Wallis test of the control bins on unit gives H = 625, 516 and 468 for the three measures (14 units; p prints as 0).")
s=s.replace("One of the four t-tests holds, and the acid ANOVA fails, under every variant.","One or two of the four t-tests hold, and the acid ANOVA fails (p 0.13 to 0.54), under every variant.")
open('results_md.py','w').write(s)
EOF
cat >> $TMPDIR/results_md.py <<'PYEOF'

SUMMARY = """## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig2a-stg1-traces | reproduced (assumed) |
| fig2bcd-stg1-measures | reproduced (assumed) |
| fig3a-stg-variability-examples | blocked, metadata_insufficient |
| fig3c-stg-rhythmic-fraction | partially reproduced (assumed) |
| stg-state-transitions | blocked, metadata_insufficient |
| fig3d-stg-frequency | partially reproduced (assumed) |
| fig3e-stg-spikes-per-burst | reproduced (assumed) |
| fig3f-stg-duty-cycle | partially reproduced (assumed) |
| fig3s2-stg-control-variability | reproduced (assumed) |
| fig4a-ptx-example | reproduced (assumed) |
| fig4bc-membrane-potential | reproduced (assumed) |
| fig4de-spike-amplitude | partially reproduced (assumed) |
| fig4fg-ptx-frequency | partially reproduced (assumed) |
| gastric-like-rhythm-counts | blocked, methods_underspecified |
| gastric-conditions-co-occur | blocked, methods_underspecified |
| fig5-gastric-recovery-example | blocked, methods_underspecified |
| fig6-cg1-measures | partially reproduced (assumed) |
| fig6a-cg2-less-rhythmic | reproduced (assumed) |
| fig7b-cg-rhythmic-fraction | not reproduced (assumed) |
| cg-state-transitions | blocked, metadata_insufficient |
| fig7c-cg-frequency | not reproduced (assumed) |
| fig7d-cg-spikes-per-burst | not reproduced (assumed) |
| fig7e-cg-duty-cycle | reproduced (assumed) |
| fig7s2-cg-control-variability | reproduced (assumed) |
| fig8a-ganglion-difference | not reproduced (assumed) |
| fig8b-individual-preparations | not reproduced (assumed) |
| fig8b-cross-predictive | not reproduced (assumed) |
| baseline-frequency-correlations | not reproduced (assumed) |
| robust-6-1-to-8-8 | reproduced (assumed) |
| intact-depolarize-in-acid | reproduced (assumed) |

How the analysis differs from the paper's:

- Spikes are found with automatic thresholds (an Otsu split for PD on the pdn; a fraction of the largest events for the LC on the CG trunk), where the authors set thresholds by hand in Spike2. CG bursts use a 1.0 s maximum interval and one spike, where the code's starting values are 0.3 s and two spikes (shown as a variant).
- The manual state annotations are not in the dataset. Rhythmic activity is a proxy from the pacemaker unit's bursting, which cannot separate the STG states 1 to 3 or the CG states 2 and 3.
- 13 STG preparations (877_127 is not in the project; 877_101 has no pdn) and 14 CG units (887_017 is not in the project) in place of 15 each. A missing pH step counts as 0 in the extracellular measures, as the paper's code gives it; leaving it out is shown as a variant.
- The PTX files have no README; their pH is taken from the recorded bath pH, and a PTX preparation missing a step is left out of that protocol's tests.
- The [INTRA] parameters are the code's starting values, which the authors adjusted by hand.

What was found about the dataset: two experiments the paper's code uses are absent (877_127, 887_017). Seven experiments lack one pH step. The PTX folders have no README, and in two of them the recorded pH shows the 9.3 file before the 8.8 file. In 903_046 one file names the PD and LP electrodes the other way round from the other ten. Several READMEs disagree with their folders (887_145 lists 887_149 file names; 877_149 lists 877_149_00010.abf; two folders hold unlisted files; 887_061 names an IN 15 channel the files do not have). 877_101 has no pdn. The state, burst and gastric annotations behind the paper's figures are not deposited. Every STG and CG file read whole matches its pinned SHA-256."""
PYEOF
cat > $TMPDIR/build_nb.py <<'EOF'
import re, nbformat, sys
sys.path.insert(0, '.')
from results_md import R, SUMMARY
src = open('nb_src.py').read()
parts = re.split(r'^# %%(.*)$', src, flags=re.M)
nb = nbformat.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
for hdr, body in zip(parts[1::2], parts[2::2]):
    hdr = hdr.strip(); body = body.strip("\n")
    if hdr.startswith("md"):
        if body.strip() == "## Summary":
            nb.cells.append(nbformat.v4.new_markdown_cell(SUMMARY)); continue
        if not body.strip():
            continue
        nb.cells.append(nbformat.v4.new_markdown_cell(body)); continue
    tags = re.findall(r'\[([^\]]+)\]', hdr)
    c = nbformat.v4.new_code_cell(body)
    if tags: c.metadata["tags"] = tags
    nb.cells.append(c)
    for t in tags:
        if t.startswith("claim:") and t[6:] in R:
            nb.cells.append(nbformat.v4.new_markdown_cell(R[t[6:]]))
nbformat.write(nb, 'entries/haley-2018/reproduce_haley_2018.ipynb')
print(len(nb.cells), 'cells')
EOF
cd $TMPDIR && . dev/bin/activate && python build_nb.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 1, in <module>
    import re, nbformat, sys
ModuleNotFoundError: No module named 'nbformat'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat pyyaml jsonschema && python build_nb.py
```

```
95 cells
Shell cwd was reset to
```

**Agent**

The notebook is built (95 cells). Next: entry.yaml, requirements, README, then lock and run.

**Agent calls Bash**

```bash
cat entries/fouke-2025/README.md | head -40; python3 -c "import json;print(json.load(open('schemas/entry.schema.json'))['properties'].keys())" 2>/dev/null || ls schemas
```

```
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
| ZF swim in bouts, DC continuously | Reproduced |
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/haley-2018 && cat > entry.yaml <<'EOF'
schema_version: 1
name: haley-2018
type: reproduction
title: Two crab central pattern generators across extreme pH (Haley, Hampton & Marder 2018)
description: Tests the findings of Haley, Hampton and Marder (2018) on OSF project r7aes, the raw
  Axon recordings of the stomatogastric and cardiac ganglia of Cancer borealis across saline pH 5.5
  to 10.4, and of the picrotoxin experiments. It measures PD and Large Cell burst frequency, spikes
  per burst and duty cycle from the extracellular nerves, intracellular PD and LP measures, and a
  proxy for rhythmic activity, and runs the paper's repeated-measures and mixed ANOVAs.
license: Apache-2.0
notebooks:
- path: reproduce_haley_2018.ipynb
  title: Reproducing Haley, Hampton & Marder (2018) from OSF r7aes
  runtime_minutes: 13
helpers:
- crabph.py
- r7aes_files.py
related:
- id: osf:r7aes/2019-01-08T14:49:50
  relation: uses_data
- id: doi:10.7554/elife.41877
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
aiohttp
fsspec
numpy
pandas
pyabf
requests
scipy
EOF
cat > README.md <<'EOF'
# Haley, Hampton & Marder (2018) from OSF r7aes

Tests the findings of [Haley, Hampton & Marder (2018)](https://doi.org/10.7554/elife.41877) on
[OSF:r7aes](https://osf.io/r7aes/), which holds the raw Axon recordings of the paper's
stomatogastric (STG), cardiac (CG) and picrotoxin (PTX) experiments: one file per pH step, with a
README per STG and CG experiment. The manual state annotations and the Spike2 burst output behind
the paper's figures are not in the project.

| Claim | Outcome |
|---|---|
| Example STG and CG preparations (Figures 2, 6) | Reproduced (fig2a, fig2bcd, fig6a); partially reproduced (fig6) |
| STG burst measures across pH (Figure 3D to F, supplement 2) | Reproduced (3e, 3s2); partially reproduced (3d, 3f) |
| STG and CG fraction of time rhythmic (Figures 3C, 7B, 8) | Partially reproduced (3c); not reproduced (7b, 8a, 8b, 8b cross-predictive); reproduced (robust 6.1 to 8.8) |
| Semi-isolated PD and LP with PTX (Figure 4) | Reproduced (4a, 4bc); partially reproduced (4de, 4fg) |
| CG burst measures across pH (Figure 7C to E, supplement 2) | Reproduced (7e, 7s2); not reproduced (7c, 7d) |
| Baseline frequency correlations | Not reproduced |
| Intact PD and LP depolarize in acid | Reproduced |
| State transitions, Figure 3A examples, gastric-like rhythms (Figure 5) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every outcome rests on assumptions the paper leaves open: spike thresholds set automatically where
the authors set them by hand, a proxy for the hand-annotated states, and the pH of the PTX files
taken from their recorded bath pH. The attempt record, with the reasons and the differences from
the paper's method, is [`attempts/haley-2018-01.yaml`](../../attempts/haley-2018-01.yaml).

- `reproduce_haley_2018.ipynb`: the analysis. It streams every STG and CG file whole (about
  57 GB, checking each SHA-256) and the last minute of each PTX file, and takes about 13 minutes.
- `crabph.py`: reading the .abf files from OSF, the READMEs, spikes and bursts, the intracellular
  measures, and the ANOVAs. Other notebooks on this project can import it.
- `r7aes_files.py`: the pinned version, size and SHA-256 of every file.
EOF
cd ../.. && date -u && python tools/entry.py lock entries/haley-2018 2>&1 | tail -5
```

```
Thu Nov 26 01:55:17 UTC 2026
wrote haley-2018/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent**

Lock done. Running check and the full clean run (about 13 min expected).

**Agent calls Bash**

```bash
timeout 5400 python tools/entry.py all entries/haley-2018 2>&1 | tail -30; date -u
```

```
Installed kernelspec registry-haley-2018 in executed/haley-2018/.venv/share/jupyter/kernels/registry-haley-2018
0 error(s)
pass  reproduce_haley_2018.ipynb  (594 s)
Thu Nov 26 02:05:22 UTC 2026
```

**Agent**

Clean run passed in 594 s with 0 check errors. Checking that the executed outputs match the result text.

**Agent calls Bash**

```bash
ls executed/haley-2018/; python3 - <<'EOF'
import json
nb=json.load(open('executed/haley-2018/reproduce_haley_2018.ipynb'))
def out(c): return ''.join(''.join(o.get('text','')) if o['output_type']=='stream' else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    o=out(c)
    if any('error' in x.get('output_type','') for x in c.get('outputs',[])): print('ERROR in',tags)
    if not tags or tags[0] in ('sanity',) or tags[0].startswith('finding'):
        print('====',tags, '\n', o[:2500])
EOF
```

```
reproduce_haley_2018.ipynb
result.json
==== [] 
 OSF project r7aes files pinned as of 2019-01-08T14:49:50 - 408 files

==== [] 
 providers: {'osfstorage': 'listed', 'github': 'HTTP 403 Forbidden'}
osfstorage files now: 408; pinned: 408; changed or gone since pinned: 0; new: 0

==== [] 
 experiments listed by the paper's code and absent from the project: ['877_127', '887_017']
    exp order  files_in_readme  files_used    not_in_readme missing_conditions                              units      intracellular                                  notes
877_093    BA               11          11                                 5.5                           PD:IN 12   PD:VM1_2, LP:VM1                                       
877_101    AB               12          12                                                                PD:None                                                          
877_121    AB               12          12                                                               PD:IN 13                                                          
877_141    AB               12          12                                                                PD:IN 9           PD:VM1_2                                       
877_149    AB               12          12                                                 CG1L:IN 13, CG2L:IN 11                                                          
887_005    BA               11          11                                10.4               PD:IN 13, CG2L:IN 11   PD:VM1, LP:VM1_2                                       
887_011    BA               11          11 887_011_0001.abf               10.4                         CG3L:IN 11                                                          
887_049    AB               12          12 887_049_0026.abf                                              PD:IN 11   PD:VM1, LP:VM1_2                                       
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
old=s[s.index('# %% [finding-readme-mismatch]'):s.index('# %% [finding-ptx-order]')]
new='''# %% [finding-readme-mismatch]
for e, pl in plans.items():
    names = [f for f, _ in pl["desc"]["files"]]
    absent = [(f, r) for f, (r, _) in zip(names, pl["seq_raw"]) if f"{e}/{f}" not in C.FILES]
    if absent:
        print(e, "README names", len(absent), "files not in the folder, e.g.", absent[0][0], "-> matched by number to", absent[0][1])
    if pl["unlisted"]:
        print(e, "folder holds files the README does not list:", [f.split("/")[1] for f in pl["unlisted"]])
    keys = [k for k, _ in pl["desc"]["electrodes"] if k.startswith(("IN", "extra"))]
    per_file = [set(h["channels"]) for h in pl["heads"].values()]
    never = [k for k in keys if not any(k in ch for ch in per_file)]
    some = [k for k in keys if k not in never and not all(k in ch for ch in per_file)]
    if never or some:
        print(e, "README electrodes in no file:", never, "; in only some files:", some)

'''
s=s.replace(old,new)
open('nb_src.py','w').write(s)
EOF
python3 - <<'EOF'
import json
nb=json.load(open('executed/haley-2018/reproduce_haley_2018.ipynb'))
def out(c): return ''.join(''.join(o.get('text','')) if o['output_type']=='stream' else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
for c in nb['cells']:
    tags=c['metadata'].get('tags',[]) if c['cell_type']=='code' else []
    if tags and tags[0].startswith('claim:'):
        o=out(c)
        lines=[l for l in o.splitlines() if any(k in l for k in ('criterion','ANOVA F','holds','meeting','reading','ceased','CG with','t-tests','main:','effects p'))]
        print('==',tags[0]); print('\n'.join(lines[:12]))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'executed/haley-2018/reproduce_haley_2018.ipynb'
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/haley-2018/reproduce_haley_2018.ipynb'))
def out(c): return ''.join(''.join(o.get('text','')) if o['output_type']=='stream' else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
for c in nb['cells']:
    tags=c['metadata'].get('tags',[]) if c['cell_type']=='code' else []
    if tags and tags[0].startswith('claim:'):
        o=out(c)
        lines=[l for l in o.splitlines() if any(k in l for k in ('criterion','ANOVA F','holds','meeting','reading','ceased','CG with','t-tests','main:','effects p'))]
        print('==',tags[0]); print('\n'.join(lines[:12]))
EOF
```

```
== claim:fig2a-stg1-traces

== claim:fig2bcd-stg1-measures
reading (a) holds: True ; reading (b) holds: True (spikes at 5.5 against control is the same in both)
== claim:fig3c-stg-rhythmic-fraction
STG fraction rhythmic, missing steps as 0: acid ANOVA F(4,48) = 14.18, p = 1.03e-07 (n = 13); base ANOVA F(5,60) = 2.88, p = 0.0214 (n = 13)
criterion: True True True False
variant: missing steps left out: acid ANOVA F(4,40) = 12.54, p = 1.06e-06 (n = 11); base ANOVA F(5,55) = 2.85, p = 0.0234 (n = 12)
variant: proxy factor 2.0: acid ANOVA F(4,48) = 12.58, p = 4.47e-07 (n = 13); base ANOVA F(5,60) = 3.05, p = 0.0162 (n = 13)
variant: proxy factor 5.0: acid ANOVA F(4,48) = 15.18, p = 4.33e-08 (n = 13); base ANOVA F(5,60) = 2.71, p = 0.0282 (n = 13)
== claim:fig3d-stg-frequency
PD burst frequency (Hz), missing steps as 0: acid ANOVA F(4,48) = 13.70, p = 1.59e-07 (n = 13); base ANOVA F(5,60) = 5.28, p = 0.000437 (n = 13)
criterion: acid p >= 0.05: False ; base p < 0.05: True ; 9.3: False ; 10.4: True
variant: missing steps left out: acid ANOVA F(4,40) = 14.57, p = 2e-07 (n = 11); base ANOVA F(5,55) = 6.20, p = 0.000126 (n = 12)
variant: the code's window (480 s from the first burst): acid ANOVA F(4,48) = 2.42, p = 0.0612 (n = 13); base ANOVA F(5,60) = 3.08, p = 0.0154 (n = 13)
variant: preparations still bursting at 5.5 only: acid ANOVA F(4,24) = 5.01, p = 0.00442 (n = 7); base ANOVA F(5,30) = 3.68, p = 0.0103 (n = 7)
== claim:fig3e-stg-spikes-per-burst
PD spikes per burst, missing steps as 0: acid ANOVA F(4,48) = 26.09, p = 1.59e-11 (n = 13); base ANOVA F(5,60) = 9.51, p = 1.02e-06 (n = 13)
criterion: True True True
variant: missing steps left out: acid ANOVA F(4,40) = 23.93, p = 3.69e-10 (n = 11); base ANOVA F(5,55) = 7.72, p = 1.48e-05 (n = 12)
[... 77 more lines not kept]
```

**Agent**

Executed outputs match the result text. Now the attempt record; checking the schema for findings and outcomes.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(s.get('required'))
for k in ['provenance','inputs','findings','outcomes','datasets','dataset']:
    if k in p: print(k, json.dumps(p[k])[:1500]); print()
print(json.dumps(s.get('$defs',s.get('definitions',{})))[:5000])
EOF
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.", "type": "string", "pattern": "^https://"}}}, "author_notes": {"description": "The notes from the paper's authors that this attempt used (papers/author-notes/<pape

inputs {"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}

findings {"description": "What the attempt
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
f=p['findings']['items']['properties']; print(list(f), json.dumps({k:f[k] for k in ['severity','notebook','output','versions','fixed_in'] if k in f})[:1500])
o=p['outcomes']['items']['properties']; print(list(o))
print(list(p))
EOF
cat papers/datasets/haley-2018.yaml
```

```
['kind', 'statement', 'found', 'about', 'severity', 'datasets', 'versions', 'fixed_in', 'notebook', 'output'] {"severity": {"description": "For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives a wrong result. `major`: a main analysis is blocked or changed, and the user would notice. `minor`: evident from the values or easy to work around, a wrong unit label included. `none`: no problem, a check that passed. Required from protocol pilot-18.", "enum": ["critical", "major", "minor", "none"]}, "notebook": {"description": "Path of the notebook within the entry whose code shows the finding.", "type": "string", "minLength": 1}, "output": {"description": "Which output of that notebook shows the finding: a cell tag, as for an outcome.", "type": "string", "minLength": 1}, "versions": {"description": "For a finding about the data: the versions of the dataset the finding was seen in, as the archive names them (0.240503.0152). Unset: the version the attempt read. Give it when the finding was seen in another version, such as the one the paper cites, and list the version the attempt read too if the finding is there as well. With several `datasets`, the versions are of the one dataset the finding names.", "type": "array", "minItems": 1, "uniqueItems": true, "items": {"type": "string", "minLength": 1}}, "fixed_in": {"description": "For a finding about the data: the first version of the dataset in which the attempt looked for the problem and it was gone. Unset: not 
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
# The datasets this paper is tested on (docs/paper-first.
[... 8 more lines not kept]
```

**Agent**

Writing the attempt record. First a small `finding-no-annotations` cell, so the major finding about undeposited annotations has code that shows it.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''# %% [finding-no-pdn]''','''# %% [finding-no-annotations]
from collections import Counter
print("file types in the project:", dict(Counter(p.rsplit(".", 1)[-1] for p in C.FILES)))
print("files other than .abf:", sorted({p.split("/")[-1] for p in C.FILES if not p.endswith(".abf")}))
print("No state annotation (stateData_STG.xlsx, stateData_CG.xlsx), Spike2 burst output (*_bursts.txt) or gastric annotation is in the project.")

# %% [finding-no-pdn]''')
open('nb_src.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python build_nb.py && date -u
```

```
96 cells
Thu Nov 26 02:06:09 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/attempt.py <<'PYEOF'
import yaml
NB = "reproduce_haley_2018.ipynb"
THR = "Spike thresholds are automatic (crabph.unit_threshold), where the authors set them by hand in Spike2 (spikenburst.s2s); assumed."
CGB = "CG bursts use a 1.0 s maximum interspike interval and one spike (crabph.BURST_RULES), as the LC fires one or two spikes about 0.5 s apart per Small Cell burst in several units and the paper's CG state 1 counts one LC spike per SC burst (Results, cardiac rhythm, paragraph 3); the code's starting values (0.3 s, two spikes) are shown as a variant; assumed."
PROXY = "The manual state annotation is not in the dataset. Rhythmic activity is a proxy from the pacemaker unit (PD, or LC) bursting with onsets at most 3 control periods apart, runs under 10 s merged (Methods paragraph 3); gap factors 2 and 5 are shown. For the STG it counts state 3 as rhythmic; assumed."
N_STG = "13 STG preparations of 15 (877_127 is not in the project; 877_101 has no pdn)."
N_CG = "14 CG units of 15 (887_017 is not in the project); units of one ganglion are counted as preparations, as the paper's code lists them."
MISS = "A missing pH step counts as 0 (pHCumulative.m sets empty bins to 0 and a missing condition has no bursts); leaving it out is shown as a variant."
PTXC = "The PTX folders have no README; the pH of each file is taken from its recorded bath pH (crabph.assign_ptx_conditions), and a preparation missing a step is left out of that protocol's tests (8 complete of 9); assumed."
INTRA = "The waveform parameters are the code's starting values (maxBurstFreq 2 and 10 Hz, minSpikeHeight 10 and 3 mV; intracellularAnalysis.m), which the authors adjusted by hand; assumed."
WIN = "The window is the last 8 min of each file (Methods, Data acquisition and analysis, paragraph 2); the code's window (480 s from the first burst, pHCumulative.m) is shown as a variant."

def o(claim, outcome, notes, deviations=None, assumed=True, blocked_by=None, measured=None, output=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if output and outcome != "blocked":
        d["notebook"] = NB; d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed and outcome != "blocked": d["assumed"] = True
    return d

outcomes = [
 o("fig2a-stg1-traces", "reproduced",
   "897_037 is rhythmic by the proxy over the whole of every step from 7.2 to 6.1 and 8.3 to 10.4, both recoveries, and also 5.5 (reading a), under gap factors 2, 3 and 5. At 10.4 PD spikes per burst are 12.43 against 13.10 at the control before base, and the PD slow-wave amplitude (VM1_2, last minute) 17.65 against 18.03 mV. Both decreases are small. The proxy cannot tell normal from weak triphasic, so the triphasic part rests on PD bursting.",
   [PROXY, THR, INTRA]),
 o("fig2bcd-stg1-measures", "reproduced",
   "In 897_037 frequency at 5.5 is 0.118 Hz above its control and at 10.4 0.266 Hz below (Spearman rho with pH -0.80 in acid, -1.00 in base). PD spikes per burst at 5.5 are 5.40 below control, and the duty cycle at 10.4 is 0.048 below control (rho -0.94). Both readings hold, and the frequency and spike parts hold in the code's window.",
   [THR, WIN]),
 o("fig3a-stg-variability-examples", "blocked",
   "The criterion needs STG states 1 and 2 apart at 10.4, and states 2 to 4 at 5.5. The manual annotation is not in the dataset (no xlsx or annotation file in the project), and the proxy, built on PD bursting alone, cannot tell normal, weak and intermittent triphasic apart. The two examples are not named in the paper or the code.",
   blocked_by="metadata_insufficient"),
 o("fig3c-stg-rhythmic-fraction", "partially_reproduced",
   "Both ANOVAs on the proxy fraction are significant (acid F(4,48) = 14.18, p = 1.0e-07; base F(5,60) = 2.88, p = 0.021). At 5.5 the fraction is 0.393 against 1.0 (corrected p = 0.0013). At 10.4 it is 0.771, not significant (p = 0.31; 0.22 to 0.61 across variants). The expected 15 preparations are 13 here. The proxy counts intermittent triphasic as rhythmic, which can only raise the fraction in base.",
   [PROXY, THR, N_STG, MISS], measured=13),
 o("stg-state-transitions", "blocked",
   "Counting transitions among the four STG states over whole recordings needs the manual annotation, which is not in the dataset; the proxy has two states.",
   blocked_by="metadata_insufficient"),
 o("fig3d-stg-frequency", "partially_reproduced",
   "Base ANOVA p = 4.4e-04, and frequency at 10.4 is lower (-0.407 Hz, corrected p = 0.047). At 9.3 the drop is not significant (-0.206 Hz, p = 0.65). The acid ANOVA is significant (F(4,48) = 13.70, p = 1.6e-07), driven by 5.5 (-0.837 Hz, p = 0.0011), so the claim of absence fails. In the code's window the acid ANOVA gives p = 0.061, as the paper reports, but no base t-test is significant (p 0.26 to 1). With missing steps left out, acid p = 2.0e-07 and 10.4 p = 0.092.",
   [THR, N_STG, MISS, WIN]),
 o("fig3e-stg-spikes-per-burst", "reproduced",
   "Acid ANOVA F(4,48) = 26.09, p = 1.6e-11; base F(5,60) = 9.51, p = 1.0e-06 (13 preparations). PD spikes per burst at 5.5 are 2.24 against 9.43 (corrected p = 3.2e-05). The same holds with missing steps left out and in the code's window.",
   [THR, N_STG, MISS, WIN]),
 o("fig3f-stg-duty-cycle", "partially_reproduced",
   "Both ANOVAs are significant (acid p = 2.3e-09, base p = 3.6e-10). The duty cycle at 6.1 is 0.023 below control, not above (corrected p = 0.93). In the code's window it is 0.041 above control at 6.1, not significant (p = 0.090).",
   [THR, N_STG, MISS, WIN]),
 o("fig3s2-stg-control-variability", "reproduced",
   "Reading (b) holds. Kruskal-Wallis of the 48 control bins on preparation gives H = 606, 545 and 491 for frequency, spikes per burst and duty cycle (13 preparations; p below double precision). Reading (a) holds for spikes per burst only: the preparation means span 0.48, 0.75 and 0.37 of the pooled range.",
   [THR, N_STG, "The criterion's readings (a) and (b) give different results; the claim holds under (b), as the criterion allows."]),
 o("fig4a-ptx-example", "reproduced",
   "903_052 meets every part. Its PD slow-wave amplitude at 6.7 is 0.41 of control, and at 5.5 PD is silent and depolarized by 16.4 mV. At 10.4 it fires 1.0 spikes per slow wave, and LP fires tonically at all six steps from 6.7 to 10.4 and is silent at 5.5. All 9 PTX preparations have a silent, depolarized PD at 5.5. The other parts hold in 2 to 7 of the 9.",
   [PTXC, INTRA, "One spike per PD burst is read as a ratio of PD spikes to slow-wave peaks above 0 and at most 1.5; LP firing without slow-wave bursts as an interspike-interval coefficient of variation below 1. These readings of the words are this attempt's; assumed."]),
 o("fig4bc-membrane-potential", "reproduced",
   "PD acid ANOVA F(4,28) = 31.00, p = 6.4e-10; LP base F(5,35) = 41.70, p = 8.9e-14 (8 complete preparations). PD is depolarized at 5.5 (+19.0 mV, corrected p = 7.9e-07) and 6.1 (+11.6 mV, p = 0.016). LP is hyperpolarized at 8.8 (-2.2 mV, p = 0.020), 9.3 (-9.5 mV), 9.8 (-12.1 mV) and 10.4 (-12.6 mV, p = 2.0e-04). The parts claimed relatively constant are not significant (LP acid ANOVA p = 0.65, PD base ANOVA p = 0.13). The code's slow-wave-trough measure gives the same outcome.",
   [PTXC, INTRA, "Minimum membrane potential is the minimum of the unfiltered Vm between successive slow-wave peaks (Methods, paragraph 5); the code's slow-wave troughs are a variant."]),
 o("fig4de-spike-amplitude", "partially_reproduced",
   "The acid ANOVAs are significant for PD (p = 1.5e-06) and LP (p = 0.0015). The PD base ANOVA is not significant (p = 0.26), as claimed. Amplitude at 5.5 is lower for PD (corrected p = 7.8e-04) and LP (p = 0.0044). The LP base ANOVA is not significant (p = 0.095), and LP at 6.1 (-3.4 mV) is not significant (p = 0.11). This matches the criterion's partial condition.",
   [PTXC, INTRA]),
 o("fig4fg-ptx-frequency", "partially_reproduced",
   "All four ANOVAs are significant (PD acid p = 7.0e-08, PD base 0.0016, LP acid 7.3e-09, LP base 7.3e-10). Six of the seven named t-tests hold, including PD at 5.5 (-1.26 Hz, p = 0.0034). LP at 8.3 is higher than control (+2.2 Hz, p = 0.098). The code's peak-to-peak PD frequency gives the same counts.",
   [PTXC, INTRA, "PD burst frequency from slow-wave trough-to-trough intervals (Methods, paragraph 5); the code's peak-to-peak (analyzeWaveform.m) is a variant."]),
 o("gastric-like-rhythm-counts", "blocked",
   "The paper identified gastric-like rhythms by eye and coded them as 8.x in its manual STG annotation (pHCumulative.m), which is not in the dataset. The criterion's fallback, rhythmic LG bursting alternating with DG bursting, has no period, burst or alternation thresholds in the paper or its code. The files name nerves (lgn, dgn), not units, so any detector would rest on thresholds of this attempt alone. The question is for the paper's authors (finding 11).",
   blocked_by="methods_underspecified"),
 o("gastric-conditions-co-occur", "blocked",
   "Depends on gastric-like-rhythm-counts, which is blocked.", blocked_by="methods_underspecified"),
 o("fig5-gastric-recovery-example", "blocked",
   "The example is not named. The criterion needs LG, GM, DG and MCN1 bursts identified on the lgn, dgn and ion, which the paper did by eye with no criterion, as for gastric-like-rhythm-counts.",
   blocked_by="methods_underspecified"),
 o("fig6-cg1-measures", "partially_reproduced",
   "In 877_149 CG2L the cardiac frequency is lower at 5.5 than control (-0.044 Hz) and higher at 10.4 (+0.040 Hz), the duty cycle is lower at 5.5 (-0.133), and the unit is rhythmic by the proxy over every step. LC spikes per burst fall in acid (-6.05 at 5.5; rho +0.80 with pH), and the duty cycle in base does not fall (+0.018 at 10.4; rho +0.20). Both parts fail under both readings, the 0.3 s burst rule and the code's window.",
   [THR, CGB, PROXY]),
 o("fig6a-cg2-less-rhythmic", "reproduced",
   "Of 8 other acid-first CG units, 887_093 CG2L meets the criterion under gap factors 2, 3 and 5. Its fraction is 0.38 at 5.5 and 0 at 9.8 and 10.4 against 1.0 at control, at least 0.63 at every step from 6.1 to 9.3, and 1.0 in the final recovery. The example is not named, so it cannot be said that this is the paper's CG #2.",
   [THR, CGB, PROXY]),
 o("fig7b-cg-rhythmic-fraction", "not_reproduced",
   "The base ANOVA is significant (p = 9.9e-10), and the fraction is lower at 9.3, 9.8 and 10.4 (0.55, 0.40, 0.33 against 0.99; corrected p 0.012 to 5.9e-04). The acid ANOVA is not (p = 0.058), and 5.5 (0.82) is not significant (p = 0.25), so neither the full nor the partial condition is met. With gap factor 2 the acid ANOVA gives p = 0.023, and 5.5 is still not significant (p = 0.12).",
   [THR, CGB, PROXY, N_CG, MISS]),
 o("cg-state-transitions", "blocked",
   "Counting transitions among CG states 1 to 3 needs the manual annotation, which is not in the dataset. The proxy follows the LC only and cannot tell SC-only bursting (state 2) from silence (state 3).",
   blocked_by="metadata_insufficient"),
 o("fig7c-cg-frequency", "not_reproduced",
   "The LC frequency at 10.4 is 0.092 Hz below control, not significant (corrected p = 0.84). The base ANOVA gives p = 0.056 and the acid ANOVA p = 0.037. No variant makes 10.4 significant (p 0.18 to 1). Frequency at 5.5 is 0.059 Hz below the acid control.",
   [THR, CGB, N_CG, MISS, WIN]),
 o("fig7d-cg-spikes-per-burst", "not_reproduced",
   "The base ANOVA is significant (p = 3.7e-05), and spikes per burst fall at 10.4 (-2.84, corrected p = 9.2e-04). The acid ANOVA is not (p = 0.54), and the increases at 5.5 (+1.27) and 6.1 (+0.61) and the fall at 9.8 (p = 0.26) are not significant. Under every variant the acid ANOVA fails (p 0.13 to 0.54), and one or two of the four t-tests hold.",
   [THR, CGB, N_CG, MISS, WIN]),
 o("fig7e-cg-duty-cycle", "reproduced",
   "Base ANOVA p = 4.8e-05, acid ANOVA p = 0.52 (14 units). Every variant gives the same outcome (base p 5.0e-04 to 0.0091; acid p 0.13 to 0.52). The acid effects are at most 0.014 in duty cycle.",
   [THR, CGB, N_CG, MISS, WIN]),
 o("fig7s2-cg-control-variability", "reproduced",
   "Reading (b) holds: Kruskal-Wallis H = 625, 516 and 468 for frequency, spikes per burst and duty cycle (14 units; p below double precision). Under reading (a) the preparation means span 0.39, 0.79 and 0.62 of the pooled range, so (a) fails for frequency.",
   [THR, CGB, N_CG]),
 o("fig8a-ganglion-difference", "not_reproduced",
   "With sum-to-zero contrasts all six ANOVA effects are significant under both univariate and multivariate tests: pH p = 5.9e-10 (acid) and 2.8e-12 (base), ganglion 0.034 and 0.015, interaction 5.7e-04 and 0.0040. With treatment contrasts the acid pH effect is not (p = 0.15). The STG is less rhythmic than the CG at 5.5 (0.39 against 0.82, corrected p = 0.042). It is more rhythmic at 9.3 (0.85 against 0.55) and 9.8 (0.77 against 0.40), not significantly (p = 0.36, 0.21). Both the full and the partial condition need all three t-tests. With gap factor 2, 9.8 is significant (p = 0.023) and 5.5 is not (p = 0.090).",
   [THR, CGB, PROXY, N_STG, N_CG, MISS]),
 o("fig8b-individual-preparations", "not_reproduced",
   "STG ceased firing at 5.5 in 6 of 11 preparations with a 5.5 file under readings (a) and (b), and 4 under (c). Counting the 2 without a 5.5 file as silent, as the code would, gives 8 of 13 against 14 of 15 (tolerance 1.4). 877_141, 887_141 and 897_037 burst throughout 5.5. CG units reduced at 5.5 are 5 of 14 under both readings (expected 6, tolerance 0.6). CG units fully rhythmic everywhere are 2 under both readings (expected 3, tolerance 0.3); gap factor 5 gives 3 under (a). All preparations are fully rhythmic at control.",
   [PROXY, THR, CGB, N_STG, N_CG, "Reading (a) of ceased firing, state 4 at the end of the step, is taken as no PD spikes in the last 10 s of the 5.5 file."],
   measured=[8, 5, 2]),
 o("fig8b-cross-predictive", "not_reproduced",
   "Reading (a) fails in both ganglia. Of the 4 STG preparations reduced at 10.4, 877_121 keeps a fraction of 0.59 at 5.5. In the CG, 1 of 5 units reduced at 5.5 is not reduced at 10.4. The Fisher tests give p = 1.0 in both ganglia.",
   [PROXY, THR, CGB]),
 o("baseline-frequency-correlations", "not_reproduced",
   "LC frequency at control correlates with LC frequency at 5.5 (Pearson r = 0.73, p = 0.0033, 14 units) and not at 10.4 (r = -0.16, p = 0.66), as claimed. The PD correlations are not strong under any reading. Extracellular PD gives r = 0.40 at 5.5 (p = 0.22, 11) and r = 0.48 at 10.4 (p = 0.12, 12). PTX PD gives r = -0.81 at 5.5 and 0.34 at 10.4.",
   [THR, CGB, "A preparation missing the step is left out of that correlation."]),
 o("robust-6-1-to-8-8", "reproduced",
   "No corrected t-test from 6.1 to 8.8 shows a significant decrease in either ganglion (smallest corrected p STG 0.53, CG 0.68), under gap factors 2, 3 and 5. The mean fractions there are 0.86 to 1.0 (STG) and 0.91 to 1.0 (CG).",
   [PROXY, THR, CGB, N_STG, N_CG]),
 o("intact-depolarize-in-acid", "reproduced",
   "In intact preparations, PD (7 with a 5.5 file, of 9) and LP (5 of 6) are depolarized at 5.5 against the acid control, by 18.2 and 11.7 mV. Every one of them is depolarized, and the acid ANOVAs give p = 2.9e-11 (PD) and 6.9e-05 (LP). Readings (a) and (b) both hold, and the code's slow-wave troughs give the same result.",
   [INTRA, "Intracellular PD and LP channels as the READMEs name them (Vm1_1 in a README is VM1 in files without VM1_1)."]),
]

findings = [
 dict(kind="data_missing", about="data", severity="major",
      statement="Two experiments that the paper's code analyses are not in the project. STG 877_127 is one of the 15 STG preparations (pHCumulative.m), and CG 887_017 (unit CG3L) one of the 15 CG units. The STG and CG analyses can use 14 of 15 each.",
      notebook=NB, output="finding-missing-experiments"),
 dict(kind="data_missing", about="data", severity="minor",
      statement="Seven experiments have no file for one pH step. 877_093 and 887_069 lack 5.5; 887_005, 887_011 and 887_149 lack 10.4 (their READMEs list 11 files). Among the PTX folders, 903_046 lacks 6.1 and 903_060 lacks 10.4. The paper's code handles a missing condition, so the steps may never have been recorded, but the READMEs do not say so.",
      notebook=NB, output="finding-missing-steps"),
 dict(kind="metadata_error", about="data", severity="minor",
      statement="Several READMEs disagree with their folders. 887_145's README lists its files under the names 887_149_0001.abf to 887_149_0014.abf. 877_149's lists 877_149_00010.abf for 877_149_0010.abf. 887_011_0001.abf and 887_049_0026.abf are in the folders but not in the READMEs. 887_061's README names an IN 15 channel that the files do not have (they have IN 14), and 877_149's IN 9 and 897_041's IN 10 are in only some files.",
      notebook=NB, output="finding-readme-mismatch"),
 dict(kind="metadata_insufficient", about="data", severity="major",
      statement="The nine PTX folders (903_046 to 903_064) have no README. Nothing names the pH of each file, the protocol order or the nerves beyond the channel names. Here the pH was inferred from the bath pH signal recorded in each file, which separates the steps cleanly.",
      notebook=NB, output="finding-ptx-order"),
 dict(kind="other", about="data", severity="minor",
      statement="In 903_058 and 903_060 the recorded bath pH shows the file after 8.3 at the 9.3 level and the next file at the 8.8 level (903_058_0014 and 0015, 903_060_0003 and 0004), so these solutions were applied out of their nominal order. An analysis that assumes the file order is the protocol order swaps these two steps.",
      notebook=NB, output="finding-ptx-order"),
 dict(kind="metadata_error", about="data", severity="major",
      statement="In 903_046_0002 the intracellular channels are named the other way round from the other ten files of the experiment. The input the others call PD3 is LP3 there, and LP4 is PD4. Its spikes coincide with the pdn spikes (0.62 of them within 5 ms) as in the other files, so the labels of 903_046_0002 are swapped. An analysis by channel name exchanges PD and LP in that control file.",
      notebook=NB, output="finding-ptx-label-swap"),
 dict(kind="metadata_insufficient", about="data", severity="minor",
      statement="877_101, one of the paper's 15 STG preparations, has no pdn, and its intracellular channel ME1_Vx is not named in the README. The PD unit can only be taken from the lvn, where it shares the nerve with LP and PY, so this attempt left it out of the PD measures.",
      notebook=NB, output="finding-no-pdn"),
 dict(kind="data_missing", about="data", severity="major",
      statement="The project holds only the raw .abf files and the READMEs. The manual state annotations (stateData_STG.xlsx, stateData_CG.xlsx), the Spike2 spike and burst output, and the gastric-rhythm annotation behind Figures 3, 5, 7 and 8 are not deposited. The state transition analyses and the gastric counts cannot be repeated, and every burst measure depends on thresholds that have to be set again.",
      notebook=NB, output="finding-no-annotations"),
 dict(kind="other", about="data", severity="minor",
      statement="The project links a GitHub storage add-on that the OSF API does not list for an anonymous reader (HTTP 403), and the registry's target list names OSF Storage only. The files read here are all in OSF Storage, and the live listing matches the pinned 408 files."),
 dict(kind="code_mismatch", about="paper",
      statement="pHCumulative.m compares a file length in seconds with sampleFreq*480 in samples, so its window is the 480 s after the first burst of each file, where the Methods say the last 8 min. With the code's window the acid ANOVA on PD frequency gives p = 0.061, matching the Results' relatively invariant frequency in acid. With the last 8 min it gives p = 1.6e-07. The paper's statistics may rest on the start of each step."),
 dict(kind="methods_unavailable", about="paper",
      statement="Questions for the authors. (1) The Spike2 thresholds and burst parameters per file, which the code sets by hand and does not record. This attempt set thresholds automatically and used a 1.0 s, one-spike burst rule for the LC. (2) How a missing pH step entered the statistics; the code gives it 0 (silent), and this attempt shows that and leaving it out. (3) Which PTX file is which pH, and whether 903_058 and 903_060 received 9.3 before 8.8. (4) Which file stands for a condition where a README lists two controls in a row (887_141, 897_005) or repeated acid steps (887_061). (5) Whether 877_101's PD was measured on the lvn. (6) The criteria for a gastric-like rhythm, identified by eye in the paper."),
 dict(kind="selection_undocumented", about="paper",
      statement="The paper reports 15 CG preparations, while its code lists 15 Large Cell units from 10 experiments (877_149, 887_149 and 897_041 contribute two or three units each). The statistics treat units of one ganglion as independent preparations, which the paper does not say."),
]

rec = {
 "schema_version": 3,
 "id": "haley-2018-01",
 "datasets": [{"archive": "osf", "id": "r7aes", "version": "2019-01-08T14:49:50", "doi": "10.17605/osf.io/r7aes", "relation": "primary"}],
 "paper": "doi:10.7554/elife.41877",
 "date": "2026-11-26",
 "entry": "haley-2018",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-19"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/encorescience/encore-registry/actions/runs/45733226000"}},
 "inputs": [{"what": "The lists of experiments and units the paper analyses (pHCumulative.m, pHCumulativePTX.m), the bin, window, discard and burst parameters, the waveform analysis and its starting parameters, and the statistics (statistics.R). Method details only; no data.",
             "source": "https://github.com/jesshaley/haley_hampton_marder_2018 at commit 83f5904"}],
 "outcomes": outcomes,
 "findings": findings,
}
out = yaml.safe_dump(rec, sort_keys=False, width=100, allow_unicode=True)
open('attempts/haley-2018-01.yaml', 'w').write(out)
import re
bad = [l for l in out.splitlines() if re.search(r':\s.*: ', l) and not l.strip().startswith(("-", "'", '"'))]
print(len(out.splitlines()), 'lines; lines with inner colon-space:', len(bad))
PYEOF
cd $TMPDIR && . dev/bin/activate && python attempt.py && grep -n "^- \|^  - " attempts/haley-2018-01.yaml | head -3; grep -c "'" attempts/haley-2018-01.yaml
```

```
610 lines; lines with inner colon-space: 1
4:- archive: osf
24:- what: The lists of experiments and units the paper analyses (pHCumulative.m, pHCumulativePTX.m), the
29:- claim: fig2a-stg1-traces
86
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/haley-2018-01.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,f'{path}[{i}]')
    elif isinstance(x,str) and ': ' in x:
        i=x.index(': '); print(path, '...', x[max(0,i-40):i+30])
walk(d)
EOF
```

```
.outcomes[8].notes ... ding (a) holds for spikes per burst only: the preparation means span 0
.outcomes[23].notes ... Reading (b) holds: Kruskal-Wallis H = 625, 516 
.outcomes[24].notes ... r both univariate and multivariate tests: pH p = 5.9e-10 (acid) and 2.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('attempt.py').read()
s=s.replace("Reading (a) holds for spikes per burst only: the preparation means span 0.48, 0.75 and 0.37 of the pooled range.","Reading (a) holds for spikes per burst only, as the preparation means span 0.48, 0.75 and 0.37 of the pooled range.")
s=s.replace("Reading (b) holds: Kruskal-Wallis H = 625, 516 and 468","Reading (b) holds, with Kruskal-Wallis H = 625, 516 and 468")
s=s.replace("under both univariate and multivariate tests: pH p = 5.9e-10 (acid) and 2.8e-12 (base), ganglion 0.034 and 0.015, interaction 5.7e-04 and 0.0040.","under both univariate and multivariate tests (pH p = 5.9e-10 acid and 2.8e-12 base, ganglion 0.034 and 0.015, interaction 5.7e-04 and 0.0040).")
open('attempt.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python attempt.py && cd  && python tools/entry.py check entries/haley-2018 2>&1 | tail -15
```

```
610 lines; lines with inner colon-space: 0
0 error(s)
```

**Agent**

Check passes with 0 errors. The notebook changed (two finding cells), so I'm re-running it clean.

**Agent calls Bash**

```bash
date -u; timeout 5400 python tools/entry.py all entries/haley-2018 2>&1 | tail -5; date -u
```

```
Thu Nov 26 02:07:43 UTC 2026
Installed kernelspec registry-haley-2018 in executed/haley-2018/.venv/share/jupyter/kernels/registry-haley-2018
0 error(s)
pass  reproduce_haley_2018.ipynb  (656 s)
Thu Nov 26 02:18:45 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/haley-2018/reproduce_haley_2018.ipynb'))
def out(c): return ''.join(''.join(o.get('text','')) if o['output_type']=='stream' else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    if any(o['output_type']=='error' for o in c.get('outputs',[])): print('ERROR', tags)
    if tags and tags[0] in ('finding-readme-mismatch','finding-no-annotations'): print(tags, out(c))
    if 'providers' in out(c) or 'notebook ran' in out(c): print(out(c)[:400])
    if tags and tags[0] in ('claim:fig3d-stg-frequency','claim:fig8b-individual-preparations'): print(out(c).splitlines()[0][:200])
EOF
python tools/entry.py handover entries/haley-2018 2>&1 | tail -5; ls executed/haley-2018/handover/
```

```
['finding-readme-mismatch'] 877_149 README names 1 files not in the folder, e.g. 877_149_00010.abf -> matched by number to 877_149/877_149_0010.abf
877_149 README electrodes in no file: [] ; in only some files: ['IN 9']
887_011 folder holds files the README does not list: ['887_011_0001.abf']
887_049 folder holds files the README does not list: ['887_049_0026.abf']
887_061 README electrodes in no file: ['IN 15'] ; in only some files: []
887_145 README names 12 files not in the folder, e.g. 887_149_0001.abf -> matched by number to 887_145/887_145_0001.abf
897_041 README electrodes in no file: [] ; in only some files: ['IN 10']

['finding-no-annotations'] file types in the project: {'abf': 385, 'txt': 23}
files other than .abf: ['README.txt']
No state annotation (stateData_STG.xlsx, stateData_CG.xlsx), Spike2 burst output (*_bursts.txt) or gastric annotation is in the project.

STG preparations: 13 (877_101 has no pdn; 877_127 is not in the project)
   prep  has_55  spikes_last10s  bursts_last_min  frac_rhythmic
notebook ran 10.9 min; peak memory 3.39 GB

wrote executed/haley-2018/handover
crabph.py
haley-2018.yaml
r7aes_files.py
[... 1 more lines not kept]
```

**Agent**

The handover is built. One check: the OSF listing cell's output didn't show in that filter.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/haley-2018/reproduce_haley_2018.ipynb'))
c=[c for c in nb['cells'] if c['cell_type']=='code' and 'osf_listing' in ''.join(c['source'])][0]
print(c['outputs'])
EOF
git status --short | head; date -u
```

```
[{'name': 'stdout', 'output_type': 'stream', 'text': ["OSF listing could not be read: TimeoutError('The read operation timed out') - the pin was not checked against OSF in this run\n"]}]
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
Thu Nov 26 02:19:05 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/haley-2018 && python3 - <<'EOF'
s=open('crabph.py').read()
old='''        for attempt in range(6):
            try:
                with urllib.request.urlopen(u, timeout=60) as r:
                    return json.load(r)
            except urllib.error.HTTPError as e:
                if e.code < 500 or attempt == 5:
                    raise
                time.sleep(5 * 2 ** attempt)'''
new='''        for attempt in range(6):
            try:
                with urllib.request.urlopen(u, timeout=120) as r:
                    return json.load(r)
            except urllib.error.HTTPError as e:
                if e.code < 500 or attempt == 5:
                    raise
            except (TimeoutError, urllib.error.URLError):
                if attempt == 5:
                    raise
            time.sleep(5 * 2 ** attempt)'''
assert old in s
s=s.replace(old,new); open('crabph.py','w').write(s)
EOF
cd ../.. && timeout 5400 python tools/entry.py all entries/haley-2018 2>&1 | tail -2; python3 - <<'EOF'
import json
nb=json.load(open('executed/haley-2018/reproduce_haley_2018.ipynb'))
c=[c for c in nb['cells'] if c['cell_type']=='code' and 'osf_listing' in ''.join(c['source'])][0]
print(c['outputs'])
print([o for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[]) if o['output_type']=='error'])
EOF
date -u
```

```
0 error(s)
pass  reproduce_haley_2018.ipynb  (989 s)
[{'name': 'stdout', 'output_type': 'stream', 'text': ["providers: {'osfstorage': 'listed', 'github': 'HTTP 403 Forbidden'}\n", 'osfstorage files now: 408; pinned: 408; changed or gone since pinned: 0; new: 0\n']}]
[]
Thu Nov 26 02:35:49 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/haley-2018/reproduce_haley_2018.ipynb'))
txt=''.join(''.join(o.get('text','')) for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[]) if o['output_type']=='stream')
for k in ['acid ANOVA F(4,48) = 13.70, p = 1.59e-07','F(4,52) = 2.45, p = 0.0578','STG ceased at 5.5, of 11 with a 5.5 file: {\'a\': 6','units meeting the criterion: [\'887_093 CG2L\']','PTX preparations meeting every part: 1','274 match of 274','reading (a) holds: True ; reading (b) holds: True','held: 6 of 7']:
    print(k in txt, k)
EOF
python tools/entry.py handover entries/haley-2018 2>&1 | tail -1; python tools/entry.py check entries/haley-2018 2>&1 | tail -1; git status --short entries attempts questions claims
```

```
True acid ANOVA F(4,48) = 13.70, p = 1.59e-07
True F(4,52) = 2.45, p = 0.0578
True STG ceased at 5.5, of 11 with a 5.5 file: {'a': 6
True units meeting the criterion: ['887_093 CG2L']
True PTX preparations meeting every part: 1
True 274 match of 274
True reading (a) holds: True ; reading (b) holds: True
True held: 6 of 7
wrote executed/haley-2018/handover
0 error(s)
?? attempts/haley-2018-01.yaml
?? entries/haley-2018/
```

**Agent calls Bash**

```bash
ls -la entries/haley-2018/; rm -rf entries/haley-2018/__pycache__; ls entries/haley-2018; date -u
```

```
total 352
drwxr-xr-x   4 runner runner   4096 Nov 26 01:55 .
drwxr-xr-x 359 runner runner  16384 Nov 26 01:20 ..
drwxr-xr-x   3 runner runner   4096 Nov 26 01:22 .claude
-rw-r--r--   1 runner runner   2279 Nov 26 01:55 README.md
drwxr-xr-x   2 runner runner   4096 Nov 26 02:19 __pycache__
-rw-r--r--   1 runner runner  47660 Nov 26 02:19 crabph.py
-rw-r--r--   1 runner runner    958 Nov 26 01:55 entry.yaml
-rw-r--r--   1 runner runner  51794 Nov 26 01:21 r7aes_files.py
-rw-r--r--   1 runner runner  85957 Nov 26 02:06 reproduce_haley_2018.ipynb
-rw-r--r--   1 runner runner     49 Nov 26 01:55 requirements.in
-rw-r--r--   1 runner runner 131055 Nov 26 01:55 requirements.lock.txt
README.md
crabph.py
entry.yaml
r7aes_files.py
reproduce_haley_2018.ipynb
requirements.in
requirements.lock.txt
Thu Nov 26 02:36:17 UTC 2026
```

**Agent calls Bash**

```bash
find entries/haley-2018/.claude -type f | head;
```

```
(Bash completed with no output)
```

**Agent**

I've completed steps 1 to 5 and the step-6 handover for haley-2018. Of 30 claims, 11 are reproduced, 6 partially reproduced, 7 not reproduced and 6 blocked. Every tested outcome is marked `assumed`, because the analysis depends on choices the paper left to hand work. Nothing is committed: the workflow will commit `entries/haley-2018/` and `attempts/haley-2018-01.yaml`.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2a-stg1-traces, fig2bcd-stg1-measures | reproduced (assumed) |
| fig3a-stg-variability-examples | blocked, metadata_insufficient |
| fig3c-stg-rhythmic-fraction | partially reproduced (assumed): 5.5 significant, 10.4 not (p = 0.31) |
| stg-state-transitions | blocked, metadata_insufficient |
| fig3d-stg-frequency | partially reproduced (assumed): the acid ANOVA is significant, where the paper says invariant |
| fig3e-stg-spikes-per-burst | reproduced (assumed) |
| fig3f-stg-duty-cycle | partially reproduced (assumed): no increase at 6.1 |
| fig3s2-stg-control-variability | reproduced (assumed), under reading (b) |
| fig4a-ptx-example, fig4bc-membrane-potential | reproduced (assumed) |
| fig4de-spike-amplitude, fig4fg-ptx-frequency | partially reproduced (assumed) |
| gastric-like-rhythm-counts, gastric-conditions-co-occur, fig5-gastric-recovery-example | blocked, methods_underspecified |
| fig6-cg1-measures | partially reproduced (assumed) |
| fig6a-cg2-less-rhythmic | reproduced (assumed) |
| fig7b-cg-rhythmic-fraction, fig7c-cg-frequency, fig7d-cg-spikes-per-burst | not reproduced (assumed) |
| cg-state-transitions | blocked, metadata_insufficient |
| fig7e-cg-duty-cycle, fig7s2-cg-control-variability | reproduced (assumed) |
| fig8a-ganglion-difference, fig8b-individual-preparations, fig8b-cross-predictive, baseline-frequency-correlations | not reproduced (assumed) |
| robust-6-1-to-8-8, intact-depolarize-in-acid | reproduced (assumed) |

## 2. Dataset, assumptions and questions

**What the dataset holds.** OSF Storage has 408 files: 385 raw .abf and 23 READMEs, all at their pinned versions. I checked the 274 STG and CG files I read whole against their SHA-256 and all match; the live listing shows no changes.

**Findings about the data:**
- Two experiments the paper's code uses are absent: 877_127 (STG) and 887_017 (CG) (major).
- Seven experiments lack one pH step (minor).
- The nine PTX folders have no README, so each file's pH had to be inferred from the recorded bath pH signal (major).
- In 903_058 and 903_060 that signal shows the 9.3 solution was applied before 8.8 (minor).
- In 903_046_0002 the PD and LP channel names are swapped relative to the other ten files of that experiment (major).
- Several READMEs disagree with their folders; for example, 887_145's README lists its files as 887_149_* (minor).
- 877_101 has no pdn channel, so its PD unit can't be isolated (minor).
- The state annotations, Spike2 burst output and gastric annotations behind the figures are not deposited (major).
- The project links a GitHub add-on that returns 403 to an anonymous reader (minor).

**Findings about the paper:**
- The code's 8-minute window is in fact the 480 s after the first burst of each file, not the last 8 minutes. With the code's window, the acid ANOVA on PD frequency gives p = 0.061 (as the paper reports); with the Methods' window it gives p = 1.6e-07.
- The paper's "15 CG preparations" are 15 units from 10 experiments.

**Assumptions:**
- Spike thresholds are set automatically (the authors set them by hand).
- CG bursts use a 1.0 s / 1-spike rule, with the code's 0.3 s / 2-spike values shown as a variant.
- Rhythmic states come from a proxy based on pacemaker bursting, shown with gap factors 2, 3 and 5.
- PTX pH comes from the recorded pH signal.
- The intracellular measures use the code's starting parameters.
- A missing pH step counts as 0, as the code does; leaving it out is shown as a variant.

**Questions for the paper's authors** (one `methods_unavailable` finding): the per-file thresholds; how missing steps entered the statistics; which PTX file is which pH; which file stands for a condition where there are duplicate controls or repeated steps; whether 877_101's PD came from the lvn; and the criteria for a gastric rhythm.

I asked a reader no questions.

## 3. Protocol gaps

1. "Check the sha256 of what you read" can't apply to partial reads. I read the STG and CG files whole (57 GB) and checked them; I read only the last minute of each PTX file and did not hash those.
2. The target list names OSF Storage as the only provider, but the API also lists a GitHub add-on that refuses anonymous access. I recorded it as a minor finding.
3. The OSF API returned 500 errors and timeouts. Since the listing only checks the pin and feeds no result, I added retries and made the cell print "not checked" on failure. One run did time out; I re-ran until the listing succeeded.
4. `assumed: true` ends up on every tested outcome, so it no longer separates outcomes. The deviations say which assumption each one rests on.
5. Where a criterion defines its own "partially" condition I applied it strictly (fig7b and fig8a are therefore not reproduced). Where it has none, I used the protocol's general definition.
6. `measured` is awkward when the expected value is a sample size (fig3c expects 15 preparations); I recorded 13.
7. The 903_046 label swap sits between critical and major in the severity table. I chose major, because the other ten files show the correct names.
8. Clean-run time varied from 10 to 16.5 minutes with network speed; `runtime_minutes` is left at 13.

## 4. Runtime and failures

The work ran from 01:05 to about 02:37 UTC, roughly 1.5 h. The final clean run (`tools/entry.py all`) passed with 0 errors in 989 s at 3.4 GB peak memory. The handover is in `executed/haley-2018/handover/`. One run's OSF listing timed out, as above; nothing else failed.

## End of run

93 turns, 83 minutes, $10.00 at API prices, result: success.
