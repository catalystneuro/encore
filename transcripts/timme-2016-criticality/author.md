# crcns-hc-8 · author · run 42570443240

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  wc -l docs/protocol.md README.md docs/design.md docs/archives.md; ls claims/crcns-hc-8 paper entries/001453-fouke-2025 claims/001453; git diff --stat
```

```
Mon Nov  9 06:04:39 UTC 2026
  625 docs/protocol.md
  139 README.md
  271 docs/design.md
  290 docs/archives.md
 1325 total
claims/001453:
10.1016-j.cub.2025.04.027.yaml

claims/crcns-hc-8:
10.3389-fphys.2016.00425.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

[... 8 more lines not kept]
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
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 606 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml"
}
```

```
1	# Claims for Timme, Marshall, Bennett, Ripp, Lautzenhiser & Beggs (2016), Front. Physiol. 7:425,
2	# "Criticality Maximizes Complexity in Neural Tissue", doi:10.3389/fphys.2016.00425, on CRCNS data
3	# set hc-8 (doi:10.6080/K0PC308P).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
5	# protocol as stated in docs/protocol.md.
6	#
7	# Text read: the version of record (PMC5037237, open access) as supplied under paper/ (Europe PMC
8	# JATS XML flattened): Methods 2.1 to 2.11, Results 3.1 to 3.3, Discussion, figure legends of
9	# Figures 1 to 12 and Table 1, and the supplement (Data_Sheet_1.PDF, supplementary Figures S1 to S9
10	# with their text). The supplied text drops the display equations; Equations 1 to 14 were read from
11	# the MathML of the PMC XML (eutils efetch, PMC5037237): Eq. 9 integration, Eq. 10
12	# C_N(X) = (1/N) sum over k = 2..N of [((k-1)/(N-1)) I(X_1^N) - <I(X_j^k)>_j], Eq. 11
13	# B_basic = <A(t+1)/A(t)>_t, Eq. 12 A(t+k) = r_k A(t), Eq. 13 r_k ~ B_new^k, Eq. 14
14	# chi = var(A(t)/N_neurons). No PDF of the main article is supplied, so values printed only inside
15	# the figures were not read: the mean and standard deviation of each exponent in Figure 8, the
16	# branching ratio histograms of Figure 9, the significance stars of Figures 10 and 11, the list of
17	# excluded recordings in Figure 2B, and the axes of Figures 7 and 12. Claims on those figures rest on
18	# the Results and the legends and carry no expected values from the figures.
19	#
20	# Code. The paper cites the NCC MATLAB toolbox (Marshall et al., 2016) and "Timme N. M. (2016).
[... 504 more lines not kept]
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
cd  cat paper/hc-8.data-description.txt; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=hc-8/" | python -c "import sys,re; t=sys.stdin.read(); [print(k,s) for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t)]; print(re.findall(r'<IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  B=https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-8/live; curl -s $B/checksums.md5; echo; curl -s $B/filelist.txt; echo; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
bd4e2a8685df3e55e1a3c04fbe09d9ce  Data.zip
af8f7972cac67d210489498508bf9259  docs/crcns_hc-8_data_description.docx
cab59e7c2cb7c58a89c8e9f2732ca509  docs/crcns_hc-8_data_description.pdf
87a1f10ccc353c140caf4e6d6c2b5f67  filelist.txt

# CRCNS.org 'hc-8' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 Data.zip	891317727 (850.0 MB)
 docs/crcns_hc-8_data_description.docx	31358 (30.6 KB)
 docs/crcns_hc-8_data_description.pdf	97558 (95.2 KB)
 checksums.md5	233

schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z]" attempts/001453-fouke-2025-01.yaml; sed -n '/^findings:/,/^verifications:/p' attempts/001453-fouke-2025-01.yaml | head -40; ls schemas; python tools/entry.py --help 2>&1 | head -20; head -60 entries/001453-fouke-2025/omr.py
```

```
1:schema_version: 2
2:id: 001453-fouke-2025-01
3:dataset:
8:paper: doi:10.1016/j.cub.2025.04.027
9:date: 2026-10-14
10:entry: 001453-fouke-2025
11:provenance:
22:inputs:
34:outcomes:
243:findings:
309:verifications:
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fphys.2016.00425.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fphys.2016.00425.txt",
 "offset": 224,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fphys.2016.00425.txt",
 "offset": 343,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '543,1004p' paper/10.3389-fphys.2016.00425.txt | awk 'length($0)>40'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; curl -sI -m 10 http://www.nicholastimme.com | head -3; python -c "import fsspec, scipy, numpy; print(fsspec.__version__, scipy.__version__, numpy.__version__)"; nproc; free -g | head -2
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 20 http://www.nicholastimme.com/software | grep -oiE 'href="[^"]*(zip|NCC|ncc)[^"]*"' | head; curl -s -m 20 http://www.nicholastimme.com | grep -oiE 'href="[^"]*"' | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s -m 20 http://www.nicholastimme.com/software.html | grep -oiE '(href|src)="[^"]*"' | grep -iv css | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && for h in ca54221c5919b874c5ffb0a03f682560 971efb8df3b4cee0918d28361ab5560e 98697c791c08ce110c0ebe10a6142deb; do curl -sL -m 60 -o $h.bin "https://nebula.wsimg.com/$h?AccessKeyId=AE70CEF69B3CE16C32E9&disposition=0&alloworigin=1"; echo $h $(sha256sum $h.bin | cut -c1-64) $(file -b $h.bin | cut -c1-40); done
```

Result: the fetched text is not kept.

**Agent**

Found the NCC toolbox zip matching the claims file's sha256. Reading its key functions to port them.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p ncc && cd ncc && unzip -oq ../98697c791c08ce110c0ebe10a6142deb.bin && find . -name "*.m" | head -60; wc -l $(find . -name "*.m") | tail -1
```

```
./NCCToolboxV1/cbmodel.m
./NCCToolboxV1/plplottool.m
./NCCToolboxV1/avshapecollapsestd.m
./NCCToolboxV1/pldist.m
./NCCToolboxV1/avpropvals.m
./NCCToolboxV1/plmle.m
./NCCToolboxV1/randomizeasdf2.m
./NCCToolboxV1/avgshapes.m
./NCCToolboxV1/brestimate.m
./NCCToolboxV1/bethelattice.m
./NCCToolboxV1/sizegivdurwls.m
./NCCToolboxV1/demoempdata.m
./NCCToolboxV1/complexityexamples.m
./NCCToolboxV1/asdf2toraster.m
./NCCToolboxV1/avshapecollapse.m
./NCCToolboxV1/rldecode.m
./NCCToolboxV1/demotruncdist.m
./NCCToolboxV1/avprops.m
./NCCToolboxV1/pvcalc.m
./NCCToolboxV1/rebin.m
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1 && strip(){ grep -v '^\s*%' "$1" | grep -v '^\s*$'; }; for f in plparams.m plmle.m pvcalc.m; do echo "=== $f"; strip $f; done
```

```
=== plparams.m
function [tau, xmin, xmax, sigmaTau, p, pCrit, ks] = plparams(x, varargin)
nSamples = 500;
pCrit = .2;
likelihood = 10^(-3);
iVarArg = 1;
while iVarArg <= length(varargin)
    argOkay = true;
    switch varargin{iVarArg},
        case 'samples',    nSamples = varargin{iVarArg+1}; iVarArg = iVarArg + 1;
        case 'threshold',  pCrit = varargin{iVarArg+1}; iVarArg = iVarArg + 1;
        case 'likelihood', likelihood = varargin{iVarArg+1}; iVarArg = iVarArg + 1;
        otherwise,
            argOkay = false;
    end
    if ~argOkay
        disp(['(PLPARAMS) Ignoring invalid argument #' num2str(iVarArg+1)]);
    end
    iVarArg = iVarArg + 1;
end
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1 && strip(){ grep -v '^\s*%' "$1" | grep -v '^\s*$'; }; for f in complexity.m; do echo "=== $f"; strip $f; done
```

```
=== complexity.m
function [Cn,IntInfPart] = complexity(X,nSubSets,varargin)
SubSampFlag = false;
iVarArg = 1;
while iVarArg <= length(varargin)
    argOkay = true;
    if ischar(varargin{iVarArg}),
        switch varargin{iVarArg},
            case 'subsampcorrect',	SubSampFlag = true;
            otherwise, 
                argOkay = false;
        end
    end
    if ~argOkay
        disp(['(COMPLEXITY) Ignoring invalid argument #' num2str(iVarArg+1)]);
    end
    iVarArg = iVarArg + 1;
end
nNeurons = size(X,1);
nT = size(X,2);
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1 && strip(){ grep -v '^\s*%' "$1" | grep -v '^\s*$' | grep -v "argOkay\|varargin\|iVarArg\|disp(\['(\|otherwise\|^\s*end$"; }; for f in demoempdata.m rebin.m avprops.m avgshapes.m avshapecollapse.m sizegivdurwls.m; do echo "=== $f"; strip $f; done
```

```
=== demoempdata.m
load sample_data
Av = avprops(asdf2, 'ratio', 'fingerprint');
minBR = min(Av.branchingRatio);
maxBR = max(Av.branchingRatio);
nEdges = 25;
edges = minBR:((maxBR-minBR)/(nEdges - 1)):maxBR;
BRhist = histc(Av.branchingRatio, edges);
plot(edges, BRhist);
title('Histogram of Avalanche Branching Ratios', 'fontsize', 14)
xlabel('Branching Ratio (s_{t+1} / s_t)', 'fontsize', 14)
ylabel('Frequency of Occurrence', 'fontsize', 14)
[tau, xminSZ, xmaxSZ, sigmaSZ, pSZ, pCritSZ, ksDR, DataSZ] =...
    avpropvals(Av.size, 'size', 'plot');
UniqSizes = unique(Av.size);
Occurances = hist(Av.size,UniqSizes);
AllowedSizes = UniqSizes(Occurances >= 20);
AllowedSizes(AllowedSizes < 4) = [];
LimSize = Av.size(ismember(Av.size,AllowedSizes));
[tau, xminSZ, xmaxSZ, sigmaSZ, pSZ, pCritSZ, DataSZ] =...
[... 253 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1 && strip(){ grep -v '^\s*%' "$1" | grep -v '^\s*$' | grep -v "argOkay\|varargin\|iVarArg\|disp(\['(\|otherwise\|^\s*end$"; }; for f in randomizeasdf2.m brestimate.m; do echo "=== $f"; strip $f; done; grep -n "plparams\|plmle\|case" avpropvals.m | head -20
```

```
=== randomizeasdf2.m
stdev = 10;
stdevOp = 'time';
        end
    end
    end
end
randasdf2 = asdf2;
if strcmp(method,'wrap')
    for iChannel = 1:asdf2.nchannels
        CutTime = randi(asdf2.nbins);
        randasdf2.raster{iChannel} = [asdf2.raster{iChannel}(asdf2.raster{iChannel} > CutTime) - CutTime,...
            asdf2.raster{iChannel}(asdf2.raster{iChannel} <= CutTime) + (asdf2.nbins - CutTime)];
    end
    randasdf2.randinfo = 'Wrapped Spike Trains';
elseif strcmp(method,'jitter')
    if strcmp(stdevOp,'time')
        stdevbinsize = stdev / asdf2.binsize;
    elseif strcmp(stdevOp,'bin')
        stdevbinsize = stdev;
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ncc/NCCToolboxV1 && strip(){ grep -v '^\s*%' "$1" | grep -v '^\s*$' | grep -v "argOkay\|varargin\|iVarArg\|disp(\['(\|otherwise\|^\s*end$"; }; for f in bethelattice.m cbmodel.m; do echo "=== $f"; strip $f; done; grep -n "complexity\|nSubSets\|chain\|0.8" complexityexamples.m democomplexity.m | head -30
```

```
=== bethelattice.m
function [asdf2,fullsizes,fulldurs,fullshapes] = bethelattice(pTrans, nTrials, StopLayer, StopLayerFinal)
MaxLayer = 1;
MaxNeuron = 1;
AllSpkRecord = cell([nTrials,1]);
Durs = zeros([nTrials,1]);
fullshapes = cell([nTrials,1]);
fullsizes = zeros([nTrials,1]);
fulldurs = zeros([nTrials,1]);
for iTrial = 1:nTrials
    iTrial
    iLayer = 1;
    ActiveListOld = 1;
    SpkRecord = [1,1];
    while (~isempty(ActiveListOld)) && (iLayer < StopLayer)
        iLayer = iLayer + 1;
        Hits = (rand([2*length(ActiveListOld),1]) < pTrans);
        HitList = find(Hits);
        EOList = mod(HitList,2);
        EOList(EOList == 0) = 2;
[... 221 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && uv venv -q dev && source dev/bin/activate && uv pip install -q numpy scipy fsspec aiohttp requests matplotlib pandas ipykernel nbformat nbclient 2>&1 | tail -2; python -c "import fsspec,aiohttp;print('ok')"
```

```
Mon Nov  9 06:07:48 UTC 2026
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && time python -c "
import fsspec, zipfile, io, scipy.io as sio, numpy as np
url='https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-8/live/Data.zip'
f=fsspec.open(url, block_size=2**20).open()
z=zipfile.ZipFile(f)
inf=z.infolist()
print(len(inf)); 
for i in inf[:5]+inf[-3:]: print(i.filename, i.file_size, i.compress_size)
names=[i.filename for i in inf if i.filename.endswith('.mat')]
print(len(names))
m=sio.loadmat(io.BytesIO(z.read(names[0])), squeeze_me=True, struct_as_record=False)
print(m.keys())
d=m['data']; print(d._fieldnames)
for k in d._fieldnames:
  v=getattr(d,k); print(k, type(v), getattr(v,'shape',None), v if np.ndim(v)==0 or isinstance(v,str) else '')
print(d.spikes[0][:10], d.spikes[0].dtype)
print(d.wave_ClusParams._fieldnames if hasattr(d.wave_ClusParams,'_fieldnames') else d.wave_ClusParams)
"
```

```
436
Data/ 0 0
Data/Culture10DIV10.mat 3342905 3343318
Data/Culture10DIV13.mat 2215841 2216031
Data/Culture10DIV18.mat 2103611 2103862
Data/Culture10DIV19.mat 2437648 2437935
Data/Culture9DIV34.mat 1309441 1309583
Data/Culture9DIV7.mat 2272897 2273222
Data/Culture9DIV9.mat 1864795 1865047
435
dict_keys(['__header__', '__version__', '__globals__', 'data'])
['spikes', 'nNeurons', 'binsize', 'nbins', 'recordingID', 'datatype', 'expsys', 'channel', 'wave_ClusParams']
spikes <class 'numpy.ndarray'> (96,) 
nNeurons <class 'int'> None 96
binsize <class 'float'> None 0.05
nbins <class 'int'> None 73999936
recordingID <class 'str'> None DisCultSet13DIV10Array22
datatype <class 'str'> None Spikes
expsys <class 'str'> None Rat Hippocampal Dissociated Cultures
channel <class 'numpy.ndarray'> (96,) 
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/crcns-hc-8-timme-2016
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-hc-8-timme-2016/hc8.py",
 "content": "\"\"\"Loading and measures for CRCNS hc-8, the culture recordings of Timme et al. (2016).\n\nTimme, Marshall, Bennett, Ripp, Lautzenhiser & Beggs (2016), \"Criticality Maximizes Complexity in\nNeural Tissue\", Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425. Data set doi:10.6080/K0PC308P.\n\nThe data set is one zip, hc-8/live/Data.zip, of 435 MATLAB files CultureXDIVY.mat, each with a\nstruct `data` whose `spikes` is a cell array of spike times per neuron in 0.05 ms bins. The zip is\nread in place from the public S3 bucket over range requests; nothing is written to disk.\n\nThe measures port the NCC MATLAB toolbox that the paper cites (Marshall et al., 2016; \"NCC Toolbox\nVersion 1\", June 14th, 2016, from the Software page of nicholastimme.com, zip sha256\nb7c912f8154f70fc82b13ab1725ed191935ed2877256cadd7e39f66737be294b, the version the claims file\nread). Each function names the toolbox function it ports. Where the parameters come from:\n\n- First 59 min of each recording, rebinning to the mean network-wide ISI, avalanches as runs of\n  active bins: Methods 2.2 and 2.3 (claims file, common method). The ISI is rounded to a whole\n  number of 0.05 ms bins, as `rebin.m` requires (claims file, common detail 1, a standard choice).\n- Cuts before power-law fits (values >= 4 seen at least 20 times), MLE on tau in [1, 5] to 0.001,\n  500 surrogates and p >= 0.2, the support search largest range first: Methods 2.7, `plparams.m`,\n  `plmle.m`, `pvcalc.m`.\n- Size given duration by weighted least squares over the fitted duration range, weights the number\n  of avalanches per duration: Methods 2.7, `sizegivdurwls.m`.\n- Shape collapse of mean profiles of durations >= 4 seen >= 20 times, exponent in [0, 4] refined\n  to 0.001, 1000 interpolation points, curvature 2 x the quadratic coefficient: Methods 2.8,\n  `avgshapes.m`, `avshapecollapse.m`. The claims file takes the absolute value (common detail 6).\n- Complexity with the sub-sampling correction (randomized data subtracted, cut at the first peak):\n  Methods 2.9, `complexity.m`. The number of random subsets per subset size is a parameter;\n  Methods 2.9 give 100.\n- Randomizations jitter (SD in rebinned bins), wrap, Poisson, swap and shuffling: Methods 2.5,\n  `randomizeasdf2.m` (shuffling is its `swap2`, which is what Methods 2.5 describe).\n- Branching ratio B_new with delays 1 to 8 and 0 <= A(t) <= 10: Methods 2.11, `brestimate.m`.\n- Susceptibility: Eq. 14 and the claims file's common detail 5.\n- Sub-sampling: 30 random sub-samples from 40% to 100% of the neurons, weighted least squares on\n  1/N with weight N, the intercept kept: Methods 2.10.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nimport zipfile\nfrom functools import lru_cache\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\nfrom scipy import optimize, signal, sparse\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-8/live\"\nZIP_URL = f\"{BUCKET}/Data.zip\"\nZIP_MD5 = \"bd4e2a8685df3e55e1a3c04fbe09d9ce\"  # hc-8/live/checksums.md5\nBIN_MS = 0.05            # data description: spike times in 0.05 ms bins\nANALYSIS_MIN = 59.0      # Methods 2.2: first 59 min of each recording\nANALYSIS_BINS = int(round(ANALYSIS_MIN * 60e3 / BIN_MS))\n\nMIN_VALUE = 4            # Methods 2.7: sizes or durations less than 4 removed\nMIN_COUNT = 20           # Methods 2.7: values seen fewer than 20 times removed\nN_SURROGATES = 500       # Methods 2.7\nP_CRIT = 0.2             # Methods 2.7\nBR_DELAYS = np.arange(1, 9)      # Methods 2.11: 1 <= k <= 8\nBR_ACT_MAX_CULTURE = 10          # Methods 2.11: 0 <= A(t) <= 10 for the culture data\nBR_ACT_MAX_MODEL = 5             # Methods 2.11: 0 <= A(t) <= 5 for the cortical branching model\n\n\n# ----------------------------------------------------------------------------------------------\n# Loading\n\n@lru_cache(maxsize=1)\ndef _zip():\n    f = fsspec.open(ZIP_URL, block_size=2**20).open()\n    return zipfile.ZipFile(f)\n\n\ndef recording_names() -> list[str]:\n    \"\"\"Members CultureXDIVY.mat of Data.zip, sorted by culture then DIV.\"\"\"\n    names = [i.filename for i in _zip().infolist() if i.filename.endswith(\".mat\")]\n    return sorted(names, key=lambda n: culture_div(n))\n\n\ndef culture_div(name: str) -> tuple[int, int]:\n    m = re.search(r\"Culture(\\d+)DIV(\\d+)\\.mat$\", name)\n    return int(m.group(1)), int(m.group(2))\n\n\ndef load(name: str, zf: zipfile.ZipFile | None = None) -> dict:\n    \"\"\"One recording: spike times per neuron (0.05 ms bins, int64) and the struct's metadata.\"\"\"\n    zf = zf or _zip()\n    m = sio.loadmat(io.BytesIO(zf.read(name)), squeeze_me=True, struct_as_record=False)\n    d = m[\"data\"]\n    spikes = [np.atleast_1d(np.asarray(s, dtype=np.int64)) for s in np.atleast_1d(d.spikes)]\n    return dict(name=name, spikes=spikes, nNeurons=int(d.nNeurons), binsize=float(d.binsize),\n                nbins=int(d.nbins), recordingID=str(d.recordingID), datatype=str(d.datatype),\n                expsys=str(d.expsys), channel=np.atleast_1d(d.channel),\n                wave_clus=d.wave_ClusParams)\n\n\ndef open_zip() -> zipfile.ZipFile:\n    \"\"\"A fresh handle on the zip, for use in another thread or process.\"\"\"\n    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())\n\n\n# ----------------------------------------------------------------------------------------------\n# Rebinning and avalanches\n\ndef first_window(spikes: list[np.ndarray], nbins: int = ANALYSIS_BINS) -> list[np.ndarray]:\n    \"\"\"Spikes in the first 59 min (bins 1..nbins in the 1-based convention of the files).\"\"\"\n    return [s[(s >= 1) & (s <= nbins)] for s in spikes]\n\n\ndef network_isi_bins(spikes: list[np.ndarray]) -> float:\n    \"\"\"Mean interval between consecutive spikes of all neurons pooled, in 0.05 ms bins (Methods 2.3).\n\n    Spikes of different neurons in the same 0.05 ms bin give intervals of 0, which are kept.\"\"\"\n    t = np.sort(np.concatenate(spikes))\n    return float(np.mean(np.diff(t))) if t.size > 1 else np.nan\n\n\ndef rebin(spikes: list[np.ndarray], factor: int, nbins: int = ANALYSIS_BINS):\n    \"\"\"`rebin.m`: new time ceil(t / factor), duplicates within a neuron merged.\"\"\"\n    new = [np.unique(np.ceil(s / factor).astype(np.int64)) for s in spikes]\n    return new, int(np.ceil(nbins / factor))\n\n\ndef activity(raster: list[np.ndarray], nbins: int) -> np.ndarray:\n    \"\"\"A(t), the number of active neurons per bin, for bins 1..nbins (index 0 is bin 1).\"\"\"\n    a = np.zeros(nbins + 1, dtype=np.int32)\n    for s in raster:\n        np.add.at(a, s, 1)\n    return a[1:]\n\n\ndef avalanches(act: np.ndarray):\n    \"\"\"`avprops.m` on the activity series: runs of consecutive active bins.\n\n    Returns sizes, durations, start indices (0-based bin index) of each avalanche.\"\"\"\n    on = act > 0\n    d = np.diff(np.concatenate([[0], on.astype(np.int8), [0]]))\n    starts = np.flatnonzero(d == 1)\n    ends = np.flatnonzero(d == -1)\n    dur = ends - starts\n    cs = np.concatenate([[0], np.cumsum(act, dtype=np.int64)])\n    size = cs[ends] - cs[starts]\n    return size, dur, starts\n\n\n# ----------------------------------------------------------------------------------------------\n# Power-law fitting (plmle.m, pvcalc.m, plparams.m)\n\ndef apply_cuts(x: np.ndarray) -> np.ndarray:\n    \"\"\"demoempdata.m: keep values >= 4 that occur at least 20 times (Methods 2.7).\"\"\"\n    u, c = np.unique(x, return_counts=True)\n    keep = u[(c >= MIN_COUNT) & (u >= MIN_VALUE)]\n    return x[np.isin(x, keep)]\n\n\nclass _PLData:\n    \"\"\"Histogram of integer data with prefix sums of x^-tau on the 0.001 tau grid of plmle.m.\"\"\"\n\n    TAUS = np.round(np.arange(1000, 5001) / 1000.0, 3)\n\n    def __init__(self, x: np.ndarray):\n        x = np.asarray(x, dtype=np.int64)\n        self.x = x\n        self.xmax_all = int(x.max())\n        self.counts = np.bincount(x, minlength=self.xmax_all + 1).astype(np.float64)\n        self.cum_n = np.concatenate([[0], np.cumsum(self.counts)])          # cum_n[v+1] = #x <= v\n        logv = np.log(np.maximum(np.arange(self.xmax_all + 1), 1))\n        self.cum_log = np.concatenate([[0], np.cumsum(self.counts * logv)])\n        self.logv = logv\n        self._W = None\n\n    def W(self):\n        if self._W is None:\n            v = np.arange(1, self.xmax_all + 1, dtype=np.float64)\n            # cumulative sums over v of v^-tau, rows tau; column j is sum over 1..j\n            w = np.exp(-np.outer(self.TAUS, np.log(v)))\n            self._W = np.concatenate([np.zeros((len(self.TAUS), 1)), np.cumsum(w, axis=1)], axis=1)\n        return self._W\n\n    def mle(self, xmin: np.ndarray, xmax: np.ndarray) -> np.ndarray:\n        \"\"\"plmle.m for integer data, vectorized over candidate supports: coarse-to-fine to 0.001.\"\"\"\n        xmin = np.atleast_1d(xmin).astype(np.int64)\n        xmax = np.atleast_1d(xmax).astype(np.int64)\n        W = self.W()\n        n = self.cum_n[xmax + 1] - self.cum_n[xmin]\n        slog = self.cum_log[xmax + 1] - self.cum_log[xmin]\n        mlog = slog / n\n\n        def L(idx):  # idx: (ncand, m) tau indices\n            Z = W[idx, xmax[:, None]] - W[idx, xmin[:, None] - 1]\n            return -np.log(Z) - self.TAUS[idx] * mlog[:, None]\n\n        lo = np.zeros(len(xmin), dtype=np.int64)\n        hi = np.full(len(xmin), 4000, dtype=np.int64)\n        best = None\n        for step in (100, 10, 1):\n            m = (hi - lo) // step + 1\n            mmax = int(m.max())\n            idx = lo[:, None] + step * np.arange(mmax)[None, :]\n            valid = np.arange(mmax)[None, :] < m[:, None]\n            idx = np.where(valid, idx, lo[:, None])\n            Lv = np.where(valid, L(idx), -np.inf)\n            j = np.argmax(Lv, axis=1)\n            best = idx[np.arange(len(j)), j]\n            # the next level spans the neighbours of the best value (plmle.m edge rules)\n            jl = np.where(j == 0, 0, j - 1)\n            jh = np.where(j == m - 1, m - 1, j + 1)\n            lo = lo + step * jl\n            hi = lo + step * (jh - jl)\n        return self.TAUS[best]\n\n    def cdf_pair(self, xmin: int, xmax: int, tau: float):\n        v = np.arange(xmin, xmax + 1)\n        pdf_x = self.counts[xmin:xmax + 1]\n        n = pdf_x.sum()\n        pdf_fit = v.astype(float) ** (-tau)\n        pdf_fit /= pdf_fit.sum()\n        return pdf_x, int(n), pdf_fit\n\n    def ks(self, xmin: int, xmax: int, tau: float) -> float:\n        pdf_x, n, pdf_fit = self.cdf_pair(xmin, xmax, tau)\n        return float(np.max(np.abs(np.cumsum(pdf_x / n) - np.cumsum(pdf_fit))))\n\n\ndef pvcalc(pl: _PLData, xmin: int, xmax: int, tau: float, rng: np.random.Generator,\n           n_samples: int = N_SURROGATES):\n    \"\"\"pvcalc.m for integer data: surrogates drawn from the fitted truncated power law with the\n    data's number of events, KS of each against the fit; p is the fraction at least as large as\n    the data's KS. All surrogates are drawn (pvcalc.m stops early only when the decision is\n    already certain, which does not change whether p >= 0.2).\"\"\"\n    pdf_x, n, pdf_fit = pl.cdf_pair(xmin, xmax, tau)\n    emp = np.max(np.abs(np.cumsum(pdf_x / n) - np.cumsum(pdf_fit)))\n    samp = rng.multinomial(n, pdf_fit, size=n_samples)\n    ks = np.max(np.abs(np.cumsum(samp, axis=1) / n - np.cumsum(pdf_fit)[None, :]), axis=1)\n    return float(np.mean(emp <= ks)), float(emp)\n\n\ndef support_order(x: np.ndarray) -> np.ndarray:\n    \"\"\"plparams.m: all pairs of unique values, without the pair of each value with the next one,\n    ranked by (log(xmax/xmin) / log(max ratio))^2, largest first (stable order for ties).\"\"\"\n    u = np.unique(x)\n    i, j = np.triu_indices(len(u), k=2)       # drops adjacent pairs (k = 1) and identical values\n    pairs = np.column_stack([u[i], u[j]])\n    r = np.log(pairs[:, 1] / pairs[:, 0])\n    r = r / r.max()\n    order = np.argsort(-(r ** 2), kind=\"stable\")\n    return pairs[order]\n\n\ndef plparams(x: np.ndarray, rng: np.random.Generator, screen: float = 1.2, chunk: int = 2000):\n    \"\"\"plparams.m: the largest support (in the ranking above) whose truncated power-law fit gives\n    p >= 0.2.\n\n    Screening, to keep the search fast: a support whose data KS exceeds screen / sqrt(n) is\n    rejected without surrogates. For sqrt(n) KS above 1.2 the asymptotic Kolmogorov probability\n    is 0.11 < 0.2, and the KS of discrete surrogates against a fixed distribution is smaller\n    still, so these supports would be rejected by pvcalc as well (a numerical shortcut, not a\n    change of method).\n\n    Returns dict with tau, xmin, xmax, p, n_tried (supports evaluated), n (events in range).\"\"\"\n    x = np.asarray(x, dtype=np.int64)\n    out = dict(tau=np.nan, xmin=np.nan, xmax=np.nan, p=np.nan, ks=np.nan, n=0, n_tried=0)\n    if np.unique(x).size < 3:\n        return out\n    pl = _PLData(x)\n    pairs = support_order(x)\n    tried = 0\n    for c0 in range(0, len(pairs), chunk):\n        pc = pairs[c0:c0 + chunk]\n        taus = pl.mle(pc[:, 0], pc[:, 1])\n        for (xmin, xmax), tau in zip(pc, taus):\n            tried += 1\n            pdf_x, n, pdf_fit = pl.cdf_pair(int(xmin), int(xmax), float(tau))\n            emp = np.max(np.abs(np.cumsum(pdf_x / n) - np.cumsum(pdf_fit)))\n            if emp * np.sqrt(n) > screen:\n                continue\n            p, _ = pvcalc(pl, int(xmin), int(xmax), float(tau), rng)\n            if p >= P_CRIT:\n                return dict(tau=float(tau), xmin=int(xmin), xmax=int(xmax), p=p, ks=float(emp),\n                            n=int(n), n_tried=tried)\n    out[\"n_tried\"] = tried\n    return out\n\n\ndef plmle_full(x: np.ndarray) -> float:\n    \"\"\"plmle.m over all of x (no range search), as Methods 2.10 use for sub-samples.\"\"\"\n    x = np.asarray(x, dtype=np.int64)\n    if np.unique(x).size < 2:\n        return np.nan\n    pl = _PLData(x)\n    return float(pl.mle(np.array([x.min()]), np.array([x.max()]))[0])\n\n\ndef sizegivdur(size: np.ndarray, dur: np.ndarray, durmin, durmax) -> float:\n    \"\"\"sizegivdurwls.m: slope of log10 mean size on log10 duration, weighted by the number of\n    avalanches per duration, over the unique durations from durmin to durmax.\"\"\"\n    if not np.isfinite(durmin) or not np.isfinite(durmax):\n        return np.nan\n    u, inv, c = np.unique(dur, return_inverse=True, return_counts=True)\n    ms = np.bincount(inv, weights=size) / c\n    sel = (u >= durmin) & (u <= durmax)\n    if sel.sum() < 2:\n        return np.nan\n    X = np.column_stack([np.log10(u[sel]), np.ones(sel.sum())])\n    y = np.log10(ms[sel])\n    w = np.sqrt(c[sel].astype(float))\n    beta, *_ = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)\n    return float(beta[0])\n\n\n# ----------------------------------------------------------------------------------------------\n# Shape collapse (avgshapes.m, avshapecollapse.m)\n\ndef mean_profiles(act: np.ndarray, size, dur, starts, min_dur: int = 4, min_count: int = 20):\n    \"\"\"avgshapes.m with 'cutoffs', 4, 20: the mean profile of each duration >= 4 seen >= 20 times.\"\"\"\n    u, c = np.unique(dur, return_counts=True)\n    keep = u[(u >= min_dur) & (c >= min_count)]\n    prof = []\n    for T in keep:\n        st = starts[dur == T]\n        idx = st[:, None] + np.arange(T)[None, :]\n        prof.append(act[idx].mean(axis=0))\n    return prof\n\n\ndef shape_collapse(profiles: list[np.ndarray], n_interp: int = 1000):\n    \"\"\"avshapecollapse.m: the exponent 1/sigma nu z in [0, 4] (refined to 0.001) minimizing the\n    mean over scaled time of the variance across scaled profiles over the squared range, and the\n    curvature, 2 x the leading coefficient of a quadratic fit of the mean collapsed profile.\"\"\"\n    if len(profiles) < 2:\n        return np.nan, np.nan\n    T = np.array([len(p) for p in profiles], dtype=float)\n    grid = np.linspace(0, 1, n_interp)\n    interp = np.array([np.interp(grid, np.linspace(0, 1, len(p)), p) for p in profiles])\n    logT = np.log(T)\n\n    def errors(xs):\n        scale = np.exp(np.outer(1 - xs, logT))            # (nx, nprof)\n        S = scale[:, :, None] * interp[None, :, :]        # (nx, nprof, ninterp)\n        var = S.var(axis=1, ddof=1).mean(axis=1)\n        rng_ = S.max(axis=(1, 2)) - S.min(axis=(1, 2))\n        return var / rng_ ** 2\n\n    lo, hi = 0.0, 4.0\n    best = None\n    for it in range(1, 4):\n        xs = np.round(np.arange(lo, hi + 1e-9, 10.0 ** (-it)), 6)\n        e = errors(xs)\n        best = xs[int(np.argmin(e))]\n        lo, hi = best - 10.0 ** (1 - it), best + 10.0 ** (1 - it)\n    S = np.exp((1 - best) * logT)[:, None] * interp\n    coeffs = np.polyfit(grid, S.mean(axis=0), 2)\n    return float(best), float(2 * coeffs[0])\n\n\n# ----------------------------------------------------------------------------------------------\n# Complexity (complexity.m)\n\ndef _states(raster_bins: list[np.ndarray], bins: np.ndarray):\n    \"\"\"Unique network states over the given bins: a sparse (n_unique x n_neurons) matrix and the\n    count of each state.\"\"\"\n    n = len(raster_bins)\n    pos = {}\n    index = np.full(bins.max() + 2 if bins.size else 1, -1, dtype=np.int64)\n    index[bins] = np.arange(bins.size)\n    rows, cols = [], []\n    for j, s in enumerate(raster_bins):\n        r = index[s[s < index.size]]\n        r = r[r >= 0]\n        rows.append(r)\n        cols.append(np.full(r.size, j))\n    rows = np.concatenate(rows) if rows else np.array([], dtype=np.int64)\n    cols = np.concatenate(cols) if cols else np.array([], dtype=np.int64)\n    X = sparse.csr_matrix((np.ones(rows.size, dtype=np.int64), (rows, cols)), shape=(bins.size, n))\n    return X\n\n\ndef _unique_rows(X: sparse.csr_matrix, rng: np.random.Generator):\n    \"\"\"Unique rows of a 0/1 sparse matrix with their counts (hash on random 62-bit weights).\"\"\"\n    w = rng.integers(1, 2**62, size=X.shape[1], dtype=np.int64)\n    h = X @ w\n    _, first, cnt = np.unique(h, return_index=True, return_counts=True)\n    return X[first], cnt\n\n\ndef _integration_curve(U: sparse.csr_matrix, cnt: np.ndarray, nT: int, n_subsets: int,\n                       rng: np.random.Generator) -> np.ndarray:\n    \"\"\"Mean integration of random k-subsets for k = 1..N (k = 1 is 0), as complexity.m.\"\"\"\n    N = U.shape[1]\n    nsp = np.asarray(U.multiply(cnt[:, None]).sum(axis=0)).ravel().astype(float)\n    p1 = nsp / nT\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        ent = -(p1 * np.log2(p1)) - ((1 - p1) * np.log2(1 - p1))\n    ent = np.nan_to_num(ent)\n    curve = np.zeros(N)\n    w_all = rng.integers(1, 2**62, size=N, dtype=np.int64)\n    Ud = U.tocsc()\n    from math import comb\n    for k in range(2, N + 1):\n        if comb(N, k) <= n_subsets:\n            from itertools import combinations\n            subsets = [np.array(c) for c in combinations(range(N), k)]\n        else:\n            subsets = [rng.permutation(N)[:k] for _ in range(n_subsets)]\n        vals = np.empty(len(subsets))\n        for i, sub in enumerate(subsets):\n            w = np.zeros(N, dtype=np.int64)\n            w[sub] = w_all[sub]\n            h = Ud @ w\n            _, inv = np.unique(h, return_inverse=True)\n            p = np.bincount(inv, weights=cnt) / nT\n            vals[i] = ent[sub].sum() + np.sum(p * np.log2(p))\n        curve[k - 1] = vals.mean()\n    return curve\n\n\ndef complexity(X: sparse.csr_matrix, n_subsets: int, rng: np.random.Generator,\n               subsamp_correct: bool = True):\n    \"\"\"complexity.m on a (time bins x neurons) 0/1 matrix.\n\n    With the correction, the integration curve of the data with each neuron's bins permuted\n    independently is subtracted, and the curve is cut after the first peak of I(k)/(k-1)\n    (findpeaks with a minimum peak distance of max(3, round(0.1 N))). Returns (Cn, curve).\"\"\"\n    nT, N = X.shape\n    U, cnt = _unique_rows(X, rng)\n    curve = _integration_curve(U, cnt, nT, n_subsets, rng)\n    Cn = np.sum(np.linspace(0, curve[-1], N) - curve) / N\n    if not subsamp_correct:\n        return float(Cn), curve\n    Xc = X.tocsc()\n    rows, cols = [], []\n    for j in range(N):\n        r = Xc.indices[Xc.indptr[j]:Xc.indptr[j + 1]]\n        perm = rng.permutation(nT)\n        rows.append(perm[r])\n        cols.append(np.full(r.size, j))\n    Xr = sparse.csr_matrix((np.ones(sum(r.size for r in rows), dtype=np.int64),\n                            (np.concatenate(rows), np.concatenate(cols))), shape=(nT, N))\n    Ur, cntr = _unique_rows(Xr, rng)\n    curve_r = _integration_curve(Ur, cntr, nT, n_subsets, rng)\n    corr = curve - curve_r\n    m = corr[1:] / np.arange(1, N)\n    mpd = max(3, int(np.floor(0.1 * N + 0.5)))\n    cut = N + 1\n    if len(m) >= 3:\n        locs, _ = signal.find_peaks(m, distance=mpd)\n        if len(locs):\n            cut = locs[0] + 1 + 2          # 1-based Cut of complexity.m\n    kept = corr[:cut - 1]\n    Cn = np.sum(np.linspace(0, kept[-1], len(kept)) - kept) / len(kept)\n    return float(Cn), corr\n\n\ndef raster_matrix(raster: list[np.ndarray], bins: np.ndarray) -> sparse.csr_matrix:\n    \"\"\"(len(bins) x neurons) 0/1 matrix of the raster restricted to the given 1-based bins.\"\"\"\n    return _states(raster, bins)\n\n\n# ----------------------------------------------------------------------------------------------\n# Randomizations (randomizeasdf2.m), on rebinned rasters with bins 1..nbins\n\ndef rand_jitter(raster, nbins, sd_bins, rng):\n    \"\"\"Jitter: each spike moved by round(sd * N(0,1)) bins, kept in place when it would leave the\n    recording or land on another spike of the same neuron. randomizeasdf2.m moves spikes one at a\n    time in random order; here all moves are proposed at once and a move is accepted when its\n    target is free in the original train and not taken by an earlier proposal (in a random\n    order), which keeps the spike count, as Methods 2.5 require.\"\"\"\n    out = []\n    for s in raster:\n        n = s.size\n        if n == 0:\n            out.append(s)\n            continue\n        new = s + np.round(sd_bins * rng.standard_normal(n)).astype(np.int64)\n        ok = (new >= 1) & (new <= nbins) & ~np.isin(new, s)\n        order = rng.permutation(n)\n        cand = new[order]\n        okc = ok[order]\n        # first proposal for each target wins\n        _, first = np.unique(np.where(okc, cand, -1 - np.arange(n)), return_index=True)\n        win = np.zeros(n, dtype=bool)\n        win[first] = True\n        okc &= win\n        res = s.copy()\n        res[order[okc]] = cand[okc]\n        out.append(np.sort(res))\n    return out\n\n\ndef rand_wrap(raster, nbins, rng):\n    \"\"\"Wrap: each train cut at a random point and the two parts exchanged.\"\"\"\n    out = []\n    for s in raster:\n        cut = rng.integers(1, nbins + 1)\n        out.append(np.sort(np.where(s > cut, s - cut, s + (nbins - cut))))\n    return out\n\n\ndef rand_poisson(raster, nbins, rng):\n    \"\"\"Poisson: each neuron's spikes placed at distinct uniformly random bins.\"\"\"\n    return [np.sort(rng.choice(nbins, size=s.size, replace=False) + 1) for s in raster]\n\n\ndef rand_swap(raster, nbins, rng):\n    \"\"\"Swap: neuron labels of all spikes permuted (each neuron keeps its count, each bin its\n    activity), then every spike that landed on a neuron already spiking in that bin is traded\n    with a random other spike when the trade is valid, as randomizeasdf2.m 'swap'.\"\"\"\n    lab = np.concatenate([np.full(s.size, j) for j, s in enumerate(raster)])\n    t = np.concatenate(raster)\n    lab = lab[rng.permutation(lab.size)]\n    N = len(raster)\n    for _ in range(1000):\n        key = t * N + lab\n        order = np.argsort(key, kind=\"stable\")\n        dup = np.flatnonzero(np.diff(key[order]) == 0)\n        if dup.size == 0:\n            break\n        keys_set = set(key.tolist())\n        bad = order[dup + 1]\n        for i in bad:\n            for _try in range(200):\n                j = rng.integers(lab.size)\n                if lab[j] == lab[i] or t[j] == t[i]:\n                    continue\n                k1 = t[i] * N + lab[j]\n                k2 = t[j] * N + lab[i]\n                if k1 in keys_set or k2 in keys_set:\n                    continue\n                keys_set.discard(t[j] * N + lab[j])\n                keys_set.add(k1)\n                keys_set.add(k2)\n                lab[i], lab[j] = lab[j], lab[i]\n                break\n    return [np.sort(t[lab == j]) for j in range(N)]\n\n\ndef rand_shuffle(raster, nbins, rng):\n    \"\"\"Neuron shuffling (randomizeasdf2.m 'swap2', Methods 2.5): in each bin the active count is\n    kept and the active neurons drawn uniformly without replacement from all neurons.\"\"\"\n    N = len(raster)\n    act = activity(raster, nbins)\n    bins = np.flatnonzero(act) + 1\n    a = act[bins - 1]\n    # random keys per (bin, neuron); the a smallest keys in each bin are the active neurons\n    out_t, out_n = [], []\n    for start in range(0, bins.size, 20000):\n        b = bins[start:start + 20000]\n        aa = a[start:start + 20000]\n        keys = rng.random((b.size, N))\n        ranks = np.argsort(keys, axis=1)\n        mask = np.arange(N)[None, :] < aa[:, None]\n        rr, cc = np.nonzero(mask)\n        out_t.append(b[rr])\n        out_n.append(ranks[rr, cc])\n    t = np.concatenate(out_t)\n    n = np.concatenate(out_n)\n    return [np.sort(t[n == j]) for j in range(N)]\n\n\n# ----------------------------------------------------------------------------------------------\n# Branching ratio and susceptibility\n\ndef branching_new(act: np.ndarray, act_max: int, delays=BR_DELAYS):\n    \"\"\"brestimate.m: slopes r_k of A(t+k) on A(t) over bins with 0 <= A(t) <= act_max, fitted with\n    r_k = b B^k by non-linear least squares from (1, 1). Returns (B_new, B_simple, slopes).\"\"\"\n    act = act.astype(float)\n    slopes = []\n    for k in delays:\n        a0, ak = act[:-k], act[k:]\n        sel = a0 <= act_max\n        slopes.append(np.polyfit(a0[sel], ak[sel], 1)[0])\n    slopes = np.array(slopes)\n    a0, a1 = act[:-1], act[1:]\n    sel = a0 <= act_max\n    br_simple = np.polyfit(a0[sel], a1[sel], 1)[0]\n    try:\n        (B, b), _ = optimize.curve_fit(lambda k, B, b: b * B ** k, delays.astype(float), slopes,\n                                       p0=[1.0, 1.0], maxfev=20000)\n    except RuntimeError:\n        B = np.nan\n    return float(B), float(br_simple), slopes\n\n\ndef branching_basic(act: np.ndarray) -> float:\n    \"\"\"Eq. 11, the time average of A(t+1)/A(t) over bins with A(t) > 0.\"\"\"\n    a0, a1 = act[:-1].astype(float), act[1:].astype(float)\n    sel = a0 > 0\n    return float(np.mean(a1[sel] / a0[sel]))\n\n\ndef susceptibility(act: np.ndarray, n_neurons: int):\n    \"\"\"Eq. 14 as printed, var(A/N), and the Williams-Garcia et al. (2014) form N var(A/N), over all\n    bins (claims file, common detail 5).\"\"\"\n    rho = act.astype(float) / n_neurons\n    v = float(np.var(rho))\n    return v, n_neurons * v\n\n\n# ----------------------------------------------------------------------------------------------\n# Sub-sampling (Methods 2.10)\n\ndef subsample_sizes(n: int, n_samples: int = 30, layout: str = \"even\", rng=None):\n    \"\"\"Sizes of the sub-samples: 'even', 30 sizes evenly spaced from 40% of n to n (reading a of\n    the claims file); 'all', every integer size from 40% of n to n (reading b, 30 at each).\"\"\"\n    lo = int(np.ceil(0.4 * n))\n    if layout == \"even\":\n        return np.unique(np.round(np.linspace(lo, n, n_samples)).astype(int)).tolist() if False \\\n            else np.round(np.linspace(lo, n, n_samples)).astype(int).tolist()\n    return [m for m in range(lo, n + 1) for _ in range(n_samples)]\n\n\ndef wls_intercept(n_neurons, values):\n    \"\"\"Weighted least squares of values on 1/N with weight N; the intercept (1/N = 0).\"\"\"\n    n = np.asarray(n_neurons, dtype=float)\n    v = np.asarray(values, dtype=float)\n    ok = np.isfinite(v)\n    if ok.sum() < 2:\n        return np.nan\n    X = np.column_stack([1 / n[ok], np.ones(ok.sum())])\n    w = np.sqrt(n[ok])\n    beta, *_ = np.linalg.lstsq(X * w[:, None], v[ok] * w, rcond=None)\n    return float(beta[1])\n\n\n# ----------------------------------------------------------------------------------------------\n# Statistics\n\ndef fdr(p, method: str = \"bh\"):\n    \"\"\"Benjamini-Hochberg ('bh') or Benjamini-Yekutieli ('by') adjusted p-values.\"\"\"\n    p = np.asarray(p, dtype=float)\n    m = p.size\n    order = np.argsort(p)\n    c = np.sum(1.0 / np.arange(1, m + 1)) if method == \"by\" else 1.0\n    adj = p[order] * m * c / np.arange(1, m + 1)\n    adj = np.minimum.accumulate(adj[::-1])[::-1]\n    out = np.empty(m)\n    out[order] = np.minimum(adj, 1.0)\n    return out\n\n\ndef terrell_scott_mode(x):\n    \"\"\"Mode of a histogram with the Terrell-Scott (1985) number of bins, (2n)^(1/3).\"\"\"\n    x = np.asarray(x, dtype=float)\n    x = x[np.isfinite(x)]\n    k = int(np.ceil((2 * x.size) ** (1 / 3)))\n    h, e = np.histogram(x, bins=k)\n    i = int(np.argmax(h))\n    return float((e[i] + e[i + 1]) / 2), k\n"
}
```

```
File created successfully at: entries/crcns-hc-8-timme-2016/hc8.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016 && source $TMPDIR/dev/bin/activate && cat > $TMPDIR/survey.py <<'EOF'
import time, numpy as np, hc8, sys, hashlib, pickle
from concurrent.futures import ThreadPoolExecutor
import threading
names = hc8.recording_names()
print(len(names), names[:3])
loc = threading.local()
def one(n):
    if not hasattr(loc,'z'): loc.z = hc8.open_zip()
    d = hc8.load(n, loc.z)
    sp = d['spikes']
    allt = np.concatenate(sp)
    r = dict(name=n, nN=d['nNeurons'], nspikes=[s.size for s in sp], nbins=d['nbins'], binsize=d['binsize'],
             rid=d['recordingID'], tmin=int(allt.min()) if allt.size else -1, tmax=int(allt.max()) if allt.size else -1,
             sorted=all(np.all(np.diff(s)>=0) for s in sp), dups=sum(int(np.sum(np.diff(np.sort(s))==0)) for s in sp),
             lenmatch=len(sp)==d['nNeurons'], datatype=d['datatype'], expsys=d['expsys'],
             nchan=len(d['channel']), chan=np.asarray(d['channel']).tolist(),
             hash=hashlib.md5(b''.join(np.sort(s).tobytes() for s in sp)).hexdigest(),
             neuronhash=[hashlib.md5(s.tobytes()).hexdigest() for s in sp],
             stdmin=getattr(d['wave_clus'],'stdmin',None), sr=getattr(d['wave_clus'],'sr',None), ref=getattr(d['wave_clus'],'ref',None))
    return r
k = int(sys.argv[1])
t=time.time()
with ThreadPoolExecutor(8) as ex: res=list(ex.map(one, names[:k]))
print('time', time.time()-t)
pickle.dump(res, open(sys.argv[2],'wb'))
EOF
python $TMPDIR/survey.py 16 $TMPDIR/s16.pkl
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 1, in <module>
    import time, numpy as np, hc8, sys, hashlib, pickle
ModuleNotFoundError: No module named 'hc8'
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016 && source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/survey.py 16 $TMPDIR/s16.pkl
```

```
435 ['Data/Culture1DIV6.mat', 'Data/Culture1DIV9.mat', 'Data/Culture1DIV10.mat']
time 1.779940128326416
```

**Agent**

Loading is fast (about 0.1 s per recording). Running the full survey of all 435 files.

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/survey.py 435 $TMPDIR/sall.pkl && python - <<'EOF'
import pickle, numpy as np, collections
res=pickle.load(open('/tmp/claude-1001/sall.pkl','rb')) if False else pickle.load(open(__import__('os').environ['TMPDIR']+'/sall.pkl','rb'))
nN=np.array([r['nN'] for r in res]); print('recs',len(res),'neurons',nN.sum(),'min',nN.min(),'max',nN.max(),'mean',nN.mean(),'median',np.median(nN))
print('lenmatch', all(r['lenmatch'] for r in res), 'sorted', sum(r['sorted'] for r in res), 'dups', sum(r['dups']>0 for r in res), sum(r['dups'] for r in res))
nb=np.array([r['nbins'] for r in res]); print('nbins min/max', nb.min(), nb.max(), (nb*0.05/60000).min(), (nb*0.05/60000).max())
tm=np.array([r['tmax'] for r in res]); print('tmax > nbins', np.sum(tm>nb), 'tmin',min(r['tmin'] for r in res))
print('short <59min', np.sum(nb < 59*60e3/0.05))
print(collections.Counter(r['binsize'] for r in res), collections.Counter(r['datatype'] for r in res), collections.Counter(r['expsys'] for r in res))
print(collections.Counter(str(r['stdmin']) for r in res), collections.Counter(str(r['sr']) for r in res), collections.Counter(str(r['ref']) for r in res))
h=collections.Counter(r['hash'] for r in res); print('dup recordings', [k for k,v in h.items() if v>1])
rid=collections.Counter(r['rid'] for r in res); print('dup recordingIDs', [(k,v) for k,v in rid.items() if v>1][:10])
zero=sum(sum(1 for c in r['nspikes'] if c==0) for r in res); print('empty neurons', zero)
# neuron-level duplicates across recordings
nh=collections.defaultdict(list)
for r in res:
    for j,(hh,c) in enumerate(zip(r['neuronhash'],r['nspikes'])):
        if c>10: nh[hh].append((r['name'],j))
d=[v for v in nh.values() if len(set(x[0] for x in v))>1]; print('neurons identical across recordings', len(d), d[:5])
w=[v for v in nh.values() if len(v)>1 and len(set(x[0] for x in v))==1]; print('identical neurons within recording', len(w), w[:3])
cult=collections.Counter(int(r['name'].split('Culture')[1].split('DIV')[0]) for r in res); print('cultures', len(cult), sorted(cult.items()))
EOF
```

```
435 ['Data/Culture1DIV6.mat', 'Data/Culture1DIV9.mat', 'Data/Culture1DIV10.mat']
time 19.938902378082275
recs 435 neurons 39529 min 3 max 142 mean 90.8712643678161 median 91.0
lenmatch True sorted 435 dups 6 21
nbins min/max 70993936 89449936 59.161613333333335 74.54161333333333
tmax > nbins 47 tmin 22
short <59min 0
Counter({0.05: 435}) Counter({'Spikes': 435}) Counter({'Rat Hippocampal Dissociated Cultures': 435})
Counter({'5': 435}) Counter({'20000': 435}) Counter({'30': 435})
dup recordings []
dup recordingIDs []
empty neurons 0
neurons identical across recordings 0 []
identical neurons within recording 0 []
cultures 28 [(1, 23), (2, 16), (3, 24), (4, 26), (5, 24), (6, 15), (7, 14), (8, 13), (9, 14), (10, 14), (11, 13), (12, 14), (13, 13), (14, 14), (15, 15), (16, 15), (17, 14), (18, 14), (19, 14), (20, 14), (21, 13), (22, 13), (23, 15), (24, 14), (25, 14), (26, 14), (27, 15), (28, 14)]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import time, numpy as np, hc8
z=hc8.open_zip(); names=hc8.recording_names()
n=names[100]; d=hc8.load(n,z); print(n, d['nNeurons'])
t=time.time()
sp=hc8.first_window(d['spikes'])
isi=hc8.network_isi_bins(sp); f=int(round(isi)); print('isi bins',isi, 'ms', isi*0.05)
r,nb=hc8.rebin(sp,f); act=hc8.activity(r,nb); size,dur,st=hc8.avalanches(act)
print('nav',size.size,'nbins',nb,'active bins',(act>0).sum(), 'maxsize',size.max(),'maxdur',dur.max(), time.time()-t)
rng=np.random.default_rng(0)
t=time.time(); fs=hc8.plparams(hc8.apply_cuts(size),rng); print('size fit',fs, time.time()-t)
t=time.time(); fd=hc8.plparams(hc8.apply_cuts(dur),rng); print('dur fit',fd, time.time()-t)
t=time.time(); print('sgd', hc8.sizegivdur(size,dur,fd['xmin'],fd['xmax']), time.time()-t)
t=time.time(); prof=hc8.mean_profiles(act,size,dur,st); print('nprof',len(prof), hc8.shape_collapse(prof), time.time()-t)
t=time.time(); print('br', hc8.branching_new(act,10)[:2], hc8.branching_basic(act), hc8.susceptibility(act,len(r)), time.time()-t)
bins=np.flatnonzero(act)+1
X=hc8.raster_matrix(r,bins); U,c=hc8._unique_rows(X,rng); print('X',X.shape,'nnz',X.nnz,'unique',U.shape)
t=time.time(); C=hc8.complexity(X,5,rng); print('complexity n5',C[0], time.time()-t)
for nm,fn in [('j1',lambda: hc8.rand_jitter(r,nb,1,rng)),('j100',lambda: hc8.rand_jitter(r,nb,100,rng)),('wrap',lambda: hc8.rand_wrap(r,nb,rng)),('pois',lambda: hc8.rand_poisson(r,nb,rng)),('swap',lambda: hc8.rand_swap(r,nb,rng)),('shuf',lambda: hc8.rand_shuffle(r,nb,rng))]:
    t=time.time(); rr=fn(); a2=hc8.activity(rr,nb)
    print(nm, time.time()-t, 'counts kept', all(a.size==b.size for a,b in zip(r,rr)), 'act same', np.array_equal(a2,act), 'nav', hc8.avalanches(a2)[0].size)
EOF
```

```
Data/Culture5DIV19.mat 104
isi bins 194.83151435097278 ms 9.74157571754864
nav 70981 nbins 363077 active bins 186152 maxsize 586 maxdur 114 0.1170206069946289
size fit {'tau': 2.834, 'xmin': 11, 'xmax': 42, 'p': 0.246, 'ks': 0.011845636007647542, 'n': 5182, 'n_tried': 119} 0.03708195686340332
dur fit {'tau': 3.302, 'xmin': 7, 'xmax': 23, 'p': 0.706, 'ks': 0.007562962169374021, 'n': 4028, 'n_tried': 22} 0.008440494537353516
sgd 1.3453400409078886 0.031182527542114258
nprof 20 (1.341, -0.9294053000604375) 0.04536175727844238
br (0.9657086070749376, 0.45814148867494764) 0.7794784280151522 (0.00019302034082958338, 0.020074115446276672) 0.20469307899475098
X (186152, 104) nnz 353026 unique (31294, 104)
complexity n5 0.0037299088444550086 1.865929126739502
j1 0.12134170532226562 counts kept True act same False nav 70844
j100 0.1265850067138672 counts kept True act same False nav 82345
wrap 0.030895709991455078 counts kept True act same False nav 82088
pois 0.036472320556640625 counts kept True act same False nav 84972
swap 0.23732423782348633 counts kept True act same True nav 70981
shuf 0.4225132465362549 counts kept False act same True nav 70981
```

**Agent calls Bash**

```bash
date -u
```

```
Mon Nov  9 06:11:19 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
import numpy as np, pandas as pd, time
rng=np.random.default_rng(0); h=rng.integers(0,5000,31000).astype(np.int64)*1234567891
t=time.time()
for _ in range(200): np.unique(h, return_inverse=True)
print('unique', (time.time()-t)/200*1e3,'ms')
t=time.time()
for _ in range(200): c,u=pd.factorize(h)
print('factorize', (time.time()-t)/200*1e3,'ms')
from scipy import sparse
X=sparse.random(31000,104,density=0.02,format='csc',random_state=0); X.data[:]=1; X=X.astype(np.int64)
w=rng.integers(1,2**62,104,dtype=np.int64)
t=time.time()
for _ in range(200): X@w
print('matvec csc', (time.time()-t)/200*1e3,'ms')
Xr=X.tocsr()
t=time.time()
for _ in range(200): Xr@w
print('matvec csr', (time.time()-t)/200*1e3,'ms')
EOF
```

```
unique 0.9862101078033447 ms
factorize 0.2686154842376709 ms
matvec csc 0.08882403373718262 ms
matvec csr 0.21738529205322266 ms
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
import re
p='hc8.py'; s=open(p).read()
s=s.replace("""            h = Ud @ w
            _, inv = np.unique(h, return_inverse=True)
            p = np.bincount(inv, weights=cnt) / nT""","""            inv, _ = pd.factorize(Ud @ w)
            p = np.bincount(inv, weights=cnt) / nT""")
s=s.replace("import numpy as np\nimport scipy.io","import numpy as np\nimport pandas as pd\nimport scipy.io")
open(p,'w').write(s)
EOF
PYTHONPATH=. python - <<'EOF'
import time, numpy as np, hc8
z=hc8.open_zip(); names=hc8.recording_names()
for n in [names[100], names[300]]:
    d=hc8.load(n,z); sp=hc8.first_window(d['spikes']); f=int(round(hc8.network_isi_bins(sp)))
    r,nb=hc8.rebin(sp,f); act=hc8.activity(r,nb); bins=np.flatnonzero(act)+1
    X=hc8.raster_matrix(r,bins)
    for ns in [10,30,100]:
        t=time.time(); v=[hc8.complexity(X,ns,np.random.default_rng(s))[0] for s in range(3 if ns<100 else 2)]
        print(n, ns, np.round(v,5), (time.time()-t)/len(v))
EOF
```

```
Data/Culture5DIV19.mat 10 [0.00113 0.00182 0.00036] 1.7725079854329426
Data/Culture5DIV19.mat 30 [0.00195 0.00072 0.00309] 4.70199720064799
Data/Culture5DIV19.mat 100 [0.00032 0.0007 ] 15.017948269844055
Data/Culture19DIV18.mat 10 [0.00628 0.00486 0.00242] 2.1867052714029946
Data/Culture19DIV18.mat 30 [0.00214 0.00032 0.00172] 5.872151056925456
Data/Culture19DIV18.mat 100 [0.00073 0.00371] 18.8708473443985
```

**Agent calls Bash**

```bash
cd  && sed -n 1,80p tools/entry.py | sed -n 20,80p; grep -n "def \|timeout\|max_minutes\|ENCORE\|environ" tools/entry.py | head -60
```

```
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.

`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
executed/<name>/handover/. Run the entry first.

Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
script itself. The entry's own dependencies come only from its lock file.
"""
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/crcns-hc-8-timme-2016/hc8.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# Per-recording pipeline

RANDOMIZATIONS = ["jitter1", "jitter10", "jitter100", "wrap", "poisson", "swap", "shuffle"]
JITTER_SD = {"jitter1": 1, "jitter10": 10, "jitter100": 100}   # Methods 2.5, in rebinned bins


def prepare(d: dict) -> dict:
    """First 59 min, network ISI, rebinning, activity and avalanches of one recording.

    Neurons with no spike in the first 59 min are dropped (complexity.m would give NaN for them);
    the number dropped is returned."""
    sp = first_window(d["spikes"])
    n_all = len(sp)
    counts_all = np.array([s.size for s in sp])
    sp = [s for s in sp if s.size > 0]
    isi = network_isi_bins(sp)
    factor = max(1, int(round(isi)))
    r, nb = rebin(sp, factor)
    act = activity(r, nb)
    return dict(name=d["name"], spikes=sp, counts_all=counts_all, n_all=n_all,
                n_silent=int(n_all - len(sp)), isi_bins=isi, factor=factor, raster=r, nbins=nb,
                act=act)


def randomize(kind: str, raster, nbins, rng):
    if kind in JITTER_SD:
        return rand_jitter(raster, nbins, JITTER_SD[kind], rng)
    return {"wrap": rand_wrap, "poisson": rand_poisson, "swap": rand_swap,
            "shuffle": rand_shuffle}[kind](raster, nbins, rng)


def criticality(act: np.ndarray, n_neurons: int, rng: np.random.Generator) -> dict:
    """Avalanche counts, the size and duration fits with range search, size given duration,
    shape collapse and susceptibility of one activity series."""
    size, dur, starts = avalanches(act)
    cs, cd = apply_cuts(size), apply_cuts(dur)
    fs = plparams(cs, rng) if cs.size else plparams(np.array([1]), rng)
    fd = plparams(cd, rng) if cd.size else plparams(np.array([1]), rng)
    prof = mean_profiles(act, size, dur, starts)
    sc_exp, curv = shape_collapse(prof)
    chi_a, chi_b = susceptibility(act, n_neurons)
    return dict(n_av=int(size.size), n_size_cut_values=int(np.unique(cs).size),
                n_dur_cut_values=int(np.unique(cd).size), n_profiles=len(prof),
                tau=fs["tau"], s_xmin=fs["xmin"], s_xmax=fs["xmax"], s_p=fs["p"],
                s_tried=fs["n_tried"],
                alpha=fd["tau"], d_xmin=fd["xmin"], d_xmax=fd["xmax"], d_p=fd["p"],
                d_tried=fd["n_tried"],
                s_range=np.log10(fs["xmax"] / fs["xmin"]) if np.isfinite(fs["tau"]) else np.nan,
                d_range=np.log10(fd["xmax"] / fd["xmin"]) if np.isfinite(fd["tau"]) else np.nan,
                sgd=sizegivdur(size, dur, fd["xmin"], fd["xmax"]),
                sc_exp=sc_exp, curv=curv, abs_curv=abs(curv) if np.isfinite(curv) else np.nan,
                chi_a=chi_a, chi_b=chi_b)


def avalanche_ratio(act: np.ndarray) -> float:
    """avprops.m 'ratio': per avalanche sum of s(t+1)/s(t) over its bins divided by its duration;
    the mean over avalanches."""
    size, dur, starts = avalanches(act)
    a = act.astype(float)
    nxt = np.concatenate([a[1:], [0]])
    within = (a > 0) & (nxt > 0)
    ratio = np.where(within, nxt / np.where(a > 0, a, 1), 0.0)
    cs = np.concatenate([[0], np.cumsum(ratio)])
    per = (cs[starts + dur] - cs[starts]) / dur
    return float(per.mean())


def subsample_exponents(spikes: list[np.ndarray], rng: np.random.Generator, own_isi: bool,
                        factor_full: int, sizes: list[int]) -> dict:
    """Methods 2.10 for the culture exponents: for each sub-sample of neurons, tau and alpha by the
    MLE over all avalanches that survive the cuts (no range search), 1/sigma nu z from size given
    duration over the cut duration range and from the shape collapse, then the weighted least
    squares intercept on 1/N. own_isi: each sub-sample rebinned to its own network ISI (the
    analysis of the whole system, Methods 2.3, repeated, as Methods 2.10 say the analyses were
    identical); otherwise the full system's bin."""
    N = len(spikes)
    lab = np.concatenate([np.full(s.size, j) for j, s in enumerate(spikes)])
    t = np.concatenate(spikes)
    o = np.argsort(t, kind="stable")
    t, lab = t[o], lab[o]
    vals = {k: [] for k in ("tau", "alpha", "sgd", "sc_exp")}
    for m in sizes:
        keep = np.zeros(N, dtype=bool)
        keep[rng.permutation(N)[:m]] = True
        sel = keep[lab]
        tt, ll = t[sel], lab[sel]
        f = max(1, int(round((tt[-1] - tt[0]) / (tt.size - 1)))) if own_isi else factor_full
        b = np.ceil(tt / f).astype(np.int64)
        key = np.unique(b * N + ll)
        nb = int(np.ceil(ANALYSIS_BINS / f))
        act = np.bincount(key // N, minlength=nb + 1)[1:nb + 1].astype(np.int32)
        size, dur, starts = avalanches(act)
        cs, cd = apply_cuts(size), apply_cuts(dur)
        vals["tau"].append(plmle_full(cs) if cs.size else np.nan)
        vals["alpha"].append(plmle_full(cd) if cd.size else np.nan)
        vals["sgd"].append(sizegivdur(size, dur, cd.min(), cd.max()) if cd.size else np.nan)
        prof = mean_profiles(act, size, dur, starts)
        vals["sc_exp"].append(shape_collapse(prof)[0])
    return {k: wls_intercept(sizes, v) for k, v in vals.items()}
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> entries/crcns-hc-8-timme-2016/hc8.py <<'EOF'


_ZF = None


def _worker_zip():
    global _ZF
    if _ZF is None:
        _ZF = open_zip()
    return _ZF


def culture_record(args) -> dict:
    """Notebook 1, one recording: counts, ISI, real-data criticality measures, branching ratios,
    sub-sampled exponents (both rebinning readings) and the criticality measures of each
    randomization. args = (index, name, seed)."""
    i, name, seed = args
    d = load(name, _worker_zip())
    p = prepare(d)
    N = len(p["raster"])
    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1],
               n_neurons=d["nNeurons"], n_silent=p["n_silent"], nbins_file=d["nbins"],
               isi_ms=p["isi_bins"] * BIN_MS, factor=p["factor"],
               rates=p["counts_all"] / (ANALYSIS_MIN * 60.0),
               t_max_ms=float(max(s.max() for s in d["spikes"] if s.size) * BIN_MS),
               min_isi_ms=float(min(np.diff(s).min() for s in d["spikes"] if s.size > 1) * BIN_MS))
    act = p["act"]
    res = {"real": criticality(act, N, np.random.default_rng([seed, i, 1]))}
    out["B_new"], out["B_simple"], out["slopes"] = branching_new(act, BR_ACT_MAX_CULTURE)
    out["B_basic"] = branching_basic(act)
    out["B_avalanche"] = avalanche_ratio(act)
    sizes = subsample_sizes(N)
    for own, tag in ((True, "own"), (False, "fixed")):
        ss = subsample_exponents(p["spikes"], np.random.default_rng([seed, i, 2 + own]), own,
                                 p["factor"], sizes)
        for k, v in ss.items():
            out[f"ss_{tag}_{k}"] = v
    for j, kind in enumerate(RANDOMIZATIONS):
        rng = np.random.default_rng([seed, i, 10 + j])
        rr = randomize(kind, p["raster"], p["nbins"], rng)
        a2 = activity(rr, p["nbins"])
        if kind in ("swap", "shuffle"):
            out[f"{kind}_act_identical"] = bool(np.array_equal(a2, act))
            out[f"{kind}_counts_kept"] = bool(all(a.size == b.size for a, b in zip(rr, p["raster"])))
            res[kind] = dict(res["real"])   # A(t) is unchanged, so every avalanche measure is
            continue
        out[f"{kind}_counts_kept"] = bool(all(a.size == b.size for a, b in zip(rr, p["raster"])))
        res[kind] = criticality(a2, N, rng)
    out["measures"] = res
    return out


def complexity_record(args) -> dict:
    """Notebook 2, one recording: complexity (sub-sampling correction on, n_subsets random subsets
    per size) on the avalanche bins of the real data and of each randomization, with the real
    data's susceptibility and fit ranges. args = (index, name, seed, n_subsets)."""
    i, name, seed, n_subsets = args
    d = load(name, _worker_zip())
    p = prepare(d)
    N = len(p["raster"])
    act = p["act"]
    crit = criticality(act, N, np.random.default_rng([seed, i, 1]))
    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1], n_neurons=N,
               chi_a=crit["chi_a"], chi_b=crit["chi_b"], s_range=crit["s_range"],
               d_range=crit["d_range"], n_av=crit["n_av"], n_profiles=crit["n_profiles"],
               n_size_cut_values=crit["n_size_cut_values"],
               n_dur_cut_values=crit["n_dur_cut_values"])
    for j, kind in enumerate(["real"] + RANDOMIZATIONS):
        rng = np.random.default_rng([seed, i, 100 + j])
        rr = p["raster"] if kind == "real" else randomize(kind, p["raster"], p["nbins"], rng)
        a2 = act if kind == "real" else activity(rr, p["nbins"])
        bins = np.flatnonzero(a2) + 1
        X = raster_matrix(rr, bins)
        # a neuron that the shuffle left without a spike has no entropy; drop it
        keep = np.asarray(X.sum(axis=0)).ravel() > 0
        X = X[:, keep] if not keep.all() else X
        out[f"C_{kind}"] = complexity(X, n_subsets, rng)[0]
        out[f"nbins_{kind}"] = int(bins.size)
    return out
EOF
cd entries/crcns-hc-8-timme-2016 && source $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import time, numpy as np, hc8, resource
names=hc8.recording_names()
for i in [0, 100, 300]:
    t=time.time(); o=hc8.culture_record((i,names[i],1)); 
    print(names[i], round(time.time()-t,1),'s', {k:(round(v,3) if isinstance(v,float) else v) for k,v in o.items() if k not in ('measures','rates','slopes')})
    for k,m in o['measures'].items(): print('  ',k, {a:(round(b,3) if isinstance(b,float) else b) for a,b in m.items()})
print('maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
EOF
```

```
Data/Culture1DIV6.mat 11.7 s {'name': 'Data/Culture1DIV6.mat', 'culture': 1, 'div': 6, 'n_neurons': 89, 'n_silent': 0, 'nbins_file': 71567936, 'isi_ms': 6.611, 'factor': 132, 't_max_ms': 3578377.35, 'min_isi_ms': 0.1, 'B_new': 0.985, 'B_simple': 0.281, 'B_basic': 0.755, 'B_avalanche': 0.439, 'ss_own_tau': 2.384, 'ss_own_alpha': 3.087, 'ss_own_sgd': 1.195, 'ss_own_sc_exp': 1.297, 'ss_fixed_tau': 1.763, 'ss_fixed_alpha': 2.439, 'ss_fixed_sgd': 1.085, 'ss_fixed_sc_exp': 1.22, 'jitter1_counts_kept': True, 'jitter10_counts_kept': True, 'jitter100_counts_kept': True, 'wrap_counts_kept': True, 'poisson_counts_kept': True, 'swap_act_identical': True, 'swap_counts_kept': True, 'shuffle_act_identical': True, 'shuffle_counts_kept': False}
   real {'n_av': 119426, 'n_size_cut_values': 37, 'n_dur_cut_values': 20, 'n_profiles': 20, 'tau': 3.364, 's_xmin': 13, 's_xmax': 39, 's_p': 0.246, 's_tried': 156, 'alpha': 3.995, 'd_xmin': 8, 'd_xmax': 24, 'd_p': 0.404, 'd_tried': 31, 's_range': np.float64(0.477), 'd_range': np.float64(0.477), 'sgd': 1.283, 'sc_exp': 1.256, 'curv': 0.012, 'abs_curv': 0.012, 'chi_a': 0.0, 'chi_b': 0.015}
   jitter1 {'n_av': 119224, 'n_size_cut_values': 37, 'n_dur_cut_values': 21, 'n_profiles': 21, 'tau': 3.352, 's_xmin': 12, 's_xmax': 41, 's_p': 0.574, 's_tried': 122, 'alpha': 3.878, 'd_xmin': 8, 'd_xmax': 25, 'd_p': 0.55, 'd_tried': 31, 's_range': np.float64(0.534), 'd_range': np.float64(0.495), 'sgd': 1.297, 'sc_exp': 1.25, 'curv': -0.04, 'abs_curv': 0.04, 'chi_a': 0.0, 'chi_b': 0.015}
   jitter10 {'n_av': 120591, 'n_size_cut_values': 35, 'n_dur_cut_values': 20, 'n_profiles': 20, 'tau': 3.169, 's_xmin': 11, 's_xmax': 38, 's_p': 0.988, 's_tried': 101, 'alpha': 3.831, 'd_xmin': 9, 'd_xmax': 23, 'd_p': 0.908, 'd_tried': 42, 's_range': np.float64(0.538), 'd_range': np.float64(0.407), 'sgd': 1.315, 'sc_exp': 1.276, 'curv': -0.112, 'abs_curv': 0.112, 'chi_a': 0.0, 'chi_b': 0.014}
   jitter100 {'n_av': 121287, 'n_size_cut_values': 45, 'n_dur_cut_values': 25, 'n_pr
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import time, numpy as np, hc8
names=hc8.recording_names()
for i in [0, 300]:
    t=time.time(); o=hc8.complexity_record((i,names[i],1,10)); print(round(time.time()-t,1), {k:(round(v,5) if isinstance(v,float) else v) for k,v in o.items()})
EOF
```

```
17.2 {'name': 'Data/Culture1DIV6.mat', 'culture': 1, 'div': 6, 'n_neurons': 89, 'chi_a': 0.00017, 'chi_b': 0.01482, 's_range': np.float64(0.47712), 'd_range': np.float64(0.47712), 'n_av': 119426, 'n_profiles': 20, 'n_size_cut_values': 37, 'n_dur_cut_values': 20, 'C_real': 0.00013, 'nbins_real': 313973, 'C_jitter1': 1e-05, 'nbins_jitter1': 314377, 'C_jitter10': 3e-05, 'nbins_jitter10': 317347, 'C_jitter100': 8e-05, 'nbins_jitter100': 327359, 'C_wrap': 0.00012, 'nbins_wrap': 338673, 'C_poisson': 0.0007, 'nbins_poisson': 338183, 'C_swap': 0.00049, 'nbins_swap': 313973, 'C_shuffle': 2e-05, 'nbins_shuffle': 313973}
19.7 {'name': 'Data/Culture19DIV18.mat', 'culture': 19, 'div': 18, 'n_neurons': 92, 'chi_a': 0.00033, 'chi_b': 0.03006, 's_range': np.float64(0.65321), 'd_range': np.float64(0.66901), 'n_av': 95238, 'n_profiles': 35, 'n_size_cut_values': 43, 'n_dur_cut_values': 35, 'C_real': 0.00297, 'nbins_real': 244099, 'C_jitter1': 0.00026, 'nbins_jitter1': 253772, 'C_jitter10': 0.00102, 'nbins_jitter10': 271950, 'C_jitter100': 3e-05, 'nbins_jitter100': 318834, 'C_wrap': 0.00053, 'nbins_wrap': 330008, 'C_poisson': 0.00212, 'nbins_poisson': 329919, 'C_swap': 5e-05, 'nbins_swap': 244099, 'C_shuffle': 0.15322, 'nbins_shuffle': 244099}
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import numpy as np, hc8
from scipy import signal
names=hc8.recording_names(); i=300
d=hc8.load(names[i]); p=hc8.prepare(d)
for kind in ['real','shuffle']:
  for s in range(3):
    rng=np.random.default_rng([1,i,s])
    rr=p['raster'] if kind=='real' else hc8.randomize(kind,p['raster'],p['nbins'],rng)
    a2=hc8.activity(rr,p['nbins']); bins=np.flatnonzero(a2)+1; X=hc8.raster_matrix(rr,bins)
    C,corr=hc8.complexity(X,10,rng)
    N=X.shape[1]; m=corr[1:]/np.arange(1,N); locs,_=signal.find_peaks(m,distance=max(3,round(0.1*N)))
    print(kind, s, round(C,5), 'N',N,'first peak k', (locs[0]+2) if len(locs) else None, 'corr[k] at 2,5,10,20,50,N', np.round(corr[[1,4,9,19,49,N-1]],3))
EOF
```

```
real 0 0.0012 N 92 first peak k 4 corr[k] at 2,5,10,20,50,N [0.000e+00 1.000e-03 1.300e-02 5.900e-02 4.320e-01 1.377e+00]
real 1 0.00438 N 92 first peak k 11 corr[k] at 2,5,10,20,50,N [0.000e+00 1.000e-03 8.000e-03 5.600e-02 3.910e-01 1.375e+00]
real 2 0.00251 N 92 first peak k 9 corr[k] at 2,5,10,20,50,N [0.    0.002 0.013 0.081 0.379 1.371]
shuffle 0 0.12523 N 92 first peak k 76 corr[k] at 2,5,10,20,50,N [0.000e+00 1.000e-03 3.000e-03 3.000e-02 3.890e-01 1.114e+00]
shuffle 1 0.15272 N 92 first peak k None corr[k] at 2,5,10,20,50,N [0.000e+00 1.000e-03 3.000e-03 3.000e-02 3.880e-01 1.106e+00]
shuffle 2 0.15381 N 92 first peak k None corr[k] at 2,5,10,20,50,N [0.    0.    0.003 0.03  0.388 1.109]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
p='hc8.py'; s=open(p).read()
old="""    kept = corr[:cut - 1]
    Cn = np.sum(np.linspace(0, kept[-1], len(kept)) - kept) / len(kept)
    return float(Cn), corr
"""
new="""    kept = corr[:cut - 1]
    Cn = np.sum(np.linspace(0, kept[-1], len(kept)) - kept) / len(kept)
    if return_variants:
        uncut = np.sum(np.linspace(0, corr[-1], N) - corr) / N
        raw = np.sum(np.linspace(0, curve[-1], N) - curve) / N
        return dict(cut=float(Cn), uncut=float(uncut), raw=float(raw), k_kept=len(kept), N=N)
    return float(Cn), corr
"""
assert old in s; s=s.replace(old,new)
s=s.replace("""def complexity(X: sparse.csr_matrix, n_subsets: int, rng: np.random.Generator,
               subsamp_correct: bool = True):""","""def complexity(X: sparse.csr_matrix, n_subsets: int, rng: np.random.Generator,
               subsamp_correct: bool = True, return_variants: bool = False):""")
s=s.replace("""    (findpeaks with a minimum peak distance of max(3, round(0.1 N))). Returns (Cn, curve).\"\"\"""",
"""    (findpeaks with a minimum peak distance of max(3, round(0.1 N))). Returns (Cn, curve), or
    with return_variants a dict: 'cut' (complexity.m), 'uncut' (the corrected curve without the
    cut), 'raw' (no correction), 'k_kept' (subset sizes kept by the cut) and 'N'.\"\"\"""")
old2="""        out[f"C_{kind}"] = complexity(X, n_subsets, rng)[0]
"""
new2="""        cv = complexity(X, n_subsets, rng, return_variants=True)
        out[f"C_{kind}"] = cv["cut"]
        out[f"Cuncut_{kind}"] = cv["uncut"]
        out[f"Craw_{kind}"] = cv["raw"]
        out[f"kkept_{kind}"] = cv["k_kept"]
        out[f"N_{kind}"] = cv["N"]
"""
assert old2 in s; s=s.replace(old2,new2)
open(p,'w').write(s)
EOF
date -u
```

```
Mon Nov  9 06:17:17 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-hc-8-timme-2016/models.py",
 "content": "\"\"\"The three models of Timme et al. (2016), Methods 2.4, ported from the NCC MATLAB toolbox.\n\nThese are simulations: they use no recorded data. Parameters:\n\n- Chain model (Methods 2.4, last paragraph): 12 neurons, the first active or inactive in\n  alternate runs (so p = 0.5 each), p(a_i+1 = a_i) = 0.5 (1 + c). Methods 2.9 say the model's\n  joint distribution was defined exactly, so the complexity uses the exact distribution and every\n  subset of each size (Eq. 10; \"the lesser of all possible permutations or 100\").\n- Bethe lattice (Methods 2.4, `bethelattice.m`): each neuron sends two connections to the next\n  layer, p_trans = 0.5, one active neuron in layer 1 per run, activity stopped at layer 10^4.\n  The number of runs, 10^4, is the claims file's standard choice. Small avalanches are runs whose\n  last active layer is 8 or less (\"stopped on or before the 8th layer\", Results 3.1); in the\n  raster, runs follow each other with one silent bin between them, as `bethelattice.m` places\n  them, over the 255 neurons of layers 1 to 8.\n- Cortical branching model (Methods 2.4, `cbmodel.m` with method 'spont'): 100 neurons on a\n  10 x 10 torus, four nearest neighbours, p_spont = 10^-4, 3 x 10^5 steps. A neuron with j\n  active neighbours fires with the probability `cbmodel.m` builds, P_0 = p_spont,\n  P_j+1 = P_j + p_trans - P_j p_trans.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom itertools import combinations\n\nimport numpy as np\n\n\n# ----------------------------------------------------------------------------------------------\n# Chain model\n\ndef chain_joint(c: float, n: int = 12):\n    \"\"\"All 2^n states and their exact probabilities.\"\"\"\n    states = ((np.arange(2 ** n)[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int8)\n    same = states[:, 1:] == states[:, :-1]\n    p = 0.5 * np.prod(np.where(same, 0.5 * (1 + c), 0.5 * (1 - c)), axis=1)\n    return states, p\n\n\ndef _entropy(p):\n    p = p[p > 0]\n    return float(-np.sum(p * np.log2(p)))\n\n\ndef chain_integration_curve(c: float, n: int = 12):\n    \"\"\"Mean integration over all subsets of each size k = 1..n (Eq. 9), from the exact joint.\"\"\"\n    states, p = chain_joint(c, n)\n    weights = 1 << np.arange(n)\n    h1 = np.array([_entropy(np.bincount(states[:, i], weights=p, minlength=2)) for i in range(n)])\n    curve = np.zeros(n)\n    for k in range(2, n + 1):\n        vals = []\n        for sub in combinations(range(n), k):\n            sub = list(sub)\n            code = states[:, sub] @ weights[:k]\n            hj = _entropy(np.bincount(code, weights=p, minlength=2 ** k))\n            vals.append(h1[sub].sum() - hj)\n        curve[k - 1] = np.mean(vals)\n    return curve\n\n\ndef complexity_from_curve(curve):\n    \"\"\"Eq. 10: (1/N) sum over k of [(k-1)/(N-1) I(X) - <I(X_j^k)>].\"\"\"\n    N = len(curve)\n    return float(np.sum(np.linspace(0, curve[-1], N) - curve) / N)\n\n\n# ----------------------------------------------------------------------------------------------\n# Bethe lattice\n\ndef bethe_full_sizes(n_runs: int, rng, p: float = 0.5, stop_layer: int = 10 ** 4):\n    \"\"\"Sizes, durations and profiles of the full model (counts per layer only):\n    n_l+1 ~ Binomial(2 n_l, p), stopped at layer 10^4.\"\"\"\n    sizes = np.zeros(n_runs, dtype=np.int64)\n    durs = np.zeros(n_runs, dtype=np.int64)\n    profiles = []\n    for r in range(n_runs):\n        n, layer, prof = 1, 1, [1]\n        while n > 0 and layer < stop_layer:\n            n = rng.binomial(2 * n, p)\n            layer += 1\n            if n > 0:\n                prof.append(n)\n        sizes[r], durs[r] = sum(prof), len(prof)\n        profiles.append(np.array(prof))\n    return sizes, durs, profiles\n\n\ndef bethe_small_raster(n_runs: int, rng, p: float = 0.5, max_layer: int = 8):\n    \"\"\"Runs of the Bethe lattice, keeping those whose last active layer is <= max_layer.\n\n    Neuron j of layer l (1-based j) has index 2^(l-1) - 1 + (j - 1); a neuron's children in the\n    next layer are 2(j-1)+1 and 2(j-1)+2, as `bethelattice.m`. Returns the raster as a list of\n    1-based spike bins per neuron, the number of bins, and the small avalanches' sizes.\"\"\"\n    n_neurons = 2 ** max_layer - 1\n    spikes_t, spikes_n, sizes = [], [], []\n    t0 = 1\n    for r in range(n_runs):\n        active = np.array([0])          # 0-based position within the layer\n        rec = [(1, active)]\n        layer = 1\n        while active.size and layer <= max_layer:\n            hits = rng.random(2 * active.size) < p\n            idx = np.flatnonzero(hits)\n            active = 2 * active[idx // 2] + (idx % 2)\n            layer += 1\n            if active.size:\n                rec.append((layer, active))\n        if active.size:                 # still active beyond max_layer: not a small avalanche\n            continue\n        dur = len(rec)\n        for l, a in rec:\n            spikes_t.append(np.full(a.size, t0 + l - 1))\n            spikes_n.append(2 ** (l - 1) - 1 + a)\n        sizes.append(sum(a.size for _, a in rec))\n        t0 += dur + 1                   # one silent bin between runs\n    t = np.concatenate(spikes_t)\n    nn = np.concatenate(spikes_n)\n    raster = [np.sort(t[nn == j]) for j in range(n_neurons)]\n    return raster, int(t0 - 1), np.array(sizes)\n\n\n# ----------------------------------------------------------------------------------------------\n# Cortical branching model\n\ndef cb_simulate(p_trans: float, n_models: int, rng, t_steps: int = 3 * 10 ** 5,\n                side: int = 10, p_spont: float = 1e-4):\n    \"\"\"n_models independent cortical branching models run together; returns packed states\n    (t_steps x n_models x ceil(side^2 / 8) uint8). The first step is silent, as cbmodel.m.\"\"\"\n    n = side * side\n    probconv = np.zeros(5)\n    probconv[0] = p_spont\n    for j in range(4):\n        probconv[j + 1] = probconv[j] + p_trans - probconv[j] * p_trans\n    packed = np.zeros((t_steps, n_models, (n + 7) // 8), dtype=np.uint8)\n    state = np.zeros((n_models, side, side), dtype=bool)\n    for it in range(1, t_steps):\n        s = state.view(np.int8)\n        cnt = (np.roll(s, 1, 1) + np.roll(s, -1, 1) + np.roll(s, 1, 2) + np.roll(s, -1, 2))\n        state = rng.random((n_models, side, side)) < probconv[cnt]\n        packed[it] = np.packbits(state.reshape(n_models, n), axis=1)\n    return packed\n\n\ndef cb_raster(packed: np.ndarray, model: int, n: int = 100) -> np.ndarray:\n    \"\"\"(t_steps x n) bool states of one model.\"\"\"\n    return np.unpackbits(packed[:, model, :], axis=1, count=n).astype(bool)\n"
}
```

```
File created successfully at: entries/crcns-hc-8-timme-2016/models.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import time, numpy as np, models, hc8
for c in [0,0.8,1]:
    cur=models.chain_integration_curve(c); print('chain',c, np.round(cur[[1,5,11]],4), models.complexity_from_curve(cur))
rng=np.random.default_rng(0)
t=time.time(); r,nb,sz=models.bethe_small_raster(10000,rng); print('bethe small', len(sz), nb, sz.max(), time.time()-t)
t=time.time(); pk=models.cb_simulate(0.25, 30, rng, t_steps=30000); print('cb 3e4 steps', time.time()-t)
for p in [0.2,0.25,0.3]:
    pk=models.cb_simulate(p, 2, rng, t_steps=300000)
    R=models.cb_raster(pk,0); A=R.sum(1); s,d,st=hc8.avalanches(A); print(p,'nav',s.size,'active frac',(A>0).mean(),'max size',s.max(),'max dur',d.max(), 'mean A', A.mean())
EOF
```

```
chain 0 [0. 0. 0.] 0.0
chain 0.8 [0.1966 1.9476 5.841 ] 0.4312696772769103
chain 1 [ 1.  5. 11.] 0.0
bethe small 6951 26933 29 0.4509725570678711
cb 3e4 steps 2.1616246700286865
0.2 nav 2861 active frac 0.031106666666666668 max size 84 max dur 35 mean A 0.04693
0.25 nav 2773 active frac 0.058293333333333336 max size 444 max dur 72 mean A 0.14779
0.3 nav 1232 active frac 0.59468 max size 49334 max dur 2451 mean A 9.52906
```

**Agent calls Bash**

```bash
date -u; cd  sed -n '/"outcomes"/,/"findings"/p' schemas/attempt.schema.json | head -120 | grep -E '"(enum|required)"|"[a-z_]+": \{' | head -40; grep -n '"data"' -A6 schemas/claims.schema.json | head -20
```

```
Mon Nov  9 06:19:41 UTC 2026
  "properties": {
    "schema_version": {
    "id": {
    "dataset": {
      "required": [
      "properties": {
        "archive": {
        "id": {
        "version": {
        "modified": {
        "doi": {
      "if": {
        "properties": {
          "archive": {
      "then": {
        "properties": {
          "id": {
    "paper": {
    "date": {
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016 && source $TMPDIR/dev/bin/activate && python - <<'EOF'
p='hc8.py'; s=open(p).read()
old="""    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1],
               n_neurons=d["nNeurons"], n_silent=p["n_silent"], nbins_file=d["nbins"],"""
new="""    allt = np.concatenate(d["spikes"])
    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1],
               n_neurons=d["nNeurons"], n_trains=len(d["spikes"]), binsize=d["binsize"],
               recordingID=d["recordingID"], datatype=d["datatype"], expsys=d["expsys"],
               n_channel=len(d["channel"]), n_spikes=int(allt.size),
               n_beyond_nbins=int(np.sum(allt > d["nbins"])),
               n_dup_spikes=int(sum(np.sum(np.diff(s) == 0) for s in d["spikes"])),
               all_sorted=bool(all(np.all(np.diff(s) >= 0) for s in d["spikes"])),
               train_hash=hash(b"".join(s.tobytes() for s in d["spikes"])),
               n_silent=p["n_silent"], nbins_file=d["nbins"],"""
assert old in s; s=s.replace(old,new)
# randomization rng separate from measurement rng in both workers
old="""    for j, kind in enumerate(RANDOMIZATIONS):
        rng = np.random.default_rng([seed, i, 10 + j])
        rr = randomize(kind, p["raster"], p["nbins"], rng)"""
new="""    for j, kind in enumerate(RANDOMIZATIONS):
        rr = randomize(kind, p["raster"], p["nbins"], np.random.default_rng([seed, i, 10 + j]))
        rng = np.random.default_rng([seed, i, 20 + j])"""
assert old in s; s=s.replace(old,new)
old="""    for j, kind in enumerate(["real"] + RANDOMIZATIONS):
        rng = np.random.default_rng([seed, i, 100 + j])
        rr = p["raster"] if kind == "real" else randomize(kind, p["raster"], p["nbins"], rng)
        a2 = act if kind == "real" else activity(rr, p["nbins"])"""
new="""    for j, kind in enumerate(["real"] + RANDOMIZATIONS):
        rng = np.random.default_rng([seed, i, 100 + j])
        # the same randomized data as culture_record (same generator for the randomization)
        rr = p["raster"] if kind == "real" else randomize(
            kind, p["raster"], p["nbins"], np.random.default_rng([seed, i, 10 + j - 1]))
        a2 = act if kind == "real" else activity(rr, p["nbins"])
        if kind != "real":
            size, dur, starts = avalanches(a2)
            out[f"chi_a_{kind}"], out[f"chi_b_{kind}"] = susceptibility(a2, N)
            out[f"abs_curv_{kind}"] = abs(shape_collapse(mean_profiles(a2, size, dur, starts))[1])"""
assert old in s; s=s.replace(old,new)
old="""    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1], n_neurons=N,
               chi_a=crit["chi_a"], chi_b=crit["chi_b"], s_range=crit["s_range"],"""
new="""    out = dict(name=name, culture=culture_div(name)[0], div=culture_div(name)[1], n_neurons=N,
               chi_a=crit["chi_a"], chi_b=crit["chi_b"], abs_curv=crit["abs_curv"],
               s_range=crit["s_range"],"""
assert old in s; s=s.replace(old,new)
s=s.replace('train_hash=hash(b"".join(s.tobytes() for s in d["spikes"])),','train_hash=hashlib.md5(b"".join(s.tobytes() for s in d["spikes"])).hexdigest(),')
s=s.replace("import io\n","import hashlib\nimport io\n")
open(p,'w').write(s)
EOF
grep -n "RANDOMIZATIONS = " hc8.py
```

```
661:RANDOMIZATIONS = ["jitter1", "jitter10", "jitter100", "wrap", "poisson", "swap", "shuffle"]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb && cat > $TMPDIR/nb/common.py <<'EOF'
import nbformat as nbf
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    return c
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    return c
def save(cells, path):
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nbf.write(nb, path)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/build1.py",
 "content": "import sys\nsys.path.insert(0, sys.argv[1])\nfrom common import md, code, save\n\ncells = []\ncells.append(md(r\"\"\"\n# Timme et al. (2016) on CRCNS hc-8: avalanches, exponents, branching ratio and randomizations\n\nPaper: Timme, Marshall, Bennett, Ripp, Lautzenhiser & Beggs (2016), \"Criticality Maximizes\nComplexity in Neural Tissue\", Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425. The claims file\n`claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` was written from the version of record\n(PMC5037237) with its supplement, and checked by a second reader.\n\nDataset: CRCNS hc-8, doi:10.6080/K0PC308P, read from the public bucket\n`crcnsarchive/hc-8/live/Data.zip` (435 files `Data/CultureXDIVY.mat`). Version: CRCNS data sets\nare not versioned, so the version is `unversioned` (docs/archives.md). The zip read is the one\nwhose MD5 the data set's `checksums.md5` gives as `bd4e2a8685df3e55e1a3c04fbe09d9ce`; the data\ndescription is version 0.9 (Sept. 28, 2016). This is the only published copy (the bucket's\n`hc-8/orig/` holds a draft description, no data), and the paper names no version, so it is the\none pinned.\n\nThis notebook covers the culture claims that do not need the complexity. The complexity claims are\nin `complexity_culture.ipynb` and the model claims in `models.ipynb`. The measures port the NCC\nMATLAB toolbox the paper cites (see `hc8.py`).\n\n| claim | here |\n|---|---|\n| culture-counts | tested |\n| fig2d-network-isi | tested |\n| fig2e-avalanche-count | tested |\n| fig8-subsampling-exponents | tested |\n| fig8-exponents-match-literature | tested (with outside reference values) |\n| fig8-sigmanuz-methods-agree | tested |\n| eq4-exponent-relation | tested |\n| eq4-relation-randomized | tested |\n| fig9-branching-ratio | tested |\n| fig10b-susceptibility-randomization | tested |\n| fig10c-curvature-randomization | tested |\n| fig11ac-fit-range-randomization | tested |\n| fig11bd-exponents-randomization | tested |\n\"\"\"))\ncells.append(code(r\"\"\"\nimport os\nfor v in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ.setdefault(v, \"1\")\nimport time, resource, collections\nimport multiprocessing as mp\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport hc8\n\nSEED = 20161\n# HC8_SUBSET is used only while developing (a few recordings); the record runs all of them\nSUBSET = int(os.environ.get(\"HC8_SUBSET\", \"0\"))\nnames = hc8.recording_names()\nidx = list(range(len(names))) if not SUBSET else list(range(0, len(names), len(names) // SUBSET))[:SUBSET]\nt0 = time.time()\nwith mp.get_context(\"spawn\").Pool(4) as pool:\n    recs = list(pool.imap(hc8.culture_record, [(i, names[i], SEED) for i in idx], chunksize=1))\nprint(f\"{len(recs)} recordings analysed in {(time.time() - t0) / 60:.1f} min; \"\n      f\"peak memory of this process {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nbase = pd.DataFrame([{k: v for k, v in r.items() if k not in (\"measures\", \"rates\", \"slopes\")} for r in recs])\nKINDS = [\"real\"] + hc8.RANDOMIZATIONS\nmeas = {k: pd.DataFrame([r[\"measures\"][k] for r in recs], index=base.index) for k in KINDS}\nrates = np.concatenate([r[\"rates\"] for r in recs])\n\"\"\"))\ncells.append(md(r\"\"\"\n## Data check\n\nThe files hold one data stream, spike times per neuron, with no trial table or annotations, so\nthere is no second clock to align. The checks are of the description against the values.\n\"\"\"))\ncells.append(code(r\"\"\"\nprint(\"recordings:\", len(base), \"| cultures:\", base.culture.nunique(),\n      \"| recordings per culture: min\", base.groupby(\"culture\").size().min(), \"max\", base.groupby(\"culture\").size().max())\nprint(\"DIV range:\", base[\"div\"].min(), \"to\", base[\"div\"].max())\nprint(\"neurons (data.nNeurons): total\", base.n_neurons.sum(), \"| min\", base.n_neurons.min(),\n      \"max\", base.n_neurons.max(), \"mean\", round(base.n_neurons.mean(), 1))\nprint(\"length(data.spikes) == nNeurons in every file:\", bool((base.n_trains == base.n_neurons).all()))\nprint(\"data.binsize values (ms):\", sorted(base.binsize.unique()), \"| datatype:\", base.datatype.unique(),\n      \"| expsys:\", base.expsys.unique())\nprint(\"length(data.channel) == nNeurons:\", bool((base.n_channel == base.n_neurons).all()))\ndur_min = base.nbins_file * hc8.BIN_MS / 60e3\nprint(f\"data.nbins as minutes: {dur_min.min():.2f} to {dur_min.max():.2f} (description: about 1 hour)\")\nprint(f\"last spike time: {base.t_max_ms.min() / 60e3:.2f} to {base.t_max_ms.max() / 60e3:.2f} min\")\nprint(\"recordings with spike times beyond data.nbins:\", int((base.n_beyond_nbins > 0).sum()),\n      f\"({int(base.n_beyond_nbins.sum())} spikes)\")\nprint(\"every spike train sorted:\", bool(base.all_sorted.all()),\n      \"| recordings with repeated spike times within a neuron:\", int((base.n_dup_spikes > 0).sum()),\n      f\"({int(base.n_dup_spikes.sum())} repeats)\")\nprint(f\"shortest interval within a neuron: {base.min_isi_ms.min():.2f} ms \"\n      \"(wave_Clus 'ref' parameter is 30 samples, 1.5 ms; Methods 2.2 say the dead time was removed)\")\nprint(\"identical recordings (same spike trains):\", int(base.train_hash.duplicated().sum()),\n      \"| repeated recordingID:\", int(base.recordingID.duplicated().sum()))\nprint(\"neurons with no spike in the first 59 min (dropped):\", int(base.n_silent.sum()))\nprint(f\"firing rate over the first 59 min: {rates.min():.4f} to {rates.max():.2f} Hz, \"\n      f\"mean {rates.mean():.2f} Hz (description: average 1.9 Hz)\")\nprint(f\"mean network ISI: {base.isi_ms.min():.2f} to {base.isi_ms.max():.2f} ms; \"\n      f\"rebinning factor {base.factor.min()} to {base.factor.max()} bins of 0.05 ms\")\nprint(\"randomizations keep each neuron's spike count:\",\n      {k: bool(base[f\"{k}_counts_kept\"].all()) for k in hc8.RANDOMIZATIONS})\nprint(\"swap and shuffle leave A(t) unchanged:\",\n      bool(base.swap_act_identical.all()), bool(base.shuffle_act_identical.all()))\n\"\"\", tags=[\"sanity\"]))\ncells.append(code(r\"\"\"\n# Exclusion for too few avalanches (claims file, common detail 2). Reading (a): the size and the\n# duration distributions each keep at least one value after the cuts of Methods 2.7, and at least\n# two durations enter the shape collapse; reading (b): all recordings.\nr = meas[\"real\"]\nincl_a = (r.n_size_cut_values >= 1) & (r.n_dur_cut_values >= 1) & (r.n_profiles >= 2)\nfit_ok = r.tau.notna() & r.alpha.notna() & r.sgd.notna() & r.sc_exp.notna()\nprint(\"recordings kept under reading (a):\", int(incl_a.sum()), \"of\", len(r), \"| excluded:\", int((~incl_a).sum()))\nprint(\"recordings with every full-system fit available:\", int(fit_ok.sum()))\nprint(\"excluded recordings:\", list(base.name[~incl_a].str.replace(\"Data/\", \"\")))\nprint(\"avalanches in the excluded recordings:\", list(r.n_av[~incl_a]))\n\"\"\"))\n\n# culture-counts\ncells.append(md(r\"\"\"\n## culture-counts\n\n> The culture data hold 435 recordings and 39,529 spike-sorted neurons in total; most recordings\n> yield about 100 neurons, and firing rates range from roughly 0.05 to 20 Hz.\n\"\"\"))\ncells.append(code(r\"\"\"\nnn = base.n_neurons.values\nmode_nn, k_nn = hc8.terrell_scott_mode(nn)\nprint(\"number of recordings:\", len(base), \"(expected 435, tolerance 0)\")\nprint(\"total neurons:\", int(nn.sum()), \"(expected 39529, tolerance 0)\")\nprint(f\"neurons per recording: (a) median {np.median(nn):.0f}; (b) Terrell-Scott mode {mode_nn:.1f} \"\n      f\"({k_nn} bins); expected 100 +/- 10; range {nn.min()} to {nn.max()}\")\np5, p95 = np.percentile(rates, [5, 95])\nprint(f\"firing rates over {len(rates)} neurons: 5th percentile {p5:.3f} Hz, 95th {p95:.2f} Hz \"\n      f\"(criterion: within 0.045 to 22 Hz); min {rates.min():.4f}, max {rates.max():.2f}\")\npos = rates[rates > 0]\nprint(f\"orders of magnitude spanned by non-zero rates: {np.log10(pos.max() / pos.min()):.2f} \"\n      f\"(1st to 99th percentile: {np.log10(np.percentile(pos, 99) / np.percentile(pos, 1)):.2f})\")\nprint(\"fraction of neurons below 0.05 Hz:\", round(float(np.mean(rates < 0.05)), 3),\n      \"| above 20 Hz:\", round(float(np.mean(rates > 20)), 4))\nprint(\"\\nneurons per recording by culture (median):\")\nprint(base.groupby(\"culture\").n_neurons.median().astype(int).to_dict())\nfig, ax = plt.subplots(1, 2, figsize=(9, 3))\nax[0].hist(nn, bins=k_nn); ax[0].set_xlabel(\"neurons per recording\")\nax[1].hist(np.log10(pos), bins=50); ax[1].set_xlabel(\"log10 firing rate (Hz)\")\nplt.tight_layout(); plt.show()\n\"\"\", tags=[\"claim:culture-counts\"]))\n\n# fig2d\ncells.append(md(r\"\"\"\n## fig2d-network-isi\n\n> Most recordings have a mean network-wide interspike interval of around 7 ms, though some are\n> much higher or lower.\n\"\"\"))\ncells.append(code(r\"\"\"\nisi = base.isi_ms.values\nmode_isi, k_isi = hc8.terrell_scott_mode(isi)\nprint(f\"mean network ISI per recording: (a) median {np.median(isi):.2f} ms; (b) Terrell-Scott mode \"\n      f\"{mode_isi:.2f} ms ({k_isi} bins); expected 7 +/- 0.7 ms\")\nprint(f\"range {isi.min():.2f} to {isi.max():.2f} ms; 5th to 95th percentile \"\n      f\"{np.percentile(isi, 5):.2f} to {np.percentile(isi, 95):.2f} ms\")\nprint(\"by culture (median ms):\", base.groupby(\"culture\").isi_ms.median().round(1).to_dict())\nplt.figure(figsize=(4, 3)); plt.hist(isi, bins=k_isi); plt.xlabel(\"mean network ISI (ms)\"); plt.show()\n\"\"\", tags=[\"claim:fig2d-network-isi\"]))\n\n# fig2e\ncells.append(md(r\"\"\"\n## fig2e-avalanche-count\n\n> After rebinning to the network ISI, most recordings contain around 10,000 avalanches.\n\"\"\"))\ncells.append(code(r\"\"\"\nnav = meas[\"real\"].n_av.values\nmode_nav, k_nav = hc8.terrell_scott_mode(nav)\nprint(f\"avalanches per recording (first 59 min, rebinned to the network ISI): (a) median {np.median(nav):.0f}; \"\n      f\"(b) Terrell-Scott mode {mode_nav:.0f} ({k_nav} bins); expected 10000 +/- 1000\")\nprint(f\"range {nav.min()} to {nav.max()}; 5th to 95th percentile {np.percentile(nav, 5):.0f} to {np.percentile(nav, 95):.0f}\")\nprint(\"recordings with 9000 to 11000 avalanches:\", int(np.sum((nav >= 9000) & (nav <= 11000))))\nprint(\"by culture (median):\", meas[\"real\"].groupby(base.culture).n_av.median().astype(int).to_dict())\nplt.figure(figsize=(4, 3)); plt.hist(nav, bins=k_nav); plt.xlabel(\"avalanches per recording\"); plt.show()\n\"\"\"))\ncells[-1].metadata[\"tags\"] = [\"claim:fig2e-avalanche-count\"]\n\n# fig8\ncells.append(md(r\"\"\"\n## fig8-subsampling-exponents\n\n> In the culture recordings, sub-sampling extrapolation gives lower values of tau and alpha with\n> lower errors than the search algorithm on the full system, while 1/sigma nu z changes little\n> between the two.\n\nFull system: tau and alpha by the range search of `plparams.m` after the cuts, 1/sigma nu z from\nsize given duration over the fitted duration range and from the shape collapse. Sub-sampling\n(Methods 2.10): 30 random sub-samples at sizes evenly spaced from 40% to 100% of the neurons\n(layout reading a), MLE over all avalanches surviving the cuts, weighted least squares on 1/N with\nweight N, intercept kept. Each sub-sample is rebinned to its own network ISI (main reading,\nMethods 2.10: \"These analyses were identical to those performed in the whole recorded system\");\nkeeping the full system's bin is shown as a variant. Layout reading b (30 sub-samples at every\ninteger size) is run on four recordings below.\n\"\"\"))\ncells.append(code(r\"\"\"\ndef msd(x):\n    x = np.asarray(x, dtype=float); x = x[np.isfinite(x)]\n    return x.mean(), x.std(ddof=1), x.size\n\nsel = incl_a\nfull = {\"tau\": meas[\"real\"].tau[sel], \"alpha\": meas[\"real\"].alpha[sel],\n        \"sgd\": meas[\"real\"].sgd[sel], \"sc_exp\": meas[\"real\"].sc_exp[sel]}\nrows = []\nfor tag in (\"own\", \"fixed\"):\n    for k in (\"tau\", \"alpha\", \"sgd\", \"sc_exp\"):\n        fm, fs, fn = msd(full[k]); sm, ss, sn = msd(base[f\"ss_{tag}_{k}\"][sel])\n        rows.append(dict(rebinning=tag, exponent=k, full_mean=fm, full_sd=fs, full_n=fn,\n                         ss_mean=sm, ss_sd=ss, ss_n=sn, rel_change=(sm - fm) / fm))\nfig8 = pd.DataFrame(rows)\nprint(fig8.round(3).to_string())\nfor tag in (\"own\", \"fixed\"):\n    t = fig8[fig8.rebinning == tag].set_index(\"exponent\")\n    print(f\"\\n[{tag} bin] tau lower: {t.ss_mean['tau'] < t.full_mean['tau']}, tau SD lower: {t.ss_sd['tau'] < t.full_sd['tau']}; \"\n          f\"alpha lower: {t.ss_mean['alpha'] < t.full_mean['alpha']}, alpha SD lower: {t.ss_sd['alpha'] < t.full_sd['alpha']}; \"\n          f\"|change| sgd {abs(t.rel_change['sgd']):.3f}, shape collapse {abs(t.rel_change['sc_exp']):.3f} (criterion < 0.10)\")\nprint(\"\\nall recordings with finite values (exclusion reading b):\")\nfor k in (\"tau\", \"alpha\", \"sgd\", \"sc_exp\"):\n    print(k, \"full %.3f +/- %.3f (n=%d)\" % msd(meas[\"real\"][k]), \"| sub-sampled (own bin) %.3f +/- %.3f (n=%d)\" % msd(base[f\"ss_own_{k}\"]))\nprint(\"\\nfull-system fits: size p >= 0.2 found in\", int(meas[\"real\"].tau.notna().sum()), \"recordings; duration in\",\n      int(meas[\"real\"].alpha.notna().sum()))\nprint(\"full-system tau range %.3f to %.3f; sub-sampled (own bin) %.3f to %.3f\" % (\n    np.nanmin(full[\"tau\"]), np.nanmax(full[\"tau\"]), np.nanmin(base.ss_own_tau[sel]), np.nanmax(base.ss_own_tau[sel])))\nprint(\"\\nby culture, median tau full vs sub-sampled (own bin):\")\nprint(pd.DataFrame({\"full\": meas[\"real\"].tau[sel].groupby(base.culture[sel]).median(),\n                    \"ss\": base.ss_own_tau[sel].groupby(base.culture[sel]).median()}).round(2).T.to_string())\nfig, ax = plt.subplots(1, 4, figsize=(13, 3))\nfor a, k in zip(ax, (\"tau\", \"alpha\", \"sgd\", \"sc_exp\")):\n    a.hist(full[k].dropna(), bins=30, alpha=.6, label=\"full\"); a.hist(base[f\"ss_own_{k}\"][sel].dropna(), bins=30, alpha=.6, label=\"sub-sampled\")\n    a.set_xlabel(k)\nax[0].legend(); plt.tight_layout(); plt.show()\n\"\"\", tags=[\"claim:fig8-subsampling-exponents\"]))\ncells.append(code(r\"\"\"\n# Layout reading (b): 30 random sub-samples at every integer size from 40% to 100%, on four\n# recordings drawn with a fixed seed among those kept; compared with layout (a) on the same ones.\nrng_b = np.random.default_rng([SEED, 8])\npick = rng_b.choice(np.flatnonzero(sel.values), size=min(4, int(sel.sum())), replace=False)\n\ndef layout_b(i):\n    d = hc8.load(names[idx[i]]); p = hc8.prepare(d)\n    sizes = hc8.subsample_sizes(len(p[\"spikes\"]), layout=\"all\")\n    return hc8.subsample_exponents(p[\"spikes\"], np.random.default_rng([SEED, idx[i], 9]), True, p[\"factor\"], sizes)\n\nt1 = time.time()\nlb = pd.DataFrame([layout_b(i) for i in pick], index=base.name.iloc[pick].str.replace(\"Data/\", \"\"))\nla = base.iloc[pick][[f\"ss_own_{k}\" for k in (\"tau\", \"alpha\", \"sgd\", \"sc_exp\")]].set_axis(lb.index)\nprint(f\"layout (b) on {len(pick)} recordings, {(time.time() - t1) / 60:.1f} min\")\nprint(pd.concat({\"layout a\": la.set_axis([\"tau\", \"alpha\", \"sgd\", \"sc_exp\"], axis=1), \"layout b\": lb}, axis=1).round(3).to_string())\nprint(\"full-system values of the same recordings:\")\nprint(meas[\"real\"].iloc[pick][[\"tau\", \"alpha\", \"sgd\", \"sc_exp\"]].set_axis(lb.index).round(3).to_string())\n\"\"\", tags=[\"claim:fig8-subsampling-exponents\"]))\n\n# fig8 literature\ncells.append(md(r\"\"\"\n## fig8-exponents-match-literature\n\n> The culture critical exponents from the sub-sampling method agree better with previously reported\n> values for neural avalanches (Mazzoni et al. 2007, Pasquale et al. 2008, Friedman et al. 2012)\n> than those from the search algorithm on the full system.\n\nThe reference values come from the three cited papers (inputs of the attempt record); they are\nset in the next cell with their sources.\n\"\"\"))\ncells.append(code(r\"\"\"\n# REFERENCE VALUES (outside inputs; see the attempt record's `inputs`)\nREFS = {}\n\"\"\", tags=[\"claim:fig8-exponents-match-literature\"]))\ncells.append(code(r\"\"\"\nt_own = fig8[fig8.rebinning == \"own\"].set_index(\"exponent\")\nrows = []\nfor paper, vals in REFS.items():\n    for k, v in vals.items():\n        rows.append(dict(paper=paper, exponent=k, reference=v, full_mean=t_own.full_mean[k], ss_mean=t_own.ss_mean[k],\n                         d_full=abs(t_own.full_mean[k] - v), d_ss=abs(t_own.ss_mean[k] - v)))\nlit = pd.DataFrame(rows)\nif len(lit):\n    lit[\"ss_closer\"] = lit.d_ss < lit.d_full\n    print(lit.round(3).to_string())\n    for k in (\"tau\", \"alpha\"):\n        s = lit[lit.exponent == k]\n        print(f\"{k}: sub-sampling closer for {int(s.ss_closer.sum())} of {len(s)} cited papers that report it\")\nelse:\n    print(\"no reference values\")\n\"\"\", tags=[\"claim:fig8-exponents-match-literature\"]))\n\n# sigmanuz agree\ncells.append(md(r\"\"\"\n## fig8-sigmanuz-methods-agree\n\n> The values of 1/sigma nu z from the size given duration fits and from the shape collapse agree\n> within error.\n\"\"\"))\ncells.append(code(r\"\"\"\nfor tag in (\"own\", \"fixed\"):\n    t = fig8[fig8.rebinning == tag].set_index(\"exponent\")\n    for which, m, s in ((\"full system\", \"full_mean\", \"full_sd\"), (\"sub-sampling\", \"ss_mean\", \"ss_sd\")):\n        if which == \"full system\" and tag == \"fixed\":\n            continue\n        diff = abs(t[m][\"sgd\"] - t[m][\"sc_exp\"]); bound = max(t[s][\"sgd\"], t[s][\"sc_exp\"])\n        print(f\"{which} ({tag} bin): size given duration {t[m]['sgd']:.3f} +/- {t[s]['sgd']:.3f}, shape collapse \"\n              f\"{t[m]['sc_exp']:.3f} +/- {t[s]['sc_exp']:.3f}; |difference| {diff:.3f} vs larger SD {bound:.3f}: agree {diff < bound}\")\nd = (meas[\"real\"].sgd - meas[\"real\"].sc_exp)[sel]\nprint(f\"per recording (full system): median difference {d.median():.3f}, |difference| < 0.1 in {float((d.abs() < 0.1).mean()):.2f} of recordings\")\n\"\"\", tags=[\"claim:fig8-sigmanuz-methods-agree\"]))\n\n# eq4\ncells.append(md(r\"\"\"\n## eq4-exponent-relation\n\n> The culture critical exponents satisfy the relation (alpha - 1)/(tau - 1) = 1/sigma nu z (Eq. 4)\n> with both the search algorithm and the sub-sampling method.\n\"\"\"))\ncells.append(code(r\"\"\"\ndef relation(tm, ts, am, as_):\n    f = (am - 1) / (tm - 1)\n    sf = np.sqrt((as_ / (tm - 1)) ** 2 + ((am - 1) * ts / (tm - 1) ** 2) ** 2)\n    return f, sf\n\ndef eq4_table(tbl, m, s):\n    f, sf = relation(tbl[m][\"tau\"], tbl[s][\"tau\"], tbl[m][\"alpha\"], tbl[s][\"alpha\"])\n    out = {\"ratio\": f, \"sd\": sf, \"sgd\": tbl[m][\"sgd\"], \"sc\": tbl[m][\"sc_exp\"],\n           \"holds_sgd\": abs(f - tbl[m][\"sgd\"]) <= sf, \"holds_sc\": abs(f - tbl[m][\"sc_exp\"]) <= sf}\n    out[\"holds\"] = out[\"holds_sgd\"] or out[\"holds_sc\"]\n    return out\n\nfor tag in (\"own\", \"fixed\"):\n    t = fig8[fig8.rebinning == tag].set_index(\"exponent\")\n    for which, m, s in ((\"search algorithm (full)\", \"full_mean\", \"full_sd\"), (\"sub-sampling\", \"ss_mean\", \"ss_sd\")):\n        if which.startswith(\"search\") and tag == \"fixed\":\n            continue\n        e = eq4_table(t, m, s)\n        print(f\"{which} [{tag} bin]: (alpha-1)/(tau-1) = {e['ratio']:.3f} +/- {e['sd']:.3f}; 1/sigma nu z sgd {e['sgd']:.3f}, \"\n              f\"shape collapse {e['sc']:.3f}; within one SD: sgd {e['holds_sgd']}, shape collapse {e['holds_sc']}\")\nrr = meas[\"real\"][sel]\npr = (rr.alpha - 1) / (rr.tau - 1)\nprint(f\"\\nper recording, full system: median (alpha-1)/(tau-1) {pr.median():.3f}, median sgd {rr.sgd.median():.3f}; \"\n      f\"|ratio - sgd| < 0.1 in {float(((pr - rr.sgd).abs() < 0.1).mean()):.2f} of recordings, < 0.2 in {float(((pr - rr.sgd).abs() < 0.2).mean()):.2f}\")\nfor tag in (\"own\",):\n    ps = (base[f\"ss_{tag}_alpha\"] - 1) / (base[f\"ss_{tag}_tau\"] - 1)\n    print(f\"per recording, sub-sampling: median ratio {ps[sel].median():.3f}, median sgd {base[f'ss_{tag}_sgd'][sel].median():.3f}\")\n\"\"\", tags=[\"claim:eq4-exponent-relation\"]))\n\n# eq4 randomized\ncells.append(md(r\"\"\"\n## eq4-relation-randomized\n\n> Randomized culture data also satisfy the critical exponent relation, with different exponent values.\n\nFull-system exponents of each randomization that changes the avalanches (swap and shuffling keep\nA(t), so their exponents equal the real data's and cannot differ).\n\"\"\"))\ncells.append(code(r\"\"\"\nreal_m = meas[\"real\"][sel]\nrows = []\nfor k in [\"jitter1\", \"jitter10\", \"jitter100\", \"wrap\", \"poisson\"]:\n    m_ = meas[k][sel]\n    tm, ts, _ = msd(m_.tau); am, as_, _ = msd(m_.alpha); gm, gs, _ = msd(m_.sgd); cm, cs_, _ = msd(m_.sc_exp)\n    f, sf = relation(tm, ts, am, as_)\n    holds = (abs(f - gm) <= sf) or (abs(f - cm) <= sf)\n    dt = abs(tm - real_m.tau.mean()) > real_m.tau.std(ddof=1)\n    da = abs(am - real_m.alpha.mean()) > real_m.alpha.std(ddof=1)\n    rows.append(dict(method=k, tau=tm, tau_sd=ts, alpha=am, alpha_sd=as_, ratio=f, ratio_sd=sf, sgd=gm, sc=cm,\n                     relation_holds=holds, tau_differs=dt, alpha_differs=da))\neqr = pd.DataFrame(rows)\nprint(eqr.round(3).to_string())\nprint(f\"\\nreal data: tau {real_m.tau.mean():.3f} +/- {real_m.tau.std(ddof=1):.3f}, alpha {real_m.alpha.mean():.3f} +/- {real_m.alpha.std(ddof=1):.3f}\")\nok = eqr[eqr.relation_holds & (eqr.tau_differs | eqr.alpha_differs)]\nprint(\"methods where the relation holds and tau or alpha differs by more than one SD:\", list(ok.method))\n\"\"\", tags=[\"claim:eq4-relation-randomized\"]))\n\n# fig9\ncells.append(md(r\"\"\"\n## fig9-branching-ratio\n\n> With the sub-sampling-corrected method, most culture recordings have branching ratios slightly\n> below 1, while the basic method gives ratios substantially below 1 and more varied.\n\"\"\"))\ncells.append(code(r\"\"\"\nbn, bb = base.B_new.values, base.B_basic.values\nprint(f\"B_new: median {np.nanmedian(bn):.3f}, mean {np.nanmean(bn):.3f}, SD {np.nanstd(bn, ddof=1):.3f}, range {np.nanmin(bn):.3f} to {np.nanmax(bn):.3f}, \"\n      f\"failed fits {int(np.isnan(bn).sum())}\")\nprint(f\"B_basic (Eq. 11): median {np.median(bb):.3f}, mean {bb.mean():.3f}, SD {bb.std(ddof=1):.3f}, range {bb.min():.3f} to {bb.max():.3f}\")\nfor w in (0.05, 0.1):\n    in_band = np.mean((bn >= 1 - w) & (bn < 1)); below = np.mean(bb < 1 - w)\n    print(f\"reading band {w}: B_new in [{1 - w}, 1) for {in_band:.3f} of recordings; B_basic below {1 - w} for {below:.3f}; \"\n          f\"SD B_basic > SD B_new: {np.std(bb, ddof=1) > np.nanstd(bn, ddof=1)}\")\nprint(\"B_new >= 1 in\", int(np.sum(bn >= 1)), \"recordings\")\nprint(f\"variants: brsimple (slope of A(t+1) on A(t), A(t) <= 10) median {base.B_simple.median():.3f}, SD {base.B_simple.std():.3f}; \"\n      f\"avprops per-avalanche ratio median {base.B_avalanche.median():.3f}, SD {base.B_avalanche.std():.3f}\")\nprint(\"\\nby culture, fraction of recordings with B_new in [0.9, 1):\")\nprint(base.assign(b=(bn >= 0.9) & (bn < 1)).groupby(\"culture\").b.mean().round(2).to_dict())\nfig, ax = plt.subplots(figsize=(4, 3)); ax.hist(bb, bins=40, alpha=.6, label=\"basic\"); ax.hist(bn[np.isfinite(bn)], bins=40, alpha=.6, label=\"new\")\nax.legend(); ax.set_xlabel(\"branching ratio\"); plt.show()\n\"\"\", tags=[\"claim:fig9-branching-ratio\"]))\n\n# randomization tests\ncells.append(md(r\"\"\"\n## Randomization tests (Figures 10B, 10C and 11)\n\nThe Figure 10 and 11 legends give a rank sum test of the real data against each randomization\nacross recordings, with false discovery rate control. Readings of the correction (claims file,\ncommon detail 3): Benjamini-Hochberg (BH) or Benjamini-Yekutieli (BY), over the seven comparisons\nof one panel; the family of all panels of the figure is shown as a variant. Recordings kept under\nexclusion reading (a); reading (b), all recordings with finite values, is shown too.\n\"\"\"))\ncells.append(code(r\"\"\"\ndef panel(col, kinds=hc8.RANDOMIZATIONS, rows=sel):\n    out = []\n    x = meas[\"real\"][col][rows].dropna()\n    for k in kinds:\n        y = meas[k][col][rows].dropna()\n        p = stats.mannwhitneyu(x, y, alternative=\"two-sided\").pvalue\n        out.append(dict(randomization=k, real_median=x.median(), rand_median=y.median(),\n                        change=y.median() - x.median(), p=p, n_real=len(x), n_rand=len(y)))\n    t = pd.DataFrame(out).set_index(\"randomization\")\n    t[\"p_bh\"] = hc8.fdr(t.p.values, \"bh\"); t[\"p_by\"] = hc8.fdr(t.p.values, \"by\")\n    return t\n\npanels = {}\nfor col in (\"chi_a\", \"chi_b\", \"abs_curv\", \"curv\", \"s_range\", \"d_range\", \"tau\", \"alpha\"):\n    panels[col] = panel(col)\nfam11 = pd.concat([panels[c] for c in (\"s_range\", \"tau\", \"d_range\", \"alpha\")], keys=[\"s_range\", \"tau\", \"d_range\", \"alpha\"])\nfam11[\"p_bh_fig\"] = hc8.fdr(fam11.p.values, \"bh\"); fam11[\"p_by_fig\"] = hc8.fdr(fam11.p.values, \"by\")\npanels_b = {col: panel(col, rows=slice(None)) for col in (\"chi_a\", \"chi_b\", \"abs_curv\", \"s_range\", \"d_range\", \"tau\", \"alpha\")}\nFIVE = [\"jitter1\", \"jitter10\", \"jitter100\", \"wrap\", \"poisson\"]\n\"\"\"))\n\ncells.append(md(r\"\"\"\n## fig10b-susceptibility-randomization\n\n> Culture susceptibility decreases under randomization, most under the strongest forms such as\n> Poisson randomization.\n\"\"\"))\ncells.append(code(r\"\"\"\nfor col, lab in ((\"chi_a\", \"reading (a) Eq. 14 var(A/N)\"), (\"chi_b\", \"reading (b) N var(A/N)\")):\n    t = panels[col]\n    print(lab); print(t.to_string(float_format=lambda v: f\"{v:.3g}\"))\n    five = t.loc[FIVE]\n    dec = five.change.sort_values()\n    for c in (\"p_bh\", \"p_by\"):\n        ok = bool(((five.change < 0) & (five[c] < 0.05)).all())\n        print(f\"  {c}: all five lower with corrected p < 0.05: {ok}\")\n    print(\"  largest decreases (median):\", list(dec.index[:2]), \"| Poisson among the two largest:\", \"poisson\" in list(dec.index[:2]))\n    print(\"  relative median change:\", (five.change / five.real_median).round(3).to_dict())\n    print(\"  exclusion reading (b):\", {k: (round(v.change, 6), f\"{v.p_bh:.2g}\") for k, v in panels_b[col].loc[FIVE].iterrows()})\nprint(\"\\nper culture, fraction of recordings with lower chi (reading b) under Poisson:\",\n      (meas[\"poisson\"].chi_b < meas[\"real\"].chi_b)[sel].groupby(base.culture[sel]).mean().round(2).to_dict())\n\"\"\", tags=[\"claim:fig10b-susceptibility-randomization\"]))\n\ncells.append(md(r\"\"\"\n## fig10c-curvature-randomization\n\n> The culture shape collapse curvature decreases under randomization, so the collapsed avalanches\n> become flatter.\n\"\"\"))\ncells.append(code(r\"\"\"\nt = panels[\"abs_curv\"]\nprint(\"absolute curvature (claims file, common detail 6)\"); print(t.to_string(float_format=lambda v: f\"{v:.3g}\"))\nfive = t.loc[FIVE]\nfor c in (\"p_bh\", \"p_by\"):\n    print(f\"{c}: all five lower with corrected p < 0.05: {bool(((five.change < 0) & (five[c] < 0.05)).all())}; \"\n          f\"lower and significant: {list(five.index[(five.change < 0) & (five[c] < 0.05)])}\")\nprint(\"exclusion reading (b):\", {k: (round(v.change, 4), f\"{v.p_bh:.2g}\") for k, v in panels_b[\"abs_curv\"].loc[FIVE].iterrows()})\nprint(\"\\nvariant, signed curvature (toolbox output):\"); print(panels[\"curv\"].loc[FIVE].to_string(float_format=lambda v: f\"{v:.3g}\"))\nprint(f\"real data: signed curvature negative (arched) in {float((meas['real'].curv[sel] < 0).mean()):.2f} of recordings; \"\n      f\"range {meas['real'].curv[sel].min():.3f} to {meas['real'].curv[sel].max():.3f}\")\nprint(\"\\nper culture, fraction of recordings with lower |curvature| under Poisson:\",\n      (meas[\"poisson\"].abs_curv < meas[\"real\"].abs_curv)[sel].groupby(base.culture[sel]).mean().round(2).to_dict())\n\"\"\", tags=[\"claim:fig10c-curvature-randomization\"]))\n\ncells.append(code(r\"\"\"\n# Whole-figure family for Figure 10 panels B and C (panel A, complexity, is in complexity_culture.ipynb,\n# which computes the family of all three panels)\nfam10 = pd.concat([panels[\"chi_a\"], panels[\"abs_curv\"]], keys=[\"chi_a\", \"abs_curv\"])\nfam10[\"p_bh_fig\"] = hc8.fdr(fam10.p.values, \"bh\"); fam10[\"p_by_fig\"] = hc8.fdr(fam10.p.values, \"by\")\nprint(fam10.loc[(slice(None), FIVE), [\"change\", \"p\", \"p_bh_fig\", \"p_by_fig\"]].to_string(float_format=lambda v: f\"{v:.3g}\"))\n\"\"\", tags=[\"claim:fig10b-susceptibility-randomization\", \"claim:fig10c-curvature-randomization\"]))\n\ncells.append(md(r\"\"\"\n## fig11ac-fit-range-randomization\n\n> The size and duration power-law fit ranges decrease under strong randomization such as Poisson\n> randomization, but increase slightly under 10-bin jittering.\n\"\"\"))\ncells.append(code(r\"\"\"\nfor col in (\"s_range\", \"d_range\"):\n    t = panels[col]\n    print(col, \"(decades, log10 xmax/xmin)\"); print(t.to_string(float_format=lambda v: f\"{v:.3g}\"))\n    print(f\"  Poisson lower: {t.change['poisson'] < 0}, p_bh {t.p_bh['poisson']:.3g}, p_by {t.p_by['poisson']:.3g}; \"\n          f\"10-bin jitter higher median: {t.change['jitter10'] > 0} (change {t.change['jitter10']:.4f}, p_bh {t.p_bh['jitter10']:.3g})\")\n    print(\"  means real vs jitter10:\", round(meas['real'][col][sel].mean(), 4), round(meas['jitter10'][col][sel].mean(), 4))\n    print(\"  whole-figure family:\", fam11.loc[col].loc[FIVE, [\"change\", \"p_bh_fig\", \"p_by_fig\"]].round(4).to_dict(\"index\"))\nprint(\"\\nper culture, fraction of recordings with a shorter size fit range under Poisson:\",\n      (meas[\"poisson\"].s_range < meas[\"real\"].s_range)[sel].groupby(base.culture[sel]).mean().round(2).to_dict())\n\"\"\", tags=[\"claim:fig11ac-fit-range-randomization\"]))\n\ncells.append(md(r\"\"\"\n## fig11bd-exponents-randomization\n\n> The size and duration power-law exponents increase under randomization, as randomization removes\n> large or long avalanches and steepens the distributions.\n\"\"\"))\ncells.append(code(r\"\"\"\nfor col in (\"tau\", \"alpha\"):\n    t = panels[col]\n    print(col); print(t.to_string(float_format=lambda v: f\"{v:.3g}\"))\n    five = t.loc[FIVE]\n    for c in (\"p_bh\", \"p_by\"):\n        up = list(five.index[(five.change > 0) & (five[c] < 0.05)])\n        print(f\"  {c}: higher with corrected p < 0.05 for {len(up)} of 5: {up}\")\n    print(\"  whole-figure family BH:\", fam11.loc[col].loc[FIVE, \"p_bh_fig\"].round(4).to_dict())\nfor k in FIVE:\n    m_ = meas[k][sel]\n    print(f\"{k}: median largest size kept by the cuts' fit xmax {m_.s_xmax.median():.0f} vs real {meas['real'].s_xmax[sel].median():.0f}; \"\n          f\"avalanches {m_.n_av.median():.0f} vs {meas['real'].n_av[sel].median():.0f}\")\nprint(\"\\nper culture, fraction of recordings with higher tau under Poisson:\",\n      (meas[\"poisson\"].tau > meas[\"real\"].tau)[sel].groupby(base.culture[sel]).mean().round(2).to_dict())\n\"\"\", tags=[\"claim:fig11bd-exponents-randomization\"]))\n\ncells.append(md(r\"\"\"\n## Summary\n\"\"\"))\n\nsave(cells, sys.argv[2])\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/build1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python $TMPDIR/nb/build1.py $TMPDIR/nb culture_criticality.ipynb && cat > $TMPDIR/nb/run.py <<'EOF'
import sys, time, nbformat
from nbclient import NotebookClient
nb = nbformat.read(sys.argv[1], as_version=4)
t=time.time()
try:
    NotebookClient(nb, timeout=3600, kernel_name="python3", resources={"metadata": {"path": "."}}).execute()
finally:
    nbformat.write(nb, sys.argv[2])
    print("time", time.time()-t)
EOF
date -u; HC8_SUBSET=8 python $TMPDIR/nb/run.py culture_criticality.ipynb $TMPDIR/nb/out1.ipynb 2>&1 | tail -20
```

```
Mon Nov  9 06:22:19 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
time 2815.3541922569275
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/nb/out1.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or (o.get('data',{}).get('text/plain') if 'data' in o else None) or ''.join(o.get('traceback',[]))[-1500:]
        if t: print('---', c.metadata.get('tags'), '\n', str(t)[:1800])
EOF
```

```
Mon Nov  9 07:09:24 UTC 2026
--- None 
 8 recordings analysed in 1.8 min; peak memory of this process 0.21 GB

--- ['sanity'] 
 recordings: 8 | cultures: 8 | recordings per culture: min 1 max 1
DIV range: 6 to 28
neurons (data.nNeurons): total 714 | min 65 max 109 mean 89.2
length(data.spikes) == nNeurons in every file: True
data.binsize values (ms): [np.float64(0.05)] | datatype: <StringArray>
['Spikes']
Length: 1, dtype: str | expsys: <StringArray>
['Rat Hippocampal Dissociated Cultures']
Length: 1, dtype: str
length(data.channel) == nNeurons: True
data.nbins as minutes: 59.64 to 61.67 (description: about 1 hour)
last spike time: 59.64 to 61.67 min
recordings with spike times beyond data.nbins: 0 (0 spikes)
every spike train sorted: True | recordings with repeated spike times within a neuron: 0 (0 repeats)
shortest interval within a neuron: 0.10 ms (wave_Clus 'ref' parameter is 30 samples, 1.5 ms; Methods 2.2 say the dead time was removed)
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 20 "https://export.arxiv.org/api/query?search_query=ti:%22Universal%20critical%20dynamics%20in%20high%20resolution%20neuronal%20avalanche%22&max_results=3" | grep -E "<id>|<summary>" -A6 | head -30
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/build2.py",
 "content": "import sys\nsys.path.insert(0, sys.argv[1])\nfrom common import md, code, save\n\ncells = []\ncells.append(md(r\"\"\"\n# Timme et al. (2016) on CRCNS hc-8: complexity of the culture recordings\n\nPaper: Timme et al. (2016), Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425; claims file\n`claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` (version of record, PMC5037237, with the\nsupplement). Dataset: CRCNS hc-8, doi:10.6080/K0PC308P, `hc-8/live/Data.zip` (MD5\n`bd4e2a8685df3e55e1a3c04fbe09d9ce` in the data set's `checksums.md5`), version `unversioned`: CRCNS\ndata sets carry no versions and this is the only published copy (see `culture_criticality.ipynb`).\n\nComplexity (Methods 2.9, `complexity.m` of the NCC toolbox): on the avalanche bins of the rebinned\nfirst 59 min, with the sub-sampling correction (the integration curve of data whose neurons are\neach permuted in time is subtracted, and the curve is cut at the first peak of I(k)/(k-1)). The\npaper uses up to 100 random subsets per subset size; this notebook uses 10, to fit the time limit\n(435 recordings x 8 conditions). Two variants are shown: the corrected curve without the cut, and\nno correction. The randomized data are the same as in `culture_criticality.ipynb` (same\ngenerators).\n\n| claim | here |\n|---|---|\n| fig10a-complexity-randomization | tested |\n| figs8-complexity-susceptibility-correlation | tested |\n| figs9-complexity-fit-range-correlation | tested |\n| fig12a-swap-preserves-complexity | tested |\n| fig12b-shuffle-lowers-complexity | tested |\n\"\"\"))\ncells.append(code(r\"\"\"\nimport os\nfor v in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ.setdefault(v, \"1\")\nimport time, resource\nimport multiprocessing as mp\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport hc8\n\nSEED = 20161          # the same seed as culture_criticality.ipynb, so the randomized data are the same\nN_SUBSETS = 10        # Methods 2.9 give up to 100; 10 to fit the time limit (a deviation)\nSUBSET = int(os.environ.get(\"HC8_SUBSET\", \"0\"))   # only while developing\nnames = hc8.recording_names()\nidx = list(range(len(names))) if not SUBSET else list(range(0, len(names), len(names) // SUBSET))[:SUBSET]\nt0 = time.time()\nwith mp.get_context(\"spawn\").Pool(4) as pool:\n    recs = list(pool.imap(hc8.complexity_record, [(i, names[i], SEED, N_SUBSETS) for i in idx], chunksize=1))\ncx = pd.DataFrame(recs)\nprint(f\"{len(cx)} recordings in {(time.time() - t0) / 60:.1f} min; peak memory of this process \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nKINDS = [\"real\"] + hc8.RANDOMIZATIONS\n\"\"\"))\ncells.append(code(r\"\"\"\nprint(\"recordings:\", len(cx), \"| cultures:\", cx.culture.nunique(), \"| neurons analysed:\", int(cx.n_neurons.sum()))\nprint(\"avalanche bins per recording (real): %d to %d\" % (cx.nbins_real.min(), cx.nbins_real.max()))\nfor k in KINDS:\n    c = cx[f\"C_{k}\"]\n    print(f\"{k:10s} complexity (bits/neuron) median {c.median():.5f}, range {c.min():.5f} to {c.max():.5f}; \"\n          f\"subset sizes kept by the cut: median {cx[f'kkept_{k}'].median():.0f} of {cx[f'N_{k}'].median():.0f}; \"\n          f\"NaN {int(c.isna().sum())}\")\nprint(\"neurons left without a spike by shuffling (dropped):\", int((cx.N_shuffle < cx.n_neurons).sum()), \"recordings\")\nincl_a = (cx.n_size_cut_values >= 1) & (cx.n_dur_cut_values >= 1) & (cx.n_profiles >= 2)\nprint(\"recordings kept under exclusion reading (a):\", int(incl_a.sum()), \"of\", len(cx))\n\"\"\", tags=[\"sanity\"]))\n\ncells.append(md(r\"\"\"\n## fig10a-complexity-randomization\n\n> Culture complexity decreases under randomization, most under the strongest forms such as Poisson\n> randomization, with the exception of spike swapping.\n\nRank sum test of the real data against each randomization across recordings, false discovery rate\nover the seven comparisons of the panel, Benjamini-Hochberg (BH) or Benjamini-Yekutieli (BY)\n(claims file, common detail 3); the family of all three panels of Figure 10 is a variant.\n\"\"\"))\ncells.append(code(r\"\"\"\ndef panel(prefix, rows=incl_a, kinds=hc8.RANDOMIZATIONS, real_col=None):\n    out = []\n    x = cx[real_col or f\"{prefix}_real\"][rows].dropna()\n    for k in kinds:\n        y = cx[f\"{prefix}_{k}\"][rows].dropna()\n        p = stats.mannwhitneyu(x, y, alternative=\"two-sided\").pvalue\n        out.append(dict(randomization=k, real_median=x.median(), rand_median=y.median(),\n                        change=y.median() - x.median(), rel_change=(y.median() - x.median()) / x.median(), p=p))\n    t = pd.DataFrame(out).set_index(\"randomization\")\n    t[\"p_bh\"] = hc8.fdr(t.p.values, \"bh\"); t[\"p_by\"] = hc8.fdr(t.p.values, \"by\")\n    return t\n\nfmt = lambda v: f\"{v:.3g}\"\nNOT_SWAP = [\"jitter1\", \"jitter10\", \"jitter100\", \"wrap\", \"poisson\", \"shuffle\"]\nfor prefix, lab in ((\"C\", \"complexity.m (correction and cut)\"), (\"Cuncut\", \"variant: correction, no cut\"), (\"Craw\", \"variant: no correction\")):\n    t = panel(prefix)\n    print(lab); print(t.to_string(float_format=fmt))\n    sub = t.loc[NOT_SWAP]\n    dec = sub.change.sort_values()\n    for c in (\"p_bh\", \"p_by\"):\n        ok = list(sub.index[(sub.change < 0) & (sub[c] < 0.05)])\n        print(f\"  {c}: lower with corrected p < 0.05 for {len(ok)} of 6 non-swap randomizations: {ok}\")\n    print(\"  two largest median decreases:\", list(dec.index[:2]), \"| Poisson among them:\", \"poisson\" in list(dec.index[:2]), \"\\n\")\n    if prefix == \"C\":\n        t10a = t\nfam = pd.concat([t10a, panel(\"chi_a\", real_col=\"chi_a\"), panel(\"abs_curv\", real_col=\"abs_curv\")], keys=[\"C\", \"chi_a\", \"abs_curv\"])\nfam[\"p_bh_fig\"] = hc8.fdr(fam.p.values, \"bh\"); fam[\"p_by_fig\"] = hc8.fdr(fam.p.values, \"by\")\nprint(\"whole-figure family (Figure 10 A to C), complexity rows:\")\nprint(fam.loc[\"C\", [\"change\", \"p\", \"p_bh_fig\", \"p_by_fig\"]].to_string(float_format=fmt))\nprint(\"\\nall recordings (exclusion reading b):\")\nprint(panel(\"C\", rows=slice(None))[[\"change\", \"p_bh\", \"p_by\"]].to_string(float_format=fmt))\nprint(\"\\nper culture, fraction of recordings with lower complexity under Poisson:\",\n      (cx.C_poisson < cx.C_real)[incl_a].groupby(cx.culture[incl_a]).mean().round(2).to_dict())\nfig, ax = plt.subplots(figsize=(7, 3))\nax.boxplot([cx[f\"C_{k}\"][incl_a].dropna() for k in KINDS], labels=KINDS, whis=(0, 100)); ax.set_yscale(\"symlog\", linthresh=1e-4)\nax.set_ylabel(\"complexity (bits/neuron)\"); plt.xticks(rotation=30); plt.tight_layout(); plt.show()\nprint(\"plotted range: %.5f to %.5f\" % (min(cx[f'C_{k}'].min() for k in KINDS), max(cx[f'C_{k}'].max() for k in KINDS)))\n\"\"\", tags=[\"claim:fig10a-complexity-randomization\"]))\n\ncells.append(md(r\"\"\"\n## figs8-complexity-susceptibility-correlation\n\n> Across culture recordings, complexity and susceptibility are positively correlated (correlation 0.23).\n\"\"\"))\ncells.append(code(r\"\"\"\nr_ = cx[incl_a]\nfor col, lab in ((\"chi_a\", \"susceptibility reading (a) var(A/N)\"), (\"chi_b\", \"reading (b) N var(A/N)\")):\n    for cc, clab in ((\"C_real\", \"complexity.m\"), (\"Cuncut_real\", \"variant no cut\"), (\"Craw_real\", \"variant no correction\")):\n        ok = r_[[cc, col]].dropna()\n        pr = stats.pearsonr(ok[cc], ok[col]); sr = stats.spearmanr(ok[cc], ok[col])\n        print(f\"{lab}, {clab}: Pearson r = {pr.statistic:.3f} (p = {pr.pvalue:.2g}), Spearman {sr.statistic:.3f}, n = {len(ok)}\")\nprint(\"expected 0.23 +/- 0.023\")\n\"\"\", tags=[\"claim:figs8-complexity-susceptibility-correlation\"]))\n\ncells.append(md(r\"\"\"\n## figs9-complexity-fit-range-correlation\n\n> Across culture recordings, complexity is positively correlated with the size fit range (0.296)\n> and the duration fit range (0.197).\n\"\"\"))\ncells.append(code(r\"\"\"\nfor col, exp in ((\"s_range\", 0.296), (\"d_range\", 0.197)):\n    for cc, clab in ((\"C_real\", \"complexity.m\"), (\"Cuncut_real\", \"variant no cut\"), (\"Craw_real\", \"variant no correction\")):\n        ok = r_[[cc, col]].dropna()\n        pr = stats.pearsonr(ok[cc], ok[col]); sr = stats.spearmanr(ok[cc], ok[col])\n        print(f\"{col}, {clab}: Pearson r = {pr.statistic:.3f} (p = {pr.pvalue:.2g}), Spearman {sr.statistic:.3f}, n = {len(ok)}; expected {exp} +/- {exp / 10:.4f}\")\n\"\"\", tags=[\"claim:figs9-complexity-fit-range-correlation\"]))\n\ncells.append(md(r\"\"\"\n## fig12a-swap-preserves-complexity\n\n> Culture complexity does not change substantially under spike swapping, and real and swapped\n> complexity are strongly correlated with most recordings near the equality line.\n\"\"\"))\ncells.append(code(r\"\"\"\nfor prefix, lab in ((\"C\", \"complexity.m\"), (\"Cuncut\", \"variant no cut\"), (\"Craw\", \"variant no correction\")):\n    t = panel(prefix)\n    a, b = r_[f\"{prefix}_real\"], r_[f\"{prefix}_swap\"]\n    ok = a.notna() & b.notna()\n    pr = stats.pearsonr(a[ok], b[ok]); sr = stats.spearmanr(a[ok], b[ok]); w = stats.wilcoxon(a[ok], b[ok])\n    rel = ((b - a) / a)[ok]\n    print(f\"{lab}: rank sum p = {t.p['swap']:.3g}, BH {t.p_bh['swap']:.3g}, BY {t.p_by['swap']:.3g}; median change {t.change['swap']:.3g} \"\n          f\"(relative {t.rel_change['swap']:.3f}); median per-recording relative change {rel.median():.3f}; \"\n          f\"Pearson r {pr.statistic:.3f}, Spearman {sr.statistic:.3f}; signed-rank p {w.pvalue:.3g}; n {int(ok.sum())}\")\nfig, ax = plt.subplots(1, 2, figsize=(8, 3.5))\nfor a_, k in zip(ax, (\"swap\", \"shuffle\")):\n    a_.scatter(r_.C_real, r_[f\"C_{k}\"], s=4); m = max(r_.C_real.max(), r_[f\"C_{k}\"].max())\n    a_.plot([0, m], [0, m], \"k--\", lw=.8); a_.set_xlabel(\"real\"); a_.set_ylabel(k)\nplt.tight_layout(); plt.show()\n\"\"\", tags=[\"claim:fig12a-swap-preserves-complexity\"]))\n\ncells.append(md(r\"\"\"\n## fig12b-shuffle-lowers-complexity\n\n> Culture complexity decreases somewhat under neuron shuffling; real and shuffled complexity are\n> strongly correlated, but real complexity tends to be greater.\n\nShuffling as Methods 2.5, which is what the toolbox's `swap2` does, so the variant the claims file\nnames is the same procedure.\n\"\"\"))\ncells.append(code(r\"\"\"\nfor prefix, lab in ((\"C\", \"complexity.m\"), (\"Cuncut\", \"variant no cut\"), (\"Craw\", \"variant no correction\")):\n    t = panel(prefix)\n    a, b = r_[f\"{prefix}_real\"], r_[f\"{prefix}_shuffle\"]\n    ok = a.notna() & b.notna()\n    pr = stats.pearsonr(a[ok], b[ok]); sr = stats.spearmanr(a[ok], b[ok])\n    print(f\"{lab}: real > shuffled in {float((a[ok] > b[ok]).mean()):.3f} of {int(ok.sum())} recordings; rank sum BH {t.p_bh['shuffle']:.3g}, \"\n          f\"BY {t.p_by['shuffle']:.3g}; median change {t.change['shuffle']:.3g}; Pearson r {pr.statistic:.3f}, Spearman {sr.statistic:.3f}\")\nprint(\"per culture, fraction with real > shuffled (complexity.m):\",\n      (r_.C_real > r_.C_shuffle).groupby(r_.culture).mean().round(2).to_dict())\n\"\"\", tags=[\"claim:fig12b-shuffle-lowers-complexity\"]))\ncells.append(md(r\"\"\"\n## Summary\n\"\"\"))\nsave(cells, sys.argv[2])\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/build2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016 && source $TMPDIR/dev/bin/activate && python - <<'EOF'
p='hc8.py'; s=open(p).read()
old="""        prof = mean_profiles(act, size, dur, starts)
        vals["sc_exp"].append(shape_collapse(prof)[0])
    return {k: wls_intercept(sizes, v) for k, v in vals.items()}
"""
new="""        prof = mean_profiles(act, size, dur, starts)
        vals["sc_exp"].append(shape_collapse(prof)[0])
    if return_values:
        return vals
    return {k: wls_intercept(sizes, v) for k, v in vals.items()}


def subsample_chunk(args) -> dict:
    \"\"\"Sub-sample values (own-ISI rebinning) of one recording for a chunk of sizes, for running
    layout reading b in parallel. args = (name, sizes, seed list).\"\"\"
    name, sizes, seed = args
    p = prepare(load(name, _worker_zip()))
    vals = subsample_exponents(p["spikes"], np.random.default_rng(seed), True, p["factor"], sizes,
                               return_values=True)
    vals["n"] = list(sizes)
    return vals
"""
assert old in s; s=s.replace(old,new)
s=s.replace("""def subsample_exponents(spikes: list[np.ndarray], rng: np.random.Generator, own_isi: bool,
                        factor_full: int, sizes: list[int]) -> dict:""","""def subsample_exponents(spikes: list[np.ndarray], rng: np.random.Generator, own_isi: bool,
                        factor_full: int, sizes: list[int], return_values: bool = False) -> dict:""")
open(p,'w').write(s)
b=open('/tmp/claude-1001/nb/build1.py').read()
old=b[b.index("# Layout reading (b): 30 random"):b.index('""", tags=["claim:fig8-subsampling-exponents"]))\n\n# fig8 literature')]
new='''# Layout reading (b): 30 random sub-samples at every integer size from 40% to 100%, on one
# recording drawn with a fixed seed among those kept (the layout costs about 55 times layout (a);
# one recording is what the time limit allows), compared with layout (a) on the same recording.
rng_b = np.random.default_rng([SEED, 8])
i_b = int(rng_b.choice(np.flatnonzero(sel.values)))
n_b = int(base.n_neurons.iloc[i_b] - base.n_silent.iloc[i_b])
sizes_b = hc8.subsample_sizes(n_b, layout="all")
chunks = [(names[idx[i_b]], sizes_b[j::8], [SEED, idx[i_b], 9, j]) for j in range(8)]
t1 = time.time()
with mp.get_context("spawn").Pool(4) as pool:
    parts = pool.map(hc8.subsample_chunk, chunks)
vb = {k: sum((p_[k] for p_ in parts), []) for k in ("tau", "alpha", "sgd", "sc_exp", "n")}
lb = {k: hc8.wls_intercept(vb["n"], vb[k]) for k in ("tau", "alpha", "sgd", "sc_exp")}
print(f"layout (b) on {base.name.iloc[i_b]}: {len(sizes_b)} sub-samples in {(time.time() - t1) / 60:.1f} min")
print(pd.DataFrame({"layout a": [base[f"ss_own_{k}"].iloc[i_b] for k in lb], "layout b": list(lb.values()),
                    "full system": [meas["real"][k].iloc[i_b] for k in lb]}, index=list(lb)).round(3).to_string())
'''
b=b.replace(old,new)
open('/tmp/claude-1001/nb/build1.py','w').write(b)
EOF
python $TMPDIR/nb/build1.py $TMPDIR/nb culture_criticality.ipynb && python $TMPDIR/nb/build2.py $TMPDIR/nb complexity_culture.ipynb && date -u && HC8_SUBSET=4 python $TMPDIR/nb/run.py complexity_culture.ipynb $TMPDIR/nb/out2.ipynb 2>&1 | grep -v WARNING | tail -3
```

```
Mon Nov  9 07:11:06 UTC 2026

[31mTypeError[39m: Axes.boxplot() got an unexpected keyword argument 'labels'. Did you mean 'label'?
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && sed -i 's/labels=KINDS, whis=(0, 100)); ax.set_yscale/whis=(0, 100)); ax.set_xticks(range(1, len(KINDS) + 1), KINDS); ax.set_yscale/' $TMPDIR/nb/build2.py && sed -i 's/plt.xticks(rotation=30); plt.tight_layout(); plt.show()\nprint("plotted/X/' $TMPDIR/nb/build2.py && python $TMPDIR/nb/build2.py $TMPDIR/nb complexity_culture.ipynb && HC8_SUBSET=4 python $TMPDIR/nb/run.py complexity_culture.ipynb $TMPDIR/nb/out2.ipynb 2>&1 | grep -v WARNING | tail -3; python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/nb/out2.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or ''.join(o.get('traceback',[]))[-800:]
        if t: print('---', c.metadata.get('tags'), '\n', str(t)[:1500])
EOF
```

```
time 155.5916519165039
--- None 
 4 recordings in 2.5 min; peak memory of this process 0.21 GB

--- ['sanity'] 
 recordings: 4 | cultures: 4 | neurons analysed: 372
avalanche bins per recording (real): 87688 to 859919
real       complexity (bits/neuron) median 0.00017, range 0.00004 to 0.00837; subset sizes kept by the cut: median 5 of 94; NaN 0
jitter1    complexity (bits/neuron) median 0.00192, range 0.00012 to 0.00448; subset sizes kept by the cut: median 6 of 94; NaN 0
jitter10   complexity (bits/neuron) median 0.00356, range 0.00003 to 0.00826; subset sizes kept by the cut: median 10 of 94; NaN 0
jitter100  complexity (bits/neuron) median 0.00011, range 0.00001 to 0.00043; subset sizes kept by the cut: median 6 of 94; NaN 0
wrap       complexity (bits/neuron) median 0.00045, range 0.00009 to 0.00082; subset sizes kept by the cut: median 10 of 94; NaN 0
poisson    complexity (bits/neuron) median 0.00017, range 0.00008 to 0.00041; subset sizes kept by the cut: median 8 of 94; NaN 0
swap       complexity (bits/neuron) median 0.00076, range 0.00001 to 0.00638; subset sizes kept by the cut: median 5 of 94; NaN 0
shuffle    complexity (bits/neuron) median 0.18722, range 0.00737 to 0.34901; subset sizes kept by the cut: median 64 of 94; NaN 0
neurons left without a spike by shuffling (dropped): 0 recordings
recordings kept under exclusion reading (a): 4 of 4

--- ['claim:fig10a-complexity-randomization'] 
 complexity.m (correction and cut)
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
p='/tmp/claude-1001/nb/build2.py'; b=open(p).read()
old='''idx = list(range(len(names))) if not SUBSET else list(range(0, len(names), len(names) // SUBSET))[:SUBSET]'''
new='''# 180 of the 435 recordings, drawn with a fixed seed: all 435 would take about 68 min with 4
# processes (37 s per recording in development), over the 60 min limit of a notebook
N_RECORDINGS = 180
idx = sorted(np.random.default_rng([SEED, 0]).choice(len(names), size=N_RECORDINGS, replace=False).tolist())
if SUBSET:
    idx = idx[:SUBSET]'''
assert old in b; b=b.replace(old,new)
b=b.replace("""(435 recordings x 8 conditions). Two variants""","""of 8 conditions), and runs on 180 of the 435 recordings drawn with a fixed seed. Two variants""")
open(p,'w').write(b)
EOF
python $TMPDIR/nb/build2.py $TMPDIR/nb complexity_culture.ipynb; grep -c "180" complexity_culture.ipynb
```

```
3
```

**Agent calls Bash**

```bash
cat >> entries/crcns-hc-8-timme-2016/models.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# Analyses of the cortical branching model

def _quad_coef(x):
    """Quadratic coefficient of log10 P(x) on log10 x over the values kept by the cuts of
    Methods 2.7 (P over all avalanches); the claims file's reading of "curved"."""
    import hc8
    u, c = np.unique(x, return_counts=True)
    keep = (u >= hc8.MIN_VALUE) & (c >= hc8.MIN_COUNT)
    if keep.sum() < 3:
        return np.nan
    return float(np.polyfit(np.log10(u[keep]), np.log10(c[keep] / x.size), 2)[0])


def cb_point(args) -> list[dict]:
    """One p_trans: simulate n_models models and, for each, the curvature of the size and duration
    distributions, the shape collapse curvature of the full model and extrapolated by sub-sampling
    (30 sub-samples from 40 to 100 neurons, sizes evenly spaced, Methods 2.10), the susceptibility
    (both readings) extrapolated the same way, and B_new (delays 1 to 8, A(t) <= 5, no
    sub-sampling, Methods 2.11). args = (p_trans, n_models, t_steps, seed)."""
    import hc8
    p_trans, n_models, t_steps, seed = args
    rng = np.random.default_rng(seed)
    packed = cb_simulate(p_trans, n_models, rng, t_steps=t_steps)
    sizes = hc8.subsample_sizes(100)
    out = []
    for m in range(n_models):
        R = cb_raster(packed, m)
        A = R.sum(axis=1).astype(np.int32)
        s, d, st = hc8.avalanches(A)
        rec = dict(p_trans=p_trans, model=m, n_av=int(s.size), active_frac=float((A > 0).mean()),
                   quad_size=_quad_coef(s), quad_dur=_quad_coef(d))
        _, curv = hc8.shape_collapse(hc8.mean_profiles(A, s, d, st))
        rec["curv_full"] = abs(curv) if np.isfinite(curv) else np.nan
        chi_full = hc8.susceptibility(A, 100)
        rec["chi_a_full"], rec["chi_b_full"] = chi_full
        cv, ca, cb = [], [], []
        for n in sizes:
            sub = np.sort(rng.permutation(100)[:n])
            a = R[:, sub].sum(axis=1).astype(np.int32)
            s2, d2, st2 = hc8.avalanches(a)
            c2 = hc8.shape_collapse(hc8.mean_profiles(a, s2, d2, st2))[1]
            cv.append(abs(c2) if np.isfinite(c2) else np.nan)
            x = hc8.susceptibility(a, n)
            ca.append(x[0]); cb.append(x[1])
        rec["curv_ss"] = hc8.wls_intercept(sizes, cv)
        rec["chi_a_ss"] = hc8.wls_intercept(sizes, ca)
        rec["chi_b_ss"] = hc8.wls_intercept(sizes, cb)
        rec["B_new"] = hc8.branching_new(A, hc8.BR_ACT_MAX_MODEL)[0]
        out.append(rec)
    return out


def tau_sd(xmin: int, xmax: int, tau: float, n: int, rng, n_samples: int = 500) -> float:
    """pvcalc.m with threshold 1: the SD of the MLE refitted on surrogates of the fitted law."""
    import hc8
    v = np.arange(xmin, xmax + 1, dtype=float)
    pdf = v ** (-tau)
    pdf /= pdf.sum()
    samp = rng.multinomial(n, pdf, size=n_samples)
    mlog = samp @ np.log(v) / n
    taus = hc8._PLData.TAUS
    logZ = np.log(np.exp(-np.outer(taus, np.log(v))).sum(axis=1))
    L = -logZ[None, :] - mlog[:, None] * taus[None, :]
    return float(np.std(taus[np.argmax(L, axis=1)], ddof=1))
EOF
echo done
```

```
done
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/build3.py",
 "content": "import sys\nsys.path.insert(0, sys.argv[1])\nfrom common import md, code, save\n\ncells = []\ncells.append(md(r\"\"\"\n# Timme et al. (2016): the model claims (chain model, Bethe lattice, cortical branching model)\n\nPaper: Timme et al. (2016), Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425; claims file\n`claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` (version of record, PMC5037237, with the\nsupplement). These claims are simulations and use no recorded data; the dataset, CRCNS hc-8\n(doi:10.6080/K0PC308P, version `unversioned`, see `culture_criticality.ipynb`), is not read here.\nThe models port `bethelattice.m` and `cbmodel.m` of the NCC toolbox (see `models.py`).\n\n| claim | here |\n|---|---|\n| fig3-chain-model-complexity | tested |\n| fig5d-bethe-small-avalanches | tested |\n| fig5e-shuffle-removes-complexity | tested |\n| fig5f-network-state-poisson-keeps-complexity | tested |\n| fig6-cb-distribution-curvature | tested |\n| fig7c-cb-curvature-no-peak | tested on the 0.01 grid (reading b) |\n| fig7ab-cb-complexity-susceptibility-peak | blocked, too_large (complexity of 30 sub-samples per model); the susceptibility and B_new on the grid are printed below for reference |\n| fig7a-complexity-boundary-rise | blocked (depends on fig7ab) |\n| figs2-recording-length | blocked, too_large |\n| fig7d-cb-branching-ratio-near-1 | blocked (depends on fig7ab) |\n\"\"\"))\ncells.append(code(r\"\"\"\nimport os\nfor v in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ.setdefault(v, \"1\")\nimport time, resource\nimport multiprocessing as mp\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport hc8, models\n\nSEED = 20162\nQUICK = bool(os.environ.get(\"MODELS_QUICK\"))     # only while developing\nN_SUBSETS = 10      # random subsets per size for complexity (Methods 2.9 give up to 100)\nBETHE_RUNS = 10 ** 4        # claims file: a standard choice\nCB_MODELS = 30 if not QUICK else 2               # Methods 2.4\nCB_STEPS = 3 * 10 ** 5 if not QUICK else 3 * 10 ** 4   # Methods 2.4\nGRID = np.round(np.arange(0.20, 0.30 + 1e-9, 0.01), 2)  # claims file, p_trans grid reading (b)\nt0 = time.time()\nwith mp.get_context(\"spawn\").Pool(4) as pool:\n    cb_parts = pool.map(models.cb_point, [(float(p), CB_MODELS, CB_STEPS, [SEED, j]) for j, p in enumerate(GRID)])\ncb = pd.DataFrame([r for part in cb_parts for r in part])\nprint(f\"cortical branching models: {len(cb)} ({CB_MODELS} per p_trans, {len(GRID)} values, {CB_STEPS} steps) in \"\n      f\"{(time.time() - t0) / 60:.1f} min\")\n\"\"\"))\ncells.append(code(r\"\"\"\nprint(\"chain model: 12 neurons, c in {0, 0.8, 1}, exact joint distribution\")\nprint(f\"Bethe lattice: {BETHE_RUNS} runs, p_trans 0.5, stop layer 10^4; small avalanches end by layer 8 (255 neurons)\")\nprint(f\"cortical branching model: 100 neurons (10 x 10 torus), p_spont 1e-4, {CB_STEPS} steps, {CB_MODELS} models per p_trans\")\ng = cb.groupby(\"p_trans\")\nprint(pd.DataFrame({\"avalanches (median)\": g.n_av.median(), \"active fraction (median)\": g.active_frac.median().round(3)}).T.to_string())\n\"\"\", tags=[\"sanity\"]))\n\ncells.append(md(r\"\"\"\n## fig3-chain-model-complexity\n\n> In the 12-neuron chain model, random data (c = 0) give zero integration, ordered data (c = 1)\n> give high integration, and only the complex data (c = 0.8) give non-zero complexity.\n\"\"\"))\ncells.append(code(r\"\"\"\nfor c in (0.0, 0.8, 1.0):\n    curve = models.chain_integration_curve(c)\n    print(f\"c = {c}: whole-system integration {curve[-1]:.6f} bits; integration at k = 2, 6, 12: \"\n          f\"{np.round(curve[[1, 5, 11]], 4)}; complexity {models.complexity_from_curve(curve):.8f} bits\")\n\"\"\", tags=[\"claim:fig3-chain-model-complexity\"]))\n\ncells.append(md(r\"\"\"\n## fig5d-bethe-small-avalanches\n\n> In the critical Bethe lattice model (p_trans = 0.5), avalanche sizes are power-law distributed and\n> show shape collapse, and the small avalanches (stopped by the 8th layer) are power-law distributed\n> in size and have non-zero complexity.\n\"\"\"))\ncells.append(code(r\"\"\"\nrng5 = np.random.default_rng([SEED, 5])\nfs_full, fd_full, fprof = models.bethe_full_sizes(BETHE_RUNS, rng5)\nfit_full = hc8.plparams(hc8.apply_cuts(fs_full), rng5)\nprint(f\"full model: {BETHE_RUNS} runs, largest size {fs_full.max()}, longest {fd_full.max()} layers; size fit after cuts: tau {fit_full['tau']}, \"\n      f\"range {fit_full['xmin']} to {fit_full['xmax']}, p {fit_full['p']}\")\nkeep = [p for p, d in zip(fprof, fd_full) if d >= 4]\nu, c = np.unique(fd_full[fd_full >= 4], return_counts=True)\nprof_full = [np.mean([p for p, d in zip(fprof, fd_full) if d == T], axis=0) for T in u[c >= 20]]\nprint(\"full model shape collapse (durations >= 4 seen >= 20 times): 1/sigma nu z %.3f, curvature %.3f\" % hc8.shape_collapse(prof_full))\nraster5, nb5, sizes5 = models.bethe_small_raster(BETHE_RUNS, rng5)\nact5 = hc8.activity(raster5, nb5)\ns5, d5, st5 = hc8.avalanches(act5)\nprint(f\"small avalanches: {len(sizes5)} of {BETHE_RUNS} runs; sizes 1 to {sizes5.max()}; avalanches in the raster {s5.size} \"\n      f\"(sizes match the runs: {np.array_equal(np.sort(s5), np.sort(sizes5))})\")\nfit5 = hc8.plparams(hc8.apply_cuts(s5), rng5)\nfit5_nocut = hc8.plparams(s5, rng5)\nprint(f\"size fit after the cuts of Methods 2.7: tau {fit5['tau']}, range {fit5['xmin']} to {fit5['xmax']}, p {fit5['p']} \"\n      f\"(accepted: {fit5['p'] >= 0.2 if np.isfinite(fit5['p']) else False}); without cuts: tau {fit5_nocut['tau']}, \"\n      f\"range {fit5_nocut['xmin']} to {fit5_nocut['xmax']}, p {fit5_nocut['p']}\")\nbins5 = np.flatnonzero(act5) + 1\nX5 = hc8.raster_matrix(raster5, bins5)\nkeep5 = np.asarray(X5.sum(axis=0)).ravel() > 0\ncx5 = hc8.complexity(X5[:, keep5], N_SUBSETS, np.random.default_rng([SEED, 51]), return_variants=True)\nprint(f\"complexity (correction and cut, {N_SUBSETS} subsets per size): {cx5['cut']:.5f} bits/neuron over {cx5['N']} neurons \"\n      f\"({cx5['k_kept']} sizes kept); variants: no cut {cx5['uncut']:.5f}, no correction {cx5['raw']:.5f}\")\n\"\"\", tags=[\"claim:fig5d-bethe-small-avalanches\"]))\n\ncells.append(md(r\"\"\"\n## fig5e-shuffle-removes-complexity\n\n> In the Bethe lattice small avalanches, neuron shuffling preserves the avalanche size distribution\n> but removes the complexity.\n\"\"\"))\ncells.append(code(r\"\"\"\nrsh = hc8.rand_shuffle(raster5, nb5, np.random.default_rng([SEED, 52]))\nash = hc8.activity(rsh, nb5)\nprint(\"A(t) unchanged by shuffling:\", bool(np.array_equal(ash, act5)), \"| size distribution equal:\",\n      bool(np.array_equal(np.sort(hc8.avalanches(ash)[0]), np.sort(s5))))\nXs = hc8.raster_matrix(rsh, np.flatnonzero(ash) + 1)\nks = np.asarray(Xs.sum(axis=0)).ravel() > 0\ncxs = hc8.complexity(Xs[:, ks], N_SUBSETS, np.random.default_rng([SEED, 53]), return_variants=True)\nprint(f\"shuffled complexity {cxs['cut']:.5f} vs original {cx5['cut']:.5f}: ratio {cxs['cut'] / cx5['cut']:.3f} (criterion < 0.10); \"\n      f\"variants: no cut {cxs['uncut']:.5f} vs {cx5['uncut']:.5f}, no correction {cxs['raw']:.5f} vs {cx5['raw']:.5f}\")\n\"\"\", tags=[\"claim:fig5e-shuffle-removes-complexity\"]))\n\ncells.append(md(r\"\"\"\n## fig5f-network-state-poisson-keeps-complexity\n\n> In the Bethe lattice small avalanches, randomizing the order of whole network states preserves the\n> complexity but changes the avalanche size distribution dramatically.\n\nAll time bins (including the silent bin between runs) are put in a random order, so whole network\nstates move to random times (Methods 2.5, paragraph 4, last sentence).\n\"\"\"))\ncells.append(code(r\"\"\"\nperm = np.random.default_rng([SEED, 54]).permutation(nb5)        # new position of each bin\nrpo = [np.sort(perm[s - 1] + 1) for s in raster5]\napo = hc8.activity(rpo, nb5)\nspo = hc8.avalanches(apo)[0]\nXp = hc8.raster_matrix(rpo, np.flatnonzero(apo) + 1)\nkp = np.asarray(Xp.sum(axis=0)).ravel() > 0\ncxp = hc8.complexity(Xp[:, kp], N_SUBSETS, np.random.default_rng([SEED, 55]), return_variants=True)\nprint(f\"complexity after permuting network states {cxp['cut']:.5f} vs original {cx5['cut']:.5f}: relative difference \"\n      f\"{abs(cxp['cut'] - cx5['cut']) / cx5['cut']:.3f} (criterion < 0.05); no cut {cxp['uncut']:.5f} vs {cx5['uncut']:.5f} \"\n      f\"({abs(cxp['uncut'] - cx5['uncut']) / cx5['uncut']:.3f}); no correction {cxp['raw']:.5f} vs {cx5['raw']:.5f} \"\n      f\"({abs(cxp['raw'] - cx5['raw']) / cx5['raw']:.3f})\")\nprint(f\"avalanches: {spo.size} after vs {s5.size} before; largest size {spo.max()} vs {s5.max()}\")\nfitp = hc8.plparams(hc8.apply_cuts(spo), np.random.default_rng([SEED, 56]))\nsd5 = models.tau_sd(fit5[\"xmin\"], fit5[\"xmax\"], fit5[\"tau\"], fit5[\"n\"], np.random.default_rng([SEED, 57])) if np.isfinite(fit5[\"tau\"]) else np.nan\nprint(f\"size fit after permutation: tau {fitp['tau']}, range {fitp['xmin']} to {fitp['xmax']}, p {fitp['p']}; original tau {fit5['tau']} \"\n      f\"+/- {sd5:.3f} (SD of refits on 500 surrogates)\")\nchanged = (not np.isfinite(fitp[\"p\"])) or fitp[\"p\"] < 0.2 or abs(fitp[\"tau\"] - fit5[\"tau\"]) > sd5\nprint(\"size distribution no longer the original power law:\", changed)\nu0, c0 = np.unique(s5, return_counts=True); u1, c1 = np.unique(spo, return_counts=True)\nprint(\"fraction of avalanches of size 1: before %.3f, after %.3f\" % (c0[u0 == 1].sum() / s5.size, c1[u1 == 1].sum() / spo.size))\n\"\"\", tags=[\"claim:fig5f-network-state-poisson-keeps-complexity\"]))\n\ncells.append(md(r\"\"\"\n## fig6-cb-distribution-curvature\n\n> In the cortical branching model, low transmission probabilities give size and duration\n> distributions that curve downwards, high ones give distributions that curve upwards, and p_trans\n> near 0.25 gives the straightest distributions.\n\"\"\"))\ncells.append(code(r\"\"\"\nq = cb.groupby(\"p_trans\")[[\"quad_size\", \"quad_dur\"]].agg([\"mean\", \"std\", \"count\"])\nprint(q.round(4).to_string())\nfor col in (\"quad_size\", \"quad_dur\"):\n    m = cb.groupby(\"p_trans\")[col].mean()\n    print(f\"{col}: p 0.2 {m[0.2]:.4f} (negative: {m[0.2] < 0}), p 0.3 {m[0.3]:.4f} (positive: {m[0.3] > 0}), \"\n          f\"p 0.25 {m[0.25]:.4f}; smallest magnitude among 0.2, 0.25, 0.3 at {m.loc[[0.2, 0.25, 0.3]].abs().idxmin()}; \"\n          f\"over the grid at {m.abs().idxmin()}\")\n\"\"\", tags=[\"claim:fig6-cb-distribution-curvature\"]))\n\ncells.append(md(r\"\"\"\n## fig7c-cb-curvature-no-peak\n\n> The shape collapse curvature of the cortical branching model does not peak near the critical\n> point; sub-critical avalanches are more curved than super-critical ones.\n\"\"\"))\ncells.append(code(r\"\"\"\ncv = cb.groupby(\"p_trans\")[[\"curv_ss\", \"curv_full\"]].agg([\"mean\", \"std\"])\nprint(cv.round(3).to_string())\nm = cb.groupby(\"p_trans\").curv_ss.mean()\ninner = m.iloc[1:-1]\npeaks = [p for p in inner.index if m[p] > m[round(p - 0.01, 2)] and m[p] > m[round(p + 0.01, 2)]]\nnear = [p for p in peaks if abs(p - 0.25) <= 0.02 or abs(p - 0.265) <= 0.02]\nprint(f\"extrapolated |curvature|: p 0.2 {m[0.2]:.3f} vs p 0.3 {m[0.3]:.3f} (0.2 larger: {m[0.2] > m[0.3]}); interior maxima at {peaks}; \"\n      f\"within 0.02 of 0.25 or 0.265: {near}\")\nmf = cb.groupby(\"p_trans\").curv_full.mean()\nprint(f\"full 100-neuron system: p 0.2 {mf[0.2]:.3f} vs 0.3 {mf[0.3]:.3f}\")\nprint(\"models with a failed shape collapse (NaN):\", int(cb.curv_ss.isna().sum()))\n\"\"\", tags=[\"claim:fig7c-cb-curvature-no-peak\"]))\n\ncells.append(md(r\"\"\"\n## Reference for the blocked claims fig7ab, fig7d\n\nThe complexity of every sub-sample is what makes fig7ab too large here; the susceptibility and the\nbranching ratio on the same models are cheap and are printed for reference. They decide no\noutcome.\n\"\"\"))\ncells.append(code(r\"\"\"\nref = cb.groupby(\"p_trans\")[[\"chi_a_ss\", \"chi_b_ss\", \"chi_b_full\", \"B_new\"]].mean()\nprint(ref.round(4).to_string())\nprint(\"p_trans of the largest mean extrapolated susceptibility: reading (a)\", ref.chi_a_ss.idxmax(), \"| reading (b)\", ref.chi_b_ss.idxmax())\nprint(\"p_trans with mean B_new closest to 1:\", (ref.B_new - 1).abs().idxmin())\nprint(f\"run time of this notebook so far: {(time.time() - t0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\"))\ncells.append(md(r\"\"\"\n## Summary\n\"\"\"))\nsave(cells, sys.argv[2])\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/build3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python $TMPDIR/nb/build3.py $TMPDIR/nb models.ipynb && date -u && MODELS_QUICK=1 python $TMPDIR/nb/run.py models.ipynb $TMPDIR/nb/out3.ipynb 2>&1 | grep -v WARNING | tail -3; python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/nb/out3.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or ''.join(o.get('traceback',[]))[-1200:]
        if t: print('---', c.metadata.get('tags'), '\n', str(t)[:1500])
EOF
```

```
Mon Nov  9 07:17:50 UTC 2026

[31mValueError[39m: Encountered all NA values

--- None 
 cortical branching models: 22 (2 per p_trans, 11 values, 30000 steps) in 0.2 min

--- ['sanity'] 
 chain model: 12 neurons, c in {0, 0.8, 1}, exact joint distribution
Bethe lattice: 10000 runs, p_trans 0.5, stop layer 10^4; small avalanches end by layer 8 (255 neurons)
cortical branching model: 100 neurons (10 x 10 torus), p_spont 1e-4, 30000 steps, 2 models per p_trans
p_trans                      0.20     0.21     0.22     0.23     0.24     0.25     0.26     0.27     0.28     0.29     0.30
avalanches (median)       290.500  278.000  276.500  293.000  278.000  266.000  265.500  252.500  254.500  212.000  114.500
active fraction (median)    0.029    0.033    0.035    0.043    0.051    0.063    0.064    0.093    0.156    0.318    0.604

--- ['claim:fig3-chain-model-complexity'] 
 c = 0.0: whole-system integration 0.000000 bits; integration at k = 2, 6, 12: [0. 0. 0.]; complexity 0.00000000 bits

--- ['claim:fig3-chain-model-complexity'] 
 c = 0.8: whole-system integration 5.841048 bits; integration at k = 2, 6, 12: [0.1966 1.9476 5.841 ]; complexity 0.43126968 bits
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
p='/tmp/claude-1001/nb/build3.py'; b=open(p).read()
b=b.replace('''smallest magnitude among 0.2, 0.25, 0.3 at {m.loc[[0.2, 0.25, 0.3]].abs().idxmin()}; "
          f"over the grid at {m.abs().idxmin()}")''','''smallest magnitude among 0.2, 0.25, 0.3 at {m.loc[[0.2, 0.25, 0.3]].abs().dropna().idxmin() if m.loc[[0.2, 0.25, 0.3]].notna().any() else None}; "
          f"over the grid at {m.abs().dropna().idxmin() if m.notna().any() else None}")''')
b=b.replace('''print("p_trans of the largest mean extrapolated susceptibility: reading (a)", ref.chi_a_ss.idxmax(), "| reading (b)", ref.chi_b_ss.idxmax())
print("p_trans with mean B_new closest to 1:", (ref.B_new - 1).abs().idxmin())''','''print("p_trans of the largest mean extrapolated susceptibility: reading (a)", ref.chi_a_ss.dropna().idxmax(), "| reading (b)", ref.chi_b_ss.dropna().idxmax())
print("p_trans with mean B_new closest to 1:", (ref.B_new - 1).abs().dropna().idxmin())''')
open(p,'w').write(b)
EOF
python $TMPDIR/nb/build3.py $TMPDIR/nb models.ipynb && MODELS_QUICK=1 python $TMPDIR/nb/run.py models.ipynb $TMPDIR/nb/out3.ipynb 2>&1 | grep -v WARNING | tail -2; python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/nb/out3.ipynb',4)
for c in nb.cells[-6:]:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or ''.join(o.get('traceback',[]))[-600:]
        if t: print('---', c.metadata.get('tags'), '\n', str(t)[:1200])
EOF
date -u
```

```
time 21.85775661468506
--- ['claim:fig6-cb-distribution-curvature'] 
         quad_size           quad_dur          
             mean std count     mean std count
p_trans                                       
0.20          NaN NaN     0      NaN NaN     0
0.21          NaN NaN     0      NaN NaN     0
0.22          NaN NaN     0      NaN NaN     0
0.23          NaN NaN     0      NaN NaN     0
0.24          NaN NaN     0      NaN NaN     0
0.25          NaN NaN     0      NaN NaN     0
0.26          NaN NaN     0      NaN NaN     0
0.27          NaN NaN     0      NaN NaN     0
0.28          NaN NaN     0      NaN NaN     0
0.29          NaN NaN     0      NaN NaN     0
0.30          NaN NaN     0      NaN NaN     0
quad_size: p 0.2 nan (negative: False), p 0.3 nan (positive: False), p 0.25 nan; smallest magnitude among 0.2, 0.25, 0.3 at None; over the grid at None
quad_dur: p 0.2 nan (negative: False), p 0.3 nan (positive: False), p 0.25 nan; smallest magnitude among 0.2, 0.25, 0.3 at None; over the grid at None

--- ['claim:fig7c-cb-curvature-no-peak'] 
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cp $TMPDIR/nb/../nb/out1.ipynb /dev/null; ls; printf "aiohttp\nfsspec\nmatplotlib\nnumpy\npandas\nrequests\nscipy\n" > requirements.in && cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-hc-8-timme-2016
type: reproduction
title: Criticality and complexity in rat hippocampal cultures (Timme et al. 2016)
description: Tests the findings of Timme, Marshall, Bennett, Ripp, Lautzenhiser and Beggs (2016) on
  CRCNS data set hc-8, the spike-sorted spontaneous activity of 435 recordings from 28 dissociated
  hippocampal cultures. It recomputes the avalanche statistics, critical exponents with and without
  sub-sampling, branching ratios, susceptibility, shape collapse curvature and neural complexity, and
  their changes under five kinds of randomization, with a Python port of the NCC toolbox the paper
  used. A third notebook runs the paper's chain, Bethe lattice and cortical branching models.
license: Apache-2.0
notebooks:
- path: culture_criticality.ipynb
  title: Avalanches, exponents, branching ratio and randomizations in the culture recordings
  runtime_minutes: 30
- path: complexity_culture.ipynb
  title: Complexity of the culture recordings and of their randomizations
  runtime_minutes: 30
- path: models.ipynb
  title: The chain, Bethe lattice and cortical branching models
  runtime_minutes: 8
helpers:
- hc8.py
- models.py
related:
- id: crcns:hc-8/unversioned
  relation: uses_data
- id: doi:10.3389/fphys.2016.00425
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/crcns-hc-8-timme-2016 2>&1 | tail -3 && python tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -15
```

```
__pycache__
complexity_culture.ipynb
culture_criticality.ipynb
hc8.py
models.ipynb
models.py
wrote entries/crcns-hc-8-timme-2016/requirements.lock.txt
error: entries/crcns-hc-8-timme-2016/culture_criticality.ipynb: neither the notebook nor a helper names version unversioned of dataset hc-8, which entry.yaml pins
error: entries/crcns-hc-8-timme-2016/complexity_culture.ipynb: neither the notebook nor a helper names version unversioned of dataset hc-8, which entry.yaml pins
error: entries/crcns-hc-8-timme-2016/models.ipynb: neither the notebook nor a helper names version unversioned of dataset hc-8, which entry.yaml pins
3 error(s)
```

**Agent calls Bash**

```bash
grep -n "names version\|def _names_dataset\|version_named\|unversioned" tools/entry.py | head;
```

```
204:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
```

**Agent calls Bash**

```bash
sed -n 185,210p tools/entry.py
```

```
report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
        for d, v in versions.items():
            if not v:
                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())

    for name in [n for n in listed if n in present]:
        path = entry_dir / name
        nb = nbformat.read(path, as_version=4)
        if any(c.cell_type == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.cells):
            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
        code = code_of(path)
        for dandiset in dandisets:
            if dandiset not in code and dandiset not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
            version = versions[dandiset]
            if version and version not in code and version not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016 && sed -i 's|^ZIP_MD5 = |DATASET_ID = "hc-8"\nDATASET_VERSION = "unversioned"  # CRCNS data sets carry no versions (docs/archives.md); the MD5 pins the zip\nZIP_MD5 = |' hc8.py && rm -rf __pycache__ && grep -n "DATASET_" hc8.py && cd ../.. && python tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -5; date -u
```

```
53:DATASET_ID = "hc-8"
54:DATASET_VERSION = "unversioned"  # CRCNS data sets carry no versions (docs/archives.md); the MD5 pins the zip
0 error(s)
Mon Nov  9 07:19:17 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016 && source $TMPDIR/dev/bin/activate && PYTHONPATH=. timeout 600 python - <<'EOF'
import pickle, os, numpy as np, hc8, time
res=pickle.load(open(os.environ['TMPDIR']+'/sall.pkl','rb'))
small=sorted(res,key=lambda r:r['nN'])[:3]
names=hc8.recording_names()
for r in small:
    i=names.index(r['name']); t=time.time()
    o=hc8.culture_record((i,r['name'],1)); m=o['measures']['real']
    print(r['name'], r['nN'], round(time.time()-t,1), 'nav',m['n_av'],'tau',m['tau'],'alpha',m['alpha'],'prof',m['n_profiles'],'Bnew',o['B_new'], 'ss', o['ss_own_tau'])
    t=time.time(); c=hc8.complexity_record((i,r['name'],1,10)); print('  C', c['C_real'], c['C_shuffle'], round(time.time()-t,1))
EOF
```

```
Data/Culture1DIV33.mat 3 2.2 nav 3346 tau 1.803 alpha 1.815 prof 10 Bnew 0.993758428602761 ss 0.7577999999999997
  C 0.011185984008466716 0.08622735923594001 0.2
Data/Culture3DIV35.mat 15 1.5 nav 2250 tau 1.0 alpha 3.126 prof 6 Bnew 0.5191544079535776 ss 1.0000000000000002
  C 0.017313017803846604 0.30122426316467155 0.7
Data/Culture3DIV34.mat 26 1.8 nav 8920 tau 3.311 alpha 3.486 prof 10 Bnew 0.48410717863653546 ss 1.1619849386644436
  C 0.0031779160683782642 0.08387951707498584 0.8
```

**Agent calls Bash**

```bash
cd  && date -u && python tools/entry.py all entries/crcns-hc-8-timme-2016 2>&1 | grep -v "WARNING" | tail -20; date -u
```

```
Mon Nov  9 07:19:40 UTC 2026
Installed kernelspec registry-crcns-hc-8-timme-2016 in executed/crcns-hc-8-timme-2016/.venv/share/jupyter/kernels/registry-crcns-hc-8-timme-2016
0 error(s)
pass  culture_criticality.ipynb  (2754 s)
pass  complexity_culture.ipynb  (1896 s)
pass  models.ipynb  (713 s)
Mon Nov  9 08:49:11 UTC 2026
```

**Agent**

All three notebooks passed on the full data (46, 32 and 12 min). Reading the outputs now; 1 h 28 min left before the 10:17 cutoff.

**Agent calls Bash**

```bash
ls executed/crcns-hc-8-timme-2016/ && source $TMPDIR/dev/bin/activate && cat > $TMPDIR/show.py <<'EOF'
import nbformat, sys
nb=nbformat.read(sys.argv[1],4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or ''.join(o.get('traceback',[]))[-600:]
        if t: print('---', c.metadata.get('tags'), '\n', str(t)[:int(sys.argv[2]) if len(sys.argv)>2 else 4000])
EOF
python $TMPDIR/show.py executed/crcns-hc-8-timme-2016/culture_criticality.ipynb 3500
```

```
complexity_culture.ipynb
culture_criticality.ipynb
models.ipynb
result.json
--- None 
 435 recordings analysed in 43.2 min; peak memory of this process 0.23 GB

--- ['sanity'] 
 recordings: 435 | cultures: 28 | recordings per culture: min 13 max 26
DIV range: 6 to 35
neurons (data.nNeurons): total 39529 | min 3 max 142 mean 90.9
length(data.spikes) == nNeurons in every file: True
data.binsize values (ms): [np.float64(0.05)] | datatype: <StringArray>
['Spikes']
Length: 1, dtype: str | expsys: <StringArray>
['Rat Hippocampal Dissociated Cultures']
Length: 1, dtype: str
length(data.channel) == nNeurons: True
data.nbins as minutes: 59.16 to 74.54 (description: about 1 hour)
last spike time: 59.16 to 74.54 min
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python $TMPDIR/show.py executed/crcns-hc-8-timme-2016/complexity_culture.ipynb 5000; python $TMPDIR/show.py executed/crcns-hc-8-timme-2016/models.ipynb 3000; date -u
```

```
--- None 
 180 recordings in 31.5 min; peak memory of this process 0.21 GB

--- ['sanity'] 
 recordings: 180 | cultures: 28 | neurons analysed: 16503
avalanche bins per recording (real): 25459 to 1629926
real       complexity (bits/neuron) median 0.00192, range -0.00001 to 0.07202; subset sizes kept by the cut: median 8 of 94; NaN 0
jitter1    complexity (bits/neuron) median 0.00131, range 0.00000 to 0.03711; subset sizes kept by the cut: median 7 of 94; NaN 0
jitter10   complexity (bits/neuron) median 0.00079, range 0.00000 to 0.02663; subset sizes kept by the cut: median 8 of 94; NaN 0
jitter100  complexity (bits/neuron) median 0.00022, range 0.00000 to 0.00593; subset sizes kept by the cut: median 7 of 94; NaN 0
wrap       complexity (bits/neuron) median 0.00030, range -0.00003 to 0.00154; subset sizes kept by the cut: median 8 of 94; NaN 0
poisson    complexity (bits/neuron) median 0.00029, range 0.00000 to 0.01460; subset sizes kept by the cut: median 8 of 94; NaN 0
swap       complexity (bits/neuron) median 0.00066, range 0.00000 to 0.05213; subset sizes kept by the cut: median 8 of 94; NaN 0
shuffle    complexity (bits/neuron) median 0.14468, range 0.00000 to 0.34901; subset sizes kept by the cut: median 75 of 94; NaN 0
neurons left without a spike by shuffling (dropped): 0 recordings
recordings kept under exclusion reading (a): 180 of 180

--- ['claim:fig10a-complexity-randomization'] 
 complexity.m (correction and cut)
               real_median  rand_median    change  rel_change        p     p_bh     p_by
[... 195 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']
print(json.dumps({k:(v.get('enum') or v.get('type')) for k,v in o['properties'].items()}))
print('required',o.get('required'))
print(json.dumps(o.get('allOf',o.get('if','')))[:1500])
f=s['properties']['findings']['items']; print('findings', f.get('required'), list(f['properties']))
print('top required', s.get('required'))
print(json.dumps(s['properties']['provenance'])[:1500])
EOF
sed -n '/^verifications/,$p' attempts/001453-fouke-2025-01.yaml | head -5; grep -n "^  agent\|^    harness\|protocol:" attempts/001453-fouke-2025-01.yaml | head
```

```
{"claim": "string", "outcome": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "blocked_by": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "too_large", "not_runnable", "other"], "notes": "string", "notebook": "string", "output": "string", "measured": null, "deviations": "array", "assumed": "boolean", "proposed": "object"}
required ['claim', 'outcome']
[{"if": {"properties": {"outcome": {"const": "blocked"}}}, "then": {"required": ["blocked_by", "notes"]}}, {"if": {"properties": {"assumed": {"const": true}}, "required": ["assumed"]}, "then": {"required": ["deviations"], "properties": {"deviations": {"minItems": 1}, "outcome": {"not": {"const": "blocked"}}}}}]
findings ['kind', 'statement'] ['kind', 'statement', 'found']
top required ['schema_version', 'id', 'dataset', 'paper', 'date', 'provenance', 'outcomes']
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platfor
[... 8 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/results.py",
 "content": "FAIL = (\"A failure to reproduce here may be a failure of this attempt, not of the paper: see the \"\n        \"reasoning and the differences from the paper's method.\")\n\nR1 = {\n\"culture-counts\": \"**Result: reproduced.** The data set holds 435 recordings and 39529 neurons, both exactly as stated. The median number of neurons per recording is 91 and the Terrell-Scott mode 93.3, both within 10% of 100. The 5th and 95th percentiles of the firing rate are 0.045 Hz (at the printed precision, on the lower bound of the widened range) and 7.70 Hz, and non-zero rates span 3.62 orders of magnitude.\",\n\"fig2d-network-isi\": \"**Result: reproduced.** The median mean network ISI is 6.67 ms, within 7 +/- 0.7 ms (the histogram mode, 8.50 ms, is outside). ISIs range from 0.91 to 152.78 ms, so some recordings are much higher or lower.\",\n\"fig2e-avalanche-count\": \"**Result: not reproduced.** After rebinning the first 59 min to the network ISI, the median number of avalanches per recording is 83289 and the histogram mode 81707, about eight times the stated 10,000; only 2 of 435 recordings have 9000 to 11000 avalanches.\",\n\"fig8-subsampling-exponents\": \"**Result: reproduced.** Sub-sampling lowers the mean tau from 2.491 to 2.106 and its SD from 0.623 to 0.407, and the mean alpha from 2.928 to 2.730 and its SD from 0.648 to 0.579. The mean 1/sigma nu z changes by 3.6% (size given duration) and 1.6% (shape collapse). With the full system's bin kept for the sub-samples the same holds (tau 1.745, alpha 2.356, changes of 1.9% and 3.4%). On the one recording run with layout (b), the extrapolated values differ from layout (a) by at most 0.044.\",\n\"fig8-exponents-match-literature\": None,\n\"fig8-sigmanuz-methods-agree\": \"**Result: reproduced.** On the full system the two estimates of 1/sigma nu z are 1.411 +/- 0.157 and 1.467 +/- 0.204, a difference of 0.056; with sub-sampling 1.360 +/- 0.226 and 1.490 +/- 0.337, a difference of 0.130. Both differences are smaller than the larger SD.\",\n\"eq4-exponent-relation\": \"**Result: reproduced.** From the mean exponents, (alpha - 1)/(tau - 1) is 1.293 +/- 0.694 for the search algorithm and 1.565 +/- 0.778 for sub-sampling, within one SD of both estimates of 1/sigma nu z (1.411 and 1.467; 1.360 and 1.490). The propagated SDs are large, so this test is weak: per recording, the ratio is within 0.1 of the size given duration exponent in 0.21 of recordings.\",\n\"eq4-relation-randomized\": \"**Result: reproduced.** The relation holds within one SD for all five randomizations that change the avalanches, and for wrap and Poisson both tau (3.262, 4.287) and alpha (3.659, 4.294) differ from the real data's (2.491 +/- 0.623, 2.928 +/- 0.648) by more than one SD.\",\n\"fig9-branching-ratio\": \"**Result: reproduced.** B_new has median 0.973 and SD 0.064; 0.736 of recordings lie in [0.95, 1) and 0.874 in [0.9, 1). B_basic has median 0.798 and SD 0.088, below 0.95 in 0.947 of recordings. Both readings of the band satisfy the criterion; 16 recordings have B_new of 1 or more.\",\n\"fig10b-susceptibility-randomization\": \"**Result: reproduced.** With the Williams-Garcia form N var(A/N) and Benjamini-Hochberg, all five randomizations that change A(t) lower the median susceptibility with corrected p < 0.05 (largest corrected p 0.0231, for 1-bin jitter), and Poisson and wrap give the largest decreases (-72%). With Eq. 14 as printed, or with Benjamini-Yekutieli, 1-bin jitter is not significant (corrected p 0.0908 and 0.235 for Eq. 14).\",\n\"fig10c-curvature-randomization\": \"**Result: partially reproduced.** The absolute shape collapse curvature falls from a median of 2.29 to 0.813 (10-bin jitter), 0.048 (100-bin jitter), 0.266 (wrap) and 0.0746 (Poisson), each with corrected p < 1e-37, but 1-bin jitter raises it to 2.43 (corrected p 0.391). Four of the five randomizations flatten the collapse.\",\n\"fig11ac-fit-range-randomization\": \"**Result: reproduced.** Poisson randomization shortens the median size fit range from 0.694 to 0.248 decades and the duration fit range from 0.663 to 0.211 (corrected p about 4e-141), and 10-bin jitter lengthens them to 0.740 and 0.732 (corrected p 0.000135 and 5e-06). 100-bin jitter and wrap also shorten both ranges significantly, and 1-bin jitter does not change them (corrected p 0.455 and 0.398).\",\n\"fig11bd-exponents-randomization\": \"**Result: partially reproduced.** Tau rises significantly under 10-bin jitter, 100-bin jitter, wrap and Poisson (4 of 5; median 2.50 to 4.53 under Poisson) and falls under 1-bin jitter (2.39, corrected p 0.0108). Alpha rises significantly under 100-bin jitter, wrap and Poisson (3 of 5); 1-bin and 10-bin jitter do not change it significantly (corrected p 0.107 and 0.401).\",\n}\n\nR2 = {\n\"fig10a-complexity-randomization\": \"**Result: partially reproduced.** With the toolbox's complexity, five of the six randomizations other than swapping lower the median complexity with corrected p < 0.05 (from 0.00192 to 0.00022 to 0.00131 bits/neuron), and Poisson is among the two largest decreases; shuffling raises it to 0.145 (corrected p 4.2e-37), against the claim. Without the toolbox's cut, all six lower it under Benjamini-Hochberg (largest corrected p 0.0264).\",\n\"figs8-complexity-susceptibility-correlation\": \"**Result: not reproduced.** Over 180 recordings the Pearson correlation of complexity with susceptibility is 0.542 (Eq. 14) and 0.625 (N var(A/N)), outside 0.23 +/- 0.023; both are positive. Of the variants, complexity without the correction gives 0.221 with Eq. 14, and without the cut -0.330.\",\n\"figs9-complexity-fit-range-correlation\": \"**Result: not reproduced.** The Pearson correlations of complexity with the size and duration fit ranges are 0.143 (p 0.055) and -0.049 (p 0.52), against 0.296 and 0.197. Without the cut they are 0.200 and 0.228, and without the correction 0.466 and 0.245.\",\n\"fig12a-swap-preserves-complexity\": \"**Result: not reproduced.** By the paper's rank sum test, spike swapping lowers the toolbox's complexity (median from 0.00192 to 0.00066, -65%, corrected p 3.2e-08), and real and swapped complexity correlate with Pearson r 0.502, below 0.7. Both variants agree with the paper: without the cut the change is -2.5% (p 0.422, r 0.968), and without the correction -0.2% (p 0.811, r 0.996).\",\n\"fig12b-shuffle-lowers-complexity\": \"**Result: not reproduced.** With the toolbox's complexity, real complexity exceeds shuffled complexity in 0.100 of 180 recordings (median change +0.143, corrected p 4.2e-37) and the correlation is 0.234. Without the cut the claim holds: real exceeds shuffled in 0.994 of recordings, the rank sum gives corrected p 1.1e-25, and r is 0.856.\",\n}\n\nR3 = {\n\"fig3-chain-model-complexity\": \"**Result: reproduced.** The whole-system integration is 0 bits for c = 0 and 11 bits for c = 1 (5.84 for c = 0.8); the complexity is 0 for c = 0 and c = 1 to eight decimals and 0.431 bits for c = 0.8.\",\n\"fig5d-bethe-small-avalanches\": \"**Result: reproduced.** 7018 of 10000 runs end by layer 8. Their sizes after the cuts are accepted as a truncated power law (tau 1.593, sizes 4 to 12, p 0.338), and their complexity is 0.00637 bits/neuron. The full model's sizes are also accepted (tau 1.402, p 0.368).\",\n\"fig5e-shuffle-removes-complexity\": \"**Result: reproduced.** Shuffling leaves A(t), and so the size distribution, unchanged, and lowers the complexity from 0.00637 to 0.00002, a ratio of 0.003.\",\n\"fig5f-network-state-poisson-keeps-complexity\": \"**Result: not reproduced.** Permuting the network states changes the size distribution (tau 2.222 against 1.593 +/- 0.058), but the toolbox's complexity falls from 0.00637 to 0.00001, a relative difference of 0.998. Without the cut the difference is 0.049 and without the correction 0.020, both within 5%: the change comes from where the cut falls.\",\n\"fig6-cb-distribution-curvature\": \"**Result: partially reproduced.** For durations the mean quadratic term is -1.23 at p_trans 0.2, +1.39 at 0.3, and smallest in magnitude at 0.25 (-0.020). For sizes it is +0.087 at 0.2, so the low-p_trans size distributions do not curve downwards by this measure, and the smallest magnitude is at 0.21.\",\n\"fig7c-cb-curvature-no-peak\": \"**Result: not reproduced.** The extrapolated absolute curvature is larger at p_trans 0.2 (4.258) than at 0.3 (2.999), but it has an interior maximum at 0.25 (4.667), so it does peak near the critical point on the 0.01 grid.\",\n}\n\nSUMMARY1 = \"\"\"## Summary\n\n| claim | outcome |\n|---|---|\n| culture-counts | reproduced |\n| fig2d-network-isi | reproduced |\n| fig2e-avalanche-count | not reproduced |\n| fig8-subsampling-exponents | reproduced |\n| fig8-exponents-match-literature | blocked (reference values not retrieved) |\n| fig8-sigmanuz-methods-agree | reproduced |\n| eq4-exponent-relation | reproduced |\n| eq4-relation-randomized | reproduced |\n| fig9-branching-ratio | reproduced |\n| fig10b-susceptibility-randomization | reproduced |\n| fig10c-curvature-randomization | partially reproduced |\n| fig11ac-fit-range-randomization | reproduced |\n| fig11bd-exponents-randomization | partially reproduced |\n\nDifferences from the paper's method: the NCC toolbox is ported to Python (`hc8.py`); jitter\nproposes all moves at once instead of one spike at a time; layout reading (b) of the sub-sampling\nwas run on one recording only; no recording is excluded under reading (a) of the exclusion rule,\nwhile the paper excluded some.\n\nAbout the dataset: the counts of recordings (435) and neurons (39529) match the paper exactly, and\nno recording is deposited twice. 47 recordings have spike times beyond `data.nbins` (64 spikes),\nand 6 recordings have 21 repeated spike times within a neuron.\n\n\"\"\" + FAIL\n\nSUMMARY2 = \"\"\"## Summary\n\n| claim | outcome |\n|---|---|\n| fig10a-complexity-randomization | partially reproduced |\n| figs8-complexity-susceptibility-correlation | not reproduced |\n| figs9-complexity-fit-range-correlation | not reproduced |\n| fig12a-swap-preserves-complexity | not reproduced |\n| fig12b-shuffle-lowers-complexity | not reproduced |\n\nDifferences from the paper's method: 10 random subsets per subset size instead of up to 100, and\n180 of the 435 recordings, to fit the time limit. The toolbox's cut at the first peak of\nI(k)/(k-1) keeps a median of 8 of 94 subset sizes for the real data and 75 for shuffled data, and\nmost of the disagreements come from it: without the cut, fig10a, fig12a and fig12b agree with the\npaper. Whether the paper's 100 subsets make the cut fall later is not tested here.\n\n\"\"\" + FAIL\n\nSUMMARY3 = \"\"\"## Summary\n\n| claim | outcome |\n|---|---|\n| fig3-chain-model-complexity | reproduced |\n| fig5d-bethe-small-avalanches | reproduced |\n| fig5e-shuffle-removes-complexity | reproduced |\n| fig5f-network-state-poisson-keeps-complexity | not reproduced |\n| fig6-cb-distribution-curvature | partially reproduced |\n| fig7c-cb-curvature-no-peak | not reproduced |\n| fig7ab-cb-complexity-susceptibility-peak | blocked, too_large |\n| fig7a-complexity-boundary-rise | blocked, too_large (depends on fig7ab) |\n| figs2-recording-length | blocked, too_large |\n| fig7d-cb-branching-ratio-near-1 | blocked, too_large (depends on fig7ab) |\n\nDifferences from the paper's method: 10 random subsets per size for complexity; the p_trans grid\nof 0.01 only (reading b), as 0.005 would double the simulation time; curvature of the\ndistributions as a quadratic term, a measure the paper does not define. These are simulations, so\nthey say nothing about the dataset.\n\n\"\"\" + FAIL\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/results.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cd $TMPDIR/nb && python - <<'EOF'
import re
p='results.py'; s=open(p).read()
s=s.replace("lower the median complexity with corrected p < 0.05 (from 0.00192 to 0.00022 to 0.00131 bits/neuron)","lower the median complexity with corrected p < 0.05 (medians of 0.00022 to 0.00131 against 0.00192 bits/neuron)")
open(p,'w').write(s)
EOF
cat > insert.py <<'EOF'
import sys, nbformat
sys.path.insert(0, '.')
from results import R1, R2, R3, SUMMARY1, SUMMARY2, SUMMARY3
E = 'entries/crcns-hc-8-timme-2016/'
X = 'executed/crcns-hc-8-timme-2016/'
def patch(path, R, summary, header_fix=None):
    nb = nbformat.read(path, as_version=4)
    if any(c.cell_type == 'markdown' and c.source.startswith('**Result:') for c in nb.cells):
        print('already patched', path); return
    if header_fix:
        nb.cells[0].source = nb.cells[0].source.replace(*header_fix)
    for cid, text in R.items():
        if text is None: continue
        last = max(i for i, c in enumerate(nb.cells) if f'claim:{cid}' in c.metadata.get('tags', []))
        nb.cells.insert(last + 1, nbformat.v4.new_markdown_cell(text))
    j = max(i for i, c in enumerate(nb.cells) if c.cell_type == 'markdown' and c.source.startswith('## Summary'))
    nb.cells[j].source = summary
    nbformat.write(nb, path)
    print('patched', path)
hf = ('| fig8-exponents-match-literature | tested (with outside reference values) |', '| fig8-exponents-match-literature | blocked: the reference values of the three cited papers were not retrieved in this run |')
for base in (E, X):
    patch(base + 'culture_criticality.ipynb', R1, SUMMARY1, hf)
    patch(base + 'complexity_culture.ipynb', R2, SUMMARY2)
    patch(base + 'models.ipynb', R3, SUMMARY3)
EOF
python insert.py; date -u
```

```
patched entries/crcns-hc-8-timme-2016/culture_criticality.ipynb
patched entries/crcns-hc-8-timme-2016/complexity_culture.ipynb
patched entries/crcns-hc-8-timme-2016/models.ipynb
patched executed/crcns-hc-8-timme-2016/culture_criticality.ipynb
patched executed/crcns-hc-8-timme-2016/complexity_culture.ipynb
patched executed/crcns-hc-8-timme-2016/models.ipynb
Mon Nov  9 08:50:59 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
for base in ('entries/crcns-hc-8-timme-2016/','executed/crcns-hc-8-timme-2016/'):
    p=base+'culture_criticality.ipynb'; nb=nbformat.read(p,4)
    for c in nb.cells:
        if c.cell_type=='markdown' and 'The reference values come from the three cited papers' in c.source:
            c.source=c.source.replace("""The reference values come from the three cited papers (inputs of the attempt record); they are
set in the next cell with their sources.""","""The reference values are in the three cited papers. They were not retrieved in this run, so the
cell below holds none and the claim is blocked; the full-system and sub-sampled means it would
compare are printed under fig8-subsampling-exponents.""")
    nbformat.write(nb,p)
EOF
cd entries/crcns-hc-8-timme-2016 && sed -i 's/  runtime_minutes: 30\n- path: complexity/X/' entry.yaml && python - <<'EOF'
s=open('entry.yaml').read()
s=s.replace("""- path: culture_criticality.ipynb
  title: Avalanches, exponents, branching ratio and randomizations in the culture recordings
  runtime_minutes: 30""","""- path: culture_criticality.ipynb
  title: Avalanches, exponents, branching ratio and randomizations in the culture recordings
  runtime_minutes: 46""").replace("""  runtime_minutes: 30
- path: models.ipynb""","""  runtime_minutes: 32
- path: models.ipynb""").replace("runtime_minutes: 8","runtime_minutes: 12")
open('entry.yaml','w').write(s)
EOF
grep runtime entry.yaml; rm -rf __pycache__; ls
```

```
runtime_minutes: 46
  runtime_minutes: 32
  runtime_minutes: 12
complexity_culture.ipynb
culture_criticality.ipynb
entry.yaml
hc8.py
models.ipynb
models.py
requirements.in
requirements.lock.txt
```

**Agent**

Notebooks carry their conclusions. Writing the entry README and the attempt record now (08:52).

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-hc-8-timme-2016/README.md",
 "content": "# Timme et al. (2016) on CRCNS hc-8\n\nTests the findings of Timme, Marshall, Bennett, Ripp, Lautzenhiser and Beggs (2016), \"Criticality\nMaximizes Complexity in Neural Tissue\", Front. Physiol. 7:425 (doi:10.3389/fphys.2016.00425), on\nCRCNS data set hc-8 (doi:10.6080/K0PC308P), the spike-sorted spontaneous activity of 435 recordings\nfrom 28 dissociated rat hippocampal cultures. The files are read in place from the public bucket\n`crcnsarchive/hc-8/live/Data.zip`; CRCNS data sets are not versioned, so the zip's MD5 from the\ndata set's `checksums.md5` pins it.\n\n- `culture_criticality.ipynb`: counts, network ISI, avalanches, critical exponents with and without\n  sub-sampling, branching ratios, susceptibility, shape collapse curvature and fit ranges, and how\n  they change under randomization (all 435 recordings, about 46 min with 4 processes).\n- `complexity_culture.ipynb`: neural complexity of the real and randomized data (180 recordings,\n  about 32 min).\n- `models.ipynb`: the chain model, the Bethe lattice and the cortical branching model (about 12 min).\n- `hc8.py`: loading, and a Python port of the NCC MATLAB toolbox functions the paper used\n  (`plparams`, `plmle`, `pvcalc`, `avprops`, `rebin`, `avgshapes`, `avshapecollapse`,\n  `sizegivdurwls`, `complexity`, `randomizeasdf2`, `brestimate`). `models.py`: the models.\n\nThe counts of recordings and neurons match the paper exactly, and the exponents, branching ratios,\nsusceptibility, curvature and fit ranges behave as the paper reports, with some exceptions under\nthe weakest randomization. The number of avalanches per recording is about eight times the stated\n10,000. The complexity results depend on the toolbox's cut of the integration curve: with it,\nspike swapping and shuffling change complexity in ways the paper does not report; without it they\nagree with the paper. Four model claims are blocked for time.\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\nRun with `python tools/entry.py all entries/crcns-hc-8-timme-2016`.\n"
}
```

```
File created successfully at: entries/crcns-hc-8-timme-2016/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-hc-8-timme-2016-01.yaml",
 "content": "schema_version: 2\nid: crcns-hc-8-timme-2016-01\ndataset:\n  archive: crcns\n  id: hc-8\n  version: unversioned\n  doi: 10.6080/K0PC308P\npaper: doi:10.3389/fphys.2016.00425\ndate: 2026-11-09\nentry: crcns-hc-8-timme-2016\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42570443240\ninputs:\n- what: The NCC MATLAB toolbox the paper cites (Marshall et al., 2016), NCC Toolbox Version 1 of June\n    14th, 2016, read and ported to Python in hc8.py and models.py (power-law fitting, avalanches,\n    shape collapse, complexity, randomizations, branching ratio, Bethe lattice and cortical\n    branching model). It is code, not data; the claims file names the same file.\n  source: http://www.nicholastimme.com/software.html, zip with sha256\n    b7c912f8154f70fc82b13ab1725ed191935ed2877256cadd7e39f66737be294b\noutcomes:\n- claim: culture-counts\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:culture-counts\n  measured:\n  - 435\n  - 39529\n  - 91\n  notes: The data set holds 435 recordings and 39529 neurons (data.nNeurons, equal to the number of\n    spike trains in every file), as the paper states. The median number of neurons per recording is\n    91 and the Terrell-Scott histogram mode 93.3. Firing rates over the first 59 min have 5th and\n    95th percentiles of 0.045 Hz (printed to three decimals, on the lower bound of the criterion's\n    range of 0.045 to 22 Hz) and 7.70 Hz, minimum 0.0155 Hz and maximum 64.20 Hz; non-zero rates\n    span 3.62 orders of magnitude.\n  deviations:\n  - The 5th percentile of the firing rate was printed to three decimals and equals the lower bound\n    of the widened range at that precision, so whether it lies inside cannot be told from the\n    output; the rest of the claim does not depend on it.\n- claim: fig2d-network-isi\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig2d-network-isi\n  measured: 6.67\n  notes: Reading (a), the median mean network ISI over the 435 recordings, is 6.67 ms, within 7 +/-\n    0.7 ms; reading (b), the Terrell-Scott mode, is 8.50 ms and outside. The ISI ranges from 0.91 to\n    152.78 ms (5th to 95th percentile 2.65 to 19.81 ms).\n  deviations:\n  - The ISI is rounded to a whole number of 0.05 ms bins for rebinning, as rebin.m requires (claims\n    file, common detail 1).\n- claim: fig2e-avalanche-count\n  outcome: not_reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig2e-avalanche-count\n  measured: 83289\n  notes: After rebinning the first 59 min to the mean network ISI, the median number of avalanches\n    per recording is 83289 (reading a) and the histogram mode 81707 (reading b), against 10000 +/-\n    1000; the range is 2250 to 531966 and only 2 of 435 recordings have 9000 to 11000. A first 59 min\n    of about 3540 s binned at about 7 ms gives some 500,000 bins, so 10,000 avalanches would need far\n    fewer active bins than these recordings have. How the paper counted avalanches for Figure 2E is\n    asked of the authors (findings).\n- claim: fig8-subsampling-exponents\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig8-subsampling-exponents\n  notes: Over 435 recordings, the full-system search gives tau 2.491 +/- 0.623 and alpha 2.928 +/-\n    0.648; sub-sampling with each sub-sample rebinned to its own ISI gives tau 2.106 +/- 0.407 and\n    alpha 2.730 +/- 0.579, lower means and lower SDs. 1/sigma nu z changes by 3.6% (size given\n    duration, 1.411 to 1.360) and 1.6% (shape collapse, 1.467 to 1.490). Keeping the full system's\n    bin for the sub-samples gives tau 1.745 +/- 0.465, alpha 2.356 +/- 0.504 and changes of 1.9% and\n    3.4%, the same conclusion. On one recording run with layout (b), the extrapolated values differ\n    from layout (a) by at most 0.044. One recording has no accepted duration fit.\n  deviations:\n  - Methods 2.10 do not say whether a sub-sample is rebinned to its own network ISI; the main\n    reading rebins it (\"These analyses were identical to those performed in the whole recorded\n    system\", Methods 2.10), and keeping the full system's bin is shown. Both give the same outcome.\n  - Layout reading (b) of the sub-sampling (30 sub-samples at every integer size) was run on one\n    recording only, as it costs about 55 times layout (a).\n  - No recording is excluded under reading (a) of the exclusion rule (all 435 keep values after the\n    cuts and at least two shape collapse durations), while Figure 2B marks some as excluded.\n- claim: fig8-exponents-match-literature\n  outcome: blocked\n  blocked_by: other\n  notes: The test needs the exponents reported by Mazzoni et al. (2007), Pasquale et al. (2008) and\n    Friedman et al. (2012). They were not retrieved in this run; a title search of arXiv for Friedman\n    et al. (2012) found no record, and there was no time to obtain the other two. The means it would\n    compare are printed under fig8-subsampling-exponents (full system tau 2.491, alpha 2.928;\n    sub-sampled tau 2.106, alpha 2.730).\n- claim: fig8-sigmanuz-methods-agree\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig8-sigmanuz-methods-agree\n  notes: Full system, size given duration 1.411 +/- 0.157 and shape collapse 1.467 +/- 0.204,\n    difference 0.056; sub-sampling (own bin) 1.360 +/- 0.226 and 1.490 +/- 0.337, difference 0.130;\n    sub-sampling (full-system bin) 1.383 and 1.517, difference 0.133 against SD 0.297. Every\n    difference is below the larger SD. Per recording the two differ by less than 0.1 in 0.67 of\n    recordings.\n- claim: eq4-exponent-relation\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:eq4-exponent-relation\n  notes: From the mean exponents, (alpha - 1)/(tau - 1) is 1.293 +/- 0.694 (search algorithm) and\n    1.565 +/- 0.778 (sub-sampling), within one propagated SD of both estimates of 1/sigma nu z. The\n    propagated SDs are about half the value, so the test accepts a wide range; per recording the\n    ratio is within 0.1 of the size given duration exponent in 0.21 of recordings and within 0.2 in\n    0.47 (medians 1.226 and 1.389).\n- claim: eq4-relation-randomized\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:eq4-relation-randomized\n  notes: The relation holds within one SD for all five randomizations that change the avalanches.\n    For wrap and Poisson, tau (3.262, 4.287) and alpha (3.659, 4.294) each differ from the real data\n    (2.491 +/- 0.623, 2.928 +/- 0.648) by more than one SD; for the jitters they do not. Swap and\n    shuffling keep A(t) and so the exponents.\n- claim: fig9-branching-ratio\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig9-branching-ratio\n  notes: B_new (delays 1 to 8, A(t) <= 10) has median 0.973, SD 0.064 and range 0.484 to 1.030; 0.736\n    of recordings lie in [0.95, 1) and 0.874 in [0.9, 1); 16 recordings are at 1 or above. B_basic\n    (Eq. 11) has median 0.798 and SD 0.088, below 0.95 in 0.947 of recordings and below 0.9 in 0.846.\n    Both band readings satisfy the criterion. Variants, brsimple median 0.586 and the per-avalanche\n    ratio of avprops median 0.404.\n- claim: fig10b-susceptibility-randomization\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig10b-susceptibility-randomization\n  notes: Under reading (b) of the susceptibility (N var(A/N)) with Benjamini-Hochberg, all five\n    randomizations that change A(t) lower the median (relative changes -9.2% to -71.9%) with\n    corrected p from 0.0231 (1-bin jitter) to 3e-138, and Poisson and wrap give the largest\n    decreases. Under Eq. 14 as printed (reading a), 1-bin jitter is not significant (corrected p\n    0.0908 BH, 0.235 BY), and under Benjamini-Yekutieli with reading (b) its corrected p is 0.0598.\n    Swap and shuffling leave the susceptibility unchanged, as the legend says.\n- claim: fig10c-curvature-randomization\n  outcome: partially_reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig10c-curvature-randomization\n  notes: The median absolute curvature of the real data is 2.29; it falls to 0.813 (10-bin jitter),\n    0.048 (100-bin jitter), 0.266 (wrap) and 0.0746 (Poisson), each with corrected p below 1e-37\n    under both corrections, and rises to 2.43 under 1-bin jitter (corrected p 0.391). The criterion\n    needs all five, so the claim holds for four. The toolbox's signed curvature is negative (arched)\n    in 0.94 of real recordings.\n- claim: fig11ac-fit-range-randomization\n  outcome: reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig11ac-fit-range-randomization\n  notes: Poisson randomization shortens the median size fit range from 0.694 to 0.248 decades and\n    the duration range from 0.663 to 0.211 (corrected p about 4e-141). 10-bin jitter lengthens them\n    to 0.740 and 0.732 (corrected p 0.000135 and 5e-06, significant). 100-bin jitter and wrap\n    shorten both significantly, and 1-bin jitter changes neither (corrected p 0.455 and 0.398), so\n    the legend's wider statement holds for three of the four other randomizations.\n- claim: fig11bd-exponents-randomization\n  outcome: partially_reproduced\n  notebook: culture_criticality.ipynb\n  output: claim:fig11bd-exponents-randomization\n  notes: Tau rises significantly under 10-bin jitter, 100-bin jitter, wrap and Poisson (median 2.50\n    to 4.53 under Poisson) and falls under 1-bin jitter (2.39, corrected p 0.0108). Alpha rises\n    significantly under 100-bin jitter, wrap and Poisson; 1-bin and 10-bin jitter do not change it\n    significantly (corrected p 0.107 and 0.401). Under Poisson the median largest fitted size falls\n    from 44 to 21, consistent with the paper's explanation.\n- claim: fig10a-complexity-randomization\n  outcome: partially_reproduced\n  notebook: complexity_culture.ipynb\n  output: claim:fig10a-complexity-randomization\n  notes: Over 180 recordings, the toolbox's complexity (correction and cut) has median 0.00192\n    bits/neuron in the real data; 1-bin, 10-bin and 100-bin jitter, wrap and Poisson lower it to\n    medians of 0.00022 to 0.00131 with corrected p from 0.00925 to 5e-31, and Poisson is among the\n    two largest decreases. Shuffling raises it to 0.145 (corrected p 4.2e-37), so five of the six\n    randomizations other than swapping meet the criterion. The cut keeps a median of 8 of 94 subset\n    sizes for the real data and 75 for shuffled data. Without the cut, all six lower complexity\n    (BH, largest corrected p 0.0264); without the correction, shuffling raises it.\n  deviations:\n  - 10 random subsets per subset size, where Methods 2.9 give up to 100, and 180 of the 435\n    recordings drawn with a fixed seed; all 435 with 10 subsets were estimated at about 68 min, over\n    the notebook limit.\n- claim: figs8-complexity-susceptibility-correlation\n  outcome: not_reproduced\n  notebook: complexity_culture.ipynb\n  output: claim:figs8-complexity-susceptibility-correlation\n  measured: 0.542\n  notes: Pearson r between the toolbox's complexity and the susceptibility over 180 recordings is\n    0.542 with Eq. 14 as printed and 0.625 with N var(A/N) (Spearman 0.585 and 0.630), against 0.23\n    +/- 0.023; the correlation is positive, as stated, but larger. Complexity without the correction\n    gives 0.221 with Eq. 14, and without the cut -0.330.\n  deviations:\n  - As for fig10a-complexity-randomization, 10 subsets per size and 180 recordings.\n- claim: figs9-complexity-fit-range-correlation\n  outcome: not_reproduced\n  notebook: complexity_culture.ipynb\n  output: claim:figs9-complexity-fit-range-correlation\n  measured:\n  - 0.143\n  - -0.049\n  notes: Pearson r of the toolbox's complexity with the size fit range is 0.143 (p 0.055) and with\n    the duration fit range -0.049 (p 0.52), against 0.296 and 0.197. Without the cut they are 0.200\n    and 0.228, without the correction 0.466 and 0.245.\n  deviations:\n  - As for fig10a-complexity-randomization, 10 subsets per size and 180 recordings.\n- claim: fig12a-swap-preserves-complexity\n  outcome: not_reproduced\n  notebook: complexity_culture.ipynb\n  output: claim:fig12a-swap-preserves-complexity\n  notes: By the paper's rank sum test, spike swapping lowers the toolbox's complexity from a median\n    of 0.00192 to 0.00066 (-65%; corrected p 3.2e-08 BH, 8.3e-08 BY), and real and swapped\n    complexity correlate with Pearson r 0.502 (Spearman 0.496), below the 0.7 reading of strong.\n    Both variants agree with the paper; without the cut the median change is -2.5% (rank sum p\n    0.422, r 0.968) and without the correction -0.2% (p 0.811, r 0.996). The disagreement comes from\n    the cut of the integration curve, which falls at different subset sizes in real and swapped\n    data.\n  deviations:\n  - As for fig10a-complexity-randomization, 10 subsets per size and 180 recordings.\n- claim: fig12b-shuffle-lowers-complexity\n  outcome: not_reproduced\n  notebook: complexity_culture.ipynb\n  output: claim:fig12b-shuffle-lowers-complexity\n  notes: With the toolbox's complexity, real complexity exceeds shuffled complexity in 0.100 of 180\n    recordings, the median rises by 0.143 (corrected p 4.2e-37) and Pearson r is 0.234. Without the\n    cut the claim holds (real greater in 0.994 of recordings, corrected p 1.1e-25, r 0.856); without\n    the correction real is never greater. Shuffling as Methods 2.5 describe is the toolbox's swap2,\n    so the claims file's variant is the same procedure.\n  deviations:\n  - As for fig10a-complexity-randomization, 10 subsets per size and 180 recordings.\n- claim: fig3-chain-model-complexity\n  outcome: reproduced\n  notebook: models.ipynb\n  output: claim:fig3-chain-model-complexity\n  notes: With the exact joint distribution, the whole-system integration is 0 bits for c = 0, 5.84\n    for c = 0.8 and 11 for c = 1; the complexity is 0 to eight decimals for c = 0 and c = 1 and 0.431\n    bits for c = 0.8.\n- claim: fig5d-bethe-small-avalanches\n  outcome: reproduced\n  notebook: models.ipynb\n  output: claim:fig5d-bethe-small-avalanches\n  notes: Of 10000 runs, 7018 end by layer 8. Their sizes after the cuts of Methods 2.7 are accepted\n    as a truncated power law (tau 1.593, sizes 4 to 12, p 0.338) and their complexity, with the\n    correction and 10 subsets per size, is 0.00637 bits/neuron (no cut 0.271, no correction 0.374).\n    The full model's sizes are accepted too (tau 1.402, 4 to 43, p 0.368) and its shape collapse\n    gives 1/sigma nu z 1.598.\n  deviations:\n  - The number of runs (10^4) is the claims file's standard choice; small avalanches are those whose\n    last active layer is 8 or less (\"stopped on or before the 8th layer\", Results 3.1).\n- claim: fig5e-shuffle-removes-complexity\n  outcome: reproduced\n  notebook: models.ipynb\n  output: claim:fig5e-shuffle-removes-complexity\n  notes: Shuffling leaves A(t) and the size distribution unchanged and lowers the complexity from\n    0.00637 to 0.00002 bits/neuron (ratio 0.003). Without the cut it falls from 0.271 to -0.050;\n    without the correction it rises from 0.374 to 0.414.\n- claim: fig5f-network-state-poisson-keeps-complexity\n  outcome: not_reproduced\n  notebook: models.ipynb\n  output: claim:fig5f-network-state-poisson-keeps-complexity\n  notes: Permuting the order of all time bins changes the size distribution (tau 2.222 against the\n    original 1.593 +/- 0.058, sizes of 1 from 0.361 to 0.209 of avalanches), but the toolbox's\n    complexity falls from 0.00637 to 0.00001, a relative difference of 0.998, against the criterion\n    of 5%. The same states are kept, so the difference comes from the cut; without it the relative\n    difference is 0.049 and without the correction 0.020, both within 5%.\n- claim: fig6-cb-distribution-curvature\n  outcome: partially_reproduced\n  notebook: models.ipynb\n  output: claim:fig6-cb-distribution-curvature\n  notes: Averaged over 30 models, the quadratic term of the duration distribution is -1.23 at\n    p_trans 0.2, +1.39 at 0.3 and smallest in magnitude at 0.25 (-0.020), as stated. For the size\n    distribution it is +0.087 at 0.2 (SD 0.513), +1.22 at 0.3 and smallest in magnitude at 0.21, so\n    the low-p_trans size distributions do not curve downwards by this measure.\n  deviations:\n  - Curvature is the quadratic term of log10 probability on log10 size, the claims file's measure;\n    the paper does not define one.\n- claim: fig7c-cb-curvature-no-peak\n  outcome: not_reproduced\n  notebook: models.ipynb\n  output: claim:fig7c-cb-curvature-no-peak\n  notes: The extrapolated absolute shape collapse curvature, averaged over 30 models, is larger at\n    p_trans 0.2 (4.258) than at 0.3 (2.999), as stated, but it rises to an interior maximum of 4.667\n    at 0.25, within 0.02 of the critical point; the full 100-neuron system peaks there too (3.508).\n  deviations:\n  - Only the p_trans grid of 0.01 (reading b) was run; the 0.005 grid (reading a) would double the\n    simulation time.\n- claim: fig7ab-cb-complexity-susceptibility-peak\n  outcome: blocked\n  blocked_by: too_large\n  notes: The test needs the complexity of 30 sub-samples of each of 30 models at 11 or 21 values of\n    p_trans, 9,900 to 18,900 complexity computations on 40 to 100 neurons and up to 180,000 active\n    bins. At about 2 s each with 10 subsets per size (the culture runs took 37 s per recording for\n    8 computations), that is 5 to 10 hours of CPU, beyond the run. The susceptibility part was run\n    for reference on the 0.01 grid; its extrapolated mean rises monotonically to the largest\n    p_trans tested, 0.3, under both readings, and decides nothing here.\n- claim: fig7a-complexity-boundary-rise\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig7ab-cb-complexity-susceptibility-peak, blocked for the cost of the complexity\n    of the sub-sampled cortical branching models.\n- claim: figs2-recording-length\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the complexity of 30 models per p_trans at three recording lengths, on all time bins,\n    three times the computation that blocks fig7ab-cb-complexity-susceptibility-peak (with\n    extrapolation), or 990 to 1,890 complexity computations of the whole 100-neuron system per\n    recording length without it; not run for time.\n- claim: fig7d-cb-branching-ratio-near-1\n  outcome: blocked\n  blocked_by: too_large\n  notes: Its criterion compares the p_trans where B_new is closest to 1 with the peaks of\n    fig7ab-cb-complexity-susceptibility-peak, which is blocked. B_new was computed for reference on\n    the 0.01 grid; its mean is closest to 1 at p_trans 0.28 (1.0052).\nfindings:\n- kind: metadata_error\n  statement: In 47 of the 435 files, 64 spike times are later than data.nbins, which the data\n    description defines as the length of the recording in bins.\n- kind: format_error\n  statement: Six files hold 21 repeated spike times within one neuron (the same 0.05 ms bin listed\n    twice in a spike train).\n- kind: methods_unavailable\n  statement: Question for the authors. Figure 2E and Methods 2.3 say most recordings contain around\n    10,000 avalanches after rebinning to the mean network ISI. Rebinning the first 59 min of each file\n    to its mean network ISI and counting runs of active bins gives a median of 83,289 avalanches per\n    recording. Were avalanches counted differently for Figure 2E (a different window, bin, or a\n    minimum size or duration)?\n- kind: methods_unavailable\n  statement: Question for the authors. Which recordings were excluded for too few avalanches (red\n    squares of Figure 2B), and with what threshold? Every recording here keeps size and duration\n    values after the cuts of Methods 2.7 and at least two durations for the shape collapse.\n- kind: methods_unavailable\n  statement: Question for the authors. With the complexity function of the NCC toolbox (sub-sampling\n    correction and cut at the first peak of I(k)/(k-1)) and 10 subsets per size, the cut keeps a\n    median of 8 of 94 subset sizes in the real culture data and 75 in shuffled data, and spike\n    swapping then lowers complexity by 65% and shuffling raises it, unlike Figures 10A and 12.\n    Without the cut the results agree with the paper. How often did the cut apply in the paper's\n    culture analysis with 100 subsets, and was it applied to the randomized data in the same way?\n- kind: methods_unavailable\n  statement: Question for the authors. Methods 2.4 give p_trans from 0.2 to 0.3 in increments of\n    0.05, which cannot place a peak at 0.265 (Results 3.2); what grid was used for Figure 7?\n"
}
```

```
File created successfully at: attempts/crcns-hc-8-timme-2016-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p='attempts/crcns-hc-8-timme-2016-01.yaml'; s=open(p).read()
old="""    bins. At about 2 s each with 10 subsets per size (the culture runs took 37 s per recording for
    8 computations), that is 5 to 10 hours of CPU, beyond the run. The susceptibility part was run
    for reference on the 0.01 grid; its extrapolated mean rises monotonically to the largest
    p_trans tested, 0.3, under both readings, and decides nothing here."""
