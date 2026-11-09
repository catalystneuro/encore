# johnson-2017 · author · run 42682552461

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md | head -c 200000 | wc -c; ls; ls entries claims attempts paper
```

```
Mon Nov  9 19:25:33 UTC 2026
38382
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
[... 758 more lines not kept]
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
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 628 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/johnson-2017.yaml; ls papers/datasets | grep johnson; cat papers/datasets/johnson-2017.yaml; ls targets | head; grep -rl "pfc-5" targets queue 2>/dev/null | head
```

```
<persisted-output>
Output too large (42.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/65f5c295-e757-4da1-b024-8d3e92f7524b/tool-results/b408r1q2l.txt

Preview (first 2KB):
# Claims for Johnson, Dewar, Solbakk, Endestad, Meling & Knight (2017), Current Biology 27,
# 1829-1835, "Bidirectional Frontoparietal Oscillatory Systems Support Working Memory",
# doi:10.1016/j.cub.2017.05.046, on CRCNS data set pfc-5 (doi:10.6080/K0ZC811B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
# protocol as stated in docs/protocol.md (Reader), version pilot-14.
#
# Text read: the version of record with its supplemental information, as supplied under paper/
# (PDF extracted to text): main text (Results, Discussion), figure legends 1 to 4, STAR Methods
# (pages e1 to e4), and the supplement (legends of Figures S1 to S4, Tables S1 to S3, read from
# the text). The PDF could not be rendered in this run, so the figures themselves were not read:
# the channel list of the Figure 2 cluster (the PFC region of interest of the PSI analysis) and
# the time courses of Figures 2 to 4 are known only from the text and legends. The extraction
# garbles symbols: "3" stands for the multiplication sign, "/" for an arrow, "%" for less than
# or equal, "R" for greater than or equal, "jZj" for |Z|, and a replacement character for the
# minus sign in exponents. Quotes keep the extracted characters. The CRCNS data descriptor
# (paper/pfc-5.data-description.txt) was read only to know what the data set holds; no claim or
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/johnson-2017.yaml"
}
```

```
1	# Claims for Johnson, Dewar, Solbakk, Endestad, Meling & Knight (2017), Current Biology 27,
2	# 1829-1835, "Bidirectional Frontoparietal Oscillatory Systems Support Working Memory",
3	# doi:10.1016/j.cub.2017.05.046, on CRCNS data set pfc-5 (doi:10.6080/K0ZC811B).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record with its supplemental information, as supplied under paper/
8	# (PDF extracted to text): main text (Results, Discussion), figure legends 1 to 4, STAR Methods
9	# (pages e1 to e4), and the supplement (legends of Figures S1 to S4, Tables S1 to S3, read from
10	# the text). The PDF could not be rendered in this run, so the figures themselves were not read:
11	# the channel list of the Figure 2 cluster (the PFC region of interest of the PSI analysis) and
12	# the time courses of Figures 2 to 4 are known only from the text and legends. The extraction
13	# garbles symbols: "3" stands for the multiplication sign, "/" for an arrow, "%" for less than
14	# or equal, "R" for greater than or equal, "jZj" for |Z|, and a replacement character for the
15	# minus sign in exponents. Quotes keep the extracted characters. The CRCNS data descriptor
16	# (paper/pfc-5.data-description.txt) was read only to know what the data set holds; no claim or
17	# method comes from it.
18	#
19	# Code. The paper's Key Resources Table and Data and Software Availability say the custom MATLAB
20	# code is deposited with the data at CRCNS (http://crcns.org). By the data descriptor it is the
[... 645 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/pfc-5.data-description.txt; sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls -R entries/fouke-2025 | head -30; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -c 6000 attempts/fouke-2025-01.yaml
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
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pfc-5/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-5; curl -s $B/live/checksums.md5; curl -s $B/live/filelist.txt; curl -s $B/live/docs/summary_file_behavior_pfc.txt; mkdir -p scripts && curl -s $B/live/analysis_scripts.tar.gz | tar xz -C scripts && find scripts -type f | xargs ls -la
```

```
463b2d55e0ab54842879baa262d69a6a  analysis_scripts.tar.gz
8b99bb689ca4e4f0aec71a8604263e9a  Cortex_2021_paper_update.zip
42af60ebf34494de818693b77c2795d3  data/ctrl01.tar.gz
e79834d7631eb9dfce807f372c75e3aa  data/ctrl02.tar.gz
7a834cf6afc4fd44855e0ec6d643a47c  data/ctrl03.tar.gz
bbd773e7945d1bcc2928227383707bef  data/ctrl04.tar.gz
3923511ac3def13d56e2af2eff18774e  data/ctrl05.tar.gz
25da306213bed17f3e5e1514d5888a6a  data/ctrl06.tar.gz
bcd427429fb041a9455c4db5cfc6c768  data/ctrl07.tar.gz
ebf09a6d3c5a9d4b4c570cecf8b1ce01  data/ctrl08.tar.gz
276409e1fda02b443221505e32921097  data/ctrl09.tar.gz
aec230327ab8c33a17990382a1bb1068  data/ctrl10.tar.gz
55bf9dc60f42adbcf687bc7b8365f71a  data/ctrl11.tar.gz
d11208b51b397f3c4e22c32941302aa2  data/ctrl12.tar.gz
851f79f8b790e90808f43f267fbc20f1  data/ctrl13.tar.gz
534186e60a2b235cda232659efdbf8f2  data/ctrl14.tar.gz
accc5cf833d24db61ef5b40df333fa51  data/ctrl15.tar.gz
30261b19e9d37d636ef0876a3ec8f436  data/ctrl16.tar.gz
6420818c25888266d021cb7985deb32c  data/ctrl17.tar.gz
8e4cf6cb8f73d7afc3fd45909d6a255c  data/ctrl18.tar.gz
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/analysis_scripts; for f in erp_compute.m erp_stat_group.m erp_stat_group_hem.m fft_compute.m fft_stat_group.m fft_stat_group_hem.m; do echo "=== $f"; cat $f; done
```

```
=== erp_compute.m
% Compute task-induced ERPs for all subjects in a group. Requires fieldtrip
% toolbox.
%
% Key:
% group = 'ctrl'/'pfc' (required)
%
% E. L. Johnson, PhD
% Copyright (c) 2017
% UC Berkeley
% [removed: an e-mail address]

function [] = erp_compute(group)
% erp_compute('ctrl');

% INPUT PATH TO DATA DIRECTORY
path = %%INSERT%%

dataDir = [path '/data/'];
saveDir = [path '/erp/'];
[... 451 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/analysis_scripts; for f in tfr_compute.m tfr_stat_group.m psi_compute.m psi_stat_group.m psi_degree_stat_group.m subfunctions/psianalysis.m subfunctions/subtracterp.m subfunctions/zbaseline.m; do echo "=== $f"; cat $f; done; diff psi_compute.m psi_compute_ver_0_60.m; diff subfunctions/psianalysis.m subfunctions/psianalysis_ver_0_60.m; diff tfr_stat_group.m tfr_stat_group_hem.m | head -20
```

```
=== tfr_compute.m
% Compute task-induced TFRs for all subjects in a group. Requires fieldtrip
% toolbox.
%
% Key:
% group = 'ctrl'/'pfc' (required)
%
% E. L. Johnson, PhD
% Copyright (c) 2017
% UC Berkeley
% [removed: an e-mail address]

function [] = tfr_compute(group)
% tfr_compute('ctrl');

% INPUT PATH TO DATA DIRECTORY
path = %%INSERT%%

dataDir = [path '/data/'];
saveDir = [path '/tfr/'];
[... 803 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "import fsspec, scipy, numpy, h5py, mne" 2>&1; uv --version; time python3 - <<'EOF'
import tarfile, urllib.request, time
t=time.time()
u=urllib.request.urlopen("https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-5/live/data/pfc02.tar.gz")
tf=tarfile.open(fileobj=u, mode="r|gz")
for m in tf:
    print(m.name, m.size, round(time.time()-t,1))
    if m.isfile():
        f=tf.extractfile(m)
        n=0
        while True:
            b=f.read(1<<22)
            if not b: break
            n+=len(b)
print(time.time()-t)
EOF
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec, scipy, numpy, h5py, mne
ModuleNotFoundError: No module named 'fsspec'
uv 0.13.7 (x86_64-unknown-linux-gnu)
pfc02 0 0.5
pfc02/data_primary.bdf 392915456 0.5
pfc02/data_derived.mat 42137319 7.9
pfc02/summary_file_trial.csv 5212 8.8
8.83281922340393

real	0m8.892s
user	0m2.686s
sys	0m0.665s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q numpy scipy h5py mne fsspec aiohttp requests pandas statsmodels matplotlib ipykernel nbformat nbclient 2>&1 | tail -2; python -c "import mne; print(mne.__version__)"
```

```
1.13.2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import tarfile, urllib.request, io, scipy.io, numpy as np, time
u=urllib.request.urlopen("https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-5/live/data/pfc02.tar.gz")
tf=tarfile.open(fileobj=u, mode="r|gz")
for m in tf:
    if m.name.endswith('.mat'):
        b=tf.extractfile(m).read(); open('pfc02.mat','wb').write(b)  # dev only, scratch
    if m.name.endswith('.csv'):
        open('pfc02.csv','wb').write(tf.extractfile(m).read())
print(b[:120])
EOF
head -5 pfc02.csv; wc -l pfc02.csv
```

```
b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Tue Jun  6 21:32:29 2017 HDF5 schema 1.00 .                     \x00\x00\x00\x00'
1,0,1,1,1,1150,2564,4945,6845,9395
2,1,2,2,2,900,1065,21137,23037,25337
3,0,2,2,2,900,2054,38286,40186,42486
4,1,1,2,2,1150,641,55982,57882,60432
5,0,1,2,3,900,4425,72362,74262,76562
120 pfc02.csv
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import h5py, numpy as np
f=h5py.File('pfc02.mat','r')
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype)
f.visititems(show) if False else None
print(list(f.keys()))
for seg in ['pretrial','encmain','proc']:
    g=f[seg]; print(seg, list(g.keys()))
    for k in g.keys():
        o=g[k]
        if isinstance(o,h5py.Dataset): print('  ',k,o.shape,o.dtype, o[()].ravel()[:8] if o.dtype!=object and o.size<50000 else '')
    tr=g['trial']; print('  ntrials',tr.shape)
    r0=f[tr[0,0]]; print('  trial0',r0.shape)
    t0=f[g['time'][0,0]][()].ravel(); print('  time0',t0[0],t0[-1],len(t0))
    ti=g['trialinfo'][()]; print('  trialinfo', ti.shape, ti[:,:5].T)
lab=[''.join(chr(c) for c in f[r][()].ravel()) for r in f['encmain']['label'][()].ravel()]
print(lab)
EOF
```

```
['#refs#', 'encmain', 'pretrial', 'proc']
pretrial ['elec', 'fsample', 'label', 'time', 'trial', 'trialinfo']
   fsample (1, 1) float64 [255.64295676]
   label (1, 64) object 
   time (108, 1) object 
   trial (108, 1) object 
   trialinfo (7, 108) float64 [1. 2. 3. 4. 5. 6. 7. 8.]
  ntrials (108, 1)
  trial0 (129, 64)
  time0 0.0 0.5 129
  trialinfo (7, 108) [[1.000e+00 0.000e+00 1.000e+00 1.000e+00 1.000e+00 1.150e+03 2.564e+03]
 [2.000e+00 1.000e+00 2.000e+00 2.000e+00 2.000e+00 9.000e+02 1.065e+03]
 [3.000e+00 0.000e+00 2.000e+00 2.000e+00 2.000e+00 9.000e+02 2.054e+03]
 [4.000e+00 1.000e+00 1.000e+00 2.000e+00 2.000e+00 1.150e+03 6.410e+02]
 [5.000e+00 0.000e+00 1.000e+00 2.000e+00 3.000e+00 9.000e+02 4.425e+03]]
encmain ['elec', 'fsample', 'label', 'time', 'trial', 'trialinfo']
   fsample (1, 1) float64 [256.]
   label (1, 64) object 
   time (108, 1) object 
   trial (108, 1) object 
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import h5py, numpy as np, pandas as pd
f=h5py.File('pfc02.mat','r')
ti={s:f[s]['trialinfo'][()].T for s in ['pretrial','encmain','proc']}
for s in ti: print(s, ti[s][:,0].astype(int).tolist()[:30])
print(set(ti['encmain'][:,0])==set(ti['proc'][:,0]), set(ti['pretrial'][:,0])==set(ti['encmain'][:,0]))
print((ti['pretrial']==ti['encmain']).all())
csv=pd.read_csv('pfc02.csv',header=None)
print(csv.shape, csv[1].mean(), csv[2].value_counts().to_dict())
m=csv.set_index(0).loc[ti['encmain'][:,0].astype(int)]
print((m[1].values==ti['encmain'][:,1]).all(), (m[2].values==ti['encmain'][:,2]).all(), (m[4].values==ti['encmain'][:,4]).all())
m=csv.set_index(0).loc[ti['proc'][:,0].astype(int)]
print((m[1].values==ti['proc'][:,1]).all(), (m[2].values==ti['proc'][:,2]).all())
# elec
e=f['encmain']['elec']; print(list(e.keys()))
EOF
```

```
pretrial [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
encmain [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
proc [2, 3, 5, 7, 9, 12, 13, 16, 18, 20, 21, 23, 26, 27, 30, 31, 33, 35, 38, 39, 42, 44, 45, 47, 50, 52, 54, 56, 57, 60]
True True
True
(120, 10) 0.6666666666666666 {1: 60, 2: 60}
True True True
True True
['chanpos', 'elecpos', 'label']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; wc -c paper/10.1016-j.cub.2017.05.046.txt; grep -n "STAR\|Data Preprocessing\|Spectral Decomposition\|Phase Slope\|Graph Theory\|Cluster-Based\|Behavioral Analysis\|Event-Related\|Baseline Spectral" paper/10.1016-j.cub.2017.05.046.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt",
 "offset": 20,
 "limit": 230
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt",
 "offset": 596,
 "limit": 480
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt",
 "offset": 249,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt",
 "offset": 1075,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; curl -s https://raw.githubusercontent.com/fieldtrip/fieldtrip/20151205/specest/ft_specest_mtmconvol.m | grep -n "reqtimeboi\|prepad\|postpad\|padtype\|nan(\|NaN" | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sI https://raw.githubusercontent.com/fieldtrip/fieldtrip/20151205/specest/ft_specest_mtmconvol.m | head -3; curl -s "https://api.github.com/repos/fieldtrip/fieldtrip/git/refs/tags/20151205" | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.github.com/repos/fieldtrip/fieldtrip/commits?until=2015-12-06T00:00:00Z&per_page=1" | grep -m2 '"sha"';
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://raw.githubusercontent.com/fieldtrip/fieldtrip/b3909bfecc5273652756ed2e41f84e9195f96186/specest/ft_specest_mtmconvol.m > $TMPDIR/mtmconvol.m; grep -n "reqtimeboi\|prepad\|postpad\|padtype\|nan\|NaN\|endnsample\|timeboi =" $TMPDIR/mtmconvol.m | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 95,175p $TMPDIR/mtmconvol.m; sed -n 225,330p $TMPDIR/mtmconvol.m
```

```
dat = ft_preproc_polyremoval(dat, polyorder, 1, ndatsample);
end

% Determine fsample and set total time-length of data
fsample = 1./mean(diff(time));
dattime = ndatsample / fsample; % total time in seconds of input data

% Zero padding
if round(pad * fsample) < ndatsample
  error('the padding that you specified is shorter than the data');
end
if isempty(pad) % if no padding is specified padding is equal to current data length
  pad = dattime;
end
postpad    = round((pad - dattime) * fsample);
endnsample = round(pad * fsample);  % total number of samples of padded data
endtime    = pad;            % total time in seconds of padded data

% Set freqboi and freqoi
freqoiinput = freqoi;
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; C=b3909bfecc5273652756ed2e41f84e9195f96186; curl -s https://raw.githubusercontent.com/fieldtrip/fieldtrip/$C/ft_networkanalysis.m > na.m; grep -n "threshold\|degrees\|binar\|isdirected\|issymmetric\|abs(" na.m | head -40; curl -s https://raw.githubusercontent.com/fieldtrip/fieldtrip/$C/external/bct/degrees_dir.m | grep -v "^%" | head; curl -s https://raw.githubusercontent.com/fieldtrip/fieldtrip/$C/external/bct/degrees_und.m | grep -v "^%"|head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; C=b3909bfecc5273652756ed2e41f84e9195f96186; curl -s -o nb.mat -w "%{http_code} %{size_download}\n" https://raw.githubusercontent.com/fieldtrip/fieldtrip/$C/template/neighbours/biosemi64_neighb.mat; . dev/bin/activate; python -c "
import scipy.io as s; m=s.loadmat('nb.mat',squeeze_me=True); n=m['neighbours']; print(len(n)); print(n[0]); print(sum(len(x['neighblabel']) for x in n)/len(n))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
date -u; sed -n 1,80p tools/entry.py | head -80; grep -n "def cmd_\|add_parser" tools/entry.py | head -30
```

```
Mon Nov  9 19:31:13 UTC 2026
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
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "max-minutes\|max_minutes" tools/entry.py | head; grep -n "dataset the entry uses\|names the dataset" -A15 tools/entry.py | grep -n "crcns\|unversioned" | head
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
429:                   max_minutes: float) -> int:
435:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes):
463:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
492:        if ok and seconds > max_minutes * 60:
494:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
556:    parser.add_argument("--max-minutes", type=float, default=60,
592:                              args.timeout, args.max_minutes)
602:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
```

**Agent calls Bash**

```bash
mkdir -p entries/johnson-2017; date -u
```

```
Mon Nov  9 19:33:23 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/johnson-2017/frontoparietal.py",
 "content": "\"\"\"Loading and measures for Johnson et al. (2017), \"Bidirectional Frontoparietal Oscillatory\nSystems Support Working Memory\" (doi:10.1016/j.cub.2017.05.046), on CRCNS data set pfc-5\n(doi:10.6080/K0ZC811B), read as crcns:pfc-5/unversioned from the public bucket crcnsarchive.\n\nWhere each parameter comes from:\n\n- The claims file (claims/johnson-2017.yaml), \"shared methods\", gives the measures: correct\n  trials, 3-cycle Hanning windows (3/f), 10 ms steps for power and 100 ms for PSI, zero padding\n  to 7500 ms, bootstrapped Z against the pretrial baseline, PSI over 2-7 and 9-24 Hz Z scored on\n  a frequency-shuffled null, then baseline corrected, and the cluster test (independent t,\n  cluster-forming threshold 0.05 two-tailed, sum of t, 1000 shuffles).\n- The paper's own code, deposited in the data set (pfc-5/live/analysis_scripts.tar.gz, read in\n  the notebook), settles the details the claims file leaves open (the claims file allows this,\n  \"Where those scripts settle a detail named as open below, the author may follow them\"):\n  FieldTrip's biosemi64 neighbour template and minnbchan = 2 (O1; *_stat_group.m); the\n  hemisphere index as 27 left minus right channels in the code's order (O3;\n  *_stat_group_hem.m); the swap of 10 controls and the surface Laplacian already in\n  data_derived.mat (O4, O5; the data descriptor); mtmconvol and mtmfft as FieldTrip computes them\n  (tfr_compute.m, fft_compute.m, psi_compute.m); zbaseline.m draws r = the trial count of the data\n  being scored (per visual hemifield); degree as FieldTrip's ft_networkanalysis 'degrees' with\n  threshold 1.96 on the signed Z (psi_compute.m), which counts connections with Z > 1.96 in or\n  out of a channel; the PSI group test per seed channel A, clustering over neighbours of B and\n  time (psi_stat_group.m). FieldTrip's code is read at commit\n  b3909bfecc5273652756ed2e41f84e9195f96186 (the last before release 20151205, the one the paper\n  cites).\n- Assumptions (step 1.6), each stated in the notebook with every reading run:\n  * Window edges. FieldTrip's mtmconvol returns NaN wherever a 3/f window does not fit inside\n    the segment; the deposited segments have no buffers (500, 1500 and 900 ms), so below 6 Hz\n    no baseline value exists. Reading \"fit\" keeps FieldTrip's mask; reading \"pad\" keeps the\n    convolution values over the zero padding the paper names (\"zero-padded to 7,500 ms\"). The\n    two give identical values wherever the window fits.\n  * The bootstrap of zbaseline.m is replaced by its exact expectation: the mean of r draws\n    without replacement from N pooled baseline values has mean mu and standard deviation\n    sd / sqrt(r) * sqrt((N - r) / (N - 1)). This removes the Monte Carlo noise of 1000 draws.\n  * PSI. The Methods compute the cross-spectral density and PSI after Nolte et al. (2008)\n    (reading \"nolte\": coherency of the trial-averaged cross-spectrum). psianalysis.m instead\n    averages per-trial phase slopes and multiplies the Fourier coefficients without a complex\n    conjugate; reading \"trialwise\" follows its structure with the conjugate. The null shuffles\n    the frequency bins and recomputes PSI (Methods); psianalysis.m draws two independent\n    permutations, which reading \"trialwise\" follows.\n- Standard choices that cannot change a result: the random seeds; the FIR filter of the ERPs\n  (FieldTrip's default order 3 * fix(fs / 30) with a Hamming window, applied forwards and\n  backwards, to the trial average, which is the same as averaging filtered trials).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport os\nimport re\nimport tarfile\nimport urllib.request\n\nimport numpy as np\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-5/live/\"\nDATASET = \"crcns:pfc-5/unversioned\"\nDATASET_DOI = \"10.6080/K0ZC811B\"\nFIELDTRIP_COMMIT = \"b3909bfecc5273652756ed2e41f84e9195f96186\"\nNEIGHBOURS_URL = (\"https://raw.githubusercontent.com/fieldtrip/fieldtrip/\"\n                  f\"{FIELDTRIP_COMMIT}/template/neighbours/biosemi64_neighb.mat\")\n\nCONTROLS = [f\"ctrl{i:02d}\" for i in range(1, 21)]\nPATIENTS = [f\"pfc{i:02d}\" for i in range(1, 15)]\nSUBJECTS = CONTROLS + PATIENTS\n\nFS = 256.0\nPAD = 7.5                     # seconds, cfg.pad = 7.5 in every *_compute.m\nFREQS = np.arange(1, 41)      # 1 to 40 Hz (claims file, shared methods)\nBANDS = {\"dt\": np.arange(2, 8), \"ab\": np.arange(9, 25)}   # PSI bands (psi_compute.m)\n\n# Hemisphere index channels, in the order of *_stat_group_hem.m\nLEFT = ['Fp1', 'AF7', 'AF3', 'F1', 'F3', 'F5', 'F7', 'FT7', 'FC5', 'FC3', 'FC1', 'C1', 'C3', 'C5',\n        'T7', 'TP7', 'CP5', 'CP3', 'CP1', 'P1', 'P3', 'P5', 'P7', 'P9', 'PO7', 'PO3', 'O1']\nRIGHT = ['Fp2', 'AF8', 'AF4', 'F2', 'F4', 'F6', 'F8', 'FT8', 'FC6', 'FC4', 'FC2', 'C2', 'C4', 'C6',\n         'T8', 'TP8', 'CP6', 'CP4', 'CP2', 'P2', 'P4', 'P6', 'P8', 'P10', 'PO8', 'PO4', 'O2']\n\n\n# ----------------------------------------------------------------------------- reading\n\ndef fetch(name: str) -> bytes:\n    \"\"\"A small file of the data set, whole (docs, checksums, scripts).\"\"\"\n    with urllib.request.urlopen(BUCKET + name) as r:\n        return r.read()\n\n\ndef stream_subject_files(sid: str) -> dict:\n    \"\"\"Stream <sid>.tar.gz from the bucket and return data_derived.mat (bytes) and\n    summary_file_trial.csv (bytes). The tar is read as a gzip stream; the raw .bdf that comes\n    first is decompressed and skipped, never kept or written.\"\"\"\n    import fsspec\n    out = {\"members\": []}\n    with fsspec.open(BUCKET + f\"data/{sid}.tar.gz\", \"rb\", block_size=2**22) as f:\n        with tarfile.open(fileobj=f, mode=\"r|gz\") as tf:\n            for m in tf:\n                out[\"members\"].append((m.name, m.size))\n                if m.name.endswith(\"data_derived.mat\"):\n                    out[\"derived\"] = tf.extractfile(m).read()\n                elif m.name.endswith(\"summary_file_trial.csv\"):\n                    out[\"csv\"] = tf.extractfile(m).read()\n    return out\n\n\ndef read_derived(raw: bytes) -> dict:\n    \"\"\"data_derived.mat (MATLAB 7.3) into arrays: per segment, data (trials, 64, samples),\n    time, trialinfo (trials, 7), fsample; and the labels.\"\"\"\n    import h5py\n    f = h5py.File(io.BytesIO(raw), \"r\")\n    out = {}\n    for seg in (\"pretrial\", \"encmain\", \"proc\"):\n        g = f[seg]\n        refs = g[\"trial\"][()].ravel()\n        trials = [f[r][()].T for r in refs]          # stored (samples, 64): transpose\n        lens = {t.shape[1] for t in trials}\n        times = [f[r][()].ravel() for r in g[\"time\"][()].ravel()]\n        out[seg] = {\n            \"data\": np.stack(trials) if len(lens) == 1 else trials,\n            \"lengths\": sorted(lens),\n            \"time\": times[0],\n            \"time_first\": sorted({round(float(t[0]), 6) for t in times}),\n            \"trialinfo\": g[\"trialinfo\"][()].T,\n            \"fsample\": float(g[\"fsample\"][()].ravel()[0]),\n        }\n    out[\"label\"] = [\"\".join(chr(c) for c in f[r][()].ravel()) for r in f[\"encmain\"][\"label\"][()].ravel()]\n    return out\n\n\ndef read_trial_csv(raw: bytes):\n    import pandas as pd\n    cols = [\"trial\", \"correct\", \"vhf\", \"type\", \"condition\", \"jitter\", \"rt\", \"t_pre\", \"t_enc\", \"t_proc\"]\n    return pd.read_csv(io.BytesIO(raw), header=None, names=cols)\n\n\ndef neighbours(labels: list[str]) -> np.ndarray:\n    \"\"\"FieldTrip's biosemi64 neighbour template (what ft_prepare_neighbours with\n    layout biosemi64.lay and method 'template' loads), as a boolean adjacency over labels.\"\"\"\n    import scipy.io\n    with urllib.request.urlopen(NEIGHBOURS_URL) as r:\n        m = scipy.io.loadmat(io.BytesIO(r.read()), squeeze_me=True)\n    idx = {l.lower(): i for i, l in enumerate(labels)}\n    A = np.zeros((len(labels), len(labels)), bool)\n    for n in m[\"neighbours\"]:\n        a = idx.get(str(n[\"label\"]).lower())\n        if a is None:\n            continue\n        for b in np.atleast_1d(n[\"neighblabel\"]):\n            b = idx.get(str(b).lower())\n            if b is not None:\n                A[a, b] = A[b, a] = True\n    return A\n\n\n# ----------------------------------------------------------------------------- spectral\n\ndef hanning(n: int) -> np.ndarray:\n    \"\"\"MATLAB hanning(n): no zero end points.\"\"\"\n    k = np.arange(1, n + 1)\n    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))\n\n\ndef mtmconvol(x: np.ndarray, freqs, toi_step: float, fs: float = FS, pad: float = PAD):\n    \"\"\"FieldTrip ft_specest_mtmconvol (commit above) with a Hanning taper and t_ftimwin = 3/f.\n    x: (..., nsamples), demeaned first (ft_freqanalysis polyremoval 0). Returns the complex\n    spectrum (..., nfreq, ntime), the boolean mask of the points FieldTrip keeps (window inside\n    the data), and the times. Outside the mask the values are the convolution over the zero\n    padding (\"pad\" reading); FieldTrip sets them to NaN (\"fit\" reading).\"\"\"\n    x = x - x.mean(axis=-1, keepdims=True)\n    nd = x.shape[-1]\n    N = int(round(pad * fs))\n    tend = (nd - 1) / fs\n    toi = np.unique(np.round(np.arange(0, tend + 1e-9, toi_step) * fs) / fs)\n    tb = np.round(toi * fs).astype(int) + 1                      # 1-based sample of each time\n    X = np.fft.fft(x.astype(np.float64), n=N, axis=-1)\n    out = np.empty(x.shape[:-1] + (len(freqs), len(toi)), np.complex64)\n    mask = np.zeros((len(freqs), len(toi)), bool)\n    for i, f in enumerate(freqs):\n        tw = 3.0 / f\n        L = int(round(tw * fs))\n        tap = hanning(L)\n        tap = tap / np.linalg.norm(tap)\n        tappad = int(np.ceil(N / 2) - np.floor(L / 2))\n        ang = np.arange(-(L - 1) / 2, (L - 1) / 2 + 1) * (2 * np.pi / fs) * f\n        w = np.zeros(N, complex)\n        w[tappad:tappad + L] = tap * np.exp(1j * ang)\n        dum = np.fft.fftshift(np.fft.ifft(X * np.fft.fft(w), axis=-1), axes=-1)\n        out[..., i, :] = dum[..., tb - 1] * np.sqrt(2.0 / L)\n        ns = tw * fs\n        mask[i] = (tb >= ns / 2) & (tb < nd - ns / 2)\n    return out, mask, toi\n\n\ndef mtmfft_power(x: np.ndarray, freqs, fs: float = FS, pad: float = PAD) -> np.ndarray:\n    \"\"\"FieldTrip ft_specest_mtmfft, Hanning taper over the whole segment, padded to 7.5 s;\n    power |F|^2 at the requested frequencies. x: (..., nsamples).\"\"\"\n    x = x - x.mean(axis=-1, keepdims=True)\n    nd = x.shape[-1]\n    N = int(round(pad * fs))\n    tap = hanning(nd)\n    tap = tap / np.linalg.norm(tap)\n    F = np.fft.fft(x * tap, n=N, axis=-1) * np.sqrt(2.0 / nd)\n    idx = np.round(np.asarray(freqs) * pad).astype(int)\n    return np.abs(F[..., idx]) ** 2\n\n\ndef lowpass_fir(x: np.ndarray, fc: float = 30.0, fs: float = FS) -> np.ndarray:\n    \"\"\"FieldTrip's default FIR low-pass (order 3 * fix(fs / fc), fir1, two-pass), with\n    mirror padding to 7.5 s as cfg.padding = 7.5 asks.\"\"\"\n    from scipy.signal import firwin, filtfilt\n    order = 3 * int(fs // fc)\n    b = firwin(order + 1, fc / (fs / 2))\n    nd = x.shape[-1]\n    npad = max(0, (int(round(PAD * fs)) - nd) // 2)\n    xp = np.pad(x, [(0, 0)] * (x.ndim - 1) + [(npad, npad)], mode=\"reflect\") if npad < nd else \\\n        np.pad(x, [(0, 0)] * (x.ndim - 1) + [(npad, npad)], mode=\"symmetric\")\n    y = filtfilt(b, [1.0], xp, axis=-1)\n    return y[..., npad:npad + nd]\n\n\n# ----------------------------------------------------------------------------- PSI\n\ndef _perm_matrix(nf: int, n_perm: int, rng, mode: str) -> np.ndarray:\n    \"\"\"Indicator matrix (nf*nf, n_perm): which (i, j) frequency pairs enter each null PSI.\n    'adjacent': one shuffle of the bins, PSI over adjacent pairs (Methods).\n    'code': two independent shuffles, nf pairs (psianalysis.m).\"\"\"\n    P = np.zeros((nf * nf, n_perm), np.float32)\n    for p in range(n_perm):\n        if mode == \"adjacent\":\n            pi = rng.permutation(nf)\n            i, j = pi[:-1], pi[1:]\n        else:\n            i, j = rng.permutation(nf), rng.permutation(nf)\n        np.add.at(P[:, p], i * nf + j, 1.0)\n    return P\n\n\ndef _z_from_M(M: np.ndarray, obs: np.ndarray, P: np.ndarray) -> np.ndarray:\n    \"\"\"M: (rows, nf*nf) of Im(conj(C_i) C_j); obs: (rows,). Z of obs on the null M @ P\n    (MATLAB std, ddof 1).\"\"\"\n    z = np.empty(M.shape[0], np.float32)\n    step = 4096\n    for s in range(0, M.shape[0], step):\n        null = M[s:s + step] @ P\n        mu = null.mean(axis=1)\n        sd = null.std(axis=1, ddof=1)\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            z[s:s + step] = (obs[s:s + step] - mu) / sd\n    return z\n\n\ndef psi_z(F: np.ndarray, n_perm: int = 1000, seed: int = 0) -> dict:\n    \"\"\"PSI Z for every ordered channel pair and time point. F: (trials, chan, nf, nt) complex.\n    Returns {'nolte': (chan, chan, nt), 'trialwise': (chan, chan, nt)}; positive Z(a, b) means a\n    leads b (Nolte et al. 2008 sign: phase of a minus b grows with frequency... here PSI(a, b) =\n    Im sum conj(C_ab(f)) C_ab(f+1) with C_ab = <X_a conj(X_b)>).\"\"\"\n    ntr, nc, nf, nt = F.shape\n    rng = np.random.default_rng(seed)\n    P_adj = _perm_matrix(nf, n_perm, rng, \"adjacent\")\n    P_code = _perm_matrix(nf, n_perm, rng, \"code\")\n    out = {\"nolte\": np.empty((nc, nc, nt), np.float32), \"trialwise\": np.empty((nc, nc, nt), np.float32)}\n    for t in range(nt):\n        X = F[..., t].astype(np.complex128)                       # (tr, c, f)\n        # Nolte: coherency of the trial-averaged cross-spectrum\n        S = np.einsum(\"raf,rbf->abf\", X, X.conj()) / ntr\n        p = np.real(np.einsum(\"raf,raf->af\", X, X.conj())) / ntr\n        C = S / np.sqrt(p[:, None, :] * p[None, :, :])\n        M = np.imag(C.conj()[..., :, None] * C[..., None, :]).reshape(nc * nc, nf * nf).astype(np.float32)\n        obs = np.imag(C[..., :-1].conj() * C[..., 1:]).sum(-1).reshape(-1).astype(np.float32)\n        out[\"nolte\"][..., t] = _z_from_M(M, obs, P_adj).reshape(nc, nc)\n        # trialwise (psianalysis.m structure, with the conjugate)\n        Z = X / np.abs(X)\n        D = Z[..., :-1].conj() * Z[..., 1:]                       # (tr, c, f-1)\n        Dr = np.moveaxis(D, 1, -1).reshape(-1, nc)               # (tr*(f-1), c)\n        obs2 = (Dr.imag.T @ Dr.real - Dr.real.T @ Dr.imag) / ntr  # Im(d_a conj d_b)\n        pp = np.einsum(\"raf,rbf->abf\", Z, Z.conj()) / ntr\n        M2 = np.imag(pp.conj()[..., :, None] * pp[..., None, :]).reshape(nc * nc, nf * nf).astype(np.float32)\n        out[\"trialwise\"][..., t] = _z_from_M(M2, obs2.reshape(-1).astype(np.float32), P_code).reshape(nc, nc)\n    for k in out:\n        for c in range(nc):\n            out[k][c, c, :] = np.nan\n    return out\n\n\ndef psianalysis_literal_pp(Xa: np.ndarray, Xb: np.ndarray) -> np.ndarray:\n    \"\"\"The normalised cross-spectrum of psianalysis.m for one trial, as written: csd = X_a .* X_b\n    (no conjugate), divided by sqrt(diag(cs) * diag(cs)') where ' is MATLAB's conjugate\n    transpose.\"\"\"\n    return (Xa * Xb) / np.sqrt((Xa * Xa) * np.conj(Xb * Xb))\n\n\n# ----------------------------------------------------------------------------- per subject\n\ndef process_subject(sid: str, n_perm_psi: int = 1000) -> dict:\n    \"\"\"Stream one subject and reduce it to what the claims use. Everything returned is small.\"\"\"\n    os.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\n    files = stream_subject_files(sid)\n    raw = files[\"derived\"]\n    d = read_derived(raw)\n    csv = read_trial_csv(files[\"csv\"])\n    res = {\"sid\": sid, \"members\": files[\"members\"], \"derived_md5\": hashlib.md5(raw).hexdigest(),\n           \"csv\": csv, \"label\": d[\"label\"]}\n    for seg in (\"pretrial\", \"encmain\", \"proc\"):\n        res[f\"{seg}_lengths\"] = d[seg][\"lengths\"]\n        res[f\"{seg}_trialinfo\"] = d[seg][\"trialinfo\"]\n        res[f\"{seg}_fsample\"] = d[seg][\"fsample\"]\n        res[f\"{seg}_time_first\"] = d[seg][\"time_first\"]\n    ti = d[\"encmain\"][\"trialinfo\"]\n    # align proc to encmain by trial number (proc is stored in another order)\n    order = {int(t): i for i, t in enumerate(d[\"proc\"][\"trialinfo\"][:, 0])}\n    pidx = np.array([order[int(t)] for t in ti[:, 0]])\n    pre = d[\"pretrial\"][\"data\"].astype(np.float64)\n    enc = d[\"encmain\"][\"data\"].astype(np.float64)\n    proc = d[\"proc\"][\"data\"].astype(np.float64)\n    proc_al = proc[pidx]\n    correct = ti[:, 1] == 1\n    hemi = ti[:, 2].astype(int)          # 1 intact, 2 lesioned (descriptor)\n    res[\"n_trials\"] = len(ti)\n    # fingerprint and Laplacian check\n    res[\"fingerprint\"] = float(np.abs(enc[0]).sum())\n    A = neighbours(d[\"label\"])\n    cc = np.corrcoef(enc[:, :, :].transpose(1, 0, 2).reshape(64, -1))\n    res[\"neighbour_corr\"] = float(np.nanmean(cc[A]))\n    # ---------------- ERP\n    base = lowpass_fir(pre[correct].mean(0)).mean(-1)\n    res[\"erp_base\"] = base.astype(np.float32)\n    for h in (1, 2):\n        sel = correct & (hemi == h)\n        res[f\"erp_enc_{h}\"] = (lowpass_fir(enc[sel].mean(0)) - base[:, None]).astype(np.float32)\n        res[f\"erp_proc_{h}\"] = (lowpass_fir(proc_al[sel].mean(0)) - base[:, None]).astype(np.float32)\n        # the code's selection: encmain indices applied to proc in its stored order\n        res[f\"erp_proc_codeidx_{h}\"] = (lowpass_fir(proc[sel].mean(0)) - base[:, None]).astype(np.float32)\n    # ---------------- baseline FFT, all trials\n    res[\"fft\"] = mtmfft_power(pre, FREQS).mean(0).astype(np.float32)\n    # ---------------- TFR power, correct trials\n    Fp, mp, tp = mtmconvol(pre[correct], FREQS, 0.01)\n    Pp = np.abs(Fp) ** 2                                         # (tr, ch, f, t)\n    del Fp\n    res[\"tfr_pre_time\"] = tp\n    for rd, m in ((\"pad\", np.ones_like(mp)), (\"fit\", mp)):\n        vals = np.where(m[None, None], Pp, np.nan)\n        n = np.sum(m, axis=-1) * Pp.shape[0]                     # per freq\n        res[f\"tfr_base_mu_{rd}\"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)\n        res[f\"tfr_base_sd_{rd}\"] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32) if n.max() > 1 else None\n        res[f\"tfr_base_N_{rd}\"] = n\n    del Pp\n    res[\"n_correct\"] = int(correct.sum())\n    for seg, x in ((\"enc\", enc), (\"proc\", proc_al)):\n        for h in (1, 2):\n            sel = correct & (hemi == h)\n            F, m, tt = mtmconvol(x[sel], FREQS, 0.01)\n            res[f\"tfr_{seg}_{h}\"] = (np.abs(F) ** 2).mean(0).astype(np.float32)\n            res[f\"tfr_{seg}_mask\"] = m\n            res[f\"tfr_{seg}_time\"] = tt\n            res[f\"n_{seg}_{h}\"] = int(sel.sum())\n            del F\n    res[\"tfr_pre_mask\"] = mp\n    # ---------------- PSI, correct trials, trial mean subtracted (subtracterp.m)\n    for band, fr in BANDS.items():\n        x = pre[correct] - pre[correct].mean(0)\n        F, m, tt = mtmconvol(x, fr, 0.1)\n        res[f\"psi_{band}_pre_mask\"] = m\n        res[f\"psi_{band}_pre_time\"] = tt\n        z = psi_z(F, n_perm_psi, seed=1)\n        for k, v in z.items():\n            res[f\"psi_{band}_pre_{k}\"] = v\n        for seg, xx in ((\"enc\", enc), (\"proc\", proc_al)):\n            for h in (1, 2):\n                sel = correct & (hemi == h)\n                x = xx[sel] - xx[sel].mean(0)\n                F, m, tt = mtmconvol(x, fr, 0.1)\n                res[f\"psi_{band}_{seg}_mask\"] = m\n                res[f\"psi_{band}_{seg}_time\"] = tt\n                z = psi_z(F, n_perm_psi, seed=2 + h)\n                for k, v in z.items():\n                    res[f\"psi_{band}_{seg}_{h}_{k}\"] = v\n    return res\n\n\n# ----------------------------------------------------------------------------- cluster test\n\ndef _label(mask: np.ndarray, edges: np.ndarray):\n    \"\"\"Connected components of mask (nodes, *grid): face connectivity along the grid axes,\n    and between nodes joined by `edges` (E, 2) at the same grid point.\"\"\"\n    from scipy import ndimage\n    from scipy.sparse import coo_matrix\n    from scipy.sparse.csgraph import connected_components\n    st = np.zeros((3,) * mask.ndim, bool)\n    c = (1,) * mask.ndim\n    st[c] = True\n    for ax in range(1, mask.ndim):\n        for o in (0, 2):\n            idx = list(c)\n            idx[ax] = o\n            st[tuple(idx)] = True\n    lab, n = ndimage.label(mask, structure=st)\n    if n == 0:\n        return lab, 0\n    if len(edges):\n        L1 = lab[edges[:, 0]].reshape(len(edges), -1)\n        L2 = lab[edges[:, 1]].reshape(len(edges), -1)\n        both = (L1 > 0) & (L2 > 0)\n        a, b = L1[both], L2[both]\n        if a.size:\n            g = coo_matrix((np.ones(a.size), (a, b)), shape=(n + 1, n + 1))\n            _, comp = connected_components(g, directed=False)\n            remap = comp\n            # component ids: relabel to 1..k keeping 0 as background\n            u, inv = np.unique(remap[1:], return_inverse=True)\n            newid = np.concatenate([[0], inv + 1])\n            lab = newid[lab]\n            n = len(u)\n    return lab, n\n\n\ndef cluster_test(x1: np.ndarray, x2: np.ndarray, adjacency: np.ndarray | None, n_perm: int = 1000,\n                 alpha: float = 0.05, minnbchan: int = 2, seed: int = 0) -> dict:\n    \"\"\"FieldTrip ft_*statistics, montecarlo with cluster correction as the paper's scripts\n    set it: ft_statfun_indepsamplesT (group 1 minus group 2), clusteralpha 0.05 two-tailed,\n    maxsum, 1000 shuffles, correcttail 'prob' (p doubled), minnbchan. x1: (n1, nodes, *grid),\n    x2: (n2, nodes, *grid). adjacency: (nodes, nodes) boolean or None (no spatial\n    clustering). NaN points are left out of every cluster.\"\"\"\n    from scipy import stats\n    n1, n2 = len(x1), len(x2)\n    X = np.concatenate([x1, x2]).astype(np.float64)\n    shape = X.shape[1:]\n    Xf = X.reshape(len(X), -1)\n    valid = np.all(np.isfinite(Xf), axis=0)\n    Xf = np.where(valid, Xf, 0.0)\n    df = n1 + n2 - 2\n    crit = stats.t.ppf(1 - alpha / 2, df)\n    if adjacency is not None:\n        edges = np.argwhere(np.triu(adjacency, 1))\n        A = adjacency.astype(np.float32)\n    else:\n        edges = np.zeros((0, 2), int)\n        A = None\n    S1, S2 = Xf, Xf ** 2\n\n    def tstat(g):            # g: (k, n) boolean group-1 membership\n        g = g.astype(np.float64)\n        s1 = g @ S1\n        q1 = g @ S2\n        s2 = S1.sum(0) - s1\n        q2 = S2.sum(0) - q1\n        m1, m2 = s1 / n1, s2 / n2\n        v1 = (q1 - n1 * m1 ** 2) / (n1 - 1)\n        v2 = (q2 - n2 * m2 ** 2) / (n2 - 1)\n        sp = ((n1 - 1) * v1 + (n2 - 1) * v2) / df\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            t = (m1 - m2) / np.sqrt(sp * (1 / n1 + 1 / n2))\n        t[:, ~valid] = 0.0\n        return np.nan_to_num(t)\n\n    def clusters(t):\n        t = t.reshape(shape)\n        res = []\n        for sign in (1, -1):\n            m = (sign * t) > crit\n            if A is not None and minnbchan > 0:\n                cnt = np.tensordot(A, m.astype(np.float32), axes=(1, 0))\n                m = m & (cnt >= minnbchan)\n            lab, n = _label(m, edges)\n            if n:\n                sums = np.bincount(lab.ravel(), weights=t.ravel(), minlength=n + 1)[1:]\n            else:\n                sums = np.zeros(0)\n            res.append((lab, sums))\n        return res\n\n    g0 = np.zeros((1, n1 + n2), bool)\n    g0[0, :n1] = True\n    t_obs = tstat(g0)[0]\n    (labp, sp_), (labn, sn_) = clusters(t_obs)\n    rng = np.random.default_rng(seed)\n    maxp = np.zeros(n_perm)\n    maxn = np.zeros(n_perm)\n    chunk = 50\n    for s in range(0, n_perm, chunk):\n        k = min(chunk, n_perm - s)\n        G = np.zeros((k, n1 + n2), bool)\n        for i in range(k):\n            G[i, rng.permutation(n1 + n2)[:n1]] = True\n        T = tstat(G)\n        for i in range(k):\n            (_, a), (_, b) = clusters(T[i])\n            maxp[s + i] = a.max() if a.size else 0.0\n            maxn[s + i] = b.min() if b.size else 0.0\n    out = {\"t\": t_obs.reshape(shape), \"crit\": crit, \"clusters\": [], \"valid\": valid.reshape(shape)}\n    for sign, lab, sums, null in ((1, labp, sp_, maxp), (-1, labn, sn_, maxn)):\n        for i, sm in enumerate(sums):\n            p = np.mean(null >= sm) if sign > 0 else np.mean(null <= sm)\n            out[\"clusters\"].append({\"sign\": sign, \"stat\": float(sm), \"p\": float(min(1.0, 2 * p)),\n                                    \"mask\": lab == i + 1})\n    out[\"clusters\"].sort(key=lambda c: c[\"p\"])\n    return out\n\n\ndef pair_adjacency(adj: np.ndarray, mode: str):\n    \"\"\"Adjacency over ordered channel pairs (a, b), a != b, for the PSI group test.\n    mode 'pairs': (a, b) ~ (a', b') when a and a' are equal or neighbours and so are b and b'.\n    mode 'seed': (a, b) ~ (a, b') when b and b' are neighbours (psi_stat_group.m, per seed a).\n    Returns (pairs (P, 2), adjacency (P, P) boolean).\"\"\"\n    nc = len(adj)\n    pairs = np.array([(a, b) for a in range(nc) for b in range(nc) if a != b])\n    idx = -np.ones((nc, nc), int)\n    idx[pairs[:, 0], pairs[:, 1]] = np.arange(len(pairs))\n    near = adj | np.eye(nc, dtype=bool)\n    P = np.zeros((len(pairs), len(pairs)), bool)\n    for k, (a, b) in enumerate(pairs):\n        if mode == \"pairs\":\n            aa = np.flatnonzero(near[a])\n            bb = np.flatnonzero(near[b])\n            j = idx[np.ix_(aa, bb)].ravel()\n        else:\n            j = idx[a, np.flatnonzero(adj[b])]\n        j = j[(j >= 0) & (j != k)]\n        P[k, j] = True\n    P = P | P.T\n    return pairs, P\n"
}
```

```
File created successfully at: entries/johnson-2017/frontoparietal.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/johnson-2017 && python3 - <<'EOF'
import re
s=open('frontoparietal.py').read()
s=s.replace('''def cluster_test(x1: np.ndarray, x2: np.ndarray, adjacency: np.ndarray | None, n_perm: int = 1000,
                 alpha: float = 0.05, minnbchan: int = 2, seed: int = 0) -> dict:''','''def cluster_test(x1: np.ndarray, x2: np.ndarray, adjacency, n_perm: int = 1000,
                 alpha: float = 0.05, minnbchan: int = 2, seed: int = 0, node_groups=None) -> dict:''')
s=s.replace('''    clustering). NaN points are left out of every cluster."""''','''    clustering), dense or scipy.sparse. node_groups: optional integer group of each node; each
    group is then a separate test with its own maximum (psi_stat_group.m tests each seed channel
    on its own). NaN points are left out of every cluster."""
    from scipy import sparse''')
s=s.replace('''    if adjacency is not None:
        edges = np.argwhere(np.triu(adjacency, 1))
        A = adjacency.astype(np.float32)
    else:''','''    if adjacency is not None:
        A = sparse.csr_matrix(adjacency, dtype=np.float32)
        tri = sparse.triu(A, 1).tocoo()
        edges = np.stack([tri.row, tri.col], 1)
    else:''')
s=s.replace('''                cnt = np.tensordot(A, m.astype(np.float32), axes=(1, 0))
                m = m & (cnt >= minnbchan)''','''                cnt = (A @ m.reshape(m.shape[0], -1).astype(np.float32)).reshape(m.shape)
                m = m & (cnt >= minnbchan)''')
s=s.replace('''            if n:
                sums = np.bincount(lab.ravel(), weights=t.ravel(), minlength=n + 1)[1:]
            else:
                sums = np.zeros(0)
            res.append((lab, sums))''','''            if n:
                sums = np.bincount(lab.ravel(), weights=t.ravel(), minlength=n + 1)[1:]
                if groups is not None:
                    first = np.zeros(n + 1, int)
                    first[lab.ravel()] = node_of.ravel()
                    grp = groups[first[1:]]
                else:
                    grp = np.zeros(n, int)
            else:
                sums, grp = np.zeros(0), np.zeros(0, int)
            res.append((lab, sums, grp))''')
s=s.replace('''    g0 = np.zeros((1, n1 + n2), bool)''','''    groups = None if node_groups is None else np.asarray(node_groups)
    node_of = np.broadcast_to(np.arange(shape[0]).reshape((-1,) + (1,) * (len(shape) - 1)), shape)
    ng = 1 if groups is None else int(groups.max()) + 1
    g0 = np.zeros((1, n1 + n2), bool)''')
s=s.replace('''    (labp, sp_), (labn, sn_) = clusters(t_obs)
    rng = np.random.default_rng(seed)
    maxp = np.zeros(n_perm)
    maxn = np.zeros(n_perm)''','''    (labp, sp_, gp_), (labn, sn_, gn_) = clusters(t_obs)
    rng = np.random.default_rng(seed)
    maxp = np.zeros((n_perm, ng))
    maxn = np.zeros((n_perm, ng))''')
s=s.replace('''            (_, a), (_, b) = clusters(T[i])
            maxp[s + i] = a.max() if a.size else 0.0
            maxn[s + i] = b.min() if b.size else 0.0''','''            (_, a, ga), (_, b, gb) = clusters(T[i])
            if a.size:
                np.maximum.at(maxp[s + i], ga, a)
            if b.size:
                np.minimum.at(maxn[s + i], gb, b)''')
s=s.replace('''    for sign, lab, sums, null in ((1, labp, sp_, maxp), (-1, labn, sn_, maxn)):
        for i, sm in enumerate(sums):
            p = np.mean(null >= sm) if sign > 0 else np.mean(null <= sm)
            out["clusters"].append({"sign": sign, "stat": float(sm), "p": float(min(1.0, 2 * p)),
                                    "mask": lab == i + 1})''','''    for sign, lab, sums, grp, null in ((1, labp, sp_, gp_, maxp), (-1, labn, sn_, gn_, maxn)):
        for i, sm in enumerate(sums):
            nl = null[:, grp[i]]
            p = np.mean(nl >= sm) if sign > 0 else np.mean(nl <= sm)
            out["clusters"].append({"sign": sign, "stat": float(sm), "p": float(min(1.0, 2 * p)),
                                    "group": int(grp[i]), "mask": lab == i + 1})''')
open('frontoparietal.py','w').write(s)
EOF
grep -n "tfr_base_sd" frontoparietal.py
```

```
343:        res[f"tfr_base_sd_{rd}"] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32) if n.max() > 1 else None
```

**Agent calls Bash**

```bash
sed -i 's/        res\[f"tfr_base_sd_{rd}"\] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32) if n.max() > 1 else None/        with np.errstate(invalid="ignore", divide="ignore"):\n            res[f"tfr_base_sd_{rd}"] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32)/' frontoparietal.py && sed -n 336,348p frontoparietal.py && . $TMPDIR/dev/bin/activate && python - <<'EOF'
import numpy as np, frontoparietal as fp
rng=np.random.default_rng(0)
# PSI sign: a leads b by 20 ms
ntr, n = 60, 385
src = rng.standard_normal((ntr, n+20))
from scipy.signal import butter, filtfilt
b,a = butter(3,[2/128,8/128],'band'); src=filtfilt(b,a,src)
xa = src[:, 20:] ; xb = src[:, :-20]   # xb(t) = src(t), xa(t)=src(t+20): a is ahead -> a leads
x = np.stack([xa, xb + 0.3*rng.standard_normal(xb.shape), rng.standard_normal(xb.shape)], 1)
F, m, tt = fp.mtmconvol(x - x.mean(0), fp.BANDS['dt'], 0.1)
z = fp.psi_z(F, 200)
print('mask', m.sum(1)); print('nolte Z(a,b)', np.round(z['nolte'][0,1],1)); print('trialwise', np.round(z['trialwise'][0,1],1)); print('a,noise', np.round(z['nolte'][0,2],1))
# literal code pp
Xa, Xb = F[0,0,:,8], F[0,1,:,8]
pp = fp.psianalysis_literal_pp(Xa, Xb); print('literal pp', np.round(pp,3), 'vs exp(2i phase b)', np.round(np.exp(2j*np.angle(Xb)),3))
# cluster test synthetic
x1 = rng.standard_normal((20, 27, 50)); x2 = rng.standard_normal((14, 27, 50)); x2[:, 3:8, 10:30] += 1.2
labels=fp.LEFT
import time; t=time.time()
A = fp.neighbours(labels)
r = fp.cluster_test(x1, x2, A, n_perm=200)
print(time.time()-t, [(c['sign'], round(c['p'],3), c['mask'].sum()) for c in r['clusters'][:3]])
EOF
```

```
Pp = np.abs(Fp) ** 2                                         # (tr, ch, f, t)
    del Fp
    res["tfr_pre_time"] = tp
    for rd, m in (("pad", np.ones_like(mp)), ("fit", mp)):
        vals = np.where(m[None, None], Pp, np.nan)
        n = np.sum(m, axis=-1) * Pp.shape[0]                     # per freq
        res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
        with np.errstate(invalid="ignore", divide="ignore"):
            res[f"tfr_base_sd_{rd}"] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32)
        res[f"tfr_base_N_{rd}"] = n
    del Pp
    res["n_correct"] = int(correct.sum())
    for seg, x in (("enc", enc), ("proc", proc_al)):
mask [ 0  5  8 10 10 10]
nolte Z(a,b) [1.7 2.  2.2 2.2 2.2 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3]
trialwise [ -1.9 -12.6   1.3   2.6   1.9   3.2   2.7   3.4   2.7   1.4   2.8   2.8
   2.3   2.8   4.7   5.6]
a,noise [ 0.5  0.   0.2  1.3  1.9 -0.6 -0.4  1.7  2.2  2.3 -0.1 -1.3 -0.9 -0.9
  1.   1.1]
literal pp [-0.458-0.889j -0.594+0.805j -0.078+0.997j  0.747+0.665j  0.681+0.732j
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python - <<'EOF'
import time, resource, numpy as np, frontoparietal as fp
t=time.time()
r = fp.process_subject('pfc02')
print('time', time.time()-t, 'maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
for k,v in r.items():
    if isinstance(v,np.ndarray): print(k, v.shape, v.dtype, np.nanmin(v) if v.dtype!=bool else v.sum(), np.nanmax(v) if v.dtype!=bool else '')
    elif k!='csv': print(k, v if not isinstance(v,list) or len(v)<10 else len(v))
import pickle; pickle.dump(r, open('/tmp/claude/pfc02.pkl','wb')) if False else None
EOF
```

```
entries/johnson-2017/frontoparietal.py:342: RuntimeWarning: Mean of empty slice
  res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
time 70.81725525856018 maxrss MB 940.67578125
sid pfc02
members [('pfc02', 0), ('pfc02/data_primary.bdf', 392915456), ('pfc02/data_derived.mat', 42137319), ('pfc02/summary_file_trial.csv', 5212)]
derived_md5 1a5fae25c968c82d3705eecfb27aef78
label 64
pretrial_lengths [129]
pretrial_trialinfo (108, 7) float64 0.0 6943.0
pretrial_fsample 255.64295676429566
pretrial_time_first [0.0]
encmain_lengths [385]
encmain_trialinfo (108, 7) float64 0.0 6943.0
encmain_fsample 256.0
encmain_time_first [0.0]
proc_lengths [231]
proc_trialinfo (108, 7) float64 0.0 6943.0
proc_fsample 256.0
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='frontoparietal.py'
s=open(p).read()
s=s.replace('''    out = {"nolte": np.empty((nc, nc, nt), np.float32), "trialwise": np.empty((nc, nc, nt), np.float32)}''','''    out = {k: np.empty((nc, nc, nt), np.float32) for k in ("nolte", "trialwise", "literal")}''')
s=s.replace('''        out["trialwise"][..., t] = _z_from_M(M2, obs2.reshape(-1).astype(np.float32), P_code).reshape(nc, nc)
''','''        out["trialwise"][..., t] = _z_from_M(M2, obs2.reshape(-1).astype(np.float32), P_code).reshape(nc, nc)
        # literal psianalysis.m: no conjugate in the cross-spectrum
        Xs = X.astype(np.complex64)
        U = psianalysis_literal_pp(Xs[:, :, None, :], Xs[:, None, :, :])   # (tr, a, b, f)
        obs3 = np.imag(U[..., :-1].conj() * U[..., 1:]).sum(-1).mean(0)
        pp3 = U.mean(0)
        del U
        M3 = np.imag(pp3.conj()[..., :, None] * pp3[..., None, :]).reshape(nc * nc, nf * nf).astype(np.float32)
        out["literal"][..., t] = _z_from_M(M3, obs3.reshape(-1).astype(np.float32), P_code).reshape(nc, nc)
''')
s=s.replace('''    Returns {'nolte': (chan, chan, nt), 'trialwise': (chan, chan, nt)}; positive Z(a, b) means a
    leads b (Nolte et al. 2008 sign: phase of a minus b grows with frequency... here PSI(a, b) =
    Im sum conj(C_ab(f)) C_ab(f+1) with C_ab = <X_a conj(X_b)>).""",''','''    Returns {'nolte', 'trialwise', 'literal'}, each (chan, chan, nt). PSI(a, b) = Im sum_f
    conj(C_ab(f)) C_ab(f+1) with C_ab built from X_a conj(X_b), so positive Z(a, b) means a leads
    b (Nolte et al. 2008). 'literal' is psianalysis.m as written (see psianalysis_literal_pp)."""''')
s=s.replace('''    Returns {'nolte': (chan, chan, nt), 'trialwise': (chan, chan, nt)}; positive Z(a, b) means a
    leads b (Nolte et al. 2008 sign: phase of a minus b grows with frequency... here PSI(a, b) =
    Im sum conj(C_ab(f)) C_ab(f+1) with C_ab = <X_a conj(X_b)>)."""''','''    Returns {'nolte', 'trialwise', 'literal'}, each (chan, chan, nt). PSI(a, b) = Im sum_f
    conj(C_ab(f)) C_ab(f+1) with C_ab built from X_a conj(X_b), so positive Z(a, b) means a leads
    b (Nolte et al. 2008). 'literal' is psianalysis.m as written (see psianalysis_literal_pp)."""''')
s += '''

def process_all(subjects=SUBJECTS, workers: int = 4) -> dict:
    """process_subject for every subject, a few at a time (each worker holds one subject)."""
    from concurrent.futures import ProcessPoolExecutor
    for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[v] = "1"
    with ProcessPoolExecutor(workers) as ex:
        return dict(zip(subjects, ex.map(process_subject, subjects)))
'''
open(p,'w').write(s)
EOF
grep -n "literal" frontoparietal.py | head
```

```
253:    Returns {'nolte', 'trialwise', 'literal'}, each (chan, chan, nt). PSI(a, b) = Im sum_f
255:    b (Nolte et al. 2008). 'literal' is psianalysis.m as written (see psianalysis_literal_pp)."""
260:    out = {k: np.empty((nc, nc, nt), np.float32) for k in ("nolte", "trialwise", "literal")}
278:        # literal psianalysis.m: no conjugate in the cross-spectrum
280:        U = psianalysis_literal_pp(Xs[:, :, None, :], Xs[:, None, :, :])   # (tr, a, b, f)
285:        out["literal"][..., t] = _z_from_M(M3, obs3.reshape(-1).astype(np.float32), P_code).reshape(nc, nc)
292:def psianalysis_literal_pp(Xa: np.ndarray, Xb: np.ndarray) -> np.ndarray:
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, pickle, resource, frontoparietal as fp, os
t=time.time()
R = fp.process_all(workers=4)
print('time', time.time()-t)
pickle.dump(R, open(os.environ['TMPDIR']+'/all.pkl','wb'))
print('saved', os.path.getsize(os.environ['TMPDIR']+'/all.pkl')/1e6, 'MB')
EOF
date -u
```

```
Mon Nov  9 19:37:28 UTC 2026
entries/johnson-2017/frontoparietal.py:350: RuntimeWarning: Mean of empty slice
  res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/johnson-2017/frontoparietal.py:350: RuntimeWarning: Mean of empty slice
  res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/johnson-2017/frontoparietal.py:350: RuntimeWarning: Mean of empty slice
  res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/johnson-2017/frontoparietal.py:350: RuntimeWarning: Mean of empty slice
  res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='frontoparietal.py'
s=open(p).read()
s=s.replace('''                elif m.name.endswith("summary_file_trial.csv"):
                    out["csv"] = tf.extractfile(m).read()''','''                elif "summary_file_trial" in m.name and m.isfile():
                    out.setdefault("csv_all", []).append((m.name, tf.extractfile(m).read()))
    if out.get("csv_all"):
        out["csv"] = sorted(out["csv_all"])[0][1]''')
s=s.replace('''    csv = read_trial_csv(files["csv"])''','''    csv = read_trial_csv(files["csv"]) if "csv" in files else None''')
s=s.replace('''def process_all(subjects=SUBJECTS, workers: int = 4) -> dict:
    """process_subject for every subject, a few at a time (each worker holds one subject)."""
    from concurrent.futures import ProcessPoolExecutor
    for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[v] = "1"
    with ProcessPoolExecutor(workers) as ex:
        return dict(zip(subjects, ex.map(process_subject, subjects)))''','''def _safe(sid):
    try:
        return process_subject(sid)
    except Exception as e:          # reported, not hidden: the notebook prints every failure
        return {"sid": sid, "error": repr(e)}


def process_all(subjects=SUBJECTS, workers: int = 4, done=None) -> dict:
    """process_subject for every subject, a few at a time (each worker holds one subject).
    A subject that fails is returned with its error. `done` is called with each result."""
    from concurrent.futures import ProcessPoolExecutor, as_completed
    for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[v] = "1"
    out = {}
    with ProcessPoolExecutor(workers) as ex:
        futs = {ex.submit(_safe, s): s for s in subjects}
        for f in as_completed(futs):
            r = f.result()
            out[futs[f]] = r
            if done:
                done(r)
    return {s: out[s] for s in subjects}''')
s=s.replace('''        res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
        with np.errstate(invalid="ignore", divide="ignore"):
            res[f"tfr_base_sd_{rd}"] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32)''','''        with np.errstate(invalid="ignore", divide="ignore"), warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)   # no baseline value below 6 Hz under "fit"
            res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
            res[f"tfr_base_sd_{rd}"] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32)''')
s=s.replace("import urllib.request\n","import urllib.request\nimport warnings\n",1)
open(p,'w').write(s)
EOF
cat > $TMPDIR/runall.py <<'EOF'
import os, pickle, time, sys
sys.path.insert(0, 'entries/johnson-2017')
import frontoparietal as fp
d = os.environ['TMPDIR'] + '/subj'; os.makedirs(d, exist_ok=True)
todo = [s for s in fp.SUBJECTS if not os.path.exists(f'{d}/{s}.pkl')]
t = time.time()
def done(r):
    if 'error' in r: print('ERROR', r['sid'], r['error'], flush=True); return
    pickle.dump(r, open(f"{d}/{r['sid']}.pkl", 'wb')); print(r['sid'], round(time.time()-t), [m for m in r['members']], flush=True)
fp.process_all(todo, workers=4, done=done)
print('total', time.time()-t)
EOF
date -u
```

```
Mon Nov  9 19:55:38 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python $TMPDIR/runall.py 2>&1 | grep -v Warning | grep -v "var = nanvar"; date -u
```

```
ctrl02 209 [('ctrl02', 0), ('ctrl02/data_primary.bdf', 570526208), ('ctrl02/channel_replace.txt', 43), ('ctrl02/data_derived.mat', 50148409), ('ctrl02/summary_file_trial.csv', 6706)]
ctrl01 225 [('ctrl01', 0), ('ctrl01/data_primary.bdf', 587569664), ('ctrl01/channel_replace.txt', 43), ('ctrl01/data_derived.mat', 60666344), ('ctrl01/summary_file_trial.csv', 8236)]
ctrl03 229 [('ctrl03', 0), ('ctrl03/data_primary.bdf', 576805376), ('ctrl03/data_derived.mat', 65774132), ('ctrl03/summary_file_trial.csv', 7870)]
ctrl04 266 [('ctrl04', 0), ('ctrl04/data_primary.bdf', 680411648), ('ctrl04/data_derived.mat', 82057426), ('ctrl04/summary_file_trial.csv', 9737)]
ctrl05 465 [('ctrl05', 0), ('ctrl05/data_primary.bdf', 668750336), ('ctrl05/data_derived.mat', 81316672), ('ctrl05/summary_file_trial.csv', 10065)]
ctrl06 494 [('ctrl06', 0), ('ctrl06/data_primary.bdf', 709116416), ('ctrl06/data_derived.mat', 73202433), ('ctrl06/summary_file_trial.csv', 8723)]
ctrl07 504 [('ctrl07', 0), ('ctrl07/data_primary.bdf', 640494080), ('ctrl07/data_derived.mat', 84572557), ('ctrl07/summary_file_trial.csv', 9692)]
ctrl08 524 [('ctrl08', 0), ('ctrl08/data_primary_1.bdf', 276975104), ('ctrl08/data_primary_2.bdf', 557743616), ('ctrl08/summary_file_trial_2.csv', 5070), ('ctrl08/data_derived.mat', 70045230), ('ctrl08/summary_file_trial_1.csv', 6069)]
ctrl11 692 [('ctrl11', 0), ('ctrl11/data_primary.bdf', 572320256), ('ctrl11/channel_replace.txt', 61), ('ctrl11/data_derived.mat', 56498249), ('ctrl11/summary_file_trial.csv', 7005)]
ctrl10 776 [('ctrl10', 0), ('ctrl10/data_primary.bdf', 694315520), ('ctrl10/data_derived.mat', 83394118), ('ctrl10/summary_file_trial.csv', 9755)]
ctrl09 795 [('ctrl09', 0), ('ctrl09/data_primary.bdf', 981138944), ('ctrl09/data_derived.mat', 91017404), ('ctrl09/summary_file_trial.csv', 10871)]
ctrl12 805 [('ctrl12', 0), ('ctrl12/data_primary.bdf', 790745600), ('ctrl12/data_derived.mat', 80206307), ('ctrl12/summary_file_trial.csv', 9848)]
ctrl13 861 [('ctrl13', 0), ('ctrl13/d
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python - <<'EOF'
import time, numpy as np, frontoparietal as fp
rng=np.random.default_rng(0)
x=rng.standard_normal((95,64,385))
t=time.time(); F,m,tt=fp.mtmconvol(x, fp.FREQS, 0.01); print('tfr enc 1 hemi', time.time()-t)
t=time.time(); F,m,tt=fp.mtmconvol(x, fp.BANDS['ab'], 0.1); print('conv ab', time.time()-t)
import cProfile, pstats
t=time.time(); z=fp.psi_z(F[..., :4], 1000); print('psi ab 4 timepoints', time.time()-t)
cProfile.run("fp.psi_z(F[..., :2], 1000)", '/tmp/claude-1001/prof')
pstats.Stats('/tmp/claude-1001/prof').sort_stats('cumtime').print_stats(12)
EOF
```

```
tfr enc 1 hemi 5.733212232589722
conv ab 2.1795477867126465
psi ab 4 timepoints 2.0032401084899902
Mon Nov  9 20:32:37 2026    /tmp/claude-1001/prof

         8431 function calls in 1.009 seconds

   Ordered by: cumulative time
   List reduced from 55 to 12 due to restriction <12>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.009    1.009 {built-in method builtins.exec}
        1    0.001    0.001    1.009    1.009 <string>:1(<module>)
        1    0.035    0.035    1.008    1.008 entries/johnson-2017/frontoparietal.py:254(psi_z)
        2    0.641    0.320    0.641    0.320 entries/johnson-2017/frontoparietal.py:295(psianalysis_literal_pp)
        6    0.137    0.023    0.176    0.029 entries/johnson-2017/frontoparietal.py:240(_z_from_M)
        6    0.000    0.000    0.078    0.013 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/einsumfunc.py:1242(einsum)
        6    0.078    0.013    0.078    0.013 {built-in method numpy._core._multiarray_umath.c_einsum}
       26    0.048    0.002    0.048    0.002 {method 'reduce' of 'numpy.ufunc' objects}
        6    0.000    0.000    0.031    0.005 {method 'std' of 'numpy.ndarray' objects}
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, frontoparietal as fp
t=time.time(); r=fp.stream_subject_files('pfc02'); print('fsspec', time.time()-t)
EOF
```

```
fsspec 34.623074531555176
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='frontoparietal.py'
s=open(p).read()
s=s.replace('''    first is decompressed and skipped, never kept or written."""
    import fsspec
    out = {"members": []}
    with fsspec.open(BUCKET + f"data/{sid}.tar.gz", "rb", block_size=2**22) as f:''','''    first is decompressed and skipped, never kept or written. A tar.gz can only be read in
    order, so it is read as one HTTP stream (urllib), not with fsspec's range requests, which
    were four times slower here (35 s against 9 s for pfc02)."""
    out = {"members": []}
    with urllib.request.urlopen(BUCKET + f"data/{sid}.tar.gz") as f:''')
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import pickle, os, numpy as np, glob
d=os.environ['TMPDIR']+'/subj'
R={os.path.basename(f)[:-4]: pickle.load(open(f,'rb')) for f in sorted(glob.glob(d+'/*.pkl'))}
lab=R['ctrl01']['label']; L={l:i for i,l in enumerate(lab)}
pfc=[L[c] for c in ['AF7','F5','F7','FC5','FT7']]; po=[L[c] for c in ['P1','P3','P5','P7','P9','PO3','PO7','O1']]
for band in ['dt','ab']:
  for rd in ['nolte','trialwise','literal']:
    for grp in ['ctrl','pfc']:
      for h in [2,1]:
        rows=[]
        for s,r in R.items():
            if not s.startswith(grp): continue
            base=np.nanmean(r[f'psi_{band}_pre_{rd}'],axis=-1)
            e=r[f'psi_{band}_enc_{h}_{rd}']-base[...,None]; p=r[f'psi_{band}_proc_{h}_{rd}']-base[...,None]
            z=np.concatenate([e,p],-1)[np.ix_(pfc,po)].mean((0,1))
            rows.append(z)
        print(band, rd, grp, h, np.round(np.mean(rows,0),1))
EOF
```

```
<stdin>:13: RuntimeWarning: Mean of empty slice
dt nolte ctrl 2 [-0.   0.1  0.   0.  -0.2 -0.2 -0.1 -0.2 -0.2 -0.1 -0.2 -0.1 -0.1 -0.1
 -0.  -0.1 -0.2 -0.1 -0.1 -0.1  0.   0.  -0.1  0.   0.1]
dt nolte ctrl 1 [ 0.1  0.1  0.  -0.2 -0.2 -0.2 -0.1 -0.  -0.1 -0.1 -0.1  0.  -0.  -0.1
 -0.1 -0.1 -0.2 -0.1 -0.   0.  -0.   0.   0.1 -0.   0. ]
dt nolte pfc 2 [ 0.1  0.1  0.2  0.2  0.1  0.1 -0.1 -0.   0.   0.   0.   0.1 -0.1 -0.1
  0.   0.  -0.  -0.1 -0.1  0.1  0.2  0.4  0.4  0.2  0.3]
dt nolte pfc 1 [ 0.1  0.  -0.1  0.2  0.2  0.1  0.3  0.1 -0.1 -0.2 -0.1 -0.  -0.1 -0.1
 -0.1 -0.   0.4  0.2  0.2  0.4  0.4  0.3  0.3  0.2  0.2]
dt trialwise ctrl 2 [ 11.1   7.9  12.7   6.2   6.3  19.7  18.8  -0.3   6.1   3.1 -14.2  -4.4
   9.6   8.7   9.8  15.9 -20.5 -22.9  -9.8   3.9   1.8   2.2   7.8   9.7
   9.8]
dt trialwise ctrl 1 [ 11.   10.6   9.1   8.7  11.3  11.8  14.9   2.    7.4  -0.3  -5.1  -1.2
   3.4   6.9   9.7  14.8 -19.7 -30.1  -8.1  -0.7   0.4   5.    9.   12.1
  15.6]
dt trialwise pfc 2 [ -7.3   5.7   5.3   3.2   4.    7.    8.4   0.7   2.5   5.    2.7   0.6
  -1.6   4.7  14.9  10.5 -12.4 -14.5 -11.7  -5.6  -0.3   9.7  11.4   6.
   8.1]
dt trialwise pfc 1 [ 5.   8.   8.  11.6  5.   5.3  1.4  7.2 -2.4 -1.   1.3 -4.  -5.9  2.1
  5.   4.6 -0.  -7.2 -8.9 -1.8  4.9  3.7  2.9  6.6 10.9]
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='frontoparietal.py'
s=open(p).read()
old_conv='''    X = np.fft.fft(x.astype(np.float64), n=N, axis=-1)
    out = np.empty(x.shape[:-1] + (len(freqs), len(toi)), np.complex64)'''
new_conv='''    import scipy.fft as sfft
    X = sfft.fft(x.astype(np.float32), n=N, axis=-1)                 # complex64
    out = np.empty(x.shape[:-1] + (len(freqs), len(toi)), np.complex64)'''
assert old_conv in s; s=s.replace(old_conv,new_conv)
old='''        dum = np.fft.fftshift(np.fft.ifft(X * np.fft.fft(w), axis=-1), axes=-1)
        out[..., i, :] = dum[..., tb - 1] * np.sqrt(2.0 / L)'''
new='''        dum = sfft.ifft(X * sfft.fft(w).astype(np.complex64), axis=-1)
        # fftshift then take samples tb - 1: the same as taking (tb - 1 + N // 2) mod N
        out[..., i, :] = dum[..., (tb - 1 + N // 2) % N] * np.sqrt(2.0 / L)'''
assert old in s; s=s.replace(old,new)
old='''        Xs = X.astype(np.complex64)
        U = psianalysis_literal_pp(Xs[:, :, None, :], Xs[:, None, :, :])   # (tr, a, b, f)
        obs3 = np.imag(U[..., :-1].conj() * U[..., 1:]).sum(-1).mean(0)
        pp3 = U.mean(0)
        del U'''
new='''        # U = X_a X_b / sqrt(X_a^2 conj(X_b)^2) = exp(i psi), psi = phi_a + phi_b - w,
        # w = principal angle of 2 (phi_a - phi_b), halved (MATLAB's principal square root)
        ph = np.angle(X).astype(np.float32)                       # (tr, c, f)
        dif = 2 * (ph[:, :, None, :] - ph[:, None, :, :])
        w = (np.mod(dif + np.pi, 2 * np.pi) - np.pi) / 2
        psi = ph[:, :, None, :] + ph[:, None, :, :] - w
        del dif, w
        obs3 = np.sin(np.diff(psi, axis=-1)).sum(-1).mean(0)
        pp3 = np.cos(psi).mean(0) + 1j * np.sin(psi).mean(0)
        del psi'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && OMP_NUM_THREADS=1 python - <<'EOF'
import numpy as np, time, frontoparietal as fp
rng=np.random.default_rng(1)
x=rng.standard_normal((40,64,385))
t=time.time(); F,m,tt=fp.mtmconvol(x, fp.FREQS, 0.01); print('tfr', time.time()-t)
# compare to float64 reference at one freq
N=1920; f=10; L=round(0.3*256); tap=fp.hanning(L); tap/=np.linalg.norm(tap)
tappad=int(np.ceil(N/2)-np.floor(L/2)); ang=np.arange(-(L-1)/2,(L-1)/2+1)*(2*np.pi/256)*f
w=np.zeros(N,complex); w[tappad:tappad+L]=tap*np.exp(1j*ang)
xd=x-x.mean(-1,keepdims=True)
ref=np.fft.fftshift(np.fft.ifft(np.fft.fft(xd,n=N)*np.fft.fft(w)),axes=-1)[...,np.round(tt*256).astype(int)]*np.sqrt(2/L)
print('max rel err', np.abs(F[...,f-1,:]-ref).max()/np.abs(ref).max())
Fb,_,_=fp.mtmconvol(x, fp.BANDS['ab'], 0.1)
X=Fb[...,5].astype(np.complex128)
U=fp.psianalysis_literal_pp(X[:,:,None,:],X[:,None,:,:]); o_ref=np.imag(U[...,:-1].conj()*U[...,1:]).sum(-1).mean(0)
t=time.time(); z=fp.psi_z(Fb[...,5:6],1000); print('psi 1 t', time.time()-t)
ph=np.angle(X); dif=2*(ph[:,:,None,:]-ph[:,None,:,:]); ww=(np.mod(dif+np.pi,2*np.pi)-np.pi)/2; ps=ph[:,:,None,:]+ph[:,None,:,:]-ww
print('literal obs err', np.nanmax(np.abs(np.sin(np.diff(ps,axis=-1)).sum(-1).mean(0)-o_ref)))
EOF
```

```
tfr 1.5157887935638428
max rel err 1.644005244142217e-07
psi 1 t 0.22754287719726562
literal obs err 8.881784197001252e-16
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import pickle, os, glob, time, numpy as np, frontoparietal as fp
d=os.environ['TMPDIR']+'/subj'
R={os.path.basename(f)[:-4]: pickle.load(open(f,'rb')) for f in sorted(glob.glob(d+'/*.pkl'))}
lab=R['ctrl01']['label']; A=fp.neighbours(lab)
C=[s for s in R if s.startswith('ctrl')]; P=[s for s in R if s.startswith('pfc')]
def z(r,seg,h,rd='pad'):
    mu=r[f'tfr_base_mu_{rd}']; sd=r[f'tfr_base_sd_{rd}']; N=r[f'tfr_base_N_{rd}']; n=r[f'n_{seg}_{h}']
    with np.errstate(all='ignore'):
        s=sd/np.sqrt(n)*np.sqrt((N-n)/(N-1))
    return (r[f'tfr_{seg}_{h}']-mu[...,None])/s[...,None]
x1=np.stack([z(R[s],'proc',2) for s in C]); x2=np.stack([z(R[s],'proc',2) for s in P])
t=time.time(); out=fp.cluster_test(x1,x2,A,n_perm=100); print('tfr proc main 100 perms', time.time()-t, [(c['sign'],c['p']) for c in out['clusters'][:3]])
pairs,PA=fp.pair_adjacency(A,'pairs'); _,SA=fp.pair_adjacency(A,'seed')
def pz(r,seg,h,rd='trialwise',band='dt'):
    b=np.nanmean(r[f'psi_{band}_pre_{rd}'],-1); v=r[f'psi_{band}_{seg}_{h}_{rd}']-b[...,None]; return v[pairs[:,0],pairs[:,1]]
y1=np.stack([pz(R[s],'proc',2) for s in C]); y2=np.stack([pz(R[s],'proc',2) for s in P])
for nm,adj,grp in [('a',None,None),('b',PA,None),('c',SA,pairs[:,0])]:
    t=time.time(); out=fp.cluster_test(y1,y2,adj,n_perm=100,node_groups=grp, minnbchan=2 if adj is not None else 0); print(nm, time.time()-t, [(c['sign'],round(c['p'],3),c['mask'].sum()) for c in out['clusters'][:3]])
EOF
```

```
<stdin>:15: RuntimeWarning: Mean of empty slice
tfr proc main 100 perms 2.0720162391662598 [(1, 0.38), (-1, 0.76), (-1, 0.82)]
a 0.25009608268737793 [(1, 1.0, np.int64(2)), (1, 1.0, np.int64(1)), (1, 1.0, np.int64(1))]
b 1.2796070575714111 [(1, 0.66, np.int64(472)), (-1, 0.66, np.int64(472)), (1, 1.0, np.int64(4))]
c 0.46033477783203125 [(1, 0.02, np.int64(11)), (1, 0.02, np.int64(45)), (-1, 0.02, np.int64(18))]
```

**Agent calls Bash**

```bash
date -u; grep -n "def \|^[A-Z_]* = " frontoparietal.py | head -50
```

```
Mon Nov  9 20:35:16 UTC 2026
58:BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-5/live/"
59:DATASET = "crcns:pfc-5/unversioned"
60:DATASET_DOI = "10.6080/K0ZC811B"
61:FIELDTRIP_COMMIT = "b3909bfecc5273652756ed2e41f84e9195f96186"
62:NEIGHBOURS_URL = ("https://raw.githubusercontent.com/fieldtrip/fieldtrip/"
65:CONTROLS = [f"ctrl{i:02d}" for i in range(1, 21)]
66:PATIENTS = [f"pfc{i:02d}" for i in range(1, 15)]
67:SUBJECTS = CONTROLS + PATIENTS
69:FS = 256.0
70:PAD = 7.5                     # seconds, cfg.pad = 7.5 in every *_compute.m
71:FREQS = np.arange(1, 41)      # 1 to 40 Hz (claims file, shared methods)
72:BANDS = {"dt": np.arange(2, 8), "ab": np.arange(9, 25)}   # PSI bands (psi_compute.m)
75:LEFT = ['Fp1', 'AF7', 'AF3', 'F1', 'F3', 'F5', 'F7', 'FT7', 'FC5', 'FC3', 'FC1', 'C1', 'C3', 'C5',
77:RIGHT = ['Fp2', 'AF8', 'AF4', 'F2', 'F4', 'F6', 'F8', 'FT8', 'FC6', 'FC4', 'FC2', 'C2', 'C4', 'C6',
83:def fetch(name: str) -> bytes:
89:def stream_subject_files(sid: str) -> dict:
109:def read_derived(raw: bytes) -> dict:
133:def read_trial_csv(raw: bytes):
139:def neighbours(labels: list[str]) -> np.ndarray:
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> frontoparietal.py <<'EOF'


# ----------------------------------------------------------------------------- derived measures

def power_z(r: dict, seg: str, h: int, reading: str = "pad", r_mode: str = "hemifield") -> np.ndarray:
    """Task power Z scored on the pretrial baseline (zbaseline.m), in its exact expectation:
    (mean power over the r trials - baseline mean) / (baseline sd / sqrt(r) * sqrt((N - r) /
    (N - 1))), N pooled baseline values (correct trials by time points). r_mode 'hemifield':
    r = trials of the data being scored (zbaseline.m); 'all': r = all correct trials of the
    subject (the Methods' "number of trials in that subject's dataset"). reading 'fit' sets to
    NaN every point FieldTrip leaves NaN (window outside the segment, here or in the baseline).
    Returns (64, 40, ntime)."""
    mu = r[f"tfr_base_mu_{reading}"].astype(np.float64)
    sd = r[f"tfr_base_sd_{reading}"].astype(np.float64)
    N = r[f"tfr_base_N_{reading}"].astype(np.float64)[None, :]
    n = r[f"n_{seg}_{h}"] if r_mode == "hemifield" else r["n_correct"]
    with np.errstate(invalid="ignore", divide="ignore"):
        s = sd / np.sqrt(n) * np.sqrt((N - n) / (N - 1))
        z = (r[f"tfr_{seg}_{h}"] - mu[..., None]) / s[..., None]
    if reading == "fit":
        z = np.where(r[f"tfr_{seg}_mask"][None], z, np.nan)
    return z


def hem_index(x: np.ndarray, labels: list[str], axis: int = 1) -> np.ndarray:
    """Lesioned minus intact homolog (left minus right after the swap), 27 channels in the
    order of *_stat_group_hem.m."""
    li = [labels.index(c) for c in LEFT]
    ri = [labels.index(c) for c in RIGHT]
    return np.take(x, li, axis=axis) - np.take(x, ri, axis=axis)


def psi_bc(r: dict, band: str, seg: str, h: int, reading: str, window: str = "pad") -> np.ndarray:
    """Baseline-corrected PSI Z (64, 64, ntime): Z minus its temporal mean over the pretrial
    baseline (psi_compute.m). window 'fit': points whose 3/f windows do not all fit inside the
    segment are NaN, and the baseline mean is over the baseline points that fit (FieldTrip)."""
    pre = r[f"psi_{band}_pre_{reading}"].astype(np.float64)
    z = r[f"psi_{band}_{seg}_{h}_{reading}"].astype(np.float64)
    if window == "fit":
        pre = np.where(r[f"psi_{band}_pre_mask"].all(0), pre, np.nan)
        z = np.where(r[f"psi_{band}_{seg}_mask"].all(0), z, np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        base = np.nanmean(pre, axis=-1)
    return z - base[..., None]


def psi_raw(r: dict, band: str, seg: str, h: int | None, reading: str) -> np.ndarray:
    key = f"psi_{band}_pre_{reading}" if seg == "pre" else f"psi_{band}_{seg}_{h}_{reading}"
    return r[key].astype(np.float64)


def degree(z: np.ndarray, mode: str) -> np.ndarray:
    """Network degree per channel from PSI Z (64, 64, nt), before baseline correction.
    'ft_count': ft_networkanalysis 'degrees' on Z > 1.96, directed: in-degree plus out-degree
    (psi_compute.m), i.e. connections with |Z| > 1.96 in either direction. Readings of the
    claims file: 'out_signed' (a) sum of Z over connections leaving the channel with |Z| >
    1.96; 'out_count' (b) their count; 'abs_both' (c) sum of |Z| over true connections in
    either direction."""
    z = np.nan_to_num(z)
    if mode == "ft_count":
        g = (z > 1.96).astype(float)
        return g.sum(0) + g.sum(1)
    true = np.abs(z) > 1.96
    if mode == "out_signed":
        return np.where(true, z, 0).sum(1)
    if mode == "out_count":
        return true.sum(1).astype(float)
    if mode == "abs_both":
        return np.where(true, np.abs(z), 0).sum(1) + np.where(true, np.abs(z), 0).sum(0)
    raise ValueError(mode)


# ----------------------------------------------------------------------------- behaviour

def ancova_rm(Y: np.ndarray, B: np.ndarray, names: list[str]) -> list[dict]:
    """Repeated-measures ANCOVA as SPSS GLM computes it (Type III, sphericity assumed).
    Y: (n, 2, 3) accuracy by visual hemifield (lesion, intact) and condition. B: (n, k)
    between-subject terms without the intercept (factors effect coded +-1, covariates raw).
    Between-subject terms are tested on the subject mean; within-subject effects on orthonormal
    contrasts of the within cells, regressed on the same terms (their intercept is the
    within-subject main effect, each slope its interaction with that term)."""
    n = len(Y)
    X = np.column_stack([np.ones(n), B])
    XtXi = np.linalg.pinv(X.T @ X)
    dfe = n - np.linalg.matrix_rank(X)
    c_v = np.array([1, -1]) / np.sqrt(2)
    c_c = np.array([[1, -1, 0], [1, 1, -2]], float)
    c_c = c_c / np.linalg.norm(c_c, axis=1, keepdims=True)
    blocks = {
        "": [Y.mean(axis=(1, 2)) * np.sqrt(6)],
        "Visual Hemifield": [np.einsum("v,nvc->n", c_v, Y) / np.sqrt(3)],
        "Condition": [np.einsum("kc,nvc->nk", c_c, Y)[:, k] / np.sqrt(2) for k in range(2)],
        "Visual Hemifield x Condition": [np.einsum("v,kc,nvc->nk", c_v, c_c, Y)[:, k] for k in range(2)],
    }
    out = []
    for within, ys in blocks.items():
        ss_h = np.zeros(X.shape[1])
        sse = 0.0
        for y in ys:
            beta = XtXi @ X.T @ y
            res = y - X @ beta
            sse += res @ res
            ss_h += beta ** 2 / np.diag(XtXi)
        q = len(ys)
        for j, nm in enumerate(["(intercept)"] + names):
            if within == "" and j == 0:
                continue
            label = within if j == 0 else (nm if within == "" else f"{within} x {nm}")
            F = (ss_h[j] / q) / (sse / (q * dfe))
            from scipy import stats
            out.append({"term": label, "F": F, "df1": q, "df2": q * dfe,
                        "p": float(stats.f.sf(F, q, q * dfe)),
                        "partial_eta2": ss_h[j] / (ss_h[j] + sse)})
    return out


def lmm_wald(df, formula: str, group: str = "subject") -> dict:
    """Linear mixed model with a random intercept per subject (statsmodels MixedLM, REML);
    F = (beta / se)^2 per fixed effect, p from F(1, n - p) (fitglme's residual degrees of
    freedom)."""
    import statsmodels.formula.api as smf
    from scipy import stats
    m = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
    fe = m.fe_params
    se = m.bse_fe
    dfe = len(df) - len(fe)
    return {k: {"beta": float(fe[k]), "F": float((fe[k] / se[k]) ** 2), "df2": dfe,
                "p": float(stats.f.sf((fe[k] / se[k]) ** 2, 1, dfe))} for k in fe.index if k != "Intercept"}


def glmm_binomial(k: np.ndarray, n: np.ndarray, X: np.ndarray, groups: np.ndarray, names: list[str],
                  nq: int = 30) -> dict:
    """Logit mixed model with a random intercept per subject, fitted by maximum likelihood
    with Gauss-Hermite quadrature; Wald F = (beta / se)^2, p from F(1, rows - p)."""
    from scipy import optimize, special, stats
    gh_x, gh_w = np.polynomial.hermite.hermgauss(nq)
    ug = np.unique(groups)
    gi = np.searchsorted(ug, groups)
    p = X.shape[1]
    lc = special.gammaln(n + 1) - special.gammaln(k + 1) - special.gammaln(n - k + 1)

    def nll(th):
        b, ls = th[:p], th[p]
        eta = X @ b
        u = np.sqrt(2) * np.exp(ls) * gh_x[None, :]
        e = eta[:, None] + u
        ll = k[:, None] * e - n[:, None] * np.logaddexp(0, e) + lc[:, None]
        G = np.zeros((len(ug), nq))
        np.add.at(G, gi, ll)
        m = G.max(1, keepdims=True)
        return -np.sum(m[:, 0] + np.log((np.exp(G - m) * gh_w[None]).sum(1) / np.sqrt(np.pi)))

    th0 = np.zeros(p + 1)
    th0[0] = special.logit(np.clip(k.sum() / n.sum(), 0.01, 0.99))
    th0[p] = np.log(0.5)
    opt = optimize.minimize(nll, th0, method="BFGS")
    th = opt.x
    h = 1e-4
    H = np.zeros((p + 1, p + 1))
    for i in range(p + 1):
        for j in range(i, p + 1):
            ei = np.eye(p + 1)[i] * h
            ej = np.eye(p + 1)[j] * h
            H[i, j] = H[j, i] = (nll(th + ei + ej) - nll(th + ei - ej) - nll(th - ei + ej) + nll(th - ei - ej)) / (4 * h * h)
    cov = np.linalg.inv(H)
    dfe = len(k) - p
    out = {}
    for i, nm in enumerate(names):
        if nm == "Intercept":
            continue
        F = th[i] ** 2 / cov[i, i]
        out[nm] = {"beta": float(th[i]), "F": float(F), "df2": dfe, "p": float(stats.f.sf(F, 1, dfe))}
    out["_converged"] = bool(opt.success)
    return out
EOF
date -u
```

```
Mon Nov  9 20:35:49 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/part1.py",
 "content": "# %% [markdown]\n# # Reproducing Johnson et al. (2017) on CRCNS pfc-5\n#\n# HEADER_PLACEHOLDER\n\n# %%\nimport time, resource, io, tarfile, re, warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport frontoparietal as fp\n\nT0 = time.time()\nprint(\"dataset\", fp.DATASET, \"doi\", fp.DATASET_DOI)\nmd5 = {}\nfor line in fp.fetch(\"checksums.md5\").decode().splitlines():\n    if line.strip():\n        h, name = line.split(None, 1)\n        md5[name.strip()] = h\nfiles_read = ([\"checksums.md5 (itself not listed)\", \"docs/summary_file_behavior_pfc.txt\",\n               \"docs/summary_file_behavior_ctrl.txt\", \"analysis_scripts.tar.gz\"]\n              + [f\"data/{s}.tar.gz\" for s in fp.SUBJECTS])\nfor f in files_read:\n    print(md5.get(f, \"-\" * 32), f)\n\n# %% [markdown]\n# The paper's code, deposited in the data set (`analysis_scripts.tar.gz`). The lines below are\n# the ones this notebook follows where the claims file leaves a detail open, and the two places\n# where the code disagrees with the Methods or with the data.\n\n# %%\nscripts = {}\nwith tarfile.open(fileobj=io.BytesIO(fp.fetch(\"analysis_scripts.tar.gz\")), mode=\"r:gz\") as tf:\n    for m in tf.getmembers():\n        if m.isfile() and m.name.endswith(\".m\") and \"/._\" not in m.name:\n            scripts[m.name.split(\"analysis_scripts/\")[-1]] = tf.extractfile(m).read().decode(\"latin-1\")\nprint(sorted(scripts))\ndef show(name, pattern):\n    for i, line in enumerate(scripts[name].splitlines(), 1):\n        if re.search(pattern, line):\n            print(f\"{name}:{i}: {line.strip()}\")\nshow(\"tfr_stat_group.m\", r\"neighbours|minnbchan|numrandomization|clusteralpha|tail|layout|method =\")\nshow(\"tfr_stat_group_hem.m\", r\"cfgl.channel|cfgr.channel|individual-|powspctrm-\")\nshow(\"tfr_compute.m\", r\"cfgc.trials|cfgv.trials|ft_selectdata\\(cfgv, proc\\)|foi|t_ftimwin|pad|toi_res =\")\nshow(\"subfunctions/zbaseline.m\", r\"randsample|ntrials =\")\nshow(\"psi_compute.m\", r\"subtracterp|toi_res =|threshold|cfggt.method|fmin = |psianalysis\\(\")\nshow(\"subfunctions/psianalysis.m\", r\"csd\\(|ppsub\\(|psisub\\(|nulldist\\(:|psimtx\\(\")\nshow(\"psi_stat_group.m\", r\"for e = 1:nchan|subspctrm =\")\nshow(\"fft_compute.m\", r\"method|foi|pad\")\nshow(\"erp_compute.m\", r\"lpfreq|padding|cfgc.trials|ft_selectdata\\(cfgv, proc\\)\")\n\n# %%\nt_load = time.time()\nR = fp.process_all(fp.SUBJECTS, workers=4)\nfailed = {s: r[\"error\"] for s, r in R.items() if \"error\" in r}\nprint(\"subjects loaded\", len(R) - len(failed), \"failed\", failed)\nprint(f\"loading and per-subject computation took {(time.time() - t_load) / 60:.1f} min; \"\n      f\"peak memory of this process {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nCTRL = [s for s in fp.CONTROLS if s not in failed]\nPFC = [s for s in fp.PATIENTS if s not in failed]\nlabels = R[CTRL[0]][\"label\"]\nL = {c: i for i, c in enumerate(labels)}\nADJ = fp.neighbours(labels)\nADJ_HEM = ADJ[np.ix_([L[c] for c in fp.LEFT], [L[c] for c in fp.LEFT])]\npfc_doc = pd.read_csv(io.BytesIO(fp.fetch(\"docs/summary_file_behavior_pfc.txt\")), sep=\"\\t\")\nctrl_doc = pd.read_csv(io.BytesIO(fp.fetch(\"docs/summary_file_behavior_ctrl.txt\")), sep=\"\\t\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/part1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/part2.py",
 "content": "# %% tags=[\"sanity\"]\n# What was loaded, and the description checked against the data\nrows = []\nfor s in CTRL + PFC:\n    r = R[s]\n    csv = r[\"csv\"]\n    ti = r[\"encmain_trialinfo\"]\n    names = [m[0].split(\"/\")[-1] for m in r[\"members\"] if m[1] > 0]\n    # lesioned visual hemifield in the trial table's coding (1 left, 2 right)\n    m = csv.set_index(\"trial\").loc[ti[:, 0].astype(int)]\n    les_vhf = sorted(set(m[\"vhf\"].values[ti[:, 2] == 2]))\n    same_order = bool(np.array_equal(r[\"proc_trialinfo\"][:, 0], ti[:, 0]))\n    same_set = set(r[\"proc_trialinfo\"][:, 0]) == set(ti[:, 0])\n    rows.append({\n        \"subject\": s, \"csv_trials\": len(csv), \"derived_trials\": len(ti),\n        \"derived_in_csv\": bool(set(ti[:, 0].astype(int)) <= set(csv[\"trial\"])),\n        \"info_agrees\": bool((m[\"correct\"].values == ti[:, 1]).all() and (m[\"condition\"].values == ti[:, 4]).all()\n                            and (m[\"jitter\"].values == ti[:, 5]).all() and (m[\"rt\"].values == ti[:, 6]).all()),\n        \"lesioned_vhf_csv\": les_vhf, \"pre_eq_enc_info\": bool(np.array_equal(r[\"pretrial_trialinfo\"], ti)),\n        \"proc_same_set\": same_set, \"proc_same_order\": same_order,\n        \"len_pre_enc_proc\": (r[\"pretrial_lengths\"], r[\"encmain_lengths\"], r[\"proc_lengths\"]),\n        \"fsample_pre_enc_proc\": (round(r[\"pretrial_fsample\"], 2), r[\"encmain_fsample\"], r[\"proc_fsample\"]),\n        \"two_blocks\": any(\"_2\" in n for n in names), \"channel_replace\": any(\"channel_replace\" in n for n in names),\n        \"neighbour_corr\": round(r[\"neighbour_corr\"], 2),\n    })\nsan = pd.DataFrame(rows).set_index(\"subject\")\nwith pd.option_context(\"display.width\", 250, \"display.max_columns\", 30, \"display.max_rows\", 50):\n    print(san)\nprint(\"\\nsubjects: controls\", len(CTRL), \"patients\", len(PFC))\nprint(\"labels identical in every subject:\", all(R[s][\"label\"] == labels for s in CTRL + PFC), \"| n =\", len(labels))\nprint(\"segment start times (s):\", sorted({x for s in CTRL + PFC for k in (\"pretrial\", \"encmain\", \"proc\") for x in R[s][f\"{k}_time_first\"]}))\nprint(\"segment samples pretrial/encmain/proc:\", sorted({str(v) for v in san[\"len_pre_enc_proc\"]}),\n      \"-> at 256 Hz: 0 to 0.5 s, 0 to 1.5 s, 0 to 0.898 s; no buffers\")\nprint(\"fsample fields:\", sorted({str(v) for v in san[\"fsample_pre_enc_proc\"]}))\nprint(\"derived trials all in the trial table:\", san[\"derived_in_csv\"].all(), \"| trial info agrees:\", san[\"info_agrees\"].all())\nprint(\"pretrial and encmain trialinfo identical:\", san[\"pre_eq_enc_info\"].all())\nprint(\"proc holds the same trials as encmain:\", san[\"proc_same_set\"].all(),\n      \"| in the same order:\", int(san[\"proc_same_order\"].sum()), \"of\", len(san))\nfing = pd.Series({s: R[s][\"fingerprint\"] for s in CTRL + PFC})\nmd5d = pd.Series({s: R[s][\"derived_md5\"] for s in CTRL + PFC})\nprint(\"duplicate recordings (identical first-trial sums or identical data_derived.mat):\",\n      int(fing.duplicated().sum()), int(md5d.duplicated().sum()))\n# hemifield coding and the swap\npat_hem = pfc_doc.set_index(\"subid\")[\"lesion_hem\"]\nok_pat = all(san.loc[s, \"lesioned_vhf_csv\"] == ([2] if pat_hem[s] == \"L\" else [1]) for s in PFC)\nswapped = [s for s in CTRL if san.loc[s, \"lesioned_vhf_csv\"] == [1]]\nprint(\"patients: derived 'lesioned' hemifield is contralateral to the lesion in every patient:\", ok_pat)\nprint(\"controls whose 'lesioned' hemifield is the left one (swapped across the midline):\", len(swapped), swapped)\nprint(\"neighbouring-channel correlation, median (range):\", san[\"neighbour_corr\"].median(),\n      san[\"neighbour_corr\"].min(), san[\"neighbour_corr\"].max())\n# accuracy in the docs summary against the trial tables\ndef acc_cells(s):\n    csv = R[s][\"csv\"]\n    lesvhf = san.loc[s, \"lesioned_vhf_csv\"][0]\n    out = {}\n    for name, v in ((\"lesion\", lesvhf), (\"intact\", 3 - lesvhf)):\n        out[name] = csv.loc[csv.vhf == v, \"correct\"].mean()\n    for v, vn in ((1, \"left\"), (2, \"right\")):\n        for c, cn in ((1, \"iden\"), (2, \"spa\"), (3, \"temp\")):\n            out[f\"vhf_{vn}_{cn}\"] = csv.loc[(csv.vhf == v) & (csv.condition == c), \"correct\"].mean()\n    return out\ndoc = pd.concat([pfc_doc.set_index(\"subid\"), ctrl_doc.set_index(\"subid\")])\ndiffs = []\nfor s in CTRL + PFC:\n    a = acc_cells(s)\n    diffs.append(max(abs(a[\"lesion\"] - doc.loc[s, \"vhf_lesion\"]), abs(a[\"intact\"] - doc.loc[s, \"vhf_intact\"]),\n                     *[abs(a[k] - doc.loc[s, k]) for k in a if k.startswith(\"vhf_\")]))\nprint(\"largest difference between the trial tables' accuracies and the docs summary files:\", round(max(diffs), 3))\nprint(\"docs summary: patients\", len(pfc_doc), \"controls\", len(ctrl_doc),\n      \"| patient males\", int((pfc_doc.gender == \"M\").sum()), \"| control males\", int((ctrl_doc.gender == \"M\").sum()))\n# units and ranges\nerp_all = np.stack([R[s][\"erp_enc_2\"] for s in CTRL + PFC])\nfft_all = np.stack([R[s][\"fft\"] for s in CTRL + PFC])\nprint(f\"ERP (data units, no unit stored; microvolts per area under the Laplacian): {erp_all.min():.2f} to {erp_all.max():.2f}\")\nprint(f\"baseline power: {fft_all.min():.3g} to {fft_all.max():.3g}\")\nzz = np.stack([fp.power_z(R[s], \"proc\", 2) for s in CTRL + PFC])\nprint(f\"power Z (proc, lesioned hemifield, reading pad): {np.nanmin(zz):.1f} to {np.nanmax(zz):.1f}\")\nm_fit = R[CTRL[0]][\"tfr_pre_mask\"]\nprint(\"frequencies with any baseline value under FieldTrip's window rule ('fit'):\",\n      fp.FREQS[m_fit.any(1)].min(), \"to 40 Hz; proc frequencies with any value:\",\n      fp.FREQS[R[CTRL[0]][\"tfr_proc_mask\"].any(1)].min(), \"to 40 Hz\")\nfor band in (\"dt\", \"ab\"):\n    print(f\"PSI {band}: time points whose windows all fit, pretrial/encmain/proc:\",\n          int(R[CTRL[0]][f\"psi_{band}_pre_mask\"].all(0).sum()), int(R[CTRL[0]][f\"psi_{band}_enc_mask\"].all(0).sum()),\n          int(R[CTRL[0]][f\"psi_{band}_proc_mask\"].all(0).sum()))\n\n# %% [markdown]\n# **Do the segments share the clock of the trial table?** Stimuli went to one visual hemifield,\n# so the posterior ERP should differ between the hemispheres, and between the two hemifield\n# conditions, shortly after the first stimulus (time 0 of the encoding-maintenance segment) and\n# not before the visual response can arise. Below: the lateralised posterior ERP (P7, PO7, O1\n# minus P8, PO8, O2) for lesioned- minus intact-hemifield trials, tested across all 34 subjects\n# at each time point. The null is the same statistic with the hemifield labels flipped in a\n# random half of the subjects (1000 times).\n\n# %%\npost_l = [L[c] for c in (\"P7\", \"PO7\", \"O1\")]\npost_r = [L[c] for c in (\"P8\", \"PO8\", \"O2\")]\nlat = np.stack([(R[s][\"erp_enc_2\"][post_l].mean(0) - R[s][\"erp_enc_2\"][post_r].mean(0))\n                - (R[s][\"erp_enc_1\"][post_l].mean(0) - R[s][\"erp_enc_1\"][post_r].mean(0)) for s in CTRL + PFC])\ntt = np.arange(lat.shape[1]) / fp.FS\ntval = stats.ttest_1samp(lat, 0).statistic\nrng_clock = np.random.default_rng(11)\nnull = np.array([np.abs(stats.ttest_1samp(lat * rng_clock.choice([-1, 1], len(lat))[:, None], 0).statistic).max()\n                 for _ in range(1000)])\nthr = np.quantile(null, 0.95)\nsig = np.flatnonzero(np.abs(tval) > thr)\nprint(f\"max |t| threshold (95% of sign-flip null): {thr:.2f}\")\nprint(f\"first time with |t| above it: {tt[sig[0]] * 1000:.0f} ms; peak |t| {np.abs(tval).max():.1f} at {tt[np.abs(tval).argmax()] * 1000:.0f} ms\")\nfor a, b in ((0, 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 0.4), (0.4, 0.8), (0.8, 1.5)):\n    w = (tt >= a) & (tt < b)\n    print(f\"  {a * 1000:4.0f}-{b * 1000:4.0f} ms: max |t| = {np.abs(tval[w]).max():.1f}\")\n# processing segment: the test prompt is central; check the posterior ERP peaks after its offset\ngp = np.stack([R[s][\"erp_proc_2\"][post_l + post_r].mean(0) for s in CTRL + PFC]).mean(0)\ntp = np.arange(len(gp)) / fp.FS\nprint(f\"processing segment: grand posterior ERP largest deflection at {tp[np.abs(gp).argmax()] * 1000:.0f} ms after time 0\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/part2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb; cat > $TMPDIR/nb/dev.py <<'EOF'
import sys, os, glob, pickle
sys.path.insert(0, 'entries/johnson-2017')
import frontoparietal as fp
d = os.environ['TMPDIR'] + '/subj'
_cache = None
def fake(subjects=None, workers=4, done=None):
    global _cache
    if _cache is None:
        _cache = {os.path.basename(f)[:-4]: pickle.load(open(f, 'rb')) for f in sorted(glob.glob(d + '/*.pkl'))}
    return {s: _cache[s] for s in fp.SUBJECTS}
fp.process_all = fake
parts = sys.argv[1:]
src = "\n".join(open(p).read() for p in parts)
import matplotlib; matplotlib.use('Agg')
g = {}
exec(compile(src, 'nb', 'exec'), g)
pickle.dump({k: v for k, v in g.items() if k in ('_keep',)}, open(os.devnull, 'wb'))
EOF
cd $TMPDIR/nb && . ../dev/bin/activate && python dev.py part1.py part2.py 2>&1 | grep -v "^$" | head -120
```

```
dataset crcns:pfc-5/unversioned doi 10.6080/K0ZC811B
-------------------------------- checksums.md5 (itself not listed)
a4b67dd6b28e4988214714807585216a docs/summary_file_behavior_pfc.txt
706b3463fde82c6b9c1b6862071badda docs/summary_file_behavior_ctrl.txt
463b2d55e0ab54842879baa262d69a6a analysis_scripts.tar.gz
42af60ebf34494de818693b77c2795d3 data/ctrl01.tar.gz
e79834d7631eb9dfce807f372c75e3aa data/ctrl02.tar.gz
7a834cf6afc4fd44855e0ec6d643a47c data/ctrl03.tar.gz
bbd773e7945d1bcc2928227383707bef data/ctrl04.tar.gz
3923511ac3def13d56e2af2eff18774e data/ctrl05.tar.gz
25da306213bed17f3e5e1514d5888a6a data/ctrl06.tar.gz
bcd427429fb041a9455c4db5cfc6c768 data/ctrl07.tar.gz
ebf09a6d3c5a9d4b4c570cecf8b1ce01 data/ctrl08.tar.gz
276409e1fda02b443221505e32921097 data/ctrl09.tar.gz
aec230327ab8c33a17990382a1bb1068 data/ctrl10.tar.gz
55bf9dc60f42adbcf687bc7b8365f71a data/ctrl11.tar.gz
d11208b51b397f3c4e22c32941302aa2 data/ctrl12.tar.gz
851f79f8b790e90808f43f267fbc20f1 data/ctrl13.tar.gz
534186e60a2b235cda232659efdbf8f2 data/ctrl14.tar.gz
accc5cf833d24db61ef5b40df333fa51 data/ctrl15.tar.gz
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,os
for s in ['ctrl08','pfc03','pfc10']:
    r=pickle.load(open(os.environ['TMPDIR']+f'/subj/{s}.pkl','rb'))
    ti=r['encmain_trialinfo']; print(s, ti[:,0].min(), ti[:,0].max(), len(ti), r['csv'].trial.min(), r['csv'].trial.max(), len(r['csv']))
"
```

```
ctrl08 1.0 180.0 180 1.0 240.0 240
pfc03 2.0 120.0 109 21 120 100
pfc10 1.0 240.0 220 1 120 120
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cd entries/johnson-2017 && python - <<'EOF'
import tarfile, urllib.request, io, pandas as pd
from concurrent.futures import ThreadPoolExecutor
import frontoparietal as fp
def get(s):
    out={}
    with urllib.request.urlopen(fp.BUCKET+f"data/{s}.tar.gz") as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                if "summary_file_trial" in m.name: out[m.name]=fp.read_trial_csv(tf.extractfile(m).read())
    return s,out
with ThreadPoolExecutor(6) as ex:
    for s,out in ex.map(get, ['ctrl08','pfc03','pfc10','pfc11','pfc12','pfc13']):
        for k,v in out.items(): print(s,k,len(v), v.trial.min(), v.trial.max(), v.t_pre.min(), v.t_pre.max(), v.vhf.value_counts().to_dict())
EOF
```

```
ctrl08 ctrl08/summary_file_trial_2.csv 116 81 196 4420 1746779 {2: 60, 1: 56}
ctrl08 ctrl08/summary_file_trial_1.csv 240 1.0 240.0 108156.0 2481577.0 {1.0: 63, 2.0: 60}
pfc03 pfc03/summary_file_trial_2.csv 120 2 240 4020 1503030 {1: 60, 2: 60}
pfc03 pfc03/summary_file_trial_1.csv 100 21 120 283013 1562019 {2: 55, 1: 45}
pfc10 pfc10/summary_file_trial_2.csv 120 2 240 6669 1548295 {2: 60, 1: 60}
pfc10 pfc10/summary_file_trial_1.csv 120 1 120 505298 2097560 {1: 60, 2: 60}
pfc11 pfc11/summary_file_trial_2.csv 120 121 240 92153 1689247 {1: 60, 2: 60}
pfc11 pfc11/summary_file_trial_1.csv 120 1 120 9850 1702246 {1: 60, 2: 60}
pfc12 pfc12/summary_file_trial_2.csv 120 2 240 7498 1557601 {1: 60, 2: 60}
pfc12 pfc12/summary_file_trial_1.csv 120 1 120 7172 1586865 {2: 60, 1: 60}
pfc13 pfc13/summary_file_trial_2.csv 120 2 240 5705 1585436 {2: 60, 1: 60}
pfc13 pfc13/summary_file_trial_1.csv 120 1 120 14737 1623754 {2: 60, 1: 60}
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='frontoparietal.py'
s=open(p).read()
old='''    csv = read_trial_csv(files["csv"]) if "csv" in files else None'''
new='''    csv = None
    if files.get("csv_all"):
        import pandas as pd
        csv = pd.concat([read_trial_csv(b).assign(block=n.split("/")[-1]) for n, b in sorted(files["csv_all"])],
                        ignore_index=True)
        csv = csv.dropna(subset=["trial", "correct", "vhf"]).astype({"trial": int, "correct": int, "vhf": int,
                                                                       "condition": int, "jitter": int})'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    if out.get("csv_all"):
        out["csv"] = sorted(out["csv_all"])[0][1]
''','')
s += '''

def link_trials(csv, ti: np.ndarray) -> np.ndarray:
    """Row of the trial table (csv, all blocks) for each derived trial: same trial number and
    response time; failing that, the one row with the same response time, condition, jitter
    and accuracy. -1 where no single row matches. Two-block subjects number their trials in
    ways that overlap between blocks, so the trial number alone does not identify a row."""
    out = -np.ones(len(ti), int)
    tr = csv["trial"].to_numpy()
    rt = csv["rt"].to_numpy()
    key = np.stack([csv["rt"], csv["condition"], csv["jitter"], csv["correct"]], 1)
    for i, row in enumerate(ti):
        j = np.flatnonzero((tr == int(row[0])) & (rt == row[6]))
        if len(j) != 1:
            j = np.flatnonzero((key == row[[6, 4, 5, 1]]).all(1))
        if len(j) == 1:
            out[i] = j[0]
    return out
'''
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import os, pickle, tarfile, urllib.request, pandas as pd
from concurrent.futures import ThreadPoolExecutor
import frontoparietal as fp
d=os.environ['TMPDIR']+'/subj'
def fix(s):
    out=[]
    with urllib.request.urlopen(fp.BUCKET+f"data/{s}.tar.gz") as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                if "summary_file_trial" in m.name and m.isfile(): out.append((m.name, tf.extractfile(m).read()))
    csv = pd.concat([fp.read_trial_csv(b).assign(block=n.split("/")[-1]) for n, b in sorted(out)], ignore_index=True)
    csv = csv.dropna(subset=["trial","correct","vhf"]).astype({"trial": int, "correct": int, "vhf": int, "condition": int, "jitter": int})
    r=pickle.load(open(f'{d}/{s}.pkl','rb')); r['csv']=csv; pickle.dump(r, open(f'{d}/{s}.pkl','wb'))
    li=fp.link_trials(csv, r['encmain_trialinfo']); return s, len(csv), (li>=0).sum(), len(li)
with ThreadPoolExecutor(6) as ex:
    for x in ex.map(fix, ['ctrl08','pfc03','pfc10','pfc11','pfc12','pfc13']): print(x)
EOF
```

```
('ctrl08', 239, np.int64(180), 180)
('pfc03', 220, np.int64(109), 109)
('pfc10', 240, np.int64(220), 220)
('pfc11', 240, np.int64(212), 212)
('pfc12', 240, np.int64(114), 114)
('pfc13', 240, np.int64(111), 111)
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('part2.py').read()
old='''    m = csv.set_index("trial").loc[ti[:, 0].astype(int)]
    les_vhf'''
new='''    link = fp.link_trials(csv, ti)
    m = csv.iloc[link[link >= 0]]
    ti_l = ti[link >= 0]
    les_vhf'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    les_vhf = sorted(set(m["vhf"].values[ti[:, 2] == 2]))''','''    les_vhf = sorted(set(m["vhf"].values[ti_l[:, 2] == 2]))''')
s=s.replace('''        "derived_in_csv": bool(set(ti[:, 0].astype(int)) <= set(csv["trial"])),
        "info_agrees": bool((m["correct"].values == ti[:, 1]).all() and (m["condition"].values == ti[:, 4]).all()
                            and (m["jitter"].values == ti[:, 5]).all() and (m["rt"].values == ti[:, 6]).all()),''','''        "csv_blocks": csv["block"].nunique(), "linked": int((link >= 0).sum()),
        "info_agrees": bool((m["correct"].values == ti_l[:, 1]).all() and (m["condition"].values == ti_l[:, 4]).all()
                            and (m["jitter"].values == ti_l[:, 5]).all() and (m["rt"].values == ti_l[:, 6]).all()),''')
s=s.replace('''print("derived trials all in the trial table:", san["derived_in_csv"].all(), "| trial info agrees:", san["info_agrees"].all())''','''print("derived trials linked to one trial-table row (trial number and response time):",
      int(san["linked"].sum()), "of", int(san["derived_trials"].sum()), "| trial info agrees where linked:", san["info_agrees"].all())
print("subjects with two trial tables (two recording blocks):", list(san.index[san["csv_blocks"] > 1]))''')
open('part2.py','w').write(s)
EOF
. ../dev/bin/activate && python dev.py part1.py part2.py 2>&1 | sed -n '/subjects loaded/,$p'
```

```
subjects loaded 34 failed {}
loading and per-subject computation took 0.0 min; peak memory of this process 0.53 GB
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/indexes/base.py", line 3816, in get_loc
    return self._engine.get_loc(casted_key)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "pandas/_libs/index.pyx", line 172, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 201, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7726, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7734, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'block'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tmp/claude-1001/nb/dev.py", line 16, in <module>
    exec(compile(src, 'nb', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "nb", line 86, in <module>
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/frame.py", line 4330, in __getitem__
[... 5 more lines not kept]
```

**Agent**

Cached single-block subjects lack the `block` column; I'll patch the cache in place to match the new helper output.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import os, glob, pickle
for f in glob.glob(os.environ['TMPDIR']+'/subj/*.pkl'):
    r=pickle.load(open(f,'rb'))
    if 'block' not in r['csv']:
        c=r['csv'].assign(block='summary_file_trial.csv').dropna(subset=["trial","correct","vhf"]).astype({"trial": int, "correct": int, "vhf": int, "condition": int, "jitter": int})
        r['csv']=c; pickle.dump(r, open(f,'wb'))
EOF
cd $TMPDIR/nb && . ../dev/bin/activate && python dev.py part1.py part2.py 2>&1 | sed -n '/subjects loaded/,$p'
```

```
subjects loaded 34 failed {}
loading and per-subject computation took 0.0 min; peak memory of this process 0.53 GB
         csv_trials  derived_trials  csv_blocks  linked  info_agrees lesioned_vhf_csv  pre_eq_enc_info  proc_same_set  proc_same_order       len_pre_enc_proc    fsample_pre_enc_proc  two_blocks  channel_replace  neighbour_corr
subject                                                                                                                                                                                                                           
ctrl01          187             156           1     156         True              [2]             True           True            False  ([129], [385], [231])  (255.64, 256.0, 256.0)       False             True            0.49
ctrl02          153             129           1     129         True              [2]             True           True            False  ([129], [385], [231])  (255.64, 256.0, 256.0)       False             True            0.54
ctrl03          180             169           1     169         True              [2]             True           True            False  ([129], [385], [231])  (255.64, 256.0, 256.0)       False            False            0.55
ctrl04          220             211           1     211         True              [2]             True           True            False  ([129], [385], [231])  (255.64, 256.0, 256.0)       False            False            0.55
ctrl05          229             209           1     209         True              [2]             True           True            False  ([129], [385], [231])  (255.64, 256.0, 256.0)       False            False            0.52
ctrl06          197             188           1     188         True              [2]             True           True            False  ([129], [385], [231])  (255.64, 256.0, 256.0)       False            False            0.51
ctrl07          219             218           1     218         True 
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import os, glob, pickle, numpy as np, pandas as pd, io
import sys; sys.path.insert(0,'entries/johnson-2017'); import frontoparietal as fp
R={os.path.basename(f)[:-4]: pickle.load(open(f,'rb')) for f in sorted(glob.glob(os.environ['TMPDIR']+'/subj/*.pkl'))}
ref=R['ctrl01']['label']
for s,r in R.items():
    if r['label']!=ref: print(s, [ (i,a,b) for i,(a,b) in enumerate(zip(ref,r['label'])) if a!=b][:6])
pfc=pd.read_csv(io.BytesIO(fp.fetch("docs/summary_file_behavior_pfc.txt")), sep="\t").set_index('subid')
ctrl=pd.read_csv(io.BytesIO(fp.fetch("docs/summary_file_behavior_ctrl.txt")), sep="\t").set_index('subid')
doc=pd.concat([pfc,ctrl])
for s,r in R.items():
    L={c:i for i,c in enumerate(r['label'])}
    pl=[L[c] for c in ('P7','PO7','O1')]; pr=[L[c] for c in ('P8','PO8','O2')]
    e1,e2=r['erp_enc_1'],r['erp_enc_2']
    t=np.arange(385)/256; w=(t>0.08)&(t<0.25)
    lat=((e2[pl].mean(0)-e2[pr].mean(0))-(e1[pl].mean(0)-e1[pr].mean(0)))[w]
    csv=r['csv']; a1=csv[csv.vhf==1].correct.mean(); a2=csv[csv.vhf==2].correct.mean()
    print(s, doc.loc[s,'lesion_hem'] if s.startswith('pfc') else '-', 'lat mean %.2f absmax-signed %.2f'%(lat.mean(), lat[np.abs(lat).argmax()]), 'acc vhf1 %.2f vhf2 %.2f doc les %.2f int %.2f'%(a1,a2,doc.loc[s,'vhf_lesion'],doc.loc[s,'vhf_intact']))
EOF
```

```
ctrl06 [(57, 'P4', 'P6'), (58, 'P6', 'P8'), (59, 'P8', 'PO8'), (60, 'P10', 'PO4'), (61, 'PO8', 'O2'), (62, 'PO4', 'P4')]
ctrl09 [(42, 'FT8', 'FC6'), (43, 'FC6', 'FC4'), (44, 'FC4', 'FC2'), (45, 'FC2', 'FCz'), (46, 'FCz', 'Cz'), (47, 'Cz', 'C2')]
ctrl11 [(55, 'CP2', 'P2'), (56, 'P2', 'P4'), (57, 'P4', 'P6'), (58, 'P6', 'P8'), (59, 'P8', 'P10'), (60, 'P10', 'PO8')]
ctrl19 [(19, 'P1', 'P3'), (20, 'P3', 'P5'), (21, 'P5', 'P7'), (22, 'P7', 'P9'), (23, 'P9', 'PO7'), (24, 'PO7', 'PO3')]
ctrl20 [(13, 'C5', 'T7'), (14, 'T7', 'TP7'), (15, 'TP7', 'CP5'), (16, 'CP5', 'CP3'), (17, 'CP3', 'CP1'), (18, 'CP1', 'P1')]
pfc03 [(15, 'TP7', 'CP5'), (16, 'CP5', 'CP3'), (17, 'CP3', 'CP1'), (18, 'CP1', 'P1'), (19, 'P1', 'P3'), (20, 'P3', 'P5')]
pfc06 [(27, 'Iz', 'POz'), (28, 'Oz', 'Pz'), (29, 'POz', 'CPz'), (30, 'Pz', 'Fpz'), (31, 'CPz', 'Fp2'), (32, 'Fpz', 'AF8')]
pfc07 [(14, 'T7', 'TP7'), (15, 'TP7', 'CP5'), (16, 'CP5', 'CP3'), (17, 'CP3', 'CP1'), (18, 'CP1', 'P1'), (19, 'P1', 'P3')]
pfc08 [(0, 'Fp1', 'AF7'), (1, 'AF7', 'AF3'), (2, 'AF3', 'F1'), (3, 'F1', 'F3'), (4, 'F3', 'F5'), (5, 'F5', 'F7')]
pfc09 [(9, 'FC3', 'FC1'), (10, 'FC1', 'C1'), (11, 'C1', 'C3'), (12, 'C3', 'C5'), (13, 'C5', 'T7'), (14, 'T7', 'TP7')]
pfc11 [(38, 'F2', 'F4'), (39, 'F4', 'F6'), (40, 'F6', 'F8'), (41, 'F8', 'FT8'), (42, 'FT8', 'FC6'), (43, 'FC6', 'FC4')]
pfc13 [(19, 'P1', 'P3'), (20, 'P3', 'P5'), (21, 'P5', 'P7'), (22, 'P7', 'P9'), (23, 'P9', 'PO7'), (24, 'PO7', 'O1')]
pfc14 [(13, 'C5', 'T7'), (14, 'T7', 'TP7'), (15, 'TP7', 'CP5'), (16, 'CP5', 'CP3'), (17, 'CP3', 'CP1'), (18, 'CP1', 'P1')]
ctrl01 - lat mean 0.77 absmax-signed 3.60 acc vhf1 0.93 vhf2 0.96 doc les 0.95 int 0.93
ctrl02 - lat mean -1.09 absmax-signed -5.91 acc vhf1 0.97 vhf2 0.97 doc les 0.97 int 0.98
ctrl03 - lat mean 0.59 absmax-signed 1.85 acc vhf1 0.96 vhf2 0.98 doc les 0.97 int 0.96
ctrl04 - lat mean 0.42 absmax-signed -6.02 acc vhf1 0.97 vhf2 0.98 doc les 0.97 int 0.98
ctrl05 - lat mean -0.06 absmax-signed -1.28 acc vhf1 0.98 vhf2 0.99 doc les 
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import os, glob, pickle, numpy as np
R={os.path.basename(f)[:-4]: pickle.load(open(f,'rb')) for f in sorted(glob.glob(os.environ['TMPDIR']+'/subj/*.pkl'))}
t=np.arange(385)/256
for nm,(a,b) in {'P1 90-140':(0.09,0.14),'N1 150-220':(0.15,0.22),'N1b 220-300':(0.22,0.3), 'second stim N1 350-420':(0.35,0.42)}.items():
    out={}
    for s,r in R.items():
        L={c:i for i,c in enumerate(r['label'])}
        pl=[L[c] for c in ('P7','PO7','P9','O1')]; pr=[L[c] for c in ('P8','PO8','P10','O2')]
        w=(t>=a)&(t<b)
        d=lambda e: e[pl][:,w].mean()-e[pr][:,w].mean()
        out[s]=d(r['erp_enc_2'])-d(r['erp_enc_1'])
    print(nm, 'ctrl', ''.join('+' if out[s]>0 else '-' for s in R if s.startswith('ctrl')), ' pfcL', ''.join('+' if out[s]>0 else '-' for s in ['pfc01','pfc02','pfc03','pfc04','pfc05','pfc06','pfc07']), ' pfcR', ''.join('+' if out[s]>0 else '-' for s in ['pfc08','pfc09','pfc10','pfc11','pfc12','pfc13','pfc14']))
EOF
```

```
P1 90-140 ctrl --+--+--++++-+++++--  pfcL +-+-+++  pfcR +---+-+
N1 150-220 ctrl +-+++---+-+---+-++++  pfcL +++-+++  pfcR +-+----
N1b 220-300 ctrl +-++-+-++---+-+-++--  pfcL --++-+-  pfcR -++++-+
second stim N1 350-420 ctrl -+-+---+-++++-+---++  pfcL -+--+--  pfcR --++-++
```

**Agent calls Bash**

```bash
cd entries/johnson-2017 && python3 - <<'EOF'
p='frontoparietal.py'
s=open(p).read()
s=s.replace('''# Hemisphere index channels''','''# One channel order for every subject (ctrl01's). The files do not share an order: an
# interpolated channel sits at the end of the list in some subjects.
CANON = ['Fp1', 'AF7', 'AF3', 'F1', 'F3', 'F5', 'F7', 'FT7', 'FC5', 'FC3', 'FC1', 'C1', 'C3', 'C5', 'T7',
         'TP7', 'CP5', 'CP3', 'CP1', 'P1', 'P3', 'P5', 'P7', 'P9', 'PO7', 'PO3', 'O1', 'Iz', 'Oz', 'POz', 'Pz',
         'CPz', 'Fpz', 'Fp2', 'AF8', 'AF4', 'AFz', 'Fz', 'F2', 'F4', 'F6', 'F8', 'FT8', 'FC6', 'FC4', 'FC2',
         'FCz', 'Cz', 'C2', 'C4', 'C6', 'T8', 'TP8', 'CP6', 'CP4', 'CP2', 'P2', 'P4', 'P6', 'P8', 'P10', 'PO8',
         'PO4', 'O2']

# Hemisphere index channels''')
s=s.replace('''    return res


# ----------------------------------------------------------------------------- cluster test''','''    return canonical(res)


def canonical(res: dict) -> dict:
    """Put every channel axis of a subject's results in the order CANON (the subject's own order
    is kept as 'label_file')."""
    lab = res["label"]
    if "label_file" in res or lab == CANON:
        res.setdefault("label_file", list(lab))
        res["label"] = list(CANON)
        return res
    idx = np.array([lab.index(c) for c in CANON])
    for k, v in list(res.items()):
        if not isinstance(v, np.ndarray) or v.dtype == bool:
            continue
        if k.startswith(("erp_", "tfr_enc_", "tfr_proc_", "tfr_base_mu", "tfr_base_sd")) or k == "fft":
            if v.ndim >= 1 and v.shape[0] == 64:
                res[k] = v[idx]
        elif k.startswith("psi_") and v.ndim == 3 and v.shape[:2] == (64, 64):
            res[k] = v[np.ix_(idx, idx)]
    res["label_file"] = list(lab)
    res["label"] = list(CANON)
    return res


# ----------------------------------------------------------------------------- cluster test''')
open(p,'w').write(s)
EOF
grep -n "tfr_base_N\|tfr_enc_mask\|erp_base" frontoparietal.py | head -5
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import os, glob, pickle, sys
sys.path.insert(0,'.'); import frontoparietal as fp
for f in glob.glob(os.environ['TMPDIR']+'/subj/*.pkl'):
    r=pickle.load(open(f,'rb'))
    if 'label_file' not in r:
        r=fp.canonical(r); pickle.dump(r, open(f,'wb'))
r=pickle.load(open(os.environ['TMPDIR']+'/subj/pfc08.pkl','rb')); print(r['label'][:3], r['label_file'][:3], r['label_file'][-2:])
EOF
```

```
356:    res["erp_base"] = base.astype(np.float32)
377:        res[f"tfr_base_N_{rd}"] = n
629:    N = r[f"tfr_base_N_{reading}"].astype(np.float64)[None, :]
['Fp1', 'AF7', 'AF3'] ['AF7', 'AF3', 'F1'] ['Fp1', 'PO4']
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('part2.py').read()
s=s.replace('''print("labels identical in every subject:", all(R[s]["label"] == labels for s in CTRL + PFC), "| n =", len(labels))''','''print("channel order of the files differs from ctrl01's in", sum(R[s]["label_file"] != fp.CANON for s in CTRL + PFC),
      "subjects (an interpolated channel moved to the end); every array is put in one order:", all(R[s]["label"] == fp.CANON for s in CTRL + PFC))''')
old=s[s.index('# hemifield coding and the swap'):s.index('print("neighbouring-channel correlation')]
new='''# hemifield coding and the swap
print("trial-table visual hemifield (1 left, 2 right) of the trials data_derived codes 2 ('lesioned'):",
      sorted({str(v) for v in san["lesioned_vhf_csv"]}), "in every subject")
pat_hem = pfc_doc.set_index("subid")["lesion_hem"]
print("so derived column 3 equals the trial table's hemifield in every trial, for left- and right-lesioned patients alike")
# early visual lateralisation (N1, 150-220 ms): left minus right posterior, column 3 = 2 minus = 1
t_enc = np.arange(385) / fp.FS
w_n1 = (t_enc >= 0.15) & (t_enc < 0.22)
pl4 = [L[c] for c in ("P7", "PO7", "P9", "O1")]
pr4 = [L[c] for c in ("P8", "PO8", "P10", "O2")]
def n1_lat(s):
    d = lambda e: e[pl4][:, w_n1].mean() - e[pr4][:, w_n1].mean()
    return d(R[s]["erp_enc_2"]) - d(R[s]["erp_enc_1"])
n1 = pd.Series({s: n1_lat(s) for s in CTRL + PFC})
for nm, grp in (("controls", CTRL), ("left-lesioned patients", [s for s in PFC if pat_hem[s] == "L"]),
                ("right-lesioned patients", [s for s in PFC if pat_hem[s] == "R"])):
    print(f"N1 lateralisation positive in {int((n1[grp] > 0).sum())} of {len(grp)} {nm}")
'''
s=s.replace(old,new)
old=s[s.index('# accuracy in the docs summary against the trial tables'):s.index('print("docs summary: patients"')]
new='''# accuracy in the docs summary against the trial tables, under both codings of the hemifield
def acc_vhf(s, v):
    csv = R[s]["csv"]
    return csv.loc[csv.vhf == v, "correct"].mean()
doc = pd.concat([pfc_doc.set_index("subid"), ctrl_doc.set_index("subid")])
cmp = pd.DataFrame({s: {"acc_vhf1": acc_vhf(s, 1), "acc_vhf2": acc_vhf(s, 2), "doc_lesion": doc.loc[s, "vhf_lesion"],
                        "doc_intact": doc.loc[s, "vhf_intact"]} for s in CTRL + PFC}).T
cmp["lesion_is_vhf1"] = (cmp.acc_vhf1 - cmp.doc_lesion).abs().le(0.006) & (cmp.acc_vhf2 - cmp.doc_intact).abs().le(0.006)
cmp["lesion_is_vhf2"] = (cmp.acc_vhf2 - cmp.doc_lesion).abs().le(0.006) & (cmp.acc_vhf1 - cmp.doc_intact).abs().le(0.006)
print(cmp.round(3).to_string())
for nm, grp in (("controls", CTRL), ("patients", PFC)):
    print(f"{nm}: docs 'vhf_lesion' equals the trial-table accuracy of hemifield 1 in {int(cmp.loc[grp, 'lesion_is_vhf1'].sum())}, "
          f"of hemifield 2 in {int(cmp.loc[grp, 'lesion_is_vhf2'].sum())} of {len(grp)} (within 0.006)")
'''
s=s.replace(old,new)
old=s[s.index('# %% [markdown]\n# **Do the segments share the clock'):]
new='''# %% [markdown]
# **Do the segments share the clock of the trial table?** The first shape appears at time 0 of
# the encoding-maintenance segment and the second at 200 ms, so a visual response should
# arise in posterior channels after about 80 ms and again after about 280 ms, and not before.
# Below, the posterior ERP (P7, P8, P9, P10, PO7, PO8, O1, O2), both hemifields, tested
# against zero across the 34 subjects at each time point; the threshold is the 95th
# percentile of the largest |t| when each subject's sign is flipped at random (1000 times).
# The trial tables give no event inside the processing segment other than its start.

# %%
post = [L[c] for c in ("P7", "P8", "P9", "P10", "PO7", "PO8", "O1", "O2")]
def first_response(key, n_t):
    x = np.stack([(R[s][f"{key}_1"] + R[s][f"{key}_2"])[post].mean(0) / 2 for s in CTRL + PFC])[:, :n_t]
    tv = stats.ttest_1samp(x, 0).statistic
    rng_clock = np.random.default_rng(11)
    nul = np.array([np.abs(stats.ttest_1samp(x * rng_clock.choice([-1, 1], len(x))[:, None], 0).statistic).max()
                    for _ in range(1000)])
    return tv, np.quantile(nul, 0.95)
tv, thr = first_response("erp_enc", 385)
tt = np.arange(len(tv)) / fp.FS
sig = np.flatnonzero(np.abs(tv) > thr)
print(f"encoding-maintenance: threshold |t| > {thr:.2f}; first time above it {tt[sig[0]] * 1000:.0f} ms; "
      f"peak |t| {np.abs(tv).max():.1f} at {tt[np.abs(tv).argmax()] * 1000:.0f} ms")
for a, b in ((0, 0.06), (0.06, 0.12), (0.12, 0.2), (0.2, 0.28), (0.28, 0.4), (0.4, 0.8), (0.8, 1.5)):
    w = (tt >= a) & (tt < b)
    print(f"  {a * 1000:4.0f}-{b * 1000:4.0f} ms: max |t| = {np.abs(tv[w]).max():.1f}")
tv, thr = first_response("erp_proc", 231)
tt = np.arange(len(tv)) / fp.FS
sig = np.flatnonzero(np.abs(tv) > thr)
print(f"processing: threshold {thr:.2f}; first time above it "
      f"{(tt[sig[0]] * 1000 if len(sig) else float('nan')):.0f} ms; peak |t| {np.abs(tv).max():.1f} at {tt[np.abs(tv).argmax()] * 1000:.0f} ms")
'''
s=s.replace(old,new)
open('part2.py','w').write(s)
EOF
. ../dev/bin/activate && python dev.py part1.py part2.py 2>&1 | sed -n '/^subjects: controls/,$p'
```

```
subjects: controls 20 patients 14
channel order of the files differs from ctrl01's in 13 subjects (an interpolated channel moved to the end); every array is put in one order: True
segment start times (s): [0.0]
segment samples pretrial/encmain/proc: ['([129], [385], [231])'] -> at 256 Hz: 0 to 0.5 s, 0 to 1.5 s, 0 to 0.898 s; no buffers
fsample fields: ['(255.64, 256.0, 256.0)', '(256.0, 256.0, 256.0)']
derived trials linked to one trial-table row (trial number and response time): 6369 of 6369 | trial info agrees where linked: True
subjects with two trial tables (two recording blocks): ['ctrl08', 'pfc03', 'pfc10', 'pfc11', 'pfc12', 'pfc13']
pretrial and encmain trialinfo identical: True
proc holds the same trials as encmain: True | in the same order: 0 of 34
duplicate recordings (identical first-trial sums or identical data_derived.mat): 0 0
trial-table visual hemifield (1 left, 2 right) of the trials data_derived codes 2 ('lesioned'): ['[np.int64(2)]'] in every subject
so derived column 3 equals the trial table's hemifield in every trial, for left- and right-lesioned patients alike
N1 lateralisation positive in 11 of 20 controls
N1 lateralisation positive in 6 of 7 left-lesioned patients
N1 lateralisation positive in 2 of 7 right-lesioned patients
neighbouring-channel correlation, median (range): 0.495 0.18 0.58
        acc_vhf1  acc_vhf2  doc_lesion  doc_intact  lesion_is_vhf1  lesion_is_vhf2
ctrl01     0.929     0.955        0.95        0.93           False            True
ctrl02     0.974     0.974        0.97        0.98            True           False
ctrl03     0.965     0.979        0.97        0.96           False           False
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Mon Nov  9 20:43:51 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/part3.py",
 "content": "# %% [markdown]\n# ## Behaviour\n#\n# The hemifield codes disagree (data check above): `data_derived.mat` codes visual hemifield 2\n# as \"lesioned\" (descriptor), and that code equals the trial table's \"right\" in every trial and\n# every subject; the docs summary file, whose patient values are the paper's Table S1, gives\n# the patients' lesioned-hemifield accuracy as that of trial-table hemifield 1 in 9 of 14\n# patients (all those with one trial table). Two codings are therefore run where the lesioned\n# hemifield matters:\n#\n# - **A (descriptor)**: hemifield 2 of `data_derived.mat` (trial table \"right\") is the lesioned\n#   one in every subject.\n# - **B (left/right)**: the code is left/right; the lesioned hemifield is the one contralateral\n#   to the lesion before the swap, right for left-lesioned patients and left for\n#   right-lesioned patients; controls as in A (which 10 controls were swapped is not in the\n#   data, so their lesioned side cannot be known).\n#\n# For behaviour, the docs reading (**S1**: trial-table hemifield 1 is the lesioned one, for\n# every patient) is also shown, as it is the one that reproduces Table S1.\n\n# %%\npinfo = pfc_doc.set_index(\"subid\")\ndef les_code(s, coding):\n    \"\"\"Trial-table hemifield (1 left, 2 right) taken as lesioned.\"\"\"\n    if coding == \"A\":\n        return 2\n    if coding == \"B\":\n        return 1 if (s in PFC and pinfo.loc[s, \"lesion_hem\"] == \"R\") else 2\n    if coding == \"S1\":\n        return 1 if s in PFC else 2\ndef cells(s, coding, source=\"table\"):\n    \"\"\"Accuracy and trial counts per (lesion/intact, condition); source 'table' = every trial of\n    the trial tables (after the eye-gaze exclusion), 'derived' = the trials kept in\n    data_derived.mat.\"\"\"\n    if source == \"table\":\n        d = R[s][\"csv\"][[\"correct\", \"vhf\", \"condition\"]]\n    else:\n        ti = R[s][\"encmain_trialinfo\"]\n        d = pd.DataFrame({\"correct\": ti[:, 1], \"vhf\": ti[:, 2], \"condition\": ti[:, 4]})\n    lv = les_code(s, coding)\n    out = []\n    for v, vn in ((lv, 1), (3 - lv, 0)):\n        for c in (1, 2, 3):\n            x = d.loc[(d.vhf == v) & (d.condition == c), \"correct\"]\n            out.append({\"subject\": s, \"group\": int(s in PFC), \"lesion_vhf\": vn, \"condition\": c,\n                        \"k\": int(x.sum()), \"n\": len(x), \"acc\": x.mean()})\n    return out\nbeh = {cd: pd.DataFrame([row for s in CTRL + PFC for row in cells(s, cd)]) for cd in (\"A\", \"B\", \"S1\")}\nprint(\"cells per coding:\", {k: len(v) for k, v in beh.items()}, \"| empty cells:\", int((beh[\"A\"].n == 0).sum()))\nprint(\"trials per cell, min to max:\", beh[\"A\"].n.min(), \"to\", beh[\"A\"].n.max())\n\n# %% [markdown]\n# ### cohort-and-trials\n# > The study has 14 unilateral PFC patients and 20 age- and education-matched controls; after\n# > cleaning, subjects kept on average 187 trials, 94 +- 21 (55 to 119) in the lesioned and\n# > 93 +- 22 (51 to 120) in the intact visual hemifield.\n\n# %% tags=[\"claim:cohort-and-trials\"]\nprint(\"patients\", len(PFC), \"controls\", len(CTRL))\nrows = []\nfor s in CTRL + PFC:\n    ti = R[s][\"encmain_trialinfo\"]\n    for cd in (\"A\", \"B\"):\n        lv = les_code(s, cd)\n        for rd, sel in ((\"all kept\", np.ones(len(ti), bool)), (\"correct\", ti[:, 1] == 1)):\n            rows.append({\"subject\": s, \"coding\": cd, \"reading\": rd, \"total\": int(sel.sum()),\n                         \"lesioned\": int((sel & (ti[:, 2] == lv)).sum()), \"intact\": int((sel & (ti[:, 2] == 3 - lv)).sum())})\ntc = pd.DataFrame(rows)\nsumm = tc.groupby([\"reading\", \"coding\"]).agg(\n    total_mean=(\"total\", \"mean\"), les_mean=(\"lesioned\", \"mean\"), les_sd=(\"lesioned\", lambda x: x.std(ddof=1)),\n    les_min=(\"lesioned\", \"min\"), les_max=(\"lesioned\", \"max\"), int_mean=(\"intact\", \"mean\"),\n    int_sd=(\"intact\", lambda x: x.std(ddof=1)), int_min=(\"intact\", \"min\"), int_max=(\"intact\", \"max\"))\nprint(summ.round(1).to_string())\nprint(\"ranges widened by 10% of each bound: lesioned 49.5 to 130.9, intact 45.9 to 132\")\nprint(\"\\nby group, all kept trials (coding A):\")\nprint(tc[(tc.reading == \"all kept\") & (tc.coding == \"A\")].assign(group=lambda d: np.where(d.subject.str.startswith(\"pfc\"), \"patients\", \"controls\"))\n      .groupby(\"group\")[[\"total\", \"lesioned\", \"intact\"]].agg([\"mean\", \"min\", \"max\"]).round(1).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### demographics-matched\n# > Controls do not differ from patients in age or education, nor in variance.\n\n# %% tags=[\"claim:demographics-matched\"]\nage_p, age_c = pfc_doc.test_age.astype(float), ctrl_doc.test_age.astype(float)\nedu_p, edu_c = pfc_doc.edu_yrs.astype(float), ctrl_doc.edu_yrs.astype(float)\nprint(f\"age: patients {age_p.mean():.1f} +- {age_p.std():.1f} [{age_p.min():.0f}-{age_p.max():.0f}], \"\n      f\"controls {age_c.mean():.1f} +- {age_c.std():.1f} [{age_c.min():.0f}-{age_c.max():.0f}]\")\nprint(f\"education: patients {edu_p.mean():.1f} +- {edu_p.std():.1f}, controls {edu_c.mean():.1f} +- {edu_c.std():.1f}\")\nprint(f\"males: patients {(pfc_doc.gender == 'M').sum()}, controls {(ctrl_doc.gender == 'M').sum()}\")\nfor nm, a, b in ((\"age\", age_p, age_c), (\"education\", edu_p, edu_c)):\n    t = stats.ttest_ind(a, b, equal_var=True)\n    F = a.var(ddof=1) / b.var(ddof=1)\n    print(f\"{nm}: t(32) = {t.statistic:.2f}, p = {t.pvalue:.3f}; variance F(13,19) = {F:.2f}, one-tailed p = {stats.f.sf(F, 13, 19):.3f}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### patient-factors-no-effect\n# > In patients, no lesion or demographic factor (lesion hemisphere, etiology, size, years since\n# > lesion, age, gender, education, IQ) nor visual hemifield or condition has a significant\n# > effect on accuracy, which permits pooling the patients into one group.\n#\n# Between-subject terms as Table S2 lists them; factors coded +-1 (Type III), covariates as\n# recorded in `docs/summary_file_behavior_pfc.txt`; etiology is stroke against tumour\n# resection (Results: \"a single stroke or surgical resection of a low-grade tumor\").\n\n# %% tags=[\"claim:patient-factors-no-effect\"]\npi_ = pinfo.loc[PFC]\nhem = np.where(pi_.lesion_hem == \"L\", 1.0, -1.0)\neti = np.where(pi_.lesion_etiology == \"Stroke\", 1.0, -1.0)\ngen = np.where(pi_.gender == \"M\", 1.0, -1.0)\nB = np.column_stack([hem, eti, pi_.lesion_size, pi_.elapsed_yrs, pi_.test_age, gen, pi_.edu_yrs, pi_.iq,\n                     hem * eti, hem * gen, eti * gen]).astype(float)\nbnames = [\"Hemisphere\", \"Etiology\", \"Size\", \"Elapsed\", \"Age\", \"Gender\", \"Education\", \"IQ\",\n          \"Hemisphere x Etiology\", \"Hemisphere x Gender\", \"Etiology x Gender\"]\nprint(\"etiology, stroke:\", int((eti > 0).sum()), \"tumour resection:\", int((eti < 0).sum()))\nanc = {}\nfor cd in (\"S1\", \"B\"):\n    b = beh[cd][beh[cd].group == 1]\n    Y = np.stack([b[b.subject == s].sort_values([\"lesion_vhf\", \"condition\"], ascending=[False, True]).acc.to_numpy().reshape(2, 3)\n                  for s in PFC])\n    anc[cd] = pd.DataFrame(fp.ancova_rm(Y, B, bnames)).set_index(\"term\")\nboth = anc[\"S1\"][[\"F\", \"df1\", \"df2\", \"partial_eta2\", \"p\"]].join(anc[\"B\"][[\"F\", \"p\"]], rsuffix=\"_codingB\")\nprint(both.round(3).to_string())\nfor cd in (\"S1\", \"B\"):\n    print(f\"coding {cd}: smallest p = {anc[cd].p.min():.3f} ({anc[cd].p.idxmin()}); terms with p < 0.05: {int((anc[cd].p < 0.05).sum())}\")\nprint(\"(coding A gives the same F values as S1: it swaps lesion and intact in every patient)\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### table-s1-patient-accuracy\n# > Each patient's accuracy in the lesioned and intact visual hemifield is as Table S1 lists,\n# > from 0.65 to 0.98.\n#\n# The reference values are Table S1's, typed from the paper (patients 1 to 14, lesion then\n# intact hemifield); `pfc01` to `pfc14` are taken as patients 1 to 14, whose lesion hemisphere,\n# etiology, size, age and gender in the docs file match the table row by row (checked below).\n\n# %% tags=[\"claim:table-s1-patient-accuracy\"]\nTABLE_S1 = {1: (0.88, 0.85), 2: (0.65, 0.68), 3: (0.98, 0.98), 4: (0.83, 0.85), 5: (0.91, 0.88),\n            6: (0.97, 0.94), 7: (0.81, 0.92), 8: (0.97, 0.92), 9: (0.86, 0.96), 10: (0.88, 0.92),\n            11: (0.79, 0.70), 12: (0.92, 0.89), 13: (0.92, 0.88), 14: (0.82, 0.80)}\nTABLE_S1_ROWS = {1: (\"L\", 27.44, 48, \"F\"), 2: (\"L\", 46.86, 54, \"M\"), 3: (\"L\", 0.57, 46, \"M\"), 4: (\"L\", 54.94, 34, \"M\"),\n                 5: (\"L\", 77.61, 64, \"F\"), 6: (\"L\", 185.56, 57, \"F\"), 7: (\"L\", 11.11, 71, \"F\"), 8: (\"R\", 30.81, 22, \"F\"),\n                 9: (\"R\", 4.74, 20, \"F\"), 10: (\"R\", 10.84, 41, \"M\"), 11: (\"R\", 56.83, 37, \"M\"), 12: (\"R\", 38.09, 29, \"F\"),\n                 13: (\"R\", 14.87, 62, \"F\"), 14: (\"R\", 32.22, 64, \"F\")}\nmatch_rows = all((pinfo.loc[f\"pfc{i:02d}\", \"lesion_hem\"], round(pinfo.loc[f\"pfc{i:02d}\", \"lesion_size\"], 2),\n                  pinfo.loc[f\"pfc{i:02d}\", \"test_age\"], pinfo.loc[f\"pfc{i:02d}\", \"gender\"]) == v for i, v in TABLE_S1_ROWS.items())\nprint(\"docs rows match Table S1 rows (hemisphere, size, age, gender):\", match_rows)\nprint(\"docs vhf_lesion/vhf_intact equal Table S1:\",\n      all((pinfo.loc[f\"pfc{i:02d}\", \"vhf_lesion\"], pinfo.loc[f\"pfc{i:02d}\", \"vhf_intact\"]) == v for i, v in TABLE_S1.items()))\nres_s1 = {}\nfor cd in (\"S1\", \"A\", \"B\"):\n    for src in (\"table\", \"derived\"):\n        vals = []\n        for i in range(1, 15):\n            s = f\"pfc{i:02d}\"\n            c = pd.DataFrame(cells(s, cd, src))\n            les = c[c.lesion_vhf == 1].k.sum() / c[c.lesion_vhf == 1].n.sum()\n            itc = c[c.lesion_vhf == 0].k.sum() / c[c.lesion_vhf == 0].n.sum()\n            vals += [(s, \"lesion\", les, TABLE_S1[i][0]), (s, \"intact\", itc, TABLE_S1[i][1])]\n        v = pd.DataFrame(vals, columns=[\"subject\", \"vhf\", \"measured\", \"table_s1\"])\n        v[\"diff\"] = v.measured - v.table_s1\n        res_s1[(cd, src)] = v\n        print(f\"coding {cd:2s}, {src:7s} trials: {int((v['diff'].abs() <= 0.02 + 1e-9).sum())} of 28 within 0.02; \"\n              f\"median |diff| {v['diff'].abs().median():.3f}; measured range {v.measured.min():.2f} to {v.measured.max():.2f}\")\nv = res_s1[(\"S1\", \"table\")]\nprint(v.assign(measured=v.measured.round(3), diff=v[\"diff\"].round(3)).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### accuracy-patients-impaired\n# > PFC patients are less accurate than controls (mean +- SD 0.87 +- 0.08 against 0.95 +-\n# > 0.03), a group effect with p < 7 x 10^-5 in the mixed-effects model with group as the only\n# > fixed effect.\n\n# %% tags=[\"claim:accuracy-patients-impaired\"]\nb = beh[\"A\"].copy()\nb[\"cond_f\"] = b.condition.astype(str)\nacc_all = {s: R[s][\"csv\"].correct.mean() for s in CTRL + PFC}\nacc_cell = b.groupby(\"subject\").acc.mean()\nfor nm, a in ((\"(a) all trials\", pd.Series(acc_all)), (\"(b) mean of six cells\", acc_cell)):\n    print(f\"{nm}: controls {a[CTRL].mean():.3f} +- {a[CTRL].std():.3f}, patients {a[PFC].mean():.3f} +- {a[PFC].std():.3f}\")\nprint(\"\\nper-group accuracy, by subject (a):\")\nprint(\"  controls\", np.round([acc_all[s] for s in CTRL], 2))\nprint(\"  patients\", np.round([acc_all[s] for s in PFC], 2))\nlm = {}\nlm[\"group only, linear\"] = fp.lmm_wald(b, \"acc ~ group\")\nlm[\"full, linear, condition as number\"] = fp.lmm_wald(b, \"acc ~ group * lesion_vhf * condition\")\nlm[\"full, linear, condition as factor\"] = fp.lmm_wald(b, \"acc ~ group * lesion_vhf * cond_f\")\nXg = np.column_stack([np.ones(len(b)), b.group])\nlm[\"group only, binomial logit\"] = fp.glmm_binomial(b.k.to_numpy(float), b.n.to_numpy(float), Xg, b.subject.to_numpy(), [\"Intercept\", \"group\"])\nXf = np.column_stack([np.ones(len(b)), b.group, b.lesion_vhf, b.condition, b.group * b.lesion_vhf, b.group * b.condition,\n                      b.lesion_vhf * b.condition, b.group * b.lesion_vhf * b.condition]).astype(float)\nnf_ = [\"Intercept\", \"group\", \"lesion_vhf\", \"condition\", \"group:lesion_vhf\", \"group:condition\", \"lesion_vhf:condition\", \"group:lesion_vhf:condition\"]\nlm[\"full, binomial logit, condition as number\"] = fp.glmm_binomial(b.k.to_numpy(float), b.n.to_numpy(float), Xf, b.subject.to_numpy(), nf_)\nfor k, v in lm.items():\n    g = v[\"group\"]\n    print(f\"{k:45s} group: beta {g['beta']:+.3f}, F(1,{g['df2']}) = {g['F']:.2f}, p = {g['p']:.2e}\")\nd_cohen = (np.mean([acc_all[s] for s in CTRL]) - np.mean([acc_all[s] for s in PFC])) / np.sqrt(\n    (19 * np.var([acc_all[s] for s in CTRL], ddof=1) + 13 * np.var([acc_all[s] for s in PFC], ddof=1)) / 32)\nprint(f\"Cohen's d (pooled SD, subject accuracies) = {d_cohen:.2f}\")\nprint(\"binomial fits converged:\", lm[\"group only, binomial logit\"][\"_converged\"], lm[\"full, binomial logit, condition as number\"][\"_converged\"])\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### patients-above-chance\n# > Despite the impairment, patients perform well above the 0.5 chance rate.\n\n# %% tags=[\"claim:patients-above-chance\"]\nbp = beh[\"S1\"][beh[\"S1\"].group == 1]\ndef t_chance(x):\n    t = stats.ttest_1samp(x, 0.5, alternative=\"greater\")\n    return t.statistic, t.pvalue\nt_a = t_chance(np.array([acc_all[s] for s in PFC]))\nprint(f\"(a) overall: t(13) = {t_a[0]:.2f}, one-tailed p = {t_a[1]:.1e}\")\nfor vn, nm in ((1, \"lesion\"), (0, \"intact\")):\n    x = bp[bp.lesion_vhf == vn].groupby(\"subject\").apply(lambda d: d.k.sum() / d.n.sum(), include_groups=False)\n    t = t_chance(x.to_numpy())\n    print(f\"(b) {nm} hemifield (Table S1 coding): t(13) = {t[0]:.2f}, p = {t[1]:.1e}\")\nfor vn, nm in ((1, \"lesion\"), (0, \"intact\")):\n    for c in (1, 2, 3):\n        x = bp[(bp.lesion_vhf == vn) & (bp.condition == c)].acc.to_numpy()\n        t = t_chance(x)\n        print(f\"(c) {nm}, condition {c}: t(13) = {t[0]:.2f}, p = {t[1]:.1e}, min accuracy {x.min():.2f}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### accuracy-no-hemifield-condition-effect\n# > Accuracy does not differ between visual hemifield presentations or between conditions.\n\n# %% tags=[\"claim:accuracy-no-hemifield-condition-effect\"]\nm3 = {\"linear\": fp.lmm_wald(b, \"acc ~ lesion_vhf * condition\")}\nX3 = np.column_stack([np.ones(len(b)), b.lesion_vhf, b.condition, b.lesion_vhf * b.condition]).astype(float)\nm3[\"binomial logit\"] = fp.glmm_binomial(b.k.to_numpy(float), b.n.to_numpy(float), X3, b.subject.to_numpy(),\n                                        [\"Intercept\", \"lesion_vhf\", \"condition\", \"lesion_vhf:condition\"])\nm3[\"linear, condition as factor\"] = fp.lmm_wald(b, \"acc ~ lesion_vhf * cond_f\")\nfor k, v in m3.items():\n    for term, r_ in v.items():\n        if term.startswith(\"_\"):\n            continue\n        print(f\"{k:28s} {term:28s} beta {r_['beta']:+.4f}  F(1,{r_['df2']}) = {r_['F']:.2f}  p = {r_['p']:.3f}\")\nprint(\"\\nvariant, full model (Table S3 first model), coding A:\")\nfor k in (\"full, linear, condition as number\", \"full, binomial logit, condition as number\"):\n    for term in (\"lesion_vhf\", \"condition\", \"lesion_vhf:condition\"):\n        r_ = lm[k][term]\n        print(f\"  {k:42s} {term:22s} F = {r_['F']:.2f}  p = {r_['p']:.3f}\")\nbB = beh[\"B\"]\nr_B = fp.lmm_wald(bB, \"acc ~ lesion_vhf * condition\")\nprint(\"coding B, linear:\", {k: round(v[\"p\"], 3) for k, v in r_B.items()})\nprint(\"mean accuracy by hemifield (coding A, subject means of cells):\", b.groupby(\"lesion_vhf\").acc.mean().round(3).to_dict(),\n      \"| by condition:\", b.groupby(\"condition\").acc.mean().round(3).to_dict())\n\n# %% [markdown]\n# **Result: ...**\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/part3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/    x = np.stack(\[(R\[s\]\[f"{key}_1"\] + R\[s\]\[f"{key}_2"\])\[post\].mean(0) \/ 2 for s in CTRL + PFC\])\[:, :n_t\]/    x = np.stack([(R[s][f"{key}_1"] + R[s][f"{key}_2"])[post].mean(0) \/ 2 for s in CTRL + PFC])[:, :n_t]\n    x = x - x[:, :13].mean(1, keepdims=True)          # change from the first 50 ms/' part2.py && sed -i 's/# percentile of the largest |t| when each subject.s sign is flipped at random (1000 times)./# percentile of the largest |t| when each subject'"'"'s sign is flipped at random (1000 times).\n# Each subject'"'"'s ERP is taken relative to its mean over the first 50 ms, as the pretrial\n# baseline lies 1.5 s earlier and the start screen leaves an offset./' part2.py && . ../dev/bin/activate && python dev.py part1.py part2.py part3.py 2>&1 | sed -n '/^encoding-maintenance/,$p'
```

```
encoding-maintenance: threshold |t| > 3.64; first time above it 656 ms; peak |t| 5.9 at 684 ms
     0-  60 ms: max |t| = 1.1
    60- 120 ms: max |t| = 1.9
   120- 200 ms: max |t| = 2.0
   200- 280 ms: max |t| = 1.9
   280- 400 ms: max |t| = 2.1
   400- 800 ms: max |t| = 5.9
   800-1500 ms: max |t| = 5.7
processing: threshold 2.94; first time above it 20 ms; peak |t| 8.2 at 836 ms
cells per coding: {'A': 204, 'B': 204, 'S1': 204} | empty cells: 0
trials per cell, min to max: 19 to 40
patients 14 controls 20
                 total_mean  les_mean  les_sd  les_min  les_max  int_mean  int_sd  int_min  int_max
reading  coding                                                                                    
all kept A            187.3      94.4    21.1       55      119      93.0    22.1       51      120
         B            187.3      93.7    21.5       55      119      93.6    21.8       51      120
correct  A            172.4      87.1    21.2       36      112      85.2    21.7       34      116
         B            172.4      86.8    21.5       36      112      85.6    21.4       34      116
ranges widened by 10% of each bound: lesioned 49.5 to 130.9, intact 45.9 to 132

[... 159 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/part4.py",
 "content": "# %% [markdown]\n# ## EEG: group tests\n#\n# Every group test below is the cluster test of the paper's scripts (`*_stat_group.m`,\n# `*_stat_group_hem.m`): independent-samples t of controls minus patients, cluster-forming\n# threshold p < 0.05 two-tailed (|t(32)| > 2.04), cluster size the sum of t, FieldTrip's\n# biosemi64 neighbours with minnbchan = 2, 1000 shuffles of the group labels, p doubled\n# (correcttail 'prob'). A positive cluster means controls above patients. The hemisphere index\n# is left (lesioned) minus right (intact) homolog, 27 channels. Hemifield h = 2 is the\n# \"lesioned\" hemifield of coding A, h = 1 the \"intact\" one.\n\n# %%\nSEED = {\"erp\": 101, \"fft\": 202, \"pow\": 303, \"psi\": 404, \"deg\": 505}\ndef hfor(s, h, coding=\"A\"):\n    if coding == \"B\" and s in PFC and pinfo.loc[s, \"lesion_hem\"] == \"R\":\n        return 3 - h\n    return h\ndef stack(key, h=None, coding=\"A\", fn=None):\n    \"\"\"Controls and patients stacked; key may contain {h}.\"\"\"\n    def one(s):\n        v = R[s][key.format(h=hfor(s, h, coding))] if h is not None else R[s][key]\n        return fn(v) if fn else v\n    return np.stack([one(s) for s in CTRL]), np.stack([one(s) for s in PFC])\nHEM_LABELS = fp.LEFT\ndef describe(res, chans, axes, n=4, pmax=1.01):\n    \"\"\"Print the n most significant clusters: sign, p, sum of t, channels, and the span of each\n    other axis. axes: list of (name, values, unit).\"\"\"\n    out = []\n    for c in res[\"clusters\"][:n]:\n        if c[\"p\"] > pmax:\n            continue\n        m = c[\"mask\"]\n        ch = [chans[i] for i in np.flatnonzero(m.reshape(m.shape[0], -1).any(1))]\n        spans = []\n        for k, (nm, vals, unit) in enumerate(axes):\n            other = tuple(i for i in range(m.ndim) if i != k + 1)\n            idx = np.flatnonzero(m.any(axis=other))\n            spans.append(f\"{nm} {vals[idx[0]]:g}-{vals[idx[-1]]:g} {unit}\")\n        out.append(c)\n        print(f\"   {'+' if c['sign'] > 0 else '-'} p = {c['p']:.3f}  sum t = {c['stat']:.1f}  {', '.join(spans)}  \"\n              f\"channels ({len(ch)}): {' '.join(ch[:20])}{' ...' if len(ch) > 20 else ''}\")\n    if not res[\"clusters\"]:\n        print(\"   no cluster\")\n    return out\ndef minp(res, sign=None):\n    ps = [c[\"p\"] for c in res[\"clusters\"] if sign is None or c[\"sign\"] == sign]\n    return min(ps) if ps else 1.0\nt_enc_ms = np.arange(385) / fp.FS * 1000\nt_proc_ms = np.arange(231) / fp.FS * 1000\nTESTS = {}\nt_tests = time.time()\n\n# %% [markdown]\n# ### erp-lesioned-maintenance\n# > For stimuli presented to the lesioned visual hemifield, patients show attenuated positive\n# > ERPs in posterior channels and reversed-polarity signals in lesioned-hemisphere anterior\n# > channels early in maintenance.\n\n# %% tags=[\"claim:erp-lesioned-maintenance\"]\nPOST_S2 = [\"P6\", \"P8\", \"P10\", \"PO8\"]\nANT_ERP = [\"F5\", \"F7\", \"FC5\", \"FT7\", \"C3\", \"C5\", \"T7\"]\nfor coding in (\"A\", \"B\"):\n    x1, x2 = stack(\"erp_enc_{h}\", 2, coding)\n    res = fp.cluster_test(x1, x2, ADJ, seed=SEED[\"erp\"])\n    TESTS[(\"erp_enc_main\", 2, coding)] = res\n    print(f\"coding {coding}: encoding-maintenance, lesioned hemifield, group main effect\")\n    describe(res, labels, [(\"time\", t_enc_ms, \"ms\")], n=6)\n    for c in res[\"clusters\"]:\n        if c[\"p\"] >= 0.05:\n            continue\n        m = c[\"mask\"]\n        tmask = m.any(0)\n        late = t_enc_ms[tmask].max() > 400\n        post = any(m[L[ch]].any() for ch in POST_S2)\n        ant = [ch for ch in ANT_ERP if m[L[ch]].any()]\n        mc = x1.mean(0)[m].mean()\n        mp = x2.mean(0)[m].mean()\n        print(f\"   cluster p = {c['p']:.3f}: extends past 400 ms {late}; includes P6/P8/P10/PO8 {post}; \"\n              f\"anterior channels {ant}; mean ERP in cluster controls {mc:.2f}, patients {mp:.2f}\")\nprint(\"posterior P6-P8-P10-PO8, 400-800 ms, mean ERP (coding A): controls %.2f, patients %.2f\" % (\n    stack(\"erp_enc_{h}\", 2)[0][:, [L[c] for c in POST_S2]][:, :, (t_enc_ms >= 400) & (t_enc_ms < 800)].mean(),\n    stack(\"erp_enc_{h}\", 2)[1][:, [L[c] for c in POST_S2]][:, :, (t_enc_ms >= 400) & (t_enc_ms < 800)].mean()))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### erp-processing-interaction\n# > At active processing, for lesioned-hemifield stimuli, ERPs show a group by hemisphere\n# > interaction without a group main effect; patients have enhanced signal in\n# > lesioned-hemisphere anterior channels 100 ms after the test prompt, relative to the intact\n# > homologs.\n#\n# The processing segment is aligned to the encoding segment by trial number (the file stores\n# it in another order). Variant: the selection of `erp_compute.m`, which applies the encoding\n# segment's trial indices to the processing segment as stored.\n\n# %% tags=[\"claim:erp-processing-interaction\"]\nANT_PROC = [\"Fp1\", \"AF3\", \"AF7\", \"F5\", \"F7\", \"FC5\", \"FT7\"]\nfor coding, key in ((\"A\", \"erp_proc_{h}\"), (\"B\", \"erp_proc_{h}\"), (\"A\", \"erp_proc_codeidx_{h}\")):\n    tag = f\"coding {coding}\" + (\", erp_compute.m trial selection\" if \"codeidx\" in key else \"\")\n    x1, x2 = stack(key, 2, coding)\n    rh = fp.cluster_test(fp.hem_index(x1, labels), fp.hem_index(x2, labels), ADJ_HEM, seed=SEED[\"erp\"])\n    rm = fp.cluster_test(x1, x2, ADJ, seed=SEED[\"erp\"])\n    TESTS[(\"erp_proc_hem\", 2, coding, key)] = rh\n    TESTS[(\"erp_proc_main\", 2, coding, key)] = rm\n    print(f\"{tag}: group x hemisphere\")\n    describe(rh, HEM_LABELS, [(\"time\", t_proc_ms, \"ms\")], n=4)\n    for c in rh[\"clusters\"]:\n        if c[\"p\"] < 0.05:\n            m = c[\"mask\"]\n            ant = [ch for ch in ANT_PROC if ch in HEM_LABELS and m[HEM_LABELS.index(ch)].any()]\n            tm = t_proc_ms[m.any(0)]\n            print(f\"     p = {c['p']:.3f}: sign {c['sign']} (negative = patients' index above controls'), \"\n                  f\"time {tm.min():.0f}-{tm.max():.0f} ms, anterior channels {ant}\")\n    print(f\"{tag}: group main effect, smallest cluster p = {minp(rm):.3f}\")\n    describe(rm, labels, [(\"time\", t_proc_ms, \"ms\")], n=2)\nhi1, hi2 = (fp.hem_index(x, labels) for x in stack(\"erp_proc_{h}\", 2))\nw100 = (t_proc_ms >= 50) & (t_proc_ms <= 150)\nai = [HEM_LABELS.index(c) for c in ANT_PROC if c in HEM_LABELS]\nprint(\"index over FP1-AF3-AF7-F5-F7-FC5-FT7, 50-150 ms (coding A): controls %.2f, patients %.2f\" % (\n    hi1[:, ai][:, :, w100].mean(), hi2[:, ai][:, :, w100].mean()))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### erp-intact-none\n# > None of the ERP group effects is seen when stimuli are presented to the intact visual\n# > hemifield.\n\n# %% tags=[\"claim:erp-intact-none\"]\nfor coding in (\"A\", \"B\"):\n    x1, x2 = stack(\"erp_enc_{h}\", 1, coding)\n    r1 = fp.cluster_test(x1, x2, ADJ, seed=SEED[\"erp\"])\n    x1, x2 = stack(\"erp_proc_{h}\", 1, coding)\n    r2 = fp.cluster_test(x1, x2, ADJ, seed=SEED[\"erp\"])\n    r3 = fp.cluster_test(fp.hem_index(x1, labels), fp.hem_index(x2, labels), ADJ_HEM, seed=SEED[\"erp\"])\n    for nm, r_, ch, tm in ((\"encoding-maintenance main effect\", r1, labels, t_enc_ms),\n                           (\"processing main effect\", r2, labels, t_proc_ms),\n                           (\"processing group x hemisphere\", r3, HEM_LABELS, t_proc_ms)):\n        TESTS[(\"erp_intact\", nm, coding)] = r_\n        print(f\"coding {coding}, intact hemifield, {nm}: smallest cluster p = {minp(r_):.3f}\")\n        describe(r_, ch, [(\"time\", tm, \"ms\")], n=2)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### baseline-spectral-interaction\n# > In the pretrial baseline, patients have higher raw power between 6 and 18 Hz in\n# > lesioned-hemisphere anterior channels (AF3, F3, F5) than in the intact homologs, a group by\n# > hemisphere interaction (a steepened spectral slope over the lesion).\n#\n# All trials, 500 ms pretrial segment, Hanning taper, zero padded to 7.5 s (`fft_compute.m`),\n# 1 to 40 Hz, raw power averaged over trials.\n\n# %% tags=[\"claim:baseline-spectral-interaction\"]\nf1, f2 = stack(\"fft\")\nrf = fp.cluster_test(fp.hem_index(f1, labels), fp.hem_index(f2, labels), ADJ_HEM, seed=SEED[\"fft\"])\nTESTS[\"fft_hem\"] = rf\nprint(\"baseline power, group x hemisphere:\")\ndescribe(rf, HEM_LABELS, [(\"frequency\", fp.FREQS, \"Hz\")], n=5)\nai = [HEM_LABELS.index(c) for c in (\"AF3\", \"F3\", \"F5\")]\nfr = (fp.FREQS >= 6) & (fp.FREQS <= 18)\ni1, i2 = fp.hem_index(f1, labels), fp.hem_index(f2, labels)\nprint(\"index AF3-F3-F5, 6-18 Hz: controls %.3f, patients %.3f\" % (i1[:, ai][:, :, fr].mean(), i2[:, ai][:, :, fr].mean()))\nprint(\"per patient:\", np.round(i2[:, ai][:, :, fr].mean((1, 2)), 2))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### baseline-no-group-effect\n# > Baseline raw power shows no main effect of group.\n\n# %% tags=[\"claim:baseline-no-group-effect\"]\nrf2 = fp.cluster_test(f1, f2, ADJ, seed=SEED[\"fft\"])\nTESTS[\"fft_main\"] = rf2\nprint(f\"baseline power, group main effect: smallest cluster p = {minp(rf2):.3f}\")\ndescribe(rf2, labels, [(\"frequency\", fp.FREQS, \"Hz\")], n=4)\ntt_ = stats.ttest_ind(f1, f2, axis=0)\nprint(f\"channel-frequency points with uncorrected p < 0.05: {int((tt_.pvalue < 0.05).sum())} of {tt_.pvalue.size}\")\npl8 = [L[c] for c in (\"P1\", \"P3\", \"P5\", \"P7\", \"P9\", \"PO3\", \"PO7\", \"O1\")]\na8 = (fp.FREQS >= 8) & (fp.FREQS <= 12)\nprint(\"posterior lesioned-side alpha (8-12 Hz) power: controls %.2f, patients %.2f\" % (f1[:, pl8][:, :, a8].mean(), f2[:, pl8][:, :, a8].mean()))\n\n# %% [markdown]\n# **Result: ...**\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/part4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && . ../dev/bin/activate && time python dev.py part1.py part2.py part3.py part4.py 2>&1 | sed -n '/^coding A: encoding-maintenance/,$p' | grep -v Warning | grep -v "smf.mixedlm"
```

```
coding A: encoding-maintenance, lesioned hemifield, group main effect
   - p = 0.006  sum t = -391.9  time 820.312-886.719 ms  channels (15): AF7 F5 F7 FT7 FC5 FC3 C1 C3 C5 T7 P1 Pz CPz Cz CP2
   + p = 0.014  sum t = 309.1  time 753.906-863.281 ms  channels (6): TP8 P4 P6 P8 P10 PO8
   + p = 0.206  sum t = 169.9  time 800.781-867.188 ms  channels (7): CP3 CP1 P3 P5 P7 P9 PO7
   + p = 0.562  sum t = 118.9  time 335.938-382.812 ms  channels (5): Fp1 AF3 F1 F3 AFz
   - p = 0.794  sum t = -104.1  time 917.969-953.125 ms  channels (10): CP1 P1 P3 P5 PO3 Pz CPz CP2 P2 P4
   + p = 0.842  sum t = 99.4  time 1144.53-1187.5 ms  channels (6): F3 F5 FC3 C1 C3 CP1
   cluster p = 0.006: extends past 400 ms True; includes P6/P8/P10/PO8 False; anterior channels ['F5', 'F7', 'FC5', 'FT7', 'C3', 'C5', 'T7']; mean ERP in cluster controls -0.33, patients 0.52
   cluster p = 0.014: extends past 400 ms True; includes P6/P8/P10/PO8 True; anterior channels []; mean ERP in cluster controls 1.23, patients -0.09
coding B: encoding-maintenance, lesioned hemifield, group main effect
   - p = 0.070  sum t = -209.1  time 820.312-871.094 ms  channels (15): F5 F7 FT7 FC5 C5 T7 CP3 CP1 P1 Pz CPz Cz C2 C4 C6
   - p = 0.386  sum t = -141.0  time 902.344-960.938 ms  channels (13): TP7 CP5 CP1 P1 P3 P5 P7 PO7 Pz CPz Cz CP2 P2
   + p = 0.900  sum t = 99.1  time 1156.25-1191.41 ms  channels (7): C1 C3 TP7 CP5 CP3 P3 P5
   + p = 0.932  sum t = 96.9  time 828.125-867.188 ms  channels (4): P5 P7 P9 PO7
   + p = 0.970  sum t = 95.0  time 765.625-804.688 ms  channels (4): P4 P6 P8 PO8
   + p = 1.000  sum t = 40.3  time 332.031-347.656 ms  channels (4): Fp1 AF3 Fpz AFz
posterior P6-P8-P10-PO8, 400-800 ms, mean ERP (coding A): controls 0.24, patients 0.12
coding A: group x hemisphere
   - p = 0.294  sum t = -92.8  time 332.031-355.469 ms  channels (8): C5 CP5 CP3 P3 P5 P7 PO7 PO3
   + p = 1.000  sum t = 14.3  time 613.281-617.188 ms  channels (3): F1 F3 FC1
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Mon Nov  9 20:46:56 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/part5.py",
 "content": "# %% [markdown]\n# ## Task-induced power\n#\n# Readings run for every power claim (data check: the segments have no buffers):\n# - window **pad**: the 3/f windows run into the zero padding, so every frequency has values\n#   (the assumption adopted; it is the only reading under which the 3-4 Hz results of the paper\n#   exist); **fit**: FieldTrip's rule, NaN wherever the window leaves the segment, which leaves no\n#   baseline below 7 Hz and nothing at 3-4 Hz.\n# - r of the bootstrap: **hemifield** (`zbaseline.m`, the trials being scored) or **all** (the\n#   Methods' \"number of trials in that subject's dataset\").\n\n# %%\nt_enc_s = R[CTRL[0]][\"tfr_enc_time\"]\nt_proc_s = R[CTRL[0]][\"tfr_proc_time\"]\ndef zstack(seg, h, reading=\"pad\", r_mode=\"hemifield\", coding=\"A\"):\n    return stack(f\"tfr_{seg}_{{h}}\", h, coding, fn=None) if False else (\n        np.stack([fp.power_z(R[s], seg, hfor(s, h, coding), reading, r_mode) for s in CTRL]),\n        np.stack([fp.power_z(R[s], seg, hfor(s, h, coding), reading, r_mode) for s in PFC]))\ndef band_course(z, chans, fmin, fmax):\n    \"\"\"Mean over channels and frequencies (NaN-aware) -> (subjects, time).\"\"\"\n    fi = (fp.FREQS >= fmin) & (fp.FREQS <= fmax)\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\", RuntimeWarning)\n        return np.nanmean(z[:, [L[c] for c in chans]][:, :, fi], axis=(1, 2))\nANT_S4 = [\"AF7\", \"F5\", \"F7\", \"FC5\", \"FT7\"]\nPOST_S4 = [\"P1\", \"P3\", \"P5\", \"P7\", \"P9\", \"PO3\", \"PO7\", \"O1\"]\n\n# %% [markdown]\n# ### power-anterior-theta-controls\n# > In controls, delta-theta (2 to 7 Hz) power in anterior channels rises during\n# > encoding-maintenance and stays elevated through active processing, where it peaks, above\n# > Z = 3.29 against the pretrial baseline.\n\n# %% tags=[\"claim:power-anterior-theta-controls\"]\nrows = []\nfor reading in (\"pad\", \"fit\"):\n    for r_mode in (\"hemifield\", \"all\"):\n        ce = {h: band_course(zstack(\"enc\", h, reading, r_mode)[0], ANT_S4, 2, 7) for h in (1, 2)}\n        cp = {h: band_course(zstack(\"proc\", h, reading, r_mode)[0], ANT_S4, 2, 7) for h in (1, 2)}\n        for hf in (\"pooled\", 1, 2):\n            e = (ce[1] + ce[2]) / 2 if hf == \"pooled\" else ce[hf]\n            p = (cp[1] + cp[2]) / 2 if hf == \"pooled\" else cp[hf]\n            with warnings.catch_warnings():\n                warnings.simplefilter(\"ignore\", RuntimeWarning)\n                ge, gp = np.nanmean(e, 0), np.nanmean(p, 0)\n            full = np.concatenate([ge, gp])\n            peak_in_proc = bool(np.nanargmax(full) >= len(ge)) if np.isfinite(full).any() else False\n            maj_p = np.nanmean(p > 3.29, 0) if np.isfinite(p).any() else np.array([np.nan])\n            rows.append({\"window\": reading, \"r\": r_mode, \"hemifield\": hf,\n                         \"enc mean Z 0-0.4 s\": np.nanmean(ge[t_enc_s < 0.4]) if np.isfinite(ge).any() else np.nan,\n                         \"enc mean Z 0.4-1.5 s\": np.nanmean(ge[t_enc_s >= 0.4]) if np.isfinite(ge).any() else np.nan,\n                         \"proc max group-mean Z\": np.nanmax(gp) if np.isfinite(gp).any() else np.nan,\n                         \"proc frac. time group mean > 3.29\": np.nanmean(gp > 3.29) if np.isfinite(gp).any() else np.nan,\n                         \"max fraction of controls > 3.29 (proc)\": np.nanmax(maj_p),\n                         \"group-mean max lies in proc\": peak_in_proc,\n                         \"time of max (s, proc if in proc)\": (t_proc_s[np.nanargmax(gp)] if peak_in_proc else t_enc_s[np.nanargmax(ge)]) if np.isfinite(full).any() else np.nan})\ntab = pd.DataFrame(rows)\nwith pd.option_context(\"display.width\", 250, \"display.max_columns\", 20):\n    print(tab.round(2).to_string())\ne = (band_course(zstack(\"enc\", 1)[0], ANT_S4, 2, 7) + band_course(zstack(\"enc\", 2)[0], ANT_S4, 2, 7)) / 2\np = (band_course(zstack(\"proc\", 1)[0], ANT_S4, 2, 7) + band_course(zstack(\"proc\", 2)[0], ANT_S4, 2, 7)) / 2\nprint(\"\\nper control (pad, r hemifield, pooled): max Z in processing\", np.round(np.nanmax(p, 1), 1))\nprint(\"                                         max Z in encoding-maintenance\", np.round(np.nanmax(e, 1), 1))\nprint(\"group mean course, encoding-maintenance every 100 ms:\", np.round(e.mean(0)[::10], 1))\nprint(\"group mean course, processing every 100 ms:\", np.round(p.mean(0)[::10], 1))\nfig, ax = plt.subplots(figsize=(7, 3))\nax.plot(t_enc_s, e.mean(0), label=\"encoding-maintenance\")\nax.plot(1.5 + 0.1 + t_proc_s, p.mean(0), label=\"processing (shifted by 1.6 s)\")\nax.axhline(3.29, ls=\":\", c=\"k\"); ax.set_xlabel(\"s\"); ax.set_ylabel(\"Z, 2-7 Hz, anterior\"); ax.legend(fontsize=7)\nax.set_title(\"controls, pad, r hemifield, hemifields pooled\"); plt.show()\nprint(\"plotted range:\", round(float(np.nanmin([e.mean(0).min(), p.mean(0).min()])), 1), \"to\", round(float(np.nanmax([e.mean(0).max(), p.mean(0).max()])), 1))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### power-posterior-alphabeta\n# > Posterior channels show beta-gamma (12 to 35 Hz) increases and alpha desynchronization at\n# > encoding, then alpha-beta (9 to 24 Hz) decreases through maintenance (|Z| > 1.96) and active\n# > processing (Z < -3.29), in both groups.\n\n# %% tags=[\"claim:power-posterior-alphabeta\"]\nrows = []\nfor reading in (\"pad\", \"fit\"):\n    for r_mode in (\"hemifield\", \"all\"):\n        for gi, gname in ((0, \"controls\"), (1, \"patients\")):\n            ze = {h: zstack(\"enc\", h, reading, r_mode)[gi] for h in (1, 2)}\n            zp = {h: zstack(\"proc\", h, reading, r_mode)[gi] for h in (1, 2)}\n            for hf in (\"pooled\", 1, 2):\n                pick = (lambda d: (d[1] + d[2]) / 2) if hf == \"pooled\" else (lambda d, hf=hf: d[hf])\n                ab_e = np.nanmean(band_course(pick(ze), POST_S4, 9, 24), 0)\n                ab_p = np.nanmean(band_course(pick(zp), POST_S4, 9, 24), 0)\n                bg_e = np.nanmean(band_course(pick(ze), POST_S4, 12, 35), 0)\n                maint = (t_enc_s >= 0.4)\n                with warnings.catch_warnings():\n                    warnings.simplefilter(\"ignore\", RuntimeWarning)\n                    rows.append({\"window\": reading, \"r\": r_mode, \"group\": gname, \"hemifield\": hf,\n                                 \"maint frac < -1.96\": np.nanmean(ab_e[maint] < -1.96), \"maint max Z\": np.nanmax(ab_e[maint]),\n                                 \"proc frac < -3.29\": np.nanmean(ab_p < -3.29), \"proc max Z\": np.nanmax(ab_p),\n                                 \"12-35 Hz mean Z 0-0.4 s\": np.nanmean(bg_e[t_enc_s < 0.4])})\ntab2 = pd.DataFrame(rows)\nwith pd.option_context(\"display.width\", 250, \"display.max_columns\", 20, \"display.max_rows\", 60):\n    print(tab2.round(2).to_string())\nzc = zstack(\"enc\", 2)\nprint(\"\\nalpha (8-12 Hz) posterior, 0-0.4 s, lesioned hemifield, pad: controls %.2f, patients %.2f\" % (\n    np.nanmean(band_course(zc[0], POST_S4, 8, 12)[:, t_enc_s < 0.4]), np.nanmean(band_course(zc[1], POST_S4, 8, 12)[:, t_enc_s < 0.4])))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### power-lowtheta-interaction\n# > At active processing, patients have reduced low-theta (3 to 4 Hz) power in\n# > lesioned-hemisphere anterior channels relative to the intact homologs, a group by\n# > hemisphere interaction found both when stimuli went to the lesioned and to the intact visual\n# > hemifield.\n#\n# O2 readings: (a) channels by frequency (1 to 40 Hz) by time, as `tfr_stat_group_hem.m` runs\n# it; (b) channels by time on the 3-4 Hz mean. Window reading pad (fit has no value at 3-4 Hz).\n# A positive cluster is the patients' index below the controls'.\n\n# %% tags=[\"claim:power-lowtheta-interaction\"]\nANT_LES = [\"Fp1\", \"AF7\", \"AF3\", \"F1\", \"F3\", \"F5\", \"F7\", \"FT7\", \"FC5\", \"FC3\", \"FC1\"]\nlowtheta = {}\nf34 = (fp.FREQS >= 3) & (fp.FREQS <= 4)\nfor h in (2, 1):\n    z1, z2 = zstack(\"proc\", h)\n    i1, i2 = fp.hem_index(z1, labels), fp.hem_index(z2, labels)\n    ra = fp.cluster_test(i1, i2, ADJ_HEM, seed=SEED[\"pow\"])\n    rb = fp.cluster_test(i1[:, :, f34].mean(2), i2[:, :, f34].mean(2), ADJ_HEM, seed=SEED[\"pow\"])\n    TESTS[(\"pow_hem\", h, \"a\")] = ra\n    TESTS[(\"pow_hem\", h, \"b\")] = rb\n    print(f\"hemifield {h} ({'lesioned' if h == 2 else 'intact'}), (a) channel x frequency x time:\")\n    describe(ra, HEM_LABELS, [(\"frequency\", fp.FREQS, \"Hz\"), (\"time\", t_proc_s * 1000, \"ms\")], n=4)\n    for c in ra[\"clusters\"]:\n        if c[\"p\"] < 0.05:\n            m = c[\"mask\"]\n            cov34 = bool(m[:, f34].any())\n            ant = [HEM_LABELS[i] for i in np.flatnonzero(m[:, f34].any((1, 2)))] if cov34 else []\n            print(f\"     p = {c['p']:.3f}, sign {c['sign']}: covers 3-4 Hz {cov34}; anterior channels at 3-4 Hz \"\n                  f\"{[a for a in ant if a in ANT_LES]}\")\n    print(f\"hemifield {h}, (b) channel x time, 3-4 Hz:\")\n    describe(rb, HEM_LABELS, [(\"time\", t_proc_s * 1000, \"ms\")], n=3)\n    for c in rb[\"clusters\"]:\n        if c[\"p\"] < 0.05:\n            lowtheta.setdefault(h, []).append([HEM_LABELS[i] for i in np.flatnonzero(c[\"mask\"].any(1))])\n    ai = [HEM_LABELS.index(c) for c in ANT_S4]\n    print(\"   index 3-4 Hz, AF7-F5-F7-FC5-FT7, whole segment: controls %.2f, patients %.2f\" % (\n        np.nanmean(i1[:, ai][:, :, f34]), np.nanmean(i2[:, ai][:, :, f34])))\nprint(\"significant 3-4 Hz clusters (reading b), channels:\", lowtheta)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### power-no-group-main-effect\n# > Task-induced power shows no group main effect, neither for anterior theta nor for the\n# > posterior alpha-beta decreases.\n\n# %% tags=[\"claim:power-no-group-main-effect\"]\nnomain = []\nfor seg, tt_s in ((\"enc\", t_enc_s), (\"proc\", t_proc_s)):\n    for h in (2, 1):\n        for reading in (\"pad\", \"fit\"):\n            z1, z2 = zstack(seg, h, reading)\n            r_ = fp.cluster_test(z1, z2, ADJ, seed=SEED[\"pow\"])\n            TESTS[(\"pow_main\", seg, h, reading)] = r_\n            nomain.append({\"segment\": seg, \"hemifield\": h, \"reading\": f\"(a) {reading}\", \"min cluster p\": minp(r_)})\n            print(f\"{seg}, hemifield {h}, window {reading}, chan x freq x time: smallest p = {minp(r_):.3f}\")\n            describe(r_, labels, [(\"frequency\", fp.FREQS, \"Hz\"), (\"time\", tt_s * 1000, \"ms\")], n=2, pmax=0.2)\n        z1, z2 = zstack(seg, h, \"pad\")\n        for fmin, fmax in ((3, 4), (2, 7), (9, 24)):\n            fi = (fp.FREQS >= fmin) & (fp.FREQS <= fmax)\n            r_ = fp.cluster_test(z1[:, :, fi].mean(2), z2[:, :, fi].mean(2), ADJ, seed=SEED[\"pow\"])\n            nomain.append({\"segment\": seg, \"hemifield\": h, \"reading\": f\"(b) {fmin}-{fmax} Hz\", \"min cluster p\": minp(r_)})\n        g_ant = band_course(z1, ANT_S4, 3, 4).mean() - band_course(z2, ANT_S4, 3, 4).mean()\n        g_post = band_course(z1, POST_S4, 9, 24).mean() - band_course(z2, POST_S4, 9, 24).mean()\n        print(f\"   controls minus patients, anterior 3-4 Hz Z {g_ant:+.2f}, posterior 9-24 Hz Z {g_post:+.2f}\")\nprint(pd.DataFrame(nomain).round(3).to_string())\n\n# %% [markdown]\n# **Result: ...**\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/part5.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('part5.py').read()
s=s.replace('''def zstack(seg, h, reading="pad", r_mode="hemifield", coding="A"):
    return stack(f"tfr_{seg}_{{h}}", h, coding, fn=None) if False else (
        np.stack([fp.power_z(R[s], seg, hfor(s, h, coding), reading, r_mode) for s in CTRL]),
        np.stack([fp.power_z(R[s], seg, hfor(s, h, coding), reading, r_mode) for s in PFC]))''','''def zstack(seg, h, reading="pad", r_mode="hemifield", coding="A"):
    """Power Z of controls and patients, (subjects, 64, 40, time)."""
    return (np.stack([fp.power_z(R[s], seg, hfor(s, h, coding), reading, r_mode) for s in CTRL]),
            np.stack([fp.power_z(R[s], seg, hfor(s, h, coding), reading, r_mode) for s in PFC]))''')
open('part5.py','w').write(s)
EOF
. ../dev/bin/activate && time python dev.py part1.py part2.py part3.py part4.py part5.py 2>&1 | sed -n '/^ *window  *r  *hemifield/,$p' | grep -v Warning | grep -v "smf.mixedlm\|warnings.warn\|nanmean\|np.nan"
```

```
window          r hemifield  enc mean Z 0-0.4 s  enc mean Z 0.4-1.5 s  proc max group-mean Z  proc frac. time group mean > 3.29  max fraction of controls > 3.29 (proc)  group-mean max lies in proc  time of max (s, proc if in proc)
0     pad  hemifield    pooled                2.19                  1.79                   3.74                               0.50                                    0.55                         True                              0.53
1     pad  hemifield         1                1.83                  1.58                   3.81                               0.41                                    0.55                         True                              0.55
2     pad  hemifield         2                2.55                  1.99                   3.69                               0.54                                    0.55                         True                              0.51
3     pad        all    pooled                3.11                  2.53                   5.32                               0.73                                    0.65                         True                              0.53
4     pad        all         1                2.64                  2.27                   5.46                               0.73                                    0.65                         True                              0.55
5     pad        all         2                3.59                  2.80                   5.19                               0.74                                    0.65                         True                              0.51
6     fit  hemifield    pooled                0.34                  0.11                   0.81                               0.00                                    0.20                         True                              0.58
7     fit  hemifield         1                0.17                 -0.16                   0.73                               0.00 
[... 95 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/part6.py",
 "content": "# %% [markdown]\n# ## Directional connectivity (PSI)\n#\n# PSI Z per subject is computed in the helper under three readings (see its docstring):\n# **trialwise** (adopted: the structure of `psianalysis.m`, per-trial phase slopes averaged\n# over trials and Z scored on the frequency-shuffled trial-mean coherency, with the complex\n# conjugate the Methods' \"cross-spectral density\" implies), **nolte** (PSI of the trial-averaged\n# coherency, Nolte et al. 2008, null from one shuffle of the bins) and **literal** (`psianalysis.m`\n# exactly as written, without the conjugate). The window reading is pad: under fit no\n# delta-theta value exists at all (data check), and alpha-beta exists only at the points listed\n# there. Z is baseline corrected by the temporal mean of the pretrial Z (`psi_compute.m`).\n# Positive Z(A, B): A leads B.\n#\n# The literal code's normalised cross-spectrum does not depend on channel A's phase except for\n# its sign; on random coefficients:\n\n# %%\nrng_lit = np.random.default_rng(7)\nxa = rng_lit.standard_normal(6) + 1j * rng_lit.standard_normal(6)\nxb = rng_lit.standard_normal(6) + 1j * rng_lit.standard_normal(6)\npp1 = fp.psianalysis_literal_pp(xa, xb)\npp2 = fp.psianalysis_literal_pp(xa * np.exp(1j * rng_lit.uniform(0, 2 * np.pi, 6)), xb)\nprint(\"literal pp, |pp| =\", np.round(np.abs(pp1), 3))\nprint(\"pp divided by exp(2i phase(B)):\", np.round(pp1 / np.exp(2j * np.angle(xb)), 3))\nprint(\"after changing A's phases at random:\", np.round(pp2 / np.exp(2j * np.angle(xb)), 3))\nt_psi_enc = R[CTRL[0]][\"psi_dt_enc_time\"]\nt_psi_proc = R[CTRL[0]][\"psi_dt_proc_time\"]\nprint(\"PSI times (s): encoding-maintenance\", np.round(t_psi_enc, 2), \"processing\", np.round(t_psi_proc, 2))\n\n# %%\nPFC_ROI = {\"(b) Figure S4 ANTERIOR\": ANT_S4}\nif lowtheta.get(2):\n    PFC_ROI[\"(a) power-lowtheta cluster\"] = [c for c in lowtheta[2][0] if c in ANT_LES]\nprint(\"PFC regions of interest:\", PFC_ROI)\nPO_ROI = POST_S4\ndef roi_course(band, h, reading, roi, window=\"pad\"):\n    \"\"\"Baseline-corrected PSI Z from the PFC region to the parieto-occipital region, mean over\n    pairs: (controls, time), (patients, time) for encoding-maintenance then processing.\"\"\"\n    a = [L[c] for c in roi]\n    b = [L[c] for c in PO_ROI]\n    def one(s):\n        e = fp.psi_bc(R[s], band, \"enc\", h, reading, window)[np.ix_(a, b)].mean((0, 1))\n        p = fp.psi_bc(R[s], band, \"proc\", h, reading, window)[np.ix_(a, b)].mean((0, 1))\n        return e, p\n    ce = [one(s) for s in CTRL]\n    pe = [one(s) for s in PFC]\n    return (np.stack([x[0] for x in ce]), np.stack([x[1] for x in ce])), (np.stack([x[0] for x in pe]), np.stack([x[1] for x in pe]))\nCOURSES = {}\nfor band in (\"dt\", \"ab\"):\n    for reading in (\"trialwise\", \"nolte\", \"literal\"):\n        for rn, roi in PFC_ROI.items():\n            for h in (2, 1):\n                COURSES[(band, reading, rn, h)] = roi_course(band, h, reading, roi)\ndef show_course(band, reading, rn, h):\n    (ce, cp), (pe, pp_) = COURSES[(band, reading, rn, h)]\n    print(f\"  {band} {reading:9s} {rn} h{h}: controls enc {np.round(ce.mean(0), 1)} proc {np.round(cp.mean(0), 1)}\")\n    print(f\"  {'':2s} {'':9s} {'':{len(rn)}s}    patients enc {np.round(pe.mean(0), 1)} proc {np.round(pp_.mean(0), 1)}\")\n\n# %% [markdown]\n# ### psi-deltatheta-bottomup-encoding\n# > In both groups, delta-theta PSI shows parieto-occipital regions leading PFC at the offset of\n# > the second stimulus at encoding, at baseline-corrected Z of -10 or below.\n\n# %% tags=[\"claim:psi-deltatheta-bottomup-encoding\"]\nnear400 = (t_psi_enc >= 0.3 - 1e-6) & (t_psi_enc <= 0.5 + 1e-6)\nrows = []\nfor reading in (\"trialwise\", \"nolte\", \"literal\"):\n    for rn in PFC_ROI:\n        for h in (2, 1):\n            (ce, _), (pe, _) = COURSES[(\"dt\", reading, rn, h)]\n            for gname, x in ((\"controls\", ce), (\"patients\", pe)):\n                rows.append({\"reading\": reading, \"ROI\": rn, \"hemifield\": h, \"group\": gname,\n                             \"min group-mean Z 300-500 ms\": x.mean(0)[near400].min(),\n                             \"fraction of subjects <= -9 at some point there\": np.mean((x[:, near400] <= -9).any(1)),\n                             \"fraction <= -1.96\": np.mean((x[:, near400] <= -1.96).any(1))})\n        show_course(\"dt\", reading, list(PFC_ROI)[0], 2)\nprint(pd.DataFrame(rows).round(2).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### psi-deltatheta-pfc-lead-controls\n# > In delta-theta PSI, controls shift to PFC leading parieto-occipital regions in\n# > mid-maintenance (Z > 1.96), and the PFC lead peaks early in active processing (Z of 10 or\n# > more), whereas patients show zero directionality (Z < 1.96).\n\n# %% tags=[\"claim:psi-deltatheta-pfc-lead-controls\"]\nmaint = t_psi_enc >= 0.4 - 1e-6\nearly = t_psi_proc <= 0.45\nrows = []\nfor reading in (\"trialwise\", \"nolte\", \"literal\"):\n    for rn in PFC_ROI:\n        for h in (2, 1):\n            (ce, cp), (pe, pp_) = COURSES[(\"dt\", reading, rn, h)]\n            gc = np.concatenate([ce.mean(0), cp.mean(0)])\n            gpat = np.concatenate([pe.mean(0)[maint], pp_.mean(0)])\n            rows.append({\"reading\": reading, \"ROI\": rn, \"hemifield\": h,\n                         \"ctrl max Z maintenance\": ce.mean(0)[maint].max(),\n                         \"ctrl max Z early proc\": cp.mean(0)[early].max(),\n                         \"ctrl max lies in early proc\": bool(np.argmax(gc) >= len(ce.mean(0)) and np.argmax(gc) - len(ce.mean(0)) < early.sum()),\n                         \"patients max Z (maint+proc)\": gpat.max(),\n                         \"ctrl majority > 9 early proc\": bool((np.mean(cp[:, early] >= 9, 0) > 0.5).any()),\n                         \"patients majority < 1.96 throughout\": bool((np.mean(np.concatenate([pe[:, maint], pp_], 1) < 1.96, 0) > 0.5).all())})\nprint(pd.DataFrame(rows).round(2).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### psi-alphabeta-bottomup\n# > In alpha-beta (9 to 24 Hz) PSI, parieto-occipital regions lead PFC throughout encoding,\n# > maintenance and active processing, for both visual hemifields.\n\n# %% tags=[\"claim:psi-alphabeta-bottomup\"]\nrows = []\nfor reading in (\"trialwise\", \"nolte\", \"literal\"):\n    for rn in PFC_ROI:\n        for h in (2, 1):\n            (ce, cp), (pe, pp_) = COURSES[(\"ab\", reading, rn, h)]\n            for gname, e, p in ((\"controls\", ce, cp), (\"patients\", pe, pp_)):\n                rows.append({\"reading\": reading, \"ROI\": rn, \"hemifield\": h, \"group\": gname,\n                             \"enc frac < -1.96\": np.mean(e.mean(0) < -1.96), \"proc frac < -1.96\": np.mean(p.mean(0) < -1.96),\n                             \"enc frac < 0\": np.mean(e.mean(0) < 0), \"proc frac < 0\": np.mean(p.mean(0) < 0),\n                             \"median Z\": np.median(np.concatenate([e.mean(0), p.mean(0)]))})\n        show_course(\"ab\", reading, list(PFC_ROI)[0], 2)\nprint(pd.DataFrame(rows).round(2).to_string())\n# window reading fit, alpha-beta, where values exist\nfor reading in (\"trialwise\", \"literal\"):\n    a = [L[c] for c in ANT_S4]; b_ = [L[c] for c in PO_ROI]\n    for h in (2, 1):\n        v = np.stack([np.concatenate([fp.psi_bc(R[s], \"ab\", \"enc\", h, reading, \"fit\")[np.ix_(a, b_)].mean((0, 1)),\n                                      fp.psi_bc(R[s], \"ab\", \"proc\", h, reading, \"fit\")[np.ix_(a, b_)].mean((0, 1))]) for s in CTRL + PFC])\n        g = np.nanmean(v[:len(CTRL)], 0)\n        print(f\"fit window, {reading}, h{h}: controls' group-mean Z where defined {np.round(g[np.isfinite(g)], 1)}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### psi-deltatheta-group-clusters\n# > Across all 64 by 64 channel pairs, delta-theta PSI differs between groups intermittently\n# > during encoding and maintenance and in a sustained way during active processing.\n#\n# Clustering readings: **(c)** per seed channel A, over neighbours of B and time, each seed its\n# own test (`psi_stat_group.m`; adopted, as the paper's code settles it); (a) per pair over\n# time; (b) over time and pairs whose both channels are equal or neighbours.\n\n# %%\nPAIRS, PADJ = fp.pair_adjacency(ADJ, \"pairs\")\n_, SADJ = fp.pair_adjacency(ADJ, \"seed\")\nCLUST = {\"(c) per seed\": (SADJ, PAIRS[:, 0], 2), \"(a) per pair\": (None, None, 0), \"(b) pairs\": (PADJ, None, 2)}\ndef psi_pairs(band, seg, h, reading):\n    def one(s):\n        v = fp.psi_bc(R[s], band, seg, h, reading)\n        return v[PAIRS[:, 0], PAIRS[:, 1]]\n    return np.stack([one(s) for s in CTRL]), np.stack([one(s) for s in PFC])\ndef coverage(res, times, pthr=0.05):\n    \"\"\"Times (ms) covered by any cluster with p < pthr, by sign.\"\"\"\n    out = {}\n    for c in res[\"clusters\"]:\n        if c[\"p\"] < pthr:\n            ti = np.flatnonzero(c[\"mask\"].any(0))\n            out.setdefault(c[\"sign\"], set()).update(np.round(times[ti] * 1000).astype(int).tolist())\n    return {k: sorted(v) for k, v in out.items()}\nPSI_TESTS = {}\ndef run_psi(band, readings_clust, psi_readings):\n    rows = []\n    for reading in psi_readings:\n        for seg, tms in ((\"enc\", t_psi_enc), (\"proc\", t_psi_proc)):\n            for h in (2, 1):\n                x1, x2 = psi_pairs(band, seg, h, reading)\n                for cn in readings_clust:\n                    adj, grp, mn = CLUST[cn]\n                    r_ = fp.cluster_test(x1, x2, adj, seed=SEED[\"psi\"], minnbchan=mn, node_groups=grp)\n                    PSI_TESTS[(band, reading, seg, h, cn)] = r_\n                    cov = coverage(r_, tms)\n                    nsig = sum(c[\"p\"] < 0.05 for c in r_[\"clusters\"])\n                    rows.append({\"PSI\": reading, \"segment\": seg, \"hemifield\": h, \"clustering\": cn,\n                                 \"min p\": round(minp(r_), 3), \"significant clusters\": nsig,\n                                 \"ms covered, controls > patients\": cov.get(1, []),\n                                 \"ms covered, patients > controls\": cov.get(-1, [])})\n    return pd.DataFrame(rows)\n\n# %% tags=[\"claim:psi-deltatheta-group-clusters\"]\nt_psi_tests = time.time()\ndt_tab = pd.concat([run_psi(\"dt\", list(CLUST), [\"trialwise\"]), run_psi(\"dt\", [\"(c) per seed\"], [\"nolte\", \"literal\"])])\nwith pd.option_context(\"display.width\", 300, \"display.max_colwidth\", 80, \"display.max_rows\", 60):\n    print(dt_tab.to_string())\nprint(\"windows of the paper: lesioned (h2) enc 100-200 and 700-800 ms, proc 100-700 ms; intact (h1) enc 200-300 and 1000-1200 ms, proc 0-500 ms\")\nprint(f\"PSI tests took {(time.time() - t_psi_tests) / 60:.1f} min\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### psi-network-degree\n# > A post hoc network analysis of delta-theta PSI shows group differences from lesioned PFC to\n# > bilateral central-posterior regions, sustained for 200 ms early in active processing, for\n# > both visual hemifields.\n#\n# Degree on the Z scored PSI before baseline correction, then minus the temporal mean of the\n# baseline degree (`psi_compute.m`). Readings: **ft_count** (`ft_networkanalysis` 'degrees' on\n# Z > 1.96: in- plus out-degree; the code's), (a) out_signed, (b) out_count, (c) abs_both.\n# Group test over channels by time (`psi_degree_stat_group.m`).\n\n# %% tags=[\"claim:psi-network-degree\"]\nrows = []\nfor reading in (\"trialwise\", \"literal\"):\n    for mode in (\"ft_count\", \"out_signed\", \"out_count\", \"abs_both\"):\n        for h in (2, 1):\n            def deg(s):\n                base = fp.degree(fp.psi_raw(R[s], \"dt\", \"pre\", None, reading), mode).mean(-1)\n                return fp.degree(fp.psi_raw(R[s], \"dt\", \"proc\", h, reading), mode) - base[:, None]\n            d1 = np.stack([deg(s) for s in CTRL]); d2 = np.stack([deg(s) for s in PFC])\n            r_ = fp.cluster_test(d1, d2, ADJ, seed=SEED[\"deg\"])\n            TESTS[(\"deg\", reading, mode, h)] = r_\n            for c in r_[\"clusters\"][:3]:\n                if c[\"p\"] >= 0.1:\n                    continue\n                ti = np.flatnonzero(c[\"mask\"].any(0))\n                ch = [labels[i] for i in np.flatnonzero(c[\"mask\"].any(1))]\n                rows.append({\"PSI\": reading, \"degree\": mode, \"hemifield\": h, \"p\": round(c[\"p\"], 3),\n                             \"sign (+ controls > patients)\": c[\"sign\"], \"ms\": (t_psi_proc[ti] * 1000).round().astype(int).tolist(),\n                             \"channels\": \" \".join(ch)})\n            if not any(c[\"p\"] < 0.1 for c in r_[\"clusters\"]):\n                rows.append({\"PSI\": reading, \"degree\": mode, \"hemifield\": h, \"p\": round(minp(r_), 3),\n                             \"sign (+ controls > patients)\": None, \"ms\": [], \"channels\": \"\"})\nwith pd.option_context(\"display.width\", 300, \"display.max_colwidth\", 120, \"display.max_rows\", 60):\n    print(pd.DataFrame(rows).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### psi-alphabeta-no-group-effect\n# > PFC lesions do not affect alpha-beta PSI at any point of encoding, maintenance or active\n# > processing.\n\n# %% tags=[\"claim:psi-alphabeta-no-group-effect\"]\nab_tab = pd.concat([run_psi(\"ab\", list(CLUST), [\"trialwise\"]), run_psi(\"ab\", [\"(c) per seed\"], [\"nolte\", \"literal\"])])\nwith pd.option_context(\"display.width\", 300, \"display.max_colwidth\", 80, \"display.max_rows\", 60):\n    print(ab_tab.to_string())\nfor reading in (\"trialwise\", \"literal\"):\n    for h in (2, 1):\n        (ce, cp), (pe, pp_) = COURSES[(\"ab\", reading, list(PFC_ROI)[0], h)]\n        print(f\"{reading}, h{h}: controls minus patients, PFC to parieto-occipital Z, enc {np.mean(ce) - np.mean(pe):+.2f}, proc {np.mean(cp) - np.mean(pp_):+.2f}\")\nprint(f\"all group tests took {(time.time() - t_tests) / 60:.1f} min; whole notebook so far {(time.time() - T0) / 60:.1f} min; \"\n      f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% [markdown]\n# **Result: ...**\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/part6.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && . ../dev/bin/activate && time python dev.py part1.py part2.py part3.py part4.py part5.py part6.py 2>&1 | sed -n '/^literal pp/,$p' | grep -v Warning | grep -v "smf.mixedlm\|warnings.warn\|nanmean\|np.nan"; date -u
```

```
literal pp, |pp| = [1. 1. 1. 1. 1. 1.]
pp divided by exp(2i phase(B)): [-1.-0.j -1.-0.j  1.+0.j -1.-0.j -1.-0.j  1.-0.j]
after changing A's phases at random: [-1.-0.j  1.+0.j -1.-0.j -1.+0.j -1.-0.j -1.+0.j]
PSI times (s): encoding-maintenance [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2 1.3 1.4 1.5] processing [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8]
PFC regions of interest: {'(b) Figure S4 ANTERIOR': ['AF7', 'F5', 'F7', 'FC5', 'FT7'], '(a) power-lowtheta cluster': ['AF7', 'F5', 'F7', 'FT7', 'FC5']}
  dt trialwise (b) Figure S4 ANTERIOR h2: controls enc [ 10.6   8.1  12.5   6.4   6.1  19.1  18.8  -0.5   5.7   2.8 -14.2  -4.6
   9.6   8.9   9.9  15.8] proc [-20.6 -23.   -9.7   4.3   1.4   1.6   7.9   9.1   8.4]
                                         patients enc [-7.4  5.7  4.9  6.2  4.7  7.2  8.7  1.9  2.8  6.5  4.4  1.3 -0.2  5.4
 14.4  9.8] proc [-11.  -13.4 -10.6  -5.    0.4   9.5  11.4   7.4   8.5]
  dt trialwise (b) Figure S4 ANTERIOR h2: controls enc [ 10.6   8.1  12.5   6.4   6.1  19.1  18.8  -0.5   5.7   2.8 -14.2  -4.6
   9.6   8.9   9.9  15.8] proc [-20.6 -23.   -9.7   4.3   1.4   1.6   7.9   9.1   8.4]
                                         patients enc [-7.4  5.7  4.9  6.2  4.7  7.2  8.7  1.9  2.8  6.5  4.4  1.3 -0.2  5.4
 14.4  9.8] proc [-11.  -13.4 -10.6  -5.    0.4   9.5  11.4   7.4   8.5]
  dt nolte     (b) Figure S4 ANTERIOR h2: controls enc [-0.   0.1  0.1  0.  -0.2 -0.2 -0.1 -0.2 -0.2 -0.1 -0.2 -0.1 -0.1 -0.1
 -0.1 -0.1] proc [-0.2 -0.1 -0.1 -0.1  0.  -0.  -0.1  0.   0.1]
                                         patients enc [ 0.2  0.1  0.2  0.2  0.1  0.  -0.1 -0.   0.1  0.   0.1  0.1 -0.1 -0.1
 -0.   0. ] proc [ 0.  -0.  -0.1  0.   0.2  0.4  0.4  0.2  0.3]
  dt nolte     (b) Figure S4 ANTERIOR h2: controls enc [-0.   0.1  0.1  0.  -0.2 -0.2 -0.1 -0.2 -0.2 -0.1 -0.2 -0.1 -0.1 -0.1
 -0.1 -0.1] proc [-0.2 -0.1 -0.1 -0.1  0.  -0.  -0.1  0.   0.1]
                                         patients enc [ 0.2  0.1  0.2  0.2  0.1  0.  -0.1 -0. 
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/nb && python3 - <<'EOF'
s=open('part6.py').read()
old='''        for rn, roi in PFC_ROI.items():
            for h in (2, 1):
                COURSES[(band, reading, rn, h)] = roi_course(band, h, reading, roi)'''
assert old in s
s=s.replace('''        show_course("dt", reading, list(PFC_ROI)[0], 2)
print(pd.DataFrame(rows).round(2).to_string())''','''print(pd.DataFrame(rows).round(2).to_string())
for reading in ("trialwise", "nolte", "literal"):
    show_course("dt", reading, list(PFC_ROI)[0], 2)''')
s=s.replace('''        show_course("ab", reading, list(PFC_ROI)[0], 2)
print(pd.DataFrame(rows).round(2).to_string())''','''print(pd.DataFrame(rows).round(2).to_string())
for reading in ("trialwise", "nolte", "literal"):
    show_course("ab", reading, list(PFC_ROI)[0], 2)''')
open('part6.py','w').write(s)
EOF
grep -c "Result: \.\.\." $TMPDIR/nb/part*.py
```

```
Mon Nov  9 21:01:16 UTC 2026
/tmp/claude-1001/nb/part1.py:0
/tmp/claude-1001/nb/part2.py:0
/tmp/claude-1001/nb/part3.py:7
/tmp/claude-1001/nb/part4.py:5
/tmp/claude-1001/nb/part5.py:4
/tmp/claude-1001/nb/part6.py:6
Shell cwd was reset to
```

**Agent**

All 22 claims now run end to end on cached data in about 8 minutes of analysis. Writing the conclusions, header and summary, then I'll launch the clean full run.

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/results.py <<'PYEOF'
RESULTS = [
# cohort
"""**Result: reproduced.** 14 patients and 20 controls. Over all trials kept in `data_derived.mat` (reading a) subjects average 187.3 trials, 94.4 +- 21.1 (55 to 119) in the lesioned and 93.0 +- 22.1 (51 to 120) in the intact hemifield under coding A, the paper's numbers to the trial; coding B gives 93.7 +- 21.5 and 93.6 +- 21.8 with the same ranges. Correct trials only (reading b) give 172.4 per subject, outside 187 +- 18.7.""",
# demographics
"""**Result: reproduced.** No test gives p < 0.05: age t(32) = 0.35, p = 0.725 (paper t < 0.36, p > 0.72); education t(32) = -1.38, p = 0.178; variance F(13,19) = 0.76 (age, p = 0.685) and 1.42 (education, p = 0.237). The education test differs from the paper's bound (t < 1.22, p > 0.23), and the education variance test from F < 1.31, p > 0.31; the ages (patients 46.4 +- 16.4, controls 44.1 +- 18.8) match. The demographics come from the docs summary files.""",
# patient factors
"""**Result: reproduced.** No term of the repeated-measures ANCOVA reaches p < 0.05 (smallest p = 0.106, gender, F(1,2) = 7.96), under the Table S1 coding and under coding B; the paper's bound is p > 0.14. The F values do not match Table S2 term by term (for example age F = 7.27 against 4.38, gender 7.96 against 5.33).""",
# table s1
"""**Result: partially reproduced.** 20 of the 28 values are within 0.02 of Table S1 when trial-table hemifield 1 is taken as the lesioned one in every patient (coding S1), with every trial of the trial tables or with the trials kept after cleaning; the 8 misses are the 4 patients recorded in two blocks (pfc10 to pfc13, differences 0.028 to 0.098). The paper's own coding note (the lesioned hemifield is the right one for left-lesioned patients) together with the descriptor's coding of the trial tables (1 left, 2 right) gives 6 to 12 of 28 (codings A and B). Measured values range from 0.65 to 0.98, as in the table.""",
# impaired
"""**Result: partially reproduced (assumption: the linear model of the Methods).** Mean accuracy is 0.952 +- 0.031 in controls and 0.872 +- 0.099 in patients, within tolerance of 0.95 and 0.87. In the group-only linear mixed model, group F(1,202) = 11.68, p = 7.6e-4, below the Bonferroni level 0.0071 but not below 7e-5; the binomial logit reading gives F = 25.83, p = 8.5e-7. Neither F is within 16.77 +- 1.68. The full model's group effect is F(1,196) = 0.22 (p = 0.64) with condition as a number, against the paper's 4.70 (p = 0.03).""",
# chance
"""**Result: reproduced.** On each patient's overall accuracy (reading a), t(13) = 14.13, one-tailed p = 1.4e-9, above 13.89 (15.43 less 10%). Per hemifield (reading b) t = 13.63 and 13.76, and per hemifield and condition (reading c) t = 6.28 to 29.63, so the paper's "t > 15.43" for every test is not met under readings b and c. Every test is far above chance.""",
# no hemifield
"""**Result: reproduced (assumption: the linear model of the Methods).** In the linear mixed model with hemifield and condition only, hemifield p = 0.915, condition p = 0.094 and their interaction p = 0.715. The binomial logit reading finds a condition effect (F(1,200) = 20.71, p < 0.001), and with condition as a factor the spatial condition differs from identity (p < 0.001); mean accuracy is 0.879, 0.956 and 0.922 in the identity, spatial and temporal conditions. In the full model condition has p = 0.038 (linear).""",
# erp lesioned
"""**Result: reproduced under coding A (assumption: the descriptor's hemifield coding).** Two clusters pass p < 0.05 after 400 ms: one in F5, F7, FT7, FC5, C3, C5, T7 (with FC3, C1 and others) at 820 to 887 ms, p = 0.006, where the patients' mean ERP is +0.52 and the controls' -0.33 (opposite signs), and one in TP8, P4, P6, P8, P10, PO8 at 754 to 863 ms, p = 0.014, controls above patients (1.23 against -0.09). Both lie in maintenance, about 400 ms after its start; the paper says "early during the maintenance". Under coding B neither cluster survives (smallest p = 0.070).""",
# erp proc
"""**Result: not reproduced.** No group by hemisphere cluster passes p < 0.05 at active processing (smallest p = 0.294, coding A; 0.500, coding B; 0.272 with the trial selection of `erp_compute.m`), though the patients' index over FP1-AF3-AF7-F5-F7-FC5-FT7 at 50 to 150 ms is higher than the controls' (0.38 against 0.05). There is no group main effect under coding A (smallest p = 0.636); the code's trial selection gives one (p = 0.036, right posterior channels, 55 to 141 ms).""",
# erp intact
"""**Result: reproduced.** For the intact hemifield no test finds a cluster with p < 0.05: encoding-maintenance main effect p = 0.554, processing main effect p = 0.126, processing group by hemisphere p = 0.188 (coding A); 0.518, 0.180 and 0.706 under coding B.""",
# baseline interaction
"""**Result: reproduced.** One group by hemisphere cluster passes, p = 0.004, over AF3, F3, F5 and FC3 from 3 to 19 Hz, with the patients' lesioned-minus-intact power above the controls' (6 to 18 Hz index at AF3-F3-F5: 2.48 against -0.30). The paper reports p = 0.004 over AF3-F3-F5 at 6 to 18 Hz; the cluster here extends down to 3 Hz.""",
# baseline no group
"""**Result: partially reproduced.** No cluster of the group main effect passes (smallest p = 0.066, controls above patients at 13 to 40 Hz over 23 anterior channels), but 476 of 2560 channel-frequency points have uncorrected p < 0.05, where the paper states uncorrected p > 0.05; the criterion marks the claim as only partly holding when any point passes.""",
# anterior theta
"""**Result: reproduced (assumption: windows may run into the zero padding).** With the padded windows, the controls' 2 to 7 Hz Z over AF7-F5-F7-FC5-FT7 rises during encoding-maintenance (group mean 2.2 over 0 to 0.4 s, 1.8 later), exceeds 3.29 during active processing (maximum 3.74 at 0.53 s, hemifields pooled; 3.81 and 3.69 per hemifield) and peaks there; with r = all correct trials the maximum is 5.32. The proportion of controls above 3.29 at any processing time is at most 0.55. Under FieldTrip's window rule only 6 to 7 Hz has values and the maximum is 0.81 to 1.36, so the claim does not hold under that reading.""",
# posterior ab
"""**Result: not reproduced.** The posterior 9 to 24 Hz Z is not below -1.96 through maintenance in any reading (at most 4% of maintenance time points with the padded windows, 20% under FieldTrip's rule with r = all trials), and its group mean stays above -1 in processing (maximum 0.07 to 0.89). The 12 to 35 Hz Z is above zero at encoding in both groups (0.38 to 1.10), and 8 to 12 Hz is slightly negative at 0 to 0.4 s (-0.42 controls, -0.51 patients).""",
# lowtheta
"""**Result: partially reproduced (assumptions: padded windows, and the test on the 3-4 Hz mean).** On the 3 to 4 Hz mean (reading b) the lesioned hemifield gives a group by hemisphere cluster over AF7, F5, F7, FT7 and FC5 at 12 to 352 ms, p = 0.040, with the patients' index below the controls' (-1.79 against 0.27 over the segment); the intact hemifield's cluster in F5-F7-FT7-FC5 has p = 0.134. On channels by frequency by time (reading a, as `tfr_stat_group_hem.m` runs it) neither hemifield has a significant cluster (p = 0.508 and 0.834), though the leading cluster lies at 3 to 5 Hz in the same five channels.""",
# no main
"""**Result: reproduced.** No group main effect cluster passes on channels by frequency by time, in either segment, hemifield or window reading (smallest p = 0.388). On band means (reading b) the smallest p is 0.062 (3 to 4 Hz, encoding-maintenance). Controls minus patients is +1.2 to +1.3 Z in anterior 3 to 4 Hz during encoding-maintenance and about 0 in processing; posterior 9 to 24 Hz differs by -0.43 to +0.14.""",
# bottomup enc
"""**Result: not reproduced.** No reading gives the PFC to parieto-occipital delta-theta Z at -9 or below near 400 ms in both groups. With the adopted trialwise PSI the group means at 300 to 500 ms stay positive (minima 4.4 to 8.6); with Nolte's PSI they lie between -0.21 and 0.06; with the literal code the controls' are positive (7.6 to 12.3) and the patients' -6.2 to -6.6.""",
# pfc lead
"""**Result: not reproduced.** In no reading does the controls' PFC lead peak early in processing: with the trialwise PSI their maximum in early processing is 4.3 and 0.2 against 19.2 and 15.0 in maintenance, and the patients reach 14.4; Nolte's PSI stays within +-0.4; the literal code gives controls 21 to 22 in early processing but larger values at the segment edges (up to 227), and patients above 1.96.""",
# ab bottomup
"""**Result: not reproduced (assumption: PSI with the conjugate, as the Methods' cross-spectral density implies).** With the trialwise PSI the controls' alpha-beta Z from PFC to parieto-occipital channels is mostly positive (median 3.7 and 3.8; below -1.96 at 11 to 25% of time points). Nolte's PSI never passes -1.96. The literal code of `psianalysis.m` reproduces the claim: Z below -1.96 at 94% of encoding-maintenance and 100% of processing time points in both groups and hemifields (median about -23).""",
# group clusters
"""**Result: not reproduced.** With the adopted readings (trialwise PSI, per-seed clustering of `psi_stat_group.m`) significant clusters cover 2 of the 7 processing time points of the lesioned window (100 and 400 ms of 100 to 700 ms) and 2 of 6 of the intact window (0 and 100 ms), not most of either; the encoding-maintenance windows are touched in the lesioned hemifield (200 ms, and 700 to 800 ms) and in the intact one only at 700 to 800 ms. Clustering per pair or over neighbouring pairs finds no cluster (smallest p = 0.56). The literal code covers 4 of 7 lesioned processing points (100 to 500 ms) but 2 of 6 intact ones.""",
# degree
"""**Result: not reproduced.** No reading gives a cluster with p <= 0.01 of patients below controls early in processing in both hemifields. The closest are, with the trialwise PSI, a cluster of the sum of |Z| at 0 to 100 ms in right central-posterior channels (FC6 to PO8), p = 0.046, lesioned hemifield only, and the code's degree count at 800 ms (p = 0.022); with the literal code the out-degree count gives p = 0.006 at 0 to 100 ms but with patients above controls.""",
# ab no group
"""**Result: not reproduced (assumptions: trialwise PSI, per-seed clustering).** The per-seed test of `psi_stat_group.m` finds alpha-beta clusters with p < 0.05 in three of four segment and hemifield combinations (smallest p = 0.010); it tests each of the 64 seed channels at 0.05 with no correction across seeds, and Nolte's PSI and the literal code also give clusters (smallest p 0.002 and 0.020). Clustering per pair or over neighbouring pairs finds none (p = 1.0). Controls minus patients in the PFC to parieto-occipital Z is +3.3 to +6.9 with the trialwise PSI.""",
]
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
exec(open('results.py').read())
RESULTS[13] = """**Result: not reproduced.** The posterior 9 to 24 Hz Z is below -1.96 at no more than 4% of maintenance time points with the padded windows, and at most 20% under FieldTrip's rule (r = all trials), in either group. In processing it is below -3.29 at 1% (r = trials of the hemifield) to 54% (r = all trials) of time points. The 12 to 35 Hz Z is above zero at encoding in both groups (0.38 to 1.10), and 8 to 12 Hz is slightly negative at 0 to 0.4 s (-0.42 controls, -0.51 patients)."""
RESULTS[12] = RESULTS[12].replace("Under FieldTrip's window rule only 6 to 7 Hz has values", "Under FieldTrip's window rule only 7 Hz of the band has a baseline")
RESULTS[19] = RESULTS[19].replace("and in the intact one only at 700 to 800 ms.", "and in the intact one only at 700 and 800 ms, outside its windows (200 to 300 and 1000 to 1200 ms).")
open('results.py','w').write("RESULTS = " + repr(RESULTS) + "\n")
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/header.md",
 "content": "# Reproducing Johnson et al. (2017) on CRCNS pfc-5\n\n**Paper.** Johnson, Dewar, Solbakk, Endestad, Meling & Knight (2017), \"Bidirectional\nFrontoparietal Oscillatory Systems Support Working Memory\", Current Biology 27, 1829-1835,\ndoi:10.1016/j.cub.2017.05.046. The claims file (`claims/johnson-2017.yaml`) was written from the\nversion of record with its supplemental information; it decides what is tested.\n\n**Dataset.** CRCNS pfc-5 (doi:10.6080/K0ZC811B), read anonymously from the public bucket\n`crcnsarchive` under `pfc-5/live/` (`crcns:pfc-5/unversioned`). CRCNS data sets have no versions;\nthe files under `live/` are the only published state of the data (the descriptor is at its\nversion 0.8, April 2021, and `analysis_scripts.tar.gz` holds the 0.61 update of the PSI scripts),\nso they are what is pinned. The first code cell prints the MD5 sums from the data set's\n`checksums.md5` for every file read, so that a later change is detectable. Each subject's\n`.tar.gz` is streamed once; `data_derived.mat` (preprocessed, surface Laplacian, lesions swapped\nto the left) and the trial tables are read from it in memory, and the raw `.bdf` is skipped.\n\n**Method.** Measures follow the claims file; where it leaves a detail open, the paper's code\ndeposited in the data set settles it (the claims file allows this), and where neither does the\nreadings are all run and the choice adopted is stated (helper docstring, `frontoparietal.py`).\n\n| claim | tested |\n|---|---|\n| cohort-and-trials | tested |\n| demographics-matched | tested |\n| patient-factors-no-effect | tested |\n| table-s1-patient-accuracy | tested |\n| accuracy-patients-impaired | tested |\n| patients-above-chance | tested |\n| accuracy-no-hemifield-condition-effect | tested |\n| erp-lesioned-maintenance | tested |\n| erp-processing-interaction | tested |\n| erp-intact-none | tested |\n| baseline-spectral-interaction | tested |\n| baseline-no-group-effect | tested |\n| power-anterior-theta-controls | tested |\n| power-posterior-alphabeta | tested |\n| power-lowtheta-interaction | tested |\n| power-no-group-main-effect | tested |\n| psi-deltatheta-bottomup-encoding | tested |\n| psi-deltatheta-pfc-lead-controls | tested |\n| psi-deltatheta-group-clusters | tested |\n| psi-network-degree | tested |\n| psi-alphabeta-bottomup | tested |\n| psi-alphabeta-no-group-effect | tested |\n\nNo claim is blocked.\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/header.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb/summary.md",
 "content": "## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n| claim | outcome | rests on an assumption |\n|---|---|---|\n| cohort-and-trials | reproduced | no |\n| demographics-matched | reproduced | no |\n| patient-factors-no-effect | reproduced | no |\n| table-s1-patient-accuracy | partially reproduced | no |\n| accuracy-patients-impaired | partially reproduced | yes (linear model) |\n| patients-above-chance | reproduced | no |\n| accuracy-no-hemifield-condition-effect | reproduced | yes (linear model) |\n| erp-lesioned-maintenance | reproduced | yes (hemifield coding A) |\n| erp-processing-interaction | not reproduced | no |\n| erp-intact-none | reproduced | no |\n| baseline-spectral-interaction | reproduced | no |\n| baseline-no-group-effect | partially reproduced | no |\n| power-anterior-theta-controls | reproduced | yes (padded windows) |\n| power-posterior-alphabeta | not reproduced | no |\n| power-lowtheta-interaction | partially reproduced | yes (padded windows, 3-4 Hz mean) |\n| power-no-group-main-effect | reproduced | no |\n| psi-deltatheta-bottomup-encoding | not reproduced | no |\n| psi-deltatheta-pfc-lead-controls | not reproduced | no |\n| psi-deltatheta-group-clusters | not reproduced | no |\n| psi-network-degree | not reproduced | no |\n| psi-alphabeta-bottomup | not reproduced | yes (PSI with the conjugate) |\n| psi-alphabeta-no-group-effect | not reproduced | yes (PSI reading, per-seed test) |\n\n**How the analysis differs from the paper's.** It runs in Python, not MATLAB and FieldTrip: the\nspectral estimates, the cluster test (with minnbchan and FieldTrip's neighbour template) and the\nmodels are reimplemented. The bootstrap of the power Z is replaced by its exact expectation.\nThree choices the paper does not settle change outcomes and are stated as assumptions: the\nhemifield coding of `data_derived.mat` (the descriptor's, A), letting the 3/f windows run into\nthe zero padding (the segments have no buffers, so FieldTrip's rule leaves no value below 7 Hz in\nthe baseline), and the PSI (per-trial phase slopes as `psianalysis.m` computes them, but with the\ncomplex conjugate of a cross-spectral density). The processing segment is matched to the trials by\ntrial number.\n\n**What was found about the dataset.**\n- The processing segments of `data_derived.mat` are stored in another trial order than the\n  pretrial and encoding-maintenance segments in all 34 subjects; `erp_compute.m` and\n  `tfr_compute.m` select processing trials with the encoding segment's indices, so they average\n  trials of the wrong accuracy and hemifield.\n- The derived hemifield column, described as 1 intact and 2 lesioned, equals the trial tables'\n  left/right column in every trial of every subject, for left- and right-lesioned patients alike.\n  The docs summary file (and Table S1) give the patients' lesioned-hemifield accuracy as that of\n  hemifield 1 in the 9 patients with one trial table, which contradicts the paper's own note that\n  the lesioned hemifield is the right one for left-lesioned patients. Which 10 controls were\n  swapped is not recorded.\n- The segments have no time buffers (500, 1500 and 900 ms), so the deposited `tfr_compute.m` and\n  `psi_compute.m`, run on them with FieldTrip's mtmconvol, return no delta-theta PSI at all and no\n  power below 7 Hz in the baseline.\n- `psianalysis.m` multiplies Fourier coefficients without the complex conjugate; its normalised\n  cross-spectrum then depends on channel B's phase alone, up to sign, and is not the PSI of\n  Nolte et al. This literal code reproduces the paper's alpha-beta PSI pattern.\n- The channel order differs between subjects' files (13 subjects), with no note in the\n  descriptor.\n- Six subjects were recorded in two blocks with two trial tables whose trial numbers overlap;\n  derived trials can be linked to them only by trial number with response time. For 4 of these\n  patients the docs summary and Table S1 accuracies do not match the two tables.\n- The pretrial segment's `fsample` field reads 255.64 Hz in 33 subjects though its time axis is\n  256 Hz.\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb/summary.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/build.py <<'EOF'
import re, nbformat, sys
sys.path.insert(0, '.')
exec(open('results.py').read())
src = "\n".join(open(p).read() for p in ["part1.py", "part2.py", "part3.py", "part4.py", "part5.py", "part6.py"])
cells = []
for block in re.split(r"^# %%", src, flags=re.M)[1:]:
    head, _, body = block.partition("\n")
    head = head.strip()
    if head.startswith("[markdown]"):
        text = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in body.strip("\n").splitlines())
        cells.append(nbformat.v4.new_markdown_cell(text))
    else:
        tags = re.findall(r'tags=\["([^"]+)"\]', head)
        c = nbformat.v4.new_code_cell(body.strip("\n"))
        if tags:
            c.metadata["tags"] = tags
        cells.append(c)