new="""    bins. The culture complexity took 31.5 min for 180 recordings times 8 computations on 4
    processes, about 5 s of CPU per computation with 10 subsets per size; at that rate the model
    claim needs 14 to 26 hours of CPU, beyond the run. The susceptibility part was run for reference
    on the 0.01 grid; its extrapolated mean is largest at 0.3, the largest p_trans tested, under
    both readings, and decides nothing here."""
assert old in s; s=s.replace(old,new)
old="""    recording. A first 59 min
    of about 3540 s binned at about 7 ms gives some 500,000 bins, so 10,000 avalanches would need far
    fewer active bins than these recordings have. How the paper counted"""
assert old not in s
s=s.replace("""1000; the range is 2250 to 531966 and only 2 of 435 recordings have 9000 to 11000. A first 59 min
    of about 3540 s binned at about 7 ms gives some 500,000 bins, so 10,000 avalanches would need far
    fewer active bins than these recordings have. How the paper counted avalanches for Figure 2E is
    asked of the authors (findings).""","""1000; the range is 2250 to 531966 and only 2 of 435 recordings have 9000 to 11000. How the paper
    counted avalanches for Figure 2E is asked of the authors (findings).""")
open(p,'w').write(s)
EOF
grep -n "500,000" attempts/crcns-hc-8-timme-2016-01.yaml; python tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -8; date -u
```

```
0 error(s)
Mon Nov  9 08:52:50 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016 && source $TMPDIR/dev/bin/activate && python - <<'EOF'
p='hc8.py'; s=open(p).read()
old="""               min_isi_ms=float(min(np.diff(s).min() for s in d["spikes"] if s.size > 1) * BIN_MS))"""
new="""               min_isi_ms=float(min(np.diff(s).min() for s in d["spikes"] if s.size > 1) * BIN_MS),
               min_pos_isi_ms=float(min(np.diff(s)[np.diff(s) > 0].min() for s in d["spikes"]
                                        if np.sum(np.diff(s) > 0) > 0) * BIN_MS),
               wave_clus_ref=float(getattr(d["wave_clus"], "ref", np.nan)),
               wave_clus_sr=float(getattr(d["wave_clus"], "sr", np.nan)))"""
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
b=open('/tmp/claude-1001/nb/build1.py').read()
old='''print(f"shortest interval within a neuron: {base.min_isi_ms.min():.2f} ms "
      "(wave_Clus 'ref' parameter is 30 samples, 1.5 ms; Methods 2.2 say the dead time was removed)")'''