# header
cells[0] = nbformat.v4.new_markdown_cell(open("header.md").read())
i = 0
for c in cells:
    if c.cell_type == "markdown" and c.source.strip() == "**Result: ...**":
        c.source = RESULTS[i]; i += 1
assert i == len(RESULTS), i
cells.append(nbformat.v4.new_markdown_cell(open("summary.md").read()))
cells.append(nbformat.v4.new_code_cell('print(f"notebook ran in {(time.time() - T0) / 60:.1f} min; peak memory of this process "\n      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")'))
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, "entries/johnson-2017/reproduce_johnson_2017.ipynb")
print(len(cells), "cells")
EOF
cd $TMPDIR/nb && . ../dev/bin/activate && python build.py
```

```
86 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/johnson-2017 && cat > entry.yaml <<'EOF'
schema_version: 1
name: johnson-2017
type: reproduction
title: Frontoparietal oscillations in working memory after PFC lesions (Johnson et al. 2017)
description: Tests the findings of Johnson, Dewar, Solbakk, Endestad, Meling and Knight (2017) on
  CRCNS data set pfc-5, the scalp EEG and behaviour of 14 patients with unilateral prefrontal
  lesions and 20 controls in a lateralised working memory task. It covers accuracy and the
  patient covariates, task ERPs, baseline spectra, task-induced power and phase slope index
  connectivity, using the preprocessed data and the analysis code deposited with the data set.