new='''print(f"shortest interval within a neuron: {base.min_isi_ms.min():.2f} ms; shortest non-zero: {base.min_pos_isi_ms.min():.2f} ms "
      f"(median over recordings {base.min_pos_isi_ms.median():.2f} ms)")
print("data.wave_ClusParams.ref values:", sorted(base.wave_clus_ref.unique()), "| sr values:", sorted(base.wave_clus_sr.unique()),
      "(Methods 2.2 say the 1.5 ms dead time was removed)")'''
assert old in b; b=b.replace(old,new)
old='''print(f"firing rates over {len(rates)} neurons: 5th percentile {p5:.3f} Hz, 95th {p95:.2f} Hz "'''
new='''print(f"firing rates over {len(rates)} neurons: 5th percentile {p5:.5f} Hz, 95th {p95:.2f} Hz "'''
assert old in b; b=b.replace(old,new)
b=b.replace("""The reference values come from the three cited papers (inputs of the attempt record); they are
set in the next cell with their sources.""","""The reference values are in the three cited papers. They were not retrieved in this run, so the
cell below holds none and the claim is blocked; the full-system and sub-sampled means it would
compare are printed under fig8-subsampling-exponents.""")
open('/tmp/claude-1001/nb/build1.py','w').write(b)
EOF
python $TMPDIR/nb/build1.py $TMPDIR/nb culture_criticality.ipynb && PYTHONPATH=. timeout 300 python -c "
import hc8; o=hc8.culture_record((0,hc8.recording_names()[0],1)); print(o['min_pos_isi_ms'], o['wave_clus_ref'], o['wave_clus_sr'])" && rm -rf __pycache__ && date -u
```

```
0.1 30.0 20000.0
Mon Nov  9 08:53:23 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && ls ../../executed/crcns-hc-8-timme-2016/.venv/share/jupyter/kernels/ && cat > $TMPDIR/nb/run_entry.py <<'EOF'
import sys, time, nbformat
from nbclient import NotebookClient
nb = nbformat.read(sys.argv[1], as_version=4)
t=time.time()
try:
    NotebookClient(nb, timeout=3600, kernel_name=sys.argv[3], resources={"metadata": {"path": "."}}).execute()
finally:
    nbformat.write(nb, sys.argv[2])
    print("time", round(time.time()-t), "s")
EOF
date -u; JUPYTER_PATH=executed/crcns-hc-8-timme-2016/.venv/share/jupyter python $TMPDIR/nb/run_entry.py culture_criticality.ipynb executed/crcns-hc-8-timme-2016/culture_criticality.ipynb registry-crcns-hc-8-timme-2016 2>&1 | grep -v WARNING | tail -3; date -u
```

```
python3
registry-crcns-hc-8-timme-2016
Mon Nov  9 08:53:30 UTC 2026
time 2828 s
Mon Nov  9 09:40:38 UTC 2026
```

**Agent calls Bash**

```bash
cd  && source $TMPDIR/dev/bin/activate && python $TMPDIR/show.py executed/crcns-hc-8-timme-2016/culture_criticality.ipynb 1400 | sed -n 1,75p
```

```
--- None 
 435 recordings analysed in 44.6 min; peak memory of this process 0.22 GB

--- ['sanity'] 
 recordings: 435 | cultures: 28 | recordings per culture: min 13 max 26
DIV range: 6 to 35
neurons (data.nNeurons): total 39529 | min 3 max 142 mean 90.9
length(data.spikes) == nNeurons in every file: True
data.binsize values (ms): [np.float64(0.05)] | datatype: <StringArray>
['Spikes']
Length: 1, dtype: str | expsys: <StringArray>
['Rat Hippocampal Dissociated Cultures']
Length: 1, dtype: str
length(data.channel) == nNeurons: True
data.nbins as minutes: 59.16 to 74.54 (description: about 1 hour)
last spike time: 59.16 to 74.54 min
recordings with spike times beyond data.nbins: 47 (64 spikes)
every spike train sorted: True | recordings with repeated spike times within a neuron: 6 (21 repeats)
shortest interval within a neuron: 0.00 ms; shortest non-zero: 0.05 ms (median over recordings 0.10 ms)
data.wave_ClusParams.ref values: [np.float64(30.0)] | sr values: [np.float64(20000.0)] (Methods 2.2 say the 1.5 ms dead time was removed)
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && source $TMPDIR/dev/bin/activate && python - <<'EOF'
p='results.py'; s=open(p).read()
old="The 5th and 95th percentiles of the firing rate are 0.045 Hz (at the printed precision, on the lower bound of the widened range) and 7.70 Hz"
new="The 5th and 95th percentiles of the firing rate are 0.04548 Hz and 7.70 Hz, inside 0.045 to 22 Hz"
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
python insert.py && cd  && python - <<'EOF'
p='attempts/crcns-hc-8-timme-2016-01.yaml'; s=open(p).read()
old="""    91 and the Terrell-Scott histogram mode 93.3. Firing rates over the first 59 min have 5th and
    95th percentiles of 0.045 Hz (printed to three decimals, on the lower bound of the criterion's
    range of 0.045 to 22 Hz) and 7.70 Hz, minimum 0.0155 Hz and maximum 64.20 Hz; non-zero rates
    span 3.62 orders of magnitude.
  deviations:
  - The 5th percentile of the firing rate was printed to three decimals and equals the lower bound
    of the widened range at that precision, so whether it lies inside cannot be told from the
    output; the rest of the claim does not depend on it.
"""
new="""    91 and the Terrell-Scott histogram mode 93.3. Firing rates over the first 59 min have 5th and
    95th percentiles of 0.04548 Hz and 7.70 Hz, inside the criterion's range of 0.045 to 22 Hz,
    close to its lower bound; the minimum is 0.0155 Hz and the maximum 64.20 Hz, and non-zero rates
    span 3.62 orders of magnitude.
"""
assert old in s; s=s.replace(old,new)
s=s.replace("""- kind: methods_unavailable
  statement: Question for the authors. Figure 2E""","""- kind: other
  statement: data.wave_ClusParams.ref is 30 in every file (1.5 ms at the stored sr of 20000 Hz), the
    detector dead time, while Methods 2.2 say the dead time was removed; within-neuron intervals as
    short as 0.05 ms occur, so the stored parameter does not describe the sorting that produced
    the spikes.
- kind: methods_unavailable
  statement: Question for the authors. Figure 2E""",1)