license: Apache-2.0
notebooks:
- path: reproduce_johnson_2017.ipynb
  title: Reproducing Johnson et al. (2017) from CRCNS pfc-5
  runtime_minutes: 30
helpers:
- frontoparietal.py
related:
- id: crcns:pfc-5/unversioned
  relation: uses_data
- id: doi:10.1016/j.cub.2017.05.046
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
scipy
statsmodels
EOF
cat > README.md <<'EOF'
# Johnson et al. (2017) on CRCNS pfc-5

Tests the claims in `claims/johnson-2017.yaml` on CRCNS data set pfc-5 (doi:10.6080/K0ZC811B),
streamed from the public bucket `crcnsarchive`. The notebook `reproduce_johnson_2017.ipynb`
streams each subject's archive once, reduces it with `frontoparietal.py` and runs every test.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.
EOF
grep -rn "crcns:" ../*/entry.yaml | head -3; cd ../.. && python tools/entry.py lock entries/johnson-2017 2>&1 | tail -3; date -u
```

```
../bruno-2017/entry.yaml:19:- id: crcns:apl-1/unversioned
../deweese-2004/entry.yaml:19:- id: crcns:ac-2/unversioned
../eyherabide-2008/entry.yaml:19:- id: crcns:ia-1/unversioned
wrote johnson-2017/requirements.lock.txt (Python 3.13, with hashes)
Mon Nov  9 21:03:01 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/johnson-2017 2>&1 | tail -15
```

```
error: entries/johnson-2017/entry.yaml: (top level): Additional properties are not allowed ('python' was unexpected)
1 error(s)
```

**Agent calls Bash**

```bash
cat entries/johnson-2017/entry.yaml | tail -5; git diff --stat; git status --short | head
```

```
related:
- id: crcns:pfc-5/unversioned
  relation: uses_data
- id: doi:10.1016/j.cub.2017.05.046
  relation: reproduces
 tools/build_site.py       | 245 ++++++++++++++++++++++++++++++++++++++++++++--
 tools/entry.py            | 112 +++++++++++++++++++--
 tools/notify.py           |   5 +-
 tools/runner/chain.sh     |   5 +-
 tools/site_assets/app.css |  31 ++++++
 tools/site_assets/list.js |  33 ++++++-
 6 files changed, 411 insertions(+), 20 deletions(-)
 M tools/build_site.py
 M tools/entry.py
 M tools/notify.py
 M tools/runner/chain.sh
 M tools/site_assets/app.css
 M tools/site_assets/list.js
?? .bash_profile
?? .bashrc
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '"python"\|\bpython:' tools/entry.py | head; grep -rn "python" schemas/entry*.json | head -5; ls schemas
```

```
199:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
378:    if entry.get("python"):
379:        return str(entry["python"])
389:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
392:    line = f'python: "{version}"'
393:    if re.search(r"^python:.*$", text, re.M):
394:        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
467:    python = venv / "bin" / "python"
501:        {"entry": entry["name"], "python": python_of(entry_dir), "results": results}, indent=1) + "\n")
559:                                         "upgrade-python: the version to move to")
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Bash**

```bash
sed -n 370,400p tools/entry.py; grep -n "def check_entry\|validate(entry\|entry.schema" tools/entry.py | head
```

```
LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")


def python_of(entry_dir: Path) -> str:
    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
    (entries from before the field), else the registry's default for new entries, PYTHON_VERSION."""
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text()) or {}
    if entry.get("python"):
        return str(entry["python"])
    lock_file = entry_dir / "requirements.lock.txt"
    if lock_file.is_file():
        m = LOCK_VERSION.search(lock_file.read_text()[:2000])
        if m:
            return m.group(1)
    return PYTHON_VERSION


def set_python(entry_dir: Path, version: str) -> None:
    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
    path = entry_dir / "entry.yaml"
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
head -12 entries/johnson-2017/entry.yaml; grep -n "python" schemas/entry.schema.json | head -3; git diff tools/entry.py | grep -n "set_python" | head
```

```
schema_version: 1
name: johnson-2017
type: reproduction
title: Frontoparietal oscillations in working memory after PFC lesions (Johnson et al. 2017)
description: Tests the findings of Johnson, Dewar, Solbakk, Endestad, Meling and Knight (2017) on
  CRCNS data set pfc-5, the scalp EEG and behaviour of 14 patients with unilateral prefrontal
  lesions and 20 controls in a lateralised working memory task. It covers accuracy and the
  patient covariates, task ERPs, baseline spectra, task-induced power and phase slope index
  connectivity, using the preprocessed data and the analysis code deposited with the data set.
license: Apache-2.0
python: "3.13"
notebooks:
39:+def set_python(entry_dir: Path, version: str) -> None:
60:+        set_python(entry_dir, version)
```

**Agent calls Bash**

```bash
sed -i '/^python: "3.13"$/d' entries/johnson-2017/entry.yaml && python tools/entry.py check entries/johnson-2017 2>&1 | tail -5; sed -n 425,440p tools/entry.py; grep -n "def cmd_all\|args.command == .all.\|\"all\"" tools/entry.py | head
```

```
0 error(s)
    return out


def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
                   max_minutes: float) -> int:
    """Lock the entry for another Python version, run it, and compare what each claim's cells print with the run in
    `before` (its executed notebooks). The entry moves to the new version only when nothing differs; otherwise
    entry.yaml and the lock are put back and the differences are printed, for the attempt to record."""
    saved = {f: (entry_dir / f).read_text() for f in ("entry.yaml", "requirements.lock.txt")
             if (entry_dir / f).is_file()}
    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes):
        for f, text in saved.items():
            (entry_dir / f).write_text(text)
        print(f"error: Python {version} could not lock or run the entry; it stays on {python_of(entry_dir)}",
              file=sys.stderr)
        return 1
551:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover", "upgrade-python"])
595:    if args.command in ("check", "all"):
```

**Agent**

Check passes. Starting the full clean run now (expected ~25–35 min).

**Agent calls Bash**

```bash
date -u; time python tools/entry.py all entries/johnson-2017 2>&1 | tail -20; date -u
```

```
Mon Nov  9 21:03:33 UTC 2026
Installed kernelspec registry-johnson-2017 in executed/johnson-2017/.venv/share/jupyter/kernels/registry-johnson-2017
0 error(s)
pass  reproduce_johnson_2017.ipynb  (1628 s)

real	27m16.072s
user	80m33.010s
sys	5m36.739s
Mon Nov  9 21:30:49 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/johnson-2017/; . $TMPDIR/dev/bin/activate && python - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat
nb = nbformat.read('executed/johnson-2017/reproduce_johnson_2017.ipynb', 4)
for i, c in enumerate(nb.cells):
    if c.cell_type != 'code': continue
    print(f"===== cell {i} tags={c.metadata.get('tags')}")
    for o in c.get('outputs', []):
        if o.output_type == 'stream' and o.name == 'stdout': print(o.text)
        elif o.output_type == 'error': print('ERROR', o.ename, o.evalue)
EOF
wc -l $TMPDIR/exec_out.txt; grep -n "ERROR\|took\|peak memory\|notebook ran" $TMPDIR/exec_out.txt
```

```
reproduce_johnson_2017.ipynb
result.json
787 /tmp/claude-1001/exec_out.txt
105:loading and per-subject computation took 19.1 min; peak memory of this process 0.60 GB
735:PSI tests took 2.1 min
783:all group tests took 7.8 min; whole notebook so far 27.0 min; peak memory 3.44 GB
786:notebook ran in 27.0 min; peak memory of this process 3.44 GB
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/exec_out.txt",
 "offset": 100,
 "limit": 700
}
```

```
File content (25825 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "proc holds\|lesioned' hemifield\|N1 lateral\|channel order\|derived trials linked\|docs 'vhf_lesion'\|first time above\|threshold\|fsample fields\|frequencies with any\|PSI dt:\|PSI ab:\|duplicate\|neighbouring" exec_out.txt; sed -n '/^ *total_mean/,/^ranges/p' exec_out.txt; grep -n "^age\|^education\|^males\|coding S1: smallest\|coding B: smallest\|coding .*trials:\|^(a)\|^(b)\|^(c)\|group only\|full, \|Cohen\|converged" exec_out.txt
```

```
74:psi_compute.m:48: cfggt.threshold = 1.96; % z-score threshold, p = 0.05
146:channel order of the files differs from ctrl01's in 13 subjects (an interpolated channel moved to the end); every array is put in one order: True
149:fsample fields: ['(255.64, 256.0, 256.0)', '(256.0, 256.0, 256.0)']
150:derived trials linked to one trial-table row (trial number and response time): 6369 of 6369 | trial info agrees where linked: True
153:proc holds the same trials as encmain: True | in the same order: 0 of 34
154:duplicate recordings (identical first-trial sums or identical data_derived.mat): 0 0
157:N1 lateralisation positive in 11 of 20 controls
158:N1 lateralisation positive in 6 of 7 left-lesioned patients
159:N1 lateralisation positive in 2 of 7 right-lesioned patients
160:neighbouring-channel correlation, median (range): 0.495 0.18 0.58
196:controls: docs 'vhf_lesion' equals the trial-table accuracy of hemifield 1 in 10, of hemifield 2 in 10 of 20 (within 0.006)
197:patients: docs 'vhf_lesion' equals the trial-table accuracy of hemifield 1 in 9, of hemifield 2 in 1 of 14 (within 0.006)
202:frequencies with any baseline value under FieldTrip's window rule ('fit'): 7 to 40 Hz; proc frequencies with any value: 4 to 40 Hz
203:PSI dt: time points whose windows all fit, pretrial/encmain/proc: 0 0 0
204:PSI ab: time points whose windows all fit, pretrial/encmain/proc: 2 12 6
207:encoding-maintenance: threshold |t| > 3.64; first time above it 656 ms; peak |t| 5.9 at 684 ms
216:processing: threshold 2.94; first time above it 20 ms; peak |t| 8.2 at 836 ms
                 total_mean  les_mean  les_sd  les_min  les_max  int_mean  int_sd  int_min  int_max
reading  coding                                                                                    
all kept A            187.3      94.4    21.1       55      119      93.0    22.1       51      120
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/^coding A: encoding-maintenance/,/^   window          r hemifield/p' exec_out.txt | grep -v "^   [+-] p = 1.000" | head -80
```

```
coding A: encoding-maintenance, lesioned hemifield, group main effect
   - p = 0.006  sum t = -391.9  time 820.312-886.719 ms  channels (15): AF7 F5 F7 FT7 FC5 FC3 C1 C3 C5 T7 P1 Pz CPz Cz CP2
   + p = 0.014  sum t = 309.1  time 753.906-863.281 ms  channels (6): TP8 P4 P6 P8 P10 PO8
   + p = 0.206  sum t = 169.9  time 800.781-867.188 ms  channels (7): CP3 CP1 P3 P5 P7 P9 PO7
   + p = 0.562  sum t = 118.9  time 335.938-382.812 ms  channels (5): Fp1 AF3 F1 F3 AFz
   - p = 0.794  sum t = -104.1  time 917.969-953.125 ms  channels (10): CP1 P1 P3 P5 PO3 Pz CPz CP2 P2 P4
   + p = 0.842  sum t = 99.4  time 1144.53-1187.5 ms  channels (6): F3 F5 FC3 C1 C3 CP1
   cluster p = 0.006: extends past 400 ms True; includes P6/P8/P10/PO8 False; anterior channels ['F5', 'F7', 'FC5', 'FT7', 'C3', 'C5', 'T7']; mean ERP in cluster controls -0.33, patients 0.52
   cluster p = 0.014: extends past 400 ms True; includes P6/P8/P10/PO8 True; anterior channels []; mean ERP in cluster controls 1.23, patients -0.09

coding B: encoding-maintenance, lesioned hemifield, group main effect
   - p = 0.070  sum t = -209.1  time 820.312-871.094 ms  channels (15): F5 F7 FT7 FC5 C5 T7 CP3 CP1 P1 Pz CPz Cz C2 C4 C6
   - p = 0.386  sum t = -141.0  time 902.344-960.938 ms  channels (13): TP7 CP5 CP1 P1 P3 P5 P7 PO7 Pz CPz Cz CP2 P2
   + p = 0.900  sum t = 99.1  time 1156.25-1191.41 ms  channels (7): C1 C3 TP7 CP5 CP3 P3 P5
   + p = 0.932  sum t = 96.9  time 828.125-867.188 ms  channels (4): P5 P7 P9 PO7
   + p = 0.970  sum t = 95.0  time 765.625-804.688 ms  channels (4): P4 P6 P8 PO8
posterior P6-P8-P10-PO8, 400-800 ms, mean ERP (coding A): controls 0.24, patients 0.12

===== cell 37 tags=['claim:erp-processing-interaction']
coding A: group x hemisphere
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/claim:power-anterior-theta-controls/,/claim:psi-deltatheta-bottomup/p' exec_out.txt | grep -v "^   [+-] p = 1.000" | cut -c1-200 | head -120
```

```
===== cell 51 tags=['claim:power-anterior-theta-controls']
   window          r hemifield  enc mean Z 0-0.4 s  enc mean Z 0.4-1.5 s  proc max group-mean Z  proc frac. time group mean > 3.29  max fraction of controls > 3.29 (proc)  group-mean max lies in proc 
0     pad  hemifield    pooled                2.19                  1.79                   3.74                               0.50                                    0.55                         True 
1     pad  hemifield         1                1.83                  1.58                   3.81                               0.41                                    0.55                         True 
2     pad  hemifield         2                2.55                  1.99                   3.69                               0.54                                    0.55                         True 
3     pad        all    pooled                3.11                  2.53                   5.32                               0.73                                    0.65                         True 
4     pad        all         1                2.64                  2.27                   5.46                               0.73                                    0.65                         True 
5     pad        all         2                3.59                  2.80                   5.19                               0.74                                    0.65                         True 
6     fit  hemifield    pooled                0.34                  0.11                   0.81                               0.00                                    0.20                         True 
7     fit  hemifield         1                0.17                 -0.16                   0.73                               0.00                                    0.20                         True 
8     fit  hemifield         2                0.51                  0.39                   0.95                               0.00  
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/claim:psi-deltatheta-bottomup/,$p' exec_out.txt | grep -v "^  dt\|^  ab\|^ *patients enc" | cut -c1-230 | grep -n "" | sed -n '1,200p' | grep -v "^[0-9]*: *$" | head -150
```

```
1:===== cell 66 tags=['claim:psi-deltatheta-bottomup-encoding']
2:      reading                         ROI  hemifield     group  min group-mean Z 300-500 ms  fraction of subjects <= -9 at some point there  fraction <= -1.96
3:0   trialwise      (b) Figure S4 ANTERIOR          2  controls                         6.09                                            0.50               0.60
4:1   trialwise      (b) Figure S4 ANTERIOR          2  patients                         4.72                                            0.14               0.50
5:2   trialwise      (b) Figure S4 ANTERIOR          1  controls                         8.63                                            0.45               0.75
6:3   trialwise      (b) Figure S4 ANTERIOR          1  patients                         4.37                                            0.36               0.57
7:4   trialwise  (a) power-lowtheta cluster          2  controls                         6.09                                            0.50               0.60
8:5   trialwise  (a) power-lowtheta cluster          2  patients                         4.72                                            0.14               0.50
9:6   trialwise  (a) power-lowtheta cluster          1  controls                         8.63                                            0.45               0.75
10:7   trialwise  (a) power-lowtheta cluster          1  patients                         4.37                                            0.36               0.57
11:8       nolte      (b) Figure S4 ANTERIOR          2  controls                        -0.21                                            0.00               0.00
12:9       nolte      (b) Figure S4 ANTERIOR          2  patients                         0.02                                            0.00               0.00
13:10      nolte      (b) Figure S4 ANTERIOR          1  controls                        -0.19                                            0.00               0.00

[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; sed -n '/^findings:/,/^[a-z_]*:/p' attempts/fouke-2025-01.yaml | head -30; python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); 
o=s['properties']['outcomes']['items']; print('outcome', o.get('required'), list(o['properties']))
f=s['properties']['findings']['items']; print('finding', f.get('required'), list(f['properties']))
print('dataset', s['properties'].get('datasets',{}).get('items',{}).get('properties',{}).keys())
print(list(s['properties']))
"
```

```
Mon Nov  9 21:31:20 UTC 2026
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
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/johnson-2017.yaml 2>/dev/null || ls papers/datasets | head; sed -n '/^provenance:/,/^inputs:/p' attempts/fouke-2025-01.yaml; grep -rn "crcns" attempts/deweese-2004-01.yaml | head -5; ls questions | head -3
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.cub.2017.05.046
datasets:
- archive: crcns
  id: pfc-5
  relation: primary
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
4:- archive: crcns
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,12p attempts/deweese-2004-01.yaml; grep -n "^  harness" attempts/*.yaml | tail -2
```

```
schema_version: 3
id: deweese-2004-01
datasets:
- archive: crcns
  id: ac-2
  version: unversioned
  doi: 10.6080/K0G44N6R
  relation: primary
paper: doi:10.1152/jn.00197.2004
date: '2026-11-04'
entry: deweese-2004
provenance:
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec && cat > $TMPDIR/rec/make.py <<'PYEOF'
import yaml
NB = "reproduce_johnson_2017.ipynb"
COMMON_DEV = [
    "The analysis runs in Python, not MATLAB and FieldTrip (release 20151205); mtmconvol, mtmfft, the FIR low-pass, the cluster test (maxsum, minnbchan 2, correcttail prob) and the models are reimplemented from FieldTrip's code at commit b3909bfecc5273652756ed2e41f84e9195f96186 and the paper's scripts.",
]
O = []
def add(claim, outcome, notes, deviations=None, measured=None, assumed=None):
    d = {"claim": claim, "outcome": outcome, "notebook": NB, "output": f"claim:{claim}"}
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    if deviations:
        d["deviations"] = deviations
    if assumed:
        d["assumed"] = True
    O.append(d)

add("cohort-and-trials", "reproduced",
    "14 patients and 20 controls. Over all trials kept in data_derived.mat (reading a), 187.3 trials per subject, 94.4 +- 21.1 (55 to 119) in the lesioned and 93.0 +- 22.1 (51 to 120) in the intact hemifield under hemifield coding A (the descriptor's); coding B gives 93.7 +- 21.5 and 93.6 +- 21.8 with the same ranges. Correct trials only (reading b) give 172.4 per subject, outside 187 +- 18.7, and lesioned 87.1 +- 21.2 (36 to 112), intact 85.2 +- 21.7 (34 to 116), whose minima fall outside the widened ranges. Reading a matches.",
    measured=[14, 20, 187.3, 94.4, 93.0])
add("demographics-matched", "reproduced",
    "No test gives p < 0.05. Age t(32) = 0.35, p = 0.725 (paper t < 0.36, p > 0.72); education t(32) = -1.38, p = 0.178 (paper t < 1.22, p > 0.23); variance F(13,19) = 0.76, one-tailed p = 0.685 for age and 1.42, p = 0.237 for education (paper F < 1.31, p > 0.31). Patients 46.4 +- 16.4 years, controls 44.1 +- 18.8. The education statistics do not match the paper's bounds, though they lead to the same conclusion. Ages and education are from the docs summary files of the data set.",
    measured=[46.4, 44.1])
add("patient-factors-no-effect", "reproduced",
    "In the repeated-measures ANCOVA (14 patients, 11 between-subject terms as Table S2 lists them, factors coded +-1, Type III, sphericity assumed) no term has p < 0.05; the smallest is gender, F(1,2) = 7.96, p = 0.106, and the paper's bound is p > 0.14. Individual F values differ from Table S2 (age 7.27 against 4.38, gender 7.96 against 5.33, IQ 6.40 against 2.56). Coding the lesioned hemifield as in Table S1 or as left/right by lesion side (coding B) changes only the hemifield terms, none significant under either.",
    deviations=["The ANCOVA is computed as SPSS GLM does it (Type III, effect-coded factors, raw covariates), reimplemented with least squares; the paper ran it in SPSS 20. Etiology is coded stroke against tumour resection, as the claims file says (one degree of freedom in Table S2)."])
add("table-s1-patient-accuracy", "partially_reproduced",
    "20 of 28 values are within 0.02 of Table S1 when trial-table hemifield 1 is taken as the lesioned one for every patient (the coding of the docs summary file, which holds Table S1's values), with all trial-table trials (reading a) or with the trials kept after cleaning (reading b). The 8 misses are the 4 patients recorded in two blocks, pfc10 to pfc13 (|differences| 0.028 to 0.098); their two trial tables together do not give the table's values. Taking the descriptor's coding of the trial tables (1 left, 2 right) with the paper's note that the lesioned hemifield is the right one for left-lesioned patients gives 6 to 12 of 28. Measured values range from 0.65 to 0.98, as in the table.",
    deviations=["pfc01 to pfc14 are matched to Table S1 rows 1 to 14; lesion hemisphere, size, age and gender of the docs file agree row by row.",
                "The hemifield coding that matches Table S1 (hemifield 1 lesioned in every patient) contradicts the paper's own note and the descriptor; it is shown with the other codings, and the outcome is the same count (20) under both denominators of the criterion."],
    measured=20)
add("accuracy-patients-impaired", "partially_reproduced",
    "Mean accuracy is 0.952 +- 0.031 in controls and 0.872 +- 0.099 in patients (subject accuracy over all trials, or the mean of six cells; identical). In the group-only linear mixed model (204 cells, random intercept per subject) the group effect is F(1,202) = 11.68, p = 7.6e-4, patients lower: below the Bonferroni level 0.0071 but not below 7e-5. The binomial logit reading gives F(1,202) = 25.83, p = 8.5e-7, which meets the bound. F is outside 16.77 +- 1.68 in both. The full model's group effect is F(1,196) = 0.22, p = 0.64 (linear, condition as a number; the paper's 4.70, p = 0.03), and the full binomial model did not converge. Cohen's d on subject accuracies 1.18 (paper 1.47).",
    deviations=["The Results call the model logit, the Methods linear; the readings give different outcomes (p bound met only by the logit model), and the Methods' linear model is adopted, as for accuracy-no-hemifield-condition-effect. Both are shown.",
                "Linear model fitted with statsmodels MixedLM (REML); binomial model by maximum likelihood with 30-point Gauss-Hermite quadrature; F = (beta/se)^2 with the residual degrees of freedom, as fitglme reports."],
    measured=[0.952, 0.872, 11.68], assumed=True)
add("patients-above-chance", "reproduced",
    "On each patient's overall accuracy (reading a) t(13) = 14.13, one-tailed p = 1.4e-9, above 13.89. Per hemifield (reading b) t = 13.63 and 13.76, and per hemifield and condition (reading c) t = 6.28 to 29.63, below 13.89 in four of six tests, so the claim holds under reading a only. Every test is far above chance (largest p = 1.4e-5).",
    measured=14.13)
add("accuracy-no-hemifield-condition-effect", "reproduced",
    "In the linear mixed model with hemifield and condition only, hemifield F(1,200) = 0.01, p = 0.915; condition F = 2.84, p = 0.094; interaction F = 0.13, p = 0.715. The binomial logit reading finds a condition effect (F(1,200) = 20.71, p < 0.001), and with condition as a three-level factor the spatial condition differs from identity (F = 12.64, p < 0.001); subject mean accuracy is 0.879, 0.956 and 0.922 in the identity, spatial and temporal conditions. Variant, the full model: hemifield p = 0.430, condition p = 0.038, interaction p = 0.525 (linear). Coding B gives p = 0.468, 0.022 and 0.602.",
    deviations=["The readings give different outcomes; the Methods' linear model is adopted (STAR Methods, Behavioral Analysis, \"Accuracy was tested in a linear mixed-effects model\"), with the logit model of the Results shown."],
    assumed=True)
add("erp-lesioned-maintenance", "reproduced",
    "Under coding A two group clusters pass p < 0.05 after 400 ms. One covers F5, F7, FT7, FC5, C3, C5, T7 (with AF7, FC3, C1, P1, Pz, CPz, Cz, CP2) at 820 to 887 ms, p = 0.006; in it the patients' mean ERP is +0.52 and the controls' -0.33, opposite signs. The other covers TP8, P4, P6, P8, P10, PO8 at 754 to 863 ms, p = 0.014, controls 1.23 against patients -0.09 (patients attenuated). Both match the paper's channels; they lie about 350 to 490 ms into maintenance. Under coding B neither survives (smallest p = 0.070).",
    deviations=["The ERP is filtered on the trial average (the filter is linear), with mirror padding to 7.5 s and FieldTrip's default FIR order; baseline is the mean over time of the correct-trial pretrial ERP (erp_compute.m)."],
    assumed=True)
add("erp-processing-interaction", "not_reproduced",
    "No group by hemisphere cluster passes p < 0.05 at active processing (smallest p = 0.294 under coding A, 0.500 under coding B, 0.272 with the trial selection of erp_compute.m). The patients' index over FP1-AF3-AF7-F5-F7-FC5-FT7 at 50 to 150 ms is higher than the controls' (0.38 against 0.05), the direction the paper reports. No group main effect under coding A (smallest p = 0.636); the code's selection gives one (p = 0.036, right posterior channels, 55 to 141 ms).",
    deviations=["The processing segment is matched to trials by trial number; data_derived.mat stores it in another order than the other segments, and erp_compute.m applies the encoding segment's indices to it. The code's selection is shown as a variant."])
add("erp-intact-none", "reproduced",
    "For the intact hemifield no cluster has p < 0.05: encoding-maintenance main effect smallest p = 0.554, processing main effect 0.126, processing group by hemisphere 0.188 (coding A); 0.518, 0.180 and 0.706 under coding B. The paper gives pcluster > 0.33; two tests here fall below 0.33.")
add("baseline-spectral-interaction", "reproduced",
    "One group by hemisphere cluster passes, p = 0.004 (the paper's value), over AF3, F3, F5 and FC3 from 3 to 19 Hz, with the patients' lesioned-minus-intact power above the controls' (index at AF3-F3-F5, 6 to 18 Hz, 2.48 against -0.30; 10 of 14 patients above 0.3). The cluster extends below the paper's 6 Hz, down to 3 Hz.",
    deviations=["All trials, 1 to 40 Hz (fft_compute.m uses 2 to 40 Hz; the claims file says 1 to 40)."])
add("baseline-no-group-effect", "partially_reproduced",
    "No cluster of the group main effect passes (smallest p = 0.066, controls above patients at 13 to 40 Hz over 23 mostly anterior channels). 476 of 2560 channel-frequency points have uncorrected p < 0.05, where the paper says uncorrected p > 0.05; the criterion marks the claim as only partly holding when any point passes. Posterior lesioned-side alpha power is 17.4 in controls and 11.5 in patients.")
add("power-anterior-theta-controls", "reproduced",
    "With windows running into the zero padding, the controls' 2 to 7 Hz Z over AF7-F5-F7-FC5-FT7 (both hemifields pooled, r = trials of the hemifield) has a group mean of 2.2 at 0 to 0.4 s and 1.8 later in encoding-maintenance, exceeds 3.29 at 50% of processing time points and reaches its maximum, 3.74, at 0.53 s of processing; per hemifield 3.81 and 3.69. With r = all correct trials the maximum is 5.32. At most 55% of controls exceed 3.29 at any processing time point, so reading b of O7 (most subjects) holds only narrowly. Under FieldTrip's window rule the baseline has values only from 7 Hz and the maximum is 0.81 to 1.36.",
    deviations=["Assumption, window edges. The deposited segments have no buffers, and FieldTrip's mtmconvol returns NaN wherever a 3/f window leaves the segment, so below 7 Hz no baseline value exists and 2 to 6 Hz power cannot be Z scored. The values over the zero padding the Methods name (\"zero-padded to 7,500 ms\") are kept; this is the only reading under which the 2 to 7 Hz result exists. Both readings are shown.",
                "The bootstrap of zbaseline.m (1000 draws of r baseline values) is replaced by its expectation, mean and sd / sqrt(r) * sqrt((N - r) / (N - 1))."],
    measured=3.74, assumed=True)
add("power-posterior-alphabeta", "not_reproduced",
    "Over P1-P3-P5-P7-P9-PO3-PO7-O1 the 9 to 24 Hz Z is below -1.96 at no more than 4% of maintenance time points with padded windows and at most 20% under FieldTrip's rule (r = all trials), in either group; the maximum over maintenance is 0.21 to 1.75. In processing the group mean is below -3.29 at 0 to 1% of time points with r = trials of the hemifield and up to 54% with r = all trials. The 12 to 35 Hz Z is above zero at 0 to 0.4 s in both groups (0.38 to 1.10), and 8 to 12 Hz is slightly negative there (-0.42 controls, -0.51 patients).")
add("power-lowtheta-interaction", "partially_reproduced",
    "On the 3 to 4 Hz mean (O2 reading b), the lesioned hemifield gives a group by hemisphere cluster over AF7, F5, F7, FT7 and FC5 at 12 to 352 ms of processing, p = 0.040 (the paper's 0.04), with the patients' index below the controls' (-1.79 against 0.27 over the segment); the intact hemifield's cluster over F5-F7-FT7-FC5 at 461 to 578 ms has p = 0.134 (paper 0.036). On channels by frequency by time (reading a, as tfr_stat_group_hem.m runs it) neither hemifield is significant (p = 0.508 and 0.834), though the leading cluster lies at 3 to 5 Hz in the same five channels. Under FieldTrip's window rule there is no value at 3 to 4 Hz.",
    deviations=["Assumption, window edges, as for power-anterior-theta-controls.",
                "Assumption, O2. The readings differ (reading a not significant in either hemifield). Reading b is adopted, as Figure 2 reports the test on low-theta (3-4 Hz) asymmetry and the paper's tfr_stat_group.m restricts frequencies when asked; reading a is shown."],
    assumed=True)
add("power-no-group-main-effect", "reproduced",
    "No group main effect cluster passes on channels by frequency by time in either segment, hemifield or window reading (smallest p = 0.388). On band means (O2 reading b) the smallest p is 0.062 (3 to 4 Hz, encoding-maintenance, lesioned hemifield). Controls minus patients is +1.18 to +1.31 Z in anterior 3 to 4 Hz during encoding-maintenance and -0.06 to +0.01 in processing; in posterior 9 to 24 Hz -0.43 to +0.14.")
PSI_DEV = "Assumption, PSI. The Methods compute PSI from the cross-spectral density (Nolte et al. 2008); psianalysis.m averages per-trial phase slopes, Z scores them on a null from the frequency-shuffled trial-mean coherency, and multiplies the Fourier coefficients without the complex conjugate, so that its normalised cross-spectrum depends on channel B's phase alone, up to sign. The adopted reading follows the code's structure with the conjugate (trialwise); Nolte's PSI of the trial-averaged coherency and the literal code are shown."
PSI_WIN = "Window edges. Under FieldTrip's rule no delta-theta PSI exists in any segment (the 2 Hz window is 1.5 s), so the padded windows are used; for alpha-beta the fit reading is shown where values exist."
add("psi-deltatheta-bottomup-encoding", "not_reproduced",
    "No reading gives the PFC (AF7-F5-F7-FC5-FT7, which is also the power-lowtheta cluster) to parieto-occipital delta-theta Z at -9 or below within 100 ms of 400 ms in both groups. Trialwise, group means at 300 to 500 ms stay positive (minima 4.37 to 8.63); Nolte, -0.21 to 0.06; literal code, controls 7.63 and 12.27, patients -6.24 and -6.64. At most 57% of subjects in a group reach -9 at some point there (literal, patients).",
    deviations=[PSI_DEV, PSI_WIN])
add("psi-deltatheta-pfc-lead-controls", "not_reproduced",
    "Trialwise, the controls' Z exceeds 1.96 in maintenance (maximum 19.2 and 15.0) but in early processing reaches only 4.27 and 0.17, and the patients reach 14.4 and 11.0. Nolte's PSI stays within -0.06 to 0.40 in both groups. The literal code gives controls 21.0 and 22.3 in early processing but larger values at the segment edges (227), and patients up to 186. No reading has the controls' maximum in early processing with patients below 1.96.",
    deviations=[PSI_DEV, PSI_WIN])
add("psi-deltatheta-group-clusters", "not_reproduced",
    "With the per-seed test of psi_stat_group.m (each seed channel its own test), trialwise PSI, significant clusters cover 2 of the 7 processing time points of the lesioned window (100 and 400 ms of 100 to 700) and 2 of 6 of the intact window (0 and 100 ms of 0 to 500), not most. In encoding-maintenance the lesioned hemifield has clusters at 200 ms and 700 to 800 ms among others (7 clusters, 200 to 1500 ms), the intact one only at 700 and 800 ms, outside its windows. Clustering per pair (reading a) or over neighbouring pairs (reading b) finds no cluster (smallest p = 0.564). With the literal code the lesioned processing window is covered at 4 of 7 points (100 to 500 ms) and the intact at 2 of 6; with Nolte's PSI 3 of 7 and 3 of 6. Clusters of both signs occur.",
    deviations=[PSI_DEV, PSI_WIN, "Clustering. Readings a and b of the claims file and the per-seed test of psi_stat_group.m are all run; none meets the criterion."])
add("psi-network-degree", "not_reproduced",
    "No degree reading gives a cluster with p <= 0.01 of patients below controls early in processing in both hemifields. Trialwise PSI, the closest are the sum of |Z| in either direction (reading c) at 0 to 100 ms in FC6, C6, T8, CP6, P6, P8, P10, PO8 (right, the intact side), p = 0.046, lesioned hemifield only; and the code's degree count (in plus out, Z > 1.96) at 800 ms, p = 0.022. With the literal code the out-degree count gives p = 0.006 at 0 to 100 ms with patients above controls.",
    deviations=[PSI_DEV, PSI_WIN, "Degree. The code's ft_networkanalysis 'degrees' on Z > 1.96 (in-degree plus out-degree) is run with the claims file's three readings."])
add("psi-alphabeta-bottomup", "not_reproduced",
    "Trialwise, the controls' alpha-beta Z from PFC to parieto-occipital channels is mostly positive (median 3.70 and 3.78; below -1.96 at 12 and 25% of encoding-maintenance points); patients' median -1.59 and -0.64. Nolte's PSI never passes -1.96. The literal code of psianalysis.m reproduces the claim in both groups and hemifields, Z below -1.96 at 94% of encoding-maintenance and 100% of processing points (median about -23). Under FieldTrip's window rule the trialwise controls' Z is mostly negative where defined (for example -17.5 to 6.3, lesioned hemifield).",
    deviations=[PSI_DEV, "Window edges. The padded windows are used; the fit reading is shown where values exist."],
    assumed=True)
add("psi-alphabeta-no-group-effect", "not_reproduced",
    "The per-seed test of psi_stat_group.m finds alpha-beta clusters with p < 0.05 in three of four segment and hemifield combinations with trialwise PSI (smallest p = 0.010), with Nolte's PSI in four of four (smallest 0.002) and with the literal code in three of four (smallest 0.020). It tests each of 64 seeds at 0.05 with no correction across seeds, so clusters are expected by chance. Clustering per pair or over neighbouring pairs finds none (p = 1.0). Controls minus patients in the PFC to parieto-occipital Z is +3.3 to +6.9 (trialwise).",
    deviations=[PSI_DEV, "Absence is judged on the paper's test, the per-seed cluster test of psi_stat_group.m, which the claims file allows the author to follow; readings a and b are shown."],
    assumed=True)

for o in O:
    o.setdefault("deviations", [])
    o["deviations"] = o["deviations"] + COMMON_DEV

rec = {
 "schema_version": 3,
 "id": "johnson-2017-01",
 "datasets": [{"archive": "crcns", "id": "pfc-5", "version": "unversioned", "doi": "10.6080/K0ZC811B", "relation": "primary"}],
 "paper": "doi:10.1016/j.cub.2017.05.046",
 "date": "2026-11-09",
 "entry": "johnson-2017",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-14"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/42682552461"}},
 "inputs": [{"what": "FieldTrip's biosemi64 neighbour template (template/neighbours/biosemi64_neighb.mat), which the paper's *_stat_group.m scripts load through ft_prepare_neighbours; and FieldTrip's ft_specest_mtmconvol.m, ft_specest_mtmfft.m and ft_networkanalysis.m, read to reimplement them.",
             "source": "https://github.com/fieldtrip/fieldtrip at commit b3909bfecc5273652756ed2e41f84e9195f96186"}],
 "outcomes": O,
 "findings": [
  {"kind": "format_error", "statement": "In data_derived.mat the proc (active processing) segment holds the same trials as the pretrial and encmain segments but in another order, in all 34 subjects; its trialinfo is reordered with it. Nothing in the descriptor says so."},
  {"kind": "code_mismatch", "statement": "erp_compute.m and tfr_compute.m select the processing segment's correct trials and hemifields with indices taken from encmain.trialinfo, so, given the reordering, they average processing trials of the wrong accuracy and hemifield. With the code's selection the processing ERP gives a group main effect (p = 0.036) that the matched trials do not (p = 0.636)."},
  {"kind": "code_mismatch", "statement": "psianalysis.m computes the cross-spectrum as the product of the two channels' Fourier coefficients without a complex conjugate (in both deposited versions). Its normalised cross-spectrum then equals plus or minus exp(2i phase of channel B), independent of channel A except for its sign, which is not the phase slope index of Nolte et al. (2008) that the Methods cite. This literal code reproduces the paper's alpha-beta PSI pattern (Z about -23 throughout in both groups)."},
  {"kind": "methods_unavailable", "statement": "Question for the authors. The deposited segments are 500, 1500 and 900 ms long with no buffers, so FieldTrip's mtmconvol with 3/f windows (tfr_compute.m, psi_compute.m) returns no value where a window leaves the segment, no baseline power below 7 Hz, no 3 to 4 Hz power at all in processing, and no delta-theta PSI in any segment. Were the analyses run on longer segments (the Methods mention 1000 ms buffers at epoching), or were windows allowed to run into the zero padding? This attempt assumed the latter."},
  {"kind": "metadata_error", "statement": "The descriptor says trialinfo column 3 of data_derived.mat is 1 intact and 2 lesioned visual hemifield, but it equals the trial table's column C (1 left, 2 right) in every trial of every subject, for left- and right-lesioned patients alike. The docs summary file (whose patient values are Table S1's) gives the patients' lesioned-hemifield accuracy as that of trial-table hemifield 1 in all 9 single-block patients, left- and right-lesioned, which contradicts the paper's note that the lesioned hemifield is the right one for left-lesioned patients. Early visual lateralisation (N1, 150 to 220 ms) is positive in 6 of 7 left-lesioned and 2 of 7 right-lesioned patients, which hints that the column is left/right. The ERP and baseline results reproduce under the descriptor's coding and not under the left/right one."},
  {"kind": "metadata_insufficient", "statement": "Which 10 controls were swapped across the midline is not recorded; in the docs summary file 10 controls have their 'lesion' accuracy equal to hemifield 1 and 10 to hemifield 2 (with ties), which may encode it, but no file says so."},
  {"kind": "metadata_insufficient", "statement": "Six subjects (ctrl08, pfc03, pfc10 to pfc13) were recorded in two blocks with two trial tables whose trial numbers overlap (for example pfc03 numbers 21 to 120 in one and 2 to 240 in the other; ctrl08's first table has 240 rows of which 117 are empty). Derived trials can be linked to a table row only by trial number together with response time (6369 of 6369 linked this way). For 4 of these patients the docs summary and Table S1 accuracies do not match the two tables (differences up to 0.098)."},
  {"kind": "format_error", "statement": "The channel order of data_derived.mat differs between subjects: in 13 subjects an interpolated channel is moved to the end of the label list. Analyses that index channels by position, across subjects, mix channels; the deposited scripts select channels by label for the hemisphere index but grand-average the other data by position."},
  {"kind": "metadata_error", "statement": "The pretrial segment's fsample field reads 255.64 Hz in 33 subjects (256 in pfc11), though its time axis (129 samples over 0 to 0.5 s) and the other segments are at 256 Hz. The descriptor's summary gives 6 male patients; the docs summary file and the paper give 5."},
  {"kind": "other", "statement": "The per-seed PSI cluster test of psi_stat_group.m tests each of the 64 seed channels at a cluster level of 0.05 with no correction across seeds; on alpha-beta PSI, which the paper reports as unaffected by group, it yields significant clusters in three of four tests here."},
  {"kind": "other", "statement": "Whether the segments share the clock of the trial tables could not be established from the data: the posterior ERP, taken from its first 50 ms, departs from zero only at 656 ms of the encoding-maintenance segment (threshold from a sign-flip null), with no clear visual response to the stimuli at 0 and 200 ms; the processing segment has no event inside it to check against. That the ERP and baseline clusters match the paper's channels and p values is consistent with the alignment."},
 ],
}
class D(yaml.SafeDumper):
    pass
def str_rep(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)
D.add_representer(str, str_rep)
txt = yaml.dump(rec, Dumper=D, sort_keys=False, width=100, allow_unicode=True)
open("attempts/johnson-2017-01.yaml", "w").write(txt)
print(len(txt))
PYEOF
. $TMPDIR/dev/bin/activate && pip list 2>/dev/null | grep -i pyyaml || uv pip install -q pyyaml; python $TMPDIR/rec/make.py && grep -n "—\|rather\|\*\*" attempts/johnson-2017-01.yaml | head; date -u
```

```
PyYAML                    6.0.3
Traceback (most recent call last):
  File "/tmp/claude-1001/rec/make.py", line 1, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Mon Nov  9 21:32:54 UTC 2026
```

**Agent calls Bash**

```bash
python3 $TMPDIR/rec/make.py && grep -n "—\|rather\|\*\*" attempts/johnson-2017-01.yaml | head; python tools/entry.py check entries/johnson-2017 2>&1 | tail -5
```

```
35911
0 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR/rec && python3 - <<'EOF'
s=open('make.py').read()
s=s.replace(" (index at AF3-F3-F5, 6 to 18 Hz, 2.48 against -0.30; 10 of 14 patients above 0.3)"," (index at AF3-F3-F5, 6 to 18 Hz, 2.48 against -0.30)")
s=s.replace("In processing the group mean is below -3.29 at 0 to 1% of time points with r = trials of the hemifield and up to 54% with r = all trials.","In processing the group mean is below -3.29 at 0 to 28% of time points with r = trials of the hemifield and up to 54% with r = all trials.")
open('make.py','w').write(s)
EOF
python3 make.py; cd  && python3 - <<'EOF'
import nbformat
old="In processing it is below -3.29 at 1% (r = trials of the hemifield) to 54% (r = all trials) of time points."
new="In processing it is below -3.29 at 0 to 28% (r = trials of the hemifield) and up to 54% (r = all trials) of time points."
for p in ["entries/johnson-2017/reproduce_johnson_2017.ipynb","executed/johnson-2017/reproduce_johnson_2017.ipynb"]:
    nb=nbformat.read(p,4); n=0
    for c in nb.cells:
        if c.cell_type=="markdown" and old in c.source: c.source=c.source.replace(old,new); n+=1
    nbformat.write(nb,p); print(p,n)
EOF
sed -i 's/In processing it is below -3.29 at 1% (r = trials of the hemifield) to 54% (r = all trials) of time points./In processing it is below -3.29 at 0 to 28% (r = trials of the hemifield) and up to 54% (r = all trials) of time points./' $TMPDIR/nb/results.py; grep -c "0 to 28%" $TMPDIR/nb/results.py
```

```
35879
entries/johnson-2017/reproduce_johnson_2017.ipynb 1
executed/johnson-2017/reproduce_johnson_2017.ipynb 1
1
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/johnson-2017 2>&1 | tail -3 && python tools/entry.py handover entries/johnson-2017 2>&1 | tail -5; ls executed/johnson-2017/handover/; date -u
```

```
0 error(s)
wrote executed/johnson-2017/handover
frontoparietal.py
johnson-2017.yaml
reproduce_johnson_2017.ipynb
Mon Nov  9 21:33:46 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import nbformat
nb=nbformat.read('executed/johnson-2017/handover/reproduce_johnson_2017.ipynb',4)
print(sum('**Result' in c.source for c in nb.cells if c.cell_type=='markdown'), any('## Summary' in c.source for c in nb.cells))
"; git status --short | grep -v "^ M tools\|^?? \.\|idea"; rm -rf $TMPDIR/subj $TMPDIR/all.pkl $TMPDIR/pfc02.mat $TMPDIR/pfc02.csv
```

```
0 False
?? attempts/johnson-2017-01.yaml
?? entries/johnson-2017/
?? scripts
?? tools/colab.py
?? tools/journals.py
```

**Agent calls Bash**

```bash
ls -la scripts | head; git ls-files scripts | head -3
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  9 19:21 scripts
```

**Agent**

I've finished steps 1 to 6 for `entries/johnson-2017` on CRCNS pfc-5. All 22 claims were tested and none is blocked: 10 reproduced, 4 partially reproduced, 8 not reproduced. `entry.py all` passes (0 errors, notebook ran in 27 min) and the handover is built in `executed/johnson-2017/handover/`. Nothing is committed.

**1. Outcomes** ("assumed" means the outcome rests on a choice the paper leaves open)

| claim | outcome | assumed |
|---|---|---|
| cohort-and-trials | reproduced: 187.3 trials; lesioned hemifield 94.4 ± 21.1 [55–119]; intact 93.0 ± 22.1 [51–120] | |
| demographics-matched | reproduced | |
| patient-factors-no-effect | reproduced (smallest p = 0.106) | |
| table-s1-patient-accuracy | partially reproduced: 20 of 28 values within 0.02 | |
| accuracy-patients-impaired | partially reproduced: linear model p = 7.6e-4; F not 16.77 under any reading | yes |
| patients-above-chance | reproduced: t = 14.13 | |
| accuracy-no-hemifield-condition-effect | reproduced (linear model) | yes |
| erp-lesioned-maintenance | reproduced: p = 0.006 anterior, p = 0.014 over P6/P8/P10/PO8 | yes |
| erp-processing-interaction | not reproduced (p = 0.294) | |
| erp-intact-none | reproduced | |
| baseline-spectral-interaction | reproduced: p = 0.004 over AF3/F3/F5 | |
| baseline-no-group-effect | partially reproduced: no cluster, but 476 points with uncorrected p < 0.05 | |
| power-anterior-theta-controls | reproduced: maximum Z 3.74 in processing | yes |
| power-posterior-alphabeta | not reproduced | |
| power-lowtheta-interaction | partially reproduced: lesioned hemifield p = 0.040; intact p = 0.134 | yes |
| power-no-group-main-effect | reproduced | |
| psi-deltatheta-bottomup-encoding | not reproduced | |
| psi-deltatheta-pfc-lead-controls | not reproduced | |
| psi-deltatheta-group-clusters | not reproduced | |
| psi-network-degree | not reproduced | |
| psi-alphabeta-bottomup | not reproduced (the paper's code as written does reproduce it) | yes |
| psi-alphabeta-no-group-effect | not reproduced | yes |

**2. Dataset**

Version: CRCNS data sets are not versioned, so the files under `pfc-5/live/` are pinned by the MD5 sums the notebook prints.

What I found (recorded as findings):
- **Processing segment out of order:** in all 34 subjects it is stored in a different trial order from the other segments. `erp_compute.m` and `tfr_compute.m` select its trials with the encoding segment's indices, so they average the wrong trials.
- **Hemifield code:** the derived column the descriptor calls "1 intact / 2 lesioned" equals the trial table's left/right column in every trial of every subject. The docs summary, which equals Table S1, contradicts the paper's own note on which hemifield is lesioned. Which 10 controls were swapped across the midline is not recorded.
- **No buffers on the segments:** they are 500, 1500 and 900 ms long. FieldTrip's 3/f windows therefore leave no baseline power below 7 Hz and no delta-theta PSI at all.
- **PSI code:** `psianalysis.m` leaves out the complex conjugate. The result depends only on channel B's phase (up to sign), so it is not Nolte's PSI.
- **Other file problems:**
  - Channel order differs in 13 subjects.
  - Six two-block subjects have trial tables whose trial numbers overlap; I linked trials by trial number plus response time.
  - The pretrial `fsample` field reads 255.64 Hz.
  - The descriptor says 6 male patients; the summary file has 5.
- **Clock check:** I could not establish that the segments share the trial table's clock from the ERP.

Assumptions:
- Hemifield coding: the descriptor's.
- Window edges: windows may run into the zero padding (the only reading under which the 3–4 Hz results exist).
- Low-theta test: run on the 3–4 Hz mean.
- Accuracy model: linear, as the Methods say.
- PSI: the code's structure with the conjugate restored.
- Clustering: the code's per-seed PSI test.

I replaced the bootstrap Z with its exact expectation. Every alternative reading is run and shown in the notebook.

Questions for the paper's authors (in the record's findings):
- Were the analyses run on segments with buffers? This is the only one filed as a `methods_unavailable` question.
- Which hemifield code is right?
- Was the missing conjugate in `psianalysis.m` intended?
- Which controls were swapped?

The last three are written as statements in the findings, not as explicit questions. I asked a reader nothing.

**3. Where the protocol was unclear or wrong**
1. `entry.py lock` writes `python: "3.13"` into `entry.yaml`, and the entry schema then rejects it. I deleted the line; the tool falls back to the lock file's version.
2. `archives.md` covers zips only. pfc-5 is tar.gz, which has to be read in order, and fsspec range reads were 4× slower. I streamed each file with urllib, keeping nothing on disk.
3. The protocol has no rule for code that is wrong, as opposed to code that disagrees with the Methods. I applied "Methods first" and ran the literal code as a variant.
4. Absence claims are to be judged "on the paper's test", but that test's clustering was itself open. I followed the deposited code, which the claims file allows.
5. When an expected value fails (F = 16.77) but the criterion's condition passes, the protocol doesn't say which wins. I chose partially reproduced.
6. The suggested clock check assumes trial-level decoding is available. Here it gave nothing conclusive, and I recorded it as not established.
7. "Trust the data" can't settle a conflict between two of the data set's own documents. I adopted the descriptor's coding as an assumption.
8. The "under 10 minutes" target can't be met: each run has to stream about 20 GB (19 min), and caching between runs isn't allowed.

**4. Runtime and failures**

The clean run took 27.3 min end to end (notebook 27.0 min, peak memory 3.4 GB). The first full development pass failed after 18 min on two-block subjects; fixed. The full binomial accuracy model did not converge; the record says so. The untracked `scripts` entry at the repo root is a device file that predates this run and isn't mine.

## End of run

97 turns, 129 minutes, $10.82 at API prices, result: success.