open(p,'w').write(s)
EOF
python tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -3; python tools/entry.py handover entries/crcns-hc-8-timme-2016 2>&1 | tail -5; ls executed/crcns-hc-8-timme-2016/handover/; date -u
```

```
patched entries/crcns-hc-8-timme-2016/culture_criticality.ipynb
already patched entries/crcns-hc-8-timme-2016/complexity_culture.ipynb
already patched entries/crcns-hc-8-timme-2016/models.ipynb
patched executed/crcns-hc-8-timme-2016/culture_criticality.ipynb
already patched executed/crcns-hc-8-timme-2016/complexity_culture.ipynb
already patched executed/crcns-hc-8-timme-2016/models.ipynb
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Traceback (most recent call last):
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
ls: cannot access 'executed/crcns-hc-8-timme-2016/handover/': No such file or directory
Mon Nov  9 09:40:53 UTC 2026
```

**Agent**

The dev venv was still active; rerunning the checks with the system Python.

**Agent calls Bash**

```bash
deactivate 2>/dev/null; cd  && /usr/bin/env -u VIRTUAL_ENV PATH=/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin python3 tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -3; which python; python tools/entry.py check entries/crcns-hc-8-timme-2016 2>&1 | tail -3 && python tools/entry.py handover entries/crcns-hc-8-timme-2016 2>&1 | tail -5; ls executed/crcns-hc-8-timme-2016/handover/
```

```
File "tools/entry.py", line 54, in <module>
    import nbformat
ModuleNotFoundError: No module named 'nbformat'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
0 error(s)
wrote executed/crcns-hc-8-timme-2016/handover
10.3389-fphys.2016.00425.yaml
complexity_culture.ipynb
culture_criticality.ipynb
hc8.py
models.ipynb
models.py
```

**Agent calls Bash**

```bash
grep -c "Result:" executed/crcns-hc-8-timme-2016/handover/*.ipynb; grep -c "Result:" entries/crcns-hc-8-timme-2016/*.ipynb; git status --short; date -u
```

```
executed/crcns-hc-8-timme-2016/handover/complexity_culture.ipynb:0
executed/crcns-hc-8-timme-2016/handover/culture_criticality.ipynb:0
executed/crcns-hc-8-timme-2016/handover/models.ipynb:0
entries/crcns-hc-8-timme-2016/complexity_culture.ipynb:5
entries/crcns-hc-8-timme-2016/culture_criticality.ipynb:12
entries/crcns-hc-8-timme-2016/models.ipynb:6
 M tools/build_site.py
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
?? attempts/crcns-hc-8-timme-2016-01.yaml
?? entries/crcns-hc-8-timme-2016/
?? scripts
[... 1 more lines not kept]
```

**Agent**

I've finished the author run (protocol steps 1 to 6) for CRCNS hc-8 and Timme et al. 2016. The entry is `entries/crcns-hc-8-timme-2016/` (three notebooks, helpers `hc8.py` and `models.py`) and the record is `attempts/crcns-hc-8-timme-2016-01.yaml`. `entry.py check` reports 0 errors and the handover is built. Nothing is committed.

The analyses use a Python port of the paper's NCC MATLAB toolbox. I downloaded it from the author's website; its sha256 matches the one in the claims file, and it is listed under `inputs`. The data set is pinned as `unversioned`, with the MD5 of `Data.zip` from `checksums.md5`. CRCNS data sets have no versions and the bucket holds only this one copy.

**1. Outcomes** (29 claims: 12 reproduced, 4 partially reproduced, 8 not reproduced, 5 blocked)

| claim | outcome |
|---|---|
| culture-counts | reproduced: 435 recordings, 39,529 neurons, median 91 neurons |
| fig2d-network-isi | reproduced: median 6.67 ms |
| fig2e-avalanche-count | not reproduced: median 83,289 avalanches, not about 10,000 |
| fig8-subsampling-exponents | reproduced |
| fig8-exponents-match-literature | blocked (`other`): reference values from the three cited papers not retrieved |
| fig8-sigmanuz-methods-agree | reproduced |
| eq4-exponent-relation | reproduced (weak test: the propagated SDs are large) |
| eq4-relation-randomized | reproduced |
| fig9-branching-ratio | reproduced |
| fig10b-susceptibility-randomization | reproduced (under N·var(A/N) with Benjamini-Hochberg) |
| fig10c-curvature-randomization | partially reproduced: 4 of 5 randomizations |
| fig11ac-fit-range-randomization | reproduced |
| fig11bd-exponents-randomization | partially reproduced: tau 4 of 5, alpha 3 of 5 |
| fig10a-complexity-randomization | partially reproduced: shuffling raises complexity |
| figs8-complexity-susceptibility-correlation | not reproduced: r 0.542 vs 0.23 |
| figs9-complexity-fit-range-correlation | not reproduced: r 0.143 and -0.049 |
| fig12a-swap-preserves-complexity | not reproduced: swapping lowers complexity by 65% |
| fig12b-shuffle-lowers-complexity | not reproduced: real exceeds shuffled in only 10% of recordings |
| fig3-chain-model-complexity | reproduced |
| fig5d-bethe-small-avalanches | reproduced |
| fig5e-shuffle-removes-complexity | reproduced |
| fig5f-network-state-poisson-keeps-complexity | not reproduced |
| fig6-cb-distribution-curvature | partially reproduced: durations match, sizes at p_trans 0.2 do not |
| fig7c-cb-curvature-no-peak | not reproduced: curvature peaks at 0.25 |
| fig7ab, fig7a-complexity-boundary-rise, figs2, fig7d | blocked (`too_large`): complexity of sub-sampled cortical branching models, about 14 to 26 h of CPU |

Most of the complexity failures come from one step: the toolbox cuts the integration curve at its first peak. In the real data that cut keeps a median of 8 of 94 subset sizes, against 75 in shuffled data. Without the cut, fig10a, fig12a, fig12b and fig5f agree with the paper. No outcome is marked as resting on an assumption.

**2. Dataset**
- The counts match the paper exactly, and no recording is deposited twice.
- Findings recorded:
  - 47 files have 64 spike times beyond `data.nbins`.
  - 6 files repeat a spike time within a neuron, 21 times in all.
  - `wave_ClusParams.ref` is 30 samples (1.5 ms) in every file, although Methods 2.2 say the dead time was removed; intervals as short as 0.05 ms occur.
- Four questions for the paper's authors are recorded as `methods_unavailable` findings:
  - how avalanches were counted for Figure 2E;
  - which recordings were excluded for too few avalanches, and by what threshold (none are excluded under the reading used here);
  - how often the complexity cut applied with 100 subsets, and whether randomized data were cut the same way;
  - the p_trans grid of Figure 7.
- No questions to a reader.

**3. Where the protocol was unclear or missing something**
1. It doesn't say how to classify claims that are pure simulations and use no recorded data. I tested them with the default `data: dataset` and said in the notebook and summary that they say nothing about the dataset.
2. Under "Time" it allows `too_large` only "where the computation stopped it". For claims that only depend on a claim blocked for cost (fig7d, fig7a-boundary), I used `too_large` and named the dependency in the notes.
3. It doesn't say how to block an outside input that is public but wasn't retrieved in time (fig8-literature). I used `other`.
4. It doesn't say how to add the "**Result:**" cells, which can only be written after the full run, without re-executing. I inserted the same markdown cells into the source and the executed notebooks, leaving code and outputs untouched.
5. "Run every command in the foreground" plus the 60-minute notebook limit forced splitting the work into three notebooks; the protocol could suggest this for heavy entries.
6. The data-check step's clock check doesn't fit a dataset with a single spike-time stream. I said in the notebook that there is no second clock to check.

**4. Runtime and what failed**
- Full runs: 46 min (criticality, all 435 recordings), 32 min (complexity, 180 recordings), 12 min (models). The criticality notebook was re-run once (47 min) to print the firing-rate percentile at higher precision and read the wave_Clus parameters from the files.
- About 47 minutes were lost early to a development cell whose run time I underestimated: a sub-sampling layout that ran 44.9 min on 4 recordings. That layout ended up being run on one recording only.
- To fit the limits, complexity uses 10 subsets per size instead of 100 and 180 of the 435 recordings, and the p_trans grid is 0.01 only. Each is recorded as a deviation.
- Untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others) are at the repository root; I didn't create them. `tools/build_site.py` was already modified when the run started.

## End of run

78 turns, 217 minutes, $9.87 at API prices, result: success.
